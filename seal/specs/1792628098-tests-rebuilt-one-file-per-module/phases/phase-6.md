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

### Batch B, `hooks/`, group 4, at 714f2df2

**The module.** `hooks/mode-gate.py`, whose cases were the 24 of `tests/test_the_mode_question_is_asked_once.py`'s section *S7-S10: the gate* and `test_a_table_the_walker_refuses_is_silence_from_the_mode_gate`, now `tests/test_mode_gate.py`. The old file keeps the config reader's cases. The two `check:` lines that name it, in `docs/one-root-by-lifetime.md` line 223 and its Korean twin line 212, stand under the config reader's rule *A cell may carry an escaped pipe*, whose cases stay, so they still name the file that holds their rule. The survey's 44 matches in `tests/test_gate_judges_the_repo_it_commits_to.py` were the word `Mode` in a config row; reading the file found no case of this module there.

**The move check** (`executed`):

`bin/test-layout --moved e945c57c --from tests/test_the_mode_question_is_asked_once.py --to tests/test_mode_gate.py tests/test_the_mode_question_is_asked_once.py`

`test-layout: moved: 66 old cases, 180 items against 180 at e945c57c16fc, 4 failed`, exit 1. The four lines are one merge made on purpose: `test_a_recorded_mode_is_silent`, `test_a_local_root_with_a_recorded_mode_is_silent` and `test_a_mode_row_written_twice_is_silence_not_a_question` read alike once names and strings are normalised, so they became `Test_main::test_accepts_a_root_whose_config_answers_or_refuses_the_mode`, parametrized over the root and the rows.

**Helpers.** `TABLE`, `opt_in_shared`, `write_config` and `write_unreadable` are used by both files, so they moved to `tests/conftest.py`.

**The mutation table** (`executed`, one batch over `tests/test_mode_gate.py` with `-x`; the old column against the old file in an archive of e945c57c):

| Mutants | New column | Old column | Old gaps |
|---|---|---|---|
| 16 | 12 red, 4 survived | 4 survived | a session id of `.` or `..`; `undeclared` answering the falsy home it was given in place of `""`, which no caller tells apart while `optin.home_at` answers `""`; `git_dir_of` answering on a non-zero exit; the question's first sentence without the root's path, which the first option names again |

The mutants sit at `already_asked`'s `basename`, dot names, existing marker and write error; `undeclared`'s missing home and both readings of `refused`; `git_dir_of`'s exit and absolute join; `marker_dir`'s shared and local arms; and `main`'s tool test, root, first prompt, second prompt and the question's text. No case was added.

**Cases and seconds** (`executed`, serial): before, 180 items in 2.48 s; after, 181 items in 2.67 s over the two files, the new file alone 27 items in 3.63 s.

**The real-git cases kept.** Every case runs the gate as a process against the `repo` fixture, and two add a linked worktree: which git directory holds the marker is git's answer.

**Left where they stand.** `test_a_line_that_will_not_parse_is_named_and_the_hook_still_says_nothing` reads the config reader and the gate's `undeclared` in one body, and waits in the old file for `hooks/config.py`. `tests/test_first_setup_asks_once.py`'s case naming `mode-gate.py` reads the bootstrap prose and the dispatcher's list, and is the first-setup rule's.

**The boundary** (`executed`). At the tree committed as 714f2df2: the two files, `tests/test_first_setup_asks_once.py`, `tests/test_a_reference_root_is_read_and_never_taken.py`, the censuses, the `git_listing` files, `tests/test_chain_hooks_hardening.py`, `tests/test_test_layout.py` and `tests/test_conftest.py`, 26 files: 1,900 passed; `tests/test_a_signer_declares_its_pact.py`, which names the old file in a docstring, 50 passed. The shards module: the known red alone. `bin/test-layout --check` exits 0, 154 files read, 130 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean on each changed file.

### Batch B, `hooks/`, group 5, at 04115ed2

**The modules.** `hooks/answers.py`, `hooks/answer-write.py` and `hooks/answer-clear.py`, whose fifteen cases sat in `tests/test_the_old_spellings_reach_the_hook.py`, now `tests/test_answers.py` (`Test_given`, `Test_write`, `Test_module`), `tests/test_answer_write.py` (`Test_main`) and `tests/test_answer_clear.py`. No other file reaches the three modules by name or import (`git grep`, `executed`); the survey's matches elsewhere were the word `answers`. The old file keeps `hooks/tokens.py`'s two cases and is named in both lists.

**Where the cases went.** `test_another_call_neither_replaces_nor_clears_an_answer` writes two calls and clears each, so it is `Test_write`'s refusing case. `call_id`'s one case and `root_dir`'s one case have no partner to make a pair with, so each is in `Test_module`. `hooks/answer-clear.py`'s two cases write through the writer before they clear, so they are its `Test_module`, and `--check` reports its `main` with no class.

**The move check** (`executed`):

`bin/test-layout --moved 714f2df2 --from tests/test_the_old_spellings_reach_the_hook.py --to tests/test_answers.py tests/test_answer_write.py tests/test_answer_clear.py tests/test_the_old_spellings_reach_the_hook.py`

`test-layout: moved: 17 old cases, 37 items against 37 at 714f2df2eff1, 0 failed`, exit 0. No module of the group has a mutation table. `--pairs` names no pair in the four files.

**Helpers and loading.** `A`, `B`, `shell` and `run` are used by all three new files, so they moved to `tests/conftest.py`, which now imports `io`; `tests/e2e/commit/test_commit_flow.py`'s docstring names `tests/conftest.py#shell`. The new files load `answers` through `load_hook_module` under the name the cases read, because `TARGET` has to be the first statement after the imports and ruff's E402 refuses an `import answers` after it.

**Cases and seconds** (`executed`, serial): 37 items in 0.18 s before, 40 items in 0.15 to 0.19 s after over the four files.

**Left where they stand.** For `hooks/tokens.py`, in the old file: `test_a_token_is_a_bare_word_and_nothing_else` and `test_the_three_token_reads_answer_as_one`, with `TOKEN_CASES` and `_corpora`.

**The boundary** (`executed`). At the tree committed as 04115ed2: the four files, the commit flow, `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py`, the censuses, the `git_listing` files, `tests/test_chain_hooks_hardening.py`, `tests/test_test_layout.py` and `tests/test_conftest.py`, 28 files: 2,075 passed. The shards module: the known red alone. `bin/test-layout --check` exits 0, 157 files read, 130 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean on each changed file.

### Batch B, `hooks/`, group 6, at df48707c

**The module.** `hooks/hooksession.py`, whose three `claude_pid` cases group 3 left under their names in `tests/test_session_lease.py`, now `tests/test_hooksession.py` (`Test_claude_pid`). `tests/e2e/commit/test_commit_flow.py` keeps its scenarios that read a lease back through `from_lease` and `session`, as phase 5 placed them in the flow.

**The move check** (`executed`):

`bin/test-layout --moved 04115ed2 --from tests/test_session_lease.py --to tests/test_hooksession.py tests/test_session_lease.py`

`test-layout: moved: 18 old cases, 28 items against 28 at 04115ed2da4d, 0 failed`, exit 0. No mutation table.

**Helpers.** `stub_process_tree` serves both files, so it moved to `tests/conftest.py`. It replaced `getppid` and `run` on the `os` and `subprocess` the loaded session-lease module holds; those are the shared modules, so the conftest version replaces them on `os` and `subprocess` directly.

**Cases and seconds** (`executed`, serial): 29 items in 0.94 s before, 30 items in 1.03 to 3.33 s after over the two files.

**The boundary** (`executed`). At the tree committed as df48707c: the two files, `tests/test_lease_liveness.py`, the commit flow, the censuses, the `git_listing` files, `tests/test_chain_hooks_hardening.py`, `tests/test_test_layout.py` and `tests/test_conftest.py`, 26 files: 1,897 passed. The shards module: the known red alone. `bin/test-layout --check` exits 0, 158 files read, 130 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean on each changed file.

### The third spawn, after the framer's amendment at 066e619b

**What this spawn was asked.** First, re-wrap `CONTRIBUTING.md`'s launcher paragraph, which CI run 39895069406 at 1b0e7c23 failed on line 127 at 118 columns, and name the framer's `## Rule changes` items and Q10's wait in `handoff.md`. Then the held-back `hooks/` groups in the order `questions.md` gives, one commit per group: the dispatcher with `hooks/console.py` and the creation flow; routing; the implementer family; optin; `hooks/worktree_consent.py`, then the worktree guard's light files; the sealer stamp, its queue and `hooks/commitgate.py`, written anew; the commit gate's light cases; then the shared readers, one group each. `hooks/githooks.py` and `hooks/hook-install.py` wait on Q10. After the first group that empties a file a `check:` line names, run `bin/rules --check` and stop if it refuses.

**Whether the frame holds** (`read`). It holds. `spec.md` *Rule changes* carries an item for each `check:` line the groups above empty or whose rule their cases hold, and `.github/scripts/rules.py#target_problem` refuses a target that does not exist or is not a file, and reads nothing inside it.

**CI at 1b0e7c23** (`executed`, `gh run view 39895069406 --log-failed`). Two cases failed: `tests/test_docs_line_wrap.py::test_prose_stays_within_the_wrap_limit[CONTRIBUTING.md]` on the macOS, ubuntu and Windows legs, and `test_the_durations_file_prices_the_suite`, the known red. Every file groups 1 to 6 wrote passed on the Windows and ubuntu legs. 5639d076 re-wraps the paragraph; the wrap module passes, 39 cases.

### Batch B, `hooks/`, group 7, at 9c70ddbf

**The modules.** `hooks/dispatch.py`, whose cases were the ten of `tests/test_dispatch.py`, 31 of `tests/test_a_gate_that_fails_says_so.py` and the dispatcher's of `tests/test_console_is_not_utf8.py`, now `tests/test_dispatch.py` with `TARGET`; `hooks/console.py`, whose case runs the commit gate alone, now `tests/test_console.py`; and the creation flow, the six cases of `tests/test_a_creation_is_judged_before_git_runs.py`, now `tests/e2e/creation/test_creation_flow.py` with `TARGET = "hooks/dispatch.py"`, one scenario class, `Test_a_creation_is_judged_before_git_runs`. `tests/test_a_gate_that_fails_says_so.py` keeps its case that reads `docs/commit-review-gate-spec.md` *Registration*, which is #923's and which the section's `## Rule changes` item keeps on the line. `tests/test_console_is_not_utf8.py` keeps routing's case for routing's group.

**The emptied file a `check:` line names** (`executed`). `tests/test_a_creation_is_judged_before_git_runs.py` holds a docstring naming the flow and no case. With it so, `bin/rules --check` exits 0 and prints `rules: all 249 check lines in 62 rule files hold.` The framer's reading of `rules.py#target_problem` is the one the tree gives: the file exists, and nothing reads what it holds.

**The move check** (`executed`):

`bin/test-layout --moved 5639d076 --from tests/test_dispatch.py tests/test_a_gate_that_fails_says_so.py tests/test_console_is_not_utf8.py tests/test_a_creation_is_judged_before_git_runs.py --to tests/test_dispatch.py tests/test_console.py tests/e2e/creation/test_creation_flow.py tests/test_a_gate_that_fails_says_so.py tests/test_console_is_not_utf8.py tests/test_a_creation_is_judged_before_git_runs.py`

`test-layout: moved: 51 old cases, 59 items against 59 at 5639d076e5d3, 2 failed`, exit 1. The two lines are one edit made on purpose: the console case the dispatcher runs called its file's `dispatch(group, payload, encoding)`, and `tests/test_dispatch.py` holds the failure report's `dispatch(hooks, group, body, cwd=None)`, so the case calls its helper as `dispatch_under`. Narrowed per Q8's default: the creation flow's own old file, `--from tests/test_a_creation_is_judged_before_git_runs.py --to tests/e2e/creation/test_creation_flow.py tests/test_a_creation_is_judged_before_git_runs.py`, ends `6 old cases, 8 items against 8 at 5639d076e5d3, 0 failed`, exit 0; the dispatcher and the console, which share `tests/test_console_is_not_utf8.py`, end `45 old cases, 51 items against 51 at 5639d076e5d3, 2 failed`, so both run the mutants. `--pairs` names no pair in the three new files.

**Helpers.** `KOREAN`, `HOSTILE`, `_console_repo_template`, `opted_in_repo` and the `korean_repo` fixture serve three files, so they moved to `tests/conftest.py`; the fixture's definition is the same in both trees, so the fixture condition holds. The console file's `decision_of` read a finished process's bytes and conftest's read text, so conftest's now reads either. The failure report's helpers moved with its cases into `tests/test_dispatch.py`.

**The names rewritten.** `hooks/dispatch.py`'s docstring of `toplevel` and its `entry_point` exemption, `skills/verify/scripts/seal_stamp.py`'s comment on `MESSAGE_RESERVE` (`tests/test_dispatch.py#longest_report`), `tests/censuses.py#entry_point`'s docstring and `tests/test_gates_do_not_fail_open.py`'s docstring name the new files. `seal/follow-up.md`'s row on `console.to_utf8()` still names the old file as the one enumerating `hooks/`, a measurement of 2026-09-22 that phase 3's censuses had already overtaken, and stands.

**The mutation tables** (`executed`, one `bin/mutation-check` batch per module over the new file with `-x`; the old column in an archive of 5639d076, against the three old files, for the survivors only).

| Module | Mutants | New column | Old column | Old gaps |
|---|---|---|---|---|
| `hooks/dispatch.py` | 50 | 48 red, 2 survived, 190.3 s | 2 survived | `main` running a known group's gates for an unknown group: the refusing case runs in a repository not opted in, where those gates are silent; `main`'s event name, which no case reads |
| `hooks/console.py` | 3 | 2 red, 1 survived | 1 survived | `to_utf8` leaving stdout unconfigured: the commit gate prints JSON with every non-ASCII character escaped, so any console carries it |

The dispatcher's mutants sit at `run_gate`'s phase, its `SystemExit` catch in `main()` and at load, and its argv swap; `readable`'s object test, reason test and message test; `classify`'s readable test and text strip; `merge`'s rank, kept message and joined text; `path_part`'s dot names; `toplevel`'s `.git` test; `common_dir`'s directory test and its git question; `opted_in`'s cannot-tell answer and its asked answer; `capped`'s astral width and its comparison; `first_line`'s line; `record`'s session test, seen test, opt-in test, name cap, exclusive create and place; `read_record`'s object test; `flat`'s join; `describe`'s load expansion, decided groups, group cap, message cap, gate cap and cause; `draw`'s subagent test, opt-in test, file-time fallback, claim, order and count; `beside`'s object test and empty answer; `report`'s record call, the order beside the stamp and the empty group; and `main`'s unknown group, unreadable output, the `stop` draw and the event name. The console's sit at the reconfigure call and at the stdout and stdin entries of `STREAMS`. No case was added: every survivor is an old gap.

**Cases and seconds** (`executed`, serial, pytest's own figure): 59 items in 12.54 s before, at 5639d076 in an archive with the worktree's `.venv`; 62 items in 12.11 s after, over the three new files and the three old ones. Each "after" counts the census cases.

**The real-git cases kept.** The flow's every case: a clone with the installed stubs, the dispatcher run below a shell named `claude`, the command run by bash, then `post-bash`, and the world read afterwards. In `tests/test_dispatch.py`, the cases that run a copy of `hooks/` against the `repo` fixture, where the records land in the git common dir, and `Test_module::test_the_walk_agrees_with_its_twin_in_sealer_stamp`, which adds a linked worktree.

**Phase 4's survivors** (`executed`). h14, `q` not quoting, re-run against the creation flow: SURVIVED, 9 passed. No path in the flow needs quoting, so it stays an old gap.

**The boundary** (`executed`). At the tree committed as 9c70ddbf: the six files, every test file naming `decision_of`, `opted_in_repo`, `korean_repo`, `HOSTILE` or `KOREAN`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_seal_stamp.py` and `tests/test_gates_do_not_fail_open.py`, 40 files: 2,196 passed. `bin/test-layout --check` exits 0, 160 files read, 129 declaring no `TARGET`; `bin/rules --check` exits 0. Ruff checks and formats each changed `.py` file clean.

### Batch B, `hooks/`, group 8, at 4f50aee0 and 6c126f35

**The module.** `hooks/routing.py`, whose parser cases were 23 of `tests/test_routing_is_recorded.py` and the undecodable declaration's case of `tests/test_console_is_not_utf8.py`, now `tests/test_routing.py` (`Test_parse`, `Test_module`). The old routing file keeps the 27 cases that run the commit gate, one of them through `hooks/gate.py#arms_missing` as well, which wait for the commit gate's light cases. `tests/test_console_is_not_utf8.py` held no other case and no `check:` line names it, so it went. The `check:` line of `docs/the-record-layout.md` *The fold, and what tells it from a deletion* names the old routing file and moves to `tests/test_routing.py` through its `## Rule changes` item.

**Left where they stand.** `tests/test_the_hooks_hide_what_a_renderer_hides.py`'s two cases of `routing.shown`: one holds the reader to the renderer oracle over a generated corpus, and the other is that case's guard against a reader that hides nothing, so the pair stays with the oracle, where `spec.md` *What the frame decided* keeps a check that judges markdown against an oracle. `tests/test_waiver_decided_at_start.py`'s two template cases assert the placeholder text of `templates/sdd-routing.md` and are #923's. `tests/test_a_reference_root_is_read_and_never_taken.py`'s case pins `settle.py` and routing's constants together, and `tests/test_a_script_copied_alone_exits_2.py`'s parametrized case pins `hooks/config.py` and routing alike; both wait for `hooks/config.py`'s group.

**The move check** (`executed`):

`bin/test-layout --moved 459d7944 --from tests/test_routing_is_recorded.py tests/test_console_is_not_utf8.py --to tests/test_routing.py tests/test_routing_is_recorded.py`

`test-layout: moved: 51 old cases, 69 items against 70 at 459d7944c0d4, 4 failed`, exit 1. As first placed it ended `70 items against 70 ..., 0 failed`. Then `--pairs` named three cases that call `parse(two_axis_text())`: `test_a_two_axis_declaration_is_still_a_declaration` and `test_a_declaration_without_a_planning_row_is_still_a_declaration` became `Test_parse::test_accepts_a_two_axis_declaration_with_no_optional_row_answered`, and the four lines are that merge and the count. The third, `test_an_absent_automation_row_is_not_the_same_fact_as_a_chosen_no`, is named and not merged: its point is that a chosen `no` and an absent row parse apart, which neither other case asserts.

**Helpers.** `two_axis_text` and `with_row` are used by both files, so they moved to `tests/conftest.py`; `tests/block_shapes.py`'s comment names the new place.

**The mutation table** (`executed`, one batch over `tests/test_routing.py` with `-x`; the old column against the two old files in an archive of 459d7944). The mutants sit at the functions the moved cases call: `shown`'s hidden test and its walk of the text, `table_rows`'s row test and cell count, `parse`'s count of a label, the review, destination and branch tests, the four optional vocabularies and the planning row's label, and `declarations`' decode catch, its missing home and its parsed test. `current_branch`, `for_branch`, `item_dir` and the round readers are reached only by the commit gate's cases, which did not move, so the move cannot have lost what they hold.

| Mutants | New column | Old column | Old gaps | Cases added |
|---|---|---|---|---|
| 16 | 11 red, 5 survived, 10.5 s | 3 survived, 2 red | `table_rows` reading a line that does not start with a pipe; `table_rows` reading a one-cell row; `declarations` reading a repository with no `seal/` as its own root | `Test_parse::test_refuses_a_review_answer_outside_the_vocabulary`, red on the review test read as truthiness; `Test_module::test_a_routing_md_that_does_not_parse_is_left_out`, red on the parsed test removed. The old file killed both through the commit gate's hook |

**Cases and seconds** (`executed`, serial): 70 items in 6.88 s before, in the archive of 459d7944; 72 items in 6.58 s after, over the two files.

**The real-git cases kept.** None in `tests/test_routing.py`: the parser reads text, and `declarations` reads a directory. The commit gate's cases in the old file run the hook against the `repo` fixture.

**The boundary, routing** (`executed`). At the tree committed as 4f50aee0: the two files, every test file naming `two_axis_text`, `with_row`, `block_shapes` or `routing`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 64 files: 4,620 passed and 2 skipped. At 6c126f35, `tests/test_routing.py`: 45 passed. `bin/test-layout --check` exits 0, 160 files read, 128 declaring no `TARGET`; `bin/rules --check` exits 0. Ruff clean on each changed file.

### Batch B, `hooks/`, group 9, at d8bba633

**The modules.** `hooks/implementer-mark.py`, whose eight cases were the mark's in `tests/test_the_implementer_is_recorded.py`, now `tests/test_implementer_mark.py` (`Test_main`, `Test_module`); and `hooks/implementer-notice.py`, whose fifteen were the notice's, now `tests/test_implementer_notice.py` (`Test_main`). `hooks/implementer.py` has no file: every case reaches it through one of the two hooks, and the mark file loads it to ask `stands`, as `questions.md` says. The old file keeps `test_the_commit_gate_decides_identically_with_the_row_and_without`, which runs the commit gate's hook alone and waits for the commit gate's group; the `check:` line of `docs/commit-review-gate-spec.md` *The implementer mark and notice* moves through its `## Rule changes` item to the two new files and `tests/test_commit_review_gate.py`.

**The move check** (`executed`):

`bin/test-layout --moved 8dedf9e4 --from tests/test_the_implementer_is_recorded.py --to tests/test_implementer_mark.py tests/test_implementer_notice.py tests/test_the_implementer_is_recorded.py`

`test-layout: moved: 24 old cases, 24 items against 24 at 8dedf9e4698c, 3 failed`, exit 1. As first placed it ended `0 failed`. Then `--pairs` named `test_the_other_answer_is_not_a_defect` and `test_an_unreadable_answer_says_nothing_either`, whose bodies differ by one string, and they became `Test_main::test_refuses_an_answer_that_names_no_agent`, parametrized over the two answers; the three lines are that merge. The two modules share the one old file, so both run the mutants, and so does `hooks/implementer.py`, which the moved cases reach.

**Helpers.** `ITEM`, `run_dispatch`, `declare`, `spawn` and `bash` serve the two new files and the old one, so they moved to `tests/conftest.py`. `hooks/dispatch.py`'s comment on the isolation property and `bin/arm-check`'s usage example name the new files.

**The mutation tables** (`executed`, one batch per module with `-x`; the old column in an archive of 8dedf9e4, against the old file, for the survivors only).

| Module | Mutants | New column | Old column | Old gaps |
|---|---|---|---|---|
| `hooks/implementer-mark.py` | 4 | 3 red, 1 survived | 1 survived | `main` taking a tool other than `Agent` or `Task`, which no case sends |
| `hooks/implementer.py`, over both new files | 5 | 3 red, 2 survived | 2 survived | `git_dir` answering on a non-zero exit; `write` writing an empty branch, a detached HEAD |
| `hooks/implementer-notice.py` | 13 | 8 red, 5 survived | 5 survived | `commits` reading the command without dropping comments and heredoc bodies; `already_told` taking a missing or dot session id; `notify` skipping the opt-in, which `for_branch` already answers with nothing outside an opted-in repository; `main` taking a tool other than Bash; the one-axis line's `no smith was spawned`, which no case reads |

The mutants sit at the mark hook's tool test, agent test, opt-in and branch; `implementer.py`'s git exit, `write`'s branch test, `stands`' comparison and `mark_for`'s qualifier and exact match; and the notice's declared and standing tests in `unfulfilled`, the one-line and joined wording in `line`, `commits`' subcommand test and its cleaning, `already_told`'s record and session tests, `notify`'s opt-in, and `main`'s tool, commit and `githooks.decides` tests. No case was added: every survivor is an old gap.

**Cases and seconds** (`executed`, serial): 24 items in 4.38 s before, in the archive; 26 items in 4.64 s after, over the three files.

**The real-git cases kept.** Every case: the hooks run through the dispatcher against the `repo` fixture, and the mark is a file in the git dir git names.

**The boundary** (`executed`). At the tree committed as d8bba633: the three files, every test file naming `run_dispatch`, `declare`, `spawn`, `ITEM` or `bash(`, every file naming `arm-check`, the `git_listing` files, the censuses, `tests/test_dispatch.py`, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 82 files: 4,681 passed and 10 skipped. `bin/test-layout --check` exits 0, 162 files read, 128 declaring no `TARGET`; `--pairs` names none in the new files; `bin/rules --check` exits 0. Ruff clean on each changed file.

### Batch B, `hooks/`, group 10, at 449feefb

**The module.** `hooks/optin.py`, whose cases were 29 of `tests/test_optin_home.py` and three of `tests/test_gates_do_not_fail_open.py`, now `tests/test_optin.py` (`Test_repo_root`, `Test_git_common_dir`, `Test_home_paths`, `Test_home`, `Test_opted_in`, `Test_parity_config`, `Test_module`). Group 1 left the version check's two cases and the review-skill gate's three in the old optin file for this module, because they pin how a hook reads the two places; they are in `Test_module`. The old file keeps the commit gate's seven cases, which wait for the commit gate's group. The `check:` lines of `docs/one-root-by-lifetime.md` and its Korean twin that name the old file move to `tests/test_optin.py` through their `## Rule changes` items.

**The move check** (`executed`):

`bin/test-layout --moved 9197c897 --from tests/test_optin_home.py tests/test_gates_do_not_fail_open.py --to tests/test_optin.py tests/test_optin_home.py tests/test_gates_do_not_fail_open.py`

`test-layout: moved: 46 old cases, 47 items against 47 at 9197c897c376, 6 failed`, exit 1. The six lines are the three cases from `tests/test_gates_do_not_fail_open.py`, each named twice. They read a module the file loaded at import under the name `optin`, which `tests/test_optin.py` gives to its fixture, so each now requests the fixture and reads the module through it; their bodies are as they were. `--pairs` names `test_review_skill_gate_fires_on_the_new_home` and `test_review_skill_gate_stays_silent_on_the_legacy_marker`, which assert opposite verdicts on two inputs, so neither covers the other and they are not merged.

**Helpers.** `home`, `legacy` and `scratch` serve both files, so they moved to `tests/conftest.py`. `tests/test_a_shrunken_corpus_declines_to_judge.py#LISTS_A_FIXTURE` names the local-root case under its new file, and `tests/test_first_setup_asks_once.py`'s docstring names `tests/test_optin.py`. That module's three cases fail while the new file is untracked, because its scan lists tracked files; after 449feefb they pass, 17 cases.

**The mutation table** (`executed`, one batch over `tests/test_optin.py` with `-x`; the old column against the two old files in an archive of 9197c897):

| Mutants | New column | Old column | Old gaps |
|---|---|---|---|
| 15 | 10 red, 5 survived, 18.6 s | 5 survived | `repo_root` asking git for a path that is not a directory, which git refuses anyway; `repo_root` answering git's spelling without `normpath`, which is the same spelling on POSIX; `home_paths` asking git when the caller passed the common directory, which no case counts; `home_paths` leaving the local place unnormalised; `parity_config` reading a repository with no root, where `home` answers nothing |

The mutants sit at `repo_root`'s directory test, its `None` guard and its `normpath`; `git_common_dir`'s directory fast path, its `None` guard and its join; `home_paths`' empty root, its passed common directory and its local normalisation; `home_at`'s marker as a file, the marker test, each place as a directory and the order; and `parity_config`'s file test and its missing root. No case was added.

**Cases and seconds** (`executed`, serial): 47 items in 2.29 s before, in the archive; 48 items in 2.07 s after, over the three files.

**The real-git cases kept.** Every case that takes the `repo` fixture asks git for the root or the common directory, and four add a linked worktree, whose `.git` is a file git has to resolve; the cases that stub `subprocess.run` are the rows where the reading is asked without git.

**The boundary** (`executed`). At the tree committed as 449feefb, before the commit: the three files, every test file naming `home(`, `legacy(`, `scratch(`, `KOREAN` or `optin`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 42 files: 2,841 passed and the three untracked-file failures above, which pass once committed. `bin/test-layout --check` exits 0, 163 files read, 128 declaring no `TARGET`; `bin/rules --check` exits 0. Ruff clean on each changed file.

### Batch B, `hooks/`, group 11, at e94c6826

**The module.** `hooks/worktree_consent.py`, whose cases were 40 of `tests/test_the_guard_asks_once_per_session.py` and the consent writer's five of `tests/test_guard_resolves_the_tree_it_judges.py` (four of `creation_directory` and one of `segment_cwd`), now `tests/test_worktree_consent.py` (`Test_main`, `Test_consent`, `Test_automation_answered`, `Test_segment_cwd`, `Test_creation_directory`, `Test_module`). The first old file keeps `test_the_labels_match_the_routing_question_the_orchestrator_asks`, which reads `skills/implement/orchestration.md`'s question and is #923's. The second keeps the guard's cases and the cases where the guard and the writer are asked of one command, which wait for the guard's group. The `check:` lines of `docs/worktree-guard-spec.md` that name the two old files move to `tests/test_worktree_consent.py` and `tests/test_worktree_guard.py` through their `## Rule changes` items.

**The move check** (`executed`):

`bin/test-layout --moved 167950a6 --from tests/test_the_guard_asks_once_per_session.py tests/test_guard_resolves_the_tree_it_judges.py --to tests/test_worktree_consent.py tests/test_the_guard_asks_once_per_session.py tests/test_guard_resolves_the_tree_it_judges.py`

`test-layout: moved: 100 old cases, 165 items against 165 at 167950a6e8bb, 0 failed`, exit 0. No mutation table. `--pairs` names no pair in the new file. The file's `projects` fixture moved with it, unchanged, and no autouse fixture of a test file reaches it, as `questions.md` says.

**Helpers.** Six files imported the once-per-session file's helpers, so `ACTIVE`, `IDLE`, `common_dir`, `consent_dir`, `grant`, `ROUTING_QUESTION`, `ROUTING_OPTIONS`, `ask_entries`, `write_transcript`, `TOKEN`, `PRESS` and `dirty_deny` moved to `tests/conftest.py`, with `BASE_TREE_CHAINS`, `PLACEMENT_CHAINS` and `_a_dirty_w_under_a_clean_session`, which the writer's cases share with the guard's. The commit flow, the creation flow, `tests/test_question_gate.py`, `tests/test_worktree_guard.py` and `tests/test_an_automation_run_meets_no_commit_prompt.py` import them from there. `tests/test_a_creation_in_another_clone_asks_nobody.py` and `tests/test_the_idle_session_rows_ask_nobody.py` patch the guard copy the consent file loads and share it through `judge`, so they import `wg` from `tests/test_worktree_consent.py` until the guard's group places them.

**Cases and seconds** (`executed`, serial): 165 items in 11.20 s before, in an archive of 167950a6; 166 items in 11.97 s after, over the three files. `.test_durations` prices the two old files' current cases at 14.6 and 40.0 Windows seconds, under rule 3's threshold; its 173.0 s for the first file is the price of the cases phase 5 rewrote out of it.

**The real-git cases kept.** The writer's cases run the hook against the `repo` fixture, where the record lands in the git common dir; two add a linked worktree, and the `creation_directory` cases copy the fixture into a dirty `w` beside a clean session tree.

**The boundary** (`executed`). At the tree committed as e94c6826: every test file naming one of the moved helpers or the new file, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 40 files: 2,184 passed and 3 skipped. `bin/test-layout --check` exits 0, 164 files read, 128 declaring no `TARGET`; `bin/rules --check` exits 0. Ruff clean on each changed file.

### The fourth spawn

**What this spawn was asked.** First, the `console.to_utf8()` row of `seal/follow-up.md` named `tests/test_console_is_not_utf8.py`, which group 8 removed; the row names the file that now holds the enumeration of `hooks/` entry points, in the first group's record commit. Then the rest of `hooks/` in this order, one commit per group and its record: the worktree guard's light files with phase 4's h21 re-run; the sealer stamp, its queue and `hooks/commitgate.py` written anew; the commit gate's light cases; the six shared readers, one group each. Phase 4's h2, h4, h6, h12 and h23 are re-run where a group rebuilds the module whose cases reach one. If `hooks/` finishes, the seven directories outside it follow in `plan.md`'s order.

**Whether the frame holds** (`read`). It holds for group 12. Every `check:` line naming a file the group drains has its `## Rule changes` item in `spec.md`, and the cases those items name (`Test_only_creates_a_worktree`, `Test_main::test_refuses_to_be_silent_where_the_writer_records`, `Test_main::test_refuses_a_line_weaker_than_its_switch_or_its_creation`, `Test_main::test_accepts_data_no_shell_runs_as_no_command`, `Test_shape_of::test_accepts_no_listed_form_that_moves_head_under_git`) stand in `tests/test_worktree_guard.py` since phase 5.

**The follow-up row** (`read`). `tests/censuses.py#entry_point` is the reading that enumerates `hooks/` alone: it reads a file only under `("hooks/",)` and refuses a `__main__` that does not open with `console.to_utf8()`. The case that held the enumeration in 2026-09 left `tests/test_console_is_not_utf8.py` when phase 3 built the censuses (197bc2a0), so the row names `tests/censuses.py` and nothing else in it changed.

### Batch B, `hooks/`, group 12, at c512b123

**The module.** `hooks/worktree-guard.py`'s light files: the 29 cases of `tests/test_lease_liveness.py`, the 20 of `tests/test_worktree_guard_signals.py`, the 10 of `tests/test_the_idle_session_rows_ask_nobody.py`, the 9 of `tests/test_a_creation_in_another_clone_asks_nobody.py`, the guard's 48 of the 54 in `tests/test_guard_resolves_the_tree_it_judges.py` and the process probe of `tests/test_gates_do_not_fail_open.py`, all into `tests/test_worktree_guard.py`. Each case went to the class of the function it calls: `Test_module`, `Test_split_command`, `Test_has_token`, `Test_walk_command`, `Test_lease_owner_alive`, `Test_fresh_leases`, `Test_dead_session_ids`, `Test_transcript_idle_minutes`, `Test_sessions_in_tree`, `Test_tracked_changes`, `Test_repo_paths`, `Test_main` and `Test_shape_of`, and two new classes, `Test_file_activity_epoch` and `Test_last_user_snippet`. A single case of a function with no class (`project_slug`, `proc_cwd`, `ancestors`, `parse_git`, `apply_chdir`, the generator of redirections, the guard loaded beside a broken wider reader) is in `Test_module`.

**Where the old files stand.** `tests/test_lease_liveness.py` held only the guard's cases and no `check:` line names it, so it went. The signals file and the two press-row files are named by `check:` lines of `docs/worktree-guard-spec.md` and keep a docstring and no case. `tests/test_guard_resolves_the_tree_it_judges.py` keeps the commit gate's `test_the_commit_gate_says_what_declining_does`, for the commit gate's group, and five cases that read the policy and the READMEs, which are #923's. `tests/test_gates_do_not_fail_open.py` keeps the commit gate's case, and its docstring names the probe's new place.

**The move check** (`executed`):

`bin/test-layout --moved 56fb82e0 --from tests/test_worktree_guard.py tests/test_lease_liveness.py tests/test_worktree_guard_signals.py tests/test_a_creation_in_another_clone_asks_nobody.py tests/test_the_idle_session_rows_ask_nobody.py tests/test_guard_resolves_the_tree_it_judges.py tests/test_gates_do_not_fail_open.py --to tests/test_worktree_guard.py tests/test_worktree_guard_signals.py tests/test_a_creation_in_another_clone_asks_nobody.py tests/test_the_idle_session_rows_ask_nobody.py tests/test_guard_resolves_the_tree_it_judges.py tests/test_gates_do_not_fail_open.py`

`test-layout: moved: 219 old cases, 358 items against 358 at 56fb82e0646c, 123 failed`, exit 1. Each failure line was read:

- 110 lines are the fixture condition alone: `fixture _git_asked_once_per_directory: requested in the working tree only`, one per moved case, as `questions.md` says.
- 10 lines are five bodies edited on purpose, each named twice. The creation rows' file and the switch rows' file each defined `situation`, `elsewhere`, `unattended` and `no_marker` with other bodies, and one module holds one definition of a name, so the creation side's are `creation_situation`, `creation_elsewhere`, `creation_unattended` and `no_create_marker`. Four creation cases call them under the new names. `tests/test_worktree_guard.py` already held a `LISTED` of whole commands, so the redirection case reads the moved tuple of verbs as `LISTED_VERBS`.
- 3 lines are one merge. `--pairs` named `test_live_lease_still_denies` and `test_lease_entries_flow_into_deny`, whose bodies differ by the lease entry's text alone, so they are one case parametrized over the entry, `a-live-owner` and `a-fresh-lease`.

No move needed repair. `--pairs` then names no pair in the file.

**Helpers.** The light files' helpers moved with their cases, under their names except the five above. The `wko` fixture of the switch rows' file is kept; the creation rows' copy loaded the same module under another name. `tests/test_the_old_spellings_reach_the_hook.py#_corpora` reads the guard's token commands from `tests/test_worktree_guard.py`. One edit went past the moved cases: the edit hook's `ruff check --fix` dropped the local `import re` of `test_the_list_carries_its_counts_and_nothing_unmeasured` once the module imported `re`, the move check named that body, and the import is back.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `hooks/worktree-guard.py` with `--tests "bin/test tests/test_worktree_guard.py -q -p no:xdist -x"`). 70 mutants, w1 to w70, one or two at the decision points of each class's function, the classes phase 5 wrote and the two this group added. 70 red, 0 survived, in 169.2 s after a 14.3 s baseline, so the old column did not run. Five red runs were read for their failing case through `--junitxml` (w4, w9, w13, w20, w40), and each failed on a case of the class the mutant sits in; four of the five are cases this group moved.

| # | Mutation | New file |
|---|---|---|
| w1, w2 | `_idle_min` takes zero; `_lang` reads `ko` as English | red |
| w3, w4 | `has_token` reads a here-document body; `parses_cleanly` reads the comment-free text | red |
| w5, w6 | `only_creates_a_worktree` compares the basename; `ELSEWHERE` without `>` | red |
| w7, w8 | `split_command` keeps comments; `walk_command` reads here-document lines | red |
| w9, w10 | `ancestors` adds no parent; `proc_cwd` keeps `lsof`'s `n` | red |
| w11, w12, w13 | `last_user_snippet` reads its own session, cuts the id at six; `project_slug` keeps dots | red |
| w14, w15, w16 | `last_active_event_epoch` reads oldest first; `file_activity_epoch` parses a stale file; an `attachment` read as active | red |
| w17, w18, w19 | `transcript_idle_minutes` reads a dead session's file, its subagents; walks no subdirectory | red |
| w20, w21 | `lease_owner_alive` on Windows reads a `None` stdout; reads a gone pid as unanswerable | red |
| w22, w23, w24 | `dead_session_ids` asks about a pid that is no integer, reads another host's lease, reads an unprobeable owner as dead | red |
| w25 to w29 | `fresh_leases` counts its own lease, escalates a scanned pid, escalates an unprobeable owner, keeps a gone owner's lease, counts an ownerless lease as live | red |
| w30 to w36 | `sessions_in_tree` counts any name holding `claude`, a sibling directory, no signal as idle, where its own session is invisible; drops the transcript arm; reads no dead ids in either transcript scan | red |
| w37, w38, w39 | `fmt_sessions` names a lease a transcript; `tracked_changes` counts untracked files; `phantom_entries` misses an index-only entry | red |
| w40, w41, w42 | `repo_paths` asks git with no timeout, names another root outside a repository; `git_at` says `git` wherever the shell is in a repository | red |
| w43, w44 | `already_asked` takes the session id as a path, asks twice | red |
| w45, w46 | `choose` ignores the press, runs no `before_ask` | red |
| w47, w48, w49 | consent allows a compound; creation row 4 ignores the press; `judge_creation` notes the quote where a token was read | red |
| w50 to w60 | `main`: an Agent without isolation judged; the Agent path reads no payload transcript; an ACTIVE tree lets a switch through; the token stands neither choice row aside; the idle row and the dirty row read the press in the switch's tree; the dirty row's phantoms and changes read the shell's directory; the second silent exit judges no creation; another clone's record names no split | red |
| w61 to w63 | `tree_matters` passes unusable detection; `automation_pressed` reads a raising reader as the press; the stop asks beside a switch | red |
| w64 to w70 | `_restores` takes a bare `--`; `_hidden_mover` finds nothing; `_rebase_names_a_branch` ignores `--root`; `_hidden_in` reads no string handed to a shell; `_command_findings` passes an untokenizable command; `_merged_findings` finds nothing without the wider reader; `stash branch` listed | red |

The exact replacements are kept with the build's driver outside the tree. An id here names a row of this table alone.

**Phase 4's h21** (`executed`). `guard_decision`'s silent answer renamed in `tests/conftest.py`, run against `tests/test_worktree_guard.py` with `-x`: SURVIVED, exit 1. Every moved case that calls `decide` expects a deny or an ask, so no case reaches the silent branch. The old files missed it too (`phases/phase-4.md`), so it stays an old gap.

**Cases and seconds** (`executed`, serial, pytest's own figure): 359 items in 22.85 s before, over the seven files at 56fb82e0; 359 items in 15.38 s after, over the six files. `tests/test_worktree_guard.py` alone: 352 items in 15.17 s serial, 5.9 s parallel.

**The real-git cases kept.** The moved lease, transcript and decision cases run on the `repo` fixture, whose git directory holds the leases; the press rows copy it into a second clone; the cases of the tree each command is judged in build a session tree with a dirty `w` under it, init repositories of their own, clone, and add a linked worktree in `test_the_way_on_passes_the_guard`, where the deny's named commands run under git. Each is a row where the guard's reading and git agree on which tree a command acts in.

**The boundary** (`executed`). At the tree committed as c512b123: the six files, `tests/test_the_old_spellings_reach_the_hook.py`, `tests/test_worktree_consent.py`, every test file naming the guard's file or the old files, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 31 files: 1,900 passed and 3 skipped. `bin/test-layout --check` exits 0, 163 files read, 127 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `hooks/`, group 13, at 5d6640b2

**The modules.** `hooks/sealer-stamp.py`, `hooks/sealer-stamp-queue.py` and the guarantee arm of `hooks/commitgate.py`, whose cases sat in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`. `.test_durations` prices them at 110.2 Windows seconds, so rule 3 writes them anew from the code: `tests/test_sealer_stamp.py` (`Test_toplevel`, `Test_load_stamp`, `Test_drawings`, `Test_main`, `Test_module`), `tests/test_sealer_stamp_queue.py` (`Test_shaped`, `Test_load_stamp`, `Test_main`, `Test_module`) and `tests/test_commitgate.py` (`Test_guarantee_off_history`, `Test_pre_commit`, `Test__record_refusal`, `Test_post_commit`). No move check runs for a module written anew; the mutants are its proof.

**How the new files run** (rule 4). Each hook's `main` runs in the process, its payload on `sys.stdin`. Each file builds its world once in a module-scoped fixture, and each case copies it: an opted-in repository for the `Stop` hook, a repository in local mode with a `sealed` work item under `.git/seal/` for the edit gate, and the declared work item on `feat/x` for the commit gate. One case per stamp hook runs it through `hooks/dispatch.py` as the harness does. `hooks/commitgate.py`'s other readings, the waiver, the mark, the backstop and the sequencer, stay with the commit flow, `tests/e2e/commit/test_commit_flow.py`, as phase 5 placed them, so `bin/test-layout --check` reports their functions with no class here.

**Where the old file stands.** It keeps its eight cases that read the documents, the READMEs, `agents/sealer.md` and `seal_stamp.py`'s comment and help, which are #923's, and their helpers. The `check:` line of `docs/the-review-record.md` *The stamp* names the file for one of them, and its `## Rule changes` item adds `tests/test_sealer_stamp.py`. Three of those prose cases, two here and one in `tests/test_the_commit_gate_decides_at_the_commit.py`, list the cases that carry a rule marker by name, and they now name the rewritten cases; `Test_guarantee_off_history::test_accepts_every_guarantee_but_one_sealed_off_the_history` carries the two markers the old quiet case carried.

**Each old case, and where it went.** Every class below is in the new file of its module unless another file is named.

- `test_the_main_sessions_stop_draws_each_undrawn_file_once`: rewritten as `Test_main::test_accepts_the_main_sessions_stop_and_draws_once` and `Test_module::test_the_stop_group_draws_through_the_dispatcher`.
- `test_a_subagents_end_draws_nothing_and_leaves_the_file` and `test_another_sessions_stop_leaves_its_file_alone`: rewritten as the rows of `Test_main::test_refuses_any_end_but_its_own_sessions_stop`.
- `test_several_files_come_out_one_stop_each_oldest_first`: rewritten as `Test_drawings::test_accepts_the_oldest_file_first_and_claims_what_it_draws`, the `not-json` row of `Test_drawings::test_refuses_to_claim_a_file_that_is_no_stamps_values`, and `Test_drawings::test_refuses_to_claim_what_one_message_does_not_carry`.
- `test_a_malformed_later_file_does_not_take_the_earlier_ones`: rewritten as that refusing case's row `an-item-that-is-no-string`.
- `test_a_file_an_older_gate_wrote_with_its_scale_is_drawn_by_the_hook` and `test_a_values_file_from_an_older_gate_draws_every_row_in_the_new_layout`: rewritten as `Test_drawings::test_accepts_a_file_an_older_gate_wrote`. The second's line-by-line check of the drawing is `seal_stamp.stamp`'s, held in `tests/test_seal_stamp.py`.
- `test_the_sealers_worktree_and_the_main_checkout_share_the_file` and `test_a_turn_ending_in_a_subdirectory_still_draws`: rewritten as `Test_main::test_accepts_a_turn_ending_in_a_subdirectory_or_a_linked_worktree` and `Test_toplevel::test_accepts_a_subdirectory_as_its_repository`.
- `test_a_repository_that_never_opted_in_is_not_drawn_for`: rewritten as `Test_main::test_refuses_a_repository_that_never_opted_in`.
- `test_the_hook_is_registered_for_stop_and_nothing_else`: placed in `Test_module` under its name.
- `test_the_hooks_message_is_under_the_budget_for_one_file`: rewritten into `Test_main::test_accepts_one_seal_too_large_for_its_disc_drawn_alone_without_it`, whose second `Stop` draws a real run's stamp with its disc under the budget.
- `test_two_files_in_one_turn_are_under_the_budget_together`: rewritten as `Test_drawings::test_refuses_to_claim_what_one_message_does_not_carry`.
- `test_seals_past_what_one_message_carries_wait_for_the_next_turn`: cut. Its twelve-file walk is one row per kind of the two `Test_drawings` cases above, and s5, which claims every file, is red on them.
- `test_one_seal_too_large_for_the_disc_is_drawn_alone_without_it`: rewritten as the `Test_main` case of that name.
- `test_the_stop_group_reports_the_stop_event`: the dispatcher's, placed in `tests/test_dispatch.py` as `Test_main::test_accepts_the_stop_group_and_names_its_event`; `hooks/dispatch.py`'s comment on `FAILED` names it there.
- `test_admitteds_docstring_fits_the_line_length`: `seal_stamp.admitted`'s, placed in `tests/test_seal_stamp.py`'s `Test_admitted`.
- `test_the_edit_gate_leaves_shared_mode_to_post_commit`: rewritten as `Test_main::test_refuses_a_shared_mode_guarantee_post_commit_queues`.
- `test_the_edit_gate_queues_a_local_mode_sealed_guarantee`, both tools: rewritten as `Test_main::test_accepts_a_local_mode_sealed_guarantee` and `Test_module::test_the_post_edit_group_queues_through_the_dispatcher`; the `Stop` that then draws the file is the `Stop` hook's, held by its own file.
- `test_a_subagents_write_queues_and_draws_nothing`: rewritten as `Test_main::test_accepts_a_subagents_write_for_the_main_session`; the subagent's end drawing nothing is the `Stop` hook's refusing row.
- `test_the_edit_gate_is_silent_off_a_guarantee`, five rows: rewritten as `Test_main::test_refuses_any_other_edit_before_it_loads_seal_stamp`, seven rows, and `Test_shaped`.
- `test_a_sealed_over_a_commit_the_branch_does_not_hold_is_refused_at_the_commit`, two rows: rewritten as `Test_pre_commit::test_refuses_a_sealed_off_the_history_and_records_the_refusal` and `Test_guarantee_off_history::test_refuses_a_sealed_over_a_commit_the_history_does_not_hold`, two rows each.
- `test_the_guarantee_refusal_is_quiet_off_its_one_fact`, 25 rows: rewritten as `Test_guarantee_off_history`'s accepting cases (the target at HEAD, an ancestor, `withheld`, two verdicts, one near miss, the unfilled template, a stale earlier run; no `routing.md` in the index, no `Branch` row, another branch, no HEAD; no guarantee staged with no reader loaded; a deleted guarantee), `Test_pre_commit::test_accepts_a_sealed_at_head_and_reaches_the_reader`, `Test_pre_commit::test_accepts_a_sealed_off_the_history_where_it_cannot_stand_on_the_fact` (a reader that will not load, the sequencer's commit, no session) and `Test_post_commit::test_refuses_to_queue_a_copy_of_a_sealed_item_onto_main` (`merge --squash`, and a checkout from a commit no ref holds). Rows cut: `undecided`, one verdict that is not `sealed` as `withheld` is; six of the seven near misses, whose reading is `chain_check.py`'s and is held whole by `tests/test_the_sealer_guarantees.py#NEAR_MISSES`; `cherry-pick -n onto main` and `checkout of the item onto main`, a copy onto another branch than the declared one, as the `another-branch` row and `merge --squash` are; the unborn branch through `pre-commit`, now the `no-head` row.
- `test_a_refused_row_over_a_drawn_seal_does_not_draw_again`: rewritten as `Test_post_commit::test_refuses_to_draw_again_over_a_refused_row_of_a_drawn_seal`.
- `test_a_tracking_ref_left_by_a_rebase_withholds_nothing`: rewritten as `Test_post_commit::test_accepts_the_repair_of_a_row_refused_after_a_rebase`.

**Helpers.** `guarantee_record`, `routing_record`, `queued_values` and `STAMP_ITEM` serve the edit gate's and the commit gate's files, so they are in `tests/conftest.py`; the commits are `conftest.commit_everything_as_e`'s. `tests/test_a_shrunken_corpus_declines_to_judge.py#LISTS_A_FIXTURE` names `tests/test_commitgate.py#paths_of`, which lists the paths staged in the case's own copy of the world.

**The mutation tables** (`executed`, one `bin/mutation-check` batch per module with `-x`, against its new file; the old column against the old stamp file in an archive of af232663 with the worktree's `.venv`, for the survivors only).

| Module | Mutants | New column | Old column | Old gaps |
|---|---|---|---|---|
| `hooks/sealer-stamp.py` | 14 | 12 red, 2 survived, 7.0 s | 2 survived | `drawings` drawing no file before it claims it: a values file that reads and labels but does not draw is no shape either file writes; `main` with no `if not session` test: an empty session reads the `none` directory, which only a values file written with no session fills |
| `hooks/sealer-stamp-queue.py` | 10 | 10 red, 4.9 s | not run | none |
| `hooks/commitgate.py` | 19 | 17 red, 2 survived, 61.8 s | 2 survived | `guarantee_off_history` without its `text is None` test: the deleted-guarantee row passes either way; without its `target is None` test: only a `sealed` with no `Target SHA` row reaches it, and neither file stages one |

The mutants sit at `toplevel`'s two exits, `load_stamp`'s catch, `drawings`' draw before the claim and its admitted count, and `main`'s event, agent, session, payload, opt-in, its order before the directory, the loaded stamp, the common dir and the message (s1 to s14); at `shaped`'s separator and its pattern's two ends, `TOOLS`, and `main`'s session, payload, catch, message, session handed on and shape before the loader (q1 to q10); and at `guarantee_off_history`'s head, staged items, deleted file, verdict count, verdict word, target, declared branch, declaration, ancestry and recorded id, `pre_commit`'s sequencer, record and text, `_record_refusal`'s catch, `post_commit`'s two catches, queue and lines, and `_context`'s session (c1 to c19). No case was added: every survivor is an old gap. The exact replacements are kept with the build's driver outside the tree.

**Group 7's event-name gap** (`executed`). `hooks/dispatch.py#main` with `EVENTS` dropped from the event name is red on `tests/test_dispatch.py` now, on the case placed there above alone. Group 7 recorded `main`'s event name as read by no case, from the dispatcher's old files; whether its mutant was this replacement is not recorded (`unverified`, the build's driver of group 7 holds it).

**Cases and seconds** (`executed`, serial, pytest's own figure): 62 items in 35.96 s before, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` alone; 91 items in 10.98 s after, over the three new files and the old one, which runs its 8 prose cases in 0.35 s. The new files alone: 28 items in 0.63 s, 24 in 0.84 s and 31 in 7.59 s.

**The real-git cases kept.** The commit gate's every case: the guarantee and its declaration are read from the index git keeps, the ancestry is `git merge-base`'s answer, and the two rebase cases and the copies onto `main` clone the world, as the shapes are where git and the arm agree on what HEAD's history holds. The edit gate's cases read the work item from a local-mode root git places under the common dir. The `Stop` hook's linked-worktree case adds a worktree, whose common dir git names.

**The boundary** (`executed`). At the tree committed as 5d6640b2: the three new files, the old one, `tests/test_dispatch.py`, `tests/test_seal_stamp.py`, `tests/test_the_commit_gate_decides_at_the_commit.py`, the commit flow, every test file naming the stamp hooks, `commitgate` or the old file, every file reading `rule_carriers` or a `git_listing`, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 31 files: 2,291 passed and 3 skipped. The shards module: the known red alone. `bin/test-layout --check` exits 0, 166 files read, 127 declaring no `TARGET`; `--pairs` names no pair in the five changed module files; `bin/rules --check` exits 0, 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### The fifth spawn

**What this spawn was asked.** The rest of `hooks/`, one commit per group and its record: group 14, the commit gate's light cases in the held-back files; then the six shared readers, one group each, with the `check:` lines grepped before each reader group and a stop at the first line that has no `## Rule changes` item. `hooks/githooks.py` and `hooks/hook-install.py` wait on Q10. Phase 4's h2, h4, h6, h12 and h23 are re-run where a group rebuilds the module whose cases reach one. If `hooks/` finishes, the seven directories outside it follow in `plan.md`'s order.

### Batch B, `hooks/`, group 14, at f5185d67

**Whether the frame holds** (`executed`, `git grep` over the `check:` lines of `docs/`, `CONTRIBUTING.md`, `skills/` and `agents/`). It does not hold for the whole group. `plan.md`'s amendment of 066e619b says `spec.md` *Rule changes* carries every `check:` line the held-back `hooks/` groups would empty or whose rules their cases hold. Five lines name a file that holds commit gate cases, hold a rule those cases assert, and have no item:

| Line | Its rule | The file it names, and the commit gate cases holding the rule there |
|---|---|---|
| `docs/commit-review-gate-spec.md` line 83 | the refusal under the `automation` press, and how the press is read | `tests/test_an_automation_run_meets_no_commit_prompt.py`: all 17 cases, among them the three that call `worktree_consent.automation_answered` |
| `docs/commit-review-gate-spec.md` line 125 | a target the gate cannot resolve stops, and the table of what cannot be resolved | `tests/test_gate_judges_the_repo_it_commits_to.py` (with `tests/test_what_the_reader_understands.py`): the cases that run the gate over a `cd` or `-C` it cannot place |
| `docs/commit-review-gate-spec.md` line 139 | a commit is read wherever the shell would run one | `tests/test_a_commit_behind_a_reserved_word_is_judged.py` and `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`: the three cases of the first that run the gate's `main` |
| `docs/the-review-and-parity-arms.md` line 52 | the waiver goes in front of the command | `tests/test_the_waiver_can_be_typed.py`: all 6 cases |
| `docs/the-review-and-parity-arms.md` line 141 | the parity arm's table, and a diff git could not take is asked about | `tests/test_chain_hooks_hardening.py`: the parity arm's fourteen cases, two of them `hooks/commitgate.py`'s and `hooks/gate.py`'s |

So the group is the commit gate's cases that hold none of those rules, the cases the plan lets move. Each file in the table keeps its cases, and the commit gate runs its mutants again in the group that places them, once the framer writes the five items. `tests/test_gate_judges_the_repo_it_commits_to.py` and `tests/test_a_path_the_command_wrote_out.py` also hold gate cases whose rows pin how `hooks/cmdline.py` reads a `cd`, a name or a pipeline; those are rule 2's *left for its module*, for the reader's group.

**The module.** `hooks/commit-review-gate.py`, whose light cases were these, all now in `tests/test_commit_review_gate.py`:

- `Test_main`: the 27 of `tests/test_routing_is_recorded.py`; the one of `tests/test_the_implementer_is_recorded.py`; 5 of the 7 of `tests/test_optin_home.py`; the 10 of `tests/test_chain_hooks.py`; the one of `tests/test_gates_do_not_fail_open.py`; the commit gate's one of `tests/test_guard_resolves_the_tree_it_judges.py`; the 5 commit gate cases of `tests/test_local_mode_resolves_under_the_git_dir.py`; the commit gate's 9 at the head of `tests/test_chain_hooks_hardening.py` and its `test_the_review_arm_asks_on_a_document_only_commit`, which carries the `review-arm-asks` marker.
- `Test_touches_code`: the two `touches_code` cases of `tests/test_optin_home.py`, renamed `test_refuses_the_home_directory_as_code` and `test_accepts_a_code_change_alongside_the_home_directory`.
- `Test_module`: `read_mark`'s one case of `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`, under its name.

63 old cases, 64 items, land as 59 cases. The other cases keep their names.

**Where the old files stand.** `tests/test_chain_hooks.py` and `tests/test_gates_do_not_fail_open.py` held nothing else and no `check:` line names either, so they went. `tests/test_routing_is_recorded.py`, `tests/test_the_implementer_is_recorded.py` and `tests/test_optin_home.py` are named by `check:` lines with `## Rule changes` items, and keep a docstring and no case. `tests/test_local_mode_resolves_under_the_git_dir.py` keeps the implementer notice's case and the case that runs three gates over the scratch marker, both left behind by groups 9 and 10. `tests/test_guard_resolves_the_tree_it_judges.py` and the encoding file keep their #923 cases, and the hardening file its prose cases and the parity arm's.

**The move check** (`executed`):

`bin/test-layout --moved 9818ee1a --from tests/test_commit_review_gate.py tests/test_routing_is_recorded.py tests/test_the_implementer_is_recorded.py tests/test_optin_home.py tests/test_gates_do_not_fail_open.py tests/test_guard_resolves_the_tree_it_judges.py tests/test_local_mode_resolves_under_the_git_dir.py tests/test_chain_hooks.py tests/test_chain_hooks_hardening.py tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py --to tests/test_commit_review_gate.py tests/test_routing_is_recorded.py tests/test_the_implementer_is_recorded.py tests/test_optin_home.py tests/test_guard_resolves_the_tree_it_judges.py tests/test_local_mode_resolves_under_the_git_dir.py tests/test_chain_hooks_hardening.py tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`

`test-layout: moved: 144 old cases, 187 items against 187 at 9818ee1a991f, 90 failed`, exit 1. Each failure line was read:

- 32 lines are the fixture condition alone: `fixture _the_press_is_read_off_the_session_id: requested in the working tree only`, one per moved case, the file's autouse fixture, as `questions.md` says. It replaces the press reader on the module the file loads, and every moved case runs the hook as a process or loads a copy of its own, so no verdict changed.
- 53 lines are the routing file's 27 old cases and the 26 cases they became, edited on purpose. Their helper was `gate(repo)`, and this file's `gate` is the loaded module, so the helper is `commit_gate(repo)`. Two of them are one now: `--pairs` named the chain and the direct declaration, which became `test_a_declared_item_commits_without_a_prompt`, parametrized over the answer and still carrying `routing-read-first`.
- 5 lines are one merge. `--pairs` named the hardening file's heredoc-message and env-prefix cases, and its cd-chain case with the opt-in file's new-home case; once each pair was merged, the two merged cases were a pair too, so the four are one, `test_commit_gate_fires_on_the_new_home`, parametrized over the four commands. `opt_in` and `home` make the same directory.

No move needed repair. As first placed, before the merges, the check ended `144 old cases, 187 items against 187 at 9818ee1a991f, 90 failed` too, with 36 fixture lines and the 54 routing lines. `--pairs` then names no pair in the changed files.

**Helpers.** The local-mode file's `local` fixture and the hardening file's `stage` serve both files and the new one, so they are in `tests/conftest.py`; `stage` now runs conftest's `git`, which checks the exit, where the hardening file's did not. The routing file's `declare` is in the new file under its name. Three helpers resolve to conftest's or the new file's where their old file had its own, and the move check reads none of them, so they are named here:

- The routing cases' `payload` and `reason_of` are conftest's. The `payload` gives the same dict for every call they make. conftest's `reason_of` raises on a silent output where the routing file's returned `""`, and every call is on a stop.
- The implementer case's `declare` is the routing file's, which writes the same declaration under another item id, with and without the `Implementation` row.
- `test_gate_rearms_after_commit_moves_head` runs conftest's `git`, which checks the exit; its two commands succeed in the `repo` fixture.

`CHOICE_DIR` is read from the loaded gate, and `optin` and `hooks/routing.py` are loaded once at the file's head.

**The names rewritten** (`executed`, `git grep` for each moved or removed file). `SECURITY.md` said `tests/test_gates_do_not_fail_open.py` exists for the fail-open class alone, and now says each gate's test file holds its cases for that class. `skills/verify/SKILL.md`'s `arm-check` example runs `tests/test_commit_review_gate.py`. `tests/test_a_shrunken_corpus_declines_to_judge.py#LISTS_A_FIXTURE` names the uncommitted-declaration case under the new file. `tests/test_the_direct_answer_owes_the_sealers_record.py` pins the first option's docstring in the new file, and its docstring says so. The docstrings of `tests/test_dispatch.py` (a citation of the removed file, dropped), `tests/test_question_gate.py`, `tests/test_first_setup_asks_once.py` and the four files that keep cases name the new places. What stands: `tests/test_optin.py`, `tests/test_session_lease.py` and `tests/test_worktree_guard.py` name the removed files as where their own cases came from; `tests/test_review_axes.py` describes the repository issue #57 measured; and `tests/test_arm_check.py` names `tests/test_chain_hooks.py#reader_blanking_passes`, which left the tree at 8350c578 (#923), before this branch.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `hooks/commit-review-gate.py` with `--tests "bin/test tests/test_commit_review_gate.py -q -p no:xdist -x"`, at the tree committed as f5185d67; the old column in an archive of 9818ee1a with the worktree's `.venv`, against the ten old files, for the survivors only). 40 mutants, g1 to g40, one or two at the decision points of each class's function and of the functions the moved cases reach: `touches_code`, `read_mark`, `already_asked`, `declaration_hint`, the prompts and `judge`. An id here names a row of this table alone.

| # | Mutation | New file | Old files |
|---|---|---|---|
| g1, g2 | `_hides_a_commit` answers no commit past the bound; `_reads_a_commit` misses a commit segment | red | not run |
| g3 to g8 | `commit_invocations` finds no heredoc body's commit, no substitution's, no `eval`, no shell string; reads the comments; drops the glued view | red | not run |
| g9 | `commit_targets` groups by the directory's text, not its repository | SURVIVED | SURVIVED |
| g10 | `commit_targets` ignores the walk's base | red | not run |
| g11 | `commit_shape` reads no `-a` in a short cluster | SURVIVED | red |
| g12 | `commit_shape` reads no pathspec after `--` | SURVIVED | SURVIVED |
| g13 | `changed_paths` answers the paths where a `git diff` failed | SURVIVED | red |
| g14 | `touches_code` reads no path | red | not run |
| g15 | `commit_shape` takes a value option's value as a path | SURVIVED | SURVIVED |
| g16 | `read_mark` decodes strictly | red | not run |
| g17 | `has_marker` reads a substring | red | not run |
| g18 to g20 | `already_asked` never finds its marker; answers no on a write error; takes the session id as a path | red | not run |
| g21 to g24 | the header spells no number; `ask_reason` drops the third way; `question_reason` counts two options; `waiver_form` drops the quotes | red | not run |
| g25, g26 | `automation_pressed` reads a raise as the press; takes any truthy answer | red | not run |
| g27, g28 | `unreadable_reason` calls a mixed set a construct; counts one path twice | red | not run |
| g29, g30 | `declaration_hint` answers nothing where `relpath` raises; never relative | red | not run |
| g31 to g34 | `judge` honours no waiver; the review arm never stands; the parity arm never stands; reads no HEAD | red | not run |
| g35 to g40 | `main`: no unparsed fallback; a session id where there is none; standing outside an opted-in session; no further repository announced; the reading stands aside for a command that is not plain; a `cd` names no directory | red except g38, SURVIVED | g38 SURVIVED |

The batch ran 34 red and 6 survived in 683.7 s after a 30.2 s baseline; the old column ran 2 red and 4 survived in 270.6 s. g9, g12, g15 and g38 are old gaps: the group's old files miss them too. g38 is red on `tests/test_gate_judges_the_repo_it_commits_to.py::test_or_reaches_both_the_session_and_the_destination` in the working tree (`executed`, 38.5 s), a case that did not move. g11 and g13 are red on the old files, and the cases that kill them did not move: `bin/test tests/test_chain_hooks_hardening.py -q -p no:xdist -x -k parity` in the working tree is red on both (`executed`, 13.4 s), the parity arm's cases the table above keeps there. So the move lost neither, and no case was added: a case for either in the new file would be a second copy of a hardening case that stands. The exact replacements are kept with the build's driver outside the tree.

**Phase 4's survivors** (`executed`). h4, conftest's `git` always checking the exit, run against `tests/test_commit_review_gate.py` with `-x`: SURVIVED, 139 passed in 99.8 s. The file now calls conftest's `git` more, and every call it makes succeeds, so no case reaches the unchecked branch; it stays an old gap. h2, h6, h12 and h23 are not reached by this group's files: no moved case calls `read`, `commit_everything_as_e`, `imported_roots` or `repo_relative` (`read`).

**Cases and seconds** (`executed`, serial, pytest's own figure): 188 items in 28.61 s before, over the ten files at 9818ee1a, 75 of them the new file's; 188 items in 29.63 s and 30.88 s after, over the eight files, on a machine at load average 24 to 40. The new file alone: 139 items in 22.41 to 25.52 s.

**The real-git cases kept.** Every moved `Test_main` case runs the hook as the harness does, against the `repo` fixture or a repository of its own, where the gate asks git for the root, HEAD, the git directory and the staged paths; two add a linked worktree, whose declaration lives in the main tree's common directory. `Test_touches_code` stages into the `repo` fixture and reads the diff git gives.

**The boundary** (`executed`). At the tree committed as f5185d67, before the commit: the changed files, every file importing `stage` or requesting `local`, every file naming the moved or removed files, `SECURITY.md` or the verify skill, the `arm-check` files, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_docs_line_wrap.py`, 59 files: 2,973 passed and 13 skipped in 32.9 s. `bin/test-layout --check` exits 0, 164 files read, 125 declaring no `TARGET`; `--pairs` names no pair in the changed files; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed `.py` file clean. `tests/test_conftest.py` was named for that run and a filter of the list dropped it; it ran at group 15's boundary, over a tree holding group 14: 8 passed.

### Batch B, `hooks/`, group 15, at f1d13be0

**The `check:` lines** (`executed`, `git grep` over the `check:` lines of `docs/`, `CONTRIBUTING.md`, `skills/` and `agents/`). No line names either old file, and no case of the group carries a rule marker.

**The module.** `hooks/blocks.py`, the first shared reader, whose own cases were four of `tests/test_the_hooks_hide_what_a_renderer_hides.py` and two of `tests/test_every_reader_ends_a_line_where_gfm_does.py`, now `tests/test_blocks.py`:

- `Test_gfm_lines`: the splitter's two cases, renamed `test_refuses_to_end_a_line_at_any_of_the_eight` and `test_accepts_a_text_without_the_eight_as_splitlines_splits_it`.
- `Test_walk_text`: the walk's three answers per reader line, renamed `test_refuses_to_claim_a_piece_inside_its_lines_open_comment`, `test_refuses_to_claim_a_piece_inside_other_inline_html_its_line_left_open` and `test_accepts_an_unclosed_fence_at_the_reader_line_it_starts`.
- `Test_module`: `walk`'s paragraph case, under its name, the one case of a function with no class.

6 old cases, 10 items. `bin/test-layout --check` reports `columns`, `fence_closes`, `fence_only`, `fence_opener`, `leaves_html_open`, `leaves_open`, `not_spaces_after_the_run` and `walk` with no class: no undeclared case calls one of them as its subject.

**Left where they stand.** The renderer file keeps halves 1 and 2, the walk and the config and routing readers held to the CommonMark oracle over the shapes and a generated corpus, which `spec.md` *What the frame decided* keeps where it is. The splitter file keeps `test_every_copy_of_the_splitter_is_the_readers`, which holds the copies in other modules to this one, and the other modules' cases. `tests/test_unverified_rows_close.py::test_the_fence_walks_agree_shape_by_shape` holds this module's two fence walks to `unverified_check.py`'s and to `hooks/config.py#fence_map`, files against each other, and stays.

**The move check** (`executed`):

`bin/test-layout --moved 06d0f554 --from tests/test_the_hooks_hide_what_a_renderer_hides.py tests/test_every_reader_ends_a_line_where_gfm_does.py --to tests/test_blocks.py tests/test_the_hooks_hide_what_a_renderer_hides.py tests/test_every_reader_ends_a_line_where_gfm_does.py`

`test-layout: moved: 31 old cases, 142 items against 142 at 06d0f55453fc, 0 failed`, exit 0. No mutation table. `--pairs` names no pair in the new file.

**Helpers.** `INLINE_KINDS` is data both files read, so it is in `tests/block_shapes.py`; `texts` and `SPLITLINES_ONLY` serve both the splitter's cases and the copies' case, so they are in `tests/conftest.py`. `INLINE_OPEN_CLOSE` moved with the cases that read it. The splitter's cases read `reader.gfm_lines`, where `reader` was `unverified_check.py`, whose `gfm_lines` is this module's own; in the new file `reader` is this module, under the name the bodies read. The move check reads no module-level name, so it is named here.

**Cases and seconds** (`executed`, serial): 142 items in 9.33 s before, the two old files in an archive of 06d0f554 with the worktree's `.venv`; 143 items in 5.19 and 5.33 s after, over the three files, the census item among them.

**The real-git cases kept.** None: the walk and the splitter read text.

**Phase 4's survivors.** None is reached: the new file calls `census_case`, `load_hook_module` and `texts` from `tests/conftest.py` (`read`).

**The boundary** (`executed`). At the tree committed as f1d13be0, before the commit: the three files, every file naming `block_shapes`, `blocks.py` or the moved helpers, the `git_listing` files, the censuses, `tests/test_test_layout.py` and `tests/test_chain_hooks_hardening.py`, 34 files: 3,331 passed and 3 skipped in 50.1 s; `tests/test_conftest.py`: 8 passed. `bin/test-layout --check` exits 0, 165 files read, 125 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff checks and formats each changed file clean.

### The shared readers stop at `hooks/config.py`

**The `check:` lines its group meets** (`executed`, `git grep`; the rule `read`). `docs/one-root-by-lifetime.md` line 223 and `docs/one-root-by-lifetime.ko.md` line 212 name `tests/test_the_mode_question_is_asked_once.py` for the rule *A cell may carry an escaped pipe, and one line that will not parse is named rather than treated as the end of the table*. The config reader's cases in that file hold it; group 4 left them there for this group, and its record says the two lines stand under them. `spec.md` *Rule changes* carries no item for either line, so the config reader's group does not start, and the spawn hands back at this boundary.

**What the later reader groups meet** (`executed`, `git grep` over the `check:` lines for every undeclared file that loads the reader; whether the reader's own cases hold each line's rule is `unverified` until its group reads them, and the spawn that places each reader answers it):

| Reader | Lines naming the files it draws from, with no item in `spec.md` |
|---|---|
| `hooks/config.py`, beside the two above | `docs/the-record-layout.md` 29, 150, 170, 177; `agents/warden.md` 99; `docs/the-pact.md` 18, 31, 45, 61, 75; `docs/the-broad-gate.md` 33; `skills/writing-style/SKILL.md` 275; `docs/one-root-by-lifetime.md` 197, 214 and `docs/one-root-by-lifetime.ko.md` 189, 204 |
| `hooks/gate.py` | `docs/the-review-and-parity-arms.md` 141, whose rule its one case in an undeclared file, the hardening file's backstop case, holds (`read`, group 14's table) |
| `hooks/tokens.py` | none: its candidate files are named by no line, and the waiver file names `tokens` in a docstring alone |
| `hooks/cmdline.py` | `docs/commit-review-gate-spec.md` 125 and 139, group 14's; `docs/branch-and-release.md` 146; `docs/the-commit-gate-inside-git.md` 183 |
| `hooks/cmdline_base.py` | `docs/the-commit-gate-inside-git.md` 183 |

### The sixth spawn, after the framer's survey at 0b134a29

**What this spawn was asked.** The commit gate's cases that the five lines of group 14 held, with the commit gate's mutants run again, g9, g11 and g13 among them; then the shared readers from `hooks/config.py` on, one group each, `hooks/cmdline.py`'s text-reading cases moving as they stand into `tests/test_cmdline.py`; the two cases groups 9 and 10 left in `tests/test_local_mode_resolves_under_the_git_dir.py`; then the seven directories outside `hooks/`. Phase 4's h2, h6, h12 and h23 are re-run where a group rebuilds a module whose cases reach one. A group meeting a `check:` line with no verdict in the frame records it and keeps the line, instead of stopping.

**Whether the frame holds** (`read`). It holds. `spec.md` *Rule changes* carries an item for each of the five lines group 14 named: `docs/commit-review-gate-spec.md` *The PreToolUse reading of a commit* to `tests/test_commit_review_gate.py` and `tests/test_worktree_consent.py`; its two *Which repository* lines to `tests/test_commit_review_gate.py` and `tests/test_cmdline.py`; `docs/the-review-and-parity-arms.md` *Review arm* to `tests/test_commit_review_gate.py`, and *Parity arm* to that file, `tests/test_commitgate.py` and `tests/test_gate.py`. The fifth spawn's stop above no longer holds: every line the shared readers meet has a verdict in `spec.md`, an item or a row of *The check lines the remaining groups meet*.

**The order of the groups** (`read`). The parity arm's case of `hooks/commitgate.py` went first, alone, so its module's check could pass on its own instead of running its mutants beside the commit gate's. Then the commit gate's cases; then the two readers whose own cases are fewest, `hooks/gate.py` and `hooks/tokens.py`, each one case; `questions.md` orders the readers only after the `hooks/` groups whose files hold their cases, and a short group closes with a complete record where `hooks/config.py`'s and `hooks/cmdline.py`'s, each drawing from more than twenty files, would not fit what was left of this spawn.

### Batch B, `hooks/`, group 16, at b8e201e1

**The module.** `hooks/commitgate.py`'s parity case, `test_a_diff_git_could_not_take_is_asked_about_at_pre_commit`, from `tests/test_chain_hooks_hardening.py` into `tests/test_commitgate.py`'s `Test_pre_commit`, under its name. `parity_repo`, `parity_only` and `a_git_whose_diff_fails` serve the hardening file and both new files, so they moved to `tests/conftest.py`.

**The move check** (`executed`):

`bin/test-layout --moved 0b134a29 --from tests/test_chain_hooks_hardening.py tests/test_commitgate.py --to tests/test_chain_hooks_hardening.py tests/test_commitgate.py`

`test-layout: moved: 56 old cases, 71 items against 71 at 0b134a29b35e, 0 failed`, exit 0. No mutation table. `--pairs` names no pair in `tests/test_commitgate.py`.

**Cases and seconds** (`executed`, serial): 72 items in 11.45 s before, the two files in an archive of 0b134a29 with the worktree's `.venv`; 72 items in 12.12 s after.

**The real-git cases kept.** The moved case runs `pre_commit` in the `repo` fixture with a `git` that refuses `diff`, which is the failure the arm has to read.

**The boundary** (`executed`). At the tree committed as b8e201e1, before the commit: the two files, the censuses, `tests/test_test_layout.py` and `tests/test_conftest.py`, 303 passed. `bin/test-layout --check` exits 0, 165 files read, 125 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `hooks/`, group 17, at 67a86c57

**The modules.** `hooks/commit-review-gate.py`, whose cases the five lines held, and `hooks/worktree_consent.py`, one of whose cases shared an old file with them:

- From `tests/test_gate_judges_the_repo_it_commits_to.py`, every case that runs the hook or calls `commit_invocations` or `commit_targets`, 54 of its 82: `Test_commit_invocations` takes the five that call it, `Test_main` the 43 that run the hook, and `Test_module` the three of `commit_targets`, which have no refusing case to pair with, and the three that read the gate's imports (a broken guard, a sibling load, a broken `cmdline.py`). The file keeps `hooks/cmdline.py`'s walk, read through `commit_dirs` with no git, for the reader's group.
- From `tests/test_an_automation_run_meets_no_commit_prompt.py`, its 17: 16 into `Test_automation_pressed`, and `test_an_answer_to_another_question_leaves_the_press_standing`, which calls `worktree_consent.automation_answered` alone, into `tests/test_worktree_consent.py`'s `Test_automation_answered`.
- From `tests/test_a_commit_behind_a_reserved_word_is_judged.py`, the three that run `main` over its `SHAPES`, into `Test_main`; the file keeps the reading's rows, and `tests/test_commit_review_gate.py` imports `SHAPES` and `HERE` from it.
- From `tests/test_the_waiver_can_be_typed.py`, its six: five into `Test_main`, and `waiver_form`'s one into `Test_module`.
- From `tests/test_chain_hooks_hardening.py`, the parity arm's twelve, into `Test_main`.

The automation and waiver files are named by `check:` lines whose items are not yet settled, so each keeps a docstring naming where its cases went, and no case.

**The press stub** (`executed`). The file's autouse `_the_press_is_read_off_the_session_id` answers the press from the session id. Under it three moved cases turn red (a later answer that takes the press back, a reader that raises, a read only once a stop is decided) and two pass without testing what they say (the press read against the session's own repository, every way of not finding the press), because each builds a transcript and asks the reader for it. `Test_automation_pressed` overrides the fixture under the same name, as `questions.md` says, and lifts the stub only for a case that requests `projects`, so its two cases from phase 5 keep the stub. `worktree_consent` in the file is the module the gate imported by its plain name, which the cases patch.

**The move check** (`executed`):

`bin/test-layout --moved b8e201e1 --from tests/test_commit_review_gate.py tests/test_worktree_consent.py tests/test_an_automation_run_meets_no_commit_prompt.py tests/test_gate_judges_the_repo_it_commits_to.py tests/test_a_commit_behind_a_reserved_word_is_judged.py tests/test_the_waiver_can_be_typed.py tests/test_chain_hooks_hardening.py tests/test_no_shape_the_base_stops_reads_silent.py --to tests/test_commit_review_gate.py tests/test_worktree_consent.py tests/test_gate_judges_the_repo_it_commits_to.py tests/test_a_commit_behind_a_reserved_word_is_judged.py tests/test_chain_hooks_hardening.py tests/test_no_shape_the_base_stops_reads_silent.py`

`test-layout: moved: 292 old cases, 409 items against 409 at b8e201e1f012, 115 failed`, exit 1. Each failure line was read:

- 66 lines are the fixture condition alone, `fixture _the_press_is_read_off_the_session_id: requested in the working tree only`, one per moved case whose body is unchanged.
- 2 lines are `Test_automation_pressed`'s two phase 5 cases, `its definition differs from the base's`: the class's override.
- 30 lines are 15 bodies edited on purpose, each named twice. The automation file's `make_repo` came from `tests/test_no_shape_the_base_stops_reads_silent.py` and the gate file's `make_repo` takes other arguments, so the first is `tests/conftest.py#staged_repo` and fourteen automation cases call it under that name; the consent case calls it too, and reads the module its file loads, `wc`.
- 6 lines are the reserved-word file's three bodies: its `say` used a fixed session and answered the decision alone, so they call the file's `decision(...)[0]`.
- 2 lines are `test_the_same_root_forms_answer_what_the_release_did`, whose nested `state_half` docstring is a string in the body and moved four columns right with the class.
- 9 lines are two merges. `--pairs` named five gate cases that hand a commit to a shell (a heredoc fed to bash, an `eval`, a body inside a body, an `eval` of an `eval`, an `eval` of a substitution), whose bodies differ by the command alone; they are `Test_main::test_refuses_a_commit_a_body_or_an_eval_hands_to_a_shell`, parametrized over the five, still carrying `one-heredoc-shape-is-data`. It named the unreadable `cd` and the unreadable `-C` where the plugin has no standing; they are `Test_main::test_accepts_silence_on_an_unreadable_target_where_the_plugin_has_no_standing`.

No move needed repair. `--pairs` then names no pair in the two changed module files.

**Helpers.** `sh` serves the gate file and the walk left in `tests/test_gate_judges_the_repo_it_commits_to.py`, and `staged_repo` the gate file and the consent file, so both are in `tests/conftest.py`; `tests/test_no_shape_the_base_stops_reads_silent.py` no longer builds a repository for anyone. The gate file's `make_repo` with its template, `released_hooks`, the waiver's shell probes, `opted_in_repo` with its template, and the automation file's `press`, `say`, `sequence` and their constants moved into `tests/test_commit_review_gate.py`. `unreadable` there reads the gate's own `Unresolved`, which is the class `commit_targets` builds. `tests/test_a_shrunken_corpus_declines_to_judge.py#CONTENT_FROM_GIT` names `tests/test_commit_review_gate.py#released_hooks`.

**The mutation tables** (`executed`, one `bin/mutation-check` batch per module over the file as committed at 67a86c57, `-x` in `--tests`; the old column in an archive of b8e201e1 with the worktree's `.venv`, against the eight old files, `test_the_same_root_forms_answer_what_the_release_did` deselected because an archive holds no tag).

The commit gate runs group 14's g1 to g40 again, as they stand in that record, and four more at `main`'s press, which the moved automation cases reach: g41 reads the press against the target's root, g42 reads it before any stop is decided, g43 drops the press from the unreadable arm's text, g44 gives the resolved arm the question in place of the automation text. Against `tests/test_commit_review_gate.py`: 44 mutants, 42 red, 2 survived, in 1148.5 s after a 54.2 s baseline. The old column ran g12 and g15: both survived, in 177.0 s.

| # | Group 14 | Now | Old files at b8e201e1 |
|---|---|---|---|
| g9, `commit_targets` groups by text | survived, an old gap | red, 44.3 s | not run |
| g11, `commit_shape` reads no `-a` in a cluster | survived; the hardening file's parity cases killed it | red, 58.7 s | not run |
| g12, `commit_shape` reads no pathspec after `--` | survived, an old gap | survived | survived, an old gap |
| g13, `changed_paths` answers paths after a failed diff | survived; the parity cases killed it | red, 119.8 s | not run |
| g15, `commit_shape` takes a value option's value as a path | survived, an old gap | survived | survived, an old gap |
| g38, `main` announces no further repository | survived; `test_or_reaches_both_the_session_and_the_destination` killed it | red, 41.2 s | not run |
| g41 to g44, `main`'s press | not in the table | red | not run |

Every other mutant of g1 to g40 is red as in group 14. The parity cases and the gate file's case that killed g11, g13 and g38 from their old files now kill them in the new file.

`hooks/worktree_consent.py` had no table; group 11's check passed it. Its 25 mutants, k1 to k25, sit at one or two decision points of each function: `main`'s event, isolation and session tests; `consent`'s catch and its record read first; `consent_path`'s dot names; `granted`'s file test; `record`'s write error; `leading_phrase`'s cut; `is_routing_question`'s each-once test; `transcript_for`'s one match and its payload path; `_routing_preset`'s `multiSelect` and its `Other` answer; `_routing_answer`'s routing question and its None for another question; `last_routing_answer`'s sidechain, link, clone and last answer; `segment_cwd`'s `-C`; `place`'s fallback; `creation_directory`'s comment drop and its placement; `split_with_separators`' backslash doubling. Against `tests/test_worktree_consent.py`: 25 mutants, 20 red, 5 survived, in 62.4 s; the old column ran the five: all survived, in 330.0 s.

| # | Mutation | New file | Old files |
|---|---|---|---|
| k3 | `main` records a payload with no session id | SURVIVED | SURVIVED |
| k10 | `is_routing_question` takes a label set without counting each once | SURVIVED | SURVIVED |
| k13 | `_routing_preset` reads an absent `multiSelect` as single-select | SURVIVED | SURVIVED |
| k16 | `_routing_answer` reads an answer to another question as taking the press back | red | not run |
| k23 | `creation_directory` reads comments | SURVIVED | SURVIVED |
| k25 | `split_with_separators` doubles no backslash on Windows | SURVIVED | SURVIVED |

The five survivors are old gaps: no old case sends a session-less payload to the writer, two routing labels alike, a result with no `multiSelect`, a creation behind a comment, or a Windows path through the writer. k16 is the mutant the moved consent case answers. No case was added. The exact replacements are kept with the build's driver outside the tree.

**Cases and seconds** (`executed`, serial, pytest's own figure): 411 items in 55.57 s before, the eight files in an archive of b8e201e1, where the release comparison fails for want of a tag; 410 items in 52.38 s after over the eight files, measured with group 18's case already gone from the hardening file. The new commit gate file alone ran its batch's baseline in 54.2 s.

**The real-git cases kept.** Every moved `Test_main` case: the hook run as the harness runs it, in a repository copied from a template built once or in the `repo` fixture, two or three repositories where the command crosses them, a linked worktree where a `cd -` returns, a parity mark under the git directory, and the release's own hooks read out of the last tag. The waiver's cases run the advised form in every shell on PATH against real git; the press cases run `main` in the process over a repository git placed, which is what the press is read against.

**Phase 4's survivors.** None of h2, h6, h12 and h23 is reached: no moved case calls `read`, `commit_everything_as_e`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). Before the merges, at the tree committed as 67a86c57 less the merges: the eight files, `tests/test_a_shrunken_corpus_declines_to_judge.py`, `tests/test_commitgate.py`, the censuses, `tests/test_test_layout.py` and `tests/test_conftest.py`, 13 files: 691 passed. After the merges, the merged cases: 7 passed. `bin/test-layout --check` exits 0, 165 files read, 125 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `hooks/`, group 18, at 95991e42

**The module.** `hooks/gate.py`, the second shared reader, whose one case in an undeclared file was the hardening file's backstop case, `test_the_backstop_hands_the_parity_arm_none_where_git_could_not_list`, now `tests/test_gate.py`'s `Test_module` under its name. Its other readings run through the hooks that render them, in the commit flow and the commit gate's and `hooks/commitgate.py`'s files; `--check` reports its functions with no class.

**The move check** (`executed`): `bin/test-layout --moved 67a86c57 --from tests/test_chain_hooks_hardening.py --to tests/test_gate.py tests/test_chain_hooks_hardening.py` ends `test-layout: moved: 27 old cases, 27 items against 27 at 67a86c5730f0, 0 failed`, exit 0. No mutation table.

**Cases and seconds** (`executed`, serial): 27 items in 1.51 s before, the hardening file at 67a86c57; 28 items in 0.48 s after, the census item among them.

**The boundary** (`executed`). At 95991e42: the two files, the censuses, `tests/test_test_layout.py` and `tests/test_conftest.py`, 259 passed. `bin/test-layout --check` exits 0, 167 files read; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean.

### Batch B, `hooks/`, group 19, at e1e39bf7

**The module.** `hooks/tokens.py`, the third shared reader. `test_a_token_is_a_bare_word_and_nothing_else` leaves `tests/test_the_old_spellings_reach_the_hook.py` with `TOKEN_CASES` for `tests/test_tokens.py`'s `Test_module`, its one case, which no refusing case pairs with. The old file keeps `test_the_three_token_reads_answer_as_one`, which holds the commit gate's `has_marker` and the worktree guard's `has_token` to `tokens.given`, a check across files that `spec.md` *What the frame decided* keeps where it is; its `_corpora` reads `TOKEN_CASES` from the new file. `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py`'s three cases pin `hooks/one_heredoc.py`, `hooks/cmdline.py` and this module together and wait for `hooks/cmdline.py`'s group.

**The move check** (`executed`): `bin/test-layout --moved 95991e42 --from tests/test_the_old_spellings_reach_the_hook.py --to tests/test_tokens.py tests/test_the_old_spellings_reach_the_hook.py` ends `test-layout: moved: 2 old cases, 19 items against 19 at 95991e42b3d5, 0 failed`, exit 0. No mutation table.

**Cases and seconds** (`executed`, serial): 19 items in 0.25 s before; 20 items in 0.10 s after.

**The boundary** (`executed`). At e1e39bf7: the two files, `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py` and `tests/test_worktree_guard.py`, which `_corpora` imports, the censuses, `tests/test_test_layout.py` and `tests/test_conftest.py`, 797 passed and 3 skipped. `bin/test-layout --check` exits 0; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean.

### The local-mode file, group 20, at 6277911e

**The cases.** The two that groups 9 and 10 left in `tests/test_local_mode_resolves_under_the_git_dir.py`: `test_the_implementer_notice_names_the_local_path` into `tests/test_implementer_notice.py`'s `Test_main`, and `test_a_scratch_marker_under_the_common_directory_keeps_every_gate_silent` into `tests/test_optin.py`'s `Test_module`, because each of the three gates it runs reads the marker through `optin`. `declare_smith` serves both files from `tests/conftest.py`; its default item is conftest's `ITEM`, which the notice case's assertion reads too. The old file held nothing else and no `check:` line names it, so it went, and `tests/test_first_setup_asks_once.py`'s docstring names the notice's file in its place.

**The move check** (`executed`): `bin/test-layout --moved e1e39bf7 --from tests/test_local_mode_resolves_under_the_git_dir.py tests/test_implementer_notice.py tests/test_optin.py --to tests/test_implementer_notice.py tests/test_optin.py` ends `test-layout: moved: 53 old cases, 55 items against 55 at e1e39bf7b23d, 0 failed`, exit 0. No mutation table.

**Cases and seconds** (`executed`, serial): 57 items in 4.30 s before, the three files at e1e39bf7; 57 items in 4.84 s after, over the two.

**The boundary** (`executed`). At 6277911e: the two files, `tests/test_first_setup_asks_once.py`, `tests/test_implementer_mark.py` and `tests/test_commit_review_gate.py`, which read the conftest helpers beside the new one, the censuses, `tests/test_test_layout.py` and `tests/test_conftest.py`, 608 passed. `bin/test-layout --check` exits 0, 166 files read, 124 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean.

### The seventh spawn

**What this spawn was asked.** The three shared readers left in `hooks/`, one group each, `hooks/config.py` split along its public functions where one group would not close with a complete record, and `agents/warden.md` line 99 rewritten in its group's commit; `hooks/cmdline.py`'s text-reading cases moving as they stand into `tests/test_cmdline.py`, with the constant `TARGET = "/target"` of `tests/test_what_the_reader_understands.py` renamed when its cases land in a file declaring `TARGET`; then `hooks/cmdline_base.py`; then the seven directories outside `hooks/` in `plan.md`'s order, rule 3 where an old file prices at 60 s or more, each group rewriting the lines outside `docs/` that `spec.md` *The check lines the remaining groups meet* assigns it, and the group placing `skills/verify/scripts/arm_check.py`'s cases correcting `tests/test_arm_check.py`'s docstring. A `check:` line with no verdict in `spec.md` is recorded and left as it is. Phase 4's h2, h6, h12 and h23 are re-run where a group rebuilds a module whose cases reach one.

**Whether the frame holds** (`read`). It holds for `hooks/config.py`. Every `check:` line its groups meet has a verdict in `spec.md`: `agents/warden.md` line 99 has its row; `docs/one-root-by-lifetime.md` lines 197 and 223, their Korean twins at 189 and 212, and `docs/the-pact.md` lines 18, 31, 75 and 126 have their items; `docs/the-pact.md` lines 45 and 61, `docs/one-root-by-lifetime.md` line 214 and its twin's 204 are lines a drained file keeps. `docs/the-record-layout.md` line 29 names the fold file for its size rule, which the policy root's case does not hold, so moving that case changes nothing the line names.

### Batch B, `hooks/`, group 21, at 1b3e6978

**How `hooks/config.py` is split** (`read`). Its cases sit in more than ten files, and one case of `tests/test_a_signer_declares_its_pact.py` and six of `tests/test_pact_check.py` read a module-level `PACT` that is the pact's text in the first file and the pact's path in the second, so placing both in one file changes one side's bodies and sends the module to the mutants. The groups are: this one, the small files; group 22, the reader cases of `tests/test_the_mode_question_is_asked_once.py`; group 23, the pact's readers, last, so the mutants run once over every case the module's file holds.

**The cases.** Into `tests/test_config.py`, each with its body:

- `Test_reference_roots`: the seven resolver cases (C1) of `tests/test_a_reference_root_is_read_and_never_taken.py`, two renamed `test_accepts_a_row_naming_its_prefixes_with_or_without_a_slash` and `test_refuses_a_row_written_twice_or_a_file_that_will_not_read`.
- `Test_normalise_remote`: the three cases of `tests/test_the_records_can_be_carried_out_and_in.py`, two renamed `test_accepts_remote_urls_that_reduce_to_one_host_and_path` and `test_refuses_to_reduce_two_different_repositories_to_one`, with their `seal` fixture.
- `Test_config_rows`: the six cases of `tests/test_the_pull_request_language_is_the_repositorys.py` that call `items` on a text written for them, two renamed `test_accepts_an_item_value_table_and_no_other` and `test_refuses_a_second_table_further_down_as_more_rows`.
- `Test_gfm_table`: the three cases of `tests/test_one_table_walker_reads_what_gfm_renders.py` that ask no oracle, two renamed `test_refuses_a_hidden_line_directly_above_the_header` and `test_accepts_the_rows_above_a_heading_piece_and_refuses_the_row_below`.
- `Test_module`: `policy_root`'s one case from `tests/test_a_document_has_room_for_the_next_fold.py` and `test_the_baseline_is_the_first_code_span_of_its_one_row` from `tests/test_chain_check.py`, each under its name, one case of a function with no refusing partner.

21 cases, 36 items, and the census item.

**Helpers.** `write_config` in `tests/conftest.py` now makes the directory it writes into, as the reference-root file's own copy did, and that copy is gone; its other callers write into a directory that exists. `parity_file` and `BASELINE` serve `tests/test_chain_check.py` and the new file, so they are in `tests/conftest.py`. The new file reads the row reader through `items = config.config_rows` and `_config_reader()`, which answers the module the file loaded where the old file loaded a copy per call; the move check reads neither, so they are named here.

**Left where they stand.** In the reference-root file: the census of every `bin/` command, the pinned constants of `settle.py` and `hooks/routing.py`, the planted team `specs/` run through three checks, all comparing shipped files with each other, and the two prose cases, #923's. `tests/test_a_script_copied_alone_exits_2.py::test_a_hook_reader_copied_without_the_walk_names_it` holds `hooks/config.py` and `hooks/routing.py` to one sentence in one parametrized body, a check across files that stays. The oracle file keeps every case that asks cmark-gfm, as `spec.md` *What the frame decided* keeps a check against an oracle. In the pull request language file, `configured_language` and its cases model a session's reading of the row and stay, with `test_this_file_loads_the_one_reader_and_not_a_copy_of_it`, which holds that model to the one reader.

**The move check** (`executed`):

`bin/test-layout --moved fb0c5dfc --from tests/test_a_reference_root_is_read_and_never_taken.py tests/test_a_document_has_room_for_the_next_fold.py tests/test_the_records_can_be_carried_out_and_in.py tests/test_chain_check.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_one_table_walker_reads_what_gfm_renders.py --to tests/test_config.py tests/test_a_reference_root_is_read_and_never_taken.py tests/test_a_document_has_room_for_the_next_fold.py tests/test_the_records_can_be_carried_out_and_in.py tests/test_chain_check.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_one_table_walker_reads_what_gfm_renders.py`

`test-layout: moved: 193 old cases, 803 items against 803 at fb0c5dfccd2f, 0 failed`, exit 0. No mutation table. `--pairs` names no pair in the new file.

**The lines rewritten.** `agents/warden.md` line 99 names `tests/test_a_reference_root_is_read_and_never_taken.py tests/test_config.py`, as `spec.md` assigns. `hooks/config.py`'s comment on `HOME` names the new file as the one holding it equal to `hooks/optin.py#HOME`; the docstrings of the records file, the reference-root file and the oracle file name where their cases went.

**Cases and seconds** (`executed`, serial, pytest's own figure): 804 items in 39.68 s before, the six old files at fb0c5dfc; 805 items in 38.01 s after, over the seven files, the census item among them.

**The real-git cases kept.** `Test_reference_roots::test_local_mode_reads_the_row_under_the_git_directory` inits a repository and asks git for its common directory, where the local-mode root sits. No other case runs git.

**Phase 4's survivors.** None is reached: no moved case calls `read`, `commit_everything_as_e`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as 1b3e6978, before the commit: the changed files, every test file naming `warden.md`, `write_config`, `parity_file`, `BASELINE` or `test_config`, the `git_listing` files, the censuses, `tests/test_every_agent_reads_the_contract.py`, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 53 files: 3,933 passed and 13 skipped in 48.3 s. After the commit, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and the new file: 2,008 passed and 3 skipped. `bin/test-layout --check` exits 0, 167 files read, 124 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. `uvx ruff check` and `uvx ruff format --check` pass each changed `.py` file, one file per run.

### Batch B, `hooks/`, group 22, at 10f6ad94

**The cases.** The 33 cases of `tests/test_the_mode_question_is_asked_once.py` that call the reader as their subject, each with its body, into `tests/test_config.py`:

- `Test_config_rows`, 13: the #415 escape cases, the three-column row, the two fenced examples, the fence rule, the code-span delimiters, the three breaks inside inline HTML, the row and the header after a break GFM does not honour.
- `Test_config_value`, 7: `test_one_row_is_its_value_and_no_row_is_none`, renamed `test_accepts_one_row_as_its_value_and_no_row_as_none`, and `test_an_item_written_again_below_the_stopping_line_has_no_value`, renamed `test_refuses_an_item_written_again_below_the_stopping_line`, with the fenced example of a row, the per-item refusal, the next heading's table, the line below the stop, and `test_a_line_that_will_not_parse_is_named_and_the_hook_still_says_nothing`, which group 4 left for this module.
- `Test_declared_mode`, 5: two renamed `test_accepts_the_row_from_the_root_the_folder_is_at` and `test_refuses_a_mode_row_written_twice`.
- `Test_config_table`, 3: two renamed `test_refuses_a_fenced_pipe_line_as_a_line_somebody_wrote` and `test_accepts_every_config_shape_as_the_frame_expects`, with the sixteen shapes.
- `Test_fence_map`, 3: two renamed `test_refuses_to_name_a_fence_inside_a_closed_comment` and `test_accepts_a_fence_nobody_closed_as_the_one_named`.
- `Test_unfenced`, 2: renamed `test_refuses_a_commented_row_in_either_line_ending` and `test_accepts_every_line_under_a_mid_line_comment`.

**Left where they stand**, for the group that places `skills/implement/scripts/seal.py`'s light files: the ten cases that call `seal.py`'s `write_row` or `with_row` as their subject, among them `test_the_fence_rule_answers_the_same_for_a_crlf_file`, which holds the writer's CRLF walk beside the reader's, and `test_the_command_and_the_gate_read_one_parser`, which holds `seal.py`'s re-export of the reader. The file's docstring says so. `docs/one-root-by-lifetime.md` line 223 and its twin's 212 name this file for the rule *A cell may carry an escaped pipe*, whose writer clause these cases hold; `spec.md`'s items move both lines to `tests/test_config.py` alone (`unverified` whether the line then needs `tests/test_seal.py` as well, once that group places the writer's cases; the framer answers it, and the item is left as it stands).

**Helpers.** The file's function-scoped `config` fixture serves both files and is in `tests/conftest.py`, its definition unchanged, so the fixture condition holds; `tests/test_config.py` keeps its module-level `config`, which the fixture parameter shadows inside the cases that request it. `PIPED_TABLE`, `FENCED_ABOVE`, `FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN`, `FENCED_REFUSAL`, `UNDER_THE_COMMENT`, `crlf` and `shape_text` serve both files and are in `tests/conftest.py` too; `GATE`, the commented shapes and `LIVE` moved with the cases that read them.

**The move check** (`executed`):

`bin/test-layout --moved 92add28b --from tests/test_config.py tests/test_the_mode_question_is_asked_once.py --to tests/test_config.py tests/test_the_mode_question_is_asked_once.py`

`test-layout: moved: 65 old cases, 190 items against 190 at 92add28be86b, 0 failed`, exit 0. No mutation table. `--pairs` names no pair in the new file.

**Cases and seconds** (`executed`, serial, pytest's own figure): 191 items in 4.36 s and 3.35 s before, the two files in an archive of 92add28b run with the worktree's `.venv`; 191 items in 1.02 s and 0.43 s after, in the worktree.

**The real-git cases kept.** The seven `Test_declared_mode` and `Test_config_value` cases that take the `repo` fixture read a root in a repository git made, and `test_accepts_the_row_from_the_root_the_folder_is_at` asks git for the common directory of a local-mode root.

**Phase 4's survivors.** None is reached (`read`).

**The boundary** (`executed`). At the tree committed as 10f6ad94, before the commit: the two files, `tests/test_mode_gate.py`, `tests/test_seal.py` and `tests/test_a_signer_declares_its_pact.py`, which read `config_shapes` or the conftest helpers, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`: 2,265 passed and 3 skipped. `bin/test-layout --check` exits 0, 167 files read, 124 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean on each changed file.

### Batch B, `hooks/`, group 23, at ca726662

**The cases.** Into `tests/test_config.py`, the last of `hooks/config.py`'s:

- From `tests/test_a_signer_declares_its_pact.py`, the 17 reader cases: `Test_pact_declaration` takes the seven of `pact_declaration`, two renamed `test_accepts_one_pact_normalised` and `test_refuses_a_row_that_will_not_parse_and_never_reads_it_as_absent`; `Test_declared_pacts` takes `test_an_unreadable_config_is_no_declaration`; `Test_pact_signers` takes the nine of the `Signer` table, two renamed `test_accepts_the_signers_a_pact_lists_and_no_table_in_a_comment` and `test_refuses_a_pact_with_no_table_or_an_unfilled_one`.
- From `tests/test_pact_check.py`, the seven phase 5 left for this module, each running `check` over the pact's world: the signer config the walker refuses and the `Pact notify` row into `Test_declared_pacts`, renamed `test_refuses_a_signer_config_the_walker_refuses_with_exit_2` and `test_accepts_a_pact_notify_row_an_earlier_release_read_as_nothing`; the five of the `Signer` table into `Test_pact_signers`.

**Left where they stand.** In the signer file: `test_s4_the_configs_this_plugin_writes_or_copies_are_silent` and `test_the_template_and_the_config_skill_carry_the_pact_row_alone`, which read the configs and templates this plugin ships, and the routing step's sentences, the cases `spec.md` says hold `docs/the-pact.md` lines 45 and 61; and `test_seal_keeps_one_normaliser`, which holds `seal.py`'s re-export of the normaliser and waits, with the mode file's re-export case, for the group that places `seal.py`'s light files.

**Two bodies changed, and one merge.** The signer file's `PACT` is the pact's text and the pact_check file's `PACT` is its path, and one module holds one name, so the text is `PACT_TEXT` in the new file and the two cases that read it read it so. `--pairs` then named `test_a_signer_row_below_a_blank_line_is_refused` and `test_a_signer_written_as_an_autolink_is_never_passed_over`, whose bodies differ by the line added and the sentence printed; they are `Test_pact_signers::test_refuses_a_signer_the_walk_never_reads_and_prints_why`, parametrized over the two. It also names `test_accepts_the_signers_a_pact_lists_and_no_table_in_a_comment` with `test_s2_a_pact_headed_as_0_18_wrote_it_is_read_the_same`, which both read `PACT_TEXT`; the first pins the signers and the header, and the second that the old header reads to the same answer under its own word, so neither covers the other and they are not merged.

**Helpers.** The pact's world serves `tests/test_pact_check.py` and the new file, so `tests/conftest.py` holds it: `_template` and `world` with their definitions unchanged, `World`, `init`, `pact`, `old_header`, `clause`, `signer_config`, `grounding_row`, the URLs, `LOCATOR`, `PACT`, `SPEC`, `V1` to `V3`, `URL` and `ORDERS`, and `pact_check_modules`, which loads `pact_check.py` and its evidence reader once, so `World.run` and the cases that patch the module reach one module. `_template` commits through conftest's `commit`, the name `commit_everything_as_e` has there, and asks git through conftest's `git`, which checks the exit as `git_out` did. The move check reads none of the helpers, so they are named here. `tests/test_one_word_one_meaning.py#RENAMED_COMPAT` names `tests/conftest.py` and `tests/test_config.py` in place of the signer file, which no longer spells the 0.18.x header; the sweep refused both until it did.

**The move check** (`executed`):

`bin/test-layout --moved c6c1d8b0 --from tests/test_config.py tests/test_a_signer_declares_its_pact.py tests/test_pact_check.py --to tests/test_config.py tests/test_a_signer_declares_its_pact.py tests/test_pact_check.py`

`test-layout: moved: 134 old cases, 333 items against 333 at c6c1d8b03de3, 7 failed`, exit 1. Each line was read: 4 are the two `PACT_TEXT` bodies, each named twice, and 3 the merge, the two old cases and the case they became. No move needed repair. Groups 21 and 22 passed, and this group fails, so `hooks/config.py` runs its mutants here, once, over every case its file holds.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `hooks/config.py` with `--tests "bin/test tests/test_config.py -q -p no:xdist -x"`, at the tree committed as ca726662; the old column in an archive of fb0c5dfc, the base before group 21, against the nine files the three groups drew from, run with the worktree's `.venv` and `test_every_template_is_named_by_a_document_that_ships` deselected because an archive is no repository git lists). 87 mutants, c1 to c90, at the decision points of each public function: 75 red and 12 survived, in 86.8 s after a 2.0 s baseline; the old column ran the 12 in 482.8 s, 7 red and 5 survived. An id here names a row of this table alone, and the exact replacements are kept with the build's driver outside the tree.

| # | Mutation | New file | Old files |
|---|---|---|---|
| c1 to c5, c7 to c9 | `unescaped` undoes nothing; `fence_map` hides nothing or names no opener; `hidden_lines` names a sure opener or reads no text; `unfenced` reads no text; `config_table` reads every refused table as none, or numbers rows one on | red | not run |
| c6 | `hidden_lines` names the last opener left open, not the first | SURVIVED | SURVIVED |
| c11, c12 | `config_text` reads a directory as absent; lets an undecodable file raise | red | not run |
| c13 | `config_text` has no guard for an empty home | SURVIVED | SURVIVED |
| c14 | `unreadable_config` says `str(exc)` in place of the reason | SURVIVED | SURVIVED |
| c15 to c18, c20 to c23 | the doubled-row sentence; `config_value` reads a walker refusal as no row, counts nothing below the stop, or one row below as none; `rows_named_below` counts pieces after a break, passes the next heading, or counts any first cell; `value_of` takes two rows | red | not run |
| c25 to c28 | `declared_value` and `declared_mode` read an unreadable file as absent; `declared_mode` keeps the case, or calls any value a mode | red | not run |
| c29 to c39 | `inside_the_root` misses `seal` itself; `reference_roots` answers no root as the default, reads `None` as a prefix, keeps backslashes, keeps `seal/`, keeps a duplicate; `under_reference_root` keeps the root, reads `specs` at the top only, matches a prefix of a name; `policy_root` takes a path out of the repository, or keeps a trailing slash | red | not run |
| c40 to c54 | `normalise_remote` reads a port as an scp colon, keeps `user@`, keeps `.git`, keeps the case; `pact_name` names a path with no slash; `remote_entries` passes a space, two spellings of one repository, a name an anchor cannot carry, or an empty entry, and refuses two signers ending alike; `pact_declaration` drops the walker's sentence on either arm, or splits on commas; `declared_pacts` reads an unreadable file as no row, or no file as unreadable | red | not run |
| c55, c57, c62 to c65, c67 | `table_cells` reads a pipe after an even run of backslashes; `html_start` numbers the kinds from 2; `raw_html_open` forgets CDATA, or never closes a block; `a_list_above` resets on no heading, or sees no list item; `gfm_table` skips the list-item refusal | SURVIVED | red |
| c56, c58 to c61, c66, c68 to c79 | `table_cells` reads past the last pipe; `table_end` reads four columns, a thematic break, a list item or an HTML block as a row; `gfm_line_starts` starts every piece; `gfm_table` skips the line-above, open-block, delimiter-place, width and shared-line refusals, reads a gap as no end, reads past the next heading, refuses no stray row, takes a piece after a break, a stray delimiter or a row of another width, or says `stops at` for a line with no pipe | red | not run |
| c80 to c88 | `read_table` never reads the old header, keeps a glued old header as a row, names the old header twice, or drops the old table; `pact_signers` drops its `so it names no signer`, refuses a table GFM does not render as listing nobody, or keeps `row` for `signer`; `baseline_commit` takes two rows, or a SHA that only begins the span | red | not run |
| c89 | `baseline_commit` drops the walker's refusals from its `why` | SURVIVED | SURVIVED |
| c90 | `renamed_header` renames a header that holds no `Signer` | SURVIVED | SURVIVED |

The five old gaps: no case leaves two fences open, asks `config_text` for an empty home, reads the reason in an unreadable-config sentence, refuses a parity table the walker stops while its row is missing, or reads a table other than the pact's through `read_table`. c55, c57, c62 to c65 and c67 are red on the old files, and the cases that kill them did not move: `bin/test tests/test_one_table_walker_reads_what_gfm_renders.py -q -p no:xdist -x` in the working tree is red on all seven (`executed`, 14.4 s), the oracle cases `spec.md` *What the frame decided* keeps there. So the move lost none of them, and no case was added, as for group 14's g11 and g13.

**Phase 4's survivors** (`executed`). h6, `commit_everything_as_e` without its identity, run against `tests/test_config.py` with `-x`, since the world the moved pact cases copy is committed through it: SURVIVED, 233 passed. The suite's environment gives git an identity, so it stays an old gap. h2, h12 and h23 are not reached: no moved case calls `read`, `imported_roots` or `repo_relative` (`read`).

**Cases and seconds** (`executed`, serial, pytest's own figure): 335 items in 4.78 s before, the three files in an archive of c6c1d8b0 with the worktree's `.venv`; 335 items in 5.11 s after. 24 old cases became 23.

**The real-git cases kept.** The seven cases from the pact_check file run `check` over a copy of the world, whose two repositories git holds: the pact's history and the signer's origin are git's answers.

**The boundary** (`executed`). At the tree committed as ca726662, before the commit: the three files, `tests/test_one_word_one_meaning.py`, the oracle file, every test file requesting a fixture named `world`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`: 3,316 passed and 3 skipped in 40.2 s. `bin/test-layout --check` exits 0, 167 files read, 124 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff checks and formats each changed file clean.

**Where the seventh spawn stopped.** At the boundary after group 23. `hooks/cmdline.py`'s group moves about 150 cases out of seven files and then runs the mutants of a 3,097-line module, which needs that module read whole to place them; it could not close with a complete record in what was left of this spawn, and `hooks/cmdline_base.py` and the seven directories come after it.

### What `hooks/` holds back

**The installer waits on Q10** (`read`). `hooks/githooks.py` and `hooks/hook-install.py` have their cases in `tests/test_the_hooks_are_installed_where_git_runs_them.py`, which `docs/the-commit-gate-inside-git.md` names on the `check:` line of a section whose heading is also the document's title. `questions.md` Q10's default is wait, so the two keep their cases there through this work.

**Files a group may drain but not remove** (`executed`, `git grep` over the `check:` lines of `docs/`, `CONTRIBUTING.md`, `skills/` and `agents/`). Of the undeclared files that hold `hooks/` cases, these are named by a `check:` line: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_hooks_are_installed_where_git_runs_them.py`, `tests/test_routing_is_recorded.py`, `tests/test_optin_home.py`, `tests/test_a_gate_that_fails_says_so.py`, `tests/test_worktree_guard_signals.py`, `tests/test_guard_resolves_the_tree_it_judges.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_the_mode_question_is_asked_once.py`, `tests/test_gate_judges_the_repo_it_commits_to.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_an_automation_run_meets_no_commit_prompt.py`, `tests/test_the_waiver_can_be_typed.py`, `tests/test_a_commit_behind_a_reserved_word_is_judged.py`, `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`, and `tests/test_a_creation_is_judged_before_git_runs.py`, which group 7 emptied. Each line has its `## Rule changes` item in `spec.md` since 0b134a29 except the installer's; group 17 emptied the automation file and the waiver file, which keep a docstring.

**Where `hooks/` stands at 6277911e** (`read`). Groups 16 and 17 placed the commit gate's cases the five lines held, with `hooks/commitgate.py`'s and `hooks/worktree_consent.py`'s that shared their files; groups 18 and 19 placed `hooks/gate.py`'s and `hooks/tokens.py`'s own cases, one each; group 20 emptied the local-mode file. Three shared readers remain, `hooks/config.py`, `hooks/cmdline.py` and `hooks/cmdline_base.py`, and every line their groups meet has a verdict in `spec.md`.

### What remains in phase 6

- `hooks/`: the two shared readers left, one group each; `hooks/config.py` closed in groups 21 to 23. `hooks/cmdline.py`'s group takes the walk left in `tests/test_gate_judges_the_repo_it_commits_to.py` (28 cases), the reading rows of the reserved-word, wrapper, no-shape and heredoc-data files and of `tests/test_what_the_reader_understands.py`, and the gate cases of `tests/test_a_path_the_command_wrote_out.py` that pin the reading, about 3,900 lines of cases; its cases move as they stand under Q1. Read for it (`read`, the seventh spawn): `hooks/cmdline.py` imports nothing of `hooks/cmdline_base.py`, so a case loading `cmdline.py` is that module's; the reader constant `TARGET = "/target"` of `tests/test_what_the_reader_understands.py` is read in 24 places of its case bodies, so renaming it fails the move check and sends `hooks/cmdline.py` to its mutants whatever else holds; the three heredoc-data cases carry `@pytest.mark.rule` markers, and `tests/test_commit_review_gate.py` imports `SHAPES` and `HERE` from the reserved-word file. `hooks/githooks.py` and `hooks/hook-install.py` wait on Q10. `hooks/answer-clear.py` has a file whose `Test_module` holds its two round trips and no `Test_main`.
- `skills/implement/scripts/seal.py`'s light files now include the ten writer cases and the re-export case left in `tests/test_the_mode_question_is_asked_once.py`, and the re-export case left in `tests/test_a_signer_declares_its_pact.py` (groups 22 and 23).
- The other seven shipped directories of `plan.md`'s phase 6 row: `hooks/git/`, `skills/verify/scripts/`, `skills/code-review/scripts/`, `skills/settle/scripts/`, `skills/implement/scripts/`, `.github/scripts/`, `evals/scripts/`, with the light files phase 5 left for its other modules, and the lines outside `docs/` their groups rewrite. `tests/test_arm_check.py`'s docstring names `tests/test_chain_hooks.py#reader_blanking_passes`, gone since 8350c578, and the group that places `skills/verify/scripts/arm_check.py`'s cases corrects it.
- Phase 4's survivors: h14 was re-run against the creation flow in group 7, h21 against the guard's file in group 12, h4 against the commit gate's file in group 14 and h6 against `tests/test_config.py` in group 23, and each survives, an old gap. h2, h12 and h23 wait for the groups that rebuild the modules whose cases reach them; no group through 23 reaches one (`unverified`, for the spawn that places those modules).
