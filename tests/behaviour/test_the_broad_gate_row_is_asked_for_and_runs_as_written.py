"""The `Broad gate` key is asked for, and it runs as the command it reads as.

Two tickets about one key of `seal/config.json`, in causal order. Nothing ever
asks a person for it (#401), so the first repository to fill it in by hand
filled it in the way every command in every document here is written — wrapped
in backticks — and nothing looked at what was written (#402). A shell reads
that as command substitution: the checks run, their exit status is thrown
away, and their output is executed in their place. The measured pair is the
whole of why this exists — the same content exits 1 bare and exited 0 wrapped,
with the failure still on the screen.

`tests/skills/test_broad_gate.py` holds the executed half: the gate refusing
each form and letting the others run (`Test_wholly_substituted`,
`Test_not_as_written`), and the refusal it prints where the key is absent
(`Test_missing_row`). What is pinned HERE is what a person reads and acts
on in the documents: the section of `templates/setup/config.md` that lists
the forms, the forms the gate refuses, the citation of the criterion for
choosing a value, and the command that answers the key. The reasons, the
criterion's rules and the sentence that sends a session which meets the
refusal to a person instead of letting it choose are the proofer's to read.
"""

from conftest import read
from test_broad_gate import flat

# No TARGET: its cases hold the broad gate row across templates/setup/config.md, skills/config/SKILL.md and the two orchestration documents.


TEMPLATE = ("templates", "setup", "config.md")
CONFIG_SKILL = ("skills", "config", "SKILL.md")
ORCH = ("skills", "implement", "orchestration.md")
REVIEW_ORCH = ("skills", "code-review", "orchestration.md")

REFUSED_AND_ALLOWED = "### What is refused, and what stays allowed"


def section(text, heading, level):
    """The text under HEADING up to the next heading of the same level."""
    assert heading in text, f"{heading!r} is not a heading any more"
    body = text.split(heading, 1)[1]
    return body.split("\n" + "#" * level + " ", 1)[0]


def table(text, header):
    """The rows of ONE table in a section — the one whose header row starts
    with HEADER — so a form moved from the refused list to the allowed one
    stops satisfying the case named for the list it left.

    Round 1's 🟡 6. `rows` returns every `| ` line under the heading, and both
    tables live under one heading, so it merged them: a form of the allowed
    table could be found in the refused one with every case still green.
    """
    assert header in text, f"{header!r} is not a table in this section"
    after = text.split(header, 1)[1]
    out = []
    for line in after.splitlines():
        if line.startswith("| "):
            out.append(line)
        elif out:
            break
    return out


def named(table_rows, form):
    """The one row of TABLE_ROWS whose FIRST cell names FORM, or None.

    The name cell and not the whole row. Matching anywhere in the row let a
    row be found by its own prose: renaming the pipe row's first cell left
    this green, because the cost cell says *and a pipe cannot reach this row
    at all* further along the same line. That is 🟡 6's weakness one level
    in, met while repairing 🟡 6.
    """
    for line in table_rows:
        cells = line.split(" | ")
        if form in flat(cells[0]):
            return line
    return None


# --- A7: the template says what is refused and what is not ------------------


def test_the_template_carries_the_heading_of_the_two_lists():
    """The lists are what a reviewer is pointed at when they want to argue
    with a form, so they live together under one heading, which the config
    skill cites. The two pairing cases below read each list's rows."""
    # The heading of `templates/setup/config.md` that `skills/config/SKILL.md`
    # cites, which a person resolves to the two lists.
    assert REFUSED_AND_ALLOWED in read(*TEMPLATE)


REFUSED = (
    # The form `skills/verify/scripts/broad_gate.py` refuses as a value
    # wholly wrapped in backticks, which a person writing the key reads in
    # the refused table.
    "backticks",
    # The form it refuses as a value wholly wrapped in `$(…)`.
    "`$(…)`",
    # The form it refuses as a value that ends in `&`.
    "trailing `&`",
)


def test_each_refused_form_is_named_in_the_refused_table():
    """Each form the gate refuses is named in the first cell of a row of the
    REFUSED table, not anywhere under the heading: round 1 found a form of
    one list read in the other. The reason each row gives is the proofer's
    to read."""
    body = section(read(*TEMPLATE), REFUSED_AND_ALLOWED, 3)
    refused = table(body, "| Refused |")
    for form in REFUSED:
        assert named(refused, form), f"the refused list does not name {form}"


def test_the_template_names_the_command_that_rewrites_a_refused_key():
    """#402 *Not this*. A refused value is not stripped or repaired, so the
    person rewrites the key, and the lists' section names the command that
    does. That the section says nothing is stripped is the proofer's to
    read."""
    body = flat(section(read(*TEMPLATE), REFUSED_AND_ALLOWED, 3))
    # The command `/agentic:config`, which a person types to rewrite the key.
    assert "/agentic:config" in body, (
        "the section does not say where a person rewrites the key"
    )


# No case asserts that the two lists partition the forms, and that is not an
# omission. `$(…)` belongs in both and must: the whole command wrapped in it
# is refused, and one INSIDE a longer line is legal, which is the distinction
# the section exists to draw. A partition case over the matching keys was
# written here and asserted exactly that falsehood; it went red on its first
# run and came out rather than being weakened into something that passes.
# What `table()` buys is that a refused form is read in the list it is in.


# --- A8: the criterion has one home ------------------------------------------

CRITERION = "### The criterion for choosing a value"


def test_the_config_skill_sends_the_criterion_to_its_owner_by_name():
    """A link is one sentence naming the owner, and it does not restate the
    rule (the shape `tests/text/test_the_rules_have_one_owner.py` holds every
    linking carrier to). Whether the skill restates a rule is the proofer's
    to read."""
    skill = flat(read(*CONFIG_SKILL))
    # The heading *The criterion for choosing a value*, which a person
    # reading the skill resolves in `templates/setup/config.md`.
    assert CRITERION.lstrip("# ") in skill, (
        "the config skill does not name the section that owns the criterion"
    )


def refusal_bullet():
    """The config skill's paragraph about the refusal, bounded at the blank
    line — not the file. Round 1's 🟡 8: the clause naming the three forms
    could be deleted with 15 cases green, because every assertion matched a
    sentence on one side of it or the other."""
    skill = read(*CONFIG_SKILL)
    opening = "**The `Broad gate` key is looked at before it is run**"
    assert opening in skill, "the refusal paragraph is gone from the config skill"
    return flat(skill[skill.index(opening) :].split("\n\n", 1)[0])


def test_the_config_skill_points_at_the_section_and_names_the_refused_forms():
    """The door a person reaches later. It names the three forms so somebody
    reading it knows the refusal exists, and sends the reasoning to the one
    owner. What the paragraph says of the refusal is the proofer's to read."""
    skill = flat(read(*CONFIG_SKILL))
    # The heading of `templates/setup/config.md` the skill cites, which a
    # person opens to learn what the key may hold.
    assert "What is refused, and what stays allowed" in skill, (
        "the config skill does not point at the section that decides this"
    )
    bullet = refusal_bullet()
    # The three forms `broad_gate.py` refuses in the key, which a person
    # filling it in has to recognise in what they wrote.
    for form in ("backticks", "`$(…)`", "trailing `&`"):
        assert form in bullet, (
            f"the config skill does not name {form}, so somebody reading it "
            "does not learn that the refusal exists"
        )


# --- A10: a session that meets the refusal brings it to a person ------------
#
# #401's third Done-when, and the one the ticket says a sentence already
# failed: *a session that meets the refusal anyway is told to bring it to a
# person rather than to choose — and something checks that, since a sentence
# is what failed here.* The something is the refusal the gate prints, which
# `tests/skills/test_broad_gate.py`'s `Test_missing_row` reads, and the
# command below that answers it; the orchestration's sentences on it are the
# proofer's to read.


def test_the_review_orchestrator_names_the_command_that_answers_the_row():
    """The other party in the room when the refusal lands: whoever runs the
    broad gate is the one holding finished work with no pull request open
    and a reason to get past it. That it stops the run and asks a person,
    and why, is the proofer's to read."""
    orchestrator = flat(read(*REVIEW_ORCH))
    # The command `/agentic:config`, which the person runs to answer the key.
    assert "/agentic:config" in orchestrator
