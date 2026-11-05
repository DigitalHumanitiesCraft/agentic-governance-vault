# Managing the cyber risk of agentic AI

Publisher: National Cyber Security Centre (NCSC-UK), blog post
Date: 20 August 2026 (as stated at the foot of the page)
Original: [NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md](../NCSC-UK_2026-08-20_managing-cyber-risk-agentic-ai.md)
Bindingness: Empfehlung (non-binding guidance)

## Core statement
The post offers interim practical advice for designers and operators of environments in which AI agents act with significant autonomy. The NCSC says the advice rests on its own research to date and will be superseded by formal guidance (section "Advice and effective practice will continue to evolve"). Its main position is that controls should be proportionate to the autonomy granted, that model-level safeguards are a baseline only, and that sandboxing, observability, attribution and an emergency shutdown are needed in addition to careful prompting and human oversight.

## Relevance to the Leitfrage

### Client projects
- Apply controls in proportion to the autonomy of each deployment. Agents that only suggest or perform tightly constrained low-risk tasks need less than agents that act on production systems (section "Assess how much autonomy is needed").
- Restrict the agent's credentials, data and network reach to what the task needs, which limits the "blast radius" if the agent malfunctions or is compromised (section "Control the AI agent's environment", part b).
- Credentials include API keys, OAuth grants, SSH keys and authenticated sessions. Give an agent its own identity, minimal permissions and short-lived credentials, and where possible inject credentials through a proxy so the agent never holds them (part e).
- If an agent contacts third-party systems, make its traffic identifiable, for example through IP addresses that support reverse lookup or identifying HTTP headers. Treat abuse reports about the agent like vulnerability or abuse reports and follow an incident playbook (section "Make your AI activity easy to attribute").

### Research
- The source says nothing specific on this field.

### Programming
- Always run agents in a sandbox. For high-risk work the most robust option is an isolated, disconnected environment with pre-downloaded tools (part a).
- Deny inbound and outbound traffic by default and allow only what is required. The post gives a four-level maturity model for network access, from unrestricted (level 1) to no external access with a locally hosted model (level 4) (part c).
- It gives a four-level maturity model for compute isolation, from none (level 1) through containers (level 2) and virtualisation (level 3) to dedicated hardware (level 4). Built-in agent sandboxes should be evaluated, not assumed sufficient (part d).
- Agents may find and exploit configuration issues in controls, so use several layers of isolation and re-validate configurations regularly, and include explicit prompts not to leave the allowlist or attempt escape (part d).
- Do not rely on prompting alone. Combine prompts with technical and operational controls, and repeat critical constraints in long-running tasks because context compression may drop them (section "Prompt carefully").
- Write down which activities are in scope and which are red lines, and carry out threat modelling before deployment (section "Identify what could go wrong").

### Organisation
- Name individuals or a group responsible for agentic AI activity where unintended activity would have significant consequences (section "Set the right level of oversight").
- Choose between human-in-the-loop, human-on-the-loop and human-out-of-the-loop according to risk tolerance. For higher risk, combine human oversight with technically enforced controls. Approvals should be "guaranteed and gated" (sections "Prompt carefully" and "Set the right level of oversight").
- Judge models may help supervise agents but must themselves be evaluated independently (section "Set the right level of oversight").
- Log agent transcripts, reasoning traces and sandbox events such as access logs, proxy logs and network traffic. Protect the logs from modification or deletion and make them immutable where possible (section "Observability").
- Treat agent activity as user activity within security operations and incident response. Start autonomous runs in office hours when more oversight is available, and extend to nights and weekends only once controls are shown to work (section "Observability").
- Keep the ability to "pull the plug" at once, which includes cutting network access and the link between agent and inference service, not only stopping the agent process (section "Emergency shutdown").
- Review controls and assumptions continually so that granted autonomy stays proportionate to risk appetite (section "Further reading").

## Limits
- It is a short blog post, explicitly interim, with no empirical evaluation of the controls it recommends.
- It is aimed at designers and operators building highly autonomous agent environments. The higher maturity levels (dedicated hardware, locally hosted models) may be disproportionate for a small company.
- It refers to recent incidents involving unsanctioned agent activity through a linked NCSC statement, but this summary did not read that statement.
- It does not cover research integrity, data protection or EU legal obligations. The retrieval note (Retrieved 2026-11-05) in the file header is the compiler's, not the publisher's.
