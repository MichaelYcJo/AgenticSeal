# Routing: 1795759278-the-cores-margin-depends-on-the-path

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1641-the-cores-margin-depends-on-the-path |

Answered 2026-11-27 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-27 for the issues of `release: 0.39.3`, and on the same day put #1630 in the release beside #1639, #1640, #1641 and #1642, and asked that the work run as the release before it did: each framer on Fable, the crafter, the proofer and the sealer on Opus, independent items in parallel lanes, and one broad gate at a time. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **One work item for one issue.** #1641 shares no file with the other two items of the release.
- **Planning, framer, on Fable.** The item decides how the core's size under the harness cap is measured, which governs what every session receives.
- **Implementation, crafter.** The test it changes holds every later sentence added to the core, so its case is seen red against a core grown past the cap.
- **The version move.** This item's pull request carries the release's version move, because it is expected to merge first into the release branch; the framer names the phase that moves `.claude-plugin/plugin.json`, and that phase's commit records the version it writes.
- **Review, through the review chain.** Whether the measure stops depending on the checkout path, and what margin it states, are judgments a round reads.
- **Automation, yes.** #1641's *Done when* asks a measure against a fixed root and a known installed margin. Both are read in this tree, and none needs a real session, a credential, an outside service or a permission.
- **Destination, open the pull request**, as under `complete`.
- **Branch.** Cut from the open release branch, whose tip was the merge of the previous release into `main` when it was cut, 2026-11-27.
