"""Which process is a Claude Code session's own `claude` (#692, #868).

**This module is the one reader of which process and which variable are the
session's.** The lease writer (`hooks/session-lease.py`) records
`claude_pid`, and the worktree guard's count of other sessions tests a
process's name with `is_claude`, so both find the same process. The writer
used to take any process whose name held `claude`, at a different depth, so
a `claude-host` ancestor was recorded and no reader ever matched that lease.
`claude_pid` reads `CLAUDE_PID` first, a value the harness exports beside
`SESSION_VARIABLE` to every Bash child (measured: it is the pid the walk
finds), and walks only where it is absent. The walk stays under the variable
for contract rule 13's reason: the variable is a platform guarantee, and a
defence resting on one is verified only with it removed.

The commit gate's route from a git hook back to its session lived here until
#1027 removed every hook of this plugin that ran inside git.
"""

import os
import subprocess

# The one variable the harness exports that names the session.
SESSION_VARIABLE = "CLAUDE_CODE_SESSION_ID"

# The variable the harness exports beside it that names the session's own
# `claude` process (executed in a Bash child on 2026-10-07 and 2026-10-08).
PID_VARIABLE = "CLAUDE_PID"


def is_claude(comm):
    """Whether a process whose `ps` comm is COMM is a Claude Code session:
    its executable's basename is `claude`, nothing more and nothing less.
    `claude-host` and `xclaude` are not; `/x/bin/claude` is."""
    return os.path.basename(str(comm or "").strip()) == "claude"


def claude_pid(environ=None):
    """The pid of the session's `claude` process, or None.

    `CLAUDE_PID` where the environment carries a pid above 1, an observed
    value; else the nearest ancestor `claude_ancestor` finds. None is a real
    answer: an extension host whose process is not named `claude`, and which
    exports no variable, must not be mistaken for a session that exited."""
    environ = os.environ if environ is None else environ
    value = str(environ.get(PID_VARIABLE) or "").strip()
    if value.isdigit() and int(value) > 1:
        return int(value)
    return claude_ancestor()


def claude_ancestor(start=None, depth=20):
    """The pid of the nearest ancestor process named `claude`, or None."""
    pid = os.getppid() if start is None else start
    for _ in range(depth):
        if pid is None or pid <= 1:
            return None
        try:
            out = subprocess.run(
                ["ps", "-o", "ppid=,comm=", "-p", str(pid)],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=5,
            ).stdout.strip()
        except (OSError, subprocess.SubprocessError):
            return None
        if not out:
            return None
        parent, _, comm = out.partition(" ")
        if is_claude(comm):
            return pid
        try:
            pid = int(parent)
        except ValueError:
            return None
    return None
