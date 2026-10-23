"""The old consent spellings reach the git hook, for one Bash call only
(#692, `questions.md` P3 answer (a), W6).

`hooks/tokens.py` reads the bare words, and these cases are its, waiting for
the phase of #942 that rebuilds it. `hooks/answers.py` keeps the words, and
the two PreToolUse/PostToolUse gates around them write and clear; their cases
are `tests/test_answers.py`, `tests/test_answer_write.py` and
`tests/test_answer_clear.py`. What a hook does with an answer is
`tests/e2e/commit/test_commit_flow.py`'s.
"""

import sys
from pathlib import Path

import pytest
from conftest import load_hook_module

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "hooks"))
import tokens

TOKEN_CASES = (
    [
        (": '[no-review]'; git commit -m x", ("[no-review]",)),
        ("git worktree add ../wt f  # [worktree-ok]", ("[worktree-ok]",)),
        ("(git worktree add ../wt f [worktree-ok])", ("[worktree-ok]",)),
        (
            ": '[no-review]' '[no-parity]'; git commit -m x",
            ("[no-review]", "[no-parity]"),
        ),
        ('git commit -m "drop [no-review] later"', ()),
        ("git commit -m x[no-review]", ()),
        ("echo 'it''s [no-review]", ()),
        ("git commit -m x", ()),
        # #773, S4: a here-document body is data. Red at `94d7b2e0` for the
        # two body rows; the rest are green there and stay green.
        (
            "python3 - <<'EOF'\nnote = \"[no-review]\"\nEOF\ngit -C ../r commit -m x",
            (),
        ),
        ("cat > f <<EOF\n[no-review]\nEOF\ngit -C ../r commit -m x", ()),
        (
            ": '[no-review]'; cat > f <<EOF\nbody\nEOF\ngit commit -m x",
            ("[no-review]",),
        ),
        ("cat > f <<EOF\nbody\nEOF\ngit commit -m x  # [no-review]", ("[no-review]",)),
        ('cat <<EOF\n"\nEOF\necho [no-review] "\n"', ()),
        (None, ()),
        # #868, phase 1 of work item 1791384157: the words read before a split
        # fails are read, so the documented comment form with an apostrophe
        # after the token keeps its token, and a token inside the quote that
        # never closes is still nothing. Red at `5623d728` for the first two.
        (
            "git switch main 2>&1 | tail -1 # [shared-tree-ok] the release's own tree",
            ("[shared-tree-ok]",),
        ),
        (
            ": '[no-review]'; git commit -q -m x\ncat > f <<'EOF'\nit's\nEOF",
            ("[no-review]",),
        ),
        ("git status  # it's [worktree-ok]", ()),
        ("git commit -m 'x [no-review]", ()),
    ],
    [
        "the no-op form",
        "in a comment",
        "riding a parenthesis",
        "two",
        "inside a message",
        "glued to a word",
        "an unbalanced quote reads nothing",
        "none",
        "in the one shape's program body",
        "in a body outside the shape",
        "the no-op form beside a body",
        "a comment after a body's terminator",
        "a split only the bodiless text finishes reads what the raw text reads",
        "no command at all reads nothing, as at the base",
        "a comment whose apostrophe comes after the token",
        "a body whose apostrophe comes after the typed waiver",
        "a comment whose apostrophe comes before the token",
        "a token inside a quote that never closes",
    ],
)


@pytest.mark.rule("how-a-stop-is-put")
@pytest.mark.parametrize("command, found", TOKEN_CASES[0], ids=TOKEN_CASES[1])
def test_a_token_is_a_bare_word_and_nothing_else(command, found):
    assert tokens.given(command) == found


def _corpora():
    """Every command of the three consent-token corpora: the cases above, the
    commit gate's heredoc cases, and the worktree guard's token cases."""
    import tempfile

    import test_one_heredoc_shape_is_data_to_the_commit_gate as heredoc_cases
    import test_worktree_guard as guard_cases

    commands = [command for command, _ in TOKEN_CASES[0] if command is not None]
    with tempfile.TemporaryDirectory() as scratch:
        commands += list(heredoc_cases.every_case(Path(scratch)))
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
