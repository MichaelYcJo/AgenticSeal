# Routing: 1795569535-a-fix-writes-a-count-into-a-record

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1613-a-fix-writes-a-count-into-a-record |

Answered 2026-11-25 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-25, once for the four issues #1612, #1613, #1614 and #1615 of `release: 0.39.0`. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The change moves a rule into `skills/agent-contract/SKILL.md`, which every agent reads, and the rule restates what other text states (the contract's rule that keeps a count from serving as a coordinate, and the crafter's, framer's and orchestrator's procedures for a fix and a fold). Finding every statement of it is a reader's work (contract rule 12).
- **Planning, framer.** The issue leaves open where the rule stands and how it reaches each party that edits a record after round 1: the crafter's fix pass, the framer's fold, and the orchestrator's record edits.
- **Implementation, crafter.** The diff spans the contract and the procedures that cite it.
- **Review, through the review chain.** Whether each party that edits a record reads the rule, and whether the old statements were removed in the same commit, is a judgment a round reads.
- **Automation, yes.** Every line of the issue's *Done when* was read before the batch. The first line is delivered in this tree. The second line counts fix-made findings in the next release's classification of a repository that runs the chain; that reading comes after this release and is no step of this run, so it goes to `seal/follow-up.md` with the owner as its answerer, and the run does not wait on it.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.39.0` at `fd89e2114`, the v0.38.8 merge on `main`. The release holds #1612, #1614 and #1615 after this item, in that order; this item merges first and moves `plugin.json` to 0.39.0, a minor version, because #1614 and #1615 are `feat:`.
