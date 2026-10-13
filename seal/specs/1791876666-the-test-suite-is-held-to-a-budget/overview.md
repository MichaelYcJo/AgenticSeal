# 1791876666-the-test-suite-is-held-to-a-budget — overview

<!-- The closing memo (implement skill, step 4). Only what the diff cannot
show; each part written when it happened. Opened at phase 1. -->

📋 implement applied
· spec:     spec.md (Scope, The removal criterion, S1–S4, S6, Removes); plan.md (Technical context, phase 1, Test rows); questions.md Q4, Q6; docs/the-evidence-ledger.md §A released row is read again in the branch's fragment; templates/sdd-phase.md
· evidence: none committed yet: the G4 re-read row is in phases/phase-1.md and is written in phase 4
· verified: phases/phase-1.md, which labels each figure executed or read

## Why this work exists

The suite only grows, and a few files whose cases each spawn git and bash hold
most of its time. This work cuts those files by removals a mutation table
proves redundant, and lowers #930's budget rows to match.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| 191 parametrized ids of `test_s2_a_commit_bash_makes_into_an_undeclared_repository_does_not_land` removed, phase 1 | `spec.md` §Removes: "nothing — the frame names no unit … every removed function is a divergence row". The function stays; 191 of its 226 parameter rows leave | the removal | phase 1's mutation table: m1–m5 each still red after, and the counts of killers that are not S2 rows unchanged |
| S3 "the sample's rows all land in `main` or `u` without hooks" | read as true on every leg. On Windows `env -i` finds no git, and the `env -i` rows are the only S2 killers of m4 and m5 | two `env -i` rows kept, skipping on Windows by a named limit (`NO_GIT_UNDER_ENV_I`), as `stdbuf` already did; every other row fails rather than skips | the S9 case's own comment (#692's Windows pass) and `.test_durations`' low-band price of every `env -i` row |
| The battery, m1–m4 | `plan.md` names m1–m4; Q6 asks phase 1 to draw the battery from the docstrings | m1–m5: m5 breaks the stub's lease check (`hooks/githooks.py#_P2`), the shell half of the route m4 breaks in Python | Q6's default lets the work extend the battery |
| The ledger fragment's re-read row, owed by S6 when a cited case's text moves | not committed in phase 1 | written in phase 4, where `plan.md` puts the fragment | a fragment makes the records arm refuse six of `plan.md`'s names (phases/phase-1.md) |

## Not verified

| Item | Who must answer |
|---|---|
| Whether each of the 35 sampled rows lands in `main` or `u` without hooks on ubuntu-latest. Only macOS was executed, and Windows was read from `.test_durations`; G4 records 145 rows landing on Linux in 2026-10, not which ones | the pull request's ubuntu leg, read by the orchestrator: a vacuous row there fails S2 by name |
| The phase-1 file's Windows seconds after the sample (Q4) | #931's next refresh, or a `workflow_dispatch` of `test.yml` on the branch |

## Not done

The `slow-file` row is not lowered, because #930's `seal/budgets.md` is not on
this branch. The figures wait in `phases/phase-1.md`, and the later of the two
pull requests lowers the row.

## Fed back into the spec

none
