"""`hooks/hooksession.py`: which process is the session's `claude`.

The lease writer and the worktree guard's count both ask this module which
pid is the session's. The cases come from `tests/test_lease_liveness.py` by
way of `tests/test_session_lease.py` (#942's phase 6).
"""

import os
import sys

import pytest
from conftest import census_case, stub_process_tree

TARGET = "hooks/hooksession.py"

# The cases import the module by name, as the hooks that use it do.
sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks")
)


class Test_claude_pid:
    def test_accepts_the_claude_ancestor_past_the_shell(self, monkeypatch):
        """The immediate parent is the shell that spawned the hook — measured here,
        /bin/zsh, with claude two levels up. Recording getppid() would name a
        process that dies constantly, and every dead shell would retire a live
        session's lease. The lease writer's own walk (`owner_pid`) left with #868;
        it asks `hooks/hooksession.py#claude_pid`."""
        import hooksession

        stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "claude")})
        assert hooksession.claude_pid() == 50

    @pytest.mark.parametrize("value", ["", "x", "0", "1", "-5"])
    def test_refuses_an_exported_pid_that_names_no_process_and_walks(
        self, monkeypatch, value
    ):
        """S5 of work item 1791384157, the other side: a value that is not a pid
        above 1 is not read, and the walk answers as it did."""
        import hooksession

        stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "claude")})
        assert hooksession.claude_pid({"CLAUDE_PID": value}) == 50, value

    def test_refuses_a_tree_with_no_claude_ancestor(self, monkeypatch):
        """An extension host is not named `claude`. No pid is recorded, so the
        guard reads the lease as unattributable rather than as an exited session."""
        import hooksession

        stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "code")})
        assert hooksession.claude_pid() is None


class Test_claude_ancestor:
    def test_accepts_the_nearest_ancestor_named_claude(self, monkeypatch):
        import hooksession

        stub_process_tree(
            monkeypatch,
            100,
            {100: (60, "/bin/zsh"), 60: (50, "claude"), 50: (1, "claude")},
        )
        assert hooksession.claude_ancestor() == 60

    def test_refuses_pid_1_even_where_it_is_named_claude(self, monkeypatch):
        """Pid 1 is never a session's own process, the floor `claude_pid`
        keeps for `CLAUDE_PID` too: a lease naming pid 1 would read as live
        for as long as the machine, or a container whose first process it is,
        stays up (#1017, round 3's h3)."""
        import hooksession

        stub_process_tree(monkeypatch, 100, {100: (1, "/bin/zsh"), 1: (0, "claude")})
        assert hooksession.claude_ancestor() is None


test_census = census_case(TARGET)
