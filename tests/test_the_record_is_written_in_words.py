"""The round record is written in words, and so is every text that states it.

The record's facts are its labelled lines and its `Confirms` cells; a mark
the check does not read is a mark a reader has to sort, and sorting marks is
what four rounds of this repository found read wrong. So the template, the
review skill's findings format and the two definitions that write or fill a
round carry no emoji at all (`spec.md` of
`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
§*What a round records*, T39).
"""

import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")

# Pictographs, the dingbats and miscellaneous symbols the old marks came from
# (U+2600-U+27BF: the check mark, the cross), the arrows-and-shapes block the
# white square came from, and the variation selector that asks for the
# emoji rendering. Dashes, arrows and mathematical signs prose uses sit
# outside every range.
EMOJI = re.compile("[\U0001f000-\U0001faff☀-➿⬀-⯿️]")

# The proof block's marker is one every skill shares, and `spec.md` §*Removes*
# leaves it to part B and #940 by name; its verdict line below it is words.
SHARED_MARKER = "📋 code-review applied"


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def section(text, heading):
    """The lines of the `## ` section HEADING, to the next `## ` heading."""
    lines = text.split("\n")
    start = lines.index(heading)
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )
    return lines[start:end], start


def emoji_lines(rel, lines, first=0):
    return [
        f"{rel}:{first + i + 1}: {line.strip()}"
        for i, line in enumerate(lines)
        if EMOJI.search(line) and line.strip() != SHARED_MARKER
    ]


def test_the_template_the_format_and_the_two_definitions_carry_no_emoji():
    found = []
    for rel in ("templates/sdd-round.md", "agents/warden.md", "agents/smith.md"):
        found += emoji_lines(rel, read(rel).split("\n"))
    rel = "skills/code-review/SKILL.md"
    lines, start = section(read(rel), "## Findings format")
    assert len(lines) > 40, f"{rel} §Findings format read as {len(lines)} lines"
    found += emoji_lines(rel, lines, start)
    assert not found, "an emoji in a text that states the round record:\n" + "\n".join(
        found
    )
