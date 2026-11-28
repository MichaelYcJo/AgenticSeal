"""`/iadd:config` — the door to `agentory/config.json`.

Issue #105. Three settings existed when this module was written (#113), and
the only way to see them was to open a file nobody had a reason to open. The
skill is instructions rather than a program, so what is pinned here is what
a reader of it acts on: the keys it names, the commands it routes a change
to and the spelling of a value. The places that resolve the root are the
core's opening paragraph's since #1578, and
`tests/text/test_the_rules_have_one_owner.py` holds the skill's citation of
it. Whether its sentences say the rest is the proofer's to read.

**The skill routes rather than reimplements.** A key that moves files is
`iadd mode`'s work, and a second implementation inside a skill is one
nothing can mutation-test.
"""

import pytest
from conftest import flat, read

# No TARGET: its cases hold the config door across the config skill, the bootstrap, the config template and the READMEs.

SKILL = ("skills", "config", "SKILL.md")
# The bootstrap is the orchestrator's since #292, in its own file since #1046.
BOOTSTRAP = ("skills", "implement", "bootstrap.md")
TEMPLATE = ("templates", "setup", "config.md")


ROWS = (
    "Commit and pull request language",
    "Record language",
    "Mode",
    "Broad gate",
    # The fold's values, read by `iadd fold` (#566, #953).
    "Document token ceiling",
    "Policy root",
    # The reference roots (#688), missing from the skill until #647 counted
    # the table, and the row a signer declares its pact in (#647).
    "Reference specs",
    "Pact",
    # The inspection mark on a pull request body, read by `iadd pr-body`, and on
    # the release note, read by this repository's `mark` job (#1204).
    "Pull request inspection mark",
    "Release note inspection mark",
)


@pytest.mark.parametrize("row", ROWS)
def test_the_skill_names_every_row_the_template_ships(row):
    """S1. A door that shows two of three rows is a door somebody has to go
    round anyway."""
    # The key a person writes into `config.json` through the skill, which the
    # plugin's scripts read by that spelling, named by the skill and shipped
    # by the template.
    assert row in flat(*SKILL), f"the skill does not name `{row}`"
    assert row in flat(*TEMPLATE), f"the template no longer ships `{row}`"


def test_the_mode_row_is_routed_to_iadd_mode():
    """S2 and S3. `iadd mode` is what the pull-request checks run, so the
    skill hands the move to it."""
    text = flat(*SKILL)
    # The two commands the session runs to move the root, the code spans of
    # the sentence.
    assert "Run `iadd mode local` or `iadd mode shared`" in text, (
        "the skill does not hand the move to the command that owns it"
    )


def test_the_way_back_from_shared_is_spelled():
    """S5. Until the commit, a switch to shared is walked back by unstaging
    the root before `iadd mode local`, so the skill spells that command."""
    text = flat(*SKILL)
    # The command a person types first to walk a switch to shared back.
    assert "git reset -- :/agentory" in text, "the way back is not spelled"


def test_the_bootstrap_names_the_way_back_to_its_own_questions():
    """S7. A person who answers a question in a batch has no reason to expect
    a way back to it, so the batch has to say there is one."""
    # The command a person types to change an answer later.
    assert "/iadd:config" in flat(*BOOTSTRAP), (
        "first setup asks three questions and names nothing that changes the "
        "answers later"
    )


def test_the_skill_says_how_a_quote_or_a_backslash_is_written():
    """#415, as #1454 leaves it. This file is where a person is told to edit
    the value in place, so it is where they meet a value that needs a
    character JSON escapes. The criterion and the two lists stay pointed at
    rather than copied down; this is not one of them — it is how to write
    the value at all.
    """
    text = flat(*SKILL)
    # The escapes `\"` and `\\` a person writes into the value, which the
    # parser turns back into the characters; the code spans are the fact.
    assert '**A `"` or a `\\` in a value is written `\\"` or `\\\\`.**' in text, (
        "the front door does not say how a quote or a backslash is written"
    )


@pytest.mark.parametrize("parts", [("README.md",), ("README.ko.md",)])
def test_both_readmes_list_it(parts):
    """A door nobody is told about is the file all over again."""
    # The command a reader of the README types.
    assert "/iadd:config" in read(*parts), f"{parts[0]} does not list it"
