# The unverified record

What `skills/verify/scripts/unverified_check.py` reads, for a person who
changes it.

## The unverified record, and the baseline it is read against

**A baseline reference is resolved once, to a merge base, and every arm reads
that commit.** A branch name is not a commit: it moves while the pull request
is open, so two arms reading it a second apart can compare against two
different trees. The report names the revision it actually compared against,
and a reference sharing no history with the head is exit 2 — a comparison
against nothing is not a comparison.
check: one-merge-base

**A pull request that declares nothing owes the unverified check nothing.**
Handed a `seal/` root's own `threads` path, `seal unverified` exits 0 and
names the state in two more cases beside the settled root: where no `seal/`
directory is in the tree, and where `threads/` holds work items none of which
carries a `gaps.md`. There is no row to read, and none could have left.
Where the root is not in the tree it compares nothing against the base
either, so the pull request that moves a root to local mode is not read as
deleting its records. Every other path holding no `gaps.md` is still
exit 2, which keeps a misspelt path from passing in silence.
check: nothing-declared-nothing-owed
