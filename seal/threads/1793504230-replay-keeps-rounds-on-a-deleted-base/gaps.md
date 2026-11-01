# Closing memo: 1793504230-replay-keeps-rounds-on-a-deleted-base

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set, `tests/evals/test_replay_targets.py` and `tests/evals/test_seed_defects.py`, and ran `ruff check` and `ruff format --check` on its changed files alone (contract rule 2) | the orchestrator, by `seal gate` after the review rounds settle |
| closed Whether the base taken from the landed commit is the base the review saw for `release/v0.25.2`'s one record. That release has no tag, so the `v<X.Y.Z>^2` comparison `frame/design.md` *Grounding* makes for the other 17 records cannot be made for it | answered by the proofer of round 1, from the branch's history on GitHub: `trail/rounds/round-1.md` *Confirmations*, the entry on this row |

## Not done

nothing
