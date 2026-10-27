"""File edits go through the `Edit` tool, and the rule says why.

Nothing pinned this prose when it landed (#34): deleting both paragraphs left
the suite green, and those paragraphs were the whole of a fix that changed no
code. A change that ships only as instructions has to be held by something,
or the next sweep through these files removes it and nothing notices.

The rule is contract rule 9, which every agent receives at startup, and each
definition keeps only its own application: for `agents/proofer.md` that a
probe script and a scratch fixture are edits too, for `agents/crafter.md` the
forms a shell edit takes. So the cases assert one carrier, the contract: a
case asserting the same sentence in two files is the duplication the
contract was written to end, and `tests/test_a_moved_rule_leaves_its_definition.py`
is what refuses it.

#1027 changed the second reason. It was that an edit through the `Edit` tool
leaves the commit gate no command line to read, with the heredoc shape that
gate took as data; the commit gate is gone, and the reason is now that the
routing check sees only the edit tools. The cases assert the new reason and
the absence of the old one, following `tests/test_one_word_one_meaning.py`: a
document can gain the corrected sentence and keep the wrong one two
paragraphs down, which is how two answers ship at once.
"""

import os

from conftest import flat

ROOT = os.path.join(os.path.dirname(__file__), "..")
CONTRACT = ("skills", "agent-contract", "SKILL.md")
SMITH = ("agents", "crafter.md")
CARRIERS = (CONTRACT,)


def test_the_rule_names_the_tool_and_pairs_its_two_reasons():
    """The instruction itself, in each file that states it. One reason alone
    reads as a style preference."""
    for parts in CARRIERS:
        text = flat(*parts)
        who = "/".join(parts)
        assert "`Edit` tool" in text, f"{who} stopped naming the tool"
        assert "Two reasons point the same way" in text, f"{who} lost the pairing"
        assert "An edit must be able to fail" in text, f"{who} lost reason 1"


def test_the_rule_names_the_second_reason():
    """Reason 2 is only here: the routing check refuses at the edit tools,
    so an edit made through the shell reaches no check before the pull
    request. The warden never loads `implement`, so for every agent this is
    the only place it is stated."""
    for parts in CARRIERS:
        text = flat(*parts)
        who = "/".join(parts)
        assert "the routing check sees only the edit tools" in text, (
            f"{who} lost reason 2 -- that the routing check reads the edit tools"
        )
        assert "an edit through the shell is invisible to it" in text, (
            f"{who} lost the consequence"
        )


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
    for parts in (*CARRIERS, SMITH, ("agents", "proofer.md")):
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
    warden = flat("agents", "proofer.md")
    assert "rule 9" in warden, "the reviewer can no longer reach the rule"
    assert "scratch fixture" in warden, (
        "the reviewer stopped being told which of its own acts are edits"
    )


def test_the_implementer_keeps_the_half_that_makes_the_rule_its_own():
    """What stayed in `agents/crafter.md` when contract rule 9 took the rest.

    The reviewer's half answers *are my acts edits at all*. The smith never
    had that doubt -- it is the agent that edits -- so its half is the act
    itself, named in its `## Never` with the forms a shell edit takes.
    """
    smith = flat(*SMITH)
    assert "rule 9" in smith, "the implementer can no longer reach the rule"
    assert "Edit through the shell: no `sed -i`, no heredoc" in smith, (
        "the smith stopped being told which of its acts rule 9 rules out, and it "
        "is the agent that edits most"
    )
