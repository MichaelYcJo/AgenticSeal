# Closing memo: 1795132764-a-pr-body-can-pass-githubs-length-limit

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the work item's HEAD | answered: the work item's broad run, `trail/gate.md` at `26ec989b4` against `c63d0b070`, on which `guarantee.md` sealed |
| closed The unit GitHub counts a pull request body's 65,536 characters in. The build counts UTF-16 code units, which fit under a code-point count as well; a count in UTF-8 bytes would refuse, at `gh pr create`, a body this build writes where its text is mostly outside ASCII (`frame/questions.md` Q1) | a measurement no record asks for: it would have decided whether `pr_body.py#LIMIT` counts the unit GitHub counts; no body on record was refused at `gh pr create`; no issue, failed run or other work item's rule rests on it |

## Not done

nothing
