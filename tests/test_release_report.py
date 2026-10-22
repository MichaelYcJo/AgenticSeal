"""`release-report`'s cases under the test layout (#942).

The release table carries one row per test file: its priced cases and
seconds in `.test_durations` at the last release tag and now, slowest now
first. The rows are a report and never a ceiling. The other cases of this
script are still in `tests/test_the_release_table_reads_two_trees_and_fails_nothing.py`
until the batch that rebuilds this module moves them.

Seen red before they were committed (contract rule 15): three cases failed
against the script that printed no test-file rows, and `mutation-check`
turned the fourth, the exit on an unreadable tree, red by letting `main` go
on past the tree it could not read.
"""

import importlib.util
import json
import os

import pytest
from conftest import census_case

TARGET = ".github/scripts/release_report.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_SPEC = importlib.util.spec_from_file_location(
    "specseal_release_report_under_layout", os.path.join(ROOT, TARGET)
)
report = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(report)

AT = {
    "tests/test_a.py::test_one": 1.0,
    "tests/test_a.py::test_two": 2.0,
    "tests/test_gone.py::test_one": 5.0,
}
NOW = {"tests/test_a.py::test_one": 1.5, "tests/test_new.py::test_one": 9.0}


def priced(root, durations):
    """A tree at ROOT holding `.test_durations` as DURATIONS; its path."""
    root.mkdir()
    (root / ".test_durations").write_text(json.dumps(durations), encoding="utf-8")
    return str(root)


class Test_module_rows:
    def test_accepts_two_trees_as_one_row_per_file_slowest_now_first(self, tmp_path):
        rows = report.module_rows(
            priced(tmp_path / "at", AT), priced(tmp_path / "now", NOW)
        )
        assert rows == [
            "| `tests/test_new.py` | — | — | 1 | 9.0 |",
            "| `tests/test_a.py` | 2 | 3.0 | 1 | 1.5 |",
            "| `tests/test_gone.py` | 1 | 5.0 | — | — |",
        ]

    def test_refuses_a_durations_file_that_prices_no_case(self, tmp_path):
        with pytest.raises(report.Unreadable, match="no object of case ids"):
            report.module_rows(
                priced(tmp_path / "at", ["x"]), priced(tmp_path / "now", NOW)
            )


class Test_main:
    def test_accepts_the_file_rows_printed_under_the_release_table(
        self, tmp_path, monkeypatch, capsys
    ):
        monkeypatch.setattr(report, "meter", lambda: None)
        monkeypatch.setattr(report, "reading", lambda root, kernel: ({}, 1.0, {}))
        at, now = priced(tmp_path / "at", AT), priced(tmp_path / "now", NOW)
        assert report.main(["--against", "v0.0.1", "--at", at, "--root", now]) == 0
        out = capsys.readouterr().out
        assert out.index("### Against v0.0.1") < out.index(
            "### Test files against v0.0.1"
        )
        assert (
            "| Test file | Cases at v0.0.1 | Seconds at v0.0.1 | Cases now | Seconds now |\n"
            "|---|---|---|---|---|\n"
            "| `tests/test_new.py` | — | — | 1 | 9.0 |\n"
        ) in out

    def test_refuses_to_print_rows_for_a_tree_it_cannot_read(self, tmp_path, capsys):
        now = priced(tmp_path / "now", NOW)
        missing = str(tmp_path / "missing")
        assert report.main(["--against", "v0.0.1", "--at", missing, "--root", now]) == 2
        assert capsys.readouterr().out == ""


test_census = census_case(TARGET)
