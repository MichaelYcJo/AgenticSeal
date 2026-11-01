"""The round record is written in words, and so is every text that states it.

The record's facts are its `seal` blocks; a mark the check does not read is
a mark a reader has to sort, and sorting marks is what four rounds of this
repository found read wrong. So no file an agent reads as instruction carries
an emoji or a proof block: every definition, every skill's `SKILL.md` and
every template (T6 of work item 1792251842, which wrote the crafter anew,
which took over T39's four files). Each verdict word means one thing, too: a
repair with no commit on the branch closes `deferred <where it was
repaired>`, one a commit made closes `fixed <commit>`, and `rejected` is a
finding that does not hold (T41, `frame/design.md` of
`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
*What a round records*).
"""

import glob
import os
import re

import pytest
from conftest import ROOT, read

# Pictographs, the dingbats and miscellaneous symbols the old marks came from
# (U+2600-U+27BF: the check mark, the cross), the technical block
# (U+2300-U+23FF: the hourglass, the stopwatch), the arrows-and-shapes block
# the white square came from, and the variation selector that asks for the
# emoji rendering. Dashes, arrows and mathematical signs prose uses sit
# outside every range.
EMOJI = re.compile("[\U0001f000-\U0001faff☀-➿⬀-⯿⌀-⏿️]")

# A proof block's head line, `<mark> <skill> applied`, and a seal line's
# `sealed @ <sha>`. The hand-back's labels carry the claims now, and the
# sealer's `guarantee.md` is the one seal.
PROOF_BLOCK = re.compile(
    r"^[^\w\n]*[a-z][\w-]* applied[ \t]*$|\bsealed @", re.MULTILINE
)

# The files an agent reads as instruction, every one of them read.
CORPUS = ("agents/*.md", "skills/*/SKILL.md", "templates/*/*.md")


def corpus():
    """Every file CORPUS names, relative to the root, with forward slashes."""
    found = []
    for pattern in CORPUS:
        paths = sorted(glob.glob(os.path.join(ROOT, pattern)))
        assert paths, f"{pattern} names no file"
        found += [os.path.relpath(p, ROOT).replace(os.sep, "/") for p in paths]
    return found


def section(text, heading):
    """The lines of the `## ` section HEADING, to the next `## ` heading."""
    lines = text.split("\n")
    start = lines.index(heading)
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )
    return lines[start:end], start


def test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block():
    found = []
    for rel in corpus():
        text = read(rel)
        for n, line in enumerate(text.split("\n"), 1):
            if EMOJI.search(line):
                found.append(f"{rel}:{n}: {line.strip()}")
        for m in PROOF_BLOCK.finditer(text):
            n = text.count("\n", 0, m.start()) + 1
            found.append(f"{rel}:{n}: a proof block: {m.group().strip()}")
    assert not found, (
        "a mark or a proof block in a file an agent reads; write the word:\n"
        + "\n".join(found)
    )


PARITY_REVIEW = ("skills/legacy-parity/SKILL.md", "## Parity review")
PARITY_WORDS = ["differs", "grounded", "equivalent", "unread"]


def test_the_parity_verdicts_are_four_words():
    """T4 of #970: a parity review labels a verdict with one of four
    lowercase words at the start of its line.

    The labels were four emoji nobody read, and no case read the section, so
    a mark or a fifth label could come back with every other case green."""
    rel, heading = PARITY_REVIEW
    lines, _ = section(read(rel), heading)
    fences = [i for i, line in enumerate(lines) if line.startswith("```")]
    assert len(fences) == 2, f"{rel} {heading} holds no one block of labels"
    labels = [
        line.split()[0] for line in lines[fences[0] + 1 : fences[1]] if line.strip()
    ]
    # The four verdict words a parity review writes at the start of a line,
    # which the caller of the review reads as its verdicts.
    assert labels == PARITY_WORDS, (
        f"{rel} {heading}: the labels are {labels}, not {PARITY_WORDS}"
    )


def sentences(lines):
    """The sentences of LINES, folded onto one line and cut after each `.`."""
    text = " ".join(" ".join(lines).split())
    return re.split(r"(?<=\.)\s+(?=[A-Z`*])", text)


@pytest.mark.rule("fix-pass-two-lines")
def test_a_repair_with_no_commit_closes_deferred_where_it_was_made():
    rel = "docs/the-review-record.md"
    lines, _ = section(read(rel), "## The round record")
    opener = "**The fix pass appends one close block per finding"
    start = next(i for i, line in enumerate(lines) if line.startswith(opener))
    end = next(i for i in range(start, len(lines)) if lines[i].startswith("check: "))
    paragraph = sentences(lines[start:end])

    # The sentence the verdict below is read in, so it cannot pass on a
    # paragraph that names no such repair.
    outside = [s for s in paragraph if "outside the tree" in s]
    assert outside, (
        f"{rel} *The round record*: the fix-pass paragraph names no repair "
        "outside the tree"
    )
    for s in outside:
        # The close block's `verdict:` value `deferred <where it was
        # repaired>`, whose `deferred` word `hooks/lib/fields.py` reads.
        assert "`deferred <where it was repaired>`" in s, (
            f"a repair outside the tree closes `deferred <where it was repaired>`: {s}"
        )

    # The sentence the verdict below is read in, as above.
    corrections = [s for s in paragraph if "correction to a record" in s]
    assert corrections, (
        f"{rel} *The round record*: the fix-pass paragraph names no record correction"
    )
    for s in corrections:
        # The close block's `verdict:` value `fixed <commit>`, which
        # `hooks/lib/fields.py` reads.
        assert "`fixed <commit>`" in s, (
            f"a repair a commit made closes `fixed <commit>`: {s}"
        )
