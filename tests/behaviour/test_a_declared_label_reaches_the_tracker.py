"""#450: a label this repository's documents specify exists on the tracker,
and stops existing on the issue it was spent on; the cases here read the
workflow and the document.

  A12  the document names the workflow that removes a spent label
  A14  the label step and the roll run whether or not a step before them
       failed, because neither needs a step after checkout to have succeeded
       (#515)

The cases of the scripts' functions stand in their files:
`.github/scripts/tracker_labels.py`'s in `tests/github/test_tracker_labels.py`,
the case holding each declared label's citation of its section among them,
`close_issues_on_release.py`'s in `tests/github/test_close_issues_on_release.py`,
and the label reader's case in
`tests/github/test_label_merged_on_release_branch.py`. The document's path is
that first file's `OWNER`.

**Shown red before it was committed (contract rule 15).** A12 was run
against the document with the one sentence it pins removed, in phase 4 of
work item `1790076050-the-release-tail-is-three-acts-no-document-names`,
which #514's fold retired. A14 was added by work item
`1790134781-a-label-description-past-100-characters-fails-every-release`,
and its red run is recorded in that work item's ledger row C2.
"""

import os

import pytest
from conftest import ROOT, read
from test_tracker_labels import OWNER
from workflows import load

WORKFLOW = os.path.join(ROOT, ".github", "workflows", "close-issues-on-release.yml")


def flat(rel):
    return " ".join(read(os.path.join(ROOT, rel)).split())


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
    # The step's command `tracker_labels.py --apply`, which the runner runs.
    assert "tracker_labels.py --apply" in text
    # The permission `issues: write`, which the runner grants the job.
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
    found = [
        named
        for job in load(WORKFLOW)["jobs"].values()
        for named in job["steps"]
        if named.get("name") == step
    ]
    assert len(found) == 1, f"the workflow has {len(found)} steps named {step!r}"
    assert found[0].get("if") == "${{ !cancelled() }}", (
        f"{step!r} runs only when every step before it succeeded, so a failed "
        "earlier step skips it again"
    )


def test_the_document_names_what_spends_the_label():
    """A12. What removes a spent label was a gap #450 named, and a reader
    fills it in for themselves, differently each time, when the document
    does not."""
    # The workflow path a reader resolves for what removes the spent label,
    # and the label as
    # `.github/scripts/close_issues_on_release.py#SPENT_ON_CLOSE` spells it.
    assert (
        "`.github/workflows/close-issues-on-release.yml` removes `size: now`"
        in flat(OWNER)
    ), f"{OWNER} no longer names the workflow that removes `size: now`"
