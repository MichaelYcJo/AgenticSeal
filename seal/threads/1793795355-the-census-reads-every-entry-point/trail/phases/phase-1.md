# Phase 1: 1793795355-the-census-reads-every-entry-point

## What this phase found

**The frame holds against the tree, with the corrections below.** It was
read at c9dce34c4 before the first edit. A probe parsed every tracked `.py`
and printed the first statements of its first module-level `__main__` block
(executed, a script under the scratch directory). It found the 48 entry
points, the two files with two blocks, the five loops without `stdin`, the
two loops after other statements and the 18 blocks without an answer that
design *Grounding* names. The widened census, run over every tracked `.py`
before the repairs, printed the 25 lines design *User scenarios &
acceptance* gives (executed): 17 blocks without an answer, the five loops
without `stdin`, `broad_gate.py:3246` and `seal_stamp.py:1508` out of order,
and `hooks/dispatch.py:613`'s exemption excusing nothing. After the repairs
it printed none (executed). `git grep -n 'exempt from entry_point'` outside
`seal/threads/` and `tests/` lists `hooks/lib/launch.py`, `broad_gate.py`
and `seal_stamp.py` alone (executed).

**The frame cites two commits no clone keeps.** `frame/design.md:27` cites
`3937d861` and `79252e48`. No `main` or release ref contains either
(executed: `git for-each-ref --contains`), and
`tests/text/test_a_cited_commit_outlives_the_squash.py` fails on them at the
frame's commit and at this phase's (executed). The squash commits on `main`
that hold the same two files byte for byte are `569780eff` for the
`1793521558` phase-3 record and `48d035aa6` for the `1793490088` phase-2
record (executed: `git diff` between each pair prints nothing). The design is
the framer's file, so the citation is left for the orchestrator to fold.

**The `hooks/after.py` arm moves from the `if` line to the block's first
statement.** Design *Scope* item 4 says the case
`test_refuses_a_block_without_the_call_and_one_with_it_after_main` keeps its
assertions. Its `hooks/after.py` plant calls `main()` and then
`console.to_utf8()`. Design *Scope* item 3 refuses an answer that is not the
block's first statement at the line of that first statement, so the census
now names line 2, not line 1. The assertion was changed to line 2. The order
is still refused, as plan A5 requires. Judged against design *Scope* item 3.

**`opens_with_to_utf8` became `calls_to_utf8(statement)`.** Design *Data &
interfaces* says the first-form reader stays. The census now looks for the
block's first answer statement wherever it stands, so the reader takes one
statement rather than a block. A name that says "opens with" would describe a
check it no longer makes. Nothing outside `tests/censuses.py` called it
(executed: `git grep`). Judged against design *Scope* item 3.

**The `entry_point` docstring was rewritten in this phase, not phase 2.**
Design *Scope* item 7 places it with phase 2. At this phase's commit, the old
docstring said "Every hook entry point" about a census that reads every
tracked `.py`. `skills/core/SKILL.md` *The rule a mechanism is kept against*
says a change rewrites the text it amends in the same commit. What phase 2
still owes from item 7 is `hooks/lib/console.py:54`.

**Phase 2 also meets `hooks/lib/console.py:46-53`.** That paragraph names
the scripts that spell the loop inline, and says none of the others gives a
reason. This phase added ten more loops: six under `.github/scripts/`, three
under `evals/scripts/`, and `mutation_check.py` and `test_layout.py`. Each of
the ten loads nothing from `hooks/lib/` at import, which is plan A10's reason
for the loop. The paragraph is phase 2's file, and its sentence on who spells
the loop should account for them.

**Q2 is answered: none of the seventeen met a reason.** Each of their
`__main__` blocks held one statement, `main()` or an exit around it (read).
`run_tests.py` runs pytest in a child process. The child opens its own
streams, so the parent's reconfigure does not reach it (read,
`run_tests.py:604-607`). `close_issues_on_release.py` and `rule_cases.py`
put `hooks/lib/` on `sys.path` at import, so each imports `console` and
calls `console.to_utf8()`. The other ten spell the loop. Judged against
`frame/questions.md` Q2 and plan A10.

**Two arms were added to the shape case beyond design *Scope* item 4's
list.** In the first, `reconfigure` is called on `sys.stdout` rather than on
the stream the loop binds. In the second, the stream is bound from
`getattr(sys, "stdout", None)` rather than from the target's first name.
Design *Scope* item 2 names both conditions. Without the two arms, a
mutation of either guard would have had no case to turn red.

**A case was renamed.** `test_accepts_the_call_first_a_module_and_a_file_outside_hooks`
became `test_accepts_the_call_first_and_a_module`. Its `tests/x.py` arm left
with design `## Removes`, and the old name described an arm the case no
longer has.

**Comments moved with the calls.** The comments above the call in
`finding_counts.py` and `tracker_labels.py` moved into the `__main__` block.
Each said "below" about text that `main` prints, and `main` now stands above
the block, so "below" became "`main` prints". `arm_check.py`'s comment ended
"this script reads no stdin", the reason it left out `stdin`. Its loop now
names `stdin`, so that clause went.

**The save hook removes an import as soon as it is unused.** Adding
`import console` before its call, and removing the call from `main()` before
writing it into the block, each lost the import to `ruff --fix` on save. The
seven imports were written again, and `uvx ruff check` over the changed files
passes (executed). Phase 2 meets the same hook.

**Seen red, each new case (contract rule 15).** Against the census as at
215ad6020, 13 of the 15 entry-point cases failed (executed:
`bin/test -q -p no:xdist tests/test_censuses.py -k Test_entry_point`).
`test_accepts_the_call_first_and_a_module` passed: its arms were already
accepted. The `skills/verify/scripts/x.py` arm of
`test_accepts_a_loop_over_the_streams_pairs_as_the_first_statement` passed,
because the old census read nothing outside `hooks/`. That arm went red under
M2 below. The two arms added afterwards were run against the old census
loaded from `git show 215ad6020:tests/censuses.py`. Each was refused at line
1 where the case expects line 2 (executed).

**Mutation runs, each `seal mutate tests/censuses.py` with
`pytest -q -p no:xdist tests/test_censuses.py -k <cases>`, at 5a6ee0f87.**
Every run ended `red: the cases failed against the mutation` (executed):

| Run | Guard broken | Cases that went red |
|---|---|---|
| M1 | the corpus, `_python(rel, root)` given `("hooks/",)` again | the three arms of `test_refuses_a_block_without_an_answer_outside_hooks` |
| M2 | `loop_pairs` returns `None` for a loop of the form | both arms of `test_accepts_a_loop_over_the_streams_pairs_as_the_first_statement` |
| M3 | the comparison with `STREAMS`, made `is None` | both arms of `test_refuses_a_loop_whose_pairs_are_not_the_streams_pairs_at_its_for_line` |
| M4a | an iterable that is not a literal read as `STREAMS` | the `console.STREAMS` arm of `test_refuses_a_loop_of_another_shape_at_its_for_line` |
| M4b | the `encoding` value's check removed | its `latin-1` arm |
| M4c | the `errors` name's check removed | its constant `errors` arm |
| M4d | the receiver's check removed | its `sys.stdout` arm and its binding arm |
| M4e | the binding's name check removed | its binding arm |
| M5 | the order check made `if False:` | `test_refuses_a_block_without_the_call_and_one_with_it_after_main` and `test_refuses_a_loop_after_a_statement_there_and_reads_its_pairs_exempted` |
| M6 | the last `__main__` block read in place of the first | `test_reads_the_first_main_block_and_no_later_one` |
| M7 | `console_streams` drops its first pair | `test_reads_the_pairs_hooks_lib_console_holds_from_the_file` |
| M8 | a `for` with `reconfigure` no longer an answer | nine cases across the accept, drift and shape cases |
| M9 | the no-answer refusal made `if False:` | the `deep.py` arm and the three outside-`hooks/` arms |

The repaired scripts only gain a statement the census reads, or move one.
Their `__main__` blocks are what changed, and the census over each is the
case that holds them, so no mutation was run on them.

**The exemptions of `broad_gate.py` and `seal_stamp.py` hold only the
order.** With each exemption line deleted, in a copy under the scratch
directory, the census refused `broad_gate.py:3246` and `seal_stamp.py:1508`,
each saying the answer at 3252 or 1512 is not the block's first statement
(executed). The case
`test_refuses_a_loop_after_a_statement_there_and_reads_its_pairs_exempted`
holds that a drifted loop under the same exemption is still refused.

**The phase-boundary set ran once.** It was one `bin/test -q` over the 85
test modules that name a file this phase changed (executed). 3984 passed, 13
were skipped and 2 failed. One is the citation above. The other is
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which fails until this phase's `gaps.md` stands, and the record commit
writes it. The modules for the plan row's *Verified by* cell are
`tests/test_censuses.py`, `tests/hooks/test_console.py`,
`tests/hooks/test_dispatch.py` and the 25 module files of the scripts this
phase edits. They passed in one command at 8485e67fd: 1884 passed and 2
were skipped (executed).

**The `evals/scripts/noninferiority.py` hunk is its `__main__` block
alone.** `git diff 215ad6020 -- evals/scripts/noninferiority.py` shows one
hunk at `:1598` (executed), as plan *Operational impact* asks.
