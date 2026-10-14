"""A handoff carried a command that has two forms, and named neither.

`docs/review-handoff-protocol.md` lists *the runner incantation* among what an
orchestrator hands an implementer, and said nothing about a command whose flag
changes what it reads. Issue #153 measured what that cost: `evidence-check`
scoped to a work item's own fragment was handed to every segment of one work
item, three review rounds and two fix passes all ran it, all reported a clean
ledger, and the unscoped read at the pull request found fifteen drifted rows
and one broken claim — every one in a file the branch had touched.

Neither instruction was wrong about its own subject. The narrowing is what
keeps `--reverify` off a row whose claim is false and belongs to somebody
else, which is correct for the WRITE; it was carried into the READ, where it
blinds. So the prose has to name both forms, and a reader who only learns the
read's form deletes the narrowing and puts the write back on the false claim.

The sibling execution cases live in
`tests/test_a_narrowed_ledger_read_says_what_it_skipped.py`: the tool
announces its own narrowing, because a session that narrows on its own
initiative reads none of this. Every case here was seen red at `23c7ccb`,
before the prose existed.
"""

import os

ROOT = os.path.join(os.path.dirname(__file__), "..")


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return handle.read()


def flat(*parts):
    return " ".join(read(*parts).split())


def test_the_handoff_says_which_form_of_a_command_it_carries():
    """The requirement itself. Without it the handoff carries whichever form
    somebody last found useful, which is exactly what happened."""
    protocol = flat("docs", "review-handoff-protocol.md")
    assert "A command with more than one form names the form" in protocol, (
        "the handoff's requirements say nothing about a command whose flag "
        "changes what it reads — which is the whole of #153"
    )
    assert "what the other one is for" in protocol, (
        "naming the form without naming the other form's purpose is how the "
        "narrowing got carried across in the first place"
    )


def test_the_requirement_count_moved_with_the_requirement():
    """A fourth bullet under a sentence that says three is the list counting
    one thing and the reader counting another — and the sentence is what a
    conformance reader skims. The list took a fifth bullet in #156, and this
    case is where the count has to follow it."""
    protocol = flat("docs", "review-handoff-protocol.md")
    assert "Five requirements" in protocol
    assert "Three requirements, each bought" not in protocol
    assert "Four requirements, each bought" not in protocol
