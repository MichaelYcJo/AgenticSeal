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

#1027 changed the second reason. It was that an edit through the `Edit` tool
leaves the commit gate no command line to read, with the heredoc shape that
gate took as data; the commit gate is gone, and the reason is now that the
routing check sees only the edit tools. A case asserts the absence of the
old one: a document can gain the corrected sentence and keep the wrong one
two paragraphs down, which is how two answers ship at once. The reasons
themselves are the proofer's to read; the case that reads the contract pins
the tool's name.
"""

from conftest import flat

CONTRACT = ("skills", "agent-contract", "SKILL.md")
CRAFTER = ("agents", "crafter.md")
CARRIERS = (CONTRACT,)


def test_the_rule_names_the_tool():
    """The instruction itself, in each file that states it."""
    for parts in CARRIERS:
        text = flat(*parts)
        who = "/".join(parts)
        # The name of the tool an agent calls for a file edit.
        assert "`Edit` tool" in text, f"{who} stopped naming the tool"


def test_the_rule_no_longer_rests_on_the_commit_gate():
    """#1027 removed every gate that read a command line, the heredoc shape
    it took as data with it. A carrier that kept the old reason would send a
    session to spell a heredoc for a reader that is gone."""
    for parts in CARRIERS:
        text = flat(*parts)
        who = "/".join(parts)
        for gone in (
            "no Bash command line exists",
            "the commit gate has nothing to read",
            "one shape the gate matches byte for byte",
            "`docs/commit-review-gate-spec.md` *A file edit goes through",
        ):
            assert gone not in text, f"{who} still carries the old reason: {gone!r}"


def test_no_carrier_claims_a_fact_about_the_reader_repository():
    """Round 1's finding 2 of #34.

    These files ship as a plugin and are read inside repositories that hold
    none of its hooks. `This repository's are` is a claim about the READER's
    repository, and it is false there.
    """
    for parts in (*CARRIERS, CRAFTER, ("agents", "proofer.md")):
        text = flat(*parts)
        who = "/".join(parts)
        for loose in (
            "This repository's are",
            "and this one's are",
            "the gate's own tests are where they cluster",
        ):
            assert loose not in text, (
                f"{who} asserts something about the repository it is read in: {loose!r}"
            )


def test_the_reviewer_keeps_the_half_that_makes_the_rule_its_own():
    """What stayed in `agents/proofer.md` when contract rule 9 took the rest.

    A reviewer edits less than an implementer and would read a rule about
    edits as somebody else's. Its paragraph is the one that names what its
    own edits are -- a probe script, a scratch fixture, a file patched to see
    whether a finding reproduces -- and without it contract rule 9 arrives
    at an agent that does not think it is addressed.
    """
    proofer = flat("agents", "proofer.md")
    assert "rule 9" in proofer, "the reviewer can no longer reach the rule"
    assert "scratch fixture" in proofer, (
        "the reviewer stopped being told which of its own acts are edits"
    )
