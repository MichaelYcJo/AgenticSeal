"""seal deferrals: does anything other than this session actually run the
check being deferred?

The failure this exists for: a session narrowed its run to one domain and
wrote "the rest is CI's job". The repository had three workflows — reviewer
assignment, deploy on push to the default branch, and a migration-graph check
— and not one of them ran the test suite. The named answerer did not exist,
so the `unverified` row was a loophole wearing condition 4's clothes.

The tool reads command lines and no trigger: it names each CI file holding a
runner, and whether that file runs before the change merges is its reader's
to open (#1167). No case here asserts an event the tool read.

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


# A job that runs the test suite, for the cases that vary only the trigger.
PYTEST_JOB = "jobs:\n  t:\n    steps:\n      - run: pytest\n"

# The path a workflow is printed under, in the platform's separator.
TEST_YML = os.path.join(".github", "workflows", "test.yml")

LIMIT = (
    "limit: reads command text, not a YAML graph: a runner reached through "
    "a composite action, a reusable workflow, or a script this cannot see "
    "reads as absent; no trigger is read, so a file named here may run only "
    "after the change merges"
)
TRIGGER = (
    "  trigger   not read: open each ci file above for whether it runs "
    "before the change merges"
)
UNANSWERED = (
    "Deferring tests to CI names an answerer that is not there. "
    "Run it, or say it is unanswered."
)


def answered(*ci):
    """The whole output for `--kind tests` where CI holds a runner: one
    `ci` line per (file, commands) pair given, then the trigger line."""
    lines = ["tests: a runner in CI"]
    lines += [f"  ci        {name} — {cmds}" for name, cmds in ci]
    return "\n".join([*lines, TRIGGER, "", LIMIT, ""])


class Test_main:
    # --- a CI file holds a runner ---------------------------------------------

    def test_accepts_a_workflow_holding_a_runner_and_leaves_its_trigger_to_the_reader(
        self, repo
    ):
        workflow(
            repo,
            "test.yml",
            "name: Test\non: pull_request\njobs:\n"
            "  t:\n    steps:\n      - run: uv run pytest\n",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        assert r.stdout == answered((TEST_YML, "uv run pytest")), r.stdout

    @pytest.mark.parametrize(
        "trigger",
        [
            "on:\n\tpull_request:\n",
            "on: push # a\u2028b\n",
            "on:\n  push:\n    branches: [main]\n",
            "on: {pull_request: {}}\n",
            "name: Test\n",
        ],
        ids=[
            "a-block-indented-by-a-tab",
            "a-line-separator-in-a-comment",
            "a-push-only-block",
            "a-flow-mapping",
            "no-on-key",
        ],
    )
    def test_the_output_is_the_same_whatever_the_trigger(self, repo, trigger):
        """#1167: the owner's two misreadings, a tab-indented `on:` block
        and U+2028 inside a comment, and every other trigger, read as one:
        the file named, its runner line, and the trigger left unread."""
        workflow(repo, "test.yml", trigger + PYTEST_JOB)
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        assert r.stdout == answered((TEST_YML, "pytest")), r.stdout

    @pytest.mark.parametrize(
        "char",
        ["\u2028", "\u2029", "\x85", "\x0b", "\x0c", "\x1c", "\x1d", "\x1e"],
        ids=[
            "U+2028",
            "U+2029",
            "U+0085",
            "U+000B",
            "U+000C",
            "U+001C",
            "U+001D",
            "U+001E",
        ],
    )
    def test_a_step_is_printed_whole_where_a_comment_holds_a_break_yaml_does_not_take(
        self, repo, char
    ):
        """#1167's second misreading: `str.splitlines` ends a line at eight
        characters YAML 1.2 does not, which printed a word from a comment as
        a command of its own. The step is printed as the line it is, comment
        and all, for its reader."""
        step = f"./deploy.sh # see{char}pytest"
        workflow(
            repo,
            "test.yml",
            "on: pull_request\njobs:\n  d:\n    steps:\n      - run: " + step + "\n",
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        assert r.stdout == answered((TEST_YML, step)), r.stdout

    @pytest.mark.parametrize("end", ["\r\n", "\r"], ids=["CRLF", "CR"])
    def test_a_line_ends_at_each_of_yamls_line_breaks(self, repo, end):
        (repo / ".github" / "workflows" / "test.yml").write_bytes(
            end.join(["on: pull_request", *PYTEST_JOB.splitlines(), ""]).encode()
        )
        r = run(["--kind", "tests", str(repo)])
        assert r.returncode == 0, r.stdout + r.stderr
        assert r.stdout == answered((TEST_YML, "pytest")), r.stdout

    # --- the answerer is missing ---------------------------------------------

    def test_refuses_a_tree_with_no_ci_as_an_answerer(self, tmp_path):
        d = tmp_path / "bare"
        d.mkdir()
        r = run(["--kind", "tests", str(d)])
        assert r.returncode == 1
        assert "nothing" in r.stdout.lower()
        assert r.stdout == "\n".join(
            [
                "tests: NO RUNNER IN CI",
                "  nothing runs it",
                "",
                LIMIT,
                "",
                UNANSWERED,
                "",
            ]
        ), r.stdout

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
        assert "assign.yml" not in r.stdout, r.stdout
        assert "deploy.yml" not in r.stdout, r.stdout

    def test_the_printed_limit_says_no_trigger_is_read(self, tmp_path):
        r = run(["--kind", "tests", str(tmp_path)])
        [limit] = [line for line in r.stdout.split("\n") if line.startswith("limit: ")]
        assert limit == LIMIT, limit

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
        assert r.stdout == "\n".join(
            [
                "tests: NO RUNNER IN CI",
                "  local     .pre-commit-config.yaml (the committer's machine "
                "only) — pytest",
                "",
                LIMIT,
                "",
                UNANSWERED,
                "",
            ]
        ), r.stdout

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
        assert r.stdout == answered((".gitlab-ci.yml", "pytest -q")), r.stdout

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
