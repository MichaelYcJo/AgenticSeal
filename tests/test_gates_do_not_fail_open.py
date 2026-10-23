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
"""

import io
import json
import os
import subprocess
import sys

import pytest
from conftest import git_repo, load

ROOT = os.path.join(os.path.dirname(__file__), "..")
KOREAN = "한글"


optin = load("hooks/optin.py", "specseal_optin_failopen")


def test_a_reader_that_decoded_nothing_answers_empty_rather_than_raising(monkeypatch):
    """The `None` stdout, produced directly.

    This is what the dead reader thread leaves behind, and it is the state that
    made `optin.repo_root` raise `AttributeError` out of the commit gate — a
    PreToolUse hook exiting non-zero is a non-blocking error, so the command it
    was judging went through unjudged.

    The module's own docstring states the direction: everything here fails
    toward "not opted in", and that is `""`, not an exception.
    """

    def decoded_nothing(*args, **kwargs):
        return subprocess.CompletedProcess(args, 0, stdout=None, stderr=None)

    monkeypatch.setattr(optin.subprocess, "run", decoded_nothing)
    assert optin.repo_root(str(ROOT)) == ""
    assert optin.opted_in(str(ROOT)) is False
    assert optin.parity_config(str(ROOT)) == ""


def test_a_repository_whose_path_the_locale_cannot_carry_still_resolves(tmp_path):
    """The encoding half, asked of the answer rather than of the source.

    Under `text=True` this returns one of two wrong things depending on the
    ambient codepage: nothing at all where the decode fails outright (cp949,
    and the reader-thread death above), or a plausible-looking path that does
    not exist where the codepage decodes every byte to something (cp1252 turns
    the UTF-8 bytes of Korean into Latin-1 letters, and `opted_in` then answers
    False about a repository that is opted in).

    Asserting that the answer names a directory that EXISTS catches both, and
    on a UTF-8 locale it is a no-op — the same shape as every other
    substitution in this work item.
    """
    repo = git_repo(tmp_path / KOREAN / "repo")
    (repo / "seal").mkdir()
    got = optin.repo_root(str(repo))
    assert got, "the root came back empty for a repository that is right there"
    assert os.path.isdir(got), f"resolved to a directory that does not exist: {got!r}"
    assert os.path.normpath(got) == os.path.normpath(str(repo))
    assert optin.opted_in(str(repo)) is True


def test_the_process_probe_survives_output_it_cannot_decode(monkeypatch):
    """`tasklist` is the only process probe Windows has — there is no `ps` and
    no `/proc` — and it answers in the OEM codepage, so it is the one reader in
    this tree whose source is not UTF-8.

    Under `text=True` its reader thread died and `r.stdout` came back `None`,
    which `.splitlines()` then hit OUTSIDE the `try`. The guard's session
    detection went blind on exactly the consoles most likely to be non-UTF-8,
    and blind means `reliable` is False, which means every branch switch
    reaches the cannot-tell arm.
    """
    guard = load("hooks/worktree-guard.py", "specseal_guard_failopen")
    if not hasattr(guard, "lease_owner_alive"):
        pytest.skip("the probe moved; this case names it by function")

    def decoded_nothing(*args, **kwargs):
        return subprocess.CompletedProcess(args, 0, stdout=None, stderr=None)

    monkeypatch.setattr(guard.subprocess, "run", decoded_nothing)
    monkeypatch.setattr(guard.sys, "platform", "win32")
    # False — "this pid is not running" — and not a traceback. Answering the
    # question wrongly is a separate matter from failing to answer it at all,
    # and only the second one takes the caller down with it.
    assert guard.lease_owner_alive(1) is False


def test_the_common_directory_reader_that_decoded_nothing_answers_empty(
    tmp_path, monkeypatch
):
    """S10 (#80). `git_common_dir` has the same `subprocess.run` shape as
    `repo_root` and, for a tree whose `.git` is a FILE, the same dead reader
    thread: `stdout` comes back `None`. That reads as "" — no common
    directory, so no local root, so not opted in — and never raises."""
    linked = tmp_path / "linked"
    linked.mkdir()
    (linked / ".git").write_text(
        "gitdir: /nowhere/.git/worktrees/linked\n", encoding="utf-8"
    )

    def decoded_nothing(*args, **kwargs):
        return subprocess.CompletedProcess(args, 0, stdout=None, stderr=None)

    monkeypatch.setattr(optin.subprocess, "run", decoded_nothing)
    assert optin.git_common_dir(str(linked)) == ""
    assert optin.home_at(str(linked)) == ""
    assert optin.home(str(linked)) == ""
    assert optin.opted_in(str(linked)) is False


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
