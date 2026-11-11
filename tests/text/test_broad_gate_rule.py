"""The one-broad-run rule spans several documents; drift between them is the bug.

The skill states it, the agent contract binds every agent to it, the crafter
follows it, the proofer audits it, and two records carry it to the next
session. The preset block stated it too, for a session that loaded none of
them, until #1177 retired the block; a session now reads the core, which
the plugin's `SessionStart` hook prints. A rule
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

import re

from conftest import flat, read

# No TARGET: its cases hold the one broad run across the agent definitions, the skills and the documents that state it.


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
    answers. Where the two answers land is the proofer's to read."""
    crafter = flat("agents", "crafter.md")
    # The two contract rule numbers the crafter resolves for what its
    # hand-back answers.
    assert "rule 2" in crafter and "rule 3" in crafter, (
        "the implementer can no longer reach the rules its hand-back answers"
    )


RUN = "seal gate --base <base> --record <item>"


def test_the_orchestration_names_the_broad_run_command():
    """S2 of #969. The orchestration that spawns the sealer names the
    preflight, the run and the run's log. Each is what the orchestrator
    types or opens, so each is held by its spelling; who may run the gate
    and in what order the steps come are the proofer's to read. Contract
    rule 2 named the run's command too until #1312, which took that copy out
    of every agent's preload, since only the orchestrator types it."""
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
    # The path of the record a session opens to learn whether the broad run
    # already happened.
    assert "`trail/gate.md`" in read("docs", "checks", "the-pull-request-check.md"), (
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


def test_the_order_inside_a_ticket_names_the_preflight():
    """The order section sequences the sealer's spawn, so the step before it
    is written in where the spawn is. Where it stands in the order is the
    proofer's to read."""
    text = joined(
        section(
            read("skills", "implement", "orchestration.md"),
            "Orchestrator: the order inside a ticket",
        )
    )
    # The command the orchestrator runs before it spawns the sealer.
    assert PREFLIGHT in text, "the order does not name the preflight"


EXAMPLE_ROW = (
    '"Broad gate": "uvx ruff check . && uvx ruff format --check . && bin/test -q"'
)


def test_the_example_row_goes_lint_first_and_the_prose_cites_the_arms_list():
    """S9, the owner's answer of 2026-10-01: the key a repository copies puts
    the seconds-long linters ahead of the suite, as this repository's own key
    does. The prose above it points at the one list of the gate's arms, and
    names the preflight that runs those arms alone."""
    body = section(read("templates", "setup", "config.md"), "Broad gate")
    # The config key and value a repository copies into its `config.json`.
    assert EXAMPLE_ROW in body, "the example key is not the lint-first one"
    lead = joined(body).split("```")[0]
    # The script whose docstring lists the arms, which a reader opens, and
    # the command that runs the arms alone.
    assert "broad_gate.py" in lead and PREFLIGHT in lead, lead


def test_the_broad_gate_section_names_the_preflight():
    """S10. `verify` names the preflight in the section that assigns the
    run."""
    text = joined(
        section(read("skills", "verify", "orchestration.md"), "The broad gate")
    )
    # The command the orchestrator runs before the sealer is spawned.
    assert PREFLIGHT in text, "the broad gate section does not name the preflight"
