# Phase 1: 1793580304-a-measurement-no-record-asks-for-closes-its-row

## What this phase found

**The frame holds, with one sentence of *Scope* item 6 read more narrowly
than it is written.** Every coordinate the design and the plan name stands
where they say at `544ba35bd`, whose `skills/` and `tests/` equal
`0633f9a5`'s (`git diff --quiet 0633f9a5 544ba35bd -- skills tests`, exit
0). Step 6's table is at `skills/settle/SKILL.md` lines 275 to 279,
`ROWS_HEADING` at `settle.py` lines 434 to 438, the heading pin at
`tests/skills/test_settle.py` line 2405, and the three cases that split the
report on the constant at lines 592, 882 and 1532. The design's `from`
stands in `docs/the-record-layout.md` lines 104 to 107.

*Scope* item 6 drops "their order and the row kinds" from the docstring of
`test_the_skill_states_the_settling_sessions_procedure`. In that docstring,
"their order" is the order of the steps, and the new case holds the order of
the row kinds, not of the steps. The design's `## Removes` row also keeps
what each kind means as the proofer's. So the docstring now reads "The
steps, their order and what each row kind means are the proofer's to read;
the order of the row kinds is the next case's." Judged against contract
rule 19: the sentence is rewritten in place to the fact that changed, and
the fact that did not change stays stated.

**Decisions settled while writing the text.**

- The meaning of "on record" is a paragraph under step 6's table, in the
  words of design *Data & interfaces*. A settling session reads step 6 and
  not the design, and the two new rows turn on that phrase. Without the
  paragraph, the row's own `Who must answer` cell could read as the record
  that needs the answer, and every row would be re-homed again. Judged
  against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
  가지로만 읽히게 쓴다*, whose second rule asks that a term this
  repository uses carry one meaning, and against `frame/questions.md`'s
  stated assumption.
- The order paragraph is split into two sentences of grounds after the rule:
  why a measurement of a gone unit is moot, and why a measurement no record
  asks for closes before re-homing (design *Scope* item 2). The second
  borrows the `to`'s closing sentence, "an issue nothing on record waits on
  costs its reader a reading and a close", so the skill and the policy give
  the same reason.
- The heading reads "moot, answered, a measurement no record asks for, or a
  measurement to re-home". The comma before "or" keeps "asks for" from
  running into "or a measurement" as one phrase.

**One addition beyond the six *Scope* items, inside the build's file.**
`skills/settle/SKILL.md` *What the dry run shows*, the bullet on open rows,
gains one sentence: the heading names the four kinds of step 6 in its
table's order and gives no row a kind, and the settling session decides
each. The orchestrator's spawn asked that the skill be written so this
reading holds, and that bullet is where the skill says what the dry run
prints. Judged against `skills/core/SKILL.md` *Judgment is spent where
meaning is the question, and a script answers the rest* and design G7. No
other dry-run text changes.

**Each new or changed case was seen red before the change.** One command at
`544ba35bd` with the edited cases and the unchanged code:
`bin/test -p no:xdist -q tests/skills/test_settle.py
tests/text/test_settle_reads_before_it_removes.py -k
"test_the_dry_runs_headings_say_who_decides or
test_the_skill_orders_the_row_kinds or
test_the_skill_states_the_settling_sessions_procedure"`, exit 1, 2 failed
and 1 passed. The heading pin failed because the constant read "moot,
answered or a measurement to re-home". The order case failed with
`['moot', 'answered', 'a measurement nobody has taken']`. The docstring-only
case passed, as a docstring change should. After the change, the same
command exited 0.

**Each unit that adds behaviour went red under `seal mutate`, at
`15eb84523`.**

- `bin/seal mutate skills/settle/scripts/settle.py --replace "a measurement
  no record " "a measurement nobody " --tests "bin/test -p no:xdist -q
  tests/skills/test_settle.py -k
  test_the_dry_runs_headings_say_who_decides"`: red, the case failed
  against the mutation (exit 1), and the command exited 0.
- `bin/seal mutate skills/settle/SKILL.md --replace "   | a measurement no
  record asks for |" "   | a measurement nobody asked for |" --tests
  "bin/test -p no:xdist -q tests/text/test_settle_reads_before_it_removes.py
  -k test_the_skill_orders_the_row_kinds"`: red, the case failed against
  the mutation (exit 1), and the command exited 0.

`git status --short` was empty after both runs.

**The phase-boundary run.** One command through `bin/test` over 24
modules, exit 0, 1870 passed and 8 skipped. The 8 skipped are
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:242`,
"no shipped document names it". `bin/seal layout --check tests` exited 0.
`uvx ruff check` and `uvx ruff format --check` over `settle.py`,
`tests/skills/test_settle.py` and
`tests/text/test_settle_reads_before_it_removes.py` exited 0.

The modules were listed this way:

- `git grep -l` over `tests` and `evals` for `settle/SKILL.md`, which
  listed 13 modules, and over `tests` for `settle.py`, which listed 11. All
  of them ran.
- `git grep -l` over `tests` for `seal/threads` listed about 60 modules,
  most of which build a fixture tree. A second search for a path joined on
  `ROOT` with `seal`, `threads` named the modules that read this
  repository's own records, and the run took those that read a file this
  phase writes: `test_chain_hooks_hardening.py`, `test_unverified_check.py`
  and `test_the_pull_request_language_is_the_repositorys.py`. To these it
  added the plan's list, `tests/test_censuses.py`,
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and
  `tests/text/test_a_moved_rule_leaves_its_definition.py`.

The second list is a sample, since a module can spell the path in a way
neither search matches. The broad run is what reads the rest.

**Where else the rule stood.** `git grep -n -i` over everything outside
`seal/threads` and `tests` for "nobody has taken", "re-home", "moot" and
"open row" found the kinds stated only in `skills/settle/SKILL.md` step 6,
`settle.py#ROWS_HEADING` and `docs/the-record-layout.md` lines 98 to 118.
That last one changes through the design's `## Rule changes`.
`docs/release-checklist.md` step 2b, `settle.py`'s docstring, the skill's
command block and both READMEs' `seal settle` rows name open rows and no
kind, and they stand as they were. This is a search for wordings, so it is
a sample. A sentence that states the kinds in other words is the proofer's
to find.
