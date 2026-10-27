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

Phase 6 moved here, under their names and with their bodies, the guard's cases
of its light files: the lease and transcript readers' cases of
`tests/test_lease_liveness.py`, the activity signals of
`tests/test_worktree_guard_signals.py`, the press rows of
`tests/test_the_idle_session_rows_ask_nobody.py` and
`tests/test_a_creation_in_another_clone_asks_nobody.py`, the tree each
command is judged in from `tests/test_guard_resolves_the_tree_it_judges.py`,
the process probe of `tests/test_gates_do_not_fail_open.py`, and the guard's
half of the reader's S13 from `tests/test_what_the_reader_understands.py`.
Each runs on the `repo` fixture or a directory of its own, as it did there.

The round 9 fix pass placed in `Test_last_user_snippet` the record holding a
raw U+2028, from `tests/test_every_reader_ends_a_line_where_gfm_does.py`, a
case of this module alone. That file's case for `last_active_event_epoch`
is merged into `Test_last_active_event_epoch`'s accepting case, which hands
the reader the same raw separator inside the newest active event.
"""

import contextlib
import functools
import importlib.util
import io
import json
import ntpath
import os
import pathlib
import re
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
    BASE_TREE_CHAINS,
    LS,
    PLACEMENT_CHAINS,
    TOKEN,
    _a_dirty_w_under_a_clean_session,
    ask_entries,
    census_case,
    consent_dir,
    dirty,
    git,
    git_out,
    grant,
    guard_decision,
    iso,
    lease_dir,
    load,
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


# --- the light files' helpers, moved with their cases ----------------------------


def write_lease(repo, name, body):
    p = os.path.join(lease_dir(repo), name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(body)
    return p


def dead_pid():
    """A pid that has certainly exited — spawned and reaped here."""
    p = subprocess.Popen([sys.executable, "-c", "pass"])
    p.wait()
    return p.pid


def stale_lease(repo, name, pid):
    p = write_lease(
        repo, name, json.dumps({"ts": 1, "pid": pid, "host": socket.gethostname()})
    )
    os.utime(p, (time.time() - 3600,) * 2)
    return p


decide = functools.partial(guard_decision, wg)


def transcripts_for(monkeypatch, tmp_path, cwd):
    """The ~/.claude/projects directory the guard will scan for `cwd`.

    HOME and USERPROFILE both: expanduser reads HOME on POSIX and USERPROFILE
    on Windows, so setting one leaves the other platform pointed at the real
    home directory.
    """
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    d = tmp_path / ".claude" / "projects" / wg.project_slug(str(cwd))
    d.mkdir(parents=True)
    return d


def fresh_transcript(path):
    """A transcript whose tail is ACTIVE events — an exited session's tail
    looks exactly like this, which is the whole difficulty."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps({"type": "assistant", "timestamp": iso(1)}) + "\n")


def exited_session(repo, tmp_path, monkeypatch, sid="ended-session"):
    """The incident: a fresh transcript whose owner the lease proves is gone."""
    proj = transcripts_for(monkeypatch, tmp_path, repo)
    fresh_transcript(proj / f"{sid}.jsonl")
    write_lease(
        repo,
        sid,
        json.dumps(
            {"ts": int(time.time()), "pid": dead_pid(), "host": socket.gethostname()}
        ),
    )
    return proj


def idle_minutes(repo, own="my-session"):
    return wg.transcript_idle_minutes(
        str(repo), own, dead_ids=wg.dead_session_ids(str(repo))
    )


def only_our_own_claude(monkeypatch, fake_pid=424242, *others):
    """Make the process scan work and find no OTHER session — the incident.

    `sessions_in_tree` returns unreliable unless it can spot its own process,
    and the test runner is not named `claude`. Feeding the scan one pid and
    putting that pid in the ancestor set reproduces the state at the denial:
    a scan that worked, correctly finding nobody else.
    """
    real = wg.subprocess.run
    listing = "".join(f"{p} claude\n" for p in (fake_pid, *others))

    def fake(cmd, *a, **k):
        if list(cmd[:2]) == ["ps", "-axo"]:
            return subprocess.CompletedProcess(cmd, 0, listing, "")
        return real(cmd, *a, **k)

    monkeypatch.setattr(wg.subprocess, "run", fake)
    monkeypatch.setattr(wg, "ancestors", lambda pid: {fake_pid})


def write_jsonl(path, events):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(e) + "\n" for e in events)


def jsonl(path, events):
    """JSON Lines as a JavaScript writer emits them: a U+2028 inside a
    string stays raw, which JSON permits."""
    path.write_text(
        "".join(json.dumps(e, ensure_ascii=False) + "\n" for e in events),
        encoding="utf-8",
    )


def project_dir(monkeypatch, tmp_path, cwd):
    # os.path.expanduser("~") reads HOME on POSIX but USERPROFILE on
    # Windows (ntpath.expanduser never looks at HOME) -- setting only one
    # leaves the other platform resolving "~" to the real home directory.
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    d = tmp_path / ".claude" / "projects" / wg.project_slug(str(cwd))
    d.mkdir(parents=True)
    return d


def agent_decide(monkeypatch, capsys, repo, tool_input, sessions=([], [], True)):
    monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": sessions)
    monkeypatch.setattr(
        wg,
        "load_input",
        lambda: {
            "tool_name": "Agent",
            "session_id": "me",
            "tool_input": tool_input,
            "cwd": str(repo),
        },
    )
    try:
        wg.main()
    except SystemExit:
        pass
    out = capsys.readouterr().out.strip()
    if not out:
        return "silent", ""
    d = json.loads(out)["hookSpecificOutput"]
    return d["permissionDecision"], d["permissionDecisionReason"]


# The press rows (#896 and #903): the switch ladder's two choice rows and the
# creation ladder's two in another clone ask nobody under `automation`.


@pytest.fixture
def wko(monkeypatch):
    """The guard loaded with Korean text."""
    monkeypatch.setenv("SPECSEAL_LANG", "ko")
    return load_hook_module("worktree-guard.py", "wg_896_ko")


def judge(module, monkeypatch, capsys, cwd, command, sessions, session_id="me"):
    """MODULE's decision and reason for COMMAND issued from CWD, with the
    session count stubbed to SESSIONS; `silent` where nothing printed."""
    monkeypatch.setattr(module, "sessions_in_tree", lambda top, own="": sessions)
    monkeypatch.setattr(
        module,
        "load_input",
        lambda: {
            "tool_name": "Bash",
            "session_id": session_id,
            "tool_input": {"command": command},
            "cwd": str(cwd),
        },
    )
    try:
        module.main()
    except SystemExit:
        pass
    out = capsys.readouterr().out.strip()
    if not out:
        return "silent", ""
    d = json.loads(out)["hookSpecificOutput"]
    return d["permissionDecision"], d["permissionDecisionReason"]


IDLE_LINES = {
    "en": "    pid 222 (Terminal terminal)  /tree\n"
    "        terminal in/out 6.7h ago · transcript activity 1.5h ago",
    "ko": "    pid 222 (Terminal 터미널)  /tree\n"
    "        터미널 입력/출력 6.7시간 전 · 작업 기록(트랜스크립트) 1.5시간 전",
}


def situation(lang, row, idle_min):
    """Each switch row's opening, as it reads attended: row 1-b's header and
    its idle sessions, and row 2's cannot-tell sentence."""
    if row == "idle":
        return {
            "en": "Other Claude sessions may exist in this tree, but none of them "
            f"can be shown to be working: no input or transcript for {idle_min}+ "
            "minutes, or a lease whose owning session cannot be identified.\n",
            "ko": "이 트리에 다른 Claude 세션이 있을 수 있으나, 작업 중임을 확인할 수 "
            f"있는 것은 없습니다 — {idle_min}분 이상 활동(키 입력·작업 기록)이 없거나, "
            "lease 를 남긴 세션이 누구인지 확인되지 않습니다.\n",
        }[lang] + IDLE_LINES[lang]
    return {
        "en": "Cannot determine whether other sessions are working in this tree "
        "(process inspection unavailable in this environment).",
        "ko": "이 트리에서 다른 세션이 작업 중인지 확인할 수 없습니다(이 환경에서는 "
        "프로세스 조회가 불가능합니다).",
    }[lang]


def ways_on(lang, git, wt_root):
    """What follows the opening under the press where the split's creation
    is consented: no question, the split as plain commands, working there by
    path, and the re-issue sentence. The why-sentence is the press's, the
    one the session's own clone reads."""
    if lang == "en":
        return (
            "This session's person pressed `automation` on the routing "
            "question, so this guard puts no question to them, and none is to "
            "be put to them in its place.\n"
            "\n"
            "The way on that needs nobody is to split into a worktree. That "
            "answer already consents to creating one, so these commands pass "
            "as written:\n"
            "\n"
            "  # check an existing branch out into a worktree\n"
            f"  {git} worktree add {wt_root}/<branch> <branch>\n"
            "\n"
            "  # or create a new branch off the latest origin/main\n"
            f"  {git} fetch origin\n"
            f"  {git} worktree add {wt_root}/<name> -b <branch> origin/main\n"
            "\n"
            "Then work in that tree by path from this session: `git -C` with "
            f"the path the creation named, `{wt_root}/<branch>` or "
            f"`{wt_root}/<name>`, for git, and an absolute path for every "
            "edit. A branch already checked out in a worktree needs no "
            "switch: work in that worktree.\n"
            "\n"
            "Re-issuing this command unchanged meets this same refusal."
        )
    return (
        "이 세션의 사용자가 라우팅 질문에서 `automation` 을 눌렀습니다. 그래서 "
        "이 guard 는 사용자에게 아무것도 묻지 않으며, 다른 방법으로 대신 물어서도 "
        "안 됩니다.\n"
        "\n"
        "사람이 없어도 되는 길은 worktree 로 분리하는 것입니다. 그 답이 worktree "
        "생성에 이미 동의했으므로, 아래 명령은 쓰인 그대로 통과합니다.\n"
        "\n"
        "  # 기존 브랜치를 worktree로 꺼내기\n"
        f"  {git} worktree add {wt_root}/<branch> <branch>\n"
        "\n"
        "  # 새 브랜치를 최신 origin/main 기준으로 생성 (저장소 정책)\n"
        f"  {git} fetch origin\n"
        f"  {git} worktree add {wt_root}/<name> -b <branch> origin/main\n"
        "\n"
        "그런 다음 이 세션에서 그 트리를 경로로 지정해 작업하세요. git 은 "
        f"생성할 때 쓴 경로(`{wt_root}/<branch>` 또는 `{wt_root}/<name>`)를 "
        "`git -C` 로 지정하고, 파일 편집은 절대 경로로 합니다. 이미 어느 "
        "worktree 에 체크아웃된 브랜치라면 전환할 필요 없이 그 worktree 에서 "
        "작업하세요.\n"
        "\n"
        "이 명령을 그대로 다시 실행하면 같은 거부를 받습니다."
    )


def elsewhere(lang):
    """What follows the opening under the press when the switch's tree is in
    another clone than the session's own and this session holds no creation
    record there: the press is consent only in the clone it was given in, so
    no split is named (round 1, red 1)."""
    if lang == "en":
        return (
            "This session's person pressed `automation` on the routing "
            "question, so this guard puts no question to them, and none is to "
            "be put to them in its place.\n"
            "\n"
            "That answer was read in this session's own clone, and it consents "
            "to creating a worktree only in a clone it was given in. This tree "
            "is in another clone, where this session has created no worktree, "
            "so a split of it may be put to a person, and this guard names no "
            "way on here. Leave this switch to a session working in the clone "
            "this tree is in.\n"
            "\n"
            "Re-issuing this command unchanged meets this same refusal."
        )
    return (
        "이 세션의 사용자가 라우팅 질문에서 `automation` 을 눌렀습니다. 그래서 "
        "이 guard 는 사용자에게 아무것도 묻지 않으며, 다른 방법으로 대신 물어서도 "
        "안 됩니다.\n"
        "\n"
        "그 답은 이 세션의 클론에서 읽은 것이고, 답을 받은 클론에서만 worktree "
        "생성에 동의합니다. 이 트리는 다른 클론에 있고 이 세션은 그 클론에서 "
        "worktree 를 만든 적이 없으므로, 이 트리를 분리하면 사람에게 물을 수 "
        "있습니다. 그래서 이 guard 는 여기서 갈 길을 알려 주지 않습니다. 이 전환은 "
        "이 트리가 있는 클론에서 작업하는 세션에 맡기세요.\n"
        "\n"
        "이 명령을 그대로 다시 실행하면 같은 거부를 받습니다."
    )


def unattended(module, lang, row, repo, git="git"):
    """The whole deny for ROW, for a switch in REPO."""
    wt_root = module.repo_paths(str(repo))[1]
    return situation(lang, row, module.IDLE_MIN) + "\n\n" + ways_on(lang, git, wt_root)


def assert_names_nobody(reason):
    for word in ("AskUserQuestion", "[shared-tree-ok]", "[worktree-ok]"):
        assert word not in reason, (word, reason)


def no_marker(module, repo, session="me"):
    """True when no switch-side choice marker was written for SESSION in
    REPO."""
    gd = module.git_dir(str(repo))
    return not (pathlib.Path(gd) / module.CHOICE_DIR / "switch" / session).exists()


ROWS = {"idle": ([], IDLE, True), "unusable": ([], [], False)}


def git_ok(*args):
    r = subprocess.run(
        ["git", *args], capture_output=True, encoding="utf-8", errors="replace"
    )
    assert r.returncode == 0, (args, r.stdout, r.stderr)
    return r.stdout.strip()


def creation_situation(lang, row, idle_min):
    """Each creation row's opening, as it reads attended: the origin, then
    row 3's only-idle sentence and its idle sessions, or row 4's cannot-tell
    sentence."""
    origin = {
        "en": "Attempting to create a worktree with `git worktree add`.\n",
        "ko": "`git worktree add` 로 worktree를 만들려 합니다.\n",
    }[lang]
    if row == "idle":
        return (
            origin
            + {
                "en": "The only other sessions here have shown no activity (input "
                f"or transcript) for {idle_min}+ minutes — if they are forgotten "
                "tabs this is effectively single-stream work and plain `git "
                "switch` beats a worktree.\n",
                "ko": f"이 트리의 다른 세션은 {idle_min}분 이상 활동(키 입력·작업 "
                "기록)이 없는 것뿐입니다 — 잊힌 탭이면 사실상 단건 작업이라 worktree "
                "없이 `git switch` 가 낫습니다.\n",
            }[lang]
            + IDLE_LINES[lang]
        )
    return (
        origin
        + {
            "en": "Cannot determine whether other sessions are working here (ps/lsof "
            "unavailable), so no automatic verdict.",
            "ko": "동시 세션 여부를 확인할 수 없어(ps/lsof 사용 불가) 자동 판정을 못 합니다.",
        }[lang]
    )


def creation_elsewhere(lang):
    """What follows a creation row's opening under the press: #896's press
    sentence, why no way on is named for a creation in a clone the press was
    not given in, and #896's re-issue sentence."""
    if lang == "en":
        return (
            "This session's person pressed `automation` on the routing "
            "question, so this guard puts no question to them, and none is to "
            "be put to them in its place.\n"
            "\n"
            "That answer was read in this session's own clone, and it consents "
            "to creating a worktree only in a clone it was given in. This tree "
            "is in another clone, where this session has created no worktree, "
            "and nobody is at the keyboard to choose between splitting it and "
            "switching in its shared tree, so this guard names no way on here. "
            "Leave this creation to a session working in the clone this tree "
            "is in.\n"
            "\n"
            "Re-issuing this command unchanged meets this same refusal."
        )
    return (
        "이 세션의 사용자가 라우팅 질문에서 `automation` 을 눌렀습니다. 그래서 "
        "이 guard 는 사용자에게 아무것도 묻지 않으며, 다른 방법으로 대신 물어서도 "
        "안 됩니다.\n"
        "\n"
        "그 답은 이 세션의 클론에서 읽은 것이고, 답을 받은 클론에서만 worktree "
        "생성에 동의합니다. 이 트리는 다른 클론에 있고 이 세션은 그 클론에서 "
        "worktree 를 만든 적이 없습니다. 이 트리를 분리할지 공용 트리에서 전환할지 "
        "고를 사람도 자리에 없으므로, 이 guard 는 여기서 갈 길을 알려 주지 "
        "않습니다. 이 생성은 이 트리가 있는 클론에서 작업하는 세션에 맡기세요.\n"
        "\n"
        "이 명령을 그대로 다시 실행하면 같은 거부를 받습니다."
    )


def creation_unattended(lang, row):
    """The whole deny for ROW, for a creation in another clone."""
    return (
        creation_situation(lang, row, wg.IDLE_MIN) + "\n\n" + creation_elsewhere(lang)
    )


@pytest.fixture
def other(repo, tmp_path):
    """A second clone of the same history, beside `repo`, and its root."""
    d = tmp_path / "other-repo"
    shutil.copytree(repo, d)
    return wg.repo_paths(str(d))[0]


def creation(top, tail=""):
    return f"git -C {shlex.quote(top)} worktree add ../wt feature/x{tail}"


def no_create_marker(module, top, session="me"):
    """True when no creation-side choice marker was written for SESSION."""
    gd = module.git_dir(top)
    return not (pathlib.Path(gd) / module.CHOICE_DIR / "create" / session).exists()


def no_record(*tops, session="me"):
    """True when neither clone holds a consent record for SESSION."""
    return not any((consent_dir(t) / session).exists() for t in tops)


def windows_creation(monkeypatch, capsys, projects, repo, other):
    """S11's body, with nothing stubbed but the payload: the creation in the
    other clone under this session's press, as `main` judges it."""
    write_transcript(projects, "me", ask_entries(repo))
    monkeypatch.setattr(
        wg,
        "load_input",
        lambda: {
            "tool_name": "Bash",
            "session_id": "me",
            "tool_input": {"command": creation(other)},
            "cwd": str(repo),
        },
    )
    try:
        wg.main()
    except SystemExit:
        pass
    d = json.loads(capsys.readouterr().out)["hookSpecificOutput"]
    return d["permissionDecision"], d["permissionDecisionReason"]


# The tree each command is judged in: the session's cwd, a `-C`, a `cd`, and
# the base's frozen walk (#689, #826, #868).


def run(monkeypatch, capsys, command, cwd, sessions=([], [], True)):
    """Run the hook, returning (decision, reason, tree_it_judged): the last
    tree the sessions were read for. SESSIONS is the answer for every tree,
    or a function of the tree that gives it."""
    seen = {}

    def stub(top, own=""):
        seen["top"] = top
        return sessions(top) if callable(sessions) else sessions

    monkeypatch.setattr(wg, "sessions_in_tree", stub)
    monkeypatch.setattr(
        wg,
        "load_input",
        lambda: {
            "tool_name": "Bash",
            "session_id": "me",
            "tool_input": {"command": command},
            "cwd": str(cwd),
        },
    )
    try:
        wg.main()
    except SystemExit:
        pass
    out = capsys.readouterr().out.strip()
    decision = (
        "silent"
        if not out
        else json.loads(out)["hookSpecificOutput"]["permissionDecision"]
    )
    reason = (
        ""
        if not out
        else json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
    )
    return decision, reason, seen.get("top")


# Round 2 of work item 1790550712, finding 1, as a class: every command a
# reason tells the person to run acts on the shell's repository unless it names
# another. Where the tree judged is not the shell's, each one carries `-C` and
# the tree's root; where it is, the text is what it always was.
PRINTED_COMMAND = re.compile(
    r"git(?P<at> -C \S+)? (fetch origin|switch -c <|switch <branch>|worktree add [^`]"
    r"|restore)"
)


def printed_commands(reason):
    return [m for m in PRINTED_COMMAND.finditer(reason)]


def _the_tree_the_guard_judges_a_creation_in(monkeypatch, capsys, command, cwd):
    """The `top` the guard hands `judge_creation` for COMMAND, or None."""
    seen = []

    def judged(_command, _cwd, top, *_rest, **_kw):
        seen.append(top)
        raise SystemExit(0)

    monkeypatch.setattr(wg, "judge_creation", judged)
    run(monkeypatch, capsys, command, cwd)
    return seen[0] if seen else None


# A segment only #674's reading reads as git, in FRONT of one `86256492` read
# (round 1 of 1790745049, red 1). The guard takes the first segment of each
# kind, so while it read with #674's `parse_git` the wider segment took the
# place of the one the base judged. An ACTIVE session sits in any tree the
# stub is asked about, so `top` is what tells the two apart.
WIDER_FIRST = (
    "2>/dev/null git switch feature/x; cd w && git switch feature/x",
    "git 2>/dev/null switch feature/x; cd w && git switch feature/x",
    "nocorrect git switch feature/x; cd w && git switch feature/x",
    "repeat 1 git switch feature/x; cd w && git switch feature/x",
    "cd clean && 2>/dev/null git switch feature/x; cd ../w && git switch feature/x",
)

# zsh's precommand words and short loop in front of git (round 1 of
# 1790745049, yellow 2). #674's `command_word` reads them as runners, so the
# build read each as git with an unresolved directory; `86256492` read none of
# them as git.
ZSH_PREFIXED = (
    "cd w && repeat 2 git {verb}",
    "cd w && for i (1) git {verb}",
    "cd w && noglob git {verb}",
    "cd w && nocorrect git {verb}",
    # Round 2 of 1790745049, white 3: `542f920b`'s guard read `foreach` too.
    "cd w && foreach i (1) git {verb}; end",
)

SWITCH = "git switch feature/x"

# #686's seven: a `cd` the frozen walk cannot follow, or follows confidently
# to the wrong place, before the switch. bash switches the dirty `w`; the
# guard judges the clean session tree and says nothing.
UNPLACED = {
    "builtin cd": f"builtin cd w && {SWITCH}",
    "command cd": f"command cd w && {SWITCH}",
    "time cd": f"time cd w && {SWITCH}",
    "pushd": f"pushd w && {SWITCH}",
    "noglob cd": f"noglob cd w && {SWITCH}",
    "cd to an unset variable": f'cd "$W" && {SWITCH}',
    "2>&1 cd": f"2>&1 cd w && {SWITCH}",
    # #854 (round 3 of work item 1791270162, white 3): the splitter cuts
    # `cd w 2>&1` at its `&` and the walk keeps the directory before the
    # `cd`; an `if` body's directory is unresolved. bash runs both in `w`.
    "cd 2>&1": f"cd w 2>&1 && {SWITCH}",
    "a cut git in an if body": f"cd w && if true; then 2>&1 {SWITCH}; fi",
}

WIDER_ONLY = {
    "git 2>&1 worktree add": ("cd w && git 2>&1 worktree add ../wt b", "creation"),
    # Run in `w` since #826: in the clean session tree an unrecognised shape
    # says nothing, which is row 5 of *A. Branch switch* and not the reading under test.
    "--config-env, a creation": (
        "cd w && git --config-env k=v worktree add ../wt b",
        "creation",
    ),
    "2>/dev/null nice -n 5 git switch": (
        f"cd w && 2>/dev/null nice -n 5 {SWITCH}",
        "switch",
    ),
    "--config-env, a switch": ("cd w && git --config-env k=v switch x", "switch"),
    # Round 2 of 1790993140: a redirection glued to the subcommand's end.
    # bash runs each (executed by the round); the frozen parser reads
    # `switch>/dev/null` as the subcommand, which is the redirection shape
    # since #826, and `worktree add>/dev/null` as a `worktree` whose `add` a
    # redirection hides (`_hidden_mover`).
    "a redirection glued to switch": (
        "cd w && git switch>/dev/null feature/x",
        "switch",
    ),
    "a redirection glued to checkout": (
        "cd w && git checkout>/dev/null -b y",
        "switch",
    ),
    "a redirection glued to add": (
        "cd w && git worktree add>/dev/null ../wt b",
        "creation",
    ),
    # #737. The splitter cuts `&>` at `&`; bash runs each as a switch
    # (executed). The frozen reading reads the `git switch` or `git checkout`
    # in front of the cut, so the first meets the ladder and the second is
    # unrecognised.
    "&> between switch and its name": (
        "cd w && git switch &>/dev/null feature/x",
        "switch",
    ),
    "&> between checkout and its name": (
        "cd w && git checkout &>/dev/null feature/x",
        "switch",
    ),
    # #737. bash runs it as a creation (executed); silent at `2b1dcb1f`,
    # where `2>/dev/null` was read as `worktree`'s first positional.
    "a redirection between worktree and add": (
        "cd w && git worktree 2>/dev/null add ../wt b",
        "creation",
    ),
    **{
        f"zsh: {shape.split('&& ')[1]}": (
            shape.format(verb="switch feature/x"),
            "switch",
        )
        for shape in ZSH_PREFIXED
    },
}


def _redirections():
    """Every redirection `hooks/lib/cmdline.py`'s `_REDIRECTION` names, as (operator,
    target) pairs, each operator once bare and, where it is not `&`-led, with
    a number and with bash 4.1's `{fd}` in front. Derived from the pattern, so
    an operator the reader learns is a new case the day it is added.

    Each operator takes every kind of target it has: a duplicating one a
    descriptor, `-` to close it and `1-` to move it, and every other one but
    a here-document's a word and the word `-`. A target ending in `-` is
    what `<<-` looks like, and round 1 of work item 1791270162 found
    `git worktree 2>&- add …` and `git worktree >- add …` listed where bash
    creates the worktree, because the generator gave `>&` and `<&` the
    target `1` alone."""
    pattern = wg.wide._REDIRECTION.pattern
    assert pattern.endswith(")"), pattern
    operators = pattern[pattern.rindex("(?:") + 3 : -1]
    pairs = []
    for op in (o.replace("\\", "") for o in re.split(r"(?<!\\)\|", operators)):
        if op in ("<<", "<<-"):
            targets = ["EOF"]
        elif op.endswith("&"):
            targets = ["1", "-", "1-"]
        else:
            targets = ["word" if op == "<<<" else "/dev/null", "-"]
        fds = [""] if op.startswith("&") else ["", "2", "{fd}"]
        pairs += [(fd + op, target) for fd in fds for target in targets]
    return pairs


# Since #826: a verb that can move a branch or add a worktree, and a listed
# verb whose listing rests on a word after the subcommand.
MOVING = (
    "switch feature/x",
    "checkout feature/x",
    "checkout -b y",
    "worktree add ../wt b",
    "stash branch x",
)
LISTED_VERBS = (
    "status",
    "checkout -- README.md",
    "worktree list",
    "stash",
    "stash push -m wip",
)


def _placed(verb):
    """`git <verb>` with every redirection `_redirections` gives, at every
    position, glued to the word before it and spaced, its target glued and
    spaced -- as `(command, at, glued, operator, spaced_target)`, where `at`
    is the index of the word of `git <verb>` the redirection stands before.

    A number or a `{fd}` is a descriptor only as a word of its own, so those
    are spaced: glued, bash hands it to git inside the word before
    (`--2>&1` is the option `--2`), which is another verb."""
    words = ["git", *verb.split()]
    for op, target in _redirections():
        gluable = not op[0].isdigit() and not op.startswith("{")
        for at in range(len(words) + 1):
            for glued in (False, True) if at and gluable else (False,):
                for spaced_target in (False, True):
                    redirection = op + (" " if spaced_target else "") + target
                    head = " ".join(words[:at])
                    tail = " ".join(words[at:])
                    joint = "" if glued else " "
                    command = (head + joint + redirection).lstrip()
                    command = (command + " " + tail).rstrip()
                    if target == "EOF":
                        command += "\nEOF"
                    yield command, at, glued, op, spaced_target


def _read_by_the_guard(command):
    """What `main` acts on in COMMAND before any tree is read: each switch
    and creation the frozen segments hold, and every unrecognised shape, from
    a segment, a group a `&` cut apart, a substitution body or an
    untokenizable command. Empty where every git in it is listed."""
    text = wg._judgment_text(command)
    items, clean = wg._tokenize_with_separators(text)
    found = []
    for _sep, tokens in items:
        shape, finding = wg._segment_finding(tokens)
        if shape in ("switch", "creation"):
            found.append(shape)
        elif finding is not None:
            found.append(finding)
    found += [merged[1] for merged in wg._merged_findings(items)]
    return found + wg._command_findings(text, clean)


# One shape per position of Axis 3 of work item 1791119071, through `main()`,
# over the dirty `w`.
PLACED_SWITCHES = {
    "R0, a stuck value": "git checkout -by",
    "R1, between checkout and its name": "git checkout 2>/dev/null feature/x",
    "R3, glued to the name": "git checkout feature/x>/dev/null",
    "R4, between -b and its value": "git checkout -b 2>/dev/null y",
    "R4, glued to -b": "git checkout -b>/dev/null y",
    "R5, after the name": "git switch feature/x 2>/dev/null",
}

# #780: a consent token inside a here-document body is not read. `has_token`
# reads a token only where the command as written AND the command with its
# here-document bodies taken out carry it, the rule `hooks/lib/tokens.py#given`
# has kept for the commit gate since #773. Each body below is one a consent
# read must not take a token from: the one shape `hooks/lib/one_heredoc.py`
# matches byte for byte, and a body behind an unquoted delimiter, which
# `hooks/lib/cmdline.py` finds.
BODY_TOKENS = {
    "[shared-tree-ok] in the one shape's body": (
        "python3 - <<'EOF'\n# [shared-tree-ok]\nEOF\ngit switch feature/x",
        "[shared-tree-ok]",
    ),
    "[shared-tree-ok] behind an unquoted delimiter": (
        "cat <<EOF >/dev/null\n[shared-tree-ok]\nEOF\ngit switch feature/x",
        "[shared-tree-ok]",
    ),
    "[worktree-ok] in the one shape's body": (
        "python3 - <<'EOF'\n# [worktree-ok]\nEOF\ngit worktree add ../wt -b y",
        "[worktree-ok]",
    ),
    "[worktree-ok] behind an unquoted delimiter": (
        "cat <<EOF >/dev/null\n[worktree-ok]\nEOF\ngit worktree add ../wt -b y",
        "[worktree-ok]",
    ),
}

# The documented forms, each beside a here-document in the same command.
TYPED_BESIDE_A_BODY = {
    "a trailing comment before a body": (
        "git switch feature/x  # [shared-tree-ok]\ncat <<'EOF' >/dev/null\nb\nEOF",
        "[shared-tree-ok]",
    ),
    "a trailing comment after the one shape's terminator": (
        "python3 - <<'EOF'\nprint(1)\nEOF\ngit switch feature/x  # [shared-tree-ok]",
        "[shared-tree-ok]",
    ),
    "a bare word after the command": (
        "git switch feature/x [shared-tree-ok]\ncat <<EOF >/dev/null\nb\nEOF",
        "[shared-tree-ok]",
    ),
    "a bare word before the command": (
        "cat <<EOF >/dev/null\nb\nEOF\n: [shared-tree-ok]; git switch feature/x",
        "[shared-tree-ok]",
    ),
    "inside a subshell": (
        "(git worktree add ../wt f [worktree-ok])\ncat <<EOF >/dev/null\nb\nEOF",
        "[worktree-ok]",
    ),
    "a comment after a creation, a body behind it": (
        "git worktree add ../wt f  # [worktree-ok]\ncat <<'EOF' >/dev/null\nb\nEOF",
        "[worktree-ok]",
    ),
}


def _raises(command):
    raise RuntimeError("the wider body reader is broken")


def _a_guard_whose_wider_reader_exits_at_load(monkeypatch, tmp_path):
    """The guard loaded from a copy of `hooks/` whose `cmdline.py` raises
    `SystemExit` at load, as
    `test_a_wider_reader_that_exits_at_load_costs_only_the_question` makes
    it, so `tokens.without_bodies` fails on its own import."""
    hooks = tmp_path / "hooks"
    shutil.copytree(os.path.join(os.path.dirname(__file__), "..", "hooks"), hooks)
    (hooks / "lib" / "cmdline.py").write_text("raise SystemExit(3)\n", encoding="utf-8")
    monkeypatch.delitem(sys.modules, "cmdline", raising=False)
    monkeypatch.syspath_prepend(str(hooks / "lib"))
    spec = importlib.util.spec_from_file_location(
        "wg_exiting_reader_780", hooks / "worktree-guard.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.wide is None
    return module


def _the_bases_token_read(command, token):
    """`a3aa139a`'s `has_token`, verbatim: the command as written."""
    segments, _clean = wg._tokenize(command)
    return any(
        tok == token or tok.strip("()") == token for toks in segments for tok in toks
    )


# Commands whose raw text the frozen splitter cannot finish, while the same
# text with its body taken out splits: a token there is one the command as
# written never offered (`plan.md` F, #773's reason for its AND).
UNREADABLE_UNTIL_THE_BODY_GOES = (
    "cat <<'EOF' >/dev/null\nit's\nEOF\ngit switch feature/x  # [shared-tree-ok]",
    "cat <<EOF >/dev/null\ndon't\nEOF\ngit worktree add ../wt f  # [worktree-ok]",
)

TOKEN_COMMANDS = (
    *(command for command, _ in BODY_TOKENS.values()),
    *(command for command, _ in TYPED_BESIDE_A_BODY.values()),
    *UNREADABLE_UNTIL_THE_BODY_GOES,
    "git switch feature/x  # [shared-tree-ok]",
    "git switch feature/x && echo done  # [shared-tree-ok]",
    "git switch feature/x && echo 'we documented [shared-tree-ok] today'",
    "git switch x && echo the [shared-tree-ok] token is documented",
    "git worktree add ../wt f  # [worktree-ok]",
    'git worktree add ../wt -b b origin/main && echo "wip; go"  # [worktree-ok]',
    'git worktree add ../wt f && echo "we agreed on [worktree-ok] yesterday',
    "git worktree add ../wt f  # [worktree-ok] but don't",
    "(git worktree add ../wt f [worktree-ok])",
    "git switch x [shared-tree-ok])",
)


def _a_dirty_clone_beside(repo, tmp_path):
    other = tmp_path / "other"
    shutil.copytree(repo, other)
    (other / "f.txt").write_text("changed on purpose\n", encoding="utf-8")
    return other


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

    def test_bad_idle_override_falls_back_instead_of_crashing(self, monkeypatch):
        # An unparseable override used to raise at import time; the hook then
        # exited non-zero, which Claude Code reads as "no verdict" — one typo
        # silently disabled the guard.
        from conftest import load_hook_module

        for bad in ("abc", "", "-3", "0"):
            monkeypatch.setenv("WORKTREE_GUARD_IDLE_MIN", bad)
            mod = load_hook_module("worktree-guard.py", f"wg_idle_{bad or 'empty'}")
            assert mod.IDLE_MIN == 5, bad
        monkeypatch.setenv("WORKTREE_GUARD_IDLE_MIN", "12")
        assert load_hook_module("worktree-guard.py", "wg_idle_ok").IDLE_MIN == 12

    def test_project_slug_encodes_dots_and_slashes(self):
        assert wg.project_slug("/Users/x/api.example.com") == "-Users-x-api-example-com"

    # --- real OS probes: these helpers are stubbed in every decision test,
    # so without these cases they never execute on any platform, CI included

    def test_proc_cwd_reports_this_process_real_cwd(self):
        got = wg.proc_cwd(os.getpid())
        if got is None:
            if os.path.isdir("/proc"):
                pytest.fail("/proc exists but proc_cwd returned None")
            pytest.skip("no /proc on this platform and lsof unavailable")
        assert os.path.realpath(got) == os.path.realpath(os.getcwd())

    def test_proc_cwd_sees_another_process_without_lsof(self, monkeypatch, tmp_path):
        # The Linux path must stand on its own: with lsof unavailable, a session
        # working in another tree still has to be visible, or the guard silently
        # decides the tree is single-stream.
        if not os.path.isdir("/proc"):
            pytest.skip("/proc-only behavior")
        monkeypatch.setattr(
            wg.subprocess,
            "run",
            lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError("lsof")),
        )
        p = subprocess.Popen(
            [sys.executable, "-c", "import time; time.sleep(30)"], cwd=str(tmp_path)
        )
        try:
            assert os.path.realpath(wg.proc_cwd(p.pid)) == os.path.realpath(
                str(tmp_path)
            )
        finally:
            p.kill()
            p.wait()

    def test_ancestors_includes_self_and_parent(self):
        a = wg.ancestors(os.getpid())
        assert os.getpid() in a
        if sys.platform == "win32":
            pytest.skip("ancestors() walks `ps`, which Windows doesn't have")
        if os.getppid() > 1:
            assert os.getppid() in a, "parent pid missing — ps parsing is broken"

    def test_parse_git_reports_the_chdir_it_used_to_only_skip(self):
        sub, args, chdirs = wg.parse_git(["git", "-C", "/srv/app", "switch", "topic"])
        assert (sub, args) == ("switch", ["topic"])
        assert chdirs == ["/srv/app"], "the value that decides WHICH repo was dropped"

    def test_repeated_chdir_composes_like_git_does(self, tmp_path):
        base = str(tmp_path)
        assert wg.apply_chdir(base, ["a", "b"]) == os.path.join(base, "a", "b")
        absolute = "C:\\abs" if os.name == "nt" else "/abs"
        assert wg.apply_chdir(base, [absolute]) == os.path.normpath(absolute)
        assert wg.apply_chdir(base, []) == os.path.normpath(base)

    def test_the_redirections_are_read_from_the_reader(self):
        """The generator below is only as wide as this list, and as its targets:
        a closed and a moved descriptor, and a word ending in `-`, among them."""
        pairs = _redirections()
        ops = {op for op, _target in pairs}
        assert {"&>", "&>>", ">&", "<&", "2>", "{fd}>", "<<<", ">|", ">!"} <= ops, ops
        assert len(ops) == 2 + 12 * 3, sorted(ops)
        assert {
            ("2>&", "-"),
            (">&", "1-"),
            ("<&", "-"),
            (">", "-"),
            ("&>", "-"),
        } <= set(pairs), pairs

    def test_a_wider_reader_that_exits_at_load_leaves_the_guard_reading(
        self, monkeypatch, tmp_path
    ):
        """Round 1 of 1790993140, white 5. A `hooks/lib/cmdline.py` whose body raises
        `SystemExit` is a failure `hooks/dispatch.py` catches beside `Exception`,
        and the guard's import catches it too, so the guard still loads and keeps
        its own rows. Seen red with `except Exception:` alone.

        Since #826 what it keeps is the frozen reading's shapes, and a git only
        the missing reader could have read is the bare word's finding, a stop
        where the tree matters (`tests/test_worktree_guard.py`'s
        `test_refuses_to_be_silent_where_the_wider_reader_is_broken` holds the
        verdicts). It asserted candidate C's empty answer."""
        hooks = tmp_path / "hooks"
        shutil.copytree(os.path.join(os.path.dirname(__file__), "..", "hooks"), hooks)
        (hooks / "lib" / "cmdline.py").write_text(
            "raise SystemExit(3)\n", encoding="utf-8"
        )
        monkeypatch.delitem(sys.modules, "cmdline", raising=False)
        monkeypatch.syspath_prepend(str(hooks / "lib"))
        spec = importlib.util.spec_from_file_location(
            "wg_exiting_reader", hooks / "worktree-guard.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        assert module.wide is None
        assert module.shape_of(["git", "switch", "x"]) == "switch"
        assert module.shape_of(["noglob", "git", "switch", "x"]) == "unrecognised"


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

    def test_a_windows_path_survives_tokenizing(self):
        """POSIX-mode shlex eats `\\`, which is the Windows path separator.

        Run on every platform by asking for the Windows branch explicitly -- the
        failure it guards is invisible on the machines most sessions run on, and
        the value it destroys is the one that decides WHICH repository the command
        acts on. All three quoting forms are here because the fix doubles the
        backslashes before splitting, and single quotes are the form shlex does
        not unescape again.
        """
        for cmd, token in (
            (r"git -C C:\proj\repo switch topic", r"C:\proj\repo"),
            (r'git -C "C:\proj\repo" switch topic', r"C:\proj\repo"),
            (
                r"git -C 'C:\proj\repo' switch topic",
                "C:" + "\\" * 2 + "proj" + "\\" * 2 + "repo",
            ),
        ):
            segments, clean = wg.split_command(cmd, windows=True)
            assert clean, cmd
            _, _, chdirs = wg.parse_git(segments[0])
            assert chdirs == [token], cmd
            # Whatever the form, the path the guard acts on is the real one:
            # ntpath.normpath collapses the doubled separators (measured).
            assert ntpath.normpath(chdirs[0]) == r"C:\proj\repo", cmd

    def test_posix_escaping_still_works(self):
        """The Windows branch is not the default; an escaped space is still one arg."""
        assert wg.split_command(r"git -C /a\ b switch topic", windows=False) == (
            [["git", "-C", "/a b", "switch", "topic"]],
            True,
        )

    def test_an_untokenizable_command_holding_git_is_a_finding_of_its_own(self):
        """The splitter reports what it managed to read and says it gave up.
        `git switch "unclosed` yields a `switch` segment, which the ladder reads,
        and the command as a whole is an untokenizable one holding `git`, which is
        unrecognised (#826, the owner's answer P4 (a)): what the splitter could
        not read is not taken to be nothing."""
        command = 'git switch "unclosed'
        segments, clean = wg.split_command(command)
        assert clean is False
        assert wg.shape_of(segments[0]) == "switch"
        found = wg._command_findings(wg._judgment_text(command), clean)
        assert [f.kind for f in found] == ["untokenizable"], found


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

    def test_the_retry_token_survives_a_closing_parenthesis(self, repo):
        """A consent read that the judgment read can reach past.

        The judgment read strips a subshell opener, so a creation command inside
        parentheses now classifies — and `has_token` did not strip anything, so
        the token written at the end of that command carried the closing
        parenthesis and matched nothing. Creation is the one verdict in this guard
        with no `ask` behind it, which makes an unreadable token an inescapable
        loop rather than an extra prompt.
        """
        inside = "(git worktree add ../wt f [worktree-ok])"
        assert wg.has_token(inside, "[worktree-ok]")
        assert wg.has_token("git switch x [shared-tree-ok])", "[shared-tree-ok]")
        assert not wg.has_token("echo nothing here", "[worktree-ok]")

    @pytest.mark.parametrize("name", sorted(TYPED_BESIDE_A_BODY))
    def test_a_typed_token_beside_a_body_is_still_read(self, name):
        """`frame/design.md` A7. Every documented form still carries consent when a
        here-document stands in the same command."""
        command, token = TYPED_BESIDE_A_BODY[name]
        assert wg.has_token(command, token), name

    @pytest.mark.parametrize("break_it", ["cmdline exits at load", "without_bodies"])
    def test_a_broken_wider_reader_reads_no_body_token_and_keeps_a_typed_one(
        self, monkeypatch, tmp_path, break_it
    ):
        """`frame/design.md` A8. Where `hooks/lib/cmdline.py` does not load, or where
        `hooks/lib/tokens.py#without_bodies` raises, the bodies are found by the
        frozen reader `_judgment_text` uses. A body token is still not read and a
        typed one still is (`plan.md` G and H). The body half is red at
        `a3aa139a`."""
        guard = wg
        if break_it == "without_bodies":
            monkeypatch.setattr(wg.tokens, "without_bodies", _raises)
        else:
            guard = _a_guard_whose_wider_reader_exits_at_load(monkeypatch, tmp_path)
        for name, (command, token) in BODY_TOKENS.items():
            assert not guard.has_token(command, token), name
        for name, (command, token) in TYPED_BESIDE_A_BODY.items():
            assert guard.has_token(command, token), name

    @pytest.mark.parametrize("token", ["[worktree-ok]", "[shared-tree-ok]"])
    @pytest.mark.parametrize("break_it", [None, "without_bodies"])
    def test_the_token_read_never_reads_more_than_the_base(
        self, monkeypatch, token, break_it
    ):
        """`frame/design.md` A9. Over every command of A6-A8, the two the splitter cannot
        finish until the body goes, and the existing token cases, `has_token` is
        True only where `a3aa139a`'s was, with the wider body reader working
        and raising. It holds by the AND in `frame/design.md` *Scope* In 5; red with the
        read over the body-free text alone (`plan.md` F)."""
        if break_it:
            monkeypatch.setattr(wg.tokens, "without_bodies", _raises)
        read = [command for command in TOKEN_COMMANDS if wg.has_token(command, token)]
        assert read, "no command carried the token where both reads find it"
        more = [
            command for command in read if not _the_bases_token_read(command, token)
        ]
        assert not more, more


class Test_walk_command:
    def test_accepts_a_cd_as_moving_the_segment_after_it(self):
        walked = wg.walk_command("cd sub && git switch x", "/base")
        # Built as `hooks/lib/cmdline_base.py#apply_chdir` builds it, joined and
        # then normalised, which on Windows turns the leading `/` into `\`.
        landed = os.path.normpath(os.path.join("/base", "sub"))
        assert walked[1] == (["git", "switch", "x"], (landed,))

    def test_refuses_a_heredoc_line_as_a_segment(self):
        walked = wg.walk_command("cat > n <<'EOF'\ngit switch x\nEOF", "/base")
        assert [tokens for tokens, _ in walked] == [["cat", ">", "n", "<<EOF"]]

    def test_a_windows_cd_path_is_not_mistaken_for_an_expansion(self):
        """A `cd` argument is the same kind of value as a `-C` one and arrives the
        same way, so it goes through the same adapter.

        POSIX-mode shlex reads `\\` as an escape and the guard doubles the
        backslashes before splitting to hand them back. The reader must then not
        treat what comes out as a destination it cannot compute — the characters
        it refuses are the ones that name a value or a set of paths (`$`, a glob),
        and a path separator is neither.
        """
        for cmd in (
            r"cd C:\proj\repo && git switch topic",
            r'cd "C:\proj\repo" && git switch topic',
        ):
            items, clean = wg._tokenize_with_separators(cmd, windows=True)
            assert clean, cmd
            assert items[0][1][0] == "cd", cmd
            assert ntpath.normpath(items[0][1][1]) == r"C:\proj\repo", cmd
            walked = wg.walk_command(cmd, r"C:\start", windows=True)
            where = walked[1][1][0]
            assert not isinstance(where, wg.cmdline.Unresolved), cmd

    def test_the_guard_reads_the_same_answer(self):
        """S13. Issue #68's rounds twice fixed one gate and left the other, so the
        guard is asserted rather than assumed. It reads the walk through
        `walk_command` in `hooks/worktree-guard.py`, and since #689 that walk is
        `hooks/lib/cmdline_base.py`'s, `86256492`'s reader frozen, where the commit
        gate takes `cmdline.walk_directories`; an `eval` is refused by both.

        `wg.cmdline` rather than a reader loaded here: the guard reaches its
        reader with a plain `import cmdline_base as cmdline`, which goes through
        `sys.modules`, while
        `load_hook_module` builds a second instance under its own name. The two
        `Unresolved` classes are then different objects and `isinstance` is False
        across them -- which is a test that passes for the wrong reason waiting to
        happen, since the failing direction is "nothing was unreadable".
        """
        walked = wg.walk_command("eval 'cd /target'; git switch main", "/session")
        wheres = list(walked[-1][1])
        assert wheres and all(isinstance(w, wg.cmdline.Unresolved) for w in wheres), (
            f"the guard still answered with a directory: {[str(w) for w in wheres]}"
        )


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

    def test_the_process_probe_survives_output_it_cannot_decode(self, monkeypatch):
        """`tasklist` is the only process probe Windows has — there is no `ps` and
        no `/proc` — and it answers in the OEM codepage, so it is the one reader in
        this tree whose source is not UTF-8.

        Under `text=True` its reader thread died and `r.stdout` came back `None`,
        which `.splitlines()` then hit OUTSIDE the `try`. The guard's session
        detection went blind on exactly the consoles most likely to be non-UTF-8,
        and blind means `reliable` is False, which means every branch switch
        reaches the cannot-tell arm.
        """
        guard = load("hooks/worktree-guard.py", "agentic_guard_failopen")
        if not hasattr(guard, "lease_owner_alive"):
            pytest.skip("the probe moved; this case names it by function")

        def decoded_nothing(*args, **kwargs):
            return subprocess.CompletedProcess(args, 0, stdout=None, stderr=None)

        monkeypatch.setattr(guard.subprocess, "run", decoded_nothing)
        monkeypatch.setattr(guard.sys, "platform", "win32")
        # False — "this pid is not running" — and not a traceback. Answering the
        # question wrongly is a separate matter from failing to answer it at all,
        # and only the second one takes the caller down with it.
        assert guard.lease_owner_alive(1) is False


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

    # A lease outlives the session that wrote it: it is stamped on every tool
    # call and never removed at session end. Measured: two conversations ended
    # at 11:28 and 11:32 and their leases denied a branch switch in a third. A
    # lease whose owning process is gone is not a work stream, and a lease that
    # cannot be attributed is a question for the user, not a refusal.

    def test_lease_of_a_dead_process_is_dropped(self, repo):
        write_lease(
            repo,
            "ended-session",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": dead_pid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        live, unattributable = wg.fresh_leases(str(repo), "me")
        assert live == [] and unattributable == []

    def test_lease_of_a_live_process_stays_active(self, repo):
        write_lease(
            repo,
            "running-session",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": os.getpid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        live, unattributable = wg.fresh_leases(str(repo), "me")
        assert len(live) == 1 and "running-" in live[0][1]
        assert unattributable == []

    def test_lease_without_a_pid_is_unattributable_not_active(self, repo):
        """The pre-upgrade format: a bare timestamp. Ask, do not deny."""
        write_lease(repo, "legacy-session", "1")
        live, unattributable = wg.fresh_leases(str(repo), "me")
        assert live == []
        assert len(unattributable) == 1 and "legacy-s" in unattributable[0][1]

    def test_lease_from_another_host_stays_active(self, repo):
        """No pid to check here, and a fresh stamp still means someone is working."""
        write_lease(
            repo,
            "elsewhere",
            json.dumps({"ts": int(time.time()), "pid": 1, "host": "some-other-host"}),
        )
        live, unattributable = wg.fresh_leases(str(repo), "me")
        assert len(live) == 1 and unattributable == []

    def test_own_lease_is_ignored_in_both_lists(self, repo):
        write_lease(
            repo,
            "me",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": os.getpid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        assert wg.fresh_leases(str(repo), "me") == ([], [])

    # Quiet is not the same question as gone. Alive answers "does the session
    # exist"; the idle window answers "is it working". A session quiet for an
    # hour but still running is a forgotten tab, which the process scan
    # already treats as a question. The escalation is confined to what the
    # scan CANNOT see: a lease naming a pid the scan already reports adds
    # nothing.

    def test_stale_lease_with_a_live_owner_the_scan_misses_asks(self, repo):
        stale_lease(repo, "other-cwd-session", os.getpid())
        live, unattributable = wg.fresh_leases(
            str(repo), "me", scanned_pids=frozenset()
        )
        assert live == []
        assert len(unattributable) == 1 and "other-cw" in unattributable[0][1]

    def test_stale_lease_the_scan_already_reports_is_not_counted_twice(self, repo):
        """The narrowing. The scan saw this pid and classified it; the lease steps
        aside rather than raising a second prompt for one session."""
        stale_lease(repo, "seen-session", os.getpid())
        assert wg.fresh_leases(
            str(repo), "me", scanned_pids=frozenset({os.getpid()})
        ) == (
            [],
            [],
        )

    def test_stale_lease_with_a_dead_owner_stays_dropped(self, repo):
        stale_lease(repo, "ended-session", dead_pid())
        assert wg.fresh_leases(str(repo), "me", scanned_pids=frozenset()) == ([], [])

    def test_stale_lease_without_a_pid_stays_dropped(self, repo):
        """No owner to ask about, so age remains the only filter it has."""
        p = write_lease(repo, "legacy-old", "1")
        os.utime(p, (time.time() - 3600,) * 2)
        assert wg.fresh_leases(str(repo), "me", scanned_pids=frozenset()) == ([], [])

    def test_stale_lease_with_an_unprobeable_owner_is_not_escalated(
        self, repo, monkeypatch
    ):
        """`None` is "could not ask", not "is running". Escalating it would turn
        every unanswerable probe into a prompt, which is the absence of evidence
        being read as evidence."""
        stale_lease(repo, "unprobeable", 424242)
        monkeypatch.setattr(wg, "lease_owner_alive", lambda pid: None)
        assert wg.fresh_leases(str(repo), "me", scanned_pids=frozenset()) == ([], [])

    def test_fresh_lease_with_an_unprobeable_owner_still_denies(
        self, repo, monkeypatch
    ):
        """The fresh path keeps treating an unanswerable probe as active work —
        conservative there, because the stamp itself says someone just worked."""
        write_lease(
            repo,
            "unprobeable-now",
            json.dumps(
                {"ts": int(time.time()), "pid": 424242, "host": socket.gethostname()}
            ),
        )
        monkeypatch.setattr(wg, "lease_owner_alive", lambda pid: None)
        live, _ = wg.fresh_leases(str(repo), "me", scanned_pids=frozenset())
        assert len(live) == 1 and "unprobeable" in live[0][1]

    def test_the_fresh_path_is_unchanged_by_the_scan(self, repo):
        """A lease stamped moments ago is active work whether or not the scan
        also found it; this narrowing must not touch the deny path."""
        write_lease(
            repo,
            "busy-session",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": os.getpid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        live, _ = wg.fresh_leases(
            str(repo), "me", scanned_pids=frozenset({os.getpid()})
        )
        assert len(live) == 1


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

    def test_dead_session_ids_names_only_provably_dead_owners(
        self, repo, tmp_path, monkeypatch
    ):
        """Every shape that is not positive evidence of death stays out."""
        write_lease(
            repo,
            "gone",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": dead_pid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        write_lease(
            repo,
            "running",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": os.getpid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        write_lease(
            repo,
            "far-away",
            json.dumps({"ts": int(time.time()), "pid": 1, "host": "some-other-host"}),
        )
        write_lease(repo, "no-pid", "1")
        assert wg.dead_session_ids(str(repo)) == frozenset({"gone"})

    def test_dead_session_ids_is_empty_without_a_lease_directory(self, tmp_path):
        """No repo, no leases, no exclusions — and no exception."""
        d = tmp_path / "not-a-repo"
        d.mkdir()
        assert wg.dead_session_ids(str(d)) == frozenset()

    def test_a_non_integer_pid_is_never_asked_about(self, repo, monkeypatch):
        """The guard clause, pinned where POSIX cannot show it on its own.

        `os.kill` rejects a string pid with TypeError, so on this platform a bad
        pid falls out anyway and the check looks redundant. It is not: Windows
        probes with `tasklist /FI "PID eq {pid}"`, where a string interpolates
        happily and can match a real process. Forcing lease_owner_alive to answer
        "gone" for anything is what makes the clause the only thing standing
        between a malformed lease and a retired transcript.
        """
        write_lease(
            repo,
            "bad-pid",
            json.dumps(
                {"ts": int(time.time()), "pid": "424242", "host": socket.gethostname()}
            ),
        )
        monkeypatch.setattr(wg, "lease_owner_alive", lambda pid: False)
        assert wg.dead_session_ids(str(repo)) == frozenset()


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


class Test_file_activity_epoch:
    def test_accepts_a_fresh_active_event(self, tmp_path):
        p = tmp_path / "t.jsonl"
        write_jsonl(
            p,
            [
                {"type": "attachment", "timestamp": iso(180)},
                {"type": "assistant", "timestamp": iso(0)},
            ],
        )
        epoch = wg.file_activity_epoch(str(p), time.time() - 300)
        assert epoch is not None and (time.time() - epoch) < 120

    def test_refuses_fresh_passive_events_as_activity(self, tmp_path):
        p = tmp_path / "t.jsonl"
        write_jsonl(
            p,
            [
                {"type": "assistant", "timestamp": iso(180)},
                {"type": "attachment", "timestamp": iso(0)},
            ],
        )
        epoch = wg.file_activity_epoch(str(p), time.time() - 300)
        assert epoch is not None and (time.time() - epoch) > 3600  # 3h, not now

    def test_stale_mtime_is_trusted_without_parsing(self, tmp_path):
        p = tmp_path / "t.jsonl"
        write_jsonl(
            p, [{"type": "assistant", "timestamp": iso(0)}]
        )  # content lies fresh
        os.utime(p, (time.time() - 7200,) * 2)
        epoch = wg.file_activity_epoch(str(p), time.time() - 300)
        assert abs((time.time() - epoch) - 7200) < 90  # mtime wins on the cheap path


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

    def test_transcript_scan_reaches_background_agents(self, monkeypatch, tmp_path):
        cwd = tmp_path / "tree"
        cwd.mkdir()
        proj = project_dir(monkeypatch, tmp_path, cwd)
        sub = proj / "other-session" / "subagents"
        sub.mkdir(parents=True)
        write_jsonl(sub / "agent-x.jsonl", [{"type": "assistant", "timestamp": iso(1)}])
        idle = wg.transcript_idle_minutes(str(cwd), "my-session")
        assert idle is not None and idle < 5

    def test_own_session_files_are_excluded(self, monkeypatch, tmp_path):
        cwd = tmp_path / "tree"
        cwd.mkdir()
        proj = project_dir(monkeypatch, tmp_path, cwd)
        write_jsonl(proj / "mine.jsonl", [{"type": "assistant", "timestamp": iso(0)}])
        assert wg.transcript_idle_minutes(str(cwd), "mine") is None

    # A lease also retires the TRANSCRIPT its session left behind. Measured in
    # this repository on 2026-09-08: `fresh_leases` retired session fdbb7b51's
    # lease on positive evidence its pid was gone, and `sessions_in_tree`'s
    # last arm then read that same session's two-minute-old transcript and put
    # it straight back into `active`. A session lands in the dead set only on
    # positive evidence its owner is gone, so every unreadable answer leaves
    # the transcript counted exactly as before.

    def test_an_exited_sessions_transcript_is_not_a_work_stream(
        self, repo, tmp_path, monkeypatch
    ):
        """THE INCIDENT. Fresh transcript, active tail, owner provably gone."""
        exited_session(repo, tmp_path, monkeypatch)
        assert idle_minutes(repo) is None

    def test_a_transcript_with_no_lease_still_counts(self, repo, tmp_path, monkeypatch):
        """THE CASE THAT MUST NOT BREAK — an extension-panel session that has
        written transcripts but not yet touched the repo, so it has no lease.
        Nothing proves it dead, so it stays a live work stream."""
        proj = transcripts_for(monkeypatch, tmp_path, repo)
        fresh_transcript(proj / "panel-session.jsonl")
        idle = idle_minutes(repo)
        assert idle is not None and idle < wg.IDLE_MIN

    def test_a_live_lease_owner_keeps_its_transcript(self, repo, tmp_path, monkeypatch):
        proj = transcripts_for(monkeypatch, tmp_path, repo)
        fresh_transcript(proj / "running-session.jsonl")
        write_lease(
            repo,
            "running-session",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": os.getpid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        idle = idle_minutes(repo)
        assert idle is not None and idle < wg.IDLE_MIN

    def test_a_lease_from_another_host_does_not_retire_a_transcript(
        self, repo, tmp_path, monkeypatch
    ):
        """Another machine's pid is not ours to probe, so it is not evidence.

        The pid here is one that has certainly exited ON THIS host, which is the
        whole point: only the host check keeps it out of the dead set. An earlier
        draft used pid 1, which is alive everywhere, so the case passed with the
        host check deleted — it was pinning nothing."""
        proj = transcripts_for(monkeypatch, tmp_path, repo)
        fresh_transcript(proj / "elsewhere.jsonl")
        write_lease(
            repo,
            "elsewhere",
            json.dumps(
                {"ts": int(time.time()), "pid": dead_pid(), "host": "some-other-host"}
            ),
        )
        idle = idle_minutes(repo)
        assert idle is not None and idle < wg.IDLE_MIN

    def test_a_lease_without_a_pid_does_not_retire_a_transcript(
        self, repo, tmp_path, monkeypatch
    ):
        """The pre-upgrade bare-timestamp format: no owner to ask about."""
        proj = transcripts_for(monkeypatch, tmp_path, repo)
        fresh_transcript(proj / "legacy-session.jsonl")
        write_lease(repo, "legacy-session", "1")
        idle = idle_minutes(repo)
        assert idle is not None and idle < wg.IDLE_MIN

    def test_a_dead_sessions_subagent_transcripts_are_skipped(
        self, repo, tmp_path, monkeypatch
    ):
        """Background agents run inside their session's process; when the lease
        proves that process gone, its subagents went with it."""
        proj = transcripts_for(monkeypatch, tmp_path, repo)
        sub = proj / "ended-session" / "subagents"
        sub.mkdir(parents=True)
        fresh_transcript(sub / "agent-x.jsonl")
        write_lease(
            repo,
            "ended-session",
            json.dumps(
                {
                    "ts": int(time.time()),
                    "pid": dead_pid(),
                    "host": socket.gethostname(),
                }
            ),
        )
        assert idle_minutes(repo) is None

    def test_an_unprobeable_owner_does_not_retire_a_transcript(
        self, repo, tmp_path, monkeypatch
    ):
        """Where this fix's fail direction lives. `None` from lease_owner_alive is
        "could not ask", never "is gone" — so the transcript stays counted, and an
        unreadable answer reproduces today's behaviour rather than opening the
        fail-open direction where the guard allows a switch that takes someone
        else's branch."""
        proj = transcripts_for(monkeypatch, tmp_path, repo)
        fresh_transcript(proj / "unprobeable.jsonl")
        write_lease(
            repo,
            "unprobeable",
            json.dumps(
                {"ts": int(time.time()), "pid": 424242, "host": socket.gethostname()}
            ),
        )
        monkeypatch.setattr(wg, "lease_owner_alive", lambda pid: None)
        idle = idle_minutes(repo)
        assert idle is not None and idle < wg.IDLE_MIN


class Test_last_user_snippet:
    def test_accepts_the_conversation_another_session_left(self, monkeypatch, tmp_path):
        cwd = tmp_path / "tree"
        cwd.mkdir()
        proj = project_dir(monkeypatch, tmp_path, cwd)
        write_jsonl(
            proj / "abcd1234-x.jsonl",
            [
                {
                    "type": "user",
                    "timestamp": iso(3),
                    "message": {"content": "리뷰 이어서 진행해줘"},
                },
                {"type": "assistant", "timestamp": iso(2)},
            ],
        )
        sid, _ts, text = wg.last_user_snippet(str(cwd), "me")
        assert sid == "abcd1234" and "리뷰 이어서" in text

    def test_refuses_its_own_session_and_an_absent_transcript(
        self, monkeypatch, tmp_path
    ):
        cwd = tmp_path / "tree"
        cwd.mkdir()
        proj = project_dir(monkeypatch, tmp_path, cwd)
        write_jsonl(
            proj / "mine.jsonl",
            [{"type": "user", "timestamp": iso(1), "message": {"content": "secret"}}],
        )
        assert wg.last_user_snippet(str(cwd), "mine") is None

    def test_a_transcript_record_holding_a_raw_separator_is_read(
        self, monkeypatch, tmp_path
    ):
        """S16 of #664. Cut at a U+2028 a JavaScript writer leaves raw in a
        string, the last user record was two halves that each failed to parse,
        and the snippet named an earlier message."""
        cwd = tmp_path / "tree"
        cwd.mkdir()
        monkeypatch.setenv("HOME", str(tmp_path))
        monkeypatch.setenv("USERPROFILE", str(tmp_path))
        proj = tmp_path / ".claude" / "projects" / wg.project_slug(str(cwd))
        proj.mkdir(parents=True)
        jsonl(
            proj / "abcd1234-x.jsonl",
            [
                {
                    "type": "user",
                    "timestamp": "2026-01-01T00:00",
                    "message": {"content": "first"},
                },
                {
                    "type": "user",
                    "timestamp": "2026-01-01T00:05",
                    "message": {"content": f"second{LS}message"},
                },
            ],
        )
        _sid, when, text = wg.last_user_snippet(str(cwd), "me")
        assert when == "2026-01-01T00:05"
        assert text.startswith("second")


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

    @pytest.mark.rule("a-persons-own-commit")
    def test_the_guard_counts_the_sessions_the_one_test_names(
        self, tmp_path, monkeypatch
    ):
        """S4 of work item 1791384157, the guard's half: its count of other
        sessions tests each process's name with `hooksession.is_claude`, so a
        `claude-host` in the tree is not a session and `/x/bin/claude` is. A break
        reading any name holding `claude` survived every guard case until this
        one."""
        import types

        top = str(tmp_path)
        table = "10 /x/bin/claude\n20 /x/bin/claude\n30 claude-host\n"
        monkeypatch.setattr(
            wg.subprocess, "run", lambda *a, **k: types.SimpleNamespace(stdout=table)
        )
        monkeypatch.setattr(wg, "ancestors", lambda pid: {10})
        monkeypatch.setattr(wg, "proc_cwd", lambda pid: top)
        monkeypatch.setattr(wg, "tty_idle_minutes", lambda pid: 0.5)
        monkeypatch.setattr(wg, "transcript_idle_minutes", lambda *a: None)
        monkeypatch.setattr(wg, "dead_session_ids", lambda top: set())
        monkeypatch.setattr(wg, "fresh_leases", lambda *a: ([], []))
        monkeypatch.setattr(wg, "host_app", lambda pid: "")
        active, idle, reliable = wg.sessions_in_tree(top, "me")
        assert reliable and not idle
        assert [entry[0] for entry in active] == [20], active

    def test_sessions_in_tree_does_not_resurrect_an_exited_session(
        self, repo, tmp_path, monkeypatch
    ):
        """End to end: the arm must not put back what fresh_leases just buried."""
        exited_session(repo, tmp_path, monkeypatch)
        only_our_own_claude(monkeypatch)
        active, _idle, reliable = wg.sessions_in_tree(str(repo), "my-session")
        assert reliable is True
        assert active == [], f"an exited session came back as active: {active}"

    def test_sessions_in_tree_still_sees_an_unattached_live_session(
        self, repo, tmp_path, monkeypatch
    ):
        """The arm still fires for the case it exists for: a fresh transcript with
        no process AND nothing proving its session dead."""
        proj = transcripts_for(monkeypatch, tmp_path, repo)
        fresh_transcript(proj / "panel-session.jsonl")
        only_our_own_claude(monkeypatch)
        active, _idle, reliable = wg.sessions_in_tree(str(repo), "my-session")
        assert reliable is True
        assert len(active) == 1 and active[0][0] is None

    def test_a_live_session_is_not_kept_active_by_a_dead_neighbours_transcript(
        self, repo, tmp_path, monkeypatch
    ):
        """The same defect on the OTHER call site, which the arm's fix does not
        reach on its own.

        A live `claude` process sits in the tree with no terminal input for an
        hour. Its only remaining evidence of work is the project transcript — and
        that transcript belongs to a neighbour that has exited. Counting it holds
        the session in `active`, which on the switch path is a hard deny; with the
        dead session excluded it falls to `idle`, which is a question the user can
        answer. Never a silent allow either way: the pid is real, so the session
        stays in one of the two lists.
        """
        exited_session(repo, tmp_path, monkeypatch)
        other = 525252
        only_our_own_claude(monkeypatch, 424242, other)
        monkeypatch.setattr(wg, "proc_cwd", lambda pid: str(repo))
        monkeypatch.setattr(wg, "tty_idle_minutes", lambda pid: 60.0)

        active, idle, reliable = wg.sessions_in_tree(str(repo), "my-session")
        assert reliable is True
        assert active == [], f"a dead neighbour's transcript held it active: {active}"
        assert len(idle) == 1 and idle[0][0] == other


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

    def test_tracked_changes_ignore_untracked(self, repo):
        (repo / "new-untracked.txt").write_text("x", encoding="utf-8")
        assert wg.tracked_changes(str(repo)) == []


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

    def test_the_repository_lookup_cannot_hang_the_gate(self, repo):
        """A shape check, and labelled as one: no unresponsive mount was mounted.

        `repo_paths` shells out to git once per candidate directory, and the
        reader can hand it several. The same species of call in `hooks/lib/optin.py`
        carries `timeout=5` for a reason recorded there. A hook that never returns
        is a hook that never decides.
        """
        import inspect

        source = inspect.getsource(wg.repo_paths)
        assert "timeout=" in source, (
            "the git lookup has no timeout, so an unresponsive path hangs the hook"
        )


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

    # --- the decision a lease leads to ---

    def test_unattributable_lease_offers_a_choice_instead_of_blocking(
        self, monkeypatch, capsys, repo
    ):
        """Both this and the ACTIVE-session block return `deny` now, so the reason
        is what tells them apart: this one hands the decision back to the user."""
        lease = [(None, f"{repo}  [lease: legacy-s… owner unknown]", None, 0.5, None)]
        d, reason = decide(
            monkeypatch,
            capsys,
            repo,
            "git switch feature/x",
            sessions=([], lease, True),
        )
        assert d == "deny"
        assert "AskUserQuestion" in reason

    def test_the_question_names_both_choices(self, monkeypatch, capsys, repo):
        """The point of denying here is that BOTH ways on get named — the shared
        tree with its retry token, and the worktree."""
        lease = [(None, f"{repo}  [lease: legacy-s… owner unknown]", None, 0.5, None)]
        _, reason = decide(
            monkeypatch,
            capsys,
            repo,
            "git switch feature/x",
            sessions=([], lease, True),
        )
        assert "[shared-tree-ok]" in reason
        assert "worktree" in reason.lower()

    @pytest.mark.parametrize(
        "entry",
        ["[lease: running-… pid 42 alive]", "[lease: abcd1234…]"],
        ids=["a-live-owner", "a-fresh-lease"],
    )
    def test_live_lease_still_denies(self, monkeypatch, capsys, repo, entry):
        lease = [(None, f"{repo}  {entry}", None, 0.5, None)]
        d, reason = decide(
            monkeypatch,
            capsys,
            repo,
            "git switch feature/x",
            sessions=(lease, [], True),
        )
        assert d == "deny" and "lease" in reason

    # --- rows reached through `decide` ---

    def test_worktree_add_idle_sessions_offer_both_ways_on(
        self, monkeypatch, capsys, repo
    ):
        d, reason = decide(
            monkeypatch,
            capsys,
            repo,
            "git worktree add ../wt feature/x",
            sessions=([], [(2, "/t", 400.0, 90.0, "Terminal")], True),
        )
        assert d == "deny" and "git switch" in reason  # switch may suffice
        assert "AskUserQuestion" in reason and "[shared-tree-ok]" in reason

    def test_worktree_add_unreliable_offers_both_ways_on(
        self, monkeypatch, capsys, repo
    ):
        assert (
            decide(
                monkeypatch,
                capsys,
                repo,
                "git worktree add ../wt feature/x",
                sessions=([], [], False),
            )[0]
            == "deny"
        )

    def test_dirty_ask_lists_the_files(self, monkeypatch, capsys, repo):
        (repo / "f.txt").write_text("changed\n", encoding="utf-8")
        d, reason = decide(monkeypatch, capsys, repo, "git switch feature/x")
        assert d == "ask" and "f.txt" in reason

    # --- Agent/Task isolation:"worktree" path ---

    def test_agent_isolation_worktree_single_stream_asks(
        self, monkeypatch, capsys, repo
    ):
        """`ask`, not `deny`, in a tree where this session is the only one. The
        agent runs beside this session, so the call is concurrent work however
        many sessions the count finds (#8), and the first creation of a session is
        one confirmation."""
        assert (
            agent_decide(
                monkeypatch, capsys, repo, {"prompt": "x", "isolation": "worktree"}
            )[0]
            == "ask"
        )

    def test_agent_isolation_worktree_concurrent_asks(self, monkeypatch, capsys, repo):
        """Another session ACTIVE in the tree changes nothing on this path: it
        counts no sessions, so the reason is the one a one-session tree gets and
        lists nobody. It used to list the other session, back when this path
        reached the creation ladder's ACTIVE row."""
        decision, reason = agent_decide(
            monkeypatch,
            capsys,
            repo,
            {"prompt": "x", "isolation": "worktree"},
            sessions=([(1, "/t", 0.1, 0.1, None)], [], True),
        )
        assert decision == "ask"
        assert "runs beside this session" in reason
        assert "actively working" not in reason
        assert "single-stream" not in reason

    def test_agent_without_isolation_is_untouched(self, monkeypatch, capsys, repo):
        assert agent_decide(monkeypatch, capsys, repo, {"prompt": "x"})[0] == "silent"

    # --- the switch ladder's two choice rows under `automation` (#896) ---
    #
    # Rows 1-b and 2 of *A. Branch switch* `deny` on every attempt under the
    # press. Where a creation in the switch's clone is consented, the reason
    # names the split; in another clone it names none. It names no question
    # tool and no token, and writes no choice marker.

    @pytest.mark.parametrize("row", ["idle", "unusable"])
    def test_under_the_press_a_choice_row_denies_every_attempt(
        self, monkeypatch, capsys, projects, repo, wko, row
    ):
        """S3 (row 1-b) and S4 (row 2). Three attempts, one deny text each time,
        in both languages, naming the split and nothing a person would answer,
        and no choice marker left behind. Seen red at `c38f97d7`: `deny` naming
        `AskUserQuestion`, then `ask`, then `ask`."""
        write_transcript(projects, "me", ask_entries(repo))
        for lang, module in (("en", wg), ("ko", wko)):
            want = unattended(module, lang, row, repo)
            for attempt in range(3):
                got = judge(
                    module, monkeypatch, capsys, repo, "git switch feature/x", ROWS[row]
                )
                assert got == ("deny", want), (lang, attempt, got)
                assert_names_nobody(got[1])
            assert no_marker(module, repo), lang

    def test_the_token_still_reads_as_it_does_attended(
        self, monkeypatch, capsys, projects, repo
    ):
        """S6, P2 (a). Under the press `[shared-tree-ok]` stands both rows aside
        as it does attended: a clean tree is silent, and a dirty one reaches the
        tracked-changes row with the token's lead rather than this work's deny.
        Green at `c38f97d7` by design; shown red by the mutation that reads the
        press ahead of the token (phase 2's record). The dirty row's verdict
        under the press is #894's deny, whole, with the token's lead: pinned
        here since #894 merged in (phase 3)."""
        write_transcript(projects, "me", ask_entries(repo))
        command = "git switch feature/x  # [shared-tree-ok]"
        for row, sessions in ROWS.items():
            got = judge(wg, monkeypatch, capsys, repo, command, sessions)
            assert got == ("silent", ""), (row, got)
            dirty(repo)
            got = judge(wg, monkeypatch, capsys, repo, command, sessions)
            assert got == ("deny", dirty_deny("en", TOKEN["en"])), (row, got)
            assert "split into a worktree" not in got[1], got
            (repo / "f.txt").write_text("one\ntwo\nthree\n", encoding="utf-8")

    def test_the_way_on_passes_the_guard(
        self, monkeypatch, capsys, projects, repo, tmp_path
    ):
        """S7, run rather than read (contract rule 13). The fixture gains an
        `origin` holding `main` (W3), so the commands the deny names run as
        written: the fetch and the creation each pass the guard and then run in
        git, and a git command in the new worktree, issued by path from this
        session, passes too. Seen red at `c38f97d7`: the deny named the
        `[worktree-ok]` form, and the first attempt was a question."""
        origin = tmp_path / "origin.git"
        git_ok("init", "-q", "--bare", str(origin))
        git_ok("-C", str(repo), "remote", "add", "origin", str(origin))
        git_ok("-C", str(repo), "push", "-q", "origin", "HEAD:refs/heads/main")
        write_transcript(projects, "me", ask_entries(repo))
        idle = ROWS["idle"]

        decision, reason = judge(wg, monkeypatch, capsys, repo, "git switch y", idle)
        assert decision == "deny", reason
        wt_root = wg.repo_paths(str(repo))[1]
        named = f"git worktree add {wt_root}/<name> -b <branch> origin/main"
        assert f"  git fetch origin\n  {named}\n" in reason, reason

        assert judge(wg, monkeypatch, capsys, repo, "git fetch origin", idle) == (
            "silent",
            "",
        )
        git_ok("-C", str(repo), "fetch", "-q", "origin")
        wt = f"{wt_root}/y"
        creation = f"git worktree add {shlex.quote(wt)} -b feature/y origin/main"
        decision, reason = judge(wg, monkeypatch, capsys, repo, creation, idle)
        assert decision == "allow", reason
        git_ok(
            "-C",
            str(repo),
            "worktree",
            "add",
            "-q",
            wt,
            "-b",
            "feature/y",
            "origin/main",
        )
        assert git_ok("-C", wt, "branch", "--show-current") == "feature/y"
        status = f"git -C {shlex.quote(wt)} status"
        assert judge(wg, monkeypatch, capsys, repo, status, idle) == ("silent", "")

    def test_a_creation_on_the_same_line_is_stopped_with_it(
        self, monkeypatch, capsys, projects, repo
    ):
        """S8. A deny stops the whole line, so the creation behind the switch
        does not run and nothing is recorded for it. Seen red at `c38f97d7`: the
        attended deny naming `AskUserQuestion`."""
        write_transcript(projects, "me", ask_entries(repo))
        command = "git switch feature/x && git worktree add ../wt f"
        got = judge(wg, monkeypatch, capsys, repo, command, ROWS["idle"])
        assert got == ("deny", unattended(wg, "en", "idle", repo)), got
        assert not (consent_dir(repo) / "me").exists()
        assert not (repo.parent / "wt").exists()

    def test_the_plain_retry_after_the_stop_meets_the_deny(
        self, monkeypatch, capsys, projects, repo
    ):
        """S9. The unrecognised-shape stop names the plain spelling, and its
        plain retry now meets this work's deny in the two states the rows cover.
        Where another session is ACTIVE both are the denies they were. Seen red at
        `c38f97d7`: the retry met the attended deny naming `AskUserQuestion`."""
        write_transcript(projects, "me", ask_entries(repo))
        for row, sessions in ROWS.items():
            decision, reason = judge(
                wg, monkeypatch, capsys, repo, "git checkout feature/x", sessions
            )
            assert decision == "deny" and STOP in reason, (row, reason)
            got = judge(wg, monkeypatch, capsys, repo, "git switch feature/x", sessions)
            assert got == ("deny", unattended(wg, "en", row, repo)), (row, got)

        active = (ACTIVE, [], True)
        decision, reason = judge(
            wg, monkeypatch, capsys, repo, "git checkout feature/x", active
        )
        assert decision == "deny" and STOP in reason, reason
        decision, reason = judge(
            wg, monkeypatch, capsys, repo, "git switch feature/x", active
        )
        assert decision == "deny" and "actively working" in reason, reason
        assert "worktree add" in reason, reason

    def test_the_press_is_read_at_most_once_per_command(
        self, monkeypatch, capsys, projects, repo
    ):
        """S10, W2. The press is read only where one of the two rows fires, and
        each row ends the command, so a switch reads the transcript once at most:
        never in a clean single-stream tree, once in the idle state, once where
        the idle tree is also dirty, and once where the stop read it first. Seen
        red at `c38f97d7`: 0, 0, 0, 1."""
        write_transcript(projects, "me", ask_entries(repo))
        real = wg.worktree_consent.automation_answered
        reads = []

        def counted(*args, **kwargs):
            reads.append(args)
            return real(*args, **kwargs)

        monkeypatch.setattr(wg.worktree_consent, "automation_answered", counted)
        counts = []
        for sessions, make_dirty, command in (
            (([], [], True), False, "git switch feature/x"),
            (ROWS["idle"], False, "git switch feature/x"),
            (ROWS["idle"], True, "git switch feature/x"),
            (ROWS["idle"], False, "git checkout README.md && git switch feature/x"),
        ):
            (repo / "f.txt").write_text(
                "changed\n" if make_dirty else "one\ntwo\nthree\n", encoding="utf-8"
            )
            reads.clear()
            judge(wg, monkeypatch, capsys, repo, command, sessions)
            counts.append(len(reads))
        assert counts == [0, 1, 1, 1], counts

    def test_the_press_for_a_switch_is_read_from_the_sessions_own_root(
        self, monkeypatch, capsys, projects, repo, tmp_path
    ):
        """S11. Whether anybody is at the keyboard is a fact about the session,
        so the press is read against the root the shell stands in, not the tree
        the switch names. A switch into another clone in the idle state denies
        under this session's press, and a press given only in that other clone
        leaves the attended first attempt. Seen red at `c38f97d7`: the first half
        was the attended deny. Since round 1 the first half names no split, because
        the press is consent only in the clone it was given in."""
        other = tmp_path / "other-repo"
        shutil.copytree(repo, other)
        command = f"git -C {shlex.quote(str(other))} switch feature/x"

        write_transcript(projects, "me", ask_entries(repo))
        got = judge(wg, monkeypatch, capsys, repo, command, ROWS["idle"])
        want = situation("en", "idle", wg.IDLE_MIN) + "\n\n" + elsewhere("en")
        assert got == ("deny", want), got
        assert no_marker(wg, other)

        write_transcript(projects, "me", ask_entries(other))
        decision, reason = judge(wg, monkeypatch, capsys, repo, command, ROWS["idle"])
        assert decision == "deny" and "AskUserQuestion" in reason, reason

    @pytest.mark.skipif(
        sys.platform != "win32",
        reason="M2: the reading that every Windows switch is row 2 is Windows's",
    )
    def test_on_windows_a_switch_under_the_press_is_row_twos_deny(
        self, monkeypatch, capsys, projects, repo
    ):
        """M2 of work item 1791781864, measured by the Windows shards. Nothing is
        stubbed: `sessions_in_tree` runs as it does there, where `ps` takes no
        `-o` and detection reads unusable. If the reading is wrong, this case is
        where it shows, and `docs/worktree-guard-spec.md` *Known limits* is
        corrected in this work item. Seen red at `c38f97d7` off Windows, by a
        deleted probe in which the process scan found no `claude` process — the
        same branch: the attended deny."""
        write_transcript(projects, "me", ask_entries(repo))
        monkeypatch.setattr(
            wg,
            "load_input",
            lambda: {
                "tool_name": "Bash",
                "session_id": "me",
                "tool_input": {"command": "git switch feature/x"},
                "cwd": str(repo),
            },
        )
        try:
            wg.main()
        except SystemExit:
            pass
        d = json.loads(capsys.readouterr().out)["hookSpecificOutput"]
        got = (d["permissionDecision"], d["permissionDecisionReason"])
        assert got == ("deny", unattended(wg, "en", "unusable", repo)), got

    def test_a_switch_into_another_clone_names_no_split_it_cannot_consent(
        self, monkeypatch, capsys, projects, repo, tmp_path, wko
    ):
        """Round 1, red 1. The press consents to a creation only in the clone it
        was given in (`worktree_consent.automation_answered`, condition 4), so a
        switch into another clone under this session's press is refused without
        naming a split that clone's creation ladder would put to a person. Both
        rows, both languages. Seen red at `44c67f9f`, where the reason said the
        split's commands pass as written."""
        other = tmp_path / "other-repo"
        shutil.copytree(repo, other)
        write_transcript(projects, "me", ask_entries(repo))
        top = wg.repo_paths(str(other))[0]
        command = f"git -C {shlex.quote(top)} switch feature/x"
        for row, sessions in ROWS.items():
            for lang, module in (("en", wg), ("ko", wko)):
                decision, reason = judge(
                    module, monkeypatch, capsys, repo, command, sessions
                )
                assert decision == "deny", (row, lang, reason)
                assert reason == situation(lang, row, wg.IDLE_MIN) + "\n\n" + elsewhere(
                    lang
                ), (row, lang, reason)
                assert "worktree add" not in reason, reason
                assert_names_nobody(reason)
            assert no_marker(wg, other)

    def test_a_clone_this_session_already_split_is_named_the_split(
        self, monkeypatch, capsys, projects, repo, tmp_path, wko
    ):
        """Round 1, red 1, the record's half. Where this session already created a
        worktree in the other clone, its creation record is consent there
        (`worktree_consent.granted`), so the switch into that clone names the
        split as it does in the session's own clone, and says the record
        consents rather than the press, which consents only in the clone it was
        given in (round 2). Both languages. Seen red with the record's branch
        taken out of the clone test through `seal mutate` (round 1), and
        against the round-1 text, which credited the press (round 2)."""
        other = tmp_path / "other-repo"
        shutil.copytree(repo, other)
        write_transcript(projects, "me", ask_entries(repo))
        grant(other)
        top = wg.repo_paths(str(other))[0]
        command = f"git -C {shlex.quote(top)} switch feature/x"
        at = f"git -C {shlex.quote(top)}"
        because = {
            "en": (
                "That answer already consents to creating one, so these commands "
                "pass as written:",
                "This session already created a worktree in this clone, and that "
                "creation consents to the next one here, so these commands pass as "
                "written:",
            ),
            "ko": (
                "그 답이 worktree 생성에 이미 동의했으므로, 아래 명령은 쓰인 그대로 "
                "통과합니다.",
                "이 세션은 이 클론에서 이미 worktree 를 만들었고 그 생성이 이 클론의 "
                "다음 생성에도 동의하므로, 아래 명령은 쓰인 그대로 통과합니다.",
            ),
        }
        for lang, module in (("en", wg), ("ko", wko)):
            was, now = because[lang]
            base = unattended(module, lang, "idle", other, git=at)
            assert was in base, (lang, base)
            got = judge(module, monkeypatch, capsys, repo, command, ROWS["idle"])
            assert got == ("deny", base.replace(was, now)), (lang, got)

    # --- the creation ladder's two choice rows in another clone (#903) ---
    #
    # Rows 3 and 4 of *B. Worktree creation* are never reached under the press
    # in the clone it was given in, because row 0 reads the press as consent
    # first. In another clone, where this session holds no record, both rows
    # `deny` on every attempt under the press and name no way on.

    @pytest.mark.parametrize("row", ["idle", "unusable"])
    def test_under_the_press_a_creation_row_denies_every_attempt(
        self, monkeypatch, capsys, projects, repo, other, wko, row
    ):
        """S1 (row 3) and S2 (row 4). Three attempts, one deny text each time, in
        both languages, naming no way on and nothing a person would answer, and
        neither a choice marker nor a consent record left behind. Seen red at
        `321e9de1`, both rows: the first attempt was the attended deny naming
        `AskUserQuestion`."""
        write_transcript(projects, "me", ask_entries(repo))
        for lang, module in (("en", wg), ("ko", wko)):
            want = creation_unattended(lang, row)
            for attempt in range(3):
                got = judge(
                    module, monkeypatch, capsys, repo, creation(other), ROWS[row]
                )
                assert got == ("deny", want), (lang, attempt, got)
                assert_names_nobody(got[1])
                # The origin line names the command being judged; nothing after
                # it names one to run.
                assert "worktree add" not in got[1].split("\n", 1)[1], got
            assert no_create_marker(module, other), lang
        assert no_record(repo, other)

    def test_a_record_in_the_other_clone_outranks_the_rows(
        self, monkeypatch, capsys, projects, repo, other
    ):
        """S5. This session's record in the other clone is consent there, read at
        row 0 before any row below it, so the creation is allowed with the
        record's text and the deny is never reached. Green at `321e9de1`, which is
        the point; seen red through `seal mutate` with row 0's read taken
        out."""
        write_transcript(projects, "me", ask_entries(repo))
        grant(other)
        decision, reason = judge(
            wg, monkeypatch, capsys, repo, creation(other), ROWS["idle"]
        )
        assert decision == "allow", reason
        assert "A worktree creation already ran in this repository" in reason, reason

    def test_the_token_still_reaches_its_own_row(
        self, monkeypatch, capsys, projects, repo, other
    ):
        """S6. `[worktree-ok]` is read at row 2, above both choice rows, and its
        row is an `ask` under the press as attended. The deny names no token, so
        a model that appends one read it elsewhere, and the command line records
        that it did. Green at `321e9de1`; seen red through `seal mutate` with
        row 2 taken out."""
        write_transcript(projects, "me", ask_entries(repo))
        tagged = creation(other, "  # [worktree-ok]")
        decision, reason = judge(wg, monkeypatch, capsys, repo, tagged, ROWS["idle"])
        assert decision == "ask", reason
        assert "[worktree-ok] was given" in reason, reason
        assert "pressed `automation`" not in reason, reason

    def test_the_press_for_a_creation_is_read_from_the_sessions_own_root(
        self, monkeypatch, capsys, projects, repo, other, tmp_path
    ):
        """S7. Whether anybody is at the keyboard is a fact about the session, so
        the rows read the press against the root the shell stands in. A press
        given only in a third clone leaves the attended first attempt, and a
        press given in the creation's own clone is consent there at row 0. Green
        at `321e9de1` for both halves; seen red through `seal mutate` with the
        rows reading a press that is not there."""
        third = tmp_path / "third-repo"
        shutil.copytree(repo, third)
        write_transcript(projects, "me", ask_entries(third))
        decision, reason = judge(
            wg, monkeypatch, capsys, repo, creation(other), ROWS["idle"]
        )
        assert decision == "deny" and "AskUserQuestion" in reason, reason

        write_transcript(projects, "me", ask_entries(other))
        decision, reason = judge(
            wg, monkeypatch, capsys, repo, creation(other), ROWS["idle"]
        )
        assert decision == "allow" and "pressed `automation`" in reason, reason

    @pytest.mark.parametrize("row", ["idle", "unusable"])
    def test_an_unbalanced_quote_under_the_press_names_no_token(
        self, monkeypatch, capsys, projects, repo, other, wko, row
    ):
        """S1 for a command the lexer gives up on (round 1, yellow 1). The
        origin's quote note exists for the single-stream deny's way past,
        `[worktree-ok]`; under the press rows 3 and 4 name no token, so the deny
        is S1's, word for word, on every attempt. Seen red at `9e7514f3`: the
        first line named `[worktree-ok]` and invited a re-issue, and the retry
        with the token reached row 2's `ask`."""
        write_transcript(projects, "me", ask_entries(repo))
        command = creation(other, "  # don't")
        for lang, module in (("en", wg), ("ko", wko)):
            for attempt in range(2):
                got = judge(module, monkeypatch, capsys, repo, command, ROWS[row])
                assert got == ("deny", creation_unattended(lang, row)), (
                    lang,
                    attempt,
                    got,
                )
                assert_names_nobody(got[1])

    @pytest.mark.parametrize("row", ["idle", "unusable"])
    def test_attended_an_unbalanced_quote_keeps_the_quote_note(
        self, monkeypatch, capsys, projects, repo, other, wko, row
    ):
        """Attended, rows 3 and 4 open with the origin and its quote note, as at
        the base: only the press drops the note (round 2, note 5). No transcript
        is planted, so nothing is pressed; each language is its own session, so
        each meets its first attempt. Seen red through `seal mutate` with the
        attended arm of both rows' `lead` dropped."""
        command = creation(other, "  # don't")
        for lang, module in (("en", wg), ("ko", wko)):
            decision, reason = judge(
                module, monkeypatch, capsys, repo, command, ROWS[row], f"att-{lang}"
            )
            assert decision == "deny" and "AskUserQuestion" in reason, (lang, reason)
            assert "[worktree-ok]" in reason.splitlines()[0], (lang, reason)

    def test_a_creation_behind_a_cd_meets_the_same_deny(
        self, monkeypatch, capsys, projects, repo, other
    ):
        """S8. A creation reached through a `cd` into the other clone is the same
        creation: the deny stops the whole line with S1's text, and with the
        command stopped no `PostToolUse` writer runs, so no record is minted for
        a creation nobody was asked about. Seen red at `321e9de1`, where the
        reason named `AskUserQuestion`."""
        write_transcript(projects, "me", ask_entries(repo))
        command = f"cd {shlex.quote(other)} && git worktree add ../wt feature/x"
        got = judge(wg, monkeypatch, capsys, repo, command, ROWS["idle"])
        assert got == ("deny", creation_unattended("en", "idle")), got
        assert no_create_marker(wg, other)
        assert no_record(repo, other)

    def test_the_transcript_is_read_at_most_twice_per_creation(
        self, monkeypatch, capsys, projects, repo, other
    ):
        """S10. Row 0 reads the transcript once for the creation's clone, and the
        rows read it once more for the session's own root, only where row 3 or
        row 4 fires: once for a creation in the press's own clone, twice in the
        other clone's idle state, once in its clean single-stream state, and
        twice in its idle state attended, because whether the press is there is
        what that read finds out. Seen red at `321e9de1`: 1, 1, 1, 1."""
        real = wg.worktree_consent.automation_answered
        reads = []

        def counted(*args, **kwargs):
            reads.append(args)
            return real(*args, **kwargs)

        monkeypatch.setattr(wg.worktree_consent, "automation_answered", counted)
        pressed = ask_entries(repo)
        counts = []
        for entries, command, sessions in (
            (pressed, "git worktree add ../wt feature/x", ROWS["idle"]),
            (pressed, creation(other), ROWS["idle"]),
            (pressed, creation(other), ([], [], True)),
            (ask_entries(repo, answer="per axis"), creation(other), ROWS["idle"]),
        ):
            write_transcript(projects, "me", entries)
            reads.clear()
            judge(wg, monkeypatch, capsys, repo, command, sessions)
            counts.append(len(reads))
        assert counts == [1, 2, 1, 2], counts

    @pytest.mark.skipif(
        sys.platform != "win32",
        reason="M1: the reading that every Windows creation is row 4 is Windows's",
    )
    def test_on_windows_a_creation_in_another_clone_is_row_fours_deny(
        self, monkeypatch, capsys, projects, repo, other
    ):
        """S11, M1 of work item 1791852612, measured by the Windows shards.
        Nothing is stubbed: `sessions_in_tree` runs as it does there, where `ps`
        takes no `-o` and detection reads unusable. If the reading is wrong, this
        case is where it shows, and `docs/worktree-guard-spec.md` *Known limits*
        is corrected in this work item. Seen red at `321e9de1` off Windows, by a
        deleted probe that ran this body with the process scan stubbed to read
        unusable: the attended deny."""
        got = windows_creation(monkeypatch, capsys, projects, repo, other)
        assert got == ("deny", creation_unattended("en", "unusable")), got

    # --- the tree each command is judged in ---
    #
    # The guard judged the session's cwd, not the tree the command acts on:
    # `git -C <repo> switch <branch>` names its own repository, and with the
    # cwd at a home directory the containment test in `sessions_in_tree`
    # matched every Claude session on the machine.

    def test_the_tree_judged_is_the_one_the_command_names(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        outside = tmp_path / "elsewhere"
        outside.mkdir()
        _, _, top = run(monkeypatch, capsys, f"git -C {repo} switch feature/x", outside)
        # One spelling on both sides: git answers with forward slashes on Windows.
        expected = {
            os.path.normpath(str(repo)),
            os.path.normpath(os.path.realpath(repo)),
        }
        assert top in expected, f"judged {top!r}; the command acts on {str(repo)!r}"

    def test_a_cwd_that_is_no_repo_is_not_a_tree(self, monkeypatch, capsys, tmp_path):
        """The measured false deny: cwd stood in for the tree root.

        Every session on the machine sits under a home directory, so `startswith`
        matched all of them and an active one denied the switch.
        """
        outside = tmp_path / "not-a-repo"
        outside.mkdir()
        decision, _, top = run(
            monkeypatch,
            capsys,
            "git switch feature/x",
            outside,
            sessions=(ACTIVE, [], True),
        )
        assert decision == "silent", (
            "with no repository there is nothing to keep two sessions out of"
        )
        assert top is None, (
            "session detection ran against a directory that is not a tree"
        )

    def test_a_cd_moves_the_tree_the_guard_judges(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """S10. The rider being discharged named both gates, and the parsing is
        shared: a session that walks to another repository and switches a branch
        there was judged against the tree it started in.

        That is the shape a session takes the moment this very guard refuses a
        `git switch` and tells the user to work in a separate worktree. The
        session stays where it was; the commands do not.
        """
        outside = tmp_path / "elsewhere"
        outside.mkdir()
        _, _, top = run(
            monkeypatch, capsys, f"cd {repo} && git switch feature/x", outside
        )
        expected = {
            os.path.normpath(str(repo)),
            os.path.normpath(os.path.realpath(repo)),
        }
        assert top in expected, f"judged {top!r}; the command switches in {str(repo)!r}"

    def test_a_cd_moves_the_tree_even_when_the_session_sits_in_a_repository(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """S10 in the shape `frame/design.md` states it: "the session sits in `A`".

        The case above seats the session in a directory that is no repository, so
        the pre-fix failure there is `top is None` — the guard finding nothing at
        all. That does not distinguish "judged the wrong tree" from "judged
        nothing", and the wrong tree is the defect. Here the session sits in a
        real repository, so a guard that ignores the `cd` judges THAT one and the
        assertion has something to be wrong about.
        """
        other = tmp_path / "other"
        subprocess.run(["git", "init", "-q", str(other)], check=True)
        subprocess.run(
            [
                "git",
                "-C",
                str(other),
                "-c",
                "user.email=e@example.com",
                "-c",
                "user.name=e",
                "commit",
                "-qm",
                "base",
                "--allow-empty",
            ],
            check=True,
            capture_output=True,
        )
        _, _, top = run(monkeypatch, capsys, f"cd {other} && git switch -c f", repo)
        expected = {
            os.path.normpath(str(other)),
            os.path.normpath(os.path.realpath(other)),
        }
        assert top in expected, (
            f"judged {top!r}; the command switches in {str(other)!r}, and the "
            f"session's own repository is {str(repo)!r}"
        )

    def test_a_cd_to_no_repository_leaves_the_guard_judging_its_own_tree(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """A regression this work introduced: the parent denied, the fix that followed was silent.

        A `cd` whose destination reads cleanly but holds no repository sent the
        guard to `if not top: sys.exit(0)`. With `;` the failing `cd` does not
        stop what follows — it runs in the session's own tree, which is exactly
        the tree another session may be sitting in.

        The commit gate STOPS on a target like this and this guard falls back
        instead, because the two protect different things: a commit nobody judged
        is a commit nobody reviewed, while going silent here leaves a shared tree
        unguarded. A `-C` keeps today's silence — git itself refuses that one, and
        the case below pins it.
        """
        plain = tmp_path / "plain"
        plain.mkdir()
        for command in (
            f"cd {plain} ; git switch feature/x",
            f"cd {plain} && git switch feature/x",
            "cd /no/such/dir ; git switch feature/x",
        ):
            decision, _, top = run(
                monkeypatch, capsys, command, repo, sessions=(ACTIVE, [], True)
            )
            assert decision == "deny", command
            expected = {
                os.path.normpath(str(repo)),
                os.path.normpath(os.path.realpath(repo)),
            }
            assert top in expected, command

    def test_a_relative_chdir_option_composes_onto_the_cd_destination(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """`cd ~/projects && git -C myrepo switch main` — the ordinary shape.

        The fallback for a destination holding no repository ran BEFORE the
        segment's own `-C` was applied, so it threw the destination away and
        composed the relative `-C` onto the session directory instead. A real
        target repository became a path that does not exist, and the guard exited
        at `if not top`.

        The order is what fixes it: compose first, and only fall back when the
        composed directory holds no repository either. The parent directory here
        is deliberately NOT a repository, which is what makes the fallback fire.
        """
        outer = tmp_path / "outer"
        inner = outer / "myrepo"
        inner.mkdir(parents=True)
        subprocess.run(["git", "init", "-q", str(inner)], check=True)
        subprocess.run(
            [
                "git",
                "-C",
                str(inner),
                "-c",
                "user.email=e@example.com",
                "-c",
                "user.name=e",
                "commit",
                "-qm",
                "base",
                "--allow-empty",
            ],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(inner), "branch", "other"],
            check=True,
            capture_output=True,
        )

        _, _, top = run(
            monkeypatch, capsys, f"cd {outer} && git -C myrepo switch other", repo
        )
        expected = {
            os.path.normpath(str(inner)),
            os.path.normpath(os.path.realpath(inner)),
        }
        assert top in expected, (
            f"judged {top!r}; the switch happens in {str(inner)!r}, which the "
            f"relative -C names from the cd destination"
        )

    def test_a_chdir_option_to_no_repository_stays_silent(
        self, monkeypatch, capsys, repo
    ):
        """The other half of the case above, so the fallback cannot widen quietly.

        `git -C <nowhere> switch` fails in git before it touches any tree, so
        there is nothing to protect and the guard says nothing — its answer at
        before this change and the one it keeps.
        """
        decision, _, _ = run(
            monkeypatch,
            capsys,
            "git -C /no/such/dir switch feature/x",
            repo,
            sessions=(ACTIVE, [], True),
        )
        assert decision == "silent"

    def test_a_cd_the_guard_cannot_read_leaves_it_judging_its_own_tree(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """The commit gate stops on a destination it cannot compute, because a
        silent commit is one nobody reviewed. This guard has no such answer to
        give: what it protects is a tree two sessions would share, and with the
        destination unknown the session's own tree is the one still known to be
        shared. Going silent there would be a fail-open, so it keeps today's
        answer rather than acquiring a second stop.
        """
        decision, _, top = run(
            monkeypatch,
            capsys,
            'cd "$WT" && git switch feature/x',
            repo,
            sessions=(ACTIVE, [], True),
        )
        expected = {
            os.path.normpath(str(repo)),
            os.path.normpath(os.path.realpath(repo)),
        }
        assert top in expected
        assert decision == "deny"

    def test_an_active_session_in_the_named_tree_still_denies(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """The fix must not cost the guard its actual job."""
        outside = tmp_path / "elsewhere"
        outside.mkdir()
        decision, reason, _ = run(
            monkeypatch,
            capsys,
            f"git -C {repo} switch feature/x",
            outside,
            sessions=(ACTIVE, [], True),
        )
        assert decision == "deny"
        assert "VS Code" in reason

    def test_the_dirty_tree_row_reads_the_tree_the_switch_is_in(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """Round 1 of work item 1790550712, finding 1. The tracked-changes row
        asked `git status` in the session's own directory while every other row
        judged the tree the switch acts on. So a dirty repository reached by `git
        -C` or `cd` from elsewhere was silent, a clean clone switched from a dirty
        session tree was asked about the session tree's changes, and a dirty clone
        switched from a clean session tree was silent. Seen red at 77ad175 on all
        four."""
        outside = tmp_path / "outside"
        outside.mkdir()
        other = tmp_path / "other"
        subprocess.run(
            ["git", "clone", "-q", str(repo), str(other)],
            check=True,
            capture_output=True,
        )
        (repo / "f.txt").write_text("changed on purpose\n", encoding="utf-8")
        # A force-staged ignored path, which only the target tree's own
        # `check-ignore` can name: `phantom_entries` reads the same tree.
        (repo / ".gitignore").write_text("ign.txt\n", encoding="utf-8")
        (repo / "ign.txt").write_text("x\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-f", "ign.txt"],
            check=True,
            capture_output=True,
        )
        for command in (
            f"git -C {repo} switch feature/x",
            f"cd {repo} && git switch feature/x",
        ):
            decision, reason, _ = run(monkeypatch, capsys, command, outside)
            assert decision == "ask", (command, decision, reason)
            assert "f.txt" in reason, reason
            assert "gitignored path force-staged" in reason, reason
            # Round 2, finding 1: both commands in the note name the tree's root,
            # because the shell is not in that tree and porcelain paths are
            # relative to its root.
            hint = [x.strip() for x in reason.splitlines() if "restore --staged" in x]
            assert hint and hint[0].startswith("git -C "), hint
            assert os.path.samefile(shlex.split(hint[0])[2], repo), hint
            keep = re.search(r"`(git[^`]*) restore <path>`", reason)
            assert keep and keep.group(1).startswith("git -C "), reason
            assert os.path.samefile(shlex.split(keep.group(1))[2], repo), reason
        decision, reason, _ = run(
            monkeypatch, capsys, f"git -C {other} switch feature/x", repo
        )
        assert decision == "silent", (decision, reason)
        (repo / "f.txt").write_text("one\ntwo\nthree\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "reset", "-q", "ign.txt"],
            check=True,
            capture_output=True,
        )
        (other / "f.txt").write_text("changed in the other clone\n", encoding="utf-8")
        decision, reason, _ = run(
            monkeypatch, capsys, f"git -C {other} switch feature/x", repo
        )
        assert decision == "ask", (decision, reason)
        assert "f.txt" in reason, reason

    def test_the_force_staged_check_reads_from_the_root_of_the_tree(
        self, monkeypatch, capsys, repo
    ):
        """Round 2 of work item 1790550712, finding 2. `git status --porcelain`
        names paths from the root of the tree, and `git check-ignore` reads a path
        from where it runs. Reached through a subdirectory, the check asked about
        `sub/ign.txt`, and an anchored pattern named nothing. The third cell, a
        session sitting in the subdirectory, missed it before this work item too."""
        (repo / "sub").mkdir()
        (repo / ".gitignore").write_text("/ign.txt\n", encoding="utf-8")
        (repo / "ign.txt").write_text("x\n", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(repo), "add", "-f", "ign.txt"],
            check=True,
            capture_output=True,
        )
        for command, cwd in (
            (f"cd {repo / 'sub'} && git switch feature/x", repo),
            (f"git -C {repo / 'sub'} switch feature/x", repo),
            ("git switch feature/x", repo / "sub"),
        ):
            decision, reason, _ = run(monkeypatch, capsys, command, cwd)
            assert decision == "ask", (command, decision, reason)
            assert "gitignored path force-staged" in reason, (command, reason)

    def test_every_printed_command_names_the_tree_it_is_about(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """From outside the judged tree, each row that hands the person a command
        names that tree: the switch ladder's ACTIVE deny and idle choice, and the
        creation ladder's single-stream deny and idle choice. From inside it, none
        of them carries `-C`. Seen red before the fix: every command printed from
        outside ran in the shell's own repository, or failed where the shell had
        none."""
        other = tmp_path / "other"
        subprocess.run(
            ["git", "init", "-q", str(other)], check=True, capture_output=True
        )
        idle = [(222, "/tree", 400.0, 90.0, "Terminal")]
        rows = (
            ("switch", "ACTIVE", (ACTIVE, [], True)),
            ("switch", "idle", ([], idle, True)),
            ("worktree add ../wt f", "single", ([], [], True)),
            ("worktree add ../wt f", "idle", ([], idle, True)),
        )
        for n, (verb, state, sessions) in enumerate(rows):
            tail = "feature/x" if verb == "switch" else ""
            for shell in (other, repo):
                command = f"git -C {repo} {verb} {tail}".rstrip()
                monkeypatch.setattr(
                    wg, "sessions_in_tree", lambda t, o="", s=sessions: s
                )
                monkeypatch.setattr(
                    wg,
                    "load_input",
                    lambda command=command, shell=shell, n=n: {
                        "tool_name": "Bash",
                        "session_id": f"p{n}-{shell.name}",
                        "tool_input": {"command": command},
                        "cwd": str(shell),
                    },
                )
                try:
                    wg.main()
                except SystemExit:
                    pass
                out = json.loads(capsys.readouterr().out)["hookSpecificOutput"]
                reason = out["permissionDecisionReason"]
                found = printed_commands(reason)
                assert found, (verb, state, reason)
                for m in found:
                    if shell == repo:
                        assert m.group("at") is None, (verb, state, m.group(0))
                    else:
                        assert m.group("at"), (verb, state, m.group(0))
                        assert os.path.samefile(shlex.split(m.group("at"))[1], repo), (
                            m.group(0)
                        )

    def test_a_cd_behind_a_redirection_leaves_the_guard_on_the_tree_the_base_judged(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """Round 2 of 1790660768 made the guard judge the tree a `cd` behind a
        redirection reaches, and #689 took that back: the guard and the consent
        writer read through `hooks/lib/cmdline_base.py`, which is `86256492`'s reader,
        and that reader does not land these `cd`s. So the guard judges the clean
        session tree and is silent, and the consent writer files the creation
        under the session's clone, while bash runs both in the dirty `w`. That is
        the containment's accepted cost, recorded in #689's spec. The commit gate
        still lands each `cd` (`test_commit_review_gate.py::Test_main`).

        Changed by #689 rather than deleted. It asserted `ask` naming `f.txt`,
        and the consent writer filing under `w`; at the containment it failed on
        the first command with `silent`, the answer `86256492` gives."""
        session = tmp_path / "session"
        session.mkdir()
        subprocess.run(["git", "-C", str(session), "init", "-q"], check=True)
        shutil.copytree(repo, session / "w")
        (session / "w" / "f.txt").write_text("changed on purpose\n", encoding="utf-8")
        for command in (
            "cd w 2>/dev/null && git switch feature/x",
            "2>/dev/null cd w && git switch feature/x",
            "cd>/dev/null w && git switch feature/x",
        ):
            decision, reason, _ = run(monkeypatch, capsys, command, session)
            assert decision == "silent", (command, decision, reason)
        acted = wg.worktree_consent.creation_directory(
            "2>/dev/null cd w && git worktree add ../wt", str(session)
        )
        assert os.path.normpath(acted) == str(session), acted

    def test_a_chain_past_the_walks_cap_keeps_the_tree_the_base_judged(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """Q7 of 1790660768, in the guard. Nine `cd`s landed past their
        redirections carry the walk past `STATE_CAP`, and its collapse left one
        unresolved directory, which the guard reads as the session's own clean
        tree. `86256492`'s walk never reached the cap: every `cd nosuch` fails, so
        the switch runs in the dirty `w`, and that is the tree it judged."""
        session = tmp_path / "session"
        session.mkdir()
        subprocess.run(["git", "-C", str(session), "init", "-q"], check=True)
        shutil.copytree(repo, session / "w")
        (session / "w" / "f.txt").write_text("changed on purpose\n", encoding="utf-8")
        chain = "2>/dev/null cd nosuch; " * 9 + "cd w && "
        decision, reason, _ = run(
            monkeypatch, capsys, chain + "git switch feature/x", session
        )
        assert decision == "ask", (decision, reason)
        assert "f.txt" in reason, reason
        acted = wg.worktree_consent.creation_directory(
            chain + "git worktree add ../wt", str(session)
        )
        assert os.path.samefile(acted, session / "w"), acted

    @pytest.mark.parametrize("name", sorted(BASE_TREE_CHAINS))
    def test_the_guard_judges_the_tree_the_base_judged_whatever_the_walk_leads(
        self, monkeypatch, capsys, repo, tmp_path, name
    ):
        """#689. At `542f920b` each chain was silent: the walk's directory led the
        base's, and it was either a directory the `||` skips or one the `cd`
        never reached. `86256492` asked about the dirty `w`, and so does this."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        chain = BASE_TREE_CHAINS[name].format(
            missing=tmp_path / "nosuch-either", other=other
        )
        decision, reason, top = run(
            monkeypatch, capsys, chain + "git switch feature/x", session
        )
        assert decision == "ask", (name, decision, reason)
        assert "f.txt" in reason, (name, reason)
        assert top and os.path.samefile(top, session / "w"), (name, top)

    @pytest.mark.parametrize("name", sorted(PLACEMENT_CHAINS))
    def test_the_writer_files_under_the_clone_the_guard_judged(
        self, monkeypatch, capsys, repo, tmp_path, name
    ):
        """S3 of work item 1791384157. For every chain, the clone the consent
        writer files a creation under is the clone the guard judged it in: the
        guard's `main` and the writer's `creation_directory` are two paths
        through one placement. Red at `5623d728` on the two chains above."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        chain = PLACEMENT_CHAINS[name].format(
            missing=tmp_path / "nosuch-either", other=other
        )
        command = chain + "git worktree add ../wt f"
        judged = _the_tree_the_guard_judges_a_creation_in(
            monkeypatch, capsys, command, session
        )
        acted = wg.worktree_consent.creation_directory(command, str(session))
        filed = wg.worktree_consent.optin.repo_root(acted)
        assert judged and filed, (name, judged, acted)
        assert os.path.samefile(judged, filed), (name, judged, filed)

    def test_a_git_only_the_reading_past_redirections_finds_stops_in_its_segments_tree(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """#689. `2>/dev/null nice -n 5 git switch` is git only to the reading
        past redirections (#674). The guard reads through `86256492`'s frozen
        reader, which finds no git there, while bash switches `w`.

        Changed by round 1 of 1790745049, by phase 4 of 1790993140 (#678's
        candidate C, which asked about it with no tree), and by phase 3 of
        1791270162 (#826): the segment is an unrecognised shape now, judged in the
        tree its segment names, which the frozen walk places in the dirty `w`, so
        the stop asks there. It asserted `top is None`, C's tree-less question."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        decision, reason, top = run(
            monkeypatch,
            capsys,
            "cd w && 2>/dev/null nice -n 5 git switch feature/x",
            session,
        )
        assert decision == "ask", (decision, reason)
        assert "`2>/dev/null nice -n 5 git switch feature/x`" in reason, reason
        assert top and os.path.samefile(top, session / "w"), top

    @pytest.mark.parametrize("command", WIDER_FIRST)
    def test_a_segment_the_base_reads_no_git_in_does_not_take_the_first_slot(
        self, monkeypatch, capsys, repo, tmp_path, command
    ):
        """Round 1 of 1790745049, red 1. bash switches `w`, and `86256492` denied
        each command over the session active in `w`. At `4bc94f05` the first
        segment took the slot and the guard judged the session's own tree.

        Rewritten by phase 3 of 1791270162 (#826): the hidden segment in front
        is an unrecognised shape judged in its own tree, the clean session tree
        (`clean` for the last command) with nobody else in it, so it says
        nothing there, and the switch the frozen reading reads keeps the slot and
        is denied over the session active in `w`. The stub used to put an ACTIVE
        session in every tree, which now stops on the hidden shape first."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        w = session / "w"
        active = [(111, str(w), 1.0, 0.5, "VS Code")]
        decision, reason, top = run(
            monkeypatch,
            capsys,
            command,
            session,
            sessions=lambda t: (
                (active, [], True) if os.path.samefile(t, w) else ([], [], True)
            ),
        )
        assert decision == "deny", (command, decision, reason)
        assert "Blocking this branch switch" in reason, reason
        assert top and os.path.samefile(top, w), (command, top)

    @pytest.mark.parametrize("shape", ZSH_PREFIXED)
    def test_a_zsh_prefixed_git_is_not_git_to_the_guard_or_the_consent_writer(
        self, monkeypatch, capsys, repo, tmp_path, shape
    ):
        """Round 1 of 1790745049, yellow 2. The guard does not judge the tree,
        and the consent writer files nothing, as at `86256492`. At `4bc94f05` the
        guard judged the session's tree and denied, and the writer filed the
        creation under the session's clone.

        Changed by phase 4 of 1790993140 (#678's guard half): it asserted
        `silent` over the ACTIVE session, then `ask`, candidate C's question with
        no tree. Changed again by phase 3 of 1791270162 (#826): the shape is
        unrecognised and judged in `w`, where a session is ACTIVE, so the stop is
        a `deny` whoever is at the keyboard (`questions.md` P5) and names the
        plain spelling. The writer's half is unchanged."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        active = [(111, str(session / "w"), 1.0, 0.5, "VS Code")]
        decision, reason, top = run(
            monkeypatch,
            capsys,
            shape.format(verb="switch feature/x"),
            session,
            sessions=(active, [], True),
        )
        assert decision == "deny", (shape, decision, reason)
        assert "Write `git` first" in reason, reason
        assert top and os.path.samefile(top, session / "w"), (shape, top)
        acted = wg.worktree_consent.creation_directory(
            shape.format(verb="worktree add ../wt"), str(session)
        )
        assert acted == "", (shape, acted)

    # #686 and #678's guard half, decided by a count: both were built in phase
    # 2 of work item 1790993140 and counted in phase 3 over the recorded runs.
    # #686's ask fired on 9 recorded pairs and was removed, so its fallback is
    # a known limit. #678's question was wired, and #826 replaced it with the
    # unrecognised-shape stop.

    @pytest.mark.parametrize("name", sorted(UNPLACED))
    def test_a_switch_tree_the_guard_cannot_place_is_judged_as_its_own(
        self, monkeypatch, capsys, repo, tmp_path, name
    ):
        """`docs/worktree-guard-spec.md` *Known limits*: asking here would have
        stopped 9 of the 27,351 recorded command and directory pairs, so the
        fallback stays (phase 3 of work item 1790993140). Seen red against a
        mutant whose last silent exit asks."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        decision, reason, _ = run(monkeypatch, capsys, UNPLACED[name], session)
        assert decision == "silent", (name, decision, reason)

    def test_a_one_tree_reason_calls_the_tree_it_judges_this_tree(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """`docs/worktree-guard-spec.md` *A. Branch switch*: a reason that describes one tree
        calls it "this tree", whichever tree it is, so with the session's tree
        clean and `w` dirty the reason about `w` names no path (#854, round 3 of
        work item 1791270162, white 2)."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        decision, reason, top = run(
            monkeypatch, capsys, "git -C w checkout feature/x", session
        )
        assert decision == "ask", (decision, reason)
        assert top and os.path.samefile(top, session / "w"), top
        assert "in this tree a branch switch would matter" in reason, reason
        assert str(session / "w") not in reason, reason

    @pytest.mark.parametrize("name", sorted(WIDER_ONLY))
    def test_a_git_only_the_wider_reading_finds_stops_where_its_tree_matters(
        self, monkeypatch, capsys, repo, tmp_path, name
    ):
        """#678's guard half asked each of these with no tree (candidate C, silent
        at `233f0455`). Since #826 each is an unrecognised shape, judged in the
        tree its segment names, the dirty `w`, and stopped there with its plain
        spelling. The two creations hidden behind a redirection after `worktree`
        were silent at `9c03ae85`, where `worktree` was listed whatever stood
        where git reads `add` (phase 3 of 1791270162)."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        command, _kind = WIDER_ONLY[name]
        decision, reason, top = run(monkeypatch, capsys, command, session)
        assert decision == "ask", (name, decision, reason)
        # The stop's text, or the ladder's where an `&` cut leaves the frozen
        # reading a plain `git switch` (`&>` between switch and its name).
        assert "uncommitted tracked changes" in reason, reason
        assert top and os.path.samefile(top, session / "w"), (name, top)

    @pytest.mark.parametrize(
        "name", sorted(k for k, (_c, kind) in WIDER_ONLY.items() if kind == "creation")
    )
    def test_a_creation_only_the_wider_reading_finds_stops_whatever_the_consent_record(
        self, monkeypatch, capsys, repo, tmp_path, name
    ):
        """`questions.md` D10 of 1790993140 read consent first for these, as for
        every creation, and #734 found it read against the wrong clone. Since
        #826 the stop reads no consent record (`frame/design.md` In 3 of 1791270162): a
        creation having run says nothing about whether this one is plain, and
        the plain retry meets *B. Worktree creation*, which reads its own clone's consent."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        assert wg.worktree_consent.record(str(session), "me")
        assert wg.worktree_consent.record(str(session / "w"), "me")
        decision, reason, _ = run(monkeypatch, capsys, WIDER_ONLY[name][0], session)
        assert decision == "ask", (name, decision, reason)

    @pytest.mark.parametrize(
        "first", ["git checkout README.md && ", "git checkout nosuch; "]
    )
    def test_a_shape_in_a_clean_tree_takes_no_stop_from_one_in_a_dirty_tree(
        self, monkeypatch, capsys, repo, tmp_path, first
    ):
        """Round 1 of 1790993140, yellow 3, in #826's terms. The `checkout` in
        front is unrecognised in the clean session tree, which matters to nobody,
        and the switch behind the redirection is unrecognised in the dirty `w`.
        Each shape is judged in its own tree, so the second still stops, and the
        stop lists both. Silent at `9c03ae85`, where only the first unrecognised
        shape's tree was read."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        command = f"{first}cd w && 2>/dev/null {SWITCH}"
        decision, reason, top = run(monkeypatch, capsys, command, session)
        assert decision == "ask", (decision, reason)
        assert f"`2>/dev/null {SWITCH}`" in reason, reason
        assert f"`{first.split(' &&')[0].rstrip('; ')}`" in reason, reason
        assert top and os.path.samefile(top, session / "w"), top

    def test_each_tree_is_placed_once_however_many_shapes_it_holds(
        self, monkeypatch, capsys, repo
    ):
        """#826, phase 3. Each unrecognised shape is judged in its own tree, and
        a tree is looked up once, so three `checkout`s in one clean tree cost one
        `repo_paths` for the stop, not three. Survived a break dropping the
        dedupe until this case; red with it dropped."""
        asked = []
        real = wg.repo_paths

        def counting(cwd):
            asked.append(cwd)
            return real(cwd)

        monkeypatch.setattr(wg, "repo_paths", counting)
        command = "git checkout a; git checkout b; git checkout c"
        decision, reason, _ = run(monkeypatch, capsys, command, repo)
        assert decision == "silent", (decision, reason)
        assert asked == [str(repo)], asked

    def test_a_hidden_switch_behind_a_judged_one_adds_no_question(
        self, monkeypatch, capsys, repo
    ):
        """The kind the frozen loop judged keeps its verdict: a clean single
        stream lets the switch through, and a second switch only the wider
        reading finds is not asked about. Since #826 the second is an
        unrecognised shape, and its tree is the same clean single-stream one, so
        it says nothing there either."""
        command = f"{SWITCH}; 2>/dev/null git switch main"
        decision, reason, top = run(monkeypatch, capsys, command, repo)
        assert decision == "silent", (decision, reason)
        assert top and os.path.samefile(top, repo), top

    def test_a_hidden_creation_behind_a_judged_one_adds_no_question(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """The judged creation's own clone has consent, so its verdict is
        silence; a second creation only the wider reading finds is not asked
        about. Since #826 the second is an unrecognised shape judged in the tree
        its `-C` names, which is clean with nobody else in it, so it says
        nothing there."""
        elsewhere = tmp_path / "elsewhere"
        elsewhere.mkdir()
        assert wg.worktree_consent.record(str(repo), "me")
        command = (
            f"git -C {repo} worktree add ../wt-a -b a && "
            f"git -C {repo} 2>&1 worktree add ../wt-b -b b"
        )
        decision, reason, _ = run(monkeypatch, capsys, command, elsewhere)
        assert decision == "silent", (decision, reason)

    @pytest.mark.parametrize("name", sorted(PLACED_SWITCHES))
    def test_a_switch_wherever_its_redirection_stands_is_stopped_in_a_dirty_tree(
        self, monkeypatch, capsys, repo, tmp_path, name
    ):
        """bash runs each as a switch (phase 1 of 1791119071, executed). All but
        R5 were silent at `94d7b2e0`. Since #826 R0-R4 are a `checkout` with no
        `-- <path>`, unrecognised and stopped in the dirty tree before the
        ladder, and R5 meets the ladder's dirty-tree row; both texts name the
        uncommitted changes, in the tree the segment names. It asserted the
        ladder's file list for all six."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        decision, reason, top = run(
            monkeypatch, capsys, f"cd w && {PLACED_SWITCHES[name]}", session
        )
        assert decision == "ask", (name, decision, reason)
        assert "uncommitted tracked changes" in reason, (name, reason)
        assert top and os.path.samefile(top, session / "w"), (name, top)

    @pytest.mark.parametrize(
        "command",
        [
            "git checkout -- f.txt 2>/dev/null",
            "git checkout -- 2>/dev/null f.txt",
            "git checkout --conflict 2>/dev/null merge -- f.txt",
        ],
    )
    def test_a_restore_with_its_dashes_stays_silent_wherever_its_redirection_stands(
        self, monkeypatch, capsys, repo, tmp_path, command
    ):
        """The tree used to tell the file from the branch (`plan.md` Alternatives
        A of 1791119071); since #826 the `--` does, and a redirection among the
        words after it is no path, so a restore with a path after its `--` keeps
        its silence in the dirty `w`. It asserted the silence of the same three
        restores without their `--`, which are unrecognised now."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        decision, reason, _ = run(monkeypatch, capsys, f"cd w && {command}", session)
        assert decision == "silent", (command, decision, reason)

    def test_a_message_search_over_a_dirty_tree_is_asked(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """`frame/design.md` A3 of 1791163981, #790's own shape through `main()`: `git
        checkout ':/<message>'` detaches at the newest commit whose message
        matches, so it moves a dirty tree. Red at `a3aa139a`, where it was
        silent. Since #826 nothing is looked up: a `checkout` with no `-- <path>`
        is unrecognised and stopped in the dirty tree, so the search matching
        nothing, which git refuses, is stopped too, where it used to be silent
        because the lookup found nothing. Its plain spelling is `git switch
        --detach ':/<message>'`, which the stop names."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        for search in ("':/base'", "':/nomatch-xyz'"):
            decision, reason, top = run(
                monkeypatch, capsys, f"cd w && git checkout {search}", session
            )
            assert decision == "ask", (search, decision, reason)
            assert "git switch --detach <rev>" in reason, reason
            assert top and os.path.samefile(top, session / "w"), (search, top)

    @pytest.mark.parametrize("name", sorted(BODY_TOKENS))
    def test_a_token_only_a_body_carries_is_not_read(
        self, monkeypatch, capsys, repo, name
    ):
        """`frame/design.md` A6. A `[shared-tree-ok]` only a body carries leaves the
        cannot-tell row's choice in place, and a `[worktree-ok]` only a body
        carries leaves the single-stream creation denied. Red at `a3aa139a`, where
        the first was silent and the second asked."""
        command, token = BODY_TOKENS[name]
        assert not wg.has_token(command, token), name
        if token == "[shared-tree-ok]":
            decision, reason, _ = run(
                monkeypatch, capsys, command, repo, sessions=([], [], False)
            )
            assert decision == "deny", (name, decision, reason)
            assert "[shared-tree-ok]" in reason, reason
        else:
            decision, reason, _ = run(monkeypatch, capsys, command, repo)
            assert decision == "deny", (name, decision, reason)
            assert "[worktree-ok]" in reason, reason

    @pytest.mark.parametrize(
        "behind",
        [
            "git -C {other} switch feature/x",
            "2>/dev/null git -C {other} switch feature/x",
        ],
        ids=["a switch the frozen reading reads", "a switch only candidate C reads"],
    )
    @pytest.mark.parametrize(
        "front", ["git checkout ':/base'", "git checkout ':/nomatch'"]
    )
    def test_a_newly_read_checkout_in_front_takes_no_question_away(
        self, monkeypatch, capsys, repo, tmp_path, front, behind
    ):
        """Round 1 of 1791163981, yellow 3. A `checkout` in a clean single-session
        tree stands in front of a switch in a second, dirty tree. `a3aa139a`
        read no switch in front, so it judged the second tree's switch, or
        candidate C asked about it; the guard still asks. The two `:/base` cases
        were red at `85e77dc8`, where the checkout took the slot and C's question.

        Since #826 the `checkout` is unrecognised in the clean tree, which takes
        no stop, and the switch behind it is judged in `other`: by the ladder
        where the frozen reading reads it, and as an unrecognised shape in its
        own tree where only the wider reading does. The second pair was silent at
        `9c03ae85`, where only the first unrecognised shape's tree was read."""
        other = _a_dirty_clone_beside(repo, tmp_path)
        command = f"{front} && {behind.format(other=other)}"
        decision, reason, _ = run(monkeypatch, capsys, command, repo)
        assert decision == "ask", (command, decision, reason)


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

    def test_a_restore_inside_a_subshell_is_listed_by_its_dashes_alone(self):
        """A closing parenthesis rides on the last word, and since #826 no word is
        looked up, so nothing has to peel it: `(git checkout -- README.md)` holds
        a path after `--` and is listed, and the two without one are
        unrecognised, inside a subshell as outside it."""
        for command, shape in (
            ("(git checkout -- README.md)", "listed"),
            ("(git checkout README.md)", "unrecognised"),
            ("(git checkout .)", "unrecognised"),
            ("(git checkout feature/x)", "unrecognised"),
        ):
            segments, _ = wg.split_command(command)
            assert wg.shape_of(segments[0]) == shape, command

    def test_no_redirection_makes_a_moving_verb_listed_wherever_it_stands(self):
        """#826, phase 3. For every operator `_REDIRECTION` names, at every
        position, glued to the word before it and spaced, its target glued and
        spaced, a verb that can move a branch or add a worktree is never read as
        listed: it is a switch, a creation, or an unrecognised shape the stop
        names. Red at `9c03ae85` on 208 of the 2,356 shapes, 104 each of `worktree
        add` and `stash branch`, whose deciding word a redirection stood in front
        of, was glued to, or cut away with an `&`: `worktree` and `stash` were
        listed by their subcommand alone (a deleted probe, phase 3). With the
        targets widened to a closed and a moved descriptor and a word ending in
        `-` (round 1, red 2), red at `4de95fa7` on 110 of 4,712 shapes, every one
        a target ending in `-` that `_plain_words` read as taking the next word
        (`git worktree 2>&- add`, `>-`, `<<<-`, `<>-`)."""
        silent = [
            command
            for verb in MOVING
            for command, *_where in _placed(verb)
            if not _read_by_the_guard(command)
        ]
        assert not silent, (len(silent), silent[:10])

    def test_a_redirection_after_a_listed_verbs_words_keeps_it_listed(self):
        """The other direction, so the rule above cannot be met by stopping
        everything: a listed verb with any redirection written after its own
        words, glued or spaced, is still listed and costs no stop. `git stash
        2>/dev/null` hides no word, while `git stash 2>/dev/null branch x` does.
        One placement is left out, a redirection glued to the subcommand itself
        (`git status>/dev/null`): the frozen reading takes that word for the
        subcommand, and phase 2 made it a shape of its own whose rewrite moves
        the redirection (`questions.md` W3). Red at `9c03ae85` on 24 shapes, a
        path glued to its redirection after `--` read as no path, and on 96
        against this phase's first draft, which read `git worktree list>/dev/null`
        as hiding a word (a deleted probe and a run, phase 3)."""
        stopped = [
            (command, _read_by_the_guard(command))
            for verb in LISTED_VERBS
            for command, at, glued, *_rest in _placed(verb)
            if at == len(verb.split()) + 1
            and not (glued and at == 2)
            and _read_by_the_guard(command)
        ]
        assert not stopped, (len(stopped), stopped[:10])

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

# Phase 1 of work item 1791270162, its `trail/phases/phase-1.md`, measurement M1: every git
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
# What the frame judges does not leave the branch (`frame/design.md` In 5), and the
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
    """S11 of work item 1791270162. None of the symbols `frame/design.md` In 4
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
