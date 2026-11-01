"""An agent commits with its repository written out, in the form rule 16 names.

Contract rule 16 is the written half of work item `1790644505` (#662, #665). The
gate half refuses, in an `automation` run, every commit it stops; this half is
what makes the refusal rare. Both were measured to be needed: in the
milestone-49 run three of the four stops that reached the person began
`cd <worktree> &&` and committed after a `;` or a new line, and the
orchestrator's loop over a variable met the gate in all three milestone runs.

The cases read the rule's number, its heading and the `git -C` form an agent
types, and the orchestration's citation of the rule. The rule's reason is the
proofer's to read.
#1027 removed every gate that read a commit, and the reason that rested on
that reading went with it; the shell's starting directory is the one left.
The rule points at contract rule 9 rather than restating it, and
`tests/text/test_a_moved_rule_leaves_its_definition.py` is what refuses a copy.
"""

from conftest import read
from test_the_agent_contract_holds_the_universal_rules import HEADING

CONTRACT = ("skills", "agent-contract", "SKILL.md")
ORCHESTRATION = ("skills", "implement", "orchestration.md")


def section(number):
    text = read(*CONTRACT)
    heads = list(HEADING.finditer(text))
    for i, m in enumerate(heads):
        if int(m.group(1)) == number:
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            return m.group(2), " ".join(text[m.end() : end].split())
    return None, ""


def test_the_rule_is_section_sixteen_and_names_the_shape():
    heading, body = section(16)
    # The contract rule number 16, which `skills/implement/orchestration.md`
    # and the agent definitions cite: an agent resolving the citation reaches
    # this heading.
    assert heading == "A commit names its repository in the command that makes it"
    # The command form `git -C <absolute path>`, which every agent types when
    # it commits.
    assert "absolute path written out after `git -C`, in a command of its own" in body


def test_no_reason_rests_on_a_gate_reading_the_command():
    """#1027: nothing reads a commit's command any more, so a reason that
    said what such a reader could place would send a session after a gate
    that is gone."""
    _, body = section(16)
    for gone in ("the gate", "Two reasons", "loop variable"):
        assert gone not in body, f"rule 16 still rests on the reading: {gone!r}"


def test_it_points_at_the_edit_rule_rather_than_restating_it():
    _, body = section(16)
    assert "rule 9" in body
    for copied in ("subprocess.run", "An edit must be able to fail"):
        assert copied not in body, f"rule 16 restates a neighbour: {copied!r}"


def test_the_orchestration_cites_contract_rule_16():
    """The loop over `$wt`, `$1` and `$d` was the orchestrator's, in all three
    milestone runs on disk. How the orchestration applies the rule to its
    routing files is the proofer's to read."""
    text = " ".join(read(*ORCHESTRATION).split())
    # The contract rule number the orchestrator resolves when it commits its
    # routing files.
    assert "contract rule 16" in text
