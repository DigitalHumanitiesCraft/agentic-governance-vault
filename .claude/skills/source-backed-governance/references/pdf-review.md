# PDF review

Render every page as an image (e.g. PyMuPDF `page.get_pixmap(dpi=90)`, run with `uv run --with pymupdf python ...` where PyMuPDF is not installed) and look at each one. Fix in `build_pdf.py` or in the draft, rebuild, and look again.

These patterns make a document hard to read and look generated.

- Coloured pills or badges inside sentences. Status belongs in a quiet margin column.
- Citations inside the sentence, repeated prefixes such as "PDF S." for every page, long English section titles in German text. Group per source on a separate small line.
- One accent colour on every heading rule, bullet and box. Use accent at most once, or not at all.
- Template covers: gradient background, letter-spaced kicker line, legend of pills. Use a plain cover with logo, title, subtitle and dates.
- Lines longer than about 80 characters for print reading, sans-serif body text at small size.
- Tables with a column that only holds citation numbers.
- Grey text for the points the reader must decide on.
- Full URLs in the source list. Link the host name.
- Single orphan lines on a last page, and headings at the foot of a page.
