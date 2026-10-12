# 1791384152-a-reader-declares-its-input-class — round 3's corrections

Round 3 found nothing needing a fix and ended the run capped; these are its
four notes, each corrected in a commit of its own after it.

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| ⬜ 1 | answered | corrected at cbab19d1 — the `--map` refusal and `docs/the-reader-registry.md` name the `./<path>` spelling that reads the row in this tree |
| ⬜ 2 | answered | corrected at a5c543d0 — the row's path is normalised before it is read and resolved, so `kept.py/#k` and `kept.py/.#k` read `STANDING`; a case pins both and the `./` route |
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
