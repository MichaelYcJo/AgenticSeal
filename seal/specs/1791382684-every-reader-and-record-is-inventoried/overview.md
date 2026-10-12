# 1791382684-every-reader-and-record-is-inventoried — overview

## Why this work exists

The inventory found that the readers which kept being reopened were the ones
guessing at text they did not control, and the item ships as that inventory:
its first frame's backfill of `Reads:` lines was built, read false three
rounds running, and withdrawn whole by the reframe (`spec.md` §*The
reframe*), so the tree's code is what 7608d82c holds.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| `inventory/` gained a marker on 10 lines | `spec.md` §*The inventory's fate*: "Nothing in the build moves or edits it." The ledger fragment phase 3 wrote made the item live, and `evidence-check`'s records arm then refused 14 names the inventory read at 5623d728 and siblings have since removed, exit 2 | each line ends `· NAME NOT IN TREE`, and the markers stay after the reframe | `spec.md` §*What the reframe removes*: "the ten `· NAME NOT IN TREE` markers phase 3 added (true of the tree, and read by nothing while the item has no ledger fragment)" |
| the build's own divergences | phases 1 to 3 met eight more — the pinned `hooks/cmdline_base.py`, the frame's 23 unparsed cells, the cells with no direction word, the two-class cells, the rider stamps, the prose of 57 units, the marker class, the backslash cells | withdrawn with the build in phase 4; none describes the tree any more | `phases/phase-1.md` to `phase-3.md` and `rounds/round-1.md` to `round-3.md` keep them as the history the reframe rests on |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, lint and typecheck over the build's tree | the sealer, after the review rounds settle |
| ✅ that each of the 189 `Reads:` lines says what its unit reads today: each is the inventory's reading of 2026-10-07 carried over for a unit whose hash has not moved since, and was not read against the code again | withdrawn: phase 4 (ef8fb33c) restored the 44 files, so no such line is in the tree; rounds 1 to 3 had read them and found 71 false |
| ✅ phase 4, `hooks/worktree-guard.py`'s units | gone with the reframe (`plan.md` §*Phases*): this branch changes the guard at no commit, and its units declare when next touched |

## Not done

The 189 units the build wrote a line on are back on the census, beside the
rest the inventory rowed, and each declares when next touched, by whoever reads its body then;
`spec.md` §*The direction word, settled* is the definition that hand applies.
The inventory's other columns (`Decides`, `Duplicates`, `Note`) stay where
they are, as the reading of 5623d728.

## Fed back into the spec

none
