"""`hooks/sealer-stamp-queue.py`, one class per function.

Written anew from the code by #942's phase 6; the old cases of
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` were read for
their inputs. `main` runs in the process. One repository in local mode is
built for the module, its root under the git common dir with a work item
whose `guarantee.md` reads `sealed` over the branch's commit, and each case
takes a copy, so the values file the gate queues is the case's own. One case
runs the gate through `hooks/dispatch.py post-edit`, as the harness runs it.
"""

import io
import json
import os
import shutil
import subprocess
import sys

import pytest
from conftest import (
    ROOT,
    STAMP_ITEM,
    census_case,
    commit_everything_as_e,
    git,
    git_out,
    guarantee_record,
    load_hook_module,
    queued_values,
    routing_record,
)

TARGET = "hooks/sealer-stamp-queue.py"

gate = load_hook_module("sealer-stamp-queue.py", "sealer_stamp_queue_under_test")
stamp = gate.load_stamp()


@pytest.fixture(scope="module")
def _local_template(tmp_path_factory):
    """A repository in local mode on `feat/x`, built once: no `seal/` in its
    tree, and under `.git/seal/specs/<item>/` the work item's `routing.md`
    naming the branch, two round records, `broad-gate.md` and a
    `guarantee.md` reading `sealed` over the branch's commit."""
    repo = tmp_path_factory.mktemp("queue-world") / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    (repo / "README.md").write_text("x\n", encoding="utf-8")
    commit_everything_as_e(repo, "x")
    git(repo, "switch", "-qc", "feat/x")
    (repo / "work.txt").write_text("the work\n", encoding="utf-8")
    commit_everything_as_e(repo, "the work")
    target = git_out(repo, "rev-parse", "--short", "HEAD")
    base = git_out(repo, "rev-parse", "--short", "main")
    item = repo / ".git" / "seal" / "specs" / STAMP_ITEM
    (item / "rounds").mkdir(parents=True)
    for n in (1, 2):
        (item / "rounds" / f"round-{n}.md").write_text("x\n", encoding="utf-8")
    (item / "routing.md").write_text(routing_record(), encoding="utf-8")
    (item / "broad-gate.md").write_text(
        f"| Field | Value |\n|---|---|\n| Broad gate | {target} against {base} |\n",
        encoding="utf-8",
    )
    (item / "guarantee.md").write_text(
        guarantee_record(target, base, "sealed"), encoding="utf-8"
    )
    return repo


@pytest.fixture
def local(tmp_path, _local_template):
    """This case's copy: (repo, the guarantee's path)."""
    repo = tmp_path / "repo"
    shutil.copytree(_local_template, repo)
    return repo, repo / ".git" / "seal" / "specs" / STAMP_ITEM / "guarantee.md"


def payload(path, cwd, tool="Write", session="s-1", **extra):
    """A `PostToolUse` payload for TOOL on the file at PATH."""
    body = {
        "hook_event_name": "PostToolUse",
        "tool_name": tool,
        "tool_input": {"file_path": str(path)},
        "cwd": str(cwd),
    }
    if session:
        body["session_id"] = session
    body.update(extra)
    return body


@pytest.fixture
def edited(monkeypatch, capsys):
    """`main` after an edit: BODY on stdin, a dict as JSON and a string as it
    is; what it printed."""

    def run(body):
        text = body if isinstance(body, str) else json.dumps(body)
        monkeypatch.setattr(sys, "stdin", io.StringIO(text))
        gate.main()
        return capsys.readouterr().out

    return run


def queued_line(path):
    real = os.path.realpath(path)
    return stamp.QUEUED.format(
        id=STAMP_ITEM.split("-")[0], path=real, command=stamp.quote(real)
    )


class Test_shaped:
    @pytest.mark.parametrize(
        "path",
        [
            "/x/repo/.git/seal/specs/1799000000-an-item/guarantee.md",
            "/x/repo/seal/specs/a/guarantee.md",
            "/x/repo/.git/seal/specs/a/../b/guarantee.md",
        ],
    )
    def test_accepts_a_work_items_guarantee(self, path):
        assert gate.shaped(path)

    def test_accepts_a_windows_path_with_its_separators(self, monkeypatch):
        monkeypatch.setattr(gate.os, "sep", "\\")
        monkeypatch.setattr(gate.os.path, "normpath", lambda p: p)
        assert gate.shaped(r"C:\x\repo\.git\seal\specs\a\guarantee.md")

    @pytest.mark.parametrize(
        "path",
        [
            "/x/repo/.git/seal/specs/a/notes.md",
            "/x/repo/docs/guarantee.md",
            "/x/repo/seal/specs/a/b/guarantee.md",
            "/x/repo/seal/specs/guarantee.md",
            "/x/repo/seal/specs/a/guarantee.md.bak",
        ],
    )
    def test_refuses_any_other_file(self, path):
        assert not gate.shaped(path)


class Test_load_stamp:
    def test_accepts_the_shipped_seal_stamp(self):
        assert callable(gate.load_stamp().queue_for_local_guarantee)

    def test_refuses_nothing_itself_and_lets_main_stay_silent(
        self, local, edited, monkeypatch
    ):
        """It raises what the import raises; `main` catches it and says
        nothing."""
        repo, path = local

        def broken():
            raise SystemExit(3)

        monkeypatch.setattr(gate, "load_stamp", broken)
        assert edited(payload(path, repo)) == ""
        assert queued_values(repo) == []


class Test_main:
    @pytest.mark.rule("stamp-drawn-once")
    @pytest.mark.parametrize("tool", ["Write", "Edit"])
    def test_accepts_a_local_mode_sealed_guarantee(self, local, edited, tool, tmp_path):
        """1792363231 S6: the work item's one values file is queued for the
        payload's session and the writer's line is printed. The repository is
        found from the edited file, never from the payload's `cwd`, which is
        outside it."""
        repo, path = local
        elsewhere = tmp_path / "elsewhere"
        elsewhere.mkdir()
        out = edited(payload(path, elsewhere, tool=tool))
        (written,) = queued_values(repo)
        assert os.path.dirname(written) == str(repo / ".git" / "specseal-stamp" / "s-1")
        assert json.loads(out) == {"systemMessage": queued_line(written)}

    @pytest.mark.rule("stamp-drawn-once")
    def test_accepts_a_subagents_write_for_the_main_session(self, local, edited):
        """The sealer writes its own `guarantee.md`, so the payload carries its
        `agent_id` beside the main session's `session_id`; queueing is not
        drawing, and the file is queued for the main session."""
        repo, path = local
        sealer = {"agent_id": "a-1", "agent_type": "specseal:sealer"}
        assert json.loads(edited(payload(path, repo, **sealer)))
        (written,) = queued_values(repo)
        assert os.path.dirname(written) == str(repo / ".git" / "specseal-stamp" / "s-1")

    @pytest.mark.rule("stamp-drawn-once")
    def test_refuses_a_shared_mode_guarantee_post_commit_queues(
        self, local, edited, tmp_path
    ):
        """1792363231 S5, the gate's half: a `sealed` under `<repo>/seal/`,
        whose stamp `post-commit` queues at the commit, queues nothing here."""
        repo, path = local
        shared = repo / "seal" / "specs" / STAMP_ITEM
        shutil.copytree(path.parent, shared)
        assert edited(payload(shared / "guarantee.md", repo)) == ""
        assert queued_values(repo) == []

    @pytest.mark.rule("stamp-drawn-once")
    @pytest.mark.parametrize(
        "given",
        [
            lambda path, cwd: payload(path.parent / "notes.md", cwd),
            lambda path, cwd: payload(cwd / "docs" / "guarantee.md", cwd),
            lambda path, cwd: payload(path, cwd, tool="NotebookEdit"),
            lambda path, cwd: payload(path, cwd, session=None),
            lambda path, cwd: {**payload(path, cwd), "tool_input": {"file_path": 7}},
            lambda path, cwd: "a payload that is not JSON",
            lambda path, cwd: "[]",
        ],
        ids=[
            "another-file-of-the-item",
            "a-guarantee-outside-seal-specs",
            "notebook-edit",
            "no-session",
            "a-path-that-is-no-string",
            "not-json",
            "a-list",
        ],
    )
    def test_refuses_any_other_edit_before_it_loads_seal_stamp(
        self, local, edited, given, monkeypatch
    ):
        """The gate runs after every file edit in every repository, so for
        any other edit it says nothing, writes nothing, and loads
        `seal_stamp.py`, its only way to `git`, not at all; the guarantee's
        own `Write` is the control that the loader is reached."""
        repo, path = local
        (path.parent / "notes.md").write_text(
            path.read_text(encoding="utf-8"), encoding="utf-8"
        )
        loads = []
        real = gate.load_stamp
        monkeypatch.setattr(gate, "load_stamp", lambda: loads.append(1) or real())
        assert edited(given(path, repo)) == ""
        assert loads == [] and queued_values(repo) == []
        assert edited(payload(path, repo))
        assert loads == [1]


class Test_module:
    @pytest.mark.rule("stamp-drawn-once")
    def test_the_post_edit_group_queues_through_the_dispatcher(self, local):
        """The gate as the harness runs it after a `Write`: `dispatch.py
        post-edit` with the payload on stdin prints the writer's line, and the
        group holds the gate."""
        repo, path = local
        done = subprocess.run(
            [sys.executable, os.path.join(ROOT, "hooks", "dispatch.py"), "post-edit"],
            input=json.dumps(payload(path, repo)),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            cwd=str(repo),
        )
        assert done.returncode == 0, done.stderr
        (written,) = queued_values(repo)
        assert json.loads(done.stdout) == {"systemMessage": queued_line(written)}
        dispatch = load_hook_module("dispatch.py", "dispatch_for_the_post_edit_group")
        assert "sealer-stamp-queue.py" in dispatch.GROUPS["post-edit"]


test_census = census_case(TARGET)
