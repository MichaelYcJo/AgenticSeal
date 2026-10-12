# 1791779434-under-automation-the-guard-asks-nobody — review round 1

| Field | Value |
|---|---|
| Target SHA | c0fbf89cbd23b6b0102b876b855ba1f9ae5d9899 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 897 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `190b457ef1fd3cad070975eac4b1bc5c07cdd0f9..2022f615507048d7461cf751c2116d20e34a0d2a`, 6 commits |
| Contract changes | none |
| New units | test_a_creating_switch_under_the_press_takes_the_stash_way (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (way 1 misplaces the commit for `git switch -c`) and 🟡 2 (the squash claim sent to every repository) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 1 of #894 (PR #897), target c0fbf89c against `origin/release/v0.21.0` at c38f97d7. Attack in this order:

1. **The attended path is byte-identical.** Without the press, the dirty-tree row must emit today's `ask`, unchanged in both languages. Diff the reason strings and the decision path against c38f97d7.
2. **The press is read from the session's own root** (`repo_paths(cwd)[0]`), not from the target tree. Try a session in one clone that switches another clone through `git -C`. Which root is read, and is that right?
3. **The deny's ways on actually work.** The guard reads the tree before the command runs, so `git stash && git switch x` in one call meets the same deny. Check that the text says each step is its own command, that `pop` applies to whatever is checked out, and that the detached-HEAD check is correct. A deny the model cannot get past is a stop.
4. **No loop.** Re-issuing the same switch unchanged meets the same deny, and the text says so. Check that nothing tells the model to call `AskUserQuestion`.
5. **S8:** `hooks/commit-review-gate.py`, `hooks/worktree_consent.py` and `hooks/cmdline_base.py` are byte-identical to c38f97d7.
6. **The three `Corrected ·` rows** (0.20.0 S2 and S6, 0.15.5 A4) and the in-place re-stamps in the fragments of 1791384154, 1791384157 and 1791384160. Is every claim true? The smith flagged that 0.15.6 W9 ("asks") was re-stamped with no note, and is now true only when someone is attending.
7. **The orchestration paragraph** on re-pressing at resume: does it match `automation_answered`'s actual conditions? Are M2's claims about `--resume` and compaction keeping the session id stated at the confidence that was measured?

Facts arriving as coordinates, executed by the orchestrator at c0fbf89c: `bin/evidence-check . --strict` exit 0; the S8 diff is empty. Everything else in the smith's report is the smith's, unverified.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Under the press, `git switch -c <new>` in a dirty tree meets the deny, and way 1 (commit here first) puts the commit on the branch being left, or leaves it off the new branch when a start point is named | `hooks/worktree-guard.py:3296` | **fixed** `a798c85a` | fixed at a798c85a — way 1 now says it keeps the changes on the branch checked out now and sends a switch that creates its branch (`-c`) to way 2, in both languages and in the policy paragraph; `test_a_creating_switch_under_the_press_takes_the_stash_way` pins both `-c` forms and runs way 2 with real git, seen red through `mutation-check` with the sentence removed; the changelog fragment followed in 1abaa1ef; Executed: both `-c` forms answer the deny under the press, and the base asked. Read: git's semantics for a commit before `switch -c` |
| 🟡 2 | The deny tells the model, in every opted-in repository, that a feature branch squashes at the merge | `hooks/worktree-guard.py:3299` | **fixed** `1eec0f8e` | fixed at 1eec0f8e — the squash clause is gone from both languages, and S1 asserts that no squash is named; Read: `skills/implement/SKILL.md` §2 makes squashing a property to read off each repository. The hook ships to all of them |
| ⬜ 3 | 0.15.6 W9 re-stamped as holding at `main@c6554e10` with no note, while its *asks* holds only without the press | `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md:31` | answered | corrected at 4fd6edf5 — `Corrected · W9` in this item's fragment, held by `test_the_dirty_tree_row_reads_the_tree_the_switch_is_in`, `test_the_force_staged_check_reads_from_the_root_of_the_tree` and `test_the_press_is_read_from_the_sessions_own_root`; Read: the W2 case shows the deny for the same switch under the press. A record correction, so `Needs a fix` does not count it |
| ⬜ 4 | The resume paragraph omits `automation_answered`'s same-clone condition, so a resumed session started outside the clone can press and still hold no press the guard reads | `skills/implement/orchestration.md:291` | answered | corrected at cdd60874 — the resume paragraph says the press is put from inside the clone the run works in and cites §*Creation consent* rule 4; 2022f615 re-wrapped its last line; Read: `hooks/worktree_consent.py#automation_answered`, condition 4 |
| ⬜ 5 | For `--discard-changes`, `-f` and `-m`, the deny says the changes would follow, which is false. Inherited from the base's `ask` | `hooks/worktree-guard.py:3288` | answered | the *would follow* premise for `--discard-changes`, `-f` and `-m` is the base's `ask` text, carried word for word; the attended text is pinned byte-identical to the base (S2), so rewording it is a change to both readers and not this item's; Executed: all three meet the deny under the press |
| 🟢 | The attended path is byte-identical to the base in both languages and every state that reaches the row | `hooks/worktree-guard.py:3282` | confirmed | Executed: base and head differential, 20 of 20 cells identical |
| 🟢 | The press is read from the session's own root, as the stop reads it, and that is the right root | `hooks/worktree-guard.py:3282` | confirmed | Executed: the W2 case passes, and a shell outside any repository asks. Read: the stop's call at line 2956 |
| 🟢 | Every way on the deny names passes the guard, including from a detached HEAD, and the detached-HEAD check is correct | `hooks/worktree-guard.py:3292` | confirmed | Executed: probe over 9 commands in a dirty tree and 3 from a detached HEAD |
| 🟢 | No loop: the re-issue sentence is present and no question tool is named | `hooks/worktree-guard.py:3308` | confirmed | Read, and S1 pins the whole text in both languages |
| 🟢 | S8: the three hooks are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --stat` printed nothing, exit 0 |
| 🟢 | The `Corrected ·` rows for 0.20.0 S2 and S6 and 0.15.5 A4 state what the head does | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md:9` | confirmed | Read against `main`. Their cases passed in the module run |
| 🟢 | M2's claim reproduces at the confidence the orchestration paragraph states | `skills/implement/orchestration.md:301` | confirmed | Executed: the same counts, plus no transcript continuing another file's chain |

## Paste-ready fixes

```python
                    f"  1. Commit the changes here first (`{git} commit …`), then "
                    "re-issue the switch. This keeps them on the branch checked "
                    "out now, so where the switch creates its branch (`-c`) to "
                    "carry them there, take way 2. On a branch a `routing.md` "
                    "declares, the commit gate is silent for that commit. Where "
                    f"HEAD is detached (`{git} branch --show-current` prints "
                    "nothing), the commit lands on no branch: name it with "
                    f"`{git} branch <name>` before the switch, or take way 2.\n"
```
```python
                    f"  1. 먼저 여기서 변경을 커밋하고(`{git} commit …`) 전환을 "
                    "다시 실행합니다. 이 방법은 변경을 지금 체크아웃된 브랜치에 "
                    "남기므로, 브랜치를 새로 만들어(`-c`) 변경을 그쪽으로 옮기려는 "
                    "전환이면 2번을 택하세요. `routing.md` 가 선언한 브랜치에서는 "
                    "커밋 게이트가 이 커밋을 막지 않습니다. HEAD 가 분리되어 "
                    f"있으면(`{git} branch --show-current` 가 아무것도 출력하지 "
                    "않으면) 커밋이 어느 브랜치에도 남지 않습니다. 전환 전에 "
                    f"`{git} branch <name>` 으로 이름을 붙이거나 2번을 "
                    "택하세요.\n"
```
```python
def test_a_creating_switch_under_the_press_takes_the_stash_way(
    monkeypatch, capsys, projects, repo
):
    """Round 1, yellow 1. `-c` meets the deny, the reason sends a creating
    switch to way 2, and way 2 carries the change onto the new branch."""
    write_transcript(projects, "me", ask_entries(repo))
    dirty(repo)
    decision, reason = decide(monkeypatch, capsys, repo, "git switch -c newb")
    assert decision == "deny", reason
    assert "creates its branch (`-c`)" in reason, reason
    assert "squashes" not in reason, reason
    for command in ("git stash", "git switch -c newb", "git stash pop"):
        assert decide(monkeypatch, capsys, repo, command) == ("silent", ""), command
        git_in(repo, *command.split()[1:])
    assert git_in(repo, "branch", "--show-current") == "newb"
    assert git_in(repo, "status", "--porcelain") == "M f.txt"
```
```
| Corrected · W9 · the switch ladder's tracked-changes row lists the changes of the tree the switch acts on — the `git -C` or `cd` target every row above it judged — and runs its force-staged check at that tree's root, not in the shell's starting directory and not in a subdirectory it was reached through. Without the `automation` press a dirty repository reached from elsewhere asks and names its own changes; under the press, read from the session's own root, it is the `deny` to the model naming the same changes; a clean clone switched from a dirty session tree says nothing; an anchored ignore pattern is named from a subdirectory | `seal/releases/0.15.6.md#"### 1790550712-the-worktree-guard-judges-a-switch-after-a-creation">"W9 · the switch ladder's"@<hash>`, `tests/test_guard_resolves_the_tree_it_judges.py::test_the_dirty_tree_row_reads_the_tree_the_switch_is_in`, `tests/test_the_guard_asks_once_per_session.py::test_the_press_is_read_from_the_sessions_own_root` | **Executed** <date>: both cases pass at the head | <date> | Corrected <date> by work item 1791779434-under-automation-the-guard-asks-nobody (#894): W9 said a dirty repository reached from elsewhere asks, and under the press it is the deny |
```
```markdown
The session puts it from a directory inside the clone the run works in: the
readers keep the answer only where the result's own directory and the
gate's root are the same clone (`docs/worktree-guard-spec.md` §*Creation
consent*, rule 4).
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py -q` in the clone at `c0fbf89c` | exit 0, 228 passed |
| Base and head differential: the base's `hooks/worktree-guard.py` loaded beside the head's, the same payloads with no press reaching the row, through a one-file test_tmp probe (deleted) | 20 of 20 cells `identical=True`, all `ask` |
| Under the press, dirty tree: the guard over 18 commands, the ways on and the switch shapes | ways on all silent. `git switch` with `feature/x`, `-c newb`, `-c newb main`, `-`, `--discard-changes`, `-f` and `-m` all deny with the row's text. `git checkout -b newb` meets the stop |
| Under the press, detached HEAD, dirty tree | `git branch --show-current` silent and prints the empty string. `git branch keep` silent. `git switch feature/x` denies |
| Under the press given in the repository, shell outside any repository, `git -C <repo> switch feature/x` | `ask` |
| `git diff --stat origin/release/v0.21.0...c0fbf89c` on the three S8 hooks | no output, exit 0 |
| Read-only count over `~/.claude/projects/*/*.jsonl` | 115 files, 8 with more than one version, 20 compaction boundaries, 0 foreign ids, 0 first entries parented in another file |
| The full suite, the repository-wide lint and the typecheck | not yet. Unverified. The sealer runs them once, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
