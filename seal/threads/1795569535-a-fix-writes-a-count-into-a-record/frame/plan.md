# Implementation Plan: 1795569535-a-fix-writes-a-count-into-a-record (#1613)

## Technical context

The tree as read at `b03b0e290`.

`skills/agent-contract/SKILL.md:193` to `:200` is rule 19, two sentences on what a change does to the text it amends, citing `skills/core/SKILL.md` *The rule a mechanism is kept against* and rule 12. `tests/text/test_the_agent_contract_holds_the_universal_rules.py` reads the contract's headings by `HEADING` (`^## (\d+) (.+)$`) and pins no sentence of rule 19, so a reworded heading that keeps its number stays green there. `skills/implement/fix-pass.md:28` to `:41` is the paste-ready section; `skills/implement/fold-and-reframe.md:22` to `:24` holds the fold's rewrite sentence; `skills/implement/orchestration.md:31` to `:33` is step 1's sentence on contract rule 21; `skills/code-review/orchestration.md:179` to `:181` holds the clause Scope item 5 replaces; `agents/framer.md:224` to `:234` is the paragraph Scope item 6 removes. `tests/text/test_the_rules_have_one_owner.py` defines `FIX_PASS_PROCEDURE`, `FOLD`, `ORCH_IMPL` and `ORCH` already, and no constant for the contract. `test_the_framer_folds_a_decision_it_is_sent` and `test_a_decision_after_the_frame_is_folded_into_it` pin `contract rule 12` in the fold and the order; Scope items 3 and 4 add a citation beside it and remove none.

The failure scenario of the chosen approach, six months on: a party reads R5's line between a universal that states a rule and one that states the tree the wrong way. A proofer raises a finding on a rule sentence such as "every agent preloads the contract", or a crafter writes "the files" where it could have named them, and a reader loses the members the count stood for. R3 asks for the members or a citation, and the proofer's reading of each finding against R5 is where the line is held; no script reads it, so a drift shows only in the round records the settle reads.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Extend rule 19, which states what a change does to the text it amends | The heading grows, and a reader who cites rule 19 for its first half now cites a longer rule | chosen. The new clauses are the other half of rule 19's own fact (`frame/design.md` G2), so one rule holds both, and no number is spent |
| A new contract rule 22 with its own heading | The forward half of the fact, what a change writes, stands apart from rule 19's backward half, what stood on the old fact, and a later rewording of one leaves the other | rejected |
| Put the clauses in rule 12, which the fix and fold procedures cite (`frame/design.md` G4) | Rule 12 is about the instances one defect's cause produces, read by the party that fixes a finding. A fold or an orchestrator's `pr.md` edit fixes no finding, so the clauses would read as the fixing party's alone | rejected |
| Keep `agents/framer.md`'s paragraph and add a copy of it to the crafter's fix pass and to the orchestrator's order | Three statements of one rule, as #161's count rule reached eight carriers and rounds 7, 8 and 9 corrected them a few at a time (`tests/text/test_the_rules_have_one_owner.py`'s docstring). The premise that would keep the framer's paragraph, a framer-only part of it, was checked: its only framer-only words are the names of the frame files, which R6's reach covers | rejected; the paragraph goes (`frame/design.md` `## Removes`) |
| Scope the rule to records, as the issue's wording does | 29 of the issue's 72 fix-made defects were in code (the issue body), and a docstring that says "the three callers" goes false at the next fix as a record does. `skills/core/SKILL.md`'s one-source rule already governs every fact (`frame/design.md` G1, G11) | rejected; R6 reaches every text a change writes |
| A script that refuses `every`, `only`, `none` or a number word in a record | A rule sentence holds "every" correctly, and a reading guessed from words is the one `skills/core/SKILL.md` *The rule a mechanism is kept against* says is reported and never used to block | rejected |
| Rely on the preload alone, with no citation at the steps | The contract arrives once at startup, and a party writing a fold or a fix reads the procedure of that step. A citation there costs a clause, and the `RULES` row holds it | rejected; Scope items 2 to 5 cite rule 19 |
| Cite rule 19 in `skills/code-review/SKILL.md`'s paste-ready paragraph too | The proofer preloads the contract, and the fix pass's reading (Scope item 2) is where a snippet becomes a change. #1612 and #1615 both change `skills/code-review/SKILL.md` | rejected |
| Write the policy's account into `docs/running/the-agent-set.md` in this pull request | The subject is the code (`frame/design.md` G12), and the settle writes the policy root from `## Rule changes` | rejected; the account is the `add` of `## Rule changes` |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 8 | `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_every_agent_reads_the_contract.py`; the new `RULES` row seen red once per carrier with that carrier's citation removed; `git grep -n -F 'A count of a list is stated once' -- agents skills docs templates` and `git grep -n -F 'no sentence counts the examples' -- agents skills docs templates` each print nothing (at `b03b0e290` each prints the one line `frame/design.md` G8 and G9 name, which Scope items 6 and 5 take out) | |

## Overlap with the release

Each row reads the other item's issue body (`gh issue view <N> --json body`), since no branch of the clone names #1612, #1614 or #1615 (`git branch -a`, executed at `b03b0e290`) and none has a frame. Where a row names a section the other item will change, that is the issue's proposal read against the tree, not a frame's statement.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1612 | `skills/implement/fix-pass.md`: this item edits *A paste-ready fix is read before it is applied*, and #1612's close that reruns the listing command lands in the close blocks. Contract rule 19's sentence on finding what stood on the old fact is the rule #1612's listing command applies, so #1612 reads the rule this item extends | #1613 | This item carries the version move and is the smaller diff. #1612's command that lists every place stating a fact is R3's "the command that lists them", so #1612 builds on the extended rule inside its own rounds |
| #1614 | `skills/implement/fold-and-reframe.md`, the fold's rewrite sentence, and `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, whose fold paragraphs #1614 rewrites below the step 1 this item edits | #1613 | This item adds a citation to each file and moves no rule, so #1614's rewrite of the fold order meets one clause and keeps it |
| #1615 | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, where this item rewrites a clause and #1615 changes who reads a records-only fix. #1615's record axes in `skills/code-review/SKILL.md` read the record defects R1 defines | #1613 | An axis for a record against a fact can cite rule 19 once it stands, and #1615 is a `feat:` whose rounds come after the move |

## Operational impact

The version moves from 0.38.8 to 0.39.0, a minor version, because #1614 and #1615 are `feat:` and the release's check refuses a `feat:` in a patch (the orchestrator's decision in the spawn prompt). Phase 1's commit that adds `changelog.md` writes `"version": "0.39.0"` into `.claude-plugin/plugin.json`, the one place outside the records that states the version (`frame/design.md` G16), and the fragment says the version moves to 0.39.0. No migration, environment variable or dependency. A user's agents receive the rule at their next spawn after the update, through the contract they preload.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
