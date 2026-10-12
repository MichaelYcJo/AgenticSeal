# 1791382684-every-reader-and-record-is-inventoried — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 9c228af5 |
| Ran by | smith on opus, as the run-level `handoff.md` §*Starting on a new machine* item 4 names the spawn |

## What this phase was asked

The records say what the tree now has: the ledger fragment
`seal/ledger/1791382684-every-reader-and-record-is-inventoried.md` removed,
the changelog's `### Changed` entry removed, `overview.md`'s two `Not
verified` rows closed with ✅ and its divergence and `Not done` sections
rewritten, `survivors.md` re-derived, `phases/phase-4.md` and this record
written; then `origin/release/v0.21.0` merged in (at 34fc36e9), a merge and
never a rebase, and whatever the merge drifts read again.

## What this phase found

**The merge drifted nothing.** `origin/release/v0.21.0` at 34fc36e9 brought
#894's work (#897), and the merge, c778429d, met no conflict:
`tests/undeclared_readers.txt` equalled the base's after phase 4, as
`plan.md` §*Seams* said it would. `bin/evidence-check .` after it: exit 0,
8,415 ok, 0 drifted, so no `Re-read ·` row is owed and none was written. The
branch's `.py` files and census now equal the release branch's
(`git diff --quiet origin/release/v0.21.0 HEAD -- '*.py'
tests/undeclared_readers.txt`, exit 0), and `hooks/worktree-guard.py` is the
release branch's at every byte.

**`survivors.md` re-derived to nothing, so it is gone.** `survivor-check
--range origin/release/v0.21.0...HEAD` at the merge read 0 sentences removed
and named no place. The plan keeps what the check still names, which is no
row, and the check refuses an exemption file with no row: run with the
re-derived file holding only its header, it exited 2 ("An exemption file
with nothing in it silences nothing"). So the file is removed, and the
check runs without `--exempt` for this item, exit 0. `overview.md` records
the divergence from the plan's verification cell.

**What the records now claim.** No ledger fragment of this item is under
`seal/ledger/`, and with none the records arm reads none of this item's
records; the ten inventory markers stay as `spec.md` §*What the reframe
removes* says. `changelog.md` holds `### Added` alone. `overview.md`'s
`Not verified` has one open row, the sealer's.
