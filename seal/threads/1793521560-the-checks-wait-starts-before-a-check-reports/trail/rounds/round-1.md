# Review round 1: 1793521560-the-checks-wait-starts-before-a-check-reports

```seal
target: fb6735fcf5fce967827c28a013939c4de8a86f0d against release/v0.27.2
```

The target is the branch `fix/1222-the-checks-wait-starts-before-a-check-reports` at `fb6735fc`, read against its base `release/v0.27.2` at `813665f0`, which is also the merge base (executed: `git merge-base HEAD release/v0.27.2`). No earlier round exists, so no fact is carried; every fact below was established this round. `seal/parity.md` is not declared, so this round writes no `original:` line. `seal/config.md` has no `Record language` row, so the record is in English.

The axes walked: the frame's *Scope* items 1 to 3 and *Removes* against the diff (stage 1). Then the poll's stop condition as an input boundary: which checks `statusCheckRollup` holds on the pushed commit, and when. Next, concurrency between the push, the pull request's creation and GitHub's listing of checks. After that, the error paths of `gh pr checks` (exit 1 for no check and for a failed check). Last, the pins' ability to fail, the version move, the exemption row, and the fragment's shape.

## Findings

### 1. A check of another event on the pushed commit ends the poll, and `--watch` then exits 0 before the pull request's own checks are listed

```seal
severity: should
location: `skills/code-review/orchestration.md:228-250`, `seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports/changelog.md:3`, `tests/text/test_the_rules_have_one_owner.py:367`, `seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports/frame/design.md:56`
evidence: executed `gh pr view 1245 --json createdAt,headRefOid`, `gh pr view 1245 --json statusCheckRollup`, `gh run list --commit 29d582caedbfc749d457e67edb88ab3d5e3ba690 --json workflowName,event,createdAt`, `gh pr checks 1245 --watch`
```

Why it matters: the poll ends once "the SHA it prints is the commit it pushed last and the count is above 0" (`skills/code-review/orchestration.md:243-244`). `statusCheckRollup` lists every check on that commit, of every event, and not only the pull request's own. The paragraph's guard covers one kind of stale check, the finished checks of the commit before the push (`orchestration.md:244-245`). It does not cover finished checks of another event on the pushed commit itself. Where such a check stands, the poll ends at its first read, `gh pr checks <N> --watch` finds nothing pending, and it exits 0 at once. The pull request's own `pull_request` checks are listed some seconds later. The orchestrator then reads a pass on a pull request nothing has checked. That is the false pass the paragraph's SHA guard exists to stop, reached another way.

The frame's own data holds the instance. *Grounding* row 12 (`frame/design.md:12`) names five pull requests whose first check "started before the pull request opened, because their head already had runs". This round read what those runs were. #1245 opened at 09:15:21Z on head `29d582ca`, and the rollup's only check before that was `label` from `label merged on release branch`, started 09:12:42Z, finished 09:12:52Z, `SUCCESS` (executed). `gh run list --commit` lists that run with event `push`, and lists `tests` and `hygiene` with event `pull_request`, created at 09:15:25Z, four seconds after the pull request opened (executed). `.github/workflows/label-merged-on-release-branch.yml:20-22` runs it on every push to `release/*` (read). #1212, #1207, #1194 and #1188 show the same `label` check finished before they opened (executed). So a poll run one second after `gh pr create` on #1245 would have printed `["29d582ca...",1]` and ended. `gh pr checks 1245 --watch` over finished checks alone exits 0 in under a second (executed: 0.98 s, exit 0). The paragraph's reading at that moment is inferred from these timestamps, since no pull request could be opened read-only to watch it happen.

In this repository the instance is the release pull request, which `docs/release-checklist.md:104-110` has the orchestrator open (read). Its head is a `release/*` commit that already holds `label`, and `813665f0`, the head of `release/v0.27.2` today, holds 17 finished checks from `main`'s and the release branch's `push` runs (executed: `gh api repos/MichaelYcJo/AgenticSeal/commits/813665f0.../check-runs`). The section is also read in every user's repository (`frame/plan.md:11`), where a workflow `on: push` for every branch is common. There the pushed commit carries that workflow's checks before the pull request opens, and a fast one has finished by the poll's first read. A `gh workflow run --ref <branch>` at the head commit, which the section's platform paragraph asks for (`orchestration.md:266-270`), leaves the same kind of check.

The frame states the premise this rests on: "a count above 0 is the state in which `--watch` waits" (`frame/design.md:56`). The probe on #1245 refutes it. `--watch` waits while a listed check is pending, and a count of finished checks above 0 is a state in which it does not wait. Plan row 3 (`frame/plan.md:26`) rejects a count without the SHA because the old commit's finished checks end the poll. The same reasoning covers a finished check of another event on the new commit, and the chosen row 1 does not answer it. The fragment's entry (`changelog.md:3`) repeats the stop condition and the claim that the SHA keeps the wait off finished checks, so it changes with the paragraph. The pin at `tests/text/test_the_rules_have_one_owner.py:367` holds the read's spelling and moves with it.

The fix replaces the read and the stop condition at `orchestration.md:240-245`. The SHA still comes from `gh pr view`, and the count is of the pull request's own runs. The precondition is that the pull request's checks come from GitHub Actions workflows on `pull_request`. Such a run's head SHA is the pull request's head commit, as the `gh run list --commit` probe above shows. A repository whose pull request checks come from another CI service, or from `pull_request_target`, lists none here. Its poll then reaches the two-minute report, which says no check reported, a visible miss and not a pass. The paragraph should state that limit beside the command.

```sh
gh pr view <N> --json headRefOid --jq .headRefOid
gh run list --commit <the SHA it printed> --event pull_request --json databaseId --jq length
```

```markdown
and stops once the SHA the first prints is the commit it pushed last and the
second prints a count above 0. It then runs the wait. The SHA keeps the wait
off the finished checks of the commit before the push. The second count keeps
it off finished checks of another event on the pushed commit itself: a `push`
or `workflow_dispatch` run on that commit is listed among the pull request's
checks too, often finished before the pull request opens, and `--watch` over
finished checks alone exits 0 at once. The count reads GitHub Actions runs on
`pull_request` only; where the pull request's checks come from elsewhere, the
poll reaches the limit below and the report says so.
```

### 2. The pin case holds the poll's read but not its stop condition or the report it ends in

```seal
severity: should
location: `tests/text/test_the_rules_have_one_owner.py:360-378`, `skills/code-review/orchestration.md:243-250`
evidence: executed `bin/test -q tests/text/test_the_rules_have_one_owner.py -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge`
```

Why it matters: phase 1 claims its four pins each name "one fact the orchestrator acts on" (`trail/phases/phase-1.md:13`). They do. But the fact the paragraph turns on is the stop condition, and no pin holds it: the SHA it prints is the commit pushed last, and the count is above 0. Nor does a pin hold what the owner reads when the limit passes, the report naming the SHA and the pull request not treated as checked. In the clone, this round deleted the stop condition's SHA clause, the SHA's reason and the report sentence (`orchestration.md:243-250`) and left the fenced command. The case still passed, exit 0 (executed). The pin `--json headRefOid,statusCheckRollup` at line 367 holds the read's spelling, so a later edit can drop the comparison that makes the read worth taking. The pull request then goes back to the false pass after a push that plan row 3 rejects, and nothing goes red. The report line is text a person reads and acts on, so contract rule 14 asks for its pin in the same commit. `docs/what-a-script-gates.md` *The checks* lets a prose case pin a fact a reader acts on, which both of these are.

The fix adds two facts to the case's `said` tuple, in the spelling the paragraph gives them once finding 1's fix lands. Below is the spelling at `fb6735fc`:

```python
        "the SHA it prints is the commit it pushed last",
        "no check reported on that commit and names the SHA",
```

Each is seen red with its sentence deleted before it is committed (contract rule 15).

## Confirmations

```seal
confirms: none
```
What matched: *Scope* item 1 (`frame/design.md:29-34`), each of its five facts, at `skills/code-review/orchestration.md:228-250` (read). The command and its reason for reading every workflow's checks stand at lines 228-231. The message, the exit 1 and gh 2.100.0 stand at lines 232-234. The failed check's same exit stands at lines 234-236. The ten-second poll in a fenced block, its stop on the SHA and the count, and the wait after it stand at lines 236-245. The two-minute limit, the second `state,mergeable` read and the report under `OPEN` and `MERGEABLE` stand at lines 245-250. *Removes* holds: the old sentence is gone and its words open the new paragraph (executed: `git diff 813665f0..HEAD -- skills/code-review/orchestration.md`). The frame's no-check measurement was re-run here: `gh pr checks 11673 --repo octocat/Hello-World --watch` exited 1 with `no checks reported on the 'Exp4-code-review' branch`, and the `gh pr view` read printed the head SHA with a count of 0 (executed).

```seal
confirms: none
```
What matched: phase 1's claim that the four new assertions go red against the base. With `813665f0`'s `skills/code-review/orchestration.md` restored in the clone, `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` exited 1 at the first new fact, `` `no checks reported on the '<branch>' branch` `` (executed). At the target, that module, `tests/behaviour/test_release_hygiene.py` and `tests/behaviour/test_docs_line_wrap.py` ran in one command: 115 passed, exit 0 (executed). The poll's line is 102 columns wide and stands in the file's only fenced block. The base held none (executed: `git show 813665f0:skills/code-review/orchestration.md` counted no fence line). The line-wrap check skips fenced code, so the width claim holds.

```seal
confirms: none
```
What matched: phase 1's one departure. It is claimed as a row in `VERSIONS_OF_ANOTHER_PRODUCT` of the same class as the git, bash and Claude Code rows. `tests/behaviour/test_release_hygiene.py:176-183` keys the row on `("skills/code-review/orchestration.md", "2.100.0")`, and the lookup at lines 273-276 reads the pair, so the number passes in that file alone (read). The rows at lines 128-175 are each a tool build a measurement names (read). The paragraph names gh 2.100.0 as *Scope* item 1 asks. The row is the route the check's own refusal names (`tests/behaviour/test_release_hygiene.py:298`, read), and the module passes (executed, above).

```seal
confirms: none
```
What matched: phase 2's version move and fragment. `.claude-plugin/plugin.json:4` reads `"version": "0.27.2"`, and `git show --stat 895515f7` lists that file and the work item's `changelog.md`, two files and nothing else (executed). `git grep '0\.27\.[12]'` outside `seal/threads/` finds `plugin.json:4` and the docstring at `tests/text/test_the_rules_have_one_owner.py:691`, which names 0.27.1's settle (executed). `docs/branch-and-release.md:31-32` moves the version in the first pull request into `release/vX.Y.Z` (read). The fragment ends with `### Process changes` and one row in the four columns `templates/records/process.md` gives (read), as `docs/the-record-layout.md` *A change writes fragments, never a shared file* asks for a diff that changes a `skills/*/orchestration.md` file. Its `### Fixed` entry states the paragraph's facts, and finding 1 is where it changes.

```seal
confirms: none
```
What matched: the claim in phase 1 and the frame that the section is the one place the tree states the wait. Two searches ran here. `git grep` for wait on CI or checks, CI green and until CI, over `skills`, `agents`, `docs`, `templates`, `hooks`, `README.md` and `CONTRIBUTING.md`, finds only `orchestration.md:216` and `:228`. `git grep` for `sleep`, `run_in_background` and every-N-seconds wordings finds only `orchestration.md:236` (both executed). Like the crafter's, these are searches for wordings, so they are a sample: a sentence describing the wait in other words would not show.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The paragraph followed on a live pull request: whether the head is stale right after a push, and how long a pushed commit takes to list its first check (`frame/questions.md` Q1, S1 and S2). A push is a write, so this round took no measurement | `frame/questions.md:15`, `gaps.md:8` | the orchestrator, at this work's pull request after its first push |
| The full suite, the repository-wide lint and the format check at the target. This round ran three modules and no broad command (contract rule 2); `gaps.md` labels the suite `unverified` with the orchestrator as its answerer, and that label is honest | `gaps.md:7` | the orchestrator, by `seal gate` after the rounds settle |
| Phase 1's one shell substitution in `trail/phases/phase-1.md` in place of the `Edit` tool (contract rule 9). The spawn prompt relays it from the crafter's hand-back, and `phase-1.md` does not name it. The file reads whole, with no visible broken span, but this round cannot tell what the substitution was meant to change or whether it matched | `seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports/trail/phases/phase-1.md` | the orchestrator, which holds the hand-back |

## Probes

| Command | Result |
|---|---|
| `gh pr view <n> --json createdAt,headRefOid` and `gh pr view <n> --json statusCheckRollup` for 1245, 1212, 1207, 1194 and 1188 | each head's `label` check of `label merged on release branch` started and finished minutes before the pull request opened; every `tests` and `hygiene` check started 6 to 8 seconds after it opened |
| `gh pr view <n> --json number,baseRefName,headRefName,title` for the same five and 1214 | the five are release pull requests, `release/vX.Y.Z` into `main`; 1214 is a settle into `release/v0.27.1` |
| `gh run list --commit 29d582caedbfc749d457e67edb88ab3d5e3ba690 --json workflowName,event,headSha,createdAt` | `hygiene` and `tests` with event `pull_request`, created 09:15:25Z; `label merged on release branch` with event `push`, created 09:12:39Z |
| `gh pr checks 1245 --watch`, timed | exit 0 in 0.98 s over 15 finished checks |
| `gh api repos/MichaelYcJo/AgenticSeal/commits/813665f0.../check-runs` | 17 check runs, all `completed` |
| `gh pr checks 11673 --repo octocat/Hello-World --watch`; the same without `--watch`; `gh pr view 11673 --repo octocat/Hello-World --json headRefOid,statusCheckRollup --jq '[.headRefOid, (.statusCheckRollup \| length)]'` | exit 1; stderr `no checks reported on the 'Exp4-code-review' branch`; `["6fd23f196d536163971e4a466d09c0439ec009f4",0]` |
| In the clone, the stop condition, the SHA's reason and the report sentence deleted from `skills/code-review/orchestration.md:243-250` with the `Edit` tool, then `bin/test -q tests/text/test_the_rules_have_one_owner.py -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` | 1 passed, exit 0: nothing in the case pins the stop condition or the report; the file was restored with `git checkout` and `git status -s` was empty |
| In the clone, `git checkout 813665f0 -- skills/code-review/orchestration.md`, then the same case with `-p no:xdist` | exit 1 at `` `no checks reported on the '<branch>' branch` ``; the file was restored to `fb6735fc` and `git status -s` was empty |
| `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_docs_line_wrap.py` at the target in the clone | 115 passed, exit 0 |
| `sleep 2` and an `until` loop with `sleep 2` in this agent's shell | both ran, exit 0: a ten-second poll can be run as written |
