# Round 2 report — 1791852612-under-automation-a-creation-in-another-clone-asks-nobody (#903)

| Field | Value |
|---|---|
| Round | 2, the verifying round |
| Target | the fix diff `6528e2eb..462e6dd5` (2 commits), draft PR #916 into `release/v0.21.1` |
| Target SHA | `d71acaf9` |
| Base | `origin/release/v0.21.1` at `321e9de1` |
| Reviewed by | warden |
| Where it ran | a `git clone --no-local` of the worktree at `d71acaf9`, under the session scratchpad, removed before handover |
| Earlier rounds | `rounds/round-1.md` and `rounds/round-1-report.md`, read for coordinates; every verdict below is re-derived |

Every case run in this round ran with `SPECSEAL_CASE_CEILING_S=600`, because
the machine was loaded.

## What this round answers

Round 1 recorded three findings closed. This round opened each fix and asked
whether it closes the finding, then judged the two surfaces the fixes created:
the new `plain_origin` argument and the new case.

```
🟡 1  quote note named [worktree-ok] under the press   -> closed (executed: red without the fix, green with it)
🟡 2  third copy of the shared sentences             -> closed (executed: a reword now reaches the tracked-changes row)
🟡 3  READMEs said "not at all" under the press      -> closed (read: both rows scoped to the press's own clone)
   new surface: plain_origin, judge_creation's Reads: line
      ├─ 🟢 the Reads: line's class and direction are right
      ├─ ⬜ 5  the `lead` line has a fallback no caller reaches, and its attended arm survives deletion
      └─ ⬜ 6  the policy's Enforced-by line does not name the new case
```

Nothing found needs a fix. The two notes are about pins and paperwork; the
behaviour is right in every state probed.

## The three closures

### 🟡 1 is closed: under the press the quote note no longer reaches the deny

`judge_creation` now keeps the origin before the quote note as
`plain_origin` (`hooks/worktree-guard.py:2029`) and hands it to
`guard_worktree_creation`. Rows 3 and 4 open with it where the press is
read, and with the full origin otherwise (`:1870`, `:1908`). Row 5 still
opens with the full origin, which is #920's surface and unchanged by this
diff.

Executed: the new case passes at `d71acaf9`. With both `lead` lines put back
to `origin`, its two parameters fail (probe 2), so the case was seen red
against the defect it pins, as its docstring claims. The press is still read
once per firing row, inside each row's `if`, so S10's `[1, 2, 1, 2]` holds,
and the new module passes whole (probe 1).

### 🟡 2 is closed: the tracked-changes row now says the shared strings

The row under the press (`hooks/worktree-guard.py:3585`, `:3610`) now calls
`press_sentence()` and `reissue_sentence()` instead of carrying copies.
Read: both strings are byte for byte the copies they replace, in both
languages, so nothing a reader sees changed, and `dirty_deny` in
`tests/test_the_guard_asks_once_per_session.py` still pins the same text.

Executed: with `press_sentence`'s English reworded, cases in
`tests/test_the_guard_asks_once_per_session.py` now fail, among them
`test_the_plain_retry_meets_todays_rows` (probe 5). Round 1's probe 5 found
the same module at 101 passed under the same reword. A reword now reaches
the row instead of leaving it behind, and ledger S9's *one string each*
holds.

`hooks/commit-review-gate.py:803` and `hooks/gate.py:272` carry press
sentences of their own. They speak for another hook ("this gate") and are not
copies of this guard's string, so they are outside the class. Over the
branch range the surviving-wording check is clean (probe 6).

### 🟡 3 is closed: both READMEs scope the press to the clone it was given in

`README.md:201` and `README.ko.md:198` now say a creation is not asked at
all under the press *in the clone that answer was given in*. Read against
`hooks/worktree-guard.py#guard_worktree_creation`: row 0's consent answers
every creation in that clone, so the sentence is true there, and the same
row's next sentences already say what happens in another clone. No other
document in the tree carries the old claim (read: a search over every
tracked `.md` outside `seal/specs/` and `seal/releases/`).

## The new surface

### The `Reads:` line on `judge_creation` is right

`Reads: guess — …; unknown mixed` (`hooks/worktree-guard.py:1963`).

- **Class.** The unit parses the command the model wrote, through
  `has_token`, `parses_cleanly` and `only_creates_a_worktree`. The registry
  gives a unit parsing text its caller handed it the class of where that text
  came from, so `guess` is right.
- **Direction.** An input it cannot understand is a command the lexer gives
  up on. Without consent, `has_token` reads no token from it and the ladder
  stops it: an `ask` at row 1, a choice or the press's deny at rows 3 and 4, a
  `deny` at row 5. With consent, `only_creates_a_worktree` refuses to vouch
  for it, so `consented` is `silent`, the guard returns without responding,
  and the harness's own flow judges the call, a pass. Both happen, so `mixed`
  is the right word. The paragraph under the line says exactly this.

The line's grammar is executed: `tests/test_a_reader_declares_its_input_class.py`
passes at `d71acaf9` (probe 1).

### ⬜ 5 — the `lead` line carries a fallback no caller reaches, and its attended arm survives deletion

`hooks/worktree-guard.py:1870` and `:1908` read
`lead = (plain_origin or origin) if pressed else origin`.

- **The fallback.** `plain_origin` defaults to `""`, and `judge_creation` is
  the only caller of `guard_worktree_creation` in the tree; it always passes a
  non-empty string. Executed: with the fallback dropped, the guard modules
  stay green (probe 4). This is the condition nothing can make false that this
  function's own comment at row 0 argues against.
- **The attended arm.** With `if pressed else origin` dropped, so that
  attended rows 3 and 4 also lose the quote note, 268 cases across the four
  guard modules stay green (probe 3). The policy says *attended both rows are
  what they were, word for word*, and its enforcing case,
  `test_the_attended_creation_choice_rows_are_the_bases`, uses no quote.

Nothing ships wrong: both arms do the right thing today. The note is that the
fix added a branch whose attended half no case reaches. The case to plant
for it is in *Regression tests to plant* below.

### ⬜ 6 — the policy's Enforced-by line does not name the new case

`docs/worktree-guard-spec.md` §*A creation in another clone under the press*
says the deny *names no question tool, no `[worktree-ok]`*. For a command with
an unbalanced quote, the case that holds that sentence is
`test_an_unbalanced_quote_under_the_press_names_no_token`, and the
subsection's `Enforced by:` line does not list it. The ledger's S1 row does.
Adding the case to that line ties the sentence to the case for the input
that broke it.

## Regression tests to plant

For ⬜ 5's attended arm, destination
`tests/test_a_creation_in_another_clone_asks_nobody.py`, beside the new
case:

```python
@pytest.mark.parametrize("row", ["idle", "unusable"])
def test_attended_an_unbalanced_quote_keeps_the_quote_note(
    monkeypatch, capsys, projects, repo, other, wko, row
):
    """Attended, rows 3 and 4 open with the origin and its quote note, as
    they did at the base: only the press drops the note (round 2, note 5)."""
    write_transcript(projects, "me", [])
    command = creation(other, "  # don't")
    for lang, module in (("en", wg), ("ko", wko)):
        decision, reason = judge(module, monkeypatch, capsys, repo, command, ROWS[row])
        assert decision == "deny", (lang, decision)
        assert "[worktree-ok]" in reason.splitlines()[0], (lang, reason)
```

It has not been run. The transcript call with an empty list is a guess at
how this module plants an attended session; the smith checks it against
`write_transcript` and sees the case go red with `if pressed else origin`
removed before planting it.

## Facts for the evidence ledger

None new. Ledger S1 already names the new case, and S9's *one string each*
now holds for the tracked-changes row too (probe 5).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — under the press an unbalanced quote no longer puts `[worktree-ok]` into rows 3 and 4's deny | `hooks/worktree-guard.py:1870` | confirmed | executed (probes 1, 2): the new case passes at `d71acaf9` and fails both parameters with the two `lead` lines put back to `origin` |
| 🟢 | round 1's finding 2 is closed — the tracked-changes row says the shared press and re-issue strings | `hooks/worktree-guard.py:3585` | confirmed | read: the strings are byte for byte the copies they replace; executed (probe 5): a reword of `press_sentence` now fails cases in `tests/test_the_guard_asks_once_per_session.py`, which passed 101 under round 1's reword |
| 🟢 | round 1's finding 3 is closed — both READMEs scope the press's no-question creation to its own clone | `README.md:201` | confirmed | read: row 0 answers every creation in the press's clone; `README.ko.md:198` says the same; no other tracked `.md` carries the old claim |
| 🟢 | `judge_creation`'s `Reads: guess … unknown mixed` is the right class and direction | `hooks/worktree-guard.py:1963` | confirmed | read: it parses the model's command; an untokenizable command is stopped without consent and left silent under it; executed (probe 1): the declaration check passes |
| 🟢 | the `plain_origin` argument breaks no call site | `hooks/worktree-guard.py:1607` | confirmed | read: `judge_creation` is the only caller of `guard_worktree_creation` in hooks and tests |
| ⬜ 5 | the `lead` line's `or origin` fallback is unreachable, and its attended arm survives deletion with every case green | `hooks/worktree-guard.py:1870` | open | executed (probes 3, 4): both mutations leave 268 cases green; behaviour is right in both arms today |
| ⬜ 6 | the policy subsection's `Enforced by:` line does not name the case that holds *names no `[worktree-ok]`* for a command with an unbalanced quote | `docs/worktree-guard-spec.md:558` | open | read: the ledger's S1 row names the case; the subsection's line does not |

## Executed probes

| What was run | Result |
|---|---|
| 1. `bin/test` on `tests/test_a_creation_in_another_clone_asks_nobody.py` and `tests/test_a_reader_declares_its_input_class.py`, at `d71acaf9` | exit 0 |
| 2. a `test_tmp_*` probe: both `lead` lines replaced by `lead = origin`, then `test_an_unbalanced_quote_under_the_press_names_no_token`; file restored and its hash checked | exit 1, both parameters failed |
| 3. the same probe: both `lead` lines replaced by `lead = plain_origin or origin` (attended arm dropped), then the new module, `tests/test_worktree_guard.py`, `tests/test_the_guard_asks_once_per_session.py` and `tests/test_the_idle_session_rows_ask_nobody.py` | exit 0, 268 passed, 2 skipped (Windows-only) |
| 4. the same probe: both `lead` lines replaced by `lead = plain_origin if pressed else origin` (fallback dropped), the same four modules | exit 0, 268 passed, 2 skipped |
| 5. the same probe: `press_sentence`'s English reworded, then `tests/test_the_guard_asks_once_per_session.py` and `tests/test_the_idle_session_rows_ask_nobody.py` | exit 1, 30 failed across both, including `test_the_plain_retry_meets_todays_rows` in the first |
| 6. `skills/code-review/scripts/survivor_check.py --range 321e9de1...d71acaf9` with every `seal/specs/*/survivors.md` as `--exempt`, as the broad gate runs it | exit 0, no removed wording standing. Over the fix range alone it lists three press sentences in other hooks; they are those hooks' own strings, and the broad gate does not read that range |
| 7. `bin/test` on `tests/test_a_corrected_sentence_survives_elsewhere.py` | exit 0, 173 passed |
| The broad gate: full suite, repository-wide lint, typecheck | not yet. It is the sealer's. This report leaves nothing needing a fix, so it has come due: the sealer's spawn is next |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round 1, ⬜ 4 | `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md:30` | carried open, closes once at the run's end; not reported again |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| under the press in another clone, row 5's hints still name `[worktree-ok]` | issue #920, already deferred before this round; the fix diff did not touch row 5 | the owner, through #920 |

Needs a fix: no
Loses a record or crashes: no

## Proof block

Files opened this round: `hooks/worktree-guard.py` (lines 359–500,
1465–2070, 2810–2880, 3530–3620), `tests/test_a_creation_in_another_clone_asks_nobody.py`
(lines 1–80, 247–268), `tests/test_the_guard_asks_once_per_session.py`
(lines 1827–1895), `tests/test_worktree_guard.py` (lines 1205–1285),
`docs/worktree-guard-spec.md` (lines 177–185, 527–558),
`docs/the-reader-registry.md` (lines 15–92), `README.md:201`,
`README.ko.md:198`, this item's `spec.md` (lines 13–80), `overview.md`,
`rounds/round-1.md`, `rounds/round-1-report.md`, and the ledger fragment's
S1, S9 and S11 rows. The clone, its virtual environment and the probe file
were removed before handover.
