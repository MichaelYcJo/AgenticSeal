# Closing memo: 1794289597-pr-md-copies-the-changelog-below-the-fold

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the format check at this branch's HEAD | the orchestrator, through the broad gate |
| the five sealer eval cases under `evals/behaviour/sealer/` run by an agent against the new body layout, whose `seal pr-body --check` refuses the new layout where the sandbox resolves `seal` to an installed 0.37.1 plugin (`frame/design.md` G11) | the repository owner, at the next run of the behaviour evals |

## Not done

A `details` tag on a line of the changelog fragment is still refused with the sentence "a `details` tag GitHub would read as a second fold or as the end of the copy's one `<details>`". A `</details>` on such a line now stands above the fold, where no fold is open for it to end, so the second half of that sentence does not fit it. The refusal itself stands, because a `<details>` there would still open a fold over the rest of the body. `frame/design.md` *User scenarios & acceptance* S3 keeps the existing refusal cases "with no change to what they assert", and one of them pins this sentence. So the wording was left as it is.
