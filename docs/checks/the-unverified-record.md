# The unverified record

What `skills/verify/scripts/unverified_check.py` reads, for a person who
changes it.

**A pull request that declares nothing owes the unverified check
nothing.** Handed a `seal/` root's own `threads` path, `seal unverified`
exits 0 and names the state in two more cases beside the settled root:
where no `seal/` directory is in the tree, and where `threads/` holds
work items none of which carries a `gaps.md`. There is no row to read.
Every other path holding no `gaps.md` is still exit 2, which keeps a
misspelt path from passing in silence.
check: nothing-declared-nothing-owed
