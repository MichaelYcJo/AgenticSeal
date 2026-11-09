# Questions for the planner: 1794200907-agents-write-commands-the-parser-reads

The issue left these judgments open, and the tree answered each. The grounds stand where each line points.

- Which command shapes prompted a person, and how often per window: `frame/design.md` G8 and G9.
- Whether the prompts rose with the gates' removal in 0.33.0: `frame/design.md` G8.
- Whether the spawn prompts' existing lines already cover the shapes that recur: `frame/design.md` G9, and `frame/plan.md` *Alternatives considered* row 8.
- Where the rule lives: `frame/plan.md` *Alternatives considered* rows 1, 2 and 3.
- How the rule reaches the orchestrator: `frame/design.md` G17, and `frame/plan.md` *Alternatives considered* rows 9 and 10.
- Whether to stop asking agents to remove what they made under the scratchpad, or to have them write the removal in a form the parser reads: `frame/plan.md` *Alternatives considered* rows 4 and 5.
- Where the crafter's scratch stands, and where the new clauses are pinned: `frame/design.md` G18, and `frame/plan.md` *Alternatives considered* rows 11 and 12.
- Whether anything checks an agent's command: `frame/plan.md` *Alternatives considered* row 6.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the prompts in the two shapes `frame/design.md` G9 names stop, for the agents and for the orchestrator, once a run goes under a plugin that holds rule 21? No run under the rule exists at framing time, and this repository's agents receive the installed plugin's contract, so neither the tree nor a probe can answer it now. | a measurement | Read the transcripts of the first runs under 0.37.0 as `frame/design.md` G7 read them, split by party as G8 splits them. If the two shapes stop prompting, the rule holds. If they recur in subagents, the next question is the rule's wording. If they recur in the top-level session, it is whether step 1's pointer reaches the orchestrator. | Rule 21 stands. The reading is posted to the open flow-measurement log and never used to block. | open |
