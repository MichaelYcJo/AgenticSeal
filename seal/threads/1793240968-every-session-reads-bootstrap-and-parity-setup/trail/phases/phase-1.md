# Phase 1: 1793240968-every-session-reads-bootstrap-and-parity-setup

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 3890b230 |

## What this phase was asked

Build phase 1 of `frame/plan.md` against the frame at `77fe5438`, under the
owner's automation answer, with HEAD at the approval line `b192cf1c`. The
parity setup is stated once. `skills/implement/orchestration.md`
*Orchestrator: Parity setup* is removed, and the Bootstrap's step 3 answers a
yes with one sentence sending the orchestrator to
`skills/parity-setup/SKILL.md` *Procedure*. The acts table loses the Parity
setup row, and the Bootstrap row's grounds carry what that row said.
`skills/parity-setup/SKILL.md:15-17` says the bootstrap's yes runs its
procedure. `tests/behaviour/test_chain_hooks_hardening.py:237-247` is
re-pointed and seen red with the new step 3 sentence deleted. The sibling
#1142 edits the `Implementation` row of *What the answer writes*, which this
phase does not touch.

## What this phase found

**The frame holds against the tree, with one exception (read, at
`b192cf1c`).** Every phase 1 coordinate resolves to the text it names: the
Bootstrap at lines 89 to 280, the Parity setup at 281 to 301, step 3 at 263
to 269, the acts rows at 666 and 667, the case at 237 to 247 and the
docstring at `tests/behaviour/test_first_setup_asks_once.py:243`. The
exception is the re-pointed assertion. The plan's row has it read the whole
of `orchestration.md` for `skills/parity-setup/SKILL.md`, and the same row
puts that path into the acts table's Bootstrap row. A whole-file needle
would therefore stay green with step 3 deleted. The case reads the
*Orchestrator: Bootstrap* section alone, and `gaps.md` records the
divergence.

**How the case was seen red (executed).** With the assertion re-pointed and
`orchestration.md` as it stood at `b192cf1c`, `bin/test
tests/behaviour/test_chain_hooks_hardening.py -k
test_parity_declaration_is_bootstrappable_not_hand_written -p no:xdist -q`
exited 1 on `the bootstrap's yes never reaches the parity-setup procedure`.
After the commit, `bin/seal mutate skills/implement/orchestration.md` over
the step 3 sentence, which replaced it with `**Yes**: the orchestrator
continues the work.`, printed `red: the cases failed against the mutation
(exit 1)` and exited 0, and the tree was clean after the restore.

**The step 3 sentence cites the procedure as a section.** It reads
`skills/parity-setup/SKILL.md` *Procedure*, so
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves it
against the skill's `## Procedure` heading.

**The narrow runs (executed, one module per command, exit codes read
directly).** `test_chain_hooks_hardening.py` exit 0, 30 passed;
`test_every_orchestrator_act_names_its_delivery.py` exit 0, 14 passed;
`test_first_setup_asks_once.py` exit 0, 50 passed;
`test_a_cited_section_stands_in_its_file.py` exit 0, 23 passed;
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` exit 0, 8
passed; `test_docs_line_wrap.py` exit 0, 39 passed. The first run of
`test_chain_hooks_hardening.py` exited 1 on
`test_every_spec_directory_that_reached_the_ladder_has_an_overview`, because
a work item holding a frame owes `gaps.md`. The memo was opened in this
phase's commit, and the module then passed.
