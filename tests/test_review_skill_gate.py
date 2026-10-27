"""review-skill-gate — the built-in review skill asks before it displaces ours.

Claude Code ships a `code-review` skill of its own. When the model picks it
in a repo that also carries specseal's, the user gets a bug-and-cleanup sweep
where they expected a spec-compliance review — and only finds out after the
review has already run. The gate turns that into one prompt beforehand.
"""

import io
import json
import os
import subprocess
import sys

import pytest
from conftest import census_case, decision_of, load_hook_module, opt_in, run_hook

TARGET = "hooks/review-skill-gate.py"

gate = load_hook_module("review-skill-gate.py", "review_skill_gate_for_units")


def payload(skill, repo, **extra):
    p = {
        "tool_name": "Skill",
        "session_id": "s1",
        "tool_input": {"skill": skill},
        "cwd": str(repo),
    }
    p.update(extra)
    return p


def run(skill, repo, **extra):
    return run_hook("review-skill-gate.py", payload(skill, repo, **extra))


class Test_git:
    def test_accepts_a_command_and_answers_its_output(self, repo):
        assert gate.git(["rev-parse", "--git-dir"], str(repo)) == ".git"

    def test_refuses_a_failed_git_whatever_it_printed(self, repo, monkeypatch):
        """A git that exits non-zero answers nothing, even where it wrote a
        path, so no marker goes under a directory a failed call named (#1017,
        the body's `git` row). The real git prints nothing on a failure, so
        the failure is faked to remove that guarantee (contract rule 13)."""

        def failed(cmd, **kwargs):
            return subprocess.CompletedProcess(cmd, 128, stdout="/x/.git\n", stderr="")

        monkeypatch.setattr(gate.subprocess, "run", failed)
        assert gate.git(["rev-parse", "--git-dir"], str(repo)) == ""


class Test_main:
    # --- the contended name ------------------------------------------------

    def test_refuses_the_builtin_so_the_user_is_offered_a_choice(self, repo):
        opt_in(repo)
        assert decision_of(run("code-review", repo)) == "deny"

    def test_refuses_the_builtin_with_a_reason_asking_a_two_option_question(self, repo):
        opt_in(repo)
        reason = json.loads(run("code-review", repo))["hookSpecificOutput"][
            "permissionDecisionReason"
        ]
        assert "AskUserQuestion" in reason
        assert "/agentic:code-review" in reason
        assert "/code-review" in reason

    def test_refuses_without_a_session_id_by_asking_instead_of_denying(self, repo):
        """No id means no way to record the question, and a deny would repeat.

        `ask` cannot loop: approving is itself the way through."""
        opt_in(repo)
        p = payload("code-review", repo)
        del p["session_id"]
        assert decision_of(run_hook("review-skill-gate.py", p)) == "ask"

    # --- everything else stays silent --------------------------------------

    def test_accepts_a_call_without_opt_in(self, repo):
        assert decision_of(run("code-review", repo)) == "silent"

    def test_accepts_our_own_skill(self, repo):
        opt_in(repo)
        assert decision_of(run("agentic:code-review", repo)) == "silent"

    @pytest.mark.parametrize(
        "names",
        [
            ("debug", "agentic:implement", "code-reviewer", "review"),
            ("acme:code-review", "code-review-strict", "my-code-review"),
        ],
        ids=["unrelated", "merely-contains-it"],
    )
    def test_accepts_any_other_skill_name(self, repo, names):
        """Substring matching would swallow a third-party skill by accident."""
        opt_in(repo)
        for name in names:
            assert decision_of(run(name, repo)) == "silent", name

    # --- a gate that crashes must let the work through ---------------------

    def test_accepts_a_malformed_payload_silently(self, repo):
        assert (
            decision_of(run_hook("review-skill-gate.py", {"tool_name": "Skill"}))
            == "silent"
        )

    @pytest.mark.parametrize("text", ["[]", '"code-review"', "3"])
    def test_accepts_a_payload_that_is_no_object_silently(
        self, text, monkeypatch, capsys
    ):
        """JSON that is not an object has no `.get`, and the gate says
        nothing rather than raising (#1017, the body's payload row)."""
        monkeypatch.setattr(sys, "stdin", io.StringIO(text))
        gate.main()
        assert capsys.readouterr().out == ""

    def test_accepts_a_missing_cwd_silently(self, repo):
        assert (
            decision_of(
                run_hook(
                    "review-skill-gate.py",
                    {"tool_name": "Skill", "tool_input": {"skill": "code-review"}},
                )
            )
            == "silent"
        )


class Test_already_asked:
    def test_accepts_a_second_call_in_the_same_session(self, repo):
        """The user who picks the built-in must not be denied their retry."""
        opt_in(repo)
        assert decision_of(run("code-review", repo)) == "deny"
        assert decision_of(run("code-review", repo)) == "silent"

    def test_accepts_a_linked_worktree_as_a_repository_too(self, repo, tmp_path):
        """Splitting review work into a worktree is the flow the README steers
        toward, and the gate went silent on every call made from one.

        `.git` is a FILE there, pointing at `<main>/.git/worktrees/<name>`, so a
        git-dir built as `<root>/.git` is not a directory and the marker write
        raises. An unwritable marker reads as "already asked", so the question
        separating the two review skills disappeared -- silently, every call.
        """
        opt_in(repo)
        # git tracks files, not directories, so the opt-in needs one to ride on --
        # and it has to be committed, or the worktree does not see it at all.
        (repo / "seal" / "ledger.md").write_text("# ledger\n", encoding="utf-8")
        git = lambda *a: subprocess.run(
            ["git", "-C", str(repo), *a],
            check=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        git("add", "-A")
        git("commit", "-qm", "opt in")
        wt = tmp_path / "wt"
        git("worktree", "add", "-q", str(wt), "-b", "wt/x")

        assert decision_of(run("code-review", wt)) == "deny"
        # and the marker landed in the worktree's OWN git dir, so the second call
        # goes through there -- a deny with nowhere to record it would repeat.
        assert decision_of(run("code-review", wt)) == "silent"
        gd = subprocess.run(
            ["git", "-C", str(wt), "rev-parse", "--absolute-git-dir"],
            check=True,  # or `gd` is "" and the join below reads the CWD instead,
            capture_output=True,  # failing as "no such file" and hiding the marker
            encoding="utf-8",
            errors="replace",
        ).stdout.strip()
        assert os.path.isfile(os.path.join(gd, "agentic-review-choice", "s1"))
        # The isolation runs the other way too: the worktree's marker did not
        # spend the main tree's question, so the same session is still asked
        # there. That is what "once per session per working tree" means, and
        # without this the gate could satisfy the asserts above by recording
        # every tree's question in one shared place.
        assert decision_of(run("code-review", repo)) == "deny"

    def test_refuses_another_sessions_marker_and_asks_again(self, repo):
        opt_in(repo)
        assert decision_of(run("code-review", repo)) == "deny"
        assert decision_of(run("code-review", repo, session_id="s2")) == "deny"


test_census = census_case(TARGET)
