# Routing: 1794383422-the-census-reads-root-names-from-a-case-root

| Axis | Answer |
|---|---|
| Review | straight to the PR |
| Destination | open the pull request |
| Implementation | the session |
| Automation | yes |
| Branch | fix/1498-the-census-reads-root-names-from-a-case-root |

Answered 2026-11-11 by the orchestrator, before the first edit.

## Why this way

The owner answered question 1 with `agentic` on 2026-11-11, for the work items of 0.37.4 (#1481–#1489, #1498), and this route is the orchestrator's choice, judged against `skills/implement/orchestration.md` *Under agentic*.

- **Planning, no row.** The issue fixes the change at its coordinate: `tests/censuses.py#_root_names` reads `lib/optin.py` from the repository the census module stands in instead of from `ROOT`.
- **Implementation, the session.** The change is one function of a test helper; a spawn would cost more than the diff.
- **Review, straight to the PR.** The change touches no gate, hook or document an agent reads, and a defect in it shows at once as a failing case of the suite; the sealer's reading of the diff against the issue is enough.
- **Automation, yes.** Nothing in the issue waits on a person.
- **Destination, open the pull request**, as under `complete`. This work item carries the version move to 0.37.4, because no plan orders it after another and it is the first to merge.
