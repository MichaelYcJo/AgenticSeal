# tests rebuilt one file per module (#942) — overview

## Why this work exists

The suite grew to 7,466 cases and four thousand Windows seconds in files named after scenarios, so a new case had no place to start from and a heavy file had no owner; each shipped module now has one test file that names it, held by a check, and the heaviest modules are rewritten to cost less while the mutation table shows they still protect what the old files did.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When `.test_durations` loses the removed ids | `spec.md` *Removes*: "pruned by the smith with one `Edit` per batch". Phases 3 and 5 left the removed ids priced | phase 7 prunes every batch's ids at once | `plan.md` phase 7 names the pruning and the refresh from CI; a refresh writes the file whole, so a per-batch prune is spent work. `test_the_durations_file_prices_the_suite` runs only over the whole collection, and the orchestrator's broad run is after phase 7 |
| Which old cases a batch A module takes | `spec.md` rule 2: "every old case that exercises the target gets one verdict". Phase 5 classified the cases of the files that price at 60 s or more | the light files that exercise a batch A module are left for phase 6 | `spec.md` rule 3 rewrites a module from the code only where its old files price at 60 s or more, and every other module's old cases are "placed and merged", which is batch B's rule; phase 6 places those cases into the file phase 5 wrote. `phases/phase-5.md` names each such file |
| What `--pairs` compares when an argument reads a local, and when a call has no argument | `spec.md` rule 1 at 8aa42bf8: "leaving out an argument that reads a name the case assigns". Phases 1 to 4 left out the whole call; round 1's fix pass left out the argument alone at c6d2bfc4. `spec.md` *What holds the rules* names no rule for a call with no argument, and at 94660204 `--pairs` named `tests/test_seal_stamp.py::Test_build`'s two `build()` calls as a pair | the whole call is left out, as phases 1 to 4 built it; the fix pass's rule is reverted at c343efe9. A call with no argument is not compared either, from phase 5's third spawn on | the fix pass's rule named 31 pairs at c6d2bfc4, 20 in `tests/test_broad_gate.py` and 11 in `tests/test_censuses.py`, most of them calls whose inputs are files on disk, and the orchestrator dropped it on 2026-10-22. 95e88420 wrote the frame to the whole call (`spec.md` *What holds the rules*, `plan.md` *Alternatives*). Any two calls with no argument compare equal, so such a pair says nothing about the two cases, and the orchestrator ruled on 2026-10-22 that such a call is not compared. With that rule `bin/test-layout --pairs` over `tests/` names 0 pairs. The framer writes the sentence into `spec.md` *What holds the rules* |
| Which old cases a module takes when a case's rows pin another module's reading | `spec.md` rule 2: "every old case that exercises the target gets one verdict", one of place, merge, cut, rewrite and to #923. The commit gate's three old files hold cases whose rows pin how `hooks/cmdline.py`, `hooks/one_heredoc.py` and `hooks/tokens.py` read a shape | such a case stays in its old file, rewritten in place without git where it ran the gate's `main`, for the phase that rebuilds the module it pins | the proof's mutants are the target's alone, so they cannot show that a sample of another module's rows protects what the rows did. The rows run no git and the three files now run in 2.1 s. `phases/phase-5.md` names each case |
| How a module's world is reset between cases | `spec.md` rule 1: "built once per module by a module-scoped fixture and copied for each case; the copy is the reset". `tests/test_commit_review_gate.py` never copies its world | the session id is the reset | no case writes into the world but the gate's choice marker, keyed by a session id each case makes its own. A copy per case would cost each of 20 cases a copy of five directories and reset nothing |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck at the work item's head | the orchestrator, through `broad-gate` after the review rounds settle |
| what the suite costs in CI minutes after the rebuild (`questions.md` Q5) | a measurement: the release table at the next release pull request |
| the Windows fixes at 7efbd4c6 and 3e5cbb59, `tests/test_seal.py` at ef95b457, `tests/test_noninferiority.py` at 136c8923 and `tests/test_unverified_check.py` at b770ca64, run on macOS only | the orchestrator, on the next CI run's Windows legs |

## Not done

Phase 4 left seven survived mutations of `tests/conftest.py` helpers (h2, h4, h6, h12, h14, h21, h23). Each closes in the batch that rebuilds the module whose cases reach it; none closed with `broad_gate.py`, `seal_stamp.py`, the commit flow, `hooks/commit-review-gate.py`, `hooks/worktree-guard.py`, `chain_check.py`, `pact_check.py`, `hooks/root-migrate.py`, `seal.py`, `noninferiority.py` or `unverified_check.py`, as `phases/phase-5.md` says, so each is left to phase 6.

Phase 5 closed at b770ca64 with its eleven modules rebuilt, `skills/verify/scripts/broad_gate.py`, `skills/verify/scripts/seal_stamp.py`, the commit flow into `tests/e2e/commit/`, `hooks/commit-review-gate.py`, `hooks/worktree-guard.py`, `skills/code-review/scripts/chain_check.py`, `skills/verify/scripts/pact_check.py`, `hooks/root-migrate.py`, `skills/implement/scripts/seal.py`, `evals/scripts/noninferiority.py` and `skills/verify/scripts/unverified_check.py`. Phases 6 and 7 are not started.

`docs/one-root-by-lifetime.md` names the two old files of `seal.py` in its `check:` lines at 154 and 231, and `docs/one-root-by-lifetime.ko.md` at 149 and 220, for rules `tests/test_seal.py` now holds; each moves through a `## Rule changes` item the framer writes (`phases/phase-5.md` *`skills/implement/scripts/seal.py`*).

`hooks/root-migrate.py#move` leaves an item's own directory on disk, empty, when it merges a directory holding a subdirectory into one that exists; git sees nothing there, and `specs/` then stays too. #942 changes no shipped code, so the new cases pin the behaviour as it is, and whether to repair it is the orchestrator's to place (`phases/phase-5.md` *`hooks/root-migrate.py`*).

## Fed back into the spec

none
