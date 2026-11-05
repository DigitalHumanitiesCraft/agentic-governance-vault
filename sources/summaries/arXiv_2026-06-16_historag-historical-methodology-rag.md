# HistoRAG: Embedding Historical Methodology in Retrieval-Augmented Generation Through Critical Technical Practice (preprint, v1)

Publisher: Humboldt-Universität zu Berlin (Digital History), via arXiv
Date: 16 June 2026 (arXiv v1 stamp on PDF p. 1 and submission history; listed as companion preprint to a journal article under review)
Original: [arXiv_2026-06-16_historag-historical-methodology-rag.pdf](../arXiv_2026-06-16_historag-historical-methodology-rag.pdf)
Bindingness: Befund (preprint, not peer-reviewed)

## Core statement
The paper argues that standard retrieval-augmented generation is built for factual question answering and embeds assumptions that conflict with historical method (PDF p. 1). It proposes three design interventions, separated retrieval and analysis with an explicit user step between them, temporal windowing for balanced source samples, and an LLM-as-judge step that scores each source against researcher-defined criteria with a written justification, and tests them on 102,189 news magazine articles from 1950 to 1979 (PDF pp. 1, 5 to 8). LLM-generated syntheses are framed as Zwischentexte, interpretive proposals that a historian must verify, and the authors deliberately do not build an autonomous agent for the interpretive core of the work (PDF pp. 18 to 20).

## Relevance to the Leitfrage
### Client projects
The source says nothing specific on this field. The corpus is licensed by its publisher and not redistributed, so the code is open but the empirical results are reproducible only with corpus access (PDF p. 22).

### Research
- Agents and transparency: "Each decision an agent makes (to search this rather than that, to prioritise these results, to frame the synthesis in this way) is a decision the historian does not see, cannot evaluate, cannot contest." (PDF p. 20, section 7.2).
- Where autonomy fits: "For well-defined tasks with clear correctness criteria (formatting references, identifying duplicate documents, transcribing standardised forms) autonomous processing may be appropriate." For the interpretive core, "the historian must remain in the loop, not as a rubber stamp for machine decisions but as the locus of scholarly accountability." (PDF p. 20).
- Human step between finding and interpreting sources: "Transfer between phases requires an explicit user action", and the historian accepts, rejects or flags sources before any LLM interpretation (PDF pp. 5 to 6).
- Search bias: queries with 1970s vocabulary retrieved no chunks from the 1950s, and even a combined query under-retrieved the earliest five years; vocabulary choice becomes an invisible methodological decision (PDF p. 11). Keyword and semantic search surfaced largely disjoint sets of articles (PDF pp. 15 to 17).
- Provenance: "All retrieved chunks carry full provenance metadata" (title, date, issue, URL), so every passage stays traceable (PDF p. 10).
- Verification of generated text: the authors checked cited passages of the generated syntheses against the sources and note that "compelling narrative details are precisely where hallucination risk is highest." (PDF p. 18). The syntheses read a historical term through a present-day lens, which only the historian's context knowledge corrected (PDF pp. 18 to 19).
- Labelling: Zwischentexte "are labelled as machine-generated interpretive proposals, they carry source citations that can be verified" (PDF p. 19).
- Model dependence: four models ranked sources almost identically (correlations above 0.96 on 30 letters) but used different score scales, so "A filtering rule like "retain all sources scoring 7 or above" would yield dramatically different corpora depending on which model performed the evaluation." The authors suggest percentiles instead of absolute thresholds (PDF pp. 14 to 15).
- Candidate rule: in agent-supported source and literature work, the agent proposes and justifies, a person decides which sources enter the analysis, and every generated statement keeps a verifiable link to its source.

### Programming
- The framework separates a reusable core from a corpus-specific adapter and is released under MIT with archived, tagged releases; the paper names the embedding model and vector store versions used for its results (PDF pp. 9, 22).
- LLM-based relevance scoring should evaluate each item independently; batch evaluation led models to rank items against each other (PDF p. 8).

### Organisation
The source says nothing specific on this field. The authors name API cost and processing time as a sustainability question (PDF p. 20).

## Limits
- Preprint, single corpus, single language and one genre (reader letters); the cross-model comparison uses 30 items and is called indicative (PDF pp. 14, 20 to 21).
- No user study with practising historians (PDF p. 21).
- It concerns retrieval and synthesis over a fixed corpus, not agents with write access or tool use; its statement on agents is the authors' design position, not an empirical finding.
