"""`hooks/dispatch.py`: one process per event, same decisions as one process
per gate, and a gate that fails is said once per session.

The dispatcher runs every gate of a group in its own process, merges their
outputs into one stdout, and skips a gate that raises, so the rest of the
group still decides and no tool call is blocked. The skip leaves a record
under the git common dir, keyed by session and gate, and the `stop` group says
every pending record once, at the end of the main session's turn, as a
`systemMessage` (#28).

Most cases drive `dispatch.py` from a COPY of `hooks/` as a subprocess, which
is what production spawns. A broken gate is one whose file is replaced by
`def broken(:\\n`. The live `hooks/` is never touched. The cases come from
`tests/test_dispatch.py`, `tests/test_a_gate_that_fails_says_so.py`,
`tests/test_console_is_not_utf8.py` (#942's phase 6) and
`tests/test_the_root_migrates_itself.py`, whose case of the session-start
group's order is in `Test_module` (#942's phase 7).
"""

import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys

import pytest
from conftest import (
    HOSTILE,
    KOREAN,
    census_case,
    decision_of,
    declare_routing,
    git,
    load_hook_module,
)

TARGET = "hooks/dispatch.py"

HOOKS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "hooks"))
BROKEN = "def broken(:\n"
RECORDS = "specseal-gate-failure"

# The words a person reads (contract rule 14). Pinned whole, so an edit that
# changes what the line says has to change this too.
LABEL_ONE = "SpecSeal: 1 gate failed and was skipped"
CLOSING = (
    "Nothing was blocked, and each gate is said once per session. "
    "Updating or reinstalling the plugin usually repairs it."
)


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


def hooks_copy(tmp_path, files):
    """A copy of `hooks/` with each `files` entry written over the file of
    that name; a value of None removes it."""
    hooks = tmp_path / "hooks"
    shutil.copytree(HOOKS, hooks, ignore=shutil.ignore_patterns("__pycache__"))
    for name, body in files.items():
        path = hooks / name
        if body is None:
            path.unlink()
        else:
            path.write_text(body, encoding="utf-8")
    return hooks


def dispatch(hooks, group, body, cwd=None):
    """`dispatch.py <group>` from `hooks`, as the harness spawns it. `body`
    is sent as JSON, or as it is where it is already a string."""
    r = subprocess.run(
        [sys.executable, str(hooks / "dispatch.py"), group],
        input=body if isinstance(body, str) else json.dumps(body),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        cwd=cwd,
    )
    assert r.returncode == 0, r.stderr
    return r.stdout


def dispatch_under(group, payload, encoding):
    """Run the entry point the way `hooks.json` does, on a hostile console.

    Bytes rather than `text=True`, and `ensure_ascii=False`, because the
    default JSON encoder escapes every non-ASCII character -- an earlier suite
    piped `json.dumps` output and so could never carry the byte that breaks
    this. Its stdin defect survived three review rounds behind that.
    """
    return subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), group],
        input=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        capture_output=True,
        timeout=30,
        env={**os.environ, "PYTHONIOENCODING": encoding, "PYTHONUTF8": "0"},
    )


def bash(repo, session, command="git commit -m x", **extra):
    body = {
        "hook_event_name": "PreToolUse",
        "tool_name": "Bash",
        "session_id": session,
        "tool_input": {"command": command},
        "cwd": str(repo),
    }
    body.update(extra)
    return body


def edit(repo, session, name="f.txt", **extra):
    """An `Edit` of NAME in REPO, which the routing check at the edit tools
    refuses on a branch no declaration names."""
    body = {
        "hook_event_name": "PreToolUse",
        "tool_name": "Edit",
        "session_id": session,
        "tool_input": {"file_path": str(repo / name)},
        "cwd": str(repo),
    }
    body.update(extra)
    return body


def stop(hooks, repo, session, **extra):
    body = {"hook_event_name": "Stop", "session_id": session, "cwd": str(repo)}
    body.update(extra)
    return dispatch(hooks, "stop", body)


def said(stdout):
    """The `systemMessage` lines of one JSON object, which carries no
    decision (S12)."""
    out = json.loads(stdout)
    assert "hookSpecificOutput" not in out and "decision" not in out, out
    return out["systemMessage"].split("\n")


def records(repo, session):
    directory = repo / ".git" / RECORDS / session
    return sorted(os.listdir(directory)) if directory.is_dir() else []


def opted_in(repo):
    (repo / "seal").mkdir()
    return repo


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def gates_said(lines):
    """The gate each line of a report names, in the order said."""
    return [line.split(" ", 1)[0] for line in lines[1:-1]]


ASTRAL = "\U0001d54f"


def units(text):
    """`text`'s length in UTF-16 units, the length the harness counts."""
    return len(text.encode("utf-16-le", "surrogatepass")) // 2


def longest_report(d, count):
    """The longest report `count` failed gates can put before a stamp, in
    UTF-16 units, the blank line `report` adds included: every gate this
    plugin names and three foreign ones, in every group this plugin names and
    a foreign one, at every phase, with each field past its cap -- a record
    an older or newer plugin wrote is what the read-side caps are for
    (round 1's 🟡 3). Each gate is said once per session, so `count` distinct
    gates."""
    fields = {"error": "E" * 300, "message": "m" * 400}
    gates = {g for gs in d.GROUPS.values() for g in gs} | {c * 300 for c in "xyz"}
    groups = [*d.GROUPS, "G" * 300]
    longest = {}
    for gate in gates:
        for group in groups:
            for phase in ("load", "run", None):
                line = d.describe(gate, {"group": group, "phase": phase, **fields})
                longest[gate] = max(longest.get(gate, ""), line, key=units)
    chosen = sorted(longest.values(), key=units, reverse=True)[:count]
    one = count == 1
    label = d.LABEL.format(
        count=f"{count} gate{'' if one else 's'}", verb="was" if one else "were"
    )
    return units("\n".join([label, *chosen, d.CLOSING])) + 2


STAMP = os.path.join(
    os.path.dirname(HOOKS), "skills", "verify", "scripts", "seal_stamp.py"
)
STAMP_VALUES = {
    "tree": "aaa1111",
    "base": "bbb2222",
    "from": "origin/base",
    "item": "/x/seal/specs/1799000000-an-item",
    "session": "s-1",
    "scale": 0.9,
    "rows": [("SEALED", ""), None, ("tree", "aaa1111"), ("suite", "3 passed")],
}


def stop_live(repo, session):
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), "stop"],
        input=json.dumps(
            {"hook_event_name": "Stop", "session_id": session, "cwd": str(repo)}
        ),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )
    assert r.returncode == 0, r.stderr
    return r.stdout


def stop_in_process(repo, monkeypatch, capsys, printed):
    """`dispatch.main()` for `stop`, with the group's own output replaced by
    `printed`; what it printed."""
    d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_the_join")
    monkeypatch.setattr(d, "run_gate", lambda _gate, _payload: printed)
    monkeypatch.setattr(sys, "argv", ["dispatch.py", "stop"])
    body = {"hook_event_name": "Stop", "session_id": "s-x", "cwd": str(repo)}
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps(body)))
    d.main()
    return capsys.readouterr().out


def pending_record(repo):
    directory = repo / ".git" / RECORDS / "s-x"
    directory.mkdir(parents=True)
    (directory / "mode-gate.py.pending").write_text("{}", encoding="utf-8")


# Every shape found to raise in `classify` or `merge` at `551c7967`, after the
# gates had run and outside `run_gate`'s isolation, so the group exited 1.
UNREADABLE = (
    "null",
    "0",
    "3",
    "[1]",
    "[]",
    '"words"',
    "true",
    '{"hookSpecificOutput": 3}',
    '{"hookSpecificOutput": {"permissionDecision": 5}}',
    '{"hookSpecificOutput": {"permissionDecision": "ask", '
    '"permissionDecisionReason": 7}}',
    '{"systemMessage": 3}',
)


def printing(text):
    """A gate whose `main()` prints `text` and nothing else."""
    return f"def main():\n    print({text!r})\n"


class Test_run_gate:
    @pytest.mark.skipif(
        sys.platform == "win32",
        reason="the probe puts a shell stub named `ruff` on PATH; Windows resolves "
        "a bare name through CreateProcess, which does not find a .cmd",
    )
    def test_accepts_an_edit_and_hands_the_gate_its_file_not_the_group_name(
        self, tmp_path
    ):
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
        assert log.is_file() and str(target) in log.read_text(encoding="utf-8"), (
            r.stderr
        )

    def test_accepts_a_system_exit_from_main_as_a_gate_finishing(self, repo, tmp_path):
        """`worktree-guard.py` ends with `sys.exit(0)` from `main()` at nine
        sites, so a `SystemExit` there is a gate finishing, not failing."""
        opted_in(repo)
        hooks = hooks_copy(
            tmp_path, {"mode-gate.py": "import sys\ndef main():\n    sys.exit(0)\n"}
        )
        dispatch(hooks, "pre-bash", bash(repo, "s-x", command="ls"))
        assert records(repo, "s-x") == []

    def test_refuses_to_let_a_crashing_gate_take_the_group_down(
        self, repo, monkeypatch
    ):
        d = dispatch_module()
        monkeypatch.setattr(
            d, "GROUPS", {"g": ("nonexistent-gate.py", "routing-edit-gate.py")}
        )
        (repo / "seal").mkdir()
        out = io.StringIO()
        argv, stdin = sys.argv, sys.stdin
        try:
            sys.argv = ["dispatch.py", "g"]
            sys.stdin = io.StringIO(json.dumps(edit(repo, "s1")))
            import contextlib

            with contextlib.redirect_stdout(out):
                d.main()
        finally:
            sys.argv, sys.stdin = argv, stdin
        assert decision_of(out.getvalue()) == "deny"

    def test_refuses_to_let_a_system_exit_at_load_take_the_group_down(
        self, repo, tmp_path, monkeypatch
    ):
        """S7. A module body calling `sys.exit(0)` used to escape `run_gate`,
        whose catch was `Exception` alone, and end the whole group: the gate
        after it never decided. Seen red against the phase-1 tree, where
        `main()` raised `SystemExit` and printed nothing. The shape of the
        crashing-gate case above, run against a copy so the planted gate never
        enters the live `hooks/`."""
        opted_in(repo)
        hooks = hooks_copy(tmp_path, {"exits-at-load.py": "import sys\nsys.exit(0)\n"})
        d = load(hooks / "dispatch.py", "dispatch_for_s7")
        monkeypatch.setattr(
            d, "GROUPS", {"g": ("exits-at-load.py", "routing-edit-gate.py")}
        )
        out = io.StringIO()
        monkeypatch.setattr(sys, "argv", ["dispatch.py", "g"])
        monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps(edit(repo, "s-x"))))
        with contextlib.redirect_stdout(out):
            d.main()
        assert decision_of(out.getvalue()) == "deny", out.getvalue()
        record = repo / ".git" / RECORDS / "s-x" / "exits-at-load.py.pending"
        body = json.loads(record.read_text(encoding="utf-8"))
        at = body.pop("at")
        assert body == {
            "group": "g",
            "phase": "load",
            "error": "SystemExit",
            "message": "0",
        }
        # When and in what order this call's failures happened: the writer's
        # clock in nanoseconds, and this gate's place among them.
        assert type(at[0]) is int and at[0] > 0 and at[1] == 0, at


class Test_classify:
    def test_accepts_json_the_merge_can_read_as_before(self):
        """The shapes that were read before still are: an object with no
        decision, one whose optional fields are null, and a decision."""
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_readable")
        assert d.classify('{"a": 1}') == ("json", {"a": 1})
        nulls = {"hookSpecificOutput": None, "systemMessage": None}
        assert d.classify(json.dumps(nulls)) == ("json", nulls)
        ask = {"hookSpecificOutput": {"permissionDecision": "ask"}}
        assert d.classify(json.dumps(ask)) == ("decision", ask)
        assert d.classify("plain\n") == ("text", "plain")

    def test_accepts_a_deny_beside_a_message_that_is_not_text(self):
        """Round 2's 🟡 3. #661 must not drop output the merge read before. Its
        decision path reads the decision and its reason and never the
        `systemMessage`, and a falsy `hookSpecificOutput` was read as absent.
        Seen red at `02e47435`, where the merge printed nothing for either."""
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_a_deny")
        deny = {
            "hookSpecificOutput": {"permissionDecision": "deny"},
            "systemMessage": 3,
        }
        assert d.classify(json.dumps(deny)) == ("decision", deny)
        assert decision_of(d.merge([json.dumps(deny)], "PreToolUse")) == "deny"
        for falsy in (False, 0, "", []):
            body = {"hookSpecificOutput": falsy, "systemMessage": "m"}
            assert d.classify(json.dumps(body)) == ("json", body), falsy
            assert json.loads(d.merge([json.dumps(body)], "Stop")) == body, falsy
        reason = {
            "hookSpecificOutput": {
                "permissionDecision": "ask",
                "permissionDecisionReason": 7,
            }
        }
        assert d.classify(json.dumps(reason))[0] == "unreadable"

    def test_refuses_json_a_gate_prints_that_is_not_a_hooks_output_and_ends_nothing(
        self, repo, tmp_path
    ):
        """#661. A gate printing JSON the merge cannot read — not an object, or
        an object whose decision or reason is not text, or with no decision a
        message that is not text — used to end its whole group with exit 1,
        taking a neighbour's `deny` or `systemMessage` with it. `null` and `0`
        survive beside a deny and end a group beside a message, so each shape
        is planted beside both. The output is dropped, the group decides as it
        would without it, and the gate is said at turn end."""
        opted_in(repo)
        for n, shape in enumerate(UNREADABLE):
            hooks = hooks_copy(
                tmp_path / f"h{n}",
                {
                    # The neighbour's deny, which the planted shape must not take.
                    "worktree-guard.py": printing(decision("deny", "r")),
                    "mode-gate.py": printing(shape),
                    "version-check.py": printing('{"systemMessage": "m"}'),
                    "root-migrate.py": printing(shape),
                },
            )
            session = f"s-{n}"
            out = dispatch(hooks, "pre-bash", bash(repo, session))
            assert decision_of(out) == "deny", (shape, out)
            start = {"hook_event_name": "SessionStart", "session_id": session}
            start["cwd"] = str(repo)
            assert json.loads(dispatch(hooks, "session-start", start)) == {
                "systemMessage": "m"
            }, shape
            lines = said(stop(hooks, repo, session))
            assert lines[1].startswith(
                "mode-gate.py failed while running in pre-bash (ValueError: printed "
                "JSON the dispatcher cannot read: "
            ), (shape, lines)
            assert gates_said(lines) == ["mode-gate.py", "root-migrate.py"], lines


class Test_merge:
    def test_accepts_the_strictest_decision_and_keeps_every_reason(self):
        """An overruled gate still has something the user needs to read."""
        d = dispatch_module()
        out = json.loads(
            d.merge(
                [decision("ask", "review"), decision("deny", "worktree")], "PreToolUse"
            )
        )
        assert out["hookSpecificOutput"]["permissionDecision"] == "deny"
        reason = out["hookSpecificOutput"]["permissionDecisionReason"]
        assert "review" in reason and "worktree" in reason

    def test_accepts_plain_reminders_into_one_stdout(self):
        d = dispatch_module()
        assert d.merge(["first\n", "", "second\n"], "PostToolUse") == "first\nsecond"

    def test_refuses_to_drop_a_line_said_once_beside_a_neighbours_decision(self):
        """#692: `hook-install.py` says its line once per session, so a `deny`
        beside it in the same group must not drop it."""
        d = dispatch_module()
        out = json.loads(
            d.merge(
                [
                    json.dumps({"systemMessage": "installed"}),
                    decision("deny", "worktree"),
                ],
                "PreToolUse",
            )
        )
        assert out["systemMessage"] == "installed"
        assert out["hookSpecificOutput"]["permissionDecision"] == "deny"


class Test_opted_in:
    def test_accepts_a_broken_opt_in_module_as_opted_in_and_says_it(
        self, repo, tmp_path
    ):
        """S6b. `optin.py` is what the report asks whether to speak, and it is
        the broken module: "cannot tell" writes the record. `sealer-stamp.py`
        fails in the `stop` group itself and is said in the same invocation."""
        opted_in(repo)
        hooks = hooks_copy(tmp_path, {"optin.py": BROKEN})
        dispatch(hooks, "pre-bash", bash(repo, "s-x"))
        # One file time for all of them, as a coarse file system gives: the order
        # said is `pre-bash`'s own order, which is not name order here. The git
        # hook installer imports `optin.py` too, and it runs first (#692).
        for path in (repo / ".git" / RECORDS / "s-x").iterdir():
            os.utime(path, ns=(10**18, 10**18))
        lines = said(stop(hooks, repo, "s-x"))
        assert gates_said(lines) == [
            "hook-install.py",
            "worktree-guard.py",
            "mode-gate.py",
            "sealer-stamp.py",
        ], lines
        assert "sealer-stamp.py failed to load in stop (SyntaxError: " in "\n".join(
            lines
        ), lines
        assert any(
            line.startswith("sealer-stamp.py ")
            and line.endswith("); calls went ahead without it.")
            for line in lines
        ), lines

    def test_refuses_a_repository_that_never_opted_in_and_records_nothing(
        self, repo, tmp_path
    ):
        """S8. A globally installed plugin does not write into, or speak about,
        a repository that does not run the workflow."""
        hooks = hooks_copy(tmp_path, {"mode-gate.py": BROKEN})
        dispatch(hooks, "pre-bash", bash(repo, "s-x"))
        assert not (repo / ".git" / RECORDS).exists()
        assert stop(hooks, repo, "s-x") == ""


class Test_record:
    def test_accepts_a_record_once_and_asks_about_it_once(self, repo, monkeypatch):
        """The opt-in is asked only for a gate not yet written down, so a gate
        that stays broken costs no `optin.py` load after its first record. And
        the file is created exclusively: a record that appears between the check
        and the write — the race, forced here by blinding the check — is not
        overwritten."""
        opted_in(repo)
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_the_record")
        asked = []
        real = d.opted_in
        monkeypatch.setattr(d, "opted_in", lambda *a: asked.append(a) or real(*a))
        body = bash(repo, "s-x")
        failure = [("mode-gate.py", "run", RuntimeError("first"))]
        d.record("pre-bash", failure, body)
        d.record("pre-bash", [("mode-gate.py", "run", RuntimeError("second"))], body)
        assert len(asked) == 1, asked
        # Blind only the records directory: `toplevel` asks `exists` too, and
        # blinding that would stop the call before it reached the write.
        real_exists = os.path.exists
        monkeypatch.setattr(
            d.os.path,
            "exists",
            lambda p: False if RECORDS in str(p) else real_exists(p),
        )
        d.record("pre-bash", [("mode-gate.py", "run", RuntimeError("third"))], body)
        path = repo / ".git" / RECORDS / "s-x" / "mode-gate.py.pending"
        assert json.loads(path.read_text(encoding="utf-8"))["message"] == "first"

    def test_accepts_a_foreign_class_name_capped_where_it_is_written(self, repo):
        """S14 (#722). `record` wrote `type(exc).__name__` whole, and a class
        from outside the plugin names itself whatever it likes. A 120-character
        name and a name of 60 characters outside the BMP (120 units) are each
        written at `NAME_CAP` units, and an astral character that would cross
        the cap is left out whole rather than split into half a pair. Seen red
        against the `record` that wrote the name uncapped."""
        opted_in(repo)
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_the_name_cap")
        assert d.NAME_CAP == 40
        wide = type("N" * 120, (Exception,), {})
        astral = type("y" + ASTRAL * 60, (Exception,), {})
        d.record(
            "pre-bash",
            [
                ("mode-gate.py", "run", wide("x")),
                ("worktree-guard.py", "load", astral("z")),
            ],
            bash(repo, "s-x"),
        )
        directory = repo / ".git" / RECORDS / "s-x"
        written = {
            name: json.loads((directory / name).read_text(encoding="utf-8"))["error"]
            for name in ("mode-gate.py.pending", "worktree-guard.py.pending")
        }
        assert written == {
            "mode-gate.py.pending": "N" * 40,
            "worktree-guard.py.pending": "y" + ASTRAL * 19,
        }, written
        assert all(units(name) <= d.NAME_CAP for name in written.values())
        body = json.loads(
            (directory / "mode-gate.py.pending").read_text(encoding="utf-8")
        )
        line = d.describe("mode-gate.py", body)
        assert f"({'N' * 40}: x)" in line, line

    def test_refuses_to_record_where_there_is_nowhere_to_write(self, repo, tmp_path):
        """S13. No session id, or a records directory that cannot be made — a
        FILE of that name, because the CI job runs as root and `chmod` stops
        nothing there. Each leaves the group's stdout what it is with the gate
        absent, and exits 0.

        Each side of a comparison gets a session of its own: `mode-gate.py`
        denies the first call of a session and not the next, so two calls under
        one id differ on that gate's state and say nothing about this one."""
        opted_in(repo)
        broken = hooks_copy(tmp_path / "a", {"mode-gate.py": BROKEN})
        absent = hooks_copy(tmp_path / "b", {"mode-gate.py": None})

        nameless = bash(repo, "")
        del nameless["session_id"]
        assert dispatch(broken, "pre-bash", nameless) == dispatch(
            absent, "pre-bash", nameless
        )
        assert not (repo / ".git" / RECORDS).exists(), "recorded with no session"

        (repo / ".git" / RECORDS).write_text("", encoding="utf-8")
        assert dispatch(broken, "pre-bash", bash(repo, "s-f1")) == dispatch(
            absent, "pre-bash", bash(repo, "s-f2")
        )
        assert stop(broken, repo, "s-f1") == ""

    def test_refuses_a_session_id_naming_a_directory_outside_the_records(
        self, repo, tmp_path
    ):
        """The id becomes a path part, so a separator in a malformed one must not
        escape — `hooks/worktree-guard.py#already_asked` measured `../../escaped`
        putting a file at the repository root."""
        opted_in(repo)
        hooks = hooks_copy(tmp_path, {"mode-gate.py": BROKEN})
        dispatch(hooks, "pre-bash", bash(repo, "../../escaped"))
        assert not (repo / "escaped").exists()
        assert not (repo / ".git" / "escaped").exists()
        assert records(repo, "escaped") == ["mode-gate.py.pending"]
        # `..` has no separator to strip, and would name the records directory's
        # parent: the common dir itself.
        dispatch(hooks, "pre-bash", bash(repo, ".."))
        assert not (repo / ".git" / "mode-gate.py.pending").exists()


class Test_describe:
    def test_accepts_a_gate_that_raises_in_main_as_a_run_failure(self, repo, tmp_path):
        """S5. The import succeeded and `main()` raised: the line says `while
        running`, and names the class and the message's first line."""
        opted_in(repo)
        hooks = hooks_copy(
            tmp_path,
            {
                "mode-gate.py": "def main():\n    raise RuntimeError('boom\\nsecond line')\n"
            },
        )
        dispatch(hooks, "pre-bash", bash(repo, "s-x", command="ls"))
        lines = said(stop(hooks, repo, "s-x"))
        assert lines[1] == (
            "mode-gate.py failed while running in pre-bash (RuntimeError: boom); "
            "calls went ahead without it, and the other gates in pre-bash still "
            "decided."
        ), lines

    def test_accepts_every_group_that_loads_a_gate_that_fails_to_load(
        self, repo, tmp_path
    ):
        """Round 1's 🟡 1. A load failure belongs to the file, so it fails in
        every group that loads it, and the record is written once, by the first.
        `worktree-guard.py` sits in `pre-bash` and `pre-agent`, and the
        `pre-agent` half is the `isolation: "worktree"` spawn going unguarded:
        one `pre-bash` failure must not read as a Bash-only gap. A group where
        the gate stands alone, `post-agent` for `worktree_consent.py`, is named
        among the failures and not among the groups whose other gates decided.

        Changed by #689: the guard and the consent writer load `cmdline_base.py`,
        so that module is broken beside `cmdline.py`, which
        `implementer-notice.py` loads."""
        opted_in(repo)
        hooks = hooks_copy(tmp_path, {"cmdline.py": BROKEN, "cmdline_base.py": BROKEN})
        dispatch(hooks, "pre-bash", bash(repo, "s-x"))
        dispatch(
            hooks,
            "post-bash",
            bash(repo, "s-x", command="ls", hook_event_name="PostToolUse"),
        )
        lines = said(stop(hooks, repo, "s-x"))
        by_gate = {line.split(" ", 1)[0]: line for line in lines[1:-1]}
        guard, consent = by_gate["worktree-guard.py"], by_gate["worktree_consent.py"]
        assert guard.startswith(
            "worktree-guard.py failed to load in pre-bash and pre-agent ("
        ), guard
        assert guard.endswith(
            "; calls went ahead without it, and the other gates in pre-bash and "
            "pre-agent still decided."
        ), guard
        assert consent.startswith(
            "worktree_consent.py failed to load in post-bash and post-agent ("
        ), consent
        assert consent.endswith(
            "; calls went ahead without it, and the other gates in post-bash still decided."
        ), consent
        assert by_gate["implementer-notice.py"].startswith(
            "implementer-notice.py failed to load in post-bash ("
        ), by_gate

        # A failure while running depends on the payload, so the same two-group
        # gate failing in `main()` names only the group it was seen in.
        directory = repo / ".git" / RECORDS / "s-y"
        directory.mkdir(parents=True)
        (directory / "worktree-guard.py.pending").write_text(
            json.dumps({"group": "pre-agent", "phase": "run", "error": "E"}),
            encoding="utf-8",
        )
        assert said(stop(hooks, repo, "s-y"))[1] == (
            "worktree-guard.py failed while running in pre-agent (E); calls went "
            "ahead without it, and the other gates in pre-agent still decided."
        )

    def test_accepts_a_record_another_version_wrote_with_its_own_group_and_a_capped_gate(
        self,
    ):
        """Round 1's 🟡 3. A load failure whose record names a group today's
        `GROUPS` does not put the gate in -- a gate that moved between versions --
        names that group alone, rather than adding every group the gate is in
        now. And the gate's name, the record's file name, is cut at `NAME_CAP`
        like the type name. Seen red at `64196684`."""
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_the_foreign_record")
        moved = d.describe(
            "session-lease.py", {"group": "session-start", "phase": "load"}
        )
        assert moved.startswith("session-lease.py failed to load in session-start;"), (
            moved
        )
        known = d.describe("worktree-guard.py", {"group": "pre-bash", "phase": "load"})
        assert "in pre-bash and pre-agent" in known, known
        long = d.describe("g" * 120, {"group": "pre-bash", "phase": "run"})
        assert long.startswith("g" * d.NAME_CAP + " failed while running"), long
        astral = d.describe("y" + ASTRAL * 60, {"phase": "run"})
        assert astral.startswith("y" + ASTRAL * 19 + " failed while running"), astral

    def test_refuses_a_field_an_older_plugin_wrote_past_its_cap(self):
        """S15 (#722). `read_record` says an older or newer plugin may have
        written the record, so `describe` cannot trust the writer's caps: a
        300-unit `error`, a 400-unit `message` and a 300-unit `group` are each
        cut to their cap as the line is built. Seen red against the `describe`
        that interpolated the fields whole."""
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_the_read_cap")
        line = d.describe(
            "mode-gate.py",
            {
                "group": "g" * 300,
                "phase": "run",
                "error": "E" * 300,
                "message": "m" * 400,
            },
        )
        assert f" in {'g' * d.NAME_CAP} (" in line, line
        assert f"({'E' * d.NAME_CAP}: {'m' * d.MESSAGE_CAP})" in line, line
        astral = d.describe(
            "mode-gate.py",
            {"phase": "run", "error": "y" + ASTRAL * 300, "message": ASTRAL * 400},
        )
        assert f"(y{ASTRAL * 19}: {ASTRAL * 100})" in astral, astral


class Test_draw:
    def test_accepts_a_broken_gate_at_the_end_of_the_turn_and_only_once(
        self, repo, tmp_path
    ):
        """S1, S3, S4, S12, S14. Seen red against the `dispatch.py` that only
        swallowed, where `stop` printed nothing at all."""
        opted_in(repo)
        hooks = hooks_copy(tmp_path, {"mode-gate.py": BROKEN})

        dispatch(hooks, "pre-bash", bash(repo, "s-x"))
        assert records(repo, "s-x") == ["mode-gate.py.pending"]
        lines = said(stop(hooks, repo, "s-x"))
        assert lines[0] == LABEL_ONE, lines
        assert lines[1].startswith(
            "mode-gate.py failed to load in pre-bash (SyntaxError: "
        ), lines
        assert lines[1].endswith(
            "); calls went ahead without it, and the other gates in pre-bash still decided."
        ), lines
        assert lines[2:] == [CLOSING], lines
        assert records(repo, "s-x") == ["mode-gate.py.reported"]

        # S3: the same session, the same broken gate: nothing new, nothing said.
        dispatch(hooks, "pre-bash", bash(repo, "s-x"))
        assert records(repo, "s-x") == ["mode-gate.py.reported"]
        assert stop(hooks, repo, "s-x") == ""

        # S4: another session is told for itself.
        dispatch(hooks, "pre-bash", bash(repo, "s-y"))
        assert said(stop(hooks, repo, "s-y"))[0] == LABEL_ONE

    @pytest.mark.parametrize(
        "broken, named",
        [
            (
                {"cmdline.py": BROKEN},
                ["answer-write.py", "implementer-notice.py"],
            ),
            ({"cmdline_base.py": BROKEN}, ["worktree-guard.py", "worktree_consent.py"]),
            (
                {"cmdline.py": BROKEN, "cmdline_base.py": BROKEN},
                [
                    "answer-write.py",
                    "worktree-guard.py",
                    "implementer-notice.py",
                    "worktree_consent.py",
                ],
            ),
        ],
        ids=["cmdline", "cmdline_base", "both"],
    )
    def test_accepts_every_gate_a_broken_shared_module_breaks_and_no_other(
        self, repo, tmp_path, broken, named
    ):
        """S6. A broken shared reader names every gate that imports it, once, and
        no gate that does not. `cmdline.py` is imported by
        `implementer-notice.py`, and since #773 by `answer-write.py` through
        `tokens.given`, whose read leaves the heredoc bodies out; since #689
        `cmdline_base.py`, the reader frozen at `86256492`, is imported by the
        worktree guard and `worktree_consent.py`. The worktree guard's import
        of `cmdline.py` is guarded, so a broken `cmdline.py` does not name it.

        Changed by #689 twice. Round 1's fix pass broke both readers at once to
        keep four gates named, which lost the per-module "no gate that does not"
        (round 2 of 1790745049, white 4); each reader is now broken alone as well."""
        opted_in(repo)
        hooks = hooks_copy(tmp_path, broken)
        dispatch(hooks, "pre-bash", bash(repo, "s-x"))
        dispatch(
            hooks,
            "post-bash",
            bash(repo, "s-x", command="ls", hook_event_name="PostToolUse"),
        )
        # Every record gets one file time, as a file system with coarse times
        # gives records written in one call (Windows CI did): the order said is
        # the order the gates failed, which each record carries itself.
        for path in (repo / ".git" / RECORDS / "s-x").iterdir():
            os.utime(path, ns=(10**18, 10**18))
        lines = said(stop(hooks, repo, "s-x"))
        assert lines[0] == f"SpecSeal: {len(named)} gates failed and were skipped", (
            lines
        )
        assert gates_said(lines) == named, lines
        assert lines[-1] == CLOSING

    def test_accepts_records_oldest_first(self, repo, tmp_path):
        """One line per record, in the order the gates failed, so a name that
        sorts first is not said first. The order is the `at` pair each record
        carries — the writer's clock and its place in that call's failures — and
        not the file's time, which Windows CI gave two records alike (NTFS keeps
        100 ns, and a file time can be set at a coarser tick). A record with no
        `at`, from another plugin version, falls back to its file time, set here
        whole seconds apart so every file system keeps them distinct."""
        opted_in(repo)
        directory = repo / ".git" / RECORDS / "s-x"
        directory.mkdir(parents=True)
        carried = (
            ("worktree-guard.py", [10**18, 0]),
            ("answer-write.py", [10**18, 1]),
            ("mode-gate.py", [10**18 + 5, 0]),
        )
        for gate, at in carried:
            path = directory / (gate + ".pending")
            path.write_text(
                json.dumps({"group": "pre-bash", "at": at}), encoding="utf-8"
            )
            os.utime(path, ns=(10**18, 10**18))
        # An `at` that is not two integers is read as absent, not compared.
        for gate, body, seconds in (
            ("version-check.py", {"group": "session-start", "at": ["late", 1]}, 1),
            ("session-lease.py", {"group": "post-bash"}, 2),
        ):
            old = directory / (gate + ".pending")
            old.write_text(json.dumps(body), encoding="utf-8")
            os.utime(old, ns=(10**18 + seconds * 10**9, 10**18 + seconds * 10**9))
        lines = said(stop(hooks_copy(tmp_path, {}), repo, "s-x"))
        assert gates_said(lines) == [
            "worktree-guard.py",
            "answer-write.py",
            "mode-gate.py",
            "version-check.py",
            "session-lease.py",
        ], lines

    def test_accepts_a_record_that_cannot_be_read_and_names_its_gate(
        self, repo, tmp_path
    ):
        """A record another plugin version wrote, or a half-written one: the
        gate's name is the file's name, and that is the report's whole value."""
        opted_in(repo)
        directory = repo / ".git" / RECORDS / "s-x"
        directory.mkdir(parents=True)
        planted = {
            "lint-python.py": "not json",
            "mode-gate.py": "[1]",
            "version-check.py": json.dumps({"group": 5, "phase": "load"}),
            "session-lease.py": json.dumps({"error": "OSError"}),
            "worktree-guard.py": json.dumps(
                {"group": "pre-bash\nstop", "error": "E", "message": "a\n  b"}
            ),
        }
        # None of these carries an `at`, so their file times order them: whole
        # seconds apart, which every file system keeps distinct. 1 ns apart was
        # below NTFS's 100 ns, and Windows CI said them in name order.
        for n, (gate, body) in enumerate(planted.items()):
            path = directory / (gate + ".pending")
            path.write_text(body, encoding="utf-8")
            os.utime(path, ns=(10**18 + n * 10**9, 10**18 + n * 10**9))
        lines = said(stop(hooks_copy(tmp_path, {}), repo, "s-x"))
        assert lines[1:-1] == [
            "lint-python.py failed; calls went ahead without it.",
            "mode-gate.py failed; calls went ahead without it.",
            "version-check.py failed to load; calls went ahead without it.",
            "session-lease.py failed (OSError); calls went ahead without it.",
            "worktree-guard.py failed in pre-bash stop (E: a b); calls went ahead "
            "without it.",
        ], lines

    def test_refuses_a_record_that_cannot_be_claimed(self, repo, tmp_path):
        """The rename to `.reported` comes before the line, so a record another
        drawer took first — here, one whose `.reported` name is a directory the
        rename cannot replace — is not said by this one."""
        opted_in(repo)
        directory = repo / ".git" / RECORDS / "s-x"
        (directory / "mode-gate.py.reported").mkdir(parents=True)
        (directory / "mode-gate.py.pending").write_text("{}", encoding="utf-8")
        assert stop(hooks_copy(tmp_path, {}), repo, "s-x") == ""

    def test_refuses_records_in_a_repository_not_opted_in(self, repo, tmp_path):
        """A record that is there in a repository that does not run the workflow
        — left from before it opted out — is neither said nor taken."""
        directory = repo / ".git" / RECORDS / "s-x"
        directory.mkdir(parents=True)
        (directory / "mode-gate.py.pending").write_text("{}", encoding="utf-8")
        assert stop(hooks_copy(tmp_path, {}), repo, "s-x") == ""
        assert records(repo, "s-x") == ["mode-gate.py.pending"]

    def test_refuses_a_subagents_stop_and_says_its_failure_at_the_main_sessions(
        self, repo, tmp_path
    ):
        """S10. A subagent's tool payload carries the parent's `session_id`, so
        its failure is recorded under the main session. A `Stop`-shaped payload
        naming an agent is a subagent's end, and draws nothing."""
        opted_in(repo)
        hooks = hooks_copy(tmp_path, {"session-lease.py": BROKEN})
        dispatch(
            hooks,
            "post-bash",
            bash(
                repo, "s-x", command="ls", hook_event_name="PostToolUse", agent_id="a-1"
            ),
        )
        assert records(repo, "s-x") == ["session-lease.py.pending"]
        assert stop(hooks, repo, "s-x", agent_id="a-1") == ""
        assert stop(hooks, repo, "s-x", hook_event_name="SubagentStop") == ""
        assert records(repo, "s-x") == ["session-lease.py.pending"]
        assert said(stop(hooks, repo, "s-x"))[0] == LABEL_ONE


class Test_report:
    def test_accepts_the_report_before_the_stamp_and_leaves_the_stamp_unchanged(
        self, repo, tmp_path
    ):
        """S9. One `systemMessage`: the report first, then a blank line, then
        the stamp exactly as it is drawn with nothing pending — so the drawing
        stays the last thing on the screen (#400). The live `hooks/` is run, not
        a copy, because `sealer-stamp.py` reaches `seal_stamp.py` beside it; the
        record is planted, which is also a record written by another process."""
        opted_in(repo)
        stamp = load(STAMP, "seal_stamp_for_s9")
        for session in ("s-alone", "s-both"):
            stamp.write_values(str(repo / ".git"), session, STAMP_VALUES)
        directory = repo / ".git" / RECORDS / "s-both"
        directory.mkdir(parents=True)
        (directory / "mode-gate.py.pending").write_text(
            json.dumps(
                {
                    "group": "pre-bash",
                    "phase": "run",
                    "error": "KeyError",
                    "message": "'x'",
                }
            ),
            encoding="utf-8",
        )
        alone = said(stop_live(repo, "s-alone"))
        both = said(stop_live(repo, "s-both"))
        assert alone[0].startswith("SEALED aaa1111"), alone
        assert both[: len(both) - len(alone) - 1] == [
            LABEL_ONE,
            "mode-gate.py failed while running in pre-bash (KeyError: 'x'); calls "
            "went ahead without it, and the other gates in pre-bash still decided.",
            CLOSING,
        ], both
        assert both[len(both) - len(alone) - 1] == "", both
        assert both[len(both) - len(alone) :] == alone, "the stamp moved"

    def test_accepts_an_object_without_a_message_and_makes_the_report_its_message(
        self, repo, monkeypatch, capsys
    ):
        """The group's own keys are kept, and the report is the whole message
        where the group had none."""
        opted_in(repo)
        pending_record(repo)
        out = json.loads(
            stop_in_process(repo, monkeypatch, capsys, '{"continue": true}')
        )
        assert out["continue"] is True
        assert out["systemMessage"].split("\n")[0] == LABEL_ONE
        assert out["systemMessage"].endswith(CLOSING), out

    def test_accepts_the_groups_decision_exactly_as_without_the_gate(
        self, repo, tmp_path
    ):
        """S2. The report leaves the failing call's own stdout alone: a broken
        gate and an absent one give the same bytes, the routing check's deny
        beside them included."""
        opted_in(repo)
        broken = hooks_copy(tmp_path / "a", {"mode-gate.py": BROKEN})
        absent = hooks_copy(tmp_path / "b", {"mode-gate.py": None})
        assert dispatch(broken, "pre-bash", bash(repo, "s-a")) == dispatch(
            absent, "pre-bash", bash(repo, "s-b")
        )
        broken = hooks_copy(tmp_path / "c", {"routing-edit-gate.py": BROKEN})
        absent = hooks_copy(tmp_path / "d", {"routing-edit-gate.py": None})
        assert dispatch(broken, "pre-edit", edit(repo, "s-c")) == dispatch(
            absent, "pre-edit", edit(repo, "s-d")
        )

    def test_refuses_plain_text_at_stop_and_the_records_wait(
        self, repo, monkeypatch, capsys
    ):
        """No gate in `stop` prints plain text, and plain `Stop` stdout reaches a
        different reader than a `systemMessage`. So such a turn end is printed
        as it was, and the records wait for one that can carry them."""
        opted_in(repo)
        pending_record(repo)
        assert stop_in_process(repo, monkeypatch, capsys, "plain words\n") == (
            "plain words\n"
        )
        assert records(repo, "s-x") == ["mode-gate.py.pending"]

    def test_refuses_a_payload_it_cannot_read_and_records_nothing(self, repo, tmp_path):
        """Not JSON, not an object, or an empty `cwd`: nothing is recorded,
        nothing raises, and dispatch exits 0 with the group's own stdout. An
        empty `cwd` must not fall back to the directory the process happens to
        stand in, which is a repository here."""
        opted_in(repo)
        broken = hooks_copy(tmp_path / "a", {"mode-gate.py": BROKEN})
        absent = hooks_copy(tmp_path / "b", {"mode-gate.py": None})
        for payload in ("not json", "[1, 2]"):
            assert dispatch(broken, "pre-bash", payload) == dispatch(
                absent, "pre-bash", payload
            )
        dispatch(broken, "pre-bash", bash(repo, "s-x", cwd=""), cwd=str(repo))
        assert not (repo / ".git" / RECORDS).exists()


class Test_main:
    def test_accepts_a_group_and_reaches_the_gate_inside_it(self, repo):
        (repo / "seal").mkdir()
        assert (
            decision_of(run_dispatch("pre-bash", payload("git commit -m x", repo)))
            == "deny"
        )

    def test_accepts_a_gate_with_nothing_to_say_and_leaves_the_group_silent(self, repo):
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

    def test_accepts_post_bash_and_writes_the_lease(self, repo):
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

    @pytest.mark.parametrize("encoding", HOSTILE)
    def test_accepts_a_payload_the_console_cannot_decode_and_reaches_a_verdict(
        self, korean_repo, encoding
    ):
        """The stdin half, which is the half that was missed.

        `dispatch.py` holds the only stdin read production takes, so a raise there
        takes every gate in the group down at once — and `hooks.json` runs
        `python3 … || py -3 …`, so the retry meets an already-consumed stdin and
        passes silently a second time.

        Measured against a tree with the reconfigure removed: `exit 1`, stdout
        empty, `UnicodeDecodeError: 'cp949' codec can't decode byte 0xed`.
        """
        r = dispatch_under(
            "pre-bash",
            {
                "tool_name": "Bash",
                "session_id": f"ko-{encoding}",
                "cwd": str(korean_repo),
                "tool_input": {"command": f"git commit -m {KOREAN}"},
            },
            encoding,
        )
        assert decision_of(r) == "deny", (
            f"{encoding}: the gate went silent, which the harness reads as "
            f"approval. stderr: {r.stderr.decode('utf-8', 'replace')[-300:]}"
        )
        assert r.returncode == 0, r.stderr.decode("utf-8", "replace")[-300:]

    def test_refuses_an_unknown_group_and_does_nothing(self, repo):
        assert (
            run_dispatch("pre-nothing", payload("git commit -m x", repo)).strip() == ""
        )

    def test_accepts_the_stop_group_and_names_its_event(self, monkeypatch, capsys):
        """`main` names the event on its decision path, and named every group
        that is not `pre-` as `PostToolUse`. The `stop` group answers `Stop`, so
        a decision coming out of it, should one ever do, says so."""
        d = dispatch_module()
        decision = json.dumps(
            {
                "hookSpecificOutput": {
                    "permissionDecision": "ask",
                    "permissionDecisionReason": "r",
                }
            }
        )
        monkeypatch.setattr(d, "run_gate", lambda _gate, _payload: decision)
        monkeypatch.setattr(sys, "argv", ["dispatch.py", "stop"])
        monkeypatch.setattr(sys, "stdin", io.StringIO("{}"))
        d.main()
        said = json.loads(capsys.readouterr().out)
        assert said["hookSpecificOutput"]["hookEventName"] == "Stop", said


class Test_module:
    def test_the_installer_runs_before_the_gates_it_serves(self):
        """#692: first in `pre-bash`, so a stub that went missing is back before
        the command runs; last at `session-start`, after the root migrations."""
        d = dispatch_module()
        assert d.GROUPS["pre-bash"][0] == "hook-install.py"
        assert d.GROUPS["session-start"][-1] == "hook-install.py"

    def test_the_hook_is_wired_into_session_start_before_the_git_hooks(self):
        """The dispatch group is the only thing that runs hooks in production, and
        the git hooks are installed into the root this one may just have moved, so
        the order is part of the contract."""
        dispatch = load_hook_module("dispatch.py", "dispatch_for_root")
        group = dispatch.GROUPS["session-start"]
        assert "root-migrate.py" in group
        assert group.index("root-migrate.py") < group.index("hook-install.py")

    def test_a_message_is_its_first_line_and_capped(self):
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_the_cap")
        assert d.first_line(RuntimeError("\n  one  \ntwo")) == "one"
        assert d.first_line(RuntimeError("y" * 500)) == "y" * d.MESSAGE_CAP
        assert d.MESSAGE_CAP == 200
        # The cap is in UTF-16 units, the unit the harness counts the `Stop`
        # message in (`seal_stamp.MESSAGE_RESERVE`): a character outside the BMP
        # is two, and one that would pass the cap is left out whole.
        astral = "\U0001d54f"
        assert d.first_line(RuntimeError(astral * 500)) == astral * 100
        assert d.first_line(RuntimeError("y" + astral * 500)) == "y" + astral * 99
        # The last character inside the BMP is one unit.
        last = chr(0xFFFF)
        assert d.first_line(RuntimeError(last * 500)) == last * d.MESSAGE_CAP

    def test_only_nothing_or_an_object_can_carry_the_report(self):
        """JSON that is not an object has nowhere to put a message either. It
        cannot reach `beside` through `main()` today — `merge()`'s own reader
        raises on it first — so it is asked of `beside` directly."""
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_beside")
        assert d.beside("  \n") == {}
        assert d.beside('{"a": 1}') == {"a": 1}
        assert d.beside("[1]") is None
        assert d.beside("plain") is None

    def test_two_failed_gates_fit_the_reserve_with_every_field_at_its_cap(self):
        """S14 (#722). With the name capped as well as the message, the longest
        two-gate report fits `seal_stamp.MESSAGE_RESERVE` and a third would not.
        The reserve's comment states the figures this measures, so a cap that
        moves has to move the comment with it."""
        d = load(os.path.join(HOOKS, "dispatch.py"), "dispatch_for_the_reserve")
        stamp = load(STAMP, "seal_stamp_for_the_reserve")
        one, two, three = (longest_report(d, n) for n in (1, 2, 3))
        assert two <= stamp.MESSAGE_RESERVE < three, (one, two, three)
        with open(STAMP, encoding="utf-8") as handle:
            source = handle.read()
        comment = source.split("\nMESSAGE_RESERVE = ", 1)[0].rsplit("\n\n", 1)[1]
        for figure in (one, two, three):
            assert f"{figure:,}" in comment, (figure, comment)

    def test_the_walk_agrees_with_its_twin_in_sealer_stamp(self, repo, tmp_path):
        """`questions.md` Q2, answered duplicated: `dispatch.py` cannot import
        `sealer-stamp.py` without importing `console` and `optin` with it. So the
        two walks are held to one answer — in a subdirectory of the main
        checkout, and in a linked worktree, where `.git` is a file and git is
        asked. A failure recorded from the worktree is said from the checkout."""
        d = load_hook_module("dispatch.py", "dispatch_for_the_twin")
        sealer = load_hook_module("sealer-stamp.py", "sealer_stamp_for_the_twin")
        optin = load_hook_module("optin.py", "optin_for_the_twin")
        tree = tmp_path / "tree"
        git(repo, "worktree", "add", "-q", str(tree), "feature/x")
        (repo / "docs" / "deep").mkdir(parents=True)
        for cwd in (repo / "docs" / "deep", tree):
            top = d.toplevel(str(cwd))
            assert top == sealer.toplevel(str(cwd)), cwd
            assert d.common_dir(top) == optin.git_common_dir(top), cwd
        assert os.path.samefile(d.common_dir(d.toplevel(str(tree))), repo / ".git")

        def no_process(*_a, **_k):
            raise AssertionError("a main checkout started a process")

        real_run = d.subprocess.run
        d.subprocess.run = no_process
        try:
            assert d.common_dir(str(repo)) == str(repo / ".git")
        finally:
            d.subprocess.run = real_run

        # Local mode, so the worktree's branch, which has no `seal/`, is opted
        # in from both trees.
        (repo / ".git" / "seal").mkdir()
        hooks = hooks_copy(tmp_path, {"mode-gate.py": BROKEN})
        dispatch(hooks, "pre-bash", bash(tree, "s-x"))
        assert records(repo, "s-x") == ["mode-gate.py.pending"]
        assert said(stop(hooks, repo, "s-x"))[0] == LABEL_ONE


test_census = census_case(TARGET)
