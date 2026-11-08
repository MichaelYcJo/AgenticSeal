# Questions for the planner: 1794096494-compare-reads-a-grader-with-a-string-target

The judgments the issue left open that the tree answered, each with its
grounds where it stands:

- Whether the guard tests for a string or for a mapping: `plan.md` *Alternatives considered*, row 1.
- Whether the fix belongs in the reader, in the side's writer or in the graders: `plan.md` *Alternatives considered*, rows 2 to 6.
- Which graders carry a target that is not a mapping: `frame/design.md` *Grounding*, the class row.
- Whether `regrade` gets a case of its own: `frame/design.md` *Scope*, the first item under Out.
- Where on the ladder the change sits, and whether it states a rule change: `frame/design.md` *Grounding*, the ladder row and the policy root row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does `compare` read the paid crafter pair of #1178, the sides at `33ced573b` and `4531133b7`, as `Verdict: pass` at this work item's HEAD? The tree cannot answer it because no side is committed, and no probe here can run because the side files are not in this environment. The run is free, since `compare` runs no eval. | a measurement | Run `evals/scripts/noninferiority.py compare --agent crafter --phase <N> --old <side at 33ced573b> --new <side at 4531133b7> --out <file>` at HEAD: a `Verdict:` line confirms the fix on the real pair, and a refusal or a traceback names a shape the synthetic case of `frame/design.md` *Scope* item 3 does not hold. | The synthetic case stands as the proof, and the issue's `Verdict: pass` stays the issue author's claim. | open |
