# Review round 2: 1793169128-spawn-rows-push-cells-past-the-header

target: ab628278, fixes 92b21979..ab628278

## Findings

None. The fix range changes three records and no code. `git diff --stat
92b21979..ab628278` lists `changelog.md`, `gaps.md` and `trail/rounds/round-1.md`
only, and `git diff --stat 977b6613..ab628278 -- skills tests` lists the same
two files that round 1 reviewed at `dbf9f2ef`, with no line changed since
(executed). No unit was added or changed, so no finding of this round
names a fix pass as the cause of a defect.

## Confirmations

confirms: round-1#1
The close `fixed 2752c754` holds. `changelog.md:3` now reads "Before, a label
longer than the column pushed every cell of its row to the right", and then
says the label is `cycle N  ` and the `subagent_type` together, so for a
single-digit cycle any name longer than 21 characters overflowed.
`gaps.md:5-9` now says the label, `cycle N  ` and the agent name together, was
longer than the label column. Both are round 1's paste-ready text, word for
word (read, `git show ab628278:` of each file). The arithmetic holds: `cycle 1  `
is 9 characters, so a 21-character name makes exactly 30 and fits, and a
22-character name makes 31 and overflows. This round carried the label's shape
from round 1 (`skills/verify/scripts/session_cost.py:2245`) and did not
re-derive it, because the fix range changes no code. The commit `2752c754`
touches both paths that the finding's `location:` names.
The crafter claimed that no other statement puts the threshold on the name
alone. This round ran its own `git grep` at `ab628278` over the work item's
records, `skills/verify`, the module's tests, `docs` and `CHANGELOG.md`
(probe row 1). The hits outside round 1's own text are these. `frame/design.md:4`
says "longer than the column allows", which is correct. `frame/plan.md:70`
puts 21 characters on a basename after the last `:`, which is correct for a
single-digit cycle. `skills/verify/scripts/session_cost.py:2240` and
`tests/skills/test_session_cost.py:3286` say it of the label. The hit at
`skills/verify/scripts/broad_gate.py:2827` is about check names in another
table and is not part of this class. The fix pass wrote only the `verdict:`
and `answer:` lines of round 1's finding (read, the diff of `ab628278`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and whether the unpriced new case keeps `test_the_durations_file_prices_the_suite` under `STALE_SHARE`, carried from round 1 and still open | `.test_durations` | the orchestrator, through `seal gate` |
| Round 1's row on names with characters wider than one terminal column, carried and not re-judged, since the fix range changes no code | `skills/verify/scripts/session_cost.py:2246` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git grep -nE 'longer than (the\|its)( label)? column\|name (is \|was )?longer than' ab628278 -- seal/threads/1793169128-spawn-rows-push-cells-past-the-header skills/verify tests/skills/test_session_cost.py docs CHANGELOG.md` | exit 0. Every hit outside `round-1.md` states the threshold on the label, on the column "allows", or on a basename with the 21-character figure. The one other hit is `broad_gate.py:2827`, a different table. |
| `git diff --stat 92b21979..ab628278`, and `git diff --stat 977b6613..ab628278 -- skills tests` | records only in the fix range. The code diff since the base is the same two files round 1 read. |
