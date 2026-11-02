# Questions for the planner: a head run that pytest stopped with exit 0 does not seal (#883)

The issue left these judgments open, and the tree answered each one:

- Whether a head run that stopped part-way with exit 0 is refused: yes. `frame/design.md` *Grounding* G5, G7 and G9, and `frame/plan.md` *Alternatives considered* rows A and B.
- What the refusal says: `frame/design.md` *Scope* item 2.
- Which stops count: every session `RunRecord.unended` counts, not only a non-empty `stopped`. `frame/design.md` *Grounding* G2, and `frame/plan.md` *Alternatives considered* row C.
- Whether the base is run for a stop: no. `frame/plan.md` *Alternatives considered* row G.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does this repository's own `Broad gate` row (`bin/test -q`) leave any pytest session at `HEAD` stopped part-way, so that the new arm fails this branch's own broad run? The frame could not run the suite: contract rule 2 gives the full suite to the orchestrator's one broad run and to no agent. The nearest evidence is the v0.28.0 tag, where `pytest tests/ -q -n auto` gave `unended 0` (`frame/design.md` G3), but `bin/test` reaches pytest through `.github/scripts/run_tests.py` and this branch adds tests. | a measurement | No session stops: the run passes as before. A session stops: the run fails with the Scope 2 line, and the stop is in the tree; `records/` in the kept output names it, and it is repaired as a `new` failure would be. | No session stops, and the build proceeds. The orchestrator's broad run answers it. | answered 2026-11-03 by the orchestrator: no session stops. The broad run at a4c4e7f3, with the new arm in it, passed (`trail/gate.md`) |
