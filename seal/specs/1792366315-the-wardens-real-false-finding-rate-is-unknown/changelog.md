### Added

- **A side already paid for is graded again under another suite's truths,
  with no run (#971).** `evals/scripts/noninferiority.py regrade --side
  IN.json --suite-rev REV --out OUT.json` grades each run of a committed
  side on REV's `truth-` graders, searching each grader's regex over the
  run's report rows. It writes the side again with the scores following, and
  names the suite it ran in `specseal.regraded_from`. It exits 2, naming the
  case, in these cases:
  - the side's own suite does not give back from its rows what it recorded;
  - REV differs from the side's suite in anything but `truth-` graders;
  - REV holds other cases;
  - a truth is one no report row can answer.

  #957's two warden sides, regraded onto af9c924b, give back their recorded
  figures: 55 rows with 43 false, and 47 rows with 31 false.

### Changed

- **The warden's suite lists the real defects its runs recurred on
  (#971).** The harness counted every report row that no `truth-` grader
  matched as false. So a real defect a case did not list read as a false
  finding, and 43 of the baseline's 55 rows and 31 of the phase-3 side's 47
  read as false.

  Each of those 74 rows is now classed, from #971's first comment, and tied
  to its committed row in the work item's `evals/false-rows.md`. Of them,
  1 a side is `wrong`.

  A real defect named in at least two of a case's four runs is a truth of
  the case: 15 truths added. A listed truth a run found at a coordinate its
  regex missed is widened with that coordinate: 2 widened. Both come from
  one input file, `evals/scripts/recurred_truths.json`. All three
  generators read it, and an entry the case cannot take stops them with
  exit 1. No other file of any case changed, and no other agent's suite
  moved.

  Under the new suite, at 864798a4, the same two sides read:

  | Side | False rows, af9c924b | False rows, 864798a4 | Recall, af9c924b | Recall, 864798a4 |
  |---|---|---|---|---|
  | baseline | 43/55 | 19/55 | 13/24 | 39/54 |
  | phase 3 | 31/47 | 12/47 | 16/24 | 41/54 |

- **The new suite is the one a warden comparison uses from the release
  after 0.22.2, and 0.22.2 decides nothing on it.** By the owner's
  decision in #971, 0.22.2's comparisons stay on af9c924b's suite: #968,
  #970, #985 and the milestone's closing verdict. One of them passes
  `--suite-rev af9c924b` and is unaffected. A comparison against an
  af9c924b baseline that passes the default `HEAD` meets the new suite, and
  `compare` refuses it.

  From the release after 0.22.2, a warden baseline is still a run of the
  tree it starts from. The regraded phase-3 side measured a preload that is
  no longer the tree's, so it is a record and not a baseline.
