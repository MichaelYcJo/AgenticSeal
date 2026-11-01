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


def test_the_orchestrator_writes_the_body_file_the_sealer_reads():
    """S8 of #943 and S12 of #1044, the orchestrator's half. The owner
    section names the commands that write the pull request body's file and
    send it, and the constant that marks where the copy of the records
    starts. Each is something the orchestrator types or opens, so each is
    held by its spelling; the order and the wording around them are the
    proofer's to read."""
    text = flat(*ORCH)
    pinned = [
        # The command the orchestrator types to open the pull request from
        # the body file.
        "`gh pr create --body-file <that file>`",
        # The command the orchestrator types to give an open pull request a
        # repaired body.
        "`gh api -X PATCH repos/<owner>/<repo>/pulls/<N> -F body=@<file>`",
        # The command the orchestrator types to write the body's copy of the
        # records, with the scratchpad path the sealer's spawn names.
        "`seal pr-body <item> --body <scratchpad>/<work-item-id>/pr-body.md`",
        # The citation the orchestrator resolves to find the line its own
        # part goes above.
        "`skills/code-review/scripts/pr_body.py#HEADING`",
    ]
    missing = [phrase for phrase in pinned if phrase not in text]
    assert missing == [], missing


def test_the_owner_names_the_dispatch_command():
    """S4 of #943 and #1058. The owner section names the run that pays for
    the other platforms before the pull request opens, as the command the
    orchestrator types; why that run sees what a `pull_request` run sees,
    and the limit left, are the proofer's to read."""
    text = flat(*ORCH)
    # The command the orchestrator types to dispatch the `tests` workflow on
    # its branch.
    assert "run `gh workflow run tests --ref <branch>`" in text


def test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge():
    """S7 of #945. A pull request GitHub cannot merge gets no merge ref and
    no `pull_request` CI, and nothing else says so, so the owner section
    reads `mergeable` before it waits on CI. #1200 adds `state` to the same
    read, before a push as well as after it, because a commit pushed to the
    branch of a merged pull request reaches no pull request, and the wait
    reads every workflow's checks rather than one workflow's run. A conflict
    is integrated by a merge, never a rebase, and the chain check reads no
    merge commit, so a resolution outside the records gets a verifying
    round. #1222 adds the poll before the wait, because the wait run before a
    check has reported exits 1 without waiting. Round 1 of #1222 counts the
    checks of `pull_request` runs alone, because a finished check of another
    event on the pushed commit ended the poll before the pull request's own
    checks were listed, and pins the poll's stop condition and its report."""
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
        "`no checks reported on the '<branch>' branch`",
        "exits 1 without waiting",
        "starts the wait only once the commit it pushed last has a check of a "
        "`pull_request` run.**",
        "Every ten seconds the orchestrator runs",
        "gh pr view <N> --json headRefOid --jq .headRefOid",
        "gh pr checks <N> --json event --jq "
        "'[.[] | select(.event == \"pull_request\")] | length'",
        "stops once the first prints the commit it pushed last and the second "
        "prints a count above 0",
        "the second command exits 1 while no check at all has reported",
        "The count reads the checks of GitHub Actions runs on `pull_request` alone",
        "within two minutes",
        "reads `gh pr view <N> --json state,mergeable` once more",
        "no check of a `pull_request` run reported on that commit and names the SHA",
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


def sentences(text):
    """`text`, flattened, cut after each full stop: the unit a pinned
    relation has to stand in together."""
    return re.split(r"(?<=\.)\s+", text)


@pytest.mark.rule("run-ends-with-verifying-round")
def test_a_close_that_does_not_hold_reopens_it():
    """S9 and S26 of work item 1791933022. A verifying round answers each
    closed finding on one of three line keywords, `confirms:`,
    `regression:` and `reopens:`, which `hooks/lib/fields.py` spells and the
    chain check reads. Every carrier that names the first two in one
    sentence names the third in it too, so no carrier hands the proofer a
    channel with a keyword missing. When a close reopens, and how the run
    ends, are the proofer's to read."""
    for carrier in (RECORD, PROOFER, SKILL, ORCH):
        both = [
            s
            for s in sentences(flat(*carrier))
            if "`confirms:`" in s and "`regression:`" in s
        ]
        # The two line keywords `hooks/lib/fields.py` spells, which the
        # proofer writes and the chain check reads.
        assert both, f"{'/'.join(carrier)} names the channel nowhere"
        for s in both:
            # The third line keyword of the same channel, `reopens:`, which
            # the proofer writes and the chain check reads.
            assert "`reopens:`" in s, (
                f"{'/'.join(carrier)} names the channel by `confirms:` and "
                f"`regression:` alone: {s}"
            )


JUDGMENTS = "`frame/plan.md` *Judgments of the run*"


def test_the_orchestrators_run_judgments_are_rows_of_the_plan():
    """#1167, *Scope* item 11. The cap, the second regression on one unit
    and a decision folded after the frame are judgments the orchestrator
    weighs, and each goes to one row of the plan's table, which the
    settle's dry run reads. Each place the orchestrator acts from cites
    that table, and the citation is what this reads; the signals the cap
    names are the proofer's to read. *The run* in the policy root changes
    at the settle, so this reads the two skill files the orchestrator acts
    from."""
    text = flat(*ORCH)
    run = text[
        text.index("## Orchestrator: the run ends with a verifying round") : (
            text.index(REGRESSION)
        )
    ]
    regression = text[
        text.index(REGRESSION) : text.index("## Orchestrator: the pull request opens")
    ]
    # The citation the orchestrator resolves to write a judgment at the cap.
    assert "as one row of " + JUDGMENTS in run, run
    row = regression[
        regression.index("| the unit already had a regression") : regression.index(
            "The framer's route:"
        )
    ]
    # The citation the orchestrator resolves to write a second regression's
    # route.
    assert JUDGMENTS in row, row
    # The citation the orchestrator resolves to write a decision folded into
    # the frame.
    assert JUDGMENTS in the_order(), "a folded decision's grounds have no home"
