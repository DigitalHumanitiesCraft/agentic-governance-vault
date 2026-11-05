---
title: Northwind Traders, KI im Vertrieb (Übung)
type: kundenprojekt
language: de
tags:
  - bereich/projekt
  - feld/projekte
  - thema/datenschutz
related:
  - "[[ACTIVE-WORK]]"
  - "[[2026-11-05_northwind-anfrage]]"
  - "[[2026-11-05_northwind-angebot-uebung]]"
  - "[[governance-entwurf]]"
---
# Northwind Traders, KI im Vertrieb (Übung)

Dieses Dokument führt das Projekt Northwind Traders. Es sammelt Stand, Entscheidungen, offene Fragen und nächste Schritte und verweist für die Einzelheiten auf Protokoll, Angebot, Datenbeschreibung und Anforderungen. [[ACTIVE-WORK]] nennt das Projekt mit seinem nächsten Schritt und verweist hierher.

Das Projekt ist eine Übung für Sitzung 3 des Workshops am 9. November 2026. Northwind Traders ist eine fiktive Firma, die Anfrage ist synthetisch, und kein Entwurf wird versendet.

## Auftraggeber

Northwind Traders ist ein fiktiver Großhandel für Feinkost und Getränke aus der Beispieldatenbank Northwind von Microsoft. Die Anfrage stellt die Vertriebsleitung. Weil die Firma fiktiv ist, trägt das Projekt keine Angebotsnummer und steht in keiner echten Angebotsübersicht.

## Anfrage

Die Mail vom 5. November 2026 wünscht einen eintägigen Workshop, intern weitergebbare Folien, eine kleine Webseite mit Begriffen und Regeln und einen ersten Vorschlag für interne KI-Regeln im Vertrieb. Dazu fragt sie, welche Produkte und Länder den meisten Umsatz bringen, und hängt vier Excel-Exporte an. Anlass, Herkunft und Inhalt der Anhänge stehen im [Protokoll der Anfrage](../protokolle/2026-11-05_northwind-anfrage.md), das Rohmaterial liegt lokal in `eingang/`.

## Prüfung gegen die Governance

Die Anfrage ist gegen den [Governance-Entwurf](../knowledge/governance-entwurf.md) geprüft. Das Ergebnis steht im Protokoll im Abschnitt „Abgleich mit dem Governance-Entwurf“. Für die Projektführung zählen vier Punkte daraus.

- Kundendaten fallen in die Datenklasse „Personenbezogen“. Abgeleitet aus der Rollenlogik des Entwurfs wäre DHCraft Auftragsverarbeiter und bräuchte vor der Verarbeitung echter personenbezogener Daten von Northwind einen Vertrag zur Auftragsverarbeitung.
- Die Umsatzfrage braucht nur Bestellungen und Produkte. Kunden- und Mitarbeitendenlisten werden nicht verarbeitet.
- Auswertungen laufen lokal per Skript, ohne externen KI-Dienst.
- Der Workshop ist eine Maßnahme zur KI-Kompetenz. Aus den Leitlinien von DHCraft übertragbar sind Datenklassen, Werkzeugregister, die Bindung an Auftragsverarbeiter und die Transparenzregeln.

## Geltende Regeln

Diese Regeln der [Leitlinien](../knowledge/leitlinien-dhcraft.md) sind aus der Prüfung gegen die Governance abgeleitet, getrennt nach Regeln, die DHCraft in diesem Projekt binden, und Regeln, die sich in den Regelvorschlag für Northwind übertragen lassen. Jeder Eintrag zitiert den Anfang der Regel wörtlich, `scripts/build_dashboard.py` ordnet ihn daran der Regel zu und meldet einen Fehler, wenn der Anfang auf keine oder auf mehrere Regeln passt.

### Gilt für DHCraft in diesem Projekt

- „Before an agent works with client data, document which service receives which data and in which role“ Würde DHCraft Kundendaten von Northwind auswerten, wäre es Auftragsverarbeiter, und Datenfluss und Rollen wären vorher festzuhalten.
- „Check before each new agent use with personal data whether it needs its own legal basis“ Eine Auswertung der Kundendaten fiele in die Datenklasse „Personenbezogen“, für die vorher die Rechtsgrundlage zu prüfen ist.
- „Send personal data only to services bound as processors.“ Erhielte DHCraft echte Kundendaten von Northwind, dürften sie nur an Dienste gehen, die als Auftragsverarbeiter gebunden sind.
- „Give agents access only to the folders and accounts of the current task“ Der Agent, der das Umsatzskript gebaut hat, hatte den ganzen Ordner `eingang/` in Reichweite, also auch `kunden.xlsx` und `mitarbeitende.xlsx`. Bei echten Kundendaten wäre sein Zugriff auf die Bestell- und Produktdateien zu beschränken.
- „Tell clients which AI tools and agents handle their material“ Der Antwortentwurf sagt der Vertriebsleitung, dass nur Bestellungen und Produkte ausgewertet wurden, ohne die Daten an einen KI-Dienst zu geben. Dass ein KI-Agent das Auswertungsskript geschrieben hat, nennt er noch nicht.
- „Internal texts and professional correspondence written with AI need no AI label.“ Die intern weitergegebenen Folien des Workshops brauchen deshalb keine Kennzeichnung, ihre Weitergabe regelt eine Lizenz.

### Übertragbar in den Regelvorschlag für Northwind

- „Take measures that support the AI literacy of everyone who works with agents“ Der Workshop ist eine Maßnahme zur KI-Kompetenz, wie Northwind sie als Betreiber für sein Team unterstützen muss.
- „Keep a register of approved AI tools and agents“ Das Werkzeugregister nennt die Prüfung als übertragbar, für Northwind etwa als Liste der zugelassenen Chatbots und Konten.

## Leistungen und Stand

| Leistung | Stand | Unterlage |
| --- | --- | --- |
| Umsatzauswertung als Skript und Webseite | Gebaut, die Seite enthält nur Summen. `scripts/northwind_check.py` rechnet jede Kennzahl unabhängig nach und vergleicht sie mit Seite und Protokoll. Die Seite ist Teil der öffentlichen Workshop-Ergebnisse. | [Umsatzseite](../dashboard/northwind/index.html), [Anforderungen](../knowledge/northwind/requirements.md) |
| Beschreibung der Übungsdaten | Liegt vor, mit Personenbezug je Blatt und den Fragen, die die Daten ohne Personenbezug beantworten. | [Datenbeschreibung](../knowledge/northwind/data.md) |
| Antwortentwurf an die Vertriebsleitung | Entwurf mit Rückfragen und einer ersten Antwort zum Umsatz. Er steht nur im Protokoll und wird weder in Thunderbird abgelegt noch versendet. | [Protokoll, Antwortentwurf](../protokolle/2026-11-05_northwind-anfrage.md) |
| Angebotsentwurf | Übungsentwurf mit fünf Leistungen. Der Aufwand ist ein Vorschlag, Tagessatz, Reisekosten und Umsatzsteuer sind Platzhalter. | [Angebotsentwurf](../protokolle/2026-11-05_northwind-angebot-uebung.md) |
| Workshop, Folien, Webseite, Regelvorschlag | Im Angebotsentwurf beschrieben, nicht beauftragt und nicht begonnen. Für die Webseite ist die öffentliche Arbeitsfläche in `public/` das Muster. | [Angebotsentwurf](../protokolle/2026-11-05_northwind-angebot-uebung.md) |

## Entscheidungen

- Die Daten sind fiktiv, die Übung behandelt sie trotzdem wie echte. Ein Vertrag zur Auftragsverarbeitung ist für diese Dateien deshalb nicht nötig.
- Für die Umsatzfrage liest das Skript nur Bestellungen, Bestellpositionen, Produkte und Kategorien, nie `kunden.xlsx` und `mitarbeitende.xlsx`. Begründung und Prüfung stehen in den [Anforderungen](../knowledge/northwind/requirements.md) unter R1.
- Angebot und Antwort bleiben Übungsentwürfe ohne Angebotsnummer, ohne Eintrag in die Angebotsübersicht und ohne Entwurf in Thunderbird.

## Offene Fragen an den Auftraggeber

Die Fragen stammen aus dem Protokoll und dem Antwortentwurf darin. Antworten werden hier eingetragen.

- Wo hat Northwind seinen Sitz? Governance und Quellen setzen EU-Recht voraus.
- Wie groß ist das Team, das am Workshop teilnimmt, und wie viel Erfahrung hat es mit KI-Werkzeugen?
- Welche Chatbots nutzt das Team, mit privaten oder mit Firmenkonten?
- Darf DHCraft personenbezogene Daten von Northwind erhalten, und unter welchem Vertrag?
- Soll der Workshop vor Ort oder online stattfinden, und welche Termine kommen infrage?

## Offen beim Inhaber

- Tagessatz, Aufwand, Reisekosten, Termin und Ort des Angebots legt der Inhaber fest.

## Nächste Schritte

- Der Inhaber legt Tagessatz und Aufwand fest, danach wird der Angebotsentwurf vervollständigt.
- Antworten auf die Rückfragen gehen in dieses Dokument und in den Angebotsentwurf ein.
- Das Protokoll schlägt eine Recherche nach Quellen aus 2026 zu KI im Vertrieb und zu Kundendaten in Chatbots und CRM-Systemen vor. Die Wissensbasis enthält dazu bisher nichts, und der Regelvorschlag für Northwind bräuchte solche Quellen.

## Verlauf

- 2026-11-05: Anfrage eingegangen und gegen die Governance geprüft, Umsatzauswertung gebaut und geprüft, Antwort- und Angebotsentwurf erstellt, siehe [Protokoll](../protokolle/2026-11-05_northwind-anfrage.md).
