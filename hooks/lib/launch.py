#!/usr/bin/env python3
"""Run an AgenticSeal script on an interpreter at or above the plugin's floor.

Every `bin/` wrapper but `bin/test`, and its `.cmd` twin, runs its script
through this file:

    python3 hooks/lib/launch.py <script> [arguments...]

The one such wrapper is `bin/seal`, and each tool `seal` runs as a
subcommand is handed to the interpreter this file already held to the floor
(`skills/implement/scripts/seal.py#tool_command`).

`bin/test` hands `.github/scripts/run_tests.py` to the interpreter itself,
because that script's job begins below the floor: on an older `python3` it
builds a virtualenv at or above `FLOOR`, with `uv` or a newer interpreter it
finds, and runs the suite there. A refusal at entry would stop the one script
written to get past an old `python3`.

Below `FLOOR` it writes one sentence naming the floor, the version it found
and the interpreter it found it at, and exits 2 before the script is read.
Otherwise it runs the script as `__main__`, with `sys.argv`, `sys.path[0]`
and `__file__` set the way running the script directly sets them, so the
script's sibling imports and its own path behave as they would.

**This file is the floor's one source.** `.github/scripts/run_tests.py`
reads `FLOOR` from it. `ruff.toml`'s `target-version` cannot import, so
`tests/test_launch.py` holds it equal.

**Its syntax is the oldest Python 3's.** No f-string, no walrus, nothing
keyword-only, and no import above the check that a new release added: a
launcher that cannot parse is the traceback it exists to replace.

It sits in `hooks/` because each wrapper it serves reaches it relative to
itself, as `$here/../hooks/lib/launch.py`, and `hooks/` already ships the modules the
scripts share. `hooks/hooks.json` does not run through it: a gate that fails
is skipped and said, and the call goes ahead
(`docs/the-session-hooks.md` *Registration*), where exit 2 from a hook
is the harness's word for blocking the call.

Exit codes: 2 for an interpreter below the floor or no script named, with
nothing read and nothing written; otherwise the script's own.
"""

import os
import sys

FLOOR = (3, 12)

REFUSAL = (
    "{command}: needs python {floor} or newer, and this is python {found} "
    "at {executable}.\n"
    "Nothing was read and nothing was written.\n"
    "`python3` is not always the newest interpreter installed -- macOS ships "
    "python 3.9 under that name -- so name one explicitly, `python{floor} "
    "{script} ...`, or see CONTRIBUTING.md section 'Running the checks'.\n"
)
USAGE = "usage: launch.py <script> [arguments...]\n"


def refusal(script, version, executable):
    """The sentence for `script` on an interpreter below the floor.

    The command is the script's name the way its wrapper spells it,
    `seal.py` as `seal` and a `_` as a `-`, so a reader who typed the
    wrapper can tell what answered. The paths are escaped to ASCII first, and the
    rest of the sentence is ASCII already: it is written before anything sets
    up stderr, and a path the console cannot encode would otherwise end the
    refusal in a traceback.
    """
    script = script.encode("ascii", "backslashreplace").decode("ascii")
    executable = executable.encode("ascii", "backslashreplace").decode("ascii")
    command = os.path.basename(script)
    if command.endswith(".py"):
        command = command[: -len(".py")]
    return REFUSAL.format(
        command=command.replace("_", "-"),
        floor=".".join(str(part) for part in FLOOR),
        found=".".join(str(part) for part in version[:3]),
        executable=executable,
        script=script,
    )


def main(argv):
    """Refuse below the floor, else run `argv[1]` as `__main__`.

    `sys.path[0]` is the script's directory with links resolved, which is
    what the interpreter puts there for a script it runs itself.
    """
    if len(argv) < 2:
        sys.stderr.write(USAGE)
        return 2
    script = argv[1]
    if tuple(sys.version_info[:2]) < FLOOR:
        sys.stderr.write(refusal(script, sys.version_info, sys.executable))
        return 2
    import runpy

    sys.argv[:] = argv[1:]
    sys.path[0] = os.path.dirname(os.path.realpath(script))
    runpy.run_path(os.path.abspath(script), run_name="__main__")
    return 0


# exempt from entry_point: the launcher imports nothing before its floor check
if __name__ == "__main__":
    sys.exit(main(sys.argv))
