# Phase 1: 1794200907-agents-write-commands-the-parser-reads

## What this phase found

**The frame holds for this phase.** `2831458a` differs from `bdac7850`,
the commit the frame read, only by the three frame files (executed: `git
diff --stat bdac7850 2831458a`). Every coordinate the phase row reaches
stood where the frame placed it. `skills/agent-contract/SKILL.md` was 214
lines long and ended with rule 19 (executed: `wc -l`). `FACTS` held entries
for rules 1 and 11, and the module docstring said "Two facts are pinned"
(read). `skills/update/SKILL.md` set `f=$(mktemp)` and removed it with
`rm -f "$f"` (read). Step 1 of `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* named no file but the core
(read). `.claude-plugin/plugin.json:4` was the only file outside
`seal/threads/` naming `0.36.0` (executed: `git grep -n '0\.36\.0'`).
Issue #1445 has one comment, the one `frame/design.md` G16 reads
(executed: `gh issue view 1445 --json title,url,comments`).

**Decision: rule 21 says a line the parser cannot read is held for a
person to approve, not that it is refused.** Claude Code asks a person
about such a line, and the transcript reading counts prompts a person
answered (`frame/design.md` G8 and G10). "Refused" would read as a
denial no person sees. The module docstring says the same: two forms the
parser reads and one it cannot. Judged against
`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다*.

**Decision: rule 21's last sentence names the two cases its examples do
not cover.** It reads "a form not named here is held to the same aim, and
so is a named form Claude Code stops reading". The second case is the
failure scenario `frame/plan.md` *Technical context* gives for the chosen
approach, where Claude Code's judgment moves and an example goes stale.
Judged against `skills/core/SKILL.md` *The rule a mechanism is kept
against*, which keeps a list of spellings out of every rule.

**Decision: the sentence in step 1 names the file that holds rule 21.**
*Scope* item 5 has the orchestrator open rule 21 "once beside the core",
and the sentence reads "which the orchestrator opens once in
`skills/agent-contract/SKILL.md` beside the core". The orchestrator does
not receive the contract at startup, so a citation by number alone does
not say where to open it. The sentence still cites `contract rule 21` in
that spelling, as `frame/design.md` *Data & interfaces* asks, and states
no form of its own. Judged against `skills/implement/SKILL.md`, the
paragraph **`skills/agent-contract/SKILL.md` binds this session too, and
only if you load it.**

**Decision: the changelog fragment's `### Process changes` table holds
one row, for step 1.** The rule asks for the table where the diff changes
a `skills/*/orchestration.md` file, and this diff changes
`skills/implement/orchestration.md`. The contract is not among the files
that rule lists, so rule 21 stands in `### Fixed` and not in the table.
Judged against `docs/layout/the-record-layout.md` *A change writes
fragments, never a shared file*.

**Seen red.** The entry for 21 went into `FACTS` before rule 21 was
written, on the tree of `2831458a`. `bin/test
tests/text/test_the_agent_contract_holds_the_universal_rules.py -q -p
no:xdist` failed 5 cases and passed 14: `test_each_section_holds_its_rule[21]`,
`test_no_pin_is_its_own_heading` with `KeyError: 21`, and the three
`test_deleting_a_pinned_phrase_is_caught[21-…]` cases with `KeyError: 21`
(executed). With rule 21 written, the module passed 19 cases (executed).

**Mutation.** After `94bfb623`, one `seal mutate` call over
`skills/agent-contract/SKILL.md` deleted each of the three pinned spellings
from rule 21's body alone, with `--tests` running
`test_each_section_holds_its_rule` under `-x -p no:xdist`. All three
mutants read `red` and the call exited 0. Each failed on its own
spelling: `rule 21 no longer holds the command forms an agent copies into
a shell, which Claude Code's parser reads: ['<the spelling>']` (executed).
The working tree was clean after the run (executed: `git status
--short`).

**The other two changes have no case, as the frame says.** The sentence
in step 1 and `rm -f "${f:?}"` in `skills/update/SKILL.md` are read at
review (`frame/design.md` S3 and S5). No case reads either, so no `seal
mutate` run can watch them.

**No unit was renamed or moved,** so no census is owed. The phase removed
nothing, matching `frame/design.md` `## Removes`.

**The phase-boundary run.** No test file outside `tests/text/` and
`tests/behaviour/` reads a path this phase changed. Every other match for
`plugin.json`, `skills/implement/orchestration.md` or the contract was a
path written into a fixture (read). So the set is the tree-wide files,
which hold the five files the plan row names, in one command: `bin/test
tests/text tests/behaviour -q`. Its first run, at `b58bd082` before this
record and `gaps.md` were written, exited 1. The only failure was
`test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
naming this work item's missing `gaps.md` (executed). The run after the
records were written is in the hand-back.

**The policy root keeps one section the settle writes.**
`docs/running/the-agent-set.md` *One contract every agent receives, and
one definition each* does not yet say what `frame/design.md` `## Rule
changes` adds about rule 21. This work item's subject is the contract and
not the policy root, so the settle writes it (`skills/implement/SKILL.md`
*Document layout — two roots, three lifetimes*).
