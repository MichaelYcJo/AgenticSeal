"""The broad gate's stamp reaches the person it is drawn for (#400).

Work item 1790562543. An inspector's stdout was a pipe into a report that arrived
folded behind `ctrl+o`, so a stamp drawn there was never seen. The stamp is
drawn from the inspector's `cleared` inspection: the inspector's
`agentic stamp --inspection` queues its values under the git common dir (#1376),
and the plugin's `Stop` hook draws each undrawn file once, after the
orchestrator's turn's text (#1430).

This module holds the cases that read the documents, and the case that
holds both commands' `--help` to one fact.
`skills/verify/scripts/stamp.py`'s own cases, the queue and the draw
among them, are `tests/skills/test_stamp.py`.
"""

import os
import subprocess
import sys

from conftest import ROOT, flat, flattened, load_module, read, section

# No TARGET: its cases hold the stamp across docs/checks/the-stamp.md, two skills, agents/inspector.md and both READMEs, and hold stamp.py's and broad_gate.py's --help to one fact.


STAMP = os.path.join(ROOT, "skills", "verify", "scripts", "stamp.py")
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")


def stamp_module():
    return load_module(STAMP, "agentic_stamp_for_its_values")


def stamp(*args):
    """`stamp.py` as a person types it, stdout a pipe."""
    return subprocess.run(
        [sys.executable, STAMP, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )


# `docs/checks/the-stamp.md` *The stamp*, read flattened: the stamp's rules
# stand in a document of their own since #1312.
STAMP_DOC = ("docs", "checks", "the-stamp.md")
STAMP_HEADING = "## The stamp"


# --- S16: the rules are where they are read ----------------------------------


def test_the_orchestrator_is_given_the_stamps_commands_and_the_runs_lines():
    """S16, the orchestrator's half (contract rule 14), and #975 S13. The rule
    sits in the section that spawns the inspector and names the facts the
    orchestrator acts on: the command the inspector queues the stamp with, the
    lines the broad run opens with, which the orchestrator relays, and the
    command that stays the person's to type. When the stamp is drawn, that
    the orchestrator draws none, and what it does with the inspector's line are
    the proofer's to read. Since #1579 that section stands in the file the
    orchestrator opens once the last round has no finding open."""
    text = flat("skills", "code-review", "gate-to-pull-request.md")
    section = text.split(
        "## Orchestrator: from the preflight to the open pull request", 1
    )[1]
    for fact in (
        # The command the inspector queues the stamp with, whose line the
        # orchestrator meets in the inspector's hand-back.
        "`agentic stamp --inspection`",
        # The lines the broad run's stdout opens with, which the orchestrator
        # relays.
        "`BROAD GATE PASSED`",
        "`BROAD GATE FAILED`",
        # Round 1's yellow 1 of #400: the command a line names for the person
        # to type, which the orchestrator quotes and never runs.
        "`agentic stamp --from`",
    ):
        assert fact in section, fact


def test_the_verify_skill_names_what_queues_the_stamp_and_what_draws_it():
    """S16, `verify`'s half, and #975 S13. The stamp is the inspector's, drawn
    once per work item from its `cleared` inspection, and the gate draws
    nothing. #1376: queued by the inspector's `agentic stamp --inspection` under
    either root; #1430: drawn by the plugin's `Stop` hook. The skill names
    the command and the hook; its sentences are the proofer's to read."""
    text = flat("skills", "verify", "SKILL.md")
    for fact in (
        # The command the inspector queues the stamp's values with.
        "`agentic stamp --inspection`",
        # The harness event whose hook draws the stamp, which a reader
        # resolves in `hooks/hooks.json`.
        "`Stop`",
    ):
        assert fact in text, fact


def test_the_policy_names_the_command_the_marker_and_the_command_to_draw():
    """S16, the policy's half, and #975 S10 and S13. `docs/checks/the-stamp.md`
    *The stamp* carries the drawing rule, names the command that queues the
    stamp, and ends in a `check:` line naming the marker the cases that
    queue and draw it carry; a second statement, on what the screen shows,
    names `agentic stamp --from <path>` for where a file was written. The
    rule's trigger, its limits, its exit and the places nothing draws are
    the proofer's to read (1792363231 S7 and S8, #1027 and #1376); the
    command's closing ` || exit 0` is pinned. #1492: the measurement of
    2026-11-06 is cited from its `docs/experiments/` record."""
    text = flattened(section(read(*STAMP_DOC), STAMP_HEADING))
    screen = "**What the person's screen shows is not checked"
    rule, unchecked = text.split(screen, 1)
    # The command that queues the stamp, and the one that draws it, which a
    # person resolves to see what wrote the values file and what read it.
    assert "`agentic stamp --inspection <path>`" in rule
    assert "`agentic stamp --stop`" in rule
    # The marker `skills/settle/scripts/rules.py#markers` reads on the rule's
    # check line, whose carriers the loop below reads back from that reader.
    assert "check: stamp-drawn-once" in rule
    from conftest import rule_carriers

    held = rule_carriers("stamp-drawn-once")
    local = "Test_queue_for_written_inspection."
    for case in (
        local + "test_a_local_mode_cleared_inspection_queues_one_stamp",
        local + "test_a_local_mode_second_cleared_queues_nothing",
        local + "test_a_local_mode_inspection_off_its_branch_queues_nothing",
        local + "test_a_shared_mode_cleared_inspection_queues_one_stamp_at_its_write",
        local + "test_a_shared_mode_cleared_already_in_the_history_queues_nothing",
        "Test_main.test_inspection_queues_the_stamp_and_prints_the_line_naming_it",
        "Test_main.test_stop_draws_the_payloads_clone_once_and_exits_0",
        "Test_drawn_at_stop.test_accepts_the_main_sessions_stop_and_draws_once",
        "Test_drawn_at_stop.test_refuses_a_cwd_outside_the_clone_the_stamp_waits_in",
        "Test_main.test_the_plugins_stop_command_draws_once_and_exits_0",
    ):
        assert case in held, case
    # The command `agentic stamp --from <path>`, which the person types to draw
    # a stamp the hook could not.
    assert "names `agentic stamp --from <path>`" in unchecked
    # Round 2 of #1430, finding 1: the closing ` || exit 0` of the `Stop`
    # command, which a person reads to tell why the hook never keeps a turn
    # going.
    assert "` || exit 0`" in rule
    # The path of the dated record the measurement stands in, which a reader
    # opens for what was measured.
    assert "`docs/experiments/2026-11-06-" in unchecked


def test_the_policy_states_the_refusal_record_and_names_its_cases():
    """1792363231 S8. *The stamp* carries the refusal record as a rule of
    its own: a `cleared` refused because its
    audited commit is not on the branch leaves a record in the clone that
    refused it, and the earlier-run chain skips it, so the inspector's new
    audit draws the work item's one stamp. #1027 and #1376: it names the
    record's path, the one writer, `agentic stamp --inspection`, the matcher's
    floor, and `cleared_before`, which skips a recorded refusal as the chain
    does; and its `check:` line names the marker the cases that hold each
    carry. Its sentences are the proofer's to read."""
    text = flattened(section(read(*STAMP_DOC), STAMP_HEADING))
    rule = text.split(
        "**A `cleared` refused because its audited commit is not on the branch "
        "leaves a refusal record",
        1,
    )[1].split("**The stamp's `Stop` hook is the plugin's", 1)[0]
    for fact in (
        # The path of the refusal record, which a person opens or clears.
        "`<git-common-dir>/agentic-stamp-refused/<id>-<target>`",
        # The command that writes it, which the inspector runs.
        "`agentic stamp --inspection`",
        # The matcher's floor, the number of characters a row's commit is
        # written in at least.
        "seven",
        # The function that skips a recorded refusal, which a reader resolves
        # in `stamp.py`.
        "`cleared_before`",
    ):
        assert fact in rule, fact
    # The marker `skills/settle/scripts/rules.py#markers` reads on the rule's
    # check line, whose carriers the loop below reads back from that reader.
    assert "check: refused-cleared-leaves-a-record" in rule
    from conftest import rule_carriers

    held = rule_carriers("refused-cleared-leaves-a-record")
    local = "Test_queue_for_written_inspection."
    for case in (
        local + "test_a_refusal_record_skips_only_its_own_verdict",
        local
        + "test_a_local_mode_cleared_refused_off_its_branch_then_cleared_again_draws_once",
        local + "test_a_local_mode_inspection_off_its_branch_queues_nothing",
        local
        + "test_a_shared_mode_cleared_refused_then_committed_then_cleared_again_draws_once",
        "Test_cleared_before.test_skips_a_cleared_this_clone_recorded_refusing",
    ):
        assert case in held, case


# Each fact the section of either README edition names, which a user reads
# to learn what runs on their machine and what it leaves there.
README_FACTS = (
    # The file the hooks are registered in, which a user opens.
    "`hooks/hooks.json`",
    # The harness event of the first hook and the script it runs.
    "`SessionStart`",
    "`hooks/core-start.py`",
    # The harness event of the second hook and the command it runs.
    "`Stop`",
    "`stamp.py --stop`",
    # The harness event of the third hook and the script it runs.
    "`PreToolUse`",
    "`hooks/ask-under-automation.py`",
    # The harness event of the fourth hook and the script it runs.
    "`PostToolUse`",
    "`hooks/edit-leaves-copies.py`",
    # The one command shape the hooks run, as `hooks/hooks.json` spells it.
    '`python3 "<script>" || py -3 "<script>" || exit 0`',
    # The command that writes the stamp's values, and the two directories
    # the queue and a refusal leave under the git common dir.
    "`agentic stamp --inspection`",
    "`<git-common-dir>/agentic-stamp/`",
    "`<git-common-dir>/agentic-stamp-refused/`",
)


def test_both_readmes_say_what_the_stamp_hook_writes_and_leaves():
    """Round 1's yellow 4. The inventory a user reads to learn what runs on
    their machine did not list the `Stop` hook, in either edition. Since
    #1430 the plugin ships hooks again, since #1608 a `PreToolUse` one
    too, and since #1612 a `PostToolUse` one, so each edition names each of
    them, the files and commands they
    run, and the directories the queue leaves. The editions move together,
    so both are read, each in its section alone, since *Install* names the
    hooks too. What each edition says of them
    is the proofer's to read."""
    for edition, heading in (
        ("README.md", "## What runs on your machine"),
        ("README.ko.md", "## 내 컴퓨터에서 도는 것"),
    ):
        whole = read(edition)
        # The section's heading, which bounds what the facts are read in.
        assert heading in whole, (edition, heading)
        section = whole.split(heading, 1)[1].split("\n## ", 1)[0]
        text = flattened(section)
        for fact in README_FACTS:
            assert fact in text, (edition, fact)


# --- S16: the inspector is told it draws nothing --------------------------------


def test_the_inspector_queues_the_stamp_once_and_draws_none():
    """S16, the inspector's half (contract rule 14). `agents/inspector.md` said the
    drawing arrives as letters and to pass it through, which the 0.15.6 run
    did — every stamp behind `ctrl+o`. Since #969 the inspector runs no gate, so
    there is no line of the gate's for it to pass on. Since #975 the stamp is
    drawn in the orchestrator's session from the inspector's own `cleared`
    verdict, once per work item, and never from the orchestrator's run. Since
    #1376 the inspector queues it itself, with `agentic stamp --inspection`, names
    that write as its own, and carries the line it prints into its report.
    Since #1430 the plugin's `Stop` hook draws it. The definition names the
    command the inspector runs and not the one that draws by hand; how it says
    the rest is the proofer's to read."""
    text = flat("agents", "inspector.md")
    # The command the inspector runs once on the `inspection.md` it wrote.
    assert "`agentic stamp --inspection <path>`" in text
    # The command that draws a stamp by hand, which the inspector would run were
    # it written here: the inspector draws no stamp (`agents/inspector.md` *Never*,
    # its bullet on a stamp, and `docs/checks/the-stamp.md` *The stamp*, its
    # bold lead **The stamp is drawn once per work item, from the inspector's
    # `cleared`**).
    assert "agentic stamp --from" not in text, (
        "the inspector is told a command that draws a stamp, which it never does"
    )


# --- S13: the scale, retired (#853) -----------------------------------------


def test_the_stamp_draws_its_sample_and_neither_command_offers_a_scale():
    """S13 (#853). The disc has one size since #832, so `agentic stamp --shape`
    draws the sample with no scale to choose, and neither command's help
    names a scale. What the comment where the scale stood says is the
    proofer's to read."""
    mod = stamp_module()
    out = stamp("--shape")
    assert out.returncode == 0, out.stderr
    assert out.stdout == "\n" + "\n".join(mod.stamp(mod.SAMPLE_ROWS, True)) + "\n\n"
    for command in ([sys.executable, STAMP], [sys.executable, GATE]):
        help_text = subprocess.run(
            [*command, "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        ).stdout
        assert "scale" not in help_text, help_text
