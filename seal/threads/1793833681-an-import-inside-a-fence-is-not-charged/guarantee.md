# Guarantee: 1793833681-an-import-inside-a-fence-is-not-charged

The audit stopped at `agents/sealer.md` step 2: the pull request body's
check exited 1, so no claim was re-run and no party was compared.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run passed at a commit that HEAD follows only with paths under the work item's directory | `trail/gate.md`, `run: 8b87cb7f against 32bf3e98` | `git log --no-merges --name-only 8b87cb7f..HEAD ^6adb548e` | holds (executed): 8b87cb7f resolves and is an ancestor of HEAD; the one commit after it, 8e3e73ee, touches only `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/trail/gate.md` |
| The part of the pull request body below `## From the records` is the records' own text | the spawn prompt: `seal pr-body` wrote that part (exit 0) | `seal pr-body seal/threads/1793833681-an-import-inside-a-fence-is-not-charged --body pr-body.md --check` | does not hold (executed): exit 1, `refused: pr-body.md:182: reads ``, which the records do not give`. Lines 182 and 183, a blank line and the Claude Code attribution line after the fold's closing `</details>`, stand below the heading and are not the records'. The same check on a copy of the body cut after line 181 exits 0 (executed), so those two lines are the only cause |

The crafter's `executed` and `seen red` claims and the `## Removes` rows
were not sampled (unverified; answered by the next sealer run, once the
body passes its check).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the orchestrator's part of the pull request body | not read: step 2 stops before the parties are read (unverified; the next sealer run reads it) | not compared | not compared |
| the design, the build, the last round, the changelog | not read for the same reason (unverified; the next sealer run reads them) | not compared | not compared |

```seal
target: 8e3e73ee against 6adb548e
Verdict: withheld reason: refused: pr-body.md:182: reads ``, which the records do not give
```
