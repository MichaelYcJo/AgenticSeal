# 1791384152-a-reader-declares-its-input-class — round 2's fix pass

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 🟡 1 | fixed | 5dfefd3b |
| ⬜ 2 | fixed | 5dfefd3b |
| ⬜ 3 | answered | corrected at 6c5d4529 |
| ⬜ 4 | fixed | 6c5d4529 |
| ⬜ 5 | answered | corrected at 6c5d4529 |
| ⬜ 6 | fixed | 6c5d4529 |

## What the fix range changes

The range is 5dfefd3b..6c5d4529.

- **Contract changes:** none. `removal_findings` keeps its parameters and its return; it no longer hands `maps` or `default_repo` to `place`, and returns more findings of the shape it already returned.
- **New units:** `tests/test_a_record_states_what_the_tree_has.py#test_a_removal_is_read_in_this_tree_never_in_another_checkout`, the round's regression case, and `tests/test_a_record_states_what_the_tree_has.py#test_a_path_through_dot_dot_is_refused_never_read_as_gone`, the case for ⬜ 2. No shipped unit is new.

⬜ 2 was fixed rather than answered because it is the same function and the same direction as 🟡 1, and the fix forces a format rather than reading one more spelling: a `## Removes` path that walks through `..` is refused, so whether `a/../x.py` names a file never depends on whether `a` exists. A path that escapes the tree keeps round 1's escape refusal, which is checked first.

## Seen red

Each through `bin/mutation-check` against 5dfefd3b, every verdict `red`: `place` handed `maps` and `default_repo` again, the `--map` refusal removed, and the `..` refusal removed.
