"""The axes table is the review's coverage, so what it omits is invisible.

Eight axes each settled by reading one request end to end. A defect that needs
a second actor — a reservation mutated while an external call is in flight —
matched none of them, and an axis nobody listed leaves no trace: a row of
`## Not judged` records that you looked and could not decide, not that nobody
looked. Two documents share this table; drift between them is the bug.
"""

import pytest
from conftest import read


def test_the_table_asks_what_a_second_actor_does():
    axes = read("skills", "code-review", "SKILL.md")
    assert "| Concurrency & atomicity |" in axes, (
        "the axes table lost the only row that is not settled by reading one path"
    )
    for probe in ("between the read that decides", "retry executes twice"):
        assert probe in axes, f"the concurrency row lost `{probe}`"


def test_the_table_asks_the_security_questions():
    """Security was named in stage 2 and absent from the table, and the table
    is what makes an axis mandatory — an axis in prose leaves no `❓` when
    nobody walks it. Three of one round's four blocking findings had a
    stronger security frame than the one they were given, one of them a
    fail-open in a repository that keeps `test_gates_do_not_fail_open.py`
    for that class alone (issue #57)."""
    axes = read("skills", "code-review", "SKILL.md")
    assert "| Security |" in axes, "the axes table has no security row"
    for probe in ("fails open or closed", "crafted name, path, or payload"):
        assert probe in axes, f"the security row lost `{probe}`"
    # Round 1's 🟡 4: the prose groups Security with Concurrency as
    # not-settled-by-one-request-read and grounded only concurrency, so a
    # prose tightening could read the grouping as licensing a revert. The
    # ground is what makes the grouping earned rather than asserted.
    assert "nobody sends in good faith" in axes, (
        "the security paragraph lost the ground for its one-path exemption"
    )


def test_the_table_says_it_is_a_floor():
    """A fixed list is repeatable and blind in the same move.

    Without this the next unlisted axis — rounding, time zones, migration
    ordering — goes the way the concurrency one did."""
    axes = read("skills", "code-review", "SKILL.md")
    assert "### The table is a floor, not a ceiling" in axes
    assert "name this change's own axes before starting" in axes, (
        "nothing tells a round to add the axes this particular diff needs"
    )


def test_legacy_parity_still_points_at_that_table():
    """`legacy-parity` inherits the axes by reference, so one edit covers both.

    A copy would be two answers shipping at once."""
    assert "the same comparison axes" in read("skills", "legacy-parity", "SKILL.md")


def test_the_record_of_a_comparison_names_its_writer():
    """T5 of #970 (C5 of #2): the record of a comparison is written by the
    party that compared, and the tracer and the crafter write none.

    The section said *you*, so a crafter or a tracer opening the skill read
    itself as the writer of a record its definition does not name. #1027
    removed the parity mark and gave the comparison under `straight to the
    PR` to the sealer (`questions.md` Q1's default), so the writers are the
    proofer in each round record and the sealer in `guarantee.md`."""
    text = read("skills", "legacy-parity", "SKILL.md")
    heading = "\n## Recording the comparison\n"
    assert heading in text, "`legacy-parity` lost its section on the record"
    body = " ".join(text.split(heading, 1)[1].split("\n## ", 1)[0].split())
    for clause in (
        "| through the review chain | the proofer, in each round record |",
        "| straight to the PR | the sealer, once, in `guarantee.md` |",
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


def test_the_preset_block_carries_the_routing_decision():
    """The rule lived only in `implement`, which loads when the skill is invoked.

    A session that never invokes it would meet the gate at its first edit
    instead. Under `no work item` the block names the record and the trailer
    that replaced the per-command waiver (#1027)."""
    preset = read("templates", "setup", "claude-md-block.md")
    assert "Routing, decided at the start" in preset
    assert "seal/threads/<work-item-id>/routing.md" in preset
    assert "`seal no-work-item`" in preset
    assert "`Seal-Routing: no work item`" in preset
    assert "[no-review]" not in preset and "[no-parity]" not in preset


def test_a_later_round_inherits_no_verdict_anywhere():
    """A sentence saying axes carry "without re-walking" outranks a corrected
    sentence twenty lines below it; the old handoff protocol had both at once.
    The record's documents now say only what carries: where to look. The
    proofer's definition carries the table of which facts may be carried, and
    a verdict is on its re-derived side."""
    skill = " ".join(read("skills", "code-review", "SKILL.md").split())
    record = " ".join(read("docs", "the-review-record.md").split())
    proofer = " ".join(read("agents", "proofer.md").split())
    for stale in ("inherit judged axes", "without re-walking"):
        for where, text in (
            ("SKILL.md", skill),
            ("the-review-record.md", record),
            ("proofer.md", proofer),
        ):
            assert stale not in text, (
                f"verdict inheritance came back as `{stale}` in {where}"
            )
    assert "What carries is **where to look, not what was concluded**" in skill, (
        "the cross-session records stopped saying what actually carries"
    )
    assert (
        "| Where a subsystem lives, what a helper is for | Any verdict, on any axis |"
        in proofer
    ), "the proofer's table no longer puts every verdict on the re-derived side"


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
        "an added line is never supplied after the round that would have written it",
        "A record written before a line was added lacks it, and the lack is "
        "no finding for a later round.",
    ):
        assert said in record, f"the-review-record.md lost `{said}`"


def test_implement_and_the_preset_block_do_not_drift():
    """Both state the same decision; only one of them is always loaded.

    The routing section is `implement`'s orchestrator half since #292, so
    the skill side of the pair is `orchestration.md` — the file the session
    that asks the question reads, and no crafter spawn preloads."""
    implement = " ".join(read("skills", "implement", "orchestration.md").split())
    preset = " ".join(read("templates", "setup", "claude-md-block.md").split())
    # The answers each box writes are the orchestration file's alone since
    # #940: the block states the rules and leaves the vocabulary to the file
    # a session asking the question reads.
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
    for both in (
        "seal/threads/<work-item-id>/routing.md",
        # The write is its own command. Both documents mandate it and the
        # commit gate's first prompt now names it as a way out, so all three
        # drift together or not at all -- and this is the one the gate cannot
        # check for itself, because a batched write leaves nothing on disk to
        # look at.
        "in a command of its own",
        # The SHAPE of the asking, not just its vocabulary. The rule against
        # asking the axes separately is worth nothing if only one document
        # carries it, and the preset block is the one a session that never
        # loads the skill reads.
        #
        # The shape moved (#88): three checkboxes in one question became two
        # questions in one call, because two presets beside the axes is five
        # options and the harness allows four. **This phrase was
        # `one \`multiSelect\` question with three checkboxes` and went stale at
        # the build's phase 2 — red here from that commit on, and neither the
        # build nor round 1 ran this module.** Both chose their narrow set by
        # which files they had edited; this one reads two of those files and
        # was in neither set.
        #
        # It moved again (#911): the boxes meant nothing under two of
        # question 1's three answers and were on screen under all three, so
        # question 1 now goes alone and the boxes follow only under
        # `per axis`.
        "Ask question 1 alone; the boxes in a second call only under `per axis`.",
    ):
        assert both in implement, f"the skill lost `{both}`"
        assert both in preset, f"the preset block lost `{both}`"


def test_the_fix_pass_resumes_the_implementer():
    """A fix pass resumes the implementer only below the context threshold
    (#945). `tests/text/test_the_rules_have_one_owner.py` pins the rule and the
    command that reads the context; this pins the reason a resume is worth
    taking below it, the fresh spawn where the implementer's session is gone,
    and the limit a compaction leaves."""
    skill = " ".join(read("skills", "code-review", "orchestration.md").split())
    assert (
        "whose context already holds the files it wrote, the tests it ran and "
        "the grounds it recorded" in skill
    ), "the reason a resume is worth taking below the threshold went"
    assert (
        "A fix pass also takes a fresh spawn where the implementer's session no "
        "longer exists" in skill
    ), "the fallback for a session that no longer exists went"
    assert (
        "a compaction that shrank the implementer's context does not lower the "
        "reading" in skill
    ), "the limit a compaction leaves on the reading went"
