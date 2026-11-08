# Implementation Plan: #1440 the batching bars are met or removed

## Technical context

The tree as read at `9c1cde63`.

The code this removes, by its coordinates at that commit:

- `skills/verify/scripts/session_cost.py:2448-2478`: the comment block, `SEGMENT_BARS` and `segment_kind`.
- `skills/verify/scripts/session_cost.py:2599-2665`: `report_grades`, called once at `:2829` inside `report_segments`.
- `skills/verify/scripts/session_cost.py:1876-1880`: the loop in `measure_segments` that adds `kind` and `bar` to every row, in both the walked branch and the own-file branch.
- `skills/verify/scripts/session_cost.py:1884-1893`: the `token_totals` docstring, which justifies its two turn counters by the bars.
- `skills/verify/scripts/session_cost.py:2192-2232`: the plain reading's advisory and the `nothing obvious` line's `>= 1.2` conjunct. The `repeats` lines above them stay.
- `skills/agent-contract/SKILL.md:116-118`: rule 10's last sentence.
- `skills/verify/orchestration.md:243-245`: step 1's clause about the grade.
- The test coordinates are in `frame/design.md` *Removes*.

Constraints:

- The `t/turn` column and `numbers.tools_per_turn` stay, so readings posted since 0.9.4 remain comparable. Only verdicts go.
- `session_cost.py` runs from the installed plugin in other repositories. The removal reaches them at the next release and needs nothing from them.
- The policy text in `docs/running/` stays until the settle (`frame/design.md` *Rule changes*). Between the merge and the settle, `docs/running/the-run.md` *The per-segment bars* states bars the script no longer prints. The policy in force is the baseline plus the unsettled designs' rule changes (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*), so that gap is the layout working as designed. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` excuses a citation of a section a pending `remove` with no `from` takes out, which covers the measuring-a-run.md citation until then.

Failure scenario of the chosen approach, six months on: agents stop batching for a new reason, for example a prompt that asks for one read per call. No printed verdict flags it. It shows only as calls, turns and tokens rising against the last reading, and it is caught only where someone reads the per-segment table against the previous one, as `docs/running/measuring-a-run.md` *A band flags a reading for judgment* asks. That is the instrument that judged every reading in this item's *Grounding*. The bars did not judge any of them.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the bars and add a structural lever: a proofer definition step that opens every file the round names in one call, plus spawn prompts asking for batches | #696 did this for the framer: the opening in `agents/framer.md` and rule 10's "Open every file a coordinate names in one call". 65 Opus framers on disk read a median of 1.31 after it. This release's six framers were asked in the spawn and read 1.10–1.43 (`frame/design.md` *Grounding*). A proofer line adds text every proofer spawn pays for, and the reading stays where it is. The ratio also cannot see the batching Opus does, which is chained reads in one Bash call. | rejected. The premise that keeps the structure, "Opus meets the bar when the instruction asks", was checked against the transcripts on disk and does not hold. |
| Keep the bars and lower them to where Opus reads, framer about 1.2 and proofer about 1.1 | A bar set at the current median flags half the segments on noise and catches no defect. It is the kind of numeric threshold the owner rejects, and the ratio is still blind to chained reads. | rejected |
| Replace tools per turn with a reads-per-turn measure that counts each read a Bash call chains | The count is guessed from command words. `skills/core/SKILL.md` *The rule a mechanism is kept against* says such a reading is reported, never used to judge. It would be a new mechanism with no catch on record. Turns times context, which is what cost tracks, is already printed per segment: calls, span, tokens and largest context. | rejected. The probe that counted reads per turn for this frame was deleted after its one run. |
| Move the framer and the proofer to Fable 5.1 | This is the one lever the data shows moving the ratio and the turn count: Fable framers have a median of 3.10 tools per turn and 17 turns, against Opus's 1.31 and 48. It overturns the owner's standing model choice, and per-token cost is not measured here. There are no Fable proofer segments on disk to read. | rejected for this item. The model is the owner's choice, made before this item. |
| Remove the proofer bar and keep the framer bar, which 23 of 65 Opus framers meet | The bar that remains is met by about a third of the segments, through a ratio that cannot see chained reads, and nobody acts on it. Two segment kinds under one measure would follow two policies. | rejected |
| Remove the bars and keep the plain reading's advisory below 1.2 | The advisory prints "independent calls are going out one at a time", which is false for Opus segments where 72% of Bash calls chain reads. Since #197 it has read 1.00 on every implementer. Its one policy sentence sits inside the section the rule changes remove, so keeping it would need a new home in the policy. | rejected |
| Remove the bars, the grade, the plain advisory and every pin of them, and keep the ratio as a number with no verdict | The six-month failure is in *Technical context*. | chosen |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2, 3, 4 and 5 of `frame/design.md`, and each *Removes* row the build owns | `bin/test tests/skills/test_session_cost.py tests/text/test_the_handoff_before_round_one.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q` green. Each of the three rewritten new-output cases seen red at `9c1cde63`. One run of `session_cost.py --segments` over a run transcript on disk shows the table with no grade block, quoted in the phase record. `bin/test tests -q -k test_the_durations_file_prices_the_suite` answers `frame/questions.md` Q1. `git grep -n -E 'SEGMENT_BARS\|report_grades\|segment_kind\|per-segment bar\|framing bar\|reviewing bar'` outside `seal/` and `docs/running/` returns only `.test_durations`, the file this work leaves to its census. | abc732f2 |

One phase, because every removal has to land together. Taking `SEGMENT_BARS` out turns `test_the_scripts_bars_are_the_protocols` red. Taking the advisory out turns `test_the_advisory_and_the_tying_paragraph_name_one_value` red. Those cases sit in the module that also pins the contract sentence.

**Where this meets the release's other work items.** These overlaps were read in the tree. The sibling frames were still skeletons when this frame was written.

- #1439 shares `skills/verify/scripts/session_cost.py` and `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*. This item edits the grade, the row keys, the plain advisory and step 1's one clause. #1439's posting, `--post` and the settle or release step, sits in other functions. **#1440 should merge before #1439.** Then #1439's posted readings and its tests are built against a page without the grade block, and against rows without `kind` or `bar`. The ticket's other branch, "meet their bars on the readings #1439 posts", is not taken, so this item does not wait on #1439.
- #1443 edits `agents/framer.md`. This item does not, so there is no overlap.
- #1444 is about `.test_durations`. This item removes test cases and leaves the file to its census (`frame/questions.md` Q1).
- #1441 and #1442 edit no file this item edits (their file lists are the orchestrator's guess, `unverified`).

## Operational impact

- Any reader outside this repository that reads `kind` or `bar` from a `session_cost.py --segments --json` row stops finding them. No reader in the tree does (`frame/design.md` *Data & interfaces*).
- The plain `session_cost.py <transcript>` reading prints `nothing obvious` on runs where it used to print the `batching` line. The numbers do not move.
- No migration, environment variable or dependency. This pull request does not move the version.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-09 | Phase 1's hand-back named six frame statements; the orchestrator read the three frame files whole against HEAD and rewrote four: the plain-reading case's name in *User scenarios* and in the `test_session_cost.py` *Removes* row, the helpers that row says leave (`batched` and `graded_run`, renamed `spawned_run`, stay), the census in phase 1's Verified-by cell, and `frame/questions.md` Q1's Status. The two *Grounding* rows it named, the ticket's comments and the reading of #935, are not folded. | Each of the four was false at HEAD (`trail/phases/phase-1.md`); *Grounding* is dated to `9c1cde63`, and both rows were true of the ticket the framer read. | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-09 | The pull request's title takes `chore:`, and the kind that came closest is `fix:`. | The work removes a verdict and two JSON keys that no party acted on and adds no behaviour; it repairs nothing that read wrong in the code, since the bars were printed as designed. | `skills/commit-pr-convention/SKILL.md` *Commit messages* |
| 2026-11-09 | Round 1's finding 4 adds a removal the frame did not name, so the orchestrator folded it before the fix pass: *Removes* gains the verifying-row pin of `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py`, and its count line reads 11 rows. Findings 1 to 3 change no frame statement and go to the fix pass. | The settle's `remove` of *The per-segment bars* turns that case red, and no other document states a verifying bar for it to follow (`trail/rounds/round-1.md`). | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
