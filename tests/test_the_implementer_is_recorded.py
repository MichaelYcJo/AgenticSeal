"""Who framed and who implemented is declared, marked when it happens, noticed.

The mark's cases moved to `tests/test_implementer_mark.py` and the notice's to
`tests/test_implementer_notice.py` (#942's phase 6). What stays is the case
that holds the rule's last clause: the commit gate's decision has to be
byte-identical with the `Implementation` row and without it, which is the
case that would catch this axis leaking into a decision it was never given.
It runs the commit gate's hook and nothing of the family, so it waits for the
commit gate's group.
"""

from conftest import bash, declare, opt_in, run_hook

# --- and it changes no decision ---------------------------------------------


def test_the_commit_gate_decides_identically_with_the_row_and_without(repo):
    """S11, the load-bearing half: notice, never denial. Byte-identical,
    because the reason text is what a session acts on."""
    opt_in(repo)
    declare(repo, implementation=None)
    without = run_hook("commit-review-gate.py", bash(repo))
    declare(repo, implementation="smith")
    with_row = run_hook("commit-review-gate.py", bash(repo, session="s2"))
    assert without == with_row == "", (without, with_row)
