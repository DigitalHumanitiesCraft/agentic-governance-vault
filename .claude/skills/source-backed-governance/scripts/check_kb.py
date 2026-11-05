# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check that every claim in knowledge/ is backed by a stored source.

Single-file script (PEP 723 regime, standard library only).

Data flow: reads knowledge/*.md and the file listing of sources/, prints
every violation and exits 0 only when none was found.

Rules checked:
- Claim documents (every knowledge/*.md except INDEX.md, project.md,
  quellen.md and journal.md): each paragraph, list item and table body row below the first
  "## " heading cites at least one source as a Markdown link
  "[Label, locator](../sources/<file>)". The locator after the first comma
  names the passage (page, section, article). Text before the first "## "
  heading is the document preamble and makes no claims. Sections whose
  heading starts with one of NO_CLAIM_SECTIONS hold gaps, assumptions and
  the organisation's own settings, which have no source.
- Every cited file exists in sources/.
- quellen.md lists every file in sources/ exactly once in its first table
  (later tables are not source rows) with the columns
  File | Title | Publisher | Date | Link | Category, all filled, the date
  starting with an existing YYYY-MM-DD, YYYY-MM or YYYY and with one of the
  --window prefixes, or marked "exception"
  (an approved exception) or "current" (current valid version of a law or
  standard, as agreed in project.md), and the link an http(s) URL.
- Every file in sources/ is cited by at least one claim document.
- Every file in sources/ has a summary sources/summaries/<stem>.md, and every
  summary belongs to a stored original. Skip this with --no-summaries
  before the summaries exist.

Usage: python check_kb.py [root] [--window 2025,2026] [--no-summaries]
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

NON_CLAIM_DOCS = frozenset({"INDEX.md", "project.md", "quellen.md", "journal.md"})
# Section headings (lower case prefixes) that record gaps and assumptions
# rather than source-backed claims.
NO_CLAIM_SECTIONS = (
    "gaps",
    "open points",
    "annahmen",
    "lücken",
    "offene punkte",
    "festlegungen",
)
CITATION = re.compile(r"\[([^\]]+)\]\(\.\./sources/([^)\s]+)\)")
SOURCE_LINK = re.compile(r"\]\(\.\./sources/([^)\s]+)\)")
SOURCE_COLUMNS = ("File", "Title", "Publisher", "Date", "Link", "Category")
# A year alone or a month is allowed where the source states no day. The
# date must end the cell or be followed by a space, comma, semicolon or
# parenthesis, so "2026-1", "20261" and "2026/99/99" are rejected instead of
# being read as their valid prefix.
DATE_PREFIX = re.compile(r"(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?(?=$|[\s,;(])")


def _blocks(text: str) -> list[tuple[int, str]]:
    """Split the claim part of a document into (line number, block) pairs.

    A block is a paragraph, a single list item with its continuation lines,
    or a single table row. Skipped are headings, the preamble, fenced code,
    block quotes, and sections whose heading (after any numbering) starts
    with one of NO_CLAIM_SECTIONS, including their subsections. The caller
    drops table header rows.
    """
    blocks: list[tuple[int, str]] = []
    in_claims = False
    exempt_level = 0  # heading level of the open exempt section, 0 if none
    in_fence = False
    current: list[str] = []
    start = 0

    def flush() -> None:
        if current:
            blocks.append((start, " ".join(current)))
            current.clear()

    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if line.startswith(("```", "~~~")):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        heading = re.match(r"(#+)\s+(.*)", line)
        if heading:
            flush()
            level = len(heading.group(1))
            if level == 2:
                in_claims = True
            if exempt_level and level <= exempt_level:
                exempt_level = 0
            title = re.sub(r"^[\d.]+\s*", "", heading.group(2)).lower()
            if not exempt_level and title.startswith(NO_CLAIM_SECTIONS):
                exempt_level = level
            continue
        if not in_claims or exempt_level or line.startswith(">"):
            flush()
            continue
        if not line:
            flush()
            continue
        is_item = re.match(r"([-*]|\d+\.)\s", line) is not None
        is_row = line.startswith("|")
        if is_row:
            flush()
            if not re.fullmatch(r"\|[\s:|-]+\|", line):
                blocks.append((number, line))
            continue
        if is_item:
            flush()
        if not current:
            start = number
        current.append(line)
    flush()
    return blocks


def _first_table_rows(text: str) -> list[list[str]]:
    """Return the rows of the first table, without its delimiter row.

    Later tables (notes, excluded sources) are not source rows.
    """
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            if rows:
                break
            continue
        if not re.fullmatch(r"\|[\s:|-]+\|", line):
            rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def _has_real_date(cell: str) -> bool:
    """Whether the cell starts with an existing YYYY-MM-DD, YYYY-MM or YYYY."""
    found = DATE_PREFIX.match(cell)
    if not found:
        return False
    year, month, day = found.groups()
    try:
        datetime.date(int(year), int(month or 1), int(day or 1))
    except ValueError:
        return False
    return True


def _check_claim_doc(path: Path, sources: set[str], cited: set[str]) -> list[str]:
    errors = []
    lines = path.read_text(encoding="utf-8").splitlines()
    header_lines = {
        index + 1
        for index, line in enumerate(lines)
        if index + 1 < len(lines)
        and line.strip().startswith("|")
        and re.fullmatch(r"\|[\s:|-]+\|", lines[index + 1].strip())
    }
    for number, block in _blocks("\n".join(lines)):
        if number in header_lines:
            continue
        citations = CITATION.findall(block)
        if not citations:
            errors.append(f"{path.name}:{number}: claim without source citation")
        for label, target in citations:
            target = target.split("#", 1)[0]  # a page anchor such as #page=3
            cited.add(target)
            if target not in sources:
                errors.append(f"{path.name}:{number}: cited file missing: {target}")
            if "," not in label or not label.split(",", 1)[1].strip():
                errors.append(
                    f"{path.name}:{number}: citation of {target} lacks a locator"
                )
    return errors


def _check_source_list(
    path: Path, sources: set[str], window: tuple[str, ...]
) -> list[str]:
    if not path.exists():
        return ["quellen.md missing"]
    rows = _first_table_rows(path.read_text(encoding="utf-8"))
    if not rows or tuple(rows[0]) != SOURCE_COLUMNS:
        return [f"quellen.md: table header must be {' | '.join(SOURCE_COLUMNS)}"]
    errors = []
    listed: list[str] = []
    for row in rows[1:]:
        if len(row) != len(SOURCE_COLUMNS) or not all(row):
            errors.append(f"quellen.md: incomplete row: {' | '.join(row)}")
            continue
        found = SOURCE_LINK.search(row[0]) or re.search(r"`([^`]+)`", row[0])
        name = found.group(1) if found else row[0]
        listed.append(name)
        if name not in sources:
            errors.append(f"quellen.md: listed file missing in sources/: {name}")
        # Every row needs a real date, also a marked one ("2023-07-01,
        # current"). Older sources enter only under the exception recorded
        # in project.md, and the date cell must say so.
        if not _has_real_date(row[3]):
            errors.append(f"quellen.md: {name}: date is not a real date: {row[3]}")
        elif not row[3].startswith(window) and not any(
            marker in row[3] for marker in ("exception", "current")
        ):
            errors.append(f"quellen.md: {name}: date outside window: {row[3]}")
        if not re.match(r"https?://\S+$", row[4]):
            errors.append(f"quellen.md: {name}: link is not a URL")
    for name in sorted(sources):
        count = listed.count(name)
        if count != 1:
            errors.append(f"quellen.md: {name} listed {count} times, expected once")
    return errors


def _check_summaries(source_dir: Path, sources: set[str]) -> list[str]:
    summary_dir = source_dir / "summaries"
    stems = {Path(name).stem for name in sources}
    summaries = (
        {p.stem for p in summary_dir.glob("*.md")} if summary_dir.is_dir() else set()
    )
    return [
        f"sources/{name} has no summary in sources/summaries/"
        for name in sorted(sources)
        if Path(name).stem not in summaries
    ] + [
        f"sources/summaries/{stem}.md has no original in sources/"
        for stem in sorted(summaries - stems)
    ]


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument(
        "--window",
        default=str(datetime.date.today().year),
        help="accepted date prefixes in quellen.md, comma separated, e.g. 2025,2026",
    )
    parser.add_argument("--no-summaries", action="store_true")
    args = parser.parse_args()
    root = args.root
    knowledge, source_dir = root / "knowledge", root / "sources"
    if not knowledge.is_dir() or not source_dir.is_dir():
        print(f"knowledge/ or sources/ missing under {root}")
        return 2
    sources = {
        p.name
        for p in source_dir.iterdir()
        if p.is_file() and not p.name.startswith(".")
    }
    cited: set[str] = set()
    errors = []
    claim_docs = sorted(
        p for p in knowledge.glob("*.md") if p.name not in NON_CLAIM_DOCS
    )
    for path in claim_docs:
        errors += _check_claim_doc(path, sources, cited)
    errors += _check_source_list(
        knowledge / "quellen.md", sources, tuple(args.window.split(","))
    )
    errors += [
        f"sources/{name} is never cited in knowledge/"
        for name in sorted(sources - cited)
    ]
    if not args.no_summaries:
        errors += _check_summaries(source_dir, sources)
    for error in errors:
        print(error)
    print(
        f"{len(claim_docs)} claim documents, {len(sources)} sources, "
        f"{len(errors)} problems"
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
