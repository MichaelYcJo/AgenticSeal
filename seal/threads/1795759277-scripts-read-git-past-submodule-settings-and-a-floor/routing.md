# Routing: 1795759277-scripts-read-git-past-submodule-settings-and-a-floor

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1640-1642-scripts-read-git-past-submodule-settings-and-a-floor |

Answered 2026-11-27 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-27 for the issues of `release: 0.39.3`, and on the same day put #1630 in the release beside #1639, #1640, #1641 and #1642, and asked that the work run as the release before it did: each framer on Fable, the crafter, the proofer and the sealer on Opus, independent items in parallel lanes, and one broad gate at a time. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **One work item for two issues.** #1640 and #1642 both concern how the plugin's scripts call git: #1640 the reads of changed and dirty paths that a submodule setting can shorten, and #1642 the oldest git those calls may assume. `lib/gitcmd.py`'s docstring is the home for both, as it is for the keys `argv` sets.
- **Planning, framer, on Fable.** The item judges each git read that a gate decides on, in `chain_check.py`, `seal.py` and `broad_gate.py`.
- **Implementation, crafter.** Each read the frame changes needs a case seen red, so the build stays with a crafter.
- **Review, through the review chain.** Whether a submodule path can change a read's answer, and which git version the plugin states as its floor, are judgments a round reads.
- **Automation, yes.** #1640's *Done when* asks each named read judged, and #1642's asks a stated floor with its reason and a script that says so or stays within it. The floor is read from the git features the tree's scripts use, and none of it needs a real session, a credential, an outside service or a permission.
- **Destination, open the pull request**, as under `complete`.
- **Branch.** Cut from the open release branch, whose tip was the merge of the previous release into `main` when it was cut, 2026-11-27.
