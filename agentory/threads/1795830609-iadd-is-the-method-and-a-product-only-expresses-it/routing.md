# Routing: 1795830609-iadd-is-the-method-and-a-product-only-expresses-it

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Planning | framer |
| Implementation | crafter |
| Automation | yes |
| Branch | feat/1658-the-plugin-stays-agentic |

Answered 2026-11-28 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic`. The rows are chosen against `skills/implement/orchestration.md` *Under agentic*. The batch held no other question: #1658's *Done when* needs no credential, no outside service and no real session, and the names it decides were settled with the owner in conversation on 2026-11-28 before the issue was written.

- **Planning, `framer`.** #1658 names the three layers but leaves the plan to sort every identifier #1656 spelt `iadd` into one of them: a product's goes to `agentic`, a place's to `agentory`, and the method's stays `IADD`. That sorting is a judgment across the agents, skills, scripts, tests and documents, and it decides the build.
- **Implementation, `crafter`.** The diff reaches the plugin's identity, its command, its environment variables, its records root and the code that finds the root. #1656 was the same size, and a diff that size would crowd out what the orchestrator still has to hold.
- **Review, through the review chain.** The rename touches the gates that read the root by name, `chain_check.py#root_name` and `lib/optin.py#home_at` among them. A defect there stops every session that runs them, so a reader independent of the build is worth its rounds.
- **Automation, `yes`.** The owner asked the run to go to the pull request ("머지는 이미했으니까 2번부터하면될듯", after the plan named the second pull request as step 2). Every question the orchestrator foresees has a default the framer can give from the tree or from #1658. The work item commits in this repository alone: moving CodeChallenge comes after the release.
- **Destination, `open the pull request`.** Nothing in the conversation asks for the branch back.
- **Base and version.** The work item is built on `release/v0.40.0` at 801465cb, where #1656 merged. The version is already 0.40.0 there, so this work item writes its changelog fragment and moves no version.
- **The parties' type.** The installed plugin is `agentic` 0.39.x, which reads a `seal/` root, and this tree holds `iadd/`. As in #1656 after its phase 7, the framer, the crafter, the proofer and the inspector are spawned as `general-purpose` agents bound by this tree's `agents/<name>.md`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md`, and every subcommand runs from this tree's `bin/`.
