"""The commands `agents/proofer.md` has a verifying round type to read the
code of a range that holds a merge of the base.

Those reads are typed by hand, so `lib/gitcmd.py#argv` does not add
`--ignore-submodules=none` to them as it does for every script's `diff`,
`log` and `status`. Without the flag, a repository whose
`diff.ignoreSubmodules` reads `all`, or whose `.gitmodules` entry reads
`ignore = all`, hides a commit that only moves a submodule's pointer, and a
merge's resolution that sets one (#1648).
"""

import pathlib

import conftest

# No TARGET: its case reads agents/proofer.md, a definition no script imports.


ROOT = pathlib.Path(conftest.ROOT)
PROOFER = ROOT / "agents" / "proofer.md"


def test_a_merge_round_reads_the_branch_and_the_resolution_with_submodules_shown():
    """S2 of #1648. The paragraph on a round after a merge of the base names
    both commands with the flag.

    Protects: a verifying round that reads a merge's range and never sees that
    the branch, or the merge's resolution, moves a submodule's pointer."""
    text = " ".join(PROOFER.read_text(encoding="utf-8").split())
    head = text.index("**A round after a merge of the base reviews")
    paragraph = text[head : text.index("That text is part of the target", head)]
    # The branch's own commits, as the round types the read.
    assert (
        "`git log --ignore-submodules=none --no-merges -p <a>..<b> ^<base>`"
        in paragraph
    ), paragraph
    # The merge's resolution, as the round types the read.
    assert "`git show --ignore-submodules=none <merge>`" in paragraph, paragraph
