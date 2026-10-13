# 1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 1db4e4bb |
| Ran by | unknown — the spawn prompt named no agent or model for this segment; the orchestrator fills this row |

## What this phase was asked

Rewrite the pins first: the three cases in `tests/test_waiver_decided_at_start.py`
assert the one spelling from `spec.md` §*Data & interfaces* and refuse
`two questions in ONE `AskUserQuestion` call` as a stale copy, and
`tests/test_review_axes.py#test_implement_and_the_preset_block_do_not_drift`
pairs the documents on the new phrase; run them red against the old text.
Then rewrite `skills/implement/orchestration.md` (the two headings, the file
header, the section opening, the ceiling paragraph, the diagram, the
multi-repository sentence, the act table rows), `templates/claude-md-block.md`
and the regenerated `CLAUDE.md`, the pointers in `skills/implement/SKILL.md`
and `agents/framer.md`, and the heading reference in
`docs/worktree-guard-spec.md`. Keep `### Question 1 — single-select` and its
table, and the literal `in one call`.

## What this phase found

**Seen red.** With the pins rewritten and the documents untouched,
`bin/test tests/test_waiver_decided_at_start.py tests/test_review_axes.py -q
-p no:xdist` exited 1, `4 failed, 33 passed`:

```
FAILED tests/test_waiver_decided_at_start.py::test_the_skill_asks_the_whole_question_in_the_first_batch
FAILED tests/test_waiver_decided_at_start.py::test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis
FAILED tests/test_waiver_decided_at_start.py::test_the_preset_block_carries_it_too
FAILED tests/test_review_axes.py::test_implement_and_the_preset_block_do_not_drift
E   AssertionError: templates/claude-md-block.md still asks the old question, ...
```

(That run used the frame's sixteen-word sentence; the spelling was shortened
afterwards, below, and the pins and documents moved together.)

**The frame's sentence and heading did not fit two checks the plan's command
set does not run.** Every module that reads one of the edited files was run
once (60 modules, `6703 passed, 8 failed`). Two failures were this phase's:

- `tests/test_no_passage_is_pasted_into_a_second_file.py` refused the
  sixteen-word sentence shared by the orchestrator's section and the block
  template. The written spelling is fourteen words, under its fifteen-word
  window: *Ask question 1 alone; the boxes in a second call only under
  `per axis`.*
- `tests/test_docs_line_wrap.py` refused the 99-column heading. The written
  heading is `## Orchestrator: how the work is routed — question 1 alone,
  boxes if per axis, one file`, 87 columns.

A third was the phase-1 sentence naming `0.21.1` in
`docs/worktree-guard-spec.md`, refused by
`tests/test_release_hygiene.py#test_no_loaded_file_names_a_version_at_or_above_the_running_one`;
it now names #911. One more was the missing `overview.md`, opened here. The
other three were cases over the 90-second ceiling under that 60-module run
(`test_a_corrected_sentence_survives_elsewhere.py` twice,
`test_settle_reads_before_it_removes.py` once), re-run alone afterwards.
After the fixes the plan's set with those three readers added exited 0,
`363 passed`, and `claude_block.py --check` exited 0.

**For phase 3: the heading move breaks five released families, not two
re-read rows.** Rows citing
`skills/implement/orchestration.md#"## Orchestrator: how the work is routed — two questions, one call, one file"`
(directly, or as the parent of `### A work item that commits in more than one repository`)
root at 0.12.0 (*No agent this plugin spawns has `AskUserQuestion`* and
*one spelling*), 0.15.5 A2, 0.19.0 `Corrected · P4`, and 0.21.0 S10, with
their `Re-read ·` rows in 0.18.1, 0.19.0 and 0.21.0. A moved anchor is
re-pointed by a `Corrected ·` row, not cleared by a re-read
(`docs/the-evidence-ledger.md` §*A released row is read again in the
branch's fragment*). Phase 1's edit to `docs/worktree-guard-spec.md`
§*Creation consent* also drifted three rows (0.20.0 once, 0.21.0 twice),
which are re-reads.
