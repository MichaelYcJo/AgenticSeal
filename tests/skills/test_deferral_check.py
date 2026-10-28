"""seal deferrals: does anything other than this session actually run the
check being deferred?

The failure this exists for: a session narrowed its run to one domain and
wrote "the rest is CI's job". The repository had three workflows — reviewer
assignment, deploy on push to the default branch, and a migration-graph check
— and not one of them ran the test suite. The named answerer did not exist,
so the `unverified` row was a loophole wearing condition 4's clothes.

Every case runs the command, so each sits in `Test_main`, and the launcher's
case in `Test_module`. #942's phase 6 placed them in classes.
"""

import os
import subprocess
import sys

import pytest
from conftest import ROOT, census_case

TARGET = "skills/verify/scripts/deferral_check.py"

SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "deferral_check.py")


def run(args, cwd=None):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        cwd=cwd,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


@pytest.fixture
def repo(tmp_path):
    """A bare project directory; each test writes the CI it wants to assert on."""
    d = tmp_path / "proj"
    (d / ".github" / "workflows").mkdir(parents=True)
    return d


def workflow(repo, name, text):
    (repo / ".github" / "workflows" / name).write_text(text, encoding="utf-8")


class Test_main:
    # --- the answerer exists -------------------------------------------------

    def test_accepts_pytest_on_a_pull_request_as_the_answerer(self, repo):
        workflow(
            repo,
            "test.yml",
            "name: Test\non: pull_request\njobs:\n"
            "  t:\n    steps:\n      - run: uv run pytest\n",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        assert "test.yml" in r.stdout
        assert "pytest" in r.stdout

    def test_inline_event_list_is_read(self, repo):
        workflow(
            repo,
            "ci.yml",
            "on: [push, pull_request]\njobs:\n  t:\n    steps:\n      - run: make test\n",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        assert "make test" in r.stdout

    # --- the answerer is missing ---------------------------------------------

    def test_refuses_a_tree_with_no_ci_as_an_answerer(self, tmp_path):
        d = tmp_path / "bare"
        d.mkdir()
        r = run(["--kind", "tests", str(d)])
        assert r.returncode == 1
        assert "nothing" in r.stdout.lower()

    def test_workflows_that_run_no_tests_do_not_resolve(self, repo):
        """The measured shape: three workflows, none of them a test run."""
        workflow(
            repo,
            "assign.yml",
            "on:\n  pull_request:\n    types: [opened]\njobs:\n"
            "  a:\n    steps:\n      - uses: actions/github-script@v7\n",
        )
        workflow(
            repo,
            "deploy.yml",
            "on:\n  push:\n    branches: [main]\njobs:\n"
            "  d:\n    steps:\n      - run: ./deploy.sh\n",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 1
        assert "assign.yml" not in r.stdout or "no runner" in r.stdout.lower()

    def test_runner_on_wrong_trigger_is_named_not_counted(self, repo):
        """A suite that only runs after merge cannot answer a deferral made before it."""
        workflow(
            repo,
            "post.yml",
            "on:\n  push:\n    branches: [main]\njobs:\n"
            "  t:\n    steps:\n      - run: pytest\n",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 1
        assert "post.yml" in r.stdout
        assert "pull_request" in r.stdout

    # --- a local hook is not CI ----------------------------------------------

    def test_pre_commit_is_reported_but_does_not_resolve(self, repo):
        (repo / ".pre-commit-config.yaml").write_text(
            "repos:\n  - repo: local\n    hooks:\n      - id: t\n        entry: pytest\n",
            encoding="utf-8",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 1
        assert "pre-commit" in r.stdout
        assert "local" in r.stdout.lower()

    # --- other CI systems ----------------------------------------------------

    def test_gitlab_ci_is_read(self, tmp_path):
        d = tmp_path / "gl"
        d.mkdir()
        (d / ".gitlab-ci.yml").write_text(
            "test:\n  script:\n    - pytest -q\n", encoding="utf-8"
        )
        r = run(["--kind", "tests", str(d)])
        assert r.returncode == 0, r.stdout + r.stderr
        assert ".gitlab-ci.yml" in r.stdout

    # --- kinds are independent -----------------------------------------------

    def test_lint_resolves_while_tests_do_not(self, repo):
        workflow(
            repo,
            "lint.yml",
            "on: pull_request\njobs:\n  l:\n    steps:\n      - run: ruff check .\n",
        )
        assert run(["--kind", "lint", str(repo)]).returncode == 0
        assert run(["--kind", "tests", str(repo)]).returncode == 1

    def test_all_kinds_needs_every_kind(self, repo):
        workflow(
            repo,
            "lint.yml",
            "on: pull_request\njobs:\n  l:\n    steps:\n      - run: ruff check .\n",
        )
        r = run(["--kind", "all", str(repo)])
        assert r.returncode == 1
        assert "tests" in r.stdout

    # --- usage ---------------------------------------------------------------

    def test_missing_path_exits_two(self, tmp_path):
        # Asserts on the message too: a missing *script* also exits 2, which would
        # make this the one test in the file that passes before anything is built.
        r = run(["--kind", "tests", str(tmp_path / "nope")])
        assert r.returncode == 2
        assert "no such path" in (r.stdout + r.stderr).lower()


class Test_module:
    @pytest.mark.skipif(
        os.name == "nt", reason="the POSIX command; bin/seal.cmd is its Windows twin"
    )
    def test_the_command_is_present_and_runs_the_script(self):
        wrapper = os.path.join(ROOT, "bin", "seal")
        assert os.path.isfile(wrapper), "bin/seal missing"
        assert os.access(wrapper, os.X_OK), "bin/seal not executable"
        done = subprocess.run(
            [wrapper, "deferrals", "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert done.returncode == 0, done.stderr
        assert done.stdout.startswith("usage: seal deferrals"), done.stdout


test_census = census_case(TARGET)
