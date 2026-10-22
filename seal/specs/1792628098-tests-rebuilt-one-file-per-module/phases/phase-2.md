# Phase 2: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 243dc28f |

## What this phase was asked

`SLOW_CASE_S` and a terminal-summary report in `tests/conftest.py` in place of the failing ceiling and its environment variable; `tests/test_conftest.py` under the layout, taking the slow-case module's cases; one row per test file in `.github/scripts/release_report.py`, with its cases in `tests/test_release_report.py`; the `CONTRIBUTING.md` paragraph on a case's budget rewritten in place to the report. `docs/release-checklist.md` changes through the spec's `## Rule changes`, which this phase does not edit. S6 and S7 are seen red first, and `release_report.py --against v0.22.2 --at <archive>` prints the rows locally.

## What this phase found

**Measured at 27fefa61, before the first edit** (`executed`).

- `git grep -l "CASE_CEILING_S\|SPECSEAL_CASE_CEILING_S\|over_the_ceiling\|ceiling_from" -- ':!seal/specs' ':!changelog'` prints 4 files: `.test_durations`, `CONTRIBUTING.md`, `tests/conftest.py` and `tests/test_a_slow_case_names_itself.py`. The ceiling starts at `tests/conftest.py` line 855 and its hook at line 896; the frame named lines 856 to 910.
- `tests/test_a_slow_case_names_itself.py` holds 8 cases, all 8 priced in `.test_durations`.
- `.github/scripts/release_report.py#suite_seconds` stands at line 102. `git grep -l release_report -- tests` prints 2 modules; no `tests/test_release_report.py` exists.
- The `from` sentence of the spec's first rule change reads at `docs/release-checklist.md` lines 174 to 175, word for word once whitespace is collapsed.
- The last release tag is v0.22.2.

**Whether the frame holds.** It holds, with three places where the tree asked for something the frame did not say.

- One case of the slow-case module was not `conftest.py`'s. `test_every_pytest_leg_has_a_timeout_and_the_job_reads_it` reads `.github/workflows/test.yml`, and it already imported its readers from `tests/test_ci_gives_the_checks_what_they_need.py`. It moved there, to the cases that read the same workflow, and not to `tests/test_conftest.py`.
- The ceiling failed a slow passing call and left a failing one its own report. The report names every call past `SLOW_CASE_S`, passing or failing: a report has no outcome of its own to protect.
- `.test_durations` lost the slow-case module's 8 ids through one `Edit`, whose match on the 8 lines is what asserts each id was present. The frame names a script, and the prompt for this build forbids a script that writes a repository file.

**The cases, and how each was seen red** (`executed`). Against the tree before the change, `tests/test_conftest.py` and `tests/test_release_report.py` failed 6 of their 8 cases. The two that passed are refusals of a state the old code also refused: the quick case not named, and the exit on an unreadable tree. `bin/mutation-check` turned each red.

| # | Mutation | Cases | Verdict |
|---|---|---|---|
| c1 | a setup report read as a call | `tests/test_conftest.py` | red |
| c2 | a call at `SLOW_CASE_S` named | `tests/test_conftest.py` | red |
| c3 | the slowest call printed last | `tests/test_conftest.py` | red |
| c4 | the summary writes no line | `tests/test_conftest.py` | red |
| c5 | every call named, quick or slow | `tests/test_conftest.py` | red |
| r1 | a file's cases counted twice | `tests/test_release_report.py` | red |
| r2 | a file's seconds not summed | `tests/test_release_report.py` | red |
| r3 | the rows sorted fastest first | `tests/test_release_report.py` | red |
| r4 | seconds printed without their decimal | `tests/test_release_report.py` | red |
| r5 | `main` prints no file table | `tests/test_release_report.py` | red |
| r6 | `main` goes on past an unreadable tree | `tests/test_release_report.py` | red |
| r7 | a durations file that is no object read | `tests/test_release_report.py` | red |
| r8 | the file table's separator row dropped | `tests/test_release_report.py` | SURVIVED, then red after 243dc28f |
| r9 | the suite's seconds read through `durations` dropped | `tests/test_the_release_table_reads_two_trees_and_fails_nothing.py` | red |

r8 survived the first run: no case read the separator. 243dc28f reads the header, the separator and the first row as one block, and r8 is red against it. `git status` was clean after every run.

**The modules' cost** (`executed`, macOS arm64, `-p no:xdist`). `tests/test_conftest.py` runs 4 cases in 0.75 s, most of it the one inner pytest run its module-scoped fixture builds once. `tests/test_release_report.py` runs 4 cases in 0.02 s. The slow-case module it replaces priced at 2.92 Windows seconds in `.test_durations`.

**The release table locally** (`executed`). `python3 .github/scripts/release_report.py --against v0.22.2 --at <archive>`, the archive written by `git archive v0.22.2`, exits 0 and prints 145 file rows under `### Test files against v0.22.2`. The first is the sealer's file at 376 cases and 691.5 s at v0.22.2 and 373 cases and 761.1 s now. `tests/test_a_slow_case_names_itself.py` prints 8 cases and 3.2 s at the tag and absent now.

**`docs/release-checklist.md`** is not edited here: the spec's `## Rule changes` holds both changes for `settle` to apply, and `chain_check.py` parses them at the pull request. The first change's `from` sentence matches the section as it reads at 243dc28f.

**The phase boundary** (`executed`, at 243dc28f). One `bin/test ... -q` over 117 modules: phase 1's 69, the four this phase wrote or changed, and every module that imports `conftest` or names `release_report`. 6,836 passed, 16 skipped and 1 failed, the same overview census as phase 1's boundary, for the same reason. No case was named slow. `bin/test tests -q -k test_the_durations_file_prices_the_suite` passes on the pruned file. `bin/rules --check`, `bin/unverified-check seal/specs/` and `chain_check.py --baseline release/v0.22.3 --worktree` each exit 0.
