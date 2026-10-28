"""Issue #359, the signal half: the workflow that runs
`.github/scripts/label_merged_on_release_branch.py` on a squash into
`release/vX.Y.Z`. These cases read the workflow and wait for #923.

#942's phase 6 placed the cases of the script's functions in
`tests/github/test_label_merged_on_release_branch.py`.
"""

import os
import re

from conftest import read

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WORKFLOW = os.path.join(
    ROOT, ".github", "workflows", "label-merged-on-release-branch.yml"
)


def workflow_settings():
    """The workflow with its comment lines removed.

    A setting that exists only in a comment is not a setting, which is
    `tests/test_ci_gives_the_checks_what_they_need.py`'s measured reason for
    the same helper: dropping a real `types:` line and keeping the comment
    above it left that file's checks green. It is also what lets the trigger
    below be read at all — this workflow carries a comment block between
    `on:` and `permissions:`, and a reader that stops at the first
    unindented line stops there.
    """
    return "\n".join(
        line
        for line in read(WORKFLOW).splitlines()
        if not line.lstrip().startswith("#")
    )


def test_the_token_is_the_smallest_that_can_add_a_label():
    """Read the block as a mapping, not as text: a substring search for
    `contents: write` passes `contents:  write`, which is one value to YAML.

    Its sibling `close-issues-on-release.yml` has the same case. This token is
    handed a pull request body somebody else wrote, and the only thing that
    keeps that from mattering is how little it can do.
    """
    workflow = workflow_settings()
    block = re.search(r"^permissions:\n((?:  [\w-]+:.*\n)+)", workflow, re.M)
    assert block, "the workflow states no permissions block, so it inherits all"
    granted = dict(re.findall(r"^  ([\w-]+):\s*(\S+)\s*$", block.group(1), re.M))
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
    workflow = workflow_settings()
    on = re.search(r"^on:\n((?:  .*\n|\n)*?)^\w", workflow, re.M)
    assert on and re.findall(r"^  ([\w_]+):", on.group(1), re.M) == ["push"], (
        "the workflow gained a second trigger"
    )
    assert re.search(r"^\s*branches:\s*\['release/\*'\]\s*$", workflow, re.M), (
        "the push trigger no longer names `release/*` alone"
    )


def test_the_checkout_has_the_range_the_script_reads():
    """`arrived()` reads `git log before..after`. At depth 1 neither end of
    that range is in the clone, and the run reads the tip alone — which is the
    fallback that dropped three of four pull requests when it fired."""
    assert "fetch-depth: 0" in read(WORKFLOW)
