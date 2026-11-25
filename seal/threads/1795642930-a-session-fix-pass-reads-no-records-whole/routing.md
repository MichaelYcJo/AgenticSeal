# Routing: 1795642930-a-session-fix-pass-reads-no-records-whole

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | the session |
| Automation | yes |
| Branch | fix/1623-a-session-fix-pass-reads-no-records-whole |

Answered 2026-11-26 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-26 for #1623, the one issue of `release: 0.39.1`. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The issue changes who a fix pass's reading of its range and the work item's records binds. `agents/crafter.md` states that reading. `skills/implement/fix-pass.md` sends the crafter to it, and `skills/code-review/orchestration.md` and `skills/implement/orchestration.md` say who makes a fix pass, so finding every statement of who the reading binds is a reader's work (contract rule 12). A defect there shows as a later session that misreads the text, not as a suite that fails.
- **Planning, framer.** The issue leaves open what the crafter's *Job* and hand-back stand for in a session's pass, and the rule stands in several documents.
- **Implementation, the session.** The change is to a few paragraphs of procedure text and the cases that hold them, a diff small enough that it does not threaten what the orchestrator still has to hold (`docs/running/the-agent-set.md` *What a spawn costs*). Its fix passes are then a session's, the case the issue names.
- **Review, through the review chain.** Whether the bound reading reads one way to a session and to a crafter is a judgment a round reads.
- **Automation, yes.** Every line of the issue's *Done when* was read before the batch. Each is delivered in this tree, and none needs a real session, a credential, an outside service or a permission.
- **Destination, open the pull request**, as under `complete`.
- **Branch.** The branch is cut from `origin/release/v0.39.1` at `4e7ad2362`, the merge of release 0.39.0 into `main`. This item is the release's first pull request, so it moves the version to 0.39.1.
