# Design: a measurement no record asks for closes its row (#1045)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 `docs/the-record-layout.md` *The fold, and what tells it from a deletion*, the paragraph opening **A released work item leaves at the settle whatever it wrote** (lines 98 to 118 at `0633f9a5`, read) | This is the policy document that states the kinds of an open row: moot, answered, and "a row naming a measurement nobody has taken is re-homed as an issue, or as a `seal/follow-up.md` row in a repository with no tracker". It holds no fourth kind and no order. The work changes that sentence through `## Rule changes`, and a pull request does not edit `docs/` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |
| G2 `skills/settle/SKILL.md` *The settling session's procedure* step 6 (lines 272 to 294 at `0633f9a5`, read) | The step's table has three kinds in this order: moot, answered, a measurement nobody has taken. A row takes the first kind that fits. The paragraph under it re-homes every measurement as one issue per distinct measurement. #1054 renumbered the steps (PR #1284), so the issue's `:189-193` at `0b75346f` is stale, and this is the table's place now |
| G3 `skills/settle/scripts/settle.py#ROWS_HEADING` (lines 434 to 438, read) | The dry run prints one heading above every open row: "for the settling session to decide as moot, answered or a measurement to re-home". The dry run decides no row's kind. Per row it prints the item and whether each backticked path is in the working tree (`settle.py#open_rows`, `#report` lines 1120 to 1129) |
| G4 `tests/skills/test_settle.py#Test_module::test_the_dry_runs_headings_say_who_decides` (line 2405, read) | It pins "moot, answered or a measurement to re-home" in `ROWS_HEADING`, under contract rule 14. The heading's new text moves this pin with it in the same commit |
| G5 `tests/text/test_settle_reads_before_it_removes.py#test_the_skill_states_the_settling_sessions_procedure` (lines 65 to 73, read) | Its docstring says "The steps, their order and the row kinds are the proofer's to read" (#1033). The order of the kinds is now pinned by a case, so that docstring sentence is rewritten in the same commit (contract rule 19). Its one assert, "`seal/follow-up.md` row", still holds |
| G6 `docs/what-a-script-gates.md` *the cases under `tests/text/` and `tests/behaviour/` that read prose* row (line 53, read) | "A case pins a fact a reader acts on; one that pins wording goes." The table's order is such a fact: it decides which kind a row takes. The case reads the order of the four kinds and pins no sentence |
| G7 `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* (read) | Whether a failure, a report or a decision on record depends on a measurement's answer is meaning, read from the row and the records it names. The settling session decides it. The dry run prints the kinds in the table's order and proposes none for a row. Nothing the dry run reads exactly tells such a row apart: a `## Not verified` row is `| Item | Who must answer |` (`templates/records/sdd-gaps.md`), and neither cell says what waits on the answer |
| G8 The owner's decision of 2026-10-27, in issue #1045's body (read through the orchestrator's spawn; `gh` reads the issue here, executed `gh issue view 1045 --json title,state,body,comments`, 2 comments) | Builds on it. Not every unmeasured row is an issue. A fourth kind closes the row in its record with the reason and opens nothing, and it sits before *a measurement nobody has taken* in the table's order |
| G9 The 0.22.4 settle's 27 re-homed issues, #1061 to #1087 (executed: `gh issue view <N> --json number,state,stateReason` for each, 2026-11-02) | 22 are closed as not planned, 2 closed as completed, and 3 are open. The issue body counts 20 not planned and 2 folded into other issues, which together are the 22. This is the catch record of the clause the work narrows (`## Removes`) |
| G10 #1148, merged as PR #1194 in 0.25.1 (executed: `gh pr view 1194 --json title,mergedAt,baseRefName,body`, and `gh issue view 1148`) | Builds on it, and does not re-decide it. #1148 item 4 decided the rest of #1045's first scope: "A `fixed` finding located in, and fixed in, the work item's own records alone owes no verifying round", and the divergence table of `gaps.md`. Its first principle, one source, is weighed for the dry run's heading in `plan.md` A3 |
| G11 #1276, the band rule of #1263, pending as `seal/threads/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/design.md` `## Rule changes` item 1 (an `add` to `docs/measuring-a-run.md` *What a measurement must survive, and what it must not invent*, read) | Builds on it. "An issue follows a reading judged `worse` so ... and none follows a reading whose only ground is its band." This work states the same rule for an open row at the settle: an issue follows a measurement something on record needs, and none follows a row whose only ground is that nobody took the measurement |
| G12 #1269, the 0.27.x settle (executed: `gh pr view 1269`, read its body) | Builds on it, and leaves its defaults where they stand. That settle re-homed 16 rows, grouped rows one event answers into one issue per event, and re-homed a row whose measurement an open issue already holds by a comment on that issue. Those are the settling session's defaults, and #1281 is the work that reads earlier settles' judgments. The new kind closes a row before any of them applies |
| G13 #1054, merged as PR #1284 (read: `seal/threads/1793573496-the-settle-folds-named-directories-the-person-marks/frame/design.md` `## Rule changes`) | Its `add` lands at the end of the same section of `docs/the-record-layout.md`, earlier in merge order. It leaves this work's sentence as it stands, so the `from` below reads the same before and after it. The settle reads both in one group |
| G14 #1217 and #1281 (executed: `gh issue view 1217`, `gh issue view 1281`) | Both follow this work in 0.28.0 and edit `skills/settle/SKILL.md`. #1217 adds `seal settle --draft`, and #1281 reads earlier settles' judgments. Neither is built here |
| G15 `README.md:265` and `README.ko.md:259`, the `seal settle` cheat-sheet rows (read) | A person runs `seal settle` and reads its output. Each row says the dry run lists every open row and names no kind, so neither changes |
| G16 Probe P1 (executed, `plan.md` *Technical context*) | `rule_changes.py#parse` reads this design's `## Rule changes` as one `change` with no error, and `settle.py#facts` finds its `from` in its section at `0633f9a5`, and does not find its `to` |

## Scope

In:

1. `skills/settle/SKILL.md` *The settling session's procedure* step 6. The table gains the kind **a measurement no record asks for** between *answered* and *a measurement nobody has taken*, and *a measurement nobody has taken* covers only a measurement something on record needs. The rows read as `## Data & interfaces` gives them.
2. The same step's order paragraph says why the new kind comes before re-homing: a measurement no record asks for is closed before it can open an issue.
3. The same step's re-home paragraph names a measurement something on record needs as the one re-homed, and adds the record that needs each row's answer to the issue body it lists.
4. `skills/settle/scripts/settle.py#ROWS_HEADING` names the four kinds in the table's order. It proposes no kind for a row.
5. `tests/skills/test_settle.py#Test_module::test_the_dry_runs_headings_say_who_decides` pins the heading's four kinds in place of the three.
6. A case in `tests/text/test_settle_reads_before_it_removes.py` reads step 6's table and pins the order of its four kinds. The docstring of `#test_the_skill_states_the_settling_sessions_procedure` drops "their order and the row kinds" from what it leaves to the proofer, since the new case holds the order.
7. `docs/the-record-layout.md` *The fold, and what tells it from a deletion* states the fourth kind and the order, through `## Rule changes` below.

Out:

- Whether a row's kind is proposed per row by the dry run. Whether something on record waits on an answer is meaning (G7), so no script reads it.
- The settling session's defaults for grouping re-homed rows into issues, and for commenting on an open issue (G12). #1281 reads earlier settles' judgments.
- `seal settle --draft` (#1217).
- A verifying round for a records-only fix, and `gaps.md`'s divergence table. #1148 decided both (G10).
- Re-judging the three still-open issues of #1061 to #1087. The owner reviewed all 27 on 2026-10-27 (G8, G9).
- Who writes a `## Not verified` row and what it holds. The crafter's and sealer's rows are unchanged. The new kind is applied at the settle only.
- `README.md` and `README.ko.md` (G15), and `.claude-plugin/plugin.json`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A row no record asks for is closed | Given an open `## Not verified` row of a released record that names a run on a platform no failure, issue, finding or rule on record points to, when the settling session decides it at step 6, then it takes the kind *a measurement no record asks for*, is closed in its record with `closed` and the reason, and no issue and no `seal/follow-up.md` row is opened for it | check: none reader: the proofer at review, and the owner at the next settle's pull request, whose body lists each row by kind |
| S2 A row a record needs is still re-homed | Given an open row whose measurement an open issue, a failed run or a rule on record waits on, when the settling session decides it, then it takes *a measurement nobody has taken* and is re-homed to an issue whose body names the record that needs the answer | check: none reader: the proofer at review, and the owner at the next settle's pull request |
| S3 The dry run offers the new kind | Given a released record with an open row, when `seal settle` runs, then the heading above the open rows names moot, answered, a measurement no record asks for, and a measurement to re-home, in that order | check: tests/skills/test_settle.py |
| S4 A case pins the table's order | Given `skills/settle/SKILL.md` step 6, when its table's kinds are read in order, then they are moot, answered, a measurement no record asks for, a measurement nobody has taken. The case fails against the base's three-kind table | check: tests/text/test_settle_reads_before_it_removes.py |
| S5 The policy change parses | Given this design, when `chain-check` reads its `## Rule changes` at the pull request, then it reads one `change` and refuses nothing, and the settle finds its `from` in its section | `chain-check` reads it at the pull request through `skills/settle/scripts/rule_changes.py`; probe P1 ran the same reader at framing (G16) |

## Data & interfaces

Step 6's table, as the build writes it. The cells carry the decision; the wrap and the commas are the crafter's.

| The row is | When | What closes it |
|---|---|---|
| moot | it names a unit the tree no longer holds | the coordinate showing the unit gone |
| answered | another record or a later run already answered it | that record or run, named |
| a measurement no record asks for | it names a run, a platform or a reading no record holds, and no failure, report or decision on record depends on its answer | the reason, naming what the answer would have decided; nothing is opened |
| a measurement nobody has taken | it names a run, a platform or a reading no record holds | the issue it is re-homed to |

"On record" means a record that outlives the settle and rests on the answer: an open issue, a failed run, or a rule or design of another work item. The row's own work item is not such a record, its design, questions and rounds among them, because `--apply` removes its directory and nothing in it can wait on the answer; the row's own `Who must answer` cell is not one either.

`settle.py#ROWS_HEADING` changes its text only. No function, argument or output line changes, and the three cases that split the report on the constant (`tests/skills/test_settle.py` lines 592, 882 and 1532) read it by name.

## Rule changes

- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: names that record; a row naming a measurement nobody has taken is re-homed
    as an issue, or as a `seal/follow-up.md` row in a repository with no
    tracker.
  to: names that record; a row naming a measurement no failure, report or
    decision on record depends on is closed with that reason and opens
    nothing; and a row naming a measurement something on record needs is
    re-homed as an issue, or as a `seal/follow-up.md` row in a repository
    with no tracker. A row that fits more than one kind takes the first
    that fits, in this order, so only a measurement something on record
    needs opens an issue. An issue nothing on record waits on costs its
    reader a reading and a close.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The duty to re-home every measurement nobody has taken as an issue. Its catch record: the 0.22.4 settle opened 27 issues under it, and 22 of them closed as not planned (G9) | `skills/settle/SKILL.md` *The settling session's procedure* step 6, the row *a measurement nobody has taken* and the paragraph under the table | The row and paragraph are rewritten in place to cover a measurement something on record needs. A measurement nothing waits on is closed in its record with its reason, which the settle's pull request body lists |
| The same duty as policy | `docs/the-record-layout.md` *The fold, and what tells it from a deletion* | `## Rule changes` above, written by the settle after the release |
| The three-kind phrase of the dry run's heading and its pin | `skills/settle/scripts/settle.py#ROWS_HEADING`, `tests/skills/test_settle.py#Test_module::test_the_dry_runs_headings_say_who_decides` | Rewritten in place to the four kinds |
| "their order and the row kinds" in what the docstring leaves to the proofer | `tests/text/test_settle_reads_before_it_removes.py#test_the_skill_states_the_settling_sessions_procedure` | The new case holds the order. What each kind means stays the proofer's |

The work adds a kind to a rule, and the kind is a narrowing: it takes out the issues the old clause opened with nothing on record behind them. It adds no gate, check, hook, mark or line grammar. The one case it adds pins the order the issue's *Done when* names.

Framed 2026-11-02 by framer, before the build.
