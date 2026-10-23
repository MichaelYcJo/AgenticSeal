"""`hooks/session-lease.py`: the lease a session leaves on every tool call.

The lease file is stamped on every tool call and read by the worktree guard
and the commit gate's lease route; it is never removed at session end, which
is why it records who owns it. The cases come from
`tests/test_lease_liveness.py`, `tests/test_chain_hooks.py` and
`tests/test_chain_hooks_hardening.py` (#942's phase 6). What a reader makes of
a lease is the worktree guard's, and stays with its cases.
"""

import json
import os
import socket
import subprocess
import sys
import time

import pytest
from conftest import (
    census_case,
    git,
    git_dir,
    lease_dir,
    load_hook_module,
    payload,
    run_hook,
)

TARGET = "hooks/session-lease.py"

HOOKS = os.path.join(os.path.dirname(__file__), "..", "hooks")

sl = load_hook_module("session-lease.py", "sl_owner")


def leases_of(repo):
    d = os.path.join(git_dir(repo), "specseal-leases")
    return sorted(os.listdir(d)) if os.path.isdir(d) else []


def run_lease_hook(repo, session):
    payload = {
        "tool_name": "Bash",
        "session_id": session,
        "tool_input": {"command": "ls"},
        "cwd": str(repo),
    }
    subprocess.run(
        [sys.executable, os.path.join(HOOKS, "session-lease.py")],
        input=json.dumps(payload),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )


def stub_process_tree(monkeypatch, start, tree):
    """`ps -o ppid=,comm= -p <pid>` against a fixture tree of {pid: (ppid, comm)}.

    Only `ps` is faked; everything else (git, notably) reaches the real
    subprocess, so main() can still resolve the repo.
    """
    import types

    real_run = sl.subprocess.run
    monkeypatch.setattr(sl.os, "getppid", lambda: start)

    def fake_run(cmd, **kwargs):
        if not (isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "ps"):
            return real_run(cmd, **kwargs)
        pid = int(cmd[-1])
        if pid not in tree:
            return types.SimpleNamespace(stdout="")
        ppid, comm = tree[pid]
        return types.SimpleNamespace(stdout=f"{ppid} {comm}\n")

    monkeypatch.setattr(sl.subprocess, "run", fake_run)


def run_main_in_process(repo, monkeypatch, session, filed=None):
    """main() with stdin stubbed, so the wiring — not just owner_pid() — is
    under test. A version that recorded getppid() passes every test that only
    calls owner_pid() directly. FILED is the lease's file name where it is not
    SESSION (`pid-<ppid>` for a payload with no session id). A SESSION of
    None leaves the `session_id` key out of the payload."""
    import io

    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": "ls"},
        "cwd": str(repo),
    }
    if session is not None:
        payload["session_id"] = session
    monkeypatch.setattr(sl.sys, "stdin", io.StringIO(json.dumps(payload)))
    sl.main()
    with open(os.path.join(lease_dir(repo), filed or session), encoding="utf-8") as f:
        return json.load(f)


class Test_main:
    # --- which repository a call leases --------------------------------------

    def test_accepts_a_bash_call_and_leases_its_cwds_repo(self, repo):
        run_hook("session-lease.py", payload("ls", repo, session="sess-a"))
        assert leases_of(repo) == ["sess-a"]

    @pytest.mark.parametrize(
        "tool, session",
        [("Write", "sess-b"), ("Edit", "sess-e")],
        ids=["write", "edit"],
    )
    def test_accepts_an_edit_and_leases_the_edited_files_repo_not_the_cwd(
        self, repo, tmp_path, tool, session
    ):
        p = {
            "tool_name": tool,
            "session_id": session,
            "tool_input": {"file_path": str(repo / "f.txt")},
            "cwd": str(tmp_path),
        }
        run_hook("session-lease.py", p)
        assert session in leases_of(repo)

    def test_accepts_a_bash_call_in_a_subdirectory_and_leases_the_repo_root(self, repo):
        (repo / "sub").mkdir()
        p = {
            "tool_name": "Bash",
            "session_id": "sess-sub",
            "tool_input": {"command": "ls"},
            "cwd": str(repo / "sub"),
        }
        run_hook("session-lease.py", p)
        assert "sess-sub" in leases_of(repo)

    def test_accepts_a_missing_session_id_and_files_the_lease_by_pid(self, repo):
        p = {"tool_name": "Bash", "tool_input": {"command": "ls"}, "cwd": str(repo)}
        run_hook("session-lease.py", p)
        assert any(name.startswith("pid-") for name in leases_of(repo))

    def test_accepts_a_new_lease_and_prunes_the_stale_ones(self, repo):
        import time

        run_hook("session-lease.py", payload("ls", repo, session="sess-old"))
        stale = os.path.join(git_dir(repo), "specseal-leases", "sess-old")
        os.utime(stale, (time.time() - 100000,) * 2)
        run_hook("session-lease.py", payload("ls", repo, session="sess-new"))
        assert leases_of(repo) == ["sess-new"]

    def test_refuses_a_call_outside_any_repo_silently(self, tmp_path):
        p = {
            "tool_name": "Bash",
            "session_id": "sess-c",
            "tool_input": {"command": "ls"},
            "cwd": str(tmp_path),
        }
        assert run_hook("session-lease.py", p).strip() == ""

    def test_refuses_to_lease_a_linked_worktrees_call_against_the_main_tree(
        self, repo, tmp_path
    ):
        wt = tmp_path / "wt"
        git(repo, "worktree", "add", "-q", str(wt), "feature/x")
        p = {
            "tool_name": "Bash",
            "session_id": "sess-wt",
            "tool_input": {"command": "ls"},
            "cwd": str(wt),
        }
        run_hook("session-lease.py", p)
        # the worktree session's lease lands in the worktree's own git-dir,
        # so it does NOT count against the main tree (already-isolated rule)
        assert "sess-wt" not in leases_of(repo)

    # --- what the lease records -----------------------------------------------

    def test_accepts_a_call_and_records_a_parseable_record(self, repo):
        """Through a real subprocess, so only what holds in every environment is
        asserted. Whether a pid lands depends on the ancestry the hook happens to
        have — present under a Claude Code session, absent on a CI runner, and both
        are correct. The pid logic is pinned by the stubbed-tree cases below, which
        do not depend on where the suite runs.

        The first version of this asserted a pid unconditionally. It passed locally
        for the wrong reason: pytest was launched from inside a session, so `claude`
        really was an ancestor. CI is what said so.
        """
        run_lease_hook(repo, "sess-x")
        with open(os.path.join(lease_dir(repo), "sess-x"), encoding="utf-8") as f:
            rec = json.load(f)
        assert rec["host"] == socket.gethostname()
        assert abs(rec["ts"] - time.time()) < 60
        if "pid" in rec:
            assert isinstance(rec["pid"], int) and rec["pid"] > 0

    def test_accepts_the_claude_ancestor_as_owner_not_the_shell(
        self, repo, monkeypatch
    ):
        stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "claude")})
        rec = run_main_in_process(repo, monkeypatch, "sess-owner")
        assert rec["pid"] == 50, "recorded the shell (getppid) instead of the session"

    @pytest.mark.rule("a-persons-own-commit")
    @pytest.mark.parametrize("comm", ["/x/bin/claude", "claude-host"])
    def test_accepts_the_process_the_hook_reads_back(self, repo, monkeypatch, comm):
        """S4 of work item 1791384157 (#868). The pid the lease writer records is
        the one the commit gate's lease route looks for (`claude_ancestor`), by
        one test of a process's name: its basename is `claude`. At `5623d728` the
        writer took any comm holding `claude`, so a `claude-host` ancestor was
        recorded, and no reader ever matched that lease. Red there on
        `claude-host`."""
        import hooksession

        stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, comm)})
        rec = run_main_in_process(repo, monkeypatch, "sess-one-test")
        assert rec.get("pid") == hooksession.claude_ancestor(), (comm, rec)
        assert hooksession.is_claude(comm) is (comm == "/x/bin/claude")

    @pytest.mark.rule("a-persons-own-commit")
    def test_accepts_the_pid_the_harness_exports(self, repo, monkeypatch):
        """S5 of work item 1791384157. Where the environment carries
        `CLAUDE_PID`, an observed value, the lease records it, even where the walk
        finds no process named `claude` (an extension host). Red at `5623d728`,
        where the lease recorded no pid."""
        monkeypatch.setenv("CLAUDE_PID", "4242")
        # The variable is read as this session's only beside this session's id
        # (round 1 of work item 1791384157, yellow 4).
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "sess-exported")
        stub_process_tree(monkeypatch, 100, {100: (1, "code")})
        rec = run_main_in_process(repo, monkeypatch, "sess-exported")
        assert rec["pid"] == 4242, rec

    def test_refuses_to_record_a_pid_when_the_owner_is_unknown(self, repo, monkeypatch):
        stub_process_tree(monkeypatch, 100, {100: (1, "code")})
        rec = run_main_in_process(repo, monkeypatch, "sess-ext")
        assert "pid" not in rec
        assert rec["host"] == socket.gethostname()

    @pytest.mark.parametrize("payload", [None, ""])
    @pytest.mark.parametrize("environment", [None, ""])
    def test_refuses_a_pid_beside_no_session_id_on_either_side(
        self, repo, monkeypatch, environment, payload
    ):
        """Round 2 of work item 1791384157, white 4, built as round 3's white 4
        asked: both absences, on both sides. `None` removes the environment
        variable and leaves the payload's `session_id` key out; `""` sets each
        empty. Where neither side names a session the two absences matched, and
        the lease `pid-<ppid>` recorded the inherited 4242. A missing id names no
        session, so the walk answers. `[None-None]` and `[-]` red with
        `hooks/session-lease.py` at `e0c5a191` (`phases/phase-8.md`)."""
        monkeypatch.setenv("CLAUDE_PID", "4242")
        if environment is None:
            monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
        else:
            monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", environment)
        stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "claude")})
        rec = run_main_in_process(repo, monkeypatch, payload, filed="pid-100")
        assert rec["pid"] == 50, rec

    @pytest.mark.rule("a-persons-own-commit")
    @pytest.mark.parametrize("outer", ["the-outer-session", None])
    def test_refuses_a_pid_exported_for_another_session(self, repo, monkeypatch, outer):
        """Round 1 of work item 1791384157, yellow 4. A `claude` started from
        another session's Bash inherits that session's `CLAUDE_PID`, and a hook
        the harness gives no variable of its own would record it in the inner
        session's lease, which no reader of the inner session matches. Where the
        environment's session id is not the payload's, absent included, the lease
        records the walk's answer, as before #868. Red at `1680ea76`, where it
        recorded 4242."""
        monkeypatch.setenv("CLAUDE_PID", "4242")
        if outer is None:
            monkeypatch.delenv("CLAUDE_CODE_SESSION_ID", raising=False)
        else:
            monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", outer)
        stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "claude")})
        rec = run_main_in_process(repo, monkeypatch, "sess-inner")
        assert rec["pid"] == 50, rec

    def test_refuses_to_raise_where_the_lease_directory_is_unwritable(self, repo):
        """Failure is silent by contract; the hook must not become a blocker."""
        d = lease_dir(repo)
        os.chmod(d, 0o500)
        try:
            run_lease_hook(repo, "sess-y")
        finally:
            os.chmod(d, 0o700)


# Left for `hooks/hooksession.py`, under their names: each asks its
# `claude_pid` through the process tree `stub_process_tree` fakes.
def test_the_session_pid_walks_past_the_shell(monkeypatch):
    """The immediate parent is the shell that spawned the hook — measured here,
    /bin/zsh, with claude two levels up. Recording getppid() would name a
    process that dies constantly, and every dead shell would retire a live
    session's lease. The lease writer's own walk (`owner_pid`) left with #868;
    it asks `hooks/hooksession.py#claude_pid`, the reader the commit gate's
    lease route asks too."""
    import hooksession

    stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "claude")})
    assert hooksession.claude_pid() == 50


def test_the_session_pid_is_none_without_a_claude_ancestor(monkeypatch):
    """An extension host is not named `claude`. No pid is recorded, so the
    guard reads the lease as unattributable rather than as an exited session."""
    import hooksession

    stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "code")})
    assert hooksession.claude_pid() is None


@pytest.mark.parametrize("value", ["", "x", "0", "1", "-5"])
def test_an_exported_pid_that_names_no_process_falls_back_to_the_walk(
    monkeypatch, value
):
    """S5 of work item 1791384157, the other side: a value that is not a pid
    above 1 is not read, and the walk answers as it did."""
    import hooksession

    stub_process_tree(monkeypatch, 100, {100: (50, "/bin/zsh"), 50: (1, "claude")})
    assert hooksession.claude_pid({"CLAUDE_PID": value}) == 50, value


test_census = census_case(TARGET)
