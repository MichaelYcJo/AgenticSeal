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
import re
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


# A job that runs the test suite, for the cases that vary only the trigger.
PYTEST_JOB = "jobs:\n  t:\n    steps:\n      - run: pytest\n"


def labelled(out, label):
    """The lines of the command's output that open with LABEL, such as
    `answers`, `too late` or `unread`."""
    return [line for line in out.split("\n") if line.startswith(f"  {label} ")]


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

    # --- the trigger is read, or reported unread and not counted --------------

    @pytest.mark.parametrize(
        "trigger",
        [
            '"on":\n  push:\n    branches: [main]\n',
            "on:\n    push:\n        branches: [main]\n",
            "'on':\n  push:\n    branches: [main]\n",
            "on:\n- push\n",
            "on:\n  push: {branches: [main]}\n",
            "on:\n  push: # on main\n    branches: [main]\n",
        ],
        ids=[
            "double-quoted-key",
            "block-at-four-spaces",
            "single-quoted-key",
            "sequence-at-indent-zero",
            "key-with-a-value",
            "key-with-a-comment",
        ],
    )
    def test_a_push_only_trigger_in_each_spelling_is_too_late(self, repo, trigger):
        """#1123: each spelling read as unread and counted as answering."""
        workflow(repo, "post.yml", trigger + PYTEST_JOB)
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 1, r.stdout + r.stderr
        [line] = labelled(r.stdout, "too late")
        assert "post.yml (on push, not pull_request)" in line

    @pytest.mark.parametrize(
        "trigger",
        [
            '"on":\n  pull_request:\n',
            "on:\n    pull_request:\n        types: [opened]\n",
            'on: ["pull_request"]\n',
            "on:\n  - pull_request # the run\n",
            "on: [pull_request, ]\n",
            "on:\n  pull_request\n",
            "on:\n  pull_request\n    # the run\n",
            "on: pull_request\n  # the run\n",
        ],
        ids=[
            "double-quoted-key",
            "block-at-four-spaces",
            "quoted-name",
            "item-with-a-comment",
            "flow-list-trailing-comma",
            "name-on-the-line-below",
            "name-with-a-comment-below",
            "inline-name-with-a-comment-below",
        ],
    )
    def test_a_pull_request_trigger_in_the_wider_spellings_answers(self, repo, trigger):
        workflow(repo, "test.yml", trigger + PYTEST_JOB)
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        [line] = labelled(r.stdout, "answers")
        assert "test.yml (on pull_request)" in line

    @pytest.mark.parametrize(
        "trigger",
        [
            "name: CI\n",
            "on: {pull_request: {}}\n",
            "on: [\n  push\n]\n",
            "on: [pull_request,\n    push]\n",
            "on: [pull_request, {types: [opened]}]\n",
            "on:\n  pull_request:\n  ? push\n",
            "on:\n    pull_request:\n  push:\n",
            "on: [pull_request,,]\n",
            "on:\n  pull_request\n  push\n",
            "on:\n  pull_request\n    push\n",
            "on:\n  - pull_request\n    closed\n",
            "on: pull_request\n  push\n",
            "on: [pull_request]\n  push\n",
            "on:\n  pull_request:foo\n",
            "on:\n  pull_request:foo\n    push\n",
            "on:pull_request\n",
        ],
        ids=[
            "no-on-key",
            "flow-mapping",
            "flow-list-across-lines",
            "flow-list-closed-on-a-later-line",
            "one-list-element-unread",
            "one-block-entry-unread",
            "a-line-shallower-than-the-block",
            "two-trailing-commas",
            "two-names-on-the-lines-below",
            "a-name-continued-on-a-deeper-line",
            "an-item-continued-on-a-deeper-line",
            "an-inline-name-continued-on-a-deeper-line",
            "an-inline-list-continued-on-a-deeper-line",
            "a-name-glued-to-a-colon",
            "a-glued-name-continued-on-a-deeper-line",
            "an-on-key-glued-to-its-value",
        ],
    )
    def test_an_unread_trigger_is_reported_and_not_counted(self, repo, trigger):
        """One element the scan cannot read makes the whole trigger unread:
        a partial set would read as the whole trigger."""
        workflow(repo, "ci.yml", trigger + PYTEST_JOB)
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 1, r.stdout + r.stderr
        assert labelled(r.stdout, "answers") == [], r.stdout
        [line] = labelled(r.stdout, "unread")
        assert "ci.yml (trigger unread, not counted) — pytest" in line

    def test_an_unread_workflow_beside_one_that_answers_still_resolves(self, repo):
        workflow(repo, "nightly.yml", "name: Nightly\n" + PYTEST_JOB)
        workflow(repo, "test.yml", "on: pull_request\n" + PYTEST_JOB)
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        [answers] = labelled(r.stdout, "answers")
        assert "test.yml (on pull_request)" in answers
        [unread] = labelled(r.stdout, "unread")
        assert "nightly.yml (trigger unread, not counted)" in unread

    @pytest.mark.parametrize(
        "trigger, code, label, events",
        [
            ("on: pull_request # trigger\n", 0, "answers", "pull_request"),
            ("on: [push] # trigger\n", 1, "too late", "push"),
        ],
        ids=["inline-name", "inline-list"],
    )
    def test_a_trailing_comment_is_not_read_as_an_event(
        self, repo, trigger, code, label, events
    ):
        workflow(repo, "ci.yml", trigger + PYTEST_JOB)
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == code, r.stdout + r.stderr
        [line] = labelled(r.stdout, label)
        read = re.search(r"\(on (.*?)(?:, not pull_request)?\) —", line)
        assert read and read.group(1) == events, line

    def test_the_printed_limit_names_a_trigger_it_cannot_read(self, tmp_path):
        r = run(["--kind", "tests", str(tmp_path)])
        [limit] = [line for line in r.stdout.split("\n") if line.startswith("limit: ")]
        assert "flow mapping" in limit, limit
        assert "unread and is not counted" in limit, limit
        assert "filters (types, branches, paths) are not read" in limit, limit

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
