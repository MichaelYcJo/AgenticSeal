"""A `questions.md` row said what was being asked and never who could answer
it, so three kinds of question wore one shape on the page.

#84's second comment measured all three inside one run's four rows. One of
them was a **measurement** sitting in the human batch: six probes at about
three seconds each settled it, and they showed the issue's own instruction was
wrong. Queued behind a person it would have cost a round trip and returned an
opinion, which is the wrong instrument for it. A third kind — **the work** —
cannot be answered at framing time by anybody, and holding it open waits for
somebody who was never coming.

Two documents carry the consequence and this module pins both.

  the template   `templates/sdd-questions.md` is the file a session types
                 into. The column has to be in the shipped table, because a
                 session bootstraps from the template and never reads the
                 argument for it; the argument, the three values and who
                 writes `Status`, is `skills/implement/SKILL.md` *3. The SDD
                 file set*, which the framer opens
  the report     `agents/framer.md`'s hand-back step and its person-row rule
                 split on the same three values. A row a PERSON answers goes
                 to the orchestrator in full; the other two are a path and a
                 count, because there is nothing in them for the reader to
                 act on

The report half is the one that is easy to get backwards, and it was
backwards: the rule read *never the rows' text*, unconditionally, resting on
contract rule 5's *an aggregate is not a coordinate*. That rule is about a claim a reader
might believe and act on without opening it. A question a person must answer
is not a claim — it is the asking itself, and an approval given against a
count of questions is an approval given against nothing.
"""

import os
import re

from conftest import read

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

ANSWERERS = ("a person", "a measurement", "the work")


def flat(*parts):
    """Whitespace-normalised, so a re-wrap of the same sentence is not a
    failure. These files are hand-wrapped and the sentences move columns."""
    return " ".join(read(*parts).split())


# --- the template -----------------------------------------------------------


def test_the_questions_template_carries_the_answerer_column():
    """S7 of #84. The column is in the shipped table or it does not exist:
    a session copies `templates/sdd-questions.md` and writes rows into
    whatever header it finds there."""
    tpl = read("templates", "sdd-questions.md")
    header = (
        "| # | Question | Who can answer | Options & what each implies "
        "| Default until answered | Status |"
    )
    assert header in tpl, (
        "`templates/sdd-questions.md` has no `Who can answer` column in its "
        "table header. Prose about the three kinds is worth nothing here -- "
        "the header is what a session fills in"
    )
    body = tpl[tpl.index(header) :]
    assert "|---|---|---|---|---|---|" in body, (
        "the separator row still has the old column count, so the table "
        "renders with the answerer cell folded into its neighbour"
    )


def test_the_skill_names_the_three_answerers_and_only_those():
    """Three values, spelled out. A free-text column collects the name of
    whoever the framer had in mind, which is the same as no column: the point
    is that a MEASUREMENT is never queued behind a person, and that only
    works if `a measurement` is a value a reader recognises."""
    tpl = flat("skills", "implement", "SKILL.md")
    for value in ANSWERERS:
        assert f"**{value}**" in tpl, (
            f"`skills/implement/SKILL.md` no longer offers `{value}` as one "
            "of the three answers the column takes"
        )
    assert "wrong instrument" in tpl, (
        "the skill lost the reason a measurement is not a person's row. "
        "Without it the column reads as a label and the round trip gets paid "
        "anyway"
    )
    assert "does not travel back to the framer" in tpl, (
        "the skill no longer says where a `the work` row is settled. A row "
        "nobody can answer at framing time, with no destination, is held open "
        "waiting for somebody who was never coming"
    )


def test_the_skill_says_the_framer_does_not_own_the_answers():
    """The other half of S7. A row is a question put to somebody else, so the
    status belongs to whoever answered it and not to whoever asked."""
    tpl = flat("skills", "implement", "SKILL.md")
    assert "opens rows and does not own their answers" in tpl, (
        "`skills/implement/SKILL.md` stopped saying that the framer opens "
        "rows without owning their answers, which is what keeps a frame from "
        "answering its own questions and calling that a decision"
    )
    assert (
        "`Status` column is written by whoever answered, as "
        "`answered <date> by <who>`" in tpl
    ), (
        "nothing says who writes the row's status, or in which words. The "
        "writer closing it is the frame closing a question nobody outside it "
        "ever saw"
    )


# --- the report -------------------------------------------------------------


def report_of(agent):
    """The definition's hand-back step and its person-row rule, flattened.

    Since #968 the report is the last step of `## Order of work`, and the
    rule for a person's row is a paragraph of `## Rules`; the two together
    are what a framer reads when it writes the report."""
    text = read("agents", agent)
    step = re.search(r"^\d+\. Hand back\.(.*?)^## ", text, re.M | re.S)
    assert step, f"agents/{agent} has no `Hand back.` step"
    lead = "**A row only a person can answer"
    start = text.index(lead)
    rule = text[start : text.index("\ncheck: ", start)]
    return " ".join((step.group(1) + rule).split())


def test_a_person_answerable_row_reaches_the_report_in_full():
    """Q2 of #84, answered by the repository owner on 2026-09-11 against the
    default that stood.

    The old rule was unconditional — the path and the count, never the rows'
    text — and it made the approval depend on a file the approver was not
    looking at. Measured in this work item's own run: the orchestrator put
    Q1's full text in front of the owner and got an answer that reversed the
    frame's default. A count would have sent them to the file."""
    report = report_of("framer.md")
    assert "never the rows' text" not in report, (
        "`agents/framer.md`'s report rule is unconditional again. A person "
        "cannot answer a question they were handed a count of, so a frame "
        "obeying that rule ships an approval given against nothing"
    )
    assert "A row only a person can answer is reproduced in full" in report, (
        "the report no longer sends a person-answerable row's own text. "
        "Nobody can answer a question they were handed a count of, so a "
        "frame obeying the shorter rule ships an approval given against "
        "nothing"
    )
    assert "handed a count of" in report, (
        "the reason the split exists is gone, which is how the shorter rule "
        "gets restored by whoever next tidies the section"
    )
    assert "the path and the count" in report, (
        "the other two answerers lost their form. A measurement row and a "
        "work row have nothing in them for the reader to act on, and putting "
        "them in full is how the batch stops being readable in one sitting"
    )


def test_the_report_does_not_reduce_the_frame_to_counts():
    """Two more rows join for the same reason the first did: the approval has
    to stand up without opening a file.

    A phase count is a number and a reader cannot tell a wrong decomposition
    from a number. And a report of what was decided does not surface what was
    left out — this frame's own scope enumerated the documents that call the
    agent set four and omitted both README editions, which is what its first
    phase then hit."""
    report = report_of("framer.md")
    assert "The phases, one line each" in report, (
        "the report gives the phase count instead of the phases. Whoever "
        "approves the plan is approving the order the work comes in"
    )
    assert "What you put out of scope, and why, one line each" in report, (
        "the report gives a count of what was excluded instead of the "
        "exclusions. That is where a framing error hides: what was decided "
        "is visible and what was left out is not"
    )
    assert not re.search(r"the phase count", report), (
        "`the phase count` survives beside the line-each rule, so a framer "
        "reading the section gets both and satisfies the cheaper one"
    )


def test_the_hand_back_labels_what_the_framer_ran_as_executed():
    """Round 1 of #968, finding 3. A framer runs `git show`, `grep` and
    `wc -l` while it reads, and a frame labels those facts `executed`. A
    hand-back told that every claim is `read` misstates them (contract rule 4);
    what is true is narrower, that it ran no check of the repository's."""
    report = report_of("framer.md")
    assert "executed nothing" not in report, (
        "the hand-back says the framer ran nothing, and the commands it runs "
        "while reading give facts that only running them again can check"
    )
    assert "is `executed`" in report, (
        "the hand-back no longer tells the framer which label a fact from a "
        "command it ran takes"
    )
    assert "no check of the repository's" in report, (
        "the hand-back lost the narrower claim that stays true: the framer "
        "runs none of the repository's checks"
    )
