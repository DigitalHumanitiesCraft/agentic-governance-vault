# /// script
# requires-python = ">=3.11"
# dependencies = ["python-pptx", "pillow"]
# ///
"""Build the pitch deck from the approved outline knowledge/pitch-gliederung.md.

Single-file generator (PEP 723 regime) next to the copied helper module
dhcraft_deck.py from the dhcraft-pptx skill. Data flow: the outline is read,
each "## Folie N: ..." section becomes one content slide with its statements as
rows, its citations as a short source line and its speaker note plus the
status of every statement and the full citations in the notes field. A title
slide with the watercolor logo opens the deck. Writes
output/DHCraft_Pitch_Regeln_fuer_AI_Agents.pptx.

Design decisions:
- The generator reads nothing but the approved outline, so slide text cannot
  drift from what the operator approved; a text change goes through the
  outline and the chat first.
- A title "Bereich: Aussage" is split into the claim as slide title and the
  area as subline, so titles stay short; the words are unchanged.
- The four areas keep one theme hue each (Projekte purple, Forschung
  blue-deep, Programmierung green, Organisation orange). The opening slide
  shows the four hexagons with their area names as a map; every area slide
  repeats the cluster small at the top right with its own hexagon filled, so
  colour never carries meaning alone and the numbers have a legend. Subline
  and status labels take the area hue (black on orange for contrast).
- Every statement is a row with its status (Pflicht, Vorgabe ...) as a label
  on the left, because the owners must see what is binding and what DHCraft
  chooses. A Befund is set apart as a card, since it is evidence, not a rule.
- The Organisation slide is the decision slide: its rows are outlined cards
  with an empty tick box, so it reads as a sheet to decide on.

Usage: uv run scripts/pitch/build_pitch.py
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import dhcraft_deck as d  # noqa: E402  (copied helper next to this file)
from pptx.dml.color import RGBColor  # noqa: E402
from pptx.enum.shapes import MSO_SHAPE  # noqa: E402
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN  # noqa: E402
from pptx.util import Inches, Pt  # noqa: E402

ROOT = HERE.parents[1]
OUTLINE = ROOT / "knowledge" / "pitch-gliederung.md"
LOGO = HERE / "assets" / "dhcraft_logo_watercolor+text_transparent.png"
OUT = ROOT / "output" / "DHCraft_Pitch_Regeln_fuer_AI_Agents.pptx"
THEMES = {"Projekte": 0, "Forschung": 1, "Programmierung": 2, "Organisation": 3}
AREAS = list(THEMES)
DECISION_THEME = 3
# Derived slide tints, not palette tokens: inactive hexagons, cards and rules.
PALE = RGBColor(0xEE, 0xEE, 0xEE)
PALE_TEXT = RGBColor(0x59, 0x59, 0x59)
RULE = RGBColor(0xD0, 0xD0, 0xD0)
ROWS_TOP = 1.95
# The opening slide has no subline, so its rows start higher.
ROWS_TOP_PLAIN = 1.55
ROWS_BOTTOM = 6.45
LABEL_W = 1.75
CITE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
STATEMENT = re.compile(
    r"^- (.+?) \((Pflicht|Vorgabe|Empfehlung|Ableitung|Befund)\) \((.+)\)\.$"
)


def _slides(text: str) -> list[dict]:
    """Slides of the outline: title, statements with status and citations, note."""
    slides = []
    for block in re.split(r"^## ", text, flags=re.M)[1:]:
        heading, _, body = block.partition("\n")
        match = re.match(r"Folie \d+: (.+)", heading.strip())
        if not match:
            continue
        statements = []
        for line in body.splitlines():
            if not line.startswith("- "):
                continue
            found = STATEMENT.match(line.strip())
            if not found:
                sys.exit(f"Statement not in the expected form: {line[:80]}")
            claim, status, cites = found.groups()
            statements.append((claim + ".", status, CITE.findall(cites)))
        note = " ".join(
            line.lstrip("> ").removeprefix("Sprechernotiz: ")
            for line in body.splitlines()
            if line.startswith(">")
        )
        slides.append({"title": match.group(1), "statements": statements, "note": note})
    if len(slides) > 5:
        sys.exit(f"The outline has {len(slides)} slides; a pitch has at most five.")
    return slides


def _short(label: str) -> str:
    """Short citation for the source line: 'PDF S. 16' becomes 'S. 16'."""
    return label.replace("PDF S. ", "S. ").replace(", Abschnitt ", ", ")


def _source_text(statements: list) -> str:
    # Several pages of the same source are merged ("DSB 1/2026, S. 3, 4").
    merged: dict[str, list[str]] = {}
    for _, _, cites in statements:
        for label in cites:
            name, _, place = _short(label).partition(", ")
            places = merged.setdefault(name, [])
            if place and place not in places:
                places.append(place)
    parts = []
    for name, places in merged.items():
        pages = sorted(
            (p.removeprefix("S. ") for p in places if p.startswith("S. ")),
            key=lambda page: int(re.match(r"\d+", page).group()),
        )
        other = [p for p in places if not p.startswith("S. ")]
        detail = ([f"S. {', '.join(pages)}"] if pages else []) + other
        parts.append(f"{name}, {'; '.join(detail)}" if detail else name)
    return " | ".join(parts)


def _ink(theme: int | None) -> RGBColor:
    """Text colour of an area: its hue, black on orange, deep purple without area."""
    if theme is None:
        return d.PURPLE_DEEP
    return d.BLACK if theme == DECISION_THEME else d.THEME_HUES[theme][0]


def _cluster(
    slide, cx: float, cy: float, size: float, active: int | None, label_size: int
):
    """Four hexagons in a honeycomb as in the logo; returns their centres.

    The active area is filled with its hue and the others are pale, so the
    position in the deck shows without reading. Without an active area all
    four are filled, as the map on the opening slide."""
    w = size * 0.866
    centres = [
        (cx - w / 2, cy - size * 0.375),
        (cx + w / 2, cy - size * 0.375),
        (cx, cy + size * 0.375),
        (cx + w, cy + size * 0.375),
    ]
    for i, (x, y) in enumerate(centres):
        on = active is None or i == active
        hue, label = d.THEME_HUES[i]
        d.hexagon(
            slide,
            x,
            y,
            size * 0.96,
            hue if on else PALE,
            str(i + 1),
            label_size=label_size,
            label_color=label if on else PALE_TEXT,
        )
    return centres


def _area_slide(prs, title: str, subline: str | None, theme: int | None):
    slide = d.blank(prs)
    title_w = d.SLIDE_W - 2 * d.MARGIN - (2.3 if theme is not None else 0)
    d.text(
        slide, d.MARGIN, 0.5, title_w, 0.8, title, size=30, font=d.TITLE_FONT, bold=True
    )
    if subline:
        d.text(
            slide,
            d.MARGIN,
            1.25,
            title_w,
            0.5,
            subline,
            size=20,
            bold=True,
            color=_ink(theme),
        )
    if theme is not None:
        _cluster(slide, d.SLIDE_W - d.MARGIN - 1.3, 0.95, 0.66, theme, label_size=13)
    return slide


def _rule(slide, x1: float, x2: float, y: float) -> None:
    # A thin filled rectangle: a connector picks up the theme's shadow and
    # renders doubled.
    line = _rect(slide, x1, y - 0.006, x2 - x1, 0.012)
    line.fill.solid()
    line.fill.fore_color.rgb = RULE
    line.line.fill.background()


def _rect(slide, x: float, y: float, w: float, h: float):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.shadow.inherit = False
    return shape


def _rows(slide, statements: list, theme: int | None, right: float) -> None:
    """One row per statement: status label left, claim right, hairlines between."""
    left = d.MARGIN
    top = ROWS_TOP if theme is not None else ROWS_TOP_PLAIN
    height = (ROWS_BOTTOM - top) / len(statements)
    for i, (claim, status, _) in enumerate(statements):
        y = top + i * height
        if theme == DECISION_THEME:
            d.box(
                slide,
                left,
                y + 0.08,
                right - left,
                height - 0.16,
                fill=d.WHITE,
                line=d.ORANGE,
            )
            tick = _rect(slide, left + 0.3, y + height / 2 - 0.16, 0.32, 0.32)
            tick.fill.background()
            tick.line.color.rgb = d.BLACK
            tick.line.width = Pt(1.5)
            label_x = left + 0.9
            claim_x = label_x + LABEL_W
        elif status == "Befund":
            d.box(slide, left, y + 0.1, right - left, height - 0.2, fill=PALE)
            accent = _rect(slide, left, y + 0.1, 0.1, height - 0.2)
            accent.fill.solid()
            accent.fill.fore_color.rgb = (
                d.THEME_HUES[theme][0] if theme is not None else d.PURPLE
            )
            accent.line.fill.background()
            label_x = left + 0.35
            claim_x = left + LABEL_W + 0.35
        else:
            label_x = left
            # Same claim column as a Befund card on the slide.
            claim_x = left + LABEL_W + 0.35
            if i and statements[i - 1][1] != "Befund":
                _rule(slide, left, right, y)
        d.text(
            slide,
            label_x,
            y,
            LABEL_W - 0.2,
            height,
            status,
            size=15,
            bold=True,
            color=_ink(theme),
            anchor=MSO_ANCHOR.MIDDLE,
        )
        d.text(
            slide,
            claim_x,
            y,
            right - claim_x - 0.3,
            height,
            claim,
            size=22,
            anchor=MSO_ANCHOR.MIDDLE,
        )


def _legend(slide) -> float:
    """Map of the four areas on the opening slide; returns the right edge of the rows."""
    cx, cy, size = 10.35, 4.05, 1.5
    centres = _cluster(slide, cx, cy, size, None, label_size=26)
    for i, (x, y) in enumerate(centres):
        top = y - size / 2 - 0.42 if i < 2 else y + size / 2 + 0.06
        # The two lower labels move apart so the long words do not touch.
        shift = 0 if i < 2 else (-0.25 if i == 2 else 0.25)
        d.text(
            slide,
            x + shift - 1.1,
            top,
            2.2,
            0.35,
            AREAS[i],
            size=15,
            bold=True,
            color=_ink(i),
            align=PP_ALIGN.CENTER,
        )
    return cx - size * 0.866 * 1.5 - 0.3


def _source(slide, citation: str) -> None:
    """Short citations, 12 pt, two lines at most; the full citations are in the notes."""
    d.text(slide, d.MARGIN, 6.68, 9.8, 0.6, citation, size=12)


def build() -> Path:
    slides = _slides(OUTLINE.read_text(encoding="utf-8"))
    prs = d.new_presentation()
    title = d.title_slide(
        prs,
        LOGO,
        ["Regeln für AI Agents", "bei DHCraft"],
        "Regelkonform, sicher und nachprüfbar in Projekten, Forschung und Programmierung",
        "Pitch für die Eigentümer, November 2026",
    )
    d.notes(
        title,
        "Titelfolie. Der Pitch bereitet den Beschluss der Governance-Beschlussvorlage 1.0 vor.",
    )
    for spec in slides:
        area, _, claim = spec["title"].partition(": ")
        theme = THEMES.get(area) if claim else None
        slide = _area_slide(
            prs,
            claim if theme is not None else spec["title"],
            area if theme is not None else None,
            theme,
        )
        right = _legend(slide) if theme is None else d.SLIDE_W - d.MARGIN
        _rows(slide, spec["statements"], theme, right)
        _source(slide, _source_text(spec["statements"]))
        status = "\n".join(
            f"- {claim} ({status}; {'; '.join(cites)})"
            for claim, status, cites in spec["statements"]
        )
        d.notes(slide, f"{spec['note']}\n\nAussagen mit Status und Quelle:\n{status}")
    OUT.parent.mkdir(exist_ok=True)
    prs.save(OUT)
    return OUT


if __name__ == "__main__":
    print(build())
