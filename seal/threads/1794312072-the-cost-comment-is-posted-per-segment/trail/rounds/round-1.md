# Review round 1: 1794312072-the-cost-comment-is-posted-per-segment

```seal
target: bb4a98683 against release/v0.37.2
```

The range is `8f99b773e..bb4a98683`, the whole branch, read in a `git clone --no-local` at `bb4a98683` under the round's scratch directory, since removed. This is the first round, so no fact is carried from an earlier record: every coordinate below was opened this round. No `seal/parity.json` stands, so no original is compared. The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md`. Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands.

## Findings

### 1. The section's one command never shows the orchestrator the Contract rule 6 line it is told to act on

```seal
severity: must
location: `skills/verify/orchestration.md:184-200`, `skills/verify/orchestration.md:236-245`, `skills/verify/scripts/session_cost.py:3365-3371`, `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/frame/design.md:57`, `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/frame/design.md:69`, `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/changelog.md:5`, `tests/text/test_a_segment_feeds_the_flow_log.py:417`
evidence: executed `bin/test tests/skills/test_tmp_rule6_reach.py -q -p no:xdist -k probe -s` in the clone (the `## Probes` row); read `skills/verify/scripts/session_cost.py:3365-3371`, `skills/verify/scripts/session_cost.py:2932-2971`, `skills/verify/orchestration.md:184-245`, `tests/skills/test_session_cost.py:5358-5388`
```

Why it matters: this work's one added mechanism is the Contract rule 6 line in `--work-item`'s reading. The frame adds it so that the line still reaches an orchestrator once the per-segment `--segments` run ends. *Scope* item 4 says "The run's one reading then carries the line the per-segment `--segments` run printed", and `frame/plan.md` *Alternatives considered* row H rejects keeping it in `--segments` alone because "No step the orchestrator runs prints it". The section then has the orchestrator act on the line: "The reading prints it ... so the orchestrator gives it the home that `skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson is written* gives a lesson" (`skills/verify/orchestration.md:238-245`).

The one command the section prescribes is the posting form, `seal cost --work-item <dir> --post --says <file>` (`:188`). With `--post`, `work_item` sends the whole reading into a buffer and hands the buffer to `post` (`session_cost.py:3368-3371`). So the orchestrator's terminal shows only `post`'s one state line. The probe ran that command over the S5 fixture, a segment that made one `Agent` call, under three log states:

- One open log: exit 0. The terminal printed only "posted the run's reading to #42". The line went into the issue comment, which no step of the section has the orchestrator read.
- No issue has ever carried the label, the case the section itself calls the one "most installed repositories meet" (`:219-220`): exit 0. Nothing was posted, the terminal printed only the no-history line, and the rule 6 line was computed and thrown away.
- A closed log: exit 1. Same as no history: the line reached no one.

An unreadable `gh` lookup, more than one open log and an empty `--says` reading discard the buffer the same way, by `post` at `:2953-2985` and `said` at `:3011-3025` (read).

So the build does not meet the frame's acceptance row S5 (`frame/design.md:57`), which says that with or without `--post`, "the reading prints the Contract rule 6 line naming that segment's file and its count". It prints the line only without `--post`, and the section never names that form. The S5 case (`tests/skills/test_session_cost.py:5358`) passes because, under `--post`, it reads the posted body from one open log and never the terminal. The changelog says the same as S5, "`seal cost --work-item` prints the Contract rule 6 line" (`changelog.md:5`), and the S5 case cannot show that claim false. The old section had the orchestrator read the numbers first and post second (`8f99b773e:skills/verify/orchestration.md:254-258`). It also said "Without `--post` it prints the same reading and posts nothing". The rewrite dropped both, and the frame's D1 item 3 (`frame/design.md:69`) prescribes the posting command alone.

The same cause reaches the `--says` file. The section says that file holds "the orchestrator's sentence on what the readings say" (`:191-193`). The only command the section names shows no reading before the post, so the orchestrator writes that sentence about numbers it has not seen. The release's step in `docs/releasing/release-checklist.md:216-219` has the same shape. It stood before this work, and this finding does not ask the fix to change it.

The fix keeps one post per work item and puts the reading in front of the orchestrator first. Replace `skills/verify/orchestration.md:184-189` with:

````markdown
**The run ends when the work item's last segment has handed back**, the
sealer's where one runs. The orchestrator first reads the run with
`seal cost --work-item <the work item's directory>`, which prints the rows
the post will carry and any `Contract rule 6` line below them, and posts
nothing. It writes the `--says` file from that reading, then posts it with
one command:

```
seal cost --work-item <the work item's directory> --post --says <file>
```
````

and replace the second sentence of `:238-240` with:

```markdown
The reading without `--post` prints it where a segment's own transcript
holds an `Agent` call, and names that segment's file and its count; the
posted comment carries the same line inside its fence.
```

This snippet does not cover every statement of the fact. The fix pass also owes the following:

- `frame/design.md` D1 item 3 (`:69`) and S1 (`:53`), which name one command, need the read step beside the post.
- S5 (`:57`) needs to say where the line is printed and where it is posted.
- `changelog.md:3` and `:5` need to say the same.
- The pin at `tests/text/test_a_segment_feeds_the_flow_log.py:417` should assert that the section names the form without `--post` as the one that prints the line. Contract rule 14 asks for that pin, and it is seen red with the new sentence deleted.

The other way to fix this is in code: `work_item` could print the rule 6 lines to the terminal as well as posting them. That changes printed output, so it owes its own pin, and it still leaves the `--says` sentence written without the numbers in view.

## Confirmations

What matched: *Scope* item 3 and S3. `grep -n -F -e '#300' -e '#377' -e '#642' -e 'reading taken before' skills/verify/orchestration.md` printed nothing (executed). The analyse sentence on the skill carrying the three changes is gone from `session_cost.py:1094-1098` (read).

What matched: S6. `git grep -n -F -e 'Measure the segment' -e 'feed the flow log' -- ':!seal/threads'` prints 10 lines, and none holds the old heading. Phase 2 claimed 10 lines and four wrapped citations. The four second lines I read at `.github/scripts/roll_flow_measurement_issue.py:5-6`, `skills/code-review/orchestration.md:423-424`, `skills/commit-pr-convention/SKILL.md:257-258` and `tests/text/test_a_segment_feeds_the_flow_log.py:53-54` each continue "Measure the run, and" (executed, read). `skills/implement/orchestration.md:174-176` cites the new heading wrapped before "log" (read).

What matched: S8 and the section's size. Phase 2 claimed 5,232 words for `skills/implement/orchestration.md`, and 1,352 words for the section where it had 3,502. `wc -w` gives 5,232. The section from `:160` to the file's end gives 1,352, and `8f99b773e`'s `:160-483` gives 3,502 (executed).

What matched: S1's text search. `git grep -n -i -E 'after every crafter or proofer segment|segment that just' -- skills docs agents templates` printed nothing (executed). A wider sweep of `skills`, `agents`, `templates`, `README.md`, `README.ko.md`, `CONTRIBUTING.md`, `.github`, `docs` and `evals` for a per-segment post or measurement found none outside the three `docs/` files that `## Rule changes` covers (executed, `git grep -n -i -E` over segment-and-post wordings, each hit read). This sweep is a sample of an open class of wordings, as the frame's G12 says of its own list.

What matched: D1, read against `skills/verify/orchestration.md:160-280`. The section holds the items in D1's order: the opening, which names neither label, then the two logs, the command, the exit codes, the rule 6 line, and the run's table with its three paragraphs. The exit codes at `:217-234` match `session_cost.py#work_item` `:3295-3371`, `#post` `:2932-3008`, `#said` and `#main` `:3374-3435` (read). The one exception is finding 1.

The exit-1 list at `:223-226` leaves out two exits the code has. One is a `routing.md` with no branch, a `sys.exit` in `work_item_keys` at `:3148-3153`. The other is a `--says` path that cannot be opened, a traceback from `read_says` at `:2928`. Its catch-all sentence, "Every other exit 1 is named in the run's hand-over", gives each an action, so this is no finding. "The run's hand-over" appears in no other file. The only report the orchestrator still owes after the last segment is its report to the person, so this round reads the phrase as that report.

What matched: D2 and S4, a sample. Phase 1 named a line for each paragraph. I opened the module docstring at `session_cost.py:60-75`, `measure_segments` at `:1777-1782`, the `--spawns` page lines at `:2300-2310`, `analyse`'s comment at `:1114-1128`, the overlap comment at `:2398-2414` and the 900-second cut at `:1152`. Each holds what the old section's paragraph said. The two new docstring paragraphs at `:67-75` match the old text at `8f99b773e:skills/verify/orchestration.md:353-359` and `:412-416` (read). The sample did not reach the other nine rows of phase 1's D2 table.

What matched: D3 and *Scope* item 7. The roll's close comment now names `docs/running/measuring-a-run.md` *Where a reading goes* at `.github/scripts/roll_flow_measurement_issue.py:364-365`, and that section holds the reasoning for the two labels and for never opening a log at `docs/running/measuring-a-run.md:110-131` (read). The docstring rewritten at `:7-10` agrees with the exit-1 bullet at `skills/verify/orchestration.md:223-231`. The comment `:382-386` that D3 keeps still holds at `:383-386` (read).

What matched: D4. `report_work_item` calls `report_breaches` with `own_file: True` at `session_cost.py:3292`. The early return at `:2544-2545` stops the line before the pair of counts against unnamed segments (read). The narrow run over `Test_work_item`, `Test_post` and `Test_emit` passed 46 cases (executed).

What matched: D5. The five removed cases are gone and `SECTION_HEADING` names the new heading. The S2 case at `tests/text/test_a_segment_feeds_the_flow_log.py:163` pins the three codes and "the run's hand-over". The module's narrow run passed 19 cases (executed). Phase 2 claims it saw the S2 case red by `seal mutate`, with three mutants all red. I did not run that again, so the claim is read, not executed.

What matched: the new tests against their groups. `bin/seal layout --pairs` names no pair that holds `test_a_segment_that_spawned_prints_the_contract_rule_6_line` or `test_the_section_says_what_each_exit_of_the_command_means` (executed). No case in `Test_work_item` pinned the rule 6 line before the S5 case. No case in the flow-log module pinned the exit codes before the S2 case (read).

What matched: the rule changes. Each `from` of the seven operations in `frame/design.md:121-155` stands word for word in its section at the target: `docs/running/measuring-a-run.md:99-135`, `docs/releasing/release-checklist.md:205-220` and `docs/releasing/issues-and-milestones.md` (executed, `skills/settle/scripts/rule_changes.py#parse` over the frame, then a substring check of each operation's `from` in its file with whitespace collapsed). `git diff --stat 8f99b773e bb4a98683 -- docs` prints nothing, so G1 holds (executed).

What matched: `frame/questions.md` Q2, for this round. `python3 skills/code-review/scripts/chain_check.py --baseline 8f99b773e --root <the branch worktree> --worktree`, run over this record, printed no notice at a line of `frame/design.md` naming a test pin or a copy. Its only refusal in this record is finding 1 standing open (executed).

What matched: `pr.md`. Each of its five quotes stands word for word in `frame/plan.md` at the place its coordinate names, with whitespace collapsed (executed, a substring check over the collapsed file). `bin/seal pr-body` composed the body into the round's scratch directory with exit 0 (executed).

What matched: `changelog.md`. Its counts and sentences hold at the target: 39 segment comments on #1458, whose title is "after 0.36.0", the word counts above, and the printed messages at `session_cost.py:2971-2974` and `:3007`. The exception is the sentence at `:5`, which finding 1 names. The sentence at `:16` says the three `docs/` files keep the old rule until the settle, and that holds (read; executed, `gh issue view 1458`).

What matched: the judgments of the run. #1510 is open, and its title names the G13 attribution that `frame/plan.md:63` homes there (executed, `gh issue view 1510`).

Two rewordings in `session_cost.py` left lines unwrapped: `:39`, at 127 characters, and `:2576`, at 124. Neither is a finding. `ruff.toml` selects no `E501`, and a line that only reads badly is no defect.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD; the suite stays `unverified` in this round, which ran two narrow modules | `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/gaps.md:8` | the orchestrator, by `seal gate --record` |
| The run's post over this machine's transcripts and the open log, and the release's later run posting nothing; contract rule 6 withholds the post from this round | `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/gaps.md:7`, `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/gaps.md:9` | the orchestrator, by the tree's `bin/seal cost --work-item` when the run ends |
| Phase 2's `seal mutate` runs that saw the S2 case and the roll pin red | `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/trail/phases/phase-2.md:27` | read from the record, not re-run; the sealer samples it |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_rule6_reach.py -q -p no:xdist -k probe -s`, in the clone, a subclass of `Test_work_item` running the S5 fixture through `main` with `--post` under one open log, no history and a closed log | one open: exit 0, terminal "posted the run's reading to #42", one comment posted with the rule 6 line in it. No history: exit 0, terminal the no-history line, nothing posted. Closed: exit 1, terminal the closed-log line, nothing posted. In all three the terminal held no `Contract rule 6`. The file was deleted after its one run |
| `bin/test tests/text/test_a_segment_feeds_the_flow_log.py -q`, in the clone | exit 0, 19 passed |
| `bin/test tests/skills/test_session_cost.py -q -k 'Test_work_item or Test_post or Test_emit'`, in the clone | exit 0, 46 passed |
| `bin/seal pr-body seal/threads/1794312072-the-cost-comment-is-posted-per-segment --body <scratch>/body.md` | exit 0, the body written into the round's scratch directory |
