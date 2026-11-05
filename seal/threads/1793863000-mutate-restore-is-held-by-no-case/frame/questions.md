# Questions for the planner: mutate-restore-is-held-by-no-case

The issue left these open, and the tree answered each. Nobody reopens them without opening the row that holds the grounds:

- Which rung of the work-item ladder this sits on, and whether its subject is the policy root or the code: `frame/design.md` *Grounding*, the rung row and the document-layout row.
- Where the issue's `SKILL.md` description and its test module stand now: `frame/design.md` *Grounding*, the row on where the issue's three coordinates stand.
- Whether the round 4 report still exists, and whether its paste-ready texts are applied as given: `frame/design.md` *Grounding*, the round 4 report row, and `frame/plan.md` *Alternatives considered*, the first row.
- Whether `batch_run`'s restore after its baseline is in scope: `frame/design.md` *Grounding*, the probe row and the rules 12 and 19 row.
- Which statements of `not restored` are behind the code: `frame/design.md` *Grounding*, the `not restored` class row.
- Whether the timed-out and interrupt cases run on Windows: `frame/plan.md` *Alternatives considered*, the Windows row.
- Whether the message `restore` raises is this work's, and where the build starts: `frame/design.md` *Grounding*, the #1393 row and the orchestrator's row, and `frame/plan.md` *Alternatives considered*, the two rows on the message.
- Whether the new descriptions get a text case: `frame/plan.md` *Alternatives considered*, the text-case row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the new `no baseline` parameters, one pair and batch, pass on CI's `windows-latest` legs? | a measurement | Pass: nothing changes. Fail: the restore after a baseline behaves differently on Windows, and the phase or a fix pass reads the failure before deciding between a fix and a POSIX-only `skipif` with its reason, as the neighbouring cases carry | They pass, as the existing `rewritten` and `removed` restore cases and the `no baseline` cases already do there. No machine in this session runs Windows, so no probe could answer it; the pull request's CI run does | answered 2026-11-05 by the orchestrator, from a measurement: they pass. The `workflow_dispatch` run 42018700617 of `tests` at f7891943 passed on all four `windows-latest` legs, and with `-rfEs` the logs list only the three POSIX-only parameters (`one-pair-timed-out`, `batch-timed-out`, `batch-interrupt`) as skipped, so the two `no baseline` parameters ran and passed |
