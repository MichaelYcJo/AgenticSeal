# Closing memo: 1793419350-a-prefix-states-what-a-change-is

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at this branch's head after `release/v0.26.0` is merged in: the full suite, the repository-wide lint and format | the orchestrator, by `seal gate` |
| S8 and S9: that the rewritten table gives #1167 and #1198 `feat:`, each for the part `frame/design.md` *The first cases* names, and gives a change to what a check refuses `feat:`, `fix:` or `refactor:` and never `chore:` | the proofer, reading the table at review |
| That `skills/core/SKILL.md` *The rule a mechanism is kept against*, which the release check's comment on `FEAT` cites, says a script keeps no list of spellings: on this branch's base it does not, and #1167's phase 1 writes it | the orchestrator, at the merge of `release/v0.26.0` into this branch |
| The renamed step and its `::error::` line on a real release pull request into `main` | the orchestrator, at the release pull request |
| S10: that each case in `frame/design.md` *The cases the rule was run against* gives the prefix that table names under the rewritten `skills/commit-pr-convention/SKILL.md` *Commit messages*. No case in the suite reads the table's rule, and the crafter's own run of the twelve cases is a reading | the proofer, reading the rewritten section at review |

## Not done

The comment block above the step in `.github/workflows/hygiene.yml` explains the milestone question alone and was left as it stands. The step's name now states the second question, and the script's module docstring holds its reasoning, so a sentence there would restate the docstring.

Phase 2 left two sentences of `skills/commit-pr-convention/SKILL.md` outside *Commit messages* as they stand: *First, check the title against the history* and *Before the pull request opens* item 2 each say the prefix is the one "the table in *Commit messages* gives the change". The table's order is now the precedence that gives the change its prefix, so the sentence still reads true, and `frame/plan.md`'s phase 2 row names no paragraph outside *Commit messages*.
