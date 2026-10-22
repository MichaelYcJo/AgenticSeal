"""Under `automation`, the switch ladder's two choice rows ask nobody (#896).

Work item 1791781864. `docs/worktree-guard-spec.md` §A's rows *only IDLE
sessions* (row 1-b) and *detection unusable* (row 2) are `choose` sites: a
`deny` once per session that tells the model to put two options to the
person with `AskUserQuestion`, and an `ask` on every attempt after. On the
0.21.0 run that was a person's prompt one step removed, in a session whose
person had pressed `automation` on the routing question, which says nobody
is at the keyboard.

Under the press both rows now `deny` on every attempt. Where a creation in
the switch's clone is consented -- by the press in the clone it was given
in, or by this session's record in a clone it already created a worktree
in -- the reason names the one way on that needs nobody: split into a
worktree and work there by path. In another clone it names no split,
because a creation there would be put to a person (round 1). It names no
question tool and no token, and it writes no choice marker, because no
question was put. Attended, both rows are the base's byte for byte
(`tests/test_worktree_guard.py`, S5).

The press is read by `automation_pressed` against the session's own root,
the reader the unrecognised-shape stop already uses, and only where one of
the two rows fires. Every case plants the press the way the harness writes
it, under a projects root this file owns.
"""

import json
import pathlib
import shlex
import shutil
import subprocess
import sys

import pytest
from conftest import load_hook_module
from test_the_guard_asks_once_per_session import (
    ACTIVE,
    IDLE,
    TOKEN,
    ask_entries,
    consent_dir,
    dirty_deny,
    grant,
    wg,
    write_transcript,
)

STOP = "does not know to leave the branch where it is"


@pytest.fixture
def projects(monkeypatch, tmp_path):
    """A projects root this case owns. Every loaded copy of the guard imports
    the one `worktree_consent`, so one patch reaches both languages."""
    root = tmp_path / "projects"
    root.mkdir()
    monkeypatch.setattr(wg.worktree_consent, "PROJECTS_ROOT", str(root))
    return root


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


def dirty(repo):
    (repo / "f.txt").write_text("changed\n", encoding="utf-8")


# --- W1: the deny's one text, both rows, both languages ---------------------

IDLE_LINES = {
    "en": "    pid 222 (Terminal terminal)  /tree\n"
    "        terminal in/out 6.7h ago · transcript activity 1.5h ago",
    "ko": "    pid 222 (Terminal 터미널)  /tree\n"
    "        터미널 입력/출력 6.7시간 전 · 작업 기록(트랜스크립트) 1.5시간 전",
}


def situation(lang, row, idle_min):
    """Each row's opening, as it reads attended: row 1-b's header and its
    idle sessions, and row 2's cannot-tell sentence."""
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
    """True when no choice marker was written for SESSION in REPO."""
    gd = module.git_dir(str(repo))
    return not (pathlib.Path(gd) / module.CHOICE_DIR / "switch" / session).exists()


ROWS = {"idle": ([], IDLE, True), "unusable": ([], [], False)}


@pytest.mark.parametrize("row", ["idle", "unusable"])
def test_under_the_press_a_choice_row_denies_every_attempt(
    monkeypatch, capsys, projects, repo, wko, row
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


def test_the_token_still_reads_as_it_does_attended(monkeypatch, capsys, projects, repo):
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


def git_ok(*args):
    r = subprocess.run(
        ["git", *args], capture_output=True, encoding="utf-8", errors="replace"
    )
    assert r.returncode == 0, (args, r.stdout, r.stderr)
    return r.stdout.strip()


def test_the_way_on_passes_the_guard(monkeypatch, capsys, projects, repo, tmp_path):
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
        "-C", str(repo), "worktree", "add", "-q", wt, "-b", "feature/y", "origin/main"
    )
    assert git_ok("-C", wt, "branch", "--show-current") == "feature/y"
    status = f"git -C {shlex.quote(wt)} status"
    assert judge(wg, monkeypatch, capsys, repo, status, idle) == ("silent", "")


def test_a_creation_on_the_same_line_is_stopped_with_it(
    monkeypatch, capsys, projects, repo
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
    monkeypatch, capsys, projects, repo
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
    monkeypatch, capsys, projects, repo
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


def test_the_press_is_read_from_the_sessions_own_root(
    monkeypatch, capsys, projects, repo, tmp_path
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
    monkeypatch, capsys, projects, repo
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
    monkeypatch, capsys, projects, repo, tmp_path, wko
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
    monkeypatch, capsys, projects, repo, tmp_path, wko
):
    """Round 1, red 1, the record's half. Where this session already created a
    worktree in the other clone, its creation record is consent there
    (`worktree_consent.granted`), so the switch into that clone names the
    split as it does in the session's own clone, and says the record
    consents rather than the press, which consents only in the clone it was
    given in (round 2). Both languages. Seen red with the record's branch
    taken out of the clone test through `mutation-check` (round 1), and
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
