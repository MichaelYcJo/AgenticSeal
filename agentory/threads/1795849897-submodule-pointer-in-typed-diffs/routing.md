# Routing: 1795849897-submodule-pointer-in-typed-diffs

| Axis | Answer |
|---|---|
| Review | straight to the PR |
| Destination | open the pull request |
| Planning | the session |
| Implementation | the session |
| Automation | yes |
| Branch | fix/1648-submodule-pointer-in-typed-diffs |

Answered 2026-11-28 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 of the routing question with `agentic` on 2026-11-28, for a request naming #1648, #1593, #1631, #1583 and #1671, and chose to cut the three releases side by side. Each row below is judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, the session:** the issue fixes the change at its coordinates, the two git reads an agent types by hand in `agents/proofer.md` and `agents/inspector.md`.
- **Implementation, the session:** the diff is two commands in two agent definitions and the cases that pin them, small enough that the orchestrator holds it.
- **Review, straight to the PR:** the change adds one flag that `lib/gitcmd.py#argv` and `agents/inspector.md` step 1 already carry. The inspector's reading of the diff against the issue is enough.
- **Automation, yes:** no question the orchestrator foresees needs a person.
- **Destination, open the pull request:** nothing in the issue or the batch asks for the branch back.

The base is the release branch for the patch, which names its version. This work item is the first of the release's two to merge, and carries the version move.
