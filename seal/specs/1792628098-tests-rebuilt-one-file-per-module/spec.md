# Feature Specification: tests rebuilt one file per module (#942)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A test is a mechanism. A case stays while the mutation table shows what it kills that no other case kills. Nothing is kept beside the tree to stay in step with it, so a census's stored exception list goes where a fact in the code can replace it |
| `CLAUDE.md` *The goal a design is chosen against* | The checks this work adds fail on a fact they read and report the rest. A report never stops a pull request to ask |
| `CONTRIBUTING.md` *What a change to a gate must carry* | Removing the commit gate's text reading changes what the gate allows. That bar is why the removal is a person's decision in `questions.md` and not this work's default |
| `docs/the-commit-gate-inside-git.md` *Where each state of a repository stands* | Names the states only the PreToolUse reading judges: a foreign hooks slot and an opted-in clone no session has reached. These are what the reading catches that git cannot |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below names every removal once |
| `docs/release-checklist.md` *5. The release pull request* | The release table is where the per-module rows land, and the sweep is a step of that section |
| `skills/settle/SKILL.md` *Rule changes* | The grammar `## Rule changes` below is written in |
| `skills/agent-contract/SKILL.md` sections 2 and 15 | The smith runs the module it touches, never the suite. A new case is seen red before it is committed |
| `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-1.md` | The worked example of a file cut by a sampled set and a mutation table, and the shape of the record each batch here writes |
| `seal/specs/1790815613-a-gate-decides-at-the-moment-of-the-action-not-from-the-text/spec.md` *What the tree answered* item 1 | The static reading of shell text is the stopped class. This work adds no rule to it and samples its tests |

## Measured at a16acb40

Each figure was executed by the framer on 2026-10-22 in the worktree, unless labelled read.

- 148 test files, all directly under `tests/`; no `tests/e2e/` exists.
- 108,791 lines of test code against 48,932 lines of shipped Python (every `.py` outside `tests/` and `.venv/`), a ratio of 2.2.
- 7,466 cases collected (`bin/test --collect-only -q -p no:xdist`); 3,621 `def test_` lines.
- `.test_durations` (read) prices 7,284 cases in 142 files at 3,999.5 Windows seconds. Sixteen files price at a minute or more; together they hold 3,071.2 of those seconds and 2,655 of those cases. The five heaviest are the sealer file at 761.1 s, the commit-gate file at 519.7 s, and the three text-reading files at 279.1 s, 242.8 s and 203.9 s.
- Helper twins: 46 distinct non-test function bodies are defined byte-identically in two or more test files, 141 definitions in all, 632 lines of which 396 are beyond one copy. The most copied names are `read` (39 definitions) and `flat` (16). No `git init` helper body is a twin. The issue's 249 twins and 1,413 lines were measured before #929 and #944.
- Shipped units: 1,306 top-level functions and classes in 72 shipped `.py` files; 404 are named in no test file's text. The three files with most unnamed units are `hooks/cmdline.py` (34), `skills/code-review/scripts/chain_check.py` (28) and `hooks/worktree-guard.py` (23).
- `tests/undeclared_readers.txt` is gone, and `agents/smith.md` line 98 and `agents/warden.md` line 131 already carry the group sentences. #923 did both.

## Scope

The work is four rules the smith applies to any module without asking, the two checks and one report that hold them, and the module batches that apply them. This frame fixes the layout, the rules and the order of work. It does not fix per-module case lists, counts or call sites: each phase's first step recomputes those at the tree it builds on, because #988, #1009 and #1005 merge before the smith starts.

### Rule 1, the layout

- One test file per shipped module: `tests/test_<stem>.py`, where `<stem>` is the module's file name without `.py` and with each hyphen written as an underscore. Where two shipped modules share a stem, each file name takes the parent directory before the stem. The target is declared once, as the first assignment after the imports: `TARGET = "<tracked path>"`. A file whose cases run a `bin/` command names the script the launcher runs.
- Inside a file, one class per public top-level function of the target (one whose name does not start with an underscore), named `Test_<function>` with the function's name spelt as the code spells it; a private function gets a class where a case needs one. Behaviour of the module as a whole sits in `Test_module`. A function's class holds at least one case whose name starts with `test_accepts_` (the behaviour on good input) and one whose name starts with `test_refuses_` (the refusal or error on bad input). Other cases in the class take any `test_` name.
- A flow across modules lives under `tests/e2e/<flow>/`, its `TARGET` names the command or hook the flow starts from, and its classes are scenarios that keep the accepting and refusing pair. The commit gate run through real git is the first flow.
- A case whose assertion reads a shipped document names that document as `TARGET`; its classes are free-named. Such cases are #923's and this work moves none of them.
- A helper used by two files is defined once, in `tests/conftest.py`. The fixture repositories a module needs are built once per module by a module-scoped fixture and copied for each case; the copy is the reset.
- The censuses are cases of each module's file: `tests/censuses.py` holds one function per census that judges one file, and each module file ends with `test_census = census_case(TARGET)` from `tests/conftest.py`, so running a module's tests runs every census over its target. A census's exemption is a comment line of its own, directly above the exempted line, because `ruff format` moves a comment written at the end of a line; the census reads it, refuses one above a line the census would not have flagged, refuses one written at the end of a line, and reads no comment that has no reason after its colon. No census keeps a list of exemptions in a test file. A tracked file whose module file does not yet declare it is judged by the sweep in `tests/test_censuses.py`, one git listing per run.

### Rule 2, how each existing case is classified

The smith reads the target's functions first and lists the classes the file must have. Then every old case that exercises the target gets one verdict and no second one:

| Verdict | When | What the batch records |
|---|---|---|
| place | the case fits a class as it is | nothing |
| merge | a case of the class already covers it, or the pairs report names it with one | the surviving case |
| cut | the mutation table shows every mutation it kills is killed by another case, or the behaviour it guards left the tree | one line: the case name, what it guarded, which case or tree fact now holds it |
| rewrite | the class is written anew under rule 3; the old cases are read for their inputs, then deleted | one line per old case, as for cut |
| to #923 | the assertion reads prose | the case name, in the batch's list left to #923 |

### Rule 3, when a module's tests are written anew from the code

A module's tests are written anew when the old files that exercise it price at 60 seconds or more in `.test_durations`, or when `bin/test-layout --pairs` names a pair inside one of its classes. Every other module's old cases are placed and merged. A module written anew gets its accepting and refusing cases from reading the code, one class per function, and the old cases are read as a reference for inputs. The proof of equal protection below is what shows the new file protects what the old ones did, and rule 4 bounds what the new file may cost.

### Rule 4, what a rewritten module may cost

The target the rebuild works toward is the issue's: the suite's real protection at a fraction of today's time, with no case that runs for tens of minutes and no file or flow that dominates the run. The smith applies this rule while writing each module, and it binds the rewrite and nothing in CI: a time reading is noisy, the per-case ceiling is a report for that reason, and the per-module rows and the release sweep are what act on a slow module after the fact.

- A rewritten module builds its fixture repositories once, in a module-scoped fixture, and resets them between cases by copying; it does not build one per case.
- A case about a reading of a command is judged without real git or a real shell. The real-git rows that stay are the ones showing the reading and git agree, and a batch names them.
- A case does not enumerate a whole input space where a sampled set, one row per kind, holds the same behaviour; the proof of equal protection is what shows it does.
- Each rewritten module's record states its seconds before and after, from `bin/test <files> -q` at the build machine, beside the cases before and after.

### The proof of equal protection

#942 changes no shipped code, so the one risk a rebuilt module carries is a fault the old cases caught and the new ones miss. A sample of mutants at the code's decision points is enough to show that risk, and the owner set its cost on 2026-10-22.

- Where the mutants go: one or two per class, at each public function's decision points, the branches where a case accepts or refuses. That is about 30 per module.
- How the new file's column runs: in one `bin/mutation-check` call carrying every mutant of the module, which runs the baseline once and then each mutant once, stopping each mutant's run at its first failure.
- When the old files' column runs: only for a mutant the new file lets survive. Where the old files miss it too, the record states an old gap. Where they kill it, the smith adds a case to the new file and sees it red on that mutant before the batch commits.
- What the record carries: the table of mutants with the new column's verdict, the old column's verdict where it ran, each old gap, and each case added.

`broad_gate.py` and `seal_stamp.py` ran under the earlier proof, a table of about 100 mutants each run in both columns, and their records stay as they were written. The commit flow's record says at which mutant it switched to this proof.

### What holds the rules

- `skills/verify/scripts/test_layout.py`, run as `bin/test-layout`. `--check` reads every `tests/**/test_*.py` that declares `TARGET` and fails on: a `TARGET` git does not track, a file name that does not match it, a `Test_<function>` naming no top-level definition of the target, a function class lacking the accepting or refusing case, a non-test top-level function whose source is byte-identical to one in another test file where one of the two files declares `TARGET`. It prints the files that declare no `TARGET` and every twin between two undeclared files, and with `--all` fails on both. It prints each public top-level function of the target that has no class, and fails on none. `--pairs` prints, for each class, two cases that call the target's function with equal argument expressions, or whose bodies are equal once names and string constants are normalised, and exits 0 whatever it prints. A call with an argument that reads a name the case assigns or takes as a parameter is not compared at all: its input is on disk or in a fixture, where the report cannot see it.
- `tests/test_test_layout.py` holds the script's own cases on fixtures, and one case that runs `--check` over this repository's `tests/`; the last phase gives that case `--all`.
- `.github/scripts/release_report.py` prints, under its existing table, one row per test file: priced cases and seconds in `.test_durations` at the pull request head and at the last release tag, sorted by seconds. It reads the two trees it already reads and nothing else.
- `tests/conftest.py` prints each case whose call ran past `SLOW_CASE_S` (90 seconds) in the terminal summary and fails nothing. `SPECSEAL_CASE_CEILING_S` is not read. The legs' `timeout-minutes` in `.github/workflows/test.yml` stay.

### What the frame decided on the issue's questions

- Question 5, the commit gate's text reading: it stays, and its three files are cut on #929's pattern, a sampled row per kind with a mutation table. The reading alone judges the two states `docs/the-commit-gate-inside-git.md` names and the stub-removal escape in its known limits; no record since #692 names a commit it caught (three records mention the reading, executed grep over `seal/specs/179[12]*/rounds`, `overview.md` and `phases`); the tree holds no count of installs in either state. Removing it allows more, which is the gate bar's costly direction, so the removal is `questions.md` Q1 with a default of keep.
- Question 6: decided by the owner, built as above.
- The censuses: a census moves into `tests/censuses.py` and runs per module through `test_census` when it judges one file by reading that file alone. A check that reads a document's prose, compares files with each other, derives a set across files, or judges records or markdown against an oracle stays where it is. `tests/test_censuses.py` sweeps every tracked file whose module file does not declare it, so a document and a module not yet rebuilt keep their censuses. The stored lists `OUT_OF_CLASS` (two blocks), `ALLOWED`, `ENTRY_POINTS_CLASSIFIED`, `COORDINATE_EXEMPT` and `HEADING_EXEMPT` become comment lines above the exempted lines. The `Reads:` census is already gone.
- The release sweep: `docs/release-checklist.md` section 5, through `## Rule changes` below.

### Out

- Cases whose assertion reads this repository's prose: #923. Each batch lists the ones it left.
- Which CI legs a pull request runs: #943. `.test_durations` cadence: #931.
- Removing the text reading itself: a work item of its own if Q1 is answered remove.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a misplaced test is refused | Given a test file declaring `TARGET` whose class names no function of the target, when `bin/test-layout --check` runs, then it exits 1 and names the file and class | `tests/test_test_layout.py`, seen red by removing the refusal |
| S2 a class without its pair is refused | Given a function class with only `test_accepts_` cases, when `--check` runs, then it exits 1 naming the class and the missing kind | `tests/test_test_layout.py` |
| S3 a twin is refused | Given two test files defining one helper byte-identically, one of them declaring `TARGET`, when `--check` runs, then it exits 1 naming both | `tests/test_test_layout.py` |
| S4 a likely pair is named, not refused | Given two cases in one class calling the function with equal arguments, when `--pairs` runs, then both names print and the exit is 0 | `tests/test_test_layout.py` |
| S5 a rebuilt module protects what the old files did | Given a module's new file and its sample of about 30 mutants at the public functions' decision points, when one `bin/mutation-check` call runs them against the new file, then every mutant is killed, or each survivor is run against the old files and either recorded as an old gap or answered by a case seen red on it | the phase record's table |
| S6 a slow case is reported | Given a case whose call runs past `SLOW_CASE_S`, when the run ends, then one line names it and its seconds and the run exits 0 | `tests/test_conftest.py`, an inner pytest run with the value lowered |
| S7 the release table has module rows | Given `.test_durations` at the head and at the tag, when `release_report.py` runs, then one row per test file prints with cases and seconds at both | `tests/test_release_report.py` on two fixture trees |
| S8 a census runs with its module | Given `tests/test_<stem>.py`, when `bin/test tests/test_<stem>.py` runs, then `test_census` judges `TARGET` under every census | `tests/test_censuses.py` with a fixture target that fails one census |
| S9 a spent exemption is refused | Given an exemption comment line directly above a line no census flags, when the census runs, then it fails naming the line | `tests/test_censuses.py` |
| S10 the whole suite is placed | Given the last batch merged, when `--check --all` runs over `tests/`, then it exits 0 | the suite case in `tests/test_test_layout.py` |

## Data & interfaces

- `bin/test-layout [--check [--all] | --pairs] [paths]`, launched through `hooks/launch.py` like `bin/mutation-check`.
- `tests/conftest.py#census_case(target)` returns the one case; `tests/censuses.py` exposes `def <census>(rel, root=None) -> list[str]`, one per census, where `rel` is the file's path relative to the repository root and `root` is the tree read, the repository root when absent.
- `release_report.py#module_rows(at, now)` reads `.test_durations` in both trees.
- `bin/mutation-check <path> --tests <command> --replace OLD NEW`, with `--replace` given once per mutant: a call with several pairs runs the baseline once, then each mutant once with its run stopped at the first failing case, restores the file after each, prints one verdict line per pair in the order given, and exits 1 where any mutant survived. A call with one pair runs as it does today.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the failing ceiling and its environment variable | `tests/conftest.py#CASE_CEILING_S`, `#ceiling_from`, `#over_the_ceiling`, `#pytest_runtest_makereport` | `SLOW_CASE_S` and a terminal-summary report in the same file; a report needs no raise |
| the slow-case module | `tests/test_a_slow_case_names_itself.py` | `tests/test_conftest.py` under rule 1, except its case that reads the legs' `timeout-minutes` in `test.yml`, which lands in `tests/test_ci_gives_the_checks_what_they_need.py` beside the cases that read the same workflow |
| the stored exemption lists | `tests/test_every_reader_ends_a_line_where_gfm_does.py#OUT_OF_CLASS`, `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py#ALLOWED` and `#ENTRY_POINTS_CLASSIFIED`, `tests/test_a_format_has_one_reader.py#COORDINATE_EXEMPT` and `#HEADING_EXEMPT` | a comment line directly above each exempted line, read by the census in `tests/censuses.py` |
| the helper twins | every non-test top-level function defined byte-identically in two or more files under `tests/` | one definition in `tests/conftest.py` |
| every test file not in the layout | `tests/test_*.py` as they stand at the build's start | `tests/test_<stem>.py`, `tests/e2e/<flow>/`, or the batch's cut lines |
| cases whose kills another case makes, and cases guarding behaviour that left the tree | named per batch in `phases/phase-N.md` | the batch's one line per case |
| the priced ids of removed cases | `.test_durations` | pruned by the smith with one `Edit` per batch, whose match on the removed lines is what asserts each id was present |
| the paragraph heading a case's budget | `CONTRIBUTING.md` *A case has a budget, and so does each leg* | rewritten in place to the report, same section; the four rules and the record shape go under a new heading `CONTRIBUTING.md` *The test layout*, which `.github/scripts/rules.py` reads like every `CONTRIBUTING.md` heading |

## Rule changes

- change
  file: docs/release-checklist.md
  section: 5. The release pull request
  from: each agent's preload bytes, the suite's seconds, each leg's minutes and each document's bytes, beside the same reading at the last release tag.
  to: each agent's preload bytes, the suite's seconds, each test file's priced
    cases and seconds, each leg's minutes and each document's bytes, beside
    the same reading at the last release tag.
- add
  file: docs/release-checklist.md
  section: 5. The release pull request
  to: **Each release clears what grew.** The module rows are a report and
    never a ceiling: a heavily exercised module needs the cases it needs. The
    owner reads the rows whose seconds or cases grew most since the tag and
    sweeps each such module with one `bin/mutation-check` call carrying a
    mutant per class, for cases that kill nothing another case does not. The
    sweep's cuts land in a work item of the next release with one line per
    cut case, the shape `CONTRIBUTING.md` *The test layout* gives.
- change
  file: docs/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: row, and it is three rules rather than an example. check: tests/test_the_seal_is_taken_once_by_the_sealer.py
  to: row, and it is three rules rather than an example.
    check: tests/test_broad_gate.py
- change
  file: docs/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: half a repair. check: tests/test_the_seal_is_taken_once_by_the_sealer.py
  to: half a repair.
    check: tests/test_broad_gate.py
- change
  file: docs/the-broad-gate.md
  section: What the gate runs, and how the list is kept true
  from: it says nothing a reader acts on. check: tests/test_the_seal_is_taken_once_by_the_sealer.py
  to: it says nothing a reader acts on.
    check: tests/test_broad_gate.py

## Open questions → questions.md

Framed 2026-10-22 by framer, before the build.
