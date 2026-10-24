"""`tests/conftest.py`'s own cases (#841, #942).

A case whose call runs past `SLOW_CASE_S` is named in the run's terminal
summary with its seconds, and nothing fails for it: a time reading is noisy,
and on 2026-10-16 a loaded machine failed a guarantor's run on time alone.
The summary hook is driven through one inner pytest run, built once for the
module, that loads this repository's `conftest.py` with the value lowered
so the run takes a second.

The workflow readers, `code_line`, `workflow_steps`, `workflow_step` and
`step_running`, are driven over one fixture workflow, and the block that
takes `gh`'s login away at import is read from a child process and asked of
`gh` itself. Those cases came from two files of their own in #942's phase 7.
The cases of `on_disk`, `shrunken_corpus`, `decline_if_shrunken` and
`build_tracked_tree` came from `tests/test_a_shrunken_corpus_declines_to_judge.py`
in #942's round 3 fix pass, and that file keeps its sweep across files.
`names_path`'s Windows case came from `tests/test_a_script_copied_alone_exits_2.py`
and `posix_id`'s from
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` in #942's
round 9 fix pass, each a case of one helper of this module.

Seen red before they were committed (contract rule 15): the three accepting
cases failed against the conftest that still held the failing ceiling, which
had neither `SLOW_CASE_S` nor a summary hook, and `mutation-check` turned
each refusing case red by breaking the condition it pins.
"""

import json
import ntpath
import os
import shutil
import subprocess
import sys
import types

import censuses
import conftest
import pytest
from conftest import (
    build_tracked_tree,
    code_line,
    decline_if_shrunken,
    names_path,
    on_disk,
    posix_id,
    shrunken_corpus,
    step_running,
    workflow_step,
    workflow_steps,
)

TARGET = "tests/conftest.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HERE = os.path.dirname(os.path.abspath(__file__))
CONFTEST = os.path.join(HERE, "conftest.py")
TOKENS = ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN", "GITHUB_ENTERPRISE_TOKEN")

# Pinned verbatim: the conftest's placeholder, which is not a credential.
NOT_A_GH_TOKEN = "specseal-suite-runs-with-gh-logged-out"

# Run the conftest's import-time code in a child whose environment carries
# every token and a config directory of its own, and report what is left.
PROBE = f"""
import json, os, runpy
runpy.run_path({CONFTEST!r})
home = os.environ.get("GH_CONFIG_DIR")
print(json.dumps({{
    "tokens": {{n: os.environ[n] for n in {TOKENS!r} if n in os.environ}},
    "home": home,
    "empty": bool(home) and os.path.isdir(home) and not os.listdir(home),
}}))
"""

# The workflow readers' fixture (#482, #462): a comment naming the script
# above an unrelated step, the real step below it, a step with no name, a
# quoted name and a second job. No YAML parser is installed where this suite
# runs, so every case that reads `.github/workflows/*.yml` reads text through
# `code_line`, `workflow_steps`, `workflow_step` and `step_running`, driven
# here over this fixture. Neutral values only
# (`CONTRIBUTING.md` *House rules*, *No real identifiers*).
WORKFLOW = """\
jobs:
  release:
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # the base is diffed

      # The step below runs correction_check.py, and this comment is not it.
      - name: an unrelated step
        run: echo unrelated

      - name: "the real step"
        shell: bash
        run: |
          if [ "${{ github.base_ref }}" = "main" ]; then
            echo "skipped"; exit 0
          fi

          python3 correction_check.py --range "x...HEAD"  # the range
  other:
    steps:
      - name: a step of another job
        run: echo other
"""

INNER_CONFTEST = """\
import importlib.util

_spec = importlib.util.spec_from_file_location("repo_conftest", {path!r})
_repo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_repo)
_repo.SLOW_CASE_S = 0.3
pytest_terminal_summary = _repo.pytest_terminal_summary
"""

INNER_TESTS = """\
import time


def test_slow():
    time.sleep(0.6)


def test_slow_and_failing():
    time.sleep(0.6)
    assert False, "its own failure"


def test_quick():
    pass
"""


@pytest.fixture(scope="module")
def inner_run(tmp_path_factory):
    """One pytest run over a slow case and a quick one, `SLOW_CASE_S` at
    0.3 s; its exit code and its output."""
    d = tmp_path_factory.mktemp("slow-case")
    path = os.path.join(ROOT, TARGET)
    (d / "conftest.py").write_text(INNER_CONFTEST.format(path=path), encoding="utf-8")
    (d / "test_inner.py").write_text(INNER_TESTS, encoding="utf-8")
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
        cwd=d,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    return run.returncode, run.stdout + run.stderr


def call(nodeid, seconds, when="call"):
    """A report as `slow_lines` reads one."""
    return types.SimpleNamespace(nodeid=nodeid, duration=seconds, when=when)


class Test_slow_lines:
    def test_accepts_a_call_past_the_value_named_with_its_seconds(self, monkeypatch):
        monkeypatch.setattr(conftest, "SLOW_CASE_S", 90)
        reports = [
            call("tests/test_x.py::test_y", 91.24),
            call("tests/test_x.py::test_z", 300),
        ]
        assert conftest.slow_lines(reports) == [
            "slow case: tests/test_x.py::test_z ran 300.0 s, past SLOW_CASE_S of 90 s",
            "slow case: tests/test_x.py::test_y ran 91.2 s, past SLOW_CASE_S of 90 s",
        ]

    def test_refuses_a_call_at_the_value_and_a_setup_past_it(self, monkeypatch):
        monkeypatch.setattr(conftest, "SLOW_CASE_S", 90)
        reports = [
            call("tests/test_x.py::test_y", 90),
            call("tests/test_x.py::test_z", 200, "setup"),
        ]
        assert conftest.slow_lines(reports) == []


class Test_pytest_terminal_summary:
    def test_accepts_a_slow_case_named_and_failing_nothing(self, inner_run):
        code, out = inner_run
        assert code == 1, out
        assert "1 failed, 2 passed" in out, out
        assert "its own failure" in out, out
        assert "slow case: test_inner.py::test_slow ran " in out, out
        assert "slow case: test_inner.py::test_slow_and_failing ran " in out, out

    def test_refuses_to_name_a_quick_case(self, inner_run):
        _, out = inner_run
        assert "test_quick ran" not in out, out


class Test_on_disk:
    def test_accepts_a_listing_split_by_what_the_tree_actually_has(self, tmp_path):
        root = build_tracked_tree(
            tmp_path / "r",
            {"a.md": "one\n", "b/c.md": "two\n", "d.md": "three\n"},
            deleted=["b/c.md"],
        )
        present, missing = on_disk(root, ["a.md", "b/c.md", "d.md"])
        assert present == ["a.md", "d.md"]
        assert missing == ["b/c.md"]

    def test_accepts_the_order_it_was_given(self, tmp_path):
        """A corpus is walked in the order git listed it, and a refusal naming
        `rel:line` is read against that order."""
        root = build_tracked_tree(tmp_path / "r", {"a.md": "", "b.md": "", "c.md": ""})
        present, missing = on_disk(root, ["c.md", "a.md", "b.md"])
        assert present == ["c.md", "a.md", "b.md"]
        assert missing == []

    def test_refuses_a_directory_on_the_list_as_a_file_that_is_there(self, tmp_path):
        """`os.path.isfile` rather than `os.path.exists`: a path git named that
        is now a directory has no content to read, and `open` would raise on it
        exactly the way a missing file does."""
        root = build_tracked_tree(tmp_path / "r", {"a.md": "one\n"})
        os.mkdir(os.path.join(root, "b"))
        present, missing = on_disk(root, ["a.md", "b"])
        assert present == ["a.md"] and missing == ["b"]


class Test_decline_if_shrunken:
    def test_accepts_a_missing_path_and_raises_the_skip_carrying_that_reason(self):
        with pytest.raises(pytest.skip.Exception) as declined:
            decline_if_shrunken(["docs/one.md"], "the KEEP allowlist's liveness check")
        assert str(declined.value) == shrunken_corpus(
            ["docs/one.md"], "the KEEP allowlist's liveness check"
        )

    def test_refuses_to_decline_when_nothing_is_missing(self):
        """The guard must not turn a check off on a whole tree, which is the one
        way this repair could report less than the crash it replaces."""
        assert decline_if_shrunken([], "x") is None


class Test_module:
    def test_the_value_is_the_one_work_item_1791270165_set(self):
        assert conftest.SLOW_CASE_S == 90

    def test_the_reason_names_every_path_and_what_declined(self):
        """A count alone is a claim removed from the corpus without a word, which
        `seal/follow-up.md`'s first row calls the one direction a checker of
        claims must not fail in. The reader needs the paths in order to judge
        them by hand."""
        reason = shrunken_corpus(
            ["seal/ledger/two.md", "docs/one.md"], "the KEEP allowlist's liveness check"
        )
        assert "docs/one.md" in reason
        assert "seal/ledger/two.md" in reason
        assert "2 tracked path(s)" in reason
        assert "the KEEP allowlist's liveness check" in reason
        assert "not judging" in reason

    def test_the_reason_sorts_the_paths_it_names(self):
        """The set a caller hands over comes from a walk, so an unsorted reason
        would read differently run to run for the same tree."""
        reason = shrunken_corpus(["b.md", "a.md"], "x")
        assert reason.index("a.md") < reason.index("b.md")

    def test_the_builder_leaves_a_deleted_file_tracked(self, tmp_path):
        """The fixture shape itself, because a fixture that staged the removal
        would build the tree this defect is NOT about."""
        root = build_tracked_tree(
            tmp_path / "r", {"a.md": "one\n", "b.md": "two\n"}, deleted=["b.md"]
        )
        listed = subprocess.run(
            ["git", "-C", str(root), "ls-files"],
            capture_output=True,
            encoding="utf-8",
            check=True,
        ).stdout.split()
        assert listed == ["a.md", "b.md"], listed
        assert not os.path.exists(os.path.join(root, "b.md"))

    @pytest.mark.parametrize(
        "line, code",
        [
            ("# a whole-line comment", None),
            ("   # an indented one", None),
            ("run: x --range foo  # --baseline bar", "run: x --range foo"),
            ("fetch-depth: 0 # why", "fetch-depth: 0"),
            # A `#` is a comment only after a blank, and only outside quotes.
            ("url: a#b", "url: a#b"),
            ('run: echo "a # b"', 'run: echo "a # b"'),
            ("run: echo 'a # b'", "run: echo 'a # b'"),
            ('run: echo "a # b" # c', 'run: echo "a # b"'),
            # An escaped quote does not close a double-quoted string (round 1, ⬜ 7).
            ('run: echo "a \\" # b"', 'run: echo "a \\" # b"'),
            ('run: echo "a \\"" # b', 'run: echo "a \\""'),
            ("name: plain", "name: plain"),
        ],
    )
    def test_one_rule_says_what_a_comment_is(self, line, code):
        """The comment rule, one owner. A line whose first non-blank character is
        `#` is no code at all; a `#` after a blank and outside quotes ends the
        code there, where YAML ends a plain scalar and the shell stops reading."""
        assert code_line(line) == code, repr(code_line(line))

    def test_a_step_is_found_by_its_name_and_ends_at_the_next_one(self):
        """`workflow_step` reads the name the way `broad_gate.py#unquote` does,
        and the block stops at the next step of its list or at the next job."""
        step = workflow_step(WORKFLOW, "the real step")
        assert 'github.base_ref }}" = "main"' in step, step
        assert "exit 0" in step, step
        assert "a step of another job" not in step, step
        assert "echo other" not in step, step
        unrelated = workflow_step(WORKFLOW, "an unrelated step")
        assert [ln.strip() for ln in unrelated.splitlines() if ln.strip()] == [
            "- name: an unrelated step",
            "run: echo unrelated",
        ], unrelated

    def test_every_step_of_every_job_is_read_and_a_nameless_one_has_none(self):
        names = [name for name, _ in workflow_steps(WORKFLOW)]
        assert names == [
            None,
            "an unrelated step",
            "the real step",
            "a step of another job",
        ], names

    def test_the_conftest_takes_every_gh_login_away(self, tmp_path):
        """A6, structural. With all four token variables set and `GH_CONFIG_DIR`
        naming a directory that holds a login, the conftest's import leaves the
        two variables `gh` reads first holding a placeholder no server accepts,
        removes the other two, and points `GH_CONFIG_DIR` at an empty directory
        of its own. A token variable that is set keeps `gh` from falling back to
        the login it keeps in the OS keyring."""
        held = tmp_path / "gh-home"
        held.mkdir()
        (held / "hosts.yml").write_text("example.com:\n    oauth_token: x\n", "utf-8")
        env = {**os.environ, "GH_CONFIG_DIR": str(held)}
        env.update({name: "x" for name in TOKENS})
        r = subprocess.run(
            [sys.executable, "-c", PROBE],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            env=env,
            cwd=HERE,
        )
        assert r.returncode == 0, r.stderr
        seen = json.loads(r.stdout.strip().splitlines()[-1])
        assert seen["tokens"] == {
            "GH_TOKEN": NOT_A_GH_TOKEN,
            "GH_ENTERPRISE_TOKEN": NOT_A_GH_TOKEN,
        }, f"the suite's token variables: {sorted(seen['tokens'])}"
        assert seen["home"] != str(held), "GH_CONFIG_DIR still names the login's home"
        assert seen["empty"], f"GH_CONFIG_DIR is not an empty directory: {seen['home']}"
        # The directory is the run's own, and it goes when the run does.
        assert not os.path.exists(seen["home"]), f"left behind: {seen['home']}"

    def test_the_token_gh_would_send_is_not_a_login(self):
        """A6, behavioural. `gh auth token` takes the same path as every API
        call -- the variables, then `hosts.yml`, then the keyring's active slot --
        and needs no network. `gh auth status` does not read the keyring without
        a `hosts.yml`, so it reported no login on a machine where `gh api` was
        still logged in. Red on a keyring machine against a block that only
        empties `GH_CONFIG_DIR`. The token is never printed."""
        gh = shutil.which("gh")
        if gh is None:
            pytest.skip("gh is not on PATH, so nothing here can reach one")
        r = subprocess.run(
            [gh, "auth", "token"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            env={**os.environ, "GH_PROMPT_DISABLED": "1"},
        )
        token = r.stdout.strip()
        assert r.returncode != 0 or token == NOT_A_GH_TOKEN, (
            "`gh auth token` found a login under the suite's environment "
            f"(exit {r.returncode}, {len(token)} characters, not printed), so a "
            "case that reaches a live `gh` passes here and fails on CI"
        )

    def test_the_path_is_found_as_a_windows_oserror_spells_it(self):
        """CI's windows-latest leg on PR #605: `chain_check.py` quotes the
        `OSError`, whose filename is repr-escaped on Windows, so every backslash
        of the path arrives doubled and the plain path is not a substring. Shown
        here with a Windows-shaped path, since a POSIX path has no separator for
        the escape to double."""
        path = "C:\\Users\\x\\alone"
        oserror = FileNotFoundError(2, "No such file or directory", path + "\\..\\r.py")
        text = f"chain-check: the shared reader would not load ({oserror})"
        assert path not in text, "the fixture no longer has the Windows shape"
        assert names_path(path, text), text
        assert names_path(path, f"cannot read {path}\\..\\r.py, and it is ...")
        assert not names_path(path, "cannot read C:\\Users\\y\\alone"), (
            "matched another path"
        )

    def test_a_path_id_is_written_with_forward_slashes(self):
        assert posix_id(ntpath.join("agents", "framer.md"), "\\") == "agents/framer.md"
        assert posix_id("agents/framer.md") == "agents/framer.md"
        assert posix_id(None) is None


class Test_step_running:
    def test_accepts_the_step_a_comment_naming_its_script_cannot_move(self):
        """B4, #482. The comment above the unrelated step names
        `correction_check.py`, and the step that runs it is found anyway: only
        code lines are asked whether they name the script."""
        step = step_running(WORKFLOW, "correction_check.py")
        assert "the real step" in step, step
        assert "echo unrelated" not in step, step
        assert '--range "x...HEAD"' in step, step
        # The step's code keeps its blank line, and loses its trailing comment.
        assert "the range" not in step, step

    @pytest.mark.parametrize(
        "call",
        [
            lambda: workflow_step(WORKFLOW, "no such step"),
            lambda: step_running(WORKFLOW, "no_such_script.py"),
            # `echo` is in three steps' code: a region that is not one step.
            lambda: step_running(WORKFLOW, "echo"),
        ],
    )
    def test_refuses_a_layout_that_is_not_exactly_one_step(self, call):
        """A step layout the reader does not model fails loudly rather than
        reading the wrong region."""
        with pytest.raises(AssertionError):
            call()


class Test_census_case:
    def test_accepts_a_target_every_census_passes(self, tmp_path, monkeypatch):
        (tmp_path / "hooks").mkdir()
        (tmp_path / "hooks" / "x.py").write_text(
            'open(p, encoding="utf-8")\n', encoding="utf-8"
        )
        monkeypatch.setattr(censuses, "ROOT", str(tmp_path))
        assert conftest.census_case("hooks/x.py")() is None

    def test_refuses_a_target_one_census_flags_naming_it(self, tmp_path, monkeypatch):
        (tmp_path / "hooks").mkdir()
        (tmp_path / "hooks" / "y.py").write_text("open(p)\n", encoding="utf-8")
        monkeypatch.setattr(censuses, "ROOT", str(tmp_path))
        with pytest.raises(AssertionError, match=r"hooks/y\.py:1: encoding: "):
            conftest.census_case("hooks/y.py")()


test_census = conftest.census_case(TARGET)
