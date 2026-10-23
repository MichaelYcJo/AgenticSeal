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

### What `hooks/` holds back

**The installer waits on Q10** (`read`). `hooks/githooks.py` and `hooks/hook-install.py` have their cases in `tests/test_the_hooks_are_installed_where_git_runs_them.py`, which `docs/the-commit-gate-inside-git.md` names on the `check:` line of a section whose heading is also the document's title. `questions.md` Q10's default is wait, so the two keep their cases there through this work.

**Files a group may drain but not remove** (`executed`, `git grep` over the `check:` lines of `docs/`, `CONTRIBUTING.md`, `skills/` and `agents/`). Of the undeclared files that hold `hooks/` cases, these are named by a `check:` line: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/test_the_hooks_are_installed_where_git_runs_them.py`, `tests/test_routing_is_recorded.py`, `tests/test_optin_home.py`, `tests/test_a_gate_that_fails_says_so.py`, `tests/test_worktree_guard_signals.py`, `tests/test_guard_resolves_the_tree_it_judges.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_the_mode_question_is_asked_once.py`, `tests/test_gate_judges_the_repo_it_commits_to.py`, `tests/test_chain_hooks_hardening.py`, and `tests/test_a_creation_is_judged_before_git_runs.py`, which group 7 emptied. Each line has its `## Rule changes` item in `spec.md` at 066e619b except the installer's.

**Why this spawn stopped at e94c6826** (`read`). The next group is the worktree guard's light files: the guard's among the 54 cases left in `tests/test_guard_resolves_the_tree_it_judges.py` (the rest read the policy, which is #923's, or run the commit gate), `tests/test_lease_liveness.py`'s 29, `tests/test_worktree_guard_signals.py`'s 20, `tests/test_a_creation_in_another_clone_asks_nobody.py`'s 9, `tests/test_the_idle_session_rows_ask_nobody.py`'s 10 and the guard's process-probe case in `tests/test_gates_do_not_fail_open.py`, all into `tests/test_worktree_guard.py` under its autouse fixture, then the guard's mutants once. Their helpers share names with the guard file's (`run`, `decide`, `judge`, `dirty_deny`), so the group is a large one, and the spawn hands back at the boundary before it with its records current.

### What remains in phase 6

- `hooks/`, in the order `questions.md` gives: the worktree guard's light files, with phase 4's h21 to re-run; `hooks/sealer-stamp.py`, `hooks/sealer-stamp-queue.py` and `hooks/commitgate.py`, written anew under rule 3 (`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` prices its remaining cases at 110.2 s); the commit gate's light cases, among them those left in `tests/test_routing_is_recorded.py`, `tests/test_the_implementer_is_recorded.py`, `tests/test_optin_home.py` and `tests/test_gates_do_not_fail_open.py`; then the six shared readers, one group each, with `hooks/config.py`'s group taking the cases `tests/test_a_reference_root_is_read_and_never_taken.py` and `tests/test_a_script_copied_alone_exits_2.py` hold for routing and config together. `hooks/githooks.py` and `hooks/hook-install.py` wait on Q10. `hooks/answer-clear.py` has a file whose `Test_module` holds its two round trips and no `Test_main`.
- The other seven shipped directories of `plan.md`'s phase 6 row: `hooks/git/`, `skills/verify/scripts/`, `skills/code-review/scripts/`, `skills/settle/scripts/`, `skills/implement/scripts/`, `.github/scripts/`, `evals/scripts/`, with the light files phase 5 left for its other modules.
- Phase 4's survivors: h14 was re-run against the creation flow in group 7 and survives, an old gap. h2, h4, h6, h12, h21 and h23 wait for the groups that rebuild the modules whose cases reach them (`unverified`, for the spawn that places those modules).
