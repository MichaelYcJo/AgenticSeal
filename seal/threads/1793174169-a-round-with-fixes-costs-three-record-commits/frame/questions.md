# Questions for the planner: 1793174169-a-round-with-fixes-costs-three-record-commits

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `frame/design.md` or
in `frame/plan.md`'s Alternatives table. Who commits the fix pass's lines
was not the tree's to answer; it is row Q2, answered by the owner.

1. **No check changes, although `routing.md` says the chain check's
   acceptance moves.** `routing.md`'s *Why this way* was written before the
   frame. A refusal of how a finding's two lines were written or committed
   could be cured only by rewriting the branch's history, and it adds a
   mechanism that removes nothing (`frame/plan.md`, *Alternatives
   considered*, row D). `chain_check.py` is unchanged. Row Q1 below puts
   the one part of this a person may want otherwise.
2. **The orchestrator's one step after the fix pass is written beside the
   fix pass's last step.** Issue #1041 *Done when* bullet 2 asks that such a
   step be "written where the fix pass's step is". The fix pass's last step
   is the end of the paragraph *The fix pass then finds what the fixes left
   standing* in `skills/code-review/orchestration.md`, so the orchestrator's
   commit is stated there (`frame/design.md`, *Scope*, item 1). The
   orchestrator keeps no other step: the verifying round already weighs
   every close (`skills/code-review/orchestration.md:106`), so an
   orchestrator's doubt goes into that round's prompt.
3. **The orchestrator commits at the hand-back, before it spawns the
   verifying round.** The owner's answer says the orchestrator commits the
   lines and does not say when. `skills/implement/SKILL.md` *2. Implement
   test-first, and let each rule name its test* says work in the working
   tree is not visible to the reviewer, so the commit lands before the
   round that weighs the closes (`frame/plan.md`, row C against row F).
4. **`skills/implement/SKILL.md:484-489` is not edited.** It names the fix
   pass as the writer of both lines and cites the review record, which
   stays true, and it says nothing about who commits. The orchestrator's
   step is in the orchestrator's file, and the crafter's exception is in
   `agents/crafter.md` (`frame/design.md`, *Out of scope*).
5. **The answer commit stays separate from the fix commit.** A `fixed`
   verdict names a commit that already exists, and a commit cannot name
   itself (`frame/plan.md`, row F, and rows C and E for the two ways of
   removing the commit).
6. **No file of a parallel work item is edited.** Phase 2 edits the five
   files phase 1 edited and this work item's `changelog.md`, and adds none.
   Each citation the work adds names a heading that exists at `aa8b54cb`:
   `docs/the-review-record.md` *The round record* and *The run*.
7. **The cause is found, and no question is left for a measurement.**
   `frame/design.md`, *Scope*, item 5, names the spawn prompts by
   transcript line, as `grep -n` counts them.
8. **Which case each new clause joins is the crafter's call.** The frame
   names the group for each scenario. `agents/crafter.md` *A new test starts
   from its group* decides the exact case, and either answer builds the same
   text.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should `chain_check.py` also refuse a finding whose `verdict:` left `open` in a commit that did not also write its `answer:`, so that a split like #955's fails the pull request instead of resting on the orchestrator's text? The tree weighs this (`frame/plan.md`, row D) and finds against it on cost and cure. Whether a mechanism is worth its cost before 1.0 is still the owner's judgment, and the two answers build different code. The owner's answer of 2026-10-28 (`guarantee.md:40`) decides who commits the two lines and says nothing about a check, so it leaves this row open. | a person | (a) No check. The rule stays text in `skills/code-review/orchestration.md` and `agents/crafter.md`, and a split costs one record commit per round until somebody reads the history. (b) A check. `chain_check.py` walks each round record's history at the pull request, and a split already committed can be cured only by rewriting the branch's history. That needs a case per shape, red first, and it touches the file #1020 edits next. Under row F it could read only which commit carried the lines, not which party made it, since both parties commit under the same author. | (a), no check. The build goes on without one. | open |
| Q2 | Issue #1041 *Done when* bullet 1 says `skills/code-review/orchestration.md` states that the orchestrator commits the fix pass's two lines as they stand. Phase 1 built the fix pass making that commit itself. Does the fix pass's own answer commit meet the owner's decision, or must the orchestrator make that commit? The sealer raised it (`guarantee.md:38`), and the earlier frame had not named the departure. | a person | (a) The fix pass commits both lines itself, as phase 1 built (`frame/plan.md`, row A). (b) The fix pass writes both lines and commits neither, and the orchestrator commits them as they stand, in one commit for the pass, and writes no `verdict:` of its own (`frame/plan.md`, row F). Phase 2 reworks the build to it. | none: the owner answered before this frame was rewritten | answered 2026-10-28 by the owner, `guarantee.md:40`: (b), the orchestrator makes that commit |
