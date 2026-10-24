# 1792449518-settle-squashes-specs-into-docs-in-place — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 33793508 |

## What this phase was asked

The settled predicate. It replaces `folded_items` and absorbs
`retired_by_rule`, reusing `rule_changes.py`'s replay with no reader or
constant of its own. `settle`, `unverified-check --baseline`, `chain-check`
and `tests/conftest.py#cutoff_item_is_traceable` ask it (S9 to S11). Its rule
is stated once, in `docs/the-record-layout.md` §*The fold, and what tells it
from a deletion*, and `docs/the-review-and-parity-arms.md` points there. The
`settle --retire` mentions phase 2 left in that document, in
`unverified_check.py`, `tests/conftest.py`, `tests/test_chain_check.py` and
`tests/test_unverified_rows_close.py` are rewritten.

## What this phase found

- The predicate is `unverified_check.py#settled(root, ref, directories,
  here=None)`. It returns the subset a settle removed. Each directory is
  judged at REF: it existed there, nothing in its record is open, and it
  either states no rule or its rules hold at HERE. A directory states no
  rule when it never wrote a `spec.md`, or its spec has no `## Rule changes`
  or one that says `nothing`.
- The replay counts texts rather than asking presence. Each text an applied
  operation names (`from`, `to`, and the section heading) must occur as often
  across `docs/` at HERE as in the replay. Counting removes the limit
  `spec.md` names: a text the base held twice no longer reads as unapplied
  when one copy goes. It also refuses a change whose old text was left beside
  the new. `overview.md` records the divergence.
- `rule_changes.pattern` (was `_pattern`) is the one matcher, so the
  predicate counts with the replay's own rule. `rule_changes.order` now reads
  any specs prefix, because the reader's fixtures keep work items under
  `specs/`, not `seal/specs/`.
- The callers hand the predicate only directories removed whole. A
  `routing.md` or `overview.md` deleted from a directory that stays is still a
  deletion. `chain-check` asks at HEAD, or the working tree under
  `--worktree`.
- Q5: `tests/conftest.py#cutoff_item_is_traceable` had no caller left since
  #923, so it was removed rather than re-pointed.
- `tests/test_every_reader_ends_a_line_where_gfm_does.py::test_every_splitlines_call_left_is_named_with_its_reason`
  was red at HEAD before this phase: phase 1's `rule_changes.order` reads
  `git log` output with `splitlines` and was not named. It is now named as git
  output.
- What became of each case:

| Case | What became of it |
|---|---|
| `test_unverified_rows_close.py#test_a_folded_work_item_is_not_read_as_this_branchs_deletion` | rewritten: `#test_a_settled_work_item_is_not_read_as_this_branchs_deletion` (S9) |
| `#test_an_unfolded_removal_beside_a_folded_one_still_fails` | rewritten: `#test_a_removal_whose_rule_docs_does_not_hold_still_fails` (S10) |
| `#test_the_folded_line_reads_as_a_sentence` | rewritten: `#test_the_settled_line_reads_as_a_sentence` |
| `#test_a_spec_at_the_base_is_still_a_deletion` | rewritten: `#test_a_spec_with_no_rule_changes_and_nothing_open_is_settled` (S11, Q2's answer turns its direction) |
| `#test_a_marker_quoted_in_prose_is_not_a_fold_record`, `#test_a_marker_inside_a_fenced_block_is_not_a_fold_record`, `#test_a_marker_inside_a_commented_out_draft_is_not_a_fold_record`, `#test_a_marker_below_the_top_level_of_docs_is_not_a_fold_record` | retired: the marker alone. The parametrized fence, comment and five-rounds families keep the live-line property |
| `#test_every_fence_shape_a_policy_document_can_carry`, `#test_every_comment_shape_a_policy_document_can_carry`, `#test_every_shape_five_review_rounds_named` | re-pointed from `folded_items` to `live_lines` and `FOLD_MARKER`, the reading `fold_check.py` uses |
| `#test_a_rule_retirement_is_not_this_branchs_deletion`, `#test_a_spec_dropped_on_the_far_side_of_a_merge_is_still_written`, `#test_the_baseline_arm_asks_the_one_predicate`, `#test_every_reader_of_a_retirement_calls_the_one_predicate` | re-pointed to `settled` and its output |
| `test_chain_check.py::TestRetired::test_a_declaration_a_fold_retired_is_not_one_this_branch_made` | rewritten: `#test_a_declaration_a_settle_removed_is_not_one_this_branch_made`; two cases added for a directory that stays and a rule only the working tree holds |
| `test_settle_reads_before_it_removes.py#test_the_predicate_asks_every_condition_itself`, `#test_the_predicate_is_what_settle_asks` | re-pointed to `settled`; a pre-model spec now passes, and an unapplied `add` is refused |
| `test_every_reader_ends_a_line_where_gfm_does.py#test_a_marker_after_a_separator_is_not_a_fold` | retired: `#test_the_ceiling_and_the_fold_agree_about_that_marker` asks the same text of `numbered_statements` |
| `#test_no_one_of_the_eight_makes_a_marker_a_line` | re-pointed to `fold_check.py#numbered_statements` |
| `test_settle_applies_rule_changes_in_place.py` | added: `#test_what_apply_removed_is_settled_for_the_readers`, `#test_a_rule_change_half_applied_is_not_settled`, `#test_merge_order_is_the_commit_that_adds_the_spec` |

- Every new or rewritten case was seen red: the rewritten ones against the
  tree before the predicate existed, and the rest by `mutation-check`, one
  command per unit. The units were the replay comparison (stubbed to accept,
  S10), the open-row condition, the spec-history condition, the pre-model
  acceptance, each named text, both callers' whole-directory filters,
  `chain-check`'s HEAD reading, `settle`'s base argument, `order`'s
  `spec.md` filter, `live_lines`'s flag and `numbered_statements`' line
  split. Each went red. `order`'s filter survived the first run and is what
  `#test_merge_order_is_the_commit_that_adds_the_spec` was written for.
