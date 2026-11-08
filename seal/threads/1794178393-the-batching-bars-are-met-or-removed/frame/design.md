# Design: #1440 the batching bars are met or removed

## Grounding

The tree as read at `9c1cde63`.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A mechanism stays only while what it caught outweighs what it costs, and a reading guessed from words is reported, never used to block. The bars have no catch on record. #640's own finding led to #696, and #696 did not move the reading (rows below). This clause decides between the ticket's two branches. |
| `docs/running/the-run.md` *The per-segment bars* (read) | This section states the bars that go: reviewing 1.8, framing 1.4, implementing judged on `repeats = 0`, verifying exempt. It also states the plain reading's advisory below 1.2. It already calls the bar "a lens ... never a refusal threshold", so removing the bars refuses nothing that refused before. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | The work's subject is a measuring script and the contract sentence that cites its bars. It is not the policy root's structure or text. So the policy text changes through `## Rule changes` for the settle, and the skills and code change in the pull request. |
| `skills/settle/rule-changes.md` *Rule changes* and `docs/README.md` (read) | Each `file:` below is picked from the index: `docs/running/the-run.md` and `docs/running/measuring-a-run.md`. No unsettled design names either file. `seal/threads/1794128303-the-plugin-ships-two-hooks-again/frame/design.md` holds `- nothing`, and the other two unsettled designs name neither file (executed, `grep -l` over `seal/threads/*/frame/design.md`). |
| `skills/agent-contract/SKILL.md` rule 10 (read) | The batching rule stays: "Open every file a coordinate names in one call" applies whether or not a bar grades it. Only the last sentence goes, which points at the bars. Rule 10's `check:` target `tests/text/test_a_moved_rule_leaves_its_definition.py` still pins rule 10 through `test_no_definition_carries_a_sections_own_sentences`, which is parametrized over every contract section (read, its `@pytest.mark.parametrize("number", sorted(SECTIONS))`), so the check line stays. |
| `docs/running/measuring-a-run.md` *A band flags a reading for judgment* (read) | This is the instrument that remains. A segment's calls, span, tokens and largest context are compared with earlier readings and weighed. Nothing else judges a reading, so a reading with no bar is still judged. |
| #51, observation 1 (read, `gh issue view 51`) | The bars came from corrected baselines on the early runs: "reviewing 1.3–2.0 ... Proposed: reviewing ≥1.8". The model those runs used is not recorded there. |
| #640 (read) | It named the confound: the drop in framer batching coincided both with the "no large parallel read burst" prompt sentence and with the move from Fable 5.1 to Opus 5.5. Its recommendation 3, separating model from instruction, was left as a question for the owner. The transcripts on disk now answer it (rows below). |
| PR #696 (read, `gh pr view 696`) | It closed #640. It added the framer's opening to `agents/framer.md` (*Bound each call, not the reading.*), the framing bar of 1.4, and the `--segments` grade. Its own first reading was Fable framers at 1.81–4.64. |
| #695 (read) | 0.17.0's Fable 5.1 framers read 1.81–4.64 "with no prohibition in the prompt and none in the definition". |
| #935 (read) | 0.22.0's framers at 2.7–3.7 were **Fable 5.1**. The log puts the ratio down to the measurement batches the owner asked each frame to run ("CI job timings, .test_durations, one mutation run, transcripts"), not to a request to batch reads. The ticket's reading, "Opus batched when the spawn asked (#935)", does not match #935's text. |
| #1424 (read) | The framer read 1.18 and the proofer 1.06, "so both read serially". The probe below shows the second half does not hold: Opus segments chain reads inside one shell call, and the ratio cannot see that. |
| Probe over every framer and proofer transcript on disk (executed) | `test_tmp_1794178393_shape.py` read each `subagents/*.meta.json` under this repository's Claude Code project directory, 1046 metas in all, and kept those whose `agentType` names a framer or a proofer. On three transcripts its call and turn counts equal `session_cost.py --json`'s: 75/58, 108/78 and 77/71. Results by the meta's `model` field: **Opus framers**: n=65, median 1.31 tools per turn, 23 of 65 at or above 1.4, a median of 48 turns. **Fable framers**: n=50, median 3.10, 49 of 50 at or above 1.4, a median of 17 turns. **Opus proofers**: n=67, median 1.12, 0 at or above 1.8. **Proofers with no model in the meta (older)**: n=125, median 1.14, 0 at or above 1.8. **Reads per turn**, counting each read command a Bash call chains (`cat`, `sed`, `grep`, `git`, ...) as one read: Opus framers median 2.60, Opus proofers median 2.71. In both kinds, 72% of Bash calls chain more than one read. |
| This release's framers, spawned with "Send independent reads together in one turn" (executed, `session_cost.py --json` on each transcript under this session's `subagents/`) | The six framers of `release: 0.36.0` read 1.10, 1.21, 1.27, 1.31, 1.35 and 1.43 tools per turn. One clears 1.4. The 1.31 is this frame, at 42 calls over 32 turns when it was read. All six were asked to batch in the spawn, and the frame definition and rule 10 ask the same. |
| The model in use (read, spawn prompt; `unverified` against a file, answerer: the repository owner) | The framer and the proofer run on Opus 5.5 by the owner's choice. Fable is used only for a new design question. This item does not change the model. |
| `routing.md` (read) | Automation, framer, crafter, through the review chain, open the pull request. |
| The ticket's comments (executed, `gh issue view 1440 --json comments`) | None. |

**What the grounds decide.** The cause is the model and not the instruction. Fable batches tool calls without being asked. Opus has not met the bars since #696 wrote the instruction into the framer's definition and rule 10, and asking in the spawn does not get it there either. Opus does batch its reads, but it chains them inside one Bash call, so tools per turn reads about 1.1 to 1.3 for segments that read about 2.6 to 2.7 files per turn. A bar on that ratio grades Opus against a shape it does not use. No proofer segment on disk has met 1.8, out of 192. So the bars, the lines that print them, and the plain reading's advisory go. The ratio stays as a printed number with no verdict.

## Scope

In:

1. `skills/verify/scripts/session_cost.py`: remove `SEGMENT_BARS`, `segment_kind` and `report_grades`, the call to `report_grades` in `report_segments`, and the loop in `measure_segments` that adds `kind` and `bar` to each segment row. Code comments and docstrings that cite the bars are rewritten in place. One is the `token_totals` docstring sentence on "the per-segment bars in `docs/running/the-run.md`".
2. The same script's plain reading: remove the batching advisory, the block under `round(data["tools_per_turn"], 2) < 1.2` and the comment above it. Remove the `>= 1.2` conjunct of the `nothing obvious` line, which then prints whenever no check was re-run. `tools_per_turn` stays in `--json` and in the `--segments` table's `t/turn` column.
3. `skills/agent-contract/SKILL.md` rule 10: remove the last sentence, "The bar each kind of segment is judged by is `docs/running/the-run.md` *The per-segment bars*, and no definition states a second copy of it." The rest of rule 10 and its check line stay.
4. `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, step 1: remove the clause "and, under the table, which rows sit under their kind's bar".
5. The test cases that pin the bars, the grade or the advisory are removed, and kept cases whose docstrings cite them are rewritten in place. `## Removes` lists them. One case per surface a person reads pins the new output: the plain reading, the `--segments` page and a `--json` segment row. Each is rewritten from a removed case and seen red at the base.
6. The policy text changes at the settle, through `## Rule changes`.

Out:

- `agents/framer.md` *Bound each call, not the reading.* stays. Its grounds are the no-progress watchdog and the range read of a large file (#478, #640's recommendation 1), not the bar, and `tests/text/test_the_handoff_before_round_one.py#test_the_framers_definition_carries_its_opening` holds it. #1443 edits that file, and this item does not.
- `skills/code-review/SKILL.md`'s probe batching line ("Batch the probe cases into one file and run it once") stays. It concerns probe files, not tools per turn.
- `agents/proofer.md` gains no batching step (`frame/plan.md` *Alternatives considered*).
- No reads-per-turn measure is added (the same table).
- The model the framer and the proofer run on is the owner's choice, and this item does not change it.
- `.test_durations` is not edited. Whether the removed cases leave it past its stale share is `frame/questions.md` Q1.
- The version move is assigned by the orchestrator.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A run's segments are read | Given a run transcript with framer, proofer and crafter segments, when `session_cost.py --segments` runs, then the table prints with its `t/turn` column. No "Tools per turn against each kind's bar" block prints, and no "graded, exempt, ungraded" count. The exit code is 0. | The rewritten `--segments` case, seen red at the base. A crafter probe over one transcript on disk, its output quoted in the phase record. |
| A segment row is read as JSON | Given the same run, when `--segments --json` runs, then each row carries `numbers.tools_per_turn` and no `kind` or `bar` key. | The rewritten JSON case, seen red at the base. `test_either_route_prints_the_same_slices` with `kind` and `bar` gone from its `labels`. |
| A single transcript is read plainly | Given a transcript where every turn sent one call and no check was re-run, when `session_cost.py <transcript>` runs, then no `batching` line prints and `nothing obvious` does. | The rewritten case, `test_the_report_names_no_batching_when_every_turn_sent_one_call`, seen red at the base. |
| An agent reads rule 10 | Given a spawned agent, when it reads contract rule 10, then the rule asks it to batch independent reads and points it at no bar. | Read at review. `tests/text/test_a_moved_rule_leaves_its_definition.py` stays green. |
| The settle reads this design | Given this design after the release, when the settle reads `## Rule changes`, then it removes the-run.md's section and the measuring-a-run.md sentence that cites it. | `chain_check.py` reads the block through `skills/settle/scripts/rule_changes.py` at review and at the pull request. |

## Data & interfaces

- The `--json` segment rows lose two keys, `kind` and `bar`. No reader in the tree uses them (executed: `git grep -n -E '\["(kind|bar)"\]'` outside `tests/` and `seal/` finds only `session_cost.py`'s own grade and the spawn-cycle `kind`, which is another field). #1439 posts readings from the same script: its frame should not read either key.
- The `--segments` page loses the block under the table that `report_grades` printed.
- The plain reading loses the `batching` line, and its `nothing obvious` line depends on repeats alone.

## Rule changes

- remove
  file: docs/running/the-run.md
  section: The per-segment bars
- remove
  file: docs/running/measuring-a-run.md
  section: Measuring a run
  from: `docs/running/the-run.md` *The per-segment bars* holds the bar each kind of segment is judged against, because it is part of what a handoff carries. This document is about the measurement itself.

## Removes

The table holds 10 rows. The build removes what the first 9 name, and the settle removes what the last names.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the per-kind bars and the grade that prints them | `skills/verify/scripts/session_cost.py#SEGMENT_BARS`, `#segment_kind`, `#report_grades`, and the `report_grades(rows)` call in `#report_segments` | nothing owns them. No release since #696 shows a bar moving a reading (*Grounding*). A reading is judged by `docs/running/measuring-a-run.md` *A band flags a reading for judgment*. |
| each segment row's `kind` and `bar` | `skills/verify/scripts/session_cost.py#measure_segments`, the `row.update(segment_kind(row["agent"]))` loop | only the grade read them, and it goes |
| the plain reading's batching advisory and the `nothing obvious` line's ratio conjunct | `skills/verify/scripts/session_cost.py#report`, the `round(data["tools_per_turn"], 2) < 1.2` block and `round(data["tools_per_turn"], 2) >= 1.2` | nothing. Its printed claim, "independent calls are going out one at a time", is false for Opus segments, where 72% of Bash calls chain reads (*Grounding*), and since #197 it has read 1.00 on every implementer. |
| the sentence citing the bars in a docstring | `skills/verify/scripts/session_cost.py#token_totals`, "the per-segment bars in `docs/running/the-run.md` are calibrated against that ratio, and widening it would move a published threshold without saying so" | rewritten in place to say why the two turn counters differ, without the bar |
| contract rule 10's pointer to the bars | `skills/agent-contract/SKILL.md` *10 Batch independent reads and runs*, its last sentence | nothing. The rule's batching guidance stays. |
| the step's mention of the grade | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, step 1, "and, under the table, which rows sit under their kind's bar" | nothing |
| the pins of the bars in the handoff module | `tests/text/test_the_handoff_before_round_one.py#test_the_contract_cites_the_per_segment_bars`, `#test_the_protocol_names_a_bar_per_segment_kind`, `#bars_section`, `#test_the_tying_paragraph_says_which_reading_applies_the_bars`, `#test_the_bars_section_cites_the_run_level_tables_owner`, `#OWNER_PATH`, `#test_the_scripts_bars_are_the_protocols`, `#test_the_advisory_and_the_tying_paragraph_name_one_value` | nothing. What they pin goes in the build (the script and contract halves) or at the settle (the-run.md's section). `PROTOCOL` stays, because other cases of the module read it. |
| the pin against a figure in a definition | `tests/text/test_a_moved_rule_leaves_its_definition.py#TOOLS_PER_TURN`, `#figures`, `#test_no_definition_states_a_tools_per_turn_figure`, `#test_a_figure_in_any_spelling_is_caught` | nothing. With no bar there is no first copy for a definition to repeat. |
| the grade and advisory cases of the script's module | `tests/skills/test_session_cost.py`: the cases from `test_a_proofer_row_under_its_bar_is_named_with_the_bar` through `test_every_json_row_carries_its_kind_and_bar`, `test_the_report_stops_claiming_one_at_a_time_above_a_ratio_of_one`, `test_a_plain_reading_printed_at_the_advisory_is_not_flagged`, and the helpers only they read, `grade_lines`, `UNDER_PROOFER` and `SINGLES`. Two of the cases are rewritten as the `--segments` and `--json` new-output cases (*Scope* item 5), and the rest go. The helpers `batched` and `graded_run`, renamed `spawned_run`, stay, because the two rewritten cases read them. The plain-reading case is rewritten in place as `test_the_report_names_no_batching_when_every_turn_sent_one_call`. `test_refuses_nothing_obvious_beside_a_repeat` keeps its assertions, and its docstring loses "clears the batching advisory". `test_the_token_turns_and_tools_per_turn_count_different_things` keeps its assertions, and its docstring loses "the per-segment bars in `docs/running/the-run.md`". |
| the policy section and its citation | `docs/running/the-run.md` *The per-segment bars*; `docs/running/measuring-a-run.md` *Measuring a run*, the sentence citing it | removed at the settle by `## Rule changes` |

This work adds no mechanism. It removes one: the grade, the advisory and the pins that held them.

Framed 2026-11-09 by framer, before the build.
