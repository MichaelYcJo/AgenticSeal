#!/usr/bin/env python3
"""PreToolUse on `AskUserQuestion`: put the rule for a run that reads
`Automation` `yes` in front of the orchestrator at the moment it asks.

`docs/running/the-run.md` *The run* says that on such a run the orchestrator
does not stop the run with a question the tree or the framer can answer.
#1608's run read that paragraph when it wrote `routing.md` and still put two
questions to a person who was not there, so the rule is shown where the
question is made rather than recalled from half an hour earlier.

The hook reads three things exactly and nothing else:

- each open work item, as `lib/routing.py#open_declarations` gives them, and
  of those the ones whose `Automation` row reads `yes`;
- the question list of the call's input, `tool_input["questions"]`, each
  question an object holding a string `question`;
- in each question's text, `MARKER` in its one spelling, followed on the
  same line by a character that is not blank.

Where an open work item reads `yes` and any question of the call does not
hold that form, it prints a `PreToolUse` deny object whose reason holds the
paragraph, read from the plugin root, the open work items with their
branches, each named once, what makes a work item open and what ends the
refusal, the header of each question that does not state why, and the form
that lets the call through. Each question is its own stop, so one reason
does not carry another. A question that holds `MARKER` with its case
changed is named in the reason as a line this hook did not read; no other
spelling is read or named. Whether the stated reason is true, and whether
the question is one only the owner can decide, is not this hook's to judge:
the person reads the reason in the question.

Where the paragraph cannot be read from the plugin root, the reason names
`DOC` *The run* and `LEAD` in its place, so a rewrite that drops the lead
still refuses with a coordinate.

**It fails toward letting the call through.** A payload that is not a JSON
object, a `cwd` that is not a string, a question list of another shape, a
git that does not start or exits non-zero, and a repository with no root
each print nothing, and so does anything that raises, `lib/gitcmd.py#Failed`
among them: the `__main__` block turns every raise into exit 0. A wrong
allow costs one question that should have waited; a wrong deny under a hook
that fires on every call would be an outage. The hook writes nothing,
reaches no network, and starts one `git worktree list` per call, plus the
`rev-parse` `lib/optin.py#home_at` asks from a linked worktree. Its command
in `hooks/hooks.json` ends with ` || exit 0`, so the command exits 0 whatever
happens, a file its interpreter cannot load among them.
"""

import json
import os
import re
import sys

LIB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib")

# The plugin root this file stands in, read where `CLAUDE_PLUGIN_ROOT` is not
# set: the harness sets it, and a hand run may not.
OWN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The form a question states why its default cannot be taken in: this text,
# in this one spelling, then a reason on the same line. This is its one home:
# a document that states the form cites `hooks/ask-under-automation.py#MARKER`.
MARKER = "No default:"

# The opening of the first line of the paragraph the reason carries, under
# `DOC`. It locates the paragraph and is no copy of its text.
LEAD = "**On a run whose `routing.md` reads `Automation` `yes`"

# The document the paragraph stands in, `/`-joined, and its section.
DOC = "docs/running/the-run.md"
SECTION = "The run"

# The marker followed, on its line, by a character that is not blank.
STATED = re.compile(re.escape(MARKER) + r"[^\S\r\n]*[^\s]")

# The marker in any case, so a spelling other than `MARKER` can be named.
NEAR = re.compile(re.escape(MARKER), re.IGNORECASE)


def _paragraph(root):
    """The paragraph of `DOC` under ROOT whose first line opens with `LEAD`,
    its lines as the document holds them, or "" where it cannot be read."""
    try:
        with open(os.path.join(root, *DOC.split("/")), encoding="utf-8") as f:
            lines = f.read().split("\n")
    except (OSError, UnicodeDecodeError):
        return ""
    for at, line in enumerate(lines):
        if line.startswith(LEAD):
            end = at
            while end < len(lines) and lines[end].strip():
                end += 1
            return "\n".join(lines[at:end])
    return ""


def _questions(tool_input):
    """The question objects of TOOL_INPUT, or None where it is not a
    non-empty list of objects each holding a string `question`."""
    found = tool_input.get("questions") if isinstance(tool_input, dict) else None
    if not isinstance(found, list) or not found:
        return None
    for one in found:
        if not isinstance(one, dict) or not isinstance(one.get("question"), str):
            return None
    return found


def _label(one):
    """The question's `header` in double quotes, or its `question` text
    where the header is missing, empty or not a string."""
    header = one.get("header")
    return (
        '"' + (header if isinstance(header, str) and header else one["question"]) + '"'
    )


def _reason(paragraph, items, unstated):
    """The refusal's text: the rule, the open work items reading `yes`, what
    makes one open and what ends the refusal, the questions that do not
    state why, the form, and each spelling of the marker this hook did not
    read."""
    rule = paragraph or (
        "Read the paragraph of `" + DOC + "` *" + SECTION + "* that opens with: " + LEAD
    )
    named = ", ".join(_label(one) for one in unstated)
    parts = [
        "This AskUserQuestion call is refused by the plugin's PreToolUse hook, "
        "hooks/ask-under-automation.py, because a work item open in this "
        "repository reads `Automation` `yes`. The rule, from `"
        + DOC
        + "` *"
        + SECTION
        + "*:",
        rule,
        "Open work items reading `Automation` `yes`: "
        + "; ".join(name + " on branch " + branch for name, branch in items)
        + ". A work item counts as open while its branch is checked out in a "
        "worktree of this repository. Where its run has ended, checking out "
        "another branch in that worktree, or removing the worktree, ends this "
        "refusal, and that work item's records take nothing from this call.",
        "The questions that do not state why their default cannot be taken: "
        + named
        + ". Where the tree or the frame/questions.md of the work item this "
        "session runs answers a question, proceed on its default and record "
        "it as that paragraph says. A question only the owner can decide "
        "states why in its own "
        "text: `"
        + MARKER
        + "` and the reason, on the same line. A call whose every question "
        "does so goes through.",
    ]
    for one in unstated:
        for spelt in sorted({m.group(0) for m in NEAR.finditer(one["question"])}):
            if spelt != MARKER:
                parts.append(
                    "Question "
                    + _label(one)
                    + " holds `"
                    + spelt
                    + "`, which this hook does not read: it reads `"
                    + MARKER
                    + "` in that one spelling."
                )
    return "\n\n".join(parts)


def main():
    """Print the deny object for the payload on stdin where it refuses, and
    nothing otherwise. A payload that is not a JSON object raises here, and
    the `__main__` block turns every raise into exit 0."""
    sys.path.insert(0, LIB)
    import routing

    payload = json.load(sys.stdin)
    # Each work item once: in shared mode every worktree cut after its
    # declaration was committed holds a copy, and each copy is a file of its own.
    items = []
    for path, parsed in routing.open_declarations(payload["cwd"]):
        item = (os.path.basename(os.path.dirname(path)), parsed["branch"])
        if parsed["automation"] == routing.AUTOMATION_YES and item not in items:
            items.append(item)
    if not items:
        return
    questions = _questions(payload.get("tool_input"))
    if questions is None:
        return
    unstated = [one for one in questions if not STATED.search(one["question"])]
    if not unstated:
        return
    root = os.environ.get("CLAUDE_PLUGIN_ROOT") or OWN_ROOT
    said = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": _reason(_paragraph(root), items, unstated),
        }
    }
    sys.stdout.write(json.dumps(said) + "\n")
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
