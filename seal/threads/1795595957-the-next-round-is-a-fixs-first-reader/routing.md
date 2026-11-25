# Routing: 1795595957-the-next-round-is-a-fixs-first-reader

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/1615-the-next-round-is-a-fixs-first-reader |

Answered 2026-11-25 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-25, once for the four issues #1612, #1613, #1614 and #1615 of `release: 0.39.0`. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The issue changes the review skill's comparison table and who reads a records-only fix, which `skills/code-review/SKILL.md`, `skills/code-review/orchestration.md` and `agents/sealer.md` state and `skills/code-review/scripts/chain_check.py` holds. A defect there lets a fix reach a pull request unread.
- **Planning, framer.** The issue leaves open which record axes carry a check, how the sealer reads a records-only fix in place of a round, and which mechanism beside the text gives a fix an independent reader before the next round. On 2026-11-25 the owner directed that every mechanism the harness and the plugin offer is weighed beside instruction text (`seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md` *Judgments of the run*, merged at `8d99b99e2`), and #1613 handed this item a `SubagentStop` `agent` hook to probe first, which the orchestrator measured before this routing (`trail/subagentstop-probe.md`).
- **Implementation, crafter.** The diff spans the review skill, its orchestration, the sealer's definition and the tests that hold them.
- **Review, through the review chain.** Whether the axes and the reader read one way to a proofer and a sealer is a judgment a round reads.
- **Automation, yes.** Every line of the issue's *Done when* was read before the batch. The first line is delivered in this tree. The second line counts rounds and withholds in the next release; that reading comes after this release, so it goes to `seal/follow-up.md` with the owner as its answerer, and the run does not wait on it.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.39.0` at `a9cc9cf93`, the squash of #1614 (PR #1618), and this item is the last of the release.
