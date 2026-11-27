# The unverified record

What `skills/verify/scripts/unverified_check.py` reads, for a person who
changes it.

**Handed a `seal/` root's own `threads` path that holds no work item,
`iadd unverified` exits 0 and names the settled root.** That is the state
a complete settle ends in, an empty directory on disk or none in a fresh
checkout, and a session runs the command after the settle. Every other
path holding no `gaps.md` is exit 2, a tree with no `seal/` root and work
items none of which carries a `gaps.md` among them, which keeps a
misspelt path from passing in silence. No workflow runs the command.
check: tests/skills/test_unverified_check.py
