# Review round 9: 1792976216-the-records-and-the-pr-checks-are-two-answers

target: f8f65ea4, fixes e2b1e994..f8f65ea4

## Findings

This round opens no finding. It read `e2b1e994..f8f65ea4`, which is two commits. `24fe948a` changes the unmerged-entry case in `tests/test_seal.py` and nothing else. `f8f65ea4` changes two lines of `rounds/round-8.md`: finding 1's `verdict:` line, from `open` to `fixed 24fe948a`, and its `answer:` line. It read them against round 8's finding 1 and against the frame that finding names, `spec.md` *In* item 3 and the phase 2 row of `plan.md`. The fix adds no unit and changes no behaviour of `seal pr-checks remove`, so no `regression:` line is owed. The class this round was asked to enumerate has no other member in the branch: no other write to git's standard input, and no comparison of a text-mode read against git's raw bytes. The confirmations give the grounds.

## Confirmations

confirms: round-8#1
The close `fixed 24fe948a` holds (executed and read). The case is `Test_pr_checks.test_refuses_an_index_entry_it_cannot_read_deleted_by_hand`, now at `tests/test_seal.py:3411-3440`. It now runs `git update-index -z --index-info` and feeds it three records, each ending in a NUL byte instead of a line feed (`tests/test_seal.py:3420-3427`). Round 8 traced the failure to a carriage return that Windows' text-mode standard input added to every path. With NUL endings no record carries a line feed for that translation to rewrite.

The fix's two claims were checked in four ways.

First, the claim about Python, read in the local CPython 3.15 `subprocess.py`. The CI legs run 3.12, and this round read no 3.12 source. Given an `encoding`, `Popen.__init__` wraps standard input in an `io.TextIOWrapper` with no `newline` argument. On Windows, `_communicate` writes `input` through that wrapper by `_writerthread` and `_stdin_write`, so each `\n` goes out as `os.linesep`. On POSIX, `_save_input` encodes `input` straight to bytes and translates nothing. The comment the fix adds at `tests/test_seal.py:3422-3423` says this, and it is accurate. The fix's string holds no `\n`. `blob` comes from `git_out`, which strips (`tests/conftest.py:1199-1201`), and `rel` and the tab carry none.

Second, a probe on macOS (executed, `python3 -I test_tmp_nul_index_info.py`). It wrote each input through an `io.TextIOWrapper` set to `newline="\r\n"`, which translates the way the Windows wrapper does, and fed the bytes to git 2.50.1. The fix's three NUL records produced bytes with no carriage return. `update-index` exited 0, and the scoped `ls-files --unmerged` listed 3 entries. The old shape, `--index-info` with `\n` endings through the same wrapper, exited 0 and listed 0 scoped entries. The unscoped listing named the path `".github/workflows/hygiene.yml\r"`, which is round 8's symptom. The two options in the other order, `--index-info -z`, exited 129 with `error: option 'index-info' must be the last argument`. So the order the fix writes is the one git accepts.

Third, the smith's red claims, re-run (executed, `bin/mutation-check tests/test_seal.py` with three `--replace` pairs and the case as its tests). The baseline passed. All three mutants went red: `-z` dropped, the terminator `\0` made `\n`, and the two options swapped.

Fourth, the Windows legs. The branch's `tests` workflow run 40271486400 at `f8f65ea4` concluded `success` on every leg (executed, `gh run view 40271486400 --json status,conclusion,jobs`). Its four Windows shards report 1266 passed and 13 skipped, 2268 passed and 20 skipped, 1283 passed and 5 skipped, and 1709 passed and 14 skipped, none failed (executed, `gh run view 40271486400 --log`). The case ran on a Windows leg and was not skipped. The durations part `test-durations-6` records it at 0.81 seconds (executed, `gh run download 40271486400` of the four parts, searched for the case). Only the Windows legs pass `--store-durations` (read, `.github/workflows/test.yml:107-110`). The `take` fixture's one skip is for the submodule worlds, and the case takes `shared` (read, `tests/test_seal.py:179-184`).

The smith's account in round 8's `answer:` line was checked claim by claim. It said the case was shown red on macOS with the old lines written as Windows writes them; the probe above reproduces that red on the same bytes. It said mutants dropping `-z` or changing the terminator are red, and they are. It said no other stdin write of the branch has the same shape; the next entry finds the same. It said the Windows leg is the orchestrator's to read; this round read it.

confirms: none
No other write the branch makes to git's standard input has this shape (executed). The branch's diff `02ee12de..f8f65ea4`, outside `seal/`, adds one `input=` and no `stdin=`, `Popen` or `communicate(`, and that `input=` is this case's. The diff covers `skills/implement/scripts/seal.py`, `hooks/mode-gate.py`, `bin/seal`, `skills/verify/scripts/unverified_check.py`, `skills/code-review/scripts/chain_check.py` and the tests. The tree at `f8f65ea4` holds no other `input=` that feeds git under `tests`, `skills`, `hooks` or `bin` (executed, `git grep` for `input=` and `stdin=`). The others are JSON payloads for hooks and scripts, which the branch did not add, plus the `stdin=subprocess.DEVNULL` arguments.

confirms: none
No comparison the branch makes sets a text-mode read beside git's raw bytes. Every such comparison holds two sides that newline translation has already passed through (read). `staged_text` takes the index copy through `subprocess.run(..., encoding="utf-8")` (`skills/implement/scripts/seal.py:1738-1757`). Captured output in text mode is translated from CRLF to LF on both platforms: on POSIX by `_translate_newlines`, and on Windows by the reading `TextIOWrapper`'s universal newlines (read, the local `subprocess.py`). `plugin_workflow` reads the template through `open(..., encoding="utf-8")` (`skills/implement/scripts/seal.py:1830-1833`). `workflow_at` reads the working file the same way (`skills/implement/scripts/seal.py:1856-1857`). So `staged == plugin_workflow()` at `skills/implement/scripts/seal.py:2040` compares two LF strings, and so does `text == plugin_workflow() == staged_text(repo, WORKFLOW)` at `skills/implement/scripts/seal.py:2110`. That holds whether the index blob carries LF or CRLF, so `core.autocrlf` decides nothing there. The other side of `:2040`, `git diff --cached --quiet`, is git comparing blobs and is read only for its exit code. The test-side comparisons go through the conftest `git` helper, which also passes `encoding` (`tests/conftest.py:1187-1196`). Examples are `cat-file blob` output against `"name: mine\n"` and `mine` (`tests/test_seal.py:3371`, `tests/test_seal.py:3409`).

This settles by reading round 8's `## Not judged` row on `skills/implement/scripts/seal.py:2040`, which round 7 first carried. Both sides of that comparison are translated on Windows, so it compares one file with itself, as the `staged_text` docstring says. It was not run on Windows with `core.autocrlf` off. The CI legs ran the arm's cases under the runner's own setting, and they passed.

confirms: none
`24fe948a` passes its narrow checks (executed). The case, round 8's census cases and the helpers selection pass in the round's clone: `bin/test tests/test_seal.py tests/test_a_shrunken_corpus_declines_to_judge.py -q -p no:randomly -k 'deleted_by_hand or path_list or unguarded or helpers'`, 12 passed. The count matches round 8's mutant run, so the census row `e2b1e994` added still counts the case's two `ls-files` calls. `uvx ruff check` and `uvx ruff format --check` over `tests/test_seal.py` exit 0. Both commits carry the work item's `SpecSeal-Routing` trailer. The repository's identity is both their author and their committer (`git log -1`). The fix adds no test function, so no new test is read against its group.

Facts carried from round 8, not re-established: the frame's coordinates for the case (`spec.md` *In* item 3 and the phase 2 row of `plan.md`), and the census's table semantics behind the row `e2b1e994` added. Every verdict above was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `f8f65ea4`. Contract rule 2 gives them to the broad gate, so this round did not run them. `broad-gate.md` still holds the run at `4b63982f`. The smith's suite stays `unverified`. This round leaves nothing open, so the broad run comes due next, and the sealer's spawn after it | the branch | the orchestrator, by `broad-gate` |
| `questions.md` Q1 and Q4 stay open for the owner, built on their defaults (a). Carried from round 6 | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/questions.md` | the owner, relayed by the orchestrator in the pull request body |
| The settle holds this spec behind specs refused for reasons outside this branch. Carried from round 2, and not replayed | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/overview.md:25` | #1033, and the orchestrator at the settle that applies this release's specs |
| `guarantee.md` is behind HEAD: it audited `64d54bd4`, and its verdict reads withheld | `seal/specs/1792976216-the-records-and-the-pr-checks-are-two-answers/guarantee.md:5` | the sealer, at its next run after the broad gate |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the repository into the round's scratch directory, checked out at `f8f65ea4` | clone at `f8f65ea`; `git status --short` stayed empty after every probe below |
| `python3 -I test_tmp_nul_index_info.py`: three `git init` repositories in the round's scratch directory, one blob each, three stage records written through an `io.TextIOWrapper` with `newline="\r\n"` and fed as bytes to `update-index` | exit 0. `-z --index-info` with `\0`: no carriage return in the bytes, update exit 0, 3 scoped unmerged entries. `--index-info` with `\n`: carriage returns in the bytes, update exit 0, 0 scoped and 3 unscoped entries, the path `".github/workflows/hygiene.yml\r"`. `--index-info -z` with `\0`: update exit 129, `option 'index-info' must be the last argument` |
| `bin/test tests/test_seal.py tests/test_a_shrunken_corpus_declines_to_judge.py -q -p no:randomly -k 'deleted_by_hand or path_list or unguarded or helpers'` in the clone | 12 passed, exit 0 |
| `bin/mutation-check tests/test_seal.py` with three `--replace` pairs: `-z` dropped, `{rel}\0` made `{rel}\n`, `-z` moved after `--index-info`; `--tests "bin/test tests/test_seal.py -q -p no:xdist -p no:randomly -k deleted_by_hand"` | baseline passed; 3 mutants, 3 red, 0 survived |
| `uvx ruff check` and `uvx ruff format --check` over `tests/test_seal.py` | both exit 0 |
| `gh -R MichaelYcJo/SpecSeal run view 40271486400 --json status,conclusion,jobs`, then `--log` searched for each leg's summary line | head `f8f65ea4`, completed, success. Every pytest leg succeeded. The Windows shards: 1266 passed and 13 skipped, 2268 passed and 20 skipped, 1283 passed and 5 skipped, 1709 passed and 14 skipped |
| `gh -R MichaelYcJo/SpecSeal run download 40271486400` of `test-durations-4` to `test-durations-7`, searched for the case | the case stands in `test-durations-6` only, at 0.81 seconds |
| `git diff 02ee12de..f8f65ea4` outside `seal/`, searched for `input=`, `stdin`, `Popen`, `communicate`, byte literals and `newline`; `git grep` for `input=` and `stdin=` at `f8f65ea4` under `tests`, `skills`, `hooks` and `bin` | one new `input=`, this case's, and no other stdin write the branch adds; the tree's other `input=` lines feed JSON to hooks and scripts |
| `git log -1` of `24fe948a` and `f8f65ea4`, and `git show f8f65ea4` | both carry the routing trailer and the repository's identity; `f8f65ea4` changes round 8's `verdict:` and `answer:` lines only |

The probe file, its three repositories, the downloaded durations parts, the saved run log, the clone and the saved outputs were removed before the hand-back.
