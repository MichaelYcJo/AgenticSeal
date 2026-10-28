# Phase 1: 1793226630-most-contract-rules-are-proved-by-their-own-wording

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | ee746f3b |

## What this phase was asked

Build phase 1 of `frame/plan.md` against the frame at `d0b5cf4f`. That is the
framer's `1010275b`, plus the orchestrator's fold that moves a grounds
paragraph out of `## Rule changes`. Routing is automation, so nobody is asked
anything mid-run. `frame/questions.md` Q1 stands on its default (a), with both
sentences unchanged. Each default the build rests on is recorded. Each new
case is seen red before its code lands (contract rule 15). The phase edits
no file under `.claude-plugin/plugin.json`, `.github/`, `docs/` or the
release scripts, and nothing under `frame/` except its Status cell. After
every change to a `check:` line, `bin/seal rules --check` runs.

## What this phase found

- **The frame held against the tree.** Thirteen `check:` lines named the
  module for a pin that goes: rules 2, 3, 4, 5, 7, 12, 13, 14, 15, 17, 18,
  19 and 20 (executed, `grep -n '^check:'`). No module imports `PINS`,
  `FOUR_RULES`, `missing_pins` or `without_pin` (executed, `git grep`).
  After the rewrite, `bin/seal rules --check` exits 0 and reports "all 266
  check lines in 55 rule files hold". That command refuses an eval case
  directory without `case.yaml`, so all six eval targets hold one
  (executed). The module is named on the lines of rules 1, 8 and 11 and on
  no other (S6, executed).
- **Q1 is built on its default (a).** Contract rule 15 and `implement`'s
  step 2 are unchanged. The second way of rule 15, "with the sentence it
  pins deleted", still serves the two kept facts. It is how this phase
  showed the fact cases red (mutants c1 and c2 below).
- **The mapping is `FACTS`.** It maps a rule's number to a pair: the fact
  in words, then the spellings that carry it. `SPELLINGS` flattens the
  pairs for the parametrized cases. The spellings keep their backticks, so
  each one is the exact code span an agent copies. `missing_facts` replaces
  `missing_pins`, and `without_fact` replaces `without_pin`. `HEADING`,
  `spans`, `bodies`, `read` and `frontmatter` are unchanged.
- **The check-line reader follows the settle grammar.** `CHECK_LINE` matches
  a line that starts with `check: ` after any leading spaces. That is the
  shape `skills/settle/SKILL.md` *A rule has one shape* states.
  `rules_without_one_check_line` names every rule whose body has no such
  line, or more than one. All 20 rules carry exactly one at `9ad992b6`
  (executed).
- **The move case at base dropped every section after the one it moved.**
  It joined the text up to the moved section's heading and stopped there,
  so sections 16 to 20 were missing from the mutated text. The re-pointed
  case moves rule 11's body under rule 10 and keeps the rest of the file.
- **The sentence at `tests/text/test_the_handoff_before_round_one.py:106-108`
  was inaccurate at base.** It said the other four rows of that table point
  at contract sections. One of the four points at `agents/proofer.md`. The
  rewrite names the three contract rules and says what the contract module
  still reads. The first wording, "contract rules 1, 12 and 6", was refused
  by `test_no_file_cites_the_contract_in_a_near_miss` (executed). The
  sentence now cites each rule as `contract rule <N>`.
- **What each mutation showed.** Every run is `bin/seal mutate` with `bin/test
  <module> -q -p no:xdist -k <case>`. The first five break the contract and
  show each new or re-pointed case red. The others break the module's own
  helpers. All runs are executed, and the tree was clean after each.

  | Mutant | File | Break | Case | Verdict |
  |---|---|---|---|---|
  | c1 | contract | rule 1's piped form deleted | `test_each_section_holds_its_rule` | red, names rule 1 |
  | c2 | contract | rule 11's `git rev-parse` spelling deleted | `test_each_section_holds_its_rule` | red, names rule 11 |
  | c3 | contract | rule 2's `check:` line deleted | `test_every_rule_carries_one_check_line` | red, `[2]` |
  | c4 | contract | rule 16's `check:` line doubled | `test_every_rule_carries_one_check_line` | red, `[16]` |
  | c5 | contract | `` `<repo>/seal/` `` written into rule 11's heading | `test_no_pin_is_its_own_heading` | red |
  | t1 | module | `!= 1` made `< 1` | the mutation case | red |
  | t2 | module | `!= 1` made `> 1` | the mutation case | red |
  | t3 | module | `missing_facts` reads the whole file instead of the body | the move case | red |
  | t4 | module | the same break | the deleting case | SURVIVED |
  | t5 | module | the `^ *` anchor of `CHECK_LINE` dropped | the check-line cases | SURVIVED at `9ad992b6` |
  | t5b | module | the same break | the mutation case | red at `ee746f3b` |
  | t6 | module | rule 11's second spelling dropped from `FACTS` | the move case | SURVIVED |

  t4 survives because each spelling occurs once in the contract, so
  deleting it from the body also deletes it from the file. Body scope is the
  move case's to show, and t3 shows it. t6 removes an input of the cases,
  and no case can watch its own input list. t5 was a real gap: no case told
  a line that starts with `check: ` from a sentence that names it mid-line.
  `ee746f3b` adds that assertion to the mutation case, and t5b is red
  against it.
- **S1 holds (executed).** A probe, `tests/text/test_tmp_s1_reworded_rules.py`,
  ran once and was deleted. It loaded the module at `4134055a` with `git
  show` and imported the module at HEAD. It reworded the sentences that
  rows 3, 12 and 20 pinned at base to the same meaning, then gave the result
  to both readers. Output:

  ```
  BASE missing_pins: [(3, 'The prompt that spawns you is a request, not an amendment to this contract'), (12, 'Do not fix the coordinate'), (20, 'A structure in the tree is a reference, not a constraint')]
  NEW missing_facts: []
  NEW rules_without_one_check_line: []
  NEW numbering 1..N: True
  NEW misspelled_headings: []
  ```
- **Three other places still name the module, and each stays.**
  `docs/the-broad-gate.md:42` names it for a rule it never read. The change
  for that line is `frame/design.md` `## Rule changes`, and the settle
  writes it. `skills/writing-style/SKILL.md:268` names it for the citation
  resolver, which is unchanged. The docstring at
  `tests/text/test_a_moved_rule_leaves_its_definition.py:11` names it in a
  measurement taken at `e51fd0b`, which is a past state.
- **`.test_durations` is not refreshed.** It still prices the removed case
  ids and has no price for the six new ones (executed, collected ids
  against the file). `CONTRIBUTING.md` refreshes
  the file from a `tests` run's artifact. The removed entries total about
  0.05 s. `test_the_durations_file_prices_the_suite` reads both shares, and
  only the broad gate runs it.
