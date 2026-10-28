"""What git's own hooks can and cannot decide about a branch switch or a
worktree creation, measured against real git.

Two rules of `docs/worktree-guard-spec.md` rest on these facts, and both
name this file on their `check:` lines. *Which tree* says no git hook can
judge a switch or a creation before it happens, so the worktree guard reads
the command. *Decided before git runs* says a hook can only take a creation
back after git made it, and a take-back cannot undo all of it, so the guard
decides a creation before git runs. The manual does not state these facts.
Phase 1 of #692 measured them on git 2.34.1, 2.39.5, 2.43.0 and 2.50.1
(`c7f4ed67:seal/specs/1790815613-a-gate-decides-at-the-moment-of-the-action-not-from-the-text/phases/phase-1.md`).
This file pins them against whatever git runs the suite, so a git release
that changes one of them turns a case red instead of silently changing what
the two rules rest on.

The three `test_no_git_refuses_a_switch_before_the_tree_moves` cases pin
*Which tree*. A switch rewrites the working tree and the index BEFORE it
updates `HEAD`, so `reference-transaction` never sees a switch it can refuse
cleanly: on 2.34-2.43 no `HEAD` line arrives at all, and on 2.50.1 it
arrives with the tree already moved. Refusing there leaves `HEAD` on the old
branch and the new branch's files checked out. A checkout and a
branch-naming rebase reach the hook the same way. If a future git refuses a
switch before the tree moves, a case goes red, and the guard's reading of
the command can be weighed against a hook again.

The four creation cases pin *Decided before git runs*:
`test_a_refused_creation_leaves_no_worktree_and_keeps_its_branch`,
`test_post_checkout_tells_a_creation_from_a_switch_and_runs_in_the_tree`,
`test_post_checkout_can_take_back_a_fresh_worktree` and
`test_what_a_take_back_cannot_undo`. A creation reaches a hook only once git
has made it. `post-checkout` can take it back, but a branch that `-b` made
stays, `-B` has already reset an existing branch, and `--no-checkout` runs
no `post-checkout` at all.

Every repository here sets `core.hooksPath` to its own absolute hooks
directory, so a person's global hooks never run in these cases.
"""

import os
import re
import stat
import subprocess
from pathlib import Path

import pytest

ZERO = "0" * 40


def _git_version():
    out = subprocess.run(
        ["git", "--version"],
        capture_output=True,
        encoding="utf-8",
        check=True,
        timeout=60,
    ).stdout
    m = re.search(r"(\d+)\.(\d+)", out)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)


# reference-transaction exists from git 2.28. Below that every case here is
# about a hook that never runs, so the module says so rather than passing.
pytestmark = pytest.mark.skipif(
    _git_version() < (2, 28),
    reason="git below 2.28 has no reference-transaction hook; "
    "the surface this file pins does not exist there",
)


def g(d, *args, check=True, env=None):
    e = dict(os.environ)
    # The cases read what the hooks wrote, and nothing about the calling
    # session may reach them.
    for k in list(e):
        if k.startswith("GIT_") and k not in ("GIT_EXEC_PATH",):
            del e[k]
    if env:
        e.update(env)
    return subprocess.run(
        ["git", "-C", str(d), *args],
        capture_output=True,
        encoding="utf-8",
        check=check,
        env=e,
        stdin=subprocess.DEVNULL,
        timeout=60,
    )


def hook(hooks, name, body):
    p = hooks / name
    p.write_text("#!/bin/sh\n" + body, encoding="utf-8")
    p.chmod(p.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def repo(tmp_path):
    """`main` with marker.txt saying `main`, and `other` saying `other`."""
    d = tmp_path / "r"
    d.mkdir()
    g(d, "init", "-q")
    g(d, "symbolic-ref", "HEAD", "refs/heads/main")
    for k, v in (
        ("user.email", "x@example.com"),
        ("user.name", "x"),
        ("commit.gpgsign", "false"),
        ("core.autocrlf", "false"),
    ):
        g(d, "config", k, v)
    hooks = tmp_path / "hooks"
    hooks.mkdir()
    g(d, "config", "core.hooksPath", str(hooks))
    (d / "marker.txt").write_text("main\n", encoding="utf-8")
    (d / "f.py").write_text("a = 1\n", encoding="utf-8")
    g(d, "add", ".")
    g(d, "commit", "-q", "-m", "init")
    g(d, "branch", "other")
    g(d, "switch", "-q", "other")
    (d / "marker.txt").write_text("other\n", encoding="utf-8")
    g(d, "commit", "-q", "-am", "other")
    g(d, "switch", "-q", "main")
    return d, hooks


# Refuses at `prepared` when a line of stdin ends with $REFUSE_SUFFIX, and
# logs, for every state, the marker file as the hook's own directory sees it.
REFUSING_RT = r"""input=$(cat)
printf '%s %s\n' "$1" "$(cat marker.txt 2>/dev/null)" >>"$RT_LOG"
printf '%s\n' "$input" | sed 's/^/  /' >>"$RT_LOG"
if [ "$1" = prepared ] && [ -n "$REFUSE_SUFFIX" ]; then
  if printf '%s\n' "$input" | grep -q -- "$REFUSE_SUFFIX\$"; then
    exit 1
  fi
fi
exit 0
"""


def head(d):
    r = g(d, "symbolic-ref", "-q", "HEAD", check=False)
    return r.stdout.strip() or g(d, "rev-parse", "HEAD").stdout.strip()


@pytest.mark.parametrize(
    "words, ref",
    [
        (["switch", "other"], "HEAD"),
        (["checkout", "other"], "HEAD"),
        # A branch-naming rebase reaches the hook the same way: its line names
        # the branch, after the tree moved (S28 of work item 1791384157,
        # executed by its second reframe on 2.50.1).
        (["rebase", "main", "other"], "refs/heads/other"),
    ],
)
def test_no_git_refuses_a_switch_before_the_tree_moves(tmp_path, words, ref):
    d, hooks = repo(tmp_path)
    log = tmp_path / "rt.log"
    hook(hooks, "reference-transaction", REFUSING_RT)
    verb = " ".join(words)
    r = g(
        d,
        *words,
        check=False,
        env={"RT_LOG": str(log), "REFUSE_SUFFIX": f" {ref}"},
    )
    text = log.read_text(encoding="utf-8") if log.exists() else ""
    head_lines = re.findall(rf"^  \S+ \S+ {re.escape(ref)}$", text, re.M)

    # Whatever git did with the hook, the working tree is on `other`.
    assert (d / "marker.txt").read_text(encoding="utf-8") == "other\n", (
        f"git {verb} left the tree on `main` after reference-transaction "
        "refused it: this git refuses a switch before the tree moves, which "
        "phase 1 of #692 found no git doing. The design's switch arm may now "
        f"be buildable as framed.\nhook log:\n{text}"
    )
    if head_lines:
        # 2.50.1: the HEAD symref line arrives, after the tree moved.
        assert r.returncode != 0
        assert head(d) == "refs/heads/main"
        assert "prepared other" in text
        # The refusal left the index on `other` too: a broken state, not a
        # prevented switch.
        assert g(d, "status", "--porcelain").stdout.strip() != ""
    else:
        # 2.34-2.43: a switch reaches reference-transaction with no line at
        # all, so a hook cannot even see it.
        assert r.returncode == 0, r.stderr
        assert head(d) == "refs/heads/other"


def test_a_refused_creation_leaves_no_worktree_and_keeps_its_branch(tmp_path):
    d, hooks = repo(tmp_path)
    hook(hooks, "reference-transaction", REFUSING_RT)
    wt = tmp_path / "wt"
    r = g(
        d,
        "worktree",
        "add",
        str(wt),
        "-b",
        "nb",
        check=False,
        env={"RT_LOG": str(tmp_path / "rt.log"), "REFUSE_SUFFIX": " HEAD"},
    )
    assert r.returncode != 0
    assert not wt.exists()
    listed = g(d, "worktree", "list", "--porcelain").stdout
    assert listed.count("worktree ") == 1, listed
    # The branch `-b` asked for is created in its own transaction first, and
    # the refusal does not take it back.
    assert (
        g(d, "rev-parse", "--verify", "-q", "refs/heads/nb", check=False).returncode
        == 0
    )


# `pwd -W` first: Git for Windows' shell prints `/c/…` for `pwd`, which no
# Windows path compares equal to, and `-W` is its spelling of `C:/…`. Every
# other shell refuses the option, and the hook falls back to `pwd -P` (#692).
POST_CHECKOUT_LOG = r"""d=$(pwd -W 2>/dev/null) || d=$(pwd -P)
printf '%s %s %s\n' "$1" "$3" "$d" >>"$PC_LOG"
exit 0
"""


def test_post_checkout_tells_a_creation_from_a_switch_and_runs_in_the_tree(tmp_path):
    d, hooks = repo(tmp_path)
    hook(hooks, "post-checkout", POST_CHECKOUT_LOG)
    log = tmp_path / "pc.log"
    env = {"PC_LOG": str(log)}
    wt = tmp_path / "wt"
    g(d, "worktree", "add", str(wt), "-b", "nb", env=env)
    g(d, "switch", "-q", "other", env=env)
    lines = log.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2, lines
    created, switched = (line.split(" ", 2) for line in lines)
    assert created[0] == ZERO
    assert created[1] == "1"
    assert Path(created[2]) == wt.resolve()
    assert switched[0] != ZERO
    assert switched[1] == "1"
    assert Path(switched[2]) == d.resolve()


# M14: post-checkout runs after a creation, cannot stop it, and can take it
# back. Phase 4 put the creation ladder there; round 1 found what a take-back
# cannot undo (the case after this one), and the owner moved the ladder back
# in front of git (`questions.md` P6, answer (a)).
UNDO = r"""case "$1" in *[!0]*) exit 0 ;; esac
new=$(pwd -P)
common=$(cd "$(git rev-parse --git-common-dir)" && pwd -P)
cd "$common" || exit 1
git worktree remove --force "$new" >/dev/null 2>&1
exit 1
"""


def test_post_checkout_can_take_back_a_fresh_worktree(tmp_path):
    d, hooks = repo(tmp_path)
    hook(hooks, "post-checkout", UNDO)
    for name, args in (("wt1", ["-b", "nb"]), ("wt2", ["other"])):
        r = g(d, "worktree", "add", str(tmp_path / name), *args, check=False)
        assert r.returncode != 0
        assert not (tmp_path / name).exists()
    listed = g(d, "worktree", "list", "--porcelain").stdout
    assert listed.count("worktree ") == 1, listed
    # The branch `-b` made stays; the existing one is free to check out again.
    assert (
        g(d, "rev-parse", "--verify", "-q", "refs/heads/nb", check=False).returncode
        == 0
    )
    (hooks / "post-checkout").unlink()
    g(d, "worktree", "add", "-q", str(tmp_path / "again"), "other")


def test_what_a_take_back_cannot_undo(tmp_path):
    """Why no creation is judged after git makes it (P6): `-B` has reset an
    existing branch before `post-checkout` runs, and `--no-checkout` runs no
    `post-checkout` at all (round 1 of #692, executed on 2.50.1)."""
    d, hooks = repo(tmp_path)
    log = tmp_path / "pc.log"
    hook(hooks, "post-checkout", UNDO.replace("exit 1\n", 'echo ran >>"$PC_LOG"\n'))
    env = {"PC_LOG": str(log)}
    other = g(d, "rev-parse", "other").stdout.strip()
    g(d, "worktree", "add", "-B", "other", str(tmp_path / "wt1"), "main", env=env)
    assert not (tmp_path / "wt1").exists()
    assert g(d, "rev-parse", "other").stdout.strip() != other
    log.unlink()
    g(d, "worktree", "add", "--no-checkout", str(tmp_path / "wt2"), "-b", "n2", env=env)
    assert (tmp_path / "wt2").exists()
    assert not log.exists()
