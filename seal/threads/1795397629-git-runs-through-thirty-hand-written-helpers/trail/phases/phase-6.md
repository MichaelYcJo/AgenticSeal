# Phase 6: 1795397629-git-runs-through-thirty-hand-written-helpers

## What this phase found

**The frame held for phase 6, with three departures.** Each claim below was judged against `frame/design.md` and `frame/plan.md` as they stand at `a27e09a80`, the merge of `origin/release/v0.38.6` that brought #1578 and #1577 in, and against the tree there. Phase 6 was built before phase 5, as `frame/plan.md` *Judgments of the run* decides, so phase 5's Status cell is empty and none of its units changed here. Under `skills/verify/scripts/` this phase changed the path spelling of *Scope* item 9 alone, in `pact_check.py`, `seal_stamp.py` and `test_layout.py`.

- Read: the frame's coordinates are dated to `d0b15b72f`, and each was located again at `a27e09a80` before it was changed. *Scope* item 9's lines stand at `seal.py:376`, `:685` and `:1350` and `settle.py:1128` and `:1573` there, where the design gives `:378`, `:687`, `:1352`, `:1161` and `:1606`. The other nine lines stand where the design gives them.
- Executed: before the build, design S10's first search over `.github/scripts/` and `evals/scripts/` printed the calls *Scope* item 8 names and `noninferiority.py`'s run of `claude`, S11's `GH_TIMEOUT` search printed nothing, and S12 printed `tag_release.py:61`.

**The departures.**

- **The closer's `run` asks `gitcmd.git` at `os.curdir`, not at the repository's top.** Design *Scope* item 8 says `run` hands its git arguments to `gitcmd.git` "at the repository's top". Read: the old `run` ran `gitcmd.argv(...)` with no `-C`, so git ran in the caller's directory; the three callers (`close_issues_on_release.py#arrived`, twice, and `release_completeness_check.py#subjects_since`) pass no directory; and both workflows that run the scripts (`.github/workflows/close-issues-on-release.yml:40`, `hygiene.yml:164`) start them at the checkout's top, so `os.curdir` is the repository's top on every run the workflows make. `Test_run` drives `run` in a fixture repository it changes into, which a path taken from the script's own location would not reach. Phase 4 made the same choice for `pr_wait.py#head`. `release_seal.py#tagged` asks `gitcmd.git` at `os.curdir` for the same reason; the design names no directory for it.
- **`publish_release_note.py#commit_message` now runs git at `ROOT`, where it ran in the caller's directory.** Every other git read of the script already ran at `ROOT` through its `git`, and `commit_message` was the one read spelt through the removed `run`. It now asks the same `git`. In the publish workflow the caller's directory is the checkout's top, which is `ROOT`, so the read gives the same answer there. The grounds are `skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has one source.
- **`test_layout.py` loads `lib/sibling.py` at import, for `git_path`.** At `a27e09a80` it loads nothing from `lib/` (design G17). It now puts `lib/` first on `sys.path` and imports `sibling` bare, as `unverified_check.py` beside it and `evals/scripts/rule_cases.py` do, and loads `lib/gitcmd.py` at import. Phase 5 adds `lib/optin.py` and the runner's `git` through the same load. Read: no case copies `test_layout.py` on its own, since the one copy in `tests/skills/test_test_layout.py` (`:731`) copies a fixture repository, and `tests/behaviour/test_every_tracked_file_meets_every_census.py:22` loads it from the tree and passed.

**Decisions settled while writing the code.**

- **The label removal reaches `gitcmd.gh` through `attempt`.** Design *Scope* item 8 says the label removal at `:182` runs through `gitcmd.gh`. `drop_label` calls `attempt("gh", "issue", "edit", …)`, and `attempt` asks `gitcmd.gh`. The census in `tests/github/test_close_issues_on_release.py` reads the literal argv words of the closer's source and asks for exactly one `gh issue edit` with the flags `--repo` and `--remove-label`. A direct `gitcmd.gh("issue", "edit", …)` call spells no `"gh"` word, and the census would read no call.
- **`run` and `attempt` share `_asked(program, args, check)`,** which hands `git` to `gitcmd.git`, `gh` to `gitcmd.gh`, and raises `ValueError` for any other program. A caller that hands `run` another program is a defect in the caller, and a `ValueError` names it.
- **What each script gives for `Failed`.** `run` lets it reach the caller with the runner's line, at exit 1; `attempt` reads it as `(False, line)`. `publish_release_note.py`'s milestones list and pull request list read `Unrun` as their reading of a failed `gh`, with the runner's line where they printed `gh`'s stderr; the release lookup lets `Unrun` stop the run, as its non-zero exit already did; `git` and the create pass `check=True` and stop in the runner's line. `tag_release.py#create` reads `Unrun` as its error string. `roll_flow_measurement_issue.py#try_run` reads `Failed` as `None`, and the list, the close and the last create rung pass `check=True`. `release_seal.py#gh` and `#tagged` read `Failed` as `Refused` with the runner's line. `dist_branch.py#git` keeps `GitFailed` for a non-zero exit and lets `Unrun` stop the run. `plugin_directory_check.py#is_ancestor` reads `Failed` at any of its three steps as `None`. `noninferiority.py#git_bytes` passes `check=True`, so a non-zero exit and a git that gave no answer both stop the run in the runner's line.
- **The four pins of `noninferiority.py`'s old line moved to the runner's line,** in the commit that changed the line, as rule 14 of the agent contract asks: `Test_git_bytes::test_refuses_a_git_that_exits_otherwise`, `Test_extract::test_refuses_a_rev_git_does_not_resolve` and `test_refuses_a_path_the_rev_does_not_hold`, and `Test_suite_tree::test_refuses_an_agent_with_no_suite_there`.
- **`Test_run` of `tests/github/test_roll_flow_measurement_issue.py` is removed with the `run` it tested,** as design *Removes* lists. The runner's `gh` is held by `tests/lib/test_gitcmd.py#Test_gh`, and `Test_try_run` was rewritten over the suite's `gh` stub.
- **`seal layout --pairs` names three pairs this phase wrote.** `Test_try_run`'s two cases call `try_run` with equal arguments and differ in the state of the `gh` stub; `tests/lib/test_console.py#Test_write_output`'s two cases call `write_output` with equal arguments and differ in `GITHUB_OUTPUT`. Each pair is an accepting and a refusing case of one call in two worlds, which is what each case is about, so the pair is the layout's notice and not a duplicate. The other four pairs it prints over the changed files predate this phase.
- **`frame/questions.md` Q2, answered by the work for phase 6.** Each script that dropped `import subprocess` has its cases patch `mod.gitcmd.subprocess.run` or the `subprocess` module itself, the one object `lib/gitcmd.py#_start` calls (`tests/github/test_close_issues_on_release.py`, `test_publish_release_note.py`, `test_release_seal.py`, through `tests/skills/test_settle.py#unanswered`). `test_roll_flow_measurement_issue.py` patches `m.gitcmd.gh` through its helper `_run`, since every call it answers is a `gh` call. `release_seal.py`'s argv assertion compares against `gitcmd.argv("-C", os.curdir, …)`, so it follows the runner's `-c` pairs.

**The searches the plan's Verified by cell names, at `ae600e8d0`.** Executed.

- S10's first search prints 18 lines. Those it allows: `noninferiority.py:401` (`claude`), `seal.py:2508` (`hand_over`'s `subprocess.call`), `broad_gate.py:980` (`run`), `:2271` (a shipped script) and its comment lines `:718` and `:736`, `mutation_check.py:405` and `test_layout.py:1037` (pytest). Phase 5 owes the other ten: `broad_gate.py:244` (`git`) and `:1506` (the worktree removal), `pact_check.py:287`, `seal_stamp.py:1010`, `session_cost.py:2776` and `:3094`, `test_layout.py:1062`, `:1162` and `:1174`, and `unverified_check.py:206`. Nothing under `.github/scripts/`, `lib/` or `evals/scripts/` is among them. S10's second search prints nothing.
- S11's first two searches print nothing. The third prints `plugin_directory_check.py:191`, which *Scope* item 8 keeps, and four lines phase 5 owes: `broad_gate.py:253` and `:258`, `test_layout.py:1160` and `unverified_check.py:204`.
- S12 prints nothing.

**Seen red and mutation claims.** Executed. Each new case below, and each pin that moved, was run against the script as it stood before its commit, with the new cases in place:

| Case | Red against the old script |
|---|---|
| `tests/lib/test_console.py#Test_write_output`, both cases | `AttributeError`: `lib/console.py` had no `write_output` |
| `test_close_issues_on_release.py#Test_run::test_refuses_a_failed_call_by_exiting_in_the_runners_line` | the old line `git rev-parse --verify nowhere failed: fatal: …` |
| `Test_module::test_attempt_answers_a_write_that_gave_no_answer_as_refused` | `subprocess.TimeoutExpired` raised out of `attempt` |
| `test_publish_release_note.py#Test_module::test_a_gh_that_gave_no_answer_is_read_as_each_read_reads_a_failure`, `test_a_git_read_that_fails_stops_the_run_in_the_runners_line` | `TimeoutExpired`, and the old `git … failed` line in place of the runner's |
| `test_tag_release.py#Test_create::test_refuses_without_gh_and_says_so` | `AttributeError`: the old script had no `gitcmd` to patch |
| `Test_create::test_refuses_a_command_that_gave_no_answer_and_names_it`, rows `gh api` and `git tag` | `TimeoutExpired` raised out of `create` |
| `test_release_seal.py#Test_module::test_a_refused_gh_or_git_call_is_a_reason_naming_the_call` | the argv the old `tagged` ran lacked the runner's `-C .` and `-c` pairs |
| `Test_module::test_a_gh_or_git_call_that_gave_no_answer_is_a_reason_naming_it` | `TimeoutExpired` raised out of `gh` |
| `test_dist_branch.py#Test_main::test_refuses_a_push_that_gave_no_answer_in_the_runners_line` | `TimeoutExpired` raised out of `main` |
| `test_plugin_directory_check.py#Test_module::test_a_commit_this_clone_does_not_have_is_not_called_unreachable`, its no-answer rows | `TimeoutExpired` raised out of `is_ancestor` |
| `test_noninferiority.py`, the four moved pins and `Test_git_bytes::test_refuses_a_git_that_gave_no_answer_in_the_runners_line` | the old `git <args>: <stderr>` line, and `TimeoutExpired` |

`test_roll_flow_measurement_issue.py`'s new cases were not run against the old script, whose missing `gitcmd` would have failed them on the patch alone; the mutants below show what holds each reading. `test_publish_release_note.py#Test_module::test_a_create_gh_refuses_stops_the_run_in_the_runners_line`, `test_the_list_is_read_from_the_release_branch`'s new assertions and `test_roll_flow_measurement_issue.py#Test_module::test_a_list_gh_refuses_stops_the_release_in_the_runners_line` were added for a mutant that survived, and each is red on that mutant.

`bin/seal mutate`, after the commit of each unit, with `-p no:xdist -x` and a `-k` over the cases named. Every run read `red` except the three marked:

| Unit | Mutant | Red on |
|---|---|---|
| closer `_asked`, git's directory | `os.curdir` to `os.pardir` | `Test_run::test_accepts_a_git_or_gh_call_and_answers_what_it_printed` |
| `_asked`, the `gh` branch | `gitcmd.gh` to `gitcmd.git` | the same case |
| `_asked`, another program | the `ValueError` to `gitcmd.gh` | `Test_run::test_refuses_a_failed_call_by_exiting_in_the_runners_line` |
| `run` | `check=True` to `check=False` | the same case |
| `attempt`, the handler | `except gitcmd.Failed` to `except ZeroDivisionError` | `Test_module::test_attempt_answers_a_write_that_gave_no_answer_as_refused` |
| `attempt`, the line | `failed.line` to `""` | the same case |
| `drop_label`, the argv | `--remove-label` to `--add-label` | `Test_main::test_the_close_comes_first_so_a_failed_label_write_cannot_cost_it` |
| `drop_label`, the answer | `return ok` to `return True` | `Test_main::test_an_already_closed_issue_reports_no_removal_that_failed` |
| `_issue_api`, the URL | `issues/` to `issue/` | SURVIVED, at `d0b15b72f` too; `gaps.md` *Not done* |
| `publish_release_note.py#git` | `check=True` to `check=False` | `Test_module::test_a_git_read_that_fails_stops_the_run_in_the_runners_line` |
| `commit_message` | `--format=%B` to `--format=%s` | SURVIVED, then red on `Test_main::test_the_title_is_the_line_the_checklist_prescribes` after `41f6da373` |
| `milestone_description`, the handler and the line | `except gitcmd.Unrun` to `except ZeroDivisionError`; `{unrun.line}` dropped | `Test_module::test_a_gh_that_gave_no_answer_is_read_as_each_read_reads_a_failure` |
| `merged_pulls`, the handler and the line | the same two | the same case |
| `merged_pulls`, a refusal's stderr | `said = None` | SURVIVED, then red on `Test_module::test_the_list_is_read_from_the_release_branch` after `41f6da373` |
| `create` | `check=True` to `check=False` | SURVIVED, then red on `Test_module::test_a_create_gh_refuses_stops_the_run_in_the_runners_line` after `41f6da373` |
| `tag_release.py#create`, the handler and the line | `except gitcmd.Unrun` to `except ZeroDivisionError`; `unrun.line` to the old sentence | `Test_create::test_refuses_without_gh_and_says_so` |
| `tag_release.py#git` | `ROOT` to `os.curdir` | `Test_main::test_accepts_a_push_that_moved_the_version_by_creating_the_tag` |
| `roll_flow_measurement_issue.py#try_run`, the handler and the exit | `except gitcmd.Failed` to `except ZeroDivisionError`; `None if out.returncode else` dropped | `Test_try_run::test_refuses_a_failed_calls_output_as_none`, rows `timeout` and `exit 1` |
| `list_open_issues` | `check=True` to `check=False` | SURVIVED, then red on `Test_module::test_a_list_gh_refuses_stops_the_release_in_the_runners_line` after `d80f37fb7` |
| the last create rung | `gitcmd.gh(..., check=True)` to `try_run(...)` | `Test_main::test_both_best_effort_arguments_failing_still_opens_the_issue` |
| `close_issue` | `gitcmd.gh` to `try_run` | `Test_main::test_accepts_one_open_issue_and_closes_it_and_opens_the_next` |
| `release_seal.py#gh`, `#tagged` the handlers; `#tagged` the directory | `except gitcmd.Failed` to `except ZeroDivisionError`, each; `os.curdir` to `os.pardir` | `-k 'a_refused_gh or gave_no_answer'` |
| `dist_branch.py#git` | the index's `env` to `None`; `given=stdin` to `None`; `binary=True` to `False` | `tests/github/test_dist_branch.py` with `-x` |
| `plugin_directory_check.py#is_ancestor`, the handler | `except gitcmd.Failed` to `except ZeroDivisionError` | `-k not_called_unreachable` |
| `is_ancestor`, the last step | `(root, sha, ref)` to `(root, ref, sha)` | SURVIVED, then red on `Test_module::test_a_commit_this_clone_does_not_have_is_not_called_unreachable` after `5a4edd844` |
| `noninferiority.py#git_bytes` | `check=True` to `check=False`; the index's `env` to `None`; `given=stdin` to `None` | `tests/evals/test_noninferiority.py` with `-x` |

The rows from `release_seal.py` on ran in one `bin/seal mutate` call each, which prints a verdict per mutant and no case name, so the cell names the cases the run was given.

*Scope* item 3 moved `write_output` with its body unchanged, and *Scope* item 9 replaced 14 spellings with `gitcmd.git_path`, which gives the same answer on every platform. Neither adds behaviour, so neither owes a mutant (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*). Executed, the census each asks for: S12 prints nothing; `git grep -n "write_output" -- .github lib` names `lib/console.py`, the comment at `.github/workflows/publish-release.yml:67`, and the calls in `publish_release_note.py` and `tag_release.py` alone; S11's first search prints nothing. The existing cases of every file whose spelling changed passed at `ae4092def` (`tests/github/test_finding_counts.py`, `test_release_report.py`, `tests/skills/test_seal.py`, `test_rules.py`, `test_settle.py`, `test_pact_check.py`, `test_seal_stamp.py`, `test_test_layout.py`: 1092 passed).

**The phase boundary run.** Executed at `ae600e8d0`: one `bin/test -q` over the plan row's files `tests/lib/test_console.py`, `tests/github`, `tests/evals/test_noninferiority.py` and `tests/skills/test_rules.py`; `tests/lib/test_gitcmd.py`; the test files of the scripts whose path spelling changed, `tests/skills/test_seal.py`, `test_settle.py`, `test_pact_check.py`, `test_seal_stamp.py` and `test_test_layout.py`; and `tests/behaviour`, `tests/text` and `tests/test_censuses.py`. It gave `3005 passed, 9 skipped`. `312c8dbd6` rewraps one docstring of `tests/github/test_close_issues_on_release.py#argv_words` after it, and that file, `tests/text` and `tests/test_censuses.py` passed again there. The suite, the lint and the typecheck over the whole tree were not run in this phase: unverified.
