"""`hooks/commit-review-gate.py`, one class per function the old cases reach.

Rebuilt from the code by #942's phase 5. The gate's own units run on text in
the process: the bounded body reader, the waiver read, the press reader and
the unreadable prompt. `main` runs in the process too, over five directories
built once for the module: an opted-in repository with no declaration, a
declared one, a declared one with a migration config, and a directory that
opted into nothing holding an opted-in repository. No case writes to them but
the gate's own choice marker, which is keyed by a session id each case makes
its own, so the session id is the reset. The press is a stub of the reader
`hooks/worktree_consent.py` owns, and whether git's hooks decide a clone is a
stub of `hooks/githooks.py#decides`; each of those modules has its own file.

How `hooks/cmdline.py` reads each shell shape stays where it stood, in
`tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`,
`tests/test_no_shape_the_base_stops_reads_silent.py` and
`tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py`, as reading cases
with no git, for the phase that rebuilds that module.
"""

import io
import json
import shlex
import sys
import types
import uuid

import pytest
from conftest import census_case, declare_routing, git, load_hook_module

TARGET = "hooks/commit-review-gate.py"

gate = load_hook_module("commit-review-gate.py", "crg_under_test")
Unresolved = gate.Unresolved

C = "git commit -m x"
WAIVER = "[no-review]"
CONSTRUCT = "contains something the gate cannot read as a plain command"
AUTOMATION = "pressed `automation` on the routing question"


def q(path):
    return shlex.quote(str(path))


def _repository(path, declared=False, parity=False):
    """An opted-in repository with one commit and a staged change."""
    path.mkdir(parents=True)
    git(path, "init", "-q")
    (path / "f").write_text("1\n", encoding="utf-8")
    git(path, "add", "f")
    git(
        path,
        "-c",
        "user.email=e@example.com",
        "-c",
        "user.name=e",
        "commit",
        "-qm",
        "b",
    )
    (path / "f").write_text("2\n", encoding="utf-8")
    git(path, "add", "f")
    (path / "seal").mkdir()
    (path / "sub").mkdir()
    if declared:
        declare_routing(path, review="straight to the PR")
    if parity:
        (path / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
        (path / "a.py").write_text("x = 1\n", encoding="utf-8")
        git(path, "add", "a.py")
    return path


@pytest.fixture(scope="module")
def world(tmp_path_factory):
    root = tmp_path_factory.mktemp("commit-review-gate")
    plain = root / "plain"
    (plain / "sub").mkdir(parents=True)
    return types.SimpleNamespace(
        root=root,
        undeclared=_repository(root / "undeclared"),
        declared=_repository(root / "declared", declared=True),
        parity=_repository(root / "parity", declared=True, parity=True),
        plain=plain,
        u2=_repository(plain / "u2"),
        missing=root / "missing",
    )


class _Press:
    """The press reader, answering for a session whose id says it pressed."""

    def automation_answered(self, top, session, transcript_path):
        return str(session).startswith("pressed")


@pytest.fixture(autouse=True)
def _the_press_is_read_off_the_session_id(monkeypatch):
    monkeypatch.setattr(gate, "worktree_consent", _Press())


def decision(monkeypatch, capsys, command, cwd, session=None):
    """`main` on one Bash call: the decision, `silent` where it printed
    nothing, and the reason."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": command},
        "cwd": str(cwd),
        "session_id": session or f"s-{uuid.uuid4().hex}",
    }
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps(payload)))
    gate.main()
    out = capsys.readouterr().out.strip()
    if not out:
        return "silent", ""
    said = json.loads(out)["hookSpecificOutput"]
    return said["permissionDecision"], said["permissionDecisionReason"]


def stops(monkeypatch, capsys, rows, cwd):
    """The rows `main` let through silent, by name."""
    return [
        name
        for name, command in rows.items()
        if decision(monkeypatch, capsys, command, cwd)[0] == "silent"
    ]


def unplaced(command, cwd="/x/session"):
    found, _clean = gate.commit_invocations(command, cwd)
    return [inv for inv in found if isinstance(inv.base, Unresolved)]


class Test__hides_a_commit:
    def test_accepts_a_body_nested_inside_the_bound_and_reads_it_through(self):
        depth = gate.NESTING_READ - 2
        around = "$(" * depth + "{}" + ")" * depth
        assert gate._hides_a_commit(around.format("true")) is False
        assert gate._hides_a_commit(around.format(C)) is True

    @pytest.mark.parametrize(
        ("opener", "closer"),
        [("$(echo ", ")"), ("<(cat ", ")"), ('"$(echo ', ')"')],
        ids=["$(", "<(", '"$('],
    )
    def test_refuses_to_read_past_the_bound(self, monkeypatch, opener, closer):
        """#674 S9: past `NESTING_READ` levels a body counts as one that might
        commit, at exactly the bound rather than at the recursion limit."""
        text = opener * 200 + "true" + closer * 200
        calls = []
        original = gate._reads_a_commit

        def counting(body):
            calls.append(1)
            return original(body)

        monkeypatch.setattr(gate, "_reads_a_commit", counting)
        assert gate._hides_a_commit(text) is True
        assert len(calls) == gate.NESTING_READ, len(calls)


class Test_commit_invocations:
    @pytest.mark.parametrize(
        "command",
        [
            C,
            f"exec {C}",
            f"2>/dev/null {C}",
            f"2>&1 {C}",
            "git>/dev/null commit -m x",
            "git 2>&1 commit -m x",
        ],
        ids=[
            "plain",
            "a runner",
            "a redirection",
            "a cut redirection",
            "glued",
            "inside",
        ],
    )
    def test_accepts_a_commit_where_the_shell_is(self, command):
        found, clean = gate.commit_invocations(command, "/x/session")
        assert clean and found, command
        assert all(inv.base == "/x/session" for inv in found), found

    def test_accepts_a_commit_the_splitter_found_once(self):
        """`git commit -m x 2>&1 | tail -1`: the glued view adds no second
        invocation of a kind its parts already found."""
        found, _ = gate.commit_invocations(f"{C} 2>&1 | tail -1", "/x/session")
        assert [(list(i.args), list(i.chdirs)) for i in found] == [
            (["-m", "x", "2>"], [])
        ]

    @pytest.mark.parametrize(
        "command",
        [
            f"nice -n 5 {C}",
            f"sh -c '{C}'",
            'sh -c "$CMD"',
            f"eval '{C}'",
            'eval "$X"',
            '2>/dev/null eval "$X"',
            'builtin eval "$X"',
            f"echo $({C})",
            f"echo $(2>/dev/null {C})",
            'sh -c 2>&1 "$CMD"',
            f"bash <<'EOF'\n{C}\nEOF",
            f"cat > f <<EOF\n{C}\nEOF",
            f"bash -c '2>&1 {C}'",
            f"bash <<'O'\nbash <<'I'\n{C}\nI\nO",
        ],
        ids=[
            "a runner's options",
            "a shell string",
            "a string's command word that expands",
            "eval",
            "an eval that expands",
            "an eval behind a redirection",
            "builtin eval",
            "a substitution",
            "a redirected commit in a substitution",
            "a string past a cut redirection",
            "a heredoc a shell runs",
            "a heredoc a file takes",
            "a cut redirection inside a string",
            "a heredoc inside a body a shell runs",
        ],
    )
    def test_refuses_to_place_a_commit_it_cannot_follow(self, command):
        hidden = unplaced(command)
        assert hidden, command
        assert all(inv.base.why == Unresolved.CONSTRUCT for inv in hidden), hidden

    def test_refuses_to_place_a_hidden_commit_behind_a_value_as_a_construct(self):
        """A string's commit run from a directory the shell names by a value
        keeps that value's reason, so the prompt can ask for the path."""
        hidden = unplaced(f"cd \"$X\" && sh -c '{C}'")
        assert hidden and all(inv.base.why == Unresolved.VALUE for inv in hidden)

    @pytest.mark.parametrize(
        "command",
        [
            "echo 'git commit'",
            f"# stage everything; then commit\n{C}",
            "echo '$(git commit -m x)'",
            'git commit -m "$(cat msg)"',
            "bash -c '[ -f x ] && echo y'",
            "for d in git commit; do :; done",
        ],
        ids=[
            "prose",
            "a comment",
            "a single-quoted substitution",
            "a message read by a substitution",
            "a shell string with no commit",
            "a word after for",
        ],
    )
    def test_refuses_to_read_a_commit_the_shell_does_not_run_unplaced(self, command):
        assert not unplaced(command), command

    def test_refuses_to_call_a_command_it_could_not_split_clean(self):
        found, clean = gate.commit_invocations("git commit -m 'x", "/x/session")
        assert clean is False and found


class Test_has_marker:
    @pytest.mark.parametrize(
        "command",
        [
            f": '{WAIVER}'; {C}",
            f"{C}  # {WAIVER}",
            f"cat > pr.md <<EOF\nbody\nEOF\n{C}  # {WAIVER}",
            f"python3 - <<'EOF'\nprint(1)\nEOF\n{C}  # {WAIVER}",
            f"cat > pr.md <<EOF\nbody\nEOF\n{C}  # {WAIVER} -- it's a probe",
        ],
        ids=[
            "the no-op in front",
            "a trailing comment",
            "a comment after a terminator",
            "a comment on the program's suffix",
            "an apostrophe after the waiver",
        ],
    )
    def test_accepts_a_waiver_typed_in_front_of_the_command(self, command):
        assert gate.has_marker(command, WAIVER), command

    @pytest.mark.parametrize(
        "command",
        [
            f'git commit -m "drop {WAIVER} later"',
            f"python3 - <<'EOF'\nnote = \"{WAIVER}\"\nEOF\n{C}",
            f"cat > pr.md <<EOF\n{WAIVER}\nEOF\n{C}",
            f"bash <<EOF\n: '{WAIVER}'; {C}\nEOF\n",
            f"cat > pr.md <<EOF\nbody\nEOF\n{C}  # don't {WAIVER}",
            f"git commit -m 'x {WAIVER}",
            f'git commit -m "x {WAIVER}',
            f'cat <<EOF\n"\nEOF\necho {WAIVER} "',
        ],
        ids=[
            "inside a message",
            "inside a program body",
            "inside a body outside the shape",
            "inside a body a shell runs",
            "behind an apostrophe in its comment",
            "inside a single quote that never closes",
            "inside a double quote that never closes",
            "a quote the body opens",
        ],
    )
    def test_refuses_a_waiver_that_is_not_a_bare_word_of_the_command(self, command):
        assert not gate.has_marker(command, WAIVER), command


class Test_automation_pressed:
    def test_accepts_a_press_the_reader_answers_true(self):
        assert gate.automation_pressed("/x/top", "pressed-1", "") is True

    @pytest.mark.parametrize(
        ("reader", "session"),
        [
            ("answers", ""),
            (None, "pressed-1"),
            ("raises", "pressed-1"),
            ("says yes", "pressed-1"),
        ],
        ids=["no session", "no reader", "a reader that raises", "an answer not True"],
    )
    def test_refuses_every_press_it_cannot_read(self, monkeypatch, reader, session):
        def raises(*_):
            raise OSError("unreadable")

        stand_ins = {
            "answers": _Press(),
            None: None,
            "raises": types.SimpleNamespace(automation_answered=raises),
            "says yes": types.SimpleNamespace(automation_answered=lambda *_: "yes"),
        }
        monkeypatch.setattr(gate, "worktree_consent", stand_ins[reader])
        assert gate.automation_pressed("/x/top", session, "") is False


class Test_unreadable_reason:
    def test_accepts_a_construct_and_offers_to_say_where_it_commits(self):
        paths = [Unresolved("/x/s", Unresolved.CONSTRUCT)] * 2
        reason = gate.unreadable_reason(paths, True, 0)
        assert CONSTRUCT in reason and "a directory it could not" not in reason
        assert "exactly these two options" in reason
        assert '"Say where it commits"' in reason
        assert reason.count("/x/s") == 1, "one path named twice"

    def test_refuses_to_offer_a_construct_way_for_a_value_beside_one(self):
        paths = [
            Unresolved("/x/s", Unresolved.CONSTRUCT),
            Unresolved("$X", Unresolved.VALUE),
        ]
        reason = gate.unreadable_reason(paths, True, 2)
        assert "2 directories it could not resolve" in reason
        assert '"Write the path out"' in reason
        assert "also commits into 2 further repositories" in reason

    def test_refuses_with_the_automation_ways_under_the_press(self):
        reason = gate.unreadable_reason(
            [Unresolved("$X", Unresolved.VALUE)], False, 0, True
        )
        assert AUTOMATION in reason and f"': '{WAIVER}'" not in reason
        assert f": '{WAIVER}'; <the same command>" in reason
        assert "AskUserQuestion" not in reason


def corpus(w, m, h):
    """`tests/test_no_shape_the_base_stops_reads_silent.py`'s rows: the
    shapes measured to leak the last time the reading was narrowed. The
    session directory is opted in and undeclared, and `w` is declared."""
    py = "import os,sys; os.system(sys.stdin.read())"
    perl = 'system(join("",<STDIN>))'

    def heredoc(head, delimiter="EOF"):
        return f"{head}\n{C}\n{delimiter}"

    deep = "$(" * 500 + "true" + ")" * 500
    return {
        "r2: a program flag after the heredoc": heredoc(f"python3 <<'EOF' -c {q(py)}"),
        "r2: a bundled -Bc": heredoc(f"python3 -Bc{q(py)} <<'EOF'"),
        "r2: perl -e after the heredoc": heredoc(f"perl <<'EOF' -e {q(perl)}"),
        "r2: $(...) before the interpreter": heredoc("sh -s $(true) python3 <<'EOF'"),
        "r2: ${...;...} before it": heredoc("sh -s ${x:-;X=} python3 - <<'EOF'"),
        "r2: >& before the interpreter": heredoc("sh -s >&python3 <<'EOF'"),
        "r2: control, bash reads stdin": heredoc("bash <<'EOF'"),
        "r2: control, -c before the heredoc": heredoc(f"python3 -c {q(py)} <<'EOF'"),
        "r2: mv, then cd": f"mv {q(w)} {q(m)} ; cd {q(w)} ; {C}",
        "r2: mv, then cd, on lines": f"mv {q(w)} {q(m)}\ncd {q(w)}\n{C}",
        "r2: chmod, then cd": f"chmod 000 {q(w)} ; cd {q(w)} ; {C}",
        "r2: control, a missing cd": f"cd {q(m)} ; {C}",
        "r3: # glued to the delimiter": heredoc(f"python3 <<EOF#x -c {q(py)}", "EOF#x"),
        "r3: # glued, quoted": heredoc(f"python3 <<'EOF'#x -c {q(py)}", "EOF#x"),
        "r3: perl, # glued": heredoc(f"perl <<EOF#x -e {q(perl)}", "EOF#x"),
        "r3: control, genuinely data": heredoc("python3 - <<EOF#x", "EOF#x"),
        "r3: $(...) in a prefix": f"X=$(mv {q(w)} {q(m)}) cd {q(w)} ; {C}",
        "r3: an invalid name prefix": f"a.b=1 cd {q(w)} ; {C}",
        "r3: a prefix, then a cd": (
            f"X=$(mv {q(w)} {q(m)}) cd {q(h)} ; cd {q(w)} ; {C}"
        ),
        "r3: control, cd then ;": f"cd {q(w)} ; {C}",
        "measured: a heredoc edit, then a commit on the next line": (
            f"cd {q(w)} && python3 - <<'EOF'\nprint(1)\nEOF\ngit add f && {C}"
        ),
        "measured: ; after cd, no heredoc": f"cd {q(w)} && true ; git add f && {C}",
        "measured: a body line equal to the delimiter ends it early": (
            f"cat > note.md <<'EOF'\nquoted:\nEOF\n{C}\nEOF"
        ),
        "r1: nice -C w, then $'...'": f"nice git -C {q(w)} commit -m x; echo $'it\\'s'; {C}",
        "r1: do -C w, then $'...'": (
            f"for d in a; do git -C {q(w)} commit -m x; done; echo $'it\\'s'; {C}"
        ),
        "r1: cd w && nice, then $'...'": f"cd {q(w)} && nice {C}; echo $'it\\'s'; {C}",
        "r1: timeout -C w, then $'...'": (
            f"timeout 5 git -C {q(w)} commit -m x; echo $'it\\'s'; {C}"
        ),
        "r1: 500 nested substitutions": f"{C}; echo {deep}",
    }


def moved_row(w):
    """The one row that left the corpus (work item 1791089603, Q1): the one
    heredoc shape, whose body is a program's text and not a command."""
    return (
        f"cd {q(w)} && python3 - <<'EOF'\ns = 'don\\'t'\n"
        f"for c in ['cd {w}; {C}']:\n    print(c)\nEOF"
    )


PY_BODY = (
    'note = """\nrun `git commit` later\ngit commit -m x\n"""\n'
    'open("m.md", "a", encoding="utf-8").write(note)'
)
PR_BODY = "quotes `git -C /x commit -m y`\ngit commit -m x"


def commit_into(repo):
    return f"git -C {q(repo)} add f && git -C {q(repo)} commit -m x"


class Test_main:
    def test_accepts_what_a_declared_repository_answers(
        self, monkeypatch, capsys, world
    ):
        d = world.declared
        rows = {
            "a plain commit": C,
            "a redirection read past": f"2>/dev/null {C}",
            "a cut redirection read past": "git 2>&1 commit -m x",
            "a spaced config env": "git --config-env core.hooksPath=VAR commit -m x",
            "a message read by a substitution": 'git commit -m "$(cat msg)"',
            "a value read before the commit": "x=$(git rev-parse HEAD) && git commit -m y",
            "no commit at all": "echo hi",
        }
        assert stops(monkeypatch, capsys, rows, d) == list(rows)

    @pytest.mark.rule("one-heredoc-shape-is-data")
    def test_accepts_the_one_heredoc_shape_as_data(self, monkeypatch, capsys, world):
        """Work item 1791089603: the body of the one shape is a program's
        text, so a commit it mentions stops nothing, and a commit after it is
        judged where it lands."""
        s, d = world.undeclared, world.declared
        rows = {
            "the moved row": moved_row(d),
            "refusal 1 as recorded": (
                f"cd {q(s)} && python3 - <<'EOF'\n{PY_BODY}\nEOF\ngrep -c git m.md"
            ),
            "a sink": f"cat > {q(world.root / 'pr.md')} <<'EOF'\n{PR_BODY}\nEOF\n",
            "tee with a lead": f"cd {q(s)} && tee -a 'a b.md' <<'EOF'\n{PR_BODY}\nEOF",
            "the program with arguments": f"python3 - x y <<'EOF'\n{PY_BODY}\nEOF",
            "refusal 3 into a declared repository": (
                f"cd {q(s)} && python3 - <<'EOF'\n{PY_BODY}\nEOF\n{commit_into(d)}"
            ),
            "the unparsed fallback reads the reduced text": (
                "python3 - <<'EOF'\nprint('git commit')\nEOF\necho $'it\\'s'"
            ),
        }
        assert stops(monkeypatch, capsys, rows, s) == list(rows)

    @pytest.mark.parametrize(
        "suffix", ["git commit -m x", "git -C {w} commit -m x", "echo done"]
    )
    def test_accepts_the_suffix_as_the_line_without_its_body(
        self, monkeypatch, capsys, world, suffix
    ):
        """Work item 1791089603 S7: after the program's body, the decision is
        the one the same line gets with the body taken out."""
        w = world.declared
        tail = suffix.format(w=q(w))
        whole = f"cd {q(w)} && python3 - <<'EOF'\n{PY_BODY}\nEOF\n{tail}"
        without = f"cd {q(w)} && python3 -\n{tail}"
        assert gate.one_heredoc.reduce(whole) == without
        here = world.undeclared
        got = decision(monkeypatch, capsys, whole, here)[0]
        assert got == decision(monkeypatch, capsys, without, here)[0]

    def test_accepts_a_waiver_typed_in_front_beside_a_body(
        self, monkeypatch, capsys, world
    ):
        s, u = world.declared, world.undeclared
        pr = q(world.root / "pr.md")
        rows = {
            "the no-op in front": f": '{WAIVER}'; cat > {pr} <<EOF\nbody\nEOF\n{commit_into(u)}",
            "a comment after the terminator": (
                f"cat > {pr} <<EOF\nbody\nEOF\n{commit_into(u)}  # {WAIVER}"
            ),
            "in front of a body a shell runs": (
                f": '{WAIVER}'; bash <<EOF\n{commit_into(u)}\nEOF\n"
            ),
        }
        assert stops(monkeypatch, capsys, rows, s) == list(rows)
        for name, command in rows.items():
            tokenless = command.replace(WAIVER, "later")
            assert decision(monkeypatch, capsys, tokenless, s)[0] == "deny", name

    def test_accepts_a_plain_commit_where_git_decides(self, monkeypatch, capsys, world):
        monkeypatch.setattr(gate.githooks, "decides", lambda root: bool(root))
        got = decision(monkeypatch, capsys, C, world.undeclared)
        assert got[0] == "silent", got

    def test_accepts_silence_where_the_session_opted_into_nothing(
        self, monkeypatch, capsys, world
    ):
        """An unreadable target speaks only from a session whose own
        repository opted in."""
        rows = {"an eval": 'eval "$X"', "a value": 'git -C "$X" commit -m x'}
        assert stops(monkeypatch, capsys, rows, world.plain) == list(rows)

    def test_refuses_each_kind_in_an_undeclared_repository(
        self, monkeypatch, capsys, world
    ):
        s = world.undeclared
        rows = {
            "a plain commit": C,
            "a runner": f"exec {C}",
            "a runner's options": f"nice -n 5 {C}",
            "a shell string": f"sh -c '{C}'",
            "a substitution": f"echo $({C})",
            "a redirection": f"2>/dev/null {C}",
            "a spaced config env": "git --config-env core.hooksPath=VAR commit -m x",
            "a cd to no repository": f"cd {q(world.plain)} && {C}",
            "a value": 'git -C "$X" commit -m x',
        }
        assert stops(monkeypatch, capsys, rows, s) == []

    def test_refuses_each_body_outside_the_one_shape(self, monkeypatch, capsys, world):
        """Work item 1791089603 S3 to S5: every body outside the one shape is
        read as shell, and the commit in it stops."""
        d = world.declared
        pr = q(world.root / "pr.md")
        rows = {
            "an assignment lead": (
                f"F={pr}; cat > \"$F\" <<'EOF'\n{PR_BODY}\nEOF\n"
                f'gh pr edit 1 --body-file "$F"'
            ),
            "a parameter argument": (
                f"F=$(ls -d {q(world.root)}/*.md) && python3 - \"$F\" <<'EOF'\n"
                f"{PY_BODY}\nEOF\n{commit_into(d)}"
            ),
            "an unquoted delimiter": f"cat > f <<EOF\n{C}\nEOF",
            "a backslash-newline in the delimiter word": f"cat > f <<'E\\\nOF'\n{C}\nEOF",
            "a consumer that runs its body": f"cat <<'EOF' | sh\n{C}\nEOF",
            "a writer, then a runner": f"cat > f.sh <<'EOF'\n{C}\nEOF\nbash f.sh",
            "a nested body": f"eval \"$(cat <<'EOF'\n{C}\nEOF\n)\"",
        }
        assert stops(monkeypatch, capsys, rows, d) == []
        got = decision(monkeypatch, capsys, rows["an assignment lead"], d)
        assert CONSTRUCT in got[1], got

    def test_refuses_where_the_commit_lands_after_the_one_shape(
        self, monkeypatch, capsys, world
    ):
        """Refusal 3 restated: the body says nothing of where the commit
        lands, so the stop names the repository the `-C` does."""
        u = world.undeclared
        command = f"cd {q(world.declared)} && python3 - <<'EOF'\n{PY_BODY}\nEOF\n{commit_into(u)}"
        got = decision(monkeypatch, capsys, command, world.declared)
        assert got[0] == "deny" and str(u) in got[1] and CONSTRUCT not in got[1], got

    def test_refuses_each_shape_the_base_stops(self, monkeypatch, capsys, world):
        """`docs/commit-review-gate-spec.md`: a change to the reading adds
        stops and never removes one."""
        s, d = world.undeclared, world.declared
        rows = corpus(d, world.root / "m", world.root)
        assert stops(monkeypatch, capsys, rows, s) == []

    def test_refuses_a_commit_that_leaves_a_declared_session(
        self, monkeypatch, capsys, world
    ):
        u = world.undeclared
        deep = "$(" * 500 + "true" + ")" * 500
        rows = {
            "the reverse direction": f"cd {q(u)} ; {C}",
            "a cd behind a redirection": f"2>/dev/null cd {q(u)} && {C}",
            "a pushd behind a redirection": f">/dev/null pushd {q(u)} && {C}",
            "a cd behind time and a redirection": f"time 2>/dev/null cd {q(u)} && {C}",
            "a cut redirection": f"2>&1 cd {q(u)} && {C}",
            "a commit found before a deep nesting": f"git -C {q(u)} commit -m x; echo {deep}",
            "a cd found before a deep nesting": f"cd {q(u)} && {C}; echo {deep}",
            "a commit found before deep headers": (
                f"git -C {q(u)} commit -m x; " + "case a in a) " * 1200 + "watch -g x"
            ),
        }
        assert stops(monkeypatch, capsys, rows, world.declared) == []

    def test_refuses_under_a_waiver_where_the_parity_arm_stands(
        self, monkeypatch, capsys, world
    ):
        """`[no-review]` waives an unresolved target whole, so a reading that
        put an unresolved directory in place of the session's own one lost the
        parity arm the session's repository still owes."""
        prefixes = [
            "2>/dev/null cd sub &&",
            ">/dev/null source /dev/null;",
            "2>/dev/null eval true;",
            "2>/dev/null $CMD;",
            "X=1 2>/dev/null cd sub &&",
            "2>/dev/null cd nosuch ||",
        ]
        rows = {p: f": '{WAIVER}'; {p} {C}" for p in prefixes}
        rows.update(
            {
                "a newly read substitution": f": '{WAIVER}'; echo $({C}) $'it\\'s'",
                "a newly read string": f": '{WAIVER}'; sh -c '{C}'; echo $'it\\'s'",
                "a parked failure": f"cd .. && 2>/dev/null cd nosuch || cd - && {C}  # {WAIVER}",
                "a cd landed past a redirection": (
                    f": '{WAIVER}'; 2>/dev/null cd {q(world.plain)} && {C}"
                ),
                "a second reading that unplaces": f": '{WAIVER}'; nice 2>/x/git commit -m git",
                "a cd with a redirection after its operand": f": '{WAIVER}'; cd sub 2>/dev/null && {C}",
                "nine landed cds": f": '{WAIVER}'; " + "2>/dev/null cd sub; " * 9 + C,
                "a refused segment, then sixteen cds": (
                    f": '{WAIVER}'; 2>/dev/null source /dev/null; "
                    + "cd sub; " * 16
                    + C
                ),
            }
        )
        assert stops(monkeypatch, capsys, rows, world.parity) == []

    def test_refuses_from_a_session_that_opted_into_nothing_where_a_cd_lands_in_one(
        self, monkeypatch, capsys, world
    ):
        rows = {
            "after a source": f">/dev/null source /dev/null; cd u2 && {C}",
            "after an eval": f"2>/dev/null eval true; cd u2 && {C}",
            "a name bound before": f'SB={q(world.u2)}; 2>/dev/null source /dev/null; git -C "$SB" commit -m x',
            "a redirection after the operand": f"cd u2 2>/dev/null && {C}",
            "a redirection glued to the operand": f"cd u2>/dev/null && {C}",
            "a cut redirection in front": f"2>&1 cd u2 && {C}",
            "twenty landed cds": "2>/dev/null cd sub && " * 20 + f"cd u2 && {C}",
        }
        assert stops(monkeypatch, capsys, rows, world.plain) == []

    def test_refuses_a_command_that_is_not_plain_where_git_decides(
        self, monkeypatch, capsys, world
    ):
        monkeypatch.setattr(gate.githooks, "decides", lambda root: bool(root))
        for command in (f"sh -c '{C}'", f'eval "$X"; {C}'):
            got = decision(monkeypatch, capsys, command, world.undeclared)
            assert got[0] == "deny", (command, got)

    @pytest.mark.rule("executed-text-is-read")
    def test_refuses_a_waiver_no_shell_would_type_in_front(
        self, monkeypatch, capsys, world
    ):
        """#773 and #868: a token inside a body, behind an apostrophe in its
        comment, or inside a quote that never closes waives nothing."""
        u = world.undeclared
        pr = q(world.root / "pr.md")
        rows = {
            "in a program body": f"python3 - <<'EOF'\nnote = \"{WAIVER}\"\nprint(note)\nEOF\n{commit_into(u)}",
            "in a body outside the shape": f"cat > {pr} <<EOF\n{WAIVER}\nEOF\n{commit_into(u)}",
            "in a body a shell runs": f"bash <<EOF\n: '{WAIVER}'; {commit_into(u)}\nEOF\n",
            "behind an apostrophe": f"cat > {pr} <<EOF\nbody\nEOF\n{commit_into(u)}  # don't {WAIVER}",
            "in an unclosed quote": f"cd {q(u)} && git commit -m 'x {WAIVER}",
        }
        assert stops(monkeypatch, capsys, rows, world.declared) == []
        got = decision(monkeypatch, capsys, rows["in an unclosed quote"], u)
        assert "No review is recorded" in got[1] and f": '{WAIVER}'" in got[1], got

    @pytest.mark.rule("how-a-stop-is-put")
    def test_refuses_the_first_attempt_with_a_question_and_the_next_with_an_ask(
        self, monkeypatch, capsys, world
    ):
        for command in (C, f"sh -c '{C}'"):
            session = f"s-{uuid.uuid4().hex}"
            first = decision(monkeypatch, capsys, command, world.undeclared, session)
            second = decision(monkeypatch, capsys, command, world.undeclared, session)
            assert (first[0], second[0]) == ("deny", "ask"), command
            assert (
                "AskUserQuestion" in first[1] and "Approving is the waiver" in second[1]
            )

    @pytest.mark.rule("how-a-stop-is-put")
    def test_refuses_every_attempt_with_a_deny_under_the_press(
        self, monkeypatch, capsys, world
    ):
        for command in (C, f"sh -c '{C}'"):
            session = f"pressed-{uuid.uuid4().hex}"
            for _ in range(2):
                got = decision(monkeypatch, capsys, command, world.undeclared, session)
                assert got[0] == "deny", (command, got)
                assert AUTOMATION in got[1] and "AskUserQuestion" not in got[1], got

    def test_refuses_a_parity_arm_no_mark_answers(self, monkeypatch, capsys, world):
        got = decision(monkeypatch, capsys, f": '{WAIVER}'; {C}", world.parity)
        assert got[0] == "deny" and "migration config" in got[1], got
        assert "No review is recorded" not in got[1], got


test_census = census_case(TARGET)
