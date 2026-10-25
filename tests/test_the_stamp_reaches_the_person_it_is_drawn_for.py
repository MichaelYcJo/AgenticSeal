"""The broad gate's stamp reaches the person it is drawn for (#400).

Work item 1790562543. A sealer's stdout was a pipe into a report that arrived
folded behind `ctrl+o`, so a stamp drawn there was never seen. The stamp is
drawn from the sealer's `sealed` guarantee: the `post-edit` gate queues its
values under the git common dir at the guarantee's write, and a `Stop` hook
in the orchestrator's session draws each undrawn file once, after that
turn's text.

This module holds the cases that read the documents, which are #923's. The
hooks' own cases are `tests/test_sealer_stamp.py` and
`tests/test_sealer_stamp_queue.py`, written anew by #942's phase 6, and
`skills/verify/scripts/seal_stamp.py`'s are `tests/test_seal_stamp.py`.
"""

import os
import subprocess
import sys

from conftest import flat, load_module

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STAMP = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")


def stamp_module():
    return load_module(STAMP, "specseal_seal_stamp_for_its_values")


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
    """`docs/the-review-record.md` *The stamp*, flattened: the stamp's rules
    stand beside the verdict they are drawn from since #975, and
    `docs/the-broad-gate.md` keeps none of them."""
    text = flat("docs", "the-review-record.md")
    assert "## Where the stamp is drawn" not in flat("docs", "the-broad-gate.md")
    section = text.split("## The stamp ", 1)[1]
    assert text.index("## The guarantee") < text.index("## The stamp ")
    return section.split("## The run", 1)[0]


def test_the_policy_states_the_budget_and_names_its_case():
    """A18. `docs/the-review-record.md` *The stamp* carries the budget rule,
    and its `check:` line names this module; the paragraph nothing enforces
    follows it. #832
    and #853: the rule names the two rungs, with the disc and the text block
    alone, the owner's disc 28 cells across, and one real run to a message;
    the unchecked paragraph says nothing outside the disc is painted, so the
    stamp is read in the terminal's own theme, where it gave the parchment's
    contrast figures before decision 6 of work item 1791270164 retired the
    sheet. The section moved from `docs/the-broad-gate.md` with #975."""
    text = stamp_section()
    budget = "**The hook holds its whole message under a budget named in the code"
    screen = "**What the person's screen shows is not checked"
    unchecked = screen + text.split(screen, 1)[1]
    assert (
        "So is how the stamp reads on a light background as well as a dark one. "
        "Nothing outside the disc is painted, so its text is in the terminal's "
        "own colours and theme"
    ) in unchecked
    assert "1.02 and 1.48" not in unchecked and "parchment" not in unchecked
    rule = budget + text.split(budget, 1)[1].split(screen, 1)[0]
    assert "check: tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py" in rule
    # Round 1's yellow 1, under the owner's rule of 2026-10-02 (`questions.md` Q6).
    assert "A seal past what one message can carry stays pending" in rule
    assert "a character outside the BMP is two" in rule
    # #832 and #853: two rungs, with the disc and without it — and the reason
    # is the owner's 28-cell disc having one size, not a smaller disc refused.
    assert "A stamp has two rungs, with its disc and then without it" in rule
    assert (
        "the owner's disc is drawn 28 cells across and has one size, so there "
        "is no smaller disc to step to, and no scale either"
    ) in rule
    assert "0.90" not in rule and "at every scale" not in rule
    assert "one stamp of a real work item's size goes out per message" in rule
    assert "does not fit with its disc by itself is the only one drawn" in rule
    assert "as the text block with no disc" in rule
    assert "0.80 and 0.75" not in rule and "at 0.75 by itself" not in rule
    assert "24 cells" not in rule and "\N{SECTION SIGN} fragment" not in rule
    assert "14 cells" not in rule and "sheet" not in rule
    assert "The gate's own terminal drawing" not in rule, "the gate draws nothing"


# --- S16: the rules are where they are read ----------------------------------


def test_the_orchestrator_is_told_the_stamp_is_drawn_for_it():
    """S16, the orchestrator's half (contract rule 14), and #975 S13. The rule
    sits in the section that spawns the sealer: the stamp is drawn at the end
    of the turn in which the sealer's report arrives, its `Write` of a
    `sealed` guarantee having queued it under either root (#1027 S13), the
    result text comes first, the orchestrator draws none — by `seal-stamp` or
    by relaying a log, which 0.15.6 did — the broad run's lines are quoted as
    `BROAD GATE PASSED` and `BROAD GATE FAILED`, and no line of the run says
    `SEALED`. Round 1's finding 2 of 1792363231: the
    edit hook's line is shown to the person at the sealer's write and never
    reaches the orchestrator, so it is not told to quote that line; where no
    stamp appeared, it names the values file and leaves the command to the
    person. 1792363231 S11: a commit of the guarantee refused for a row
    naming a commit the branch does not hold is answered by the sealer again
    at HEAD, never by an edit of the row; red against 2759a60d's sealer
    step."""
    text = flat("skills", "code-review", "orchestration.md")
    section = text.split(
        "## Orchestrator: the pull request opens once the sealer seals", 1
    )[1]
    section = section.split("## Orchestrator: verify before posting", 1)[0]
    for said in (
        "Where the guarantee's row names a commit the branch does not hold, "
        "which the pull request's check refuses as stale, spawn the sealer "
        "again at HEAD and commit what it writes; never edit the row by hand.",
        "**The stamp is drawn for you at the end of the turn in which the "
        "sealer's report arrives, and you never draw one.**",
        "the sealer's own `Write` of it queues the stamp's values, under either "
        "root, and the `Stop` hook draws them after your text. The line naming "
        "them is the edit hook's message, shown to the person at that write. It "
        "is not in the sealer's report and does not reach you.",
        "The edit hook's line never reaches you. Where no stamp appeared, name "
        "the file under `<git-common-dir>/specseal-stamp/<session>/` whose name "
        "holds the work item's id, and leave `seal-stamp --from <that file>` to "
        "the person.",
        "The broad run draws nothing: its stdout opens `BROAD GATE PASSED` or "
        "`BROAD GATE FAILED`",
        "So put the result text first",
        "Draw none yourself, neither with `seal-stamp` nor by relaying a log: a "
        "relayed log shows the person the stamp twice",
        "On a red run relay the `BROAD GATE FAILED` lines.",
        # Round 1's yellow 1 of #400: the command is named on the line that
        # points at a values file, and it stays the person's wherever it
        # appears.
        "Wherever a line you read names `seal-stamp --from`, quote it as it "
        "stands: that command is the person's to type, and never yours.",
    ):
        assert said in section, said
    assert "the edit hook's message names" not in section, (
        "the orchestrator is told to quote a line it never receives"
    )
    assert "SEALED" not in section, "a line of the broad run is quoted as SEALED"


def test_the_form_bullet_says_what_draws_the_final_seal():
    """S16, `verify`'s half, and #975 S13. The **Form** bullet said
    `broad-gate` draws the stamp when every check passed; the stamp is the
    sealer's now, drawn once per work item from its `sealed` guarantee, and
    the gate draws nothing. #1027 S13: queued at that file's write under
    either root."""
    text = flat("skills", "verify", "SKILL.md")
    assert "`broad-gate` prints the disc on success alone" not in text
    assert "`broad-gate` draws the stamp" not in text
    for said in (
        "the stamp is drawn from the sealer's `guarantee.md` reading `sealed`, "
        "once per work item",
        "The edit hook writes the values it is drawn from at the file's write, "
        "under either root, and the `Stop` hook draws them",
        "the `Stop` hook draws them in the orchestrator's session",
        "The broad gate draws nothing",
    ):
        assert said in text, said


def test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does():
    """S16, the policy's half, and #975 S10 and S13. `docs/the-review-record.md`
    *The stamp* carries the drawing rule with a `check:` line naming the marker the cases that queue and draw it
    carry, and a second statement saying what the screen shows has no case.
    That statement names every place the hook is silent — a foreign hooks
    slot, a `python3` that cannot load `seal_stamp.py`, a main session
    outside the clone, a plugin older than the hook — and `seal-stamp --from
    <path>` for where a file was written.

    1792363231 S7 and S8: the rule names both triggers, the commit in shared
    mode and the write in local mode, with the local facts that hold once
    per work item. The unchecked paragraph no longer names local mode among
    the silences, and no longer hands the never-twice gap to an issue: it
    names a local guarantee that arrived other than by `Write` or `Edit`, a
    local verdict whose branch cannot be read, and the limits the commit
    gate leaves (`spec.md` *Scope*), the coincidence `plan.md`'s path walk
    found among them, and none of `post-commit`'s removed guards. Red
    against the paragraph at 769f2aa4, and against 2759a60d's, which still
    named the guards."""
    text = stamp_section()
    screen = "**What the person's screen shows is not checked"
    rule, unchecked = text.split(screen, 1)
    unchecked = screen + unchecked
    assert (
        "**The stamp is drawn once per work item, from the sealer's `sealed`, at "
        "the end of the turn in which `guarantee.md` came to read it: at its "
        "commit in shared mode, and at its write in local mode.**"
    ) in rule
    for local in (
        "`hooks/sealer-stamp-queue.py`",
        "after each `Write` or `Edit` of "
        "`<git-common-dir>/seal/specs/<id>/guarantee.md`",
        "an ancestor of the branch the work item's `routing.md` names in its "
        "`Branch` row",
        "the root and the values directory share the common dir",
        "`settle` retires no local-mode work item",
    ):
        assert local in rule, local
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
        "Test_main.test_accepts_a_shared_mode_sealed_guarantee_at_its_write",
        "Test_main.test_accepts_a_local_mode_sealed_guarantee",
        "Test_main.test_accepts_a_subagents_write_for_the_main_session",
        "Test_main.test_refuses_any_other_edit_before_it_loads_seal_stamp",
        "Test_main.test_accepts_the_main_sessions_stop_and_draws_once",
    ):
        assert case in held, case
    # #975 round 6's finding 1: the double-stamp limit is stated where the
    # rule is, as the class `sealed_before` cannot see, with its reason.
    assert "draws the stamp again in that clone" in rule, (
        "the double-stamp limit is stated where the rule is"
    )
    assert "the history is the only record the rule reads" in rule, (
        "the limit says why it is one"
    )
    # #975 round 7's finding 1: the limit names the clone it holds in. The
    # clone that drew the stamp keeps its values file, and an amend there
    # queues nothing (`test_a_recommit_of_the_same_guarantee_queues_no_second_file`).
    assert "in a clone that holds no values file for the work item" in rule, (
        "the limit names the clone it holds in"
    )
    # 1792363231 round 2's finding 2: the class no longer names the copy from
    # a commit no ref holds, which writes no record now. Round 3's finding
    # 1: it names any copy onto a copy of the declared branch, whatever made
    # it, and that the refusal's own way on draws the second stamp. The
    # history reader skips nothing; only the chain skips a recorded refusal.
    assert (
        "A `sealed` that drew in another clone, brought onto a copy of its "
        "declared branch that does not hold its audited commit, by hand or by "
        "`checkout`, `cherry-pick -n` or `merge --squash`, is refused at its "
        "commit and recorded, and the new audit the refusal asks for draws "
        "again there; it joins that class."
    ) in rule
    assert "no ref of that clone holds" not in rule
    assert "copied here by hand" not in text
    assert "the earlier-run chain alone skips a `sealed` this clone recorded" in rule
    assert "**What the person's screen shows is not checked" in unchecked
    assert "No case, hook or workflow can observe a screen." in unchecked
    assert "check: none reader: the owner on the first real run" in unchecked
    # Round 1's yellow 1 of #400: the hook's silence where it cannot draw is
    # stated where a person looks for why no stamp appeared, with the way to
    # draw it.
    assert "**Nor is the hook's silence where it cannot draw.**" in unchecked
    for silence in (
        "where git's hooks slot is somebody else's",
        "by a shell write or `seal import`",
        "names no branch, or a branch the clone no longer holds",
        "committed past the commit gate",
        "a clone no session has reached",
        "never the `; earlier run:` chain",
        "a values directory emptied by hand",
        "by coincidence, the very commit a copy of the item on another branch "
        "was sealed and drawn over",
        # Round 3's findings 1 and 3 of work item 1792363231.
        "brought onto a copy of its declared branch that does not hold its "
        "audited commit",
        "where an amend folded the guarantee into the very commit it audited",
        "a commit that concludes a conflicted merge bringing in a side's "
        "`sealed` is refused",
        "cannot load `seal_stamp.py`",
        "outside the clone the stamp was queued in",
        "predates the hook",
    ):
        assert silence in unchecked, silence
    for guard in (
        "reflog",
        "patch-equivalent",
        "in a clone other than the one that refused",
        "brought from another branch of the clone",
    ):
        assert guard not in unchecked, guard
    assert "names `seal-stamp --from <path>`" in unchecked
    assert (
        "In local mode the line reaches the person as the edit hook's message, "
        "and nobody has watched that message on a screen yet."
    ) in unchecked
    for gone in (
        # Spelled in two pieces, so S8's `git grep` for the pointer finds the
        # policy clean and not this check on it.
        "#" + "976",
        "in local mode, where the `seal/` root sits under the git directory",
        "already read `sealed` and that verdict drew nothing",
    ):
        assert gone not in text, gone
    assert "`SEALED` line" not in text, "the gate's line is quoted as SEALED"
    assert "the stamp says which copy drew it" not in text


def test_the_policy_states_the_refusal_record_and_names_its_cases():
    """1792363231 S8. *The stamp* carries the refusal record as a rule of
    its own: a `sealed` refused because its
    audited commit is not on the branch leaves a record in the clone that
    refused it, and the earlier-run chain skips it, so the sealer's new
    audit draws the work item's one stamp. It names the two writers, the
    commit gate in shared mode and the local writer in local mode, the
    matcher's floor, and that `sealed_before` and `post-commit` ask and
    write no record; it names none of the guards `post-commit`'s record
    had; and its `check:` line names the marker the cases that hold each
    carry. Red at
    1e956838, whose paragraph described `post-commit`'s record and its
    four facts."""
    text = stamp_section()
    rule = text.split(
        "**A `sealed` refused because its audited commit is not on the branch "
        "leaves a refusal record",
        1,
    )[1].split("**The hook holds its whole message under a budget", 1)[0]
    for said in (
        "`<git-common-dir>/specseal-stamp-refused/<id>-<target>`",
        "`; earlier run: <sha> sealed`",
        "In shared mode the commit gate writes it when it refuses the commit "
        "of that row",
        "In local mode the local writer writes it where the `Branch` row's "
        "branch stands",
        "at least seven characters",
        "`sealed_before` asks no record",
        "`post-commit` writes none",
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


def test_both_readmes_list_the_stamp_hook():
    """Round 1's yellow 4. The hook inventory a user reads to learn what runs
    on their machine did not list the `Stop` hook, in either edition: the gate
    table, the opt-in list, the count of gates that wake on a condition, and
    the side effects. The editions move together, so both are read.

    1792363231 S7: the gate that queues a local-mode stamp at the write has its own
    row, and the count and the opt-in list that row made false say twelve
    gates and two stamp hooks. Its round 1's finding 3: the side effects
    gained the refusal record's directory, and the count before them went
    stale, so the sentence carries no count."""
    for edition, count, opt_in, effects, clause in (
        (
            "README.md",
            "Nine of the twelve gates",
            # The opt-in list's own words: the count sentence names the stamp
            # hooks too, so the bare name would pass with the list unchanged.
            "the two implementer hooks, the two stamp hooks and the version check.",
            "These side effects are worth stating outright",
            # The clause's own words (round 2's white 2): the gate-table row
            # carries `specseal-stamp/` too, so the bare directory passed
            # with the side effect deleted.
            "`<git-common-dir>/specseal-stamp/`, which the stamp hook renames "
            "once drawn and nothing prunes",
        ),
        (
            "README.ko.md",
            "게이트 열둘 중 아홉",
            "구현자 훅 둘, 도장 훅 둘, 버전 확인이다.",
            "다음 부수 효과는 밝혀 둡니다",
            "도장 훅은 그린 뒤 그 파일의 이름을 바꿀 뿐 지우지 않습니다",
        ),
    ):
        text = flat(edition)
        for gate in ("sealer-stamp", "sealer-stamp-queue"):
            table = [ln for ln in text.split("| ") if ln.startswith(f"{gate} ")]
            assert table, f"{edition}'s gate table has no `{gate}` row"
        assert count in text, (edition, count)
        assert opt_in in text, (edition, opt_in)
        assert effects in text and clause in text, (edition, effects, clause)
        for gone in (
            "Seven of the ten",
            "게이트 열 중 일곱",
            "Eight of the eleven",
            "Four side effects",
            "네 가지 부수 효과",
        ):
            assert gone not in text, (edition, gone)
        assert "게이트 열하나 중 여덟" not in text, edition
    # #975 S11: both editions say where the stamp's values are written, and
    # neither says the broad gate leaves them. #1027 S13: at the write of a
    # sealed guarantee under either root; and the refusal record's directory
    # stands beside the values' among the side effects, written by the edit
    # hook in either mode.
    for edition, said, gone in (
        (
            "README.md",
            (
                "queued at the write of a work item's `guarantee.md` reading "
                "`sealed` (the next row), once per work item",
                "the write of a `guarantee.md` reading `sealed` writes the stamp's "
                "values under",
                "a `sealed` refused because its audited commit is not on the work "
                "item's branch leaves an empty file under "
                "`<git-common-dir>/specseal-stamp-refused/`, written by the edit "
                "hook in either mode, which nothing prunes",
            ),
            (
                "the broad gate left for this session",
                "a sealed broad-gate run writes",
                "a `sealed` the plugin refused leaves",
                # #1027 phase 7: the git hooks' row went with the hooks.
                "Beside the arms, `pre-commit` refuses",
            ),
        ),
        (
            "README.ko.md",
            (
                "작업 항목의 `guarantee.md` 가 `sealed` 로 쓰일 때 남는",
                "`sealed` 로 읽히는 `guarantee.md` 를 쓸 때 도장에 들어갈 값을",
                "감사한 커밋이 작업 항목 브랜치에 없어 거절된 `sealed` 는 "
                "`<git-common-dir>/specseal-stamp-refused/` 아래에 빈 파일을 "
                "남깁니다. 어느 모드에서든 편집 훅이 씁니다.",
            ),
            (
                "광역 관문이 이 세션 앞으로",
                "광역 관문 실행은 도장에 들어갈 값을",
                "플러그인이 거절한 `sealed`",
                "팔과 별도로, `pre-commit` 은",
            ),
        ),
    ):
        text = flat(edition)
        for phrase in said:
            assert phrase in text, (edition, phrase)
        for phrase in gone:
            assert phrase not in text, (edition, phrase)


# --- S16: the sealer is told it draws nothing --------------------------------


def test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it():
    """S16, the sealer's half (contract rule 14). `agents/sealer.md` said the
    drawing arrives as letters and to pass it through, which the 0.15.6 run
    did — every seal behind `ctrl+o`. Since #969 the sealer runs no gate, so
    there is no line of the gate's for it to pass on: it says it draws no
    stamp. Since #975 the stamp is drawn in the orchestrator's session from
    the sealer's own committed `sealed` verdict, once per work item, and
    never from the orchestrator's run; the old instructions are gone."""
    text = flat("agents", "sealer.md")
    for said in (
        "or draw a stamp",
        "a stamp is drawn once from your `sealed`.",
    ):
        assert said in text, said
    # 1792363231 S9: a local-mode verdict is never committed.
    assert "your committed `sealed`" not in text
    assert "from its own run" not in text, "the stamp is not the run's"
    assert "seal-stamp --from" not in text, (
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
    look for the dial; `seal-stamp` with no argument draws the sample, and
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
