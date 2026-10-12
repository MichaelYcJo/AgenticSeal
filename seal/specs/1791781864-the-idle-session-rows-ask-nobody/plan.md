# Implementation Plan: the idle-session rows ask nobody

<!-- seal/specs/1791781864-the-idle-session-rows-ask-nobody/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. Framed by `specseal:framer` on Fable 5.1 for #896. -->

Approved 2026-10-12 by the repository owner, when `smith` was spawned.

## Summary

Two defects at one row, fixed in two units that do not touch each other.

- **The line** (`spec.md` In 1): `fmt_sessions` prints `<kind> <age>` for an
  unidentified session and nothing after it. One function, six sites, no
  verdict moves.
- **The rows under the press** (`spec.md` In 2): `choose` takes a `pressed`
  flag, and where it is set the site denies on every attempt with a reason
  naming the worktree split as the way on — no question tool, no token, no
  choice marker. `main` sets the flag at its two switch-direction `choose`
  calls, reading the press through the reader the stop already uses, lazily,
  so the transcript is read at most once per command.

The design reads a recorded fact — the harness-written `automation` answer
in this session's own transcript — and predicts nothing. No reader, fallback
or payload shape is added. The press reader and the commit gate are
byte-identical to the base after this work (S12).

#894 lands first. This branch then merges `origin/release/v0.21.0` in with a
merge commit, never a rebase, and only after that edits the documents the two
items share (§*Seams*, phase 3). Phases 1 and 2 touch nothing #894 touches
and can be built before it lands.

## Technical context

- `hooks/worktree-guard.py#fmt_sessions`: the `p is None` branch builds
  `kind` from whether `d` holds `[lease:`, prints `_age(tr_idle)`, and
  appends the clause. `tr_idle` is the lease's age in minutes
  (`fresh_leases`) or the transcript idle time (`sessions_in_tree`'s
  unattached-activity arm). Six callers: `guard_worktree_creation` (two),
  `stop_unrecognised` (two), `main` (two). No existing case drives the
  branch: `test_switch_idle_sessions_offer_both_ways_on` uses `IDLE`, a pid
  entry, and asserts *terminal in/out*.
- `hooks/worktree-guard.py#choose`: `deny` once per session per direction
  through `already_asked`, `ask` after, `before_ask` on the fallback path.
  Called four times: the switch ladder's rows 1-b and 2 (scope `switch`),
  and the creation ladder's only-idle and unusable rows (scope `create`).
  The creation ladder reads consent — the record or the press — before any
  of its rows, so its two calls never run under the press.
- `hooks/worktree-guard.py#main`: the token (`shared_ok`) is read before the
  rows; row 1-b is `if idle and not shared_ok`, row 2 `if not reliable and
  not shared_ok`; `steer` and `switch_or_split` are built above them, and
  `judge_the_creation` is handed in as `before_ask`. `automation_pressed` is
  called once today, at the `stop_unrecognised` call, and #894 adds a second
  call inside the `if entries:` block, which is reached only where neither
  choice row fired. Under the token the rows are skipped and the dirty row's
  read is the only one.
- `hooks/worktree-guard.py#automation_pressed`: the wrapper around
  `hooks/worktree_consent.py#automation_answered`, read against the
  session's own root. Unchanged. `tests/conftest.py#_no_real_transcripts`
  points `PROJECTS_ROOT` at an empty directory in every case; a case plants
  a press with `ask_entries` and `write_transcript` under the `projects`
  fixture, as `tests/test_worktree_guard.py#pressed_root` does.
- `hooks/worktree-guard.py#already_asked`: the marker
  `<git-dir>/specseal-worktree-choice/<scope>/<session>`. Under the press
  `choose` returns before reaching it, so nothing is written (S3).
- Ledger rows this work drifts: `seal/releases/0.9.1.md`'s row on
  `hooks/worktree-guard.py#choose`, stamped `ed62dd1a`, and the `main@…` families in
  `0.15.6`, `0.18.3` and `0.20.0` and the unreleased fragments under
  `seal/ledger/` that cite `main@08a308fb`. #894 drifts `main` first and
  writes its own `Re-read ·` rows; this item writes its own in its fragment
  with `bin/evidence-check --reverify --into seal/ledger/1791781864-….md
  --checked <date>` after the merge of phase 3.
- Fixture: `repo` in `tests/conftest.py` is a `git init` with `f.txt`; no
  `origin` remote. S7's creation therefore uses `-b feature/x` without
  `origin/main` unless W3 adds a remote.
- Language: `seal/config.md` has no `Record language` row, so the records
  are English; the guard's text is `tr(en, ko)` and both halves are pinned.
- Test runner: `bin/test <files>`.

**The failure scenario of the chosen approach, six months out.** An
automation run on Windows, where every switch is row 2, meets this deny on a
`git switch` the model issues inside the worktree it just created — detection
is unusable there too — and the model, reading *split into a worktree*,
creates a second worktree for a branch it already has. The deny's text is the
bound: it names `git worktree add … -b <branch>` as the way to *start* a
branch and says a worktree already on the branch needs no switch. Whether
that sentence holds is M1's measurement; if it does not, P1 (c) and a
Windows-specific reading of row 2 are the next frame, and this one has cost
one extra worktree per occurrence, never a prompt.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A. The line says *last seen <age>*** | `<kind> <age>` already names the measurement — *lease declaration 4.7h ago* — and a second phrase for the same number reads as a third signal beside the terminal and transcript ages the pid branch prints | **refused** (In 1) |
| **B. Drop the clause only for entries in the idle list** (a flag on `fmt_sessions`) | The function would then carry a judgment the header already carries, and the active list's clause is the same unmeasured claim one window younger. Two texts for one line, and the measured defect returns the day a caller passes the wrong flag | **refused** |
| **C. Under the press the two rows allow silently**, the press read as `[shared-tree-ok]` | Allows more. The press says nobody is at the keyboard, not that the idle session is a forgotten tab; a wrong allow moves another session's branch under it, which is the asymmetry §*Unknowns resolve conservatively* is built on | **refused** |
| **D. The deny names `[shared-tree-ok]` too**, leaving the judgment to the model | Pressing the token on the model's own judgment is the call the row exists to hand a person (§*Choice sites*: nothing verifies who put it there). The deny would then be a longer way of allowing | **P1 (c)**; the frame is built on (b) |
| **E. Under the press the token is not read at these rows** | Blocks more, and it is new mechanism the ticket did not ask for: a token the model appends is already recorded on the command line, which is the standing `[worktree-ok]` and `[no-review]` have. Adding it costs a reader clause and a case nobody measured a need for | **P2 (b)**; the frame is built on (a) |
| **F. Row 2 under the press allows while row 1-b denies**, on the ground that nothing was counted | A wrong allow in the one environment nobody can read is the worst case, and on Windows it would make every switch silent under the press | **refused** |
| **G. The press is read at the call sites in `main`**, which respond `deny` themselves before calling `choose` | Two copies of the deny's shape beside a function whose docstring owns *deny once, ask after*; the next choice site copies one of them. Reading the flag inside `choose` keeps the three verdicts of a site in one place | **refused**; the flag goes to `choose` |
| **H. The new cases are appended to `tests/test_the_guard_asks_once_per_session.py`** | #894 appended 240 lines at that file's end; two appends at one end are a conflict at the merge, after the review rounds. A new file imports the same fixtures and conflicts with nothing | **refused**; a new file |
| **I. The line prints `<kind> <age>`; the two rows deny every attempt under the press naming the split and no token; `choose` carries the flag** | A model that follows neither the split nor the re-issue sentence loops on the deny. The bound is the reason's text, as the commit gate's is; M1 owes the measurement | **chosen** (In 1, In 2) |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The line** (In 1): `fmt_sessions`'s unidentified branch prints `<kind> <age>` in both languages, its docstring says why the clause is gone; S1 and S2 as cases in `tests/test_worktree_guard.py` beside `test_switch_idle_sessions_offer_both_ways_on`, seen red at `c38f97d7` | `bin/test tests/test_worktree_guard.py tests/test_worktree_guard_signals.py` green; the handover names how S1 and S2 were shown red | 17d7ed5f |
| 2 | **The rows under the press** (In 2): `choose` takes `pressed` and the way-on text and denies before the marker where it is set; `main` passes it at rows 1-b and 2, read lazily (W2), with W1's text in both languages; `tests/test_the_idle_session_rows_ask_nobody.py` holds S3, S4, S6–S11, each new case seen red at `c38f97d7`; S5's assertion added to the three existing cases; S12 checked | `bin/test tests/test_the_idle_session_rows_ask_nobody.py tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py` green; `git diff c38f97d7 -- hooks/worktree_consent.py hooks/commit-review-gate.py hooks/cmdline_base.py` empty | abe3dc3e |
| 3 | **After #894 is on `origin/release/v0.21.0`**: `git -C <wt> merge origin/release/v0.21.0` (a merge commit; the plan's Status column is re-read after it); then the documents and fragments (S13, S14): the module docstring's rows 1-b and 2 and its CHOICE paragraph; `docs/worktree-guard-spec.md` §A rows 1-b and 2, *The stop has two readers*, §*Choice sites* *Under the press* with `Enforced by:`, §*What a blocking prompt must show*, §*Known limits* (replace #894's sentence; the Windows bullet's press consequence); `README.md` and `README.ko.md` one clause each; `seal/ledger/1791781864-….md` with S1–S13's rows and the `Re-read ·` rows `--reverify --into` writes; `changelog.md` | `bin/test tests/test_a_folded_statement_names_what_enforces_it.py tests/test_docs_line_wrap.py` green; `bin/evidence-check seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md` clean; the survivor sweep at the pull request | e905b5a5 |

Three phases, not two: the documents the two items share cannot be edited
until #894's text is in this branch, and the code they describe can.
Phases 1 and 2 are independent of each other and of #894.

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
**Re-read the column after any rebase**, or it names commits that resolve in
one clone and nowhere else. The evidence ledger has no such problem: a ledger
row names a symbol and a content hash, so there is no commit in it for a
rebase to orphan.

## Seams

Every spot both items write, read from #894's branch at `52b0b122` and its
`plan.md` phase 2. #894 lands first; this branch merges the release branch in
afterwards, never by rebase, and edits the shared documents only after that
merge (phase 3).

| Spot | #894 writes | This item writes | Expected at the merge |
|---|---|---|---|
| `hooks/worktree-guard.py`, module docstring §A rows | the dirty row (three lines, phase 1, landed) | rows 1-b and 2 (the two lines above it) and the CHOICE paragraph | adjacent lines: **conflict**, resolved by keeping both. Deferred to phase 3 so it is edited on the merged text |
| `hooks/worktree-guard.py#main` | the `if entries:` block, after `lead` (landed) | the two `choose` calls of the switch ladder, about 150 lines above | separate hunks, no conflict expected |
| `hooks/worktree-guard.py#choose`, `#fmt_sessions` | nothing | the flag and the way-on text; the line | none |
| `docs/worktree-guard-spec.md` §A table | the tracked-changes row | rows 1-b and 2 | adjacent rows: **conflict**; phase 3 |
| `docs/worktree-guard-spec.md` §A, *The stop has two readers* | In 2's sentence about the dirty row | one sentence: the plain retry meets In 2 in the idle and unusable states | same paragraph: **conflict**; phase 3 |
| `docs/worktree-guard-spec.md` §*Known limits* | a bullet naming this item's two rows as out of scope | replaces that bullet's sentence with In 2's, and adds the press consequence to the Windows bullet | this item edits #894's text: phase 3 only |
| `docs/worktree-guard-spec.md` §*Choice sites*, §*What a blocking prompt must show* | nothing | a paragraph; a sentence | none |
| `skills/implement/orchestration.md`, `skills/code-review/orchestration.md` | In 3's paragraph and link | nothing | none |
| `tests/test_the_guard_asks_once_per_session.py` | `test_the_plain_retry_meets_todays_rows` rewritten; 240 lines appended | nothing (H) | none |
| `tests/test_worktree_guard.py` | an assertion and two constants after `test_the_dirty_tree_row_names_what_was_measured` (about line 1054) | S1, S2 beside `test_switch_idle_sessions_offer_both_ways_on` (about line 145); S5's assertion in three cases between lines 145 and 510 | separate hunks, no conflict expected |
| `tests/test_the_idle_session_rows_ask_nobody.py` | nothing | the file | none |
| `README.md`, `README.ko.md` | nothing | one clause each | none |
| `seal/ledger/<id>.md`, `seal/specs/<id>/changelog.md` | its own | its own | none; both write `Re-read ·` rows for the same released `main@…` families, which the checker reads as a family and tolerates |

## Operational impact

- No migration, no new file under the git directory, no new environment
  variable, no change to `hooks/hooks.json`.
- **What a person sees differently.** Attended, the per-session line under an
  idle header no longer claims the session is working right now; it shows the
  kind of evidence and its age. Nothing else attended moves.
- **What a model sees differently under the press.** A `git switch` in a
  tree holding only idle sessions, or in an environment whose processes
  cannot be read, is refused on every attempt with the worktree split named
  as the way on. **On Windows that is every `git switch`**, in a shared tree
  and in a linked worktree alike; the way on is a worktree per branch,
  created with `-b`, which under the press needs no confirmation. Read from
  the code, not run on Windows.
- **Compatibility.** The installed guard runs from the plugin cache, so the
  0.21.0 run itself is still guarded by 0.20.0's copy; the change protects
  the run after this one. Nothing here depends on another 0.21.0 item except
  #894's text in the three shared documents (§*Seams*).
