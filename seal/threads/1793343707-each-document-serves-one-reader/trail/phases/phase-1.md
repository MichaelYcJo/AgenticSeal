# Phase 1: 1793343707-each-document-serves-one-reader

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 78848617 |

## What this phase was asked

Row 1 of `frame/plan.md` *Phases*, and nothing from rows 2 to 6. One
instruction was the spawn's own. The first phase writes this work item's
`gaps.md`, because `frame/design.md` *Scope* item 3 gives that file's
trigger to the first phase's close. The template that sets its new shape is
reshaped only in phase 2, so the file was to be written from today's
`templates/records/sdd-gaps.md`. The reason is
`tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which requires a `gaps.md` once a frame exists. Phase 2 rewrites the file to
the new template, as its row says.

## What this phase found

**The frame held at every coordinate this row names.** At `5183dd26`,
`templates/records/sdd-design.md` ended with `## Open questions` and its
placeholder, just above the mark. `templates/records/sdd-plan.md` held
`## Summary` at line 5. `agents/framer.md` held *`questions.md` is the
residue, not a collection*, and every rule in it ended in a `check:` line.
The design's *Removes* says nothing in code reads either section. The census
agrees. After the change, `git grep -n "## Open questions\|## Summary"`
outside `seal/threads/` finds six lines, all in test fixtures, and none of
them reads a template:

- `tests/conftest.py:1721` and `tests/skills/test_rule_changes.py:140`,
  `:181`, `:234` and `:240` write `## Open questions` as the section after
  `## Rule changes`. They test that the reader finds where that section
  ends, and any heading would do. They were left as they are.
- `tests/skills/test_pr_body.py:31` writes `## Summary` in a plan fixture.
  Row 2's *Verified by* cell names `tests/skills/test_pr_body.py`, and phase
  2 writes the fixtures in the new shapes.

**The template removals got no new case.** A removed section adds no
behaviour. The proof is that every reader of the two templates still passes:
`tests/skills/test_chain_check.py#template_section`, which splits the design
template at `## Rule changes` and `## Removes`; the spec-template cases of
`tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`, which hold
`## Removes` above the mark and the mark as the last line;
`tests/behaviour/test_the_set_a_work_item_always_has.py`, which reads the
plan template's Status column and approval line; and
`tests/text/test_a_record_carries_no_comment.py`. A case refusing a section's
return would be a new mechanism with nothing on record that it would catch
(`skills/core/SKILL.md` *The rule a mechanism is kept against*).

**The three framer changes are each held by a case in the framer group of
`tests/behaviour/test_waiver_decided_at_start.py`, and each case was seen
red first.** `test_questions_md_is_the_residue_and_every_row_says_why`
gained an assertion that the head points at the row holding the grounds.
`test_a_delivers_cell_cites_the_scope_items_by_number` and
`test_a_mark_is_not_the_answer_to_a_blocked_step` are new. The last also
holds that the rule's paragraph ends in its `check:` line. The three were run
against the definition at `5183dd26` and failed, exit 1, `3 failed`. After
the edits they passed, exit 0 (executed). `seal layout --pairs` over the
module found 0 pairs (executed). The cases pin phrases, which is the form
every other case in that group takes. #1146 cut such pins from the contract's
module, and the group here was left as it stands.

**The Delivers sentence stands in the Job paragraph, not in a rule.** That
paragraph is where the definition says what `frame/plan.md` holds, so the
sentence describes the file there. Job paragraphs carry no `check:` line.
`test_a_delivers_cell_cites_the_scope_items_by_number` holds it.

**`seal mutate` turned all four mutants red** (executed, one command at
`74d8a992`, exit 0). The four were: the head's pointer replaced by
"grounds"; "cites by number" replaced by "restates"; the new rule's bold lead
removed; and "names in `## Removes`" replaced by "says". The mark rule's
mutant ran against a phrase list that also pins "never by a new mark" and
the core citation.

**The first phase-boundary run found one defect, and one fix closed it.**
The Delivers edit left `agents/framer.md:37` at 132 columns against
`tests/behaviour/test_docs_line_wrap.py`'s limit of 88: `1 failed, 3339
passed`. `78848617` rewraps that paragraph without changing a word. The set
was then run again as one command over 50 modules: the row's seven, the
modules that glob `agents/` or name `agents/framer.md`,
`templates/records/sdd-design.md` or `sdd-plan.md`, those that glob
`templates/records/`, those that read the tree's `seal/threads/`, and those
that read `tests/`. It passed: exit 0, `3340 passed, 11 skipped` (executed).
The six framer evals' `shape-marks-the-spec` graders read the mark, which
this phase did not touch (read).

**`gaps.md` was written from today's template, as the spawn asked.** It has
no `## Scope confirmation`, because the work is on the ladder's top rung. Its
`## Not verified` holds one row, the broad gate, answered by the
orchestrator. `seal unverified` reads it as `1 open · 0 closed`, exit 0
(executed). The rows for the body's rendering and for the behaviour suite
are phase 6's, by its row.
