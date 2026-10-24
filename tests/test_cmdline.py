"""`hooks/cmdline.py`, the commit gate's reading of a command's text, one
class per function the old cases call by name.

Almost every case here reads a command with no git and no shell, through the
reader itself or through the commit gate's `commit_invocations`, which hands
the command to this module; a case of the second kind is `Test_module`'s.
The real-shell rows of `Test_understood` run each construct through bash to
show where it lands, and six cases of `Test_module` run the commit gate over
repositories git made, to show its verdict follows the reading. The cases
moved here as they stood, under `questions.md` Q1 of #942, and #1014 decides
the reading's future. They came from these files, by #942's phase 6:

- `tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py`: a body
  outside the one heredoc shape is read as shell for whether it commits
  (#739, #763), work item
  `1791089603-one-heredoc-shape-the-reader-matches-exactly-is-data` S4 and
  S5. That file's S6, the waiver inside a body, is `tests/test_tokens.py`'s.
- `tests/test_gate_judges_the_repo_it_commits_to.py`: the walk, which
  directory each segment of a command runs in. The commit gate judged the
  shell's cwd and not the repository a `git -C <repo> commit` names, and then
  said nothing for a `-C "$WT"` it could not resolve (#56); an unresolvable
  target now stops the commit.
- `tests/test_a_commit_behind_a_reserved_word_is_judged.py`: a commit written
  after a reserved word on the same line is a commit (#669). Only stricter: a
  reserved word that begins a command list is read past to the command word,
  and where no position names the command word the first `git` stands in and
  the directory is unresolved.
- `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`: a
  commit behind a wrapper that runs its arguments, inside a string a shell is
  handed, or inside a command substitution is a commit (#670, #674, #716,
  #737), each reading in the stricter direction.
- `tests/test_no_shape_the_base_stops_reads_silent.py`: two shapes the commit
  gate's corpus of leaks turned up, read with no git.
- `tests/test_what_the_reader_understands.py`: the reader answered "nothing
  moved" for every construct it did not model (#72); it now enumerates what
  it understands and routes everything else to `Unresolved`. Its constant
  `TARGET = "/target"` is `TARGET_DIR` here, and its `unreadable` keeps its
  name, so the walk file's is `unreadable_flags`.
- `tests/test_a_path_the_command_wrote_out.py`: a name the command assigns
  for itself fills a `$NAME` operand, and nothing guesses at an environment
  this process cannot see. Its `BODIES` is `UNRUN_BODIES` here, beside the
  wrapper file's.

`SHAPES` and `HERE` are read by `tests/test_commit_review_gate.py::Test_main`,
which runs the gate's `main` over the same shapes against real git.
"""

import functools
import os
import shlex
import subprocess
import sys

import pytest
from conftest import (
    HOOKS,
    census_case,
    commit_found,
    decision_of,
    declare_routing,
    fired,
    load_hook_module,
    local_home,
    reason_of,
    sh,
    shell_probe,
)
from conftest import run_gate as run
from test_one_heredoc import FAILS

TARGET = "hooks/cmdline.py"

sys.path.insert(0, HOOKS)
import cmdline  # noqa: E402  -- the plain name the commit gate imports

gate = load_hook_module("commit-review-gate.py", "crg_cmdline")
reader = load_hook_module("cmdline.py", "cmdline_cd")


# --- the shell walk: which directory each segment runs in -----------------


def joined(command):
    """The operator that joined each segment to the one before it."""
    items, clean = reader.split_segments_with_separators(command)
    assert clean, command
    return [sep for sep, _ in items]


def judgment_text(command):
    """`command` as the gate's JUDGMENT read sees it.

    Resolved at call time and tolerant of a `cmdline` that predates the
    function, because these cases are run against older revisions to show
    they were red there. A helper that raises `AttributeError` is not a case
    catching a defect — it is a case that never ran, and counting it as red
    inflates the accounting exactly the way a test that cannot fail inflates
    the green.
    """
    drop = getattr(reader, "drop_heredoc_bodies", None)
    return drop(command) if drop else command


def commit_dirs(command, cwd):
    """Every directory the `git commit` in `command` may run in.

    Through the judgment read, because that is what the gate performs — a
    helper that skipped it would be asking a question no gate asks, and would
    have reported a heredoc body as commands.
    """
    items, clean = reader.split_segments_with_separators(judgment_text(command))
    assert clean, command
    out = []
    for tokens, wheres in reader.walk_directories(items, str(cwd)):
        parsed = reader.parse_git(tokens)
        if parsed and parsed[0] == "commit":
            out.extend(wheres)
    return out


def unreadable_flags(wheres):
    return [isinstance(w, reader.Unresolved) for w in wheres]


# --- what the reader understands (#72) ----------------------------------------
#
# The reader answered "nothing moved" for every construct it did not model,
# which is a confident answer and wrong in both directions at once. It now
# enumerates what it UNDERSTANDS and routes everything else to `Unresolved`,
# which `docs/commit-review-gate-spec.md` treats as a stop. The cases below
# that read through `commit_wheres` are in two halves, and both are load
# bearing: the constructs that must now stop, and the ordinary shapes that
# must not have gained a single candidate.

SESSION = "/session"
TARGET_DIR = "/target"
# `TARGET_DIR` as the READER spells it back, which is not always how it was
# typed.
#
# The two constants are NOT symmetric, and the `windows-latest` job is the only
# thing that says so. `SESSION` is handed to `walk_directories` as the starting
# cwd and comes back untouched, so it answers in the spelling above.
# `TARGET_DIR` is reached through `cd`, and `apply_chdir` normalises, so on
# Windows it answers `\\target`. One run asserted the typed spelling for both
# and eight cases failed; the next asserted the normalised spelling for both
# and twelve did. The runner printed the asymmetry outright --
# `['\\target', '/session']` in one answer list.
#
# The rule the two runs together establish: a directory the reader CONSTRUCTS
# is normalised -- `cd /target`, and `<cwd>/$WT` from `cd "$WT"`, both come back
# with the platform's separator. The cwd it was HANDED is returned as given.
# `test_one_directory_reached_two_ways_stays_two_answers` is the case that
# separates them: it builds `{SESSION}/$WT` and needs the normalised form, and
# its absence from the second run's failures is what proved it.
#
# That mixed spelling is a property of the reader, not of this work item:
# nothing here touches a path separator (the arithmetic scan is
# character-level, the understood check token-level) and it is the same at
# `release/v0.22.0`. It is recorded in `round-4.md` rather than fixed here.
TARGET_READ = os.path.normpath(TARGET_DIR)


def commit_wheres(command, cwd=SESSION):
    """Every directory the `git commit` in `command` may run in.

    Through the judgment read, because that is what both gates perform.
    """
    text = reader.drop_heredoc_bodies(reader.drop_comments(command))
    items, clean = reader.split_segments_with_separators(text)
    assert clean, command
    out = []
    for tokens, wheres in reader.walk_directories(items, cwd):
        parsed = reader.parse_git(tokens)
        if parsed and parsed[0] == "commit":
            out.extend(wheres)
    return out


def unreadable(wheres):
    return [w for w in wheres if isinstance(w, reader.Unresolved)]


# Each row is (name, the command, what a real shell does with the `cd`). The
# third element is what the probe below runs, so the deny is grounded in where
# bash actually lands rather than in an argument about where it might.
MOVES_THE_SHELL = [
    ("a function body", "f() { cd %s; }; f; git commit -m x", "f() { cd %s; }; f"),
    (
        "a spaced function body",
        "f () { cd %s; }; f; git commit -m x",
        "f () { cd %s; }; f",
    ),
    ("an eval", "eval 'cd %s'; git commit -m x", "eval 'cd %s'"),
    ("a pushd", "pushd %s; git commit -m x", "pushd %s >/dev/null"),
    (
        "a for loop",
        "for d in %s; do cd $d; done; git commit -m x",
        "for d in %s; do cd $d; done",
    ),
    (
        "a while loop",
        "while true; do cd %s; break; done; git commit -m x",
        "while true; do cd %s; break; done",
    ),
    ("a sourced script by dot", ". %s/s.sh; git commit -m x", ". %s/s.sh"),
    ("a sourced script by source", "source %s/s.sh; git commit -m x", "source %s/s.sh"),
    ("a wrapper before cd", "command cd %s && git commit -m x", "command cd %s"),
    (
        "a wrapper with an option",
        "command -p cd %s && git commit -m x",
        "command -p cd %s",
    ),
    (
        "a wrapper with an end-of-options",
        "command -- cd %s && git commit -m x",
        "command -- cd %s",
    ),
    (
        "a wrapper around a variable",
        "C=cd; command $C %s && git commit -m x",
        "C=cd; command $C %s",
    ),
]

NAMES = [row[0] for row in MOVES_THE_SHELL]

# The seventeen operators that take a WORD, which is the whole family round 5
# generated. `${x:-((}` has no closing paren, so a reader with no `${…}` state
# ran the arithmetic region to the end of the input.
WORD_TAKING_EXPANSIONS = [
    "${x:-((}",
    "${x-((}",
    "${x:+((}",
    "${x+((}",
    "${y:=((}",
    "${y=((}",
    "${x:?((}",
    "${x?((}",
    "${x#((}",
    "${x##((}",
    "${x%((}",
    "${x%%((}",
    "${x/((/z}",
    "${x//((/z}",
    "${x/z/((}",
    "${x^((}",
    "${x,((}",
]


# --- a path the command wrote out ---------------------------------------------
#
# `SB=/abs/path; git -C "$SB" commit` names its destination twice: once as an
# assignment the readers stepped past, once as a `$SB` the `EXPANDS` test
# calls unresolvable. The reader now keeps the names a command string writes
# for ITSELF, and does not guess at an environment this process cannot see:
# `git -C "$WT"` with no assignment in the string stays unresolvable, and so
# does a loop variable.


def commits(command, cwd=SESSION):
    """[(chdirs, where)] for each `git commit` — what the walk hands the gate.

    `chdirs` are `parse_git`'s `-C` values and `where` is the directory the
    segment's shell is in. Those two are exactly what this change moves, and
    reading them separately is what tells a resolved `-C` apart from a
    resolved `cd`.
    """
    text = reader.drop_heredoc_bodies(reader.drop_comments(command))
    items, clean = reader.split_segments_with_separators(text)
    assert clean, command
    out = []
    for tokens, wheres in reader.walk_directories(items, cwd):
        parsed = reader.parse_git(tokens)
        if parsed and parsed[0] == "commit":
            out.extend((tuple(parsed[2]), where) for where in wheres)
    return out


def targets(command, cwd=SESSION):
    """The directories the commits land in, composed the way the gate does.

    What comes back has been through `apply_chdir`, which ends in
    `os.path.normpath` -- so on Windows `/one` arrives as `\\one`. An expected
    path written as a bare literal is therefore a test that passes on two of
    the three matrix legs and fails on the third: four assertions here did
    exactly that, one of them for two releases. Put the expected value through
    `os.path.normpath` too.
    """
    return [str(reader.compose(where, list(ch))) for ch, where in commits(command, cwd)]


def make_repo(path, opted_in, local=False):
    """A repository with one commit, and `seal/` when it opts in -- under the
    git directory when `local` (#80)."""
    subprocess.run(["git", "init", "-q", str(path)], check=True)
    git = lambda *a: subprocess.run(
        ["git", "-C", str(path), *a], check=True, capture_output=True
    )
    (path / "f.py").write_text("x = 1\n", encoding="utf-8")
    git("add", "-A")
    git("-c", "user.email=e@example.com", "-c", "user.name=e", "commit", "-qm", "base")
    (path / "f.py").write_text("x = 2\n", encoding="utf-8")
    git("add", "-A")
    if opted_in and local:
        local_home(path)
    elif opted_in:
        (path / "seal").mkdir()
    return path


# --- round 1: the reader learned to fill a name and not to empty one ------

FORGETS = [
    # The segment RUNS something, so `_bind` refuses the name -- and refusing
    # to take it is only half. bash has `/two` here and the reader answered
    # `/one`, which is the confident wrong answer the mechanism is bounded to
    # avoid.
    "export SB=/two",
    "declare SB=/two",
    "readonly SB=/two",
    "typeset SB=/two",
    # A construct `understood` rejects. Its effect on a name is no more
    # knowable than its effect on the shell's directory.
    "if true; then SB=/two; fi",
    "for i in 1; do SB=/two; done",
    "while false; do SB=/two; done",
    "eval SB=/two",
    "( SB=/two )",
    # Writes a name with no `=` in the token at all.
    "read SB",
    "read -r SB",
    "mapfile SB",
    "getopts x SB",
    "printf -v SB /two",
    # Round 2: the name-writer check read the segment's FIRST token, so
    # anything in front of the builtin hid it. `IFS= read -r line` is the
    # canonical shell idiom, and `command`/`builtin`/`env` are the spellings
    # that reach past a function of the same name.
    "IFS= read -r SB",
    "command read SB",
    "builtin read SB",
    "env read SB",
    # `unset` does not write a name, it removes one, and to this reader the
    # effect is the same: the earlier value must not survive.
    "unset SB",
    # An assignment operator other than `=`, behind a prefix.
    "export SB+=/two",
    "export SB[0]=/two",
]

BINDS = [
    ('SB=/one; git -C "$SB" commit -m x', "/one"),
    ('SB=/one; true; git -C "$SB" commit -m x', "/one"),
    ('SB=/a SB=/b; git -C "$SB" commit -m x', "/b"),
    ('A=/a; B=$A/x; git -C "$B" commit -m x', "/a/x"),
    ('A1=/a; git -C "$A1" commit -m x', "/a"),
]

# --- round 3: the wide reset was aimed rather than removed -----------------

# What each of these segments can do to a NAME is nothing: it carries none.
# Executed under bash 3.2.57, `SB=/one; <middle>; printf '%s' "$SB"` prints
# `/one` for every one of them, and every one of them prompted after that change,
# where any segment `understood` refused emptied the environment whole.
KEEPS = [
    "if [ -d /nope ]; then echo hi; fi",
    "if true; then echo hi; fi",
    "while [ -d /nope ]; do echo hi; done",
    "until true; do echo hi; done",
    "for i in a b; do echo $i; done",
    "case x in x) echo hi ;; esac",
    "( echo hi )",
    "{ echo hi; }",
    "pushd /tmp",
    "popd",
    "alias ls=ls",
]

# The other side, and it is the side that decides whether the aim was safe.
# Each of these is a segment `understood` refuses that CAN leave a name
# somewhere this reader cannot state.
UNSEEN_FORGETS = [
    # Text this scan never sees. Asked of every word rather than the first,
    # because a structure word puts it second.
    ('eval "SB=/two"', "eval"),
    ('then eval "$x"', "an eval behind a structure word"),
    (". ./lib.sh", "a sourced script"),
    ("source ./lib.sh", "the other spelling of it"),
    ('trap "SB=/two" EXIT', "a trap, which runs later"),
    ('if eval "$x"; then :; fi', "an eval in a condition"),
    # The command word this process cannot read before expansion -- the same
    # refusal `understood` makes for the DIRECTORY, asked here for the name.
    ("then $cmd SB", "an unreadable command word"),
    # A loop writes the name it iterates, once per iteration, and no `=`
    # appears in the segment for `_forget` to find.
    ("for SB in /two /three; do :; done", "a loop over the name itself"),
    ("for ((SB=0; SB<3; SB++)); do :; done", "the arithmetic loop head"),
    ("select SB in /two; do break; done", "`select`, which writes it too"),
    # A name-writing builtin hidden behind structure. `_forget` asks this of
    # the word that RUNS, which is right where the reader knows what runs;
    # here it does not, so it is asked of every word.
    ("f() { read SB; }", "a definition whose body reads"),
    ("function f { read SB; }", "the other spelling of it"),
    ("while read -r SB; do :; done", "the canonical read loop"),
    ("if IFS= read -r SB; then :; fi", "a read in a condition"),
    # Assignments inside the refused segment, which `_forget` does find.
    ("if true; then SB=/two; fi", "an assignment in a branch that may not run"),
    ("{ SB=/two; }", "a brace group, which writes the parent's name"),
    ("( SB=/two )", "a subshell, which does not -- and is forgotten anyway"),
]

# --- a body's later statements are still inside the body -------------------

# Executed under bash 3.2.57: `SB=/one; <middle>; printf '%s' "$SB"` prints
# `/one` for every one of these, because the body never runs -- a false
# condition, an empty list, an arm that does not match, a function defined
# and never called -- or runs in a subshell. Once the reset was aimed the
# reader answered `/three` for all of them: the body's FIRST statement is
# refused with the structure word in front of it, and the SECOND arrives as a
# segment of its own, indistinguishable from a top-level assignment. The wide
# reset had hidden that by accident, because the closer emptied the
# environment, and a closer carries no name. 80 of the 82 fail-opens one
# differential run found against the wide reset were this shape.
UNRUN_BODIES = [
    "if false; then echo hi; SB=/three; fi",
    "if true; then :; else echo hi; SB=/three; fi",
    "while false; do echo hi; SB=/three; done",
    "until true; do echo hi; SB=/three; done",
    "for i in; do echo hi; SB=/three; done",
    "case x in y) echo hi; SB=/three ;; esac",
    "f() { echo hi; SB=/three; }",
    "function f { echo hi; SB=/three; }",
    "( echo hi; SB=/three )",
    "(SB=/two; SB=/three)",
    "if false; then { :; }; SB=/three; fi",
    "if false; then if true; then :; fi; SB=/three; fi",
    # A closer in argument position closes nothing -- bash reads `fi` as a
    # word there, and so does the count. These eight were what was left after
    # the first version counted a closer wherever it stood.
    "if false; then echo fi; SB=/three; fi",
    "f() { echo done; SB=/three; }",
    # The other spellings `_bind` handles, inside a body.
    "if false; then :; export SB=/three; fi",
    "if false; then :; SB+=/x; fi",
    # Round 1 of the re-application. A multi-line `case` puts its arm pattern
    # on a line of its own, and that `a )` is a `)` last in its segment --
    # exactly where a subshell's closer stands. The integer count took it as
    # one and reached zero before the arm body; the stack pops a `)` only when
    # a `(` is on top.
    "case x in\na )\necho hi; SB=/three ;;\nesac",
    "case x in\n(a)\necho hi; SB=/three ;;\nesac",
    "case x in\na)\nSB=/three;;\nesac",
    # The glued spelling: `f(){` is one token, neither in `OPENERS` nor a bare
    # `{`, so nothing opened and the second statement bound.
    "f(){ echo hi; SB=/three; }",
    # A quoted `")"` in argument position, last in its segment, closed the
    # count the same way the arm pattern did.
    'if false; then echo ")"; SB=/three; fi',
    # Nested bodies and an `elif` branch that does not run.
    "if false; then :; elif false; then echo hi; SB=/three; fi",
    "while false; do case x in y) echo hi; SB=/three ;; esac; done",
    # Round 2: inside a subshell body, the spaced `)` of an array, a command
    # substitution or a process substitution is the segment's last token with
    # `(` on top of the stack, and it popped the subshell -- the assignment
    # after it bound at top level. bash: `/one`.
    "( echo hi; OT=( a b ); SB=/three; true )",
    "( echo hi; OT=$( pwd ); SB=/three; true )",
    "( echo hi; cat <( echo x ); SB=/three; true )",
]


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


# --- a commit behind a reserved word (#669) ----------------------------------

C = "git commit -m x"
UNRESOLVED, HERE = "unresolved", "here"

# (command, where its commit is judged). `here` is the directory the shell is
# in, as for any simple command; `unresolved` is what a loop or conditional
# body, a loop condition that runs again, and a construct whose command word
# is not found by position all get.
SHAPES = {
    # #669's three, as the issue names them.
    "for": (f"for d in a; do {C}; done", UNRESOLVED),
    "while": (f"while true; do {C}; break; done", UNRESOLVED),
    "if": (f"if true; then {C}; fi", UNRESOLVED),
    # The rest of the reserved words that begin a command list. Every row
    # ends when it runs, as `while`'s does: the commit gate's S2 replays this
    # table against real git, and an `until false` with no `break` never
    # returned there (#692, after the chain: CI run 36965695916).
    "until": (f"until false; do {C}; break; done", UNRESOLVED),
    "select": (f"select d in a; do {C}; done", UNRESOLVED),
    "else": (f"if false; then :; else {C}; fi", UNRESOLVED),
    "elif": (f"if false; then :; elif {C}; then :; fi", UNRESOLVED),
    "an if condition": (f"if {C}; then :; fi", UNRESOLVED),
    "a while condition": (f"while {C}; do break; done", UNRESOLVED),
    # A group, a subshell, a negation and `time` behind one of them.
    "a group in a body": (f"for d in a; do {{ {C}; }}; done", UNRESOLVED),
    "a subshell in a body": (f"for d in a; do ( {C} ); done", UNRESOLVED),
    "a glued subshell in a body": (f"if true; then ({C}); fi", UNRESOLVED),
    "a negation in a body": (f"if true; then ! {C}; fi", UNRESOLVED),
    "time in a body": (f"for d in a; do time {C}; done", UNRESOLVED),
    "a negated commit": (f"! {C}", HERE),
    # Constructs whose command word is not found by position.
    "a case arm": (f"case x in a) {C};; esac", UNRESOLVED),
    "a later case arm": (f"case x in a) :;; b) {C};; esac", UNRESOLVED),
    "a function body": (f"f() {{ {C}; }}", UNRESOLVED),
    "a spaced function body": (f"f () {{ {C}; }}", UNRESOLVED),
    "a function keyword": (f"function f {{ {C}; }}", UNRESOLVED),
    "a coprocess": (f"coproc {C}", UNRESOLVED),
}

# Round 1 of 1790644505, yellow 4: the same class for `eval`. Each runs its
# `eval` in bash, and each was silent at the base and at `f25c6b1a`, because
# `_eval_argument` read past assignments alone.
EVALS = {
    "then": f"if true; then eval '{C}'; fi",
    "do, over a variable": 'for c in a; do eval "$c"; done',
    "a while condition": f"while eval '{C}'; do break; done",
    "!": f"! eval '{C}'",
    "time": f"time eval '{C}'",
    "command": f"command eval '{C}'",
    "builtin": f"builtin eval '{C}'",
    "a subshell": f"(eval '{C}')",
    "a spaced subshell": f"( eval '{C}' )",
    "a group": f"{{ eval '{C}'; }}",
    # Round 2 of 1790644505: where no position names the command word, the
    # first `eval` stands in, as the first `git` does.
    "a case arm": f"case a in a) eval '{C}';; esac",
    "a case arm over a variable": 'case a in a) eval "$X";; esac',
    "a function body": f"f() {{ eval '{C}'; }}; f",
    "a coprocess": f"coproc eval '{C}'",
}

found = functools.partial(commit_found, gate)

# The same command with the reserved word on a line of its own, which is the
# spelling the base already read.
ACROSS_LINES = {
    "for": f"for d in a; do\n{C}\ndone",
    "while": f"while true; do\n{C}\nbreak\ndone",
    "if": f"if true; then\n{C}\nfi",
    "else": f"if false; then :; else\n{C}\nfi",
    "an if condition": f"if\n{C}\nthen :; fi",
    "a case arm": f"case x in a)\n{C}\n;; esac",
    "a function body": f"f() {{\n{C}\n}}",
}


# --- a commit behind a wrapper or in a substitution (#670) -------------------

# #670's four wrappers and the rest of the enumeration, each in the shape it
# is used in: directly in front of `git` it keeps the directory, behind its
# own operand or option it does not.
WRAPPED = {
    "exec": (f"exec {C}", HERE),
    "nice": (f"nice {C}", HERE),
    "nice -n": (f"nice -n 5 {C}", UNRESOLVED),
    "timeout": (f"timeout 5 {C}", UNRESOLVED),
    "xargs": (f"echo a | xargs {C}", HERE),
    "xargs -I": (f"echo a | xargs -I{{}} {C}", UNRESOLVED),
    "stdbuf": (f"stdbuf -oL {C}", UNRESOLVED),
    "setsid": (f"setsid {C}", HERE),
    "ionice": (f"ionice -c 3 {C}", UNRESOLVED),
    "taskset": (f"taskset 1 {C}", UNRESOLVED),
    "chrt": (f"chrt -i 0 {C}", UNRESOLVED),
    "flock": (f"flock /tmp/l {C}", UNRESOLVED),
    "chroot": (f"chroot / {C}", UNRESOLVED),
    "unshare": (f"unshare -r {C}", UNRESOLVED),
    "nsenter": (f"nsenter -t 1 {C}", UNRESOLVED),
    "prlimit": (f"prlimit --nofile=10 {C}", UNRESOLVED),
    "setpriv": (f"setpriv --reuid=1 {C}", UNRESOLVED),
    "runuser": (f"runuser -u u -- {C}", UNRESOLVED),
    "doas": (f"doas {C}", HERE),
    "pkexec": (f"pkexec {C}", HERE),
    "caffeinate": (f"caffeinate -i {C}", UNRESOLVED),
    "arch": (f"arch -arm64 {C}", UNRESOLVED),
    "strace": (f"strace -f {C}", UNRESOLVED),
    "ltrace": (f"ltrace {C}", HERE),
    "valgrind": (f"valgrind {C}", HERE),
    "gtimeout": (f"gtimeout 5 {C}", UNRESOLVED),
    "gnice": (f"gnice {C}", HERE),
    "gnohup": (f"gnohup {C}", HERE),
    "gstdbuf": (f"gstdbuf -oL {C}", UNRESOLVED),
    "genv": (f"genv -i {C}", UNRESOLVED),
    "gchroot": (f"gchroot / {C}", UNRESOLVED),
    "runcon": (f"runcon -t t {C}", UNRESOLVED),
    "find -exec": (f"find . -name f -exec {C} {{}} +", UNRESOLVED),
    "parallel": (f"parallel {C} ::: a", HERE),
    "watch -n": (f"watch -n 5 {C}", UNRESOLVED),
    "script, argv form": (f"script /dev/null {C}", UNRESOLVED),
    # The five the base already named, behind an option it stopped at.
    "env -i": (f"env -i {C}", UNRESOLVED),
    "sudo -u": (f"sudo -u a {C}", UNRESOLVED),
    "command -p": (f"command -p {C}", UNRESOLVED),
    # zsh's precommand modifiers and `repeat N` (round 1 of 1790660768,
    # yellow 5). zsh 5.9 committed for each.
    "noglob": (f"noglob {C}", HERE),
    "nocorrect": (f"nocorrect {C}", HERE),
    "repeat": (f"repeat 1 {C}", UNRESOLVED),
}

# A string handed to a shell to parse. Its directory is unresolved, as
# `eval`'s already was.
HANDED = {
    "bash -c": f"bash -c '{C}'",
    "sh -c": f'sh -c "{C}"',
    "zsh -c": f"zsh -c '{C}'",
    "dash -c": f"dash -c '{C}'",
    "bash -ec": f"bash -ec '{C}'",
    "bash -o errexit -c": f"bash -o errexit -c '{C}'",
    "sudo sh -c": f"sudo sh -c '{C}'",
    "xargs sh -c": f"echo a | xargs -I{{}} sh -c '{C}'",
    "su -c": f"su - u -c '{C}'",
    "su --command=": f"su --command='{C}' u",
    "script -c": f"script -q -c '{C}' /dev/null",
    "env -S": f"env -S '{C}'",
    "watch, one string": f"watch '{C}'",
    "env -S glued": f"env -S'{C}'",
    "env --split-string=": f"env --split-string='{C}'",
    "a command word the shell expands": 'sh -c "$CMD"',
    "a command in the string behind a list opener": f"bash -c 'if true; then {C}; fi'",
    # #716: `env` splits the string into its OWN arguments, so `-i git commit`
    # runs `env -i git commit`. Each read the string alone as a command whose
    # word is `-i`, and found nothing, at `233f0455`.
    "env -S, env's own words": f"env -S '-i {C}'",
    "env -S glued, env's own words": f"env -S'-i {C}'",
    "env --split-string, env's own words": f"env --split-string '-i {C}'",
    "env --split-string=, env's own words": f"env --split-string='-i {C}'",
    "genv -S, env's own words": f"genv -S '-i {C}'",
    "env -S, the command after the string": "env -S '-i git' commit -m x",
    # Round 1 of 1790993140, yellow 2: a cluster ending in `S`, which macOS
    # `env` accepts, and GNU's abbreviation of `--split-string`. Each found
    # nothing at `07a3dc7f`.
    "env -iS, a cluster": f"env -iS '{C}'",
    "env -vS, a cluster carrying env's own words": f"env -vS '-i {C}'",
    "env -iS glued": f"env -iS'{C}'",
    "env --split, abbreviated": f"env --split '-i {C}'",
    "env --split=, abbreviated": f"env --split='-i {C}'",
    "env -iS behind an option's value": f"env -u FOO -iS '{C}'",
    # Round 2 of 1790993140, yellow 9: GNU's getopt takes a prefix of a long
    # option that takes a value too, so its value is still env's own word.
    # Each found nothing at `f1629706`.
    "env -iS behind --un's value": f"env --un FOO -iS '{C}'",
    "env -iS behind --ch's value": f"env --ch /tmp -iS '{C}'",
    "env --split behind --ar's value": f"env --ar x --split '{C}'",
    # Round 2 of 1790993140, yellow 10: a redirection among env's options is
    # the shell's, and env still reads the cluster after it (macOS `env`,
    # executed by the round). Each found nothing at `f1629706`.
    "env -iS behind a redirection": f"env 2>/dev/null -iS '{C}'",
    "env -iS behind a redirection after a value": f"env -u FOO 2>/dev/null -iS '{C}'",
    "env -iS behind a redirection before a value": f"env -u 2>/dev/null FOO -iS '{C}'",
    "env -vS behind a cut redirection": f"env -i 2>&1 -vS '{C}'",
    # #737: BSD's getopt has `-` among its letters, as `-i`, and reads a word
    # starting `--` with more after it as a cluster led by `-`; macOS `env`
    # runs each string (executed). Each found nothing at `2b1dcb1f`.
    "env -i-S": f"env -i-S '{C}'",
    "env --S": f"env --S '{C}'",
    "env --S behind an option's value": f"env -u FOO --S '{C}'",
    # GNU's `--env0-from` takes a value (coreutils 9.12, read, not run).
    "env -iS behind --env0-from's value": f"env --env0-from f -iS '{C}'",
    # BSD reads `--unset` as `-i -u nset` and `--un` as `-i -u n`, where GNU
    # reads the long option taking the next word; macOS `env` runs each
    # (executed). Reading the word only as GNU does found nothing.
    "env -iS behind BSD's --unset": f"env --unset -iS '{C}'",
    "env -vS behind BSD's --un": f"env --un -vS '{C}'",
}

SUBSTITUTED = {
    "$( )": f"echo $({C})",
    "$( ) in double quotes": f'echo "$({C})"',
    "backticks": f"echo `{C}`",
    "an assignment's value": f"x=$({C}; echo) && ls",
    "<( )": f"cat <({C})",
    ">( )": f"echo a > >({C})",
    "nested": f"echo $(echo $({C}))",
    "a case inside": f"echo $(case x in a) {C};; esac)",
    "inside ${ }": f"echo ${{x:-$({C})}}",
    "inside an arithmetic expansion": f"echo $(( $({C}) ))",
    "inside a heredoc body a shell runs": f"bash <<'EOF'\necho $({C})\nEOF",
    "an unterminated one": f"echo $({C}",
    "a shell string inside a substitution": f"echo $(bash -c '{C}')",
    # #674, phase 1: a host glued to a subshell's `(`, and a commit behind a
    # redirection inside a substitution.
    "(sh -c)": f"(sh -c '{C}')",
    "(bash -c) after a list": f"true; (bash -c '{C}')",
    "a redirected commit in $( )": f"echo $(2>/dev/null {C})",
    # #674, phase 3: the string past a redirection after `env -S`, and the
    # hosts #670's enumeration did not mark. `parallel` runs its arguments
    # through a shell and is read for a commit only (`spec.md` *Scope*).
    "env -S 2>/dev/null": f"env -S 2>/dev/null '{C}'",
    "flock -c": f"flock /tmp/l -c '{C}'",
    "flock --command": f"flock -w 5 /tmp/l --command '{C}'",
    "parallel :::": f"parallel ::: '{C}'",
    "parallel -j2 :::": f"parallel -j2 ::: '{C}'",
    # #674, phase 4: the same, where the splitter cut the redirection.
    "sh -c 2>&1": f"sh -c 2>&1 '{C}'",
    "bash -c 2>&1 before the commit": f"bash -c '2>&1 {C}'",
    "a commit behind 2>&1 in $( )": f"echo $(2>&1 {C})",
}

# What must NOT become a stop: each is either nothing at all or exactly the
# commit it always was, judged where it always was.
CONTROLS = {
    "a single-quoted substitution is text": "echo '$(git commit -m x)'",
    "a message read by a substitution": 'git commit -m "$(cat msg)"',
    "a value read before the commit": "x=$(git rev-parse HEAD) && git commit -m y",
    "a script a shell runs is not its arguments": 'bash run.sh "$x"',
    "a wrapper around no git": "timeout 5 make",
    "arithmetic": "echo $((1+2)) && git commit -m y",
    "a word after for": "for d in git commit; do :; done",
    "a conditional in a shell string": "bash -c '[ -f x ] && echo y'",
    "a group in a shell string": "bash -c '{ echo y; }'",
    # Round 1 of 1790644505, yellow 3: positional parameters no shell runs,
    # and `watch` as a word something else was handed.
    "find -exec sh -c with _ {}": "find . -name '*.py' -exec sh -c 'wc -l \"$1\"' _ {} \\;",
    "find -exec bash -c with bash {} +": "find . -type f -exec bash -c 'echo \"$@\"' bash {} +",
    "bash -c over a glob": 'bash -c \'for f in "$@"; do echo "$f"; done\' _ *.txt',
    "bash -c with an expanded $0": 'bash -c \'echo "$0"\' "$HOME"',
    "grep for watch": "grep -n watch *.py",
    "grep for watch in a substitution's list": "grep -l watch $(git ls-files)",
    "rg for watch": 'rg watch "$DIR"',
    # #674: `watch` as the file a redirection writes to is no program.
    "watch as a redirection's target": '2> watch -g "$CMD"',
    # #674, phase 2: a runner's options inside a string, with nothing after
    # them that expands.
    "a runner's options in a shell string": "sh -c 'nice -n 5 make all'",
    # A `case` word and a `for` list are data, never a program.
    "a case word that expands, in a string": "sh -c 'case $1 in a) echo;; esac' _ a",
    "a case word that expands, before a|b)": "sh -c 'case $1 in a|b) echo;; esac' _ a",
    "a for list that expands, in a string": "sh -c 'for f in $@; do echo; done' _ a",
    # #674, phase 6: a redirection's target is never a command word, so the
    # new readings -- behind a runner, behind a header, the stand-in -- do not
    # count one that expands. The differential corpus found these.
    "a redirection to $LOG behind a runner's options": "sh -c 'nice -n 5 make >\"$LOG\"'",
    "a redirection to $LOG in a function body": "sh -c 'f() { >\"$LOG\" echo hi; }; f'",
    "{fd}> in a case arm": "sh -c 'case a in a) {fd}>f echo hi;; esac'",
    # #716: `env -S`'s string read as env's own words commits nothing where
    # it holds no commit.
    "env -S with no commit": "env -S 'echo hi'",
    "env -S with env's own option and no commit": "env -S '-i true'",
    # Round 1 of 1790993140, yellow 1: env's own words are arguments to
    # `env`, so a variable among them names no command, and a quoted operand
    # stays one word. Each was a deny in a declared repository at `07a3dc7f`
    # and silent at `233f0455`.
    "env -S behind an option's variable value": "env -u \"$V\" -S 'echo hi'",
    "env -S behind a variable directory": "env -C \"$D\" -S 'echo hi'",
    "env -S with a variable operand": "env -S 'echo' \"$X\"",
    "env -S with a quoted operand holding a list": "env -S 'echo' 'a && git commit -m y'",
    "env -S with a quoted operand holding a ;": "env -S 'printf %s' 'x; git commit -m y'",
    # An option's value before the split string reaches `env` as one word too.
    "env -S behind an option value holding a ;": "env -u 'a; git commit -m y' -S 'echo hi'",
    # Round 1 of 1790993140, yellow 2: a cluster ending in `S` after the
    # program is the program's (`ls -lS`), not a split string.
    "a program's own cluster ending in S": 'env ls -lS "$DIR"',
    # Round 2 of 1790993140, white 11: `--` ends env's options, so the word
    # after it is the program `-iS`, not a cluster. A deny at `f1629706`,
    # silent at `233f0455`.
    "a program after env's --": "env -- -iS 'git commit -m y'",
    "a program after env's -- behind an option": "env -i -- -vS 'git commit -m y'",
    # A letter no synopsis has ends the cluster: getopt fails, and env runs
    # nothing, so the `S` after it spells no split string.
    "a cluster holding a letter no synopsis has": "env -xS 'git commit -m y'",
    # #737: `genv` is GNU's env by name, so `--unset` takes `-iS` and the
    # program is the one word `git commit -m x`. BSD's reading is `env`'s.
    "genv's --unset takes the cluster as its value": f"genv --unset -iS '{C}'",
}

# #674: round 1's seven controls, rewritten into each position the work item
# teaches the reader. A program word is read by where it stands, never by
# whether it is present, so a search word and a positional parameter stay what
# they were wherever the command itself is moved to (`spec.md` *How the
# controls stay unasked*). Each is silent at `86256492` and must stay so.
ROUND_1_CONTROLS = (
    "find -exec sh -c with _ {}",
    "find -exec bash -c with bash {} +",
    "bash -c over a glob",
    "bash -c with an expanded $0",
    "grep for watch",
    "grep for watch in a substitution's list",
    "rg for watch",
)
POSITIONS = {
    "P5, behind 2>/dev/null": lambda c: f"2>/dev/null {c}",
    "P5, behind a spaced 2> target": lambda c: f"2> /dev/null {c}",
    "P10, glued to (": lambda c: f"({c})",
    "P7, a case arm": lambda c: f"case a in a) {c};; esac",
    "P7, a later arm": lambda c: f"case a in b) :;; a) {c};; esac",
    "P7, a spaced pattern": lambda c: f"case a in a ) {c};; esac",
    "P8, a function body": lambda c: f"f() {{ {c}; }}; f",
    "P8, a glued subshell body": lambda c: f"f() ({c}); f",
    "P8, function f": lambda c: f"function f {{ {c}; }}; f",
    "P9, a coprocess": lambda c: f"coproc {c}",
    "P6, behind 2>&1": lambda c: f"2>&1 {c}",
    "P6, behind >&2": lambda c: f">&2 {c}",
    "followed by 2>&1": lambda c: f"{c} 2>&1",
    "followed by 2>&1 | tail": lambda c: f"{c} 2>&1 | tail -1",
}
CONTROLS.update(
    {
        f"{name} [{position}]": rewrite(CONTROLS[name])
        for name in ROUND_1_CONTROLS
        for position, rewrite in POSITIONS.items()
    }
)

# The same hosts, where the string they run IS an expansion or holds the
# commit: each must still stop (round 1 of 1790644505, yellow 3's fence).
STILL_HANDED = {
    "sh -c $CMD": 'sh -c "$CMD"',
    "bash -o errexit -c $CMD": 'bash -o errexit -c "$CMD"',
    "su -c $CMD root": 'su -c "$CMD" root',
    "su root -c $CMD": 'su root -c "$CMD"',
    "su --command=$CMD": 'su --command="$CMD" root',
    "watch -n 1 $CMD": 'watch -n 1 "$CMD"',
    "env -S $CMD": 'env -S "$CMD"',
    "sudo sh -c $CMD": 'sudo sh -c "$CMD"',
    "bash -lc $CMD": 'bash -lc "$CMD"',
    "positional parameters that are the commit": "bash -c '\"$@\"' _ git commit -m x",
    # Round 2 of 1790644505: a word before the `-c` flag, and `watch` behind
    # a runner's own options, a list opener or a subshell, used to hide the
    # string.
    "bash --rcfile f -c $CMD": 'bash --rcfile /dev/null -c "$CMD"',
    "bash --init-file f -c $CMD": 'bash --init-file /dev/null -c "$CMD"',
    "bash 2>/dev/null -c $CMD": 'bash 2>/dev/null -c "$CMD"',
    "nice -n 5 watch $CMD": 'nice -n 5 watch -g "$CMD"',
    "timeout 60 watch $CMD": 'timeout 60 watch -g "$CMD"',
    "sudo -E watch $CMD": 'sudo -E watch "$CMD"',
    "then watch $CMD": 'if true; then watch -g "$CMD"; fi',
    "( watch $CMD )": '( watch -g "$CMD" )',
    "! watch $CMD": '! watch -g "$CMD"',
    # #674, phase 1: a program word behind a redirection, and a host glued to
    # the `(` that opens a subshell. Each is silent at `86256492`.
    "2>/dev/null eval $X": '2>/dev/null eval "$X"',
    "2> /dev/null eval $X": '2> /dev/null eval "$X"',
    "2>/dev/null watch $CMD": '2>/dev/null watch -g "$CMD"',
    "2> /dev/null watch $CMD": '2> /dev/null watch -g "$CMD"',
    "<<<x watch $CMD": '<<<x watch -g "$CMD"',
    "sh -c with 2>/dev/null before $CMD": "sh -c '2>/dev/null $CMD'",
    "sh -c with 2> /dev/null before $CMD": "sh -c '2> /dev/null $CMD'",
    "(watch $CMD)": '(watch -g "$CMD")',
    "(sh -c $CMD)": '(sh -c "$CMD")',
    "(nice watch $CMD)": '(nice watch -g "$CMD")',
    # #674, phase 2: `watch` inside a compound command's header -- a `case`
    # arm, a function body, a coprocess -- and a string's command word in the
    # same places or behind a runner's own options. Each is silent at
    # `86256492`, where the program was looked for only at the segment's start.
    "a case arm watch $CMD": 'case a in a) watch -g "$CMD";; esac',
    "a case arm (a) watch $CMD": 'case a in (a) watch -g "$CMD";; esac',
    "a case arm a ) watch $CMD": 'case a in a ) watch -g "$CMD";; esac',
    "a later case arm watch $CMD": 'case a in b) :;; a) watch -g "$CMD";; esac',
    "a case arm a|b) watch $CMD": 'case a in a|b) watch -g "$CMD";; esac',
    "a case arm in a then watch $CMD": (
        'if true; then case a in a) watch -g "$CMD";; esac; fi'
    ),
    "a function body watch $CMD": 'f() { watch -g "$CMD"; }; f',
    "a spaced definition watch $CMD": 'f () { watch -g "$CMD"; }; f',
    "a glued definition watch $CMD": 'f(){ watch -g "$CMD"; }; f',
    "function f watch $CMD": 'function f { watch -g "$CMD"; }; f',
    "function f() watch $CMD": 'function f() { watch -g "$CMD"; }; f',
    "function f () watch $CMD": 'function f () { watch -g "$CMD"; }; f',
    "a subshell body watch $CMD": 'f() ( watch -g "$CMD" ); f',
    "a case in a subshell watch $CMD": '(case a in a) watch -g "$CMD";; esac)',
    "coproc watch $CMD": 'coproc watch -g "$CMD"',
    "coproc NAME { watch $CMD }": 'coproc W { watch -g "$CMD"; }',
    "coproc { watch $CMD }": 'coproc { watch -g "$CMD"; }',
    "sh -c a function body $CMD": "sh -c 'f() { $CMD; }; f'",
    "sh -c a case arm $CMD": "sh -c 'case a in a) $CMD;; esac'",
    "sh -c function f $CMD": "sh -c 'function f { $CMD; }; f'",
    "sh -c coproc $CMD": "sh -c 'coproc $CMD'",
    "sh -c nice -n 5 $CMD": "sh -c 'nice -n 5 $CMD'",
    "sh -c timeout 5 $CMD": "sh -c 'timeout 5 $CMD'",
    "bash -c sudo -u x $CMD": "bash -c 'sudo -u x \"$CMD\"'",
    # #674, phase 3: a redirection written after the flag that hands a host
    # its string, glued or spaced. Round 3 of 1790644505 ran the four `bash`
    # shapes and each landed a commit. Each is silent at `86256492`, where the
    # redirection was taken for the string.
    "bash -c 2>/dev/null $CMD": 'bash -c 2>/dev/null "$CMD"',
    "bash -c 2> /dev/null $CMD": 'bash -c 2> /dev/null "$CMD"',
    "bash -c >/dev/null $CMD": 'bash -c >/dev/null "$CMD"',
    "bash -lc </dev/null $CMD": 'bash -lc </dev/null "$CMD"',
    "watch -g 2>/dev/null $CMD": 'watch -g 2>/dev/null "$CMD"',
    "watch -g 2> /dev/null $CMD": 'watch -g 2> /dev/null "$CMD"',
    "su -c 2>/dev/null $CMD root": 'su -c 2>/dev/null "$CMD" root',
    "su --command 2> /dev/null $CMD root": 'su --command 2> /dev/null "$CMD" root',
    "runuser -c 2>/dev/null $CMD u": 'runuser -c 2>/dev/null "$CMD" u',
    "script -c 2>/dev/null $CMD": 'script -q -c 2>/dev/null "$CMD" /dev/null',
    "env -S 2>/dev/null $CMD": 'env -S 2>/dev/null "$CMD"',
    "env --split-string 2> /dev/null $CMD": 'env --split-string 2> /dev/null "$CMD"',
    # `flock -c` passes its command to the shell with `-c` (util-linux's
    # flock(1), read for #674's Q4).
    "flock -c $CMD": 'flock /tmp/l -c "$CMD"',
    "flock -w 5 --command $CMD": 'flock -w 5 /tmp/l --command "$CMD"',
    "flock --command=$CMD": 'flock /tmp/l --command="$CMD"',
    "flock -c 2>/dev/null $CMD": 'flock /tmp/l -c 2>/dev/null "$CMD"',
    # #674, phase 4: a redirection holding `&` or `|`, which the splitter cuts
    # into a separator. Each is silent at `86256492`, where the string or the
    # program landed in a segment of its own.
    "sh -c 2>&1 $CMD": 'sh -c 2>&1 "$CMD"',
    "sh -c &>/dev/null $CMD": 'sh -c &>/dev/null "$CMD"',
    "sh -c &>>log $CMD": 'sh -c &>>log "$CMD"',
    "sh -c >&2 $CMD": 'sh -c >&2 "$CMD"',
    "bash -c >|/tmp/f $CMD": 'bash -c >|/tmp/f "$CMD"',
    "su -c 2>&1 $CMD root": 'su -c 2>&1 "$CMD" root',
    ">&2 watch $CMD": '>&2 watch -g "$CMD"',
    "<&0 watch $CMD": '<&0 watch -g "$CMD"',
    ">&- eval $X": '>&- eval "$X"',
    "sh -c with 2>&1 before $CMD": "sh -c '2>&1 $CMD'",
    # A stop `86256492` made, kept: read as written, the string's first word
    # is `>$LOG`, and that expands. The readings #674 adds leave redirections
    # out, and this one is the base's and must not.
    "sh -c >$LOG echo, the base's own stop": "sh -c '>\"$LOG\" echo hi'",
}

# #674, phase 1: a commit behind a redirection written in front of `git`, or
# between `git` and its subcommand. A redirection moves no shell, so each
# commit is judged where the shell is, as the same commit without the
# redirection is. Each read as no commit at `86256492`.
REDIRECTED = {
    "2>/dev/null git": f"2>/dev/null {C}",
    "2> /dev/null git": f"2> /dev/null {C}",
    ">/dev/null git": f">/dev/null {C}",
    ">>log git": f">>log {C}",
    "<f git": f"</dev/null {C}",
    "<>f git": f"<>/dev/null {C}",
    "<<<x git": f"<<<x {C}",
    "<<< x git": f"<<< x {C}",
    "<<EOF git": f"<<EOF {C}\nbody\nEOF",
    "<< EOF git": f"<< EOF {C}\nbody\nEOF",
    "<<-EOF git": f"<<-EOF {C}\nbody\n\tEOF",
    "{fd}>f git": f"{{fd}}>/dev/null {C}",
    "zsh >!f git": f">!/dev/null {C}",
    "zsh >>!f git": f">>!/dev/null {C}",
    # Glued, `>!f` also reads as `>` with the target `!f`; spaced, only the
    # operator's own spelling keeps `f` from being read as the program.
    "zsh >! f git": f">! /dev/null {C}",
    "zsh >>! f git": f">>! /dev/null {C}",
    "2> >(tee log) git": f"2> >(tee log) {C}",
    "an assignment, then 2>/dev/null git": f"X=1 2>/dev/null {C}",
    "2>/dev/null, then an assignment": f"2>/dev/null X=1 {C}",
    "git 2>/dev/null commit": "git 2>/dev/null commit -m x",
    "git 2> /dev/null commit": "git 2> /dev/null commit -m x",
    "git -c k=v 2>/dev/null commit": "git -c k=v 2>/dev/null commit -m x",
    # #674, phase 4: cut by the splitter, and glued back by `merged_view`.
    "2>&1 git": f"2>&1 {C}",
    ">&2 git": f">&2 {C}",
    "<&0 git": f"<&0 {C}",
    ">|f git": f">|/dev/null {C}",
    "git 2>&1 commit": "git 2>&1 commit -m x",
    "a chain: >&2 2>&1 git": f">&2 2>&1 {C}",
    # A leading `&>` is a segment that begins with `>f`, read since phase 1.
    "&>f git": f"&>/dev/null {C}",
}

# Behind a redirection AND somewhere else the walk does not place: the
# directory is unresolved for the other reason, as it was without the
# redirection.
REDIRECTED_UNPLACED = {
    "2>/dev/null nice -n 5 git": f"2>/dev/null nice -n 5 {C}",
    "then 2>/dev/null git": f"if true; then 2>/dev/null {C}; fi",
}

# #674, `questions.md` Q3's header half: every header spelling, as the splitter
# hands it back, and the word `header_end` says the command starts at. A
# spelling read by position costs nothing; `UNPLACEABLE` is the stand-in, which
# is a stop. None is a segment that opens with no header at all.
U = "UNPLACEABLE"
HEADERS = {
    "case W in P)": (["case", "a", "in", "a)", "watch"], 4),
    "case W in (P)": (["case", "a", "in", "(a)", "watch"], 4),
    "case W in P )": (["case", "a", "in", "a", ")", "watch"], 5),
    "case W in P, the rest past a |": (["case", "a", "in", "a"], 4),
    "case W, in on the next line": (["case", "a"], 2),
    "in, then a pattern": (["in", "a)", "watch"], 2),
    "a later arm P)": (["b)", "watch"], 1),
    "a later arm P )": (["b", ")", "watch"], 2),
    "a case behind then": (["then", "case", "a", "in", "a)", "watch"], 5),
    "a case glued to (": (["(case", "a", "in", "a)", "watch"], 4),
    "f() {": (["f()", "{", "watch"], 2),
    "f() (": (["f()", "(", "watch"], 2),
    "f() (glued": (["f()", "(watch"], 1),
    "f(), body on the next line": (["f()"], 1),
    "f ()": (["f", "()", "{", "watch"], 3),
    "f(){": (["f(){", "watch"], 1),
    "function f {": (["function", "f", "{", "watch"], 3),
    "function f() {": (["function", "f()", "{", "watch"], 3),
    "function f () {": (["function", "f", "()", "{", "watch"], 4),
    "function f(){": (["function", "f(){", "watch"], 2),
    "function f, body on the next line": (["function", "f"], 2),
    "coproc CMD": (["coproc", "watch"], 1),
    "coproc {": (["coproc", "{", "watch"], 2),
    "coproc (glued": (["coproc", "(watch"], 1),
    "coproc NAME {": (["coproc", "W", "{", "watch"], 3),
    "a case with no in": (["case", "a", "b", "c)"], U),
    "a pattern with no )": (["case", "a", "in", "a", "b", "c"], U),
    "a definition with no body": (["f()", "watch"], U),
    "no header: a program": (["grep", "-n", "watch"], None),
    "no header: case as an argument": (["echo", "case", "a)"], None),
    "no header: a for list": (["for", "x", "in", "a"], None),
}

MERGED = {
    "2>&1": ("a 2>&1 b", ["a", "2>&1", "b"]),
    ">&2": (">&2 a", [">&2", "a"]),
    "<&0": ("<&0 a", ["<&0", "a"]),
    ">&-": ("a >&- b", ["a", ">&-", "b"]),
    ">|f": ("a >|f b", ["a", ">|f", "b"]),
    "&>f after a word": ("a &>f b", ["a", "&>f", "b"]),
    "&>>f after a word": ("a &>>f b", ["a", "&>>f", "b"]),
    "a chain": ("a >&2 2>&1 b", ["a", ">&2", "2>&1", "b"]),
    "{fd}>&1": ("a {fd}>&1 b", ["a", "{fd}>&1", "b"]),
}

SEPARATE = {
    "a background job": ("a & b", []),
    "a pipe": ("a | b", []),
    "a list": ("a && b", []),
    "a redirection with its target, then a job": ("a > f & b", []),
    "&& before a redirection": ("a && >f b", []),
    "|| before a redirection": ("a || >f b", []),
    "; before a redirection": ("a; >f b", []),
    # bash refuses a bare operator before a list operator, and the view does
    # not make one up either.
    "a bare operator before &&": ("a > && b", []),
    "a bare operator before ;": ("a 2> ; b", []),
    "2>&1, then a list": ("a 2>&1 && b", [["a", "2>&1"]]),
}

# --- the readers, one rule each ---------------------------------------------
#
# A body the shell would close later than the reader does loses the commands
# after the early close, and a body it closes earlier reads text as commands.
# Most such misses are covered twice over at the gate -- a later `$(` is
# still found -- so each rule is pinned here on the body itself.

BODIES = {
    "a plain one": ("echo $(a b)", ["a b"]),
    "a `)` in double quotes": ('echo $(printf ")") x', ['printf ")"']),
    "a `)` in single quotes": ("echo $(printf ')') x", ["printf ')'"]),
    "an escaped `)`": ("echo $(printf \\)) x", ["printf \\)"]),
    "a `)` in a heredoc": (
        "echo \"$(cat <<'EOF'\n)\nEOF\nb)\" x",
        ["cat <<'EOF'\n)\nEOF\nb"],
    ),
    "a `)` in a dashed heredoc": (
        "echo \"$(cat <<-'EOF'\n)\n\tEOF\nb)\" x",
        ["cat <<-'EOF'\n)\n\tEOF\nb"],
    ),
    "a case runs to the end": (
        "echo $(case x in a) b;; esac) c",
        ["case x in a) b;; esac) c"],
    ),
    "nested, outermost only": ("echo $(a $(b)) c", ["a $(b)"]),
    "backticks": ("echo `a` `b`", ["a", "b"]),
    "an escaped backtick inside": ("echo `a \\` b` c", ["a \\` b"]),
    "unterminated": ("echo $(a b", ["a b"]),
    "process substitutions": ("cat <(a) >(b)", ["a", "b"]),
    "single quotes are text": ("echo '$(a)' '`b`'", []),
    "a quoted `<(` is text": ('echo "<(a)"', []),
    "a herestring opens no heredoc": ('echo $(cat <<< "a" ; b) c', ['cat <<< "a" ; b']),
    "an apostrophe in double quotes is not a quote": ('echo "it\'s $(a)"', ["a"]),
    "a double-quoted `$(` runs": ('echo "$(a)"', ["a"]),
    "an escaped `$(` is text": ("echo \\$(a) b", []),
}

TEXTS = {
    "bash -c": (["bash", "-c", "a b"], ["a b"]),
    "a cluster holding c": (["bash", "-ec", "a b"], ["a b"]),
    "every non-option word once -c is given": (
        ["bash", "-o", "errexit", "-c", "a b"],
        ["errexit", "a b"],
    ),
    "no -c: a script, not a string": (["bash", "run.sh", "a b"], []),
    "su --command=": (["su", "--command=a b", "u"], ["u", "a b"]),
    "su --command, separate": (["su", "--command", "a b"], ["a b"]),
    "--command is su's, not a shell's": (["bash", "--command", "a b"], []),
    "watch": (["watch", "-n", "5", "a b"], ["5", "a b"]),
    # #716: the string is also read as `env`'s own words, beside the string
    # alone. The base text stays first, so every answer it gave is kept.
    "env -S": (["env", "-S", "a b"], ["a b", "env a b"]),
    "env -S glued": (["env", "-Sa b"], ["a b", "env a b"]),
    "env --split-string=": (["env", "--split-string=a b"], ["a b", "env a b"]),
    "env -S, the words around it": (
        ["env", "-v", "-S", "-i a", "b"],
        ["-i a", "env -v -i a b"],
    ),
    "env -S past a redirection": (
        ["env", "-S", "2>/dev/null", "a b", "c"],
        ["2>/dev/null", "a b", "env a b c"],
    ),
    "env -S behind a redirection": (
        ["env", "2>", "/dev/null", "-S", "a b"],
        ["a b", "env a b"],
    ),
    "env -S with no string after its redirection": (
        ["env", "-S", "2>/dev/null"],
        ["2>/dev/null"],
    ),
    "behind a runner": (["sudo", "sh", "-c", "a b"], ["a b"]),
}

# Round 1 of 1790660768, yellows 3-6: shapes a real shell commits that read as
# no commit at both `86256492` and `befe53cd`. Each was run in bash 3.2.57 or
# zsh 5.9 and made a commit.
STILL_UNREAD = {
    # yellow 4: a redirection glued to the END of a word.
    "git>/dev/null": "git>/dev/null commit -m x",
    "commit>/dev/null": "git commit>/dev/null -m x",
    "git>&2, cut at &": "git>&2 commit -m x",
    "git<&0, cut at &": "git<&0 commit -m x",
    "(git>/dev/null": "(git>/dev/null commit -m x)",
    "nice>/dev/null": "nice>/dev/null git commit -m x",
    "env>/dev/null": "env>/dev/null git commit -m x",
    "eval>/dev/null": 'eval>/dev/null "$X"',
    "sh>/dev/null -c": 'sh>/dev/null -c "$CMD"',
    # The same, inside text the gate reads again as commands: a shell's
    # string, a heredoc body a shell runs, and a string whose runner hides an
    # expanding command word.
    "git>/dev/null in sh -c": "sh -c 'git>/dev/null commit -m x'",
    "git>/dev/null in a heredoc": "bash <<'EOF'\ngit>/dev/null commit -m x\nEOF",
    "nice>/dev/null $CMD in sh -c": "sh -c 'nice>/dev/null $CMD'",
    # yellow 5: zsh.
    "for i (1)": "for i (1) git commit -m x",
    "for i (1) { }": "for i (1) { git commit -m x }",
    "repeat 1 { }": "repeat 1 { git commit -m x }",
    "repeat 2 eval": 'repeat 2 eval "$X"',
    # yellow 6: the string past `--` and options behind a redirection.
    "bash -c 2>/dev/null --": 'bash -c 2>/dev/null -- "$CMD"',
    "bash -c 2>&1 --": 'bash -c 2>&1 -- "$CMD"',
    "bash -c 2>/dev/null -e": 'bash -c 2>/dev/null -e "$CMD"',
    "sh -c 2>/dev/null +x": 'sh -c 2>/dev/null +x "$CMD"',
    "bash -c 2>/dev/null -O extglob": 'bash -c 2>/dev/null -O extglob "$CMD"',
}

# yellows 3-5 in the walk: a `cd` the shell runs that the walk read as
# staying put. From a declared session, the commit lands in U, which declares
# nothing, and each read silent at both SHAs.
UNSEEN_CD = [
    "2>&1 cd {u} && git commit -m x",
    ">&2 cd {u} && git commit -m x",
    ">|f cd {u} && git commit -m x",
    "<&0 cd {u} && git commit -m x",
    ">&- cd {u} && git commit -m x",
    "2>&1 pushd {u} && git commit -m x",
    "cd>/dev/null {u} && git commit -m x",
    "pushd>/dev/null {u} && git commit -m x",
    "noglob cd {u} && git commit -m x",
    "nocorrect cd {u} && git commit -m x",
    "repeat 1 cd {u} && git commit -m x",
]

# #716: git's global options that take their value as a SEPARATE word. Each
# was run as `git <option> <value> status` on git 2.54.0 in a scratch
# repository, and status ran for exactly these (`phases/phase-1.md`, M1). The
# last three were missing from `_git_options`, so the value read as the
# subcommand and the commit behind it was no commit.
SPACED_OPTIONS = {
    "-C": ".",
    "-c": "a.b=c",
    "--git-dir": ".git",
    "--work-tree": ".",
    "--namespace": "n",
    "--config-env": "core.hooksPath=VAR",
    "--attr-source": "HEAD",
    "--shallow-file": "x",
}

# Round 2 of 1790993140: `env`'s option grammar, one case per row of
# `cmdline.ENV_OPTIONS`. Written from GNU coreutils' `src/env.c` and FreeBSD's
# `usr.bin/env/env.c` (#737), not from the table: each spelling, with the
# value its source gives it, stands in front of a cluster that hides a commit.
# A flag read as taking a value eats the cluster, and an option with a value
# read as a flag ends env's options at its value; either way the commit is
# found by nothing.
# GNU env is not installed here, so its half is read, not run.
ENV_SPELLINGS = {
    "-i": "-i",
    "-0": "-0",
    "-v": "-v",
    "-u": "-u FOO",
    "-C": "-C /tmp",
    "-S": "-S '-i true'",
    "-a": "-a x",
    "-P": "-P /bin",
    "-L": "-L user",
    "-U": "-U user",
    "--ignore-environment": "--ignore-environment",
    "--null": "--null",
    "--debug": "--debug",
    "--unset": "--unset FOO",
    "--chdir": "--chdir /tmp",
    "--split-string": "--split-string '-i true'",
    "--argv0": "--argv0 x",
    "--block-signal": "--block-signal",
    "--default-signal": "--default-signal",
    "--ignore-signal": "--ignore-signal",
    "--list-signal-handling": "--list-signal-handling",
    "--env0-from": "--env0-from f",
    "--quoting-style": "--quoting-style shell",
    "--help": "--help",
    "--version": "--version",
}

# The same grammar's other spellings: a value attached, an abbreviation, a
# cluster holding a value, and a redirection before, between and after.
ENV_GRAMMAR = {
    "a value after =": "--unset=FOO",
    "an optional value after =": "--block-signal=INT",
    "a value glued to its letter": "-uFOO",
    "a cluster ending in a letter with a value": "-iu FOO",
    "an abbreviation with a value": "--un FOO",
    "an abbreviation with no value": "--ign",
    "a lone -": "-",
    "a redirection before the options": "2>/dev/null -i",
    "a redirection between an option and its value": "-u 2>/dev/null FOO",
    "a redirection between two options": "-u FOO 2>/dev/null -0",
    "a redirection after the options": "-i 2> /dev/null",
}


# --- two shapes the commit gate's corpus of leaks turned up ------------------

BODY = "git commit -m x"


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

    def test_the_old_splitter_answers_exactly_what_it_always_did(self):
        """Three call sites read the two-element tuple; the separator arrives
        beside it rather than inside it."""
        assert reader.split_segments("cd /tmp/x && git commit") == (
            [["cd", "/tmp/x"], ["git", "commit"]],
            True,
        )

    @pytest.mark.parametrize("name", sorted(EVALS))
    def test_an_eval_behind_the_same_words_is_read(self, name, tmp_path):
        """Seen red at `f25c6b1a`, where each returned nothing."""
        assert found(EVALS[name], tmp_path), name

    @pytest.mark.parametrize("name", sorted(SHAPES))
    def test_the_commit_is_read(self, name, tmp_path):
        """Seen red at `ade83e4e`, where every one of these returned nothing."""
        command, where = SHAPES[name]
        invocations = found(command, tmp_path)
        assert invocations, f"{name}: no commit read in {command!r}"
        for inv in invocations:
            unresolved = isinstance(inv.base, cmdline.Unresolved)
            assert unresolved == (where == UNRESOLVED), (name, inv.base)

    def test_the_one_line_spelling_is_judged_as_the_multi_line_one(self, tmp_path):
        """The base always judged a body written across lines. The same body on
        one line is now judged the same way, which is the argument that the new
        reading invents nothing. The multi-line half passes at the base too."""
        for name, multi in ACROSS_LINES.items():
            one = [type(i.base) for i in found(SHAPES[name][0], tmp_path)]
            many = [type(i.base) for i in found(multi, tmp_path)]
            assert many == [cmdline.Unresolved], (name, "the base's own reading moved")
            assert one == many, name

    def test_a_directory_already_unreadable_keeps_its_reason(self, tmp_path):
        """An expanded value the walk already could not read stays a VALUE, so the
        stop still tells the model to write the path out rather than naming a
        construct it did not meet."""
        (inv,) = found('cd "$WT" && if git commit -m x; then :; fi', tmp_path)
        assert isinstance(inv.base, cmdline.Unresolved)
        assert inv.base.why == cmdline.Unresolved.VALUE

    def test_a_reserved_word_that_begins_no_command_list_reads_nothing(self, tmp_path):
        """The words after `for`, `select`, `case` and `in` are names and words,
        and a closer ends a list. Nothing here is a command, so nothing is read."""
        for command in (
            "for d in git commit; do :; done",
            "select d in git commit; do :; done",
            "[[ git == commit ]]",
            "echo git commit",
        ):
            assert not found(command, tmp_path), command

    @pytest.mark.parametrize("name", sorted(WRAPPED))
    def test_a_wrapped_commit_is_read(self, name, tmp_path):
        """Seen red at `768377bf`, where each returned nothing."""
        command, where = WRAPPED[name]
        invocations = found(command, tmp_path)
        assert invocations, f"{name}: no commit read in {command!r}"
        for inv in invocations:
            unresolved = isinstance(inv.base, cmdline.Unresolved)
            assert unresolved == (where == UNRESOLVED), (name, inv.base)

    @pytest.mark.parametrize("name", sorted({**HANDED, **SUBSTITUTED}))
    def test_a_commit_in_a_string_or_a_substitution_is_read_as_unreadable(
        self, name, tmp_path
    ):
        """Seen red at `768377bf`, where each returned nothing."""
        command = {**HANDED, **SUBSTITUTED}[name]
        invocations = found(command, tmp_path)
        assert invocations, f"{name}: no commit read in {command!r}"
        assert any(isinstance(inv.base, cmdline.Unresolved) for inv in invocations), (
            name
        )

    def test_every_enumerated_wrapper_has_a_shape(self):
        """The enumeration is the set, and every member of it is exercised here.
        A wrapper added to `RUNNERS` with no shape is a reading nothing pins."""
        named = {name.split()[0].rstrip(",") for name in WRAPPED}
        missing = sorted(
            set(cmdline.RUNNERS) - named - set(cmdline.WRAPPERS) - {"time"}
        )
        assert not missing, missing

    @pytest.mark.parametrize("name", sorted(REDIRECTED))
    def test_a_commit_behind_a_redirection_is_read_where_the_shell_is(
        self, name, tmp_path
    ):
        """Seen red at `86256492`, where each returned nothing."""
        invocations = found(REDIRECTED[name], tmp_path)
        assert invocations, f"{name}: no commit read"
        for inv in invocations:
            assert not isinstance(inv.base, cmdline.Unresolved), (name, inv.base)

    @pytest.mark.parametrize("name", sorted(REDIRECTED_UNPLACED))
    def test_a_commit_behind_a_redirection_and_a_construct_is_unplaced(
        self, name, tmp_path
    ):
        invocations = found(REDIRECTED_UNPLACED[name], tmp_path)
        assert invocations, f"{name}: no commit read"
        assert all(isinstance(inv.base, cmdline.Unresolved) for inv in invocations), (
            name
        )

    def test_a_redirection_whose_target_is_named_git_still_reads_as_git(self, tmp_path):
        """`spec.md` decision 1. `2>/x/git commit` reads as a git invocation at
        `86256492`, because the reader took the whole word's last component.
        Reading past every redirection would read it as none, so the base's answer
        is kept wherever it found one."""
        assert found("2>/x/git commit -m x", tmp_path)

    def test_a_string_behind_a_runners_operand_stops_as_the_frame_chose(self, tmp_path):
        """`spec.md` (b). Behind a runner's own option or operand the reader cannot
        tell a value from the program, so a later word that expands counts, and a
        positional parameter handed to `wc` is such a word. The frame counted this
        as a cost rather than a defect (`plan.md` Alternatives F)."""
        command = "sh -c 'timeout 5 wc -l \"$1\"' _ f"
        assert found(command, tmp_path), command

    def test_sudo_s_does_not_hand_a_quoted_string_to_its_shell_as_a_command_line(
        self, tmp_path
    ):
        """#674, `questions.md` Q4, answered *not as stated* from `man sudo`
        (1.9.17p2): with `-s` or `-i`, "the command and any args are concatenated,
        separated by spaces, after escaping each character (including white
        space) with a backslash … except for alphanumerics, underscores, hyphens,
        and dollar signs". So `sudo -s 'git commit -m x'` reaches the shell as one
        word, not a command line, and `sudo` is not a string host. The argv form
        does run a commit, and `sudo`'s runner reading already finds it."""
        assert not found("sudo -s 'git commit -m x'", tmp_path)
        assert found("sudo -s git commit -m x", tmp_path)

    def test_a_commit_the_splitter_already_found_is_not_found_twice(self, tmp_path):
        """`spec.md` S6's control. `git commit -m x 2>&1 | tail -1` finds its
        commit in the part before the cut, exactly as at `86256492`, and the
        merged view adds nothing: the list is the base's list, `2>` and all."""
        invocations = found("git commit -m x 2>&1 | tail -1", tmp_path)
        assert [(list(inv.args), list(inv.chdirs)) for inv in invocations] == [
            (["-m", "x", "2>"], [])
        ]
        assert not isinstance(invocations[0].base, cmdline.Unresolved)

    @pytest.mark.parametrize("name", sorted(STILL_HANDED))
    def test_a_string_that_is_an_expansion_is_read_as_unreadable(self, name, tmp_path):
        """Each was a deny in a declared repository through the gate's `main`, and
        an unplaced commit is what that deny reads; `main`'s half is
        `tests/test_commit_review_gate.py::Test_main`'s."""
        invocations = found(STILL_HANDED[name], tmp_path)
        assert any(isinstance(inv.base, cmdline.Unresolved) for inv in invocations), (
            name
        )

    def test_the_controls_read_no_hidden_commit(self, tmp_path):
        for name, command in CONTROLS.items():
            hidden = [
                inv
                for inv in found(command, tmp_path)
                if isinstance(inv.base, cmdline.Unresolved)
            ]
            assert not hidden, name

    @pytest.mark.parametrize("name", sorted(BODIES))
    def test_substitution_bodies(self, name):
        command, bodies = BODIES[name]
        assert cmdline.substitution_bodies(command) == bodies, name

    @pytest.mark.parametrize("name", sorted(TEXTS))
    def test_reparsed_texts(self, name):
        tokens, texts = TEXTS[name]
        assert cmdline.reparsed_texts(tokens) == texts, name

    @pytest.mark.parametrize("name", sorted(STILL_UNREAD))
    def test_a_shape_both_shas_read_as_no_commit_is_read(self, name, tmp_path):
        """Seen red at `3b8522c3`, where each returned nothing."""
        assert found(STILL_UNREAD[name], tmp_path), name

    @pytest.mark.parametrize("shape", UNSEEN_CD)
    def test_a_cd_the_walk_did_not_see_is_read_as_leaving(self, shape, tmp_path):
        """Seen red at `3b8522c3`, where each was silent through the gate's `main`
        from a declared session. A commit read as landing in U, or as unplaced,
        is what makes that stop; `main`'s half is
        `tests/test_commit_review_gate.py::Test_main`'s."""
        session = str(tmp_path / "session")
        command = shape.format(u=tmp_path / "u")
        assert any(
            isinstance(inv.base, cmdline.Unresolved) or inv.base != session
            for inv in found(command, session)
        ), command

    @pytest.mark.parametrize("option", sorted(SPACED_OPTIONS))
    def test_a_commit_behind_a_spaced_global_option_is_read(self, option, tmp_path):
        """Seen red at `233f0455` for `--config-env`, `--attr-source` and
        `--shallow-file`, where each returned nothing."""
        value = SPACED_OPTIONS[option]
        assert found(f"git {option} {value} commit -m x", tmp_path), option
        assert not found(f"git {option} {value} status", tmp_path), option

    def test_every_row_of_the_env_grammar_has_a_case(self):
        rows = set()
        for short, long, _value in cmdline.ENV_OPTIONS:
            rows |= {f"-{short}"} if short else set()
            rows |= {long} if long else set()
        assert rows == set(ENV_SPELLINGS), rows ^ set(ENV_SPELLINGS)

    @pytest.mark.parametrize("name", sorted({**ENV_SPELLINGS, **ENV_GRAMMAR}))
    def test_a_cluster_behind_env_s_own_options_is_read(self, name, tmp_path):
        """Each found nothing at `f1629706` where the row's value, a redirection,
        an abbreviation or the cluster's value is what ended env's options."""
        spelling = {**ENV_SPELLINGS, **ENV_GRAMMAR}[name]
        command = f"env {spelling} -vS '{C}'"
        assert found(command, tmp_path), command

    def test_the_split_string_after_the_options_is_read_past_a_redirection(
        self, tmp_path
    ):
        assert found(f"env -iS 2>/dev/null '{C}'", tmp_path)
        assert found(f"env --spl 2>/dev/null '{C}'", tmp_path)

    def test_an_ambiguous_prefix_names_no_long_option(self):
        """GNU's getopt refuses a prefix of two long names (`--i`, `--d`), and env
        then runs nothing; one long name's prefix is that name."""
        assert cmdline._env_long("--i", True) is None
        assert cmdline._env_long("--d", True) is None
        assert cmdline._env_long("--un", True) == "--unset"
        assert cmdline._env_long("--un", False) is None

    def test_the_gate_reaches_a_repository_the_command_named_for_itself(self, tmp_path):
        """S2 at the gate, in the direction that costs a prompt today.

        The shell sits in a repository that never opted in; the commit lands in
        one that did. Written out, that stops. Written as an assignment and a
        `$SB`, it used to resolve to a directory that exists nowhere — so the gate
        asked about a path the user never typed instead of about the repository.
        """
        here = make_repo(tmp_path / "plain", opted_in=False)
        there = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run(f'SB={sh(there)}; git -C "$SB" commit -m x', here, session="named")
        assert fired(out)
        assert str(there) in reason_of(out), (
            "the verdict is about the repository the commit lands in"
        )

    def test_a_declaration_silences_the_name_the_way_it_silences_the_path(
        self, tmp_path
    ):
        """S1's other direction, and the one the original probes measured: the repository
        IS declared, so the written-out form is silent and the named form asked."""
        here = make_repo(tmp_path / "plain", opted_in=False)
        there = make_repo(tmp_path / "opted-in", opted_in=True)
        declare_routing(there)
        out = run(f'SB={sh(there)}; git -C "$SB" commit -m x', here, session="declared")
        assert decision_of(out) == "silent", (
            f"{there} carries a declaration; the gate judged a path nobody typed"
        )

    def test_the_named_form_answers_what_the_written_out_form_answers(self, tmp_path):
        """Byte-identical, because the two commands reach the same repository.

        Comparing the two prompts is what catches a fix that resolves the target
        and then describes it differently — a user reading the two would have no
        way to tell that one command is the other one written out.
        """
        here = make_repo(tmp_path / "plain", opted_in=False)
        there = make_repo(tmp_path / "opted-in", opted_in=True)
        written = run(f"git -C {sh(there)} commit -m x", here, session="written")
        named = run(f'SB={sh(there)}; git -C "$SB" commit -m x', here, session="named2")
        assert decision_of(written) == decision_of(named) == "deny"
        assert reason_of(written) == reason_of(named)

    def test_a_cd_to_a_named_path_reaches_the_same_repository(self, tmp_path):
        """The `cd` operand at the gate, which is the second of the two call
        sites the spec names."""
        here = make_repo(tmp_path / "plain", opted_in=False)
        there = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run(f'SB={sh(there)}; cd "$SB" && git commit -m x', here, session="cd")
        assert fired(out)
        assert str(there) in reason_of(out)

    def test_an_environment_name_still_stops_the_gate(self, tmp_path):
        """S3 at the gate. The environment-variable answer must not move: the gate has no way
        to know what `$WT` holds, and a silence there is indistinguishable from a
        repository checked and found clean."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        declare_routing(here)
        assert fired(run('git -C "$WT" commit -m x', here, session="env")), (
            "the reader answered for a value only the user's shell holds"
        )

    def test_the_aimed_reset_moves_the_gates_verdict_and_only_where_it_should(
        self, tmp_path
    ):
        """The reader's answer is not the deliverable; the gate's verdict is.

        Measured on two real repositories, both carrying a routing declaration,
        with the session sitting in one of them. At `b76fd99` all eight shapes
        below returned `deny`, naming a `$SB` the user never typed. Six of them
        carry no name and now return `silent`, which is the answer the same
        command written out has always had. The two that CAN write a name still
        deny, and that is the half of the measurement that matters.
        """
        here = make_repo(tmp_path / "session", opted_in=True)
        there = make_repo(tmp_path / "opted-in", opted_in=True)
        declare_routing(here)
        declare_routing(there)
        for at, shape in enumerate(KEEPS[:6]):
            command = f'SB={sh(there)}; {shape}; git -C "$SB" commit -m x'
            out = run(command, here, session=f"kept{at}")
            assert decision_of(out) == "silent", (
                f"`{shape}` carries no name, `{there}` is declared, and the gate "
                f"asked about a path nobody typed: {reason_of(out)}"
            )
        for at, shape in enumerate(
            ("if [ -d /nope ]; then SB=/two; fi", 'eval "SB=/two"')
        ):
            command = f'SB={sh(there)}; {shape}; git -C "$SB" commit -m x'
            out = run(command, here, session=f"lost{at}")
            assert decision_of(out) == "deny", (
                f"`{shape}` can write the name, and the gate passed a commit "
                "whose repository this reader cannot name"
            )

    def test_a_structure_word_does_not_hide_the_command_that_runs(self):
        """`_runs` reads past the compound-command structure to the word that
        actually runs, and `understood`'s two exceptions come with it: `[` and
        `[[` hold characters `EXPANDS` lists and are conditionals rather than
        globs. Without them `if [ -d <x> ]` empties the environment again, which
        is the shape this round exists to keep."""
        assert reader._runs(shlex.split("then echo hi")) == "echo"
        assert reader._runs(shlex.split("if [ -d /nope ]")) == "["
        assert reader._runs(shlex.split("f() { read SB")) == "read"
        assert reader._runs(shlex.split("fi")) is None
        # `case WORD in` -- the word is data being matched, not a command, so an
        # unreadable one says nothing about what ran.
        assert reader._runs(shlex.split("case $HOME in")) is None

    def test_what_opens_a_body_and_what_closes_one(self):
        def after(segment, stack=()):
            return reader._nesting(shlex.split(segment), list(stack))

        assert after("for ((SB=0") == ["for"]
        assert after("k++))") == []
        assert after("(cd /x") == ["("]
        assert after("case x in x)") == ["case"]
        assert after("( echo hi )") == []
        assert after("} > out", ["{"]) == []
        assert after("echo fi done esac", ["if"]) == ["if"]
        assert after("then if true", ["if"]) == ["if", "if"]
        # A `)` closes only a `(`: a multi-line arm pattern and a quoted `")"`
        # inside a `case` or an `if` close nothing.
        assert after("a )", ["case"]) == ["case"]
        assert after('echo ")"', ["if"]) == ["if"]
        # And every closer pops only its own opener.
        assert after("fi", ["case"]) == ["case"]
        # The glued function head opens a `{` body.
        assert after("f(){ echo hi") == ["{"]
        assert after("function f {") == ["{"]
        # Openers count in command position only.
        assert after('git commit -m "(wip) x"') == []
        assert after("grep -c '(' f") == []
        assert after("time { echo") == ["{"]
        assert after("! ( cd /x )") == []
        # A `)` that belongs to the segment's own `SB=(` or `$(` leaves the
        # subshell on the stack; at top level it closes nothing either way.
        assert after("OT=( a b )", ["("]) == ["("]
        assert after("OT=$( pwd )", ["("]) == ["("]
        assert after("cat <( echo x )", ["("]) == ["("]
        assert after("X=$( pwd )") == []


class Test_split_segments_with_separators:
    def test_accepts_the_operator_that_joined_two_segments(self):
        """`&&` and `||` are opposites in a shell and were indistinguishable here.

        Measured on the unfixed module: all three forms returned
        `[['cd','/tmp/x'], ['git','commit']]`, so a design judging only the `cd`
        destination would judge the wrong repository with confidence on `||`, and
        one judging every reachable directory would keep asking about the
        session's own on `&&`.
        """
        for sep in ("&&", ";", "||", "|"):
            assert joined(f"cd /tmp/x {sep} git commit") == ["", sep], sep

    def test_an_operator_at_the_end_of_a_line_is_still_that_operator(self, tmp_path):
        """A newline behind an operator glued itself onto it.

        The newline is converted to `;` character by character, and shlex groups a
        RUN of punctuation into ONE token — so `cd <B> ||` followed by a newline
        arrived as the single token `||;`, which is in neither `BRANCHING` nor the
        plain-`;` path. Measured tokens: `||;`, `|;`, `&;`.

        Writing the operator at the end of the line is the ordinary way to write a
        long command, so this is the common form rather than a constructed one,
        and it was silent where the commit before this work item stopped it.
        """
        b = tmp_path / "b"
        for sep in ("||", "|", "|&", "&"):
            items, clean = reader.split_segments_with_separators(
                f"cd {sh(b)} {sep}\ngit commit -m x"
            )
            assert clean
            assert [s for s, _ in items] == ["", sep], (
                f"{sep} followed by a newline arrived as one glued token"
            )
            got = [
                str(w)
                for w in commit_dirs(f"cd {sh(b)} {sep}\ngit commit -m x", tmp_path)
            ]
            assert str(tmp_path) in got, (
                f"{sep}: the session's own directory dropped out"
            )

    def test_refuses_the_newline_after_an_operator_as_the_one_that_binds(
        self, tmp_path
    ):
        """`&&` at the end of a line is `&&`, not the newline that follows it."""
        b = tmp_path / "b"
        items, _ = reader.split_segments_with_separators(
            f"cd {sh(b)} &&\ngit commit -m x"
        )
        assert [s for s, _ in items] == ["", "&&"]


class Test_walk_directories:
    def test_accepts_a_cd_as_carrying_the_commit_that_follows_it(self, tmp_path):
        """`&&` runs the commit only where the `cd` arrived, so B is the answer."""
        assert commit_dirs(f"cd {sh(tmp_path / 'b')} && git commit -m x", tmp_path) == [
            str(tmp_path / "b")
        ]

    def test_a_semicolon_carries_the_commit_to_both(self, tmp_path):
        """`;` is not `&&`, and this loop used to run both through one assertion.

        `;` runs what follows whether the `cd` succeeded or not, so a failed `cd`
        leaves the commit in the directory the shell was already in -- executed:
        `bash -c 'cd /no/such/dir ; pwd'` prints the directory it started in. The
        row was added beside the `&&` one with no grounds and pinned the defect as
        the expected answer; issue #72 names it, and this is the assertion that
        replaces it.
        """
        assert commit_dirs(f"cd {sh(tmp_path / 'b')} ; git commit -m x", tmp_path) == [
            str(tmp_path / "b"),
            str(tmp_path),
        ]

    def test_a_relative_cd_composes_against_the_directory_the_shell_is_in(
        self, tmp_path
    ):
        assert commit_dirs("cd sub && git commit -m x", tmp_path) == [
            str(tmp_path / "sub")
        ]

    def test_a_command_with_no_cd_still_answers_the_shells_own_directory(
        self, tmp_path
    ):
        assert commit_dirs("git commit -m x", tmp_path) == [str(tmp_path)]

    def test_or_reaches_the_directory_the_cd_did_not_leave(self, tmp_path):
        """`cd X || git commit` commits where the shell already was, and the
        session's own directory is what a reader dropping the operator loses."""
        assert commit_dirs(f"cd {sh(tmp_path / 'b')} || git commit -m x", tmp_path) == [
            str(tmp_path),
            str(tmp_path / "b"),
        ]

    def test_a_pipeline_does_not_move_the_shell_that_commits(self, tmp_path):
        """Both sides of a pipeline run in subshells, so a `cd` in one does not
        move the shell the next command runs in.

        Executed: `bash -c 'cd <B> | pwd'` from `<A>` prints `<A>`. The reader
        treated `|` as ordinary sequencing and answered `<B>` alone, so a commit
        landing in the session's own repository was judged against a repository it
        never touches — and where that other repository carried a routing
        declaration, the arm went silent. `&` was already branching for exactly
        this reason; `|` and `|&` have the same property and did not get the same
        answer.
        """
        b = tmp_path / "b"
        for sep in ("|", "|&"):
            got = [
                str(w)
                for w in commit_dirs(f"cd {sh(b)} {sep} git commit -m x", tmp_path)
            ]
            assert str(tmp_path) in got, f"{sep}: the shell never left {tmp_path}"
            assert str(b) in got, f"{sep}: a shell with `lastpipe` set does land there"

    def test_a_branch_that_skips_a_cd_keeps_the_directory_it_skipped_from(
        self, tmp_path
    ):
        """`cd N || cd B && git commit` reaches N and B, and the reader kept
        neither of them for the right reason.

        If the first `cd` works the second is skipped and the commit lands in N;
        if it fails the commit lands in B. The union was formed by looking only at
        the operator that FOLLOWS a segment, so the second `cd` overwrote it and N
        stopped being a candidate. A segment joined by a branching operator may
        never run, so the states in front of it have to survive past it.
        """
        n, b = tmp_path / "n", tmp_path / "b"
        got = [
            str(w)
            for w in commit_dirs(
                f"cd {sh(n)} || cd {sh(b)} && git commit -m x", tmp_path
            )
        ]
        assert str(n) in got, "the branch where the second cd is skipped"
        assert str(b) in got, "the branch where the first cd failed"

    def test_a_heredoc_body_is_data_and_not_commands(self, tmp_path):
        """Writing a script and then committing it is ordinary, and the script is
        not a command the shell runs.

        A newline was unconditionally a segment separator, so a `cd` written INSIDE
        a heredoc body moved the reader's shell and the commit two lines later was
        judged against a repository the shell never entered. The session's own
        directory was not in the candidate list at all — this is not over-collecting
        and missing, it is being confidently wrong.

        `drop_comments` in the same module exists for the same reason: a JUDGMENT
        read has to drop what the shell will not execute.
        """
        b = tmp_path / "b"
        for opener in ("<<'EOF'", '<<"EOF"', "<<EOF", "<<-EOF"):
            command = (
                f"cat > run.sh {opener}\n"
                f"cd {sh(b)}\n"
                "make\n"
                "EOF\n"
                "git add -A && git commit -m x"
            )
            got = [str(w) for w in commit_dirs(command, tmp_path)]
            assert got == [str(tmp_path)], f"{opener}: {got}"

    def test_a_herestring_is_not_a_heredoc(self, tmp_path):
        """`<<<` feeds one word to stdin and opens no body, so nothing after it
        may be swallowed."""
        got = [str(w) for w in commit_dirs("cat <<<hello\ngit commit -m x", tmp_path)]
        assert got == [str(tmp_path)], got

    def test_a_failure_branch_survives_an_intervening_segment(self, tmp_path):
        """`cd <B> && make || git commit` commits where the shell is when the `cd`
        fails, and that is the session's own directory.

        Only the IMMEDIATELY next operator was consulted, so one segment between
        the `cd` and the `||` dropped the failure branch entirely. It is the
        mirror of what round 2's tagging closed, one operator further along.
        """
        b = tmp_path / "b"
        for middle in ("make", "test -f x", "git add -A", "npm run build && lint"):
            got = [
                str(w)
                for w in commit_dirs(
                    f"cd {sh(b)} && {middle} || git commit -m x", tmp_path
                )
            ]
            assert str(tmp_path) in got, f"{middle}: {got}"

    def test_the_common_cross_repository_form_gains_nothing(self, tmp_path):
        """The cost the other option would have charged, pinned so it cannot be
        paid by accident.

        `cd <repo> && git commit` is the shape this work item exists to make
        silent when the target is declared, and it is the prompt-flood direction
        issue #45 named. Carrying the failure branch must not put the session's
        own directory back into this answer.
        """
        b = tmp_path / "b"
        assert [
            str(w) for w in commit_dirs(f"cd {sh(b)} && git commit -m x", tmp_path)
        ] == [str(b)]
        # The `;` form belongs to `test_a_semicolon_carries_the_commit_to_both`
        # above and not here. `;` runs what follows whether the `cd` worked or
        # not, so a failed `cd` leaves the commit in the session's own directory,
        # and issue #72 closed that — it is a second candidate the reader offers
        # on purpose, not the cost this case exists to keep at zero.

    def test_a_line_continuation_leaves_the_destination_readable(self, tmp_path):
        """A long command wrapped across lines is the same command.

        An escaped newline survived as a character inside the token, so `cd` read
        as a two-argument `cd` and the destination fell to unreadable. It errs
        toward stopping, but a command that passes on one line was blocked for
        being wrapped.
        """
        b = tmp_path / "b"
        got = commit_dirs(f"cd {sh(b)} \\\n&& git commit -m x", tmp_path)
        assert [str(w) for w in got] == [str(b)], got
        assert not any(isinstance(w, reader.Unresolved) for w in got)

    def test_two_exclusive_branches_are_not_walked_as_one(self, tmp_path):
        """`cd build || cd dist` reaches build OR dist, never `build/dist`.

        The second `cd` was applied to the state the FIRST one produced, so the
        reader offered a directory no run of the command can reach. It is
        fail-closed — an extra candidate is judged rather than missed — but the
        cost is not zero: a composed path exists nowhere, so it enters the
        unreadable partition, and that partition returns before the real verdict
        is used. The phantom then replaces the answer in the prompt.
        """
        got = [
            str(w)
            for w in commit_dirs("cd build || cd dist && git commit -m x", tmp_path)
        ]
        assert str(tmp_path / "build" / "dist") not in got, (
            "a directory no shell run can reach was offered as a candidate"
        )
        assert str(tmp_path / "build") in got and str(tmp_path / "dist") in got

    def test_a_skipped_branch_does_not_execute_the_next_one(self, tmp_path):
        """The tag that makes the case above work, asserted on its own.

        A state that arrived by a branch that SUCCEEDED must not run a segment
        joined by `||`, and one that arrived by a branch that FAILED must not run
        a segment joined by `&&`.
        """
        got = [
            str(w)
            for w in commit_dirs("cd a || cd b || cd c && git commit -m x", tmp_path)
        ]
        for name in ("a", "b", "c"):
            assert str(tmp_path / name) in got, name
        assert str(tmp_path) not in got, (
            "with every cd failing the `&&` never runs, so the session's own "
            "directory is not a landing place"
        )
        assert len(got) == 3, got

    def test_the_candidate_count_stays_linear_in_the_branches(self, tmp_path):
        """Measured before the fix: 16 segments produced 65536 candidates and a
        non-git command took 5.8 seconds. Each `||` adds one landing place, so the
        count is the number of branches rather than two to its power."""
        command = " || ".join(f"cd d{i}" for i in range(16)) + " && git commit -m x"
        got = commit_dirs(command, tmp_path)
        assert len(got) <= 20, f"{len(got)} candidates from 16 branches"

    def test_a_command_the_reader_cannot_bound_is_unreadable_rather_than_slow(
        self,
        tmp_path,
    ):
        """The cap, which is containment and not a fix.

        Three shapes still multiply, and the candidates in all of them are REAL
        rather than phantom: a chain of pipe stages, where the reader keeps the
        moved directory beside the unmoved one, and chains of `;` or of `&&` and
        `||`, where each one parks a further failure branch. Counting the `cd`
        segments in front of the commit, they reach the cap at seven, seven and
        nine-or-ten — and the pipe chain at six when the commit is joined by `;`,
        which parks a branch at every stage on top of the pipe keeping both. Past
        the cap the whole command reads as a directory the reader could not
        compute, which is the failure direction this module already has — a stop,
        never a guess.
        """
        # Fourteen stages, not forty: without the cap this is 16384 candidates,
        # which the reader still computes in well under a second, so the case
        # FAILS rather than hanging. A red nobody can wait for is not a red.
        command = " | ".join(f"cd d{i}" for i in range(14)) + " ; git commit -m x"
        got = commit_dirs(command, tmp_path)
        assert len(got) <= reader.STATE_CAP
        assert any(isinstance(w, reader.Unresolved) for w in got), (
            "past the cap the answer has to say it is not an answer"
        )

    def test_a_pipeline_in_front_of_a_cd_does_not_hide_the_session(self, tmp_path):
        """The mirror of the case above: the branching operator is BEFORE the
        `cd`, so the `cd` segment itself may never run."""
        b = tmp_path / "b"
        got = [
            str(w)
            for w in commit_dirs(f"echo hi | cd {sh(b)} && git commit -m x", tmp_path)
        ]
        assert str(tmp_path) in got

    def test_one_directory_is_named_once(self, tmp_path):
        """Two ways of reaching the same directory are one candidate, not two.
        `cd N || cd B` reached B from both branches and reported it twice."""
        n, b = tmp_path / "n", tmp_path / "b"
        got = [
            str(w)
            for w in commit_dirs(
                f"cd {sh(n)} || cd {sh(b)} && git commit -m x", tmp_path
            )
        ]
        assert len(got) == len(set(got)), got

    def test_refuses_a_destination_the_reader_cannot_expand_as_a_directory(
        self, tmp_path
    ):
        """The gate reads the command BEFORE the shell expands it, which is the
        same fact that made `git -C "$WT"` unresolvable (issue #56)."""
        for dest in ('"$WT"', "'$WT'", "/tmp/x*", "{a,b}"):
            wheres = commit_dirs(f"cd {dest} && git commit -m x", tmp_path)
            assert unreadable_flags(wheres) == [True], dest

    def test_a_subshell_does_not_hide_the_cd_by_hiding_the_word(self, tmp_path):
        """`(cd X && git commit)` tokenizes its first word as `(cd`, so the cd was
        invisible while the commit was not — the fail-open reproduced with one
        parenthesis. Where the commit runs cannot be read, so it is not read."""
        wheres = commit_dirs(f"(cd {sh(tmp_path / 'b')} && git commit -m x)", tmp_path)
        assert wheres and all(unreadable_flags(wheres)), wheres

    def test_cd_dash_goes_back_to_the_directory_before_it(self, tmp_path):
        command = f"cd {sh(tmp_path / 'b')} && cd - && git commit -m x"
        assert commit_dirs(command, tmp_path) == [str(tmp_path)]

    def test_cd_dash_with_nothing_behind_it_is_unreadable(self, tmp_path):
        wheres = commit_dirs("cd - && git commit -m x", tmp_path)
        assert unreadable_flags(wheres) == [True]

    def test_an_unreadable_directory_still_says_what_it_could_not_read(self, tmp_path):
        """The prompt for an unresolved target prints the directories it could
        not identify, so the text has to survive being marked unreadable."""
        (where,) = commit_dirs('cd "$WT" && git commit -m x', tmp_path)
        assert "$WT" in str(where)

    @pytest.mark.parametrize("cd", ["cd u2 2>&1", "cd u2 >|f", "cd u2 >&2"])
    def test_a_cd_the_splitter_cut_after_its_operand_lands_once(self, tmp_path, cd):
        """Round 2 of 1790660768's fix pass. In `cd W 2>&1` the splitter's first
        part is `cd W 2>`, which lands in W on its own words. The group's glued
        view landed it again from there, and the walk named W/W, a directory the
        command never reaches."""
        items = cmdline.split_segments_with_separators(f"{cd} && {BODY}")[0]
        here = str(tmp_path)
        wheres = [
            w for t, w in cmdline.walk_directories(items, here) if t[:1] == ["git"]
        ]
        assert wheres, cd
        named = [str(w) for w in wheres[0]]
        landed = [str(w) for w in wheres[0] if not isinstance(w, cmdline.Unresolved)]
        assert os.path.join(here, "u2") in landed, (cd, named)
        assert os.path.join(here, "u2", "u2") not in named, (cd, named)

    def test_the_common_cross_repository_form_gains_no_candidate(self):
        """S11. `cd <repo> && git commit` is the shape issue #45 exists to keep
        silent, and the detector must not have widened it by one candidate."""
        wheres = commit_wheres(f"cd {TARGET_DIR} && git commit -m x")
        assert [str(w) for w in wheres] == [TARGET_READ]
        assert unreadable(wheres) == []

    def test_the_commit_message_heredoc_gains_nothing(self):
        """S12. The form Claude Code itself writes. A `$(cat <<'EOF' ...)` body is
        a commit message, and the segment holding it is an ordinary `git`
        invocation -- nothing in it is a construct the reader fails to read.

        Driven with a segment IN FRONT of the commit, because a single-segment
        command's `running` is always `[(cwd, None)]` and no answer it produces
        can be unreadable. Without one the type assertion below cannot fail:
        measured, it stayed green under a mutation that made `understood()`
        return False for everything.
        """
        wheres = commit_wheres(
            "git add -A && git commit -m \"$(cat <<'EOF'\ntitle\nEOF\n)\""
        )
        assert [str(w) for w in wheres] == [SESSION]
        assert unreadable(wheres) == []

    @pytest.mark.parametrize(
        "command",
        [
            f"cd {TARGET_DIR} ; git commit -m x",
            f"cd {TARGET_DIR} && make ; git commit -m x",
            f"cd {TARGET_DIR} && make\ngit commit -m x",
            f"cd {TARGET_DIR} && npm run build && lint ; git commit -m x",
        ],
    )
    def test_a_semicolon_consumes_the_failure_branch(self, command):
        """S8-S10. `;` and a newline run what follows either way.

        `||` was the only operator that consumed a parked failure, so a `cd` in
        front of a `;` read as though it could not fail and the directory the
        shell was already in dropped out of the answer. Where that directory is
        the session's own and the target carries a routing declaration, the
        declaration silenced a commit that could land in either.

        A newline is the same operator: `split_segments_with_separators` writes
        an unquoted one out as `;`, so the third row is the second row wrapped
        the way a long command is normally written.
        """
        found = commit_wheres(command)
        wheres = [str(w) for w in found]
        assert TARGET_READ in wheres, command
        assert SESSION in wheres, f"the failure branch of the `cd` is missing: {wheres}"
        # By TYPE, not by text. `Unresolved` subclasses `str`, so an answer that
        # has gone entirely unreadable spells the same two paths and passed the
        # two assertions above unchanged.
        assert unreadable(found) == []

    def test_the_ampersand_form_is_still_the_target_alone(self):
        """The mirror of the case above, and the cost that must stay at zero.

        `&&` runs the commit only where the `cd` arrived. Making `;` branch must
        not have taught `&&` to, or every `cd <repo> && git commit` starts
        answering for the session's own repository too -- the prompt volume issue
        #45 exists to reduce.
        """
        found = commit_wheres(f"cd {TARGET_DIR} && git commit -m x")
        assert [str(w) for w in found] == [TARGET_READ]
        assert unreadable(found) == []

    def test_a_semicolon_chain_reaches_the_cap_rather_than_multiplying(self):
        """`;` adds a branch point, so it adds a shape that multiplies.

        Measured at `STATE_CAP` = 64, counting the `cd` segments in front of the
        commit: a chain of `;`-joined `cd`s reads as a directory the reader could
        not compute from the seventh on. Before this change that chain did not
        multiply at all -- one candidate at any length -- because a `;` consumed
        nothing. Past the cap the answer says it is not an answer, which is this
        module's failure direction: a stop, never a guess.
        """
        command = " ; ".join(f"cd d{i}" for i in range(8)) + " ; git commit -m x"
        wheres = commit_wheres(command)
        assert len(wheres) <= reader.STATE_CAP
        assert unreadable(wheres) == wheres, (
            "past the cap the answer has to say it is not an answer"
        )

    def test_cd_dash_does_not_launder_an_unreadable_shell(self):
        """`cd -` returns to a directory the reader recorded, and after a segment
        it could not follow that record is not where the shell has been.

        Returning the recorded previous directory washed the answer clean:
        `eval 'cd /A; cd /B' && cd - && git commit` answered the session's own
        directory with nothing marked unreadable, while bash stood in `/A`. It is
        the one place the invariant this work item introduces did not survive a
        segment.
        """
        found = commit_wheres("eval 'cd /A; cd /B' && cd - && git commit -m x")
        assert found and unreadable(found) == found, (
            f"the answer came back readable: {[str(w) for w in found]}"
        )

    def test_cd_dash_with_no_previous_directory_invents_no_path(self):
        """A `cd -` the reader has no previous directory for is unreadable, not a
        path built out of the operand.

        `<cwd>/-` exists nowhere, and putting it in the prompt names a target the
        user never typed. The `;` merge feeds exactly that state -- a branch whose
        `cd` failed has no previous directory -- so a shape that used to need
        `cd -` as the very first segment became common.
        """
        found = commit_wheres("cd /A ; cd - ; git commit -m x")
        assert not [w for w in found if str(w).endswith("/-")], (
            f"a path nobody typed reached the answer: {[str(w) for w in found]}"
        )

    def test_an_unreadable_target_records_why_it_could_not_be_read(self):
        """The two ways a target goes unreadable need different ways out, so the
        reader records which one happened.

        For a value the shell would have expanded, writing the absolute path in
        its place is a real instruction. For a construct there is no value to
        replace and the directory carried is the last one the reader could name,
        usually the session's own -- so the same instruction changes nothing and
        the waiver becomes the only exit. `hooks/commit-review-gate.py` picks the
        arm off this field; without it, both failures got the value's prompt.
        """
        value = commit_wheres('cd "$WT" && git commit -m x')
        assert [w.why for w in value] == [reader.Unresolved.VALUE]

        construct = commit_wheres("eval 'cd /B' && git commit -m x")
        assert [w.why for w in construct] == [reader.Unresolved.CONSTRUCT]

        # A command can reach both, and they stay apart: `cd "$WT"` is the value
        # the reader could not expand and the `eval` is the construct it could not
        # follow. Collapsing them by type alone -- which is how the states used to
        # be keyed -- leaves one prompt speaking for both.
        both = commit_wheres("cd \"$WT\" || eval 'cd /B' || git commit -m x")
        assert sorted({w.why for w in both}) == [
            reader.Unresolved.CONSTRUCT,
            reader.Unresolved.VALUE,
        ], [(str(w), w.why) for w in both]

    def test_one_directory_reached_two_ways_stays_two_answers(self):
        """The reason is part of what makes two states distinct, not a label on
        one of them.

        A pipeline leaves the parent shell where it was and carries the moved
        state beside it, so `cd "$WT" && eval '…' | git commit` reaches
        `<cwd>/$WT` twice: once as the value the reader could not expand, and once
        marked by the `eval` it could not follow. Keyed by type alone, which is
        how these states used to be told apart, the two collapse into whichever
        came first and one prompt then speaks for both.
        """
        both = commit_wheres("cd \"$WT\" && eval 'cd /B' | git commit -m x")
        at_value = {w.why for w in both if str(w) == os.path.normpath(f"{SESSION}/$WT")}
        assert at_value == {
            reader.Unresolved.VALUE,
            reader.Unresolved.CONSTRUCT,
        }, [(str(w), getattr(w, "why", None)) for w in both]

    @pytest.mark.parametrize(
        "command",
        [
            "cd - && git commit -m x",
            "cd - ; git commit -m x",
        ],
    )
    def test_a_cd_dash_the_reader_cannot_retrace_says_construct(self, command):
        """The directory carried is one the reader named itself, so there is no
        value for the user to write out.

        Marked `VALUE`, the gate answers a `cd -` it cannot retrace with *"write
        the absolute path in place of the unresolved value"* — an instruction with
        no value to apply it to, which leaves the waiver as the only way past.
        That is the arm round 1 opened as a blocking finding, reached through a
        different door.
        """
        found = commit_wheres(command)
        reasons = {getattr(w, "why", None) for w in found}
        assert reader.Unresolved.CONSTRUCT in reasons, [
            (str(w), getattr(w, "why", None)) for w in found
        ]
        # `;` also carries the branch where the `cd -` FAILED, and that shell
        # really did stay put -- a readable answer, correctly. What must not be
        # here is `VALUE`, which is the arm with no value to write out.
        assert reader.Unresolved.VALUE not in reasons

    def test_the_cap_collapse_says_construct(self, monkeypatch):
        """Past `STATE_CAP` the command reached more directories than the reader
        will answer for, and that is not a value anyone can write out either.

        Driven with the cap lowered rather than with a sixty-segment command, so
        the case reads as what it is about.
        """
        monkeypatch.setattr(reader, "STATE_CAP", 3)
        command = " ; ".join(f"cd a{i}" for i in range(6)) + " ; git commit -m x"
        found = commit_wheres(command)
        assert found and all(
            getattr(w, "why", None) == reader.Unresolved.CONSTRUCT for w in found
        ), [(str(w), getattr(w, "why", None)) for w in found]

    def test_a_readable_directory_carries_no_reason(self):
        """The field is what tells an unreadable target from a readable one at the
        grouping key, so a plain answer must not grow one by accident."""
        assert [getattr(w, "why", None) for w in commit_wheres("git commit -m x")] == [
            None
        ]

    def test_a_name_the_command_defined_names_the_repository(self):
        """S1. The one-assignment shape, which is the common one."""
        assert commits('SB=/abs/path; git -C "$SB" commit -m x') == [
            (("/abs/path",), SESSION)
        ]

    def test_the_braced_spelling_reads_the_same(self):
        """S1. `${SB}` is the same name written the other way, and a reader that
        filled one and not the other would answer differently for two spellings of
        one command."""
        assert commits('SB=/abs/path; git -C "${SB}" commit -m x') == [
            (("/abs/path",), SESSION)
        ]

    def test_a_name_composed_with_a_suffix_resolves(self):
        """S2. `"$SB/r1"` is how a scratch repository is actually named."""
        assert commits('SB=/abs/path; git -C "$SB/r1" commit -m x') == [
            (("/abs/path/r1",), SESSION)
        ]

    def test_a_cd_to_a_name_the_command_defined_moves_the_shell(self):
        """S1 through the other operand. `_cd_target` and `parse_git` are two
        call sites reading one fact, and fixing one would answer differently for
        `cd "$SB" && git commit` than for `git -C "$SB" commit`."""
        assert targets('SB=/abs/path; cd "$SB" && git commit -m x') == [
            os.path.normpath("/abs/path")
        ]
        assert targets('SB=/abs/path; cd "$SB/r1" && git commit -m x') == [
            os.path.normpath("/abs/path/r1")
        ]

    def test_a_value_built_from_an_earlier_name_resolves(self):
        """`B=$A/sub` records what `$A` already resolved to, because the value is
        substituted as it is bound."""
        assert commits('A=/base; B=$A/sub; git -C "$B" commit -m x') == [
            (("/base/sub",), SESSION)
        ]

    def test_the_later_assignment_is_the_one_used(self):
        """S5, first half."""
        assert commits('SB=/one; SB=/two; git -C "$SB" commit -m x') == [
            (("/two",), SESSION)
        ]

    def test_an_environment_variable_is_still_unresolvable(self):
        """S3, and it is the line the whole mechanism is bounded by.

        `$WT` comes from a shell this process cannot see. A reader that answered
        from its OWN environment would be silently wrong wherever the two differ,
        which is the confident-wrong direction `understood`'s docstring exists to
        end. The `$` has to survive into the operand.
        """
        assert commits('git -C "$WT" commit -m x') == [(("$WT",), SESSION)]

    def test_an_undefined_name_beside_a_defined_one_is_still_unresolvable(self):
        """The same, with the mechanism switched on. An environment that holds
        `SB` must not answer for `OTHER`."""
        assert commits('SB=/x; git -C "$OTHER" commit -m x') == [(("$OTHER",), SESSION)]

    def test_a_loop_variable_keeps_its_prompt_and_names_itself(self):
        """S4. `$n` has as many values as the loop has iterations, and one of them
        is not an answer.

        The operand comes back with `$SB` filled and `$n` standing, so the text a
        prompt prints names the part that could not be read rather than the part
        that could — which is what makes "write this one out" a usable
        instruction.
        """
        assert commits('SB=/p; git -C "$SB/r$n" commit -m x') == [
            (("/p/r$n",), SESSION)
        ]

    def test_the_expansion_operators_are_left_standing(self):
        """Everything one step out from a bare name stays unresolvable: an
        operator that takes a WORD, a command substitution, an arithmetic
        expansion, and a positional parameter."""
        for operand, expected in (
            ("${SB:-/y}", "${SB:-/y}"),
            ("${#SB}", "${#SB}"),
            ("$(pwd)", "$(pwd)"),
            ("$((1+1))", "$((1+1))"),
            ("$1", "$1"),
            ("$@", "$@"),
        ):
            assert commits(f'SB=/x; git -C "{operand}" commit -m x') == [
                ((expected,), SESSION)
            ], operand

    def test_the_expands_test_still_stands_in_front_of_the_shell(self):
        """The substitution goes IN FRONT of the `EXPANDS` test and never replaces
        it, so a value carrying a glob is still a set of paths rather than one."""
        kind, operand = reader._cd_target(["cd", "/a*b"])
        assert (kind, operand) == ("unknown", "/a*b")
        where = commits('SB="/a*b"; cd "$SB" && git commit -m x')[0][1]
        assert isinstance(where, reader.Unresolved), (
            f"a glob named through a variable became one path: {where!r}"
        )

    def test_an_assignment_in_the_same_segment_does_not_expand_in_it(self):
        """`SB=/x git -C "$SB"` — bash expands the arguments before it applies the
        assignment, so the shell does not see `/x` here either."""
        assert commits('SB=/abs/path git -C "$SB" commit -m x') == [(("$SB",), SESSION)]

    def test_an_assignment_the_reader_cannot_place_never_enters(self):
        """S5, second half. `understood` already refuses to say where these leave
        the shell, and a name is no easier than a directory.

        A subshell is on this list twice over: bash discards its assignments when
        it exits, so answering `/inside` would be wrong about bash and not only
        about what this reader can see.
        """
        for name, command in (
            ("a function body", 'f() { SB=/inside; }; f; git -C "$SB" commit -m x'),
            (
                "a loop body",
                'for i in 1; do SB=/inside; done; git -C "$SB" commit -m x',
            ),
            ("a subshell", '(SB=/inside); git -C "$SB" commit -m x'),
            ("an eval", "eval 'SB=/inside'; git -C \"$SB\" commit -m x"),
        ):
            assert [ch for ch, _ in commits(command)] == [("$SB",)], name

    def test_a_pipeline_stage_leaves_the_parent_shells_name_alone(self):
        """bash runs each stage in a subshell: `A=1 | true; echo $A` prints
        nothing. The same fact that keeps a pipeline from moving the parent
        shell's DIRECTORY keeps it from writing its names."""
        for sep in ("|", "|&", "&"):
            assert [
                ch for ch, _ in commits(f'SB=/x {sep} git -C "$SB" commit -m y')
            ] == [("$SB",)], sep

    def test_an_assignment_this_reader_does_not_model_empties_the_name(self):
        """`A+=x` appends and `a[0]=x` writes one element. An earlier `SB=/one`
        left standing through either would answer confidently with a path the
        shell never reaches — the single failure mode this mechanism has."""
        for form in ("SB+=/two", "SB[0]=/two"):
            assert commits(f'SB=/one; {form}; git -C "$SB" commit -m x') == [
                (("$SB",), SESSION)
            ], form

    def test_a_name_rebound_to_something_unresolvable_stops_again(self):
        """The later assignment wins even when it loses the answer: a reader that
        kept `/one` here would name a repository the shell left two segments
        ago."""
        assert commits('SB=/one; SB=$WT; git -C "$SB" commit -m x') == [
            (("$WT",), SESSION)
        ]

    def test_an_assignment_in_front_of_a_command_is_that_commands_environment(self):
        """bash keeps a prefix assignment out of the shell: `A=1 true; echo "$A"`
        prints an empty line, measured under bash 3.2.57.

        So the shapes this reads are exactly the ones `understood` calls
        "assignments alone". `SB=/x make` looks like an assignment and is not one,
        and reading it would name a repository the shell never learned about.
        """
        for command in (
            'SB=/x make; git -C "$SB" commit -m y',
            'SB=/x true && git -C "$SB" commit -m y',
        ):
            assert [ch for ch, _ in commits(command)] == [("$SB",)], command

    def test_two_assignments_in_one_segment_both_land(self):
        """`A=/a B=/b` alone is still assignments alone, and bash keeps both."""
        assert commits(
            'A=/a B=/b; git -C "$A" commit -m x && git -C "$B" commit -m y'
        ) == [
            (("/a",), SESSION),
            (("/b",), SESSION),
        ]

    def test_a_single_quoted_operand_is_filled_too_and_that_is_the_cost(self):
        """The measured cost of this mechanism, pinned as a DECISION.

        bash expands nothing inside single quotes: `ls -d '$SB'` names a directory
        literally called `$SB`, executed. This reader cannot tell the two quotings
        apart -- `shlex` runs in posix mode and takes both off, so `git -C '$SB'`
        and `git -C "$SB"` arrive as one token -- and it now answers `/x` for both
        where it used to answer `<cwd>/$SB` for both and was right about the first.

        That is the fail-OPEN direction, and it is accepted rather than closed. It
        needs a directory literally named `$SB`, single-quoted, in a command that
        also assigns `SB`. Closing it means carrying quote provenance out of the
        splitter, which changes how every argument in every command tokenizes.

        Asserting the CURRENT answer rather than the ideal one: if quote
        provenance ever lands, this expectation flips and the flip is the signal.
        """
        assert commits("SB=/x; git -C '$SB' commit -m y") == [(("/x",), SESSION)]

    def test_a_name_a_segment_may_have_written_is_forgotten(self):
        """Round 1, and it is a REGRESSION rather than a gap.

        Before this branch every one of these reached the gate as `$SB`, because
        nothing was resolved at all. The branch resolved the first assignment and
        then held it across a segment that may have changed it, so a stop became
        a silence -- measured at the gate, `deny` at the base and `silent` here,
        with bash committing in a repository nothing had reviewed.
        """
        for middle in FORGETS:
            where = targets(f'SB=/one; {middle}; git -C "$SB" commit -m x')
            assert any("$SB" in w for w in where), (
                f"`{middle}` left `/one` standing: {where}. The reader has to "
                "forget a name it cannot follow, not keep the value from before"
            )

    def test_a_conditional_branch_does_not_bind_a_name(self):
        """`states` and `parked` model a conditional for the DIRECTORY and
        nothing modelled it for a name.

        Measured: `SB=/one; [ -d /nope ] && SB=/two; git -C "$SB" commit`
        answered `/two` where bash has `/one`. The branch may not run, so what it
        assigns is not something this reader can state."""
        for joined in ("&&", "||"):
            where = targets(f'SB=/one; true {joined} SB=/two; git -C "$SB" commit -m x')
            assert any("$SB" in w for w in where), (
                f"a `{joined}` branch bound a name the shell may never have set: {where}"
            )

    def test_forgetting_did_not_take_the_answers_with_it(self):
        """The other direction. A reader that forgets everything is correct and
        useless, and the shapes that DO resolve are the point of this work."""
        for command, expected in BINDS:
            where = targets(command)
            assert os.path.normpath(expected) in where, (
                f"{command!r} stopped resolving: {where}"
            )

    def test_a_refused_segment_that_carries_no_name_keeps_the_environment(self):
        """Round 3, and the regression is this branch's own.

        An earlier commit on this branch cured a real fail-open -- an `eval` and a sourced script were
        answering with a path bash had left -- by emptying the environment for
        every segment `understood` refused. Six shapes that answered `/one` at
        before it prompted after it, and `if …; then … fi` is the commonest shape
        in a script, in a work item that exists to stop asking.
        """
        for middle in KEEPS:
            where = targets(f'SB=/one; {middle}; git -C "$SB" commit -m x')
            assert where == [os.path.normpath("/one")], (
                f"`{middle}` carries no name and cannot have written one, and the "
                f"reader lost `/one` across it: {where}"
            )

    def test_a_refused_segment_that_can_write_a_name_forgets_it(self):
        """The aim only holds if what it keeps is what carries no name.

        Every entry here answered `$SB` after that change because everything did.
        Keeping any one of them would answer confidently with a path the shell is
        not in, which is the one failure mode this whole mechanism is bounded to
        avoid.
        """
        for middle, why in UNSEEN_FORGETS:
            where = targets(f'SB=/one; {middle}; git -C "$SB" commit -m x')
            assert any("$SB" in w for w in where), (
                f"{why} -- `{middle}` -- left `/one` standing: {where}"
            )

    def test_the_reset_still_empties_the_whole_environment_not_one_name(self):
        """An `eval` says nothing about which name it wrote, so no name survives
        it. `_forget` would drop what the segment NAMES, and an `eval` names
        nothing -- which is the difference between the two branches."""
        where = targets('SB=/one; OT=/other; eval "$x"; git -C "$OT" commit -m x')
        assert any("$OT" in w for w in where), (
            f"an `eval` left a second name standing: {where}. What it wrote is "
            "not something this reader can narrow to the names it can see"
        )
        # And the aimed branch does NOT empty the second name.
        assert targets('SB=/one; OT=/other; fi; git -C "$OT" commit -m x') == [
            os.path.normpath("/other")
        ]

    def test_a_name_writer_read_blindly_costs_a_prompt_and_not_an_answer(self):
        """The cost of asking `NAME_WRITERS` of every word rather than of the
        word that runs. `echo read` writes nothing, and this reader forgets on it
        anyway -- a prompt, which is what the branch gave for everything before.
        It is recorded rather than fixed, because the direction is the safe one."""
        where = targets('SB=/one; then echo read SB; git -C "$SB" commit -m x')
        assert any("$SB" in w for w in where), where

    def test_the_pipeline_branch_forgets_and_lastpipe_is_why(self):
        """Round 2 found nothing reaching this branch: turning it into `pass`
        left the suite green.

        `shopt -s lastpipe` runs a pipeline's last stage in the current shell, so
        `true | SB=/two` writes the parent's `SB` under a setting this process
        cannot see and `SB=/two | true` does not. Which of the two a segment is
        depends on a shell option, so the answer is the one this reader gives for
        anything it cannot state. The cost is one prompt where bash has `/one`.
        """
        for command in (
            'SB=/one; SB=/two | true; git -C "$SB" commit -m x',
            'SB=/one; true | SB=/two; git -C "$SB" commit -m x',
            'SB=/one; SB=/two & git -C "$SB" commit -m x',
        ):
            where = targets(command)
            assert any("$SB" in w for w in where), (
                f"the pipeline branch kept a name across a stage bash runs in a "
                f"subshell -- or wrote one under `lastpipe` that it cannot see: "
                f"{command!r} answered {where}"
            )

    def test_the_arithmetic_loop_head_forgets_its_counter_and_not_the_rest(self):
        """`for ((i=0; i<3; i++))` arrives as the single token `for` `((i=0`, and
        `_name_at` reads a name from the START of a word -- so the `(` comes off
        first. A loop head this reader cannot read a name out of empties the
        environment instead, because which name it writes is not visible."""
        where = targets(
            "SB=/one; OT=/other; for ((SB=0; k<3; k++)); do :; done; "
            'git -C "$OT" commit -m x'
        )
        assert where == [os.path.normpath("/other")], (
            f"the arithmetic head took a name it never wrote with it: {where}"
        )
        # The counter itself, named only in the head. bash leaves `SB` at `3`.
        where = targets(
            'SB=/one; for ((SB=0; k<3; k++)); do :; done; git -C "$SB" commit -m x'
        )
        assert any("$SB" in w for w in where), (
            f"the loop counter kept the value from before the loop: {where}"
        )
        assert reader._unseen({"SB": "/one"}, shlex.split("for $v in a b")) == {}, (
            "a loop head with no readable name left a value standing"
        )

    def test_the_blind_sweep_forgets_bare_names_only(self):
        """`_unseen` asks `NAME_WRITERS` of every word and then forgets the bare
        names beside it. The operand test is `end == len(tok)`, the same line
        `_forget` carries, and loosening it here survived every test while the
        same loosening in `_forget` did not: `read -rp 'SB> ' ans` would forget
        `SB` on the strength of a prompt string. Executed under bash 3.2.57 with
        stdin closed, `SB` is `/one` after it."""
        kept = reader._unseen(
            {"SB": "/one", "ans": "x"}, shlex.split("if read -rp 'SB> ' ans")
        )
        assert kept.get("SB") == "/one", "`SB> ` is not the name `SB`"
        assert "ans" not in kept, "the name the `read` writes survived it"
        where = targets(
            "SB=/one; if read -rp 'SB> ' ans; then :; fi; git -C \"$SB\" commit -m x"
        )
        assert where == [os.path.normpath("/one")], where

    def test_a_bodys_later_statement_is_not_a_top_level_one(self):
        for middle in UNRUN_BODIES:
            where = targets(f'SB=/one; {middle}; git -C "$SB" commit -m x')
            assert any("$SB" in w for w in where), (
                f"`{middle}` -- a statement inside a body this reader cannot say "
                f"ran was bound as if it were top level: {where}"
            )

    def test_the_body_ends_at_its_closer(self):
        """The count has to come back down, or the aim is lost again one level
        up: every assignment after the first compound command would be forgotten
        and the string would prompt from there on."""
        for command in (
            'SB=/one; if false; then echo hi; SB=/two; fi; SB=/three; git -C "$SB" commit -m x',
            'SB=/one; if false; then { :; }; SB=/two; fi; SB=/three; git -C "$SB" commit -m x',
            'SB=/one; ( echo hi ); SB=/three; git -C "$SB" commit -m x',
            'SB=/one; f() { echo hi; }; SB=/three; git -C "$SB" commit -m x',
            'SB=/one; case x in x) echo hi ;; esac; SB=/three; git -C "$SB" commit -m x',
            # The arithmetic head is not a subshell, so the loop nets to zero.
            'SB=/one; for ((k=0; k<2; k++)); do :; done; SB=/three; git -C "$SB" commit -m x',
            # A closer in argument position is a word, and does not close early.
            'SB=/one; if true; then echo fi; fi; SB=/three; git -C "$SB" commit -m x',
            # Round 1: the multi-line `case` ends at its `esac`, so the stack has
            # to pop `case` there -- with `stack.pop()` removed this one prompts.
            'SB=/one; case x in\na )\necho hi ;;\nesac; SB=/three; git -C "$SB" commit -m x',
            # And an opener outside command position opens nothing, so the
            # everyday shapes round 1 found newly prompting resolve again.
            "SB=/one; grep -c '(' f; SB=/three; git -C \"$SB\" commit -m x",
            'SB=/one; time { echo hi; }; SB=/three; git -C "$SB" commit -m x',
            'SB=/one; if true; then if true; then :; fi; fi; SB=/three; git -C "$SB" commit -m x',
            # Round 2: the `)` an array or a substitution closes at top level is
            # nobody's subshell closer, so the assignment after it still binds.
            'SB=/one; OT=( a b ); ( echo hi ); SB=/three; git -C "$SB" commit -m x',
            'SB=/one; X=$( pwd ); SB=/three; git -C "$SB" commit -m x',
        ):
            assert targets(command) == [os.path.normpath("/three")], command
        # A paren inside a commit message opened a body for the rest of the string.
        where = targets(
            'SB=/one; git commit -m "(wip) x"; SB=/three; git -C "$SB" commit -m x'
        )
        assert os.path.normpath("/three") in where, where

    def test_a_glued_closer_costs_a_prompt_and_not_an_answer(self):
        """`(cd <x> && make)` arrives as `(cd` … `make)`, and the glued closer is
        not counted because a `case` pattern `x)` looks the same. The count stays
        open and the assignment after it is forgotten -- a prompt where bash has
        `/three`. Recorded as the cost rather than fixed, because the direction is
        the safe one."""
        where = targets(
            'SB=/one; (cd /x && echo hi); SB=/three; git -C "$SB" commit -m x'
        )
        assert any("$SB" in w for w in where), where

    def test_a_call_to_a_function_the_string_defined_empties_the_environment(self):
        """`f() { SB=/three; }; SB=/one; f; git -C "$SB"` -- bash `/three`, the
        reader `/one`. The call is a plain word `understood` accepts and `_forget`
        finds nothing in, but the definition is in the same string, so the reader
        has seen the name."""
        for command in (
            'f() { SB=/three; }; SB=/one; f; git -C "$SB" commit -m x',
            'function f { SB=/three; }; SB=/one; OT=/o; f; git -C "$OT" commit -m x',
            'f(){ SB=/three; }; SB=/one; time f; git -C "$SB" commit -m x',
            'f () { SB=/three; }; SB=/one; if true; then f; fi; git -C "$SB" commit -m x',
            'f() { SB=/three; }; SB=/one; true && f; git -C "$SB" commit -m x',
        ):
            where = targets(command)
            assert any("$" in w for w in where), (
                f"{command!r} kept a name the call may have rewritten: {where}"
            )
        # A definition is not a call, and a word never defined here is a word.
        assert targets('f() { SB=/three; }; SB=/one; g; git -C "$SB" commit -m x') == [
            os.path.normpath("/one")
        ]

    def test_the_writers_round_one_found_are_forgotten(self):
        """`((SB=3))`, `let "SB = 3"` and `${SB:=/three}` each write `SB` with no
        `NAME=` at the start of a word. Executed under bash 3.2.57: `SB` is `3`,
        `3` and -- for `:=` on a set name -- `/one`; the reader forgets on all of
        them, which is a prompt and never an answer."""
        for middle in (
            "((SB=3))",
            'let "SB = 3"',
            "let SB++",
            ': "${SB:=/three}"',
            'echo "${SB=/three}"',
            "if ((SB=3)); then :; fi",
            'while let "SB = 3"; do break; done',
            'if true; then : "${SB:=/three}"; fi',
        ):
            where = targets(f'SB=/one; {middle}; git -C "$SB" commit -m x')
            assert any("$SB" in w for w in where), f"`{middle}` kept `/one`: {where}"
        # The operators that read a name without writing it are left standing.
        assert targets(
            'SB=/one; echo "${SB:-/three}" "${#SB}"; git -C "$SB" commit -m x'
        ) == [os.path.normpath("/one")]


class Test_understood:
    def test_accepts_a_plain_command_and_not_a_construct(self):
        """The check has to be able to say no AND yes, or it is not a check.

        `verify`'s second condition: a check that cannot fail is a counterfeit
        seal. `understood` returning False for everything would make every test
        above pass and every command in the repository prompt.
        """
        assert reader.understood(["git", "commit", "-m", "x"]) is True
        assert reader.understood(["cd", "/tmp"]) is True
        assert reader.understood(["FOO=1", "make"]) is True
        assert reader.understood(["eval", "cd /tmp"]) is False
        assert reader.understood(["for", "d", "in", "x"]) is False
        assert reader.understood(["command", "-p", "cd", "/tmp"]) is False
        assert reader.understood(["command", "$C", "/tmp"]) is False
        assert reader.understood(["time", "make"]) is True

    def test_refuses_a_reserved_word_behind_a_prefix_as_a_simple_command(self):
        """`understood` asked the reserved-word question of the FIRST token only,
        and `!` and `time` are prefixes it steps past. `! for SB in /two /three`
        then reached `_bind` as something that runs, `_forget` found no `=` in
        it, and `/one` stood where bash has `/three`. Two of the 82."""
        assert not reader.understood(shlex.split("! for SB in /two /three"))
        assert not reader.understood(shlex.split("time pushd /x"))
        assert not reader.understood(shlex.split("command pushd /x"))
        # And what the prefixes still pass through.
        assert reader.understood(shlex.split("! true"))
        assert reader.understood(shlex.split("time echo hi"))
        assert reader.understood(shlex.split("command -p ls"))
        for middle in (
            "! for SB in /two /three; do :; done",
            "time for SB in /two; do :; done",
        ):
            where = targets(f'SB=/one; {middle}; git -C "$SB" commit -m x')
            assert any("$SB" in w for w in where), (
                f"`{middle}` kept the value from before the loop: {where}"
            )

    @pytest.mark.parametrize("name,command,_probe", MOVES_THE_SHELL, ids=NAMES)
    def test_a_construct_the_reader_does_not_model_stops_the_commit(
        self, name, command, _probe
    ):
        """S1-S6. Not "the shell stayed here", which is an answer -- `Unresolved`,
        which is the reader saying it does not have one."""
        filled = command.replace("%s/s.sh", "/x/s.sh")
        if "%s" in filled:
            filled = filled % TARGET_DIR
        wheres = commit_wheres(filled)
        assert wheres, f"{name}: no commit was found at all"
        assert unreadable(wheres) == wheres, (
            f"{name}: the reader still answered with a directory: "
            f"{[str(w) for w in wheres]}"
        )

    @pytest.mark.parametrize("name,_command,probe", MOVES_THE_SHELL, ids=NAMES)
    def test_a_real_shell_really_lands_in_the_target(
        self, name, _command, probe, tmp_path
    ):
        """The other half of the measurement, and the reason the stop is right.

        Every construct above leaves bash in the target directory, so the reader's
        old answer -- the session's own directory -- named a repository the commit
        was not going to land in. Without this, the tests above pin a stop with no
        evidence that anything was ever wrong.

        `sudo cd` is deliberately not here: it looks for a binary named `cd` and
        finds none, so it does NOT move the shell. The reader stops for it anyway,
        because keeping which wrapper forks would be one more enumeration.
        """
        why = shell_probe("bash")
        if why:
            pytest.skip(f"bash: {why}")
        target = tmp_path / "target"
        target.mkdir()
        # The sourced-script rows name a script beside the target; the others
        # ignore it. Writing it unconditionally keeps the table one shape.
        (tmp_path / "s.sh").write_text(
            f"cd {shlex.quote(str(target))}\n", encoding="utf-8"
        )
        filled = probe.replace("%s/s.sh", shlex.quote(str(tmp_path / "s.sh")))
        if "%s" in filled:
            filled = filled % shlex.quote(str(target))
        out = subprocess.run(
            ["bash", "-c", filled + "; pwd -P"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        landed = out.stdout.strip().splitlines()[-1] if out.stdout.strip() else ""
        assert landed == str(target.resolve()), (
            f"{name}: bash landed in {landed!r}, so this row is not the case it "
            f"claims to be (stderr: {out.stderr.strip()!r})"
        )

    @pytest.mark.parametrize(
        "command",
        [
            f"cd {TARGET_DIR} && make && git commit -m x",
            f"cd {TARGET_DIR} && ./deploy.sh && git commit -m x",
            f"cd {TARGET_DIR} && git add -A && git commit -m x",
            "sudo git commit -m x",
            "env FOO=1 git commit -m x",
            "time git commit -m x",
            # A conditional expression holds no commands, so it cannot leave the
            # shell anywhere. `[[ … ]]` is a reserved word and `[` is `test`
            # spelled the other way -- read as a scope opener and as a glob
            # respectively, both stopped what `test -f f.py && git commit`, the
            # same condition in a third spelling, never stopped.
            "[ -f f.py ] && git commit -m x",
            "[[ -f f.py ]] && git commit -m x",
            "[ ! -f zzz ] && git commit -m x",
            "test -f f.py && git commit -m x",
            # `shopt` does not move a shell. It was a relocator for one round on
            # the grounds that `expand_aliases` turns alias expansion on, and an
            # alias written in the command is caught by `alias` itself while one
            # set by a profile is caught by nothing -- so it closed no door and
            # stopped `shopt -s globstar && git commit`.
            "shopt -s globstar && git commit -m x",
            "shopt -s nullglob && git commit -m x",
        ],
    )
    def test_an_ordinary_command_is_still_understood(self, command):
        """A wrapper, a script, a build tool -- none of them is a construct. A
        detector that stopped on these would be the "judge every directory named
        anywhere" option `plan.md` rejected, arriving by accident."""
        found = commit_wheres(command)
        assert found, f"no commit was found at all: {command!r}"
        assert unreadable(found) == []

    def test_a_reserved_word_that_only_stands_in_front_is_not_a_scope(self):
        """`time` and `!` stand in FRONT of a command rather than opening a scope.

        Read as scope openers they stopped `time make && git commit` and
        `! grep -q zzz f && git commit`, both ordinary and both silent before this
        work item. The segment's own directory was never the question -- what
        changed was every segment after it.
        """
        for command in (
            "time make && git commit -m x",
            "! grep -q zzz f.py && git commit -m x",
        ):
            found = commit_wheres(command)
            # `unreadable([]) == []`, so an answer with no commit in it passes the
            # line below. A commit swallowed whole is not hypothetical here --
            # both the arithmetic case and the comment case produced exactly that.
            assert found, f"no commit was found at all: {command!r}"
            assert unreadable(found) == []
        # The pair: a `cd` behind one of them is unreadable, because whether the
        # word forks is what decides whether that `cd` reaches this shell.
        assert (
            unreadable(commit_wheres(f"time cd {TARGET_DIR} && git commit -m x")) != []
        )

    def test_an_alias_on_cd_stops_the_commit(self):
        """`alias cd='cd <B>'` leaves both words in the command exactly as written.

        So this is a directory the reader got confidently wrong rather than a
        command it never saw -- which is why `alias` and `shopt` are relocators
        and not, like a command hidden in an `eval` string, issue #75's shape.
        Executed: bash stands in `<B>` while the reader answered `['/tmp', '/S']`
        with nothing marked unreadable.

        Not every candidate comes back unreadable, and that is the reader being
        consistent rather than a gap. An absolute `cd` does not depend on where
        the shell was, so `/tmp` is recovered clean -- the rule that lets
        `eval 'echo hi'; cd /tmp; git commit` answer `/tmp` instead of giving up.
        One unreadable candidate is what stops the commit, and that is what this
        asserts.

        What no enumeration reaches: an alias set by `BASH_ENV` or a profile,
        which never appears in the command string at all.
        """
        found = commit_wheres(f"alias cd='cd {TARGET_DIR}'\ncd /tmp\ngit commit -m x")
        assert unreadable(found), (
            f"nothing in the answer says the reader could not follow the alias: "
            f"{[str(w) for w in found]}"
        )


class Test_drop_comments:
    def test_accepts_a_paren_inside_an_expansion_as_a_word_part(self):
        """Both models, not one. This is the half issue #78's title is about.

        Asserted at `drop_comments` rather than through a shell: bash rejects
        `echo ${x:-((} zz)#c` outright — `syntax error near unexpected token ')'`,
        measured — so there is no behaviour to compare against. What is being
        pinned is that the two models answer the same question the same way, which
        is what makes their answers predictable when one of them is wrong.
        """
        text = "echo ${x:-((} zz)#c ; git commit -m x"
        assert reader.drop_comments(text) == text, (
            "the `)` ended the word, the `#` opened a comment, and the commit went"
        )

    def test_refuses_a_bare_brace_as_an_expansion_opener(self):
        """A bare `{` is a group or a brace expansion, not an expansion of a name.

        Measured under bash 3.2.57: `echo { #c ; echo REACHED` prints `{` and does
        NOT reach the next command, so bash opens a comment there. Counting a bare
        `{` would hold the expansion open past the `}` that never comes, leave the
        comment standing, and read `git commit` as a command bash never runs.
        """
        assert commit_wheres("echo { #c ; git commit -m x") == []
        assert reader.drop_comments("echo { #c ; git commit -m x") == "echo { "

    def test_a_hash_after_a_command_substitution_opens_no_comment(self):
        """`)` ends a word for a subshell and not for `$(…)`, and this reader
        cannot tell them apart.

        Executed: `bash -c 'echo $(echo a)#foo && echo X'` prints `a#foo` and then
        `X`, so bash runs everything after that `#`. Reading it as a comment
        opener deleted the `&& git commit` behind it — and once the commit gate's
        judgment read started dropping comments, that deletion reached a gate with
        no commit left to judge. A blank still opens one.
        """
        found = commit_wheres(f"cd {TARGET_DIR} && echo $(pwd)#note && git commit -m x")
        assert found, "the commit was deleted with a comment bash does not open"
        assert [str(w) for w in found] == [TARGET_READ]
        # The spaced form is a comment in bash too, so the commit really is gone
        # from what the shell would run -- and the reader answers for the segments
        # that remain rather than inventing one.
        spaced = commit_wheres(
            f"cd {TARGET_DIR} && echo $(pwd) # note && git commit -m x"
        )
        assert spaced == []

    @pytest.mark.parametrize(
        "command",
        [
            "cat <(echo a)#zzz ; git commit -m x",
            "echo <(echo a)#zzz ; git commit -m x",
            "echo a > >(cat)#zzz ; git commit -m x",
            "x=(a b)#zzz && git commit -m x",
            "files=(*.py)#zzz ; git commit -m x",
            "x=()#zzz && git commit -m x",
        ],
    )
    def test_a_hash_after_a_word_part_paren_opens_no_comment(self, command):
        """A `)` that closes something a WORD runs through opens no comment.

        `$(` is not the only opener. Four are: `$(`, the `<(` and `>(` of a
        process substitution, and the `(` of an array assignment `name=(`.
        Measured under bash 3.2.57 against a scratch repository -- every command
        here really creates a commit, and reading that `)` as a subshell's put a
        comment where bash opens none and deleted the commit behind it.

        Round 2 closed `$(` and round 4 found the other three still open, which
        is why the model is pinned here by construct rather than by example.
        """
        assert commit_wheres(command), command

    def test_a_subshell_close_still_opens_one(self, command=None):
        """The other side of the same constant, so neither direction is free.

        `(echo a)#zzz` really is a comment to bash -- and bash creates no commit
        there, so the reader answering `blind` is correct. Teaching every `)` to
        leave the word running would make this case wrong.
        """
        assert not commit_wheres("(echo a)#zzz ; git commit -m x")

    @pytest.mark.parametrize("op", ["@", "!", "*", "+", "?"])
    def test_an_extglob_pattern_keeps_the_word_running(self, op):
        """extglob's five operators make `(` part of a WORD, the way `$(` does.

        Read as a command paren, the `)` ends the word and the `#` after it opens a
        comment bash does not -- which DELETES the commit behind it, and both gates
        then say nothing. Measured under bash 3.2.57 against a scratch repository:
        with `shopt -s extglob` on the line above, `ls -d @(a|b)#x ; git commit`
        really commits, 1 -> 2.

        `bash -n` calls it a syntax error and is WRONG here: `extglob` is a runtime
        shopt the parse check cannot see. Measure this family with `bash -O
        extglob`. Round 4 enumerated four openers and declared the list closed;
        this is the fifth time that constant has been found short.
        """
        assert commit_wheres(f"shopt -s extglob\nls -d {op}(a|b)#x ; git commit -m x")

    def test_a_hash_inside_a_parameter_expansion_opens_no_comment(self):
        """The other paren model's own cost, which issue #78 reported as nothing.

        It was measured on six `${x:-((}#zzz` shapes, where this reader agrees
        with bash. A `#` after a BLANK inside the expansion was never measured and
        is a fail-OPEN: executed under bash 3.2.57, `echo ${x:-a #b} ; echo
        REACHED` prints `a #b` and then `REACHED`, so bash opens no comment and
        runs what follows -- while `drop_comments` returned `echo ${x:-a ` and the
        `git commit` behind it was gone from the segment list entirely.
        """
        assert commit_wheres("echo ${x:-a #b} ; git commit -m x") == [SESSION]
        assert "#b" in reader.drop_comments("echo ${x:-a #b} ; git commit -m x")

    @pytest.mark.parametrize("expansion", WORD_TAKING_EXPANSIONS)
    def test_the_six_shapes_the_comment_model_already_answered_are_unchanged(
        self, expansion
    ):
        """S7's other half. `${…}#zzz` was measured against bash at round 5 and
        the reader agreed on all of it; teaching this model about `${…}` must not
        move an answer it already had right."""
        assert commit_wheres(f"echo {expansion}#zzz ; git commit -m x") == [SESSION]

    def test_a_case_pattern_comment_does_not_take_the_segment_list(self):
        """An unbalanced `)` ends the word, which is what keeps a comment readable.

        A `case` pattern's `)` closes nothing this reader opened, and it is the
        place an unbalanced one actually occurs. Measured: bash opens a comment
        after it, and a comment left in place whose text holds an apostrophe opens
        a quote that never closes -- which took every later line, the commit
        included, out of the segment list.
        """
        command = (
            "case x in\nx)#don't\n  echo hit ;;\nesac\ncd /elsewhere && git commit -m x"
        )
        text = reader.drop_heredoc_bodies(reader.drop_comments(command))
        _, clean = reader.split_segments_with_separators(text)
        assert clean, "the apostrophe in a comment bash DOES open took the segment list"


class Test_drop_heredoc_bodies:
    def test_accepts_a_heredoc_body_as_dropped(self):
        """The case `drop_heredoc_bodies` exists for, pinned beside the fix.

        A body is data. Stepping over arithmetic must not have taught the reader
        to walk into one -- `cd /elsewhere` here is a line written to a file, and
        the commit belongs to the session's own repository.
        """
        wheres = commit_wheres(
            "cat > run.sh <<'EOF'\ncd /elsewhere\nEOF\ngit commit -m x"
        )
        assert [str(w) for w in wheres] == [SESSION]

    @pytest.mark.parametrize(
        "command",
        [
            "n=$((1<<2))\ngit commit -m x",
            "n=$(( (1<<2) + 3 ))\ngit commit -m x",
            "echo $((n<<1))\ngit commit -m x",
        ],
    )
    def test_refuses_arithmetic_as_a_heredoc(self, command):
        """S7. `<<` inside `$((…))` is a left shift.

        Read as a redirect it took `2))` for a delimiter and dropped every line
        after it looking for one that matched, so the commit did not arrive
        misjudged -- it did not arrive at all, and a gate with no commit in front
        of it has nothing to say. The assertion is therefore that a commit is
        FOUND, and found where the shell actually is.
        """
        wheres = commit_wheres(command)
        assert wheres, "the commit after the arithmetic was swallowed entirely"
        assert [str(w) for w in wheres] == [SESSION], (
            "the commit after the arithmetic was swallowed with the heredoc body"
        )
        assert unreadable(wheres) == []

    @pytest.mark.parametrize(
        "command",
        [
            "n=$[1<<2]\ngit commit -m x",
            "n=$[ (1<<2) + 3 ]\ngit commit -m x",
        ],
    )
    def test_the_older_arithmetic_spelling_is_arithmetic_too(self, command):
        """`$[…]` is bash's older spelling of `$((…))` and closes on ONE bracket.

        Left out of the branch that steps over arithmetic, it swallowed the commit
        below it exactly as `$((1<<2))` did -- measured with the commit really
        created in a scratch repository while the reader's segment list held no
        commit at all.
        """
        found = commit_wheres(command)
        assert found, "the commit after the arithmetic was swallowed entirely"
        assert [str(w) for w in found] == [SESSION]
        assert unreadable(found) == []

    def test_a_parenthesis_in_a_string_does_not_stretch_the_arithmetic(self):
        """The depth count tracks quotes, because a shell does.

        Counting brackets blind, one `(` inside a string ran the region to the end
        of the input, and the heredoc body after it was raised as commands -- so
        `cat > run.sh <<'EOF'` with a `cd` in the body newly stopped a command
        that only writes a file.
        """
        command = "x=$((printf '(' ) )\ncat > run.sh <<'EOF'\ncd /elsewhere\nEOF\ngit commit -m x"
        found = commit_wheres(command)
        assert [str(w) for w in found] == [SESSION], (
            "the heredoc body was read as commands"
        )
        assert unreadable(found) == []

    @pytest.mark.parametrize(
        "command",
        [
            "i=0\nwhile ((i<1)); do((i=i+(1<<2)))\nbreak; done\ngit commit -m x",
            "if true; then((x=1<<2))\nfi\ngit commit -m x",
            "if false; then :\nelse((x=1<<2))\nfi\ngit commit -m x",
            "!((1<<2))\ngit commit -m x",
            "{((x=1<<2))\n}\ngit commit -m x",
        ],
    )
    def test_arithmetic_glued_to_a_reserved_word_is_arithmetic_too(self, command):
        """`(` is a metacharacter, so a reserved word ends at it with no blank.

        Requiring one was a fail-open. Measured under bash 3.2.57 against a
        scratch repository: each of these really creates a commit. Read as a
        redirect, the `<<` took its delimiter out of the expression and swallowed
        every line after it, the commit included, and both gates stayed silent.
        """
        assert commit_wheres(command), command

    def test_the_spaced_form_was_never_the_broken_one(self, command=None):
        """The control. One space was the whole difference, which is what said the
        defence was half built rather than absent."""
        assert commit_wheres(
            "i=0\nwhile ((i<1)); do ((i=i+(1<<2)))\nbreak; done\ngit commit -m x"
        )

    def test_a_paren_pair_in_a_quoted_string_is_not_arithmetic(self, command=None):
        """The cost of dropping the blank, bounded where it is cheapest to check.

        Quotes are handled before the arithmetic branch, so a `((` inside them
        opens no region and a following heredoc body is still dropped. The two
        shapes that DO answer differently without the blank are both rejected by
        `bash -n`, and are recorded at the branch rather than pinned here.
        """
        found = commit_wheres(
            "echo '((' <<'EOF'\ngit commit -m sneaky\nEOF\ngit commit -m real"
        )
        assert len(found) == 1, f"the heredoc body was read as commands: {found}"

    @pytest.mark.parametrize("expansion", WORD_TAKING_EXPANSIONS)
    def test_a_paren_pair_inside_a_parameter_expansion_is_a_word(self, expansion):
        """Issue #78, and this expectation is the flip that says it landed.

        It used to assert `2` -- the sneaky commit inside the heredoc body counted
        as a second one, because the arithmetic region ran to the end of the input
        and the `<<` below it was never read as a redirect. Round 5 measured the
        family at 51 shapes across all seventeen operators and pinned the answer
        it gave rather than the answer bash gives, so that leaving it stayed a
        decision.

        Both paren models now count `${…}` nesting, so the `((` in here is the
        text bash treats it as, the heredoc opens, and the body is dropped. One
        commit, which is what bash makes.
        """
        found = commit_wheres(
            f"echo {expansion} <<'EOF'\ngit commit -m sneaky\nEOF\ngit commit -m real"
        )
        assert len(found) == 1, f"the heredoc body was read as commands: {found}"

    def test_a_parameter_expansion_paren_no_longer_imports_the_body_s_cd(self):
        """The sharpest form, and the one that cost a person something.

        Executed under bash 3.2.57 against a scratch repository: bash prints `((`,
        stays in the directory it started in, and makes one commit -- 1 -> 2. The
        gate used to answer for `/target`, a path that exists only in the heredoc
        body, and DENIED a commit that had already been reviewed.

        It now answers for the directory the shell is actually in, which is the
        session's own. This assertion used to be `TARGET_READ in …`.
        """
        found = commit_wheres(
            "echo ${x:-((} <<'EOF'\ncd /target\nEOF\ngit commit -m real"
        )
        assert [str(w) for w in found] == [SESSION], found

    @pytest.mark.parametrize("arith", ["$((1<<2))", "$[1<<2]"])
    def test_arithmetic_inside_a_parameter_expansion_is_still_stepped_over(self, arith):
        """The direction `${…}` state can break, and the reason `$((` and `$[` are
        unconditional while a bare `((` is not.

        `$((1<<2))` is arithmetic wherever it is written, and the `<<` inside it is
        a shift. Suppressing the skip inside `${…}` would read that `<<` as a
        redirect naming the delimiter `2))}`, swallow every line after it, and take
        the `git commit` with it — a fail-OPEN, where the family this change closes
        was fail-closed. Executed: `echo ${x:-$((1<<2))}` prints `4` and reaches
        the next command.
        """
        found = commit_wheres(
            f"echo ${{x:-{arith}}} <<EOF\ncd /target\nEOF\ngit commit -m real"
        )
        assert [str(w) for w in found] == [SESSION], found

    def test_an_unbalanced_expansion_leaves_the_heredoc_readable(self):
        """`${` with no `}` holds the count open to the end of the input, which is
        the state that could hide a real `((` region. Nothing else moves: the
        heredoc opener is read by a later branch, so the body is still dropped and
        the commit below it is still found."""
        found = commit_wheres("echo ${x <<EOF\ncd /target\nEOF\ngit commit -m real")
        assert [str(w) for w in found] == [SESSION], found

    def test_a_hash_inside_an_expansion_closes_no_brace_in_either_model(self):
        """Round 1: `drop_comments` got `and not braces` and the heredoc splitter
        did not, so the two models answered one question two ways.

        `${x:-a #b}` opened a comment in the splitter that swallowed the closing
        `}`, `braces` stayed 1 to the end of the input, every `((` after it
        stopped being an arithmetic region, and a `<<` inside one opened a
        heredoc that ate the rest of the command. Measured: the `git worktree
        add` below such a line left the segment list entirely and the worktree
        guard went silent on a command bash really runs, `rc=0`.
        """
        command = "echo ${x:-a #b}\n((1<<2))\ngit worktree add -b nb ../wt"
        text = reader.drop_heredoc_bodies(reader.drop_comments(command))
        items, clean = reader.split_segments_with_separators(text)
        assert clean, command
        words = [tokens for _, tokens in items]
        assert any(t[:2] == ["git", "worktree"] for t in words), (
            f"the `git worktree add` left the segment list: {words}. A `#` inside "
            "an expansion must not close the brace count in either model"
        )

    def test_refuses_a_heredoc_opener_inside_an_expansion(self):
        """Round 2: `braces` reached the `#` and `((` branches and not `<<`.

        `${x:-<<E}` opened a heredoc whose delimiter was `E}`, the closing line
        never came, and every line below it was swallowed as a body -- so a
        `git worktree add` bash really runs, `rc=0`, left the segment list
        entirely. 32 of 333 generated inputs failed open this way and every one
        was this family.
        """
        command = "echo ${x:-<<E}\ngit worktree add -b nb ../wt"
        items, clean = reader.split_segments_with_separators(
            reader.drop_heredoc_bodies(reader.drop_comments(command))
        )
        assert clean, command
        words = [tokens for _, tokens in items]
        assert any(t[:2] == ["git", "worktree"] for t in words), (
            f"the `git worktree add` left the segment list: {words}"
        )

    def test_accepts_a_heredoc_opened_after_an_unbalanced_expansion(self):
        """The guard the fix above needed, and the reason it is not one word.

        Adding `not braces` alone would let an UNBALANCED `${` hold the count to
        the end of the input, hiding every heredoc opener after it and reading a
        body as commands -- the fail-OPEN direction, and the opposite of what the
        count exists for. So an expansion counts only when a `}` closes it."""
        command = "echo ${x <<EOF\ncd /elsewhere\nEOF\ngit commit -m x"
        items, clean = reader.split_segments_with_separators(
            reader.drop_heredoc_bodies(reader.drop_comments(command))
        )
        assert clean, command
        words = [tokens for _, tokens in items]
        assert not any("cd" in t for t in words), (
            f"the heredoc body was read as commands: {words}. An unbalanced "
            "`${` must not hold the brace count open"
        )


class Test__bind:
    def test_refuses_a_subshell_of_its_own_accord(self):
        """`_bind`'s subshell guard is asserted at the unit, because the walk's
        `understood` check already refuses these and would keep the guard green
        if it were deleted — measured, removing it turns no case in this file red.

        Two things refusing one shape is deliberate: bash discards a subshell's
        assignments when it exits, so `(SB=/inside)` is wrong about bash and not
        only about what this reader can follow.
        """
        assert reader._bind({}, ["(SB=/inside)"]) == {}
        assert reader._bind({}, ["{", "SB=/inside"]) == {}
        assert reader._bind({}, ["SB=/inside"]) == {"SB": "/inside"}

    def test_accepts_only_a_bare_name_operand_as_forgotten(self):
        """The other side of `_forget`'s permissiveness.

        Forgetting costs a prompt and keeping costs a repository nobody reviewed,
        so it leans toward forgetting -- but it must still be reading operands
        rather than dropping the environment whenever a name-writer appears."""
        kept = reader._bind({"SB": "/one"}, shlex.split("read SB.x"))
        assert kept.get("SB") == "/one", (
            "`SB.x` is not the name `SB`, and forgetting on it makes every "
            "name-writer segment a full reset"
        )
        kept = reader._bind({"SB": "/one"}, shlex.split("read OTHER"))
        assert kept.get("SB") == "/one", "a name-writer forgot a name it never named"

    def test_the_subshell_refusal_forgets_rather_than_keeps(self):
        """`_bind`'s own subshell guard, reached directly.

        `( SB=/two )` is caught twice over -- the walk excludes a subshell join
        and `_bind` refuses one of its own accord -- so a mutation to either
        alone leaves the other standing. This calls `_bind` with the tokens, so
        the guard inside it is the only thing answering.
        """
        kept = reader._bind({"SB": "/one"}, shlex.split("( SB=/two )"))
        assert "SB" not in kept, (
            "`_bind`'s subshell guard returned the environment untouched, so a "
            "value from before the subshell survives it. Refusing to take a name "
            "and keeping the old one is the confident wrong answer"
        )
        # And the same for the branch that refuses a segment which runs something.
        kept = reader._bind({"SB": "/one"}, shlex.split("export SB=/two"))
        assert "SB" not in kept

    def test_an_array_assignment_empties_the_name(self):
        """`SB=(/three)` makes an array whose `$SB` is `/three`, and the reader
        bound the text between the parens: `git -C "$SB"` composed `(/three)`
        onto the session directory. Unmodelled, so the name is emptied."""
        kept = reader._bind({"SB": "/one"}, shlex.split("SB=(/three)"))
        assert "SB" not in kept, "an array assignment kept the value from before it"
        where = targets('SB=(/three); git -C "$SB" commit -m x')
        assert any("$SB" in w for w in where), where


class Test__substitute:
    def test_accepts_a_bound_name_and_leaves_every_other_standing(self):
        """`verify`'s second condition, at the unit that does the work.

        `_substitute` returning its operand unchanged would leave every case above
        green except the six that now resolve, and one that filled every `$`
        would take S3 and S4 with it. Both directions are asserted here.
        """
        assert reader._substitute("$SB/r1", {"SB": "/x"}) == "/x/r1"
        assert reader._substitute("${SB}/r1", {"SB": "/x"}) == "/x/r1"
        assert reader._substitute("$SB", {}) == "$SB"
        assert reader._substitute("$WT", {"SB": "/x"}) == "$WT"
        assert reader._substitute("${SB:-/y}", {"SB": "/x"}) == "${SB:-/y}"
        assert reader._substitute("$SBX", {"SB": "/x"}) == "$SBX"
        assert reader._substitute("/plain/path", {"SB": "/x"}) == "/plain/path"

    def test_refuses_to_rescan_a_value_holding_a_dollar(self):
        """One pass, so nothing here loops: what a substitution writes is not
        read again."""
        assert reader._substitute("$A", {"A": "$A", "B": "/x"}) == "$A"
        assert reader._substitute("$B", {"B": "$A/y", "A": "/loop"}) == "$A/y"


class Test_parse_git:
    def test_accepts_the_command_word_behind_a_list_opener(self, tmp_path):
        """`parse_git` is the one reading both gates and the consent writer use,
        so a switch or a creation in a loop body is read as one too."""
        for tokens, sub in (
            (["do", "git", "switch", "main"], "switch"),
            (["then", "!", "git", "worktree", "add", "../wt"], "worktree"),
            (["else", "{", "git", "checkout", "main"], "checkout"),
        ):
            parsed = cmdline.parse_git(tokens)
            assert parsed and parsed[0] == sub, tokens

    def test_refuses_a_subshell_with_no_subcommand_as_a_git_invocation(self):
        """`parse_git` documents "None when no subcommand", and stripping the
        closing parenthesis could leave the empty string instead — a value that
        reads as a subcommand to anything testing it for identity."""
        assert reader.parse_git(["(", "git", ")"]) is None
        assert reader.parse_git(["(git", ")"]) is None
        assert reader.parse_git(["git"]) is None

    def test_a_redirection_with_nothing_after_it_keeps_the_base_subcommand(self):
        """The same rule one scan over: `git 2>/dev/null` names no subcommand past
        the redirection, so the answer `86256492` gave is the one returned."""
        assert cmdline.parse_git(["git", "2>/dev/null"]) == ("2>/dev/null", [], [])
        assert cmdline.parse_git(["git", "2>/dev/null", "commit"]) == (
            "commit",
            [],
            [],
        )

    def test_a_glued_config_env_reads_as_it_did(self):
        assert cmdline.parse_git(["git", "--config-env=k=v", "commit", "-m", "x"]) == (
            "commit",
            ["-m", "x"],
            [],
        )


class Test_header_end:
    @pytest.mark.parametrize("name", sorted(HEADERS))
    def test_accepts_each_header_spelling_at_the_word_its_command_starts(self, name):
        tokens, want = HEADERS[name]
        want = cmdline.UNPLACEABLE if want == U else want
        assert cmdline.header_end(tokens) == want, name

    def test_refuses_a_header_spelling_it_cannot_place_as_unplaceable(self):
        """#674, `spec.md` *Two stand-ins*. A header the positional reading does
        not recognise is read the way `86256492` read every header for `git`: any
        later `watch` counts as the program, and any later word that expands counts
        as the string's command word. A false one is a stop, never a silence."""
        tokens = ["case", "a", "b", "watch", "-g", "$CMD"]
        assert cmdline.header_end(tokens) == cmdline.UNPLACEABLE
        assert cmdline.command_strings(tokens) == ["$CMD"]
        assert cmdline.names_an_unknown_command("case a b echo $CMD")
        # A redirection's target is a file, and the stand-in does not count it.
        assert not cmdline.names_an_unknown_command('case a b echo >"$LOG"')


class Test_merged_view:
    @pytest.mark.parametrize("name", sorted(MERGED))
    def test_accepts_the_cut_operators_glued_back(self, name):
        """#674, `spec.md` decision 3: the cut operators glued back, as a view."""
        command, tokens = MERGED[name]
        items, _clean = cmdline.split_segments_with_separators(command)
        groups = cmdline.merged_view(items)
        assert [g[1] for g in groups] == [tokens], name

    @pytest.mark.parametrize("name", sorted(SEPARATE))
    def test_refuses_to_glue_across_a_real_separator(self, name):
        """A background job, a pipe and a list are not redirections, and the
        view never glues across one."""
        command, groups = SEPARATE[name]
        items, _clean = cmdline.split_segments_with_separators(command)
        assert [g[1] for g in cmdline.merged_view(items)] == groups, name


class Test_names_an_unknown_command:
    def test_accepts_an_unknown_command_word_as_named_and_no_structural_one(self):
        assert cmdline.names_an_unknown_command("$CMD a")
        assert cmdline.names_an_unknown_command("echo; ${X} b")
        for text in (
            "[ -f x ] && echo y",
            "{ echo y; }",
            "echo $X",
            "if true; then :; fi",
        ):
            assert not cmdline.names_an_unknown_command(text), text

    @pytest.mark.parametrize("header", ["case a in a) ", "f() { ", "coproc "])
    def test_refuses_to_read_past_the_header_bound(self, header):
        """Round 1 of 1790660768, red 2. Past `HEADERS_READ` headers, one inside
        the next, both header readings answer in the stopping direction; one
        header fewer, the same segment is read to its end and names nothing."""

        bound = cmdline.HEADERS_READ
        for depth, expected in ((bound - 1, False), (bound, True)):
            tokens = (header * depth + "true watch").split()
            assert cmdline._is_the_program(tokens, len(tokens) - 1) is expected, depth
            assert cmdline.names_an_unknown_command(header * depth + "true") is expected


test_census = census_case(TARGET)
