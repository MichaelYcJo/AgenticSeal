"""The `Broad gate` key is asked for, and it runs as the command it reads as.

Two tickets about one key of `seal/config.json`, in causal order. Nothing ever
asks a person for it (#401), so the first repository to fill it in by hand
filled it in the way every command in every document here is written — wrapped
in backticks — and nothing looked at what was written (#402). A shell reads
that as command substitution: the checks run, their exit status is thrown
away, and their output is executed in their place. The measured pair is the
whole of why this exists — the same content exits 1 bare and exited 0 wrapped,
with the failure still on the screen.

`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` holds the executed half:
the gate refusing each form over a fixture repository, and the forms that stay
allowed still sealing. What is pinned HERE is what a person reads and acts
on — what `templates/setup/config.md` promises about the key, the criterion
for choosing a value and its one owner, the refusal the gate prints, and the
command that answers the key. The sentence that sends a session which meets
the refusal to a person instead of letting it choose is the proofer's to
read.
"""

import os
import pathlib
import re

import conftest
from conftest import read

ROOT = pathlib.Path(conftest.ROOT)
TEMPLATE = ("templates", "setup", "config.md")
CONFIG_SKILL = ("skills", "config", "SKILL.md")
ORCH = ("skills", "implement", "orchestration.md")
REVIEW_ORCH = ("skills", "code-review", "orchestration.md")

REFUSED_AND_ALLOWED = "### What is refused, and what stays allowed"


def flat(text):
    """Runs of whitespace folded to one space, so a phrase a hand-wrap splits
    across two lines still reads as the phrase.

    A block quote's `> ` goes with the wrap it marks: the criterion is a
    two-line quote, and folding without dropping the marker leaves `the exit
    code the > gate reads` — a phrase nobody wrote and nobody can assert.
    """
    unquoted = "\n".join(re.sub(r"^\s*>\s?", "", line) for line in text.splitlines())
    return re.sub(r"\s+", " ", unquoted)


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
    tables live under one heading, so it merged them: the pipe row could be
    moved into the refused table with every case still green, and the refused
    loop below could pair a form with another form's reason. That is the
    contract rule 14 artifact for this change asserting nothing about its own content, in a
    release whose whole subject is a check that could not fail.
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


REFUSED = {
    "backticks": "discards its exit status",
    "`$(…)`": "the same semantics",
    "trailing `&`": "before any check has finished",
}


def test_each_refused_form_is_named_with_what_a_shell_does_with_it():
    """A list without the reason is an enumeration the next reader extends by
    analogy, which is how a narrow refusal becomes the general sanitiser #402
    steers away from.

    The reason is asserted IN the form's own row of the REFUSED table. The
    dictionary already holds the pairing, and a loop asking only whether both
    strings appear somewhere under the heading throws it away: round 1 swapped
    the backticks row's reason with the `$(…)` row's and 15 cases stayed
    green, leaving the backticks row explaining itself as *the same semantics
    in the spelling somebody who knows shell reaches for first*.
    """
    body = section(read(*TEMPLATE), REFUSED_AND_ALLOWED, 3)
    refused = table(body, "| Refused |")
    for form, because in REFUSED.items():
        row = named(refused, form)
        assert row, f"the refused list does not name {form}"
        assert because in flat(row), (
            f"{form} is listed with the wrong reason, or with none: {row!r}"
        )


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


ALLOWED = {
    "**inside** a longer line": "runs as the command it reads as",
    "quotes, redirection": "the repository's own claim about itself",
    "a pipe": "LAST status",
    # Round 1's 🟡 1. A backgrounding `&` breaks the criterion's second half
    # wherever it stands, and only the trailing form is refused — so the
    # mid-line form has to be in ONE of the two lists. It is here, with what
    # it costs, because telling it from a `2>&1` or a quoted `&` needs the
    # shell parser this list exists to avoid.
    "an `&` anywhere but at the end": "may still be running when the gate reports",
}


def test_each_allowed_form_is_listed_with_what_it_costs():
    """What stays legal is a commitment rather than an omission, and a cost
    stated in the open is what keeps it from being re-litigated as a defect.

    Read from the ALLOWED table alone, and the cost from the form's own row:
    round 1 moved the pipe row into the refused table and both allowed-list
    cases stayed green, which made them assert only that certain characters
    appear somewhere under the heading.
    """
    body = section(read(*TEMPLATE), REFUSED_AND_ALLOWED, 3)
    legal = table(body, "| Stays legal |")
    for form, cost in ALLOWED.items():
        row = named(legal, form)
        assert row, f"the allowed list does not name {form}"
        assert cost in flat(row), (
            f"{form} is listed with the wrong cost, or with none: {row!r}"
        )


# No case asserts that the two lists partition the forms, and that is not an
# omission. `$(…)` belongs in both and must: the whole command wrapped in it
# is refused, and one INSIDE a longer line is legal, which is the distinction
# the section exists to draw. A partition case over the matching keys was
# written here and asserted exactly that falsehood; it went red on its first
# run and came out rather than being weakened into something that passes.
# What `table()` buys is the pairing above — a row's reason read from the
# row, in the list the row is in.


# --- A8: the criterion has one home ------------------------------------------

CRITERION = "### The criterion for choosing a value"

THREE_RULES = [
    "red repository-wide for reasons unrelated to any branch",
    "A command that **fixes** the tree",
    "Every pytest the command runs keeps the environment the gate hands it",
]


def test_the_template_carries_all_three_rules_of_the_criterion():
    """#401's second half. The key is the one value only a person can write
    and nobody had written down how to choose it: the session that met the
    refusal derived these three under pressure, and two of them existed in no
    document at all."""
    body = flat(section(read(*TEMPLATE), CRITERION, 3))
    for rule in THREE_RULES:
        assert rule in body, f"the criterion does not carry {rule!r}"


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
# is what failed here.* The something is the refusal the gate prints, read
# below, and the executed case beside it in
# `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`; the
# orchestration's sentences on it are the proofer's to read.


def missing_row_text():
    """The refusal itself, built by the module rather than quoted from it."""
    import importlib.util

    path = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
    spec = importlib.util.spec_from_file_location("agentic_broad_gate_text", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return flat(module.missing_row("/seal"))


def test_the_absent_row_refusal_no_longer_tells_the_reader_to_write_one():
    """The only reader standing in front of this message is a session, so
    *write the repository's own broad command into it* asked the one party
    that may not. It printed the key to type, too."""
    said = missing_row_text()
    assert "Write the repository's own broad command" not in said
    assert "<the full suite, the repository-wide lint, the typecheck>" not in said
    assert "not this session's to do" in said


def test_the_absent_row_refusal_says_whose_the_row_is_and_where_it_is_answered():
    """Naming the door is what keeps *not this session's* from reading as a
    dead end — which is how a refusal with no route becomes a session filling
    the key in anyway. #1454: the door adds the key alone, since a JSON file
    carries no section beside it."""
    said = missing_row_text()
    assert "the key is a thing a person wrote" in said
    assert "/agentic:config" in said
    assert "it shows every key and adds this one —" in said
    assert "with its section" not in said
    assert (
        "`templates/setup/config.md` *The criterion for choosing a value* is what "
        "they choose against"
    ) in said
    assert "(`skills/verify/SKILL.md` *The Seal Test*)" in said
    assert "Nothing ran" in said


def test_the_review_orchestrator_names_the_command_that_answers_the_row():
    """The other party in the room when the refusal lands: whoever runs the
    broad gate is the one holding finished work with no pull request open
    and a reason to get past it. That it stops the run and asks a person,
    and why, is the proofer's to read."""
    orchestrator = flat(read(*REVIEW_ORCH))
    # The command `/agentic:config`, which the person runs to answer the key.
    assert "/agentic:config" in orchestrator
