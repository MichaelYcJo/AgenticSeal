# 1791384152-a-reader-declares-its-input-class — round 1's fix pass

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 🟡 1 | fixed | e6843d9a |
| 🟡 2 | fixed | 20c4e993 |
| 🟡 3 | fixed | 978aa43a |
| ⬜ 4 | fixed | 1aa26afa |
| ⬜ 5 | answered | the two descriptions in `survivor_check.py` are of phase records as the check meets them, and every phase record written before #835 does carry what it removed; the check reads those records, so the sentence stays true where it stands |
| ⬜ 6 | answered | the writer runs only where no census exists, and this repository's census exists; a path with whitespace in it would be refused line by line by the test that reads it, which is loud, and widening `CENSUS_LINE` is mechanism a fix pass does not add |

## What the fix range changes

The range is e6843d9a..1aa26afa.

- **Contract changes:** none. `k1_call`, `removal_findings` and `cutoff_row` keep their parameters and their returns; `removal_findings` returns more findings of the shape it already returned.
- **New units:** `tests/test_a_record_states_what_the_tree_has.py#test_a_coordinate_that_does_not_read_is_refused_never_read_as_gone`, the case that pins 🟡 2. No shipped unit is new.
- **Removed:** `tests/reader_registry.py#K1_MODULES`, the receiver rule 🟡 1 is about; it never shipped, so it takes no row in the frame's `## Removes`.

## Seen red

Each through `bin/mutation-check`, every verdict `red`: the name fallback restricted to a receiver no import binds (the build's rule), the `os.open` row removed, the `re.split` row removed, the escaping-path refusal removed (the case fails on the `None` repository it then joins), and the unreadable-path refusal removed.
