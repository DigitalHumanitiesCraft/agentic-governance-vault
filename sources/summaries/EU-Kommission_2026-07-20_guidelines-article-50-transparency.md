# Guidelines on the implementation of the transparency obligations for certain AI systems under Article 50 of the AI Act

Publisher: European Commission (document C(2026) 5054 final, annex to a Communication approving the content of the draft Commission Communication)
Date: Brussels, 20.7.2026 (as stated on the source)
Original: [EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf](../EU-Kommission_2026-07-20_guidelines-article-50-transparency.pdf)
Bindingness: Empfehlung (non-binding guidance on a binding law; the text says "These Guidelines are non-binding", PDF p. 4)

## Core statement
A 51-page guidance document on Article 50 of the AI Act. It explains the four transparency duties: information that one interacts with an AI system (Art. 50(1)), machine-readable marking and detection of synthetic content (Art. 50(2)), information about emotion recognition and biometric categorisation (Art. 50(3)), and labelling of deep fakes and of AI-generated texts on matters of public interest (Art. 50(4)). It names AI agents and coding agents explicitly and clarifies what falls outside the duties, which is relevant for DHCraft both as a builder of agent workflows and as an author of texts.

## Relevance to the Leitfrage
### Client projects
- Role test for deployers: a legal person remains the deployer even if contractors or freelancers operate the system on its behalf and under its control; its own employees are not separate deployers (PDF p. 7, para. 14). A company that commissions an agency without deciding whether or how AI is used is not a deployer (PDF pp. 7 to 8, para. 14).
- Deployers who use AI to generate or manipulate texts that inform the public on matters of public interest must disclose this (Art. 50(4)), unless the text underwent human review or editorial control and a person holds editorial responsibility (PDF p. 44, paras. 132 to 133). Human review means deliberate examination of the substance by persons with relevant knowledge, with fact-checking as minimum; spell-checking, automated review or cursory approval do not count (PDF p. 44, paras. 134 to 135). Substantive AI changes after the review void the exception (PDF pp. 44 to 45, para. 136). The person or function with editorial responsibility should be named publicly (PDF p. 45, para. 138).
- Explicit examples outside Art. 50(4): "AI-manipulated text by a consultant for a client advice regarding measures to be taken for regulatory compliance" (PDF p. 43); also private or organisation-internal correspondence is not "published" (PDF p. 43).
- Examples inside Art. 50(4) that would matter for publishing: AI-generated summaries of articles, and AI-manipulated parts of articles on public-interest topics, unless reviewed (PDF p. 43). Translations that underwent human review are given as an example of the exception (PDF p. 45).
- Candidate rule: before publishing AI-assisted texts on public-interest topics for or with clients (reports, websites, news-style items), document a substantive human review with fact-check and a named person with editorial responsibility, otherwise label the text.
- Art. 50 is "without prejudice" to the GDPR and consumer law; the AI notice does not replace data protection information duties (PDF pp. 20 to 21, paras. 50 to 52). Where a service is AI-driven, the AI function may be an essential characteristic that must be disclosed before a consumer contract (PDF pp. 20 to 21, para. 50).

### Research
- Exclusion: Art. 2(6) AI Act excludes AI systems and models, including their outputs, developed and put into service for the sole purpose of scientific research and development. This is "without prejudice to applicable research ethical standards and EU data protection" law. If the system or outputs are used for other purposes, Art. 50 applies (PDF p. 9, para. 21). Art. 2(8) excludes research, testing and development before placing on the market; testing in real-world conditions is not covered (PDF p. 10, para. 22).
- Texts: AI-generated summaries and paraphrasing beyond minor correction count as semantic changes that need marking by the provider (PDF p. 30). This is a provider duty; for researchers using such tools it matters only if they place their own system on the market.
- Academic peer review is cited as an example of human review in the Art. 50(4) text exception (PDF p. 44, para. 134), and an internally peer-reviewed academic blog as example of editorial responsibility held by a research centre (PDF p. 45).
- Otherwise the source says nothing specific on research integrity or funding applications.

### Programming
- Coding agents are listed as AI systems "capable of directly interacting with natural persons" and therefore covered by Art. 50(1) (PDF p. 13, para. 31). AI agents must be designed so that they disclose their artificial nature and the person on whose behalf they act. Where the provider cannot predict contacts with natural persons, the agent should be designed at architecture level, and instructed, to disclose itself wherever interaction with a person is reasonably likely. Agents should also disclose themselves to the persons instructing them at key steps such as authorisation, reporting and validation, and at every new interaction (PDF p. 13, para. 31).
- Examples of disclosure: an email generated by an AI agent carries an AI label at the top (PDF p. 15, para. 36); AI identifiers and verifiable credentials, with EU digital identity wallets named as one option (PDF p. 15, footnote 21). Terms and conditions or documentation alone are insufficient (PDF p. 16, para. 38).
- Candidate rule: any agent that sends mail, messages or comments to people, for example an issue or pull request comment, states that it is an AI agent and on whose behalf it acts.
- Exceptions: AI-powered code assistance and code review chatbots "available only to professional developers" fall under the obviousness exception, as do internal assistants for trained, AI-literate staff (PDF p. 18). The exception is read restrictively; where the general public could be reached it cannot be relied on (PDF pp. 17 to 18, para. 45).
- Machine-to-machine calls between AI systems, including agents, whose outputs are not meant to reach natural persons are outside Art. 50(1) (PDF p. 13, para. 30). Text and code auto-completion is listed as outside the interaction duty (PDF p. 14).
- Marking duty (providers only): source code, configuration, SQL, IaC, YAML, JSON, scripts, APIs and libraries are outside the Art. 50(2) marking duty, as are short sequences such as single words or alt-text and exclusively machine-to-machine outputs, including agent-to-agent communication (PDF p. 24, para. 68). Agent actions are in scope only if they output AI-generated audio, image, video or text perceptible by people; chain of thought, web requests and browser actions are not (PDF p. 23, para. 63).
- Modification: a company that modifies an existing generative AI system and puts it into service under its own name becomes a provider of the new system (PDF p. 7).

### Organisation
- Dates: Art. 50 applies from 2 August 2026. A transitional rule from the AI Omnibus gives existing generative systems until 2 December 2026 for the marking obligation only; the interaction disclosure applies from 2 August 2026 (PDF p. 51, para. 153). Content created before 2 August 2026 need not be labelled retroactively, but texts created earlier and published on or after that date must be labelled if in scope (PDF p. 51, para. 154).
- Literacy: Art. 4 AI Act applies to providers and deployers within the scope of Art. 50 (PDF p. 11, para. 25). Compliance with Art. 50 does not mean the use is lawful otherwise (PDF p. 10, para. 25).
- Compliance evidence: adherence to a code of practice assessed as adequate is called the most straightforward way to demonstrate compliance. Non-signatories are expected to explain their measures, for instance by a gap analysis against the code, and may face more information requests (PDF pp. 48 to 49, paras. 146 to 148). A code of practice on transparency of AI-generated content was published on 10 June 2026 (PDF p. 48, footnote 43).
- Penalties: up to EUR 15 000 000 or 3 % of worldwide annual turnover, whichever is higher; for SMEs whichever is lower (PDF p. 50, para. 152).
- Personal non-professional use is excluded for deployers, but "freelance activity" counts as professional (PDF p. 9, para. 19).
- Information must be clear, distinguishable, at the latest at first interaction or exposure, and accessible (PDF pp. 47 to 48, paras. 141 to 144).
- Candidate rules: a register of DHCraft's roles per AI system (provider, deployer), a decision record on whether the exceptions apply, and a calendar entry for the transitional date and for the next revision of the guidelines.

## Limits
- Non-binding; only the Court of Justice can interpret the AI Act authoritatively (PDF p. 4, para. 5). The document is first-edition guidance and may be amended or withdrawn (PDF p. 51, para. 155).
- The cover page labels the file an annex to a Communication approving the "draft" guidelines; whether this is the final published text is not stated in the file.
- Addresses mainly providers of interactive and generative systems and deployers of deep-fake and public-interest text content. It does not address ordinary internal use of coding assistants by developers, research integrity, funding rules or data protection beyond cross-references.
- The sections on deep fakes (PDF pp. 34 to 42), emotion recognition and biometric categorisation (PDF pp. 31 to 34) were read at lower depth since they have no obvious application to DHCraft's work; no rule is derived from them here.
- Page citations refer to PDF pages; the table of contents numbers are printed pages and differ by one.
