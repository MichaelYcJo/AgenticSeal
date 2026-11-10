# Review round 2: 1794312072-the-cost-comment-is-posted-per-segment

```seal
target: a6f0006de, fixes bb4a98683..a6f0006de
```

This is a verifying round. The range is `bb4a98683..a6f0006de`, five commits: the round 1 record (`ae3a7176b`), the framer's fold of finding 1 (`d258c0bb7`), the fix (`8bc38ba9f`), a changelog item and a `gaps.md` row (`9dc104229`), and the close block (`a6f0006de`). Its code and tests are `skills/verify/orchestration.md`, `tests/text/test_a_segment_feeds_the_flow_log.py` and a docstring in `tests/skills/test_session_cost.py`. `git diff --stat bb4a98683..a6f0006de` names no file under `docs/` and no `session_cost.py` (executed). I read the branch worktree and changed nothing there but this record. Every probe and narrow run went in a `git clone --no-local` at `a6f0006de` under the round's scratch directory, since removed.

The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, both phase records and `trail/rounds/round-1.md`. Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands. No `seal/parity.json` stands, so no original is compared.

Carried from round 1 as coordinates and not re-derived, because the range does not touch the files they stand in: the D2 sample in `session_cost.py`, S8's count of `skills/implement/orchestration.md`, D3 and D4, the `from` of each rule-change operation in the three `docs/` files, and the `gh` reads of #1458 and #1510. Re-derived this round: `session_cost.py#work_item` (`:3295-3371`), `#post` (`:2932-3008`) and `#said` (`:3011-3025`), opened again because the section's new sentences describe them.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the section now shows the orchestrator the reading before it posts. `skills/verify/orchestration.md:184-198` has it read the run first with a fenced `seal cost --work-item <the work item's directory>`, which posts nothing, write the `--says` file from that reading, and then post with a second fenced command, `--post --says <file>`. `:200-201` says why the read comes first, and `:248-252` names the read without `--post` as the form that prints the `Contract rule 6` line, with the posted comment carrying it in its fence. `:233-234` keeps the read where the label has no history, and `:210-211` puts `--label flow-baseline` on both commands (read). `session_cost.py#work_item` matches each sentence. Without `--post`, it reads the log's comments, leaves out the segments a comment names, and prints `report_work_item`'s reading and any `log_note` (`:3305-3368`). With `--post`, it redirects that reading into `post` (`:3369-3371`) (read). The probe in `## Probes` ran the S5 fixture through `main` under one open log, no history and a closed log. The read printed the `Contract rule 6` line and exited 0 in all three, and under the last two it also printed the log's state. The posting form's terminal held no `Contract rule 6` line in any of the three (executed). That is round 1's probe written again from its `## Probes` row, with the read added beside each post. The fix pass claimed `session_cost.py` is unchanged because `frame/plan.md:31`, row M, rejects the code route. The diff names no such file, and row M says the read first "changes no output" (read; executed, `git diff --stat`).

What matched: the pins of the fix. `tests/text/test_a_segment_feeds_the_flow_log.py:437` asserts the read as a line of its own, so it cannot match the posting line. `:444` asserts the sentence naming the read without `--post`. I removed only the fenced read from the section in the clone, and the case failed on `:437`'s assertion. I then put only the sentence back to "The reading prints it", and the case failed on `:444`'s assertion. Each time the failure was the guard the assertion names. This repeats the fix pass's `seen red` claim (executed). The S5 case at `tests/skills/test_session_cost.py:5358-5390` already read the printed output without `--post` (`:5378`) beside the posted body, and only its docstring changed (read). The narrow runs passed: the flow-log module, `tests/text/test_the_chain_section_has_one_shape.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, 89 cases, and `Test_work_item`, `Test_post` and `Test_emit`, 46 cases (executed).

What matched: the new tests against their group. The range adds no case. It adds two assertions to `test_the_section_says_the_mode_notices_a_spawn_inside_a_segment`, and no other case of the flow-log module pins the read's fence or the sentence (read). The S5 case's docstring now says that with `--post` the terminal shows only the post's state line, and no assertion of that case reads the terminal after the post (`tests/skills/test_session_cost.py:5380-5390`). The range did not change that behaviour, so this is a docstring that claims more than it pins and no finding.

What matched: the framer's fold at `d258c0bb7`. G18 cites `session_cost.py#work_item` `:3352-3358` under the Grounding's `98a0fa824`, and at that commit the lines hold the `--post` branch it describes (executed, `git show 98a0fa824:skills/verify/scripts/session_cost.py`). *Scope* items 1, 4 and 6, S1, S5 and D1 items 3 to 5 name the read and the post, and the section holds each in D1's order (read). The *Judgments of the run* row of finding 1 cites `:3368-3371` at the target, and those lines are the redirect (read). The new line in `frame/questions.md` points at G18, D1 item 3 and row M, and each stands (read).

What matched: the class of finding 1, a sample. The fix pass claimed that its search of the open class found no other statement of the single command outside `docs/`. I searched `.github`, `README.md`, `README.ko.md`, `agents`, `skills`, `templates` and `evals` for `seal cost` and for `work-item` and read each hit (executed, `git grep -n -i -E` over both, outside `seal/threads` and the meter's own scripts). `README.md:397` and `:421`, `README.ko.md:393` and `:417`, and `skills/implement/orchestration.md:172-177` and `:487` each hold with the read beside the post. `skills/code-review/orchestration.md:31-39` runs `--segments` before a fix pass and posts nothing. `docs/releasing/release-checklist.md:217` is the release's step, which round 1 left outside the finding, and `docs/running/measuring-a-run.md:118-132` is covered by `## Rule changes`, whose `to` texts state the posting command as "one command" for the post alone. The class is every wording of the run's command, an open set, so this list is a sample.

What matched: the acceptance searches, run again at the target. S1's `git grep -n -i -E 'after every crafter or proofer segment|segment that just' -- skills docs agents templates`, S3's `grep -n -F` of the history markers over `skills/verify/orchestration.md`, and S6's `git grep -n -F -e 'Measure the segment' -- ':!seal/threads'` each printed nothing (executed).

What matched: `changelog.md`. Items 1 to 3 and the first process row state the read and then the post, the posting command's exit codes, and why the line reaches the orchestrator through the read, and each holds against `skills/verify/orchestration.md:184-252` (read). The word count at `:14`, 1,460 for the section where it held 3,502, is what `sed -n '160,$p' skills/verify/orchestration.md | wc -w` prints (executed).

What matched: `gaps.md`. The range rewords row 3 in place to name the read beside the post, and removes no row (executed, `git diff --word-diff`).

What matched: `pr.md`. Each of its five quotes stands word for word in `frame/plan.md` at the place its coordinate names, with whitespace collapsed. Row A, which the fold rewrote, still ends with the quoted Verdict cell (executed, a substring check over the collapsed file). The tree's `bin/seal pr-body` composed the body into the round's scratch directory with exit 0 (executed).

What matched: `frame/questions.md` Q2, for this round. `python3 skills/code-review/scripts/chain_check.py --baseline 8f99b773e --root <the branch worktree> --worktree`, run over this record, exited 0 and printed no notice at a line of `frame/design.md` naming a test pin or a copy. Its two other lines say git carries no `trail/gate.md` and no `guarantee.md` yet, which the orchestrator's broad run and the sealer write after the rounds (executed).

Under one open log, the read prints the count already in the log and no line that names the log (the probe, executed). The section's "the log's state" (`skills/verify/orchestration.md:193`) reads as that count there, and each state that ends the post is named by the posting command's own line, so this is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD; the suite stays `unverified` in this round, which ran narrow modules alone | `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/gaps.md:8` | the orchestrator, by `seal gate --record` |
| The run's read and its post over this machine's transcripts and the open log, and the release's later run posting nothing; contract rule 6 withholds the post from this round | `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/gaps.md:7`, `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/gaps.md:9` | the orchestrator, by the tree's `bin/seal cost --work-item` when the run ends |

## Probes

| Command | Result |
|---|---|
| `PROBE_OUT=<scratch>/probe.out bin/test tests/skills/test_tmp_round2_read.py -q -p no:xdist -k probe`, in the clone, a subclass of `Test_work_item` running the S5 fixture through `main` without and then with `--post` under one open log, no history and a closed log | exit 0. Read: exit 0 in all three, the `Contract rule 6` line printed in all three, and the line `no open flow-measurement log was read (no history)` or `(closed)` printed under the last two. Post: one open, exit 0, terminal "posted the run's reading to #42", one comment; no history, exit 0, the no-history line, nothing posted; closed, exit 1, the closed-log line, nothing posted. The post's terminal held no `Contract rule 6` line in any of the three. The subclass also ran the 21 inherited cases, all green. The file was deleted after its one run |
| `bin/test tests/text/test_a_segment_feeds_the_flow_log.py -q -p no:xdist`, in the clone, with the fenced read removed from `skills/verify/orchestration.md` | exit 1; the one failure is `:437`'s assertion. The section was restored with `git checkout` |
| the same, with "The read without `--post` prints it" put back to "The reading prints it" | exit 1; the one failure is `:444`'s assertion. The section was restored with `git checkout` |
| `bin/test tests/text/test_a_segment_feeds_the_flow_log.py tests/text/test_the_chain_section_has_one_shape.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py -q`, in the clone | exit 0, 89 passed |
| `bin/test tests/skills/test_session_cost.py -q -k 'Test_work_item or Test_post or Test_emit'`, in the clone | exit 0, 46 passed |
| `bin/seal pr-body seal/threads/1794312072-the-cost-comment-is-posted-per-segment --body <scratch>/body.md`, in the clone | exit 0, the body written into the round's scratch directory |
