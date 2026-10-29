# Phase 2: 1793240966-the-framer-has-no-read-only-probe

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | e8051ef0 |

## What this phase was asked

Build `frame/plan.md` *Phases* row 2 against the frame at `d76aec0f`.
`agents/framer.md` gains the new rule in `## Rules`, its `check:` line
naming `evals/behaviour/framer/rule-framer-sharp-s/` and
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`,
and the five amendments `frame/design.md` *Data & interfaces* lists: the
*Job* paragraph, step 5, step 8, the *Never* list and the residue rule.
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`
gains a case for `<scratchpad>/<work-item-id>/frame/`, and its docstring's
class line counts the framer. The byte count of `agents/framer.md` before
and after goes into this record for the pull request body.

## What this phase found

**The design's residue wording would have broken a pinned sentence.**
`frame/design.md` *Data & interfaces* says "Every row owes a reason the
tree could not answer it" becomes "a reason neither the tree nor a probe
could answer it". `tests/behaviour/test_waiver_decided_at_start.py:793`
asserts the phrase "owes a reason the tree could not answer it", and
`plan.md` *Technical context* says "Every sentence the existing cases pin
stays". The rule now reads "Every row owes a reason the tree could not
answer it and no probe could either", which keeps the pin and carries the
design's meaning. `gaps.md` records the divergence.

**The design's module list for S7 misses `tests/github/test_rules.py`.**
`git grep -l -e framer.md -e '"agents"' -- tests/` lists 44 modules, and
`tests/github/test_rules.py` is not among them, though the plan names it.
It was added to the run by hand.

**How the new case was seen red (executed).** With
`agents/framer.md` unchanged since `c48cd5e3` (`git diff --quiet c48cd5e3
HEAD -- agents/framer.md` exited 0), `bin/test
tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py
-q -p no:xdist` exited 1: `test_the_framers_probe_is_named_for_the_work_item`
failed on its first assertion, and the three other cases passed. After the
rule it exited 0.

**Mutation (executed).** `seal mutate agents/framer.md` with two mutants,
the work item id dropped from the directory and the sentence saying agents
of one session share one scratchpad removed: the baseline passed and both
went red; exit 0.

**The narrow run (executed).** `bin/test` over the 44 modules the grep
lists and `tests/github/test_rules.py`, in one command, exited 0: 1443
passed, 8 skipped. Among them are
`tests/text/test_a_question_says_who_can_answer_it.py` (S6),
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`, and
`tests/behaviour/test_waiver_decided_at_start.py`. `uvx ruff check` and
`uvx ruff format --check` over the changed test module exited 0.

**The preload grows by 1,555 bytes (executed).** `agents/framer.md` is
10,334 bytes at `c48cd5e3` and 11,889 bytes at `e8051ef0`, 212 lines.

**Two other descriptions of the framer stay true, and were left.**
`agents/framer.md`'s frontmatter says the framer "writes no code, and
builds nothing", and `README.md`'s framer row says it "writes no code". A
probe script lives in the scratchpad and is gone before the hand-back, so
neither sentence is made false.

**The cross-references follow the file's own form.** Step 5 cites the new
rule in italics, *A question a command answers is answered by running it*,
the way step 4 cites *A design states its rule changes*. The rule cites
contract rules 2, 7, 9 and 17 by number and restates none of them.
