# Implementation Plan: a measurement no record asks for closes its row (#1045)

## Technical context

The work changes one step of the settling session's procedure, one constant of the dry run, two test modules, and one policy sentence through `frame/design.md` *Rule changes*.

- `skills/settle/SKILL.md` *The settling session's procedure* step 6, lines 272 to 294 at `0633f9a5`: the kinds table (277 to 279), the order paragraph (281 to 283) and the re-home paragraph (285 to 288). The paragraph at 290 to 294, on the files the dry run names as not read, decides "by the same table" and reads the new kind with no edit.
- `skills/settle/scripts/settle.py#ROWS_HEADING`, lines 434 to 438. `#report` prints it once above the open rows (line 1121). No other code reads its words.
- `tests/skills/test_settle.py#Test_module::test_the_dry_runs_headings_say_who_decides`, line 2405, pins the three-kind phrase. The cases at lines 592, 882 and 1532 split the report on the constant by name and do not change.
- `tests/text/test_settle_reads_before_it_removes.py` holds the cases that read the skill (#1033's S11). The new order case goes there, beside `#test_the_skill_states_the_settling_sessions_procedure`, whose docstring changes (design G5).
- `docs/the-record-layout.md` lines 98 to 118: the policy paragraph. The settle after the release writes it from the design's `change`.

Framing executed probe P1 under `<scratchpad>/1793580304-a-measurement-no-record-asks-for-closes-its-row/frame/`: a `git clone --no-local` of the worktree at `0633f9a5` with this design copied in, and a `test_tmp_p1.py` that loaded `rule_changes.py` and `settle.py` from the clone. `rule_changes.py#parse` returned one `change` with `errors=[]` and `unread=[]`. `settle.py#facts` returned `from` found and `to` not found in *The fold, and what tells it from a deletion*. The directory was removed after the run.

Framing executed `gh issue view <N> --json number,state,stateReason` for #1061 to #1087: 22 closed as not planned, 2 closed as completed, 3 open (design G9).

Neither hook-run script loads a module this work adds or changes. `settle.py` runs through `bin/seal`, and the work adds no import, so `tests/hooks/test_launch.py` has nothing new to read. A test class may change, so `bin/seal layout --check tests` applies.

Failure scenarios of the chosen approach, six months on:

- A settling session closes a row as *a measurement no record asks for* when an open issue or a failed run did wait on it. The record that waits still stands, so the measurement is not lost. The settle's pull request body lists each row by kind with its reason (step 11), and the owner reads it before the merge. No script can tell a sound reason from a thin one, because what waits on an answer is meaning (design G7).
- A session reads "nothing on record" as "nothing I found" and closes rows without opening the records a row names. The reason cell owes what the answer would have decided, so a reason that names nothing is visible to the owner at the settle's pull request.
- A later edit adds a fifth kind to the table and forgets the dry run's heading. The order case pins the skill's table and the heading pin pins the constant, and neither compares the two. The heading's reader is a person running `seal settle` (design G15), and a heading one kind short misleads that reader until the next settle reads the skill. A case comparing the two would be a mechanism with no catch on record (A3 below).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 A fourth kind, *a measurement no record asks for*, before *a measurement nobody has taken* in step 6's table. The settling session decides it, the dry run's heading names the four kinds, a case pins the table's order, and the policy sentence changes through `## Rule changes` | The three in *Technical context* | Chosen. It is the owner's decision of 2026-10-27 (design G8), and it states for an open row the rule #1276 states for a reading past its band (design G11) |
| A2 Keep the structure: three kinds, and every measurement nobody has taken is re-homed | The 0.22.4 settle opened 27 issues under it and 22 closed as not planned (design G9). Each costs the owner a reading and a close, and the count of open measurement issues then says less than it seems to | Rejected. The premise that keeps it is that every unmeasured row has something waiting on its answer. Checked against #1061 to #1087, it held for at most 5 of 27 |
| A3 The dry run's heading cites step 6's table instead of naming the kinds, so the kinds have one source (#1148's first principle, design G10) | A person runs `seal settle` from the README's cheat sheet (design G15) and reads the heading without the skill open. A heading that only cites a table tells that reader nothing about what each row can become. The issue's *Done when* asks that the dry run offer the new kind | Rejected. The heading already names the kinds and is pinned under contract rule 14. The work keeps that structure and writes it in place |
| A4 The dry run proposes a kind per row, for instance a row naming no issue number and no run as *no record asks for* | A row whose measurement an issue waits on, with no `#N` in its own text, is proposed for closing. A row that names an issue already closed is proposed for re-homing. The script would re-encode a meaning judgment as a grammar rule | Rejected under `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* (design G7) |
| A5 Close every unmeasured row with its reason, and never re-home one | A measurement a failure waits on loses its home, such as the issues of #1061 to #1087 the owner kept open on 2026-10-27 (design G9). The rule then trades issues nobody needs for measurements nobody remembers | Rejected. The issue keeps re-homing for a measurement something on record needs |
| A6 The new kind after *a measurement nobody has taken* | A row takes the first kind that fits, so every unmeasured row would still be re-homed and the new kind would never be reached | Rejected. The issue places it before |
| A7 A new column on `## Not verified` rows, written by the row's writer, saying what waits on the answer, so the settle reads it exactly | The writer writes the row at build time and cannot know what will be on record at the settle. The column is a mark on every row of every record, with a template change and a reader to keep. It caught nothing on the day it is added | Rejected under `skills/core/SKILL.md` *The rule a mechanism is kept against*, and #1148's direction that marks are kept to the minimum |
| A8 The policy sentence names the kinds and not their order | The order is what decides that a measurement no record asks for closes before it can open an issue. The issue names the policy document as a home of the order | Rejected. The `to` says the order in one sentence |
| A9 The re-homed issue's body stays as it is: each row's work item, text and answerer | The issue's next reader cannot see what waits on its answer, and re-judges it the way the owner re-judged #1061 to #1087 | Rejected. The body also names the record that needs each row's answer, which is the grounds of the kind (`skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both*) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 1 to 6, and the work item's `changelog.md` with its *Process changes* row | The order case seen red against step 6's table at `0633f9a5`, and the heading pin seen red against `ROWS_HEADING` at `0633f9a5`, each shown as contract rule 15 asks. Narrow, in one command: `tests/skills/test_settle.py`, `tests/text/test_settle_reads_before_it_removes.py`, and every module `git grep -l` lists for `skills/settle/SKILL.md`, `settle.py` or `seal/threads` that the crafter judges reads a changed path, among them `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_unverified_rows_close.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/github/test_rules.py` and `tests/text/test_a_document_has_room_for_the_next_fold.py`. `bin/seal layout --check tests`. `tests/hooks/test_launch.py` does not apply (*Technical context*). The suite is the orchestrator's broad run | `15eb84523` |

## Operational impact

None. No migration, environment variable or dependency. The dry run's heading above the open rows reads differently; nothing parses its words. A settling session from this release on closes a measurement no record asks for in its record and opens no issue for it.

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
