# Phase 1: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

## What this phase found

**The frame holds against the tree at `1594f5525`, with one anchor that
moved.** The contract's preamble, description and rule 11, the three
definitions' record steps and *Never* lists, the paragraph of
`docs/running/the-agent-set.md` and the two test modules stood where
`frame/design.md` *Grounding* G4, G13 and G15 say (read). T8 is placed after
"The prose in the records follows `Record language` in `config.json` under
that root" and its clause. Since #1578 that sentence runs on past a colon
and ends at "says what an absent key does.", so T8 stands after that full
stop, which is where the frame's words point (read, judged against
`frame/design.md` *Data & interfaces* T8).

**The reference-root bullet can leave both definitions.** The bullet also
banned copying a file out of a reference root, which "never written by
anything this skill produces" in `skills/implement/SKILL.md` *Document
layout — two roots, three lifetimes* does not say alone. That sentence cites
`templates/setup/config.md` *Reference specs*, whose "never moves, edits,
absorbs or deletes a reference root" covers the copy, so the reader is sent
to the whole ban (read, judged against `frame/plan.md` *Alternatives
considered* row 2).

**Two departures from the frame's case clauses, each grounded in its
scenario.** First, `frame/design.md` S7 names
`tests/text/test_a_language_section_of_writing_style_opens_alone.py` as
what verifies that the framer's, the crafter's and the proofer's steps cite
rule 11. *Scope* item 9 gives that module only two clauses, and neither
reads a step. So the case gained a third clause: each definition in
`CITING_STEPS` has a block that names `writing-style` and cites
`rule 11`. Second, the dangling-heading arm over the contract survived
`seal mutate` on its reader list, because no heading the contract names is
dangling at HEAD. The case now asserts the contract's two headings are
among the spans the arm read (`f96c68b2d`). Both were judged against
`skills/implement/SKILL.md` *2. Implement test-first, and let each rule
name its test* and `frame/design.md` S7.

**A rule 19 correction the frame did not name.** The docstring of
`tests/behaviour/test_a_probe_that_commits_says_so.py` said rule 8's number
"is one the contract's preamble lists as retired". It now names
`docs/running/the-agent-set.md`. The other statements of the moved facts
were found by `git grep` on `contract's preamble`, `preamble`,
`16 and 20`, `never reused`, `reasons no agent`, `crafter, proofer, tracer`,
`copy a file out of`, `English prose rules`, `record's language` and
`language section` over the tree outside `seal/threads/` (executed). That
list is a sample, as contract rule 12 says of the other statements of a
rule. No other hit states a moved fact as it stood.

**How `RETIRED` reads the document.** `retired()` reads only the paragraph
that opens **The contract's rule numbers are stable.**, up to the next
blank line. Where the paragraph is reworded so that opening is missing, it
lists nothing, and each retired number then reads as a gap. That is the
red failure `frame/plan.md` *Alternatives considered* row 6 accepts.
`numbering_faults(text, doc)` reads the document's list unless the case
passes a mutated one, so
`test_a_listed_number_that_has_a_heading_is_named` now mutates the
document, not the contract.

**Seen red, each before its fix or with its guard removed (executed).**
- At `1594f5525`, with the two test modules changed and no text edited:
  four numbering cases of
  `tests/text/test_the_agent_contract_holds_the_universal_rules.py` failed
  with "8 has no heading and the document does not list it", and the
  language case failed with "contract rule 11 no longer names both language
  sections by heading; it names []". The language case's `uncited` clause
  was not reached there, so it was shown red by the mutations below.
- After `9c6beaf5a` and `f96c68b2d`, `seal mutate`. Each run was red
  (exit 0), and each failing line names the guard broken:
  - `docs/running/the-agent-set.md`, the list cut to "8 and 16": red, "20
    has no heading and the document does not list it".
  - The contract test's reader turned back to the contract, `retired(text)`:
    red.
  - Its paragraph scope emptied, `doc[at:at]`: red.
  - `agents/proofer.md`, `agents/framer.md` and `agents/crafter.md`, each
    step's "rule 11" changed to "rule 12": red, each naming its own file in
    the `uncited` assertion.
  - The contract's `## English prose rules` misspelt: red on the rule 11
    clause.
  - A `## Nonexistent` span added to rule 11's sentence: red on the
    dangling assertion, naming `skills/agent-contract/SKILL.md`.
  - The reader list `[*rels, CONTRACT]` cut to `rels`: SURVIVED at
    `9c6beaf5a`, and red at `f96c68b2d` on "the heading check no longer
    reads skills/agent-contract/SKILL.md".

  The cases each run used were
  `bin/test -q -p no:xdist tests/text/test_the_agent_contract_holds_the_universal_rules.py`
  and `bin/test -q -p no:xdist tests/text/test_a_language_section_of_writing_style_opens_alone.py -k opens_alone`.

**The moved text owes no case of its own.** The contract's preamble, the
three definitions' steps and *Never* bullets, and the document's paragraph
are moves and deletions of text. They are proved as `skills/verify/SKILL.md`
*The narrow command still has to be able to fail* says for a move: by the
existing cases at the new place, the two modules above, and by the census
of the old spelling. The census is the plan row's searches at `f96c68b2d`.
`git grep -n -F` printed nothing for `Write in a reference root` and
`English prose rules` in `agents`, and for `retired numbers`,
`crafter, proofer, tracer` and `reasons no agent weighs` in `skills`
(executed).

**The phase boundary set was run in one command (executed).** It was
`bin/test -q tests/text tests/behaviour` followed by the modules
`git grep -l -E 'agent-contract|crafter\.md|framer\.md|proofer\.md|the-agent-set' -- tests`
lists outside those two directories. `tests/run_tests.py` is left out of
that list because it is the runner and not a test module. The set
includes `tests/behaviour/test_a_cited_section_stands_in_its_file.py`.
At `f96c68b2d` it gave 1746 passed, 9 skipped and 1 failed. The failure was
`tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which names this work item for having no `gaps.md`. This record's commit
writes that file, and the set run again at that commit is the result the
hand-back reports.

**Bytes at `f96c68b2d` (executed, `git show <rev>:<path> | wc -c`).**
`skills/agent-contract/SKILL.md` holds 11,625, against 12,029 at v0.38.5 and
11,932 at `6edff124a`. `agents/crafter.md` went from 9,427 to 9,219,
`agents/framer.md` from 15,839 to 15,634, and `agents/proofer.md` from
10,123 to 9,985, each against `6edff124a`. The release table's preload rows
are phase 3's measurement (`frame/design.md` *Scope* item 12).

**For the next phase.** `agents/crafter.md` step 10 still reads "after the
same `writing-style` section", which resolves to step 8's new wording, so
it was left as it stands.
