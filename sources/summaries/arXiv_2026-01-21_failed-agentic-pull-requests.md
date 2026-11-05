# Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub

Publisher: arXiv preprint (arXiv:2601.15195v1, cs.SE), authors from Drexel University and Missouri University of Science and Technology; formatted for MSR 2026 (Mining Software Repositories)
Date: 21 January 2026 (arXiv stamp, PDF p. 1)
Original: [arXiv_2026-01-21_failed-agentic-pull-requests.pdf](../arXiv_2026-01-21_failed-agentic-pull-requests.pdf)
Bindingness: Befund (empirical finding)

## Core statement
This is a mining study of 33,596 pull requests (PRs) authored by five coding agents (OpenAI Codex, Copilot, Devin, Cursor, Claude Code) on GitHub projects with more than 100 stars, taken from the AIDev-pop dataset (PDF pp. 1-3). The quantitative part compares merged and not-merged PRs on task type, size, CI results and review activity. The qualitative part codes the primary rejection reason of a stratified sample of 600 rejected PRs into a taxonomy (562 were still accessible). The authors report that documentation, CI and build tasks merge most often, performance and bug-fix tasks least often, and that the most frequent rejection pattern is that nobody reviewed the PR (PDF pp. 2-4). The paper is a preprint and a short five-page study.

## Relevance to the Leitfrage

### Client projects
- Where DHCraft agents contribute to a client's or third party's repository, the findings suggest following the project's contribution norms. Maintainers' comments ask for small, focused PRs limited to one coherent change (PDF p. 4).
- Licence and ownership problems appeared in a small number of rejections, with agents not meeting requirements such as signing a Contributor License Agreement. The authors read this as a legal and governance constraint that current agents cannot satisfy (4 PRs, PDF p. 4).
- Duplicate PRs were the most common reason for rejection among PRs that were actively reviewed (142 of 562, 23%), which indicates a need to check for existing work before opening a PR (PDF p. 4).

### Research
- The source says nothing specific on this field.

### Programming
- Not-merged PRs involve larger changes in lines and files, with small-to-medium effect sizes (Cliff's delta 0.17 for lines and 0.10 for files), and they more often fail CI (delta 0.24) (PDF p. 3).
- In the logistic regression each additional failed CI check lowers the odds of a merge by about 15% (PDF p. 4).
- Merge rates differ by task type. Across agents, documentation (84%), CI (79%) and build (74%) lead, and performance (55%) and fix (64%) trail (PDF p. 3). Merge rates also differ by agent, from 82.59% for Codex to 43.04% for Copilot (PDF p. 3). The authors do not control for differences in how the agents are used, so the agent ranking is descriptive.
- Code-level rejections were mostly CI or test failures (99 of 562, 17%), followed by incorrect (19) and incomplete (15) implementations (PDF p. 4).
- The conclusion recommends that agents validate submissions against CI before opening a PR and decompose tasks into localised changes (PDF p. 4).
- A small group of rejections (9) involved agents that repeatedly ignored or misread explicit reviewer instructions (PDF p. 4).

### Organisation
- Reviewer abandonment was the largest category (228 of 562, 38%): PRs closed with no meaningful human interaction. The authors take this as a sign of poor project coordination, and one implication is that agent output needs a named human reviewer who commits to responding (PDF pp. 2, 4). This implication is an interpretation and not a tested result.
- The authors frame failures as socio-technical, arising from misalignment with repository workflows, developer expectations and project coordination, and not only from technical defects (PDF pp. 2, 4).

## Limits
- It is an arXiv preprint. The dataset covers open-source projects with more than 100 stars and five specific agents, and may not transfer to private client repositories or to the current versions of these agents.
- Merge status is a proxy for quality. A PR may be closed for reasons unrelated to its content, and the study cannot say how many human-authored PRs fail for the same reasons, since there is no human baseline in this paper.
- The qualitative coding used two annotators with moderate agreement after round one (kappa 0.55) and strong agreement after refinement (0.91), applied to a sample of 100 PRs. The remaining 500 were coded independently, one annotator per PR, as the text describes (PDF p. 2).
- 38 sampled PRs were no longer accessible. Table 1 values for review-related variables were not statistically significant in the regression (PDF p. 3). The text read is short and gives few figures beyond those cited.
- The paper does not examine security, data protection or research settings.
