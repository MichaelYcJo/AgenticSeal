# Closing memo: 1793678623-each-rule-rides-with-the-agent-that-uses-it

## Not verified

| Item | Who must answer |
|---|---|
| Phase 1 changed text every agent receives: the contract's preamble now lists retired numbers, and rules 8 and 20 left as sections. No behaviour eval was run, since `evals/README.md` *The behaviour suite* makes no later edit owe a run. Whether an agent that adds a rule takes the number after the highest one used, and whether a session reading an old record's rule 8 or rule 20 finds it named as retired, is read, not measured. No agent of this run receives the new preamble, since agents read the installed 0.30.0 | the proofer at review; the live reading is `frame/questions.md` Q1's |
| The numbering case cannot see the highest number used leave the list or the file, since nothing else in the contract says it was used (`trail/phases/phase-1.md`, the `seal mutate` run on the list). A diff that drops 20 from the list, or retires the highest rule without listing it, passes the case | the proofer at review, on each diff of the contract's preamble |
| The phase-boundary set is held by no case, in the contract before phase 2 or in the *Phase boundary* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* after it. Rule 2's `check:` targets, `tests/text/test_broad_gate_rule.py` and `evals/behaviour/sealer/rule-sealer-no-gate/`, never read that sentence (`trail/phases/phase-2.md`). A diff that drops a part of the set from the row passes the suite | the proofer at review |
| Phase 2 moved rule 16 into `skills/implement/SKILL.md` *2.* and the phase-boundary set into the verify row. Whether a crafter spawned under 0.30.1 commits in the `git -C` form and runs the set from the verify row is read, not measured, since agents of this run read the installed 0.30.0 | `frame/questions.md` Q1's measurement |
| Phase 3 left each agent to find the plugin's paths through contract rule 11 alone. The proofer and the sealer now get the parity record from `skills/legacy-parity/SKILL.md` *Recording the comparison* alone. The crafter and the framer now get the reference-root reading from `skills/implement/SKILL.md` *Document layout* alone. Whether agents spawned under 0.30.1 still resolve `skills/` paths at the plugin's root, still write the `original:` line, and still read a reference root, is read, not measured. No agent of this run receives the new text | `frame/questions.md` Q1's measurement; the proofer at review for the reading |
| No case reads the plugin-path sentence in contract rule 11. Before phase 3 none read it in the five definitions either. A diff that drops it passes the suite | the proofer at review |

## Not done

Phase 1 did not build a guard for the highest number used. Such a guard
would read the contract at the last release tag, and require every number
used there to stay a heading or a listed number. It would read git history
beside the tree, and `frame/design.md` *Removes* says this work adds no
mechanism. `skills/core/SKILL.md` *The rule a mechanism is kept against*
keeps a check to what it reads exactly, and nothing beside the tree to stay
in step with it. The limit is stated in the docstring of
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` instead.
