# Questions for the planner: the orchestrator's acts table goes, with the test that holds it (#506)

The ticket left these open, and the tree answered each one. They are not
reopened here.

- Whether the table and its enumeration stay: `frame/design.md` *Scope* D1,
  and `frame/plan.md` *Alternatives considered* A3 to A5.
- Which of #506's two repairs is built, or neither: `frame/design.md` *Scope*
  D2, and `frame/plan.md` *Alternatives considered* A1 and A2.
- Whether #506 item 1's docstring case is built, for this module or for every
  module: `frame/design.md` *Grounding*, the probe row, and `frame/plan.md`
  *Alternatives considered* A7.
- Whether the work edits `docs/` directly or states a rule change:
  `frame/design.md` *Grounding*, the *Document layout* row, and
  `frame/plan.md` *Alternatives considered* A6.
- Whether the `Orchestrator:` marker changes: `frame/design.md` *Scope* O1,
  and `frame/plan.md` *Alternatives considered* A8.

Assumed, because a different answer would not change what is built: the
22 `.test_durations` entries are removed by hand in the phase's commit. If
they were left, the CI durations job's `--clean-durations` would drop them
at its next run.

No row is open.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
