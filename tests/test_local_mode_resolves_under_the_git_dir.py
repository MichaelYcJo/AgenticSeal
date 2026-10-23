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

The commit gate's cases are in `tests/test_commit_review_gate.py`'s
`Test_main`, and the `local` fixture in `tests/conftest.py` (#942's phase 6).
"""

import os

from conftest import (
    branch_of,
    decision_of,
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
