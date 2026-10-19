# 1792368014-the-framer-is-written-anew-from-its-job — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

## Why this work exists

The framer's definition is written to the shape the smith and the warden
already have and preloads the contract alone, so a framer spawn carries
26,027 bytes at startup instead of 86,353 and opens the two skills by
section at the steps that need them.

## Where spec and implementation diverged

Opened at phase 1. Each row is one divergence; `phases/phase-1.md` holds the
detail.

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Removals `## Removes` did not name (phase 1) | `## Removes` names the sections and sentences that leave `agents/framer.md`; phase 1 also removed the clause *`sealer` runs the broad gate over what is left*, the paragraph saying `smith` reads narrowly by comparison, the #263 reading under the reading list, the paragraph on what a mark is worth (`hooks/implementer.py`), the sentence keeping the two utility skills off the `skills:` list (#292), and the section *The frame is a drawing, and a phase prompt points at a row* | removed | the first is false since #969 moved the broad gate to the orchestrator; the rest are narration or address the orchestrator, and `spec.md` §*Data & interfaces* lists every section the new file keeps. The #292 reason stands in `tests/test_chain_hooks_hardening.py`'s comment above `UTILITY_SKILLS` |
| The README skills row and its count check (phase 1) | `## Removes` names the framer's row in each README edition; the skills row of each said *the four the agents follow from their first tool call are in the column to the left*, which the rewrite makes false | both rows now say two are preloaded and fourteen are loaded on demand, `implement` and `writing-style` in the list; `tests/test_chain_hooks_hardening.py::test_the_readme_group_counts_are_derived_too` gained the spellings for 2 and 14 | that case derives each group from the `skills:` lists and went red on the rewrite with *the `preloaded` group holds 2 skills and no spelling is recorded -- add it rather than loosening the check* |
| Two citations in `skills/implement/orchestration.md` (phase 1) | the frame does not name the file; `:381` cited the framer's `## When you run` and `:416` its §*You have no interactive phase*, both sections the rewrite removes | re-pointed to `## Job` and the rule *You ask nobody anything* | contract §19: a change corrects what stood on the old fact in the same commit. The lines are outside the ranges #943 and #976 edit (`spec.md` §*The read set after the rewrite*) |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck on this branch | the orchestrator's broad gate, after the review rounds settle |
| the framer's eval side on the rewritten tree (S3, S9, S10) | phase 2, which the orchestrator schedules after #976 and #985 merge (`questions.md` Q2) |

## Not done

Nothing in phase 1.

## Fed back into the spec

None.
