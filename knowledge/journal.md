---
title: Journal
type: journal
language: en
tags:
  - bereich/projekt
related:
  - "[[INDEX]]"
  - "[[project]]"
---
# Journal

## 2026-11-05 One dashboard in card style and a public copy of the vault

The internal dashboard and the public card workspace now share one frontend in the card style of the workspace. `dashboard/` holds the source, and `scripts/build_dashboard.py` copies it into `public/` with the public data, where controls without data are absent. The internal build adds the reader with full texts page by page, notes, protocols and project documents. `scripts/export_public_vault.py` copies the committed vault without the stored originals and the inbox into the repository `agentic-governance-vault`.

Evidence: a Playwright test over both builds via file:// passed after an independent review and its fixes, covering search with umlaut variants, filters, citation jumps, keyboard use, 200 percent zoom and widths down to 320 px; the knowledge check, check_vault.py and northwind_check.py pass.

## 2026-11-05 Three 2026 sources stored and integrated

The earlier entry misread the operator: the answer "without originals" concerned only the planned public copy, never storing originals in this vault. The Code of Practice on transparency of AI-generated content, the CNIL and CIANum note on agentic AI and the BSI security information were therefore stored with original and summary and integrated into quellen.md, project.md and the rules; two new rules cover separated agent memories and real human decisions under Article 22 GDPR, one covers the review policy and label form under the Code. Several CNIL locators in the summary counted printed instead of PDF pages and were corrected.

Evidence: every quote of the three summaries was found on its cited PDF page with pdftotext; page counts and 2026 dates were checked on the PDFs and the publisher pages.

## 2026-11-05 Sources on DH research, research software and agent code review

Three research agents searched for the open points in project.md: Digital Humanities and research integrity, data protection and security authorities, and review and test practice for agent-written code. Seven sources entered with original and summary: the ÖAWI guideline on good scientific practice, the ReSA report on research software, the JOHD study on LLM encoding in TEI, the HistoRAG preprint on historical source work, the OpenSSF and CNCF guide on open source security, a preprint on security debt in agent pull requests, and an NCSC-UK blog post on vibe coding. They added rules on disclosure and responsibility in research, TEI encoding, source work, dependency and secret checks, and code review, and extended existing rules with further citations instead of duplicating them. The Code of Practice on labelling AI-generated content, a CNIL note on agentic AI and a BSI security information were read but at first not taken in, on a misreading of the operator's answer (corrected in the entry above); their summaries were moved out of the vault and later restored. The agents rejected further candidates for date, access, relevance or vendor origin, among them a CISA paper on open source security that could not be retrieved. Candidate rules on AI-assisted vulnerability reports and on written expectations for research software were left out, the first as outside the Leitfrage, the second because the governance itself fulfils it.

Evidence: every rule quote was found on its cited page with pdftotext or in the stored page copy. The Zenodo record of the ÖAWI guideline states July 2026 as publication date. The knowledge check, check_vault.py and the dashboard build ran clean afterwards.

## 2026-11-05 Client projects managed through project documents

Client projects now have one German project document each in `projekte/`, type `projekt`, from the template `notizen/_vorlagen/projekt.md`. ACTIVE-WORK.md gained a section Projekte that holds per project only its state, next step and a link, and the Northwind lines moved there. The Northwind exercise is the first project, `projekte/northwind-traders.md`, pointing to its protocol, offer draft, data description, requirements and revenue page. check_vault.py, the dashboard build and the Bases overview read the new folder.

Evidence: `python scripts/check_vault.py` reports 0 problems, and the dashboard build lists the project document as a note labelled Projekt.

## 2026-11-05 Pitch deck and publication

The pitch outline was approved, and `scripts/pitch/build_pitch.py` builds the deck from it with the dhcraft-pptx helpers. A visual and an argument review ran; their findings are not yet applied, among them that the PR statement on slide 5 overstates its study. The operator decided to publish the workshop results under DigitalHumanitiesCraft, and https://dhcraft.org/agentic-governance-workspace/ now serves a start page, the card workspace, the governance PDF, the pitch deck and the Northwind page. Originals and full texts of sources stay unpublished.

Evidence: the local copy of the site returned 200 for every linked path, showed no console errors and no horizontal overflow at 1280 and 375 px, and contains no link into `knowledge/`, `sources/` or local paths.

## 2026-11-05 Workflow run: open findings, workshop gaps and a real skill run

A workflow of seven owner agents, each followed by an adversarial reviewer and a fix pass, and a final completeness critic implemented the remaining work:
- The build script lets the Markdown parser escape raw HTML, so inline code is no longer escaped twice. Only dot leaders are removed from PDF pages, so table-of-contents pages keep their text. A file name used in two folders is a build error.
- TAG-TAXONOMY.md is now the source of the tag taxonomy, and check_vault.py reads it, covers knowledge/ recursively, reports ambiguous Wikilinks and checks Markdown links in angle brackets.
- The skill's check_kb.py validates real dates and reads only the first table of quellen.md.
- The pages find "Maßnahme" and "Massnahme" alike, the public page explains on an empty rule search that the rules are English, and keyboard use, 200 percent zoom and reflow were tested and fixed.
- knowledge/northwind/ describes the exercise data and the requirements of the revenue page, and scripts/northwind_check.py recomputes every key figure independently.
- knowledge/pitch-gliederung.md is a German five-slide outline with sources awaiting approval, and the skill .claude/skills/pitch/ records the procedure. No deck exists yet.
- A real run of source-backed-governance with live web search on generative AI in university teaching, in Downloads/skill-testlauf, went through to a five-page PDF. Its findings went into the skill: delegated gates, a fallback without subagents, script location, a pdftotext fallback for multi-column pages, alternative official channels for blocked originals, year-only file names, law excerpts and consolidated versions, a German PDF term for the marker current, and a resolved output path in build_pdf.py, whose relative --out failed.

After the run, the dashboard takes rule entries only from the two rule documents and no longer from the preamble or the pitch outline, and it reads knowledge/northwind/.

Evidence: the knowledge check reports 3 claim documents, 17 sources and 0 problems; check_vault.py reports 0 problems; northwind_check.py reports 2302 comparisons and 0 failures; ruff is clean; the reviewers' issues were fixed or answered; the test PDF rebuilt with the corrected script shows no English marker.

## 2026-11-05 Governance as Beschlussvorlage 1.0

The operator decided that the governance names no individual services and does not describe current agent practice, and stated that DHCraft works mainly with public-domain or freely usable humanities research data, with personal data rare. The draft became a Beschlussvorlage 1.0: the preamble and the data classes reflect the data situation, the assessment on the data protection officer rests on it, a section Festlegungen records the two decisions, and a Beschluss block awaits date and signatures of both owners. The open questions on services, contracts and external action were removed from the draft, project.md and ACTIVE-WORK.

Evidence: the knowledge check and `check_vault.py` report 0 problems; the PDF `DHCraft_Governance_AI_Agents_Beschlussvorlage_v1.0.pdf` renders ten pages, each inspected as an image.

## 2026-11-05 Review round on scripts, pages and curation

Three independent review agents checked the scripts, the three web pages and the curation of the vault. Fixed after verification:
- The public build now fails closed. It writes nothing when its data would contain a local link, and it drops images.
- Public rules keep their field when a subsection is added.
- A short row in quellen.md is reported instead of crashing the build.
- The vault check parses flow-style tags, accepts PDF page links and path-style Wikilinks, and covers subfolders of protokolle/.
- The Northwind script resolves every key before it sums, opens each workbook once and reports unusable lines.
- The vault's own older copy of check_kb.py was removed. The skill's script, which knows "Festlegungen", subsections and code blocks, is now the knowledge check.
- On the pages: the skip link of the public page works, closing a panel goes back instead of adding history entries, and the covered content becomes inert under an overlay panel. Focus returns to the opening hit or control on every page. Dashboard links keep the active filters, finds are marked only in content, and the revenue page keeps its table open and shows round axis values.
- CLAUDE.md, HOME, INDEX, the READMEs and ACTIVE-WORK now describe the current layout, the publishing route and the git boundary. The governance draft states in its preamble that it is no legal advice.

Evidence: the knowledge check and `check_vault.py` report 0 problems; ruff is clean; a copy with planted errors showed the fail-closed public build, the kept field and the reported short row; 17 keyboard and browser checks with Playwright pass; the PDF renders ten pages.

## 2026-11-05 Northwind exercise data, revenue analysis, offer and reply

The four attachments of the Northwind inquiry turned out to be the Northwind sample database, converted for a session of the workshop on 9 November, and are fictional. `scripts/northwind_umsatz.py` computes revenue by product, delivery country and month locally from Orders, Order Details, Products and Categories, and never opens the customer or employee files. `--csv` writes the full rankings to output/, `--web` the sums for the revenue page in `dashboard/northwind/`. An exercise offer draft, with the new document type `angebot`, and a reply draft stand in protokolle/. Neither carries an offer number or went to Thunderbird.

Evidence: a second, independent computation gives the same total of 1,265,793.04; the revenue page was exercised in the browser with linked filters.

## 2026-11-05 Client inquiry and a talk curated into the vault

An inquiry from Northwind Traders for a workshop, slides, a web page and AI rules for its sales team was checked against the governance draft and recorded as a protocol; its raw text stays local in the inbox, and its attachments arrived later the same day, see the next entry. A talk on how open models can compete with closed labs was kept as a personal note, because a talk is no source under the rules of this base. ACTIVE-WORK now lists the inquiry, the prepared public repository and the decision whether the tool register should record open weights and local operation. The tag taxonomy gained `thema/offene-modelle`.

Evidence: `check_kb.py` and `check_vault.py` report 0 problems; the dashboard lists both notes; the public data contains neither.

## 2026-11-05 Public card workspace

The operator wants a public page where visitors click through the knowledge base, with every document as a card, and decided that only the guidelines are public, not the governance draft. Research in the vault and the operator's repositories found card and panel patterns but no card workspace of this kind; the vault rules allow cards for self-contained objects with comparable structure and reject nested boxes. The page in public/ combines the DHCraft tokens and fonts of the second-brain-vault site, hairline cards as in the KISUG explorer and the board with selection panel of the ACTIVE-WORK interface. Selecting a source marks the rules resting on it, selecting a rule marks its sources. The build writes only source metadata, own summaries and the guideline rules, and fails on any non-web link in the public data.

Evidence: the public data holds 17 sources and 31 rules, no full text and no link into the base; in the browser filters, selection, the jump from rule to source, Back and Escape with focus return work; wide, medium and narrow widths were inspected as screenshots; opened from the file system the page loads its data. The page has not been published.

## 2026-11-05 Inbox for protocols, rules as dashboard entries

The vault gained an inbox: raw material such as transcripts, mails and feedback goes to eingang/, which stays local because it carries names and statements of third parties, and an agent turns it into a protocol in protokolle/ following the rule in CLAUDE.md. A meeting or mail is no source; what it decides enters the governance draft only as a setting or assumption. A Bases view lists documents, notes and protocols in HOME. The dashboard now lists each cited rule as an entry with status, section and sources at their pages, filterable by status, and searches personal notes and protocols, with their Wikilinks resolved.

Evidence: `check_kb.py` and `check_vault.py` report 0 problems; the build yields 86 rules from the two claim documents; in the browser the status filter Pflicht lists 13 rules and a rule opens its passage in the governance draft; a test note with Wikilinks appeared under the kind Notiz with working links and was removed afterwards. The Bases view was not opened in Obsidian here.

## 2026-11-05 Folder set up as an Obsidian vault

The operator wants the folder as an Obsidian vault for both the project and personal knowledge. Every knowledge document now opens with a frontmatter block (title, type, language, tags, related); links between knowledge documents stand as Wikilinks in the related property only, because the check script, the PDF and the dashboard read the body. HOME.md is the map of content, ACTIVE-WORK.md the running state, notizen/ holds personal notes with a template, and CLAUDE.md records purpose, layout and rules. The tag taxonomy has the axes bereich, feld, ziel and thema and lives in scripts/check_vault.py, which also checks frontmatter and dead links. The PDF and dashboard scripts drop the frontmatter before rendering.

Evidence: `check_kb.py` and `check_vault.py` report 0 problems; `check_vault.py` found every error planted in a copy; the PDF renders with ten pages and no frontmatter; in the browser the dashboard shows the knowledge documents without frontmatter, a citation opens AEPD at page 33 and the search works.

## 2026-11-05 Dashboard reworked after an independent review

A review agent exercised the dashboard and found that it served finding documents but not working with evidence: searching closed the open document, Back lost the reading position, a source did not show which rules rest on it, German compound queries failed, and running headers and tables of contents of the PDFs supplied most snippets. The dashboard now shows filters, results and the open document side by side; a search inside an open document keeps it open; history entries keep scroll positions; every source lists the rules citing it with status, section and page; hits show up to three snippets with page links; the reader has a page field and opens the PDF at the page in view. The build drops repeated page headers and table of contents lines, treats hyphens as spaces and shows each source's bindingness in the header. The knowledge index gained a tools table and a section on continuing the work, and project.md now records the open organisational inputs.

Evidence: the build reports no errors; `check_kb.py` passes; in the browser a citation from the governance draft opened WP 243 at page 9 and Back returned to the same scroll position, search inside the AEPD guidance kept the document open, the page field jumped to page 50, and "Prompt-Injection", "Massnahme" and "pruefung" found their documents; wide, medium and phone widths were inspected as screenshots.

## 2026-11-05 Search dashboard

The operator asked for a local dashboard to search the knowledge base, opened by double click, showing for a PDF source its summary and the full text page by page, placed in `dashboard/`. `scripts/build_dashboard.py` writes the data as a JavaScript file because browsers block loading local JSON from the file system; it renders Markdown with raw HTML escaped and turns every citation into a link to the source at its PDF page. Search runs in the browser over all words, with phrases in quotes and umlaut folding. A German query finds little in the English sources, so the empty result says so.

Evidence: the build reports no errors and every page link lies within its PDF; in the browser, search, filters, the citation from the governance draft to page 16 of Regulation (EU) 2026/1744 (Article 4), the find buttons, Escape with focus return, and the phone width were exercised; over `file://` the data loads and the page jump is set.

## 2026-11-05 Skill revised after a second dry run

A second fresh agent ran the skill on an accessibility guideline for a software start-up and exercised both scripts on a hand-made folder. The procedure held; the scripts failed on subsections and numbering in exempt sections, on code blocks, on legal locators with commas and section locators, and found browsers only at two Windows paths. These are fixed: exemptions carry into subsections, code and quotes are skipped, the label ends at the first comma, the browser is searched on the PATH and on macOS, tables fold a basis column only when all its cells hold only links, the legend lists only used statuses, and a `current` marker admits the valid version of laws and standards. SKILL.md now creates project.md at the plan gate, defines the fields of the Leitfrage, checks dependencies at setup and describes verification of web and legal texts.

Evidence: the skill's scripts pass on this repository and on the dry-run probes that failed before; the workshop PDF renders with the same ten pages.

## 2026-11-05 Skill revised after a dry run

A fresh agent ran the skill as a dry run on an open access and research data policy for an institute library, reading only the skill folder. It found that a literal run would fail: the check script hard-coded the 2026 window and demanded summaries before they exist, the locator convention clashed with the PDF script, the status vocabulary differed between briefs, conventions and script, and description and draft name were tied to AI governance. The skill now takes window and summary check as parameters, accepts both locator forms and any link text, folds a basis column by position, uses one status vocabulary including Befund, sets the window as a decision in the plan step, adds gates after research and a setup step, and names its dependencies.

Evidence: the revised scripts pass on this repository and on a synthetic open access fixture; the PDF differs from the workshop PDF only in the generalised wording.

## 2026-11-05 Procedure extracted as a skill

The procedure of this session, from the context questions through research, distillation, Leitfrage, summaries, governance draft and PDF review, is now the skill `.claude/skills/source-backed-governance/`. It carries the gates at which the person decides, the agent briefs, the conventions enforced by the check script and the readability findings from the PDF review. Its two scripts are generalised copies of `scripts/check_kb.py` and `scripts/build_governance_pdf.py`, with organisation details as parameters.

Evidence: the skill's `check_kb.py` passes on this repository and finds the planted errors in a fixture; its `build_pdf.py` reproduces the governance PDF with identical page count, differing only in the generalised wording.

## 2026-11-05 Legal base texts on the data protection officer as an exception

The operator approved an exception to the 2026 window for the question of designating a data protection officer. An agent stored GDPR Recital 97 and Articles 37 to 39, the WP 243 guidelines of 2017 and the DSG provisions from RIS, each with a summary, and every quoted passage was checked against the original. The governance draft now carries a section on the data protection officer. Its assessment that DHCraft is presumably not obliged is marked as a derivation, together with a written check to be repeated when new project types or the revised EDPB guidelines appear. The check script accepts older sources only when quellen.md marks them as exception.

Evidence: `python scripts/check_kb.py` passes.

## 2026-11-05 Search on the duty to designate a data protection officer

A research agent searched for 2026 sources on Article 37 GDPR. No qualifying source states the criteria. The EDPB work programme 2026-2027 was added because it announces a targeted update of the DPO guidelines, and the governance draft now plans a review when that update appears. The pages of the Austrian Datenschutzbehörde on the topic carry no date and stay outside the knowledge base.

Evidence: `python scripts/check_kb.py` passes.

## 2026-11-05 Governance draft for DHCraft

The operator stated that DHCraft has two people, both owners, and asked whether a data protection officer is needed. The knowledge base recommends a data protection person in agent governance (AEPD) but holds no source on the legal duty under Article 37 GDPR, so that question stays open with a proposed web search. The activity profile of DHCraft comes from dhcraft.org, because the vault was ruled out for the workshop. The draft in governance-entwurf.md is written in German as an organisational document for adoption, introduces four data classes as a DHCraft derivation, and is rendered as a PDF with the watercolor logo.

Evidence: `python scripts/check_kb.py` passes with both claim documents, and the PDF was inspected page by page.

## 2026-11-05 Knowledge base aligned to the Leitfrage

The operator chose the Leitfrage on rules for lawful, secure and verifiable agent use and approved the cleanup plan. Two agents summarised every source in relation to the Leitfrage in `sources/summaries/`, and all quoted passages were checked against the cited PDF pages. The rules in leitlinien-dhcraft.md are now grouped by the fields of the Leitfrage, carry the goal they serve, and gained rules from the summaries, among them the Rule of 2 of the AEPD, hidden instructions in third-party documents, reference checking and a tool register. governance.md and agentic-engineering.md were dissolved into the rules and the summaries, their gaps moved to project.md. The AGENTS.md study stays as a source but feeds no rule, since it concerns effectiveness. The FWF and the ERA guidelines disagree on whether an AI literature review needs disclosure, and the rule names this conflict.

Evidence: `python scripts/check_kb.py` passes, including the new summary check.

## 2026-11-05 Digital Omnibus excerpt replaced by the Official Journal PDF

The operator downloaded the authentic PDF of Regulation (EU) 2026/1744. All passages cited from the former excerpt were found verbatim, and the citations now point to PDF pages.

Evidence: `python scripts/check_kb.py` passes.

## 2026-11-05 Knowledge base established

Built in a live workshop. The goal, the split into two research agents, the three quality criteria (provenance, verified 2026 date with bindingness, verifiability) and the document set were agreed with the operator before the research started.

Agent A (rules) delivered eight sources, agent B (practice) six. All dates and quoted passages were checked against the stored originals. The RTR FAQ was excluded because it states no date. The Digital Omnibus remains a verbatim excerpt because EUR-Lex blocked the automatic download of the authentic PDF.

Evidence: `python scripts/check_kb.py` passes.
