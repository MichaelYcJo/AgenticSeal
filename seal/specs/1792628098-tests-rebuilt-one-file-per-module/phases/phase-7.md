# Phase 7: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | 3c6b9e0d; its first step is cc391101 |

## What this phase was asked

The spawn ran in two parts. Part 1: S14 first, `--moved` in `skills/verify/scripts/test_layout.py` dropping the docstring of every function and class a compared case or fixture defines, through one function `_moved_form` that `_resolver` also calls, with S14's rows of `tests/test_test_layout.py::Test_moved` seen red against the script at 9e92e4e8, the script's docstring and `_moved_form`'s rewritten in the same commit, the changed code's mutants in one `bin/mutation-check` batch, and group 44's move check re-run to confirm it names no failure for `test_one_open_issue_closes_it_and_opens_the_next`. Then S10 under `questions.md` Q9's default: `bin/test-layout --check --all`, and the suite case given `--all` only where it exits 0, or else `overview.md` *Not done* naming each undeclared file and why it stays. Then the overview's rows for the framer closed against 9e92e4e8. Then the suite's wall time measured locally the same way twice, `bin/test -q` in an archive of the base where #942 left `release/v0.22.3` and in the worktree, with the pass, fail and skip counts and the load average at each run. Part 2, after the orchestrator's CI run 39964746967 at b2c300c9: first, the cases whose subject is a `tests/conftest.py` helper moved from the three undeclared files part 1 found into `tests/test_conftest.py`, as phase 6's groups moved theirs, by the move check and the mutants only where it fails, one commit and its record, a case that checks across files or reads prose staying with its reason in `overview.md` *Not done*; then `.test_durations` replaced from that run's `test-durations` artifact, the closing memo with the wall times before and after and the CI wall time per leg, phase 7's Status in `plan.md`, and `handoff.md` naming round 3 as next.

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

### The conftest helpers' cases, at 099cd54d

**Whether the frame holds** (`read`). It holds for two of the three files. `tests/test_a_workflow_is_read_the_one_way.py` and `tests/test_the_suite_runs_with_gh_logged_out.py` are named by no `check:` line, and no `check:` line states the rules their moving cases hold: `CONTRIBUTING.md` *Running the checks* states the logged-out rule with no `check:` line under it (`executed`, `grep` over the rule files). It does not hold for `tests/test_a_shrunken_corpus_declines_to_judge.py`. `docs/release-checklist.md` line 134 names that file for *A sweep that walks a git listing judges what remains instead of stopping at the first tracked file the disk lacks, and a case whose verdict needs the whole corpus says so*, and its cases of `on_disk`, `shrunken_corpus` and `decline_if_shrunken` hold that rule. `plan.md` phase 6 lets a group move only once every `check:` line whose rule its moving cases hold has its item in `spec.md` *Rule changes*, and the line has none, so those eight cases stay until the framer writes one naming `tests/test_conftest.py` beside the file.

**The cases** (`executed`). Into `tests/test_conftest.py`, bodies unchanged:

- From `tests/test_a_workflow_is_read_the_one_way.py`, all five, with `WORKFLOW` and its comment: `Test_step_running` takes `test_accepts_the_step_a_comment_naming_its_script_cannot_move`, renamed from `test_a_comment_naming_a_script_cannot_move_the_step`, and `test_refuses_a_layout_that_is_not_exactly_one_step`, renamed from `test_a_reader_that_does_not_find_exactly_one_step_says_so`, whose rows call `step_running` twice and `workflow_step` once. `Test_module` takes `test_one_rule_says_what_a_comment_is` (`code_line`), `test_a_step_is_found_by_its_name_and_ends_at_the_next_one` (`workflow_step`) and `test_every_step_of_every_job_is_read_and_a_nameless_one_has_none` (`workflow_steps`). Each of those three is its function's one case, so no class of `code_line`, `workflow_step` or `workflow_steps` could hold the pair `bin/test-layout --check` asks of a function class. The file is emptied and removed: no `check:` line names it.
- From `tests/test_the_suite_runs_with_gh_logged_out.py`, the block's two cases, `test_the_conftest_takes_every_gh_login_away` and `test_the_token_gh_would_send_is_not_a_login`, into `Test_module`, with `HERE`, `CONFTEST`, `TOKENS`, `NOT_A_GH_TOKEN` and `PROBE`. The block runs at import and is no function. `test_contributing_says_the_suite_runs_logged_out` reads `CONTRIBUTING.md` and stays for #923, and takes `TOKENS` from `tests/test_conftest.py` by import.

`tests/conftest.py`'s comment above `code_line` and `tests/test_the_rules_claude_md_names_have_one_home.py`'s `LINKED` and `CARRIERS` name `tests/test_conftest.py` where they named the removed file, because the workflow fixture's comment citing `CONTRIBUTING.md` *House rules* moved with it. That comment was re-wrapped so the section's name stands on one line: the home file's case reads the file flattened, and `*House` and `rules*` on two comment lines read as `*House # rules*`, which failed `test_every_linked_file_names_each_home_and_section` once before the commit.

**The move check** (`executed`): `bin/test-layout --moved HEAD --from tests/test_conftest.py tests/test_a_workflow_is_read_the_one_way.py tests/test_the_suite_runs_with_gh_logged_out.py --to tests/test_conftest.py tests/test_the_suite_runs_with_gh_logged_out.py`, HEAD at b2c300c9, ends `test-layout: moved: 15 old cases, 27 items against 27 at b2c300c9c8ea, 0 failed`, exit 0. No mutants run; `--pairs` names none in `tests/test_conftest.py`.

**Cases and seconds** (`executed`, serial): 28 items in 4.55 s before, in an archive of b2c300c9 with the worktree's `.venv`; 28 in 4.81 s after.

**The real-git cases kept.** None of the moved cases runs git. `test_the_token_gh_would_send_is_not_a_login` runs `gh auth token`, and skips where `gh` is absent.

**The boundary** (`executed`). At the tree committed as 099cd54d, before the commit over the same bytes: `tests/test_conftest.py`, `tests/test_the_suite_runs_with_gh_logged_out.py`, `tests/test_the_rules_claude_md_names_have_one_home.py`, `tests/test_test_layout.py`, `tests/test_chain_hooks_hardening.py` and the 19 test files `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists, `tests/test_censuses.py` and `tests/test_a_shrunken_corpus_declines_to_judge.py` among them: 2,417 passed and 3 skipped. The shards module over the whole collection: 17 passed and `test_the_durations_file_prices_the_suite` failed, the known red. `--check` exits 0 with 184 files read, 0 refused and 115 declaring no `TARGET`, and `--check --all` refuses those 115; `bin/rules --check` and `bin/unverified-check seal/specs/` exit 0; ruff checks and formats each changed Python file clean, one file per run.

### `.test_durations` from CI, at 3c6b9e0d

**The artifact** (`executed`). `gh -R MichaelYcJo/SpecSeal run download 39964746967 -n test-durations -D <scratch>` gave one `.test_durations` of 7,726 ids priced at 1,662.0 s, with LF line ends, and it was moved over the committed file. The committed file it replaced priced 3,996.6 s, of which 3,780.4 s belonged to 5,263 ids the suite no longer collects.

**What the durations case reads** (`executed`, against the tree after 099cd54d). `bin/test tests -q -k test_the_durations_file_prices_the_suite` passes: 1 passed. Of the 7,726 collected cases, 19 have no price, 0.25%, and they are exactly the cases 099cd54d moved into `tests/test_conftest.py`, priced in the artifact under their old ids. Those 19 old ids are 7.8 s of the file's 1,662.0 s, 0.47%, under `STALE_SHARE`'s 5%. `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -p no:xdist` gives 16 passed and 2 skipped: run alone, the module skips the two cases that need the whole collection, which the `-k` run over `tests` gives them.

**CI run 39964746967 at b2c300c9** (`executed` by the orchestrator for the verdicts; the seconds by this smith, `gh run view 39964746967 --json jobs`, each job's start to its end). Every job passed except the durations case on the legs whose shard holds it.

| Job | Conclusion | Seconds |
|---|---|---|
| pytest, macOS, group 1 of 3 | success | 125 |
| pytest, macOS, group 2 of 3 | success | 126 |
| pytest, macOS, group 3 of 3 | failure, the durations case | 85 |
| pytest, ubuntu | failure, the durations case | 142 |
| pytest, Windows, group 1 of 4 | success | 201 |
| pytest, Windows, group 2 of 4 | success | 133 |
| pytest, Windows, group 3 of 4 | success | 184 |
| pytest, Windows, group 4 of 4 | failure, the durations case | 118 |
| lint | success | 8 |
| durations | success | 10 |
| arm-check-grammar, 3.13 and 3.14 | success | 26 and 22 |
| release-report | skipped | |

The run took 219 s from its creation to its last job. No run of the base was timed the same way, so these figures are the after side of `questions.md` Q5 alone.

### The phase's close, at 3c6b9e0d

`plan.md`'s Status cell for phase 7 holds 3c6b9e0d, the last build commit. S14 holds, and group 44's move check passes. S10 stays open under Q9's default with 115 undeclared files, each named in `overview.md` *Not done* with the reason it stays. The shrunken-corpus file's eight helper cases wait on a *Rule changes* item for `docs/release-checklist.md` line 134, which is the framer's. `test_the_durations_file_prices_the_suite` passes, and `bin/test tests/test_test_layout.py -q` gives 55 passed (`executed`).
