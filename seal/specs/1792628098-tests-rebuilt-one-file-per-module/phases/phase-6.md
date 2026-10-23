# Phase 6: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | not closed; its first step is 6e7214be, extended to the two sets at 43324e4e |

## What this phase was asked

The first spawn: `bin/test-layout --moved <base> --from <old file>... <new file>` in `skills/verify/scripts/test_layout.py`, with `tests/test_test_layout.py::Test_moved` seen red first (S11), the mode named in `bin/test-layout`'s comment and the script's docstring, and the record-shape bullet of `CONTRIBUTING.md` *The test layout* rewritten in place: the mutant table is the part of a record whose module the check did not pass, the sentence `about 30 per module` gives way to the rule `spec.md` *The proof of equal protection* states, and the clause `before the old cases are read` is dropped. Then Batch B, every remaining shipped module, one commit per shipped directory in `plan.md`'s order, `hooks/` first, stopping at a directory boundary. Per module the move check runs: where it exits 0 the record holds its command and last line, and where it exits 1 the module runs the mutation proof as in phase 5.

The second spawn, after the framer's amendment at 3ad42cb3: extend `--moved` from one new file to the two sets `--from <old file>... --to <new file>...`, with S12 and S13's rows of `Test_moved` seen red first and every `Test_moved` row run with `--to`; rewrite the spelling in `bin/test-layout`'s comment, the script's docstring and `CONTRIBUTING.md` *The test layout*'s record-shape bullet, and remove the one-new-file form; run the mutation proof for the changed code in one batch; one commit. Then Batch B from `hooks/` (31 modules left), one commit per shipped directory or per smaller group rebuilt together; per `questions.md` Q8's default, one check run per commit, narrowed to the modules that share the failing old files where it exits 1. Per group: the four rules, then the move check; where it exits 0 the record holds its command and last line; where it exits 1, each failure line is read first, a move not meant is repaired, and the mutation proof runs per module for what remains failing. `hooks/cmdline.py`'s cases in the three text-reading files stay sampled per kind under Q1, and #1014 decides their future. A case that pins a module of a later group stays in its old file. Stop at a group boundary where the next group cannot be finished with a complete record; the order inside `hooks/` is the smith's, with the reason stated.

## What this phase found

**Whether the frame holds.** It holds for the move check as built. It does not hold for Batch B as the frame expects the check to be used, below.

**The move check, at 6e7214be** (`executed`, macOS arm64). `test_layout.py` gains `moved`, the pure reading of the body and fixture conditions, and `_moved_main`, which reads the old files with `git show`, collects both sides with pytest and prints the result. The three conditions are `spec.md`'s, with these readings the build took:

- The census case is left out on both sides of the count, not on the new file's alone. A phase 5 file that gains moved cases is named in `--from` too, and at the base it already holds its census case.
- A case requests a fixture by a parameter, by a `usefixtures` mark on the case, on its class or in the file's `pytestmark`, and as an autouse fixture of its class, its file or `tests/conftest.py`. The names a `parametrize` mark hands a case are not fixtures. The two cases must request the same names, and each name, followed through the fixtures it requests, must be defined alike in both trees. A case moved out of a class that carried `usefixtures` therefore fails, though its body is unchanged.
- A fixture is read in the case's class, then its file, then `tests/conftest.py`, as `spec.md` says. A conftest under a subdirectory of `tests/` is not read; none exists at 6e7214be. A fixture renamed through `name=` is read under its function's name; no test file uses `name=` (`git grep`, `executed`).
- `questions.md` Q6 and Q7 are built on their defaults: the base is collected in a detached worktree, removed by its own path with `git worktree remove --force` before the check ends, and a name no tree defines is pytest's own.
- pytest runs on the interpreter running the check where it has pytest, and on the repository's `.venv` otherwise, because `bin/test-layout` runs on the system `python3`, which has no pytest on this machine (`executed`). Neither found is exit 2.
- At 6e7214be `--from` took every word after it and its last word was the new file, the spelling `spec.md` gave then. 43324e4e replaced it with `--to` (below).

S11, seen red and then green (`executed`). Before the mode existed, all six cases of `Test_moved` failed with `one of the arguments --check --pairs is required`. As committed, `Test_moved` holds `test_accepts_a_pure_move`, `test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture` with nine rows (a cut, a merge, two alike cases merged into one, an edited body, a changed conftest fixture, a changed class fixture, a lost autouse, a fixture left behind in the old file, and a fixture the new file shadows), and `test_refuses_a_base_or_an_old_file_it_cannot_read`. One world is built for the module, a repository with two old files and a conftest at its base commit, and each case writes its new file into a copy of it.

The mutation table, one `bin/mutation-check` batch over `skills/verify/scripts/test_layout.py` with `--tests "bin/test tests/test_test_layout.py -q -p no:xdist -x -k Test_moved"`, at the tree committed as 6e7214be: 24 mutants, 24 red, in 45.4 s. The first run of the batch, on a draft, had four survivors. Each now has a row or a changed unit: v17 the row with a decorated helper named as a fixture, v21 the worktree removed by its path in place of a prune, v23 the row `two-alike-merged`, v24 the row `a-changed-class-fixture`.

| # | Mutation | Verdict |
|---|---|---|
| v1 | the count not compared | red |
| v2, v3 | the census case counted; the collection read past its ids | red |
| v4 to v7 | every form equal; `self`, the docstring or the name kept in the form | red |
| v8 to v11 | parametrized names requested; class `usefixtures`, `pytestmark` or autouse ignored | red |
| v12 to v16 | the requested sets not compared; dependencies not followed; definitions not compared; a fixture defined at the base only or in the working tree only passed | red |
| v17, v18 | any decorator a fixture; autouse read from nothing | red |
| v19, v20 | a base that names no commit passed; an old file the base lacks passed | red |
| v21 | the base's worktree left behind | red |
| v22 | the new file not taken from `--from`'s last word | red |
| v23, v24 | one new case standing for two old ones; a class's fixtures not read | red |

**Cases and seconds** (`executed`, `bin/test tests/test_test_layout.py -q`, the parallel runner). Before, at ac965ee7: 36 cases. After, at 6e7214be: 47 cases in 2.4 s; `Test_moved`'s eleven run in 3.1 s serial. One run of the check over this repository, `bin/test-layout --moved HEAD --from tests/test_seal.py tests/test_seal.py`, printed `test-layout: moved: 159 old cases, 314 items against 314 at ac965ee77d86, 0 failed` and took 1.5 s.

**Batch B did not start in the first spawn.** `hooks/`, the first directory, holds 34 shipped modules, three of them rebuilt in phase 5: `hooks/commit-review-gate.py`, `hooks/worktree-guard.py` and `hooks/root-migrate.py`. A scan of the 136 test files that declare no `TARGET` (`executed`, a script outside the tree that reads each file for a `hooks/` module's file name or import) finds 57 that name a `hooks/` module, 35 of them naming two or more. The directory also holds `hooks/cmdline.py`, whose cases phase 5 left in the commit gate's three text-reading files. One commit for the directory with complete records is more than this spawn can finish, so it stops at the directory boundary.

**What the frame's check cannot pass.** The count condition compares the new file with the whole of each `--from` file. An old file whose cases belong to two modules is split between two new files, and neither new file can then pass: each holds fewer items than the old file. So every module whose old cases share a file with another module's falls to the mutation proof, however its cases were only moved. If most of the 35 files above do split, the mutants `plan.md` *Alternatives considered* dropped for moved modules come back for most of `hooks/`. A check that takes several new files and compares their union with the old files would pass a split; `spec.md` *Data & interfaces* gave `--moved` one new file, so the first spawn did not build it. The orchestrator decided the set form on 2026-10-23, the framer wrote it into the frame at 3ad42cb3, and 43324e4e built it (below).

**The boundary** (`executed`). At the tree committed as 6e7214be, one `bin/test ... -q` over 42 modules: `tests/test_test_layout.py`; every test file naming `test_layout`, `test-layout` or `CONTRIBUTING`; `tests/test_censuses.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_conftest.py` and every other file `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists. 2,536 passed in 35.7 s. The shards module over the whole collection, `bin/test tests -q -k test_the_windows_leg_runs_in_shards_that_make_the_whole`: 32 passed and 1 failed, `test_the_durations_file_prices_the_suite`, the known red until phase 7. `bin/test-layout --check` exits 0 with 153 files read, 0 refused and 137 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats `skills/verify/scripts/test_layout.py` and `tests/test_test_layout.py` clean, one file per run, and `--pairs` names 0 pairs in `tests/test_test_layout.py`.

### The move check over two sets, at 43324e4e

**Whether the frame holds** (`read`). It holds for this step: `spec.md` *Data & interfaces*, S12, S13 and the *Removes* row agree with `main` at 3ad42cb3, whose `args.moved` branch popped the last `--from` word into the new file.

**What changed** (`executed`, macOS arm64). `main` takes `--to` as a second list. `--moved` without both lists, or with any path in neither, stops with argparse's exit 2, and so does `--to` or `--from` without `--moved`. `moved` reads every new file, files on each side in path order, and resolves a new case's fixtures in that case's own file. A new case that stands for no old case prints `moved: <new file>::<case>: body: stands for no old case`, so an old case that lands twice is named by its second landing. The count compares the items of all new files with the items of all old files at the base, and its line reads `the new files collect <n> items`. A new file that cannot be read exits 2.

**S12 and S13, seen red, then green** (`executed`). Against the script at 3ad42cb3, `Test_moved` failed 15 of its 17 cases: every row run with `--to` stopped on argparse's refusal, among them S12's two rows (`one-old-file-in-two-new-files`, `an-old-file-in-both-sets`) and S13's row `a-case-landing-twice`. The two that passed there, `a-path-after-the-lists` and `to-alone`, each failed on its mutant below. Built, `bin/test tests/test_test_layout.py -q -p no:xdist` gives 53 passed. Two rows of the refusing case changed their expected lines: `a-merge` and `an-edited-body` now also print the new case that stands for no old case, which is the second condition as `spec.md` states it.

| # | Mutation over `skills/verify/scripts/test_layout.py` | New column |
|---|---|---|
| m1 | the cases that stand for no old case not printed | red |
| m2 | the new files read in reverse path order | red |
| m3 | a new case's fixtures read in the last new file parsed | red |
| m4 | only the first new file collected | red |
| m5 | a path in neither list let through | red |
| m6 | `--moved` without `--to` let through | red |
| m7 | `--to` without `--moved` let through | red |
| m8 | a new file that cannot be read let through | survived, then red after a row |
| m9 | a surplus case named without its file | red |

One `bin/mutation-check` batch with `--tests "bin/test tests/test_test_layout.py -q -p no:xdist -x -k Test_moved"`: 9 mutants, 8 red, 1 survived, in 33.2 s. m8 survived because no case named a `--to` file that does not exist; `test_refuses_a_base_or_a_file_it_cannot_read` (renamed from `..._an_old_file_...`) gained that row and went red on m8 alone in 12.9 s. No old column ran: the one-new-file form had no `--to`, so its cases could not run these mutants.

### Batch B, `hooks/`, group 1, at 0a86c1b4

**The order inside `hooks/`** (`read`). The groups go from the modules whose cases sit in one old file of their own toward the modules whose cases are spread across many shared files (`hooks/config.py`, `hooks/gate.py`, `hooks/tokens.py`, `hooks/cmdline.py`, `hooks/blocks.py`, `hooks/dispatch.py`). A small group's check is short and a failure sends one small module to the mutants; each module placed early also leaves fewer cases in the shared files a later group has to read. A scan by name over the undeclared test files (`executed`, a script outside the tree) gave each module's candidate files; each group's membership is decided by reading the cases, and the scan over-reaches where a module's stem is a common word.

**The modules.** `hooks/lint-python.py`, `hooks/version-check.py`, `hooks/review-skill-gate.py`, `hooks/question-gate.py`. Each of their new files has the layout's name, and the first three keep their old file's name.

**The move check, over the group** (`executed`):

`bin/test-layout --moved 43324e4e --from tests/test_lint_python.py tests/test_version_check.py tests/test_review_skill_gate.py tests/test_an_automation_run_puts_no_question.py tests/test_gates_do_not_fail_open.py --to tests/test_lint_python.py tests/test_version_check.py tests/test_review_skill_gate.py tests/test_question_gate.py tests/test_gates_do_not_fail_open.py`

`test-layout: moved: 73 old cases, 74 items against 73 at 43324e4e104e, 17 failed`, exit 1. Narrowed to each module, since the four share no old file:

| Module | Narrowed check's last line | Failure lines |
|---|---|---|
| `hooks/lint-python.py` | `14 old cases, 14 items against 14 at 43324e4e104e, 7 failed` | five old cases merged into two parametrized cases |
| `hooks/version-check.py` | `18 old cases, 19 items against 18 at 43324e4e104e, 4 failed` | one old case split into its accepting and refusing case, and the count |
| `hooks/review-skill-gate.py` | `12 old cases, 12 items against 12 at 43324e4e104e, 3 failed` | two old cases merged into one parametrized case |
| `hooks/question-gate.py` | `29 old cases, 29 items against 29 at 43324e4e104e, 3 failed` | two old cases merged into one parametrized case |

Every failure line is a merge or a split made on purpose; no move needed repair. Question-gate's check exited 0 as first placed (`29 old cases, 29 items against 29 at 43324e4e104e, 0 failed`), before its pair was merged.

**Why the merges.** Placed in one class, the old cases became pairs `--pairs` names: lint-python's three config files and its two pyprojects without `[tool.ruff]`, review-skill-gate's two loops over skill names, and question-gate's two checkouts no declaration names. Rule 2 merges a case the pairs report names with another, so each pair became one parametrized case, and the module runs the mutants. Version-check's `test_an_untagged_remote_answers_rather_than_failing` held both halves of `latest`, so rule 1's pair split it. One pair is named and not merged: review-skill-gate's `test_refuses_the_builtin_so_the_user_is_offered_a_choice` and `test_accepts_our_own_skill` read alike once strings are normalised and assert opposite verdicts on two inputs, so neither covers the other.

**The mutation tables** (`executed`, one `bin/mutation-check` batch per module over the new file with `-x`; the old column in an archive of 43324e4e, against the old file, for the survivors only).

| Module | Mutants | New column | Old column | Old gaps |
|---|---|---|---|---|
| `hooks/lint-python.py` | 12 | 7 red, 5 survived | 5 survived | `resolve_runner`'s `uv` branch; a non-`.py` path past the suffix test; a missing runner; the stdin payload; a failing formatter. The last three cases build no ruff config, so `uses_ruff` returns first and the branch they name is never reached |
| `hooks/version-check.py` | 10 | 9 red, 1 survived | 1 survived | `running` with no plugin root |
| `hooks/review-skill-gate.py` | 9 | 7 red, 2 survived | 2 survived | `git` returning output on a non-zero exit; a payload that is not an object |
| `hooks/question-gate.py` | 9 | 9 red | not run | none |

The mutants sit at each class's decision points: lint-python's three config tests, the repository boundary and the root in `uses_ruff`, `resolve_runner`'s first branch, and `main`'s suffix, off switch, `uses_ruff`, runner, order, stdin and formatter-error branches; version-check's tag pattern, interval, retry back-date, `latest`'s exit and no-tag answers, the opt-in, the throttle, the retry call, the comparison and `running`'s root; review-skill-gate's skill name, opt-in, ask, already-asked, marker, session path, git dir join, `git`'s exit and the payload type; question-gate's `shown` fallback, the reason's path, the question count, the multi-select, the question text, the tool name, the automation row, the press reader and the alone test. No case was added: every survivor is an old gap.

**Cases and seconds** (`executed`, serial, pytest's own figure; before from an archive of 43324e4e with the worktree's `.venv`):

| Module | Before | After |
|---|---|---|
| `hooks/lint-python.py` | 14 in `tests/test_lint_python.py`, 0.14 s | 15 items, 0.15 s |
| `hooks/version-check.py` | 18 in `tests/test_version_check.py`, 0.57 s | 20 items, 0.90 s |
| `hooks/review-skill-gate.py` | 12 in `tests/test_review_skill_gate.py`, 1.01 s | 13 items, 0.96 s |
| `hooks/question-gate.py` | 29 in `tests/test_an_automation_run_puts_no_question.py` and `tests/test_gates_do_not_fail_open.py`, 3.29 to 3.73 s | 30 items in `tests/test_question_gate.py` and `tests/test_gates_do_not_fail_open.py`, 3.57 to 7.70 s over three runs of one tree |

Each "after" counts the census case.

**The real-git cases kept.** Version-check's `Test_latest::test_accepts_an_untagged_remote_as_an_answer` (a bare remote), review-skill-gate's every case (the hook runs in the `repo` fixture, and `Test_already_asked::test_accepts_a_linked_worktree_as_a_repository_too` adds a worktree), and question-gate's every case but the registration case: the gates resolve a branch and a git directory through git, and each case is a row where the reading and git agree.

**Left where they stand.** For #923: `test_the_notice_agrees_with_the_docstring_about_what_a_reload_re_reads` in `tests/test_version_check.py`, and `test_the_prose_points_to_the_gate_and_no_longer_says_nothing_holds_it` in `tests/test_question_gate.py`, each under its name. For `hooks/worktree_consent.py`: `test_the_press_reader_reads_nothing_for_a_root_that_is_no_clone`, under its name in `tests/test_question_gate.py`. For `hooks/optin.py`, in `tests/test_optin_home.py`: the two version-check cases and the review-skill-gate cases there, which pin how each hook reads the opt-in homes. `tests/test_gates_do_not_fail_open.py` keeps its other gates' cases; its `load` and `git_repo` moved to `tests/conftest.py`, so the question gate's case could move with its body unchanged.

**The boundary** (`executed`). At the tree committed as 0a86c1b4: the changed files and the files naming them, `tests/test_censuses.py`, every file the `git_listing` grep lists, `tests/test_chain_hooks_hardening.py`, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_the_guard_asks_once_per_session.py`, which the question gate's file imports, 31 files: 1,867 passed. The shards module: 32 passed and 1 failed, `test_the_durations_file_prices_the_suite`, the known red. `bin/test-layout --check` exits 0, 153 files read, 133 declaring no `TARGET`; `--pairs` names the one review-skill-gate pair above; `bin/rules --check` exits 0, 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean, one file per run.

### Batch B, `hooks/`, group 2, at ccca432d

**The modules.** `hooks/launch.py`, whose six cases were the whole of `tests/test_a_script_says_which_interpreter_it_needs.py`, now `tests/test_launch.py`; and `hooks/one_heredoc.py`, whose fourteen cases were the whole of `tests/test_one_heredoc_shape_is_read_exactly.py` and `tests/test_one_heredoc_shape_agrees_with_the_shell.py`, now `tests/test_one_heredoc.py`. No `check:` line names any of the three old files.

**The move check** (`executed`):

`bin/test-layout --moved 0a86c1b4 --from tests/test_a_script_says_which_interpreter_it_needs.py tests/test_one_heredoc_shape_is_read_exactly.py tests/test_one_heredoc_shape_agrees_with_the_shell.py --to tests/test_launch.py tests/test_one_heredoc.py`

`test-layout: moved: 20 old cases, 147 items against 147 at 0a86c1b4c088, 0 failed`, exit 0. No module of the group has a mutation table. `--pairs` names no pair in either new file.

**Where the cases went.** Launch: `Test_main` holds the run at the floor and the refusal below it; `Test_module` holds the refusal's ASCII, the floor's one source, the wrappers' launch and the set linted at the floor, each a property of the module as a whole. One_heredoc: every case of `reduce` and `_match` is in `Test_reduce`, the shell rows among them, and the import census is in `Test_module`. `FAILS` moved with its case, and `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py` now imports it from `tests/test_one_heredoc.py`.

**The names rewritten.** `hooks/launch.py`'s docstring, `ruff.toml`'s comment, `tests/censuses.py`'s comment, `CONTRIBUTING.md` *Running the checks* and the two `LISTS_A_FIXTURE` keys in `tests/test_a_shrunken_corpus_declines_to_judge.py` (`#floor_carriers`, `#before_any_floor`) name `tests/test_launch.py`; `hooks/one_heredoc.py`'s docstring names `tests/test_one_heredoc.py`. `tests/test_censuses.py`'s docstring still names the launcher's old file, as the place phase 3 took the floor census from, and stands.

**Cases and seconds** (`executed`, serial): launch, 6 cases in 0.37 s before and 7 items in 0.45 s after; one_heredoc, 141 items in 51.24 s before and 142 in 46.39 s after. The shell rows are almost all of one_heredoc's time on macOS, and `.test_durations` prices the two old files at 1.2 s, which is under rule 3's threshold.

**The real-shell rows kept.** `Test_reduce::test_accepts_only_what_the_shell_cuts_where_the_reader_does` and `Test_reduce::test_accepts_a_programs_suffix_the_shell_runs_and_no_line_of_its_body` run every admitted string through bash and zsh, directly and through `eval`: they are the rows showing the reading and the shell agree, which rule 4 keeps. Launch's two process cases run a Python interpreter on the launcher.

**Left where they stand.** `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py` keeps its three cases, which read each shape through the commit gate's reading and pin `hooks/one_heredoc.py`, `hooks/cmdline.py` and `hooks/tokens.py` together; they wait for the last of the three. `tests/test_edits_go_through_the_edit_tool.py::test_the_rule_names_the_one_heredoc_shape_it_does_not_read` reads prose and is #923's.

**The boundary** (`executed`). At the tree committed as ccca432d: the changed test files, `tests/test_the_old_spellings_reach_the_hook.py`, which imports the commit-gate heredoc file, `tests/test_censuses.py`, the `git_listing` files, `tests/test_chain_hooks_hardening.py`, `tests/test_test_layout.py` and `tests/test_conftest.py`, 25 files: 2,037 passed. The shards module: 32 passed and 1 failed, the known red. `bin/test-layout --check` exits 0, 152 files read, 130 declaring no `TARGET`; `--pairs` names group 1's one pair; `bin/rules --check` exits 0; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed `.py` file clean, one file per run.

### Batch B, `hooks/`, group 3, at e6700896

**The module.** `hooks/session-lease.py`, whose cases sat in `tests/test_lease_liveness.py` (eleven), `tests/test_chain_hooks.py` (four) and `tests/test_chain_hooks_hardening.py` (four), now `tests/test_session_lease.py`. The three old files keep their other cases and are named in both lists.

**The move check** (`executed`):

`bin/test-layout --moved ccca432d --from tests/test_lease_liveness.py tests/test_chain_hooks.py tests/test_chain_hooks_hardening.py --to tests/test_session_lease.py tests/test_lease_liveness.py tests/test_chain_hooks.py tests/test_chain_hooks_hardening.py`

`test-layout: moved: 108 old cases, 119 items against 119 at ccca432d83a7, 3 failed`, exit 1. The three lines are one merge made on purpose: `test_write_leases_edited_files_repo_not_cwd` and `test_edit_tool_leases_like_write` read alike once strings are normalised, so they became `Test_main::test_accepts_an_edit_and_leases_the_edited_files_repo_not_the_cwd`, parametrized over the tool. No move needed repair.

**Helpers.** `lease_dir` is used by the cases that moved and by the guard's cases that stayed, so it moved to `tests/conftest.py`. The two `leases_of` helpers read the same directory, one through `conftest.git_dir` and one through a local `git` with `rev-parse --absolute-git-dir`; the new file keeps the first, and the linked-worktree case runs `conftest.git`, which checks git's exit where the local helper did not.

**The mutation table** (`executed`, one batch over `tests/test_session_lease.py` with `-x`; the old column against the three old files in an archive of ccca432d):

| Mutants | New column | Old column | Old gaps |
|---|---|---|---|
| 15 | 9 red, 6 survived | 6 survived | a tool other than Bash and the editors taken as Bash; a target that is not a directory; `git_dir` answering nothing outside a repository, or answering on a non-zero exit; the session id joined without `basename`; the write's `OSError` let through. The case for an unwritable directory runs the hook in a subprocess and asserts nothing about its exit |

The mutants sit at `main`'s tool test, editor target, other-tool return, directory test, git directory test, session id, pid file name, own-session test, exported pid, pid record, prune cutoff and comparison and write error, and at `git_dir`'s exit and its `--absolute-git-dir`. No case was added: every survivor is an old gap.

**Cases and seconds** (`executed`, serial). Before, the three old files at ccca432d: 119 items in 10.43 s, and 22.84 s an hour later on the same tree. After, the new file and the three old files: 120 items in 11.37 s, 25.07 s and 22.18 s over three runs; the new file alone, 29 items in 7.03 s.

**The real-git cases kept.** Every case of `Test_main` runs the hook against the `repo` fixture's git, and the linked-worktree case adds a worktree: where the lease lands is the git directory git names.

**Left where they stand.** For `hooks/hooksession.py`, under their names in `tests/test_session_lease.py`: `test_the_session_pid_walks_past_the_shell`, `test_the_session_pid_is_none_without_a_claude_ancestor` and `test_an_exported_pid_that_names_no_process_falls_back_to_the_walk`, which ask its `claude_pid` through `stub_process_tree`. For `hooks/worktree-guard.py`, in `tests/test_lease_liveness.py`: its 29 cases of `fresh_leases`, `dead_session_ids`, `transcript_idle_minutes`, `sessions_in_tree` and `main`. They cannot pass the move check inside `tests/test_worktree_guard.py`, whose autouse `_git_asked_once_per_directory` every case there requests, and the guard has five more light files, four named by `check:` lines in `docs/worktree-guard-spec.md`; they wait for one group that places all of them and runs the guard's mutants once.

**The boundary** (`executed`). At the tree committed as e6700896: the four files, every file carrying `rule_carriers` or the `a-persons-own-commit` marker (`tests/e2e/commit/test_commit_flow.py`, `tests/test_the_commit_gate_decides_at_the_commit.py`, `tests/test_the_hooks_are_installed_where_git_runs_them.py`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`), the censuses, the `git_listing` files, `tests/test_chain_hooks_hardening.py`, `tests/test_test_layout.py` and `tests/test_conftest.py`, 29 files: 1,993 passed. The shards module: the known red alone. `bin/test-layout --check` exits 0, 153 files read, 130 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean on each changed file.

### What `hooks/` holds back

**The implementer family waits for a rule change** (`read`). `hooks/implementer.py`, `hooks/implementer-mark.py` and `hooks/implementer-notice.py` have their cases in `tests/test_the_implementer_is_recorded.py`, and `docs/commit-review-gate-spec.md` line 212 names that file in the `check:` line of the rule *A `framer` or `smith` spawn leaves a mark*. Placing the cases empties the file, and `bin/rules --check` then refuses the line; the smith edits nothing under `docs/`. The line needs a `## Rule changes` item in `spec.md`, naming `tests/test_implementer_mark.py tests/test_implementer_notice.py`, before the family moves.

**Files a group may drain but not remove** (`executed`, `git grep` over the `check:` lines of `docs/`, `CONTRIBUTING.md`, `skills/` and `agents/`). Of the undeclared files that hold `hooks/` cases, these are named by a `check:` line: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_hooks_are_installed_where_git_runs_them.py`, `tests/test_routing_is_recorded.py`, `tests/test_optin_home.py`, `tests/test_a_gate_that_fails_says_so.py`, `tests/test_worktree_guard_signals.py`, `tests/test_guard_resolves_the_tree_it_judges.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_the_mode_question_is_asked_once.py`, `tests/test_gate_judges_the_repo_it_commits_to.py`, `tests/test_a_creation_is_judged_before_git_runs.py` and `tests/test_chain_hooks_hardening.py`. A group that would move every case out of one of them needs the framer's rule change first.
