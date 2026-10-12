# Round 2 report — 1791779434, under automation the guard asks nobody (#894)

Target `8fb7eaeb`, base `origin/release/v0.21.0` at `c38f97d7`, fix range
`190b457e..2022f615`. This is the verifying round for round 1's fixes. It
read round 1's record, report and fix table for coordinates, and re-derived
every verdict at the target.

## The shape of what was found

Both of round 1's yellows are closed as far as they reach. One thing ties the
two new findings together: the deny's text assumes that every switch carries
the changes along.

```
round 1, yellow 1 fixed: a switch that creates its branch (-c) is sent to way 2
   │
   ├─ holds for -c, -C, --create, --force-create, -cX, --create=X, -c X <start>
   │
   └─ 🟡 1  --orphan also creates its branch, and way 2 ends in a conflict there
            (the sentence came from the fix, a798c85a)

round 1, note 5 answered: "the would-follow premise is the base's text, word for word"
   │
   └─ 🟡 2  it is not: the deny's sentence is new at c68fa49b, and S2 does not pin it.
            For --discard-changes, -f and --orphan the premise is false
```

The rest stands. Round 1's note 3 and note 4 answers hold. The attended `ask`
is byte-identical to the base. S8 holds. The new unit is depth 1. One
paperwork correction comes out of note 3 (⬜ 3).

## The five questions, in the order asked

### 1. Round 1's yellow 1 fix (a798c85a): is every creating form covered, and is way 2 right for each

Executed, through the guard under the press in a dirty tree, with each step
judged before real git ran it. The forms tested were `git switch -C newb`,
`--create newb`, `--force-create newb`, `-cnewb`, `--create=newb` and
`-c newb feature/x`. Every one meets the deny, and the reason carries the new
sentence. Way 2 (`git stash`, the same switch, `git stash pop`) is silent at
every step for each form, and each run ends on `newb` with `M f.txt` and an
empty stash list. Read: the reason names only `-c` in its parenthesis, but its
condition is "where the switch creates its branch", and that covers all six
forms. That is a fair way to write it.

`--orphan` is the one creating form where way 2 is wrong. That is 🟡 1.

The new case runs way 2 through the guard and not around it. Read: each of
the three commands goes through `decide`, which runs the guard's `main` on
the tree as it stands, and then `git_in` runs that command with real git.
Only `sessions_in_tree` is stubbed, as it is in every case in the module.
Executed: with `hooks/worktree-guard.py` from `1eec0f8e` put back in a scratch
clone, the case fails on the `-c` sentence assertion. So it pins what it
claims.

### 2. Round 1's yellow 2 fix (1eec0f8e): the squash clause

Executed: `git grep -i squash` at the target finds no hit in
`hooks/worktree-guard.py`, `docs/worktree-guard-spec.md`, the changelog
fragment or this item's ledger fragment. The only hits are S1's comment and
assertion in the test module. Read: S1 pins the English text by equality and
also asserts that `squash` is absent. It pins the Korean text by equality
with `dirty_deny("ko", …)`, which no longer carries `squash 됩니다`. Closed.

### 3. The three answered notes

- **Note 3 (W9): the grounds stand.** Read: `Corrected · W9` at
  `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md:18` cites
  the three tests that the fix table names. Its claim matches `main`: attended,
  it asks; under the press read from the session's own root, it denies; a
  clean clone stays silent. Executed: all three cases pass at the target.
  `docs/the-evidence-ledger.md` says that a `Corrected ·` row supersedes the
  family of the row it cites. That makes the stale hash in the re-read row
  inert, but the row still states something false. That is ⬜ 3.
- **Note 4 (the resume paragraph): the grounds stand.** Read:
  `hooks/worktree_consent.py#automation_answered`, condition 4, requires that
  the result entry's own `cwd` is in the same clone as `top`.
  `docs/worktree-guard-spec.md` §*Creation consent* states the same as its
  rule 4 (line 289). The paragraph at `skills/implement/orchestration.md:293`
  says the press is put "from a directory inside the clone the run works in"
  and cites that rule. That is the condition, at the right confidence.
- **Note 5 (the *would follow* premise): the grounds do not stand.** See 🟡 2.

### 4. The attended text is still byte-identical (S2), and S8 holds

Executed: the whole `respond("ask", …)` block, from its opening line to the
`# 4)` comment, is byte-identical at `c38f97d7` and `8fb7eaeb` (654
characters, both languages). Executed: `git diff --stat c38f97d7 8fb7eaeb`
over `hooks/commit-review-gate.py`, `hooks/worktree_consent.py` and
`hooks/cmdline_base.py` prints nothing, exit 0.

### 5. Depth

Read: the fix range adds one function,
`test_a_creating_switch_under_the_press_takes_the_stash_way`. The hook's change
sits inside `main`, which existed before. This is round 1's fix pass, so the
new unit is depth 1, as the record's `New units` row says.

## Findings

### 🟡 1 — `--orphan` creates its branch, and way 2 ends in a conflict there

`hooks/worktree-guard.py:3298` (English) and `:3323` (Korean). Both sentences
were written by round 1's fix, a798c85a.

Executed: under the press, `git switch --orphan newb` in a dirty tree meets
the deny. Its new sentence sends "a switch that creates its branch" to way 2.
Run through the guard, way 2 goes like this:

- `git stash` is silent and saves the change.
- `git switch --orphan newb` is silent and succeeds, leaving an empty tree.
- `git stash pop` exits 1 with `CONFLICT (modify/delete): f.txt deleted in
  Updated upstream and modified in Stashed changes`. The tree ends at
  `DU f.txt` and the stash entry is kept.

Nothing is lost, because the stash stays. But the model followed the text
exactly and landed in a conflict on an unborn branch, which it then has to
untangle with nobody to ask. Executed, without the guard: git refuses
`git switch --orphan newb` over a modified tracked file (`Your local changes
… would be overwritten`). So the base never moved changes onto an orphan
either. The right way is way 1. Executed with the proposed fix applied:
`git commit -am x` and then `git switch --orphan newb` are both silent, the
switch succeeds, and the change stays committed on the branch it was made on.

Why it is 🟡: the release would ship a sentence whose plain reading sends one
creating form into a conflict.

### 🟡 2 — The deny says the changes would follow, which is false for a discarding switch, and round 1's grounds for leaving it do not hold

`hooks/worktree-guard.py:3287` (English) and `:3312` (Korean). This text was
written in phase 1, at c68fa49b.

Round 1's fix table answered note 5 with this: "the *would follow* premise …
is the base's `ask` text, carried word for word; the attended text is pinned
byte-identical to the base (S2), so rewording it is a change to both readers."
I checked each part of that against the code:

- **"Carried word for word".** Executed: `would follow` does not occur
  anywhere in the base's `hooks/worktree-guard.py`, and neither does `switch
  itself may go ahead`. The base's `ask` says *They will follow you onto the
  target branch*, after the listing. The deny says *and they would follow it
  onto the target branch*, before it. The premise came from the base. The
  sentence is this item's own.
- **"Rewording it is a change to both readers".** Read: `spec.md` S2 pins
  only the case without the press, and the deny is its own string inside
  `tr(...)`. Executed (question 4): the `ask` block is untouched. So the deny
  can be reworded without moving a byte of the attended text.

What stays wrong, executed: under the press, `git switch --discard-changes
feature/x`, `git switch -f feature/x` and `git switch --orphan newb` each meet
the deny, which tells the model its changes would follow. With
`--discard-changes` and `-f` git drops them. With `--orphan` git refuses the
switch. For `-m` the sentence holds, because git merges the changes onto the
target. A model that meant to drop the changes is then given only ways that
keep them, and way 1 commits them onto the branch under review.

Why it is 🟡: the deny states a false fact about the model's own command, and
the action it points to puts a commit on a reviewed branch. The fix rewords
only the premise and leaves the attended `ask` byte-identical, so S2 still
holds.

### ⬜ 3 — 0.15.6 W9's re-read row still says the claim holds at a hash where it did not (correction)

`seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31`.

Read: phase 1's ledger commit, 8bdd6680, moved this row's hash from
`main@08a308fb` to `main@c6554e10`. The deny already existed at that hash,
yet the row kept its *the cited row's claim holds*. The fix pass then added
`Corrected · W9`, which supersedes the family, and `--reverify` left this row
at `c6554e10` (15 rows moved to `d88d26b8`; this one did not). The checker no
longer reads it, so nothing fails. But a reader who opens this fragment sees a
reading that says *asks* held at a hash where it held only without the press.
The two neighbouring rows that this item also corrected, A4 at line 27 and S2
at line 58, still carry the base's `08a308fb`, where their claims did hold.
Putting W9 back to `08a308fb` makes the three rows consistent. This is a
record correction, so `Needs a fix` does not count it.

## Axes walked

- **Spec compliance.** S1, S2 and S8 were re-derived at the target (above).
  S4 (the ways on pass) was extended to every creating form, executed, and
  `--orphan` is the exception (🟡 1).
- **Class (§12).** The class is "the deny names a way that does not do what
  the text says for some switch form". Enumerated across `git switch` options
  that create (`-c`, `-C`, `--create`, `--force-create`, `--orphan`, attached
  and `=` spellings, with a start point) and options that do not carry
  (`--discard-changes`, `-f`, `-m`). The two findings are the two members
  found. `git checkout -b` never reaches this row, because it is
  unrecognised and meets the stop (read: `_git_finding`).
- **Failure direction.** Both findings fail toward an extra turn or a
  conflict the model can recover from. Neither loses a change, and neither
  crashes.

## Regression tests to plant

- `tests/test_the_guard_asks_once_per_session.py`: an orphan case (deny
  names `--orphan`, then way 1 through the guard with real git), and a
  discarding-switch case (no `would follow` for `--discard-changes`, `-f`
  and `--orphan`). Both are fenced under 🟡 1 and 🟡 2 below. Executed in a
  scratch clone: both fail against the target's hook on their first
  assertion, and both pass with the fix applied.
- `docs/worktree-guard-spec.md`: the `Enforced by:` line of the
  tracked-changes row takes the two new cases.

## Facts for the evidence ledger

- The deny's premise is this item's text, not the base's. The base's
  `ask` block is byte-identical at the target (executed). Whoever writes S1's
  ledger row after the fix should cite the reworded premise.
- `--orphan` over a modified tracked file is refused by git 2.50.1 (executed).
  Under the press, the deny is what the model sees first.

## Not verified

- The full suite, the repository-wide lint and the typecheck: unverified.
  The sealer runs them once, after the rounds settle.
- `bin/evidence-check . --strict` at the target was not run in this round.
  It is a whole-repository check, and the fix pass's re-stamps are the
  sealer's to judge. The orchestrator answers whether it runs before the
  sealer.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `git switch --orphan` creates its branch, so the fix's new sentence sends it to way 2, and there the pop meets a modify/delete conflict and keeps the stash | `hooks/worktree-guard.py:3298` | open | Executed: deny under the press; way 2 through the guard ends `DU f.txt` with the stash kept; git alone refuses `--orphan` over the change; way 1 is silent and succeeds with the proposed fix. The sentence came from a798c85a |
| 🟡 2 | The deny says the changes would follow, which is false for `--discard-changes`, `-f` and `--orphan`; round 1's grounds for note 5 (base text word for word, pinned by S2) do not hold | `hooks/worktree-guard.py:3287` | open | Executed: `would follow` and `switch itself may go ahead` are absent from the base's hook, and the base's `ask` block is byte-identical at the target. Read: S2 pins only the unpressed case. Executed: all three forms meet the deny with the premise |
| ⬜ 3 | 0.15.6 W9's re-read row still says the claim holds at `main@c6554e10`, a hash where it held only without the press | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31` | open | Read: 8bdd6680 moved the hash; `Corrected · W9` supersedes the family, so the row is inert but false; A4 (line 27) and S2 (line 58) keep the base's `08a308fb`. A record correction, so `Needs a fix` does not count it |
| 🟢 | round 1's yellow 1 is closed for every creating form except `--orphan` — `-c`, `-C`, `--create`, `--force-create`, `-cX`, `--create=X`, `-c X <start>` | `hooks/worktree-guard.py:3296` | confirmed | Executed: each meets the deny with the sentence, and way 2 through the guard ends on `newb` with `M f.txt` and no stash; the new case fails against 1eec0f8e's hook |
| 🟢 | round 1's yellow 2 is closed — no squash clause in either language | `hooks/worktree-guard.py:3296` | confirmed | Executed: `git grep -i squash` hits only S1's own comment and assertion. Read: the Korean text is pinned by equality |
| 🟢 | round 1's note 3 answer holds — `Corrected · W9` states what `main` does and its three tests pass | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md:18` | confirmed | Executed: the three cited cases pass at the target. Read: the claim against `main` |
| 🟢 | round 1's note 4 answer holds — the resume paragraph states `automation_answered`'s condition 4 | `skills/implement/orchestration.md:293` | confirmed | Read: `hooks/worktree_consent.py#automation_answered` condition 4 and §*Creation consent* rule 4 |
| 🟢 | S2: the attended `ask` is byte-identical to the base in both languages | `hooks/worktree-guard.py:3338` | confirmed | Executed: block comparison, identical |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --stat` printed nothing, exit 0 |
| 🟢 | The fix range's one new unit is depth 1 | `tests/test_the_guard_asks_once_per_session.py#test_a_creating_switch_under_the_press_takes_the_stash_way` | confirmed | Read: the only function added in the range; the hook change sits in `main` |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_the_guard_asks_once_per_session.py` plus the two W9 cases of `tests/test_guard_resolves_the_tree_it_judges.py`, in a scratch clone at `8fb7eaeb` | exit 0, 87 passed |
| The new case against 1eec0f8e's `hooks/worktree-guard.py`, in the scratch clone | exit 1, fails on the `-c` sentence assertion |
| One-file test_tmp probe (deleted): under the press, dirty tree, ten switch forms through the guard, and way 2 run step by step with real git | every form denies with the premise and the sentence; way 2 is clean for the six `-c`-family forms; for `--orphan` the pop exits 1 with `DU f.txt` and the stash kept |
| The same probe, git alone over a dirty tree | five creating forms succeed carrying `M f.txt`; `--orphan` exits 1, `would be overwritten` |
| Base and target `respond("ask", …)` block comparison | identical, 654 characters |
| `git diff --stat c38f97d7 8fb7eaeb` over the three S8 hooks | no output, exit 0 |
| `git grep -i squash` at the target over the hook, the policy, the test module, the changelog and the ledger fragment | only S1's comment and assertion |
| Proposed fixes for 🟡 1 and 🟡 2 applied in the scratch clone: `bin/test tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py` | exit 0, 231 passed |
| The two proposed cases against the target's hook | exit 1, 2 failed, each on its first assertion |
| `bin/test tests/test_docs_line_wrap.py tests/test_a_folded_statement_names_what_enforces_it.py` with the proposed policy edit | exit 0, 73 passed |
| The full suite, the repository-wide lint and the typecheck | not yet. Unverified. The sealer runs them once, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Paste-ready fixes

### 🟡 1 and 🟡 2 — `hooks/worktree-guard.py`, the deny in both languages

```python
                    f"{lead}, so the switch itself may go ahead — but there are "
                    f"{len(entries)} uncommitted tracked changes, and a switch "
                    "that keeps them carries them onto the target branch:\n"
                    f"{listing}\n{note}\n"
```
```python
                    "out now, so where the switch creates its branch (`-c`) to "
                    "carry them there, take way 2. A switch to `--orphan` starts "
                    "from an empty tree that nothing carries onto, so it takes "
                    "this way. On a branch a `routing.md` "
                    "declares, "
```
```python
                    f"{lead} 전환 자체는 진행할 수 있지만, 커밋되지 않은 변경 "
                    f"{len(entries)}건이 있고 변경을 유지하는 전환이면 이 변경이 "
                    f"대상 브랜치로 따라갑니다:\n{listing}\n{note}\n"
```
```python
                    "전환이면 2번을 택하세요. `--orphan` 전환은 빈 트리에서 "
                    "시작해 변경이 따라갈 곳이 없으므로 이 방법을 택하세요. "
                    "`routing.md` 가 선언한 브랜치에서는 "
```

### 🟡 1 and 🟡 2 — `tests/test_the_guard_asks_once_per_session.py`, `dirty_deny` and two cases

```python
            "uncommitted tracked changes, and a switch that keeps them carries "
            "them onto the target branch:\n"
```
```python
            "2. A switch to `--orphan` starts from an empty tree that nothing "
            "carries onto, so it takes this way. On a branch a `routing.md` "
            "declares, the commit gate is "
```
```python
        "변경을 유지하는 전환이면 이 변경이 대상 브랜치로 따라갑니다:\n"
```
```python
        "택하세요. `--orphan` 전환은 빈 트리에서 시작해 변경이 따라갈 곳이 "
        "없으므로 이 방법을 택하세요. "
        "`routing.md` 가 선언한 브랜치에서는 커밋 게이트가 이 커밋을 "
```
```python
def test_an_orphan_switch_under_the_press_takes_the_commit_way(
    monkeypatch, capsys, projects, repo
):
    """Round 2, yellow 1. `--orphan` creates its branch from an empty tree, so
    way 2's pop meets a modify/delete conflict there and keeps the stash. The
    reason sends it to way 1, and way 1, run with real git, leaves the change
    committed on the branch it was made on and the orphan switch clean."""
    write_transcript(projects, "me", ask_entries(repo))
    dirty(repo)
    here = git_in(repo, "branch", "--show-current")
    decision, reason = decide(monkeypatch, capsys, repo, "git switch --orphan newb")
    assert decision == "deny", reason
    assert "`--orphan` starts from an empty tree" in reason, reason
    for command in ("git commit -am x", "git switch --orphan newb"):
        assert decide(monkeypatch, capsys, repo, command) == ("silent", ""), command
        git_in(repo, *command.split()[1:])
    assert git_in(repo, "branch", "--show-current") == "newb"
    assert git_in(repo, "show", f"{here}:f.txt") == "changed"


def test_the_deny_does_not_say_a_discarding_switch_carries_the_changes(
    monkeypatch, capsys, projects, repo
):
    """Round 2, yellow 2. `--discard-changes` and `-f` drop the changes and
    git refuses `--orphan` over them, so the deny says only that a switch that
    keeps them carries them."""
    write_transcript(projects, "me", ask_entries(repo))
    dirty(repo)
    for command in (
        "git switch --discard-changes feature/x",
        "git switch -f feature/x",
        "git switch --orphan newb",
    ):
        decision, reason = decide(monkeypatch, capsys, repo, command)
        assert decision == "deny", (command, reason)
        assert "would follow" not in reason, (command, reason)
        assert "a switch that keeps them carries them" in reason, (command, reason)
```

### 🟡 1 and 🟡 2 — `docs/worktree-guard-spec.md`, the tracked-changes paragraph

```markdown
branch (`-c`) to carry them there to the stash sequence. A switch to
`--orphan` starts from an empty tree that no pop carries them onto, so the
reason sends it to the commit. It says only that a switch that keeps the
changes carries them, because `--discard-changes` and `-f` drop them and git
refuses `--orphan` over them. Where HEAD is
```

Append to the row's `Enforced by:` line:

```
, tests/test_the_guard_asks_once_per_session.py::test_an_orphan_switch_under_the_press_takes_the_commit_way, tests/test_the_guard_asks_once_per_session.py::test_the_deny_does_not_say_a_discarding_switch_carries_the_changes
```

The changelog fragment's item 1 follows:

```markdown
     is checked out when it runs, so a switch that creates its branch (`-c`)
     to carry them there is sent this way, and a switch to `--orphan` is
     sent to the commit. A detached HEAD is
```

### ⬜ 3 — the W9 re-read row's hash

```
`hooks/worktree-guard.py#main@08a308fb`
```

This goes in place of `main@c6554e10` on line 31 of the 1791384157 fragment,
as A4 and S2 stand.

Needs a fix: yes — 🟡 1 (`--orphan` is sent to way 2 and ends in a conflict) and 🟡 2 (the deny's *would follow* premise is false for a discarding switch, and round 1's grounds for leaving it do not hold)
Loses a record or crashes: no

## Proof block

Files opened at `8fb7eaeb`:

- `hooks/worktree-guard.py`: the module docstring's command-matching
  paragraph, `_git_finding`, and `main` from row 3 to the end of the ladder
- `hooks/worktree_consent.py`: `automation_answered`
- `tests/test_the_guard_asks_once_per_session.py`: the header, `decide`,
  `projects`, `dirty`, `git_in`, `dirty_deny`, S1, and
  `test_a_creating_switch_under_the_press_takes_the_stash_way`
- `tests/conftest.py`: `_build_repo`, `repo`
- `docs/worktree-guard-spec.md`: the tracked-changes paragraph and its
  `Enforced by:` line, §*Creation consent* rule 4
- `docs/the-evidence-ledger.md`: the paragraphs on `Corrected ·` families and
  `--reverify --into`
- `skills/implement/orchestration.md`: the resume paragraph
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/`: `spec.md`
  S1 to S11, `changelog.md`, `rounds/round-1.md`, `rounds/round-1-report.md`
  (headings, note 5, proof block), `rounds/round-1-fixes.md`
- `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` line 18,
  and `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md`
  lines 27, 31 and 58
- the fix range's diff `190b457e..2022f615`, and the round brief the
  orchestrator wrote for this round
