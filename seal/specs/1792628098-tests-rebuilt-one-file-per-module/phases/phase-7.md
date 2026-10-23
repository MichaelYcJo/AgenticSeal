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
