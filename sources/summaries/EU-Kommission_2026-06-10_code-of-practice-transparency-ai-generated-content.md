# Code of Practice on Transparency of AI-Generated Content

Publisher: European Commission (AI Office); drafted by two working groups of independent chairs and vice-chairs, published by the Commission as the final Code
Date: 10 June 2026 (publication date stated on the Commission news item "Commission publishes Code of Practice on marking and labelling AI-generated content", https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content; the PDF itself carries no date)
Original: [EU-Kommission_2026-06-10_code-of-practice-transparency-ai-generated-content.pdf](../EU-Kommission_2026-06-10_code-of-practice-transparency-ai-generated-content.pdf)
Bindingness: Empfehlung (voluntary code). Measures marked "will" are, in the Code's own terms, those "that need to be met to be compliant with Article 50(4) or (5) AI Act" (PDF p. 28); adherence "does not constitute conclusive evidence of compliance" (PDF p. 26).

## Core statement
The Code turns the transparency duties of Article 50(2), (4) and (5) AI Act into concrete measures. Section 1 (PDF pp. 5 to 25) addresses providers of generative AI systems and requires machine-readable marking of outputs, in general with two layers (digitally signed metadata and an imperceptible watermark), and a detection solution. For free-form text a single watermark layer suffices, and very short text is exempt from watermarking (PDF pp. 8 to 9). Section 2 (PDF pp. 26 to 38) addresses deployers who publish deep fakes or AI-generated text on matters of public interest. It sets an "AI" icon or equivalent label, its design and placement, internal processes, staff awareness and, for the editorial exception, a minimum content for an internal review policy. The Commission guidelines on Article 50 already in the base call adherence to an adequate code the most straightforward way to demonstrate compliance; this Code is the text those guidelines point to.

## Relevance to the Leitfrage

### Client projects
- Section 2 applies only to text "published with the purpose of informing the public on matters of public interest, without human review or editorial control and where no natural or legal person holds editorial responsibility" (PDF p. 28). Texts with human review and a responsible person fall outside the labelling duty.
- A deployer that relies on the review exception and is no media service provider commits to an internal policy for human review or editorial control before publication. The policy contains at least "The identification of the natural or legal person with editorial responsibility (name, role and contact details);" and an overview of the organisational measures and human resources for review (PDF p. 36). It does not require "to document individual instances of human review or editorial control over individual text publications" (PDF p. 36). Contact details of the responsible function or person are to be published where not already public (PDF p. 36).
- Where a text is labelled, the label is the capitalised acronym "AI" as main visual element, in English unless national language law requires otherwise (PDF p. 29). For published text the label stands "above or at the top of the text, near the headline of the text, or in the colophon at the beginning of the text"; only the AI-generated part may be labelled (PDF p. 32). An EU icon in variants "AI + GENERATED" and "AI + MODIFIED" is free to use without attribution (PDF p. 37).
- Labels must be accessible: screen-reader compatibility and detectability by assistive technologies are named, with WCAG 2.1 and EN 301 549 encouraged (PDF pp. 30 to 31). This touches DHCraft's web work for clients.
- Labelling does not exempt from other law, for example consent of depicted persons or rightsholders (PDF p. 29).

### Research
- The Code says nothing specific on research publications. Its exception for human review applies to any deployer, so a scholarly text with substantive review and a named responsible person needs no label. Measure 1.2 allows altering metadata markings for "research purposes" (PDF p. 10), which concerns providers only.

### Programming
- If DHCraft becomes the provider of a generative system, for example an agent that it puts into service under its own name and that outputs text, Section 1 applies. A downstream provider "may rely on the results of testing performed by an upstream model provider or a third-party provider of marking and detection solutions", but keeps ultimate responsibility (PDF p. 21). Reliance on open-source marking solutions is to be documented (PDF p. 21).
- Providers retain and do not intentionally remove existing metadata markings of content their system transforms (PDF p. 10). Providers are encouraged to offer an option that lets deployers apply a perceptible label upon generation (PDF p. 11).
- Compliance processes, testing and training are to be proportionate for SMEs and small mid-caps (PDF pp. 7, 20 to 21).

### Organisation
- Deployers keep "appropriate internal compliance processes and documentation" on how they label, proportionate to size (PDF p. 33), and, where AI is used regularly for published text, a process to verify that labels are placed correctly (PDF p. 34).
- Deployers ensure "awareness of the disclosure obligations under Article 50(4) and (5) AI Act among their personnel, including employees, and external contractors directly involved in the implementation of disclosure measures" (PDF p. 34). Training on when disclosure is required, on editorial responsibility and on correcting missing labels is encouraged (PDF p. 34).
- Substantiated reports of missing or wrong labels are to be reviewed and remedied without undue delay (PDF pp. 34 to 35).

## Limits
- The PDF carries no date and no document number; the date rests on the Commission news page. The Code's adequacy assessment by Commission and AI Board was pending at publication according to that page; this summary did not read the Commission opinion on the assessment.
- The Code binds only signatories. For non-signatories it is a reference point, not a legal duty.
- Section 1 was read in full on PDF pp. 5 to 12 and 20 to 22; the technical requirements on PDF pp. 12 to 19 (detection, robustness, interoperability) and the glossary on PDF pp. 22 to 25 were scanned, not studied, because they concern providers of marking technology.
