# Phase 2: 1794200907-agents-write-commands-the-parser-reads

## What this phase found

**The frame holds for this phase.** Every coordinate the phase row
reaches stood at `4c193822` where the frame placed it. `agents/crafter.md`
*Rules* named no scratch location (executed: `grep -n scratchpad
agents/crafter.md`, no match). Rule 21's removal example read "A directory
you made is removed in one `rm -rf` of the directory, never file by file in
a loop", and its check line named one module (read).
`tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`
held `ROUND_HOME` and `FRAME_HOME`, and its docstring counted four
instances of the class (read).

**Seen red.** Both cases went into the module before either sentence was
written. `bin/test
tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py
-q -p no:xdist` exited 1, with 2 failed and 4 passed (executed). The
crafter's case failed on its first assertion, "`agents/crafter.md` *Rules*
does not name a phase's directory as
`<scratchpad>/<work-item-id>/phase-<n>/`". Rule 21's case failed on its
first assertion, "contract rule 21 does not name the directory a removal
takes as one under `<scratchpad>/<work-item-id>/`". With both sentences
written, that module, `tests/text/test_a_moved_rule_leaves_its_definition.py`
and `tests/text/test_the_agent_contract_holds_the_universal_rules.py`
passed 216 cases in one command (executed).

**Mutation.** After `8b55ee74`, one `seal mutate` call over
`agents/crafter.md` made three mutants: the phase directory without
`phase-<n>/`, the fix pass directory without `fix-<n>/`, and "share one
scratchpad" written as "use one scratchpad". `--tests` ran the crafter's
case alone under `-x -p no:xdist`. All three read `red` and the call
exited 0 (executed). Each mutant removed one guard while the others held,
and "share" stands once in the section, so each red is its own
assertion's (read). A second call over `skills/agent-contract/SKILL.md`
made two mutants, one without "under `<scratchpad>/<work-item-id>/`" and
one with "never names the" written as "names the", against rule 21's case
alone. Both read `red` and the call exited 0 (executed). The working tree
was clean after each call (executed: `git status --short`).

**Decision: rule 21's example says "the removal never names the scratchpad
itself", and the case pins that phrase.** *Scope* item 6 words the clause
as "never the scratchpad itself". Joined to "is removed in one `rm -rf` of
that directory", that wording leaves the reader to supply what "never"
governs. Naming the removal as the subject gives one reading. Judged
against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다*.

**Decision: rule 21's example now names only a directory under
`<scratchpad>/<work-item-id>/`.** That narrows the example, not the rule:
the section still says its forms are examples and not a list. This is
*Scope* item 6's wording, and every agent definition that names a scratch
location names one under that directory.

**Decision: the crafter's rule says what `<n>` is in each directory.**
*Scope* item 7 defines `<n>` only for a fix pass. A phase's `<n>` is the
phase, and the rule says so, because a crafter spawned for phase 2 under
review round 1 holds two numbers either could mean. The rule stands right
after *The frame is judged before it is built to.*, because a phase's
first write outside the worktree comes before anything else it builds. It
cites rule 21 for the form of the removal and copies none of its words:
`tests/text/test_a_moved_rule_leaves_its_definition.py` passed, so no run
of the rule's words reaches the window that test holds (executed).

**Decision: the module docstring counts five instances and the clause.**
The crafter's directories are the fifth instance of the class the module
names. Rule 21's clause is not a location an agent writes to, so the
docstring names it beside the five as the same repair at the moment of
cleanup rather than as a sixth instance.

**No unit was renamed or moved,** so no census is owed. The phase removed
nothing, matching `frame/design.md` `## Removes`.

**The phase-boundary run.** No test file outside `tests/text/` and
`tests/behaviour/` reads `agents/crafter.md` or the contract.
`git grep -l` on `crafter.md`, `agent-contract` and `"agents"` over
`tests` and `evals` listed `tests/skills/test_passages.py`,
`tests/skills/test_mutation_check.py`, `tests/skills/test_payload_meter.py`,
`tests/skills/test_seal.py`, `tests/skills/test_chain_check.py`,
`tests/evals/test_noninferiority.py`, `tests/github/test_release_report.py`
and `tests/test_conftest.py` outside those two directories (executed). Each
names the path only as a parameter, in a docstring, or in a fixture it
builds, and `test_chain_check.py` opens `agents/proofer.md` alone (read).
So the set is the tree-wide files, which hold phase 1's five modules and
the scratch module, in one command: `bin/test tests/text tests/behaviour
-q`. It exited 1, with 1 failed, 1812 passed and 8 skipped (executed). The
one failure is
`tests/behaviour/test_every_tracked_file_meets_every_census.py::test_every_file_no_module_file_declares_meets_every_census`.
It names `frame/design.md:25`, G18, where the transcript path holds the
real user directory that the `real_identifiers` census refuses. That line
came in with `4c193822`, the frame fold this phase was spawned on, and
this phase's diff does not touch `frame/design.md` (executed: `git blame
-L 25,25` and `git diff --stat 4c193822 8b55ee74`). The frame is not this
phase's to write, so the hand-back names the line for the orchestrator to
fold.
