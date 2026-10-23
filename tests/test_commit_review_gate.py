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
import os
import subprocess
import sys
import types
import uuid

import pytest
from conftest import (
    bash,
    branch_of,
    census_case,
    decision_of,
    declare_routing,
    fired,
    git,
    git_dir,
    git_repo,
    home,
    legacy,
    linked_worktree,
    load,
    load_hook_module,
    local_home,
    opt_in,
    payload,
    q,
    reason_of,
    run_hook,
    scratch,
    stage,
    with_row,
)

TARGET = "hooks/commit-review-gate.py"

gate = load_hook_module("commit-review-gate.py", "crg_under_test")
Unresolved = gate.Unresolved
routing = load_hook_module("routing.py", "specseal_routing_for_the_commit_gate")
gate_module = load_hook_module("gate.py", "specseal_gate_for_routing_tests")
optin = load("hooks/optin.py", "specseal_optin_failopen")

C = "git commit -m x"
WAIVER = "[no-review]"
CONSTRUCT = "contains something the gate cannot read as a plain command"
AUTOMATION = "pressed `automation` on the routing question"
CHOICE_DIR = gate.CHOICE_DIR
CHAIN = "through the review chain"
DIRECT = "straight to the PR"


def declare(
    repo,
    review=CHAIN,
    destination="open the pull request",
    branch=None,
    item="1787708604-a-work-item",
    body=None,
    implementation=None,
    planning=None,
):
    """Write a routing declaration, or arbitrary `body` when given.

    `implementation` and `planning` are both left out by default, which is
    what every declaration written before those axes existed looks like.
    """
    d = repo / "seal" / "specs" / item
    d.mkdir(parents=True, exist_ok=True)
    if body is None:
        third = f"| Implementation | {implementation} |\n" if implementation else ""
        fourth = f"| Planning | {planning} |\n" if planning else ""
        body = (
            f"# {item} -- routing\n\n"
            "| Axis | Answer |\n"
            "|---|---|\n"
            f"| Review | {review} |\n"
            f"| Destination | {destination} |\n"
            f"{fourth}"
            f"{third}"
            f"| Branch | {branch or branch_of(repo)} |\n"
        )
    path = d / "routing.md"
    path.write_text(body, encoding="utf-8")
    return path


def commit_gate(repo, cmd="git commit -m x", **kw):
    """The hook's output for CMD typed in REPO, run as the harness runs it."""
    return run_hook("commit-review-gate.py", payload(cmd, repo, **kw))


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

    # --- the hook as the harness runs it, in a repository of each case's own -

    def test_gate_silent_without_opt_in(self, repo):
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload("git commit -m x", repo))
            )
            == "silent"
        )

    def test_gate_denies_so_the_user_is_offered_both_ways_on(self, repo):
        """Declining an `ask` is a bare "No": the user who wanted the other way on
        has to retype the command. A deny gives the model the turn back."""
        opt_in(repo)
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        assert decision_of(out) == "deny"
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "AskUserQuestion" in reason
        assert "[no-review]" in reason and "review chain" in reason.lower()

    def test_the_next_attempt_gets_the_plain_prompt(self, repo):
        """Denying every time would trap a session whose answer the gate cannot
        read off the command. The fallback is the prompt this gate always had."""
        opt_in(repo)
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload("git commit -m x", repo))
            )
            == "deny"
        )
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        assert decision_of(out) == "ask"
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "Approving is the waiver" in reason

    def test_a_different_session_is_asked_the_question_too(self, repo):
        opt_in(repo)
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload("git commit -m x", repo))
            )
            == "deny"
        )
        assert (
            decision_of(
                run_hook(
                    "commit-review-gate.py",
                    payload("git commit -m x", repo, session="s2"),
                )
            )
            == "deny"
        )

    def test_an_unwritable_marker_counts_as_already_asked(self, repo):
        """A marker that cannot be recorded means the question is treated as
        asked. Inverted, the deny repeats forever in exactly the environments
        that cannot write, and the commit never lands."""
        opt_in(repo)
        # Unwritable on BOTH platforms. `os.chmod(gd, 0o500)` is a no-op for a
        # directory on Windows -- the mode bits are accepted and the write still
        # succeeds -- so the gate recorded the question, answered `silent`, and
        # the rule this case states went unheld on the one platform where an
        # unwritable git-dir is most likely.
        #
        # Occupying the marker directory's own name with a file raises `OSError`
        # everywhere: `makedirs(..., exist_ok=True)` re-raises when the name it
        # finds is not a directory.
        gd = git_dir(repo)
        with open(os.path.join(gd, CHOICE_DIR), "w", encoding="utf-8") as f:
            f.write("not a directory")
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload("git commit -m x", repo))
            )
            == "ask"
        )

    def test_a_session_id_with_separators_stays_inside_the_git_dir(self, repo):
        """The id names a file. Measured on the sibling guard: `../../escaped`
        put an empty file at the repository root."""
        opt_in(repo)
        run_hook(
            "commit-review-gate.py",
            payload("git commit -m x", repo, session="../../escaped"),
        )
        assert not (repo / "escaped").exists()
        assert os.path.isfile(
            os.path.join(git_dir(repo), "specseal-commit-choice", "escaped")
        )

    def test_without_a_session_id_it_asks_instead_of_denying(self, repo):
        """No id means nowhere to record that the question was asked, and a deny
        would then repeat forever. `ask` cannot loop: approving is the way out."""
        opt_in(repo)
        p = payload("git commit -m x", repo)
        del p["session_id"]
        assert decision_of(run_hook("commit-review-gate.py", p)) == "ask"

    def test_gate_allows_when_cycle_reviewed(self, repo):
        opt_in(repo)
        head = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        ).stdout.strip()
        with open(
            os.path.join(git_dir(repo), "specseal-reviewed"), "w", encoding="utf-8"
        ) as f:
            f.write(head)
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload("git commit -m x", repo))
            )
            == "silent"
        )

    def test_gate_ignores_non_commit_and_bypass_tag(self, repo):
        opt_in(repo)
        assert (
            decision_of(run_hook("commit-review-gate.py", payload("git log", repo)))
            == "silent"
        )
        assert (
            decision_of(
                run_hook(
                    "commit-review-gate.py",
                    payload("git commit -m x [no-review]", repo),
                )
            )
            == "silent"
        )

    def test_the_marker_inside_a_message_is_prose_not_a_waiver(self, repo):
        """`-m "drop [no-review] from the docs"` describes work; it does not waive.

        A substring test cannot tell a waiver from a sentence about one, and the
        message body is where people write sentences."""
        opt_in(repo)
        assert fired(
            run_hook(
                "commit-review-gate.py", payload('git commit -m "x [no-review]"', repo)
            )
        )

    def test_gate_ignores_echoed_git_commit(self, repo):
        opt_in(repo)
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload("echo git commit -m x", repo))
            )
            == "silent"
        )

    def test_gate_ignores_heredoc_mentions(self, repo):
        opt_in(repo)
        cmd = "cat > doc.md <<EOF\nrun: git commit -m x\nEOF"
        assert (
            decision_of(run_hook("commit-review-gate.py", payload(cmd, repo)))
            == "silent"
        )

    def test_gate_catches_separators_inside_message(self, repo):
        opt_in(repo)
        for cmd in (
            'git commit -m "fix && update deps"',
            'git commit -m "a; b"',
            'git commit -m "line1\nline2"',
        ):
            assert fired(run_hook("commit-review-gate.py", payload(cmd, repo))), cmd

    def test_gate_fails_closed_on_unparseable_commit(self, repo):
        # Unbalanced quotes defeat tokenization; if git+commit appear anyway,
        # asking beats exempting exactly the commands too gnarly to parse.
        opt_in(repo)
        assert fired(
            run_hook(
                "commit-review-gate.py", payload('git commit -m "unbalanced', repo)
            )
        )
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload('echo "unbalanced git', repo))
            )
            == "silent"
        )

    def test_gate_rearms_after_commit_moves_head(self, repo):
        opt_in(repo)
        gd = git(repo, "rev-parse", "--absolute-git-dir").stdout.strip()
        head = git(repo, "rev-parse", "HEAD").stdout.strip()
        with open(os.path.join(gd, "specseal-reviewed"), "w", encoding="utf-8") as f:
            f.write(head)
        (repo / "f.txt").write_text("more\n", encoding="utf-8")
        git(repo, "commit", "-qam", "next")  # cycle closes, mark goes stale
        assert fired(
            run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        )

    def test_gate_ignores_non_bash_tools(self, repo):
        opt_in(repo)
        p = {
            "tool_name": "Write",
            "session_id": "s",
            "tool_input": {"file_path": str(repo / "x")},
            "cwd": str(repo),
        }
        assert decision_of(run_hook("commit-review-gate.py", p)) == "silent"

    @pytest.mark.rule("review-arm-asks")
    @pytest.mark.parametrize("path", ["docs/policies/note.md", "seal/ledger.md"])
    def test_the_review_arm_asks_on_a_document_only_commit(self, repo, path):
        """The parity arm's line at `docs/` and `seal/` is the parity arm's alone.

        The review arm asks whether anybody reads the change before it lands, and
        in a repository that runs this workflow `docs/` is the policy the code
        conforms to. #518 measured it: #514's fold, which changed `docs/`,
        `seal/` and four test files, produced seven fixed findings, all located
        in `docs/`, one of them blocking, and 26 fixed findings across every
        round record sit in the ledger alone. So a commit confined to either
        root meets the review arm exactly as a code change does
        (`docs/the-review-and-parity-arms.md` *Review arm*). One path per root,
        because the line can leak by halves: an exemption for `seal/` alone
        passes every `docs/` case. This case is what fails if `touches_code`,
        or either half of it, is ever shared between the arms.
        """
        (repo / "seal").mkdir(exist_ok=True)
        (repo / path).parent.mkdir(parents=True, exist_ok=True)
        stage(repo, path, "text\n")
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        assert decision_of(out) == "deny", (
            f"a commit confined to {path} passed the review arm with no "
            "declaration, no review mark and no waiver"
        )
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "[no-review]" in reason

    def test_the_commit_gate_says_what_declining_does(self, tmp_path):
        """A hook returns allow/deny/ask; declining renders as a bare No.

        The reason string is the only place that can give the decline a
        destination, and `implement` *1. Read the spec before the code* rejects
        a question whose no leads nowhere.
        """
        from conftest import run_hook

        repo = tmp_path / "repo"
        (repo / "seal").mkdir(parents=True)
        git = lambda *a: subprocess.run(
            ["git", "-C", str(repo), *a], capture_output=True, check=True
        )
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        (repo / "f.py").write_text("x = 1\n", encoding="utf-8")
        git("add", "-A")
        git(
            "-c",
            "user.email=e@example.com",
            "-c",
            "user.name=e",
            "commit",
            "-qm",
            "base",
        )
        (repo / "f.py").write_text("x = 2\n", encoding="utf-8")
        git("add", "-A")

        out = run_hook(
            "commit-review-gate.py",
            {
                "tool_name": "Bash",
                "tool_input": {"command": "git commit -m 'change'"},
                "cwd": str(repo),
            },
        )
        d = json.loads(out)["hookSpecificOutput"]
        assert d["permissionDecision"] == "ask"
        reason = d["permissionDecisionReason"]
        assert "Approving is the waiver" in reason
        assert "Declining cancels the commit" in reason, (
            "the decline branch has no text of its own, so it reads as a dead end"
        )
        assert "[no-review]" in reason and "review chain" in reason, (
            "both continuations have to be named, or the prompt is a yes/no"
        )

    def test_the_commit_gates_hint_survives_a_root_with_no_relative_spelling(
        self, tmp_path, monkeypatch, capsys
    ):
        r"""Round 1 of #80, the blocking finding 1. The stop text names the
        declaration under the resolved root, relative to the repository, and
        `os.path.relpath` is what builds that. On Windows a linked worktree on
        another drive than the main tree makes `ntpath.relpath` raise
        (`ValueError: path is on mount 'D:', start on mount 'C:'`). The gate
        built the hint before it had judged anything, so the exception left
        `main()`, `dispatch.py`'s crash isolation swallowed it, and empty stdout
        is an allow: a commit went through in an opted-in repository, unjudged.

        The raise is induced rather than found, so the case runs on every leg.
        What is asserted is the direction: the gate still stops, and the path it
        names is the absolute one — there is no relative spelling of a path on
        another drive, and the absolute path is the one to type. `gate` here is
        a copy of the module loaded for this case alone.
        """
        gate = load("hooks/commit-review-gate.py", "specseal_gate_failopen")
        repo = git_repo(tmp_path / "repo")
        (repo / ".git" / "seal").mkdir()
        home = optin.home(str(repo))
        assert home and os.path.isabs(home), home

        def refuses(path, start=None):
            raise ValueError("path is on mount 'D:', start on mount 'C:'")

        monkeypatch.setattr(os.path, "relpath", refuses)
        monkeypatch.setattr(
            sys,
            "stdin",
            io.StringIO(
                json.dumps(
                    {
                        "tool_name": "Bash",
                        "session_id": "failopen-relpath",
                        "tool_input": {"command": "git commit -m x"},
                        "cwd": str(repo),
                    }
                )
            ),
        )
        gate.main()
        out = capsys.readouterr().out
        assert out.strip(), (
            "the gate printed nothing — an allow for a commit it never judged"
        )
        decision = json.loads(out)["hookSpecificOutput"]
        assert decision["permissionDecision"] in ("deny", "ask"), decision
        expected = os.path.join(home, "specs", "<work-item-id>", "routing.md")
        assert expected in decision["permissionDecisionReason"], decision[
            "permissionDecisionReason"
        ]

    # --- the opt-in: `seal/` read at the first of two places ------------------

    @pytest.mark.parametrize(
        "cmd",
        [
            "git commit -m x",
            "cd sub && git commit -m x",
            # The commit form Claude Code itself is instructed to use: the
            # message arrives via $(cat <<'EOF' ...) inside double quotes. A
            # quote-blind splitter shredded this and the gate stayed silent.
            "git commit -m \"$(cat <<'EOF'\nfix: thing\n\nbody\nEOF\n)\"",
            "GIT_AUTHOR_DATE=2026-01-01T00:00:00 git commit -m x",
        ],
        ids=[
            "a-plain-commit",
            "after-a-cd-chain",
            "a-heredoc-message",
            "an-env-prefix",
        ],
    )
    def test_commit_gate_fires_on_the_new_home(self, repo, cmd):
        home(repo)
        assert fired(run_hook("commit-review-gate.py", payload(cmd, repo)))

    def test_commit_gate_stays_silent_on_the_legacy_marker(self, repo):
        """S3: every gate is silent over `.specseal/`, and the only thing that
        speaks is the migration hook at session start."""
        legacy(repo)
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        assert decision_of(out) == "silent"

    def test_the_commit_gate_is_silent_in_a_scratch_repository(self, repo):
        home(repo)
        scratch(repo)
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        assert decision_of(out) == "silent"

    def test_the_commit_gate_still_fires_beside_a_scratch_DIRECTORY(self, repo):
        """The gate-level half of the file-not-directory rule."""
        home(repo)
        (repo / ".git" / "specseal-scratch").mkdir()
        assert fired(
            run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        )

    def test_a_scratch_repository_gives_no_standing_over_a_target_it_cannot_read(
        self, repo
    ):
        """The stop for an unreadable target is the session's own repository
        speaking, so the marker has to reach that too — otherwise the probe that
        prompted issue #68 keeps prompting, one door along."""
        home(repo)
        scratch(repo)
        out = run_hook(
            "commit-review-gate.py", payload('git -C "$WT" commit -m x', repo)
        )
        assert decision_of(out) == "silent"

    # --- local mode: the declaration under `<git-common-dir>/seal/` -----------

    def test_the_commit_gate_is_silent_with_a_declaration_under_the_local_root(
        self, local
    ):
        repo, home = local
        declare_routing(repo, home=home)
        assert decision_of(run_hook("commit-review-gate.py", bash(repo))) == "silent"

    def test_the_commit_gate_is_silent_from_a_linked_worktree_too(self, repo, tmp_path):
        """The declaration lives in the main tree's common directory; the
        worktree's branch is what it names."""
        home = local_home(repo)
        other = linked_worktree(repo, tmp_path)
        declare_routing(other, home=home)
        assert decision_of(run_hook("commit-review-gate.py", bash(other))) == "silent"

    def test_the_commit_gate_fires_without_one_and_names_the_resolved_path(self, local):
        """Q5 (a). The stop text used to spell `seal/specs/<work-item-id>/routing.md`
        whatever the mode, and a session that typed it in local mode wrote a
        declaration the gate never reads. The path is under the resolved root,
        relative to the repository, spelled the way the platform spells it."""
        repo, _ = local
        out = run_hook("commit-review-gate.py", bash(repo))
        assert fired(out)
        reason = reason_of(out)
        resolved = os.path.join(".git", "seal", "specs", "<work-item-id>", "routing.md")
        assert resolved in reason, reason
        assert "`seal/specs/<work-item-id>/routing.md`" not in reason, (
            "the literal shared-mode spelling is still offered in local mode"
        )

    def test_the_stop_text_from_a_linked_worktree_is_a_path_a_person_can_type(
        self, repo, tmp_path
    ):
        """From a linked worktree the resolved root is outside the tree, so the
        relative path climbs out of it — typeable, where `.git/seal/…` names a
        FILE's child there."""
        home = local_home(repo)
        other = linked_worktree(repo, tmp_path)
        out = run_hook("commit-review-gate.py", bash(other))
        assert fired(out)
        resolved = os.path.join(
            os.path.relpath(home, other), "specs", "<work-item-id>", "routing.md"
        )
        assert resolved in reason_of(out), reason_of(out)

    def test_in_shared_mode_the_stop_text_still_names_the_tree_root(self, repo):
        """The other half of Q5: a shared repository is told `seal/specs/…`,
        the path it always was."""
        (repo / "seal").mkdir()
        out = run_hook("commit-review-gate.py", bash(repo))
        assert fired(out)
        resolved = os.path.join("seal", "specs", "<work-item-id>", "routing.md")
        assert resolved in reason_of(out), reason_of(out)

    # --- the routing declaration is read, both ways ---------------------------

    @pytest.mark.rule("routing-read-first")
    @pytest.mark.parametrize("review", [CHAIN, DIRECT], ids=["chain", "direct"])
    def test_a_declared_item_commits_without_a_prompt(self, repo, review):
        """S1 and S4. The whole point: the answer was given, so it is not
        asked again; and declaring is the routing answer, so requiring
        `[no-review]` as well would be requiring the same answer twice."""
        opt_in(repo)
        declare(repo, review=review)
        assert decision_of(commit_gate(repo)) == "silent"

    def test_no_declaration_behaves_exactly_as_before(self, repo):
        """S2. The gate a repository that declares nothing meets is unchanged."""
        opt_in(repo)
        assert decision_of(commit_gate(repo)) == "deny"
        assert decision_of(commit_gate(repo)) == "ask"

    def test_a_malformed_declaration_does_not_silence_the_gate(self, repo):
        """S3. Toward asking, never toward silence -- a gate a corrupt file turns
        off has nothing left to do but stay quiet."""
        opt_in(repo)
        declare(repo, body="# routing\n\nwe decided to go through the review chain.\n")
        assert fired(commit_gate(repo))

    def test_an_unknown_answer_is_not_an_answer(self, repo):
        """The vocabulary is fixed. `maybe` is not one of the two ways on."""
        opt_in(repo)
        declare(repo, review="maybe later")
        assert fired(commit_gate(repo))

    def test_an_empty_routing_directory_changes_nothing(self, repo):
        opt_in(repo)
        (repo / "seal" / "routing").mkdir(parents=True)
        assert fired(commit_gate(repo))

    def test_another_branch_s_declaration_does_not_apply_here(self, repo):
        """Declarations accumulate over a repository's life. Without a scope, the
        first work item ever declared would silence the gate forever."""
        opt_in(repo)
        declare(repo, review=CHAIN, branch="feature/somewhere-else")
        assert fired(commit_gate(repo))

    def test_two_declarations_for_one_branch_are_ambiguous(self, repo):
        """Two answers for the same branch is not an answer. Toward asking."""
        opt_in(repo)
        declare(repo, review=CHAIN, item="1787708604-one")
        declare(repo, review=DIRECT, item="1787708605-two")
        assert fired(commit_gate(repo))

    def test_a_declaration_for_another_branch_leaves_this_one_readable(self, repo):
        """One stale declaration must not make a live one ambiguous."""
        opt_in(repo)
        declare(repo, review=CHAIN, item="1787708604-here")
        declare(repo, review=CHAIN, item="1787700000-elsewhere", branch="feature/old")
        assert decision_of(commit_gate(repo)) == "silent"

    def test_an_uncommitted_declaration_silences_the_commit_that_adds_it(self, repo):
        """The fact the gate's first option rests on, asserted directly.

        `declarations()` opens the path rather than asking git, so a declaration
        that exists only in the working tree is already in force. That is what
        makes "write the declaration first" a real way out of a work item's FIRST
        commit: there is no order in which the file must be committed before it
        counts, and so no first-commit waiver to spend. The tests above rely on
        this without saying so -- none of them commits the file -- and an
        unstated premise is one a later change moves silently.
        """
        opt_in(repo)
        path = declare(repo)
        tracked = subprocess.run(
            ["git", "-C", str(repo), "ls-files", "--error-unmatch", str(path)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert tracked.returncode != 0, "the premise is an UNCOMMITTED declaration"
        assert decision_of(commit_gate(repo)) == "silent"

    def test_the_first_prompt_names_the_declaration_as_a_way_out(self, repo):
        """Three ways out, and the prompt named two.

        A session starting a work item was handed "review it first" and "commit
        without a review" -- the two answers that do not fit -- and none of the
        one that does. Measured: a session read the missing option as a
        chicken-and-egg the design does not have and put it to the user twice.
        """
        opt_in(repo)
        out = commit_gate(repo)
        assert decision_of(out) == "deny"
        reason = reason_of(out)
        assert '1. "Declare the routing"' in reason
        # The way the platform spells it: the path is joined under the resolved
        # root (#80, Q5), so on Windows it arrives with backslashes.
        assert os.path.join("seal", "specs", "<work-item-id>", "routing.md") in reason
        assert "IN A COMMAND OF ITS OWN" in reason, (
            "the option stopped saying the one thing that makes it work"
        )

    def test_the_first_option_does_not_let_the_model_pick_the_review_answer(self, repo):
        """`straight to the PR` written by the model is a waiver with no word in it.

        The option tells the model to write the declaration and said nothing about
        which Review answer to write. `straight to the PR` silences this arm for
        every later commit on the branch, and at the pull request `chain_check.py`
        requires the broad run's `broad-gate.md` of it and no reviewer's record -- so
        a model filling that row in for itself takes the waiver the option below
        spells out, and takes it more quietly: the
        `[no-review]` form leaves the word in the command where a reader can point
        at it, and this leaves nothing anywhere but one line of a file it was just
        told to write.
        """
        opt_in(repo)
        reason = reason_of(commit_gate(repo))
        assert "USER'S answer" in reason, (
            "the option stopped saying who decides the Review row"
        )
        for spelling in ("through the review chain", "straight to the PR"):
            assert spelling in reason, f"the option names only one answer: {spelling}"

    def test_the_first_option_says_what_the_direct_answer_owes(self, repo):
        """A8 of #241, for the one carrier a whole-file substring cannot read.

        The option said `straight to the PR` is the one CI requires nothing for,
        which has been false since `chain_check.py#direct_seal` required the
        broad run's `broad-gate.md` at a ready pull request. A model reading the
        option as written would tell the user the direct answer is unchecked.
        """
        opt_in(repo)
        reason = reason_of(commit_gate(repo))
        assert "requires nothing" not in reason, (
            "the option still says the direct answer requires nothing"
        )
        assert "broad-gate.md" in reason, (
            "the option does not say what the direct answer owes at the pull request"
        )
        assert "USER'S answer" in reason and "straight to the PR" in reason

    def test_the_first_prompt_counts_the_options_it_lists(self, repo):
        """The header tells the model to offer EXACTLY that many.

        Written down rather than derived, the number goes stale the moment an
        option is added -- and the model obeys the number, so the third option is
        the one it drops.
        """
        opt_in(repo)
        reason = reason_of(commit_gate(repo))
        assert "exactly these three options:" in reason
        assert "these two options" not in reason
        for label in (
            '1. "Declare the routing"',
            '2. "Review it first"',
            '3. "Commit without a review"',
        ):
            assert label in reason, f"the prompt lost `{label}`"

    def test_the_second_prompt_names_it_too(self, repo):
        """The `ask` prompt is what every attempt after the first reaches.

        Leaving it at two ways sent a session that had just read the third option
        back to a sentence saying there were only two.
        """
        opt_in(repo)
        assert decision_of(commit_gate(repo)) == "deny"
        out = commit_gate(repo)
        assert decision_of(out) == "ask"
        reason = reason_of(out)
        # The same platform spelling as the first prompt's assertion above: the
        # windows leg of PR #95 (run 33643327406) failed on the `/` literal here
        # after phase 1 had fixed only the first one.
        assert os.path.join("seal", "specs", "<work-item-id>", "routing.md") in reason
        assert "for any commit" in reason, (
            "the two-way sentence must scope itself once a third way follows it"
        )

    def test_the_third_way_names_its_arm_where_two_are_listed(self, repo):
        """`this arm` points at nothing in a prompt that lists two of them.

        With review and parity both firing, `ask_reason` prints the two states
        together and then the review arm's sentence. Written as "it silences this
        arm ... re-issue the commit unchanged" it made a promise the gate does not
        keep: executed, writing the declaration and re-issuing gets the parity arm
        and one more prompt. The sentence has to name the arm it belongs to and
        say what it does NOT do.
        """
        opt_in(repo)
        (repo / "seal" / "parity.md").write_text(
            "# migration config\n", encoding="utf-8"
        )
        (repo / "code.py").write_text("x = 1\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
        )
        assert decision_of(commit_gate(repo)) == "deny"
        reason = reason_of(commit_gate(repo))
        assert "[no-review]" in reason and "[no-parity]" in reason, (
            "this case is only about the prompt where BOTH arms are listed"
        )
        assert "REVIEW arm" in reason, (
            "the third way does not say which of the two arms it is a way out of"
        )
        assert "`straight to the PR`, it silences NOTHING ELSE" in reason, (
            "the sentence still reads as though the commit then goes through"
        )
        # #988: the chain answer quiets the parity arm too, and the sentence
        # that says what the declaration silences says so.
        assert "`through the review chain`, it silences the parity arm too" in reason
        # Case-insensitive: the first version of this check read the lower-case
        # spelling only, and a mutation that opened the sentence with `Re-issue`
        # walked straight through it.
        assert "re-issue the commit unchanged" not in reason.lower(), (
            "`unchanged` promises a commit the other arm still stops"
        )

    def test_the_parity_arm_gains_no_third_way(self, repo):
        """Nothing declares a comparison against the original in advance.

        The routing sentence rides on the review arm, so an arm that has no such
        way out must not inherit one -- offering it there would name a file that
        silences nothing. Under `straight to the PR` the parity arm still stands
        at the commit (#988, `questions.md` Q1), which is where its prompt is
        read.
        """
        opt_in(repo)
        (repo / "seal" / "parity.md").write_text(
            "# migration config\n", encoding="utf-8"
        )
        declare(repo, review=DIRECT)
        (repo / "code.py").write_text("x = 1\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
        )
        assert decision_of(commit_gate(repo)) == "deny"
        reason = reason_of(commit_gate(repo))
        assert "[no-parity]" in reason
        # The PROPERTY, not a filename. `"routing.md" not in reason` said the same
        # thing today and would go red on a parity prompt that got MORE accurate --
        # one that says in so many words that a declaration does not silence this
        # arm. What must not happen is the review arm's sentence riding along.
        assert "There is a third way" not in reason, (
            "the parity arm inherited the review arm's `also` sentence"
        )

    def test_a_direct_declaration_does_not_waive_the_parity_arm(self, repo):
        """S2 of #988. Under `straight to the PR` no review round exists to
        record a comparison against the original, so the declaration quiets the
        review arm alone and a code commit still meets the parity arm."""
        opt_in(repo)
        (repo / "seal" / "parity.md").write_text(
            "# migration config\n", encoding="utf-8"
        )
        declare(repo, review=DIRECT)
        (repo / "code.py").write_text("x = 1\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
        )
        out = commit_gate(repo)
        assert fired(out)
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "[no-parity]" in reason
        assert "[no-review]" not in reason

    @pytest.mark.rule("parity-quiet-under-the-chain")
    def test_a_chain_declaration_quiets_the_parity_arm(self, repo):
        """S1 of #988, through `gate.arms_missing` and the PreToolUse reading.
        In a review chain the warden compares the change with the original after
        the smith has committed it, and each round record carries that
        comparison to the pull request. So a code commit on a branch declaring
        the review chain meets neither arm, while the same commit with no
        declaration meets the parity arm."""
        opt_in(repo)
        (repo / "seal" / "parity.md").write_text(
            "# migration config\n", encoding="utf-8"
        )
        (repo / "code.py").write_text("x = 1\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
        )

        def missing():
            return gate_module.arms_missing(
                str(repo), str(repo), {gate_module.REVIEW}, lambda: ["code.py"]
            )

        assert missing() == [gate_module.PARITY]
        declare(repo, review=CHAIN)
        assert missing() == []
        assert decision_of(commit_gate(repo)) == "silent"
        assert decision_of(commit_gate(repo)) == "silent"

    def test_no_review_still_waives_one_command_on_its_own(self, repo):
        """S5. The token keeps its meaning for a commit with no work item."""
        opt_in(repo)
        assert (
            decision_of(commit_gate(repo, cmd="git commit -m x [no-review]"))
            == "silent"
        )

    def test_declaring_creates_the_root_and_the_root_is_the_opt_in(self, repo):
        """Since 0.4.0 the whole work item lives under `seal/`, so writing the
        first declaration creates the root, and the root's presence IS the
        opt-in (`docs/one-root-by-lifetime.md`, "The opt-in signal is the root
        itself"). Two cases used to pin the opposite -- that a declaration under
        `specs/` created no `.specseal/` -- because answering where a work item
        was going must not switch four gates on in a repository that never asked.
        That hazard is answered differently now: the once-per-repo moment of the
        `implement` skill creates `seal/` on purpose and says so, and a session
        that writes a declaration is one that has been through it. What this
        case pins is the consequence, so a reader finds it stated rather than
        inferred: a declared repository is an opted-in repository, and the
        declaration it just wrote silences the review arm for the branch it
        names."""
        assert not (repo / "seal").exists()
        declare(repo, review=CHAIN)
        assert (repo / "seal").is_dir(), "the declaration lives under the root"
        assert decision_of(commit_gate(repo)) == "silent"  # opted in, and declared

    def test_a_declaration_for_another_branch_leaves_the_gate_asking(self, repo):
        """The root exists once anything is declared, so the gate is on; but a
        declaration naming some OTHER branch is not this commit's answer."""
        declare(repo, review=CHAIN, branch="somebody-elses-branch")
        assert (repo / "seal").is_dir()
        assert fired(commit_gate(repo))

    def test_a_routing_only_work_item_is_a_whole_work_item(self, repo):
        """Below the SDD ladder nothing is written -- no `spec.md`, no closing
        memo -- so those changes used to leave no trace at all. They are most of
        what the gate sees, which is why they get an id and a directory."""
        opt_in(repo)
        path = declare(repo, review=DIRECT, item="1787700000-a-typo-fix")
        assert sorted(os.listdir(path.parent)) == ["routing.md"]
        assert decision_of(commit_gate(repo)) == "silent"

    def test_the_commit_gate_decides_the_same_with_the_row_and_without_it(self, repo):
        """S1 + S3 at the gate rather than at the parser. Adding the axis must not
        move the decision the two older axes produce."""
        opt_in(repo)
        declare(repo, review=CHAIN)
        assert decision_of(commit_gate(repo)) == "silent"
        declare(repo, review=CHAIN, implementation="smith")
        assert decision_of(commit_gate(repo)) == "silent"
        declare(repo, review=CHAIN, implementation="whoever gets to it")
        assert decision_of(commit_gate(repo)) == "silent"

    def test_the_commit_gate_decides_the_same_with_the_planning_row_and_without(
        self, repo
    ):
        """S9 at the gate rather than at the parser, the shape the third axis's own
        case has. A backticked, capitalised or absent answer decides exactly what
        the declaration without the row decides."""
        opt_in(repo)
        declare(repo, review=CHAIN)
        assert decision_of(commit_gate(repo)) == "silent"
        for answer in ("framer", "the session", "`framer`", "Framer", "whoever"):
            declare(repo, review=CHAIN, planning=answer)
            assert decision_of(commit_gate(repo)) == "silent", answer

    def test_the_commit_gate_decides_identically_with_the_row_and_without(self, repo):
        """S11 of the implementer axis, the load-bearing half: notice, never
        denial. Byte-identical, because the reason text is what a session acts
        on."""
        opt_in(repo)
        declare(repo, implementation=None)
        without = run_hook("commit-review-gate.py", bash(repo))
        declare(repo, implementation="smith")
        with_row = run_hook("commit-review-gate.py", bash(repo, session="s2"))
        assert without == with_row == "", (without, with_row)

    def test_a_review_label_written_twice_makes_the_gate_ask(self, repo):
        """S5 at the gate: a doubled strict label is no declaration, so the
        commit gate asks as it does for any `routing.md` that will not parse.
        Seen red against the last-wins parser: silent."""
        opt_in(repo)
        path = declare(repo, review=CHAIN)
        body = path.read_text(encoding="utf-8")
        path.write_text(
            body.replace(f"| Review | {CHAIN} |\n", f"| Review | {CHAIN} |\n" * 2),
            encoding="utf-8",
        )
        assert fired(commit_gate(repo))

    def test_the_commit_gate_decides_the_same_with_the_new_rows_and_without(self, repo):
        """S9's shape at the gate for both new rows.

        These two rows are the furthest from the gate of any in the file — nothing
        reads them at a commit at all — so the property to pin is that adding them
        moves no decision the four older rows produce.
        """
        opt_in(repo)
        declare(repo, review=CHAIN)
        assert decision_of(commit_gate(repo)) == "silent"
        for label, answers in (
            (routing.AUTOMATION, ("yes", "no", "`yes`", "unattended", "")),
            (routing.ANSWER_PRESSED, ("automation", "per axis", "Automation", "")),
        ):
            for answer in answers:
                declare(
                    repo,
                    review=CHAIN,
                    body=with_row(label, answer).replace(
                        "| Branch | feature/x |", f"| Branch | {branch_of(repo)} |"
                    ),
                )
                assert decision_of(commit_gate(repo)) == "silent", f"{label} = {answer}"


class Test_touches_code:
    def test_accepts_a_code_change_alongside_the_home_directory(self, repo):
        gate = load_hook_module("commit-review-gate.py", "commit_review_gate")
        (repo / "seal").mkdir()
        (repo / "seal" / "ledger.md").write_text("# ledger\n", encoding="utf-8")
        (repo / "app.py").write_text("x = 1\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
        )
        assert gate.touches_code(
            str(repo), gate.commit_invocations("git commit -m x")[0]
        )

    def test_refuses_the_home_directory_as_code(self, repo):
        """The parity gate compares code against an original; `seal/` is neither.

        Asking there would train people to click through the prompt, which costs
        more than the check is worth."""
        gate = load_hook_module("commit-review-gate.py", "commit_review_gate")
        (repo / "seal").mkdir()
        (repo / "seal" / "ledger.md").write_text("# ledger\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
        )
        assert not gate.touches_code(
            str(repo), gate.commit_invocations("git commit -m x")[0]
        )


class Test_module:
    def test_a_mark_that_is_not_utf8_reads_as_text_rather_than_raising(self, tmp_path):
        """#741's D7, at the one hook read whose handler catches `OSError` alone.

        On a cp1252 machine the unnamed read never raised, because cp1252 decodes
        almost any byte; strict UTF-8 raises `UnicodeDecodeError`. Inside a hook
        that raise reaches `dispatch.py`'s `except Exception`, which is an allow,
        so naming the encoding must not be what turns a stray byte into a pass."""
        crg = load_hook_module("commit-review-gate.py", "crg_for_the_encoding_case")
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "specseal-reviewed").write_bytes(b"\xffabc\n")
        got = crg.read_mark(str(tmp_path), ".git", "specseal-reviewed")
        assert got == "\N{REPLACEMENT CHARACTER}abc", repr(got)


test_census = census_case(TARGET)
