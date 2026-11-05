# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check the Obsidian vault: frontmatter, dead links and tags.

Single-file script (PEP 723 regime, standard library only).

Data flow: reads TAG-TAXONOMY.md, HOME.md, ACTIVE-WORK.md, knowledge/**/*.md,
notizen/**/*.md, protokolle/**/*.md, projekte/**/*.md and
sources/summaries/*.md, prints every violation and exits 0 only when none was
found.

Rules checked:
- Notes (the root documents, knowledge/, notizen/, protokolle/, projekte/)
  start with a frontmatter block holding title, type, language, tags and
  related; type and language come from the fixed lists below.
- Every tag, in frontmatter or inline as #tag, belongs to the taxonomy in
  TAG-TAXONOMY.md: each list item there that starts with a tag in backticks
  defines one tag. A missing taxonomy file is reported as a problem.
- Every Wikilink [[name]] or [[name#heading]] resolves to exactly one file of
  the vault (by file name or path suffix, as Obsidian resolves it) and, with a
  heading, to a heading of that note. A name that fits two files is reported,
  because Obsidian would pick one of them silently.
- Every relative Markdown link, also in the form [text](<path with spaces>),
  points to an existing file or folder inside the vault.

The stored originals in sources/ are third-party text and are not checked;
their summaries are. Ignored folders match Obsidian's excluded files.

Usage: python scripts/check_vault.py [vault root, default: parent of scripts/]
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

TAXONOMY_FILE = "TAG-TAXONOMY.md"
TYPES = frozenset(
    {
        "home",
        "active-work",
        "index",
        "projekt",
        "kundenprojekt",
        "regeln",
        "entwurf",
        "quellen",
        "journal",
        "notiz",
        "protokoll",
        "angebot",
        "taxonomie",
        "daten",
        "anforderungen",
        "gliederung",
    }
)
LANGUAGES = frozenset({"de", "en"})
REQUIRED = ("title", "type", "language", "tags", "related")
IGNORED = (
    "eingang",
    "public",
    "output",
    "dashboard",
    ".claude",
    ".ruff_cache",
    ".obsidian",
    ".git",
)

WIKILINK = re.compile(r"!?\[\[([^\]|#]*)(?:#([^\]|]*))?(?:\|[^\]]*)?\]\]")
# Target either in angle brackets (may hold spaces) or bare, optional title.
MD_LINK = re.compile(r"\]\((?:<([^>\n]*)>|([^)\s]+))(?:\s+\"[^\"]*\")?\)")
INLINE_TAG = re.compile(r"(?<![\w/&#])#([^\s#\d.,;:!?)(\]\[][^\s#.,;:!?)(\]\[]*)")
CODE = re.compile(r"```.*?```|`[^`\n]*`", flags=re.S)
TAXONOMY_ENTRY = re.compile(r"^\s*[-*]\s+`([a-z]+/[a-z0-9-]+)`", flags=re.M)
# Only fenced blocks: CODE would also strip the inline backticks that mark a tag.
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,}).*?^ {0,3}\1", flags=re.S | re.M)


def _frontmatter(text: str) -> tuple[dict[str, object] | None, str]:
    """Parse the small YAML subset the vault uses: scalars and lists."""
    match = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        return None, text
    data: dict[str, object] = {}
    key = ""
    for line in match.group(1).splitlines():
        item = re.match(r"\s+-\s+(.*)", line)
        if item and key:
            values = data.setdefault(key, [])
            if isinstance(values, list):
                values.append(item.group(1).strip().strip('"'))
            continue
        pair = re.match(r"([\w-]+):\s*(.*)", line)
        if pair:
            key, value = pair.group(1), pair.group(2).strip()
            if value.startswith("[") and value.endswith("]"):
                # Flow list, e.g. tags: [a, b]
                data[key] = [
                    v.strip().strip('"') for v in value[1:-1].split(",") if v.strip()
                ]
            else:
                data[key] = [] if value == "" else value.strip('"')
    return data, text[match.end() :]


def load_taxonomy(root: Path) -> frozenset[str] | None:
    """Read the allowed tags from TAG-TAXONOMY.md; None when the file is missing."""
    path = root / TAXONOMY_FILE
    if not path.is_file():
        return None
    _, body = _frontmatter(path.read_text(encoding="utf-8"))
    return frozenset(TAXONOMY_ENTRY.findall(FENCE.sub("", body)))


def _heading_key(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def _headings(path: Path) -> set[str]:
    if path.suffix != ".md":
        return set()
    text = path.read_text(encoding="utf-8")
    return {_heading_key(h) for h in re.findall(r"^#{1,6}\s+(.+)$", text, flags=re.M)}


def _files(root: Path) -> list[Path]:
    return [
        p
        for p in root.rglob("*")
        if p.is_file()
        and not any(part in IGNORED for part in p.relative_to(root).parts)
    ]


class _Resolver:
    """Resolve Wikilink names to files the way Obsidian does.

    A bare name matches a file name with extension, or the stem of a Markdown
    file. A name with a slash matches the end of a vault path, with or without
    the .md suffix.
    """

    def __init__(self, root: Path, files: list[Path]) -> None:
        self.by_name: dict[str, set[Path]] = {}
        self.paths: list[tuple[str, Path]] = []
        for p in files:
            rel = p.relative_to(root).as_posix().lower()
            self.by_name.setdefault(p.name.lower(), set()).add(p)
            self.paths.append((rel, p))
            if p.suffix == ".md":
                self.by_name.setdefault(p.stem.lower(), set()).add(p)
                self.paths.append((rel[: -len(".md")], p))

    def __call__(self, name: str) -> list[Path]:
        key = name.lower()
        if "/" not in key:
            return sorted(self.by_name.get(key, ()))
        key = key.lstrip("/")
        return sorted(
            {p for rel, p in self.paths if rel == key or rel.endswith("/" + key)}
        )


def _check_note(data: dict[str, object] | None, rel: str) -> list[str]:
    if data is None:
        return [f"{rel}: no frontmatter"]
    errors = [f"{rel}: frontmatter lacks {key}" for key in REQUIRED if key not in data]
    if data.get("type") not in TYPES:
        errors.append(f"{rel}: type {data.get('type')!r} not in {sorted(TYPES)}")
    if data.get("language") not in LANGUAGES:
        errors.append(
            f"{rel}: language {data.get('language')!r} not in {sorted(LANGUAGES)}"
        )
    if "tags" in data and not isinstance(data["tags"], list):
        errors.append(f"{rel}: tags must be a list")
    return errors


def check(root: Path) -> list[str]:
    errors: list[str] = []
    taxonomy = load_taxonomy(root)
    if taxonomy is None:
        errors.append(
            f"{TAXONOMY_FILE}: missing; it defines the allowed tags, "
            "so no tag can be checked"
        )
    elif not taxonomy:
        errors.append(
            f"{TAXONOMY_FILE}: defines no tag; each tag is a list item "
            "starting with the tag in backticks"
        )

    files = _files(root)
    resolve = _Resolver(root, files)

    notes = [root / "HOME.md", root / "ACTIVE-WORK.md"]
    if taxonomy is not None:
        notes.append(root / TAXONOMY_FILE)
    notes += sorted((root / "knowledge").rglob("*.md"))
    notes += sorted((root / "notizen").rglob("*.md"))
    notes += sorted((root / "protokolle").rglob("*.md"))
    notes += sorted((root / "projekte").rglob("*.md"))
    checked = notes + sorted((root / "sources" / "summaries").glob("*.md"))

    for path in checked:
        rel = path.relative_to(root).as_posix()
        if not path.exists():
            errors.append(f"{rel}: missing")
            continue
        text = path.read_text(encoding="utf-8")
        data, body = _frontmatter(text)
        tags: list[str] = []
        if path in notes:
            errors.extend(_check_note(data, rel))
        if data and isinstance(data.get("tags"), list):
            tags.extend(data["tags"])

        prose = CODE.sub("", text)
        for name, heading in WIKILINK.findall(prose):
            # In tables the alias pipe is escaped as \|.
            name = name.rstrip("\\").strip()
            targets = resolve(name) if name else [path]
            if not targets:
                errors.append(f"{rel}: dead Wikilink [[{name}]]")
                continue
            if len(targets) > 1:
                where = ", ".join(t.relative_to(root).as_posix() for t in targets)
                errors.append(f"{rel}: ambiguous Wikilink [[{name}]] fits {where}")
                continue
            if heading.startswith("page="):
                continue  # page anchor into a PDF
            if heading and _heading_key(heading) not in _headings(targets[0]):
                errors.append(f"{rel}: [[{name}#{heading}]] has no such heading")

        for angled, bare in MD_LINK.findall(CODE.sub("", body)):
            href = angled or bare
            if not href or re.match(r"(https?|mailto):|#", href):
                continue
            target = (path.parent / unquote(href.split("#", 1)[0])).resolve()
            if not target.exists():
                errors.append(f"{rel}: dead link {href}")
            elif not target.is_relative_to(root.resolve()):
                errors.append(f"{rel}: link leaves the vault {href}")

        if taxonomy is None:
            continue
        # Inline tags: outside code, link targets and Wikilinks.
        plain = MD_LINK.sub("]", WIKILINK.sub("", CODE.sub("", body)))
        tags.extend(INLINE_TAG.findall(plain))
        errors.extend(
            f"{rel}: tag {tag!r} not defined in {TAXONOMY_FILE}"
            for tag in tags
            if tag not in taxonomy
        )
    return errors


def main() -> int:
    root = (
        Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    )
    sys.stdout.reconfigure(encoding="utf-8")
    errors = check(root)
    for error in errors:
        print(error)
    print(f"{len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
