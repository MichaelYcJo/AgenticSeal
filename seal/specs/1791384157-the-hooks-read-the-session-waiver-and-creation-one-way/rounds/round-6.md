# 1791384157-the-hooks-read-the-session-waiver-and-creation-one-way — review round 6

| Field | Value |
|---|---|
| Target SHA | 8bba58353607204de53f50fd4a64c0161024e8bd |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 881 |
| Broad gate | 4bc36941 against 23f5977c |
| Fixes checked by | no fixes to check |
| Fix range | `8bba58353607204de53f50fd4a64c0161024e8bd..d37021860400c0cde680e683f8b6c5f31eb98f07`, 3 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (a comment in `hooks/tokens.py` still says the guard reads a brace through `QUOTED_SPANS`), 🟡 2 (the rebase sentence and its pin say a branch-naming rebase reaches `reference-transaction` as a switch does, which is false from the onto branch with diverged branches) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

The second redesign's first finding round: 99a35836..8bba5835, the merge 048506e7 of the release branch at ad447367, then phases 11 and 12 (63a518a8, 8e231b70, 8bba5835). Counts start over past the reframe. The redesign deletes the brace reader after the framer found that git's reference-transaction hook cannot refuse a switch before the tree moves. The spawn asked five things: whether any brace-reading code, case, sentence or ledger claim survives; whether the four #856 forms pass in an active tree exactly as the limit states while brace-free commands decide as 0.20.0's guard does; whether #868's four other facts are intact; whether the 77 NAME NOT IN TREE markers are fair and no sibling fragment was altered; and the reviewer's own axes. Probes were to run in a scratch repository, never the session's checkout. It also ran the eight guard modules once. Facts arrived labelled. Read: the owner's 2026-10-12 direction to observe the act rather than predict the command. Read from the smith: the deletion, the named limit, the markers and the module runs.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The comment above `QUOTED_SPANS` still says the worktree guard reads a brace expansion through it; the guard reads none since phase 11 | `hooks/tokens.py:68` | deferred #893 | #893 — the run ends at this record (capped: round 4 met the floor and round 5 closed on a fix, counted by the generator across the owner-directed reframe). The comment names a reader the guard no longer has; the one-clause deletion is in the report and in #893; executed: `QUOTED_SPANS` has one reader, `is_plain`; read: the comment and the guard's diff |
| 🟡 2 | The rebase sentence says a branch-naming rebase reaches `reference-transaction` as a switch does; from its onto branch with diverged branches, the first HEAD line arrives before the branch's content and a refusal there leaves the tree clean | `docs/the-commit-gate-inside-git.md:174` | deferred #893 | #893 — the run ends at this record. The finding bears on whether the second reframe's delete stands, which is `questions.md` P2, the owner's to answer; #893 carries the executed topology, the sentence, its pin and the reviewer's case; executed on git 2.50.1: the refusal exits 128 with HEAD on `main` and a clean tree; from a third branch the tree moves first; the pinned parameter covers only the case where `main` is an ancestor of `other` |
| ⬜ 3 | S28 and phase 11 name the CI legs as the answerer for git 2.34–2.43, and no leg runs those gits | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:9` | answered | corrected at e9ed9e54: S28 and `phases/phase-11.md` say no CI leg runs the floor gits and name the repository owner as the answerer; executed: the ubuntu job at the target logged git 2.55.0; read: `.github/workflows/test.yml`'s matrix; a correction |
| ⬜ 4 | The plan's phase 11 row keeps a marker for two case names the phase planted, and says the grep shows one comment where phase 11 records three lines | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/plan.md:235` | answered | corrected at e9ed9e54: plan row 11 drops the marker for the two planted case names and says the grep found three lines; executed: the only one of 83 added marker lines whose underscore names are all in the tree; a correction |
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

## Paste-ready fixes

```python
# A backslash escape, a single-quoted span and a double-quoted span: what a
# text read takes out to see what the shell leaves unquoted. `is_plain` reads
# a subshell or a group through it.
QUOTED_SPANS = re.compile(r"\\.|'[^']*'|\"(?:\\.|[^\"\\])*\"")
```
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
```python
        "A branch-naming rebase reaches `reference-transaction` as a switch does "
        "when it only checks the branch out",
        "the rebase first detaches HEAD at that branch's own commit, and that "
        "line arrives before any of the named branch's content is in the tree",
```
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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `tests/test_worktree_guard.py:2178` | round 1's 🔴 1 — fixed |
| round-1 | `tests/test_worktree_guard.py:729` | round 1's 🔴 2 — fixed |
| round-1 | `hooks/worktree-guard.py:2270` | round 1's 🟡 3 — fixed |
| round-1 | `hooks/session-lease.py:91` | round 1's 🟡 4 — fixed |
| round-1 | `hooks/worktree-guard.py:2007` | round 1's ⬜ 5 — answered |
| round-1 | `hooks/tokens.py:33` | round 1's ⬜ 6 — fixed |
| round-1 | `hooks/hooksession.py:68` | round 1's ❓ — out of verified scope |
| round-1 | `hooks/worktree_consent.py:419` | round 1's ❓ — out of verified scope |
| round-2 | `hooks/worktree-guard.py:2292` | round 2's 🟡 1 — fixed |
| round-2 | `hooks/worktree-guard.py:2470` | round 2's 🟡 2 — fixed |
| round-2 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/survivors.md:24` | round 2's ⬜ 3 — answered |
| round-2 | `hooks/session-lease.py:98` | round 2's ⬜ 4 — fixed |
| round-2 | `hooks/session-lease.py:25` | round 2's ⬜ 5 — fixed |
| round-2 | `tests/test_worktree_guard.py:2199` | round 2's 🟢 — confirmed |
| round-2 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/survivors.md` | round 2's 🟢 — confirmed |
| round-2 | `hooks/worktree-guard.py:2282` | round 2's 🟢 — confirmed |
| round-2 | `hooks/tokens.py:45` | round 2's 🟢 — confirmed |
| round-3 | `hooks/worktree-guard.py:2320` | round 3's 🟡 1 — deferred |
| round-3 | `hooks/worktree-guard.py:2325` | round 3's 🟡 2 — deferred |
| round-3 | `hooks/worktree-guard.py:2392` | round 3's 🟡 3 — deferred |
| round-3 | `tests/test_lease_liveness.py:401` | round 3's ⬜ 4 — deferred |
| round-3 | `hooks/worktree-guard.py:2321` | round 3's ⬜ 5 — deferred |
| round-3 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/rounds/round-2-fixes.md:23` | round 3's ⬜ 6 — deferred |
| round-3 | `tests/test_worktree_guard.py:1933` | round 3's 🟢 — confirmed |
| round-3 | `tests/test_worktree_guard.py:1985` | round 3's 🟢 — confirmed |
| round-3 | `hooks/session-lease.py:102` | round 3's 🟢 — confirmed |
| round-3 | `hooks/session-lease.py:27` | round 3's 🟢 — confirmed |
| round-4 | `hooks/worktree-guard.py:2485` | round 4's 🟡 1 — fixed |
| round-4 | `docs/worktree-guard-spec.md:106` | round 4's 🟡 3 — fixed |
| round-4 | `hooks/worktree-guard.py:2409` | round 4's ⬜ 4 — fixed |
| round-4 | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:86` | round 4's ⬜ 5 — answered |
| round-4 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/rounds/round-2-report.md:85` | round 4's ⬜ 6 — answered |
| round-4 | `tests/test_worktree_guard.py:1937` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_worktree_guard.py:1945` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_worktree_guard.py:1949` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_lease_liveness.py:402` | round 4's 🟢 — confirmed |
| round-4 | `docs/worktree-guard-spec.md:102` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/phases/phase-7.md:38` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/phases/phase-7.md:32` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_worktree_guard.py:1924` | round 4's 🟢 — confirmed |
| round-5 | `hooks/worktree-guard.py:2046` | round 5's 🟡 1 — fixed |
| round-5 | `hooks/worktree-guard.py:2021` | round 5's 🟡 2 — fixed |
| round-5 | `docs/worktree-guard-spec.md:80` | round 5's ⬜ 3 — answered |
| round-5 | `seal/specs/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way/phases/phase-7.md:75` | round 5's ⬜ 4 — answered |
| round-5 | `hooks/worktree-guard.py:2488` | round 5's 🟢 — confirmed |
| round-5 | `docs/worktree-guard-spec.md:116` | round 5's 🟢 — confirmed |
| round-5 | `hooks/worktree-guard.py:2430` | round 5's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The brace class of #856: every spelling rounds 1 to 5 found, now listed and silent as a named limit | #886, by the second reframe; already deferred, not new | the repository owner, through `questions.md` P2 and #886 |
| Whether `reference-transaction`'s first HEAD line for a rebase typed from its onto branch could be refused (🟡 2's fact, as design input) | #886 | the repository owner |
