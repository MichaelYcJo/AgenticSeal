# Routing: 1795742081-records-name-the-base-and-version-as-values

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1633-records-name-the-base-and-version-as-values |

Answered 2026-11-27 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-27 for the issues of `release: 0.39.2`, and on the same day agreed that #1633 joins the release and runs in parallel with the work item for #1624, #1628 and #1629, with its framer on Fable. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The issue asks which values a record cites by role or by command, which every party that writes a record reads in the templates and the writing rules.
- **Planning, framer, on Fable.** The owner's direction: the framer runs on Fable where the item changes what every party reads, and the crafter, the proofer and the sealer run on Opus.
- **Implementation, crafter.** The change is to templates, rules and the cases that hold them, built under the crafter's rules.
- **Review, through the review chain.** Whether a rule reads one way to every party that writes a record is a judgment a round reads.
- **Automation, yes.** The issue's *Done when* asks for template and rule text. It is delivered in this tree and needs no real session, credential, outside service or permission.
- **Destination, open the pull request**, as under `complete`.
- **Branch.** Cut from the open release branch after #1620's pull request merged into it, in a worktree, because another work item of the same release is built in the main checkout at the same time.
