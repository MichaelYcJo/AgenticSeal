# Feature Specification: the idle-session rows ask nobody

<!-- seal/specs/1791781864-the-idle-session-rows-ask-nobody/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Framed by `specseal:framer` on Fable 5.1 for #896. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | An `automation` press is the owner saying nobody is at the keyboard. A row that denies once with *call `AskUserQuestion`* and asks on every attempt after is a person's prompt one step removed, and under the press that is a defect whatever the guard read correctly |
| `docs/commit-review-gate-spec.md` §*Where the person said nobody would be answering, every stop is a deny* | The shape every stop takes under the press: a `deny` to the model whose reason names the ways on that need nobody, names no question tool, and says that re-issuing the command unchanged meets the same refusal. In 2 gives the two choice rows this shape. The same section says the last routing answer from the clone stands, so a later `per axis` takes a press back — which is why In 2 writes no choice marker |
| `docs/worktree-guard-spec.md` §A, rows *only IDLE sessions* and *detection unusable* | Today's rows: **choice**, because forgotten tabs are the user's call. They stay the attended verdict, byte for byte. Under the press there is no user to make the call |
| `docs/worktree-guard-spec.md` §A, *The stop has two readers* | The unrecognised-shape stop already reads the press through `hooks/worktree-guard.py#automation_pressed`, against the session's own root, and under the press its plain retry *meets the rows above*. In 2 is what those rows answer on that retry |
| `docs/worktree-guard-spec.md` §*Choice sites* | Three things In 2 keeps: the test for a site (*after declining, is there more than one command this session could issue?*) — under the press the answer is one, the split; the marker is written by `PreToolUse` and means *the question was put* — under the press no question is put, so none is written; and the token *records the user's answer in the command; nothing verifies that a user rather than the model put it there* — which is why In 2 does not name it (P1 (b)) and why its reading is left as it is (P2) |
| `docs/worktree-guard-spec.md` §*What a blocking prompt must show (identification)* | The per-session line is the **disaggregated signals** — the ages, each named. A present-tense claim is not a signal, and In 1 removes the one `fmt_sessions` appends |
| `docs/worktree-guard-spec.md` §*Unknowns resolve conservatively* | *A deny that fires on EVERY switch in an environment is no longer a cost, it is an outage.* In 2 under the press on Windows is such a deny, and §*Scope* says what keeps it from being an outage: the way on needs nobody and is always available. The owner's P1 (c) is the lever if that reading is wrong |
| `docs/worktree-guard-spec.md` §*Creation consent*, the table of five sources | The press is consent, read before every creation row, so under the press a `git worktree add` is allowed where it is the whole command and silent where it is not. That is what makes the split *the way on that needs nobody*, and why the deny names a plain `git worktree add` with no `[worktree-ok]`. *A `routing.md` is not read, not even as a fallback* — this work adds no reader and reads nothing new |
| `docs/worktree-guard-spec.md` §*Known limits*, the Windows bullet | Every tree state there reads *detection unusable*, so row 2 is every switch on Windows. Read from the code, not run |
| `seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md` §*The class*, and its `questions.md` P1 | #894 enumerated the class — every `ask` the guard can emit while the press is readable — and left rows 1-b and 2 to this item at P1 (a). Its In 2 is the register the deny below follows: the ways on first, each a command of its own, no question tool, the re-issue sentence |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | A test seen red, a stated failure direction, a prompt budget, platform honesty. Each is answered in §*Scope* and `plan.md` |
| `skills/agent-contract/SKILL.md` §12 | The class, not the coordinate. The line is printed by one function at six sites (In 1 names them); the press is read at the two `choose` sites of the switch direction, and §*The class* says why the creation direction's two choice rows take nothing |
| `skills/agent-contract/SKILL.md` §13, §14, §15 | The way on is run against the guard, not read off it (S7); the changed texts are pinned in both languages; every new case is seen red at the base |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | `seal/releases/0.9.1.md`'s row on `hooks/worktree-guard.py#choose`, stamped `ed62dd1a`, and the `main@…` families of `0.15.6`, `0.18.3` and `0.20.0` drift under this work. Each re-read is a `Re-read ·` citing row in this item's fragment, never an edit of a released file |
| `skills/writing-style/SKILL.md`, the Korean sentence rules | The Korean half of every text this work writes |

## Scope

### What was measured (read from #896; verified against the code, not re-run)

A `git switch -c <branch> origin/main` in a tree holding an old lease drew
this prompt on 2026-10-12 (the path is an example):

```
이 트리에 다른 Claude 세션이 있을 수 있으나, 작업 중임을 확인할 수 있는 것은 없습니다 — 3분 이상 활동(키 입력·작업 기록)이 없거나, lease 를 남긴 세션이 누구인지 확인되지 않습니다.
    (프로세스 미확인 세션 — VS Code 확장 패널·다른 cwd 의 세션 등)  /Users/x/work/feature  [lease: 5924d73a… pid 87946 alive, quiet]
        lease 선언 4.7시간 전 — 지금 이 트리에서 작업 중
```

Read from the code, this is row 1-b of §A. `hooks/worktree-guard.py#fresh_leases`
put the lease in its `unattributable` list as
`(None, "<top>  [lease: 5924d73a… pid 87946 alive, quiet]", None, 282.0, None)`
— alive, quiet past `IDLE_MIN`, and not a pid the process scan reported —
and `sessions_in_tree` appended that list to `idle`. `fmt_sessions`'s
`p is None` branch printed `kind` (*lease declaration* / *lease 선언*),
`_age(282.0)` (*4.7h ago* / *4.7시간 전*), and then the clause the function
appends to every unidentified entry whatever its age. The header above it was
written by row 1-b and says the opposite. Then `choose` denied once with the
`AskUserQuestion` instruction, and every attempt after was an `ask` — in a
session whose `routing.md` reads `Answer pressed | automation`.

### In 1 — the per-session line states what was measured, and nothing more

`hooks/worktree-guard.py#fmt_sessions`'s unidentified branch prints
`<kind> <age>` and stops there, in both languages: `lease declaration 4.7h
ago` / `lease 선언 4.7시간 전`, or `transcript activity 1m ago` / `작업
기록(트랜스크립트) 1분 전`. The clause *working on this tree right now* /
*지금 이 트리에서 작업 중* is removed from the function, not from one list.

- **It goes from every entry, not only the idle ones.** The function cannot
  tell which list it is printing, and the judgment is the header's at every
  site: *actively working* over the active list, *none of them can be shown
  to be working* over the idle list, and the stop's two sentences likewise.
  An unidentified entry in the active list — a lease under `IDLE_MIN` old,
  or fresh transcript activity with no process to pin it on — is active
  *because* its age is under the window, and the age is what the line says.
- **Six sites print it, through one function**: `guard_worktree_creation`
  (the ACTIVE row and the only-idle choice row), `stop_unrecognised` (the
  busy and the idle descriptions), and `main`'s switch ladder (the ACTIVE row
  and row 1-b). The pid branch of the function is unchanged.
- Not *last seen <age>* (`plan.md` A): `<kind> <age>` is already the
  measurement by name, and a second phrase for the same number would read as
  a third signal.

**Failure direction.** No verdict moves. **Prompt budget.** Unchanged.

### In 2 — under the press, the two choice rows deny on every attempt and name the split

Where `hooks/worktree-guard.py#automation_pressed(repo_paths(cwd)[0],
session_id, transcript_path)` is True — the session's own root, the reader
the stop already uses, every way of not reading the press being False — row
1-b (`idle and not shared_ok`) and row 2 (`not reliable and not shared_ok`)
respond `deny` on every attempt, and the reason:

- opens with the row's situation as today (row 1-b: its header, the idle
  sessions through `fmt_sessions`, the newest other-session snippet; row 2:
  the cannot-tell sentence);
- says that this session's person pressed `automation` on the routing
  question, so this guard puts no question to them and none is to be put to
  them in its place;
- names the one way on that needs nobody, **the split into a worktree**, as
  commands the model can issue: `git worktree add <wt_root>/<branch>
  <branch>` for a branch that already exists, or `git worktree add
  <wt_root>/<name> -b <branch> origin/main` for a new one, with no
  `[worktree-ok]` — under the press a creation is consented before any row
  is read (§*Creation consent*) — and then working in that tree by path from
  this session (`git -C <wt_root>/<name> …`, edits by absolute path), which
  is how this repository's own automation runs already work;
- names no question tool, and **does not name `[shared-tree-ok]`** — P1's
  default (b): pressing the token on the model's own judgment is the call
  the row exists to hand a person, and §*Choice sites* says nothing verifies
  who put it there;
- says that re-issuing the command unchanged meets the same refusal.

What it does **not** do, each decided from the tree:

- **It writes no choice marker.** `already_asked` is `PreToolUse`'s record
  that *the question was put*; under the press none is. So a session whose
  person later answers `per axis` in the same clone — the last answer stands
  (`docs/commit-review-gate-spec.md`) — meets the first-attempt deny with
  the question, as an attended session does today.
- **It changes nothing about the token's reading.** `git switch x #
  [shared-tree-ok]` under the press turns the two rows silent as it does
  attended (S6). The deny does not name the token, so a model that appends
  it read it elsewhere, and the command line records that it did — the same
  standing `[worktree-ok]` and `[no-review]` have. P2 lets the owner make the
  token inert under the press instead.
- **The creation direction's two choice rows take nothing.** §B's only-idle
  and detection-unusable rows sit below the consent row, and the press is
  consent, so no `choose` call in that direction runs under the press.
- **Attended, both rows are byte-identical to the base** (S5): the deny with
  the `AskUserQuestion` instruction once per session per direction, the
  `ask` after, the marker, `before_ask`.
- **A creation on the same line** is stopped with the deny — a deny stops
  the whole command — and the consent writer records nothing, because the
  command did not run (S8). The model then issues the creation alone, which
  the press consents to.

**Failure direction.** Blocks more, never allows more: in one reader's state
a verdict moves from *deny once, then ask* to *deny always*, and nowhere
else. A wrong deny — a press read where the owner had taken it back — costs
the model a turn and a worktree, and the reader that decides it is unchanged,
so this work produces no such reading the stop does not already produce.

**On Windows every switch takes row 2** (§*Known limits*), so under the press
every `git switch` there — in a shared tree and in a linked worktree alike,
since detection is unusable in both — is this deny. §*Unknowns resolve
conservatively* calls a deny on every switch in an environment an outage.
What keeps this one a cost rather than an outage is that its way on needs
nobody and never meets a prompt: `git worktree add <path> -b <branch>
origin/main` creates and checks the branch out with no switch, and under the
press it is consented. A `smith` in its worktree needs no switch at all. The
reading is from the code and not run on Windows, and P1 (c) is where the
owner overturns the trade.

**Prompt budget.** Under the press the two rows put zero questions to a
person, from one deny-with-instruction plus an `ask` per attempt after.
Attended, unchanged.

### The class (`agent-contract` §12)

| Site | Under the press today | This work |
|---|---|---|
| every reason that prints an unidentified session: `guard_worktree_creation` ×2, `stop_unrecognised` ×2, `main` ×2 | the line claims *working on this tree right now* at any age | **the line prints `<kind> <age>`** (In 1) |
| §A row 1-b, only IDLE sessions (`choose`, scope `switch`) | first attempt `deny` naming `AskUserQuestion`; every attempt after `ask` | **`deny` on every attempt, naming the split** (In 2) |
| §A row 2, detection unusable (`choose`, scope `switch`) | the same | **the same deny** (In 2) |
| §A row 1, ACTIVE | `deny` with the worktree steer, whoever is at the keyboard | unchanged |
| §A tracked-changes row | `deny` to the model (#894) | unchanged; read after the two rows, so a dirty tree in the idle state meets In 2 first |
| unrecognised shape, tree matters | `deny` naming the plain spelling (#826) | unchanged; its plain retry now meets In 2 in the idle and unusable states (S9) |
| §B only-idle and detection-unusable rows (`choose`, scope `create`) | unreachable: consent is read first | unchanged |

### Out of scope, each with why

- **Making `[shared-tree-ok]` inert under the press.** P2, default (a). New
  behaviour the ticket did not ask for, and the token's standing is an audit
  trail already.
- **Naming the token in the deny.** P1 (c); the frame is built on (b).
- **The attended choice site**: its two texts, its budget, its marker, its
  `before_ask`. Byte-identical (S5).
- **A cross-session, cross-machine or `routing.md` reading of the press, or
  a payload-shape guess.** #894 In 1 and its `plan.md` A–D say why each is
  refused; the owner's rule is to observe, not predict. This work reads the
  press through `automation_pressed` only.
- **`hooks/worktree_consent.py`, `hooks/commit-review-gate.py`,
  `hooks/cmdline_base.py`.** Byte-identical to the base (S12).
- **The headers above the per-session lines, and the pid branch of
  `fmt_sessions`.** They already say what was measured.
- **#21** (the attended dirty-tree prompt recommends an answer it does not
  offer) and **#20** (a declaration for the guard's answer). Different
  questions.
- **The 0.21.0 run's own protection.** The installed guard runs from the
  plugin cache, so this change protects the run after this release.

## User scenarios & acceptance *(mandatory)*

S1, S2 and S5 are cases in `tests/test_worktree_guard.py`; S3, S4 and S6–S11
in a new file, `tests/test_the_idle_session_rows_ask_nobody.py`, which
imports `ask_entries`, `write_transcript`, `decide`, `IDLE` and `ACTIVE`
from `tests/test_the_guard_asks_once_per_session.py` the way `pressed_root`
already does (`plan.md` H says why a new file). Each new case is seen red at
the base, `c38f97d7`, and the handover says how. The ages below are the
measured entry's: `282.0` minutes.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the line prints the measurement | Given an idle list holding `(None, "<top>  [lease: 5924d73a… pid 87946 alive, quiet]", None, 282.0, None)` · When `git switch feature/x` · Then the reason's session line is `        lease declaration 4.7h ago` and holds neither *working on this tree right now* nor *지금 이 트리에서 작업 중*; with `SPECSEAL_LANG=ko` the line is `        lease 선언 4.7시간 전`. The same with a transcript-activity entry `(None, "<top>", None, 1.0, None)` in the active list: `        transcript activity 1m ago` under the ACTIVE header | new case beside `test_switch_idle_sessions_offer_both_ways_on`; red at the base (the clause is present) |
| S2 the clause is gone from every site | Given the two entries of S1 · When each of the six sites is driven — `guard_worktree_creation` (ACTIVE row, only-idle row), `stop_unrecognised` (busy, idle), `main` (ACTIVE row, row 1-b) · Then no reason holds either clause, and the source of `hooks/worktree-guard.py` holds neither string | new case; red at the base |
| S3 under the press row 1-b denies every attempt | Given session `me`'s `automation` press (`ask_entries`, `write_transcript`), sessions `([], IDLE, True)` · When `git switch feature/x` three times · Then `deny` each time with one text: the row's header, the idle line, the press sentence, the split named with `worktree add <wt_root>/<branch> <branch>` and `worktree add <wt_root>/<name> -b <branch> origin/main`, `git -C`, the re-issue sentence; no `AskUserQuestion`, no `[shared-tree-ok]`, no `[worktree-ok]`; `<git-dir>/specseal-worktree-choice/switch/` holds no `me`. Both languages | new case; red at the base (`deny`, `ask`, `ask`) |
| S4 under the press row 2 denies every attempt | The same with sessions `([], [], False)` and row 2's header | new case; red at the base |
| S5 without the press both rows are the base's | Given no press · When `git switch feature/x` twice in each of the two states · Then attempt 1 is `deny` with the `AskUserQuestion` instruction and attempt 2 is `ask`, each reason byte-identical to the base's, both languages | the three existing cases stay (`test_switch_idle_sessions_offer_both_ways_on`, `test_the_second_attempt_gets_the_plain_prompt`, `test_switch_unreliable_detection_offers_both_ways_on`); one new assertion compares against the base's text captured in the case, the way #894's `ATTENDED_ASK` does |
| S6 the token's reading is unchanged under the press | Given the press, each of the two states, a clean tree · When `git switch feature/x  # [shared-tree-ok]` · Then silent, as attended; with one modified tracked file, #894's deny with the token lead | new case; green at the base for the clean half, which is the point — it pins P2 (a) |
| S7 the way on passes the guard | Given the press and the idle state · When `git worktree add ../wt -b feature/x` is judged by the guard and then run by git in the fixture, then `git -C ../wt status` is judged · Then the creation is `allow` (consent), the worktree exists on `feature/x`, and the status is silent (listed) | new case, real git; W3 decides the fixture's remote |
| S8 a creation on the same line is stopped with it and records nothing | Given the press, the idle state, no consent record · When `git switch feature/x && git worktree add ../wt f` · Then `deny` with S3's text, and `specseal-worktree-consent/` holds no `me` | new case; the PostToolUse writer is not run because the command did not |
| S9 the plain retry after the stop meets the deny | Given the press, the idle state, then the unusable state · When `git checkout feature/x` then `git switch feature/x` · Then the stop's `deny`, then S3's (S4's) `deny`; in the ACTIVE state both are the deny with the worktree steer, as today | new case (an extension of #894's S6 to the two states it does not cover, in the new file) |
| S10 the press is read at most once per command | Given a counting `worktree_consent.automation_answered` · When a switch in the clean single-stream state, the idle state, the idle-and-dirty state, and `git checkout README.md && git switch feature/x` in the idle state · Then the count is 0, 1, 1, 1 | new case, the shape of `test_the_tree_is_read_once_for_both_kinds`; W2 |
| S11 the press is read from the session's own root | Given the press in the session's own clone's transcript and a second clone `W` in the idle state · When `git -C W switch x` · Then S3's deny; with the press written under `W`'s clone only, the attended first-attempt deny | new case, the shape of #894's `test_the_press_is_read_from_the_sessions_own_root` |
| S12 the other readers are unchanged | `hooks/worktree_consent.py`, `hooks/commit-review-gate.py`, `hooks/cmdline_base.py` byte-identical to `c38f97d7` | `git diff c38f97d7 -- <the three>` empty; asserted by the handover |
| S13 the policy says what the code does | `docs/worktree-guard-spec.md` §A rows 1-b and 2 carry In 2; *The stop has two readers* says the plain retry meets In 2 in those states; §*Choice sites* gains a paragraph *Under the press* with `Enforced by:` naming S3, S4, S6, S8, S10; §*What a blocking prompt must show* says the line is the signals and nothing after them (S1, S2); §*Known limits* replaces #894's sentence about these rows with In 2's and the Windows bullet gains the press consequence; the module docstring's rows 1-b and 2 and its CHOICE paragraph say the same in their words; `README.md` and `README.ko.md`'s `worktree-guard` row gain one clause each, together | `bin/test tests/test_a_folded_statement_names_what_enforces_it.py tests/test_docs_line_wrap.py`; the survivor sweep at the pull request |
| S14 the fragments | `seal/specs/1791781864-…/changelog.md` says what a person sees differently; `seal/ledger/1791781864-….md` holds S1–S13's rows and the `Re-read ·` rows for every released row `choose` and `main` drift | `bin/evidence-check seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md`; the hygiene workflow at the pull request |

## Data & interfaces

- `hooks/worktree-guard.py#fmt_sessions`: the two unidentified f-strings
  lose their tail after `{_age(tr_idle)}`. Signature unchanged.
- `hooks/worktree-guard.py#choose`: gains `pressed=False` and the way-on
  text; where `pressed`, it responds `deny` with `situation` plus that text
  before the marker logic, so `already_asked` is not called. W1 decides
  whether the text is composed in `main` from `steer` or inside `choose`.
- `hooks/worktree-guard.py#main`: the two `choose` calls of the switch
  ladder pass `pressed=automation_pressed(repo_paths(cwd)[0], session_id,
  transcript_path)`, evaluated only where the row fires (W2), so a command
  reads the transcript at most once (S10). The creation ladder's `choose`
  calls pass nothing.
- Text: one new `tr(en, ko)` pair for the press paragraph and the way on,
  following the register of #894's dirty-row deny and
  `hooks/commit-review-gate.py#AUTOMATION_WAYS`.
- No new file, marker, environment variable, payload field or reader. No
  change to `hooks/hooks.json`.

## Rule changes

- nothing
  why: written: the choice rows under the press, in docs/worktree-guard-spec.md
    *Choice sites*.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the clause ending an unidentified session's per-session line, saying it was working on the tree now, at any age (In 1) | `hooks/worktree-guard.py#fmt_sessions>"working on this tree right now"` | nowhere: the header above every list carries the judgment, and `docs/worktree-guard-spec.md` §*What a blocking prompt must show* says the line is the signals alone |
| the Korean half of the same clause | `hooks/worktree-guard.py#fmt_sessions>"지금 이 트리에서 작업 중"` | the same |
| #894's §*Known limits* bullet saying the two choice rows still reach a person under the press | `docs/worktree-guard-spec.md#"## Known limits">"detection unusable, still reach a person: the first attempt is a `deny`"` | §*Choice sites*, *Under the press*, and the bullet that replaced it |

Written by the smith in phase 3, after #835 landed `Removes from` in
`seal/config.md` at a work-item id below this one; the frame predates the
rule. The rows are the removals `spec.md` In 1 and `plan.md` §*Seams* already
name.

## Open questions → questions.md

P1, P2 (a person); M1, M2 (a measurement); W1, W2, W3 (the work). Each row
says which judgment it could not settle from the tree and who closes it.

Framed 2026-10-12 by framer, before the build.
