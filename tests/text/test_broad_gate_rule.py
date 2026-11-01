"""The one-broad-run rule spans several documents; drift between them is the bug.

The skill states it, the agent contract binds every agent to it, the crafter
follows it, the proofer audits it, and two records carry it to the next
session. The preset block stated it too, for a session that loaded none of
them, until #1177 retired the block and the plugin's `SessionStart` hook
began printing the core into every session. A rule
spread this wide fails by one of them quietly dropping its part, which is
invisible in any single diff.

Phases 3 and 4 of #107 moved the prohibition and the refusal out of the two
agent definitions and into `skills/agent-contract/SKILL.md`. The cases moved
with them rather than being deleted: what each definition still holds is its
own APPLICATION -- the proofer has a named field for the question, the
crafter cites the two rules its hand-back answers -- and a case asserting
the same sentence in two files is the duplication the
contract was written to end. That duplication has its own module now,
`tests/text/test_a_moved_rule_leaves_its_definition.py`, because until phase 4
nothing in the tree noticed a moved rule being pasted back.
"""

import glob
import os
import re

from conftest import ROOT, flat, read
from test_the_agent_contract_holds_the_universal_rules import HEADING


def read_at(path):
    """One file by absolute path, for the cases that walk a glob."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_the_broad_gate_section_cites_the_owner_of_its_timing():
    """The section that runs the gate cites the section that owns when the
    run comes. #943 renamed that section, and a citation left at the old
    name points at a heading no file has. When the gate fires is the
    proofer's to read."""
    scope = read("skills", "verify", "orchestration.md")
    section = scope.split("## The broad gate")[1].split("\n## ")[0]
    flat = " ".join(section.split())  # re-wrapping a paragraph is not a regression
    # The citation the orchestrator resolves to learn when the run comes:
    # the backticked path and the heading in italics, as since #940.
    assert f"`skills/code-review/orchestration.md` *{SPAWN_SECTION}* owns when" in (
        flat
    ), "the broad gate section no longer names the owner of when the run comes"


def test_the_crafter_puts_both_answers_in_the_hand_back():
    """What stayed with the implementer when contract rule 2 and contract
    rule 3 moved: the crafter's definition cites both rules its hand-back
    answers. Where the two answers land is the proofer's to read, except the
    one clause `docs/the-broad-gate.md:42` still names this module for."""
    crafter = flat("agents", "crafter.md")
    # The two contract rule numbers the crafter resolves for what its
    # hand-back answers.
    assert "rule 2" in crafter and "rule 3" in crafter, (
        "the implementer can no longer reach the rules its hand-back answers"
    )
    # A phrase of the rule, not a fact: the last assert of this module that
    # reads the rule `docs/the-broad-gate.md:42` closes, kept unchanged until
    # that line's change lands (#1233, `frame/design.md` Scope item 9).
    assert "the suite labelled `unverified`" in crafter, (
        "the suite stopped going over labelled, and a suite that is simply "
        "not mentioned reads as a suite that passed"
    )


def contract_section(number):
    """The body of `## <N>` in the contract, heading excluded.

    Scoped rather than whole-file, because the thing #120 has to keep out is
    a WORD -- `orchestrator` -- that the contract says legitimately elsewhere
    (its opening paragraph, about the prompt a round arrives in). A whole-file
    absence check would either fail on that sentence or be dropped."""
    text = read("skills", "agent-contract", "SKILL.md")
    heads = list(HEADING.finditer(text))
    for index, match in enumerate(heads):
        if int(match.group(1)) != number:
            continue
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        return " ".join(text[match.end() : end].split())
    raise AssertionError(f"the contract has no rule {number}")


RUN = "seal gate --base <base> --record <item>"


def test_the_contract_and_the_orchestration_name_the_broad_run_command():
    """S2 of #969. Contract rule 2 names the orchestrator's command for the
    broad run, and the orchestration that spawns the sealer names the
    preflight, the run and the run's log. Each is what the orchestrator
    types or opens, so each is held by its spelling; who may run the gate
    and in what order the steps come are the proofer's to read."""
    body = contract_section(2)
    # The command the orchestrator types for the broad run, as contract
    # rule 2 names it.
    assert RUN in body, "contract rule 2 stopped naming the orchestrator's command"
    order = joined(
        section(read("skills", "code-review", "orchestration.md"), SPAWN_SECTION)
    )
    steps = [
        # The command the orchestrator types before the broad run.
        PREFLIGHT,
        # The command the orchestrator types for the broad run.
        RUN,
        # The path the orchestrator writes the run's output to.
        "<scratchpad>/<work-item-id>/gate.log",
    ]
    missing = [step for step in steps if step not in order]
    assert not missing, f"the orchestration does not name: {missing}"


def test_no_definition_promises_the_suite_once_the_rounds_settle():
    """Round 1, finding 2 of #120. `agents/proofer.md` read *rule 2 keeps the
    suite out of your hands UNTIL the rounds settle*, which says it becomes the
    proofer's afterwards.

    Under the old contract rule 2 that was a harmless imprecision about a prohibition with
    a holder who was not an agent. Under the new one it is false in a way a
    reader can act on: this file assigns none of the three, and since #969 no
    definition does, because the orchestrator runs the gate. The hazard is
    live rather than theoretical --
    `agents/proofer.md`'s own bullet on the broad gate's state puts a reviewer in
    exactly the moment the sentence appears to release.

    Asserted over the whole glob, not over the one file the finding named,
    because a temporal release is the shape any definition can pick up while
    describing a rule it does not hold.

    **The direction this can still miss, stated rather than left to be found.**
    It matches one spelling. A definition that promises the suite in other
    words -- *yours once the rounds have settled* -- is invisible here, which
    round 2 of #120 measured by rewording the corrected sentence and watching
    this case stay green. That is a verbatim-versus-semantic trade: no
    constant decides when two sentences say the same thing.
    What narrows it is that the wrong sentence had exactly one idiom in this
    tree, and the glob is what catches that idiom arriving in a second file --
    which is the copy this shape actually spreads by."""
    for path in sorted(glob.glob(os.path.join(ROOT, "agents", "*.md"))):
        text = " ".join(read_at(path).split())
        assert "until the rounds settle" not in text.lower(), (
            f"{os.path.basename(path)} promises the suite once the rounds "
            "settle. Contract rule 2 has no such release for anyone: an agent takes the "
            "broad gate when its own definition assigns it, and never later"
        )


def test_the_reviewer_has_a_field_for_the_question_the_default_produces():
    """The reviewer needs somewhere for a declined instruction to land, and
    `agents/proofer.md` names the round record's section it goes in. Why a
    report needs a field where a conversation does not is the proofer's to
    read."""
    proofer = " ".join(read("agents", "proofer.md").split())
    # The round record's section `## Not judged`, from
    # `templates/records/sdd-round.md`, which the proofer writes the
    # declined instruction into.
    assert "goes in as a row of `## Not judged` with the caller" in proofer, (
        "the reviewer asks a question with no field to ask it in, and a seal "
        "gets taken over an axis nobody decided"
    )


def test_the_broad_gate_state_survives_a_handoff():
    """A session joining at round 3 cannot see which commands were run."""
    assert "`trail/gate.md`" in read("docs", "the-review-record.md"), (
        "the record lost the file that tells the next session whether the one "
        "broad run already happened"
    )


# --- 1790815611: the record arms run before the sealer is spawned (#638) -------

PREFLIGHT = "seal gate --preflight"
SPAWN_SECTION = "Orchestrator: the pull request opens once the sealer seals"


def section(text, heading):
    """The `## heading` section of `text`, its heading line included, up to
    the next heading of the same or a higher level."""
    lines = text.splitlines()
    start = lines.index(f"## {heading}")
    end = next(
        (i for i in range(start + 1, len(lines)) if re.match(r"^#{1,2} ", lines[i])),
        len(lines),
    )
    return lines[start:end]


def joined(lines):
    return " ".join(" ".join(lines).split())


def test_the_acts_table_row_names_the_preflight_and_stays_a_sentence():
    """S8's other half. The row for that section keeps `still a sentence` —
    a session that skips the preflight loses time and nothing else, because
    the broad run asks the same arms — and its grounds name the step."""
    rows = [
        line
        for line in read("skills", "implement", "acts.md").splitlines()
        if line.startswith(f"| {SPAWN_SECTION} |")
    ]
    assert len(rows) == 1, f"{len(rows)} acts-table rows name the section"
    # The `Delivered by` value `still a sentence`, which
    # `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`
    # parses and a maintainer reads when an act moves.
    assert "| still a sentence |" in rows[0], rows[0]
    # The command the row's grounds name, which the orchestrator types.
    assert PREFLIGHT in rows[0], "the row's grounds do not name the preflight"


def test_the_order_inside_a_ticket_puts_the_preflight_before_the_sealer():
    """The order section sequences the sealer's spawn, so the step before it
    is written in where the spawn is."""
    text = joined(
        section(
            read("skills", "implement", "orchestration.md"),
            "Orchestrator: the order inside a ticket",
        )
    )
    assert PREFLIGHT in text, "the order does not name the preflight"
    assert text.index(PREFLIGHT) < text.index("then the sealer, and then the pull"), (
        text
    )


EXAMPLE_ROW = (
    "| Broad gate | uvx ruff check . && uvx ruff format --check . && bin/test -q |"
)
BY_HAND = (
    "`evidence-check`",
    "`seal unverified`",
    "`chain_check.py`",
    "`survivor-check`",
)


def test_the_example_row_goes_lint_first_and_the_arms_are_not_listed_by_hand():
    """S9, the owner's answer of 2026-10-01: the row a repository copies puts
    the seconds-long linters ahead of the suite, as this repository's own row
    does. The prose above it named four of the gate's six arms; it points at
    the one list instead, and says the preflight runs those arms alone."""
    body = section(read("templates", "setup", "config.md"), "Broad gate")
    assert EXAMPLE_ROW in body, "the example row is not the lint-first one"
    lead = joined(body).split("```")[0]
    listed = [name for name in BY_HAND if name in lead]
    assert not listed, f"the prose still lists arms by hand: {listed}"
    assert "broad_gate.py" in lead and PREFLIGHT in lead, lead


def test_the_skill_says_the_preflight_is_not_the_broad_gate():
    """S10. `verify` names the preflight in the section that assigns the run,
    and says what keeps it from being mistaken for one: no suite, nothing
    sealed. The sealer's own definition never mentions it — the sealer does
    not preflight, and its four acts are unchanged."""
    text = joined(
        section(read("skills", "verify", "orchestration.md"), "The broad gate")
    )
    assert PREFLIGHT in text, "the broad gate section does not name the preflight"
    at = text.index(PREFLIGHT)
    said = text[max(0, at - 300) : at + 500]
    assert "runs no suite" in said and "writes nothing" in said, said
    assert "orchestrator" in said, said
    assert "--preflight" not in read("agents", "sealer.md"), (
        "the sealer's definition names the preflight"
    )
