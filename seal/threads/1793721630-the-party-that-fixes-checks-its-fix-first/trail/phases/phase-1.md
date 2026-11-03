# Phase 1: 1793721630-the-party-that-fixes-checks-its-fix-first

## What this phase found

**The frame holds at every coordinate it builds to, with one statement of
G13 that the tree does not bear out.** At `e2449b643`, rule 12's section
stood at `skills/agent-contract/SKILL.md:151-165` with no `check:` line,
the sweep sentences at `agents/crafter.md:180-185`, step 10 at `:59-65`,
the fold paragraph at `skills/implement/orchestration.md:51-68`, and the
fix-pass paragraph at `skills/code-review/orchestration.md:71-90`.
`CRAFTERS_FOUR_RULES` stood at
`tests/text/test_a_moved_rule_leaves_its_definition.py:383-400`, the sweep
clause at `:496`, and the fold case at
`tests/text/test_the_rules_have_one_owner.py:369-381` (executed, one `sed
-n` per coordinate). G13 says no document of `docs/` states the crafter's
impact check. `docs/forms/the-round-record.md:98` says the fix pass writes
its close block "after its fix commits and the corrections its sweep made"
(executed: `git grep -n -i sweep -- docs`). The sentence stays true, since
the crafter's new rule keeps the search across the tree and its
corrections, so this phase leaves it. The design's `## Rule changes` reads
`- nothing`, and a write to the policy root is not this phase's. The
hand-back names it for the orchestrator.

**The new rule has a case of its own, not a row of `CRAFTERS_FOUR_RULES`.**
That constant is named for decision 1 of #967, and its case's docstring
reads "S4's four rules". A fifth entry would make both false. The case
`test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back`
stands in the same module, beside the fix-pass case, and reads the rule
through the group's helper `crafter_rule`. It also pins step 10's
citation of the rule (*Scope* item 4). Judged against
`frame/questions.md`'s first assumption and `agents/crafter.md` *A new
test starts from its group*.

**`crafter_rule` now matches a lead that wraps across lines.** The new
lead is 93 columns and does not fit the 88-column limit
`tests/behaviour/test_docs_line_wrap.py` reads, so it wraps. The helper
compared the raw paragraph with the lead and returned nothing; it now
compares the paragraph with its whitespace joined. The new case went red
on its first run with "lost its rule" for that reason (executed).

**Three wordings depart from the frame's drafts.**

- *Scope* item 6 keeps the close-block sentences of the fix-pass
  paragraph. Their "after its fix commits and those corrections" lost its
  antecedent when the sweep sentence went, so it reads "after its fix
  commits and the corrections its read made". The clause and comment of
  `tests/text/test_the_rules_have_one_owner.py#test_the_fix_pass_reads_the_implementers_context_before_it_resumes`
  follow. Judged against `skills/core/SKILL.md` *The rule a mechanism is
  kept against*: a change rewrites the text it amends in place.
- *Scope* item 2's draft names a file the crafter does not write as
  "`routing.md` or a frame cell other than your Status cell".
  `frame/design.md` and `frame/questions.md` hold lines, not cells. The
  first wording, "a frame file outside your Status cell", read as any
  frame file but `frame/plan.md`, and `7422e78f5` replaced it with "any
  line of the frame but your Status cell in `frame/plan.md`". Judged
  against `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
  가지로만 읽히게 쓴다*.
- The bold sentence "On the hand-back the orchestrator commits the round
  record ..." in `skills/code-review/orchestration.md` is rewrapped. The
  edit had left a line of 118 columns, which
  `tests/behaviour/test_docs_line_wrap.py` refused (executed). Its words
  did not change.

**Each changed or added clause was seen red with its sentence deleted
(contract rule 15).** Every run was a `bin/seal mutate` batch at
`e23058b4c`, and every case is a presence check (executed):

- `agents/crafter.md`, 9 mutants, 9 red, under `-k 'reads_its_range or
  fix_pass_appends'`. They deleted, one at a time, the hunk read, the
  records read, the fix in what the crafter writes, the closed set, the
  sample's naming, the `## Not done` sentence, the `check:` line, step
  10's citation and the fix pass's citation.
- `skills/implement/orchestration.md`, 3 mutants, 3 red, under `-k
  folded_into_it`. They deleted the whole-file fold, the reading after the
  fold commit, and the hand-over to the crafter.
- `skills/code-review/orchestration.md`, 1 mutant, 1 red, under `-k
  implementers_context`. It restored "those corrections".

`7422e78f5` then rewrapped lines of the crafter rule and of the fold
paragraph, and reworded the clause on the files the crafter does not
write. No clause the case
pins changed its words, and the case passed at that commit (executed).
Contract rule 12's sentences and the review file's new sentences have no
case (`gaps.md`), so no mutant was run over them.

**The S commands, at `94fef7e61` (executed).** S1 printed one line,
`skills/agent-contract/SKILL.md:169`, holding "proofer's share", and
nothing for "open part of a sample". S3 and S5 printed nothing and exited
1. S6 listed the four texts and the two test modules and nothing else
outside `seal/`. S7's seven modules passed alone in one `bin/test`
command over the tree of `e23058b4c`, 355 cases, and they are among the
boundary run below.

**The phase boundary ran as one command at `94fef7e61`, with `gaps.md`,
`changelog.md` and the Status cell written and this record not yet, 83
modules, 4296 passed and 10 skipped (executed).**
The list joins the modules that name one of the four edited files, the
modules that glob a directory's markdown, and the modules that read
`seal/threads/` from the repository root. It was built by `grep -rlE`
over `tests/`.

**The other statements across the tree of each rule this range reworded
or removed are a sample (contract rule 12).** The method was `git grep -n`
over the tree outside `seal/threads/` for "open part of a sample", "find
every other place", "by its words and by the", "folds that statement",
"reads that list against", "statements beside each coordinate", "proofer's
share", "calls a sample a sample" and "rule 12". A second `git grep -n -i`
over `agents`, `skills`, `docs`, `templates`, `hooks`, `README.md` and
`CONTRIBUTING.md` searched "sample", "left standing", "whole list",
"sweep", "reworded or removed" and "every other place stat". They listed
these, and each stands.

- `skills/agent-contract/SKILL.md:213-214`, rule 19, says a list none of
  rule 12's three methods made is a sample. Rule 12 still says so.
- The docstrings and comments that cite contract rule 12 for the class,
  in `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:18`,
  `tests/behaviour/test_a_probe_that_commits_says_so.py:48`,
  `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:314`,
  `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:73`,
  `tests/github/test_close_issues_on_release.py:994` and `:1116`,
  `tests/hooks/test_routing.py:371`,
  `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:13`
  and `tests/text/test_the_handoff_before_round_one.py:65`. Rule 12's
  first four sentences, which they cite, did not change.
- `seal/follow-up.md:47-48` name open classes under rule 12, as G15 reads.
- `docs/forms/the-round-record.md:98`, above.
