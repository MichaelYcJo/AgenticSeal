# Phase 2: 1793678623-each-rule-rides-with-the-agent-that-uses-it

## What this phase found

**The frame's coordinates for this phase hold.** HEAD before the phase was
3354cef75, which changes `frame/plan.md` alone (`git show --stat`,
executed). Each line D1 and the `## Removes` rows of this phase name opens
what they say (read). These were the contract's rule 2 and rule 16, rule
19's clause, `skills/implement/orchestration.md:364`,
`skills/implement/multi-repository.md:20`, `agents/crafter.md:53` and
`skills/verify/SKILL.md:144`. Phase 1's record named two docstrings that
call old rule 16 by its number as #957 history. Both stood where it said
(read).

**Rule 16 moved with its wording.** It stands in
`skills/implement/SKILL.md` *2.* as the bold-lead rule *A commit names its
repository in the command that makes it*, with its `check:` line. It sits
after the two paragraphs of *Commit at the smallest step that stands on its
own*, the second of which says what committing buys, and before *Before
each commit, lint, format and typecheck*. D1 places it "after *Commit at
the smallest step*", and that rule ends with its second paragraph. "A file
edit is rule 9's" became "A file edit is contract rule 9's", as D1 states.
The preamble's list now reads `8, 16 and 20`. The numbering reader read it
unchanged, as phase 1 said it would.

**Rule 2 keeps no pointer to the phase-boundary set.** D1 says rule 2 keeps
the slice tests, the broad gate and the `unverified` hand-over. Its first
sentence now ends at the slice tests. A pointer to the verify row would
cost every spawn bytes for a step only the crafter and the session that
builds take, and both reach the row without the contract: crafter step 7
cites it, and the session reads `verify`. Judged against
`skills/core/SKILL.md` *A document is cut by who opens it and at which
step, so a party opens only what its step needs*.

**The verify row states the set in rule 2's words.** The *Phase boundary*
row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*
read "the set contract rule 2 names for a phase boundary". It now holds the
set: the cases the phase's plan row names and the test modules that read a
path the phase changed, whether they name it, import it or glob the
directory that holds it. Crafter step 7 cites that row and section.

**Rule 19 keeps "or corrects".** D3's row says rule 19 cites the core for
the rule and keeps the method. The core's *The rule a mechanism is kept
against* says the same commit "removes what stood on the old fact". The old
rule 19 said "removes or corrects", and a re-pointed citation is corrected,
not removed. So rule 19 now cites the core for the rule. It then says that
what stood on the old fact, which the same commit removes or corrects, is
every other sentence, case and citation stating it. The `git grep` method,
the sample rule and the sentence on corrections written beside are kept.
Judged against `frame/design.md` D3, the rule-19 row, and the core's
section.

**The two citations of rule 16 cite the rule's lead, not the section.**
D1 says the citations go to the rule's new home. Section *2.* runs to 79
lines and holds six bold-lead rules (`awk`, executed). The lead names the
one rule. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves
a bold lead as it resolves a heading (read: its module docstring and
`test_a_bold_rule_lead_resolves_outside_a_fence_and_case_for_case`). Both
`skills/implement/orchestration.md` and
`skills/implement/multi-repository.md` now cite `skills/implement/SKILL.md`
*A commit names its repository in the command that makes it*.

**The move was proved by the existing cases at the new path.**
`tests/behaviour/test_a_commit_names_its_repository.py` read rule 16's body
from the contract. It now reads the paragraph from the bold lead through
its `check:` line in `skills/implement/SKILL.md`. Its four cases keep their
assertions, with three changes, each one a fact the move changed:

- Two cases are renamed. `test_the_rule_is_section_sixteen_and_names_the_shape`
  is now `test_the_rule_stands_in_implement_and_names_the_shape`, and
  `test_the_orchestration_cites_contract_rule_16` is now
  `test_the_orchestration_cites_the_rule`. Each old name stated a number
  that is now retired.
- The edit-rule case reads `contract rule 9`, the form the rule now
  writes. The orchestration case reads the new citation.
- The module docstring said
  `tests/text/test_a_moved_rule_leaves_its_definition.py` refuses a copy of
  the rule. That module reads each contract section against `agents/*.md`,
  and the rule is no longer a section, so that sentence went.

No case was written new and no `seal mutate` run was taken, since a move
adds no behaviour (`skills/verify/SKILL.md` *The narrow command still has
to be able to fail*, the *Names or places only* row).

**`tests/text/test_broad_gate_rule.py` needed no retargeting.** The plan's
*Verified by* cell names it as retargeted at the new homes. None of its
cases reads rule 2's phase-boundary sentence (read). Its crafter case reads
`rule 2` and `rule 3` in `agents/crafter.md`, and both still stand, in *The
broad gate is not yours* and step 10. The eval
`evals/behaviour/sealer/rule-sealer-no-gate/`, rule 2's other `check:`
target, does not name the set either (`grep`, executed). So the set was
held by no case in the contract, and it is held by none in the verify row.
`gaps.md` *Not verified* holds that.

**Every citation of rule 16 and of the phase-boundary set was listed, by
two methods.**

- **The case the design names produced the list for citations it reads.**
  A detached worktree at 3354cef75 took the new contract and nothing else.
  There, `test_every_cited_section_exists` failed, exit 1, and named four
  dangling citations (executed):
  `skills/implement/multi-repository.md:20`,
  `skills/implement/orchestration.md:364` and
  `tests/behaviour/test_a_commit_names_its_repository.py:3` and `:70`.
  The worktree was then removed. At d68e9b1d6 the same case passes.
- **A search listed the spellings that case does not read.** It was a
  `git grep` outside `seal/` and `CHANGELOG.md` for `rule` or `rules`, an
  optional list, then 16, or `phase-boundary set`, or `set contract rule 2`
  (executed). At 3354cef75 it found 11 lines. They were the four above, the
  module docstring's `rule 16 names` at `:1` and the two failure messages
  at `:53` and `:60` of the same module, `agents/crafter.md:53`,
  `skills/verify/SKILL.md:144`,
  `tests/text/test_a_moved_rule_leaves_its_definition.py:53` and
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py:647`. At
  d68e9b1d6 it finds none, exit 1 (executed). A Python pass with whitespace
  folded across line breaks, which also matched `§16` and `contract's
  rule`, found none either (executed).
- The two docstrings that named #957's numbering were reworded. One now
  says "a rule #957 folded into contract rule 11". The other says a rule
  that moves or retires leaves its number behind.
- The comment above `RETIRED` in
  `tests/text/test_the_agent_contract_holds_the_universal_rules.py` gave
  `8 and 20` as its example. It now gives `8, 16 and 20`.
- The list is whole for the `rule N` spellings and the set's two names. A
  sentence that names the rule in other words, such as "the commit rule in
  the contract", is outside it. That part of the class is a sample, left to
  review. No `docs/` file named either (the same searches).

**The contract is 896 bytes smaller.** It was 12,465 bytes at 3354cef75 and
is 11,569 at d68e9b1d6 (`wc -c`, executed). `agents/crafter.md` grew 66
bytes, from 10,952 to 11,018, because step 7 now names the verify row and
section. So the crafter's preload falls by 830 bytes, and each other
agent's by 896. `skills/implement/SKILL.md` grew 721 bytes, to 26,127, and
`skills/verify/SKILL.md` grew 111, to 15,208 (`wc -c`, executed). Phase 4
measures the preloads with `release_report.py`.

**The phase-boundary set passed.** The set was 84 modules, listed by
command (executed). It holds the plan row's four modules. It holds every
test module that names the contract, `crafter`, the `agents` directory,
implement's `SKILL.md` or `orchestration.md`, `multi-repository`, or
verify's `SKILL.md`. It holds every module that imports one of the four
changed test modules, and every module that lists or walks the tree
(`ls-files`, `os.walk`, `glob(`, `rglob` or `censuses`). The command was
`bin/test <the 84 modules> -q`, and it exited 0: 3407 passed, 11 skipped
(executed). It ran at d68e9b1d6, before this record and `gaps.md`'s rows
were written. With this record, the two rows and the Status cell in the
working tree, the 58 test modules that name `threads`, `gaps.md` or
`phases/` ran in one `bin/test` command and exited 0: 4271 passed, 1
skipped (executed). `git grep -n "contract rule 16"` outside `seal/` lists
nothing, exit 1 (executed).

**What phase 3 needs.**

- The contract has 17 sections. `tests/text/test_a_moved_rule_leaves_its_definition.py`
  asks for at least 16, so it still holds.
- `agents/crafter.md` step 1 still holds the plugin-path sentence, and step
  7 now sits between it and phase 3's other removals. Step 7's citation is
  66 bytes, and phase 3's removals from the crafter outweigh it.
- Rule 11's half of Q2 is still open, as phase 1 left it.
