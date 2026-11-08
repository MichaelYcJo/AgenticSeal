"""The broad gate's stamp reaches the person it is drawn for (#400).

Work item 1790562543. A sealer's stdout was a pipe into a report that arrived
folded behind `ctrl+o`, so a stamp drawn there was never seen. The stamp is
drawn from the sealer's `sealed` guarantee: the sealer's
`seal stamp --guarantee` queues its values under the git common dir (#1376),
and the plugin's `Stop` hook draws each undrawn file once, after the
orchestrator's turn's text (#1430).

This module holds the cases that read the documents, which are #923's.
`skills/verify/scripts/seal_stamp.py`'s own cases, the queue and the draw
among them, are `tests/skills/test_seal_stamp.py`.
"""

import os
import subprocess
import sys

from conftest import ROOT, flat, flattened, load_module, read

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
    stand in a document of their own since #1312, and `docs/running/the-broad-gate.md`
    keeps none of them."""
    text = flat("docs", "checks", "the-stamp.md")
    assert "## Where the stamp is drawn" not in flat(
        "docs", "running", "the-broad-gate.md"
    )
    return text.split("## The stamp ", 1)[1]


# --- S16: the rules are where they are read ----------------------------------


def test_the_orchestrator_is_told_the_stamp_is_drawn_for_it():
    """S16, the orchestrator's half (contract rule 14), and #975 S13. The rule
    sits in the section that spawns the sealer: the stamp is drawn at the end
    of the turn in which the sealer's report arrives, its
    `seal stamp --guarantee` having queued it under either root, the result
    text comes first, the orchestrator draws none — by `seal stamp` or by
    relaying a log, which 0.15.6 did — the broad run's lines are quoted as
    `BROAD GATE PASSED` and `BROAD GATE FAILED`, and no line of the run says
    `SEALED`. Since #1376 the line naming the values file arrives in the
    sealer's hand-back, and the orchestrator quotes it, leaving
    `seal stamp --from` to the person. 1792363231 S11: a commit of the
    guarantee refused for a row naming a commit the branch does not hold is
    answered by the sealer again at HEAD, never by an edit of the row. #1198
    made the row the newest verdict block."""
    text = flat("skills", "code-review", "orchestration.md")
    section = text.split(
        "## Orchestrator: the pull request opens once the sealer seals", 1
    )[1]
    section = section.split("## Orchestrator: verify before posting", 1)[0]
    for said in (
        "Where the guarantee's newest verdict block names a commit the branch "
        "does not hold, which the pull request's check refuses as stale, spawn "
        "the sealer again at HEAD and commit what it writes; never edit a block "
        "by hand.",
        "**The stamp is drawn for you at the end of the turn in which the "
        "sealer's report arrives, and you never draw one.**",
        "the sealer's `seal stamp --guarantee` queues the stamp's values, under "
        "either root, and the plugin's `Stop` hook draws them after your text. "
        "The line naming them arrives in the sealer's hand-back.",
        "The sealer's hand-back carries that line; quote it in the turn's text.",
        "Where the hand-back carries no such line, no stamp was queued and none "
        "is drawn",
        "The broad run draws nothing: its stdout opens `BROAD GATE PASSED` or "
        "`BROAD GATE FAILED`",
        "So put the result text first",
        "Draw none yourself, neither with `seal stamp` nor by relaying a log: a "
        "relayed log shows the person the stamp twice",
        "On a red run relay the `BROAD GATE FAILED` lines.",
        # Round 1's yellow 1 of #400: the command is named on the line that
        # points at a values file, and it stays the person's wherever it
        # appears.
        "Wherever a line you read names `seal stamp --from`, quote it as it "
        "stands: that command is the person's to type, and never yours.",
    ):
        assert said in section, said
    # #1376: no edit hook queues the stamp, and the queue has no session
    # directory. #1430: no launcher names a root that is gone.
    for gone in ("edit hook", "agentic-stamp/<session>/", "launcher"):
        assert gone not in section, gone
    assert "SEALED" not in section, "a line of the broad run is quoted as SEALED"


def test_the_form_bullet_says_what_draws_the_final_seal():
    """S16, `verify`'s half, and #975 S13. The **Form** bullet said
    `seal gate` draws the stamp when every check passed; the stamp is the
    sealer's now, drawn once per work item from its `sealed` guarantee, and
    the gate draws nothing. #1376: queued by the sealer's
    `seal stamp --guarantee` under either root; #1430: drawn by the plugin's
    `Stop` hook."""
    text = flat("skills", "verify", "SKILL.md")
    assert "`seal gate` prints the disc on success alone" not in text
    assert "`seal gate` draws the stamp" not in text
    assert "The edit hook" not in text
    for said in (
        "the stamp is drawn from the sealer's `guarantee.md` reading `sealed`, "
        "once per work item",
        "The sealer's `seal stamp --guarantee` writes the values it is drawn "
        "from, under either root, and the plugin's `Stop` hook draws them in "
        "the orchestrator's session",
        "The broad gate draws nothing",
    ):
        assert said in text, said


def test_the_policy_names_the_command_the_marker_and_the_command_to_draw():
    """S16, the policy's half, and #975 S10 and S13. `docs/checks/the-stamp.md`
    *The stamp* carries the drawing rule, names the command that queues the
    stamp, and ends in a `check:` line naming the marker the cases that
    queue and draw it carry; a second statement, on what the screen shows,
    names `seal stamp --from <path>` for where a file was written. The
    rule's trigger, its limits and the places nothing draws are the
    proofer's to read (1792363231 S7 and S8, #1027 and #1376)."""
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


def test_the_policy_states_the_refusal_record_and_names_its_cases():
    """1792363231 S8. *The stamp* carries the refusal record as a rule of
    its own: a `sealed` refused because its
    audited commit is not on the branch leaves a record in the clone that
    refused it, and the earlier-run chain skips it, so the sealer's new
    audit draws the work item's one stamp. #1027 and #1376: it names the one
    writer, `seal stamp --guarantee` under either root, the matcher's floor,
    and that `sealed_before` skips a recorded refusal as the chain does; it
    names none of the guards the removed `post-commit` record had; and its
    `check:` line names the marker the cases that hold each carry."""
    text = stamp_section()
    rule = text.split(
        "**A `sealed` refused because its audited commit is not on the branch "
        "leaves a refusal record",
        1,
    )[1].split("**The stamp's `Stop` hook is the plugin's", 1)[0]
    for said in (
        "`<git-common-dir>/agentic-stamp-refused/<id>-<target>`",
        "an earlier verdict block reading `sealed` that this clone recorded "
        "refusing is skipped",
        "One writer leaves it, for a row that stands in its own clone and "
        "nowhere else: `seal stamp --guarantee`, in either mode, where "
        "the `Branch` row's branch stands and does not hold the audited commit.",
        "In shared mode the pull request's check refuses the same row as stale",
        "at least seven characters",
        "`sealed_before` skips a `sealed` this clone recorded refusing",
    ):
        assert said in rule, said
    for gone in ("reflog", "patch-equivalent", "No ref of the clone", "must hold"):
        assert gone not in rule, gone
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


def test_both_readmes_say_what_the_stamp_hook_writes_and_leaves():
    """Round 1's yellow 4. The inventory a user reads to learn what runs on
    their machine did not list the `Stop` hook, in either edition. Since
    #1430 the plugin ships two hooks again, so each edition names both, the
    one command shape, that neither writes into the person's settings, the
    launcher of 0.33.0 to 0.34.1 as `/agentic:update`'s to name, and the side
    effects of the queue. The editions move together, so both are read.

    1792363231's round 1 finding 3: the side effects gained the refusal
    record's directory, and the count before them went stale, so the sentence
    carries no count. #975 S11: neither edition says the broad gate leaves
    the stamp's values. What each edition says is read in its section alone,
    since *Install* names the two hooks too; what is gone is read over the
    whole file."""

    for edition, heading, said, gone in (
        (
            "README.md",
            "## What runs on your machine",
            (
                "**The plugin ships two hooks, registered in `hooks/hooks.json`, "
                "and neither writes into your settings.**",
                "- **`SessionStart`**, at a session's start and again after "
                "`/clear` or a compaction, runs `hooks/core-start.py`.",
                "- **`Stop`**, at the end of each turn of the main session, runs "
                "`seal_stamp.py --stop`",
                'Each command is `python3 "<script>" || py -3 "<script>"`',
                "`/agentic:update` names both for you to take out by hand.",
                "These side effects are worth stating outright",
                # The clause's own words (round 2's white 2), so the bare
                # directory named elsewhere does not pass with it deleted.
                "the sealer's `seal stamp --guarantee`, run once on a "
                "`guarantee.md` reading `sealed`, writes the stamp's values under "
                "`<git-common-dir>/agentic-stamp/`, which the stamp's hook renames "
                "once drawn and nothing prunes",
                "a `sealed` refused because its audited commit is not on the work "
                "item's branch leaves an empty file under "
                "`<git-common-dir>/agentic-stamp-refused/`, in either mode, which "
                "nothing prunes either",
            ),
            (
                "| Gate |",
                "| sealer-stamp",
                "Four side effects",
                "the broad gate left for this session",
                "a sealed broad gate run writes",
                "written by the edit hook",
                "The plugin registers no hook",
                "seal stamp --install",
                "seal stamp --remove",
            ),
        ),
        (
            "README.ko.md",
            "## 내 컴퓨터에서 도는 것",
            (
                "**플러그인은 훅 두 개를 `hooks/hooks.json` 에 등록해 함께 "
                "내보내고, 어느 훅도 사용자 설정에 쓰지 않습니다.**",
                "- **`SessionStart`** 는 세션이 시작할 때, 그리고 `/clear` 나 "
                "압축(compaction) 뒤에 다시 `hooks/core-start.py` 를 돌립니다.",
                "- **`Stop`** 은 메인 세션의 턴이 끝날 때마다 "
                "`seal_stamp.py --stop` 을 돌립니다.",
                '두 명령은 모두 `python3 "<script>" || py -3 "<script>"` 꼴이고',
                "`/agentic:update` 가 이 둘을 알려 주면 사용자가 직접 지웁니다.",
                "다음 부수 효과는 밝혀 둡니다",
                "도장 훅은 그린 뒤 그 파일의 이름을 바꿀 뿐 지우지 않습니다",
                "감사한 커밋이 작업 항목 브랜치에 없어 거절된 `sealed` 는 어느 "
                "모드에서든 `<git-common-dir>/agentic-stamp-refused/` 아래에 빈 "
                "파일을 남깁니다.",
            ),
            (
                "| 게이트 |",
                "| sealer-stamp",
                "네 가지 부수 효과",
                "광역 관문 실행은 도장에 들어갈 값을",
                "편집 훅이 씁니다",
                "훅을 하나도 등록하지 않습니다",
                "seal stamp --install",
                "seal stamp --remove",
            ),
        ),
    ):
        whole = read(edition)
        assert heading in whole, (edition, heading)
        section = whole.split(heading, 1)[1].split("\n## ", 1)[0]
        text = flattened(section)
        for phrase in said:
            assert phrase in text, (edition, phrase)
        for phrase in gone:
            assert phrase not in flattened(whole), (edition, phrase)


# --- S16: the sealer is told it draws nothing --------------------------------


def test_the_sealer_queues_the_stamp_once_and_draws_none():
    """S16, the sealer's half (contract rule 14). `agents/sealer.md` said the
    drawing arrives as letters and to pass it through, which the 0.15.6 run
    did — every seal behind `ctrl+o`. Since #969 the sealer runs no gate, so
    there is no line of the gate's for it to pass on. Since #975 the stamp is
    drawn in the orchestrator's session from the sealer's own `sealed`
    verdict, once per work item, and never from the orchestrator's run. Since
    #1376 the sealer queues it itself, with `seal stamp --guarantee`, names
    that write as its own, and carries the line it prints into its report;
    the old instructions are gone. Since #1430 the plugin's `Stop` hook
    draws it."""
    text = flat("agents", "sealer.md")
    for said in (
        "Run `seal stamp --guarantee <path>` once, `<path>` being the "
        "`guarantee.md` you wrote.",
        "is your one write beside `guarantee.md` (rule 6), and you draw nothing: "
        "the plugin's `Stop` hook draws it.",
        "Its one line goes into your report as it printed it",
        "or draw a stamp",
        "you queue the stamp once from your `sealed` and draw nothing.",
    ):
        assert said in text, said
    # 1792363231 S9: a local-mode verdict is never committed.
    assert "your committed `sealed`" not in text
    assert "from its own run" not in text, "the stamp is not the run's"
    assert "seal stamp --from" not in text, (
        "the sealer is told to pass on a stamp command from a run it did not take"
    )
    assert "the drawing arrives as letters" not in text
    assert "pass it through as it came" not in text
    # Round 1's white 6: no gate draws in a sealer, so the `gate` row says
    # which copy measured the tree, not which drew the stamp.
    assert "which gate drew the stamp" not in text


# --- S13: the scale, retired (#853) -----------------------------------------


def test_the_stamp_says_why_it_has_no_scale_and_neither_command_offers_one():
    """S13 (#853). The comment where the scale stood says there is none and
    why — the disc has one size since #832 — so the next reader does not
    look for the dial; `seal stamp` with no argument draws the sample, and
    neither command's help names a scale."""
    mod = stamp_module()
    with open(STAMP, encoding="utf-8") as handle:
        source = " ".join(handle.read().replace("#", " ").split())
    assert "There is no scale ( 853)." in source, "the retirement is not said"
    assert "the disc is `DISC_CELLS` across whatever a scale said" in source
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
