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
| `docs/the-commit-gate-inside-git.md` §*The convergence argument is claimed for commits alone* | *Those arms still predict from text, and do not converge.* The owner's standing judgment on a reader that says what git will do: it is kept only where pinned not to grow. The reframe after round 3 applies it to the deny's own sentences — a recipe per switch form is a prediction from text, and three rounds measured it not converging (§*Why the deny predicts nothing*) |
| `docs/worktree-guard-spec.md` §*Known limits*, the brace-reader paragraph | The precedent: a reader built in work item 1791384157 and taken out in the same release, because *every reading of it imitated bash, and five review rounds each found the next spelling it missed*. Three rounds of this item found the next switch form the same way |
| `seal/specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused/spec.md` §Grounding, the #834 row | *What converged read an owned format or an observed fact and refused the unknown. What did not converge read someone else's text and let the unknown through.* The test the reframed deny is written against: every sentence in it is a fact the guard read or a fact about the guard itself |
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

### In 2 — the dirty-tree row under the press is a deny to the model, and its own sentences predict nothing

*Reframed after round 3. The first frame's In 2 prescribed a way on per
switch form; §*Why the deny's own sentences predict nothing* says what that
cost and why this In 2 replaces it. The press sentence and the shape — fact, press, ways
on, no question tool, the re-issue sentence — are the first frame's and stay.*

Where `automation_answered` is True for the session's own clone, the
tracked-changes row of §A answers `deny` instead of `ask`. **The reason
states what the guard read, and infers nothing beyond the index-residue note
it shares with the `ask`.** The guard holds three
facts: tracked changes are present (`git status`, the `entries` list), the
command asks for a switch (its shape, §A), and the press is in this session's
transcript. What the switch form does with the changes, where a commit lands,
whether a `stash pop` applies cleanly — none of that is read from any fact
the guard holds, and no sentence of the reason says it. The reason:

- opens with the lead and lists the changes as today (file list, index-only
  residue note, the three leads of #624.2 unchanged in wording), and says
  only that they are present — not what the switch would do with them;
- carries the press sentence, byte-identical to the first frame's and to the
  one #896 copies: *This session's person pressed `automation` on the routing
  question, so this guard puts no question to them, and none is to be put to
  them in its place.*;
- says what the row means, in the guard's own terms: it stops a switch while
  uncommitted tracked changes are present, and where none are present it
  says nothing (§A's clean row — an owned fact);
- names `git commit` and `git stash`, each as a listed shape that passes
  this guard when issued alone (§A, *Which commands reach these rows* — an
  owned fact, S4), and says that which one fits this switch, and what
  follows it, is the model's to decide. It
  promises no outcome for any form, and names no sequence past the one
  command: no `pop`, no *then re-issue the switch* for one form and *take
  the other way* for another;
- says each command is issued on its own, because the guard reads the tree
  before the command runs and a compound `git stash && git switch x` meets
  the same row (S5 — an owned fact);
- names no question tool, and says that re-issuing the command unchanged
  meets the same refusal (the commit gate's shape).

**One text for every switch form.** The reason is the same bytes for a plain
switch, the creating family (`-c`, `-C`, `--create`, `--force-create`),
`--orphan`, `--detach`, the discarding forms (`-f`, `--discard-changes`),
`-m`/`--merge` and `-`, from a branch and from a detached HEAD, and it
contains no switch option word (S12). A per-form clause is a prediction, and
S12 is the case that keeps one from coming back as a fix: a form a later
round finds is a row in S12's parametrisation, never a sentence in the deny.

Without the press the row is byte-for-byte today's `ask` (S2). `[shared-tree-ok]`
stays ignored at this row in both readers: it answers a different question
(§*Choice sites*). Carrying the changes along, the one destination approving
used to give, is what the model decides for itself under the press, with the
commands git offers; the deny neither names nor forbids it.

**Failure direction.** Blocks more, never allows more: a verdict moves from
`ask` to `deny` in one state and nowhere else. A wrong deny — a press read
where the owner had taken it back — costs the model a turn; the reader that
decides it is unchanged, so this work can produce no such reading that today's
unrecognised-shape stop does not already produce. **Prompt budget.** Under the
press the dirty row puts zero questions to a person, from one per dirty switch.
Attended, unchanged. In 3 adds one click at a resume, at a moment a person is
present by definition. **What the shorter reason gives up.** A model told
less decides more: one that stashes and never restores leaves a stash in its
own session, listed by `git stash list`, and one that commits onto a detached
HEAD has a commit no branch names until it names one. Neither loses the
change, and neither is this guard's to predict; M4 measures whether it
happens, and P3 is whether the stash should be named at all.

### Why the deny's own sentences predict nothing (reframe after round 3)

Three review rounds each found the first frame's recipe wrong for one more
switch form. Round 1: `-c` — *commit here first* puts the commit on the
branch being left, so the fix sent a creating switch to the stash way. Round
2: `--orphan` — the stash way's pop conflicts on the empty tree, so the fix
sent `--orphan` back to the commit; and `-f`/`--discard-changes` drop the
changes, so *would follow* was false and the premise was narrowed. Round 3:
a detached HEAD with `--orphan` — the detached-HEAD sentence still offered
the stash way; and a target branch that changed a listed file — the pop stops
on a `UU` conflict where the reason promised a carry. Each fix was a sentence
about what git does for one form, and each next round found the form the
sentence had not named (`rounds/round-1.md`, `round-2.md`, `round-3.md`).

Round 3's table of sixteen setups is the measurement (`rounds/round-3-report.md`
§1): fourteen cells where the recipe held and two where it did not, and
nothing the guard reads distinguishes them. The guard does not read HEAD's
state, the target branch's history, or what a stash holds, and the first
frame refused to add a git spawn for the first of those (W1). A reason that
is right in fourteen cells and wrong in two, with no fact to tell them apart,
is a prediction from text, and this repository has judged that class not to
converge three times over (the Grounding rows for
`docs/the-commit-gate-inside-git.md`, the brace reader, and 1791384159).

So the reframed deny keeps every sentence that is a fact the guard read or a
fact about the guard itself — the changes listed from `git status`, the
press, that `commit` and `stash` are listed shapes (S4), that a compound
meets the same row (S5), that a re-issue meets the same refusal — and drops
every sentence of its own about what git will do. The index-residue note it
shares with the `ask` stays as the `ask` has it. Round 3's two findings
close under this frame by the removal of the sentences they were about, not
by a third sentence; the redesign's own review round records that
(`skills/code-review/orchestration.md` §*A fix of a fix twice sends the work
item back to its framer*, *A record after the stop is the redesign's*).

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
- **A guard that reads HEAD's state, the target branch or the stash to
  tailor the reason** (reframe). That is a new reader for a fact the deny
  would then predict from, and §*Which tree* pins the switch arm's reading
  not to grow; `plan.md` J says why it would not have ended the rounds
  either.
- **The attended `ask`'s own prediction** — *They will follow you onto the
  target branch* is the base's text and is false for the discarding forms
  too. S2 pins it byte-identical, and it is #21's attended site; the reframe
  changes the pressed reader only.

## User scenarios & acceptance *(mandatory)*

Each S-row is a case in `tests/test_the_guard_asks_once_per_session.py` or
`tests/test_worktree_guard.py` unless it says otherwise; each new case is seen
red against the base (`c38f97d7`) and the handover says how.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the dirty row under the press is a deny that states the facts (rewritten at the reframe) | Given session `me`'s `automation` press in its transcript (`ask_entries`), a single-stream tree with one modified tracked file · When `git switch feature/x` · Then `deny`; the reason lists `f.txt`, carries the press sentence byte-identical to the first frame's, names `git commit` and `git stash` as commands issued on their own that pass this guard alone, says the choice and what follows are the model's, says re-issuing unchanged meets the same refusal, and contains none of `AskUserQuestion`, `pop`, `way 2`, `squash`, `carries`, `-c`, `--orphan`, `detached`. Both languages (`SPECSEAL_LANG=ko`), the whole text pinned | `test_under_the_press_the_dirty_row_is_a_deny_to_the_model` rewritten; red at `0f1663f5`'s guard (its text names `-c`, `--orphan` and way 2) and at the base (`ask`) |
| S2 without the press the row is today's ask | Given no press · When the same command in the same tree, in each of the three states of `test_the_dirty_tree_row_names_what_was_measured` · Then the reason is byte-identical to the base's | the existing case stays; one new assertion compares against the base's text captured in the case |
| S3 the token does not reach the row under the press either | Given the press, only-idle sessions or detection unusable, a dirty tree · When `git switch other  # [shared-tree-ok]` · Then `deny`, lead `[shared-tree-ok] carries the user's answer…`, the rest S1's text | new case; red at the base (`ask`) |
| S4 the named commands pass the guard (narrowed at the reframe) | Given the press and a dirty tree · When `git commit -am x` then `git switch feature/x` as two issues; and `git stash` then `git switch feature/x` as two · Then every issue is silent at the guard: the two commands are listed shapes, and the switch after either meets a clean tree. What git did with the change is asserted by nothing, because the deny promises none of it | `test_the_ways_on_pass_the_guard` narrowed to the owned claim, real git in the fixture repository, the guard run per issue (`decide`) and git run between them. The three recipe cases of rounds 1–2 — `test_a_creating_switch_under_the_press_takes_the_stash_way`, `test_an_orphan_switch_under_the_press_takes_the_commit_way`, `test_the_deny_does_not_say_a_discarding_switch_carries_the_changes` — are removed with the sentences they pin, and their `Enforced by:` entries with them (W4; NAME NOT IN TREE since phase 3) |
| S5 a compound stash-and-switch meets the deny, not a loop | Given the press and a dirty tree · When `git stash && git switch feature/x` · Then `deny` with S1's text, which says to run them as commands of their own | new case; red at the base (`ask`) |
| S6 the plain retry after an unrecognised-shape stop meets In 2 | Given the press and a dirty tree · When `git checkout feature/x` then `git switch feature/x` · Then `deny` with the stop's text, then `deny` with S1's text; in an ACTIVE tree both are the deny with the worktree steer, as today | `test_the_plain_retry_meets_todays_rows` rewritten; its 0.20.0 ledger row S6 takes a `Corrected ·` citing row in this item's fragment |
| S7 a creation on the same line is stopped with it and records nothing | Given the press, no consent record, a dirty tree · When `git switch feature/x && git worktree add ../wt f` · Then `deny`, and `specseal-worktree-consent/` holds no file for `me` | new case; the PostToolUse writer is not run because the command did not |
| S8 the other readers are unchanged | `hooks/commit-review-gate.py`, `hooks/worktree_consent.py` and `hooks/cmdline_base.py` are byte-identical to `c38f97d7`'s | `git diff c38f97d7 -- <the three>` is empty; read at review and asserted by the handover |
| S9 the policy says what the code does (rewritten at the reframe) | `docs/worktree-guard-spec.md` §A's tracked-changes row and *The tracked-changes row has two readers too* carry the reframed In 2 — the deny states the facts, names the two commands, promises no outcome, one text for every form — with one paragraph saying why (§*Why the deny's own sentences predict nothing*, in the policy's words), and `Enforced by:` lines naming S1, S3, S5, S6, S12 and losing the three removed cases; *The stop has two readers* is unchanged; §*Known limits* carries In 1 (the press is this session's, on this machine; a resumed run presses again); the module docstring's row (`hooks/worktree-guard.py` lines 27–31) says the same in its words | the `Enforced by:` resolver (`tests/test_a_folded_statement_names_what_enforces_it.py`), `tests/test_docs_line_wrap.py`, the survivor sweep |
| S12 one text for every switch form (new at the reframe) | Given the press and a dirty tree · When each form round 3's table enumerated — plain `feature/x`, `-c newb`, `-C newb`, `--create newb`, `--force-create newb`, `-C feature/x`, `--orphan newb`, `--detach feature/x`, `-f feature/x`, `--discard-changes feature/x`, `-m feature/x`, `--merge feature/x`, `-` — from a branch, and plain and `--orphan newb` from a detached HEAD · Then every verdict is `deny` with byte-identical reasons across the forms, and the reason contains none of the forms' option words and none of `pop`, `way 2`, `carries`, `conflict`, `detached`. Both languages | new case, parametrised over the table so a form a later round finds is a row here and not a sentence in the deny; red at `0f1663f5` on the word check (its one reason names `-c` and `--orphan`); the equality half is one string at `0f1663f5` too, so it is seen red through `mutation-check` with a per-form clause planted in the text |
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
- Text: one `tr(en, ko)` pair for the deny, the same bytes for every switch
  form, with no clause keyed on a form, HEAD's state, or the target branch
  (S12); the three leads of #624.2 keep their words, and the press sentence
  keeps the first frame's bytes.

## Rule changes

- nothing
  why: written: the tracked-changes row's two readers, in docs/worktree-guard-spec.md *A*.

## Open questions → questions.md

P1–P3 (a person); M1–M4 (a measurement); W1–W4 (the work). Each row says
which judgment it could not settle from the tree and who closes it. P3, M4,
W3 and W4 are the reframe's.

Framed 2026-10-12 by framer, before the build.
Reframed 2026-10-12 by framer, after round 3.
