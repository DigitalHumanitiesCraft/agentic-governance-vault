---
title: Governance für AI Agents bei Digital Humanities Craft
type: entwurf
language: de
tags:
  - bereich/projekt
  - feld/projekte
  - feld/forschung
  - feld/programmierung
  - feld/organisation
related:
  - "[[leitlinien-dhcraft]]"
  - "[[quellen]]"
  - "[[project]]"
---
# Governance für AI Agents bei Digital Humanities Craft

Beschlussvorlage, Version 1.0 vom 5. November 2026. Die Governance gilt, sobald beide Eigentümer sie beschlossen haben.

Diese Governance regelt, wie Digital Humanities Craft (DHCraft) AI Agents in Kundenprojekten, in der Forschung und beim Programmieren einsetzt. Ein AI Agent ist hier ein System auf Basis eines Large Language Model (LLM), das mehrschrittige Aufgaben mit Werkzeugen wie Shell, Browser, Dateien oder Mail selbstständig plant und ausführt. Die Governance gilt für alle, die für DHCraft mit Agents arbeiten, also für die beiden Eigentümer und für freie Mitarbeitende.

DHCraft ist ein Unternehmen mit zwei Personen in Graz. Es entwickelt Forschungssoftware und digitale Editionen, berät und schult zu generativer KI und arbeitet als technischer Partner in Drittmittelprojekten. Agents arbeiten dabei vor allem mit geisteswissenschaftlichen Forschungsdaten, oft mit gemeinfreien oder frei nutzbaren Objekten. Personenbezogene Daten kommen nur selten vor. Die Regeln für sie und für besonders geschützte Daten gelten für diese Fälle.

Jede Regel nennt ihren Status und ihre Quellen in der Wissensbasis mit Seite. Die Status sind unten erklärt. Die rechtlichen Einschätzungen in dieser Governance sind keine Rechtsberatung.

## 1 Grundsätze

- Die Verantwortung für alles, was ein Agent tut oder erzeugt, bleibt bei der Person, die ihn einsetzt. Der Einsatz eines Agents gilt nie als Übertragung von Kontrolle oder Verantwortung (Empfehlung) ([ERA Guidelines 2026, PDF S. 7](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf); [ERA Guidelines 2026, PDF S. 8](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Ein Agent erhält so viel Selbstständigkeit, wie das Risiko der Aufgabe zulässt. Je mehr er selbst entscheidet, desto größer ist der mögliche Schaden eines Fehlers (Empfehlung) ([NCSC-UK 2026, Abschnitt Assess how much autonomy is needed](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- Ein Agent erhält nur die Zugänge, die seine aktuelle Aufgabe braucht, und nie einen breiten oder unbeschränkten Zugriff (Empfehlung) ([Five Eyes 2026, PDF S. 4](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [Five Eyes 2026, PDF S. 7](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).
- Die DSGVO gilt neben dem AI Act und wird von ihm nicht verdrängt. Der AI Act ist keine Rechtsgrundlage für eine Datenverarbeitung (Pflicht) ([DSB 1/2026, PDF S. 3](../sources/DSB-AT_2026_newsletter-1-2026-ki-und-datenschutz.pdf); [DSB 1/2026, PDF S. 4](../sources/DSB-AT_2026_newsletter-1-2026-ki-und-datenschutz.pdf)).

## 2 Rollen und Verantwortung

- Die Eigentümer benennen eine Person, die für den Einsatz von Agents bei DHCraft verantwortlich ist. Sie führt das Werkzeugregister, gibt neue Werkzeuge frei und ist Ansprechperson bei Vorfällen (Empfehlung) ([NCSC-UK 2026, Abschnitt Set the right level of oversight](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- Zur Governance gehört eine Person, die den Datenschutz und die konkreten Verarbeitungen kennt. Bei DHCraft kann das eine der beiden Personen sein oder eine externe Beratung (Empfehlung) ([AEPD 2026, PDF S. 52](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)). Ob daraus eine formelle Bestellung als Datenschutzbeauftragte Person werden muss, regelt der folgende Abschnitt.
- DHCraft ist im Sinne des AI Act Betreiber jedes Agents, den es beruflich nutzt. Freie Mitarbeitende, die in seinem Auftrag arbeiten, ändern daran nichts (Pflicht) ([Art. 50 Guidelines 2026, PDF S. 7](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf); [Art. 50 Guidelines 2026, PDF S. 9](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf)).
- Baut DHCraft einen Agent, der unter eigenem Namen in Betrieb geht, ist DHCraft sein Anbieter. Lässt ein Kunde den Agent entwickeln und betreibt ihn unter seinem Namen, ist der Kunde Anbieter. Der Vertrag hält diese Rolle fest (Pflicht) ([Art. 50 Guidelines 2026, PDF S. 6](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf)).

### Datenschutzbeauftragte Person

- Eine Datenschutzbeauftragte Person ist Pflicht für Behörden und für Verantwortliche und Auftragsverarbeiter, deren Kerntätigkeit in der umfangreichen, regelmäßigen und systematischen Überwachung von Personen besteht oder in der umfangreichen Verarbeitung besonders geschützter Daten nach Art. 9 DSGVO (Pflicht) ([DSGVO, Art. 37 Abs. 1](../sources/EU-Parlament-Rat_2016-04-27_dsgvo-art-37-39.md)). Die Pflicht gilt auch für Auftragsverarbeiter wie DHCraft, und sie folgt nicht automatisch daraus, dass ein Kunde selbst eine solche Person bestellen muss ([WP 243, PDF S. 9](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf)).
- Kerntätigkeiten sind die Haupttätigkeiten eines Unternehmens. Datenverarbeitung als Nebentätigkeit zählt nicht ([DSGVO, Erwägungsgrund 97](../sources/EU-Parlament-Rat_2016-04-27_dsgvo-art-37-39.md)). Die Leitlinien der Datenschutzbehörden nennen Lohnabrechnung und gewöhnlichen IT-Support als Beispiele für Nebentätigkeiten ([WP 243, PDF S. 7](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf)).
- Für „umfangreich“ gibt es keine Schwelle. Maßgeblich sind die Zahl der Betroffenen, die Menge und Art der Daten, die Dauer und die räumliche Reichweite. Die Patientendaten einer einzelnen Ärztin gelten als nicht umfangreich, und dazwischen liegt eine Grauzone ([WP 243, PDF S. 7–8](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf)).
- Das österreichische Datenschutzgesetz begründet für private Unternehmen keine zusätzliche Pflicht. Es regelt die Verschwiegenheit einer bestellten Person, und die Bestellpflicht in § 57 gilt nur für Sicherheits- und Strafverfolgungsbehörden ([DSG, § 5 und § 36 Abs. 1](../sources/RIS-AT_2026-11-05_dsg-datenschutzbeauftragter.md)).
- Für DHCraft folgt daraus vermutlich keine Pflicht. Überwachung von Personen gehört nicht zu seinen Tätigkeiten, und personenbezogene Daten kommen in der Arbeit mit überwiegend gemeinfreien Forschungsdaten nur selten vor, sodass ihre Verarbeitung weder Kerntätigkeit noch umfangreich sein dürfte (Ableitung) ([DSGVO, Art. 37 Abs. 1](../sources/EU-Parlament-Rat_2016-04-27_dsgvo-art-37-39.md); [WP 243, PDF S. 7–8](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf)). Kommen Projekte mit vielen personenbezogenen Daten hinzu, ist die Frage neu zu stellen.
- DHCraft hält diese Prüfung schriftlich fest und aktualisiert sie, wenn ein neuer Projekttyp mit personenbezogenen Daten hinzukommt (Empfehlung) ([WP 243, PDF S. 5](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf)). Die Prüfung wird außerdem wiederholt, wenn der EDPB seine Leitlinien zu Datenschutzbeauftragten überarbeitet hat ([EDPB 2026, PDF S. 3](../sources/EDPB_2026-02-11_work-programme-2026-2027.pdf)).
- Bestellt DHCraft freiwillig eine Datenschutzbeauftragte Person, gelten alle Pflichten der Art. 37 bis 39 DSGVO wie bei einer Pflichtbestellung ([WP 243, PDF S. 5](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf)). Wer über Zwecke und Mittel der Verarbeitung entscheidet, etwa die Geschäftsführung, kann diese Rolle wegen Interessenkonflikts nicht übernehmen ([WP 243, PDF S. 16](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf); [DSGVO, Art. 38 Abs. 6](../sources/EU-Parlament-Rat_2016-04-27_dsgvo-art-37-39.md)). Bei zwei Eigentümern käme daher nur eine externe Person auf Dienstvertrag in Frage ([DSGVO, Art. 37 Abs. 6](../sources/EU-Parlament-Rat_2016-04-27_dsgvo-art-37-39.md)).
- Ohne Bestellung trägt die Ansprechperson für Datenschutz nicht den Titel Datenschutzbeauftragte, damit intern und gegenüber der Behörde keine Verwechslung entsteht (Empfehlung) ([WP 243, PDF S. 6](../sources/Art29WP_2017-04-05_wp243-guidelines-dpo.pdf)).

## 3 Werkzeuge

- DHCraft führt ein Register aller zugelassenen KI-Werkzeuge und Agents mit Einsatzzweck, Hosting-Ort und den Bedingungen zur Weiterverwendung von Daten (Ableitung) ([ERA Guidelines 2026, PDF S. 11](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf); [Five Eyes 2026, PDF S. 18](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).
- Agents laden nur Werkzeuge und Erweiterungen aus diesem Register, in festgelegten Versionen (Empfehlung) ([Five Eyes 2026, PDF S. 18](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).
- Wo es möglich und nötig ist, nutzt DHCraft selbst betriebene oder lokal gehostete Werkzeuge oder solche vertrauenswürdiger Dritter, die den europäischen Datenschutz einhalten (Empfehlung) ([ERA Guidelines 2026, PDF S. 11](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Ein externer Dienst, an den personenbezogene Daten gehen, ist Auftragsverarbeiter und braucht einen entsprechenden Vertrag. Ein vollständig lokaler Agent braucht diese Prüfung nicht (Empfehlung) ([AEPD 2026, PDF S. 31–32](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).
- Verträge und Nutzungsbedingungen von Online-Diensten werden bei der Aufnahme ins Register und danach regelmäßig geprüft, unter Beteiligung der Datenschutz-Person (Empfehlung) ([AEPD 2026, PDF S. 70](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).

## 4 Datenklassen

DHCraft teilt die Daten, mit denen Agents arbeiten, in vier Klassen ein. Die Einteilung ist eine Ableitung aus den Anforderungen an Vertraulichkeit, Personenbezug und besonders geschützte Daten in den Quellen ([ERA Guidelines 2026, PDF S. 7–8](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf); [AEPD 2026, PDF S. 35](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).

| Klasse | Beispiele | Regel für Agents | Grundlage |
| --- | --- | --- | --- |
| Offen | eigener Code, veröffentlichte Texte und Daten, gemeinfreie und frei nutzbare Forschungsdaten | Agents arbeiten in einer abgeschotteten Umgebung mit eingeschränktem Netz (Empfehlung). | [NCSC-UK 2026, Abschnitt Control the AI agent's environment with a robust sandbox](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md) |
| Vertraulich | unveröffentlichte Forschung, Anträge, Gutachten, Kundenmaterial ohne Personenbezug | Nur Dienste, die Eingaben nicht zum Training weiterverwenden, oder lokale Systeme (Empfehlung). | [ERA Guidelines 2026, PDF S. 7–8](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf); [DFG 2026, PDF S. 2–3](../sources/DFG_2026-03_leitlinie-ki-in-der-begutachtung.pdf) |
| Personenbezogen | Kundendaten, Korrespondenzen, Kontaktdaten | Datenfluss und Rollen sind dokumentiert, die Rechtsgrundlage ist geprüft, und Daten gehen nur an Auftragsverarbeiter (Empfehlung). | [AEPD 2026, PDF S. 33](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf); [AEPD 2026, PDF S. 35](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf) |
| Besonders geschützt | Angaben zu Religion, Herkunft, Gesundheit, etwa in Zeitzeugnissen | Zusätzlich eine Ausnahme nach Art. 9 DSGVO, Prüfung einer Datenschutz-Folgenabschätzung, lokale oder vertraglich gesicherte Verarbeitung und menschliche Freigabe jeder Handlung (Ableitung). | [AEPD 2026, PDF S. 35](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf); [DSB 1/2026, PDF S. 4](../sources/DSB-AT_2026_newsletter-1-2026-ki-und-datenschutz.pdf); [AEPD 2026, PDF S. 39–40](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf) |

- Vor jedem neuen Einsatz mit personenbezogenen Daten wird geprüft, ob er eine eigene Rechtsgrundlage braucht und ob eine Datenschutz-Folgenabschätzung nötig ist. Agents machen eine solche Abschätzung nicht automatisch erforderlich, es kommt auf die Verarbeitung an (Pflicht) ([AEPD 2026, PDF S. 35](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf); [AEPD 2026, PDF S. 41](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf); [DSB 1/2026, PDF S. 4](../sources/DSB-AT_2026_newsletter-1-2026-ki-und-datenschutz.pdf)).
- Ersetzen Agents bisherige Mittel einer Verarbeitung, wird das Verarbeitungsverzeichnis angepasst (Empfehlung) ([AEPD 2026, PDF S. 36](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).

## 5 Arbeitsregeln

### Kundenprojekte

- Ein Agent erhält nur die Ordner und Konten der aktuellen Aufgabe, nie ein ganzes Postfach, Laufwerk oder eine Kundendatenbank (Empfehlung) ([Five Eyes 2026, PDF S. 7](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [AEPD 2026, PDF S. 19](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).
- Kunden erfahren, welche KI-Werkzeuge und Agents ihr Material bearbeiten und wie es geschützt ist (Ableitung) ([ERA Guidelines 2026, PDF S. 10](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Ein Agent, den DHCraft baut und der mit Menschen kommuniziert, gibt sich als KI zu erkennen und sagt, in wessen Auftrag er handelt (Pflicht für den Anbieter) ([Art. 50 Guidelines 2026, PDF S. 13](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf)).

### Forschung und Anträge

- Prüfpunkte im Ablauf sorgen dafür, dass ein Mensch methodische Entscheidungen eines Agents bestätigt (Empfehlung) ([ERA Guidelines 2026, PDF S. 7](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Jede Literaturangabe und jede Sachaussage, die ein Agent liefert, wird vor der Verwendung am Original geprüft. Erfundene Angaben in FWF-Anträgen werden sanktioniert, bis hin zur Rückforderung von Fördermitteln (Vorgabe) ([FWF 2026, Abschnitt Penalties for improper use of AI](../sources/FWF_2026-07-07_ki-in-foerderantraegen.md); [ERA Guidelines 2026, PDF S. 9](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Für Forschungsschritte, die ein Agent ausführt, werden Prompts, Protokolle, Modellversionen und Parameter aufbewahrt (Empfehlung) ([ERA Guidelines 2026, PDF S. 7](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf); [AEPD 2026, PDF S. 66](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).
- Personenbezogene Daten Dritter gehen nur mit Einwilligung oder anderer Rechtsgrundlage und klarem Zweck an externe KI-Dienste (Empfehlung) ([ERA Guidelines 2026, PDF S. 8](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Bei Begutachtungen bleibt das Urteil beim Menschen, und vertrauliches Material geht nur an gesicherte oder lokale Systeme. Für DFG-Gutachten ist das verbindlich (Vorgabe) ([DFG 2026, PDF S. 2–3](../sources/DFG_2026-03_leitlinie-ki-in-der-begutachtung.pdf); [ERA Guidelines 2026, PDF S. 9](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).
- Code und Methoden werden so genau veröffentlicht, dass andere, auch Agents, die Ergebnisse nachvollziehen können. Unvollständige Methodenbeschreibungen sind der Hauptgrund, warum das misslingt (Ableitung) ([Agentic reproduction 2026, PDF S. 1](../sources/arXiv_2026-09-29_agentic-reproduction-social-science.pdf)).

### Programmieren

- Coding Agents laufen in einer abgeschotteten Umgebung mit freigegebenen Netzzielen und eigenen, kurzlebigen Zugangsdaten (Empfehlung) ([NCSC-UK 2026, Abschnitt Control the AI agent's environment with a robust sandbox](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- Webseiten, Mails und Dokumente Dritter können versteckte Anweisungen an den Agent enthalten und werden entsprechend behandelt (Empfehlung) ([AEPD 2026, PDF S. 49](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf); [Five Eyes 2026, PDF S. 6](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).
- Änderungen eines Agents bleiben klein und mit den Prüfenden abgestimmt, weil große und unabgestimmte Pull Requests von Agents häufiger scheitern (Ableitung) ([Failed agentic PRs 2026, PDF S. 1](../sources/arXiv_2026-01-21_failed-agentic-pull-requests.pdf); [Failed agentic PRs 2026, PDF S. 2](../sources/arXiv_2026-01-21_failed-agentic-pull-requests.pdf)).
- Wer eine neue Bibliothek oder Methode lernt, nutzt den Agent für Erklärungen und schreibt den Code selbst. Wer ganz delegiert, lernt deutlich weniger und kann Agent-Code später schlechter prüfen (Ableitung) ([Skill formation study 2026, PDF S. 1](../sources/arXiv_2026-02-01_ai-impact-skill-formation.pdf)).

## 6 Freigaben und Protokolle

- Löschen, Deployen, Pushen und das Versenden von Nachrichten brauchen eine menschliche Freigabe. Das Werkzeug erzwingt sie über seine Berechtigungen, eine Anweisung im Prompt reicht nicht. Wann eine Freigabe nötig ist, legen Menschen fest und nicht der Agent (Empfehlung) ([Five Eyes 2026, PDF S. 22](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [NCSC-UK 2026, Abschnitt Prompt carefully](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- Kein Agent verbindet ungeprüfte Eingaben, Zugriff auf sensible Daten und selbstständiges Handeln. Wo alle drei zusammenkommen, gibt ein Mensch jede Handlung frei (Empfehlung) ([AEPD 2026, PDF S. 39–40](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).
- Die Verläufe der Agents werden aufbewahrt und gegen Änderung geschützt, auch gegen Änderung durch den Agent selbst. Da sie sensible Daten enthalten können, gelten für sie dieselben Schutzregeln wie für die Daten (Empfehlung) ([NCSC-UK 2026, Abschnitt Observability](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md); [Five Eyes 2026, PDF S. 20](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).

## 7 Transparenz

- Interne Texte und berufliche Korrespondenz, die mit KI entstehen, brauchen keine Kennzeichnung. Ein veröffentlichter Text, der die Öffentlichkeit über Fragen von öffentlichem Interesse informiert, braucht entweder eine redaktionelle Prüfung mit verantwortlicher Person oder eine Kennzeichnung (Pflicht) ([Art. 50 Guidelines 2026, PDF S. 43](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf)).
- Kommentare, Issues und Nachrichten, die ein Agent an Menschen schreibt, nennen den Agent als Verfasser und DHCraft als Auftraggeber (Ableitung) ([Art. 50 Guidelines 2026, PDF S. 13](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf); [Art. 50 Guidelines 2026, PDF S. 15](../sources/EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf)).
- In FWF-Anträgen wird ein wesentlicher KI-Anteil offengelegt (Vorgabe) ([FWF 2026, lead text](../sources/FWF_2026-07-07_ki-in-foerderantraegen.md)). Eine KI-gestützte Literaturrecherche legt DHCraft ebenfalls offen. Der FWF verlangt das nicht, die EU-Leitlinien zählen sie aber als wesentliche Nutzung ([ERA Guidelines 2026, PDF S. 7](../sources/EU-Kommission-GD-RTD_2026-10-15_era-living-guidelines-genai.pdf)).

## 8 Vorfälle

- Jede Agent-Tätigkeit lässt sich sofort stoppen, einschließlich der Netzverbindung und der Verbindung zum LLM-Dienst (Empfehlung) ([NCSC-UK 2026, Abschnitt Emergency shutdown](../sources/NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)).
- In unklaren Lagen hält ein Agent an und fragt nach, statt weiterzuarbeiten (Empfehlung) ([Five Eyes 2026, PDF S. 20](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).
- DHCraft legt fest, wie es auf einen kompromittierten oder fehlerhaften Agent reagiert, und probt das Vorgehen (Empfehlung) ([Five Eyes 2026, PDF S. 19](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)).

## 9 Kompetenz und Einführung

- DHCraft ergreift Maßnahmen, die die KI-Kompetenz aller unterstützen, die für DHCraft mit Agents arbeiten, freie Mitarbeitende eingeschlossen. Ein Zertifikat oder ein garantiertes Niveau verlangt das Gesetz nicht (Pflicht) ([Reg. 2026/1744, PDF S. 16](../sources/EU-Parlament-Rat_2026-07-08_verordnung-2026-1744-digital-omnibus-ki.pdf)).
- Agents kommen stufenweise zum Einsatz, zuerst für Aufgaben ohne sensible Daten. Zugänge wachsen erst nach Erfahrung (Empfehlung) ([Five Eyes 2026, PDF S. 19](../sources/FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf); [AEPD 2026, PDF S. 55](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).
- Die Eigentümer prüfen diese Governance laufend anhand der Erfahrungen und Vorfälle und passen sie an (Empfehlung) ([AEPD 2026, PDF S. 53](../sources/AEPD_2026-02_agentic-artificial-intelligence.pdf)).

## Festlegungen

- Diese Governance nennt keine einzelnen Dienste. Welche Werkzeuge zugelassen sind, mit Einsatzzweck, Hosting-Ort und Stand der Verträge, hält das Werkzeugregister nach Abschnitt 3 fest.
- DHCraft arbeitet vor allem mit gemeinfreien und frei nutzbaren Forschungsdaten. Die Regeln für personenbezogene und besonders geschützte Daten gelten für die seltenen Fälle, in denen solche Daten vorkommen.

### Beschluss

Die Eigentümer von Digital Humanities Craft beschließen diese Governance in der Version 1.0.

Datum des Beschlusses: ______________________

Unterschrift: ______________________ ______________________

## Annahmen und offene Punkte

Die Angaben zu Größe, Tätigkeit und Datenlage von DHCraft stammen von den Eigentümern, nicht aus der Wissensbasis.

Die Einschätzung zur Datenschutzbeauftragten Person stützt sich auf Gesetzestexte und Leitlinien von 2016 und 2017, die als Ausnahme vom Zeitfenster 2026 in die Wissensbasis aufgenommen wurden. Sie ist keine Rechtsberatung, und wo die Grauzone bei „umfangreich“ berührt ist, sollte eine Fachperson die schriftliche Prüfung gegenlesen.

Österreich hat die Behörden für den AI Act noch nicht benannt. Sobald das geschieht, ist die Governance auf deren Vorgaben zu prüfen.
