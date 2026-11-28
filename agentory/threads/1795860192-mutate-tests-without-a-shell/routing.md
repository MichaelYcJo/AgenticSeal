# Routing: 1795860192-mutate-tests-without-a-shell

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | the session |
| Implementation | the session |
| Automation | yes |
| Branch | fix/1677-mutate-tests-without-a-shell |

Answered 2026-11-28 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 of the routing question with `agentic` on 2026-11-28, for the request that names #1676. In the same request the owner asked that #1677 be taken up with it. Each row below is judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, the session:** the issue names the change's coordinates and leaves one choice open, between refusing a shell operator and running `--tests` through `sh -c`. The tree answers it (`frame/design.md` *Grounding*).
- **Implementation, the session:** the diff is one reader in `skills/verify/scripts/mutation_check.py`, its cases, and the text of `skills/verify/agentic-mutate.md` that states the refusal.
- **Review, through the review chain:** the change adds a refusal to a command whose verdict other parties stand on, and a defect in it shows as a run that measures nothing, not as a failing suite.
- **Automation, yes:** no question the orchestrator foresees needs a person.
- **Destination, open the pull request:** nothing in the issue or the request asks for the branch back.

The base is the release branch for the patch. #1648, the release's other work item that carries the version move, changes neither of this item's files.
