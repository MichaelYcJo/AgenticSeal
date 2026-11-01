"""The release seal is drawn and attached at publish time (#718).

The cases here read the publishing workflow and `docs/release-checklist.md`,
and wait for #923; `docs/branch-and-release.md` names this file on its
`check:` line, and its bullet on the seal is the proofer's to read.

#942's phase 6 placed the cases of `.github/scripts/release_seal.py`'s
functions in `tests/github/test_release_seal.py`.
"""

import os

from conftest import ROOT, flat
from conftest import load_module as load


def test_the_publishing_workflow_installs_the_pins_the_runner_holds():
    """S16 (#718). The `seal` job's install line carries the parser exactly
    as `run_tests.py` pins it, so the suite at the tag runs on the version
    every other run of the suite uses. Since #857 the seal is a copy of a
    committed PNG, so the line installs no Pillow."""
    runner = load(
        os.path.join(ROOT, ".github", "scripts", "run_tests.py"), "rt_for_seal"
    )
    with open(
        os.path.join(ROOT, ".github", "workflows", "publish-release.yml"),
        encoding="utf-8",
    ) as handle:
        installs = [
            line.split("run:", 1)[1].split()
            for line in handle
            if "run: pip install" in line
        ]
    assert len(installs) == 1, installs
    assert runner.MARKDOWN_IT in installs[0], installs
    assert not any(word.lower().startswith("pillow") for word in installs[0]), installs
    # #647: the suite at the tag collects the table walker's case, which
    # imports the pinned renderer.
    assert runner.CMARKGFM in installs[0], installs


def test_the_checklist_box_says_where_a_missing_seal_is_explained():
    """`docs/release-checklist.md` *6. After the merge*, the release-note box: it names the
    `seal` job and its asset, the `::warning::` line its log carries the
    reason on, and the commands of the hand-drawn route. When the job runs,
    that it never fails the release, and the reasons it gives are the
    proofer's to read."""
    text = flat("docs", "release-checklist.md")
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
