"""What is left of `settle`'s old file: the cases that read the skill, the
documents, the READMEs, the checklist and the cheat sheets, which wait for
#923. #458, closing #83.

#942's phase 6 placed the cases that run the command or call
`skills/settle/scripts/settle.py`'s functions in `tests/test_settle.py`, and
the `tree` fixture in `tests/conftest.py`. `docs/the-record-layout.md` names
this file on the `check:` lines whose rules the skill cases here hold, and on
others until the settle that applies the work item's rule changes.
"""

import importlib.util
import os

import pytest
from conftest import flattened as flat
from test_settle import OVERVIEW_OPEN, moment, run

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")


def load():
    spec = importlib.util.spec_from_file_location("settle", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


settle = load()


def test_a_closed_row_is_told_to_merge_before_its_directory_goes(tree):
    """Round 1's finding 2. The CI readers ask the rule of the merge base, so
    a row closed and its directory retired in one pull request is refused
    there after `settle` said the removal was fine. The report, the
    skill and the policy all say the closure merges first."""
    moment(tree, overview=OVERVIEW_OPEN)
    _, text = run(tree)
    assert "in a pull request merged before the one that retires the directory" in (
        flat(text)
    ), text
    assert "merge first" in flat(skill()), (
        "the skill lets a settle close a row and retire its directory in one "
        "pull request, which the CI readers refuse at the merge base"
    )
    assert "in a pull request merged before the one that retires" in document(
        "docs", "the-record-layout.md"
    )


def test_the_documents_say_the_closure_has_to_reach_the_base():
    """S11, contract rule 14's half of #602: the skill, the policy, both cheat-sheet rows,
    the kept heading and the module docstring say the rule is asked at the
    merge base of `--released-at` and `HEAD`, and what a person does about a
    directory kept there."""
    text = flat(skill())
    assert "*kept until the closure reaches <base>*" in text, text
    # #611: `base_heading` prints `RULE_MOVED_HEADING` instead once
    # `--released-at` has moved past the fork, and the skill named only the
    # first of the two wordings.
    assert "*kept: the closure has not reached <base>*" in text, text
    assert "Merged first means merged to the branch the release merges to" in text
    assert "the merge base of `--released-at` and `HEAD`" in text
    policy = flat(document("docs", "the-record-layout.md"))
    assert "`settle` asks it at the merge base of `--released-at` and `HEAD`" in policy
    # Round 1, 🟡 1: that merge base is CI's only until the base moves.
    assert "until the base moves past the fork" in policy, policy
    # Round 2, ⬜ 5: `document` flattens, so a split on a newline took the rest
    # of the file as the row. The raw file is read, so the row is the row.
    for edition, phrase in (
        ("README.md", "until `--released-at` moves on past that commit"),
        ("README.ko.md", "앞으로 나아가기 전까지는"),
    ):
        with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
            row = f.read().split("`settle [--apply]`")[1].split("\n")[0]
        assert "`--released-at`" in row and "`HEAD`" in row, (
            f"{edition}'s cheat-sheet row does not say the base is asked"
        )
        # Round 2, 🟡 1: CI's revision is the fork only until the base moves.
        assert phrase in row, row
        assert "because that is where CI asks" not in row, row
        assert "CI 가 그 지점에서 확인하기 때문입니다" not in row, row
    assert "which is the base's tip" in text, text
    assert "merging it into this branch and running `settle`" in text, text
    assert "to the branch the release merges to" in flat(settle.RULE_KEPT_HEADING)
    with open(SCRIPT, encoding="utf-8") as f:
        head = flat(f.read().split('"""')[1])
    assert "sharing no commit with `HEAD`" in head, "exit 2's seventh state is missing"
    assert "closure has not reached the merge base" in head, "exit 1's cause is missing"


def test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule():
    """Contract rule 14's half of D3. The policy said such an item *is kept by name*; that
    is overturned, and the one condition the frame added is stated where the
    owner can overturn it."""
    policy = document("docs", "the-record-layout.md")
    assert "and it is kept by name" not in policy, (
        "the policy still keeps a spec-less directory by name"
    )
    assert "it is retired by that rule, with no marker" in policy
    assert "nothing in the record may still be open" in policy
    assert "a judgment the repository owner may overturn" in policy
    text = flat(skill())
    assert "A released work item with no `spec.md` states no rule" in text
    assert "*retired by the rule*" in text and "*kept by the rule*" in text
    for edition in ("README.md", "README.ko.md"):
        assert "`spec.md`" in document(edition).split("`settle [--apply]`")[1][:900], (
            f"{edition}'s cheat-sheet row does not name the rule arm"
        )


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
    assert "population floor" in text, (
        "the skill never tells a session that its own checks read the corpus"
    )
    assert "a list of readers written in any document is not the whole list" in text, (
        "the skill lets a written list of readers stand as the whole list, "
        "which is what makes a fold turn a suite red"
    )
    for answer in ("retire the case", "re-point it at a fixture corpus", "decline"):
        assert answer in text, f"the skill does not offer `{answer}`"


def test_the_skill_says_the_spec_judges_and_the_command_applies():
    """#953: the judgment is made when the spec is written and reviewed, so a
    session running `settle` writes no policy prose."""
    text = flat(skill())
    assert "moves and does not verify" in text, text[:200]
    assert "The spec decides; the command applies." in text
    assert "you judge and write" not in text


def test_the_skill_says_a_settle_is_not_a_work_item_and_owes_no_range_row():
    """#517's D1: a settle with no work item has no directory, so the skill
    hands it no row shape to copy, and says how it commits instead."""
    text = flat(skill())
    assert "| Range | Grounds |" not in text, (
        "the skill still hands a settle a range row"
    )
    assert "## A settle is not a work item" in skill()
    assert "A settle opens no directory under `seal/specs/`" in text
    assert "`seal no-work-item`" in text, "the skill does not say how a settle edits"
    assert "`SpecSeal-Routing: no work item`" in text, (
        "the skill does not say how a settle commits"
    )
    assert "[no-review]" not in text, "the skill still names the retired waiver"
    assert "reviewed at its pull request" in text
    assert "keeps no log" in text


def test_the_skill_says_the_directory_goes_with_the_rule_it_applied():
    text = flat(skill())
    assert "A directory goes only with the rule changes it applied" in text


def test_the_skill_states_how_the_changes_land():
    """#953: in place, in merge order, the later spec winning, and no
    marker."""
    text = flat(skill())
    assert "in merge order" in text
    assert "the later spec wins" in text
    assert "No marker is written" in text
    assert "<!-- specs/" not in text


def test_the_skill_says_it_fails_no_build():
    """G5. `settle` is invoked, never triggered — the ticket's own *Not this*."""
    text = flat(skill())
    assert "It is invoked, never triggered" in text
    assert "It does not fail a build." in text


def document(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return flat(f.read())


@pytest.mark.parametrize(
    "parts", [("seal", "README.md"), ("templates", "seal-README.md")]
)
def test_the_seal_readme_says_the_step_exists(parts):
    """Both editions of the same file, which
    `tests/test_first_setup_asks_once.py` holds byte for byte. It has said a
    work item "waits until a later `settle` folds it" since the root existed,
    and a reader who went looking for the step found nothing."""
    text = document(*parts)
    assert "settle --apply" in text and "skills/settle/SKILL.md" in text
    assert "A settle is not a work item and opens no directory here." in text, (
        f"{'/'.join(parts)} does not say a settle opens no work item (#517)"
    )
    assert "wrote no `spec.md` and holds nothing open" in text
    assert "retire-process" not in text and "folds it" not in text


def test_the_implement_skill_states_the_model():
    """S15. The policy root is the baseline a pull request does not edit, and
    the policy in force is it plus every unsettled spec's rule changes in
    merge order. The sentence it replaced made `settle` the one writer of a
    policy document a session wrote by hand."""
    text = document("skills", "implement", "SKILL.md")
    assert "one writer that does is `settle`" not in text
    assert "is the baseline, and a pull request does not edit it" in text
    assert "plus the rule changes of every unsettled spec, in merge order" in text


@pytest.mark.parametrize(
    "parts", [("agents", "framer.md"), ("README.md",), ("README.ko.md",)]
)
def test_every_other_carrier_points_to_the_model(parts):
    """S15. The model has one home, and every other carrier links to it."""
    text = document(*parts)
    assert "one writer that does is `settle`" not in text, "/".join(parts)
    assert (
        "`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*"
        in text
    ), "/".join(parts)


def test_the_release_checklist_carries_the_by_hand_step():
    """G5. `settle` is invoked and never triggered, so the only thing that
    makes it happen is a line in the list somebody works down on the day."""
    text = document("docs", "release-checklist.md")
    assert "settle --apply" in text, "the checklist never names the step"
    assert "retire-process" not in text and "settle --retire" not in text
    assert "A settle is not a work item" in text, (
        "the checklist does not say the settle opens no work item"
    )
    assert "range-row" not in text, "the checklist still owes a settle a range row"
    assert "skills/settle/SKILL.md" in text
    # Round 1, finding 10: a document past the ceiling is a report (Q6), and
    # the checklist points to the skill's section rather than ordering a split.
    assert (
        "`skills/settle/SKILL.md` *A document past its ceiling is split, never "
        "trimmed*" in " ".join(text.split())
    )
    assert "split along its headings in the same pull request" not in text


@pytest.mark.parametrize("edition", ["README.md", "README.ko.md"])
def test_both_cheat_sheets_carry_the_command(edition):
    """The count and the name are derived by
    `tests/test_chain_hooks_hardening.py`; what nothing derives is the row a
    reader actually types from. `CONTRIBUTING.md` requires the two editions to
    move together and the hygiene workflow only warns about it."""
    text = document(edition)
    assert "`settle [--apply]`" in text, (
        f"{edition}'s cheat sheet has no row for the command"
    )
    # The raw file is read, so the row is the row.
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        row = f.read().split("`settle [--apply]`")[1].split("\n")[0]
    assert "`## Rule changes`" in row, row
    assert "retire" not in row, row


def test_the_module_and_the_skill_both_say_local_mode_is_refused():
    """Round 2, finding 3 — contract rule 14's other half. The exit-code list named three
    causes of exit 2 and there were four, and the one document a session reads
    before it folds said nothing about the refusal at all. A person whose root
    sits under the git directory meets a stop no document predicted."""
    with open(SCRIPT, encoding="utf-8") as f:
        head = f.read().split('"""')[1]
    assert "Exit codes" in head, "the docstring no longer documents exit codes"
    assert "local mode" in head, "exit 2 covers a local-mode root and the list does not"
    assert "opted out" in head, "exit 2 covers the opt-out and the list does not"
    text = flat(skill())
    assert "refuses to run in local mode" in text, (
        "the skill never tells a session that this command stops in local mode"
    )
    assert "seal mode shared" in text, "the skill does not give the way out"
