#!/usr/bin/env python3
"""SessionStart: print the core into a session whose repository holds a
`seal/` root (#1177, #1430).

The core, `skills/core/SKILL.md`, is what every party of this plugin judges
by. An agent receives it through its definition's `skills:` list; a session
receives it here, as plain text under the first line `lib/core.py` defines,
which names the file printed and the plugin's version, and above the
closing line that names where work starts. In a clone of the plugin's own
repository the file printed is the clone's (`core.origin`). A session in a
repository with no root receives nothing.

`hooks/hooks.json` runs this file for `SessionStart` with the matcher
`startup|clear|compact`: a resumed session keeps what its start printed,
and a compaction drops it. It writes nothing, and it exits 0 on every path,
printing nothing where it fails, so the `py -3` half of its command in
`hooks/hooks.json` runs only where `python3` could not start.
"""

import json
import os
import sys

LIB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib")

# The plugin root this file stands in, read where `CLAUDE_PLUGIN_ROOT` is not
# set: the harness sets it, and a hand run may not.
OWN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    """Print `core.output` for the payload's `cwd`. A payload that is not a
    JSON object holding `cwd` raises here, or names no repository to
    `core.output`, and either way nothing is printed: the `__main__` block
    turns every raise into exit 0."""
    sys.path.insert(0, LIB)
    import core

    cwd = json.load(sys.stdin)["cwd"]
    root = os.environ.get("CLAUDE_PLUGIN_ROOT") or OWN_ROOT
    text = core.output(cwd, root)
    if text:
        sys.stdout.write(text + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `lib/console.py`
    # owns the reasoning and the three decisions behind these lines. They are
    # its loop rather than its `to_utf8()`, because they run before `lib/` is
    # imported, which this script survives the absence of.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    try:
        main()
    except BaseException:
        pass
    sys.exit(0)
