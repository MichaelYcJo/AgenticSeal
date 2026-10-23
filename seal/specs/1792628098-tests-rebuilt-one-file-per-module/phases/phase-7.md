# Phase 7: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | not closed; its first step is cc391101 |

## What this phase was asked

The spawn ran in two parts. Part 1: S14 first, `--moved` in `skills/verify/scripts/test_layout.py` dropping the docstring of every function and class a compared case or fixture defines, through one function `_moved_form` that `_resolver` also calls, with S14's rows of `tests/test_test_layout.py::Test_moved` seen red against the script at 9e92e4e8, the script's docstring and `_moved_form`'s rewritten in the same commit, the changed code's mutants in one `bin/mutation-check` batch, and group 44's move check re-run to confirm it names no failure for `test_one_open_issue_closes_it_and_opens_the_next`. Then S10 under `questions.md` Q9's default: `bin/test-layout --check --all`, and the suite case given `--all` only where it exits 0, or else `overview.md` *Not done* naming each undeclared file and why it stays. Then the overview's rows for the framer closed against 9e92e4e8. Then the suite's wall time measured locally the same way twice, `bin/test -q` in an archive of the base where #942 left `release/v0.22.3` and in the worktree, with the pass, fail and skip counts and the load average at each run. Part 2, after the orchestrator's CI run on the final tree: `.test_durations` replaced from that run's `test-durations` artifact, the closing memo with the wall times before and after and the CI wall time per leg, phase 7's Status in `plan.md`, and `handoff.md` naming round 3 as next.

## What this phase found

**Whether the frame holds** (`read`). It holds for S14: `spec.md` *The proof of equal protection* states the body condition with every nested docstring dropped, `plan.md`'s phase 7 row and the alternative it chose name one function both comparisons call, and `_moved_form` and `_resolver` at 9e92e4e8 each dropped the top docstring alone, by two copies of one statement. S14's row says the accepting row is seen red against the script at 54b41700; the script did not change between 54b41700 and 9e92e4e8 (`git diff 54b41700 9e92e4e8 -- skills/verify/scripts/test_layout.py` is empty, `executed`), so the run at 9e92e4e8 is the same run.

### S14, at cc391101

**What changed** (`executed`, macOS arm64). `_moved_form` walks the definition it is given and drops the docstring of every function, async function and class in it, the definition itself included, where it dropped the definition's own docstring alone. `_resolver` returns `_moved_form` of the fixture's definition in place of its own dump of the definition with the top docstring dropped, so a fixture is read as a case's body is read. Two readings ride on the one function and the build took them as the frame's "docstrings dropped as for a case": a fixture's name is dropped from its form, which changes nothing because a fixture is resolved by its name on both sides; and a fixture's first `self` is dropped, so a fixture moved from a file into a class, where it takes `self`, compares equal to the definition it was. The module docstring's `body` and `fixture` entries say both.

**The rows** (`executed`). The world of `Test_moved` gains a third old file at the base, `tests/test_old_c.py`, holding `test_four` and the fixture `maker`. `maker` defines a function with a docstring over three lines; `test_four` defines a function holding a class holding an async method, each with a docstring over three lines. `NESTED_NEW` is the two moved into a class `Test_four`, every line four spaces deeper as the formatter leaves a move, the docstrings' continuation lines among them, with `self` added and the case renamed. `test_accepts_a_pure_move` is parametrized over two rows, `every-kind-of-move`, the case as it was, and `a-nested-docstring-re-indented`. `test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture` gains `olds` as a fourth argument, the two old files for its ten rows as they were, and the row `an-edited-nested-function`, where the nested method returns 4 in place of 3 and the check names `tests/test_old_c.py::test_four` on the body condition and the new case as standing for no old case.

**Seen red** (`executed`). Against the script at 9e92e4e8, `bin/test tests/test_test_layout.py -q -p no:xdist -k Test_moved` gave 1 failed and 18 passed: `a-nested-docstring-re-indented` exited 1 with `moved: tests/test_old_c.py::test_four: body: not in the new files unchanged` and the new case standing for no old case. `an-edited-nested-function` passed there, as a refusal the old script already made; the mutant n6 below is what shows it red. Built, the module gives 55 passed.

**The mutation table** (`executed`, one `bin/mutation-check` batch over `skills/verify/scripts/test_layout.py` with `--tests "bin/test tests/test_test_layout.py -q -p no:xdist -x -k Test_moved"`, at the tree committed as cc391101): 8 mutants, 8 red, in 11.7 s after a 4.5 s baseline. No old column ran: every mutant was red against the new file.

| # | Mutation | New file |
|---|---|---|
| n1 | the walk reads the definition alone, the form before this step | red |
| n2 | the walk reads the definition and its direct children, not every depth | red |
| n3 | a class's docstring kept | red |
| n4 | an async function's docstring kept | red |
| n5 | a function's docstring kept | red |
| n6 | every nested body dropped whole, not its docstring alone | red |
| n7 | `_resolver` dumps the fixture's definition whole, not through `_moved_form` | red |
| n8 | a first `self` kept | red |

**Group 44's move check, re-run** (`executed`): `bin/test-layout --moved 0cc2609c --from tests/test_a_release_rolls_the_flow_measurement_issue.py --to tests/test_roll_flow_measurement_issue.py tests/test_a_release_rolls_the_flow_measurement_issue.py` ends `test-layout: moved: 35 old cases, 35 items against 35 at 0cc2609cad5a, 0 failed`, exit 0, and prints no line for `test_one_open_issue_closes_it_and_opens_the_next`. Group 44 ran its 38 mutants at 222bf69a because of that one case; its record stays as written, and the module's proof stands under either reading.

**The boundary** (`executed`). At the tree committed as cc391101, before the commit over the same bytes: `bin/test tests/test_test_layout.py tests/test_censuses.py tests/test_a_reference_root_is_read_and_never_taken.py tests/test_conftest.py -q`, the module and every test file naming `test_layout` or `test-layout`, 238 passed. `bin/test-layout --check` exits 0 with 185 files read, 0 refused and 116 declaring no `TARGET`; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0. `uvx ruff check` and `uvx ruff format --check` pass each of the two changed files, one file per run, and `--pairs` names 0 pairs in `tests/test_test_layout.py`.

### S10 under Q9's default

**`--check --all`** (`executed`, at cc391101): `bin/test-layout --check --all` exits 1, `test-layout: 185 files read, 116 refused, 116 declare no TARGET`. Every refusal is a file that declares no `TARGET`; no twin between two undeclared files is refused. So the suite case `Test_main::test_accepts_this_repositorys_tests` keeps `--check` without `--all`, and `overview.md` *Not done* names each of the 116 files with the reason it stays.

**How the 116 were sorted** (`executed`, a script outside the tree that reads each file's cases with `test_layout.py#_all_cases` and every `check:` line with `.github/scripts/rules.py#rule_files`, `#check_lines` and `#parse`; `read`, each file's docstring and the paths its text names). 19 hold no case, and each is named by a `docs/` line and stands in a `from:` of `spec.md` *Rule changes* and in no `to:`, every line counted (`tests/test_optin_home.py` on six lines, three more files on two). 1 is the installer file Q10 holds. 13 hold checks across files or against an oracle. 80 hold cases that read prose, a workflow, a wrapper or the released files.

**What the sort found that the frame does not place.** Three of the 116 hold cases of `tests/conftest.py`'s own helpers: `tests/test_a_shrunken_corpus_declines_to_judge.py` drives `on_disk` and `decline_if_shrunken`, `tests/test_a_workflow_is_read_the_one_way.py` drives `code_line`, `code_lines`, `workflow_step` and `step_running` over fixtures and nothing else, and `tests/test_the_suite_runs_with_gh_logged_out.py` reads what the conftest does to `gh`'s login. `tests/test_conftest.py` declares `TARGET = "tests/conftest.py"`, so these cases have a rule 1 file, but Batch B's list was the shipped modules, `git ls-files '*.py'` less `tests/` (`plan.md` phase 6), and no group drew from them. Placing them is a move phase 7 was not asked to make, so they stay, and `overview.md` names them.

### The suite's wall time, before and after

Both runs are `bin/test -q`, the parallel runner on its default `-n auto`, on one macOS arm64 machine of 12 cores, one after the other with nothing else of this session running, and both on the worktree's `.venv` (`executed`). The wall seconds are the shell's, from just before `bin/test` to its exit; pytest's own figure is beside them.

| Run | Tree | Collected | Passed | Failed | Skipped | Wall | pytest | Load average before, 1 / 5 / 15 min | After |
|---|---|---|---|---|---|---|---|---|---|
| before | an archive of 6046f062, where #942 left `release/v0.22.3`, committed once as a repository of its own | 7,494 | 7,478 | 2 | 14 | 183.9 s | 183.31 s | 2.76 / 3.05 / 3.19 | 10.13 / 7.66 / 5.17 |
| after | the worktree at 6a54be98 | 7,726 | 7,711 | 1 | 14 | 91.4 s | 91.07 s | 7.68 / 7.26 / 5.08 | 10.83 / 8.87 / 5.94 |

The archive was committed once (`git init`, `git add -A`, one commit, driven from Python) because the suite reads its own tracked files through git, and a tree git does not track would fail those cases for a reason neither tree has. The worktree's `.venv` was linked in and excluded in the archive's `.git/info/exclude`, so the archive's status read clean.

**The failures** (`executed`). Before, both are the archive's and not the base's: `tests/test_gate_judges_the_repo_it_commits_to.py::test_the_same_root_forms_answer_what_the_release_did` says "no tag is reachable from HEAD", and `tests/test_release_hygiene.py::test_this_checkout_has_tags_to_read_the_shipped_set_from` says "no `v*` tag is readable from this checkout". A repository of one commit has no tag. After, the one failure is `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite`, the known red until part 2: 5,713 of the 7,726 collected cases have no price in `.test_durations`, and 3,780.4 s of its 3,996.6 s belong to 5,263 ids the suite no longer collects. No case printed a slow-case line.

**What the figures say.** The after run took half the before run's wall time, over 232 more collected items. It started at a higher one-minute load, 7.68 against 2.76, because the before run had ended a minute earlier; a higher load can only slow a run, so the load did not flatter the after figure. One run on each side is one sample on a shared machine, where `phases/phase-6.md` *The phase's close* saw one tree's figure move by up to three times, and the CI legs' minutes are the measurement `questions.md` Q5 waits on.
