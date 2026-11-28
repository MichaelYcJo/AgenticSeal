"""What a review round reads beside its diff: the comparison's record, the
original's resolution order and the list of the original's output surface in
`legacy-parity`, with the framer's step that sends it to that list, and an
earlier round's `executed` line.

The comparison axes themselves are the proofer's to walk and to read: a
table of them pinned by its row labels turned red at a rewording and said
nothing about whether a round walked an axis.
"""

import re

from conftest import load_lib_module, read, section
from test_the_record_is_written_in_words import PARITY_REVIEW, PARITY_WORDS

# No TARGET: its cases hold what a review round reads across the parity skill, the review skill, the round record's form and the framer's definition.

# The reader of `routing.md`, whose `REVIEW_ANSWERS` a comparison's record is
# keyed by.
routing = load_lib_module("routing.py", "agentic_routing_for_review_axes")

PARITY = "skills/legacy-parity/SKILL.md"


def prose(rel, heading):
    """The `## ` section HEADING of REL folded onto one line, without its
    heading, its fenced blocks and its `check:` lines."""
    kept, fenced = [], False
    for line in section(read(rel), heading).split("\n"):
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and not line.startswith("check: "):
            kept.append(line)
    return " ".join(" ".join(kept).split())


def step(rel, n):
    """Step N of REL's `## Order of work`, folded onto one line."""
    lines = section(read(rel), "## Order of work").split("\n")
    start = next(i for i, line in enumerate(lines) if line.startswith(f"{n}. "))
    end = next(
        (i for i in range(start + 1, len(lines)) if re.match(r"\d+\. ", lines[i])),
        len(lines),
    )
    return " ".join(" ".join(lines[start:end]).split())


def test_the_list_of_the_originals_surface_has_one_home_and_one_writer():
    """#15, the scenario *The frame lists the surface*: in a migration the
    design's *Grounding* lists the original's output surface, and the
    framer writes it.

    The comparison started at the coordinates the design cited, so an item
    nobody cited was compared by nobody: a port shipped two of its
    original's thirteen response items missing, and a person found them by
    hand after the migration was called done."""
    body = prose(PARITY, "## The original's coordinates")
    # The path and the heading of the list's home, which the framer writes
    # and the tracer and the proofer open.
    assert "`frame/design.md` *Grounding*" in body, (
        f"{PARITY} *The original's coordinates* names no home for the list"
    )
    # The party that writes the list, and the act. The section names the
    # framer a second time, where the original does not resolve for it, so
    # the party alone would hold with the writer gone.
    assert "framer writes the list" in body, (
        f"{PARITY} *The original's coordinates* names no writer for the list"
    )


def test_the_framer_is_sent_to_the_section_that_asks_for_the_list():
    """#15, the scenario *The frame lists the surface*, the framer's half:
    its definition names the parity config at step 4, and the section that
    says what the *Grounding* lists is the one it is sent to there. The
    config alone says that the original ranks between the ticket and the
    code, and nothing of what the frame lists."""
    said = step("agents/framer.md", 4)
    # The citation the framer resolves to the section above.
    assert f"`{PARITY}` *The original's coordinates*" in said, (
        "`agents/framer.md` step 4 does not send the framer to the list"
    )


def test_an_item_the_port_lacks_differs_and_the_walk_stands_in_the_round():
    """#15, the scenarios *The dropped field is a finding* and *The walk is
    readable next round*: an item the original sends and the port does not
    takes one of the four verdict words, `differs` by default, and each item
    walked stands in the round record, so the next round opens the walk
    instead of enumerating the surface again."""
    rel, heading = PARITY_REVIEW
    body = prose(rel, heading)
    named = [w for w in re.findall(r"`(\w+)`", body) if w in PARITY_WORDS]
    # The verdict word an absent item takes, named outside the block of
    # labels, which the proofer gives the item in the round record.
    assert "differs" in named, f"{rel} {heading} gives an absent item no verdict"
    # The record and its section where each walked item stands, which the
    # next round opens.
    for home in ("round record", "`## Confirmations`"):
        assert home in body, f"{rel} {heading} does not name {home!r} for the walk"


def test_an_item_the_list_and_the_port_both_lack_is_located_in_both():
    """#15, round 1's second finding: an item the original sends that the
    design's list and the port both lack is the issue's own case, since
    nobody listed it and so nobody built it. Its one finding is located in
    `frame/design.md`, and in the port's entry point as well where nothing
    grounds leaving the item out, so a fix that adds the item to the list
    alone does not close a `differs` finding."""
    rel, heading = PARITY_REVIEW
    body = prose(rel, heading)
    for part in (
        # The round record's field that says where a finding shows, which the
        # proofer writes and the chain check reads.
        "`location:`",
        # The path the finding is located in, which the fix pass opens.
        "`frame/design.md`",
    ):
        assert part in body, (
            f"{rel} {heading} does not locate an item both lack with {part!r}"
        )


def test_the_record_of_a_comparison_names_its_writer():
    """T5 of #970 (C5 of #2): the record of a comparison is written by the
    party that compared, and the tracer and the crafter write none.

    The section said *you*, so a crafter or a tracer opening the skill read
    itself as the writer of a record its definition does not name. #1027
    removed the parity mark and gave the comparison under `straight to the
    PR` to the inspector (`questions.md` Q1's default), so the writers are the
    proofer in each round record and the inspector in `inspection.md`. #1198
    put each line in a block: the round block, and the verdict block each
    run of the inspector appends."""
    text = read("skills", "legacy-parity", "SKILL.md")
    heading = "\n## Recording the comparison\n"
    # The heading `agents/proofer.md` and `skills/implement/orchestration.md`
    # cite in italics.
    assert heading in text, "`legacy-parity` lost its section on the record"
    body = " ".join(text.split(heading, 1)[1].split("\n## ", 1)[0].split())
    for fact in (
        # The `Review` answers `lib/routing.py#REVIEW_ANSWERS` accepts, each a
        # row's first cell, which a reader matches against `routing.md`.
        *(f"| {answer} |" for answer in routing.REVIEW_ANSWERS),
        # The file the inspector appends the line to.
        "`inspection.md`",
    ):
        assert fact in body, f"the record of a comparison lost {fact!r}"


def test_the_resolution_order_ends_with_the_caller_asking():
    """S4 of #970, the skill's half (round 1, finding 1): the order ends with
    the caller asking and recording, and a reader that cannot ask returns
    `original not found`. T3 holds the tracer's half; this is the text every
    reader of the skill opens, and the base's wording made the reader ask.
    The order and who asks are the proofer's to read."""
    text = read("skills", "legacy-parity", "SKILL.md")
    heading = "\n## The migration config\n"
    assert heading in text, "`legacy-parity` lost its migration-config section"
    body = " ".join(text.split(heading, 1)[1].split("\n## ", 1)[0].split())
    for fact in (
        # The path of the file the declaration lives in, which a reader opens.
        "`~/.claude/agentic/parity-paths.json`",
        # The words a reader that cannot ask returns, which its caller reads
        # as no original resolved.
        "`original not found`",
    ):
        assert fact in body, f"the resolution order lost {fact!r}"


def test_a_later_round_re_runs_an_executed_line():
    """S9 (#985): an `evidence: executed` line is a command a later round can
    run again, and it carries where a verdict does not. A deleted probe comes
    back from its `## Probes` row. The record's document states it beside
    the line, and `skills/code-review/SKILL.md` *Earlier rounds*, which the
    proofer follows, says it where a round reads the earlier records; what
    each says is the proofer's to read."""
    record = " ".join(read("docs", "forms", "the-round-record.md").split())
    # The round record's heading a later round writes a deleted probe again
    # from.
    assert "`## Probes`" in record, "the-round-record.md lost `## Probes`"
    skill = " ".join(read("skills", "code-review", "SKILL.md").split())
    rounds = skill.split("## Earlier rounds", 1)[1].split("## The record", 1)[0]
    # The line a later round re-runs, the field and the value `lib/fields.py`
    # reads.
    assert "`evidence: executed`" in rounds, (
        "`skills/code-review/SKILL.md` *Earlier rounds* lost `evidence: executed`"
    )
