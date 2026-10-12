# 1791382684-every-reader-and-record-is-inventoried — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | ef8fb33c |
| Ran by | smith on opus, as the run-level `handoff.md` §*Starting on a new machine* item 4 names the spawn |

## What this phase was asked

The reframe's withdrawal: the 44 `.py` files the build changed and
`tests/undeclared_readers.txt` restored from 7608d82c by `git checkout
7608d82c -- <paths>`, the paths from `git diff --name-only 7608d82c HEAD --
'*.py' tests/undeclared_readers.txt`, in one commit that touches nothing else,
with no docstring edited by hand and no script written.
`hooks/worktree-guard.py` is not touched.

## What this phase found

**The restore was exactly the plan's.** The path list held 45 paths, the 44
`.py` files and the census, and neither `hooks/worktree-guard.py` nor
`hooks/cmdline_base.py` was among them. One `git checkout 7608d82c --` over
those paths, one commit, 45 files.

**What it took back with the lines.** The three `# RIDER:` stamps phase 2
re-stamped (`hooks/optin.py#repo_root`,
`hooks/review-skill-gate.py#already_asked`,
`skills/code-review/scripts/round_record.py#units_named_earlier`) returned to
#835's dates and hashes with their files, and they reproduce: the rider check
read 20 ok, 0 drifted. Rounds 1 and 2's corrections went with the lines they
corrected, since they were edits to the same docstrings.

**Checks at the phase's close, executed.** `git diff --quiet 7608d82c HEAD --
'*.py' tests/undeclared_readers.txt` exit 0; the census 1,584 lines;
`bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py
tests/test_a_rider_reaches_its_file.py` 126 passed; `bin/evidence-check .`
exit 0, 8,397 ok, 0 drifted (the ledger fragment still stood; phase 5
removes it).
