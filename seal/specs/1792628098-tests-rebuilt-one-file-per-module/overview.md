# tests rebuilt one file per module (#942) — overview

## Why this work exists

The suite grew to 7,466 cases and four thousand Windows seconds in files named after scenarios, so a new case had no place to start from and a heavy file had no owner; each shipped module now has one test file that names it, held by a check, and the heaviest modules are rewritten to cost less while the mutation table shows they still protect what the old files did.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When `.test_durations` loses the removed ids | `spec.md` *Removes*: "pruned by the smith with one `Edit` per batch". Phases 3 and 5 left the removed ids priced | phase 7 prunes every batch's ids at once | `plan.md` phase 7 names the pruning and the refresh from CI; a refresh writes the file whole, so a per-batch prune is spent work. `test_the_durations_file_prices_the_suite` runs only over the whole collection, and the orchestrator's broad run is after phase 7 |
| Which old cases a batch A module takes | `spec.md` rule 2: "every old case that exercises the target gets one verdict". Phase 5 classified the cases of the files that price at 60 s or more | the light files that exercise a batch A module are left for phase 6 | `spec.md` rule 3 rewrites a module from the code only where its old files price at 60 s or more, and every other module's old cases are "placed and merged", which is batch B's rule; phase 6 places those cases into the file phase 5 wrote. `phases/phase-5.md` names each such file |
| What `--pairs` compares when an argument reads a local | `spec.md` rule 1 at 8aa42bf8: "leaving out an argument that reads a name the case assigns". Phases 1 to 4 left out the whole call; round 1's fix pass left out the argument alone at c6d2bfc4 | the whole call is left out, as phases 1 to 4 built it; the fix pass's rule is reverted in phase 5's first commit after 95e88420 | the fix pass's rule named 31 pairs at c6d2bfc4, 20 in `tests/test_broad_gate.py` and 11 in `tests/test_censuses.py`, most of them calls whose inputs are files on disk, and the orchestrator dropped it on 2026-10-22. 95e88420 wrote the frame to the whole call (`spec.md` *What holds the rules*, `plan.md` *Alternatives*). After the revert `bin/test-layout --pairs` over `tests/` names 0 pairs |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck at the work item's head | the orchestrator, through `broad-gate` after the review rounds settle |
| what the suite costs in CI minutes after the rebuild (`questions.md` Q5) | a measurement: the release table at the next release pull request |

## Not done

Phase 4 left seven survived mutations of `tests/conftest.py` helpers (h2, h4, h6, h12, h14, h21, h23). Each closes in the batch that rebuilds the module whose cases reach it; none closed with `broad_gate.py`, as `phases/phase-5.md` says.

Phase 5 rebuilt one of its eleven modules, `skills/verify/scripts/broad_gate.py`, before the spawn handed back. The other ten remain for the next phase 5 spawn: `seal_stamp.py`, the commit flow into `tests/e2e/commit/`, `hooks/commit-review-gate.py`, `hooks/worktree-guard.py`, `chain_check.py`, `pact_check.py`, `hooks/root-migrate.py`, `seal.py`, `evals/scripts/noninferiority.py` and `unverified_check.py`.

## Fed back into the spec

none
