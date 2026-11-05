# Public card workspace

A static page that shows the guidelines of the knowledge base as cards, each rule with its status, goal and sources, and each source with its own summary and a link to the original at its publisher. Visitors filter by field, status, goal and kind of source, select a card and follow the connections between rules and sources.

It is the public build of the card dashboard in `dashboard/`. `index.html`, `style.css`, `app.js` and `assets/` here are copies that the build writes; edit them in `dashboard/` only, a change made here is overwritten by the next build.

## What is public

The page contains only what `scripts/build_dashboard.py` writes into `public/data.js`:

- metadata of every source (title, publisher, date, category, link to the publisher),
- the own summary of every source, with links into the private base removed,
- the rules of `knowledge/leitlinien-dhcraft.md` with status, goal, field and cited pages.

The stored originals, their full text, the governance draft, the other knowledge documents, notes and protocols are not part of it. The build reports an error if the public data contains a link that is not a web URL.

## Build and publish

```bash
uv run scripts/build_dashboard.py
```

The folder `public/` is then complete: `index.html`, `style.css`, `app.js` and `assets/` copied from `dashboard/`, and `data.js`. It runs by double click and needs no server. To publish it, copy `index.html`, `style.css`, `app.js`, `data.js` and `assets/`, but not this README, into the folder `leitlinien/` of the repository `agentic-governance-workspace` under `Documents/GitHub`, whose own README.md and LICENSE.md describe the published site. That repository also carries a start page, the governance PDF and the pitch deck from `output/` in `material/`, and a copy of `dashboard/northwind/` in `northwind/` whose back link points to the start page. GitHub Pages serves its main branch at https://dhcraft.org/agentic-governance-workspace/. Never publish this repository itself, because it contains `knowledge/` and `sources/`.

## Licences

Own texts and summaries: CC BY 4.0, Digital Humanities Craft. Code: MIT. The fonts Sora and Instrument Sans are under the SIL Open Font License, see `assets/fonts/`. The sources belong to their publishers.
