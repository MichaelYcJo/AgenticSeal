#!/usr/bin/env python3
"""Add the release's commit to `dist`, the branch the plugin directory reads.

The directory's submission form does not answer in time for this
repository's whole tree, and answers for the tree without its suites and
records. So the directory tracks `dist`, a branch whose tree at each
release is `git archive` of the release's tag. The paths that leave are the
ones `.gitattributes` marks `export-ignore`, read at the tag, and this script
holds no list of them.

**The tree is the tag's tree less what the archive leaves out.** The tag is
read into an index of the script's own, every path `git archive` of the tag
does not list is removed from that index, and `git write-tree` writes it. So
each file `dist` holds has the tag's own mode and object, and the archive
decides membership: a directory pattern such as `/tests/` drops every file
under it, which `git check-attr` asked of one file does not answer.

**One commit per release, and never a rewrite.** The directory serves a
scanned commit of the branch it tracks, and a rewritten branch would orphan
it. The tip of `dist` is read from `origin` with `git ls-remote` and fetched,
and the new commit names it as its one parent; where `origin` has no `dist`,
the commit has no parent. The tag's commit is not a parent, so `dist`'s
history does not carry `main`'s: the message's first line is `dist: <tag>`,
and its body names the tag's commit instead. It is pushed as `<commit>:refs/heads/dist` without force, so where `dist` moved
after its tip was read, git refuses the push and the run is red.

**A re-run makes nothing.** Where the tip's tree is already the tree built
for the tag, nothing is committed or pushed, and the run says so.

`DRY_RUN=1` builds the tree and prints the commit it would push, and
commits and pushes nothing, for the reason `close_issues_on_release.py`'s
docstring gives.

**Limit: the tag is taken as the newest release.** A tag pushed by hand for
an older version adds a commit whose tree is that older release, and the
directory picks it up as the newest. The hand-pushed tag is the repair path
for a failed tag step, which names the newest release there.

The commit's author and committer are the identity git is given, by its
config or its environment; the workflow's `dist` job names the GitHub
Actions bot in the step's environment.

Environment: `TAG`, the tag the `publish` job passed on, and `DRY_RUN`.

Exit codes: 0 where a commit was pushed, none was needed, or the run was
dry -- 1 where a git command failed, the push refused among them, with git's
error printed, a tag the checkout cannot resolve among them -- 2 where `TAG`
is unset or empty.
"""

import io
import os
import subprocess
import sys
import tarfile
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from; it
# loads every other module this script reads.
sys.path.insert(0, os.path.join(HERE, "..", "..", "lib"))
import sibling  # noqa: E402

console = sibling.load("lib/console.py")

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REMOTE = "origin"
BRANCH = "refs/heads/dist"


class GitFailed(Exception):
    """A git command that exited non-zero, with what it printed."""


def git(*args, index=None, stdin=None):
    """`git` run in the repository at `ROOT`, under the index file `index`
    where one is named; its standard output as bytes."""
    env = dict(os.environ)
    if index is not None:
        env["GIT_INDEX_FILE"] = index
    done = subprocess.run(
        ["git", "-C", ROOT, *args], input=stdin, capture_output=True, env=env
    )
    if done.returncode:
        said = done.stderr.decode("utf-8", "replace").strip()
        raise GitFailed(f"git {args[0]} failed: {said}")
    return done.stdout


def text(*args, **kwargs):
    return git(*args, **kwargs).decode("utf-8").strip()


def archived(tag):
    """Every file path `git archive` of `tag` writes."""
    with tarfile.open(fileobj=io.BytesIO(git("archive", "--format=tar", tag))) as tar:
        return {member.name for member in tar.getmembers()}


def archive_tree(tag):
    """The tree of `tag` less every path its archive does not hold, written
    from an index of this call's own, so the checkout's index is left as it
    was."""
    kept = archived(tag)
    with tempfile.TemporaryDirectory() as scratch:
        index = os.path.join(scratch, "index")
        git("read-tree", tag, index=index)
        listed = git("ls-files", "-z", index=index).decode("utf-8").split("\0")
        gone = "".join(f"{path}\0" for path in listed if path and path not in kept)
        git(
            "update-index",
            "--force-remove",
            "-z",
            "--stdin",
            index=index,
            stdin=gone.encode("utf-8"),
        )
        return text("write-tree", index=index)


def remote_tip():
    """The commit `dist` names on `origin`, fetched here, or "" for none."""
    heads = text("ls-remote", "--heads", REMOTE, BRANCH)
    if not heads:
        return ""
    git("fetch", "-q", REMOTE, BRANCH)
    return heads.split()[0]


def main():
    tag = os.environ.get("TAG", "").strip()
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if not tag:
        print("TAG is empty, so there is no release to add to dist")
        return 2
    if dry:
        print("DRY_RUN — nothing will be pushed")
    try:
        commit = text("rev-parse", "--verify", f"{tag}^{{commit}}")
        tree = archive_tree(tag)
        tip = remote_tip()
        if tip and text("rev-parse", f"{tip}^{{tree}}") == tree:
            print(
                f"nothing to push: dist's tip {tip} already holds the archive of {tag}"
            )
            return 0
        on = f"on {tip}" if tip else "as the first commit of dist"
        if dry:
            print(f"would push a commit of tree {tree} for {tag} {on}")
            return 0
        parent = ["-p", tip] if tip else []
        made = text(
            "commit-tree",
            tree,
            *parent,
            "-m",
            f"dist: {tag}",
            "-m",
            f"The tree of `git archive {tag}`, the release tagged at {commit}.",
        )
        git("push", REMOTE, f"{made}:{BRANCH}")
    except GitFailed as failed:
        print(f"nothing was pushed for {tag}: {failed}")
        return 1
    print(f"pushed {made} to dist for {tag}, {on}")
    return 0


if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
