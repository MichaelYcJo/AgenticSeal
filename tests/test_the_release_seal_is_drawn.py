"""The release seal is drawn and attached at publish time (#718).

The cases here read the publishing workflow, `docs/branch-and-release.md`
and `docs/release-checklist.md`, and wait for #923;
`docs/branch-and-release.md` names this file on its `check:` line.

#942's phase 6 placed the cases of `.github/scripts/release_seal.py`'s
functions in `tests/test_release_seal.py`.
"""

import os

from conftest import flat
from conftest import load_module as load

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def test_the_publishing_workflow_installs_the_pins_the_runner_holds():
    """S16 (#718). The `seal` job's install line carries the parser and
    Pillow exactly as `run_tests.py` pins them, so the suite at the tag and
    the drawing run on the versions every other run of the suite uses."""
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
    assert runner.MARKDOWN_IT in installs[0] and runner.PILLOW in installs[0], installs
    # #647: the suite at the tag collects the table walker's case, which
    # imports the pinned renderer.
    assert runner.CMARKGFM in installs[0], installs


def test_the_release_tail_says_the_seal_is_a_second_act_that_never_fails_it():
    """`docs/branch-and-release.md` *Cutting a release*, in its paragraph
    **Every act the release performs once it reaches `main`**: the bullet on
    the note says the seal job runs only on a
    release this run created, edits only a glance table still as generated,
    and cannot turn the release red, and the section's `check:` line names
    the module that pins the fallback. It no longer says the seal is drawn
    from the broad gate's letter; seen red by the old sentence put back.
    How the seal is drawn is #1009 S1 and S2's, and the bullet's sentence
    on it is `spec.md`'s `## Rule changes` item of work item 1792624592."""
    text = flat("docs", "branch-and-release.md")
    bullet = text.split("**The release note publishes itself.**", 1)[1].split(
        "- **", 1
    )[0]
    assert "**Then the release's seal is attached.**" in bullet
    assert "letter" not in bullet
    assert "runs only when this run created the release" in bullet
    assert (
        "only to one whose glance table is still exactly as it was generated" in bullet
    )
    assert "so the seal can never turn the release red" in bullet
    section = text.split("**Every act the release performs once it reaches `main`", 1)[
        1
    ]
    enforced = section.split(" check: ", 1)[1].split("###", 1)[0]
    assert "tests/test_the_release_seal_is_drawn.py" in enforced.split(), enforced


def test_the_checklist_box_says_where_a_missing_seal_is_explained():
    """`docs/release-checklist.md` *6. After the merge*, the release-note box: it names the
    `seal` job, says its log carries the reason on a `::warning::` line and
    that it never fails the release, and gives the hand-drawn route."""
    text = flat("docs", "release-checklist.md")
    box = text.split("**A GitHub Release exists at `vX.Y.Z`**", 1)[1].split("- [ ]", 1)[
        0
    ]
    assert "the same workflow's `seal` job attaches `seal.png`" in box
    assert "says why on a `::warning::` line" in box
    assert "That job never fails the release." in box
    assert "`DRY_RUN=1 python3 .github/scripts/release_seal.py`" in box
    assert "`gh release upload`" in box
    # Round 1's finding 8: the route draws from the tag's tree and ends at the edit.
    assert "from a checkout at the tag" in box
    assert "then apply the note it prints with `gh release edit --notes-file`" in box
    # Round 2's finding 12: the reasons match the refusal's three causes.
    assert "published without one" in box
    assert "the pull requests moved between the two lists" in box
