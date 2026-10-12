# Round 2 report — 1791781864-the-idle-session-rows-ask-nobody (#896)

| Field | Value |
|---|---|
| Target | `fix/896-the-idle-session-rows-ask-nobody` at `57f46c5f`; fix range `c7860bfe..5652b6be`, then the rest of the build; base `origin/release/v0.21.0` at `34fc36e9` |
| Kind | verifying round over round 1's fixes, widened by the prompt to the rest of the build |
| Where it ran | a `git clone --no-local` of the worktree at `57f46c5f`, under `<scratchpad>/1791781864-the-idle-session-rows-ask-nobody/round-2/clone`, removed at handover |
| Ran by | specseal:warden on claude-opus-5-5 |

Carried from round 1 as coordinates, not verdicts: the two-root reading of
the press (`hooks/worktree-guard.py#automation_pressed` against the session's
root, `hooks/worktree_consent.py#automation_answered` condition 4 against the
creation's clone), and that #894's dirty-row deny and the unrecognised-shape
stop name no creation. I re-opened the second by search: neither text names a
`worktree add` or a split under the press, so rows 1-b and 2 are still the
whole class of texts that promise a creation.

## Round 1's findings, each answered

- **Round 1's blocking finding is closed.** The fix pass claimed the deny
  names the split only where the switch's tree is in the session's own clone
  or holds this session's creation record. The code at
  `hooks/worktree-guard.py:3149` does that. `own` is the clone of
  `repo_paths(cwd)[0]`, which is the root `automation_pressed` reads, so a
  true press means the press was given in `own` (condition 4). The equality
  test is therefore exactly "the press consents to a creation in the switch's
  clone", and `granted(top, session_id)` is exactly the record branch of
  `consent`. I ran the named commands rather than trusting the two new cases.
  In another clone with a record, the fetch is silent and both creation forms
  get `allow`. From a linked worktree of the session's own clone, the switch
  names the split. With the press given from inside a linked worktree, a
  switch in the main tree names it too. In another clone without a record,
  the text names no split (all executed, probe 1). I also mutated each half
  of the condition. Making the clone test `True` turned S11 and the
  another-clone case red. Taking out the record's branch turned the
  already-split case red (executed). So the two cases do pin what the fix
  pass says they pin.
- **The press sentence is still #894's `PRESS`, byte for byte.** I parsed
  the guard source and found the only string constants that begin with the
  press sentence. In both languages each one is `PRESS[lang]` followed by
  `\n\n`. Every deny under the press, in both branches, both rows and both
  languages, carries `\n\n` + `PRESS[lang]` + `\n\n` (executed, probe 1).
- **S10's counts are unchanged.**
  `test_the_press_is_read_at_most_once_per_command` is not in the fix diff,
  so it is byte-identical. It passes at `57f46c5f` (executed). The only
  thing the fix adds under the press is `unattended_text`, and that calls
  `_clone_of` and `granted`. Both are `git rev-parse` and a `stat`, and
  neither calls `automation_answered` (read).
- **Round 1's yellow 2 is closed.** `choose` declares `Reads: observed` at
  `hooks/worktree-guard.py:1479`. The registry case passes (executed).
- **Round 1's yellow 3 is closed.** The Windows bullet, §*Unknowns resolve
  conservatively* and changelog item 3 all now except `[shared-tree-ok]`.
  That matches row 2's `not reliable and not shared_ok` (read).
- **Notes 4–6 are answered as stated.** The placeholder names both
  creation forms in both languages, and `ways_on` pins them. `handoff.md`
  names PR #902 and the verifying round. #894's S2 Proof cell names #894's
  one branch and #896's two reads (read).

## Findings

### 🟡 1 — in a clone that holds only this session's record, the deny says the press consents, and the record is what does

`hooks/worktree-guard.py:3157`, inside `unattended_text`. That is a unit
round 1's fix wrote, so this finding is a fix of a fix.

The record branch reuses the own-clone sentence: *That answer already
consents to creating one, so these commands pass as written*. In a second
clone, *that answer* (the press read from the session's own clone) consents
to nothing. `automation_answered` condition 4 refuses it there. The commands
pass because `consent` returns `"record"`. The creation's own `allow` then
says so: *A worktree creation already ran in this repository this session*
(executed, probe 1). Within one command pair, the model reads two
contradictory reasons for the same consent.
`test_a_clone_this_session_already_split_is_named_the_split` pins the false
sentence, because it compares against `ways_on`, which is the own-clone text.

**Why it matters.** This is the sentence round 1's blocking finding was about,
one branch over: the guard states as fact which answer consents where. Here
the behaviour is right and the stated fact is wrong. A model that trusts it
learns that the press reaches a clone it does not reach. §14 asks for the text
to say what the code does and for a case to pin that text.

**The fix** chooses the sentence by which consent holds. The own-clone text
stays byte for byte, so S3, S4, S7–S9 and S11 are untouched. Executed in the
clone: the replacement case failed against the guard at `57f46c5f` on the
English assertion. With the code fence applied, it passed together with the
whole module and `tests/test_worktree_guard.py` (157 passed, 1 skipped).
`ruff check` and `ruff format --check` were clean on both files.

### 🟡 2 — the docstrings and the changelog say *that answer* consents in a clone this session already split

`hooks/worktree-guard.py:27` and `hooks/worktree-guard.py:89` (the module
docstring), `tests/test_the_idle_session_rows_ask_nobody.py:11` (the module
docstring) and `:128` (the `ways_on` docstring), and
`seal/specs/1791781864-the-idle-session-rows-ask-nobody/changelog.md:14`
(item 1).

The fix pass carried the qualifier into every copy, but four copies attach
both clones to the answer. Examples: *where that answer consents to it: in the
clone it was given in, or where this session already created a worktree*, and
*split into a worktree with `git worktree add`, which that answer consents to
there*. The policy (`docs/worktree-guard-spec.md:614`) and the ledger's R1
attribute the record branch correctly, so the copies disagree with the
document they summarise. The changelog fragment is the one a person reads in
the release note.

I enumerated the class by searching for `consents`, `pass as written` and
`동의` across the hooks, the case module, the policy, both READMEs, the
item's changelog and both ledgers:

- Correct: the policy's *Under the press* paragraph, ledger R1, and the code
  comment above `press`.
- Misattributed: the four sites above, plus 🟡 1's reason text.
- Naming the press clone only: the policy's decision-matrix row, both
  READMEs, and #894's S2 and S9. They are incomplete, because they leave out
  the record clone, but nothing in them is false. I leave them as they are.

### ⬜ 3 — a press given in the switch's clone as well is still read as "another clone"

`hooks/worktree-guard.py:3181` (the other-clone text) and
`docs/worktree-guard-spec.md:619`.

`automation_answered` keeps the last answer per clone. So a session whose
person pressed `automation` while the session stood in clone B, and again in
clone A, holds consent in both. From A, a switch into B gets the other-clone
text, which says no way on exists. Yet the named creation in B gets `allow`
(executed, probe 1). The text hedges with *may be put to a person*. The policy
does not hedge: *a creation there is not consented*. Nobody is asked, so
nothing here needs a fix. The guard withholds a way on that exists. Telling
the two cases apart costs a second transcript read, which S10 forbids, or a
reader that returns every clone with a press. The smith can answer this with
grounds. If #903 makes §B's rows deny under the session-root press, the
difference stops mattering.

### ⬜ 4 — the policy paragraph's new sentences break the wrap, and one sentence now reads as if both reasons said it

`docs/worktree-guard-spec.md:620` is 99 characters in a paragraph wrapped at
79, and lines 632–633 break short. The sentence *The reason says a branch
already checked out in a worktree needs no switch* now follows the
another-clone sentence. That makes it read as if it describes both reasons,
but the other-clone reason does not say it. `tests/test_docs_line_wrap.py`
passes, so no check reads this paragraph's width.

### ⬜ 5 — round 1's record names `elsewhere` as a new unit and omits `unattended_text`

`seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-1.md`, row
`New units`. The fix table names `main`'s nested `unattended_text` and the two
cases. The record names the test helper `elsewhere` and the two cases. The
generator does not bound a nested function as a unit. This is a correction to
the run's paperwork, and it is why 🟡 1's `Location` is a line rather than
`path#unattended_text`.

## Regression tests to plant

- `tests/test_the_idle_session_rows_ask_nobody.py`: replace
  `test_a_clone_this_session_already_split_is_named_the_split` with the fenced
  version under 🟡 1. It now covers both languages and pins the record's
  sentence. I saw it red at `57f46c5f` (executed).

## Facts for the evidence ledger

- Under the press, the condition at `hooks/worktree-guard.py:3150` is
  equivalent to `consent(top, session)` for every session whose press is
  given in one clone only. `own` is the root `automation_pressed` reads, so a
  true press is a press in `own`. Where the press was given in more than one
  clone, the condition is narrower (⬜ 3). Coordinates:
  `hooks/worktree-guard.py#automation_pressed`,
  `hooks/worktree_consent.py#automation_answered`,
  `hooks/worktree_consent.py#consent`. Executed in probe 1.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | in a clone holding only this session's creation record, the deny says *that answer already consents*, while the press is refused there by condition 4 and the record is what consents; the already-split case pins the false sentence | `hooks/worktree-guard.py:3157` | open | executed (probe 1): the switch's reason carries the press sentence's claim, the creation's `allow` names the record; inside `unattended_text`, written by round 1's fix |
| 🟡 2 | the module docstrings of the guard and the case module, the `ways_on` docstring and changelog item 1 say the answer consents in a clone this session already split | `hooks/worktree-guard.py:27` | open | read: `hooks/worktree_consent.py#automation_answered` condition 4; the policy's *Under the press* paragraph and ledger R1 attribute it to the record |
| ⬜ 3 | a press also given in the switch's clone is read as another clone: no way on is named though the creation is `allow` | `hooks/worktree-guard.py:3181` | open | executed (probe 1); no person is asked; separating it costs a second transcript read (S10) |
| ⬜ 4 | the policy paragraph's line 620 is 99 wide, lines 632–633 break short, and the branch-already-in-a-worktree sentence reads as if both reasons said it | `docs/worktree-guard-spec.md:620` | open | read |
| ⬜ 5 | round 1's `New units` row names `elsewhere` and not `unattended_text` | `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/round-1.md` | open | correction to the run's paperwork; the fix table names `unattended_text` |
| 🟢 | round 1's blocking finding is closed — a switch into another clone names no split, and where the split is named its commands pass | `hooks/worktree-guard.py:3149` | confirmed | executed: probe 1 ran the named fetch and both creation forms (silent, `allow`, `allow`) and the linked-worktree paths; both halves of the condition mutated, each turned its cases red |
| 🟢 | round 1's yellow 2 is closed — `choose` declares `observed` | `hooks/worktree-guard.py:1479` | confirmed | read; `tests/test_a_reader_declares_its_input_class.py` passes (executed) |
| 🟢 | round 1's yellow 3 is closed — the Windows sentences except `[shared-tree-ok]` | `docs/worktree-guard-spec.md:981` | confirmed | read: the bullet, §*Unknowns resolve conservatively* and changelog item 3 match row 2's condition |
| 🟢 | round 1's notes 4, 5 and 6 are answered as stated | `tests/test_the_idle_session_rows_ask_nobody.py#ways_on` | confirmed | read: both creation paths in both languages; `handoff.md`; #894's S2 Proof cell |
| 🟢 | the press sentence is #894's `PRESS` byte for byte, in both branches, rows and languages | `hooks/worktree-guard.py:3135` | confirmed | executed (probe 1): source constants parsed and compared; every reason under the press carries it between blank lines |
| 🟢 | S10's transcript-read counts are unchanged | `tests/test_the_idle_session_rows_ask_nobody.py#test_the_press_is_read_at_most_once_per_command` | confirmed | read: not in the fix diff, and `unattended_text` reads no transcript; executed: passes |
| 🟢 | without the press, rows 1-b and 2 are the base's text | `hooks/worktree-guard.py#main` | confirmed | read: the fix diff touches only press-side text; executed: `tests/test_worktree_guard.py` passes |
| ❓ | on Windows, with nothing stubbed, a switch under the press is row 2's deny (M2) | `tests/test_the_idle_session_rows_ask_nobody.py` | ❓ out of verified scope | skipped off Windows and this round ran on darwin; the test workflow's Windows legs answer it at the pull request |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test -q -p no:cacheprovider` over `tests/test_the_idle_session_rows_ask_nobody.py`, `tests/test_worktree_guard.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_a_reader_declares_its_input_class.py`, `tests/test_a_folded_statement_names_what_enforces_it.py`, `tests/test_docs_line_wrap.py`, `tests/test_no_real_identifiers.py`, `tests/test_one_word_one_meaning.py`, in the clone at `57f46c5f` | 434 passed, 1 skipped (the Windows-only M2 case), exit 0 |
| `ruff check` and `ruff format --check` on `hooks/worktree-guard.py` and the case module | all checks passed; 2 files already formatted |
| `bin/evidence-check --ledger` on this item's fragment, #894's, and #868's (re-stamped by the fix range) | 27 ok, 39 ok, 239 ok, 0 drifted or broken; records arm 13 work items read, 0 refused |
| probe 1, a temporary test file (five cases), deleted after its run | as written in the round-1 answers above and in ⬜ 3: named commands in a recorded clone silent, `allow`, `allow`; linked-worktree paths name the split; two presses give the other-clone text while the creation is `allow`; press constants equal `PRESS[lang]` and `\n\n` |
| two mutations of the clone test in the clone's guard, each restored with `git restore` | the clone test made `True`: S11 and the another-clone case red; the record branch removed: the already-split case red |
| 🟡 1's two fences applied in the clone | the case red at `57f46c5f`'s guard on the English assertion; with the code fence, the module and `tests/test_worktree_guard.py` 157 passed, 1 skipped; ruff clean; both files restored, `git status --short` empty |
| broad gate (full suite, lint, typecheck) | not yet: no run made by anyone; it belongs to the sealer once the rounds settle, and with 🟡 1 and 🟡 2 open it is not yet due |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Nothing new is deferred. #903 holds §B's creation rows under a press read
from the session's root. It is not re-raised here, and ⬜ 3 would disappear if
#903 lands as a deny.

## Paste-ready fixes

### 🟡 1

`hooks/worktree-guard.py#main`, in `unattended_text`: replace everything
from `def unattended_text():` down to and including the first `+ split`. The
own-clone text joins back to today's bytes.

```python
    def unattended_text():
        own = worktree_consent._clone_of(repo_paths(cwd)[0])
        # Which consent names the split decides the sentence that says why it
        # passes: the press consents only in the clone it was given in, and
        # this session's record only in the clone it was written in.
        here = bool(own) and own == worktree_consent._clone_of(top)
        if here or worktree_consent.granted(top, session_id):
            why = (
                tr(
                    "That answer already consents to creating one, so these "
                    "commands pass as written:\n\n",
                    "그 답이 worktree 생성에 이미 동의했으므로, 아래 명령은 쓰인 그대로 "
                    "통과합니다.\n\n",
                )
                if here
                else tr(
                    "This session already created a worktree in this clone, and "
                    "that creation consents to the next one here, so these "
                    "commands pass as written:\n\n",
                    "이 세션은 이 클론에서 이미 worktree 를 만들었고 그 생성이 이 "
                    "클론의 다음 생성에도 동의하므로, 아래 명령은 쓰인 그대로 "
                    "통과합니다.\n\n",
                )
            )
            return (
                press
                + tr(
                    "The way on that needs nobody is to split into a worktree. ",
                    "사람이 없어도 되는 길은 worktree 로 분리하는 것입니다. ",
                )
                + why
                + split
```

`tests/test_the_idle_session_rows_ask_nobody.py`: replace the case whole.

```python
def test_a_clone_this_session_already_split_is_named_the_split(
    monkeypatch, capsys, projects, repo, tmp_path, wko
):
    """Round 1, red 1, the record's half. Where this session already created a
    worktree in the other clone, its creation record is consent there
    (`worktree_consent.granted`), so the switch into that clone names the
    split as it does in the session's own clone, and says the record
    consents rather than the press, which consents only in the clone it was
    given in (round 2). Both languages."""
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
```

### 🟡 2

`hooks/worktree-guard.py`, module docstring, §A's only-IDLE row (lines 25–28):

```
    can tell. Where the person pressed `automation` nobody is there to tell:
    a `deny` to the model on every attempt instead, naming the split as the
    way on where its creation is consented: by that answer in the clone it
    was given in, or by this session's record where it already created a
    worktree (#896)
```

The same docstring, the *Under the press* paragraph (lines 89–92):

```
direction's two sites deny on every attempt. Where a creation in the
switch's clone is consented -- by that answer in the clone it was given in,
or by this session's record in a clone it already created a worktree in --
the reason names the way on that needs nobody: split into a worktree and
work there by path. A switch into
```

`tests/test_the_idle_session_rows_ask_nobody.py`, module docstring (lines
11–18, which also brings line 17 back under the width):

```
Under the press both rows now `deny` on every attempt. Where a creation in
the switch's clone is consented -- by the press in the clone it was given
in, or by this session's record in a clone it already created a worktree
in -- the reason names the one way on that needs nobody: split into a
worktree and work there by path. In another clone it names no split,
because a creation there would be put to a person (round 1). It names no
question tool and no token, and it writes no choice marker, because no
question was put. Attended, both rows are the base's byte for byte
(`tests/test_worktree_guard.py`, S5).
```

The same file, the `ways_on` docstring:

```python
    """What follows the opening under the press where the split's creation
    is consented: no question, the split as plain commands, working there by
    path, and the re-issue sentence. The why-sentence is the press's, the
    one the session's own clone reads."""
```

`seal/specs/1791781864-the-idle-session-rows-ask-nobody/changelog.md`, item 1:

```
  1. Where the person pressed `automation`, both rows now refuse the switch
     to the model on every attempt. Where a creation in the switch's clone
     is consented, by that answer in the clone it was given in or by a
     worktree this session already created in that clone, the refusal names
     the way on that needs nobody: split into a worktree with `git worktree
     add` and work there by path with `git -C`. A switch into another clone
     is refused without one, because a split there would be put to the
     person. It names no question tool and no `[shared-tree-ok]`, and says
     that re-issuing the switch unchanged meets the same refusal.
```

Needs a fix: yes — 🟡 1 (the record branch's reason credits the press with a consent only the record gives, and a case pins it), 🟡 2 (four docstring and changelog copies credit the answer with the record clone's consent)

Loses a record or crashes: no

The broad gate has not come due. 🟡 1 and 🟡 2 are open, so a fix pass comes
before the sealer's spawn.

## Proof block

Files opened in this round, at `57f46c5f` unless named otherwise:

- `seal/specs/1791781864-the-idle-session-rows-ask-nobody/rounds/`: `round-1.md`, `round-1-report.md`, `round-1-fixes.md`; `handoff.md` (the table); `overview.md` and `changelog.md` (the fix diff)
- `hooks/worktree-guard.py`: the fix diff whole; `guard_worktree_creation` lines 1559–1680; `automation_pressed`; `main` lines 2854–3413; the branch's whole diff against `34fc36e9`; `stop_unrecognised` searched for a split
- `hooks/worktree_consent.py` lines 1–420: `consent_path`, `granted`, `_clone_of`, `automation_answered`, `consent`, `record`
- `tests/test_the_idle_session_rows_ask_nobody.py` lines 1–498; `tests/test_the_guard_asks_once_per_session.py` (`grant`, `ask_entries`, `write_transcript`, `PRESS`); `tests/conftest.py` (`repo`)
- `docs/worktree-guard-spec.md` lines 598–633 and the fix diff; `README.md` and `README.ko.md` (the fix diff)
- `seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md` (R1, S3·S4, S11), `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` (S2, S9), and the word diff of `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md` (anchor re-stamps only)
- `ruff.toml`
