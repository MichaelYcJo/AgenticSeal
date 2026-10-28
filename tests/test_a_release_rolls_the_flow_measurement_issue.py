"""What the tracker's own document says about the flow-measurement roll's
convention (#155), read against the script's constants; these cases wait for
#923.

#942's phase 6 placed the cases of
`.github/scripts/roll_flow_measurement_issue.py`'s functions in
`tests/github/test_roll_flow_measurement_issue.py`, and this file loads the script
through that file's `_roller`. `docs/issues-and-milestones.md` names this
file on its `check:` lines.

The rule lives in two places a person reads: the script's docstring, and
`docs/issues-and-milestones.md`, which is the tracker's own authority. Of
the two only the document may carry the title format --
`test_a_segment_feeds_the_flow_log.py::test_the_shipped_skill_names_no_repository_specific_tracker_state`
keeps every tracker convention that exists in this repository alone out of
`skills/verify/SKILL.md`, which ships. So the document is where a reader
learns what a title means, and the cases below read it against the constant
the script writes titles through rather than against a literal: the writer
and the document drifting apart is how a person tidies a title into a shape
the roll no longer reads.
"""

import os
import re

from test_roll_flow_measurement_issue import _roller

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOC = os.path.join(ROOT, "docs", "issues-and-milestones.md")
DOC_SECTION = "**`flow-measurement` is a label that is not an index.**"


def _tracker_section():
    """That document's `flow-measurement` section, whitespace-collapsed so a
    phrase check does not break every time the prose re-wraps."""
    with open(DOC, encoding="utf-8") as handle:
        text = handle.read()
    rest = text[text.index(DOC_SECTION) :]
    return " ".join(rest[: rest.index("\n## ")].split())


def test_the_tracker_doc_states_the_condition_the_roll_carries():
    """The document described the roll as unconditional -- it closed the
    current log and opened the next *when a release reaches `main`*. That is
    the behaviour #155 removed, and it is the sentence a person reaches for
    when they wonder why a release closed nothing. Without the condition, a
    release that rolled nothing reads as a mechanism that has broken."""
    section = _tracker_section()
    assert "opens the next when a release reaches `main`" not in section, (
        "the document is back to describing the roll as firing on every "
        "release. It fires on a push to `main` where a new version has "
        "shipped since the open log opened, and the difference is the whole "
        "of #155 -- the unconditional form closed a log the next release "
        "still needed"
    )
    assert "push to `main`" in section, (
        "the document must name the trigger the workflow actually has. A "
        "push to `main` is not the same event as a release, and the roll "
        "runs on every one of them"
    )
    assert "only where a new version has shipped" in section, (
        "the document names the trigger and not the condition, which is the "
        "half that decides whether anything happens. A reader with the "
        "trigger alone expects every push to roll the log"
    )


def test_the_tracker_doc_states_the_title_the_roll_writes():
    """The format belongs here rather than in the shipped skill, and it has
    to be the format the script actually writes. Reading the document against
    `TITLE_MARKER` and `rolled_from` is what keeps the example in it from
    becoming a title the roll would read as an old one."""
    m = _roller()
    section = _tracker_section()
    assert m.TITLE_MARKER in section, (
        f"the document never states the marker the roll writes and reads "
        f"({m.TITLE_MARKER!r}). A person retitling a log by hand has nothing "
        f"to copy, and the shipped skill may not carry it -- "
        f"`test_the_shipped_skill_names_no_repository_specific_tracker_state` "
        f"keeps this repository's tracker conventions out of it"
    )
    readable = [
        example
        for example in re.findall(r"`(chore: [^`]+)`", section)
        if m.rolled_from(example)
    ]
    assert readable, (
        "the document shows no example title the roll can read back. An "
        "example that `rolled_from` answers `None` for is an old-convention "
        "title being held up as the new one, which is the confusion this "
        "section exists to end"
    )


def test_the_tracker_doc_states_the_whole_prefix_the_roll_requires():
    """The document is where a person retitling a log by hand copies the
    format from, so the rule in it has to be the rule the code enforces. It
    said *a title with no `after` in it* was the old convention, which reads
    as: put `after` in it and the roll will find your version. The code
    requires the whole prefix from the first character, and the gap between
    those two readings is a title that stalls its log with the workflow
    green."""
    m = _roller()
    section = _tracker_section()
    assert "A title with no `after` in it" not in section, (
        "the document states a looser rule than the code enforces. A title "
        "with `after` somewhere in it is not a log this roll wrote, and a "
        "reader following this sentence writes one that answers a version "
        "the roll then reads as not due"
    )
    assert "does not begin with" in section, (
        "the document must say the prefix is required from the start of the "
        "title, not merely present in it -- that is the difference between "
        "`chore: flow measurement — after 0.8.2` and `docs: explain flow "
        "measurement — after 0.8.2`, and the second stalls its log"
    )
    assert m.TITLE_PREFIX in section, (
        f"the document must spell the whole prefix the roll writes and "
        f"requires ({m.TITLE_PREFIX!r}), read out of the script's own "
        f"constant rather than against a literal here"
    )


def test_the_tracker_doc_says_what_a_title_written_before_this_means():
    """Closed logs are not retitled (`questions.md` assumption 6), so both
    conventions are visible in the tracker forever. The document is the only
    place a person can learn that the two mean different things -- and that
    the older one is read as due rather than ignored."""
    section = _tracker_section()
    assert "predicted" in section, (
        "the document never says what an older title names. `chore: flow "
        "measurement — 0.9.0` reads exactly like the current form to anyone "
        "who was not here for the change, and it means the opposite: the "
        "version the log was predicted to be for, not the one it rolled from"
    )
    assert "not rewritten" in section, (
        "the document must say the older titles stay as they are. Without "
        "it, the obvious tidy -- retitle them into the new form -- is what a "
        "reader does next, and it falsifies every comment that cites them"
    )
    assert "due" in section, (
        "the document never says how the roll reads an older title. Read as "
        "not due it would stall that log forever with the workflow green, "
        "which is the failure class #155 is about; the direction is chosen, "
        "so it is stated"
    )
