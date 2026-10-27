# Review round 3: 1793057294-close-the-mutation-gaps-the-old-tests-had

target: 7761b95c, fixes 88c27ed5..7761b95c

This is a verifying round for a failure the pull request's CI found after
the sealer sealed at af4cb419. The `tests` run 40446828473 is the first run
of the `pull_request` event on #1057, at 88c27ed5. It failed on the ubuntu,
macOS and Windows legs. Each failed leg failed the same three cases, which
phase 5 added to `tests/test_chain_check.py` *Test_declared_for_this_branch*.
The ubuntu leg runs the whole suite in one job, and it printed 3 failed,
6,740 passed and 17 skipped. This round read that log through
`gh run view 40446828473 --log-failed`.

The round read `git diff 88c27ed5..7761b95c` whole. It touches three paths.
The first is `tests/test_chain_check.py`, at 516d0ff6. The other two are
records of the work item, `phases/phase-7.md` and `overview.md`, at 7761b95c.
The round ran its probes in a `git clone --no-local` of the worktree, kept in
the round's scratch directory. No `seal/parity.md` is declared, so no parity
comparison applies. Round 2 opened no finding, so no close is owed an answer
this round.

Carried from rounds 1 and 2 as coordinates, not as verdicts: the work item's
32 changed test files, from `git diff --name-only 5daa931f...HEAD -- tests`,
and the counts of lines holding `def test_`. This round re-ran both at the
head. The 32 files are unchanged. The counts still read 169 added over
`5daa931f...HEAD` and 182 over `134d7203..HEAD`, with none removed. The fix
range adds one such line and removes one, because it rewraps the signature
of one case.

The smith claimed three things. The first is that the three cases called
`chain.declared_for_this_branch` in the test process without clearing
`GITHUB_HEAD_REF`. The second is that 516d0ff6 clears the variable as the
file's other cases do, and was seen red with the variable set and green
after. The third is that a sweep of the 32 files under a `pull_request`
environment found no other case failing this way. Each claim is judged
under the confirmations below.

## Findings

No finding opened this round.

## Confirmations

confirms: none
The fix at 516d0ff6 holds. Each of the three cases now calls
`monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)` after the fixture's
commit and before the call (`tests/test_chain_check.py:2865` and `:2881`).
The parametrised case takes `monkeypatch` in its signature, which covers both
of its parameters. This round ran the class with
`GITHUB_HEAD_REF=some-other-branch` set. At 88c27ed5 it printed 3 failed and
6 passed, and the three failures were these cases. At 7761b95c it printed 9
passed. Between 516d0ff6 and 7761b95c only records change, so the green run
also holds for 516d0ff6. The pull request's own `tests` run 40447728522 at
7761b95c passed every leg: ubuntu, the three macOS groups and the four
Windows groups. Its ubuntu leg printed 6,743 passed and 17 skipped, which is
the 6,740 of the failed run plus the three cases. Executed with the two class
runs, read for run 40447728522 through `gh run view`.

confirms: none
The cause holds as `phases/phase-7.md` states it.
`skills/code-review/scripts/chain_check.py:2005` takes `GITHUB_HEAD_REF`
before the checked-out branch. The failed run's assertion text names
`test/1017-close-the-mutation-gaps-the-old-tests-had`, the branch under
review, where the fixture's branch is `feature`. The record's run facts also
hold. Run 40446828473 is `pull_request` at 88c27ed5, and run 40444267960 is
`workflow_dispatch` at bf2096ba. Executed with `gh run view --json
event,headSha` for both runs.

confirms: none
The class of the defect is enumerated, as contract rule 12 asks. The tests
call `declared_for_this_branch` directly in three places,
`tests/test_chain_check.py:2866`, `:2882` and `:2897`, and all three now
clear the variable. Every other test reaches the function through
`chain.main` (`chain_check.py:2176`). That happens only in
`tests/test_chain_check.py`, directly or through `chain_check_run`
(`tests/conftest.py:1495`). There the fixtures and helpers remove the
variable or set their own value: `event` at `:238-246`, the fixture at
`:2315-2316`, and `run_check` at `:2772-2775`. Executed with `git grep` for
the function and for `chain.main(` and `chain_check_run` across `tests/`.

confirms: none
The sweep's conclusion holds, but the sweep did not set every variable the
code reads. Shipped Python reads five `GITHUB_` variables. The sweep set two
of them, `GITHUB_HEAD_REF` and `GITHUB_ACTIONS`
(`skills/verify/scripts/unverified_check.py:1444`). It did not set the other
three:

- `GITHUB_EVENT_PATH`, read at `skills/code-review/scripts/chain_check.py:758`
  and `:769`. A `pull_request` run points it at a payload naming the pull
  request.
- `GITHUB_OUTPUT`, read at `.github/scripts/publish_release_note.py:439`.
- `GITHUB_STEP_SUMMARY`, read at `.github/scripts/durations_union.py:181`
  through its `env` argument.

No changed test file names `publish_release_note` or `durations_union`, so
only `GITHUB_EVENT_PATH` could reach one of the 32 files. Its readers are
reached from `tests/test_chain_check.py` and `tests/test_broad_gate.py`.
Each of those files' cases sets the variable to its own payload or removes
it: `tests/test_broad_gate.py:75` lists it in `AMBIENT`, which `:154-159`
removes. This round ran both files under the sweep's six variables, with
`GITHUB_EVENT_PATH` pointing at a payload for a ready pull request and with
`GITHUB_OUTPUT` and `GITHUB_STEP_SUMMARY` set. It printed 568 passed and 1
skipped, exit 0. The `pull_request` runs themselves set every variable the
event sets. At 88c27ed5 the ubuntu leg failed only the three cases, and at
7761b95c every leg passed. So the closing sentence of `phases/phase-7.md`,
"No other case read the run's environment", is true. It rests on those runs
and on this reading, not on the sweep alone. The `overview.md` row says
"under that environment set by hand", and that means the six variables
phase 7 names. That is no finding, because phase 7 names the six exactly and
the conclusion holds. Executed with the probe and `git grep -nE
'(GITHUB|RUNNER)_[A-Z_]+' -- '*.py' ':!tests'`.

confirms: none
The new row of `overview.md` *Not verified* asks the orchestrator to answer
from the pull request's next `tests` run. That run is 40447728522 at
7761b95c, event `pull_request`, and it concluded success on every job.
Closing the row is the orchestrator's act, and this round does not write it.
Read through `gh run view 40447728522 --json
status,conclusion,headSha,event,jobs`.

confirms: none
The range breaks nothing else. `uvx ruff check` and `uvx ruff format
--check` over `tests/test_chain_check.py` exit 0, and the run's `lint` job
passed at 7761b95c. The fix adds no case and removes none. Phase 7's new
section is added at the end of its record, and no earlier sentence of the
record stated a fact the section changes. Executed with ruff, read for the records.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 7761b95c. This round ran none of the three. The hygiene run 40447728492 at 7761b95c refused because the newest broad-gate run is behind HEAD, since 516d0ff6 touches `tests/test_chain_check.py` | `broad-gate.md` | the orchestrator, by `broad-gate --base release/v0.22.4 --record` now that this round leaves nothing open |
| The guarantee at 7761b95c. The same hygiene run refused because `guarantee.md` is behind HEAD and the sealer runs again. Its third refusal, a round `target:` behind HEAD, is the one this record answers once it is committed | `guarantee.md` | the sealer, spawned after the orchestrator's broad run |
| Every claim outside the fix range, carried from rounds 1 and 2 and the phase records: the mutant rows, t5's equivalence and the `.test_durations` share. The range touches none of their modules or cases | `phases/phase-1.md` to `phases/phase-7.md` | the sealer, in its sample of claims |
| The 30 changed test files other than the two this round ran, under the sweep's environment by hand. Not re-run here. The pull request's own run 40447728522 ran them under the real environment and passed | `phases/phase-7.md` *The pull request's CI found three cases reading the run's branch* | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `GITHUB_HEAD_REF=some-other-branch bin/test tests/test_chain_check.py -q -p no:xdist -k Test_declared_for_this_branch`, in the clone at 88c27ed5 | 3 failed and 6 passed, exit 1. The three failures are the three cases 516d0ff6 changes |
| The same command in the clone at 7761b95c | 9 passed, exit 0 |
| `bin/test tests/test_chain_check.py tests/test_broad_gate.py -q` in the clone at 7761b95c, under `GITHUB_HEAD_REF`, `GITHUB_BASE_REF`, `GITHUB_EVENT_NAME=pull_request`, `GITHUB_REF`, `GITHUB_ACTIONS=true`, `CI=true`, `GITHUB_EVENT_PATH` naming a payload for a ready pull request, `GITHUB_OUTPUT` and `GITHUB_STEP_SUMMARY` | 568 passed and 1 skipped, exit 0. This is a narrow run and no seal of the suite |
| `uvx ruff check` and `uvx ruff format --check` over `tests/test_chain_check.py` in the clone at 7761b95c | both exit 0 |
| `gh run view 40446828473 --log-failed`, `gh run view 40447728522` and `gh run view 40447728492 --log-failed` | 40446828473 failed the three cases on every failed leg, and its ubuntu leg printed 3 failed and 6,740 passed. 40447728522 succeeded on every job, and its ubuntu leg printed 6,743 passed. 40447728492 refused the round target, the broad-gate record and the guarantee as behind HEAD |
| `git diff 5daa931f...HEAD -- tests`, `git diff 134d7203..HEAD -- tests` and `git diff 88c27ed5..HEAD -- tests`, each through `grep -c` for added and removed `def test_` lines | 169 and 0, 182 and 0, and 1 and 1 |
| `git status --porcelain` in the clone after the probes | empty. The clone, the payload and the saved logs are deleted before the hand-back |
