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
    ROOT,
    census_case,
    git,
    git_dir,
    lease_dir,
    load_hook_module,
    payload,
    run,
    run_hook,
    stub_process_tree,
)

TARGET = "hooks/session-lease.py"

HOOKS = os.path.join(ROOT, "hooks")

sl = load_hook_module("session-lease.py", "sl_owner")


def leases_of(repo):
    d = os.path.join(git_dir(repo), "agentic-leases")
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


class Test_git_dir:
    def test_accepts_a_repository_and_answers_its_absolute_git_dir(self, repo):
        assert sl.git_dir(str(repo)) == git_dir(repo)

    def test_refuses_a_failed_git_whatever_it_printed(self, repo, monkeypatch):
        """A git that exits non-zero answers nothing, even where it wrote a
        path: the exit is the answer, and the lease goes nowhere rather than
        under a directory a failed call named (#1017, the body's `git_dir` row
        on a non-zero exit). The real git prints nothing on a failure, so the
        failure is faked to remove that guarantee (contract rule 13)."""

        def failed(cmd, **kwargs):
            return subprocess.CompletedProcess(cmd, 128, stdout="/x/.git\n", stderr="")

        monkeypatch.setattr(sl.subprocess, "run", failed)
        assert sl.git_dir(str(repo)) is None


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

    def test_accepts_a_notebook_edit_and_leases_the_notebooks_repo(
        self, repo, tmp_path
    ):
        """`NotebookEdit` names its file under `notebook_path`, and it is an
        edit like the other two (#1017, round 3's s6)."""
        p = {
            "tool_name": "NotebookEdit",
            "session_id": "sess-nb",
            "tool_input": {"notebook_path": str(repo / "n.ipynb")},
            "cwd": str(tmp_path),
        }
        run_hook("session-lease.py", p)
        assert leases_of(repo) == ["sess-nb"]

    def test_refuses_a_tool_that_is_neither_bash_nor_an_editor(self, repo):
        """A `Read` in the repository touches nothing, so it leases nothing
        (#1017, the body's tool-test row)."""
        p = {
            "tool_name": "Read",
            "session_id": "sess-read",
            "tool_input": {"file_path": str(repo / "f.txt")},
            "cwd": str(repo),
        }
        run_hook("session-lease.py", p)
        assert leases_of(repo) == []

    def test_refuses_a_target_that_is_no_directory_whatever_git_answers(
        self, repo, monkeypatch
    ):
        """An edited path whose parent is a FILE names no directory to lease.
        The real git refuses such a directory too, so `git_dir` is faked to
        answer for any path, which removes that guarantee (contract rule 13;
        #1017, the body's directory-test row and round 3's s9)."""
        (repo / "f.txt").write_text("x\n", encoding="utf-8")
        answer = git_dir(repo)
        monkeypatch.setattr(sl, "git_dir", lambda path: answer)
        p = {
            "tool_name": "Write",
            "session_id": "sess-file",
            "tool_input": {"file_path": str(repo / "f.txt" / "inner.txt")},
            "cwd": str(repo),
        }
        run(sl, monkeypatch, p)
        assert leases_of(repo) == []

    def test_refuses_a_call_outside_any_repo_without_raising(
        self, tmp_path, monkeypatch
    ):
        """Where `git_dir` finds no repository the hook returns, in the process
        and not by an exception the harness reports (#1017, the body's
        `git_dir` row outside a repository and round 3's s10)."""
        run(sl, monkeypatch, payload("ls", tmp_path, session="sess-out"))
        assert not os.path.exists(tmp_path / "agentic-leases")

    def test_accepts_a_session_id_with_a_separator_and_files_it_by_its_basename(
        self, repo
    ):
        """The id names a file under `agentic-leases/`, so only its last part
        is used, and a separator in it cannot reach another directory (#1017,
        the body's session-id row)."""
        run_hook("session-lease.py", payload("ls", repo, session="nested/sess-n"))
        assert leases_of(repo) == ["sess-n"]

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
        stale = os.path.join(git_dir(repo), "agentic-leases", "sess-old")
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

    def test_refuses_to_record_a_pid_when_reading_the_owner_raises(
        self, repo, monkeypatch
    ):
        """Any error reading the owner records no pid, and the lease is still
        written: a lease is a safety net, never a blocker (#1017, round 3's
        s12)."""

        def broken(environ=None):
            raise RuntimeError("the reader failed")

        monkeypatch.setattr(sl.hooksession, "claude_pid", broken)
        rec = run_main_in_process(repo, monkeypatch, "sess-broken")
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
        `hooks/session-lease.py` at `e0c5a191` (`trail/phases/phase-8.md`)."""
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

    def test_refuses_to_raise_where_the_lease_directory_cannot_be_made(
        self, repo, monkeypatch
    ):
        """A FILE where the lease directory goes makes the write fail on every
        platform, which a mode bit does not on Windows. The failure stays in
        the hook (#1017, the body's write-error row)."""
        blocker = os.path.join(git_dir(repo), "agentic-leases")
        with open(blocker, "w", encoding="utf-8") as f:
            f.write("not a directory")
        run(sl, monkeypatch, payload("ls", repo, session="sess-z"))
        assert os.path.isfile(blocker)


test_census = census_case(TARGET)
