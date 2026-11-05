# Card dashboard

A local page for working with the knowledge base. Every rule, source, knowledge document, note, protocol and project document is a card. Rules come from the guidelines and the governance draft, grouped by rule document and field or section, each with its status, goal and sources. Search and filters (kind, rule document, field, status, goal, kind of source) stand on the left. Selecting a rule or a source opens a side panel with its details and marks the connected cards: the sources a rule rests on, or the rules that rest on a source. A source's panel leads to its full text, a knowledge document or note card opens its text directly. In the reader, citations open the cited source at its PDF page, and each source lists the rules that cite it.

Create or refresh the data after every change to `knowledge/`, `sources/`, `notizen/`, `protokolle/` or `projekte/`:

```bash
uv run scripts/build_dashboard.py
```

Then open `dashboard/index.html` by double click. No server is needed. The data file `data.js` is generated and not committed.

Search terms must all occur. Put a phrase in double quotes. Umlauts and ß match their spelled-out forms (`massnahme` finds `Maßnahme`), and hyphens count as spaces. Many sources are English, so an English term finds more there. While searching, a card shows where the term occurs in the full text, and each find opens the text at its page. With a document open, a search keeps it open and marks the finds. Enter in the search field, or F3, jumps to the next find. The page field jumps within a PDF, and "PDF öffnen" opens the original at the page in view. Escape closes the panel or the reader, and browser Back returns to the previous place, including its scroll position.

## One frontend, two builds

`index.html`, `app.js`, `style.css` and `assets/` in this folder are the only source of the frontend. The build copies them into `public/` together with the public data, which holds source metadata, own summaries and the rules of the guidelines. The page shows only what its data holds, so the public copy has no reader, no rule document filter and no links to local pages. Edit the frontend here, never in `public/`. See [public/README.md](../public/README.md) for what is published.

The subfolder `northwind/` is a separate page with the revenue of the Northwind exercise data, linked from the head of the dashboard. Its data comes from `uv run scripts/northwind_umsatz.py --web` and holds sums only.
