# How AI Impacts Skill Formation

Publisher: arXiv preprint (arXiv:2601.20245v2, cs.CY), by Judy Hanwen Shen (Anthropic Fellows Program) and Alex Tamkin (Anthropic)
Date: 1 February 2026 (arXiv stamp; the title page states February 3, 2026, PDF p. 1)
Original: [arXiv_2026-02-01_ai-impact-skill-formation.pdf](../arXiv_2026-02-01_ai-impact-skill-formation.pdf)
Bindingness: Befund (empirical finding)

## Core statement
The authors ran a pre-registered, between-subjects randomised experiment on learning a new Python library (Trio, asynchronous programming). 52 participants with more than one year of Python experience did two tasks, 26 with a chat-based AI assistant (GPT-4o) and 26 without, followed by a quiz without AI on debugging, code reading and conceptual understanding (PDF pp. 6-7, 9). The AI group scored about 17% lower on the quiz (Cohen's d = 0.738, p = 0.010), with no statistically significant gain in completion time (PDF pp. 2, 9-10). Screen recordings of 51 participants were coded into six AI interaction patterns, of which three preserved learning (PDF pp. 12-14).

## Relevance to the Leitfrage

### Client projects
- The source says nothing specific on this field.

### Research
- The authors speak of professional skill acquisition in general, motivated by supervising AI. They state that AI-enhanced productivity "is not a shortcut to competence" and should be adopted carefully to preserve skill formation, especially in safety-critical domains (PDF p. 1, abstract). The experiment covers programming only, so transfer to research skills such as literature work or statistics is an extrapolation.

### Programming
- Using AI impaired conceptual understanding, code reading and debugging. The largest gap was in debugging questions and the smallest in code reading (PDF p. 11). The authors point out that debugging and code reading are the skills needed to verify AI-written code (PDF p. 6).
- Learning-preserving patterns were conceptual inquiry only (n=7, 65% quiz score), generation followed by comprehension questions (n=2, 86%) and hybrid queries asking for code together with explanation (n=3, 68%) (PDF pp. 13-14).
- Low-scoring patterns were full delegation (n=4, 39%), progressive reliance (n=4, 35%) and iterative AI debugging (n=4, 24%). Delegation was the fastest at 19.5 minutes against 23 for the control group, and about 20% of the AI group used it (PDF pp. 13, 19).
- Participants who worked without AI met more errors (median 3 against 1) and resolved them themselves. The authors attribute part of the learning difference to this, which is an interpretation based on observation (PDF pp. 17-18).
- Speed gains were not significant on average. The authors explain this by time spent composing queries, and some participants spent up to 11 minutes on that (PDF pp. 9, 12, 14).
- The authors expect the effect to be at least as large with agentic tools, since these need even less human participation. This is an expectation, since the study used a chat assistant only (PDF p. 19).

### Organisation
- The paper says junior staff under time pressure may delegate to AI at the expense of skill development, and that companies shifting to AI-written code with human supervision may end up with humans unable to validate and debug it (PDF p. 19).
- The authors mention that learning or explanatory modes offered by AI services can support cognitive effort (PDF p. 20). A rule on when to use them is not derived in the paper.
- The study gives no tested organisational intervention. Suggestions such as requiring explanation alongside generation are inferences from the interaction patterns, not experimental results.

## Limits
- Authors are affiliated with an AI vendor (Anthropic Fellows Program and Anthropic), and the study used a competitor's model (GPT-4o) in a chat setting. The affiliation is stated on PDF p. 1.
- It is a preprint (version 2). The sample is small (n=52, qualitative groups of 2 to 7 people), the task lasted about one hour, and skill formation was measured by a quiz taken immediately afterwards, not over months (PDF p. 19).
- Participants were crowd workers paid a flat fee, with limited incentive to learn the library, and were instructed to finish as fast as possible (PDF pp. 9, 19).
- Pilot studies on another platform showed non-compliance with the no-AI condition (35% in one pilot). The main study used a platform with screen recording to verify compliance (PDF p. 8).
- Concept-area breakdowns and the six patterns come from exploratory, not pre-registered, analysis (PDF p. 11). The study has no human-tutor comparison and measures neither prompting skill nor long-run outcomes (PDF p. 19).
