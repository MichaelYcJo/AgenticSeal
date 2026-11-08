"""What a review round reads beside its diff: the comparison's record, the
original's resolution order and the list of the original's output surface in
`legacy-parity`, with the two agent steps that write and check that list, an
earlier round's `executed` line, and a record older than a line of the
grammar.

The comparison axes themselves are the proofer's to walk and to read: a
table of them pinned by its row labels turned red at a rewording and said
nothing about whether a round walked an axis.
"""

import re

import pytest
from conftest import read
from test_the_record_is_written_in_words import PARITY_REVIEW, PARITY_WORDS, section

PARITY = "skills/legacy-parity/SKILL.md"


def prose(rel, heading):
    """The `## ` section HEADING of REL folded onto one line, without its
    heading, its fenced blocks and its `check:` lines."""
    lines, _ = section(read(rel), heading)
    kept, fenced = [], False
    for line in lines[1:]:
        if line.startswith("```"):
            fenced = not fenced
        elif not fenced and not line.startswith("check: "):
            kept.append(line)
    return " ".join(" ".join(kept).split())


def step(rel, n):
    """Step N of REL's `## Order of work`, folded onto one line."""
    lines, _ = section(read(rel), "## Order of work")
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
    # The round record's field that says where a finding shows, and the two
    # places it names: the port, where the item is missing, and the design.
    for part in ("`location:`", "port's entry point", "`frame/design.md`"):
        assert part in body, (
            f"{rel} {heading} does not locate an item both lack with {part!r}"
        )


def test_the_tracer_names_what_the_list_of_the_surface_lacks():
    """#15, the scenario *The tracer names what the list lacks*: the tracer,
    spawned before a phase, reports each item of the original's output
    surface the design's list lacks, with its coordinate; its report is
    where the list is checked against the original before review."""
    said = step("agents/tracer.md", 6)
    # The list the skill names, and its lack, which the orchestrator reads
    # in the report as a finding on the frame.
    for part in ("output surface", "lacks"):
        assert part in said, f"`agents/tracer.md` step 6 lost {part!r}"


def test_the_record_of_a_comparison_names_its_writer():
    """T5 of #970 (C5 of #2): the record of a comparison is written by the
    party that compared, and the tracer and the crafter write none.

    The section said *you*, so a crafter or a tracer opening the skill read
    itself as the writer of a record its definition does not name. #1027
    removed the parity mark and gave the comparison under `straight to the
    PR` to the sealer (`questions.md` Q1's default), so the writers are the
    proofer in each round record and the sealer in `guarantee.md`. #1198
    put each line in a block: the round block, and the verdict block each
    run of the sealer appends."""
    text = read("skills", "legacy-parity", "SKILL.md")
    heading = "\n## Recording the comparison\n"
    assert heading in text, "`legacy-parity` lost its section on the record"
    body = " ".join(text.split(heading, 1)[1].split("\n## ", 1)[0].split())
    for clause in (
        "| through the review chain | the proofer, in the round block of each "
        "round record |",
        "| straight to the PR | the sealer, in the verdict block each of its "
        "runs appends to `guarantee.md` |",
        "the tracer and the crafter record none",
    ):
        assert clause in body, f"the record of a comparison lost {clause!r}"
    assert "-parity`" not in body, "the section still writes the mark"


def test_the_resolution_order_ends_with_the_caller_asking():
    """S4 of #970, the skill's half (round 1, finding 1): the order ends with
    the caller asking and recording, and a reader that cannot ask returns
    `original not found`. T3 holds the tracer's half; this is the text every
    reader of the skill opens, and the base's wording made the reader ask."""
    text = read("skills", "legacy-parity", "SKILL.md")
    heading = "\n## The migration config\n"
    assert heading in text, "`legacy-parity` lost its migration-config section"
    body = " ".join(text.split(heading, 1)[1].split("\n## ", 1)[0].split())
    for clause in (
        "it lives in `~/.claude/agentic/parity-paths.md`",
        "the caller asks the user and records the answer",
        "a reader that cannot ask returns `original not found` with what it tried",
        "A comparison against a guessed original proves nothing.",
    ):
        assert clause in body, f"the resolution order lost {clause!r}"


def test_a_later_round_re_runs_an_executed_line():
    """S9 (#985): an `evidence: executed` line is a command a later round can
    run again, and it carries where a verdict does not. Re-deriving the claim
    instead spends the round on a search the earlier one already named, and
    a deleted probe is the case that needs saying: it comes back from its
    `## Probes` row. The record's document states it beside the line, and
    `skills/code-review/SKILL.md` *Earlier rounds*, which the proofer follows, says it
    where a round reads the earlier records."""
    record = " ".join(read("docs", "forms", "the-round-record.md").split())
    for said in (
        "**A later round re-runs an `executed` line rather than re-deriving "
        "the claim.**",
        "writes it again from its `## Probes` row",
    ):
        assert said in record, f"the-round-record.md lost `{said}`"
    skill = " ".join(read("skills", "code-review", "SKILL.md").split())
    rounds = skill.split("## Earlier rounds", 1)[1].split("## The record", 1)[0]
    said = (
        "Where you weigh an earlier finding, re-run its `evidence: executed` "
        "line rather than re-deriving the claim"
    )
    assert said in rounds, (
        f"`skills/code-review/SKILL.md` *Earlier rounds* lost `{said}`"
    )


@pytest.mark.rule("old-table-shape-refused")
def test_a_record_written_before_a_line_was_added_is_no_finding():
    """S10 (#985): a record written before the grammar gained a line lacks
    it, and a later round that judges it by the new grammar reports a defect
    nobody could have avoided. #971's `false-rows.md:117` is that class: a
    0.21 record judged by 0.22's grammar, counted a `wrong` finding."""
    record = " ".join(read("docs", "checks", "the-pull-request-check.md").split())
    for said in (
        "added field is never supplied after the round that would have written it",
        "A record written before a line was added lacks it, and the lack is "
        "no finding for a later round.",
    ):
        assert said in record, f"the-pull-request-check.md lost `{said}`"


def test_the_routing_section_holds_the_answers_and_the_shape():
    """The routing decision has one home, `implement`'s orchestrator half.

    It is `orchestration.md` since #292, the file the session that asks the
    question reads and no crafter spawn preloads. Until #1177 the preset
    block stated the rules beside it and this case held the two together;
    the block is retired, so what it carried is held here, in the home
    alone."""
    implement = " ".join(read("skills", "implement", "orchestration.md").split())
    for only in (
        "through the review chain",
        "straight to the PR",
        "open the pull request",
        "stop before the pull request",
        "What is checked is the answer",
        "each box is a row of",
        # The third axis. A document still saying two would send a session to
        # a template whose row it never asked about.
        "`the session`",
    ):
        assert only in implement, f"the skill lost `{only}`"
    for said in (
        "seal/threads/<work-item-id>/routing.md",
        # The write is its own command, and this is the one part the gate
        # cannot check for itself, because a batched write leaves nothing on
        # disk to look at.
        "in a command of its own",
        # The SHAPE of the asking, not just its vocabulary.
        #
        # The shape moved (#88): three checkboxes in one question became two
        # questions in one call, because two presets beside the axes is five
        # options and the harness allows four. **This phrase was
        # `one \`multiSelect\` question with three checkboxes` and went stale at
        # the build's phase 2 — red here from that commit on, and neither the
        # build nor round 1 ran this module.** Both chose their narrow set by
        # which files they had edited; this case then read two of those files
        # and was in neither set.
        #
        # It moved again (#911): the boxes meant nothing under two of
        # question 1's three answers and were on screen under all three, so
        # question 1 now goes alone and the boxes follow only under
        # `per axis`.
        "Ask question 1 alone; the boxes in a second call only under `per axis`.",
        # Under `no work item`, the trailer that records the answer in place
        # of the per-command waiver (#1027), which the block named until #1177.
        "`Seal-Routing: no work item`",
    ):
        assert said in implement, f"the skill lost `{said}`"
    assert "[no-review]" not in implement and "[no-parity]" not in implement
