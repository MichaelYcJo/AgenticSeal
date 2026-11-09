# Phase 1: 1794201840-the-orchestrator-chooses-each-items-route

## What this phase found

**The frame holds for this phase.** `f80823a6` differs from `e1067476`,
the commit the frame read, only by the three frame files (executed:
`git diff --stat e1067476 f80823a6`). The coordinates the phase builds on
held at `f80823a6` (read): G21's lines in `agents/framer.md`,
`skills/implement/SKILL.md`, `skills/implement/orchestration.md` and
`skills/commit-pr-convention/SKILL.md`, and G25's pins at
`tests/behaviour/test_waiver_decided_at_start.py:55`, `:385`, `:404-405`
and `:475-476`.

**Seen red before the text was written** (executed: `bin/test
tests/behaviour/test_waiver_decided_at_start.py tests/text/test_review_axes.py
-p no:xdist -q` against `f80823a6`'s prose with the new pins in place, 6
failed). Each failing line names its guard:

- `#test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis`
  failed at "question 1 does not offer exactly four options".
- `#test_question_1_is_put_every_time_with_the_ladders_answer_marked`
  failed at "and `agentic` is the answer marked".
- `#test_question_1_lists_the_four_modes_in_the_owners_order`, new, failed
  at "question 1 offers ['automation', 'per axis', 'no work item']".
- `#test_the_exit_names_what_does_not_run_rather_than_where_it_ends`
  failed at "question 1 has no exit option labelled `direct`".
- `#test_the_ceiling_is_stated_beside_the_shape` failed at "the ceiling
  does not name question 1".
- `tests/text/test_review_axes.py#test_the_routing_section_holds_the_answers_and_the_shape`
  failed at the `SHAPE` sentence reading "only under `manual`".

**Mutations, each with `seal mutate` after the build was committed**
(executed, each `red`):

- `agentic`'s cell with `` `direct` `` replaced by "the exit": the new
  case failed at "`agentic`'s description does not say it may choose
  `direct`". This is the one assertion the run against `f80823a6` could
  not show red alone, because the order assertion above it failed first.
- The label `manual` replaced by `per axis`: the new case failed at
  "At index 2 diff: 'per axis' != 'manual'".
- The ceiling paragraph replaced by its text at `f80823a6`: the ceiling
  case failed at "the ceiling does not name question 1".

**The ceiling case was made case-blind after its first mutation**
(`19c3ea45`). It first asserted the capitalised "Question 1", and the first
mutation left "to question 1" in the paragraph. A reader takes either
spelling as naming question 1, so the case now reads the paragraph
lower-cased. Judged against `skills/core/SKILL.md` *The rule a mechanism
is kept against*: no script carries a list of the spellings a label is
written in.

**Departures from the frame, each with its grounds.**

- **The paragraph *A label names what it turns off, not where it ends* is
  rewritten as *A label names no destination, and its description says
  what it turns off*.** The owner named the four answers as modes, so the
  question reads as four modes rather than phrases that spell out what
  each does, and each description says what its answer does
  (`frame/design.md` G1). Under that decision the old sentence is false
  for every label. What it guarded still holds: no label names a
  destination, which `#test_the_exit_names_what_does_not_run_rather_than_where_it_ends`
  pins. *Scope* item 1 left the cell words to the build under that
  section; the section's own heading is the departure. The case's
  docstring is rewritten to match.
- **The exit's description names six things, not five.** Following G2,
  it opens "This session writes the change itself: no agent, no work
  item, no frame, no review, no seal and no `routing.md`." The paragraph
  that counted "the five things that do not happen" now says the
  description names every party and record that does not run or is not
  written, so no count stands to go stale.
- **The parts of *Scope* items 10 and 11 that stand in
  `skills/implement/orchestration.md` are done here, not in phase 2.**
  These are the old labels in *What the answer writes* (`automation`
  writes all four party rows, `per axis`, `no work item` as the answer), in
  the order block, and "the direct answer" in the paragraph opening **The
  declaration moves the check and waives nothing**, which now names
  `straight to the PR`. With the table renamed, the file would otherwise
  name one answer by two labels at HEAD. Judged against `agents/crafter.md`
  *Before you hand back, your range and the work item's records are read
  whole against HEAD*. The test comments and docstrings next to the hunks
  this phase changed are rewritten for the same reason:
  `tests/behaviour/test_waiver_decided_at_start.py` at the `SHAPE` comment,
  the docstrings of the cases on question 1, the exit and the `Planning`
  row, the `Planning` case's comment on the box tables (`aa8a9280`), and
  `tests/text/test_review_axes.py`'s two comments beside the
  `SHAPE` copy. A census over the four edited prose files finds the old
  labels nowhere as an answer, and `no work item` only as the trailer's
  value (executed: `git grep -n -w "automation"` and `git grep -n "per
  axis\|\`no work item\`\|\*\*no work item\*\*\|direct answer\|direct
  route"` over those files). Phase 2 keeps the rest of items 10 and 11:
  `CONTRIBUTING.md`, `skills/code-review/orchestration.md`, the READMEs,
  `evals/`, `tests/lib/test_routing.py` and
  `tests/text/test_the_direct_answer_owes_the_sealers_record.py`.
- **`skills/implement/orchestration.md` *Orchestrator: when a work item is
  required* gains one sentence** (`63c3d9ff`): under `complete` and
  `manual` the rung decides what a work item writes, and under `agentic` it
  is one signal of those *Under agentic* weighs. G21's list did not name
  that section. Reading the file whole found it in the class of *Scope*
  item 4, statements that the ladder alone decides the frame or the route
  (contract rule 12).
- **The test function name
  `test_question_1_is_asked_alone_and_the_boxes_only_under_per_axis`
  stays.** `.test_durations` keys the case by that name. The frame keeps
  the name of `tests/text/test_the_direct_answer_owes_the_sealers_record.py`
  for the same reason (`frame/plan.md` *Alternatives considered*).

**Decisions made while writing, each with its grounds.**

- The assertion that *The ceiling* names question 1 is added to the
  existing `#test_the_ceiling_is_stated_beside_the_shape`, not written as
  a case of its own as *Scope* item 8 reads. That case already reads the
  ceiling paragraph's cap on a question's options, and a new assertion
  goes into the group that covers what it reads (`agents/crafter.md` *A
  new test starts from its group*).
- *Under agentic* gives each row's choice as a bulleted list, not a
  table. Three cases of `tests/behaviour/test_waiver_decided_at_start.py`
  count the lines opening `| Implementation |`, `| Planning |` and
  `| Automation |` in `skills/implement/orchestration.md` and require one
  each. A second table keyed by the rows would make those counts two.
- The combinations table cites `agents/crafter.md` *Order of work* for
  "`crafter` building with no frame". G11 also names the rule *A declared
  frame that is absent stops the build*. That rule covers a declared
  framer whose `frame/design.md` is missing. It does not cover a crafter
  routed with no frame declared at all, and *Order of work* is where the
  crafter reads `frame/plan.md` and fills its Status cell.
- The sentence on the mark's grounds says a ladder mark would recommend
  `complete` "because nearly every change alters observable behaviour and
  sits above its last rung". The skill ships to every repository that
  installs the plugin, so the grounds name no property of this
  repository alone. `frame/design.md` G3 states the same reading for
  this repository.

**What phase 2 needs.**

- Two sentences of this phase cite text phase 2 writes. *What the answer
  writes* and *Under agentic* say the sealer reads a chosen route's grounds
  against the diff (`agents/sealer.md` step 4). *Under agentic* also says
  the settle reads the release's routes (`skills/settle/SKILL.md` *The
  settling session's procedure* step 5). Neither file says so until
  *Scope* items 5 and 6 land.
- The README lines of *Scope* item 7 must not share a passage of fifteen
  words or more with question 1's cells or with *Under agentic*, which
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refuses.
- `tests/behaviour/test_the_set_a_work_item_always_has.py` refuses a
  number word before "file" or "files" in `skills/implement/SKILL.md` and
  `skills/implement/orchestration.md`. *Under agentic* writes "a two-line
  fix" and no file count.
