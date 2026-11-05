---
title: Agentic Engineering und Governance
type: index
language: en
tags:
  - bereich/projekt
related:
  - "[[project]]"
  - "[[leitlinien-dhcraft]]"
  - "[[governance-entwurf]]"
  - "[[quellen]]"
  - "[[journal]]"
---
# Agentic Engineering und Governance

This knowledge base answers one Leitfrage for Digital Humanities Craft (DHCraft), a small research and software company in Graz, Austria: which rules DHCraft needs so that AI agents work lawfully, securely and verifiably in projects, research and programming. It rests on sources published in 2026, with one exception approved for the question of a data protection officer and recorded in [project.md](project.md).

## Documents

| Document | Question it answers |
| --- | --- |
| [project.md](project.md) | Which Leitfrage applies, for whom, and what remains open? |
| [leitlinien-dhcraft.md](leitlinien-dhcraft.md) | Which rules follow for DHCraft, which goal does each serve, and how binding is it? |
| [governance-entwurf.md](governance-entwurf.md) | How do the rules become a governance DHCraft can adopt? German Beschlussvorlage 1.0, rendered as PDF by `scripts/build_governance_pdf.py` into `output/`. |
| [quellen.md](quellen.md) | Which sources underlie the rules, with publisher, date, link, category and summary? |
| [journal.md](journal.md) | How did the knowledge base come about? |
| [pitch-gliederung.md](pitch-gliederung.md) | How does the answer reach the owners in at most five slides? German outline awaiting approval; a claim document that restates rules of the guidelines with their sources. |
| [northwind/data.md](northwind/data.md), [northwind/requirements.md](northwind/requirements.md) | What do the Northwind exercise data contain, and what must the revenue page meet? Outside the claim and source system. |

The originals lie in [sources/](../sources/), a summary of each source in relation to the Leitfrage in [sources/summaries/](../sources/summaries/).

## Glossary

### regelkonform

The rule serves compliance with law, data protection or funder requirements.

### sicher

The rule protects data, systems and clients against errors and attacks by or through agents.

### nachprüfbar

The rule keeps agent work traceable and checkable for DHCraft, clients, reviewers and readers.

### Pflicht

Binding by law, here the AI Act as amended by Regulation (EU) 2026/1744 and the GDPR.

### Vorgabe

Binding requirement of a funder or organisation, sanctioned within its sphere, such as the FWF's disclosure duty.

### Empfehlung

Guidance by an authority or body without binding force.

### Ableitung

A rule DHCraft draws from cited findings that the sources themselves do not state as a rule.

### Befund

An empirical result of a study.

## Method

Two research agents searched in parallel, one on applicable rules (law, data protection, funders) and one on working practice (security guidance, empirical studies). Each source was admitted only if it was published in 2026 with the date verified on the source (or under the exception recorded in [project.md](project.md)), came from an authority, a recognised body or a scientific study, and was available in full text. A later targeted search added the sources on the data protection officer. Two further agents summarised each source in relation to the Leitfrage. Every quoted passage, both in the rules and in the summaries, was checked against the stored original.

Each rule cites its source file with a locator in the form `[Label, PDF p. 4](../sources/file.pdf)`, where PDF p. is the page in the PDF file. The skill's script `.claude/skills/source-backed-governance/scripts/check_kb.py` checks that every rule carries such a citation, that every cited file exists, that [quellen.md](quellen.md) lists every stored source exactly once, and that every source has its summary.

## Tools

| Tool | What it does |
| --- | --- |
| `python .claude/skills/source-backed-governance/scripts/check_kb.py . --window 2026` | Checks citations, the source table, the date window and the summaries. Must report 0 problems after every change. |
| `scripts/check_vault.py` | Checks frontmatter, tags against the taxonomy, Wikilinks and Markdown links of the vault. Must report 0 problems. |
| `scripts/build_governance_pdf.py` | Renders [governance-entwurf.md](governance-entwurf.md) as PDF into `output/`, which is not committed. |
| `scripts/build_dashboard.py` | Builds the data of the card dashboard in `dashboard/`, with each rule and the sources it cites. It also writes the public data in `public/data.js` and copies the shared frontend from `dashboard/` into `public/`, see [public/README.md](../public/README.md). Its use is described in [dashboard/README.md](../dashboard/README.md). |
| `.claude/skills/source-backed-governance/` | The research-to-draft procedure of this knowledge base as a reusable skill for other topics and organisations, without the vault layer described in CLAUDE.md. |

## Continuing the work

A new source is stored in `sources/` under the name `Publisher_YYYY-MM-DD_short-title`, gets its row in [quellen.md](quellen.md) with the date checked on the source, and its summary in `sources/summaries/`. Rules that rest on it cite it with a locator in [leitlinien-dhcraft.md](leitlinien-dhcraft.md) and, where they change the governance, in [governance-entwurf.md](governance-entwurf.md). Afterwards the knowledge check must pass, and the PDF and the dashboard data are built again. Open questions on the sources stand in [project.md](project.md), open organisational inputs in the section "Annahmen und offene Punkte" of the governance draft.
