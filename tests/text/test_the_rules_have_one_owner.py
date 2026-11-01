"""Each review-chain rule has one carrier that states it, and every other
carrier links to that one in a sentence that names it.

A rule stated in eight places is eight places to disagree: #161's count rule
reached eight carriers, and rounds 7, 8 and 9 corrected them three at a time.
The table below holds each rule's owner, the sentence the owner states, and
the sentence each linking carrier names the owner with.

0.22.0 (#923) replaced the three record documents with
`docs/the-review-record.md`; the rules that left with their mechanism left
this table, and the ones that stayed name their owner there.
"""

import re

import pytest
from conftest import flat

RECORD = ("docs", "the-review-record.md")
SKILL = ("skills", "code-review", "SKILL.md")
# The orchestrator's half of the review skill (#265).
ORCH = ("skills", "code-review", "orchestration.md")
PROOFER = ("agents", "proofer.md")
IMPLEMENT = ("skills", "implement", "SKILL.md")
# The orchestrator's half of the implement skill (#292). The order a ticket
# runs in landed here in #351.
ORCH_IMPL = ("skills", "implement", "orchestration.md")
# The bootstrap, which proposes the `Broad gate` row, in its own file since
# #1046.
BOOTSTRAP = ("skills", "implement", "bootstrap.md")
VERIFY = ("skills", "verify", "SKILL.md")
SEALER = ("agents", "sealer.md")
FRAMER = ("agents", "framer.md")
TRACKER = ("docs", "issues-and-milestones.md")
RECORD_LAYOUT = ("docs", "the-record-layout.md")
CONFIG_TEMPLATE = ("templates", "setup", "config.md")
CONFIG_SKILL = ("skills", "config", "SKILL.md")
ROUND_TEMPLATE = ("templates", "records", "sdd-round.md")

ONE_SEAL_IS_FINAL = (
    "`skills/verify/SKILL.md` *The hand-back's labels carry the claims, and "
    "the one seal is the sealer's* owns that rule"
)
AFTER_THE_SEAL = (
    "`skills/code-review/orchestration.md` *Orchestrator: the pull request "
    "opens once the sealer seals* owns"
)
CONTRIBUTING = ("CONTRIBUTING.md",)
CRITERION_OWNER = "`templates/setup/config.md` *The criterion for choosing a value* owns the criterion"
FRAGMENT_OWNER = (
    "`docs/the-record-layout.md` *A commit after the build brings its "
    "changelog fragment along* owns that rule"
)
RUN_OWNS_THE_RULE = "`docs/the-review-record.md` *The run* owns that rule"


# rule → (owner, the sentence the owner states, {link carrier: how it names
# the owner}). A link is one sentence and names the owner's file or the
# owner's subsection; it does not restate the rule.
RULES = {
    "3 🟡 is a defect the release would ship": (
        SKILL,
        "a defect the release would ship",
        {},
    ),
    # #943: a pull request opened before round 1 ran the suite on three
    # platforms at every push of every round, and its Ready press once more.
    "6 the pull request opens once the sealer has sealed": (
        ORCH,
        "The pull request opens ready, once the sealer has sealed, and CI runs then.",
        {
            ORCH_IMPL: f"the pull request opens ({AFTER_THE_SEAL} when)",
            CONTRIBUTING: f"{AFTER_THE_SEAL} the order a maintainer's run follows",
        },
    ),
    "7 a compacted session hands the next round to a fresh one": (
        ORCH,
        "A session that has compacted hands the next round to a fresh one, and "
        "the round record is the handoff.",
        {},
    ),
    # Since #967 an agent's hand-back carries its claims under the three
    # labels and no agent but the sealer takes a seal.
    "10 the hand-back's labels carry the claims, and one seal is the sealer's": (
        VERIFY,
        "The hand-back's labels carry the claims, and the one seal over the "
        "whole project is the sealer's `guarantee.md`.",
        {SEALER: ONE_SEAL_IS_FINAL},
    ),
    # From #401: the `Broad gate` row is the one value only a person can
    # write, and the criterion for it is folded into one owner.
    "12 the criterion for choosing a Broad gate value": (
        CONFIG_TEMPLATE,
        "A check that is red repository-wide for reasons unrelated to any "
        "branch does not belong in the row",
        {CONFIG_SKILL: CRITERION_OWNER, BOOTSTRAP: CRITERION_OWNER},
    ),
    # From #493: filing a finding ran at 100% and acting on one at 47%, so a
    # new issue is a rung rather than the default.
    "14 a finding is filed where somebody will act": (
        RECORD,
        "A leftover finding goes where somebody will act on it, and the "
        "orchestrator writes why there.",
        # The crafter's copy of the ladder left with #967. Filing is the
        # orchestrator's act (the ladder's own `check:` line says so), and a
        # crafter hands a leftover back with its answerer (its step 10).
        {
            TRACKER: "`docs/the-review-record.md` *The run* owns where a filed "
            "finding goes",
        },
    ),
    # From #797: three of six 0.18.2 fragments shipped false because the
    # commits after the build changed behaviour.
    "15 a commit after the build brings its changelog fragment along": (
        RECORD_LAYOUT,
        "A commit after the build that changes what the work item ships "
        "updates the work item's `changelog.md` in the same range.",
        {IMPLEMENT: FRAGMENT_OWNER, ORCH: FRAGMENT_OWNER},
    ),
    # From #823, and since 0.22.0 one mark rather than a count of two
    # (`questions.md` Q1 of work item 1791933022), routed by the comparison
    # of the fix with the frame (the owner, 2026-10-16, on round 8).
    "16 a regression is routed by comparing the fix with the frame": (
        RECORD,
        "A regression is routed by comparing the fix with the frame.",
        {FRAMER: RUN_OWNS_THE_RULE, IMPLEMENT: RUN_OWNS_THE_RULE},
    ),
    # #945, S5: one crafter resumed across phases read 941,799 tokens in one
    # turn, so a phase is a fresh spawn and a fix pass resumes only below
    # the largest context a fresh crafter reached in the 0.22.0 run.
    "17 each phase is a fresh crafter": (
        ORCH,
        "Each phase of a work item is built by a fresh `crafter` spawn, and the "
        "orchestrator never resumes a crafter across a phase boundary.",
        {},
    ),
    "18 a fix pass resumes the implementer only below the threshold": (
        ORCH,
        "A fix pass resumes the implementer only while the implementer's "
        "largest per-turn context is below 806,241 tokens, and is a fresh "
        "`crafter` spawn otherwise.",
        {},
    ),
    # #1041: in #955 and #1016 the orchestrator's fix-pass prompts left every
    # `verdict:` line to the orchestrator, which rewrote them in a commit of
    # its own, so a round with fixes cost three record commits. #1198 made
    # the two lines one close block.
    "19 the orchestrator writes no close block of a finding a fix pass answers": (
        ORCH,
        "The orchestrator writes no close block of a finding the fix pass "
        "answers, and its fix-pass prompt leaves every such block to the "
        "crafter.",
        {},
    ),
    # #1041, the owner's answer of 2026-10-28: issue #1041 *Done when*
    # bullet 1 gives the commit of the fix pass's two lines to the
    # orchestrator, which makes it before the verifying round reads them.
    "20 the orchestrator commits the round record the fix pass left": (
        ORCH,
        "On the hand-back the orchestrator commits the round record as the fix "
        "pass left it, in one commit for the whole pass, before it spawns the "
        "verifying round, and changes none of its lines.",
        {},
    ),
}


@pytest.mark.parametrize("rule", sorted(RULES))
def test_the_owner_states_the_rule(rule):
    owner, sentence, _ = RULES[rule]
    assert sentence in flat(*owner), (
        f"{'/'.join(owner)} no longer states rule {rule!r}, and it is the one "
        "carrier that does"
    )


@pytest.mark.parametrize("rule", sorted(r for r in RULES if RULES[r][2]))
def test_every_link_names_the_owner(rule):
    owner, _, links = RULES[rule]
    for carrier, names_the_owner in links.items():
        assert carrier != owner, f"{rule!r}: the owner is listed as its own link"
        assert names_the_owner in flat(*carrier), (
            f"{'/'.join(carrier)} carries rule {rule!r} without naming "
            f"{'/'.join(owner)} as its owner, which is a second statement of "
            "the rule rather than a link to the one that owns it"
        )


FIX_PASS = "## Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer"


def test_the_fix_pass_reads_the_implementers_context_before_it_resumes():
    """S5 of #945. Rules 17 and 18 pin the two bold sentences; this pins
    what lets an orchestrator act on them: what a fresh crafter is handed, the
    command that reads the implementer's context, where the threshold came
    from, and the old rule gone."""
    text = flat(*ORCH)
    section = text[text.index(FIX_PASS) : text.index("## Orchestrator: the run ends")]
    for said in (
        "the phase records the earlier phases wrote",
        "`seal cost --segments <the implementer's agent-*.jsonl>`",
        "the largest value of its `context` column",
        "hands it the round record and the phase records",
        "the largest context a fresh, never-resumed crafter reached in the 0.22.0 run",
        # #1041, S1: the fix pass writes its closes last, after the sweep's
        # corrections, and commits none, since the orchestrator commits them
        # (rule 20); a doubt goes to the next round rather than into a
        # rewrite of the block. #1198 made the two lines one close block.
        "Last, the fix pass appends the close block of every finding it "
        "answered, after its fix commits and those corrections",
        "and leaves the round record uncommitted",
        "That commit holds `trail/rounds/round-N.md` alone.",
        "A close the orchestrator doubts goes into the verifying round's spawn prompt",
        "the orchestrator does not rewrite the block",
        "it edits nothing else in the record",
    ):
        assert said in section, f"the fix-pass section no longer says {said!r}"
    assert "the fix pass commits the two lines" not in section, (
        "the fix-pass section still has the fix pass commit its own two lines, "
        "which the owner gave to the orchestrator on 2026-10-28"
    )
    assert "Orchestrator: a fix pass resumes the implementer" not in text
    assert "never spawn a fresh one while that session still exists" not in text


REGRESSION = "### A regression is routed by comparing the fix with the frame"


def test_the_framers_route_closes_each_finding_with_a_close_block_in_one_commit():
    """S2 of #1041, under #1198. On the framer's route no fix pass runs, so
    the orchestrator closes every open finding itself; row *The record*
    names the close block's `answer:` beside `deferred the frame`, and one
    commit for every block."""
    text = flat(*ORCH)
    section = text[
        text.index(REGRESSION) : text.index("## Orchestrator: the pull request opens")
    ]
    row = section[section.index("| The record |") : section.index("| The framer |")]
    for said in (
        "you append a close block to every open finding",
        "its `verdict:` reading `deferred the frame`",
        "its `answer:` naming the regression that sent the work item back",
        "commit every such block in one commit",
    ):
        assert said in row, (
            f"row *The record* of the framer's route no longer says {said!r}"
        )


def test_a_draft_is_tolerated_and_still_owes_the_record():
    """#943 stopped telling an orchestrator to open a draft, and did not
    refuse a repository whose people still open one.

    BOTH halves are asserted: a draft is not refused, and the record is
    still owed once it is marked ready. Requiring only the first would go
    green over a document that had quietly turned the draft into a permanent
    exemption.
    """
    assert "A repository that still opens a draft is not refused." in flat(*ORCH)
    assert (
        "`ready_for_review` event re-runs it when the draft is marked ready, "
        "so the record is still owed then"
    ) in flat(*ORCH)
    assert "Nothing that can reach `main` is exempt" in flat(*ORCH)


def test_the_orchestrator_writes_the_body_file_the_sealer_reads():
    """S8 of #943, the orchestrator's half. `agents/sealer.md` reads the pull
    request body from a file the spawn prompt names, because no pull request
    exists when the sealer runs. The owner section writes that file, names it
    in the spawn, opens the pull request with it, and gives a repaired body to
    a pull request already open on the stated limit's path. Round 1 of #943
    reverted each of the first three and this module stayed green.

    S12 of #1044: `seal pr-body` writes the body's copy of the records, so
    the orchestrator runs it after `trail/gate.md` is committed, which that
    copy includes, writes its own part above the heading (#1148) and
    restates no record there, and runs it again before every later sealer
    spawn and every `PATCH` of the body, which is every repair's last step."""
    text = flat(*ORCH)
    pinned = [
        "the issue and the file holding the pull request body",
        "`gh pr create --body-file <that file>`",
        "`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`",
        "write the pull request body after `trail/gate.md` is committed",
        "`seal pr-body <item> --body <scratchpad>/<work-item-id>/pr-body.md`",
        "`skills/code-review/scripts/pr_body.py#HEADING`",
        "Then write your own part above that line, from the top of the file",
        "Your part restates no record",
        "before every later spawn of the sealer and before every "
        "`gh api -X PATCH` of the body",
    ]
    missing = [phrase for phrase in pinned if phrase not in text]
    assert missing == [], missing
    assert "once you have written the pull request body to a file" not in text
    gate = flat("docs", "the-broad-gate.md")
    assert "before the pull request opens" in gate
    assert "before a pull request is marked ready" not in gate


def test_a_run_that_stops_before_the_pull_request_pushes_nothing():
    """Round 1 of #943, finding 2. `Destination | stop before the pull
    request` hands the branch back committed and unpushed, and the review
    chain still runs under it, so both of the owner section's pushes are
    conditioned on the destination."""
    text = flat(*ORCH)
    assert (
        "Where `Destination` reads `open the pull request`, push the branch"
    ) in text
    assert (
        "Under `stop before the pull request` nothing is pushed, and the "
        "branch is handed back committed and unpushed."
    ) in text
    assert (
        "Under `stop before the pull request` push nothing: name the "
        "platform risk in the hand-back"
    ) in text


def test_the_owner_states_the_dispatch_step_and_the_limit():
    """S4 of #943. Opening the pull request after the sealer moves the other
    platforms to the end, so the owner section says how a platform-specific
    change pays for them earlier, and states what is left: a defect only one
    platform shows is met at the pull request and takes the repair path.
    #1058: the step names the run it reads, why that run's cases see what a
    `pull_request` run's cases see, and what it cannot have."""
    text = flat(*ORCH)
    assert "run `gh workflow run tests --ref <branch>`" in text
    assert (
        "That run is a `workflow_dispatch` run of `tests`. Its cases see what "
        "a `pull_request` run's cases see, because `tests/conftest.py` removes "
        "every `GITHUB_` variable at import. It cannot have a pull request's "
        "merge commit, or the `hygiene` workflow, which starts only on a "
        "`pull_request` event."
    ) in text
    assert (
        "**The stated limit: a defect that only one platform shows, in work "
        "nobody expected to be platform-specific, is found when the pull "
        "request opens, after the sealer.**"
    ) in text


def test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge():
    """S7 of #945. A pull request GitHub cannot merge gets no merge ref and
    no `pull_request` CI, and nothing else says so, so the owner section
    reads `mergeable` before it waits on CI. #1200 adds `state` to the same
    read, before a push as well as after it, because a commit pushed to the
    branch of a merged pull request reaches no pull request, and the wait
    reads every workflow's checks rather than one workflow's run. A conflict
    is integrated by a merge, never a rebase, and the chain check reads no
    merge commit, so a resolution outside the records gets a verifying
    round."""
    text = flat(*ORCH)
    section = text[
        text.index("## Orchestrator: the pull request opens once the sealer seals") : (
            text.index("## Orchestrator: verify before posting")
        )
    ]
    for said in (
        "reads `gh pr view <N> --json state,mergeable` when the pull request "
        "opens, before each push to its branch and after each push",
        "`MERGED` or `CLOSED` stops the push",
        "`gh pr checks <N> --watch`",
        "`CONFLICTING` means GitHub made no merge ref for the pull request and "
        "runs no `pull_request` CI on it, and nothing else says so",
        "`UNKNOWN` means GitHub has not computed the answer yet",
        "A conflict with the base is integrated by merging the base into the "
        "branch, never by a rebase.",
        "after the branch whose changes conflict with this one has landed",
        "the orchestrator spawns a verifying round on that resolution",
        "`--no-merges`",
    ):
        assert said in section, f"the owner section no longer says {said!r}"


# Where step 2 of the order inside a ticket opens.
STEP_2 = "2. The framer writes `frame/design.md`, `plan.md` and `questions.md`."


def test_the_order_opens_the_pull_request_after_the_sealer():
    """`skills/implement/orchestration.md` *Orchestrator: the order inside a
    ticket* is what a session reads to know what comes after the crafter. #943
    moved the pull request from between the build and the rounds to after
    the sealer, so no step of the order opens, keeps or readies a draft."""
    text = flat(*ORCH_IMPL)
    step = text[text.index(STEP_2) : text.index("3. The pull request body")]
    # 1790815611 (#638) wrote the orchestrator's preflight in as the step
    # before the sealer's spawn, and #969 the broad run after it: the sealer
    # reads the run's record, so the run comes before the spawn. Since #940
    # the step says it in words rather than arrows. #1044 put the body's
    # copy of the records between the run and the spawn, since it copies
    # the run's record and the sealer checks it.
    assert (
        "spawns the crafter (*The frame is read against the issue at the "
        "spawn* below). The "
        "proofer's rounds follow, then `seal gate --preflight` and `seal gate "
        "--record`, both run by the orchestrator, then `seal pr-body`, which "
        "the orchestrator runs to write the pull request body's copy of the "
        "records, then the sealer, and then the pull request opens (" in step
    ), step
    assert "draft" not in step, step


def test_the_order_no_longer_defers_the_framer_to_a_ticket():
    """Step 2 read `spec · plan (framer, once #84 exists; the session until
    then)` -- a step written before the agent it names, carrying its own
    escape clause for the interval, which closed when `agents/framer.md`
    landed."""
    step = flat(*ORCH_IMPL)
    step = step[step.index(STEP_2) : step.index("3. The pull request body")]
    assert "framer" in step, "step 2 stopped naming who draws the frame"
    for gone in ("once #84 exists", "the session until then"):
        assert gone not in step, (
            f"step 2 still carries `{gone}`. The framer ships, so the interval "
            "that clause covered is over and the escape reads as the rule"
        )


def test_the_acts_table_says_no_commit_holds_who_wrote_the_close_block():
    """#1041, the owner's answer of 2026-10-28: the fix pass commits neither
    line, so the row's `Grounds` cell cannot send a reader to the history
    for who wrote them. The table is `skills/implement/acts.md`'s since
    #1148, and the two lines are one close block since #1198."""
    text = flat("skills", "implement", "acts.md")
    start = text.index(
        "| Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer |"
    )
    row = text[
        start : text.index(
            "| Orchestrator: the run ends with a verifying round |", start
        )
    ]
    assert "is in no commit, because the fix pass commits no close block" in row
    assert "`verdict:` and `answer:` lines" not in row
    assert (
        "whether that commit changed them are in the round record's history" not in row
    )


def the_order():
    """`skills/implement/orchestration.md` *Orchestrator: the order inside a
    ticket*, flattened, up to the subsection under it."""
    text = flat(*ORCH_IMPL)
    return text[
        text.index("## Orchestrator: the order inside a ticket") : text.index(
            "### The frame is read against the issue at the spawn"
        )
    ]


def test_a_decision_after_the_frame_is_folded_into_it():
    """S9 of #945. A crafter reads the frame and not the issue's comments, so
    a decision made after the frame is committed is folded into it before
    the next crafter spawns, and before framing into the issue body."""
    order = the_order()
    for said in (
        "A decision made after the frame is committed is folded, in place, into "
        "`frame/design.md` or `plan.md` before the next crafter spawns.",
        "naming the comments to fold",
        "the orchestrator keeps one line of its own in `plan.md`",
        "naming the comments to fold, below the title,",
        "folds the decision into the issue body",
    ):
        assert said in order, f"the order no longer says {said!r}"


def test_a_handoff_file_is_written_only_to_move_the_work():
    """S9 of #945. Where a work item stands is in the records it already
    has, so a `handoff.md` lives only as long as a move between sessions."""
    order = the_order()
    for said in (
        "Where a work item stands is read from `plan.md`'s Status column, "
        "`gaps.md` and the phase records.",
        "a `handoff.md` in the work item's directory only to move the work to "
        "another session or another machine",
        "The orchestrator that hands the work over writes",
        "The orchestrator that takes the work over deletes it once",
    ):
        assert said in order, f"the order no longer says {said!r}"


def test_a_recurring_problem_gets_a_prevention_home():
    """S9 of #945. A problem met twice in one run gets the place that
    prevents it before the next spawn, and the issue records where."""
    order = the_order()
    for said in (
        "A problem that recurs within a run gets a prevention home at once.",
        "a mechanism that stops it, or a rule written into the file the "
        "recurring act is read from",
        "The work item in progress builds that home.",
        "records the home in a comment on the issue of the work item in progress",
    ):
        assert said in order, f"the order no longer says {said!r}"


def test_a_regression_is_a_defect_a_fix_passs_own_commit_made():
    """The owner's ruling of 2026-10-16, on round 7 of work item 1791933022:
    a `regression:` line names a defect a fix pass's own commit introduced,
    and a defect in a unit a build phase made, which the framer designed and
    the owner approved, is an ordinary finding of new work, so its round
    gets its fix pass. The document states it, and the proofer, who writes
    the line, says the same."""
    run = flat(*RECORD)
    run = run[run.index("## The run") : run.index("## The handoff")]
    assert "A regression is a defect a fix pass's own commit introduced." in run
    assert "is an ordinary finding of new work" in run
    for carrier in (RECORD, PROOFER):
        text = flat(*carrier)
        assert "a fix pass's own commits added or changed" in text, (
            f"{'/'.join(carrier)} does not say a `regression:` line is for a "
            "unit a fix pass's own commits made"
        )
        assert "the fixes under review added or changed" not in text, (
            f"{'/'.join(carrier)} still gives a `regression:` line to any unit "
            "the reviewed commits made, a build phase's among them"
        )
        # Round 9 of 1791933022, finding 1: every `fixed` commit touches its
        # finding's path, so a fix that did not hold has usually changed the
        # unit its defect still stands in. The unit alone gave that finding
        # both lines; the defect's origin decides it.
        assert "those commits introduced" in text, (
            f"{'/'.join(carrier)} gives a `regression:` line to a unit a fix "
            "pass changed without asking whether its commits made the defect"
        )
        assert "left the defect standing" in text, (
            f"{'/'.join(carrier)} does not say a `fixed` commit that left the "
            "defect standing in the unit it changed takes `reopens:`"
        )


def sentences(text):
    """`text`, flattened, cut after each full stop: the unit a pinned
    relation has to stand in together."""
    return re.split(r"(?<=\.)\s+", text)


def the_run():
    text = flat(*RECORD)
    return text[text.index("## The run") : text.index("## The handoff")]


@pytest.mark.rule("run-ends-with-verifying-round")
def test_a_close_that_does_not_hold_reopens_it():
    """The owner's decision of 2026-10-16, on round 8 of work item
    1791933022 (S9, S26): a close that does not hold where no fix pass's
    commit made the defect is raised again on a `reopens:` line, as an
    ordinary finding that gets its fix pass. *The run* says so; every
    carrier that names the channel's `confirms:` and `regression:` lines in
    one sentence names `reopens:` in it too; and the orchestration's
    verifying-round section ends the run only where the check does."""
    reopened = [
        s for s in sentences(the_run()) if "`reopens:`" in s and "does not hold" in s
    ]
    assert reopened, "*The run* does not say a close that does not hold reopens"
    assert any(
        "where no fix pass's commit made the defect" in s
        and "gets its fix pass" in s
        and "framer" not in s
        for s in reopened
    ), reopened
    for carrier in (RECORD, PROOFER, SKILL, ORCH):
        both = [
            s
            for s in sentences(flat(*carrier))
            if "`confirms:`" in s and "`regression:`" in s
        ]
        assert both, f"{'/'.join(carrier)} names the channel nowhere"
        for s in both:
            assert "`reopens:`" in s, (
                f"{'/'.join(carrier)} names the channel by `confirms:` and "
                f"`regression:` alone: {s}"
            )
    orch = flat(*ORCH)
    verifying = orch[
        orch.index("So a run ends with a **verifying round**") : orch.index(
            "### A regression"
        )
    ]
    assert "the run ends at that round" not in verifying
    # #1148: a `fixed` finding located in the work item's records alone,
    # whose commit touched them alone, is read by the sealer at HEAD, and the
    # check passes it in the last record.
    # #1198: a finding with no close block is open, and `open` is no verdict.
    assert (
        "run ends only on a round whose record holds no finding without a "
        "close block, no `rejected` one, and no `fixed` one that names a path "
        "outside the work item's records or whose commit touched one" in verifying
    ), "the verifying-round section no longer says where the run ends"
    # Round 9 of 1791933022, finding 3: the check holds a second condition on
    # the same record, so a run ended on the first alone is refused.
    assert (
        "and whose `target:` commit is HEAD, or is followed only by the work "
        "item's own records" in verifying
    ), "the verifying-round section ends the run on one of the check's two conditions"


@pytest.mark.rule("run-ends-with-verifying-round")
def test_a_fix_pass_to_the_records_alone_owes_no_verifying_round():
    """S4 of #1148. `chain_check.py#records` passes a `fixed` of the last
    record located in the work item's records alone whose commit touched
    them alone, so the orchestration that spawns the verifying round says
    the same: such a fix pass owes none, its reader is the sealer, a
    finding located in code owes the round whatever its fix touched, and
    the round's *When* says the same exception (round 1 of #1148, finding
    1)."""
    orch = flat(*ORCH)
    opening = orch[
        orch.index("## Orchestrator: the run ends with a verifying round") : orch.index(
            "So a run ends with a **verifying round**"
        )
    ]
    assert (
        "except a fix pass whose findings are all located in the work item's "
        "own records and whose commits touched only those records" in opening
    ), opening
    assert "the sealer reads every record at HEAD and is that fix's reader" in opening
    assert "the pass owes no verifying round" in opening, opening
    assert (
        "A finding located in code is read by a round whatever its fix touched"
        in opening
    ), opening
    assert (
        "**after the fixes** for the previous round are committed, never "
        "before, or it reviews what has already been reviewed; a fix pass "
        "whose findings are all located in the work item's records, with "
        "commits that touched nothing else, owes none" in orch
    ), "the verifying round's When row does not state the records-only exception"


COMPARISON = ("what the frame says", "what the fix did", "where the defect came from")


def test_a_regression_is_routed_by_comparing_the_fix_with_the_frame():
    """The owner's refinement of 2026-10-16, on round 8 of work item
    1791933022 (S27): a `regression:` line does not send the work item to
    its framer by itself. One sentence of the finding's grounds compares the
    fix with the frame, and the round is routed on it: to the framer where
    the fix built what the frame says, to a fix pass where it departed or
    the defect came from how it was written, and to the framer for a second
    regression on the same unit after a fix-pass route."""
    run = the_run()
    assert "**A regression is routed by comparing the fix with the frame.**" in run
    for carrier in (RECORD, PROOFER, ORCH):
        assert any(
            all(part in s for part in COMPARISON) for s in sentences(flat(*carrier))
        ), f"{'/'.join(carrier)} does not name the comparison in one sentence"
    for route in (
        "Where the fix built what the frame says and the defect is still there",
        "the work item goes back to its framer",
        "Where the fix departed from the frame, or the defect came from how the "
        "fix was written",
        "a paste-ready fix taken from a review record among them",
        "gets an ordinary fix pass",
        "A second regression on the same unit after a fix-pass route is the "
        "signal that the frame is wrong whatever the sentence reads",
    ):
        assert route in run, f"*The run* no longer says {route!r}"
    assert "### A regression is routed by comparing the fix with the frame" in flat(
        *ORCH
    )
    for carrier in (RECORD, ROUND_TEMPLATE, ORCH, PROOFER, FRAMER):
        text = flat(*carrier)
        for gone in (
            "A round carrying a `regression:` line gets no fix pass",
            "A round carrying one gets no fix pass",
            "no fix pass is commissioned",
            "the fix passes stop",
            "A regression stops the fix passes",
            "A regression sends the work item back to its framer",
        ):
            assert gone not in text, (
                f"{'/'.join(carrier)} still routes on the `regression:` line "
                f"alone: {gone!r}"
            )


def test_the_cap_counts_from_the_last_design_change():
    """The owner's decision of 2026-10-16, on round 9 of work item
    1791933022, finding 2: the round cap counts from the last design change,
    a reframe or a new phase the owner approved, so the first review of new
    work starts a fresh count; a regression routed to a fix pass is followed
    by one verifying round whatever the count; and the loop guard stands.
    The extension rule stopped extending at any round carrying a regression,
    which left both routes a regression now takes with no round to go on to
    past round 3; #1167 replaced the extension with the orchestrator's
    judgment, settled into *The run* in 0.27.1's settle."""
    run = the_run()
    for said in (
        "counted from the last design change",
        "a reframe, or a new phase the owner approved in `frame/plan.md`",
        "starts the count again",
        "followed by one verifying round whatever the count",
    ):
        assert said in run, f"*The run* no longer says {said!r}"
    assert (
        "A second regression on the same unit after a fix-pass route is the "
        "signal that the frame is wrong" in run
    ), "*The run* lost the loop guard"
    for carrier in (ORCH, ("README.md",)):
        assert "counted from the last design change" in flat(*carrier), (
            f"{'/'.join(carrier)} caps rounds without saying where the count starts"
        )
    assert "마지막 설계 변경" in flat("README.ko.md"), (
        "README.ko.md caps rounds without saying where the count starts"
    )
    assert "the record that stopped the run" not in flat(*FRAMER), (
        "agents/framer.md still reads a regression's round as the end of the run"
    )


JUDGMENTS = "`frame/plan.md` *Judgments of the run*"


def test_the_orchestrators_run_judgments_are_rows_of_the_plan():
    """#1167, *Scope* item 11. The cap, the second regression on one unit
    and a decision folded after the frame are judgments the orchestrator
    weighs, and each goes to one row of the plan's table, which the
    settle's dry run reads; the extension line the proofer wrote from the
    spawn prompt, which no round record ever carried, goes, and so does the
    route taken whatever the comparison says. *The run* in the policy root
    changes at the settle, so this reads the two skill files the
    orchestrator acts from."""
    text = flat(*ORCH)
    run = text[
        text.index("## Orchestrator: the run ends with a verifying round") : (
            text.index(REGRESSION)
        )
    ]
    regression = text[
        text.index(REGRESSION) : text.index("## Orchestrator: the pull request opens")
    ]
    assert "as one row of " + JUDGMENTS in run, run
    for signal in ("as many findings as the one before it", "a `regression:` line"):
        assert signal in run, f"the cap no longer names the signal {signal!r}"
    assert "the extension line" not in run, run
    assert "extends one round at a time" not in run, run
    row = regression[
        regression.index("| the unit already had a regression") : regression.index(
            "The framer's route:"
        )
    ]
    assert JUDGMENTS in row, row
    assert "whatever the sentence says" not in row, row
    assert JUDGMENTS in the_order(), "a folded decision's grounds have no home"
    fix_pass = text[
        text.index("**The fix pass then finds") : text.index("**You type only the half")
    ]
    assert (
        "names a statement of a rule it reworded that stands in the work "
        "item's frame" in fix_pass
    ), fix_pass
