"""In local mode every gate finds what it reads under `<git-common-dir>/seal/`.

The read side of #80 shipped in 0.4.0: `optin.home_at` looks at `<repo>/seal/`
and then at the common git directory's `seal/`. What these cases pin is the
JOINERS — the hooks that spelled `seal/` under the repository root rather than
asking for the resolved root, and the one whose printed path a session would
type in the wrong place (spec S6, Q5). Each is run in a local-mode fixture:
the `repo` fixture with `local_home` and nothing at `<repo>/seal/`.

The fail direction of every path here is "not opted in" or "nothing written"
(S10), and the scratch marker under the common directory takes the opt-in
back in local mode the way it does in shared mode.
"""

import os

import pytest
from conftest import (
    branch_of,
    decision_of,
    declare_routing,
    fired,
    linked_worktree,
    local_home,
    reason_of,
    run_hook,
)

ITEM = "1788000000-a-work-item"


def bash(repo, command="git commit -m x", session="s1"):
    return {
        "tool_name": "Bash",
        "session_id": session,
        "tool_input": {"command": command},
        "cwd": str(repo),
    }


def declare_smith(repo, home, item=ITEM):
    """A declaration under `home` whose third axis says `smith`."""
    d = home / "specs" / item
    d.mkdir(parents=True, exist_ok=True)
    (d / "routing.md").write_text(
        f"# {item} -- routing\n\n"
        "| Axis | Answer |\n|---|---|\n"
        "| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
        "| Implementation | smith |\n"
        f"| Branch | {branch_of(repo)} |\n",
        encoding="utf-8",
    )
    return d


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def local(repo):
    """The `repo` fixture in local mode: `seal/` under `.git/` and nowhere
    else."""
    home = local_home(repo)
    assert not (repo / "seal").exists()
    return repo, home


# --- the commit gate: reads the declaration, and names where to write it ------


def test_the_commit_gate_is_silent_with_a_declaration_under_the_local_root(local):
    repo, home = local
    declare_routing(repo, home=home)
    assert decision_of(run_hook("commit-review-gate.py", bash(repo))) == "silent"


def test_the_commit_gate_is_silent_from_a_linked_worktree_too(repo, tmp_path):
    """The declaration lives in the main tree's common directory; the
    worktree's branch is what it names."""
    home = local_home(repo)
    other = linked_worktree(repo, tmp_path)
    declare_routing(other, home=home)
    assert decision_of(run_hook("commit-review-gate.py", bash(other))) == "silent"


def test_the_commit_gate_fires_without_one_and_names_the_resolved_path(local):
    """Q5 (a). The stop text used to spell `seal/specs/<work-item-id>/routing.md`
    whatever the mode, and a session that typed it in local mode wrote a
    declaration the gate never reads. The path is under the resolved root,
    relative to the repository, spelled the way the platform spells it."""
    repo, _ = local
    out = run_hook("commit-review-gate.py", bash(repo))
    assert fired(out)
    reason = reason_of(out)
    resolved = os.path.join(".git", "seal", "specs", "<work-item-id>", "routing.md")
    assert resolved in reason, reason
    assert "`seal/specs/<work-item-id>/routing.md`" not in reason, (
        "the literal shared-mode spelling is still offered in local mode"
    )


def test_the_stop_text_from_a_linked_worktree_is_a_path_a_person_can_type(
    repo, tmp_path
):
    """From a linked worktree the resolved root is outside the tree, so the
    relative path climbs out of it — typeable, where `.git/seal/…` names a
    FILE's child there."""
    home = local_home(repo)
    other = linked_worktree(repo, tmp_path)
    out = run_hook("commit-review-gate.py", bash(other))
    assert fired(out)
    resolved = os.path.join(
        os.path.relpath(home, other), "specs", "<work-item-id>", "routing.md"
    )
    assert resolved in reason_of(out), reason_of(out)


def test_in_shared_mode_the_stop_text_still_names_the_tree_root(repo):
    """The other half of Q5: a shared repository is told `seal/specs/…`,
    the path it always was."""
    (repo / "seal").mkdir()
    out = run_hook("commit-review-gate.py", bash(repo))
    assert fired(out)
    resolved = os.path.join("seal", "specs", "<work-item-id>", "routing.md")
    assert resolved in reason_of(out), reason_of(out)


# --- the implementer notice: prints the path it resolved --------------------


def test_the_implementer_notice_names_the_local_path(local):
    repo, home = local
    declare_smith(repo, home)
    out = run_hook("implementer-notice.py", bash(repo))
    assert "answers `Implementation` with `smith`" in out, out
    assert os.path.join(".git", "seal", "specs", ITEM, "routing.md") in out, out


# --- S10: the scratch marker takes local mode back too -----------------------


def test_a_scratch_marker_under_the_common_directory_keeps_every_gate_silent(local):
    repo, home = local
    (repo / ".git" / "specseal-scratch").write_text("", encoding="utf-8")
    declare_smith(repo, home)

    assert decision_of(run_hook("commit-review-gate.py", bash(repo))) == "silent"
    assert (
        decision_of(
            run_hook(
                "review-skill-gate.py",
                {
                    "tool_name": "Skill",
                    "session_id": "s1",
                    "tool_input": {"skill": "code-review"},
                    "cwd": str(repo),
                },
            )
        )
        == "silent"
    )
    assert run_hook("implementer-notice.py", bash(repo)) == ""
