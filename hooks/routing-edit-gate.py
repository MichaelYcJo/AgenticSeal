#!/usr/bin/env python3
"""PreToolUse gate: the first edit on an undeclared branch is refused.

The rule is `docs/the-routing-check.md` *The edit check*. The routing is
decided before the first edit, so this gate checks that moment itself: a
`Write`, `Edit` or `NotebookEdit` of a file in an opted-in repository's
worktree is refused while no routing declaration names the branch checked out
there and the session has not recorded, through `seal no-work-item` on that
branch, that its change belongs to no work item.

**The edited file decides, never the payload's `cwd`.** The file's path is
resolved to the worktree that holds it, because a session can edit a tree its
working directory is not in. A path that is not absolute places no file, and
the edit tools refuse one, so it is not judged. The tool input is a path, so
no command is read.

**Three kinds of file are not judged**: one under the repository's `seal/`
root, so the declaration can always be written; one git ignores, which never
lands in a commit; and one outside every opted-in repository.

**A detached HEAD names no branch, except during a paused rebase**, where the
branch the rebase names stands for it (`routing.worktree_branch`, which
`seal no-work-item` resolves its branch through too), so resolving a
conflict on a declared branch is never refused, **and at a
commit that a declared branch already holds**, under its local name or a
remote-tracking one, so a proofer's clone at the reviewed commit and a
red-first clone of an earlier one edit without a stop. A detached HEAD at
any other commit is refused.

The declaration is read through `routing.for_branch`, so every way it cannot
be read is no declaration, and the edit is refused. The no-work-item record
is `routing.no_work_item`'s, and it lets an edit through only on a branch it
names. The refusal reads the person's `automation` press
through `worktree_consent.automation_answered`: pressed, it names no question
tool; otherwise it tells the model to put the routing question. Where HEAD is
detached, its ways on start by checking out a branch, because
`seal no-work-item` records nothing there.

The checks run cheapest-first on the path an allowed edit takes, because this
gate runs before every edit in an opted-in repository: the root, the `seal/`
root and the branch's declaration are read first, and the ignore test, the
record and the press only where the declaration is missing.
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import console
import optin
import routing

# The edit tools, in the order `hooks/hooks.json`'s matchers name them: the
# `pre-edit` matcher and the `post-edit` matcher are this list joined by `|`.
TOOLS = ("Write", "Edit", "NotebookEdit")

HEADER = "AgenticSeal refused this edit; nothing was written."
STATE = (
    "`{file}` is in `{top}`, which runs the AgenticSeal workflow, and no routing "
    "declaration names `{branch}`, the branch checked out there. The routing "
    "is decided before the first edit."
)
DETACHED = (
    "`{file}` is in `{top}`, which runs the AgenticSeal workflow, and HEAD is "
    "detached there, so no routing declaration can name its branch. The "
    "routing is decided before the first edit."
)
# The opening of the ways on under the person's `automation` press, and of
# the attended text, each followed by the ways for a branch or for a
# detached HEAD, where `seal no-work-item` records nothing.
PRESS = (
    "This session's person pressed `automation` on the routing question, so "
    "no question is put to them, and none is to be put to them in its place.\n\n"
    "The ways on, none of which needs a person:\n"
)
PRESSED = PRESS + (
    "  1. Where this edit belongs to the work item the run was routed for, "
    "write its declaration at `{hint}` from `templates/records/sdd-routing.md`, naming "
    "`{branch}`, and edit again.\n"
    "  2. Where it belongs to no work item, run `seal no-work-item` once on "
    "`{branch}`, and edit again."
)
PRESSED_DETACHED = PRESS + (
    "  1. Where this edit belongs to the work item the run was routed for, "
    "check out its branch in `{top}`, write its declaration at `{hint}` from "
    "`templates/records/sdd-routing.md`, naming that branch, and edit again.\n"
    "  2. Where it belongs to no work item, check out a branch in `{top}`, "
    "run `seal no-work-item` once on it, and edit again; on a detached HEAD it "
    "records nothing."
)
ASK = (
    "Do not choose for the user. Put the routing question to them with the "
    "AskUserQuestion tool, as `skills/implement/orchestration.md` "
    "*Orchestrator: how the work is routed* states. "
)
ATTENDED = ASK + (
    "Then write the declaration at `{hint}` from `templates/records/sdd-routing.md`, "
    "naming `{branch}`, or, where they answer `no work item`, run "
    "`seal no-work-item` once on `{branch}`. Then edit again."
)
ATTENDED_DETACHED = ASK + (
    "Then check out a branch in `{top}`, and write its declaration at `{hint}` "
    "from `templates/records/sdd-routing.md`, naming that branch, or, where they "
    "answer `no work item`, run `seal no-work-item` once on it, because on a "
    "detached HEAD it records nothing. Then edit again."
)
UNCHANGED = "Re-issuing this edit unchanged meets this same refusal."


def edited_path(event):
    """The absolute path the call edits, or "" where it names none."""
    tool_input = event.get("tool_input")
    if not isinstance(tool_input, dict):
        return ""
    key = "notebook_path" if event.get("tool_name") == "NotebookEdit" else "file_path"
    path = tool_input.get(key)
    if not isinstance(path, str) or not os.path.isabs(path):
        return ""
    return path


def nearest_directory(path):
    """The closest directory at or above PATH's parent that exists, or "".
    A `Write` may create its file and the directories above it."""
    where = os.path.dirname(path)
    while where and not os.path.isdir(where):
        parent = os.path.dirname(where)
        if parent == where:
            return ""
        where = parent
    return where


def inside(path, root):
    """Whether PATH is ROOT or below it, compared real path to real path."""
    path, root = os.path.realpath(path), os.path.realpath(root)
    try:
        return os.path.commonpath([path, root]) == root
    except ValueError:
        return False


def git(top, *args):
    """`(exit code, stdout)` of git in TOP, or `(None, "")` where it cannot
    run."""
    try:
        r = subprocess.run(
            ["git", "-C", top, *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return None, ""
    return r.returncode, r.stdout or ""


def detached_on_declared(top):
    """Whether TOP's detached HEAD is a commit that a branch some declaration
    names already holds, under `refs/heads/<branch>` or any
    `refs/remotes/<remote>/<branch>`: a clone at a reviewed commit, or a
    red-first check of an earlier commit of that branch. Commits made there
    reach a pull request only through a branch, which this gate and the
    trailer arm judge (round 1 of #1027, finding 3)."""
    names = {d["branch"] for _, d in routing.declarations(top) if d.get("branch")}
    for name in sorted(names):
        code, out = git(
            top,
            "for-each-ref",
            "--format=%(refname)",
            f"refs/heads/{name}",
            f"refs/remotes/*/{name}",
        )
        for ref in out.split() if code == 0 else []:
            # `for-each-ref` also matches a pattern with no glob as a prefix
            # ending at a slash, so `refs/heads/feat` lists
            # `refs/heads/feat/sub`; only the declared name itself counts.
            # The remote pattern holds a glob, which git matches whole
            # (round 2 of #1027, finding 2).
            if ref.startswith("refs/heads/") and ref != f"refs/heads/{name}":
                continue
            if git(top, "merge-base", "--is-ancestor", "HEAD", ref)[0] == 0:
                return True
    return False


def ignored(top, path):
    """Whether git ignores PATH in TOP's worktree. A test git cannot answer
    is no answer, and the file is judged."""
    try:
        rel = os.path.relpath(os.path.realpath(path), os.path.realpath(top))
    except ValueError:
        return False
    code, _ = git(top, "check-ignore", "-q", "--", rel)
    return code == 0


def declaration_hint(top):
    """The declaration path a refusal tells a session to write, relative to
    `top` and spelled the way the platform spells it, as
    `hooks/implementer-notice.py` spells the same file: the root arrives
    `normpath`ed (`hooks/lib/optin.py`), so `os.path.join` keeps one dialect.

    Under the root this repository resolves to: in local mode that root is
    under the git directory. A linked worktree on another Windows drive has no
    relative spelling (`ntpath.relpath` raises), and the absolute path is the
    one to type there (round 1 of #80, red 1). `decide` refuses only where
    that root exists, so it is always found here.
    """
    home = optin.home_at(top)
    try:
        rel = os.path.relpath(home, top)
    except ValueError:
        rel = home
    return os.path.join(rel, optin.WORK_ITEMS, "<work-item-id>", routing.FILENAME)


def reason(path, top, branch, pressed):
    """The whole text of the refusal."""
    shown = os.path.relpath(os.path.realpath(path), os.path.realpath(top))
    if branch:
        state = STATE
        ways = PRESSED if pressed else ATTENDED
    else:
        state = DETACHED
        ways = PRESSED_DETACHED if pressed else ATTENDED_DETACHED
    hint = declaration_hint(top)
    return "\n\n".join(
        [
            HEADER,
            state.format(file=shown, top=top, branch=branch),
            ways.format(hint=hint, top=top, branch=branch),
            UNCHANGED,
        ]
    )


def decide(event):
    """The refusal's text, or None where the edit goes ahead."""
    if not isinstance(event, dict) or event.get("tool_name") not in TOOLS:
        return None
    path = edited_path(event)
    where = nearest_directory(path) if path else ""
    top = optin.repo_root(where)
    if not top:
        return None
    common = optin.git_common_dir(top)
    home = optin.home_at(top, common)
    if not home or inside(path, home):
        return None
    branch = routing.worktree_branch(top)
    if routing.for_branch(top, branch):
        return None
    if not branch and detached_on_declared(top):
        return None
    if ignored(top, path):
        return None
    session = event.get("session_id")
    if routing.no_work_item(common, session, branch):
        return None
    import worktree_consent

    pressed = worktree_consent.automation_answered(
        top, session, event.get("transcript_path") or ""
    )
    return reason(path, top, branch, pressed)


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return
    said = decide(event)
    if said is None:
        return
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": said,
                }
            }
        )
    )


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/lib/console.py`
    # owns the reasoning and the three decisions behind these lines.
    console.to_utf8()
    main()
