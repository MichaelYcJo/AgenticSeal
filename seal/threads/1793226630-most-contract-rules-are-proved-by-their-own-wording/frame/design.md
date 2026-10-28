# Feature Specification: 1793226630-most-contract-rules-are-proved-by-their-own-wording

Issue #1111. The base is `4134055a` on `release/v0.24.0`, and this work
item's branch is `chore/1111-most-contract-rules-are-proved-by-their-own-wording`.
Every coordinate below is read at that base unless it names another commit.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against*: "A mechanism stays only while its history shows what it caught against what it costs" | Each pin is decided by what its history shows it caught and what it cost. *Each pin, decided* below gives both for all 20 rows of `PINS` |
| The same section: "A check gates only a fact it reads; a noisy reading, or one guessed from words, is a report", and "A rule's proof is the test or behaviour eval its `check:` line names" | A pin stays only where its phrase is a fact some reader needs fixed. A rule whose pin goes has its `check:` line name what reads the behaviour, or `none reader:` |
| The same section: "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact" | The module's docstring, the docstring sentence of `tests/text/test_the_handoff_before_round_one.py:106-108` that leans on these pins, and the 13 `check:` lines that name the module go in the commit that removes the pins |
| `skills/settle/SKILL.md` *A rule has one shape* | A `check:` target is a file, an eval case directory `evals/behaviour/<agent>/<case>/` holding `case.yaml`, or a marker. A rule with no case reads `check: none reader: <who reads it>` |
| `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*: "A rule no case can hold says `check: none reader: <who reads it>`, and the reader is who holds it instead" | The rules no case reads name their reader. `the proofer at review` is the tree's usual spelling (12 lines, executed `git grep -c`). `the orchestrator at each hand-back` is new, for the two rules whose breach only a hand-back shows |
| #956's audit, row R38 (the comment of 2026-10-28 on #956, read): positive phrase pins `refuses`, lets through `no`, fix `none: #1111` | A phrase pin stops nothing the check exists to stop. Its one effect is that a rule reworded to the same meaning turns a case red. This work is where each one is decided |
| #956's audit, row R40 (read): the `test_tmp_` grader passes a leftover named `tmp_test_x.py`, fix `#1038` | Rule 7's new `check:` line names the crafter eval cases with that let-through known. #1038 owns the grader's fix, and this work does not touch it |
| `skills/implement/SKILL.md` *Document layout, two roots, three lifetimes*: the policy root "is the baseline, and a pull request does not edit it" | `docs/the-broad-gate.md:42` names the module for a rule the module does not read. The change goes in `## Rule changes` below, and the pull request does not edit `docs/` |
| Contract rule 6: "post nothing, push nothing, open no pull request, and spawn no agent" | The crafter writes the per-module count into its phase record. The orchestrator posts it on #1111, which is the issue's second *Done when* |
| Contract rule 15 | Each case this work adds or re-points is seen red before it is committed, and the phase record says how |

## Scope

**In.**

1. Every phrase pin on a rule sentence in
   `tests/text/test_the_agent_contract_holds_the_universal_rules.py`. That
   means the 20 rows of `PINS` (`:38-68`), which the issue's first *Done
   when* names, and the seven other cases of the same module that assert a
   phrase of the contract's prose (*The module's other phrase cases* below).
   The issue says the work "starts with the contract module", so the whole
   module is in, and the other modules are counted.
2. The `check:` lines of `skills/agent-contract/SKILL.md` that name the
   module for a rule whose pin goes: rules 2, 3, 4, 5, 7, 12, 13, 14, 15,
   17, 18, 19 and 20 (13 lines, executed `grep -n '^check:'`).
3. What stood on the old fact: the module's docstring (`:1-20`), the
   comments above `PINS` (`:34-37`, `:40-43`, `:49-54`), and the sentence of
   `tests/text/test_the_handoff_before_round_one.py:106-108` that says the
   module "pins from the other side" the contract rules that a table there
   names.
4. The count the issue's second *Done when* asks for: the phrase pins on
   rule sentences in every other `tests/text` module, each module with its
   number, written into phase 2's record for the orchestrator to post.
5. One rule change in `docs/the-broad-gate.md`, stated below and written by
   the settle after the release.

**Out.**

- **Phrase pins on contract sentences in other modules.** They are
  `tests/text/test_edits_go_through_the_edit_tool.py` (rule 9),
  `tests/behaviour/test_a_commit_names_its_repository.py` (rule 16),
  `tests/behaviour/test_a_probe_that_commits_says_so.py` (rules 7 and 8),
  `tests/text/test_broad_gate_rule.py:189-210` (rule 2) and
  `tests/text/test_the_handoff_before_round_one.py:62` (rule 5), all read.
  The issue's *What changes* starts with the contract module and has the
  rest counted. The `tests/text` ones are in the count, and those under
  `tests/behaviour` are named here so the next work item finds them.
- **The two pins outside the contract that the issue names.**
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:839-859`
  (moved by #1040 from `:883-886` at `0b75346f`, read at both) and
  `tests/text/test_broad_gate_rule.py:54-55` (read). The second is in the
  count. Neither is decided here, for the same reason.
- **Negative pins**, which assert that a spelling is absent. They are #956's
  row R37, and #1038 owns them. The count leaves them out.
- **Output pins**, which assert a message a person reads (contract rule
  14's application, for example `tests/hooks/test_dispatch.py:48`). They pin
  text a script prints, not a rule sentence, and the count leaves them out.
- **The citation resolver in this module** (`CITATION`, `BARE_CITATION`,
  `NEAR_CITATION` and the cases at `:285-399`). It reads citation
  spellings, which is a fact by the issue's own list. #1127 (0.24.1)
  widens its reach, and this work does not touch it.
- **A new rule about phrase pins.** `CLAUDE.md` *The rule a mechanism is
  kept against* already holds both halves, and the issue applies them. A
  sentence restating them elsewhere would be a second source.
  `frame/questions.md` Q1 asks the owner about contract rule 15's wording.
- **Every file on #1117's list.** This work edits none of
  `.claude-plugin/plugin.json`, `.github/`, `docs/branch-and-release.md`,
  `docs/release-checklist.md` or the release scripts, and it does not edit
  `CLAUDE.md`.

## Each pin, decided

The test for every row is the issue's: a pin stays where its phrase is a
fact a reader needs fixed, such as a citation's spelling, a heading a reader
resolves, or a word a checker matches. A command spelling that an agent
copies into a shell counts as that kind of fact, because the shell reads
it character by character (`frame/questions.md`, judgment 2).

**What history shows the pins caught.** Executed: `git log --follow` on the
module lists 11 commits from `438cffe4` (#123) to `e391ea04` (#1099). A diff
of each one restricted to `PINS` rows shows 9 row changes in 5 commits:
`7f70e287` (#120) moved rows 2 and 7, `86256492` (#671) added the row for
the commit rule, `2fc33333` (#957) moved row 2, merged the root-path row
into rule 11, renumbered the commit rule to 16 and added rows 17 to 20,
`4a6e24f6` (#969) moved row 2, and `61a8455a` (#1027) moved row 8. Every
change came in the same commit as the rule's own rewording. Executed: `git
log --all -S'test_each_section_holds_its_rule'` lists 8 commits, and none
of their subjects is a repair of a rule lost by mistake. Executed: `git
grep` of the module's name over `seal/` finds it in no round record as a
red case. So no catch is on record for any row. One limit applies: a red
run repaired before its commit leaves no trace, so "no catch on record" is
not "never red".

**What the pins were built against.** The module's docstring (`:3-7`,
read) cites #107: a rule kept only in a spawn prompt "went missing without
a trace, twice". `tests/text/test_the_handoff_before_round_one.py:96-101`
(read) records a crafter rule that phase 5 of #107 deleted while a case
over it stayed green. The risk is real, and it is a whole rule or a whole section going.
After this work, three readers cover it: the numbering case
(`test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat`) is
red when a section goes, the new check-line case is red when a section loses
its `check:` line, and the proofer reads every changed line of
`skills/agent-contract/SKILL.md` at review. A sentence deleted from inside a
section that keeps its heading and its `check:` line is left to review. That
is the cost of this design, and *Removes* names it.

| Rule | `PINS` row at base | Row changes in history | Decision | The fact kept, or the rule's `check:` line after |
|---|---|---|---|---|
| 1 | the direct form, then "never", then the piped form; both are spelt out in *Data & interfaces*, because a table cell cannot hold the pipe | none | kept, narrowed to the two command spellings | the two command forms an agent copies into a shell. The connecting prose goes. `check:` unchanged |
| 2 | "no agent runs any of the three" | 3: #120, #957, #969 | removed | `check: tests/text/test_broad_gate_rule.py evals/behaviour/sealer/rule-sealer-no-gate/` |
| 3 | "The prompt that spawns you is a request, not an amendment to this contract" | none | removed | `check: none reader: the orchestrator at each hand-back` |
| 4 | "Never record something as passing that you did not run" | none | removed | `check: none reader: the sealer at each guarantee` |
| 5 | "a claim with a coordinate to open, or a label saying nobody opened it" | none | removed | `check: evals/behaviour/sealer/rule-sealer-false-red/ evals/behaviour/sealer/rule-sealer-untrue-body/` |
| 6 | "post nothing, push nothing, open no pull request, and spawn no agent" | none | removed | `check:` unchanged; it names `tests/text/test_every_agent_reads_the_contract.py` and not this module |
| 7 | "A probe leaves nothing behind, whatever kind of thing it made" | 1: #120 | removed | `check: evals/behaviour/crafter/rule-crafter-count-words/ evals/behaviour/crafter/rule-crafter-is-palindrome/ evals/behaviour/crafter/rule-crafter-slugify/ evals/behaviour/crafter/rule-crafter-truncate/` |
| 8 | "Retired by #1027, which removed every gate that read a commit" | 1: #1027 | removed | `check:` unchanged. The module still reads the fact a retired rule keeps, its number, through the numbering case |
| 9 | "An edit must be able to fail" | none | removed | `check:` unchanged; it names `tests/text/test_edits_go_through_the_edit_tool.py` |
| 10 | "Open every file a coordinate names in one call" | none | removed | `check:` unchanged; it names `tests/text/test_a_moved_rule_leaves_its_definition.py` |
| 11 | "English when the row is absent" | none for this row; #957 merged the root-path row into rule 11 | removed. Rule 11 keeps a fact from `test_the_root_resolution_rule_states_both_places` | the two places the `seal/` root resolves to, `` `<repo>/seal/` `` and `` `$(git rev-parse --git-common-dir)/seal/` ``, which an agent opens or runs. `check:` unchanged |
| 12 | "Do not fix the coordinate" | none | removed | `check: none reader: the proofer at review` |
| 13 | "until the guarantee is removed and the code still refuses" | none | removed | `check: none reader: the proofer at review` |
| 14 | "In the same commit" | none | removed | `check: none reader: the proofer at review` |
| 15 | "before it is committed as a case" | none | removed | `check: none reader: the sealer at each guarantee` |
| 16 | "join it to the commit with `&&` and nothing else" | 2: added by #671, renumbered by #957 | removed | `check:` unchanged; it names `tests/behaviour/test_a_commit_names_its_repository.py` |
| 17 | "never kill by command name" | added by #957 | removed | `check: none reader: the orchestrator at each hand-back` |
| 18 | "never bend the code to pass it" | added by #957 | removed | `check: none reader: the proofer at review` |
| 19 | "removes or corrects what stood on the old fact" | added by #957 | removed | `check: none reader: the proofer at review` |
| 20 | "A structure in the tree is a reference, not a constraint" | added by #957 | removed | `check: none reader: the proofer at review` |

**Why each eval case is the reader it is.** Every target below holds
`case.yaml` (executed `ls`).

- Rule 2: the `shape-runs-no-broad-run` grader allows no Bash call matching
  `seal\s+gate\s+--base` (read,
  `evals/behaviour/sealer/rule-sealer-no-gate/graders/shape-runs-no-broad-run.md`).
  All five sealer cases carry it. `rule-sealer-no-gate` is named because in
  that case no broad run is on record, so it is the case where an agent is
  most drawn to run the gate itself. `tests/text/test_broad_gate_rule.py`
  stays on the line, because its rule-2 cases are out of scope here.
- Rule 5: the truth graders of `rule-sealer-false-red` and
  `rule-sealer-untrue-body` pass only where the sealer re-ran a party's
  claim instead of taking the record's word for it (read), which is rule 5
  done by the agent under test. Rules 4 and 15 name no eval case: that
  case's graders read whether the sealer catches the crafter's breach,
  which is the sealer's own rule (`agents/sealer.md:132-136`), and none
  reads the sealer's own labels or its own red runs (round 1, finding 2).
- Rule 7: each crafter case carries `shape-no-probe-left`, a `not_contains`
  over `test_tmp_` in the fixture's files (read). No case is privileged
  over the others, so all four are named. R40's let-through stands and is
  #1038's.

## The module's other phrase cases

| Case at base | What it asserts | Decision |
|---|---|---|
| `test_the_contract_is_a_skill_that_preloads_and_is_not_a_command` (`:125-134`) | `name: agent-contract`, `user-invocable: false`, and no `disable-model-invocation: true` | kept. These are frontmatter keys the harness reads, so each is a word a checker matches |
| `test_the_description_says_what_it_is_and_what_it_is_not` (`:137-144`) | four description phrases | removed. No checker reads them. `NOT for:` is read by `tests/behaviour/test_chain_hooks_hardening.py:307` only for skills that block model invocation, which the contract does not (read) |
| `test_every_pinned_section_exists_and_nothing_is_unpinned` (`:155-158`) | every section has a `PINS` row | removed. It is the rule this work retires |
| `test_no_pin_is_its_own_heading` (`:161-164`) | no pin is satisfied by its heading | kept, over the two kept facts |
| `test_the_contract_says_it_is_universal_only` (`:167-170`) | two sentences of the opening paragraph | removed |
| `test_the_numbering_rule_is_stated` (`:173-176`) | two phrases of the numbering sentence | removed. The numbering case reads the numbering itself |
| `test_each_section_holds_its_rule` (`:182-186`) | every `PINS` phrase inside its body | kept, over the two kept facts |
| `test_the_exit_code_rule_carries_both_forms_in_one_sentence` (`:189-198`) | both forms in one paragraph, with `never` and `always 0` | folded into rule 1's fact. The paragraph test and the two words go |
| `test_the_root_resolution_rule_states_both_places` (`:201-212`) | both root spellings, and the root before `Record language` | folded into rule 11's fact. The prose spans (`means ... where`, `otherwise`) and the order assertion go |
| `test_the_leavings_rule_says_whose_leaving_it_is` (`:215-243`) | three phrases of rule 7 | removed. Rule 7's reader is the crafter eval cases |
| `test_deleting_a_pinned_phrase_is_caught` (`:259-265`) | deleting a pin turns it red | kept, over the two kept facts |
| `test_moving_a_sentence_to_another_section_is_caught` (`:268-279`) | rule 15's body moved under rule 14 is caught | re-pointed at rule 11's fact moved under rule 10. The scoping to a section stays shown red |
| `FOUR_RULES` and `test_the_four_rules_stand_with_their_enforcers` (`:70-71`, `:426-435`) | rules 17 to 20 keep their `PINS` phrase and a `check:` line | replaced by one case: every `## <N>` body holds exactly one line that starts with `check: `. `seal rules --check` cannot read whether a rule carries the line at all (`skills/settle/SKILL.md` *A rule has one shape*, read), and every rule has one at base (20 lines, executed) |
| `test_dropping_an_enforcer_from_one_of_the_four_is_caught` (`:438-444`) | the case above can fail | re-pointed at any rule |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A rule is reworded to the same meaning | Given the contract with the sentences that rows 3, 12 and 20 pinned at base reworded to the same meaning, when the module runs, then it passes | Phase 1: a `test_tmp_` probe feeds the reworded text to the module's readers at base (red) and after the change (green), then is deleted. The phase record carries both outputs |
| S2 A kept fact goes | Given rule 1's piped form or rule 11's `` `$(git rev-parse --git-common-dir)/seal/` `` deleted from its body, when the module runs, then the case names that rule | `test_deleting_a_pinned_phrase_is_caught`, over the facts |
| S3 A kept fact moves | Given rule 11's fact moved under rule 10, when the module runs, then rule 11 is named | the re-pointed move case |
| S4 A rule loses its `check:` line | Given any rule's `check:` line deleted, when the module runs, then that rule is named | the new check-line case and its mutation case, each seen red |
| S5 Every `check:` line resolves | Given the 13 rewritten lines, when `seal rules --check` reads the contract, then no line is refused, and every eval target holds `case.yaml` | `bin/seal rules --check`, and `bin/test tests/github/test_rules.py` |
| S6 Only rules the module reads name it | Given the contract after the change, when its `check:` lines are listed, then the module is named on the lines of rules 1, 8 and 11 and no other | `grep -n '^check:' skills/agent-contract/SKILL.md` |
| S7 The importers still run | Given the five modules that import `HEADING` from this one, when each runs, then each passes | `bin/test` over `tests/behaviour/test_a_commit_names_its_repository.py`, `tests/behaviour/test_a_probe_that_commits_says_so.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py` and `tests/text/test_broad_gate_rule.py` |
| S8 The count is recorded | Given every `tests/text/*.py` module but this one, at the commit phase 1 closed, when each is read by the method below, then phase 2's record holds one row per module with its number, and the commit | phase 2's record. The sealer re-derives one module's number |

## Data & interfaces

**The module after the change.** `PINS` is replaced by one mapping, from a
rule's number to the fact it fixes and the spellings that carry the fact.
It holds two rules:

- Rule 1. Fact: the two command forms an agent copies into a shell.
  Spellings: `` `cmd >/dev/null 2>&1; echo $?` `` and `` `cmd | tail; echo $?` ``.
- Rule 11. Fact: the two places the `seal/` root resolves to, which an
  agent opens or runs. Spellings: `` `<repo>/seal/` `` and
  `` `$(git rev-parse --git-common-dir)/seal/` ``.

The fact is written beside its spellings in the mapping, so a reader of the
module sees what each one fixes, which is the first *Done when* of the
issue. The names of the mapping and of its helpers are the build's.
`HEADING`, `spans`, `bodies` and `read` keep their names and behaviour,
because five modules import `HEADING` (executed `git grep`). The module
keeps its file name, because `skills/writing-style/SKILL.md:268` and
`tests/text/test_a_language_section_of_writing_style_opens_alone.py:47` name
it for its citation resolver.

**The count's method.** The corpus is every `tests/text/*.py` file except
this module, at the commit phase 1 closed. A phrase pin on a rule sentence is
an `assert` whose test is `<string literal> in <expression>`, where all of
these hold:

- the operator is `in`, not `not in`;
- the expression is text read from a Markdown file of the tree;
- the literal is prose of that file, and not one of these: a citation, a
  heading (it opens with `#`), a path, a `check:` line or one of its words,
  a field name or marker a checker reads, or a fenced block's content.

A literal built by an f-string or `.format` counts when its fixed text
meets the same test. The build may list candidates with a probe (contract
rule 7) and decide each one by reading it. Phase 2's record gives each
module's number and, beside it, the number of asserts it left out by kind.
The issue's figure of 182 is its own grep, which counts only lines that
open with a long literal, so it is no bound on this count; the method
sizes it.

**The one policy line this work changes.** The rule above the `check:`
line in `docs/the-broad-gate.md` *One act, one owner, and the owner is the
orchestrator* is "A suite that is not mentioned reads as a suite that
passed" (`docs/the-broad-gate.md:39-42`, read). The contract module reads
none of it at base or after this work. `PINS` row 2 is "no agent runs any
of the three", and the module has no other assertion on the label (read).
`tests/text/test_broad_gate_rule.py:142-149` asserts that
`agents/crafter.md` hands the suite over labelled `unverified` with the
orchestrator named as its answerer (read), so it is the reader the line
names in its place, through the item below.

## Rule changes

- change
  file: docs/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: check: tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_every_agent_reads_the_contract.py
  to: check: tests/text/test_broad_gate_rule.py tests/text/test_every_agent_reads_the_contract.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| 19 rows of `PINS` (2 to 20), and the prose half of row 1 | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#PINS` | No history of a catch (*Each pin, decided*). Each rule's `check:` line names its reader, as the table there says |
| The rule that every section has a pin | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_every_pinned_section_exists_and_nothing_is_unpinned` | It is the mechanism this work retires. A section that goes is red in the numbering case |
| Four phrases of the contract's description | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_description_says_what_it_is_and_what_it_is_not` | No checker reads the description's prose for this skill |
| Two sentences of the opening paragraph | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_contract_says_it_is_universal_only` | Prose pins. The proofer reads them at review |
| The numbering sentence's two phrases | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_numbering_rule_is_stated` | The numbering case reads the numbering itself |
| The one-paragraph test and the words `never` and `always 0` of rule 1 | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_exit_code_rule_carries_both_forms_in_one_sentence` | The two command spellings stay as rule 1's fact |
| The prose spans of rule 11 and the order of root and config | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_root_resolution_rule_states_both_places` | The two root spellings stay as rule 11's fact |
| Three phrases of rule 7 | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_leavings_rule_says_whose_leaving_it_is` | Rule 7's reader is the four crafter eval cases |
| The four-rule constant and its phrase half | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#FOUR_RULES` | One case reads a `check:` line in every rule |
| A sentence deleted from inside a rule that keeps its heading and its `check:` line is no longer red | `skills/agent-contract/SKILL.md`, every rule | The proofer reads every changed line of the contract at review. This is the cost the design accepts |
| The module named as the reader of 13 rules | `skills/agent-contract/SKILL.md`, the `check:` lines of rules 2, 3, 4, 5, 7, 12, 13, 14, 15, 17, 18, 19 and 20 | The lines name the readers in *Each pin, decided* |
| The docstring paragraph that argues for one pin per section, and the comments above `PINS` | `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `:9-14` and `:34-54` | Rewritten to say what the module reads after the change |
| "which `test_the_agent_contract_holds_the_universal_rules.py` pins from the other side" | `tests/text/test_the_handoff_before_round_one.py`, `:106-108` | Rewritten. Of the three contract rules that table names (1, 6 and 12), only rule 1's command forms stay pinned in that module |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
