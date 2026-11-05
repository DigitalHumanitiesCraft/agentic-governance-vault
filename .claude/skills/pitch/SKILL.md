---
name: pitch
description: Turns a source-backed knowledge base into a short pitch of at most five slides for an organisation, first as an outline with sources in the chat and only after approval as a PowerPoint deck. Triggers on "Pitch aus der Wissensbasis", "Folien aus der Wissensbasis", "mach einen Pitch daraus", "Wissen in die Organisation tragen", "Präsentation für die Eigentümer". Not for building the knowledge base itself (source-backed-governance) and not for slides without a cited knowledge base.
---

# Pitch from the knowledge base

Carries the answer of a knowledge base into the organisation as a pitch of at most five slides. Every statement on a slide rests on a stored original in `sources/` with its locator. The person steers at the gates marked below. Never pass a gate without their answer, and never create a deck file before gate 4.

The knowledge base follows the conventions of the `source-backed-governance` skill: `knowledge/project.md` holds the Leitfrage with fields and goals, the claim documents cite `../sources/` with locators, and `sources/summaries/` holds one summary per original. Citation format, locators and statuses are those of its `references/conventions.md`; this skill does not repeat them.

## Procedure

1. Transfer to the organisation. Ask at most three questions, in one message: who the audience is and what they decide, what the pitch should achieve (inform, win approval, prepare a decision), and the setting (length, live or sent ahead). Take what `project.md` and the claim documents already answer instead of asking. Gate: answers.
2. Leitfrage. Propose the question the pitch answers, normally the Leitfrage from `project.md` narrowed to the audience, or up to three alternatives when the audience needs a different cut. Recommend one. Gate: choice.
3. Outline in the chat. Write the outline into `knowledge/<name>-gliederung.md` and show it in full in the chat:
   - at most five slides, each with a title, two to four statements and a short speaker note;
   - each statement taken only from `knowledge/` and `sources/`, with its status and a citation to the original with locator, never to a summary;
   - the preamble states that the outline awaits approval and that no deck exists yet;
   - speaker notes in block quotes, and what the organisation decides for itself or what does not fit in a final section "Offene Punkte".
   Verify every cited locator against the original before showing the outline: `pdftotext -enc UTF-8 -layout -f N -l N` for a PDF page, the cited heading in a stored `.md` source. Run the knowledge check of the vault (`check_kb.py`) until it reports 0 problems. Where the base holds nothing for a statement the person wants, say so and leave it out or propose research through `source-backed-governance`.
4. Approval gate. The person approves the text of every slide in the chat. Revise the outline file and show the changed slides again until each one is approved. Slide text enters the deck only after this approval, and later changes to slide text go through the chat again before they enter the deck.
5. Slides. Generate the deck from the approved outline only:
   - with the installed `dhcraft-pptx` skill when it is available, which brings the corporate design, a reproducible generator and its review steps;
   - otherwise with a single-file `python-pptx` generator script in `scripts/`, which reads nothing but the approved outline and writes to `output/`.
   Put the citations on each slide as a short source line and the speaker notes into the notes field. Render every slide to an image and look at it before showing the deck.
6. Design feedback. Show the rendered slides and ask for one round of design feedback (layout, emphasis, images). Apply it to the generator, rebuild and render again. Text changes from this round return to step 4.

## Verification

- `check_kb.py` reports 0 problems with the outline in `knowledge/`, and the vault check accepts its frontmatter.
- Every citation on a slide matches a citation in the approved outline.
- The deck has at most five content slides and contains no statement absent from the approved outline.
- Report which steps ran, which renders were inspected, and what is still open.

## Boundaries

- The outline and the deck carry no claims beyond the sources; a meeting, mail or personal note is no source.
- Legal assessments carry the note that they are no legal advice, as the governance draft does.
- The deck file is a generated artefact in `output/` and is not committed.
