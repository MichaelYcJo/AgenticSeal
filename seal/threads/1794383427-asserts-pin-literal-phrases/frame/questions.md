# Questions for the planner: the literal asserts of tests/text and tests/behaviour are weighed a second time (#1488)

The judgments the issue left open that the tree answered, so nobody reopens them:

- Which asserts the work reads, beyond the two forms the issue counted: `frame/design.md` *The listing* and *Scope* item 1, and `plan.md` *Alternatives considered* A2 and A3.
- Which of those asserts read a document and which read a program: `frame/design.md` *What an assert reads*.
- What tells the absence of a removed design from an absence a rule forbids: `frame/design.md` *The criterion*.
- Whether a kept literal stays whole: `plan.md` A6 and A7.
- What happens to `tests/behaviour/test_no_document_names_the_old_roots.py` and to the check line that names it: `frame/design.md` *Grounding* G5, and `plan.md` A8 and A9.
- How a `docs/` check line changes when a ruling takes its last reader: `frame/design.md` G6 and *Scope* item 9, and `plan.md` A10.
- Whether the rows of `.test_durations` leave with their cases: `frame/design.md` G8 and `plan.md` A11.
- Which modules are left to the sibling work items, and which merges first: `plan.md` *Overlap with the release*.
- With which commands the counts are recorded, given that the issue's absence count is not reproduced: `frame/design.md` G3 and *The counts*.

No row below needs a person.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which test modules outside a phase's narrow run turn red once its asserts, cases and helpers go. The reason no probe answers it here: it is the suite's behaviour, and the framer runs none of the repository's test modules (contract rule 2). | a measurement | A module in the phase's narrow run turns red: the phase fixes the place it reads and records it in its `trail/phases/phase-N.md`. A module outside it turns red: the orchestrator's broad gate finds it, and the fix goes through a round. None turns red: the row closes on the phase runs and the gate's record. | The narrow run of `frame/design.md` *The narrow run* is each phase boundary's set, and the suite beyond it is `unverified`, answered by the orchestrator's broad gate | open |
| Q2 | Which side of *The criterion* each listed assert of the four groups falls on, and which of them read a file's text at all. The reason the tree does not answer it here: the framer read whole the cases behind `frame/design.md` *Worked examples* and the old-roots module, and read the others as rows of *The listing*. What a right side reads, and whether a short literal is a fact or a word, is settled only by reading the case, which is the build. | the work | Kept: the assert stays with its comment and its literal cut to the fact. Removed: the assert goes, and its case goes when no assert is left in it. Not ruled: the assert reads behaviour or a built text and is unchanged. A phase that meets a literal it can read either way names it, with the side it took and why, in its `trail/phases/phase-N.md`, for the proofer. | *The criterion* and *Worked examples* of `frame/design.md` | open |
| Q3 | Which check lines under `docs/`, beyond the two of `## Rule changes`, name a module that keeps no case reading the line's rule after a ruling. The reason the tree does not answer it here: it follows from Q2's rulings, line by line. | the work | None does: nothing more. One or more does: each phase names the line and the module in its phase record, and after phase 4 the orchestrator sends the framer those lines as one fold, which adds a `change` for each to `frame/design.md` `## Rule changes`. | `frame/design.md` *Scope* item 9 | open |
| Q4 | Whether a ruling leaves a module with no `test_*` function while a `docs/` check line names it. The reason the tree does not answer it here: it follows from Q2's rulings. | the work | None is left so: nothing more. One is: the file stays, the phase names it in its phase record, and the orchestrator files one issue for its deletion after the settle and names it in the pull request body. | `frame/design.md` *Scope* item 6 and its *Out* | open |
