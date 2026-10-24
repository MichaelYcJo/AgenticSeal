"""lint-python: the one hook that rewrites the user's source and can hit the network."""

import json
import os
import subprocess
import sys

import pytest
from conftest import census_case, load_hook_module

TARGET = "hooks/lint-python.py"

lp = load_hook_module("lint-python.py", "lint_py")


def run_hook_stdin(payload, tmp_path):
    script = os.path.join(os.path.dirname(__file__), "..", "hooks", "lint-python.py")
    return subprocess.run(
        [sys.executable, script],
        input=payload,
        cwd=str(tmp_path),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


# --- the project decides -----------------------------------------------------
#
# This hook rewrites the file you just saved, and `ruff check --fix` changes
# code, not layout. Installed globally it used to do that everywhere — to repos
# using black, to repos with their own ruff settings it ignored, to repos that
# had chosen no formatter. Configuring ruff is a project saying it wants ruff.


def _py_in(tmp_path, *, config=None, name="m.py"):
    if config:
        for filename, body in config.items():
            (tmp_path / filename).write_text(body, encoding="utf-8")
    f = tmp_path / name
    f.write_text("import os\nx = 1\n", encoding="utf-8")
    return f


def _ran(monkeypatch, tmp_path, path, env=None):
    calls = []
    monkeypatch.setattr(lp, "resolve_runner", lambda: ["ruff"])
    monkeypatch.setattr(
        lp.subprocess,
        "run",
        lambda *a, **k: calls.append(a[0]) or subprocess.CompletedProcess(a, 0),
    )
    monkeypatch.setattr(lp.sys, "argv", ["lint-python.py", str(path)])
    for k, v in (env or {}).items():
        monkeypatch.setenv(k, v)
    lp.main()
    return calls


class Test_uses_ruff:
    @pytest.mark.parametrize(
        "config",
        [
            {"ruff.toml": "line-length = 88\n"},
            {".ruff.toml": "line-length = 88\n"},
            {"pyproject.toml": "[tool.ruff]\nline-length = 88\n"},
        ],
        ids=["ruff-toml", "dotted-ruff-toml", "pyproject-tool-ruff"],
    )
    def test_accepts_a_project_that_configures_ruff(
        self, monkeypatch, tmp_path, config
    ):
        f = _py_in(tmp_path, config=config)
        assert _ran(monkeypatch, tmp_path, f)

    def test_accepts_config_found_from_a_subdirectory(self, monkeypatch, tmp_path):
        (tmp_path / "ruff.toml").write_text("line-length = 88\n", encoding="utf-8")
        sub = tmp_path / "src" / "pkg"
        sub.mkdir(parents=True)
        f = sub / "m.py"
        f.write_text("x = 1\n", encoding="utf-8")
        assert _ran(monkeypatch, tmp_path, f)

    @pytest.mark.parametrize(
        "config",
        [
            {"pyproject.toml": '[project]\nname = "x"\n'},
            {"pyproject.toml": "[tool.black]\nline-length = 100\n"},
        ],
        ids=["pyproject-alone", "black"],
    )
    def test_refuses_a_pyproject_without_a_tool_ruff_table(
        self, monkeypatch, tmp_path, config
    ):
        """A pyproject.toml says nothing about formatting, and a project using
        black is left alone."""
        f = _py_in(tmp_path, config=config)
        assert _ran(monkeypatch, tmp_path, f) == []

    def test_refuses_a_project_with_no_formatter(self, monkeypatch, tmp_path):
        assert _ran(monkeypatch, tmp_path, _py_in(tmp_path)) == []

    def test_refuses_to_search_past_a_repository_boundary(self, monkeypatch, tmp_path):
        """A parent checkout's settings must not speak for a nested one."""
        (tmp_path / "ruff.toml").write_text("line-length = 88\n", encoding="utf-8")
        nested = tmp_path / "vendor" / "other"
        (nested / ".git").mkdir(parents=True)
        f = nested / "m.py"
        f.write_text("x = 1\n", encoding="utf-8")
        assert _ran(monkeypatch, tmp_path, f) == []


class Test_main:
    def test_accepts_a_python_file_and_runs_check_fix_then_format(
        self, monkeypatch, tmp_path
    ):
        (tmp_path / "ruff.toml").write_text("line-length = 88\n", encoding="utf-8")
        f = tmp_path / "m.py"
        f.write_text("x = 1\n", encoding="utf-8")
        invocations = []
        monkeypatch.setattr(lp, "resolve_runner", lambda: ["ruff"])
        monkeypatch.setattr(
            lp.subprocess, "run", lambda cmd, **k: invocations.append(cmd) or None
        )
        monkeypatch.setattr(lp.sys, "argv", ["lint-python.py", str(f)])
        lp.main()
        assert [c[1] for c in invocations] == ["check", "format"], invocations
        assert "--fix" in invocations[0] and invocations[0][-1] == str(f)

    def test_refuses_a_non_python_file_before_it_looks_for_a_runner(
        self, monkeypatch, tmp_path
    ):
        called = []
        monkeypatch.setattr(
            lp, "resolve_runner", lambda: called.append("resolved") or ["ruff"]
        )
        monkeypatch.setattr(
            lp.sys, "argv", ["lint-python.py", str(tmp_path / "notes.md")]
        )
        lp.main()
        assert called == [], "a non-.py path must not even look for a runner"

    def test_refuses_quietly_where_no_runner_is_found(self, monkeypatch, tmp_path):
        f = tmp_path / "m.py"
        f.write_text("x = 1\n", encoding="utf-8")
        monkeypatch.setattr(lp, "resolve_runner", lambda: None)
        monkeypatch.setattr(
            lp.subprocess,
            "run",
            lambda *a, **k: (_ for _ in ()).throw(AssertionError("must not run")),
        )
        monkeypatch.setattr(lp.sys, "argv", ["lint-python.py", str(f)])
        lp.main()  # no exception == pass

    def test_refuses_to_let_a_failing_formatter_block_the_edit(
        self, monkeypatch, tmp_path
    ):
        f = tmp_path / "m.py"
        f.write_text("x = 1\n", encoding="utf-8")
        monkeypatch.setattr(lp, "resolve_runner", lambda: ["ruff"])
        monkeypatch.setattr(
            lp.subprocess, "run", lambda *a, **k: (_ for _ in ()).throw(OSError("boom"))
        )
        monkeypatch.setattr(lp.sys, "argv", ["lint-python.py", str(f)])
        lp.main()  # swallowed — a formatter crash must not wedge the session

    def test_refuses_a_malformed_payload_with_exit_zero(self, tmp_path):
        for payload in ("not json at all", "{}", json.dumps({"tool_input": {}})):
            r = run_hook_stdin(payload, tmp_path)
            assert r.returncode == 0, (payload, r.stderr)

    def test_refuses_where_the_off_switch_is_set_even_with_ruff_configured(
        self, monkeypatch, tmp_path
    ):
        f = _py_in(tmp_path, config={"ruff.toml": "line-length = 88\n"})
        assert _ran(monkeypatch, tmp_path, f, env={"SPECSEAL_LINT": "off"}) == []


test_census = census_case(TARGET)
