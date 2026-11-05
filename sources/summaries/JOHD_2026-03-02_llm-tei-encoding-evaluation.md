# A Multi-Dimensional Evaluation Framework for Assessing LLM Performance in TEI Encoding

Publisher: Journal of Open Humanities Data (Ubiquity Press), volume 12, article 39; single author from the Department of Digital Humanities, University of Graz
Date: 2 March 2026 (publication date stated on PDF p. 20; submitted 18 November 2025, accepted 19 January 2026)
Original: [JOHD_2026-03-02_llm-tei-encoding-evaluation.pdf](../JOHD_2026-03-02_llm-tei-encoding-evaluation.pdf)
Bindingness: Befund (peer-reviewed discussion paper with an empirical case study; the journal states it is peer-reviewed, PDF p. 20)

## Core statement
The paper builds a stratified evaluation framework for TEI XML that LLMs generate from plain-text transcriptions, and tests it on 100 letters of a multilingual 18th and 19th century correspondence with two proprietary and two open-weight models (PDF pp. 1, 3, 9 to 10). It separates dimensions that can be checked automatically (well-formedness, source fidelity as string comparison, schema validity) from those that need reference encodings or human review (structure, semantic accuracy) (PDF p. 4). The best models reach composite scores of about 92 to 94 percent, yet the author concludes that current LLMs are "not yet reliable as autonomous encoders for scholarly editions" (PDF pp. 16, 18).

## Relevance to the Leitfrage
### Client projects
- For edition projects, the paper names the practical question it answers: without assessment frameworks, DH projects cannot tell whether LLM assistance brings productivity gains or unacceptable quality risks (PDF p. 3).
- The choice of open-weight, locally run models is motivated by budget, data privacy requirements and institutional policies that may preclude proprietary APIs; a quantised local model was competitive with proprietary ones on this task (PDF pp. 10, 12).

### Research
- LLMs exhibit behaviours that conflict with editorial principles, among them "the normalisation of historical spelling through adaptation to modern orthography and the insertion of plausible, yet fictitious text", which compromises source fidelity (PDF p. 2).
- "Preserving input text is critical for scholarly editions, where historical orthography constitutes research data that LLMs often misinterpret as errors requiring correction." Even similarity scores of 98 to 99 percent may hide critical alterations (PDF p. 5).
- High aggregate scores are misleading: "even scores exceeding 90% can demand substantial post-processing for reference quality." (PDF p. 16).
- Some errors are systematic and correctable by script, others sporadic: for two models, "sporadic character-level substitutions and content insertions require case-by-case verification, resisting automated post-processing." (PDF p. 16).
- Semantic appropriateness and interpretive boundaries cannot be detected by automated metrics and need human-in-the-loop review (PDF pp. 6, 16).
- The study records model versions, prompt templates and outputs in a public dataset to make the evaluation reproducible (PDF pp. 8 to 10), and names missing repeated runs as a limitation, because stochastic variation may explain apparent improvements (PDF p. 18).
- Candidate rule: before agent-generated encoding enters an edition, an automated character-level comparison with the source transcription runs on every file, and every deviation is checked by a person.

### Programming
- The framework itself is a model for a check pipeline: XML parser for well-formedness, normalised string comparison for source fidelity, RelaxNG validation for schema compliance, released as MIT-licensed code (PDF pp. 4 to 5, 8). Schema validity is "necessary but insufficient" for encoding quality (PDF p. 5).
- Few-shot examples improved schema adherence more than detailed rules for some models (PDF p. 12).

### Organisation
The source says nothing specific on this field.

## Limits
- One corpus, one genre (letters), single-encoder reference annotations, and no repeated runs (PDF pp. 16, 18).
- It evaluates LLM text-to-TEI conversion, not autonomous agents with tool access.
- The author and DHCraft's operator work in the same Graz Digital Humanities context, and the paper cites earlier work co-authored by the operator (PDF pp. 2, 19 to 20). The findings are used here for what the text reports, not for the framing.
