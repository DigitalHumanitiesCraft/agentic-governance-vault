# Auswirkungen auf die Cybersicherheit von Organisationen durch die Entwicklung im Bereich Künstlicher Intelligenz

Publisher: Bundesamt für Sicherheit in der Informationstechnik (BSI), BSI-IT-Sicherheitsinformation BITS-B Nr. 2026-262788-1032, TLP:CLEAR, criticality 2 / yellow
Date: 22 June 2026 ("Version 1.0, 22.06.2026", PDF p. 1 and footer of every page)
Original: [BSI_2026-06-22_ki-auswirkungen-cybersicherheit.pdf](../BSI_2026-06-22_ki-auswirkungen-cybersicherheit.pdf)
Bindingness: Empfehlung (security information of a German federal authority; not binding for an Austrian company)

## Core statement
The BSI warns that current AI models find vulnerabilities and produce working exploits at scale and partly autonomously, so that organisations must expect more zero-days, faster exploitation of published patches and more incidents (PDF pp. 1 to 3). It adds that AI systems themselves widen the attack surface, in particular through indirect prompt injection in agentic systems that are coupled to tools, APIs or workflows (PDF p. 3). The recommended measures are mostly established practice that the BSI says is often neglected: know and minimise the attack surface, patch exposed systems within hours, assume breach and strengthen detection and logging, least privilege, MFA, backups, separation of development environments, and awareness of AI-supported social engineering (PDF pp. 4 to 6). AI tools may support defence but "lediglich eine ergänzende, niemals jedoch eine ersetzende Maßnahme darstellen sollten" (PDF p. 7).

## Relevance to the Leitfrage

### Client projects
- Every system reachable from the internet is to be treated as an initial point of attack; exposure of services and ports is to be limited to what is necessary and verified actively (PDF p. 4). This concerns the web applications DHCraft runs for clients.
- Exposed systems are to be patched first: "Kurzfristiges Einspielen von Patches innerhalb weniger Stunden, besser Minuten sollte gewährleistet werden" (PDF p. 5). Software and hardware should be replaced before end of support (PDF p. 5).
- Organisations should know which of their systems are reachable from partners or service providers, so that they can be cut off in an incident at the partner (PDF pp. 4, 6).

### Research
- The source says nothing specific on this field.

### Programming
- Agents: hidden instructions "beispielsweise auf Webseiten, in Dokumenten oder E-Mails" can steer a model, and this becomes critical "vor allem in agentischen Systemen, in denen LLMs mit externen Tools, APIs oder automatisierten Workflows gekoppelt sind und ihre Ausgaben direkte Aktionen auslösen können" (PDF p. 3). Consequences named are data exfiltration, unauthorised system access and persistent malware (PDF p. 3).
- "KI-Komponenten müssen daher wie andere sicherheitskritische IT-Systeme betrachtet und durch geeignete Schutzmaßnahmen, Isolation, Validierungsschichten und Berechtigungskonzepte abgesichert werden" (PDF p. 3). Models can carry backdoors through poisoning, so they should come from trustworthy sources (PDF p. 3).
- "Trennen Sie Entwicklungsumgebungen von anderen Netzwerk-Bereichen, um weitreichende Kompromittierungen durch Supply-Chain Angriffe auf Software-Bibliotheken bzw. über Paketmanager (npm. PyPI, etc.) zu verhindern" (PDF p. 6). Outbound communication and the credentials available in CI/CD pipelines and on developer clients are to be minimised (PDF p. 6).
- Software makers can use AI during development to find vulnerabilities in source code and to test products and patches before release (PDF p. 7).

### Organisation
- IT security needs a responsible function and the backing of management (PDF p. 4).
- Logs of network traffic and system events are to be stored outside the system itself, backed up and kept as long as the law permits (PDF p. 5).
- Staff are to be trained on AI-supported phishing, including deepfake video calls and cloned voices (PDF p. 6).
- Where capacity is lacking, external service providers should be considered for hardening and incident response (PDF p. 6).

## Limits
- The document addresses organisations in Germany, with operators of exposed infrastructure as main audience. Patch times of minutes to hours may be disproportionate for a small company without round-the-clock staff; the BSI itself asks for reachability outside working hours (PDF p. 5).
- Its focus is AI as an attack tool. Agent use inside the organisation is treated in one paragraph (PDF p. 3), and for the secure adoption of agentic AI the BSI refers to the Five Eyes guide already in the base (PDF p. 7).
- It names individual frontier models and cites vendor blogs and a preprint on agent worms; this summary did not read those references.
