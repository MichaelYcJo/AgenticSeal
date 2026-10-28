"""`release-report`'s cases under the test layout (#942).

The release table carries one row per test file: its priced cases and
seconds in `.test_durations` at the last release tag and now, slowest now
first. The rows are a report and never a ceiling. #942's phase 6 placed here
the script's other cases from
`tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, which
keeps the case that reads the tests workflow's job.

Seen red before they were committed (contract rule 15): three cases failed
against the script that printed no test-file rows, and `seal mutate`
turned the fourth, the exit on an unreadable tree, red by letting `main` go
on past the tree it could not read.
"""

import importlib.util
import json
import os

import pytest
from conftest import ROOT, census_case

TARGET = ".github/scripts/release_report.py"

_SPEC = importlib.util.spec_from_file_location(
    "agentic_release_report_under_layout", os.path.join(ROOT, TARGET)
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


AGENT = "---\nname: proofer\nskills:\n  - review\n---\n"


def tree(root, agent_body, durations, docs):
    """A tree holding one agent and its one skill, `.test_durations` as
    `durations`, `CLAUDE.md`, `CONTRIBUTING.md` and `docs/<name>.md` for each
    of `docs`; returns its path as text."""
    files = {
        "agents/proofer.md": AGENT + agent_body,
        "skills/review/SKILL.md": "# review\n",
        ".test_durations": json.dumps(durations),
        "CLAUDE.md": "# c\n",
        "CONTRIBUTING.md": "# contributing\n",
        **{f"docs/{name}.md": text for name, text in docs.items()},
    }
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, "utf-8", newline="\n")
    return str(root)


def job(name, minutes):
    return {
        "name": name,
        "started_at": "2026-10-15T10:00:00Z",
        "completed_at": f"2026-10-15T10:{minutes:02d}:00Z",
    }


def jobs_file(path, jobs):
    path.write_text("".join(json.dumps(j) + "\n" for j in jobs), "utf-8")
    return str(path)


def rows_of(out):
    """`{What: (tag cell, now cell, change cell)}` of the printed table."""
    rows = {}
    for line in out.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("| ") and len(cells) == 4 and cells[0] != "What":
            rows[cells[0]] = tuple(cells[1:])
    return rows


class _Kernel:
    """A stand-in for `payload_meter.py`: one agent, `proofer`, whose
    composition is ROWS, or raises ERROR where one is given."""

    def __init__(self, rows=(), error=None):
        self.rows, self.error = list(rows), error

    def agents_in(self, root):
        return {"proofer": "definition"}

    def composition(self, root, plugin, agent, definition, verbose):
        if self.error:
            raise self.error
        return self.rows


class Test_preloads:
    def test_accepts_each_agents_own_share_summed(self, tmp_path):
        rows = [
            {"bytes": 10, "share": "agent"},
            {"bytes": 5, "share": "skill"},
            {"bytes": 3, "share": "agent"},
        ]
        assert report.preloads(str(tmp_path), _Kernel(rows)) == {"proofer": 13}

    def test_refuses_a_definition_it_cannot_read_as_unreadable(self, tmp_path):
        """An `OSError` reading an agent becomes the exit-2 sentence `main`
        prints, never a traceback."""
        kernel = _Kernel(error=PermissionError(13, "denied", "agents/proofer.md"))
        with pytest.raises(report.Unreadable, match="an agent definition under"):
            report.preloads(str(tmp_path), kernel)


class Test_durations:
    def test_accepts_case_ids_to_whole_and_fractional_seconds(self, tmp_path):
        assert report.durations(priced(tmp_path / "t", {"t::a": 1, "t::b": 2.5})) == {
            "t::a": 1,
            "t::b": 2.5,
        }

    def test_refuses_a_file_of_booleans_as_seconds(self, tmp_path):
        """`true` passes an `isinstance(v, int)` test and is no number of
        seconds, so a file of them is no reading."""
        with pytest.raises(report.Unreadable, match="no object of case ids"):
            report.durations(priced(tmp_path / "t", {"t::a": True}))


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


class Test_leg_minutes:
    def test_accepts_a_leg_without_its_job_that_has_no_start_time(self, tmp_path):
        started = job("pytest (ubuntu-latest, 3.12, 1)", 9)
        unstarted = job("pytest (ubuntu-latest, 3.12, 2)", 20)
        del unstarted["started_at"]
        jobs = jobs_file(tmp_path / "jobs.jsonl", [started, unstarted])
        assert report.leg_minutes(jobs) == {"ubuntu": 9.0}

    def test_refuses_a_job_whose_name_only_begins_as_a_pytest_job(self, tmp_path):
        """The whole name is the pytest job's shape or the job is not one."""
        jobs = jobs_file(
            tmp_path / "jobs.jsonl", [job("pytest (ubuntu-latest, 3.12) report", 9)]
        )
        assert report.leg_minutes(jobs) == {}


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

    def test_the_release_table_reads_two_trees_and_fails_nothing(
        self, tmp_path, capsys
    ):
        """S9: a grown preload, an agent and a document on one side only and a
        leg with no run at the tag are each a row, and the exit is 0 whatever
        they show: the tag's tree and this one side by side, each leg's minutes
        summed over its pytest jobs, `no run found` where a run has no job
        list."""
        at = tree(
            tmp_path / "at", "x" * 100, {"t::a": 1.0, "t::b": 2.0}, {"gone": "ab\n"}
        )
        scout = "---\nname: scout\n---\n"
        (tmp_path / "at" / "agents" / "scout.md").write_text(
            scout, "utf-8", newline="\n"
        )
        now = tree(
            tmp_path / "now", "x" * 150, {"t::a": 1.0, "t::b": 3.0}, {"new": "abc\r\n"}
        )
        jobs = jobs_file(
            tmp_path / "jobs.jsonl",
            [
                job("pytest (ubuntu-latest, 3.12)", 9),
                job("pytest (windows-latest, 3.12, 1)", 20),
                job("pytest (windows-latest, 3.12, 2)", 25),
                job("lint", 1),
            ],
        )
        code = report.main(
            ["--against", "v1.2.3", "--at", at, "--root", now, "--ci-jobs", jobs]
        )
        out = capsys.readouterr().out
        assert code == 0, out
        assert out.startswith("### Against v1.2.3\n"), out
        assert "| What | v1.2.3 | Now | Change |" in out, out
        rows = rows_of(out)
        grown = len(AGENT) + 100 + len("# review\n")
        assert rows["preload `proofer` (bytes)"] == (
            f"{grown:,}",
            f"{grown + 50:,}",
            f"+50 ({50 / grown:+.1%})",
        ), rows
        assert rows["preload `scout` (bytes)"] == (f"{len(scout)}", "—", "gone"), rows
        assert rows["the suite (seconds)"] == ("3", "4", "+1 (+33.3%)"), rows
        assert rows["`ubuntu` leg (minutes)"] == ("no run found", "9.0", "—"), rows
        assert rows["`windows` leg (minutes)"] == ("no run found", "45.0", "—"), rows
        assert rows["`macos` leg (minutes)"] == ("no run found", "no run found", "—")
        assert rows["`docs/gone.md` (bytes)"] == ("3", "—", "gone"), rows
        assert rows["`docs/new.md` (bytes)"] == ("—", "4", "new"), rows
        assert rows["`CLAUDE.md` (bytes)"] == ("4", "4", "+0 (+0.0%)"), rows
        assert "`CONTRIBUTING.md` (bytes)" in rows, rows

    def test_accepts_each_process_archive_file_as_a_document_row(
        self, tmp_path, capsys
    ):
        """#945: each `seal/process/<X.Y.Z>.md` is a document row beside
        `docs/*.md`, so the archive's size is read at each release; the rest
        of the `seal/` root is no document and has no row."""
        at = tree(tmp_path / "at", "", {"t::a": 1.0}, {})
        now = tree(tmp_path / "now", "", {"t::a": 1.0}, {})
        for rel in (
            "seal/process/0.23.0.md",
            "seal/README.md",
            "seal/threads/1-x/a.md",
        ):
            path = tmp_path / "now" / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# 0.23.0\n", "utf-8", newline="\n")
        assert report.main(["--against", "v1", "--at", at, "--root", now]) == 0
        rows = rows_of(capsys.readouterr().out)
        seal = [what for what in rows if what.startswith("`seal/")]
        assert seal == ["`seal/process/0.23.0.md` (bytes)"], rows
        assert rows["`seal/process/0.23.0.md` (bytes)"] == ("—", "9", "new"), rows

    @pytest.mark.parametrize(
        "lines",
        [
            "",
            "not json\n",
            '{"id": 1}\n',
            json.dumps(job("pytest (ubuntu-latest, 3.12)", 9)) + "\nnot json\n",
        ],
        ids=["empty", "not json", "no name", "a job, then a line that is none"],
    )
    def test_a_job_list_that_holds_no_run_reads_no_run_found(
        self, tmp_path, capsys, lines
    ):
        """A job list that is empty or is no job list `gh` wrote, even after a
        job that reads, is no reading, never a traceback or a part of a run, and
        the table still prints at exit 0."""
        at = tree(tmp_path / "at", "", {"t::a": 1.0}, {})
        jobs = tmp_path / "jobs.jsonl"
        jobs.write_text(lines, "utf-8")
        argv = ["--against", "v1", "--at", at, "--root", at, "--ci-jobs", str(jobs)]
        assert report.main([*argv, "--ci-jobs-at", str(tmp_path / "absent")]) == 0
        rows = rows_of(capsys.readouterr().out)
        assert rows["`ubuntu` leg (minutes)"] == ("no run found", "no run found", "—")

    @pytest.mark.parametrize(
        "spoil, said",
        [
            ("no tree", "is no directory"),
            ("no durations", ".test_durations under"),
            ("durations not json", "cannot be read"),
            ("durations not seconds", "is no object of case ids to seconds"),
        ],
    )
    def test_a_tree_that_cannot_be_read_is_exit_2(self, tmp_path, capsys, spoil, said):
        """Nothing was compared, so nothing is printed as if it had been."""
        at = tree(tmp_path / "at", "", {"t::a": 1.0}, {})
        durations = os.path.join(at, ".test_durations")
        if spoil == "no tree":
            at = str(tmp_path / "nowhere")
        elif spoil == "no durations":
            os.remove(durations)
        elif spoil == "durations not json":
            with open(durations, "w", encoding="utf-8") as handle:
                handle.write("{")
        else:
            with open(durations, "w", encoding="utf-8") as handle:
                handle.write('{"t::a": "slow"}')
        root = tree(tmp_path / "now", "", {"t::a": 1.0}, {})
        assert report.main(["--against", "v1", "--at", at, "--root", root]) == 2
        captured = capsys.readouterr()
        assert captured.out == "", captured.out
        assert said in captured.err, captured.err
        assert "Nothing was compared." in captured.err, captured.err


class Test_module:
    def test_the_table_reads_this_tree_against_the_last_tag(self):
        """The repository's own two trees read: an agent row for every agent
        this tree defines, three leg rows, and a row for every `docs/*.md`."""
        rows = report.table(
            "v0",
            report.reading(ROOT, report.meter()),
            report.reading(ROOT, report.meter()),
            {},
            {},
        )
        found = rows_of(rows)
        agents = sorted(
            f[: -len(".md")] for f in os.listdir(os.path.join(ROOT, "agents"))
        )
        for agent in agents:
            assert found[f"preload `{agent}` (bytes)"][2] == "+0 (+0.0%)", agent
        docs = [f for f in os.listdir(os.path.join(ROOT, "docs")) if f.endswith(".md")]
        for name in docs:
            assert f"`docs/{name}` (bytes)" in found, name
        assert sum(1 for k in found if k.endswith("leg (minutes)")) == 3, found


test_census = census_case(TARGET)
