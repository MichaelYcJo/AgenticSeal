# Questions for the planner: 1793437163-fields-stand-in-marked-blocks (#1198)

The judgments the issue left open that the tree answered, each with its grounds where it stands:

- Build or drop: build. `frame/design.md` *The review*, *Why build, and what a block does not fix*; `frame/plan.md` A1.
- Which records take blocks: the round records, `guarantee.md` and `trail/gate.md`. `frame/plan.md` A10 and A11. Where this is narrower than the issue's *Done when*, and why each kept form already meets it: `frame/design.md` *Why build, and what a block does not fix*.
- Who moves `plugin.json`: the fragment commit, only where the base does not already read `0.27.0`. `frame/design.md` *Scope* item 11.
- Commands, templates or both: templates assemble the agents' blocks, one reader disassembles every block, and `seal gate --record` assembles its own. `frame/plan.md` A5a and A5b.
- The mark and the body: a fence with the info string `seal`, `<key>: <value>` lines, the kind named by the first key. `frame/plan.md` A2, A3, A4.
- Stacking: a close block appended by the fix pass; a verdict block per sealer run; a run block per broad run. `frame/plan.md` A6, A16, A11.
- Where the grammar lives: `hooks/lib/fields.py`, not the policy root. `frame/design.md` *Grounding*, the policy-root row; `frame/plan.md` A8.
- Records written before the change: refused with one message naming the template. `frame/design.md` *Scope* item 9; `frame/plan.md` A9.
- #1121 and #1122: #1121 is already closed in 0.26.0; #1122 closes here. #1125, #1126, #1128, #1150 and the rest of milestone 75 keep their place. `frame/design.md` *The order against milestone 75*.
- The comment's two YAML readers: in, as Scope item 10. `frame/plan.md` A15.
- The spelling of the guarantee's verdict key: `Verdict:` as today. `frame/plan.md` A14.

Assumed in writing, because a different answer would not change what is built:

- No eval run is part of this work. The proofer's and the sealer's next comparison runs both sides fresh (`frame/plan.md` *Operational impact*).
- No question goes to a person in this run: `routing.md` answers `Automation` `yes`, and no row below is a person's.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a case of `tests/behaviour/test_one_word_one_meaning.py` pin a phrase this work rewords, such as "labelled line"? The tree cannot answer it before the wording is written, and a probe would need the phase's text. | the work | Keep the phrase where it names a fact the change keeps; change the case in the same commit where the phrase is wording, as #1167 phase 1 did. The module's removal is #1197's, not this work item's | change the case in the same commit, and name it in the phase record | answered by phase 1: yes, `GATE_SEAL_NAMES` pinned the gate's names, and 99ca2178 lets it take "`seal` block" in the same commit (`trail/phases/phase-1.md`); later phases answer it the same way where they reword |
| Q2 | Do the sealer cases' `truth-*.md` graders still read the outcome each was written for once their scaffolds write blocks? Each grader is a regex over the sealer's report, and whether one still finds its defect depends on the scaffold text phase 3 writes. | the work | Where a grader still reads its outcome, it stays; where it does not, it changes with its scaffold, and the case's recorded sides stop comparing, which *Operational impact* already states | each grader is read against its new scaffold in phase 3, and the phase record names each one changed | open |
