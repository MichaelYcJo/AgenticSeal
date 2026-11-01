"""What is left of `settle`'s old file: the cases that read the skill, the
documents, the READMEs, the checklist and the cheat sheets, which wait for
#923. #458, closing #83.

#942's phase 6 placed the cases that run the command or call
`skills/settle/scripts/settle.py`'s functions in `tests/skills/test_settle.py`, and
the `tree` fixture in `tests/conftest.py`. `docs/the-record-layout.md` names
this file on the `check:` lines whose rules the skill cases here hold. Since
#1033 the skill states the settling session's procedure, and the cases that
read it are its S11.
"""

import os

import pytest
from conftest import ROOT
from conftest import flattened as flat

SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")


def test_the_cheat_sheets_name_the_design_file_the_settle_reads():
    """Contract rule 14's half of D3. Each README edition's `seal settle`
    row names the file whose rule changes the settle reads. Whether a
    released work item with no design leaves like any other is the
    proofer's to read."""
    for edition in ("README.md", "README.ko.md"):
        # The path `frame/design.md`, which the person running
        # `seal settle` resolves to the file it reads.
        assert (
            "`frame/design.md`"
            in document(edition).split("`seal settle [--apply]`")[1][:900]
        ), f"{edition}'s cheat-sheet row does not name the rule arm"


SKILL = os.path.join(ROOT, "skills", "settle", "SKILL.md")


def skill():
    with open(SKILL, encoding="utf-8") as f:
        return f.read()


def test_the_skill_names_the_floors_a_fold_has_to_answer():
    """A11. `docs/one-root-by-lifetime.md` *The dependency rule* names two
    readers and the real list is longer — fourteen test modules read this
    repository's own corpus and at least six carry a population floor. A
    session that folds without answering them removes the population its own
    suite was asserting over, and the commit under review is what broke it.

    The three answers are named because the fourth — lowering the floor until
    the run passes — is the one that turns a check into a comment."""
    text = flat(skill())
    # A phrase of the rule, not a fact: the last assert of this module that
    # reads the rule `docs/the-record-layout.md:156` closes, whose section
    # *Answer every check that reads the corpus* gives these three answers.
    # Kept unchanged until that line's change lands (#1233,
    # `frame/design.md` Scope item 9).
    for answer in ("retire the case", "re-point it at a fixture corpus", "decline"):
        assert answer in text, f"the skill does not offer `{answer}`"


def test_the_skill_states_the_settling_sessions_procedure():
    """S11 and S13, #1033's *In* item 3. The settling session's procedure
    names the file a measurement nobody has taken is re-homed in. The
    steps, their order and the row kinds are the proofer's to read."""
    text = flat(skill())
    procedure = text.split("## The settling session's procedure")[1].split("## ")[0]
    # The path `seal/follow-up.md`, where the settling session writes the
    # row for a measurement nobody has taken (`questions.md` Q1's default).
    assert "`seal/follow-up.md` row" in procedure


def test_the_skill_names_how_a_settle_edits_and_commits():
    """#517's D1. A settle has no work item, so the skill names the command
    that records that and the trailer its commits carry. Why a settle is no
    work item is the proofer's to read."""
    text = flat(skill())
    # The command the settling session types on the settle's branch.
    assert "`seal no-work-item`" in text, "the skill does not say how a settle edits"
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
    `tests/behaviour/test_first_setup_asks_once.py` holds byte for byte. It has said a
    work item "waits until a later `settle` folds it" since the root existed,
    and a reader who went looking for the step found nothing."""
    text = document(*parts)
    assert "settle --apply" in text and "skills/settle/SKILL.md" in text
    assert "A settle is not a work item and opens no directory here." in text, (
        f"{'/'.join(parts)} does not say a settle opens no work item (#517)"
    )
    assert (
        "whose record holds no open row, whether or not it wrote a `frame/design.md`"
        in (text)
    )
    assert "retire-process" not in text and "folds it" not in text


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
    text = document("docs", "release-checklist.md")
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


def test_the_module_and_the_skill_both_say_how_local_mode_settles():
    """S10 of #955, contract rule 14. Since #955 `settle` reads a local root,
    so neither text says it refuses one. The skill states where the work
    items are read and removed, what released means there and how the order
    is read, what the dry run adds and what `--apply` removes, and the three
    limits; the docstring's exit-code list names a `gh` that cannot be asked
    and no longer a root in local mode. Round 2's finding 3 of #458 holds
    still: every cause of exit 2 is in the list."""
    with open(SCRIPT, encoding="utf-8") as f:
        head = flat(f.read().split('"""')[1])
    exits = head.split("Exit codes")[1]
    assert "a root in local mode" not in exits, exits
    assert "a `gh` that is not on PATH or whose query fails" in exits, exits
    assert "opted out" in exits, "exit 2 covers the opt-out and the list does not"
    assert "Local mode is refused" not in head, head
    assert "refuses to run in local mode" not in flat(skill())
    section = flat(skill().split("\n## In local mode\n")[1].split("\n## ")[0])
    for said in (
        "under the common git directory",
        "so a work item's directory is `<git-common-dir>/seal/threads/<id>/`",
        "the pull request from the branch its `routing.md` names has merged",
        "reachable from `--released-at`",
        "`gh pr list --head <branch> --state merged --json number,mergeCommit`",
        "Each `frame/design.md` is read from its directory",
        "their merge commits' place in `git rev-list --topo-order --reverse`",
        "with its pull request's number and its merge commit",
        "which of the three states holds",
        "no `routing.md` that `hooks/lib/routing.py` reads as a declaration naming "
        "a branch",
        "a pull request listed with no merge commit among them",
        "`seal export` takes a copy for whoever wants one",
        "removes each released local directory whose record holds no open row",
        "Shared mode never asks `gh`",
        "reached `--released-at` without a pull request reads as unreleased, "
        "and its directory is removed by hand",
        "A repository on a host `gh` cannot ask cannot settle in local mode",
        "reads that later work item as released",
        "So does a merged pull request from a fork whose branch has the same "
        "name, since `gh pr list --head` matches a branch's name and not its "
        "owner",
        "it does not rule out the second, because the flow does not name a "
        "fork's branches",
    ):
        assert said in section, said
    assert "never produces this" not in section, section
