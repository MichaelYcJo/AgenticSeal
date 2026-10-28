"""#450: a label this repository's documents specify exists on the tracker,
and stops existing on the issue it was spent on; the cases here read the
workflow and the document, and wait for #923.

  A12  the document says when the judgment is made, what removes a spent
       label, and that no backlog sweep is owed
  A14  the label step and the roll run whether or not a step before them
       failed, because neither needs a step after checkout to have succeeded
       (#515)

#942's phase 6 placed the cases of the scripts' functions in their files:
`.github/scripts/tracker_labels.py`'s in `tests/github/test_tracker_labels.py`,
`close_issues_on_release.py`'s in `tests/github/test_close_issues_on_release.py`,
and the label reader's case in
`tests/github/test_label_merged_on_release_branch.py`.

**Shown red before it was committed (contract rule 15).** A12 was run
against the document with the one sentence it pins removed, in phase 4 of
work item `1790076050-the-release-tail-is-three-acts-no-document-names`,
which #514's fold retired. A14 was added by work item
`1790134781-a-label-description-past-100-characters-fails-every-release`,
and its red run is recorded in that work item's ledger row C2.
"""

import os
import re

import pytest
from conftest import read
from test_tracker_labels import labels_module

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WORKFLOW = os.path.join(ROOT, ".github", "workflows", "close-issues-on-release.yml")
OWNER = "docs/issues-and-milestones.md"


def flat(rel):
    return " ".join(read(os.path.join(ROOT, rel)).split())


def test_every_declared_label_says_which_document_specifies_it():
    """A row here is a copy of a decision made somewhere else. A reader who
    cannot get back to the original has to take the copy's word for what the
    label means — which is how a label and its section drift apart."""
    mod = labels_module()
    assert mod.declared(), "nothing is declared, so the step reconciles nothing"
    for label in mod.declared():
        assert label["specified_by"].startswith(OWNER.split("/")[-1]) or label[
            "specified_by"
        ].startswith("docs/"), label
        document, _, heading = label["specified_by"].partition(" *")
        assert os.path.exists(os.path.join(ROOT, document)), (
            f"{label['name']!r} cites {document}, which is not in the tree"
        )
        # The section is cited by its heading text in italics, and the
        # heading is read as it renders, its own emphasis dropped.
        with open(os.path.join(ROOT, document), encoding="utf-8") as handle:
            headings = {
                line.lstrip("#").strip().replace("*", "")
                for line in handle
                if line.startswith("#")
            }
        assert heading.endswith("*") and heading[:-1] in headings, (
            f"{label['name']!r} cites {label['specified_by']!r}, and "
            f"{document} has no such heading"
        )


def test_the_workflow_runs_the_apply_arm_and_needs_no_new_permission():
    """The whole argument for this shape: the job already fires when `main`
    moves and already holds `issues: write`, so the act costs no new trigger
    and no new scope. A step that needed either would be a different
    decision."""
    text = "\n".join(
        line
        for line in read(WORKFLOW).splitlines()
        if not line.lstrip().startswith("#")
    )
    assert "tracker_labels.py --apply" in text
    assert "issues: write" in text
    assert text.count("permissions:") == 1, (
        "the job grew a second permissions block, so the claim that this "
        "needed no new scope has stopped being checkable here"
    )


@pytest.mark.parametrize(
    "step",
    [
        "create the labels the documents specify and the tracker lacks",
        "roll the flow-measurement issue to the next version",
    ],
)
def test_a_failed_step_cannot_skip_the_independent_steps_after_it(step):
    """A14, #515's second cost. The label step failed and the roll behind it
    was skipped, because a step with no `if:` runs only when every step before
    it succeeded. Neither step needs a step after checkout to have succeeded,
    so a failure before them must not decide whether they run."""
    steps = re.split(r"^      - ", read(WORKFLOW), flags=re.M)
    found = [s for s in steps if s.startswith(f"name: {step}\n")]
    assert len(found) == 1, f"the workflow has {len(found)} steps named {step!r}"
    assert re.search(r"^        if: \$\{\{ !cancelled\(\) \}\}\s*$", found[0], re.M), (
        f"{step!r} runs only when every step before it succeeded, so a failed "
        "earlier step skips it again"
    )


@pytest.mark.parametrize(
    ("clause", "what_it_answers"),
    [
        pytest.param(
            "The judgment is made at filing, and again when an issue moves milestone.",
            "when somebody decides it",
            id="when the judgment is made",
        ),
        pytest.param(
            "removes `size: now` from each issue it closes when the release "
            "reaches `main`",
            "what removes a spent one",
            id="what removes a spent label",
        ),
        pytest.param(
            "No sweep of the standing backlog is owed, and none should be done.",
            "whether the open backlog gets one",
            id="no sweep is owed",
        ),
    ],
)
def test_the_document_answers_what_it_left_open(clause, what_it_answers):
    """A12. Each of the three was a gap #450 named, and each is the kind a
    reader fills in for themselves — differently each time — when the document
    does not."""
    assert clause in flat(OWNER), (
        f"{OWNER} no longer says {what_it_answers}: {clause!r} is gone"
    )


def test_the_no_sweep_rule_carries_its_reason():
    """A rule with no reason is one the next reader overturns by having a
    different intuition, and the obvious first move after creating a label is
    to apply it everywhere."""
    doc = flat(OWNER)
    assert "a sweep is the batch, performed once, by the very party the label" in doc
