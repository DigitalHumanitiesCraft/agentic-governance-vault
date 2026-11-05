---
title: "{{title}}"
type: kundenprojekt
language: de
status:
tags:
  - bereich/projekt
  - feld/projekte
related:
  - "[[ACTIVE-WORK]]"
---
# {{title}}

%% Tags nur aus [[TAG-TAXONOMY]]; ein neues Tag wird zuerst dort eingetragen. Das Dokument verweist auf Protokolle, Angebote und Wissensdokumente, statt sie zu kopieren. Termine und Prioritäten nur, wenn der Inhaber sie gesetzt hat. `status` ist einer von anfrage, angebot, beauftragt, abgeschlossen und wird nur vom Inhaber gesetzt. %%

## Auftraggeber

%% Rolle und Organisation, keine Personennamen. %%

## Anfrage

%% Was gewünscht ist, in wenigen Sätzen, mit Markdown-Link auf das Protokoll der Anfrage. %%

## Prüfung gegen die Governance

%% Ergebnis der Prüfung gegen den Governance-Entwurf als knappe Zusammenfassung, Quelle ist das Protokoll. Ableitungen als Ableitungen kennzeichnen. %%

## Geltende Regeln

%% Zwei Gruppen: Regeln, die DHCraft im Projekt binden, und Regeln, die sich in einen Regelvorschlag für den Auftraggeber übertragen lassen. Leere Gruppen dürfen fehlen, Listenpunkte außerhalb der Gruppen meldet der Build als Fehler. Je Regel aus knowledge/leitlinien-dhcraft.md ein Listenpunkt. Er beginnt mit dem Anfang der Regel wörtlich in „…“, so lang, dass er nur auf diese eine Regel passt, und nennt danach in einem Satz, warum sie greift. `scripts/build_dashboard.py` ordnet jeden Punkt seiner Regel zu und schreibt die öffentlichen Daten nicht, wenn ein Anfang auf keine oder auf mehrere Regeln passt. %%

### Gilt für DHCraft in diesem Projekt

### Übertragbar in den Regelvorschlag für den Auftraggeber

## Leistungen und Stand

%% Stand je Leistung, Unterlage als Markdown-Link. %%

| Leistung | Stand | Unterlage |
| --- | --- | --- |

## Entscheidungen

%% Festlegungen für das Projekt, mit Begründung oder Verweis darauf. %%

## Offene Fragen an den Auftraggeber

%% Die einzige laufende Liste der Rückfragen; Antworten werden hier eingetragen. %%

## Offen beim Inhaber

%% Was nur der Inhaber entscheidet, etwa Preis, Aufwand, Termin und Ort. %%

## Nächste Schritte

## Verlauf

%% Datum und Ereignis, mit Link auf das Protokoll. %%
