---
title: Anfrage Northwind Traders, Workshop und KI-Regeln im Vertrieb
type: protokoll
language: de
tags:
  - bereich/projekt
  - feld/projekte
  - thema/datenschutz
related:
  - "[[ACTIVE-WORK]]"
  - "[[governance-entwurf]]"
  - "[[2026-11-05_northwind-angebot-uebung]]"
---
# Anfrage Northwind Traders, Workshop und KI-Regeln im Vertrieb

## Anlass

Am 5. November 2026 kam eine Mail der Vertriebsleitung von Northwind Traders, einem Großhandel für Feinkost und Getränke. Das Rohmaterial liegt lokal in `eingang/2026-11-05_northwind-anfrage.md`. Laut Mail arbeitet das Team fast nur mit Excel-Listen, und mehrere Mitarbeitende kopieren Kundendaten in Chatbots. Gewünscht sind ein eintägiger Workshop, intern weitergebbare Folien, eine kleine Webseite mit Begriffen und Regeln und ein erster Vorschlag für interne KI-Regeln im Vertrieb. Dazu fragt die Vertriebsleitung, welche Produkte und Länder den meisten Umsatz bringen, und nennt vier Excel-Exporte der Jahre 1996 bis 1998 als Anhänge: Bestellungen, Produkte, Kunden und Mitarbeitende.

Die Anhänge liegen seit dem 5. November lokal in `eingang/`. Laut der README im Datenordner des Workshops vom 9. November 2026 (Uni for Life, Sitzung 3), `C:/Users/Chrisi/Documents/GitHub/DHCraft/knowledge-context-agentic-engineering/workshops/2026-11-09-ufl/data`, ist die Anfrage eine synthetische Übung. Aus diesem Ordner lassen sich die Dateien wieder in `eingang/` kopieren. Die vier Dateien sind aus der Beispieldatenbank Northwind von Microsoft umgewandelt, einem fiktiven Großhandel mit Bestellungen von 1996 bis 1998. Spaltennamen und Werte sind unverändert, die Lizenz liegt als `LICENSE-northwind.txt` bei.

| Datei | Blätter, Zeilen | Personenbezug |
| --- | --- | --- |
| `bestellungen.xlsx` | Orders (830), Order Details (2155) | Lieferadressen von Firmen, Kennung der bearbeitenden Person |
| `produkte.xlsx` | Products (77), Categories (8), Suppliers (29) | Ansprechpersonen bei Lieferanten |
| `kunden.xlsx` | Customers (91), Shippers (3) | Ansprechpersonen mit Telefonnummern |
| `mitarbeitende.xlsx` | Employees (9) | Geburtsdaten, Privatadressen, private Telefonnummern, Notizen, alle fiktiv |

Die Daten sind fiktiv. Ein Vertrag zur Auftragsverarbeitung ist für diese Dateien deshalb nicht nötig. Die Übung behandelt sie trotzdem so, als wären sie echt.

## Entscheidungen

- Die Anhänge sind in `eingang/` abgelegt. Zunächst wurden nur Spaltenköpfe und Zeilenzahlen gelesen. Für die Umsatzfrage liest das Skript danach die Werte von Orders, Order Details und Products, nie `kunden.xlsx` und `mitarbeitende.xlsx`.
- Für die Umsatzfrage reichen Orders mit dem Lieferland `ShipCountry`, Order Details mit Preis, Menge und Rabatt und Products mit den Produktnamen. `kunden.xlsx` und `mitarbeitende.xlsx` werden für diese Frage nicht verarbeitet.

## Umsatzauswertung

Das Skript `scripts/northwind_umsatz.py` rechnet lokal, ohne KI-Dienst, und liest nur Orders, Order Details und Products. Umsatz einer Bestellzeile ist Preis mal Menge mal eins minus Rabatt. Das Land ist das Lieferland der Bestellung. Die Daten umfassen 830 Bestellungen mit 2155 Positionen vom 4. Juli 1996 bis 6. Mai 1998, darunter 21 noch nicht versandte Bestellungen, die mitgezählt sind. Die Jahre 1996 und 1998 sind unvollständig, ein Vergleich nach Jahren wäre deshalb schief. Der Gesamtumsatz beträgt 1.265.793,04. Eine zweite, unabhängige Rechnung über die Tabellenspalten kommt auf dieselbe Summe.

| Rang | Produkt | Umsatz | Anteil |
| --- | --- | --- | --- |
| 1 | Côte de Blaye | 141.396,73 | 11,2 % |
| 2 | Thüringer Rostbratwurst | 80.368,67 | 6,3 % |
| 3 | Raclette Courdavault | 71.155,70 | 5,6 % |
| 4 | Tarte au sucre | 47.234,97 | 3,7 % |
| 5 | Camembert Pierrot | 46.825,48 | 3,7 % |

| Rang | Lieferland | Umsatz | Anteil |
| --- | --- | --- | --- |
| 1 | USA | 245.584,61 | 19,4 % |
| 2 | Deutschland | 230.284,63 | 18,2 % |
| 3 | Österreich | 128.003,84 | 10,1 % |
| 4 | Brasilien | 106.925,78 | 8,4 % |
| 5 | Frankreich | 81.358,32 | 6,4 % |

Die vollständigen Ranglisten mit 77 Produkten und 21 Ländern schreibt das Skript mit `--csv` nach `output/`. Der Datensatz nennt keine Währung. Mit `--web` erzeugt es die Daten für die [Auswertung als Webseite](../dashboard/northwind/index.html): Umsatz pro Monat, nach Lieferland, Kategorie und Produkt, mit Filtern, die alle Diagramme verbinden. Die Seite enthält nur Summen.

## Abgleich mit dem Governance-Entwurf

- Eine Analyse der Kundendaten fällt in die Datenklasse „Personenbezogen“ des [[governance-entwurf#4 Datenklassen|Governance-Entwurfs]]. Datenfluss und Rollen sind dann zu dokumentieren, die Rechtsgrundlage ist zu prüfen. Als Ableitung aus derselben Rollenlogik wäre DHCraft Auftragsverarbeiter von Northwind und bräuchte vor der Analyse einen Vertrag zur Auftragsverarbeitung.
- Die Umsatzfrage braucht nur Bestellungen und Produkte. Die Mitarbeitendenliste wird nicht verarbeitet, nach der Regel, dass ein Agent nur die Daten der aktuellen Aufgabe erhält.
- Die Auswertung läuft lokal und nachvollziehbar per Skript, ohne externen KI-Dienst.
- Kundendaten in Chatbots ist das Kernproblem bei Northwind. Ein Dienst, dem Northwind personenbezogene Daten im Auftrag überlässt, ist in der Regel Auftragsverarbeiter und braucht einen Vertrag, siehe [[governance-entwurf#3 Werkzeuge]], wo das als Empfehlung steht. Private Chatbot-Konten haben in der Regel keinen.
- Der Workshop wäre eine Maßnahme zur KI-Kompetenz, die Northwind als Betreiber unterstützen muss. Das Gesetz verlangt dafür kein Zertifikat, siehe [[governance-entwurf#9 Kompetenz und Einführung]].
- Intern weitergegebene Folien mit KI-Anteil brauchen keine Kennzeichnung. Die Weitergabe regelt eine Lizenz. Die Kennzeichnungsregel steht in [[governance-entwurf#7 Transparenz]].
- Für die Webseite ist die öffentliche Arbeitsfläche in `public/` ein fertiges Muster, das eigene Inhalte für Northwind bräuchte.
- Die Leitlinien von DHCraft sind auf Forschung, Förderer und Code zugeschnitten. Übertragbar sind Datenklassen, Werkzeugregister, die Bindung an Auftragsverarbeiter und die Transparenzregeln.

## Offene Fragen

Die Fragen werden im Projektdokument [[northwind-traders]] weitergeführt.

- Wo hat Northwind seinen Sitz? Governance und Quellen setzen EU-Recht voraus.
- Wie groß ist das Team, das am Workshop teilnimmt?
- Welche Chatbots nutzt das Team, mit welchen Konten?
- Darf DHCraft personenbezogene Daten von Northwind erhalten, und unter welchem Vertrag?

## Vorschläge für die Wissensbasis

- Recherche nach Quellen aus 2026 zu KI im Vertrieb und zu Kundendaten in Chatbots und CRM-Systemen. Die Wissensbasis enthält dazu bisher nichts.
- Das Angebot liegt als Übungsentwurf in [[2026-11-05_northwind-angebot-uebung]], ohne Angebotsnummer und ohne Eintrag in die echte Angebotsübersicht, weil Northwind fiktiv ist.

## Antwortentwurf (Übung)

Der Entwurf steht nur hier und nicht in Thunderbird, weil Northwind fiktiv ist. Die Anrede ist hier durch einen Platzhalter ersetzt.

> Betreff: AW: Anfrage Workshop Agentic Engineering und Governance
>
> Sehr geehrter Herr [Name],
>
> vielen Dank für Ihre Anfrage. Workshop, Folien, Webseite und einen ersten Regelvorschlag kann ich Ihnen gern anbieten. Damit das Angebot zu Ihrem Team passt, würde ich vorab gern ein kurzes Gespräch von etwa einer Stunde führen und dabei Folgendes klären:
>
> - An welchem Standort arbeitet Ihr Team? Davon hängt ab, welche Rechtsvorschriften für die Regeln gelten.
> - Wie viele Personen nehmen teil, und wie viel Erfahrung haben sie mit KI-Werkzeugen?
> - Welche Chatbots nutzt das Team, und über private oder über Firmenkonten?
> - Soll der Workshop bei Ihnen vor Ort oder online stattfinden, und welche Termine kommen infrage?
>
> Zu den Anhängen: Für den Workshop genügen Exporte ohne Angaben zu Personen. Die Liste der Mitarbeitenden brauche ich nicht und habe sie nicht ausgewertet. Bitte schicken Sie mir weitere Kunden- oder Personaldaten erst, wenn wir dafür einen Vertrag zur Auftragsverarbeitung geschlossen haben.
>
> Vorab zu Ihrer Frage nach dem Umsatz: In den Bestellungen von Juli 1996 bis Mai 1998 bringt der Wein Côte de Blaye mit rund 11 Prozent den größten Anteil, vor Thüringer Rostbratwurst und Raclette Courdavault. Nach Lieferland liegen die USA und Deutschland mit zusammen rund 37 Prozent vorn, vor Österreich. Ausgewertet habe ich dafür nur Bestellungen und Produkte, ohne Kunden- oder Personaldaten, und ohne die Daten an einen KI-Dienst zu geben. Genau dieses Vorgehen kann Ihr Team im Workshop an den eigenen Listen üben.
>
> Ich freue mich auf Ihre Rückmeldung.
>
> Mit freundlichen Grüßen
> Christopher Pollin
> Digital Humanities Craft
