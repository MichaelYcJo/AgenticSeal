"""`hooks/worktree_consent.py`: the record a creation that ran leaves, and the
routing answer's reader, the two consent sources the worktree guard reads.

**The harness only runs a `git worktree add` that was approved**, so a
`PostToolUse` observation of one that actually ran is written after the
answer rather than before the question, which is the one thing a command text
cannot forge. An automation run creates its worktrees before any of them has
run, so the person's `automation` answer to the routing question, which the
harness writes into the session's transcript from the click, is the second
source. The writer files a creation under the clone the guard judged, through
the guard's own placement. The guard's reading of both is
`tests/hooks/test_worktree_guard.py`'s.

The cases come from `tests/test_the_guard_asks_once_per_session.py`,
`tests/test_guard_resolves_the_tree_it_judges.py`,
`tests/test_an_automation_run_meets_no_commit_prompt.py` (#942's phase 6) and
`tests/hooks/test_question_gate.py`, whose case of the press reader takes that file's
`payload`, `write_the_transcript` and `SESSION` (#942's phase 7).
"""

import json
import os
import subprocess
import sys

import pytest
from conftest import (
    BASE_TREE_CHAINS,
    PLACEMENT_CHAINS,
    ROOT,
    ROUTING_OPTIONS,
    ROUTING_QUESTION,
    _a_dirty_w_under_a_clean_session,
    ask_entries,
    census_case,
    consent_dir,
    decision_of,
    grant,
    load_hook_module,
    run_hook,
    staged_repo,
    write_transcript,
)
from test_question_gate import SESSION, payload, write_the_transcript

TARGET = "hooks/worktree_consent.py"

wg = load_hook_module("worktree-guard.py", "wg_consent")
wc = load_hook_module("worktree_consent.py", "wc_consent")
HOOKS = os.path.join(ROOT, "hooks")


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


# A transcript line cut off mid-write: not JSON, and it carries both words the
# reader's prefilter looks for, so it reaches the parser.
TRUNCATED = '{"type": "user", "toolUseResult": {"answers": {"AskUserQuestion'

# The session a transcript of a press is written under.
PRESSED = "pressed"


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


BOXES_QUESTION = "Under per axis, which of these apply?"
BOXES = (
    "run end to end without stopping to ask",
    "implement with crafter",
    "review with proofer",
    "open the pull request",
)


def with_the_boxes(entries):
    """The same call with question 2's four boxes beside question 1.

    That is the shape every session asked before #911, and the one a
    machine whose installed block predates it still asks until
    `/agentic:update` reaches it."""
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


class Test_main:
    """The writer: a creation that actually ran leaves the record."""

    def test_accepts_a_creation_that_ran_and_leaves_a_record(self, repo):
        run_hook("worktree_consent.py", post(repo))
        assert (consent_dir(repo) / "me").is_file()

    def test_accepts_a_creation_anywhere_in_the_command(self, repo):
        """A creation ANYWHERE in a command that ran is a creation that was
        approved, so the writer reads every segment until it finds one. The
        guard's PreToolUse walk judges that same first creation."""
        run_hook(
            "worktree_consent.py",
            post(repo, command="git status && git worktree add ../wt feature/x"),
        )
        assert (consent_dir(repo) / "me").is_file()

    def test_accepts_a_failed_creation_and_still_records_the_approval(self, repo):
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

    def test_accepts_a_linked_worktree_and_files_under_its_clone(self, repo, tmp_path):
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

    def test_accepts_an_isolated_agent_and_writes_the_record_bash_reads(
        self, monkeypatch, capsys, repo
    ):
        run_hook(
            "worktree_consent.py",
            post(repo, tool="Agent", command={"prompt": "x", "isolation": "worktree"}),
        )
        assert (consent_dir(repo) / "me").is_file()
        assert (
            decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "allow"
        )

    def test_refuses_a_command_that_creates_nothing(self, repo):
        for command in ("git status", "git switch feature/x", "git worktree list"):
            run_hook("worktree_consent.py", post(repo, command=command))
        assert not consent_dir(repo).exists()

    def test_refuses_a_malformed_session_id_escaping_the_directory(self, repo):
        """The id names a file. `../../escaped` put an empty file at a repository
        root once already, through the other marker."""
        run_hook("worktree_consent.py", post(repo, session_id="../../escaped"))
        assert (consent_dir(repo) / "escaped").is_file()
        assert not (repo / "escaped").exists()

    def test_refuses_a_pre_tool_use_payload(self, repo):
        """The writer is wired to one event, and it also refuses a payload that
        names the other. Nothing sends it one; a group misconfigured by hand
        would."""
        payload = post(repo)
        payload["hook_event_name"] = "PreToolUse"
        payload.pop("tool_response")
        run_hook("worktree_consent.py", payload)
        assert not consent_dir(repo).exists()

    def test_refuses_an_agent_without_isolation(self, repo):
        run_hook(
            "worktree_consent.py", post(repo, tool="Agent", command={"prompt": "x"})
        )
        assert not consent_dir(repo).exists()

    def test_refuses_an_unrecordable_consent_and_asks_rather_than_crashing(
        self, monkeypatch, capsys, repo, tmp_path
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
        assert (
            decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "deny"
        )


class Test_consent:
    def test_accepts_the_routing_preset_as_consent(self, projects, repo):
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

    def test_refuses_any_exception_as_consent(self, monkeypatch, repo):
        """The class, not the two instances: both call sites go through
        `consent`, so whatever the reader raises next is *no consent* there."""

        def boom(*a, **k):
            raise RuntimeError("a shape nobody measured")

        monkeypatch.setattr(wc, "automation_answered", boom)
        assert wc.consent(str(repo), "me") == ""
        grant(repo)
        assert wc.consent(str(repo), "me") == "record"

    def test_refuses_a_directory_at_the_record_path(self, monkeypatch, capsys, repo):
        """The record is a FILE, and its existence is the fact. A directory of that
        name is not one — the same distinction `optin.py` draws for
        `agentic-scratch`, where a directory of the marker's name silenced every
        gate in the tree."""
        (consent_dir(repo) / "me").mkdir(parents=True)
        assert not wc.granted(str(repo), "me")
        assert (
            decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "deny"
        )


class Test_automation_answered:
    def test_accepts_the_payloads_transcript_path_where_it_names_this_session(
        self, projects, repo, tmp_path
    ):
        """Rule 1's first form. The file sits outside the projects root, so only
        the payload's path can have found it."""
        elsewhere = write_transcript(tmp_path / "elsewhere", "me", ask_entries(repo))
        assert wc.automation_answered(str(repo), "me", str(elsewhere))
        assert not wc.automation_answered(str(repo), "me")
        # A path naming another session's file is not this session's transcript.
        theirs = write_transcript(tmp_path / "elsewhere", "them", ask_entries(repo))
        assert not wc.automation_answered(str(repo), "me", str(theirs))

    def test_accepts_the_parents_transcript_for_a_subagents_own_path(
        self, projects, repo
    ):
        """A subagent's call carries its parent's session id, so the glob finds
        the parent's file whatever path the subagent's own payload names."""
        write_transcript(projects, "me", ask_entries(repo))
        sub = projects / "-Users-x-repo" / "me" / "subagents" / "agent-a1.jsonl"
        sub.parent.mkdir(parents=True)
        sub.write_text("", encoding="utf-8")
        assert wc.automation_answered(str(repo), "me", str(sub))

    def test_accepts_an_answer_from_a_linked_worktree_as_the_same_clone(
        self, projects, repo, tmp_path
    ):
        linked = tmp_path / "linked"
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "add", "-q", str(linked), "feature/x"],
            check=True,
            capture_output=True,
        )
        write_transcript(projects, "me", ask_entries(linked))
        assert wc.automation_answered(str(repo), "me")

    def test_accepts_a_later_answer_past_a_malformed_line(self, projects, repo):
        write_transcript(projects, "me", [TRUNCATED, *ask_entries(repo)])
        assert wc.automation_answered(str(repo), "me")

    def test_accepts_question_1_alone_and_the_boxes_beside_it_as_the_same_press(
        self, projects, repo
    ):
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

    def test_refuses_the_boxes_asked_alone_as_giving_or_taking_back_the_press(
        self, projects, repo
    ):
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
        write_transcript(
            projects, "me", earlier + q1 + boxes_alone(repo, BOXES, "toolu_b")
        )
        assert wc.automation_answered(str(repo), "me") is False

        write_transcript(projects, "me", earlier + boxes_alone(repo, (), "toolu_b"))
        assert wc.automation_answered(str(repo), "me") is True
        assert wc.consent(str(repo), "me") == "answer"

    def test_refuses_a_typed_answer_that_qualifies_the_preset(self, projects, repo):
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

    def test_refuses_a_sidechain_entry(self, projects, repo):
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

    def test_refuses_an_assistant_message_saying_automation(self, projects, repo):
        """S6 (a). The model writes its own messages."""
        said = {
            "type": "assistant",
            "cwd": str(repo),
            "message": {
                "role": "assistant",
                "content": [
                    {"type": "text", "text": 'The user answered: "automation"'}
                ],
            },
        }
        write_transcript(projects, "me", [said])
        assert not wc.automation_answered(str(repo), "me")

    def test_refuses_a_result_not_linked_to_an_ask(self, projects, repo):
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

    def test_refuses_the_other_routing_answers(self, projects, repo):
        """S6 (c). `per axis` is the boxes, which this work does not read (Q1)."""
        for answer in ("per axis", "no work item"):
            write_transcript(projects, "me", ask_entries(repo, answer=answer))
            assert not wc.automation_answered(str(repo), "me"), answer

    def test_refuses_automation_on_another_question(self, projects, repo):
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

    def test_refuses_a_multi_select_routing_shape(self, projects, repo):
        write_transcript(projects, "me", ask_entries(repo, multi=True))
        assert not wc.automation_answered(str(repo), "me")

    def test_refuses_a_result_before_its_question(self, projects, repo):
        use, result = ask_entries(repo)
        write_transcript(projects, "me", [result, use])
        assert not wc.automation_answered(str(repo), "me")

    def test_refuses_another_sessions_answer(self, projects, repo):
        """S7. The answer belongs to the session the person was talking to."""
        write_transcript(projects, "them", ask_entries(repo))
        assert not wc.automation_answered(str(repo), "me")

    def test_refuses_an_answer_given_in_another_clone(self, projects, repo, tmp_path):
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

    def test_refuses_an_unreadable_transcript(self, projects, repo):
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
            [
                TRUNCATED,
                "{not json",
                "[1, 2]",
                '"a string"',
                "null",
                '["AskUserQuestion"]',
            ],
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

    def test_refuses_two_transcripts_for_one_session(self, projects, repo):
        """Choosing one of two would be a guess about which the harness meant."""
        write_transcript(projects, "me", ask_entries(repo), slug="-a")
        write_transcript(projects, "me", ask_entries(repo), slug="-b")
        assert not wc.automation_answered(str(repo), "me")

    def test_refuses_both_shapes_that_raised_without_raising(self, projects, repo):
        """The two narrow repairs, pinned below `consent`'s catch-all, which would
        otherwise hide either one coming undone."""
        use, result = ask_entries(repo)
        result["message"]["content"][0]["tool_use_id"] = ["toolu_01routing"]
        write_transcript(projects, "me", [use, result])
        assert wc.automation_answered(str(repo), "me") is False
        assert wc.automation_answered(str(repo), "me", "/x/\x00y/me.jsonl") is False

    def test_an_answer_to_another_question_leaves_the_press_standing(
        self, projects, tmp_path
    ):
        """Only an answer to the routing question takes the press back. A later
        question the model put for something else is not a routing answer, and
        reading it as one would put a prompt back in front of a person who said
        nobody would be answering."""
        repo = staged_repo(tmp_path / "repo")
        first = ask_entries(repo, tool_id="toolu_01first")
        other = ask_entries(
            repo,
            answer="yes",
            options=("yes", "no"),
            question="Which name?",
            tool_id="toolu_01other",
        )
        write_transcript(projects, PRESSED, first + other)
        assert wc.automation_answered(str(repo), PRESSED)


def preset_result(**fields):
    """A structured result pressing the preset on the routing question, which
    carries FIELDS beside its text and its options."""
    asked = {
        "question": ROUTING_QUESTION,
        "options": [{"label": o, "description": "d"} for o in ROUTING_OPTIONS],
        **fields,
    }
    return {"questions": [asked], "answers": {ROUTING_QUESTION: ROUTING_OPTIONS[0]}}


class Test__routing_preset:
    def test_accepts_the_preset_pressed_on_a_single_select_question(self):
        assert wc._routing_preset(preset_result(multiSelect=False))

    def test_refuses_a_question_whose_multi_select_is_absent(self):
        """The routing question is single-select, and `multiSelect` must say
        so: an absent field is a shape nobody measured, so it is not read as
        single-select."""
        assert not wc._routing_preset(preset_result())


class Test_segment_cwd:
    def test_accepts_the_C_target_of_the_segment_that_was_judged(self, repo):
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

    def test_accepts_a_quoted_C_value_past_an_apostrophe(self, repo):
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

    def test_refuses_to_move_a_non_git_segment(self, tmp_path):
        assert wg.segment_cwd(["echo", "hello"], str(tmp_path)) == str(tmp_path)


class Test_creation_directory:
    @pytest.mark.parametrize("name", sorted(BASE_TREE_CHAINS))
    def test_accepts_where_the_base_filed_whatever_the_walk_leads(
        self, repo, tmp_path, name
    ):
        """#689, the consent twin. At `542f920b` the writer filed each creation
        under the walk's first directory, the skipped or unreached one; bash
        creates from `w`, and `86256492` filed it there."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        chain = BASE_TREE_CHAINS[name].format(
            missing=tmp_path / "nosuch-either", other=other
        )
        acted = wg.worktree_consent.creation_directory(
            chain + "git worktree add ../wt", str(session)
        )
        assert os.path.normpath(acted) == str(session / "w"), (name, acted)

    def test_accepts_the_creations_own_dash_c_composed(self, repo, tmp_path):
        """S3 of work item 1791384157, the half the chains do not reach: the
        writer files under the directory the creation's own `-C` names, composed
        onto the directory its segment runs in, as the guard judges it. A
        relative `-C` after a `cd` is the case `place` composes before it falls
        back. A break returning the shell's directory survived until this case."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        for command, expected in (
            (f"git -C {other} worktree add ../wt f", other),
            ("cd w && git -C ../clean worktree add ../wt f", session / "clean"),
        ):
            acted = wg.worktree_consent.creation_directory(command, str(session))
            assert os.path.samefile(acted, expected), (command, acted)

    def test_accepts_the_creation_the_base_filed_behind_a_wider_one(
        self, repo, tmp_path
    ):
        """Round 1 of 1790745049, red 1, the consent twin. `86256492` filed under
        `w`; at `4bc94f05` the first creation, which it did not read as git, was
        filed under the session's clone."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        acted = wg.worktree_consent.creation_directory(
            "2>/dev/null git worktree add ../wt-a; cd w && git worktree add ../wt-b",
            str(session),
        )
        assert os.path.normpath(acted) == str(session / "w"), acted

    @pytest.mark.parametrize(
        "name",
        [
            "an unreadable segment, then a cd whose failure branch creates",
            "a cd into nothing, then a semicolon",
        ],
    )
    def test_refuses_a_directory_bash_does_not_create_from(self, repo, tmp_path, name):
        """S1 and S2 of work item 1791384157. The writer took the first entry of
        the walk that was not `Unresolved`: the directory the `||` skips in the
        first chain, and a directory that holds nothing in the second, where no
        record was written at all. bash creates from the session's own directory
        in both. Red at `5623d728`, where the writer answered `{other}` and
        `{missing}`."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        chain = PLACEMENT_CHAINS[name].format(
            missing=tmp_path / "nosuch-either", other=other
        )
        acted = wg.worktree_consent.creation_directory(
            chain + "git worktree add ../wt f", str(session)
        )
        assert os.path.normpath(acted) == str(session), (name, acted)

    def test_refuses_a_creation_written_in_a_comment(self, repo):
        """A comment is not executed, so a `git worktree add` behind a `#`
        created nothing and is filed nowhere."""
        command = "echo hi #; git worktree add ../wt f"
        assert wc.creation_directory(command, str(repo)) == ""


class Test_module:
    def test_the_writer_is_in_both_post_groups(self):
        d = load_hook_module("dispatch.py", "dispatch_consent")
        assert "worktree_consent.py" in d.GROUPS["post-bash"]
        assert "worktree_consent.py" in d.GROUPS["post-agent"]

    def test_hooks_json_sends_the_agent_after_event_to_the_group(self):
        with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as f:
            cfg = json.load(f)
        matchers = {
            group["matcher"]: group["hooks"][0]["command"]
            for group in cfg["hooks"]["PostToolUse"]
        }
        assert "Agent|Task" in matchers, matchers
        assert "post-agent" in matchers["Agent|Task"]

    def test_a_session_id_that_is_only_separators_has_no_record_path(self, repo):
        """The id names a file, so an id that reduces to nothing must resolve to no
        path at all rather than to the directory above it. Left to the filesystem,
        `..` would be refused by `open` raising on a directory — a defence resting
        on a platform guarantee, which contract rule 13 refuses."""
        for bad in ("", ".", "..", "/", "../..", os.sep):
            assert wc.consent_path(str(repo), bad) == "", bad
        assert wc.consent_path(str(repo), "me").endswith(os.path.join("me"))

    def test_a_session_id_that_reduces_to_nothing_has_no_transcript(
        self, projects, repo
    ):
        for session in ("", ".", "..", "/"):
            assert wc.transcript_for(session) == "", session

    def test_no_case_reads_the_real_projects_root(self):
        """`tests/conftest.py`'s autouse fixture points the guard's copy of the
        reader at an empty directory, so a case that builds no transcript cannot
        find one belonging to whoever runs the suite. Seen red by deleting the
        fixture's `setattr`."""
        real = os.path.join(os.path.expanduser("~"), ".claude", "projects")
        assert real != wg.worktree_consent.PROJECTS_ROOT
        assert not os.listdir(wg.worktree_consent.PROJECTS_ROOT)

    def test_a_shape_the_reader_did_not_expect_keeps_the_guards_deny(
        self, repo, tmp_path
    ):
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

    def test_the_press_reader_reads_nothing_for_a_root_that_is_no_clone(self, tmp_path):
        """The gate's `top` is always a clone, so this is the reader's own half:
        a transcript it cannot place is unread, never "not answered"."""
        consent = load_hook_module("worktree_consent.py", "consent_for_question_gate")
        write_the_transcript(tmp_path / "cwd")
        path = payload(tmp_path / "cwd")["transcript_path"]
        nowhere = tmp_path / "no-repository"
        nowhere.mkdir()
        answer = consent.last_routing_answer(str(nowhere), SESSION, path)
        assert answer is consent.UNREAD, answer


test_census = census_case(TARGET)
