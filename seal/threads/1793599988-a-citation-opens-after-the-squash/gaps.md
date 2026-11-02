# Closing memo: 1793599988-a-citation-opens-after-the-squash

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over the tree at the phase's commit | the orchestrator, by `seal gate` once the review rounds settle |
| The tree case after `release/v0.28.1` is merged in, and any citation it refuses then (`frame/design.md` *Scope* item 6, `frame/questions.md` Q1) | the orchestrator, at that merge and before round 1 |
| The tree case on CI's checkout, where only the remote-tracking `main` and `release/*` refs stand | CI's `tests` workflow on the pull request |
| The module on the Windows leg, where paths are joined with a backslash | CI's Windows leg on the pull request |
| The exit-code half of the containment test working alone, apart from git printing no ref when `--contains` fails (`trail/phases/phase-1.md`, the eleventh mutant) | the proofer at review |

## Not done

The tree case keeps no floor on the number of citations it reads. A floor
written as a number is a count kept beside the tree, which
`skills/core/SKILL.md` *The rule a mechanism is kept against* refuses, and
the planted cases already hold the reader through the imported
`COMMIT_PATH`.

A work item's own `trail/` and `guarantee.md` are not read under "an
ancestor of HEAD". That is `frame/plan.md` A4, rejected for this item on
the grounds the plan gives.

The four open issues that cite the dead commit in their bodies were not
edited. A tree check reads no issue body, and the frame leaves them to the
orchestrator (`frame/design.md` *Scope*, out).
