"""`hooks/tokens.py`, the one reader of a consent token, one class per function.

The bare-word case came from `tests/test_the_old_spellings_reach_the_hook.py`
(#942's phase 6), with `TOKEN_CASES`, which that file's three-reads case still
reads as one of its corpora. How the worktree guard reads a token through
this module is that gate's own file's.

`Test_module`'s S6 came from
`tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py` (#942's phase
6), with `every_case`, which the three-reads case reads as another corpus: a
waiver inside a here-document body is data, and neither read honours a token
the base read did not (#773).
"""

import shlex
import sys

import pytest
from conftest import HOOKS, census_case, load_hook_module, q

TARGET = "hooks/tokens.py"

# `tokens` imports `hooksession` by its plain name, as the hooks do.
sys.path.insert(0, HOOKS)
tokens = load_hook_module("tokens.py", "tokens_under_test")
cmdline = load_hook_module("cmdline.py", "cmdline_for_the_base_reads")

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


# --- #773: a waiver inside a here-document body is data -----------------------
#
# Work item `1791119070-a-waiver-inside-a-here-document-body-is-data`,
# scenario S6. The consent read, `hooks/tokens.py#given`, reads the command
# without its here-document bodies, and only where the base read also found
# the token. Each command is built from named parts -- the opener, the body,
# the suffix -- and is never run.

WAIVER = "[no-review]"


def commit_into(repo):
    """The suffix every case commits with: a `git -C` the reader can place."""
    return f"git -C {q(repo)} add f && git -C {q(repo)} commit -m x"


def s1_program_body(target):
    """The one shape with the program: a Python string literal holds the
    token, and the suffix commits into `target` (#769 round 1's probe)."""
    body = f'note = "{WAIVER}"\nprint(note)'
    return f"python3 - <<'EOF'\n{body}\nEOF\n{commit_into(target)}"


# Openers the one-shape reader refuses, each feeding a body no shell runs:
# `spec.md` case 3.
OUTSIDE_THE_SHAPE = {
    "a sink with an unquoted delimiter": "cat > {scratch} <<EOF",
    "a sink with a double-quoted delimiter": 'cat > {scratch} <<"EOF"',
    "another interpreter": "python - <<'EOF'",
}


def s2_body_outside_the_shape(opener, scratch, target):
    """An opener `one_heredoc` refuses, the token alone on a body line, and a
    commit after the terminator."""
    return f"{opener.format(scratch=q(scratch))}\n{WAIVER}\nEOF\n{commit_into(target)}"


DOCUMENTED = {
    "the no-op in front, outside the shape": (
        ": '{w}'; cat > {scratch} <<EOF\nbody\nEOF\n{commit}"
    ),
    "a trailing comment after the terminator, outside the shape": (
        "cat > {scratch} <<EOF\nbody\nEOF\n{commit}  # {w}"
    ),
    "a trailing comment on the program's suffix": (
        "python3 - <<'EOF'\nprint(1)\nEOF\n{commit}  # {w}"
    ),
    # #868: an apostrophe AFTER the token in its comment keeps it; one before
    # it reads nothing, `TOKEN_CASES`' "a comment whose apostrophe comes
    # before the token".
    "a trailing comment with an apostrophe after the waiver": (
        "cat > {scratch} <<EOF\nbody\nEOF\n{commit}  # {w} -- it's a probe"
    ),
}


def documented(name, scratch, target):
    return DOCUMENTED[name].format(
        w=WAIVER, scratch=q(scratch), commit=commit_into(target)
    )


def s5_shell_body(target, in_front=False):
    """A body `bash` runs, holding a commit; the token either inside the body,
    in front of that commit, or typed in front of the Bash call's own command."""
    commit = commit_into(target)
    if in_front:
        return f": '{WAIVER}'; bash <<EOF\n{commit}\nEOF\n"
    return f"bash <<EOF\n: '{WAIVER}'; {commit}\nEOF\n"


# A command where taking the body out turns the raw text's split around, so
# the read without bodies finds the token where the base read did not
# (`plan.md` alternative F). It is no command a shell would run, and it is
# here because the AND is the only thing that refuses it: the raw text never
# closes its last quote and reads nothing; without the body, every quote
# closes and the token is a bare word.
NEWLY_READ = {
    "given": f'cat <<EOF\n"\nEOF\necho {WAIVER} "\n"',
}


def base_marker(command):
    """The commit gate's `has_marker` as it stood at `94d7b2e0`: the strict
    scan over the raw command where it splits cleanly, the substring test
    where it does not. Half of the base `given` is held against."""
    segments, clean = cmdline.split_segments(command)
    if not clean:
        return WAIVER in command
    return any(tok == WAIVER for toks in segments for tok in toks)


def base_words(command):
    """Every bare word of `command`, comments included, () for one that does
    not split: the split `given` read at `94d7b2e0`."""
    lexer = shlex.shlex(command or "", posix=True, punctuation_chars=";&|<>")
    lexer.commenters = ""
    lexer.whitespace_split = True
    try:
        return tuple(lexer)
    except ValueError:
        return ()


def base_given(command):
    """`tokens.given` as it stood at `94d7b2e0`: the bare words of the raw
    command."""
    found = {w.strip("()") for w in base_words(command)}
    return {t for t in tokens.KNOWN if t in found}


def every_case(tmp_path):
    scratch, target = tmp_path / "pr.md", tmp_path / "undeclared"
    yield s1_program_body(target)
    for opener in OUTSIDE_THE_SHAPE.values():
        yield s2_body_outside_the_shape(opener, scratch, target)
    for name in DOCUMENTED:
        yield documented(name, scratch, target)
    yield s5_shell_body(target)
    yield s5_shell_body(target, in_front=True)
    yield from NEWLY_READ.values()


class Test_module:
    @pytest.mark.rule("how-a-stop-is-put")
    @pytest.mark.parametrize("command, found", TOKEN_CASES[0], ids=TOKEN_CASES[1])
    def test_a_token_is_a_bare_word_and_nothing_else(self, command, found):
        assert tokens.given(command) == found

    @pytest.mark.rule("how-a-stop-is-put")
    @pytest.mark.rule("executed-text-is-read")
    def test_s6_neither_read_honours_a_token_the_base_did_not(self, tmp_path):
        """S6. For every command above, the read finds a token only where a
        base read found it. `NEWLY_READ` turns red the moment the read drops
        the AND with its base read; the rest are green at `94d7b2e0` by
        definition.

        Since #868 the two reads were one, and it reads the words before a
        split fails, so its base is the two base reads together: it finds a
        token only where one of them did. The documented comment with an
        apostrophe after the waiver is the case the strict base `given`
        refused and the commit gate's `has_marker` read."""
        for command in every_case(tmp_path):
            bases = base_given(command) | ({WAIVER} if base_marker(command) else set())
            assert set(tokens.given(command)) <= bases, command
        assert not base_given(NEWLY_READ["given"])
        assert tokens.given(NEWLY_READ["given"]) == ()


test_census = census_case(TARGET)
