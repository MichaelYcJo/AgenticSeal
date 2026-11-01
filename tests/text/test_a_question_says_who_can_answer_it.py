"""A `questions.md` row said what was being asked and never who could answer
it, so three kinds of question wore one shape on the page.

#84's second comment measured all three inside one run's four rows. One of
them was a **measurement** sitting in the human batch: six probes at about
three seconds each settled it, and they showed the issue's own instruction was
wrong. Queued behind a person it would have cost a round trip and returned an
opinion, which is the wrong instrument for it. A third kind — **the work** —
cannot be answered at framing time by anybody, and holding it open waits for
somebody who was never coming.

`templates/records/sdd-questions.md` is the file a session types into. The
column has to be in the shipped table, because a session bootstraps from the
template and never reads the argument for it; the argument and the three
values are `skills/implement/SKILL.md` *3. The SDD file set*, which the
framer opens. This module pins the header and the three values. How
`agents/framer.md`'s report splits on them is the orchestrator's to read at
each framer report.
"""

from conftest import read

ANSWERERS = ("a person", "a measurement", "the work")


def flat(*parts):
    """Whitespace-normalised, so a re-wrap of the same sentence is not a
    failure. These files are hand-wrapped and the sentences move columns."""
    return " ".join(read(*parts).split())


# --- the template -----------------------------------------------------------


def test_the_questions_template_carries_the_answerer_column():
    """S7 of #84. The column is in the shipped table or it does not exist:
    a session copies `templates/records/sdd-questions.md` and writes rows into
    whatever header it finds there."""
    tpl = read("templates", "records", "sdd-questions.md")
    header = (
        "| # | Question | Who can answer | Options & what each implies "
        "| Default until answered | Status |"
    )
    assert header in tpl, (
        "`templates/records/sdd-questions.md` has no `Who can answer` column in its "
        "table header. Prose about the three kinds is worth nothing here -- "
        "the header is what a session fills in"
    )
    body = tpl[tpl.index(header) :]
    assert "|---|---|---|---|---|---|" in body, (
        "the separator row still has the old column count, so the table "
        "renders with the answerer cell folded into its neighbour"
    )


def test_the_skill_names_the_three_answerers():
    """Three values, spelled out. A free-text column collects the name of
    whoever the framer had in mind, which is the same as no column: the point
    is that a MEASUREMENT is never queued behind a person, and that only
    works if `a measurement` is a value a reader recognises."""
    tpl = flat("skills", "implement", "SKILL.md")
    for value in ANSWERERS:
        # The three values a framer writes into the `Who can answer` cell;
        # the orchestrator reads them, and the grader
        # `evals/behaviour/framer/rule-framer-generated-page/graders/shape-no-measurement-row.md`
        # matches `a measurement` in that cell.
        assert f"**{value}**" in tpl, (
            f"`skills/implement/SKILL.md` no longer offers `{value}` as one "
            "of the three answers the column takes"
        )
