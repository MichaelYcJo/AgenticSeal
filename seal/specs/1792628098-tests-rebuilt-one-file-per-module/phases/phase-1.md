# Phase 1: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | cbf6ef6f |

## What this phase was asked

The layout check: `skills/verify/scripts/test_layout.py`, run as `bin/test-layout` with its `.cmd` twin, and `tests/test_test_layout.py` declaring `TARGET`, with one suite case that runs `--check` over `tests/` without `--all`. `CONTRIBUTING.md` *The test layout* states the four rules and the record shape. The sentences in `agents/smith.md` and `agents/warden.md` that send a reader to the pairs a duplicate check names get the command's name. S1 to S4 are seen red first. `bin/test-layout --check` exits 0 and prints the count of files that declare no `TARGET`. The frame was written at a16acb40, so the phase first recomputes its facts at HEAD and builds on the tree where the two differ.

## What this phase found

**Measured at dc517d8b, before the first edit** (`executed`).

- `git ls-files 'tests/test_*.py' | wc -l` prints 145. The frame counted 148 at a16acb40, before #1005 merged.
- `git grep -l '^TARGET = ' -- tests/` prints 1 file, `tests/test_what_the_reader_understands.py`. Its `TARGET` is a path constant and not a declaration: the first assignment after its imports is `reader`.
- `grep -n 'duplicate check' agents/smith.md agents/warden.md` puts the smith's sentence at lines 98 to 101 and the warden's at lines 135 to 138. The frame names line 131 for the warden; the sentence moved when #1005 merged.

**Whether the frame holds.** It holds, with four places where its text and the tree disagree or where the text allows two readings. The build took the reading below in each.

- Twins. `spec.md` lists a twin among the failures of `--check`, and the plan asks `--check` to exit 0 in this phase and to list the twins in phase 4's first step. The tree holds 46 twin groups today, so both cannot hold if every twin fails. The script refuses a twin where one of its files declares `TARGET`, or under `--all`, and reports every other twin. Phase 4's first step reads that report.
- Pairs. The frame names two cases calling the function with equal argument expressions. Read literally, every two cases that pass a local of one name, such as `source`, are a pair, and the first run named 7 pairs in this phase's own file, none of them real. An argument that reads a name the case assigns or takes as a parameter is not compared. The script's docstring says so, and `Test_pairs` holds it.
- Classes the rule does not name. `Test_module` needs no accepting and refusing pair, because it is no function's class. A file under `tests/e2e/` is not held to the stem rule, and every one of its classes keeps the pair. A file whose `TARGET` is a document is held to neither the stem rule nor the class rule.
- `spec.md`'s `## Removes` names three rules under the new heading and `plan.md` names four. `CONTRIBUTING.md` *The test layout* states four: the layout, the verdicts, when a module is written anew, and what a rewritten module may cost, with the record shape after them.

**What the check prints over today's `tests/`** (`executed`, at cbf6ef6f). `bin/test-layout --check` exits 0 and ends `test-layout: 146 files read, 0 refused, 145 declare no TARGET`. Above that it prints 145 `declares no TARGET` lines and 46 twin lines, every one a report. `bin/test-layout --pairs` prints `test-layout: 146 files read, 0 pairs`: no old file has a `Test_<name>` class yet.

**What else the boundary run asked of the change.**

- `tests/test_a_reference_root_is_read_and_never_taken.py` classifies every command in `bin/`, and `test-layout` takes a row: it walks no `specs/` directory.
- `tests/test_every_reader_ends_a_line_where_gfm_does.py` refused `.splitlines(` in the twin reader. The reader now takes a definition's text through `ast.get_source_segment`, which counts lines the way the parser does, and needs no entry in `OUT_OF_CLASS`.
- `tests/test_no_passage_is_pasted_into_a_second_file.py` refused one sentence added to both agent files. The warden's sentence is worded apart from the smith's.

**Seen red** (`executed`). Before the script existed, `bin/test tests/test_test_layout.py -q` stopped at collection with `FileNotFoundError` for the script. After it, each refusal was broken in turn by `bin/mutation-check` with the module's cases as the command, `bin/test tests/test_test_layout.py -q -p no:xdist`. S1 is m14, S2 m15, S3 m10, m11 and m22, S4 m25 and m27.

| # | Mutation in `skills/verify/scripts/test_layout.py` | Verdict |
|---|---|---|
| m1 | the declaration's name not compared with `TARGET` | red |
| m2 | a non-string value read as a declaration | red |
| m3 | the module docstring not skipped | red |
| m4 | the imports not skipped | red |
| m5 | a hyphen kept in the stem | red |
| m6 | the parent not put before a shared stem | red |
| m7 | a document given a file name | red |
| m8 | a function read as a class | red |
| m9 | a `test_` function read as a helper | red |
| m10 | one file's second definition read as a twin | red |
| m11 | a definition in one file read as a twin | red |
| m12 | an untracked `TARGET` passed | red |
| m13 | a wrong file name passed | red |
| m14 | a class naming no definition passed | red |
| m15 | a class without its pair passed | red |
| m16 | `Test_module` held to the pair | red |
| m17 | a document's classes held to the pair | red |
| m18 | a flow's file held to the stem rule | red |
| m19 | an undeclared file reported under `--all` | red |
| m20 | a function with a class reported as without one | red |
| m21 | a private function reported | red |
| m22 | a twin beside a declared file reported | red |
| m23 | names not normalised in a body | red |
| m24 | strings not normalised in a body | red |
| m25 | an argument reading a local compared | red |
| m26 | a method call not read as a call of the function | red |
| m27 | equal bodies not compared | red |
| m28 | `--check` exiting 0 on a refusal | red |
| m29 | `--all` taken without `--check` | red |
| m30 | a directory outside a repository read | red |
| m31 | a definition's decorators left out of its text | red |

`git status` was clean after every run.

**The module's cost** (`executed`, macOS arm64). `bin/test tests/test_test_layout.py -q` runs 31 cases in 7.48 s, most of it the parallel runner starting; under `-p no:xdist` the cases take 0.7 s. One case runs git, the suite case over `tests/`. Every other case reads fixture text.

**The phase boundary** (`executed`, at cbf6ef6f). One `bin/test ... -q` over 69 modules: this module, every module that reads `CONTRIBUTING.md`, `agents/smith.md`, `agents/warden.md` or the scripts in `bin/`, every module `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists, and the ten meta modules. 3,962 passed, 11 skipped and 1 failed. The failure is `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`: this work item holds `spec.md` and no `overview.md`, as it did at dc517d8b, and the orchestrator's prompt puts `overview.md` after phase 7. `bin/rules --check`, `bin/unverified-check seal/specs/` and `chain_check.py --baseline release/v0.22.3 --worktree` each exit 0.
