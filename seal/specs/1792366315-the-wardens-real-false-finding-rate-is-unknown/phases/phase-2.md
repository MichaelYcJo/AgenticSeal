# 1792366315-the-wardens-real-false-finding-rate-is-unknown — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | cd39630a |


## What this phase was asked

Record phase 1's divergences from the frame in `overview.md`: the two
fenced rows with no re-run command, the finding wording marked once for
all rows, and the two moved facts. Then build `noninferiority.py regrade`.
It re-grades a side's committed `report_rows` against a suite at no cost.
It refuses with exit 2 where re-grading the side under its own suite does
not reproduce its record, and where the target suite differs outside
`truth-` files. Write the cases first and see them red. Then re-grade the
two committed warden sides at af9c924b and reproduce 55/43 and 47/31.
#966's rule 3 change is in this tree at 8a100e13, and `regrade` must not
change `verdict`. Close with this record and the Status cell.

## What this phase found

**What was built.** `regrade --side IN.json --suite-rev REV --out OUT.json`
does three things:

1. It reads REV's `truth-` grader files through `grader_from`, the reader
   of the front matter `behaviour.grader` writes.
2. It grades each run of IN on those graders. A grader passes where its
   regex, with the grader's own flags, is found in the run's report rows
   joined by newlines.
3. It writes OUT with the graders, the results and the scores replaced. It
   sets `specseal.suite_rev` and `suite_tree` to REV's, and
   `specseal.regraded_from` to the suite IN ran.

`compare`, `check`, `side_numbers` and `verdict` are unchanged. Comparing
the functions of the module at 8a100e13 and at cd39630a, `main` is the only
one that changed, and only to register the subcommand (executed).

**What it refuses**, each with exit 2, naming the case, and writing
nothing:

- The side names no agent or no suite.
- The side ran a case that its own suite or the target suite does not
  hold.
- The target suite holds a case the side never ran.
- The target suite changes a case's files other than its `truth-` graders.
- Graded again on its own suite, the side does not give back its recorded
  truth graders, truth results, run scores, case aggregates or side
  aggregates.
- A truth grader is not a `contains` regex, carries a flag Python's `re`
  has no letter for, or has no front matter.

Four of these go beyond what `spec.md` §*Data & interfaces* says.
`overview.md` §*Fed back into the spec* names them, marked as inferred.

**The scores are recomputed by a measured formula.** A regraded side
carrying the scores of the grading it replaced would state something
false. So I tried the eval's formula against every recorded value of #957's
eight committed sides before building on it. A run's score is its passed
graders' weight over every scored grader's, and it passes at the suite's
threshold. A case's score and pass rate are its runs' means. The side's
are its cases' means, and its cases passed are those whose every run
passed. The formula reproduced every recorded value of all eight sides
(executed). The self-check refuses any side it does not reproduce, so a
later change to the eval's formula stops `regrade` rather than writing
wrong scores.

**S3 over the committed sides, executed.** `noninferiority.py regrade
--suite-rev af9c924b` over `baseline-warden.json` printed `55 rows, 43
false`. Over `warden-phase-3.json` it printed `47 rows, 31 false`. Both
exited 0. For each side, every grader's passes and the aggregates equal
the recorded ones, and 24 of 24 truth results are the recorded ones. The
outputs went to the scratchpad. Phase 4 commits the sides regraded onto
the new suite.

**`regrade` refuses a side that reports in another shape.** Over the other
committed sides of #957, each on its own suite, the smith's and the
framer's four sides exit 0 with 0 rows. The sealer's two sides exit 2: its
truth graders read the sealer's report text, which holds no `location:`
lines, so the rows cannot give back the recorded results (executed). The
refusal does what it is for. It also means `regrade` stands in only for an
agent whose truths read `location:` lines, the warden today.

**How the cases were seen red.**

- The first five cases (S3, the wider truth, and three refusals) ran red
  before `regrade` existed: argparse refused the subcommand (executed).
- Each case added after the code went red under a mutation of the branch
  it pins. Of 44 single-unit mutations through `mutation-check`, one per
  unit added, 43 were red (executed).
- The survivor replaces the newline that joins a run's rows with a space.
  It is an equivalent mutant for these rows. Every row starts with
  `location: `, and every truth pattern is `^location: .*(?:…)`, so `.*`
  reaches a later row either way. A pattern ending in `$`, or not anchored
  on `location:`, would tell the two joins apart; no generator writes one
  today.
- The case rows put run 0's truth row second, so the `m` flag is what lets
  it be found. Its mutation was red.

**What phase 3 needs from this.**

- Generator output reads back. `grader_from` reads exactly what
  `behaviour.grader` writes: a quoted value holding a doubled quote, a
  comma or a brace, and an integer weight. The case
  `test_a_truth_grader_file_reads_back_to_what_behaviour_wrote` pins this.
- A regrade onto phase 3's commit is refused if that commit changes any
  warden case file other than a `truth-` grader. That includes a scaffold,
  a prompt or a `shape-` grader. Q3's byte-for-byte regeneration therefore
  has to hold for every file but the added truths.
- No other text states what `regrade` does. `git grep -n -e regrade` over
  `evals/`, `docs/`, `skills/` and `agents/` at cd39630a names only the
  module, its README paragraph and the test module. The README names no
  `run --from-raw`, so the paragraph follows the sentence about the
  record's recomputation (`overview.md`, the divergence row).
