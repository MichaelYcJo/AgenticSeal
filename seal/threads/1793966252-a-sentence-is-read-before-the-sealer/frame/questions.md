# Questions for the planner: 1793966252-a-sentence-is-read-before-the-sealer

The tree answered these, and none is reopened here:

- Whether #1415's item 3 pays its cost: `frame/plan.md` *Alternatives considered*, the row on a new crafter read.
- Where the body's first part lives: `frame/plan.md` *Alternatives considered*, the `pr.md` row and the scratchpad row.
- Whether a script checks each quote: `frame/plan.md` *Alternatives considered*, the row on a quote script.
- Whether the run's comparison table and the broad run's figures stay in the body: `frame/design.md` *Grounding*, the `skills/verify/orchestration.md` row, and `frame/plan.md` *Alternatives considered*, the row on the broad run's figures.
- Whether `docs/` is edited in place or through `## Rule changes`: `frame/design.md` *Grounding*, the `skills/implement/SKILL.md` row.
- Whether the sealer names the round that missed a sentence: `frame/plan.md` *Alternatives considered*, the row on that label.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Who commits the repair of a round finding located in `pr.md`, and what does the fix pass's close block name? The tree cannot answer it: `agents/crafter.md` *Job* names no write of `pr.md`, and the close block is the fix pass's. The tree's precedent is a finding located in a frame file, and the commits that closed those were squashed away (`git cat-file -e` of each `fixed` commit that the round records under `seal/threads/` name for such a finding exits 128, executed) | the work | (a) The orchestrator commits the repair before the fix pass, and the pass's close block reads `fixed <that commit>`, as for a frame file the crafter does not write. (b) `agents/crafter.md` *Job* gains `pr.md`, so the fix pass repairs it; the record the orchestrator writes would then have two writers | (a) | answered (a) by the work, `trail/phases/phase-2.md` |
| Q2 | Do the sealer's evals still hold once their `OWN_PART` stands in `pr.md`? No probe here can answer it: an eval run starts a paid model session, and the milestone `release: 0.34.0` (renamed from `release: 0.33.1`) puts the paid run on the owner's machine after the merge | a measurement | Holds: nothing follows. Fails: the scaffold in `evals/scripts/rule_cases.py` writes a work item the sealer reads differently, and a fix goes into the next work item | Phase 2 writes the cases again and runs `tests/behaviour/test_evals_layout.py`; the eval waits for the milestone's paid run | open |
