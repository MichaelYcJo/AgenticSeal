"""What the agent files say about a probe, now that no gate reads its commit.

Issue #82. A review agent spawned to run round 1 wrote probes that committed
with shell variables, two of them reached a user who was not driving the
session as permission prompts inside five minutes, and the agent was stopped
to end them. The shapes that avoided the prompt became contract rule 8, and
#1027 retired that rule: no gate reads a commit any more, so a probe's commit
reaches nobody. What stays is rule 7's: a probe leaves nothing behind, and
its files are edits under rule 9. The cases below hold that each definition
that once pointed at rule 8 points at what is left, and that the old shapes
are gone with it.
"""

import os

from conftest import read
from test_the_agent_contract_holds_the_universal_rules import HEADING

CONTRACT = os.path.join("skills", "agent-contract", "SKILL.md")


def section(number):
    """Rule N's body, so a shape that drifts into another rule is not a pass."""
    text = read(CONTRACT)
    heads = list(HEADING.finditer(text))
    for i, m in enumerate(heads):
        if int(m.group(1)) != number:
            continue
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        return " ".join(text[m.end() : end].split())
    raise AssertionError(f"the contract has no rule {number}")


def test_the_retired_rule_keeps_its_number_and_none_of_its_shapes():
    """#1027. The numbering rule keeps rule 8 as one line; a shape left in it
    would send a probe after a gate that is gone."""
    body = section(8)
    assert "Retired by #1027" in body
    for gone in ("subprocess.run", "git -C /abs/path/r1", "[no-review]", "keyboard"):
        assert gone not in body, f"rule 8 still carries {gone!r}"


def test_no_definition_points_a_probe_at_the_retired_rule():
    """A pointer at rule 8 now reaches one line that says nothing about how
    to probe; each definition that had one points at rules 7 and 9."""
    for name in ("proofer.md", "tracer.md", "crafter.md"):
        text = " ".join(read("agents", name).split())
        assert "rule 8" not in text, f"agents/{name} still points at rule 8"


def test_the_reviewer_still_says_a_probe_file_is_an_edit():
    """What stayed in `agents/proofer.md` is the application, not the shapes.

    The proofer edits less than the crafter and would read a rule about edits as
    somebody else's. Its own paragraph is what says a scratch fixture and a
    patched file are edits too."""
    proofer = " ".join(read("agents", "proofer.md").split())
    assert "rule 7" in proofer and "rule 9" in proofer, (
        "the pointer went, so the probe rules are reachable only by an agent "
        "that already knows to look for them"
    )
    assert "A probe leaves nothing, and its files are edits" in proofer
    for gone in ("reaches no gate", "gives the commit gate a command to read"):
        assert gone not in proofer, f"agents/proofer.md still says {gone!r}"


def test_the_procedure_a_reviewer_follows_carries_the_leavings_rule_too():
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
    reviewer follows is this one."""
    skill = " ".join(read("skills", "code-review", "SKILL.md").split())
    assert "everything else it made goes with it" in skill, (
        "the Probes row states deleting the named file as the whole "
        "obligation again, which is the reading rule 7 was rewritten to end"
    )
    assert "Contract rule 7 is about leavings, not files" in skill, (
        "the row's qualifier has no rule behind it, so a reviewer who reads "
        "`everything else it made` has nothing saying what that covers"
    )


def test_the_fact_finder_reads_first_and_leaves_nothing():
    """`agents/tracer.md` once carried the three shapes verbatim, then a
    pointer at rule 8. Its rule *Constraints, enums and defaults are read,
    not probed* says what reading settles for an original, and points at
    rule 7 for a probe it does run."""
    tracer = " ".join(read("agents", "tracer.md").split())
    assert "read, not probed" in tracer, (
        "the tracer's own half -- what an original settles by reading -- went"
    )
    assert "leaves nothing behind (rule 7)" in tracer, (
        "the fact-finder can no longer reach the rule for a probe it runs"
    )
