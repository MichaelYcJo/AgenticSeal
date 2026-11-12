"""Each review-chain rule has one carrier that states it, and every other
carrier links to that one in a sentence that names it.

A rule stated in eight places is eight places to disagree: #161's count rule
reached eight carriers, and rounds 7, 8 and 9 corrected them three at a time.
The table below holds each rule's owner, the facts the owner states that a
reader acts on, and the citation each linking carrier names the owner by.
Whether the owner's sentences state the rule, and whether a carrier restates
it around its link, are the proofer's to read.

0.22.0 (#923) replaced the three record documents with one, which #1312 cut
by reader; the rules that left with their mechanism left this table, and the
ones that stayed name their owner in `docs/running/the-run.md`.
"""

import re

import pytest
from conftest import flat

# No TARGET: its cases hold each review-chain rule's owner across the skills, the definitions and the documents that carry it.

RECORD = ("docs", "running", "the-run.md")
SKILL = ("skills", "code-review", "SKILL.md")
# The orchestrator's half of the review skill (#265).
ORCH = ("skills", "code-review", "orchestration.md")
PROOFER = ("agents", "proofer.md")
IMPLEMENT = ("skills", "implement", "SKILL.md")
# The fix pass's procedure, cut from `IMPLEMENT` *5.* and `agents/crafter.md`
# in #1471.
FIX_PASS_PROCEDURE = ("skills", "implement", "fix-pass.md")
# The orchestrator's half of the implement skill (#292). The order a ticket
# runs in landed here in #351.
ORCH_IMPL = ("skills", "implement", "orchestration.md")
# The bootstrap, which proposes the `Broad gate` key, in its own file since
# #1046.
BOOTSTRAP = ("skills", "implement", "bootstrap.md")
VERIFY = ("skills", "verify", "SKILL.md")
SEALER = ("agents", "sealer.md")
FRAMER = ("agents", "framer.md")
# The framer's fold and reframe, cut from `agents/framer.md` in #1473 so a
# first frame does not preload it; the definition names it in one sentence.
FOLD = ("skills", "implement", "fold-and-reframe.md")
TRACKER = ("docs", "releasing", "issues-and-milestones.md")
CORE = ("skills", "core", "SKILL.md")
PR_CHECK = ("docs", "checks", "the-pull-request-check.md")
RECORD_LAYOUT = ("docs", "layout", "the-record-layout.md")
CONFIG_TEMPLATE = ("templates", "setup", "config.md")
CONFIG_SKILL = ("skills", "config", "SKILL.md")

# Each link is the owner's path and section, the citation a reader of the
# linking carrier resolves; the sentence around it is the proofer's to read.
ONE_SEAL_IS_FINAL = (
    "`skills/verify/SKILL.md` *The hand-back's labels carry the claims, and "
    "the one seal is the sealer's*"
)
AFTER_THE_SEAL = (
    "`skills/code-review/orchestration.md` *Orchestrator: the pull request "
    "opens once the sealer seals*"
)
CONTRIBUTING = ("CONTRIBUTING.md",)
CRITERION_OWNER = "`templates/setup/config.md` *The criterion for choosing a value*"
FRAGMENT_OWNER = (
    "`docs/layout/the-record-layout.md` *A commit after the build brings its "
    "changelog fragment along*"
)
RUN_OWNS_THE_RULE = "`docs/running/the-run.md` *The run*"
EARLIER_ROUNDS = "`skills/code-review/SKILL.md` *Earlier rounds*"
THE_CORES_ROW = (
    "the row *No fix that no round reads* of `skills/core/SKILL.md` "
    "*Judgment is not licence to skip a party*"
)
CONVENTION = ("skills", "commit-pr-convention", "SKILL.md")
OUTSIDE_THE_REVIEW = ("skills", "writing-style", "outside-the-review.md")


# rule -> (owner, the facts the owner states, {link carrier: the citation it
# names the owner by}). A fact is a spelling, a path or a number a reader of
# the owner acts on; the rule's words are the proofer's to read.
RULES = {
    # #943: a pull request opened before round 1 ran the suite on three
    # platforms at every push of every round, and its Ready press once more.
    "6 the pull request opens once the sealer has sealed": (
        ORCH,
        (),
        {ORCH_IMPL: AFTER_THE_SEAL, CONTRIBUTING: AFTER_THE_SEAL},
    ),
    # Since #967 an agent's hand-back carries its claims under the three
    # labels and no agent but the sealer takes a seal.
    "10 the hand-back's labels carry the claims, and one seal is the sealer's": (
        VERIFY,
        (
            # The file the sealer writes its seal into, which the chain
            # check's guarantee arm reads.
            "`guarantee.md`",
        ),
        {SEALER: ONE_SEAL_IS_FINAL},
    ),
    # From #401: the `Broad gate` key is the one value only a person can
    # write, and the criterion for it is folded into one owner.
    "12 the criterion for choosing a Broad gate value": (
        CONFIG_TEMPLATE,
        (),
        {CONFIG_SKILL: CRITERION_OWNER, BOOTSTRAP: CRITERION_OWNER},
    ),
    # From #493: filing a finding ran at 100% and acting on one at 47%, so a
    # new issue is a rung rather than the default.
    "14 a finding is filed where somebody will act": (
        RECORD,
        (),
        # The crafter's copy of the ladder left with #967. Filing is the
        # orchestrator's act, and a crafter hands a leftover back with its
        # answerer (its step 10).
        {TRACKER: RUN_OWNS_THE_RULE},
    ),
    # From #797: three of six 0.18.2 fragments shipped false because the
    # commits after the build changed behaviour.
    "15 a commit after the build brings its changelog fragment along": (
        RECORD_LAYOUT,
        (
            # The fragment's file name, which a commit after the build
            # updates and the release reads.
            "`changelog.md`",
        ),
        {FIX_PASS_PROCEDURE: FRAGMENT_OWNER, ORCH: FRAGMENT_OWNER},
    ),
    # From #823, and since 0.22.0 one mark rather than a count of two
    # (`questions.md` Q1 of work item 1791933022), routed by the comparison
    # of the fix with the frame (the owner, 2026-10-16, on round 8).
    "16 a regression is routed by comparing the fix with the frame": (
        RECORD,
        (),
        {FOLD: RUN_OWNS_THE_RULE, IMPLEMENT: RUN_OWNS_THE_RULE},
    ),
    # #945, S5: one crafter resumed across phases read 941,799 tokens in one
    # turn, so a fix pass resumes only below the largest context a fresh
    # crafter reached in the 0.22.0 run.
    "18 a fix pass resumes the implementer only below the threshold": (
        ORCH,
        (
            # The per-turn context, in tokens, the orchestrator compares the
            # implementer's `context` column with.
            "806,241",
        ),
        {},
    ),
    # #1476: four files each said what the three lines mean, and #161's
    # rounds corrected such copies a few at a time. The review skill, which
    # the proofer opens at step 1, defines them, and the other three name
    # that section.
    "21 a closed finding is answered on one of three lines": (
        SKILL,
        (
            # The two close verdicts a fix pass writes, which the chain check
            # reads.
            "`fixed <commit>`",
            "`rejected`",
            # The three line keywords `lib/fields.py` spells, which the
            # proofer writes and the chain check reads.
            "`confirms:`",
            "`regression:`",
            "`reopens:`",
        ),
        {PROOFER: EARLIER_ROUNDS, RECORD: EARLIER_ROUNDS, ORCH: EARLIER_ROUNDS},
    ),
    # #1476: five files each gave the condition on which a fix owes no
    # verifying round, and the core's row gave one half of it. The row
    # states both halves, as the check holds them, and each other file names
    # the row.
    "22 a change after the last round is read by a round, or by the sealer": (
        CORE,
        (),
        {
            RECORD: THE_CORES_ROW,
            ORCH: THE_CORES_ROW,
            PR_CHECK: THE_CORES_ROW,
            ORCH_IMPL: THE_CORES_ROW,
        },
    ),
    # #1478: four findings and one withheld verdict of 0.37.0 named a
    # changelog sentence a second time at its quote in `pr.md`. `seal
    # pr-body` writes the fragment above the fold, so `pr.md` quotes none of
    # it, and the files that said what `pr.md` holds name the owner.
    "23 pr.md quotes no sentence of changelog.md": (
        ORCH,
        (
            # The two records the rule is about, by the names the orchestrator
            # writes them under.
            "`pr.md`",
            "`changelog.md`",
            # The command that writes the fragment into the body, and the
            # constant that holds the line it writes it under.
            "`seal pr-body`",
            "`skills/code-review/scripts/pr_body.py#HEADING`",
        ),
        {
            CONVENTION: AFTER_THE_SEAL,
            IMPLEMENT: AFTER_THE_SEAL,
            CONFIG_TEMPLATE: AFTER_THE_SEAL,
            OUTSIDE_THE_REVIEW: AFTER_THE_SEAL,
        },
    ),
}


@pytest.mark.parametrize("rule", sorted(r for r in RULES if RULES[r][1]))
def test_the_owner_states_the_rule(rule):
    owner, facts, _ = RULES[rule]
    text = flat(*owner)
    missing = [fact for fact in facts if fact not in text]
    assert not missing, (
        f"{'/'.join(owner)} no longer names {missing} for rule {rule!r}, and "
        "it is the one carrier that does"
    )


@pytest.mark.parametrize("rule", sorted(r for r in RULES if RULES[r][2]))
def test_every_link_names_the_owner(rule):
    owner, _, links = RULES[rule]
    for carrier, names_the_owner in links.items():
        assert carrier != owner, f"{rule!r}: the owner is listed as its own link"
        # The owner's path and section, which a reader of the carrier
        # resolves.
        assert names_the_owner in flat(*carrier), (
            f"{'/'.join(carrier)} carries rule {rule!r} without naming "
            f"{'/'.join(owner)} as its owner, which is a second statement of "
            "the rule rather than a link to the one that owns it"
        )


FIX_PASS = "## Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer"


def test_the_fix_pass_reads_the_implementers_context_before_it_resumes():
    """S5 of #945. Rule 18 holds the threshold; this holds what lets an
    orchestrator act on the section: the command that reads the
    implementer's context and the column it reads, the section a fold of the
    records follows, and the record the commit of the closes holds."""
    text = flat(*ORCH)
    section = text[text.index(FIX_PASS) : text.index("## Orchestrator: the run ends")]
    for fact in (
        # The command the orchestrator runs over the implementer's transcript.
        "`seal cost --segments <the implementer's agent-*.jsonl>`",
        # The column of its output the orchestrator reads.
        "`context`",
        # The section the orchestrator resolves for how it folds a file that
        # holds a statement the fix pass named (round 2 of #1318).
        "`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*",
        # The path of the record the orchestrator's commit of the closes
        # holds (#1041).
        "`trail/rounds/round-N.md`",
    ):
        assert fact in section, f"the fix-pass section no longer says {fact!r}"


REGRESSION = "### A regression is routed by comparing the fix with the frame"


def test_the_framers_route_closes_each_finding_with_a_close_block_in_one_commit():
    """S2 of #1041, under #1198. On the framer's route no fix pass runs, so
    the orchestrator closes every open finding itself; row *The record*
    names the close block's `answer:` beside `deferred the frame`. That one
    commit holds every block is the proofer's to read."""
    text = flat(*ORCH)
    section = text[
        text.index(REGRESSION) : text.index("## Orchestrator: the pull request opens")
    ]
    row = section[section.index("| The record |") : section.index("| The framer |")]
    for said in (
        # The close verdict the orchestrator writes, which the chain check
        # reads as a close.
        "`deferred the frame`",
        # The close block's field that names the regression.
        "`answer:`",
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
    round. #1222 adds a poll before the wait, because the wait run before a
    check has reported exits 1 without waiting, and counts the checks of
    `pull_request` runs alone. #1494 replaces the read, the poll and the wait
    with `seal pr-wait`, which reads `gh`'s JSON and answers with an exit
    code: `gh pr checks --watch` exits 0 where the only bad check was
    cancelled, and ends before a job that waits on another has its check.
    The command's reads, its limit and their reasons stand in its docstring
    and in `tests/skills/test_pr_wait.py`, so the section gives the two
    commands the orchestrator types and what it does at each exit code. The
    case holds those commands, each exit code with the states that name
    exits 4 to 6, and the flag the orchestrator reads the branch's commits
    with; each row's act is the proofer's to read."""
    text = flat(*ORCH)
    section = text[
        text.index("## Orchestrator: the pull request opens once the sealer seals") : (
            text.index("## Orchestrator: verify before posting")
        )
    ]
    for said in (
        # The read the orchestrator types before each push, and the wait it
        # types when the pull request opens and after each push.
        "`seal pr-wait <N> --once`",
        "`seal pr-wait <N>`",
        # Each exit code the command answers with, as a row of the table that
        # gives the orchestrator's act at it.
        "| 0 |",
        "| 1 |",
        "| 2 |",
        "| 3 |",
        # The three states that stop the push or the wait, each with its code.
        "| 4 | `state` is `MERGED` |",
        "| 5 | `state` is `CLOSED` |",
        "| 6 | `state` is `OPEN` and `mergeable` is `CONFLICTING` |",
        # The flag the orchestrator reads the branch's commits with, so a
        # merge commit is left out.
        "`--no-merges`",
    ):
        assert said in section, f"the owner section no longer says {said!r}"


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
    the next crafter spawns, and before framing into the issue body.

    #1477 rewrote the one paragraph of ordered acts as six paragraphs of
    judgment, numbered as rows of that work item's `frame/design.md` D1.
    The case holds what those paragraphs name that the orchestrator opens,
    writes or types; whether each clause of D1 still stands is the proofer's
    to read. Every fact the section misses is named in one failure."""
    order = the_order()
    facts = (
        # The frame files a decision is folded into, and the file that states
        # the framer's fold.
        "`frame/design.md`",
        "`plan.md`",
        "`skills/implement/fold-and-reframe.md`",
        # The table the orchestrator writes each decision's row into, which
        # the settle reads.
        "`frame/plan.md` *Judgments of the run*",
        # The sections of the same file the paragraphs cite in italics.
        "*The frame is read against the issue at the spawn*",
        "*Alternatives considered*",
        "*Orchestrator: how the work is routed*",
        "*A problem that recurs within a run gets a prevention home at once*",
        # The sections a decision's fact often stands in, which the message
        # to the framer names.
        "*Scope*",
        "*Removes*",
        "*Grounding*",
        "*Technical context*",
        # The section the version move's fold is written into.
        "`frame/plan.md` *Operational impact*",
        # The records whose statements the orchestrator repairs or sends to a
        # fix pass.
        "`pr.md`",
        "`routing.md`",
        "`gaps.md`",
        "`changelog.md`",
        # The contract rule the read after a fold commit cites.
        "contract rule 12",
        # The command the framer's spawn prompt names for reading the issue.
        "`gh issue view <N> --json body,comments`",
    )
    missing = [fact for fact in facts if fact not in order]
    assert not missing, f"the order no longer names {missing}"


def test_the_framer_folds_a_decision_it_is_sent():
    """#1442, Scope item 5. The framer is resumed or spawned again with the
    decisions made after its frame was committed. The rule cites the
    sections and the contract rules the framer opens to answer them, and
    the table it writes a rejected decision into. The regression route keeps
    its own half of the rule, which rule 16 of `RULES` reads.

    #1473 moved the rule to `skills/implement/fold-and-reframe.md`, so a first
    frame does not preload it, and `agents/framer.md` names that file. Its
    four citations that resolved only inside the definition now name
    `agents/framer.md` or the contract."""
    path = "/".join(FOLD)
    # The path of the file a framer sent a fold opens.
    assert f"`{path}`" in flat(*FRAMER), (
        f"`agents/framer.md` no longer names `{path}`, so a framer sent a "
        "fold does not know where the rule stands"
    )
    text = flat(*FOLD)
    lead = "You have two routes back: a decision's fold, and the review chain's regression."
    start = text.index(lead)
    rule = text[start : text.index("check:", start)]
    for fact in (
        # The section the framer resolves for how it answers a decision.
        "`agents/framer.md` *An orchestrator's reading of the frame is "
        "answered in one exchange*",
        # The table the framer writes a rejected decision into.
        "`plan.md`'s *Alternatives considered*",
        # The contract rules the framer resolves for opening what a decision
        # cites and for reading each file whole.
        "contract rule 5",
        "contract rule 12",
        # The table whose row the framer reads with `plan.md`.
        "*Judgments of the run*",
        # The step a framer spawned fresh for a fold does not repeat.
        "`agents/framer.md` *Order of work* step 4",
    ):
        assert fact in rule, f"the framer's fold no longer says {fact!r}"


def test_a_handoff_file_is_written_only_to_move_the_work():
    """S9 of #945. Where a work item stands is in the records it already
    has, so a `handoff.md` lives only as long as a move between sessions.
    When it is written and deleted is the proofer's to read."""
    order = the_order()
    for said in (
        # The file the orchestrator writes to move the work.
        "`handoff.md`",
        # The records a work item's standing is read from.
        "`plan.md`",
        "`gaps.md`",
    ):
        assert said in order, f"the order no longer says {said!r}"


def test_a_recurring_problem_gets_a_prevention_home():
    """S9 of #945. A problem met twice in one run gets the place that
    prevents it before the next spawn, and the issue records where. Where
    the home goes is the proofer's to read."""
    order = the_order()
    for said in (
        # The paragraph's lead, which the fold paragraph of the same section
        # cites in italics.
        "A problem that recurs within a run gets a prevention home at once",
        # #1442, Scope item 2: the home is a decision, so the framer folds
        # it; the paragraph it cites for that.
        "*A decision made after the frame is committed is folded*",
    ):
        assert said in order, f"the order no longer says {said!r}"


def sentences(text):
    """`text`, flattened, cut after each full stop: the unit a pinned
    relation has to stand in together."""
    return re.split(r"(?<=\.)\s+", text)


@pytest.mark.rule("run-ends-with-verifying-round")
def test_a_close_that_does_not_hold_reopens_it():
    """S9 and S26 of work item 1791933022, and #1476. A verifying round
    answers each closed finding on one of three line keywords, `confirms:`,
    `regression:` and `reopens:`, which `lib/fields.py` spells and the
    chain check reads. `skills/code-review/SKILL.md` defines them, so it
    names the first two in one sentence, and the other three carriers owe
    no such sentence. Any sentence of the four that names the first two
    names the third in it too, so no carrier hands the proofer a channel
    with a keyword missing. When a close reopens, and how the run ends, are
    the proofer's to read."""

    def both(carrier):
        return [
            s
            for s in sentences(flat(*carrier))
            if "`confirms:`" in s and "`regression:`" in s
        ]

    # The two line keywords `lib/fields.py` spells, which the proofer
    # writes and the chain check reads.
    assert both(SKILL), f"{'/'.join(SKILL)} names the channel nowhere"
    for carrier in (RECORD, PROOFER, SKILL, ORCH):
        for s in both(carrier):
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
    names are the proofer's to read. This reads the two skill files the
    orchestrator acts from, not `docs/running/the-run.md` *The run*."""
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
    assert JUDGMENTS in run, run
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
