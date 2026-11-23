"""#450: a label this repository's documents specify stops existing on the
issue it was spent on; the cases here read the workflow and the document.

  A12  the document names the workflow that removes a spent label
  A14  the roll runs whether or not a step before it failed, because it needs
       no step after checkout to have succeeded (#515)

The cases of the scripts' functions stand in their files:
`close_issues_on_release.py`'s in `tests/github/test_close_issues_on_release.py`,
and the label reader's case in
`tests/github/test_label_merged_on_release_branch.py`. `OWNER` is the
document that specifies the label.

**Shown red before it was committed (contract rule 15).** A12 was run
against the document with the one sentence it pins removed, in phase 4 of
work item `1790076050-the-release-tail-is-three-acts-no-document-names`,
which #514's fold retired. A14 was added by work item
`1790134781-a-label-description-past-100-characters-fails-every-release`,
and its red run is recorded in that work item's ledger row C2.
"""

import os

import pytest
from conftest import ROOT, flat
from workflows import load

# No TARGET: its cases hold the label rule across .github/workflows/close-issues-on-release.yml and docs/releasing/issues-and-milestones.md.

WORKFLOW = os.path.join(ROOT, ".github", "workflows", "close-issues-on-release.yml")
OWNER = "docs/releasing/issues-and-milestones.md"


@pytest.mark.parametrize(
    "step",
    ["roll the flow-measurement issue to the next version"],
)
def test_a_failed_step_cannot_skip_the_independent_steps_after_it(step):
    """A14, #515's second cost. The step before the roll failed and the roll
    behind it was skipped, because a step with no `if:` runs only when every
    step before it succeeded. The roll needs no step after checkout to have
    succeeded, so a failure before it must not decide whether it runs."""
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
