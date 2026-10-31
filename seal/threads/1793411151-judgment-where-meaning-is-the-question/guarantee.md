# Guarantee: 1793411151-judgment-where-meaning-is-the-question

| Field | Value |
|---|---|
| Target SHA | ff6eb5a9 against f80f48e6 |
| Broad gate | dae46f8d against f80f48e6 |

The base `release/v0.26.0` resolved through `origin/release/v0.26.0` to
`f80f48e6`; `release/v0.26.0@{upstream}` answered nothing (executed, `git
rev-parse --verify --quiet`). `trail/gate.md` names one run, `dae46f8d
against f80f48e6`, an ancestor of HEAD (`git merge-base --is-ancestor`, exit
0, executed). `git log --no-merges --name-only dae46f8d..HEAD ^f80f48e6`
names one commit, `ff6eb5a9`, touching only
`seal/threads/1793411151-judgment-where-meaning-is-the-question/trail/gate.md`
(executed). The run's counts, 6,208 passed and 11 skipped with the chain
check at exit 0, are the gate's own log as the orchestrator kept it (read).
No `seal/parity.md` is in git, so no `original:` line is owed (executed,
`git ls-files`).

`bin/seal pr-body seal/threads/1793411151-judgment-where-meaning-is-the-question
--body <scratchpad>/1793411151-judgment-where-meaning-is-the-question/pr-body.md
--check`, the tree's command at HEAD, exited 0: "below `## From the records`
is the records' text" (executed).

## Claims re-run

Each `seen red` was run in `<scratchpad>/1793411151-judgment-where-meaning-is-the-question/at-base/`,
a `git clone --no-local` at `ff6eb5a9` with the named script restored from
`f80f48e6`, then restored to HEAD and run again; the clone was removed after.

| Claim | Source | Command | Result |
|---|---|---|---|
| The first scenario's case failed against the near-miss refusal "a label in another spelling"; the third scenario's guarantee case failed because the misspelt `original:` counted as present and the arm exited 0, and `round_of` refused the line; the second scenario's case failed on the missing `UNREAD_FILE` | `trail/phases/phase-2.md:73-84` | `chain_check.py` from `f80f48e6`: `bin/test tests/skills/test_chain_check.py -q -p no:xdist -k "test_a_verdict_in_another_spelling_leaves_its_finding_without_one or test_refuses_a_direct_guarantee_whose_only_original_is_misspelt or test_a_line_spelt_otherwise_is_no_original_line or test_names_a_record_under_another_name_and_keeps_the_exit"` | holds: 4 failed, on "a label in another spelling: the check reads `verdict:`", on `assert 0 == 1`, on "a label in another spelling: the check reads `original:`" and on `no attribute 'UNREAD_FILE'`; at HEAD 4 passed (executed) |
| `original_of` counting a line that opens like `original:` is red | `trail/phases/phase-2.md:86-98`, the mutation's last break | `bin/seal mutate skills/code-review/scripts/chain_check.py --replace "    at = [i for i, line in enumerate(lines) if label_of(line) == ORIGINAL_ROW]" "    at = [i for i, line in enumerate(lines) if label_of(line) == ORIGINAL_ROW or opens_like(line) == ORIGINAL_ROW]" --tests "bin/test tests/skills/test_chain_check.py -q -p no:xdist -k 'Test_original_of or Test_originals_of'"` | holds: `red`, 2 failed and 14 passed, the two #1121 R9 cases (executed) |
| The tab-indented block failed on `tests: resolves`, and the U+2028 row failed | `trail/phases/phase-4.md:57-63` | `deferral_check.py` from `f80f48e6`: `bin/test "tests/skills/test_deferral_check.py::Test_main::test_the_output_is_the_same_whatever_the_trigger" -q -p no:xdist` | holds: 5 failed, `[a-block-indented-by-a-tab]` on `tests: resolves`, `[a-line-separator-in-a-comment]` among them; at HEAD 5 passed (executed) |
| The `rules.py` render case failed on the line printed as refused | `trail/phases/phase-3.md:117-119` | `.github/scripts/rules.py` from `f80f48e6`: `bin/test tests/github/test_rules.py -q -p no:xdist -k test_a_line_not_read_is_printed_as_one_and_holds_nothing` | holds: 1 failed, "refused: `Enforced by: tests/test_x.py` is no check line"; at HEAD 1 passed (executed) |
| The four closing-word rows failed on their refusal | `trail/phases/phase-3.md:113-114` | `unverified_check.py` from `f80f48e6`: `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -k test_accepts_open_rows_and_the_word_that_closes_one` | holds: 4 failed, the full stop, colon, capitalised and upper-case rows, 6 passed; at HEAD 10 passed (executed) |
| The beside case failed on the second-header refusal | `trail/phases/phase-3.md:120-122` | `pact_check.py` from `f80f48e6`: `bin/test tests/skills/test_pact_check.py -q -p no:xdist -k test_grades_the_exact_table_and_names_a_near_one_beside_it` | holds: 1 failed, "REFUSED ... the frame holds a second `\| Pact \| Clause \| Hash \|` header", `assert 2 == 0`; at HEAD 1 passed (executed) |
| The judgments cases failed on the missing constants | `trail/phases/phase-5.md:83-88` | `settle.py` from `f80f48e6`: `bin/test tests/skills/test_settle.py -q -p no:xdist -k "test_the_judgments_are_printed_by_the_document_each_stands_on or test_refuses_to_read_rows_under_a_heading_near_the_judgments_section"` | holds: 4 failed, `no attribute 'JUDGMENTS_HEADING'`; at HEAD 4 passed (executed) |
| The core printed by the hook stays under `hooks/lib/core.py#CAP` | `trail/phases/phase-1.md:52-56` (8,017 at phase 1) | in the clone at HEAD, `python3 -I` calling `core.output(root, root)` and `len` | holds: 8,655 characters against a cap of 10,000, the header carrying the clone's path; the figure grew with round 1's fixes (executed) |
| `seal rules --check` holds every check line | `trail/phases/phase-4.md:104-105`, `trail/phases/phase-5.md:110-111` | `bin/seal rules --check` in the clone at HEAD | holds: exit 0, "all 265 check lines in 54 rule files hold" (executed) |
| Nothing of the `## Removes` rows and the changelog's removals stands in the tree: `OLD_COLUMNS`, `old_spelling`, `OLD_SPELLINGS`, `misspelt`, `spelt_otherwise`, `MEANT`, `MEANT_VERDICT`; the trigger reading and the outcomes `too late` and `wrong trigger`; `NEAR_CLOSED`; the extension line; the hard second-regression route; "first rung that fits" outside `docs/`; the writing-style sentence | `frame/design.md:315-332`; `changelog.md` *Changed* | `grep -nE` over `chain_check.py`, `pact_check.py`, `rule_changes.py`, `rules.py`, `unverified_check.py`, `deferral_check.py`; `git grep` over `skills`, `agents`, `templates`, the READMEs | holds: none stands. `SPELT`, `header_key`, `NEAR` and `NEAR_NOTHING` remain only as the nets that name a line and as the base reading phase 3 kept, as the rows say. The `docs/` rows are `## Rule changes` items, pending the settle (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | scripts read one spelling and name what they did not read; the core lists the invariants; the cap, the regression route and the leftover homes read as guidance; the orchestrator's judgments get `frame/plan.md` *Judgments of the run*, read by the settle; #1170 built, #1121 R9 and R11 built and R3 a limit, #1125 decided as a limit; `docs/` lands at the settle | the issue: its direction (2026-10-29) asks for naming over grammar, and its *Order* says 0.25.1's reader fixes are closed or kept against the result, which Table D does; the build; the tree's Removes (read) | none |
| the build | the diff `f80f48e6...HEAD` and the five phase records: the five readers changed, the core's Table B, the guidance in `skills/code-review/orchestration.md`, the template section and the dry run's *The judgments* | the design's Scope items 1 to 3 and 5 to 14, item 4 moved to #1197 as `frame/plan.md:78` records; every sampled claim above re-ran as recorded | none |
| the last round | round 11 opens nothing and confirms round-10#1 at `58d9c003` | the build at `20160b89`; the two cases and the docstring are in the tree (read, `tests/skills/test_settle.py:1061-1099`) | none of its own. It names `20160b89`'s one plan row and does not remark that round 10's route has none |
| the changelog | the dry run's judgments added; the readers name instead of refusing; the cap and the second regression read as judgments; four process changes, among them "The orchestrator writes each judgment of a run, ... a regression's route, ... as a row" | the build, line for line (read) | the plan's table: round 10's regression route is a judgment of this run and has no row |
| the orchestrator's part of the pull request body | the fifteen rows of `frame/plan.md` *Judgments of the run* are the orchestrator's judgments of this run; "Findings whose every `location:` is under `seal/threads/`: 2 of 18"; the other figures, the version move and the merge order | 70 commits as 44, 13, 6, 6 and 1 by kind; 3,672 of 5,791 lines added under `seal/threads/`; 18 findings, 6, 1, 2, 1, 0, 3, 0, 1, 3, 1, 0 by round; 10:45 to 14:45; the gate's 6,208 and 11; `plugin.json` at `0.26.0` (executed) | (1) `trail/rounds/round-10.md:35-36` routes `regression: round-9#2` to a fix pass, and `frame/plan.md:75-91` holds no row for that route, where `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, as this build writes it, says "Each route is a judgment, and you write it as one row of that table"; round 4's route has its row at `frame/plan.md:83`. (2) Three findings are located under `seal/threads/` alone, not two: round-1#6, round-2#1 and round-9#3 (`trail/rounds/round-9.md:238`) |

The route itself holds against the rule in force on this branch. Round
10's grounds compare the fix with the frame: the defect "came from round
9's paste-ready grounds, which named the fence as the one edge, and the fix
took them as written" (`trail/rounds/round-10.md:44-46`), the second row of
the routing table, an ordinary fix pass. The unit, the near-heading scan in
`settle.py#judgments`, had no earlier regression in this run; round 4's was
`chain_check.py`'s `original:` naming. So neither the branch's third row nor
`docs/the-review-record.md` *The run*'s "A second regression on the same unit
after a fix-pass route goes to the framer whatever the comparison says"
applies (read). What does not hold is the record of that judgment: the
table this work adds and the rule it ships say the route is a row, and the
body names the table as the whole of the run's judgments.

Both repairs are in the work item's records and the body's first part:
one row in `frame/plan.md` *Judgments of the run* for round 10's route, and
"3 of 18" in the body's table.

Verdict: withheld reason: the orchestrator's account of its run does not hold at two coordinates. (1) `frame/plan.md` *Judgments of the run* (`:75-91`) holds no row for round 10's route of `regression: round-9#2` (`trail/rounds/round-10.md:36`) to a fix pass, which `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* says is written as one row, while the pull request body's first part names those fifteen rows as the orchestrator's judgments of the run. (2) The body's first part says 2 of 18 findings are located under `seal/threads/` alone; the round records give 3: round-1#6, round-2#1 and round-9#3 (`trail/rounds/round-9.md:238`).
