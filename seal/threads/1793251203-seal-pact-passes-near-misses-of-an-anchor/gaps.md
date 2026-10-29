# Closing memo: 1793251203-seal-pact-passes-near-misses-of-an-anchor

## Why this work exists

`seal pact` read a near miss of a pact anchor as no anchor, so a signer
whose anchors stood under a header in another case or in bold, named an
undeclared remote, or used the old inline token in capitals was reported as
citing nothing. A header that means the anchor header is now read as one,
an undeclared remote is refused at its line, and the shapes the
normalisation leaves out are the proofer's judgment.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| S5 of the first frame | `frame/plan.md` phase 1: seen red against `28edee12` / shown red by `seal mutate` on the scan's guard, and later removed with the scan | the mutation, then removal | `trail/phases/phase-1.md` *What this phase found*; the reframe after round 4 |
| The emphasis run's guards | `frame/design.md`: no space inside the run, no nesting, no escape / the guards removed | removed | `trail/phases/phase-3.md`: a key equals an anchor word only when the wrapped text is the word, so no guard changed a decision and each mutant stayed green; `CLAUDE.md` *The rule a mechanism is kept against* |
| The proofer's text | `frame/plan.md` phase 4: one sentence / three sentences | three | `trail/phases/phase-4.md`: one sentence broke `skills/writing-style/SKILL.md` *English prose rules* |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the orchestrator, through `seal gate` |

## Not done

**A run of four or more emphasis characters is outside the normalisation,
and no case pins it.** `****Pact****` is not read as the anchor header, and
widening the run to four would pass every case (`trail/phases/phase-3.md`,
read). The orchestrator judged it a limit and sent nothing back to the
framer: the normalisation is closed at what renders as emphasis a person
writes, and a run of four is written by nobody. Source: `CLAUDE.md` *The
first value: efficient development through the workflow*, judgment spent
where meaning is the question; the proofer's sentence covers such a header
as a shape the normalisation leaves out.

**The walker's own over-refusal stays.** An anchor table, a blank line, then
an indented code block whose line is written `| ... |` is refused by
`hooks/lib/config.py#gfm_table` as a row the walk never reaches, though
GitHub renders the line as code (`trail/phases/phase-1.md`, the walker
limit). It predates this work and the plan does not edit the walker.

## Fed back into the design

none
