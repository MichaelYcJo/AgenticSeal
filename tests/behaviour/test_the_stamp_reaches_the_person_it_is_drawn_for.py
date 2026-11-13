"""The broad gate's stamp reaches the person it is drawn for (#400).

Work item 1790562543. A sealer's stdout was a pipe into a report that arrived
folded behind `ctrl+o`, so a stamp drawn there was never seen. The stamp is
drawn from the sealer's `sealed` guarantee: the sealer's
`seal stamp --guarantee` queues its values under the git common dir (#1376),
and the plugin's `Stop` hook draws each undrawn file once, after the
orchestrator's turn's text (#1430).

This module holds the cases that read the documents, and the case that
holds both commands' `--help` to one fact.
`skills/verify/scripts/seal_stamp.py`'s own cases, the queue and the draw
among them, are `tests/skills/test_seal_stamp.py`.
"""

import os
import subprocess
import sys

from conftest import ROOT, flat, flattened, load_module, read

# No TARGET: its cases hold the stamp across docs/checks/the-stamp.md, two skills, agents/sealer.md and both READMEs, and hold seal_stamp.py's and broad_gate.py's --help to one fact.


STAMP = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")


def stamp_module():
    return load_module(STAMP, "agentic_seal_stamp_for_its_values")


def seal_stamp(*args):
    """`seal_stamp.py` as a person types it, stdout a pipe."""
    return subprocess.run(
        [sys.executable, STAMP, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )


def stamp_section():
    """`docs/checks/the-stamp.md` *The stamp*, flattened: the stamp's rules
    stand in a document of their own since #1312."""
    text = flat("docs", "checks", "the-stamp.md")
    return text.split("## The stamp ", 1)[1]


# --- S16: the rules are where they are read ----------------------------------


def test_the_orchestrator_is_given_the_stamps_commands_and_the_runs_lines():
    """S16, the orchestrator's half (contract rule 14), and #975 S13. The rule
    sits in the section that spawns the sealer and names the facts the
    orchestrator acts on: the command the sealer queues the stamp with, the
    lines the broad run opens with, which the orchestrator relays, and the
    command that stays the person's to type. When the stamp is drawn, that
    the orchestrator draws none, and what it does with the sealer's line are
    the proofer's to read."""
    text = flat("skills", "code-review", "orchestration.md")
    section = text.split(
        "## Orchestrator: the pull request opens once the sealer seals", 1
    )[1]
    section = section.split("## Orchestrator: verify before posting", 1)[0]
    for fact in (
        # The command the sealer queues the stamp with, whose line the
        # orchestrator meets in the sealer's hand-back.
        "`seal stamp --guarantee`",
        # The lines the broad run's stdout opens with, which the orchestrator
        # relays.
        "`BROAD GATE PASSED`",
        "`BROAD GATE FAILED`",
        # Round 1's yellow 1 of #400: the command a line names for the person
        # to type, which the orchestrator quotes and never runs.
        "`seal stamp --from`",
    ):
        assert fact in section, fact


def test_the_verify_skill_names_what_queues_the_stamp_and_what_draws_it():
    """S16, `verify`'s half, and #975 S13. The stamp is the sealer's, drawn
    once per work item from its `sealed` guarantee, and the gate draws
    nothing. #1376: queued by the sealer's `seal stamp --guarantee` under
    either root; #1430: drawn by the plugin's `Stop` hook. The skill names
    the command and the hook; its sentences are the proofer's to read."""
    text = flat("skills", "verify", "SKILL.md")
    for fact in (
        # The command the sealer queues the stamp's values with.
        "`seal stamp --guarantee`",
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
    names `seal stamp --from <path>` for where a file was written. The
    rule's trigger, its limits, its exit and the places nothing draws are
    the proofer's to read (1792363231 S7 and S8, #1027 and #1376); the
    command's closing ` || exit 0` is pinned. #1492: the measurement of
    2026-11-06 is cited from its `docs/experiments/` record."""
    text = stamp_section()
    screen = "**What the person's screen shows is not checked"
    rule, unchecked = text.split(screen, 1)
    # The command that queues the stamp, and the one that draws it, which a
    # person resolves to see what wrote the values file and what read it.
    assert "`seal stamp --guarantee <path>`" in rule
    assert "`seal stamp --stop`" in rule
    # The marker `.github/scripts/rules.py#markers` reads on the rule's check
    # line, whose carriers the loop below reads back from that reader.
    assert "check: stamp-drawn-once" in rule
    from conftest import rule_carriers

    held = rule_carriers("stamp-drawn-once")
    local = "Test_queue_for_written_guarantee."
    for case in (
        local + "test_a_local_mode_sealed_guarantee_queues_one_stamp",
        local + "test_a_local_mode_second_sealed_queues_nothing",
        local + "test_a_local_mode_guarantee_off_its_branch_queues_nothing",
        local + "test_a_shared_mode_sealed_guarantee_queues_one_stamp_at_its_write",
        local + "test_a_shared_mode_sealed_already_in_the_history_queues_nothing",
        "Test_main.test_guarantee_queues_the_stamp_and_prints_the_line_naming_it",
        "Test_main.test_stop_draws_the_payloads_clone_once_and_exits_0",
        "Test_drawn_at_stop.test_accepts_the_main_sessions_stop_and_draws_once",
        "Test_drawn_at_stop.test_refuses_a_cwd_outside_the_clone_the_stamp_waits_in",
        "Test_main.test_the_plugins_stop_command_draws_once_and_exits_0",
    ):
        assert case in held, case
    # The command `seal stamp --from <path>`, which the person types to draw
    # a stamp the hook could not.
    assert "names `seal stamp --from <path>`" in unchecked
    # Round 2 of #1430, finding 1: the closing ` || exit 0` of the `Stop`
    # command, which a person reads to tell why the hook never keeps a turn
    # going.
    assert "` || exit 0`" in rule
    # The path of the dated record the measurement stands in, which a reader
    # opens for what was measured.
    assert "`docs/experiments/2026-11-06-" in unchecked


def test_the_policy_states_the_refusal_record_and_names_its_cases():
    """1792363231 S8. *The stamp* carries the refusal record as a rule of
    its own: a `sealed` refused because its
    audited commit is not on the branch leaves a record in the clone that
    refused it, and the earlier-run chain skips it, so the sealer's new
    audit draws the work item's one stamp. #1027 and #1376: it names the
    record's path, the one writer, `seal stamp --guarantee`, the matcher's
    floor, and `sealed_before`, which skips a recorded refusal as the chain
    does; and its `check:` line names the marker the cases that hold each
    carry. Its sentences are the proofer's to read."""
    text = stamp_section()
    rule = text.split(
        "**A `sealed` refused because its audited commit is not on the branch "
        "leaves a refusal record",
        1,
    )[1].split("**The stamp's `Stop` hook is the plugin's", 1)[0]
    for fact in (
        # The path of the refusal record, which a person opens or clears.
        "`<git-common-dir>/agentic-stamp-refused/<id>-<target>`",
        # The command that writes it, which the sealer runs.
        "`seal stamp --guarantee`",
        # The matcher's floor, the number of characters a row's commit is
        # written in at least.
        "seven",
        # The function that skips a recorded refusal, which a reader resolves
        # in `seal_stamp.py`.
        "`sealed_before`",
    ):
        assert fact in rule, fact
    # The marker `.github/scripts/rules.py#markers` reads on the rule's check
    # line, whose carriers the loop below reads back from that reader.
    assert "check: refused-sealed-leaves-a-record" in rule
    from conftest import rule_carriers

    held = rule_carriers("refused-sealed-leaves-a-record")
    local = "Test_queue_for_written_guarantee."
    for case in (
        local + "test_a_refusal_record_skips_only_its_own_verdict",
        local
        + "test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once",
        local + "test_a_local_mode_guarantee_off_its_branch_queues_nothing",
        local
        + "test_a_shared_mode_seal_refused_then_committed_then_resealed_draws_once",
        "Test_sealed_before.test_skips_a_sealed_this_clone_recorded_refusing",
    ):
        assert case in held, case


# Each fact the section of either README edition names, which a user reads
# to learn what runs on their machine and what it leaves there.
README_FACTS = (
    # The file the two hooks are registered in, which a user opens.
    "`hooks/hooks.json`",
    # The harness event of the first hook and the script it runs.
    "`SessionStart`",
    "`hooks/core-start.py`",
    # The harness event of the second hook and the command it runs.
    "`Stop`",
    "`seal_stamp.py --stop`",
    # The one command shape both hooks run, as `hooks/hooks.json` spells it.
    '`python3 "<script>" || py -3 "<script>" || exit 0`',
    # The command that writes the stamp's values, and the two directories
    # the queue and a refusal leave under the git common dir.
    "`seal stamp --guarantee`",
    "`<git-common-dir>/agentic-stamp/`",
    "`<git-common-dir>/agentic-stamp-refused/`",
)


def test_both_readmes_say_what_the_stamp_hook_writes_and_leaves():
    """Round 1's yellow 4. The inventory a user reads to learn what runs on
    their machine did not list the `Stop` hook, in either edition. Since
    #1430 the plugin ships two hooks again, so each edition names both, the
    files and commands they run, and the directories the queue leaves. The
    editions move together, so both are read, each in its section alone,
    since *Install* names the two hooks too. What each edition says of them
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


# --- S16: the sealer is told it draws nothing --------------------------------


def test_the_sealer_queues_the_stamp_once_and_draws_none():
    """S16, the sealer's half (contract rule 14). `agents/sealer.md` said the
    drawing arrives as letters and to pass it through, which the 0.15.6 run
    did — every seal behind `ctrl+o`. Since #969 the sealer runs no gate, so
    there is no line of the gate's for it to pass on. Since #975 the stamp is
    drawn in the orchestrator's session from the sealer's own `sealed`
    verdict, once per work item, and never from the orchestrator's run. Since
    #1376 the sealer queues it itself, with `seal stamp --guarantee`, names
    that write as its own, and carries the line it prints into its report.
    Since #1430 the plugin's `Stop` hook draws it. The definition names the
    command the sealer runs and not the one that draws by hand; how it says
    the rest is the proofer's to read."""
    text = flat("agents", "sealer.md")
    # The command the sealer runs once on the `guarantee.md` it wrote.
    assert "`seal stamp --guarantee <path>`" in text
    # The command that draws a stamp by hand, which the sealer would run were
    # it written here: the sealer draws no stamp (`agents/sealer.md` *Never*,
    # its bullet on a stamp, and `docs/checks/the-stamp.md` *The stamp*, its
    # bold lead **The stamp is drawn once per work item, from the sealer's
    # `sealed`**).
    assert "seal stamp --from" not in text, (
        "the sealer is told a command that draws a stamp, which it never does"
    )


# --- S13: the scale, retired (#853) -----------------------------------------


def test_the_stamp_draws_its_sample_and_neither_command_offers_a_scale():
    """S13 (#853). The disc has one size since #832, so `seal stamp --shape`
    draws the sample with no scale to choose, and neither command's help
    names a scale. What the comment where the scale stood says is the
    proofer's to read."""
    mod = stamp_module()
    out = seal_stamp("--shape")
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
