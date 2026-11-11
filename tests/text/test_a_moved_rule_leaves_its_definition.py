"""A rule moved into the contract does not stay behind in a definition too.

Q2 of #107 answered *full*: `skills/agent-contract/SKILL.md` is the single
home for every universal rule, and each `agents/*.md` keeps only its own
application. Phases 3 and 4 did the moving. Nothing checked that it was a
move.

Without this module, contract rule 9's body pasted back into
`agents/proofer.md` as a paragraph, or under a `###` heading, leaves
`test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`,
`test_every_agent_reads_the_contract` and
`test_the_agent_contract_holds_the_universal_rules` all green. Only a paste
under a new `##` heading is caught there, by the list of `## ` headings
`test_every_agent_reads_the_contract` holds each definition to (#957). When
phases 1 and 2 wrote their two modules, every assertion in them was a
presence check, and the only absence checks in the tree were about the
contract's own frontmatter. So the half of Q2 that says *the definition
keeps only its own application* had nothing behind it at all, and the tree
could drift straight back to the state #107 opens with, one paste at a time,
with a green suite the whole way.

## Where this draws the line

A definition MAY cite a rule by its number and say what the rule means
for its own role, in its own words -- that is the application form, and
phases 3 and 4 kept several deliberately: the proofer's audit of the
`unverified` label, its `## Not judged` row, the #36 cost of a
prompt landing during a round; the crafter's 1.08-1.17 and its
hand-back as the place both answers land. Every one of those is about one
agent, and none of them is the rule.

What a definition may NOT do is carry the contract's own sentences. So the
check is verbatim rather than semantic: a run of `WINDOW` consecutive words
from a section's body, whitespace-normalised, appearing inside an agent
definition.

Verbatim is the deliberate half. The failure that was measured is a paste,
and a check that tried to catch a paraphrase would have to decide when two
sentences say the same thing -- which no constant can hold, and which would
refuse the application prose this rule exists to permit. What it therefore
does not catch is a definition restating a universal rule in fresh words.
That is a reviewer's finding, and saying otherwise here would be the
counterfeit `CONTRIBUTING.md` refuses.

`WINDOW` comes from the tree rather than from taste. Measured across all
three definitions after phase 4, the longest run any KEPT application shares
with any section is 10 words (`agents/crafter.md`'s `a bare word is a pathspec
and git rejects it`, which the retired probe rule and the design gate's waiver
paragraph both spelled because both were about the same git fact; the
proofer's 9-word echo of contract rule 6 was the next). Both left with their
rewrites (#957, #967), and the widest kept run since is 8 words,
`agents/sealer.md` with contract rule 2 (the framer's 8 with contract rule 5
left with its rewrite, #968). The smallest run a REAL duplication produced,
measured on the same files before phase 4 removed them, is 25 words
(contract rule 10), then 31 (contract rule 9), 37 (a rule #957 folded into
contract rule 11), 59 (contract rule 11) and 66 (contract rule 3).
Fifteen sits between 10 and 25 with margin
on both sides, and both ends of that margin are printed by
`test_the_window_sits_between_what_was_measured`, so a later edit that
narrows the gap is red rather than silently mis-tuned.

The list of rules is derived from the contract, never typed here. A
hand-copied list is a second source that disagrees with the first, and this
repository has been bitten by exactly that -- `ROUND_RECORD_FIELDS` in
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` carries the
scar. A rule added as number 21 is checked on the day it lands, and so is a
fourth agent definition, because both come from a glob.
"""

import glob
import os

import pytest
from conftest import ROOT, load_module, read
from conftest import flattened as flat
from conftest import repo_relative as name
from test_the_agent_contract_holds_the_universal_rules import HEADING

CONTRACT = os.path.join(ROOT, "skills", "agent-contract", "SKILL.md")
AGENTS = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))

# A run of this many consecutive words is longer than any phrase two of these
# documents share by writing about the same mechanism, and shorter than the
# smallest copy phase 4 removed. Both bounds are measured; see the docstring
# and `test_the_window_sits_between_what_was_measured`. The number is
# `skills/settle/scripts/passages.py`'s, the reader the paste check and
# `chain-check` share (#1216).
WINDOW = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "passages.py"),
    "agentic_passages_for_the_moved_rule_check",
).WINDOW

# What the two ends of that margin were, when the number was chosen. These are
# not the rule -- they are what makes the rule auditable, and the case below
# is what keeps them from becoming a story about a number nobody re-measured.
LONGEST_KEPT_APPLICATION = 10
SMALLEST_REAL_DUPLICATION = 25


def sections(text):
    """{number: body} for every `## <N>` in the contract, heading excluded.

    The heading is left out on purpose: a heading is a label, and a
    definition that names the same subject in its own heading is doing the
    citing this file permits."""
    heads = list(HEADING.finditer(text))
    out = {}
    for index, match in enumerate(heads):
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        out[int(match.group(1))] = text[match.end() : end]
    return out


SECTIONS = sections(read(CONTRACT))


def runs(body, window=WINDOW):
    """Every window of `window` consecutive words in a section body."""
    words = flat(body).split()
    return [" ".join(words[i : i + window]) for i in range(len(words) - window + 1)]


def copied(body, definition, window=WINDOW):
    """The runs of `body` that appear verbatim in `definition`."""
    haystack = flat(definition)
    return [run for run in runs(body, window) if run in haystack]


def longest_shared(body, definition):
    """The longest run of `body`'s words that appears in `definition`.

    Reported rather than asserted on, so a failure says how much was copied
    and a measurement case can print the margin."""
    haystack = flat(definition)
    words = flat(body).split()
    best = 0
    for start in range(len(words)):
        end = start
        while end < len(words) and " ".join(words[start : end + 1]) in haystack:
            end += 1
        best = max(best, end - start)
    return best


# --- there is something to check -------------------------------------------


def test_the_globs_find_the_definitions_and_the_sections():
    """A glob that matches nothing passes every case parametrised on it, and
    both of these are globs."""
    assert len(AGENTS) >= 3, f"agents/*.md matched {len(AGENTS)} files"
    assert len(SECTIONS) >= 16, f"the contract has {len(SECTIONS)} numbered sections"


# --- the move was a move ----------------------------------------------------


@pytest.mark.parametrize("number", sorted(SECTIONS))
@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_no_definition_carries_a_sections_own_sentences(path, number):
    """One case per section per definition, so a failure names both.

    Both axes are derived: a rule 21 added tomorrow and a fourth agent added
    tomorrow are each checked on the day they land, which is the miss with no
    other symptom."""
    duplicated = copied(SECTIONS[number], read(path))
    assert not duplicated, (
        f"{name(path)} carries contract rule {number}'s own words: "
        f"{duplicated[0]!r}. A definition may cite rule {number} and say what "
        "it means for its role, "
        "in its own words; carrying the contract's sentences is the "
        "duplication the contract was written to end, and it is invisible in "
        "a diff that only adds"
    )


def test_the_window_sits_between_what_was_measured():
    """The number is a measurement, so it is checked against the tree.

    Two ways this goes wrong quietly. A kept application grows until it
    shares more than `WINDOW` words with a section, and the case above starts
    refusing the prose it exists to permit. Or `WINDOW` is raised past what a
    real copy produces, and the case passes on a paste. Both are edits
    somebody makes for a good local reason, and neither shows up anywhere
    else."""
    widest = max(
        (
            (longest_shared(body, read(path)), name(path), number)
            for number, body in SECTIONS.items()
            for path in AGENTS
        ),
    )
    assert widest[0] < WINDOW, (
        f"{widest[1]} now shares {widest[0]} words with contract rule "
        f"{widest[2]}, which "
        f"is at or over the {WINDOW}-word window. Either that application "
        "prose has drifted into a copy, or it needs rewording -- do not "
        "raise the window, which is what makes the copy invisible"
    )
    # RIDER: this assertion is on the MAXIMUM, not per pair, and it is `<=`,
    # so it fires only at 11. Round 1 of #120 measured what that costs: a
    # SECOND definition newly reaching 10 leaves the maximum at 10 and says
    # nothing, and a new near-copy has appeared with the case green. The
    # docstring above records the 10 as one NAMED pair, which is the shape a
    # per-pair check would keep. Nothing shipped broken -- the primary guard
    # at `WINDOW` 15 is intact -- so this is a canary one word less sensitive
    # than its own docstring claims. Measured at both ends of that branch:
    # 10 at the base and 10 at the tip, same pair, so it moved no number and
    # the reviewer did not ask for the assertion to change. If you open this
    # case, decide whether the bound belongs per pair; a fix pass may not add
    # the walk that would answer it.
    assert widest[0] <= LONGEST_KEPT_APPLICATION, (
        f"the longest kept application is now {widest[0]} words "
        f"({widest[1]}, contract rule {widest[2]}), where "
        f"{LONGEST_KEPT_APPLICATION} was "
        "measured at phase 4. The margin under the window is shrinking; "
        "re-measure both ends before this case is the one that fails"
    )
    assert WINDOW < SMALLEST_REAL_DUPLICATION, (
        "the window is at or over the smallest duplication ever measured, so "
        "a real copy can now pass"
    )


# --- the check can fail -----------------------------------------------------


def paste_back(definition, number):
    """A definition with contract rule N's body pasted back in under a new heading.

    This is the orchestrator's mutation of 2026-09-03, in the module rather
    than in a transcript: it is the exact edit a session makes when it
    decides a definition ought to state the rule too."""
    return definition.rstrip("\n") + (
        f"\n\n## What rule {number} states\n\n{SECTIONS[number].strip()}\n"
    )


@pytest.mark.parametrize("number", sorted(SECTIONS))
@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_pasting_a_section_body_back_into_a_definition_is_caught(path, number):
    """Every section, in every definition -- the mutation was run against one
    pair, and a case that only held that pair would be pinning the
    experiment rather than the rule."""
    mutated = paste_back(read(path), number)
    assert copied(SECTIONS[number], mutated), (
        f"contract rule {number} pasted whole into {name(path)} is not caught, "
        "so that rule's body holds no run of "
        f"{WINDOW} words -- it is too short for this check to see"
    )


# --- a rule that moved to ANOTHER DEFINITION does not stay behind either ----

# The same property one axis over. Above, a rule moved into the contract; here,
# three acts moved out of `agents/crafter.md` and into `agents/framer.md` and
# `skills/implement/orchestration.md` (#419). Three documents said the acts
# were not the crafter's while `crafter.md` claimed all three in twenty lines, and
# nothing could see the disagreement — which is the same invisible-in-a-diff
# failure this module opens with.
#
# Named by CONTENT, never by the line range the frame measured them at. The
# waiver example, then a kept application, sat inside that range, so a
# removal keyed on lines would have taken it too.
CRAFTER = os.path.join(ROOT, "agents", "crafter.md")

MOVED_OUT_OF_CRAFTER = {
    "the design gate": (
        "you own this decision, and no skill makes it for you",
        "Ask everything that needs a person here, in one batch",
        # The SECOND copy, sixty lines below the span `plan.md` measured the
        # first at, and the design gate by CONTENT: present approaches and
        # wait for a go. Left standing it would have had the file say `phase 2
        # is your caller's spawn` in one paragraph and `wait for an explicit
        # go` in another. It was removed with the others and held by nothing —
        # round 1 pasted it back and 242 cases stayed green, which makes it
        # the one thing the build found by going past its named span and the
        # one thing the suite could not see come back.
        "wait for an explicit go",
    ),
    "the routing batch": (
        "How the work is routed belongs in that batch",
        "one `multiSelect` question with three checkboxes",
    ),
    "the `routing.md` write": (
        "Write the answer into `seal/threads/<work-item-id>/routing.md`",
    ),
    "the inference that a missing frame proves none was owed": (
        "Where no frame was drawn, the ladder put the work",
    ),
}


def test_the_crafter_claims_no_act_another_definition_owns():
    """S13 and S14's first half. One case per act, so a failure names which.

    A presence-only suite cannot catch this: every one of these sentences
    reads perfectly well, and pasting one back is an edit that only ADDS.
    That is the measurement this module was built on, applied to a move
    between definitions rather than a move into the contract.
    """
    crafter = flat(read(CRAFTER))
    for act, phrases in MOVED_OUT_OF_CRAFTER.items():
        for phrase in phrases:
            assert flat(phrase) not in crafter, (
                f"`agents/crafter.md` carries {act} again: {phrase!r}. Three "
                "other documents own it, and a definition that keeps the "
                "words of an act it does not perform is an instruction to "
                "perform it"
            )


def test_a_citation_is_not_a_copy():
    """The other direction, which matters more than it looks.

    A check that flagged the application forms would be worse than no check:
    the definitions would be rewritten to satisfy it, and what they would
    lose is the half that is actually theirs. So the kept applications are
    named here and asserted clean."""
    kept = {
        ("agents", "proofer.md"): (
            "so it goes through the `Edit` or `Write` tool (rule 9)",
            "whether that label is honest",
            "a row of `## Not judged`",
        ),
        # The crafter's waiver example, its RIDER and its pointer at the
        # retired probe rule left with its rewrite (#967), and the one waiver
        # sentence left with #1027, which removed what it waived.
        ("agents", "crafter.md"): ("hand-back",),
    }
    for parts, phrases in kept.items():
        definition = read(os.path.join(ROOT, *parts))
        haystack = flat(definition)
        for phrase in phrases:
            assert phrase in haystack, (
                f"{'/'.join(parts)} lost its own application: {phrase!r}"
            )
        for number, body in SECTIONS.items():
            assert not copied(body, definition), (
                f"{'/'.join(parts)}'s application prose reads as a copy of "
                f"contract rule {number}"
            )


# --- the proofer's own rules from the 0.22.0 run (#957) -----------------------


def test_the_proofer_checks_its_record_in_the_branch_worktree():
    """The hand-back check reads the tree the record is in (#957 round 1,
    finding 8).

    `chain_check.py`'s `--root` defaults to the session's directory, which is
    the main checkout where the branch has a worktree of its own, so a check
    with no `--root` passes or refuses on files that do not hold the record.
    Every eval case runs in one tree, so none can see it; this case reads the
    command."""
    with open(os.path.join(ROOT, "agents", "proofer.md"), encoding="utf-8") as f:
        text = " ".join(f.read().split())
    # The command the proofer runs at its hand-back, with the `--root` that
    # points it at the branch worktree.
    assert (
        "chain_check.py --baseline <base> --root <the branch worktree> --worktree"
        in text
    ), "the proofer's hand-back check names no `--root`, so it reads the session's tree"


def test_the_proofer_finds_a_missed_statement_on_the_method_of_a_fix():
    """#1472, Scope item 7. Contract rule 12 told the proofer how to read a
    fixing party's account of its own reading; the sentence left the
    contract, which every agent preloads, for the proofer's rule on the
    records a round reads whole. A list the account calls whole, with a
    statement that reading held left out, is a finding on the method even
    where every listed instance was fixed (#1318)."""
    text = flat(read(os.path.join(ROOT, "agents", "proofer.md")))
    lead = (
        "**Every round reads the work item's records that state the present, "
        "whole, against its target.**"
    )
    assert lead in text, "`agents/proofer.md` lost its rule on the records"
    start = text.index(lead)
    rule = text[start : text.index("**A verifying round answers", start)]
    clause = (
        "is a finding on the method, even where every instance on the list was fixed."
    )
    assert clause in rule, f"the proofer's rule on the records lost {clause!r}"


# --- the crafter's own rules from its rewrite (#967) ---------------------------


def crafter_rule(lead):
    """The `## Rules` paragraph of `agents/crafter.md` that opens with **LEAD**,
    as written, or "" where none does."""
    text = read(CRAFTER)
    rules = text[text.index("\n## Rules\n") :]
    for paragraph in rules.split("\n\n"):
        # A lead may wrap across lines, as #1318's does.
        if " ".join(paragraph.split()).startswith(f"**{lead}**"):
            return paragraph
    return ""


# The four rules decision 1 of #967 names, each by its lead and the clauses
# that make it the rule rather than its title. #1027 retired the fourth, *The
# waiver is one command's.*, with the gate it waived.
CRAFTERS_FOUR_RULES = {
    "A new test starts from its group.": (
        "Before writing a case, read the tests of the function it covers",
        "any pair a duplicate check in the repository names",
        "add the case to that group",
    ),
    "Commit before you mutate, and restore from `seal mutate`'s copy.": (
        "A revert through `git checkout -- <file>` restores the committed state",
        "`seal mutate` holds the bytes it read",
    ),
    # #1148 moved the rule to `skills/implement/SKILL.md` *2.*, where a
    # session that builds reads it too; the definition keeps its application.
    "A stop at three failed fixes is handed back.": (
        "`skills/implement/SKILL.md` *2. Implement test-first, and let each rule "
        "name its test*",
        "hand back the architecture question",
    ),
}


def test_the_crafters_four_rules_stand_with_their_enforcers():
    """T3 of #967: S4's rules each keep their paragraph and their clauses.
    #1027 retired the fourth, the waiver, and the case holds that it stays
    gone.

    These three have no eval case that plants their breach, so a later trim
    could drop any of them with every grader green — #107's failure, a rule
    that left the repository while the suite passed."""
    for lead, clauses in CRAFTERS_FOUR_RULES.items():
        paragraph = crafter_rule(lead)
        assert paragraph, f"`agents/crafter.md` lost the rule {lead!r}"
        said = flat(paragraph)
        for clause in clauses:
            assert clause in said, f"{lead!r} lost {clause!r}"
    assert crafter_rule("The waiver is one command's.") == "", (
        "the crafter still states a waiver nothing reads since #1027"
    )


READ_WHOLE = (
    "Before you hand back, your range and the work item's records are read "
    "whole against HEAD."
)


def test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back():
    """#1318, Scope item 2. 35 of the 37 `regression:` findings of 0.27.0 to
    0.30.1 stood in the fixing party's own diff or in its work item's
    records (`frame/design.md` G9), a set closed enough to read whole. So
    after its last commit, in a phase and in a fix pass, the crafter reads
    its range hunk by hunk and the six files that state the present, fixes
    what it writes, names the frame's statements for the orchestrator, and
    calls only the tree-wide search a sample. Step 10 carries that account
    by citing the rule, not by restating it.

    #1472 moved the closed set's reason and the proofer's share out of
    contract rule 12, which every agent preloads, into this rule, which the
    one party that reads the set holds: reading it whole is rule 12's second method,
    and neither a sample's unreached part nor what is not finished is left
    to the proofer."""
    paragraph = crafter_rule(READ_WHOLE)
    # The rule's bold lead, which step 10 and `skills/implement/fix-pass.md`
    # cite in italics and a reader of either resolves here.
    assert paragraph, "`agents/crafter.md` lost its rule on reading the range whole"
    said = flat(paragraph)
    for fact in (
        # The directory whose files the crafter reads whole.
        "`seal/threads/<work-item-id>/`",
        # The command the crafter runs for the other statements of a rule.
        "`git grep`",
        # The file and the heading the crafter writes what it did not finish
        # under.
        "`gaps.md` `## Not done`",
        # The contract rule whose second method the closed set is read by,
        # which the crafter opens.
        "rule 12",
    ):
        assert fact in said, f"the rule lost {fact!r}"
    text = read(CRAFTER)
    order = flat(text[text.index("\n## Order of work\n") : text.index("\n## Never\n")])
    # The citation of the rule in italics, which step 10's reader resolves to
    # the paragraph above.
    assert f"*{READ_WHOLE[:-1]}*" in order, (
        "step 10 no longer cites the rule on reading the range whole"
    )


FIX_PASS_FILE = os.path.join(ROOT, "skills", "implement", "fix-pass.md")
ROUND_RECORD_FORM = os.path.join(ROOT, "docs", "forms", "the-round-record.md")


def test_the_fix_pass_follows_its_own_file_and_the_form_states_the_close_block():
    """The fix pass's procedure stands in `skills/implement/fix-pass.md`,
    which the crafter opens at step 9 (#1471). The file cites the form's two
    paragraphs on the close block, the contract rule a procedure step is read
    under, the field its answer goes in and the crafter's rule on reading the
    range whole; the form states the close block's `verdict:` values and its
    `location:` line. The block's grammar is `lib/fields.py`'s and is held
    there."""
    said = flat(read(FIX_PASS_FILE))
    for fact in (
        # The two sections of the form a fix pass resolves for the close
        # block's values and its `location:` line (#1471).
        "`docs/forms/the-round-record.md` *A finding's `verdict:` decides it, "
        "and severity is for people*",
        "`docs/forms/the-round-record.md` *The fix pass appends one close block "
        "per finding and edits nothing else in the file*",
        # The contract rule a fix pass resolves for the two `seal/` roots a
        # procedure step is read in.
        "contract rule 11",
        # The field the fix pass writes its own wording of a fix into.
        "`answer:`",
        # The crafter's rule a fix pass resolves for the reading it makes
        # after its last fix (#1318).
        f"`agents/crafter.md` *{READ_WHOLE[:-1]}*",
    ):
        assert fact in said, f"`skills/implement/fix-pass.md` lost {fact!r}"
    form = flat(read(ROUND_RECORD_FORM))
    for fact in (
        # The close block's `verdict:` values, which `lib/fields.py` matches.
        "`fixed <commit>`",
        "`rejected`",
        "`deferred <home>`",
        "`deferred <where it was repaired>`",
        # The field a close block carries where its fix went elsewhere.
        "`location:`",
    ):
        assert fact in form, f"`docs/forms/the-round-record.md` lost {fact!r}"
    text = read(CRAFTER)
    order = flat(text[text.index("\n## Order of work\n") : text.index("\n## Never\n")])
    # The path the crafter opens at step 9 in a fix pass.
    assert "`skills/implement/fix-pass.md`" in order, (
        "step 9 no longer sends a fix pass to `skills/implement/fix-pass.md`"
    )


def test_the_crafters_hand_back_names_the_follow_up_file():
    """Round 1 of #967: step 10 hands back what the crafter may not record
    itself, and names the file a leftover goes to, which the orchestrator
    files from."""
    text = read(CRAFTER)
    order = flat(text[text.index("\n## Order of work\n") : text.index("\n## Never\n")])
    # The path `seal/follow-up.md`, the code span, where the orchestrator
    # files a leftover the hand-back names.
    assert "a leftover for `seal/follow-up.md`" in order, (
        "step 10 no longer names the file a leftover goes to"
    )


# --- the tracer's own rules from its rewrite (#970) --------------------------

TRACER = os.path.join(ROOT, "agents", "tracer.md")

# The rule S4 of #970 names, by its lead. Of the tracer's other rules,
# `tests/behaviour/test_a_probe_that_commits_says_so.py` reads one, and the
# orchestrator reads the rest at each tracer report.
GUESSED = "**A guessed original proves nothing.**"


def test_the_tracer_opens_the_parity_skill_and_returns_original_not_found():
    """T3 of #970: the tracer opens `legacy-parity` at step 1, and where no
    original resolves it returns `original not found` instead of asking.

    No case runs the tracer (#957's Q3), so a trim could drop either with
    every grader green. The second is S4: the skill's resolution order ends
    with the caller asking the user, and a subagent has nobody to ask."""
    text = read(TRACER)
    rules = text[text.index("\n## Rules\n") :]
    guessed = next((p for p in rules.split("\n\n") if p.startswith(GUESSED)), "")
    # The words `original not found`, the code span, which the tracer returns
    # and its caller reads as no original resolved.
    assert "return `original not found` naming what was tried, and no findings" in flat(
        guessed
    ), "the rule no longer says what the tracer returns where no original resolves"
    order = flat(text[text.index("\n## Order of work\n") : text.index("\n## Never\n")])
    # The path of the skill the tracer opens at step 1.
    assert order.startswith("## Order of work 1. Open `skills/legacy-parity/SKILL.md`")
