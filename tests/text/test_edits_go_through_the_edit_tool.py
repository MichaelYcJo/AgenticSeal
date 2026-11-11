"""File edits go through the `Edit` tool, and the rule says why.

Nothing pinned this prose when it landed (#34): deleting both paragraphs left
the suite green, and those paragraphs were the whole of a fix that changed no
code. A change that ships only as instructions has to be held by something,
or the next sweep through these files removes it and nothing notices.

The rule is contract rule 9, which every agent receives at startup, and each
definition keeps only its own application: for `agents/proofer.md`, that a
probe script and a scratch fixture are edits too. So the cases assert one carrier, the contract: a
case asserting the same sentence in two files is the duplication the
contract was written to end, and `tests/text/test_a_moved_rule_leaves_its_definition.py`
is what refuses it.

#1027 changed the second reason, and #1376 took it out. No check reads an
edit now, and the reason that stands is the first: an edit must be able to
fail. The reason is the proofer's to read; the case that reads the contract
pins the tool's name.
"""

from conftest import flat

CONTRACT = ("skills", "agent-contract", "SKILL.md")
CARRIERS = (CONTRACT,)


def test_the_rule_names_the_tool():
    """The instruction itself, in each file that states it."""
    for parts in CARRIERS:
        text = flat(*parts)
        who = "/".join(parts)
        # The name of the tool an agent calls for a file edit.
        assert "`Edit` tool" in text, f"{who} stopped naming the tool"


def test_the_reviewer_points_at_the_edit_rule():
    """What stayed in `agents/proofer.md` when contract rule 9 took the rest:
    the rule's number, which the proofer resolves. Which of its own acts the
    paragraph names as edits is the proofer's to read."""
    proofer = flat("agents", "proofer.md")
    # The contract rule number the proofer resolves for the rule on edits.
    assert "rule 9" in proofer, "the reviewer can no longer reach the rule"
