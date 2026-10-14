# 1791876666-the-test-suite-is-held-to-a-budget — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 74c23261 |
| Ran by | smith on Opus 5.5, as `routing.md` and `handoff.md` name it |

## What this phase was asked

Phase 2 of the reframed plan (d1b981ce, approved at cc4ab070), the regrowth
check:

- `.github/scripts/case_check.py`, the `Kills:` docstring grammar,
  `tests/unguarded-files.txt` with the 185 files, and the `cases` job in
  `test.yml`;
- T1–T7, each with its own `Kills:` line;
- the `CONTRIBUTING.md` paragraph rewritten in place;
- verification by the fixture-tree probes the plan names;
- Q1 and Q2 marked as answered by the owner: Q1 is #943 in 0.22.1, with D4
  until then, and Q2 is #942 in 0.22.0.

Asked during the phase, as owner decisions of 2026-10-14:

- one run of the file per mutant, read for its killer set, in place of the
  with-and-without pair;
- a function whose only change is its docstring is still checked;
- the proof finishes within five minutes on a pull request, and a file whose
  proof would pass that fails the job, named and told
  `restructure: test the decision directly`, never by a timeout.

Also asked:

- that any verdict from the run another agent killed (PID 46132) be discarded
  and re-run;
- an answer to #942's Q2.

#930's `seal/budgets.md` is not on this branch, so the five measurers and
their rows wait for it. Phase 3 is not started.

## What this phase found

**The frame holds, with one consequence it does not spell out.** The check
reads every function that is new or changed against the pull request's base,
which means phase 1's S2 and its three pins too, not only what phase 2 adds.
Each now carries a line, proved by the check itself (below), except phase 1's
T3, `test_every_sampled_name_is_a_corpus_row` (NAME NOT IN TREE: removed), which is removed. Its mutant, a
misspelt `SAMPLE` name, is killed by S2's own row for that name, which fails
on a `KeyError`. So no line could prove T3 alone. `mutation-check` with the
name misspelt is red with T3 gone (`executed`). S2's line names the one thing
only its rows exercise in that file: an emptied environment's `git` below a
shell below `claude`, so the lease walk has to climb past the call's shell
(`hooksession.claude_ancestor`'s `depth`).

**The grammar** (Q3): `Kills: <path> "<OLD>" "<NEW>"`, OLD and NEW as JSON
string literals. The line is read from the docstring as written in the file,
not as Python evaluates it, so `\"` and `\n` mean the same in a raw docstring
and in a plain one, and `\n` is how a multi-line mutant is written. A case
that pins prose names the document (T6).

**The run model, as the owner set it.** Each touched file runs once as it
stands, and must pass. Then each new or changed function's mutant runs once
through `mutation-check` over the whole file. The run must be red, and its
failing ids, read from pytest's `FAILED` and `ERROR` lines, must be the
function's own and no other function's. A shared kill is named, never
allowed: a mutant two cases kill is the duplication the check exists to
refuse. A docstring-only change is a change, because the function's text
runs from its first decorator to its last line, docstring included.

**`mutation-check --baseline-passed` is new, and the model depends on it.**
Without it every `mutation-check` call reruns its baseline, so one mutated
run per function still costs two file runs. With it a file costs 1 + N runs,
for N functions to prove. The option skips only the run against the file as
it is. It is for a caller that ran the same command against the same bytes
and saw it pass, which `case_check.py` does once per file before any mutant.
A bare call is byte-for-byte what it was: `main` passes `baseline` only when
the option is set. Released row L7 said the baseline always runs, so it has a
`Corrected ·` row in the fragment. It is the only released claim the option
changes. Of the rows that speak of `mutation-check`, L1 says the bytecode is
cleared before each run, the baseline and the mutated one; that still holds
for every run that happens, and its re-read is in the fragment. L2 to L5 say
nothing of the baseline run.

**Where a function's text ends.** `case_check.py` cuts each function's text
by the line numbers `ast` gives, so it splits Python source where Python's
tokenizer ends a line (`\r\n`, `\r`, `\n`). `str.splitlines` also ends a line
at U+2028 and similar characters, which Python reads inside a string. A test
file holding one shifted every later line, so a change on a function's last
line was not read as a change.
`test_a_line_end_python_does_not_read_moves_no_function` pins it, and is the
only killer of its mutant (`executed`). The check's other splits are a
subprocess's output, its docstring's first line, and its own list file. Each
is named out of class in
`tests/test_every_reader_ends_a_line_where_gfm_does.py`'s table, since none is
a document's lines.

**The bound.**

- `--bound` is minutes for the whole check, five in the job.
- A file's cost is its one run times the functions it owes, read before any
  mutant is written. A file whose proof would pass what is left of the bound
  is named with `restructure: test the decision directly`.
- Each mutated run is capped by the time left, so a run past the bound is a
  named `timed out`, never a silent one.
- The job's `timeout-minutes` is 15, above the bound plus setup.
- A `cost` line in the summary gives each file's run and its mutants'
  seconds.

**What the check found when run on itself** (`executed`, over this branch
against `origin/release/v0.22.0`):

| Run | Commit | Result | Seconds | What it named |
|---|---|---|---|---|
| 1, with-and-without | 314232d5 | 9 proved, 1 named | 317 | T2: its mutant (the refusal read as proved) was killed by T5 too, because T5's stale line also failed to land. T5's changed function now keeps a line that lands but that its body no longer kills |
| 2 | 43f71101 | discarded | 217 | two without-runs came back with no verdict at all: another agent killed this worktree's `mutation_check.py` with `kill -9` (PID 46132) during the run, by the orchestrator's account. T8 now pins that such a run names its exit |
| 3, with-and-without | abe57743 | 11 proved, 0 named | 305 | — |
| 4, one run per mutant | a8fa6a86 | 13 proved, 1 named | 313 | T5's mutant was killed by the bound case too, because its fixture changed a function rather than adding one. The bound case now adds one |
| 5, one run per mutant, bound 5 | 74c23261 | 11 proved, 1 named | 126 | `tests/test_the_commit_gate_decides_at_the_commit.py: restructure` — its one run took 93 s with `-n 4` at load averages 94–115, so its three functions needed 278 s against the 275 s left |

Runs 4 and 5 were taken with `-n 4`, near the ubuntu runner's four cores, on a
machine shared with two other builds at load averages from 27 to 115. In run
5 the case file cost 2 s for its one run and 23 s for its 11 mutants. Whether
the commit-gate file fits on an idle runner is what PR #939's `cases` job
shows (`overview.md`). The bound named the file before running it, which is
the behaviour the owner asked for.

**The probes the plan names** are cases that build a fixture repository at a
base and at HEAD and run the check in process, with real mutants through the
repository's own `mutation_check.py`. Every one passes (`executed`), and the
check proved each on its own mutant (run 5):

| Probe | Case | Exit |
|---|---|---|
| a function without a line | T1 `test_a_new_function_without_a_kills_line_is_named` | 1 |
| a line that does not land | T2 `test_a_line_whose_replacement_does_not_land_is_named` | 1 |
| a mutant its file kills through another function too | T3 `test_a_mutation_the_file_kills_without_the_function_is_named_with_its_killer` | 1, naming the killer |
| a proven function | T4 `test_a_proven_function_passes_and_the_summary_lists_both_runs` | 0, the summary written |
| a prose pin through a `.md` path | T6 `test_a_prose_pin_runs_through_the_document` | 0 |
| a changed function with a stale line | T5 `test_a_changed_function_is_read_as_new` | 1 |
| a file off the list, and one added to it | T7 `test_a_file_leaves_the_list_only_when_every_function_carries_the_line` | 1 |
| a mutant only another function kills | `test_a_mutant_only_another_function_kills_is_named` | 1 |
| a run that prints nothing | `test_a_run_that_prints_nothing_is_named_by_its_exit` | — |
| a file whose proof would pass the bound | `test_a_file_whose_proof_would_pass_the_bound_is_named_to_restructure` | 1 |
| `--baseline-passed` | `test_a_caller_that_ran_the_baseline_skips_it_in_mutation_check` | — |

**#942's Q2, answered by the design and the owner's decisions.**

- (i) One run per function under its mutant, read for the killer set, is
  built. Through `--baseline-passed` a file costs 1 + N runs of itself,
  where the pair cost 2N plus 2N of the function alone. #942's 1,554
  ubuntu-minutes for its 14 heaviest files, read under the pair, come to
  about half.
- (ii) No matrix over functions. The bound is per pull request, five
  minutes, and a file whose proof would pass it is named to restructure
  before it runs. A matrix would spend more runner minutes on exactly the
  files the owner reads as testing decisions through the whole stack.
- (iii) Yes, a docstring-only change is a change. The `Kills:` line is the
  claim, and a line added unproven is the failure the check exists for. So
  lining a file costs one run per function, and on a heavy file that is the
  restructure finding.

**What the phases after this one take from the owner (2026-10-14).** For
each shipped module, the old tests serve only as the baseline, their set of
killed mutants, and as the reference, the regressions of real bugs to port.
The redundant or heavy parts are rebuilt as direct tests of the decision, plus
one end-to-end case per real path, and the old files are deleted. The result
may not be weaker than today: the killed-mutant set never drops, and the
`Kills:` lines and the tables are that proof.

**Carried to phase 5, the sealer file (measured before the reframe, at
480bea69 and fcd735bc).**

- Q5's inventory: 105 test functions reach the gate, and their first gate
  runs have 100 distinct signatures (the tree built, the gate call, the
  environment). The read-only cases that share one are about 6 Windows
  seconds, so a memoized run per signature saves almost nothing there.
- fcd735bc removed six corpus layouts (`Qf-row`, `Qf-env`, `Qf-ini`,
  `R1-row`, `R1-ini`, `Q8`; 12 ids, 56.49 Windows seconds). Each differs from
  a kept layout only by a junit option, and nothing the gate or its recorder
  runs reads junit output.
- The battery at 480bea69 (`executed`) was twelve mutations of
  `broad_gate.py`'s words and the recorder (`base_word`'s five rows, the
  record key, `realpath`, `unended`, `PYTEST_ADDOPTS`, the collecting module,
  a failed collection's path, the failing gate's exit). Every one was red:

| Mutation | Corpus killers | Other killers |
|---|---|---|
| b01 any failing file reads `failing on base too` | 50 | 39 |
| b02 `not reached` reads `new` | 36 | 20 |
| b03 the exit-0 rule dropped | 2 | 7 |
| b04 the collected rule dropped | 15 | 47 |
| b05 no `no record` | 0 | 4 |
| b06 the key ignored | 0 | 19 |
| b07 the worktree's `realpath` dropped | 17 | 69 |
| b08 `unended` never counted | 0 | 23 |
| b09 `PYTEST_ADDOPTS` replaced | 0 | 1 |
| b10 the defining module, not the collecting one | 9 | 0 |
| b11 a failed collection carries no path | 0 | 3 |
| b12 a failing gate exits 2 | 55 | 110 |

- The removed rows' kill vectors equal their kept twins' (P1's for the Qf and
  R1 rows, P3-sh's for Q8), so each mutation keeps its killers.
- The after battery at fcd735bc was stopped by the reframe, so the after
  column is derived, not measured: removing ids leaves every other case's
  kills as they were. Phase 5 runs it.
- `REGRESSED_WORDS`' released row R5 is corrected in the fragment.

**The ledger.** Three changes moved cited content: S2's docstring, the
`CONTRIBUTING.md` paragraph, and `mutation_check.py`'s `mutation_run` and
`main`. Every root claim citing them was read before its row was written:

- `Re-read ·` rows for S1, P3, A6, S9, H4, S4, R3, R4, L1 and L3;
- G4's row re-stamped in place;
- `Corrected ·` rows for R5 and L7.

`plan.md`'s names the tree does not hold are marked `NAME NOT IN TREE`, as
the orchestrator decided for this file's names: the two `gh api` fields, T8
(planted with the measurers) and T9 (phase 3). `bin/evidence-check .` and
`bin/evidence-check --strict .` both exit 0 at the commit that carries this
record (`executed`).
