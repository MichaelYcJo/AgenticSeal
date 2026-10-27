#!/usr/bin/env python3
"""PreToolUse gate: on a branch declared `Automation` `yes`, no question is put.

The rule is `docs/the-review-record.md` *The run*. This file holds what the
rule rests on.

The declaration is read through `routing.declared`, so a linked worktree, a
root under the common git directory, a branch with no commit yet, a paused
rebase and a detached HEAD resolve through `routing.worktree_branch`, as the
edit gate resolves them. Every way of not
reading it (no `seal/`, no branch, a file that does not parse, two files for
one branch) is the attended answer, and the gate prints nothing.

`routing.md` is written by the model, which is why the worktree guard never
reads it as consent. Read here only to refuse, a row the model forged binds
only the model.

The routing question put alone goes through while this session's transcript
can be read and holds no answer to it from this clone, read by the press
reader the worktree guard uses (`worktree_consent.last_routing_answer`).
That is the resumed session, which puts question 1 again so the gates that
read the press find it. Where no transcript can be read, those gates find no
press either, so the question is refused. Once an answer is recorded, the
routing question is refused like any other, and so is a question dressed in
its labels, a shape no list of spellings closes. "Put alone" is the shape
the press reader counts: one question, its labels
(`worktree_consent.is_routing_question`), single-select, with its text. A
call whose questions cannot be read is not that question, and is refused.

Any routing answer from this clone in the session spends the exemption,
including one given for another work item, so a session that has already
answered for another branch cannot put question 1 again. That is outside the
one-issue flow, and is a limit rather than a mechanism.

A gate whose own reason says to ask with the question tool meets this
refusal too, and its question states no default: the session takes none of
the ways on that question offers, and hands the stop back at the end of the
run.

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
QUESTIONS = optin.QUESTIONS


def shown(path, top):
    """PATH relative to TOP, or whole where it has no relative spelling."""
    try:
        return os.path.relpath(path, top)
    except ValueError:
        return path


def reason(top, item):
    return (
        f"SpecSeal refused this question. `{routing.FILENAME}` in "
        f"`{shown(item, top)}` answers `{routing.AUTOMATION}` with "
        f"`{routing.AUTOMATION_YES}`, so this run does not stop to ask. Build "
        "on the default the question states, write that default as a row of "
        f"`{QUESTIONS}` in the same thread, and name it in the pull request "
        "body, where the owner can overturn it. A question that states no "
        "default, such as another gate's choice, is not yours to answer: take "
        "none of its ways on and hand that stop back at the end of the run. "
        "Asking again meets the same refusal. The routing question put alone "
        "goes through only until this session has answered it here."
    )


def routing_question_alone(tool_input):
    questions = tool_input.get("questions") if isinstance(tool_input, dict) else None
    if not isinstance(questions, list) or len(questions) != 1:
        return False
    question = questions[0]
    return (
        worktree_consent.is_routing_question(question)
        and question.get("multiSelect") is False
        and isinstance(question.get("question"), str)
    )


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(event, dict) or event.get("tool_name") != TOOL:
        return
    cwd = event.get("cwd")
    top = optin.repo_root(cwd)
    declared = routing.declared(cwd, top)
    if not declared or declared["automation"] != routing.AUTOMATION_YES:
        return
    if (
        routing_question_alone(event.get("tool_input"))
        and worktree_consent.last_routing_answer(
            top, event.get("session_id"), event.get("transcript_path") or ""
        )
        is None
    ):
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
