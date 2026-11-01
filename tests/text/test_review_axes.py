"""What a review round reads beside its diff: the comparison's record and
the original's resolution order in `legacy-parity`, an earlier round's
`executed` line, a record older than a line of the grammar, and where the
routing question is asked.

The comparison axes themselves are the proofer's to walk and to read: a
table of them pinned by its row labels turned red at a rewording and said
nothing about whether a round walked an axis.
"""

import pytest
from conftest import read


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


def test_the_core_names_where_the_routing_question_is():
    """#1177: the core reaches every session and every agent, so it is where
    a session that has opened no skill learns which section states the
    routing question and which hook holds it. The core's paragraph on asking
    a person cites both by path; what it says of the batch is the proofer's
    to read."""
    core = " ".join(read("skills", "core", "SKILL.md").split())
    asking = core.split("**Asking a person is the most expensive step.**", 1)
    assert len(asking) == 2, "the core lost its paragraph on asking a person"
    paragraph = asking[1].split("**", 1)[0]
    # The citation a session resolves to the section that asks the routing
    # question.
    assert (
        "`skills/implement/orchestration.md` *Orchestrator: how the work is routed*"
        in paragraph
    ), "the core does not name the routing section"
    # The path of the hook that refuses the first edit, which a session
    # opens when the refusal arrives.
    assert "`hooks/routing-edit-gate.py`" in paragraph, (
        "the core does not name the hook that refuses the first edit"
    )


def test_a_later_round_re_runs_an_executed_line():
    """S9 (#985): an `evidence: executed` line is a command a later round can
    run again, and it carries where a verdict does not. Re-deriving the claim
    instead spends the round on a search the earlier one already named, and
    a deleted probe is the case that needs saying: it comes back from its
    `## Probes` row. The record's document states it beside the line, and
    `skills/code-review/SKILL.md` *Earlier rounds*, which the proofer follows, says it
    where a round reads the earlier records."""
    record = " ".join(read("docs", "the-review-record.md").split())
    for said in (
        "**A later round re-runs an `executed` line rather than re-deriving "
        "the claim.**",
        "writes it again from its `## Probes` row",
    ):
        assert said in record, f"the-review-record.md lost `{said}`"
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
    record = " ".join(read("docs", "the-review-record.md").split())
    for said in (
        "added field is never supplied after the round that would have written it",
        "A record written before a line was added lacks it, and the lack is "
        "no finding for a later round.",
    ):
        assert said in record, f"the-review-record.md lost `{said}`"


def test_the_routing_section_holds_the_answers_and_the_shape():
    """The routing decision has one home, `implement`'s orchestrator half.

    It is `orchestration.md` since #292, the file the session that asks the
    question reads and no crafter spawn preloads. Until #1177 the preset
    block stated the rules beside it and this case held the two together;
    the block is retired, and the core the plugin's `SessionStart` hook
    prints names this section
    (`test_the_core_names_where_the_routing_question_is`), so what the block
    carried is held here, in the home alone."""
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
        # Under `no work item`, the record and the trailer that replaced the
        # per-command waiver (#1027), which the block named until #1177.
        "`seal no-work-item`",
        "`Seal-Routing: no work item`",
    ):
        assert said in implement, f"the skill lost `{said}`"
    assert "[no-review]" not in implement and "[no-parity]" not in implement
