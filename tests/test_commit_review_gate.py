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

How `hooks/cmdline.py` reads each shell shape is `tests/test_cmdline.py`'s,
reading cases with no git; until #942's phase 6 places the rest there,
`tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` and
`tests/test_no_shape_the_base_stops_reads_silent.py` keep theirs.

#942's phase 6 placed here the gate's cases of
`tests/test_gate_judges_the_repo_it_commits_to.py`,
`tests/test_an_automation_run_meets_no_commit_prompt.py`,
`tests/test_a_commit_behind_a_reserved_word_is_judged.py`,
`tests/test_the_waiver_can_be_typed.py` and the parity arm's of
`tests/test_chain_hooks_hardening.py`. Most run the hook as the harness runs
it, in a repository copied per case from a template built once
(`make_repo`, `opted_in_repo`) or in the `repo` fixture. The cases of
`Test_automation_pressed` that build a transcript under `projects` read the
press with the reader itself, so that class lifts the stub for them.
"""

import atexit
import io
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import types
import uuid
from pathlib import Path

import pytest
from conftest import (
    ATE_THE_PROBE,
    NOT_A_SHELL,
    a_git_whose_diff_fails,
    ask_entries,
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
    parity_only,
    parity_repo,
    payload,
    q,
    reason_of,
    run_hook,
    scratch,
    sh,
    shell_probe,
    stage,
    staged_repo,
    with_row,
    write_transcript,
)
from conftest import run_gate as run
from test_a_commit_behind_a_reserved_word_is_judged import HERE, SHAPES

TARGET = "hooks/commit-review-gate.py"

gate = load_hook_module("commit-review-gate.py", "crg_under_test")
Unresolved = gate.Unresolved
# The press reader the gate imported by its plain name, so the cases that
# patch it reach the copy `gate.main` reads.
worktree_consent = gate.worktree_consent
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


def unreadable(wheres):
    return [isinstance(w, Unresolved) for w in wheres]


# --- the hook run as a process, in a repository copied per case -------------

_GATE_REPO_TEMPLATE = None


def _gate_repo_template():
    """A repo with one commit and a staged change, built once per process --
    `make_repo` is called 57 times in this file, always onto this shape."""
    global _GATE_REPO_TEMPLATE
    if _GATE_REPO_TEMPLATE is None:
        d = Path(tempfile.mkdtemp(prefix="specseal-gate-repo-template-")) / "repo"
        subprocess.run(["git", "init", "-q", str(d)], check=True)

        def git(*a):
            subprocess.run(["git", "-C", str(d), *a], capture_output=True, check=True)

        (d / "f.py").write_text("x = 1\n", encoding="utf-8")
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
        (d / "f.py").write_text("x = 2\n", encoding="utf-8")
        git("add", "-A")
        atexit.register(shutil.rmtree, d, True)
        _GATE_REPO_TEMPLATE = d
    return _GATE_REPO_TEMPLATE


MODE_ROW = "# Repository config\n\n| Item | Value |\n|---|---|\n| Mode | {mode} |\n"


def make_repo(path, opted_in, local=False):
    """A repo with one commit, `seal/` when it opts in, and a staged change.

    `local=True` puts the root under the git directory instead (#80).

    The mode is RECORDED, because `hooks/mode-gate.py` joined the `pre-bash`
    group (#151) and an unrecorded one is a state it has to name. These cases
    measure the commit gate, and every one of them reads a merged decision or
    a merged reason -- so a second voice in the group would make some of them
    pass for a reason they do not state, and one of them (the broken-reader
    case, which asserts the group falls SILENT) fail outright.
    """
    shutil.copytree(_gate_repo_template(), path)
    if opted_in and local:
        home = local_home(path)
    elif opted_in:
        home = path / "seal"
        home.mkdir()
    else:
        return path
    (home / "config.md").write_text(
        MODE_ROW.format(mode="local" if local else "shared"), encoding="utf-8"
    )
    return path


def released_hooks(dest):
    """The last release's `hooks/` written into `dest`, and the tag it came from.

    A tag, not a SHA. The reason first given for leaving this unpinned — that
    a hard-coded commit stops resolving once the branch is squashed — is true
    of a SHA and false of a tag, and `git describe --tags --abbrev=0` keeps
    naming "the release this is measured against" after the next release too.
    Read file by file rather than through `tar`, so nothing depends on an
    archive format or on `tarfile`'s extraction filter.
    """
    root = Path(__file__).resolve().parent.parent
    tag = subprocess.run(
        ["git", "-C", str(root), "describe", "--tags", "--abbrev=0", "HEAD"],
        capture_output=True,
        encoding="utf-8",
    ).stdout.strip()
    assert tag, (
        "no tag is reachable from HEAD, so the released gate cannot be built. "
        "A clone without tags cannot answer this and must not read as a pass "
        "— fetch them (`git fetch --tags`, or `fetch-depth: 0` in CI)"
    )
    listing = subprocess.run(
        ["git", "-C", str(root), "ls-tree", "--name-only", tag, "hooks/"],
        capture_output=True,
        encoding="utf-8",
        check=True,
    ).stdout.split()
    dest.mkdir(parents=True, exist_ok=True)
    for rel in listing:
        if not rel.endswith((".py", ".json")):
            continue
        blob = subprocess.run(
            ["git", "-C", str(root), "show", f"{tag}:{rel}"],
            capture_output=True,
            check=True,
        ).stdout
        (dest / Path(rel).name).write_bytes(blob)
    return tag


# --- the waiver's advised form, run in every shell on PATH -------------------

NAMED_SHELLS = ("sh", "bash", "zsh")
SHELL_PROBE = {s: shell_probe(s) for s in NAMED_SHELLS if shutil.which(s)}
SHELLS = [s for s, why in SHELL_PROBE.items() if why is None]
# Split by WHY the name dropped out, because the two need opposite treatment.
#
# A name that is not a shell at all has to be droppable: `windows-latest`
# resolves `bash` to the WSL launcher, and the probe exists to remove exactly
# that. Failing on it would fail the runner for doing what it was asked.
#
# A working shell that answered wrong is the silent shrink instead -- one
# `echo` in a developer's `.zshenv` and the waiver's cases stop running in
# `zsh` while still reporting a pass. `assert SHELLS` sees an empty list and
# not a shrunken one, so that case is asserted on separately below.
UNUSABLE_SHELLS = {
    s: w for s, w in SHELL_PROBE.items() if w and w.endswith(NOT_A_SHELL)
}
POLLUTED_SHELLS = {
    s: w for s, w in SHELL_PROBE.items() if w and w.endswith(ATE_THE_PROBE)
}


_WAIVER_REPO_TEMPLATE = None


def _waiver_repo_template():
    """A repo with one commit and a staged change, built once per process."""
    global _WAIVER_REPO_TEMPLATE
    if _WAIVER_REPO_TEMPLATE is None:
        d = Path(tempfile.mkdtemp(prefix="specseal-waiver-repo-template-")) / "repo"
        subprocess.run(["git", "init", "-q", str(d)], check=True)

        def g(*a):
            subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)

        (d / "f.py").write_text("x = 1\n", encoding="utf-8")
        g("add", "-A")
        g(
            "-c",
            "user.email=e@example.com",
            "-c",
            "user.name=e",
            "commit",
            "-qm",
            "base",
        )
        (d / "f.py").write_text("x = 2\n", encoding="utf-8")
        g("add", "-A")
        atexit.register(shutil.rmtree, d, True)
        _WAIVER_REPO_TEMPLATE = d
    return _WAIVER_REPO_TEMPLATE


def opted_in_repo(tmp_path):
    """A repo the gate fires in, with a staged change ready to commit."""
    d = tmp_path / "repo"
    shutil.copytree(_waiver_repo_template(), d)
    (d / "seal").mkdir()
    return d


# --- the press read off a transcript, for `Test_automation_pressed` ----------
#
# "Under the press" means a transcript built by conftest's `projects` fixture
# and `write_transcript`, under a projects root the case owns. No case reads a
# real transcript.

PRESSED = "pressed"
PLAIN = "plain"
ASK_TOOL = "AskUserQuestion"


def press(projects, cwd, session=PRESSED, **entries):
    write_transcript(projects, session, ask_entries(cwd, **entries))


def say(monkeypatch, capsys, command, cwd, session=PRESSED, transcript=None):
    """(decision, reason) for one issue of `command`; ("silent", "") for none."""
    payload = {"tool_name": "Bash", "tool_input": {"command": command}, "cwd": str(cwd)}
    if session is not None:
        payload["session_id"] = session
    if transcript is not None:
        payload["transcript_path"] = str(transcript)
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps(payload)))
    gate.main()
    printed = capsys.readouterr().out.strip()
    if not printed:
        return "silent", ""
    out = json.loads(printed)["hookSpecificOutput"]
    return out["permissionDecision"], out["permissionDecisionReason"]


def spend_the_budget(repo, session=PRESSED):
    """Write the marker the gate writes at a session's first stop."""
    d = repo / ".git" / "specseal-commit-choice"
    d.mkdir(parents=True, exist_ok=True)
    (d / session).write_text("", encoding="utf-8")


def forget_the_budget(repo):
    shutil.rmtree(repo / ".git" / "specseal-commit-choice", ignore_errors=True)


UNREADABLE_BODY = "bash <<'EOF'\ngit commit -m x\nEOF"
# The orchestrator's loop in all three milestone runs on disk, which spent the
# main checkout's deny for the whole run. Its `git` follows a `;`: the base
# reads no commit at all in `do git commit` written on one line, a reading
# this work item does not change (`phases/phase-1.md`).
UNREADABLE_LOOP = (
    'for w in a:1 b:2; do IFS=: read d n <<< "$w"; git -C $d commit -m x; done'
)


def measured(w):
    return {
        "a heredoc edit, then a commit on the next line": (
            f"cd {q(w)} && python3 - <<'EOF'\nprint(1)\nEOF\n"
            "git add f && git commit -m x"
        ),
        "a ; after the cd, no heredoc": (
            f"cd {q(w)} && true ; git add f && git commit -m x"
        ),
        "a body line equal to the delimiter ends it early": (
            "cat > note.md <<'EOF'\nquoted:\nEOF\ngit commit -m x\nEOF"
        ),
    }


def reasons_under_the_press(monkeypatch, capsys, projects, tmp_path):
    repo = staged_repo(tmp_path / "repo")
    press(projects, repo)
    return {
        "resolved": say(monkeypatch, capsys, "git commit -m x", repo)[1],
        "unreadable": say(monkeypatch, capsys, UNREADABLE_BODY, repo)[1],
    }


def sequence(monkeypatch, capsys, repo, session, transcript=None):
    """Two resolved stops and two unreadable ones, from a fresh budget."""
    forget_the_budget(repo)
    out = []
    for command in ("git commit -m x", "git commit -m x"):
        out.append(say(monkeypatch, capsys, command, repo, session, transcript))
    forget_the_budget(repo)
    for command in (UNREADABLE_BODY, UNREADABLE_BODY):
        out.append(say(monkeypatch, capsys, command, repo, session, transcript))
    forget_the_budget(repo)
    return out


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

    def test_the_invocation_reports_the_chdir_it_used_to_only_skip(self):
        found, clean = gate.commit_invocations("git -C /srv/app commit -m x")
        assert clean and len(found) == 1
        assert found[0].args == ["-m", "x"]
        assert found[0].chdirs == ["/srv/app"], (
            "the value that decides WHICH repository the commit lands in was dropped"
        )

    def test_a_plain_commit_carries_no_chdir(self):
        found, _ = gate.commit_invocations("git commit -m x")
        assert found[0].chdirs == []

    def test_a_heredoc_that_never_terminates_swallows_the_rest(self, tmp_path):
        """An unterminated body runs to the end of the input -- `git commit -m x`
        on the last line is swallowed WITH it, not read as a live segment of its
        own the way a naive drop that missed the unterminated case would.

        It still surfaces as a hidden commit needing review (issue #75), the same
        accepted cost as `cat > run.sh <<'EOF' … git commit … EOF`: nothing here
        can tell "cat, so this is data" from "bash, so this runs" without the
        interpreter enumeration issue #75 rejects, so a swallowed body that reads
        as a commit stops whether or not its heredoc ever terminated.
        """
        command = f"cat <<'EOF'\ncd {sh(tmp_path / 'b')}\ngit commit -m x"
        found, _clean = gate.commit_invocations(command, str(tmp_path))
        assert len(found) == 1
        # `gate.Unresolved`, not `reader.Unresolved`: `commit_invocations` wraps
        # the base using the `cmdline` module IT imported, a separate load from
        # this file's own `reader`, so the two classes fail `isinstance` against
        # each other despite naming the same type.
        assert isinstance(found[0].base, gate.Unresolved)
        assert found[0].base.why == gate.Unresolved.CONSTRUCT

    def test_a_heredoc_body_does_not_hide_a_commit_that_follows_it(self, tmp_path):
        """The other direction, so the drop cannot quietly grow: what comes AFTER
        the terminator is a command again."""
        command = "cat > run.sh <<'EOF'\nhello\nEOF\ngit commit -m x"
        found, _clean = gate.commit_invocations(command, str(tmp_path))
        assert len(found) == 1

    def test_the_quoted_heredoc_commit_form_still_parses(self, tmp_path):
        """The form Claude Code itself writes: the body sits inside `"$(…)"`, so
        the opener is quoted and no body is dropped."""
        command = "git commit -m \"$(cat <<'EOF'\nsubject\n\nbody\nEOF\n)\""
        found, clean = gate.commit_invocations(command, str(tmp_path))
        assert clean and len(found) == 1, (found, clean)


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
    """The press as `main` reads it. A case that builds a transcript under
    `projects` reads it with `hooks/worktree_consent.py`'s own reader, through
    the whole of `main`; the others answer from the session id, as the file's
    autouse fixture does."""

    @pytest.fixture(autouse=True)
    def _the_press_is_read_off_the_session_id(self, request, monkeypatch):
        if "projects" not in request.fixturenames:
            monkeypatch.setattr(gate, "worktree_consent", _Press())

    def test_accepts_a_press_the_reader_answers_true(self):
        assert gate.automation_pressed("/x/top", "pressed-1", "") is True

    # --- S1 and S2: a stop in a repository the gate read ----------------------

    def test_a_resolved_stop_after_the_budget_is_spent_is_refused(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S1. The base answers `ask` here, which is a person's prompt."""
        repo = staged_repo(tmp_path / "repo")
        press(projects, repo)
        spend_the_budget(repo)
        decision, reason = say(monkeypatch, capsys, "git commit -m x", repo)
        assert decision == "deny", reason
        assert "pressed `automation`" in reason

    def test_a_parity_stop_under_the_press_is_refused_too(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S1, the other arm. The review arm is waived so the parity arm alone
        stands; a parity prompt in an automation run breaks the same promise."""
        repo = staged_repo(tmp_path / "repo")
        (repo / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
        press(projects, repo)
        command = ": '[no-review]'; git commit -m x"
        for _ in range(2):
            decision, reason = say(monkeypatch, capsys, command, repo)
            assert decision == "deny", reason
            assert "[no-parity]" in reason, "the waiver offered is not the arm's"
            assert "'[no-review]'" not in reason.split("pressed `automation`")[1]

    @pytest.mark.rule("parity-quiet-under-the-chain")
    def test_a_chain_declared_code_commit_meets_no_parity_stop_under_the_press(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S1 of #988, under the press. A branch declaring the review chain in a
        migration repository commits its code with no parity mark at HEAD, so
        the smith's first code commit no longer ends an `automation` run."""
        repo = staged_repo(
            tmp_path / "repo", declared=True, review="through the review chain"
        )
        (repo / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
        press(projects, repo)
        for _ in range(2):
            assert say(monkeypatch, capsys, "git commit -m x", repo) == ("silent", "")

    def test_a_resolved_stop_the_first_time_puts_no_question(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S2. The base's first stop instructs the model to put the choice up
        with the question tool, which a subagent has none of and which an
        automation run's main session must not use."""
        repo = staged_repo(tmp_path / "repo")
        press(projects, repo)
        decision, reason = say(monkeypatch, capsys, "git commit -m x", repo)
        assert decision == "deny"
        assert ASK_TOOL not in reason

    def test_the_press_is_read_against_the_sessions_own_repository(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """The press was given in the clone the session sits in, and a commit
        aimed at another repository is still this session's commit. Read against
        the target, it would be found nowhere, and the second stop would be a
        person's prompt again. Seen red by reading it against the target."""
        session = staged_repo(tmp_path / "session")
        elsewhere = staged_repo(tmp_path / "elsewhere")
        press(projects, session)
        command = f"git -C {q(elsewhere)} commit -m x"
        got = [say(monkeypatch, capsys, command, session)[0] for _ in "12"]
        assert got == ["deny", "deny"]

    # --- S3: a stop where the gate could not read the repository ---------------

    @pytest.mark.parametrize("command", [UNREADABLE_BODY, UNREADABLE_LOOP])
    def test_an_unreadable_stop_is_refused_every_time(
        self, monkeypatch, capsys, projects, tmp_path, command
    ):
        """S3. A body a shell runs, and a commit inside a loop over a variable.
        The base denies the first and asks the second."""
        repo = staged_repo(tmp_path / "repo")
        press(projects, repo)
        for attempt in (1, 2):
            decision, reason = say(monkeypatch, capsys, command, repo)
            assert decision == "deny", (attempt, reason)
            assert ASK_TOOL not in reason
            assert "pressed `automation`" in reason

    # --- S4: three of the four measured shapes refused, the fourth silent -----

    def test_three_measured_shapes_are_refused_under_the_press(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S4. The session directory is opted in and undeclared, and W is
        declared, as in the measured run. Without the press each is what it was:
        a deny, then an ask. Under it, a deny both times.

        Three of the four. The fourth, a patch whose body loops over a commit
        string, is the one heredoc shape work item 1791089603 (#739) makes data,
        and it left on the owner's answer to that work item's Q1:
        `test_the_fourth_measured_shape_is_silent_under_the_press` pins it."""
        session = staged_repo(tmp_path / "session")
        w = staged_repo(tmp_path / "w", declared=True)
        press(projects, session)
        for name, command in measured(w).items():
            plain = [say(monkeypatch, capsys, command, session, PLAIN)[0] for _ in "12"]
            pressed = [say(monkeypatch, capsys, command, session)[0] for _ in "12"]
            assert plain == ["deny", "ask"], (name, plain)
            assert pressed == ["deny", "deny"], (name, pressed)
            forget_the_budget(session)

    def test_the_fourth_measured_shape_is_silent_under_the_press(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """Q1 of work item 1791089603: the fourth measured shape is a Python
        program's text, and nothing on it commits."""
        session = staged_repo(tmp_path / "session")
        w = staged_repo(tmp_path / "w", declared=True)
        press(projects, session)
        command = moved_row(w)
        plain = [say(monkeypatch, capsys, command, session, PLAIN)[0] for _ in "12"]
        pressed = [say(monkeypatch, capsys, command, session)[0] for _ in "12"]
        assert plain == pressed == ["silent", "silent"], (plain, pressed)

    # --- S5: what the refusal says ----------------------------------------------

    def test_the_refusal_names_the_ways_on_that_need_nobody(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S5, pinned (contract rule 14). The ways on are in this order: make the
        repository readable, edit through the tools, the waiver only where no
        work item owns the commit, and hand back otherwise. Seen red by deleting
        each sentence of the text in turn."""
        for where, reason in reasons_under_the_press(
            monkeypatch, capsys, projects, tmp_path
        ).items():
            flat = " ".join(reason.split())
            order = [
                "pressed `automation` on the routing question",
                "so this gate puts no question to them",
                "The ways on, none of which needs a person:",
                "Re-issue the commit so the repository it lands in can be read:",
                "`git -C <absolute path> commit …` in a command of its own",
                "joined to the commit by `&&` alone",
                "because a failed `cd` leaves the shell there",
                "goes through the `Edit` tool, and a new file through the `Write` tool",
                "Neither leaves a command line for this gate to read.",
                "Only for a commit that belongs to no work item",
                ": '[no-review]'; <the same command>",
                "the marker is a pathspec and git rejects the command",
                "hand it back",
                "Re-issuing this command unchanged meets this same refusal.",
            ]
            at = []
            for phrase in order:
                assert phrase in flat, f"{where}: lost {phrase!r}"
                at.append(flat.index(phrase))
            assert at == sorted(at), f"{where}: the ways on are out of order"
            assert ASK_TOOL not in flat, where

    def test_the_refusal_still_says_what_was_stopped(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """The state each base prompt opens with stays: which mark is missing in
        which repository, or that the repository could not be read."""
        reasons = reasons_under_the_press(monkeypatch, capsys, projects, tmp_path)
        assert reasons["resolved"].startswith("No review is recorded for this cycle")
        assert reasons["unreadable"].startswith(
            "This command contains something the gate cannot read"
        )

    def test_a_later_routing_answer_takes_the_press_back(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """Round 1 of 1790644505, yellow 5. A session that pressed `automation` for
        one work item and then answered `per axis` for another has, on its latest
        answer, a person who may be asked; the automation text would tell the
        model not to. The last answer from this clone stands, so the gate goes
        back to the base's deny-then-ask. The guard shares this reader but reads
        its creation record first, so it asks again only while no creation has
        run; a record written under the press stands (round 2 of 1790644505). A
        later `automation` press gives the press back."""
        repo = staged_repo(tmp_path / "repo")
        first = ask_entries(repo, tool_id="toolu_01first")
        later = ask_entries(repo, answer="per axis", tool_id="toolu_01later")
        write_transcript(projects, PRESSED, first + later)
        assert not worktree_consent.automation_answered(str(repo), PRESSED)
        got = [say(monkeypatch, capsys, "git commit -m x", repo)[0] for _ in "12"]
        assert got == ["deny", "ask"]
        again = ask_entries(repo, tool_id="toolu_01again")
        write_transcript(projects, PRESSED, first + later + again)
        assert worktree_consent.automation_answered(str(repo), PRESSED)

    # --- S6: without the press, nothing changes ---------------------------------

    def test_without_the_press_the_answer_is_the_bases(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S6. Every way of not finding the press is byte-identical to the answer
        with no transcript at all, which is the base's answer."""
        repo = staged_repo(tmp_path / "repo")
        reference = sequence(monkeypatch, capsys, repo, PLAIN)
        assert [d for d, _ in reference] == ["deny", "ask", "deny", "ask"]

        other = tmp_path / "other"
        subprocess.run(
            ["git", "init", "-q", str(other)], check=True, capture_output=True
        )

        def sidechain():
            use, result = ask_entries(repo)
            result["isSidechain"] = True
            return [use, result]

        variants = {
            "per axis": ask_entries(repo, answer="per axis"),
            "an Other answer": ask_entries(
                repo, answer="automation - but ask me first"
            ),
            "a sidechain entry": sidechain(),
            "a press in another clone": ask_entries(other),
            "an unreadable transcript": ["{not json", '{"toolUseResult": {"answers'],
        }
        for name, entries in variants.items():
            write_transcript(projects, PLAIN, entries)
            assert sequence(monkeypatch, capsys, repo, PLAIN) == reference, name

        # A directory where the file would be.
        path = write_transcript(projects, PLAIN, [])
        path.unlink()
        path.mkdir()
        assert sequence(monkeypatch, capsys, repo, PLAIN) == reference, "a directory"

    def test_a_reader_that_raises_or_did_not_load_is_no_press(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S6, contract rule 13. `hooks/dispatch.py` skips a gate that raises, and a
        skipped gate is silence, so the reader failing must land on the base's
        answer rather than on nothing. Seen red with the guard around the reader
        removed."""
        repo = staged_repo(tmp_path / "repo")
        press(projects, repo)
        reference = sequence(monkeypatch, capsys, repo, PLAIN)

        def raises(*_args, **_kwargs):
            raise RuntimeError("a transcript shape nobody measured")

        with monkeypatch.context() as m:
            m.setattr(worktree_consent, "automation_answered", raises)
            assert sequence(monkeypatch, capsys, repo, PRESSED) == reference
        with monkeypatch.context() as m:
            m.setattr(gate, "worktree_consent", None)
            assert sequence(monkeypatch, capsys, repo, PRESSED) == reference

    def test_the_press_is_read_only_once_a_stop_is_decided(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """The transcript scan is paid on a stop and never on a command the gate
        lets through. Seen red by reading the press before the declaration."""
        session = staged_repo(tmp_path / "session")
        w = staged_repo(tmp_path / "w", declared=True)
        press(projects, session)
        calls = []
        real = worktree_consent.automation_answered

        def counted(*args, **kwargs):
            calls.append(args)
            return real(*args, **kwargs)

        monkeypatch.setattr(worktree_consent, "automation_answered", counted)
        for command in ("git status", f"git -C {q(w)} commit -m x", "echo git commit"):
            assert say(monkeypatch, capsys, command, session)[0] == "silent", command
        assert calls == []
        assert say(monkeypatch, capsys, "git commit -m x", session)[0] == "deny"
        assert len(calls) == 1

    def test_a_session_with_no_id_still_asks(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S6. No session id, no transcript to read, and no way to record that a
        question was put, so a deny would repeat forever."""
        repo = staged_repo(tmp_path / "repo")
        press(projects, repo)
        for command in ("git commit -m x", UNREADABLE_BODY):
            assert say(monkeypatch, capsys, command, repo, None)[0] == "ask", command

    # --- S8: a declared target stays silent -------------------------------------

    def test_a_declared_target_stays_silent_under_the_press(
        self, monkeypatch, capsys, projects, tmp_path
    ):
        """S8. The press is read only after a stop is decided, so a commit the
        base lets through is let through. Seen red by a mutation that refuses
        under the press before the declaration is read."""
        session = staged_repo(tmp_path / "session")
        w = staged_repo(tmp_path / "w", declared=True)
        press(projects, session)
        for command in (f"cd {q(w)} && git commit -m x", f"git -C {q(w)} commit -m x"):
            assert say(monkeypatch, capsys, command, session) == ("silent", ""), command

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

    # --- what a body, an `eval` or a comment hands the gate --------------------

    @pytest.mark.rule("one-heredoc-shape-is-data")
    @pytest.mark.parametrize(
        ("command", "session"),
        [
            ("bash <<'EOF'\ngit commit -m x\nEOF", "h"),
            ("eval 'git commit -m x'", "e"),
            ("bash <<'OUTER'\nbash <<'INNER'\ngit commit -m x\nINNER\nOUTER", "nest1"),
            ("eval eval 'git commit -m x'", "nest2"),
            ('eval "$(cat payload.txt)"', "nest3"),
        ],
        ids=[
            "an-interpreter-fed-body",
            "an-eval-argument",
            "a-body-inside-a-body",
            "an-eval-of-an-eval",
            "an-eval-of-a-substitution",
        ],
    )
    def test_refuses_a_commit_a_body_or_an_eval_hands_to_a_shell(
        self, tmp_path, command, session
    ):
        """issue #75. Each row hands a commit to something that runs it.

        `bash <<'EOF'` hands its body to a shell that EXECUTES it, unlike
        `cat`, which only reads it as data. The reader cannot tell the two apart
        without the interpreter enumeration issue #75 rejects, so a dropped body
        that reads as a commit stops either way — the accepted cost is a stop on
        a script that WRITES those words without running them.

        `eval 'git commit -m x'` really commits, and the segment's own command
        word is `eval`, not `git`. `eval` concatenates its arguments and
        re-parses the result, which is the same question `_hides_a_commit`
        answers for a dropped heredoc body.

        Nested: `bash <<'OUTER'` feeds a body that itself opens `bash <<'INNER'`,
        and `_hides_a_commit` used to strip the inner heredoc without re-checking
        what it stripped. `eval eval '…'` re-parses into an `eval` invocation,
        and `_eval_argument` peeled one layer only. `eval "$(cat payload)"` runs
        a command this process cannot read, the same fact that makes
        `git -C "$WT"` Unresolved rather than silently passed.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run(command, here, session=session)
        assert decision_of(out) == "deny", decision_of(out)

    def test_a_heredoc_body_mentioning_commit_in_prose_does_not_stop(self, tmp_path):
        """`_reads_as_commit` reuses `parse_git`'s own rule — a segment's own
        first token must literally be `git` — so a heredoc body that only
        MENTIONS the words does not invent an invocation out of prose."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run(
            "cat > notes.md <<'EOF'\nremember to git commit before lunch\nEOF",
            here,
            session="n",
        )
        assert not fired(out), (
            f"prose inside a heredoc body stopped: {decision_of(out)}"
        )

    def test_an_eval_argument_that_does_not_commit_does_not_stop(self, tmp_path):
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run("eval 'echo hello'", here, session="q")
        assert not fired(out), f"an eval with no commit stopped: {decision_of(out)}"

    @pytest.mark.parametrize(
        "comment",
        [
            "# stage everything; then commit",
            "git add -A  # stage; then",
            "# do the thing; done",
            "# check if it built; if so commit",
        ],
    )
    def test_a_comment_is_not_a_construct(self, tmp_path, comment):
        """The judgment read drops comments, so English in one is not shell.

        A comment segment's first token used to be `#`, which is neither a `cd`
        nor a `git`, so nothing read it and the gate did not need to drop it --
        `hooks/worktree-guard.py` dropped comments and this gate did not, and the
        difference cost nothing. Reading a segment for what CONSTRUCT it is ended
        that: `# stage everything; then commit` splits at the `;`, the next
        segment starts with the reserved word `then`, and an ordinary commit two
        lines later was stopped for a sentence in English.

        Driven through the gate rather than the reader, because the reader is not
        where the two reads diverge -- the gate's own line is.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        declare_routing(here)
        out = run(f"{comment}\ngit commit -m x", here, session="s1")
        assert not fired(out), (
            f"a comment stopped an ordinary commit: {decision_of(out)}"
        )

    # --- which repository the commit lands in -----------------------------------

    @pytest.mark.rule("executed-text-is-read")
    def test_a_commit_aimed_elsewhere_is_judged_there(self, tmp_path):
        """The measured defect: the prompt belonged to a repo the commit never touches."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        there = make_repo(tmp_path / "scratch", opted_in=False)
        out = run(f"git -C {sh(there)} commit -m 'scratch'", here)
        assert decision_of(out) == "silent", (
            f"the commit lands in {there}, which never opted in; the gate judged the shell"
        )

    def test_a_commit_in_the_repository_the_shell_sits_in_still_gates(self, tmp_path):
        """The fix must not cost the gate its actual job."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        assert fired(run("git commit -m 'change'", here))

    def test_the_gate_fires_for_the_named_repository_from_outside(self, tmp_path):
        """The other direction: the shell is elsewhere and the commit lands in the repo."""
        here = make_repo(tmp_path / "plain", opted_in=False)
        there = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run(f"git -C {sh(there)} commit -m 'change'", here)
        assert fired(out)
        assert (
            "[no-review]"
            in json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        )

    @pytest.mark.rule("executed-text-is-read")
    def test_a_cd_reaches_the_repository_the_commit_lands_in(self, tmp_path):
        """S1. The measured fail-open: `cd <repo> && git commit` was judged
        against the directory the session started in, so the same commit into the
        same repository was stopped when written with `-C` and silent when
        written with `cd`."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        there = make_repo(tmp_path / "scratch", opted_in=True)
        out = run(f"cd {sh(there)} && git commit -m x", here, session="s1")
        assert fired(out)
        reason = reason_of(out)
        assert str(there) in reason, (
            "the verdict is about the repository the commit misses"
        )
        assert str(here) not in reason

    def test_a_cd_inside_one_repository_costs_what_it_always_did(self, tmp_path):
        """S2. The same-root shortcut, which is what keeps this fix cheap.

        Where every directory the command reaches sits in one repository, the
        operator does not matter and neither does the `cd`: the verdict and the
        prompt are the ones the gate gave before it could read either. Without
        this, `cd src && git commit` — the common harmless form — costs a prompt
        of its own, which is the prompt volume issue #45 exists to reduce.

        This case compares two forms inside ONE build, so a regression that moves
        both is invisible to it. `test_the_same_root_forms_answer_what_the_release_did`
        below is the half that cannot: it drives the LAST RELEASE's gate.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        (here / "src").mkdir()
        plain = run("git commit -m x", here, session="plain")
        walked = run(
            f"cd {sh(here / 'src')} && git commit -m x", here, session="walked"
        )
        assert decision_of(plain) == decision_of(walked) == "deny"
        assert reason_of(plain) == reason_of(walked), (
            "a cd within one repository changed the prompt the user sees"
        )

    def test_the_same_root_forms_answer_what_the_release_did(self, tmp_path):
        """The same-root shortcut against the gate people are actually running.

        Six forms whose directories all sit in one repository. Every one has to
        return the same decision AND the same reason text as the last release —
        the reason as well, because that is what the user reads, and a prompt that
        changed wording for a `cd` the release could not even see would be a new
        prompt wearing an old verdict.

        A different session id per revision: the budget marker lives in the
        repository's git dir, so a shared id would make the second run meet the
        `ask` that follows a `deny` and report a difference that is the test's own
        doing.

        One difference is deliberate and is masked rather than tolerated loosely.
        The release resolved the printed root with a `rev-parse --show-toplevel`
        of its own, and git answers with forward slashes on every platform, so on
        Windows it addressed the user in a dialect no Windows path is written in.
        This gate routes that through `optin.repo_root`, which spells the path the
        way the platform does. Caught by CI on the Windows runner, where the two
        spellings are the whole of the difference and the verdicts are identical.

        Masking the path — rather than comparing decisions alone — is what keeps
        the pin able to fail: a wording change anywhere else in the prompt still
        turns it red, which is the property this case was added for.

        WHAT IS COMPARED ACROSS RELEASES, AND WHAT IS NOT. The fear in the
        paragraph above is a prompt that changed *for one form* — the `cd` the
        release could not see getting different words from the plain commit. That
        is a per-form property, and comparing whole texts across releases is a
        coarse way to reach it: it also pins the WAYS-ON list, which is advice and
        is expected to improve. It went red the first time that list gained an
        option, on a change that touched no form at all.

        So the two properties are separated and both are asserted. Across
        releases, per form: the decision and the STATE — the sentences saying what
        is wrong, which is the part a verdict is made of. Across the six forms,
        within each revision: the ENTIRE reason, byte for byte. A prompt that
        changed wording for one form fails the second check whichever release it
        is in, which is the property this case was added for, stated directly
        rather than through a proxy.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        (here / "src").mkdir()
        # The released hooks read the root at its 0.3 address. Both roots are
        # present so each revision sees an opted-in repository, and the comparison
        # stays about the command forms, which is the only thing it is about.
        (here / ".specseal").mkdir()
        old = tmp_path / "released"
        tag = released_hooks(old)

        def released(command, cwd, session):
            r = subprocess.run(
                [sys.executable, str(old / "commit-review-gate.py")],
                input=json.dumps(
                    {
                        "tool_name": "Bash",
                        "tool_input": {"command": command},
                        "cwd": str(cwd),
                        "session_id": session,
                    }
                ),
                capture_output=True,
                encoding="utf-8",
                timeout=60,
            )
            if not r.stdout.strip():
                return ("silent", "")
            d = json.loads(r.stdout)["hookSpecificOutput"]
            return (d["permissionDecision"], d["permissionDecisionReason"])

        def one_spelling(verdict):
            """`verdict` with the repository's own path reduced to one address."""
            decision, reason = verdict
            native = str(here)
            for spelling in (native, native.replace("\\", "/")):
                reason = reason.replace(spelling, "<repo>")
            return decision, reason

        forms = [
            ("git commit -m x", here),
            (f"cd {sh(here / 'src')} && git commit -m x", here),
            ("cd src && git commit -m x", here),
            ("cd . && git commit -m x", here),
            (f"cd {sh(here)} && git commit -m x", here / "src"),
            ("git -C src commit -m x", here),
        ]

        def state_half(reason):
            """The reason minus its ways-on list.

            The list starts at whichever of the two headers this prompt carries —
            the deny spends its reason on the question, the ask renders buttons.
            A reason with neither RAISES. Returning it whole was the safe-looking
            direction and is the quiet one: the comparison would go back to
            pinning the entire text, which is what this rewrite exists to stop,
            and nothing would say so. Every prompt this gate emits carries one of
            the two headers -- both `question_reason` shapes, `ask_reason`, and
            the unreadable arm's two branches -- so reaching the end means a
            header was reworded, which is exactly when someone needs to look.
            """
            if not reason:
                return reason
            for header in (
                "\n\nDo not choose for the user.",
                "\n\nApproving is the waiver",
            ):
                if header in reason:
                    return reason.split(header, 1)[0]
            raise AssertionError(
                "no ways-on header found, so this comparison would silently "
                f"widen back to the whole text: {reason[:200]!r}"
            )

        was_all, now_all = [], []
        for i, (command, cwd) in enumerate(forms):
            was = one_spelling(released(command, cwd, f"rel{i}"))
            now = run(command, cwd, session=f"new{i}")
            now = one_spelling(
                ("silent", "")
                if not now.strip()
                else (
                    json.loads(now)["hookSpecificOutput"]["permissionDecision"],
                    json.loads(now)["hookSpecificOutput"]["permissionDecisionReason"],
                )
            )
            was_all.append((command, was))
            now_all.append((command, now))
            assert was[0] == now[0], (
                f"{command!r} differs from {tag}: {was[0]} -> {now[0]}"
            )
            assert state_half(was[1]) == state_half(now[1]), (
                f"{command!r}'s STATE differs from {tag}\n"
                f"was: {state_half(was[1])[:200]}\nnow: {state_half(now[1])[:200]}"
            )

        # No form may be told anything the others are not, in either revision.
        for label, group in ((tag, was_all), ("this revision", now_all)):
            first_command, first = group[0]
            for command, verdict in group[1:]:
                assert verdict == first, (
                    f"in {label}, {command!r} answers differently from "
                    f"{first_command!r}, and both sit in one repository\n"
                    f"{first_command!r}: {first[0]} {first[1][:200]}\n"
                    f"{command!r}: {verdict[0]} {verdict[1][:200]}"
                )

    def test_a_declaration_still_silences_a_cd_within_its_own_repository(
        self, tmp_path
    ):
        """The other half of S2: the answer given for this repository still
        answers for a commit that lands in this repository."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        (here / "src").mkdir()
        declare_routing(here)
        assert decision_of(run(f"cd {sh(here / 'src')} && git commit -m x", here)) == (
            "silent"
        )

    def test_or_reaches_both_the_session_and_the_destination(self, tmp_path):
        """S3. `||` runs the commit where the shell already was, and reaches the
        destination only when the `cd` failed. Both are targets, and the operator
        is the only thing that says so."""
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        out = run(f"cd {sh(there)} || git commit -m x", here, session="s1")
        assert fired(out)
        reason = reason_of(out)
        assert str(here) in reason and str(there) in reason
        assert "also commits into" in reason

    def test_a_pipeline_does_not_spend_another_repositorys_declaration(self, tmp_path):
        """The same forgery as S7, reached through a pipeline instead of `&&`.

        Measured before the fix: `cd <B> | git commit` was SILENT where the parent
        commit denied. The commit lands in the session's own repository, which has
        nothing recorded; the declaration that silenced it belongs to `<B>`.
        """
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        declare_routing(there)
        for sep in ("|", "|&"):
            out = run(
                f"cd {sh(there)} {sep} git commit -m x", here, session=f"pipe{sep}"
            )
            assert fired(out), (
                f"{sep}: {there}'s declaration answered for a commit in {here}"
            )
            assert str(here) in reason_of(out), sep

    def test_a_heredoc_body_does_not_spend_another_repositorys_declaration(
        self, tmp_path
    ):
        """S7's forgery, reached through a heredoc instead of an operator."""
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        declare_routing(there)
        command = (
            f"cat > run.sh <<'EOF'\ncd {sh(there)}\nmake\nEOF\n"
            "git add -A && git commit -m x"
        )
        out = run(command, here, session="heredoc")
        assert fired(out), f"{there}'s declaration answered for a commit in {here}"
        assert str(here) in reason_of(out)

    def test_a_middle_segment_does_not_spend_another_repositorys_declaration(
        self, tmp_path
    ):
        """The same forgery, reached by putting one segment between the `cd` and
        the `||` that consumes its failure."""
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        declare_routing(there)
        out = run(f"cd {sh(there)} && make || git commit -m x", here, session="middle")
        assert fired(out)
        assert str(here) in reason_of(out)

    def test_a_skipped_branch_still_reaches_the_gate(self, tmp_path):
        """`cd <N> || cd <B> && git commit` was silent before the fix: only `<B>`
        survived as a candidate, and `<B>` carries a declaration."""
        here = make_repo(tmp_path / "repoA", opted_in=True)
        nowhere = make_repo(tmp_path / "repoN", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        declare_routing(there)
        out = run(
            f"cd {sh(nowhere)} || cd {sh(there)} && git commit -m x",
            here,
            session="skip",
        )
        assert fired(out)
        assert str(nowhere) in reason_of(out), (
            "the branch where the second cd is skipped"
        )

    def test_a_cd_the_gate_cannot_read_stops_the_commit(self, tmp_path):
        """S4. The gate reads the command before the shell expands it, so `cd
        "$WT"` names a directory it cannot identify. That is not a repository
        checked and found clean; it joins the partition an unresolvable `-C`
        already has (docs/commit-review-gate-spec.md)."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run('cd "$WT" && git commit -m x', here, session="s1")
        # The parent commit ALSO denies here, for the ordinary reason — it judged
        # the session's own repository, which has no review mark. So the decision
        # alone distinguishes nothing, and the two assertions below are what do:
        # the prompt has to be the unreadable-target one, naming the value it
        # could not expand.
        assert decision_of(out) == "deny"
        reason = reason_of(out)
        assert "$WT" in reason, "the prompt has to name what it could not read"
        assert "could not be read" in reason, (
            "this is the ordinary review prompt, which is what the parent commit "
            "returned — the target was judged rather than reported as unreadable"
        )

    def test_the_prompt_offers_the_way_out_that_exists(self, tmp_path):
        """Two ways a target goes unreadable, and only one of them has a value to
        write out.

        The unreadable-target prompt leads with "write the absolute path in place
        of the unresolved value", which is a real instruction for `cd "$WT"` and
        an impossible one for an `eval` — there is no such value, and the
        directory named is the session's own. Both arms then collapsed onto
        `[no-review]`, which is the standing waiver this gate exists to avoid.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)

        value = reason_of(run('cd "$WT" && git commit -m x', here, session="v"))
        assert "could not resolve to a repository" in value
        assert "Write the path out" in value, value

        construct = reason_of(
            run("eval 'cd /elsewhere' && git commit -m x", here, session="c")
        )
        assert "cannot read as a plain command" in construct, construct
        assert "Say where it commits" in construct, construct
        assert "Write the path out" not in construct, (
            "the construct arm offers an instruction that cannot be followed"
        )

    def test_one_directory_is_announced_once(self, tmp_path):
        """The reader can reach one directory twice, for two different reasons.
        The prompt counts directories, not states.

        `cd "$WT" && eval '…' | git commit` reaches `<cwd>/$WT` as a value that
        could not be expanded and again as a state an `eval` marked, and the
        prompt announced "2 directories" naming the same path twice — the reader's
        bookkeeping leaking into what the user reads.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        reason = reason_of(
            run(
                "cd \"$WT\" && eval 'cd /elsewhere' | git commit -m x",
                here,
                session="d",
            )
        )
        first = reason.splitlines()[0]
        assert "2 directories" not in first, first
        assert first.count("$WT") == 1, first

    @pytest.mark.parametrize(
        "command",
        [
            "cd \"$WT\" || eval 'cd /elsewhere' || git commit -m x",
            # Both reasons at ONE path. The prompt lists paths once and judges the
            # arm over every target, and only this shape tells the two apart --
            # judging over the deduplicated list gives the construct arm, which
            # says nothing about writing a path out and cannot speak for `$WT`.
            "cd \"$WT\" | eval 'cd /elsewhere' || git commit -m x",
        ],
    )
    def test_a_command_reaching_both_kinds_does_not_get_the_narrower_prompt(
        self, tmp_path, command
    ):
        """One command can reach both, and the prompt has to answer for both.

        `cd "$WT"` leaves a target the reader could not expand and the `eval`
        leaves one it could not follow. The construct wording says nothing about
        writing a path out, so it cannot speak for the value half.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        both = reason_of(run(command, here, session="b"))
        assert "Write the path out" in both, both

    def test_a_cd_into_no_repository_stops_rather_than_going_silent(self, tmp_path):
        """A `cd` names a directory the way a `-C` does, and the stop follows from
        that rather than from the destination looking odd.

        Found by the broad gate, not by design: reading the `cd` while still
        counting only `-C` as "the command named a directory" sent
        `cd sub && git commit` — where `sub` is no repository — to the early
        return in `judge`, which is silence. That is issue #56's fail-open reached
        through the new door, and the case that caught it
        (`tests/test_chain_hooks_hardening.py:91`) predates this work.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run("cd sub && git commit -m x", here, session="s1")
        assert decision_of(out) == "deny"
        assert "sub" in reason_of(out), "the prompt has to name what it could not read"

    @pytest.mark.parametrize(
        "command",
        ['cd "$WT" && git commit -m x', 'git -C "$WT" commit -m x'],
        ids=["an-unreadable-cd", "an-unreadable-dash-c"],
    )
    def test_accepts_silence_on_an_unreadable_target_where_the_plugin_has_no_standing(
        self, tmp_path, command
    ):
        """A globally installed plugin must not prompt in repositories that never
        opted in. The session's own repository is what gives the gate standing to
        speak about a target it cannot identify, for a `cd` as for a `-C` — it is
        not used to judge that target, which would answer for a repository the
        commit may never touch."""
        here = make_repo(tmp_path / "plain", opted_in=False)
        assert decision_of(run(command, here, session="s1")) == "silent"

    def test_a_subshell_does_not_carry_a_commit_past_the_gate(self, tmp_path):
        """S5. `(cd <repo> && git commit)` tokenizes its first word as `(cd`, so
        the cd was invisible and the commit was not — the fail-open reproduced
        with one parenthesis."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        there = make_repo(tmp_path / "scratch", opted_in=True)
        declare_routing(here)
        out = run(f"(cd {sh(there)} && git commit -m x)", here, session="s1")
        assert decision_of(out) != "silent", (
            "the declaration in the session's repository carried a commit that "
            "may land in another one"
        )

    def test_a_subshell_commit_with_no_trailing_argument_is_still_a_commit(
        self, tmp_path
    ):
        """`(git commit)` puts the closing parenthesis on the SUBCOMMAND.

        `parse_git` then read it as `commit)`, no invocation was found, and the
        gate returned before any of this work's walking was used. The `-m x` form
        hides it because the paren attaches to the argument instead — which is
        why the S5 case above passed while this one did not.

        Silent before this change as well, so it is not a regression. It is fixed rather
        than documented as an exception because `spec.md` S5 and
        `docs/commit-review-gate-spec.md` both claim the subshell case is closed, and a
        commit inside a subshell commits for real.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        assert fired(run("(git commit)", here, session="s1")), (
            "a commit wrapped in a bare subshell was invisible to the gate"
        )

        there = make_repo(tmp_path / "scratch", opted_in=True)
        declare_routing(here)
        assert decision_of(
            run(f"(cd {sh(there)} && git commit)", here, session="s2")
        ) != ("silent")

    def test_cd_dash_is_judged_where_the_shell_returns_to(self, tmp_path):
        """S6. The previous directory is state the reader has to carry, and
        carrying it is what keeps an ordinary shell form from stopping."""
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        third = make_repo(tmp_path / "repoC", opted_in=True)

        # Two steps, so the answer is NOT the directory the session started in.
        # A one-step `cd B && cd - && git commit` returns to the session's own
        # repository, which is also what a reader that cannot follow `cd` at all
        # answers — the case passed unchanged on the parent commit and so
        # distinguished nothing.
        out = run(
            f"cd {sh(third)} && cd {sh(there)} && cd - && git commit -m x",
            here,
            session="s1",
        )
        assert fired(out)
        reason = reason_of(out)
        assert str(third) in reason, (
            "the shell returned to repoC, and the verdict follows"
        )
        assert str(here) not in reason, "the session's own repository is not the target"
        assert str(there) not in reason, "the shell came back; the verdict did not"

    def test_a_declaration_does_not_travel_to_another_repository(self, tmp_path):
        """S7. The direction that forges what this project sells.

        `A` was given a routing answer for its own branch. The commit lands in
        `B`, which has no declaration and no review mark. Measured on the unfixed
        gate: the declaration found in `A` made the arm silent, so the commit went
        through unjudged — and there was no moment at which anyone could have
        typed a waiver or clicked a prompt. The same command with `git -C` denied.
        """
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        declare_routing(here)

        assert decision_of(run("git commit -m x", here, session="s1")) == "silent", (
            "the declaration has to keep answering for its own repository"
        )
        out = run(f"cd {sh(there)} && git commit -m x", here, session="s1")
        assert fired(out), "a declaration given for repoA silenced a commit into repoB"
        assert str(there) in reason_of(out)

    def test_a_chdir_the_gate_cannot_resolve_stops_the_commit(self, tmp_path):
        """Issue #56. This used to be silent, and silence was the whole hole.

        A `-C` value that resolves to no repository is not a repository the gate
        checked and found clean. It is a repository the gate never saw. Those had
        the same outcome — nothing — and the second is the one that ships an
        unreviewed commit.

        It reverses `test_a_chdir_to_no_repository_decides_nothing`, which pinned
        the silence as intended behaviour on the grounds that a non-existent path
        is not opted in. That reasoning holds only if the path is what it looks
        like, and the next case shows it need not be.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run(
            f"git -C {sh(tmp_path / 'nowhere')} commit -m 'x'", here, session="s1"
        )
        assert decision_of(out) == "deny"
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "nowhere" in reason, "the prompt has to name what it could not read"

    def test_a_shell_variable_reaches_the_gate_unexpanded(self, tmp_path):
        """The form every agent in the release session was told to write.

        The hook reads `tool_input.command` before the shell touches it, so the
        `-C` value arrives as the four characters `$WT`. It names no directory,
        and the repository the commit really lands in is never looked at.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        assert fired(run('git -C "$WT" commit -m x', here, session="s1"))

    def test_the_marker_still_waives_an_unreadable_target(self, tmp_path):
        """Both answers have to continue, and the second one is the token."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        out = run('git -C "$WT" commit -m x [no-review]', here, session="s1")
        assert decision_of(out) == "silent"

    def test_a_second_attempt_falls_to_the_plain_prompt(self, tmp_path):
        """The budget is the gate's existing one: deny once per session per repo."""
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        assert (
            decision_of(run('git -C "$WT" commit -m x', here, session="s2")) == "deny"
        )
        assert decision_of(run('git -C "$WT" commit -m x', here, session="s2")) == "ask"

    def test_a_directory_with_the_home_marker_but_no_repository(self, tmp_path):
        """`seal/` outside a repository is still not an opt-in.

        Two halves, and they now differ. Named by a `-C`, it is a target the gate
        could not resolve, so it stops (above). Sitting in it with no `-C`, there
        is no repository and no command naming one, so there is nothing to stop.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        fake = tmp_path / "looks-opted-in"
        (fake / "seal").mkdir(parents=True)
        assert fired(run(f"git -C {sh(fake)} commit -m 'x'", here, session="s1"))
        assert decision_of(run("git commit -m 'x'", fake, session="s1")) == "silent"

    def test_the_prompt_names_the_repository_the_verdict_is_about(self, tmp_path):
        """Measured: a review run where the session sits marks the WRONG repo.

        Shell in repoA, commit into repoB, both opted in. The mark has to land in
        repoB; a mark in repoA changes nothing. The prompt is the only place that
        can say so, and it used to name no repository at all — so the model ran
        the review in its own cwd, the gate kept stopping the commit, and the
        budget ran out into an `ask` that ships repoB unreviewed on one click.
        """
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        command = f"git -C {sh(there)} commit -m 'change'"

        # The deny carries the options; the `ask` after it carries only the state
        # and the ways on — and the `ask` is the one that ships the commit on a
        # single click, so both have to name the repository.
        first = run(command, here, session="s1")
        assert decision_of(first) == "deny"
        denied = json.loads(first)["hookSpecificOutput"]["permissionDecisionReason"]
        assert f"AGAINST {there}" in denied, (
            "the review is not steered at the target repo"
        )

        after = run(command, here, session="s1")
        assert decision_of(after) == "ask"
        asked = json.loads(after)["hookSpecificOutput"]["permissionDecisionReason"]
        assert f"review chain against {there}" in asked

        # The state is the FIRST paragraph of both reasons and the sentence a
        # person reads before anything else. Asserting the whole reason would let
        # the way on satisfy it alone, so this one looks at the state itself.
        for label, reason in (("deny", denied), ("ask", asked)):
            assert str(there) in reason.split("\n\n")[0], (
                f"the {label} state does not say which repository it is about"
            )

    def test_the_parity_arm_names_the_repository_too(self, tmp_path):
        """The other arm had no case at all, so its address was never read.

        `[no-review]` waives the review arm, leaving the migration-config arm
        alone in the prompt — the same three places have to carry the target.
        """
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        (there / "seal" / "parity.md").write_text(
            "# migration config\n", encoding="utf-8"
        )
        command = f"git -C {sh(there)} commit -m 'change' [no-review]"

        first = run(command, here, session="s1")
        assert decision_of(first) == "deny"
        denied = json.loads(first)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "[no-parity]" in denied, "the review arm was supposed to be waived"
        assert "[no-review]" not in denied
        assert str(there) in denied.split("\n\n")[0], "the state names no repository"
        assert f"in {there}'s migration config" in denied, (
            "the comparison is not steered"
        )

        after = run(command, here, session="s1")
        asked = json.loads(after)["hookSpecificOutput"]["permissionDecisionReason"]
        assert decision_of(after) == "ask"
        assert f"compare {there} against the original" in asked
        assert str(there) in asked.split("\n\n")[0]

    def test_a_mark_in_the_shells_repository_does_not_answer_for_the_target(
        self, tmp_path
    ):
        """The fact the prompt exists to convey, pinned on its own."""
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)

        def mark(repo):
            gd = subprocess.run(
                ["git", "-C", str(repo), "rev-parse", "--absolute-git-dir"],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            ).stdout.strip()
            head = subprocess.run(
                ["git", "-C", str(repo), "rev-parse", "HEAD"],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            ).stdout.strip()
            (Path(gd) / "specseal-reviewed").write_text(head, encoding="utf-8")

        command = f"git -C {sh(there)} commit -m 'change'"
        mark(here)
        assert fired(run(command, here)), (
            "a mark in the shell's repo answered for the target"
        )
        mark(there)
        assert decision_of(run(command, here)) == "silent"

    def test_a_second_repository_is_announced_in_the_first_prompt(self, tmp_path):
        """One command, two repositories, one decision — say the next one is coming."""
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        command = f"git commit -m x && git -C {sh(there)} commit -m y"

        # The two decisions mean opposite things. A deny cancels the command, so
        # the retry meets repoB; an approved `ask` runs the command whole —
        # measured, both commits land and repoB is never asked about.
        denied = run(command, here, session="s1")
        assert decision_of(denied) == "deny"
        first = json.loads(denied)["hookSpecificOutput"]["permissionDecisionReason"]
        assert str(there) in first, (
            "the retry meets repoB with no warning it was coming"
        )
        assert "the retry meets the next" in first

        asked = run(command, here, session="s1")
        assert decision_of(asked) == "ask"
        second = json.loads(asked)["hookSpecificOutput"]["permissionDecisionReason"]
        assert str(there) in second
        assert "never asked about separately" in second, (
            "the ask path promises a question that approving makes sure never comes"
        )

    def test_the_announcement_names_a_root_not_the_directory_given(self, tmp_path):
        """The other half of grouping by root, which nothing was holding.

        `test_a_subdirectory_is_not_a_further_repository` pins the merging — that
        no announcement appears. When one DOES appear it has to name the same
        thing the two arms name, which is a repository. Reverting the announcement
        to the directory left every case green.
        """
        here = make_repo(tmp_path / "repoA", opted_in=True)
        there = make_repo(tmp_path / "repoB", opted_in=True)
        (there / "sub").mkdir()
        out = run(f"git commit -m x && git -C {sh(there / 'sub')} commit -m y", here)
        assert fired(out)
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "also commits into" in reason
        assert str(there / "sub") not in reason, (
            "the announcement names a directory where the arms name a repository"
        )
        assert str(there) in reason

    def test_a_subdirectory_is_not_a_further_repository(self, tmp_path):
        """Measured: the announcement named a directory that is no repository.

        `git commit && git -C <repo>/sub commit` names two directories and one
        repository. Grouping by the string judged that repository twice and told
        the user a second one was waiting — a path that `git rev-parse` does not
        call a repository at all.
        """
        here = make_repo(tmp_path / "repoA", opted_in=True)
        (here / "sub").mkdir()
        out = run(f"git commit -m x && git -C {sh(here / 'sub')} commit -m y", here)
        assert fired(out)
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "also commits into" not in reason, (
            "a subdirectory of the same repository was announced as another one"
        )

    def test_a_subdirectory_commit_does_not_hide_the_migration_arm(self, tmp_path):
        """Grouping by root left the group one cwd, and a pathspec needs its own.

        A pathspec is resolved against the directory git runs in. With the group's
        cwd taken from whichever invocation came first, `git -C <repo>/sub commit
        && git -C <repo> commit -m y f.py` looked for `<repo>/sub/f.py`, found
        nothing, and `touches_code` reported a commit carrying no files — so the
        migration-config arm lost its grounds and went silent.

        The review mark is written here, which is the ordinary state of a
        repository that has just been reviewed. That leaves the migration-config
        arm as the only gate, and a commit with no comparison against the original
        went out with no prompt at all.
        """
        repo = tmp_path / "repoP"
        (repo / "seal").mkdir(parents=True)
        (repo / "seal" / "parity.md").write_text(
            "# migration config\n", encoding="utf-8"
        )
        subprocess.run(["git", "init", "-q", str(repo)], check=True)

        def git(*a):
            return subprocess.run(
                ["git", "-C", str(repo), *a],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                check=True,
            ).stdout.strip()

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
        (repo / "sub").mkdir()
        # Unstaged on purpose: the pathspec form is then the only view that sees it.
        (repo / "f.py").write_text("x = 2\n", encoding="utf-8")
        Path(git("rev-parse", "--absolute-git-dir"), "specseal-reviewed").write_text(
            git("rev-parse", "HEAD"), encoding="utf-8"
        )

        outside = tmp_path / "elsewhere"
        outside.mkdir()
        plain = f"git -C {sh(repo)} commit -m y f.py"
        subdir_first = f"git -C {sh(repo / 'sub')} commit -m x && {plain}"

        assert fired(run(plain, outside)), "the fixture has to reach the parity arm"
        assert fired(run(subdir_first, outside)), (
            "a subdirectory commit in front of it silenced the migration-config arm"
        )

    # --- a commit behind a reserved word, through `main` ------------------------

    @pytest.mark.parametrize("name", sorted(SHAPES))
    def test_the_gate_stops_the_commit(self, monkeypatch, capsys, tmp_path, name):
        """Through `main()`, in an opted-in repository with no declaration: every
        shape stops, where at `ade83e4e` every one of them was silent."""
        repo = staged_repo(tmp_path / "repo")
        assert decision(monkeypatch, capsys, SHAPES[name][0], repo)[0] == "deny", name

    def test_a_declared_repository_still_stops_a_commit_it_cannot_place(
        self, monkeypatch, capsys, tmp_path
    ):
        """An unresolved directory stops before any declaration is read, the way
        the multi-line spelling always has; the negated commit, which runs where
        the shell is, stays silent in a declared repository like any commit."""
        repo = staged_repo(tmp_path / "repo", declared=True)
        for name, (command, where) in SHAPES.items():
            expected = "silent" if where == HERE else "deny"
            assert decision(monkeypatch, capsys, command, repo)[0] == expected, name
            for marker in (repo / ".git" / "specseal-commit-choice").glob("*"):
                marker.unlink()

    def test_a_heredoc_body_that_loops_over_a_commit_stops(
        self, monkeypatch, capsys, tmp_path
    ):
        """`_hides_a_commit` reads a body through the same `parse_git`."""
        repo = staged_repo(tmp_path / "repo")
        body = f"bash <<'EOF'\nfor d in a; do {C}; done\nEOF"
        assert gate._hides_a_commit(body.split("\n", 1)[1].rsplit("\n", 1)[0])
        assert decision(monkeypatch, capsys, body, repo)[0] == "deny"

    # --- the waiver's form, typed and run ----------------------------------------

    @pytest.mark.parametrize(
        "command",
        [
            ": '[no-review]'; git commit -m x",
            "git commit -m x  # [no-review]",
            "git commit -m x  # [no-review] it's deliberate",
            "git commit -m x  # [no-review] -- don't ask",
        ],
    )
    def test_an_apostrophe_after_the_marker_does_not_silence_the_waiver(
        self, tmp_path, command
    ):
        """Whether the command parses is measured on the command as WRITTEN.

        The judgment read drops comments, so a command carrying an apostrophe in
        one parses cleanly once the comment is gone. That answer used to be handed
        to the CONSENT read, which then ran its strict bare-word scan on the RAW
        command — where the same apostrophe opens a quote that never closes and
        swallows the marker. The waiver was honoured before the judgment read
        started dropping comments and refused after, with nothing to tell the user
        why.

        Since #868 the one consent reader, `hooks/tokens.py#given`, reads the bare
        words before the point a split fails, so a marker written before the
        apostrophe is read. Changed by work item 1791384157: the two apostrophe
        rows had the apostrophe BEFORE the marker, which waived only through
        `has_marker`'s substring fallback; they are
        `test_an_apostrophe_before_the_marker_waives_nothing` now.
        """
        repo = opted_in_repo(tmp_path)
        assert decision_of(
            run_hook("commit-review-gate.py", payload(command, repo))
        ) == ("silent"), command

    @pytest.mark.parametrize(
        "command",
        [
            "git commit -m x  # don't [no-review]",
            "git commit -m x  # it's [no-review], deliberately",
        ],
    )
    def test_an_apostrophe_before_the_marker_waives_nothing(self, tmp_path, command):
        """#868 In 3, the cost `spec.md` of work item 1791384157 names: to a
        reader that reads comments on purpose, the apostrophe opens a quote that
        never closes, and a marker inside it is read as nothing. The substring
        fallback that honoured it is gone, because reading loosely is the one
        direction that waives with nobody asked; the stop names the marker typed
        in front, `: '[no-review]'; git commit …`, which splits. No recorded run
        held this form (`phases/phase-1.md`)."""
        repo = opted_in_repo(tmp_path)
        out = run_hook("commit-review-gate.py", payload(command, repo))
        assert decision_of(out) in ("deny", "ask"), (command, out)
        assert ": '[no-review]'" in out, out

    def test_the_form_the_gate_advises_is_the_one_that_runs(self, tmp_path):
        """Both halves, executed: git accepts it and the gate reads the marker.

        Either half alone is the defect. A form git accepts but the gate cannot
        read stops the commit anyway; a form the gate reads but git rejects is
        what shipped.
        """
        assert SHELLS, f"no shell to test the advice in; unusable: {UNUSABLE_SHELLS}"
        assert not POLLUTED_SHELLS, (
            f"{POLLUTED_SHELLS} are working shells on PATH, so the advised form "
            "should have run in them and did not"
        )
        # The WSL launcher is a Windows fact, and the drop it earns is unconditional
        # only because `os.name` was never asked. On POSIX a name that resolves and
        # then refuses to run a command is a broken environment, not a runner doing
        # what it was told, and letting it drop in silence is half of the shrink
        # round 1's finding 10 named.
        if os.name != "nt":
            assert not UNUSABLE_SHELLS, (
                f"{UNUSABLE_SHELLS} are on PATH and would not run a command; the "
                "runner's WSL `bash` is a Windows-only reason to drop one"
            )
        for shell in SHELLS:
            repo = opted_in_repo(tmp_path / shell)
            cmd = ": '[no-review]'; git commit -m x"
            assert decision_of(
                run_hook("commit-review-gate.py", payload(cmd, repo))
            ) == ("silent"), f"{shell}: the gate did not read the marker"
            r = subprocess.run(
                # Quoted, because this string is about to be a real shell
                # command: an unquoted native path loses its separators to the
                # shell before `cd` ever sees it, and the test then measured
                # whether `cd` can reach a directory that does not exist.
                [shell, "-c", f"cd {shlex.quote(str(repo))} && {cmd}"],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
                env={
                    **os.environ,
                    "GIT_AUTHOR_NAME": "e",
                    "GIT_AUTHOR_EMAIL": "e@e.example",
                    "GIT_COMMITTER_NAME": "e",
                    "GIT_COMMITTER_EMAIL": "e@e.example",
                },
            )
            assert r.returncode == 0, (
                f"{shell}: git rejected the advised form\n{r.stderr}"
            )

    @pytest.mark.parametrize(
        "cmd",
        ["git commit -m x [no-review]", "git commit -m x '[no-review]'"],
    )
    def test_the_form_that_was_advised_is_rejected_by_git(self, tmp_path, cmd):
        """The defect itself, pinned. The gate reads it; git will not take it."""
        assert SHELLS, (
            f"no shell to run the rejected form in; unusable: {UNUSABLE_SHELLS}"
        )
        repo = opted_in_repo(tmp_path / "broken")
        assert decision_of(run_hook("commit-review-gate.py", payload(cmd, repo))) == (
            "silent"
        ), "the marker is read — reading was never the problem"
        r = subprocess.run(
            # The first shell that answered the probe, not the name `bash`:
            # on a `windows-latest` runner that name is the WSL launcher.
            [SHELLS[0], "-c", f"cd {shlex.quote(str(repo))} && {cmd}"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        assert r.returncode != 0
        assert "pathspec" in r.stderr, r.stderr

    def test_every_prompt_shows_the_runnable_form(self, tmp_path):
        """A prompt that names a marker has to show where it goes.

        All three arms are checked — review, parity, and the unresolved target —
        because the sentence was copied between them and a fix to one leaves the
        others saying the thing that fails.
        """
        repo = opted_in_repo(tmp_path / "prompts")
        (repo / "seal" / "parity.md").write_text(
            "| Original repo | org/legacy |\n", encoding="utf-8"
        )
        seen = []
        for cmd, session in (
            ("git commit -m x", "s1"),  # deny: both arms, question form
            ("git commit -m x", "s1"),  # ask: both arms, plain form
            ('git -C "$WT" commit -m x', "s2"),  # the unresolved target
        ):
            out = run_hook(
                "commit-review-gate.py", payload(cmd, repo) | {"session_id": session}
            )
            seen.append(
                json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
            )
        for reason in seen:
            assert ": '[no-" in reason, f"no runnable form in:\n{reason}"
            assert "as a BARE WORD" not in reason, (
                "the prompt still tells the user to type a pathspec"
            )
            # The SHAPE of every form a prompt prints, not just that one is
            # present. `": '[no-" in reason` is a prefix test, and it passes a
            # prompt advising `git commit … : '[no-review]'` -- the pathspec form
            # git rejects, which is the whole defect this file exists for.
            # Measured: that mutation passed the entire suite. The guard that used
            # to catch it was the cross-release text pin in
            # `test_the_same_root_forms_answer_what_the_release_did`, and that pin
            # was deliberately narrowed to the STATE half, so the option BODIES --
            # where these forms live -- had nothing looking at them.
            for form in re.findall(r"`([^`]*\[no-[a-z]+\][^`]*)`", reason):
                assert re.match(
                    r"^: (?:'\[no-[a-z]+\] ?'|'\[no-[a-z]+\]' ?)+; ", form
                ), f"a form git rejects reached a prompt: {form!r}"

    # --- the parity arm ----------------------------------------------------------

    def test_parity_repo_asks_when_code_commits_without_a_comparison(self, repo):
        parity_repo(repo)
        stage(repo, "service.py")
        cmd = parity_only("git commit -m x")
        out = run_hook("commit-review-gate.py", payload(cmd, repo))
        assert decision_of(out) == "deny"
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "[no-parity]" in reason
        assert "[no-review]" not in reason, (
            "the parity arm fired alone — naming the review marker sends the user "
            "to the one token that does not silence it"
        )

    def test_the_parity_arms_plain_prompt_names_its_own_marker(self, repo):
        """The closing sentence used to be hardcoded to `[no-review]`, so a commit
        stopped by the parity arm alone was told to re-issue with a token that
        changes nothing here."""
        parity_repo(repo)
        stage(repo, "service.py")
        cmd = parity_only("git commit -m x")
        run_hook("commit-review-gate.py", payload(cmd, repo))  # spends it
        out = run_hook("commit-review-gate.py", payload(cmd, repo))
        assert decision_of(out) == "ask"
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "[no-parity]" in reason and "[no-review]" not in reason

    def test_a_diff_git_could_not_take_is_asked_about_by_the_parity_arm(
        self, repo, tmp_path
    ):
        """S10 of work item 1791384157 (#868), the PreToolUse reading. Where `git
        diff` fails, the commit's paths are unknown, and a change git could not
        list is not a change confined to `docs/` and `seal/`, so the parity arm
        asks. Red at `5623d728`, where the failure read as an empty diff and the
        arm said nothing."""
        if os.name == "nt":
            pytest.skip("the shim is a POSIX shell script")
        parity_repo(repo)
        stage(repo, "service.py")
        path = a_git_whose_diff_fails(tmp_path)
        out = run_hook(
            "commit-review-gate.py",
            payload(parity_only("git commit -m x"), repo),
            env={"PATH": path},
        )
        assert decision_of(out) == "deny", out
        assert "[no-parity]" in out, out

    def test_parity_mark_matching_head_allows(self, repo):
        parity_repo(repo)
        stage(repo, "service.py")
        gd = git(repo, "rev-parse", "--absolute-git-dir").stdout.strip()
        head = git(repo, "rev-parse", "HEAD").stdout.strip()
        with open(os.path.join(gd, "specseal-parity"), "w", encoding="utf-8") as f:
            f.write(head)
        cmd = parity_only("git commit -m x")
        assert (
            decision_of(run_hook("commit-review-gate.py", payload(cmd, repo)))
            == "silent"
        )

    def test_parity_gate_ignores_document_only_commits(self, repo):
        # Asking on a docs-only commit trains people to click through the prompt.
        parity_repo(repo)
        (repo / "docs" / "policies").mkdir(parents=True, exist_ok=True)
        stage(repo, "docs/policies/note.md", "text\n")
        cmd = parity_only("git commit -m x")
        assert (
            decision_of(run_hook("commit-review-gate.py", payload(cmd, repo)))
            == "silent"
        )

    @pytest.mark.parametrize("path", ["docs/policies/note.md", "seal/ledger.md"])
    def test_a_document_only_commit_wakes_one_arm_and_not_two(self, repo, path):
        """In a migration repository the same commit wakes the review arm alone:
        the parity arm's silence on `docs/` and `seal/` holds, and the review
        arm's question does not borrow either half of it."""
        parity_repo(repo)
        (repo / path).parent.mkdir(parents=True, exist_ok=True)
        stage(repo, path, "text\n")
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        assert decision_of(out) == "deny"
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "[no-review]" in reason
        assert "[no-parity]" not in reason, (
            "the parity arm woke on a docs-only commit, so the question names a "
            "comparison nothing could have made"
        )

    def test_parity_gate_silent_without_the_declaration(self, repo):
        stage(repo, "service.py")
        assert (
            decision_of(
                run_hook("commit-review-gate.py", payload("git commit -m x", repo))
            )
            == "silent"
        )

    def test_no_parity_escape_is_visible_in_the_command(self, repo):
        parity_repo(repo)
        stage(repo, "service.py")
        assert (
            decision_of(
                run_hook(
                    "commit-review-gate.py",
                    payload(parity_only("git commit -m x [no-parity]"), repo),
                )
            )
            == "silent"
        )

    def test_parity_gate_sees_commits_that_never_touched_the_index(self, repo):
        """`-a` and a trailing pathspec both skip staging.

        The gate read only `git diff --cached`, so these two forms — the ones
        people type by hand — reported an empty change and the gate went silent
        on them."""
        parity_repo(repo)
        (repo / "f.txt").write_text(
            "one\ntwo\nfour\n", encoding="utf-8"
        )  # tracked, never staged
        for cmd in (
            "git commit -am x",
            "git commit -a -m x",
            "git commit -m x f.txt",
            "git commit -mfix f.txt",
            "git commit -m x -- f.txt",
        ):
            one = parity_only(cmd)
            assert fired(run_hook("commit-review-gate.py", payload(one, repo))), one

    def test_an_unstaged_document_change_still_does_not_ask(self, repo):
        """The `-a` fix must not turn every docs commit into a prompt."""
        parity_repo(repo)
        (repo / "docs").mkdir(exist_ok=True)
        (repo / "docs" / "note.md").write_text("text\n", encoding="utf-8")
        git(repo, "add", "docs/note.md")
        git(repo, "commit", "-qm", "docs")
        (repo / "docs" / "note.md").write_text("more text\n", encoding="utf-8")
        cmd = parity_only("git commit -am x")
        assert (
            decision_of(run_hook("commit-review-gate.py", payload(cmd, repo)))
            == "silent"
        )

    def test_declaring_the_migration_config_opts_into_the_review_arm_too(self, repo):
        """The two opt-ins stopped being independently declarable at 0.10.

        `docs/review-chain-spec.md` claimed a repo could have `.specseal/parity.md`
        and no `.specseal/`, which the path makes impossible. The claim survived
        because the pre-0.10 `docs/parity.md` could still produce that state, and
        the tests here used it. Removing that address is what made the claim
        visible; the document now says the arms are evaluated independently and
        declared together.
        """
        parity_repo(repo)
        stage(repo, "service.py")
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "specseal-reviewed" in reason and "specseal-parity" in reason

    def test_both_opt_ins_report_together(self, repo):
        parity_repo(repo)
        opt_in(repo)
        stage(repo, "service.py")
        out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
        assert decision_of(out) == "deny"
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        assert "specseal-reviewed" in reason and "specseal-parity" in reason, reason
        # Two axes waived independently, so two questions — but ONE call, because
        # a second call is a second interruption for a decision made at once.
        assert "BOTH questions in ONE call" in reason
        assert "[no-review]" in reason and "[no-parity]" in reason


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

    def test_repeated_chdirs_compose_the_way_git_resolves_them(self, tmp_path):
        """Measured against git 2.50: `git -C a -C b` lands in `a/b`, not `b`."""
        targets = gate.commit_targets(
            str(tmp_path), gate.commit_invocations("git -C a -C b commit -m x")[0]
        )
        assert [t for t, _ in targets] == [str(tmp_path / "a" / "b")]

    def test_each_repository_the_command_commits_to_is_judged(self, tmp_path):
        """One command can commit twice; the second target must not be lost."""
        targets = gate.commit_targets(
            str(tmp_path),
            gate.commit_invocations(
                f"git commit -m x && git -C {sh(tmp_path / 'o')} commit"
            )[0],
        )
        assert [t for t, _ in targets] == [str(tmp_path), str(tmp_path / "o")]

    def test_an_absolute_chdir_recovers_a_directory_the_reader_had_lost(self, tmp_path):
        """`-C` with an absolute path does not depend on where the shell is."""
        command = f'cd "$WT" && git -C {sh(tmp_path / "b")} commit -m x'
        found, clean = gate.commit_invocations(command, str(tmp_path))
        assert clean
        targets = gate.commit_targets(str(tmp_path), found)
        assert [str(t) for t, _ in targets] == [str(tmp_path / "b")]
        assert unreadable([t for t, _ in targets]) == [False]

    def test_the_helper_keeps_the_marker_out_of_the_git_command(self):
        """What makes the form work: the marker is never an argument to git."""
        form = gate.waiver_form(["[no-review]", "[no-parity]"])
        assert form.startswith(": '[no-review]' '[no-parity]';")
        assert form.index("[no-review]") < form.index(";"), (
            "a marker after the separator is an argument to whatever follows"
        )

    def test_the_worktree_guard_is_no_longer_load_bearing_for_this_gate(self, tmp_path):
        """The fail-open this file used to pin as a cost is gone, not documented.

        The gate reached `parse_git` and `apply_chdir` by loading
        `hooks/worktree-guard.py` from disk. That load could fail, and the gate
        kept running with no parser at all — which read as "every command is
        unparseable" and produced three wrong answers at once: an unreviewed
        commit aimed at an opted-in repository went silent, a sentence merely
        mentioning git and commit prompted, and `[no-review]` waived from inside
        the commit message through the substring fallback.

        The first of those is the same shape as issue #56 — the gate saying
        nothing for a reason that has nothing to do with review.

        `hooks/cmdline.py` now owns both functions and the guard only re-exports
        them, so this gate imports them by plain name and the guard is not in the
        path at all. Removing the load removed the cost; there was no reason to
        keep paying it to keep the note.
        """
        opted = make_repo(tmp_path / "opted-in", opted_in=True)
        plain = make_repo(tmp_path / "plain", opted_in=False)
        hooks = tmp_path / "hooks"
        shutil.copytree(Path(__file__).resolve().parent.parent / "hooks", hooks)

        def gate(command, cwd):
            r = subprocess.run(
                [sys.executable, str(hooks / "commit-review-gate.py")],
                input=json.dumps(
                    {
                        "tool_name": "Bash",
                        "tool_input": {"command": command},
                        "cwd": str(cwd),
                    }
                ),
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
            )
            return decision_of(r.stdout)

        aimed_at_opted_in = f"git -C {sh(opted)} commit -m x"
        prose = 'echo "remember to git commit later"'
        in_message = "git commit -m 'fix [no-review] later'"

        before = (
            gate(aimed_at_opted_in, plain),
            gate(prose, opted),
            gate(in_message, opted),
        )
        assert before == ("ask", "silent", "ask"), before

        for broken in ("def broken(:\n", None):
            if broken is None:
                (hooks / "worktree-guard.py").unlink()
            else:
                (hooks / "worktree-guard.py").write_text(broken, encoding="utf-8")
            after = (
                gate(aimed_at_opted_in, plain),
                gate(prose, opted),
                gate(in_message, opted),
            )
            assert after == before, (
                f"a broken worktree guard changed this gate's verdicts: {after}"
            )

    def test_the_gate_does_not_load_a_sibling_hook_at_all(self, tmp_path):
        """The mechanism, not just its effect. A later change could reinstate the
        load and leave the case above green by re-exporting the same functions —
        until the day the sibling breaks."""
        source = (
            Path(__file__).resolve().parent.parent / "hooks" / "commit-review-gate.py"
            # Named, because this file's own subject is a tree that does not assume
            # the ambient codepage: the gate's source carries em dashes, and reading it
            # without saying UTF-8 made this case fail on a cp949 console for a reason
            # that had nothing to do with what it asserts.
        ).read_text(encoding="utf-8")
        assert "from cmdline import" in source
        for loader in ("_sibling(", "spec_from_file_location", "importlib"):
            assert loader not in source, (
                f"the gate loads a hook from disk again: {loader}"
            )

    def test_a_broken_command_reader_leaves_no_verdict_rather_than_a_wrong_one(
        self, tmp_path
    ):
        """`cmdline.py` is imported by name, so a broken one is an ImportError at
        module load and the gate never runs.

        `hooks/dispatch.py` turns that into exit 0 and no output for the call,
        which reads exactly like an allow there. Since #28 the failure is written
        down and said at the end of the turn, and the call's own stdout is still
        what this case asserts. What changed here is that it is now the ONLY way
        the parsing can go missing, instead of one of two.
        A gate that did not load has no verdict; a gate that loaded with no parser
        had three wrong ones.
        """
        here = make_repo(tmp_path / "opted-in", opted_in=True)
        hooks = tmp_path / "hooks"
        shutil.copytree(Path(__file__).resolve().parent.parent / "hooks", hooks)
        payload = json.dumps(
            {
                "tool_name": "Bash",
                "tool_input": {"command": "git commit -m 'change'"},
                "cwd": str(here),
            }
        )

        def dispatch():
            r = subprocess.run(
                [sys.executable, str(hooks / "dispatch.py"), "pre-bash"],
                input=payload,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
            )
            return decision_of(r.stdout)

        assert dispatch() == "ask", "the fixture itself has to reach the gate"
        (hooks / "cmdline.py").write_text("def broken(:\n", encoding="utf-8")
        assert dispatch() == "silent", (
            "recorded, not endorsed: dispatch swallows the ImportError and the "
            "absence of a gate reads as an allow"
        )


test_census = census_case(TARGET)
