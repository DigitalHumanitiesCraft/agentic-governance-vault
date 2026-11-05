# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

Publisher: arXiv preprint (arXiv:2602.11988v3, cs.SE), authors from ETH Zurich and LogicStar.ai; marked "Preprint" (PDF p. 1)
Date: 29 September 2026 (arXiv stamp of version 3, PDF p. 1)
Original: [arXiv_2026-09-29_agents-md-context-files.pdf](../arXiv_2026-09-29_agents-md-context-files.pdf)
Bindingness: Befund (empirical finding)

## Core statement
The study tests whether repository context files such as AGENTS.md or CLAUDE.md help coding agents resolve real tasks. It uses 300 SWE-bench Lite tasks from 11 popular Python repositories with LLM-generated context files, and a new benchmark, CtxBench, of 138 instances from 12 niche Python repositories that contain developer-written context files (PDF pp. 2, 5). Four agent and model pairs were tested (Claude Code with Sonnet 4.5, Codex with GPT-5.2 and GPT-5.1 Mini, Qwen Code with Qwen3-30B) in settings with no file, an LLM-generated file and a developer-written file, each sampled once (PDF p. 5). The result is that context files did not significantly change the success rate but raised cost and steps, by about 20% on average for LLM-generated files (PDF p. 6).

## Relevance to the Leitfrage

### Client projects
- The source says nothing specific on this field.

### Research
- The source says nothing specific on this field.

### Programming
- LLM-generated context files lowered resolution rates in 5 of 8 settings, by 0.5% on SWE-bench and 2% on CtxBench on average, and the changes were not significant (p = 0.87 and 0.37). They raised cost by 20% and 23% and added steps (PDF p. 6).
- Developer-written files improved performance by 2.4% on average (p = 0.21, not significant). They outperformed LLM-generated files with p = 0.038, and raised cost by up to 19% (PDF p. 6). The introduction states a 7% margin for developer-written over LLM-generated files, which does not match these figures directly, and the difference could not be reconciled from the text read (PDF p. 2).
- Agents follow instructions in context files. Named tools were used 1.6 times per instance (uv) and 2.5 times (repository-specific tools) when mentioned, against almost never when not, and context files led to more testing, searching and file reading (PDF p. 8). The authors link the extra cost to this obedience and to additional reasoning tokens (PDF p. 8).
- Repository overviews did not help agents reach the relevant files faster (PDF p. 7).
- The authors conclude that context files should be omitted when LLM-generated, and that human-written ones should contain only instructions missing from the README, such as specific conventions or non-functional requirements, and be evaluated before adoption (PDF p. 2). This is the authors' recommendation, resting on the benchmark results.
- When all documentation files were removed from the repository, LLM-generated context files improved success by 2.7% on average and beat developer-written ones. The authors read this as redundancy with existing documentation (PDF p. 16).
- Stronger models did not write better context files, and the prompt used to generate the files made no consistent difference (PDF pp. 8-9). File length showed no clear effect (PDF p. 16).

### Organisation
- The source says nothing specific on this field. A general point is that the authors treat agent-developer recommendations as claims to be tested, and say any attempt to improve performance should be rigorously evaluated before deployment (PDF p. 1, abstract).

## Limits
- It is a preprint (version 3). Authors include employees of LogicStar.ai, a company active in agent tooling, and the text does not discuss this.
- Only Python repositories were studied. The authors note that models may already know Python tooling, which could reduce the value of context files (PDF p. 9).
- Success is measured by passing tests only. Code quality, efficiency and security are not measured, and the authors name them as open (PDF p. 9).
- CtxBench relies on LLM agents to build environments, task descriptions and tests, with manual review of the tests and inspection of all instances (PDF pp. 4-5). Each agent was sampled once, with confidence reported through significance tests (PDF pp. 5-6).
- Results are not statistically significant for most success-rate comparisons, so the claim is "no demonstrated improvement" and not "harm".
- The study does not address rules files used for safety, compliance or style enforcement, since it measures only task resolution.
