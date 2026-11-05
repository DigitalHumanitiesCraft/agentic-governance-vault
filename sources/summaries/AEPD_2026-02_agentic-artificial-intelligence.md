# Agentic Artificial Intelligence from the Perspective of Data Protection

Publisher: Agencia Española de Protección de Datos (AEPD), Madrid
Date: Version 1.1, February 2026 (as stated on the cover)
Original: [AEPD_2026-02_agentic-artificial-intelligence.pdf](../AEPD_2026-02_agentic-artificial-intelligence.pdf)
Bindingness: Empfehlung (non-binding guidance of a supervisory authority; the text calls itself "an introductory study without pretensions to be exhaustive", PDF p. 70)

## Core statement
A 71-page guidance paper from the Spanish data protection authority on what changes in a personal data processing when it is carried out fully or partly by AI agents. It describes agent architecture, vulnerabilities, GDPR compliance questions, threats such as prompt injection and memory poisoning, and a catalogue of measures. Its main position is that the agent is only a means of processing, so the controller stays fully responsible and must govern, minimise, limit autonomy, log and supervise. It rejects both irrational rejection and uncritical acceptance of agents (PDF p. 2).

## Relevance to the Leitfrage
### Client projects
- Role clarification: the controller determines purposes and means "regardless of the form" of the means, including agentic systems, and must ensure compliance and manage the new risks (PDF p. 31). A provider of an agentic service that processes personal data in the framework of the controller's processing acts as processor (PDF p. 33). Third-party services receiving personal data are processors; services that receive no personal data or cannot link it to a user have no data protection role (PDF p. 32).
- Candidate rule: before an agent touches client personal data, document each service in the chain with its data protection role and the contract, and design and document the data flows (PDF p. 33, accountability).
- Transparency: additional recipients, for example a generative AI service of another entity, must be named to data subjects and users, storage periods and additional automated decisions must be informed (PDF p. 34). Further processing for a new purpose needs prior information under Art. 13(2) GDPR (PDF p. 34).
- Lawfulness: if the agent adds no processing beyond the original, no new basis is needed; if it does, a basis and for special categories an Art. 9 exception are required (PDF p. 35). The use of an agent "is not a purpose in itself" (PDF p. 35).
- The RoPA must be updated when agents replace traditional means: categories, recipients, transfers, retention, Art. 32 measures (PDF p. 36).
- Data subject rights must remain exercisable; memory and logs must be technically able to support access, rectification, erasure, restriction and objection by design (PDF pp. 26, 36 to 37).
- Art. 22 GDPR: agents do not always produce automated decisions, but where they do, the conditions, safeguards and information duties apply (PDF pp. 37 to 38). Other automated actions such as sending mail or transferring files can affect confidentiality and call for reversibility by design (PDF p. 38).
- International transfers that arise through agents need Chapter V safeguards and entry in the RoPA; without them the agent should be redesigned or replaced (PDF pp. 42 to 43).
- A DPIA is not required in every case but depends on the processing and agent type; an existing DPIA must be reviewed (PDF p. 41).
- An agent must not give consents or enter contracts on behalf of a user without control (PDF pp. 30, 33).

### Research
The source says nothing specific on research, research integrity, funding applications or peer review. Its general points on hallucination-free sources are limited to quality of retrieved external information (PDF p. 20) and are framed as data protection accuracy issues.

### Programming
- Rule of 2, in its AI agent formulation: an agent should not combine all three properties of processing untrusted inputs, access to sensitive information and the ability to act automatically. Allowed pairings are: with untrusted input and sensitive access, no automatic action without human supervision; with sensitive access and action, guarantees of integrity are needed; with untrusted input and action, no access to sensitive information or personal data (PDF pp. 39 to 40). The figure itself is not readable in the extracted text; the three cases are described in the running text.
- Prompt injection: direct and indirect, including instructions hidden in PDFs, emails or web pages (PDF p. 49). Named variants include memory poisoning and RAG poisoning, zero-click injection, data exfiltration through URL parameters, session hijacking and lateral movement, long pipeline attacks, context confusion, delayed triggers, privilege escalation through tools, attacks on workflow platforms, screen control and deletion or ransomware (PDF pp. 49 to 50).
- Controls named: strict separation of data and instructions, labelling and traceability of content origin, limited tool privileges, validation and sanitisation of inputs at each stage, guardrails (PDF p. 61); service catalogue and whitelists with versions (PDF p. 61); restriction of accessible services to what a processing needs (PDF p. 61); guardrails and rigid formats on tool parameters and on tool responses (PDF p. 62).
- Human checkpoints: defined criteria for approval before high-impact actions, irreversible actions such as permanent deletion, sending communications or payments, atypical behaviour, and user-defined limits (PDF p. 62). Reversibility of agent actions should be assessed (PDF p. 62). Adjustable autonomy per processing (PDF p. 62).
- Identity and privileges: least privilege, granular RBAC/ABAC, MFA for high-privilege accounts, limited credential lifetime, no delegation of privileges between agents except in predefined flows, mutual authentication between agents (PDF p. 66). Excessive permissions make an agent a pivot point between systems (PDF p. 30).
- Sandboxing: containers or microVMs and restricted terminals with limited commands, services and network access, "essential in the deployment test phases" (PDF p. 67).
- Circuit breakers and hard step limits for loops, goal deviation and mass data access (PDF p. 68). Data extraction flow control requiring express user action for mass shipments to third parties (PDF p. 67).
- Update control with the power to decide when updates go to production, version control with roll-back (PDF pp. 66 to 67).
- Repeatability: record configuration of decision processes including inputs, intermediate data traffic and pseudo-randomness settings such as seeds and temperature (PDF p. 66). The source states that agent behaviour is non-repeatable without control of sources, services, versions and memory (PDF pp. 29 to 30).
- Verification and validation tests remain applicable; golden tests with reference results to detect deviations (PDF pp. 54, 65).
- A standard operating procedure for prompts with structured fields (PDF pp. 65 to 66).
- Easy low-code agent tools (n8n is shown) tempt unqualified users to deploy outside governance, described as "BYOAgentic" (PDF p. 21).
- Candidate rules for DHCraft agents: no combination of untrusted input, sensitive access and autonomous action without a human gate, least privilege per task, sandboxed execution, whitelisted tools, step limits, and log of inputs, tool calls and versions.

### Organisation
- A governance framework that includes agentic AI "is the most important measure" (PDF p. 51). Its elements include assigned roles, selection criteria for agents and connections, redesign control of processing, human supervision, formalised relationships with model and service providers, monitoring and retirement, incident management and training (PDF pp. 52 to 53).
- Accept the possibility of failure: design processing and reaction plans on the principle of safe failure (PDF p. 52).
- Misuse of the human as scapegoat: responsibility must not be shifted to the supervisor; the user and supervisor have assigned responsibility within limits, but it does not replace the controller's diligence in design and tool selection (PDF p. 47). Automation bias can undermine human supervision (PDF pp. 28, 47 to 48).
- Effective human supervision requires competence and authority, training, independence, diligence, means, information and time. A four-eyes principle may apply for high-impact processes (PDF pp. 63 to 64).
- Memory control: compartmentalise memory by processing, case and user, retention limits, option to disable persistent memory, sanitisation, no-log or zero-retention policy at component level (PDF pp. 58 to 60).
- Documentation as an integrity-controlled, dynamically maintained record of decisions, architecture and events; traceability and data lineage (PDF pp. 64 to 65).
- Qualified professionals needed for deployment (PDF p. 64). Literacy at management, ICT and user levels, and the role of the DPO (PDF p. 69).
- Evidence-based continuous assessment, automated where the processing is automated (PDF p. 53), and avoidance of "checkbox security" (PDF p. 51). Incremental, precautionary rollout starting with low-risk uses (PDF p. 55).
- Contracts and terms of service of services change unilaterally and must be evaluated at design and over the life cycle (PDF p. 54).
- The paper recommends the LIINE4DU threat modelling framework (PDF p. 38), refers to the IMDA Singapore governance framework as a guide (PDF p. 52, footnote 39) and notes that the AI Act or other regulations may also apply depending on entity and system (PDF p. 8, 52).

## Limits
- Non-binding guidance of the Spanish authority, not an EDPB text; the Austrian authority is not mentioned.
- Scope is data protection of personal data processing by controllers and processors; it explicitly excludes domestic use, model development and training, and organisations where no personal data is processed (PDF p. 8).
- It does not analyse any concrete processing and describes risks as not inherent to all agents (PDF pp. 9, 17).
- No guidance for research integrity, funding, publication or software licensing questions.
- The Rule of 2 figure is not in the extracted text, so its wording is reconstructed from the explanatory paragraphs.
- The paper is general and rarely distinguishes small organisations; many measures assume an organisation with a DPO and an ICT department.
