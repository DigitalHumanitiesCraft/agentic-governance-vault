# Securing Open Source in the Age of AI: A Practical Guide for Maintainers, Security Engineers, Researchers, and the Communities That Depend on Them

Publisher: Open Source Security Foundation (OpenSSF) and Cloud Native Computing Foundation (CNCF), both Linux Foundation; eBook, version 1.0
Date: May 2026 ("Version: 1.0 | May 2026", PDF p. 1)
Original: [OpenSSF-CNCF_2026-05_securing-open-source-age-of-ai.pdf](../OpenSSF-CNCF_2026-05_securing-open-source-age-of-ai.pdf)
Bindingness: Empfehlung (non-binding guidance)

## Core statement
The eBook collects practices from maintainers, security engineers and downstream consumers for handling AI-assisted contributions, AI-found vulnerabilities and AI tools in open source work (PDF p. 2). Its central claim is that AI does not change the fundamentals of open source security, only the velocity of attacks, reports and fixes (PDF p. 2). It asks projects to state their stance on AI contributions, to document a threat model, to verify model output before merging, to check every dependency a model suggests, to prefer signed models and packages with provenance, and to weigh open or local models against shared public models (PDF pp. 8-12). The guide is short (20 pages) and written for open source projects; it is a practice guide without empirical evaluation.

## Relevance to the Leitfrage

### Client projects
- A project should publish how it wants security defects reported, for example in a SECURITY.md, and offer a private channel for confidential reports (PDF p. 8).
- A project should state its stance on AI-contributed or AI-derived content and document it in a discoverable AI policy, including what AI content it will not accept: "The project should state what their stance on AI-contributed or derived content is." (PDF p. 8).
- A documented threat model, including explicitly forbidden configurations, helps both human and AI contributors focus on relevant issues (PDF p. 8).
- Third-party projects may refuse AI-generated code; where a project has an AI-use policy, contributors should follow it (PDF p. 16).

### Research
- Security researchers using AI should disclose whether and how AI tools were used in a report, give a proof of concept privately, and propose a patch and test cases (PDF pp. 14-16). The heading reads "Be Clear and Up-Front if and How AI Tools Were Used in the Report" (PDF p. 16).

### Programming
- Model output must be verified before merging: "the old cybersecurity maxim “Trust, but verify” must be top of mind when evaluating the model’s output before merging." (PDF p. 12).
- Models recommend old, vulnerable dependencies or non-existent packages; attackers register such hallucinated names ("slopsquatting"), so every suggested dependency must be checked (PDF p. 12).
- Adversaries seed malicious packages and models. Knowing where a model or package came from matters, and signed artifacts (model signing), combined with attestations such as SLSA, help confirm origin and integrity, "but only when verified" (PDF p. 12).
- Running open models on local or isolated hardware keeps sensitive data inside the trust boundary; public large models are shared environments where requests may be used for training (PDF p. 10). Small language models can suit narrow tasks with data security benefits (PDF p. 10).
- No single model is best for every scenario; weigh models per task and budget (PDF p. 10). A smaller, focused model for a well-scoped task is cheaper and lower in carbon (PDF p. 7).
- Persona prompting alone was found in earlier studies to give less secure code; combine prompts with security context such as the OWASP Top 10 and the OpenSSF guides (PDF pp. 9-10).
- Prompt quality can be paired with evaluation, repeatable test prompts and regression testing (PDF p. 6).

### Organisation
- AI use requires more expertise, not less: "The use of AI also matters greatly here, requiring more expertise to use effectively, not less." (PDF p. 6).
- Token and API costs can run out of control without guardrails; budget them (PDF p. 7).
- No external party or tool can rate an organisation's risk; assess every AI-produced finding in the organisation's own context (PDF p. 6).
- The closing section restates least privilege, minimal images, rebuild and redeploy and default deny as the continuing imperative (PDF p. 17).

## Limits
- It is written for open source maintainers and researchers, not for a service firm with client repositories. Transfer to DHCraft is an inference.
- The tone is informal; many statements are practice advice without evidence. Statements on model signing describe what signing can show, not an evaluated control.
- It names products and programmes (for example a commercial inspection tool offered free to qualifying projects) that the knowledge base does not adopt.
- The text gives no concrete criteria for when a local model is adequate, and no process for approving a model.
