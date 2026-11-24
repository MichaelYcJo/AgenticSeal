"""The release seal is drawn and attached at publish time (#718).

The cases here read the publishing workflow and
`docs/releasing/release-checklist.md`; `docs/releasing/branch-and-release.md`
names this file on its `check:` line, and its bullet on the seal is the
proofer's to read.

The cases of `.github/scripts/release_seal.py`'s functions stand in
`tests/github/test_release_seal.py`.
"""

import os

from conftest import code_lines, flat
from workflows import load as load_workflow

# No TARGET: its cases hold the release seal across .github/workflows/publish-release.yml, tests/requirements.txt and docs/releasing/release-checklist.md.


def test_the_publishing_workflow_installs_the_requirements_file():
    """S16 (#718), and #1575. The `seal` job's install line reads
    `tests/requirements.txt` and names nothing beside it, so the suite at
    the tag runs on the packages, at the versions, every other run of the
    suite installs."""
    workflow = load_workflow(
        os.path.join(".github", "workflows", "publish-release.yml")
    )
    installs = [
        line.split()
        for job in workflow["jobs"].values()
        for step in job["steps"]
        for line in code_lines(step.get("run", ""))
        if line.split()[:2] == ["pip", "install"]
    ]
    assert installs == [["pip", "install", "-r", "tests/requirements.txt"]], installs


def test_the_checklist_box_says_where_a_missing_seal_is_explained():
    """`docs/releasing/release-checklist.md` *After the merge*, the release-note box: it names the
    `seal` job and its asset, the `::warning::` line its log carries the
    reason on, and the commands of the hand-drawn route. When the job runs,
    that it never fails the release, and the reasons it gives are the
    proofer's to read."""
    text = flat("docs", "releasing", "release-checklist.md")
    box = text.split("**A GitHub Release exists at `vX.Y.Z`**", 1)[1].split("- [ ]", 1)[
        0
    ]
    # The job name `seal` and the asset `seal.png`, which the person running
    # the box looks for on the workflow run and on the release.
    assert "the same workflow's `seal` job attaches `seal.png`" in box
    # The annotation `::warning::`, the line `release_seal.py` prints the
    # reason on and the person reads in the job's log.
    assert "says why on a `::warning::` line" in box
    # The command the person runs to draw the seal by hand.
    assert "`DRY_RUN=1 python3 .github/scripts/release_seal.py`" in box
    # The command the person runs to attach it.
    assert "`gh release upload`" in box
    # The command and flag the person runs to apply the note the script
    # prints (round 1's finding 8).
    assert "then apply the note it prints with `gh release edit --notes-file`" in box
