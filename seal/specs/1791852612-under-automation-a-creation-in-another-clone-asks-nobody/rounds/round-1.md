# 1791852612-under-automation-a-creation-in-another-clone-asks-nobody — review round 1

| Field | Value |
|---|---|
| Target SHA | 9e7514f351f3b949d44ec180a4b31d85d6d9f1aa |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #916 |
| Broad gate | not yet |
| Fixes checked by | round-2 |
| Fix range | `6528e2ebabe8d2dee8936057f9d5de69623f0c2c..462e6dd53ba1b9ed107a4d99de05ab382972c66d`, 2 commits |
| Contract changes | guard_worktree_creation → judge_creation, round-1-report.md, round-1.md |
| New units | test_an_unbalanced_quote_under_the_press_names_no_token (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (an unbalanced quote puts `[worktree-ok]` into the deny under the press), 🟡 2 (the third copy of the shared sentences drifts silently), 🟡 3 (both READMEs say a creation is never asked under the press) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 1 of #903, target 9e7514f3 against `origin/release/v0.21.1` at 321e9de1, over the whole build, phases 1–2, under the owner's decision on #903 (the creation direction's two choice rows deny to the model under the press; row 1, ACTIVE, outside it). The reviewer was asked to judge the smith's divergences in `overview.md` — S10 pinned as `[1, 2, 1, 2]`, S1's check after the origin line only, the prompt-budget sentence narrowed to the clone the press was given in, #896's S13 closed as `Corrected ·`, three half-false sentences rewritten — and the copy of the press and re-issue sentences left inside `main`'s #894 tracked-changes deny, outside W1.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | under the press, a creation with an unbalanced quote gets rows 3 and 4's deny with the origin's quote note, which names `[worktree-ok]` and invites a re-issue; the token retry reaches row 2's `ask`, a person's prompt | `hooks/worktree-guard.py:2008` | **fixed** `462e6dd5` | fixed at 462e6dd5; executed (probe 3): both rows, two attempts each, `deny` naming `[worktree-ok]`; the retry with the token was `ask`. Contradicts `spec.md` In 1 and `docs/worktree-guard-spec.md` §*A creation in another clone under the press* |
| 🟡 2 | #894's tracked-changes deny under the press keeps inline copies of both shared sentences; a reword of `press_sentence` leaves it behind with every case green, so the ground `phases/phase-1.md` gives for leaving it is false | `hooks/worktree-guard.py:3555` | **fixed** `462e6dd5` | fixed at 462e6dd5; executed (probe 5): `press_sentence` English reworded, `tests/test_the_guard_asks_once_per_session.py` 101 passed exit 0, `tests/test_the_idle_session_rows_ask_nobody.py` 7 failed; ledger S9 says one string each |
| 🟡 3 | both READMEs say a creation is not asked at all under the press; row 1 still asks in another clone, the reason the policy's budget sentence was narrowed | `README.md:201` | **fixed** `85be560f` | fixed at 85be560f; read: `hooks/worktree-guard.py#guard_worktree_creation` row 1 is above the press; overview divergence 3; `README.ko.md:198` is the same claim |
| ⬜ 4 | #896's S13 `Corrected ·` row keeps claims about §*What a blocking prompt must show* and §*Unknowns resolve conservatively* but no longer cites either section | `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md:30` | open | read: `seal/releases/0.21.0.md:748` cited both; both headings stand at `9e7514f3`; correction to the run's paperwork |
| 🟢 | rows 3 and 4 deny on every attempt under the press in another clone, with one text, both languages, no marker | `hooks/worktree-guard.py:1892` | confirmed | executed (probe 1): S1, S2, S8 green at `9e7514f3`; probe 2: red at `321e9de1`'s guard |
| 🟢 | the frame's seen-red claims hold: S1, S2, S8 and S10 red at the base, S3, S5, S6 and S7 green there by design | `tests/test_a_creation_in_another_clone_asks_nobody.py` | confirmed | executed (probe 2): base guard in the clone, 4 failed and 4 passed, matching `phases/phase-1.md` |
| 🟢 | S10's `[1, 2, 1, 2]` is right and the frame's fourth count was not | `tests/test_a_creation_in_another_clone_asks_nobody.py#test_the_transcript_is_read_at_most_twice_per_creation` | confirmed | read: `spec.md` *Data & interfaces* puts the read inside each row's `if`; executed (probe 4): attended, own clone, unusable reads twice |
| 🟢 | S1's *no `worktree add`* is checked after the origin line, as In 1's *opens with `origin`* requires | `tests/test_a_creation_in_another_clone_asks_nobody.py#test_under_the_press_a_creation_row_denies_every_attempt` | confirmed | read: the origin line names the judged command; its variable part is 🟡 1 |
| 🟢 | the prompt budget's zero, scoped to the press's own clone | `docs/worktree-guard-spec.md:522` | confirmed | read: rows 1, 3 and 4 asked in another clone at `321e9de1`; row 1 still does |
| 🟢 | #896's S13 is a `Corrected ·` row, the right kind | `seal/releases/0.21.0.md:748` | confirmed | read: the released claim says *the creation direction untouched* without a clone qualifier |
| 🟢 | the three rewritten sentences say what the ladder does | `hooks/worktree-guard.py:95` | confirmed | read: the module docstring, the comment in `main` and §*Choice sites* against rows 1–5 |
| 🟢 | `guard_worktree_creation` declares `observed`, `refused`; the two new units declare `nothing` | `hooks/worktree-guard.py:1610` | confirmed | read against `docs/the-reader-registry.md` §*The four classes*; executed (probe 1): `tests/test_a_reader_declares_its_input_class.py` passes |
| 🟢 | the three other readers and `hooks/hooks.json` are unchanged | `hooks/worktree_consent.py` | confirmed | executed: `git diff --quiet 321e9de1 9e7514f3` over the three files exit 0; no hunk in `hooks/hooks.json` |
| ❓ | S11: on Windows, a creation in another clone under the press is row 4's deny with nothing stubbed | `tests/test_a_creation_in_another_clone_asks_nobody.py#test_on_windows_a_creation_in_another_clone_is_row_fours_deny` | ❓ out of verified scope | skipped off Windows; answered by the test workflow's Windows shards at the pull request |

## Paste-ready fixes

```python
    user_ok = has_token(command, "[worktree-ok]")
    origin = tr(
        "Attempting to create a worktree with `git worktree add`.",
        "`git worktree add` 로 worktree를 만들려 합니다.",
    )
    # The note below is the single-stream deny's way past, which is
    # `[worktree-ok]`. Under the press rows 3 and 4 name no token (#903), so
    # they open with the origin as it stands here.
    plain_origin = origin
    if not user_ok and not parses_cleanly(command):
        origin += tr(
            # ... the note, unchanged ...
        )
    guard_worktree_creation(
        top,
        cwd,
        origin,
        user_ok=user_ok,
        session_id=session_id,
        consented=("allow" if only_creates_a_worktree(command, cwd) else "silent"),
        transcript_path=transcript_path,
        plain_origin=plain_origin,
    )
```
```python
def guard_worktree_creation(
    top: str,
    cwd: str,
    origin: str,
    user_ok: bool,
    session_id: str = "",
    consented="silent",
    transcript_path="",
    plain_origin="",
):
    ...
    # 3) 살아 있긴 하나 한동안 입력이 없는 세션뿐 -> 잊힌 탭일 가능성. 사용자가 안다.
    if idle:
        pressed = automation_pressed(repo_paths(cwd)[0], session_id, transcript_path)
        lead = (plain_origin or origin) if pressed else origin
        choose(
            top,
            session_id,
            "create",
            (
                f"{lead}\n"
                + tr(
                    # ... row 3's sentence, unchanged ...
                )
                + f"{fmt_sessions(idle)}\n"
                + f"{fmt_snippet(top, session_id)}\n"
            ),
            # ... question, options, fallback unchanged ...
            pressed=pressed,
            unattended=elsewhere,
        )

    # 4) 동시 세션 판정 불가 -> 자동으로 만들지 말고 물어본다.
    if not reliable:
        pressed = automation_pressed(repo_paths(cwd)[0], session_id, transcript_path)
        lead = (plain_origin or origin) if pressed else origin
        choose(
            top,
            session_id,
            "create",
            (
                f"{lead}\n"
                + tr(
                    # ... row 4's sentence, unchanged ...
                )
            ),
            # ... question, options, fallback unchanged ...
            pressed=pressed,
            unattended=elsewhere,
        )
```
```python
@pytest.mark.parametrize("row", ["idle", "unusable"])
def test_an_unbalanced_quote_under_the_press_names_no_token(
    monkeypatch, capsys, projects, repo, other, wko, row
):
    """S1 for a command the lexer gives up on. The origin's quote note
    exists for the single-stream deny's way past, `[worktree-ok]`; under
    the press rows 3 and 4 name no token, so the deny is S1's, word for
    word. Seen red at `9e7514f3`: the first line named `[worktree-ok]`."""
    write_transcript(projects, "me", ask_entries(repo))
    command = creation(other, "  # don't")
    for lang, module in (("en", wg), ("ko", wko)):
        got = judge(module, monkeypatch, capsys, repo, command, ROWS[row])
        assert got == ("deny", unattended(lang, row)), (lang, got)
        assert_names_nobody(got[1])
```
```python
        if automation_pressed(repo_paths(cwd)[0], session_id, transcript_path):
            respond(
                "deny",
                tr(
                    f"{lead}, so no other row of this guard stops the switch, "
                    f"but {len(entries)} uncommitted tracked changes are "
                    f"present:\n{listing}\n{note}\n",
                    f"{lead} 이 guard 의 다른 규칙은 이 전환을 막지 않지만, "
                    f"커밋되지 않은 추적 파일 변경이 {len(entries)}건 "
                    f"있습니다:\n{listing}\n{note}\n",
                )
                + press_sentence()
                + tr(
                    "This row of the guard stops a branch switch while "
                    "uncommitted tracked changes are present, and says nothing "
                    "of a switch once none are.\n\n"
                    "The ways on, none of which needs a person. Issue each "
                    "command on its own: this guard reads the tree before a "
                    f"command runs, so `{git} stash && {git} switch <branch>` on "
                    f"one line meets this same refusal. `{git} commit` and "
                    f"`{git} stash` are on this guard's list of commands that "
                    "leave the branch where it is, so each passes it when "
                    "issued alone. Which of them fits this switch, and what to "
                    "run after it, is yours to decide.\n\n",
                    "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 "
                    "동안 브랜치 전환을 막고, 변경이 없으면 전환에 대해 아무 "
                    "말도 하지 않습니다.\n\n"
                    "사람이 없어도 되는 길은 아래와 같습니다. 명령은 하나씩 따로 "
                    "실행하세요. 이 guard 는 명령이 실행되기 전에 트리를 "
                    f"읽으므로, `{git} stash && {git} switch <branch>` 처럼 한 "
                    f"줄에 쓰면 같은 거부를 받습니다. `{git} commit` 과 "
                    f"`{git} stash` 는 이 guard 가 브랜치를 그대로 두는 명령으로 "
                    "꼽는 목록에 있어, 따로 실행하면 이 guard 를 통과합니다. 이 "
                    "전환에 어느 쪽이 맞는지, 그 뒤에 무엇을 실행할지는 직접 "
                    "정하세요.\n\n",
                )
                + reissue_sentence(),
            )
```
```
A creation is not asked again once one has run in the session, and not at all where you pressed `automation` on the routing question, in the clone that answer was given in.
```
```
한 세션에서 생성이 한 번 실행된 뒤에는 다시 묻지 않고, 라우팅 질문에서 `automation` 을 눌렀다면 그 답을 받은 클론에서는 처음부터 묻지 않는다.
```

## Executed probes

| What was run | Result |
|---|---|
| 1. `bin/test` on `tests/test_a_creation_in_another_clone_asks_nobody.py`, `tests/test_the_idle_session_rows_ask_nobody.py`, the S3 case in `tests/test_worktree_guard.py` and `tests/test_a_reader_declares_its_input_class.py`, at `9e7514f3` | exit 0, 94 passed, 2 skipped (the Windows-only cases) |
| 2. the same new cases and the S3 case with `hooks/worktree-guard.py` replaced by `321e9de1`'s, in the clone, then restored | exit 1: S1 idle, S2 unusable, S8 and S10 failed; S5, S6, S7 and S3 passed |
| 3. a `test_tmp_*` probe: press for `repo`, `git -C <other> worktree add ../wt feature/x  # don't`, rows idle and unusable, two attempts each, then the retry with `# [worktree-ok]` | every attempt `deny`, opening *No [worktree-ok] was read, … close or drop the quote and re-issue*; the retry `ask` with the token's text |
| 4. the same probe file: attended (`per axis`), creation in the session's own clone, detection unusable, counting `automation_answered` | 2 reads, `deny` |
| 5. `press_sentence`'s English reworded in the clone, then `tests/test_the_guard_asks_once_per_session.py` and `tests/test_the_idle_session_rows_ask_nobody.py`, then restored | first module exit 0, 101 passed; second exit 1, 7 failed |
| 6. `git diff --quiet 321e9de1 9e7514f3 -- hooks/worktree_consent.py hooks/commit-review-gate.py hooks/cmdline_base.py` | exit 0 |
| The broad gate: full suite, repository-wide lint, typecheck | not yet. It is the sealer's, after the rounds settle; this report leaves findings open, so it has not come due |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
