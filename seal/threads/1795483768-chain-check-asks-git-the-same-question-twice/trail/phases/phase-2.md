# Phase 2: 1795483768-chain-check-asks-git-the-same-question-twice

## What this phase found

### The frame, read against the tree before the build

The frame holds for this phase. At `541d15e3b`, `chain_check.py#tracked_declarations` listed HEAD's entries with one `ls-tree` and read each `routing.md` through `read_record`, one `git show` each, or from disk under `WORKTREE` (read). `settle.py#decoded` and the loop of `settle.py#blobs` were as *Data & interfaces* describes them, and `blobs` was the only reader of the loop (read). No case reaches `settle.decoded` or the loop except through `blobs` (executed: `git grep` over `tests/`).

*Alternatives considered* A5 names a risk: a case that hands a declaration to `main` through the `reading` or `answered` seam, without committing it, would no longer reach `tracked_declarations`. No case of `tests/skills/test_chain_check.py` failed after the change, so none relied on it (executed: S7's line, below).

### Decisions settled while building

- **The batch read stands in its own function, `chain_check.py#_blob_texts`.** The frame names no function for it. `tracked_declarations` lists `(path, blob id)` pairs, then reads the texts through `_blob_texts` at HEAD or through `read_record` under `WORKTREE`, and parses each. Grounds: `frame/design.md` *Data & interfaces*, the fourth item, which keeps `tracked_declarations`'s signature and answer. It was `blob_texts` until `4646cc303`. `CONTRIBUTING.md` *The test layout* gives each public function of a module a class of its own, and the function's cases are `tracked_declarations`'s, so the underscore marks it as that function's helper.
- **No batch starts where HEAD carries no declaration.** `_blob_texts` returns `[]` for no blob ids and starts nothing. Without that guard, every run over a repository with no work item would start a `cat-file --batch` with empty input that phase 1's code never started. `tests/skills/test_chain_check.py`'s `undeclared` world, which `Test_routing_trailers` runs `main` over, is one (read). Grounds: `frame/design.md` G2, which judges the work by the processes it saves.
- **A batch that exits non-zero reads as no declaration.** `_blob_texts` reads its exit code before it reads the output, and gives None for each blob. Without that check, `batch_texts` raises `ValueError` on empty output. A `missing` answer reads as None through `batch_texts`'s `(None, answer)`. Grounds: `frame/design.md` *Data & interfaces*, the fourth item.
- **An `Unrun` from the batch ends the run at exit 2, as every other read does.** `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line` gains the parameter `declarations`, the words `cat-file --batch`. That case lists each git read of `main` by the reader that asks it, and the batch is a new read. Grounds: `frame/design.md` G3, a command that did not answer is no answer.
- **`decoded` and the parse move unchanged, so they get no new case.** `git grep -n -E '^def decoded' -- lib skills` names `lib/gitcmd.py:296` alone (executed, the census `frame/plan.md` phase 2's Verified by cell names). `settle.py` holds no bare `decoded(` call (executed: `grep -n decoded skills/settle/scripts/settle.py` lists `gitcmd.decoded` and one docstring line naming `lib/gitcmd.py#decoded`). `Test_blobs` in `tests/skills/test_settle.py` passes unchanged over the moved parse (executed, in S7's line below). Grounds: `skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the row for names or places only.
- **`tests/lib/test_gitcmd.py` gains no `Test_decoded` or `Test_batch_texts`.** `CONTRIBUTING.md` *The test layout* gives each public function a class in its module's test file, and `seal layout --check tests/lib/test_gitcmd.py` reports both as missing, without refusing (executed). Before this phase every public function of `lib/gitcmd.py` had its class. Both units moved with their bodies unchanged, `frame/plan.md` phase 2 names `Test_blobs` as their proof, and a case in either class would watch nothing `Test_blobs`'s two cases do not. Grounds: `agents/crafter.md` *A new test starts from its group*, and the verify row above. `gaps.md` `## Not done` names it for the proofer.
- **`git_run`'s error line names `said` before it raises.** The line with `gitcmd.decoded` ran past the 88-column width. The message is the same text. Grounds: `ruff.toml` `line-length = 88`.
- **The fragment and the version move in one commit, `5b2b334a1`.** Grounds: `frame/design.md` G6 and S10.

### Departures from the frame

- `frame/design.md` S6 names one case. The phase adds two cases in a new group, `Test_tracked_declarations`, and one parameter of an existing case. The second case holds *Data & interfaces*' non-zero exit, and the parameter holds G3 for the new read. `seal layout --pairs tests/skills/test_chain_check.py` named no pair (executed). The module held no group for `tracked_declarations` before. Its other cases are in `Test_declared_for_this_branch`, through the function that calls it.
- S6's case also asserts that no batch starts where HEAD carries no declaration. *Decisions settled while building* gives the grounds.

### Seen red

- **S6**, `Test_tracked_declarations::test_accepts_the_declarations_at_head_read_in_one_process`, was written before the change and run against `541d15e3b`'s `chain_check.py`. It failed at `assert verbs == ["ls-tree", "cat-file"]` with `['ls-tree', 'show', 'show', 'show']` (executed).
- **The non-zero exit**, `Test_tracked_declarations::test_refuses_a_declaration_from_a_batch_that_exited_non_zero`, was run against the same code. It failed at `assert ... == []`, because the old code started no batch and took the declaration (executed). Mutant 5 below shows it red with the exit code left unread.
- **The batch's `Unrun`**, `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[declarations]`, was run against the same code. It failed at `assert len(asked) == 1` with 0, because no `cat-file --batch` was started (executed). Mutant 9 below shows it red with the `Unrun` caught.
- The first assertion of S6's case, that a HEAD with no declaration starts `ls-tree` alone, was added in `85db20afa` after the change. Mutant 4 shows it red.

### Mutation runs

Each row is one `seal mutate` run over `skills/code-review/scripts/chain_check.py` at `85db20afa` (executed), where the helper was `blob_texts` and the two cases bore the names `test_reads_the_declarations_at_head_in_one_process` and `test_reads_no_declaration_from_a_batch_that_exited_non_zero`. `4646cc303` renames the three and changes no body. Rows 1 to 8 ran `bin/test tests/skills/test_chain_check.py -q -x -p no:xdist -k Test_tracked_declarations`, first as one batch of eight, which read 8 red, and then rows 1, 4, 5 and 8 alone to read the failing line. Row 9 ran `-k declarations`. Every run was red.

| # | Break | Case | Failing line |
|---|---|---|---|
| 1 | `if WORKTREE:` read as `if False:`, so the batch is read under `WORKTREE` | S6's case | `assert verbs == ["ls-tree"]`, with `cat-file` |
| 2 | the texts read through `read_record`, one `show` each | S6's case | red, line not read alone |
| 3 | the type, `parts[1]`, given to the batch in place of the blob id | S6's case | red, line not read alone |
| 4 | `if not blobs:` read as `if False:`, so an empty batch starts | S6's case | `assert started() == ([], ["ls-tree"])`, with `cat-file` |
| 5 | the batch's exit code left unread | the non-zero exit case | `ValueError: subsection not found`, raised by `batch_texts` over the failed batch's empty output |
| 6 | the batch asked with `binary=False` | S6's case | red, line not read alone |
| 7 | the batch's answer taken in place of its text | S6's case | red, line not read alone |
| 8 | an unparsed text kept as a declaration | the non-zero exit case | `assert ... == []`, with `(path, None)` |
| 9 | `_blob_texts` catches `Unrun` and returns None for each blob | `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[declarations]` | `assert code == 2`, with 0 |

Mutant 5's failing line is a raise inside `batch_texts`, not the case's assertion. The guard exists so that a failed batch is not parsed, and the raise is that parse, so the line names the guard's purpose.

### The phase boundary run

`frame/design.md` S7's line, `bin/test tests/lib/test_gitcmd.py tests/skills/test_chain_check.py tests/skills/test_settle.py tests/skills/test_pr_body.py -q`, passed 608 cases over the code `c1cbcdba3` commits (executed). Its four modules are also in the run below.

One `bin/test ... -q` over 38 paths passed 4,552 cases and skipped 10, at `4646cc303` with this phase's records on disk (executed). The paths are every test file whose text names `gitcmd`, `chain_check`, `settle.py`, `settle.main`, `seal settle`, `pr_body`, `plugin.json` or `batch_texts` (`git grep -l -E` over `tests/*.py`, with `tests/conftest.py` left out), and `tests/text` and `tests/behaviour`. The same run at `5b2b334a1` failed one case, `tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_layout::test_accepts_this_repositorys_tests`: `seal layout --check` refused `Test_tracked_declarations`, whose two cases named neither `test_accepts_` nor `test_refuses_`. `4646cc303` renames them. A test file that reaches a changed path only through another module is outside the list, and `gaps.md` names it.
