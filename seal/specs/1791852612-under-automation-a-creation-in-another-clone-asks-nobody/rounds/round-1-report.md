# Round 1 report — 1791852612-under-automation-a-creation-in-another-clone-asks-nobody (#903)

| Field | Value |
|---|---|
| Round | 1 |
| Target | draft PR #916, branch `fix/903-under-automation-a-creation-in-another-clone-asks-nobody`, phases 1–2 |
| Target SHA | `9e7514f3` |
| Base | `origin/release/v0.21.1` at `321e9de1` |
| Reviewed by | warden |
| Where it ran | a `git clone --no-local` of the worktree at `9e7514f3`, under the session scratchpad, removed before handover |
| Earlier rounds | none: this is the first round, so the only voices besides the code were the frame and the smith's account (`overview.md`, `phases/phase-1.md`, `phases/phase-2.md`) |

Every case run in this round ran with `SPECSEAL_CASE_CEILING_S=600`, because
the machine was loaded by parallel builds (`CONTRIBUTING.md` §*Running the
checks*).

## How the findings relate

```
In 1: under the press, rows 3 and 4 deny naming no way on and no token
  ├─ 🟡 1  one input shape breaks it: an unbalanced quote puts `[worktree-ok]`
  │        into the deny's first line, and following it reaches a person's `ask`
  ├─ 🟡 2  the shared sentences have a third copy; the ground given for leaving
  │        it ("a reword fails there") is false when executed
  └─ 🟡 3  the README still says a creation is "not at all" asked under the
           press, the claim the smith narrowed in the policy for the same reason
⬜ 4  paperwork: #896's S13 correction drops two of the sections its claim names
```

## Stage 1 — spec compliance

In 1 is built as framed. Rows 3 and 4 of `hooks/worktree-guard.py#guard_worktree_creation`
read the press through `automation_pressed(repo_paths(cwd)[0], …)`, inside
each row's `if`, and hand `choose` its `pressed` verdict with the new
other-clone text (`hooks/worktree-guard.py:1892`, `:1922`). The text is the
row's situation, `press_sentence`, the other-clone sentence and
`reissue_sentence`, in both languages. `choose` returns before
`already_asked`, so no marker is written. Row 0, row 1, row 2 and row 5 did
not move, and the Agent/Task path is untouched. `hooks/worktree_consent.py`,
`hooks/commit-review-gate.py` and `hooks/cmdline_base.py` are byte-identical
to `321e9de1` (executed, `git diff --quiet` exit 0), and `hooks/hooks.json`
has no hunk.

I checked whether the deny's claim *this tree is in another clone* can be
reached in the session's own clone. It cannot, read from the code: `consent`
and `automation_pressed` both end in `automation_answered`, against the same
transcript, and condition 4 compares `_clone_of(top)` with the result
entry's clone. For one clone the two reads give one answer, so `consent`
returning `""` while the rows read the press True means the clones differ.

The one place the build departs from In 1's text contract is 🟡 1.

### The smith's divergences, each judged

- **S10 pinned as `[1, 2, 1, 2]`.** Confirmed. The frame's fourth count, 1,
  contradicts its own *Data & interfaces*, which puts the read inside each
  row's `if`. Attended, row 3 still fires, and only that read can say the
  press is absent. The doc sentence *a creation there reads the transcript
  twice* reads *there* as *where one of the two rows fires*, which matches
  every state. Executed: an attended creation in the session's own clone
  with detection unusable read the transcript twice, as that sentence says.
- **S1's *no `worktree add`* checked after the origin line only.**
  Confirmed. In 1 requires the reason to open with `origin`, which names
  `git worktree add` as the command judged, so the frame's S1 sentence could
  not hold as written. The intent behind it, that no command to run is
  named, is what the case checks. But the origin line is not always one
  fixed sentence, and that is 🟡 1.
- **The prompt-budget sentence narrowed to the press's own clone.**
  Confirmed. *Zero for a session whose person pressed `automation`* was
  false in another clone at `321e9de1` (rows 1, 3 and 4 asked there) and is
  still false there through row 1. Leaving it would have the section state
  two budgets. The same claim stands unnarrowed in both READMEs, which is
  🟡 3.
- **#896's S13 closed as `Corrected ·`, not `Re-read ·`.** Confirmed as the
  right kind of row. The released row (`seal/releases/0.21.0.md`, line 748)
  says §*Choice sites* states *the creation direction untouched*, with no
  clone qualifier, and #903 makes that false in another clone. Its
  coordinates are ⬜ 4.
- **Three sentences rewritten as half-false.** Confirmed: the module
  docstring's *Under the press* paragraph, `main`'s comment above the
  shared sentences, and §*Choice sites*' *Elsewhere it names no split*. Each
  now says a creation in another clone is not consented: the rows refuse it,
  or ask where another session is active. Under the press that matches the
  ladder: row 1 still asks, and rows 3 and 4 deny. The switch deny's own
  sentence, *a split of it may be put to a person*, stays true through
  row 1 and row 2 on P1's default.
- **The third copy of the two sentences, in #894's tracked-changes deny.**
  Not confirmed. The smith left it on the ground that a reword of
  `press_sentence` that misses the copy *fails there rather than drifting
  silently*. Executed, it does not fail there. That is 🟡 2.

### W2 — the `Reads:` line on `guard_worktree_creation`

Confirmed: `observed`, `refused`. The unit's own inputs are the consent (a
record's presence and a harness-written transcript), the process scan and
the press. The token reaches it as a bool its caller read, so under
`docs/the-reader-registry.md` §*The four classes* it does not lower the
class. Every unreadable input of its own lands on a row that stops the
command. `press_sentence` and `reissue_sentence` declare `nothing`, as
formatters of the guard's own text.

## Stage 2 — findings

### 🟡 1 — under the press, an unbalanced quote puts `[worktree-ok]` into the deny, and following it reaches a person

*From execution (probe 3).* `hooks/worktree-guard.py#judge_creation`
appends a note to `origin` when the command carries no token and does not
parse cleanly (`hooks/worktree-guard.py:2008`). The note reads *No
[worktree-ok] was read, … If you already appended one, close or drop the
quote and re-issue.* It is there for the single-stream deny, whose way past
is that token. Rows 3 and 4 open their situation with the same `origin`, so
under the press the deny that In 1 says names no `[worktree-ok]` names it
in its first line, in both rows and on every attempt.

The probe ran `git -C <other> worktree add ../wt feature/x  # don't` from
`repo`, with the press for `repo` and the other clone idle and then
unusable. Each attempt was `deny`, with the quote note before the press
sentence. A retry that closes the quote and appends the token reaches
row 2's `ask`, which is a prompt to a person in a session whose person said
nobody would answer.

Why it matters:

- **The contract is broken.** `spec.md` In 1 and
  `docs/worktree-guard-spec.md` §*A creation in another clone under the
  press* both say the reason names no `[worktree-ok]`. For this input it
  does.
- **It steers toward a person.** S6 accepts row 2's `ask` under the press
  only because the deny does not name the token, so a model that appends it
  read it elsewhere. Here it read it in the deny.
- **Nothing pins it.** `assert_names_nobody` would catch the token, but
  every S1 command parses cleanly, so no case reaches the note.

The fix gives rows 3 and 4 the origin without the note when the press is
read, and leaves every attended text byte-identical (S3).

### 🟡 2 — the press and re-issue sentences have a third copy, and a reword of the shared one leaves it behind with every case green

*From execution (probe 5).* W1 moved `main`'s two locals into
`press_sentence` and `reissue_sentence`. Its docstring calls the first *the
sentence every deny under the press carries*. #894's tracked-changes deny
under the press (`hooks/worktree-guard.py:3548`–`3570`) still carries both
sentences inline, inside one `tr(...)` pair. `phases/phase-1.md` names the
copy and leaves it, because *its text is pinned by
`tests/test_the_guard_asks_once_per_session.py`'s `dirty_deny` cases, so a
reword of `press_sentence` that misses it fails there rather than drifting
silently*.

That ground does not hold. The probe reworded `press_sentence`'s English in
the clone. `tests/test_the_guard_asks_once_per_session.py` passed whole,
101 cases with exit 0, because `dirty_deny` pins its own literal of the old
sentence, which the inline copy still prints. Only
`tests/test_the_idle_session_rows_ask_nobody.py` failed (7 cases), and
updating its literal to the new wording is the routine next step. After it,
the switch ladder says two different press sentences and every case is
green. That is the drift the smith's ground says cannot happen.

- **Why 🟡 and not ⬜:** today's bytes are identical, so nothing ships
  wrong at this release. But the copy was kept on a stated ground that is
  false, the ledger's S9 row says the sentences *both ladders say are one
  string each*, and the fix is byte-identical output.
  `agent-contract` §12 owes the fix to every instance of the class.
- **What the fix does:** #894's deny composes from `press_sentence()` and
  `reissue_sentence()` around two `tr` pairs holding its own text. The
  `dirty_deny` cases stay green unchanged. The same mutation then turns them
  red, which is the proof the copy is gone.

### 🟡 3 — both READMEs still say a creation is "not at all" asked under the press

*From reading.* `README.md:201` says *A creation is not asked again once
one has run in the session, and not at all where you pressed `automation`
on the routing question.* `README.ko.md:198` says *라우팅 질문에서
`automation` 을 눌렀다면 처음부터 묻지 않는다.* In another clone under the
press, row 1 (an ACTIVE session there) still asks a person, by P1's
default. The smith narrowed the policy's equal claim, *Zero for a session
whose person pressed `automation`*, for that reason (overview divergence 3)
and edited this README cell in the same diff. The README sentence was left
as it was, so it is the one copy of the claim the class enumeration missed.
The new sentence two clauses later qualifies rows 3 and 4 but not row 1.

### ⬜ 4 — paperwork: #896's S13 correction drops two of the sections its claim names

*From reading.* `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md:30`
supersedes the released S13 row. Its claim still says §*What a blocking
prompt must show* says an unidentified session prints its signal and age
alone, and that §*Unknowns resolve conservatively* says why that is a cost.
Its coordinates name only §*Decision matrix*, §*Choice sites* and §*Known
limits*. The released row also cited
`docs/worktree-guard-spec.md#"### What a blocking prompt must show (identification)"`
and `#"### Unknowns resolve conservatively"`. Both headings still exist at
`9e7514f3` (lines 771 and 787). Once the correction retires the released
row, those two claims have no anchor for `evidence-check` to watch. The
correction is to add the two coordinates at their current hashes, or drop
the two clauses from the claim. This is a correction to the run's
paperwork, so it is not counted in `Needs a fix`.

## Regression tests to plant

- `tests/test_a_creation_in_another_clone_asks_nobody.py`: an S1 variant whose command carries an unbalanced quote (`creation(other, "  # don't")`), both rows, both languages, asserting the whole S1 text and `assert_names_nobody`. Seen red at `9e7514f3` by probe 3, where the reason named `[worktree-ok]`. Its fenced form is under 🟡 1 below. Add it to the `Enforced by:` line of §*A creation in another clone under the press*.
- No new case for 🟡 2. The mutation in probe 5 is the proof: after the fix, rewording `press_sentence` must turn the `dirty_deny` cases red.

## Facts for the evidence ledger

- The creation deny under the press names no `[worktree-ok]` for a command with an unbalanced quote: a row on the 🟡 1 case once it is planted.
- `press_sentence` and `reissue_sentence` are the only sources of the two sentences in `hooks/worktree-guard.py`: S9's row is restated to cite #894's deny as a caller once 🟡 2 is fixed.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | under the press, a creation with an unbalanced quote gets rows 3 and 4's deny with the origin's quote note, which names `[worktree-ok]` and invites a re-issue; the token retry reaches row 2's `ask`, a person's prompt | `hooks/worktree-guard.py:2008` | open | executed (probe 3): both rows, two attempts each, `deny` naming `[worktree-ok]`; the retry with the token was `ask`. Contradicts `spec.md` In 1 and `docs/worktree-guard-spec.md` §*A creation in another clone under the press* |
| 🟡 2 | #894's tracked-changes deny under the press keeps inline copies of both shared sentences; a reword of `press_sentence` leaves it behind with every case green, so the ground `phases/phase-1.md` gives for leaving it is false | `hooks/worktree-guard.py:3555` | open | executed (probe 5): `press_sentence` English reworded, `tests/test_the_guard_asks_once_per_session.py` 101 passed exit 0, `tests/test_the_idle_session_rows_ask_nobody.py` 7 failed; ledger S9 says one string each |
| 🟡 3 | both READMEs say a creation is not asked at all under the press; row 1 still asks in another clone, the reason the policy's budget sentence was narrowed | `README.md:201` | open | read: `hooks/worktree-guard.py#guard_worktree_creation` row 1 is above the press; overview divergence 3; `README.ko.md:198` is the same claim |
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

The probe file was deleted after it ran, and the clone, its virtual
environment and the probe outputs were removed before handover.

## Paste-ready fixes

### 🟡 1

In `hooks/worktree-guard.py#judge_creation`, keep the origin without the
quote note beside the one with it, and hand both down:

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

In `hooks/worktree-guard.py#guard_worktree_creation`, add the parameter and
read the press before the situation is built, in each row's `if`, so the
count S10 pins does not move:

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

The case, in `tests/test_a_creation_in_another_clone_asks_nobody.py`:

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

### 🟡 2

In `hooks/worktree-guard.py#main`, the tracked-changes deny under the press
composes from the two shared sentences. The output is byte-identical, so
the `dirty_deny` cases stay green as they are:

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

Seen working: reword `press_sentence`'s English through `mutation-check`,
and the `dirty_deny` cases in `tests/test_the_guard_asks_once_per_session.py`
must now fail. Then correct `phases/phase-1.md`'s *fails there rather than
drifting silently* and restate the ledger's S9 row to name this deny.

### 🟡 3

`README.md`, the `worktree-guard` row:

```
A creation is not asked again once one has run in the session, and not at all where you pressed `automation` on the routing question, in the clone that answer was given in.
```

`README.ko.md`, the `worktree-guard` row:

```
한 세션에서 생성이 한 번 실행된 뒤에는 다시 묻지 않고, 라우팅 질문에서 `automation` 을 눌렀다면 그 답을 받은 클론에서는 처음부터 묻지 않는다.
```

Needs a fix: yes — 🟡 1 (an unbalanced quote puts `[worktree-ok]` into the
deny under the press), 🟡 2 (the third copy of the shared sentences drifts
silently), 🟡 3 (both READMEs say a creation is never asked under the press)
Loses a record or crashes: no

## Proof block

Files opened in this round: `seal/specs/1791852612-under-automation-a-creation-in-another-clone-asks-nobody/spec.md`,
`overview.md`, `questions.md`, `phases/phase-1.md`, `phases/phase-2.md`,
`changelog.md`; `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md`;
`hooks/worktree-guard.py` (`choose`, `guard_worktree_creation`,
`judge_creation`, `automation_pressed`, `parses_cleanly`'s caller, `main`'s
press sentences, `unattended_text` and the tracked-changes deny);
`hooks/worktree_consent.py` (`consent_path` to `record`);
`tests/test_a_creation_in_another_clone_asks_nobody.py`; the diff of
`tests/test_worktree_guard.py`; `tests/test_the_idle_session_rows_ask_nobody.py`
(`judge`, `assert_names_nobody`); `tests/test_the_guard_asks_once_per_session.py`
(the `dirty_deny` lines); `docs/the-reader-registry.md` §*The four classes*;
the diff of `docs/worktree-guard-spec.md`, `README.md`, `README.ko.md` and
`tests/undeclared_readers.txt`; `seal/releases/0.21.0.md:748`;
`seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-1-report.md`
(for the report's shape); `bin/test`.
