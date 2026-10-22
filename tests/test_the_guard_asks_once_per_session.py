"""The worktree guard asked once per worktree, so an unattended run stopped
at the first `git worktree add` and again at every one after it.

Measured on the 0.9.1 release run (#237): six work items on six branches needed
six creations, and the guard held the run at all six. There was no path through
it that cost zero prompts — the `[worktree-ok]` site says so in writing, and it
is right about the token: the token is written into the command by whoever
issues it, so the model can write it on the first attempt, and reading it as
consent would turn the guard off with nobody asked.

What separates the first creation from the sixth is available without trusting
the token. **The harness only runs a `git worktree add` that was approved**, so
a `PostToolUse` observation of one that actually ran is written after the
answer rather than before the question, which is the one thing a command text
cannot forge.

Two halves, and they are separable on purpose:

  the writer   `hooks/worktree_consent.py` — the `PostToolUse` arm. Its own
               file rather than a branch inside the guard, because
               `hooks/dispatch.py` hands every gate the same payload with no
               event name, so one file wired to both events would have to tell
               them apart by sniffing a harness field. A gate wired only to
               `PostToolUse` needs no such guarantee (contract rule 13).
  the reader   `guard_worktree_creation`'s first row, whose cases are
               `tests/test_worktree_guard.py`'s since #942's phase 5.

What stays here is `hooks/worktree_consent.py`'s: the writer, the routing
answer's reader and the few cases that show the guard reading what they
wrote, until the phase that rebuilds that module. Several test files import
the helpers below.
"""

import json
import os
import pathlib
import subprocess
import sys

import pytest
from conftest import decision_of, load_hook_module, run_hook

wg = load_hook_module("worktree-guard.py", "wg_consent")
wc = load_hook_module("worktree_consent.py", "wc_consent")
HOOKS = os.path.join(os.path.dirname(__file__), "..", "hooks")

ACTIVE = [(111, "/tree", 1.0, 0.5, "VS Code")]
IDLE = [(222, "/tree", 400.0, 90.0, "Terminal")]


def common_dir(repo):
    """The clone's git directory — where the record lives.

    `--git-common-dir` rather than `--absolute-git-dir`: the record stands for
    "this session may split this clone into worktrees", and a linked worktree
    is the same clone. git answers relatively from a main worktree, so the
    join is not optional.
    """
    out = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--git-common-dir"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()
    return pathlib.Path(os.path.normpath(os.path.join(str(repo), out)))


def consent_dir(repo):
    return common_dir(repo) / "specseal-worktree-consent"


def grant(repo, session="me"):
    """Write the record by hand — the reader's tests do not need the writer."""
    d = consent_dir(repo)
    d.mkdir(parents=True, exist_ok=True)
    (d / session).write_text("", encoding="utf-8")
    return d / session


def decide(
    monkeypatch,
    capsys,
    repo,
    command,
    sessions=([], [], True),
    session_id="me",
    cwd=None,
    transcript_path=None,
):
    """`cwd` is where the SHELL is, which is not always `repo`: a `git -C
    <repo> worktree add` issued from outside any repository is the one shape
    that reaches the guard's second silent exit."""
    monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": sessions)
    payload = {
        "tool_name": "Bash",
        "session_id": session_id,
        "tool_input": {"command": command},
        "cwd": str(cwd or repo),
    }
    if transcript_path is not None:
        payload["transcript_path"] = str(transcript_path)
    monkeypatch.setattr(wg, "load_input", lambda: payload)
    try:
        wg.main()
    except SystemExit:
        pass
    out = capsys.readouterr().out.strip()
    if not out:
        return "silent", ""
    d = json.loads(out)["hookSpecificOutput"]
    return d["permissionDecision"], d["permissionDecisionReason"]


def post(repo, tool="Bash", command="git worktree add ../wt feature/x", **extra):
    """The payload the harness sends AFTER a tool call has run."""
    payload = {
        "hook_event_name": "PostToolUse",
        "tool_name": tool,
        "session_id": "me",
        "cwd": str(repo),
        "tool_input": {"command": command} if tool == "Bash" else command,
        "tool_response": {"stdout": "", "stderr": "", "interrupted": False},
    }
    payload.update(extra)
    return payload


# --- the writer: a creation that actually ran ------------------------------


def test_a_creation_that_ran_leaves_a_record(repo):
    run_hook("worktree_consent.py", post(repo))
    assert (consent_dir(repo) / "me").is_file()


def test_a_command_that_creates_nothing_leaves_no_record(repo):
    for command in ("git status", "git switch feature/x", "git worktree list"):
        run_hook("worktree_consent.py", post(repo, command=command))
    assert not consent_dir(repo).exists()


def test_a_creation_anywhere_in_the_command_records(repo):
    """A creation ANYWHERE in a command that ran is a creation that was
    approved, so the writer reads every segment until it finds one. The
    guard's PreToolUse walk judges that same first creation."""
    run_hook(
        "worktree_consent.py",
        post(repo, command="git status && git worktree add ../wt feature/x"),
    )
    assert (consent_dir(repo) / "me").is_file()


def test_a_failed_creation_still_records_the_approval(repo):
    """Q2. The record is about the approval, which happened. The retry after a
    failure — a path that already exists, a branch already checked out — is the
    worst moment to put the question again."""
    run_hook(
        "worktree_consent.py",
        post(
            repo,
            tool_response={
                "stdout": "",
                "stderr": "fatal: '../wt' already exists",
                "interrupted": False,
                "is_error": True,
            },
        ),
    )
    assert (consent_dir(repo) / "me").is_file()


def test_a_malformed_session_id_cannot_escape_the_directory(repo):
    """The id names a file. `../../escaped` put an empty file at a repository
    root once already, through the other marker."""
    run_hook("worktree_consent.py", post(repo, session_id="../../escaped"))
    assert (consent_dir(repo) / "escaped").is_file()
    assert not (repo / "escaped").exists()


def test_a_pre_tool_use_payload_is_not_a_creation_that_ran(repo):
    """The writer is wired to one event, and it also refuses a payload that
    names the other. Nothing sends it one; a group misconfigured by hand
    would."""
    payload = post(repo)
    payload["hook_event_name"] = "PreToolUse"
    payload.pop("tool_response")
    run_hook("worktree_consent.py", payload)
    assert not consent_dir(repo).exists()


def test_an_unrecordable_consent_asks_rather_than_crashing(
    monkeypatch, capsys, repo, tmp_path
):
    """Q3. A guard that crashes reads as a silent allow — the module says so
    about `_idle_minutes`. The write fails silently instead, no record exists,
    and the next creation meets the question it always did.

    stdout being empty is not the claim: a traceback goes to STDERR and leaves
    stdout empty too, which is how a crashing hook and a quiet one look alike.
    The exit status and stderr are what tell them apart, so both are read."""
    blocked = consent_dir(repo)
    blocked.parent.mkdir(parents=True, exist_ok=True)
    blocked.write_text("not a directory", encoding="utf-8")
    assert wc.record(str(repo), "me") is False
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "worktree_consent.py")],
        input=json.dumps(post(repo)),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == ""
    assert r.stderr.strip() == "", r.stderr
    assert decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "deny"


def test_a_directory_at_the_record_path_is_not_a_record(monkeypatch, capsys, repo):
    """The record is a FILE, and its existence is the fact. A directory of that
    name is not one — the same distinction `optin.py` draws for
    `specseal-scratch`, where a directory of the marker's name silenced every
    gate in the tree."""
    (consent_dir(repo) / "me").mkdir(parents=True)
    assert not wc.granted(str(repo), "me")
    assert decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "deny"


def test_a_session_id_that_is_only_separators_has_no_record_path(repo):
    """The id names a file, so an id that reduces to nothing must resolve to no
    path at all rather than to the directory above it. Left to the filesystem,
    `..` would be refused by `open` raising on a directory — a defence resting
    on a platform guarantee, which contract rule 13 refuses."""
    for bad in ("", ".", "..", "/", "../..", os.sep):
        assert wc.consent_path(str(repo), bad) == "", bad
    assert wc.consent_path(str(repo), "me").endswith(os.path.join("me"))


def test_the_record_follows_the_clone_not_the_worktree(repo, tmp_path):
    """Q4's neighbour: the SCOPE. A session that creates its first worktree
    from the main tree and its second from inside a linked one has made one
    decision, so it pays for one."""
    linked = tmp_path / "linked"
    subprocess.run(
        ["git", "-C", str(repo), "worktree", "add", "-q", str(linked), "feature/x"],
        check=True,
        capture_output=True,
    )
    run_hook("worktree_consent.py", post(linked))
    assert (consent_dir(repo) / "me").is_file()
    assert consent_dir(linked) == consent_dir(repo)


# --- where a segment's `-C` places it (`worktree_consent.segment_cwd`) -------


def test_the_C_target_follows_the_segment_that_was_judged(repo):
    """`main()` asks `segment_cwd` for the `-C` target of the very segment
    whose shape it read, from the same token list. Reading the two from
    separate tokenizations is how a switch aimed at another repository gets
    judged against THIS tree."""
    cmd = "git -C /x/y switch b  # don't"
    segments, _ = wg.split_command(cmd)
    assert wg.shape_of(segments[0]) == "switch"
    # `normpath`, because `apply_chdir` ends in one: the assertion is that
    # the target followed the segment, not that this platform spells a path
    # with `/`.
    assert wg.segment_cwd(segments[0], "/base") == os.path.normpath("/x/y")


def test_a_quoted_C_value_survives_an_apostrophe(repo):
    """A `-C` value with a space is what separates a quote-aware splitter from
    a whitespace one, and an apostrophe elsewhere in the command must not cost
    it. Both forms were unclassified before the guard borrowed the splitter."""
    for cmd, target in (
        ('git -C "my repo" switch b', "/base/my repo"),
        ("git -C 'my repo' switch b  # don't", "/base/my repo"),
    ):
        segments, _ = wg.split_command(cmd)
        assert wg.shape_of(segments[0]) == "switch", cmd
        assert wg.segment_cwd(segments[0], "/base") == os.path.normpath(target), cmd


# --- the Agent/Task path shares the record ---------------------------------


def test_the_agent_path_writes_the_record_bash_reads(monkeypatch, capsys, repo):
    run_hook(
        "worktree_consent.py",
        post(repo, tool="Agent", command={"prompt": "x", "isolation": "worktree"}),
    )
    assert (consent_dir(repo) / "me").is_file()
    assert decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "allow"


def test_an_agent_without_isolation_records_nothing(repo):
    run_hook("worktree_consent.py", post(repo, tool="Agent", command={"prompt": "x"}))
    assert not consent_dir(repo).exists()


# --- wiring ----------------------------------------------------------------


def test_the_writer_is_in_both_post_groups():
    d = load_hook_module("dispatch.py", "dispatch_consent")
    assert "worktree_consent.py" in d.GROUPS["post-bash"]
    assert "worktree_consent.py" in d.GROUPS["post-agent"]


def test_hooks_json_sends_the_agent_after_event_to_the_group():
    root = os.path.join(os.path.dirname(__file__), "..")
    with open(os.path.join(root, "hooks", "hooks.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    matchers = {
        group["matcher"]: group["hooks"][0]["command"]
        for group in cfg["hooks"]["PostToolUse"]
    }
    assert "Agent|Task" in matchers, matchers
    assert "post-agent" in matchers["Agent|Task"]


# --- the routing answer: the second consent source (#604) ------------------
#
# An automation run creates its worktrees before any of them has run, so the
# record cannot exist at the first one. The person's `automation` answer to the
# routing question can: the harness writes it into the session's transcript
# from the click, and the model writes the question and never which option was
# pressed. The fixtures below build transcript lines in the shape measured on
# 2026-09-26 (`spec.md` *Data & interfaces*), under a projects root the case
# owns, so no case reads a transcript of whoever runs the suite.

ROUTING_QUESTION = "How should this work be routed?"
ROUTING_OPTIONS = ("automation (Recommended)", "per axis", "no work item")
# A transcript line cut off mid-write: not JSON, and it carries both words the
# reader's prefilter looks for, so it reaches the parser.
TRUNCATED = '{"type": "user", "toolUseResult": {"answers": {"AskUserQuestion'


def ask_entries(
    cwd,
    answer="automation (Recommended)",
    options=ROUTING_OPTIONS,
    multi=False,
    tool="AskUserQuestion",
    tool_id="toolu_01routing",
    result_id=None,
    question=ROUTING_QUESTION,
):
    """One question put and answered: the assistant's `tool_use`, then the
    `user` entry the harness writes with the structured `toolUseResult`."""
    asked = {
        "questions": [
            {
                "question": question,
                "header": "Routing",
                "multiSelect": multi,
                "options": [{"label": o, "description": "d"} for o in options],
            }
        ]
    }
    use = {
        "type": "assistant",
        "cwd": str(cwd),
        "message": {
            "role": "assistant",
            "content": [
                {"type": "tool_use", "id": tool_id, "name": tool, "input": asked}
            ],
        },
    }
    result = {
        "type": "user",
        "cwd": str(cwd),
        "isSidechain": False,
        "message": {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": result_id or tool_id,
                    "content": f'The user answered: "{question}"="{answer}".',
                }
            ],
        },
        "toolUseResult": {
            "questions": [dict(asked["questions"][0])],
            "answers": {question: answer},
        },
    }
    return [use, result]


def write_transcript(root, session, entries, slug="-Users-x-repo"):
    """`<root>/<slug>/<session>.jsonl`, one JSON object (or raw line) each."""
    d = pathlib.Path(root) / slug
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{session}.jsonl"
    with open(path, "w", encoding="utf-8") as f:
        for e in entries:
            f.write((e if isinstance(e, str) else json.dumps(e)) + "\n")
    return path


def other_clone(tmp_path):
    d = tmp_path / "other"
    d.mkdir()
    subprocess.run(["git", "init", "-q", str(d)], check=True, capture_output=True)
    return d


@pytest.fixture
def projects(monkeypatch, tmp_path):
    """A projects root this case owns, seen by the unit copy and the guard's."""
    root = tmp_path / "projects"
    root.mkdir()
    monkeypatch.setattr(wc, "PROJECTS_ROOT", str(root))
    monkeypatch.setattr(wg.worktree_consent, "PROJECTS_ROOT", str(root))
    return root


def test_the_routing_preset_is_consent(projects, repo):
    """The measured answer, and the three decorations measured beside it --
    each on the pressed option's label, which is where a decoration lives. A
    pressed option's answer IS its label: 184 of 184 on disk."""
    for answer in (
        "automation",
        "automation (Recommended)",
        "automation (권장)",
        "automation — 안 멈추고 끝까지",
    ):
        options = (answer, "per axis", "no work item")
        write_transcript(
            projects, "me", ask_entries(repo, answer=answer, options=options)
        )
        assert wc.automation_answered(str(repo), "me"), answer
        assert wc.consent(str(repo), "me") == "answer", answer


def test_a_typed_answer_that_qualifies_the_preset_is_not_consent(projects, repo):
    """Round 1, finding 1. An `Other` answer is the person's own text, which
    the harness writes into `answers` verbatim, so cutting it at a decoration
    read *automation - but ask me before each worktree* as the preset -- the
    opposite of what the person wrote. Only a pressed option's label is an
    answer the guard reads."""
    for typed in (
        "automation - but ask me before each worktree",
        "automation (stop before creating worktrees)",
        "automation — 단, worktree 는 물어봐",
    ):
        write_transcript(projects, "me", ask_entries(repo, answer=typed))
        assert not wc.automation_answered(str(repo), "me"), typed


def test_a_sidechain_entry_is_not_consent(projects, repo):
    """A subagent has no `AskUserQuestion`, so no real click can carry
    `isSidechain: true`. Every main-transcript entry measured carries `false`
    (round 2 of work item 1790381327: 136 of 136 linked results), so an absent
    or non-bool value is refused as an unmeasured shape, the way
    `_routing_preset` refuses an absent `multiSelect`. The `False` row is the
    other half: without it, refusing everything would pass."""
    for value in (True, "true", 1, None, "absent"):
        use, result = ask_entries(repo)
        if value == "absent":
            del result["isSidechain"]
        else:
            result["isSidechain"] = value
        write_transcript(projects, "me", [use, result])
        assert not wc.automation_answered(str(repo), "me"), value
    use, result = ask_entries(repo)
    assert result["isSidechain"] is False
    write_transcript(projects, "me", [use, result])
    assert wc.automation_answered(str(repo), "me")


def test_the_payloads_transcript_path_is_read_when_it_names_this_session(
    projects, repo, tmp_path
):
    """Rule 1's first form. The file sits outside the projects root, so only
    the payload's path can have found it."""
    elsewhere = write_transcript(tmp_path / "elsewhere", "me", ask_entries(repo))
    assert wc.automation_answered(str(repo), "me", str(elsewhere))
    assert not wc.automation_answered(str(repo), "me")
    # A path naming another session's file is not this session's transcript.
    theirs = write_transcript(tmp_path / "elsewhere", "them", ask_entries(repo))
    assert not wc.automation_answered(str(repo), "me", str(theirs))


def test_a_subagents_own_path_falls_back_to_the_parents_transcript(projects, repo):
    """A subagent's call carries its parent's session id, so the glob finds
    the parent's file whatever path the subagent's own payload names."""
    write_transcript(projects, "me", ask_entries(repo))
    sub = projects / "-Users-x-repo" / "me" / "subagents" / "agent-a1.jsonl"
    sub.parent.mkdir(parents=True)
    sub.write_text("", encoding="utf-8")
    assert wc.automation_answered(str(repo), "me", str(sub))


def test_an_assistant_message_saying_automation_is_not_consent(projects, repo):
    """S6 (a). The model writes its own messages."""
    said = {
        "type": "assistant",
        "cwd": str(repo),
        "message": {
            "role": "assistant",
            "content": [{"type": "text", "text": 'The user answered: "automation"'}],
        },
    }
    write_transcript(projects, "me", [said])
    assert not wc.automation_answered(str(repo), "me")


def test_a_result_not_linked_to_an_ask_is_not_consent(projects, repo):
    """S6 (b). A Bash result can echo *The user answered: "automation"*, and
    even carry the answer's shape, but its `tool_use_id` names a Bash call.
    Seen red by dropping the id link from `automation_answered`."""
    bash = ask_entries(repo, tool="Bash", tool_id="toolu_01bash")
    # An AskUserQuestion elsewhere in the file, so the link is what decides.
    other = ask_entries(repo, answer="per axis", tool_id="toolu_01other")
    write_transcript(projects, "me", other + bash)
    assert not wc.automation_answered(str(repo), "me")
    echo = {
        "type": "user",
        "cwd": str(repo),
        "message": {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": "toolu_01bash",
                    "content": 'The user answered: "automation"',
                }
            ],
        },
        "toolUseResult": {"stdout": 'The user answered: "automation"'},
    }
    write_transcript(projects, "me", [*other, bash[0], echo])
    assert not wc.automation_answered(str(repo), "me")


def test_the_other_routing_answers_are_not_consent(projects, repo):
    """S6 (c). `per axis` is the boxes, which this work does not read (Q1)."""
    for answer in ("per axis", "no work item"):
        write_transcript(projects, "me", ask_entries(repo, answer=answer))
        assert not wc.automation_answered(str(repo), "me"), answer


def test_automation_on_another_question_is_not_consent(projects, repo):
    """S6 (d). The model writes the question and its options, so a question
    it made up with an `automation` option is the model's, not the routing
    batch. Seen red by dropping the option-set check."""
    for options in (
        ("automation", "manual"),
        ("automation", "per axis", "no work item", "something else"),
        ("automation", "per axis"),
    ):
        write_transcript(
            projects, "me", ask_entries(repo, answer="automation", options=options)
        )
        assert not wc.automation_answered(str(repo), "me"), options


def test_a_multi_select_routing_shape_is_not_consent(projects, repo):
    write_transcript(projects, "me", ask_entries(repo, multi=True))
    assert not wc.automation_answered(str(repo), "me")


BOXES_QUESTION = "Under per axis, which of these apply?"
BOXES = (
    "run end to end without stopping to ask",
    "implement with smith",
    "review with warden",
    "open the pull request",
)


def with_the_boxes(entries):
    """The same call with question 2's four boxes beside question 1.

    That is the shape every session asked before #911, and the one a
    machine whose installed block predates it still asks until
    `/specseal:update` reaches it."""
    use, result = (json.loads(json.dumps(e)) for e in entries)
    boxes = {
        "question": BOXES_QUESTION,
        "header": "Axes",
        "multiSelect": True,
        "options": [{"label": b, "description": "d"} for b in BOXES],
    }
    use["message"]["content"][0]["input"]["questions"].append(boxes)
    result["toolUseResult"]["questions"].append(dict(boxes))
    result["toolUseResult"]["answers"][BOXES_QUESTION] = ", ".join(BOXES)
    return [use, result]


def test_question_1_alone_and_the_boxes_beside_it_read_the_same_press(projects, repo):
    """#911 (work item 1791852610), S5. The routing question is now asked as
    question 1 alone, and the boxes come in a second call only under
    `per axis`; an installed block older than #911 still puts both in one
    call. The reader has to read the two shapes the same, or an un-updated
    machine's `automation` run meets the guard's prompt again (#894).

    Seen red by a throwaway edit to `_routing_preset` that returned False
    for a result carrying more than one question."""
    shapes = {
        "question 1 alone": lambda **kw: ask_entries(repo, **kw),
        "the boxes beside it": lambda **kw: with_the_boxes(ask_entries(repo, **kw)),
    }
    for shape, build in shapes.items():
        write_transcript(projects, "me", build())
        assert wc.automation_answered(str(repo), "me") is True, shape
        assert wc.consent(str(repo), "me") == "answer", shape
        write_transcript(projects, "me", build(answer="per axis"))
        assert wc.automation_answered(str(repo), "me") is False, shape
        assert wc.consent(str(repo), "me") == "", shape

    # A press given in the old shape is taken back by a later `per axis`
    # given in the new one: the last answer from this clone stands whatever
    # shape either was asked in.
    earlier = with_the_boxes(ask_entries(repo, tool_id="toolu_01before"))
    later = ask_entries(repo, answer="per axis", tool_id="toolu_02after")
    write_transcript(projects, "me", earlier)
    assert wc.automation_answered(str(repo), "me") is True
    write_transcript(projects, "me", earlier + later)
    assert wc.automation_answered(str(repo), "me") is False
    assert wc.consent(str(repo), "me") == ""


def boxes_alone(repo, ticked, tool_id):
    """The second call of the new shape: the four boxes, alone."""
    return ask_entries(
        repo,
        answer=", ".join(ticked),
        options=BOXES,
        multi=True,
        tool_id=tool_id,
        question=BOXES_QUESTION,
    )


def test_the_boxes_asked_alone_neither_give_nor_take_back_the_press(projects, repo):
    """#911, round 1. Under `per axis` the boxes come in a second call of
    their own. That result answers no routing question, so the `per axis`
    before it stands however many boxes were ticked, an earlier press stays
    taken back, and a press is not taken back by a boxes call alone.

    Seen red by a throwaway edit to `_routing_answer` that returned True for
    any result carrying a `multiSelect` question."""
    q1 = ask_entries(repo, answer="per axis", tool_id="toolu_q1")
    for ticked in (BOXES, BOXES[:1], ()):
        write_transcript(projects, "me", q1 + boxes_alone(repo, ticked, "toolu_b"))
        assert wc.automation_answered(str(repo), "me") is False, ticked
        assert wc.consent(str(repo), "me") == "", ticked

    earlier = ask_entries(repo, tool_id="toolu_earlier")
    write_transcript(projects, "me", earlier + q1 + boxes_alone(repo, BOXES, "toolu_b"))
    assert wc.automation_answered(str(repo), "me") is False

    write_transcript(projects, "me", earlier + boxes_alone(repo, (), "toolu_b"))
    assert wc.automation_answered(str(repo), "me") is True
    assert wc.consent(str(repo), "me") == "answer"


def test_a_result_before_its_question_is_not_consent(projects, repo):
    use, result = ask_entries(repo)
    write_transcript(projects, "me", [result, use])
    assert not wc.automation_answered(str(repo), "me")


def test_another_sessions_answer_is_not_consent(projects, repo):
    """S7. The answer belongs to the session the person was talking to."""
    write_transcript(projects, "them", ask_entries(repo))
    assert not wc.automation_answered(str(repo), "me")


def test_an_answer_given_in_another_clone_is_not_consent(projects, repo, tmp_path):
    """S7. The same session, answering from a different repository, said
    nothing about splitting this one. Seen red by dropping the clone check."""
    write_transcript(projects, "me", ask_entries(other_clone(tmp_path)))
    assert not wc.automation_answered(str(repo), "me")
    write_transcript(projects, "me", ask_entries(tmp_path / "no-such-dir"))
    assert not wc.automation_answered(str(repo), "me")
    use, result = ask_entries(repo)
    del result["cwd"]
    write_transcript(projects, "me", [use, result])
    assert not wc.automation_answered(str(repo), "me")


def test_an_answer_from_a_linked_worktree_is_the_same_clone(projects, repo, tmp_path):
    linked = tmp_path / "linked"
    subprocess.run(
        ["git", "-C", str(repo), "worktree", "add", "-q", str(linked), "feature/x"],
        check=True,
        capture_output=True,
    )
    write_transcript(projects, "me", ask_entries(linked))
    assert wc.automation_answered(str(repo), "me")


def test_an_unreadable_transcript_is_no_consent(projects, repo):
    """S8. Every way of not finding the answer lands on the old behaviour."""
    assert not wc.automation_answered(str(repo), "me")  # no transcript at all
    d = projects / "-Users-x-repo" / "me.jsonl"
    d.mkdir(parents=True)  # a directory where the file would be
    assert not wc.automation_answered(str(repo), "me")
    d.rmdir()
    # A line cut off mid-write carries the words the prefilter looks for, so
    # it reaches the parser; the others show the parser's non-object answers.
    write_transcript(
        projects,
        "me",
        [TRUNCATED, "{not json", "[1, 2]", '"a string"', "null", '["AskUserQuestion"]'],
    )
    assert not wc.automation_answered(str(repo), "me")
    use, result = ask_entries(repo)
    del result["toolUseResult"]["answers"]
    write_transcript(projects, "me", [use, result])
    assert not wc.automation_answered(str(repo), "me")
    use, result = ask_entries(repo)
    result["toolUseResult"] = "a string"
    result["message"]["content"] = "a string"
    write_transcript(projects, "me", [use, result])
    assert not wc.automation_answered(str(repo), "me")


def test_a_malformed_line_does_not_hide_a_later_answer(projects, repo):
    write_transcript(projects, "me", [TRUNCATED, *ask_entries(repo)])
    assert wc.automation_answered(str(repo), "me")


def test_two_transcripts_for_one_session_are_none(projects, repo):
    """Choosing one of two would be a guess about which the harness meant."""
    write_transcript(projects, "me", ask_entries(repo), slug="-a")
    write_transcript(projects, "me", ask_entries(repo), slug="-b")
    assert not wc.automation_answered(str(repo), "me")


def test_a_session_id_that_reduces_to_nothing_has_no_transcript(projects, repo):
    for session in ("", ".", "..", "/"):
        assert wc.transcript_for(session) == "", session


def test_the_labels_match_the_routing_question_the_orchestrator_asks():
    """The reader's constants against `skills/implement/orchestration.md`
    *Question 1*. Relabelling the question there turns this red instead of
    quietly bringing the guard's prompt back. Seen red by editing a
    constant."""
    root = pathlib.Path(__file__).resolve().parent.parent
    text = (root / "skills" / "implement" / "orchestration.md").read_text(
        encoding="utf-8"
    )
    section = text.split("\n### Question 1\n", 1)[1].split("\n### ", 1)[0]
    labels = [
        row.split("|")[2].strip().strip("*")
        for row in section.splitlines()
        if row.startswith("| ") and row.split("|")[1].strip().isdigit()
    ]
    assert tuple(labels) == wc.ROUTING_LABELS
    assert labels[0] == wc.PRESET


def test_no_case_reads_the_real_projects_root():
    """`tests/conftest.py`'s autouse fixture points the guard's copy of the
    reader at an empty directory, so a case that builds no transcript cannot
    find one belonging to whoever runs the suite. Seen red by deleting the
    fixture's `setattr`."""
    real = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    assert real != wg.worktree_consent.PROJECTS_ROOT
    assert not os.listdir(wg.worktree_consent.PROJECTS_ROOT)


# --- round 1, finding 2: the consent read never raises ----------------------


def dispatch_pre_bash(repo, session, transcript_path):
    """The group the harness actually runs, as a subprocess, so a gate that
    raises is skipped exactly the way `hooks/dispatch.py` skips it."""
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), "pre-bash"],
        input=json.dumps(
            {
                "tool_name": "Bash",
                "session_id": session,
                "transcript_path": transcript_path,
                "tool_input": {"command": "git worktree add ../wt f"},
                "cwd": str(repo),
            }
        ),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )
    return r.stdout


def test_a_shape_the_reader_did_not_expect_keeps_the_guards_deny(repo, tmp_path):
    """Round 1, finding 2. `dispatch.py` skips a gate that raises, so a
    consent read that raised turned the guard's deny into no decision at all.
    Two inputs raised: a `tool_use_id` that is a list (unhashable) and a NUL in
    `transcript_path`. Each is run through `dispatch.py pre-bash` beside a
    well-formed control, and each must reach the same stop the control does.
    A fresh session id per call, so the guard's own per-session memory is not
    what differs."""
    use, result = ask_entries(repo, answer="per axis")
    control = write_transcript(tmp_path / "t", "s-ok", [use, result])
    use, result = ask_entries(repo)
    result["message"]["content"][0]["tool_use_id"] = ["toolu_01routing"]
    listed = write_transcript(tmp_path / "t", "s-list", [use, result])
    outs = {
        "control": dispatch_pre_bash(repo, "s-ok", str(control)),
        "list id": dispatch_pre_bash(repo, "s-list", str(listed)),
        "NUL path": dispatch_pre_bash(repo, "s-nul", "/x/\x00y/s-nul.jsonl"),
    }
    assert decision_of(outs["control"]) == "deny", outs["control"]
    for name, out in outs.items():
        assert decision_of(out) == "deny", (name, out)


def test_the_reader_itself_answers_both_shapes_without_raising(projects, repo):
    """The two narrow repairs, pinned below `consent`'s catch-all, which would
    otherwise hide either one coming undone."""
    use, result = ask_entries(repo)
    result["message"]["content"][0]["tool_use_id"] = ["toolu_01routing"]
    write_transcript(projects, "me", [use, result])
    assert wc.automation_answered(str(repo), "me") is False
    assert wc.automation_answered(str(repo), "me", "/x/\x00y/me.jsonl") is False


def test_consent_fails_closed_on_any_exception(monkeypatch, repo):
    """The class, not the two instances: both call sites go through
    `consent`, so whatever the reader raises next is *no consent* there."""

    def boom(*a, **k):
        raise RuntimeError("a shape nobody measured")

    monkeypatch.setattr(wc, "automation_answered", boom)
    assert wc.consent(str(repo), "me") == ""
    grant(repo)
    assert wc.consent(str(repo), "me") == "record"


# --- the tracked-changes row's deny under the press (#894) -------------------
#
# Work item 1791779434. The texts other test files compare the guard's deny
# with; the guard's own cases are `tests/test_worktree_guard.py`'s.

TOKEN = {
    "en": "[shared-tree-ok] carries the user's answer to switch in this shared tree",
    "ko": "[shared-tree-ok] 가 공용 트리에서 전환한다는 사용자의 답을 담고 있어",
}


# The press sentence, byte for byte the first frame's: #896 copies it.
PRESS = {
    "en": "This session's person pressed `automation` on the routing question, "
    "so this guard puts no question to them, and none is to be put to them in "
    "its place.",
    "ko": "이 세션의 사용자가 라우팅 질문에서 `automation` 을 눌렀습니다. 그래서 "
    "이 guard 는 사용자에게 아무것도 묻지 않으며, 다른 방법으로 대신 물어서도 "
    "안 됩니다.",
}


def dirty_deny(lang, lead):
    """W3: the deny's one text for `dirty(repo)`, issued from inside the tree.
    Every sentence is a fact the guard read or a fact about the guard; none
    says what git does for any switch form (the reframe after round 3)."""
    if lang == "en":
        return (
            f"{lead}, so no other row of this guard stops the switch, but 1 "
            "uncommitted tracked changes are present:\n"
            "     M  f.txt\n"
            "\n" + PRESS["en"] + "\n\n"
            "This row of the guard stops a branch switch while uncommitted "
            "tracked changes are present, and says nothing of a switch once "
            "none are.\n"
            "\n"
            "The ways on, none of which needs a person. Issue each command on "
            "its own: this guard reads the tree before a command runs, so `git "
            "stash && git switch <branch>` on one line meets this same refusal. "
            "`git commit` and `git stash` are on this guard's list of commands "
            "that leave the branch where it is, so each passes it when issued "
            "alone. Which of them fits this switch, and what to run after it, is "
            "yours to decide.\n"
            "\n"
            "Re-issuing this command unchanged meets this same refusal."
        )
    return (
        f"{lead} 이 guard 의 다른 규칙은 이 전환을 막지 않지만, 커밋되지 않은 "
        "추적 파일 변경이 1건 있습니다:\n"
        "     M  f.txt\n"
        "\n" + PRESS["ko"] + "\n\n"
        "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 동안 브랜치 "
        "전환을 막고, 변경이 없으면 전환에 대해 아무 말도 하지 않습니다.\n"
        "\n"
        "사람이 없어도 되는 길은 아래와 같습니다. 명령은 하나씩 따로 실행하세요. "
        "이 guard 는 명령이 실행되기 전에 트리를 읽으므로, `git stash && git "
        "switch <branch>` 처럼 한 줄에 쓰면 같은 거부를 받습니다. `git commit` 과 "
        "`git stash` 는 이 guard 가 브랜치를 그대로 두는 명령으로 꼽는 목록에 "
        "있어, 따로 실행하면 이 guard 를 통과합니다. 이 전환에 어느 쪽이 맞는지, "
        "그 뒤에 무엇을 실행할지는 직접 정하세요.\n"
        "\n"
        "이 명령을 그대로 다시 실행하면 같은 거부를 받습니다."
    )
