# Conventions

`scripts/check_kb.py` enforces the parts marked as checked, `scripts/build_pdf.py` relies on the parts marked as rendered.

## Files

- Originals in `sources/`, named `Publisher_YYYY-MM-DD_short-title.ext` (`YYYY-MM` if only the month is stated, `YYYY` if only the year). PDFs stay PDFs. Web pages are stored as `.md` with a header block (Title, Publisher, Date as stated, URL, Retrieved) followed by the full main text with its headings. Laws may be stored as a verbatim excerpt of the cited provisions, with the scope of the excerpt in the header block. For a consolidated law, the file name and the Date column carry the date of the consolidated version (Fassung vom), the header block also the retrieval date.
- One summary per original in `sources/summaries/<same base name>.md` (checked).
- Documents may open with a YAML frontmatter block, for example for Obsidian. `check_kb.py` reads it as preamble and `build_pdf.py` drops it. Links in the body stay Markdown links; Wikilinks do not count as citations.
- `knowledge/` holds `INDEX.md`, `project.md` (profile, window, exceptions, Leitfrage with fields and goals, open points), `quellen.md`, `journal.md` and the claim documents, including the draft.

## Citations (checked, rendered)

- In claim documents every paragraph, list item and table row below the first `## ` heading cites at least one source. Citations stand in parentheses at the end of the sentence, several separated by semicolons:

  ```text
  Regel in einem Satz (Vorgabe) ([Herausgeber 2025, PDF p. 3](../sources/Herausgeber_2025-03-01_titel.pdf); [Gesetz, § 2 Abs. 1, Z 3](../sources/...)).
  ```

- The label ends at the first comma and contains none; everything after it is the locator: `PDF p. 12` or `PDF S. 12` (the page in the PDF file, not the printed number), or a section, article or paragraph for web pages and legal texts. Locators longer than 40 characters appear in the PDF only as the source number.
- Text before the first `## ` heading is preamble without citations. Sections whose heading, after any numbering, starts with Gaps, Open points, Annahmen, Lücken, Offene Punkte or Festlegungen hold gaps, assumptions and the organisation's own settings without citations, including their subsections. Fenced code blocks and block quotes need no citation.
- Cite originals only, never a file in `sources/summaries/`.
- Every stored source is cited at least once.

## Source list (checked, rendered)

`knowledge/quellen.md` holds one table:

```text
| File | Title | Publisher | Date | Link | Category |
| --- | --- | --- | --- | --- | --- |
| [Herausgeber_2025-03-01_titel.pdf](../sources/Herausgeber_2025-03-01_titel.pdf)<br>[summary](../sources/summaries/Herausgeber_2025-03-01_titel.md) | Titel | Herausgeber | 2025-03-01 | https://... | Kategorie |
```

The first link in the File cell points to the original. The date starts with a prefix of the agreed window (`--window`, comma separated). Two markers admit other dates: `current` for the current valid version of a law, standard or funder rule when `project.md` records that rule for the run, with the version date (e.g. `2023-07-01, current`); `exception` for a single source the person approved. If a law was amended and no consolidated text can be stored, store the original as `current` and the amending act separately, and say in `project.md` that they are read together.

## Rules tables (rendered)

Tables render in any column layout. If the last column is headed Grundlage, Basis, Quellen or Sources and every cell in it holds only source links, the PDF folds it into the cell before it. The status stands in parentheses inside the rule text and appears below it in the PDF:

```text
| Feld | Regel | Grundlage |
| --- | --- | --- |
| Nachweis | Regel in einem Satz (Vorgabe). | [Herausgeber 2025, PDF p. 5](../sources/...) |
```

## Status

One vocabulary for briefs, documents and PDF, written in parentheses after the sentence, e.g. `(Empfehlung)`. An optional qualifier may follow, e.g. `(Pflicht für den Anbieter)` or `(Pflicht ab 28.06.2025)`. The PDF legend lists only the statuses the draft uses.

- Pflicht: follows from law.
- Vorgabe: binding rule outside the law, e.g. of a funder, a standard made binding by reference, or the organisation.
- Empfehlung: non-binding guidance.
- Ableitung: drawn by the organisation from the sources.
- Befund: result of an empirical study.

## Goals

The goal of a rule names a quality the Leitfrage asks for. Take the goals recorded with the Leitfrage in `project.md`.
