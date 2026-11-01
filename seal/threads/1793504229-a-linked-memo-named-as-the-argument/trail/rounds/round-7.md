# Review round 7: 1793504229-a-linked-memo-named-as-the-argument

```seal
target: 9876e1af, fixes a6c538e9..9876e1af
```

This is a narrow verifying round. Its target is the diff from round 6's target (a6c538e9) to HEAD: the round 6 record at 9e7d6921, the fix commit 9580f0f9, and the close block at 9876e1af. The base is `origin/release/v0.27.1`, whose merge base with HEAD is 48d035aa. The scope is the one the orchestrator set: verify the close of round 6's finding 1, read the diff of 9580f0f9 whole, run `bin/seal layout --check tests`, search for a reference to the old name `absolute` outside `os.path.abspath`, and run `tests/skills/test_unverified_check.py`. No `seal/parity.md` is declared, so no original is compared and no `original:` line is owed. The record language is English, since `seal/config.md` has no `Record language` row.

Carried from round 6, not re-established: that the helper's only callers are `repository_of` and `as_named` in the same module, and that `CONTRIBUTING.md` *The test layout* owes a class to a public top-level function only. Re-derived this round: every verdict below, the line numbers, the layout check's output and the search, all at 9876e1af. Every run was in a `git clone --no-local` of the worktree at 9876e1af. Old names in earlier round records and in `frame/plan.md` *Judgments of the run* are history, and this round leaves them as they stand.

## Findings

None.

## Confirmations

```seal
confirms: round-6#1
```
What holds: the helper is private, and the test layout reports no missing class for it (executed). The close claims that `absolute` was renamed `_absolute` at its definition, at its two calls and in `as_named`'s docstring. Read at 9876e1af, `skills/verify/scripts/unverified_check.py:1095` defines `_absolute`, `:1054` is `repository_of`'s call `nearest_existing(_absolute(path))`, `:1076` is `as_named`'s call `full = _absolute(path)`, and `:1075` is the docstring naming `_absolute`. The diff of 9580f0f9 changes those four lines in the module and nothing else in code. Its body and docstring are unchanged, so the behaviour is the same and a rename owes no new case (`skills/code-review/SKILL.md` *Probes and regression tests*). `bin/seal layout --check tests` exits 0 with `151 files read, 0 refused, 86 declare no TARGET`. No `report:` line names `skills/verify/scripts/unverified_check.py`, where round 6's probe at a6c538e9 printed `function absolute has no class Test_absolute`. The fix commit touches the finding's `location:` path `skills/verify/scripts/unverified_check.py`, as a `fixed` close requires.

```seal
confirms: none
```
What matched: no reference to the old name is left outside the history the scope excludes (executed). The close claims `git grep` found no other caller and no attribute access. Four searches over the tree at 9876e1af back it. `git grep -nE '(^|[^a-zA-Z_.])absolute\('` finds only round records 2, 4, 5 and 6. A search for `.absolute` and for `absolute` in single or double quotes finds three `pytest.mark.parametrize` ids, in `tests/hooks/test_optin.py:153`, `tests/skills/test_arm_check.py:1437` and `tests/skills/test_seal.py:1136`, none of which names the helper. A search for an `import` of `absolute` or an `__all__` naming it finds none. A search for the backticked name outside round records finds only `frame/plan.md:47`, a row of *Judgments of the run*. The search ranges over the spellings a Python reference takes, a call, an attribute, a string and an import, so it is built from what produces a reference and not from the instances seen. A name built at run time from parts would escape it, and no `getattr` in the module or its tests takes a computed name for this helper (read).

```seal
confirms: none
```
What matched: the work item's records name the function by its new name (read). `trail/phases/phase-1.md:13`, `:94`, `:95` and `:102` and `gaps.md:10` name `_absolute`, and the diff changes only the name in each line. The close's account of where the branches are pinned matches round 6's mutations: `Test_repository_of` and `Test_as_named` carry the `..` cases, and `Test_main::test_refuses_a_row_lost_under_a_named_link_loop_as_real_reads_it` the loop case.

```seal
confirms: none
```
What matched: the module passes with the rename (executed). `bin/test tests/skills/test_unverified_check.py -q` exits 0 with 390 passed, the same count as round 6's module runs. `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/unverified_check.py` exit 0. The diff adds no test, so no new case is read against its group.

```seal
confirms: none
```
What matched: the label on the broad gate is honest. The close block and `gaps.md:11` leave the full suite and the repository-wide lint to the orchestrator through `seal gate`, and no record on the branch claims a broad run after 4045ddf7 (read). This round ran none. It leaves nothing open, so what comes due is the orchestrator's broad run and then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, at 9876e1af | the branch at 9876e1af | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/seal layout --check tests`, in the clone at 9876e1af | EXIT=0, `151 files read, 0 refused, 86 declare no TARGET`. No line names `skills/verify/scripts/unverified_check.py` |
| `git grep -nE '(^\|[^a-zA-Z_.])absolute\('` | hits only in `trail/rounds/round-2.md`, `round-4.md`, `round-5.md` and `round-6.md` |
| `git grep -nE` for `.absolute` as a word and for `absolute` in single or double quotes | three `parametrize` ids, none naming the helper |
| `git grep -nE 'import .*\babsolute\b\|__all__' -- '*.py'`, filtered to the name and the module | no hit, exit 1 |
| ``git grep -n '`absolute`' -- ':!seal/threads/*/trail/rounds/*'`` | one hit, `frame/plan.md:47`, a *Judgments of the run* row |
| `bin/test tests/skills/test_unverified_check.py -q` | EXIT=0, 390 passed |
| `uvx ruff check` and `uvx ruff format --check` on `skills/verify/scripts/unverified_check.py` | EXIT=0; EXIT=0 |

The clone and the round's scratch outputs were removed before hand-back.
