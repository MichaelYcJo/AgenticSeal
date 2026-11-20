# Closing memo: 1795132764-a-pr-body-can-pass-githubs-length-limit

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the work item's HEAD | the orchestrator, once the review rounds settle |
| The unit GitHub counts a pull request body's 65,536 characters in. The build counts UTF-16 code units, which fit under a code-point count as well; a count in UTF-8 bytes would refuse, at `gh pr create`, a body this build writes where its text is mostly outside ASCII (`frame/questions.md` Q1) | a measurement, by whoever may post to a scratch pull request, as Q1 states |

## Not done

nothing
