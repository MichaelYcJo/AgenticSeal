# Closing memo: 1794289597-pr-md-copies-the-changelog-below-the-fold

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the format check at this branch's HEAD | the orchestrator, through the broad gate |
| the five sealer eval cases under `evals/behaviour/sealer/` run by an agent against the new body layout, whose `seal pr-body --check` refuses the new layout where the sandbox resolves `seal` to an installed 0.37.1 plugin (`frame/design.md` G11) | the repository owner, at the next run of the behaviour evals |

## Not done

A `details` tag on a line of the changelog fragment is still refused with the sentence "a `details` tag GitHub would read as a second fold or as the end of the copy's one `<details>`". A `</details>` on such a line now stands above the fold, where no fold is open for it to end, so the second half of that sentence does not fit it. The refusal itself stands, because a `<details>` there would still open a fold over the rest of the body. `frame/design.md` *User scenarios & acceptance* S3 keeps the existing refusal cases "with no change to what they assert", and one of them pins this sentence. So the wording was left as it is.

`skills/code-review/orchestration.md`'s paragraph opening **Where a fix pass or a fold changes a sentence that `pr.md` quotes or `pr.<lang>.md` renders** does not ask the orchestrator for a new rendering where a fix pass or a fold adds a list item to `changelog.md`, because such a change rewrites no sentence `pr.<lang>.md` renders. The proofer names the missing rendering as a finding located in `pr.<lang>.md` (`agents/proofer.md`, **Every round reads the work item's records that state the present, whole, against its target**), and the orchestrator repairs it as the same paragraph states. Covering the case in the paragraph would build beyond `frame/design.md` *Scope* item 5, which words that sentence, so phase 2 left it for the orchestrator to weigh.
