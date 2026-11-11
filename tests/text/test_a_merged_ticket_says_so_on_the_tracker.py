"""Issue #359, the signal half: the workflow that runs
`.github/scripts/label_merged_on_release_branch.py` on a squash into
`release/vX.Y.Z`. These cases read the workflow and wait for #923.

#942's phase 6 placed the cases of the script's functions in
`tests/github/test_label_merged_on_release_branch.py`.
"""

import os

from conftest import ROOT, read
from workflows import load

WORKFLOW = os.path.join(
    ROOT, ".github", "workflows", "label-merged-on-release-branch.yml"
)


def test_the_token_is_the_smallest_that_can_add_a_label():
    """Read the block as a mapping, not as text: a substring search for
    `contents: write` passes `contents:  write`, which is one value to YAML.

    Its sibling `close-issues-on-release.yml` has the same case. This token is
    handed a pull request body somebody else wrote, and the only thing that
    keeps that from mattering is how little it can do.
    """
    granted = load(WORKFLOW).get("permissions")
    assert granted, "the workflow states no permissions block, so it inherits all"
    assert granted == {"contents": "read", "issues": "write"}, (
        f"the token's scopes changed: {granted}. Its only writes are a label "
        "create and a label add"
    )


def test_the_trigger_is_a_push_to_a_release_branch_and_nothing_else():
    """A trigger an untrusted pull request can fire hands it this token.

    The sibling workflow's case says the same of `push: [main]`; a release
    branch is pushed to by a squash merge, which needs write access to the
    repository.
    """
    on = load(WORKFLOW)["on"]
    assert list(on) == ["push"], "the workflow gained a second trigger"
    assert on["push"] == {"branches": ["release/*"]}, (
        "the push trigger no longer names `release/*` alone"
    )


def test_the_checkout_has_the_range_the_script_reads():
    """`arrived()` reads `git log before..after`. At depth 1 neither end of
    that range is in the clone, and the run reads the tip alone — which is the
    fallback that dropped three of four pull requests when it fired."""
    assert "fetch-depth: 0" in read(WORKFLOW)
