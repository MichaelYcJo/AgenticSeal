# 1792449518-settle-squashes-specs-into-docs-in-place — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | cb2f9849 |

## What this phase was asked

One read and the index. The ceiling arm checks one row, `Document token
ceiling`, which replaces `Document line ceiling`. `Over the ceiling` goes with
the freeze. `Policy root`, the one new row, is read by every `docs` constant.
The index arm reads paths only, and `docs/README.md` arrives from the
record-layout table, which goes. `templates/config.md` states both rows and
the estimate once. The prose names each row without restating its value
(S12 to S14).

Changed after the spawn by the owner (2026-10-20, relayed by the
orchestrator): a document past the ceiling is a report, not a gate.
`fold-check` and `settle --apply` name it as one to split and exit 0, the
skill recommends the split rather than requiring it in the same pull
request, and this repository declares 25000, not the interim 37,178.

## What this phase found

- `hooks/config.py#policy_root` is the one reader of the row and holds the
  one default. `unverified_check.py#policy_root`, `fold_check.py#declared`
  and `settle.py` (through the reader) ask it. An empty value, an absolute
  path and a `..` part read as `docs`. `rule_changes.parse` takes the root
  as a required argument, so no second default exists.
- The estimate is `fold_check.py#tokens`, with `BYTES_PER_TOKEN` the one
  constant. `past_ceiling` and `past_ceiling_lines` are what `fold-check` and
  `settle --apply` both print.
- The index is read as table rows: each row after a table's header names
  its documents as backticked paths. A row naming none, a document no row
  names, and one named on two rows are refused at exit 1.
- The index found a defect on its first run here: `docs/the-pact.md` was
  missing from the record-layout table it replaces. `docs/README.md` has its
  row.
- `settle --apply` writes `<policy root>/README.md` when it creates the root,
  and after writing it prints the index rows owed and the documents past the
  ceiling under one heading, refusing nothing. A row `fold-check` cannot
  read is printed as a sentence, never as a traceback after the writes.
- In `unverified_check.py#settled`, the policy root and `rule_changes.py`
  load only where a spec is read, so a copy with no `hooks/` still judges a
  spec-less removal (`#test_a_copy_with_no_hooks_beside_it_prunes_nothing`
  found it).
- `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py` was red
  at HEAD before this phase: phase 1's `rule_changes.py` is named in the
  settle skill and was neither wrapped nor classified. It is now in
  `NO_WRAPPER`, as a module with no command line.
- What became of each case in `tests/test_a_document_has_room_for_the_next_fold.py`:

| Case | What became of it |
|---|---|
| `#test_every_document_in_docs_is_under_the_ceiling_or_frozen`, `#test_the_listed_document_still_holds_markers`, `#test_a_listed_document_at_its_frozen_count_passes`, `#test_a_fold_into_the_listed_document_is_named`, `#test_a_marker_removed_from_the_listed_document_is_named`, `#test_a_listed_document_back_under_the_ceiling_is_named`, `#test_a_listed_document_that_is_gone_is_named`, `#test_a_quoted_marker_is_not_counted`, `#test_a_marker_swapped_into_the_listed_document_is_named`, `#test_the_frozen_digest_is_the_listed_document_s_markers`, `#test_a_marker_removed_on_purpose_is_told_to_recompute_the_digest`, `#test_a_count_that_moved_is_told_to_recompute_the_digest_too`, `#test_an_over_the_ceiling_entry_is_read_with_its_digest`, `#test_a_listed_document_below_the_top_level_is_named_as_outside_it` | retired with the freeze |
| `#test_a_document_past_the_ceiling_outside_the_list_is_named`, `#test_a_document_at_the_ceiling_is_not_over_it`, `#test_the_command_names_a_document_over_the_ceiling_and_exits_1` | rewritten: `#test_a_document_past_the_ceiling_is_named_and_the_run_exits_0` |
| `#test_a_line_end_only_splitlines_sees_does_not_add_a_line` | retired: the ceiling counts no lines |
| `#test_the_record_layout_states_the_values_the_config_rows_hold`, `#test_the_prose_pin_fails_when_either_side_moves_alone`, `prose_disagreements` | removed: the prose names the rows and holds no value to pin |
| `#test_this_repository_passes_the_command_with_no_flags`, the row cases, the subdirectory, opted-out and no-root cases | rewritten to the token row, the policy root and the index line |
| `#test_settle_owns_the_placement_rule` | rewritten to "is recommended to be split" |
| added | `#test_the_estimate_is_utf8_bytes_halved_rounded_up`, the index cases, `#test_the_line_row_is_no_longer_read`, `#test_the_policy_root_row_moves_every_check_there`, `#test_the_policy_root_row_reads_as_docs_unless_it_names_a_directory_inside` |

- `tests/test_every_reader_ends_a_line_where_gfm_does.py#test_the_ceiling_and_the_fold_agree_about_that_marker`
  became `#test_the_shape_arm_reads_no_marker_there`: the count and the
  digest it compared are gone. Two cases in
  `tests/test_settle_applies_rule_changes_in_place.py` hold S14 and the
  report after `--apply`.
- Every new case was seen red against the tree before the code, and each
  unit added was mutated once with `mutation-check`: the rounding, the
  ceiling comparison, the three index refusals, the index excluding itself,
  `fold-check`'s policy root, the config guard, `settle`'s index write, its
  report, its parse root, and the predicate's root. Each went red.
- For phase 5: `docs/the-pact.md` opens "a work item that finds it wrong
  corrects it rather than working around it", the same sentence class as
  `docs/the-record-layout.md:278`, which `docs/README.md` now carries in the
  new model.
