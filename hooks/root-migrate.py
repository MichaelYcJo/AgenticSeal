#!/usr/bin/env python3
"""SessionStart: a layout an earlier release wrote moves into the current one,
once per repository.

`moves` lists the units, each a `(kind, src, dst)` of repository-relative
paths, and this tree has none. The 0.3.x layout is not a unit: no code of the
plugin opens its two directories, a top-level `specs/` may be another tool's,
and README.md *Coming up from 0.3.x* gives the commands that move it by hand
(`docs/one-root-by-lifetime.md`, "The plugin writes only to its own root").

Writing to a tree unasked is licensed on three grounds: the tree is the
plugin's own, every step is a staged `git mv` or a rewrite of a file git
already tracks, and `git diff --cached` shows the whole of it with the old
text safe in history. The notice ends "review the diff and commit" because
the write is the beginning of a review.

Boundaries, each pinned in `tests/test_root_migrate.py`:

  - **never over uncommitted work** — anything `git status --porcelain`
    reports under a directory a unit comes from, or a git that cannot answer,
    refuses the whole move with one line and stamps nothing
  - **only what git tracks** — a unit's files come from `git ls-files`, so an
    ignored file under a source directory is not moved and stays where it is,
    and the directory may remain on disk holding nothing else
  - **once per repository** — a completed move stamps the marker, and so does
    a repository that has nothing old left and a root at EITHER place,
    `<repo>/seal/` or `<git-common-dir>/seal/`, so switching to an old branch
    later does not move it again — into a tree that local mode (#80) chose
    to keep clean, in the second case
  - **a stopped move resumes** — a step that fails stops the run, prints what
    moved and what did not, and stamps nothing; the next session start moves
    what remains and stamps only when nothing old is left
  - **silent when there is nothing to do**
"""

# RIDER: this file is a reader of a layout an earlier release wrote, and of
# nothing the current layout holds. It can be deleted once no repository is
# left to migrate, and nothing else has to change when it goes;
# `hooks/dispatch.py`'s session-start group is the one place that names it.

import json
import os
import posixpath
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import console
import optin

HOOKS = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(os.path.expanduser("~"), ".claude", "specseal")
MARKER = os.path.join(STATE_DIR, "root-migrated")
TEMPLATE = os.path.join(HOOKS, "..", "templates", "seal-README.md")

NEW = optin.HOME


class MoveError(Exception):
    """A unit that did not move. `resumable` says whether the next session
    start can pick it up unaided; a destination already holding the file, or
    a `seal` that is a file, needs a person first, and the line says so
    instead of promising a continuation that never comes."""

    def __init__(self, path, error, resumable=True):
        super().__init__(f"{path}: {error}")
        self.path = path
        self.error = error
        self.resumable = resumable


def attempted(root):
    try:
        with open(MARKER, encoding="utf-8") as f:
            # exempt from splitlines: a marker file of root paths
            return root in f.read().splitlines()
    except OSError:
        return False


def stamp(root):
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        with open(MARKER, "a", encoding="utf-8") as f:
            f.write(root + "\n")
    except OSError:
        pass


def under(root, rel):
    """The disk path of a `/`-joined repository-relative path."""
    return os.path.join(root, *rel.split("/"))


def git(root, *args):
    return subprocess.run(
        ["git", "-C", root, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )


def sources(units):
    """The directories the units come from, each once and sorted: what
    `dirty` reads and what `run_moves` removes once the moves empty it."""
    return sorted({posixpath.dirname(src) for _, src, _ in units})


def dirty(root, units):
    """True when anything under a directory the units come from is
    uncommitted — or git cannot say. Work in progress outranks the move, and
    an unanswerable question is treated as work in progress: moving on a
    guess is the one direction this hook must never fail in.

    One shape is not work in progress: a staged rename or deletion with a
    clean worktree (`R ` and `D ` in porcelain's two columns). That is what
    a stopped run of this hook leaves behind, and a resume has to see past
    its own earlier steps or a stopped move can never finish. Anything with
    a worktree change, anything untracked, and anything staged as an
    addition or a modification still refuses.

    A `git ls-files` that cannot answer is the same case, because the units
    are what it lists, and it is refused here before a guess can move
    anything.
    """
    roots = sources(units)
    if any(tracked_names(root, rel) is None for rel in roots):
        return True
    try:
        r = git(root, "status", "--porcelain", "--", *roots)
    except (OSError, subprocess.SubprocessError):
        return True
    if r.returncode != 0:
        return True
    # exempt from splitlines: git output
    for line in r.stdout.splitlines():
        if len(line) < 2:
            continue
        x, y = line[0], line[1]
        if y != " " or x not in "RD":
            return True
    return False


def tracked_names(root, rel):
    """The top-level names git tracks under `rel`, sorted — or None when git
    cannot say.

    Every step of the move is a `git mv`, so a unit is what git tracks. An
    ignored file directly under a source directory (`.DS_Store` is macOS's
    default) passes `dirty()`, which reads porcelain, and then stops `git mv`
    for good: every session start met the same unit, and the tree stayed
    half-moved. Listing the directory was the defect; git's own list is the
    fix.
    """
    try:
        r = git(root, "ls-files", "-z", "--", rel)
    except (OSError, subprocess.SubprocessError):
        return None
    if r.returncode != 0:
        return None
    prefix = rel + "/"
    names = set()
    for path in r.stdout.split("\0"):
        if path.startswith(prefix):
            head = path[len(prefix) :].split("/", 1)[0]
            if head:
                names.add(head)
    return sorted(names)


def entries(root, rel):
    """What is under `rel` as units: git's list, or the directory listing when
    git cannot answer — `dirty()` reads as dirty then, so nothing moves."""
    names = tracked_names(root, rel)
    if names is not None:
        return names
    try:
        return sorted(os.listdir(under(root, rel)))
    except OSError:
        return []


def moves(root):
    """The units still to move, in the order they move, as (kind, src, dst).

    A `readme` unit's destination is then rewritten from the template. The
    list is computed from what git tracks as it stands, which is what makes a
    stopped move resume: a unit that already moved is not there to be listed.
    No layout this tree reads is still to move, so the list is empty.
    """
    return []


def git_mv(root, src, dst):
    """One staged rename. `git mv` does not create its destination's parent,
    and a `seal` that is a file makes creating it fail — inside the `try`,
    because an exception out of here ends the whole migration under the
    dispatcher, with nothing said until the turn ends (#28)."""
    parent = os.path.dirname(under(root, dst))
    try:
        os.makedirs(parent, exist_ok=True)
    except OSError as exc:
        raise MoveError(
            src, f"cannot create {os.path.dirname(dst)}/: {exc}", resumable=False
        ) from exc
    try:
        r = git(root, "mv", src, dst)
    except (OSError, subprocess.SubprocessError) as exc:
        raise MoveError(src, str(exc)) from exc
    if r.returncode != 0:
        raise MoveError(src, (r.stderr or r.stdout).strip() or f"exit {r.returncode}")


def taken(src, dst):
    """The error for a destination that already holds a file: `git mv` would
    say `destination exists` and the plain tail would promise a continuation
    that never comes, because the state does not change by itself."""
    return MoveError(
        src,
        f"{dst} already exists — keep one by hand: git rm {src} if {dst} is "
        f"the newer, or git rm {dst} to let the move bring the old one over",
        resumable=False,
    )


def move(root, src, dst):
    """`src` to `dst`, whole when nothing is at `dst` yet.

    When `dst` already exists — the state a stopped run leaves — a directory
    is moved file by file, in the order git lists them, because `git mv dir
    existing-dir` would put it INSIDE the destination. A file already at its
    destination is the person's to settle (a merge of a branch bootstrapped
    on the new layout leaves exactly that), and is named rather than tried.
    Then every directory under `src` that holds nothing when the walk reaches
    it is removed, the deepest first and `src` last, whichever run emptied
    it, unless its removal fails; one an ignored file holds stays, with every
    directory above it. Two limits, not guarded. A Windows junction placed
    under `src` by hand, which git does not track, is walked into, and the
    empty directories behind it are removed too. Where the removal of a
    directory fails, as on Windows when another process holds it open, that
    directory and every one above it stay, and nothing is removed by mistake.
    """
    if not os.path.isdir(under(root, src)):
        if os.path.exists(under(root, dst)):
            raise taken(src, dst)
        git_mv(root, src, dst)
        return
    if not os.path.exists(under(root, dst)):
        git_mv(root, src, dst)
        return
    r = git(root, "ls-files", "-z", "--", src)
    if r.returncode != 0:
        raise MoveError(src, (r.stderr or "").strip() or "git ls-files failed")
    for rel in sorted(p for p in r.stdout.split("\0") if p):
        target = dst + rel[len(src) :]
        if os.path.exists(under(root, target)):
            raise taken(rel, target)
        git_mv(root, rel, target)
    # Each directory is listed again when the walk reaches it. The lists
    # `os.walk` yields were read before the subdirectories below were
    # removed, so they still name them, and a directory that had held one
    # stayed on disk empty (#1016, #1018).
    for here, _, _ in os.walk(under(root, src), topdown=False):
        try:
            if not os.listdir(here):
                os.rmdir(here)
        except OSError:
            pass


def rewrite_readme(root, dst):
    """A `readme` unit's second half: the moved README becomes the template's
    text.

    A template that cannot be read leaves the moved file as it was — a README
    describing the old layout is the state Q5 weighed, and it beats stopping
    the move for a file that is not the move.
    """
    try:
        with open(TEMPLATE, encoding="utf-8") as f:
            text = f.read()
        with open(under(root, dst), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        return
    git(root, "add", "--", dst)


def run_moves(root, units):
    """(units moved, the error that stopped the run or None)."""
    done = 0
    for kind, src, dst in units:
        try:
            move(root, src, dst)
            if kind == "readme":
                rewrite_readme(root, dst)
        except MoveError as exc:
            return done, exc
        done += 1
    for old in sources(units):
        path = under(root, old)
        # A link is never this cleanup's to remove. POSIX `rmdir` refuses one
        # with ENOTDIR; Windows' `RemoveDirectoryW` removes a directory link
        # itself, whatever is behind it, and deleted a team's linked `specs/`
        # from the working tree (PR #700's windows leg, #688; contract
        # rule 13).
        if os.path.islink(path):
            continue
        try:
            os.rmdir(path)
        except OSError:
            pass  # something else is in it, or it is already gone
    return done, None


def has_root(root):
    """True when `seal/` is a directory at either place the root can be."""
    if os.path.isdir(under(root, NEW)):
        return True
    common = optin.git_common_dir(root)
    return bool(common) and os.path.isdir(os.path.join(common, NEW))


def say(message):
    print(json.dumps({"systemMessage": message}))


def listed(dirs):
    """`a/` or `a/ and b/`, the way the notices name directories."""
    return " and ".join(f"{d}/" for d in dirs)


def main():
    """Move what is still to move once, and say in one line what moved."""
    try:
        event = json.load(sys.stdin) or {}
        cwd = event.get("cwd")
    except (ValueError, AttributeError):
        return
    if not cwd or not os.path.isdir(cwd):
        return
    # NOT `optin.opted_in`: a layout still to move is one the gates may not
    # read as opted in, and a hook gated on the opt-in would never meet it.
    root = optin.repo_root(cwd)
    if not root:
        return

    units = moves(root)
    if not units:
        # Nothing old left. Stamped so that checking out a branch that still
        # carries an old layout later finds the once-per-repository rule
        # already answered, rather than a move staged onto that branch.
        #
        # Either place, read directly rather than through `optin.home_at`,
        # so the scratch opt-out does not hide the root from this rule. A
        # local-mode repository (#80) keeps the root under the git directory
        # and was never stamped by a tree-only test: it re-listed the old
        # names at every session start, and an old branch checked out later
        # was moved INTO the tree the person chose to keep clean.
        if not attempted(root) and has_root(root):
            stamp(root)
        return
    if attempted(root):
        return  # once per repository; the silent gates are the backstop (Q8)
    if dirty(root, units):
        say(
            f"specseal: the old layout under {listed(sources(units))} holds "
            "uncommitted changes — not touching work in progress. Commit, then "
            f"the next session start moves it into {NEW}/."
        )
        return

    done, error = run_moves(root, units)
    if error is not None:
        tail = (
            "The next session start continues."
            if error.resumable
            else "Settle that by hand, then the next session start continues."
        )
        say(
            f"specseal: moved {done} of {len(units)} into {NEW}/ and stopped at "
            f"{error.path}: {error.error}. {tail}"
        )
        return
    stamp(root)
    say(
        f"specseal: moved {listed(sources(units))} into {NEW}/ — review the diff "
        "and commit"
    )


if __name__ == "__main__":
    console.to_utf8()
    main()
