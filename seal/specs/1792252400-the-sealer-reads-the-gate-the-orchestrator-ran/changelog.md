### Changed

- **The orchestrator runs the broad gate before it spawns the sealer, and
  the sealer runs nothing broad (#969).** The order at a ready pull request
  is now `broad-gate --preflight`, then `broad-gate --base <base> --record
  <item>` run by the orchestrator, then `broad-gate.md` committed, then the
  sealer spawned. The sealer's first act is to read that record. Where the
  item has no `broad-gate.md`, or a commit after the run it names touches a
  path outside the item's directory, the sealer writes `withheld — no broad
  run at HEAD` and runs nothing broad in its place. A session of yours that spawns the
  sealer the old way gets that verdict back: run the gate, commit its
  record, and spawn the sealer again. The stamp is drawn as before, at the
  end of the turn of the session that ran the gate. The sealer's model stays
  Opus, decided by measurement: on the same suite a Sonnet sealer cost
  1.4076 USD against 2.8036 and passed 53 of 54 graders against 54, losing
  one verdict line's shape, so `noninferiority.py model` printed `opus`.

  | Agent | Tree | Preload bytes | Tokens per tool call | Spend USD | Graders passed | Verdict |
  |---|---|---|---|---|---|---|
  | sealer | `2fc33333` → `5ca68b5d`, one suite (`c2544c8f`) | 24,652 → 23,792 | 35,490.9 → 33,386.8 | 3.1901 → 2.8036 | 39 → 54 of 54 | pass |
  | sealer | at the close, `1483d8ba`, the renamed five-case suite | 24,702 | 37,080.5 | 3.3898 | 68 of 68 | none: the reference a later sealer change compares against, never compared across suites |

  Each figure is read with `noninferiority.py#side_numbers` from the work
  item's `evals/baseline-sealer.json` (committed at `9184881a`),
  `evals/sealer-phase-4.json` and `evals/sealer-sonnet-phase-4.json`
  (`d27f7994`) and `evals/reference-sealer.json` (re-run after round 3
  on the five-case suite); the verdict is `evals/sealer-phase-4.md` at
  `d27f7994`. The four-case sides are 8 runs each and the reference 10,
  none cut short.
  (`1792252400-the-sealer-reads-the-gate-the-orchestrator-ran`, #969)
- **The sealer's verdict reads `sealed`, `withheld — <reason>` or
  `undecided — <question>` (#969).** These replace `sound`, `not sound` and
  `undecidable` in `guarantee.md`, its template, the sealer's definition and
  the check at the pull request. A `guarantee.md` that still reads one of
  the old words fails a ready pull request on its `Verdict:` line, and the
  line says the word changed. If a work item of yours is in flight with a
  `guarantee.md` reading `sound` when you update, do not edit the word.
  Where the committed `broad-gate.md` names a run at HEAD, or one followed
  only by the work item's records, spawn the sealer again at HEAD, which
  reads it and writes the verdict in the new words over the code it audited.
  Otherwise run `broad-gate --base <base> --record <item>` and commit
  `broad-gate.md` first, then spawn the sealer.
  (`1792252400-the-sealer-reads-the-gate-the-orchestrator-ran`, #969)
