# Phase 2: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

## What this phase found

**The frame holds against the tree at `e7b4821b5`.** Phase 1 changed none
of `skills/implement/SKILL.md`, `templates/setup/config.md`,
`lib/config.py`, `skills/settle/SKILL.md` or `tests/lib/test_config.py`
(executed: `git diff --stat 6edff124a e7b4821b5`). So every coordinate
`frame/design.md` *Scope* items 1, 10 and 11 give stood at its line. Each
landing place the *Removes* table names for those items stands where
*Grounding* G8 says (read). These are step 1 of
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*, the batch section, the drain section and *Under agentic*, the
paragraph **Three returns and stop.** of `skills/verify/orchestration.md`,
and the no-rebase paragraph of `skills/code-review/orchestration.md`.

**One citation the frame did not name pointed at a removed paragraph.**
`skills/code-review/orchestration.md:94-95` said the contract binds the
orchestrator "as the opening of `skills/implement/SKILL.md` states". That
opening is the paragraph *Scope* item 1 removes first. The sentence now
cites step 1 of `skills/implement/orchestration.md` *Orchestrator: the
order inside a ticket*. That is where the frame's *Removes* row lands the
paragraph, and where the orchestrator opens the contract beside the core.
The citation was found by listing every citation of
`skills/implement/SKILL.md` across the tree, with its whitespace folded and
its context printed, and reading each one for which paragraph it means
(executed). This was judged against contract rule 19 and
`frame/design.md` *Removes*. No case pinned the old wording (executed:
`git grep -n -F 'binds you too' -- tests` printed nothing).
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves the
new citation, and it passed in the boundary run below. Phase 3 should
know one effect of this re-point. It adds 72 bytes to
`skills/code-review/orchestration.md`: 38,635 at `6edff124a` and 38,707
at `c3c80da33`. `frame/design.md` S3 asks that file to be smaller than at
`6edff124a` once phase 3 has cut it.

**T1 drops the `agentic` clause of the paragraph it replaces.** The old
paragraph said that under `agentic` the choice is the orchestrator's and
weighs the ladder, and it named *Under agentic*. T1 says the choice is the
orchestrator's by the ladder. The crafter acts on neither clause, and
`skills/implement/orchestration.md` *Under agentic* still states the choice
for the orchestrator, who opens that file. The paragraph after T1 opens
"`questions.md` is not on that ladder", and T1 still names the ladder, so
that sentence still has a referent. Judged against `frame/design.md`
*Data & interfaces* T1.

**What each removal took, and what stays beside it.** *Scope* item 1 took
ten spans. Each was taken whole, at the bounds the frame gives. The
sentence "Three failed fixes stop the work" and its second sentence stay.
`skills/verify/orchestration.md` still cites them as "the three-fix rule".
The Phases paragraph now ends at "not at the end.". Section 5 now holds
the fix-pass paragraph alone. `skills/implement/SKILL.md` went from 26,353
bytes at `6edff124a` to 22,114 at `c3c80da33`. `templates/setup/config.md`
went from 36,591 to 36,164, and `skills/settle/SKILL.md` from 28,885 to
28,802 (executed: `git show <rev>:<path> | wc -c`).

**The moved text owes no case of its own.** Every change in this phase
deletes text, moves a fact into the docstring that already held half of
it (T14), or re-points a citation. So it is proved as
`skills/verify/SKILL.md` *The narrow command still has to be able to
fail* says for a move: by the existing cases and by the census of the old
spelling. No case was written new, and no `seal mutate` ran, because no
unit adds behaviour. At `c3c80da33`, the plan row's census was
`git grep -n -F '<pattern>' -- <pathspec>` for each G21 pattern located
in the three files. Each printed nothing (executed). The patterns were:
`binds this session too`, `not audience`, `avoidable cost`,
`assert old in text`, `returns through the broad`, `is not decoration`,
`Nothing measures from the column`, `never rebased`,
`Findings from reading` and `rows still open to their destinations` in
`skills`; `Pact notify` and `0.3.x` in `templates`; and `No gate refuses`
in `skills/settle`.

**The other statements of each removed fact still stand where the frame
says (executed, a sample in contract rule 12's sense).** The search was
`git grep` over the tree outside `seal/threads/`. Its words were the
phrases of each removed span: `An edit must be able to fail`,
`assert the landing`, `whatever number of issues`, `Where feature
branches squash`, `orphan them earlier`, `unsettled work item`,
`refuses a branch`, `driving the work directly`, `binds you too`,
`Pact notify` and `0.3.x`. The remaining statements are these:

- contract rule 9;
- `README.md:127`, a person's document, on the batch;
- `skills/settle/SKILL.md:72-73`, on the unsettled work item;
- `lib/config.py#reference_roots` and the comments of the 0.3.x fixtures
  in `tests/`;
- `skills/code-review/orchestration.md` on the rebase.

None contradicts the tree at `c3c80da33`. The search does not reach a
sentence that states one of these facts in other words.

**The two docstrings of `tests/lib/test_config.py` now cite
`lib/config.py#pact_declaration`.** That docstring now states the fact the
removed *Pact* paragraph stated: no command refuses, prints or names a
`Pact notify` key. The *Pact* section of `templates/setup/config.md`
stays, so the old citation would still have resolved. But it would have
sent the reader to a section that no longer says it. This was judged
against `frame/design.md` *Scope* item 10.

**The phase boundary set was run in one command (executed).** At
`c3c80da33` it was `bin/test -q tests/text tests/behaviour` followed by the
modules outside those two directories that one of three lists names:

- the plan row's `git grep -l -E` lists;
- `git grep -l -E 'code-review.{0,6}orchestration|"code-review", "orchestration\.md"' -- tests`,
  for the files that read `skills/code-review/orchestration.md`;
- the files that import `lib/config.py`.

`tests/conftest.py` and `tests/run_tests.py` were left out. The first is
a fixture module and the second is the runner. It gave 3322 passed and 10
skipped. The plan row's command alone gave 2907 passed and 9 skipped
before the commit, over the same tree.
