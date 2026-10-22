# Implementation Plan: tests rebuilt one file per module (#942)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-22 by the orchestrator, under the owner's `automation` answer and the owner's answers to Q1 and Q2, when `smith` was spawned.

## Summary

The checks go in first, then the modules are rebuilt in batches, heaviest first, each batch applying `spec.md`'s four rules and recording what it cut. Rule 4 is read before every module: a rewritten module builds its world once, judges a reading without git where it can, samples where it enumerated, and records its seconds before and after. The smith recomputes every count it acts on at the tree it builds on, with the command each phase names, because #988, #1009 and #1005 merge between this frame and the build and move cases, lines and citations.

## Technical context

- `tests/conftest.py` lines 817 to 856 hold the `repo` fixture copied from a session-scoped template, the pattern rule 1 extends to a module-scoped world. Lines 856 to 910 hold the failing ceiling phase 2 turns into a report.
- `.github/scripts/release_report.py#suite_seconds` reads `.test_durations` in a tree; phase 2 groups the same reading by file.
- `bin/mutation-check` runs one mutation under a bound and prints red or SURVIVED; it is the instrument of every batch's table. `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/phases/phase-1.md` is the record shape: the table of mutations with killers before and after, the timing table, and the removed ids' seconds.
- `tests/test_the_commit_gate_decides_at_the_commit.py` builds three repositories per case (its docstring, lines 1 to 14). The flow moves to `tests/e2e/commit/` with the world built once per module.
- `hooks/cmdline.py` (3,097 lines) and the reading in `hooks/commit-review-gate.py` stay under `questions.md` Q1's default; `hooks/cmdline_base.py` stays whatever Q1 answers, because the worktree guard's switch arm reads it (`docs/the-commit-gate-inside-git.md` *The convergence argument is claimed for commits alone*).
- Failure scenario of the chosen approach: a module rebuilt from the code reproduces the code's own blind spot, and a case the old file had for a bug the code fixed is cut because the mutation table did not include that bug. The table's mutations are chosen before the old cases are read, one per class at least, and a cut case's line names the mutation that justifies it, so a reviewer can ask for the missing mutation.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the files as they are and trim duplicates in place | The owner's finding: a fast-module sample showed thin, uneven protection, not duplication; trimming leaves the layout that let the suite grow unseen | refused |
| Replace the suite wholesale from the code, old files read by nobody | A behaviour the code has for a bug nobody remembers loses its only case, and nothing records what went | refused; rule 2 reads every old case and records every cut |
| Rebuild per module, old cases classified, heavy or duplicated modules written anew (chosen) | See Technical context; held by the mutation table and the one line per cut case | chosen |
| Group by scenario rather than by function | A new test has no place to start from, which is how adding became the default; the pairs report has no class to compare within | refused |
| A separate CI job for the layout check | A job is a mechanism beside the suite, and #929 removed the `cases` job for that reason | refused; the check is a case of the suite |
| Remove the text reading with its three files | Allows more in a foreign hooks slot and an unreached clone, the gate bar's costly direction, with no install count to weigh it by | Q1, a person's; default keep and sample |
| Keep `CASE_CEILING_S` failing | A loaded machine fails a guarantor run on time alone, as on 2026-10-16 | refused by the owner; a report |
| Keep each census as one module over every file | The implementer runs the module it touched and never the census, four times in 0.22.0 | refused; per-module cases |
| Keep the stored exemption lists | A list beside the tree drifts from it; `CLAUDE.md` refuses it | refused; a comment at the line |

## Phases

Vertical slices. Each phase's first step recomputes the facts it acts on with the command named, and each batch's `phases/phase-N.md` carries the mutation table, the before and after counts and seconds of the module, and one line per cut case. A batch's module list is written into the record when the batch starts, not here.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `skills/verify/scripts/test_layout.py`, `bin/test-layout` with its `.cmd`, `tests/test_test_layout.py` with `TARGET`, the suite case running `--check` over `tests/` without `--all`; `CONTRIBUTING.md` *The test layout* stating the four rules and the record shape; the command named in `agents/smith.md` line 98's and `agents/warden.md` line 131's sentences | S1 to S4 seen red; `bin/test-layout --check` exits 0 and prints the count of files without `TARGET`; `bin/test tests/test_test_layout.py -q` | cbf6ef6f |
| 2 | `SLOW_CASE_S` and the summary report in `tests/conftest.py`; `tests/test_conftest.py`; module rows in `release_report.py` and `tests/test_release_report.py`; `docs/release-checklist.md` through `## Rule changes`; the `CONTRIBUTING.md` paragraph rewritten | S6 and S7 seen red; `python3 .github/scripts/release_report.py --against v0.22.2 --at <archive>` prints the rows locally | |
| 3 | `tests/censuses.py` with one function per census, `census_case` in `conftest.py`, the exemption lists replaced by line comments, the old census modules placed under rule 1 | S8 and S9 seen red; every census module's old cases either placed or cut with a line; `bin/test tests/test_censuses.py -q` | |
| 4 | Helper twins defined once in `conftest.py`; first step: `bin/test-layout --check` lists them | the check names no twin; `bin/test <each touched file> -q` | |
| 5 | Batch A, the modules whose old files price at a minute or more; first step: `python3 -c` over `.test_durations` grouped by file, descending; one commit per module, the sealer's and the commit-gate flow's first, the three text-reading files sampled per kind under Q1's default | S5 per module; the pairs report names no pair in the new file; the record's tables | |
| 6 | Batch B, every remaining shipped module, one commit per shipped directory (`hooks/`, `hooks/git/`, `skills/verify/scripts/`, `skills/code-review/scripts/`, `skills/settle/scripts/`, `skills/implement/scripts/`, `.github/scripts/`, `evals/scripts/`); first step: `git ls-files '*.py'` less `tests/` | S5 per module; the pairs report; the record's tables | |
| 7 | The suite case takes `--all`; `.test_durations` pruned of removed ids; the closing memo with the suite's wall time before and after, `bin/test -q` locally | S10; `bin/test tests/test_test_layout.py -q`; `test_the_durations_file_prices_the_suite` passes | |

What a module's table must show before a case is cut: every mutation red against the old files is red against the new file. A mutation that survives the new file gets a case before the batch commits, and the case is seen red on that mutation. Beside the table, the record states the module's seconds and cases before and after, and names the real-git rows it kept under rule 4.

## Operational impact

- `SPECSEAL_CASE_CEILING_S` stops being read; a run that set it is unaffected.
- The suite's collected case ids change in every batch, so `.test_durations` is pruned per batch and refreshed from CI once at the end (`CONTRIBUTING.md` *A case has a budget*' successor paragraph says how).
- No new dependency. `bin/test-layout` is a launcher like the others under `bin/`.
