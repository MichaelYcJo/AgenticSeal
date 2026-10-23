"""`hooks/cmdline.py`, the commit gate's reading of a command's text, one
class per function the old cases call by name.

Every case here reads a command with no git and no shell, through the reader
itself or through the commit gate's `commit_invocations`, which hands the
command to this module; a case of the second kind is `Test_module`'s. The
cases moved here as they stood, under `questions.md` Q1 of #942, and #1014
decides the reading's future. They came from these files, by #942's phase 6:

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

`SHAPES` and `HERE` are read by `tests/test_commit_review_gate.py::Test_main`,
which runs the gate's `main` over the same shapes against real git.
"""

import functools
import os
import sys

import pytest
from conftest import HOOKS, census_case, commit_found, load_hook_module, sh
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


def unreadable(wheres):
    return [isinstance(w, reader.Unresolved) for w in wheres]


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
            assert unreadable(wheres) == [True], dest

    def test_a_subshell_does_not_hide_the_cd_by_hiding_the_word(self, tmp_path):
        """`(cd X && git commit)` tokenizes its first word as `(cd`, so the cd was
        invisible while the commit was not — the fail-open reproduced with one
        parenthesis. Where the commit runs cannot be read, so it is not read."""
        wheres = commit_dirs(f"(cd {sh(tmp_path / 'b')} && git commit -m x)", tmp_path)
        assert wheres and all(unreadable(wheres)), wheres

    def test_cd_dash_goes_back_to_the_directory_before_it(self, tmp_path):
        command = f"cd {sh(tmp_path / 'b')} && cd - && git commit -m x"
        assert commit_dirs(command, tmp_path) == [str(tmp_path)]

    def test_cd_dash_with_nothing_behind_it_is_unreadable(self, tmp_path):
        wheres = commit_dirs("cd - && git commit -m x", tmp_path)
        assert unreadable(wheres) == [True]

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
