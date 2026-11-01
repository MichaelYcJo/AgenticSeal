"""The step before round 1 had no protocol, and the orchestrator was blind.

Round N hands round N+1 its coordinates — `round-N.md`'s Inherited axes,
"the coordinates carry; the verdicts do not". Nothing equivalent existed for
the step before round 1: the orchestrator hands the implementer a spawn
prompt nobody's format constrains, and the one measured fact that travelled
as prose (a count standing in for a claim) cost a full review round before
anyone could check it. And while the implementer runs, the progress readout
it is already writing — `plan.md`'s Status column — is named by no document
the orchestrator reads, so "is 40 minutes normal" was answered by `git log`
twice on two consecutive work items.

Each case here was shown red before the prose it pins landed (#29).
"""

import re

from conftest import flat, read

# --- the handoff before round 1 ---------------------------------------------


PROTOCOL = ("docs", "the-review-record.md")


def test_the_protocol_carries_the_handoff_before_round_one():
    """The handoff names the labels a fact carries when it has no
    coordinate, by their spelling. What a handoff carries otherwise is the
    proofer's to read."""
    protocol = flat(*PROTOCOL)
    # The three labels by their spelling, which the orchestrator writes
    # beside a fact and an agent reads; `hooks/lib/fields.py` matches the
    # first two on a round record's `evidence:` line.
    assert "`executed`, `read` or `unverified`" in protocol, (
        "the labels a handoff fact carries are verify's three, by name — a "
        "fact with none is an assertion nobody has opened"
    )


def test_the_implementer_documents_point_at_the_section():
    """A protocol section nobody is routed to is the same defect one layer
    up: the answer exists and the party needing it does not know it is
    there — which is how session_cost.py went unused for a day. What stays
    in the definitions since phase 4 of #107 is the ROUTE: the section a
    prompt's facts arrive under."""
    for parts in (("skills", "implement", "SKILL.md"), ("agents", "crafter.md")):
        text = flat(*parts)
        # The path the implementer resolves to the section its prompt's
        # facts arrive under.
        assert "`docs/the-review-record.md`" in text and "handoff" in text, "/".join(
            parts
        )


# --- the rules a prompt no longer carries -----------------------------------


def test_the_protocol_no_longer_states_the_rules_it_points_at():
    """The restatement check: each rule below is the contract's or a
    definition's, and a copy of it in the record's document is a second
    source a paste-back would bring."""
    protocol = flat(*PROTOCOL)
    for phrase, whose in (
        ("never `cmd | tail; echo $?`", "contract rule 1"),
        ("enumerate the class, do not fix the coordinate", "contract rule 12"),
        ("Do not push, do not open a pull request", "contract rule 6"),
        ("make a `uv` venv", "`agents/proofer.md`"),
        ("Mutation-test every unit that adds behaviour", "`agents/crafter.md`"),
    ):
        assert phrase not in protocol, (
            f"the protocol states {whose} again: {phrase!r}. This document is "
            "a pointer at those rules now, and a copy beside the pointer is "
            "the state #107 opens with"
        )


# --- progress observability -------------------------------------------------


def test_the_protocol_names_the_meter():
    """The section the orchestrator reads while an agent runs names the
    script that reads the agent's transcript after the run. The progress
    channel and the stall signal are the proofer's to read."""
    protocol = flat(*PROTOCOL)
    # The script the orchestrator runs over the agent's transcript.
    assert "session_cost.py" in protocol, (
        "the meter existed through a full day of measurements nobody took, "
        "because nothing a session reads pointed at it"
    )


# --- the batching expectation in the contracts ------------------------------


def test_the_contract_cites_the_per_segment_bars():
    """Contract rule 10 points each kind of segment at its bar, and the bar
    has one home, `docs/the-review-record.md` *The per-segment bars*; no
    definition carries a copy since #957."""
    contract = flat("skills", "agent-contract", "SKILL.md")
    # The citation every agent resolves to find the bar its segment is
    # judged against.
    assert "`docs/the-review-record.md` *The per-segment bars*" in contract, (
        "the contract stopped pointing at the bars, and a figure with no home "
        "is one that measures the wrong agent"
    )


def framer_rule(text, lead):
    """The `agents/framer.md` rule paragraph opening with `**<lead>**`, up to
    its `check:` line. Scoped so a phrase elsewhere in the definition cannot
    hold one of the claims below up after the rule itself lost it."""
    match = re.search(rf"^\*\*{re.escape(lead)}\*\*(.*?)^check: ", text, re.M | re.S)
    assert match, (
        f"`agents/framer.md` has no rule opening `**{lead}**`. The opening was "
        "typed into spawn prompts from 0.12.3 and lived in no file (#640); a "
        "rename has to bring this case with it"
    )
    return " ".join(match.group(1).split())


def test_the_framers_definition_carries_its_opening():
    """#640, recommendation 1. A rule kept only in whoever last wrote a
    prompt goes missing without a trace (#107), and the framer's opening was
    exactly that: found by the 2026-09-28 sweep in no file at all.

    The bound is a rule of `agents/framer.md`, located by its lead. What it
    cites and the command it gives for a large file are held by their
    spelling; the bound's own wording is the proofer's to read."""
    text = read("agents", "framer.md")
    rule = framer_rule(text, "Bound each call, not the reading.")
    # The contract rule number the framer resolves for the rule the bound
    # applies.
    assert "rule 10" in rule, "the bound stopped citing the rule it applies"
    # The command the framer types to read a large file by range.
    assert "sed -n" in rule, (
        "the large-file half went, which is the third clause #478 recorded"
    )


# --- the per-segment bars (work item 1788277657, round 1's tests-todo) ------


def test_the_protocol_names_a_bar_per_segment_kind():
    """One bar misread two of the three segment kinds: the ratio that judges
    a reviewer is the wrong question for an edit-test loop, and the meter's
    numbers had no written rule at all about what they mean. Each kind's bar
    is a value the orchestrator reads a segment against, held here by its
    spelling; why each kind has its bar is the proofer's to read."""
    protocol = flat(*PROTOCOL)
    # The reviewing bar, the value the orchestrator reads a proofer's
    # segment against and `session_cost.py#SEGMENT_BARS` grades by.
    assert "tools per turn **≥ 1.8**" in protocol, "the reviewing bar went"
    # The implementing bar, the value the orchestrator reads a crafter's
    # segment against.
    assert "`repeats = 0`" in protocol, "the implementing bar went"
    # The verifying row's value, which tells the orchestrator a verifying
    # round is read against no bar.
    assert "| verifying | exempt |" in protocol
    # #640. The framing bar, the value the orchestrator reads a framer's
    # segment against and `session_cost.py#SEGMENT_BARS` grades by; the
    # script's constant is cross-pinned to it below rather than read from it.
    assert "| framing | tools per turn **≥ 1.4** |" in protocol, (
        "the framing bar went, and `--segments` grades framer rows against a "
        "number no policy states"
    )


def bars_section(text):
    """The body of `### The per-segment bars`, heading to the next heading of
    any level or the end of the document.

    Scoped rather than whole-file: the document names `session_cost.py` a
    section up, so a document-wide search would stay green with this section
    saying nothing about the run-level table -- which is the one edit this
    case exists to catch."""
    match = re.search(
        r"^### The per-segment bars$(.*?)(?=^#{2,3} |\Z)",
        text,
        re.M | re.S,
    )
    assert match, (
        "the per-segment bars section is gone or renamed. It is where the "
        "orchestrator meets the meter's numbers, and a rename has to bring "
        "this case with it"
    )
    return " ".join(match.group(1).split())


def test_the_tying_paragraph_says_which_reading_applies_the_bars():
    """#640. For `--segments` a row's kind is the `subagent_type` of the
    spawn it was joined to, and the paragraph names that field. What the
    paragraph says the plain reading cannot tell is the proofer's to read."""
    section = bars_section(read(*PROTOCOL))
    # The transcript field `session_cost.py` joins a row's kind by, which
    # the orchestrator reads to know why a row is graded.
    assert "`subagent_type`" in section, (
        "the paragraph says the page knows a row's kind and not how"
    )


def test_the_bars_section_cites_the_run_level_tables_owner():
    """Two instruments over the same run, and a reader who meets only the
    bars has no way to know the second one exists. The section that owns the
    bars cites the section that owns the run-level table, by its file and
    its heading. Which instrument judges what is the proofer's to read."""
    section = bars_section(read(*PROTOCOL))
    # `docs/` is not edited by a pull request: #940 moved the table to
    # `skills/verify/orchestration.md`, and its `## Rule changes` item moves
    # this citation at the settle after its release. Until then the section
    # names the old path, and either path names the owner. The path is the
    # citation the orchestrator resolves for the table's rows.
    assert any(path in section for path in OWNER_PATHS), (
        "the section names no owner for the table, so a reader arriving for "
        "its rows leaves with neither them nor the path to them"
    )
    # The heading the same citation names, which the orchestrator resolves
    # in that file.
    assert "Measure the segment, and feed the flow log" in section, (
        "the pointer names the file and not the section, which is a whole "
        "skill to search for one table"
    )


# The table's owner, and the path `docs/the-review-record.md` named before
# #940's rule change is applied.
OWNER_PATHS = ("skills/verify/orchestration.md", "skills/verify/SKILL.md")


def test_the_scripts_bars_are_the_protocols():
    """#640. The bars live in the protocol's table and, since `--segments`
    grades by kind, in `session_cost.py`'s `SEGMENT_BARS` too -- constants,
    because the script runs from the installed plugin in repositories with no
    such document. Two copies of a number is the six-month failure the plan
    names, so this reads both files and either moving alone turns it red.

    The implementing row is held too: the protocol says it is never judged
    on tools per turn, and the script's entry for it is the exemption."""
    script = read("skills", "verify", "scripts", "session_cost.py")
    protocol = read(*PROTOCOL)
    for kind, segment in (("proofer", "reviewing"), ("framer", "framing")):
        constant = re.search(rf'"{kind}": \("{segment}", ([\d.]+)\)', script)
        assert constant, f"`SEGMENT_BARS` lost its {kind} entry or its shape"
        row = re.search(
            rf"^\| {segment} \| tools per turn \*\*≥ ([\d.]+)\*\* \|", protocol, re.M
        )
        assert row, f"the protocol's bars table lost its {segment} row or its shape"
        assert constant.group(1) == row.group(1), (
            f"session_cost.py grades a {kind} row against {constant.group(1)} "
            f"and the protocol's {segment} bar is {row.group(1)} -- move both or "
            "neither"
        )
    # Round 1's ⬜ 7: the loop above names two kinds, so an entry with a bar
    # added to either table alone passed. The whole of both is compared.
    entries = re.findall(r'^    "(\w+)": \("(\w+)", ([\d.]+|None)\),$', script, re.M)
    assert len(entries) >= 3, f"`SEGMENT_BARS` moved off its shape: {entries}"
    graded = {segment: bar for _, segment, bar in entries if bar != "None"}
    rows = dict(
        re.findall(r"^\| (\w+) \| tools per turn \*\*≥ ([\d.]+)\*\* \|", protocol, re.M)
    )
    assert graded == rows, (
        f"`SEGMENT_BARS` grades {graded} and the protocol's table states {rows} "
        "-- add, move or remove both or neither"
    )
    assert '"crafter": ("implementing", None)' in script, (
        "`SEGMENT_BARS` grades a crafter row, and the protocol's implementing row "
        "says tools per turn never judges one"
    )
    assert re.search(r"^\| implementing \|.*never tools per turn", protocol, re.M)


def test_the_advisory_and_the_tying_paragraph_name_one_value():
    """The bars (1.8) live in the protocol and the advisory in the script,
    tied by one sentence — the plan's own six-month failure scenario is the
    script's threshold moving while the sentence keeps the old value. This
    case reads both files, so that move turns it red."""
    script = read("skills", "verify", "scripts", "session_cost.py")
    # #640, round 2's 🟡 8: the advisory compares the ratio rounded to the two
    # places it prints, so the pattern reads the rounded comparison.
    threshold = re.search(r'round\(data\["tools_per_turn"\], 2\) < ([\d.]+)', script)
    assert threshold, "the advisory threshold moved off its pattern in session_cost.py"
    protocol = flat(*PROTOCOL)
    assert (
        f"batching advisory below {threshold.group(1)} and stays there" in protocol
    ), (
        "the protocol's tying paragraph names a different value than "
        f"session_cost.py's {threshold.group(1)} — update the sentence, "
        "or the reader meets 1.8 and the advisory as a contradiction"
    )
