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
from conftest import flattened as flat

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")


def test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule():
    """Contract rule 14's half of D3. The policy said such an item *is kept by name*; that
    is overturned. Since #1033 the skill and the policy say such an item
    leaves like any other, once the settling session has closed every open
    row of its record."""
    policy = " ".join(document("docs", "the-record-layout.md").split())
    assert "and it is kept by name" not in policy, (
        "the policy still keeps a spec-less directory by name"
    )
    assert "it is retired by that rule, with no marker" not in policy
    assert "A released work item leaves at the settle whatever it wrote" in policy
    assert "decides every open row of its record before it goes" in policy
    assert "`frame/design.md` states no rule and goes the same way" in policy
    text = flat(skill())
    assert "A released work item with no `frame/design.md` states no rule" in text
    assert "it leaves like any other" in text
    for edition in ("README.md", "README.ko.md"):
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
    assert "population floor" in text, (
        "the skill never tells a session that its own checks read the corpus"
    )
    assert "a list of readers written in any document is not the whole list" in text, (
        "the skill lets a written list of readers stand as the whole list, "
        "which is what makes a fold turn a suite red"
    )
    for answer in ("retire the case", "re-point it at a fixture corpus", "decline"):
        assert answer in text, f"the skill does not offer `{answer}`"


def test_the_skill_says_the_session_writes_the_latest_decision_and_asks_nobody():
    """S11, #1033: the specs are a timeline, the code says what holds now,
    and the settling session writes each section; the script neither writes
    `docs/` nor judges, and nobody is asked. The sentence that made the
    command the applier is gone."""
    text = flat(skill())
    assert (
        "The specs say what was decided and in what order, the code says what "
        "holds now, and the settling session writes each section as the latest "
        "decision the code bears out. The script reads and removes; it neither "
        "writes `docs/` nor judges."
    ) in text
    assert "It asks nobody at any step" in text
    assert "The spec decides; the command applies." not in text
    assert "moves and does not verify" not in text
    assert "It does not verify." not in text


def test_the_skill_states_the_settling_sessions_procedure():
    """S11 and S13, #1033's *In* item 3, in order: the dry run, each group
    written as its latest decision with the code winning, the superseded
    operations settled unapplied, the specs read whole, every row decided and
    closed, the defaults written down, each rule's `check:` targets,
    `--apply`, the broad gate, and the pull request body. Round 1 of #1033,
    finding 5: a row that fits two kinds has one reading. Round 3 of #1033,
    finding 1: step 6 holds no searched set of test modules, since no search
    of the tests' text lists every check that reads what the session wrote,
    and step 8's broad gate is the one run that reads every check, run again
    after a fix. Round 4 of #1033, finding 1: each clause of steps 6 and 8
    that S13 names is pinned, step 6's fix and second dry run and step 8's
    failure path among them."""
    text = flat(skill())
    procedure = text.split("## The settling session's procedure")[1].split("## ")[0]
    steps = [
        "Run `seal settle`, the dry run",
        "Write the section as the latest decision states it",
        "Where the code has moved past that decision, write what the code does",
        "is superseded: it is settled with its group and not applied",
        "Read each spec listed to read whole",
        "close it in its record with `closed` and what closed it",
        "A row that fits more than one kind takes the first that fits, in the "
        "table's order",
        "take a default and write it down",
        "Run each rule's `check:` targets over what you wrote",
        "and change what a failure shows still standing on the old fact",
        "Then run the dry run again",
        "The step is done when every `check:` target passes",
        "finds a module only by how it spells a path",
        "step 8 runs every one",
        "Run `seal settle --apply`.",
        "Run the repository's `Broad gate` row.",
        "It is the one run that reads every check",
        "change that pin or copy, and name each in the pull request body",
        "answer it as *Answer every check that reads the corpus* says",
        "then run the row again",
        "The step is done when the row passes with no edit after it",
        "Open the pull request.",
    ]
    at = [procedure.find(step) for step in steps]
    assert -1 not in at, [s for s, n in zip(steps, at, strict=True) if n < 0]
    assert at == sorted(at), "the procedure's steps are out of order"
    assert "git grep" not in procedure, "step 6 still searches the tests' text"
    for kind in ("moot", "answered", "a measurement nobody has taken"):
        assert f"| {kind} |" in procedure, kind
    # questions.md Q1's default: one issue per distinct measurement.
    assert "one issue per distinct measurement (`gh issue create`)" in procedure
    assert "`seal/follow-up.md` row" in procedure


def test_the_skill_says_a_from_locates_and_is_no_precondition():
    """S11, #1033's *In* item 6: the grammar is unchanged, and `from` is the
    text as the framer read it, which locates the change and is not a
    precondition; `--apply` writes no policy document."""
    text = flat(skill())
    raw = skill().split("\n## Rule changes\n")[1].split("\n## A rule has one shape")
    section = flat(raw[0])
    assert "**`from` is the text as the spec's framer read it.**" in section
    assert "it is not a precondition" in section
    assert "applies nothing" not in section, "the grammar still says what a replay did"
    apply = text.split("## What `--apply` does")[1].split("## ")[0]
    assert "It writes no policy document." in apply
    assert "whether or not it wrote a `frame/design.md`" in apply


def test_the_skill_says_a_settle_is_not_a_work_item_and_owes_no_range_row():
    """#517's D1: a settle with no work item has no directory, so the skill
    hands it no row shape to copy, and says how it commits instead."""
    text = flat(skill())
    assert "| Range | Grounds |" not in text, (
        "the skill still hands a settle a range row"
    )
    assert "## A settle is not a work item" in skill()
    assert "A settle opens no directory under `seal/threads/`" in text
    assert "`seal no-work-item`" in text, "the skill does not say how a settle edits"
    assert "`Seal-Routing: no work item`" in text, (
        "the skill does not say how a settle commits"
    )
    assert "[no-review]" not in text, "the skill still names the retired waiver"
    assert "reviewed at its pull request" in text
    assert "keeps no log" in text
    # Round 1 finding 4 of #955: no commit holds a local work item, so git
    # history keeps the removed specs only where the root is shared.
    assert (
        "Where the root is shared the removed specs are in git history; in "
        "local mode no commit holds them"
    ) in text, text


def test_the_skill_says_it_fails_no_build():
    """G5. `settle` is invoked, never triggered — the ticket's own *Not this*."""
    text = flat(skill())
    assert "It is invoked, never triggered" in text
    assert "It does not fail a build." in text


def document(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return flat(f.read())


@pytest.mark.parametrize(
    "parts", [("seal", "README.md"), ("templates", "setup", "seal-README.md")]
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
    assert (
        "whose record holds no open row, whether or not it wrote a `frame/design.md`"
        in (text)
    )
    assert "retire-process" not in text and "folds it" not in text


def test_the_implement_skill_states_the_model():
    """S15. The policy root is the baseline a pull request does not edit, and
    the policy in force is it plus the latest decision each unsettled spec
    states at each section (#1033). The sentence it replaced made `settle`
    the one writer of a policy document a session wrote by hand."""
    text = document("skills", "implement", "SKILL.md")
    assert "one writer that does is `settle`" not in text
    assert "is the baseline, and a pull request does not edit it" in text
    assert (
        "the latest decision the unsettled specs' rule changes state at each "
        "section, in merge order"
    ) in text
    assert "plus the rule changes of every unsettled spec, in merge order" not in text


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
    move together and the hygiene workflow only warns about it. Since #1033
    the row says the settling session writes each section and `--apply`
    writes no document, and it links the procedure's section rather than
    restating it (round 1 of #1033, finding 2)."""
    text = document(edition)
    assert "`seal settle [--apply]`" in text, (
        f"{edition}'s cheat sheet has no row for the command"
    )
    # The raw file is read, so the row is the row.
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        row = f.read().split("`seal settle [--apply]`")[1].split("\n")[0]
    assert "`## Rule changes`" in row, row
    assert "`skills/settle/SKILL.md` *The settling session's procedure*" in row, row
    assert "retire" not in row, row
    assert "`HEAD`" not in row, "the row still says the base is asked"


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
