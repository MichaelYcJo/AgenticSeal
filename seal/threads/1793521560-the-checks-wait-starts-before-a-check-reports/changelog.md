### Fixed

- **The orchestrator's wait on a pull request's checks now waits for the first check to report (#1222).** `skills/code-review/orchestration.md` told the orchestrator to wait on CI with `gh pr checks <N> --watch` right after a push. Run before any check has reported on the pushed commit, that command does not wait. With gh 2.100.0 it prints `no checks reported on the '<branch>' branch` and exits 1, which is also the exit of a failed check. The orchestrator now polls `gh pr view <N> --json headRefOid,statusCheckRollup` every ten seconds and runs the wait once the commit it pushed last lists a check. The SHA in that read keeps the wait off the finished checks of the commit before the push. A poll that finds no check within two minutes is not a pass: under `OPEN` and `MERGEABLE`, the orchestrator's report says that no check reported on that commit and names its SHA, and the pull request is not treated as checked.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-01 | The orchestrator starts its wait on a pull request's checks only once the commit it pushed last lists a check, read by polling `gh pr view <N> --json headRefOid,statusCheckRollup` every ten seconds; after two minutes with no check, its report says that none reported on that commit, names the SHA, and treats the pull request as not checked | `gh pr checks <N> --watch` run before a check reports exits 1 at once with `no checks reported`, the same exit a failed check gives, so the wait never waited | https://github.com/MichaelYcJo/AgenticSeal/issues/1222 |
