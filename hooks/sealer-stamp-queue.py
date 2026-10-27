#!/usr/bin/env python3
"""PostToolUse(Write|Edit): queue a work item's stamp at the write of its
`sealed` guarantee, under either root (work item 1792363231, #1027).

The stamp is queued where the verdict comes to read `sealed`: at the write,
in shared mode as in local mode (`docs/the-review-record.md` *The stamp*).
After a `Write` or `Edit` whose file is `…/seal/threads/<id>/guarantee.md`, it
hands the path and the payload's session to
`seal_stamp.queue_for_written_guarantee`, which says whether the file is the
guarantee under the repository's root in force and whether its verdict
queues the work item's one stamp, and records a refusal where the verdict
names a commit its branch does not hold. `hooks/sealer-stamp.py` draws what
was queued at the main session's `Stop`, unchanged.

The repository is the edited file's, never the payload's `cwd`, for the
reason `hooks/session-lease.py` gives: a session can edit a tree its working
directory is not in. A subagent's `Write` (the sealer's own) carries the
main session's `session_id` (`questions.md` Q1 of work item 1792363231,
measured 2026-10-19), so the file is queued for the session whose `Stop`
draws it. Queueing is not drawing, so the payload's `agent_id` changes
nothing here.

The group runs this after every file edit in every repository. So the edit's
shape is matched first, from the payload alone: a `Write` or `Edit`, a
session, and a path ending `/seal/threads/<id>/guarantee.md`. `seal_stamp.py`
is loaded only after that, and it is this gate's only way to `git`. Every
failure is silent: the stamp is a thing shown to a person and never a reason
to stop an edit.
"""

import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import console

HOOKS = os.path.dirname(os.path.abspath(__file__))
STAMP = os.path.join(
    os.path.dirname(HOOKS), "skills", "verify", "scripts", "seal_stamp.py"
)
TOOLS = ("Write", "Edit")
# Matched against the path with `/` for every separator, so a Windows path
# matches as a POSIX one does.
GUARANTEE = re.compile(r"/seal/threads/[^/]+/guarantee\.md$")


def shaped(path):
    """Whether `path` ends in `/seal/threads/<id>/guarantee.md`."""
    normal = os.path.normpath(path).replace(os.sep, "/")
    return bool(GUARANTEE.search(normal))


def load_stamp():
    """`seal_stamp.py`, loaded by path from the plugin's `skills/`."""
    spec = importlib.util.spec_from_file_location(
        "specseal_seal_stamp_for_the_edit_gate", STAMP
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    if not isinstance(payload, dict) or payload.get("tool_name") not in TOOLS:
        return
    session = payload.get("session_id")
    path = (payload.get("tool_input") or {}).get("file_path")
    if not session or not isinstance(path, str) or not shaped(path):
        return
    try:
        lines = load_stamp().queue_for_written_guarantee(path, session)
    except (Exception, SystemExit):
        return
    if lines:
        print(json.dumps({"systemMessage": "\n".join(lines)}))


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/console.py`
    # owns the reasoning and the three decisions behind these lines.
    console.to_utf8()
    main()
