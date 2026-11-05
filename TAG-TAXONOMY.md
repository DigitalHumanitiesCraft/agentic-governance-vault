---
title: Tag-Taxonomie
type: taxonomie
language: de
tags: [bereich/projekt]
related: ["[[HOME]]"]
---
# Tag-Taxonomie

Diese Datei ist die einzige Quelle der Tags dieses Vaults. `scripts/check_vault.py` liest die erlaubten Tags aus ihr und meldet jedes Tag, das hier fehlt. Als Tag gilt jeder Eintrag, der als Listenpunkt mit einem Tag in Backticks beginnt. Ein neues Tag wird zuerst hier mit seiner Bedeutung eingetragen und erst danach in einem Dokument verwendet.

Die Taxonomie hat vier Achsen. `bereich` ordnet jedes Dokument der Projektarbeit oder dem Persönlichen zu, `feld` und `ziel` folgen der Leitfrage in [project.md](knowledge/project.md), `thema` erschließt Notizen und Protokolle quer dazu. Die Ziele sind im Glossar von [INDEX.md](knowledge/INDEX.md) definiert.

## Bereich

- `bereich/projekt`: Das Dokument gehört zur Projektarbeit, also zur Wissensbasis über Regeln für AI Agents bei DHCraft oder zu Protokollen, Angeboten und Projektdokumenten aus Kundenanfragen.
- `bereich/persoenlich`: Persönliche Notiz des Operators, die keine Aussagen für die Wissensbasis trifft.

## Feld

- `feld/projekte`: Kundenprojekte, in denen Agents Material von Kunden und personenbezogene Daten verarbeiten können.
- `feld/forschung`: Forschung einschließlich Förderanträgen und Begutachtung.
- `feld/programmierung`: Programmierung, in der Agents Code in Repositories schreiben und ändern.
- `feld/organisation`: Die Organisation von DHCraft selbst, etwa KI-Kompetenz, Zuständigkeiten und das Werkzeugregister.

## Ziel

- `ziel/regelkonform`: Die Regel dient der Einhaltung von Recht, Datenschutz oder Vorgaben von Förderern.
- `ziel/sicher`: Die Regel schützt Daten, Systeme und Kunden vor Fehlern und Angriffen durch oder über Agents.
- `ziel/nachpruefbar`: Die Regel hält die Arbeit von Agents für DHCraft, Kunden, Gutachter und Lesende nachvollziehbar und prüfbar.

## Thema

- `thema/datenschutz`: Datenschutz, insbesondere die DSGVO und der Umgang mit personenbezogenen Daten.
- `thema/ai-act`: Der AI Act in der Fassung der Verordnung (EU) 2026/1744 und die Leitlinien der Kommission dazu.
- `thema/foerderer`: Vorgaben von Forschungsförderern, etwa zur Offenlegung von KI-Nutzung in Anträgen und Begutachtung.
- `thema/offene-modelle`: Offene Modelle mit veröffentlichten Gewichten und ihr lokaler Betrieb.
