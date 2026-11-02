# Questions for the planner: the orchestrator's part of a pull request body cites its records (#1290)

The issue left these judgments open, and the tree answered each one. They are not reopened here:

- Whether the rule is held by a check: no (`frame/design.md` G1; `plan.md` *Alternatives considered* A3).
- Which file holds the rule: `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, with the other files pointing there (`frame/design.md` G9 and G10; `plan.md` A6 and A7).
- Whether the orchestrator's part may state a record's fact at all, against #1044's "only what no record holds": yes, with the record's sentence or coordinate (`frame/design.md` G4 and G5; `plan.md` A2 and A4).
- Whether the orchestrator also checks a copied sentence against the tree: no, the sealer does (`frame/design.md` G6 and G13; `plan.md` A8).
- Whether the edit can merge beside #883: yes (`frame/design.md` G11).

Assumed, because no answer changes what is built: the owner's local memory note that held the practice stays the owner's to keep or retire. It is outside the tree (`frame/design.md` *Scope*, Out).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does any test module beyond the phase's narrow run read a sentence this work rewrites? No probe answers it here, because the answer is the suite's behaviour and the framer runs none of the repository's test modules (contract rule 2). `git grep -n -e "restates no record" -e "names the record's path" -e "part does not restate" -e "기록에 없는 것만" -e "restates a record" -e "what no record holds" -- tests` prints nothing and exits 1 (executed), so no pin of the replaced sentences was found by those spellings. A module that globs `skills/` may still read one by another spelling | the work | None turns red: the row closes on the phase's run and the gate's record. One in the narrow run turns red: the phase fixes the place it reads and records it in `trail/phases/phase-1.md`. One outside it turns red: the orchestrator's broad gate finds it, and the fix goes through a round | The phase's narrow run is the set `plan.md` phase 1 names, and the suite beyond it is `unverified`, answered by the orchestrator's broad gate | open |
