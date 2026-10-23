"""`hooks/worktree-guard.py`, one class per function.

Rebuilt from the code by #942's phase 5. The readings of a command, the lease
and transcript readers, the session count and the texts run in the process
with no shell. `main` runs in the process over a world built once for the
module: a clean repository, a dirty one, one holding a force-added ignored
path, a dirty second clone `W`, a clean second clone `V` and a directory
outside any repository. The session count is a stub, and the person's
`automation` press is a transcript each case writes under its own projects
root. No case writes into the world but the guard's choice marker and the
consent record, both keyed by a session id each case makes its own, so the
session id is the reset. The cases that run git in a repository they change
take a copy of their own.
"""

import contextlib
import functools
import io
import json
import os
import shlex
import shutil
import socket
import subprocess
import sys
import time
import types
import uuid

import pytest
from conftest import (
    ask_entries,
    census_case,
    git,
    git_out,
    load_hook_module,
    shell_probe,
    write_transcript,
)

TARGET = "hooks/worktree-guard.py"

wg = load_hook_module("worktree-guard.py", "wg_under_test")

ACTIVE = [(111, "/tree", 1.0, 0.5, "VS Code")]
IDLE = [(222, "/tree", 400.0, 90.0, "Terminal")]
SINGLE = ([], [], True)
BUSY = (ACTIVE, [], True)
QUIET = ([], IDLE, True)
BLIND = ([], [], False)

STOP = "does not know to leave the branch where it is"


@pytest.fixture(scope="module")
def world(tmp_path_factory, _repo_template):
    """The trees `main` judges, built once. Each repository is the session
    template's: `f.txt` committed and a branch `feature/x`."""
    base = tmp_path_factory.mktemp("guard-world")

    def copy(name, changed=False):
        d = base / name
        shutil.copytree(_repo_template, d)
        (d / "sub").mkdir()
        if changed:
            (d / "f.txt").write_text("changed\n", encoding="utf-8")
        return d

    phantom = copy("phantom", changed=True)
    (phantom / ".gitignore").write_text("ign.txt\n", encoding="utf-8")
    (phantom / "ign.txt").write_text("x\n", encoding="utf-8")
    git(phantom, "add", "-f", "ign.txt")
    outside = base / "outside"
    outside.mkdir()
    return types.SimpleNamespace(
        base=base,
        clean=copy("clean"),
        dirty=copy("dirty", changed=True),
        phantom=phantom,
        W=copy("W", changed=True),
        V=copy("V"),
        outside=outside,
    )


# Which repository a directory is in, asked of git once per directory: the
# guard asks it of the same few directories hundreds of times a run, and a
# directory's answer does not change within one.
_ASKED = {
    (wg, "repo_paths"): functools.lru_cache(maxsize=None)(wg.repo_paths),
    (wg, "git_dir"): functools.lru_cache(maxsize=None)(wg.git_dir),
    (wg.worktree_consent.optin, "repo_root"): functools.lru_cache(maxsize=None)(
        wg.worktree_consent.optin.repo_root
    ),
}


@pytest.fixture(autouse=True)
def _git_asked_once_per_directory(monkeypatch):
    for (module, name), cached in _ASKED.items():
        monkeypatch.setattr(module, name, cached)


class Guard:
    """`main` for one payload: the session count stubbed, the stream read."""

    def __init__(self, monkeypatch, tmp_path):
        self.mp = monkeypatch
        self.tmp = tmp_path
        self.sid = f"s-{uuid.uuid4().hex[:12]}"

    def __call__(
        self,
        command,
        cwd,
        sessions=SINGLE,
        sid=None,
        tool="Bash",
        tool_input=None,
        transcript=None,
    ):
        state = sessions if callable(sessions) else (lambda top, own="": sessions)
        self.mp.setattr(wg, "sessions_in_tree", state)
        payload = {
            "tool_name": tool,
            "session_id": self.sid if sid is None else sid,
            "tool_input": {"command": command} if tool_input is None else tool_input,
            "cwd": str(cwd),
        }
        if transcript is not None:
            payload["transcript_path"] = str(transcript)
        self.mp.setattr(wg, "load_input", lambda: payload)
        return said(wg.main)

    def press(self, repo, sid=None, answer="automation (Recommended)"):
        """The person's routing answer for REPO in this session's transcript."""
        root = self.tmp / "projects"
        write_transcript(root, sid or self.sid, ask_entries(repo, answer=answer))
        self.mp.setattr(wg.worktree_consent, "PROJECTS_ROOT", str(root))
        return root

    def grant(self, repo, sid=None):
        """The consent record a creation that ran leaves, written by hand."""
        path = wg.worktree_consent.consent_path(str(repo), sid or self.sid)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").close()
        return path

    def lang(self, lang):
        self.mp.setattr(wg, "LANG", lang)


@pytest.fixture
def guard(monkeypatch, tmp_path):
    return Guard(monkeypatch, tmp_path)


def said(call, *args, **kwargs):
    """(decision, reason) CALL printed, or ("silent", "") where it printed
    nothing."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        try:
            call(*args, **kwargs)
        except SystemExit:
            pass
    text = out.getvalue().strip()
    if not text:
        return "silent", ""
    d = json.loads(text)["hookSpecificOutput"]
    return d["permissionDecision"], d["permissionDecisionReason"]


def by_tree(name, state):
    """A session count giving STATE in the tree named NAME, one stream
    elsewhere."""
    return lambda top, own="": state if os.path.basename(top) == name else SINGLE


def first_shape(command):
    """The first shape `main` would act on in COMMAND's own segments: a
    switch, a creation or an unrecognised shape, None where every segment is
    listed or no git."""
    segments, _clean = wg.split_command(command)
    for tokens in segments:
        got = wg.shape_of(tokens)
        if got not in (None, "listed"):
            return got
    return None


# --- the module ---------------------------------------------------------------


class Test_module:
    def test_accepts_the_language_and_the_idle_window_the_environment_names(
        self, monkeypatch
    ):
        monkeypatch.setenv("SPECSEAL_LANG", "ko")
        monkeypatch.setenv("LANG", "en_US.UTF-8")
        assert wg._lang() == "ko"
        monkeypatch.delenv("SPECSEAL_LANG")
        monkeypatch.setenv("LC_ALL", "ko_KR.UTF-8")
        assert wg._lang() == "ko"
        monkeypatch.delenv("LC_ALL")
        assert wg._lang() == "en"
        monkeypatch.setenv("WORKTREE_GUARD_IDLE_MIN", "7")
        assert wg._idle_min() == 7

    @pytest.mark.parametrize("value", ["0", "-3", "five"])
    def test_refuses_an_idle_window_that_is_not_a_positive_number(
        self, monkeypatch, value
    ):
        monkeypatch.setenv("WORKTREE_GUARD_IDLE_MIN", value)
        assert wg._idle_min() == 5


# --- reading the command --------------------------------------------------------


class Test_split_command:
    def test_accepts_a_comment_dropped_and_a_hash_inside_a_word_kept(self):
        assert wg.split_command("git switch feat#1")[0] == [["git", "switch", "feat#1"]]
        segments, clean = wg.split_command("git -C repo#2 switch b")
        assert clean and wg.parse_git(segments[0])[2] == ["repo#2"]
        assert wg.split_command("git switch b  # note")[0] == [["git", "switch", "b"]]
        assert wg.split_command("git worktree add ../wt f  # don't forget")[1] is True

    def test_refuses_a_quoted_separator_and_a_heredoc_body_as_segments(self):
        assert wg.split_command('echo "step 1; git switch feature/x"')[0] == [
            ["echo", "step 1; git switch feature/x"]
        ]
        body = "cat > n <<'EOF'\ngit switch x\nEOF"
        assert ["git", "switch", "x"] not in wg.split_command(body)[0]


class Test_parses_cleanly:
    def test_accepts_a_command_whose_comment_closes_its_quotes(self):
        assert wg.parses_cleanly("git worktree add ../wt f  # [worktree-ok]")

    def test_refuses_an_apostrophe_in_a_comment_as_written(self):
        assert wg.parses_cleanly("git worktree add ../wt f  # don't forget") is False


class Test_has_token:
    @pytest.mark.parametrize(
        "command",
        [
            "git switch x  # [shared-tree-ok]",
            "git switch x && echo done  # [shared-tree-ok]",
            "git switch x  # [shared-tree-ok] but don't",
        ],
    )
    def test_accepts_the_token_as_a_bare_word(self, command):
        assert wg.has_token(command, "[shared-tree-ok]")

    @pytest.mark.parametrize(
        "command",
        [
            "git switch x && echo 'we documented [shared-tree-ok] today'",
            'git switch x && echo "we agreed on [shared-tree-ok] yesterday',
            "cat <<EOF\n[shared-tree-ok]\nEOF",
            "git switch x  # \"don't forget [shared-tree-ok]",
        ],
        ids=["quoted-prose", "unclosed-quote", "heredoc-body", "after-the-quote"],
    )
    def test_refuses_the_token_as_prose(self, command):
        assert "[shared-tree-ok]" in command
        assert not wg.has_token(command, "[shared-tree-ok]")

    def test_refuses_every_token_where_the_reader_did_not_load(self, monkeypatch):
        monkeypatch.setattr(wg, "tokens", None)
        assert not wg.has_token("git switch x  # [shared-tree-ok]", "[shared-tree-ok]")


class Test_walk_command:
    def test_accepts_a_cd_as_moving_the_segment_after_it(self):
        walked = wg.walk_command("cd sub && git switch x", "/base")
        # Built as `hooks/cmdline_base.py#apply_chdir` builds it, joined and
        # then normalised, which on Windows turns the leading `/` into `\`.
        landed = os.path.normpath(os.path.join("/base", "sub"))
        assert walked[1] == (["git", "switch", "x"], (landed,))

    def test_refuses_a_heredoc_line_as_a_segment(self):
        walked = wg.walk_command("cat > n <<'EOF'\ngit switch x\nEOF", "/base")
        assert [tokens for tokens, _ in walked] == [["cat", ">", "n", "<<EOF"]]


class Test_only_creates_a_worktree:
    @pytest.mark.parametrize(
        "command",
        [
            "git worktree add ../wt f",
            "git worktree add ../wt f &",
            "'git' worktree add ../wt f",
            "git -C /elsewhere worktree add ../wt f",
        ],
    )
    def test_accepts_a_creation_and_nothing_else(self, command):
        assert wg.only_creates_a_worktree(command, "/base")

    @pytest.mark.parametrize(
        "command",
        [
            "",
            "git status",
            "git worktree list",
            "git worktree add ../wt f && echo done",
            "git worktree add ../wt f & rm -rf /tmp/x",
            "sudo git worktree add ../wt f",
            "./git worktree add ../wt f",
            "/usr/bin/git worktree add ../wt f",
            "git worktree add ../wt f $(touch /tmp/marker)",
            "git worktree add ../wt f > /tmp/clobber",
            "git worktree add ../wt f <(touch /tmp/marker)",
            "(git worktree add ../wt f)",
            "git worktree add ../wt f  # don't",
        ],
    )
    def test_refuses_a_command_that_does_anything_else(self, command):
        assert not wg.only_creates_a_worktree(command, "/base")


# --- who else is in the tree --------------------------------------------------


class Test_lease_owner_alive:
    def test_accepts_a_running_process(self):
        assert wg.lease_owner_alive(os.getpid()) is True

    def test_refuses_a_process_that_has_exited(self):
        child = subprocess.Popen([sys.executable, "-c", ""])
        child.wait()
        assert wg.lease_owner_alive(child.pid) is False


def lease(d, name, record=None, age_min=0.0):
    """A lease file NAME in D holding RECORD (JSON) or a bare timestamp,
    AGE_MIN minutes old."""
    path = d / name
    path.write_text("1" if record is None else json.dumps(record), encoding="utf-8")
    then = time.time() - age_min * 60
    os.utime(path, (then, then))
    return path


@pytest.fixture
def leases(monkeypatch, tmp_path):
    """A lease directory the readers are pointed at, and owners by pid."""
    d = tmp_path / "leases"
    d.mkdir()
    monkeypatch.setattr(wg, "lease_dir", lambda top: str(d))
    alive = {}
    monkeypatch.setattr(wg, "lease_owner_alive", lambda pid: alive.get(pid))
    return d, alive


class Test_fresh_leases:
    def test_accepts_a_live_owner_another_host_and_a_quiet_owner(self, leases):
        d, alive = leases
        alive.update({10: True, 11: True})
        here = socket.gethostname()
        lease(d, "aaaaaaaa-live", {"pid": 10, "host": here})
        lease(d, "bbbbbbbb-far", {"pid": 99, "host": "elsewhere.example.com"})
        lease(d, "cccccccc-quiet", {"pid": 11, "host": here}, age_min=60)
        live, unattributable = wg.fresh_leases("/t", "me")
        assert sorted(e[1] for e in live) == [
            "/t  [lease: aaaaaaaa… pid 10]",
            "/t  [lease: bbbbbbbb… on elsewhere.example.com]",
        ]
        assert [e[1] for e in unattributable] == [
            "/t  [lease: cccccccc… pid 11 alive, quiet]"
        ]

    def test_refuses_its_own_a_stale_a_dead_and_a_scanned_lease(self, leases):
        d, alive = leases
        alive.update({12: False, 13: True})
        here = socket.gethostname()
        lease(d, "me")
        lease(d, "old-session", age_min=60)
        lease(d, "dead-owner", {"pid": 12, "host": here})
        lease(d, "scanned", {"pid": 13, "host": here}, age_min=60)
        assert wg.fresh_leases("/t", "me", frozenset({13})) == ([], [])
        lease(d, "ownerless")
        live, unattributable = wg.fresh_leases("/t", "me", frozenset({13}))
        assert live == [] and [e[1] for e in unattributable] == [
            "/t  [lease: ownerles… owner unknown]"
        ]


class Test_dead_session_ids:
    def test_accepts_a_lease_whose_owner_on_this_host_is_gone(self, leases):
        d, alive = leases
        alive[20] = False
        lease(d, "gone", {"pid": 20, "host": socket.gethostname()})
        assert wg.dead_session_ids(str(d)) == frozenset({"gone"})

    def test_refuses_every_lease_that_proves_nothing(self, leases, monkeypatch):
        d, alive = leases
        alive.update({21: None, 22: True})
        here = socket.gethostname()
        lease(d, "unprobeable", {"pid": 21, "host": here})
        lease(d, "running", {"pid": 22, "host": here})
        lease(d, "far", {"pid": 23, "host": "elsewhere.example.com"})
        lease(d, "bare")
        (d / "broken").write_text("{", encoding="utf-8")
        assert wg.dead_session_ids(str(d)) == frozenset()
        monkeypatch.setattr(wg, "lease_dir", lambda top: None)
        assert wg.dead_session_ids(str(d)) == frozenset()


def transcript_line(kind, minutes_ago=0.0):
    stamp = time.strftime(
        "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - minutes_ago * 60)
    )
    return json.dumps({"type": kind, "timestamp": stamp})


@pytest.fixture
def project(monkeypatch, tmp_path):
    """`~/.claude/projects/<slug of /work>` under a home this case owns."""
    home = tmp_path / "home"
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("USERPROFILE", str(home))
    d = home / ".claude" / "projects" / wg.project_slug("/work")
    d.mkdir(parents=True)
    return d


class Test_last_active_event_epoch:
    def test_accepts_the_newest_active_event_past_a_line_separator(self, tmp_path):
        path = tmp_path / "t.jsonl"
        late = json.loads(transcript_line("assistant", 2))
        late["message"] = "one" + chr(0x2028) + "two"
        path.write_text(
            transcript_line("user", 30)
            + "\n"
            + json.dumps(late, ensure_ascii=False)
            + "\n"
            + transcript_line("attachment", 0)
            + "\n",
            encoding="utf-8",
        )
        got = wg.last_active_event_epoch(str(path))
        assert abs(got - (time.time() - 120)) < 5

    def test_refuses_passive_appends_and_an_unreadable_file(self, tmp_path):
        path = tmp_path / "t.jsonl"
        path.write_text(transcript_line("attachment") + "\n{\n", encoding="utf-8")
        assert wg.last_active_event_epoch(str(path)) is None
        assert wg.last_active_event_epoch(str(tmp_path / "none.jsonl")) is None


class Test_transcript_idle_minutes:
    def test_accepts_another_sessions_write_and_a_background_agents(self, project):
        (project / "other.jsonl").write_text(
            transcript_line("user", 30) + "\n", encoding="utf-8"
        )
        os.utime(project / "other.jsonl", (time.time() - 1800,) * 2)
        assert 29 < wg.transcript_idle_minutes("/work", "me") < 31
        agent = project / "third" / "subagents" / "agent-a.jsonl"
        agent.parent.mkdir(parents=True)
        agent.write_text(transcript_line("tool_use") + "\n", encoding="utf-8")
        assert wg.transcript_idle_minutes("/work", "me") < 1

    def test_refuses_its_own_a_dead_sessions_and_a_passive_write(self, project):
        for name in ("me", "gone"):
            (project / f"{name}.jsonl").write_text(
                transcript_line("user") + "\n", encoding="utf-8"
            )
        (project / "gone").mkdir()
        (project / "gone" / "a.jsonl").write_text(
            transcript_line("user") + "\n", encoding="utf-8"
        )
        (project / "idle.jsonl").write_text(
            transcript_line("attachment") + "\n", encoding="utf-8"
        )
        assert wg.transcript_idle_minutes("/work", "me", frozenset({"gone"})) is None
        assert wg.transcript_idle_minutes("/nowhere", "me") is None


@pytest.fixture
def scan(monkeypatch):
    """`sessions_in_tree`'s readers stubbed: `ps` lists PIDS as claude, this
    process's ancestors are MINE, and each pid's cwd and signals are given."""
    seen = types.SimpleNamespace(
        top="/t",
        pids=[],
        mine={os.getpid()},
        cwd={},
        tty={},
        transcript={},
        top_idle=None,
    )

    def ps(args, **kwargs):
        rows = "".join(f"{p} claude\n" for p in seen.pids)
        return types.SimpleNamespace(stdout=rows + "77 zsh\n")

    monkeypatch.setattr(wg, "subprocess", types.SimpleNamespace(run=ps))
    monkeypatch.setattr(wg, "ancestors", lambda pid: set(seen.mine))
    monkeypatch.setattr(wg, "proc_cwd", lambda p: seen.cwd.get(p))
    monkeypatch.setattr(wg, "tty_idle_minutes", lambda p: seen.tty.get(p))
    monkeypatch.setattr(wg, "host_app", lambda p: None)
    monkeypatch.setattr(wg, "dead_session_ids", lambda top: frozenset())
    monkeypatch.setattr(wg, "fresh_leases", lambda top, own, scanned: ([], []))

    def transcripts(d, own, dead=frozenset()):
        return seen.top_idle if d == seen.top else seen.transcript.get(d)

    monkeypatch.setattr(wg, "transcript_idle_minutes", transcripts)
    return seen


class Test_sessions_in_tree:
    def test_accepts_an_active_and_an_idle_session_inside_the_tree(self, scan):
        sub = os.path.join(scan.top, "sub")
        scan.pids = [1, 20, 21]
        scan.mine = {os.getpid(), 1}
        scan.cwd = {20: scan.top, 21: sub}
        scan.tty = {20: 1.0, 21: 99.0}
        scan.transcript = {sub: 99.0}
        active, idle, reliable = wg.sessions_in_tree(scan.top, "me")
        assert reliable
        assert [e[0] for e in active] == [20] and [e[0] for e in idle] == [21]

    def test_refuses_a_sibling_tree_and_reads_no_signal_as_active(self, scan):
        scan.pids = [1, 30, 31]
        scan.mine = {os.getpid(), 1}
        scan.cwd = {30: scan.top + "2", 31: scan.top}
        active, idle, reliable = wg.sessions_in_tree(scan.top, "me")
        assert reliable and [e[0] for e in active] == [31] and idle == []

    def test_refuses_to_count_where_its_own_session_is_invisible(self, scan):
        scan.pids = [40]
        scan.cwd = {40: scan.top}
        assert wg.sessions_in_tree(scan.top, "me") == ([], [], False)
        scan.pids = []
        assert wg.sessions_in_tree(scan.top, "me") == ([], [], False)

    def test_accepts_a_fresh_transcript_no_process_holds_as_active(self, scan):
        scan.pids = [1]
        scan.mine = {os.getpid(), 1}
        scan.top_idle = 1.0
        assert wg.sessions_in_tree(scan.top, "me") == (
            [(None, scan.top, None, 1.0, None)],
            [],
            True,
        )


# --- what a stop prints --------------------------------------------------------

LEASED = (
    None,
    "/x/feature  [lease: 5924d73a… pid 87946 alive, quiet]",
    None,
    282.0,
    None,
)
WRITING = (None, "/x/feature", None, 1.0, None)
CLAUSES = ("working on this tree right now", "지금 이 트리에서 작업 중")


class Test_fmt_sessions:
    def test_accepts_a_pid_with_its_two_signals_and_its_host(self, guard):
        assert wg.fmt_sessions(IDLE) == (
            "    pid 222 (Terminal terminal)  /tree\n"
            "        terminal in/out 6.7h ago · transcript activity 1.5h ago"
        )
        guard.lang("ko")
        assert wg.fmt_sessions(IDLE) == (
            "    pid 222 (Terminal 터미널)  /tree\n"
            "        터미널 입력/출력 6.7시간 전 · 작업 기록(트랜스크립트) 1.5시간 전"
        )
        assert wg.fmt_sessions([(5, "/tree", None, 60.0, None)]).endswith(
            "터미널 입력/출력 확인 불가 · 작업 기록(트랜스크립트) 1.0시간 전"
        )

    def test_refuses_to_say_an_unidentified_session_is_working(self, guard):
        for lang, leased, writing in (
            ("en", "lease declaration 4.7h ago", "transcript activity 1m ago"),
            ("ko", "lease 선언 4.7시간 전", "작업 기록(트랜스크립트) 1분 전"),
        ):
            guard.lang(lang)
            text = wg.fmt_sessions([LEASED, WRITING])
            assert f"        {leased}" in text.splitlines(), text
            assert f"        {writing}" in text.splitlines(), text
            assert not any(clause in text for clause in CLAUSES)


class Test_tracked_changes:
    def test_accepts_a_modified_tracked_file(self, world):
        assert wg.tracked_changes(str(world.dirty)) == [(" M", "f.txt")]

    def test_refuses_a_clean_tree_and_a_directory_outside_git(self, world):
        assert wg.tracked_changes(str(world.clean)) == []
        assert wg.tracked_changes(str(world.outside)) == []


class Test_phantom_entries:
    def test_accepts_an_index_only_and_a_force_added_ignored_path(self, world):
        entries = wg.tracked_changes(str(world.phantom))
        assert wg.phantom_entries(entries, str(world.phantom)) == [
            ("ign.txt", "gitignored path force-staged into the index")
        ]
        assert wg.phantom_entries([("AD", "x")], str(world.phantom)) == [
            ("x", "exists only in the index (added, then deleted in the worktree)")
        ]

    def test_refuses_a_change_visible_in_the_working_tree(self, world):
        assert wg.phantom_entries([(" M", "f.txt")], str(world.phantom)) == []


class Test_repo_paths:
    def test_accepts_a_subdirectory_as_its_tree(self, world):
        top = os.path.normpath(git_out(world.clean, "rev-parse", "--show-toplevel"))
        assert wg.repo_paths(str(world.clean / "sub")) == (
            top,
            os.path.join(os.path.dirname(top), "clean-worktrees"),
        )

    def test_refuses_a_directory_outside_any_repository(self, world):
        assert wg.repo_paths(str(world.outside)) == ("", "../<repo>-worktrees")


class Test_git_at:
    def test_accepts_the_bare_word_where_the_shell_stands_in_the_tree(self, world):
        top = wg.repo_paths(str(world.clean))[0]
        assert wg.git_at(top, str(world.clean / "sub")) == "git"

    def test_refuses_the_bare_word_where_the_shell_stands_elsewhere(self, world):
        top = wg.repo_paths(str(world.clean))[0]
        assert wg.git_at(top, str(world.outside)) == f"git -C {shlex.quote(top)}"
        assert wg.git_at(top, "") == f"git -C {shlex.quote(top)}"


class Test_already_asked:
    def test_accepts_the_first_question_and_records_it(self, world, guard):
        assert wg.already_asked(str(world.clean), guard.sid, "switch") is False
        marker = world.clean / ".git" / wg.CHOICE_DIR / "switch" / guard.sid
        assert marker.is_file()
        assert wg.already_asked(str(world.clean), guard.sid, "switch") is True
        assert wg.already_asked(str(world.clean), guard.sid, "create") is False

    def test_refuses_to_write_outside_the_git_dir_or_to_ask_twice(
        self, world, guard, monkeypatch, tmp_path
    ):
        escaped = f"../../{guard.sid}"
        assert wg.already_asked(str(world.clean), escaped, "switch") is False
        assert (world.clean / ".git" / wg.CHOICE_DIR / "switch" / guard.sid).is_file()
        assert not (world.base / guard.sid).exists()
        for session in ("", ".", ".."):
            assert wg.already_asked(str(world.clean), session, "switch") is True
        (tmp_path / wg.CHOICE_DIR).write_text("not a directory", encoding="utf-8")
        monkeypatch.setattr(wg, "git_dir", lambda cwd: str(tmp_path))
        assert wg.already_asked("/t", guard.sid, "switch") is True


class Test_choose:
    def args(self, world, sid, **kwargs):
        return dict(
            top=str(world.clean),
            session_id=sid,
            scope="switch",
            situation="the situation\n",
            question="which way?",
            options=(("1. one", "the first"), ("2. two", "the second")),
            fallback="the fallback",
            **kwargs,
        )

    def test_accepts_one_deny_with_the_options_then_the_fallback(self, world, guard):
        ran = []
        args = self.args(world, guard.sid, before_ask=lambda: ran.append(1))
        assert said(wg.choose, **args) == (
            "deny",
            "the situation\n\nDo not choose for the user. Ask with the "
            "AskUserQuestion tool, offering exactly these two options:\n\n"
            "  which way?\n    1. one — the first\n    2. two — the second\n\n"
            "Then run what they picked. Re-issuing this command before they "
            "answer reaches the ordinary confirmation prompt instead.",
        )
        assert ran == []
        assert said(wg.choose, **args) == ("ask", "the situation\nthe fallback")
        assert ran == [1]

    def test_refuses_to_ask_a_person_under_the_press_or_with_no_session(
        self, world, guard
    ):
        ran = []
        args = self.args(
            world,
            guard.sid,
            before_ask=lambda: ran.append(1),
            pressed=True,
            unattended="nobody is there",
        )
        for _attempt in (1, 2):
            assert said(wg.choose, **args) == (
                "deny",
                "the situation\n\nnobody is there",
            )
        assert ran == []
        assert not (
            world.clean / ".git" / wg.CHOICE_DIR / "switch" / guard.sid
        ).exists()
        assert said(wg.choose, **self.args(world, "")) == (
            "ask",
            "the situation\nthe fallback",
        )


# --- the shapes -------------------------------------------------------------------

SHAPES = {
    "git switch feature/x": "switch",
    "git switch -": "switch",
    "VAR=1 git switch feature/x": "switch",
    "command git switch feature/x": "switch",
    "git -C 'my repo' switch b  # don't": "switch",
    "'git' switch main  # don't": "switch",
    "git switch feature/x  # don't ask": "switch",
    "git worktree add ../wt feature/x": "creation",
    "git worktree add ../wt f  # user's call": "creation",
    "git worktree list": None,
    "git worktree remove ../wt": None,
    "git status": None,
    "git checkout -- f.txt": None,
    "git checkout feature/x -- f.txt": None,
    "git rebase main": None,
    "git rebase --root": None,
    "git rebase --ro": None,
    "git rebase --r feature/x": None,
    "git rebase --end-of-options --ro": None,
    "git stash": None,
    "echo git switch feature/x": None,
    "echo don't switch feature/x": None,
    'git commit -m "see README; git worktree add ../wt f"': None,
    'echo "a; git switch feature/x; b"': None,
    "git checkout -b feature/y": "unrecognised",
    "git checkout f.txt": "unrecognised",
    "git checkout feature/x --": "unrecognised",
    "git checkout feature/x -- >/dev/null": "unrecognised",
    "git rebase main feature/x": "unrecognised",
    "git rebase --root feature/x": "unrecognised",
    "git rebase --ro feature/x": "unrecognised",
    "git rebase - feature/x": "unrecognised",
    "git rebase -- main -x": "unrecognised",
    "git rebase --end-of-options main -x": "unrecognised",
    "git rebase --root>/dev/null feature/x": "unrecognised",
    "git stash branch y": "unrecognised",
    "git worktree 2>/dev/null add ../wt b": "unrecognised",
    "git 2>/dev/null status": "unrecognised",
    "git update-ref refs/heads/y HEAD": "unrecognised",
    "sh -c 'git switch x'": "unrecognised",
    'eval "git switch x"': "unrecognised",
    "2>/dev/null git switch x": "unrecognised",
    "noglob git switch x": "unrecognised",
    "git rebase {main,feature/x}": None,
    "git stash {branch,} y": None,
}


# --- the trees a stop reads -------------------------------------------------------


class Test_tree_matters:
    def test_accepts_a_tree_with_sessions_or_changes(self, world, monkeypatch):
        counted = []
        monkeypatch.setattr(
            wg, "sessions_in_tree", lambda top, own="": counted.append(top) or QUIET
        )
        top = str(world.dirty)
        seen = {}
        assert wg.tree_matters(top, "me", top, seen) == (True, [], IDLE, True, None)
        assert wg.tree_matters(top, "me", top, seen)[0] and counted == [top]
        monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": SINGLE)
        assert wg.tree_matters(top, "me", top) == (
            True,
            [],
            [],
            True,
            [(" M", "f.txt")],
        )
        monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": BLIND)
        assert wg.tree_matters(str(world.clean), "me", str(world.clean))[0]

    def test_refuses_a_clean_tree_nobody_else_is_in(self, world, monkeypatch):
        monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": SINGLE)
        top = str(world.clean)
        assert wg.tree_matters(top, "me", top) == (False, [], [], True, [])


class Test_automation_pressed:
    def test_accepts_the_press_given_in_the_sessions_clone(self, world, guard):
        guard.press(world.clean)
        assert wg.automation_pressed(str(world.clean), guard.sid, "") is True

    def test_refuses_every_way_of_not_reading_the_press(
        self, world, guard, monkeypatch
    ):
        guard.press(world.clean, answer="per axis")
        assert wg.automation_pressed(str(world.clean), guard.sid, "") is False
        guard.press(world.clean)
        assert wg.automation_pressed("", guard.sid, "") is False
        assert wg.automation_pressed(str(world.clean), "", "") is False

        def boom(*_a, **_k):
            raise RuntimeError("a shape nobody measured")

        monkeypatch.setattr(wg.worktree_consent, "automation_answered", boom)
        assert wg.automation_pressed(str(world.clean), guard.sid, "") is False


class Test_stop_unrecognised:
    def findings(self, n):
        return [wg.Finding("checkout", f"git checkout b{i}") for i in range(n)]

    def test_accepts_an_ask_naming_each_shape_once_and_counting_the_rest(self):
        ran = []
        changes = ("/t", ([], [], True, [(" M", "f.txt")]))
        decision, reason = said(
            wg.stop_unrecognised,
            self.findings(6) + self.findings(1),
            [changes],
            False,
            before_ask=lambda: ran.append(1),
        )
        assert decision == "ask" and ran == [1]
        assert reason.count("`git checkout b0`") == 1
        assert "`git checkout b4`" in reason and "`git checkout b5`" not in reason
        assert "  · and 1 more" in reason.splitlines()
        assert reason.endswith(
            "Approve to run it as written, or decline and re-issue it in a plain "
            "spelling."
        )

    def test_refuses_an_ask_beside_a_switch_an_active_tree_or_the_press(self):
        ran = []
        quiet = ("/q", ([], IDLE, True, None))
        busy = ("/b", (ACTIVE, [], True, None))
        for trees, pressed, switch_on_line in (
            ([quiet], False, True),
            ([quiet, busy], False, False),
            ([quiet], True, False),
        ):
            decision, reason = said(
                wg.stop_unrecognised,
                self.findings(1),
                trees,
                pressed,
                before_ask=lambda: ran.append(1),
                switch_on_line=switch_on_line,
            )
            assert decision == "deny", (trees, pressed, switch_on_line)
            assert ("Run the `git switch` as a command of its own" in reason) is (
                switch_on_line
            )
            if busy in trees:
                assert "actively working here" in reason
                assert "none of them can be shown" not in reason
        assert ran == []


# --- the creation ladder ------------------------------------------------------------


class Test_guard_worktree_creation:
    def test_accepts_consent_as_an_allow_or_a_silence(self, world, guard, monkeypatch):
        top = str(world.clean)
        monkeypatch.setattr(wg.worktree_consent, "consent", lambda *a: "record")
        decision, reason = said(
            wg.guard_worktree_creation, top, top, "ORIGIN", False, consented="allow"
        )
        assert decision == "allow" and reason.startswith(
            "ORIGIN\nA worktree creation already ran in this repository"
        )
        monkeypatch.setattr(wg.worktree_consent, "consent", lambda *a: "answer")
        decision, reason = said(
            wg.guard_worktree_creation, top, top, "ORIGIN", False, consented="allow"
        )
        assert reason.startswith("ORIGIN\nThe user pressed `automation`")
        assert said(
            wg.guard_worktree_creation, top, top, "ORIGIN", False, consented="silent"
        ) == ("silent", "")

    def test_refuses_a_creation_with_no_repository_or_no_consent(
        self, world, guard, monkeypatch
    ):
        assert said(wg.guard_worktree_creation, "", "", "ORIGIN", False) == (
            "silent",
            "",
        )
        monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": SINGLE)
        top = str(world.clean)
        decision, reason = said(
            wg.guard_worktree_creation, top, top, "ORIGIN", False, session_id=guard.sid
        )
        assert decision == "deny" and reason.startswith(
            "ORIGIN\nNo other session is working in this tree (= single-stream)."
        )


class Test_judge_creation:
    def test_accepts_a_token_as_the_users_intent(self, world, guard, monkeypatch):
        monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": SINGLE)
        top = str(world.clean)
        decision, reason = said(
            wg.judge_creation,
            "git worktree add ../wt f  # [worktree-ok] but don't",
            top,
            top,
            guard.sid,
        )
        assert decision == "ask" and "unbalanced" not in reason

    def test_refuses_a_token_it_could_not_read_and_says_why(
        self, world, guard, monkeypatch
    ):
        monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": SINGLE)
        top = str(world.clean)
        decision, reason = said(
            wg.judge_creation,
            "git worktree add ../wt f  # \"don't forget [worktree-ok]",
            top,
            top,
            guard.sid,
        )
        assert decision == "deny" and "unbalanced quote" in reason
        guard.grant(world.clean)
        assert said(
            wg.judge_creation,
            "git worktree add ../wt f && echo done",
            top,
            top,
            guard.sid,
        ) == ("silent", "")


# --- main ---------------------------------------------------------------------------

# The switch ladder's two choice rows, attempt 1 and attempt 2, in both
# languages, as `c38f97d7` printed them for a switch in the clean world.
CHOICE = {
    ("en", "idle", 1): (
        "deny",
        "Other Claude sessions may exist in this tree, but none of them can be "
        "shown to be working: no input or transcript for {idle_min}+ minutes, or "
        "a lease whose owning session cannot be identified.\n"
        "    pid 222 (Terminal terminal)  /tree\n"
        "        terminal in/out 6.7h ago · transcript activity 1.5h ago\n"
        "\n"
        "Do not choose for the user. Ask with the AskUserQuestion tool, offering "
        "exactly these two options:\n"
        "\n"
        "  No session here can be shown to be working — switch in this shared "
        "tree, or split into a worktree?\n"
        '    1. "Switch in this shared tree" — right when those are forgotten '
        "tabs or sessions that have already ended. Re-issue the SAME command "
        "with the token appended (`… # [shared-tree-ok]`); it carries this "
        "answer, so the switch goes straight through.\n"
        '    2. "Split into a worktree" — keeps the branch of a session that IS '
        "still working. Run `git worktree add {wt_root}/<branch> <branch>  # "
        "[worktree-ok]` for a branch that already exists, or `git worktree add "
        "{wt_root}/<name> -b <branch> origin/main  # [worktree-ok]` for a new "
        "one, then work there from a separate session. The token carries this "
        "answer, so creating it is confirmed rather than questioned again.\n"
        "\n"
        "Then run what they picked. Re-issuing this command before they answer "
        "reaches the ordinary confirmation prompt instead.",
    ),
    ("en", "idle", 2): (
        "ask",
        "Other Claude sessions may exist in this tree, but none of them can be "
        "shown to be working: no input or transcript for {idle_min}+ minutes, or "
        "a lease whose owning session cannot be identified.\n"
        "    pid 222 (Terminal terminal)  /tree\n"
        "        terminal in/out 6.7h ago · transcript activity 1.5h ago\n"
        "\n"
        "Your call:\n"
        "  · Approve — switch branches in this shared tree (right when those are "
        "forgotten tabs or sessions that have already ended).\n"
        "  · Deny — the switch is cancelled; split into a worktree instead so a "
        "session that IS still working keeps its branch:\n"
        "\n"
        "  # check an existing branch out into a worktree\n"
        "  git worktree add {wt_root}/<branch> <branch>\n"
        "\n"
        "  # or create a new branch off the latest origin/main\n"
        "  git fetch origin\n"
        "  git worktree add {wt_root}/<name> -b <branch> origin/main\n"
        "\n"
        "Then work in that folder from a separate Claude Code session. `git "
        "worktree list` shows worktrees.",
    ),
    ("en", "unusable", 1): (
        "deny",
        "Cannot determine whether other sessions are working in this tree "
        "(process inspection unavailable in this environment).\n"
        "\n"
        "Do not choose for the user. Ask with the AskUserQuestion tool, offering "
        "exactly these two options:\n"
        "\n"
        "  No verdict is possible here — switch in this shared tree, or split "
        "into a worktree?\n"
        '    1. "Switch in this shared tree" — right when those are forgotten '
        "tabs or sessions that have already ended. Re-issue the SAME command "
        "with the token appended (`… # [shared-tree-ok]`); it carries this "
        "answer, so the switch goes straight through.\n"
        '    2. "Split into a worktree" — keeps the branch of a session that IS '
        "still working. Run `git worktree add {wt_root}/<branch> <branch>  # "
        "[worktree-ok]` for a branch that already exists, or `git worktree add "
        "{wt_root}/<name> -b <branch> origin/main  # [worktree-ok]` for a new "
        "one, then work there from a separate session. The token carries this "
        "answer, so creating it is confirmed rather than questioned again.\n"
        "\n"
        "Then run what they picked. Re-issuing this command before they answer "
        "reaches the ordinary confirmation prompt instead.",
    ),
    ("en", "unusable", 2): (
        "ask",
        "Cannot determine whether other sessions are working in this tree "
        "(process inspection unavailable in this environment).\n"
        "Your call:\n"
        "  · Approve — switch branches in this shared tree (safe when no other "
        "session is active here).\n"
        "  · Deny — the switch is cancelled; split into a worktree instead so "
        "any concurrent session keeps its branch:\n"
        "\n"
        "  # check an existing branch out into a worktree\n"
        "  git worktree add {wt_root}/<branch> <branch>\n"
        "\n"
        "  # or create a new branch off the latest origin/main\n"
        "  git fetch origin\n"
        "  git worktree add {wt_root}/<name> -b <branch> origin/main\n"
        "\n"
        "Then work in that folder from a separate Claude Code session. `git "
        "worktree list` shows worktrees.",
    ),
    ("ko", "idle", 1): (
        "deny",
        "이 트리에 다른 Claude 세션이 있을 수 있으나, 작업 중임을 확인할 수 있는 "
        "것은 없습니다 — {idle_min}분 이상 활동(키 입력·작업 기록)이 없거나, "
        "lease 를 남긴 세션이 누구인지 확인되지 않습니다.\n"
        "    pid 222 (Terminal 터미널)  /tree\n"
        "        터미널 입력/출력 6.7시간 전 · 작업 기록(트랜스크립트) 1.5시간 전\n"
        "\n"
        "사용자 대신 고르지 마세요. AskUserQuestion 툴로 아래 두 선택지를 그대로 "
        "물어보세요:\n"
        "\n"
        "  작업 중임이 확인되는 세션이 없습니다 — 이 공용 트리에서 전환할까요, "
        "worktree 로 분리할까요?\n"
        '    1. "이 공용 트리에서 전환한다" — 잊힌 탭이거나 이미 끝난 세션이면 '
        "이쪽이 맞습니다. 같은 명령 뒤에 토큰을 붙여(`… # [shared-tree-ok]`) "
        "다시 실행하세요. 이 토큰이 지금 고른 답을 담고 있어 전환이 그대로 "
        "통과합니다.\n"
        '    2. "worktree 로 분리한다" — 아직 작업 중인 세션의 브랜치를 '
        "보존합니다. 이미 있는 브랜치면 `git worktree add {wt_root}/<branch> "
        "<branch>  # [worktree-ok]`, 새로 만들 브랜치면 `git worktree add "
        "{wt_root}/<name> -b <branch> origin/main  # [worktree-ok]` 를 "
        "실행하고, 그 폴더에서 별도 세션으로 작업하세요. 이 토큰이 지금 고른 "
        "답을 담고 있어 생성할 때 다시 묻지 않고 확인만 받습니다.\n"
        "\n"
        "고른 쪽을 실행하세요. 답을 받기 전에 같은 명령을 다시 내면 일반 확인창이 "
        "뜹니다.",
    ),
    ("ko", "idle", 2): (
        "ask",
        "이 트리에 다른 Claude 세션이 있을 수 있으나, 작업 중임을 확인할 수 있는 "
        "것은 없습니다 — {idle_min}분 이상 활동(키 입력·작업 기록)이 없거나, "
        "lease 를 남긴 세션이 누구인지 확인되지 않습니다.\n"
        "    pid 222 (Terminal 터미널)  /tree\n"
        "        터미널 입력/출력 6.7시간 전 · 작업 기록(트랜스크립트) 1.5시간 전\n"
        "\n"
        "선택해 주세요:\n"
        "  · 승인 — 이 공용 트리에서 그대로 브랜치를 전환합니다(잊힌 탭이거나 이미 "
        "끝난 세션이면 이쪽이 맞습니다).\n"
        "  · 거부 — 전환을 취소하고 worktree 로 분리해, 아직 작업 중인 세션의 "
        "브랜치를 보존합니다:\n"
        "\n"
        "  # 기존 브랜치를 worktree로 꺼내기\n"
        "  git worktree add {wt_root}/<branch> <branch>\n"
        "\n"
        "  # 새 브랜치를 최신 origin/main 기준으로 생성 (저장소 정책)\n"
        "  git fetch origin\n"
        "  git worktree add {wt_root}/<name> -b <branch> origin/main\n"
        "\n"
        "그런 다음 그 폴더에서 별도의 Claude Code 세션으로 작업하세요. worktree "
        "목록은 `git worktree list`.",
    ),
    ("ko", "unusable", 1): (
        "deny",
        "이 트리에서 다른 세션이 작업 중인지 확인할 수 없습니다(이 환경에서는 "
        "프로세스 조회가 불가능합니다).\n"
        "\n"
        "사용자 대신 고르지 마세요. AskUserQuestion 툴로 아래 두 선택지를 그대로 "
        "물어보세요:\n"
        "\n"
        "  여기서는 자동 판정이 불가능합니다 — 이 공용 트리에서 전환할까요, "
        "worktree 로 분리할까요?\n"
        '    1. "이 공용 트리에서 전환한다" — 잊힌 탭이거나 이미 끝난 세션이면 '
        "이쪽이 맞습니다. 같은 명령 뒤에 토큰을 붙여(`… # [shared-tree-ok]`) "
        "다시 실행하세요. 이 토큰이 지금 고른 답을 담고 있어 전환이 그대로 "
        "통과합니다.\n"
        '    2. "worktree 로 분리한다" — 아직 작업 중인 세션의 브랜치를 '
        "보존합니다. 이미 있는 브랜치면 `git worktree add {wt_root}/<branch> "
        "<branch>  # [worktree-ok]`, 새로 만들 브랜치면 `git worktree add "
        "{wt_root}/<name> -b <branch> origin/main  # [worktree-ok]` 를 "
        "실행하고, 그 폴더에서 별도 세션으로 작업하세요. 이 토큰이 지금 고른 "
        "답을 담고 있어 생성할 때 다시 묻지 않고 확인만 받습니다.\n"
        "\n"
        "고른 쪽을 실행하세요. 답을 받기 전에 같은 명령을 다시 내면 일반 확인창이 "
        "뜹니다.",
    ),
    ("ko", "unusable", 2): (
        "ask",
        "이 트리에서 다른 세션이 작업 중인지 확인할 수 없습니다(이 환경에서는 "
        "프로세스 조회가 불가능합니다).\n"
        "선택해 주세요:\n"
        "  · 승인 — 이 공용 트리에서 그대로 브랜치를 전환합니다(다른 활성 세션이 "
        "없다면 안전합니다).\n"
        "  · 거부 — 전환을 취소하고 worktree 로 분리해, 동시 세션의 브랜치를 "
        "보존합니다:\n"
        "\n"
        "  # 기존 브랜치를 worktree로 꺼내기\n"
        "  git worktree add {wt_root}/<branch> <branch>\n"
        "\n"
        "  # 새 브랜치를 최신 origin/main 기준으로 생성 (저장소 정책)\n"
        "  git fetch origin\n"
        "  git worktree add {wt_root}/<name> -b <branch> origin/main\n"
        "\n"
        "그런 다음 그 폴더에서 별도의 Claude Code 세션으로 작업하세요. worktree "
        "목록은 `git worktree list`.",
    ),
}

# The creation ladder's two choice rows, as `321e9de1` printed them.
CREATION_OPTIONS = {
    "en": "\n"
    "Do not choose for the user. Ask with the AskUserQuestion tool, offering "
    "exactly these two options:\n"
    "\n"
    "  {question}\n"
    '    1. "Create the worktree" — retry it and approve at the prompt — '
    "creating a worktree always takes a confirmation, so the retry asks once.\n"
    '    2. "Switch in the shared tree" — run `git switch <branch>  # '
    "[shared-tree-ok]` for an existing branch, or `git switch -c <branch> "
    "origin/main  # [shared-tree-ok]` for a new one instead. The token carries "
    "this answer, so the switch is not questioned again.\n"
    "\n"
    "Then run what they picked. Re-issuing this command before they answer "
    "reaches the ordinary confirmation prompt instead.",
    "ko": "\n"
    "사용자 대신 고르지 마세요. AskUserQuestion 툴로 아래 두 선택지를 그대로 "
    "물어보세요:\n"
    "\n"
    "  {question}\n"
    '    1. "worktree 를 만든다" — 그대로 다시 시도하고 확인창에서 승인하세요 — '
    "worktree 생성은 항상 확인을 한 번 거치므로 재시도 때 한 번 물어봅니다.\n"
    '    2. "공용 트리에서 브랜치만 전환한다" — 대신 기존 브랜치면 `git switch '
    "<branch>  # [shared-tree-ok]`, 새 브랜치면 `git switch -c <branch> "
    "origin/main  # [shared-tree-ok]` 중 하나를 실행하세요. 이 토큰이 지금 "
    "고른 답을 담고 있어 전환할 때 다시 묻지 않습니다.\n"
    "\n"
    "고른 쪽을 실행하세요. 답을 받기 전에 같은 명령을 다시 내면 일반 확인창이 "
    "뜹니다.",
}
CREATION_SITUATION = {
    ("en", "idle"): "Attempting to create a worktree with `git worktree add`.\n"
    "The only other sessions here have shown no activity (input or transcript) "
    "for {idle_min}+ minutes — if they are forgotten tabs this is effectively "
    "single-stream work and plain `git switch` beats a worktree.\n"
    "    pid 222 (Terminal terminal)  /tree\n"
    "        terminal in/out 6.7h ago · transcript activity 1.5h ago\n",
    ("en", "unusable"): "Attempting to create a worktree with `git worktree add`.\n"
    "Cannot determine whether other sessions are working here (ps/lsof "
    "unavailable), so no automatic verdict.\n",
    ("ko", "idle"): "`git worktree add` 로 worktree를 만들려 합니다.\n"
    "이 트리의 다른 세션은 {idle_min}분 이상 활동(키 입력·작업 기록)이 없는 "
    "것뿐입니다 — 잊힌 탭이면 사실상 단건 작업이라 worktree 없이 `git switch` 가 "
    "낫습니다.\n"
    "    pid 222 (Terminal 터미널)  /tree\n"
    "        터미널 입력/출력 6.7시간 전 · 작업 기록(트랜스크립트) 1.5시간 전\n",
    ("ko", "unusable"): "`git worktree add` 로 worktree를 만들려 합니다.\n"
    "동시 세션 여부를 확인할 수 없어(ps/lsof 사용 불가) 자동 판정을 못 합니다.\n",
}
CREATION_QUESTION = {
    ("en", "idle"): "Only idle sessions here — split into a worktree, or switch "
    "in the shared tree?",
    ("en", "unusable"): "No verdict is possible here — split into a worktree, or "
    "switch in the shared tree?",
    ("ko", "idle"): "여기엔 멈춰 있는 세션뿐입니다 — worktree 로 분리할까요, 공용 "
    "트리에서 전환할까요?",
    ("ko", "unusable"): "여기서는 자동 판정이 불가능합니다 — worktree 로 "
    "분리할까요, 공용 트리에서 전환할까요?",
}
CREATION_FALLBACK = {
    ("en", "idle"): "\n"
    "Still split into a worktree? Declining switches to plain `git switch` in "
    "the shared tree instead:\n"
    "  git fetch origin\n"
    "  git switch -c <branch> origin/main   # new branch\n"
    "  git switch <branch>                  # existing branch\n"
    "\n"
    "If this genuinely is concurrent work needing separation, state why and get "
    "the user's confirmation first (if the user already asked for a worktree, "
    "retry with [worktree-ok] in the command).",
    ("en", "unusable"): "Confirm if this really is concurrent work; if "
    "single-stream, cancel and use `git switch`.",
    ("ko", "idle"): "\n"
    "그래도 worktree 로 분리할지 확인해 주세요. 거부하면 공유 트리에서 `git "
    "switch` 로 전환합니다:\n"
    "  git fetch origin\n"
    "  git switch -c <branch> origin/main   # 새 브랜치\n"
    "  git switch <branch>                  # 기존 브랜치\n"
    "\n"
    "정말 동시 작업이라 분리가 필요하면 그 이유를 밝히고 사용자 확인을 먼저 "
    "받으세요 (사용자가 이미 워크트리를 지시했다면 명령에 [worktree-ok] 를 붙여 "
    "다시 시도).",
    ("ko", "unusable"): "정말 동시 작업이면 확인해 주시고, 단건이면 취소하고 `git "
    "switch` 로 진행하세요.",
}

AGENT_REASON = {
    "en": 'The Agent tool was called with isolation: "worktree" (the harness '
    "creates a worktree at <repo>/.claude/worktrees/<name>). The agent runs "
    "beside this session, so it is concurrent work and a separate tree is the "
    "right shape for it. Creating a worktree still takes the user's "
    "confirmation once per session. Declining cancels this spawn.",
    "ko": 'Agent 툴을 isolation: "worktree" 로 호출했습니다(하네스가 '
    "<repo>/.claude/worktrees/<name> 에 worktree 를 만듭니다). 이 agent 는 이 "
    "세션과 나란히 돌기 때문에 동시 작업이고, 별도 트리가 맞는 모양입니다. 다만 "
    "worktree 생성은 세션마다 한 번 사용자 확인을 거칩니다. 거부하면 이번 호출이 "
    "취소됩니다.",
}

# The tracked-changes row for the dirty world's one modified `f.txt`.
LEADS = {
    ("en", True): "Single-stream tree",
    ("en", False): "[shared-tree-ok] carries the user's answer to switch in this "
    "shared tree",
    ("ko", True): "이 트리는 단건 작업이라",
    ("ko", False): "[shared-tree-ok] 가 공용 트리에서 전환한다는 사용자의 답을 "
    "담고 있어",
}
DIRTY_ASK = {
    "en": "{lead}, so the switch is allowed — but there are 1 uncommitted "
    "tracked changes:\n     M  f.txt\nThey will follow you onto the target "
    "branch. Confirm to proceed (commit/stash first is recommended).",
    "ko": "{lead} 브랜치 전환을 허용할 수 있지만, 커밋되지 않은 변경 1건이 "
    "있습니다:\n     M  f.txt\n전환하면 이 변경이 대상 브랜치로 따라갑니다. "
    "진행할지 확인해 주세요 (커밋/스태시 후 전환을 권장).",
}
PRESS = {
    "en": "This session's person pressed `automation` on the routing question, "
    "so this guard puts no question to them, and none is to be put to them in "
    "its place.",
    "ko": "이 세션의 사용자가 라우팅 질문에서 `automation` 을 눌렀습니다. 그래서 "
    "이 guard 는 사용자에게 아무것도 묻지 않으며, 다른 방법으로 대신 물어서도 "
    "안 됩니다.",
}


def dirty_deny(lang, lead, git="git"):
    """The tracked-changes row's deny under the press, one text for every
    switch form; GIT is the command word `git_at` hands back."""
    if lang == "en":
        return (
            f"{lead}, so no other row of this guard stops the switch, but 1 "
            "uncommitted tracked changes are present:\n"
            "     M  f.txt\n"
            "\n" + PRESS["en"] + "\n\n"
            "This row of the guard stops a branch switch while uncommitted "
            "tracked changes are present, and says nothing of a switch once none "
            "are.\n"
            "\n"
            "The ways on, none of which needs a person. Issue each command on its "
            f"own: this guard reads the tree before a command runs, so `{git} "
            f"stash && {git} switch <branch>` on one line meets this same "
            f"refusal. `{git} commit` and `{git} stash` are on this guard's list "
            "of commands that leave the branch where it is, so each passes it "
            "when issued alone. Which of them fits this switch, and what to run "
            "after it, is yours to decide.\n"
            "\n"
            "Re-issuing this command unchanged meets this same refusal."
        )
    return (
        f"{lead} 이 guard 의 다른 규칙은 이 전환을 막지 않지만, 커밋되지 않은 추적 "
        "파일 변경이 1건 있습니다:\n"
        "     M  f.txt\n"
        "\n" + PRESS["ko"] + "\n\n"
        "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 동안 브랜치 "
        "전환을 막고, 변경이 없으면 전환에 대해 아무 말도 하지 않습니다.\n"
        "\n"
        "사람이 없어도 되는 길은 아래와 같습니다. 명령은 하나씩 따로 실행하세요. "
        f"이 guard 는 명령이 실행되기 전에 트리를 읽으므로, `{git} stash && {git} "
        "switch <branch>` 처럼 한 줄에 쓰면 같은 거부를 받습니다. "
        f"`{git} commit` 과 `{git} stash` 는 이 guard 가 브랜치를 그대로 두는 "
        "명령으로 꼽는 목록에 있어, 따로 실행하면 이 guard 를 통과합니다. 이 전환에 "
        "어느 쪽이 맞는지, 그 뒤에 무엇을 실행할지는 직접 정하세요.\n"
        "\n"
        "이 명령을 그대로 다시 실행하면 같은 거부를 받습니다."
    )


# The unrecognised-shape stop for `git checkout feature/x` in the dirty world.
STOP_TEXT = {
    "en": "This command holds a git command this guard does not know to leave "
    "the branch where it is, and in this tree a branch switch would matter: it "
    "has 1 uncommitted tracked changes, which a switch would carry onto the "
    "other branch.\n"
    "\n"
    "  · `git checkout feature/x` — a `git checkout` with no `-- <path>`, which "
    "can switch a branch as well as restore a file. For a switch, write `git "
    "switch <branch>` or `git switch --detach <rev>`; for a restore, `git "
    "checkout -- <path>` or `git restore <path>`.\n"
    "\n"
    "The plain spellings are what this guard reads: a `git switch` then meets "
    "the branch-switch rules, and a git subcommand on the list passes. Name "
    "another tree with `git -C <dir>`. The list is `LEAVES_THE_TREE` in "
    "hooks/worktree-guard.py. ",
    "ko": "이 명령에는 브랜치를 그대로 둔다고 이 guard 가 확인하지 못한 git 명령이 "
    "있고, 이 트리에서는 브랜치 전환이 문제가 됩니다. 커밋되지 않은 추적 파일 "
    "변경이 1건 있고, 전환하면 이 변경이 다른 브랜치로 따라갑니다.\n"
    "\n"
    "  · `git checkout feature/x` — `-- <path>` 가 없는 `git checkout` 이라, "
    "파일을 되돌릴 수도 있지만 브랜치를 전환할 수도 있습니다. 전환이라면 `git "
    "switch <branch>` 나 `git switch --detach <rev>` 로, 파일 되돌리기라면 `git "
    "checkout -- <path>` 나 `git restore <path>` 로 쓰세요.\n"
    "\n"
    "이 guard 는 위의 평범한 표기를 읽습니다. `git switch` 는 브랜치 전환 "
    "규칙으로 판단하고, 목록에 있는 git 하위 명령은 그대로 통과합니다. 다른 "
    "트리는 `git -C <dir>` 로 지정하세요. 목록은 hooks/worktree-guard.py 의 "
    "`LEAVES_THE_TREE` 입니다. ",
}
ENDINGS = {
    ("en", "ask"): "Approve to run it as written, or decline and re-issue it in a "
    "plain spelling.",
    ("en", "deny"): "Re-issue the command in a plain spelling.",
    ("ko", "ask"): "그대로 실행하려면 승인하고, 아니면 거부한 뒤 평범한 표기로 다시 "
    "실행하세요.",
    ("ko", "deny"): "평범한 표기로 다시 실행하세요.",
}
TREES = {
    "en": "This command holds a git command this guard does not know to leave "
    "the branch where it is, and in each of these trees a branch switch would "
    "matter:\n"
    "  `{repo}`: it has 1 uncommitted tracked changes, which a switch would "
    "carry onto the other branch.\n"
    "  `{w}`: whether another session works here cannot be told in this "
    "environment (process inspection is unavailable).\n"
    "\n",
    "ko": "이 명령에는 브랜치를 그대로 둔다고 이 guard 가 확인하지 못한 git 명령이 "
    "있고, 아래 트리마다 브랜치 전환이 문제가 됩니다.\n"
    "  `{repo}`: 커밋되지 않은 추적 파일 변경이 1건 있고, 전환하면 이 변경이 "
    "다른 브랜치로 따라갑니다.\n"
    "  `{w}`: 이 환경에서는 프로세스를 조회할 수 없어, 다른 세션이 이 트리에서 "
    "작업 중인지 확인할 수 없습니다.\n"
    "\n",
}

# Shapes known to leave the branch where it is, a substitution of them
# included, each with one redirection spelling.
LISTED = (
    "git status",
    "git add -A 2>/dev/null",
    "git commit -m x >/dev/null 2>&1",
    "git checkout -- f.txt",
    "git checkout feature/x -- f.txt 2> /dev/null",
    "git restore f.txt",
    "git -C W status",
    "git worktree list",
    "git stash",
    "F=$(git diff --name-only)",
    "echo `git rev-parse HEAD`",
    "diff <(git show HEAD:f.txt) f.txt",
    "git log $(git rev-parse HEAD)",
)

# Unrecognised shapes, each with a phrase of the plain spelling its stop names.
UNRECOGNISED = {
    "git checkout feature/x": "`git switch <branch>`",
    "git checkout f.txt": "`git restore <path>`",
    "git bisect start": "`git -C <scratch clone>`",
    "git stash branch y": "`git -C <scratch clone>`",
    "sh -c 'git switch x'": "rather than as a string",
    'eval "git switch x"': "rather than as a string",
    "echo $(git switch x)": "outside the substitution",
    "echo $(echo $(git checkout x))": "`git switch <branch>`",
    "2>/dev/null git switch x": "Write `git` first",
    "2>&1 git switch x": "Write `git` first",
    "git 2>&1 worktree add ../wt b": "after the command's own words",
    'git switch x && echo "unclosed': "`git commit -F <file>`",
    "git rebase main feature/x": "Write `git switch <branch>` first, then `git "
    "rebase <upstream>`.",
}

# Commands a creation of the clean world runs in, one per kind of line.
CREATIONS = (
    "git worktree add ../wt f",
    "git status && git worktree add ../wt f",
    "git switch feature/x && git worktree add ../wt f",
    "git worktree add ../wt f && git switch feature/x",
    "git checkout feature/x && git worktree add ../wt f",
    "git switch feature/x && git worktree add ../wt f  # [worktree-ok]",
    "git switch feature/x && git worktree add ../wt f &",
    "git switch feature/x && git -C {repo} worktree add ../wt f",
    "cd {repo} && git switch feature/x && git worktree add ../wt f",
)
STRICTNESS = {"allow": 0, "silent": 1, "ask": 2, "deny": 3}
STATES = (
    ("active", BUSY, "clean"),
    ("idle", QUIET, "clean"),
    ("unusable", BLIND, "clean"),
    ("dirty", SINGLE, "dirty"),
    ("clean", SINGLE, "clean"),
)


class Test_main:
    # The switch ladder.

    def test_accepts_a_switch_in_a_clean_tree_nobody_else_is_in(self, world, guard):
        assert guard("git switch feature/x", world.clean) == ("silent", "")
        assert guard("git checkout README.md && git switch x", world.clean) == (
            "silent",
            "",
        )

    def test_refuses_a_switch_where_another_session_is_active(self, world, guard):
        guard.grant(world.clean, f"{guard.sid}-record")
        guard.press(world.clean, f"{guard.sid}-answer")
        for source in ("none", "record", "answer"):
            for command in (
                "git switch feature/x  # [shared-tree-ok]",
                "git worktree add ../wt -b x && git switch feature/x",
            ):
                sid = f"{guard.sid}-{source}"
                decision, reason = guard(command, world.clean, BUSY, sid=sid)
                assert decision == "deny", (source, command)
                assert reason.startswith("Blocking this branch switch"), reason
                assert "VS Code" in reason and "AskUserQuestion" not in reason
                assert "worktree add" in reason

    @pytest.mark.parametrize("lang", ["en", "ko"])
    def test_refuses_a_switch_past_idle_or_blind_rows_without_the_choice(
        self, world, guard, lang
    ):
        guard.lang(lang)
        wt_root = wg.repo_paths(str(world.clean))[1]
        for state, sessions in (("idle", QUIET), ("unusable", BLIND)):
            sid = f"{guard.sid}-{state}"
            for attempt in (1, 2, 3):
                want, text = CHOICE[lang, state, min(attempt, 2)]
                got = guard("git switch feature/x", world.clean, sessions, sid=sid)
                assert got == (
                    want,
                    text.format(idle_min=wg.IDLE_MIN, wt_root=wt_root),
                ), (state, attempt)

    def test_accepts_the_shared_tree_token_at_the_choice_rows(self, world, guard):
        for sessions in (QUIET, BLIND):
            for command in (
                "git switch feature/x  # [shared-tree-ok]",
                "git switch feature/x && echo done  # [shared-tree-ok]",
            ):
                assert guard(command, world.clean, sessions) == ("silent", "")

    def test_refuses_a_token_in_prose_or_on_the_dirty_row(self, world, guard):
        decision, reason = guard(
            "git switch feature/x && echo 'we documented [shared-tree-ok] today'",
            world.clean,
            QUIET,
        )
        assert decision == "deny" and "AskUserQuestion" in reason
        for n, (sessions, command, counted) in enumerate(
            (
                (SINGLE, "git switch other", True),
                (QUIET, "git switch other  # [shared-tree-ok]", False),
                (BLIND, "git switch other  # [shared-tree-ok]", False),
            )
        ):
            for lang in ("en", "ko"):
                guard.lang(lang)
                got = guard(command, world.dirty, sessions, sid=f"{guard.sid}-{n}")
                lead = LEADS[lang, counted]
                assert got == ("ask", DIRTY_ASK[lang].format(lead=lead)), got

    def test_refuses_a_switch_with_no_session_id_by_asking(self, world, guard):
        assert guard("git switch feature/x", world.clean, QUIET, sid="")[0] == "ask"

    def test_accepts_each_direction_and_each_session_its_own_question(
        self, world, guard
    ):
        sid = guard.sid
        guard("git worktree add ../wt f  # [worktree-ok]", world.clean, QUIET, sid=sid)
        for command in ("git worktree add ../wt feature/x", "git switch feature/x"):
            assert guard(command, world.clean, QUIET, sid=sid)[0] == "deny", command
            assert guard(command, world.clean, QUIET, sid=sid)[0] == "ask", command
        assert guard("git switch feature/x", world.clean, QUIET, sid=sid + "b") == (
            guard("git switch feature/x", world.clean, QUIET, sid=sid + "c")
        )

    # The creation ladder.

    def test_refuses_a_creation_in_a_single_stream_tree(self, world, guard):
        for command in (
            "git worktree add ../wt feature/x",
            "git worktree add ../wt f  # it's fine",
            "git status  # don't forget\ngit worktree add ../wt f",
            "git worktree add ../wt feature/x && echo 'see [worktree-ok] notes'",
            'git worktree add ../wt f && echo "we agreed on [worktree-ok] yesterday',
            "git worktree add ../wt f | tail -2",
            "sudo git worktree add ../wt f",
            "~/git worktree add ../wt f",
        ):
            decision, reason = guard(command, world.clean)
            assert decision == "deny", command
            assert "git switch" in reason and "AskUserQuestion" not in reason
        assert (
            "unbalanced" in guard("git worktree add ../wt f  # don't", world.clean)[1]
        )

    def test_accepts_the_worktree_token_as_a_confirmation(self, world, guard):
        for lang, sentence in (
            ("en", "No other Claude session can be shown to be working in this tree"),
            ("ko", "이 트리에서 작업 중임이 확인되는 다른 Claude 세션은 없지만"),
        ):
            guard.lang(lang)
            for sessions, counted in ((SINGLE, True), (QUIET, True), (BLIND, False)):
                decision, reason = guard(
                    "git worktree add ../wt f  # [worktree-ok]", world.clean, sessions
                )
                assert decision == "ask" and "[worktree-ok]" in reason
                assert (sentence in reason) is counted, (lang, sessions)
                assert "AskUserQuestion" not in reason
        guard.lang("en")
        for command in (
            'git worktree add ../wt -b b origin/main && echo "wip; go"  # [worktree-ok]',
            "git worktree add ../wt f  # [worktree-ok] — it's concurrent work",
        ):
            decision, reason = guard(command, world.clean)
            assert decision == "ask" and "unbalanced" not in reason, command

    def test_refuses_a_creation_where_another_session_is_active_by_asking(
        self, world, guard
    ):
        decision, reason = guard("git worktree add ../wt f", world.clean, BUSY)
        assert decision == "ask" and "a worktree split looks justified" in reason

    @pytest.mark.parametrize("lang", ["en", "ko"])
    def test_refuses_a_creation_past_idle_or_blind_rows_without_the_choice(
        self, world, guard, lang
    ):
        guard.lang(lang)
        for state, sessions in (("idle", QUIET), ("unusable", BLIND)):
            sid = f"{guard.sid}-{state}"
            situation = CREATION_SITUATION[lang, state].format(idle_min=wg.IDLE_MIN)
            for attempt in (1, 2):
                got = guard(
                    "git worktree add ../wt feature/x", world.clean, sessions, sid=sid
                )
                if attempt == 1:
                    question = CREATION_QUESTION[lang, state]
                    want = (
                        "deny",
                        situation + CREATION_OPTIONS[lang].format(question=question),
                    )
                else:
                    want = ("ask", situation + CREATION_FALLBACK[lang, state])
                assert got == want, (state, attempt)

    # Consent.

    def test_accepts_consent_above_every_creation_row(self, world, guard):
        for source in ("record", "answer"):
            sid = f"{guard.sid}-{source}"
            if source == "record":
                guard.grant(world.clean, sid)
            else:
                guard.press(world.clean, sid)
            for sessions in (SINGLE, BUSY, QUIET, BLIND):
                for command in (
                    "git worktree add ../wt f",
                    "git worktree add ../wt f  # [worktree-ok]",
                    "git worktree add ../wt f &",
                    "git worktree add ../a -b feature/x origin/main",
                ):
                    decision, reason = guard(command, world.clean, sessions, sid=sid)
                    assert decision == "allow", (source, sessions, command)
        guard.lang("ko")
        reason = guard(
            "git worktree add ../wt f", world.clean, sid=f"{guard.sid}-answer"
        )[1]
        assert "라우팅 질문에서 `automation` 을 눌렀고" in reason

    def test_refuses_an_allow_for_a_command_that_is_more_than_a_creation(
        self, world, guard
    ):
        guard.grant(world.clean)
        for command in (
            "git worktree add ../wt f && echo done",
            "git worktree add ../wt f | tail -2",
            "cd /tmp && git worktree add ../wt f",
            "git worktree add ../wt f  # don't",
            "git worktree add ../wt f $(touch /tmp/marker)",
            "git worktree add ../wt f > /tmp/clobber",
            "sudo git worktree add ../wt f",
            "LD_PRELOAD=/tmp/e.so git worktree add ../wt f",
            "/usr/bin/git worktree add ../wt f",
            "~/git worktree add ../wt f",
        ):
            for sessions in (SINGLE, QUIET, BLIND):
                assert guard(command, world.clean, sessions) == ("silent", ""), command
        decision, reason = guard("git worktree add ../wt f", world.clean)
        assert decision == "allow"
        assert "A worktree creation already ran in this repository" in reason

    def test_refuses_consent_to_another_session_no_session_or_the_switch(
        self, world, guard
    ):
        guard.grant(world.clean, f"{guard.sid}-a")
        assert guard("git worktree add ../wt f", world.clean)[0] == "deny"
        assert guard("git worktree add ../wt f", world.clean, sid="")[0] == "deny"
        guard.grant(world.clean)
        assert guard("git switch feature/x", world.clean, QUIET)[0] == "deny"
        guard.press(world.clean)
        decision, reason = guard("git switch feature/x", world.clean, BUSY)
        assert decision == "deny" and "actively working" in reason
        before = sorted(os.listdir(os.path.dirname(guard.grant(world.clean))))
        guard("git worktree add ../wt f", world.clean, sid=f"{guard.sid}-n")
        assert sorted(os.listdir(os.path.dirname(guard.grant(world.clean)))) == before

    def test_accepts_the_measured_automation_run_and_the_payloads_path(
        self, world, guard, tmp_path
    ):
        guard.press(world.clean)
        command = (
            "git worktree add ../wt-a -b fix/a feature/x\n"
            "git worktree add ../wt-b -b fix/b feature/x\n"
            "git switch -c fix/c  # [worktree-ok] each branch carries its own routing.md"
        )
        assert guard(command, world.clean) == ("silent", "")
        path = write_transcript(
            tmp_path / "elsewhere", "pathed", ask_entries(world.clean)
        )
        assert guard("git worktree add ../wt f", world.clean, sid="pathed")[0] == "deny"
        assert (
            guard(
                "git worktree add ../wt f", world.clean, sid="pathed", transcript=path
            )[0]
            == "allow"
        )
        isolated = {"isolation": "worktree", "prompt": "x"}
        assert guard(
            "", world.clean, sid="pathed", tool="Agent", tool_input=isolated
        ) == ("ask", AGENT_REASON["en"])
        assert guard(
            "",
            world.clean,
            sid="pathed",
            tool="Agent",
            tool_input=isolated,
            transcript=path,
        ) == ("silent", "")

    # A switch and a creation on one line.

    def test_refuses_a_creation_behind_any_switch_verdict(self, world, guard):
        for n, sessions in enumerate((SINGLE, BUSY, QUIET, BLIND)):
            for m, command in enumerate(
                (
                    "git switch feature/x && git worktree add ../wt f",
                    "git switch feature/x || git worktree add ../wt f",
                    "git switch feature/x\ngit worktree add ../wt f",
                )
            ):
                sid = f"{guard.sid}-{n}-{m}"
                decision, reason = guard(command, world.clean, sessions, sid=sid)
                assert decision == "deny", (sessions, command)
        decision, reason = guard(
            "git switch feature/x && git worktree add ../wt f", world.dirty
        )
        assert decision == "deny" and "git switch" in reason

    def test_refuses_to_be_silent_where_the_writer_records(self, world, guard):
        holes = []
        consent = wg.worktree_consent
        for name, sessions, attempts in (
            ("single", SINGLE, 1),
            ("active", BUSY, 1),
            ("idle", QUIET, 3),
            ("unusable", BLIND, 3),
        ):
            for cwd in (world.clean, world.outside):
                for n, line in enumerate(CREATIONS):
                    command = line.format(repo=world.clean)
                    acted = consent.creation_directory(command, str(cwd))
                    if not acted or not consent.optin.repo_root(acted):
                        continue
                    sid = f"{guard.sid}-{name}-{cwd.name}-{n}"
                    for _attempt in range(attempts):
                        decision, reason = guard(command, cwd, sessions, sid=sid)
                        if decision != "deny" and (
                            "Attempting to create a worktree" not in reason
                        ):
                            holes.append((name, cwd.name, decision, command))
        assert not holes, holes

    def test_accepts_either_order_of_a_switch_and_a_creation_as_one(self, world, guard):
        differs = []
        for name, sessions, tree in STATES:
            cwd = getattr(world, tree)
            attempts = 3 if sessions in (QUIET, BLIND) else 1
            for consented in (False, True):
                runs = {}
                for order, command in (
                    ("create", "git worktree add ../wt f && git switch feature/x"),
                    ("switch", "git switch feature/x && git worktree add ../wt f"),
                ):
                    sid = f"{guard.sid}-{name}-{consented}-{order}"
                    if consented:
                        guard.grant(cwd, sid)
                    runs[order] = [
                        guard(command, cwd, sessions, sid=sid) for _ in range(attempts)
                    ]
                if runs["create"] != runs["switch"]:
                    differs.append((name, consented))
        assert not differs, differs

    def test_refuses_a_line_weaker_than_its_switch_or_its_creation(self, world, guard):
        weaker = []
        for name, sessions, tree in STATES:
            cwd = getattr(world, tree)
            for consented in (False, True):
                verdicts = {}
                for part, command in (
                    ("both", "git worktree add ../wt f && git switch feature/x"),
                    ("switch", "git switch feature/x"),
                    ("creation", "git worktree add ../wt f && git status"),
                ):
                    sid = f"{guard.sid}-{name}-{consented}-{part}"
                    if consented:
                        guard.grant(cwd, sid)
                    verdicts[part] = guard(command, cwd, sessions, sid=sid)[0]
                floor = max(STRICTNESS[verdicts[p]] for p in ("switch", "creation"))
                if verdicts["both"] == "allow" or STRICTNESS[verdicts["both"]] < floor:
                    weaker.append((name, consented, verdicts))
        assert not weaker, weaker

    def test_refuses_a_switch_into_the_new_worktree_where_the_shell_stands(
        self, world, guard
    ):
        for consented in (False, True):
            sid = f"{guard.sid}-{consented}"
            if consented:
                guard.grant(world.clean, sid)
            decision, reason = guard(
                "git worktree add ../x -b x && cd ../x && git switch y",
                world.clean,
                BUSY,
                sid=sid,
            )
            assert decision == "deny" and reason.startswith("Blocking this branch")
            decision, reason = guard(
                "git worktree add ../x -b x && git -C ../x switch y",
                world.clean,
                BUSY,
                sid=sid,
            )
            assert decision == ("silent" if consented else "ask"), reason

    # The Agent path.

    @pytest.mark.parametrize("lang", ["en", "ko"])
    def test_refuses_an_isolated_agent_without_counting_sessions(
        self, world, guard, lang
    ):
        guard.lang(lang)
        counted = []
        for n, sessions in enumerate((SINGLE, BUSY, QUIET, BLIND)):
            for prompt in ("review the diff", "the user asked for this [worktree-ok]"):
                got = guard(
                    "",
                    world.clean,
                    lambda top, own="", s=sessions: counted.append(top) or s,
                    sid=f"{guard.sid}-{n}",
                    tool="Agent",
                    tool_input={"isolation": "worktree", "prompt": prompt},
                )
                assert got == ("ask", AGENT_REASON[lang]), (sessions, prompt)
        assert counted == []

    def test_accepts_an_agent_with_consent_or_without_isolation(self, world, guard):
        isolated = {"isolation": "worktree", "prompt": "x"}
        assert guard("", world.clean, tool="Agent", tool_input={"prompt": "x"}) == (
            "silent",
            "",
        )
        assert guard("", world.outside, tool="Agent", tool_input=isolated) == (
            "silent",
            "",
        )
        guard.grant(world.clean)
        assert guard("", world.clean, tool="Agent", tool_input=isolated) == (
            "silent",
            "",
        )
        guard.press(world.clean, "pressed")
        assert guard(
            "", world.clean, sid="pressed", tool="Agent", tool_input=isolated
        ) == ("silent", "")
        assert guard("", world.clean, tool="Read", tool_input={}) == ("silent", "")

    # The unrecognised shapes.

    def test_accepts_a_listed_shape_in_every_tree_and_spawns_nothing(
        self, world, guard, monkeypatch
    ):
        calls = []
        real = subprocess.run
        monkeypatch.setattr(
            subprocess, "run", lambda *a, **k: calls.append(a) or real(*a, **k)
        )
        for name, sessions, tree in STATES:
            for pressed in (False, True):
                sid = f"{guard.sid}-{name}-{pressed}"
                if pressed:
                    guard.press(getattr(world, tree), sid)
                for shape in LISTED:
                    got = guard(shape, getattr(world, tree), sessions, sid=sid)
                    assert got == ("silent", ""), (name, pressed, shape, got)
        assert calls == []

    def test_refuses_an_unrecognised_shape_where_the_tree_matters(self, world, guard):
        for name, sessions, tree in STATES[:4]:
            for command, plain in UNRECOGNISED.items():
                decision, reason = guard(command, getattr(world, tree), sessions)
                switch_on_line = command.startswith("git switch")
                want = "deny" if name == "active" or switch_on_line else "ask"
                assert decision == want, (name, command, reason)
                assert STOP in reason and plain in reason, (name, command, reason)
        for command in UNRECOGNISED:
            assert guard(command, world.clean) == ("silent", ""), command
        for command, quoted in (
            ("git status && git checkout feature/x", "  · `git checkout feature/x` — "),
            ('sh -c "git switch x"', "  · `sh -c 'git switch x'` — "),
        ):
            assert quoted in guard(command, world.dirty)[1], command

    def test_refuses_the_stop_in_one_text_with_two_endings(self, world, guard):
        for lang in ("en", "ko"):
            guard.lang(lang)
            for decision, pressed in (("ask", False), ("deny", True)):
                sid = f"{guard.sid}-{lang}-{decision}"
                if pressed:
                    guard.press(world.dirty, sid)
                got = guard("git checkout feature/x", world.dirty, sid=sid)
                assert got == (
                    decision,
                    STOP_TEXT[lang] + ENDINGS[lang, decision],
                ), (lang, got)

    def test_refuses_a_stop_beside_a_switch_by_denying(self, world, guard):
        decision, reason = guard(
            "git checkout f.txt && git switch feature/x", world.dirty
        )
        assert decision == "deny" and reason.endswith(
            "Re-issue the command in a plain spelling. Run the `git switch` as a "
            "command of its own, so the branch-switch rules judge its tree."
        )
        decision, reason = guard("git switch feature/x 2>&1", world.dirty)
        assert decision == "ask" and STOP not in reason
        assert "They will follow you onto the target branch" in reason

    def test_refuses_each_shape_in_the_tree_its_segment_names(self, world, guard):
        named = (f"git -C {world.W} checkout x", f"cd {world.W} && git checkout x")
        for command in named:
            decision, reason = guard(command, world.clean)
            assert decision == "ask" and STOP in reason, command
            assert guard(command.replace(str(world.W), str(world.V)), world.dirty) == (
                "silent",
                "",
            )
        assert guard('cd "$W" && git checkout x', world.clean) == ("silent", "")
        assert guard('cd "$W" && git checkout x', world.dirty)[0] == "ask"
        nowhere = f"git -C {world.base / 'none'} checkout x"
        assert guard(nowhere, world.clean, BUSY) == ("silent", "")
        assert guard("git checkout f.txt && cd sub && git checkout x", world.dirty)[
            1
        ].startswith(STOP_TEXT["en"].split("\n")[0])

    def test_refuses_a_line_past_another_tree_that_matters(self, world, guard):
        for held in (BUSY, QUIET, BLIND):
            sessions = by_tree("W", held)
            for command in (
                f"git checkout f.txt && git -C {world.W} switch feature/x",
                f"git update-ref refs/x HEAD && cd {world.W} && git switch feature/x",
            ):
                decision, reason = guard(command, world.dirty, sessions)
                assert decision == "deny", (held, command)
                assert "Run the `git switch` as a command of its own" in reason
            decision, reason = guard(
                f"git checkout f.txt && git -C {world.W} checkout feature/x",
                world.dirty,
                sessions,
            )
            if held is BUSY:
                assert decision == "deny" and "actively working here" in reason
                assert "uncommitted tracked changes" not in reason
            else:
                assert decision == "ask" and f"`{world.W}`" in reason
                assert f"`{world.dirty}`" in reason

    @pytest.mark.parametrize("lang", ["en", "ko"])
    def test_refuses_with_each_tree_that_matters_named(self, world, guard, lang):
        guard.lang(lang)
        decision, reason = guard(
            f"git checkout f.txt && git -C {world.V} checkout feature/x",
            world.dirty,
            by_tree("V", BLIND),
        )
        assert decision == "ask"
        assert reason.startswith(TREES[lang].format(repo=world.dirty, w=world.V))

    @pytest.mark.parametrize(
        "group",
        [
            "2>&1 git -C {w} switch feature/x",
            "git -C {w} worktree &>/dev/null add ../wt b",
            "git -C {w} stash 2>&1 branch y",
            "cd {w} && git worktree 2>&1 add ../wt b",
        ],
    )
    def test_refuses_a_cut_group_in_the_tree_its_own_c_names(self, world, guard, group):
        command = group.format(w=world.W)
        decision, reason = guard(command, world.clean)
        assert decision == "ask" and STOP in reason, command
        decision, reason = guard(command, world.clean, by_tree("W", BUSY))
        assert decision == "deny" and STOP in reason, command

    @pytest.mark.parametrize("broken", ["missing", "raising"])
    def test_refuses_to_be_silent_where_the_wider_reader_is_broken(
        self, world, guard, monkeypatch, broken
    ):
        def boom(*_a, **_k):
            raise RuntimeError("a shape nobody measured")

        if broken == "missing":
            monkeypatch.setattr(wg, "wide", None)
        else:
            for reader in (
                "reparsed_texts",
                "substitution_bodies",
                "parse_git",
                "merged_view",
            ):
                monkeypatch.setattr(wg.wide, reader, boom)
        for command in (
            "sh -c 'git switch x'",
            'eval "git switch x"',
            "git log $(git switch x)",
            "2>/dev/null git switch x",
            "git worktree &>/dev/null add ../wt b",
            f"git -C {world.W} worktree 2>&1 add ../wt b",
        ):
            decision, reason = guard(command, world.dirty)
            assert decision == "ask" and "could not run" in reason, command
        if broken == "missing":
            assert guard("git status", world.dirty) == ("silent", "")
        assert guard(f"2>&1 git -C {world.W} switch x", world.clean) == ("silent", "")

    def test_refuses_a_body_nested_past_the_bound(self, world, guard, monkeypatch):
        command = "echo $(echo $(git status))"
        assert guard(command, world.dirty) == ("silent", "")
        monkeypatch.setattr(wg, "BODY_DEPTH", 1)
        decision, reason = guard(command, world.dirty)
        assert decision == "ask" and "could not run" in reason

    def test_accepts_data_no_shell_runs_as_no_command(self, world, guard):
        for command in (
            "cat > notes.txt <<'EOF'\ngit switch feature/x\nEOF",
            "cat > notes.txt <<EOF\ngit worktree add ../wt f\nEOF",
            'git commit -m "step 1; git worktree add ../wt f" # don\'t forget',
            'gh pr create --body "then; git switch feature/x"  # don\'t merge',
            "git rebase {main,feature/x}",
            "git worktree {add,} ../wt feature/x",
            "$GIT worktree add ../wt f",
            "git/ worktree add ../wt f",
            "uv run git worktree add ../wt f",
        ):
            assert guard(command, world.clean, BUSY) == ("silent", ""), command

    def test_accepts_the_tree_read_once_for_a_stop_and_a_switch(
        self, world, guard, monkeypatch
    ):
        seen = {"sessions": 0, "changes": 0}
        real = wg.tracked_changes

        def changes(cwd):
            seen["changes"] += 1
            return real(cwd)

        monkeypatch.setattr(wg, "tracked_changes", changes)
        state = lambda top, own="": (
            seen.__setitem__("sessions", seen["sessions"] + 1) or SINGLE
        )
        assert guard("git checkout README.md && git switch x", world.clean, state) == (
            "silent",
            "",
        )
        assert seen == {"sessions": 1, "changes": 1}

    # The press.

    def test_refuses_the_dirty_row_under_the_press_in_one_text(self, world, guard):
        for lang in ("en", "ko"):
            guard.lang(lang)
            for n, (sessions, command, counted) in enumerate(
                (
                    (SINGLE, "git switch feature/x", True),
                    (SINGLE, "git switch --orphan newb", True),
                    (SINGLE, "git stash && git switch feature/x", True),
                    (SINGLE, "git switch feature/x && git worktree add ../wt f", True),
                    (QUIET, "git switch other  # [shared-tree-ok]", False),
                    (BLIND, "git switch other  # [shared-tree-ok]", False),
                )
            ):
                sid = f"{guard.sid}-{lang}-{n}"
                guard.press(world.dirty, sid)
                got = guard(command, world.dirty, sessions, sid=sid)
                assert got == ("deny", dirty_deny(lang, LEADS[lang, counted])), command
        assert not os.path.exists(
            wg.worktree_consent.consent_path(str(world.dirty), f"{guard.sid}-en-3")
        )

    def test_refuses_the_dirty_row_with_the_note_the_ask_carries(self, world, guard):
        head = "Index-only residue invisible in the working tree:"
        asked = guard("git switch feature/x", world.phantom)
        guard.press(world.phantom, "pressed")
        denied = guard("git switch feature/x", world.phantom, sid="pressed")
        assert (asked[0], denied[0]) == ("ask", "deny")

        def note(text):
            lines = text.split("\n")
            first = lines.index(head)
            last = max(i for i, x in enumerate(lines) if "restore --staged" in x)
            return lines[first : last + 1]

        assert note(asked[1]) == note(denied[1])
        assert "ign.txt" in note(denied[1])[1]

    def test_refuses_with_the_press_read_from_the_sessions_own_root(self, world, guard):
        top = wg.repo_paths(str(world.W))[0]
        command = f"git -C {shlex.quote(str(world.W))} switch feature/x"
        at = f"git -C {shlex.quote(top)}"
        guard.press(world.clean)
        for lang in ("en", "ko"):
            guard.lang(lang)
            assert guard(command, world.clean) == (
                "deny",
                dirty_deny(lang, LEADS[lang, True], at),
            )
        guard.lang("en")
        guard.press(world.W)
        decision, reason = guard(command, world.clean)
        assert decision == "ask" and "Confirm to proceed" in reason

    def test_refuses_an_unrecognised_shape_under_the_press_to_the_model(
        self, world, guard
    ):
        guard.press(world.dirty)
        for command, plain in list(UNRECOGNISED.items())[:5]:
            decision, reason = guard(command, world.dirty)
            assert decision == "deny" and STOP in reason and plain in reason
            assert "AskUserQuestion" not in reason
        guard.grant(world.dirty, f"{guard.sid}-recorded")
        decision, reason = guard(
            "git checkout feature/x", world.dirty, sid=f"{guard.sid}-recorded"
        )
        assert decision == "ask" and STOP in reason

    def test_accepts_each_way_on_the_deny_names_under_git(
        self, guard, tmp_path, _repo_template
    ):
        repo = tmp_path / "repo"
        shutil.copytree(_repo_template, repo)
        guard.press(repo)
        here = git_out(repo, "branch", "--show-current")
        for first in ("git commit -am x", "git stash"):
            (repo / "f.txt").write_text(f"changed for {first}\n", encoding="utf-8")
            for command in (first, "git switch feature/x"):
                assert guard(command, repo) == ("silent", ""), command
                git(repo, *command.split()[1:])
            git(repo, "switch", "-q", here)


# The case binding `LEAVES_THE_TREE` to git: one form of each row run in a copy
# of a repository with a second commit on `feature/x` and a stash, and each
# form git runs as a switch, which must move HEAD.
FORMS = {
    "log": "log feature/x",
    "status": "status",
    "commit": "commit --allow-empty -qm x",
    "diff": "diff feature/x",
    "add": "add -A",
    "rev-parse": "rev-parse feature/x",
    "show": "show feature/x",
    "push": "push -q . feature/x:refs/heads/pushed",
    "grep": "grep one feature/x",
    "fetch": "fetch -q . feature/x:fetched",
    "clone": "clone -q . ../cloned{n}",
    "branch": "branch y feature/x",
    "merge-base": "merge-base {start} feature/x",
    "config": "config user.name x",
    "stash": "stash",
    "ls-tree": "ls-tree feature/x",
    "tag": "tag t feature/x",
    "ls-files": "ls-files",
    "merge": "merge -q --no-edit feature/x",
    "ls-remote": "ls-remote .",
    "archive": "archive -o ../a{n}.tar feature/x",
    "pull": "pull -q --no-rebase --no-edit . feature/x",
    "cat-file": "cat-file -t feature/x",
    "for-each-ref": "for-each-ref",
    "describe": "describe --always feature/x",
    "rev-list": "rev-list feature/x",
    "reset": "reset -q --hard feature/x",
    "remote": "remote add o .",
    "init": "init -q",
    "merge-tree": "merge-tree --write-tree {start} feature/x",
    "apply": "apply ../p.diff",
    "check-ignore": "check-ignore f.txt",
    "restore": "restore --source feature/x g.txt",
    "clean": "clean -fdq",
    "reflog": "reflog",
    "revert": "revert --no-edit HEAD",
    "blame": "blame f.txt",
    "rm": "rm -q --cached f.txt",
    "cherry-pick": "cherry-pick feature/x",
    "mv": "mv f.txt h.txt",
    "show-ref": "show-ref",
    "rebase": "rebase -q feature/x",
    "diff-tree": "diff-tree feature/x",
    "gc": "gc --auto",
    "format-patch": "format-patch -q -o ../p{n} {start}..feature/x",
    "count-objects": "count-objects",
    "update-index": "update-index --refresh",
    "help": "help -a",
    "shortlog": "shortlog -s feature/x",
}
SWITCHING = (
    "rebase {start} feature/x",
    "rebase --onto {start} {start} feature/x",
    "rebase --root feature/x",
    "rebase - feature/x",
    "rebase --ro feature/x",
    "rebase --end-of-options {start} -x",
    "rebase -- {start} -x",
    "stash branch y",
    "checkout feature/x",
    "switch feature/x",
)
BRACED = (
    "rebase {{{start},feature/x}}",
    "rebase --ro{{,}} feature/x",
    "stash {{branch,}} y",
    "worktree {{add,}} ../wt{n} feature/x",
)


class Test_shape_of:
    @pytest.mark.parametrize(
        "command", [c for c, s in SHAPES.items() if s in ("switch", "creation", None)]
    )
    def test_accepts_a_switch_a_creation_or_a_listed_shape(self, command):
        assert first_shape(command) == SHAPES[command]

    @pytest.mark.parametrize(
        "command", [c for c, s in SHAPES.items() if s == "unrecognised"]
    )
    def test_refuses_every_other_git_as_unrecognised(self, command):
        assert first_shape(command) == "unrecognised"

    def test_accepts_no_listed_form_that_moves_head_under_git(
        self, tmp_path, _repo_template, world, guard
    ):
        def run(d, *args, ok=0):
            done = subprocess.run(
                ["git", "-C", str(d), *args],
                capture_output=True,
                stdin=subprocess.DEVNULL,
                env={**os.environ, "GIT_EDITOR": "true", "GIT_PAGER": "cat"},
            )
            assert done.returncode == ok, (args, done.returncode, done.stderr)
            return done

        def head(d):
            return (d / ".git" / "HEAD").read_text(encoding="utf-8").strip()

        template = tmp_path / "template"
        shutil.copytree(_repo_template, template)
        start = head(template).rsplit("/", 1)[-1]
        run(template, "switch", "-q", "feature/x")
        (template / "g.txt").write_text("g\n", encoding="utf-8")
        run(template, "add", "g.txt")
        run(template, "commit", "-qm", "g")
        run(template, "switch", "-q", start)
        run(template, "update-ref", "refs/heads/-x", "HEAD")
        (template / "f.txt").write_text("changed\n", encoding="utf-8")
        (tmp_path / "p.diff").write_bytes(run(template, "diff").stdout)
        run(template, "stash", "-q")

        assert set(FORMS) == set(wg.LEAVES_THE_TREE)
        listed, moved = [], []
        for n, form in enumerate([*FORMS.values(), *SWITCHING]):
            words = form.format(start=start, n=n).split()
            if wg.shape_of(["git", *words]) == "listed":
                listed.append(form)
            copy = tmp_path / f"r{n}"
            shutil.copytree(template, copy)
            run(copy, *words, ok=1 if words[0] == "check-ignore" else 0)
            if head(copy) != head(template):
                moved.append(form)
        assert not set(listed) & set(moved)
        assert sorted(listed) == sorted(FORMS.values())
        assert sorted(moved) == sorted(SWITCHING)

        braced = [
            (n, form.format(start=start, n=n))
            for n, form in enumerate(BRACED, start=len(FORMS) + len(SWITCHING))
        ]
        for _n, text in braced:
            assert wg.shape_of(["git", *shlex.split(text)]) == "listed", text
            assert guard(f"git {text}", world.clean, BUSY) == ("silent", ""), text
        why = shell_probe("bash")
        if why is not None:
            pytest.skip(f"bash: {why}")
        acted = []
        for n, text in braced:
            copy = tmp_path / f"r{n}"
            shutil.copytree(template, copy)
            done = subprocess.run(
                ["bash", "-c", f"git -C {shlex.quote(str(copy))} {text}"],
                capture_output=True,
                stdin=subprocess.DEVNULL,
                env={**os.environ, "GIT_EDITOR": "true", "GIT_PAGER": "cat"},
            )
            assert done.returncode == 0, (text, done.stderr)
            if head(copy) != head(template) or (tmp_path / f"wt{n}").is_dir():
                acted.append(text)
        assert len(acted) == len(BRACED), acted


# --- left where they stand, for #923: they read this module's own text --------

# Phase 1 of work item 1791270162, its `phases/phase-1.md`, measurement M1: every git
# subcommand the frozen reading yields over the recorded runs, as pairs
# holding it in cut 1 / cut 2. Phase 3 re-read cut 1 on the same definition
# and found the same table.
RECORDED = {
    "log": (2858, 3064),
    "status": (2609, 2848),
    "commit": (2014, 2149),
    "diff": (2028, 2127),
    "add": (1842, 1947),
    "rev-parse": (893, 961),
    "show": (651, 756),
    "push": (573, 607),
    "checkout": (532, 576),
    "grep": (385, 454),
    "fetch": (252, 276),
    "clone": (223, 243),
    "branch": (223, 236),
    "worktree": (152, 164),
    "switch": (120, 126),
    "merge-base": (98, 104),
    "config": (84, 100),
    "stash": (95, 99),
    "ls-tree": (55, 73),
    "tag": (46, 60),
    "ls-files": (56, 58),
    "merge": (52, 55),
    "ls-remote": (44, 47),
    "archive": (43, 47),
    "pull": (43, 44),
    "cat-file": (38, 41),
    "for-each-ref": (26, 40),
    "describe": (26, 27),
    "rev-list": (23, 24),
    "reset": (23, 23),
    "remote": (17, 19),
    "init": (17, 17),
    "update-ref": (13, 13),
    "merge-tree": (7, 11),
    "apply": (8, 11),
    "check-ignore": (10, 10),
    "restore": (6, 7),
    "clean": (5, 6),
    "reflog": (6, 6),
    "revert": (6, 6),
    "blame": (3, 5),
    "rm": (5, 5),
    "cherry-pick": (4, 4),
    "mv": (1, 2),
    "show-ref": (2, 2),
    "rebase": (2, 2),
    "diff-tree": (1, 2),
    "gc": (1, 1),
    "format-patch": (0, 1),
    "count-objects": (0, 1),
    "update-index": (1, 1),
    "help": (1, 1),
    "symbolic-ref": (1, 1),
    "shortlog": (1, 1),
}
# What the frame judges does not leave the branch (`spec.md` In 5), and the
# words that are a shape of their own rather than a list entry.
MOVERS = {"switch", "checkout", "worktree", "update-ref", "symbolic-ref", "bisect"}


def test_the_list_carries_its_counts_and_nothing_unmeasured():
    """S10 of work item 1791270162. `LEAVES_THE_TREE` is exactly the recorded
    subcommands that leave the branch, each beside the count phase 1
    measured, and holds none of the movers. Red with one count changed in
    the module's comment, and with `rebase` taken off the list."""
    import inspect
    import re

    listed = re.findall(
        r'^\s+"([\w-]+)",\s+#\s+(\d+)/(\d+)',
        inspect.getsource(wg).split("LEAVES_THE_TREE = frozenset(")[1].split(")")[0],
        re.M,
    )
    counts = {sub: (int(a), int(b)) for sub, a, b in listed}
    assert set(counts) == set(wg.LEAVES_THE_TREE), sorted(
        set(counts) ^ set(wg.LEAVES_THE_TREE)
    )
    assert counts == {s: n for s, n in RECORDED.items() if s not in MOVERS}
    assert not (MOVERS & wg.LEAVES_THE_TREE)


def test_the_readings_are_gone():
    """S11 of work item 1791270162. None of the symbols `spec.md` In 4
    removes is defined, and the switch arm runs no `rev-parse`: nothing
    looks a name up. Red at `9c03ae85`, where every one was still defined."""
    import inspect

    gone = (
        "wider_only_kinds",
        "_bare_words",
        "ask_what_only_the_wider_reading_finds",
        "switch_kind",
        "SWITCH_OPTIONS",
        "_Options",
        "_long_option",
        "read_switch_words",
        "handed_words",
        "_redirection_width",
        "_REDIRECTION",
        "is_ref",
        "_verified",
        "_commit_named",
        "_object_named",
        "_one_merge_base",
        "_OBJECT_NAME",
        "tracked_in_any_remote",
        "_refs",
        "_fetched_as",
        "_the_bases_lookup",
        "_no_guess",
        "classify",
    )
    assert [name for name in gone if hasattr(wg, name)] == []
    arm = (
        wg.main,
        wg.shape_of,
        wg._segment_finding,
        wg._git_finding,
        wg._merged_findings,
        wg._command_findings,
        wg._finding_tree,
    )
    assert [f.__name__ for f in arm if "rev-parse" in inspect.getsource(f)] == []


test_census = census_case(TARGET)
