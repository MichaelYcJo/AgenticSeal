# Routing: 1795736973-the-preflight-passes-where-a-round-is-owed

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | fix/1620-the-preflight-passes-where-a-round-is-owed |

Answered 2026-11-27 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-27 for #1620, #1624, #1628 and #1629, the four issues of `release: 0.39.2`. This route is the orchestrator's choice for #1620, judged against `skills/implement/orchestration.md` *Under agentic*.

- **A work item, not `direct`.** The preflight's verdict comes from `skills/verify/scripts/broad_gate.py`, which reads only `skills/code-review/scripts/chain_check.py`'s exit code. Before a pull request exists, that check judges no pull request and prints each problem as a notice and exits 0 (`chain_check.py` `main`, where `strict` is false while the state is unknown and no event payload is present; read). So the preflight passes over a records-arm problem, and so does the broad gate's chain arm. A change there decides what the gate refuses before a pull request, which every user's run passes through.
- **Planning, framer.** The issue's *Done when* leaves a decision between two outcomes: the preflight refuses and names the line, or the gate document says the preflight does not read it and why. The cause above reaches the broad gate as well, which the issue does not name, so the scope is the framer's to judge.
- **Implementation, crafter.** The change is to code with cases, and a crafter's build is mutation-tested by its rules (`agents/crafter.md` *Rules*), which no rule asks of a session's build (#1629).
- **Review, through the review chain.** A gate that refuses where it passed before is behaviour a round reads.
- **Automation, yes.** The issue's *Done when* asks for a refusal or a document sentence and a case. Each is delivered in this tree, and none needs a real session, a credential, an outside service or a permission.
- **Destination, open the pull request**, as under `complete`.
- **Branch.** The branch is cut from `origin/release/v0.39.2` at `e65830869`, the merge of release 0.39.1 into `main`. This item is the release's first pull request, so it moves the version to 0.39.2.
