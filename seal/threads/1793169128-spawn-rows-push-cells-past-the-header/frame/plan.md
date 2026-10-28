# Implementation Plan: 1793169128-spawn-rows-push-cells-past-the-header

Approved <date> by <who>, when `crafter` was spawned.

## Summary

`cycle_label` cuts a spawn-cycle label from the right to `LABEL_WIDTH`, the
width the per-segment table already uses. `report_spawns` pads to that name
at its four sites, and the description line under *what each cycle spawned*
gains one space after the padded label. One case pins a 28-character
`subagent_type` and is seen red against the base first. This is the
paste-ready fix of round 1 of work item `1790835050`, with the separator
added and the shared constant's comment rewritten.

## Technical context

The code at base `977b6613`, all read:

- `skills/verify/scripts/session_cost.py:2225`, `cycle_label(row)`. It
  returns `f"cycle {row['cycle']}  {row['subagent_type'] or '?'}"` for a
  cycle row and `row["kind"]` (`head` or `tail`) otherwise, and never cuts.
- `skills/verify/scripts/session_cost.py:2236`, `report_spawns`. The header
  at `:2318` is `{'row':<30}{'span':>8}{'command':>9}{'model':>8}`
  `{'delegated':>11}{'calls':>7}{'t/turn':>8}{'gap':>7}`. A row with no call
  is printed at `:2328`, a row with numbers at `:2333`, and the description
  line at `:2419` as `{cycle_label(row):<30}{row['description'][:70]}`.
  Each cell after the label is right-aligned, so a label that fills the
  column still leaves a space before the first cell. The description is not
  right-aligned, so it needs its own space.
- `skills/verify/scripts/session_cost.py:2422` to `:2425`, the comment and
  `LABEL_WIDTH = 30`. Python looks the name up when `cycle_label` runs, so
  the constant would work where it stands. It moves above `cycle_label`
  anyway, so that a reader meets the constant before either table that
  reads it.
- `skills/verify/scripts/session_cost.py:2460`, `segment_label`. It cuts a
  named agent with `row["agent"][:width]`, with no mark, and cuts a
  transcript path from the left with a leading `…`. Its docstring says
  cutting from the right is "the way every other label here is cut". That
  sentence is false at base, because `cycle_label` does not cut, and it
  becomes true with this work.
- `tests/skills/test_session_cost.py:548`, `delegated_cells(out)`. It finds
  the header by `startswith("  row ")` and reads each row's 11 characters
  that end where the word `delegated` ends. Round 1 of work item
  `1790835050` executed it on a 37-character label and read `0.0m`, the
  `model` cell, where the `delegated` cell was `1.0m`
  (`5180b89e:seal/specs/1790835050-the-delegated-note-compares-what-it-prints/rounds/round-1-report.md`
  *3. The case*, read). That measurement is round 1's, at an older
  commit. The crafter repeats it at this base as the case's red run.
- `tests/skills/test_session_cost.py:465`, `spawn(uid, start, end,
  subagent_type, description)`, and `:515`, `spawns_of(path, args)`, are
  the fixtures the new case builds on.
  `test_the_delegated_note_follows_the_minute_the_column_prints` (`:3248`)
  builds a spawn paired in 59.6 s that prints `1.0m` under `delegated`. The
  new case reuses that shape with the long `subagent_type`.

**The failure scenario of the chosen approach, six months on.** Two agents
whose names share their first characters up to the cut print the same label
on the page. For a single-digit cycle that means the first 21 characters of
`subagent_type`. A reader comparing those two rows cannot tell them apart
from the page and has to open `--json`, where `subagent_type` stays whole.
The `cycle N` prefix still tells the rows apart. What is lost is which
agent each row was, and only for names that long.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Cut `cycle_label` from the right to `LABEL_WIDTH` with no mark, pad all four sites to `LABEL_WIDTH`, and put one space before the description | Two long names that share their first 21 characters print one label, and the reader needs `--json` to tell them apart | Chosen. It keeps the fixed column, and `segment_label` already cuts a named agent this way, so the report keeps one convention. |
| Widen the column to the longest label present, as `skills/verify/scripts/broad_gate.py:2830` computes `pad` from the widest check name. This replaces the fixed-width structure. | The column's width depends on the run. Readings pasted into the flow-measurement log stop lining up with each other. The spawn table and the per-segment table on one page get different label widths. A 60-character name widens every row of the table by 30 columns. | Rejected. The premise that keeps the fixed column was checked. `segment_label` and `report_segments` already cut and pad to one named width (`:2460` to `:2484`, `:2772` to `:2800`, read). No case and no document needs the full name on the page, since `--json` keeps `subagent_type` whole (`tests/skills/test_session_cost.py:2861` asserts it through `spawns_of`, read). |
| Print only the text after the last `:` of `subagent_type`, as `segment_kind` does for the bar lookup | Two plugins' agents with one basename print one name. A basename longer than 21 characters still overflows, so the cut is needed anyway. | Rejected. It loses information without removing the need for the cut. |
| Cut with a trailing `…` to show that the name was cut | `segment_label` cuts a named agent with no mark. One page would carry two conventions for the same act, or the work would also change `segment_label`, outside the issue. | Rejected. Consistency with the existing cut decides it. `questions.md` lists it among the judgments the tree answered. |
| Cut in `cycle_label` with `[:30]` and keep the four `:<30` literals | Five places hold one width. The comment above `LABEL_WIDTH` already names this failure: "Two literals that have to agree is a column that goes ragged the day one of them moves." | Rejected. |
| Round 1's paste-ready fix as written | A label cut to the full 30 characters runs into its description under *what each cycle spawned*, as in `cycle 1  vercel:performance-opBuild phase 1` | Adopted with the separator added and the comment above `LABEL_WIDTH` rewritten. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `cycle_label` cuts to `LABEL_WIDTH`, with its docstring saying so. `LABEL_WIDTH` stands above `cycle_label`, and its comment names both tables. `report_spawns` pads to `LABEL_WIDTH` at the header, the no-call row, the numbered row and the description line, and the description line has one space after the padded label. One new case in `Test_main` of `tests/skills/test_session_cost.py` covers all four scenarios of `frame/design.md` that need a new case. | The new case is seen red with the base `cycle_label` and `report_spawns` restored, and the hand-back says how. Then `bin/test tests/skills/test_session_cost.py -q` passes. `uvx ruff check` and `uvx ruff format --check` pass on the two changed files. `git grep -n ':<30' -- skills/verify/scripts/session_cost.py` prints nothing. The suite is the orchestrator's broad gate. | |

## Operational impact

None for a deployer: no migration, no environment variable, no dependency,
and no flag or JSON key changes. The `seal cost --spawns` page changes for a
label longer than 30 characters, which is now cut. Every line under *what
each cycle spawned* moves its description one column to the right. A script
that parses that page by column would see the second change. None in this
repository does: `git grep -c 'what each cycle spawned' -- tests` finds no
match and exits 1 (executed).
