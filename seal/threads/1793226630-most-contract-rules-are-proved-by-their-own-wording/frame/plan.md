# Implementation Plan: 1793226630-most-contract-rules-are-proved-by-their-own-wording

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

`tests/text/test_the_agent_contract_holds_the_universal_rules.py` proves 16
of the contract's 20 rules by a phrase of each rule's own wording. This work
keeps two facts, because a reader needs their characters fixed: rule 1's
two command forms, narrowed from `PINS` row 1, and rule 11's two root
spellings, taken from another case of the same module. It removes the other
19 rows of `PINS` and seven phrase cases of the same module, two of which
fold into the facts. A structural case takes their place: every rule carries a `check:`
line. The 13 `check:` lines of `skills/agent-contract/SKILL.md` that named
the module for a pin that goes now name an eval case that reads the
behaviour, or `none reader:`. A second phase counts the phrase pins on rule
sentences in every other `tests/text` module, and the orchestrator posts the
count on #1111. `frame/design.md` *Each pin, decided* holds each row's
decision and its history.

## Technical context

- **The module at base.** `PINS` (`:38-68`) maps each rule to one phrase.
  `missing_pins` (`:112-119`) collapses whitespace and looks for the phrase
  in the rule's body. The parametrized `test_each_section_holds_its_rule`
  and `test_deleting_a_pinned_phrase_is_caught` run over every row. The
  citation resolver (`:73-83`, `:285-399`) and the heading readers
  (`:30-32`, `:402-423`) read spellings, and this work leaves them alone.
- **Who imports from it.** Five modules import `HEADING` (executed `git
  grep`): `tests/behaviour/test_a_commit_names_its_repository.py:21`,
  `tests/behaviour/test_a_probe_that_commits_says_so.py:17`,
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:18`,
  `tests/text/test_a_moved_rule_leaves_its_definition.py:76` and
  `tests/text/test_broad_gate_rule.py:25`. No module imports `PINS`,
  `FOUR_RULES`, `missing_pins` or `without_pin` (executed `git grep`).
- **What reads a `check:` line.** `seal rules --check`
  (`.github/scripts/rules.py`) reads every `check:` line of the files in
  `RULE_FILES` (`:47-55`, read). It refuses a target that is no file and an
  eval case directory without `case.yaml`. It cannot read whether a rule
  carries a line at all (`skills/settle/SKILL.md` *A rule has one shape*,
  read), which is why the new structural case is not a copy of it.
  `tests/behaviour/test_docs_line_wrap.py` skips every `check:` line that
  `rules.py#parse` reads without refusal (`:197-211`, read), so a long
  `check:` line is not a wrap failure, and a refused one still is.
- **The eval targets.** `evals/behaviour/sealer/rule-sealer-no-gate/`,
  `evals/behaviour/sealer/rule-sealer-false-red/`,
  `evals/behaviour/sealer/rule-sealer-untrue-body/` and the four
  `evals/behaviour/crafter/rule-crafter-*/` directories each hold
  `case.yaml` (executed `ls`). `evals/scripts/rule_cases.py` writes them,
  so a rename there would leave a `check:` line naming a missing path, and
  `seal rules --check` would refuse that line by name.
- **The parallel work.** #1117 edits `.claude-plugin/plugin.json`,
  `.github/`, `docs/branch-and-release.md`, `docs/release-checklist.md` and
  the release scripts (the spawn prompt, unverified; the orchestrator
  answers it). This work edits none of them. #1127 (0.24.1) later edits this
  module's citation resolver, which this work does not touch.
- **The failure scenario of the chosen approach, six months out.** A sweep
  deletes one sentence from inside a contract rule, keeps the heading and
  the `check:` line, and changes the sentence's meaning. No case is red. The
  proofer is the reader, and a proofer that reads the sweep's diff as
  mechanical lets it through. This is the case #107 and phase 5 of #107
  recorded (`frame/design.md` *Each pin, decided*), narrowed: a whole rule
  or section going is still red. The kept defence is review, and the
  `check:` lines of the rules that rest on it say so in words.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Keep every pin, and write beside each the fact it fixes. This keeps the structure | For 19 of the 20 rows the phrase is a rule sentence that no checker or shell reads, so the named fact would be a label that misdescribes the pin. The cost goes on: history shows 9 row changes in 5 commits, each forced by a rule's own rewording, and no catch on record (executed, `frame/design.md` *Each pin, decided*). The premise that keeps the structure is "a rule deleted in a sweep goes unnoticed without a pin". Checked: the numbering case is red when a section goes, and the new case is red when a section loses its `check:` line. What the premise still covers is a sentence deleted inside a rule, and review reads that | Rejected |
| B. Remove the module and move its kept checks into other modules. This replaces the structure | Five modules import `HEADING` from it, and `skills/writing-style/SKILL.md:268` and `tests/text/test_a_language_section_of_writing_style_opens_alone.py:47` name it for the citation resolver. A move rewrites seven files and gains no reader. #1127 edits the resolver in 0.24.1, and a move now would turn that work into a rebase across a rename | Rejected. The module keeps its name, the citation resolver and the heading readers, and loses the phrase pins |
| C. Replace each removed pin with a new behaviour eval case | An eval case is a paid run (`runs: 2`, `timeout_seconds: 1200`, read in `evals/behaviour/crafter/rule-crafter-slugify/case.yaml`) taken at a preload rewrite, never in CI. Rules 3, 5, 12, 13, 14, 17, 18, 19 and 20 describe a judgment, and `evals/scripts/rule_cases.py:7-8` says the graders "read files and tool calls, never a judge". A grader for them would read words again | Rejected. Existing eval cases are named where their graders read the behaviour |
| D. Remove every pin, rule 1's and rule 11's spellings included, reading the issue's three examples as a closed list | A typo in rule 1's command form, such as `2>1` for `2>&1`, is copied by every agent into a shell that runs it as written, and nothing reads it. The same holds for the `git rev-parse` spelling of rule 11 | Rejected. The shell is a reader of those characters (`frame/questions.md`, judgment 2) |
| E. Name `none reader:` on every rule that loses its pin, evals included | It throws away three readers the tree already has: the sealer cases read rules 2, 4 and 15, and the crafter cases read rule 7 | Rejected |
| F. Chosen: keep the two facts, the frontmatter keys, the headings and the citation resolver. Add one structural case for the `check:` line. Remove the rest, and name the reader on each rule | *Technical context*, the failure scenario | Chosen |
| G. Count the other modules inside phase 1 | The count reads 39 modules that phase 1 does not change. A count mixed into a build phase's record is hard to re-derive, and a fix pass over phase 1 would re-open it | Rejected. Phase 2 counts at the commit phase 1 closed |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The module after `frame/design.md` *Each pin, decided* and *The module's other phrase cases*: the fact mapping for rules 1 and 11, the structural `check:` case and its mutation case, the move case re-pointed at rule 11, and the docstring and comments rewritten. The 13 `check:` lines of `skills/agent-contract/SKILL.md` rewritten. The sentence at `tests/text/test_the_handoff_before_round_one.py:106-108` rewritten | S1 to S7 of `frame/design.md`. `bin/test` over this module, `tests/text/test_the_handoff_before_round_one.py`, `tests/github/test_rules.py` and the five importers. `bin/seal rules --check`. Each new or re-pointed case seen red, by the mutation the phase record names. The S1 probe's two outputs in the phase record | ee746f3b |
| 2 | The count of phrase pins on rule sentences in every `tests/text` module but this one, by the method of `frame/design.md` *Data & interfaces*, at the commit phase 1 closed. One row per module with its number and what it left out by kind, in `trail/phases/phase-2.md`. No file outside the work item changes | S8. The sealer re-derives one module's number from the method | d2edf674 |

## Operational impact

None for a deployer. No hook, script, config row or dependency changes.
Two acts fall to the orchestrator, because contract rule 6 withholds them
from every agent: it posts phase 2's table as a comment on #1111 before the
pull request opens, and the settle after the release writes the one rule
change of `frame/design.md` into `docs/the-broad-gate.md`.
