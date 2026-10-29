"""`hooks/lib/press.py`: the person's `automation` press on the routing
question, read from the session's own main transcript.

`hooks/routing-edit-gate.py` and `hooks/question-gate.py` read it. Their
reading of it is their own files' cases; the cases here ask the reader itself,
and the case that holds its labels to `skills/implement/orchestration.md`
*Question 1*.
"""

import json
import os
import pathlib
import subprocess

import pytest
from conftest import (
    ROOT,
    ROUTING_OPTIONS,
    ROUTING_QUESTION,
    ask_entries,
    census_case,
    load_hook_module,
    staged_repo,
    write_transcript,
)
from test_question_gate import SESSION, payload, write_the_transcript

TARGET = "hooks/lib/press.py"

press = load_hook_module("lib/press.py", "press_for_its_own_file")

# A gate's copy of the reader: every gate imports `press` by its plain name,
# and that one copy is what `tests/conftest.py` points at an empty directory.
GATE = load_hook_module("question-gate.py", "question_gate_for_press")


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
    """A projects root this case owns, seen by the unit copy."""
    root = tmp_path / "projects"
    root.mkdir()
    monkeypatch.setattr(press, "PROJECTS_ROOT", str(root))
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


class Test_automation_answered:
    def test_accepts_the_payloads_transcript_path_where_it_names_this_session(
        self, projects, repo, tmp_path
    ):
        """Rule 1's first form. The file sits outside the projects root, so only
        the payload's path can have found it."""
        elsewhere = write_transcript(tmp_path / "elsewhere", "me", ask_entries(repo))
        assert press.automation_answered(str(repo), "me", str(elsewhere))
        assert not press.automation_answered(str(repo), "me")
        # A path naming another session's file is not this session's transcript.
        theirs = write_transcript(tmp_path / "elsewhere", "them", ask_entries(repo))
        assert not press.automation_answered(str(repo), "me", str(theirs))

    def test_accepts_the_parents_transcript_for_a_subagents_own_path(
        self, projects, repo
    ):
        """A subagent's call carries its parent's session id, so the glob finds
        the parent's file whatever path the subagent's own payload names."""
        write_transcript(projects, "me", ask_entries(repo))
        sub = projects / "-Users-x-repo" / "me" / "subagents" / "agent-a1.jsonl"
        sub.parent.mkdir(parents=True)
        sub.write_text("", encoding="utf-8")
        assert press.automation_answered(str(repo), "me", str(sub))

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
        assert press.automation_answered(str(repo), "me")

    def test_accepts_a_later_answer_past_a_malformed_line(self, projects, repo):
        write_transcript(projects, "me", [TRUNCATED, *ask_entries(repo)])
        assert press.automation_answered(str(repo), "me")

    def test_accepts_question_1_alone_and_the_boxes_beside_it_as_the_same_press(
        self, projects, repo
    ):
        """#911 (work item 1791852610), S5. The routing question is now asked as
        question 1 alone, and the boxes come in a second call only under
        `per axis`; an installed block older than #911 still puts both in one
        call. The reader has to read the two shapes the same, or an un-updated
        machine's `automation` run reads as no press (#894).

        Seen red by a throwaway edit to `_routing_preset` that returned False
        for a result carrying more than one question."""
        shapes = {
            "question 1 alone": lambda **kw: ask_entries(repo, **kw),
            "the boxes beside it": lambda **kw: with_the_boxes(ask_entries(repo, **kw)),
        }
        for shape, build in shapes.items():
            write_transcript(projects, "me", build())
            assert press.automation_answered(str(repo), "me") is True, shape
            write_transcript(projects, "me", build(answer="per axis"))
            assert press.automation_answered(str(repo), "me") is False, shape

        # A press given in the old shape is taken back by a later `per axis`
        # given in the new one: the last answer from this clone stands whatever
        # shape either was asked in.
        earlier = with_the_boxes(ask_entries(repo, tool_id="toolu_01before"))
        later = ask_entries(repo, answer="per axis", tool_id="toolu_02after")
        write_transcript(projects, "me", earlier)
        assert press.automation_answered(str(repo), "me") is True
        write_transcript(projects, "me", earlier + later)
        assert press.automation_answered(str(repo), "me") is False

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
            assert press.automation_answered(str(repo), "me") is False, ticked

        earlier = ask_entries(repo, tool_id="toolu_earlier")
        write_transcript(
            projects, "me", earlier + q1 + boxes_alone(repo, BOXES, "toolu_b")
        )
        assert press.automation_answered(str(repo), "me") is False

        write_transcript(projects, "me", earlier + boxes_alone(repo, (), "toolu_b"))
        assert press.automation_answered(str(repo), "me") is True

    def test_refuses_a_typed_answer_that_qualifies_the_preset(self, projects, repo):
        """Round 1, finding 1. An `Other` answer is the person's own text, which
        the harness writes into `answers` verbatim, so cutting it at a decoration
        read *automation - but ask me before each worktree* as the preset -- the
        opposite of what the person wrote. Only a pressed option's label is read
        as an answer."""
        for typed in (
            "automation - but ask me before each worktree",
            "automation (stop before creating worktrees)",
            "automation — 단, worktree 는 물어봐",
        ):
            write_transcript(projects, "me", ask_entries(repo, answer=typed))
            assert not press.automation_answered(str(repo), "me"), typed

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
            assert not press.automation_answered(str(repo), "me"), value
        use, result = ask_entries(repo)
        assert result["isSidechain"] is False
        write_transcript(projects, "me", [use, result])
        assert press.automation_answered(str(repo), "me")

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
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_a_result_not_linked_to_an_ask(self, projects, repo):
        """S6 (b). A Bash result can echo *The user answered: "automation"*, and
        even carry the answer's shape, but its `tool_use_id` names a Bash call.
        Seen red by dropping the id link from `automation_answered`."""
        bash = ask_entries(repo, tool="Bash", tool_id="toolu_01bash")
        # An AskUserQuestion elsewhere in the file, so the link is what decides.
        other = ask_entries(repo, answer="per axis", tool_id="toolu_01other")
        write_transcript(projects, "me", other + bash)
        assert not press.automation_answered(str(repo), "me")
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
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_the_other_routing_answers(self, projects, repo):
        """S6 (c). `per axis` is the boxes, which this work does not read (Q1)."""
        for answer in ("per axis", "no work item"):
            write_transcript(projects, "me", ask_entries(repo, answer=answer))
            assert not press.automation_answered(str(repo), "me"), answer

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
            assert not press.automation_answered(str(repo), "me"), options

    def test_refuses_a_multi_select_routing_shape(self, projects, repo):
        write_transcript(projects, "me", ask_entries(repo, multi=True))
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_a_result_before_its_question(self, projects, repo):
        use, result = ask_entries(repo)
        write_transcript(projects, "me", [result, use])
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_another_sessions_answer(self, projects, repo):
        """S7. The answer belongs to the session the person was talking to."""
        write_transcript(projects, "them", ask_entries(repo))
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_an_answer_given_in_another_clone(self, projects, repo, tmp_path):
        """S7. The same session, answering from a different repository, said
        nothing about splitting this one. Seen red by dropping the clone check."""
        write_transcript(projects, "me", ask_entries(other_clone(tmp_path)))
        assert not press.automation_answered(str(repo), "me")
        write_transcript(projects, "me", ask_entries(tmp_path / "no-such-dir"))
        assert not press.automation_answered(str(repo), "me")
        use, result = ask_entries(repo)
        del result["cwd"]
        write_transcript(projects, "me", [use, result])
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_an_unreadable_transcript(self, projects, repo):
        """S8. Every way of not finding the answer lands on the old behaviour."""
        assert not press.automation_answered(str(repo), "me")  # no transcript at all
        d = projects / "-Users-x-repo" / "me.jsonl"
        d.mkdir(parents=True)  # a directory where the file would be
        assert not press.automation_answered(str(repo), "me")
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
        assert not press.automation_answered(str(repo), "me")
        use, result = ask_entries(repo)
        del result["toolUseResult"]["answers"]
        write_transcript(projects, "me", [use, result])
        assert not press.automation_answered(str(repo), "me")
        use, result = ask_entries(repo)
        result["toolUseResult"] = "a string"
        result["message"]["content"] = "a string"
        write_transcript(projects, "me", [use, result])
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_two_transcripts_for_one_session(self, projects, repo):
        """Choosing one of two would be a guess about which the harness meant."""
        write_transcript(projects, "me", ask_entries(repo), slug="-a")
        write_transcript(projects, "me", ask_entries(repo), slug="-b")
        assert not press.automation_answered(str(repo), "me")

    def test_refuses_both_shapes_that_raised_without_raising(self, projects, repo):
        """The two shapes round 1 found raising are each read as no press, and
        neither raises."""
        use, result = ask_entries(repo)
        result["message"]["content"][0]["tool_use_id"] = ["toolu_01routing"]
        write_transcript(projects, "me", [use, result])
        assert press.automation_answered(str(repo), "me") is False
        assert press.automation_answered(str(repo), "me", "/x/\x00y/me.jsonl") is False

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
        assert press.automation_answered(str(repo), PRESSED)


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
        assert press._routing_preset(preset_result(multiSelect=False))

    def test_refuses_a_question_whose_multi_select_is_absent(self):
        """The routing question is single-select, and `multiSelect` must say
        so: an absent field is a shape nobody measured, so it is not read as
        single-select."""
        assert not press._routing_preset(preset_result())


class Test_module:
    def test_a_session_id_that_reduces_to_nothing_has_no_transcript(
        self, projects, repo
    ):
        for session in ("", ".", "..", "/"):
            assert press.transcript_for(session) == "", session

    def test_no_case_reads_the_real_projects_root(self):
        """`tests/conftest.py`'s autouse fixture points the gates' copy of the
        reader at an empty directory, so a case that builds no transcript cannot
        find one belonging to whoever runs the suite. Seen red by deleting the
        fixture's `setattr`."""
        real = os.path.join(os.path.expanduser("~"), ".claude", "projects")
        assert real != GATE.press.PROJECTS_ROOT
        assert not os.listdir(GATE.press.PROJECTS_ROOT)

    def test_the_press_reader_reads_nothing_for_a_root_that_is_no_clone(self, tmp_path):
        """The gate's `top` is always a clone, so this is the reader's own half:
        a transcript it cannot place is unread, never "not answered"."""
        write_the_transcript(tmp_path / "cwd")
        path = payload(tmp_path / "cwd")["transcript_path"]
        nowhere = tmp_path / "no-repository"
        nowhere.mkdir()
        answer = press.last_routing_answer(str(nowhere), SESSION, path)
        assert answer is press.UNREAD, answer

    def test_the_labels_match_the_routing_question_the_orchestrator_asks(self):
        """The reader's constants against `skills/implement/orchestration.md`
        *Question 1*. Relabelling the question there turns this red instead of
        quietly reading every press as none. Seen red by editing a constant."""
        root = pathlib.Path(ROOT)
        text = (root / "skills" / "implement" / "orchestration.md").read_text(
            encoding="utf-8"
        )
        section = text.split("\n### Question 1\n", 1)[1].split("\n### ", 1)[0]
        labels = [
            row.split("|")[2].strip().strip("*")
            for row in section.splitlines()
            if row.startswith("| ") and row.split("|")[1].strip().isdigit()
        ]
        assert tuple(labels) == press.ROUTING_LABELS
        assert labels[0] == press.PRESET


test_census = census_case(TARGET)
