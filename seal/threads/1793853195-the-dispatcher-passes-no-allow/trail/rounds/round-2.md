# Review round 2: 1793853195-the-dispatcher-passes-no-allow

```seal
target: 1edcbc8a, fixes 93662643..1edcbc8a
```

This is a verifying round. The range is ef8dc987 (round 1's record), 6b749ea1 (two assertions in `tests/hooks/test_dispatch.py#Test_merge::test_refuses_to_pass_on_a_decision_other_than_deny_or_ask` and its docstring), e359beb3 (`trail/phases/phase-1.md` and `gaps.md`) and 1edcbc8a (round 1's close block). `git diff 93662643 1edcbc8a -- hooks/` is empty, so the code under the case is the code round 1 reviewed (executed). `seal/parity.md` is not declared, so no parity comparison is owed. `seal/config.md` has no `Record language` row, so this record is in English.

Carried from round 1 and not re-established: the guard's coordinate `hooks/dispatch.py:225` and the join at `:282`; that `seal layout --pairs` names no pair in `tests/hooks/test_dispatch.py`; and that `bin/seal rules --check` exits 0 on this work item's rule change, since the range touches no frame file. Re-established this round: every verdict below, and the module's result at HEAD.

The axes walked are the ones the fix touches. Error paths: whether `merge` still raises outside `run_gate`'s isolation on a reasonless or null-reason `allow`. Test quality: whether each new assertion is red with only the guard it names removed, and whether it holds a fact its group does not. The Python 3.9 floor: whether the two shapes print the same under `/usr/bin/python3` 3.9.6. The account: whether the records the fix pass edited say what the tree does.

## Findings

None. The one finding of round 1 is closed, and the fix range adds no defect.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the close `fixed 6b749ea1`. The fix pass claimed that the two assertions pass against the build, and that each goes red under one mutant of the guard. `tests/hooks/test_dispatch.py:536-539` builds an `allow` with no reason and one with a null reason and asserts that `merge` prints `""` for each. In a `git clone --no-local` at 1edcbc8a, `bin/test tests/hooks/test_dispatch.py -q -p no:xdist` ended 54 passed, exit 0. With `hooks/dispatch.py:225` changed to `else:`, the same command ended 1 failed and 53 passed, exit 1, on `KeyError: 'permissionDecisionReason'` raised at `hooks/dispatch.py:228` from the test's line 539. With the guard changed to `elif "permissionDecisionReason" in hook_out:`, it ended 1 failed and 53 passed, exit 1, on `TypeError: sequence item 0: expected str instance, NoneType found` at the join, `hooks/dispatch.py:282`, from line 539 (executed). The first mutant fails on the reasonless body and the second on the null one, so each of the two loop items is shown red by a mutant of the guard it names. Round 1's own evidence line ended 54 passed under the first mutant, and it now ends 1 failed. This matches the fix pass's account in its close and in `trail/phases/phase-1.md` *Mutation*. The fix pass ran `seal mutate`, and this round patched the file by hand in the clone; the outcome is the same.

What matched: the case against its group. Every other decision in the module is built with a reason or is a passed `ask` or `deny`. The only reasonless decision in the file is the passed `ask` at `tests/hooks/test_dispatch.py:416` (executed: `grep -n '"permissionDecision"' tests/hooks/test_dispatch.py`). So the new assertions are the only ones that reach the dropped-decision branch where the reason is absent. They hold *Scope* 1's "where it has one" in `frame/design.md`. The snippet round 1 proposed builds `bare` inside the loop, and the commit builds it once above the loop; the assertions are the same.

What matched: the docstring's added sentence, "An `allow` with no reason, or a null one, prints nothing and ends nothing" (`tests/hooks/test_dispatch.py:530-531`). "Prints nothing" is the `== ""` assertion. "Ends nothing" is the same assertion's call returning instead of raising, which both mutant runs above show failing.

What matched: the two shapes under Python 3.9. `/usr/bin/python3 -I` 3.9.6 loaded the clone's `hooks/dispatch.py` and printed `''` for a reasonless `allow`, a null-reason `allow` and an empty-reason `allow`. Beside an `ask` with reason `rk`, each printed the `ask` with the reason `rk` alone (executed). `gaps.md` still names the 3.9 floor as unverified in CI, and that row is unchanged and still true.

What matched: the records e359beb3 changed. `trail/phases/phase-1.md` *Seen red* and *Mutation* each gain one line that says what this round re-ran above. The *Seen red* line says the assertions are green at ecfb7b58. `git diff ecfb7b58 1edcbc8a -- hooks/` changes two comment lines and no code, so the green at HEAD stands for ecfb7b58 (executed). The *S3 and S5* paragraph still holds: the docstring line 6b749ea1 replaced belongs to a case ecfb7b58 added, not to an existing case. The two changed `gaps.md` rows add the fix pass's macOS run of `tests/hooks/test_dispatch.py`, and their answerers are unchanged.

What matched, as a claim the close did not list: e359beb3 also rewrites one sentence of the phase record's paragraph *Where a dropped decision stands beside a decision-less JSON object*. The sentence called the behaviour "the reading taken" of *Scope* 1. It now says *Scope* 1 states it since the fold at 93662643. *Scope* 1 at HEAD says "beside such an object the JSON path prints the object and drops the texts" (read: `frame/design.md` line 26), so the rewritten sentence is true. The close names only the *Seen red* and *Mutation* additions, so this sentence went unannounced. It changes no claim about the code.

What matched: the closed set of rule 12 for the fix. The work item's files that state the present were read whole at 1edcbc8a: `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `trail/phases/phase-1.md`. None contradicts HEAD. `changelog.md` is unchanged, and the close says why: what ships does not change, since the fix adds assertions and no code.

What matched: `uvx ruff check` and `uvx ruff format --check` on `tests/hooks/test_dispatch.py` each exit 0 in the clone (executed).

What matched: the honesty of the `unverified` label. `gaps.md` *Not verified* names the full suite, the repository-wide lint and the format check at HEAD as unverified, with the orchestrator's broad run as their answerer (read). This round leaves nothing open. The orchestrator's broad run comes due next, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, among them the modules that read the records under `seal/threads/` | the `Broad gate` row of `seal/config.md` | the orchestrator's broad run, then the sealer |
| The two new assertions on the ubuntu and Windows legs | `.github/workflows/test.yml` | the `tests` workflow on the pull request |
| Whether the change clears `HOOK_GRANTS_PERMISSION` in the plugin directory's validation | `frame/questions.md` Q1 | the owner, on resubmitting the next release's `dist` |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into the round's scratch directory, checked out at 1edcbc8a, then `bin/test tests/hooks/test_dispatch.py -q -p no:xdist` | 54 passed, exit 0 |
| the same command with `hooks/dispatch.py:225` changed to `else:` | 1 failed, 53 passed, exit 1: `KeyError: 'permissionDecisionReason'` at `hooks/dispatch.py:228`, from `tests/hooks/test_dispatch.py:539` |
| the same command with `hooks/dispatch.py:225` changed to `elif "permissionDecisionReason" in hook_out:` | 1 failed, 53 passed, exit 1: `TypeError` at `hooks/dispatch.py:282`, from `tests/hooks/test_dispatch.py:539` |
| `/usr/bin/python3 -I -c` (3.9.6) loading the clone's `hooks/dispatch.py` at 1edcbc8a and calling `merge` on an `allow` with no reason, a null reason and an empty reason, each alone and beside an `ask` | `''` alone, and the `ask` with reason `rk` beside it, for each; exit 0 |

The file was restored with `git checkout -- hooks/dispatch.py` after the mutant runs, and the clone and the scratch directory were removed before the hand-back.
