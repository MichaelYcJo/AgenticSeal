# Review round 2: 1795849900-merge-owes-what-it-can-catch

```iadd
target: 235195ca, fixes 561bc67a..235195ca
```

A verifying round over the fixes to round 1, `561bc67a..235195ca`. The range holds four commits and no merge (executed, `git rev-list --merges 561bc67a..235195ca` printed nothing). `1ff9417e` adds round 1's record. `ca3a10bc` is the framer's fold of findings 1 to 3 into `frame/design.md` and `frame/plan.md`. `dcfbfbc8` is the fix pass. `235195ca` adds round 1's close blocks. The code this round reviews is what `dcfbfbc8` changed: `skills/code-review/orchestration.md:340-345` and `skills/code-review/orchestration.md:371-374`, `skills/code-review/gate-to-pull-request.md:40`, and `tests/text/test_the_rules_have_one_owner.py:608-668`. The base `release/v0.42.0` still stands at `596c79a6`, an ancestor of HEAD (executed, `git rev-parse` and `git merge-base --is-ancestor`). Every record that `agents/proofer.md` step 3 names was read whole at `235195ca`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`.

Facts carried from round 1 and not established again: the framer's `gh` reads (G2, G10, G22, G26), and round 1's `--remerge-diff` probe for D1, since the fix range changes neither D1 nor the paragraph that states it. Round 1's measure of the core, 9,995 characters, is carried too, because the range changes nothing under `skills/core/` or `lib/` (executed, `git diff --stat 561bc67a 235195ca -- skills/core lib` printed nothing). Each round 1 finding's `evidence: executed` search was run again at the target, and the results are named under *Confirmations*.

## Findings

### 1. The owner case pins the exit 0 row's act word for word, where *Scope* item 9 names the citation and the case leaves each row's act to the proofer

```iadd
severity: should
location: `tests/text/test_the_rules_have_one_owner.py:662-668`, `tests/text/test_the_rules_have_one_owner.py:611-614`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/gaps.md:8`
evidence: read `tests/text/test_the_rules_have_one_owner.py:596-670`, `docs/running/what-a-script-gates.md:103`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md:48`; executed `bin/agentic mutate skills/code-review/gate-to-pull-request.md --replace <the exit 0 row's act> "treats the pull request as checked at HEAD; under" --tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge"`, `git grep -n -F -e "exit 0 row's exception" -e "exception of the" -- agentory/threads/1795849900-merge-owes-what-it-can-catch tests`
regression: round-1#2
```

Why it matters: the unit is the pin that `dcfbfbc8` added to the owner case at `tests/text/test_the_rules_have_one_owner.py:662-668`. `frame/design.md` *Scope* item 9 (line 48) says the case "may pin the citation". The fix pass pinned the whole of the row's new act instead, every word from "treats the pull request as checked at HEAD" to "gives that stand-in". The defect came from pinning the row as the fix wrote it, where the frame names the fact to pin. `docs/running/what-a-script-gates.md:103`, the row for the cases under `tests/text/` that read prose, says "a case pins a fact a reader acts on" and "one that pins wording goes". The case's own docstring (lines 603 to 605) says it holds the commands, the exit codes and the flag, and that "each row's act is the proofer's to read". The fact an orchestrator acts on is that the exit 0 row sends it to the owner section, where the stand-in's conditions stand. That fact is the citation in the row. A later edit that keeps the citation and rewords the exception fails the case, so the case refuses a sentence whose meaning holds. `skills/core/SKILL.md` *The first value* names a script that does that as the worst result a check can give. The mutation this round ran shows the pin red with the exception taken out. A pin of the citation in the row's cell would fail under the same mutation as well, since the mutation takes the citation out with the exception (read).

The search printed the docstring line `tests/text/test_the_rules_have_one_owner.py:613` and `gaps.md:8`, which state what the case holds in the same terms. The snippet covers both. The search is a sample under contract rules 12 and 19, since a statement in other words escapes it. Round 1's close of finding 2 states the same pin in its `answer:` line; that is an earlier record, and this round does not ask for it to be edited.

The pin, `tests/text/test_the_rules_have_one_owner.py:659-668`: drop the four comment lines and the string that open with "The exit 0 row's act after such a merge", keep the `gh pr checks` entry, and add these lines after the loop.

```python
    # The exit 0 row's act after a merge whose broad run the pull request's
    # checks stood in for sends the orchestrator to the owner section, where
    # the stand-in's conditions stand. The case holds that citation in the
    # row; the row's words are the proofer's to read.
    passed = steps[
        steps.index(f"| {wait.PASSED} |") : steps.index(f"| {wait.FAILED} |")
    ]
    assert (
        "`skills/code-review/orchestration.md` *Orchestrator: the pull request "
        "opens once the work item is cleared*" in passed
    ), "the exit 0 row no longer cites the section that gives the stand-in's conditions"
```

The snippet assumes no OS boundary. It does assume that `steps`, flattened by `tests/conftest.py#flat`, holds `| 0 |` once and `| 1 |` once. At the target each stands once in the text after the heading (executed, a `python3 -I -c` read of `skills/code-review/gate-to-pull-request.md` counted 1 and 1, and the cut held the citation). By contract rule 15 the fix pass shows the new assertion red with the citation taken out of the row.

The docstring, `tests/text/test_the_rules_have_one_owner.py:611-614`, from "Round 1 of that work item":

```text
    proofer's to read. Round 1 of that work item adds the read that shows
    the job standing in for the broad run passed rather than skipped, and
    the exit 0 row's citation of the section that gives that stand-in's
    conditions, and the case holds the command and the citation."""
```

`gaps.md:8`, the clause that opens with "The owner case holds":

```text
The owner case holds the commands the orchestrator types, `git show --remerge-diff` and `gh pr checks <N>`, and the citation of that section in the `agentic pr-wait` table's exit 0 row, and not the act each one leads to;
```

```iadd
verdict: fixed f8ab0ed2
answer: Applied the paste-ready fix to the pin: the owner case drops the string that held the exit 0 row's whole act, keeps the `gh pr checks <N>` entry, and after the loop cuts the steps between `| 0 |` and `| 1 |` and asserts the citation of `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* inside that cut. `gaps.md:8` takes the snippet's clause. The docstring takes the snippet with one change, in my own words: it names "The first review round of #1583 and #1631" where the snippet says "Round 1 of that work item", since the settle removes that work item's directory and this round's *Confirmations* names that gap. Shown red by contract rule 15 at `f8ab0ed2`: `agentic mutate skills/code-review/gate-to-pull-request.md` replacing the row's "where it first takes the conditions `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* gives that stand-in; under" with "where it first takes the conditions of that stand-in; under", which takes the citation out of the exit 0 row alone and leaves exit 6's citation outside the cut, printed `red: the cases failed against the mutation (exit 1)`, failing at "the exit 0 row no longer cites the section that gives the stand-in's conditions". The case no longer pins wording: the same command with the exception reworded and the citation kept, "but after a merge the pull request's checks stood in for, it first takes the conditions", printed `SURVIVED`. The evidence's `git grep -n -F -e "exit 0 row's exception" -e "exception of the"` over the work item's directory and `tests`, run again at `f8ab0ed2` outside the round records, prints nothing. The narrow set `bin/test tests/skills/test_chain_check.py tests/text tests/behaviour tests/lib/test_core.py tests/hooks/test_core_start.py tests/skills/test_pr_wait.py -q` printed 1217 passed, 10 skipped, and `uvx ruff check` and `uvx ruff format --check` over the test file are clean; every file of it is the `bin/test` suite's, which phase 1's *Verified by* cell names.
```

### 2. `frame/plan.md` *Technical context* says the work amends two other statements of its rule, and the fold has since added the exit 0 row as a third

```iadd
severity: should
location: `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/plan.md:7`
evidence: read `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/plan.md:5-11`, `agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/design.md:46-48`, `skills/code-review/gate-to-pull-request.md:40`; executed `git show ca3a10bc -- agentory/threads/1795849900-merge-owes-what-it-can-catch/frame/plan.md`, `git grep -n -F 'gate-to-pull-request' -- agentory/threads/1795849900-merge-owes-what-it-can-catch ':!agentory/threads/1795849900-merge-owes-what-it-can-catch/trail/rounds'`, `git grep -n -F -e 'two other statements' -e 'other statements of its rule' -- agentory/threads/1795849900-merge-owes-what-it-can-catch`
regression: round-1#2
```

Why it matters: the unit is `frame/plan.md` *Technical context*. `ca3a10bc` changed its second bullet (line 10) for finding 1. The fold that brought the exit 0 row into *Scope* as item 9 for finding 2 left the section's opening sentence as it was. Scope item 9 (`frame/design.md:48`) and the rewritten *Out of scope* bullet (line 56) put `skills/code-review/gate-to-pull-request.md`'s exit 0 row in the work, and `dcfbfbc8` amended it at line 40. The plan's opening sentence, at line 7, still says the work rewrites one paragraph "and amends the two other statements of its rule", the core's row and `skills/verify/SKILL.md`'s row. The defect came from the fold reaching the bullets that state the stand-in's conditions and not the sentence that counts what the work amends. The section is dated to the framer's read of `0148aa63`, but this sentence says what the work does, so it is read against the target (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). At the target the work amends three statements outside the paragraph. The inspector reads the plan against the tree, and the sentence lists the files a reader would check. It is also a count that a later change made false without editing it, which contract rule 19 asks a text not to write.

The first search printed G12, Scope item 9, the *Out of scope* bullet, `changelog.md:4` and the plan's *Judgments of the run* row at line 59. Each of those names the row as in scope or describes it, and none needs a change. The second search printed line 7 alone. Both searches are samples under contract rules 12 and 19. Two other sentences were weighed and stand. *Scope* item 7 (`frame/design.md:46`) says `changelog.md` holds `### Changed` "for Scope items 1 to 3". It does not say "only", and `changelog.md:4` now also names item 9's row. The *Phases* row (line 36) says phase 1 delivered items 1 to 7 at `1c332307`, and the *Judgments of the run* row at line 59 gives item 9 to the fix pass. The fix pass may still weigh item 7.

`frame/plan.md:7`, the sentence up to "It builds on three readers", replaced whole:

```text
The work rewrites one paragraph of `skills/code-review/orchestration.md` (lines 303 to 321, `frame/design.md` G3) and amends three other statements of its rule: one row of the core's invariant table (`skills/core/SKILL.md`, the row *No inspection without the broad run*), one row of `skills/verify/SKILL.md`'s table at line 268, and, by `frame/design.md` *Scope* item 9, the exit 0 row of `skills/code-review/gate-to-pull-request.md`'s `agentic pr-wait` table at line 40.
```

The count stands in the sentence that opens the list it counts, as contract rule 19 allows. Line 40 is the row's line at `0148aa63` and at the target alike (executed, `git show 0148aa63:skills/code-review/gate-to-pull-request.md`).

```iadd
verdict: fixed 83ee5ce1
answer: The framer folded it: `83ee5ce1` replaced the opening sentence of `frame/plan.md` *Technical context* with the paste-ready fix's sentence, which names the exit 0 row by *Scope* item 9 as the third statement the work amends, and the same commit made *Scope* item 7 name item 9 beside items 1 to 3. The evidence's `git grep -n -F -e 'two other statements' -e 'other statements of its rule'` over the work item's directory, run again at `f8ab0ed2` outside the round records, prints `frame/plan.md:7` alone, which now reads "amends three other statements of its rule", the count standing in the sentence that opens its list. Read of the range: `agentic range agentory/threads/1795849900-merge-owes-what-it-can-catch --from 235195ca --out <scratchpad>/1795849900-merge-owes-what-it-can-catch/fix-2/range.txt` printed `agentic range: 235195caf4b115919497d4b8c5fa8bd1772134bd..f8ab0ed29d0480a3f125e46ee6b762e8195197d7` and wrote 558 lines, read to the last; it left no statement HEAD contradicts in a file this pass writes.
```

## Confirmations

```iadd
confirms: round-1#1
```
What holds: the stand-in's third condition at `skills/code-review/orchestration.md:340-344` now asks `gh pr checks <N>` to list as passed, not skipped, each job judged to run the `Broad gate` command's checks. The paragraph on a merge after the verdict spawns the inspector "once its conditions above hold at HEAD" (line 374) (read). The grounds hold: `skills/code-review/scripts/pr_wait.py#decide` (lines 293 to 301) passes every entry whose bucket is not in `BAD`, and `BAD` at line 152 holds `fail` and `cancel` alone, so a skipped check passes the wait (read). D4, S1, the *Removes* row, A1, *Technical context*, *The failure direction*, *Operational impact* and `changelog.md:4` carry the condition (read). The owner case is red with the paragraph's `` `gh pr checks <N>` `` replaced: `bin/agentic mutate` printed `red: the cases failed against the mutation (exit 1)`, at the assertion "the owner section no longer says '`gh pr checks <N>`'" (executed). The finding's `git grep -n -F 'pr-wait'` was run again at the target and printed the lines the close names (executed). I weighed the one that names a holder, `skills/core/SKILL.md:109`. Its *Held by* cell names `agentic pr-wait` after a merge of the base, and the wait alone does not see a skipped job. The column names the mechanism a party reads, and its other cells name scripts whose conditions stand in their homes. `frame/design.md` *Scope* item 2 asks for that name, and the cell has 5 characters of room under `lib/core.py#CAP`. So the cell stands, as the close says. I took the paragraph's "its conditions above" (line 374) to mean D4's conditions, as `frame/design.md` D6 states them, since the D5 paragraph places its own read at the hand-over.

```iadd
confirms: round-1#2
```
What holds: the exit 0 row at `skills/code-review/gate-to-pull-request.md:40` now has the orchestrator "first take the conditions `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* gives that stand-in" after a merge whose broad run the pull request's checks stood in for (read). The row no longer contradicts D5's paragraph, and it restates neither D4 nor D5, as *Scope* item 9 asks. The close's "the conditions" in place of the snippet's "the read of the base" covers finding 1's added condition too. That matches item 9's "the conditions D4 and D5 give that stand-in" (read, `frame/design.md:48`). The finding's `git grep -n -F 'treats the pull request as checked'` was run again at the target and printed the row, `skills/code-review/orchestration.md:356`, `changelog.md:4`, and `frame/design.md` lines 48, 70 and 81. Each agrees with the paragraph (executed). The pin the close names is red with the exception taken out (executed, *Probes*). Its form is this round's finding 1, and two of the work item's statements of the fold are this round's finding 2.

```iadd
confirms: round-1#3
```
What holds: R1's `to` at `frame/design.md:91-97` now lists the round as owed "where the merge's resolution changed a path outside the work item's records", and lists the broad run or the pull request's checks and the inspector apart from that condition. It no longer says "at the merge" (read). `skills/settle/scripts/rule_changes.py#parse`, run at the target over `frame/design.md` with the policy root `docs`, printed one `change` for `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, `errors=[]` and `unread=[]` (executed). R1's `from` stands once in that file with runs of whitespace collapsed (executed, a `tr -s` and `grep -o -F` count printed 1). The finding's `git grep -n -F "read from what the merge's" -- agentory docs skills`, run again at the target outside the round records, printed nothing (executed). The `to` names a round where the resolution changed a path outside the records, and not the case where the command does not run, which the paragraph treats as such a resolution (`skills/code-review/orchestration.md:321-323`). The `to` cites the section for what is owed, so it does not state the opposite.

```iadd
confirms: round-1#4
```
What holds: `gaps.md:12` says what *Scope* item 2 "asked ... before the fold at `41455989`", and the heading at `trail/phases/phase-1.md:7` says "asked at `e22357f1`" (read). The finding's `git grep -n -F "Scope* item 2 asks"`, run again at the target outside the round records, printed nothing (executed). The close also rewrote `gaps.md:8`. Its new clause is true of the case at the target: the case holds `git show --remerge-diff`'s command, `` `gh pr checks <N>` `` and the exit 0 row's exception (read, lines 654 to 668). This round's finding 1 changes what the case holds, and with it the clause.

What matched: the new unit in `frame/design.md` G25, the parse of R1 as rewritten, matches this round's own parse above. G12's added sentence matches `pr_wait.py#decide` (read).

What matched: the narrow run `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` exited 0, with 106 passed (executed). The second file holds the citations the fix added to sections that stand.

What matched: record against another work item's frame. The unsettled designs at the target are `1795841828-settle-only-release-note`, `1795841829-skill-descriptions` and `1795841830-find-leftovers-before-a-round`. None names *Work accumulates on a release branch*, `skills/code-review/gate-to-pull-request.md` or `agentic pr-wait` in its `## Rule changes` or anywhere else in its design (executed, a `grep` of each `file:` and `section:` line and of those words). `1795841829-skill-descriptions` holds no `## Rule changes` operation.

What matched: `pr.md`'s six quotes stand word for word, since `frame/questions.md` is unchanged in the range and the quoted row of `frame/plan.md` *Judgments of the run* is unchanged (read). The row the fold added at line 59 is not quoted, and `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* asks `pr.md` to quote the title's row, which it does. `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. No `gaps.md` row left the memo in the range: lines 8 and 12 were reworded in place (read, `git diff 561bc67a 235195ca`). `agentory/parity.json` is absent, so no parity comparison is owed. The chain check at the target printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed).

One gap is not a finding. The docstring sentence at `tests/text/test_the_rules_have_one_owner.py:611` names "Round 1 of that work item". The settle removes that work item's directory, so the name will point at a record that no longer stands in the tree. The docstring is read by whoever next edits the case, and the round names it here alone.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `gh pr checks <N>` lists a job whose job-level `if:` is false for the pull request with the bucket `skipping`. This round read `pr_wait.py`'s buckets and ran no pull request | `skills/code-review/orchestration.md:342-344` | the orchestrator, at the *Judgments of the run* row of the first merge whose broad run the stand-in takes |
| Whether this repository's `pull_request` run reads each check the `Broad gate` command runs, carried from round 1 | `.github/workflows/test.yml`, `agentory/config.json` | the orchestrator, at the merge's *Judgments of the run* row |
| Whether an orchestrator follows the new paragraphs and the exit 0 row. No reading of text shows an agent's behaviour | `skills/code-review/orchestration.md:315-379`, `skills/code-review/gate-to-pull-request.md:40` | the inspector, at the *Judgments of the run* row of the first work item whose run holds such a merge |
| #1631's owlery figures (G17) | `frame/design.md:25` | the repository owner |
| Q1 and Q2, open with their defaults taken | `frame/questions.md:15-16` | the repository owner |
| The broad gate: the full suite, the repository-wide lint and the format check. `gaps.md:7` labels it as not verified, with the orchestrator named | `gaps.md:7` | the orchestrator |

Nothing open in this round asks for a run that only the orchestrator takes. Once this round's two findings are closed and a round reads their fixes, the orchestrator's broad run comes due, then the inspector's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/agentic mutate skills/code-review/orchestration.md`, replacing the paragraph's `gh pr checks <N>` with `gh pr view <N>`, with `--tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge"` | `red: the cases failed against the mutation (exit 1)`, at line 670, naming `gh pr checks <N>` as no longer said; the file restored, `git status --short` empty |
| `bin/agentic mutate skills/code-review/gate-to-pull-request.md`, replacing the exit 0 row's act up to "gives that stand-in; under" with "treats the pull request as checked at HEAD; under", with the same `--tests` | `red: the cases failed against the mutation (exit 1)`, at line 670, naming the row's exception; the file restored |
| `rule_changes.parse` over `frame/design.md` at the target, policy root `docs`, under `python3 -I` | one `change`, `errors=[]`, `unread=[]` |
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | exit 0, 106 passed |
| `python3 -I -c` over `skills/code-review/gate-to-pull-request.md`, flattened and cut after the steps heading | the opener of the exit 0 row once and of the exit 1 row once, and the cut between them holds the owner section's citation |
