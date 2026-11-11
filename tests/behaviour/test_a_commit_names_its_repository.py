"""An agent commits with its repository written out, in the form the rule names.

The rule came with work item `1790644505` (#662, #665).

The rule stands in `skills/implement/SKILL.md` *2. Implement test-first, and
let each rule name its test*, which the crafter, the session that builds and
the orchestrator read. Every other agent commits too, where a spawn prompt
asks or a probe commits, and no step of theirs opens *2.*, so contract rule
6 states the form in one sentence and points at the rule.

The cases read the rule's lead, the `git -C` form an agent types, the
contract's pointer and the orchestration's citation of the rule. The rule's
reason is the proofer's to read. The rule points at contract rule 9 rather
than restating it.
"""

from conftest import read

IMPLEMENT = ("skills", "implement", "SKILL.md")
ORCHESTRATION = ("skills", "implement", "orchestration.md")
CONTRACT = ("skills", "agent-contract", "SKILL.md")
LEAD = "**A commit names its repository in the command that makes it.**"


def rule():
    """The rule as it stands in IMPLEMENT, from its bold lead through its
    `check:` line, whitespace folded; "" where no paragraph opens with the
    lead."""
    text = read(*IMPLEMENT)
    if LEAD not in text:
        return ""
    start = text.index(LEAD)
    end = text.index("\ncheck: ", start)
    return " ".join(text[start + len(LEAD) : end].split())


def test_the_rule_stands_in_implement_and_names_the_shape():
    body = rule()
    # The bold lead the orchestration and the multi-repository section cite:
    # a party resolving the citation reaches this paragraph.
    assert body, f"`skills/implement/SKILL.md` has no paragraph led by {LEAD}"
    # The command form `git -C <absolute path>`, which every party types when
    # it commits.
    assert "absolute path written out after `git -C`, in a command of its own" in body


def test_it_points_at_the_edit_rule():
    body = rule()
    # The rule number `contract rule 9`, which a party resolves for how a
    # file edit is made.
    assert "contract rule 9" in body


def test_the_contract_points_every_agents_commit_at_the_rule():
    """The framer commits where a spawn prompt asks, and a proofer's,
    sealer's or tracer's probe may commit in its clone. No step of theirs
    opens implement's *2.*, so the contract every agent preloads carries the form
    and the citation."""
    text = " ".join(read(*CONTRACT).split())
    # The command form `git -C`, which every agent writes its repository's
    # absolute path after when it commits.
    assert "`git -C`" in text, (
        "the contract no longer states the commit form every agent types"
    )
    # The citation every agent resolves to reach the rule: the path and the
    # rule's lead in italics.
    assert (
        "`skills/implement/SKILL.md` *A commit names its repository in the "
        "command that makes it*" in text
    ), "the contract no longer points an agent's commit at the rule"


def test_the_orchestration_cites_the_rule():
    """The loop over `$wt`, `$1` and `$d` was the orchestrator's, in all three
    milestone runs on disk. How the orchestration applies the rule to its
    routing files is the proofer's to read."""
    text = " ".join(read(*ORCHESTRATION).split())
    # The citation the orchestrator resolves when it commits its routing
    # files: the path and the rule's lead in italics.
    assert (
        "`skills/implement/SKILL.md` *A commit names its repository in the "
        "command that makes it*" in text
    )
