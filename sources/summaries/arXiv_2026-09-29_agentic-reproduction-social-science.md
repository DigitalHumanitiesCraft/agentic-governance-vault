# Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results

Publisher: arXiv preprint (arXiv:2604.21965v2, cs.AI), authors from ETH Zurich, TU Wien and the Complexity Science Hub, and the University of Basel. The text states it is an extended version for social scientists of a computer science paper forthcoming at EMNLP (PDF p. 18).
Date: 29 September 2026 (arXiv stamp of version 2, PDF p. 1)
Original: [arXiv_2026-09-29_agentic-reproduction-social-science.pdf](../arXiv_2026-09-29_agentic-reproduction-social-science.pdf)
Bindingness: Befund (empirical finding)

## Core statement
The authors built a pipeline in which an agent re-implements the analyses of an empirical paper from a structured, number-free methods description plus the original data, without seeing the paper, the results or the original code. Outputs are compared cell by cell with the published tables, and an LLM-based step traces discrepancies to root causes (PDF pp. 1, 4-7). They tested four LLMs in four agent scaffolds (seven combinations) on 48 economics and political science papers that the Institute for Replication had verified as reproducible, with 222 tables and 14,214 cells (PDF pp. 7-8). Agents largely recovered published results. Coefficient signs agreed 85-91% of the time for the three best agents, and the best agent was within 1.96 original standard errors for over 80% of coefficients. Performance varied strongly by model, scaffold and paper (PDF p. 2). The paper is a preprint.

## Relevance to the Leitfrage

### Client projects
- The source says nothing specific on this field.

### Research
- Strict information isolation was used to keep agents from copying results. Agents worked in a workspace with only the task, the methods description, output templates and a data link, and were prohibited from reading the original package or fetching the paper through the web (PDF p. 6).
- Compliance with the isolation was checked by two audits, a deterministic scan of accessed paths and URLs and an LLM review of the run trace, with suspicious runs inspected manually and rerun on leakage. A separate hardcoding audit looked for statistical results written as numeric literals without a computation path from the data (PDF p. 6; Appendix B.3 and B.4, PDF pp. 45-46). The LLM review was described as over-inclusive (PDF pp. 45-46).
- Comparison was deterministic, by sign agreement, percentage difference and a letter grade per value, and avoided LLM judges for the scoring (PDF p. 6).
- Most failures traced to the papers (original errors or missing data) and, to a lesser extent, to agents. Higher-performing agents showed fewer human-attributed discrepancies, because they more often guessed the unstated choice correctly. The authors read underspecified methods as a main bottleneck for automated reproduction (PDF pp. 13-14, 16).
- The authors argue that code, not the paper text, is the authoritative record of what was done, and propose explicit alignment between narrative and code. They suggest automated reproduction as a diagnostic that exposes underspecification. This is the authors' interpretation (PDF pp. 16-17).
- The authors state that agents taking on more of the research process would require new criteria for scientific validity, including the reliability of conclusions generated without direct human oversight (PDF p. 17).
- Results were not fully stable. More than 80% of tables had a grade spread of at most one step across three runs, but 25-32% of matched coefficients differed between runs by more than 1.96 original standard errors, so fine comparisons between agents need caution (PDF p. 15).

### Programming
- Agent and scaffold choice mattered. GPT-5.4 in OpenCode was best, and the same model in the Codex CLI or mini-SWE-Agent scored worse. The best setup also used far more tokens, time and cost, so the authors say accuracy differences may partly reflect compute budgets (PDF pp. 2, 11-12).
- Agents produced one Python script per table, run in a sandbox, with traces and workspace contents kept for audit (PDF pp. 4, 6, 45).
- Reported scaling and unit problems (dollars against cents) produced many large deviations and were not accounted for by the comparison (PDF p. 10).

### Organisation
- The source says nothing specific on this field.

## Limits
- It is a preprint and the authors' own evaluation of their pipeline. The sample is 48 papers already verified as reproducible with data availability, from well-regarded journals, with original code in Stata (56.3%) and R (27.1%) and none in Python (PDF p. 7). Results may not transfer to unverified or poorly documented work.
- The study covers reproduction on the same data. It does not cover replication with new data, robustness analysis, or research without data access (PDF pp. 2, 17).
- Table extraction and the root-cause attribution rely on LLMs. A human audit confirmed 49 of 53 flagged divergences (92%) but only 33 of 49 error-source labels (67%), with 10 judged unsure, so attribution shares are indicative only (PDF p. 13). About 8% of tables were dropped due to extraction issues (PDF p. 5).
- Leakage was probed with a small test of ten Economic Journal papers before and after the models' knowledge cutoff, with no significant difference. The authors say this does not rule out leakage, including from post-training (PDF p. 16).
- Figure-level comparisons were left out of the core analysis because reliable vision-language checking is uncertain (PDF p. 5). Models and scaffolds named in the text are specific versions from 2026.
- Appendix pages beyond those cited (additional tables and prompts) were skimmed and not read in full.
