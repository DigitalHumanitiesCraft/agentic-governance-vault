# Vibe check: AI may replace SaaS (but not for a while)

Publisher: National Cyber Security Centre (NCSC-UK), blog post by its CTO for Architecture
Date: 24 March 2026 (as stated on the page)
Original: [NCSC-UK_2026-03-24_vibe-check-ai-may-replace-saas.md](../NCSC-UK_2026-03-24_vibe-check-ai-may-replace-saas.md)
Bindingness: Empfehlung in form (blog post of an authority, an opinion piece rather than formal advice), but rules drawn from it are Ableitung

## Core statement
The post argues that AI-written code ("vibe coding") lowers the cost of bespoke software, so that organisations will increasingly build instead of buying software as a service, and that security professionals should shape this shift now (sections "The promise of vibe coding" and "Getting security a seat at the table"). It states that a blanket rule of human review of all AI-written code is already under strain and lists safeguards: secure-by-default models, confidence in model provenance, AI-assisted review, and deterministic controls that limit what code can do even if it is unsafe. It concludes that the current risks are likely far outside most organisations' risk tolerances (section "The vibe future?").

## Relevance to the Leitfrage

### Client projects
- Adoption will spread along three dimensions: how complex the service is, how important it is and how risk averse the organisation is (section "The promise of vibe coding"). This supports scaling review effort to the criticality of a client service. The scaling rule is an inference from the source.

### Research
- The source says nothing specific on this field.

### Programming
- Vibe coding is defined as "Using AI to write code, often without human review" (section "The promise of vibe coding").
- The post names model provenance as a safeguard: "We need to be able to have confidence in the model provenance, and be able to trust and verify that it has not been developed in a way to maliciously introduce issues in code it produces." (section "Getting security a seat at the table").
- It calls for "a deterministic architecture (that is, known controls implemented in rules and code, rather than expecting an AI to limit another AI)" to limit what code can do even if it is malicious, compromised or unsafe (same section).
- It cites one large organisation that requires even the smallest AI-built project to have test coverage, automated security testing and documentation comparable to critical software (same section).
- It lists slopsquatting among current problems of vibe coding (section "The promise of vibe coding").

### Organisation
- "A mitigation that’s sometimes suggested is that organisations will simply say 'all code written by AI must be reviewed by a human’. But already that guidance is creaking at the seams for organisations that want to build aggressively." (section "The promise of vibe coding"). The author expects AI-written code nobody has reviewed in production within five years.
- "Currently, there are risks that are likely far outside most organisations' risk tolerances." (section "The vibe future?"). The post explicitly does not advocate vibe coding.

## Limits
- It is a personal-voice blog post with forecasts, not guidance with tested controls. Rules drawn from it are Ableitung at most, and its safeguards are framed as research needs ("Some safeguards are obvious").
- It does not say how to establish model provenance or which models to trust.
- Its audience is large organisations and the public sector; its scenario of replacing SaaS with self-built tools only partly matches DHCraft's project work.
