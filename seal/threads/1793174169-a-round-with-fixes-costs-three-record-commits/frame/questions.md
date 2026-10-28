# Questions for the planner: 1793174169-a-round-with-fixes-costs-three-record-commits

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `frame/design.md` or
in `frame/plan.md`'s Alternatives table.

1. **No check changes, although `routing.md` says the chain check's
   acceptance moves.** `routing.md`'s *Why this way* was written before the
   frame. A refusal of how a finding's two lines were committed could be
   cured only by rewriting the branch's history, and it adds a mechanism
   that removes nothing (`frame/plan.md`, *Alternatives considered*, row D).
   `chain_check.py` is unchanged. Row Q1 below puts the one part of this a
   person may want otherwise.
2. **The orchestrator keeps no step after the fix pass.** The issue allows
   one ("If the orchestrator is to keep a step after the fix pass"). The
   verifying round already weighs every close
   (`skills/code-review/orchestration.md:100`), so an orchestrator's doubt
   goes into that round's prompt (`frame/design.md`, *Scope*, item 1).
3. **`skills/implement/SKILL.md:484-489` is not edited.** It already names
   the fix pass as the writer of both lines and cites the review record. The
   issue asks for an edit there only if the orchestrator keeps a step.
4. **The answer commit stays separate from the fix commit.** A `fixed`
   verdict names a commit that already exists, and a commit cannot name
   itself (`frame/plan.md`, row A, and rows C and E for the two ways of
   removing the commit).
5. **No file of a parallel work item is edited.** The five files this work
   edits are not on the lists the spawn prompt gives for #1042, #1043, #1055,
   #1056 and #956. #1043 adds a check of citations in parallel. Each
   citation this work adds names a heading that exists at `5287dd42`:
   `docs/the-review-record.md` *The round record* and *The run*.
6. **The cause is found, and no question is left for a measurement.**
   `frame/design.md`, *Scope*, item 4, names the spawn prompts by
   transcript line.
7. **Which case each new clause joins is the crafter's call.** The frame
   names the group for each scenario. `agents/crafter.md` *A new test starts
   from its group* decides the exact case, and either answer builds the same
   text.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should `chain_check.py` also refuse a finding whose `verdict:` left `open` in a commit that did not also write its `answer:`, so that a split like #955's fails the pull request instead of resting on the orchestrator's text? The tree weighs this (`frame/plan.md`, row D) and finds against it on cost and cure. Whether a mechanism is worth its cost before 1.0 is still the owner's judgment, and the two answers build different code. | a person | (a) No check. The rule stays text in `skills/code-review/orchestration.md` and `agents/crafter.md`, and a split costs one record commit per round until somebody reads the history. (b) A check. `chain_check.py` walks each round record's history at the pull request, and a split already committed can be cured only by rewriting the branch's history. That needs a case per shape, red first, and it touches the file #1020 edits next. | (a), no check. The build goes on without one. | open |
