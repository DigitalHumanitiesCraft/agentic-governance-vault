"""Building blocks for PowerPoint decks in the DHCraft slide design.

Copy this module next to a project's deck generator and import it there, so
the build stays reproducible inside the project. The colours, fonts and slide
rules come from the brand-assets repository (README, sections "Colours and
fonts" and "Slides"). Requires python-pptx and Pillow.
"""

import io
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Inches, Pt

TITLE_FONT = "Sora"
BODY_FONT = "Instrument Sans"
CODE_FONT = "Consolas"

BLACK = RGBColor(0x00, 0x00, 0x00)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PURPLE = RGBColor(0x8A, 0x4F, 0xA3)
PURPLE_DEEP = RGBColor(0x5B, 0x3A, 0x78)
GREEN = RGBColor(0x5C, 0x9E, 0x4A)
ORANGE = RGBColor(0xE3, 0x9A, 0x3B)
BLUE_DEEP = RGBColor(0x4A, 0x7A, 0xB8)
# Derived slide tints, not palette tokens: a light purple card fill and border.
PURPLE_TINT = RGBColor(0xF2, 0xEC, 0xF6)
PURPLE_LINE = RGBColor(0xD9, 0xC6, 0xE3)

# Theme hues with the label colour that keeps large bold text at 3:1 or more.
# A deck gives each theme one hue for all slides and always shows the theme
# word or number beside it, so colour never carries meaning alone.
THEME_HUES = [(PURPLE, WHITE), (BLUE_DEEP, WHITE), (GREEN, WHITE), (ORANGE, BLACK)]

SLIDE_W = 13.333
SLIDE_H = 7.5
MARGIN = 0.6
CONTENT_TOP = 2.2
SOURCE_Y = 6.8
A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def new_presentation():
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_W)
    prs.slide_height = Inches(SLIDE_H)
    return prs


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def text(slide, x, y, w, h, paragraphs, *, size=18, font=BODY_FONT, color=BLACK,
         bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, space_after=0):
    """Text box without inner padding. `paragraphs` is a string or a list of strings."""
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = shape.text_frame
    frame.word_wrap = True
    frame.auto_size = MSO_AUTO_SIZE.NONE
    frame.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(frame, side, 0)
    items = [paragraphs] if isinstance(paragraphs, str) else paragraphs
    for i, content in enumerate(items):
        para = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
        para.alignment = align
        para.space_after = Pt(space_after)
        run = para.add_run()
        run.text = content
        run.font.name = font
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    return shape


def bullets(slide, x, y, w, h, items, *, size=20, space_after=16):
    """Bulleted list with real paragraph bullets in brand purple."""
    shape = text(slide, x, y, w, h, items, size=size, space_after=space_after)
    for para in shape.text_frame.paragraphs:
        p_pr = para._p.get_or_add_pPr()
        p_pr.set("marL", str(Inches(0.3)))
        p_pr.set("indent", str(-Inches(0.3)))
        bu_clr = p_pr.makeelement(A_NS + "buClr", {})
        bu_clr.append(bu_clr.makeelement(A_NS + "srgbClr", {"val": "8A4FA3"}))
        p_pr.append(bu_clr)
        p_pr.append(p_pr.makeelement(A_NS + "buChar", {"char": "●"}))
    return shape


def hexagon(slide, cx, cy, size, fill, label=None, *, label_size=28, label_color=WHITE):
    """Pointy-top hexagon as in the DHCraft logo, centred on (cx, cy)."""
    w = size * 0.866
    pts = [(cx, cy - size / 2), (cx + w / 2, cy - size / 4), (cx + w / 2, cy + size / 4),
           (cx, cy + size / 2), (cx - w / 2, cy + size / 4), (cx - w / 2, cy - size / 4)]
    # The freeform builder rounds local coordinates to integers. Points in inches
    # with an inch scale collapse to 0 and 1 and PowerPoint rejects the file, so
    # the points go in as EMU with scale 1.
    emu = [(int(Inches(px)), int(Inches(py))) for px, py in pts]
    builder = slide.shapes.build_freeform(*emu[0], scale=1.0)
    builder.add_line_segments(emu[1:], close=True)
    shape = builder.convert_to_shape()
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.fill.background()
    shape.shadow.inherit = False  # the default shape style adds a shadow
    if label:
        text(slide, cx - w / 2, cy - size / 2, w, size, label, size=label_size, font=TITLE_FONT,
             color=label_color, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    return shape


def box(slide, x, y, w, h, *, fill=PURPLE_TINT, line=None):
    """Rounded card, tinted by default or white with a purple outline."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.adjustments[0] = 0.06
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line:
        shape.line.color.rgb = line
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def arrow(slide, x1, y, x2):
    """Thin horizontal connector in brand purple with an arrow head."""
    line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y), Inches(x2), Inches(y))
    line.line.color.rgb = PURPLE
    line.line.width = Pt(1.5)
    ln = line.line._get_or_add_ln()
    ln.append(ln.makeelement(A_NS + "tailEnd", {"type": "triangle", "w": "med", "len": "med"}))
    return line


def content_slide(prs, title, subline=None, theme=None):
    """Title and subline at fixed positions. A theme index adds its hexagon at the top right."""
    slide = blank(prs)
    title_w = SLIDE_W - 2 * MARGIN - (1.2 if theme is not None else 0)
    text(slide, MARGIN, 0.5, title_w, 0.8, title, size=30, font=TITLE_FONT, bold=True)
    if subline:
        text(slide, MARGIN, 1.3, title_w, 0.5, subline, size=20, color=PURPLE_DEEP)
    if theme is not None:
        hue, label_color = THEME_HUES[theme]
        hexagon(slide, SLIDE_W - MARGIN - 0.45, 0.95, 1.0, hue, str(theme + 1),
                label_size=22, label_color=label_color)
    return slide


def title_slide(prs, logo, title_lines, subline, occasion):
    """Watercolor logo with text on the left, title block on the right."""
    slide = blank(prs)
    slide.shapes.add_picture(str(logo), Inches(0.8), Inches(2.02), width=Inches(4.6))
    text(slide, 6.4, 2.0, 6.4, 1.9, title_lines, size=40, font=TITLE_FONT, bold=True)
    text(slide, 6.4, 4.0, 6.4, 0.9, subline, size=24, color=PURPLE_DEEP)
    text(slide, 6.4, 5.15, 6.4, 0.4, occasion, size=16)
    return slide


def stat(slide, x, y, w, h, number, label, *, outline=False, note=None):
    """Large figure with its label, on a tinted card or an outlined white card."""
    if outline:
        box(slide, x, y, w, h, fill=WHITE, line=PURPLE)
    else:
        box(slide, x, y, w, h)
    text(slide, x + 0.3, y + 0.25, w - 0.6, 0.9, number, size=48, font=TITLE_FONT, bold=True, color=PURPLE_DEEP)
    text(slide, x + 0.3, y + 1.2, w - 0.6, h - 1.4, label, size=18)
    if note:
        text(slide, x + 0.3, y + h - 0.45, w - 0.6, 0.3, note, size=12)


def picture(slide, path, x, y, w, *, crop=None):
    """Screenshot or figure with a thin light-purple frame, optionally cropped (left, top, right, bottom px)."""
    source = Path(path)
    if crop:
        with Image.open(source) as full:
            data = io.BytesIO()
            full.crop(crop).save(data, format="PNG")
        data.seek(0)
        pic = slide.shapes.add_picture(data, Inches(x), Inches(y), width=Inches(w))
    else:
        pic = slide.shapes.add_picture(str(source), Inches(x), Inches(y), width=Inches(w))
    pic.line.color.rgb = PURPLE_LINE
    pic.line.width = Pt(1)
    return pic


def source(slide, citation):
    """Citation line at the bottom margin, 11 pt."""
    text(slide, MARGIN, SOURCE_Y, SLIDE_W - 2 * MARGIN, 0.35, citation, size=11)


def notes(slide, content):
    slide.notes_slide.notes_text_frame.text = content
