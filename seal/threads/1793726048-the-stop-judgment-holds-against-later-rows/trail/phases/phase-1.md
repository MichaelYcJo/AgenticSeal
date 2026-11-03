# Phase 1: 1793726048-the-stop-judgment-holds-against-later-rows

## What this phase found

**The frame holds at every coordinate it builds to, with two line ranges
that end one line early.** At `bf9f6998e`, the stop paragraph and its table
stood at `skills/code-review/orchestration.md:133-154`, not `:133-153` as
`frame/design.md` G4 and *Scope* item 1 and `frame/plan.md` *Technical
context* state: "and commit the close blocks of that step together." is
line 154. The proofer's group rule stood at `agents/proofer.md:136-140`,
not `:136-139` as *Scope* item 4 states: its last sentence ends at line
140. The drain row stood at `skills/implement/orchestration.md:480`, the
bullet at `skills/code-review/SKILL.md:127-131`, the *Regression test* row
at `:84`, and `docs/running/the-run.md:17` and `:48` as G5 states (executed,
one `grep -n` per coordinate). The text at each range is the text the frame
describes, so the build rewrote it as the frame says. Every line number
in the frame is a coordinate of the base, and the lines after `:154` and
`:131` moved down at HEAD. The hand-back names both ranges for the
orchestrator to fold.

**S7's chain check reads nothing new for this design before or after the
edits (executed).** `python3 skills/code-review/scripts/chain_check.py
--baseline release/v0.31.0 --root . --worktree` printed, at `bf9f6998e` and
over the edited tree, the three lines a work item with no round, no gate
record and no guarantee prints, no pin notice and no copy notice, and exited
0. To show that the copy reading can fail here, one `bin/seal mutate` run
appended the `to`'s second sentence to the new paragraph of
`skills/code-review/orchestration.md` that opens "A fix that changes no
assertion owes no round of its own". A script in the scratch directory
ran the same command and exited 1 on a copy or pin notice. The baseline
passed, and the mutant went red with "this `to` repeats a passage of
`skills/code-review/orchestration.md`: 24 of its runs of 15 words stand
there". The file was restored from the command's own copy, and `git
status` was clean after it. The spawn prompt asked that the new sentences
share no 15-word run with the `to`. To keep them clear of it, the drain
row's new clause reads "Once a row ... judges the run excessive", not the
`to`'s "After a row ... has judged the run excessive".

**Five decisions of wording, each judged against the frame and
`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게
쓴다*.**

- *Scope* item 1's six points are three edits. Points 1 and 2 are a
  sentence before the table and the table's new row *What the next round
  can catch*. Point 3 is a paragraph of its own after the table, so the
  table's cells stay the weighing and the paragraph says what the weighing
  gives. Points 4, 5 and 6 are a new paragraph after "commit the close
  blocks of that step together.", with the bold lead **A row that judges
  the run excessive binds every row after it.** The section's earlier
  sentences stand as they were. That keeps "as one row of `frame/plan.md`
  *Judgments of the run*", which
  `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrators_run_judgments_are_rows_of_the_plan`
  reads (G15).
- Point 4 lists a fix confined to the work item's records beside rungs 2,
  3 and 4, and says "The orchestrator spawns no fix pass for such a
  finding". The text puts the clause about no fix pass on the rung 2, 3 and
  4 branch alone. A records-only fix has a writer, and the sealer reads it,
  as the section's opening paragraph says. Read the other way, the clause
  would leave a records-only fix with no party to write it.
- Point 6's "its round is owed as G2 says" is written as the invariant it
  cites: a round reads that repair unless it touched only the work item's
  records, as the table of `skills/core/SKILL.md` *Judgment is not licence
  to skip a party* holds. G2 is a frame row, and the skill outlives the
  frame.
- *Scope* item 3's fourth point says "one sentence of its prose". The
  bullet says "of its prose outside `## Findings`". `chain_check.py`
  reads each `### <n>.` heading under `## Findings` as a finding, so a
  sentence there could be read as one.
- *Scope* item 4's sentence is two sentences after the rule's own, and the
  rule's first sentence keeps its words. The new sentences cite
  `skills/code-review/SKILL.md` *The record* and restate none of its
  points.

**`changelog.md` holds a `### Changed` section beside the two
`### Process changes` rows *Scope* item 6 names.** Every fragment of this
release opens with one (executed: `grep -n '^###'` over each
`seal/threads/*/changelog.md`). `docs/layout/the-record-layout.md` *A fact
of a work item has one record, and every other record cites it by path and
heading* gives the fragment the one record of what changed for a user. Each
`Why` cell cites G7, as item 6 asks.

**No case is added, and the new sentences have nothing behind them
(executed).** `frame/plan.md` *Technical context* decides that no case is
added, so contract rule 15 has no case to show red. One `bin/seal mutate`
run over `skills/code-review/orchestration.md` at `72c77856e` ran three
mutants under the 49 modules that name one of the four files or
`code-review`, with `-x -p no:xdist`. It deselected the closing-overview
case of `tests/behaviour/test_chain_hooks_hardening.py`, which failed only
because `gaps.md` was not yet written. The mutants deleted the stop
paragraph's bold lead, its sentence "A later row spends no round on a
finding that is not a `must`, whatever document it cites.", and the no-cap
sentence. The baseline passed in 254.5 s, and each of the three SURVIVED.
`gaps.md` `## Not verified` names the proofer for every new sentence of the
four files.

**The S commands (executed, at `72c77856e` unless named).**

- S2: `grep -c 'three finding rounds by default' docs/running/the-run.md`
  printed `1`.
- S7: above.
- S8: `git diff --stat release/v0.31.0...HEAD -- ':!seal/'` listed
  `agents/proofer.md`, `skills/code-review/SKILL.md`,
  `skills/code-review/orchestration.md` and
  `skills/implement/orchestration.md`, and nothing else.
- S9: the five modules S9 names and every module `git grep -l` lists for
  the four paths are among the boundary run below. A first run of the 49
  modules that name the four files or `code-review`, before `gaps.md` was
  written, gave 2983 passed, 10 skipped and one failure, the closing-overview
  case named above.
- S1, S3, S4, S5 and S6 are read, and the build read each one against the
  text it wrote. S1: the new paragraph names the drain's first row and
  rung 1 as documents a later row cannot reopen the stop on. Under it,
  round 7's `should` in #1216 takes a home of rung 2, 3 or 4, and the rows
  after rounds 7 and 9 stand on no ground the section leaves open. S3 is
  the paragraph's third sentence. S4 is the drain row's new clause. S5:
  round 5's `Test_in_corpus` gap stands in a case of a unit that moved with
  its body, and G7 reads the round's own grounds that the case "is beyond
  what the design owes". So no *Scope* item, acceptance row or `check:`
  line names it, and under the bullet the round names it in prose. S6 is the
  proofer's new sentence.

**The phase boundary ran as one command at `72c77856e`, with `gaps.md`,
`changelog.md` and the Status cell written and this record not yet: 103
modules, 5114 passed and 12 skipped (executed).** The list joins three sets
of modules from `tests/`. The first names one of the four edited files,
`proofer.md` or `code-review` (`git grep -l`). The second globs the
`skills` or `agents` directory or their markdown. The third reads
`seal/threads/` (`grep -rlE`).

**The other statements across the tree of each rule this range reworded
are a sample (contract rule 12).** The method was `git grep -n -i` over the
tree outside `seal/threads/` for "excessive", "past the third round", "the
run stopped", "when you stop", "when the orchestrator stops", "the cap",
"is capped", "covers nothing", "its group does not", "stop row", "to stop,
as" and "stop paying". A second `git grep -n -i` over `evals`, `tests` and
`templates` searched "covers nothing", "nothing its group", "Judgments of
the run" and "done now". These stand:

- `docs/running/the-run.md:13` and `agents/proofer.md:132` name the cap,
  which *Scope* Out keeps: both name the weighing point that stays.
- `docs/running/the-run.md:17` says every finding still open takes a home
  when the orchestrator stops, which stays true. `:48` changes at the
  settle through `## Rule changes`. Until then, read alone, it still
  offers rung 1 after a stop row, as `frame/plan.md` *Alternatives
  considered* row 8 accepts.
- `docs/running/the-run.md:74`, `skills/implement/acts.md:76` and
  `docs/forms/the-round-record.md:105` say a stop is a row of
  `frame/plan.md` *Judgments of the run* and that the orchestrator writes a
  close block it files at the cap. Both stay true.
- `agents/crafter.md:107` says a case that covers nothing its group does
  not already cover is not added. That is the crafter's rule for building a
  case, and the proofer's weighing does not change it.
- The remaining hits name another cap, such as the size of a hook's
  message, or the plan template's heading.

The part of the class this sample did not reach is any sentence that
states the stop or the group rule in other words. The proofer reads the
range against it at review.
