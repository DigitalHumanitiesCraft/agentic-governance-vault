# Wissensbasis Agentic Engineering und Governance

This folder is an Obsidian vault with two purposes. It is the project knowledge base on rules for AI agents at Digital Humanities Craft (DHCraft), and it holds the operator's personal notes and the protocols, offers and analyses that client inquiries produce. [HOME.md](HOME.md) is the map of content, [ACTIVE-WORK.md](ACTIVE-WORK.md) the running state.

## Layout

| Path | Content | Language |
| --- | --- | --- |
| `HOME.md` | Map of content of the vault | German |
| `TAG-TAXONOMY.md` | The tag taxonomy with the meaning of every tag; `scripts/check_vault.py` reads the allowed tags from it | German |
| `ACTIVE-WORK.md` | What is running, next steps, open questions | German |
| `knowledge/` | Project knowledge base: INDEX, project, rules, governance draft, source list, journal, and `pitch-gliederung.md`, the approved pitch outline | English; the governance draft and the pitch outline German |
| `knowledge/northwind/` | Description of the Northwind exercise data (`data.md`) and the requirements of its revenue page (`requirements.md`); outside the claim and source system | English |
| `sources/` | Stored originals of every source, named `Publisher_YYYY-MM-DD_short-title` | as published |
| `sources/summaries/` | One summary per original, in relation to the Leitfrage | English |
| `notizen/` | Personal notes; templates for notes, protocols and project documents in `notizen/_vorlagen/` | German |
| `eingang/` | Raw material to process: transcripts, mails, feedback. Local only, not committed | as received |
| `protokolle/` | Distilled protocols made from the inbox, and the offer drafts that follow from them | German |
| `projekte/` | One project document per client project (type `kundenprojekt`, template `notizen/_vorlagen/kundenprojekt.md`, optional property `status` with one of `anfrage`, `angebot`, `beauftragt`, `abgeschlossen`, set only by the operator and shown in the Bases view Projekte): client by role, inquiry, governance check, deliverables with their state, decisions, open questions, next steps, links to protocols, offers and knowledge; `ACTIVE-WORK.md` lists each project and points here | German |
| `uebersicht.base` | Obsidian Bases tables of all documents, notes and protocols, embedded in HOME | |
| `scripts/` | Checks and builds (see below) | code in English |
| `dashboard/` | Card dashboard with reader: rules of both rule documents, sources with full text, knowledge documents, notes and protocols. Source of the shared frontend (`index.html`, `app.js`, `style.css`, `assets/`); its data built by `scripts/build_dashboard.py` | German interface |
| `dashboard/northwind/` | Revenue page for the Northwind exercise data, only sums, data built by `scripts/northwind_umsatz.py --web` | German interface |
| `public/` | Public build of the same dashboard: guidelines and sources with summaries. Frontend copied from `dashboard/` and data written by `scripts/build_dashboard.py`; edit the frontend in `dashboard/` only | German interface |
| `output/` | Generated PDF, previews, CSV exports and screenshots, not committed | |
| `assets/` | DHCraft logo used by the PDF build | |
| `ruff.toml` | Lint configuration for the scripts | |
| `.claude/skills/pitch/` | Procedure for a pitch of at most five slides from the knowledge base: outline with sources, approval in the chat, only then the deck | English |
| `.claude/skills/source-backed-governance/` | The research-to-draft procedure of this knowledge base as a reusable skill, without the vault layer; its `check_kb.py` is the knowledge check of this vault | English |

## Rules

- `knowledge/` follows its own conventions, described in [knowledge/INDEX.md](knowledge/INDEX.md). Every statement in a claim document (`leitlinien-dhcraft.md`, `governance-entwurf.md`) cites its original in `sources/` with a locator, as a Markdown link. Sources enter only with a date in 2026 checked on the source, or under an exception the owner approved and `project.md` records.
- Every Markdown document in `HOME.md`, `ACTIVE-WORK.md`, `knowledge/`, `notizen/`, `protokolle/` and `projekte/` starts with a frontmatter block holding `title`, `type`, `language`, `tags` and `related`. `type` is one of `home`, `active-work`, `index`, `projekt`, `kundenprojekt`, `regeln`, `entwurf`, `quellen`, `journal`, `notiz`, `protokoll`, `angebot`, `taxonomie`, `daten`, `anforderungen`, `gliederung`.
- Tags come only from [TAG-TAXONOMY.md](TAG-TAXONOMY.md): `bereich/` (projekt, persoenlich), `feld/` (the four fields of the Leitfrage), `ziel/` (the three goals) and `thema/` for notes and protocols. A new tag is added there first, with its meaning.
- In `knowledge/`, links between documents stand as Wikilinks in the `related` property only. The body keeps Markdown links, because the check script, the PDF and the dashboard read it. `HOME.md`, `ACTIVE-WORK.md`, protocols, project documents and personal notes may use Wikilinks in the text.
- Personal notes carry `bereich/persoenlich` and make no claims for the knowledge base. A finding from a note enters `knowledge/` only with a stored source and a citation.
- `ACTIVE-WORK.md` points to the documents that hold the details instead of copying them, and carries no deadlines or priorities unless the operator sets them.

- Publication runs only through the separate repository `agentic-governance-workspace` under `Documents/GitHub`, served as GitHub Pages under DigitalHumanitiesCraft, following [public/README.md](public/README.md). It holds the card workspace from `public/`, the governance PDF, the pitch deck, the Northwind revenue page and an overview image. Stored originals, full texts of sources, `knowledge/`, notes, protocols and `eingang/` never enter it. DHCraft's own texts may name the company and the operator; real client or company data may not appear. A change to what is public is the operator's decision.

## Processing the inbox

When asked to process `eingang/`, for each file:

1. Write a protocol in `protokolle/` named `YYYY-MM-DD_short-title.md` from the template `notizen/_vorlagen/protokoll.md`: occasion, decisions, open questions, proposals for the knowledge base. Refer to people by role, not by name, and quote nobody beyond what a decision needs.
2. Add decisions that change the running state and new open questions to `ACTIVE-WORK.md`, each with a Wikilink to the protocol; for a client project they go into its document in `projekte/`, and `ACTIVE-WORK.md` keeps only its state, next step and link. Close questions in `ACTIVE-WORK.md` that the material answers.
3. A meeting or mail is no source. What it decides enters `governance-entwurf.md` only in its sections "Festlegungen" or "Annahmen und offene Punkte", never as a cited rule. A claim it makes about law or practice becomes a research question, answered from `sources/` or by a new stored source.
4. Propose changes to `knowledge/` in the chat and apply them only after the operator agrees.
5. Leave the raw file in `eingang/`; the operator deletes it. Material a script still reads, such as exercise data, stays until its work is done, and the protocol records where it came from. Run the checks.

## Checks and builds

Run after every change, from this folder:

```bash
python .claude/skills/source-backed-governance/scripts/check_kb.py . --window 2026
python scripts/check_vault.py
uv run scripts/build_dashboard.py
```

After a change to the Northwind exercise data or its scripts:

```bash
uv run scripts/northwind_umsatz.py --web
uv run scripts/northwind_check.py
```

The knowledge check is the skill's `check_kb.py`: citations, the source list, the date window (2026, or an approved exception) and the summaries; sections headed Annahmen, Offene Punkte, Lücken or Festlegungen need no citations. `check_vault.py` checks frontmatter, Wikilinks and Markdown links for dead targets, and tags against the taxonomy. `build_dashboard.py` also writes `public/data.js` and copies the frontend from `dashboard/` into `public/`, both only when the public data passes its checks; it reports a file name used in two folders as an error, because links to it would be ambiguous. Rule entries in the dashboard come only from `leitlinien-dhcraft.md` and `governance-entwurf.md`. The governance PDF is built with `uv run scripts/build_governance_pdf.py` and then inspected page by page. `northwind_umsatz.py --web` rebuilds the data of `dashboard/northwind/` from the exercise files in `eingang/`, and `northwind_check.py` recomputes every key figure independently and compares it with the page and the protocol.

Some rules are kept by hand rather than by a script: Wikilinks in `knowledge/` only in `related`, `bereich/persoenlich` on personal notes, and the language of each folder.

## Boundaries

- The operator's main Obsidian vault is not read or written from here; this vault stands on its own for the workshop.
- The git repository is the parent folder `Downloads`, shared with unrelated material. Stage only paths under `wissensbasis/` by name and leave other changes in the working tree alone. Pushes stay with the operator.
