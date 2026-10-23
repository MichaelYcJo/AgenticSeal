"""`hooks/tokens.py`, the one reader of a consent token, one class per function.

The bare-word case came from `tests/test_the_old_spellings_reach_the_hook.py`
(#942's phase 6), with `TOKEN_CASES`, which that file's three-reads case still
reads as one of its corpora. How the commit gate and the worktree guard read a
token through this module is each gate's own file's.
"""

import sys

import pytest
from conftest import HOOKS, census_case, load_hook_module

TARGET = "hooks/tokens.py"

# `tokens` imports `hooksession` by its plain name, as the hooks do.
sys.path.insert(0, HOOKS)
tokens = load_hook_module("tokens.py", "tokens_under_test")

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


class Test_module:
    @pytest.mark.rule("how-a-stop-is-put")
    @pytest.mark.parametrize("command, found", TOKEN_CASES[0], ids=TOKEN_CASES[1])
    def test_a_token_is_a_bare_word_and_nothing_else(self, command, found):
        assert tokens.given(command) == found


test_census = census_case(TARGET)
