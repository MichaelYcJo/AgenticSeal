# 1791384157-the-hooks-read-the-session-waiver-and-creation-one-way — round 6 report

Written by specseal:warden on Opus 5.5. Target SHA
`8bba58353607204de53f50fd4a64c0161024e8bd`, PR 881, draft, into
`release/v0.21.0`. This is the second redesign's first finding round, and
its target is `99a35836..8bba5835`: the merge `048506e7` of the release
branch at `ad447367`, then phases 11 and 12 (`63a518a8`, `8e231b70`,
`8bba5835`). Counts start over past the reframe.

## What this round was asked

Five judgments and one check. Does any brace-reading code, case, sentence or
ledger claim survive? Do the four #856 forms pass in an ACTIVE tree exactly as
the limit states, with nothing else changed for brace-free commands against
0.20.0's guard? Are #868's four other facts intact? Are the 77 `NAME NOT IN
TREE` markers fair, and was any sibling fragment left altered? And my own
axes. The check was the eight guard modules, once.

The smith's account arrived labelled, and I read all of it. Each claim below
is checked against the code. Probes ran in a `git clone --no-local` of the
worktree at the target, under the session's scratchpad. Nothing was written in
the worktree but this report.

## How the answers relate

```
the brace reader leaves the guard (phase 11)
  ├─ guard code, tests, policy: gone; guard verdicts identical to 0.20.0   (confirmed)
  ├─ but one comment outside the guard still describes it                  (🟡 1)
  └─ the rebase sentence added beside the removal says more than git does  (🟡 2)
records rewritten for the removal (phase 12)
  ├─ markers fair, sibling fragments untouched                             (confirmed)
  └─ two paperwork corrections                                             (⬜ 3, ⬜ 4)
```

The removal is complete in the guard. What it left behind sits one file over,
and in a new policy sentence that the removal brought in.

## 🟡 1. `hooks/tokens.py` still says the guard reads a brace through it

`hooks/tokens.py:66-69`, the comment above `QUOTED_SPANS`:

> `is_plain` reads a subshell or a group through it, and the worktree guard
> reads a brace expansion through it (#856), so the two agree on what a quote
> is.

The guard no longer reads a brace at all. This branch extracted the constant
in phase 3 for the brace reader, as `phases/phase-3.md:37` records, and
phase 11 took the reader out without returning to this comment. Executed: a
search of `hooks/`, `tests/`, `bin/` and `skills/*/scripts` for `QUOTED_SPANS`
finds `hooks/tokens.py:70` and its one reader, `hooks/tokens.py:279` in
`is_plain`. No other code uses it.

Why it matters. The round was asked whether any brace sentence survives, and
this one does. It states, in shipped source, a behaviour the release removes.
A reader who trusts it will look for the guard's quote reading in
`hooks/tokens.py` and find no caller. Ledger row S25 limits its absence claim
to `hooks/worktree-guard.py`, so no record catches it either.

The class, enumerated under §12: every unit and sentence the brace reader
added outside `hooks/worktree-guard.py`. Searching code and tests for
`brace` and `#856` turns up only this comment, apart from the guard's limit
comment, its `_rebase_names_a_branch` docstring and the cases that pin the
limit. Each of those describes the limit rather than a reader. A
constant with one reader could go back inline in `is_plain`, but keeping it is
harmless; the fix below only corrects the sentence.

## 🟡 2. The rebase sentence says a rebase reaches the hook as a switch does, and from its onto branch it does not

`docs/the-commit-gate-inside-git.md:174-177`, added in phase 11 (S28):

> A branch-naming rebase reaches `reference-transaction` the same way a
> switch does: on 2.50.1 its line names the branch after the tree already
> holds it (`git rebase main other`, …).

The S28 parameter runs `git rebase main other` where `main` is an ancestor of
`other`. In that topology the rebase only checks `other` out, so it acts as a
switch. Where the two branches have diverged and the tree is on `main`, the
rebase first detaches HEAD at `main`'s own commit. That line reaches
`reference-transaction` before any of `other`'s content is in the tree.

Executed on git 2.50.1, in scratch repositories driven from Python. `main`
and `other` diverged, the tree on `main`, a hook refusing the first line that
ends in ` HEAD` at `prepared`:

- The prepared HEAD line arrived with `marker.txt` still reading `main`'s
  content and HEAD still `ref: refs/heads/main`.
- git exited 128, `fatal: ref updates aborted by hook`, and left HEAD on
  `refs/heads/main` with the tree clean. No broken state.
- Run without the refusal, the line naming `refs/heads/other` arrived last,
  after the tree held the rebased branch, as the sentence says.
- From a third branch, `third`, the tree moved to `main`'s content before
  the first HEAD line, and the refusal left the index dirty. That is the
  switch's pattern.

So the sentence holds for the line naming the branch. It is wrong as a
statement about how a branch-naming rebase reaches the hook. The form it is
false for is #856's first form as typed from `main`: `git rebase
{main,feature/x}` is `git rebase main feature/x`.

Why it matters. The second reframe's ground for **delete** is that
`reference-transaction` sees a switch only after the tree moved, so watching
the act cannot refuse it (the `overview.md` divergence row for phase 11).
For a rebase typed from its onto branch, a hook can refuse before the named
branch's content reaches the tree. The policy now states the opposite as a
fact and pins it (`tests/test_the_commit_gate_decides_at_the_commit.py:1607`).
#886 is where that ground gets decided, so the sentence should hand #886 the
true picture. Telling this detach apart from an ordinary rebase or
`checkout --detach` would itself be a reading of what git is about to do,
which is #886's question and not this round's.

## ⬜ 3. S28's unverified half names an answerer that does not run

Ledger row S28 (`seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:9`)
reads "**Unverified**: the floor gits 2.34–2.43, which the CI legs answer at
the pull request", and `phases/phase-11.md:54` reads "The CI floor leg
answers for 2.34–2.43". No CI leg runs those gits. `.github/workflows/test.yml`'s
floor is Python 3.12, and the ubuntu pytest job at the target logged
`git version 2.55.0` (executed: its log, read through `gh api`). A label
that names nobody who can answer is the deferral §4 forbids. This is
paperwork under `seal/`, so it is a correction: the row should name the
repository owner, or say that no leg runs a floor git.

## ⬜ 4. The plan's phase 11 row keeps a marker for names now planted

`seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/plan.md:235`
ends "the two new case names are NAME NOT IN TREE until this phase plants
them". The phase planted both, so the marker now exempts a line on which
every underscore name is in the tree. It is the one marker of the 83 added
lines that does (executed, see the probes). The same row's
verification cell says the grep shows "only the limit's comment", where
`phases/phase-11.md:69` records three lines. Both are corrections.

## What was confirmed

**The brace reader is gone from the guard and its tests.** Read: the diff
`048506e7..8bba5835` of `hooks/worktree-guard.py` takes out the brace test,
the quoting reader, every `braced` parameter and arm, the union of trees,
the `brace` branch of `_described` and `main`'s brace read, and `main` calls
`_finding_tree` again. The test diff takes out thirteen cases, three
constants, one helper and two policy pins, matching `phases/phase-11.md`'s
table name for name. Executed: none of the removed names appears in
`hooks/`, `tests/`, `docs/` or `skills/` outside this work item's records.
In the guard, the brace mentions left are the limit comment, the docstring
pointing at it and 0.20.0's note on a brace group.

**The four forms are silent in every tree, and nothing else moved.**
Executed: 589 commands, run through `main()` of 0.20.0's guard and of the
target's in five tree states each. The commands are every command-shaped
literal in the guard's four test modules at `v0.20.0`, `52c72bbe` and the
target, which includes all thirteen removed brace cases' spellings, plus 33
written by hand. That gives 2,945 decisions, with 1,850 silent, 560 deny and
535 ask at the target. Not one decision and not one reason differs between
the two guards. The four forms are silent in all five states, and the
controls `git rebase main feature/x` and `git worktree add ../wt feature/x`
stop in every state but one. So the limit's "listed and silent in every
tree" is exact, the changelog's "as at 0.20.0" is exact, and no brace-free
command changed. Round 5's spellings (`$''{g..g}it switch feature/x`,
`{git,$(: x)} switch feature/x`, `{git,${x:- }} switch feature/x`) are
among the silent.

**#868's four facts are intact.** Read: among the hooks, the redesign range
touches only `hooks/worktree-guard.py`, and there only brace code and three
comments. `hooks/hooksession.py`, `hooks/tokens.py`, `hooks/worktree_consent.py`,
`hooks/gate.py`, `hooks/session-lease.py` and their tests are byte-identical
between `048506e7` and the target. The guard's diff against `v0.20.0` is now
the #868 changes alone: placement through `worktree_consent.place`, the token
read through `tokens.given`, and the session count through
`hooksession.is_claude`. Executed: the token commands in the corpus,
apostrophe and parenthesis forms included, decide as at 0.20.0, which is
what S9 claims for the guard.

**The markers are fair and no sibling fragment is altered.** Executed: the
redesign adds 83 lines carrying `NAME NOT IN TREE` across 19 records of this
work item. 82 of them each name at least one unit absent from the tree, every
one a historical record (rounds, phases, `spec.md`, `overview.md`). The
exception is ⬜ 4. `git diff --name-only ad447367..8bba5835 -- seal/` lists
nothing outside this work item, `8e231b70` touches no other item's file, and
the worktree's status is clean. The four fragments the over-wide
`--reverify --into` re-dated are as the release branch has them.

## Earlier rounds' verdicts

- Round 5's yellow 1 and yellow 2 were fixed at `aa8cd282..bdf65b20` and
  never verified. The reading they fixed left the tree in phase 11, and the
  spellings are now silent as the limit states (executed above). The class
  was deferred to #886 by the second reframe, and I report it as already
  deferred.
- Rounds 1 to 4's brace findings were each closed by a reading that is no
  longer in the tree. The same holds for them: their spellings are silent by
  design now, and the class sits with #886.
- #868's non-brace closures (round 1's yellow 4 and white 6, round 2's white
  4 and 5, round 3's white 4) are carried. The range touches none of their
  units or cases, so the closures stand on the earlier rounds' executed
  grounds, which I did not re-run.
- Round 1's white 5 and round 5's white 3 and 4 were about the removed reader
  and its count, and those left with it.
- The question whether a hook process sees `CLAUDE_PID` and
  `CLAUDE_CODE_SESSION_ID` stays open, carried from rounds 1, 2 and 4.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The comment above `QUOTED_SPANS` still says the worktree guard reads a brace expansion through it; the guard reads none since phase 11 | `hooks/tokens.py:68` | open | executed: `QUOTED_SPANS` has one reader, `is_plain`; read: the comment and the guard's diff |
| 🟡 2 | The rebase sentence says a branch-naming rebase reaches `reference-transaction` as a switch does; from its onto branch with diverged branches, the first HEAD line arrives before the branch's content and a refusal there leaves the tree clean | `docs/the-commit-gate-inside-git.md:174` | open | executed on git 2.50.1: the refusal exits 128 with HEAD on `main` and a clean tree; from a third branch the tree moves first; the pinned parameter covers only the case where `main` is an ancestor of `other` |
| ⬜ 3 | S28 and phase 11 name the CI legs as the answerer for git 2.34–2.43, and no leg runs those gits | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:9` | open | executed: the ubuntu job at the target logged git 2.55.0; read: `.github/workflows/test.yml`'s matrix; a correction |
| ⬜ 4 | The plan's phase 11 row keeps a marker for two case names the phase planted, and says the grep shows one comment where phase 11 records three lines | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/plan.md:235` | open | executed: the only one of 83 added marker lines whose underscore names are all in the tree; a correction |
| 🟢 | The brace reader is absent from the guard, its tests and its policy | `hooks/worktree-guard.py:2002` | confirmed | read: the diff; executed: no removed name outside this work item's records |
| 🟢 | The four #856 forms are silent in every tree state, and no decision differs from 0.20.0's guard | `hooks/worktree-guard.py:2883` | confirmed | executed: 2,945 decisions, two guards, zero differences; the limit and contrast cases ran (12 passed, the bash half not skipped) |
| 🟢 | #868's placement, token reader, session test and git runner are intact | `hooks/worktree_consent.py:507` | confirmed | read: the range touches none of their files; executed: token commands decide as at 0.20.0 |
| 🟢 | The added markers are fair and no sibling fragment is altered | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:1` | confirmed | executed: 82 of 83 marked lines name an absent unit; no file outside this work item differs from `ad447367` |
| ⬜ | Round 5's yellow 1 and yellow 2, a brace hidden by a quote's `$` or by whitespace inside a substitution | `hooks/worktree-guard.py:2002` | deferred #886 | already deferred by the second reframe (`overview.md` Not done, `questions.md` P2); the units they were fixed in left in phase 11; executed: the spellings are silent in all five states |
| ⬜ | Rounds 1 to 4's brace findings, each closed by a reading that left the tree | `hooks/worktree-guard.py:2002` | deferred #886 | already deferred by the second reframe; executed: their spellings are silent in all five states, as the limit says |
| 🟢 | rounds 1 to 3's non-brace closures stand — the lease writer's session tie, the ANSI-C docstring, the lease case that can fail | `hooks/session-lease.py:93` | confirmed | carried, not re-run: the range touches none of their units or cases |
| ❓ | Whether a hook process the harness spawns sees `CLAUDE_PID` and `CLAUDE_CODE_SESSION_ID` | `hooks/hooksession.py:68` | ❓ out of verified scope | carried from rounds 1, 2 and 4; no hook's environment can be printed without changing the installed configuration; the repository owner answers |
| ❓ | Whether delete stands: P2 reverses the owner's confirmed (c) for #856 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/questions.md:95` | ❓ out of verified scope | this round judged the deletion as built; a *format* answer replaces it; the repository owner answers |
| ❓ | The four Windows pytest jobs at the target | `.github/workflows/test.yml:32` | ❓ out of verified scope | pending when `gh pr checks 881` was read; every other check passed; the orchestrator reads them before the sealer is spawned |

## Executed probes

| What was run | Result |
|---|---|
| The eight guard modules, `bin/test` with the eight paths the prompt names, in the clone at the target | 437 passed, exit 0 |
| `bin/test tests/test_worktree_guard.py tests/test_the_hook_surface_git_offers.py -k "named_limit or moves_head_under_git or refuses_a_switch_before" -p no:xdist -rs` | 12 passed, none skipped, exit 0 |
| `main()` of `v0.20.0`'s `hooks/` and of the target's `hooks/`, 589 commands in five tree states each, sessions and transcripts stubbed as the suite stubs them | 2,945 decisions each; 0 decisions and 0 reasons differ; four #856 forms silent in all five states; controls stop |
| `main()` of the target on `$(echo git) switch`, a here-string and two heredocs handed to a shell, `g""it switch` | the first four silent in ACTIVE and clean, as §*Known limits* says; `g""it switch` denies in ACTIVE |
| Diverged `main` and `other`, tree on `main`, `git rebase main other` under a `reference-transaction` hook refusing the first ` HEAD` line at `prepared`, git 2.50.1 | the HEAD line arrives with the tree on `main`; exit 128; HEAD `refs/heads/main`; tree clean |
| The same without a refusal | the line naming `refs/heads/other` arrives last, after the tree holds the rebased branch |
| The same from a third branch with the refusal | the tree held `main`'s content before the first HEAD line; the index was left dirty |
| The paste-ready case of 🟡 2 and its flip, as one `test_tmp_*` file, run once and deleted | the case passed; the flip (the tree moved first) failed |
| Added `NAME NOT IN TREE` lines in `048506e7..8bba5835`, each line's backticked underscore names searched in `hooks/`, `tests/`, `bin/`, `skills/`, `.github/`, `docs/` | 83 lines; 82 name an absent unit; one does not (⬜ 4) |
| `git diff --name-only ad447367..8bba5835 -- seal/`, outside this work item | nothing |
| Search of `hooks/`, `tests/`, `bin/`, `skills/*/scripts` for each removed unit, for `brace` and for `#856` | the removed names only in this work item's records; one surviving reader sentence (🟡 1) |
| `gh pr checks 881`, read at the end of the round | lint, ledger, release, both arm-check-grammar jobs, the ubuntu job and three macOS shards passed; four Windows shards pending |
| The ubuntu pytest job's log at the target, through `gh api` | `git version 2.55.0` |
| `bin/evidence-check . --strict`, `bin/survivor-check`, `bin/correction-check` | not run by this round; the smith's exits are a claim, and the sealer answers |
| The full suite | not yet — the sealer's, once the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The brace class of #856: every spelling rounds 1 to 5 found, now listed and silent as a named limit | #886, by the second reframe; already deferred, not new | the repository owner, through `questions.md` P2 and #886 |
| Whether `reference-transaction`'s first HEAD line for a rebase typed from its onto branch could be refused (🟡 2's fact, as design input) | #886 | the repository owner |

## Paste-ready fixes

### 🟡 1, `hooks/tokens.py` lines 66 to 69

```python
# A backslash escape, a single-quoted span and a double-quoted span: what a
# text read takes out to see what the shell leaves unquoted. `is_plain` reads
# a subshell or a group through it.
QUOTED_SPANS = re.compile(r"\\.|'[^']*'|\"(?:\\.|[^\"\\])*\"")
```

### 🟡 2, `docs/the-commit-gate-inside-git.md` lines 174 to 177

```markdown
M1). A branch-naming rebase reaches `reference-transaction` as a switch does
when it only checks the branch out: on 2.50.1 its line names the branch after
the tree already holds it (`git rebase main other` with `main` an ancestor of
`other`, executed by the second reframe of work item 1791384157). Where the
branches have diverged and the tree is on the onto branch, the rebase first
detaches HEAD at that branch's own commit, and that line arrives before any
of the named branch's content is in the tree: refused there, git leaves the
tree on the onto branch, clean (round 6 of that work item). The line naming
the branch still arrives last. Whether the detach can be told from an
ordinary rebase is #886's question. A worktree creation can be judged after
git made it, in `post-checkout`,
```

### 🟡 2, the pin in `tests/test_the_commit_gate_decides_at_the_commit.py` line 1607

```python
        "A branch-naming rebase reaches `reference-transaction` as a switch does "
        "when it only checks the branch out",
        "the rebase first detaches HEAD at that branch's own commit, and that "
        "line arrives before any of the named branch's content is in the tree",
```

### 🟡 2, a case beside `test_no_git_refuses_a_switch_before_the_tree_moves` in `tests/test_the_hook_surface_git_offers.py`

```python
def test_a_rebase_from_its_onto_branch_is_seen_before_the_branch_reaches_the_tree(
    tmp_path,
):
    """Round 6 of work item 1791384157, yellow 2. With `main` and `other`
    diverged and the tree on `main`, `git rebase main other` first detaches
    HEAD at `main`'s own commit. That line reaches `reference-transaction`
    before any of `other`'s content is in the tree, and a refusal there
    leaves the tree on `main`, clean. Executed on 2.50.1: passes, and the
    flip asserting the tree moved first fails."""
    d, hooks = repo(tmp_path)
    (d / "f.py").write_text("a = 2\n", encoding="utf-8")
    g(d, "commit", "-q", "-am", "main side")
    log = tmp_path / "rt.log"
    hook(hooks, "reference-transaction", REFUSING_RT)
    r = g(
        d,
        "rebase",
        "main",
        "other",
        check=False,
        env={"RT_LOG": str(log), "REFUSE_SUFFIX": " HEAD"},
    )
    text = log.read_text(encoding="utf-8") if log.exists() else ""
    if not re.search(r"^  \S+ \S+ HEAD$", text, re.M):
        # A git that sends the detach no line cannot refuse it either.
        assert r.returncode == 0, r.stderr
        assert head(d) == "refs/heads/other"
        return
    assert r.returncode != 0
    assert head(d) == "refs/heads/main"
    assert (d / "marker.txt").read_text(encoding="utf-8") == "main\n"
    assert "prepared main" in text
    assert g(d, "status", "--porcelain").stdout.strip() == ""
```

## Regression tests to plant

- The case above, in `tests/test_the_hook_surface_git_offers.py`, with its
  name added to the `Enforced by:` line under the convergence paragraph of
  `docs/the-commit-gate-inside-git.md`. NAME NOT IN TREE until planted:
  `test_a_rebase_from_its_onto_branch_is_seen_before_the_branch_reaches_the_tree`.
  Seen red here by its flip, not against the doc; the smith shows it red
  again before planting it (§15).
- No case is proposed for 🟡 1. It is a comment, and no reader sees it.

## Facts for the evidence ledger

- S28's claim should be narrowed to the topology it ran, `main` an ancestor
  of `other`, and a row added for the diverged case once the case above is
  planted. Executed on 2.50.1 by this round.
- S28's **Unverified** cell should name an answerer who runs a floor git, or
  say that none does (⬜ 3).
- S25 holds as written for `hooks/worktree-guard.py`. If 🟡 1 is fixed, a
  clause saying `hooks/tokens.py` names no brace reader would close the class
  in the record.

## The broad gate

`not yet`. No full-suite run exists at the target or at any earlier SHA of
this redesign. This round leaves two 🟡 open, so the gate has not come due;
the sealer is spawned once a round records nothing needing a fix.

Needs a fix: yes — 🟡 1 (a comment in `hooks/tokens.py` still says the guard reads a brace through `QUOTED_SPANS`), 🟡 2 (the rebase sentence and its pin say a branch-naming rebase reaches `reference-transaction` as a switch does, which is false from the onto branch with diverged branches)
Loses a record or crashes: no

## Proof block

Files opened this round, at the target, in the clone:

- `hooks/worktree-guard.py` (the diffs against `048506e7` and `v0.20.0`)
- `hooks/tokens.py` (lines 62 to 71, and the diff against `v0.20.0`)
- `docs/worktree-guard-spec.md` (the diffs against `048506e7` and `v0.20.0`)
- `docs/the-commit-gate-inside-git.md` (lines 168 to 185)
- `tests/test_worktree_guard.py` (lines 1 to 60, 470 to 549, 1100 to 1149, 1940 to 2124)
- `tests/test_the_hook_surface_git_offers.py` (lines 60 to 209)
- `tests/conftest.py` (lines 163 to 180, 480 to 554, 812 to 852)
- `.github/workflows/test.yml` (lines 25 to 60, 180 to 200)
- `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md` (whole)
- `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/changelog.md`
- `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/phases/phase-11.md`
- `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/phases/phase-12.md`
- `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/plan.md` (line 235)
- the redesign's diffs of `overview.md`, `questions.md`, `spec.md` and `survivors.md`
- `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/rounds/round-1.md` to `round-5.md` (verdict tables and the two lines)
- `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/rounds/round-5-report.md` (structure)
