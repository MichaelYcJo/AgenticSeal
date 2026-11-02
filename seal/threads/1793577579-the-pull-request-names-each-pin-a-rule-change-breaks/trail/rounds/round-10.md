# Review round 10: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 2d5254039, fixes 113acbe19..2d5254039
```

This verifying round read the diff `113acbe19..2d5254039`. That diff holds the fix pass over round 9: one test commit (`13a7bbccb`, the case name at `tests/skills/test_passages.py:87`), the orchestrator's judgment row (`b8ee4a346`, `frame/plan.md:64`), round 9's record (`cce1f7e5a`) and its close block (`2d5254039`). The judgment row bounds this round to the rename. Round 9 closed its one finding `fixed 13a7bbccb`, and this round answers it below.

Carried as coordinates and not re-established: where the corpus guard lives (`skills/settle/scripts/passages.py:57-61`, with `TOP_FILES` and `TOP_DIRS` at `passages.py:29-30`); round 9's seven boundary mutants, each failing its own parameter and no other; and round 4's `bin/seal layout --pairs` result that no duplicate pair names `tests/skills/test_passages.py`. The diff adds no test and changes no parameter, so the pairs were not printed again. Two of round 9's mutant runs were run again here, since the name's truth rests on them. Those runs used a `git clone --no-local` of the main clone at `2d5254039`, under the round's scratch directory. `git status` in the clone was empty after the runs, and the clone was removed before hand-back. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

This round confirms round 9's close and opens no finding, so no finding is a `must`.

## Findings

None.

## Confirmations

```seal
confirms: round-9#1
```
What holds: the close `fixed 13a7bbccb`. Claimed: the round's rename applied and nothing else changed, the 7 parameters pass, the old name stands only in round records, and the layout check and ruff exit 0. Found:

- Nothing but the name changed. Read: `git diff 113acbe19 2d5254039 -- tests/` is one line at `tests/skills/test_passages.py:87`, and a word diff of it changes only the function name. `test_refuses_a_path_one_guard_alone_refuses` became `test_refuses_a_path_one_widened_boundary_alone_lets_through`. The parameters, ids, comment and assertion at `:49-88` are untouched. The new name is round 9's paste-ready text.
- The cases at the new name pass. Executed: `bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider` in the main clone, exit 0, 19 passed. The seven parameters of the renamed case pass under its new name (`-rA`).
- The name now says what the case shows. Round 9's finding rested on `rel in TOP_FILES` widened to `True`, and that run was repeated here. Executed: it is red, 5 failed and 14 passed, failing `[top-files]`, `[top-dirs-slash]`, `[top-dirs-not-tests]`, `[top-dirs-not-hooks]` and `[top-dirs-not-records]`. `rel.startswith(TOP_DIRS)` widened to `True` fails the same five. So no guard refuses those paths alone, as round 9 found. The name no longer claims it. It now claims that one widened boundary alone lets each path through. Executed: `TOP_DIRS` without its slashes fails `[top-dirs-slash]` alone, 1 failed and 18 passed. The other six boundaries are carried from round 9's runs, each one failed and 18 passed. The new name and the comment at `:49-57` now give one reading of the case.
- The old name is gone outside the records. Executed: `git grep -n one_guard_alone -- ':!seal'` exits 1. The new spelling stands at `tests/skills/test_passages.py:87` and in round 9's record alone.
- The layout check still reads the case. The close says the rename keeps the `test_refuses_` prefix the layout check reads. Read: `skills/verify/scripts/test_layout.py:158` holds `REFUSES = "test_refuses_"`. Executed: `bin/seal layout --check tests` exits 0.
- `uvx ruff check` and `uvx ruff format --check` over the file each exit 0 (executed).

A rename adds no behaviour and no case, so it owes no red-first case (`skills/code-review/SKILL.md` *Probes and regression tests*). Nothing in the diff calls for one.

```seal
confirms: none
```
What matched: the judgment row at `frame/plan.md:64`. It cites `skills/implement/SKILL.md` *6. Drain the rows before the broad run, and keep the records*, and that heading stands at `skills/implement/SKILL.md:478` (read). Its table sends an item doable within this pull request to be done now and reviewed by a verifying round before the broad run. That matches the rename in place of the `deferred seal/follow-up.md` the row at `:63` had set for a wording finding. The row says it overrides that one, so the two rows do not leave two readings.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `2d5254039`. This round ran one module and the changed file's lint, so the suite is `unverified`. No finding is open, so what comes due is the broad run and then the sealer's spawn. | the branch at `2d5254039` | the orchestrator, at `seal gate` |
| The case on the Windows leg | `tests/skills/test_passages.py:49-88` | the pull request's `.github/workflows/test.yml` run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider -rA`, in the main clone at `2d5254039` | exit 0, 19 passed, the seven parameters under the new name among them |
| `bin/seal mutate skills/settle/scripts/passages.py --replace 'rel in TOP_FILES' 'True' --tests "bin/test tests/skills/test_passages.py -q -rf --tb=no -p no:xdist -p no:cacheprovider"`, in the scratch clone | red, 5 failed and 14 passed: `[top-files]`, `[top-dirs-slash]`, `[top-dirs-not-tests]`, `[top-dirs-not-hooks]`, `[top-dirs-not-records]` |
| the same command with `rel.startswith(TOP_DIRS)` to `True` | red, 5 failed and 14 passed, the same five ids |
| the same command with `TOP_DIRS` written without its slashes | red, 1 failed and 18 passed: `[top-dirs-slash]` |
| `git grep -n one_guard_alone -- ':!seal'` | exit 1, no line |
| `bin/seal layout --check tests` | exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_passages.py` | exit 0 both |
