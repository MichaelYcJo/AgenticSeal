"""Shared reader: did the person press `automation` on the routing question?

The routing question is question 1 of `skills/implement/orchestration.md`.
The person's answer to it is read from the session's own main transcript,
which the harness writes from the click. The model writes the question and its
options and never which one was pressed, so nothing the model writes stands in
for the answer, and a `routing.md` is never read here.

Two gates ask it. `hooks/routing-edit-gate.py` reads `automation_answered` to
decide whether its refusal names a question tool, and `hooks/question-gate.py`
reads `is_routing_question` and `last_routing_answer` to let question 1
through until it is answered. Both import this module rather than a copy of
it, for the reason `optin.py` gives for being a module: divergent copies is how
half of them keep the old answer.

Every way a read fails is no press.
"""

import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import optin

# Where the harness writes session transcripts. One constant, so a test points
# it at a temporary directory and no case can read a real transcript on the
# machine running it.
PROJECTS_ROOT = os.path.join(os.path.expanduser("~"), ".claude", "projects")

# Question 1 of the routing batch, `skills/implement/orchestration.md`
# *Question 1*, as leading phrases. A test pins these against
# that table, so relabelling the question turns a case red instead of quietly
# bringing the prompt back.
ROUTING_LABELS = ("automation", "per axis", "no work item")
PRESET = "automation"

# Where a label's decoration starts: `automation (Recommended)`,
# `automation — 안 멈추고 끝까지`, `automation - nothing stops`.
_DECORATION = (" (", " —", " -")


def leading_phrase(label) -> str:
    """A label casefolded and cut where its decoration starts, then stripped.

    The orchestrator may decorate a label it was told to use verbatim, and the
    ten routing answers on disk when this was written carried three
    decorations: `automation (권장)`, `automation (Recommended)` and
    `automation — 안 멈추고 끝까지`. What they share is the phrase before the
    first ` (`, ` —` or ` -`. A label that is not a string has no phrase.
    """
    if not isinstance(label, str):
        return ""
    text = label.casefold()
    cut = min((i for i in (text.find(d) for d in _DECORATION) if i >= 0), default=-1)
    return (text[:cut] if cut >= 0 else text).strip()


def is_routing_question(question) -> bool:
    """True when QUESTION is an object whose options' leading phrases are the
    three of `ROUTING_LABELS`, each once.

    The one test of "this is question 1": the press reader asks it of a
    result, and `hooks/question-gate.py` asks it of a call it would refuse.
    """
    if not isinstance(question, dict):
        return False
    options = question.get("options")
    if not isinstance(options, list):
        return False
    phrases = sorted(
        leading_phrase(o.get("label") if isinstance(o, dict) else None) for o in options
    )
    return phrases == sorted(ROUTING_LABELS)


def transcript_for(session, transcript_path="") -> str:
    """This session's own MAIN transcript, or "" for every way of not having one.

    The payload's `transcript_path` when its basename is `<session>.jsonl`;
    otherwise the one file matching `<PROJECTS_ROOT>/*/<session>.jsonl`. A
    subagent's tool call carries its parent's `session_id`, so a subagent
    reaches its parent's answer through the second form, whatever path its own
    payload names. Nothing else is scanned: no other session's file, and no
    `subagents/` file, because a subagent has no `AskUserQuestion` to be
    answered in.

    More than one match is no match. Two files cannot both be this session's
    transcript, and choosing one is a guess about which of them the harness
    meant.
    """
    session = os.path.basename(str(session or ""))
    if not session or session in (".", ".."):
        return ""
    name = session + ".jsonl"
    if transcript_path and os.path.basename(str(transcript_path)) == name:
        return str(transcript_path)
    try:
        found = glob.glob(
            os.path.join(glob.escape(PROJECTS_ROOT), "*", glob.escape(name))
        )
    except (OSError, ValueError):
        return ""
    found = [p for p in found if os.path.isfile(p)]
    return found[0] if len(found) == 1 else ""


def _routing_preset(result) -> bool:
    """True when a structured `AskUserQuestion` result pressed the preset.

    One single-select question whose options' leading phrases are exactly the
    three of `ROUTING_LABELS`, answered with one of those option labels,
    verbatim, whose leading phrase is `PRESET`. A typed `Other` answer matches
    no label and is not read, whatever it starts with. `answers` maps a question's text to the chosen label. A
    multi-select answer is the chosen labels joined by `, `, and the routing
    question is not one, so `multiSelect` must be `False` rather than merely
    absent: an absent field is a shape nobody measured.
    """
    if not isinstance(result, dict):
        return False
    questions, answers = result.get("questions"), result.get("answers")
    if not isinstance(questions, list) or not isinstance(answers, dict):
        return False
    for q in questions:
        if not is_routing_question(q) or q.get("multiSelect") is not False:
            continue
        labels = [o.get("label") if isinstance(o, dict) else None for o in q["options"]]
        text = q.get("question")
        if not isinstance(text, str):
            continue
        # A pressed option's answer IS its label, verbatim. An `Other` answer is
        # the person's own text, and cutting it at a decoration read
        # "automation - but ask me before each worktree" as the preset -- so
        # the answer must be one of the labels before its phrase is read.
        answer = answers.get(text)
        if isinstance(answer, str) and answer in labels:
            if leading_phrase(answer) == PRESET:
                return True
    return False


def _routing_answer(result):
    """True for the preset, False for any other answer to the routing
    question, None when RESULT answers no routing question at all.

    The False half is what lets a later answer take the press back: a session
    that pressed `automation` for one work item and answered `per axis` for
    the next has, on its latest answer, a person who may be asked (round 1 of
    work item 1790644505, yellow 5). Every shape that is neither the preset
    nor clearly the routing question stays None and changes nothing.
    """
    if _routing_preset(result):
        return True
    if not isinstance(result, dict) or not isinstance(result.get("questions"), list):
        return None
    if any(is_routing_question(q) for q in result["questions"]):
        return False
    return None


def _content(entry):
    message = entry.get("message")
    content = message.get("content") if isinstance(message, dict) else None
    return content if isinstance(content, list) else []


def _clone_of(cwd) -> str:
    """The common git directory of the clone `cwd` sits in, real-pathed, or ""."""
    common = optin.git_common_dir(optin.repo_root(cwd)) if isinstance(cwd, str) else ""
    return os.path.realpath(common) if common else ""


def automation_answered(top: str, session: str, transcript_path: str = "") -> bool:
    """True when the person pressed `automation` on the routing question, in
    this session's own transcript, from this clone (`last_routing_answer`)."""
    return last_routing_answer(top, session, transcript_path) is True


# What `last_routing_answer` returns where it read nothing: an object no
# answer can equal, so "unread" and "read, and not answered" stay apart.
UNREAD = object()


def last_routing_answer(top: str, session: str, transcript_path: str = ""):
    """True for the preset, False for any other answer to the routing question,
    None where this session's transcript was read and holds no answer to it
    from this clone, and `UNREAD` where no transcript could be read.

    `automation_answered` reads the True. `hooks/question-gate.py` reads the
    None: the routing question goes through it only until it is answered,
    and only where a transcript exists for the press to be recorded in.

    The harness writes this answer from the person's click; the model writes
    the question and its options and never which one was pressed. That is the
    whole difference from `[worktree-ok]` and from a `routing.md` the model
    wrote itself, and it is why the answer stands beside the record as
    consent. `docs/worktree-guard-spec.md` *Creation consent* holds the table.

    Four conditions. Failing the first, or a clone that cannot be resolved, is
    `UNREAD`; an entry failing another is skipped. The guard reads either as
    its behaviour before this reader existed:

      1. the transcript is this session's own main one (`transcript_for`);
      2. the answer is a harness-written `AskUserQuestion` result: a `user`
         entry whose `tool_result` names, by `tool_use_id`, an EARLIER
         assistant `tool_use` called `AskUserQuestion`, read from the entry's
         structured `toolUseResult`, and carrying `isSidechain: false`. A Bash
         result echoing *The user answered: "automation"* has no such link and
         no `answers` object, and a subagent has no `AskUserQuestion`;
      3. the question is the routing question and the preset was pressed
         (`_routing_preset`);
      4. the result entry's own `cwd` is in the same clone as `top`;

    and the LAST answer to the routing question from this clone is the one
    that stands, so a later answer other than the preset takes the press back
    (`_routing_answer`). The whole transcript is read for that, where the
    reader used to stop at the first press.

    A line is parsed only when it carries `AskUserQuestion` or `toolUseResult`.
    That skips assistant text and progress lines, but every tool result
    carries `toolUseResult`, so most user lines are parsed: 0.09 s on the
    largest local transcript (17.3 MB) when round 1 measured it. A read error
    is `UNREAD`, and every malformed line and every missing field is skipped.
    The two shapes round 1 found raising -- a `tool_use_id` that is not
    a string, a NUL in the path -- are handled here, and `consent` catches
    whatever else might, because `hooks/dispatch.py` skips a gate that raises
    and the guard's deny would become no decision at all.
    """
    path = transcript_for(session, transcript_path)
    if not path:
        return UNREAD
    want = _clone_of(top)
    if not want:
        return UNREAD
    asked = set()
    clones = {}
    pressed = None
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            for line in handle:
                if "AskUserQuestion" not in line and "toolUseResult" not in line:
                    continue
                try:
                    entry = json.loads(line)
                except (ValueError, RecursionError):
                    continue
                if not isinstance(entry, dict):
                    continue
                kind = entry.get("type")
                if kind == "assistant":
                    for item in _content(entry):
                        if (
                            isinstance(item, dict)
                            and item.get("type") == "tool_use"
                            and item.get("name") == "AskUserQuestion"
                            and isinstance(item.get("id"), str)
                        ):
                            asked.add(item["id"])
                    continue
                if kind != "user" or not asked:
                    continue
                # A subagent has no `AskUserQuestion`, and every main-transcript
                # user entry measured carries `isSidechain: false`. Anything
                # else -- true, absent, or not a bool -- is a shape nobody
                # measured, refused the way `_routing_preset` refuses an absent
                # `multiSelect`.
                if entry.get("isSidechain") is not False:
                    continue
                linked = any(
                    isinstance(item, dict)
                    and item.get("type") == "tool_result"
                    and isinstance(item.get("tool_use_id"), str)
                    and item["tool_use_id"] in asked
                    for item in _content(entry)
                )
                if not linked:
                    continue
                answered = _routing_answer(entry.get("toolUseResult"))
                if answered is None:
                    continue
                cwd = entry.get("cwd")
                key = cwd if isinstance(cwd, str) else ""
                if key not in clones:
                    clones[key] = _clone_of(key) if key else ""
                if clones[key] == want:
                    # The LAST answer from this clone stands: a later work
                    # item's `per axis` takes back an earlier press, and a
                    # later press gives it back.
                    pressed = answered
    except (OSError, ValueError):
        return UNREAD
    return pressed
