# Closing memo: 1795132764-a-pr-body-can-pass-githubs-length-limit

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the work item's HEAD | the orchestrator, once the review rounds settle |
| The unit GitHub counts a pull request body's 65,536 characters in. The build counts UTF-16 code units, which fit under a code-point count as well; a count in UTF-8 bytes would refuse a body this build writes, at `gh pr create` (`frame/questions.md` Q1) | a measurement, by whoever may post to a scratch pull request, as Q1 states |

## Not done

The one-file form of the length refusal holds no case. It ends `so it is shortened` where the refusal names one file, which happens where `changelog.md` is absent and the first part alone passes the limit. The three-file form, `so one of them is shortened`, is pinned by `tests/skills/test_pr_body.py#Test_main.test_refuses_a_first_part_and_changelog_past_the_limit`. The two forms differ in one phrase chosen by the number of files, and a case for the other shape would add a fixture for one word.
