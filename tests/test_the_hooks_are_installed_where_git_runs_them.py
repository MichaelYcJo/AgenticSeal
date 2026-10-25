"""The installer put the git hooks where git ran them (#692), until #1027.

This file holds no case. `hooks/hook-install.py`, the stubs it wrote and the
git hooks they ran are gone: nothing of this plugin is installed into git.
What a session does instead, at its start, is take out the stubs an earlier
release wrote, and its cases are `tests/test_stub_remove.py`.
`docs/the-commit-gate-inside-git.md` names this file on a `check:` line until
the settle that applies work item 1792935671 removes that document, so the
file stays with no case until then.
"""
