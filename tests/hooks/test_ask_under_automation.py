"""`hooks/ask-under-automation.py`: while an open work item of the session's
repository reads `Automation` `yes`, an `AskUserQuestion` call is refused
unless each of its questions states why its default cannot be taken.

The hook prints a `PreToolUse` deny object or nothing, and exits 0 on every
path (#1608). The cases run the hook's command as `hooks/hooks.json` spells
it, through `tests/hooks/test_core_start.py#start`: its `python3` half with
this interpreter in place of `python3` and `${CLAUDE_PLUGIN_ROOT}` filled
in. Which work items are open is `tests/lib/test_routing.py`'s
`Test_open_declarations`, and the registration is held by
`tests/behaviour/test_chain_hooks_hardening.py`.
"""

import json
import os

from conftest import ROOT, census_case, declare_automation, git, git_repo, load
from test_core_start import start

TARGET = "hooks/ask-under-automation.py"

hook = load(TARGET, "agentic_ask_under_automation")

EVENT = "PreToolUse"
ITEM = "1780000000-a-work-item"
BRANCH = "feature/x"

# The document the hook reads the rule from, and its section, which the
# refusal names where the paragraph cannot be read.
DOC = "docs/running/the-run.md"


def paragraph(root=ROOT):
    """The lines of `DOC` under ROOT from the one opening with `hook.LEAD`
    to the blank line after it, as the tree's own document holds them."""
    with open(os.path.join(root, *DOC.split("/")), encoding="utf-8") as f:
        lines = f.read().split("\n")
    (at,) = [i for i, line in enumerate(lines) if line.startswith(hook.LEAD)]
    end = lines.index("", at)
    return lines[at:end]


def declared(where, answer="yes", branch=BRANCH):
    """A repository at WHERE on `feature/x`, whose root holds `ITEM`'s
    `routing.md` naming BRANCH, its `Automation` row reading ANSWER."""
    repo = git_repo(where)
    git(repo, "checkout", "-q", "-b", BRANCH)
    declare_automation(repo / "seal", answer, branch, ITEM)
    return repo


def question(text, header="Scope"):
    """One question in the shape an `AskUserQuestion` call's input holds."""
    options = [
        {"label": "a", "description": "one"},
        {"label": "b", "description": "two"},
    ]
    return {
        "question": text,
        "header": header,
        "multiSelect": False,
        "options": options,
    }


def asked(cwd, *questions):
    """The `PreToolUse` payload of an `AskUserQuestion` call from CWD."""
    return json.dumps(
        {
            "cwd": str(cwd),
            "hook_event_name": EVENT,
            "tool_name": "AskUserQuestion",
            "tool_input": {"questions": list(questions)},
        }
    )


def run(body, root=None):
    """The hook's stdout for BODY, `CLAUDE_PLUGIN_ROOT` at ROOT or unset."""
    return start(body, root=root, event=EVENT)


def refused(out):
    """The reason of the deny object OUT holds whole, and nothing else."""
    said = json.loads(out)
    assert list(said) == ["hookSpecificOutput"], said
    held = said["hookSpecificOutput"]
    assert held["hookEventName"] == EVENT, held
    assert held["permissionDecision"] == "deny", held
    assert sorted(held) == [
        "hookEventName",
        "permissionDecision",
        "permissionDecisionReason",
    ], held
    return held["permissionDecisionReason"]


class Test_main:
    """The pairs differ by the payload's questions, or by the tree the
    fixture builds: whether a work item is open and reads `yes`, and which
    plugin root holds the rule."""

    def test_refuses_a_question_under_automation_yes_with_the_rule(self, tmp_path):
        """S1. The reason holds the paragraph of `DOC` *The run* from its
        first line to its last, read from the plugin root the hook stands
        in, and names the open work item and its branch."""
        repo = declared(tmp_path / "repo")
        reason = refused(run(asked(repo, question("Which scope?"))))
        lines = paragraph()
        assert lines[0] in reason and lines[-1] in reason, reason
        assert ITEM in reason and BRANCH in reason, reason
        assert '"Scope"' in reason, reason

    def test_accepts_a_call_whose_every_question_states_why(self, tmp_path):
        """S2. Each question holds `No default:` and a reason on its line,
        so the call goes through."""
        repo = declared(tmp_path / "repo")
        body = asked(
            repo,
            question("Ship it? No default: it reaches the owner's account.", "Ship"),
            question("Which key?\nNo default: the key is the owner's.", "Key"),
        )
        assert run(body) == ""

    def test_refuses_a_call_one_of_whose_questions_does_not_state_why(self, tmp_path):
        """S3. Each question is its own stop, so one stated reason does not
        carry another; the reason names the header of the one that does not,
        and of no other."""
        repo = declared(tmp_path / "repo")
        body = asked(
            repo,
            question("Ship it? No default: it reaches the owner's account.", "Ship"),
            question("Which name?", "Naming"),
        )
        reason = refused(run(body))
        assert '"Naming"' in reason and '"Ship"' not in reason, reason

    def test_refuses_a_marker_with_nothing_after_it_on_its_line(self, tmp_path):
        """A marker with no reason after it on its line states nothing."""
        repo = declared(tmp_path / "repo")
        body = asked(repo, question("Which name? No default:\nthe owner's.", "Name"))
        assert '"Name"' in refused(run(body))

    def test_refuses_a_marker_in_another_case_and_names_it_as_not_read(self, tmp_path):
        """S4. `no default: x` is not the form, so the call is refused, and
        the reason says the hook did not read that spelling."""
        repo = declared(tmp_path / "repo")
        reason = refused(run(asked(repo, question("Which? no default: x", "Near"))))
        assert '"Near" holds `no default:`, which this hook does not read' in reason

    def test_accepts_a_tree_where_no_open_work_item_reads_yes(self, tmp_path):
        """S5. A `no` on the checked-out branch, a `yes` for a branch no
        worktree has checked out, a repository with no root and a directory
        outside git each let the call through."""
        plain = git_repo(tmp_path / "plain")
        outside = tmp_path / "outside"
        outside.mkdir()
        for cwd in (
            declared(tmp_path / "no", answer="no"),
            declared(tmp_path / "released", branch="feature/released"),
            plain,
            outside,
        ):
            assert run(asked(cwd, question("Which scope?"))) == "", cwd

    def test_accepts_a_payload_that_is_not_json_and_prints_nothing(self, tmp_path):
        """S7. A payload that is not a JSON object, under S1's repository,
        prints nothing, writes nothing to stderr and exits 0 (`start`
        asserts the last two)."""
        repo = declared(tmp_path / "repo")
        for body in ("not json", "[1]", json.dumps({"cwd": 7})):
            assert run(body) == "", body
        assert run(asked(repo, question("Which scope?"))) != ""

    def test_accepts_a_payload_with_no_question_list_and_prints_nothing(self, tmp_path):
        """S7. An input with no question list, an empty one, or a question
        with no string `question`, under S1's repository, prints nothing,
        writes nothing to stderr and exits 0."""
        repo = declared(tmp_path / "repo")
        for tool_input in ({}, {"questions": []}, {"questions": [{"header": "x"}]}):
            body = json.dumps({"cwd": str(repo), "tool_input": tool_input})
            assert run(body) == "", tool_input

    def test_refuses_with_the_coordinate_where_the_paragraph_is_gone(self, tmp_path):
        """S9. Under a plugin root whose `DOC` lacks the paragraph, the
        reason names the document, its section and the paragraph's lead in
        the paragraph's place."""
        root = tmp_path / "plugin"
        (root / "docs" / "running").mkdir(parents=True)
        (root / "docs" / "running" / "the-run.md").write_text(
            "# The run\n\nAnother paragraph.\n", encoding="utf-8"
        )
        repo = declared(tmp_path / "repo")
        reason = refused(run(asked(repo, question("Which scope?")), root=root))
        # The sentence that stands in the paragraph's place: its document,
        # its section and the opening of its first line.
        said = f"`{DOC}` *The run* that opens with: {hook.LEAD}"
        assert said in reason, reason
        assert paragraph()[-1] not in reason, reason


test_census = census_case(TARGET)
