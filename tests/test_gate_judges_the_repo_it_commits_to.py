"""The commit gate judged the shell's cwd, not the repository being committed to.

`git -C <repo> commit` names its own repository. The gate resolved everything
from the payload's `cwd` and never read the command, so a commit landing in a
repository that never opted in was gated against whichever repository the shell
happened to be sitting in — and a session testing hooks, which builds a scratch
repository and drives it with `-C` from inside the repository under
development, answered a prompt on every command.

Reading `-C` opened a second hole (issue #56): the gate sees the command
before the shell expands it, so `git -C "$WT" commit` hands it the literal
characters `$WT`, and an unresolvable target now stops the commit instead.

The gate's own cases are in `tests/test_commit_review_gate.py`, and
`hooks/cmdline.py`'s walk, which directory each segment of a command runs in,
is in `tests/test_cmdline.py`'s `Test_walk_directories`,
`Test_split_segments_with_separators`, `Test_parse_git` and `Test_module`
(#942's phase 6). `docs/commit-review-gate-spec.md` names this file on a
`check:` line until the work item's rule change for it is settled, so the file
stays with no case.
"""
