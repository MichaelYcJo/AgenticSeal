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
`build_tracked_tree` came from `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`
in #942's round 3 fix pass, and that file keeps its sweep across files.
`names_path`'s Windows case came from `tests/test_a_script_copied_alone_exits_2.py`
and `posix_id`'s from
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` in #942's
round 9 fix pass, each a case of one helper of this module.

Seen red before they were committed (contract rule 15): the three accepting
cases failed against the conftest that still held the failing ceiling, which
had neither `SLOW_CASE_S` nor a summary hook, and `seal mutate` turned
each refusing case red by breaking the condition it pins.
"""

import ast
import json
import ntpath
import os
import pathlib
import shutil
import subprocess
import sys
import types

import censuses
import conftest
import pytest
from conftest import (
    ROOT,
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

TESTS = os.path.join(ROOT, "tests")
CONFTEST = os.path.join(TESTS, "conftest.py")
TOKENS = ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN", "GITHUB_ENTERPRISE_TOKEN")

# Pinned verbatim: the conftest's placeholder, which is not a credential.
NOT_A_GH_TOKEN = "agentic-suite-runs-with-gh-logged-out"

# The variables a `pull_request` run of `tests` sets for every step (#1058).
PULL_REQUEST_RUN = {
    "GITHUB_HEAD_REF": "feature/x",
    "GITHUB_BASE_REF": "main",
    "GITHUB_EVENT_NAME": "pull_request",
    "GITHUB_EVENT_PATH": "event.json",
    "GITHUB_ACTIONS": "true",
    "GITHUB_REF": "refs/pull/1/merge",
}

# Run the conftest's import-time code in a child whose environment carries
# every token and a config directory of its own, and report what is left.
PROBE = f"""
import json, os, runpy
given = sorted(n for n in os.environ if n.startswith("GITHUB_"))
runpy.run_path({CONFTEST!r})
home = os.environ.get("GH_CONFIG_DIR")
print(json.dumps({{
    "tokens": {{n: os.environ[n] for n in {TOKENS!r} if n in os.environ}},
    "home": home,
    "empty": bool(home) and os.path.isdir(home) and not os.listdir(home),
    "given": given,
    "github": sorted(n for n in os.environ if n.startswith("GITHUB_")),
}}))
"""


def run_probe(env):
    """What `PROBE` reports, run in a child whose environment is ENV."""
    r = subprocess.run(
        [sys.executable, "-c", PROBE],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        env=env,
        cwd=TESTS,
    )
    assert r.returncode == 0, r.stderr
    return json.loads(r.stdout.strip().splitlines()[-1])


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
        way this repair could report less than the crash it replaces. A skip
        raised here would end this case as skipped, which a run reads as no
        failure, so the case catches the skip and fails on it."""
        try:
            declined = decline_if_shrunken([], "x")
        except pytest.skip.Exception as skipped:
            pytest.fail(f"declined a tree with nothing missing: {skipped}")
        assert declined is None


class Test_read:
    def test_accepts_an_absolute_path_where_it_stands(self, tmp_path):
        path = tmp_path / "a.md"
        path.write_text("absolute\n", encoding="utf-8")
        assert conftest.read(str(path)) == "absolute\n"

    def test_refuses_the_working_directorys_file_for_the_roots(
        self, tmp_path, monkeypatch
    ):
        """Run from a directory that is not the repository root, as a case
        driven by bare `pytest` from elsewhere is: a relative path is still the
        root's file, never the one of that name beside the working directory."""
        (tmp_path / "CLAUDE.md").write_text("a decoy\n", encoding="utf-8")
        monkeypatch.chdir(tmp_path)
        with open(os.path.join(ROOT, "CLAUDE.md"), encoding="utf-8") as handle:
            assert conftest.read("CLAUDE.md") == handle.read()


class Test_repo_relative:
    def test_accepts_a_file_at_the_root_as_its_name(self):
        assert conftest.repo_relative(os.path.join(ROOT, "CLAUDE.md")) == "CLAUDE.md"

    def test_refuses_to_drop_the_directories_of_a_nested_path(self):
        nested = os.path.join(ROOT, "tests", "conftest.py")
        assert conftest.repo_relative(nested) == "tests/conftest.py"


def python_files(top):
    """The path of every Python file under TOP, `__pycache__` left out, in
    walk order."""
    found = []
    for directory, subdirectories, names in os.walk(top):
        subdirectories[:] = sorted(d for d in subdirectories if d != "__pycache__")
        found += [
            os.path.join(directory, n) for n in sorted(names) if n.endswith(".py")
        ]
    return found


def own_path_directories(path):
    """The line numbers at which the Python file at PATH takes a directory
    from its own `__file__`: the name inside a `dirname` call, or under a
    `.parent` or `.parents` of a path built from it. A `__file__` inside a
    string, such as a fixture's source, is no name in this file, and a loaded
    module's `module.__file__` is an attribute, so neither is read."""
    with open(path, encoding="utf-8") as handle:
        tree = ast.parse(handle.read(), path)
    lines = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            climbs = getattr(func, "attr", getattr(func, "id", None)) == "dirname"
        else:
            climbs = isinstance(node, ast.Attribute) and node.attr in (
                "parent",
                "parents",
            )
        if climbs:
            lines |= {
                n.lineno
                for n in ast.walk(node)
                if isinstance(n, ast.Name) and n.id == "__file__"
            }
    return sorted(lines)


def shared_names(top):
    """`{name: [paths]}` for each file name two Python files under TOP hold,
    each path relative to TOP and written with `/`."""
    held = {}
    for path in python_files(top):
        rel = posix_id(os.path.relpath(path, top))
        held.setdefault(os.path.basename(path), []).append(rel)
    return {name: paths for name, paths in held.items() if len(paths) > 1}


class Test_git:
    def test_accepts_a_failing_call_with_checking_off_as_its_process(self, tmp_path):
        """A repository with no commit has no HEAD to verify."""
        conftest.git(tmp_path, "init", "-q")
        done = conftest.git(tmp_path, "rev-parse", "--verify", "HEAD", check=False)
        assert done.returncode != 0

    def test_refuses_a_failing_call_by_default(self, tmp_path):
        conftest.git(tmp_path, "init", "-q")
        with pytest.raises(subprocess.CalledProcessError):
            conftest.git(tmp_path, "rev-parse", "--verify", "HEAD")


IDENTITY_VARIABLES = (
    "GIT_AUTHOR_NAME",
    "GIT_AUTHOR_EMAIL",
    "GIT_COMMITTER_NAME",
    "GIT_COMMITTER_EMAIL",
)


class Test_commit_everything_as_e:
    def test_accepts_a_commit_by_e_in_a_repository_of_another_identity(
        self, tmp_path, monkeypatch
    ):
        """The repository's own identity is `t`, and an identity in the
        environment would win over both, so the case removes it."""
        for name in IDENTITY_VARIABLES:
            monkeypatch.delenv(name, raising=False)
        repo = conftest.git_repo(tmp_path / "r")
        (repo / "g.txt").write_text("two\n", encoding="utf-8")
        head = conftest.commit_everything_as_e(repo, "two")
        assert conftest.git_out(repo, "log", "-1", "--format=%an <%ae>", head) == (
            "e <e@example.com>"
        )

    def test_refuses_a_tree_with_nothing_to_commit(self, tmp_path):
        repo = conftest.git_repo(tmp_path / "r")
        with pytest.raises(subprocess.CalledProcessError):
            conftest.commit_everything_as_e(repo, "nothing")


class Test_imported_roots:
    def test_accepts_the_top_level_name_of_each_import(self, tmp_path):
        path = tmp_path / "m.py"
        path.write_text(
            "import os.path\nimport a.b as c\nfrom json import dumps\n",
            encoding="utf-8",
        )
        assert conftest.imported_roots(path) == {"os", "a", "json"}

    def test_refuses_a_relative_import_as_a_name(self, tmp_path):
        """Each relative import is `.`, the one root that names no module."""
        path = tmp_path / "m.py"
        path.write_text("from . import x\nfrom .y import z\n", encoding="utf-8")
        assert conftest.imported_roots(path) == {"."}


class Test_q:
    def test_accepts_a_path_object_as_its_plain_text(self):
        """A path is read as its text first: `shlex.quote` takes no path."""
        assert conftest.q(pathlib.PurePosixPath("dir/plain")) == "dir/plain"

    def test_refuses_a_space_unquoted(self):
        assert conftest.q("a b") == "'a b'"


class _Guard:
    """A stand-in for a loaded worktree guard: `main` prints OUT, then exits
    as the hook does. `sessions_in_tree` and `load_input` are what
    `guard_decision` replaces."""

    def __init__(self, out=""):
        self.out = out
        self.sessions_in_tree = self.load_input = None

    def main(self):
        if self.out:
            print(self.out)
        sys.exit(0)


class Test_guard_decision:
    def test_accepts_the_guards_decision_and_reason(
        self, tmp_path, monkeypatch, capsys
    ):
        decided = {"permissionDecision": "ask", "permissionDecisionReason": "why"}
        guard = _Guard(json.dumps({"hookSpecificOutput": decided}))
        found = conftest.guard_decision(guard, monkeypatch, capsys, tmp_path, "ls")
        assert found == ("ask", "why")

    def test_refuses_a_guard_that_prints_nothing_as_anything_but_silent(
        self, tmp_path, monkeypatch, capsys
    ):
        """A guard that says nothing allows the command, and the cases tell
        that apart from a decision by the word `silent`."""
        found = conftest.guard_decision(_Guard(), monkeypatch, capsys, tmp_path, "ls")
        assert found == ("silent", "")


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
        seen = run_probe(env)
        assert seen["tokens"] == {
            "GH_TOKEN": NOT_A_GH_TOKEN,
            "GH_ENTERPRISE_TOKEN": NOT_A_GH_TOKEN,
        }, f"the suite's token variables: {sorted(seen['tokens'])}"
        assert seen["home"] != str(held), "GH_CONFIG_DIR still names the login's home"
        assert seen["empty"], f"GH_CONFIG_DIR is not an empty directory: {seen['home']}"
        # The directory is the run's own, and it goes when the run does.
        assert not os.path.exists(seen["home"]), f"left behind: {seen['home']}"

    def test_the_conftest_takes_every_github_variable_away(self):
        """S1 of #1058. With the variables a `pull_request` run sets in its
        environment, the conftest's import leaves no name that starts with
        `GITHUB_`, so a case and every child it starts see the environment of
        a run with no pull request, under every event. A case that needs one
        of these variables sets it with `monkeypatch.setenv`. The `gh` login
        is taken away as before. Seen red against `tests/conftest.py` at
        `977b6613`, which left all six names in place."""
        seen = run_probe({**os.environ, **PULL_REQUEST_RUN})
        assert seen["given"] == sorted(PULL_REQUEST_RUN), seen["given"]
        assert seen["github"] == [], f"left by the conftest: {seen['github']}"
        assert seen["tokens"] == {
            "GH_TOKEN": NOT_A_GH_TOKEN,
            "GH_ENTERPRISE_TOKEN": NOT_A_GH_TOKEN,
        }, f"the suite's token variables: {sorted(seen['tokens'])}"

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

    def test_no_test_file_derives_the_root_from_its_own_path(self):
        """`ROOT` is the one source of the repository root (#1060). A test
        file that climbed from its own `__file__` was right only at the depth
        it stood at: moving the test files one directory down meant one edit
        in each, and a file left at the old depth made a glob under the root
        empty, so a case looping over it passed over nothing. A test file
        imports `ROOT` from `tests/conftest.py`, and `CONTRIBUTING.md` *The
        test layout* says so."""
        found = [
            f"{conftest.repo_relative(path)}:{line}"
            for path in python_files(TESTS)
            if os.path.basename(path).startswith("test_")
            for line in own_path_directories(path)
        ]
        assert found == [], (
            "a test file takes the repository root from `tests/conftest.py#ROOT`, "
            f"not from its own `__file__`: {found}"
        )

    def test_no_two_python_files_under_tests_share_a_name(self):
        """The module puts every directory under `tests/` that holds a test
        file on `sys.path`, and pytest's `prepend` mode imports each test
        file by its bare name (#1060). Two files of one name then import as
        one module: pytest fails the collection of the second test file, and
        a helper of one name shadows the other wherever the path finds it
        first. Files that are not Python are not imported and are not read."""
        found = shared_names(TESTS)
        assert found == {}, (
            "each Python file under `tests/` keeps a name no other one holds, "
            f"wherever it stands: {found}"
        )


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
