# Questions for the planner: the settle drafts the released operations literally (#1217)

The ticket left these judgments open, and the tree or a probe answered each. Nobody reopens them:

- Whether `copies` is the literal pass, or a part of it: a part, and it stays as #1216 merged it. `frame/design.md` G7 and D5, `plan.md` A2, A3, A17 and A18.
- Which applier the draft uses: #953's `apply_op`, restored. `frame/design.md` G8 and P1, `plan.md` A1.
- Which step the issue's "step 2" is: step 4 since #1054. `frame/design.md` G3.
- How "one table row" and "the section's last table" are read: `frame/design.md` G9 and *Scope* item 2, `plan.md` A11 and A12.
- Where the script stops and the session's judgment starts: `frame/design.md` *Where the script stops and the session's judgment starts*.
- How the draft answers the failures #1035 named for a script that writes `docs/`: `frame/design.md` D2, `plan.md` A13 and A14.
- What the draft does on a second run, its exit code, and what it refuses: `frame/design.md` *Scope* items 3 and 4, `plan.md` A8, A9, A10 and A15.
- Which policy sentence changes, and whether it collides with a pending design: `frame/design.md` G5 and P2.
- Whether the cheat-sheet rows and the changelog fragment change: `frame/design.md` G14 and G15.
- Whether a comment on the issue changes the request: it has none, `frame/design.md` G1.

No row is open for a person.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which test modules outside a phase's narrow run turn red once the skill's opening sentence, step 4, the `README.md` and `README.ko.md` rows, `settle.py`'s docstring change. The reason no probe answers it here: it is the suite's behaviour, and the framer runs none of the repository's test modules (contract rule 2) | a measurement | A module in the phase's narrow run turns red: the phase fixes what it reads and records it in its `trail/phases/phase-N.md`. A module outside it turns red: the orchestrator's broad gate finds it, and the fix goes through a round. None turns red: the row closes on the phase runs and the gate's record | The narrow run is each phase's *Verified by* set, and the suite beyond it is `unverified`, answered by the orchestrator's broad gate | open |
| Q2 | Whether `apply_op` keeps a CRLF document's line ends through each kind, as G8's function did with its `nl`. The reason the tree does not answer it here: no document of the policy root is CRLF in this repository (executed: `grep -lU $'\r' docs/*.md` lists none), so P1 never met one | the work | It keeps them: a case pins it. It does not: the phase reads and writes with `newline=""` and keeps the document's line end in what it inserts | Line ends kept, with one case | open |
