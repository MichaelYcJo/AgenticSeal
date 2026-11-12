# Implementation Plan: 1794465691-the-orchestrator-polls-ci-by-hand

## Technical context

The tree as read at `b7b75666f`, the routing commit on `79f815a74`.

`seal` is `skills/implement/scripts/seal.py`. Its `TOOLS` table maps each subcommand to a script under the plugin and a help line, and `main` hands every argument after the name to that script on the same interpreter (`seal.py#tool_command`, `seal.py#hand_over`). Each script keeps its own parser and help. `skills/code-review/scripts/pr_body.py` is the sibling the new script sits beside, and `tests/skills/test_pr_body.py` is the shape of its test file. Scripts here load `lib/` modules through `lib/sibling.py#load` and refuse at exit 2 where one is absent (`seal.py:177-188`). A git command a script starts is built by `lib/gitcmd.py#argv` (`docs/running/what-a-script-gates.md` *Which gate a script holds*). Scripts that call `gh` do it through one module function that the tests replace (`.github/scripts/release_seal.py#gh`, design G14).

The constraint that shapes the reads is gh's own: `--json` never reports a check's result in its exit, `--watch` passes a cancelled check, and neither waits for a job created after its dependencies finish (design G7, G10). So the script reads gh's JSON and decides by itself, and never runs `--watch`.

**What breaks in six months.** A gh release renames a JSON field or a bucket. The script's read of `bucket` then finds no value it knows, and S9 holds that such a value ends at exit 2 naming the check, never at a pass. A repository on GitHub Enterprise Server without the check-run event field lists every check with an empty event, so the start never comes and the command exits 3 naming the commit (`frame/questions.md` Q2). A workflow whose jobs all wait on a manual approval stays `pending` with no limit, as it does under `--watch` today.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. The script polls `gh pr view --json state,mergeable,headRefOid,statusCheckRollup`, then `gh pr checks --json name,workflow,event,bucket` once the rollup is not empty, and confirms a read with nothing pending against `gh run list --commit <HEAD> --event pull_request` before it decides by gh's buckets | A gh release that renames a field ends at exit 2 or 3, both visible. The three reads are separate requests, so a push by another party between them could pair one commit's head with another's checks; only the orchestrator pushes to a work item's branch. | Chosen. Each fact comes from gh's parser: the state, the head, the event and the bucket. It closes the three early starts #1222 found (design G6) and the two false passes this frame found (G7, G10). |
| 2. The script polls as #1222's paragraph does, then hands over to `gh pr checks <N> --watch` and returns its exit | `--watch` exits 0 on a cancelled check, and it ends in the gap before a dependent job's check exists (G7, G10). Its exit 1 does not say which check failed, and its screen output is an alternate screen buffer the orchestrator cannot read. | Rejected. It keeps both false passes. |
| 3. One `gh api graphql` query that returns the state, the head and each check with its event in one response | The head and the checks would be read atomically. But the script would carry its own copy of gh's state-to-bucket table and its rule for repeated checks (G7), which a gh release changes in one place and this script in another. | Rejected. gh's parser is the one reader of a check's state (`skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source"). |
| 4. Read "no check yet" from `gh pr checks` exiting 1 with `no checks reported` on stderr | The script would gate on gh's wording. A `gh` that fails for another reason, such as authentication or the network, also exits 1, and would read as "no check yet" for two minutes and then as exit 3, which hides the real error. | Rejected. The empty rollup is read from `gh pr view`'s exit 0 and a count (design *Data & interfaces*, read 2). |
| 5. Exit at the first failed check, as `--fail-fast` does | The orchestrator would start the repair sooner. A second check that fails independently would show only after the next push, and every push after the rounds owes a verifying round, the broad run and the sealer again (`skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the stated limit's paragraph). | Rejected. The command waits until nothing is pending and names every failed check at once. |
| 6. Keep the before-push read as `gh pr view <N> --json state` typed by hand, or drop it | Kept by hand, the paragraph states a second command and the meaning of its values, against the issue's *Done when*. Dropped, a push after the owner merged goes to a branch in no pull request, which #1200 added the read to stop (the pin's docstring, `tests/text/test_the_rules_have_one_owner.py:319-333`). | Rejected for `--once`, which reads `state` with the same exit codes as the wait. |
| 7. A `--sha` option for the commit to wait on | No caller pushes anything but HEAD, and a stale HEAD ends at exit 3 naming both SHAs (S4). | Rejected. An option nobody passes is a surface to test and document. |
| 8. A limit on the whole wait | A limit shorter than CI turns a slow passing run into a failure the orchestrator must read, and the measured runs reach 547 seconds here and 15.3 minutes on #1516's count (design G11). | Rejected. The limit covers the start alone, as #1222's paragraph did, and the jobs' own timeouts bound the rest. |
| 9. Replace the structure: keep the procedure in the skill as prose the orchestrator runs by hand, and only correct `--watch`'s two false passes there | The paragraph grows by the runs read and the cancelled bucket, and every orchestrating session reads and runs a longer loop after every push. The premise that kept it in 0.27.2, that a patch builds no feat and that the poll is two calls the orchestrator already makes (G6), no longer holds: 0.38.0 is a minor, and the loop is now three reads, a limit and seven outcomes. | Rejected. Whether the orchestrator should wait on CI at all was settled by #1222's row 7 and is not argued again. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2 and 3 | `bin/test -q tests/skills/test_pr_wait.py tests/skills/test_seal.py tests/behaviour/test_a_reference_root_is_read_and_never_taken.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`; each case of S1 to S9 seen red against the guard it names (contract rule 15); `seal mutate` on the unit that maps a read to an exit code | |
| 2 | `frame/design.md` *Scope* items 4, 5 and 6 | `bin/test -q tests/text/test_the_rules_have_one_owner.py`, the pin seen red with each new string deleted from the paragraph; the proofer reads the paragraph against design G3 and S10 for an act that was lost | |

## Overlap with the release

The spawn names three other open work items, and none has a committed frame yet, so each row reads the item's issue and its branch, which holds only its `routing.md` at the time of reading (executed: `git log` and `git diff --stat` of each branch against `79f815a74`). This item merges last, after all three, as the description of milestone `release: 0.38.0` orders (executed: `gh api repos/MichaelYcJo/AgenticSeal/milestones`): #1516 first, #1510 and #1496 beside it, #1494 last, because this item changes the procedure the orchestrator follows after each push. Only #1516 meets this work.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1516, `chore/1516-feature-prs-wait-on-the-macos-runner` | No file. #1516 changes `.github/workflows/test.yml`'s matrix, which sets the checks a pull request into `release/*` lists, and `seal pr-wait` reads those checks. It reads them by event and bucket, never by name, so neither diff edits a line the other reads. #1516 also carries the version move. | #1516 | It carries the move, and the first pull request into the branch carries it (`skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in*). Merged first, this work's own pull request runs the matrix #1516 leaves, so S11's first real run reads the checks every later feature pull request lists. |

#1510 changes `skills/verify/scripts/session_cost.py`'s attribution of segments to work items (`names_key`, `report_work_item`), and #1496 changes `.github/scripts/publish_release_note.py` and `.github/scripts/release_seal.py`. Neither changes a file, a rule or a check this work reads or adds to, and this work changes nothing they read, so neither meets it. The CI wait's minutes moving to another row of `seal cost`'s table (design G18) is a reading of #1510's command, not a line #1510 changes.

## Operational impact

- No new dependency: the command calls `gh`, which the orchestrator's procedure already requires, and `git`.
- No environment variable and no configuration key.
- A new subcommand, `seal pr-wait`, and a changed step in the orchestrator's procedure after each push. An orchestrating session that loaded the skill before the upgrade keeps the old procedure until it reloads it.
- `seal cost`'s table counts the CI wait outside the `git` row from this release on (design G18). A reading compared across 0.38.0 moves for that reason alone.
- This pull request does not move the version; #1516 carries the move.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
