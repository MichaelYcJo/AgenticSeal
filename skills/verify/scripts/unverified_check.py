#!/usr/bin/env python3
"""agentic unverified — read what a closing memo recorded as unverified, and fail
on a record that cannot be read.

`verify` condition 4 lets a claim go out unproven as long as the row names who
answers it, and a row nobody reads again stays open after its answer has
come. A closing memo's row can say nobody has seen the gates render in an
interactive TUI and name the user as the answerer; months later the user
meets exactly that, from the other side, and asks why every gate renders as
yes/no. The record is accurate and no procedure closes it.

So this reads every `## Not verified` section and reports what is still open.
It does **not** fail because items are open. Many are open at any time, and
a build that goes red for an honest `unverified` row teaches
people to write none, which voids the condition it is defending. Counting them
is what `agentic unverified agentory/threads/` is for; no number is repeated in prose here,
because a number in a comment is right for one commit and nobody recounts it.

It fails for what the author can always fix: a section that cannot be read.
A tolerant parser reports zero there, and zero reads as "everything has been
closed", the worst available failure, because it is indistinguishable from
success.

A row or a closing memo deleted rather than closed is read by nobody here:
the proofer reads it in the closing memo's diff (`skills/implement/SKILL.md`
*4. The closing memo*).

The reader is `lib/gaps.py`, which states how a row closes and which
`agentic settle` reads a memo through as well; this command walks a tree for every `gaps.md`, reads each through it,
and prints what it found. Deliberately a text scan of markdown, not a parser
library: the gates here are stdlib-only, and the format it accepts is one
line long. That format is strict on purpose — see `lib/gaps.py#check_file`.

Exit codes: 0 the record is readable (open items are reported, not punished) ·
1 a section could not be read · 2 the path or arguments were unusable, which
includes a scan that found no closing memo at all. One state of an `agentory/`
root's own `threads` path is exit 0 instead, and says so: the path holding no
work item, empty or absent, which is the state a complete settle ends in
(`settled_root`).
"""

import argparse
import os
import sys

# `lib/` beside this script. The memo's reader, `lib/gaps.py`, the line
# that names a file to GitHub, `lib/console.py#annotate`, beside the
# streams' answer, `lib/console.py#to_utf8`, the path as git
# spells it, `lib/gitcmd.py#git_path`, the `Reference specs` key's reader and
# the root's resolver are loaded through `lib/sibling.py`.
HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "..", "..", "lib")
sys.path.insert(0, LIB)
import sibling  # noqa: E402

GAPS = sibling.load("lib/gaps.py")
console = sibling.load("lib/console.py")
GITCMD = sibling.load("lib/gitcmd.py")
# `lib/optin.py`, whose `WORK_ITEMS` names the directory under an `agentory/`
# root that holds the threads, and whose `GAPS` names a thread's closing
# memo.
OPTIN = sibling.load("lib/optin.py")
SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "venv",
}


def overviews(paths):
    """Every gaps.md under the given paths, in a stable order.

    **A walk leaves the reference roots out**: a project's own
    `specs/` is a team's document, read as history and never as this
    plugin's record, so a malformed `## Not verified` there is not a finding.
    A path NAMED, a file or a directory inside a reference root, is read as
    named — the person asked for it."""
    found = []
    for p in paths:
        # Each argument is read at its real path. `reference_rule` measures
        # the path against the top `git rev-parse --show-toplevel` gives,
        # which has its links resolved, so a tree reached through a link and
        # read as named would leave no team's `specs/` out of the walk.
        p = os.path.realpath(p)
        if os.path.isfile(p):
            found.append(p)
            continue
        skip = reference_rule(p)
        for root, dirs, files in os.walk(p):
            dirs[:] = sorted(
                d
                for d in dirs
                if d not in SKIP_DIRS and not (skip and skip(os.path.join(root, d)))
            )
            if OPTIN.GAPS in files:
                found.append(os.path.join(root, OPTIN.GAPS))
    return sorted(dict.fromkeys(found))


def config_at(top):
    """`(lib/config.py, the agentory/ root, its name in the tree)` for the
    repository at `top`: the root as `lib/optin.py#home_at` resolves it, and
    the name `lib/optin.py#home_name` gives, "" where the root is local or
    absent."""
    config = sibling.load("lib/config.py")
    resolver = sibling.load("lib/optin.py")
    common = resolver.git_common_dir(top)
    return config, resolver.home_at(top, common), resolver.home_name(top, common)


def references_at(top):
    """`(lib/config.py, roots, name)` for the repository at `top` — the
    module holding `under_reference_root`, what the key names under the root
    `lib/optin.py#home_at` resolves, and that root's name in the tree
    (`config_at`) — or None where one of the two raises while it loads or
    reads. An absent one is `lib/sibling.py#load`'s sentence at exit 2.

    None prunes nothing, which reads more and never less: the walk leaves
    no reference root out, rather than refusing a run that needed none of
    this. Read once per path a run is handed."""
    try:
        config, home, name = config_at(top)
        return config, config.reference_roots(home, name), name
    except (OSError, ImportError, AttributeError):
        return None


def reference_rule(start):
    """A predicate on a disk directory — True for one the walk from `start`
    leaves out — or None where nothing is left out: `start` outside a git
    repository or a git that did not answer, which `lib/optin.py#repo_root`
    reads alike, a `lib/` that will not load, or `start` itself inside a
    reference root, which the person named and so asked for. Every
    directory the walk meets is under `start`, so under `top` as well, and
    has a repository-relative form."""
    top = OPTIN.repo_root(start)
    if not top:
        return None
    loaded = references_at(top)
    if loaded is None:
        return None
    config, roots, name = loaded
    if config.under_reference_root(repo_relative(start, top), roots, name):
        return None

    def skip(directory):
        return config.under_reference_root(repo_relative(directory, top), roots, name)

    return skip


def repo_relative(path, root):
    r"""`path` as a repo-relative git path, or None when it has no relative form.

    The composition `git_path(os.path.relpath(...))`, `lib/gitcmd.py`'s
    helper, is not safe on its own:
    `relpath` raises across drives, and a `ValueError` raised mid-report
    kills a run that has already printed part of its rows, which
    `display_path` beside this one exists to prevent.

    None rather than a fallback, because the question is about a path INSIDE
    a repository. A path on another volume is not inside this one -- a
    working tree cannot span drives -- so there is no answer to degrade to,
    and inventing one is the quiet zero this tool refuses. `reference_rule`
    asks it only of paths under the top `lib/optin.py#repo_root` found for
    them.
    """
    try:
        return GITCMD.git_path(os.path.relpath(path, root))
    except ValueError:
        return None


def display_path(path, start):
    r"""`path` relative to `start`, or absolute when there is no relative form.

    `os.path.relpath` raises `ValueError` on Windows when the two are on
    different drives, and this is the reporting footing for every line the
    tool prints. Running `agentic unverified D:\repo\specs` from `C:\` is
    an ordinary thing to do, and unguarded it dies with a traceback before
    printing a single row. The absolute path is a worse answer than a
    relative one and a far better one than no output at all.
    """
    try:
        return os.path.relpath(path, start)
    except ValueError:
        return os.path.abspath(path)


def unique_by_target(paths):
    """One path per real file, the real file's own, in sort order.

    A tracked symbolic link and the file it points at are one record and two
    paths. Counting both doubles its open items. The path kept is the one
    `os.path.realpath` answers, whichever path the scan reached the file by,
    and it may lie outside the scanned path, or outside the repository."""
    return sorted({os.path.realpath(p) for p in paths})


def named_root(parent):
    """Whether the directory PARENT carries the root's name,
    `lib/optin.py#HOME`. Only the name is read: whether PARENT is that root
    is not asked. PARENT is a directory on disk."""
    return os.path.basename(parent) == OPTIN.HOME


def settled_root(path):
    """Whether `path` is an `agentory/` root's own `threads` directory with no work
    item under it — empty on disk, or absent while the root is there.

    That is the state a complete settle reaches, and it is two states: the
    tree that ran `agentic settle --apply` holds an empty `agentory/threads/`, and a
    fresh checkout of the commit holds none, because git keeps no empty
    directory. A person who runs `agentic unverified agentory/threads/`
    after the settle hands this tool that path, and reading it as a typo would
    refuse a finished settle. Only this one path is settled: any other path
    that is missing is still refused, which is what keeps `threads/ thraeds/`
    from passing in silence.
    """
    p = os.path.abspath(path)
    parent = os.path.dirname(p)
    if os.path.basename(p) != OPTIN.WORK_ITEMS or not os.path.isdir(parent):
        return False
    if not named_root(parent):
        return False
    if not os.path.isdir(p):
        return True
    return not any(os.path.isdir(os.path.join(p, n)) for n in os.listdir(p))


SETTLED = (
    "agentic unverified: {path} holds no work item and its `agentory/` root is "
    "there — the state a complete settle ends in, so there is nothing to read"
)


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="agentic unverified",
        description="Report open `## Not verified` items; fail on a record "
        "that cannot be read.",
    )
    ap.add_argument("path", nargs="*", default=["."])
    args = ap.parse_args(argv)

    missing = [p for p in args.path if not os.path.exists(p) and not settled_root(p)]
    if missing:
        print(f"agentic unverified: no such path: {missing[0]}", file=sys.stderr)
        return 2

    files = overviews(args.path)
    cwd = os.getcwd()
    total_open = total_closed = 0
    bad = []
    for path in unique_by_target(files):
        rel = display_path(path, cwd)
        open_rows, closed_rows, errors = GAPS.check_file(path)
        total_open += len(open_rows)
        total_closed += len(closed_rows)
        for line_no, message in errors:
            bad.append(console.annotate("error", rel, line_no, message))
        if not errors and (open_rows or closed_rows):
            print(f"  {rel}  {len(open_rows)} open · {len(closed_rows)} closed")
            for _, item, who in open_rows:
                print(f"      open  {item}  —  {who}")

    if not files:
        if all(settled_root(p) for p in args.path):
            print(SETTLED.format(path=", ".join(args.path)))
            return 0
        print(
            f"agentic unverified: no {OPTIN.GAPS} found under "
            f"{', '.join(args.path)} — nothing was checked",
            file=sys.stderr,
        )
        return 2

    print(
        f"\n{len(unique_by_target(files))} closing memos · {total_open} open"
        f" · {total_closed} closed"
        f" · {len(bad)} unreadable"
    )

    if bad:
        print("\nthe record could not be read as it stands:")
        for line in bad:
            print(line)
        print(
            "\nThis is not a report of zero open items. A section this cannot "
            "read is a section whose count is unknown."
        )
        return 1

    if total_open == 0:
        print(
            f"open: 0 — every recorded item opens with `{GAPS.CLOSED}` and says what "
            "closed it."
        )
    return 0


if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
