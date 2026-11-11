"""`release-report`'s cases under the test layout (#942).

The release table carries one row per test file: its priced cases and
seconds in the durations union at the last release tag and now, slowest now
first. The rows are a report and never a ceiling. Each union is a file the
run downloads from a run's `test-durations` artifact, and an absent one is
no reading (#1486 S5). #942's phase 6 placed here
the script's other cases from
`tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, which
keeps the cases that read the tests workflow's job.

Seen red before they were committed (contract rule 15): three cases failed
against the script that printed no test-file rows, and `seal mutate`
turned the fourth, the exit on an unreadable tree, red by letting `main` go
on past the tree it could not read.
"""

import importlib.util
import json
import os

import pytest
from conftest import ROOT, census_case, config_json, mark_root, write

TARGET = ".github/scripts/release_report.py"

_SPEC = importlib.util.spec_from_file_location(
    "agentic_release_report_under_layout", os.path.join(ROOT, *TARGET.split("/"))
)
report = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(report)

AT = {
    "tests/test_a.py::test_one": 1.0,
    "tests/test_a.py::test_two": 2.0,
    "tests/test_gone.py::test_one": 5.0,
}
NOW = {"tests/test_a.py::test_one": 1.5, "tests/test_new.py::test_one": 9.0}


def priced(path, durations):
    """A durations union at PATH holding DURATIONS; its path as text."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(durations), encoding="utf-8")
    return str(path)


AGENT = "---\nname: proofer\nskills:\n  - review\n---\n"


def tree(root, agent_body, docs):
    """A tree holding one agent and its one skill, the core, `CLAUDE.md`,
    `CONTRIBUTING.md` and `docs/<name>.md` for each of `docs`; returns its
    path as text."""
    files = {
        "agents/proofer.md": AGENT + agent_body,
        "skills/review/SKILL.md": "# review\n",
        "skills/core/SKILL.md": "# The core\n",
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
        union = priced(tmp_path / "t.json", {"t::a": 1, "t::b": 2.5})
        assert report.durations(union) == {"t::a": 1, "t::b": 2.5}

    @pytest.mark.parametrize("given", [None, "absent"])
    def test_accepts_no_union_as_no_reading(self, tmp_path, given):
        """S5: no `--durations` given, or a file the download never wrote, is
        no reading, as an absent job list is, and never exit 2."""
        path = None if given is None else str(tmp_path / "absent" / "x.json")
        assert report.durations(path) is None

    def test_refuses_a_file_of_booleans_as_seconds(self, tmp_path):
        """`true` passes an `isinstance(v, int)` test and is no number of
        seconds, so a file of them is no reading."""
        with pytest.raises(report.Unreadable, match="no object of case ids"):
            report.durations(priced(tmp_path / "t.json", {"t::a": True}))


class Test_module_rows:
    def test_accepts_two_unions_as_one_row_per_file_slowest_now_first(self):
        assert report.module_rows(AT, NOW) == [
            "| `tests/test_new.py` | — | — | 1 | 9.0 |",
            "| `tests/test_a.py` | 2 | 3.0 | 1 | 1.5 |",
            "| `tests/test_gone.py` | 1 | 5.0 | — | — |",
        ]

    def test_refuses_a_reading_to_a_side_with_no_union(self):
        """S5: a file the other union prices reads `no union found` on the
        side that has none, never a count or the `—` of a file absent from a
        present union."""
        assert report.module_rows(None, NOW) == [
            "| `tests/test_new.py` | no union found | no union found | 1 | 9.0 |",
            "| `tests/test_a.py` | no union found | no union found | 1 | 1.5 |",
        ]


INDEX = "| File | About |\n|---|---|\n| `docs/g/x.md` | x |\n"


class Test_documents:
    def test_accepts_the_top_level_and_each_group_the_index_names(self, tmp_path):
        """#1312 S6: the policy root's rows are the documents
        `skills/settle/scripts/fold_check.py#documents` lists, the top level
        and each group the index names."""
        docs = {"README": INDEX, "g/x": "abc\n"}
        root = tree(tmp_path / "t", "", docs)
        assert sorted(report.documents(root)) == [
            "CLAUDE.md",
            "CONTRIBUTING.md",
            "docs/README.md",
            "docs/g/x.md",
            "skills/core/SKILL.md",
        ]

    def test_refuses_a_directory_the_index_names_nothing_of(self, tmp_path):
        """#1312 S6: a directory the index names no document of, such as
        `docs/experiments/`, gives no row."""
        docs = {"README": INDEX, "g/x": "abc\n", "experiments/e": "e\n"}
        root = tree(tmp_path / "t", "", docs)
        assert "docs/experiments/e.md" not in report.documents(root)

    def test_accepts_the_policy_root_agentic_seal_names_beside_a_package(
        self, tmp_path
    ):
        """#1059: beside a project's own `seal/`, a package with no marker,
        the `Policy root` key is read from the marked `agentic-seal/`, so the
        rows are the documents under the root it names."""
        root = tree(tmp_path / "t", "", {})
        write(root, "seal/__init__.py", "VERSION = 1\n")
        write(root, "seal/config.json", config_json())
        mark_root(os.path.join(root, "agentic-seal"))
        write(root, "agentic-seal/config.json", config_json(("Policy root", "policy")))
        write(root, "policy/README.md", INDEX.replace("docs/", "policy/"))
        write(root, "policy/g/x.md", "abc\n")
        assert sorted(report.documents(root)) == [
            "CLAUDE.md",
            "CONTRIBUTING.md",
            "policy/README.md",
            "policy/g/x.md",
            "skills/core/SKILL.md",
        ]


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


class Test_other_legs:
    def test_accepts_the_legs_past_the_three_by_system_then_version(self):
        """#1065: the legs at another Python follow `LEGS`' order, 3.9 before
        3.14 and a version with a letter after its number, and a system
        outside `LEGS`, at the floor, comes after every system of it."""
        at = {"macos 3.13": 1.0, "windows 3.13": 4.0, "freebsd": 2.0}
        now = {"ubuntu 3.14": 3.0, "ubuntu 3.14t": 1.0, "ubuntu 3.9": 3.0}
        assert report.other_legs(at, now) == [
            "ubuntu 3.9",
            "ubuntu 3.14",
            "ubuntu 3.14t",
            "windows 3.13",
            "macos 3.13",
            "freebsd",
        ]

    def test_refuses_a_floor_leg_the_three_rows_already_print(self):
        """#1065: a leg at the floor is one of the three rows, never a row
        past them."""
        legs = {"ubuntu": 2.0, "windows": 4.0, "macos": 1.0}
        assert report.other_legs(legs, {"ubuntu": 2.0}) == []


class Test_main:
    def test_accepts_the_file_rows_printed_under_the_release_table(
        self, tmp_path, monkeypatch, capsys
    ):
        monkeypatch.setattr(report, "meter", lambda: None)
        monkeypatch.setattr(report, "reading", lambda root, kernel, s: ({}, 1.0, {}))
        at, now = priced(tmp_path / "at.json", AT), priced(tmp_path / "now.json", NOW)
        argv = ["--against", "v0.0.1", "--at", str(tmp_path)]
        assert report.main([*argv, "--durations-at", at, "--durations", now]) == 0
        out = capsys.readouterr().out
        assert out.index("### Against v0.0.1") < out.index(
            "### Test files against v0.0.1"
        )
        assert (
            "| Test file | Cases at v0.0.1 | Seconds at v0.0.1 | Cases now | Seconds now |\n"
            "|---|---|---|---|---|\n"
            "| `tests/test_new.py` | — | — | 1 | 9.0 |\n"
        ) in out

    def test_a_job_at_another_python_is_a_leg_of_its_own(
        self, tmp_path, monkeypatch, capsys
    ):
        """#1065 S4: the `ubuntu` row reads the floor's job alone, and the
        3.14 job is a row of its own after the three, `no run found` at a tag
        whose run had none."""
        monkeypatch.setattr(report, "meter", lambda: None)
        monkeypatch.setattr(report, "reading", lambda root, kernel, s: ({}, 1.0, {}))
        floor = job("pytest (ubuntu-latest, 3.12, 15)", 2)
        jobs_at = jobs_file(tmp_path / "at.jsonl", [floor])
        jobs = jobs_file(
            tmp_path / "now.jsonl", [floor, job("pytest (ubuntu-latest, 3.14, 15)", 3)]
        )
        argv = ["--against", "v1", "--at", str(tmp_path), "--ci-jobs", jobs]
        assert report.main([*argv, "--ci-jobs-at", jobs_at]) == 0
        out = capsys.readouterr().out
        rows = rows_of(out)
        assert rows["`ubuntu` leg (minutes)"] == ("2.0", "2.0", "+0.0 (+0.0%)"), rows
        assert rows["`ubuntu 3.14` leg (minutes)"] == ("no run found", "3.0", "—")
        assert out.index("`macos` leg") < out.index("`ubuntu 3.14` leg"), out

    def test_refuses_to_print_rows_for_a_tree_it_cannot_read(self, tmp_path, capsys):
        now = tree(tmp_path / "now", "", {})
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
        at = tree(tmp_path / "at", "x" * 100, {"gone": "ab\n"})
        scout = "---\nname: scout\n---\n"
        (tmp_path / "at" / "agents" / "scout.md").write_text(
            scout, "utf-8", newline="\n"
        )
        now = tree(tmp_path / "now", "x" * 150, {"new": "abc\r\n"})
        unions = tmp_path / "unions"
        argv = [
            "--durations-at",
            priced(unions / "at.json", {"t::a": 1.0, "t::b": 2.0}),
            "--durations",
            priced(unions / "now.json", {"t::a": 1.0, "t::b": 3.0}),
        ]
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
            ["--against", "v1.2.3", "--at", at, "--root", now, "--ci-jobs", jobs, *argv]
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
        # The core left `CLAUDE.md` in #1177, so the report measures it where
        # it measured `CLAUDE.md`.
        assert rows["`skills/core/SKILL.md` (bytes)"] == ("11", "11", "+0 (+0.0%)")
        assert "`CONTRIBUTING.md` (bytes)" in rows, rows

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
        at = tree(tmp_path / "at", "", {})
        jobs = tmp_path / "jobs.jsonl"
        jobs.write_text(lines, "utf-8")
        argv = ["--against", "v1", "--at", at, "--root", at, "--ci-jobs", str(jobs)]
        assert report.main([*argv, "--ci-jobs-at", str(tmp_path / "absent")]) == 0
        rows = rows_of(capsys.readouterr().out)
        assert rows["`ubuntu` leg (minutes)"] == ("no run found", "no run found", "—")

    def test_no_union_on_either_side_reads_no_reading_and_exit_0(
        self, tmp_path, capsys
    ):
        """S5: a run whose `durations` job uploaded nothing, at a tag whose
        artifact has expired, still prints the table: the suite row reads
        `no union found` on both sides, and the test-file table is empty."""
        at = tree(tmp_path / "at", "", {})
        absent = str(tmp_path / "absent" / ".test_durations")
        argv = ["--against", "v1", "--at", at, "--root", at]
        assert report.main([*argv, "--durations", absent]) == 0
        out = capsys.readouterr().out
        rows = rows_of(out)
        assert rows["the suite (seconds)"] == (
            "no union found",
            "no union found",
            "—",
        ), rows
        assert out.endswith("|---|---|---|---|---|\n"), out

    def test_a_union_this_side_alone_reads_against_no_reading_at_the_tag(
        self, tmp_path, capsys
    ):
        """S5: the first release after the union left the tree, whose tag's
        push run uploaded none this script reads, prints this side's seconds
        beside `no union found` and no change, never a traceback."""
        at = tree(tmp_path / "at", "", {})
        now = priced(tmp_path / "unions" / "now.json", NOW)
        argv = ["--against", "v1", "--at", at, "--root", at, "--durations", now]
        assert report.main(argv) == 0
        out = capsys.readouterr().out
        assert rows_of(out)["the suite (seconds)"] == ("no union found", "10", "—")
        assert (
            "| `tests/test_new.py` | no union found | no union found | 1 | 9.0 |" in out
        ), out

    @pytest.mark.parametrize(
        "spoil, said",
        [
            ("no tree", "is no directory"),
            ("durations not json", "cannot be read"),
            ("durations not seconds", "is no object of case ids to seconds"),
            ("index not utf-8", "docs/README.md could not be read as text"),
        ],
    )
    def test_a_tree_that_cannot_be_read_is_exit_2(self, tmp_path, capsys, spoil, said):
        """Nothing was compared, so nothing is printed as if it had been. A
        union that is present and does not parse is such a file: it is no
        absent reading."""
        at = tree(tmp_path / "at", "", {})
        durations = priced(tmp_path / "unions" / "at.json", {"t::a": 1.0})
        if spoil == "no tree":
            at = str(tmp_path / "nowhere")
        elif spoil == "durations not json":
            with open(durations, "w", encoding="utf-8") as handle:
                handle.write("{")
        elif spoil == "index not utf-8":
            os.makedirs(os.path.join(at, "docs"))
            with open(os.path.join(at, "docs", "README.md"), "wb") as handle:
                handle.write(b"| \xff |\n")
        else:
            with open(durations, "w", encoding="utf-8") as handle:
                handle.write('{"t::a": "slow"}')
        root = tree(tmp_path / "now", "", {})
        argv = ["--against", "v1", "--at", at, "--root", root]
        assert report.main([*argv, "--durations-at", durations]) == 2
        captured = capsys.readouterr()
        assert captured.out == "", captured.out
        assert said in captured.err, captured.err
        assert "Nothing was compared." in captured.err, captured.err


test_census = census_case(TARGET)
