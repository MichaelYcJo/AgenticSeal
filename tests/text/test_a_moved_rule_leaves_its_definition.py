"""A rule moved out of a definition does not stay behind in it.

Q2 of #107 answered *full*: `skills/agent-contract/SKILL.md` is the single
home for every universal rule, and each `agents/*.md` keeps only its own
application. That no definition carries a contract rule's own sentences is
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`'s, which reads
every pair of the contract and a definition by runs of
`skills/settle/scripts/passages.py#WINDOW` words; the comment over `WINDOW`
holds the measurement that chose it.

What this module holds is what that check does not read. An act moved out of
`agents/crafter.md` to another file does not come back into it. Each kept
application still names what it cites. And the rules the proofer, the crafter
and the tracer kept from their rewrites (#957, #967, #970) still name what
their readers resolve.

A definition MAY cite a rule by its number and say what the rule means for
its own role, in its own words -- that is the application form, and phases 3
and 4 of #107 kept several deliberately: the proofer's audit of the
`unverified` label, its `## Not judged` row, the #36 cost of a prompt landing
during a round; the crafter's hand-back as the place both answers land. Every
one of those is about one agent, and none of them is the rule. A definition
restating a universal rule in fresh words is a reviewer's finding.
"""

import os

from conftest import ROOT, read, section
from conftest import flattened as flat

# No TARGET: its cases hold the acts and the applications each definition under agents/ keeps, and the rules the proofer, the crafter and the tracer kept from their rewrites.


# --- an act that moved to another file does not stay behind ------------------

# The routing batch moved out of `agents/crafter.md` (#419) and stands in
# `skills/implement/routing-question.md`, and the crafter's *Never* forbids
# the act: "Ask a person anything".
CRAFTER = os.path.join(ROOT, "agents", "crafter.md")

MOVED_OUT_OF_CRAFTER = {
    # The question form `skills/implement/routing-question.md` asks the
    # routing batch in, which a crafter would act on were it written in its
    # definition.
    "the routing batch": ("`multiSelect`",),
}


def test_the_crafter_claims_no_act_another_definition_owns():
    """S13 and S14's first half. One case per act, so a failure names which.

    Pasting the act back is an edit that only ADDS, which a presence-only
    suite cannot catch. Whether a sentence of the crafter's definition hands
    it another act its *Never* forbids is the proofer's to read.
    """
    crafter = flat(read(CRAFTER))
    for act, phrases in MOVED_OUT_OF_CRAFTER.items():
        for phrase in phrases:
            # `agents/crafter.md` *Never*: "Ask a person anything".
            assert flat(phrase) not in crafter, (
                f"`agents/crafter.md` carries {act} again: {phrase!r}. Its "
                "*Never* forbids the act, and a definition that keeps the "
                "words of an act it does not perform is an instruction to "
                "perform it"
            )


def test_a_citation_is_not_a_copy():
    """The other direction, which matters more than it looks.

    A check that flagged the application forms would be worse than no check:
    the definitions would be rewritten to satisfy it, and what they would
    lose is the half that is actually theirs. So what each kept application
    cites is named; that its prose holds no contract rule's own words is the
    paste test's, and its words are the proofer's to read."""
    kept = {
        ("agents", "proofer.md"): (
            # The contract rule number the proofer's application cites.
            "rule 9",
            # The round record's heading the proofer writes a row of.
            "`## Not judged`",
        ),
    }
    for parts, phrases in kept.items():
        haystack = flat(read(os.path.join(ROOT, *parts)))
        for phrase in phrases:
            assert phrase in haystack, (
                f"{'/'.join(parts)} lost its own application: {phrase!r}"
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


def test_the_proofer_keeps_its_rule_on_the_records_a_round_reads_whole():
    """#1472, Scope item 7. Contract rule 12 told the proofer how to read a
    fixing party's account of its own reading; the sentence left the
    contract, which every agent preloads, for the proofer's rule on the
    records a round reads whole (#1318). What the rule says is the proofer's
    to read."""
    text = flat(read(os.path.join(ROOT, "agents", "proofer.md")))
    # The rule's bold lead, which `skills/code-review/orchestration.md` cites
    # in its verifying round's *Target* row and a reader of that row
    # resolves here.
    lead = "**Every round reads the work item's records that state the present"
    assert lead in text, "`agents/proofer.md` lost its rule on the records"


# --- the crafter's own rules from its rewrite (#967) ---------------------------


def crafter_rule(lead):
    """The `## Rules` paragraph of `agents/crafter.md` that opens with **LEAD**,
    as written, or "" where none does."""
    for paragraph in section(read(CRAFTER), "## Rules").split("\n\n"):
        # A lead may wrap across lines, as #1318's does.
        if " ".join(paragraph.split()).startswith(f"**{lead}**"):
            return paragraph
    return ""


# Two of the rules decision 1 of #967 names, each by its lead and what its
# paragraph names that a reader acts on. The rules' words are the proofer's to
# read.
CRAFTERS_RULES = {
    # The lead `skills/verify/scripts/mutation_check.py` cites in italics.
    "Commit before you mutate, and restore from `seal mutate`'s copy.": (
        # The command whose revert the rule warns of, and the command whose
        # copy restores the file.
        "`git checkout -- <file>`",
        "`seal mutate`",
    ),
    # #1148 moved the rule to `skills/implement/SKILL.md` *2.*, where a
    # session that builds reads it too; the definition keeps its application.
    "A stop at three failed fixes is handed back.": (
        # The section the crafter resolves for the rule.
        "`skills/implement/SKILL.md` *2. Implement test-first, and let each rule "
        "name its test*",
    ),
}


def test_the_crafters_rules_name_what_their_readers_resolve():
    """T3 of #967: two of S4's rules each keep their paragraph and what it
    names that a reader acts on.

    These have no eval case that plants their breach, so a later trim could
    drop either with every grader green — #107's failure, a rule that left
    the repository while the suite passed."""
    for lead, facts in CRAFTERS_RULES.items():
        paragraph = crafter_rule(lead)
        assert paragraph, f"`agents/crafter.md` lost the rule {lead!r}"
        said = flat(paragraph)
        for fact in facts:
            assert fact in said, f"{lead!r} lost {fact!r}"


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


NARROW_SET = "\n## The narrow set, then the read of the range\n"


def test_whoever_makes_the_fix_pass_makes_the_reading_of_the_range():
    """#1623, Scope item 1. A fix pass is the crafter's or the
    orchestrator's, and the orchestrator makes every pass of a work item
    whose `routing.md` answers `Implementation` with `the session`. Bound to
    the crafter alone, the reading of the range and the records whole was
    asked of nobody in such a pass, and one fact stated in several records
    was fixed one sentence at a time (owlery#236). So the paragraph binds the
    reading to whoever makes the pass, and says where the orchestrator
    corrects, folds and names what the crafter's *Job* and hand-back give."""
    text = read(FIX_PASS_FILE)
    start = text.index(NARROW_SET)
    section = flat(text[start : text.index("\n## ", start + len(NARROW_SET))])
    for fact in (
        # The routing row and its answer under which the orchestrator makes
        # every pass.
        "`Implementation`",
        "`the session`",
        # The section the orchestrator folds a frame or `routing.md`
        # statement by, as it folds one a crafter's hand-back names.
        "`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*",
        # The field the orchestrator writes the read's account into, in
        # place of the crafter's hand-back.
        "`answer:`",
        # The file and the heading what the pass did not finish goes under.
        "`gaps.md` `## Not done`",
    ):
        assert fact in section, (
            f"*The narrow set, then the read of the range* no longer says {fact!r}"
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
