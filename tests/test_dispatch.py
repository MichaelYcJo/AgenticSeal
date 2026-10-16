"""dispatch: one process per event, same decisions as one process per gate."""

import io
import json
import os
import subprocess
import sys

import pytest
from conftest import decision_of, declare_routing, load_hook_module

HOOKS = os.path.join(os.path.dirname(__file__), "..", "hooks")


def run_dispatch(group, payload, env=None):
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), group],
        input=json.dumps(payload),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        env={**os.environ, **(env or {})},
    )
    return r.stdout


def payload(cmd, repo, tool="Bash", session="s1"):
    return {
        "tool_name": tool,
        "session_id": session,
        "tool_input": {"command": cmd},
        "cwd": str(repo),
    }


def test_the_group_reaches_the_gate_inside_it(repo):
    (repo / "seal").mkdir()
    assert (
        decision_of(run_dispatch("pre-bash", payload("git commit -m x", repo)))
        == "deny"
    )


def test_a_gate_with_nothing_to_say_leaves_the_group_silent(repo):
    # The mode is recorded, because `mode-gate.py` joined this group (#151)
    # and an unrecorded one is something it HAS to say. Without the row this
    # case would still pass on the day it was written and would be asserting
    # that a gate stays quiet about a state it was added to name.
    (repo / "seal").mkdir()
    (repo / "seal" / "config.md").write_text(
        "# Repository config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
        encoding="utf-8",
    )
    assert run_dispatch("pre-bash", payload("ls", repo)).strip() == ""


def test_an_unknown_group_does_nothing(repo):
    assert run_dispatch("pre-nothing", payload("git commit -m x", repo)).strip() == ""


def test_post_bash_writes_the_lease(repo):
    """The review reminder this group carried left with its hook (#923); the
    session lease is what the group still writes."""
    (repo / "seal").mkdir()
    declare_routing(repo)
    run_dispatch("post-bash", payload("gh pr comment 42 --body hi", repo))
    gd = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--absolute-git-dir"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()
    assert os.path.isfile(os.path.join(gd, "specseal-leases", "s1"))


@pytest.mark.skipif(
    sys.platform == "win32",
    reason="the probe puts a shell stub named `ruff` on PATH; Windows resolves "
    "a bare name through CreateProcess, which does not find a .cmd",
)
def test_post_edit_does_not_read_the_group_name_as_a_file(tmp_path):
    """lint-python takes a path from argv[1]; under the dispatcher argv[1] is
    the group name, and left alone the hook would format a file called
    "post-edit" — that is, nothing at all."""
    proj = tmp_path / "proj"
    (proj / "bin").mkdir(parents=True)
    (proj / "ruff.toml").write_text("line-length = 88\n", encoding="utf-8")
    target = proj / "a.py"
    target.write_text("x=1\n", encoding="utf-8")
    log = proj / "ruff.log"
    stub = proj / "bin" / "ruff"
    stub.write_text(f'#!/bin/sh\necho "$@" >> {log}\n', encoding="utf-8")
    stub.chmod(0o755)

    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), "post-edit"],
        input=json.dumps(
            {"tool_name": "Edit", "tool_input": {"file_path": str(target)}}
        ),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        env={**os.environ, "PATH": f"{proj / 'bin'}:/usr/bin:/bin"},
    )
    assert r.returncode == 0
    assert log.is_file() and str(target) in log.read_text(encoding="utf-8"), r.stderr


# --- merging --------------------------------------------------------------


def dispatch_module():
    return load_hook_module("dispatch.py", "dispatch_mod")


def decision(kind, reason):
    return json.dumps(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": kind,
                "permissionDecisionReason": reason,
            }
        }
    )


def test_the_strictest_decision_wins_and_every_reason_survives():
    """An overruled gate still has something the user needs to read."""
    d = dispatch_module()
    out = json.loads(
        d.merge([decision("ask", "review"), decision("deny", "worktree")], "PreToolUse")
    )
    assert out["hookSpecificOutput"]["permissionDecision"] == "deny"
    reason = out["hookSpecificOutput"]["permissionDecisionReason"]
    assert "review" in reason and "worktree" in reason


def test_plain_reminders_merge_into_one_stdout():
    d = dispatch_module()
    assert d.merge(["first\n", "", "second\n"], "PostToolUse") == "first\nsecond"


def test_a_line_said_once_survives_a_neighbours_decision():
    """#692: `hook-install.py` says its line once per session, so a `deny`
    beside it in the same group must not drop it."""
    d = dispatch_module()
    out = json.loads(
        d.merge(
            [json.dumps({"systemMessage": "installed"}), decision("deny", "worktree")],
            "PreToolUse",
        )
    )
    assert out["systemMessage"] == "installed"
    assert out["hookSpecificOutput"]["permissionDecision"] == "deny"


def test_the_installer_runs_before_the_gates_it_serves():
    """#692: first in `pre-bash`, so a stub that went missing is back before
    the command runs; last at `session-start`, after the root migrations."""
    d = dispatch_module()
    assert d.GROUPS["pre-bash"][0] == "hook-install.py"
    assert d.GROUPS["session-start"][-1] == "hook-install.py"


def test_a_crashing_gate_does_not_take_the_group_down(repo, monkeypatch):
    d = dispatch_module()
    monkeypatch.setattr(
        d, "GROUPS", {"g": ("nonexistent-gate.py", "commit-review-gate.py")}
    )
    (repo / "seal").mkdir()
    out = io.StringIO()
    argv, stdin = sys.argv, sys.stdin
    try:
        sys.argv = ["dispatch.py", "g"]
        sys.stdin = io.StringIO(json.dumps(payload("git commit -m x", repo)))
        import contextlib

        with contextlib.redirect_stdout(out):
            d.main()
    finally:
        sys.argv, sys.stdin = argv, stdin
    assert decision_of(out.getvalue()) == "deny"
