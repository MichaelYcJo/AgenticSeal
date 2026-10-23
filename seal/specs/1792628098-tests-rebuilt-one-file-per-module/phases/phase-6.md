# Phase 6: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | not closed; its first step is 6e7214be |

## What this phase was asked

The first step: `bin/test-layout --moved <base> --from <old file>... <new file>` in `skills/verify/scripts/test_layout.py`, with `tests/test_test_layout.py::Test_moved` seen red first (S11), the mode named in `bin/test-layout`'s comment and the script's docstring, and the record-shape bullet of `CONTRIBUTING.md` *The test layout* rewritten in place: the mutant table is the part of a record whose module the check did not pass, the sentence `about 30 per module` gives way to the rule `spec.md` *The proof of equal protection* states, and the clause `before the old cases are read` is dropped. Then Batch B, every remaining shipped module, one commit per shipped directory in `plan.md`'s order, `hooks/` first, stopping at a directory boundary. Per module the move check runs: where it exits 0 the record holds its command and last line, and where it exits 1 the module runs the mutation proof as in phase 5.

## What this phase found

**Whether the frame holds.** It holds for the move check as built. It does not hold for Batch B as the frame expects the check to be used, below.

**The move check, at 6e7214be** (`executed`, macOS arm64). `test_layout.py` gains `moved`, the pure reading of the body and fixture conditions, and `_moved_main`, which reads the old files with `git show`, collects both sides with pytest and prints the result. The three conditions are `spec.md`'s, with these readings the build took:

- The census case is left out on both sides of the count, not on the new file's alone. A phase 5 file that gains moved cases is named in `--from` too, and at the base it already holds its census case.
- A case requests a fixture by a parameter, by a `usefixtures` mark on the case, on its class or in the file's `pytestmark`, and as an autouse fixture of its class, its file or `tests/conftest.py`. The names a `parametrize` mark hands a case are not fixtures. The two cases must request the same names, and each name, followed through the fixtures it requests, must be defined alike in both trees. A case moved out of a class that carried `usefixtures` therefore fails, though its body is unchanged.
- A fixture is read in the case's class, then its file, then `tests/conftest.py`, as `spec.md` says. A conftest under a subdirectory of `tests/` is not read; none exists at 6e7214be. A fixture renamed through `name=` is read under its function's name; no test file uses `name=` (`git grep`, `executed`).
- `questions.md` Q6 and Q7 are built on their defaults: the base is collected in a detached worktree, removed by its own path with `git worktree remove --force` before the check ends, and a name no tree defines is pytest's own.
- pytest runs on the interpreter running the check where it has pytest, and on the repository's `.venv` otherwise, because `bin/test-layout` runs on the system `python3`, which has no pytest on this machine (`executed`). Neither found is exit 2.
- `--from` takes every word after it, so the new file, written last, is taken as its last word. That is the spelling `spec.md` gives.

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

**Batch B does not start in this spawn.** `hooks/`, the first directory, holds 34 shipped modules, three of them rebuilt in phase 5: `hooks/commit-review-gate.py`, `hooks/worktree-guard.py` and `hooks/root-migrate.py`. A scan of the 136 test files that declare no `TARGET` (`executed`, a script outside the tree that reads each file for a `hooks/` module's file name or import) finds 57 that name a `hooks/` module, 35 of them naming two or more. The directory also holds `hooks/cmdline.py`, whose cases phase 5 left in the commit gate's three text-reading files. One commit for the directory with complete records is more than this spawn can finish, so it stops at the directory boundary.

**What the frame's check cannot pass.** The count condition compares the new file with the whole of each `--from` file. An old file whose cases belong to two modules is split between two new files, and neither new file can then pass: each holds fewer items than the old file. So every module whose old cases share a file with another module's falls to the mutation proof, however its cases were only moved. If most of the 35 files above do split, the mutants `plan.md` *Alternatives considered* dropped for moved modules come back for most of `hooks/`. A check that takes several new files and compares their union with the old files would pass a split; `spec.md` *Data & interfaces* gives `--moved` one new file, so this phase did not build it. The question is the framer's and the orchestrator's.

**The boundary** (`executed`). At the tree committed as 6e7214be, one `bin/test ... -q` over 42 modules: `tests/test_test_layout.py`; every test file naming `test_layout`, `test-layout` or `CONTRIBUTING`; `tests/test_censuses.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_conftest.py` and every other file `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists. 2,536 passed in 35.7 s. The shards module over the whole collection, `bin/test tests -q -k test_the_windows_leg_runs_in_shards_that_make_the_whole`: 32 passed and 1 failed, `test_the_durations_file_prices_the_suite`, the known red until phase 7. `bin/test-layout --check` exits 0 with 153 files read, 0 refused and 137 declaring no `TARGET`; `bin/rules --check` exits 0 with 249 check lines; `bin/unverified-check seal/specs/` exits 0. Ruff checks and formats `skills/verify/scripts/test_layout.py` and `tests/test_test_layout.py` clean, one file per run, and `--pairs` names 0 pairs in `tests/test_test_layout.py`.
