"""`tests/conftest.py`'s own cases (#841, #942).

A case whose call runs past `SLOW_CASE_S` is named in the run's terminal
summary with its seconds, and nothing fails for it: a time reading is noisy,
and on 2026-10-16 a loaded machine failed a guarantor's run on time alone.
The summary hook is driven through one inner pytest run, built once for the
module, that loads this repository's `conftest.py` with the value lowered
so the run takes a second.

Seen red before they were committed (contract rule 15): the three accepting
cases failed against the conftest that still held the failing ceiling, which
had neither `SLOW_CASE_S` nor a summary hook, and `mutation-check` turned
each refusing case red by breaking the condition it pins.
"""

import os
import subprocess
import sys
import types

import censuses
import conftest
import pytest

TARGET = "tests/conftest.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

INNER_CONFTEST = """\
import importlib.util

_spec = importlib.util.spec_from_file_location("repo_conftest", {path!r})
_repo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_repo)
_repo.SLOW_CASE_S = 0.3
pytest_terminal_summary = _repo.pytest_terminal_summary
"""

INNER_TESTS = """\
import time


def test_slow():
    time.sleep(0.6)


def test_slow_and_failing():
    time.sleep(0.6)
    assert False, "its own failure"


def test_quick():
    pass
"""


@pytest.fixture(scope="module")
def inner_run(tmp_path_factory):
    """One pytest run over a slow case and a quick one, `SLOW_CASE_S` at
    0.3 s; its exit code and its output."""
    d = tmp_path_factory.mktemp("slow-case")
    path = os.path.join(ROOT, TARGET)
    (d / "conftest.py").write_text(INNER_CONFTEST.format(path=path), encoding="utf-8")
    (d / "test_inner.py").write_text(INNER_TESTS, encoding="utf-8")
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
        cwd=d,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    return run.returncode, run.stdout + run.stderr


def call(nodeid, seconds, when="call"):
    """A report as `slow_lines` reads one."""
    return types.SimpleNamespace(nodeid=nodeid, duration=seconds, when=when)


class Test_slow_lines:
    def test_accepts_a_call_past_the_value_named_with_its_seconds(self, monkeypatch):
        monkeypatch.setattr(conftest, "SLOW_CASE_S", 90)
        reports = [
            call("tests/test_x.py::test_y", 91.24),
            call("tests/test_x.py::test_z", 300),
        ]
        assert conftest.slow_lines(reports) == [
            "slow case: tests/test_x.py::test_z ran 300.0 s, past SLOW_CASE_S of 90 s",
            "slow case: tests/test_x.py::test_y ran 91.2 s, past SLOW_CASE_S of 90 s",
        ]

    def test_refuses_a_call_at_the_value_and_a_setup_past_it(self, monkeypatch):
        monkeypatch.setattr(conftest, "SLOW_CASE_S", 90)
        reports = [
            call("tests/test_x.py::test_y", 90),
            call("tests/test_x.py::test_z", 200, "setup"),
        ]
        assert conftest.slow_lines(reports) == []


class Test_pytest_terminal_summary:
    def test_accepts_a_slow_case_named_and_failing_nothing(self, inner_run):
        code, out = inner_run
        assert code == 1, out
        assert "1 failed, 2 passed" in out, out
        assert "its own failure" in out, out
        assert "slow case: test_inner.py::test_slow ran " in out, out
        assert "slow case: test_inner.py::test_slow_and_failing ran " in out, out

    def test_refuses_to_name_a_quick_case(self, inner_run):
        _, out = inner_run
        assert "test_quick ran" not in out, out


class Test_module:
    def test_the_value_is_the_one_work_item_1791270165_set(self):
        assert conftest.SLOW_CASE_S == 90


class Test_census_case:
    def test_accepts_a_target_every_census_passes(self, tmp_path, monkeypatch):
        (tmp_path / "hooks").mkdir()
        (tmp_path / "hooks" / "x.py").write_text(
            'open(p, encoding="utf-8")\n', encoding="utf-8"
        )
        monkeypatch.setattr(censuses, "ROOT", str(tmp_path))
        assert conftest.census_case("hooks/x.py")() is None

    def test_refuses_a_target_one_census_flags_naming_it(self, tmp_path, monkeypatch):
        (tmp_path / "hooks").mkdir()
        (tmp_path / "hooks" / "y.py").write_text("open(p)\n", encoding="utf-8")
        monkeypatch.setattr(censuses, "ROOT", str(tmp_path))
        with pytest.raises(AssertionError, match=r"hooks/y\.py:1: encoding: "):
            conftest.census_case("hooks/y.py")()


test_census = conftest.census_case(TARGET)
