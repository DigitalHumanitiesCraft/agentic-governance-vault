# Public card workspace

A static page that shows the guidelines of the knowledge base as cards, each rule with its status, goal and sources, and each source with its own summary and a link to the original at its publisher. Visitors filter by field, status, goal and kind of source, select a card and follow the connections between rules and sources.

It is the public build of the card dashboard in `dashboard/`. `index.html`, `style.css`, `app.js` and `assets/` here are copies that the build writes; edit them in `dashboard/` only, a change made here is overwritten by the next build.

## What is public

The page contains only what `scripts/build_dashboard.py` writes into `public/data.js`:

- metadata of every source (title, publisher, date, category, link to the publisher),
- the own summary of every source, with links into the private base removed,
- the rules of `knowledge/leitlinien-dhcraft.md` with status, goal, field and cited pages,
- only when built with `--public-work`: the Arbeitsbereich, meaning the lists of `ACTIVE-WORK.md` and the project documents in `projekte/` (state, next steps, deliverables, open questions, decisions, applied rules) and the sums of the Northwind revenue data. Whether it is public is the operator's decision and not yet taken, so the plain build leaves it out. Its links to the revenue page and the governance draft point to `northwind/` and the Beschlussvorlage in `material/` on the site. Other links point to the file in the public vault repository `agentic-governance-vault` where that repository holds it outside `knowledge/`, `protokolle/`, `notizen/` and `sources/`, otherwise they are plain text.

The stored originals, their full text, the governance draft, the other knowledge documents, notes and protocols are not part of it as documents. The build reports an error, and writes no public data, if the public data contains a link that is not a web URL, a document other than a source, a vault link to a file that repository does not hold or into its `knowledge/`, `protokolle/`, `notizen/` or `sources/`, a link to `knowledge/` or `sources/` of the site, or a project rule that resolves to no public rule or to several.

## Build and publish

```bash
uv run scripts/build_dashboard.py                 # without the Arbeitsbereich
uv run scripts/build_dashboard.py --public-work   # with it, once the operator has decided so
```

The folder `public/` is then complete: `index.html`, `style.css`, `app.js` and `assets/` copied from `dashboard/`, and `data.js`. The card workspace runs by double click and needs no server. The pages of the link bar and the revenue page linked from the Arbeitsbereich exist only in the workspace repository, so locally these links lead nowhere.

Links into the vault repository show its committed state. Before publishing, commit the changed vault files, run `uv run scripts/export_public_vault.py`, then build, so a linked project document carries what the page shows. To publish it, copy `index.html`, `style.css`, `app.js`, `data.js` and `assets/`, but not this README, into the root of the repository `agentic-governance-workspace` under `Documents/GitHub`, whose own README.md and LICENSE.md describe the published site. The card workspace is thus the start page. Its link bar (`PUBLIC_LINKS` in the build script) points to pages the repository keeps beside it: the governance PDF and the pitch deck from `output/` in `material/`, a copy of `dashboard/northwind/` in `northwind/` whose back link points to the start page, the public vault repository, and `ueber.html` on provenance, limits and licence. `leitlinien/index.html` there only forwards old links to the start page. GitHub Pages serves its main branch at https://dhcraft.org/agentic-governance-workspace/. Never publish this repository itself, because it contains `knowledge/` and `sources/`.

## Licences

Own texts and summaries: CC BY 4.0, Digital Humanities Craft. Code: MIT. The fonts Sora and Instrument Sans are under the SIL Open Font License, see `assets/fonts/`. The sources belong to their publishers.
