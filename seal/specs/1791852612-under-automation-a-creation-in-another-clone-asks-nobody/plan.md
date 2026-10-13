# Implementation Plan: under automation, a creation in another clone asks nobody

<!-- seal/specs/1791852612-under-automation-a-creation-in-another-clone-asks-nobody/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. Framed by `specseal:framer` on Fable 5.1 for #903. -->

Approved 2026-10-13 by the orchestrating session, under the owner's `automation` answer, when `smith` was spawned.

## Summary

One defect at two rows, fixed in one unit, with the documents after it.

- **The rows under the press** (`spec.md` In 1): `guard_worktree_creation`'s
  rows 3 and 4 pass `choose` the `pressed` flag and the unattended text that
  `choose` already takes since #896. Where the press is read from the
  session's own root, each row denies on every attempt with its situation,
  the press sentence, a sentence saying why no way on is named — the press
  consents to a creation only in the clone it was given in, this tree is in
  another, and nobody is at the keyboard to choose — and the re-issue
  sentence. No question tool, no token, no marker, no record.
- **Where it is reachable.** Only for a creation in a clone the press does
  not consent to and this session holds no record in: row 0 answers every
  other creation first. So in the press's own clone nothing moves, and the
  attended path is byte-identical.

The design reads a recorded fact — the harness-written `automation` answer
in this session's own transcript — through the reader the switch rows and
the stop already use, and adds no reader, fallback or payload shape. The
press reader and the commit gate are byte-identical to the base after this
work (S12).

## Technical context

- `hooks/worktree-guard.py#guard_worktree_creation` (line 1560 at
  `321e9de1`): row 0 reads `worktree_consent.consent(top, session_id,
  transcript_path)` — the record first, then the press for `top`'s clone —
  and returns `allow`/`silent` where it holds. Rows 3 and 4 call
  `choose(top, session_id, "create", situation, question, create_or_switch,
  fallback)` with no `pressed`. `cwd` is the session's shell directory:
  `main`'s call says *`cwd`, not the creation's directory*, so
  `repo_paths(cwd)[0]` is the session's own root, the argument
  `automation_pressed` takes at the switch rows (`main`, lines 3289 and
  3335) and at the stop (line 3028). `transcript_path` is already a
  parameter. The unit is on `tests/undeclared_readers.txt` and declares as
  it changes (S13).
- `hooks/worktree-guard.py#choose` (line 1466): `pressed=False,
  unattended=""`; where `pressed`, it responds `deny` with `situation` plus
  `unattended` before `already_asked`, so no marker is written. Its
  docstring's last sentence says only the switch direction passes it
  (`spec.md` §*Removes*). No code change.
- `hooks/worktree-guard.py#main`, the `press` and `reissue` strings (lines
  3136–3147) and `unattended_text` (line 3149): the two sentences In 1
  reuses are locals of `main`. W1 decides whether they move to module level
  so both ladders read one string, which changes `main`'s hash and nothing
  it does, or whether `guard_worktree_creation` carries a second copy with
  a comment naming the first. The frame's default is to move them: one
  sentence in two places is how the next reword drifts one of them, and
  `main` is re-read by this work's `Re-read ·` rows either way.
- `hooks/worktree-guard.py#automation_pressed` (line 2511): unchanged. The
  wrapper around `worktree_consent.automation_answered`, every failure
  False.
- `hooks/worktree_consent.py#automation_answered` condition 4 and
  `#granted`: unchanged; they are why rows 3 and 4 are reachable under the
  press at all.
- Tests: `tests/test_the_idle_session_rows_ask_nobody.py` holds `judge`
  (stubs `sessions_in_tree` and `load_input`, returns decision and
  reason), `assert_names_nobody`, `no_marker` (switch scope; the new file
  needs a `create` one), `elsewhere` (the switch rows' other-clone text),
  the `projects` and `wko` fixtures, and the other-clone shape
  (`shutil.copytree(repo, other)`, `git -C <top> …`).
  `tests/test_the_guard_asks_once_per_session.py` holds `ask_entries`,
  `write_transcript`, `grant`, `consent_dir`, `IDLE`, `wg`, and
  `test_an_answer_given_in_another_clone_is_not_consent`.
  `tests/conftest.py#_no_real_transcripts` points `PROJECTS_ROOT` at an
  empty directory in every case.
- Fixture: `repo` in `tests/conftest.py` is a `git init` with `f.txt` and a
  `feature/x` branch; the copied clone has the same branch, so
  `worktree add ../wt feature/x` is a creation of an existing branch and
  needs no remote.
- Ledger rows this work drifts: `hooks/worktree-guard.py#guard_worktree_creation`, at
  its `321e9de1` hash, in `seal/releases/0.9.1.md` (two rows), `0.9.4.md` (two), `0.15.5.md`,
  `0.15.6.md`, `0.20.0.md`; `#choose@ed62dd1a` in `0.9.1.md` and
  `#choose@108262db` in `0.21.0.md`; and under W1's default the `main@…`
  families in `0.9.1.md`, `0.15.6.md`, `0.18.3.md`, `0.20.0.md` and
  `0.21.0.md`. Written with `bin/evidence-check --reverify --into
  seal/ledger/1791852612-….md --checked <date>` in phase 2.
- Language: `seal/config.md` has no `Record language` row, so the records
  are English; the guard's text is `tr(en, ko)` and both halves are pinned.
- Test runner: `bin/test <files>`. Base: `321e9de1`
  (`origin/release/v0.21.1`).

**The failure scenario of the chosen approach, six months out.** An
automation run whose orchestrator works across two clones of one repository
— a layout nothing in this repository's own runs has, which use one clone
and linked worktrees — meets this deny on every creation in the second
clone, and the model, told to leave the tree to a session working in that
clone, has none to hand it to. The bound is the reason's text, as #896's is:
it says what the press consents to and why, so the model's one move is to
work in the clone the press was given in. If a measured run shows a model
looping on it instead, M2 is where the count arrives and `plan.md` C is the
next frame: naming the session's own clone as the place to split, which
this frame refuses because the guard cannot tell whether two clones hold
one repository.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A. Leave the rows; the switch deny's red-1 fix already stops the steer** | The rows still put the creation to a person under the press whenever a model reaches another clone by any other route — a prompt in the session's own instructions, a `cd` it was told to make. The owner decided the rows, not the steer | **refused**; it is the decision this frame carries out |
| **B. Deny every attempt and name no way on** (the switch deny's other-clone sentence, applied to the creation) | A model with no way on may loop; the bound is the reason's text, and M2 measures it | **chosen** (In 1) |
| **C. Deny and name the session's own clone as the place to split** (`git worktree add <own wt_root>/<name> -b <branch> origin/main`) | The guard reads two common git directories and nothing about whether they hold one repository; a worktree of the wrong repository, created on the guard's say-so, is a worktree nobody asked for — the six-months failure #896's plan named, one clone over | **refused**; the lever if M2 shows looping |
| **D. Read the press as consent in every clone** (drop condition 4, or read `automation_pressed` at row 0) | Allows more: the answer was given about one clone's work item, and consent everywhere is the reading §*Creation consent* rule 4 refuses. It is also the opposite of what the owner decided | **refused** |
| **E. Append the cases to `tests/test_the_idle_session_rows_ask_nobody.py`** | #896 appended at that file's end on a branch already merged; this branch appending there meets no conflict today, but the file's name says switch rows and a reader of a creation case would look elsewhere. A new file imports the same helpers and names its own subject | **refused**; a new file |
| **F. Also deny row 1 (ACTIVE) under the press in another clone** | Outside the owner's decision, which named the two choice rows; a frame widening a policy change is the frame deciding for the owner | **P1 (b)**; the frame is built on (a), unchanged |
| **G. Compose the deny inside `guard_worktree_creation` from a second copy of the press and re-issue sentences** | Two copies of one sentence, and the next reword moves one | **W1 (b)**; the default is (a), module-level |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The rows under the press** (In 1): `guard_worktree_creation` rows 3 and 4 pass `pressed` and the unattended text to `choose`, read lazily inside each row's `if`; the other-clone sentence in both languages, the press and re-issue sentences shared per W1; `choose`'s docstring sentence replaced (§*Removes*); a `Reads:` line on `guard_worktree_creation` and its census line removed (S13); `tests/test_a_creation_in_another_clone_asks_nobody.py` with S1, S2, S5–S8, S10 and the Windows-only S11, each new case seen red at `321e9de1` where the scenario says red; S3's assertion beside the existing creation cases; S9 and S12 checked | `bin/test tests/test_a_creation_in_another_clone_asks_nobody.py tests/test_the_idle_session_rows_ask_nobody.py tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py tests/test_a_reader_declares_its_input_class.py` green; `git diff 321e9de1 -- hooks/worktree_consent.py hooks/commit-review-gate.py hooks/cmdline_base.py` empty; the handover names how each red case was shown red | 7fd83e55 |
| 2 | **The documents and fragments** (S14, S15): the module docstring's §B rows 3 and 4 and its *Under the press* paragraph; `docs/worktree-guard-spec.md` §B rows 3 and 4, §*Creation consent*'s new paragraph with `Enforced by:`, §*Choice sites*' *Under the press* sentence and `Enforced by:`, §*Known limits*' Windows bullet; `README.md` and `README.ko.md` one clause each; `survivors.md` where a quoted line of #896's records stands; `seal/ledger/1791852612-….md` with S1–S14's rows and the `Re-read ·` rows `--reverify --into` writes; `changelog.md` | `bin/test tests/test_a_folded_statement_names_what_enforces_it.py tests/test_docs_line_wrap.py` green; `bin/evidence-check seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md` clean; the survivor sweep at the pull request | 08da0870 |

Two phases, not one: the code and its cases stand on their own and are
what the review's stage 1 reads first; the documents describe them and are
written against the text phase 1 settled (W1).

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

The 0.21.1 milestone's other open items are #911 (the routing question's
boxes, `skills/implement/orchestration.md`), #905 (four `Reads:` lines in
the evidence checker), #908, #874, #873, #872, #871 and #844. None touches
`hooks/worktree-guard.py`, `docs/worktree-guard-spec.md` or the two README
rows, read from their titles only. Two files more than one item may write:

| Spot | Another item writes | This item writes | Expected at the merge |
|---|---|---|---|
| `tests/undeclared_readers.txt` | any item that declares a unit removes its line | the `guard_worktree_creation` line | a deletion each in a sorted file: no conflict unless adjacent |
| `seal/releases/*.md` `Re-read ·` families on `main@…` | #905 may re-read checker rows; none on the guard | this item's fragment | none; a family read twice is tolerated by the checker |

## Operational impact

- No migration, no new file under the git directory, no new environment
  variable, no change to `hooks/hooks.json`.
- **What a person sees differently.** Nothing. Attended, both creation
  rows are what they were, word for word.
- **What a model sees differently under the press.** A Bash `git worktree
  add` in a clone other than the one the press was given in, where this
  session has created no worktree and the tree holds only idle sessions or
  cannot be read, is refused on every attempt with no way on named, instead
  of a deny asking it to put two options to a person and an `ask` after. In
  the press's own clone, nothing. **On Windows**, where every creation
  reads *detection unusable*, that is every creation in another clone;
  read from the code, measured by S11.
- **Compatibility.** The installed guard runs from the plugin cache, so the
  0.21.1 run itself is still guarded by 0.21.0's copy; the change protects
  the run after this one. Nothing here depends on another 0.21.1 item.
