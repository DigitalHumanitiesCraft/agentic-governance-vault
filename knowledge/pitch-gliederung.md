---
title: Pitch-Gliederung Regeln für AI Agents
type: gliederung
language: de
tags:
  - bereich/projekt
  - feld/projekte
  - feld/forschung
  - feld/programmierung
  - feld/organisation
  - ziel/regelkonform
  - ziel/sicher
  - ziel/nachpruefbar
related:
  - "[[leitlinien-dhcraft]]"
  - "[[governance-entwurf]]"
---
# Pitch-Gliederung Regeln für AI Agents

Diese Gliederung ist der Entwurf eines Pitch mit fünf Folien für die Eigentümer und Partner von Digital Humanities Craft (DHCraft), einem kleinen Forschungs- und Softwareunternehmen in Graz. Er beantwortet die Leitfrage aus [project.md](project.md): Welche Regeln braucht DHCraft, damit AI Agents in Projekten, Forschung und Programmierung regelkonform, sicher und nachprüfbar arbeiten? Der Pitch soll die Beschlussvorlage in [governance-entwurf.md](governance-entwurf.md) vorbereiten.

Der Operator hat den Text aller fünf Folien am 5. November 2026 im Chat abgenommen. Spätere Änderungen am Folientext gehen wieder über den Chat, bevor sie in den Foliensatz kommen. Jede Aussage stützt sich nur auf [leitlinien-dhcraft.md](leitlinien-dhcraft.md), den Governance-Entwurf und die Originale in `sources/` und nennt ihre Quelle mit Seite oder Abschnitt. Jeder Folienpunkt trägt eine Aussage in höchstens etwa zwölf Wörtern. Die Sprechernotizen stehen als Zitatblock darunter und erläutern die Aussagen der Folie aus denselben Quellen, ohne neue hinzuzufügen. Die Status in Klammern folgen dem Vokabular aus [INDEX.md](INDEX.md); empirische Ergebnisse tragen den Status Befund. Die rechtlichen Einschätzungen sind keine Rechtsberatung.

## Folie 1: Warum DHCraft jetzt Regeln braucht

- Maßnahmen zur KI-Kompetenz aller, die für uns arbeiten, sind Pflicht (Pflicht) ([Reg. 2026/1744, PDF S. 16](../sources/EU-Parlament-Rat_2026-07-08_verordnung-2026-1744-digital-omnibus-ki.pdf)).
- Die DSGVO gilt neben dem AI Act weiter (Pflicht) ([DSB 1/2026, PDF S. 3](../sources/DSB-AT_2026_newsletter-1-2026-ki-und-datenschutz.pdf); [DSB 1/2026, PDF S. 4](../sources/DSB-AT_2026_newsletter-1-2026-ki-und-datenschutz.pdf)).
- Agents, die mit Menschen sprechen, geben sich als KI zu erkennen (Pflicht) ([Art. 50 Guidelines 2026, PDF S. 13](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf)).
- Der FWF sanktioniert erfundene Referenzen in Anträgen (Vorgabe) ([FWF 2026, Abschnitt Penalties for improper use of AI](../sources/FWF_2026-07-07_ki-in-foerderantraegen.md)).

> Sprechernotiz: Einstieg über die Lage, nicht über die Technik. Die Kompetenzpflicht verlangt kein bestimmtes Niveau und kein Zertifikat. Der AI Act ist keine Rechtsgrundlage für eine Datenverarbeitung, dafür bleibt die DSGVO maßgeblich. Der FWF kann bis zur Antragssperre oder Rückforderung gehen. Die Leitfrage zum Schluss der Folie vorlesen.

## Folie 2: Projekte: Kundenmaterial bleibt unter Kontrolle

- Vor dem Start werden Datenflüsse und Rollen jedes Dienstes dokumentiert (Empfehlung) ([AEPD 2026, PDF S. 33](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).
- Bei Personendaten ist eine Folgenabschätzung zu prüfen (Pflicht) ([AEPD 2026, PDF S. 39](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf); [DSB 1/2026, PDF S. 4](../sources/DSB-AT_2026_newsletter-1-2026-ki-und-datenschutz.pdf)).
- Agents erhalten nur die Zugänge ihrer aktuellen Aufgabe (Empfehlung) ([Five Eyes 2026, PDF S. 7](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).
- Kunden erfahren, welche KI-Werkzeuge ihr Material verarbeiten (Ableitung) ([ERA Guidelines 2026, PDF S. 10](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).

> Sprechernotiz: Personenbezogene Daten sind bei DHCraft selten, die Folie gilt für genau diese Fälle. Ein Agent in einer solchen Verarbeitung verlangt einen neuen Durchgang des Risikomanagements. Die Rechte eines Agents bestimmen, wie viel Schaden er anrichten kann. Kunden erfahren auch, wie ihr Material geschützt ist.

## Folie 3: Forschung: Die Verantwortung bleibt bei den Forschenden

- Wesentliche KI-Nutzung in FWF-Anträgen wird offengelegt (Vorgabe) ([FWF 2026, lead text](../sources/FWF_2026-07-07_ki-in-foerderantraegen.md); [ERA Guidelines 2026, PDF S. 7](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Jede Referenz eines Agents wird am Original geprüft (Vorgabe) ([FWF 2026, Abschnitt Penalties for improper use of AI](../sources/FWF_2026-07-07_ki-in-foerderantraegen.md); [ERA Guidelines 2026, PDF S. 9](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Methodische Entscheidungen bestätigt immer ein Mensch (Empfehlung) ([ERA Guidelines 2026, PDF S. 7](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Vertrauliches aus Begutachtungen geht nur an gesicherte oder lokale Systeme (Vorgabe) ([DFG 2026, PDF S. 2–3](../sources/DFG_2026-03_leitlinie-ki-in-der-begutachtung.pdf)).

> Sprechernotiz: Der FWF nimmt Literaturrecherche von der Offenlegung aus, die ERA-Leitlinien zählen eine KI-gestützte Literaturrecherche aber als wesentliche Nutzung. Offenlegen ist deshalb die sichere Wahl, und hier schafft eine Hausregel Klarheit. Geprüft werden auch Faktenaussagen. Der Einsatz eines Agents überträgt nie Kontrolle oder Verantwortung. Die DFG-Regel betrifft Gutachten, nicht eigene Anträge; gesichert heißt dort vertraglich zugesichert, ohne Nutzung der Eingaben durch den Anbieter.

## Folie 4: Programmierung: Grenzen technisch durchsetzen

- Kein Agent vereint fremde Eingaben, sensible Daten und selbstständiges Handeln (Empfehlung) ([AEPD 2026, PDF S. 39–40](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).
- Coding Agents arbeiten in einer Sandbox mit eng begrenztem Netz (Empfehlung) ([NCSC-UK 2026, Abschnitt Control the AI agent's environment with a robust sandbox](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- Folgenreiche Schritte brauchen eine Freigabe, die das Werkzeug erzwingt (Empfehlung) ([Five Eyes 2026, PDF S. 22](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [NCSC-UK 2026, Abschnitt Prompt carefully](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- Abgelehnte Pull Requests von Agents sind meist groß und unabgestimmt (Befund) ([Failed agentic PRs 2026, PDF S. 1](../sources/arXiv_2026-01-21_failed-agentic-pull-requests.pdf); [Failed agentic PRs 2026, PDF S. 2](../sources/arXiv_2026-01-21_failed-agentic-pull-requests.pdf)).

> Sprechernotiz: Die Folie mit dem meisten Alltagsbezug. Wo die drei Eigenschaften zusammenkämen, gibt ein Mensch frei, bevor der Agent handelt. Die Sandbox lässt nur freigegebene Netzziele zu, und Zugangsdaten sind kurzlebig. Eine Anweisung im Prompt allein ist keine Kontrolle. Aus dem Befund folgt die Hausregel, Agent-Änderungen klein und abgestimmt zu halten.

## Folie 5: Organisation: Was die Eigentümer beschließen

- Eine benannte Person verantwortet den Einsatz von Agents (Empfehlung) ([NCSC-UK 2026, Abschnitt Set the right level of oversight](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- Ein Register führt die freigegebenen Werkzeuge in festen Versionen (Empfehlung) ([Five Eyes 2026, PDF S. 18](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [ERA Guidelines 2026, PDF S. 11](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Agents starten mit risikoarmen Aufgaben ohne sensible Daten (Empfehlung) ([Five Eyes 2026, PDF S. 4](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [Five Eyes 2026, PDF S. 19](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).
- Protokolle sind geschützt, und jeder Agent lässt sich sofort anhalten (Empfehlung) ([NCSC-UK 2026, Abschnitt Observability](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md); [Five Eyes 2026, PDF S. 20](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [NCSC-UK 2026, Abschnitt Emergency shutdown](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).

> Sprechernotiz: Die Selbstständigkeit der Agents wächst erst mit der Erfahrung. Die Protokolle sind auch gegen Änderungen durch den Agent selbst geschützt. Überleitung zur Bitte an die Eigentümer, die Beschlussvorlage 1.0 der Governance zu beschließen. Die Folie nennt bewusst keine einzelnen Dienste, welche Werkzeuge freigegeben sind, steht im Register.

## Offene Punkte

- Der Pitch endet mit der Bitte, die Governance als Beschlussvorlage 1.0 zu beschließen. Das ist eine Festlegung von DHCraft und keine Aussage der Quellen; ob sie als eigene Schlussfolie oder als Satz auf Folie 5 erscheint, entscheidet die Abnahme.
- Keine Quelle aus 2026 behandelt Digital-Humanities-Abläufe oder Agents in der Literatur- und Quellenarbeit, und die empirischen Studien sind Preprints. Folie 3 und Folie 4 stützen sich deshalb auf allgemeine Leitlinien und auf einen Befund ohne Peer Review.
- Die Regeln zur Datenschutzbeauftragten Person und zur Kennzeichnung veröffentlichter Texte stehen in den Leitlinien, passen aber nicht mehr auf fünf Folien. Sie können eine Folie ersetzen, wenn die Abnahme das wünscht.
- Gestaltung, Titelfolie und Folienformat werden erst nach der Abnahme des Textes festgelegt.
