# <work-item-id> — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | <the commit audited, `<sha> against <base>`> |
| Broad gate | <`sealed`, or `not sealed — <the failing check, as the gate printed it>`> |

## Claims re-run

<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->

| Claim | Source | Command | Result |
|---|---|---|---|
| <what was claimed> | <`path:line` of the claim> | <the command re-run> | <holds · does not hold — what came back> |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| <the spec · the build · the last round · the changelog · the pull request body> | <what it says the work is> | <the parties and facts it agrees with> | <none, or what contradicts it> |

<!-- One line: `sound`, `not sound — <the claim, its party, its coordinate>`
or `undecidable — <the question, for the owner>`. An owner's answer is a line
under it, `Answered <date> by <who>: <answer>`, which the next run keeps. -->

Verdict: <sound · not sound — <what> · undecidable — <question>>
