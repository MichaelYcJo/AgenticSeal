# 1792449518-settle-squashes-specs-into-docs-in-place — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 1c01de0c |

## What this phase was asked

`settle --apply`: write the policy root in place in merge order, one spec at
a time, all or nothing (S1–S3, S5–S7), and remove applied directories whole
and spec-less released ones with nothing open. Remove `--retire` and
`--retire-process` with their tests. Rewrite `docs/release-checklist.md`
§2b, `docs/the-review-record.md:160`, `seal/README.md` with
`templates/seal-README.md`, and both READMEs' cheat-sheet rows. Prose short,
the rule once, no narrative of what changed (the owner's direction).

## What this phase found

- `--apply` re-reads its candidates from the tree, as `--retire` did, and
  takes only *released*, `ref` and the base from `survey`. It writes every
  document before it removes any directory.
- A spec's text is read at `--released-at`, never from disk, so an edit
  made after the release is not what applies.
- **Merge order missed a moved directory.** `git log --diff-filter=A` reads a
  moved `spec.md` as a rename, so a renamed work item had no adding commit
  and was held. `rule_changes.order` passes `--no-renames`. A case found it
  red before the fix.
- A spec with no `## Rule changes` is kept and named, and that is not a
  refusal: exit 0. Otherwise every `settle --apply` in this repository
  would exit 1 until #941 settles the backlog.
- `settle.py` dropped its marker arm, so it no longer calls
  `unverified_check.py#folded_items`. Phase 3 owns that function and its
  other callers.
- What became of each case:

| Case | What became of it |
|---|---|
| `test_settle_reads_before_it_removes.py#test_the_report_lists_each_released_unfolded_work_item` | rewritten: `#test_a_spec_with_no_rule_changes_is_listed_and_kept` |
| `#test_a_recorded_fold_leaves_the_foldable_list` | retired: it was about the marker alone |
| `#test_retire_removes_only_what_docs_records` | rewritten: `#test_apply_removes_only_what_it_applied`; `docs/the-record-layout.md` cites it |
| `#test_retire_leaves_a_team_specs_of_the_same_name_on_disk` | rewritten: `#test_apply_leaves_a_team_specs_of_the_same_name_on_disk` |
| `#test_an_interrupted_run_resumes` | retired: the marker was what it resumed from |
| `#test_the_report_lists_what_a_retirement_would_take` | rewritten: `#test_the_report_lists_what_an_apply_would_remove`. Its open-row half went, because neither arm removes a directory with an open row |
| `#test_a_marker_quoted_in_prose_is_not_a_fold_record` | retired: the marker alone |
| `#test_the_retirement_refuses_a_survey_with_no_base` | rewritten: `#test_the_apply_refuses_a_survey_with_no_base` |
| `#test_the_skill_says_who_judges_and_who_reads` | rewritten: `#test_the_skill_says_the_spec_judges_and_the_command_applies` |
| `#test_the_skill_says_a_fold_is_not_a_work_item_and_owes_no_range_row` | rewritten: `#test_the_skill_says_a_settle_is_not_a_work_item_and_owes_no_range_row` |
| `#test_the_skill_says_the_retirement_is_the_second_half_of_the_fold` | rewritten: `#test_the_skill_says_the_directory_goes_with_the_rule_it_applied` |
| `#test_the_skill_states_the_destination_rule` | rewritten: `#test_the_skill_states_how_the_changes_land` |
| `#test_the_seal_readme_says_the_step_exists`, `#test_the_release_checklist_carries_the_by_hand_step`, `#test_both_cheat_sheets_carry_the_command`, `#test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule`, `#test_the_documents_say_the_closure_has_to_reach_the_base` | rewritten to the new text; each was seen red against today's text before the prose changed |
| `#test_a_complete_retirement_is_not_reported_as_nothing_ever_folded`, `#test_a_marked_item_still_on_disk_is_not_the_fold_being_complete`, `#test_the_fold_is_complete_still_prints_when_it_is` | retired: the marker alone |
| `#test_an_untouched_tree_still_says_nothing_has_been_folded` | rewritten: `#test_an_apply_with_nothing_to_do_is_no_refusal` (exit 0, not 1) |
| `#test_a_settled_root_is_green_and_says_so` | rewritten to `--apply` and "A complete settle ends here" |
| `tests/test_settle_retires_the_process_record.py`, `tests/test_a_process_record_drop_passes_the_readers.py` | retired whole with the arm. Their live property, a released directory removed whole passing the readers, is phase 3's S9 |
| `tests/test_a_folded_statement_names_what_enforces_it.py#test_settle_owns_the_shape_rule`, `tests/test_a_document_has_room_for_the_next_fold.py#test_settle_owns_the_placement_rule`, `tests/test_a_reference_root_is_read_and_never_taken.py` (its settle row) | rewritten to the new skill sections; each seen red by mutating the sentence it pins |
| `tests/test_unverified_rows_close.py#test_the_shipped_skill_copied_into_docs_records_no_fold` | retired: its premise was that the skill shows a marker, and the skill no longer does. `## Removes` did not name it; `overview.md` records that |

- Left for phase 3, because each stands in a file phase 3 rewrites:
  `docs/the-review-and-parity-arms.md:133` and `:148` (`settle --retire`);
  the comments and docstrings that name `settle --retire` in
  `skills/verify/scripts/unverified_check.py`, `tests/conftest.py`,
  `tests/test_chain_check.py` and `tests/test_unverified_rows_close.py`.
  `docs/one-root-by-lifetime.md:690` and its `.ko.md` row stand in a dated
  section, a record of a moment, and phase 5 owns that document.
