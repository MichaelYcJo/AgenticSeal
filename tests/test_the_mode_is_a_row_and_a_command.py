"""`seal mode`: what is left here after #942's phase 5.

The cases of `skills/implement/scripts/seal.py` are in `tests/test_seal.py`.
The three cases here read the documents and the workflows that name the
command, and they are #923's.
"""

import pytest
from conftest import read


@pytest.mark.parametrize("readme", ["README.md", "README.ko.md"])
def test_both_readmes_name_the_command_before_the_by_hand_lines(readme):
    """The issue's fifth done-when: the section stops being two shell lines
    and starts naming a command.

    The FIRST runnable block of the section is the assertion, not an index
    comparison between two strings. Mutation-tested: deleting the command
    block outright left an index comparison green, because `seal mode local`
    is named in the prose above the by-hand block as well.
    """
    text = read(readme)
    assert "seal mode --check" in text, readme
    heading = (
        "### Shared or local" if readme == "README.md" else "### shared 인가 local 인가"
    )
    body = text.split(heading, 1)[1].split("\n## ", 1)[0]
    blocks = [chunk.split("```", 1)[0] for chunk in body.split("```bash\n")[1:]]
    assert blocks, f"{readme}: the section runs nothing at all"
    assert "seal mode local" in blocks[0] and "seal mode shared" in blocks[0], (
        f"{readme}: the first block of the section is not the switch — a "
        "person reading top to bottom still meets the shell lines first. "
        "Naming any `seal mode` spelling is not enough: the two directions "
        "are what the section is about, and deleting the block that carries "
        "them left a looser assertion green (mutation-tested)"
    )
    assert "mv " not in blocks[0], f"{readme}: the first block is the by-hand move"


def test_the_config_template_ships_the_row_with_no_value():
    """A template declaring `shared` would hand every local-mode repository a
    row that is wrong from the moment it is copied — and the fix the command
    then offers is `--apply`, which would move their root into the tree
    through the one door that does not open both ways."""
    text = read("templates", "config.md")
    assert "| Mode |  |" in text, "the template's Mode row carries a value"
    assert "## Mode" in text


@pytest.mark.parametrize(
    "parts", [(".github", "workflows", "hygiene.yml"), ("templates", "hygiene.yml")]
)
def test_both_hygiene_workflows_run_the_check(parts):
    """The check has to reach a pull request in this repository AND in every
    repository `seal pr-checks install` sets up, or it names a disagreement
    nowhere."""
    text = read(*parts)
    assert "mode --check" in text, "/".join(parts)
