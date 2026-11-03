# Phase 1: 1793678623-each-rule-rides-with-the-agent-that-uses-it

## What this phase found

**The reading's coordinates hold against the tree, with one off by a
line.** Outside `seal/`, the tree at 1d099e006 equals the base 0c68b9933:
`git diff --stat 0c68b9933 HEAD` lists only the frame's four files
(executed). Every line `frame/design.md` *The reading: contract rules* gives
opens the section it names, the preamble at `:16` through rule 20 at `:236`
(read). A probe measured the preamble at 715 bytes, rule 8 at 239 and rule
20 at 264 against the frame's 265 (executed). The one-byte gap is the
section's last newline. Each line the agent-definition tables name was
printed with `sed` and opens the step, rule or sentence it names (executed).
These were `agents/crafter.md`, `framer.md`, `proofer.md`, `sealer.md` and
`tracer.md`, `skills/implement/orchestration.md:364`,
`skills/implement/multi-repository.md:20`, `skills/verify/SKILL.md:144` and
`skills/code-review/orchestration.md:218`. The one miss is D3's
`skills/implement/SKILL.md:20-25`. Line 20 is blank, and the paragraph runs
from 21 to 26 (read). The claim D3 rests on stands either way.

**D2's numbering reader departs from its sentence in one place.** D2 says
"the numbers missing from 1 up to the highest heading are exactly the listed
ones". That cannot hold for D2's own list. Phase 1 lists 20, and the highest
heading is 19. Under that reading a listed 20 is a fault on the tree D2
builds. The reader runs its range up to the highest of the heading numbers
and the listed numbers. That matches D2's own preamble sentence, under which
a new rule takes the number after the highest of the retired numbers and the
rules. Judged against `frame/design.md` D2, both of its sentences.

**Q2, D2's half: the numbering sentence is worded so it reads one way.**
`frame/questions.md` Q2 gives the wording to the work. The contract's
preamble now says: "A rule number is never reused and never re-ordered. A
rule that retires leaves this file, and its number is listed here: the
retired numbers are 8 and 20. A new rule takes the number after the highest
one used, retired or not." It keeps D2's four facts: no reuse and no
re-ordering, a retired rule leaves the file, its number is listed, and the
next number comes after every one used. It is 226 bytes against D2's 237.
D2's "the highest of these and of the rules below" has two readings, since
"below" can mean lower in the file or lower in number. "The highest one
used, retired or not" has one. Judged against `skills/writing-style/SKILL.md`
*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*. The reader matches
`retired numbers are` followed by a list in the form `8 and 20` or `8, 16
and 20`, across a line break. So phase 2 adds 16 by editing the list alone.
Q2's other half, rule 11's sentence, is phase 3's. The Status cell of Q2 is
left open for that reason.

**The new cases were seen red, each in a way the cases' code shows.** All
runs were executed, and each command was `bin/test
tests/text/test_the_agent_contract_holds_the_universal_rules.py -q -p
no:xdist -k <the cases>`.

- **Against the base contract, before the contract changed.** The new cases
  ran against the base's preamble, which lists no number.
  `test_a_listed_number_that_has_a_heading_is_named` was red, exit 1, with
  `AttributeError` at `RETIRED.search(text).start(1)`. The other three
  passed.
- **Against the old case's code, before 9fa153f50.** The new contract and
  the new cases were in place. The first line of `numbering_faults`' body was
  replaced, through `Edit`, by the old case's comparison:
  `return [] if numbers == list(range(1, len(numbers) + 1)) else [numbers]`.
  `test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat`,
  `test_a_gap_the_preamble_does_not_list_is_named` and
  `test_a_listed_number_that_has_a_heading_is_named` were all red, exit 1,
  3 failed. The old code refuses the listed gap at 8, so it cannot tell a
  retired number from a lost rule. The line was removed through `Edit`, and
  the module passed.
- **The repeat case, before 0f4187f70.** The repeat check was replaced by
  `if False:` through `Edit`. `test_a_repeated_number_is_named` was red, exit
  1, with the fault for `[1, 1, 2, ...]` missing. The check was restored, and
  the module passed.

**A third planted case was added, beyond the plan's two.** At 9fa153f50,
`seal mutate` ran four mutants of `numbering_faults` and `retired` over the
four numbering cases (executed). Three were red. The mutant that disables the
repeat check SURVIVED: no planted contract repeated a number, and the old
case's code had no such case either. 0f4187f70 adds
`test_a_repeated_number_is_named`, a copy of the first section under its
own number. At 0f4187f70 the same batch went 4 mutants, 4 red, exit 0
(executed). Judged against `agents/crafter.md` *Mutation-test every unit that
adds behaviour*: a unit that stays green while broken has nothing behind it.

**The plan's failure scenario says more than the case holds.** `frame/plan.md`
*Technical context* says the numbering case refuses a retired number left
off the list. `seal mutate` on `skills/agent-contract/SKILL.md` replaced the
list `8 and 20` with `8`, and the case stayed green: SURVIVED (executed).
Listing `7, 8 and 20` was red. With 19 the highest heading, nothing else in
the file says 20 was used. Only the highest number used can go unseen like
this, from the list or as a rule. Any lower one leaves a gap the list does
not name. 1884c3c3d states that limit in the module's docstring and leaves it
to review. A guard was within reach and not taken: `gaps.md` *Not done* holds
it with its grounds.

**One removal the frame's `## Removes` did not name.** The removed case
`test_the_retired_rule_keeps_its_number_and_none_of_its_shapes` was the only
user of `section()` in `tests/behaviour/test_a_probe_that_commits_says_so.py`.
It was also the only user of the module's `HEADING` import and its `CONTRACT`
constant. All three went with the case. The module's docstring now says rule
8's number is listed as retired, and it drops the claim the case held, that
the old shapes are gone.

**Every citation of rules 8 and 20 the class holds was found, by two
listings.**

- **The case `frame/design.md` names produces the list for citations it
  reads.** `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_every_cited_section_exists`
  ran with the contract edited and nothing else (executed). It named four
  dangling `contract rule 8` citations and none of rule 20:
  `tests/behaviour/test_a_probe_that_commits_says_so.py:6`,
  `tests/conftest.py:1144`, `tests/skills/test_broad_gate.py:2625` and
  `tests/text/test_a_moved_rule_leaves_its_definition.py:46`. These are the
  four D2 names. Each was reworded where it stands. The two docstrings that
  explained a probe's commit through the retired rule lost that sentence,
  since the gate it named left with #1027.
- **A command listed the spellings that case does not read.** It was a
  regex over every tracked file outside `seal/` and `CHANGELOG.md`, each file
  read with its whitespace folded, for `rule` or `rules`, an optional list,
  then 8 or 20 (executed). Beyond the four, it found
  `tests/text/test_a_moved_rule_leaves_its_definition.py:325` and
  `tests/text/test_the_rules_have_one_owner.py:206`. The first now names "the
  retired probe rule". The second named rule 20 for the orchestrator
  committing a fix pass's close blocks, a rule
  `agents/crafter.md` *A fix pass appends close blocks and writes no phase
  record* states today, so it cites that rule.
- **Five hits remain, all in `tests/behaviour/test_a_probe_that_commits_says_so.py`.**
  Each names rule 8 as a retired number. `test_no_definition_points_a_probe_at_the_retired_rule`
  asserts no definition says `rule 8`, and its docstring and the module's say
  why. A `git grep` for `§8` and `§20` found nothing (executed). The listing
  covers the `rule N` spellings, and a sentence naming the rule some other
  way, such as "the eighth rule", is outside it. That part of the class is
  a sample, left to review.

**The policy sentence on numbering still holds.** `docs/running/the-agent-set.md`
*The contract's rule numbers are stable* says how a retired rule keeps its
number "is the contract's own preamble" (read). The preamble still says it,
as D7 states.

**The contract is 441 bytes smaller.** It was 12,906 bytes at 0c68b9933 and
is 12,465 at 1884c3c3d (`wc -c`, executed). Every agent's preload falls by
that amount. Phase 4 measures it with `release_report.py`.

**What phase 2 needs.**

- The preamble's list becomes `8, 16 and 20`, and the reader reads that
  form. Rule 16 is below the highest heading, so dropping it from the list
  would be red.
- `test_a_gap_the_preamble_does_not_list_is_named` and
  `test_a_repeated_number_is_named` plant their fault at the contract's
  first section. `test_a_listed_number_that_has_a_heading_is_named` lists
  the first heading's number. None of them names a number, so moving rule 16
  touches none of them.
- The fixtures of `tests/behaviour/test_a_cited_section_stands_in_its_file.py`
  cite one above the highest heading, now 20, a retired number. That is
  still no heading, so they still dangle as they should.
- Two lines name the old rule 16 as history, in a form the cited-section case
  does not read. One is the module docstring of
  `tests/text/test_a_moved_rule_leaves_its_definition.py`, "the old rule 16,
  now part of contract rule 11". The other is the docstring of
  `test_every_cited_section_exists`, "the old rule 17 to rule 16". Both name
  #957's numbering. Once phase 2 retires 16, the second reads as a live rule
  16.

**The phase-boundary set passed, once the records stood.** The set is 54
modules, listed by command (executed). It holds every test module naming
`agent-contract` or importing the contract module. It holds every test module
that lists tracked files or walks the tree (`ls-files`, `os.walk`, `glob`,
`rglob` or `tests/censuses.py`). It holds the two changed modules neither
listing caught: `tests/skills/test_broad_gate.py` and
`tests/text/test_the_rules_have_one_owner.py`. The change to
`tests/conftest.py` is a docstring. Each of the 54 modules imports
`conftest`, which is what that change can break. The command was
`bin/test <the 54 modules> -q`. Before the records, it went 1 failed and
3046 passed. The one failure was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which wants this work item's `gaps.md`. That failure was the missing record,
which this phase writes. With this record, `gaps.md` and the Status cell in
the working tree, the same command exited 0: 3048 passed, 12 skipped
(executed).
