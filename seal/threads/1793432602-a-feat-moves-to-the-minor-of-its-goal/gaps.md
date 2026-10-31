# Closing memo: 1793432602-a-feat-moves-to-the-minor-of-its-goal

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate at this branch's head: the full suite, the repository-wide lint and format | the orchestrator, by `seal gate` |
| S8: that each hit of the S8 grep outside `seal/threads/` states the rule as `frame/design.md` does | the proofer, running the grep and reading each hit at review |
| S9: that neither #1199's fragment nor this work item's states that every `feat:` in a patch renames the milestones forward, and that the grouping rule is stated once among the fragments' entries | the proofer, reading both fragments at review |
| S10: that `seal settle` after 0.26.0's tag shows #1199's operation before this one in two sections and this one alone in the third | `chain-check` parses `## Rule changes` at the pull request; the settling session reads the order after the tag |
| The rewritten `::error::` line and minor line on a real release pull request into `main` | the orchestrator, at the release pull request |

## Not done

`judge_feat`'s own docstring was left as it stands. It says a `feat:` makes a minor and that a patch carrying one fails, and names no repair, so nothing in it stood on the push.
