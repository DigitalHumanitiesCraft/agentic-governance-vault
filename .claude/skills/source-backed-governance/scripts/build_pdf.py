# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown"]
# ///
"""Render a source-backed Markdown document (e.g. a governance draft) as a readable A4 PDF.

Single-file script (PEP 723 regime). Data flow: the Markdown draft and the
source table in knowledge/quellen.md are converted to one HTML page in the
output folder, which headless Chrome prints to PDF.

Design decisions, from a page-by-page readability review:
- Each rule is set as a two-column item. The status (Pflicht, Vorgabe,
  Empfehlung, Ableitung, Befund) stands as a quiet word in a left column, and the
  sources follow in a separate small line. Coloured pills inside the
  sentence made every line look busy and were removed.
- Citations are grouped per source ("[3] S. 4, 7"). Page numbers refer to
  the PDF file of the source ("PDF p. 4" and "PDF S. 4" both work). Section
  locators of web pages are long headings and are dropped in the PDF; the
  Markdown draft keeps them.
- Tables: a last column headed Grundlage, Basis, Quellen or Sources that
  holds only source links is folded into the cell before it.
- The PDF text (headings, legend, notes, hyphenation) is German.
- The source list links the host name instead of printing full URLs.
- Body text is set in a serif face at a line length of about 80 characters,
  with German hyphenation, because the document is read in print.
- Chrome or Edge is used because they are widely installed and support
  @page margin boxes for page numbers; no extra PDF library needed.

Usage:
  python build_pdf.py --root <repo> --title "..." [--subtitle "..."] [--meta "line" ...]
      [--footer "..."] [--logo path.png] [--draft knowledge/governance-entwurf.md]
      [--out output/] [--pdf-name name.pdf] [--drop-first-paragraph]
The root holds knowledge/quellen.md and sources/; the draft cites ../sources/<file>.
"""

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

import markdown

BROWSER_COMMANDS = ("chrome", "msedge", "google-chrome", "chromium", "chromium-browser")
BROWSER_PATHS = (
    Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
    Path("C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
    Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe",
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
)
# Status in parentheses with an optional qualifier, e.g. "(Pflicht für den
# Anbieter)" or "(Pflicht ab 28.06.2025)".
STATUS_RE = re.compile(
    r"\s*\((Pflicht|Vorgabe|Empfehlung|Ableitung|Befund)( [^()]+)?\)"
)
BASIS_HEADERS = ("Grundlage", "Basis", "Quellen", "Sources")
LINK = r'<a href="\.\./sources/[^"]+">[^<]+</a>'
CITE_GROUP_RE = re.compile(rf"\s*\(({LINK}(?:;\s*{LINK})*)\)")
LINK_RE = re.compile(r'<a href="\.\./sources/([^"]+)">([^<]+)</a>')
STATUS_TEXT = {
    "Pflicht": "folgt aus dem Gesetz",
    "Vorgabe": "bindende Regel außerhalb des Gesetzes, etwa eines Förderers, einer Norm oder der Organisation",
    "Empfehlung": "nicht bindende Leitlinie",
    "Ableitung": "Folgerung, die die Organisation aus den Quellen zieht",
    "Befund": "Ergebnis einer empirischen Studie",
}

CSS = """
@page { size: A4; margin: 24mm 25mm 22mm 25mm;
  @bottom-left { content: "__FOOTER__"; font: 7.5pt 'Segoe UI'; color: #8b909a; }
  @bottom-right { content: counter(page); font: 7.5pt 'Segoe UI'; color: #8b909a; } }
@page :first { @bottom-left { content: none; } @bottom-right { content: none; } }
:root { --ink: #1f2430; --head: #17213a; --muted: #6a707c; --line: #dfe1e6; }
html { hyphens: auto; }
body { font-family: Cambria, Georgia, serif; font-size: 10.5pt; line-height: 1.55; color: var(--ink); margin: 0; }
h1, h2, h3, .label, .cites, th, .cover, .legend, .sources, .note { font-family: 'Segoe UI', sans-serif; }
.cover { height: 249mm; display: flex; flex-direction: column; page-break-after: always; }
.cover img { width: 26mm; }
.cover h1 { font-size: 26pt; line-height: 1.2; color: var(--head); margin: 70mm 0 5mm; font-weight: 600; }
.cover .sub { font-size: 12pt; line-height: 1.5; color: var(--muted); max-width: 125mm; }
.cover .meta { margin-top: auto; font-size: 9pt; color: var(--muted); line-height: 1.6; }
h2 { font-size: 14pt; font-weight: 600; color: var(--head); margin: 10mm 0 3.5mm; break-after: avoid; }
h3 { font-size: 11pt; font-weight: 600; color: var(--head); margin: 6mm 0 2.5mm; break-after: avoid; }
p { margin: 0 0 3mm; }
.intro p { margin-bottom: 3mm; }
.legend { margin: 5mm 0 2mm; padding-top: 3mm; border-top: 1px solid var(--line); font-size: 8.8pt; color: var(--muted); }
.legend div { display: grid; grid-template-columns: 24mm 1fr; margin-bottom: 1mm; }
ul.rules { list-style: none; padding: 0; margin: 0 0 3mm; }
ul.rules li { display: grid; grid-template-columns: 24mm 1fr; column-gap: 0; padding: 1.8mm 0; border-top: 1px solid var(--line); break-inside: avoid; }
ul.rules li:first-child { border-top: none; }
ul.rules li.plain { display: list-item; list-style: disc; margin-left: 29mm; padding: 1mm 0; border-top: none; }
.label { font-size: 8pt; font-weight: 600; color: var(--muted); padding-top: 0.6mm; }
.label.Pflicht, .label.Vorgabe { color: var(--head); }
.cites { display: block; margin-top: 0.8mm; font-size: 7.6pt; color: var(--muted); }
table { width: 100%; border-collapse: collapse; margin: 2mm 0 4mm; font-size: 9.3pt; }
th { text-align: left; font-size: 8pt; font-weight: 600; color: var(--muted); padding: 1.5mm 2mm 1.5mm 0; border-bottom: 1px solid var(--head); }
td { vertical-align: top; padding: 2.2mm 3mm 2.2mm 0; border-bottom: 1px solid var(--line); }
td:first-child { font-weight: 600; }
tr { break-inside: avoid; }
.inline-status { display: block; margin-top: 0.8mm; font-family: 'Segoe UI', sans-serif; font-size: 8pt; font-weight: 600; color: var(--muted); }
.sources { font-size: 8.3pt; line-height: 1.45; list-style: none; padding: 0; }
.sources li { display: grid; grid-template-columns: 8mm 1fr; margin-bottom: 1.4mm; break-inside: avoid; }
.sources a { color: var(--head); text-decoration: none; border-bottom: 1px solid var(--line); }
.note { font-size: 8.3pt; color: var(--muted); }
"""


def _strip_frontmatter(text: str) -> str:
    """Drop an Obsidian frontmatter block; it is vault metadata, not content."""
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)


def _find_browser() -> Path:
    for command in BROWSER_COMMANDS:
        found = shutil.which(command)
        if found:
            return Path(found)
    for path in BROWSER_PATHS:
        if path.exists():
            return path
    sys.exit(
        "No Chrome, Edge or Chromium found; install one or add it to BROWSER_PATHS."
    )


def _source_table(path: Path) -> dict[str, dict[str, str]]:
    """Map source file name to title, publisher, date and URL from quellen.md."""
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        # Key by the linked file name, so the link text may be anything.
        found = re.match(r"\| \[[^\]]+\]\(\.\./sources/([^)]+)\)", line) or re.match(
            r"\| `([^`]+)`", line
        )
        if not found:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows[found.group(1)] = {
            "title": cells[1],
            "publisher": cells[2],
            "date": cells[3],
            "url": cells[4],
        }
    if not rows:
        sys.exit("knowledge/quellen.md holds no source rows; check its table format.")
    return rows


class _Citations:
    """Numbers sources in order of first citation and formats citation lines."""

    def __init__(self, sources: dict[str, dict[str, str]]) -> None:
        self.sources = sources
        self.order: list[str] = []
        self.statuses: set[str] = set()

    def number(self, name: str) -> int:
        if name not in self.sources:
            sys.exit(f"{name} is cited in the draft but missing from quellen.md")
        if name not in self.order:
            self.order.append(name)
        return self.order.index(name) + 1

    def line(self, links: list[tuple[str, str]]) -> str:
        grouped: dict[int, list[str]] = {}
        for name, label in links:
            # The label ends at the first comma, the locator is the rest.
            locator = html.unescape(label).split(",", 1)[1].strip()
            locator = re.sub(r"^PDF (?:p|pp|S)\. ", "S. ", locator)
            # Long section headings of web pages would dominate the line;
            # the PDF keeps only the source number for them.
            if len(locator) > 40:
                locator = ""
            grouped.setdefault(self.number(name), [])
            if locator and locator not in grouped[self.number(name)]:
                grouped[self.number(name)].append(locator)
        parts = []
        for number, locators in grouped.items():
            pages = [
                loc.removeprefix("S. ") for loc in locators if loc.startswith("S. ")
            ]
            other = [loc for loc in locators if not loc.startswith("S. ")]
            text = ", ".join(([f"S. {', '.join(pages)}"] if pages else []) + other)
            parts.append(f"[{number}]{' ' + html.escape(text) if text else ''}")
        return "; ".join(parts)


def _strip(fragment: str, cites: _Citations) -> tuple[str, str | None, str]:
    """Remove status and citation groups from an HTML fragment."""
    status = STATUS_RE.search(fragment)
    links: list[tuple[str, str]] = []
    for group in CITE_GROUP_RE.findall(fragment):
        links += LINK_RE.findall(group)
    text = CITE_GROUP_RE.sub("", STATUS_RE.sub("", fragment))
    text = re.sub(r"\s+([.,;])", r"\1", text).strip()
    label = None
    if status:
        label = status.group(1) + (status.group(2) or "")
        cites.statuses.add(status.group(1))
    return text, label, cites.line(links)


def _rule_item(match: re.Match[str], cites: _Citations) -> str:
    text, label, line = _strip(match.group(1), cites)
    if not label and not line:
        # Settings and open points without status or source stay plain.
        return f'<li class="plain">{text}</li>'
    css = label.split()[0] if label else ""
    return (
        f'<li><span class="label {css}">{label or ""}</span>'
        f'<span>{text}<span class="cites">{line}</span></span></li>'
    )


def _is_links_only(cell: str) -> bool:
    return bool(LINK_RE.search(cell)) and not re.sub(rf"{LINK}|[;,\s]", "", cell)


def _table(match: re.Match[str], cites: _Citations) -> str:
    table = match.group(0)
    headers = re.findall(r"<th>(.*?)</th>", table, flags=re.S)
    rows = re.findall(r"<tr>\s*(<td>.*?)</tr>", table, flags=re.S)
    cells_per_row = [re.findall(r"<td>(.*?)</td>", row, flags=re.S) for row in rows]
    # A last column headed like a basis column, whose cells hold only source
    # links, is folded into the cell before it.
    fold = (
        len(headers) > 1
        and headers[-1].strip() in BASIS_HEADERS
        and all(cells and _is_links_only(cells[-1]) for cells in cells_per_row)
    )
    if fold:
        headers = headers[:-1]
    body = []
    for cells in cells_per_row:
        extra = LINK_RE.findall(cells.pop()) if fold else []
        out = []
        for index, cell in enumerate(cells):
            text, label, line = _strip(cell, cites)
            if index == len(cells) - 1 and extra:
                line = "; ".join(part for part in (line, cites.line(extra)) if part)
            status = f'<span class="inline-status">{label}</span>' if label else ""
            cite = f'<span class="cites">{line}</span>' if line else ""
            out.append(f"<td>{text}{status}{cite}</td>")
        body.append("<tr>" + "".join(out) + "</tr>")
    head = "".join(f"<th>{h}</th>" for h in headers)
    return (
        f"<table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table>"
    )


def _paragraph(match: re.Match[str], cites: _Citations) -> str:
    text, _, line = _strip(match.group(1), cites)
    if not line:
        return match.group(0)
    return f'<p>{text}<span class="cites">{line}</span></p>'


def _body_html(draft: Path, cites: _Citations, drop_first: bool) -> str:
    body = markdown.markdown(
        _strip_frontmatter(draft.read_text(encoding="utf-8")), extensions=["tables"]
    )
    head, _, rest = body.partition("<h2>")
    paragraphs = re.findall(r"<p>.*?</p>", head, flags=re.S)
    # With --drop-first-paragraph the first preamble paragraph (typically a
    # date line) appears only on the cover via --meta.
    intro = "".join(paragraphs[1:] if drop_first else paragraphs)
    rest = "<h2>" + rest
    handlers = {"li": _rule_item, "p": _paragraph}

    # One pass in document order, so sources are numbered as the reader
    # meets them.
    def block(match: re.Match[str]) -> str:
        if match.group(1) == "table":
            return _table(match, cites)
        inner = re.match(r"<\w+>(.*)</\w+>", match.group(0), flags=re.S)
        return handlers[match.group(1)](inner, cites)

    rest = re.sub(r"<(table|li|p)>.*?</\1>", block, rest, flags=re.S)
    rest = rest.replace("<ul>", '<ul class="rules">')
    legend = "".join(
        f'<div><span class="label {s}">{s}</span><span>{t}</span></div>'
        for s, t in STATUS_TEXT.items()
        if s in cites.statuses
    )
    return f'<div class="intro">{intro}</div><div class="legend">{legend}</div>{rest}'


def _sources_html(cites: _Citations) -> str:
    items = []
    for number, name in enumerate(cites.order, start=1):
        row = cites.sources[name]
        host = urlparse(row["url"]).netloc.removeprefix("www.")
        # The markers stay English in quellen.md for the check; the German
        # PDF names them in German.
        date = (
            row["date"]
            .replace("exception", "Ausnahme vom Zeitfenster")
            .replace("current", "geltende Fassung")
        )
        title = row["title"]
        items.append(
            f"<li><span>[{number}]</span><span>{html.escape(row['publisher'])}. "
            f"{html.escape(title)}. {html.escape(date)}. "
            f'<a href="{html.escape(row["url"])}">{html.escape(host)}</a></span></li>'
        )
    return (
        "<h2>Quellen</h2>"
        '<p class="note">Seitenangaben beziehen sich auf die Seite der PDF-Datei der Quelle. '
        "Die Originale und je eine Zusammenfassung liegen in der Wissensbasis unter sources/.</p>"
        f'<ul class="sources">{"".join(items)}</ul>'
    )


def _cover(args: argparse.Namespace) -> str:
    logo = f'<img src="{args.logo.name}" alt="">' if args.logo else ""
    sub = (
        f'<div class="sub">{html.escape(args.subtitle)}</div>' if args.subtitle else ""
    )
    meta = "<br>".join(html.escape(line) for line in args.meta)
    return (
        f'<section class="cover">{logo}<h1>{html.escape(args.title)}</h1>{sub}'
        f'<div class="meta">{meta}</div></section>'
    )


def _args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        type=Path,
        required=True,
        help="repository with knowledge/ and sources/",
    )
    parser.add_argument(
        "--draft",
        default="knowledge/governance-entwurf.md",
        help="Markdown file, relative to root",
    )
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument(
        "--meta", action="append", default=[], help="cover line, repeatable"
    )
    parser.add_argument(
        "--footer", default="", help="footer text on every page after the cover"
    )
    parser.add_argument("--logo", type=Path, help="PNG or SVG for the cover")
    parser.add_argument("--out", type=Path, help="output folder, default <root>/output")
    parser.add_argument("--pdf-name", default="document.pdf")
    parser.add_argument(
        "--drop-first-paragraph",
        action="store_true",
        help="leave the first preamble paragraph (a date line) to the cover",
    )
    args = parser.parse_args()
    args.root = args.root.resolve()
    args.draft = args.root / args.draft
    # Chrome needs an absolute file URI, so a relative --out is resolved.
    args.out = (args.out or args.root / "output").resolve()
    for path in (args.draft, args.root / "knowledge" / "quellen.md"):
        if not path.exists():
            parser.error(f"{path} not found")
    if args.logo and not args.logo.exists():
        parser.error(f"logo {args.logo} not found")
    return args


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    args = _args()
    args.out.mkdir(parents=True, exist_ok=True)
    cites = _Citations(_source_table(args.root / "knowledge" / "quellen.md"))
    body = _body_html(args.draft, cites, args.drop_first_paragraph)
    css = CSS.replace("__FOOTER__", args.footer.replace('"', "'"))
    page = (
        '<!doctype html><html lang="de"><head><meta charset="utf-8">'
        f"<title>{html.escape(args.title)}</title><style>{css}</style></head><body>"
        f"{_cover(args)}<main>{body}{_sources_html(cites)}</main></body></html>"
    )
    html_path = args.out / (args.draft.stem + ".html")
    html_path.write_text(page, encoding="utf-8")
    if args.logo:
        shutil.copy(args.logo, args.out / args.logo.name)
    pdf_path = args.out / args.pdf_name
    subprocess.run(
        [
            str(_find_browser()),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        check=True,
        capture_output=True,
        timeout=120,
    )
    if not pdf_path.exists() or pdf_path.stat().st_size == 0:
        sys.exit(f"Chrome did not write {pdf_path}")
    print(f"{pdf_path} ({len(cites.order)} sources cited)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
