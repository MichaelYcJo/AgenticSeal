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

from conftest import ROOT

DOCS = os.path.join(ROOT, "docs")
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


def pairs():
    """Every top-level `docs/X.ko.md` beside a `docs/X.md`, as names."""
    return [
        name[: -len(".ko.md")]
        for name in sorted(os.listdir(DOCS))
        if name.endswith(".ko.md")
        and os.path.isfile(os.path.join(DOCS, name[: -len(".ko.md")] + ".md"))
    ]


def read(name):
    with open(os.path.join(DOCS, name), encoding="utf-8") as f:
        return f.read()


def test_every_paired_document_carries_the_same_headings():
    """A1, A2. The walk reads at least one pair, so a broken listing cannot
    pass on an empty walk."""
    names = pairs()
    assert names, "no docs/X.ko.md beside a docs/X.md was read"
    found = []
    for name in names:
        found += disagreements(name, read(name + ".md"), read(name + ".ko.md"))
    assert not found, "\n".join(found)


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
