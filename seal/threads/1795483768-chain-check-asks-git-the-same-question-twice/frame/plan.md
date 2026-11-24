# Implementation Plan: 1795483768-chain-check-asks-git-the-same-question-twice (#1603)

## Technical context

The tree as read at `136cfca25`.

`lib/gitcmd.py#git` (`:201`) starts every git command the plugin's scripts start, through `_start` (`:164`), under `TIMEOUT`. It keeps no state between calls. `chain_check.py` reads git through its own `git` (`:357`), which returns stdout or None, and through `GITCMD.is_ancestor` (`gitcmd.py:248`). `pr_body.py` reaches git through `CHAIN.git` and `CHAIN.follows` of the `chain_check` instance it loads itself. `settle.py` reads git through `gitcmd.git` directly (`show`, `released`, `resolves`), through `git_run` (`:475`) and `git_fields` (`:1550`), and through `rule_changes.py`, which loads `gitcmd` again by its stem. Because every one of these paths ends in the one `gitcmd` module of the process, a store inside `gitcmd.git` is the one place all of them meet (`frame/design.md` *Grounding*, *Where a per-run memo has to live*).

`chain_check.py#main` (`:2107`) wraps `_checked` in a `try` that turns `GITCMD.Failed` into exit 2. `settle.py#main` (`:2010`) does the same for `_settled`. Each `with` goes inside that `try`, so an `Unrun` raised in the run still reaches the same line.

The tests reach both commands in the process. `tests/skills/test_chain_check.py` calls `chain.main` over many repositories in one process, and #1581's seams replace `read_record`, `tracked_files`, `follows` and `git` on the module (`reading` at `:441`, `answered` at `:466`). Those seams sit above `gitcmd.git`, so the memo is below every seam and leaves each one as it is. A test that patches `subprocess.run`, such as `unanswered` (`test_settle.py:188`), is reached through `_start` on the first ask of an argv, as now.

The failure scenario of the chosen approach, six months on: someone adds a git write to a command that runs inside `one_run`, or adds to `settle --apply` a git read of the working tree after its removals, such as `ls-files --deleted` or `status`. Inside the memo that read would answer as before the removal. The docstring's contract names the runs that may enter, and the case of S2 shows only that the store dies with the run. Nothing refuses a write inside a run. A reviewer reading a diff that adds a write to `chain_check.py` or `settle.py`, or a read after `apply`'s first `rmtree`, is what catches it, and the docstring is what that reviewer opens.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. One per-run memo inside `lib/gitcmd.py#git`, entered by `main` of `chain-check` and of `settle` | A command that writes through git inside the run reads a stale answer. Neither command does (`frame/design.md` *Grounding*, *Which reads cannot change within one run* and *`settle` writes after its last git read*). | Chosen. It reaches every path to git, `pr_body.py`'s second `chain_check` instance and `rule_changes.py` among them, and changes no function a case calls. |
| A2. A memo per reader inside `chain_check.py`, such as `functools.lru_cache` on `touched`, `follows` and `read_record` | Under CI the check is `__main__`, and `pr_body.py` loads a second `chain_check` instance, so the body arm's `follows` misses the store. `GITCMD.is_ancestor` bypasses `chain_check.git`. A module-level cache outlives the run: `test_chain_check.py` runs `main`, commits, and runs `main` again in one process, and the second run would read the first run's `follows`. `settle.py` would need a second copy. | Rejected. |
| A3. Replace the structure: each arm receives the records and commits another arm already read, so nothing is read twice and no memo exists | The three arms ask `follows` of different commits whose later commits overlap, so the overlap stays unless a shared store holds it, which is A1 again. Every arm's signature changes, and with them #1581's seams and every case that calls an arm with its input given. The issue keeps the existing cases as they stand. The premise that keeps the structure is that each arm reads its own records, so a case hands one arm its input without building the others, which #1581's *Scope* items 2 and 3 rest on (read: `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/frame/design.md`). Checked: `reading`, `answered` and `records_read` patch the readers one by one. | Rejected. |
| A4. Resolve HEAD to its commit once at the start and read every record at that commit | It removes no repeat A1 does not, and it changes the argv and the messages that name HEAD. | Rejected. |
| A5. One `cat-file --batch` for the declarations at HEAD, given the blob ids `tracked_declarations`'s `ls-tree` already lists | A failing batch, or a `missing` answer, must read as `show`'s non-zero reads now. Item 5 of *Scope* and `frame/design.md` *Data & interfaces* say how. A case that hands a declaration to `main` through the `reading` or `answered` seam and never commits it would no longer reach `tracked_declarations`. The framer found none. Of the cases that run `main` under either seam and name a `routing.md`, `:1824` commits its declaration through `put_spec`, `:4654` and `:4672` hand a text in place of a declaration HEAD carries at the same path, which names the branch, so the run judges that declaration whichever text `tracked_declarations` reads, and `:5072` runs under `--worktree`, where `read_record` still reads it (executed: an `ast` walk of `tests/skills/test_chain_check.py` for the tests that call `answered(` or `reading(`, name `routing.md` and run `main`; read: each case it listed). | Chosen. In #1581's real run the declaration reads are most of the distinct processes (`frame/design.md` *Grounding*, *What one `chain-check` run asks git today*), and their number grows with every unsettled work item of a repository. The parse is `settle.py#blobs`'s, moved, not a second one. |
| A6. One process for the later commits' paths in `follows`, by `diff-tree --stdin` or `log --name-only` | `diff-tree --stdin -z` sets each commit id as a field like a path, and `log` is porcelain that `diff.renames` and other keys reshape (`frame/design.md` *Grounding*, *A batch of commits' paths is not an exact reading*). | Rejected. After A1 each commit is one `diff-tree` per run, 8 in #1581's real run. |
| A7. Read the judged work item's records through one batch per work item, a read-ahead that `read_record` answers from | It is a second store beside A1's, holding texts git did not give to the argv `read_record` asks. It also lists the records ahead of the arms that decide which to read. The gain is the number of record files a run reads of a judged work item, less one. #1581's run read 8: `routing.md`, the frame's design and plan, two round records, the gate record, the guarantee and `pr.md` (executed, the probe of `frame/design.md` *Grounding*). | Deferred to the Windows reading after phase 2, `frame/questions.md` Q1. |
| A8. One `cat-file --batch` for `settle.py#timeline`'s designs | `settle` runs once per release, by the owner. Its dry run over 45 designs took 2.2 s on the framer's machine (executed), and `test_settle.py`'s worlds hold few designs, so the suite gains little. Timeline's `show` is the only `show` of the dry run, which `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line[show]` selects, so that case would have to change. | Rejected. |
| A9. Batch the design reads of `carried_by` per edited design, or `log` per changed declaration | Each is one `log` per path the pull request edits under `seal/threads/`, usually none or one. One `log` over several pathspecs loses which commit touched which path. | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2 and 3, with the cases of S1 to S5 | Each new case is shown red against `136cfca25` or with the guard it names removed, as `frame/design.md` S1 to S5 say, and the phase record names how. `frame/design.md` S7's `bin/test` line passes. The orchestrator runs S9's probe at the phase's commit and reads S9's count for phase 1, and runs S8's dispatch. | |
| 2 | *Scope* items 4, 5 and 6, with the case of S6; the crafter writes `changelog.md` and moves the version in one commit | S6's case is shown red against phase 1's per-file reads. `Test_blobs` passes unchanged. S7's `bin/test` line passes. `git grep -n -E '^def decoded' -- lib skills` names `lib/gitcmd.py` alone. The orchestrator runs S9's probe and reads S9's count for phase 2, and runs S8's dispatch. S10 holds. | |

## Overlap with the release

The spawn names no other open work item of `release: 0.38.7`, and this is its first and only planned pull request, so no item meets this work.

## Operational impact

No migration, environment variable or dependency. `lib/gitcmd.py` keeps standard library only and Python 3.9 syntax. `seal settle`, `seal pr-body` and the pull request check keep their arguments, output and exit codes. The version moves from `0.38.6` to `0.38.7` in phase 2's commit that adds `changelog.md` (`frame/design.md` G6).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
