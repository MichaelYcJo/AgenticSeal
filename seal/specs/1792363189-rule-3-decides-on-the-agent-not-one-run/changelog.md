### Changed

- **Rule 3 of the behaviour evaluation now judges the agent, not one run
  (#966).** `evals/scripts/noninferiority.py#verdict` used to compare each
  shape and reach grader on its own, so one grader losing one of its two
  runs failed a rewrite whose passes rose overall. Now the passes of every
  shape and reach grader both sides ran are added up on each side. The new
  side fails rule 3 where its total is below the baseline's. It also fails,
  naming the grader, where it failed a grader on every run that the
  baseline passed at least once. A grader the baseline lacks still has to
  pass every new run. Rules 1, 2, 4 and 5, every `no result` condition,
  `--runs` and the suite are unchanged, and so is the `model` subcommand,
  which still compares per grader.

  A failing rule 3 writes new lines under `Verdict:` in a record. A falling
  total reads `shape and reach graders passed 29/30 runs on the new side,
  fewer than the baseline's 30/30 (rule 3): ` and then each grader whose
  passes fell, as `<case>/<grader> 1/2 against 2/2`. A grader lost on every
  run reads `shape grader <case>/<grader> failed every new run (0/2) where
  the baseline passed it 2/2 (rule 3)`.

  Where the baseline passed every run of every grader, nothing can offset
  a loss, so one run still decides. #957's sealer record is that case.

  #957's six records, read again under the new rule from their committed
  side files, with no new run:

  | #957 record | As recorded | Shape and reach passes | Under the new rule |
  |---|---|---|---|
  | `warden-phase-2.md` | fail, rule 3 on one grader | 66 → 70 of 72 | pass |
  | `warden-phase-2-run-1.md` | fail, rule 3 on five graders | 66 → 66 of 72 | fail, rule 3 on one grader failed every run |
  | `warden-phase-3.md` | pass | 66 → 70 of 72 | pass |
  | `smith-phase-3.md` | pass | 48 → 48 of 48 | pass |
  | `framer-phase-3.md` | fail, rule 5 | 64 → 64 of 64 | fail, rule 5 |
  | `sealer-phase-3.md` | fail, rules 3 and 5 | 30 → 29 of 30 | fail, rules 3 and 5 |

  The re-read records are this work item's `evals/957-<record>.md`, and
  #957's own records stay as they were judged. So `noninferiority.py check`
  on #957's `warden-phase-2.md` now reports "it says `fail` and its numbers
  give `pass`", because `check` recomputes with the rule that runs it. If
  you run `check` by hand over a record written before this release, read
  that line this way.
  (`1792363189-rule-3-decides-on-the-agent-not-one-run`, #966)
