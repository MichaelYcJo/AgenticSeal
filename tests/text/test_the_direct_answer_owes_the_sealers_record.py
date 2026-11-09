"""`straight to the PR` owes the broad run's `trail/gate.md`, and every document
that describes the answer says so (#241).

`chain_check.py#broad_gate` requires that file at a ready pull request: the
one broad run, at a SHA, against the base, which the orchestrator takes
before it spawns the sealer (#969). Seven places went on saying `straight to the PR` requires nothing — the
specification's declaration table, the checker's own inventory, the
orchestration skill's four-combinations table and its closing paragraph, the
commit gate's first option, that option's own test, and the routing template's
comment. A session that had written a change and checked it itself read any
of them and concluded the vocabulary had no honest answer for it, and asked
for a third one whose record it would write about itself.

The answer is two answers and not three, and the pins here are shaped so
that an absence is trivially satisfied by a file that was never opened, so the
sentence that STANDS is what makes the sentence that is GONE evidence. Where
a file never carried the false sentence — it named the two answers and what
neither owes — only the standing half is pinned.

The commit gate's option and its test left with the gate (#1027).
"""

import pytest
from conftest import REVIEW_CHAIN_DOCS, ROOT, flat, review_chain_text
from test_waiver_decided_at_start import in_force

STANDS = "the broad run's `trail/gate.md`"

# (the sentence that is gone, or None where the file never carried one; the
# sentence that stands). The standing phrase is one no other sentence of the
# same file uses, so the pin is live for the row it was written for (ledger
# R12: a whole-file substring pin is evidence only where the words occur
# nowhere else).
DIRECT_REQUIRES = {
    ("docs", "running", "the-review-and-parity-arms.md"): (
        "nothing required; the declaration is printed",
        "the broad run's `trail/gate.md`",
    ),
}
# The orchestration skill's four-combinations table and its closing paragraph
# left for the policy root in #1148, which holds both; the skill keeps one
# sentence on `straight to the PR` and cites the section that holds the rest.
# The file and function names say "the direct answer", the name that answer
# had until #1459, because `.test_durations` keys the cases by name.
WAIVER_SECTION = (
    "`docs/running/the-review-and-parity-arms.md` *There is no standing waiver*"
)


@pytest.mark.parametrize("parts", sorted(DIRECT_REQUIRES))
def test_each_carrier_says_what_the_direct_answer_requires(parts):
    """A8. A reader opening any of these places finds what `straight to
    the PR` requires at a ready pull request and no sentence saying it
    requires nothing. Seen red by restoring one of the old sentences."""
    gone, stands = DIRECT_REQUIRES[parts]
    text = flat(*parts)
    assert stands in text, (
        f"{'/'.join(parts)} does not say `straight to the PR` owes the sealer's "
        "record, so the absence below is a search that found nothing rather "
        "than a file that says nothing"
    )
    if parts in REVIEW_CHAIN_DOCS:
        # The sentence left the spec when the spec was split (#526); it must
        # not come back in either sibling.
        text = review_chain_text(ROOT)
    if gone is not None:
        assert gone not in text, (
            f"{'/'.join(parts)} still tells a reader `straight to the PR` "
            "requires nothing, beside a checker that requires the sealer's "
            "record"
        )


def test_the_routing_section_cites_what_checks_the_direct_answer():
    """What checks `straight to the PR` is the sealer's record at the pull
    request, and the orchestration skill's sentence on that answer cites the
    policy section that says so."""
    text = flat("skills", "implement", "orchestration.md")
    # The section an orchestrator resolves to learn what checks
    # `straight to the PR`.
    assert WAIVER_SECTION in text, (
        "the skill does not cite the section that says what checks `straight to the PR`"
    )


def test_the_release_checklist_names_the_waiver_as_the_no_work_item_answer():
    """Item 9: a release's commit that belongs to no work item, a settle's
    among them, declares its class — the routing question's `direct` answer
    (`no work item` until #1459), whose recorded form is the
    `Seal-Routing: no work item` trailer on each commit — rather than
    stepping around a gate. The step is read as the policy in force: the
    section as the root holds it with each pending `## Rule changes` item
    applied, because #1459's rule change renames the answer there at the
    settle, and the case reads `direct` before the settle and after it."""
    text = in_force(
        "docs/releasing/release-checklist.md",
        "2b. Settle what earlier releases left behind",
    )
    # The routing answer `direct`, the code span, which a session gives the
    # routing question for such a commit.
    assert "`direct` answer" in text, (
        "`docs/releasing/release-checklist.md` *2b. Settle what earlier releases "
        "left behind*, as in force, does not name the waiver as the routing "
        "question's `direct` answer"
    )
