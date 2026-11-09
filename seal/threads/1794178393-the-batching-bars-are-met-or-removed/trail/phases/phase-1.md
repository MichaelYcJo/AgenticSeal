# Phase 1: 1794178393-the-batching-bars-are-met-or-removed

## What this phase found

**The frame holds against the tree.** The frame was read at `9c1cde63`, and `03cbad55` changed only the three frame files, so the build started from the tree the frame describes. Each coordinate `frame/plan.md` *Technical context* gives was opened before any edit: `SEGMENT_BARS` and `segment_kind` at `session_cost.py:2448-2478`, `report_grades` at `:2599` and its one call at `:2829`, the `kind` and `bar` loop at `:1876-1880`, the `token_totals` docstring, the plain advisory and the `>= 1.2` conjunct at `:2192-2232`, contract rule 10's last sentence, and step 1's clause in `skills/verify/orchestration.md`. Each stood where the frame put it. Every case `frame/design.md` *Removes* names stood in its module. The phase's narrow set passed at the base, 518 cases.

**Departure 1: a case the frame did not list pinned the batching line.** `tests/skills/test_session_cost.py#test_the_report_tells_its_two_turn_counts_apart` asserted the clause `2 calls over 2 turns that sent one, in this transcript alone`, which only the batching line printed. With the line gone it went red. The case also pins the token line's own label, which still prints, so the case stays: its batching assertion is removed and its docstring now says the plain reading prints neither the ratio nor its denominator. Judged against `frame/design.md` *Scope* item 5, which keeps a case whose docstring cites the advisory and rewrites it in place.

**Departure 2: two helpers *Removes* lists stay.** The *Removes* row for `tests/skills/test_session_cost.py` names `batched`, `graded_run`, `grade_lines`, `UNDER_PROOFER` and `SINGLES` as helpers only the removed cases read, and says two of those cases are rewritten as the `--segments` and `--json` cases. Both rewritten cases need a run with segment files of chosen turn sizes, which `batched` and `graded_run` build. So `batched` stays, `graded_run` stays under the name `spawned_run` because nothing grades its run, and `grade_lines`, `UNDER_PROOFER` and `SINGLES` go. The group comment above them is rewritten to say the page prints the ratio with no verdict.

**Comments outside the coordinates the frame listed were rewritten, in the class *Scope* items 1 and 5 name.** In `session_cost.py`, the `call_turns` comment in `analyse` said the key is returned "so the printed report can name it", and only the batching line printed it; it now says the key is returned beside the ratio in `--json`. The `report_spawns` comment on the delegated note cited "the cause #640 fixed twice for the tools-per-turn ratio", and both fixes were in the code this phase removes; that clause goes. In the module's negative-span case, the comment "Two calls in ONE message put tools per turn above the threshold that line also needs" went, because the `nothing obvious` line no longer needs a ratio. `test_either_route_prints_the_same_slices` lost `kind` and `bar` from its `labels` and the comment explaining them.

**The plain reading prints no tools-per-turn figure now.** The batching line was the plain reading's only place to print the ratio. The ratio stays in `--json` as `tools_per_turn` with `call_turns` beside it, and in the `--segments` table's `t/turn` column, as `frame/design.md` *Data & interfaces* states.

**Seen red at the base.** The three rewritten cases were written first and run against the unchanged script, in one command (`bin/test tests/skills/test_session_cost.py -q -p no:xdist -k ...`), and all three failed (executed):

| Case | Failing line at the base |
|---|---|
| `test_the_segments_page_prints_each_rows_ratio_and_grades_none` | `assert "Tools per turn against each kind's bar" not in flat_out`. The output also held `2 graded, 1 exempt, 0 ungraded.` and both `tools per turn against the` lines, so each of the case's three absence assertions had its text on the base page. |
| `test_a_json_segment_row_carries_the_ratio_and_no_grade` | `assert "kind" not in row` |
| `test_the_report_names_no_batching_when_every_turn_sent_one_call` | `assert "batching" not in out`, beside the printed line `batching 1.00 tools per turn` |

**Mutation runs, one per unit the phase changed in behaviour, all `red` (executed, after commit `abc732f2`).** Each restored the file from `seal mutate`'s own copy, and `git status` was clean afterwards.

| Unit | Break | Cases | Verdict |
|---|---|---|---|
| `report`'s `nothing obvious` gate | `if same <= 0:` back to `if same <= 0 and round(data["tools_per_turn"], 2) >= 1.2:` | `test_the_report_names_no_batching_when_every_turn_sent_one_call` | `red`, failing at `assert "nothing obvious" in out` |
| `report_segments` with no grade block | a `Tools per turn against each kind's bar` line printed before `report_breaches(segments)` | `test_the_segments_page_prints_each_rows_ratio_and_grades_none` | `red`, failing at the heading's absence assertion |
| `measure_segments`' rows with no grade key | a `bar` key set on every row before `return reading` | `test_a_json_segment_row_carries_the_ratio_and_no_grade` | `red`, failing at `assert "bar" not in row` |

**The page over a real run (executed).** `session_cost.py --segments` from this branch, given the transcript of session `c26b02b8` as its argument, exited 0. It printed the 19-row table with its `t/turn` column, followed directly by the token-column note and the comparability notes. No grade heading, no `graded, exempt, ungraded` count and no line naming a bar printed. Rows from the table:

```
  agent                             span  calls  t/turn    gap        tokens     context
  agentic:framer  1/2              18.3m     55    1.62    30s     8,288,372     308,242
  agentic:crafter                  16.5m    161    1.49     7s    21,644,370     267,280
  agentic:proofer                  12.0m     77    1.08     9s    15,883,211     313,021
  agentic:sealer                    6.1m     49    1.11     8s     6,622,505     198,298
```

**`frame/questions.md` Q1, measured.** `bin/test tests -q -k test_the_durations_file_prices_the_suite` passed at `abc732f2`, 1 case (executed). The cases this phase removed leave `.test_durations` within the share the case allows, so the file stays unedited, as Q1's default says. The row's Status cell is not this phase's to write.

**The plan's census returns one hit, in the file the frame leaves alone.** `git grep -n -E 'SEGMENT_BARS|report_grades|segment_kind|per-segment bar|framing bar|reviewing bar'` outside `seal/` and `docs/running/` returns only `.test_durations:5811`, the timing entry of the removed `test_the_protocol_names_a_bar_per_segment_kind` (executed). `frame/design.md` *Scope* leaves `.test_durations` unedited, and Q1's measurement above says it can stay that way.

**Until the settle, `docs/running/the-run.md` *The per-segment bars* states what the script no longer prints.** That is the gap `frame/plan.md` *Technical context* names. The section's `check:` line names `tests/text/test_the_handoff_before_round_one.py`, and since this phase no case in that module pins the section. The line goes with the section at the settle through `frame/design.md` *Rule changes*.

**The set at the phase boundary (executed).** The plan row's four modules passed alone, 492 cases, exit 0. The boundary run added the modules that read a path this phase changed: the contract's readers, `test_a_segment_feeds_the_flow_log` for `skills/verify/orchestration.md`, and the modules that read the work item's records, among them `test_a_cited_commit_outlives_the_squash`, `test_the_set_a_work_item_always_has`, `test_unverified_check` and `test_publish_release_note`. The list came from `git grep -l` over `tests/` for the changed paths' names. The 24 modules ran in one `bin/test ... -q` command with the records written and uncommitted, and 1657 cases passed, exit 0. `uvx ruff check` and `uvx ruff format --check` over the four changed Python files passed.
