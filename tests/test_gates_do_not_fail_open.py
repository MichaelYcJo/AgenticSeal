"""The reading direction: a reader that cannot decode must not answer "nothing".

`tests/test_console.py` holds the writing direction — a gate that
raises while printing dies with empty stdout. This file holds the other one,
which is quieter and worse.

`subprocess.run(..., text=True)` decodes a child's output with whatever
locale the parent had. git speaks UTF-8 on every platform. When the decode fails, the
exception is raised on subprocess's **reader thread and does not propagate**:
the call returns normally with `stdout` set to `None`. Nothing crashes. The
guard reads no other session and reports a single stream; the gate resolves no
repository and stays silent; the check finds no round record and exits 0.

Every one of those is an allow, produced by a reader that was never told what
encoding its input is in. `hooks/worktree-guard.py` names this direction itself
as the one to avoid.

Platform-independent by construction: the `None` state is produced directly,
because that is the state the reader thread leaves behind, and reproducing the
thread death would need a locale the test cannot set portably.

The guard's process probe in this direction is
`tests/test_worktree_guard.py`'s
`Test_lease_owner_alive::test_the_process_probe_survives_output_it_cannot_decode`
(#942's phase 6).
"""

import io
import json
import os
import sys

from conftest import git_repo, load

ROOT = os.path.join(os.path.dirname(__file__), "..")


optin = load("hooks/optin.py", "specseal_optin_failopen")


def test_the_commit_gates_hint_survives_a_root_with_no_relative_spelling(
    tmp_path, monkeypatch, capsys
):
    r"""Round 1 of #80, 🔴 1. The stop text names the declaration under the
    resolved root, relative to the repository, and `os.path.relpath` is what
    builds that. On Windows a linked worktree on another drive than the main
    tree makes `ntpath.relpath` raise (`ValueError: path is on mount 'D:',
    start on mount 'C:'`). The gate built the hint before it had judged
    anything, so the exception left `main()`, `dispatch.py`'s crash isolation
    swallowed it, and empty stdout is an allow: a commit went through in an
    opted-in repository, unjudged.

    The raise is induced rather than found, so the case runs on every leg.
    What is asserted is the direction: the gate still stops, and the path it
    names is the absolute one — there is no relative spelling of a path on
    another drive, and the absolute path is the one to type.
    """
    gate = load("hooks/commit-review-gate.py", "specseal_gate_failopen")
    repo = git_repo(tmp_path / "repo")
    (repo / ".git" / "seal").mkdir()
    home = optin.home(str(repo))
    assert home and os.path.isabs(home), home

    def refuses(path, start=None):
        raise ValueError("path is on mount 'D:', start on mount 'C:'")

    monkeypatch.setattr(os.path, "relpath", refuses)
    monkeypatch.setattr(
        sys,
        "stdin",
        io.StringIO(
            json.dumps(
                {
                    "tool_name": "Bash",
                    "session_id": "failopen-relpath",
                    "tool_input": {"command": "git commit -m x"},
                    "cwd": str(repo),
                }
            )
        ),
    )
    gate.main()
    out = capsys.readouterr().out
    assert out.strip(), (
        "the gate printed nothing — an allow for a commit it never judged"
    )
    decision = json.loads(out)["hookSpecificOutput"]
    assert decision["permissionDecision"] in ("deny", "ask"), decision
    expected = os.path.join(home, "specs", "<work-item-id>", "routing.md")
    assert expected in decision["permissionDecisionReason"], decision[
        "permissionDecisionReason"
    ]
