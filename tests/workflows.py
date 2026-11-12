"""The suite's one reading of a workflow file (#1486).

A case that reads a job, a step or a key of `.github/workflows/*.yml` or
`templates/setup/hygiene.yml` reads what `load` returns. The file is parsed
by PyYAML, pinned in `.github/scripts/run_tests.py#PYYAML`, so no case reads
a workflow's structure by indentation or by a regular expression over lines.

**`yaml.BaseLoader`, not `yaml.safe_load`.** PyYAML reads YAML 1.1, where a
bare `on` is a boolean, so `safe_load` returns the trigger key of every
workflow as `True`, and `15` as an integer. GitHub reads `on` as a key. The
base loader resolves no scalar: every value is a string as it is written,
`''` for an empty one, so the trigger key is `"on"` and a case compares
strings.

A parser drops comments, so a case whose subject is a comment reads it from
the file's text.

This module sits beside `tests/commonmark_oracle.py` and imports PyYAML at
its top, so a missing PyYAML fails the modules that import this one and
leaves `tests/conftest.py` importable.
"""

import os
import re

import yaml
from conftest import ROOT, code_lines


def load(path):
    """The mapping the workflow file at PATH parses to, every scalar a
    string. PATH is absolute, or relative to the repository root."""
    with open(os.path.join(ROOT, path), encoding="utf-8") as handle:
        return yaml.load(handle.read(), Loader=yaml.BaseLoader)


def job_scripts(job):
    """Each `run:` script of JOB's steps, with its shell comments off.

    The parser keeps a comment inside a script, where the shell does not run
    it, so each script's comments come off through `tests/conftest.py#code_line`.
    """
    return [
        "\n".join(code_lines(step["run"]))
        for step in job.get("steps", [])
        if "run" in step
    ]


# A job runs pytest where a line of one of its `run:` scripts names it as a
# word: `run: pytest …`, `uvx --with pytest pytest`, `uv run pytest`,
# `PYTHONPATH=x pytest`, `cd sub && pytest`, `python -m pytest`, a line of a
# `run: |` block. Only the scripts are read, so `needs: pytest`, which names
# the job of that name and runs nothing (the `durations` job and the
# `release-report` job, neither of which runs the suite), is not; a script's
# comments are off before a line is read.
RUNS_PYTEST = re.compile(r"(?<![\w.-])pytest(?:\s|$)")


def pytest_jobs(workflow):
    """{job name: job} for each job of a loaded WORKFLOW whose scripts run
    pytest, in the file's order. The suite's legs stand in more than one job
    (#1516), so a case that holds a property of every leg reads every job
    this returns rather than one job by its name."""
    return {
        name: job
        for name, job in workflow["jobs"].items()
        if any(
            RUNS_PYTEST.search(line)
            for script in job_scripts(job)
            for line in script.splitlines()
        )
    }
