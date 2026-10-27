"""The one heredoc shape `hooks/one_heredoc.py` admits, slot by slot, a string
that fails each of its clauses A-E, and every admitted string cut where a real
shell cuts it (#739, #763).

Work item `1791089603-one-heredoc-shape-the-reader-matches-exactly-is-data`,
`frame/design.md` *The shape*, scenario S4's reader half and S6 with Q3. Every admitted
string here comes back as its reduced text, and every string that fails one
clause comes back as None, which is what makes the gate read it as before. The
gate's half of S4 is in `tests/test_cmdline.py`, read without git, and in
`tests/test_commit_review_gate.py::Test_main`.

The reader decides where a body ends with an exact line comparison and no
shell lexer. That is a claim about bash and zsh, and the shell rows measure it
rather than trusting it: a generated corpus of in-shape commands, each a sink
that writes the body to a file, is run through each shell, directly and
through `eval` (the harness hands a command to the shell one of those two
ways). For every string the reader admits, the file the shell wrote must be
the reader's body byte for byte, and no marker a body line would create may
exist. A body line the shell took for the terminator would have run the next
line, `: > m<n>`, as a command.

The corpus is built over clause C's axes: near-terminator lines with a
trailing blank, a leading or trailing tab, a `#` tail, quotes, a doubled
delimiter, a carriage return and a backslash at the line's end; a body line
containing the delimiter; an empty body and a body of one empty line; and the
terminator at end of input with and without a newline. Every candidate is
built in shape, so the reader must admit exactly those without a banned byte,
and a case checks that first: a reader that stopped admitting would otherwise
pass the shell rows by comparing nothing.

The program arm, `python3 -`, is run too, for clauses E and F: the lines after
its terminator are the suffix the gate reads, so the shell must run those and
no line of the body. Its body holds the same near lines, each followed by a
line that creates a marker. Python refuses such a body as a syntax error
before running any of it, and the shell has already decided where the body
ended, so the markers that exist are the lines the shell ran as commands:
exactly the suffix's, in the directory its `cd` names. They are compared with
the markers the reader's reduced text names.

The strings are harmless: `cat`, `tee`, `python3` refusing a program it
cannot compile, a `cd` into a directory the case made, and `: >` to create a
marker. Nothing here commits. Each shell is found by
`conftest.shell_probe` and skipped by name where it is not one, and its
startup files are kept out by pointing `HOME` and `ZDOTDIR` at the case's own
directory.
"""

import ast
import os
import shutil
import subprocess

import pytest
from conftest import census_case, load_hook_module, shell_probe

TARGET = "hooks/one_heredoc.py"

reader = load_hook_module("one_heredoc.py", "one_heredoc_exactly")

HOOK = os.path.join(os.path.dirname(__file__), "..", "hooks", "one_heredoc.py")

# A body the shell reading would find a commit in, on a line of its own.
BODY = "say `git commit` later\ngit commit -m x"

SINKS = ["cat > {w}", "cat >> {w}", "tee {w}", "tee -a {w}"]
PROGRAMS = ["python3 -", "python3 - {w}", "python3 - {w} {w}"]
WORDS = ["note.md", "./a/b-c_d.txt", "'a dir/with $ and `x`'"]
LEADS = ["", "cd /x/y && ", "cd '/Users/x/a b' && "]


def admitted():
    for lead in LEADS:
        for word in WORDS:
            for consumer in SINKS + PROGRAMS:
                yield lead + consumer.format(w=word)


# Each string below fails exactly the clause it is filed under, and carries a
# commit-bearing body, so None here is the gate reading it as before. The
# commit is in a body and nowhere else: one after the terminator is judged
# where it lands, which is not what these strings are about.
FAILS = {
    # A. Bytes where a reader and some shell were measured or can be shown to
    # disagree, anywhere in the command.
    "A: a carriage return in the body": f"cat > f <<'EOF'\n{BODY}\r\nEOF",
    "A: a carriage return on the terminator": f"cat > f <<'EOF'\n{BODY}\nEOF\r\nEOF",
    "A: a carriage return ending line 1": f"cat > f <<'EOF'\r\n{BODY}\nEOF",
    "A: a NUL in the body": f"cat > f <<'EOF'\n\0{BODY}\nEOF",
    "A: a backslash-newline in the body": f"cat > f <<'EOF'\nx\\\n{BODY}\nEOF",
    "A: a backslash-newline before the terminator": f"cat > f <<'EOF'\n{BODY}\\\nEOF",
    "A: a backslash-newline in a program's suffix": (
        f"python3 - <<'EOF'\n{BODY}\nEOF\necho \\\nx"
    ),
    # B. The first line, character for character.
    "B: a space before the line": f" cat > f <<'EOF'\n{BODY}\nEOF",
    "B: two spaces": f"cat  > f <<'EOF'\n{BODY}\nEOF",
    "B: a tab": f"cat >\tf <<'EOF'\n{BODY}\nEOF",
    "B: a glued redirection": f"cat >f <<'EOF'\n{BODY}\nEOF",
    "B: a glued opener": f"cat > f<<'EOF'\n{BODY}\nEOF",
    "B: an unquoted delimiter": f"cat > f <<EOF\n{BODY}\nEOF",
    "B: a double-quoted delimiter": f'cat > f <<"EOF"\n{BODY}\nEOF',
    "B: a partly quoted delimiter": f"cat > f <<E'OF'\n{BODY}\nEOF",
    "B: an ANSI-C delimiter": f"cat > f <<$'EOF'\n{BODY}\nEOF",
    "B: a backslash delimiter": f"cat > f <<\\EOF\n{BODY}\nEOF",
    "B: the tab-stripping opener": f"cat > f <<-'EOF'\n{BODY}\nEOF",
    "B: a blank in the delimiter": f"cat > f <<'E F'\n{BODY}\nE F",
    "B: a dash in the delimiter": f"cat > f <<'E-F'\n{BODY}\nE-F",
    "B: an empty delimiter": f"cat > f <<''\n{BODY}\n",
    "B: text after the delimiter": f"cat > f <<'EOF' && echo\n{BODY}\nEOF",
    "B: a trailing space after the delimiter": f"cat > f <<'EOF' \n{BODY}\nEOF",
    "B: a comment after the delimiter": f"cat > f <<'EOF' #x\n{BODY}\nEOF",
    "B: a glued # after the delimiter": f"cat > f <<'EOF'#x\n{BODY}\nEOF#x",
    "B: cat to standard output": f"cat <<'EOF'\n{BODY}\nEOF",
    "B: a shell consumer": f"bash <<'EOF'\n{BODY}\nEOF",
    "B: an unversioned python": f"python - <<'EOF'\n{BODY}\nEOF",
    "B: a python flag": f"python3 -u - <<'EOF'\n{BODY}\nEOF",
    "B: python3 -c": f"python3 -c 'import os' <<'EOF'\n{BODY}\nEOF",
    "B: python3 without -": f"python3 <<'EOF'\n{BODY}\nEOF",
    "B: a flag after python3 -": f"python3 - -c x <<'EOF'\n{BODY}\nEOF",
    "B: a parameter as the target": f"cat > \"$F\" <<'EOF'\n{BODY}\nEOF",
    "B: a bare parameter as the target": f"cat > $F <<'EOF'\n{BODY}\nEOF",
    "B: a parameter as the program's argument": f"python3 - $F <<'EOF'\n{BODY}\nEOF",
    "B: a glob in the target": f"cat > *.md <<'EOF'\n{BODY}\nEOF",
    "B: a tilde in the target": f"cat > ~/f <<'EOF'\n{BODY}\nEOF",
    "B: a double-quoted target": f"cat > \"f\" <<'EOF'\n{BODY}\nEOF",
    "B: an assignment LEAD": f"F=/x && cat > f <<'EOF'\n{BODY}\nEOF",
    "B: an assignment prefix": f"F=/x cat > f <<'EOF'\n{BODY}\nEOF",
    "B: a substitution in the LEAD": f"cd $(ls -d /x) && cat > f <<'EOF'\n{BODY}\nEOF",
    "B: a LEAD joined by ;": f"cd /x; cat > f <<'EOF'\n{BODY}\nEOF",
    "B: two LEADs": f"cd /x && cd y && cat > f <<'EOF'\n{BODY}\nEOF",
    "B: a pipe after the sink": f"cat > f <<'EOF' | sh\n{BODY}\nEOF",
    "B: a second redirection": f"cat > f 2>&1 <<'EOF'\n{BODY}\nEOF",
    "B: tee to two files": f"tee a b <<'EOF'\n{BODY}\nEOF",
    "B: the opener on line 2": f"echo hi\ncat > f <<'EOF'\n{BODY}\nEOF",
    "B: no newline at all": "cat > f <<'EOF'",
    # C. The terminator: a line exactly D, and nothing stripped first.
    "C: no terminator": f"cat > f <<'EOF'\n{BODY}",
    "C: only a terminator with a trailing blank": f"cat > f <<'EOF'\n{BODY}\nEOF ",
    "C: only an indented terminator": f"cat > f <<'EOF'\n{BODY}\n\tEOF",
    "C: only a terminator with a # tail": f"cat > f <<'EOF'\n{BODY}\nEOF #",
    # D. Exactly one `<<` outside the body.
    "D: a second heredoc in the suffix": (
        f"python3 - <<'EOF'\nprint(1)\nEOF\nbash <<'X'\n{BODY}\nX"
    ),
    "D: a here-string in the suffix": (f"python3 - <<'EOF'\n{BODY}\nEOF\ncat <<< x"),
    "D: an arithmetic shift in the suffix": (
        f"python3 - <<'EOF'\n{BODY}\nEOF\nn=$((1<<2))"
    ),
    "D: a `<<` inside a quoted WORD": f"cat > 'a<<b' <<'EOF'\n{BODY}\nEOF",
    # E. After a sink, nothing but newlines.
    "E: a command after a sink": f"cat > f <<'EOF'\n{BODY}\nEOF\necho done",
    "E: a command after a sink's blank line": (
        f"cat > f <<'EOF'\n{BODY}\nEOF\n\nbash f"
    ),
    "E: a space after a sink": f"cat > f <<'EOF'\n{BODY}\nEOF\n ",
    "E: a comment after a sink": f"tee f <<'EOF'\n{BODY}\nEOF\n# done",
}


# --- the shell's half: the corpus and how one string is run ------------------

DELIMITERS = ["EOF", "x_9"]

# (first line without the opener, the file the body lands in, relative to the
# directory the shell starts in)
HEADS = [
    ("cat > out", "out"),
    ("cat >> out", "out"),
    ("tee -a out", "out"),
    ("cd 'a b' && tee 'o u t'", os.path.join("a b", "o u t")),
]


def near_lines(d):
    """Lines a reader could mistake for the terminator, or the delimiter
    standing inside a longer line."""
    return [
        f"{d} ",
        f" {d}",
        f"\t{d}",
        f"{d}\t",
        f"{d}#x",
        f"{d} #x",
        f"'{d}'",
        f'"{d}"',
        f"{d}{d}",
        f"{d};",
        f"{d})",
        f"x{d}",
        f"{d}x",
        f"$({d})",
        f"`{d}`",
        f"<<{d}",
        f"{d}\r",
        f"{d}\\",
    ]


def bodies(d):
    """Each body as its lines. Every near line is followed by a line that
    creates a marker, so a shell that ended the body early runs it."""
    out = []
    for i, line in enumerate(near_lines(d)):
        out.append([line, f": > m{i}"])
    out.append([x for i, line in enumerate(near_lines(d)) for x in (line, f": > n{i}")])
    out += [
        [],
        [""],
        ["", "", ": > e0"],
        [f"cat > f <<'{d}'", ": > e1"],
        ["$(: > e2)", "`: > e3`", "${x:=y}", "a\\b", "!!", "é ü 漢"],
        ["   ", "\t", "#", f"# {d}"],
        [d.swapcase(), f"{d.swapcase()}x", ": > e4"],
        # Banned by clause A, so the reader admits none of these and nothing
        # compares them. They are here so that deleting a ban puts them in
        # front of the shells rather than nowhere.
        ["x\\"],
        ["x\\", ": > e5"],
        ["x\r", ": > e6"],
    ]
    return out


ENDS = ["", "\n", "\n\n"]


def corpus():
    """(command, file, body lines) for every combination."""
    rows = []
    for d in DELIMITERS:
        for head, target in HEADS:
            for lines in bodies(d):
                for end in ENDS:
                    text = "".join(line + "\n" for line in lines)
                    rows.append((f"{head} <<'{d}'\n{text}{d}{end}", target, lines))
    return rows


BANNED = ("\r", "\0", "\\\n")

MODES = {
    "directly": lambda cmd: ["-c", cmd],
    "through eval": lambda cmd: ["-c", 'eval "$1"', "sh", cmd],
}


def run_one(shell, mode, command, target, home):
    work = home / "w"
    if work.exists():
        shutil.rmtree(work)
    (work / "a b").mkdir(parents=True)
    env = {
        k: v for k, v in os.environ.items() if k not in ("BASH_ENV", "ENV", "CDPATH")
    }
    env.update(HOME=str(home), ZDOTDIR=str(home))
    done = subprocess.run(
        [shell, *MODES[mode](command)],
        cwd=work,
        env=env,
        capture_output=True,
        timeout=30,
    )
    path = work / target
    wrote = path.read_bytes() if path.is_file() else None
    markers = sorted(
        os.path.relpath(os.path.join(root, name), work)
        for root, _, names in os.walk(work)
        for name in names
        if os.path.join(root, name) != str(path)
    )
    return done.returncode, wrote, markers


# (first line without the opener, the directory the suffix runs in, relative
# to the directory the shell starts in)
PROGRAM_HEADS = [
    ("python3 -", "."),
    ("python3 - 'q a' x.md", "."),
    ("cd 'a b' && python3 -", "a b"),
]

SUFFIXES = [": > s", ": > s\n: > t\n"]


def program_corpus():
    """(command, directory the suffix runs in) for every admitted
    combination: one near line and its marker per body, and one body of every
    near line clause A admits, each followed by its marker. That body is the
    only place near lines follow one another."""
    rows = []
    for d in DELIMITERS:
        near = near_lines(d)
        bodies_ = [[line, f": > m{i}"] for i, line in enumerate(near)]
        kept = [line for line in near if not any(b in line + "\n" for b in BANNED)]
        bodies_.append([x for i, line in enumerate(kept) for x in (line, f": > n{i}")])
        for head, where in PROGRAM_HEADS:
            for lines in bodies_:
                for suffix in SUFFIXES:
                    text = "".join(line + "\n" for line in lines)
                    command = f"{head} <<'{d}'\n{text}{d}\n{suffix}"
                    if reader.reduce(command) is not None:
                        rows.append((command, where))
    return rows


def suffix_markers(reduced, where):
    """The marker files the reduced text's own lines create, read the way
    its suffix is written: one `: > NAME` per line, after the first."""
    names = []
    for line in reduced.split("\n")[1:]:
        if line.startswith(": > "):
            names.append(os.path.normpath(os.path.join(where, line[4:])))
    return sorted(names)


class Test_reduce:
    # --- what is admitted ----------------------------------------------------

    @pytest.mark.parametrize("head", sorted(set(admitted())))
    def test_accepts_each_slot_of_the_first_line(self, head):
        """S4: each sink form, the program with and without arguments, a plain
        and a single-quoted WORD, with and without the LEAD."""
        for end in ("EOF", "EOF\n", "EOF\n\n"):
            command = f"{head} <<'EOF'\n{BODY}\n{end}"
            assert reader.reduce(command) == head, repr(command)
            assert reader._match(command) == (head, BODY + "\n"), repr(command)

    @pytest.mark.parametrize("delimiter", ["EOF", "A", "_", "9", "x_Y_1"])
    def test_accepts_every_delimiter_of_the_alphabet(self, delimiter):
        command = f"cat > f <<'{delimiter}'\nbody\n{delimiter}"
        assert reader._match(command) == ("cat > f", "body\n")

    def test_accepts_an_empty_body_as_a_body(self):
        assert reader._match("cat > f <<'EOF'\nEOF") == ("cat > f", "")
        assert reader._match("cat > f <<'EOF'\nEOF\n") == ("cat > f", "")
        assert reader._match("cat > f <<'EOF'\n\nEOF\n") == ("cat > f", "\n")

    def test_accepts_a_body_that_ends_at_the_first_exact_line(self):
        """C: every line that is not exactly D stays in the body, and the first
        one that is ends it."""
        near = ["EOF ", " EOF", "\tEOF", "EOF\t", "EOF#x", "'EOF'", "EOFEOF", "EOF;"]
        body = "\n".join(near)
        command = f"tee f <<'EOF'\n{body}\nEOF\n"
        assert reader._match(command) == ("tee f", body + "\n")

    def test_accepts_a_programs_suffix_and_drops_the_body(self):
        """E and F: after `python3 -`, what follows the terminator is a suffix,
        and the reduced text is the first line, a newline, and that suffix."""
        command = (
            "cd /x && python3 - a.md <<'EOF'\n"
            f"{BODY}\nEOF\ngrep -c x a.md\ngit -C /x commit -m y\n"
        )
        assert reader.reduce(command) == (
            "cd /x && python3 - a.md\ngrep -c x a.md\ngit -C /x commit -m y\n"
        )

    def test_accepts_a_programs_terminator_followed_only_by_newlines(self):
        for end in ("EOF", "EOF\n"):
            got = reader.reduce(f"python3 - <<'EOF'\n{BODY}\n{end}")
            assert got == "python3 -"
            assert "commit" not in got

    def test_accepts_every_in_shape_string_without_a_banned_byte(self):
        """The corpus is what the shell half compares, so it must not shrink:
        every candidate is in shape, and only clause A's bytes keep one out."""
        rows = corpus()
        admitted = [c for c, _, _ in rows if reader.reduce(c) is not None]
        expected = [c for c, _, _ in rows if not any(b in c for b in BANNED)]
        assert admitted == expected
        assert len(admitted) > 500, len(admitted)

    def test_accepts_the_program_corpus_and_keeps_its_suffix(self):
        rows = program_corpus()
        assert len(rows) > 150, len(rows)
        # The body of every admitted near line, under each delimiter, head and
        # suffix: if clause A refused it, nothing would compare it.
        combined = [command for command, _ in rows if ": > n1\n" in command]
        assert len(combined) == len(DELIMITERS) * len(PROGRAM_HEADS) * len(SUFFIXES)
        for command, where in rows:
            reduced = reader.reduce(command)
            assert suffix_markers(reduced, where), command

    # --- the real shells agree ----------------------------------------------

    @pytest.mark.rule("one-heredoc-shape-is-data")
    @pytest.mark.parametrize("mode", sorted(MODES))
    @pytest.mark.parametrize("shell", ["bash", "zsh"])
    def test_accepts_only_what_the_shell_cuts_where_the_reader_does(
        self, shell, mode, tmp_path
    ):
        why = shell_probe(shell)
        if why is not None:
            pytest.skip(f"{shell}: {why}")
        disagreements = []
        compared = 0
        for command, target, _lines in corpus():
            found = reader._match(command)
            if found is None:
                continue
            compared += 1
            code, wrote, markers = run_one(shell, mode, command, target, tmp_path)
            expected = found[1].encode("utf-8")
            if code != 0 or wrote != expected or markers:
                disagreements.append(
                    f"{command!r}: exit {code}, wrote {wrote!r}, "
                    f"reader {expected!r}, other files {markers}"
                )
        assert compared > 500, compared
        assert not disagreements, (
            f"{len(disagreements)} of {compared} admitted strings cut differently "
            f"by {shell} {mode}:\n" + "\n".join(disagreements[:20])
        )

    @pytest.mark.parametrize("mode", sorted(MODES))
    @pytest.mark.parametrize("shell", ["bash", "zsh"])
    def test_accepts_a_programs_suffix_the_shell_runs_and_no_line_of_its_body(
        self, shell, mode, tmp_path
    ):
        """Clauses E and F, measured: after `python3 -`'s terminator the shell
        runs exactly the lines the reduced text keeps, and none of the body."""
        why = shell_probe(shell)
        if why is not None:
            pytest.skip(f"{shell}: {why}")
        if shutil.which("python3") is None:
            pytest.skip("python3 is not on PATH here, so the program arm cannot run")
        disagreements = []
        rows = program_corpus()
        for command, where in rows:
            expected = suffix_markers(reader.reduce(command), where)
            _code, _wrote, markers = run_one(shell, mode, command, "", tmp_path)
            if markers != expected:
                disagreements.append(f"{command!r}: ran {markers}, reader {expected}")
        assert not disagreements, (
            f"{len(disagreements)} of {len(rows)} program strings ran differently "
            f"in {shell} {mode}:\n" + "\n".join(disagreements[:20])
        )

    # --- what is refused -----------------------------------------------------

    @pytest.mark.rule("one-heredoc-shape-is-data")
    @pytest.mark.parametrize("name", sorted(FAILS))
    def test_refuses_a_string_that_fails_one_clause(self, name):
        assert reader.reduce(FAILS[name]) is None, repr(FAILS[name])
        assert reader._match(FAILS[name]) is None

    @pytest.mark.parametrize("value", [None, b"cat > f <<'EOF'\nx\nEOF", 1])
    def test_refuses_a_command_that_is_not_text(self, value):
        assert reader.reduce(value) is None

    def test_refuses_a_sink_with_text_after_a_body_line_equal_to_the_delimiter(
        self,
    ):
        """C, from the other side: the reader does not look inside the body for
        quotes, so a delimiter line inside what looks like a string still ends
        the body -- and a sink with anything after that is no match (E)."""
        command = "cat > f <<'EOF'\ns = '''\nEOF\n'''\nEOF"
        assert reader.reduce(command) is None


class Test_module:
    def test_the_reader_imports_nothing_but_re(self):
        """The owner's instruction that the decision not rest on the shared
        splitter, made checkable: no `cmdline`, `cmdline_base` or `tokens`, and
        no shell lexer."""
        with open(HOOK, encoding="utf-8") as f:
            tree = ast.parse(f.read())
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported |= {a.name for a in node.names}
            elif isinstance(node, ast.ImportFrom):
                imported.add(node.module)
        assert imported == {"re"}, imported


test_census = census_case(TARGET)
