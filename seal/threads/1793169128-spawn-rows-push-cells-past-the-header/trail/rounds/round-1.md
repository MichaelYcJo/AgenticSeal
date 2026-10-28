# Review round 1: 1793169128-spawn-rows-push-cells-past-the-header

target: dbf9f2ef against 977b6613

## Findings

### 1. The changelog fragment and gaps.md say a name overflowed only past the column's width, while the issue's own 28-character name overflowed

severity: should
location: `seal/threads/1793169128-spawn-rows-push-cells-past-the-header/changelog.md:3`, `seal/threads/1793169128-spawn-rows-push-cells-past-the-header/gaps.md:5-8`
evidence: read `seal/threads/1793169128-spawn-rows-push-cells-past-the-header/changelog.md:3`, `seal/threads/1793169128-spawn-rows-push-cells-past-the-header/gaps.md:5-8`, `skills/verify/scripts/session_cost.py:2244-2246`, `tests/skills/test_session_cost.py:3297-3298`
verdict: open

The changelog fragment says: "Before, a `subagent_type` longer than the
column pushed every cell of its row to the right". The opening paragraph of
`gaps.md` says the same of "a spawn row whose agent name was longer than the
label column". Both sentences put the threshold at the column's 30
characters. The label is `cycle N  ` followed by `subagent_type`
(`session_cost.py:2245`), so the prefix takes 9 of the 30 characters for a
single-digit cycle. Any name longer than 21 characters overflowed, and past
cycle 9 any name longer than 20. The new case's own name,
`vercel:performance-optimizer`, is 28 characters (`test_session_cost.py:3297`),
shorter than the column. It still overflowed at the base: with the cut
removed, the case goes red (probe row 2, mutant 1).

Why it matters: the fragment goes to `CHANGELOG.md` at the release, and the
pull request body copies the records. A reader with a 25-character agent
name who reads "longer than the column" concludes that the rows of their
earlier readings were laid out correctly, when they were shifted. The
description in `frame/design.md:4` ("longer than the column allows") and the
commit message of `53bd30a4` ("a spawn row's label longer than its column")
state the threshold correctly. The two sentences above are the ones that put
it on the name.

The fix, for `changelog.md:3`, replacing the second sentence of the bullet:

```markdown
Before, a label longer than the column pushed every cell of its row to the right, and a reader took one column's number for the next one's. The label is `cycle N  ` and the `subagent_type` together, so for a single-digit cycle any name longer than 21 characters did it.
```

For `gaps.md:5-8`:

```markdown
`seal cost --spawns` printed a spawn row whose label, `cycle N  ` and the
agent name together, was longer than the label column, and every cell of
that row sat to the right of its header, so a reader took one column's
number for the next. The label is now cut to the column, and each cell
stays under its header whatever the name.
```

answer:

## Confirmations

confirms: none
The spec's four code changes stand as `frame/design.md` *Scope* states them,
read at `dbf9f2ef`. `cycle_label` cuts with `label[:LABEL_WIDTH]` and keeps
its signature (`skills/verify/scripts/session_cost.py:2232-2247`).
`LABEL_WIDTH = 30` and its comment stand above it, and the comment names both
tables, both cutters and both padders (`:2225-2229`). The comment's old
wording, "the label column of the per-segment table", is gone from the tree.
`report_spawns` pads to `LABEL_WIDTH` at the header (`:2332`), the no-call
row (`:2342`), the numbered row (`:2347`) and the description line (`:2435`).
The description line has one space after the padded label. The docstring
says the label is cut and why, and the claim that `segment_label` cuts a
named agent with no mark matches `:2491`. `git grep -n ':<30' --
skills/verify/scripts/session_cost.py` printed nothing and exited 1
(executed).

confirms: none
The crafter claimed that the new case was seen red at the base and that
`seal mutate` turned all six units red after `77d0d095`. This round ran its
own six mutants of `skills/verify/scripts/session_cost.py` against the new
case alone (probe row 2). Removing the cut, which is the base `cycle_label`,
went red. Removing the separator went red. Widening the header's pad, the
no-call row's pad or the numbered row's pad by one went red. Setting
`LABEL_WIDTH` to 31 went red. 6 of 6 were red, so the no-call row's pad, which
the crafter reported as surviving before `77d0d095`, is now watched
(executed). This says that each unit is tested. It does not say that the
table is right for every input.
Round 1 of work item `1790835050` measured `delegated_cells` reading `0.0m`
on a 37-character label. This round did not carry that measurement. It
re-established the base failure through mutant 1.

confirms: none
The crafter claimed that the module passes with 252 cases. At `dbf9f2ef`,
`bin/test tests/skills/test_session_cost.py -q` printed `252 passed` and
exited 0 (executed). The rows that the design's *A short agent name is
unchanged* scenario names are among them: `cycle 1  agentic:crafter` and
`cycle 2  agentic:proofer` (`tests/skills/test_session_cost.py:3208-3209`)
and `cycle 1  ?` (`:3424`, which was `:3390` at the base). `uvx ruff check`
and `uvx ruff format --check` on the two changed files each exited 0
(executed).

confirms: none
The new case was read against its group. It is the only case that gives
`--spawns` a label longer than the column. The case beside it,
`test_the_delegated_note_follows_the_minute_the_column_prints`, uses the
same 59.6 s spawn with `agentic:crafter`, a label that fits. `bin/seal layout
--pairs` names no pair that holds the new case (executed). The case asserts
all four scenarios of the design that need a new case: the cut label with
the row as long as its header, the `delegated` cell reading `1.0m`, the
description line with its space, and `subagent_type` whole in `--json`
(`tests/skills/test_session_cost.py:3283-3315`, read).

confirms: none
The design's rule-12 enumeration was checked with a wider search. A search
for `.ljust(`, `.rjust(`, `%-Ns` and fill-character pads in shipped Python
found only the sites the design lists (executed). A second search for
right-aligned and centred specs found numeric cells only (executed). No
other free-text label is padded to a fixed column without a cut.

confirms: none
`gaps.md` *Not done* claims that one unpriced case is within the durations
check's tolerance. `STALE_SHARE = 0.05` stands at
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:90`
(read). Whether this branch's collection stays under that share is the broad
gate's, and is a row below. The suite is labelled `unverified` in `gaps.md`
*Not verified*, with the orchestrator as its answerer. The label is honest:
neither the crafter's hand-back nor this round ran the suite.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and whether one unpriced case keeps `test_the_durations_file_prices_the_suite` under `STALE_SHARE` with the parallel work items' cases added | `.test_durations` | the orchestrator, through `seal gate` |
| A `subagent_type` with characters wider than one terminal column is cut by code points, not by display columns, so such a name would still overflow. `segment_label` shares this. Nothing in the tree says whether an agent name can hold such characters. | `skills/verify/scripts/session_cost.py:2246`, `skills/verify/scripts/session_cost.py:2491` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_session_cost.py -q`, in a `--no-local` clone at `dbf9f2ef` | `252 passed in 1.95s`, exit 0 |
| `bin/seal mutate skills/verify/scripts/session_cost.py` with six `--replace` pairs: the cut removed, the separator removed, the header's, no-call row's and numbered row's pads each widened by one, and `LABEL_WIDTH = 31`; `--tests "bin/test tests/skills/test_session_cost.py -q -p no:xdist -k long_agent_name"` | baseline passed, then 6 mutants, 6 red, 0 survived, exit 0. The file was restored, and `git status --short` in the clone printed nothing. |
| `uvx ruff check` and `uvx ruff format --check` on the two changed files | exit 0 each |
| `bin/seal layout --pairs` | 128 lines, none naming `test_a_long_agent_name_is_cut_so_its_cells_stay_under_their_headers` (grep exit 1) |
| `git grep -n ':<30' -- skills/verify/scripts/session_cost.py` | no output, exit 1 |
| `git grep -nE` over shipped Python for `.ljust(`, `.rjust(`, `%-Ns`, fill-character pads, and right-aligned or centred specs | left-aligned: only the sites `frame/design.md` *Scope* lists. Right-aligned: numeric cells only. |
