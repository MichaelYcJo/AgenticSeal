"""Under `automation`, a creation in another clone asks nobody (#903).

Work item 1791852612. `docs/worktree-guard-spec.md` *B. Worktree creation*, its rows *only IDLE
sessions* (row 3) and *detection unusable* (row 4) are `choose` sites: a
`deny` once per session that tells the model to put two options to the
person with `AskUserQuestion`, and an `ask` on every attempt after. In the
clone the press was given in they are never reached under it, because row 0
reads the press as consent first. In another clone it is not consent
(`worktree_consent.automation_answered`, condition 4), and where this session
holds no record there either, the ladder fell through to those two rows and
put the creation to a person who had said nobody would be answering --
round 1 of work item 1791781864 found the switch rows' deny steering the
model into exactly that.

Under the press both rows now `deny` on every attempt. The reason opens with
the row's situation, carries #896's press sentence, says the answer consents
to a creation only in the clone it was given in and nobody is at the
keyboard to choose for this one, names no way on, no question tool and no
token, and ends with #896's re-issue sentence. It writes no choice marker,
because no question was put. Attended, both rows are the base's byte for
byte (`tests/test_worktree_guard.py`, S3).

The press is read by `automation_pressed` against the session's own root,
the reader the switch rows and the stop use, and only where one of the two
rows fires. Every case plants the press the way the harness writes it, under
a projects root the case owns (`projects`), and makes the other clone as a
copy of the `repo` fixture, as the switch side's other-clone case does.
"""

import json
import pathlib
import shlex
import shutil
import sys

import pytest
from conftest import load_hook_module
from test_the_guard_asks_once_per_session import (
    IDLE,
    ask_entries,
    consent_dir,
    grant,
    wg,
    write_transcript,
)
from test_the_idle_session_rows_ask_nobody import assert_names_nobody, judge

ROWS = {"idle": ([], IDLE, True), "unusable": ([], [], False)}

IDLE_LINES = {
    "en": "    pid 222 (Terminal terminal)  /tree\n"
    "        terminal in/out 6.7h ago · transcript activity 1.5h ago",
    "ko": "    pid 222 (Terminal 터미널)  /tree\n"
    "        터미널 입력/출력 6.7시간 전 · 작업 기록(트랜스크립트) 1.5시간 전",
}


def situation(lang, row, idle_min):
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


def elsewhere(lang):
    """What follows the opening under the press: #896's press sentence, why
    no way on is named for a creation in a clone the press was not given in,
    and #896's re-issue sentence."""
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


def unattended(lang, row):
    """The whole deny for ROW, for a creation in another clone."""
    return situation(lang, row, wg.IDLE_MIN) + "\n\n" + elsewhere(lang)


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
    return load_hook_module("worktree-guard.py", "wg_903_ko")


@pytest.fixture
def other(repo, tmp_path):
    """A second clone of the same history, beside `repo`, and its root."""
    d = tmp_path / "other-repo"
    shutil.copytree(repo, d)
    return wg.repo_paths(str(d))[0]


def creation(top, tail=""):
    return f"git -C {shlex.quote(top)} worktree add ../wt feature/x{tail}"


def no_marker(module, top, session="me"):
    """True when no creation-side choice marker was written for SESSION."""
    gd = module.git_dir(top)
    return not (pathlib.Path(gd) / module.CHOICE_DIR / "create" / session).exists()


def no_record(*tops, session="me"):
    """True when neither clone holds a consent record for SESSION."""
    return not any((consent_dir(t) / session).exists() for t in tops)


@pytest.mark.parametrize("row", ["idle", "unusable"])
def test_under_the_press_a_creation_row_denies_every_attempt(
    monkeypatch, capsys, projects, repo, other, wko, row
):
    """S1 (row 3) and S2 (row 4). Three attempts, one deny text each time, in
    both languages, naming no way on and nothing a person would answer, and
    neither a choice marker nor a consent record left behind. Seen red at
    `321e9de1`, both rows: the first attempt was the attended deny naming
    `AskUserQuestion`."""
    write_transcript(projects, "me", ask_entries(repo))
    for lang, module in (("en", wg), ("ko", wko)):
        want = unattended(lang, row)
        for attempt in range(3):
            got = judge(module, monkeypatch, capsys, repo, creation(other), ROWS[row])
            assert got == ("deny", want), (lang, attempt, got)
            assert_names_nobody(got[1])
            # The origin line names the command being judged; nothing after
            # it names one to run.
            assert "worktree add" not in got[1].split("\n", 1)[1], got
        assert no_marker(module, other), lang
    assert no_record(repo, other)


def test_a_record_in_the_other_clone_outranks_the_rows(
    monkeypatch, capsys, projects, repo, other
):
    """S5. This session's record in the other clone is consent there, read at
    row 0 before any row below it, so the creation is allowed with the
    record's text and the deny is never reached. Green at `321e9de1`, which is
    the point; seen red through `mutation-check` with row 0's read taken
    out."""
    write_transcript(projects, "me", ask_entries(repo))
    grant(other)
    decision, reason = judge(
        wg, monkeypatch, capsys, repo, creation(other), ROWS["idle"]
    )
    assert decision == "allow", reason
    assert "A worktree creation already ran in this repository" in reason, reason


def test_the_token_still_reaches_its_own_row(
    monkeypatch, capsys, projects, repo, other
):
    """S6. `[worktree-ok]` is read at row 2, above both choice rows, and its
    row is an `ask` under the press as attended. The deny names no token, so
    a model that appends one read it elsewhere, and the command line records
    that it did. Green at `321e9de1`; seen red through `mutation-check` with
    row 2 taken out."""
    write_transcript(projects, "me", ask_entries(repo))
    tagged = creation(other, "  # [worktree-ok]")
    decision, reason = judge(wg, monkeypatch, capsys, repo, tagged, ROWS["idle"])
    assert decision == "ask", reason
    assert "[worktree-ok] was given" in reason, reason
    assert "pressed `automation`" not in reason, reason


def test_the_press_is_read_from_the_sessions_own_root(
    monkeypatch, capsys, projects, repo, other, tmp_path
):
    """S7. Whether anybody is at the keyboard is a fact about the session, so
    the rows read the press against the root the shell stands in. A press
    given only in a third clone leaves the attended first attempt, and a
    press given in the creation's own clone is consent there at row 0. Green
    at `321e9de1` for both halves; seen red through `mutation-check` with the
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
    monkeypatch, capsys, projects, repo, other, wko, row
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
            assert got == ("deny", unattended(lang, row)), (lang, attempt, got)
            assert_names_nobody(got[1])


@pytest.mark.parametrize("row", ["idle", "unusable"])
def test_attended_an_unbalanced_quote_keeps_the_quote_note(
    monkeypatch, capsys, projects, repo, other, wko, row
):
    """Attended, rows 3 and 4 open with the origin and its quote note, as at
    the base: only the press drops the note (round 2, note 5). No transcript
    is planted, so nothing is pressed; each language is its own session, so
    each meets its first attempt. Seen red through `mutation-check` with the
    attended arm of both rows' `lead` dropped."""
    command = creation(other, "  # don't")
    for lang, module in (("en", wg), ("ko", wko)):
        decision, reason = judge(
            module, monkeypatch, capsys, repo, command, ROWS[row], f"att-{lang}"
        )
        assert decision == "deny" and "AskUserQuestion" in reason, (lang, reason)
        assert "[worktree-ok]" in reason.splitlines()[0], (lang, reason)


def test_a_creation_behind_a_cd_meets_the_same_deny(
    monkeypatch, capsys, projects, repo, other
):
    """S8. A creation reached through a `cd` into the other clone is the same
    creation: the deny stops the whole line with S1's text, and with the
    command stopped no `PostToolUse` writer runs, so no record is minted for
    a creation nobody was asked about. Seen red at `321e9de1`, where the
    reason named `AskUserQuestion`."""
    write_transcript(projects, "me", ask_entries(repo))
    command = f"cd {shlex.quote(other)} && git worktree add ../wt feature/x"
    got = judge(wg, monkeypatch, capsys, repo, command, ROWS["idle"])
    assert got == ("deny", unattended("en", "idle")), got
    assert no_marker(wg, other)
    assert no_record(repo, other)


def test_the_transcript_is_read_at_most_twice_per_creation(
    monkeypatch, capsys, projects, repo, other
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


@pytest.mark.skipif(
    sys.platform != "win32",
    reason="M1: the reading that every Windows creation is row 4 is Windows's",
)
def test_on_windows_a_creation_in_another_clone_is_row_fours_deny(
    monkeypatch, capsys, projects, repo, other
):
    """S11, M1 of work item 1791852612, measured by the Windows shards.
    Nothing is stubbed: `sessions_in_tree` runs as it does there, where `ps`
    takes no `-o` and detection reads unusable. If the reading is wrong, this
    case is where it shows, and `docs/worktree-guard-spec.md` *Known limits*
    is corrected in this work item. Seen red at `321e9de1` off Windows, by a
    deleted probe that ran this body with the process scan stubbed to read
    unusable: the attended deny."""
    got = windows_creation(monkeypatch, capsys, projects, repo, other)
    assert got == ("deny", unattended("en", "unusable")), got
