# Routing: 1795339519-the-thread-layout-has-one-spelling

| Axis | Answer |
|---|---|
| Review | through the review chain |
| Destination | open the pull request |
| Implementation | the session |
| Automation | yes |
| Branch | refactor/1567-the-thread-layout-has-one-spelling |

Answered 2026-11-22 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-22, for #1567. This route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*. No release branch was open, so the orchestrator cut `release/v0.38.5` from `main` at `0eca6e77` and opened the milestone `release: 0.38.5`: the work is a `refactor:`, which fits a patch (`docs/releasing/branch-and-release.md` *The version is named at the cut*).

- **A work item, not `direct`.** The change touches three check scripts, `skills/verify/scripts/broad_gate.py`, `skills/code-review/scripts/chain_check.py` and `skills/verify/scripts/seal_stamp.py`. A defect in any of them stops every session that runs the gate.
- **Planning, no row.** The work alters no verdict, output or instruction, so it stands on the second rung of *Orchestrator: when a work item is required*, where a scope confirmation in `gaps.md` replaces the plan. The issue states each coordinate and its *Done when*, so it leaves no design choice open.
- **Implementation, the session.** The orchestrator has already read every coordinate the issue names. The issue named seven scripts and the cases that name the copies; the diff came to nine scripts, no `lib/` module and those cases, which is not large enough to threaten what the orchestrator still has to hold.
- **Review, through the review chain.** The scripts are gates. A reader independent of the build is worth its rounds there, because a refactor that changes a fallback or a path would show only as a gate that misreads a thread in a later run.
- **Automation, yes.** The work reaches nothing outside the repository, and every question has a default the issue or the tree gives.
- **Destination, open the pull request**, as under `complete`.
- **Version.** This work item is the first pull request into `release/v0.38.5`, so it carries the move of `.claude-plugin/plugin.json` to 0.38.5, made by the session in the commit that adds the changelog fragment (`skills/implement/orchestration.md` *How the work is routed*).
