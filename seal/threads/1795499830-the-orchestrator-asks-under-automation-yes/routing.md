# Routing: 1795499830-the-orchestrator-asks-under-automation-yes

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1608-the-orchestrator-asks-under-automation-yes |

Answered 2026-11-24 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-24, for #1608 alone, the one issue the request named. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The change adds a `PreToolUse` hook to `hooks/hooks.json`, and a defect in a hook stops every session that runs it. It also restates, in `skills/implement/orchestration.md`, where a rule that restricts agents may come from and what the batch reads, which other text states.
- **Planning, framer.** The issue leaves open the form a question takes to state why no default can be taken, which the hook reads exactly, and how the hook finds the open work items of the session's repository and its worktrees.
- **Implementation, crafter.** The diff spans a new hook script, `hooks/hooks.json`, two sections of `skills/implement/orchestration.md` and a test module.
- **Review, through the review chain.** Whether the hook refuses only where the rule asks, and never blocks a session with no open work item, is a judgment a round reads.
- **Automation, yes.** Every line of the issue's *Done when* was read before the batch: none needs a real session, a credential, an outside service or a permission, and the case that holds the hook runs in the suite. The fork's hook, MichaelYcJo/owlery#181, is that repository's work and outside this one.
- **Destination, open the pull request**, as under `complete`.
- **Branch, and the order.** The branch is cut from `origin/release/v0.38.8` at `7c8f67103`, the v0.38.7 merge on `main`. It is the release's first pull request, so it moves `plugin.json` to 0.38.8.
