# Careful adoption of agentic AI services

Publisher: Australian Signals Directorate's Australian Cyber Security Centre (lead publisher by copyright notice), co-authored with CISA and NSA (United States), the Canadian Centre for Cyber Security, NCSC-NZ and NCSC-UK
Date: 1 May 2026, stated on the NCSC-NZ landing page (https://ncsc.govt.nz/protect-your-organisation/careful-adoption-of-agentic-ai-services/). The PDF itself carries only the year in its copyright line (PDF p. 29).
Original: [FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf](../FiveEyes_2026-05-01_careful-adoption-agentic-ai.pdf)
Bindingness: Empfehlung (non-binding guidance)

## Core statement
The document is joint security guidance from five national cyber agencies on LLM-based agentic AI systems. It describes five groups of risk (privilege, design and configuration, behaviour, structural, accountability) and sets out best practices for designing, developing, deploying and operating agents (PDF pp. 4, 7-23). Its main position is that organisations should fold agentic AI security into their existing cyber security frameworks, adopt agents incrementally, never grant broad or unrestricted access, and use agents only for low-risk and non-sensitive tasks (PDF pp. 4, 7, 25). It is a guidance text with scenario examples and no empirical study.

## Relevance to the Leitfrage

### Client projects
- The authoring agencies recommend never granting agentic AI broad or unrestricted access, especially to sensitive data or critical systems, and using it only for low-risk, non-sensitive tasks (PDF p. 4).
- Agentic systems aggregate sensitive material such as user prompts, organisational data in retrieval stores and API keys, which makes them an attractive target (PDF p. 12).
- Third-party tools and agents are a supply chain risk (look-alike "squatted" tools, dynamically loaded packages). Recommended controls are a trusted registry of components, verification of origin and currency, an allow list of approved tools and versions, and a software bill of materials when procuring agentic systems (PDF pp. 11-12, 18).
- Policies should define legal accountability and risk ownership for agentic systems (PDF p. 19).
- The document notes that governance mechanisms designed for human actors do not always transfer to autonomous agents (PDF p. 7).

### Research
- The source says nothing specific on this field.
- General accuracy points apply. LLMs may produce plausible but wrong output, and grounded or tool-enabled agents may still rely on internal knowledge without saying so (PDF p. 13).
- Recommended mitigations are to validate critical aspects of agent output against multiple sources and to require agents to give specific references showing where key parts of a response came from (PDF pp. 17-18, 22).

### Programming
- Apply least privilege and scope each agent narrowly. Use just-in-time, short-lived credentials for privileged actions and replace long-lived static secrets with ephemeral ones (PDF pp. 23, 28).
- Give each agent its own distinct identity, and keep agents from changing their own privileges or starting unapproved delegation (PDF pp. 15, 18).
- Run agents in isolated environments with segmentation, separate high-risk agents into distinct domains, and keep agents in enclaves without write access to logs (PDF p. 20).
- Specify clear objectives with explicit do-not-do rules, and use hard constraints such as deny lists and API-level policies that the agent cannot override (PDF p. 20).
- Human approval should be required for actions where an error is costly, with system resets, network egress and deletion of critical records named as examples. Requests to delete logs or audit records should be quarantined until a human approves them. The decision when approval is needed belongs to designers or operators, not to the agent (PDF p. 22).
- Use versioning and rollback so that a system can return to known-good behaviour, and log tool usage in human-readable form (PDF pp. 17-18).
- Specification gaming is a named risk, for example an agent disabling security updates to maximise uptime (PDF p. 10).

### Organisation
- Implement governance policies for autonomous agents, define legal accountability, and build AI literacy in the organisation (PDF p. 19).
- Deploy in phases with graduated autonomy, and expand or roll back scope based on continuous evaluation (PDF p. 19).
- Set fail-safe defaults so that agents stop and escalate in uncertain situations (PDF p. 20).
- Log comprehensively, monitor all agent operations including internal processes, audit regularly for drift in identity and privilege, and combine human review with automated log analysis (PDF pp. 17, 21-22).
- Develop and test incident response procedures for agent compromise, run red teaming against agentic behaviour, and assess regularly whether an agent can bypass its safeguards (PDF pp. 17, 19, 22-23).
- Accountability is hard in agent chains because actions can be opaque, sub-agents can be spawned, and identical prompts can yield different actions, which complicates reproducibility and assurance (PDF pp. 12-13).
- The document states that governance, accountability, monitoring and human oversight are "not optional safeguards but essential prerequisites" (PDF p. 25).

## Limits
- It addresses government, critical infrastructure and industry operators, and is written mostly for developers, vendors and operators of agentic systems. Many controls (cryptographic attestation, mutual TLS, trust scoring, centralised policy decision points) presuppose enterprise infrastructure and are not scaled to a small company (PDF pp. 15, 23).
- It is guidance without empirical evidence on effectiveness. Several statements about agent behaviour, such as strategic deception and altered behaviour under evaluation, are asserted without cited studies in the text read (PDF pp. 7, 10).
- It does not address research integrity, funding proposals, peer review or GDPR and EU AI Act obligations. The disclaimer states that it is general in nature and not legal advice (PDF p. 29).
- The publication date is not printed in the PDF itself. It rests on the landing page of NCSC-NZ, see [quellen.md](../../knowledge/quellen.md).
