# Review round 3: 1793521560-the-checks-wait-starts-before-a-check-reports

```seal
target: 03bad9d40318dfcd0bb0ece750d854111797398b, fixes f87b2957..03bad9d4
```

This is a verifying round. Its target is the diff of round 2's fix pass, `f87b2957..03bad9d4`, on branch `fix/1222-the-checks-wait-starts-before-a-check-reports`. It was read in a `git clone --no-local` of the branch worktree at `03bad9d4` (executed: `git -C <clone> log -1 --format=%H`). The diff holds four commits (executed: `git show --stat` of each). `36dc0cc1` is the orchestrator's fold of three frame sentences into `frame/design.md` and `frame/plan.md`. `5a9d2f05` rewrites the bold rule at `skills/code-review/orchestration.md:228-230`, adds its pin to the case, and edits the `### Fixed` heading of `changelog.md`. `30606440` commits round 2's record with its close block alone. `03bad9d4` adds one row to `frame/plan.md` *Judgments of the run*. `seal/parity.md` is not declared, so this round writes no `original:` line. `seal/config.md` has no `Record language` row, so the record is in English.

Carried from round 2 without re-deriving: the count read's exits and the `event` values measured on #1245, #1209, `octocat/Hello-World#11673`, `microsoft/vscode#345298` and `python/cpython#161073`, and #1245's run and job timeline. No line the fix diff changed restates those facts. The `VERSIONS_OF_ANOTHER_PRODUCT` row for gh 2.100.0 is carried from round 1, and its module passed here. Re-established here: the pin's red against the old rule, the rule's mutants, and the list of every statement of the wait's start condition.

The axes walked: the close of round 2's finding against the rewritten rule and its pin. Next, every statement of the start condition in the tree and the frame (contract rules 12 and 19). Then the new pin against the other entries of its case, the fragment's heading against the paragraph, and the judgment row's grounds against the paragraph and round 2's *Not judged* row 1.

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the bold rule at `skills/code-review/orchestration.md:228-230` now reads "starts the wait only once the commit it pushed last has a check of a `pull_request` run.", the condition the poll at lines 238-246 stops on (read). `git blame -L 228,230` puts lines 229 and 230 at `5a9d2f05` (executed). The fix pass claimed the pin was red against `a9468abd`'s file and that a mutant cutting the rule went red. Here, with `a9468abd`'s `skills/code-review/orchestration.md` put back in the clone, the case exited 1 on the new pin, "the owner section no longer says 'starts the wait only once the commit it pushed last has a check of a `pull_request` run.**'" (executed). `seal mutate` then ran three mutants of the rule at the target, and all three went red (executed, `## Probes`). The first cuts "of a `pull_request` run" to "has a check.". The second leaves "has a check run.", a spelling that reads as a GitHub check run of any event. The third cuts the rule to "starts the wait.", the mutant that survived in round 2. The pin holds the rule's closing `.**`, so a sentence added after the condition inside the bold also fails it. The file was restored and `git status --short` was empty after each probe.

The fix pass also claimed that a search found no other sentence stating the old condition, and called that search a sample. This round listed the class by two methods. First, it took the section apart sentence by sentence, lines 228-262, which is whole for the section. Every sentence on when the wait starts or ends names the pushed commit and a `pull_request` check (read). Second, `git grep` for `pr checks`, `--watch`, `waits on CI`, `wait on CI`, `has a check` and `lists a check` over the tree, `trail/` and `CHANGELOG.md` left out (executed). That is whole for statements that name the wait's command and a sample for prose that names none, the limit `frame/design.md:9` already states. Outside the work item's frame and fragment, it lists the section, the pin case and `tests/behaviour/test_release_hygiene.py:178`. The last cites the measured exit, not the start condition. Inside, `frame/design.md:7`, `:8` and `:67` quote the issue and the old sentence as the work's starting point. Every other frame and fragment line states the new condition. The fragment's `### Fixed` heading at `changelog.md:3` now reads "waits for the first check of a `pull_request` run to report", as the body and the process row at `changelog.md:9` already did (read).

```seal
confirms: none
```
What matched: the orchestrator's fold at `36dc0cc1`, against the three sentences round 2's finding gave as paste-ready text (read: `git diff --word-diff f87b2957..03bad9d4 -- seal/threads`). *Scope* item 3 (`frame/design.md:36`) reads "ends once the pushed commit has a check of a `pull_request` run". S1 (`frame/design.md:48`) reads "polls the head and the count of `pull_request` checks first and runs `gh pr checks <N> --watch` only once the pushed commit has such a check; a `push` run's finished check on the same commit does not start the wait". That wording differs from round 2's text and states the same condition, with S1's own `push`-run case added. Plan row 1 (`frame/plan.md:24`) reads "It covers the three ways the wait starts early" and names all three. The commit touches only those three lines of the two files (executed: `git show --stat 36dc0cc1`).

```seal
confirms: none
```
What matched: the new judgment row at `frame/plan.md:50`, which answers round 2's *Not judged* row 1 as that row named its answerer. Its first ground holds against the paragraph. Where checks come from another CI service or event, the poll reaches the two-minute limit, and `skills/code-review/orchestration.md:253-262` has the report say no check of a `pull_request` run reported and the pull request is not checked (read). Its second ground holds for a fallback that ends the poll on another event's checks. That is round 1's false pass: `--watch` over finished checks exits 0 at once (`orchestration.md:249-251`). Round 2's row also named a narrower fallback. It runs the wait over other events' checks only at the limit and still reports the pull request as not checked. That one does not bring the false pass back. The row weighs it only through its third ground, that no repository this plugin runs in is known to have such checks. An opted-in repository's `templates/setup/hygiene.yml` runs `on: pull_request` (lines 27-28, read), so each one has at least one counted check, and the fallback would add nothing there. The decision stays fail-closed and stands on those grounds, so this round raises no finding. Its source, `skills/core/SKILL.md` *The first value*, is the value that decides between two designs that break no rule.

```seal
confirms: none
```
What matched: the new pin read against its group. It is one entry of the `said` tuple in `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` (lines 370-371). No other entry of that case holds the bold rule. The stop condition entry, "stops once the first prints the commit it pushed last and the second prints a count above 0", pins the poll and not the rule above it, and the round-2 mutant that cut the rule survived those entries. So the pin covers a fact nothing in its group covered. The repository's tests declare no duplicate pair over this case (read: the case is a text pin with no `TARGET`). The narrow set ran in one command at the target and gave 339 passed (executed). It held the 14 modules that name `skills/code-review/orchestration.md` (`git grep -lE`, executed) and three that read the work item's records: `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_no_document_names_the_old_roots.py` and `tests/behaviour/test_a_release_is_sized_by_a_criterion.py`. `tests/behaviour/test_docs_line_wrap.py` among them passed over the rewrapped lines 229-230. The fix pass's "915 passed over 30 modules" is an aggregate and was not re-run as one number. The suite stays labelled `unverified`, as `gaps.md:7` labels it, with the orchestrator as its answerer, and that label is honest: no party has run it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The paragraph followed on a live pull request, S1 and S2: whether the head is stale right after a push, and how long the pushed commit takes to list its first `pull_request` check. A push is a write, so this round took no measurement. Carried from round 2 | `frame/questions.md:15`, `gaps.md:8` | the orchestrator, at this work's pull request after its first push |
| Whether `--watch` ends before a job that waits on another through `needs:` lists its check. Carried from round 2, outside the fix diff | `frame/plan.md:18` | the orchestrator, at this work's pull request, with Q1 |
| The full suite, the repository-wide lint and the format check at the target. This round ran 17 modules and no broad command (contract rule 2). This round leaves no finding open, so what comes due is the orchestrator's broad run by `seal gate`, then the sealer's spawn | `gaps.md:7` | the orchestrator, by `seal gate`, then the sealer |

## Probes

| Command | Result |
|---|---|
| In the clone, `git checkout a9468abd -- skills/code-review/orchestration.md`, then `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge` | exit 1; `1 failed`, on the new pin; the file was restored to `03bad9d4` and `git status --short` was empty |
| In the clone, `bin/seal mutate skills/code-review/orchestration.md --timeout 300` over the same case with `-x`, three `--replace` pairs: the rule cut to "has a check.", to "has a check run.", and to "starts the wait." | baseline passes; 3 mutants, 3 red, 0 survived; `seal mutate` restores the file from held bytes, and `git status --short` was empty |
| In the clone, `git grep -n` for `pr checks`, `--watch`, `aits on CI`, `ait on CI`, `has a check` and `lists a check`, with `seal/threads/*/trail/*` excluded and `CHANGELOG.md` filtered out | hits in `skills/code-review/orchestration.md`, `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_release_hygiene.py:178`, `tests/skills/test_session_cost.py:5604` (an unrelated `pnpm` flag), and the work item's `frame/` and `changelog.md` |
| In the clone, `bin/test -q` over the 14 modules `git grep -lE 'code-review/orchestration\|"code-review", "orchestration' -- tests` lists, with `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_no_document_names_the_old_roots.py` and `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` | exit 0; 339 passed |
