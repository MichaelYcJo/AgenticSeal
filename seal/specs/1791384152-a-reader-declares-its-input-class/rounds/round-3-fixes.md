# 1791384152-a-reader-declares-its-input-class — round 3's corrections

Round 3 found nothing needing a fix and ended the run capped; these are its
four notes, each corrected in a commit of its own after it.

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| ⬜ 1 | answered | corrected at cbab19d1 — the `--map` refusal and `docs/the-reader-registry.md` name the `./<path>` spelling that reads the row in this tree |
| ⬜ 2 | answered | corrected at 5552412a — a row whose path ends in `/` or `/.`, or carries an empty or `.` segment after its first, is refused rather than read as gone; a case pins `kept.py/#k`, `kept.py/.#k`, an empty segment and the `./` route. The first correction, a5c543d0, folded the path with `normpath` |
| ⬜ 3 | answered | corrected at 3eafec0c — the `Enforced by:` line names `test_a_path_through_dot_dot_is_refused_never_read_as_gone`; line 123's re-wrap rode cbab19d1 |
| ⬜ 4 | answered | corrected at dcde8e56 — `removal_findings` takes no `default_repo`, and `file_claims` hands it none |

## Fix surface

The range is cbab19d1..dcde8e56.

- **Contract changes:** `skills/evidence-check/scripts/evidence_check.py#removal_findings` loses its `default_repo` parameter; its one caller, `file_claims`, moves with it.
- **New units:** `tests/test_a_record_states_what_the_tree_has.py#test_a_path_spelled_another_way_is_refused_never_read_as_gone`, under the name the broad gate's correction gave it. No shipped unit is new.

⬜ 2's first correction folded the path with `os.path.normpath`, which the
broad gate refused below; the path is now refused instead of folded.

## Seen red

Each through `bin/mutation-check`, every verdict `red`: the normalisation
removed (the trailing-`/` rows), and the refusal's `./` dropped (the map
case's pinned text).

## The broad gate's correction

The broad gate at 914e49d2 failed two suite guards on ⬜ 1/⬜ 2's corrections;
corrected at 5552412a and fd7f515a.

- `tests/test_the_printed_ledger_name_is_the_file_that_was_read.py` refused
  a5c543d0's `os.path.normpath(rel)`: a lexical fold names another file
  through a symlink (#163). 5552412a refuses the spelling instead, and the
  document's and the changelog's refusal lists say so.
- `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py`'s census of
  `resolve_unit` callers did not name `removal_findings`. The caller is
  phase 3's, not round 3's: the census was not grown with it, and the build
  never ran that module. `removal_findings` reads the refusal from
  `resolve_unit` and derives none, so fd7f515a grows the census by it and
  holds it to the `.refused` check the other callers meet; `mutation-check`
  of `removal_findings` deriving the refusal through `unbounded` was red.
