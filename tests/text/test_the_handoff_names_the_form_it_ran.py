"""A handoff carried a command that has two forms, and named neither.

The handoff rule listed *the runner incantation* among what an orchestrator
hands an implementer, and said nothing about a command whose flag changes
what it reads. Issue #153 measured what that cost: a checker scoped to a work
item's own fragment was handed to every segment of one work item, three
review rounds and two fix passes all ran it and reported clean, and the
unscoped read at the pull request found fifteen drifted rows and one broken
claim — every one in a file the branch had touched.

Since 0.22.0 the handoff rule is `docs/the-review-record.md` *The handoff*
(#923).
"""

from conftest import flat


def test_the_handoff_says_which_form_of_a_command_it_carries():
    """The requirement itself. Without it the handoff carries whichever form
    somebody last found useful, which is exactly what happened."""
    record = flat("docs", "the-review-record.md")
    assert "a command with two forms names the one it means" in record, (
        "the handoff rule says nothing about a command whose flag changes "
        "what it reads — which is the whole of #153"
    )
    assert "what the other is for" in record, (
        "naming the form without naming the other form's purpose is how the "
        "narrowing got carried across in the first place"
    )
