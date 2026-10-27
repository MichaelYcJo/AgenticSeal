"""What `hooks/root-migrate.py`'s own file does not hold.

#942's phase 5 rebuilt the hook's cases into `tests/test_root_migrate.py`.
These stay: the README's by-hand sequence read out of the document and run
over the 0.3.x fixture, the coming-up section read for the one path it
gives, and the source of `hooks/` read for the 0.3.x names and the hook's
rider, all for #923, which takes the cases that read prose. The case of the
session-start group's order is `hooks/dispatch.py`'s, and it is in
`tests/test_dispatch.py`.
"""

import os
import subprocess

import pytest
from conftest import ROOT, git, shell_probe
from test_root_migrate import (  # noqa: F401  -- the fixtures the cases take
    ITEM,
    _templates,
    proj,
)


def test_no_hook_names_the_0_3_x_roots():
    """No code of the plugin opens `.specseal/` or a top-level `specs/`, so
    no file in `hooks/` names the first or keeps a constant for the second,
    and the migration hook still carries the rider saying it can go once no
    repository is left to migrate."""
    src = open(os.path.join(ROOT, "hooks", "root-migrate.py"), encoding="utf-8").read()
    assert "# RIDER:" in src
    for name in sorted(os.listdir(os.path.join(ROOT, "hooks"))):
        if name.endswith(".py"):
            text = open(os.path.join(ROOT, "hooks", name), encoding="utf-8").read()
            assert ".specseal" not in text, f"{name} names the 0.3.x root"
            assert "OLD_ITEMS" not in text, f"{name} keeps the 0.3.x specs/"


HEADINGS = {
    "README.md": "### Coming up from 0.3.x",
    "README.ko.md": "### 0.3.x 에서 올라오는 경우",
}
# The sentence each README's coming-up section says the by-hand path with,
# and the words of the automatic move it no longer describes.
ONLY_PATH = {
    "README.md": "this is the only path",
    "README.ko.md": "이 방법 하나뿐입니다",
}
SESSION_START = {"README.md": "session start", "README.ko.md": "세션 시작"}


def coming_up(readme):
    """The README's coming-up section, its whitespace folded."""
    text = open(os.path.join(ROOT, readme), encoding="utf-8").read()
    assert HEADINGS[readme] in text, f"{readme} lost its coming-up section"
    return " ".join(text.split(HEADINGS[readme], 1)[1].split("\n## ", 1)[0].split())


@pytest.mark.parametrize("readme", sorted(HEADINGS))
def test_the_coming_up_section_gives_the_by_hand_path_as_the_only_one(readme):
    """Nothing moves the 0.3.x layout at a session start any more, so the
    section says the commands are the only path and no longer describes a
    move a hook makes."""
    section = coming_up(readme)
    assert ONLY_PATH[readme] in section, section
    assert SESSION_START[readme] not in section, section


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


# What git tracks once the by-hand block has run over `proj`: the old root's
# files under `seal/`, the work item under `seal/specs/`, and the project's
# own entry left under `specs/`.
BY_HAND = sorted(
    [
        "seal/README.md",
        "seal/follow-up.md",
        "seal/map.md",
        f"seal/map/{ITEM}.md",
        f"seal/specs/{ITEM}/rounds/round-1.md",
        f"seal/specs/{ITEM}/routing.md",
        "specs/notes/todo.md",
    ]
)


@pytest.mark.parametrize("readme", ["README.md", "README.ko.md"])
def test_the_readmes_by_hand_sequence_yields_the_layout_the_plugin_reads(
    proj,  # noqa: F811
    readme,
):
    """Round 1's P6, pinned to the document: the block a person copies is
    read out of the README and run line by line on the fixture, and `git
    ls-files` has to list the layout the plugin reads, with the project's own
    entry under `specs/` left where it was.

    The block is a `bash` block, so each line runs under `bash -c` -- not
    `shell=True`, which is `cmd.exe` on Windows and runs none of `mkdir -p`,
    `git mv … && …` or `rmdir` as written. The precondition is executed, not
    assumed: on a `windows-latest` runner `bash` on PATH is the WSL stub,
    which fails everything, and PR #90's windows leg showed the hand copy
    untouched at the comparison below. No code of the plugin runs on that leg
    either, so a skip here costs Windows nothing the plugin is asked to do.
    """
    why = shell_probe("bash")
    if why:
        pytest.skip(f"bash: {why} -- the by-hand block is a bash block")
    for line in by_hand_block(readme):
        line = line.replace("<id>", ITEM)
        subprocess.run(["bash", "-c", line], cwd=str(proj), capture_output=True)
    tracked = sorted(git(proj, "ls-files").stdout.split())
    assert tracked == BY_HAND, tracked


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
