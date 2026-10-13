# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

## Why this work exists

Four `Reads:` lines said `refused` where a line under `## Removes` that is
neither a row nor a `nothing` line was dropped unread; the refusal makes the
word true, and two sentences #834's round 6 found stale are corrected.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The released rows the warden's sentence drifts | `spec.md` §*Data & interfaces*: "Ledger anchors this work moves: #835's D1 row … one `Re-read ·` row in this item's fragment"; `plan.md` phase 1: "`bin/evidence-check .` names #835's D1 row … as the one DRIFTED anchor". At 3a66113f it names thirteen: D1 and twelve released rows anchored on `agents/warden.md#"## Role"` | the sentence stays in §*Role*, and phase 3 re-reads all thirteen | `spec.md` In 4 puts the sentence in §*Role*, and that section is one heading region (lines 84-397), so a sentence anywhere in it moves every row anchored on the heading. Moving it out of §*Role* would leave the frame's In 4 unbuilt |

## Not verified

none — filled at the last phase

## Not done

nothing

## Fed back into the spec

none
