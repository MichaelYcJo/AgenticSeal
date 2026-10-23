"""What `docs/the-commit-gate-inside-git.md` states about the commit gate
inside git (#692).

The commit flow itself, the gate run through real git, is
`tests/e2e/commit/test_commit_flow.py`'s (#942). The two cases left here read
the policy document's prose, and #923 places them.
"""

from pathlib import Path

import pytest


def test_the_policy_names_the_one_session_reader():
    """Contract rule 14, for S4-S6 of work item 1791384157 (#868):
    `docs/the-commit-gate-inside-git.md` names `CLAUDE_PID`, the one test of
    a process's name and the one session variable. Red against
    `5623d728`'s text."""
    path = Path(__file__).resolve().parent.parent / "docs"
    text = " ".join(
        (path / "the-commit-gate-inside-git.md").read_text(encoding="utf-8").split()
    )
    for sentence in (
        "the one session variable the harness exports to every Bash child",
        "`CLAUDE_PID` where the environment carries it, an observed value, and "
        "else its nearest ancestor whose name is `claude`",
        "A process is a Claude session by one test, its executable's basename "
        "is `claude` (`hooks/hooksession.py#is_claude`)",
        "`env -i` empties `CLAUDE_PID` as it empties the session variable",
        # Round 1 of work item 1791384157, yellow 4.
        "it reads `CLAUDE_PID` only where the hook's own "
        "`CLAUDE_CODE_SESSION_ID` is the session it records",
        # S27 of its second reframe, red against `52c72bbe`'s text.
        "A branch-naming rebase reaches `reference-transaction` the same way a "
        "switch does",
    ):
        assert sentence in text, sentence


@pytest.mark.rule("sealed-off-the-branch-refused")
def test_the_policy_states_the_guarantee_refusal_beside_the_arms():
    """Contract rule 14, for `spec.md` S7 and S11-S13 of work item
    1792363231. `docs/the-commit-gate-inside-git.md` states the refusal of a
    `sealed` the history does not hold, beside the arms and as no arm: what it reads and from where, the record it writes,
    the one way on, what it does not judge, and where it does not run; and
    its latency bullet carries phase 6's figures. Red against 2759a60d's
    text, which named no such refusal."""
    path = Path(__file__).resolve().parent.parent / "docs"
    raw = (path / "the-commit-gate-inside-git.md").read_text(encoding="utf-8")
    text = " ".join(raw.split())
    opening = "**Beside the arms, `pre-commit` refuses a commit"
    rule = opening + text.split(opening, 1)[1].split("**`--no-verify` is met", 1)[0]
    for sentence in (
        "**Beside the arms, `pre-commit` refuses a commit that stages a work "
        "item's `sealed` over a commit its own history does not hold, and "
        "records the refusal; it is no arm.**",
        "from the index, with `git show :<path>`",
        "`git merge-base --is-ancestor <target> HEAD` does not exit 0",
        # Round 3 of work item 1792363231, finding 2, a stated limit: a
        # conflicted merge that brings a side's `sealed` is refused, and its
        # way on is `--no-verify`.
        "A commit that concludes a conflicted merge is judged against `HEAD` alone",
        "the way on is `git commit --no-verify`",
        "a new audit of the sealer at HEAD",
        "`<git-common-dir>/specseal-stamp-refused/<id>-<target>`",
        "It does not read the `; earlier run:` chain",
        "no mark, no waiver and no question",
        "Where the stub does not run",
        # Finding 3: the one shape where the stub runs and the row lands.
        "a row an amend folds into the very commit it audited",
    ):
        assert sentence in rule, sentence
    from conftest import rule_carriers

    assert "check: sealed-off-the-branch-refused" in rule
    held = rule_carriers("sealed-off-the-branch-refused")
    for case in (
        "Test_a_sealed_the_branch_does_not_hold.test_refuses_it_inside_the_commit",
        "Test_pre_commit.test_refuses_a_sealed_off_the_history_and_records_the_refusal",
        "Test_guarantee_off_history."
        "test_accepts_every_guarantee_but_one_sealed_off_the_history",
        "Test_queue_for_guarantee.test_a_sealed_committed_past_the_stub_keeps_the_gap",
    ):
        assert case in held, case
    assert (
        "268 ms an ordinary judged commit against 260 ms without it, and 310 ms "
        "against 283 ms for one that stages a `sealed` guarantee"
    ) in text
