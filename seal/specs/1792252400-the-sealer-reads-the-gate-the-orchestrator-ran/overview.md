# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — overview

<!-- The closing memo (implement skill, step 4). Opened at phase 1's divergence
and closed by phase 7. Only what the diff cannot show goes here. -->

## Why this work exists

The broad gate becomes the orchestrator's one command before the sealer is
spawned, so the sealer reads the record that run wrote and no longer runs it
a second time.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Which commit the sealer cases' `broad-gate.md` names (phase 1) | `plan.md` row 1: "naming `$build against $(git rev-parse main)` … so the run's SHA is followed by one records-only commit". `$build` is followed by two. The scaffold names the commit the records were written at, which one commit follows: the record's own | the stated property: one records-only commit | the row contradicts itself, and the property is the one `spec.md` §*The act, as this item leaves it* orders: the gate runs once the pull request body and `changelog.md` are written. Either reading passes `chain_check.broad_gate` (`phases/phase-1.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| The four regenerated sealer cases have not run on a model: no grader of `rule-sealer-no-gate` and no `shape-runs-no-broad-gate` has read a trace | the orchestrator, in phase 2's baseline side |

## Not done

| Item | Who must answer |
|---|---|
| T7, `noninferiority.py model` (S7), which phase 4 says phase 3's commit builds, was in neither phase-3 spawn and is not built (`phases/phase-3.md`) | the orchestrator, before phase 4 |
| *The sealer's two files* still names `broad-gate.md` as the sealer's (`chain_check.py#SEALERS_FILES` and its messages, `docs/the-review-record.md:251`), and `skills/verify/SKILL.md` §*Every agent seals what it verified* still calls the drawn stamp the sealer's seal | the orchestrator, with phase 5's word sweep |

## Fed back into the spec

none
