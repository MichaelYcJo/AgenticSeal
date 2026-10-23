"""A body outside the one heredoc shape is read as shell for whether it
commits, and a waiver inside a body is data (#739, #763, #773).

Work item `1791089603-one-heredoc-shape-the-reader-matches-exactly-is-data`
S4 and S5, and work item `1791119070-a-waiver-inside-a-here-document-body-is-data`
S6. Every case here reads a command with no git and no shell: each row is how
`hooks/one_heredoc.py`, `hooks/cmdline.py` and `hooks/tokens.py` read one
shape, kept for the phase of #942 that rebuilds those modules. What the
commit gate decides on each kind is `tests/test_commit_review_gate.py`'s,
which holds the rest of this file's cases since #942's phase 5;
`tests/test_the_old_spellings_reach_the_hook.py` reads `every_case` below.
"""

import pytest
from conftest import load_hook_module, q
from test_one_heredoc import FAILS

gate = load_hook_module("commit-review-gate.py", "crg_one_heredoc")


def hidden_commit(command):
    """True when the gate reads a commit in COMMAND it cannot place, which is
    what stops it from a declared session directory."""
    found, _clean = gate.commit_invocations(command, "/x/session")
    return any(isinstance(inv.base, gate.Unresolved) for inv in found)


# A string that fails a clause and holds no body the shell reading finds a
# commit in has nothing for the base to stop.
NO_BODY = {"B: no newline at all"}


@pytest.mark.rule("one-heredoc-shape-is-data")
@pytest.mark.parametrize("name", sorted(set(FAILS) - NO_BODY))
def test_a_string_that_fails_one_clause_still_stops(name):
    """S4. Each fails exactly the clause its name gives and carries a
    commit-bearing body, so the gate reads it as at the base, a commit it
    cannot place. Through `main` from a declared session that was a stop."""
    assert gate.one_heredoc.reduce(FAILS[name]) is None, name
    assert hidden_commit(FAILS[name]), name


# --- S5: #760's findings and must-stop lists, rebuilt as fixtures -------------

COMMIT = "git commit -m x"

FINDINGS = {
    "round 2 red 1: a second unquoted body whose $( a backslash-newline splits": (
        f"cat > f.sh <<'A'\n{COMMIT}\nA\ncat <<B\n$\\\n(sh f.sh)\nB"
    ),
    "round 3 red 1: a backslash-newline inside the delimiter word": (
        f"cat > f <<'E\\\nOF'\n{COMMIT}\nEOF"
    ),
    "#763 red 1: a backslash-newline in an unquoted second delimiter": (
        f"cat <<'A'\nbody\nA\ncat <<E\\\nOF\n{COMMIT}\nEOF"
    ),
    "#763 red 1: a backslash-newline splitting the opener": (
        f"cat > f.sh <<'A'\n{COMMIT}\nA\ncat <\\\n<B\nsh f.sh\nB"
    ),
    "post-review red 1: the delimiter plus a CR, then a second opener": (
        f"cat > f <<'EOF'\nEOF\r\nbash <<'B'\n{COMMIT}\nB\nEOF"
    ),
    "post-review red 2: a # tail under a delimiter ending in a blank": (
        f"cat > f <<'EOF '\nEOF #\nbash <<'B'\n{COMMIT}\nB\nEOF "
    ),
    "round 3 yellow 2: a file written over a program the line runs from PATH": (
        f"cat > bin/grep <<'A'\n{COMMIT}\nA\ngrep x f"
    ),
    "post-review yellow 3: gh runs git from PATH": (
        f"cat > git <<'A'\n{COMMIT}\nA\ngh pr ready 1"
    ),
    "post-review yellow 3: ssh -G runs a Match exec": (
        f"cat > cfg <<'A'\n{COMMIT}\nA\nssh -G -F cfg host"
    ),
    "1790635415 r2: a program flag after the heredoc": (
        f"python3 <<'EOF' -c 'import os,sys; os.system(sys.stdin.read())'\n{COMMIT}\nEOF"
    ),
    "1790635415 r2: a bundled -Bc": (
        f"python3 -Bc'import os,sys; os.system(sys.stdin.read())' <<'EOF'\n{COMMIT}\nEOF"
    ),
    "1790635415 r2: $(...) before the program": (
        f"sh -s $(true) python3 <<'EOF'\n{COMMIT}\nEOF"
    ),
    "1790635415 r2: ${...;...} before it": (
        f"sh -s ${{x:-;X=}} python3 - <<'EOF'\n{COMMIT}\nEOF"
    ),
    "1790635415 r3: # glued to a quoted delimiter": (
        f"python3 <<'EOF'#x -c 'import os'\n{COMMIT}\nEOF#x"
    ),
}

# Every consumer, wrapper and construct #760 left read. Each runs its body, or
# can be made to, or is a spelling the one shape does not admit.
CONSUMERS_READ = [
    "bash <<'EOF'",
    "sh -s <<'EOF'",
    "zsh <<'EOF'",
    "cat <<'EOF' | sh",
    "cat <<'EOF' | bash -s",
    "cat <<'EOF' | python3 -",
    "source /dev/stdin <<'EOF'",
    ". /dev/stdin <<'EOF'",
    "exec bash <<'EOF'",
    "sudo bash <<'EOF'",
    "env cat <<'EOF'",
    "command cat <<'EOF'",
    "/bin/cat <<'EOF'",
    "\\cat <<'EOF'",
    "'cat' <<'EOF'",
    "X=1 cat <<'EOF'",
    "$SH <<'EOF'",
    "perl - <<'EOF'",
    "node - <<'EOF'",
    "xargs <<'EOF'",
    "ssh host <<'EOF'",
    "python3 -c 'import sys' <<'EOF'",
    "python3 -Bc'import sys' <<'EOF'",
    "python3 <<'EOF' -c 'import sys'",
    "python3 x.py <<'EOF'",
    "python3 $X <<'EOF'",
    "python3 -u - <<'EOF'",
    "cat 0<<'EOF'",
    "cat 3<<'EOF'",
    "cat <<'EOF' &",
    "cat <<'EOF' >&python3",
    "{ cat; } <<'EOF'",
    "( cat ) <<'EOF'",
    "if true; then cat <<'EOF'",
    "for x in a; do cat <<'EOF'",
    "f() { cat; }; f <<'EOF'",
    "cat <<'EOF' > >(bash)",
    "cat <<'EOF' $(true)",
    "git -c core.hooksPath=/x status; cat <<'EOF'",
    "cat <<'EOF' | git am",
    "cat <<'EOF' | gh extension exec x",
]

FILE_RUNNERS = [
    "bash f.sh",
    "sh f.sh",
    "./f.sh",
    "source f.sh",
    "make",
    "python3 - <<'P'\nimport os; os.system('sh f.sh')\nP",
    "git add f.sh",
    "gh pr create --body-file f.sh",
    "gh pr checkout 1",
    "gh alias import f.sh",
    "gh api repos/x/y --input f.sh",
    "gh pr view 1 --web",
    "gh pr edit 1",
    "cat <(bash f.sh)",
    "echo >(sh f.sh)",
    "echo `sh f.sh`",
    "echo $'\\'' ; sh f.sh ; echo \\'",
    "cat <<B\n$(sh f.sh)\nB",
    "cat <<B\n$\\\n(sh f.sh)\nB",
]

WRITERS = [
    "cat > f.sh <<'EOF'",
    "tee f.sh <<'EOF'",
    "cat <<'EOF' | tee f.sh",
    "cat <<'EOF' &> f.sh",
]

NESTED = [
    "bash <<<\"$(cat <<'EOF'\ngit commit -m x\nEOF\n)\"",
    "source <(cat <<'EOF'\ngit commit -m x\nEOF\n)",
    "eval \"$(cat <<'EOF'\ngit commit -m x\nEOF\n)\"",
    "bash <<'O'\ncat > f <<'I'\ngit commit -m x\nI\nbash f\nO",
    "sh -c \"$(cat <<'EOF'\ngit commit -m x\nEOF\n)\"",
    "git commit -m \"$(cat <<'EOF'\nsubject\nEOF\n)\"; bash <<'B'\ngit commit -m x\nB",
]


def must_stop():
    rows = dict(FINDINGS)
    for head in CONSUMERS_READ:
        rows[f"consumer: {head}"] = f"{head}\n{COMMIT}\nEOF"
    for writer in WRITERS:
        for runner in FILE_RUNNERS:
            rows[f"writer: {writer} / {runner}"] = f"{writer}\n{COMMIT}\nEOF\n{runner}"
    for i, command in enumerate(NESTED):
        rows[f"nested {i}"] = command
    return rows


MUST_STOP = must_stop()


@pytest.mark.rule("one-heredoc-shape-is-data")
@pytest.mark.parametrize("name", sorted(MUST_STOP))
def test_what_760_found_still_stops(name):
    """S5. Green at `e141980a` and after: none of these is the one shape, so
    each body is read as shell, and the commit in it is one the gate cannot
    place. Through `main` from a declared session that was a stop."""
    assert gate.one_heredoc.reduce(MUST_STOP[name]) is None, name
    assert hidden_commit(MUST_STOP[name]), name


# --- #773: a waiver inside a here-document body is data -----------------------
#
# Work item `1791119070-a-waiver-inside-a-here-document-body-is-data`,
# scenario S6. Both consent reads, `has_marker` and `hooks/tokens.py#given`
# for the git hook, read the command without its here-document bodies, and
# only where the base read also found the token. Each command is built from
# named parts -- the opener, the body, the suffix -- and is never run.

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
    # it is `tests/test_commit_review_gate.py::Test_has_marker`'s refusal.
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


# Two commands where taking the body out turns the raw text's split around, so
# the read without bodies finds the token where the base read did not
# (`plan.md` alternative F). Neither is a command a shell would run; each is
# here because the AND is the only thing that refuses it.
#   * the body's lone `"` quotes the token in the raw text; without the body,
#     the quote after the token never closes and the substring fallback reads
#     it (has_marker's half);
#   * the raw text never closes its last quote and reads nothing; without the
#     body, every quote closes and the token is a bare word (given's half).
NEWLY_READ = {
    "has_marker": f'cat <<EOF\n"\nEOF\necho {WAIVER} "',
    "given": f'cat <<EOF\n"\nEOF\necho {WAIVER} "\n"',
}


def base_marker(command):
    """`has_marker` as it stood at `94d7b2e0`: the strict scan over the raw
    command where it splits cleanly, the substring test where it does not."""
    segments, clean = gate.split_segments(command)
    if not clean:
        return WAIVER in command
    return any(tok == WAIVER for toks in segments for tok in toks)


def base_given(command):
    """`tokens.given` as it stood at `94d7b2e0`: the bare words of the raw
    command."""
    found = {w.strip("()") for w in gate.tokens.words(command)}
    return {t for t in gate.tokens.KNOWN if t in found}


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


@pytest.mark.rule("how-a-stop-is-put")
@pytest.mark.rule("executed-text-is-read")
def test_s6_neither_read_honours_a_token_the_base_did_not(tmp_path):
    """S6. For every command above, each read finds a token only where the
    base read found it. `NEWLY_READ` turns red the moment either read drops
    the AND with its base read; the rest are green at `94d7b2e0` by
    definition.

    Since #868 the two reads are one (`has_marker` is `tokens.given`), and
    it reads the words before a split fails, so its base is the two base
    reads together: it finds a token only where one of them did. The
    documented comment with an apostrophe after the waiver is the case the
    strict base `given` refused and `has_marker` read."""
    for command in every_case(tmp_path):
        bases = base_given(command) | ({WAIVER} if base_marker(command) else set())
        assert not gate.has_marker(command, WAIVER) or base_marker(command), command
        assert set(gate.tokens.given(command)) <= bases, command
    assert not base_marker(NEWLY_READ["has_marker"])
    assert not gate.has_marker(NEWLY_READ["has_marker"], WAIVER)
    assert not base_given(NEWLY_READ["given"])
    assert gate.tokens.given(NEWLY_READ["given"]) == ()
