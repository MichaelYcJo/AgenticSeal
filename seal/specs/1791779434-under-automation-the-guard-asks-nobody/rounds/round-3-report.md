# Round 3 report — 1791779434, under automation the guard asks nobody (#894)

Target `4a96d480`, base `origin/release/v0.21.0` at `c38f97d7`, fix range
`c67fc2e5..1ac03f4d`. This is the verifying round for round 2's fixes and the
run's last round. It read rounds 1 and 2 (records, reports, fix tables) for
coordinates and re-derived every verdict at the target.

## The shape of what was found

Round 2's three items are closed. Two new findings come from walking every
switch form through both ways the deny names, and both have the same cause:
the deny says what way 2 does without saying where it stops.

```
round 2, yellow 1 closed: --orphan is sent to way 1, and way 1 succeeds
   │
   └─ 🟡 1  under a detached HEAD, way 1's own sentence still offers way 2,
            and for --orphan that pop ends in the same DU conflict
            (the offer predates the range; 04f450ea made it contradict)

round 2, yellow 2 closed: the premise is true in both languages
   │
   └─ 🟡 2  way 2 says the pop "carries them onto the target branch";
            where that branch changed the same file it stops on a UU
            conflict instead (text from c68fa49b, missed by rounds 1 and 2)
```

Nothing is lost in either case: the stash is kept both times. The rest
stands. The attended `ask` is byte-identical to the base, S8 holds, the
ledger fragment's re-stamps are hash moves only, and both new units are
depth 1.

## The five questions, in the order asked

### 1. Round 2's yellow 1 fix (04f450ea): every switch form under the press

Executed in a scratch clone at the target with a one-file `test_tmp_` probe,
since deleted. For each form the tree was dirty (`M f.txt`), the press was
in the transcript, and each command of each way went through the guard's
`main` before real git ran it. Sixteen setups, two ways each:

| Form | Deny | Way 1 (commit, switch) | Way 2 (stash, switch, pop) |
|---|---|---|---|
| plain `feature/x` | yes | clean, change on the old branch | clean, `M f.txt` on `feature/x` |
| plain, `feature/x` changed `f.txt` | yes | clean | **pop exits 1, `UU f.txt`, stash kept** (🟡 2) |
| `-c`, `-C newb`, `--create`, `--force-create` | yes | clean, change on old branch and `newb` | clean, `M f.txt` on `newb` |
| `-C feature/x` (existing branch) | yes | clean | clean |
| `--orphan newb` | yes | **clean, change committed on the old branch** | pop exits 1, `DU f.txt`, stash kept |
| `--orphan newb`, HEAD detached | yes | clean once the commit is named | **pop exits 1, `DU f.txt`, stash kept** (🟡 1) |
| `--detach feature/x` | yes | clean | clean, `M f.txt` on the detached HEAD |
| `-f`, `--discard-changes` | yes | clean, nothing lost | clean, `M f.txt` carried |
| `-m feature/x` | yes | clean | clean |
| `--merge`, `feature/x` changed `f.txt` | yes | clean | pop exits 1, `UU f.txt`, stash kept |
| `-` (previous branch) | yes | clean, lands on `feature/x` | clean, lands on `feature/x` |
| plain, HEAD detached | yes | clean once the commit is named | clean |

Every guard verdict along every way was silent. Every deny carried the new
premise.

The fix holds where it was aimed. `--orphan` from a branch now reads *takes
this way*, and way 1 leaves the change committed on the branch being left
and the orphan switch clean. `git stash` does not move `@{-1}`, so `-`
reaches the same branch by both ways.

Two cells are wrong, and they are 🟡 1 and 🟡 2. The `--merge` cell is a
conflict too, but there it is what the user asked for: `git switch -m`
alone produces the same conflict.

A note on the detached rows. My first probe ran `git branch keep` before the
commit, and the change ended on no branch. The deny says *the commit lands on
no branch: name it*, so *it* is the commit and the order was mine. With the
commit first, `keep` holds the change for both plain and `--orphan`.

### 2. Round 2's yellow 2 fix (8c1db4bd): the premise

- **English, `hooks/worktree-guard.py:3287`**: *a switch that keeps them
  carries them onto the target branch*. Read: true for every form the table
  marks clean, and it makes no claim about `-f`, `--discard-changes` or
  `--orphan`.
- **Korean, `hooks/worktree-guard.py:3315`**: *변경을 유지하는 전환이면 이
  변경이 대상 브랜치로 따라갑니다*. Read: the same condition, in the same
  place.
- **Policy, `docs/worktree-guard-spec.md` §A**: it says the reason states
  only that a switch that keeps the changes carries them, and why. Read.
- **S2**: executed. The `respond("ask", …)` block at `c38f97d7` and at the
  target is identical, 654 characters each. Also executed:
  `tests/test_worktree_guard.py#test_the_dirty_tree_row_names_what_was_measured`
  and `tests/test_worktree_guard.py#test_switch_dirty_single_asks` pass at
  the target.
- **The new case** covers `--discard-changes`, `-f` and `--orphan` and
  asserts that `would follow` is absent and the new premise is present.
  Executed: it fails against `c67fc2e5`'s hook on the `would follow`
  assertion, and it passes at the target.

Closed.

### 3. Round 2's note 3 (1ac03f4d): the 1791384157 fragment's re-stamps

Read with `git diff --word-diff=porcelain c67fc2e5..1ac03f4d`. The only
tokens that change are coordinate hashes:

- The guard's `main` moves from hash d88d26b8 to 9ff50c27 on S3,
  Corrected · W7, the re-reads of A5, W2, W4, Corrected · R6, Corrected · W10,
  S8, S12, F1, F7, F8 and the writer-property row.
- The policy's §*Decision matrix* moves from hash 6280e33a to 92db2240 on
  S25, S27 and the R3 re-read.
- W9's re-read goes from `main` at c6554e10 back to `main` at 08a308fb.

No claim text, date or result cell changed. Executed: `bin/evidence-check
--strict` over the clone reports 239 ok and 0 drifted for this fragment,
and 0 drifted across 8328 rows in all. The superseded W9 row is not counted
as drift because `Corrected · W9` supersedes its family.

Read: the re-stamped rows whose claims touch the tracked-changes row are W4,
S27 and R3. None of them reads differently against the fix range's text. W4's
*the verdict is unchanged* has its own note in this item's fragment (line 14),
which round 1 accepted. S27 asks only that §A hold no brace rule. R3's
sentence is untouched. Closed.

### 4. S8

Executed: `git diff --stat c38f97d7 4a96d480 -- hooks/commit-review-gate.py
hooks/worktree_consent.py hooks/cmdline_base.py` printed nothing, exit 0.
Holds.

### 5. Depth

Read: the fix range adds two top-level definitions, both in the test module:
`tests/test_the_guard_asks_once_per_session.py#test_an_orphan_switch_under_the_press_takes_the_commit_way` (NAME NOT IN TREE since the reframe)
and
`tests/test_the_guard_asks_once_per_session.py#test_the_deny_does_not_say_a_discarding_switch_carries_the_changes` (NAME NOT IN TREE since the reframe).
The findings they pin are located in `hooks/worktree-guard.py#main`, which
predates the run. Neither sits inside round 1's new unit. Both are depth 1,
as `round-2.md` records.

## 🟡 1 — Under a detached HEAD the deny still offers way 2 to `--orphan`

`hooks/worktree-guard.py:3307` (Korean at line 3333). Way 1 now says *a
switch to `--orphan` … takes this way*. Three sentences later the same
paragraph says *where HEAD is detached … name it with `git branch <name>`
before the switch, or take way 2*. That offer does not exclude `--orphan`.

Executed: from a detached HEAD with `M f.txt`, `git stash`, `git switch
--orphan newb` and `git stash pop` are each silent at the guard. The pop
then exits 1, the tree is `DU f.txt` on `newb`, and the stash is kept. This
is exactly the outcome round 2's 🟡 1 was opened for, reached through the
other sentence.

Why it matters: in a run nobody is watching, the model is choosing among the
sentences of this reason. The only part of the text that addresses its state
(detached) names a way that leaves it in a conflict. Nothing is lost, since
the stash is kept, but the fix round 2 asked for is incomplete.

Location and depth: the offer predates the fix range. 04f450ea's new
sentence is what makes it contradictory. The finding is in `main`, which
round 2's fixes changed.

## 🟡 2 — Way 2 promises a carry that stops on a conflict where the target changed the file

`hooks/worktree-guard.py:3310` (Korean at line 3337). Way 2 says *after the
switch it carries them onto the target branch*. Where the target branch
changed a file in the listing, git's own `git switch` refuses with *would be
overwritten*. Way 2 gets past that refusal, because the stash leaves a clean
tree.

Executed: with `feature/x` committing a different `f.txt`, `git stash` and
`git switch feature/x` are silent and succeed. `git stash pop` exits 1 and
leaves `UU f.txt` with conflict markers on `feature/x`, and the stash is
kept.

Why it matters: this is the common case of the two, since switching to a
branch that touched the same file happens all the time. Attended, the person
approves the `ask` and git refuses, so nothing moves. Under the press, a
model that wants the changes on the target takes way 2, because way 1 leaves
them behind. It is then left on another branch with a conflicted tree, and
the reason told it the opposite. Nothing is lost, since the stash is kept.

Location: the sentence is from c68fa49b, this item's own first commit, so it
predates the fix range. Rounds 1 and 2 checked way 2 only on a fixture where
`feature/x` equals the base. I report it here because this round was asked
to cover the plain switch.

## Regression tests to plant

Both cases are in the fences under `## Paste-ready fixes` and go into
`tests/test_the_guard_asks_once_per_session.py`, after the
discarding-switch case. Executed in a scratch clone: both fail against the
target's hook on their sentence assertion, and both pass with the fixes
applied.

- 🟡 1: a detached HEAD, `--orphan`, the reason excludes it from the offer,
  and way 1 with the commit named leaves the change on the named branch.
- 🟡 2: `feature/x` changes `f.txt`, the reason says the pop stops, and way 2
  run with real git ends `UU f.txt` with the stash kept.
- `docs/worktree-guard-spec.md`: the `Enforced by:` line of the
  tracked-changes row takes both.

## Facts for the evidence ledger

- With git 2.50.1, `git stash pop` onto a branch that changed a stashed file
  exits 1, leaves `UU`, and keeps the stash (executed). Onto an orphan branch
  it leaves `DU` (executed, detached HEAD and attached).
- `git stash` writes no `checkout:` reflog entry, so `git switch -` after it
  reaches the same branch (executed).
- After the fixes land, `main`'s hash moves again. The `--reverify --into`
  pass that follows has to leave 0.15.6 W9's re-read row at `main@08a308fb`,
  which is round 2's note 3 not repeated.

## Not verified

- The full suite, the repository-wide lint and the typecheck: unverified.
  The sealer runs them once, after the rounds settle.
- The proposed fixes were run against the four modules named under
  `## Executed probes` and nothing wider. The orchestrator answers whether
  they land before the sealer runs.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Under a detached HEAD the deny's way 1 still offers way 2, without excluding `--orphan`, and there the pop ends `DU f.txt` with the stash kept | `hooks/worktree-guard.py:3307` | open | Executed: from a detached HEAD, stash, `--orphan` switch and pop are each silent at the guard; the pop exits 1 with `DU f.txt` and the stash kept. Read: the offer predates the range, and 04f450ea's sentence three lines up sends `--orphan` to way 1 |
| 🟡 2 | Way 2 says the pop carries the changes onto the target branch; where that branch changed a listed file, the pop stops on a conflict and keeps the stash, where git's own switch refuses | `hooks/worktree-guard.py:3310` | open | Executed: `feature/x` changes `f.txt`; stash and switch are silent and succeed; the pop exits 1 with `UU f.txt` on `feature/x` and the stash kept. Read: text from c68fa49b, outside the range |
| 🟢 | round 2's first finding is closed — `--orphan` is sent to way 1 in both languages, and way 1 succeeds from a branch | `hooks/worktree-guard.py:3300` | confirmed | Executed: deny under the press, commit then `--orphan` switch silent at the guard, change on the old branch, tree clean; the new case fails against `c67fc2e5`'s hook and passes at the target |
| 🟢 | round 2's second finding is closed — the premise says a switch that keeps the changes carries them, in both languages and the policy | `hooks/worktree-guard.py:3287` | confirmed | Executed: the new case covers `--discard-changes`, `-f` and `--orphan`, fails against `c67fc2e5`'s hook and passes at the target. Read: the Korean premise carries the same condition |
| 🟢 | round 2's note 3 is closed — W9's re-read row is back at `main@08a308fb`, and every other change to the fragment is a hash move | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31` | confirmed | Read: word diff shows only `main` and §Decision matrix hashes changed. Executed: `evidence-check --strict` 0 drifted |
| 🟢 | S2: the attended `ask` is byte-identical to the base | `hooks/worktree-guard.py:3343` | confirmed | Executed: block comparison identical, 654 characters; both S2 cases pass at the target |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --stat` printed nothing, exit 0 |
| 🟢 | The fix range's two new units are depth 1 | `tests/test_the_guard_asks_once_per_session.py#test_an_orphan_switch_under_the_press_takes_the_commit_way` | confirmed | Read: the only two definitions added; the findings they pin sit in `main`, which predates the run (removed at the reframe after round 3: NAME NOT IN TREE) |
| 🟢 | Every other switch form succeeds and loses nothing by each way the deny names — the creating family, an existing branch under `-C`, `--detach`, `-f`, `--discard-changes`, `-m`, `-`, and a plain switch from a detached HEAD | `hooks/worktree-guard.py:3296` | confirmed | Executed: each form denies with the premise; every step of both ways is silent at the guard; git leaves the change committed or in the tree with no stash left |

## Executed probes

| What was run | Result |
|---|---|
| One-file `test_tmp_` probe (deleted) in a scratch clone at `4a96d480`: sixteen setups under the press, each switch form through the guard, way 1 and way 2 run step by step with real git | 34 passed, 14 skipped (the named-commit variant runs only on a detached HEAD); per-cell results in the table under question 1 |
| The detached named-commit variant re-run with the commit before `git branch keep` | 2 passed; `keep` holds the change for plain and `--orphan` |
| Round 2's two new cases against `c67fc2e5`'s hook | exit 1, 2 failed, each on its sentence assertion |
| The two new cases, S1, S3 and the two S2 cases at the target | exit 0, 6 passed |
| Base and target `respond("ask", …)` block comparison | identical, 654 characters |
| `git diff --stat c38f97d7 4a96d480` over the three S8 hooks | no output, exit 0 |
| `bin/evidence-check --strict` over the scratch clone | exit 0, 8328 ok, 0 drifted; the 1791384157 fragment 239 ok |
| Proposed fixes for 🟡 1 and 🟡 2 applied in the scratch clone: `bin/test tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py tests/test_docs_line_wrap.py tests/test_a_folded_statement_names_what_enforces_it.py` | exit 0, 306 passed |
| The two proposed cases against the target's hook | exit 1, 2 failed, each on its sentence assertion |
| The full suite, the repository-wide lint and the typecheck | not yet. Unverified. The sealer runs them once, after the rounds settle |

## Paste-ready fixes

### 🟡 1 — `hooks/worktree-guard.py`, the detached-HEAD offer in both languages

```python
                    f"the commit lands on no branch: name it with `{git} branch "
                    "<name>` before the switch, or take way 2 unless the switch "
                    "is to `--orphan`.\n"
```

```python
                    f"`{git} branch <name>` 으로 이름을 붙이거나, `--orphan` "
                    "전환이 아니면 2번을 택하세요.\n"
```

`tests/test_the_guard_asks_once_per_session.py#dirty_deny`, the same two
sentences:

```python
            "the commit lands on no branch: name it with `git branch <name>` "
            "before the switch, or take way 2 unless the switch is to "
            "`--orphan`.\n"
```

```python
        "어느 브랜치에도 남지 않습니다. 전환 전에 `git branch <name>` 으로 이름을 "
        "붙이거나, `--orphan` 전환이 아니면 2번을 택하세요.\n"
```

The new case, after the discarding-switch case:

```python
def test_a_detached_orphan_switch_is_not_offered_the_stash_way(
    monkeypatch, capsys, projects, repo
):
    """Round 3, yellow 1. Where HEAD is detached the deny offers way 2 beside
    naming the commit, and for `--orphan` way 2's pop meets a modify/delete
    conflict. The offer leaves `--orphan` out, and way 1 with the commit
    named, run with real git, leaves the change on the named branch."""
    write_transcript(projects, "me", ask_entries(repo))
    git_in(repo, "switch", "-q", "--detach", "HEAD")
    dirty(repo)
    decision, reason = decide(monkeypatch, capsys, repo, "git switch --orphan newb")
    assert decision == "deny", reason
    assert "or take way 2 unless the switch is to `--orphan`" in reason, reason
    for command in ("git commit -am x", "git branch keep", "git switch --orphan newb"):
        assert decide(monkeypatch, capsys, repo, command) == ("silent", ""), command
        git_in(repo, *command.split()[1:])
    assert git_in(repo, "branch", "--show-current") == "newb"
    assert git_in(repo, "show", "keep:f.txt") == "changed"
```

### 🟡 2 — `hooks/worktree-guard.py`, way 2's pop in both languages

```python
                    "out when it runs: after the switch it carries them onto "
                    "the target branch, and after a switch back it returns them "
                    "here. Where the target branch changed a file listed above, "
                    "the pop stops on a conflict and keeps the stash.\n\n"
```

```python
                    "변경을 적용합니다. 전환 뒤에 실행하면 변경이 대상 브랜치로 "
                    "가고, 다시 돌아온 뒤에 실행하면 이 브랜치로 돌아옵니다. "
                    "대상 브랜치가 위에 나열된 파일을 바꿨다면 pop 은 충돌에서 "
                    "멈추고 stash 를 남깁니다.\n\n"
```

`tests/test_the_guard_asks_once_per_session.py#dirty_deny`, the same two
sentences:

```python
            "the switch it carries them onto the target branch, and after a "
            "switch back it returns them here. Where the target branch changed "
            "a file listed above, the pop stops on a conflict and keeps the "
            "stash.\n"
```

```python
        "실행하면 변경이 대상 브랜치로 가고, 다시 돌아온 뒤에 실행하면 이 "
        "브랜치로 돌아옵니다. 대상 브랜치가 위에 나열된 파일을 바꿨다면 pop 은 "
        "충돌에서 멈추고 stash 를 남깁니다.\n"
```

The new case:

```python
def test_the_deny_says_a_pop_onto_a_branch_that_changed_the_file_conflicts(
    monkeypatch, capsys, projects, repo
):
    """Round 3, yellow 2. Way 2 onto a branch that changed a listed file ends
    with the pop stopped on a conflict and the stash kept, where git's own
    switch refuses. The deny says so, and the stash is still there."""
    write_transcript(projects, "me", ask_entries(repo))
    here = git_in(repo, "branch", "--show-current")
    git_in(repo, "switch", "-q", "feature/x")
    (repo / "f.txt").write_text("other\n", encoding="utf-8")
    git_in(repo, "commit", "-qam", "diverge")
    git_in(repo, "switch", "-q", here)
    dirty(repo)
    decision, reason = decide(monkeypatch, capsys, repo, "git switch feature/x")
    assert decision == "deny", reason
    assert "the pop stops on a conflict and keeps the stash" in reason, reason
    for command in ("git stash", "git switch feature/x"):
        assert decide(monkeypatch, capsys, repo, command) == ("silent", ""), command
        git_in(repo, *command.split()[1:])
    assert decide(monkeypatch, capsys, repo, "git stash pop") == ("silent", "")
    popped = subprocess.run(
        ["git", "-C", str(repo), "stash", "pop"], capture_output=True, text=True
    )
    assert popped.returncode == 1, popped
    assert git_in(repo, "status", "--porcelain") == "UU f.txt"
    assert git_in(repo, "stash", "list").startswith("stash@{0}")
```

### 🟡 1 and 🟡 2 — `docs/worktree-guard-spec.md` §A, the tracked-changes paragraph

Replaces the four lines from `nothing) and` to `meets this same row.`:

```markdown
nothing) and `git branch <name>` before the switch, and offers the stash
sequence there only to a switch that is not to `--orphan`. Where the target
branch changed a listed file the pop stops on a conflict and keeps the stash,
the state in which git's own switch refuses, and the reason says so. It names
no question tool, and says re-issuing the command unchanged meets the same
refusal. Each way on is a command of its own because the guard reads the tree
before a line runs, so `git stash && git switch x` meets this same row.
```

Appended to that row's `Enforced by:` line:

```
, tests/test_the_guard_asks_once_per_session.py::test_a_detached_orphan_switch_is_not_offered_the_stash_way, tests/test_the_guard_asks_once_per_session.py::test_the_deny_says_a_pop_onto_a_branch_that_changed_the_file_conflicts
```

Needs a fix: yes — 🟡 1 (under a detached HEAD the deny still offers way 2 to `--orphan`, which conflicts) and 🟡 2 (way 2 promises a carry that stops on a conflict where the target branch changed a listed file)
Loses a record or crashes: no

The gate comes due once these two are answered: what comes due is the
sealer's spawn, not a run for the session reading this.

## Proof block

Files opened in this round:

- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-2.md`,
  `round-2-fixes.md`, `round-2-report.md`, `round-1.md` (grep),
  `round-1-report.md` (grep), `spec.md` (S2, S8 lines)
- `hooks/worktree-guard.py` lines 2080–2240, 2460–2500, 3120–3360 at the
  target; the `ask` block at `c38f97d7`; the whole file at `c67fc2e5`
- `tests/test_the_guard_asks_once_per_session.py` lines 40–112, 1193–1275,
  1767–1790, 1800–2070
- `tests/conftest.py` lines 163–180, 870–909
- `docs/worktree-guard-spec.md` lines 30–63
- `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md`
  (diff over the range; rows S27, Corrected · W7, the W4, W9, Corrected · R6,
  Corrected · W10 and R3 re-reads)
- `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` lines
  2, 9, 10, 14, 18
- `seal/releases/0.20.0.md` (Corrected · W10), `seal/releases/0.15.6.md` (W4)
- `skills/code-review/orchestration.md` lines 355–378
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/changelog.md`
  (diff over the range)
