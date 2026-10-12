# Feature Specification: under automation, the guard asks nobody

<!-- seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Framed by `specseal:framer` on Fable 5.1 for #894. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | Between two designs that catch the same defect, the one that stops to ask a person is the more expensive. An `automation` run is the owner saying nobody is at the keyboard, so a yes/no prompt there is a defect whatever the guard read correctly |
| `docs/commit-review-gate-spec.md` §*Where the person said nobody would be answering, every stop is a deny* | The shape every stop takes under the press: a `deny` to the model whose reason names the ways on that need nobody, names no question tool, and says that re-issuing the command unchanged meets the same refusal. The dirty-tree row takes this shape (In 2) |
| `docs/worktree-guard-spec.md` §A, row *single stream, tracked changes present* | Today's row: `ask`, "genuinely yes/no". It stays the attended verdict. Under the press it is not yes/no, because the answer the owner would give — commit first — is not one of the two buttons (#21's table of four destinations) |
| `docs/worktree-guard-spec.md` §A, *The stop has two readers* | The unrecognised-shape stop already reads the press through `hooks/worktree_consent.py#automation_answered`, against the session's own clone. In 2 reads the same press through the same reader; nothing about what is read moves |
| `docs/worktree-guard-spec.md` §*Creation consent*, the table of five sources | What the model can and cannot forge. A `routing.md` reading `Automation \| yes` is the model's, with `Write`; the transcript's `AskUserQuestion` result is the harness's, from the click. *A `routing.md` is not read, not even as a fallback.* This is why In 1 names no new evidence: everything that survives a machine move is in the tree, and everything in the tree is the model's |
| `docs/worktree-guard-spec.md` §*Creation consent*, rule 1 *This session's own main transcript* | Where the press lives: `<PROJECTS_ROOT>/*/<session-id>.jsonl` on the machine the session ran on. A subagent reaches its parent's press through the parent's id. Nothing else is scanned, by decision |
| `docs/worktree-guard-spec.md` §*Choice sites*, *The test for whether a site qualifies* | *After declining, is there more than one command this session could issue?* The dirty row fails it attended (the three rows that stay `ask` or `deny`), and under the press the question is moot: the model gets the turn and the reason names the commands |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | A test seen red, a stated failure direction, a prompt budget, platform honesty. Each is answered below and in `plan.md` |
| `skills/agent-contract/SKILL.md` §12 | The class, not the coordinate. The ticket names two stops; the class is *every `ask` the guard can emit while the press is read*, enumerated in §*Scope* |
| `skills/agent-contract/SKILL.md` §13, §15 | The deny's ways on are run against the guard, not read off it (S4, S5); the new cases are seen red against the base |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | `seal/releases/0.20.0.md` row S6 claims the plain retry in a dirty tree is the tracked-changes `ask`, with the press written. This work changes that; the correction is a citing row in this item's fragment, never an edit of the released file |
| `skills/implement/orchestration.md` §*Orchestrator: how the work is routed — two questions, one call, one file* | The press is question 1 of this batch, put through `AskUserQuestion`. In 3 adds where it is put again |
| `skills/code-review/orchestration.md`, the paragraph beginning *When the implementing session no longer exists — a new day, another machine* | The one place a resumed run is described. In 3 hangs its sentence here |

## Scope

### What was measured (read from #894; verified against the code, not re-run)

On 2026-10-12, in the 0.21.0 run, the `smith` for #835 issued two commands in
its worktree and the owner was asked yes/no twice. Every `routing.md` of the
run reads `Automation | yes` / `Answer pressed | automation`.

| Stop | Command | Row that fired | Why it asked rather than denied |
|---|---|---|---|
| 1 | `git checkout -q 2fc65bea --` | `stop_unrecognised` (a `checkout` with nothing after `--`), `hooks/worktree-guard.py#main` | `automation_pressed` read False: the press was given in an earlier session on another machine, and on this machine the owner answered in typed text. `hooks/worktree_consent.py#automation_answered` reads only a harness-written `AskUserQuestion` result in this session's own main transcript |
| 2 | `git switch -q feat/835-…` with one modified tracked file, from the detached HEAD stop 1's approval left | the tracked-changes row, `hooks/worktree-guard.py#main` (the `if entries:` block) | the row reads no press at all. `automation_pressed` is called once in `main`, for `stop_unrecognised`; the dirty row answers `ask` whoever is at the keyboard |

The ticket's third question — whether `hooks/commit-review-gate.py#automation_pressed`
has the same cross-session gap — is answered **yes, by construction**: it is a
wrapper around the same `automation_answered`, with the same four conditions
(its docstring and `docs/commit-review-gate-spec.md` §*Where the person said
nobody would be answering* say so). It is in scope only through In 3, which is
the one fix both share. No line of the gate changes (S8). Where this plugin's
git hooks run, a commit stop is git's exit status and stderr text printed into
the command's output, which the model reads whoever pressed what
(`docs/the-commit-gate-inside-git.md`, *A git hook cannot render two buttons*);
the press there decides only whether the text names a question tool.

### In 1 — where the press is read from once the session is gone: nowhere new, and said plainly

**No evidence exists that both survives a machine move and the model cannot
forge, and this work adds none.** The argument is the Grounding table's:

- The press the harness writes is in `~/.claude/projects/<slug>/<session>.jsonl`.
  A new machine has none of those files.
- The consent record and the choice markers are under the git common
  directory, which does not travel either (`agents/framer.md` makes the same
  point about the framer mark: *a git dir does not travel, so CI cannot see
  it*).
- Everything that does travel is in the tree, and the model writes the tree.
  `routing.md` is the measured case: it said `automation` on every item of
  the run, and it is exactly the file §*Creation consent* refuses to read.

So after a machine move the honest state is **no press on this machine**, and
an `ask` is the guard's correct answer to that state. The reader is not
changed, loosened, or given a fallback. `plan.md` §*Alternatives considered*
holds the three designs that were weighed and why each is refused (A, B, C).

### In 2 — the dirty-tree row under the press is a deny to the model

Where `automation_answered` is True for the session's own clone, the
tracked-changes row of §A answers `deny` instead of `ask`. The reason:

- lists the changes as today (file list, index-only residue note, the three
  leads of #624.2 unchanged in wording);
- names the ways on that need nobody, each **as a command of its own**,
  because the guard reads the tree before the command runs and a compound
  `git stash && git switch x` meets the same deny (S5):
  1. commit the changes here first — on a declared branch the commit gate is
     silent for it, and a feature branch squashes at the merge, so an
     intermediate commit costs nothing (#21, *committing first is close to
     free*);
  2. `git stash`, then the switch, then `git stash pop` — and says that `pop`
     applies to whatever is checked out when it runs (#21, executed);
  3. says which applies when HEAD is detached, because stop 2 ran from a
     detached HEAD and a commit there is on no branch (W1 decides whether the
     guard reads HEAD's state or tells the model the one-line check);
- names no question tool, and says that re-issuing the command unchanged
  meets the same refusal (the commit gate's shape).

Without the press the row is byte-for-byte today's `ask` (S2). `[shared-tree-ok]`
stays ignored at this row in both readers: it answers a different question
(§*Choice sites*). Carrying the changes along, the one destination approving
used to give, is reachable under the press through the stash sequence, so no
spelling is lost.

**Failure direction.** Blocks more, never allows more: a verdict moves from
`ask` to `deny` in one state and nowhere else. A wrong deny — a press read
where the owner had taken it back — costs the model a turn; the reader that
decides it is unchanged, so this work can produce no such reading that today's
unrecognised-shape stop does not already produce. **Prompt budget.** Under the
press the dirty row puts zero questions to a person, from one per dirty switch.
Attended, unchanged. In 3 adds one click at a resume, at a moment a person is
present by definition.

### In 3 — a resumed run presses again, through the tool

`skills/implement/orchestration.md` §*Orchestrator: how the work is routed*
gains one paragraph, and `skills/code-review/orchestration.md`'s *When the
implementing session no longer exists* paragraph a sentence linking to it:

> A run resumed in a new session — a new day, a `/clear`, another machine —
> puts question 1 through `AskUserQuestion` again before the first spawn, in
> the same call as whatever else the resume has to ask. A typed answer is not
> the press: the readers accept a harness-written result and nothing else,
> and `routing.md` is not read. Measured: 0.21.0 resumed on another machine
> with the answer given as text, and the worktree guard asked the owner twice
> in a run routed `automation` on every item (#894).

This is the recorded-fact design the owner's standing judgment asks for: the
fact is recorded again where the one reader already reads it, and nothing is
predicted. It costs one click, at a moment when a person is present (they
typed the resume). It fixes stop 1 and the commit gate's gap with one
sentence, and it is why neither reader changes.

### The class (`agent-contract` §12)

Every `ask` the guard can emit while the press is readable, enumerated from
`hooks/worktree-guard.py#main`:

| Site | Under the press today | This work |
|---|---|---|
| unrecognised shape, tree matters (`stop_unrecognised`) | `deny` (#826) | unchanged; its plain retry now meets In 2 instead of an `ask` (S6) |
| §A tracked-changes row | `ask` | **`deny`** (In 2) |
| §A rows 1-b and 2, the two `choose` sites | first attempt `deny` whose text says to call `AskUserQuestion`; every attempt after `ask` | **out of scope**, `questions.md` P1. Same class, different answer: what needs nobody there is a product decision |
| §B creation rows | unreachable: consent is read first and the press is consent | unchanged |
| Agent/Task path | silent under consent | unchanged |

### Out of scope, each with why

- **A cross-session or cross-machine reading of the press.** In 1 says none
  exists that the model cannot forge; `plan.md` A and B say why the two
  same-machine designs are refused; `questions.md` P2 lets the owner overturn
  A.
- **The two `choose` rows under the press.** P1. Not measured in #894, and the
  way on that needs nobody (split into a worktree? press `[shared-tree-ok]` on
  the model's own judgment?) is the owner's to name.
- **#21, the attended dirty-tree choice site.** It changes the prompt a person
  sees and spends the switch direction's budget. In 2's text reuses its table
  of destinations, so a later #21 inherits the words.
- **#20, a declaration for the guard's answer.** A different question (*is
  another session working here?*) with a different lifetime.
- **Any change to `hooks/commit-review-gate.py`, `hooks/worktree_consent.py`
  or `hooks/cmdline_base.py`.** S8 pins the first two byte-identical to the
  base; the third is frozen (#689).
- **`templates/claude-md-block.md` and `CLAUDE.md`.** The rule's home is
  `orchestration.md` (`1791076836`: every rule `CLAUDE.md` restates has one
  home); a link row is the orchestrator's call, not this build's.
- **Windows.** Every switch there takes the detection-unusable row, which is
  P1's site, not this work's. Read, not run (§*Known limits*).

## User scenarios & acceptance *(mandatory)*

Each S-row is a case in `tests/test_the_guard_asks_once_per_session.py` or
`tests/test_worktree_guard.py` unless it says otherwise; each new case is seen
red against the base (`c38f97d7`) and the handover says how.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the dirty row under the press is a deny | Given session `me`'s `automation` press in its transcript (`ask_entries`), a single-stream tree with one modified tracked file · When `git switch feature/x` · Then `deny`; the reason lists `f.txt`, names committing here first and `git stash` / `git stash pop` each as a command of its own, says `pop` applies to whatever is checked out, says re-issuing unchanged meets the same refusal, and does not contain `AskUserQuestion`. Both languages (`SPECSEAL_LANG=ko`) | new case; red at the base (`ask`) |
| S2 without the press the row is today's ask | Given no press · When the same command in the same tree, in each of the three states of `test_the_dirty_tree_row_names_what_was_measured` · Then the reason is byte-identical to the base's | the existing case stays; one new assertion compares against the base's text captured in the case |
| S3 the token does not reach the row under the press either | Given the press, only-idle sessions or detection unusable, a dirty tree · When `git switch other  # [shared-tree-ok]` · Then `deny`, lead `[shared-tree-ok] carries the user's answer…`, the rest S1's text | new case; red at the base (`ask`) |
| S4 the ways on pass the guard | Given the press and a dirty tree · When `git commit -am x` then `git switch feature/x` as two issues; and `git stash`, `git switch feature/x`, `git stash pop` as three · Then every issue but none is silent, and the tree ends on `feature/x` with the change where the way on said it would be | new case, real git in the fixture repository, the guard run per issue (`decide`) and git run between them |
| S5 a compound stash-and-switch meets the deny, not a loop | Given the press and a dirty tree · When `git stash && git switch feature/x` · Then `deny` with S1's text, which says to run them as commands of their own | new case; red at the base (`ask`) |
| S6 the plain retry after an unrecognised-shape stop meets In 2 | Given the press and a dirty tree · When `git checkout feature/x` then `git switch feature/x` · Then `deny` with the stop's text, then `deny` with S1's text; in an ACTIVE tree both are the deny with the worktree steer, as today | `test_the_plain_retry_meets_todays_rows` rewritten; its 0.20.0 ledger row S6 takes a `Corrected ·` citing row in this item's fragment |
| S7 a creation on the same line is stopped with it and records nothing | Given the press, no consent record, a dirty tree · When `git switch feature/x && git worktree add ../wt f` · Then `deny`, and `specseal-worktree-consent/` holds no file for `me` | new case; the PostToolUse writer is not run because the command did not |
| S8 the other readers are unchanged | `hooks/commit-review-gate.py`, `hooks/worktree_consent.py` and `hooks/cmdline_base.py` are byte-identical to `c38f97d7`'s | `git diff c38f97d7 -- <the three>` is empty; read at review and asserted by the handover |
| S9 the policy says what the code does | `docs/worktree-guard-spec.md` §A's tracked-changes row and *The stop has two readers* carry In 2 with `Enforced by:` lines naming S1, S3, S5, S6; §*Known limits* carries In 1 (the press is this session's, on this machine; a resumed run presses again); the module docstring's row says the same in its words | the `Enforced by:` resolver (`tests/test_a_folded_statement_names_what_enforces_it.py`), `tests/test_docs_line_wrap.py`, the survivor sweep |
| S10 the orchestrator's procedure carries In 3 | `skills/implement/orchestration.md` holds the paragraph; `skills/code-review/orchestration.md` links it from the *another machine* paragraph; `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` stays green (the section is the orchestrator's and already marked) | read at review; the two tests named |
| S11 the fragments | `seal/specs/1791779434-…/changelog.md` says what a person sees differently; `seal/ledger/1791779434-….md` holds S1–S10's rows and the S6 correction | `bin/evidence-check` on the fragment; the hygiene workflow at the pull request |

## Data & interfaces

- `hooks/worktree-guard.py#main`: the `if entries:` block reads
  `automation_pressed(repo_paths(cwd)[0], session_id, transcript_path)` —
  the session's own root, as `stop_unrecognised`'s call does — and answers
  `deny` where True. W2 decides whether the read is cached beside `seen` so a
  command holding an unrecognised shape and a switch scans the transcript
  once.
- No new file, marker, environment variable, or payload field. No change to
  `hooks/hooks.json`.
- Text: one new `tr(en, ko)` pair for the deny's ways on; the three leads of
  #624.2 keep their words.

## Open questions → questions.md

P1, P2 (a person); M1–M3 (a measurement); W1, W2 (the work). Each row says
which judgment it could not settle from the tree and who closes it.

Framed 2026-10-12 by framer, before the build.
