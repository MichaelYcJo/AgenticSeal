"""`/agentic:config` — the door to `seal/config.md`.

Issue #105. Three rows exist and the only way to see them was to open a file
nobody has a reason to open. The skill is instructions rather than a program,
so what is pinned here is what a reader of it acts on: the rows it names,
the commands it routes a change to, the spelling of a cell's value, and the
paths that resolve the root. Whether its sentences say the rest is the
proofer's to read.

**The skill routes rather than reimplements.** A row that moves files is
`seal mode`'s work, and a second implementation inside a skill is one
nothing can mutation-test.
"""

import pytest
from conftest import flat, read

SKILL = ("skills", "config", "SKILL.md")
# The bootstrap is the orchestrator's since #292, in its own file since #1046.
BOOTSTRAP = ("skills", "implement", "bootstrap.md")
TEMPLATE = ("templates", "setup", "config.md")


ROWS = (
    "Commit and pull request language",
    "Record language",
    "Mode",
    "Broad gate",
    # The fold's values, read by `seal fold` (#566, #953).
    "Document token ceiling",
    "Policy root",
    # The reference roots (#688), missing from the skill until #647 counted
    # the table, and the row a signer declares its pact in (#647).
    "Reference specs",
    "Pact",
)


@pytest.mark.parametrize("row", ROWS)
def test_the_skill_names_every_row_the_template_ships(row):
    """S1. A door that shows two of three rows is a door somebody has to go
    round anyway."""
    assert row in flat(*SKILL), f"the skill does not name `{row}`"
    assert row in flat(*TEMPLATE), f"the template no longer ships `{row}`"


def test_the_mode_row_is_routed_to_seal_mode():
    """S2 and S3. `seal mode` is what the pull-request checks run, so the
    skill hands the move to it."""
    text = flat(*SKILL)
    # The two commands the session runs to move the root, the code spans of
    # the sentence.
    assert "Run `seal mode local` or `seal mode shared`" in text, (
        "the skill does not hand the move to the command that owns it"
    )


def test_the_way_back_from_shared_is_spelled():
    """S5. Until the commit, a switch to shared is walked back by unstaging
    the root before `seal mode local`, so the skill spells that command."""
    text = flat(*SKILL)
    # The command a person types first to walk a switch to shared back.
    assert "git reset -- :/seal" in text, "the way back is not spelled"


def test_the_root_is_resolved_rather_than_spelled():
    """The two places, in that order — the rule every other reader follows."""
    text = flat(*SKILL)
    assert "<repo>/seal/config.md" in text
    assert "git rev-parse --git-common-dir" in text


def test_the_bootstrap_names_the_way_back_to_its_own_questions():
    """S7. A person who answers a question in a batch has no reason to expect
    a way back to it, so the batch has to say there is one."""
    assert "/agentic:config" in flat(*BOOTSTRAP), (
        "first setup asks three questions and names nothing that changes the "
        "answers later"
    )


def test_the_skill_says_how_a_value_carrying_a_pipe_is_written():
    """#415. This file is where a person is told to edit the value in place,
    so it is where they meet a value that needs a pipe. The criterion and the
    two lists stay pointed at rather than copied down; this is not one of
    them — it is how to write the cell at all, which the person editing it
    cannot read off the template's own tables.
    """
    text = flat(*SKILL)
    # The escape `\|` a person writes into a cell, which the config reader
    # turns back into a pipe; the code spans are the fact.
    assert "A value carrying a `|` is written `\\|`" in text, (
        "the front door does not say how a pipe is written into the cell"
    )


@pytest.mark.parametrize("parts", [("README.md",), ("README.ko.md",)])
def test_both_readmes_list_it(parts):
    """A door nobody is told about is the file all over again."""
    assert "/agentic:config" in read(*parts), f"{parts[0]} does not list it"
