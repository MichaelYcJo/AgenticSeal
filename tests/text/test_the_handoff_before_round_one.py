"""The step before round 1 had no protocol, and the orchestrator was blind.

Round N hands round N+1 its coordinates — `round-N.md`'s Inherited axes,
"the coordinates carry; the verdicts do not". Nothing equivalent existed for
the step before round 1: the orchestrator hands the implementer a spawn
prompt nobody's format constrains, and the one measured fact that travelled
as prose (a count standing in for a claim) cost a full review round before
anyone could check it. And while the implementer runs, the progress readout
it is already writing — `plan.md`'s Status column — is named by no document
the orchestrator reads, so "is 40 minutes normal" was answered by `git log`
twice on two consecutive work items.

Each case here was shown red before the prose it pins landed (#29).
"""

import re

from conftest import flat, read

# No TARGET: its cases hold the handoff before round 1 across docs/running/the-run.md, the implement skill and the crafter's and framer's definitions.

# --- the handoff before round 1 ---------------------------------------------


PROTOCOL = ("docs", "running", "the-run.md")


def test_the_protocol_carries_the_handoff_before_round_one():
    """The handoff names the labels a fact carries when it has no
    coordinate, by their spelling. What a handoff carries otherwise is the
    proofer's to read."""
    protocol = flat(*PROTOCOL)
    # The three labels by their spelling, which the orchestrator writes
    # beside a fact and an agent reads; `lib/fields.py` matches the
    # first two on a round record's `evidence:` line.
    assert "`executed`, `read` or `unverified`" in protocol, (
        "the labels a handoff fact carries are verify's three, by name — a "
        "fact with none is an assertion nobody has opened"
    )


def test_the_implementer_documents_point_at_the_section():
    """A protocol section nobody is routed to is the same defect one layer
    up: the answer exists and the party needing it does not know it is
    there — which is how session_cost.py went unused for a day. What stays
    in the definitions since phase 4 of #107 is the ROUTE: the section a
    prompt's facts arrive under."""
    for parts in (("skills", "implement", "SKILL.md"), ("agents", "crafter.md")):
        text = flat(*parts)
        # The path the implementer resolves to the section its prompt's
        # facts arrive under.
        assert "`docs/running/the-run.md`" in text and "handoff" in text, "/".join(
            parts
        )


# --- progress observability -------------------------------------------------


def test_the_protocol_names_the_meter():
    """The section the orchestrator reads while an agent runs names the
    script that reads the agent's transcript after the run. The progress
    channel and the stall signal are the proofer's to read."""
    protocol = flat(*PROTOCOL)
    # The script the orchestrator runs over the agent's transcript.
    assert "session_cost.py" in protocol, (
        "the meter existed through a full day of measurements nobody took, "
        "because nothing a session reads pointed at it"
    )


# --- the batching expectation in the contracts ------------------------------


def framer_rule(text, lead):
    """The `agents/framer.md` rule paragraph opening with `**<lead>**`, to the
    end of its paragraph. Scoped so a phrase elsewhere in the definition cannot
    hold one of the claims below up after the rule itself lost it."""
    match = re.search(rf"^\*\*{re.escape(lead)}\*\*(.*?)(?:\n\n|\Z)", text, re.M | re.S)
    assert match, (
        f"`agents/framer.md` has no rule opening `**{lead}**`. The opening was "
        "typed into spawn prompts from 0.12.3 and lived in no file (#640); a "
        "rename has to bring this case with it"
    )
    return " ".join(match.group(1).split())


def test_the_framers_definition_carries_its_opening():
    """#640, recommendation 1. A rule kept only in whoever last wrote a
    prompt goes missing without a trace (#107), and the framer's opening was
    exactly that: found by the 2026-09-28 sweep in no file at all.

    The bound is a rule of `agents/framer.md`, located by its lead. What it
    cites and the command it gives for a large file are held by their
    spelling; the bound's own wording is the proofer's to read."""
    text = read("agents", "framer.md")
    rule = framer_rule(text, "Bound each call, not the reading.")
    # The contract rule number the framer resolves for the rule the bound
    # applies.
    assert "rule 10" in rule, "the bound stopped citing the rule it applies"
    # The command the framer types to read a large file by range.
    assert "sed -n" in rule, (
        "the large-file half went, which is the third clause #478 recorded"
    )
