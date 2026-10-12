# 1791779434-under-automation-the-guard-asks-nobody — review round 3

| Field | Value |
|---|---|
| Target SHA | 4a96d480e32edfe1e6378364db83165ff3a47023 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 897 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `d450c303a97348ca7d7851a49f49ce8a6257a58b..d450c303a97348ca7d7851a49f49ce8a6257a58b`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | second — 🟡 1 at hooks/worktree-guard.py#main, a unit round-2's fixes changed; 🟡 2 at hooks/worktree-guard.py#main, a unit round-2's fixes changed; the fix passes stop here and the work item goes back to its framer |
| Needs a fix | yes — 🟡 1 (under a detached HEAD the deny still offers way 2 to `--orphan`, which conflicts) and 🟡 2 (way 2 promises a carry that stops on a conflict where the target branch changed a listed file) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 3 of #894 (PR #897), verifying round 2's fixes at c67fc2e5..1ac03f4d (`rounds/round-2-fixes.md`). This is the last round: the record that reads these fixes ends the run. Attack in this order:

1. **🟡 1's fix (04f450ea):** way 1 now names `--orphan` as taking the commit way. Is the text now right for every switch form under the press? Cover plain, `-c`/`-C`/`--create`/`--force-create`, `--orphan`, `--detach`, `-f`/`--discard-changes`, `-m`/`--merge`, and `-` (the previous branch). For each one, the way the deny names must succeed with real git through the guard and lose nothing.
2. **🟡 2's fix (8c1db4bd):** the premise now reads "a switch that keeps them carries them onto the target branch". Check it in both languages, check that the attended `ask` is still byte-identical to c38f97d7 (S2), and check that the new case covers the three discarding forms.
3. **⬜ 3 (1ac03f4d):** the W9 re-read row is back at `main@08a308fb`. Check that no other row of the 1791384157 fragment was changed wrongly by the fix pass's re-stamps.
4. **S8** still holds.
5. **Depth:** the two new units are depth 1.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Under a detached HEAD the deny's way 1 still offers way 2, without excluding `--orphan`, and there the pop ends `DU f.txt` with the stash kept | `hooks/worktree-guard.py:3307` | deferred the frame | the frame — the second fix of a fix, in the deny's way 1 text: on a detached HEAD it still offers way 2 without excluding `--orphan`; the framer redesigns what the deny prescribes; Executed: from a detached HEAD, stash, `--orphan` switch and pop are each silent at the guard; the pop exits 1 with `DU f.txt` and the stash kept. Read: the offer predates the range, and 04f450ea's sentence three lines up sends `--orphan` to way 1 |
| 🟡 2 | Way 2 says the pop carries the changes onto the target branch; where that branch changed a listed file, the pop stops on a conflict and keeps the stash, where git's own switch refuses | `hooks/worktree-guard.py:3310` | deferred the frame | the frame — the second fix of a fix, in the deny's way 2 text: a target branch that changed the same file makes the pop stop in a conflict; the framer redesigns what the deny prescribes; Executed: `feature/x` changes `f.txt`; stash and switch are silent and succeed; the pop exits 1 with `UU f.txt` on `feature/x` and the stash kept. Read: text from c68fa49b, outside the range |
| 🟢 | round 2's first finding is closed — `--orphan` is sent to way 1 in both languages, and way 1 succeeds from a branch | `hooks/worktree-guard.py:3300` | confirmed | Executed: deny under the press, commit then `--orphan` switch silent at the guard, change on the old branch, tree clean; the new case fails against `c67fc2e5`'s hook and passes at the target |
| 🟢 | round 2's second finding is closed — the premise says a switch that keeps the changes carries them, in both languages and the policy | `hooks/worktree-guard.py:3287` | confirmed | Executed: the new case covers `--discard-changes`, `-f` and `--orphan`, fails against `c67fc2e5`'s hook and passes at the target. Read: the Korean premise carries the same condition |
| 🟢 | round 2's note 3 is closed — W9's re-read row is back at `main@08a308fb`, and every other change to the fragment is a hash move | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31` | confirmed | Read: word diff shows only `main` and §Decision matrix hashes changed. Executed: `evidence-check --strict` 0 drifted |
| 🟢 | S2: the attended `ask` is byte-identical to the base | `hooks/worktree-guard.py:3343` | confirmed | Executed: block comparison identical, 654 characters; both S2 cases pass at the target |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --stat` printed nothing, exit 0 |
| 🟢 | The fix range's two new units are depth 1 | `tests/test_the_guard_asks_once_per_session.py#test_an_orphan_switch_under_the_press_takes_the_commit_way` | confirmed | Read: the only two definitions added; the findings they pin sit in `main`, which predates the run |
| 🟢 | Every other switch form succeeds and loses nothing by each way the deny names — the creating family, an existing branch under `-C`, `--detach`, `-f`, `--discard-changes`, `-m`, `-`, and a plain switch from a detached HEAD | `hooks/worktree-guard.py:3296` | confirmed | Executed: each form denies with the premise; every step of both ways is silent at the guard; git leaves the change committed or in the tree with no stash left |

## Paste-ready fixes

```python
                    f"the commit lands on no branch: name it with `{git} branch "
                    "<name>` before the switch, or take way 2 unless the switch "
                    "is to `--orphan`.\n"
```
```python
                    f"`{git} branch <name>` 으로 이름을 붙이거나, `--orphan` "
                    "전환이 아니면 2번을 택하세요.\n"
```
```python
            "the commit lands on no branch: name it with `git branch <name>` "
            "before the switch, or take way 2 unless the switch is to "
            "`--orphan`.\n"
```
```python
        "어느 브랜치에도 남지 않습니다. 전환 전에 `git branch <name>` 으로 이름을 "
        "붙이거나, `--orphan` 전환이 아니면 2번을 택하세요.\n"
```
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
```markdown
nothing) and `git branch <name>` before the switch, and offers the stash
sequence there only to a switch that is not to `--orphan`. Where the target
branch changed a listed file the pop stops on a conflict and keeps the stash,
the state in which git's own switch refuses, and the reason says so. It names
no question tool, and says re-issuing the command unchanged meets the same
refusal. Each way on is a command of its own because the guard reads the tree
before a line runs, so `git stash && git switch x` meets this same row.
```
```
, tests/test_the_guard_asks_once_per_session.py::test_a_detached_orphan_switch_is_not_offered_the_stash_way, tests/test_the_guard_asks_once_per_session.py::test_the_deny_says_a_pop_onto_a_branch_that_changed_the_file_conflicts
```

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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `hooks/worktree-guard.py:3296` | round 1's 🟡 1 — fixed |
| round-1 | `hooks/worktree-guard.py:3299` | round 1's 🟡 2 — fixed |
| round-1 | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31` | round 1's ⬜ 3 — answered |
| round-1 | `skills/implement/orchestration.md:291` | round 1's ⬜ 4 — answered |
| round-1 | `hooks/worktree-guard.py:3288` | round 1's ⬜ 5 — answered |
| round-1 | `hooks/worktree-guard.py:3282` | round 1's 🟢 — confirmed |
| round-1 | `hooks/worktree-guard.py:3292` | round 1's 🟢 — confirmed |
| round-1 | `hooks/worktree-guard.py:3308` | round 1's 🟢 — confirmed |
| round-1 | `hooks/commit-review-gate.py` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md:9` | round 1's 🟢 — confirmed |
| round-1 | `skills/implement/orchestration.md:301` | round 1's 🟢 — confirmed |
| round-2 | `hooks/worktree-guard.py:3298` | round 2's 🟡 1 — fixed |
| round-2 | `hooks/worktree-guard.py:3287` | round 2's 🟡 2 — fixed |
| round-2 | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md:18` | round 2's 🟢 — confirmed |
| round-2 | `skills/implement/orchestration.md:293` | round 2's 🟢 — confirmed |
| round-2 | `hooks/worktree-guard.py:3338` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_the_guard_asks_once_per_session.py#test_a_creating_switch_under_the_press_takes_the_stash_way` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
