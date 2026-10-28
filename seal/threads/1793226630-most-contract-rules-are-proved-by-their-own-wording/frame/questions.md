# Questions for the planner: 1793226630-most-contract-rules-are-proved-by-their-own-wording

## Judgments the ticket left open that the tree answered

Listed so nobody reopens them. Each one's grounds are in `frame/design.md` or
in `frame/plan.md`'s Alternatives table.

1. **The whole contract module is in scope, not only `PINS`.** The issue's
   *What changes* says "each phrase pin on a rule sentence" and that the
   work "starts with the contract module". Seven other cases of that module
   assert phrases of the contract's prose (`frame/design.md` *The module's
   other phrase cases*), and contract rule 12 asks for the class, not the
   coordinate. The issue's first *Done when* names `PINS`, and this work
   meets it as part of the whole.
2. **A command spelling an agent copies into a shell is a fact a reader
   needs fixed.** The issue lists "a citation's spelling, a heading a reader
   resolves, a word a checker matches" as examples of such a fact. In each
   example a reader depends on exact characters. The shell is that kind of
   reader for rule 1's two command forms and for rule 11's
   `git rev-parse` spelling, so those stay (`frame/plan.md` row D). A
   rewording around them stays green, so they carry none of the cost the
   issue names.
3. **The phrase pins on contract sentences in other modules are counted,
   not decided.** The issue's *What changes* starts with the contract
   module and has the other `tests/text` modules counted.
   `frame/design.md` *Scope*, Out, names the three under `tests/behaviour`
   too, so the next work item finds them. This work files no follow-up
   issue. The count posted on #1111 is what the owner decides the next step
   from.
4. **Where no case reads a rule, its reader is named in words.** Rules 12,
   13, 14, 18, 19 and 20 read `check: none reader: the proofer at
   review`, the tree's usual spelling. Rules 4 and 15 read `check: none
   reader: the sealer at each guarantee`. Rules 3 and 17 read `check: none
   reader: the orchestrator at each hand-back`: rule 3's declined
   instruction and rule 17's leftover are written in the hand-back, and no
   diff shows either.
5. **An eval case is named only where its grader reads the rule's
   behaviour.** Rule 2 names `rule-sealer-no-gate`, rule 5 names
   `rule-sealer-false-red` and `rule-sealer-untrue-body`, and rule 7 names
   the four crafter cases
   (`frame/design.md` *Why each eval case is the reader it is*). R40's
   let-through in the crafter grader stays #1038's.
6. **The count is posted by the orchestrator.** Contract rule 6 withholds
   posting from every agent. The crafter writes the table into
   `trail/phases/phase-2.md`, and the orchestrator posts it on #1111 before
   the pull request opens.
7. **`CLAUDE.md` does not change.** *The rule a mechanism is kept against*
   already holds both halves the issue quotes. A new sentence about phrase
   pins would state the same rule twice.
8. **No file on #1117's list is needed.** This work edits
   `tests/text/test_the_agent_contract_holds_the_universal_rules.py`,
   `skills/agent-contract/SKILL.md`,
   `tests/text/test_the_handoff_before_round_one.py` and this work item's
   records. `docs/the-broad-gate.md` changes only through `## Rule changes`,
   at the settle. #1117's branch holds only its `routing.md` at this
   framing (executed `git diff --stat`). Its file list is the spawn
   prompt's (unverified; the orchestrator answers it).
9. **The module keeps its file name.** `frame/plan.md` row B.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Contract rule 15 says a new case is shown failing "against the old code, or with the sentence it pins deleted". The second way presumes a case that pins a sentence, which is the kind this work removes from the contract module. `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* asks every rule a work states to end with a `check:` line naming a case, and that is how a prose rule came to get a phrase pin. Should either sentence change in this work? The tree cannot answer, because both are rules every agent reads, and the issue does not ask for them | a person | (a) Leave both. The second way of rule 15 still serves the two facts this work keeps, and implement's *A rule no case can hold says `check: none reader:`* already allows a rule with no case. (b) Narrow rule 15's second way to "with the fact it pins deleted", and add to implement's step 2 that a case on a prose rule pins only a fact. That changes text every agent reads, so it adds a phase and a pass of review | (a): both sentences stay as they are | open |
| Q2 | Some literals in the count sit on the line between a rule sentence and a word a checker reads, such as a bold lead sentence that another module finds a paragraph by (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:849` finds the crafter's paragraph by its lead). Which side does such a literal fall on? | the work | (a) Count it as a phrase pin. (b) Count it as a fact, because a reader resolves it. (c) Count it in a column of its own | (c): phase 2's record lists each such literal by its line, in a column beside the module's number, and the number leaves it out | open |
