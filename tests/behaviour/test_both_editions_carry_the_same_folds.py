"""Both editions of a document carry the same outline, heading for heading.

`CONTRIBUTING.md` requires every document with a `.ko.md` edition to move
with its English one, and a mirror drifts one edit at a time. The two
editions are prose in two languages, so nothing here compares sentences. What
is language-neutral is the outline: the sequence of heading levels. A heading
added to one edition only, or one at another level, changes it.

A heading is a live line (`skills/verify/scripts/unverified_check.py#live_lines`,
so one quoted in a fence is no heading) matching `^ {0,3}#{1,6}` followed by
a space, a tab or the end of the line, as CommonMark reads one. A digit
straight after the hashes is prose, and each edition has a line that begins
`#<number>`.
"""

import importlib.util
import os
import re

import pytest
from conftest import ROOT, build_tracked_tree, decline_if_shrunken, git_listing, on_disk

READER = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")

HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]|$)")


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


uc = _load(READER, "unverified_check")


def outline(text):
    """The level of each live heading of TEXT, in order."""
    levels = []
    for line, live in uc.live_lines(text.splitlines()):
        heading = HEADING.match(line) if live else None
        if heading:
            levels.append(len(heading.group(1)))
    return levels


def disagreements(name, english, korean):
    """What the two editions of `name` disagree on, as sentences; empty when
    they agree."""
    en, ko = outline(english), outline(korean)
    if en == ko:
        return []
    return [
        f"{name}: the heading levels differ: English {en}, Korean {ko}; one "
        "edition has a heading the other lacks"
    ]


def pairs(root=ROOT):
    """`(names, missing)`: every tracked `X.ko.md` whose tracked `X.md` stands
    beside it, both on disk, as repository-relative names without the
    extension; and each tracked half of such a pair the working tree has
    deleted. The listing is git's, so an untracked file is no pair, and
    `on_disk` keeps a deleted half from ending the walk at its `open` (#432)."""
    listed = git_listing(root, "ls-files", "--", "*.md")
    present, gone = on_disk(root, listed)
    present = set(present)
    korean = sorted(n for n in listed if n.endswith(".ko.md"))
    english = {k: k[: -len(".ko.md")] + ".md" for k in korean}
    names = [k[: -len(".ko.md")] for k in korean if {k, english[k]} <= present]
    halves = set(korean) | set(english.values())
    return names, sorted(n for n in gone if n in halves)


def under_root(name):
    """The path of NAME, a repository-relative name written with `/`."""
    return os.path.join(ROOT, *name.split("/"))


def read(name):
    with open(under_root(name), encoding="utf-8") as f:
        return f.read()


# The pairs the walk must reach (#1055 S11).
ALIVE = ("README", "docs/experiments/README")


def unread(names, missing):
    """The ALIVE pairs the walk did not read, or `pytest.skip` when every one
    of them is unread only because the working tree deleted one of its halves.

    Conditional, as `test_no_document_names_the_old_roots.py#uncovered` is: a
    decline over a neighbour that is merely mid-edit would carry a real
    finding away with it."""
    absent = [n for n in ALIVE if n not in names]
    halves = {h: n for n in absent for h in (n + ".md", n + ".ko.md")}
    explained = {halves[m] for m in missing if m in halves}
    if absent and set(absent) == explained:
        decline_if_shrunken(
            sorted(m for m in missing if m in halves), "the edition pairs"
        )
    return [n for n in absent if n not in explained]


def test_every_paired_document_carries_the_same_headings():
    """A1, A2. The walk reads at least one pair, so a broken listing cannot
    pass on an empty walk. Every pair on disk is judged before anything
    declines, so a deleted edition takes no other pair's finding with it."""
    names, missing = pairs()
    assert names, "no X.ko.md beside an X.md was read"
    found = []
    for name in names:
        found += disagreements(name, read(name + ".md"), read(name + ".ko.md"))
    assert not found, "\n".join(found)
    # #1055 S11: the pairs outside top-level `docs/` are read too.
    gone = unread(names, missing)
    assert not gone, f"not read: {gone}"


def test_a_deleted_half_of_a_named_pair_declines_and_nothing_else_does(tmp_path):
    """The liveness half declines only over a named pair the working tree
    deleted a half of, and reports one that is simply not there. The deleted
    half is the English one, which a listing of `*.ko.md` alone dropped
    without a word (#1055 round 3, finding 2)."""
    root = build_tracked_tree(
        tmp_path,
        {
            "README.md": "# A\n",
            "README.ko.md": "# A\n",
            "docs/experiments/README.md": "# B\n",
            "docs/experiments/README.ko.md": "# B\n",
            # A deleted file with no edition is no half of a pair.
            "docs/alone.md": "# C\n",
        },
        deleted=("README.md", "docs/alone.md"),
    )
    names, missing = pairs(root)
    assert names == ["docs/experiments/README"], names
    assert missing == ["README.md"], missing
    with pytest.raises(pytest.skip.Exception):
        unread(names, missing)

    def reported(names, missing):
        # A decline raised here would skip this case and pass it, so it
        # fails instead: each call below must report, not decline.
        try:
            return unread(names, missing)
        except pytest.skip.Exception as declined:
            pytest.fail(f"declined where it must report: {declined}")

    assert reported(names, []) == ["README"]
    # A neighbour mid-edit is no reason to decline: every named pair was read.
    assert reported(list(ALIVE), ["docs/other.ko.md"]) == []
    # One named pair lost to the working tree does not excuse the other,
    # which is simply not there: that one is reported, and nothing declines.
    assert reported([], ["README.md"]) == ["docs/experiments/README"]


def test_the_contribution_guide_owns_the_rule_and_names_this_check():
    """A11. `CONTRIBUTING.md` is the rule's owner, and a rule whose owner does
    not say which check reads it is one a contributor meets only at CI."""
    with open(os.path.join(ROOT, "CONTRIBUTING.md"), encoding="utf-8") as f:
        guide = f.read()
    assert "every document with a `.ko.md`\n  edition" in guide, (
        "CONTRIBUTING.md's pairing rule no longer covers every `.ko.md` edition"
    )
    assert "tests/behaviour/test_both_editions_carry_the_same_folds.py" in guide, (
        "CONTRIBUTING.md's pairing rule does not name the check that reads it"
    )
    # #1055 S12: the check reads every pair, not top-level `docs/` alone.
    assert "every top-level" not in " ".join(guide.split()), (
        "CONTRIBUTING.md still says the check reads top-level `docs/` alone"
    )


def test_a_heading_added_to_one_edition_only_is_named():
    """A3, planted."""
    english = "# T\n## A\n## B\n"
    korean = "# T\n## 가\n"
    found = disagreements("d", english, korean)
    assert len(found) == 1 and "heading levels differ" in found[0], found


def test_a_hash_without_a_space_and_a_fenced_heading_are_not_read():
    """`#458 settled` is prose, and a heading inside a fence is a quotation;
    neither is part of the outline."""
    english = "# T\n#458 settled it.\n```\n## not a heading\n```\n"
    korean = "# T\n"
    assert disagreements("d", english, korean) == []


def test_a_heading_indented_up_to_three_spaces_is_read():
    """Round 1, correction: CommonMark reads `   ## A` as a heading, and four
    spaces as an indented code block."""
    assert "heading levels differ" in disagreements("d", "# T\n   ## A\n", "# T\n")[0]
    assert disagreements("d", "# T\n    ## code\n", "# T\n") == []


def test_a_heading_with_a_tab_or_no_text_is_read():
    """Round 2, correction: CommonMark ends the hashes at a space, a tab or
    the end of the line."""
    for heading in ("##\tA", "##"):
        found = disagreements("d", f"# T\n{heading}\n", "# T\n")
        assert found and "heading levels differ" in found[0], heading
