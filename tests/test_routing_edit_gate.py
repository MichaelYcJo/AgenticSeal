"""routing-edit-gate: the first edit on an undeclared branch is refused.

The routing is decided before the first edit, so the check sits at the edit
tools: a `Write`, `Edit` or `NotebookEdit` of a file in an opted-in
repository's worktree is refused while no routing declaration names the
branch checked out there and the session has not run `seal no-work-item` on
that branch (#1027). The edited file's repository and branch are judged, never the
payload's `cwd`. Files under the `seal/` root, files git ignores and files
outside every opted-in repository are not judged.
"""

import json
import os
import shutil
import subprocess
import sys

import pytest
from conftest import (
    ask_entries,
    census_case,
    decision_of,
    declare_routing,
    git_repo,
    load_hook_module,
    load_module,
    local_home,
    mark_root,
    reason_of,
    run_hook,
    write_transcript,
)
from conftest import git as git_run
from conftest import git_out as git

TARGET = "hooks/routing-edit-gate.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HOOKS = os.path.join(ROOT, "hooks")
GATE = "routing-edit-gate.py"
SESSION = "s1"

gate = load_hook_module(GATE, "routing_edit_gate_under_test")
SEAL = load_module(
    os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
    "seal_for_routing_edit_gate",
)


def payload(path, tool="Edit", session=SESSION, cwd=None, key=None):
    """The call the harness hands the gate for an edit of PATH, from session
    SESSION, whose transcript is a path beside the file's repository that
    holds nothing unless a case writes it."""
    path = str(path)
    field = key or ("notebook_path" if tool == "NotebookEdit" else "file_path")
    return {
        "tool_name": tool,
        "session_id": session,
        "transcript_path": os.path.join(
            os.path.dirname(os.path.dirname(path)), "transcripts", f"{session}.jsonl"
        ),
        "cwd": str(cwd or os.path.dirname(path)),
        "tool_input": {field: path},
    }


def run(path, **kwargs):
    return run_hook(GATE, payload(path, **kwargs))


def opt_in(repo):
    mark_root(repo / "seal")
    return repo


def branch_of(repo):
    return git(repo, "rev-parse", "--abbrev-ref", "HEAD")


# The declaration path the refusal names, spelled the platform's way, as
# `hooks/implementer-notice.py` spells the same file
# (`tests/test_implementer_notice.py`).
HINT = os.path.join("seal", "threads", "<work-item-id>", "routing.md")


# The two texts a person reads (contract rule 14), pinned whole.
def attended(repo, branch):
    return (
        "AgenticSeal refused this edit; nothing was written.\n\n"
        f"`f.txt` is in `{repo}`, which runs the AgenticSeal workflow, and no "
        f"routing declaration names `{branch}`, the branch checked out there. "
        "The routing is decided before the first edit.\n\n"
        "Do not choose for the user. Put the routing question to them with the "
        "AskUserQuestion tool, as `skills/implement/orchestration.md` "
        "*Orchestrator: how the work is routed* states. Then write the "
        f"declaration at `{HINT}` from "
        f"`templates/records/sdd-routing.md`, naming `{branch}`, or, where they answer "
        f"`no work item`, run `seal no-work-item` once on `{branch}`. Then edit "
        "again.\n\n"
        "Re-issuing this edit unchanged meets this same refusal."
    )


def pressed(repo, branch):
    return (
        "AgenticSeal refused this edit; nothing was written.\n\n"
        f"`f.txt` is in `{repo}`, which runs the AgenticSeal workflow, and no "
        f"routing declaration names `{branch}`, the branch checked out there. "
        "The routing is decided before the first edit.\n\n"
        "This session's person pressed `automation` on the routing question, "
        "so no question is put to them, and none is to be put to them in its "
        "place.\n\n"
        "The ways on, none of which needs a person:\n"
        "  1. Where this edit belongs to the work item the run was routed for, "
        f"write its declaration at `{HINT}` from "
        f"`templates/records/sdd-routing.md`, naming `{branch}`, and edit again.\n"
        "  2. Where it belongs to no work item, run `seal no-work-item` once "
        f"on `{branch}`, and edit again.\n\n"
        "Re-issuing this edit unchanged meets this same refusal."
    )


# Where HEAD is detached no branch is named, and `seal no-work-item` records
# nothing there, so the ways on start by checking out a branch.
def detached(repo):
    return (
        "AgenticSeal refused this edit; nothing was written.\n\n"
        f"`f.txt` is in `{repo}`, which runs the AgenticSeal workflow, and HEAD is "
        "detached there, so no routing declaration can name its branch. The "
        "routing is decided before the first edit.\n\n"
    )


def attended_detached(repo):
    return detached(repo) + (
        "Do not choose for the user. Put the routing question to them with the "
        "AskUserQuestion tool, as `skills/implement/orchestration.md` "
        "*Orchestrator: how the work is routed* states. Then check out a "
        f"branch in `{repo}`, and write its declaration at `{HINT}` from "
        "`templates/records/sdd-routing.md`, naming that branch, or, where they answer "
        "`no work item`, run `seal no-work-item` once on it, because on a "
        "detached HEAD it records nothing. Then edit again.\n\n"
        "Re-issuing this edit unchanged meets this same refusal."
    )


def pressed_detached(repo):
    return detached(repo) + (
        "This session's person pressed `automation` on the routing question, "
        "so no question is put to them, and none is to be put to them in its "
        "place.\n\n"
        "The ways on, none of which needs a person:\n"
        "  1. Where this edit belongs to the work item the run was routed for, "
        f"check out its branch in `{repo}`, write its declaration at `{HINT}` "
        "from `templates/records/sdd-routing.md`, naming that branch, and edit again.\n"
        f"  2. Where it belongs to no work item, check out a branch in `{repo}`, "
        "run `seal no-work-item` once on it, and edit again; on a detached HEAD "
        "it records nothing.\n\n"
        "Re-issuing this edit unchanged meets this same refusal."
    )


class Test_main:
    # --- S1, S8: the refusal and its two texts -------------------------------

    def test_refuses_an_edit_on_a_branch_no_declaration_names(self, repo):
        """S1 and S8 attended: the deny names the declaration's path and
        `seal no-work-item`, and tells the model to put the routing question."""
        opt_in(repo)
        out = run(repo / "f.txt")
        assert decision_of(out) == "deny"
        assert reason_of(out) == attended(os.path.realpath(repo), branch_of(repo))
        # A `Write` may create the directories above its file.
        assert decision_of(run(repo / "src" / "new.py", tool="Write")) == "deny"

    def test_the_declaration_path_is_spelled_the_platforms_way_on_windows(
        self, monkeypatch
    ):
        """Under Windows' path rules the refusal names the declaration and
        the edited file in Windows' spelling, one dialect with the root it
        prints, as `hooks/implementer-notice.py` names the same file
        (`hooks/optin.py` says why), and an absolute root on another drive
        whole. CI run 40209166795 failed two cases here that had pinned `/`;
        round 2 of #1027, finding 3, put the expectation on the tree's rule."""
        import ntpath
        import types

        monkeypatch.setattr(gate, "os", types.SimpleNamespace(path=ntpath, sep="\\"))
        monkeypatch.setattr(gate.optin, "home_at", lambda top: r"C:\r\seal")
        assert (
            gate.declaration_hint(r"C:\r") == r"seal\threads\<work-item-id>\routing.md"
        )
        assert (
            gate.declaration_hint(r"D:\w")
            == r"C:\r\seal\threads\<work-item-id>\routing.md"
        )
        said = gate.reason(r"C:\r\src\new.py", r"C:\r", "feat", False)
        assert "`src\\new.py` is in `C:\\r`" in said, said

    def test_a_detached_head_names_no_branch_and_is_refused(self, repo):
        """S4 and S8 on a detached HEAD: the ways on start by checking out a
        branch, and both texts, attended and under the `automation` press,
        name `seal no-work-item` only as a run on that branch, because on a
        detached HEAD it records nothing."""
        opt_in(repo)
        git(repo, "switch", "-q", "--detach")
        top = os.path.realpath(repo)
        assert reason_of(run(repo / "f.txt")) == attended_detached(top)
        write_transcript(
            os.path.dirname(str(repo)), SESSION, ask_entries(repo), slug="transcripts"
        )
        assert reason_of(run(repo / "f.txt")) == pressed_detached(top)

    def test_accepts_a_detached_head_at_a_commit_a_declared_branch_holds(
        self, repo, tmp_path
    ):
        """Round 1 of #1027, finding 3: a proofer's clone at the reviewed SHA
        and a red-first clone of an earlier commit are detached checkouts of
        a declared branch. The branch is found under its local name, or under
        a remote-tracking one where the clone has no local branch of it."""
        opt_in(repo)
        base = branch_of(repo)
        declare_routing(repo)
        git(repo, "add", "seal")
        git(repo, "commit", "-qm", "declare")
        (repo / "f.txt").write_text("later\n", encoding="utf-8")
        git(repo, "commit", "-qam", "later")
        # The branch's head, and an earlier commit of it, by the local name.
        for at in (base, f"{base}~1"):
            git(repo, "switch", "-q", "--detach", at)
            assert decision_of(run(repo / "f.txt")) == "silent", at
        git(repo, "switch", "-q", base)
        # A clone with no local branch of that name: the remote-tracking one,
        # for a branch name holding a `/`.
        git(repo, "switch", "-q", "feature/x")
        declare_routing(repo, item="1787708605-another")
        git(repo, "add", "seal")
        git(repo, "commit", "-qm", "declare feature/x")
        git(repo, "switch", "-q", base)
        clone = tmp_path / "clone"
        git_run(tmp_path, "clone", "-q", "--no-local", str(repo), str(clone))
        git(clone, "switch", "-q", "--detach", "origin/feature/x")
        assert git(clone, "branch", "--list", "feature/x") == ""
        assert decision_of(run(clone / "f.txt")) == "silent"

    def test_refuses_a_detached_head_no_declared_branch_holds(self, repo):
        """The same tree, holding the declaration, at a commit only an
        undeclared branch holds: still refused."""
        opt_in(repo)
        declare_routing(repo)
        git(repo, "add", "seal")
        git(repo, "commit", "-qm", "declare")
        git(repo, "switch", "-q", "-c", "side")
        (repo / "f.txt").write_text("side\n", encoding="utf-8")
        git(repo, "commit", "-qam", "side")
        git(repo, "switch", "-q", "--detach")
        assert decision_of(run(repo / "f.txt")) == "deny"

    def test_refuses_a_detached_head_only_a_longer_branch_name_holds(self, repo):
        """Round 2 of #1027, finding 2: `for-each-ref refs/heads/x` also
        lists `refs/heads/x/sub`. A declaration naming `x`, with no branch
        `x` left, and an undeclared `x/sub` holding HEAD: still refused."""
        opt_in(repo)
        git(repo, "switch", "-q", "-c", "x")
        declare_routing(repo)
        git(repo, "add", "seal")
        git(repo, "commit", "-qm", "declare x")
        git(repo, "switch", "-q", "-c", "keep")
        git(repo, "branch", "-q", "-D", "x")
        git(repo, "switch", "-q", "-c", "x/sub")
        (repo / "f.txt").write_text("sub\n", encoding="utf-8")
        git(repo, "commit", "-qam", "sub")
        git(repo, "branch", "-q", "-D", "keep")
        git(repo, "switch", "-q", "--detach")
        assert decision_of(run(repo / "f.txt")) == "deny"

    def test_under_the_automation_press_the_refusal_names_no_question_tool(self, repo):
        """S8: the person pressed `automation`, read from this session's own
        transcript, so the deny puts nothing to them."""
        opt_in(repo)
        write_transcript(
            os.path.dirname(str(repo)), SESSION, ask_entries(repo), slug="transcripts"
        )
        out = run(repo / "f.txt")
        assert decision_of(out) == "deny"
        assert reason_of(out) == pressed(os.path.realpath(repo), branch_of(repo))
        assert "AskUserQuestion" not in reason_of(out)

    def test_refuses_the_same_edit_again_with_the_same_text(self, repo):
        opt_in(repo)
        assert run(repo / "f.txt") == run(repo / "f.txt")

    # --- S2, S3: what lets an edit through -----------------------------------

    @pytest.mark.parametrize(
        "review", ["through the review chain", "straight to the PR"]
    )
    def test_accepts_any_edit_on_a_declared_branch(self, repo, review):
        """S2, for either `Review` answer."""
        opt_in(repo)
        declare_routing(repo, review=review)
        assert decision_of(run(repo / "f.txt")) == "silent"
        assert decision_of(run(repo / "src" / "new.py", tool="Write")) == "silent"

    def test_accepts_the_declaration_under_either_root(self, repo):
        """S3: with no declaration, writing `routing.md` is silent under the
        shared root and under the local one, while a file outside the root
        is refused in both modes."""
        opt_in(repo)
        record = repo / "seal" / "threads" / "1700000000-x" / "routing.md"
        assert decision_of(run(record, tool="Write")) == "silent"
        assert decision_of(run(repo / "f.txt")) == "deny"
        shutil.rmtree(repo / "seal")
        home = local_home(repo)
        record = home / "threads" / "1700000000-x" / "routing.md"
        assert decision_of(run(record, tool="Write", cwd=repo)) == "silent"
        assert decision_of(run(repo / "f.txt")) == "deny"

    # --- S4: a change that belongs to no work item ---------------------------

    def test_accepts_the_session_that_recorded_no_work_item_on_that_branch_only(
        self, repo, monkeypatch, capsys
    ):
        """S4: `seal no-work-item` run under this session's id lets its edits
        through on the branch it ran on; another session's edit there, and
        this session's edit on another branch of the same clone, are still
        refused (`questions.md` Q7 of #1027, answer (b))."""
        opt_in(repo)
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", SESSION)
        assert SEAL.main(["no-work-item"], cwd=str(repo)) == 0
        capsys.readouterr()
        assert decision_of(run(repo / "f.txt")) == "silent"
        assert decision_of(run(repo / "f.txt", session="s2")) == "deny"
        git(repo, "switch", "-q", "feature/x")
        assert decision_of(run(repo / "f.txt")) == "deny"

    def test_accepts_the_recording_session_on_a_branch_with_no_commit_yet(
        self, tmp_path, monkeypatch, capsys
    ):
        """S4 before the first commit: HEAD names `main`, which has no commit,
        and `seal no-work-item` run there lets this session's edit through
        (round 4 of #1027, finding 1)."""
        fresh = tmp_path / "fresh"
        git_run(tmp_path, "init", "-q", "-b", "main", str(fresh))
        opt_in(fresh)
        monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", SESSION)
        assert SEAL.main(["no-work-item"], cwd=str(fresh)) == 0
        capsys.readouterr()
        assert decision_of(run(fresh / "f.txt", tool="Write")) == "silent"

    def test_a_record_naming_no_branch_lets_nothing_through(self, repo):
        """The record an earlier build wrote is an empty file, which names no
        branch, so it lets no edit through."""
        opt_in(repo)
        where = git(repo, "rev-parse", "--absolute-git-dir")
        records = os.path.join(where, "agentic-no-work-item")
        os.makedirs(records)
        with open(os.path.join(records, SESSION), "w", encoding="utf-8"):
            pass
        assert decision_of(run(repo / "f.txt")) == "deny"

    # --- S5: the edited file decides -----------------------------------------

    def test_the_edited_files_repository_is_judged_and_never_the_cwd(
        self, repo, tmp_path
    ):
        """S5: the payload's `cwd` in a repository that has not opted in and
        the file in one that has is refused; the reverse is silent."""
        opt_in(repo)
        other = git_repo(tmp_path / "other")
        assert decision_of(run(repo / "f.txt", cwd=other)) == "deny"
        assert decision_of(run(other / "f.txt", cwd=repo)) == "silent"

    def test_a_linked_worktree_is_judged_by_its_own_branch(self, repo, tmp_path):
        """S5: in local mode a linked worktree shares the root; its branch is
        declared and the main checkout's is not."""
        home = local_home(repo)
        tree = tmp_path / "tree"
        git(repo, "worktree", "add", "-q", str(tree), "feature/x")
        declare_routing(tree, home=home)
        assert decision_of(run(tree / "f.txt", cwd=repo)) == "silent"
        assert decision_of(run(repo / "f.txt", cwd=tree)) == "deny"

    # --- S6: what is not judged ----------------------------------------------

    def test_an_ignored_file_and_one_outside_every_repository_are_not_judged(
        self, repo, tmp_path
    ):
        """S6: an ignored file never lands in a commit, and a file outside
        every repository, or in one that has not opted in, belongs to
        nothing this plugin governs."""
        opt_in(repo)
        (repo / ".gitignore").write_text("*.log\nbuild/\n", encoding="utf-8")
        assert decision_of(run(repo / "x.log", tool="Write")) == "silent"
        assert decision_of(run(repo / "build" / "a" / "b.txt", tool="Write")) == (
            "silent"
        )
        outside = tmp_path / "outside"
        outside.mkdir()
        assert decision_of(run(outside / "a.txt", tool="Write")) == "silent"
        plain = git_repo(tmp_path / "plain")
        assert decision_of(run(plain / "f.txt")) == "silent"

    def test_a_notebook_is_judged_by_its_notebook_path(self, repo):
        """S6: `NotebookEdit` names its file `notebook_path`; under a declared
        branch it is silent, and under an undeclared one it is refused."""
        opt_in(repo)
        notebook = repo / "n.ipynb"
        assert decision_of(run(notebook, tool="NotebookEdit")) == "deny"
        declare_routing(repo)
        assert decision_of(run(notebook, tool="NotebookEdit")) == "silent"

    @pytest.mark.parametrize(
        "tool, tool_input",
        [
            ("Read", {"file_path": "{repo}/f.txt"}),
            ("Edit", {"file_path": "sub/f.txt"}),
            ("Edit", {}),
            ("Edit", None),
        ],
        ids=["another tool", "a relative path", "no path", "no input"],
    )
    def test_a_call_naming_no_absolute_edit_path_is_not_judged(
        self, repo, tool, tool_input
    ):
        """Only the edit tools are judged. They take an absolute path, and
        the gate reads no `cwd` to make one, so a relative path places no
        file, even where it names a directory under the hook's own working
        directory."""
        opt_in(repo)
        (repo / "sub").mkdir()
        if tool_input:
            tool_input = {
                k: v.format(repo=os.path.realpath(repo)) for k, v in tool_input.items()
            }
        event = {"tool_name": tool, "tool_input": tool_input, "cwd": str(repo)}
        r = subprocess.run(
            [sys.executable, os.path.join(HOOKS, GATE)],
            input=json.dumps(event),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            cwd=str(repo),
        )
        assert decision_of(r.stdout) == "silent", r.stderr

    # --- S7: a paused rebase -------------------------------------------------

    @pytest.mark.parametrize("declared", [True, False], ids=["declared", "undeclared"])
    def test_a_paused_rebase_is_judged_by_the_branch_it_names(self, repo, declared):
        """S7: HEAD is detached while the rebase waits on a conflict, and the
        branch the rebase names stands for it."""
        opt_in(repo)
        base = branch_of(repo)
        git(repo, "switch", "-q", "feature/x")
        (repo / "f.txt").write_text("feature\n", encoding="utf-8")
        git(repo, "commit", "-qam", "feature")
        git(repo, "switch", "-q", base)
        (repo / "f.txt").write_text("base\n", encoding="utf-8")
        git(repo, "commit", "-qam", "base")
        git(repo, "switch", "-q", "feature/x")
        if declared:
            declare_routing(repo)
        assert git_run(repo, "rebase", base, check=False).returncode != 0
        assert git(repo, "rev-parse", "--abbrev-ref", "HEAD") == "HEAD"
        want = "silent" if declared else "deny"
        assert decision_of(run(repo / "f.txt")) == want


class Test_module:
    def test_the_gate_is_registered_on_the_edit_tools_post_edit_names(self):
        """One list of edit tools: the gate's own, the `pre-edit` matcher and
        the `post-edit` matcher. A tool the matcher missed would pass every
        edit through it in silence."""
        dispatch = load_hook_module("dispatch.py", "dispatch_for_routing_edit_gate")
        groups = [g for g, gates in dispatch.GROUPS.items() if GATE in gates]
        assert groups == ["pre-edit"], groups
        with open(os.path.join(HOOKS, "hooks.json"), encoding="utf-8") as f:
            hooks = json.load(f)["hooks"]

        def matchers(event, group):
            run_group = f'"${{CLAUDE_PLUGIN_ROOT}}/hooks/dispatch.py" {group}'
            command = f"python3 {run_group} || py -3 {run_group}"
            return [
                e["matcher"]
                for e in hooks[event]
                if any(h["command"] == command for h in e["hooks"])
            ]

        tools = "|".join(gate.TOOLS)
        assert matchers("PreToolUse", "pre-edit") == [tools]
        assert matchers("PostToolUse", "post-edit") == [tools]

    def test_the_dispatcher_carries_the_refusal(self, repo):
        opt_in(repo)
        r = subprocess.run(
            [sys.executable, os.path.join(HOOKS, "dispatch.py"), "pre-edit"],
            input=json.dumps(payload(repo / "f.txt")),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        said = json.loads(r.stdout)["hookSpecificOutput"]
        assert said["hookEventName"] == "PreToolUse"
        assert said["permissionDecision"] == "deny"


test_census = census_case(TARGET)
