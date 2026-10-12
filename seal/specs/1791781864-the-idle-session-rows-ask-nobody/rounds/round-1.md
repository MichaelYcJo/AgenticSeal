# 1791781864-the-idle-session-rows-ask-nobody — review round 1

| Field | Value |
|---|---|
| Target SHA | 44c67f9f5bf385bc1eb6fae218a1f2d7c8856860 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #902 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | no |
| Needs a fix | yes — 🔴 1 (the deny promises a split that another clone's creation ladder puts to a person), 🟡 2 (`choose` declares `owned` for a presence test), 🟡 3 (*every* Windows switch, past the token) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 1 of #896, target 44c67f9f against `origin/release/v0.21.0` at 34fc36e9 (#894 landed), over the whole build, phases 1–3. The reviewer was asked to judge four things phase 3's smith did outside its instructions (the `## Removes` section, #894's ledger rows S2 and S9 restated in place, the §*Unknowns resolve conservatively* paragraph, `choose` declared `owned` against #834's rule that a marker presence check is `observed`), and to check that the press sentence is #894's byte for byte and that the deny is issued on every attempt.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | under the press, a switch into another clone is told its split passes as written, and the named creation meets §B's choice row, which asks a person (`deny` naming AskUserQuestion, then `ask`) | `hooks/worktree-guard.py:3125` | open | executed (probe 5); the creation reads consent from its own clone, `hooks/worktree_consent.py#automation_answered` condition 4; S11 pins the false sentence |
| 🟡 2 | `choose` declares `owned` for a marker presence test | `hooks/worktree-guard.py:1474` | open | `docs/the-reader-registry.md` §*The four classes*; #834's `plan.md` mapping rule names this guard's `already_asked` as `observed` |
| 🟡 3 | *every* `git switch` on Windows under the press is row 2's deny, though `[shared-tree-ok]` stands row 2 aside | `docs/worktree-guard-spec.md:974` | open | read: row 2 is `not reliable and not shared_ok`; S6 pins the token under the press |
| ⬜ 4 | the new sentence's `git -C {wt_root}/<name>` fits only the new-branch form and is unquoted | `hooks/worktree-guard.py:3137` | open | read; `overview.md` §*Not done* covers the shared `split` only |
| ⬜ 5 | `handoff.md` says no PR and phases 1–2 only | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/handoff.md` | open | correction to the run's paperwork |
| ⬜ 6 | #894's restated S2 keeps *the one new branch* in its Proof cell | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` | open | correction to the run's paperwork |
| 🟢 | the press sentence in the new deny is #894's `PRESS`, byte for byte, English and Korean | `hooks/worktree-guard.py:3122` | confirmed | executed (probe 3): the source literals joined and compared, and `PRESS[lang]` followed by a blank line in every reason under the press |
| 🟢 | under the press both rows deny on every attempt and write no marker | `hooks/worktree-guard.py#choose` | confirmed | executed (probe 3): four attempts, two rows, two languages, all `deny`; S3 and S4 pass |
| 🟢 | without the press both rows, and the ACTIVE steer, are the base's byte for byte | `hooks/worktree-guard.py#main` | confirmed | executed (probe 4) against a copy of `34fc36e9`'s guard |
| 🟢 | the `## Removes` section the smith added to `spec.md` is owed and correct | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/spec.md` | confirmed | `seal/config.md` `Removes from`; the divergence is in `overview.md`; records arm 0 refused (executed) |
| 🟢 | #894's live rows S2 and S9 restated in place | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` | confirmed | `docs/the-evidence-ledger.md` refuses a citation into a fragment; the claims match the code (read); the fragment checks clean (executed) |
| 🟢 | the §*Unknowns resolve conservatively* paragraph | `docs/worktree-guard-spec.md:769` | confirmed | the frame's own argument (`spec.md` §*Grounding*, In 2); its consent clause inherits 🔴 1 |
| ❓ | on Windows, with nothing stubbed, a switch under the press is row 2's deny (M2) | `tests/test_the_idle_session_rows_ask_nobody.py` | ❓ out of verified scope | skipped off Windows, and this round ran on darwin; the test workflow's Windows legs answer it at the pull request |

## Paste-ready fixes

```python
    # What rows 1-b and 2 say after their situation where this session's
    # person pressed `automation` (#896). [keep the existing comment, and add:]
    # The press is consent only in the clone it was given in
    # (`worktree_consent.automation_answered`, condition 4), or where this
    # session already created a worktree (`worktree_consent.granted`), while
    # these rows read it from the session's own root. So the split is named
    # as the way on only where the creation ladder will read consent for it;
    # a switch into another clone is refused without one. Neither check
    # reads the transcript.
    press = tr(
        "This session's person pressed `automation` on the routing "
        "question, so this guard puts no question to them, and none is to "
        "be put to them in its place.\n\n",
        "이 세션의 사용자가 라우팅 질문에서 `automation` 을 눌렀습니다. 그래서 "
        "이 guard 는 사용자에게 아무것도 묻지 않으며, 다른 방법으로 대신 "
        "물어서도 안 됩니다.\n\n",
    )
    reissue = tr(
        "Re-issuing this command unchanged meets this same refusal.",
        "이 명령을 그대로 다시 실행하면 같은 거부를 받습니다.",
    )

    def unattended_text():
        own = worktree_consent._clone_of(repo_paths(cwd)[0])
        if (own and own == worktree_consent._clone_of(top)) or (
            worktree_consent.granted(top, session_id)
        ):
            return (
                press
                + tr(
                    "The way on that needs nobody is to split into a worktree. "
                    "That answer already consents to creating one, so these "
                    "commands pass as written:\n\n",
                    "사람이 없어도 되는 길은 worktree 로 분리하는 것입니다. 그 답이 "
                    "worktree 생성에 이미 동의했으므로, 아래 명령은 쓰인 그대로 "
                    "통과합니다.\n\n",
                )
                + split
                + tr(
                    "Then work in that tree by path from this session: "
                    f"`git -C {wt_root}/<name> …` for git, and an absolute path "
                    "for every edit. A branch already checked out in a worktree "
                    "needs no switch: work in that worktree.\n\n",
                    "그런 다음 이 세션에서 그 트리를 경로로 지정해 작업하세요. git 은 "
                    f"`git -C {wt_root}/<name> …` 로, 파일 편집은 절대 경로로 "
                    "합니다. 이미 어느 worktree 에 체크아웃된 브랜치라면 전환할 필요 "
                    "없이 그 worktree 에서 작업하세요.\n\n",
                )
                + reissue
            )
        return (
            press
            + tr(
                "That answer was given in another clone, and it consents to "
                "creating a worktree in that clone only. A split of this tree "
                "would be put to a person, so no way on here needs nobody: "
                "leave this switch to a session working in this clone.\n\n",
                "그 답은 다른 클론에서 받은 것이라, 그 클론에서 worktree 를 만드는 "
                "것에만 동의합니다. 이 트리를 분리하면 사람에게 묻게 되므로, 여기에는 "
                "사람이 없어도 되는 길이 없습니다. 이 전환은 이 클론에서 작업하는 "
                "세션에 맡기세요.\n\n",
            )
            + reissue
        )
```
```python
    if idle and not shared_ok:
        pressed = automation_pressed(repo_paths(cwd)[0], session_id, transcript_path)
        choose(
            top,
            session_id,
            "switch",
            # … situation, question, options, fallback as today …
            before_ask=judge_the_creation,
            pressed=pressed,
            unattended=unattended_text() if pressed else "",
        )
```
```python
def test_a_switch_into_another_clone_names_no_split_it_cannot_consent(
    monkeypatch, capsys, projects, repo, tmp_path
):
    """Round 1, red 1. The press consents to a creation only in the clone it
    was given in, so a switch into another clone under this session's press
    is refused without naming a split that clone's creation ladder would put
    to a person."""
    other = tmp_path / "other-repo"
    shutil.copytree(repo, other)
    write_transcript(projects, "me", ask_entries(repo))
    top = wg.repo_paths(str(other))[0]
    command = f"git -C {shlex.quote(top)} switch feature/x"
    decision, reason = judge(wg, monkeypatch, capsys, repo, command, ROWS["idle"])
    assert decision == "deny", reason
    assert "another clone" in reason, reason
    assert "worktree add" not in reason and "pass as written" not in reason, reason
    assert_names_nobody(reason)
    assert no_marker(wg, other)
```
```
working in that tree by path with `git -C`. The press is consent in the clone
it was given in, read there before every creation row (§Creation consent), so
in that clone those commands pass as written with no `[worktree-ok]`. A switch
into another clone is refused under the press as well, and its reason names no
split, because a creation there is not consented and §B's rows would put it to
a person.
…
command line. In the clone the press was given in, the creation direction's two
sites never run under the press, because consent is read before them.
```
```python
    Reads: observed — whether this session was already asked in this direction, the presence of the marker this guard writes, through `already_asked`; unknown refused
```
```
  `ask` otherwise. Under the press every `git switch` there that does not
  carry `[shared-tree-ok]` is row 2's deny, in a shared tree and in a linked
  worktree alike, so an `automation` run on Windows works in a worktree per
  branch, created with `-b`, and switches only where the token is written.
```
```
Under the press those two rows are a deny on every attempt (§Choice sites,
*Under the press*), and on Windows that is every switch without
`[shared-tree-ok]`. What keeps it a cost rather than the outage above is its
way on: a worktree per branch, created with `-b`, needs no switch and no
person, and the press consents to it in the clone it was given in.
```
```
  3. On Windows, where sessions can never be counted, every `git switch`
     under the press that does not carry `[shared-tree-ok]` is this refusal,
     so an `automation` run there works in a worktree per branch.
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test -q -p no:cacheprovider` over the new file, `tests/test_worktree_guard.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_a_reader_declares_its_input_class.py`, `tests/test_a_folded_statement_names_what_enforces_it.py`, `tests/test_docs_line_wrap.py`, `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py`, `tests/test_the_printed_ledger_name_is_the_file_that_was_read.py`, `tests/test_no_real_identifiers.py`, in the clone at `44c67f9f` | 478 passed, 1 skipped (the Windows-only M2 case), exit 0 |
| `bin/evidence-check --ledger` on this item's fragment, then on #894's fragment, then with no argument | 25 ok; 39 ok; exit 0; records arm 13 work items read, 0 refused, 0 drifted |
| probe 3, a temporary test file: the guard source's string literals starting with the press sentence, joined, against `PRESS`; and four `git switch feature/x` attempts per row, per language, under the press | each literal starts with `PRESS[lang]`; 16 of 16 `deny`, each holding `PRESS[lang]` and a blank line |
| probe 4, a temporary test file with `34fc36e9`'s guard loaded beside the head's: attempts 1 and 2 and `git switch feature/x && git worktree add ../wt f`, in both rows and both languages, with no press; then the ACTIVE row | identical decisions and reasons; `deny`, `ask` |
| probe 5, a temporary test file in S11's state: the deny for `git -C <other> switch feature/x`, then the creation it names, `git -C <other> worktree add <wt_root>/y -b feature/y` | the switch: `deny`, saying *pass as written*. The creation: `deny` naming AskUserQuestion, then `ask`; in the detection-unusable state, `ask` |
| `round-record new` run on this report inside the clone, to check that it parses; the record it wrote went with the clone | wrote `round-1.md` with both lines copied and ⬜ 4–6 carried as open notes; exit 1, from `chain-check` alone, because the clone has none of the remote branches the other work items' targets sit on |
| the probe files and the base guard copy were deleted from the clone, and the clone and its round directory were removed | `git status --short` empty before removal |
| broad gate (full suite, lint, typecheck) | not yet: no run made by anyone; it belongs to the sealer once the rounds settle, and with 🔴 1 open it is not yet due |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| §B's only-idle and detection-unusable rows (`choose`, scope `create`) still put the question to a person when a session under the press creates a worktree in a clone the press was not given in. 🔴 1's fix stops the guard steering a model there, but does not close the row. Turning those rows into a deny under a press read from the session's own root is a policy change to §*Creation consent* | #903 | the repository owner, who decides whether the press from the session's own root reaches the creation direction's choice rows |
