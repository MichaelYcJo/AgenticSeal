# Feature Specification: under automation, a creation in another clone asks nobody

<!-- seal/specs/1791852612-under-automation-a-creation-in-another-clone-asks-nobody/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Framed by `specseal:framer` on Fable 5.1 for #903. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| The owner's decision on #903, 2026-10-13, given before the first edit (the issue's one comment; `routing.md` §*Why this way*) | Under the `automation` press, read from the session's own root, §B's two choice rows — only IDLE sessions, detection unusable — deny to the model, as §A's two rows do since #896, and `docs/worktree-guard-spec.md` §*Creation consent* changes with it. This frame carries that decision out and does not reopen it |
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | A press is the owner saying nobody is at the keyboard. A row that denies once with *call `AskUserQuestion`* and asks on every attempt after is a person's prompt one step removed, and under the press that is a defect whatever the guard read correctly |
| `docs/commit-review-gate-spec.md` §*commit-review-gate*, *Where the person said nobody would be answering, every stop is a deny* | The shape every stop takes under the press: a `deny` to the model whose reason names no question tool and says re-issuing the command unchanged meets the same refusal. In 1 gives the two creation rows this shape |
| `docs/worktree-guard-spec.md` §B, rows *only IDLE sessions* and *detection unusable* | Today's rows: **choice** — create it, or switch in the shared tree. They stay the attended verdict, byte for byte. Under the press there is no user to make the call |
| `docs/worktree-guard-spec.md` §B, the consent row, and §*Creation consent* rule 4 *The same clone* | Why the two rows are reachable under the press at all: the press is consent only where the result entry's `cwd` resolves to the creation's clone (`hooks/worktree_consent.py#automation_answered`, condition 4), and this session's record only in a clone it already split (`#granted`). In the press's own clone row 0 answers every creation; in another clone, with no record, the ladder falls through to rows 1–5, and rows 3 and 4 are the two the owner decided |
| `docs/worktree-guard-spec.md` §*Choice sites*, *Under the press the switch direction's two sites deny on every attempt* | The register and the rules In 1 follows: the reason opens with the row's situation, carries the press sentence, names no question tool and no token, writes no marker because no question was put, and says re-issuing meets the same refusal. Its last sentence — *In the press's own clone the creation direction's two sites never run under the press* — stays true and gains the other clone's half |
| `docs/worktree-guard-spec.md` §*Choice sites*, the token table and *The token records the user's answer in the command; nothing verifies that a user rather than the model put it there* | Why the deny names neither token. `[worktree-ok]` reaches an `ask`, a person's prompt; `[shared-tree-ok]` would let the model take the shared tree on its own judgment, the call the row exists to hand a person (#896's P1 (b)) |
| `hooks/worktree-guard.py#main`, the other-clone branch of `unattended_text` (#896 round 1, red 1) | The sibling text for a switch into another clone: *the press consents to creating a worktree only in a clone it was given in … this guard names no way on here. Leave this switch to a session working in the clone this tree is in.* In 1's deny says the same of the creation, in the same words where the act is the same |
| `docs/worktree-guard-spec.md` §*Unknowns resolve conservatively* and §*Known limits*, the Windows bullet | On Windows every creation reads *detection unusable* and takes row 4. Under the press, a creation in the session's own clone there is consented before row 4; one in another clone is In 1's deny. A deny on every creation in another clone is not an outage: the press's own clone is where the run works, and nothing stops there |
| `seal/specs/1791781864-the-idle-session-rows-ask-nobody/spec.md` §*The class*, row *§B only-idle and detection-unusable rows*, and its `rounds/round-1-report.md` §*Deferred* | #896's frame wrote those rows *unreachable: consent is read first*, which is true in the press's own clone and false in another; its round 1 found the switch rows' deny steering the model into exactly that clone, fixed the steer, and deferred the rows to #903. This work closes them |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | A test seen red, a stated failure direction, a prompt budget, platform honesty, a `Reads:` line on every unit changed, and a frame that names what it removes. Each is answered below or in `plan.md` |
| `docs/the-reader-registry.md` §*A reader declares its input class* (through `CONTRIBUTING.md`'s `Reads:` bullet) and `tests/undeclared_readers.txt` | `guard_worktree_creation` is on the census at `321e9de1` (`hooks/worktree-guard.py#guard_worktree_creation`, the line naming its hash there). A changed unit declares and leaves it; this work changes it |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | The `## Removes` grammar below, read by `evidence-check`; `seal/config.md`'s `Removes from` row binds this frame |
| `skills/agent-contract/SKILL.md` §12, §13, §14, §15 | The class, not the coordinate — §*The class* below enumerates every creation-ladder row under the press in another clone; the way the text is pinned is run against the guard, not read off it; both languages are pinned; every new case is seen red at `321e9de1` |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | The released rows on `hooks/worktree-guard.py#guard_worktree_creation` as it stood at `321e9de1` (`seal/releases/0.9.1.md`, `0.9.4.md`, `0.15.5.md`, `0.15.6.md`, `0.20.0.md`) and on `#choose` (`0.9.1.md`, `0.21.0.md`) drift under this work. Each re-read is a `Re-read ·` citing row in this item's fragment, never an edit of a released file |
| `skills/writing-style/SKILL.md`, the Korean sentence rules | The Korean half of every text this work writes |

## Scope

### What was measured (read from #896's round 1, not re-run)

Round 1 of work item 1791781864 (`rounds/round-1-report.md`, red 1 and
§*Deferred*) found the switch rows' deny under the press naming the split as
the way on for a switch into another clone. A model that took it issued
`git -C <other> worktree add …` there, and the creation ladder in that clone
read no consent — `worktree_consent.consent` returns `""` where the press's
result entry sits in a different clone (condition 4) and this session holds
no record there — so §B's only-idle or detection-unusable row ran, `choose`
denied once naming `AskUserQuestion`, and asked a person on every attempt
after. Red 1's fix stopped the steer: the switch deny names no split for
another clone. The rows themselves were left to this work, because turning
them into a deny is a policy change to §*Creation consent*, and the owner
answered it on 2026-10-13.

Read from the code, the ladder in `hooks/worktree-guard.py#guard_worktree_creation`
runs, for a Bash creation whose tree is in another clone than the session's
own and for which this session holds no record: row 1 (ACTIVE, `ask`), row 2
(`[worktree-ok]`, `ask`), row 3 (only idle, `choose` with scope `create`),
row 4 (detection unusable, `choose`), row 5 (single stream, `deny`). Rows 3
and 4 are this work's.

### In 1 — under the press, the two creation choice rows deny on every attempt, naming no way on

Where `hooks/worktree-guard.py#automation_pressed(repo_paths(cwd)[0],
session_id, transcript_path)` is True — `cwd` is the session's shell
directory, which `main` hands `guard_worktree_creation` on purpose (*`cwd`,
not the creation's directory*), so the read is against the session's own
root, by the reader the switch rows and the stop use, every way of not
reading the press being False — row 3 (`if idle:`) and row 4 (`if not
reliable:`) respond `deny` on every attempt, through `choose`'s `pressed`
verdict, and the reason:

- opens with the row's situation as today: `origin`, then for row 3 the
  only-idle sentence, the idle sessions through `fmt_sessions` and the
  newest other-session snippet, and for row 4 the cannot-tell sentence;
- carries the press sentence #896 wrote, byte for byte: *This session's
  person pressed `automation` on the routing question, so this guard puts
  no question to them, and none is to be put to them in its place.*;
- says why no way on is named, in the switch deny's other-clone words where
  the act is the same: that answer was read in this session's own clone and
  consents to creating a worktree only in a clone it was given in; this tree
  is in another clone, where this session has created no worktree; nobody is
  at the keyboard to choose between splitting it and switching in its shared
  tree; so this guard names no way on here, and the tree is left to a
  session working in the clone it is in;
- names no question tool, **no `[worktree-ok]`** — the token's row is an
  `ask`, a person's prompt — and **no `[shared-tree-ok]`** — the shared
  tree is the call the row exists to hand a person (#896 P1 (b));
- says that re-issuing the command unchanged meets the same refusal.

What it does **not** do, each decided from the tree:

- **It writes no choice marker.** `choose` returns before `already_asked`
  under `pressed`, so `<git-dir>/specseal-worktree-choice/create/` gains no
  file in the other clone. A session whose person later answers `per axis`
  — the last answer stands — meets the attended first attempt there.
- **It records no consent.** The deny stops the command, so the
  `PostToolUse` writer sees no creation that ran, and
  `specseal-worktree-consent/` in either clone stays as it was.
- **It changes nothing about either token's reading.** `[worktree-ok]`
  still reaches row 2's `ask` under the press, above these rows, as
  attended (S6); the deny does not name it, so a model that appends it read
  it elsewhere, and the command line records that it did — the standing
  `[worktree-ok]` and `[no-review]` have. `[shared-tree-ok]` is a switch
  token and the creation ladder reads none.
- **Row 1 (ACTIVE) and row 2 (`[worktree-ok]`) keep their `ask`, and row 5
  its `deny`.** The owner's decision names the two choice rows. Row 1 under
  the press in another clone is still a question to a person; it is P1 in
  `questions.md`, built on *unchanged*, and §*The class* says so.
- **In the press's own clone nothing moves.** Row 0 reads the press as
  consent before any row below it, so a bare creation is `allow` and a
  compound is `silent`, as at the base (S4). Where this session holds a
  record in the other clone, row 0 reads it first and the rows are not
  reached either (S5).
- **Attended, both rows are byte-identical to the base** (S3): the deny
  with the `AskUserQuestion` instruction once per session per direction,
  the `ask` after, the marker.
- **The Agent/Task path is untouched.** An isolated agent's worktree lands
  under the session's own repository, where the press is consent, so that
  path never reaches another clone's rows.

**Failure direction.** Blocks more, never allows more: in one reader's state
a verdict moves from *deny once, then ask* to *deny always*, and nowhere
else. A wrong deny — a press read where the owner had taken it back —
costs the model a turn and leaves the other clone untouched, and the reader
that decides it is unchanged, so this work produces no such reading the
switch rows do not already produce.

**Prompt budget.** Under the press the two rows put zero questions to a
person, from one deny-with-instruction plus an `ask` per attempt after.
Attended, unchanged. **On Windows** every creation takes row 4, so under
the press every Bash creation in another clone there is this deny, and
every creation in the press's own clone is consented as before; read from
the code, measured by M1's Windows-only case.

**What the transcript costs.** A creation in another clone under the press
reads the transcript twice — once by `worktree_consent.consent` for the
creation's clone, which finds no press there, and once by
`automation_pressed` for the session's own root. In the press's own clone it
is read once, by `consent`, and the rows are never reached. S10 counts it.

### The class (`agent-contract` §12)

Every row of the Bash creation ladder, under the press, for a creation in
another clone where this session holds no record:

| Row | Under the press today | This work |
|---|---|---|
| 0, consent | not held: the press is consent only in its own clone (condition 4), the record only where it was written | unchanged; it is what makes the rows below reachable |
| 1, ACTIVE session in the other clone | `ask` — separation justified, creation still needs a human | **unchanged**; P1 in `questions.md`, outside the owner's decision |
| 2, `[worktree-ok]` given | `ask` | unchanged; S6 pins it, and the deny below names no token |
| 3, only IDLE sessions (`choose`, scope `create`) | first attempt `deny` naming `AskUserQuestion`; every attempt after `ask` | **`deny` on every attempt, naming no way on** (In 1) |
| 4, detection unusable (`choose`, scope `create`) | the same | **the same deny** (In 1) |
| 5, single stream | `deny`, steer to `git switch` in that clone | unchanged; under the press the switch it names meets §A's rows there, which since #896 deny naming no split for another clone, or pass silently in a clean single-stream tree |
| Agent/Task, `isolation: "worktree"` | silent under the press, in the session's own clone | unchanged; never another clone |

### Out of scope, each with why

- **Row 1's `ask` under the press in another clone.** P1, default *unchanged*:
  the owner's decision names the two choice rows, and widening it is the
  frame deciding a policy change the owner did not. One sentence of text
  and one case away if the owner takes the lever.
- **Naming the session's own clone as the place to split instead.** `plan.md`
  C. The guard cannot know whether the two clones hold the same repository,
  and a worktree nobody asked for is the six-months failure #896's plan
  named.
- **Reading the press as consent in every clone** (dropping condition 4).
  `plan.md` D. It is the reading the owner's decision refuses by saying
  *deny*, and it would allow more.
- **Making either token inert under the press.** #896's P2 (a) stands for
  `[shared-tree-ok]`; `[worktree-ok]`'s row is above these and is an `ask`
  by design (§B's token row). Neither token is named, which is the bound.
- **A cross-session, cross-machine or `routing.md` reading of the press.**
  #894 In 1 and its `plan.md` A–D hold the refusals; the owner's rule is to
  observe, not predict. This work reads the press through
  `automation_pressed` only.
- **`hooks/worktree_consent.py`, `hooks/commit-review-gate.py`,
  `hooks/cmdline_base.py`.** Byte-identical to the base (S12).
- **The attended choice site**: its two texts, its budget, its marker.
  Byte-identical (S3).
- **#896's own records** (`seal/specs/1791781864-…/spec.md` §*The class*,
  `questions.md` item 6, `rounds/`). Past states quoted for audit; the
  survivor sweep is told so in `survivors.md` where a quoted line of theirs
  stands.
- **The 0.21.1 run's own protection.** The installed guard runs from the
  plugin cache, so this change protects the run after this release.

## User scenarios & acceptance *(mandatory)*

S1, S2, S5–S10 are cases in a new file,
`tests/test_a_creation_in_another_clone_asks_nobody.py`, which imports
`ask_entries`, `write_transcript`, `IDLE`, `grant`, `consent_dir` and `wg`
from `tests/test_the_guard_asks_once_per_session.py` and `judge`,
`assert_names_nobody` and the `wko` and `projects` fixtures from
`tests/test_the_idle_session_rows_ask_nobody.py`, the way the latter already
imports from the former (`plan.md` E says why a new file). Each new case is
seen red at the base, `321e9de1`, and the handover says how. The other clone
is a `shutil.copytree` of the `repo` fixture, as
`test_a_switch_into_another_clone_names_no_split_it_cannot_consent` makes
it, and the creation is `git -C <other-top> worktree add ../wt feature/x`
issued from `repo`.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 under the press row 3 denies every attempt | Given session `me`'s `automation` press written for `repo` (`ask_entries(repo)`, `write_transcript`), the other clone's sessions stubbed `([], IDLE, True)` · When the creation above, three times · Then `deny` each time with one text: `origin`, the only-idle sentence, the idle line, the snippet, the press sentence, the other-clone sentence naming no way on, the re-issue sentence; no `AskUserQuestion`, no `[worktree-ok]`, no `[shared-tree-ok]`, no `worktree add` in the reason; `<other git-dir>/specseal-worktree-choice/create/` holds no `me`; neither clone's `specseal-worktree-consent/` holds `me`. Both languages | new case; red at the base (`deny` naming `AskUserQuestion`, then `ask`, `ask`) |
| S2 under the press row 4 denies every attempt | The same with sessions `([], [], False)` and the cannot-tell sentence | new case; red at the base |
| S3 without the press both rows are the base's | Given no press · When the creation, twice, in each of the two states · Then attempt 1 is `deny` with the `AskUserQuestion` instruction and attempt 2 is `ask`, each reason byte-identical to the base's, both languages | the existing cases stay (`tests/test_the_guard_asks_once_per_session.py::test_the_first_creation_is_still_a_question`, `tests/test_worktree_guard.py::test_worktree_add_user_tag_downgrades_to_ask_without_re_asking` and the creation-side `choose` cases); one new assertion compares against the base's text captured in the case, the way #896's S5 does |
| S4 in the press's own clone the rows are not reached | Given the press for `repo`, `repo`'s sessions idle or unusable · When `git worktree add ../wt feature/x` in `repo` · Then `allow` with the answer's text, as at the base; the compound `git worktree add ../wt feature/x && git status` is silent | the existing cases stay (`test_a_bare_creation_after_the_automation_answer_is_allowed`, `test_the_answer_outranks_every_row_below_it`); one assertion in S10 counts the rows' read not happening |
| S5 a record in the other clone outranks the rows | Given the press for `repo` and `grant(other)` · When the creation in `other`, idle state · Then `allow` with the record's text | new case; green at the base, which is the point — it pins that the rows are below row 0 |
| S6 `[worktree-ok]` under the press still reaches row 2 | Given the press for `repo`, `other` idle · When `git -C <other-top> worktree add ../wt feature/x  # [worktree-ok]` · Then `ask` with the token's text, as attended; the In 1 deny is not reached | new case; green at the base — it pins that the deny names no token and the token's row is above |
| S7 the press is read from the session's own root | Given the press written for a third clone only (`ask_entries(third)`), `other` idle · When the creation in `other` from `repo` · Then the attended first-attempt `deny` naming `AskUserQuestion`; and given the press written for `other` itself, `allow` (row 0, condition 4 holds) | new case, the shape of #896's S11; red at the base for neither half — it pins which root is read |
| S8 a creation inside a compound meets the same deny and records nothing | Given the press for `repo`, `other` idle · When `cd <other-top> && git worktree add ../wt feature/x` · Then `deny` with S1's text (the deny stops the whole line), and `specseal-worktree-consent/` in `other` holds no `me` after the `PostToolUse` writer is NOT run, because the command did not | new case; red at the base |
| S9 the deny leaves the switch rows' text alone | Given the press for `repo`, `other` idle · When `git -C <other-top> switch feature/x` · Then #896's other-clone deny, byte-identical (`test_a_switch_into_another_clone_names_no_split_it_cannot_consent` stays green) | the existing case; `git diff 321e9de1 -- hooks/worktree-guard.py` shows no hunk inside `unattended_text` |
| S10 the transcript is read at most twice per creation | Given a counting `worktree_consent.automation_answered` · When a bare creation in `repo` under the press (own clone), then the creation in `other` under the press in the idle state, then in the clean single-stream state, then attended in `other` idle · Then the counts are 1, 2, 1, 1 — `consent` once each, and the rows' read only where a row fires under the press | new case, the shape of #896's S10 |
| S11 on Windows a creation in another clone under the press is row 4's deny | Given the press for `repo`, nothing stubbed · When the creation in `other` · Then S2's deny; the case is marked to run on Windows only, like `test_on_windows_a_switch_under_the_press_is_row_twos_deny` | new case; M1 measures it at the pull request's Windows shards |
| S12 the other readers are unchanged | `hooks/worktree_consent.py`, `hooks/commit-review-gate.py`, `hooks/cmdline_base.py` byte-identical to `321e9de1` | `git diff 321e9de1 -- <the three>` empty; asserted by the handover |
| S13 `guard_worktree_creation` declares and leaves the census | Its docstring carries a `Reads:` line in the registry's grammar, and `tests/undeclared_readers.txt` no longer lists `hooks/worktree-guard.py#guard_worktree_creation` | `bin/test tests/test_a_reader_declares_its_input_class.py` green |
| S14 the policy says what the code does | `docs/worktree-guard-spec.md` §B rows 3 and 4 carry In 1; §*Creation consent* gains a paragraph *A creation in another clone under the press* with `Enforced by:` naming S1, S2, S5, S6, S7, S8, S10; §*Choice sites*' *Under the press* paragraph says the creation rows deny in another clone and its `Enforced by:` gains S1 and S2; §*Known limits*' Windows bullet gains the creation half; the module docstring's §B rows and its *Under the press* paragraph say the same in their words; `choose`'s docstring no longer says only the switch direction passes `pressed`; `README.md` and `README.ko.md`'s `worktree-guard` row gain one clause each, together | `bin/test tests/test_a_folded_statement_names_what_enforces_it.py tests/test_docs_line_wrap.py`; the survivor sweep at the pull request |
| S15 the fragments | `seal/specs/1791852612-…/changelog.md` says what a model sees differently and that a person sees nothing new; `seal/ledger/1791852612-….md` holds S1–S14's rows and the `Re-read ·` rows for every released row `guard_worktree_creation` and `choose` drift | `bin/evidence-check seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md`; the hygiene workflow at the pull request |

## Data & interfaces

- `hooks/worktree-guard.py#guard_worktree_creation`: rows 3 and 4 pass
  `pressed=automation_pressed(repo_paths(cwd)[0], session_id,
  transcript_path)` and `unattended=<the text>` to `choose`, each evaluated
  inside its own `if`, so a command reads the press at most once (S10). The
  signature is unchanged — `cwd` and `transcript_path` are already
  parameters. The docstring gains a `Reads:` line (S13).
- `hooks/worktree-guard.py#choose`: no code change; its docstring's last
  sentence changes (§*Removes*).
- Text: the press sentence and the re-issue sentence are #896's, byte for
  byte, in both languages; the other-clone sentence is new, one `tr(en, ko)`
  pair, in the register of `main`'s `unattended_text` other-clone branch.
  W1 decides where the two shared sentences live so one string serves both
  ladders.
- No new file, marker, environment variable, payload field or reader. No
  change to `hooks/hooks.json`.

## Rule changes

- nothing
  why: written: a creation in another clone under the press, in docs/worktree-guard-spec.md
    *B* and *Choice sites*.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence in `choose`'s docstring saying that only the switch direction passes `pressed`, because the creation direction reads consent before any of its rows | `hooks/worktree-guard.py#choose>"Only the switch direction passes it"` | replaced in the same docstring by a sentence saying both directions pass it, and that the creation direction reaches `choose` under the press only in a clone the press does not consent to (#903) |

### Why these rows

Two sentences this work extends are not removed, because each is true as
written and gains the other clone's half after it: the module docstring's
*In the clone the press was given in, the creation direction's two sites
never run under the press: consent is read first*, and
`docs/worktree-guard-spec.md` §*Choice sites*' *In the press's own clone the
creation direction's two sites never run under the press, because consent
is read before them*.

## Open questions → questions.md

P1 (a person); M1, M2 (a measurement); W1, W2 (the work). Each row says
which judgment it could not settle from the tree and who closes it. Under
this run's `automation` answer no row blocks the build: P1 is built on its
default.

Framed 2026-10-13 by framer, before the build.
