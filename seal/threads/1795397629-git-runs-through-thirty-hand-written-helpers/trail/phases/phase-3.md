# Phase 3: 1795397629-git-runs-through-thirty-hand-written-helpers

## What this phase found

**The frame held for phase 3, with five departures.** Each claim below was judged against `frame/design.md` and `frame/plan.md` as they stand at `dec3fcb12`, and against the tree there. `skills/settle/` did not change between `d0b15b72f` and `dec3fcb12` (executed: `git diff --quiet d0b15b72f -- skills/settle` exited 0 before the build), so the frame's coordinates in `settle.py` and `rule_changes.py` held as written.

- Executed: `git grep -nE "subprocess\.(run|Popen|call|check_call|check_output)\(" d0b15b72f -- skills/settle/scripts/` prints 12 lines: the nine calls of `settle.py` that *Scope* item 5 lists, and `rule_changes.py:686`, `:720` and `:733`. The same search over the tree at `dbafadd5f` prints nothing and exits 1.
- Read: both scripts loaded `lib/gitcmd.py` before this phase, `settle.py` at first use in `git_run` and `git_fields`, and `rule_changes.py` in its `gitcmd` getter. So the class phase 1 found, a case that copies a script without `lib/gitcmd.py`, gains no instance here. `Test_module::test_a_script_copied_alone_exits_2_and_names_what_it_misses` copies `settle.py` alone, and it still fails first on `lib/sibling.py`. The method was `git grep` over `tests/` for `settle.py` and `rule_changes.py` beside `copy`, `copied`, `shutil` and `alone`, which printed no other copy. That list is a sample, for the reason phase 1 gives.

**The departures.**

- **`settle.py#GH` goes with `GH_TIMEOUT`.** *Scope* item 5 names `GH_TIMEOUT` alone. `GH` was the program `shutil.which` looked for in `ask_gh`. `lib/gitcmd.py#gh` finds `gh` itself, so a `GH` kept would name a program that selects nothing. The two `asked` strings now spell `gh`. The grounds are `skills/core/SKILL.md` *The rule a mechanism is kept against*: a change removes in the same commit what stood on the old fact. The case that set `settle.GH` to a missing program, `test_refuses_a_gh_that_cannot_be_asked_in_local_mode[absent-*]`, now makes `shutil.which` find no `gh` through `gitcmd.shutil`, and git is still found.
- **The lines of a `gh` that could not start move to the runner's line.** At `d0b15b72f` `ask_gh` said `` `gh` is not on PATH `` and `` `gh pr list --head feat/1-a` did not run (…) ``. It now gives `Unasked` the runner's line, such as `` `gh pr list --head feat/1-a --state merged --json number,mergeCommit` could not be run: `gh` is not on PATH ``. The `absent` rows of that case pin the new line, as rule 14 of the agent contract asks. The grounds are the ones phase 2 gives for `seal export`'s line: the runner's line is the one statement of a command that did not answer, and a wrapper would state it twice. A non-zero exit keeps `ask_gh`'s own line, `` `gh pr list --head feat/1-a` exited 4: … ``, because design *Scope* item 5 keeps the readings of a non-zero exit.
- **`settle.py` loads `lib/gitcmd.py` at import.** `frame/plan.md` *Technical context* reads `settle.py`'s `sibling.load(GITCMD)` at each call. `settle.py` loads `lib/optin.py` at import, and `lib/optin.py` imports `gitcmd` at import already (`lib/optin.py:40`), so the load costs no file. `main` needs the class `Failed` to catch it.
- **`main` is split.** `main` parses the arguments and refuses the flags that cannot stand together, as before. The rest of the run is `_settled(args)`, and `main` calls it inside `except gitcmd.Failed`, which writes `settle: ` and the runner's line and returns 2 (design S7). The alternative, one `try` around the whole body, re-indents about 80 lines of the run and changes nothing they do. `_settled` is private, so it needs no `Test_` class (`CONTRIBUTING.md` *The test layout*).
- **Two test files outside the plan row changed, each because a check read the new cases.**
  - `tests/text/test_a_cited_commit_outlives_the_squash.py` refused the four new docstrings that cited `d0b15b72f`. That commit is on this branch alone, so the citation stops opening when the branch squashes. The docstrings now say `settle.py` and `rule_changes.py` before #1573. **The later phases meet the same check**: a case's text cites the issue, never a commit of this branch. The phase records may cite one, since `seal/` is outside that check.
  - `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` counted the S7 case as a scope that lists paths from git, because its `parametrize` holds the constants `ls-tree` and `ls-files`. The case lists no path and opens none. The census asks for each scope it finds to be classified with its grounds, so the case has a row in `OPENS_NOTHING`. Rule 18 of the agent contract asks a check that refuses correct code to be fixed or reported. The census is not wrong here: its words are kept wide on purpose, and the row is its own remedy.

**Decisions settled while writing the code.**

- **What each reader gives for `Failed`.** `show`, `released`, `resolves`, `git_run` and `git_fields` keep their readings of a non-zero exit, as *Scope* item 5 asks, and let `Failed` reach `main`. `ask_gh` reads `Unrun` as `Unasked`, so a `gh` past the bound in local mode ends in `UNASKED`, and under `--apply` in `RELEASES_UNASKED`. Both exit 2, as design *Data & interfaces* lists `settle.py#ask_gh` among the readers with a documented reading. Every other git read reaches `main`.
- **`rule_changes.py#order` and `#merge_order` pass `check=True`.** The `Exited` they raise is a `Failed`, so it reaches `settle.py#main` as one line at exit 2. Their docstrings say so.
- **`reaches` became `gitcmd.is_ancestor(root, c, ref)`.** The arguments are in the runner's order, commit then ref, where `reaches` took the ref first.
- **`tracked_names` and `tracked_text` read through `git_fields`.** Their `ls-files -z` now carries `--literal-pathspecs` and `argv`'s `-c` pairs, and has no pathspec for the flag to change. A git that exits non-zero still gives no names and no files, as before.
- **The module docstring's exit codes name the new cause of exit 2**: a git command that could not start or did not finish within `lib/gitcmd.py#TIMEOUT`, or that exits non-zero on the history the merge order is read from, said in one line. A `gh` past the bound is named beside the `gh` that is not on PATH. Rule 14 of the agent contract asks for that, and the S7 cases pin the line.
- **`decoded`'s docstring** cites `lib/gitcmd.py#git`'s text mode rather than `subprocess.run`'s, which the script no longer calls.
- **`frame/questions.md` Q2, answered by the work for phase 3.** `settle.py` and `rule_changes.py` no longer import `subprocess`. No case patched `settle.subprocess` or `rules.subprocess` (executed: `git grep -nE "settle\.(subprocess|GH|reaches|shutil)|rules\.subprocess"` over `tests/` printed nothing before the build). `tests/skills/test_settle.py#calls` patches the `subprocess` module itself, and so does the new helper `unanswered`. That is the one object `lib/gitcmd.py#_start` calls, so both hold wherever the scripts' imports end up. No case asserted a moved call's argv.

**Seen red and mutation claims.** Executed. Each new case, and each pin that moved, was run against `settle.py` and `rule_changes.py` as they stood at `dec3fcb12`, the same bytes as `d0b15b72f`, with the new cases in place. All 16 failed:

| Case | Red against the old scripts |
|---|---|
| `Test_main::test_refuses_a_git_that_did_not_answer_in_one_line`, rows `released`, `show`, `order`, `unordered`, `tracked_text`, `from`, `apply`, `draft` (S7) | `subprocess.TimeoutExpired` raised out of `main` |
| `Test_main::test_refuses_a_git_or_gh_that_did_not_answer_in_local_mode`, rows `resolves`, `reaches`, `merge_order` (S7) | `subprocess.TimeoutExpired` raised out of `main` |
| the same case, row `gh` | the line `` `gh pr list --head feat/1-a` did not run (Command '[…]' timed out after 60 seconds) `` in place of the runner's |
| `Test_main::test_refuses_a_gh_that_cannot_be_asked_in_local_mode`, rows `absent-report` and `absent-apply` | the old line `` `gh` is not on PATH `` |
| `Test_module::test_merge_order_refuses_a_history_git_did_not_print` and `::test_merge_order_of_local_specs_refuses_a_history_git_did_not_print` | `DID NOT RAISE Exited` |

`bin/seal mutate` at `019751544` and `2633ad9fb`, each mutant in a call of its own with `-p no:xdist -x` and a `-k` over the cases named, so that each red names its case. The first batched call of ten `settle.py` mutants under the workers read 8 red and 2 `SURVIVED`, without naming the cases; the calls below name them.

| Unit | Mutant | Verdict, and the case that failed |
|---|---|---|
| `main`, the handler | `except gitcmd.Failed` to `except ZeroDivisionError` | red, `test_refuses_a_git_that_did_not_answer_in_one_line[released]` |
| `main`, the line | `unanswered.line` to `unanswered.command` | red, the same case |
| `ask_gh`, the handler | `except gitcmd.Unrun` to `except ZeroDivisionError` | red, `test_refuses_a_gh_that_cannot_be_asked_in_local_mode[absent-report]` |
| `ask_gh`, the line | `Unasked(unrun.line)` to `Unasked(str(unrun.command))` | red, the same case |
| `released_local`, the reach | `is_ancestor(root, c, ref)` to `is_ancestor(root, ref, c)` | red, `test_local_specs_are_listed_in_the_order_their_pull_requests_merged` |
| `tracked_names` | `ls-files -z` to `ls-files` | red, `Test_report::test_every_open_row_is_listed_with_the_paths_it_names` |
| `tracked_text` | the listing cut to its first name | red, `Test_tracked_text::test_accepts_each_tracked_text_file_and_no_untracked_one` |
| `resolves` | the ref asked replaced by `HEAD` | red, `test_a_released_at_ref_that_does_not_resolve_is_refused_in_local_mode` |
| `git_fields` | `--literal-pathspecs` taken out | SURVIVED, then red after `2633ad9fb`, `test_a_named_directory_is_read_as_its_name_and_never_as_a_pattern` |
| `git_run` | `--literal-pathspecs` taken out | SURVIVED (`gaps.md` *Not done*) |
| `rule_changes.py#order` | `check=True` to `check=False` | red, `test_merge_order_refuses_a_history_git_did_not_print` |
| `rule_changes.py#merge_order` | `check=True` taken out | red, `test_merge_order_of_local_specs_refuses_a_history_git_did_not_print` |
| `rule_changes.py#_ancestor` | the runner's answer replaced by `False` | red, `test_two_specs_on_one_sentence_are_one_group_in_merge_order` |

Both survivors stood at `d0b15b72f` as well: no case held `--literal-pathspecs` before the phase moved the calls that carry it. The new case for `git_fields` runs `--from 'a*'` beside a directory `ab`, which the name read as a pattern also matches. On Windows it is skipped, because `*` is not a character a name can hold there. A case for `git_run` would need a work item id or a path that git reads as a pattern, and it was not written (`gaps.md` *Not done*).

**The phase boundary run.** Executed: one `bin/test -q` over the plan row's files `tests/skills/test_settle.py` and `tests/skills/test_rule_changes.py`; `tests/text` and `tests/behaviour`, which `CONTRIBUTING.md` names as the tree-wide files; `tests/test_censuses.py`; and the test files that load a script that loads `settle.py` or `rule_changes.py`, or run `seal settle` (`tests/skills/test_chain_check.py`, `test_rules.py` and `test_seal.py`, `tests/github/test_finding_counts.py`, `test_publish_release_note.py` and `test_tag_release.py`, and `tests/lib/test_config.py`, `test_items.py`, `test_lines.py` and `test_tables.py`). At `2633ad9fb` it gave `3 failed, 3187 passed, 9 skipped`: the citation check and the two cases of the path-listing census, each named under the last departure. At `dbafadd5f` the same command gave `3190 passed, 9 skipped`.
