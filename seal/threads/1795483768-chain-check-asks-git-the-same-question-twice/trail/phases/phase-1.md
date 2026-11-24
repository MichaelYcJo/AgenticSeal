# Phase 1: 1795483768-chain-check-asks-git-the-same-question-twice

## What this phase found

### The frame, read against the tree before the build

The frame holds for this phase. At `c66128300`, `lib/gitcmd.py#git` kept no state between calls, and `chain_check.py#main` and `settle.py#main` each ran the command inside a `try` that turns `Failed` into exit 2 (read). `lib/sibling.py#load` returns the module `sys.modules` holds under the file's stem (`lib/sibling.py:111`), so every script of one process reaches one `gitcmd` (read). S1's `bodied` case shows the body arm's `follows` meeting the run's answers: it repeated reads before the memo and repeats none after it (executed, below).

One cell of the frame does not match the world it describes. `frame/design.md` S5's *Verifiable how* cell counts `ls-files -z` among the dry run's repeats. In a world built as S5's *Given* reads, the dry run asked it once (executed). `settle.py#tracked_names` (`:1044`) asks it only through `open_rows` (`:1072`), for a released work item whose record holds an open row. The case therefore gives the first design's record one open row, and with it the dry run repeats `ls-files -z` as well as the pair of commits (executed). This does not contradict *Grounding*: the framer's run over the real tree reached `open_rows`.

### Decisions settled while building

- **The contract stands in the module docstring.** A paragraph of `lib/gitcmd.py`'s docstring names which runs may enter `one_run`, and `one_run`'s own docstring points to it. Grounds: `frame/design.md` *Data & interfaces*, the third item, and G3, which names the module docstring as the home of the runner's details.
- **`git` reads `check` after the lookup, on every ask.** It starts its process through `_start` with `check` false, and raises `Exited` from the process's code and stderr itself, inside a run and outside one. `_start` builds `Exited` from the same three values (read), so a run outside `one_run` raises the same line as before. Grounds: `frame/design.md` *Data & interfaces*, the second item.
- **No new case in `tests/skills/test_chain_check.py` for S2.** This departs from S2's *Verifiable how* cell. Two cases already run `main` twice with a commit between, and each goes red alone against a memo that is never emptied (executed: `seal mutate` with `-k` naming one case, at `ed89d8389`). `Test_main::test_accepts_a_release_pull_request_leaving_a_squashed_item_to_its_own` fails at `assert code == 1` with 0. `Test_rule_changes_read::test_accepts_a_spec_another_pull_requests_squash_carried_unread` fails at `assert code == 1 and f"{own}/trail/gate.md" in out`. A third case would watch nothing those two do not. Grounds: `agents/crafter.md` *A new test starts from its group*.
- **One recorder of git commands serves both modules.** `tests/skills/test_settle.py#asks` wraps `subprocess.run` and lists each git command a call starts with its stdin, and `#repeated` names each one an earlier one equals. `#calls` now counts through `asks`, so the module keeps one wrapper. `tests/skills/test_chain_check.py` imports `asks` and `repeated` from it, as it already imports `unanswered`. Grounds: `CONTRIBUTING.md` *The test layout*, a helper two test files use is defined once, in one of them.
- **A recorded command is its argv and its stdin.** The memo keys on the input too, so two `cat-file --batch` runs with different names on stdin are two questions, and the recorder does not read them as a repeat.

### Seen red

- **S1**, `Test_main::test_asks_git_each_read_once_in_a_run` in `tests/skills/test_chain_check.py`, was written before the memo and run against `c66128300`'s code. `branch` repeated 9 reads, the first `show HEAD:seal/threads/1791999999-a-work-item/routing.md`. `bodied` repeated 12, among them `rev-parse --verify --quiet <base>^{commit}` and `diff-tree` of `follows` (executed). With the memo in place both pass, and with `main`'s `with GITCMD.one_run():` replaced by `with open(os.devnull):` the case fails again at `assert repeated(asked) == []` (executed, mutant 13 below).
- **S5**, `Test_main::test_asks_git_each_read_once_in_a_run` in `tests/skills/test_settle.py`, was written before the memo and run against `c66128300`'s code. The dry run repeated the pair's `merge-base --is-ancestor`. `--apply` repeated it and the three reads of `versions`: `for-each-ref`, `cat-file --batch-check` and `rev-list --parents --stdin` (executed). After the open row was added in `2d7e0767a`, the case was shown red with `settle.main`'s `with gitcmd.one_run():` replaced by `with open(os.devnull):`. The dry run then repeats the pair and `--literal-pathspecs ls-files -z` (executed, mutant 14 below).
- **S2, S3 and S4**, the four cases of `Test_one_run` in `tests/lib/test_gitcmd.py`, were written after the memo. Each is shown red by the break its design cell names, in the table below.

### Mutation runs

Each row is one `seal mutate` run over a committed file (executed). Rows 1 to 12 break `lib/gitcmd.py` at `ed89d8389` and run `bin/test tests/lib/test_gitcmd.py -q -x -p no:xdist -k <case>`. Row 13 breaks `chain_check.py` at `ed89d8389`, and row 14 breaks `settle.py` at `2d7e0767a`. Every run was red, and each failing line names the guard broken.

| # | Break | Case | Failing line |
|---|---|---|---|
| 1 | `one_run`'s `finally` sets nothing, so answers outlive their run (S2) | `test_accepts_a_new_answer_in_a_run_entered_after_one_ended` | the second run reads the first commit for `rev-parse HEAD` |
| 2 | `one_run` resets after a return only, so a run ended by an exception keeps its answers (S2) | the same | the third run reads the second commit |
| 3 | `_answers` starts as `{}`, so the memo is always on (S3) | `test_refuses_to_answer_again_outside_a_run` | `assert len(calls) == 2`, with 1 |
| 4 | `check` is read on the first ask only (S4) | `test_refuses_to_keep_a_command_that_gave_no_answer` | `DID NOT RAISE Exited` on the second ask |
| 5 | an `Unrun` is stored and raised again from the store (S4) | the same | `assert len(calls) == 2`, with 1 |
| 6 | a run entered inside a run makes its own store | `test_accepts_one_process_for_a_command_asked_again_in_a_run` | the inner run's `is first` |
| 7 to 11 | the key without `root`, `args`, `given`, `binary` or `env`, one break each | the same | `assert len(calls) == 6` |
| 12 | the lookup removed, so the store is never read | the same | the inner run's `is first` |
| 13 | `chain_check.main` runs `_checked` outside `one_run` | `Test_main::test_asks_git_each_read_once_in_a_run[branch]` | `assert repeated(asked) == []` |
| 14 | `settle.main` runs `_settled` outside `one_run` | `Test_main::test_asks_git_each_read_once_in_a_run` | `assert repeated(asked) == []`, naming the pair and `ls-files -z` |

### The phase boundary run

One `bin/test ... -q` over 34 paths passed 4,468 cases and skipped 10, at `2d7e0767a` with this phase's records on disk (executed). The paths are `frame/design.md` S7's four modules, every other test file whose text names `gitcmd`, `chain_check`, `settle.py`, `settle.main`, `seal settle` or `pr_body` (`git grep -l -E` over `tests/*.py`, with `tests/conftest.py` left out), and `tests/text` and `tests/behaviour`. A test file that reaches `lib/gitcmd.py` only through another module is outside that list, and `gaps.md` names it. The run before the records were written failed one case, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, on the `gaps.md` this phase writes.

`1ecdde329` follows that run and changes two docstrings alone, `lib/gitcmd.py`'s module docstring and S5's case. `bin/test tests/lib/test_gitcmd.py tests/skills/test_settle.py tests/skills/test_chain_check.py -q -k "Test_one_run or test_asks_git_each_read_once_in_a_run or Test_git or census"` passed 57 cases at that commit, so both modules still import (executed).

### For phase 2

`tests/skills/test_settle.py#asks` lists each git command a call starts, with its stdin, so S6's count of `cat-file --batch` and `show` processes can be read through it.
