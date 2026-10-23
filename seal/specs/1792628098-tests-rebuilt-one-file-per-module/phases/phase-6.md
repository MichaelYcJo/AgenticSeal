# Phase 6: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 52ce0e03; its first step is 6e7214be, extended to the two sets at 43324e4e |

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

### The eighth spawn

**What this spawn was asked.** `hooks/cmdline.py`'s cases from seven files, its text-reading cases moving as they stand into `tests/test_cmdline.py` under Q1, `tests/test_what_the_reader_understands.py`'s constant `TARGET = "/target"` renamed where its cases land in a file declaring `TARGET`, and what `tests/test_commit_review_gate.py` imports from the reserved-word file moved with the cases, split into several groups along public functions where one would not close; then `hooks/cmdline_base.py`; then the seven directories outside `hooks/` in `plan.md`'s order, rule 3 where an old file prices at 60 s or more, each group rewriting the lines outside `docs/` that `spec.md` *The check lines the remaining groups meet* assigns it, and the group placing `skills/verify/scripts/arm_check.py`'s cases correcting `tests/test_arm_check.py`'s docstring. A line with no verdict is recorded and left; an item that names too little or too much once a group moves is a row of `overview.md` for the framer. Phase 4's h2, h12 and h23 are re-run where a group rebuilds a module whose cases reach one.

**Whether the frame holds** (`read`). It holds for `hooks/cmdline.py`. The three `check:` lines naming its files, `docs/commit-review-gate-spec.md` lines 125, 139 and 145, each have an item moving them to `tests/test_commit_review_gate.py tests/test_cmdline.py` (`spec.md` lines 215, 358 and 363); `docs/the-commit-gate-inside-git.md` line 183 names neither the frozen reading file nor the hook surface file for a case this group moves. The five files those three lines name stay with a docstring and no case. No line names `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py` or `tests/test_a_path_the_command_wrote_out.py`, so each goes with its last case.

**How `hooks/cmdline.py` is split** (`read`). Renaming the reader file's `TARGET` changes 24 case bodies, so the group that moves those cases fails the move check and the module runs its mutants there whatever else holds. The groups go from the cases that move unchanged to the ones that do not, so the mutants run once, last, over every case the module's file holds: group 24, the heredoc-data file; group 25, the walk file, the reserved-word file, the wrapper file and the no-shape file, each moved with its body; group 26, the reader file and the path file, whose names collide with group 25's (`unreadable`, `BODIES`, a case name) as well as with `TARGET`.

### Batch B, `hooks/`, group 24, at 93bf39da

**The cases.** From `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py`, its three:

- S4, `test_a_string_that_fails_one_clause_still_stops`, and S5, `test_what_760_found_still_stops`, into `tests/test_cmdline.py`'s `Test_module` under their names. Each reads a command through the commit gate's `commit_invocations`, which hands it to `hooks/cmdline.py`; neither calls a function of the reader by name. `hidden_commit`, `NO_BODY` and the S5 lists came with them.
- S6, `test_s6_neither_read_honours_a_token_the_base_did_not`, into `tests/test_tokens.py`'s `Test_module`: it holds `has_marker` and `tokens.given` to the base's two reads, and since #868 `has_marker` is `tokens.given`. Its builders and `every_case` came with it, and `tests/test_the_old_spellings_reach_the_hook.py#_corpora` imports `every_case` from there.

No `check:` line names the old file, so it went.

**The move check** (`executed`): `bin/test-layout --moved 687388b5 --from tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py tests/test_tokens.py --to tests/test_cmdline.py tests/test_tokens.py` ends `test-layout: moved: 4 old cases, 215 items against 215 at 687388b5ae85, 0 failed`, exit 0. No mutation table. `--pairs` names S4 and S5, whose bodies are equal once names and strings are normalised; under Q1 the module's cases move as they stand and none is merged.

**The lines rewritten.** `tests/test_one_heredoc.py`'s docstring names `tests/test_cmdline.py` for the gate's half of S4, and `tests/test_commit_review_gate.py`'s names it for how the reader reads each shape.

**Cases and seconds** (`executed`, serial, pytest's own figure): 216 items in 0.60 s before, the two files at 687388b5; 217 items in 1.32 s after, the census item of `tests/test_cmdline.py` among them.

**The boundary** (`executed`). At the tree committed as 93bf39da, before the commit with the new file staged: the five changed files, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 27 files: 2,357 passed and 3 skipped. After the commit, the same set less the changed files plus the new file: 2,194 passed and 3 skipped. `bin/test-layout --check` exits 0, 167 files read, 123 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `hooks/`, group 25, at eb207a6d

**The cases.** 63 cases into `tests/test_cmdline.py`, each with its body:

- From `tests/test_gate_judges_the_repo_it_commits_to.py`, its 28: the 23 read through `commit_dirs` into `Test_walk_directories`, `test_a_cd_carries_the_commit_that_follows_it` renamed `test_accepts_a_cd_as_carrying_the_commit_that_follows_it` and `test_a_destination_the_reader_cannot_expand_is_not_a_directory` renamed `test_refuses_a_destination_the_reader_cannot_expand_as_a_directory`; the three of the splitter into `Test_split_segments_with_separators`, two renamed `test_accepts_the_operator_that_joined_two_segments` and `test_refuses_the_newline_after_an_operator_as_the_one_that_binds`; `parse_git`'s one into `Test_parse_git`, renamed `test_refuses_a_subshell_with_no_subcommand_as_a_git_invocation`; and `split_segments`' one, which has no refusing partner, into `Test_module`.
- From `tests/test_a_commit_behind_a_reserved_word_is_judged.py`, its 6: `test_the_guard_reads_the_same_command_word` into `Test_parse_git`, renamed `test_accepts_the_command_word_behind_a_list_opener`, and the five read through the commit gate's `commit_invocations` into `Test_module`.
- From `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`, its 27: `header_end`'s two into `Test_header_end`, renamed `test_accepts_each_header_spelling_at_the_word_its_command_starts` and `test_refuses_a_header_spelling_it_cannot_place_as_unplaceable`; `merged_view`'s two into `Test_merged_view`, renamed `test_accepts_the_cut_operators_glued_back` and `test_refuses_to_glue_across_a_real_separator`; `names_an_unknown_command`'s one into `Test_names_an_unknown_command`, renamed `test_accepts_an_unknown_command_word_as_named_and_no_structural_one`; `parse_git`'s two into `Test_parse_git`; and the 20 read through `commit_invocations`, or one case of a function with no refusing partner (`substitution_bodies`, `reparsed_texts`, `_env_long`), or a module constant (`RUNNERS`, `ENV_OPTIONS`), into `Test_module`.
- From `tests/test_no_shape_the_base_stops_reads_silent.py`, its 2: the header bound into `Test_names_an_unknown_command`, renamed `test_refuses_to_read_past_the_header_bound`, and the cut `cd` into `Test_walk_directories`.

`SHAPES` and `HERE` moved with the reserved-word cases, and `tests/test_commit_review_gate.py` imports them from the new file. The four old files are named by `check:` lines of `docs/commit-review-gate-spec.md` whose items are not yet settled, so each keeps a docstring naming where its cases went, and no case.

**The move check** (`executed`):

`bin/test-layout --moved 3cf11823 --from tests/test_cmdline.py tests/test_gate_judges_the_repo_it_commits_to.py tests/test_a_commit_behind_a_reserved_word_is_judged.py tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py tests/test_no_shape_the_base_stops_reads_silent.py --to tests/test_cmdline.py`

`test-layout: moved: 65 old cases, 661 items against 661 at 3cf118239946, 0 failed`, exit 0. No mutation table here: the module runs its mutants in group 26, over every case its file holds. `--pairs` names three pairs in `Test_module`, each two cases whose bodies are equal once names and strings are normalised and whose tables differ: S4 and S5; the reserved-word file's `eval` rows and the wrapper file's rows both SHAs read as nothing; the reserved-word file's `SHAPES` and the wrapper file's `WRAPPED`. Under Q1 none is merged.

**The lines rewritten.** `tests/test_commit_review_gate.py`'s docstring names `tests/test_cmdline.py` as the home of every reading case and of `SHAPES`.

**Cases and seconds** (`executed`, serial, pytest's own figure): 662 items in 1.03 s before, the five files in an archive of 3cf11823 with the worktree's `.venv`; 662 items in 0.98 to 1.05 s after, and 3.71 to 4.16 s on the first run after an edit.

**The real-git cases kept.** None: every case reads text.

**The boundary** (`executed`). At the tree committed as eb207a6d, before the commit with the new file staged: the six changed files, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 27 files: 2,267 passed and 3 skipped. `bin/test-layout --check` exits 0, 167 files read, 123 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `hooks/`, group 26, at da3eae09

**The cases.** Into `tests/test_cmdline.py`, each with its body unless named below:

- From `tests/test_what_the_reader_understands.py`, 41 of its 42: the constructs, the ordinary commands, the alias and the prefixes into `Test_understood`, with `test_the_understood_check_can_fail` renamed `test_accepts_a_plain_command_and_not_a_construct`; the comment model's nine into `Test_drop_comments`, two renamed `test_accepts_a_paren_inside_an_expansion_as_a_word_part` and `test_refuses_a_bare_brace_as_an_expansion_opener`; the heredoc and arithmetic model's fourteen into `Test_drop_heredoc_bodies`, renamed where a pair was needed: `test_accepts_a_heredoc_body_as_dropped`, `test_refuses_arithmetic_as_a_heredoc`, `test_refuses_a_heredoc_opener_inside_an_expansion` and `test_accepts_a_heredoc_opened_after_an_unbalanced_expansion`; the rest of the walk into `Test_walk_directories`, `test_the_common_cross_repository_form_gains_nothing` renamed `test_the_common_cross_repository_form_gains_no_candidate` beside the walk file's case of that name. Its S13, `test_the_guard_reads_the_same_answer`, reads the guard's `walk_command` and joins `tests/test_worktree_guard.py`'s `Test_walk_command` under its name.
- From `tests/test_a_path_the_command_wrote_out.py`, its 49: the 34 read through `commits` or `targets` into `Test_walk_directories`; `_bind`'s four into `Test__bind`, two renamed `test_refuses_a_subshell_of_its_own_accord` and `test_accepts_only_a_bare_name_operand_as_forgotten`; `_substitute`'s two into `Test__substitute`, renamed `test_accepts_a_bound_name_and_leaves_every_other_standing` and `test_refuses_to_rescan_a_value_holding_a_dollar`; the prefix case into `Test_understood`, renamed `test_refuses_a_reserved_word_behind_a_prefix_as_a_simple_command`; and the six that run the commit gate over repositories git made, with `_runs`' and `_nesting`'s one case each, into `Test_module`.

The reader file is named by `docs/commit-review-gate-spec.md` line 125, whose item is not yet settled, so it keeps a docstring and no case; no line names the path file, so it went. The path file's own `sh` returned what conftest's returns, so the moved cases call conftest's; its unused gate load did not come along.

**Thirteen bodies changed, on purpose** (`read`). One module holds one definition of a name, and four collided. The reader file's `TARGET = "/target"` is `TARGET_DIR` beside the declared `TARGET`, which changes eight of its bodies, and S13 writes `/target` and `/session` out in the guard's file, which holds neither constant. The walk file's `unreadable`, which answers booleans, is `unreadable_flags`, so the reader file's, which answers the unresolved directories, keeps its name; that changes three bodies moved in group 25. The path file's `BODIES` list is `UNRUN_BODIES` beside the wrapper file's `BODIES` table, one body.

**The move check** (`executed`):

`bin/test-layout --moved 0e561e86 --from tests/test_cmdline.py tests/test_what_the_reader_understands.py tests/test_a_path_the_command_wrote_out.py tests/test_worktree_guard.py --to tests/test_cmdline.py tests/test_worktree_guard.py`

`test-layout: moved: 367 old cases, 1189 items against 1189 at 0e561e86de7a, 26 failed`, exit 1. Each line was read: the 26 are the thirteen bodies above, each named twice, as the old case and as the new case that stands for no old case. No move needed repair. So `hooks/cmdline.py` runs its mutants here, once, over every case its file holds, and `hooks/worktree-guard.py` runs its own. `--pairs` names 61 pairs: group 25's three in `Test_module`; 55 among the eleven one-line `commits(...) == [...]` cases of the path file, whose bodies differ by the command and the answer alone; and three more in `Test_walk_directories` and `Test_drop_heredoc_bodies`, each two cases whose commands differ. Under Q1 none is merged.

**The mutation table of `hooks/cmdline.py`** (`executed`, one `bin/mutation-check` batch with `--tests "bin/test tests/test_cmdline.py -q -p no:xdist -x"`, at the tree committed as da3eae09; the old column in an archive of 687388b5, the base before group 24, against the seven old files, run with the worktree's `.venv`). 120 mutants, m1 to m122 less m18 and m96, at the decision points of each public function and of the private ones a class names or the walk turns on: 103 red and 17 survived, in 306.2 s after a 6.7 s baseline; the old column ran the 17 in 65.1 s, and all 17 survived. An id here names a row of this table alone, and the exact replacements are kept with the build's driver outside the tree.

| # | Mutation | New file | Old files |
|---|---|---|---|
| m1, m2 | `redirection_width` takes no spaced target; reads no `>(` target | red | not run |
| m3, m4 | `unglued` cuts a descriptor; cuts a quoted word | red | not run |
| m5 to m9 | `drop_comments` opens a comment inside `${…}`, reads a paren there as a command's, reads an unbalanced `)` as a word part, drops extglob from the word parts, counts a bare `{` | red | not run |
| m10 | `_closes` counts an unbalanced `${` | red | not run |
| m11 | `drop_heredoc_bodies` opens a comment inside `${…}` | SURVIVED | SURVIVED |
| m12 to m16 | `drop_heredoc_bodies` reads `((` inside `${…}` as arithmetic, `$[` as text, a quoted paren in arithmetic as a paren, a herestring as a heredoc, a `<<` inside `${…}` as an opener | red | not run |
| m17 | `drop_heredoc_bodies` ends a `<<-` body only at an untabbed delimiter | SURVIVED | SURVIVED |
| m19 | `heredoc_bodies` answers none | red | not run |
| m20 | `split_segments` answers clean for a split that failed | SURVIVED | SURVIVED |
| m21 to m23 | `split_segments_with_separators` keeps a line continuation, glues a newline to an operator, lets the newline bind | red | not run |
| m24 | `split_segments_with_separators` answers clean for a split that failed | SURVIVED | SURVIVED |
| m25, m26 | `merged_view` glues a redirection that carries its target; glues `&` before `>` after any separator | SURVIVED | SURVIVED |
| m27, m28 | `merged_view` glues across `&&`; `merged_segments` answers none | red | not run |
| m29 to m33 | `command_word` reads no runner, places a list opener's command, reads no zsh short loop, reads no runner's operand, places the stand-in | red | not run |
| m34 | `host_word` keeps a glued `(` | red | not run |
| m35 to m41 | `header_end` steps past a glued body, a spaced pattern's `)`, a `case` with no `in`, a coprocess's name, `function f()` and `f(){`, and places a pattern with no `)` | red | not run |
| m42 to m45 | `reparsed_texts` drops `--command=`, `parallel`, BSD's walk; `_hands_a_string` reads `-c` alone | red | not run |
| m46 | `_env_walk` reads `--` as one of env's options | red | not run |
| m47 | `_env_walk` reads no value after a cluster ending in `S` | SURVIVED | SURVIVED |
| m48, m49 | `_env_option` reads no required value; `_env_long` takes an ambiguous prefix | red | not run |
| m50 to m52 | `command_strings` reads no valued option, reads `watch` anywhere, asks no other host | red | not run |
| m53 to m59 | `names_an_unknown_command` asks no glued view and no cut word, counts a redirection behind a runner, reads past the header bound as silent; `_is_the_program` reads one header more, or an unplaceable header as no program; `_expands` reads `[` as a glob | red | not run |
| m60 to m64 | `substitution_bodies` reads a single-quoted `$(`, steps over no escaped backtick, reads a quoted `<(`; `_paren_end` counts a `case`'s `)`, reads a herestring as a heredoc | red | not run |
| m65 | `understood` asks nothing past leading redirections | red | not run |
| m66 | `understood` accepts a segment a subshell or brace opened | SURVIVED | SURVIVED |
| m67 | `understood` refuses a conditional `[[` | red | not run |
| m68 | `understood` accepts a spaced `f ()` definition | SURVIVED | SURVIVED |
| m69 to m76 | `understood` reads no prefix's option, accepts a reserved word or a `cd` behind a prefix, reads `[` as a glob, accepts an expanding word; `_past_leading_redirections` reads no zsh modifier; `Unresolved` defaults to `CONSTRUCT`; `strip_subshell` reports no glued `(` | red | not run |
| m77, m78 | `_cd_target` reads a two-operand `cd` as a path; reads `~user` as a path | SURVIVED | SURVIVED |
| m79, m80 | `_branches` runs neither branch of `;`, or of `\|\|` | red | not run |
| m81 | `compose` recovers an unreadable base under a relative `-C` | SURVIVED | SURVIVED |
| m82 to m85, m121, m122 | `_land` launders `cd -` and names no previous directory as a value; `_capped` never caps, and caps to a value; `_directories` keys by text alone; `_step` recovers an unreadable shell | red | not run |
| m86 to m90 | the walk unplaces by the first reading alone, lands a glued `cd` twice, lands no `cd` past a redirection, takes no glued refusal, parks no failure before `;` | red | not run |
| m91 | the walk keeps the parent shell for a pipe only after the segment | SURVIVED | SURVIVED |
| m92 to m95, m97 to m110 | the walk empties nothing at a defined call, binds a conditional branch, binds inside a body, empties every refused segment; `_bind`, `_forget`, `_unseen`, `_substitute`, `_nesting`, `_runs` and `_expanded` each lose one decision | red | not run |
| m111 to m116 | `_git_options` keeps no `-C`, takes `--shallow-file`'s value as the subcommand; `parse_git` reads no redirection before the subcommand, keeps a glued `)`, answers an empty subcommand, reads no redirection before `git` | red | not run |
| m117, m118 | `adds_a_worktree` takes any positional; takes any subcommand | SURVIVED | SURVIVED |
| m119, m120 | `apply_chdir` expands no `~`; does not normalise | SURVIVED | SURVIVED |

The seventeen survivors are old gaps: no moved case reads a `${…}` holding a `#` through the heredoc model alone, a `<<-` body whose delimiter is tabbed, a split that fails, a cut redirection that already carries its target, a value behind a cluster ending in `S`, a segment opened by `(` or `{` that the walk's own guards do not already refuse, a spaced `f ()`, a two-operand or `~user` `cd`, a relative `-C` from an unreadable base, a `cd` on the left of a pipe that ends the command, `adds_a_worktree`, or `apply_chdir`'s `~` and normalisation. The worktree guard and the consent writer ask `adds_a_worktree` and `apply_chdir` through `hooks/cmdline_base.py`'s copies, which their files pin. No case was added.

**The mutation table of `hooks/worktree-guard.py`** (`executed`, group 12's driver unchanged, w1 to w70, each landing once in the file as committed, `--tests "bin/test tests/test_worktree_guard.py -q -p no:xdist -x"`): 70 mutants, 70 red, in 159.4 s after a 14.7 s baseline, so the old column did not run.

**The lines rewritten.** `hooks/cmdline.py`'s comment on `_closes` names `tests/test_cmdline.py` as the file pinning `echo ${x <<EOF`; `hooks/cmdline_base.py` carries the same sentence and stays as it is, because `tests/test_the_frozen_reading_never_grows.py` pins its bytes below the rider to `86256492`. `tests/test_worktree_guard.py`'s docstring names the reader file's S13 among the cases phase 6 moved there.

**Left where they stand.** `tests/test_the_reader_agrees_with_bash.py` holds `hooks/cmdline.py`'s name environment against bash over a generated corpus, a check against an oracle that `spec.md` *What the frame decided* keeps where it is, as group 21 kept the cases that ask cmark-gfm; its second case reads that corpus.

**Cases and seconds** (`executed`, serial, pytest's own figure): over the module, 839 items in 3.48 to 4.12 s before, the seven old files in the archive of 687388b5; 838 items in 3.48 s after in `tests/test_cmdline.py`, S6 and S13 gone to `tests/test_tokens.py` and `tests/test_worktree_guard.py` and the census item come in. Over this group's four files, 1,188 passed and 3 skipped in 17.65 s before, in an archive of 0e561e86, and in 17.60 s after.

**The real-shell and real-git cases kept.** `Test_understood::test_a_real_shell_really_lands_in_the_target` runs each construct row through bash, the row showing where the shell really lands; the six gate cases of `Test_module` run the commit gate as the harness runs it over repositories git made, each showing the gate's verdict follows the reading.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: no moved case calls `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as da3eae09, before the commit: the three changed test files, every test file that loads `hooks/cmdline.py` (the rider, CI, commit gate, dispatcher, edit tool, one heredoc, frozen reading and bash oracle files), `tests/test_the_old_spellings_reach_the_hook.py`, `tests/test_tokens.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 33 files: 2,702 passed and 3 skipped. `bin/test-layout --check` exits 0, 166 files read, 122 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean, `hooks/cmdline.py` among them.

### `hooks/cmdline_base.py`, the last shared reader: nothing to move

**What reaches it** (`executed`, `git grep -n cmdline_base tests/`; the cases `read`). No case calls one of its functions as its subject from an undeclared file. `tests/test_the_frozen_reading_never_grows.py` compares its bytes with `86256492:hooks/cmdline.py` and scans the hooks for who imports it, checks across files that `spec.md` *What the frame decided* keeps where they are, and its S10 and S11 run the guard beside the installer, which waits on Q10. `tests/test_dispatch.py` breaks a copy of it to show the dispatcher's guard, and is the dispatcher's. The guard's file holds the cases of the `parse_git` and `apply_chdir` the guard imports from it, in `Test_module` since group 12, as the guard's re-exports, the reading group 22 gave `seal.py`'s re-export of the config reader. So no case moves, no file is written, the module's census stays with the sweep in `tests/test_censuses.py`, and nothing is committed beyond this record.

### `hooks/git/`: nothing to move

**What reaches it** (`executed`, `git grep` over `tests/` for each stub's file name; the cases `read`). The three stubs, `pre-commit.py`, `post-commit.py` and `reference-transaction.py`, are run by git in `tests/e2e/commit/test_commit_flow.py`, the commit flow, and in `tests/test_the_hooks_are_installed_where_git_runs_them.py`, the installer's file, which waits on Q10. What they judge is `hooks/commitgate.py`'s, in `tests/test_commitgate.py`. No other file holds a case of theirs, so the directory has no group and nothing is committed beyond this record.

**Where the eighth spawn stopped.** At the boundary after group 26 and the two directories with nothing to move. `skills/verify/scripts/` draws its cases from about forty undeclared files, each to be read case by case before a group can be chosen, and its first group could not close with a complete record in what was left of this spawn.

### What `hooks/` holds back

**The installer waits on Q10** (`read`). `hooks/githooks.py` and `hooks/hook-install.py` have their cases in `tests/test_the_hooks_are_installed_where_git_runs_them.py`, which `docs/the-commit-gate-inside-git.md` names on the `check:` line of a section whose heading is also the document's title. `questions.md` Q10's default is wait, so the two keep their cases there through this work.

**Files a group may drain but not remove** (`executed`, `git grep` over the `check:` lines of `docs/`, `CONTRIBUTING.md`, `skills/` and `agents/`). Of the undeclared files that hold `hooks/` cases, these are named by a `check:` line: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_hooks_are_installed_where_git_runs_them.py`, `tests/test_routing_is_recorded.py`, `tests/test_optin_home.py`, `tests/test_a_gate_that_fails_says_so.py`, `tests/test_worktree_guard_signals.py`, `tests/test_guard_resolves_the_tree_it_judges.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_the_mode_question_is_asked_once.py`, `tests/test_gate_judges_the_repo_it_commits_to.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_an_automation_run_meets_no_commit_prompt.py`, `tests/test_the_waiver_can_be_typed.py`, `tests/test_a_commit_behind_a_reserved_word_is_judged.py`, `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`, `tests/test_what_the_reader_understands.py`, `tests/test_no_shape_the_base_stops_reads_silent.py`, and `tests/test_a_creation_is_judged_before_git_runs.py`, which group 7 emptied. Each line has its `## Rule changes` item in `spec.md` since 0b134a29 except the installer's; group 17 emptied the automation file and the waiver file, and groups 25 and 26 the five files of `hooks/cmdline.py` among these, each keeping a docstring.

**Where `hooks/` stands at da3eae09** (`read`). Groups 16 and 17 placed the commit gate's cases the five lines held, with `hooks/commitgate.py`'s and `hooks/worktree_consent.py`'s that shared their files; groups 18 and 19 placed `hooks/gate.py`'s and `hooks/tokens.py`'s own cases, one each; group 20 emptied the local-mode file; groups 21 to 23 placed `hooks/config.py`, and groups 24 to 26 `hooks/cmdline.py`. `hooks/cmdline_base.py` has no case of its own to place. Only the installer's two modules remain, waiting on Q10.

### The ninth spawn

**What this spawn was asked.** The six directories outside `hooks/` in `plan.md`'s order, `skills/verify/scripts/` first, module by module, grouping the modules whose old files meet; rule 3 where an old file prices at 60 s or more; each group rewriting the lines outside `docs/` that `spec.md` *The check lines the remaining groups meet* assigns it, `agents/smith.md` lines 109 and 123 with `mutation_check.py`'s cases; the group placing `arm_check.py`'s cases correcting `tests/test_arm_check.py`'s docstring; the group placing `seal.py`'s writer cases settling `overview.md`'s row on `docs/one-root-by-lifetime.md` line 223; phase 4's h2, h12 and h23 re-run where a group rebuilds a module whose cases reach one; a case reading a workflow or a document left where it is. A line with no verdict is recorded and left; an item that names too little or too much is a row of `overview.md` for the framer.

**Whether the frame holds** (`read`). It holds for `skills/verify/scripts/`. `agents/smith.md` lines 109 and 123 name `tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` at 300abe34, as `spec.md` lines 105 and 106 say they did at 44525de4, and `tests/test_session_cost.py` and `tests/test_arm_check.py` keep the lines `spec.md` names for them.

### Batch B, `skills/verify/scripts/`, group 27, at ffb0bd4b

**The module.** `skills/verify/scripts/deferral_check.py`, whose eleven cases were the whole of `tests/test_deferral_check.py`, which keeps its name and now declares `TARGET`. Every case runs the command, so ten sit in `Test_main` and the launcher's case in `Test_module`. Two are renamed to the pair: `test_accepts_pytest_on_a_pull_request_as_the_answerer` and `test_refuses_a_tree_with_no_ci_as_an_answerer`. No `check:` line names the file. `tests/test_a_reference_root_is_read_and_never_taken.py` names the command in its table of every shipped command, a check across commands, and stays.

**The move check** (`executed`): `bin/test-layout --moved 300abe34 --from tests/test_deferral_check.py --to tests/test_deferral_check.py` ends `test-layout: moved: 11 old cases, 11 items against 11 at 300abe340a60, 0 failed`, exit 0. No mutation table. `--pairs` names none.

**Cases and seconds** (`executed`, serial, pytest's own figure): 11 in 0.32 s before, in an archive of 300abe34; 12 items in 1.13 s after, the census item among them.

**The real-git cases kept.** None: no case runs git.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: no case calls `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as ffb0bd4b: the changed file, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 23 files: 2,456 passed and 3 skipped. `bin/test-layout --check` exits 0, 166 files read, 121 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats the file clean.

### Batch B, `skills/verify/scripts/`, group 28, at b16613b3

**The cases.** `skills/verify/scripts/mutation_check.py`'s single-pair cases, the 28 of `tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` that run the command, into `tests/test_mutation_check.py` with their bodies and names: the 25 that call `main` in-process into `Test_main`, beside phase 5's batch cases; the launcher's case, `_end`'s case and the platform's choice of bound, which have no partner in a class of their own, into `Test_module`. The stand-ins and the process helpers they use came with them. The new file's `module` loads the command through conftest's `load_module`; the old one's, which registers it in `sys.modules`, stays with the case that uses it, so the two are not a twin.

**The lines rewritten.** `agents/smith.md` lines 109 and 123 name `tests/test_mutation_check.py` beside the old file, as `spec.md` assigns them. The old file's docstring names where its cases went, and the new file's docstring says what it took.

**Left where they stand.** For #923, in the old file under their names: `test_the_smiths_definition_names_the_command_and_no_directory_to_clear`, `test_the_boundaries_bullet_says_the_command_holds_the_copy`, `test_the_verify_skill_says_what_each_verdict_means_and_what_the_bound_ends` and `test_the_default_bound_is_the_one_both_documents_state`, each reading `agents/smith.md` or the verify skill. They hold the rules of the two lines, so the old file stays on both.

**The move check** (`executed`): `bin/test-layout --moved 6b884f5f --from tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/test_mutation_check.py --to tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py tests/test_mutation_check.py` ends `test-layout: moved: 40 old cases, 54 items against 54 at 6b884f5f9f41, 0 failed`, exit 0. No mutation table. `--pairs` names none.

**Cases and seconds** (`executed`, serial, pytest's own figure): 55 items in 11.42 s before over the two files, in an archive of 6b884f5f; 55 in 10.91 s after.

**The real-git cases kept.** None: no case runs git. The cases that run real processes, the bound's and the interrupt's, stay as they were, because the bound is what they hold.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: no moved case calls `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as b16613b3: the two changed test files, `tests/test_arm_check.py`, every test file reading `agents/smith.md`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 44 files: 3,226 passed and 5 skipped. `bin/test-layout --check` exits 0, 166 files read, 121 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed test file clean.

### Batch B, `skills/verify/scripts/`, group 29, at 31aed13b

**The cases.** `skills/verify/scripts/coordinates.py`'s, 28 of the 29 of `tests/test_a_unit_is_bounded_where_a_parser_decides.py`, into the new `tests/test_coordinates.py` with their bodies: the 20 read through `resolve_unit` into `Test_resolve_unit`, `test_a_symbol_anchor_resolves_through_ast` renamed `test_accepts_a_symbol_anchor_through_ast` and `test_a_python_file_that_will_not_parse_is_refused_naming_the_interpreter` renamed `test_refuses_a_python_file_that_will_not_parse_naming_the_interpreter`; the two of the hash into `Test_content_hash`, renamed `test_accepts_trailing_whitespace_and_blank_lines_as_no_change` and `test_refuses_to_ignore_indentation`; the four of the parse into `Test_py_spans`, two renamed `test_refuses_a_file_that_will_not_parse_with_no_symbols` and `test_accepts_a_file_edited_between_two_reads_with_its_new_spans`; `text_regions`' one and the pact anchor's pattern into `Test_module`. The helpers and tables came with them.

**Left where they stand.** For #923, in the old file under its name: `test_a_quoted_line_resolves_in_any_file`, whose assertion reads `.github/workflows/test.yml`; it imports `places`, `ec` and `RUBY` from the new file, so no helper is defined twice. `docs/the-pact.md` line 85 names the old file, and `spec.md`'s item for *The pact anchor* moves it to `tests/test_coordinates.py`, so the file stays until the settle. `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` and `tests/test_every_reader_ends_a_line_where_gfm_does.py` load the module to compare its readers with others', checks across files that stay.

**The move check** (`executed`): `bin/test-layout --moved 7cd34d46 --from tests/test_a_unit_is_bounded_where_a_parser_decides.py --to tests/test_a_unit_is_bounded_where_a_parser_decides.py tests/test_coordinates.py` ends `test-layout: moved: 29 old cases, 50 items against 50 at 7cd34d46115a, 0 failed`, exit 0. No mutation table. `--pairs` names none.

**Cases and seconds** (`executed`, serial, pytest's own figure): 50 items in 0.08 s before, in an archive of 7cd34d46; 51 in 0.10 s after over the two files, the census item among them.

**The real-git cases kept.** None: no case runs git.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: no moved case calls `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as 31aed13b, before the commit with the new file staged: the two changed files, `tests/test_pact_check.py`, `tests/test_chain_check.py` and the two files comparing readers, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 28 files: 2,833 passed and 3 skipped. `bin/test-layout --check` exits 0, 167 files read, 121 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `skills/verify/scripts/`, group 30, at 666cedbb

**The cases.** `skills/verify/scripts/payload_meter.py`'s, the 24 of `tests/test_the_payload_meter_says_what_it_measured.py`, into the new `tests/test_payload_meter.py` with their bodies: the 18 read through `measure` into `Test_measure`, `test_the_composition_table_counts_bytes_and_chars_per_file_and_in_total` renamed `test_accepts_a_tree_with_bytes_and_chars_per_file_and_in_total` and `test_a_transcript_that_never_spawned_the_baseline_agent_refuses` renamed `test_refuses_a_transcript_that_never_spawned_the_baseline_agent`; the two of `sections_of` into `Test_sections_of`, renamed `test_refuses_a_heading_inside_a_fence_as_a_section` and `test_accepts_a_heading_after_a_line_the_shared_rule_does_not_fence`; `heading_starts`' one, the two that run the command and the launcher's into `Test_module`. The module-scoped `meter` fixture came with them unchanged, with the helpers. The old file is named by `docs/the-agent-set.md` line 107, whose item moves it to `tests/test_payload_meter.py`, so it keeps a docstring and no case.

**Left where they stand.** `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` loads the module for `agents_in` and checks the shipped agents' preloaded sections against the role markers, a check across files that stays; so does `tests/test_a_script_copied_alone_exits_2.py`, whose one parametrized case runs each of several shipped scripts copied alone.

**The move check** (`executed`): `bin/test-layout --moved 2f2d21c9 --from tests/test_the_payload_meter_says_what_it_measured.py --to tests/test_payload_meter.py` ends `test-layout: moved: 24 old cases, 25 items against 25 at 2f2d21c97c4f, 0 failed`, exit 0. No mutation table. `--pairs` names none.

**Cases and seconds** (`executed`, serial, pytest's own figure): 25 items in 0.20 s before, in an archive of 2f2d21c9; 26 in 0.26 s after, the census item among them.

**The real-git cases kept.** None: no case runs git.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: no moved case calls `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as 666cedbb, before the commit with the new file staged: the two changed files, the two files above that load the module, `tests/test_every_orchestrator_act_names_its_delivery.py`, `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 28 files: 2,601 passed and 3 skipped. `bin/test-layout --check` exits 0, 168 files read, 121 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `skills/verify/scripts/`, group 31, at 391c7857

**The cases.** `skills/verify/scripts/pytest_record/specseal_pytest_record.py`'s, the 34 of `tests/test_the_recorder_writes_what_its_process_ran.py`, into the new `tests/test_specseal_pytest_record.py` with their bodies. Which process records, the five decided by `pytest_configure` claiming the key, into `Test_pytest_configure`, `test_the_recorder_records_its_own_process` renamed `test_accepts_the_measured_process_as_the_one_that_records` and `test_without_a_key_or_a_directory_nothing_is_written` renamed `test_refuses_to_record_without_a_key_or_a_directory`; the three that drive the class directly into `Test_Recorder`, `path_of`'s two renamed `test_accepts_a_path_only_from_its_own_workers_report_of_it` and `test_refuses_a_freed_workers_reports_to_a_worker_made_after_it`; the 26 that run pytest with the plugin loaded, its behaviour as a whole, into `Test_module`. The fixtures' texts and helpers came with them. No `check:` line names the old file, so it went.

**The move check** (`executed`): `bin/test-layout --moved 17ee8532 --from tests/test_the_recorder_writes_what_its_process_ran.py --to tests/test_specseal_pytest_record.py` ends `test-layout: moved: 34 old cases, 46 items against 46 at 17ee85328290, 0 failed`, exit 0. No mutation table. `--pairs` names one pair, `Test_Recorder`'s two `path_of` cases, which build the recorder with equal arguments and then send it different reports: one holds which report lends a path, the other that a freed worker's address lends nothing, so neither covers the other and none is merged, as group 1 left review-skill-gate's pair.

**Cases and seconds** (`executed`, serial, pytest's own figure, each file from an archive of its commit with the worktree's `.venv`): 46 items in 6.58 s before, at 17ee8532; 47 in 6.61 s after, at 391c7857, the census item among them. Through `bin/test` the new file ran in 9.57 and 9.91 s, the launcher's own cost.

**The real-git cases kept.** None: no case runs git. Every case of `Test_pytest_configure` and `Test_module` runs a real pytest, because what the recorder writes is what that process ran.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: no moved case calls `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as 391c7857, before the commit with the new file staged and the old one removed: the new file, the three other files naming the recorder (`tests/test_a_release_publishes_its_note.py`, `tests/test_the_gate_hands_cmd_a_path_it_can_run.py`, `tests/test_the_seal_is_taken_once_by_the_sealer.py`), the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 26 files: 2,643 passed and 4 skipped. `bin/test-layout --check` exits 0, 168 files read, 120 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats the new file clean.

### Batch B, `skills/verify/scripts/`, group 32, at bf6df24b

**The module.** `skills/verify/scripts/arm_check.py`, whose 63 cases are the whole of `tests/test_arm_check.py`, which keeps its name and now declares `TARGET`. 60 take classes with their bodies, ten renamed to the pairs:

- `Test_module`, nine: the classification tables' five, the real hook's source segments, `restore`'s refusal, the stale cache `clear_bytecode_cache` removes, and `command_words`' Windows split, each of a function with one case.
- `Test_arms`, nine: `test_an_unclassified_node_type_is_refused_rather_than_skipped` renamed `test_refuses_an_unclassified_node_type_rather_than_skipping_it`, `test_the_fixtures_arms_are_counted_by_construction` renamed `test_accepts_the_fixtures_arms_as_counted_by_construction`.
- `Test_mutate`, eleven: `test_an_arm_with_no_defined_mutation_is_refused_not_reported_unwatched` renamed `test_refuses_an_arm_with_no_defined_mutation_rather_than_reporting_it_unwatched`, `test_a_mutation_inverts_the_arm_and_leaves_the_module_parseable` renamed `test_accepts_an_inversion_that_leaves_the_module_parseable`.
- `Test_run_arms`, fifteen: `test_a_watched_arm_is_killed_and_an_unwatched_one_survives` renamed `test_accepts_a_watched_arm_as_killed_and_an_unwatched_one_as_survived`, `test_a_command_that_never_returns_is_recorded_as_unmeasured` renamed `test_refuses_a_command_that_never_returns_as_unmeasured`.
- `Test__report`, seven: `test_the_report_names_the_scope_the_shape_and_the_line_of_a_survivor` renamed `test_accepts_a_survivor_with_its_scope_shape_and_line`, `test_the_report_does_not_call_a_mutated_arm_unmutated` renamed `test_refuses_to_call_a_mutated_arm_unmutated`.
- `Test_main`, nine: `test_the_checker_is_report_only_and_exits_zero_over_the_real_module` renamed `test_accepts_a_report_only_run_at_exit_zero_over_the_real_module`, `test_a_negative_bound_is_refused_rather_than_measured` renamed `test_refuses_a_negative_bound_rather_than_measuring`.

The two triple-quoted sources fed to `textwrap.dedent` keep their old indentation inside the literal, because the AST compares the string and not what `dedent` makes of it; the first draft re-indented them and the check named both bodies.

**Left where they stand.** For #923, at the top level of the file under their names: `test_every_bound_of_the_range_table_is_a_python_ci_runs_this_module_at`, which reads `.github/workflows/test.yml`; `test_a_job_counts_only_where_its_pytest_line_selects_this_module`, whose subject is this file's reader of that workflow's pytest lines; and `test_the_skill_calls_its_survivor_counts_a_measurement_and_not_a_property`, which reads the verify skill. `docs/the-broad-gate.md` line 153 names the file, which keeps its name, so the line is unchanged, as `spec.md` says.

**The lines rewritten.** The docstring no longer names `tests/test_chain_hooks.py#reader_blanking_passes`, which left the tree at 8350c578: the sentence keeps what reading `ast`'s class tree does and drops the precedent it pointed to, because that case exists nowhere. `git grep reader_blanking` outside `seal/specs/` now finds nothing.

**The move check** (`executed`): `bin/test-layout --moved 6df0950b --from tests/test_arm_check.py --to tests/test_arm_check.py` ends `test-layout: moved: 63 old cases, 95 items against 95 at 6df0950bb66f, 0 failed`, exit 0. No mutation table. `--pairs` names one pair, `Test_arms`' fixture count and its flattening case, which read `arms` over one fixture and assert different facts of the answer, the count per scope and the nested segments' text; neither covers the other, so none is merged.

**Cases and seconds** (`executed`, serial, pytest's own figure): 93 passed and 2 skipped in 10.53 s before, in an archive of 6df0950b; 94 passed and 2 skipped in 10.43 s after, the census item among them. The two skipped are the t-string cases, which need Python 3.14.

**The real-git cases kept.** None: no case runs git.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: the file calls `code_lines` from conftest and no `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as bf6df24b: the changed file, the two `mutation_check.py` files, which load the module through the command, `tests/test_ci_gives_the_checks_what_they_need.py`, whose `jobs` the file imports, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`, 26 files: 2,616 passed and 5 skipped. `bin/test-layout --check` exits 0, 168 files read, 119 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats the file clean.

### Where the ninth spawn stopped

At the boundary after group 32, at 903d5f46. The next module in `skills/verify/scripts/`, `session_cost.py`, holds three old files and 6,157 lines to place, and the light files of `broad_gate.py` run that module's mutants; neither could close with a complete record in what was left of this spawn.

### The tenth spawn

**What this spawn was asked.** The rest of `skills/verify/scripts/`: `session_cost.py`'s three old files, split into several groups along public functions if one would not close; `broad_gate.py`'s light files, renaming the names that collide in `tests/test_broad_gate.py` and confirming each move check failure is the autouse fixture or a named rename, then the module's mutants once; the light files of `seal_stamp.py`, `unverified_check.py` and `pact_check.py`. Then `skills/code-review/scripts/` with `agents/sealer.md` line 144, `skills/settle/scripts/` and `.github/scripts/` with `skills/writing-style/SKILL.md` line 268, `skills/implement/scripts/` with `seal.py`'s light files and the eleven re-export and writer cases groups 22 and 23 left, settling `overview.md`'s row on `docs/one-root-by-lifetime.md` line 223 when the writer cases land, and `evals/scripts/`. A line with no verdict is recorded and left; a placement that makes an item name too little or too much is a row of `overview.md` for the framer.

**Whether the frame holds** (`read`). It holds for `session_cost.py`: `spec.md` *The check lines the remaining groups meet* keeps `docs/measuring-a-run.md` lines 21, 31, 38, 46 and 68 on `tests/test_session_cost.py`, and its three `## Rule changes` items move lines 54, 100 and 114 from the two other old files to it. No old file prices at 60 s (`executed`, `.test_durations`: 28.6 s, 0.3 s and 1.1 s), so rule 3 does not apply and the cases are placed. For `broad_gate.py` it does not hold in one item, below under *The eleventh spawn*.

### Batch B, `skills/verify/scripts/`, group 33, at c9af3c38

**The cases.** `skills/verify/scripts/session_cost.py`'s 194, the whole of three files, into `tests/test_session_cost.py`, which keeps its name and now declares `TARGET`. The file's helpers stay at the top in their order, then the post file's and the guard file's; two definitions each of `SCRIPT`, `HUGE_INT` and `ROOT` became one, and so did the imports.

- `Test_main`, 136: the 134 cases of the old file that run the command, and the post file's two that call `main` and refuse. `test_it_separates_command_time_from_model_time` is renamed `test_accepts_a_transcript_and_separates_command_time_from_model_time`, and `test_post_with_json_refuses` `test_refuses_post_with_json`.
- `Test_emit`, 7: the post file's cases run through `main` that hold whether `emit` prints a reading or posts it. `test_main_posts_the_report_it_would_have_printed` is renamed `test_accepts_a_reading_and_posts_the_report_it_would_have_printed`, and `test_an_empty_reading_is_refused_rather_than_posted` `test_refuses_an_empty_reading_rather_than_posting_it`.
- `Test_post`, 11: the post file's cases that call `post`. `test_one_open_posts_once_to_that_issue` is renamed `test_accepts_one_open_log_and_posts_once_to_it`, and `test_more_than_one_open_is_named_and_nothing_is_posted` `test_refuses_to_post_where_more_than_one_log_is_open`.
- `Test_family`, 17: the old file's cases that call `family`. `test_a_runner_named_by_path_is_a_test_run` is renamed `test_accepts_a_runner_named_by_path_as_a_test_run`, and `test_git_named_anywhere_but_a_command_word_is_not_git` `test_refuses_git_named_anywhere_but_a_command_word`.
- `Test_module`, 23: the one case each of `shell_words`, `load` and `token_totals`; the post file's two of `read_says`, two of `open_log`, the one of `comment_body` and the default label's, none of which has a case of the other kind; and the guard file's 14, which walk the module's own source, with their walk.

**Two bodies changed, and one fixture.** The post file's `transcript` is a one-call transcript and the old file's a three-call one, under one name. The post file's is `Test_emit`'s own fixture, so the six cases requesting it fail the fixture condition with their bodies unchanged. `token_thirds`' docstring named `tests/test_a_derived_number_reaching_an_int_carries_a_guard.py` as the check that enumerates the sites, which is now `tests/test_session_cost.py`: the docstring names the new file, and `test_the_module_states_the_rule_and_the_two_shapes_it_misses` asserts that name. The edited case was seen red against the docstring as it stood (`executed`, 1 failed), then green once the docstring changed.

**The pairs.** `--pairs` names 20, and none is merged. Four in `Test_main` have equal bodies once strings are normalised: each flattens a segment report and asserts sentences, and the two of each pair assert different sentences over different fixtures. Sixteen in `Test_post` call `post` with the same three arguments; each case first gives `_gh` a different listing or exit, which the report cannot see, so each holds a different state of the log.

**Left where they stand.** `docs/measuring-a-run.md` names `tests/test_session_cost_post.py` on lines 100 and 114 and the guard file on line 54, and `spec.md`'s items move each to `tests/test_session_cost.py`, so the two files stay until the settle with a docstring naming where their cases went and no case. `tests/test_a_segment_feeds_the_flow_log.py` reads prose and stays, as `spec.md` says.

**The move check** (`executed`):

`bin/test-layout --moved 95d02cc8 --from tests/test_session_cost.py tests/test_session_cost_post.py tests/test_a_derived_number_reaching_an_int_carries_a_guard.py --to tests/test_session_cost.py tests/test_session_cost_post.py tests/test_a_derived_number_reaching_an_int_carries_a_guard.py`

`test-layout: moved: 194 old cases, 221 items against 221 at 95d02cc818d9, 8 failed`, exit 1. Each line was read: 6 are `Test_emit`'s `transcript`, and 2 the edited docstring case, named on both sides. No move needed repair, so `session_cost.py` runs its mutants.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `skills/verify/scripts/session_cost.py` with `--tests "bin/test tests/test_session_cost.py -q -p no:xdist -x"`, at the tree committed as c9af3c38; the old column in an archive of 95d02cc8 against the three old files, run with the worktree's `.venv`). 63 mutants, s1 to s63, at the decision points of the public functions the five classes reach: 50 red and 13 survived, in 347.0 s after a 7.9 s baseline. The old column ran the 13 in 110.1 s, and every one survived there too. An id here names a row of this table alone, and the exact replacements are kept with the build's driver outside the tree.

| # | Mutation | New file | Old files |
|---|---|---|---|
| s1 to s14 | `parse_time` keeps a naive stamp; the heredoc reader joins no continued line, or ignores the tabs `<<-` allows; a `#` inside a word starts a comment; `shell_words` reads an assignment as a command; `runs_git` forgets `gh`; `abbreviates` takes a two-letter option; `writes` forgets `find`'s actions or `awk`'s long include; `only_reads` reads past a substitution, or reads a write as a read; `family` reads `git` by the anchored pattern, or reads nothing as `read`; `count` takes a `bool` | red | not run |
| s15 | `count` returns a non-finite float | SURVIVED | SURVIVED |
| s16, s17, s19 | `message_key` takes a list; `tool_name` keeps a name that is no string; `load` counts one message's turn once per row | red | not run |
| s18 | `load` keeps a row with no stamp | SURVIVED | SURVIVED |
| s20, s21 | `analyse` counts a model gap of 900 s or more; the repeats keep `other` | SURVIVED | SURVIVED |
| s22, s23 | `spawn_cuts` cuts at the last spawn's start; `spawn_cycles` names no tail | red | not run |
| s24 to s26 | `token_thirds` computes from two inputs; `subagent_transcripts` walks the session's directory and not its `subagents/`; `resume_cuts` cuts at a row not marked `isMeta` | SURVIVED | SURVIVED |
| s27 to s37 | `resume_cuts` cuts at any user row; `widest_idle_gap` names no gap; `join_segments` lets one spawn claim two files, or joins outside the tolerance; `measure_segments` never cuts an own file; `token_totals` counts a turn per row; `report` calls a negative span zero, prints idle on a span that is not positive, names nothing where `other` does not lead, compares the unrounded ratio, or prints the context line off a zero baseline | red | not run |
| s38 | `report`'s `nothing obvious` line ignores the repeat time | SURVIVED | SURVIVED |
| s39 to s41, s43 to s45 | `report_spawns` compares the unrounded minute, or refuses an exact cover; `segment_kind` keeps the prefix; `report_breaches` reconciles an own file's counts; `report_grades` grades a smith, or says every row meets its bar | red | not run |
| s42 | `report_breaches` prints nothing where segments are unnamed and no agent spawned | SURVIVED | SURVIVED |
| s46, s47 | `report_segments` drops the unnamed segments' paragraph; `newest` answers None where the directory exists | SURVIVED | SURVIVED |
| s48 to s56 | `open_log` never says closed, or reads two open as one; `read_says` never reads stdin; `post` posts in the unreadable, no-history, closed or many-open state, or calls a failed comment posted; `emit` posts a reading of blanks | red | not run |
| s57 | `emit` replaces the path as given and not its absolute spelling | SURVIVED | SURVIVED |
| s58, s59, s61 to s63 | `main` takes `--post` with `--json`, prints no `--spawns` report, exits on a transcript with tokens and no call, or drops the coordinator line; `opening_stamp` opens at no stamp | red | not run |
| s60 | `main` prints the segment report under `--segments --json` | SURVIVED | SURVIVED |

The 13 old gaps: no case hands `count` a value it should refuse and reads it back, writes a row with no stamp, puts fifteen minutes between two calls of the plain reading, repeats an `other` command, gives `token_thirds` exactly two inputs, keeps a transcript beside `subagents/` rather than in it, writes a coordinator row without `isMeta`, prints the plain reading with a repeat and a ratio of 1.2 at once, names an unnamed segment where no agent spawned, asserts the unnamed segments' paragraph, runs `--latest`, posts a body whose path was given relative, or asks `--segments` with `--json`. No case was added: the old files miss each.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: the file calls `census_case` from conftest and no `read`, `imported_roots` or `repo_relative` (`read`).

**Cases and seconds** (`executed`, serial, pytest's own figure, each tree an archive run with the worktree's `.venv`): 221 items in 7.08 s before, at 95d02cc8; 222 in 7.00 s after, at c9af3c38, the census item among them.

**The real-git cases kept.** None: no case runs git. `Test_main`'s cases run the command in a process, because what a person reads is what it prints.

**The boundary** (`executed`). At the tree committed as c9af3c38, run before the commit over the same bytes: the three changed test files; the seven other files that read `session_cost.py` (`tests/test_a_document_that_names_a_script_says_how_to_reach_it.py`, `tests/test_a_reference_root_is_read_and_never_taken.py`, `tests/test_a_script_copied_alone_exits_2.py`, `tests/test_a_segment_feeds_the_flow_log.py`, `tests/test_one_word_one_meaning.py`, `tests/test_the_handoff_before_round_one.py`, `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`); `tests/test_payload_meter.py`; the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 33 files: 2,886 passed and 11 skipped in 29.1 s. `bin/test-layout --check` exits 0, 168 files read, 0 refused, 118 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Where the tenth spawn stopped

At the boundary after group 33, at c9af3c38 and the record commit after it. The next group, `broad_gate.py`'s light files, draws on three files with name collisions on both sides and a frame item that names too little (below), and could not close with a complete record in what was left of this spawn.

### The eleventh spawn

**What this spawn was asked.** `broad_gate.py`'s light files, renaming the names that collide in `tests/test_broad_gate.py` and confirming each move check failure is the autouse fixture or a named rename, then the module's mutants once; the light files of `seal_stamp.py`, `unverified_check.py` and `pact_check.py`; then the five directories not started, in the order of the tenth spawn's ask.

**Whether the frame holds** (`read`). It holds for `broad_gate.py`, with the one item `overview.md` already leaves to the framer: `spec.md`'s item for `docs/the-broad-gate.md` line 62 names `tests/test_broad_gate.py` alone, and the partition cases that hold the line's rule stay in the old file. The tenth spawn's count of the cmd file's moving cases was fourteen; its own list names fifteen, and fifteen moved.

### Batch B, `skills/verify/scripts/`, group 34, at 5966150b and ffd898ec

**The cases.** 37 of `broad_gate.py`'s cases in the two light files, into `tests/test_broad_gate.py`, as *What remains* at c9af3c38 listed them: from the cmd file 15 of 16, six to `Test_handed_to_shell`, one to `Test_command_names_backslashed`, six to `Test_run`, one to `Test_failure_lines`, one to `Test_module`; from the steps file 22 of 31, six to `Test_job_steps`, six to `Test_module`, six to `Test_main`, three to `Test_coverage_line`, one to `Test_base_is_main`. The template case and the nine that read `hygiene.yml`, the verify skill or `docs/the-broad-gate.md` stay for #923; the steps file imports `reasons()` from the new file.

**The names.** The cmd file's `ROW` is `CMD_ROW` and its `a_record` is `a_counted_record`, beside the `ROW` and `a_record` the file holds; six bodies and one parametrize list change for it. Its `gate_module`, a fresh load per call, moves under its name, and the steps file's, which only made its `gate`, gives way to the file's `gate`. The steps file's `commit` gives way to the file's `commit_everything_as_e`: they differ in `--allow-empty`, and no moved case commits an empty tree (`read`). Its `ITEM` gives way to the file's, which no moved case names, and its `OVERVIEW` was the same text. `ROOT` stays the file's `pathlib.Path`; `GATE`, `STAMP` and `HYGIENE` are built from it.

**The pairs.** `--pairs` named two once the cases were placed, and both are merged under rule 2: `test_a_name_that_starts_in_no_directory_is_handed_over_as_written` into `test_only_the_command_names_have_their_slash_turned`, whose body it shared, its 19 rows after the 33; and `test_a_commented_out_step_is_not_a_step` into `test_the_reader_takes_the_steps_of_the_job_it_was_asked_for`, whose equality over the same workflow already excludes the commented step. `--pairs` names none in the file after.

**The docstring.** `command_names_backslashed`'s docstring named the cmd file for its `2>&1` row; ffd898ec names `tests/test_broad_gate.py`'s `Test_handed_to_shell`, and no code changes. The two comments in `broad_gate.py` naming the steps file, at its partition and at `ONLY_AT_MAIN`, stay true: the cases they name stay there.

**The move check** (`executed`):

`bin/test-layout --moved 10667b32 --from tests/test_broad_gate.py tests/test_the_gate_hands_cmd_a_path_it_can_run.py tests/test_the_gate_names_every_step_ci_runs.py --to tests/test_broad_gate.py tests/test_the_gate_hands_cmd_a_path_it_can_run.py tests/test_the_gate_names_every_step_ci_runs.py`

`test-layout: moved: 198 old cases, 314 items against 315 at 10667b32ad71, 45 failed`, exit 1. Each line was read: 28 are `_no_ambient_pull_request` requested in the working tree only; 7 old bodies and their 7 surplus lines are the two renames; 2 old bodies are the two merges; 1 is the count, one item fewer for the commented-step merge.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `skills/verify/scripts/broad_gate.py` with `--tests "bin/test tests/test_broad_gate.py -q -p no:xdist -x"`, at the tree committed as ffd898ec; the old column in an archive of 10667b32 against the three old files, run with the worktree's `.venv`). 113 mutants, b1 to b113, at least one per class at the decision points of the public functions: 109 red and 4 survived, in 270.6 s after a 13.4 s baseline. The old column ran the 4 in 46.4 s, and each survived there too. b1 was re-run alone with pytest's output kept, and its red is `Test_load`'s refusal of a sibling that raises.

| # | Mutation | New file | Old files |
|---|---|---|---|
| b1 to b21 | `load` catches only `ImportError`, or loads a missing file; `shipped_gate` re-runs itself; `plugin_version` prints an empty version; `under` takes no root as every root; `copy_origin` reads this file; `gate_copy` prints on equal bytes; `Base.moved` reads only a missing commit; `moved_line` calls every ref the runner's, or drops the no-commit sentence; `short_commit` answers for nothing; `names_a_branch` and `a_runner_could_hold` say yes; `resolve_base` skips the upstream, or reads a revision expression through a remote; `seal_home` skips the shared root, or takes any local one; `broad_command` reads a file that will not read, a doubled row or an empty value; `names_this_row` takes any first cell | red | not run |
| b22 | `refused_broad_row` answers where the walk read the row | SURVIVED | SURVIVED |
| b23 to b28, b30 to b49 | `stopping_line` answers for a sentence that quotes no line, or takes the first line; `rows_written_below` passes a heading; `hidden_row_at` calls a comment a fence; `fence_left_open` says yes; `missing_row` skips the walker's refusal or the comment; `walker_refusal` keeps the rows-below clause, wants five pipes, or calls a row below the stopping line that line; `wholly_substituted` takes a part; `not_as_written` refuses `&&`; `Check` fails only exit 1; `run` asks the caller's directory, or says nothing of the rewrite on the record or on stderr; `as_cmd_expands` ignores the environment, or computes only `CD` in capitals; `cmd_exe_reads` answers yes off Windows, or reads a quoted `COMSPEC` as another shell; `handed_to_shell` asks the current directory, or expands no `%VAR%`; the scan keeps the leading `@` in the asked part, asks about an empty part, or reads `&` as no separator | red | not run |
| b29 | `missing_row` asks whether any fence is left open, not one above the row | SURVIVED | SURVIVED |
| b50 | the scan keeps command position after `<` or `>` | SURVIVED | SURVIVED |
| b51 to b69, b71 to b113 | the scan asks about a built-in, turns no quoted name, or opens no name at `^`; `record_key` gives one key twice; `recording_env` and `record_path`, `read_record`'s key, collections, unread lines, stops and red sessions; `failing_files` repeats a file; `quote` leaves a Windows path bare; `base_word`'s five rows; `compare_at_base` compares where the base was not checked out, or runs the row without a shell; `unquote`, `job_steps`'s job, quotes, commented step and colon; `PARTITION` with a category for a reason, a row with an arm and a reason, and an arm `gate()` stops running; `base_is_main`, `steps_for`, `left_out_clause`, `workflow_text`, `unanswered` and `coverage_line`; `suite_counts`, `round_records`, `kept_runs`, `write_gate_file`, `rounds_rows`; `panel`'s base, workflow count, `gate` row and counts; `failure_lines`' heading, missing record, stopped sessions and non-suite check; `failed_form`'s pad, `report_lines`' marks; `gate`'s refusals, coverage line and preflight; `uncommitted_line`; `main`'s redirect, the variable it takes out, and its exit | red | not run |
| b70 | `compare_at_base` hands `base_word` exit 0 whatever the base's run exited | SURVIVED | SURVIVED |

The four old gaps: no case has the walk read a `Broad gate` row with an empty value above a line it refused; puts a fenced row above a fence left open further down; hands the scan a redirection followed by a name that starts in a directory; or has a file the base's run never collected while that run exited non-zero. No case was added: the old files miss each.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: neither old file is one phase 4's table names (`read`).

**Cases and seconds** (`executed`, serial, pytest's own figure, each tree an archive run with the worktree's `.venv`): 316 items in 8.48 s before, at 10667b32; 315 in 8.87 s after, at ffd898ec, the census item among them.

**The real-git cases kept.** The six moved to `Test_main` each build a repository and run the command over it, because what they hold is what the command prints over a branch; `test_the_row_runs_on_the_real_platform` and `test_a_switch_against_a_program_runs_on_the_real_platform` run the machine's own shell, the second only where it is `cmd.exe`.

**The boundary** (`executed`). At the tree committed as 5966150b, and again at ffd898ec, run before each commit over the same bytes: the three changed files; every other test file naming `broad_gate`, `test_broad_gate` or either old file; `tests/test_payload_meter.py`; the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 49 files: 3,907 passed and 12 skipped in 41.8 s. `bin/test-layout --check` exits 0, 168 files read, 0 refused, 118 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed file clean.

### Batch B, `skills/verify/scripts/`, group 35, at 2272cd1e

**`seal_stamp.py` and `pact_check.py`: nothing to move** (`read`, by the calls each case makes, at ffd898ec). Every file naming `seal_stamp` outside the module's rule 1 file either reads documents and agent definitions (the sealer file's Parts 2 and 3, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_commit_gate_decides_at_the_commit.py`), loads the module as an oracle for another module's cases (`tests/test_the_release_seal_is_drawn.py`, `.github/scripts/release_seal.py`'s), or compares files with each other. Of `pact_check.py`'s, `tests/test_a_signer_declares_its_pact.py` keeps the shipped configs, the templates and `seal.py`'s re-export, and `tests/test_config.py` and `tests/test_coordinates.py` hold other modules' cases.

**`unverified_check.py`: two cases** (`read`). Of the files naming it, only `tests/test_one_heading_rule_holds_to_commonmark.py` holds cases whose subject is one of its functions and that read no file of this repository: `test_the_frames_shapes` and `test_a_seeded_generated_corpus`, which hold `heading_level` to the markdown-it oracle. They move into `Test_heading_level` with `disagreements` and the shapes and corpus it reads. The two cases over every tracked `.md` file read documents, stay, and import `disagreements`. The rest compare readers with each other (`tests/test_every_reader_ends_a_line_where_gfm_does.py`, `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/test_both_editions_carry_the_same_folds.py`, `tests/test_the_hooks_hide_what_a_renderer_hides.py`), use the module as a reader for a check of documents or agent definitions (`tests/test_docs_line_wrap.py`, `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py`), or are the cases phase 5 left in `tests/test_unverified_rows_close.py`.

**One name added.** The moved cases call the module as `uc`, and the new file names it `UC`; the new file binds `uc = UC` once, with a comment, so the bodies move unchanged and the module skips the mutants. `heading_level`'s docstring named the old file as what holds it to markdown-it; it names both files, and no code changes.

**The move check** (`executed`):

`bin/test-layout --moved HEAD --from tests/test_unverified_check.py tests/test_one_heading_rule_holds_to_commonmark.py --to tests/test_unverified_check.py tests/test_one_heading_rule_holds_to_commonmark.py`, HEAD at ffd898ec

`test-layout: moved: 171 old cases, 329 items against 329 at ffd898ec87dc, 0 failed`, exit 0. No mutants run.

**Cases and seconds** (`executed`, serial, each tree an archive run with the worktree's `.venv`): 330 items in 6.48 s before, at ffd898ec; 330 in 6.89 s after, at 2272cd1e. In both archives the two tracked-file cases fail, because an archive is no git repository for their `git ls-files`; both pass in the worktree's boundary run.

**The boundary** (`executed`). At the tree committed as 2272cd1e, run before the commit over the same bytes: the two changed test files and every other test file naming `unverified_check`, `unverified-check`, the heading file or `commonmark_oracle`, with the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 45 files: 4,285 passed and 12 skipped in 47.0 s. `--check`, `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0 as at group 34; ruff checks and formats `unverified_check.py` and the two test files clean; `--pairs` names none in `tests/test_unverified_check.py`.

### Batch B, `skills/code-review/scripts/`, group 36, at 19c01e3b

**Whether the frame holds** (`read`). It holds: `spec.md` *The check lines the remaining groups meet* rewrites `agents/sealer.md` line 144 in this group's commit, and its item for `docs/the-review-record.md` *The guarantee* (line 290) moves that line to both files, so every line the moving cases hold has a verdict. Neither old file prices at 60 s (`executed`, `.test_durations`: 14.9 s and 3.4 s), so the cases are placed.

**The cases.** `chain_check.py`'s 19 light cases, into `tests/test_chain_check.py`. From `tests/test_the_sealer_guarantees.py`, 14: three to a new `Test_verdicts_of`, five to a new `Test_earlier_verdicts`, six to a new `Test_guarantee`, which carries the `ready-needs-sealed` mark the old class carried. Seven were renamed so each class has its accepting and refusing case: `test_each_verdict_is_read_in_its_shape` to `test_accepts_each_verdict_in_its_shape`, `test_a_verdict_in_a_comment_is_not_read_and_two_lines_are_two` to `test_refuses_a_verdict_in_a_comment_and_reads_two_lines_as_two`, `test_each_earlier_run_is_read_with_its_verdict_word` to `test_accepts_each_earlier_run_with_its_verdict_word`, `test_text_after_the_target_that_is_no_earlier_run_reads_no_word` to `test_refuses_text_after_the_target_that_is_no_earlier_run`, `test_a_sealed_verdict_at_head_passes` to `test_accepts_a_sealed_verdict_at_head`, `test_absent_unfilled_and_behind_head_are_named` to `test_refuses_absent_unfilled_and_behind_head_by_name`, and `test_a_near_miss_of_the_verdict_is_refused_at_its_line` to `test_refuses_a_near_miss_of_the_verdict_at_its_line`. From `tests/test_local_mode_reaches_the_review_chain.py`, all five, to a new `Test_declared_for_this_branch` with the file's own session-scoped `_repo_template`; `test_local_mode_is_told_it_is_local_mode` is `test_refuses_a_local_declaration_and_says_it_is_local_mode` and `test_shared_mode_is_still_told_to_add_the_file` is `test_accepts_a_shared_root_and_tells_it_to_add_the_file`. The local file goes, since no `check:` line names it. The sealer file keeps `TestTemplate`, `TestDefinition`, `TestDocument` and `test_every_committed_guarantee_shows_its_one_verdict_line`, which read the template, the definition, the document and the committed records.

**The names.** The sealer file's `ROUTING` is `SEALED_ROUTING` and its `TEMPLATE` is `GUARANTEE_TEMPLATE`, beside the file's own `ROUTING`, a format string, and `TEMPLATE`, the round template. Its `ITEM` gives way to the file's, which the moved cases name under the same word. Its `git` gives way to the file's `git_out`, which returns the same stripped stdout. The local file's `git` returned the process, and the helpers that moved with it read the file's `git_out`; the check does not compare a helper's body.

**Lines outside `docs/`.** `agents/sealer.md` line 144 reads `check: tests/test_the_sealer_guarantees.py tests/test_chain_check.py`. `tests/e2e/commit/test_commit_flow.py`'s docstring names `tests/test_chain_check.py#NEAR_MISSES`.

**The move check** (`executed`):

`bin/test-layout --moved HEAD --from tests/test_chain_check.py tests/test_the_sealer_guarantees.py tests/test_local_mode_reaches_the_review_chain.py --to tests/test_chain_check.py tests/test_the_sealer_guarantees.py`, HEAD at c30f7d95

`test-layout: moved: 116 old cases, 246 items against 246 at c30f7d9521c6, 8 failed`, exit 1. Each line was read: 6 are the `item` fixture, whose definition names `SEALED_ROUTING`; 1 old body and its surplus line are the `GUARANTEE_TEMPLATE` rename. The five local-mode cases pass.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `skills/code-review/scripts/chain_check.py` with `--tests "bin/test tests/test_chain_check.py -q -p no:xdist -x"`, at the tree committed as 19c01e3b; the old column in an archive of 2272cd1e, whose test files are c30f7d95's, against the three old files, run with the worktree's `.venv`). 54 mutants: phase 5's k1 to k36, rerun from its driver, and g1 to g18 at the decision points of the functions the moved cases reach. 51 red and 3 survived, in 714.7 s after a 40.4 s baseline; the old column ran the 3 in 160.2 s, and each survived there too.

| # | Mutation | New file | Old files |
|---|---|---|---|
| k1 to k11, k13 to k36 | phase 5's table, `phases/phase-5.md` *`skills/code-review/scripts/chain_check.py`* | red | not run |
| k12 | `reopened_of` reads its value against the `regression:` row | SURVIVED | SURVIVED |
| g1, g2 | `verdicts_of` drops an indented line's indent, or reads a comment's line | red | not run |
| g3, g4 | `verdict_word` calls every shape `sealed`, or reads a retired word only alone | red | not run |
| g5 to g7 | `earlier_verdicts` reads text after the target as entries, quotes an entry without its separator, or gives an empty rest an entry | red | not run |
| g8 to g13 | `guarantee` refuses no earlier-run entry, reads no zero-verdict file, passes `withheld`, reads no retired word, lets any record follow the commit, or reads past an unclosed comment | red | not run |
| g14 | `target_row` takes the first row of any name | red | not run |
| g15, g16 | `declared_for_this_branch` never names local mode; `local_root` calls a shared root local | red | not run |
| g17 | `declared_for_this_branch` takes two committed declarations naming the branch | SURVIVED | SURVIVED |
| g18 | `declared_for_this_branch` reads a detached HEAD as a branch | SURVIVED | SURVIVED |

The three old gaps: k12 is phase 5's equivalent mutant; no case commits two declarations naming one branch, or runs the check on a detached HEAD with no `GITHUB_HEAD_REF`. No case was added.

**Phase 4's survivors.** None of h2, h12 and h23 is reached (`read`).

**Cases and seconds** (`executed`, serial, each tree an archive run with the worktree's `.venv`): 247 items in 39.30 s before, at 2272cd1e; 247 in 39.23 s after, at 19c01e3b.

**The real-git cases kept.** The `item` fixture builds a repository per case for the arm and `main`, because the arm reads what git carries; the five local-mode cases copy one template per case and run the command, because what they hold is the sentence it prints.

**The boundary** (`executed`). At the tree committed as 19c01e3b, run before the commit over the same bytes: the changed files, the commit flow among them, and every test file naming `chain_check`, `chain-check`, `sealer.md`, the sealer file or `agents/`, with the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 74 files: 5,690 passed and 14 skipped in 60.6 s. `bin/test-layout --check` exits 0, 167 files read, 0 refused, 117 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed Python file clean; `--pairs` names none in `tests/test_chain_check.py`.

### Where the eleventh spawn stopped

At the boundary after group 36, at 19c01e3b and the record commit after it. The next directory, `skills/settle/scripts/`, writes three new files from the 114 cases of three old files and could not close with a complete record in what was left of this spawn.

### The twelfth spawn

**What this spawn was asked.** `skills/settle/scripts/`, with `skills/writing-style/SKILL.md` line 268; `skills/implement/scripts/`, with `seal.py`'s light files and the row of `overview.md` on `docs/one-root-by-lifetime.md` line 223; `.github/scripts/`, with line 268's other file; `evals/scripts/`. A line with no verdict is recorded and left; an item that names too little or too much is a row of `overview.md` for the framer.

**Whether the frame holds** (`read`). It holds for `skills/settle/scripts/`: every `check:` line naming the three old files has an item in `spec.md` *Rule changes* or a row in *The check lines the remaining groups meet*, and the two rule markers `a-settle-is-no-deletion` and `an-empty-root-is-settled` are read by `.github/scripts/rules.py#markers` from any test file. It holds for `seal.py` with the one item `overview.md` already leaves to the framer, settled below. The three old settle files price at 49.2 s, 37.0 s and 3.4 s (`executed`, `.test_durations`), so the cases are placed.

### Batch B, `skills/settle/scripts/`, group 37, at 809408e5

**The cases.** 98 of the 116 cases of the three old files, into three new files, bodies unchanged:

- `tests/test_fold_check.py`: the fold file's 21, 19 in `Test_main` (every one runs the command) and 2 in `Test_module` (the estimate and `declared` of a row written again below the stop). Renamed: `test_accepts_this_repository_with_no_flags`, `test_refuses_a_ceiling_that_is_not_a_positive_integer`.
- `tests/test_rule_changes.py`: the rule-change file's reader cases, 10 in `Test_parse`, and its replay cases, 12 in `Test_replay`. Renamed: `test_accepts_each_shape_as_one_operation_with_its_line`, `test_refuses_a_block_that_does_not_match_whole_at_its_line`, `test_accepts_a_change_and_rewrites_the_text_where_it_stands`, `test_refuses_a_spec_whose_place_it_cannot_find`.
- `tests/test_settle.py`: the rule-change file's 19 cases that run `settle` over a git history and the settle file's 36 that run the command or call its functions: 7 in `Test_report`, 13 in `Test_apply`, 27 in `Test_main`, 8 in `Test_module`. Renamed: `test_accepts_a_spec_with_no_rule_changes_and_lists_it_kept`, `Test_report::test_refuses_a_survey_with_no_base`, `test_accepts_a_spec_that_states_no_rule_and_removes_only_it`, `Test_apply::test_refuses_a_survey_with_no_base`, `test_accepts_a_settled_root_and_says_so`, `test_refuses_local_mode_rather_than_reading_an_empty_repository`.

**Two placed outside their subject's file** (`read`). `test_merge_order_is_the_commit_that_adds_the_spec` calls `rule_changes.py#order`, and `test_the_predicate_asks_every_condition_itself` calls `unverified_check.py#settled`, each over a repository this file's fixtures build. Each is in `tests/test_settle.py`'s `Test_module`: in its subject's file it would need the `repo` fixture, or the `tree` fixture with `moment`, `run` and `git`, defined twice, a twin `--check` refuses, and `tests/conftest.py` already holds a `repo` and a `run` of other bodies. Both hold rules the items for `docs/the-record-layout.md` lines 100 and 109 send to `tests/test_settle.py`, so the placement keeps those items true.

**Left where they stand**, for #923: the fold file's two cases that read the cheat sheets and the settle skill; the rule-change file's `test_the_skills_example_reads_as_the_skill_says`; the settle file's fifteen that read the skill, the documents, the READMEs, the checklist and the cheat sheets, among them `test_a_closed_row_is_told_to_merge_before_its_directory_goes`, which reads the report and the skill and the policy in one body. Each old file keeps a docstring naming where its cases went.

**Helpers.** `spec`, `line_of`, `DOC`, `op` and the `tree` fixture serve both new settle files and the old settle file, so they are `tests/conftest.py`'s; the fixture's definition is the same in both trees, so the fixture condition holds for the cases that request it, the one that stays among them. The two old `git` helpers differ in what they return, and every moved call uses neither return value, so `tests/test_settle.py` keeps the one that returns stdout. The old settle file imports `run`, `moment` and `OVERVIEW_OPEN` from `tests/test_settle.py`, and the old rule-change file `parse` and `rules` from `tests/test_rule_changes.py`.

**Lines outside `docs/`.** `skills/writing-style/SKILL.md` line 268 reads `check: tests/test_the_rules_command_reads_each_rule_off_its_test.py tests/test_rule_changes.py tests/test_censuses.py tests/test_the_agent_contract_holds_the_universal_rules.py`, and `tests/test_a_language_section_of_writing_style_opens_alone.py#WRITING_RULE_CHECKS`, which pins that line, says the same. `settle.py`'s comment on the rule arm's headings names `tests/test_settle.py`, and the old settle file for the kept heading's remedy, which a staying case pins.

**The move check** (`executed`):

`bin/test-layout --moved HEAD --from tests/test_a_document_has_room_for_the_next_fold.py tests/test_settle_applies_rule_changes_in_place.py tests/test_settle_reads_before_it_removes.py --to tests/test_fold_check.py tests/test_rule_changes.py tests/test_settle.py tests/test_a_document_has_room_for_the_next_fold.py tests/test_settle_applies_rule_changes_in_place.py tests/test_settle_reads_before_it_removes.py`, HEAD at db6541fc

`test-layout: moved: 116 old cases, 174 items against 174 at db6541fc96b0, 0 failed`, exit 0. No mutants run. `--pairs` names none in the three new files.

**Cases and seconds** (`executed`, serial, pytest's own figure): 174 items in 15.69 s before, the three old files in an archive of db6541fc with the worktree's `.venv`; 177 items in 15.51 s after over the six files, the three census items among them.

**The real-git cases kept.** The `tree` and `repo` fixtures build a repository per case, and `Test_main`'s command cases build their own: what `settle` reads is released, merged or ordered by git's history. The fold file's three `git init` cases read the repository a command typed below it belongs to.

**Phase 4's survivors.** None of h2, h12 and h23 is reached: no moved case calls `read`, `imported_roots` or `repo_relative` (`read`).

**The boundary** (`executed`). At the tree committed as 809408e5, run before the commit over the same bytes: the six files, `tests/test_a_language_section_of_writing_style_opens_alone.py`, every other test file naming a settle module, `bin/settle` or `bin/fold-check`, `tests/test_docs_line_wrap.py`, `tests/test_config.py`, the two files defining a `tree` fixture of their own, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 44 files: 3,977 passed and 12 skipped in 45.4 s. `bin/test-layout --check` exits 0, 170 files read, 0 refused, 117 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed Python file clean.

### Batch B, `skills/implement/scripts/`, group 38, at 4f350b0f

**The cases.** `seal.py`'s last light cases, into `tests/test_seal.py` with their bodies: the ten writer cases groups 22 and 23 left in `tests/test_the_mode_question_is_asked_once.py`, eight to `Test_write_row` and two to `Test_with_row`, and the two re-export cases, `test_the_command_and_the_gate_read_one_parser` from the mode file and `test_seal_keeps_one_normaliser` from the signer file, to `Test_module`. Each loads `seal.py` under its own name, as before. `BARE_TABLE` moved with its case. The mode file now holds no case and keeps a docstring, because `docs/one-root-by-lifetime.md` line 223 and its Korean edition's line 212 name it. The other files naming `seal.py` read the READMEs, the templates and the workflows, compare commands with each other, or are the timer census rows of `tests/test_release_hygiene.py`, and stay.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_seal.py tests/test_the_mode_question_is_asked_once.py tests/test_a_signer_declares_its_pact.py --to tests/test_seal.py tests/test_the_mode_question_is_asked_once.py tests/test_a_signer_declares_its_pact.py`, HEAD at 809408e5, ends `test-layout: moved: 174 old cases, 330 items against 330 at 809408e5ec2e, 0 failed`, exit 0. No mutants run. `--pairs` names none in `tests/test_seal.py`.

**The row on line 223, settled** (`read`). The rule *A cell may carry an escaped pipe* says the reader and the writer share the constant that describes a row. Its reader's cases are in `tests/test_config.py` since group 22; its writer's are now in `tests/test_seal.py`: `Test_write_row`'s eight and `Test_with_row`'s two above, and `Test_module::test_the_command_and_the_gate_read_one_parser`. The item names `tests/test_config.py` alone, so it names too little; `overview.md` states the files and leaves the item to the framer.

**Lines rewritten.** The docstrings of `tests/test_seal.py`, `tests/test_config.py`, `tests/test_mode_gate.py` (which had named the mode file as keeping the reader's cases since group 22) and `tests/test_a_signer_declares_its_pact.py`, the citation of the re-export case in `tests/test_the_pull_request_language_is_the_repositorys.py`, and `tests/conftest.py`'s comment on the config texts name the files that hold the cases.

**Cases and seconds** (`executed`, serial): 331 items in 11.13 s before, the three files in an archive of 809408e5; 331 in 10.64 s after.

**The real-git cases kept.** None among the moved cases: each writes a config file in its own directory.

**Phase 4's survivors.** None of h2, h12 and h23 is reached (`read`).

**The boundary** (`executed`). At the tree committed as 4f350b0f, run before the commit over the same bytes: the three files, the files whose docstrings changed, `tests/test_pact_check.py`, `tests/test_one_word_one_meaning.py`, `tests/test_first_setup_asks_once.py`, `tests/test_a_reference_root_is_read_and_never_taken.py`, the two old `seal.py` files, the oracle file, the two new settle files, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 35 files: 3,452 passed and 3 skipped in 40.0 s. `--check`, `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0 as at group 37. Ruff clean on each changed file.

`skills/implement/scripts/` is done.

### Batch B, `.github/scripts/`, group 39, at 46e1ec4c

**The module.** `.github/scripts/issue_claims_check.py`, whose 34 cases of its functions were in `tests/test_a_body_naming_two_issues_claims_one.py`, now `tests/test_issue_claims_check.py`: `Test_read`, `Test_report`, `Test_main`, and `Test_module` for `BLOCK_START`, `body_from`'s two cases, which have no refusing partner, the closer's shared definitions and the module's own source. The old file keeps the four cases that read `docs/issues-and-milestones.md`, the hygiene workflow and its template, and imports `read` from the new file. Its `check:` line moves to both files through `spec.md`'s item. No old file prices at 60 s (`executed`: 0.3 s).

**The merges.** Placed in one class, the old cases gave `--pairs` 23 pairs among fourteen cases of `Test_read`, three groups each asserting one body over a different text. Under rule 2 each group is one parametrized case with a row per text and each old docstring's reason kept as a comment above its row: `test_refuses_a_number_beside_a_claim_with_one_warning` (six rows), `test_accepts_a_number_a_segment_boundary_keeps_apart` (six) and `test_accepts_a_body_that_claims_and_mentions_nothing` (two). `--pairs` names none after.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_a_body_naming_two_issues_claims_one.py --to tests/test_issue_claims_check.py tests/test_a_body_naming_two_issues_claims_one.py`, HEAD at 4f350b0f. As first placed it ended `38 old cases, 50 items against 50 at 4f350b0f9144, 0 failed`; after the merges, `test-layout: moved: 38 old cases, 50 items against 50 at 4f350b0f9144, 17 failed`, exit 1. The 17 lines are the fourteen merged cases and the three they became. No move needed repair.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `.github/scripts/issue_claims_check.py` with `--tests "bin/test tests/test_issue_claims_check.py -q -p no:xdist -x"`, at the tree committed as 46e1ec4c; the old column in an archive of 4f350b0f against the old file, run with the worktree's `.venv`). 34 mutants at the decision points of `prose_only`, `segments`, `claimed_spans`, `read`, `report`, `body_from`, `main` and the three patterns: 24 red and 10 survived, in 9.4 s; the old column ran the 10 in 1.5 s, and each survived there too.

| # | Mutation | New file | Old file |
|---|---|---|---|
| i2 to i6, i10, i14 to i21, i23 to i26, i28 to i30, i32 to i34 | a fence or a span left unmasked; no sentence, blank-line or block cut; a claimed number counted as mentioned; the masked sentence quoted; a claimed or already-seen number warned again; any claim taken as before the number, or the first one named; the annotation prefix, the clean line or the claimed line's words dropped; the file arm or the empty body lost; an absent body read as empty, or exit 2 read as 0; the full stop's lookahead, a list marker's or a heading's space, the blockquote and table markers, the setext underline's or the rule's end anchor dropped | red | not run |
| i1 | the masking turns a newline inside a fence into a space | SURVIVED | SURVIVED |
| i7 | a whitespace-only segment kept | SURVIVED | SURVIVED |
| i8 | a claim's span starts at its keyword, not its digits | SURVIVED | SURVIVED |
| i9 | `claimed` keeps a number claimed twice | SURVIVED | SURVIVED |
| i11 | `mentioned` keeps a number named twice | SURVIVED | SURVIVED |
| i12 | a segment counts a claim after its end | SURVIVED | SURVIVED |
| i13 | a segment with no claim is not passed over | SURVIVED | SURVIVED |
| i22 | a sentence is shortened at any length | SURVIVED | SURVIVED |
| i27 | `ISSUE_REF` reads `#22abc` as a number | SURVIVED | SURVIVED |
| i31 | an ordered-list line opens no block | SURVIVED | SURVIVED |

Every survivor is an old gap. Three no input tells apart: a whitespace segment holds no claim (i7), a claim after a segment's end is never before a number in it (i12), and a segment with no claim adds no warning (i13). For the other seven no case has a fence whose inner newline decides a segment, a claim whose keyword and digits straddle a cut, a number claimed or mentioned twice with the list asserted, a sentence past 160 characters, a number glued to letters, or an ordered list. No case was added.

**Cases and seconds** (`executed`, serial): 50 items in 0.48 s before, in an archive of 4f350b0f; 51 in 0.47 s after over the two files, the census item among them.

**The real-git cases kept.** None: no case runs git.

**Phase 4's survivors.** None of h2, h12 and h23 is reached (`read`).

**The boundary** (`executed`). At the tree committed as 46e1ec4c, run before the commit over the same bytes after the merges: the two files, `tests/test_a_workflow_is_read_the_one_way.py`, whose docstring names a staying case, `tests/test_every_reader_ends_a_line_where_gfm_does.py`, which loads the module, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 27 files: 2,523 passed and 3 skipped in 28.4 s. `bin/test-layout --check` exits 0, 171 files read, 0 refused, 117 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. Ruff clean on each changed file.

### Batch B, `.github/scripts/`, group 40, at 565de415

**The cases.** `release_report.py`'s other four, from `tests/test_the_release_table_reads_two_trees_and_fails_nothing.py` into `tests/test_release_report.py` with their bodies and helpers: the three that run `main` into `Test_main`, and the one that reads this tree against itself through `table` into `Test_module`. The old file keeps the case that reads the tests workflow's `release-report` job, for #923; both docstrings say where the cases are.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_release_report.py tests/test_the_release_table_reads_two_trees_and_fails_nothing.py --to tests/test_release_report.py tests/test_the_release_table_reads_two_trees_and_fails_nothing.py`, HEAD at 409d8037, ends `test-layout: moved: 9 old cases, 15 items against 15 at 409d8037ab94, 0 failed`, exit 0. No mutants run; `--pairs` names none.

**Cases and seconds** (`executed`, serial): 16 items in 0.46 s and 0.08 s before, in an archive of 409d8037; 16 in 5.51 s, 3.23 s and 0.09 s after over three runs, the slowest case 0.01 s in each tree, so the spread is the shared machine's.

**The boundary** (`executed`). At the tree committed as 565de415, before the commit over the same bytes: the two files, `tests/test_a_release_cannot_ship_an_untrue_milestone.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 26 files: 2,488 passed and 3 skipped. `--check` (171 files, 0 refused), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

### Batch B, `.github/scripts/`, group 41, at 56a8ac20

**The module.** `.github/scripts/rules.py`, whose 19 cases of its functions were in `tests/test_the_rules_command_reads_each_rule_off_its_test.py`, now `tests/test_rules.py`: 18 that run `main` in `Test_main`, renamed `test_accepts_a_check_line_in_grammar` and `test_refuses_every_other_spelling_at_its_line`, and the near-miss pattern's in `Test_module`. The old file keeps the cases that read the record layout document, the `rule` marker's registration and the settle skill, and imports `rules` from the new file. No `check:` line under `docs/` names the old file.

**Lines outside `docs/`.** `skills/writing-style/SKILL.md` line 268 reads `check: tests/test_rules.py tests/test_rule_changes.py tests/test_censuses.py tests/test_the_agent_contract_holds_the_universal_rules.py`, as `spec.md` assigns, and `tests/test_a_language_section_of_writing_style_opens_alone.py#WRITING_RULE_CHECKS` says the same. `tests/test_docs_line_wrap.py#WIDE_TARGET` spells the old file's name as a fixture string of a wide line, and stands.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_the_rules_command_reads_each_rule_off_its_test.py --to tests/test_rules.py tests/test_the_rules_command_reads_each_rule_off_its_test.py`, HEAD at 565de415, ends `test-layout: moved: 22 old cases, 61 items against 61 at 565de4152a2c, 0 failed`, exit 0. No mutants run; `--pairs` names none.

**Cases and seconds** (`executed`, serial): 61 items in 0.71 s before, in an archive of 565de415; 62 in 0.75 s after.

**The boundary** (`executed`). At the tree committed as 56a8ac20, before the commit over the same bytes: the two files, the writing-style pin, `tests/test_docs_line_wrap.py`, the agent contract's file, `tests/test_the_rules_have_one_owner.py`, `tests/test_a_moved_rule_leaves_its_definition.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 30 files: 2,861 passed and 3 skipped. `--check` (172 files, 0 refused), `bin/rules --check` (249 check lines) and `bin/unverified-check seal/specs/` exit 0; ruff clean.

### Batch B, `.github/scripts/`, group 42, at 5e26a264

**The module.** `.github/scripts/release_completeness_check.py`, whose 20 cases of its functions were in `tests/test_a_release_cannot_ship_an_untrue_milestone.py`, now `tests/test_release_completeness_check.py`: nine of `judge` in `Test_judge`, ten that run `main` over the fake tracker in `Test_main`, and the case that reads the source for a write in `Test_module`. The old file keeps the four cases that read the hygiene workflow's step and `test_the_script_and_this_file_draw_the_input_boundary_the_same_way`, which reads the module docstring beside a staying case's own docstring in `__file__`, so it cannot leave that file. `seal/follow-up.md`'s row on folded-source readers names `tests/test_release_completeness_check.py#Test_module::test_the_gate_writes_nothing` where it stands now.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_a_release_cannot_ship_an_untrue_milestone.py --to tests/test_release_completeness_check.py tests/test_a_release_cannot_ship_an_untrue_milestone.py`, HEAD at 56a8ac20, ends `test-layout: moved: 25 old cases, 30 items against 30 at 56a8ac20bf30, 0 failed`, exit 0. No mutants run; `--pairs` names none.

**Cases and seconds** (`executed`, serial): 30 items in 0.14 s before; 31 in 0.10 s after.

**The boundary** (`executed`). At the tree committed as 5e26a264, before the commit over the same bytes: the two files, `tests/test_the_release_check_watches_what_ships.py`, which cites a staying case, `tests/test_a_merged_ticket_says_so_on_the_tracker.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 26 files: 2,497 passed and 3 skipped. `--check` (173 files, 0 refused), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

### Batch B, `.github/scripts/`, group 43, at 0cc2609c

**The module.** `.github/scripts/plugin_directory_check.py`, whose twelve cases were the whole of `tests/test_the_plugin_directory_answers_the_box.py`, now `tests/test_plugin_directory_check.py`: five of `line` in `Test_line`, four that run `main` in `Test_main`, and the ancestry, name and manifest path cases in `Test_module`. No `check:` line names the old file, so it went. The new file's docstring keeps the old one's citation of `CONTRIBUTING.md` *House rules*, *No real identifiers*, and `tests/test_the_rules_claude_md_names_have_one_home.py#LINKED` and `#CARRIERS` name the new file in its place. `tests/test_the_release_tail_does_not_end_at_the_tag.py` reads the release checklist and the release-tail rule, and stays.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_the_plugin_directory_answers_the_box.py --to tests/test_plugin_directory_check.py`, HEAD at 5e26a264, ends `test-layout: moved: 12 old cases, 17 items against 17 at 5e26a264b9d6, 0 failed`, exit 0. No mutants run. `--pairs` names one pair in `Test_main`: two cases call `main` with `--root` over different stubs of `fetch`, one asserting the plugin and the two files named, the other that nothing claims a listing and the closing names both pages; neither covers the other, so none is merged.

**Cases and seconds** (`executed`, serial): 17 items in 0.26 s before; 18 in 0.26 s after.

**The real-git cases kept.** `Test_module::test_a_commit_this_clone_does_not_have_is_not_called_unreachable` builds a repository, because the ancestry is git's answer.

**The boundary** (`executed`). At the tree committed as 0cc2609c, before the commit over the same bytes: the new file, the identifiers file, the release tail file, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 26 files: 2,475 passed and 3 skipped. `--check` (173 files, 0 refused, 116 declaring no `TARGET`), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

### Batch B, `.github/scripts/`, group 44, at 222bf69a

**The module.** `.github/scripts/roll_flow_measurement_issue.py`, whose 31 cases of its functions were in `tests/test_a_release_rolls_the_flow_measurement_issue.py`, now `tests/test_roll_flow_measurement_issue.py`: 23 that drive `main` in `Test_main`, `rolled_from`'s two in `Test_rolled_from`, `find_baseline_issue`'s two in `Test_find_baseline_issue`, and the body, version, close comment and list call cases in `Test_module`. The old file keeps the four cases that read `docs/issues-and-milestones.md` against the script's constants, which hold the rule of its line 179 as `spec.md` says, and loads the script through the new file's `_roller`. The docstrings of `tests/test_a_merged_ticket_says_so_on_the_tracker.py` and `tests/test_session_cost.py#_cost` name the new file.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_a_release_rolls_the_flow_measurement_issue.py --to tests/test_roll_flow_measurement_issue.py tests/test_a_release_rolls_the_flow_measurement_issue.py`, HEAD at 0cc2609c, ends `test-layout: moved: 35 old cases, 35 items against 35 at 0cc2609cad5a, 2 failed`, exit 1. The two lines are one case, `test_one_open_issue_closes_it_and_opens_the_next`, and its new form: its body defines `fake_try_run` with a docstring of three lines, and the formatter the edit hook runs re-indents a docstring's continuation lines to its new depth, so the string the check compares changed by four spaces a line (`executed`, the two ASTs diffed). The check drops a case's own docstring and keeps a nested function's, so no moved case holding a nested function with a wrapped docstring can pass it. That is a limit of the check, left to the framer in `overview.md`, and the module runs its mutants. `--pairs` names one pair in `Test_find_baseline_issue`, `test_accepts_one_open_log_and_answers_none_where_there_is_none` and `test_refuses_to_guess_between_two_open_durable_logs`, which call `find_baseline_issue("example/repo")` with equal arguments over different answers of the `try_run` each case stands in. Neither covers the other: the first asserts no number and no note where the lookup fails, finds nothing or reads no JSON, and the number where one log is open; the second asserts no number and a note naming `flow-baseline` where two are open. So neither is merged (written in round 3's fix pass).

**The mutation table** (`executed`, one `bin/mutation-check` batch over `.github/scripts/roll_flow_measurement_issue.py` with `--tests "bin/test tests/test_roll_flow_measurement_issue.py -q -p no:xdist -x"`, at the tree committed as 222bf69a; the old column in an archive of 0cc2609c against the old file, run with the worktree's `.venv`). 38 mutants, r1 to r38, at the decision points of `run`, `try_run`, `log_title`, `rolled_from`, `roll_is_due`, `read_version`, `list_open_issues`, `comment_count`, `open_flow_measurement_issues`, `close_issue`, `find_baseline_issue`, `issue_body`, `create_args`, `landed_create`, `open_issue` and `main`: 34 red and 4 survived, in 21.5 s after a 3.3 s baseline; the old column ran the 4 in 0.7 s, and each survived there too.

| # | Mutation | New file | Old file |
|---|---|---|---|
| r3, r5 to r17, r19 to r38 | the title written without its prefix; a version read with its trailing space, or an empty one as a version; due read as unreadable only; a fixed version read; the list asked without comments; a missing count read as zero; the retry with no sleep, or on two open; an empty-log sentence on an unread count; the close comment promising the next version; the lookup's empty, unparsed or two-open answer not guarded; the baseline clause kept with no log; the empty-log note on an unread count; the notes dropped from the body; the lookup label dropped from the create; the issue `main` closed counted as landed; the landed guard with no sleep or no retry; the baseline note dropped; a failed create read as landed on an empty answer; the guard skipped; the milestone note dropped on the last rung; two open read as one; the condition skipped; the nothing-due, unread-count, recovery and rolled lines losing what they name | red | not run |
| r1 | `run` does not exit on a failed call | SURVIVED | SURVIVED |
| r2 | `try_run` answers a failed call's output | SURVIVED | SURVIVED |
| r4 | `rolled_from` takes the prefix anywhere in the title | SURVIVED | SURVIVED |
| r18 | `find_baseline_issue` names the last open log, not the first | SURVIVED | SURVIVED |

Every survivor is an old gap. r18 no input tells apart: more than one open log returns before that line, so the list it reads holds one. For the others no case runs `run` or `try_run` themselves, which every case replaces, or reads a title that carries the whole prefix after other text. No case was added.

**Cases and seconds** (`executed`, serial): 35 items in 0.07 s before, in an archive of 0cc2609c; 36 in 0.07 s after.

**The real-git cases kept.** None: no case runs git or `gh`.

**The boundary** (`executed`). At the tree committed as 222bf69a, before the commit over the same bytes: the two files, the two whose docstrings changed, `tests/test_a_segment_feeds_the_flow_log.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 28 files: 2,759 passed and 3 skipped. `--check` (174 files, 0 refused, 116 declaring no `TARGET`), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

**Phase 4's survivors.** None of h2, h12 and h23 is reached by groups 40 to 44 (`read`).

### The thirteenth spawn

**What this spawn was asked.** The rest of `.github/scripts/`: `close_issues_on_release.py`, `label_merged_on_release_branch.py` and `tracker_labels.py` as one group, because three old files each define a fake `Tracker` of their own; then `durations_union.py`, `gather_changelog.py`, `publish_release_note.py`, `release_seal.py` and `run_tests.py`; then `evals/scripts/`; then phase 6's close, with phase 4's h2, h12 and h23 stated as re-run or unreached.

**Whether the frame holds** (`read`). It holds for `.github/scripts/`. Every `check:` line naming an old file the remaining groups draw from has an item in `spec.md` *Rule changes* or a row in *The check lines the remaining groups meet*: `docs/issues-and-milestones.md` lines 249 and 286 and `docs/branch-and-release.md` line 315 for the closer and the signal, `docs/release-checklist.md` line 69 and `docs/the-record-layout.md` lines 46 and 268 for the gatherer, the three lines of `docs/the-broad-gate.md` *What the runner owes the person who typed it* for the runner, and `docs/branch-and-release.md` line 94, which keeps its files. No `check:` line names `tests/test_a_declared_label_reaches_the_tracker.py` or `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`. Every old file of the directory prices under 60 s, so the cases are placed.

### Batch B, `.github/scripts/`, group 45, at efc3a79f

**The modules.** `close_issues_on_release.py`, `label_merged_on_release_branch.py` and `tracker_labels.py`, whose cases sat in `tests/test_a_declared_label_reaches_the_tracker.py`, `tests/test_a_merged_ticket_says_so_on_the_tracker.py`, `tests/test_the_closer_carries_on_past_a_refusal.py` and `tests/test_release_hygiene.py`.

**The cases.** 58 of the 94 old cases, into three new files:

- `tests/test_close_issues_on_release.py`: the keyword reader's six from the hygiene file in `Test_keywords_in`; in `Test_main`, the label file's eight that drive `main`, the refusal file's eight and the hygiene file's three; in `Test_module`, the removal-report case, the `attempt` case, the fallback's comment case and the hygiene file's argv case. Renamed: `test_accepts_only_a_keyword_before_a_number`, `test_refuses_a_keyword_inside_a_tilde_fence`, `test_accepts_the_issue_the_keyword_named_and_closes_nothing_else`, `test_refuses_a_close_both_routes_refuse_and_names_it_at_the_end`.
- `tests/test_tracker_labels.py`: the reconcile step's three `main` cases in `Test_main` and the cap case in `Test_module`. Renamed: `test_accepts_a_missing_label_and_creates_it_with_the_documents_sentence`, `test_refuses_to_write_under_check_and_reports_what_is_missing`.
- `tests/test_label_merged_on_release_branch.py`: the signal's sixteen, two in `Test_version_of`, eleven in `Test_main` and three in `Test_module`, and the label file's reader case in `Test_module`. Renamed: `test_accepts_a_release_branch_and_names_its_milestone_and_label`, `test_refuses_a_branch_that_is_not_a_release`, `test_accepts_the_issue_the_keyword_named_and_labels_nothing_else`, `test_refuses_a_non_release_branch_and_writes_nothing`.

The label file's `Tracker` and `load` live in the closer's file, and the two other new files import them. The refusal file's fake is `RefusingTracker` beside it, so its eight cases read the new name; the closer's two loaders are one, `closer_module`, beside the hygiene file's `_closer`.

**Left where they stand**, for #923: the label file's five cases that read the workflow, `docs/issues-and-milestones.md` and the documents its labels cite; the merged-ticket file's three that read its workflow; the hygiene file's token case, which reads the closer's workflow. The refusal file holds no case and stays, because `docs/branch-and-release.md` line 315 names it until the settle.

**The merge.** Placed in `Test_keywords_in`, the hygiene file's four-space and HTML comment cases gave `--pairs` one pair, equal bodies once strings are normalised. They are one parametrized case, `test_accepts_a_shape_left_unmasked_as_a_claim`, with each old docstring's reason as a comment above its row; the closer's comment above `FENCE` and `SPAN` says each shape has a row there. `--pairs` also names `tests/test_tracker_labels.py::Test_main`'s two `main(["--apply"])` cases, over different trackers: one asserts a create, the other that nothing is written, so neither covers the other and neither is merged.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_a_declared_label_reaches_the_tracker.py tests/test_a_merged_ticket_says_so_on_the_tracker.py tests/test_the_closer_carries_on_past_a_refusal.py tests/test_release_hygiene.py --to tests/test_close_issues_on_release.py tests/test_tracker_labels.py tests/test_label_merged_on_release_branch.py tests/test_a_declared_label_reaches_the_tracker.py tests/test_a_merged_ticket_says_so_on_the_tracker.py tests/test_the_closer_carries_on_past_a_refusal.py tests/test_release_hygiene.py`, HEAD at bc2b976f, ends `test-layout: moved: 94 old cases, 102 items against 102 at bc2b976ffa97, 21 failed`, exit 1. The 21 lines are three kinds, each an old case and its new form: the refusal file's eight cases, whose bodies name `RefusingTracker`; its fallback-comment case, whose message names the argv case where it named the hygiene file; and the two merged cases with the case they became.

**The mutation table** (`executed`, one `bin/mutation-check` batch per module at the tree committed as efc3a79f, `--tests "bin/test <its new file> -q -p no:xdist -x"`; the old column in an archive of bc2b976f with the worktree's `.venv`, against the old files each module's cases came from).

`close_issues_on_release.py`: 46 mutants, c1 to c46, at the decision points of `keywords_in` and its four patterns, `run`, `attempt`, `gh_json`, `_issue_api`, `issue_state`, `comments_on`, `issue_labels`, `drop_label`, `spend_label`, `closing_comment`, `close_issue`, `pull_request_body`, `arrived` and `main`: 34 red and 12 survived, after a 5.0 s baseline; the old column ran the 12 against the label file, the refusal file and the hygiene file's ten closer cases, and each survived there too.

| # | Mutation | New file | Old files |
|---|---|---|---|
| c1 to c9, c11, c12, c17, c19 to c27, c29, c31, c34, c37 to c46 | a fence or a span left unmasked; a number with no keyword claimed; the keywords read case-sensitively; a merged number read mid-subject; the tilde fence, the indented fence or the fence's own closing delimiter dropped; the double-backtick span dropped; `attempt` inverted or unstripped; the comment count never read; an issue's labels read as none; a refused removal unreported, a removal reported as failed, the dry arm or the report's guard dropped; the closing comment's pull request dropped; the first route taken as closing, a refused PATCH unreported, a landed comment taken as missing, the posted comment's body changed; a pull request read with no body; every subject dropped; a missing issue closed; any label taken as spent; an already-closed issue closed again; the closed arm's removal dropped; the dry run closing; a refused close unreported; the closed issue's removal dropped; the failures not raised; the re-run's `REPO` dropped; `DRY_RUN` ignored | red | not run |
| c10 | `run` does not exit on a failed call | SURVIVED | SURVIVED |
| c13 | `gh_json` answers the text, not its JSON | SURVIVED | SURVIVED |
| c14 | `_issue_api` exits on a 404 | SURVIVED | SURVIVED |
| c15 | `issue_state` answers `open` for every issue that exists | SURVIVED | SURVIVED |
| c16 | `comments_on` answers 0 where the read gave no count | SURVIVED | SURVIVED |
| c18 | `issue_labels` reads a missing issue's data | SURVIVED | SURVIVED |
| c28 | `close_issue` takes a count it could not read as 0 | SURVIVED | SURVIVED |
| c30 | `pull_request_body` answers an issue's body as a pull request's | SURVIVED | SURVIVED |
| c32 | `arrived` reads a range from an all-zero `before` | SURVIVED | SURVIVED |
| c33 | `arrived` reads the tip, not the range | SURVIVED | SURVIVED |
| c35 | `main` reads keywords from a number that is no pull request | SURVIVED | SURVIVED |
| c36 | the last pull request to claim an issue is named, not the first | SURVIVED | SURVIVED |

`label_merged_on_release_branch.py`: 22 mutants, m1 to m22: 19 red and 3 survived; the old column ran the 3 against the merged-ticket file and the label file's reader case, and each survived there too.

| # | Mutation | New file | Old files |
|---|---|---|---|
| m1 to m5, m7, m8, m10, m12 to m22 | the branch pattern's end anchor dropped; no version read as empty; the milestone, label or description spelled without its branch; the issue's labels or the existing labels read as none; the description dropped from the create; the add written as a remove; a number that is no pull request read; the issue and its pull request swapped; a non-release branch labelled; nothing claimed and the label created; an existing label created again; the dry run creating, labelling a missing issue, labelling again or writing; `DRY_RUN` ignored | red | not run |
| m6 | `LABEL_DESCRIPTION_LIMIT` is 1000 | SURVIVED | SURVIVED |
| m9 | the label list is read 30 at a time | SURVIVED | SURVIVED |
| m11 | the label is created in another colour | SURVIVED | SURVIVED |

`tracker_labels.py`: 9 mutants, t1 to t9: 7 red and 2 survived; the old column ran the 2 against the label file, and each survived there too.

| # | Mutation | New file | Old files |
|---|---|---|---|
| t1 to t3, t5, t7 to t9 | nothing declared; the present labels taken as missing; the description dropped from the create; the complete tracker not said; `--check` creating; `--check`'s pointer to `--apply` dropped; every run read as dry | red | not run |
| t4 | the label is created in another colour | SURVIVED | SURVIVED |
| t6 | `DRY_RUN` creates | SURVIVED | SURVIVED |

Every survivor is an old gap. Five no case can reach, because every case replaces the function or nothing calls it: `run` (c10) and `arrived` (c32, c33) are faked in every case, `_issue_api` (c14) in every case that reaches it, and `gh_json` (c13) has no caller in the tree (`executed`, `git grep gh_json -- .github`). For the others no case has a closed issue read through the real `issue_state` and asserted not closed again (c15), a comment count unreadable before the first route and readable after it (c16, c28), a missing issue read through the closer's own `issue_labels` (c18), a subject number that names an issue reaching the real `pull_request_body` (c30, c35), two pull requests claiming one issue (c36), a description held to the cap's value (m6), a tracker of more than 30 labels (m9), an asserted colour (m11, t4), or `tracker_labels.py` run under `DRY_RUN` (t6). No case was added.

**Cases and seconds** (`executed`, serial): 66 items in 0.08 s before, the three tracker files and the hygiene file's ten closer cases in an archive of bc2b976f; 69 in 0.12 s after over the three new files and the three old ones, the three census items among them.

**The real-git cases kept.** None: no case runs git or `gh`.

**Lines rewritten.** The closer's comment above `FENCE` and `SPAN`, `seal/follow-up.md`'s row on folded-source readers, and the docstrings of `tests/test_roll_flow_measurement_issue.py` (`_roller` and the round trip's case) and `tests/test_a_release_publishes_its_note.py` name the files that hold the cases.

**The boundary** (`executed`). At the tree committed as efc3a79f, before the commit over the same bytes: the seven files, the roll file, the note file, `tests/test_issue_claims_check.py`, `tests/test_the_changelog_is_gathered_at_release.py`, every file reading `seal/follow-up.md`, `tests/test_every_reader_ends_a_line_where_gfm_does.py`, `tests/test_docs_line_wrap.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 40 files: 3,153 passed and 3 skipped in 27.4 s. `bin/test-layout --check` exits 0, 177 files read, 0 refused, 116 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats each changed Python file clean.

### Batch B, `.github/scripts/`, group 46, at b68d41d1

**The module.** `.github/scripts/durations_union.py`, whose six cases were in `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, now `tests/test_durations_union.py` with the fixture parts and their two helpers: five that run `main` in `Test_main`, renamed `test_accepts_the_parts_and_writes_their_union_sorted_with_lf` and `test_refuses_a_missing_part_a_duplicate_id_or_an_unparseable_part`, and the report's empty-committed-file case in `Test_module`. The old file keeps the cases that read the workflow, the durations file and the documents, and conftest's `posix_id` case, and its docstring names the new file.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py --to tests/test_durations_union.py tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, HEAD at efc3a79f, ends `test-layout: moved: 24 old cases, 33 items against 33 at efc3a79f8793, 0 failed`, exit 0. No mutants run; `--pairs` names none.

**Cases and seconds** (`executed`, serial): 33 items in 0.11 s before, in an archive of bc2b976f; 34 in 0.13 s after.

**The real-git cases kept.** None: the union reads fixture parts on disk.

**The boundary** (`executed`). At the tree committed as b68d41d1, before the commit over the same bytes: the two files, `tests/test_ci_gives_the_checks_what_they_need.py`, which the old file imports, `tests/test_release_report.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 26 files: 2,502 passed and 5 skipped. `--check` (178 files, 0 refused), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

### Batch B, `.github/scripts/`, group 47, at 503e2f5e

**The module.** `.github/scripts/gather_changelog.py`, whose 33 cases were in `tests/test_the_changelog_is_gathered_at_release.py`, now `tests/test_gather_changelog.py` with the `tree` fixture and the layout helpers: 32 that run the script as a process in `Test_main`, renamed `test_accepts_every_fragment_into_the_released_section` and `test_refuses_a_release_with_nothing_to_gather`, and the index case that calls `indexed` in `Test_module`. The `second-gather-appends` marker moves with its case; `.github/scripts/rules.py#markers` reads a marker from any test file, so `docs/release-checklist.md` line 76 stands as `spec.md` says. The old file keeps the nine cases that read the workflow, the documents, this repository's changelog and records, and conftest's `gathered_entry`. `tests/test_release_hygiene.py`'s docstring names the file that checks the order of the sections.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_the_changelog_is_gathered_at_release.py --to tests/test_gather_changelog.py tests/test_the_changelog_is_gathered_at_release.py`, HEAD at b68d41d1, ends `test-layout: moved: 42 old cases, 52 items against 52 at b68d41d1caa8, 0 failed`, exit 0. No mutants run; `--pairs` names none.

**Cases and seconds** (`executed`, serial): 52 items in 1.35 s before, in an archive of bc2b976f; 53 in 1.41 s after.

**The real-git cases kept.** None: the gather reads and writes files under a temporary root.

**The boundary** (`executed`). At the tree committed as 503e2f5e, before the commit over the same bytes: the two files, the hygiene file, the files naming the gatherer (`tests/test_every_reader_ends_a_line_where_gfm_does.py`, `tests/test_first_setup_asks_once.py`, `tests/test_a_body_naming_two_issues_claims_one.py`, `tests/test_a_release_publishes_its_note.py`), the two rules files, `tests/test_a_workflow_is_read_the_one_way.py`, `tests/test_docs_line_wrap.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 31 files: 2,650 passed and 3 skipped. `--check` (179 files, 0 refused), `bin/rules --check` (249 check lines) and `bin/unverified-check seal/specs/` exit 0; ruff clean.

**Phase 4's survivors.** Group 45's moved cases call `read`, so h2 was re-run against `tests/test_close_issues_on_release.py` and `tests/test_label_merged_on_release_branch.py` with one `bin/mutation-check` call at the tree committed as 503e2f5e, and it survives, an old gap (`executed`): every call passes an absolute path, and `bin/test` runs from the root, so the root join changes no path. h12 and h23 are not reached by groups 45 to 47: no moved case calls `imported_roots` or `repo_relative` (`read`).

### Batch B, `.github/scripts/`, group 48, at f7ef43cc

**The modules.** `publish_release_note.py` and `release_seal.py`, one group because their cases share `tests/test_a_release_publishes_its_note.py` and `tests/test_the_release_seal_is_drawn.py`.

**The cases.** 41 of the 47 old cases, into two new files:

- `tests/test_publish_release_note.py`: the note file's 14 that run `main` in `Test_main`, renamed `test_accepts_the_gathered_section_as_the_release_note` and `test_refuses_a_tag_with_no_changelog_section`, and in `Test_module` the title pattern's bound, the branch list's call, the glance block and the gatherer seam.
- `tests/test_release_seal.py`: the seal file's 23, three in `Test_release_rows`, three in `Test_suite_counts`, eight in `Test_chain_counts`, four that run `main` in `Test_main`, and in `Test_module` the two pixel cases, the load with Pillow blocked, the alt text and the `gh` and `tagged` calls. Renamed: `test_accepts_the_fixed_set_of_rows_in_order_and_fits_the_panel`, `test_refuses_to_count_a_chain_count_nobody_could_read`, `test_accepts_the_record_and_reads_it_through_the_gates_reader`, `test_refuses_a_record_that_cannot_vouch_for_the_counts`, `test_accepts_a_tree_and_counts_items_rounds_capped_and_deferred`, `test_refuses_to_count_a_tree_whose_records_are_not_there`, `test_accepts_a_published_note_and_replaces_its_glance_table`, `test_refuses_on_any_failure_and_leaves_the_note_as_published`. `draw` has no class: its two cases assert what it paints and have no refusing partner, so both are in `Test_module`.

The emoji the note's headings and glance rows carry are spelled as Python escapes in the moved assertions, so each string constant is the one it was and the move check compares them equal; the round findings' markers in docstrings and comments are words.

**Left where they stand**, for #923: the note file's checklist title case and its two workflow cases, which load the script through the new file's `module`; the seal file's install-pin case and its two document cases. `docs/branch-and-release.md` line 94 names both old files and keeps them, as `spec.md` says; `overview.md` asks the framer whether it should name the new files too.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_a_release_publishes_its_note.py tests/test_the_release_seal_is_drawn.py --to tests/test_publish_release_note.py tests/test_release_seal.py tests/test_a_release_publishes_its_note.py tests/test_the_release_seal_is_drawn.py`, HEAD at 503e2f5e, ends `test-layout: moved: 47 old cases, 80 items against 80 at 503e2f5e32f4, 0 failed`, exit 0. No mutants run; `--pairs` names none in the two new files.

**Cases and seconds** (`executed`, serial): 80 items in 3.85 s before, in an archive of bc2b976f; 82 in 3.65 s after.

**The real-git cases kept.** None: the seal's `tree` builds a work item's records on disk, and `gh` and `git` are stood in for.

**Lines rewritten.** `publish_release_note.py`'s comment on the section heading names the seam case where it stands now.

**The boundary** (`executed`). At the tree committed as f7ef43cc, before the commit over the same bytes: the four files, `tests/test_gather_changelog.py`, `tests/test_the_gate_names_every_step_ci_runs.py`, `tests/test_the_release_tail_does_not_end_at_the_tag.py`, `tests/test_seal_stamp.py`, the hygiene file, `tests/test_ci_gives_the_checks_what_they_need.py`, `tests/test_docs_line_wrap.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 32 files: 2,757 passed and 3 skipped. `--check` (181 files, 0 refused), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

### Batch B, `.github/scripts/`, group 49, at a4a113f6

**The module.** `.github/scripts/run_tests.py`, whose 36 cases of its functions were in `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`, now `tests/test_run_tests.py` with the fake environment, the recorder and the stand-in interpreter: ten of `ensure`, two of `hide_from_git`, five of `build`, 18 that run `main`, and the repository root case in `Test_module`. Renamed: `test_accepts_a_built_environment_and_never_rebuilds_it`, `test_refuses_an_environment_below_the_floor`, `test_accepts_a_built_environment_and_hides_it_from_git`, `test_refuses_to_overwrite_an_existing_ignore`, `test_accepts_a_fresh_build_and_installs_xdist_beside_pytest`, `test_refuses_a_machine_with_neither_tool_and_names_what_to_install`, `test_accepts_the_callers_arguments_and_passes_them_through`, `test_refuses_a_tree_without_a_suite_in_a_sentence`. The old file keeps the 24 cases that read the `bin/` wrappers, the workflows, `CONTRIBUTING.md`, the handoff protocol, the agent definitions and the runner's own prose, and reads the runner through the new file's `rt`. `docs/the-broad-gate.md`'s three lines move to the new file through `spec.md`'s items; `agents/smith.md` line 142 and `agents/warden.md` line 162 keep the old file, as `spec.md` says.

**The pairs.** `--pairs` names 120 pairs in `Test_main`, every one two of the 16 cases that call `main([])`. Each case builds a different world on disk with `fake_venv`, or stands in a different `subprocess.run`, and asserts a different line or call, so none covers another and none is merged; the report compares the literal `[]` and cannot see the input that differs.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_the_suite_has_a_command_that_is_cheap_twice.py --to tests/test_run_tests.py tests/test_the_suite_has_a_command_that_is_cheap_twice.py`, HEAD at f7ef43cc, ends `test-layout: moved: 60 old cases, 95 items against 95 at f7ef43ccac39, 0 failed`, exit 0. No mutants run.

**Cases and seconds** (`executed`, serial): 95 items in 0.86 s before, in an archive of bc2b976f; 96 in 0.67 s after.

**The real-git cases kept.** The six that `git init` a directory and read `git status`, because what they hold is whether git sees the virtualenv.

**The boundary** (`executed`). At the tree committed as a4a113f6, before the commit over the same bytes: the two files, `tests/test_arm_check.py`, `tests/test_launch.py`, the note and seal files, the hygiene file, `tests/test_ci_gives_the_checks_what_they_need.py`, `tests/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/test_rules.py`, `tests/test_docs_line_wrap.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 31 files: 2,729 passed and 5 skipped. `--check` (182 files, 0 refused), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

**Phase 4's survivors.** Groups 48 and 49 call no conftest helper that h2, h12 or h23 breaks: the moved cases load modules with `load_module` and read files with `open` (`read`).

`.github/scripts/` is done: each of its 14 modules has its rule 1 file (`executed`, one `TARGET` line per module's file).

### Batch B, `evals/scripts/`, group 50, at 52ce0e03

**The modules.** `replay_targets.py`, `rule_cases.py` and `seed_defects.py`, whose 25 cases were what phase 5 left in `tests/test_a_rewritten_definition_proved_non_inferior.py`. `noninferiority.py` has its file from phase 5. `behaviour.py` has no case of its own: every case reaches it through `tests/test_noninferiority.py`, which loads it to write graders for the reader under test, or through a generator (`read`).

**Rule 3** (`executed`). `.test_durations` prices the old file at 62.0 s, but 58.1 s of that is ids phase 5 moved to `tests/test_noninferiority.py`, which phase 7 prunes (`overview.md`, the first divergence); the 28 priced ids of its 35 collected items sum to 3.9 s, and the file runs in 8.0 s serial. So the cases are placed.

**The cases.** Into three new files, bodies unchanged:

- `tests/test_replay_targets.py`: three in `Test_confirmed`, two in `Test_truth_pattern`, and six in `Test_module`, among them `test_a_named_case_is_read_at_every_release_tag`, whose rows run both generators through this module's tag reading. Renamed: `test_accepts_a_fixed_finding_the_next_round_confirmed`, `test_refuses_a_labelled_record_the_check_refuses`, `test_accepts_a_location_inside_its_line_window_and_no_further`, `test_refuses_a_coordinate_the_check_refuses`.
- `tests/test_rule_cases.py`: five that run `main` in `Test_main`. Renamed: `test_accepts_an_entry_and_adds_the_truth_its_case_is_written_with`, `test_refuses_an_entry_the_case_cannot_take`.
- `tests/test_seed_defects.py`: four in `Test_target_of` and five in `Test_module`, among them `test_the_replay_and_seeded_generators_read_the_entries_too`, which reads both generators' graders. Renamed: `test_accepts_a_shipped_commit_and_builds_its_case_on_round_1s_target`, `test_refuses_a_shipped_commit_whose_round_1_truths_share_a_line`.

`load_script` and the two labelled rounds live in the replay file, and `recurred_file`, `entry` and `truth_regex` in the rule file; the other files import them, in that order, so no import goes round. The old table's markers in the replay cases' records are spelled as Python escapes, so each string constant is the one it was.

**Left where it stands.** `test_no_two_truths_of_a_warden_case_accept_one_location`, which reads the committed warden cases under `evals/behaviour/`, a check over records; the old file keeps it and its pattern, and reads graders through the rule file's `truth_regex`. No `check:` line names the old file.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_a_rewritten_definition_proved_non_inferior.py --to tests/test_replay_targets.py tests/test_rule_cases.py tests/test_seed_defects.py tests/test_a_rewritten_definition_proved_non_inferior.py`, HEAD at f19395a5, ends `test-layout: moved: 26 old cases, 35 items against 35 at f19395a52bea, 0 failed`, exit 0. No mutants run; `--pairs` names none.

**Cases and seconds** (`executed`, serial): 35 items in 5.21 s before, in an archive of bc2b976f; 38 in 5.09 s after.

**The real-git cases kept.** The seeded cases build a shipped repository per case and run the scaffold against it, and the replay file's grammar case builds one, because what they hold is what git keeps and fetches.

**The boundary** (`executed`). At the tree committed as 52ce0e03, before the commit over the same bytes: the four files, `tests/test_noninferiority.py`, `tests/test_evals_layout.py`, `tests/test_the_sealer_guarantees.py`, `tests/test_chain_check.py`, the `git_listing` files, the censuses, `tests/test_test_layout.py`, `tests/test_conftest.py` and `tests/test_chain_hooks_hardening.py`. 30 files: 2,940 passed and 3 skipped. `--check` (185 files, 0 refused, 116 declaring no `TARGET`), `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff clean.

`evals/scripts/` is done.

### What phase 6 leaves

- `hooks/`: `hooks/githooks.py` and `hooks/hook-install.py` wait on Q10. `hooks/answer-clear.py` has a file whose `Test_module` holds its two round trips and no `Test_main`.
- `skills/verify/scripts/`, `skills/code-review/scripts/`, `skills/settle/scripts/` and `skills/implement/scripts/`: done, apart from the cases left for #923 and those that compare files with each other.
- `.github/scripts/`: done; groups 39 to 49 placed the cases of its fourteen modules.
- `evals/scripts/`: done; group 50 placed the three generators, `noninferiority.py` has its file from phase 5, and `behaviour.py` has no case of its own.
- Phase 4's survivors, all seven settled. h14 was re-run against the creation flow in group 7, h21 against the guard's file in group 12, h4 against the commit gate's file in group 14, h6 against `tests/test_config.py` in group 23, and h2 against the five rebuilt files that call `read` (`tests/test_broad_gate.py`, `tests/test_launch.py`, `tests/test_release_completeness_check.py`, `tests/test_close_issues_on_release.py` and `tests/test_label_merged_on_release_branch.py`), in two `bin/mutation-check` calls at 503e2f5e; each survives, an old gap (`executed`). h12 and h23 are not reached: no file that declares `TARGET` calls `tests/conftest.py#imported_roots` or `#repo_relative` (`executed`, `git grep` over `tests/`; `tests/test_unverified_check.py`'s `repo_relative` is the module's own). Groups 15 and 21 drew cases from h12's two files, and the cases that call `imported_roots`, which check what the oracles import, stayed with the oracles; h23's two files read the agent definitions and no group drew from them.

### The phase's close, at 52ce0e03

Batch B is placed. Every shipped module has its rule 1 file or a record of why it has none, except `hooks/githooks.py` and `hooks/hook-install.py`, whose cases stay in `tests/test_the_hooks_are_installed_where_git_runs_them.py` under `questions.md` Q10's default; `plan.md`'s Status cell for phase 6 holds 52ce0e03, the last group's commit.

The totals over groups 1 to 50 (`read`, each group's record; the seconds are the first figure each record states, serial, on a shared machine whose load moved the same tree's figure by up to three times): the groups' files held 7,803 pytest items before and 7,881 after, each parametrized row one item and each new file's census item in the after figure, in 462.6 s before and 421.8 s after. 31 groups passed the move check and ran no mutant, group 25 among them because its module's mutants ran in group 26. 18 failed it, each failure line read, and with group 13, written anew under rule 3 with no move check, those 19 groups ran 1,055 mutants over their modules in one batch per module, the commit gate's table counted in groups 14 and 17 and the worktree guard's in groups 12 and 26: 919 red and 136 survived. Of the 136, 125 are old gaps, the old files missing them too; 9 the old files kill through cases that did not move, so no case was added for them (group 14's 2 and group 23's 7); and 2 were answered by a case added and seen red on the mutant, both in group 8. Phase 6's first step, the move check itself, ran 33 more mutants in two batches, 32 red and 1 answered by a row.

What phase 6 leaves is in `overview.md`: the rows for the framer on the check lines that name too little, the move check's reading of nested docstrings, and the Windows and ubuntu legs of the files written since 1b0e7c23; the removed ids `.test_durations` still prices, for phase 7; and the undeclared files Q9 counts, among them the emptied files a `docs/` line names until the settle and the files whose cases read prose, for #923.

### The move checks re-run with the name condition

**What ran** (`executed`, macOS arm64, in round 3's fix pass). Each `bin/test-layout --moved` command this record holds for a group ran again: 49 commands, for groups 1 to 50 less group 13, which was written anew and has none. Each ran in a scratch clone of the branch, checked out at the commit the group's heading gives, the first of two where it gives two, with `HEAD` in a command read as the commit the record names beside it. Each ran twice there. The clone's own script at that commit reproduced every recorded last line word for word. Then `skills/verify/scripts/test_layout.py` as committed at 8dd97a30, which reads the names a moved case and its fixtures read (`spec.md` S15, `phases/phase-7.md` *S15, in round 3's fix pass*), was copied over the clone's and the command ran again. The first step's command at 6e7214be, `--moved HEAD --from tests/test_seal.py tests/test_seal.py`, is the one-new-file form the second step removed and no group's check, so it did not run. The two clones were removed after the runs.

A last line can differ in more than the failures added. Group 17's falls from 115 to 114: the script at 67a86c57 compared the docstring of a function `test_the_same_root_forms_answer_what_the_release_did` defines, and the script at 8dd97a30 drops it (S14), so the case's two body lines give way to one fixture line.

| Group | Commit | Recorded last line | With the name condition |
|---|---|---|---|
| 1 | 0a86c1b4 | `73 old cases, 74 items against 73 at 43324e4e104e, 17 failed`, exit 1 | `73 old cases, 74 items against 73 at 43324e4e104e, 23 failed`, exit 1 |
| 2 | ccca432d | `20 old cases, 147 items against 147 at 0a86c1b4c088, 0 failed`, exit 0 | `20 old cases, 147 items against 147 at 0a86c1b4c088, 4 failed`, exit 1 |
| 3 | e6700896 | `108 old cases, 119 items against 119 at ccca432d83a7, 3 failed`, exit 1 | `108 old cases, 119 items against 119 at ccca432d83a7, 6 failed`, exit 1 |
| 4 | 714f2df2 | `66 old cases, 180 items against 180 at e945c57c16fc, 4 failed`, exit 1 | `66 old cases, 180 items against 180 at e945c57c16fc, 4 failed`, exit 1 |
| 5 | 04115ed2 | `17 old cases, 37 items against 37 at 714f2df2eff1, 0 failed`, exit 0 | `17 old cases, 37 items against 37 at 714f2df2eff1, 15 failed`, exit 1 |
| 6 | df48707c | `18 old cases, 28 items against 28 at 04115ed2da4d, 0 failed`, exit 0 | `18 old cases, 28 items against 28 at 04115ed2da4d, 9 failed`, exit 1 |
| 7 | 9c70ddbf | `51 old cases, 59 items against 59 at 5639d076e5d3, 2 failed`, exit 1 | `51 old cases, 59 items against 59 at 5639d076e5d3, 19 failed`, exit 1 |
| 8 | 4f50aee0 | `51 old cases, 69 items against 70 at 459d7944c0d4, 4 failed`, exit 1 | `51 old cases, 69 items against 70 at 459d7944c0d4, 21 failed`, exit 1 |
| 9 | d8bba633 | `24 old cases, 24 items against 24 at 8dedf9e4698c, 3 failed`, exit 1 | `24 old cases, 24 items against 24 at 8dedf9e4698c, 17 failed`, exit 1 |
| 10 | 449feefb | `46 old cases, 47 items against 47 at 9197c897c376, 6 failed`, exit 1 | `46 old cases, 47 items against 47 at 9197c897c376, 6 failed`, exit 1 |
| 11 | e94c6826 | `100 old cases, 165 items against 165 at 167950a6e8bb, 0 failed`, exit 0 | `100 old cases, 165 items against 165 at 167950a6e8bb, 5 failed`, exit 1 |
| 12 | c512b123 | `219 old cases, 358 items against 358 at 56fb82e0646c, 123 failed`, exit 1 | `219 old cases, 358 items against 358 at 56fb82e0646c, 123 failed`, exit 1 |
| 14 | f5185d67 | `144 old cases, 187 items against 187 at 9818ee1a991f, 90 failed`, exit 1 | `144 old cases, 187 items against 187 at 9818ee1a991f, 102 failed`, exit 1 |
| 15 | f1d13be0 | `31 old cases, 142 items against 142 at 06d0f55453fc, 0 failed`, exit 0 | `31 old cases, 142 items against 142 at 06d0f55453fc, 6 failed`, exit 1 |
| 16 | b8e201e1 | `56 old cases, 71 items against 71 at 0b134a29b35e, 0 failed`, exit 0 | `56 old cases, 71 items against 71 at 0b134a29b35e, 3 failed`, exit 1 |
| 17 | 67a86c57 | `292 old cases, 409 items against 409 at b8e201e1f012, 115 failed`, exit 1 | `292 old cases, 409 items against 409 at b8e201e1f012, 114 failed`, exit 1 |
| 18 | 95991e42 | `27 old cases, 27 items against 27 at 67a86c5730f0, 0 failed`, exit 0 | `27 old cases, 27 items against 27 at 67a86c5730f0, 1 failed`, exit 1 |
| 19 | e1e39bf7 | `2 old cases, 19 items against 19 at 95991e42b3d5, 0 failed`, exit 0 | `2 old cases, 19 items against 19 at 95991e42b3d5, 2 failed`, exit 1 |
| 20 | 6277911e | `53 old cases, 55 items against 55 at e1e39bf7b23d, 0 failed`, exit 0 | `53 old cases, 55 items against 55 at e1e39bf7b23d, 2 failed`, exit 1 |
| 21 | 1b3e6978 | `193 old cases, 803 items against 803 at fb0c5dfccd2f, 0 failed`, exit 0 | `193 old cases, 803 items against 803 at fb0c5dfccd2f, 23 failed`, exit 1 |
| 22 | 10f6ad94 | `65 old cases, 190 items against 190 at 92add28be86b, 0 failed`, exit 0 | `65 old cases, 190 items against 190 at 92add28be86b, 5 failed`, exit 1 |
| 23 | ca726662 | `134 old cases, 333 items against 333 at c6c1d8b03de3, 7 failed`, exit 1 | `134 old cases, 333 items against 333 at c6c1d8b03de3, 79 failed`, exit 1 |
| 24 | 93bf39da | `4 old cases, 215 items against 215 at 687388b5ae85, 0 failed`, exit 0 | `4 old cases, 215 items against 215 at 687388b5ae85, 2 failed`, exit 1 |
| 25 | eb207a6d | `65 old cases, 661 items against 661 at 3cf118239946, 0 failed`, exit 0 | `65 old cases, 661 items against 661 at 3cf118239946, 21 failed`, exit 1 |
| 26 | da3eae09 | `367 old cases, 1189 items against 1189 at 0e561e86de7a, 26 failed`, exit 1 | `367 old cases, 1189 items against 1189 at 0e561e86de7a, 100 failed`, exit 1 |
| 27 | ffb0bd4b | `11 old cases, 11 items against 11 at 300abe340a60, 0 failed`, exit 0 | `11 old cases, 11 items against 11 at 300abe340a60, 0 failed`, exit 0 |
| 28 | b16613b3 | `40 old cases, 54 items against 54 at 6b884f5f9f41, 0 failed`, exit 0 | `40 old cases, 54 items against 54 at 6b884f5f9f41, 28 failed`, exit 1 |
| 29 | 31aed13b | `29 old cases, 50 items against 50 at 7cd34d46115a, 0 failed`, exit 0 | `29 old cases, 50 items against 50 at 7cd34d46115a, 1 failed`, exit 1 |
| 30 | 666cedbb | `24 old cases, 25 items against 25 at 2f2d21c97c4f, 0 failed`, exit 0 | `24 old cases, 25 items against 25 at 2f2d21c97c4f, 0 failed`, exit 0 |
| 31 | 391c7857 | `34 old cases, 46 items against 46 at 17ee85328290, 0 failed`, exit 0 | `34 old cases, 46 items against 46 at 17ee85328290, 0 failed`, exit 0 |
| 32 | bf6df24b | `63 old cases, 95 items against 95 at 6df0950bb66f, 0 failed`, exit 0 | `63 old cases, 95 items against 95 at 6df0950bb66f, 0 failed`, exit 0 |
| 33 | c9af3c38 | `194 old cases, 221 items against 221 at 95d02cc818d9, 8 failed`, exit 1 | `194 old cases, 221 items against 221 at 95d02cc818d9, 156 failed`, exit 1 |
| 34 | 5966150b | `198 old cases, 314 items against 315 at 10667b32ad71, 45 failed`, exit 1 | `198 old cases, 314 items against 315 at 10667b32ad71, 46 failed`, exit 1 |
| 35 | 2272cd1e | `171 old cases, 329 items against 329 at ffd898ec87dc, 0 failed`, exit 0 | `171 old cases, 329 items against 329 at ffd898ec87dc, 3 failed`, exit 1 |
| 36 | 19c01e3b | `116 old cases, 246 items against 246 at c30f7d9521c6, 8 failed`, exit 1 | `116 old cases, 246 items against 246 at c30f7d9521c6, 20 failed`, exit 1 |
| 37 | 809408e5 | `116 old cases, 174 items against 174 at db6541fc96b0, 0 failed`, exit 0 | `116 old cases, 174 items against 174 at db6541fc96b0, 77 failed`, exit 1 |
| 38 | 4f350b0f | `174 old cases, 330 items against 330 at 809408e5ec2e, 0 failed`, exit 0 | `174 old cases, 330 items against 330 at 809408e5ec2e, 0 failed`, exit 0 |
| 39 | 46e1ec4c | `38 old cases, 50 items against 50 at 4f350b0f9144, 17 failed`, exit 1 | `38 old cases, 50 items against 50 at 4f350b0f9144, 18 failed`, exit 1 |
| 40 | 565de415 | `9 old cases, 15 items against 15 at 409d8037ab94, 0 failed`, exit 0 | `9 old cases, 15 items against 15 at 409d8037ab94, 4 failed`, exit 1 |
| 41 | 56a8ac20 | `22 old cases, 61 items against 61 at 565de4152a2c, 0 failed`, exit 0 | `22 old cases, 61 items against 61 at 565de4152a2c, 1 failed`, exit 1 |
| 42 | 5e26a264 | `25 old cases, 30 items against 30 at 56a8ac20bf30, 0 failed`, exit 0 | `25 old cases, 30 items against 30 at 56a8ac20bf30, 0 failed`, exit 0 |
| 43 | 0cc2609c | `12 old cases, 17 items against 17 at 5e26a264b9d6, 0 failed`, exit 0 | `12 old cases, 17 items against 17 at 5e26a264b9d6, 0 failed`, exit 0 |
| 44 | 222bf69a | `35 old cases, 35 items against 35 at 0cc2609cad5a, 2 failed`, exit 1 | `35 old cases, 35 items against 35 at 0cc2609cad5a, 2 failed`, exit 1 |
| 45 | efc3a79f | `94 old cases, 102 items against 102 at bc2b976ffa97, 21 failed`, exit 1 | `94 old cases, 102 items against 102 at bc2b976ffa97, 36 failed`, exit 1 |
| 46 | b68d41d1 | `24 old cases, 33 items against 33 at efc3a79f8793, 0 failed`, exit 0 | `24 old cases, 33 items against 33 at efc3a79f8793, 0 failed`, exit 0 |
| 47 | 503e2f5e | `42 old cases, 52 items against 52 at b68d41d1caa8, 0 failed`, exit 0 | `42 old cases, 52 items against 52 at b68d41d1caa8, 0 failed`, exit 0 |
| 48 | f7ef43cc | `47 old cases, 80 items against 80 at 503e2f5e32f4, 0 failed`, exit 0 | `47 old cases, 80 items against 80 at 503e2f5e32f4, 2 failed`, exit 1 |
| 49 | a4a113f6 | `60 old cases, 95 items against 95 at f7ef43ccac39, 0 failed`, exit 0 | `60 old cases, 95 items against 95 at f7ef43ccac39, 5 failed`, exit 1 |
| 50 | 52ce0e03 | `26 old cases, 35 items against 35 at f19395a52bea, 0 failed`, exit 0 | `26 old cases, 35 items against 35 at f19395a52bea, 15 failed`, exit 1 |

Of the 49, 31 were recorded at exit 0: 9 still exit 0 (groups 27, 30, 31, 32, 38, 42, 43, 46 and 47) and 22 exit 1. The 18 recorded at exit 1 still exit 1, and each of their modules ran its mutants in the group's own record, so they run none again (`plan.md` *Round 3's fix pass*, step 3).

**The lines of the 22** (`executed`, each failure line read and each old case it names matched to the new case standing for it). Every line is on the name condition, so each group sends the modules whose new file, by its `TARGET`, holds a case a line names. Each name a line gives is a definition that differs between the two trees, most of them a module bound another way, by a loader's call given another name or path or by a loader in place of an import (`reader`, `answers`, `gate`, `wg`, `rules`, `settle`, `uc`), a helper changed as it moved into `tests/conftest.py` (`stub_process_tree`, `a_git_whose_diff_fails`, `git`, `shape_text`), a constant spelled another way (`ROOT`, `HERE`, `ITEM`), or a name a file now imports from another test file (`load_script`, `entry`, `TOKENS`). No difference is judged here; the mutants judge each module.

Seventeen of the named cases stand in a file that declares no `TARGET`, each a case the group left where it was and whose file the group changed around it: group 16's two in `tests/test_chain_hooks_hardening.py` (`a_git_whose_diff_fails`), group 19's `tests/test_the_old_spellings_reach_the_hook.py::test_the_three_token_reads_answer_as_one` (`_corpora`), group 22's `tests/test_the_mode_question_is_asked_once.py::test_the_writer_leaves_a_commented_row_alone` (`shape_text`), group 29's `tests/test_a_unit_is_bounded_where_a_parser_decides.py::test_a_quoted_line_resolves_in_any_file` (`RUBY`), group 35's `tests/test_one_heading_rule_holds_to_commonmark.py::test_every_tracked_markdown_file` (`disagreements`), group 37's `tests/test_settle_applies_rule_changes_in_place.py::test_the_skills_example_reads_as_the_skill_says` (`parse`) and `tests/test_settle_reads_before_it_removes.py::test_a_closed_row_is_told_to_merge_before_its_directory_goes` (`OVERVIEW_OPEN`), group 41's `tests/test_the_rules_command_reads_each_rule_off_its_test.py::test_the_slice_document_resolves_every_target` (`rules`), and group 50's `tests/test_a_rewritten_definition_proved_non_inferior.py::test_no_two_truths_of_a_warden_case_accept_one_location` (`truth_regex`), group 48's two in `tests/test_a_release_publishes_its_note.py` (`module`) and group 49's five in `tests/test_the_suite_has_a_command_that_is_cheap_twice.py` (`rt`). The plan's rule sends a module by its new file's `TARGET`, so these send none. Groups 29, 41, 48 and 49 have no other line, so they send no module; `overview.md` *Not verified* asks the framer whether a case of an undeclared file whose name changed is proved by anything.

**How the modules ran** (`executed`). Each module's decision-point mutants sit at the functions the cases a line names reach, as group 8 and group 36 placed theirs, because a function no named case reaches is read by cases that passed all four conditions. Each module ran one `bin/mutation-check` batch with `-x` at 208803e6 against its new file, the file its `TARGET` names. A survivor then ran against every new file of the failing group at the head, in a scratch clone at 208803e6, because a case of the module can stand in another module's new file. A mutant still surviving ran the old column, over the failing group's old files at the group's base. The runs of `skills/verify/scripts/mutation_check.py` used a copy of the runner outside the tree, so the mutated file never ran the batch. Four modules reuse an earlier table under `questions.md` Q11's default, each table run in a later group against a file that holds every case the failing group moved (`executed`, each case's name looked up in that file at that commit), and run the old column for that table's survivors. An id names a row of its module's table alone.

**Group 2, `hooks/one_heredoc.py`.** 13 mutants, o1 to o13, at `_match`'s banned bytes, one-line command, full match, missing terminator, `<<` count, newline-only suffix, sink suffix and first delimiter line, the delimiter, quoted and plain word patterns, the program suffix's newline and `reduce`'s answer: 11 red and 2 survived, in 490.8 s. o2, a command of one line read, and o10, a quoted word crossing a newline, survive the group's two new files at the head and the three old files at 0a86c1b4: old gaps.

**Group 5, `hooks/answers.py`, `hooks/answer-write.py`, `hooks/answer-clear.py`.**

| Module | Mutants | New file | The group's new files at the head | Old file at 714f2df2 |
|---|---|---|---|---|
| `hooks/answers.py` | 17, a1 to a17 | 14 red; a5, a9, a17 survived | a5, a9, a17 survived | a5, a9 survived, old gaps; a17 red |
| `hooks/answer-write.py` | 4, w1 to w4 | 3 red; w2 survived | w2 red | not run |
| `hooks/answer-clear.py` | 4, l1 to l4 | 3 red; l1 survived | l1 survived | l1 survived, an old gap |

The mutants sit at `_part`'s dot names, `call_id`'s two sources, `directory` and `_call_dir`'s empty parts, `clear`, `_prune`'s two ways, `write`'s token and command, `given`'s two age bounds, its argv read, its match and the escapes, and `root_dir`'s override; at the writer's tool test, call id, tokens and session; at the clearer's tool test, call id, command and session. a5 is a call directory for no call, a9 a call with no token written, l1 another tool cleared. w2, the payload's id not used, is red on `tests/test_answer_clear.py::Test_module::test_the_gates_write_before_the_call_and_clear_after_it`, which writes through the writer before it clears.

a17 is a lost protection. `root_dir` not reading `SPECSEAL_ANSWERS` was red on the old file's `test_a_payload_with_no_tool_use_id_is_keyed_by_its_command` at 714f2df2, through the answers the store under the home directory held, and no case at the head kills it. 56d2f856 adds `tests/test_answers.py::Test_module::test_the_override_names_the_store_where_it_is_set`, seen red on a17 and green as committed (`executed`, in a scratch clone at 56d2f856 with the runner copy). Under a17 the hooks write to the store under the home directory, and a directory `s1` dated during these runs stands under `~/.claude/specseal/answers`; this pass did not remove it, and its hand-back names it.

**Group 6, `hooks/hooksession.py`, `hooks/session-lease.py`.**

| Module | Mutants | New file | The group's new files at the head | Old file at 04115ed2 |
|---|---|---|---|---|
| `hooks/hooksession.py` | 9, h1 to h9 | 4 red; h2, h3, h4, h6, h8 survived | h2, h6 red; h3, h4, h8 survived | h3, h4, h8 survived, old gaps |
| `hooks/session-lease.py` | 12, s1 to s12 | 8 red; s6, s9, s10, s12 survived | s6, s9, s10, s12 survived | s6, s9, s10, s12 survived, old gaps |

The mutants sit at `claude_pid`'s exported pid, `claude_ancestor`'s pid floor, empty answer, answer, depth, start and unreadable parent, and `is_claude`; at the lease's own-session test, the environment's use, the recorded pid, the tool names, the edited path, the Bash directory, the directory and repository tests, the prune and the owner's error. h2, an exported pid never taken, and h6, a name beginning with `claude` read as claude, are red on `tests/test_session_lease.py`'s `Test_main` at the head. The old gaps: the walk passing pid 1, an empty `ps` answer walked on, an unreadable parent walked as pid 0; a notebook edit, a target that is no directory, a repository the lease cannot find, and an error reading the owner other than `OSError`.

**Group 11, `hooks/worktree_consent.py`.** Group 17's table, k1 to k25, ran at 67a86c57 against `tests/test_worktree_consent.py`, which holds group 11's five named cases: 20 red and 5 survived, k3, k10, k13, k23 and k25. Over group 11's two old files at 167950a6, k3, k10, k13 and k23 survive, old gaps as group 17 found. k25, `split_with_separators` doubling no backslash on Windows, is red there, on `test_a_windows_path_survives_tokenizing` and `test_a_windows_cd_path_is_not_mistaken_for_an_expansion`; group 12 moved both into `tests/test_worktree_guard.py`, where k25 is red at the head. No case was added.

**Group 15, `hooks/blocks.py`.** 15 mutants, k1 to k15, at `gfm_lines`' line ends, kept ends and splitter, `walk_text`'s piece inside a fenced or an open line, its unclosed fence and its line starts, `leaves_open`'s closer and its last opener, `leaves_html_open`'s tag end and closers, and `walk`'s sticky opening, its closer, a pending line and an unclosed fence: 12 red and 3 survived. k7 and k9 are red on the renderer oracle files at the head. k8, a comment closed anywhere read as closed, survives them and the two old files at 06d0f554: an old gap.

**Group 16, `hooks/commitgate.py`.** 7 mutants at `pre_commit`'s context, missing arm, failed staged diff, refusal text and sequencer test, and `_paths_between`'s base and failed listing, against `tests/test_commitgate.py` and `tests/test_gate.py`: 7 red.

**Group 18, `hooks/gate.py`.** 3 mutants at `git`'s exit and `lines`' failure and blank lines: 2 red. g3, `lines` keeping a blank line, survives the group's new files and the old file at 67a86c57: an old gap, which no git answer with a blank line reaches.

**Group 19, `hooks/tokens.py`.** 8 mutants at `given`'s two reads, `_bare`'s parentheses, `_read_words`' failed split, separators and comments, `without_bodies`' one-shape text and the order of `KNOWN`: 7 red. t5, the bodiless text read without the one shape's reduction, survives the group's new files and the old file at 95991e42: an old gap.

**Group 20, `hooks/implementer-notice.py`, `hooks/optin.py`.** The notice's 9 mutants, at the routing file's path, its absent item, the opt-in, the missing axes, the once-per-session test and its record, the axis test and the git hooks' decision: 6 red. n1, the routing file named by its absolute path, n3, a repository that does not opt in told, and n7, a clone whose git hooks decide told here too, survive the group's new files and the three old files at e1e39bf7: old gaps; the named case asserts a path that the absolute one also holds. Optin's 6 mutants, at the scratch marker, a directory of its name, the local root, the order of the two roots, a root that does not exist and a linked worktree's common directory: 6 red.

**Group 21, `hooks/config.py` and `skills/code-review/scripts/chain_check.py`.** Config reuses group 23's table, c1 to c90 less three, run at ca726662 against `tests/test_config.py`, which holds the 17 named cases: 75 red and 12 survived. Over group 21's six old files at fb0c5dfc, c6, c13, c14, c89 and c90 survive, the old gaps group 23 named; c55, c57, c62 to c65 and c67 are red, on the cases of `tests/test_one_table_walker_reads_what_gfm_renders.py`, which did not move, and all seven are red on that file at the head. Chain_check reuses group 36's table, 54 mutants run at 19c01e3b against `tests/test_chain_check.py`, which holds the six named cases: 51 red and 3 survived. k12, g17 and g18 survive group 21's old files at fb0c5dfc: old gaps.

**Group 22, `hooks/config.py`.** Group 23's table again; its 12 survivors survive group 22's two old files at 92add28b: old gaps.

**Groups 24 and 25, `hooks/cmdline.py`.** Group 26's table, m1 to m122 less two, run at da3eae09 against `tests/test_cmdline.py`, which holds the 23 named cases: 103 red and 17 survived. The 17 survive group 24's two old files at 687388b5 and group 25's five at 3cf11823: old gaps.

**Group 28, `skills/verify/scripts/mutation_check.py`.** 22 mutants at `mutated`'s count and unchanged text, `run_cases`' exit, session, group end, timeout and interrupt, the mutant's bytecode, the environment, the baseline's two refusals, the restore and its error, the UTF-8 read, the bound and the command, the platform's strategy and its detail, the exit map, the output, the zero bound and a command that cannot start, against `tests/test_mutation_check.py`: 21 red, in 253.0 s. mc21, a bound of 0 read as 0 seconds, survives the group's new files and the two old files at 6b884f5f: an old gap.

**Group 35, `skills/verify/scripts/unverified_check.py`.** 6 mutants at `heading_level`'s indent, run length, tab, bare run and level: 6 red.

**Group 37, `skills/settle/scripts/rule_changes.py` and `settle.py`.** Rule_changes' 25 mutants, at `parse`'s near miss, heading level, second section, section end, code span, comment and empty section, its no-change block and kinds and its file pattern; `apply_op`'s add, doubled heading, section end, removal and add placement; the `from` text's count and pattern; and `replay`'s all-or-none, waits, overlapping places and held specs, with `headings`' fence: 24 red. r4, a second section read, survives the group's new files and the three old files at db6541fc: an old gap. Settle's 28 mutants, at `load`'s missing sibling and its purpose, `released`'s unresolved ref, `rule_arm`'s two keeps, `rule_plan`'s pre-model spec, case, adding commit, open row, row at the base and conflicts, the report's missing base and plural, `apply`'s retired directories, policy root, held exit and missing base, `main`'s opt-out, local mode, settled root, unresolved ref, missing merge base and apply, `citations`' readers, `names`' abbreviation, the moved base, the line for a directory kept at the base and the released set: 24 red, in 316.8 s. st10, a row open at the base not read for a spec, st13, one of a count written plural, st25, an abbreviated name read as any id, and st27, a directory kept at the base with nothing open said nothing of, survive the group's new files and the three old files at db6541fc: old gaps.

**Group 40, `.github/scripts/release_report.py`.** 14 mutants at `main`'s refusal, `reading`'s missing tree, `durations`' values and parse error, `preloads`' error, `leg_minutes`' absent file, job name, sum and unparsed line, the table's missing leg, `change`'s new reading and share, the file rows' order and the file table: 11 red. rr3, a durations file of other values read, rr5, an agent definition that cannot be read let out, and rr7, a job name read by its prefix, survive the group's new files and the two old files at 409d8037: old gaps.

**Group 50, `evals/scripts/rule_cases.py` and `seed_defects.py`.** The rule file's named cases run `rule_cases.main`, whose truths `replay_targets.py#truths_with` builds, so both ran: rule_cases' 5 mutants at the warden case's truths and `main`'s writing, and `truths_with`'s 10 at its window, coordinate, range, last line, entry window, missing location, widening, doubled truth, widened body and unknown case, against `tests/test_rule_cases.py`: 15 red. Seed_defects' 14 mutants, at `target_of`'s subject, items, round 1 and round 2, its shared line and the seed, `seed`'s code token, window, repeated text and unit, the scaffold's remote and reflog, the CRLF line, `shared_line`'s count and `targets`' prefixes: 9 red. sd2, a commit adding no work item taken, sd3, a commit with no round 1 taken, sd6, a seed found in a string, sd8, a line whose text occurs twice seeded, and sd9, a line in no unit seeded, survive the group's new files and the old file at f19395a5: old gaps.

**The totals** (`executed`). 20 modules ran 231 new mutants: 193 red and 38 survived. Of the 38, 5 are red on another new file of the group at the head (w2, h2, h6, k7, k9), 32 are old gaps, and 1, a17, is a lost protection answered by a case seen red on it. The four reused tables ran their 37 survivors again, 66 runs over the old files of groups 11, 21, 22, 24 and 25: 8 red, k25 and config's seven, each on a case that stands at the head, and 58 old gaps. No other case was added.

### The move checks re-run with a test file's import followed

**What ran** (`executed`, macOS arm64, in round 4's fix pass). The 49 commands of the section above ran once more, each in a scratch clone of the branch (`git clone --shared`) checked out at the same commit, with `HEAD` in a command read as that section read it, and with `skills/verify/scripts/test_layout.py` as committed at 32cd06c7 copied over the clone's. That script follows `from <module> import` and `<module>.<name>` into every module directly under `tests/`, test files among them (`phases/phase-7.md` *A test file's import followed, at 32cd06c7*). The clone was removed after the runs. The middle column is the section above's last column.

| Group | Commit | Round 3's re-run | With a test file's import followed |
|---|---|---|---|
| 1 | 0a86c1b4 | `73 old cases, 74 items against 73 at 43324e4e104e, 23 failed`, exit 1 | `73 old cases, 74 items against 73 at 43324e4e104e, 23 failed`, exit 1 |
| 2 | ccca432d | `20 old cases, 147 items against 147 at 0a86c1b4c088, 4 failed`, exit 1 | `20 old cases, 147 items against 147 at 0a86c1b4c088, 4 failed`, exit 1 |
| 3 | e6700896 | `108 old cases, 119 items against 119 at ccca432d83a7, 6 failed`, exit 1 | `108 old cases, 119 items against 119 at ccca432d83a7, 6 failed`, exit 1 |
| 4 | 714f2df2 | `66 old cases, 180 items against 180 at e945c57c16fc, 4 failed`, exit 1 | `66 old cases, 180 items against 180 at e945c57c16fc, 4 failed`, exit 1 |
| 5 | 04115ed2 | `17 old cases, 37 items against 37 at 714f2df2eff1, 15 failed`, exit 1 | `17 old cases, 37 items against 37 at 714f2df2eff1, 15 failed`, exit 1 |
| 6 | df48707c | `18 old cases, 28 items against 28 at 04115ed2da4d, 9 failed`, exit 1 | `18 old cases, 28 items against 28 at 04115ed2da4d, 9 failed`, exit 1 |
| 7 | 9c70ddbf | `51 old cases, 59 items against 59 at 5639d076e5d3, 19 failed`, exit 1 | `51 old cases, 59 items against 59 at 5639d076e5d3, 19 failed`, exit 1 |
| 8 | 4f50aee0 | `51 old cases, 69 items against 70 at 459d7944c0d4, 21 failed`, exit 1 | `51 old cases, 69 items against 70 at 459d7944c0d4, 21 failed`, exit 1 |
| 9 | d8bba633 | `24 old cases, 24 items against 24 at 8dedf9e4698c, 17 failed`, exit 1 | `24 old cases, 24 items against 24 at 8dedf9e4698c, 17 failed`, exit 1 |
| 10 | 449feefb | `46 old cases, 47 items against 47 at 9197c897c376, 6 failed`, exit 1 | `46 old cases, 47 items against 47 at 9197c897c376, 6 failed`, exit 1 |
| 11 | e94c6826 | `100 old cases, 165 items against 165 at 167950a6e8bb, 5 failed`, exit 1 | `100 old cases, 165 items against 165 at 167950a6e8bb, 5 failed`, exit 1 |
| 12 | c512b123 | `219 old cases, 358 items against 358 at 56fb82e0646c, 123 failed`, exit 1 | `219 old cases, 358 items against 358 at 56fb82e0646c, 123 failed`, exit 1 |
| 14 | f5185d67 | `144 old cases, 187 items against 187 at 9818ee1a991f, 102 failed`, exit 1 | `144 old cases, 187 items against 187 at 9818ee1a991f, 102 failed`, exit 1 |
| 15 | f1d13be0 | `31 old cases, 142 items against 142 at 06d0f55453fc, 6 failed`, exit 1 | `31 old cases, 142 items against 142 at 06d0f55453fc, 6 failed`, exit 1 |
| 16 | b8e201e1 | `56 old cases, 71 items against 71 at 0b134a29b35e, 3 failed`, exit 1 | `56 old cases, 71 items against 71 at 0b134a29b35e, 3 failed`, exit 1 |
| 17 | 67a86c57 | `292 old cases, 409 items against 409 at b8e201e1f012, 114 failed`, exit 1 | `292 old cases, 409 items against 409 at b8e201e1f012, 114 failed`, exit 1 |
| 18 | 95991e42 | `27 old cases, 27 items against 27 at 67a86c5730f0, 1 failed`, exit 1 | `27 old cases, 27 items against 27 at 67a86c5730f0, 1 failed`, exit 1 |
| 19 | e1e39bf7 | `2 old cases, 19 items against 19 at 95991e42b3d5, 2 failed`, exit 1 | `2 old cases, 19 items against 19 at 95991e42b3d5, 2 failed`, exit 1 |
| 20 | 6277911e | `53 old cases, 55 items against 55 at e1e39bf7b23d, 2 failed`, exit 1 | `53 old cases, 55 items against 55 at e1e39bf7b23d, 2 failed`, exit 1 |
| 21 | 1b3e6978 | `193 old cases, 803 items against 803 at fb0c5dfccd2f, 23 failed`, exit 1 | `193 old cases, 803 items against 803 at fb0c5dfccd2f, 23 failed`, exit 1 |
| 22 | 10f6ad94 | `65 old cases, 190 items against 190 at 92add28be86b, 5 failed`, exit 1 | `65 old cases, 190 items against 190 at 92add28be86b, 5 failed`, exit 1 |
| 23 | ca726662 | `134 old cases, 333 items against 333 at c6c1d8b03de3, 79 failed`, exit 1 | `134 old cases, 333 items against 333 at c6c1d8b03de3, 79 failed`, exit 1 |
| 24 | 93bf39da | `4 old cases, 215 items against 215 at 687388b5ae85, 2 failed`, exit 1 | `4 old cases, 215 items against 215 at 687388b5ae85, 2 failed`, exit 1 |
| 25 | eb207a6d | `65 old cases, 661 items against 661 at 3cf118239946, 21 failed`, exit 1 | `65 old cases, 661 items against 661 at 3cf118239946, 21 failed`, exit 1 |
| 26 | da3eae09 | `367 old cases, 1189 items against 1189 at 0e561e86de7a, 100 failed`, exit 1 | `367 old cases, 1189 items against 1189 at 0e561e86de7a, 100 failed`, exit 1 |
| 27 | ffb0bd4b | `11 old cases, 11 items against 11 at 300abe340a60, 0 failed`, exit 0 | `11 old cases, 11 items against 11 at 300abe340a60, 0 failed`, exit 0 |
| 28 | b16613b3 | `40 old cases, 54 items against 54 at 6b884f5f9f41, 28 failed`, exit 1 | `40 old cases, 54 items against 54 at 6b884f5f9f41, 28 failed`, exit 1 |
| 29 | 31aed13b | `29 old cases, 50 items against 50 at 7cd34d46115a, 1 failed`, exit 1 | `29 old cases, 50 items against 50 at 7cd34d46115a, 0 failed`, exit 0 |
| 30 | 666cedbb | `24 old cases, 25 items against 25 at 2f2d21c97c4f, 0 failed`, exit 0 | `24 old cases, 25 items against 25 at 2f2d21c97c4f, 0 failed`, exit 0 |
| 31 | 391c7857 | `34 old cases, 46 items against 46 at 17ee85328290, 0 failed`, exit 0 | `34 old cases, 46 items against 46 at 17ee85328290, 0 failed`, exit 0 |
| 32 | bf6df24b | `63 old cases, 95 items against 95 at 6df0950bb66f, 0 failed`, exit 0 | `63 old cases, 95 items against 95 at 6df0950bb66f, 0 failed`, exit 0 |
| 33 | c9af3c38 | `194 old cases, 221 items against 221 at 95d02cc818d9, 156 failed`, exit 1 | `194 old cases, 221 items against 221 at 95d02cc818d9, 156 failed`, exit 1 |
| 34 | 5966150b | `198 old cases, 314 items against 315 at 10667b32ad71, 46 failed`, exit 1 | `198 old cases, 314 items against 315 at 10667b32ad71, 46 failed`, exit 1 |
| 35 | 2272cd1e | `171 old cases, 329 items against 329 at ffd898ec87dc, 3 failed`, exit 1 | `171 old cases, 329 items against 329 at ffd898ec87dc, 3 failed`, exit 1 |
| 36 | 19c01e3b | `116 old cases, 246 items against 246 at c30f7d9521c6, 20 failed`, exit 1 | `116 old cases, 246 items against 246 at c30f7d9521c6, 20 failed`, exit 1 |
| 37 | 809408e5 | `116 old cases, 174 items against 174 at db6541fc96b0, 77 failed`, exit 1 | `116 old cases, 174 items against 174 at db6541fc96b0, 77 failed`, exit 1 |
| 38 | 4f350b0f | `174 old cases, 330 items against 330 at 809408e5ec2e, 0 failed`, exit 0 | `174 old cases, 330 items against 330 at 809408e5ec2e, 0 failed`, exit 0 |
| 39 | 46e1ec4c | `38 old cases, 50 items against 50 at 4f350b0f9144, 18 failed`, exit 1 | `38 old cases, 50 items against 50 at 4f350b0f9144, 17 failed`, exit 1 |
| 40 | 565de415 | `9 old cases, 15 items against 15 at 409d8037ab94, 4 failed`, exit 1 | `9 old cases, 15 items against 15 at 409d8037ab94, 4 failed`, exit 1 |
| 41 | 56a8ac20 | `22 old cases, 61 items against 61 at 565de4152a2c, 1 failed`, exit 1 | `22 old cases, 61 items against 61 at 565de4152a2c, 0 failed`, exit 0 |
| 42 | 5e26a264 | `25 old cases, 30 items against 30 at 56a8ac20bf30, 0 failed`, exit 0 | `25 old cases, 30 items against 30 at 56a8ac20bf30, 0 failed`, exit 0 |
| 43 | 0cc2609c | `12 old cases, 17 items against 17 at 5e26a264b9d6, 0 failed`, exit 0 | `12 old cases, 17 items against 17 at 5e26a264b9d6, 0 failed`, exit 0 |
| 44 | 222bf69a | `35 old cases, 35 items against 35 at 0cc2609cad5a, 2 failed`, exit 1 | `35 old cases, 35 items against 35 at 0cc2609cad5a, 0 failed`, exit 0 |
| 45 | efc3a79f | `94 old cases, 102 items against 102 at bc2b976ffa97, 36 failed`, exit 1 | `94 old cases, 102 items against 102 at bc2b976ffa97, 30 failed`, exit 1 |
| 46 | b68d41d1 | `24 old cases, 33 items against 33 at efc3a79f8793, 0 failed`, exit 0 | `24 old cases, 33 items against 33 at efc3a79f8793, 0 failed`, exit 0 |
| 47 | 503e2f5e | `42 old cases, 52 items against 52 at b68d41d1caa8, 0 failed`, exit 0 | `42 old cases, 52 items against 52 at b68d41d1caa8, 0 failed`, exit 0 |
| 48 | f7ef43cc | `47 old cases, 80 items against 80 at 503e2f5e32f4, 2 failed`, exit 1 | `47 old cases, 80 items against 80 at 503e2f5e32f4, 0 failed`, exit 0 |
| 49 | a4a113f6 | `60 old cases, 95 items against 95 at f7ef43ccac39, 5 failed`, exit 1 | `60 old cases, 95 items against 95 at f7ef43ccac39, 0 failed`, exit 0 |
| 50 | 52ce0e03 | `26 old cases, 35 items against 35 at f19395a52bea, 15 failed`, exit 1 | `26 old cases, 35 items against 35 at f19395a52bea, 0 failed`, exit 0 |

**What the re-run changed** (`executed`, each command's lines compared with round 3's). 38 commands print round 3's lines word for word. Eight print fewer: groups 29, 41, 44, 48, 49 and 50 now exit 0, group 39 loses its line on `read` and group 45 its six lines on the cases of `tests/test_a_declared_label_reaches_the_tracker.py`. Step 1 changed one reading, so each line gone is a name that a file imports from a test file and that now reads alike where that file defines it. Three print the same count with another name on one case each: group 34's case of `tests/test_the_gate_names_every_step_ci_runs.py` on `ROOT` where it was `reasons`, group 35's case of `tests/test_one_heading_rule_holds_to_commonmark.py` on `uc` where it was `disagreements`, and group 37's two cases on `rules` and `git` where they were `parse` and `OVERVIEW_OPEN`. Each such import now reads alike, and the definition the following reaches behind it differs. No re-run prints a line on a case of a file that declares `TARGET` that round 3's did not print, so no module goes to the mutants by its `TARGET` that round 3 did not send.

**The lines that name a case in a file that declares no `TARGET`** (`executed`, a script outside the tree that reads each named case's file at the command's commit for its `TARGET` and looks the case up by name in it). 29 lines name such a case that stayed in its file while the group changed a name it reads. Round 3's section counted 17 of them, the lines of the groups recorded at exit 0. `plan.md` *Round 4's fix pass* step 4 sends such a line whatever its command was recorded at, so the lines of groups recorded at exit 1 count too: group 1's five on `ROOT`, group 7's one on `ROOT`, group 8's one on `two_axis_text`, group 9's one on `declare`, group 14's twelve on `git`, group 23's one on `URL` and group 34's one. Of round 3's 17, 10 now pass (groups 29, 41, 48, 49 and 50), and 7 still fail: group 16's two on `a_git_whose_diff_fails`, group 19's on `_corpora`, group 22's on `shape_text`, group 35's on `uc` and group 37's two on `rules` and `git`. Each line goes to the subject `spec.md` *The proof of equal protection* gives its case.

| Group | Case, where the line names it | Where it stands at 32cd06c7 | Subject | Proof |
|---|---|---|---|---|
| 1 | `tests/test_gates_do_not_fail_open.py::test_a_reader_that_decoded_nothing_answers_empty_rather_than_raising` | `tests/test_optin.py::Test_repo_root::test_refuses_a_reader_that_decoded_nothing_and_answers_empty` | `hooks/optin.py#repo_root` | op1, red |
| 1 | `::test_a_repository_whose_path_the_locale_cannot_carry_still_resolves` | `tests/test_optin.py::Test_repo_root::test_accepts_a_repository_whose_path_the_locale_cannot_carry` | `hooks/optin.py#repo_root` | op2, red |
| 1 | `::test_the_common_directory_reader_that_decoded_nothing_answers_empty` | `tests/test_optin.py::Test_git_common_dir::test_refuses_a_reader_that_decoded_nothing_and_answers_empty` | `hooks/optin.py#git_common_dir` | op3, red |
| 1 | `::test_the_process_probe_survives_output_it_cannot_decode` | `tests/test_worktree_guard.py::Test_lease_owner_alive` | `hooks/worktree-guard.py#lease_owner_alive` | wg1, red |
| 1 | `::test_the_commit_gates_hint_survives_a_root_with_no_relative_spelling` | `tests/test_commit_review_gate.py::Test_main` | `hooks/commit-review-gate.py`, `main` through `declaration_hint` | group 17's table, g29 and g30 red; g12 and g15 below |
| 7 | `tests/test_console_is_not_utf8.py::test_a_declaration_that_cannot_be_decoded_is_not_an_answer` | `tests/test_routing.py::Test_module` | `hooks/routing.py#declarations` | rt1, red |
| 8 | `tests/test_routing_is_recorded.py::test_the_commit_gate_decides_the_same_with_the_new_rows_and_without` | `tests/test_commit_review_gate.py::Test_main` | `hooks/commit-review-gate.py`, `main` | group 17's table; g12 and g15 below |
| 9 | `tests/test_the_implementer_is_recorded.py::test_the_commit_gate_decides_identically_with_the_row_and_without` | `tests/test_commit_review_gate.py::Test_main` | `hooks/commit-review-gate.py`, `main` | group 17's table; g12 and g15 below |
| 14 | ten parity cases of `tests/test_chain_hooks_hardening.py`, `test_parity_repo_asks_when_code_commits_without_a_comparison` to `test_both_opt_ins_report_together` | `tests/test_commit_review_gate.py::Test_main` | `hooks/commit-review-gate.py`, `main` through the parity arm | group 17's table; g12 and g15 below |
| 14 | `tests/test_chain_hooks_hardening.py::test_a_diff_git_could_not_take_is_asked_about_at_pre_commit` | `tests/test_commitgate.py::Test_pre_commit` | `hooks/commitgate.py#pre_commit` | group 16's table in the section above, 7 red |
| 14, 16 | `tests/test_chain_hooks_hardening.py::test_the_backstop_hands_the_parity_arm_none_where_git_could_not_list` | `tests/test_gate.py::Test_module` | `hooks/commitgate.py#_paths_between` | group 16's table in the section above, 7 red |
| 16 | `tests/test_chain_hooks_hardening.py::test_a_diff_git_could_not_take_is_asked_about_by_the_parity_arm` | `tests/test_commit_review_gate.py::Test_main` | `hooks/commit-review-gate.py`, `changed_paths` and `touches_code` | group 17's table, g13 and g14 red; g12 and g15 below |
| 19 | `tests/test_the_old_spellings_reach_the_hook.py::test_the_three_token_reads_answer_as_one` | where it was | the definition `_corpora`, line 24 of its file at e1e39bf7, a check across files; since a29834e3 the line names `_corpora` alone (*The lines sent to a definition, with every name printed*) | cp1 to cp6, old gaps |
| 22 | `tests/test_the_mode_question_is_asked_once.py::test_the_writer_leaves_a_commented_row_alone` | `tests/test_seal.py::Test_write_row` | `skills/implement/scripts/seal.py#write_row` and `#with_row` | sw1 and sw2, red |
| 23 | `tests/test_a_signer_declares_its_pact.py::test_s4_the_configs_this_plugin_writes_or_copies_are_silent` | where it was | `hooks/config.py#pact_declaration` | group 23's table, every mutant at `pact_declaration` red |
| 34 | `tests/test_the_gate_names_every_step_ci_runs.py::test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm` | where it was | the definitions `import pathlib`, `TARGET`, `ROOT` and `gate` of `tests/test_broad_gate.py`, lines 24, 43, 45 and 54 at 5966150b, a case reading prose (*The lines sent to a definition, with every name printed*) | bp1, bt1, br1, bg1 and bg2, red; ro1 stands for no definition the rule sends |
| 35 | `tests/test_one_heading_rule_holds_to_commonmark.py::test_every_tracked_markdown_file` | where it was | `skills/verify/scripts/unverified_check.py#heading_level`, which `disagreements` calls through `uc` | group 35's table in the section above, 6 red |
| 37 | `tests/test_settle_applies_rule_changes_in_place.py::test_the_skills_example_reads_as_the_skill_says` | where it was | `skills/settle/scripts/rule_changes.py#parse` | group 37's table in the section above; r4 an old gap |
| 37 | `tests/test_settle_reads_before_it_removes.py::test_a_closed_row_is_told_to_merge_before_its_directory_goes` | where it was | `skills/settle/scripts/settle.py`, its report | group 37's table in the section above; st10, st13, st25 and st27 old gaps |

**Where an earlier table stands** (`read`, each table's record; `executed`, `git diff --stat 208803e6 32cd06c7` over every shipped file and test file named in the table above, empty). Group 16's and group 35's tables in the section above ran at 208803e6 and left no survivor, and their mutants sit at the decision points of `pre_commit`, `_paths_between` and `heading_level`. Group 37's tables ran at 208803e6 with their mutants at `parse` and at `settle.py`'s report, and each survivor ran against group 37's new files at 208803e6, the two case files above among them, and over group 37's old files at db6541fc. Group 23's table ran at ca726662, and every mutant it holds at `pact_declaration` was red. Group 17's table ran at 67a86c57 with one or two mutants at each function of `hooks/commit-review-gate.py`, g13 at `changed_paths`, g14 at `touches_code`, g29 and g30 at `declaration_hint`, and left g12 and g15 at `commit_shape`. None of these files changed between 208803e6 and 32cd06c7.

**The mutants that ran** (`executed`, at 32cd06c7, in a scratch clone of the branch, one `bin/mutation-check` batch per subject with `-x`, the runner a copy outside the tree and `HOME` a directory in the scratch area; the old column in a second scratch clone checked out at each group's base).

| # | Mutation | At 32cd06c7 | Old files |
|---|---|---|---|
| op1 | `optin.repo_root` reads a None stdout as text | red, `tests/test_optin.py` | not run |
| op2 | `optin.repo_root` decodes git's answer as Latin-1 | red | not run |
| op3 | `optin.git_common_dir` reads a None stdout as text | red | not run |
| wg1 | `lease_owner_alive` reads a None stdout as text | red, `tests/test_worktree_guard.py` | not run |
| rt1 | `routing.declarations` catches no decode error | red, `tests/test_routing.py` | not run |
| sw1 | `with_row` writes past a table the walker refused | red, `tests/test_seal.py` and `tests/test_config.py` | not run |
| sw2 | `write_row` writes past `with_row`'s refusal | red | not run |
| ro1 | `ROOT` names `tests/`, not the repository | red, `tests/test_the_gate_names_every_step_ci_runs.py`, at collection | not run |
| cp1 | `_corpora` keeps a None command of `TOKEN_CASES` | SURVIVED, `tests/test_the_old_spellings_reach_the_hook.py` | SURVIVED at 95991e42, an old gap |
| cp2 to cp6 | `_corpora` leaves out one of its five sources: `TOKEN_CASES`, the heredoc commands, the guard's `TOKEN_COMMANDS`, `BODY_TOKENS` and `TYPED_BESIDE_A_BODY` | SURVIVED | SURVIVED at 95991e42, old gaps |
| g12 | `commit_shape` reads no pathspec after `--`, rebuilt from group 14's description | red, `tests/test_commit_review_gate.py`, 51.7 s | ran before the head's verdict: red at 0b134a29 on `test_parity_gate_sees_commits_that_never_touched_the_index`, which stands at 32cd06c7 in `tests/test_commit_review_gate.py`; survived at 43324e4e, 459d7944 and 8dedf9e4 |
| g15 | `commit_shape` takes a value option's value as a path, rebuilt from group 14's description | SURVIVED, 53.1 s | SURVIVED at 43324e4e, 459d7944, 8dedf9e4, 9818ee1a and 0b134a29, an old gap as groups 14 and 17 found |

These batches ran 16 mutants: 9 red and 7 survived, every survivor an old gap. cp1 to cp6 are new old gaps: the case asserts that three readers agree over the commands `_corpora` gives, so a corpus with fewer commands, or with a None among them, still agrees, at the head and at the base. g12 and g15 are rebuilt from their descriptions, because group 14's batch text is not in the tree; the rebuilt g12 removes the pathspec, which is red where group 14's survived. ro1 sits at the `ROOT` of group 34's case file, which reads at 5966150b as it read at the base 10667b32, so since round 5 it stands for no definition the subject rule sends; group 34's case is proved by the five mutants of *The lines sent to a definition, with every name printed*, all red. No protection is lost, and no case was added.

### The lines sent to a definition, with every name printed

**What was asked.** `plan.md` *Round 5's fix pass*, steps 4 to 6, after `rounds/round-5.md` finding 1: the three recorded commands that send a line to a definition run again with the script that names every name apart, the definitions each line sends are named with their file and line, and group 34's mutants run at its definitions against its case alone. This section holds group 34's and group 19's rows; 4e987021's is in `phases/phase-7.md` *The line names every name, in round 5's fix pass*.

**The re-runs** (`executed`, macOS arm64). Each command ran in a scratch clone of the branch (`git clone --shared`) checked out at the command's commit, with `skills/verify/scripts/test_layout.py` as committed at 24cd7813 copied over the clone's and restored after, and the worktree's `.venv` as the interpreter. The clone was removed when the pass ended.

| Group | Commit | Round 4's re-run | With every name printed |
|---|---|---|---|
| 19 | e1e39bf7 | `2 old cases, 19 items against 19 at 95991e42b3d5, 2 failed`, exit 1 | `2 old cases, 19 items against 19 at 95991e42b3d5, 2 failed`, exit 1 |
| 34 | 5966150b | `198 old cases, 314 items against 315 at 10667b32ad71, 46 failed`, exit 1 | `198 old cases, 314 items against 315 at 10667b32ad71, 46 failed`, exit 1 |

Each command prints one line per failing case, as round 4's re-run did, so each last line and exit stand. Compared case by case with round 4's re-run output, three lines name more names and every other line is word for word:

- group 34's case `tests/test_the_gate_names_every_step_ci_runs.py::test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm` printed `name ROOT` and now prints `names ROOT, gate, GATE, TARGET, gate_module, pathlib`;
- group 19's `test_the_three_token_reads_answer_as_one` printed `name _corpora` and now prints `names _corpora, TOKEN_CASES`;
- group 19's `test_a_token_is_a_bare_word_and_nothing_else` printed `name tokens` and now prints `names tokens, HOOKS, __file__, importlib, load_hook_module, os`. At e1e39bf7 the case stands in `tests/test_tokens.py`, which declares `TARGET = "hooks/tokens.py"`, so it counts for `hooks/tokens.py`, whose 8 mutants ran in round 3's pass, and the names it adds send nothing.

**The definitions each line sends** (`executed`, a script outside the tree that makes `_Names.forms`'s reading at the command's commit and at the group's base and keeps each definition's file and line). The case file of group 34 is `tests/test_the_gate_names_every_step_ci_runs.py`, and group 19's is `tests/test_the_old_spellings_reach_the_hook.py`.

| Group | Name on the line | At the base | At the command's commit | Sent |
|---|---|---|---|---|
| 34 | `ROOT` | the case file, line 43 | the case file, line 48; `tests/test_broad_gate.py`, line 45 | `tests/test_broad_gate.py`, line 45. The case file's reads as the base's, in the same file |
| 34 | `gate` | the case file, line 53 | `tests/test_broad_gate.py`, line 54 | `tests/test_broad_gate.py`, line 54 |
| 34 | `GATE` | the case file, line 44 | not reached | none |
| 34 | `TARGET` | not reached | `tests/test_broad_gate.py`, line 43 | `tests/test_broad_gate.py`, line 43 |
| 34 | `gate_module` | the case file, line 49 | not reached | none |
| 34 | `pathlib` | not reached | `tests/test_broad_gate.py`, line 24, `import pathlib` | `tests/test_broad_gate.py`, line 24 |
| 19 | `_corpora` | the case file, line 92 | the case file, line 24 | the case file, line 24 |
| 19 | `TOKEN_CASES` | the case file, line 21 | not reached by 24cd7813's reading; since a29834e3, `tests/test_tokens.py`, line 20, through the import inside `_corpora`, read alike, so the line no longer names it | none |

`tests/test_broad_gate.py` holds the same four lines at the base, 16, 25, 27 and 36, but the base's reading of the case does not reach that file, because `reasons` stood in the case's own file until group 34 moved it. The four lines stand unchanged at the head: `git diff --stat 5966150b 24cd7813` over the two files is empty (`executed`).

Group 19's head `_corpora` reads `TOKEN_CASES` through `from test_tokens import TOKEN_CASES` inside its own body. Since a29834e3 the name condition follows an import made inside a function body, so both readings reach `TOKEN_CASES`, the base's in the case file and the head's in `tests/test_tokens.py`, and it reads alike: the line names `_corpora` alone and sends `_corpora` (`phases/phase-7.md` *The import inside a function body, in round 5's second fix pass*). cp1 to cp6 stand for the line, because `git diff --stat 32cd06c7 412760bd` over the file is empty and a mutant that survives the whole file survives the one case in it; each survived the old files at 95991e42 too, an old gap. cp2, which empties `TOKEN_CASES`'s commands in `_corpora`, is one of `_corpora`'s mutants and stands for no name of its own.

**Group 34's mutation table** (`executed`, one `bin/mutation-check` batch over `tests/test_broad_gate.py` at 24cd7813 in the scratch clone, with `--tests "bin/test tests/test_the_gate_names_every_step_ci_runs.py::test_the_skill_counts_the_steps_with_a_local_answer_and_no_arm -q -p no:xdist -x"`, the runner a copy outside the tree and `SPECSEAL_ANSWERS` a directory in the scratch area; each mutant then ran once alone, for its output). 5 mutants, 5 red, in 3.4 s after a 1.1 s baseline that ran the one case.

| # | Definition | Mutation | At 24cd7813 | Old files |
|---|---|---|---|---|
| bp1 | `import pathlib`, line 24 | binds `posixpath` as `pathlib` | red at collection: `posixpath` has no `Path` | not run |
| bt1 | `TARGET`, line 43 | names `skills/verify/scripts/seal_stamp.py` | red at collection: the loaded module has no `stamp_module` | not run |
| br1 | `ROOT`, line 45 | names `tests/`, not the repository | red at collection: `FileNotFoundError` | not run |
| bg1 | `gate`, line 54 | binds `chain_check.py` | red at collection: the loaded module has no `stamp_module` | not run |
| bg2 | `gate`, line 54 | binds the gate with every reason of `PARTITION` emptied | red on the case's assertion: the sentence it builds opens "No steps" | not run |

Four of the five are red because `tests/test_broad_gate.py` cannot be imported, which shows that the case reads those definitions and little more, as `plan.md` *Alternatives considered* says of a definition that is neither a function nor a collection. bg2 keeps the import and changes what `gate` holds, and the case's own assertion fails, so the count the case checks comes from `gate.PARTITION` through `reasons`. No mutant survived, so the old column did not run and no case was added. ro1 stays in *The move checks re-run with a test file's import followed* as a mutant that ran.
