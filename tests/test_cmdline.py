"""`hooks/cmdline.py`, the commit gate's reading of a command's text.

Every case here reads a command with no git and no shell, through the commit
gate's `commit_invocations`, which hands the command to this module. The
cases moved here as they stood, under `questions.md` Q1 of #942, and #1014
decides the reading's future.

From `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py`, #942's
phase 6: a body outside the one heredoc shape is read as shell for whether it
commits (#739, #763). Work item
`1791089603-one-heredoc-shape-the-reader-matches-exactly-is-data` S4 and S5.
That file's S6, the waiver inside a body, is `tests/test_tokens.py`'s.
"""

import pytest
from conftest import census_case, load_hook_module
from test_one_heredoc import FAILS

TARGET = "hooks/cmdline.py"

gate = load_hook_module("commit-review-gate.py", "crg_cmdline")


def hidden_commit(command):
    """True when the gate reads a commit in COMMAND it cannot place, which is
    what stops it from a declared session directory."""
    found, _clean = gate.commit_invocations(command, "/x/session")
    return any(isinstance(inv.base, gate.Unresolved) for inv in found)


# A string that fails a clause and holds no body the shell reading finds a
# commit in has nothing for the base to stop.
NO_BODY = {"B: no newline at all"}


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


class Test_module:
    @pytest.mark.rule("one-heredoc-shape-is-data")
    @pytest.mark.parametrize("name", sorted(set(FAILS) - NO_BODY))
    def test_a_string_that_fails_one_clause_still_stops(self, name):
        """S4. Each fails exactly the clause its name gives and carries a
        commit-bearing body, so the gate reads it as at the base, a commit it
        cannot place. Through `main` from a declared session that was a stop."""
        assert gate.one_heredoc.reduce(FAILS[name]) is None, name
        assert hidden_commit(FAILS[name]), name

    @pytest.mark.rule("one-heredoc-shape-is-data")
    @pytest.mark.parametrize("name", sorted(MUST_STOP))
    def test_what_760_found_still_stops(self, name):
        """S5. Green at `e141980a` and after: none of these is the one shape, so
        each body is read as shell, and the commit in it is one the gate cannot
        place. Through `main` from a declared session that was a stop."""
        assert gate.one_heredoc.reduce(MUST_STOP[name]) is None, name
        assert hidden_commit(MUST_STOP[name]), name


test_census = census_case(TARGET)
