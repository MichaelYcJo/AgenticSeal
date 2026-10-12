# 1791384157-the-hooks-read-the-session-waiver-and-creation-one-way — phase 12

| Field | Value |
|---|---|
| Phase | 12 |
| Commit | 8e231b70 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

S29, the records against what phase 11 left in the tree:

- In the unreleased fragment, retire or rewrite ledger rows S11, S11a–S11e,
  S12, S13, S13a, S15b, S17–S22, S24, S24a and S20a against S25–S28.
  Re-hash S14 and S15, add rows for S25–S28, and write `Re-read ·` rows for
  every released row phase 11's edits drift.
- In `overview.md`, add the divergence rows for phase 11. Its Not done names
  #856 closed as a limit and the brace handed to #886. Its Not verified table
  stays as before.
- In `questions.md`, P1 reads withdrawn, P2 and P3 stand, and W5 is
  answered.
- Close 11 and 12 in `plan.md`'s Status column, and re-read `survivors.md`
  for the places the removal leaves.

## What this phase found

**The fragment.**

- Retired: S11, S11a–S11e, S12, S13, S15b, S17–S22, S20a, S24 and S24a.
  Each described the removed reader.
- Rewritten:
  - S13a. The guard half now asserts the four forms are listed.
  - S14. Its claim said a brace segment is unrecognised before
    `_rebase_names_a_branch` is asked, which stopped being true. It now
    names the limit, as the docstring does.
- Added: S25–S28.
- Re-dated: the 42 rows whose hash moved. Each was read first. The merge
  moved only `OUT_OF_CLASS` and the commit-gate policy's section, and phase
  11 moved the guard's units and §A. No claim outside the brace rows
  depended on what left.
- One new `Re-read ·` row reads `seal/releases/0.17.0.md` G1.

**`--reverify --into` also wrote other work items' fragments.** It re-dated
rows in 1791384154, 1791384156, 1791384158 and 1791384160. This file's
writes do not reach those fragments, so all four were restored from `HEAD`
before the commit.

**Records naming a removed unit carry the marker.** `bin/evidence-check
--strict` refused 82 names on 77 lines, in `spec.md`, `overview.md`, phases
3, 7, 9 and 11, and the round 1–5 records. Each line now carries `NAME NOT
IN TREE` beside the name, the remedy the check names, as phase 9 did for
the first reframe.

**`survivors.md`.** The branch's range reports the same eleven places, all
excused. The four rows rounds 4 and 5 added for their own fix ranges
excused places about the reader, so they left with it.

**What each check said, executed at `8e231b70`:**

- the eight guard modules: 437 passed, exit 0.
- `bin/survivor-check --range origin/release/v0.21.0...HEAD --exempt
  …/survivors.md`: exit 0, eleven excused.
- `bin/correction-check --range 5623d728..HEAD`: exit 0, one merge
  examined.
- `bin/evidence-check . --strict`: exit 2, on 24 drifted rows and nothing
  else, 0 refused.
  - Every one of the 24 is a row the release branch at `ad447367` already
    reports. Run in a scratch clone there, it gives 33.
  - This branch's citing rows read nine of that branch's ten
    `OUT_OF_CLASS` drifts.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| ledger rows S11, S11a–S11e, S12, S13, S15b, S17–S22, S20a, S24 and S24a from the unreleased fragment | rows S25–S28, which state what the tree has since phase 11 |
| four `survivors.md` rows for rounds 4 and 5's fix ranges | nowhere: the branch's range reports none of their places |
