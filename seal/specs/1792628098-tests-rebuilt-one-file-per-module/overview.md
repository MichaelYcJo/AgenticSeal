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
| the Windows fixes at 7efbd4c6 and 3e5cbb59, `tests/test_seal.py` at ef95b457, `tests/test_noninferiority.py` at 136c8923 and `tests/test_unverified_check.py` at b770ca64, run on macOS only | the orchestrator, on the next CI run's Windows legs |

## Not done

Phase 4 left seven survived mutations of `tests/conftest.py` helpers (h2, h4, h6, h12, h14, h21, h23). Each closes in the batch that rebuilds the module whose cases reach it; none closed with `broad_gate.py`, `seal_stamp.py`, the commit flow, `hooks/commit-review-gate.py`, `hooks/worktree-guard.py`, `chain_check.py`, `pact_check.py`, `hooks/root-migrate.py`, `seal.py`, `noninferiority.py` or `unverified_check.py`, as `phases/phase-5.md` says, so each is left to phase 6.

Phase 5 closed at b770ca64 with its eleven modules rebuilt, `skills/verify/scripts/broad_gate.py`, `skills/verify/scripts/seal_stamp.py`, the commit flow into `tests/e2e/commit/`, `hooks/commit-review-gate.py`, `hooks/worktree-guard.py`, `skills/code-review/scripts/chain_check.py`, `skills/verify/scripts/pact_check.py`, `hooks/root-migrate.py`, `skills/implement/scripts/seal.py`, `evals/scripts/noninferiority.py` and `skills/verify/scripts/unverified_check.py`. Phases 6 and 7 are not started.

`docs/one-root-by-lifetime.md` names the two old files of `seal.py` in its `check:` lines at 154 and 231, and `docs/one-root-by-lifetime.ko.md` at 149 and 220, for rules `tests/test_seal.py` now holds; each moves through the four `## Rule changes` items of `spec.md` the framer wrote at 93a009c6 (`phases/phase-5.md` *`skills/implement/scripts/seal.py`*).

`hooks/root-migrate.py#move` leaves an item's own directory on disk, empty, when it merges a directory holding a subdirectory into one that exists; git sees nothing there, and `specs/` then stays too. #942 changes no shipped code, so the new cases pin the behaviour as it is, and whether to repair it is the orchestrator's to place (`phases/phase-5.md` *`hooks/root-migrate.py`*).

## Fed back into the spec

Each clause below was written into the frame because the build had already done it. Each is inferred during implementation, and a planner may overturn it.

- `spec.md` *What holds the rules*: a call whose argument reads a name the case assigns or takes as a parameter is not compared at all (95e88420), and a call with no argument is not compared either (f74be021). Phases 1 to 4 built the first, round 1's fix pass at c6d2bfc4 replaced it with leaving out the one argument, which named 31 pairs, and c343efe9 reverted the fix pass on the orchestrator's ruling of 2026-10-22. 00674174 built the second on the orchestrator's ruling of the same day, after `--pairs` named `tests/test_seal_stamp.py::Test_build`'s two `build()` calls at 94660204. With both, `bin/test-layout --pairs` over `tests/` names 0 pairs.
- `spec.md` rule 2: the verdict `left for its module` (f74be021). The commit gate's three old files hold cases whose rows pin how `hooks/cmdline.py`, `hooks/one_heredoc.py` and `hooks/tokens.py` read a shape, and the build at 54c9e803 left each in its old file, rewritten without git where it ran the gate's `main`. The target's mutants cannot show that a sample of another module's rows protects what the rows did. `phases/phase-5.md` names each case.
- `spec.md` rule 1 and rule 4: where no case writes into the world beyond a marker keyed by a session id, each case makes its own session id and that is the reset, with no copy (f74be021). `tests/test_commit_review_gate.py` at 54c9e803 built it so, because a copy per case would cost each of 20 cases a copy of five directories and reset nothing.
- `plan.md` *Technical context* and *Alternatives considered*: whether the mutants are chosen before or after the old cases are read is not a rule the build is held to (f783cb2a). The plan said "The mutants are chosen before the old cases are read". Three phase 5 tables kept that order, `broad_gate.py`, `pact_check.py` and `hooks/root-migrate.py`, and seven chose after the old files or their cases were read: `seal_stamp.py`, `hooks/commit-review-gate.py`, `hooks/worktree-guard.py`, `chain_check.py`, `seal.py`, `noninferiority.py` and `unverified_check.py` (`phases/phase-5.md`, each module's *The mutation table*). Round 2 found the departure. It rebuilt twelve mutants from the tables' descriptions, eight of them from the seven modules, and each gave the verdict its table states. `CONTRIBUTING.md` *The test layout* drops the clause in phase 6's first step.
- `spec.md` *The proof of equal protection*: which columns the two tables of the earlier proof ran (f783cb2a). The spec said both tables ran "in both columns". `seal_stamp.py`'s did, and `broad_gate.py`'s old column ran for g1 to g9, for each mutant the new file first let survive and for g104, the rest stopped for time (`phases/phase-5.md` *`skills/verify/scripts/broad_gate.py`*). A mutant red against the new file needs no old verdict to meet the proof.
