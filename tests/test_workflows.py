"""`tests/workflows.py`'s own cases (#1486).

`load` is the suite's one reading of a workflow file, and the cases that
read a job, a step or a key compare what it returns with strings. So the
loader's two properties are pinned here over a fixture: the trigger key
comes back as the key `on`, and every scalar comes back as a string. A
path is read from the repository root, wherever pytest runs, and a path
that names no file fails rather than reading as an empty workflow.

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


# Three jobs a workflow runs the suite from, each a way a job here calls
# pytest, and two that name it and run nothing: `needs:` names a job, and
# a shell comment is not run.
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
        so a leg moved into a job of another name is still read (#1516)."""
        path = tmp_path / "fixture.yml"
        path.write_text(SUITE_JOBS, encoding="utf-8")
        loaded = workflows.load(str(path))
        found = workflows.pytest_jobs(loaded)
        assert list(found) == ["first", "second"], list(found)
        assert found["second"] is loaded["jobs"]["second"]

    def test_refuses_a_job_that_names_pytest_and_runs_nothing(self, tmp_path):
        path = tmp_path / "fixture.yml"
        path.write_text(SUITE_JOBS, encoding="utf-8")
        found = workflows.pytest_jobs(workflows.load(str(path)))
        assert "reads-a-part" not in found and "comments-on-it" not in found, found


test_census = census_case(TARGET)
