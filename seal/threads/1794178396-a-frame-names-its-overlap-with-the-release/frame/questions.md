# Questions for the planner: a frame names its overlap with the release's other work items (#1443)

The ticket left these judgments open, and the tree answered each; the grounds stand where each line points.

- Where a frame names its overlap: a new section of `frame/plan.md`, `frame/plan.md` *Alternatives considered* rows A and E.
- Whether the orchestrator could keep choosing the merge order alone: `frame/plan.md` *Alternatives considered* row B.
- Whether a script could compute the overlap from paths: `frame/plan.md` *Alternatives considered* row C, on `frame/design.md` *Grounding* G9.
- Whether items that share a file wait to build: `frame/plan.md` *Alternatives considered* row D, on `frame/design.md` *Grounding* G12.
- Who settles two plans that state opposite orders: `frame/design.md` *Scope* item 4.
- When the later item of an ordered pair takes the base in, and whether every branch should: `frame/design.md` *Scope* item 5 and `frame/plan.md` *Alternatives considered* row G.
- Whether a document of the policy root changes: `frame/design.md` *Grounding* G3 and G14.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Did any pair of 0.36.0's work items meet at the merge where no plan's *Overlap with the release* named it, or merge out of the order the plans state? The tree cannot answer it before the release's merges happen, and no probe can stand in for them. | a measurement | No unnamed meeting: the section stands as built. An unnamed meeting: its kind (a shared file, or a check meeting content) goes to the settle, which weighs the section under `skills/core/SKILL.md` *The rule a mechanism is kept against*. The orchestrator reads the release's merge commits and the plans' sections at the release. | The section and the merge order stand as built. | open |
