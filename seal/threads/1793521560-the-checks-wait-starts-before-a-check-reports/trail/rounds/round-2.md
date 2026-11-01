# Review round 2: 1793521560-the-checks-wait-starts-before-a-check-reports

```seal
target: a9468abd62ab14daca25d470ee9a21a891b7815d, fixes 2301c00d..a9468abd
```

This is a verifying round. Its target is the diff of round 1's fix pass, `2301c00d..a9468abd`, on branch `fix/1222-the-checks-wait-starts-before-a-check-reports`, read in a `git clone --no-local` of the branch worktree at `a9468abd` (executed: `git -C <clone> log -1 --format=%H`). The diff holds four commits. `4f13f382` rewrites the poll's reads, stop condition and report in `skills/code-review/orchestration.md:236-261`, with the pin case and `changelog.md`. `e45e7326` adds two pins. `b50d04e9` commits `trail/rounds/round-1.md` alone with its two close blocks (executed: `git show --stat b50d04e9`). `a9468abd` is the orchestrator's fold of the new reads into `frame/design.md`, `frame/plan.md` and `frame/questions.md`. `seal/parity.md` is not declared, so this round writes no `original:` line. `seal/config.md` has no `Record language` row, so the record is in English.

Carried from round 1 without re-deriving: the `VERSIONS_OF_ANOTHER_PRODUCT` row for gh 2.100.0 in `tests/behaviour/test_release_hygiene.py` and the version move in `895515f7`. Neither is in the fix diff, and the module that holds the row passed here. Re-established here: #1245's timeline, the exit of the count read on three pull requests, and the line-wrap check's skip of fenced code, which `tests/behaviour/test_docs_line_wrap.py` passing at the target shows for the new 86-column command line.

The axes walked: each close of round 1 against the diff. Then the new reads as inputs: the `event` value of a check that no GitHub Actions run made, and the read's exit for a failed, a pending and a missing check. Next, the two reads as a pair, since they are now two calls rather than one. After that, the limit the count states, and what the wait does once the poll ends. Last, every statement of the stop condition in the tree and the frame (contract rule 19), and the pins' ability to fail.

## Findings

### 1. The section's bold rule still starts the wait once the pushed commit has any check

```seal
severity: should
location: `skills/code-review/orchestration.md:228-229`, `tests/text/test_the_rules_have_one_owner.py:366-380`, `seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports/frame/design.md:36`, `seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports/frame/design.md:48`, `seal/threads/1793521560-the-checks-wait-starts-before-a-check-reports/frame/plan.md:24`
evidence: executed `bin/seal mutate skills/code-review/orchestration.md --tests "bin/test -q -p no:xdist -x tests/text/test_the_rules_have_one_owner.py -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge" --replace 'the wait only once the commit it pushed last has a check.**' 'the wait.**'`, `git grep -n -i "has a check\|lists a check\|lists its first\|first check\|has such a check"`, `git blame -L 228,229 skills/code-review/orchestration.md`
reopens: round-1#1
```

Why it matters: the close `fixed 4f13f382` holds for the poll itself and not for the section. Round 1's finding located the defect at `orchestration.md:228-250`. The fix rewrote lines 236-261 and left the paragraph's bold opening at lines 228-229 standing: "**The orchestrator waits on CI with `gh pr checks <N> --watch`, and starts the wait only once the commit it pushed last has a check.**" That is the stop condition round 1 refuted. On #1245 the pushed commit had a check, `label` of a `push` run, two minutes before any `pull_request` check was listed. In this skill the bold sentence is the rule a reader takes from the paragraph, and the detail below it says otherwise. An agent that reads the rule and skims the detail starts the wait on the `push` check, and `--watch` exits 0 over it at once. That is round 1's false pass. `git blame` puts both lines at `b2fa2eb6`, the build commit, so `4f13f382` did not touch them.

No pin catches the stale rule. With the bold sentence cut to "starts the wait.", the pin case still passed. It was the one mutant of ten that survived (executed, `## Probes`). Contract rule 19 asks the fix to correct every other sentence stating the old fact in the same commit. The `git grep` above lists two more such sentences in the frame, which the orchestrator's fold at `a9468abd` did not reach. *Scope* item 3 (`frame/design.md:36`) says the fragment's poll "ends once the pushed commit has a check". S1 (`frame/design.md:48`) has the wait run "only once the pushed commit has a check". The fragment itself already says "has such a check" (`changelog.md:3`), so only the frame lags. Plan row 1's verdict (`frame/plan.md:24`) still says the approach "covers both ways the wait starts early". Round 1 found a third way, another event's finished check on the pushed commit, and the new count is the guard against it. The frame sentences are the orchestrator's to fold. The skill and its pin are the fix pass's.

```markdown
**The orchestrator waits on CI with `gh pr checks <N> --watch`, and starts
the wait only once the commit it pushed last has a check of a `pull_request`
run.** The wait reads
```

```python
        "starts the wait only once the commit it pushed last has a check of a "
        "`pull_request` run",
```

The pin goes in the case's `said` tuple, and it must be seen red with the bold sentence put back as it stands at `a9468abd` (contract rule 15). The frame's three sentences, in place: *Scope* item 3 reads "ends once the pushed commit has a check of a `pull_request` run". S1 reads "only once the pushed commit has a check of a `pull_request` run". Plan row 1 reads "It covers the three ways the wait starts early: no check on the new head, the old head still named, and another event's finished check on the new head."

```seal
verdict: fixed 5a9d2f05
answer: The finding holds: `skills/code-review/orchestration.md:228-229` still read "has a check" as `b2fa2eb6` wrote it (read). The bold rule now reads "starts the wait only once the commit it pushed last has a check of a `pull_request` run.", the condition the poll below it gives, and the paste-ready pin joined the case's `said` tuple with the rule's closing `.**` so it holds the whole rule. With the file at `a9468abd`'s bytes the case failed at that pin (executed), and after `5a9d2f05` `seal mutate` cutting the rule to "starts the wait.**" went red, with the file restored to HEAD (executed). The fragment's `### Fixed` heading said "waits for the first check to report" and now names the check of a `pull_request` run; its body and process row already did. A search of the section for "has a check", "lists a check", "first check", "any check", "no check", "such a check" and "count" found no other sentence stating the old condition: the ones left state the measured no-check exit, the count read's exit 1 and the report, each already of the new condition (executed: `awk` over lines 203-457 with `grep`). The same words over `skills`, `agents`, `docs`, `templates`, `hooks`, `README.md` and `CONTRIBUTING.md` found only line 229 (executed); a search for wordings is a sample. The three frame sentences are the orchestrator's fold at `36dc0cc1`, which this pass did not edit.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: the pin case at `tests/text/test_the_rules_have_one_owner.py:366-380` now holds the poll's stop condition and the report it ends in, which round 1 found unpinned, and every other fact the fix pass named. The claim was that each new pin is red against `fb6735fc`'s paragraph and that eight mutants went red. Here, with `fb6735fc`'s `skills/code-review/orchestration.md` put back in the clone, the case exited 1 (executed). `seal mutate` then ran ten mutants of the paragraph at `a9468abd` (executed). Nine went red: the interval, each of the two reads, the stop condition, the count read's exit 1, the `pull_request` limit, the second `state,mergeable` read, the report and the two-minute limit. The tenth, the bold rule, survived, and that is finding 1, not this finding's close. `git status --short` was empty after each probe.

```seal
confirms: none
```
What matched: the claims the new paragraph makes about the count read, at `skills/code-review/orchestration.md:240-253`. All of these ran with gh 2.100.0. On #1245 the read printed 14 and exited 0, and its list holds 14 `pull_request` checks and `label` with event `push`. On #1209 it printed 14 and exited 0 while `release` stood at `FAILURE`. On `octocat/Hello-World#11673` it exited 1 with `no checks reported on the 'Exp4-code-review' branch`. So "With `--json`, a failed check exits 0" and "the second command exits 1 while no check at all has reported" hold. A pending check was read too. On `microsoft/vscode#345298`, with one check pending, `--json` exited 0 and the plain `gh pr checks` exited 8. So the read's only non-zero exits are the missing check and gh's own errors. An error, a network failure or an expired login, keeps the poll going until the limit. It then ends in the report that the pull request is not checked, so it fails closed. On `python/cpython#161073` four checks carry an empty `event`, as a check that no GitHub Actions run made does. The filter does not count them, which is the limit the paragraph states.

```seal
confirms: none
```
What matched: the fix pass's reason for not taking round 1's run count. Its claim was that a run is created seconds before its first check lists. `gh api .../actions/runs/<id>/jobs` for #1245's two `pull_request` runs (executed) shows each job without `needs:` created at 09:15:25Z, the second the runs were created, and started at 09:15:28Z or 09:15:29Z. A job's check is the job, so the listing may have come at 09:15:25Z rather than 09:15:28Z. No read-only probe shows which. The choice holds either way. The new read counts on the list `--watch` itself reads, so the poll ends only once `--watch` has a `pull_request` check to wait on, which a count of runs does not promise.

```seal
confirms: none
```
What matched: the two reads read as a pair, at `skills/code-review/orchestration.md:240-245` (read). They are now two calls, where the old read was one. The count read prints no SHA, so it counts on whatever head the pull request names when it runs. It runs after the SHA read. Where GitHub moves the head and the head's checks together, it reads a head at least as new as the one the first read printed, and the stop condition still binds the count to the pushed commit. Whether GitHub moves the two together is part of the open measurement in `frame/questions.md` Q1. The old single read rested on the same premise, so the split adds no case.

```seal
confirms: none
```
What matched: the rest of the fix diff against the paragraph. The fragment's `### Fixed` entry and process row (`changelog.md:3`, `changelog.md:9`) state the two reads, the stop on a `pull_request` check, the `push` run as the measured case and the report, as the paragraph does (read). The orchestrator's fold carries the new reads into `frame/design.md` *Scope* items 1 and 2, S3 and *Data & interfaces*, into `plan.md`'s failure scenario and rows 1 and 3, and into `questions.md` Q1 (read: `git diff 2301c00d..a9468abd -- seal/threads`). The three frame sentences it missed are in finding 1. The narrow set ran in one command at the target: the 13 modules `frame/plan.md` row 1 names that read the file, plus `tests/behaviour/test_release_hygiene.py`. It gave 267 passed (executed). The suite stays `unverified`, as `gaps.md:7` labels it, with the orchestrator as its answerer.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The count's limit, now that it is the frame's choice. Where a repository's pull request checks are not GitHub Actions `pull_request` runs, the poll always reaches the two-minute limit, and the report says the pull request is not checked. That covers external CI statuses, `pull_request_target`, and CI that runs `on: push` alone. The orchestrator then never reads that CI, so a failure there never starts the repair path that `frame/plan.md` row 7 keeps the wait for. Round 1 proposed this limit, and the fold wrote it into *Scope* item 1. It fails closed and is stated, so this round raises no finding. A smaller loss is open: at the limit, where the pushed commit lists checks of other events, the orchestrator could run the wait over those and say that no `pull_request` run listed. An opted-in repository with `templates/setup/hygiene.yml` (`on: pull_request`, line 28) always has one counted check | `skills/code-review/orchestration.md:250-261`, `frame/design.md:33` | the orchestrator, as a row of `frame/plan.md` *Judgments of the run*, or the framer if it reweighs |
| Whether `--watch` ends before a job that waits on another through `needs:` lists its check, which the fix pass left unmeasured. On #1245, `durations` and `release-report` (`needs: pytest`, `.github/workflows/test.yml:187` and `:250`) were created at 09:18:17Z, the second the last `pytest` job completed (executed). A check that is created only when its dependency completes leaves a window in which every listed check is finished. This sample shows no gap at one-second resolution, and one sample cannot bound it. It concerns the wait, not when it starts, which is `frame/plan.md`'s fourth failure scenario, outside the fix diff | `frame/plan.md:18` | the orchestrator, at this work's pull request, with Q1 |
| The paragraph followed on a live pull request, S1 and S2: whether the head is stale right after a push, and how long the pushed commit takes to list its first `pull_request` check. A push is a write, so this round took no measurement | `frame/questions.md:15`, `gaps.md:8` | the orchestrator, at this work's pull request after its first push |
| The full suite, the repository-wide lint and the format check at the target. This round ran 14 modules and no broad command (contract rule 2). The fix pass's 915 passed over its narrow set was not re-run as one number | `gaps.md:7` | the orchestrator, by `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `gh pr checks <n> --repo MichaelYcJo/AgenticSeal --json event --jq '[.[] \| select(.event == "pull_request")] \| length'` for 1245 and 1209, and with `--json event,name,state` | 14, exit 0, for each; #1245 lists `label` with event `push` beside 14 `pull_request` checks; #1209 lists `release` at `FAILURE` |
| The same count read on `octocat/Hello-World#11673` | exit 1; stderr `no checks reported on the 'Exp4-code-review' branch` |
| `gh pr checks 345298 --repo microsoft/vscode --json event,state`, then the same without `--json` | one check pending; `--json` exit 0, plain exit 8 |
| `gh pr checks 161073 --repo python/cpython --json event,state` | four checks with an empty `event`, 45 `pull_request` checks, one at `FAILURE` |
| `gh run list --commit 29d582caedbfc749d457e67edb88ab3d5e3ba690 --json databaseId,workflowName,event,createdAt`, then `gh api repos/MichaelYcJo/AgenticSeal/actions/runs/<id>/jobs` for the two `pull_request` runs | `hygiene` and `tests` created 09:15:25Z, `label merged on release branch` (push) created 09:12:39Z; jobs without `needs:` created 09:15:25Z, started 09:15:28Z to 09:15:29Z; `durations` and `release-report` created 09:18:17Z, the last `pytest` completed 09:18:17Z |
| In the clone, `git checkout fb6735fc -- skills/code-review/orchestration.md`, then `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` | exit 1; the file was restored to `a9468abd` and `git status --short` was empty |
| In the clone, `bin/seal mutate skills/code-review/orchestration.md` with ten `--replace` pairs, one per pinned fact and one cutting the bold rule at lines 228-229 to "starts the wait.", over the same case with `-x` | baseline passes; mutants 1 to 9 red; mutant 10, the bold rule, survived; `seal mutate` restores the file from held bytes |
| `bin/test -q` over the 13 modules `frame/plan.md` row 1 lists and `tests/behaviour/test_release_hygiene.py`, in the clone at the target | 267 passed |
