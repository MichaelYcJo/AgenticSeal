"""The one-broad-run rule spans six documents; drift between them is the bug.

The skill states it, the agent contract binds every agent to it, the smith
follows it, the warden audits it, two records carry it to the next session,
and the preset block states it for a session that loads none of them. A rule
spread this wide fails by one of them quietly dropping its part, which is
invisible in any single diff.

Phases 3 and 4 of #107 moved the prohibition and the refusal out of the two
agent definitions and into `skills/agent-contract/SKILL.md`. The cases moved
with them rather than being deleted: what each definition still holds is its
own APPLICATION -- the warden audits the label and has a named field for the
question, the smith puts both answers in a hand-back the caller can reply in
-- and a case asserting the same sentence in two files is the duplication the
contract was written to end. That duplication has its own module now,
`tests/test_a_moved_rule_leaves_its_definition.py`, because until phase 4
nothing in the tree noticed a moved rule being pasted back.
"""

import glob
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return f.read()


def flat(*parts):
    """The file as one line, so an assertion is not pinning where it wraps."""
    return " ".join(read(*parts).split())


def read_at(path):
    """One file by absolute path, for the cases that walk a glob."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def test_verify_says_when_not_only_what():
    scope = read("skills", "verify", "SKILL.md")
    assert "## Scope" in scope, "verify lost the section that bounds the moment"
    for row in (
        "Each slice",
        "Phase boundary",
        "Handoff to review",
        "After the rounds settle",
    ):
        assert row in scope, f"the Scope table lost its `{row}` row"
    assert "against the base commit" in scope
    assert "Nothing edits between the broad run and the PR" in scope
    assert "broad seal" not in scope


def test_the_broad_gate_section_states_its_own_timing():
    """The Scope table settles when the gate fires; the section did not repeat
    it, and a session that jumped to the section by its heading ran the whole
    suite before review. Two sessions did exactly that, 22 minutes between
    them, and both runs were void by the first review finding.

    The baseline is the same failure one step further in: it is reached for
    once an unexplained failure appears, not before one exists."""
    scope = read("skills", "verify", "SKILL.md")
    section = scope.split("## The broad gate")[1].split("\n## ")[0]
    flat = " ".join(section.split())  # re-wrapping a paragraph is not a regression
    assert "after the review rounds settle" in flat, (
        "the broad gate section stopped saying when it fires"
    )
    assert "Nothing broad runs at the handoff to review" in flat, (
        "the section stopped ruling out the run that review rounds void"
    )
    assert "once an unexplained failure appears" in flat, (
        "the baseline stopped naming the event that calls for it"
    )
    # #943 renamed the section that owns when the run comes; a citation left
    # at the old name points at a heading no file has.
    assert f"`skills/code-review/orchestration.md` §*{SPAWN_SECTION}* owns when" in (
        flat
    ), "the broad gate section no longer names the owner of when the run comes"


def test_the_owner_names_the_row_the_phrase_stood_for():
    """*After the rounds settle* names no particular rounds. A work item has
    build phases with a progression of their own and a review chain with its
    own, and a reader deciding whether the gate is due has to pick one. The
    condition is the last round record with no finding open, which the check
    at the pull request reads."""
    owner = flat("skills", "verify", "SKILL.md")
    assert "the last `rounds/round-N.md` has no finding open" in owner, (
        "the broad gate's own section stopped naming the row, and the phrase "
        "it leaves behind names no particular rounds"
    )


def test_verify_prices_the_run_that_repeats():
    """Scope decides how often; it says nothing about what each run costs, and
    the narrow run is the one that multiplies."""
    scope = read("skills", "verify", "SKILL.md")
    assert "## The cost of the run you repeat" in scope
    assert "recipe in a comment" in scope  # line-wrapped in the source
    assert "Capture once, filter locally" in scope, (
        "re-running a check to see its output differently returns nothing new"
    )


def test_the_implementers_bar_is_not_the_reviewers_and_has_one_home():
    """Contract §10 points each kind of segment at its bar in
    `docs/the-review-record.md` §*The per-segment bars*, and the implementing
    row is not judged by tools per turn: an edit-test loop judged by the
    reviewer's bar is asked for what a serial loop cannot give. Since #957
    no definition carries a second copy of a bar."""
    contract = flat("skills", "agent-contract", "SKILL.md")
    assert "`docs/the-review-record.md` §*The per-segment bars*" in contract
    bars = flat("docs", "the-review-record.md")
    assert "never tools per turn" in bars, (
        "the implementing row lost the sentence that keeps it off the reviewer's bar"
    )


def test_the_smith_puts_both_answers_in_the_hand_back():
    """What stayed with the implementer when §2 and §3 moved.

    The rule is the contract's and is asserted against it below. This is the
    half that is nobody else's: WHERE the two answers land. The smith's
    handover is a conversation the caller can reply in, so the unverified
    suite and a declined instruction both go in as prose -- which is exactly
    why the warden, whose handover is a report, needed a named field for the
    same sentence and has one.

    Round 1 of the original rule found `Decline` separable from `name`: a
    refusal nobody is told about is the same 28 minutes with a footnote. The
    disclosure half is asserted here because the smith is where it is
    disclosed."""
    smith = flat("agents", "smith.md")
    assert "§2" in smith and "§3" in smith, (
        "the implementer can no longer reach the rules its hand-back answers"
    )
    assert "the suite labelled `unverified`" in smith, (
        "the suite stopped going over labelled, and a suite that is simply "
        "not mentioned reads as a suite that passed"
    )
    assert "the orchestrator named as its answerer" in smith, (
        "the label lost its answerer, and a deferral to nobody is how "
        "`someone will look at it` becomes `nobody did`"
    )
    assert "saying what was asked and which rule refused it" in smith, (
        "the declined instruction stopped being disclosed, which is how an "
        "override stays invisible"
    )
    assert "hand-back" in smith, (
        "the destination went. Without it §3's disclosure sentence has "
        "nowhere named to land, which is the gap the warden's field fills"
    )


def contract_section(number):
    """The body of `## §N` in the contract, heading excluded.

    Scoped rather than whole-file, because the thing #120 has to keep out is
    a WORD -- `orchestrator` -- that the contract says legitimately elsewhere
    (its opening paragraph, about the prompt a round arrives in). A whole-file
    absence check would either fail on that sentence or be dropped."""
    text = read("skills", "agent-contract", "SKILL.md")
    heads = list(re.finditer(r"^## §(\d+) (.+)$", text, re.M))
    for index, match in enumerate(heads):
        if int(match.group(1)) != number:
            continue
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        return " ".join(text[match.end() : end].split())
    raise AssertionError(f"the contract has no §{number}")


# What a definition says when it hands its agent the run: the command typed
# with a base, or the sentence the sealer carried until #969. Matched over the
# whole glob, so a sixth definition is read the day it lands.
TAKES_THE_RUN = (
    "broad-gate --base",
    "the broad gate is yours",
    "spawned for exactly that",
)
RUN = "broad-gate --base <base> --record <item>"


def test_no_definition_assigns_the_broad_gate_and_the_orchestrator_runs_it_before_the_spawn():
    """S2 of #969. Contract §2 says no agent runs the broad gate and names the
    orchestrator's command; no file under `agents/` hands its agent the run;
    and the orchestration names the preflight, the run, its log and its commit
    before the sentence that spawns the sealer.

    Protects: a definition taking the run back, which is the second run of a
    suite #957 measured at 240K tokens; and the orchestration spawning the
    sealer before the run, which leaves it a record that is absent or stale.
    It replaces the three cases that pinned the interim §2, the count of
    silent definitions and the preflight's order, because each held one third
    of one fact and none held the run's place in the order."""
    contract = " ".join(read("skills", "agent-contract", "SKILL.md").split())
    body = contract_section(2)
    assert "no agent runs any of the three" in body, (
        "§2 stopped forbidding the broad gate to every agent"
    )
    assert RUN in body and "orchestrator" in body, (
        "§2 stopped naming the orchestrator's command"
    )
    assert body.index(RUN) < body.index("spawns the sealer"), (
        "§2 names the spawn before the run it waits for"
    )
    for named in ("but the sealer", "Where the run is yours"):
        assert named not in body, f"§2 still names an agent as runner: {named!r}"
    assert "Hand over with the suite labelled `unverified`" in contract, (
        "the label went, and a suite that is simply not mentioned reads as a "
        "suite that passed"
    )
    agents = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
    assert len(agents) >= 4, f"agents/*.md matched {len(agents)} files"
    taking = [
        (os.path.basename(path), marker)
        for path in agents
        for marker in TAKES_THE_RUN
        if marker in " ".join(read_at(path).split()).lower()
    ]
    assert not taking, f"a definition hands its agent the broad run: {taking}"
    order = joined(
        section(read("skills", "code-review", "orchestration.md"), SPAWN_SECTION)
    )
    steps = [
        PREFLIGHT,
        RUN,
        "<scratchpad>/<work-item-id>/broad-gate.log",
        "commit `broad-gate.md`",
        "spawn `sealer`",
    ]
    missing = [step for step in steps if step not in order]
    assert not missing, f"the orchestration does not name: {missing}"
    at = [order.index(step) for step in steps]
    assert at == sorted(at), (
        f"the orchestration's order is not preflight, run, log, commit, spawn: {steps}"
    )


def test_no_definition_promises_the_suite_once_the_rounds_settle():
    """Round 1, finding 2 of #120. `agents/warden.md` read *§2 keeps the suite
    out of your hands UNTIL the rounds settle*, which says it becomes the
    warden's afterwards.

    Under the old §2 that was a harmless imprecision about a prohibition with
    a holder who was not an agent. Under the new one it is false in a way a
    reader can act on: this file assigns none of the three, and since #969 no
    definition does, because the orchestrator runs the gate. The hazard is
    live rather than theoretical --
    `agents/warden.md`'s own bullet on the broad-gate state puts a reviewer in
    exactly the moment the sentence appears to release.

    Asserted over the whole glob, not over the one file the finding named,
    because a temporal release is the shape any definition can pick up while
    describing a rule it does not hold.

    **The direction this can still miss, stated rather than left to be found.**
    It matches one spelling. A definition that promises the suite in other
    words -- *yours once the rounds have settled* -- is invisible here, which
    round 2 of #120 measured by rewording the corrected sentence and watching
    this case stay green. That is a verbatim-versus-semantic trade: no
    constant decides when two sentences say the same thing.
    What narrows it is that the wrong sentence had exactly one idiom in this
    tree, and the glob is what catches that idiom arriving in a second file --
    which is the copy this shape actually spreads by."""
    for path in sorted(glob.glob(os.path.join(ROOT, "agents", "*.md"))):
        text = " ".join(read_at(path).split())
        assert "until the rounds settle" not in text.lower(), (
            f"{os.path.basename(path)} promises the suite once the rounds "
            "settle. §2 has no such release for anyone: an agent takes the "
            "broad gate when its own definition assigns it, and never later"
        )


def test_the_warden_audits_the_scope_of_a_seal():
    """What stayed with the reviewer: the audit, which is nobody else's.

    §2 says the reviewer does not run the suite. It does not say what the
    reviewer does INSTEAD, and that half is an application of the rule rather
    than the rule -- a seal is audited by the second person looking, and the
    warden is the only agent that is one."""
    warden = " ".join(read("agents", "warden.md").split())
    assert "whether that label is honest" in warden, (
        "the reviewer stopped being told to audit the label, so the only "
        "thing left is the prohibition and the seal goes unchecked"
    )
    assert "not whether the number is green" in warden, (
        "the audit lost the half that says what it is NOT -- a green number "
        "read as an honest label is the failure the audit exists to catch"
    )


def test_the_refusal_is_stated_once_and_names_both_directions():
    """Re-pointed in phase 3 from a per-agent loop over smith and warden.

    Round 2's finding stands and is now the contract's to hold: the rule
    reached a second file and the REFUSAL half did not follow it, so the
    principle and the disclosure alone read as `run it, but say so`. Both
    halves are asserted, plus the default for an instruction that cannot be
    classified -- a default nothing holds is the same as no default."""
    contract = " ".join(read("skills", "agent-contract", "SKILL.md").split())
    assert "do not run it" in contract, (
        "the refusal half went; the principle and the disclosure alone read "
        "as `run it, but say so`"
    )
    assert "decline, and name the instruction in your hand-back" in contract, (
        "`Decline` became separable from `name`, which is the state that was "
        "measured -- the run happened and the caller believed the prompt was "
        "honoured"
    )
    assert "run nothing extra and say in the hand-back" in contract, (
        "the contract lost the default for an instruction it cannot classify, "
        "so the rule above it decides nothing in the one case that needed "
        "deciding"
    )


def test_the_reviewer_has_a_field_for_the_question_the_default_produces():
    """The reviewer needs somewhere for that question to LAND.

    Its handover is a report, not a conversation -- unlike the smith's, which
    returns through the chain -- so an unanswered axis would otherwise be
    sealed over by the orchestrator that reads the report. That is why this
    half stayed in `agents/warden.md` when the rule above it left."""
    warden = " ".join(read("agents", "warden.md").split())
    assert "goes in as a row of `## Not judged` with the caller" in warden, (
        "the reviewer asks a question with no field to ask it in, and a seal "
        "gets taken over an axis nobody decided"
    )
    assert "a report rather than a conversation" in warden, (
        "the reason the field exists went, and a field with no reason is the "
        "next one a rewrite drops"
    )


def test_the_broad_gate_state_survives_a_handoff():
    """A session joining at round 3 cannot see which commands were run."""
    assert "`broad-gate.md`" in read("docs", "the-review-record.md"), (
        "the record lost the file that tells the next session whether the one "
        "broad run already happened"
    )


def test_the_preset_block_states_the_rule_the_loaded_files_assume():
    """Every other home for this rule loads on demand.

    An agent file needs the agent spawned and a skill needs the skill invoked.
    A session working this repo directly does neither, so the preset block --
    always in front of it -- is the only copy it will ever read."""
    preset = read("templates", "claude-md-block.md").split("<!-- specseal:end -->")[0]
    assert "<!-- specseal:start -->" in preset, "the preset markers moved"
    assert "Verification Scope" in preset, (
        "the always-loaded block lost the rule that bounds a broad run"
    )
    assert "Batch independent reads and runs" in preset, (
        "the always-loaded block lost the batching rule"
    )
    assert "Never cut the investigation." in preset, (
        "the batching rule lost its bound: fewer trips, never fewer checks"
    )


# --- 1790815611: the record arms run before the sealer is spawned (#638) -------

PREFLIGHT = "broad-gate --preflight"
SPAWN_SECTION = (
    "Orchestrator: the pull request opens once the sealer seals, and a phase is re-run"
)


def section(text, heading):
    """The `## heading` section of `text`, its heading line included, up to
    the next heading of the same or a higher level."""
    lines = text.splitlines()
    start = lines.index(f"## {heading}")
    end = next(
        (i for i in range(start + 1, len(lines)) if re.match(r"^#{1,2} ", lines[i])),
        len(lines),
    )
    return lines[start:end]


def joined(lines):
    return " ".join(" ".join(lines).split())


def test_the_acts_table_row_names_the_preflight_and_stays_a_sentence():
    """S8's other half. The row for that section keeps `still a sentence` —
    a session that skips the preflight loses time and nothing else, because
    the broad run asks the same arms — and its grounds name the step."""
    rows = [
        line
        for line in read("skills", "implement", "orchestration.md").splitlines()
        if line.startswith(f"| {SPAWN_SECTION} |")
    ]
    assert len(rows) == 1, f"{len(rows)} acts-table rows name the section"
    assert "| still a sentence |" in rows[0], rows[0]
    assert PREFLIGHT in rows[0], "the row's grounds do not name the preflight"


def test_the_order_inside_a_ticket_puts_the_preflight_before_the_sealer():
    """The order section sequences the sealer's spawn, so the step before it
    is written in where the spawn is."""
    text = joined(
        section(
            read("skills", "implement", "orchestration.md"),
            "Orchestrator: the order inside a ticket",
        )
    )
    assert PREFLIGHT in text, "the order does not name the preflight"
    assert text.index(PREFLIGHT) < text.index("then the sealer, and then the pull"), (
        text
    )


EXAMPLE_ROW = (
    "| Broad gate | uvx ruff check . && uvx ruff format --check . && bin/test -q |"
)
BY_HAND = (
    "`evidence-check`",
    "`unverified-check`",
    "`chain_check.py`",
    "`survivor-check`",
)


def test_the_example_row_goes_lint_first_and_the_arms_are_not_listed_by_hand():
    """S9, the owner's answer of 2026-10-01: the row a repository copies puts
    the seconds-long linters ahead of the suite, as this repository's own row
    does. The prose above it named four of the gate's six arms; it points at
    the one list instead, and says the preflight runs those arms alone."""
    body = section(read("templates", "config.md"), "Broad gate")
    assert EXAMPLE_ROW in body, "the example row is not the lint-first one"
    lead = joined(body).split("```")[0]
    listed = [name for name in BY_HAND if name in lead]
    assert not listed, f"the prose still lists arms by hand: {listed}"
    assert "broad_gate.py" in lead and PREFLIGHT in lead, lead


def test_the_skill_says_the_preflight_is_not_the_broad_gate():
    """S10. `verify` names the preflight in the section that assigns the run,
    and says what keeps it from being mistaken for one: no suite, nothing
    sealed. The sealer's own definition never mentions it — the sealer does
    not preflight, and its four acts are unchanged."""
    text = joined(
        section(
            read("skills", "verify", "SKILL.md"),
            "The broad gate — after the rounds, then compare against the base",
        )
    )
    assert PREFLIGHT in text, "the broad gate section does not name the preflight"
    at = text.index(PREFLIGHT)
    said = text[max(0, at - 300) : at + 500]
    assert "runs no suite" in said and "writes nothing" in said, said
    assert "orchestrator" in said, said
    assert "--preflight" not in read("agents", "sealer.md"), (
        "the sealer's definition names the preflight"
    )
