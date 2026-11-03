# Closing memo: 1793678623-each-rule-rides-with-the-agent-that-uses-it

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1 changed text every agent receives: the contract's preamble now lists retired numbers, and rules 8 and 20 left as sections. No behaviour eval was run, since `evals/README.md` *The behaviour suite* makes no later edit owe a run. Whether an agent that adds a rule takes the number after the highest one used, and whether a session reading an old record's rule 8 or rule 20 finds it named as retired, is read, not measured. No agent of this run receives the new preamble, since agents read the installed 0.30.0 | the proofer at review; the live reading is `frame/questions.md` Q1's |
| The numbering case cannot see the highest number used leave the list or the file, since nothing else in the contract says it was used (`trail/phases/phase-1.md`, the `seal mutate` run on the list). A diff that drops 20 from the list, or retires the highest rule without listing it, passes the case | the proofer at review, on each diff of the contract's preamble |

## Not done

Phase 1 did not build a guard for the highest number used. Such a guard
would read the contract at the last release tag, and require every number
used there to stay a heading or a listed number. It would read git history
beside the tree, and `frame/design.md` *Removes* says this work adds no
mechanism. `skills/core/SKILL.md` *The rule a mechanism is kept against*
keeps a check to what it reads exactly, and nothing beside the tree to stay
in step with it. The limit is stated in the docstring of
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` instead.
