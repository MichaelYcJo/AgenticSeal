# Phase 1: 1793169128-spawn-rows-push-cells-past-the-header

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 77d0d095 |

## What this phase was asked

Build `frame/plan.md`'s one phase. `skills/verify/scripts/session_cost.py#cycle_label`
cuts its label to `LABEL_WIDTH`. `report_spawns` pads to `LABEL_WIDTH`
instead of the literal `30`. The line under *what each cycle spawned* gets one
space between the label and the description. `LABEL_WIDTH` and its comment
move above `cycle_label` and name both tables. `Test_main` in
`tests/skills/test_session_cost.py` gains one case, seen red against the base
first. `frame/questions.md` left one choice to the crafter: how the case
checks that a cell sits under its header.

Edit only `session_cost.py`, `tests/skills/test_session_cost.py`,
`.test_durations` if the new case needs a key, and this work item's records.
Work items #1058, #913 and #920 run in parallel and own other files.

## What this phase found

- **The frame held at this tree.** Every coordinate `frame/design.md` and
  `frame/plan.md` name was where they said: `cycle_label` at `:2225`, the
  four `:<30` sites at `:2318`, `:2328`, `:2333` and `:2419`, the comment and
  `LABEL_WIDTH` at `:2422` to `:2425`, `delegated_cells`, `spawn`,
  `spawns_of` and the neighbouring case (read).
- **How the case reads every cell.** It keeps `delegated_cells` for the
  `delegated` column and adds one assertion that the row is exactly as long
  as its header. Every cell after the label is right-aligned at a fixed
  width, so a row as long as its header has each cell ending where its
  header ends. One assertion covers every column, and no new helper was
  written.
- **The red run reproduced round 1's reading at this base.** With the code
  unchanged, `delegated_cells` read `0.0m` where the spawn's interval printed
  `1.0m`. The row was 7 columns longer than its header, and the description
  line read `cycle 1  vercel:performance-optimizerBuild phase 1` (executed).
- **`seal mutate` found one pad nothing watched.** Six units were each broken
  once: the cut, the separator, the header's pad, the numbered row's pad, the
  no-call row's pad and the value of `LABEL_WIDTH`. Five went red. The
  no-call row's pad SURVIVED, and it was unpinned at the base too, since no
  case read where that row's text starts. The case's `head` row has no call,
  so commit `77d0d095` asserts that row's label column is as wide as the cut
  label. The same mutant then went red (executed).
- **`.test_durations` gained no key.** `CONTRIBUTING.md` says the file is
  refreshed from the `test-durations` artifact of the branch's latest CI run.
  `test_the_durations_file_prices_the_suite` passes with up to one collected
  case in twenty unpriced (`STALE_SHARE = 0.05`), so one new case does not
  need a hand-written price.
