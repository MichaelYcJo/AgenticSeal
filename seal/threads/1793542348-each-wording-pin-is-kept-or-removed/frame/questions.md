# Questions for the planner: each wording pin is kept or removed (#1233)

The judgments the issue left open that the tree answered, so nobody reopens them:

- Which modules and asserts the work reads, after #1243 and #1231 moved since `bf9efcba`: `frame/design.md` *Grounding* G2.
- Whether an assert is read alone or with its case: `plan.md` *Alternatives considered* A2.
- How a kept assert names its fact: `plan.md` A5.
- Which `docs/` check lines change, and to what reader: `frame/design.md` G5 and G7.
- What happens to the module a `docs/` check line names that the ruling empties: `frame/design.md` G4, and `plan.md` A6 and A7.
- Which modules leave whole in this change: `frame/design.md` G6.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which test modules outside a phase's narrow run turn red once its asserts, cases and modules go. The reason no probe answers it here: it is the suite's behaviour, and the framer runs none of the repository's test modules (contract rule 2). | a measurement | A module in the phase's narrow run turns red: the phase fixes the place it reads and records it in its `trail/phases/phase-N.md`. A module outside it turns red: the orchestrator's broad gate finds it, and the fix goes through a round. None turns red: the row closes on the phase runs and the gate's record. | The narrow run is each phase boundary's set, and the suite beyond it is `unverified`, answered by the orchestrator's broad gate | open |
| Q2 | Which side of *The criterion* each of the 506 listed asserts falls on. The reason the tree does not answer it here: the framer read about two dozen of the 259 cases whole, those of the three modules of design G6 and those behind eight check lines of G5; the rest is the build itself, and a literal that holds a code span inside a sentence is decided by what the assert is about, which only reading its case settles. | the work | Kept: the assert stays with a comment naming its fact and reader. Removed: the assert goes, and its case goes when nothing kept is left in it. A phase that meets a literal it can read either way names it, with the side it took and why, in its `trail/phases/phase-N.md`, for the proofer. | *The criterion* as `frame/design.md` *Data & interfaces* states it | open |
| Q3 | Whether a `docs/` check line other than the two of `## Rule changes` loses its last reader under a phase's ruling. The reason the tree does not answer it here: the span probe of design G5 cannot see a listed assert that reads a skill's restatement of a `docs/` rule, and which asserts go is Q2's. | the work | None does: nothing more. One does: the phase keeps that assert unchanged and names it and the line in its phase record, and the orchestrator adds both to the successor issue of design Scope item 7, whose frame states the line's change. | Design Scope item 9 | open |
