"""What `hooks/root-migrate.py`'s own file does not hold.

#942's phase 5 rebuilt the hook's cases into `tests/test_root_migrate.py`.
These stay: the README's by-hand sequence read out of the document and run
against what the hook does, and the hook's source read for its rider, both
for #923, which takes the cases that read prose. The case of the
session-start group's order is `hooks/dispatch.py`'s, and it is in
`tests/test_dispatch.py`.
"""

import os
import shutil
import subprocess

import pytest
from conftest import ROOT, git, shell_probe
from test_root_migrate import (  # noqa: F401  -- the fixtures the cases take
    ITEM,
    _templates,
    hook,
    proj,
    start,
)


def test_the_hook_reads_the_old_names_and_nothing_else_does():
    """S15's exception, pinned from the other side: this file is the one
    reader of `.specseal/` left in `hooks/`, and it carries a rider saying it
    can go once no repository is left to migrate."""
    src = open(os.path.join(ROOT, "hooks", "root-migrate.py"), encoding="utf-8").read()
    assert "# RIDER:" in src and ".specseal" in src
    for name in sorted(os.listdir(os.path.join(ROOT, "hooks"))):
        if name.endswith(".py") and name != "root-migrate.py":
            text = open(os.path.join(ROOT, "hooks", name), encoding="utf-8").read()
            assert ".specseal/map" not in text, f"{name} still reads the old map"


HEADINGS = {
    "README.md": "### Coming up from 0.3.x",
    "README.ko.md": "### 0.3.x 에서 올라오는 경우",
}


def by_hand_block(readme, text=None):
    """The `bash` block under the README's coming-up section, comments off.

    Bounded at the next `## ` heading and asserted to be there: the lines are
    run under `bash -c`, so a block that left its section must fail here
    rather than let a later block in the document run in its place.
    """
    if text is None:
        text = open(os.path.join(ROOT, readme), encoding="utf-8").read()
    assert HEADINGS[readme] in text, f"{readme} lost its coming-up section"
    section = text.split(HEADINGS[readme], 1)[1].split("\n## ", 1)[0]
    assert "```bash\n" in section, f"{readme}: the by-hand block left its section"
    block = section.split("```bash\n", 1)[1].split("```", 1)[0]
    return [ln.split("#", 1)[0].strip() for ln in block.splitlines() if ln.strip()]


@pytest.mark.parametrize("readme", ["README.md", "README.ko.md"])
def test_the_readmes_by_hand_sequence_yields_the_hooks_tracked_set(
    hook,  # noqa: F811
    proj,  # noqa: F811
    tmp_path,
    readme,
):
    """Round 1's P6, pinned to the document: the block a person copies is
    read out of the README and run line by line on a copy of the fixture, and
    `git ls-files` has to agree with the hook's.

    The block is a `bash` block, so each line runs under `bash -c` -- not
    `shell=True`, which is `cmd.exe` on Windows and runs none of `mkdir -p`,
    `git mv … && …` or `rmdir` as written. The precondition is executed, not
    assumed: on a `windows-latest` runner `bash` on PATH is the WSL stub,
    which fails everything, and PR #90's windows leg showed the hand copy
    untouched at the comparison below. The hook's own tests passed on that
    leg, so a skip here costs Windows nothing the hook is asked to do.
    """
    why = shell_probe("bash")
    if why:
        pytest.skip(f"bash: {why} -- the by-hand block is a bash block")
    hand = tmp_path / "hand"
    shutil.copytree(proj, hand)
    start(hook, proj)
    for line in by_hand_block(readme):
        line = line.replace("<id>", ITEM)
        subprocess.run(["bash", "-c", line], cwd=str(hand), capture_output=True)
    tracked = lambda d: git(d, "ls-files").stdout.split()
    assert tracked(hand) == tracked(proj), tracked(hand)


@pytest.mark.parametrize("readme", ["README.md", "README.ko.md"])
def test_by_hand_block_fails_loudly_when_the_block_leaves_its_section(readme):
    """Round 2's green E. A README edited so the block sits under a later
    heading must fail with the assertion, never run that later block."""
    text = open(os.path.join(ROOT, readme), encoding="utf-8").read()
    head, rest = text.split(HEADINGS[readme], 1)
    before, after = rest.split("```bash\n", 1)
    block, tail = after.split("```", 1)
    moved = (
        head
        + HEADINGS[readme]
        + before
        + tail
        + "\n\n## Elsewhere\n\n```bash\n"
        + block
        + "```\n"
    )
    with pytest.raises(AssertionError, match="left its section"):
        by_hand_block(readme, text=moved)
    assert by_hand_block(readme, text=text), "the real README still yields lines"
