# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown", "pymupdf"]
# ///
"""Build the data of the card dashboard, internal and public.

Single-file script (PEP 723 regime). Data flow: the source table in
knowledge/quellen.md gives the metadata of every original in sources/; the
originals (PDF text page by page, or Markdown), their summaries in
sources/summaries/, the documents in knowledge/, the notes and protocols in
notizen/ and protokolle/ and the project documents in projekte/ are read.
Everything goes into dashboard/data.js for the local dashboard; a curated part
(source metadata, summaries, the rules of the guidelines) goes into
public/data.js. Both files share one schema, and one frontend (index.html,
app.js, style.css, assets/ in dashboard/) serves both: the build copies it
into public/, so public/ stays a standalone folder. The frontend shows only
what its data holds, so the public copy has no reader and no notes.

Design decisions:
- The data is a .js file assigning a global, not JSON, because the dashboard
  is opened by double click from the file system, where browsers block
  fetch() of local JSON.
- Markdown is rendered to HTML here, so the browser needs no Markdown library.
  The parser treats raw HTML as text (only <br> survives, which the source
  table uses), because summaries are agent-written text. Escaping happens in
  the parser rather than before it, so `a<b` in a code span is escaped once.
- PDF text stays plain text; the dashboard inserts it with textContent.
  Running headers and footers (blocks repeated on most pages) are dropped,
  because they dominated search snippets. Of a table of contents only the
  dot leaders are dropped ("Introduction ..... 8" becomes "Introduction 8"),
  not its entries: dropping whole entries left contents pages empty in the
  reader. The page text is both reader and search text, so the entries stay
  findable; a contents page can rank among the pages with a find.
- Links to stored sources, summaries and knowledge documents become links
  inside the dashboard. A locator such as "PDF p. 12" in the link text opens
  the source at that page. A link that resolves to nothing is reported.
- Every cited block (paragraph, list item, table row) in a claim document gets
  an id. A block that states a status (Pflicht, Vorgabe, ...) becomes a rule
  entry with its status, goal, section and sources at their pages; cited
  explanations without a status stay text of the reader. The numbering counts
  every cited block, so rule ids stay stable when an explanation is added.
  Which rules rest on a source, the frontend derives from them.
- Headings of documents get ids ("h-" and a slug), and a link to a section
  ("[[governance-entwurf#4 Datenklassen]]") carries that id, so the reader
  opens the document at the section.

Errors (an original without a row in quellen.md, a row without a file, a link
that is no http(s) URL, an unreadable PDF, an unresolved internal link, a file
name used in two folders) are
collected, printed at the end and make the exit code 1. The local data file is
still written. The public data file and the frontend copy are written only
when the public checks pass (no local link, no image, no link to a note or
protocol, no path out of the folder in the frontend); otherwise the old files
stay in place.

Usage: uv run scripts/build_dashboard.py
"""

import html
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import markdown
import pymupdf as fitz
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
SOURCES = ROOT / "sources"
SUMMARIES = SOURCES / "summaries"
DASHBOARD = ROOT / "dashboard"
OUT = DASHBOARD / "data.js"
PUBLIC = ROOT / "public"
PUBLIC_OUT = PUBLIC / "data.js"
# The shared frontend; dashboard/ is its source, public/ gets a copy.
FRONTEND = ("index.html", "app.js", "style.css")
FRONTEND_ASSETS = "assets"
# The public build shows only the rules of the guidelines, by field.
PUBLIC_RULES = "k-leitlinien-dhcraft"
PUBLIC_FIELDS = ("Projekte", "Forschung", "Programmierung", "Organisation")
# Short names of the rule documents for filters and card groups.
RULE_DOC_LABELS = {
    "k-leitlinien-dhcraft": "Leitlinien",
    "k-governance-entwurf": "Governance-Entwurf",
}  # in display order
# Further local pages linked from the internal dashboard, if present.
LOCAL_PAGES = (("northwind/index.html", "Northwind-Umsatz"),)

SOURCE_COLUMNS = ("File", "Title", "Publisher", "Date", "Link", "Category")
# Same split as scripts/check_kb.py: these documents make no claims.
NON_CLAIM_DOCS = frozenset({"INDEX.md", "project.md", "quellen.md", "journal.md"})
STATUSES = ("Pflicht", "Vorgabe", "Empfehlung", "Ableitung", "Befund")

LINK_TARGET = re.compile(r"\]\(([^)\s]+)\)")
ANCHOR = re.compile(r'<a href="([^"]*)"[^>]*>(.*?)</a>', flags=re.S)
# "PDF p. 12", "PDF pp. 26, 36", "PDF S. 4": the first number is the page.
PAGE = re.compile(r"PDF (?:p|pp|S)\.\s*(\d+)")
FIELD = r"[A-Z][A-Za-z ]{1,24}: "
FIELD_LINES = re.compile(rf"^({FIELD}.*)\n(?={FIELD})", flags=re.M)
# Header fields of a summary that the dashboard shows in its own header.
SUMMARY_FIELDS = re.compile(
    r"^(Publisher|Date|Original|Bindingness|Note): (.*)\n", re.M
)
CITED_BLOCK = re.compile(r"<(li|tr|p)>(.*?)</\1>", flags=re.S)
INTERNAL_LINK = r'<a href="#" data-doc="[^"]+"[^>]*>.*?</a>'
CITATION = re.compile(
    r'<a href="#" data-doc="([^"]+)"(?: data-page="(\d+)")?(?: data-at="[^"]*")?>(.*?)</a>',
    flags=re.S,
)
WIKILINK = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:#([^\]|]*))?(?:\|([^\]]*))?\]\]")
NOTE_FOLDERS = ("notizen", "protokolle", "projekte")
NOTE_LABELS = {
    "protokoll": "Protokoll",
    "angebot": "Angebot",
    "kundenprojekt": "Projekt",
}
STATUS_NOTE = re.compile(rf"\s*\(({'|'.join(STATUSES)})\b[^)]*\)")
GOALS = re.compile(
    r"(?:regelkonform|sicher|nachprüfbar)(?:\s*(?:,|und)\s*(?:regelkonform|sicher|nachprüfbar))*"
)
# Dot leaders of a table of contents ("Introduction ........ 8").
LEADER = re.compile(r"\s*(?:(?:\.\s?){6,}|…{3,}|_{6,})\s*")


def _table_rows(text: str) -> list[list[str]]:
    """Rows of the first table only, as the skill's check_kb.py reads them;
    later tables (notes, excluded sources) are no source rows."""
    rows: list[list[str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            if rows:
                break
            continue
        if not re.fullmatch(r"\|[\s:|-]+\|", line):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def _nfc(text: str) -> str:
    # PDF text may carry decomposed umlauts; NFC keeps the client-side
    # folding of the search length-preserving.
    return unicodedata.normalize("NFC", text)


def _strip_frontmatter(text: str) -> str:
    """Drop an Obsidian frontmatter block; it is vault metadata, not content."""
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)


class _BreakTag(InlineProcessor):
    def handleMatch(self, m: re.Match[str], data: str) -> tuple[str, int, int]:
        # Stored verbatim, as the removed raw-HTML pattern stored it.
        return self.md.htmlStash.store(m.group(0)), m.start(0), m.end(0)


class _NoRawHtml(Extension):
    """Render raw HTML as text; only <br> (source table) stays a tag.

    Summaries are agent-written, so raw HTML is a trust boundary. Taking the
    raw-HTML patterns out of the parser escapes tags in running text while
    code spans and code blocks keep their own single escaping. Autolinks to
    http(s) stay; mail autolinks are dropped like any other raw tag.
    """

    def extendMarkdown(self, md: markdown.Markdown) -> None:
        md.preprocessors.deregister("html_block")
        md.inlinePatterns.deregister("html")
        md.inlinePatterns.deregister("automail")
        md.inlinePatterns.register(_BreakTag(r"<br\s*/?>", md), "br_tag", 90)


def _render(text: str) -> str:
    # Header blocks ("Publisher: ...", "Date: ...") keep one field per line.
    text = FIELD_LINES.sub("\\1  \n", text)
    rendered = markdown.markdown(
        text, extensions=["tables", "sane_lists", _NoRawHtml()]
    )
    # Wide tables scroll inside a wrapper and keep their table semantics.
    rendered = rendered.replace("<table>", '<div class="table-wrap"><table>')
    return rendered.replace("</table>", "</table></div>")


def _plain(fragment: str) -> str:
    # Inline tags vanish without a gap, block tags separate words.
    text = re.sub(r"</?(?:a|em|strong|code|span)\b[^>]*>", "", fragment)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def _drop_h1(fragment: str) -> str:
    return re.sub(r"^\s*<h1>.*?</h1>\s*", "", fragment, count=1, flags=re.S)


def _demote(fragment: str, levels: int) -> str:
    """Shift headings below the reader's own title and section headings."""
    return re.sub(
        r"<(/?)h([1-6])>",
        lambda m: f"<{m.group(1)}h{min(int(m.group(2)) + levels, 6)}>",
        fragment,
    )


def _slug(text: str) -> str:
    """Id of a heading, the same for its rendered text and a link fragment."""
    return "h-" + "-".join(re.findall(r"\w+", text.lower()))


def _heading_ids(fragment: str) -> str:
    """Give every heading an id, so a link to a section can open it."""
    seen: Counter[str] = Counter()

    def replace(m: re.Match[str]) -> str:
        slug = _slug(_plain(m.group(2)))
        seen[slug] += 1
        if seen[slug] > 1:
            slug = f"{slug}-{seen[slug]}"
        return f'<h{m.group(1)} id="{slug}">{m.group(2)}</h{m.group(1)}>'

    return re.sub(r"<h([1-6])>(.*?)</h\1>", replace, fragment, flags=re.S)


def _changed(path: Path) -> str:
    """Date of the last commit of a knowledge document, else of the file."""
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", path.name],
        cwd=path.parent,
        capture_output=True,
        text=True,
        check=False,
    )
    date = result.stdout.strip()
    if not date:
        date = datetime.fromtimestamp(path.stat().st_mtime, tz=UTC).date().isoformat()
    return date


def _attr(value: str) -> str:
    return html.escape(value, quote=True)


def _source_rows(errors: list[str]) -> dict[str, dict[str, str]]:
    rows = _table_rows((KNOWLEDGE / "quellen.md").read_text(encoding="utf-8"))
    if not rows or tuple(rows[0]) != SOURCE_COLUMNS:
        errors.append(
            "quellen.md: first table must have the columns "
            + " | ".join(SOURCE_COLUMNS)
        )
        return {}
    meta = {}
    for cells in rows[1:]:
        if len(cells) != len(SOURCE_COLUMNS):
            errors.append(
                f"quellen.md: row with {len(cells)} instead of {len(SOURCE_COLUMNS)} cells: {cells[0][:60]}"
            )
            continue
        row = dict(zip(SOURCE_COLUMNS, cells, strict=True))
        target = LINK_TARGET.search(row["File"])
        if not target:
            errors.append(f"quellen.md: row without file link: {row['Title']}")
            continue
        # The link becomes an href in the dashboard; only web URLs pass.
        if not re.match(r"https?://", row["Link"]):
            errors.append(f"quellen.md: link of {row['Title']} is no http(s) URL")
            row["Link"] = ""
        meta[Path(unquote(target.group(1))).name] = row
    return meta


def _page_blocks(page: fitz.Page) -> list[str]:
    """Text blocks of one PDF page, lines joined, hyphenation and leaders undone."""
    blocks = page.get_text(
        "blocks", flags=fitz.TEXT_DEHYPHENATE | fitz.TEXT_PRESERVE_WHITESPACE
    )
    texts = []
    for block in blocks:
        if block[6] != 0:  # image block
            continue
        text = re.sub(r"\s*\n\s*", " ", block[4])
        text = LEADER.sub(" ", text).strip()
        if text:
            texts.append(_nfc(text))
    return texts


def _boilerplate_key(text: str) -> str:
    # Page numbers differ between running headers ("39 / 71"), so digits are
    # ignored when blocks are compared across pages.
    return re.sub(r"\d+", "#", text)


def _pdf_pages(path: Path, errors: list[str]) -> list[str]:
    """Text of each PDF page as paragraphs separated by a blank line."""
    try:
        with fitz.open(path) as document:
            pages = [_page_blocks(page) for page in document]
    except RuntimeError as exc:
        errors.append(f"{path.name}: PDF not readable ({exc})")
        return []
    # A block that recurs on more than half of the pages is a running header
    # or footer. Short documents are left alone.
    counts = Counter(
        key for blocks in pages for key in {_boilerplate_key(b) for b in blocks}
    )
    repeated = (
        {key for key, n in counts.items() if n > len(pages) / 2}
        if len(pages) > 4
        else set()
    )
    return [
        "\n\n".join(b for b in blocks if _boilerplate_key(b) not in repeated)
        for blocks in pages
    ]


def _link_pages(fragment: str, doc_id: str) -> str:
    """Turn page locators in the text of a PDF summary into page links."""
    parts = re.split(r"(<[^>]+>)", fragment)
    inside_link = False
    for index, part in enumerate(parts):
        if part.startswith("<a "):
            inside_link = True
        elif part == "</a>":
            inside_link = False
        elif not part.startswith("<") and not inside_link:
            parts[index] = PAGE.sub(
                lambda m: (
                    f'<a href="#" data-doc="{_attr(doc_id)}" '
                    f'data-page="{m.group(1)}">{m.group(0)}</a>'
                ),
                part,
            )
    return "".join(parts)


def _relink(
    fragment: str,
    base: Path,
    targets: dict[Path, str],
    errors: list[str],
    where: str,
    origin: str = "",
) -> str:
    """Point links at stored files to the dashboard, open external links apart.

    Site-relative links in a stored web page ("/blogs/...") are completed with
    the origin of the page's URL.
    """

    def replace(match: re.Match[str]) -> str:
        href, label = html.unescape(match.group(1)), match.group(2)
        if href.startswith("/") and origin:
            href = origin + href
        if re.match(r"(https?|mailto):", href):
            return f'<a href="{_attr(href)}" target="_blank" rel="noopener">{label}</a>'
        if href.startswith("#"):
            return label
        href, _, fragment = href.partition("#")
        path = (base / unquote(href)).resolve()
        if path.is_dir():
            # Folder links ("../sources/") have no page in the dashboard.
            return label
        doc_id = targets.get(path)
        if doc_id is None and path.is_file() and path.is_relative_to(ROOT):
            # Other files of the repository open as files.
            href = "../" + path.relative_to(ROOT).as_posix()
            return f'<a href="{_attr(href)}" target="_blank" rel="noopener">{label}</a>'
        if doc_id is None:
            errors.append(f"{where}: link to {href} matches no document")
            return label
        page = PAGE.search(_plain(label))
        page_attr = f' data-page="{page.group(1)}"' if page else ""
        # A section of a document; a fragment of a source ("#page=3") is none.
        at = _slug(unquote(fragment)) if fragment and doc_id[:2] in ("k-", "n-") else ""
        at_attr = f' data-at="{_attr(at)}"' if at else ""
        return f'<a href="#" data-doc="{_attr(doc_id)}"{page_attr}{at_attr}>{label}</a>'

    return ANCHOR.sub(replace, fragment)


def _mark_citations(body: str, doc: dict, rules: list[dict]) -> str:
    """Give every cited block of a claim document an id and record it.

    Each block becomes a rule entry: the text without its citations, the
    status, goal, section heading and field, and its sources at their pages.
    """
    headings = [
        (m.start(), _plain(m.group(1)))
        for m in re.finditer(r"<h[2-6]>(.*?)</h[2-6]>", body, flags=re.S)
    ]
    fields = [
        (m.start(), _plain(m.group(1)))
        for m in re.finditer(r"<h2>(.*?)</h2>", body, flags=re.S)
    ]
    number = 0
    claims_start = fields[0][0] if fields else len(body)

    def mark(match: re.Match[str]) -> str:
        nonlocal number
        tag, inner = match.group(1), match.group(2)
        if 'data-doc="' not in inner or match.start() < claims_start:
            return match.group(0)
        number += 1
        anchor = f"c-{number}"
        marked = f'<{tag} id="{anchor}">{inner}</{tag}>'
        text = re.sub(rf"\(\s*(?:{INTERNAL_LINK}[;,\s]*)+\)", "", inner, flags=re.S)
        text = re.sub(INTERNAL_LINK, "", text, flags=re.S)
        status_cell = ""
        goal = ""
        if tag == "tr":
            # Rule tables keep goal and status in cells of their own; both
            # are shown apart, so they are dropped from the text.
            cells = [_plain(c) for c in re.findall(r"<td>(.*?)</td>", text, flags=re.S)]
            kept = []
            for cell in cells:
                if cell in STATUSES:
                    status_cell = cell
                elif GOALS.fullmatch(cell):
                    goal = cell
                elif cell:
                    kept.append(cell)
            text = " ".join(c if c.endswith((".", ":", "?")) else c + ";" for c in kept)
        # The status is shown apart; drop it and the gaps left by citations.
        text = re.sub(STATUS_NOTE, "", _plain(text))
        text = re.sub(r"\s+([.,;:])", r"\1", text).rstrip(" ;,")
        found = re.search(STATUS_NOTE, _plain(inner))
        status = status_cell or (found.group(1) if found else "")
        if not status:
            # A cited explanation (a definition, the sources outside the
            # Leitfrage) is no rule; it stays in the reader.
            return marked
        section = next((t for pos, t in reversed(headings) if pos < match.start()), "")
        field = next((t for pos, t in reversed(fields) if pos < match.start()), "")
        pages: dict[str, set[int]] = {}
        labels: dict[str, str] = {}
        for target, page, label in CITATION.findall(inner):
            target = html.unescape(target)
            pages.setdefault(target, set())
            # The short name of a citation ends at the first comma.
            labels.setdefault(target, _plain(label).split(",", 1)[0].strip())
            if page:
                pages[target].add(int(page))
        rules.append(
            {
                "id": f"r-{doc['id'][2:]}-{anchor}",
                "text": text,
                "status": status,
                "goal": goal,
                "section": section,
                "field": field,
                "ruleDoc": doc["id"],
                "at": anchor,
                "sources": [
                    {"id": target, "label": labels[target], "pages": sorted(numbers)}
                    for target, numbers in pages.items()
                ],
            }
        )
        return marked

    return CITED_BLOCK.sub(mark, body)


def _source_doc(
    path: Path, row: dict[str, str], targets: dict[Path, str], errors: list[str]
) -> dict:
    doc = {
        "id": path.stem,
        "kind": "source",
        "role": "source",
        "title": row["Title"],
        "publisher": row["Publisher"],
        "date": row["Date"],
        "year": row["Date"][:4],
        "category": row["Category"],
        "file": f"../sources/{path.name}",
        "url": row["Link"],
        "binding": "",
        "dateNote": "",
        "summary": "",
        "body": "",
        "pages": [],
    }
    summary_path = SUMMARIES / f"{path.stem}.md"
    if summary_path.exists():
        text = summary_path.read_text(encoding="utf-8")
        fields = dict(SUMMARY_FIELDS.findall(text))
        doc["binding"] = fields.get("Bindingness", "")
        doc["dateNote"] = fields.get("Date", "")
        doc["note"] = fields.get("Note", "")
        summary = _render(SUMMARY_FIELDS.sub("", text))
        summary = _drop_h1(
            _relink(summary, SUMMARIES, targets, errors, summary_path.name)
        )
        doc["summary"] = summary
    if path.suffix.lower() == ".pdf":
        doc["pages"] = _pdf_pages(path, errors)
        doc["summary"] = _link_pages(doc["summary"], path.stem)
    else:
        parts = urlsplit(row["Link"])
        origin = f"{parts.scheme}://{parts.netloc}" if parts.netloc else ""
        body = _render(_nfc(path.read_text(encoding="utf-8")))
        doc["body"] = _relink(body, SOURCES, targets, errors, path.name, origin)
    return doc


def _wikilinks(text: str, base: Path, files: dict[str, Path]) -> str:
    """Turn Obsidian Wikilinks into Markdown links that _relink resolves."""

    def replace(match: re.Match[str]) -> str:
        name, heading, alias = match.group(1).strip(), match.group(2), match.group(3)
        label = alias or (f"{name}, {heading}" if heading else name)
        path = files.get(name.lower())
        if path is None:
            return label
        href = Path(os.path.relpath(path, base)).as_posix()
        if heading:
            href += "#" + quote(heading.strip())
        return f"[{label}]({href})"

    return WIKILINK.sub(replace, text)


def _note_doc(
    path: Path, targets: dict[Path, str], errors: list[str], files: dict[str, Path]
) -> dict:
    raw = path.read_text(encoding="utf-8")
    kind = re.search(r"^type:\s*(\S+)", raw, flags=re.M)
    text = _strip_frontmatter(raw)
    title = re.search(r"^# (.+)$", text, flags=re.M)
    dated = re.match(r"\d{4}-\d{2}-\d{2}", path.stem)
    date = dated.group(0) if dated else _changed(path)
    body = _render(_wikilinks(text, path.parent, files))
    return {
        "id": f"n-{path.stem}",
        "kind": "note",
        "role": "note",
        "title": title.group(1).strip() if title else path.stem,
        "publisher": NOTE_LABELS.get(kind.group(1) if kind else "", "Notiz"),
        "date": date,
        "year": date[:4],
        "category": "",
        "file": "../" + path.relative_to(ROOT).as_posix(),
        "url": "",
        "binding": "",
        "dateNote": "",
        "summary": "",
        "pages": [],
        "body": _drop_h1(_relink(body, path.parent, targets, errors, path.name)),
    }


def _knowledge_doc(
    path: Path,
    targets: dict[Path, str],
    errors: list[str],
    rules: list[dict],
) -> dict:
    raw = path.read_text(encoding="utf-8")
    kind = re.search(r"^type:\s*(\S+)", raw, flags=re.M)
    text = _strip_frontmatter(raw)
    title = re.search(r"^# (.+)$", text, flags=re.M)
    date = _changed(path)
    # Rule documents are the working documents; the others (INDEX, project,
    # sources list, journal, outlines, subfolders such as northwind/) maintain
    # or use the base and yield no rule entries.
    is_rules = (
        path.parent == KNOWLEDGE
        and path.name not in NON_CLAIM_DOCS
        and not (kind and kind.group(1) == "gliederung")
    )
    doc = {
        "id": f"k-{path.stem}",
        "kind": "knowledge",
        "role": "work" if is_rules else "meta",
        "title": title.group(1).strip() if title else path.stem,
        "publisher": "DHCraft",
        "date": date,
        "year": date[:4],
        "category": "",
        "file": "../" + path.relative_to(ROOT).as_posix(),
        "url": "",
        "binding": "",
        "dateNote": "",
        "summary": "",
        "pages": [],
    }
    body = _drop_h1(_relink(_render(text), path.parent, targets, errors, path.name))
    if doc["role"] == "work":
        body = _mark_citations(body, doc, rules)
    doc["body"] = body
    return doc


def build() -> tuple[dict, list[str]]:
    errors: list[str] = []
    meta = _source_rows(errors)
    originals = sorted(
        p for p in SOURCES.iterdir() if p.is_file() and not p.name.startswith(".")
    )
    knowledge = sorted(KNOWLEDGE.rglob("*.md"))

    targets: dict[Path, str] = {}
    for path in originals:
        targets[path.resolve()] = path.stem
        targets[(SUMMARIES / f"{path.stem}.md").resolve()] = path.stem
    for path in knowledge:
        targets[path.resolve()] = f"k-{path.stem}"
    # Personal notes and protocols; the templates are no notes.
    notes = sorted(
        p
        for folder in NOTE_FOLDERS
        for p in (ROOT / folder).rglob("*.md")
        if "_vorlagen" not in p.parts
    )
    for path in notes:
        targets[path.resolve()] = f"n-{path.stem}"
    # Wikilinks resolve by file name, as in Obsidian. A name used twice would
    # let one file win silently (and give two documents one id), so it is an
    # error.
    files: dict[str, Path] = {}
    for path in [
        *originals,
        *knowledge,
        *notes,
        ROOT / "HOME.md",
        ROOT / "ACTIVE-WORK.md",
    ]:
        first = files.setdefault(path.stem.lower(), path)
        if first != path:
            errors.append(
                f"{path.relative_to(ROOT).as_posix()}: same file name as "
                f"{first.relative_to(ROOT).as_posix()}, links to it are ambiguous"
            )

    for name in sorted(set(meta) - {p.name for p in originals}):
        errors.append(f"quellen.md: {name} is listed but not stored in sources/")

    docs = []
    for path in originals:
        row = meta.get(path.name)
        if row is None:
            errors.append(f"{path.name}: no row in quellen.md")
            continue
        docs.append(_source_doc(path, row, targets, errors))

    rules: list[dict] = []
    docs.extend(_knowledge_doc(p, targets, errors, rules) for p in knowledge)
    docs.extend(_note_doc(p, targets, errors, files) for p in notes)

    for doc in docs:
        # The card text: the start of the summary, or of the document.
        doc["abstract"] = (
            _abstract(doc["summary"])
            if doc["summary"]
            else _abstract(doc["body"], lead=True)
        )
        # Plain text for search and snippets, kept apart from the HTML.
        doc["summaryText"] = _plain(doc["summary"])
        doc["bodyText"] = _plain(doc["body"])
        # Reader: h2 title, h3 section labels, content below. Knowledge
        # documents have no section label, so their headings move by one.
        levels = 2 if doc["kind"] == "source" else 1
        doc["summary"] = _demote(doc["summary"], levels)
        doc["body"] = _heading_ids(_demote(doc["body"], levels))
    # The guidelines first, as the labels list them; others after them.
    order = list(RULE_DOC_LABELS)
    rule_docs = sorted(
        (
            {"id": doc["id"], "label": RULE_DOC_LABELS.get(doc["id"], doc["title"])}
            for doc in docs
            if doc["role"] == "work"
        ),
        key=lambda d: order.index(d["id"]) if d["id"] in order else len(order),
    )
    # Every rule card shows a status; a block without one must not get here.
    errors += [
        f"{rule['id']}: rule without a status from {', '.join(STATUSES)}"
        for rule in rules
        if rule["status"] not in STATUSES
    ]
    links = [
        {"href": href, "label": label}
        for href, label in LOCAL_PAGES
        if (DASHBOARD / href).is_file()
    ]
    data = {
        "scope": "internal",
        "generated": datetime.now(tz=UTC).date().isoformat(),
        "fields": list(PUBLIC_FIELDS),
        "ruleDocs": rule_docs,
        "links": links,
        "docs": docs,
        "rules": rules,
    }
    return data, errors


def _abstract(summary: str, lead: bool = False) -> str:
    """First sentences of a summary's first paragraph, for a card.

    With lead, the first paragraph of a document, wherever it stands.
    """
    # The first paragraph under the first heading; a preamble note before
    # it (such as an approved exception) is no description of the source.
    first = (
        None
        if lead
        else re.search(
            r"</h\d>\s*(?:<p>|<ul>\s*<li>)(.*?)</(?:p|li)>", summary, flags=re.S
        )
    ) or re.search(r"<p>(.*?)</p>", summary, flags=re.S)
    text = _plain(first.group(1)) if first else ""
    sentences = re.findall(r".+?[.!?](?=\s+[A-ZÄÖÜ\"(]|$)", text)
    out = ""
    for sentence in sentences:
        out = f"{out} {sentence.strip()}".strip()
        if len(out) >= 90:
            break
    return out or text


def build_public(data: dict) -> tuple[dict, list[str]]:
    """Curated data for the public copy of the dashboard in public/.

    Same schema as the internal data. Public are the source metadata, the
    summaries (own text), the rules of leitlinien-dhcraft.md and links to the
    originals at their publishers. Not public are the stored originals and
    their full text, the governance draft, the other knowledge documents,
    notes and protocols, and the position of a rule in its document.
    """
    rules = [
        {
            "id": rule["id"],
            "text": rule["text"],
            "status": rule["status"],
            "goal": rule["goal"],
            "field": rule["field"],
            "section": rule["section"],
            "ruleDoc": rule["ruleDoc"],
            "sources": rule["sources"],
        }
        for rule in data["rules"]
        if rule["ruleDoc"] == PUBLIC_RULES and rule["field"] in PUBLIC_FIELDS
    ]
    errors: list[str] = []
    sources = []
    for doc in data["docs"]:
        if doc["kind"] != "source":
            continue
        if 'data-doc="n-' in doc["summary"]:
            errors.append(f"public: summary of {doc['id']} links to a note or protocol")
        # Links inside the base point to files that stay private; their
        # labels remain as text. Images would load files or third parties.
        summary = re.sub(r"<img\b[^>]*>", "", doc["summary"])
        summary = re.sub(
            r'<a href="#" data-doc="[^"]*"[^>]*>(.*?)</a>',
            r"\1",
            summary,
            flags=re.S,
        )
        sources.append(
            {
                "id": doc["id"],
                "kind": "source",
                "role": "source",
                "title": doc["title"],
                "publisher": doc["publisher"],
                "date": doc["date"],
                "year": doc["year"],
                "category": doc["category"],
                "url": doc["url"],
                "binding": doc["binding"],
                "dateNote": doc["dateNote"],
                "note": doc.get("note", ""),
                "abstract": doc["abstract"],
                "summary": summary,
                "summaryText": _plain(summary),
            }
        )
    payload = {
        "scope": "public",
        "generated": data["generated"],
        "fields": data["fields"],
        "ruleDocs": [d for d in data["ruleDocs"] if d["id"] == PUBLIC_RULES],
        "links": [],
        "docs": sources,
        "rules": rules,
    }
    text = json.dumps(payload, ensure_ascii=False)
    errors += [
        f"public data contains a local link {m.group(0)}"
        for m in re.finditer(r'href=\\"(?!https?:)[^"\\]*', text)
    ]
    errors += [
        f"public data contains an image {m.group(0)}"
        for m in re.finditer(r"<img\b", text)
    ]
    # The copied frontend must not reach out of public/ (sources, notes).
    for name in FRONTEND:
        if "../" in (DASHBOARD / name).read_text(encoding="utf-8"):
            errors.append(
                f"public: dashboard/{name} refers to a path outside its folder"
            )
    return payload, errors


def _copy_frontend() -> None:
    """Copy the shared frontend into public/, replacing the previous copy."""
    for name in FRONTEND:
        shutil.copy2(DASHBOARD / name, PUBLIC / name)
    shutil.copytree(
        DASHBOARD / FRONTEND_ASSETS, PUBLIC / FRONTEND_ASSETS, dirs_exist_ok=True
    )


def _write(path: Path, name: str, data: dict) -> None:
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    path.write_text(
        f"// Generated by scripts/build_dashboard.py; do not edit.\nwindow.{name} = {payload};\n",
        encoding="utf-8",
    )


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    data, errors = build()
    public, public_errors = build_public(data)
    errors += public_errors
    if public_errors:
        print(f"{PUBLIC_OUT.relative_to(ROOT)} not written, see the errors below")
    else:
        _write(PUBLIC_OUT, "KB_DATA", public)
        _copy_frontend()
        print(
            f"{PUBLIC_OUT.relative_to(ROOT)}: {len(public['docs'])} sources, "
            f"{len(public['rules'])} rules; frontend copied from dashboard/"
        )
    _write(OUT, "KB_DATA", data)
    kinds = Counter(doc["kind"] for doc in data["docs"])
    print(
        f"{OUT.relative_to(ROOT)}: {kinds['source']} sources, "
        f"{kinds['knowledge']} knowledge documents, {kinds['note']} notes, "
        f"{len(data['rules'])} rules"
    )
    for error in errors:
        print(f"ERROR {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
