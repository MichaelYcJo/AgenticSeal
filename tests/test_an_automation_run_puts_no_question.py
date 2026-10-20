"""question-gate: on a branch declared `Automation` `yes`, no question is put.

The person who pressed `automation` was told nothing stops to ask, and in
0.22.3 four framer questions reached them anyway, with the prose rule loaded
(#1002). The gate reads the checked-out branch's declaration through
`hooks/routing.py` and refuses `AskUserQuestion` there, except for the routing
question put alone, which a resumed run has to put again, until the session
has answered it.
"""

import json
import os
import shutil
import subprocess
import sys

from conftest import (
    decision_of,
    declare_routing,
    load_hook_module,
    local_home,
    run_hook,
)
from test_the_guard_asks_once_per_session import ask_entries, write_transcript

HOOKS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks")
GATE = "question-gate.py"
ITEM = "1787708604-a-work-item"
SESSION = "s1"

routing = load_hook_module("routing.py", "routing_for_question_gate")

FRAMER_QUESTION = {
    "question": "Which default should the hook print?",
    "header": "Default",
    "options": [
        {"label": "The short one", "description": "One sentence."},
        {"label": "The long one", "description": "Three sentences."},
    ],
    "multiSelect": False,
}

ROUTING_QUESTION = {
    "question": "How is this work routed?",
    "header": "Routing",
    "options": [
        {"label": "automation (Recommended)", "description": "Every party runs."},
        {"label": "per axis", "description": "The four boxes are the answer."},
        {"label": "no work item", "description": "No work item is opened."},
    ],
    "multiSelect": False,
}


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()


def declare(repo, automation="yes", home=None, review="through the review chain"):
    """The work-item directory of a declaration naming `repo`'s branch, with an
    `Automation` row unless `automation` is None."""
    item = declare_routing(repo, item=ITEM, review=review, home=home)
    if automation is not None:
        with open(item / "routing.md", "a", encoding="utf-8") as f:
            f.write(f"| {routing.AUTOMATION} | {automation} |\n")
    return item


def payload(cwd, questions=(FRAMER_QUESTION,), tool="AskUserQuestion", **extra):
    """A call from session `s1`, whose transcript is a path beside `cwd` that
    holds nothing unless a case writes it, so no case reads a real one."""
    p = {
        "tool_name": tool,
        "session_id": SESSION,
        "transcript_path": os.path.join(
            os.path.dirname(str(cwd)), "transcripts", f"{SESSION}.jsonl"
        ),
        "tool_input": {"questions": list(questions)},
        "cwd": str(cwd),
    }
    p.update(extra)
    return p


def write_the_transcript(cwd, entries=()):
    """Write the session's transcript at the path `payload` names."""
    write_transcript(os.path.dirname(str(cwd)), SESSION, entries, slug="transcripts")


def answer_the_routing_question(cwd, answer="automation (Recommended)"):
    """The session's transcript, holding the routing question answered from
    `cwd`."""
    write_the_transcript(cwd, ask_entries(cwd, answer=answer))


def run(cwd, **kwargs):
    return run_hook(GATE, payload(cwd, **kwargs))


def reason_of(stdout):
    return json.loads(stdout)["hookSpecificOutput"]["permissionDecisionReason"]


# --- S1, S2: the promise is read and every call is refused ------------------


def test_a_question_on_a_branch_declared_automation_is_refused(repo):
    declare(repo)
    assert decision_of(run(repo)) == "deny"


def test_the_refusal_says_where_the_default_goes(repo):
    """Contract §14: the reason is what the session acts on."""
    declare(repo)
    reason = reason_of(run(repo))
    item = os.path.join("seal", "specs", ITEM)
    assert reason.count(item) == 1, reason
    for said in (
        f"`{item}`",
        f"`{routing.FILENAME}`",
        "`questions.md`",
        f"answers `{routing.AUTOMATION}` with `{routing.AUTOMATION_YES}`",
        "Build on the default the question states",
        "pull request body",
        "states no default",
        "hand that stop back at the end of the run",
        "meets the same refusal",
        "The routing question put alone goes through only until this session "
        "has answered it here",
    ):
        assert said in reason, said


def test_every_call_is_refused_and_nothing_is_written(repo):
    declare(repo)
    git_dir = git(repo, "rev-parse", "--absolute-git-dir")

    def tree():
        return sorted(
            os.path.join(where, name)
            for where, dirs, files in os.walk(git_dir)
            for name in dirs + files
        )

    before = tree()
    assert decision_of(run(repo)) == "deny"
    assert decision_of(run(repo)) == "deny"
    assert tree() == before


# --- S3, S4, S5: every other reading of the declaration is attended ---------


def test_a_declaration_that_promised_nothing_is_silent(repo):
    for automation in (routing.AUTOMATION_NO, None, "Yes", "`yes`", "yes please"):
        declare(repo, automation=automation)
        assert decision_of(run(repo)) == "silent", automation
        shutil.rmtree(repo / "seal")


def test_no_seal_is_silent(repo):
    assert decision_of(run(repo)) == "silent"


def test_a_seal_with_no_declaration_for_the_branch_is_silent(repo):
    declare(repo)
    git(repo, "switch", "-q", "feature/x")
    assert decision_of(run(repo)) == "silent"


def test_a_declaration_that_does_not_parse_is_silent(repo):
    declare(repo, review="through the chain")
    assert decision_of(run(repo)) == "silent"


def test_two_declarations_naming_the_branch_are_silent(repo):
    item = declare(repo)
    shutil.copytree(item, item.parent / "1787708605-a-second-item")
    assert decision_of(run(repo)) == "silent"


def test_a_detached_head_is_silent(repo):
    declare(repo)
    git(repo, "switch", "-q", "--detach")
    assert decision_of(run(repo)) == "silent"


# --- S6, S7: the branch and the root resolve as the commit gate's do -------


def test_a_linked_worktree_reads_its_own_branch(repo, tmp_path):
    wt = tmp_path / "wt"
    git(repo, "worktree", "add", "-q", str(wt), "-b", "fix/x")
    item = declare(wt)
    shutil.copytree(item, repo / "seal" / "specs" / ITEM)
    assert decision_of(run(wt)) == "deny"
    assert decision_of(run(repo)) == "silent"


def test_a_root_under_the_common_git_directory_is_read(repo):
    declare(repo, home=local_home(repo))
    assert not (repo / "seal").exists()
    assert decision_of(run(repo)) == "deny"


# --- S8, S9, S10: the routing question alone goes through ------------------


def test_the_routing_question_put_alone_goes_through(repo):
    declare(repo)
    write_the_transcript(repo)
    assert decision_of(run(repo, questions=(ROUTING_QUESTION,))) == "silent"


def test_the_routing_question_is_refused_where_no_transcript_can_be_read(repo):
    """The press readers read the same transcript, so where it cannot be read
    no gate would find the press the question exists to record (round 2,
    finding 1)."""
    declare(repo)
    nameless = payload(repo, questions=(ROUTING_QUESTION,))
    del nameless["session_id"]
    assert decision_of(run_hook(GATE, nameless)) == "deny"
    assert decision_of(run(repo, questions=(ROUTING_QUESTION,))) == "deny", (
        "a transcript path that names no file"
    )


def test_the_routing_question_with_company_is_refused(repo):
    declare(repo)
    for questions in (
        (ROUTING_QUESTION, FRAMER_QUESTION),
        (FRAMER_QUESTION, ROUTING_QUESTION),
        (ROUTING_QUESTION, ROUTING_QUESTION),
    ):
        assert decision_of(run(repo, questions=questions)) == "deny", questions


def test_a_near_miss_of_the_routing_question_is_refused(repo):
    """Two of the three labels, a fourth beside them, a multi-select, or no
    question text is not question 1 as the press reader counts it, and its
    answer would take an earlier press back (round 1, finding 1)."""
    declare(repo)
    options = ROUTING_QUESTION["options"]
    for changed in (
        {**ROUTING_QUESTION, "options": options[:2]},
        {
            **ROUTING_QUESTION,
            "options": [*options, {"label": "automation", "description": "Again."}],
        },
        {
            **ROUTING_QUESTION,
            "options": [*options, {"label": "later", "description": "A fourth."}],
        },
        {**ROUTING_QUESTION, "multiSelect": True},
        {k: v for k, v in ROUTING_QUESTION.items() if k != "multiSelect"},
        {k: v for k, v in ROUTING_QUESTION.items() if k != "question"},
    ):
        assert decision_of(run(repo, questions=(changed,))) == "deny", changed


DRESSED_FRAMER_QUESTION = {
    **FRAMER_QUESTION,
    "options": [
        {"label": "automation - keep the short default", "description": "d"},
        {"label": "per axis - switch to the long default", "description": "d"},
        {"label": "no work item - print nothing", "description": "d"},
    ],
}


def test_the_routing_question_goes_through_only_until_it_is_answered(repo):
    """The exemption is for the resumed session that has to record its press
    once. After any answer from this clone, every question is refused, the
    routing question and one dressed in its labels included; no list of
    spellings could close that second shape (round 1, finding 1)."""
    declare(repo)
    write_the_transcript(repo)
    assert decision_of(run(repo, questions=(ROUTING_QUESTION,))) == "silent"
    write_transcript(
        repo.parent,
        SESSION,
        ask_entries(
            repo,
            answer="The short one",
            options=("The short one", "The long one"),
            question=FRAMER_QUESTION["question"],
        ),
        slug="transcripts",
    )
    assert decision_of(run(repo, questions=(ROUTING_QUESTION,))) == "silent", (
        "an answer to another question is no answer to the routing question"
    )
    for answer in ("automation (Recommended)", "per axis"):
        answer_the_routing_question(repo, answer=answer)
        for question in (ROUTING_QUESTION, DRESSED_FRAMER_QUESTION):
            out = run(repo, questions=(question,))
            assert decision_of(out) == "deny", (answer, question)


def test_an_unreadable_call_is_refused(repo):
    declare(repo)
    for tool_input in (
        {},
        {"questions": "How is this work routed?"},
        {"questions": [ROUTING_QUESTION["question"]]},
        {"questions": [{**ROUTING_QUESTION, "options": None}]},
        None,
    ):
        p = payload(repo)
        p["tool_input"] = tool_input
        assert decision_of(run_hook(GATE, p)) == "deny", tool_input


# --- S11: the tool is named exactly -----------------------------------------


def test_any_other_tool_name_is_silent(repo):
    declare(repo)
    for tool in ("askuserquestion", "AskUserQuestion ", "mcp__x__AskUserQuestion"):
        assert decision_of(run(repo, tool=tool)) == "silent", tool
    p = payload(repo)
    del p["tool_name"]
    assert decision_of(run_hook(GATE, p)) == "silent"


def test_a_payload_that_names_no_directory_is_silent(repo):
    """Run from inside a declared repository, so a gate that read its own
    process directory for a missing `cwd` would refuse."""
    declare(repo)
    nameless = payload(repo)
    del nameless["cwd"]
    for stdin in ("[1, 2]", "not json", json.dumps(nameless)):
        r = subprocess.run(
            [sys.executable, os.path.join(HOOKS, GATE)],
            input=stdin,
            cwd=str(repo),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        assert (r.returncode, r.stdout) == (0, ""), stdin


# --- S12: registered, and reached through the dispatcher -------------------


def test_the_gate_is_registered_on_the_question_tool():
    dispatch = load_hook_module("dispatch.py", "dispatch_for_question_gate")
    groups = [g for g, gates in dispatch.GROUPS.items() if GATE in gates]
    assert groups == ["pre-question"], groups
    with open(os.path.join(HOOKS, "hooks.json"), encoding="utf-8") as f:
        entries = json.load(f)["hooks"]["PreToolUse"]
    commands = [
        h["command"]
        for e in entries
        if e["matcher"] == "AskUserQuestion"
        for h in e["hooks"]
    ]
    run_group = '"${CLAUDE_PLUGIN_ROOT}/hooks/dispatch.py" pre-question'
    assert commands == [f"python3 {run_group} || py -3 {run_group}"], commands


ROOT = os.path.join(HOOKS, "..")


def flat(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return " ".join(f.read().split())


def test_the_prose_points_to_the_gate_and_no_longer_says_nothing_holds_it():
    """S14: the orchestrator's two documents name the gate, and none of the
    sentences `spec.md` `## Removes` lists still stands."""
    skill = flat("skills", "implement", "SKILL.md")
    first = skill.split("### 1. Read the spec before the code", 1)[1]
    assert f"`hooks/{GATE}`" in first.split("### 2.", 1)[0]
    assert f"`hooks/{GATE}`" in flat("skills", "implement", "orchestration.md")
    for parts, sentence in (
        (("skills", "implement", "orchestration.md"), "audit trail, not a gate"),
        (
            ("skills", "implement", "orchestration.md"),
            "in the same call as whatever else the resume has to ask",
        ),
        (("hooks", "routing.py"), "Nothing gates on it and nothing can"),
        (("hooks", "routing.py"), "nothing CAN decide one on"),
        (("templates", "sdd-routing.md"), "can hold a run to it"),
    ):
        assert sentence not in flat(*parts), (parts, sentence)


def test_the_dispatcher_carries_the_refusal(repo):
    declare(repo)
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), "pre-question"],
        input=json.dumps(payload(repo)),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    assert decision_of(r.stdout) == "deny", r.stdout
