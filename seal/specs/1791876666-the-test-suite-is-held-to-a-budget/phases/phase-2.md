# 1791876666-the-test-suite-is-held-to-a-budget — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 652bf297 |
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

Then the owner's decision that replaces the line (2026-10-14): drop the
`Kills:` docstring line, because nobody annotates a test, and a check derives
whatever it needs. The asks that came with it:

- mutants from the pull request's diff, or, for a tests-only change, from the
  units the new or changed cases exercise, with how that errs;
- each such case in the killer set of at least one mutant no other case in
  its file kills, or named;
- the mutants of changed code nothing kills listed, as a gate or a report,
  with the reason;
- `tests/unguarded-files.txt` removed if nothing owes a line;
- the plan's phase 2 row and the `CONTRIBUTING.md` paragraph rewritten in
  place, and the removals recorded as one line.

Also asked:

- that any verdict from the run another agent killed (PID 46132) be discarded
  and re-run;
- an answer to #942's Q2;
- the splitlines finding fixed, in a commit of its own (7a6d2be3).

#930's `seal/budgets.md` is not on this branch, so the five measurers and
their rows wait for it. Phase 3 is not started.

## What this phase found

**The frame holds, with one consequence it does not spell out.** The check
reads every function that is new or changed against the pull request's base,
which means phase 1's S2 and its pins too, not only what phase 2 adds. Phase
1's T3, `test_every_sampled_name_is_a_corpus_row` (NAME NOT IN TREE: removed),
is removed: its mutant, a misspelt `SAMPLE` name, is killed by S2's own row
for that name, which fails on a `KeyError`. `mutation-check` with the name
misspelt is red with T3 gone (`executed`).

**What this phase removed, in one line:** the `Kills:` grammar and its lines
on S2, T1 and T2, the eleven cases of the first case file (NAME NOT IN TREE:
`tests/test_a_new_case_names_the_mutant_it_kills.py`),
`tests/unguarded-files.txt`, which nothing reads once no case owes a line,
and the silent-run case with `first_line` and `mutation_run`'s first line,
which nothing read.

**The check as built, nothing written by hand.** Each test file holding a new
or changed function runs once as it stands, under a tracer that records the
lines each case's call runs (a pytest plugin the check writes to a scratch
directory, so an xdist worker loads it too), and must pass. For each such
function the mutants are drawn in order:

1. from the lines it runs and its siblings do not;
2. from the units of its own file it names, followed through their names;
3. from the other lines it runs;
4. from the shipped lines the range changed, the changed files the case names
   in its own text first.

A test function's own lines are never mutated, and a mutant that does not
parse is not run. The operators are an assertion dropped, a condition negated,
a comparison or a boolean flipped, a `return` made `return None`, an integer
moved by one, and the statement removed; a changed `.md` line is mutated by
removing it. Under each mutant only the cases that ran its line run (the
whole file where no case's call ran it), and a function is proved when every
failing id is its own. A docstring-only change is a change.

How it errs, stated in the module docstring:

- **Under.** A line reached only through a subprocess or a fixture's setup is
  not traced. Such a case gets its mutants from the names it uses and the
  diff, and its mutants run the whole file.
- **Under, again.** The operators are coarse. A case guarding a branch that
  only a narrower mutation tells apart, such as "a changed function, not only
  a new one, is read", can find no mutant of its own, and is named.
- **Over.** A line one case runs and its siblings do not may be setup only
  it needs, which costs a run and proves nothing.

**The survivors are a report, not a gate.** The changed shipped lines'
mutants that ran and that no case killed are listed, and so are the test
functions the range removed. A gate would be red for a mutant a file the check
did not run kills, and would send a case into the pull request's files to
quiet it. A removal is proven by its work item's mutation table. The owner's
condition, that protection never drops, is held by the pass rule for what is
added and by the tables for what is removed. The check never reads which
mutants other files kill, so it cannot hold that condition alone.

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
subprocess's output and its docstring's first line, each named out of class in
`tests/test_every_reader_ends_a_line_where_gfm_does.py`'s table, since neither
is a document's lines.

**The bound.**

- `--bound` is minutes for the whole check, five in the job.
- Each file gets an equal share of what is left. A file whose traced run
  alone passes its share is named `restructure: test the decision directly`.
  So is a function still unproven when the share is spent, with how many of
  its mutants ran.
- Each mutated run is capped by the time left, so a run past the bound is a
  named `timed out`, never a silent one.
- The job's `timeout-minutes` is 15, above the bound plus setup.
- A `cost` line gives each file's traced run and its mutants' seconds.

**What the check said when run on this branch** (`executed`, against
`origin/release/v0.22.0`, `-n 4`, near the ubuntu runner's four cores).

The `Kills:` model's five runs (314232d5 to 74c23261) each found a case of
mine whose mutant a sibling killed too, and each was fixed by narrowing a
fixture. One of them, at 43f71101, is discarded: another agent killed this
worktree's `mutation_check.py` (PID 46132) mid-run.

The derived check's runs:

| Commit | Load averages | Proved | Named | Seconds | What changed after |
|---|---|---|---|---|---|
| 1c475c11 | 113–259 | 11 | 5, the commit-gate file starved | 309 | every mutant reran the whole file, and the first file took the whole bound: now a mutant runs the cases that ran its line, and each file gets an equal share |
| 9c05ff0a | 128–211 | 12, S2 among them (`hooks/githooks.py:79 statement removed`) | 7 | 280 | a case's changed-line mutants came in path order: now the files a case names come first |
| 652bf297 | 150–249 | 9, `test_a_caller_that_ran_the_baseline_skips_it_in_mutation_check` among them (`mutation_check.py:300`) | 9 | 280 | — |

At these loads the case file's traced run took 2–4 s, and each of its
mutants took about 3 s. That fit 15 to 21 mutants per case within its share,
of 400 to 440 drawn. The commit-gate file's traced run alone took 49–105 s,
so its three changed functions got at most one mutant. Every case it named
was named `restructure` with its count of mutants run, not `kills nothing its
file does not`: the bound ended the draw before any case's draw ran out. What
the job says on an idle runner is PR #939's to show.

The survivors listed in the runs are real holes, not noise. Two examples: a
row of the comparison table no case exercises (`case_check.py:180–184`), and
`case_check.py:346` `and` made `or`.

**After CI run 38498393195** (b2564df7), which failed three jobs. Each was
read from its log before anything changed:

- **The `cases` job** named 7 cases `restructure`: each drew 400 to 534
  mutants in path order and ran 23 or fewer. The draw is redesigned, and
  the bound is unchanged (cbfd322c):
  - lines are ranked by how many siblings run them; a line only a sibling
    ran is never drawn; ties take a changed line first, then one line per
    unit;
  - the draw stops at 12 (`DRAW_CAP`);
  - the case's own ids run first and the siblings only where it failed, so
    a miss costs one case's run;
  - a subset keeps xdist's workers where the traced call seconds reach
    `WORKERS_PAY_S`;
  - a line no call ran runs the whole file, because an element removed from
    a parametrization's list removes an id;
  - the survivor report runs after every file's proofs.

  The draw then reached the end of the operators, so four were added: the
  last operand of `and`/`or` dropped, `in`/`not in` and `is`/`is not`
  flipped, and an element removed.
- **Windows** `could not start: C:hostedtoolcache…python.exe`: `shlex.split`
  reads `\` as an escape. `arm_check.py#command_words` keeps it on Windows,
  and `mutation-check`, `arm-check` and `case_check.py` split there
  (c0e6cbdf).
- **Windows** `#686: cd $W unset` landed nowhere. The cause is bash 5.3, not
  Windows: 5.3 refuses `cd ""` (its `null directory` error). The images carry
  5.3 on Windows, 5.2.21 on ubuntu and 3.2.57 on macOS. Seen red on macOS
  under a bash 5.3 built from source. 7fd12bd4 skips the row by `NO_EMPTY_CD`
  wherever the bash S2 runs refuses an empty cd. The subgroup stays in
  `SAMPLE`. On Windows it runs no row, since its other rows cd into an
  unquoted path.

| Run, `-n 4`, 5-minute bound (the first three on states cbfd322c amended) | Load | Proved | Named | Seconds |
|---|---|---|---|---|
| ranked and capped | 5–8 | 12 | 9: the case file's verdicts `restructure`, the gate file's traced run 104 s, no mutant | 300 |
| own ids first | 7–37 | 14 | 8 | 300 |
| cap 24 probe, 10-minute bound | 10–13 | 17 | 5 | 604, the case file 495 |
| cbfd322c, final | 7–12 | 17, every gate-file case: S2 by `:368 statement removed`, T1 by `:319 element removed`, T2 by `:598 condition negated` | 5, `kills nothing its file does not` | 299 |

The five named at cbfd322c ran out of their 12-mutant draws, not the bound:

- `drawn`'s order case and the silent-run case each prove at cap 24;
- the end-to-end tests-only, changed-function and removed-case paths do not
  prove even at 24. Their distinguishing mutants lie inside `check`, whose
  lines all eight end-to-end cases run, so a line-level rank cannot set them
  apart.

**Whether "the only killer in its file" is the right bar.** It stays,
at the function level. The ids of one parametrize are already one case,
because `sole_killer` folds `[…]`, so a kill rows share is their function's
own. A per-row bar would cost one proof per row: S2's 35 rows are 16 s a
whole-file run on CI. Growth by rows is held by #930's `test-cases` budget
row. Relaxing the bar to "killed nothing the base's cases kill" would pass
two new cases that are twins of each other, which is the regrowth the check
exists to stop. The direct tests named at CI were a gap in the draw and the
operators, not in the bar: the sole-killer case and T1 proved once an operand
drop and an element removal existed, and most of the rest once the draw was
ranked. The five still named are listed above.

**After CI run 38518943105** (0f2b8a33). Two jobs failed, and both logs
were read before anything changed:

- **Windows, six end-to-end cases.** Every mutant was refused: `tree()`
  wrote its fixtures with `write_text`, which writes CRLF there, and
  `mutants_of` joined lines with `\n` while `mutation-check` matches the
  file's bytes, so no `old` occurred once. The log is the proof: `1 of the 2
  mutants drawn ran`, every run 0 s, and a `.md` line removed survived too,
  which rules out stale bytecode. A CRLF fixture gives the same output on
  macOS. Since 7177f24a a mutant keeps each line's own end, and `mutants_at`
  reads with `newline=""`. `tree()` now writes the same bytes on every
  platform, and a CRLF row pins the cause everywhere (contract §13).
- **The `cases` job** proved 16 and named 6. The six were four end-to-end
  paths and two direct tests:
  - **The four paths** shared every kill with the other paths, because each
    path's case runs all of `check`. The nine paths are now one parametrized
    case with a row each (46cf830a). The check counts one function's ids as
    one killer. The merged case is red under each mutant the old cases had
    alone, numbered as at 0f2b8a33: `:879` condition negated, `:416` and `:326` `return None`, and
    `:816` statement removed. Each was shown with `mutation-check`.
  - **`drawn`'s order case** is kept. With the paths merged, a line it runs
    has fewer siblings, and it proves by `:741 condition negated`.
  - **The silent-run case** is removed, with the value it guarded
    (06f499d3). A probe of its uncapped draw found one mutant only it kills:
    the default line of `next` removed, the line naming a run that printed
    nothing. It fed `mutation_run`'s first line, and `check` discarded that
    value in both of its calls, so `first_line([], …)` at the call site
    survived every case (`executed`). `mutation_run` returns its
    exit and its output, `first_line` is gone, and so is the line-end
    table's row for `mutation_run`, whose `splitlines` call it named.

  Locally at 06f499d3, `-n 4`, load 4–10: 14 proved, 0 named, in 298 s,
  exit 0 (`executed`).

**The cases**, each a direct test of one decision or one real path end to
end, all passing (`executed` at 06f499d3, 19 ids passed):

| Decision or path | Case |
|---|---|
| each operator makes one mutant of its kind | `test_each_operator_makes_one_mutant_of_its_kind` |
| a mutant lands once, and one that cannot parse is left out | `test_a_mutant_widens_until_it_lands_once_and_one_that_cannot_parse_is_left_out` |
| the sole killer is one function or none | `test_the_sole_killer_is_one_function_or_none` |
| a named helper is followed | `test_a_function_named_in_a_case_is_followed_through_its_helpers` |
| where a function's text ends | `test_a_line_end_python_does_not_read_moves_no_function` |
| `--baseline-passed` | `test_a_caller_that_ran_the_baseline_skips_it_in_mutation_check` |
| each real path end to end, one row each: S4 → 0 in the step summary; the same on CRLF line ends; S3 → 1; a survivor listed; a tests-only case; S5's prose pin; S2's changed function; a removed case listed; a file past the bound → restructure | `test_each_real_path_end_to_end` |

**#942's Q2, answered by the design and the owner's decisions.**

- (i) One run per mutant, read for its killers, is built. The run is now the
  cases that ran the mutant's line, not the file, and the baseline is the one
  traced run.
- (ii) No matrix over functions. The bound is per pull request, and a file
  or a case past it is named to restructure. A matrix would spend more runner
  minutes on the files the owner reads as testing decisions through the whole
  stack.
- (iii) A docstring-only change is a change, by the owner's rule, so a case
  edited only in its docstring is proved again.

**What the phases after this one take from the owner (2026-10-14).** For
each shipped module, the old tests serve only as the baseline, their set of
killed mutants, and as the reference, the regressions of real bugs to port.
The redundant or heavy parts are rebuilt as direct tests of the decision, plus
one end-to-end case per real path, and the old files are deleted. The result
may not be weaker than today: the killed-mutant set never drops. The derived
check proves what is added, and each phase's mutation table proves what is
removed. Phases 3 to 6 in `plan.md` still name `Kills:` lines and
`tests/unguarded-files.txt` (NAME NOT IN TREE: removed). They are the
framer's to reframe, since only phase 2's row was mine to rewrite.

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
