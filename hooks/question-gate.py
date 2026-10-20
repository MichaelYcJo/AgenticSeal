#!/usr/bin/env python3
"""PreToolUse gate: on a branch declared `Automation` `yes`, no question is put.

The rule is `docs/the-review-record.md` §*The run*. This file holds what the
rule rests on.

The declaration is read through `routing.declared`, the call the commit gate's
PreToolUse reading makes, so a linked worktree, a root under the common git
directory and a detached HEAD resolve the same way for both. Every way of not
reading it (no `seal/`, no branch, a file that does not parse, two files for
one branch) is the attended answer, and the gate prints nothing.

`routing.md` is written by the model, which is why the worktree guard never
reads it as consent. Read here only to refuse, a row the model forged binds
only the model.

The routing question put alone goes through, by the predicate the press
reader uses (`worktree_consent.is_routing_question`): a run resumed in a new
session puts it again for the gates that read the press. A call whose
questions cannot be read is not that question, and is refused.

Failure direction: it blocks more. A wrong deny costs one default the pull
request body names; a wrong allow is the stopped run this gate exists to end.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import console
import optin
import routing
import worktree_consent

TOOL = "AskUserQuestion"
QUESTIONS = "questions.md"


def shown(path, top):
    """PATH relative to TOP, or whole where it has no relative spelling."""
    try:
        return os.path.relpath(path, top)
    except ValueError:
        return path


def reason(top, item):
    declaration = shown(os.path.join(item, routing.FILENAME), top)
    questions = shown(os.path.join(item, QUESTIONS), top)
    return (
        f"SpecSeal refused this question. `{declaration}` answers "
        f"`{routing.AUTOMATION}` with `{routing.AUTOMATION_YES}`, so nobody is "
        "at the keyboard to answer it. Build on the default the question "
        f"states, write that default as a row of `{questions}`, and name it in "
        "the pull request body, where the owner can overturn it. Asking again "
        "meets the same refusal. The routing question put alone goes through."
    )


def routing_question_alone(tool_input):
    questions = tool_input.get("questions") if isinstance(tool_input, dict) else None
    return (
        isinstance(questions, list)
        and len(questions) == 1
        and worktree_consent.is_routing_question(questions[0])
    )


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(event, dict) or event.get("tool_name") != TOOL:
        return
    if routing_question_alone(event.get("tool_input")):
        return
    cwd = event.get("cwd")
    top = optin.repo_root(cwd)
    declared = routing.declared(cwd, top)
    if not declared or declared["automation"] != routing.AUTOMATION_YES:
        return
    item = routing.item_dir(top, declared["branch"])
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason(top, item),
                }
            }
        )
    )


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/console.py`
    # owns the reasoning and the three decisions behind these lines.
    console.to_utf8()
    main()
