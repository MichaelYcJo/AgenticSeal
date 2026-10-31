# Closing memo: 1793419351-project-rules-live-in-the-repository

## Not verified

| Item | Who must answer |
|---|---|
| The broad suite, the repository-wide lint and `seal gate` at the branch's HEAD | the orchestrator, by `seal gate --base release/v0.26.0 --record seal/threads/1793419351-project-rules-live-in-the-repository` |
| The wording of `skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson is written* against issue #1200's *Done when*, which no case pins | the proofer at review |
| Contract rule 12's rewritten body and the rewritten paragraph of `skills/verify/orchestration.md` *The broad gate*, which no case pins | the proofer at review |
| That `gh pr edit` still stops on the Projects (classic) error; the sentence states it as history from the orchestrator's accounts of 0.4.0 and 0.8.0, and a probe would write to a pull request | the proofer at review |
| That `gh pr checks <N> --watch` run at once after a push waits for workflows that have not yet reported a check | the orchestrator, at the pull request's first push |

## Not done

A pin on the new section's bold sentence was not added. The plan's *Verified by* cell names none, the section's row in `skills/implement/acts.md` states that nothing reads it, and the module that holds such pins, `tests/text/test_the_rules_have_one_owner.py`, is edited by #1167 in parallel.
