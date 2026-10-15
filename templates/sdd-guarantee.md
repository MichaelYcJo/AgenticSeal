# <work-item-id> — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md — the sealer's
verdict on the work before it, independent of the smith and the warden. The
sealer writes this file and nothing else; the orchestrator commits it beside
`broad-gate.md`. Its reference is the issue body and the tree, never an
agent's word. `docs/the-review-record.md` §*The guarantee* states the rules;
`chain_check.py` reads `Target SHA` and the `Verdict:` line at the pull
request, and a ready pull request passes only on `sound` at HEAD. -->

| Field | Value |
|---|---|
| Target SHA | <the commit audited, `<sha> against <base>`> |
| Broad gate | <`sealed`, or `not sealed — <the failing check, as the gate printed it>`> |

## Claims re-run

<!-- A sample of the smith's `executed` and `seen red` claims, chosen where
the evidence is thinnest or the outcome rests on it, each re-run; every
`fixed <commit>` verdict, its commit on the branch and touching its
`Location`; every removal `spec.md` or the changelog names, absent from the
tree. -->

| Claim | Source | Command | Result |
|---|---|---|---|
| <what was claimed> | <`path:line` of the claim> | <the command re-run> | <holds · does not hold — what came back> |

## The parties

<!-- The framer's spec, the smith's diff and phase records, the warden's last
record, the changelog fragment and the pull request body, each against the
issue and the tree. -->

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| <the spec · the build · the last round · the changelog · the pull request body> | <what it says the work is> | <the parties and facts it agrees with> | <none, or what contradicts it> |

<!-- One line. `sound` · `not sound — <the claim, its party and coordinate>` ·
`undecidable — <the question, for the owner>`. The owner's answer goes on a
line under it, `Answered <date> by <who>: <answer>`, and the sealer runs again
at the new HEAD, keeping that line. -->

Verdict: <sound · not sound — <what> · undecidable — <question>>
