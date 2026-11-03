"""What the agent files say about a probe, now that no gate reads its commit.

Issue #82. A review agent spawned to run round 1 wrote probes that committed
with shell variables, two of them reached a user who was not driving the
session as permission prompts inside five minutes, and the agent was stopped
to end them. The shapes that avoided the prompt became a contract rule, and
#1027 retired it: no gate reads a commit any more, so a probe's commit
reaches nobody. Its number, 8, is one the contract's preamble lists as
retired. What stays is rule 7's: a probe leaves nothing behind, and its
files are edits under rule 9. A commit a probe makes in its clone writes the
clone's path after `git -C`, as rule 6 states and
`tests/behaviour/test_a_commit_names_its_repository.py` holds. The cases
below hold that each definition that once pointed at rule 8 points at what
is left.
"""

from conftest import read


def test_no_definition_points_a_probe_at_the_retired_rule():
    """A pointer at rule 8 now reaches a retired number and no section; each
    definition that had one points at rules 7 and 9."""
    for name in ("proofer.md", "tracer.md", "crafter.md"):
        text = " ".join(read("agents", name).split())
        assert "rule 8" not in text, f"agents/{name} still points at rule 8"


def test_the_reviewer_points_a_probe_at_rules_7_and_9():
    """What stayed in `agents/proofer.md` is the application, not the shapes.

    The proofer edits less than the crafter and would read a rule about edits as
    somebody else's, so its own paragraph points at the two rules. What that
    paragraph says a probe file is, is the orchestrator's to read in the
    proofer's report."""
    proofer = " ".join(read("agents", "proofer.md").split())
    # The contract rule numbers 7 and 9, which the proofer resolves for what
    # a probe leaves and how its files are edited.
    assert "rule 7" in proofer and "rule 9" in proofer, (
        "the pointer went, so the probe rules are reachable only by an agent "
        "that already knows to look for them"
    )


def test_the_procedure_a_reviewer_follows_cites_contract_rule_7():
    """Round 1, finding 1 of #120: contract rule 7 was widened and the skill
    a proofer actually loads still stated the named file as the whole obligation.

    That is contract rule 12 applied to this work item's own headline fix --
    the rule was corrected at its coordinate and the class was not closed. The
    class is enumerable by construction rather than by sweeping: `test_tmp_*`
    appears in exactly two shipped documents, contract rule 7 itself and this
    skill, and every other file that mentions probes either points at rule 7
    (`agents/tracer.md`) or does not state the rule at all.

    The skill is the closer document to the act, and rule 7's own story is a
    reviewer who followed the file half to the letter, deleted its probe files,
    said so in its report, and left a git worktree behind. The document that
    reviewer follows is this one, and its Probes row is the proofer's to read;
    what is pinned is the rule its qualifier cites."""
    skill = " ".join(read("skills", "code-review", "SKILL.md").split())
    # The citation `Contract rule 7`, which the proofer resolves for what a
    # probe's leavings cover.
    assert "Contract rule 7 is about leavings, not files" in skill, (
        "the row's qualifier has no rule behind it, so a reviewer who reads "
        "`everything else it made` has nothing saying what that covers"
    )


def test_the_fact_finder_points_a_probe_at_rule_7():
    """`agents/tracer.md` once carried the three shapes verbatim, then a
    pointer at rule 8. Its rule *Constraints, enums and defaults are read,
    not probed* says what reading settles for an original, which the
    orchestrator reads in the tracer's report, and points at rule 7 for a
    probe it does run."""
    tracer = " ".join(read("agents", "tracer.md").split())
    # The citation `(rule 7)`, which the tracer resolves for what a probe it
    # runs leaves behind.
    assert "leaves nothing behind (rule 7)" in tracer, (
        "the fact-finder can no longer reach the rule for a probe it runs"
    )
