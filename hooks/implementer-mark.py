#!/usr/bin/env python3
"""PreToolUse side effect: record that a declared agent was actually spawned.

The routing declaration says who draws the frame and who implements the work —
the `framer` and `crafter` subagents, or the session itself — and until this gate
existed those answers were written down and never looked at again. This is the
half that makes them checkable: when a spawn names either agent, that axis's
mark goes into the repository's git dir, and `implementer-notice.py` reads both
after a commit.

**One gate for both axes**, because the two differ by which constant gets
written. `hooks/lib/implementer.py#mark_for` is where a spawn is matched to a mark,
so this file never names an agent at all.

**Decides nothing.** It prints no decision, and prints nothing at all, so it
cannot deny, ask, or delay a spawn. `dispatch.py` merges an empty output as
silence, which is what every allow already looks like. Blocking here was
considered and rejected in the plan for this work item: a fourth thing that can
stop a session, in a plugin whose first value is efficient development
through an unattended workflow, buys less than it costs.

**Written before the spawn runs.** The mark is written at `PreToolUse`, so a
spawn that something stops after this hook still leaves it. That is the
cheaper mistake: a session that retries the spawn writes the mark again, and
one that never spawns crafter after all is missed once per session. The other
direction, a mark written only once the spawn ran, would need a second hook
on the spawn's result.

Active only in repositories with `seal/` at the root, for the same reason
every gate here is: a globally installed plugin must not write files into
repositories that never asked for the workflow.

`hooks/lib/implementer.py` owns the address and the failure direction.
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import console
import implementer
import optin
import routing


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        return
    if event.get("tool_name") not in ("Agent", "Task"):
        return
    tool_input = event.get("tool_input") or {}
    mark = implementer.mark_for(tool_input.get("subagent_type"))
    if not mark:
        return

    cwd = event.get("cwd") or ""
    if not cwd or not os.path.isdir(cwd) or not optin.opted_in(cwd):
        return

    # The branch, not the HEAD sha: a work item commits many times and neither
    # the framer nor the implementer changes when it does. A sha would go stale
    # at the first commit and turn the notice into a line printed after every
    # one. It is resolved as the edit gate resolves it, so a branch with no
    # commit yet and a paused rebase get the mark their declaration reads.
    implementer.write(cwd, routing.worktree_branch(cwd), mark)


if __name__ == "__main__":
    # Prints nothing, so the streams matter only for the payload it reads —
    # and a payload it cannot decode is a mark never written, which is a
    # notice that fires. `hooks/lib/console.py` owns the reasoning.
    console.to_utf8()
    main()
