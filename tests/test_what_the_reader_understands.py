"""The reader answered "nothing moved" for every construct it did not model.

Issue #72. `hooks/cmdline.py` walks a command's segments to say which
repository its `git commit` lands in, and its default for an unmodelled
construct was that the shell stayed where it was. That is a confident answer,
not an absent one, and it is wrong in both directions at once: a stop where
the session's own directory needs review, and a silence where that directory
carries a routing declaration and the commit lands somewhere else. The reader
now enumerates what it UNDERSTANDS and routes everything else to
`Unresolved`, which `docs/commit-review-gate-spec.md` treats as a stop.

The reader's cases are in `tests/test_cmdline.py`'s `Test_understood`,
`Test_walk_directories`, `Test_drop_comments` and `Test_drop_heredoc_bodies`,
and the guard's half, `test_the_guard_reads_the_same_answer`, is in
`tests/test_worktree_guard.py`'s `Test_walk_command` (#942's phase 6).
`docs/commit-review-gate-spec.md` names this file on a `check:` line until the
work item's rule change for it is settled, so the file stays with no case.
"""
