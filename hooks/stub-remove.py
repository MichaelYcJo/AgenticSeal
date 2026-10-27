#!/usr/bin/env python3
"""SessionStart: take out the git hook stubs an earlier release wrote (#1027).

The rule is `docs/the-routing-check.md` *Where the routing is checked*: this
plugin writes nothing into a clone's git hooks. An earlier release wrote a
`pre-commit`, a `reference-transaction` and a `post-commit` stub into the
clone's common git directory's `hooks/`, which every worktree of the clone
shares. Each runs the plugin copy whose absolute path it names, for as long
as that copy is on disk, so after an upgrade a stub would go on judging
commits with the old copy. The first session that starts in the clone takes
them out.

**A stub is a hook file whose second line starts with the marker
`# specseal-git-hook`**, the shape every stub carried. A hook file without it
is never touched: a person's own hook, or one husky, the pre-commit framework
or lefthook wrote, stays byte for byte. The marker is read in every file of
the directory, so a stub of any name goes.

It runs in any clone a session starts in, opted in or not, because a stub is
this plugin's own file wherever it stands. What it removed is said once, as
the session's message; a clone with no stub says nothing. Every failure is
silent: a stub left in place costs what it cost before, which is a commit
judged by the copy it names.

This file has a sunset (`plan.md` *Operational impact* of work item
1792935671): a later release retires it once no clone a supported release
reaches still carries a stub.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import console
import optin

MARKER = "# specseal-git-hook"

REMOVED = (
    "AgenticSeal removed the git hooks an earlier release of it wrote in "
    "{directory}: {names}. Nothing of AgenticSeal runs inside git any more, and a "
    "hook file without the line `{marker}` was left as it was."
)


def is_stub(path):
    """Whether the file at PATH carries the marker as its second line."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            head = f.read(4096)
    except OSError:
        return False
    # exempt from splitlines: a hook file an earlier release wrote
    lines = head.splitlines()
    return len(lines) >= 2 and lines[1].startswith(MARKER)


def stub_folder(cwd):
    """The common git directory's `hooks/` of the clone CWD is in, or ""."""
    top = optin.repo_root(cwd)
    common = optin.git_common_dir(top) if top else ""
    return os.path.join(common, "hooks") if common else ""


def remove(directory):
    """Remove every stub under DIRECTORY; the names removed, in name order."""
    try:
        names = sorted(os.listdir(directory))
    except OSError:
        return []
    removed = []
    for name in names:
        path = os.path.join(directory, name)
        if os.path.isfile(path) and is_stub(path):
            try:
                os.remove(path)
            except OSError:
                continue
            removed.append(name)
    return removed


def spoken(names):
    """NAMES as a person reads a list: `a`, `a and b`, `a, b and c`. The
    three a release wrote are said in the order it wrote them."""
    order = ("pre-commit", "reference-transaction", "post-commit")
    names = sorted(names, key=lambda n: (order.index(n) if n in order else 3, n))
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " and " + names[-1]


def main():
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(payload, dict):
        return
    directory = stub_folder(payload.get("cwd") or "")
    if not directory:
        return
    removed = remove(directory)
    if removed:
        said = REMOVED.format(directory=directory, names=spoken(removed), marker=MARKER)
        print(json.dumps({"systemMessage": said}))


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/console.py`
    # owns the reasoning and the three decisions behind these lines.
    console.to_utf8()
    main()
