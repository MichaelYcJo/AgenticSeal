# Questions for the planner: 1793853198-tests-name-the-gate-that-exists

The ticket left these judgments open, and the tree answered them. Do not reopen them:

- Which of the 15 unclassified lines are in the class, and what each becomes: `frame/design.md` *D1* and *Left as they stand*.
- Whether the class reaches past the words "commit gate", to the git hooks the gate ran through and to text written while it stood: `frame/design.md` *Grounding*, methods M2 and M3.
- Whether a failure message counts among the assertions the issue puts out: `frame/plan.md` *Alternatives considered* A6.
- Whether past-tense narrations of the gate are rewritten: `frame/plan.md` A5.
- Whether the dead helper `tests/conftest.py#fired` is corrected or removed: `frame/plan.md` A7.
- Whether a case is added to keep the class from returning: `frame/design.md` *D2* and `frame/plan.md` A2.
- Whether any commit-gate sentence on this list belongs to #1359: `frame/design.md` *Grounding*, the bare-commit row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does `hooks/lib/routing.py`'s module docstring join this work item? It still speaks of "the gate" in the present ("so the gate goes back to asking", "Imported by the gate and by the hygiene check", "they are most of what the gate sees"). The tree cannot answer this, and no probe can, because it is a choice of scope: #1352 and the milestone description both name `tests/` and `.github/scripts/`, and the file is shipped hook code. | a person | (a) It joins. The phase rewrites the docstring as D1 rewrites the tests, under a `test:` patch whose issue does not name it. (b) It does not join. The orchestrator names it in the release's report so that an issue can be filed, and this pull request stays within its issue | (b): it does not join, and the orchestrator names it in its report | open |
| Q2 | What is the exact wording of each N and D row's replacement? Each row in `frame/design.md` *D1* fixes what the rewrite leaves, and the sentence is written against the file's surrounding text. | the work | The phase writes each sentence and records it beside its row in the phase record | the phase's wording, within the row's *What the rewrite leaves* | open |
