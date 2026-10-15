"""The release table sets the release beside the last release tag, and fails
nothing.

#923 item 3: what a release reads release to release is one table on the
release pull request — each agent's preload bytes, the suite's seconds, each
CI leg's minutes and each document's bytes, at the tag and now — and no row
is held to a number. `.github/scripts/release_report.py` prints it; the
tests workflow's `release-report` job runs it after the suite, on a pull
request into `main` only. There is no group of cases for a script that did
not exist, so this module is that group.
"""

import importlib.util
import json
import os
import re

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, ".github", "scripts", "release_report.py")
WORKFLOW = os.path.join(ROOT, ".github", "workflows", "test.yml")


def _load():
    spec = importlib.util.spec_from_file_location("specseal_release_report", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


report = _load()

AGENT = "---\nname: warden\nskills:\n  - review\n---\n"


def tree(root, agent_body, durations, docs):
    """A tree holding one agent and its one skill, `.test_durations` as
    `durations`, `CLAUDE.md`, `CONTRIBUTING.md` and `docs/<name>.md` for each
    of `docs`; returns its path as text."""
    files = {
        "agents/warden.md": AGENT + agent_body,
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


def test_the_release_table_reads_two_trees_and_fails_nothing(tmp_path, capsys):
    """S9: a grown preload, an agent and a document on one side only and a
    leg with no run at the tag are each a row, and the exit is 0 whatever
    they show: the tag's tree and this one side by side, each leg's minutes
    summed over its pytest jobs, `no run found` where a run has no job
    list."""
    at = tree(tmp_path / "at", "x" * 100, {"t::a": 1.0, "t::b": 2.0}, {"gone": "ab\n"})
    scout = "---\nname: scout\n---\n"
    (tmp_path / "at" / "agents" / "scout.md").write_text(scout, "utf-8", newline="\n")
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
    assert rows["preload `warden` (bytes)"] == (
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
def test_a_job_list_that_holds_no_run_reads_no_run_found(tmp_path, capsys, lines):
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
def test_a_tree_that_cannot_be_read_is_exit_2(tmp_path, capsys, spoil, said):
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


def test_the_table_reads_this_tree_against_the_last_tag():
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
    agents = sorted(f[: -len(".md")] for f in os.listdir(os.path.join(ROOT, "agents")))
    for agent in agents:
        assert found[f"preload `{agent}` (bytes)"][2] == "+0 (+0.0%)", agent
    docs = [f for f in os.listdir(os.path.join(ROOT, "docs")) if f.endswith(".md")]
    for name in docs:
        assert f"`docs/{name}` (bytes)" in found, name
    assert sum(1 for k in found if k.endswith("leg (minutes)")) == 3, found


def job_block(text, name):
    """The lines of one job of a workflow, its header through the next job."""
    found = re.search(rf"(?ms)^  {re.escape(name)}:\n(.*?)(?=^  \S|\Z)", text)
    assert found, f"no job `{name}` in the workflow"
    return found.group(1)


def test_the_tests_workflow_prints_the_table_only_into_main_after_the_suite():
    """S9's job: after the suite whatever its verdict, on a pull request into
    `main` alone, with the whole history to find the tag in, and its output
    appended to the step summary. No `budgets` job is left."""
    with open(WORKFLOW, encoding="utf-8") as handle:
        text = handle.read()
    code = "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )
    block = job_block(code, "release-report")
    assert "needs: pytest" in block, block
    assert "if: ${{ !cancelled() && github.base_ref == 'main' }}" in block, block
    assert "fetch-depth: 0" in block, block
    assert "python .github/scripts/release_report.py" in block, block
    assert '>> "$GITHUB_STEP_SUMMARY"' in block, block
    assert not re.search(r"(?m)^  budgets:", code), "the budgets job is still there"
