# Review round 1: 1794401941-payload-calibration-reached-by-tests-alone

```seal
target: 238411e42 against origin/release/v0.37.4
```

This is the first round. No earlier record carries a coordinate, so every
fact below was established here. The diff was read from the merge base
`52f87b8d3` to `238411e42`, in the branch worktree and in a
`git clone --no-local` of it under the round's scratch directory. Every
run below ran in that clone. `routing.md`, the three frame files,
`gaps.md`, `changelog.md` and `pr.md` were each read whole at `238411e42`,
then both phase records. No `pr.<lang>.md` stands, and none is owed:
`seal/config.json` names English for both language keys. No
`seal/parity.json` is declared (executed: `ls`).

The issue body was read with `gh issue view 1484 --json title,body,comments`.
The issue has no comments.

## Findings

### 1. `pr.md` carries the orchestrator's own account after each quote, and quotes neither the verdicts nor the title row

```seal
severity: must
location: `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/pr.md:1-4`
evidence: read `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/pr.md:1-8`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/frame/plan.md:19`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/frame/plan.md:21`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/frame/plan.md:24`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/frame/plan.md:27`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/frame/plan.md:57`, `skills/code-review/orchestration.md:395-418`; executed `bin/seal pr-body seal/threads/1794401941-payload-calibration-reached-by-tests-alone --body <scratch>/pr-body-probe.md`, exit 0
```

Why it matters: `skills/code-review/orchestration.md:410-412` says "`pr.md`
holds no sentence of the orchestrator's own account: no sentence frames a
quote or joins two". The same paragraph says a quote's coordinate is "the
record's path, then the heading, row, finding or line that holds the
sentence". The rule exists so that every sentence of the body above the
fold is a record a round has read at its source.

Each of the four lines in `pr.md` quotes an *Approach* cell of
`frame/plan.md` *Alternatives considered*. Each quote is found word for
word at plan rows 19, 21, 24 and 27. But each parenthesis then goes past
the coordinate with a summary of the verdict that is in no record:

- Line 1 adds "rejected: `--baseline` is called by no document or workflow
  either, so the work removes four flags where the owner's decision names
  three". The verdict cell at `frame/plan.md:19` reads "Rejected. The
  issue's own line range and title put `--baseline` inside the cut (design
  G2)."
- Line 2 adds "rejected: the three stay and both READMEs' `seal payload` row
  names them". The cell at `:21` reads "Rejected. Naming the three in the
  README row meets the *Done when* line at the cost of one cell per README."
- Line 3 adds "rejected: every token figure carries one label, `estimated
  (3.2 B/token, an assumed ratio)`". The cell at `:24` reads "Rejected. One
  label for every row, *Scope* item 2."
- Line 4 adds "rejected: the rider counted a gate #1027 removed". The cell
  at `:27` reads "Rejected. `seal/follow-up.md` has the reader delete a
  spent rider."

Each added sentence is true against the tree (G3, the README rows, `BASIS`
at `skills/verify/scripts/payload_meter.py:85`, G10). The defect is that
the owner reads them as the record when they are the orchestrator's
paraphrase. Line 1's paraphrase also states the one judgment the owner
most needs to see, the fourth flag removed, in words no record holds.

The same paragraph (`skills/code-review/orchestration.md:413-418`) names
"why the title takes its prefix" as something quoted from the
orchestrator's row of `frame/plan.md` *Judgments of the run*. The commit
that wrote `pr.md`, `238411e42`, added that row at `frame/plan.md:57`, and
`pr.md` does not quote it.

`seal pr-body` composed the body from this `pr.md` and exited 0, so no
script refuses the paraphrase. Only a reader sees it.

```markdown
- "Remove the three flags the decision lists, and keep `--baseline` with `delta_against`" (`frame/plan.md` *Alternatives considered*, the row on keeping `--baseline`)
- "Rejected. The issue's own line range and title put `--baseline` inside the cut (design G2)." (`frame/plan.md` *Alternatives considered*, the row on keeping `--baseline`, its verdict)
- "Remove `--root`, `--agent` and `--json` too, so that no flag stands without a document" (`frame/plan.md` *Alternatives considered*, the row on removing `--root`, `--agent` and `--json`)
- "Rejected. Naming the three in the README row meets the *Done when* line at the cost of one cell per README." (`frame/plan.md` *Alternatives considered*, the row on removing `--root`, `--agent` and `--json`, its verdict)
- "Keep the two basis labels as they read" (`frame/plan.md` *Alternatives considered*, the row on the two labels)
- "Rejected. One label for every row, *Scope* item 2." (`frame/plan.md` *Alternatives considered*, the row on the two labels, its verdict)
- "Keep the rider at `lib/optin.py:85-91` with `parity_config` struck from its count" (`frame/plan.md` *Alternatives considered*, the row on the rider)
- "Rejected. `seal/follow-up.md` has the reader delete a spent rider." (`frame/plan.md` *Alternatives considered*, the row on the rider, its verdict)
- "The title takes `refactor:`, as the issue's title does: the release report prints the same table and no command a document or workflow calls changes" (`frame/plan.md` *Judgments of the run*, the row on the title)

Closes #1484.
```

The attribution line stays below `Closes #1484.` as it stands. The repair
is the orchestrator's, since no crafter writes `pr.md`
(`skills/code-review/orchestration.md:446-449`).

### 2. The release note and the module docstring say every total is its bytes over 3.2, and the total is the sum of its rounded rows

```seal
severity: should
location: `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/changelog.md:3`, `skills/verify/scripts/payload_meter.py:23-28`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/frame/design.md:32`
evidence: executed `bin/seal payload --json` in the clone, read with `python3 -c` comparing each table's `total.tokens` with `round(total.bytes / 3.2)`; read `skills/verify/scripts/payload_meter.py:361-371`, `tests/skills/test_payload_meter.py:510-571`
```

Why it matters: `changelog.md:3` tells a person reading the release notes
"Every row and total, the session's and each agent's, is its bytes over an
assumed 3.2 bytes per token". A total is not. `_estimated`
(`skills/verify/scripts/payload_meter.py:361-371`) sets each row to
`round(bytes / ASSUMED_RATIO)` and the total to the sum of those rows. Its
docstring says why: "so the token column a reader adds up is the total
under it". `test_every_token_figure_reads_estimated_at_the_assumed_ratio`
(`tests/skills/test_payload_meter.py:510-571`) pins the difference. Its
docstring says "What the total may not be is a second division of the
sum", and its CRLF block asserts `summed != round(total bytes / ratio)`.

On this tree the two numbers differ in five of the six tables. Session:
12,327 bytes, total 3,853 tokens, `round(12327 / 3.2)` 3,852. The crafter,
framer, sealer and tracer totals are each one token above their bytes over
3.2 (executed). A person who checks the release note's arithmetic finds a
total that does not match it.

The module docstring at `payload_meter.py:23-24` says the same to an agent:
"Every token figure, the session's and each agent's, is the row's bytes over
`ASSUMED_RATIO`". A total's token figure is a token figure and is not a
row's bytes over the ratio. *Scope* item 2 of `frame/design.md:32` says the
work does this: "Every token figure the meter prints, an agent's and the
session's, is the row's bytes over `ASSUMED_RATIO`". So the frame states
the same contradicted fact.

Fix for `changelog.md:3`, the second sentence:

```markdown
Every row, the session's and each agent's, is its bytes over an assumed 3.2 bytes per token, and every total is the sum of the rows above it, all under one basis that reads `estimated (3.2 B/token, an assumed ratio)`.
```

Fix for `skills/verify/scripts/payload_meter.py:23-28`, the whole
`tokens` paragraph:

```python
  tokens          NEVER counted. Every row's token figure, the session's and
                  each agent's, is its bytes over `ASSUMED_RATIO`, and each
                  total's is the sum of its rows', all labelled `BASIS`. A
                  bare number is refused by the module's own tests, because
                  the six calibration spawns put three agents at 2.7, 3.2
                  and 3.4 bytes per token — one ratio does not fit all of
                  them.
```

This snippet does not reach `frame/design.md:32`. That fix is owed too, as
a fold of *Scope* item 2 to "Every row's token figure, an agent's and the
session's, is the row's bytes over `ASSUMED_RATIO`, and each total's is the
sum of its rows'". S2 and S5 (`frame/design.md:57`, `:60`) state only the
basis label and stay as they read. No case changes, since the existing
case already pins the sum.

## Confirmations

What matched: the removal of `--baseline` holds to the owner's decision
(read: the issue body). The *Decision* says "Remove the calibration and
baseline paths of `seal payload`". Its parenthesis lists `--calibrate`,
`--baseline-agent` and `--sections`. The title says "calibration and
baseline modes". The first *Done when* line, "Each flag that remains is
called by a document or a workflow", fails for a kept `--baseline` unless a
document is written for it (G3). With the calibration gone, `--baseline`
could only lend ratios an earlier calibrated run wrote
(`frame/plan.md:19`). `pr.md` and `changelog.md:7` both tell the owner that
four flags go. Finding 1 is about how `pr.md` says it, not about whether
the cut holds.

What matched: S3 holds in two clones, the procedure the scenario states.
Phase 1 measured it in the worktree. This round ran
`python3 .github/scripts/release_report.py --against v0.37.3 --at <at>` in
a clone of `918342dc0` and in a clone of `238411e42`, over one
`git archive v0.37.3`. Both exited 0 with 3,056 bytes of output, and
`diff` printed nothing. The five preload rows are G5's (executed). The
difference of procedure phase 1 named therefore changes nothing.

What matched: S1. `bin/seal payload` with `--calibrate x`,
`--baseline-agent x`, `--baseline x` and `--sections` each exited 2, each
with argparse's `unrecognized arguments` line (executed).

What matched: S2. `bin/seal payload --json` exited 0. The top-level keys
were `agents`, `measured_at`, `root` and `session`. The session and every
agent held `files` and `total` alone, no row held `sections`, and every
basis of every row and total was `estimated (3.2 B/token, an assumed
ratio)` (executed).

What matched: S4. `uvx vulture --min-confidence 60 agents bin evals hooks
lib skills .github` exited 3 with 20 lines at `238411e42` and 25 at
`918342dc0`. The five lines that left are the five symbols (executed).
`git grep -n -w` on the five names outside `seal/threads` finds
`strip_ansi` only at `tests/skills/test_seal_stamp.py:275`, `:821` and
`:862`, and the other four nowhere (executed).

What matched: S5, S6 and the plan rows' narrow runs. `bin/test` over the
eleven files the two plan rows and the rider case name exited 0, 567
passed (executed). `uvx ruff check` and `uvx ruff format --check` over the
thirteen Python files the diff changes both passed (executed). S5's three
cases were seen red against the base labels, as phase 1 claims. This round
judged that by reading only: each asserts `== BASIS` or the new pair-line
text, which the base's two labels fail. S7 holds by reading the two README
rows in the diff.

What matched: `## Removes` against the diff. `comm` of the `def` and
`class` names in `tests/skills/test_payload_meter.py` at base and head
lists the 11 *Test_measure* cases, *Test_sections_of* with both cases, the
two *Test_module* cases and the six fixtures that *Removes* names. It adds
`test_refuses_a_root_that_defines_no_agent` and the two renames of
*Scope* item 5 (executed). Every other unit *Removes* names is gone from
`payload_meter.py`, `lib/routing.py`, `lib/optin.py`, `lib/lines.py` and
`seal_stamp.py` in the diff (read).

What matched: the signature change reaches every caller. `git grep -n`
for `composition(`, `pair_rows(`, `file_row(` and `.measure(` outside the
meter and its test file finds only `.github/scripts/release_report.py:148`
and the stand-in at `tests/github/test_release_report.py:105`, both with
four arguments (executed). The stand-in takes exactly four parameters, so
a five-argument call would fail that file.

What matched: the new case is read against its group. At the base, the
only `returncode == 1` in the meter's test file was the calibration
refusal *Removes* takes (`git show 52f87b8d3:tests/skills/test_payload_meter.py`,
line 800). `bin/seal layout --pairs tests/skills/test_payload_meter.py`
names four pairs, all between `Test_imports_of` cases the diff does not
touch (executed). The case asserts `returncode == 1`, and the only
`return 1` in `main` is the `if not data["agents"]:` guard, so it pins that
guard (read: `skills/verify/scripts/payload_meter.py:550-565`). The
`seal mutate` run phase 1 cites was not re-run.

What matched: the rider is spent, as G10 and *Scope* item 10 state.
`hooks/hooks.json` registers a `Stop` hook and a `SessionStart` hook and
no gate on a tool call. No "gated command" is left for the rider's count
to describe (read). The rule at `docs/layout/one-root-by-lifetime.md:22-29`,
which *Test_parity_config*'s legacy-address case held in part, is still
held by `tests/lib/test_optin.py:552-565` (read).

What matched: the two comments the diff rewrites name real readers.
`skills/implement/scripts/seal.py:2207-2208` reads `optin.PARITY_CONFIG`
beside `OLD_PARITY_CONFIG` in `seal mode`'s report, as the new comment at
`lib/optin.py:63-65` says. The fifteen colour constants the comment at
`skills/verify/scripts/seal_stamp.py:110-112` counts all stay (read).

What matched: `gaps.md` *Not done* names two sentences kept on the
"six calibration spawns" and the kept name `_fence_rule`. Each is as the
memo says, and *Out of scope* gives such history to #1485 (read). Finding 2
asks for no change to the "six calibration spawns" clause.

What matched: `changelog.md` apart from finding 2. Each other sentence of
both items holds against the tree. That includes the refusal at exit 2,
the JSON keys removed, `composition`'s four arguments and the rider's
commit gate. `git show --stat 61a8455aa` is #1027's merge, and its message
says the commit gate inside git goes (executed).

What matched: `frame/plan.md` *Judgments of the run*, first row. Phase 1
named three frame statements and phase 2 three. The fold commit
`bb11563b9` names all six (read).

`tests/skills/test_payload_meter.py:563` skips a header cell `Section`
that the meter printed at neither the base nor the head. It is a guard
from before this diff and pins nothing, so this round opens no finding
for it.

`python3 skills/code-review/scripts/chain_check.py --baseline 52f87b8d3
--root <worktree> --worktree` printed no notice at a line of
`frame/design.md` naming a test pin or a copy (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| the full suite, the repository-wide lint and the format check beyond the eleven test files and thirteen Python files this round ran | the tree at `238411e42` | the orchestrator's broad gate |
| the new case `test_refuses_a_root_that_defines_no_agent` on Windows, where the `--root` it passes and the stderr it compares carry the platform's separators | `tests/skills/test_payload_meter.py:208-220` | the Windows leg of CI, read by the orchestrator |
| the five `seal mutate` mutants of phase 1 and the `strip_ansi` mutant of phase 2, which this round judged by reading the cases and did not re-run | `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/trail/phases/phase-1.md:63-71`, `seal/threads/1794401941-payload-calibration-reached-by-tests-alone/trail/phases/phase-2.md:45-50` | the sealer, against the phase records |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the meter's, release report's, routing, optin, lines, stamp, rider and four behaviour test files, `-q` | exit 0, 567 passed, 3 warnings |
| `bin/seal payload` with each of `--calibrate x`, `--baseline-agent x`, `--baseline x`, `--sections` | exit 2 each, argparse's `unrecognized arguments` line |
| `bin/seal payload --json`, read with `python3 -c` | exit 0; keys `agents`, `measured_at`, `root`, `session`; every basis the one label; `total.tokens` minus `round(total.bytes / 3.2)` is 1 for session, crafter, framer, sealer and tracer, 0 for proofer |
| `python3 .github/scripts/release_report.py --against v0.37.3 --at <at>` in clones of `918342dc0` and `238411e42`, then `diff` | both exit 0, 3,056 bytes each, `diff` empty |
| `uvx vulture --min-confidence 60 agents bin evals hooks lib skills .github` at both commits | exit 3 each; 25 lines at the base, 20 at the head, none of the five at the head |
| `uvx ruff check` and `uvx ruff format --check` over the changed Python files, through `xargs` | both exit 0 |
| `bin/seal layout --pairs tests/skills/test_payload_meter.py` | four pairs, all in `Test_imports_of` |
| `bin/seal pr-body seal/threads/1794401941-payload-calibration-reached-by-tests-alone --body <scratch>/pr-body-probe.md` | exit 0, body written to scratch |
| `python3 skills/code-review/scripts/chain_check.py --baseline 52f87b8d3 --root <worktree> --worktree`, before the record | exit 0; names no round record, no gate record and no guarantee, and no notice on `frame/design.md` |
