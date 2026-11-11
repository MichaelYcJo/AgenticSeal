"""The settle's documents: the cases read the skill, both editions of the
README and of the seal README, the framer's definition and the release
checklist. #458, closing #83.

The cases that run the command or call
`skills/settle/scripts/settle.py`'s functions stand in `tests/skills/test_settle.py`,
and the `tree` fixture in `tests/conftest.py`. `docs/checks/the-fold.md` names
this file on the `check:` line of *A settle is not a work item*, whose rule
`test_the_skill_names_how_a_settle_commits` holds. Since
#1033 the skill states the settling session's procedure, and the cases that
read it are its S11.
"""

import os

import pytest
from conftest import ROOT
from conftest import flattened as flat

# No TARGET: its cases hold the settle across its skill, both editions of the README and of the seal README, the framer's definition and the release checklist.


def test_the_cheat_sheets_name_the_design_file_the_settle_reads():
    """Contract rule 14's half of D3. Each README edition's `seal settle`
    row names the file whose rule changes the settle reads. Whether a
    released work item with no design leaves like any other is the
    proofer's to read."""
    for edition in ("README.md", "README.ko.md"):
        with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
            # The row is one line of the table: the cell, then up to its end.
            row = f.read().split("`seal settle [--apply]`")[1].split("\n", 1)[0]
        # The path `frame/design.md`, which the person running
        # `seal settle` resolves to the file it reads.
        assert "`frame/design.md`" in row, (
            f"{edition}'s cheat-sheet row does not name the rule arm"
        )


SKILL = os.path.join(ROOT, "skills", "settle", "SKILL.md")
LOCAL_MODE = os.path.join(ROOT, "skills", "settle", "local-mode.md")


def skill(path=SKILL):
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_the_skill_states_the_settling_sessions_procedure():
    """S11 and S13, #1033's *In* item 3. The settling session's procedure
    names the file a measurement nobody has taken is re-homed in. The
    steps, their order, the row kinds and their order are the proofer's to
    read."""
    text = flat(skill())
    procedure = text.split("## The settling session's procedure")[1].split("## ")[0]
    # The path `seal/follow-up.md`, where the settling session writes the
    # row for a measurement nobody has taken (`questions.md` Q1's default).
    assert "`seal/follow-up.md` row" in procedure


def test_the_skill_names_how_a_settle_commits():
    """#517's D1. A settle has no work item, so the skill names the trailer
    its commits carry. Why a settle is no work item is the proofer's to
    read."""
    text = flat(skill())
    # The commit trailer `skills/code-review/scripts/chain_check.py`
    # matches, which the settling session writes.
    assert "`Seal-Routing: no work item`" in text, (
        "the skill does not say how a settle commits"
    )


def document(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return flat(f.read())


@pytest.mark.parametrize(
    "parts", [("seal", "README.md"), ("templates", "setup", "seal-README.md")]
)
def test_the_seal_readme_says_the_step_exists(parts):
    """Both editions of the same file, which
    `tests/behaviour/test_first_setup_asks_once.py` holds byte for byte. Each
    names the step's command and the skill it is read from, so a reader who
    goes looking for the step finds it."""
    text = document(*parts)
    # The command a reader types, and the path of the skill a reader opens.
    assert "settle --apply" in text and "skills/settle/SKILL.md" in text


@pytest.mark.parametrize(
    "parts", [("agents", "framer.md"), ("README.md",), ("README.ko.md",)]
)
def test_every_other_carrier_points_to_the_model(parts):
    """S15. The model has one home, and every other carrier links to it."""
    text = document(*parts)
    # The citation each carrier's reader resolves to reach the model's home.
    assert (
        "`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*"
        in text
    ), "/".join(parts)


def test_the_release_checklist_carries_the_by_hand_step():
    """G5. `settle` is invoked and never triggered, so the only thing that
    makes it happen is a line in the list somebody works down on the day:
    the command, and the skill the step is read from."""
    text = document("docs", "releasing", "release-checklist.md")
    # The command the person working down the checklist types.
    assert "settle --apply" in text, "the checklist never names the step"
    # The path that person opens for the procedure.
    assert "skills/settle/SKILL.md" in text
    # Round 1, finding 10: a document past the ceiling is a report (Q6). The
    # citation that person resolves for what to do with one.
    assert (
        "`skills/settle/SKILL.md` *A document past its ceiling is split, never "
        "trimmed*" in " ".join(text.split())
    )


@pytest.mark.parametrize("edition", ["README.md", "README.ko.md"])
def test_both_cheat_sheets_carry_the_command(edition):
    """The count and the name are derived by
    `tests/behaviour/test_chain_hooks_hardening.py`; what nothing derives is the row a
    reader actually types from. `CONTRIBUTING.md` requires the two editions to
    move together and the hygiene workflow only warns about it. The row
    names the command, the design section the settle reads, and the
    procedure's section, which it links rather than restates (round 1 of
    #1033, finding 2); what the dry run prints is the proofer's to read."""
    text = document(edition)
    # The command the README's reader types.
    assert "`seal settle [--apply]`" in text, (
        f"{edition}'s cheat sheet has no row for the command"
    )
    # The raw file is read, so the row is the row.
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        row = f.read().split("`seal settle [--apply]`")[1].split("\n")[0]
    # The heading `skills/settle/scripts/rule_changes.py` parses in a design.
    assert "`## Rule changes`" in row, row
    # The citation the README's reader resolves for the procedure.
    assert "`skills/settle/SKILL.md` *The settling session's procedure*" in row, row


def test_the_local_mode_section_names_what_a_local_settle_reads():
    """S10 of #955. Since #955 `settle` reads a local root, and the skill's
    local-mode file states where a work item's directory stands there, the
    flag and the two commands the release is read with, the module that
    reads the declaration and the command that takes a copy."""
    section = flat(skill(LOCAL_MODE).split("\n## In local mode\n")[1].split("\n## ")[0])
    for fact in (
        # The path a work item's directory has in local mode, which the
        # settling session opens.
        "`<git-common-dir>/seal/threads/<id>/`",
        # The flag the settling session passes the release on.
        "`--released-at`",
        # The two commands the release is read with.
        "`gh pr list --head <branch> --state merged --json number,mergeCommit`",
        "`git rev-list --topo-order --reverse`",
        # The module that reads `routing.md` as a declaration.
        "`lib/routing.py`",
        # The command a person runs for a copy of the records.
        "`seal export`",
    ):
        assert fact in section, fact
