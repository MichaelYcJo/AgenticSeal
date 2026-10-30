#!/usr/bin/env python3
"""SessionStart: print the core into the session (#1177).

The core, `skills/core/SKILL.md`, is what every party of this plugin judges
by. An agent receives it through its definition's `skills:` list; a session
receives it here, as plain text under the first line `hooks/lib/core.py`
defines, which names the file printed, the plugin's version and the file's
SHA-256. In a clone of the plugin's own repository the file printed is the
clone's (`core.origin`).

It is the one gate of the `session-core` group, because `dispatch.py#merge`
drops a gate's plain text beside a neighbour's JSON, and `version-check`
prints JSON in the `session-start` group. `hooks/hooks.json` runs the group
for `SessionStart` with the matcher `startup|clear|compact`: a resumed
session keeps what its start printed, and a compaction drops it. It prints
in every session, in any directory, and writes nothing.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import console
import core

# The plugin root this file stands in, read where `CLAUDE_PLUGIN_ROOT` is not
# set: the harness sets it, and a hand run may not.
OWN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        payload = {}
    cwd = payload.get("cwd") if isinstance(payload, dict) else ""
    root = os.environ.get("CLAUDE_PLUGIN_ROOT") or OWN_ROOT
    print(core.output(cwd if isinstance(cwd, str) else "", root))


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/lib/console.py`
    # owns the reasoning and the three decisions behind these lines.
    console.to_utf8()
    main()
