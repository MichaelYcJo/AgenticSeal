"""question-gate: on a branch declared `Automation` `yes`, no question is put.

The person who pressed `automation` was told nothing stops to ask, and in
0.22.3 four framer questions reached them anyway, with the prose rule loaded
(#1002). The gate reads the checked-out branch's declaration through
`hooks/routing.py` and refuses `AskUserQuestion` there, except for the routing
question put alone, which a resumed run has to put again.
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

HOOKS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks")
GATE = "question-gate.py"
ITEM = "1787708604-a-work-item"

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
    p = {
        "tool_name": tool,
        "session_id": "s1",
        "tool_input": {"questions": list(questions)},
        "cwd": str(cwd),
    }
    p.update(extra)
    return p


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
    for said in (
        f"`{os.path.join(item, routing.FILENAME)}`",
        f"`{os.path.join(item, 'questions.md')}`",
        f"answers `{routing.AUTOMATION}` with `{routing.AUTOMATION_YES}`",
        "Build on the default the question states",
        "pull request body",
        "meets the same refusal",
        "The routing question put alone goes through",
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
    assert decision_of(run(repo, questions=(ROUTING_QUESTION,))) == "silent"


def test_the_routing_question_with_company_is_refused(repo):
    declare(repo)
    for questions in (
        (ROUTING_QUESTION, FRAMER_QUESTION),
        (FRAMER_QUESTION, ROUTING_QUESTION),
        (ROUTING_QUESTION, ROUTING_QUESTION),
    ):
        assert decision_of(run(repo, questions=questions)) == "deny", questions


def test_a_near_miss_of_the_routing_labels_is_refused(repo):
    """Two of the three, or a fourth beside them, is not question 1."""
    declare(repo)
    options = ROUTING_QUESTION["options"]
    for changed in (
        options[:2],
        [*options, {"label": "automation", "description": "Again."}],
        [*options, {"label": "later", "description": "A fourth."}],
    ):
        question = {**ROUTING_QUESTION, "options": changed}
        assert decision_of(run(repo, questions=(question,))) == "deny", changed


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
