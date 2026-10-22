# tests rebuilt one file per module (#942) — overview

## Why this work exists

The suite grew to 7,466 cases and four thousand Windows seconds in files named after scenarios, so a new case had no place to start from and a heavy file had no owner; each shipped module now has one test file that names it, held by a check, and the heaviest modules are rewritten to cost less while the mutation table shows they still protect what the old files did.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When `.test_durations` loses the removed ids | `spec.md` *Removes*: "pruned by the smith with one `Edit` per batch". Phases 3 and 5 left the removed ids priced | phase 7 prunes every batch's ids at once | `plan.md` phase 7 names the pruning and the refresh from CI; a refresh writes the file whole, so a per-batch prune is spent work. `test_the_durations_file_prices_the_suite` runs only over the whole collection, and the orchestrator's broad run is after phase 7 |
| Which old cases a batch A module takes | `spec.md` rule 2: "every old case that exercises the target gets one verdict". Phase 5 classified the cases of the files that price at 60 s or more | the light files that exercise a batch A module are left for phase 6 | `spec.md` rule 3 rewrites a module from the code only where its old files price at 60 s or more, and every other module's old cases are "placed and merged", which is batch B's rule; phase 6 places those cases into the file phase 5 wrote. `phases/phase-5.md` names each such file |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck at the work item's head | the orchestrator, through `broad-gate` after the review rounds settle |
| what the suite costs in CI minutes after the rebuild (`questions.md` Q5) | a measurement: the release table at the next release pull request |

## Not done

Phase 4 left seven survived mutations of `tests/conftest.py` helpers (h2, h4, h6, h12, h14, h21, h23). Each closes in the batch that rebuilds the module whose cases reach it; `phases/phase-5.md` says which closed there.

## Fed back into the spec

none
