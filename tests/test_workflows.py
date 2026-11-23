"""`tests/workflows.py`'s own cases (#1486).

`load` is the suite's one reading of a workflow file and of an eval case's
`case.yaml`, and `front_matter` of a grader's fields; both parse through
`parse`, and the cases that read a job, a step or a key compare what they
return with strings. So the loader's two properties are pinned here over a
fixture: the trigger key comes back as the key `on`, and every scalar comes
back as a string. A path is read from the repository root, wherever pytest
runs, and a path that names no file fails rather than reading as an empty
workflow. A front matter ends at its second `---` line, and a text that
does not open and close one fails.

Seen red before it was committed (contract rule 15): with `yaml.SafeLoader`
in place of `yaml.BaseLoader`, the fixture's `on` came back as the key
`True` and its `timeout-minutes` as the integer 15.
"""

import os

import pytest
import workflows
from conftest import census_case

TARGET = "tests/workflows.py"

FIXTURE = """\
name: fixture
on:
  pull_request:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    strategy:
      matrix:
        python: ['3.12', 3.14]
    steps:
      - if: true
        run: echo yes
"""


class Test_load:
    def test_accepts_a_workflow_and_keeps_on_as_the_key_and_every_scalar_a_string(
        self, tmp_path
    ):
        """YAML 1.1 reads a bare `on`, `true` and `15` as a boolean, a
        boolean and an integer. A workflow case compares strings, and GitHub
        reads `on` as the trigger key, so the loader keeps every scalar as it
        is written."""
        path = tmp_path / "fixture.yml"
        path.write_text(FIXTURE, encoding="utf-8")
        loaded = workflows.load(str(path))
        assert "on" in loaded and True not in loaded, list(loaded)
        assert loaded["on"] == {"pull_request": "", "push": {"branches": ["main"]}}
        job = loaded["jobs"]["build"]
        assert job["timeout-minutes"] == "15", job
        assert job["strategy"]["matrix"]["python"] == ["3.12", "3.14"], job
        assert job["steps"] == [{"if": "true", "run": "echo yes"}], job

    def test_accepts_a_path_relative_to_the_repository_root(
        self, tmp_path, monkeypatch
    ):
        """The cases name a workflow by its path in the repository, and
        pytest may run from any directory."""
        monkeypatch.chdir(tmp_path)
        loaded = workflows.load(os.path.join(".github", "workflows", "test.yml"))
        assert loaded["name"] == "tests", loaded["name"]
        assert "on" in loaded and True not in loaded, list(loaded)

    def test_refuses_a_path_that_names_no_file(self, tmp_path):
        """A mistyped path fails the case that names it, so no case reads an
        empty workflow and passes over nothing."""
        with pytest.raises(FileNotFoundError):
            workflows.load(str(tmp_path / "missing.yml"))


# A grader's front matter as `evals/scripts/behaviour.py#grader` writes it: a
# flow map, a single-quoted scalar with a quote doubled inside, and a bound.
GRADER = "type: 'tool_used'\ntarget: {source: 'file', path: 'it''s, {a}.md'}\nmax: 0\n"


class Test_parse:
    def test_accepts_a_graders_fields_and_keeps_every_scalar_a_string(self):
        """An eval case and a grader are read by the parser `load` uses, so a
        bound such as `max: 0` comes back as the string a case compares, and
        a quoted path keeps the comma and the braces it holds."""
        assert workflows.parse(GRADER) == {
            "type": "tool_used",
            "target": {"source": "file", "path": "it's, {a}.md"},
            "max": "0",
        }


class Test_front_matter:
    def test_accepts_the_lines_between_the_first_two_rules_and_leaves_the_body_out(
        self,
    ):
        """The front matter ends at the first line that is `---` alone, so a
        pattern holding `---` stays whole, and a body that reads like a field
        is not one."""
        text = f"---\n{GRADER}pattern: 'a---b'\n---\nbody: not a field\n---\n"
        fields = workflows.front_matter(text)
        assert fields == {**workflows.parse(GRADER), "pattern": "a---b"}, fields

    @pytest.mark.parametrize(
        "text",
        ["A defect.\n", "type: 'regex'\n---\nA defect.\n", "---\ntype: 'regex'\n"],
        ids=["no rule", "no opening rule", "no closing rule"],
    )
    def test_refuses_a_text_whose_front_matter_does_not_open_and_close(self, text):
        """A grader file with no front matter fails the case that reads it,
        rather than reading as a grader with no fields."""
        with pytest.raises(ValueError, match=r"^no front matter"):
            workflows.front_matter(text)


# Two jobs that run the suite, each in a way a job here calls pytest, and
# two that name it and run nothing: `needs:` names a job, and a shell
# comment is not run.
SUITE_JOBS = """\
on: push
jobs:
  first:
    steps:
      - run: pytest tests/ -q
  reads-a-part:
    needs: first
    steps:
      - run: echo needs-names-a-job
  second:
    steps:
      - run: |
          git config --global user.name ci
          python -m pytest tests/ -q
  comments-on-it:
    needs: pytest
    steps:
      - run: echo a-comment-runs-nothing  # pytest -q
"""


class Test_pytest_jobs:
    def test_accepts_each_job_whose_script_runs_pytest_in_the_file_s_order(
        self, tmp_path
    ):
        """The jobs that run the suite are read by what their scripts run,
        so a leg moved into a job of another name is still read (#1516), and
        a job that names pytest in `needs:` or in a shell comment is not."""
        path = tmp_path / "fixture.yml"
        path.write_text(SUITE_JOBS, encoding="utf-8")
        loaded = workflows.load(str(path))
        found = workflows.pytest_jobs(loaded)
        assert list(found) == ["first", "second"], list(found)
        assert found["second"] is loaded["jobs"]["second"]

    def test_refuses_a_job_whose_script_names_a_plugin_or_a_file_of_pytest(
        self, tmp_path
    ):
        """`pytest` is read as a word: a plugin installed by its package
        name, the config file and the cache directory run no suite. The
        install line of `test.yml` names `pytest-split`, and an install line
        may name `pytest-xdist` too, so a substring reading would select a
        job that only installs them."""
        path = tmp_path / "fixture.yml"
        path.write_text(
            "on: push\n"
            "jobs:\n"
            "  installs:\n"
            "    steps:\n"
            "      - run: pip install pytest-xdist pytest-split==0.11.0 allure-pytest\n"
            "      - run: |\n"
            "          cat pytest.ini\n"
            "          rm -rf .pytest_cache\n",
            encoding="utf-8",
        )
        assert workflows.pytest_jobs(workflows.load(str(path))) == {}


test_census = census_case(TARGET)
