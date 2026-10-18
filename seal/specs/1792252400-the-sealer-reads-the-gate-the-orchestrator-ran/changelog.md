### Changed

- **The sealer's verdict reads `sealed`, `withheld — <reason>` or
  `undecided — <question>` (#969).** These replace `sound`, `not sound` and
  `undecidable` in `guarantee.md`, its template, the sealer's definition and
  the check at the pull request. A `guarantee.md` that still reads one of
  the old words fails a ready pull request on its `Verdict:` line, and the
  line says the word changed. If a work item of yours is in flight with a
  `guarantee.md` reading `sound` when you update, do not edit the word: run
  `broad-gate --base <base> --record <item>`, commit `broad-gate.md`, and
  spawn the sealer again at HEAD, so the verdict is written in the new
  words over the code it audited.
  (`1792252400-the-sealer-reads-the-gate-the-orchestrator-ran`, #969)
