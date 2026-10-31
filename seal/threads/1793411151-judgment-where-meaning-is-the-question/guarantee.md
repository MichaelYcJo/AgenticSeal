# Guarantee: 1793411151-judgment-where-meaning-is-the-question

| Field | Value |
|---|---|
| Target SHA | 083b6289 against f80f48e6; earlier run: ff6eb5a9 withheld |
| Broad gate | dae46f8d against f80f48e6 |

The base `release/v0.26.0` resolved through `origin/release/v0.26.0` to
`f80f48e6`; `release/v0.26.0@{upstream}` answered nothing (executed, `git
rev-parse --verify --quiet`). `trail/gate.md` names one run, `dae46f8d
against f80f48e6`, an ancestor of HEAD (`git merge-base --is-ancestor`, exit
0, executed). `git log --no-merges --name-only dae46f8d..HEAD ^f80f48e6`
names three commits, each touching one path under
`seal/threads/1793411151-judgment-where-meaning-is-the-question/`:
`ff6eb5a9` `trail/gate.md`, `e44b4bd6` `guarantee.md` and `083b6289`
`frame/plan.md` (executed). The run's counts, 6,208 passed and 11 skipped
with the chain check at exit 0, are the gate's own log as the orchestrator
kept it (read). No `seal/parity.md` is in git, so no `original:` line is
owed (executed, `git ls-files`).

`bin/seal pr-body seal/threads/1793411151-judgment-where-meaning-is-the-question
--body <scratchpad>/1793411151-judgment-where-meaning-is-the-question/pr-body.md
--check`, the tree's command at `083b6289`, exited 0: "below `## From the
records` is the records' text" (executed).

This is the second audit. The earlier one, at `ff6eb5a9`, withheld on two
claims of the orchestrator's: no row in `frame/plan.md` *Judgments of the
run* for round 10's route, and "2 of 18" in the body. Since `ff6eb5a9` only
`frame/plan.md` changed outside this file, so only claims whose coordinates
it holds were re-run; the sample below the line is the earlier audit's,
carried with its results, against code no commit since has touched.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| `083b6289` adds one row for round 10's `regression: round-9#2` routed to a fix pass, and the table holds sixteen rows | the coordinator's re-audit request; `frame/plan.md:92` | `git show 083b6289`; `sed -n '/^## Judgments of the run/,$p' frame/plan.md \| grep -c '^\| 2026'` | holds: one line added and none removed; 16 rows (executed) |
| The body's figure is "3 of 18" and its text "sixteen rows" | the body's first part, lines 14 and 29 | `grep -n` over the body file | holds (executed); 3 matches round-1#6, round-2#1 and round-9#3, the earlier audit's count |
| Carried: the seven `seen red` claims of phases 2 to 5, each re-run against its script restored from `f80f48e6` in a clone at `ff6eb5a9`, and passing at HEAD's code | `trail/phases/phase-2.md:73-84`, `phase-3.md:113-122`, `phase-4.md:57-63`, `phase-5.md:83-88` | as the earlier audit at `e44b4bd6` lists them | held at `ff6eb5a9` (executed then); no commit since touches a script or a test |
| Carried: the `original_of` mutant red; `core.output` 8,655 characters against the cap of 10,000; `seal rules --check` exit 0 over 265 lines; nothing of `## Removes` standing outside `docs/` | `trail/phases/phase-2.md:86-98`, `phase-1.md:52-56`, `phase-4.md:104-105`, `frame/design.md:315-332` | as the earlier audit lists them | held at `ff6eb5a9` (executed then); unchanged since |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | scripts read one spelling and name what they did not read; the core lists the invariants; the cap, the regression route and the leftover homes read as guidance; the orchestrator's judgments get `frame/plan.md` *Judgments of the run*, read by the settle; #1170 built, #1121 R9 and R11 built and R3 a limit, #1125 decided as a limit; `docs/` lands at the settle | the issue: its direction (2026-10-29) asks for naming over grammar, and its *Order* says 0.25.1's reader fixes are closed or kept against the result, which Table D does; the build; the Removes (read) | none |
| the build | the diff `f80f48e6...HEAD` and the five phase records: the five readers changed, the core's Table B, the guidance in `skills/code-review/orchestration.md`, the template section and the dry run's *The judgments* | the design's Scope items 1 to 3 and 5 to 14, item 4 moved to #1197 as `frame/plan.md:78` records; every sampled claim re-ran as recorded | none |
| the last round | round 11 opens nothing and confirms round-10#1 at `58d9c003` | the build at `20160b89`; the two cases and the docstring are in the tree (read, `tests/skills/test_settle.py:1061-1099`) | none |
| the changelog | the dry run's judgments added; the readers name instead of refusing; the cap and the second regression read as judgments; four process changes, among them the orchestrator writing each judgment of a run, a regression's route among them, as a row | the build, line for line; the plan's table, which now holds a row for each regression route of the run, round 4's at `:83` and round 10's at `:92` (read) | none |
| the orchestrator's part of the pull request body | the sixteen rows of `frame/plan.md` *Judgments of the run* are its judgments of this run; 3 of 18 findings are located under `seal/threads/` alone; the other figures, the version move and the merge order | the plan's sixteen rows; the round records' 3 of 18; 44, 13, 6, 6 and 1 commits by kind; 3,672 of 5,791 lines; 18 findings by round; the gate's 6,208 and 11; `plugin.json` at `0.26.0` (executed) | none. Its "70" commits is the count to the gate record, as its wall-clock row's frame says; the branch now holds 72 with the two record commits after it (read) |

Round 10's route holds against the rule in force on this branch. Its grounds
(`trail/rounds/round-10.md:44-46`) say the defect came from round 9's
paste-ready grounds taken as written, the routing table's second row; the
unit had no earlier regression in the run, so neither the branch's third row
nor `docs/the-review-record.md` *The run*'s second-regression route applies.
The row at `frame/plan.md:92` now records that judgment with those grounds
and the section it stands on (read). The tokens row of the body is
`unverified` here; its answerer is the orchestrator, who read the transcripts.

Verdict: sealed
