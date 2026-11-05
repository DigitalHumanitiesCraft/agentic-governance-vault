# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown"]
# ///
"""Render knowledge/governance-entwurf.md as a readable A4 PDF.

Single-file script (PEP 723 regime). Data flow: the Markdown draft and the
source table in knowledge/quellen.md are converted to one HTML page in the
output folder, which headless Chrome prints to PDF.

Design decisions, from a page-by-page readability review on 2026-11-05:
- Each rule is set as a two-column item. The status (Pflicht, Vorgabe,
  Empfehlung, Ableitung) stands as a quiet word in a left column, and the
  sources follow in a separate small line. Coloured pills inside the
  sentence made every line look busy and were removed.
- Citations are grouped per source ("[3] S. 4, 7"). Page numbers refer to
  the PDF file of the source. Section locators of web pages are long English
  headings and are dropped in the PDF; the Markdown draft keeps them.
- The source list links the host name instead of printing full URLs.
- Body text is set in a serif face at a line length of about 80 characters,
  with German hyphenation, because the document is read in print.
- Chrome is used because it is installed on the operator's machines and
  supports @page margin boxes for page numbers; no extra PDF library needed.

Usage: python scripts/build_governance_pdf.py [output folder, default: output/]
"""

import html
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

import markdown

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "knowledge" / "governance-entwurf.md"
SOURCES = ROOT / "knowledge" / "quellen.md"
LOGO = ROOT / "assets" / "dhcraft_logo_watercolor.png"
PDF_NAME = "DHCraft_Governance_AI_Agents_Beschlussvorlage_v1.0.pdf"
CHROME_PATHS = (
    Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
)
STATUS_RE = re.compile(
    r"\s*\((Pflicht|Vorgabe|Empfehlung|Ableitung)( für den Anbieter)?\)"
)
LINK = r'<a href="\.\./sources/[^"]+">[^<]+</a>'
CITE_GROUP_RE = re.compile(rf"\s*\(({LINK}(?:;\s*{LINK})*)\)")
LINK_RE = re.compile(r'<a href="\.\./sources/([^"]+)">([^<]+)</a>')
STATUS_TEXT = {
    "Pflicht": "folgt aus dem Gesetz",
    "Vorgabe": "folgt aus den Regeln eines Förderers",
    "Empfehlung": "Leitlinie einer Behörde, nicht bindend",
    "Ableitung": "Folgerung, die DHCraft aus den Quellen zieht",
}

CSS = """
@page { size: A4; margin: 24mm 25mm 22mm 25mm;
  @bottom-left { content: "Governance für AI Agents, Beschlussvorlage 1.0 vom 5. November 2026"; font: 7.5pt 'Segoe UI'; color: #8b909a; }
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
.label { font-size: 8pt; font-weight: 600; color: var(--muted); padding-top: 0.6mm; }
.label.Pflicht, .label.Vorgabe { color: var(--head); }
.cites { display: block; margin-top: 0.8mm; font-size: 7.6pt; color: var(--muted); }
table { width: 100%; border-collapse: collapse; margin: 2mm 0 4mm; font-size: 9.3pt; }
th { text-align: left; font-size: 8pt; font-weight: 600; color: var(--muted); padding: 1.5mm 2mm 1.5mm 0; border-bottom: 1px solid var(--head); }
td { vertical-align: top; padding: 2.2mm 3mm 2.2mm 0; border-bottom: 1px solid var(--line); }
td:first-child { font-family: 'Segoe UI', sans-serif; font-weight: 600; font-size: 8.8pt; width: 24mm; }
td:nth-child(2) { width: 38mm; color: var(--muted); }
tr { break-inside: avoid; }
.inline-status { font-family: 'Segoe UI', sans-serif; font-size: 8pt; font-weight: 600; color: var(--muted); }
.sources { font-size: 8.3pt; line-height: 1.45; list-style: none; padding: 0; }
.sources li { display: grid; grid-template-columns: 8mm 1fr; margin-bottom: 1.4mm; break-inside: avoid; }
.sources a { color: var(--head); text-decoration: none; border-bottom: 1px solid var(--line); }
.note { font-size: 8.3pt; color: var(--muted); }
"""


def _strip_frontmatter(text: str) -> str:
    """Drop an Obsidian frontmatter block; it is vault metadata, not content."""
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)


def _find_chrome() -> Path:
    for path in CHROME_PATHS:
        if path.exists():
            return path
    sys.exit("No Chrome or Edge found; install one or add its path to CHROME_PATHS.")


def _source_table() -> dict[str, dict[str, str]]:
    """Map source file name to title, publisher, date and URL from quellen.md."""
    rows = {}
    for line in SOURCES.read_text(encoding="utf-8").splitlines():
        found = re.match(r"\| \[([^\]]+)\]\(\.\./sources/[^)]+\)", line)
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

    def number(self, name: str) -> int:
        if name not in self.sources:
            sys.exit(f"{name} is cited in the draft but missing from quellen.md")
        if name not in self.order:
            self.order.append(name)
        return self.order.index(name) + 1

    def line(self, links: list[tuple[str, str]]) -> str:
        grouped: dict[int, list[str]] = {}
        for name, label in links:
            locator = html.unescape(label).rsplit(",", 1)[1].strip()
            # Section headings of web pages are long and English; the PDF
            # keeps only the source number for them.
            if locator.startswith(("Abschnitt", "lead text")):
                locator = ""
            locator = locator.replace("PDF S. ", "S. ")
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
        label = status.group(1) + (" (Anbieter)" if status.group(2) else "")
    return text, label, cites.line(links)


def _rule_item(match: re.Match[str], cites: _Citations) -> str:
    text, label, line = _strip(match.group(1), cites)
    css = label.split()[0] if label else ""
    return (
        f'<li><span class="label {css}">{label or ""}</span>'
        f'<span>{text}<span class="cites">{line}</span></span></li>'
    )


def _table_row(match: re.Match[str], cites: _Citations) -> str:
    cells = re.findall(r"<td>(.*?)</td>", match.group(1), flags=re.S)
    if len(cells) != 4:
        return match.group(0)
    text, label, _ = _strip(cells[2], cites)
    # The basis column holds bare links without surrounding parentheses.
    line = cites.line(LINK_RE.findall(cells[3]))
    status = f' <span class="inline-status">{label}</span>' if label else ""
    return (
        f"<tr><td>{cells[0]}</td><td>{cells[1]}</td>"
        f'<td>{text}{status}<span class="cites">{line}</span></td></tr>'
    )


def _paragraph(match: re.Match[str], cites: _Citations) -> str:
    text, _, line = _strip(match.group(1), cites)
    if not line:
        return match.group(0)
    return f'<p>{text}<span class="cites">{line}</span></p>'


def _body_html(cites: _Citations) -> str:
    body = markdown.markdown(
        _strip_frontmatter(DRAFT.read_text(encoding="utf-8")), extensions=["tables"]
    )
    head, _, rest = body.partition("<h2>")
    intro = "".join(re.findall(r"<p>.*?</p>", head, flags=re.S)[1:])
    rest = "<h2>" + rest
    rest = re.sub(r"<th>Grundlage</th>", "", rest)
    handlers = {"tr": _table_row, "li": _rule_item, "p": _paragraph}

    # One pass in document order, so sources are numbered as the reader
    # meets them.
    def block(match: re.Match[str]) -> str:
        inner = re.match(r"<\w+>(.*)</\w+>", match.group(0), flags=re.S)
        return handlers[match.group(1)](inner, cites)

    rest = re.sub(r"<(tr|li|p)>.*?</\1>", block, rest, flags=re.S)
    rest = rest.replace("<ul>", '<ul class="rules">')
    legend = "".join(
        f'<div><span class="label {s}">{s}</span><span>{t}</span></div>'
        for s, t in STATUS_TEXT.items()
    )
    return f'<div class="intro">{intro}</div><div class="legend">{legend}</div>{rest}'


def _sources_html(cites: _Citations) -> str:
    items = []
    for number, name in enumerate(cites.order, start=1):
        row = cites.sources[name]
        host = urlparse(row["url"]).netloc.removeprefix("www.")
        date = row["date"].replace("exception", "Ausnahme vom Zeitfenster 2026")
        date = date.replace(
            "consolidated version of an Act from 1999", "konsolidierte Fassung"
        )
        title = row["title"].replace("preprint", "Preprint")
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


def _cover() -> str:
    return (
        f'<section class="cover"><img src="{LOGO.name}" alt="DHCraft">'
        "<h1>Governance für AI Agents</h1>"
        '<div class="sub">Regeln für den Einsatz von AI Agents in Kundenprojekten, '
        "Forschung und Programmierung bei Digital Humanities Craft</div>"
        '<div class="meta">Beschlussvorlage, Version 1.0 vom 5. November 2026<br>'
        "Gilt nach Beschluss durch die Eigentümer<br>"
        "Gestützt auf Quellen aus dem Jahr 2026</div></section>"
    )


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    cites = _Citations(_source_table())
    body = _body_html(cites)
    page = (
        '<!doctype html><html lang="de"><head><meta charset="utf-8">'
        f"<title>Governance für AI Agents</title><style>{CSS}</style></head><body>"
        f"{_cover()}<main>{body}{_sources_html(cites)}</main></body></html>"
    )
    html_path = out_dir / "governance-entwurf.html"
    html_path.write_text(page, encoding="utf-8")
    shutil.copy(LOGO, out_dir / LOGO.name)
    pdf_path = out_dir / PDF_NAME
    subprocess.run(
        [
            str(_find_chrome()),
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
