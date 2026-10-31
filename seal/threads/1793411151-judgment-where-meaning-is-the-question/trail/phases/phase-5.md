# Phase 5: 1793411151-judgment-where-meaning-is-the-question

## What this phase found

**The frame holds at the coordinates the plan's technical context gives for
this phase, with one cell that names the wrong rules.** `survey`,
`report`, `open_rows` and `gfm_table` stand where the plan says, and
`pr_body.py` copies `## Phases` alone, so a new last section of the plan
does not reach the pull request body (read). The plan says rules 16, 18, 19
and 20 of `tests/text/test_the_rules_have_one_owner.py` name the skill.
Rule 16's owner is `docs/the-review-record.md`, and its links are the
framer's and the implement skill's; the cases that read
`skills/code-review/orchestration.md` are rules 17 to 20 and
`test_the_cap_counts_from_the_last_design_change`, which pins "counted from
the last design change" there and in both READMEs (read). The handoff said
HEAD was `27dcf020`; it was `a3f64739`, two record commits of the
orchestrator's later (executed).

**The dry run's section, line by line.** After the open rows and before
what `--apply` removes, `JUDGMENTS_HEADING`; then one `not read:` line per
plan whose section holds no table under the exact header, naming the plan;
then one group per `Judged against` cell, in the order the work items are
listed, each `judged against: <cell>`, each work item under it with its
round count, and each row as `frame/plan.md:<line>  <date>  <judgment>`
over `grounds: <grounds>`. The cell is grouped as written, so two spellings
of one document are two groups, and the settling session reads them as
one. Judged against *Scope* item 12 and `skills/core/SKILL.md` *The rule a
mechanism is kept against*: a script names what it did not read and grades
nothing.

**Three choices the frame left open, each with its grounds.**

- The plans are read from the working tree in both modes, where the
  designs are read at `--released-at` in shared mode. The open rows are
  read from the working tree in the same pass, and `--apply` removes the
  working-tree directory, so the rows printed are the rows that go. Judged
  against the module docstring of `settle.py`, *The dry run is the
  timeline*.
- The template ships an empty row under the header, as its
  *Alternatives considered* table does, and the reader skips a row whose
  every cell is empty. `frame/design.md` Table C draws the table with a
  placeholder row; a placeholder left in a plan would print as a judgment.
  The placeholder text stands in a paragraph above the table instead.
  Judged against Table C and `templates/records/sdd-plan.md`.
- `skills/settle/SKILL.md` *The settling session's procedure* gains no
  step: its step 3 now reads the judgments after the designs to read whole.
  A new step would renumber steps 4 to 9, and
  `tests/text/test_settle_reads_before_it_removes.py` pins "step 8 runs
  every one". Judged against *Scope* item 12, which asks that the procedure
  name the section and what the session does with it.

**Departures the frame did not name.** Each is a statement of a rule this
phase rewrote, corrected in the same commit (contract rule 19):
`README.md` and `README.ko.md` state the cap in their review paragraph, and
both now say the default is where the orchestrator weighs and that the
decision goes to the plan. `skills/implement/SKILL.md` *3. The SDD file
set* names the orchestrator beside the framer for `frame/plan.md`. Its
`trail/phases/phase-N.md` row first gained the decision clause too, and
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` refused it as
20 words copied from the template's placeholder, so the template and
`agents/crafter.md` step 8 carry the clause alone (`9310a2de`). In
`skills/code-review/orchestration.md` the word "cap" is gone from the two
sections; the redesign row says "starts the count again".

**What waits for the settle.** `docs/the-review-record.md` *The run* still
states the extension line and the route taken whatever the comparison says.
`skills/code-review/orchestration.md` and both READMEs state the guidance.
The pins on the policy text in `test_the_rules_have_one_owner.py`, rule 14,
rule 16 and `test_the_cap_counts_from_the_last_design_change`'s reading of
*The run*, stay green and go red at the settle, as the plan's operational
impact says.

**Where the folded sentence went.** *Scope* item 11's last sentence went
into *The fix pass then finds what the fixes left standing*,
with the fold in a commit of its own, because the same paragraph says the
round record's commit holds `trail/rounds/round-N.md` alone.

**Seen red.** The two judgments cases, the headings case with its two
`JUDGMENTS_HEADING` pins, and the `CONFIG` and `ROUTING` purposes ran
against the tree before `settle.py` changed: 5 failed, on the missing
constants and the old purpose (executed). The
two text pins, one in `test_the_rules_have_one_owner.py` and one in
`test_the_set_a_work_item_always_has.py`, ran before the skill text and
the template changed: both failed (executed).

**Mutation.** One `seal mutate` call over `settle.py` at `3904967e`,
eleven mutants, 11 red, 0 survived (executed). Each is one boundary of
`judgments` or one line `report` prints: no section read as a section; the
unread refusal dropped; the empty row kept; every row in one group; the
line not offset to the plan; the table read over the whole plan; the
survey's judgments emptied; the `not read:` line, the grounds line and the
singular "round" dropped; a refusal named only beside rows. Two branches
have no case: a `trail/rounds` that is a file, which `routing.rounds`
raises on, and a row whose `Judged against` cell is empty. The text units
add no behaviour a mutant can break, and their pins were seen red.

**Duplicates.** `seal layout --pairs` over the three changed test modules
names 0 pairs (executed).

**The boundary set.** One `bin/test -n auto` over 114 modules: the plan's
modules and every module under `tests/` that names a changed path, the
templates or `"records"`, an agent file, a README, `plugin.json` or a
`changelog.md`, or that globs or walks a directory. The list was built by
`git grep` over `tests/` and is not a census: a module that reaches a
changed path another way is the broad gate's. At `5a7a5ce0` it ran 3
failed and 4979 passed: a 107-column line in
`skills/implement/orchestration.md`, which an edit's last line left joined
to the next, and the copied clause above, twice. Both were fixed in
`9310a2de`, and the same command then ran 4982 passed and 11 skipped, exit
0 (executed). `seal rules --check` holds all 265 check lines in 54 rule
files (executed).
