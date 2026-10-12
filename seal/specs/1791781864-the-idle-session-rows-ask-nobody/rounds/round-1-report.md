# Round 1 report — 1791781864-the-idle-session-rows-ask-nobody (#896)

| Field | Value |
|---|---|
| Target | `fix/896-the-idle-session-rows-ask-nobody` at `44c67f9f`, phases 1–3, against `origin/release/v0.21.0` at `34fc36e9` |
| Frame | `spec.md`, `plan.md`, `questions.md` (P1 (b), P2 (a) at their defaults), `handoff.md` |
| Where it ran | a `git clone --no-local` of the worktree at `44c67f9f`, under `<scratchpad>/1791781864-the-idle-session-rows-ask-nobody/round-1/clone`, removed at handover |
| Ran by | specseal:warden on claude-opus-5-5 |

No earlier round exists, so nothing is carried and every verdict below is this
round's own.

## Stage 1 — spec compliance

In 1 is delivered as framed. `hooks/worktree-guard.py#fmt_sessions` prints
`<kind> <age>` for an unidentified entry and nothing after it, in both
languages, at all six sites; the pid branch is untouched (read; S1 and S2
pass, executed).

In 2 is delivered for the state the frame measured. Under the press both
switch-direction choice rows deny on every attempt, before `already_asked`, so
no marker is written; attended, both rows are the base's byte for byte. Each
of those was executed, not read off the cases (probes 3 and 4 below). The press
sentence is byte-identical to #894's `PRESS` in both languages: the guard's
own string literals were joined and compared, and every deny reason under the
press carries `PRESS[lang]` followed by a blank line (probe 3).

One claim of In 2 does not hold, and it is the claim the deny's way on rests
on (🔴 1).

## Findings

### 🔴 1 — under the press, a switch into another clone is told its split "passes as written", and the split is then put to a person

`hooks/worktree-guard.py:3125` (the `unattended` text), with the same sentence
at `hooks/worktree-guard.py:27`, `hooks/worktree-guard.py:89`,
`docs/worktree-guard-spec.md:615`, `docs/worktree-guard-spec.md:626`,
`docs/worktree-guard-spec.md:770` and item 1 of `changelog.md`.

Rows 1-b and 2 read the press through `automation_pressed` against the
session's own root (`repo_paths(cwd)[0]`), as S11 pins. The creation ladder
reads consent through `worktree_consent.consent(top, …)` against the
creation's own clone, and `hooks/worktree_consent.py#automation_answered`'s
condition 4 accepts a press only from the same clone. The policy says so in
§*Creation consent*, and #894's
`test_an_answer_given_in_another_clone_is_not_consent` pins it. So the two
readings agree only when the switch's tree is in the session's own clone.

Executed (probe 5): the state of S11. The press is in the session's clone,
`other` is a second clone holding only idle sessions, and the command is
`git -C <other> switch feature/x`. The deny reads *That answer already
consents to creating one, so these commands pass as written* and names `git
-C <other> worktree add <wt_root>/<name> -b <branch> origin/main`. Issued as
named, that creation met:

- attempt 1 in the idle state: `deny` with *Do not choose for the user. Ask
  with the AskUserQuestion tool* (§B's only-idle row, scope `create`);
- attempt 2 in the idle state: `ask`;
- the detection-unusable state: `ask`.

**Why it matters.** This is the defect #896 exists to close: a person's
question under `automation`, here reached by following the guard's own
instruction. `spec.md` §*The class* lists §B's two choice rows as
*unreachable: consent is read first*, which holds only in the press's own
clone. In a run nobody is watching, the model follows a sentence the guard
states as fact and stalls on a prompt. `test_the_press_is_read_from_the_sessions_own_root`
asserts the false sentence word for word for this very state, so the suite is
green over it.

**Not a regression.** At the base this state asked a person on the first
switch. Nothing allows more than before. It is the item's own claim that is
wrong, in a state the item pins.

**The class (`agent-contract` §12)**, enumerated by searching the hooks for
every text that promises consent (`consents`, `pass as written`,
`동의했으므로`). The reason text in both languages, the module docstring's
two sentences, and the policy's three sentences above. #894's dirty-row deny
and the unrecognised-shape stop promise no creation, so they are outside it.

**The fix** names the split only where the creation ladder will read consent
for it: the switch's tree is in the session's own clone, or this session
already holds the record there (`worktree_consent.granted`, a `stat`). Where
neither holds, the deny says the answer covers another clone and names no
way on that needs nobody. Neither check reads the transcript, so S10's counts
stand. Whether §B's two rows should themselves become denies under a press
read from the session's root is a policy question, and it is in
`## Deferred`.

### 🟡 2 — `choose` declares `owned` for a presence test, which the registry calls `observed`

`hooks/worktree-guard.py:1474`.

`choose`'s only read is `already_asked`, and that read is an
`os.path.exists` on a zero-byte marker plus an `open(path, "w")`. No format is
parsed. `docs/the-reader-registry.md` §*The four classes* defines `owned` as
*a format this repository's own writer produces* and `observed` as *a fact
asked of the system*.

#834's build reached the same reading and wrote it down as the mapping rule
in its `plan.md`: *A test of whether a file this plugin writes exists is
`observed`, whatever the row's `Class` cell says*, naming this guard's
`already_asked`. Its inventory classes the three peer `already_asked` units
(`hooks/mode-gate.py`, `hooks/review-skill-gate.py`, the implementer notice)
`observed`.

The prompt asked which reading is right for `choose`'s body. The answer is
`observed`. The direction `refused` is right: every path of `choose` stops
the command, as its paragraph says.

If this stands, 0.21.0 ships two classes for one act, and #834's phase 4 has
to reconcile it after both land. `tests/test_a_reader_declares_its_input_class.py`
passes either way, because it reads the grammar and not the truth (executed).

### 🟡 3 — the policy and the changelog say *every* `git switch` on Windows under the press is row 2's deny; `[shared-tree-ok]` still passes it

`docs/worktree-guard-spec.md:974`, `docs/worktree-guard-spec.md:770`,
`seal/specs/1791781864-the-idle-session-rows-ask-nobody/changelog.md:18`.

Row 2 is `if not reliable and not shared_ok`. Under P2 (a) the token still
stands the row aside under the press. S6 pins this in the detection-unusable
state, and the same document's §*Choice sites* paragraph says so. On Windows,
then, a `git switch … # [shared-tree-ok]` is silent in a clean tree and meets
#894's tracked-changes deny in a dirty one. It is not this deny. Under P2 (a)
that exception is the thing a reader of the Windows bullet most needs to see,
and the bullet and the changelog both deny that it exists.

### ⬜ 4 — the new sentence names `<name>` only, and prints `{wt_root}` unquoted

`hooks/worktree-guard.py:3137`. *Then work in that tree by path …
`git -C {wt_root}/<name> …`* follows two forms. The existing-branch form
creates `{wt_root}/<branch>`, so the placeholder fits only the second. The
path is also unquoted. `overview.md` §*Not done* leaves the unquoted path
because `split` is shared with the attended steer, and S5 holds that byte for
byte. This sentence is not shared, though. The behaviour and the facts are
right, so this is ⬜. It changes no verdict.

### ⬜ 5 and ⬜ 6 — paperwork corrections (not counted in `Needs a fix`)

- ⬜ 5, `seal/specs/1791781864-the-idle-session-rows-ask-nobody/handoff.md`: the
  table still reads *PR: none yet* and *phases 1–2 built*. Draft PR #902 is
  open and phase 3 closed at `e905b5a5`.
- ⬜ 6, `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md`, the
  restated S2. Its Proof cell still says *the one new branch is the press
  read inside the tracked-changes row*, while its restated claim and note
  count the two `pressed=` branches too.

## The four things phase 3's smith flagged

- **`## Removes` added to the framer's `spec.md`: right.** `seal/config.md`
  sets `Removes from` to `1791780031`, below this id, so
  `docs/the-reader-registry.md` §*A frame names what its work removes* binds
  this frame. The records arm refused it without the section. `agents/smith.md`
  says a removal the frame did not name is a divergence in `overview.md`, and
  `overview.md`'s divergence table carries it. The three rows name what In 1
  and §*Seams* already named. `evidence-check` reads every live frame with 0
  refused (executed).
- **#894's live rows S2 and S9 restated in place: right.**
  `docs/the-evidence-ledger.md` §*A citation that does not hold is named*
  refuses a citation into a fragment and says to re-stamp that fragment's row
  in place instead. A claim that stopped being true is the same case, one step
  further. Each restated claim matches the code and the policy as they now
  stand (read), and both fragments check clean (executed). The leftover Proof
  sentence is ⬜ 6.
- **The paragraph in §*Unknowns resolve conservatively*: right, with 🔴 1's
  caveat.** The argument is already the frame's, in `spec.md` §*Grounding*'s
  row on that section and In 2's Windows paragraph. The policy would otherwise
  contradict itself, because its own outage sentence now describes these rows
  on Windows. Its *the press consents to it* inherits 🔴 1.
- **`choose` declared `owned`: wrong.** It should be `observed` (🟡 2).

## Regression tests to plant

- `tests/test_the_idle_session_rows_ask_nobody.py`: a switch into another
  clone under this session's press denies naming no split and no question
  tool. Seen red at `44c67f9f`, where the reason says *pass as written*
  (fenced under 🔴 1). The first half of
  `test_the_press_is_read_from_the_sessions_own_root` changes its expected
  text with the fix.
- The same file: under the press in the session's own clone, after the
  session already holds a creation record in a second clone, a switch into
  that second clone names the split. This pins the `granted` branch of the
  fix, so a revert to the clone test alone shows red.

## Facts for the evidence ledger

- The press is read at two roots for two purposes. `automation_pressed`
  reads it against the session's own root and asks whether anybody is at the
  keyboard. `worktree_consent.consent` reads it against the creation's clone
  and asks whether this clone may be split. They agree only inside the
  press's clone. Coordinates: `hooks/worktree-guard.py#automation_pressed`,
  `hooks/worktree_consent.py#automation_answered`. Executed in probe 5.
- With the press absent, rows 1-b and 2 are `34fc36e9`'s, byte for byte.
  That covers both rows, both languages, attempts 1 and 2, a creation on the
  line, and the ACTIVE row's steer. Executed against a copy of the base
  guard in probe 4.

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| §B's only-idle and detection-unusable rows (`choose`, scope `create`) still put the question to a person when a session under the press creates a worktree in a clone the press was not given in. 🔴 1's fix stops the guard steering a model there, but does not close the row. Turning those rows into a deny under a press read from the session's own root is a policy change to §*Creation consent* | #903 | the repository owner, who decides whether the press from the session's own root reaches the creation direction's choice rows |

## Paste-ready fixes

### 🔴 1

`hooks/worktree-guard.py#main`: replace the `unattended = (…)` block with the
pieces and the function below. The text in the press's own clone is
unchanged byte for byte.

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

The two call sites, row 1-b and row 2 alike. The press is read in the row's
own `if`, as today, so S10's counts stand, and the clone check runs only
under the press:

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

The case, in `tests/test_the_idle_session_rows_ask_nobody.py`. It is red at
`44c67f9f`, where the reason carries *pass as written*:

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

`docs/worktree-guard-spec.md` §*Choice sites*, *Under the press*. Replace the
two sentences, keeping the line wrap at the document's width:

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

The module docstring at lines 25–27 and 86–90 and the changelog's item 1 take
the same qualifier, *in the clone that answer was given in*.

### 🟡 2

`hooks/worktree-guard.py#choose`:

```python
    Reads: observed — whether this session was already asked in this direction, the presence of the marker this guard writes, through `already_asked`; unknown refused
```

### 🟡 3

`docs/worktree-guard-spec.md` §*Known limits*, the Windows bullet:

```
  `ask` otherwise. Under the press every `git switch` there that does not
  carry `[shared-tree-ok]` is row 2's deny, in a shared tree and in a linked
  worktree alike, so an `automation` run on Windows works in a worktree per
  branch, created with `-b`, and switches only where the token is written.
```

§*Unknowns resolve conservatively*:

```
Under the press those two rows are a deny on every attempt (§Choice sites,
*Under the press*), and on Windows that is every switch without
`[shared-tree-ok]`. What keeps it a cost rather than the outage above is its
way on: a worktree per branch, created with `-b`, needs no switch and no
person, and the press consents to it in the clone it was given in.
```

`seal/specs/1791781864-the-idle-session-rows-ask-nobody/changelog.md`, item 3:

```
  3. On Windows, where sessions can never be counted, every `git switch`
     under the press that does not carry `[shared-tree-ok]` is this refusal,
     so an `automation` run there works in a worktree per branch.
```

Needs a fix: yes — 🔴 1 (the deny promises a split that another clone's creation ladder puts to a person), 🟡 2 (`choose` declares `owned` for a presence test), 🟡 3 (*every* Windows switch, past the token)
Loses a record or crashes: no

The broad gate has not come due. 🔴 1 and two 🟡 are open, so a fix pass and a
verifying round come before the sealer's spawn.

## Proof block

Files opened in this round, at `44c67f9f` unless named otherwise:

- `seal/specs/1791781864-the-idle-session-rows-ask-nobody/`: `spec.md`, `plan.md`, `questions.md`, `handoff.md`, `routing.md`, `phases/phase-3.md`, `overview.md`, `changelog.md`, `survivors.md`
- `hooks/worktree-guard.py`: the module docstring, `fmt_sessions`, `respond`, `already_asked`, `choose`, `guard_worktree_creation`, `judge_creation`, `automation_pressed`, `main` whole, and the reliability returns of `sessions_in_tree`
- `hooks/worktree_consent.py`: `_clone_of`, `automation_answered`, `consent`, `record`
- `tests/test_the_idle_session_rows_ask_nobody.py` whole; `tests/test_the_guard_asks_once_per_session.py` (`PRESS`, `dirty_deny`); `tests/conftest.py` (`load_hook_module`)
- `docs/worktree-guard-spec.md` (the diff, and lines 610–628, 766–772 and 968–982); `docs/the-reader-registry.md` §§*The four classes*, *Who declares*, *A frame names what its work removes*; `docs/the-evidence-ledger.md` lines 100–175
- `seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md`, `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` (the diff), and the diff of `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md`; `seal/releases/0.20.0.md` row W10
- `README.md` and `README.ko.md` (the diff); `tests/undeclared_readers.txt` (the diff); `agents/smith.md` lines 178–190
- #834's worktree: `plan.md` lines 60–85 and `inventory/1-hooks-shell.md` rows 79, 114, 128
