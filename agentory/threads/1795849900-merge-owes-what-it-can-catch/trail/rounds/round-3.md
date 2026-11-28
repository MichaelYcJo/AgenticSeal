# Review round 3: 1795849900-merge-owes-what-it-can-catch

```iadd
target: 96d4fe61, fixes 235195ca..96d4fe61
```

This round verifies the fixes to round 2, over `235195ca..96d4fe61`. The range holds four commits and no merge (executed: `git rev-list --merges 235195ca..HEAD` printed nothing). `0ca4b058` adds round 2's record. `83ee5ce1` is the framer's fold of round 2's finding 2 into `frame/plan.md:7` and `frame/design.md` *Scope* item 7, with one sentence added to G24. `f8ab0ed2` is the fix pass for finding 1. `96d4fe61` adds round 2's close blocks. So the code this round reviews is what `f8ab0ed2` changed: `tests/text/test_the_rules_have_one_owner.py:611-615` and `tests/text/test_the_rules_have_one_owner.py:660-675`. The local ref `release/v0.42.0` still stands at `596c79a6`, the merge base of HEAD (executed: `git rev-parse release/v0.42.0` and `git merge-base HEAD release/v0.42.0`; no fetch was run). Every record that `agents/proofer.md` step 3 names was read whole at `96d4fe61`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, and the headings and coordinates of `trail/rounds/round-1.md` and `trail/rounds/round-2.md`.

Facts carried from earlier rounds and not established again: the framer's `gh` reads (G2, G10, G22, G26), round 1's `--remerge-diff` probe for D1, round 1's measure of the core at 9,995 characters, and round 2's parse of R1. The range changes none of `skills/`, `lib/`, `frame/design.md` *Data & interfaces* or `## Rule changes` (executed: `git log --stat 235195ca..HEAD` lists `gaps.md`, `tests/text/test_the_rules_have_one_owner.py`, `frame/design.md` lines 32 and 46, `frame/plan.md:7` and `trail/rounds/round-2.md` alone). The paragraphs of `skills/code-review/orchestration.md` and the exit 0 row of `skills/code-review/gate-to-pull-request.md` stand as round 2 read them at `235195ca`.

## Findings

This round opens no finding.

## Confirmations

```iadd
confirms: round-2#1
```
What holds: the owner case no longer pins the exit 0 row's wording. At `tests/text/test_the_rules_have_one_owner.py:665-675` it cuts the steps from `| 0 |` to `| 1 |` and asserts that the cut holds the citation of `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* (read). The cut holds the exit 0 row alone. In the text after the steps heading, `| 0 |` and `| 1 |` each stand once (executed: a `python3 -I -c` count printed `1 1`). The exit 6 row's citation of the same section stands outside the cut. The close's claim holds by three mutations, each run with `bin/agentic mutate skills/code-review/gate-to-pull-request.md` and the case alone as `--tests` (executed, *Probes*). The case fails with the citation taken out of the exit 0 row and the rest of the row kept, and with the whole exception taken out. Each fails at line 672, the new assertion, and not at a line that names something else. With the exception reworded and the citation kept, the mutation printed `SURVIVED`. So the case holds the fact an orchestrator acts on, as `docs/running/what-a-script-gates.md:103` asks, and the case's docstring states (lines 603 to 605). The docstring at lines 611 to 615 says what the case now holds: the `gh pr checks <N>` command and the row's citation. It names "The first review round of #1583 and #1631" in place of the snippet's "Round 1 of that work item". That clears the gap round 2 named outside its findings, a name that the settle would leave pointing at a removed record. `gaps.md:8` carries the snippet's clause word for word (read). Round 2's search `git grep -n -F -e "exit 0 row's exception" -e "exception of the"` over the work item's directory and `tests`, with the round records left out, printed nothing (executed). `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` exited 0, and `uvx ruff check` and `uvx ruff format --check` over the test file each exited 0 (executed).

```iadd
confirms: round-2#2
```
What holds: `frame/plan.md:7` now says the work "amends three other statements of its rule". It lists the core's row, `skills/verify/SKILL.md`'s row at line 268, and, by *Scope* item 9, the exit 0 row of `skills/code-review/gate-to-pull-request.md`'s `agentic pr-wait` table at line 40 (read). The count stands in the sentence that opens its list, as contract rule 19 allows. Both line numbers hold at `0148aa63`, the commit the section is dated to (executed: `git show 0148aa63:skills/verify/SKILL.md` line 268 is the row *A merge, or a dependency bump*, and `git show 0148aa63:skills/code-review/gate-to-pull-request.md` line 40 is the `| 0 |` row). The list is whole against the diff. `git diff --stat 596c79a6 HEAD` names, outside the records and tests, `skills/code-review/orchestration.md`, the three files the sentence lists, `agentory/follow-up.md` and `.claude-plugin/plugin.json` (executed). The follow-up row and the version move state no part of the rule. Round 2's search `git grep -n -F -e 'two other statements' -e 'other statements of its rule'` printed `frame/plan.md:7` alone, in its new wording (executed).

What matched: the two other sentences the fold `83ee5ce1` wrote. *Scope* item 7 (`frame/design.md:46`) now gives `### Changed` to items 1 to 3 and 9. `changelog.md:4` names the exit 0 row's citation, so item 9 has its line (read). G24's added sentence says that round 1's finding 2 found the exit 0 row, which G24's search had missed. `trail/rounds/round-1.md:49` heads that finding with the exit 0 row (read).

What matched: the rest of the records read whole at the target. The range changed none of `routing.md`, `frame/questions.md`, `changelog.md`, `pr.md` or `trail/phases/phase-1.md`, so their sentences stand as round 2 read them. `pr.md`'s six quotes still stand word for word, since `frame/questions.md` Q1 and Q2 and the title's row of `frame/plan.md` *Judgments of the run* are unchanged (read). `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. No row of `gaps.md` left the memo in the range: line 8 was reworded in place (read, `git show f8ab0ed2`). `agentory/parity.json` is absent, so no parity comparison is owed. The test case changed in the range is an existing case and no new one, so no group comparison is owed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `gh pr checks <N>` lists a job whose job-level `if:` is false for the pull request with the bucket `skipping`, carried from round 2. No pull request was run | `skills/code-review/orchestration.md:342-344` | the orchestrator, at the *Judgments of the run* row of the first merge whose broad run the stand-in takes |
| Whether this repository's `pull_request` run reads each check the `Broad gate` command runs, carried from round 1 | `.github/workflows/test.yml`, `agentory/config.json` | the orchestrator, at the merge's *Judgments of the run* row |
| Whether an orchestrator follows the new paragraphs and the exit 0 row. No reading of text shows an agent's behaviour | `skills/code-review/orchestration.md:315-379`, `skills/code-review/gate-to-pull-request.md:40` | the inspector, at the *Judgments of the run* row of the first work item whose run holds such a merge |
| Whether the base has moved on the remote since `596c79a6`. This round read the local ref and ran no fetch | `release/v0.42.0` | the orchestrator, before the broad run |
| #1631's owlery figures (G17) | `frame/design.md:25` | the repository owner |
| Q1 and Q2, open with their defaults taken | `frame/questions.md:15-16` | the repository owner |
| The broad gate: the full suite, the repository-wide lint and the format check, labelled `unverified` with the orchestrator named at `gaps.md:7`. The label is honest: no record claims the suite passed | `gaps.md:7` | the orchestrator |

This round leaves nothing open. What comes due is the orchestrator's broad run, then the inspector's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/agentic mutate skills/code-review/gate-to-pull-request.md --replace` on the exit 0 row, "where it first takes the conditions" through "gives that stand-in; under" replaced with "where it first takes the conditions of that stand-in; under", with `--tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge"` | the case failed, 1 failed, at `tests/text/test_the_rules_have_one_owner.py:672`; the file restored, `git status --short` empty |
| the same, with "except after a merge whose broad run the pull request's checks stood in for, where it first takes" replaced with "but after a merge the pull request's checks stood in for, it first takes", the citation kept | `SURVIVED`, 1 passed |
| the same, with the whole exception, from ", except after a merge" through "gives that stand-in;", replaced with ";" | the case failed, 1 failed, at line 672 |
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` | exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `tests/text/test_the_rules_have_one_owner.py` | exit 0 and exit 0 |
| `python3 -I -c` over `skills/code-review/gate-to-pull-request.md`, split after the steps heading, counting `\| 0 \|` and `\| 1 \|` | `1 1` |
