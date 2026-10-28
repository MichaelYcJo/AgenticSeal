# Feature Specification: 1793169128-spawn-rows-push-cells-past-the-header

Issue #712: `seal cost --spawns` pads each row's label to 30 columns and never
cuts it, so a `subagent_type` longer than the column allows pushes every cell
of its row to the right of its header.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." | The spawn table and the per-segment table share one label width. `LABEL_WIDTH` in `skills/verify/scripts/session_cost.py` is that source, and the four literal `30`s in `report_spawns` go. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact." Contract rule 19 says the same. | The comment above `LABEL_WIDTH` says it is "the label column of the per-segment table" and that `segment_label` cuts to it and `report_segments` pads to it. The comment is rewritten to name both tables in the same commit. |
| Contract rule 12, *A defect belongs to a class, so enumerate the class*. | The class is a label from free text that is padded to a column and never cut. The enumeration is under *Scope*, and `cycle_label` is its only instance. |
| Contract rule 14, *A fix that changes what a person sees documents it and pins it*. | The cut label and the separated description are text a person reads. The new case pins both. |
| Contract rule 15, *A new case is not planted until it has been seen red*. | The new case is shown red against the base `cycle_label`, where round 1 of work item `1790835050` measured `delegated_cells` reading the `model` cell (`0.0m`) in place of the `delegated` cell (`1.0m`). |
| `docs/measuring-a-run.md` *The unit is a segment, and a segment has its own transcript*. | The section says what a spawn-cycle row measures. It says nothing about how the row is laid out, which is why `## Rule changes` holds the no-change block. |

## Scope

**In.**

- `skills/verify/scripts/session_cost.py#cycle_label` cuts its label from the
  right to `LABEL_WIDTH` characters, the way `segment_label` cuts a named
  agent. At base `977b6613` the function is at `:2225` and returns the label
  uncut (read).
- `skills/verify/scripts/session_cost.py#report_spawns` pads to `LABEL_WIDTH`
  at the four sites that now read `:<30`: the header (`:2318`), the row with
  no call (`:2328`), the row with numbers (`:2333`) and the line under *what
  each cycle spawned* (`:2419`) (read, at `977b6613`).
- Under *what each cycle spawned*, one space stands between the padded label
  and the description. Without it, a label cut to the full 30 characters runs
  straight into the description, as in
  `cycle 1  vercel:performance-opBuild phase 1`. The header table needs no
  separator, because each of its cells is right-aligned in a column wider
  than the value.
- `LABEL_WIDTH` and the comment above it move to stand above `cycle_label`,
  since both tables now read it. The comment is rewritten to say that
  `cycle_label` and `segment_label` cut to it and that `report_spawns` and
  `report_segments` pad to it.
- `cycle_label`'s docstring says that the label is cut to the column it is
  padded to, and why.
- One new case in `tests/skills/test_session_cost.py`, class `Test_main`,
  beside `test_the_delegated_note_follows_the_minute_the_column_prints`.

**The class, enumerated (rule 12).** Every format spec that pads a value to a
fixed width in shipped Python was listed with
`git grep -nE '\{[^}]*:<[0-9]+\}|:<\{' -- '*.py' ':!tests'` (executed). Each
site's input was then read:

| Site | Its label | Bounded? |
|---|---|---|
| `skills/verify/scripts/session_cost.py` `:2318`, `:2328`, `:2333`, `:2419` | `cycle_label`, carrying a free-text `subagent_type` | no: this work |
| `skills/verify/scripts/session_cost.py:2150` | a name from `FAMILIES` or `other` in a 12-wide column; the widest is `lint/type`, 9 characters (executed, importing `FAMILIES`) | yes |
| `skills/verify/scripts/session_cost.py` `:2772`, `:2795`, `:2800` | `segment_label`, cut to `LABEL_WIDTH` | yes |
| `skills/verify/scripts/broad_gate.py:2833` | a check name; the pad is the widest name present | yes |
| `.github/scripts/release_seal.py:491` | one of the fixed `LABELS`, the widest 8 characters | yes |
| `skills/verify/scripts/seal_stamp.py:593` | a fixed row label of the stamp | yes |
| `skills/implement/scripts/seal.py` `:2296`, `:2298`, `:2387` | a mode, one of `MODES` (`choices=MODES` at `:2900`) | yes |

**Out.**

- `segment_label` and the per-segment table keep their behaviour. They
  already cut to `LABEL_WIDTH` (read, `:2460` to `:2484`).
- The `--json` output does not change. `subagent_type` stays whole there, so
  a reader who needs the full name of a cut row reads it from `--json`.
- No mark such as `…` is added to a cut label. `segment_label` cuts a named
  agent from the right with no mark, and two conventions in one report would
  read as two different things. `questions.md` lists this among the
  judgments the tree answered.
- The column is not widened to the longest label. `plan.md` *Alternatives
  considered* gives the failure scenario.
- No file that the parallel work items #1058, #913 or #920 own is touched.
  This work edits `skills/verify/scripts/session_cost.py` and
  `tests/skills/test_session_cost.py` only, and the new case needs nothing
  from `tests/conftest.py`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A long agent name keeps its row under the header | Given a transcript with one spawn whose `subagent_type` is `vercel:performance-optimizer` (28 characters, so the uncut label `cycle 1  vercel:performance-optimizer` is 37), when `seal cost --spawns` prints its table, then the row's label reads `cycle 1  vercel:performance-op` and every cell of the row ends at the right edge of its own header. | The new case. `delegated_cells(out)` returns the `delegated` cell the spawn's interval prints (`1.0m` for a spawn paired in 59.6 s), not the `model` cell, and the label is asserted as the 30-character cut. Seen red against the base `cycle_label`. |
| A short agent name is unchanged | Given the existing `orchestrator` fixture (`agentic:crafter`, `agentic:proofer`), when `--spawns` prints, then the rows read as they read at base. | The existing cases in `Test_main` that assert `cycle 1  agentic:crafter` and `cycle 2  agentic:proofer` (`tests/skills/test_session_cost.py:3208`, `:3209`) and `cycle 1  ?` (`:3390`) stay green. |
| A cut label does not run into its description | Given the long-name transcript, when the page prints *what each cycle spawned*, then the line reads `cycle 1  vercel:performance-op` followed by one space and the spawn's description. | The new case asserts that line. Seen red against the base, where the line has no separator. |
| `--json` keeps the full name | Given the long-name transcript, when `seal cost --json` reads it, then the cycle row's `subagent_type` is `vercel:performance-optimizer` whole. | The new case asserts it through `spawns_of`. |
| One width for both tables | Given the module, when a reader looks for the label width, then it is one name, `LABEL_WIDTH`, and no `:<30` literal is left in `report_spawns`. | `git grep -n ':<30' -- skills/verify/scripts/session_cost.py` prints nothing, run by the crafter and again by the review. |

## Data & interfaces

- No schema, flag or JSON key changes.
- What a person sees changes in `seal cost --spawns` only, in two places.
  A spawn-cycle row's label is cut to 30 characters wherever it is printed.
  The lines under *what each cycle spawned* gain one space between the padded
  label and the description.
- `skills/verify/scripts/session_cost.py#cycle_label` keeps its signature
  `cycle_label(row)` and returns at most `LABEL_WIDTH` characters.

## Rule changes

- nothing
  why: no policy document states the spawn table's layout; docs/measuring-a-run.md says what a spawn-cycle row measures and not how wide its label is

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The literal width `30` in the header's format spec `{'row':<30}` | `skills/verify/scripts/session_cost.py#report_spawns` (`:2318` at `977b6613`) | `LABEL_WIDTH`, the one name for the label column |
| The literal width `30` in the no-call row's format spec `{cycle_label(row):<30}` | `skills/verify/scripts/session_cost.py#report_spawns` (`:2328` at `977b6613`) | `LABEL_WIDTH` |
| The literal width `30` in the numbered row's format spec `{cycle_label(row):<30}` | `skills/verify/scripts/session_cost.py#report_spawns` (`:2333` at `977b6613`) | `LABEL_WIDTH` |
| The literal width `30` in the description line's format spec `{cycle_label(row):<30}` | `skills/verify/scripts/session_cost.py#report_spawns` (`:2419` at `977b6613`) | `LABEL_WIDTH`, with one space after the padded label |
| The comment's claim that `LABEL_WIDTH` is the label column of the per-segment table alone | the comment above `skills/verify/scripts/session_cost.py#LABEL_WIDTH` (`:2422` to `:2424` at `977b6613`) | The rewritten comment above `LABEL_WIDTH`, which names both tables |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-28 by framer, before the build.
