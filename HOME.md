---
title: Wissensbasis Agentic Engineering und Governance
type: home
language: de
tags:
  - bereich/projekt
  - bereich/persoenlich
related:
  - "[[ACTIVE-WORK]]"
  - "[[INDEX]]"
  - "[[northwind-traders]]"
---
# Wissensbasis Agentic Engineering und Governance

Dieser Vault verbindet die Wissensbasis zur Governance von AI Agents bei Digital Humanities Craft mit persönlichen Notizen zum Thema.

## Leitfrage

Welche Regeln braucht DHCraft, damit AI Agents in Projekten, Forschung und Programmierung regelkonform, sicher und nachprüfbar arbeiten? Profil, Zeitfenster und offene Punkte stehen in [[project]].

## Arbeitsdokumente

- [[governance-entwurf]] ist die Governance als Beschlussvorlage 1.0 für die Eigentümer, als PDF in `output/`.
- [[leitlinien-dhcraft]] enthält die Regeln nach Feld, jede mit Ziel, Status und Quelle.

## Grundlagen

- [[quellen]] führt alle Quellen mit Herausgeber, Datum, Kategorie und Zusammenfassung.
- Die Originale liegen in `sources/`, die Zusammenfassungen in `sources/summaries/`.

## Laufende Arbeit

- [[ACTIVE-WORK]] hält fest, was läuft, die nächsten Schritte und die offenen Fragen.

## Projekte

- Jedes Kundenprojekt hat ein Projektdokument in `projekte/`, angelegt mit der Vorlage [[kundenprojekt]]. [[ACTIVE-WORK]] führt die Projekte mit Stand und nächstem Schritt und verweist auf ihr Dokument.
- [[northwind-traders]] ist die Übung zur Anfrage von Northwind Traders, mit Umsatzauswertung, Antwort- und Angebotsentwurf.

## Persönliche Notizen

- Eigene Gedanken, Lektüre und Ideen liegen in `notizen/`, angelegt mit der Vorlage [[notiz]] und getaggt mit `bereich/persoenlich`.

## Eingang und Protokolle

- Rohmaterial wie Transkripte, Mails und Feedback kommt nach `eingang/`. Es bleibt lokal und wird nicht committet.
- Ein Agent macht daraus ein Protokoll in `protokolle/` nach der Vorlage [[protokoll]], dort liegen auch Angebotsentwürfe, trägt Entscheidungen und offene Fragen in [[ACTIVE-WORK]] ein und schlägt Änderungen an der Wissensbasis vor.

## Übersicht

![[uebersicht.base]]

## Pflege und Werkzeuge

- [[INDEX]] beschreibt Methode, Glossar, Werkzeuge und die Weiterarbeit.
- [[journal]] hält fest, wie die Wissensbasis entstanden ist.
- Das Dashboard `dashboard/index.html` zeigt Regeln, Quellen, Wissensdokumente, Notizen und Protokolle als Karten, mit Suche und dem Volltext jeder Quelle. Seine Daten erzeugt `scripts/build_dashboard.py`.
- Die öffentliche Arbeitsfläche `public/index.html` ist dasselbe Dashboard mit Leitlinien und Quellen ohne Volltexte; der Build kopiert ihre Oberfläche aus `dashboard/`. Veröffentlicht wird sie als Kopie im Repository `agentic-governance-workspace`.
- Die Umsatzauswertung der Northwind-Übung liegt in `dashboard/northwind/index.html`, erzeugt von `scripts/northwind_umsatz.py --web`.
- Regeln, Ablage und Prüfungen für Agents stehen in `CLAUDE.md`, die erlaubten Tags mit ihrer Bedeutung in [[TAG-TAXONOMY]].
- Die Pitch-Gliederung [[pitch-gliederung]] ist abgenommen. Den Ablauf vom Wissen zu den Folien beschreibt der Skill `.claude/skills/pitch/`.
- Daten und Anforderungen der Northwind-Übung beschreiben `knowledge/northwind/data.md` und `knowledge/northwind/requirements.md`.
