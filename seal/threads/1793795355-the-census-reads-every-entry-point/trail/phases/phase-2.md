# Phase 2: 1793795355-the-census-reads-every-entry-point

## What this phase found

**The frame holds for this phase.** It was read at 385a6a567 before the
first edit. `CONTRIBUTING.md:423-426` held the clauses "Every hook entry
point" and "the second over `hooks/`" that design `## Removes` names. The
pin's docstring at
`tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py:3`
said "the hook entry points'", and its line 24 asserted "opens its
`__main__` with `console.to_utf8()`". `hooks/lib/console.py:54` held "Which
entry points owe the answer is #1255's." (read, each).

**Seen red, the text pin (contract rule 15).** The pin's line 24 now
asserts the new sentence on what every entry point opens its first
`__main__` block with, and a second assertion asserts "enforce both over
every tracked `.py`". Against the old bullet, the first new assertion
failed (executed: `bin/test -q -p no:xdist` over the pin's module). With
the new first sentence written and the old enforcement clause still in
place, the second new assertion failed at its own line (executed, the same
command). With the whole bullet rewritten, the case passed (executed).

**The console module's paragraph on who spells the loop was rewritten, not
line 54 alone.** Phase 2's row names `hooks/lib/console.py:54`. Phase 1's
record said the paragraph at lines 46 to 53 should account for the ten
loops phase 1 added. Line 54's answer, that every entry point owes the
answer, now opens the paragraph. The paragraph then says that an entry
point gives it by the call or by the loop. A script that loads nothing from
`hooks/lib/` at import spells the loop, because a load of the module would
be one more load that can fail before the answer. That is plan A10's
reason. The paragraph does not state A10's other half, that a script whose
own imports put `hooks/lib/` on `sys.path` calls `to_utf8()`.
`skills/implement/scripts/seal.py:241` does that and spells the loop
(executed: an `ast` walk of every loop site's module-level statements for a
`sys.path` insertion), so the sentence would be false of the tree. The
first rewrite, at 64703abb7, stated it, and a later commit of this phase
took it out. The sentence "None of the others says why it copies the loop"
now covers the scripts that reach
`hooks/lib/` at import, under `skills/*/scripts/` and under
`.github/scripts/`, other than `chain_check.py`, which does say why.
Judged against `skills/core/SKILL.md` *The rule a mechanism is kept
against*, "A change rewrites the text it amends in place".

**Phase 1's account of its ten loops does not hold whole at HEAD.** Phase
1's record says six of the ten loops are under `.github/scripts/` and that
each of the ten loads nothing from `hooks/lib/` at import. Five are under
`.github/scripts/` (executed: `git diff 215ad6020 HEAD` over each file
phase 1 changed, counting the added `reconfigure(` and `to_utf8()` lines).
They are `durations_union.py`, `label_merged_on_release_branch.py`,
`release_completeness_check.py`, `roll_flow_measurement_issue.py` and
`run_tests.py`. With the three under `evals/scripts/` and the two under
`skills/verify/scripts/`, that makes ten. Three of the ten reach
`hooks/lib/` at import (read, each file's module body).
`label_merged_on_release_branch.py:77` loads `close_issues_on_release.py`
by path, and that file puts `hooks/lib/` on `sys.path` and imports
`console` at its lines 76 to 82. `release_completeness_check.py:111` loads
`label_merged_on_release_branch.py`, so it reaches the same module.
`run_tests.py:82-94` loads `hooks/lib/launch.py` by path. The other seven
load nothing from `hooks/lib/` at import. `mutation_check.py` loads
`arm_check.py`, and `arm_check.py`'s module body imports only the standard
library (executed: an `ast` walk of each file's module-level statements).
So the console module's docstring puts those three among the scripts that
reach `hooks/lib/` at import and give no reason for the loop. It does not
put them under A10's reason. Whether `label_merged_on_release_branch.py` and
`release_completeness_check.py` should call `console.to_utf8()` is in
`gaps.md` `## Not done`.

**The exemption marker is not spelt in the console module's prose.** The
first rewrite of the paragraph quoted `# exempt from entry_point: <why>`.
The census did not read it as an exemption, because the line opens with
prose (executed: `tests/test_censuses.py` passed). But design *User
scenarios & acceptance* checks the tree with `git grep -n 'exempt from
entry_point'`, which would then list a fourth file. The paragraph now says
"carries its reason in an exemption", and the search outside `seal/threads/`
and `tests/` lists `hooks/lib/launch.py`, `broad_gate.py` and
`seal_stamp.py` alone (executed).

**No mutation run is owed.** This phase changes prose: a `CONTRIBUTING.md`
bullet, a docstring and a text pin. It adds no unit of behaviour.
`skills/verify/SKILL.md` *The narrow command still has to be able to fail*
says that for a docstring inside source, what can fail is that the module
still imports. `tests/hooks/test_console.py` imports and runs the module,
and it passed (executed).

**The other statements of the rule, a sample.** `git grep` outside
`seal/threads/` for "hook entry point", "opens its `__main__`", "second
over `hooks/`", "#1255's", "owe the answer" and `entry_point`, and over
every `*.md` for `to_utf8`, found the three places this phase rewrote
(executed). One more hit, `README.md:353`, says the hook entry point
returned its decisions on a Windows cp949 console. That is a statement
about one run of the dispatcher, not the rule, and it stands. The search
covers the spellings above. It does not cover a statement of the rule in
other words.

**The phase-boundary set ran once, at 64703abb7.** It was one
`bin/test -q` over 31 test modules (executed): each module under `tests/`
that names `CONTRIBUTING`, plus the pin, `tests/hooks/test_console.py` and
`tests/test_censuses.py`, the three the plan row's *Verified by* cell
names. 1211 passed and 2 were skipped. The commits after 64703abb7 change
the console module's docstring and this work item's records. At the
commit phase 2's Status cell names, one `bin/test -q` ran the three
modules of the *Verified by* cell with the modules that read a work item's
records from the tree: `tests/behaviour/test_chain_hooks_hardening.py`,
`test_a_phase_hands_the_next_one_a_record.py`,
`test_the_set_a_work_item_always_has.py`, `test_unverified_rows_close.py`,
`tests/text/test_a_cited_commit_outlives_the_squash.py` and
`tests/github/test_publish_release_note.py` (executed). Tests that read every tracked file
were not counted as reading a path this phase changed, apart from
`tests/test_censuses.py`. Running all of them would be the suite, which is
the broad gate's.

**The changelog fragment carries no `### Process changes` table.** This
work item changes none of the files `docs/layout/the-record-layout.md` *A
change to the way of working writes its process row in its own fragment*
names (executed: `git diff --name-only 215ad6020`).
