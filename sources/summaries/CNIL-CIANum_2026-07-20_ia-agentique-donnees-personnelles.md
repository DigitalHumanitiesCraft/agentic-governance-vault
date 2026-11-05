# IA agentique et protection des données personnelles : équation à inconnues multiples pour les utilisateurs

Publisher: Commission nationale de l'informatique et des libertés (CNIL) and Conseil de l'IA et du numérique (CIANum), exploratory note
Date: 20 July 2026 (date of the CNIL announcement "IA agentique et données personnelles : la CNIL et le Conseil de l'IA et du Numérique publient une note exploratoire", https://cnil.fr/fr/ia-agentique-cnil-cianum-note, which calls the note "coécrite avec le CIANum"); the PDF title page states "juillet 2026"
Original: [CNIL-CIANum_2026-07-20_ia-agentique-donnees-personnelles.pdf](../CNIL-CIANum_2026-07-20_ia-agentique-donnees-personnelles.pdf)
Bindingness: Empfehlung (exploratory note without binding interpretation; several passages are wishes addressed to legislators and the EDPB)

## Core statement
The note examines how agentic AI strains the GDPR principles of purpose limitation, lawfulness, minimisation, accuracy, transparency and storage limitation, and the exercise of data subject rights (PDF pp. 6 to 8). It identifies two drivers of risk: persistent memory spread over several agents, and the enrichment of user profiles from connected services that the agent queries on its own initiative (PDF pp. 8 to 9). It then discusses automated decisions under Article 22 GDPR, unclear responsibility along the value chain and the enlarged attack surface (PDF pp. 10 to 12). Section IV proposes legal and technical safeguards: traceability per task, user control over data access, memory compartmentalisation with expiry, sandboxing, human approval graded by risk of the action, a kill switch, and evaluation of agent security and data protection (PDF pp. 13 to 16). The note states that agentic systems "demeurent pleinement soumises au RGPD" (PDF p. 13).

## Relevance to the Leitfrage

### Client projects
- An agent with access to a work environment (mail, calendar, document spaces) may read all available information for a request, although part of it is not needed for the task; such data may end up in memories or in external services (PDF p. 9). Only data "strictement nécessaires à l'exécution d'une tâche" should be processed, and the user should control which data the agents may access (PDF p. 14).
- Human approval must be real. A purely formal or automatic validation does not lift a decision out of Article 22 GDPR: "l'intervention humaine doit être [page break] réelle, effective et exercer une influence sur la décision finale ; une validation purement formelle ou automatique est insuffisante" (PDF pp. 10 to 11, citing CJEU C-634/21).
- With several agents and third-party services, the roles of controller and processor are harder to assign and accountability harder to demonstrate (PDF p. 11). Errors such as a mail to the wrong recipient or disclosure of confidential data to a third-party system are hard to trace to their origin (PDF p. 11).

### Research
- The source says nothing specific on research. Its point on accuracy applies to agent-assisted source work: hallucinations can propagate through the system without an alert mechanism (PDF p. 7), and divergent or outdated information can spread between agent memories (PDF p. 9).

### Programming
- Memory: "chaque agent devrait disposer d’une mémoire dédiée et isolée, sans accès automatique aux données des autres agents" (PDF p. 15). Memories may be limited in size, expire automatically, or be separated per processing through dedicated sessions (PDF p. 15).
- Deployment in an isolated environment (sandboxing) reduces access to the user's services and data to what is needed and limits exfiltration to that perimeter (PDF p. 15).
- Classify the possible actions on each connected service by risk, "accès à des données, modification et suppression de donnés, envoi de données hors système", and require human approval before high-risk actions (PDF pp. 15 to 16). A kill switch should allow stopping an agentic process at any time (PDF p. 16).
- Filtering applies at every call of a generative model through an agent, not only at the user's initial request; actions should be monitored in real time and robustness tested before and during deployment (PDF pp. 14 to 15).
- The secure integration of third-party services (applications, databases, tools) is named as the main challenge (PDF p. 15).

### Organisation
- Traceability: "Pour chaque tâche exécutée, l'utilisateur devrait pouvoir identifier les données personnelles mobilisées, les agents intervenus, les services tiers sollicités, les échanges réalisés ainsi que leur chronologie" (PDF p. 14). Such documentation also establishes a chain of responsibility in case of malfunction (PDF p. 14).
- Deletion: when a user deletes a sensitive file from a folder shared with an agent, it can be hard to ensure the data are gone from all agent memories (PDF pp. 8 to 9). Retention rules therefore have to cover agent memories.
- Guidelines of EDPB and Commission on the interplay of GDPR and AI Act are reported as being drafted and expected by the end of 2026 (PDF p. 13).

## Limits
- It is an exploratory note, not a CNIL recommendation or guideline. The CNIL page announces it as a joint reflection; the PDF itself names no authors and no CNIL deliberation.
- It is written from the perspective of individual users of consumer agents. Transfer to a company deploying agents on client data is the compiler's inference.
- It cites one incident (an agent deleting work mails) through a news report, which this summary did not read (PDF p. 10, footnote 13). French law references (Code civil) on liability do not apply in Austria (PDF p. 12).
