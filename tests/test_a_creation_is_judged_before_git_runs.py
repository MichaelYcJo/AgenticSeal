"""A worktree creation is judged before git runs (#692).

Every case of this file moved to the creation flow,
`tests/e2e/creation/test_creation_flow.py` (#942's phase 6). The file holds
no case. It stays because `docs/worktree-guard-spec.md` *Decided before git
runs* names it on two `check:` lines, which #942's `## Rule changes` items
move to the flow when the work item is settled after the release.
"""
