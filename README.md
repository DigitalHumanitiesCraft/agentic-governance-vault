# Agentic Engineering und Governance, the vault

This is the Obsidian vault in which Digital Humanities Craft (DHCraft), a small research and software firm in Graz, worked out rules for AI agents in client projects, research and programming during a workshop in November 2026. It holds a source-backed knowledge base, the governance draft as Beschlussvorlage 1.0, notes, protocols, a fictional exercise project and the scripts and skills that build and check all of it. The published results are at https://dhcraft.org/agentic-governance-workspace/.

The vault is German in its notes and governance draft and English in its knowledge base. [CLAUDE.md](CLAUDE.md) describes layout, rules and checks, [HOME.md](HOME.md) is the map of content, and [ACTIVE-WORK.md](ACTIVE-WORK.md) the running state.

## What is not included

The stored originals of the sources in `sources/` are not part of this copy, because they belong to their publishers. Every original is listed with its link at the publisher in [knowledge/quellen.md](knowledge/quellen.md), and its own summary lies in `sources/summaries/`. Citations in the knowledge base point to these originals and therefore lead nowhere until they are downloaded under the listed file names. The raw inbox `eingang/` with the exercise mail and the Northwind sample data, generated files and Obsidian workspace state are left out as well.

## Use

Open the folder as a vault in Obsidian. To run the checks and builds, download the originals into `sources/` and run from this folder:

```bash
python .claude/skills/source-backed-governance/scripts/check_kb.py . --window 2026
python scripts/check_vault.py
uv run scripts/build_dashboard.py
```

The dashboard then opens from `dashboard/index.html` by double click. Without the originals, the checks report each missing file, and the dashboard still builds but shows only the rules, knowledge documents, notes and protocols, without source cards. The summaries can be read directly in `sources/summaries/`.

## Provenance

The repository is an export of the working vault made by `scripts/export_public_vault.py`, which copies only committed files and drops the originals. The rules are a working state of an organisation and no legal advice. The Northwind client is fictional; its exercise data are Microsoft sample data.

## Licence

Texts under CC BY 4.0, code under MIT, see [LICENSE.md](LICENSE.md).
