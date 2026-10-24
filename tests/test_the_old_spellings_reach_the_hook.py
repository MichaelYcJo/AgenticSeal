"""The old consent spellings reach the git hook, for one Bash call only
(#692, `questions.md` P3 answer (a), W6).

`hooks/tokens.py` reads the bare words, and its own case is
`tests/test_tokens.py`'s (#942's phase 6). The case left here holds the commit
gate's `has_marker` and the worktree guard's `has_token` to `tokens.given`
over three corpora, files against each other. `hooks/answers.py` keeps the
words, and the two PreToolUse/PostToolUse gates around them write and clear;
their cases are `tests/test_answers.py`, `tests/test_answer_write.py` and
`tests/test_answer_clear.py`. What a hook does with an answer is
`tests/e2e/commit/test_commit_flow.py`'s.
"""

import sys
from pathlib import Path

import pytest
from conftest import load_hook_module

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hooks"))
import tokens


def _corpora():
    """Every command of the three consent-token corpora: `tokens.given`'s own
    cases, the heredoc commands of its S6 case, and the worktree guard's
    token cases."""
    import tempfile

    import test_worktree_guard as guard_cases
    from test_tokens import TOKEN_CASES, every_case

    commands = [command for command, _ in TOKEN_CASES[0] if command is not None]
    with tempfile.TemporaryDirectory() as scratch:
        commands += list(every_case(Path(scratch)))
    commands += list(guard_cases.TOKEN_COMMANDS)
    commands += [command for command, _ in guard_cases.BODY_TOKENS.values()]
    commands += [command for command, _ in guard_cases.TYPED_BESIDE_A_BODY.values()]
    return commands


@pytest.mark.rule("executed-text-is-read")
def test_the_three_token_reads_answer_as_one():
    """S8 of work item 1791384157 (#868). Over every command of the three
    corpora, the commit gate's `has_marker` and the worktree guard's
    `has_token` answer what `tokens.given` answers, for every known token:
    one reader, so one answer. At `5623d728` each read split the command its
    own way, and `has_marker` fell back to a substring where the split
    failed."""
    gate = load_hook_module("commit-review-gate.py", "crg_one_reader")
    guard = load_hook_module("worktree-guard.py", "wg_one_reader")
    disagree = []
    for command in _corpora():
        given = tokens.given(command)
        for token in tokens.KNOWN:
            answers = (
                token in given,
                gate.has_marker(command, token),
                guard.has_token(command, token),
            )
            if len(set(answers)) > 1:
                disagree.append((command, token, answers))
    assert not disagree, disagree
