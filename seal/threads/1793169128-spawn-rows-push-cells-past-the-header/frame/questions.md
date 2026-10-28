# Questions for the planner: 1793169128-spawn-rows-push-cells-past-the-header

## Answered by the tree, not to be reopened

- **The label is cut; the column is not widened.** Issue #712 offers both.
  The comment above `skills/verify/scripts/session_cost.py#LABEL_WIDTH`
  names one fixed width for the label column. `segment_label` already cuts
  to it and `report_segments` already pads to it. `plan.md` *Alternatives
  considered* gives widening's failure scenario and the premise that was
  checked.
- **The cut is from the right and carries no mark.** `segment_label` cuts a
  named agent with `row["agent"][:width]` and no mark, and its docstring
  states that convention. A second convention for the same act in one report
  would read as a different act.
- **The full name stays reachable.** `--json` keeps `subagent_type` whole,
  and the new case asserts that.
- **The description line gains one space.** It is one of the four sites the
  issue names. Without the space, a label cut to the full 30 characters runs
  into the description. The header table needs no space, because its cells
  are right-aligned.
- **No parallel work item's file is touched.** This work edits
  `skills/verify/scripts/session_cost.py` and
  `tests/skills/test_session_cost.py`. Neither belongs to #1058, #913 or
  #920 as the spawn prompt lists them, and the new case needs nothing from
  `tests/conftest.py`.

## Assumed, because a different answer would not change what gets built

- The crafter decides how the new case reads every cell under its header. It
  can use `delegated_cells` together with assertions on the label and the
  description line, or a helper that reads every column by its header's
  right edge. Either way the acceptance rows of `frame/design.md` are what
  the case must show.

## Open rows

No row is open. Nothing in this work needs a person, a measurement before
the build, or a decision that only the build can make.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
