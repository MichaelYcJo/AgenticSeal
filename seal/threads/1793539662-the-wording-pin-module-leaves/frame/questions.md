# Questions for the planner: the wording-pin module leaves (#1243)

The judgments the issue left open that the tree answered, so nobody reopens them:

- Whether the reader of the writing-style line reaches `README.md` and `README.ko.md`: `frame/design.md` *Grounding* G8, and `plan.md` *Alternatives considered* A4.
- What the rewritten paragraph of *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* says, and whether it carries a check line: `frame/design.md` *Grounding* G7, and `plan.md` A5.
- Whether a coordinate the issue took at `ad4556f4` moved at the settle: `frame/design.md` *Grounding* G5.
- Whether a sentence names the module in prose alone: `frame/design.md` *Grounding* G6.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which test modules other than `seal rules --check` turn red once the module is deleted. The reason no probe answers it here: it is the suite's behaviour, and the framer runs none of the repository's test modules (contract rule 2). The comment of 2026-11-01 on #1243 re-homes the same row from `v0.27.2:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/gaps.md` *Not verified*. | the work | A module in `frame/design.md` *The narrow run* turns red: the phase fixes the place it reads and records it in `trail/phases/phase-1.md`. A module outside that list turns red: the orchestrator's broad gate finds it, and the fix goes through a round. None turns red: the row closes on the phase's run and the gate's record. | The narrow run is the phase boundary's set, and the suite beyond it is `unverified`, answered by the orchestrator's broad gate | open |
