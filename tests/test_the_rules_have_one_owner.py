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

import os

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RECORD = ("docs", "the-review-record.md")
SKILL = ("skills", "code-review", "SKILL.md")
# The orchestrator's half of the review skill (#265).
ORCH = ("skills", "code-review", "orchestration.md")
SMITH = ("agents", "smith.md")
WARDEN = ("agents", "warden.md")
IMPLEMENT = ("skills", "implement", "SKILL.md")
# The orchestrator's half of the implement skill (#292). The order a ticket
# runs in landed here in #351.
ORCH_IMPL = ("skills", "implement", "orchestration.md")
VERIFY = ("skills", "verify", "SKILL.md")
SEALER = ("agents", "sealer.md")
FRAMER = ("agents", "framer.md")
TRACKER = ("docs", "issues-and-milestones.md")
RECORD_LAYOUT = ("docs", "the-record-layout.md")
CONFIG_TEMPLATE = ("templates", "config.md")
CONFIG_SKILL = ("skills", "config", "SKILL.md")

ONE_SEAL_IS_FINAL = (
    "`skills/verify/SKILL.md` §*Every agent seals what it verified, and "
    "one of them is final* owns that rule"
)
BEFORE_ROUND_ONE = (
    "`skills/code-review/orchestration.md` §*Orchestrator: the pull request "
    "opens before round 1, and a phase is re-run* owns"
)
CRITERION_OWNER = (
    "`templates/config.md` §*Choosing a value — the criterion* owns the criterion"
)
FRAGMENT_OWNER = (
    "`docs/the-record-layout.md` §*A commit after the build brings its "
    "changelog fragment along* owns that rule"
)
RUN_OWNS_THE_RULE = "`docs/the-review-record.md` §*The run* owns that rule"


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return handle.read()


def flat(*parts):
    """The file as one line, so a pinned phrase survives re-wrapping."""
    return " ".join(read(*parts).split())


# rule → (owner, the sentence the owner states, {link carrier: how it names
# the owner}). A link is one sentence and names the owner's file or the
# owner's subsection; it does not restate the rule.
RULES = {
    "3 🟡 is a defect the release would ship": (
        SKILL,
        "a defect the release would ship",
        {},
    ),
    "6 the draft pull request opens before round 1": (
        ORCH,
        "The draft pull request opens at the end of the build, before round 1.",
        {ORCH_IMPL: f"the draft pull request opens ({BEFORE_ROUND_ONE} when)"},
    ),
    "7 a compacted session hands the next round to a fresh one": (
        ORCH,
        "A session that has compacted hands the next round to a fresh one, and "
        "the round record is the handoff.",
        {},
    ),
    "9 a hand-back's verification claim is a claim": (
        ORCH,
        "A hand-back's verification claim is a claim.",
        {},
    ),
    "10 every agent seals what it verified, and one seal is final": (
        VERIFY,
        "Every agent seals what it verified, and the one seal over the whole "
        "project is the sealer's.",
        {SEALER: ONE_SEAL_IS_FINAL, WARDEN: ONE_SEAL_IS_FINAL},
    ),
    # From #401: the `Broad gate` row is the one value only a person can
    # write, and the criterion for it is folded into one owner.
    "12 the criterion for choosing a Broad gate value": (
        CONFIG_TEMPLATE,
        "A check that is red repository-wide for reasons unrelated to any "
        "branch does not belong in the row",
        {CONFIG_SKILL: CRITERION_OWNER, ORCH_IMPL: CRITERION_OWNER},
    ),
    # From #493: filing a finding ran at 100% and acting on one at 47%, so a
    # new issue is a rung rather than the default.
    "14 a finding is filed where somebody will act": (
        RECORD,
        "A leftover finding takes the first rung that fits.",
        {
            SMITH: "`docs/the-review-record.md` §*The run* owns the ladder",
            TRACKER: "`docs/the-review-record.md` §*The run* owns where a filed "
            "finding goes",
        },
    ),
    # From #797: three of six 0.18.2 fragments shipped false because the
    # commits after the build changed behaviour.
    "15 a commit after the build brings its changelog fragment along": (
        RECORD_LAYOUT,
        "A commit after the build that changes what the work item ships "
        "updates the work item's `changelog.md` in the same range.",
        {SMITH: FRAGMENT_OWNER, IMPLEMENT: FRAGMENT_OWNER, ORCH: FRAGMENT_OWNER},
    ),
    # From #823, and since 0.22.0 one mark rather than a count of two
    # (`questions.md` Q1 of work item 1791933022).
    "16 a regression sends the work item back to its framer": (
        RECORD,
        "A regression stops the fix passes, at any round.",
        {FRAMER: RUN_OWNS_THE_RULE, IMPLEMENT: RUN_OWNS_THE_RULE},
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


def test_the_release_leg_is_no_longer_red_until_round_ones_record_commits():
    """#296 closed the window in which the `release` leg was red from the
    draft's opening until round 1's record committed.

    BOTH halves are asserted: the state prints on a draft rather than
    failing, and the record is still owed. Requiring only the first would go
    green over a document that had quietly turned the draft into a permanent
    exemption.
    """
    assert "That window used to be red and is not any more" in flat(*ORCH)
    assert "on a draft the missing record prints and the run exits 0" in flat(*ORCH)
    assert "Nothing that can reach `main` is exempt" in flat(*ORCH)


def test_the_order_opens_the_draft_between_the_build_and_the_rounds():
    """`skills/implement/orchestration.md` §*Orchestrator: the order inside a
    ticket* is what a session reads to know what comes after the smith; a
    pull request listed last there is the dozen-rounds-on-one-platform shape
    the owner's section measured."""
    text = flat(*ORCH_IMPL)
    step = text[text.index("2. spec · plan") : text.index("3. The pull request body")]
    assert "smith → the draft pull request opens (" in step
    # 1790815611 (#638) wrote the orchestrator's preflight in as the step
    # before the sealer's spawn, so the arrows carry it.
    assert (
        ") → warden rounds → `broad-gate --preflight`, yours → sealer → the pull "
        "request is marked ready." in step
    )
    assert step.index("the draft pull request opens") < step.index("warden rounds")


def test_the_order_no_longer_defers_the_framer_to_a_ticket():
    """Step 2 read `spec · plan (framer, once #84 exists; the session until
    then)` -- a step written before the agent it names, carrying its own
    escape clause for the interval, which closed when `agents/framer.md`
    landed."""
    step = flat(*ORCH_IMPL)
    step = step[step.index("2. spec · plan") : step.index("3. The pull request body")]
    assert "framer" in step, "step 2 stopped naming who draws the frame"
    for gone in ("once #84 exists", "the session until then"):
        assert gone not in step, (
            f"step 2 still carries `{gone}`. The framer ships, so the interval "
            "that clause covered is over and the escape reads as the rule"
        )


def test_a_regression_is_a_defect_a_fix_passs_own_commit_made():
    """The owner's ruling of 2026-10-16, on round 7 of work item 1791933022:
    a `regression:` line names a defect a fix pass's own commit introduced,
    and a defect in a unit a build phase made, which the framer designed and
    the owner approved, is an ordinary finding of new work, so its round
    gets its fix pass. The document states it, and the template and the
    warden, who write the line, say the same."""
    run = flat(*RECORD)
    run = run[run.index("## The run") : run.index("## The handoff")]
    assert "A regression is a defect a fix pass's own commit introduced." in run
    assert "is an ordinary finding of new work" in run
    for carrier in (RECORD, WARDEN, ("templates", "sdd-round.md")):
        text = flat(*carrier)
        assert "a fix pass's own commits added or changed" in text, (
            f"{'/'.join(carrier)} does not say a `regression:` line is for a "
            "unit a fix pass's own commits made"
        )
        assert "the fixes under review added or changed" not in text, (
            f"{'/'.join(carrier)} still gives a `regression:` line to any unit "
            "the reviewed commits made, a build phase's among them"
        )
