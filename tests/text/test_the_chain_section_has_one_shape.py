"""A chain-routed pull request body carries one chain section, in one shape:
what the rounds found is the copy's *Review rounds* section, and the
comparison table opens the orchestrator's part (#1044), the body's first
part since #1148.

Two bodies of the same chain came out unreadable side by side. PR #162 wrote
that section as prose and PR #168 as a table, so the numbers a reader wants to
hold against each other sat in two different shapes -- which is the whole of
what a fixed set of rows buys. `skills/commit-pr-convention/SKILL.md`
*Pull request bodies* is where a session writing a body actually reads, so
that is where the shape is stated.

Why this is its own file rather than a case in an existing module. The two
modules that already read this skill are about something else:
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` pins the language
row and nothing but it, and `tests/text/test_a_segment_feeds_the_flow_log.py` pins
`skills/verify/SKILL.md`'s measurement section, which owns the table rather
than carrying it. A reader asking why the chain section has this shape would
open neither.

The table's rows are defined in `skills/verify/orchestration.md`, and this
skill points at them. What the cases pin is what a session writing a body
acts on: the routing answer the shape holds for, and the file and section
that define the rows. The shape's sentences, and whether the skill copies
the rows, are the proofer's to read.
"""

import re

from conftest import read

SKILL = ("skills", "commit-pr-convention", "SKILL.md")


def body_section():
    """The body of `## Pull request bodies`, heading to the next `## `, as one
    line so a pinned phrase survives re-wrapping.

    Scoped rather than whole-file: this skill names the review chain in other
    sections, so a document-wide search would stay green with the section
    itself saying nothing about the shape."""
    match = re.search(
        r"^## Pull request bodies$(.*?)(?=^## )",
        read(*SKILL),
        re.M | re.S,
    )
    assert match, (
        "the pull request bodies section is gone or renamed. It is the "
        "section a session opens while writing a body, and a rename has to "
        "bring this case with it"
    )
    return " ".join(match.group(1).split())


def test_the_section_names_the_routing_answer_it_holds_for():
    """The condition the shape holds under. This skill ships to repositories
    that never run this chain, and a rule with no condition on it reads as a
    rule for them too."""
    section = body_section()
    # The `Review` routing answer `through the review chain`, which
    # `hooks/lib/routing.py#parse` reads from `routing.md`.
    assert "through the review chain" in section, (
        "the section states a shape without saying which work items it holds for"
    )


def test_the_section_points_at_the_tables_definition():
    """The rows have one owner, and this skill is a carrier that cites it."""
    section = body_section()
    # The file a session writing a body resolves for the table's rows.
    assert "skills/verify/orchestration.md" in section, (
        "the section names no owner for the table, so a session writing a "
        "body has a shape to follow and no rows to fill it with"
    )
    # The heading of that file's section that holds the rows.
    assert "Measure the segment, and feed the flow log" in section, (
        "the pointer names the file and not the section, which is a whole "
        "skill to search for one table"
    )
