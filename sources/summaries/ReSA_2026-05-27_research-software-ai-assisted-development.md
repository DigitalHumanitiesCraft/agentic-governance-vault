# Research Software in an Age of AI-Assisted Development: Reflections from Edinburgh

Publisher: Research Software Alliance (ReSA) community on Zenodo, an attribution taken from the Zenodo community record of the DOI, since the PDF itself names only its authors and the Edinburgh workshop; report of 27 authors from the research software engineering community, funded by Schmidt Sciences (PDF p. 14)
Date: 27 May 2026 (stated on PDF p. 1; Zenodo publication date 2026-05-27, DOI 10.5281/zenodo.20321134)
Original: [ReSA_2026-05-27_research-software-ai-assisted-development.pdf](../ReSA_2026-05-27_research-software-ai-assisted-development.pdf)
Bindingness: Empfehlung (community position and call to action, explicitly not a consensus of all authors)

## Core statement
The 14-page report grew out of a draft vision statement for the workshop "Research Software Engineering in the Age of Generative AI" in Edinburgh, March 2026, and records principles, risks and open questions rather than one agreed position (PDF p. 2). It starts from the assumption that AI-assisted and agentic coding tools are and will be used, and treats them as amplifiers of existing practice, good or bad (PDF p. 2). Five principles follow: research remains a human responsibility, engineering discipline matters more than ever because verification becomes the bottleneck, transparency and reproducibility need more than a disclosure of AI use, software engineering is a function everyone who codes must exercise, and sustainability needs investment in people (PDF pp. 5 to 9). It closes with a call to action for developers, research leads and the technology community (PDF pp. 12 to 14).

## Relevance to the Leitfrage
### Client projects
- Data flows: "Understand where data flows when using AI tools, both during their use and when deploying research tools that have relied on AI for their development." Data handling must be consistent with data management plans, ethics approvals and information security requirements (PDF p. 12, section 4.1).
- The report names unresolved questions of licensing, consent, attribution, authorship and copyright for code generated from training data of uncertain provenance (PDF pp. 10 to 11). This matters where DHCraft delivers agent-written code to clients under a licence.

### Research
- "Human agency and accountability must remain at every key decision point." (PDF p. 5, section 2.1).
- Transparency: because prompting moves programming to a higher level of abstraction, "disclosing that AI was used is not enough." The report asks for norms to document the decisions and constraints that shaped the output, the prompts and models used, and possibly the specifications and requirements from which code was generated (PDF p. 7, section 2.3).
- Reproducibility at scale is named as a key risk, given non-deterministic tools, fast-changing models and unclear provenance; what matters is a sufficient record of what was done (PDF p. 10, section 3).

### Programming
- Verification is the new bottleneck: AI-generated code lacks the implicit domain checks of a human author, so "if you can't check that it works, you shouldn't trust the results." (PDF p. 5, section 2.2). For quick tasks this means at least checking outputs against expected behaviour, testing edge cases and not assuming the code is correct because it runs (PDF p. 5).
- Responsibility: "Remember that you are responsible for the software you produce, especially AI-generated components." The developer's role is to understand what the code does, verify that it works and own the results (PDF p. 12, section 4.1).
- Testing, human review, documentation and version control are named as the most important tools in the AI era (PDF p. 12, section 4.1). Test-driven development as a closed loop for agentic code generation "should be considered" (PDF p. 6).
- The report notes a sycophantic tendency and a bias of current tools towards producing something, and suggests tools that plan first and check the plan with the researcher (PDF pp. 7 to 8).
- Quality at scale: without investment in review and validation, generated volume may amplify bugs and propagate subtle errors (PDF p. 10, section 3).

### Organisation
- Erosion of critical skills is the first key risk; if AI becomes a shortcut around understanding, the capacity for critical evaluation degrades (PDF p. 10, section 3). Leads should invest in people and protect on-the-job learning, because AI could erode the apprenticeship pipeline (PDF pp. 12 to 13, section 4.2).
- Leads should set clear expectations: "Adapt policies and norms for AI use in research and research software that prioritize quality, transparency, and reproducibility." (PDF p. 13, section 4.2). They should create time for evaluating tools and evaluate where AI adds value (PDF p. 13).
- Institutional misunderstanding is named as a risk: AI tools do not reduce the need for skilled practitioners who evaluate outputs (PDF p. 11).

## Limits
- A workshop report that captures discussion; the text says not all authors agree with all points (PDF p. 2). It contains many open questions rather than settled rules.
- No empirical data; statements are expert judgement.
- Not specific to the humanities; it addresses research software in general.
- Published on Zenodo without peer review.
