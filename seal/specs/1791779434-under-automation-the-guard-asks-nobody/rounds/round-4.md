# 1791779434-under-automation-the-guard-asks-nobody — review round 4

| Field | Value |
|---|---|
| Target SHA | 127d593bf41b4e884a953e29ec2203ebbc54a541 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 897 |
| Broad gate | not yet |
| Fixes checked by | round-5 |
| Fix range | `5e2e9ad5d4a3b5add6a7c3d83a74363cd11a10b7..7bc54620848442f4d89ae6d641ddadbfcccec482`, 4 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (the deny says the whole guard is silent once the tree is clean) and 🟡 2 (the deny says git's output reports what each command did, which `-q` falsifies) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 4 of #894 (PR #897), the redesign's first round after the reframe after round 3. Target 127d593b. The redesign's phases 3–4 are 34c26823..127d593b. Attack in this order:

1. **Does the reframed deny predict nothing?** Read every sentence of the pressed text in both languages. Does any sentence state or imply what git will do for some switch form: where a change goes, whether a switch succeeds, what a stash or commit leaves behind? The smith replaced the lead's "so the switch itself may go ahead" with "so no other row of this guard stops the switch". Is that a fact about the guard, and is it true? Check the rows below the dirty-tree row in `main`.
2. **Is every factual claim about the guard true?** That `git commit` and `git stash`, issued alone, pass the guard in a dirty tree under the press: run it for both, including with options such as `git stash -u`, `git commit -am`, and `git -C <path> commit`. That the row blocks only while tracked changes are present. That the re-issue sentence holds.
3. **S12** (`test_one_text_for_every_switch_form`): is the pattern-based word refusal sound in both directions? It must not pass a per-form clause, and it must not reject the text's own `git -C <path>` spelling (W4's noted overlap).
4. **S2 and S8:** the attended `ask` is byte-identical to c38f97d7, and the three hooks are unchanged.
5. **The record edits:** the smith added `NAME NOT IN TREE` markers to 23 lines across `spec.md`, `plan.md`, `questions.md` and six round records. Check that no verdict or ground text changed, using `git diff 34c26823..127d593b -- seal/specs/*/rounds/`.
6. **The 13 survivor exemptions** in `survivors.md`: is each excused sentence true where it stands?
7. **The policy paragraph** "Why the reason predicts nothing", and the restated ledger rows S1, S4, S9 and `Corrected · S2`.

Facts arriving as coordinates, from the smith and unverified: S1 and S12 seen red at the old hook; the `git grep` for `--orphan`, `way 2` and `stash pop` finds nothing.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The deny says the whole guard says nothing of a switch once no changes are present; rows 1, 1-b and 2 still stop a clean switch, and under the press a repeated choice row asks a person | `hooks/worktree-guard.py:3296` | **fixed** `b6851ffb` | fixed at b6851ffb — the report's paste-ready text: *This row of the guard stops a branch switch …* in English and *이 guard 의 이 규칙은 …* in Korean, in the hook and in `dirty_deny`; S1 was seen red through `mutation-check` with the old sentence put back; Executed: clean tree under the press, rows 1, 1-b, 2 gave deny, deny, ask. Read: In 2 and the policy scope this to the row; the code says the guard |
| 🟡 2 | The deny says git's own output reports what each command did; with `-q` it reports nothing, and the clause is a sentence about git, the class the reframe removed | `hooks/worktree-guard.py:3305` | **fixed** `927497cc` | fixed at 927497cc — the clause *and git's own output reports what each one did* and its Korean twin are gone from the hook, `dirty_deny`, `docs/worktree-guard-spec.md`, `changelog.md`, `spec.md` In 2 and its S1 row, and ledger S1; S1 was seen red through `mutation-check` with the clause put back; Executed: `git stash -q` and `git commit -q -am x` exit 0 with empty output. Read: the policy's *nothing it inferred* and ledger S1's *nothing git does* are false while it stands |
| ⬜ 3 | S12's option-word check finds four `-C` in the deny issued through `git -C <repo>` from another repository; it is sound only for its fixture's shell position | `tests/test_the_guard_asks_once_per_session.py:1903` | answered | corrected at 97ee27c4 — `option_words` takes the report's text and strips the `git -C <path>` command word and `restore --staged` before scanning; `test_the_press_is_read_from_the_sessions_own_root` now runs the check on a deny issued from another repository, red through `mutation-check` without the strip; Executed: the probe from another repository; the planted per-form clause turned six S12 rows red, so the other direction holds |
| 🟢 | round 3's first finding is closed — no sentence offers a stash way, to `--orphan` or anything else, from a detached HEAD | `hooks/worktree-guard.py:3286` | confirmed | Executed: S12's `--orphan, detached` row passes with the one text; `git grep` for `way 2` and `stash pop` exits 1 |
| 🟢 | round 3's second finding is closed — no sentence promises a carry onto a target that changed a listed file | `hooks/worktree-guard.py:3286` | confirmed | Executed: S12's two target-changed rows pass with the one text, which contains no `pop` and no `carries` |
| 🟢 | rounds 1 and 2's findings stay closed — the `-c`, `--orphan`, discarding-form and squash sentences are gone | `hooks/worktree-guard.py:3286` | confirmed | Executed: S1 and S12 assert no option word and no `squash`, and pass at the target |
| 🟢 | *so no other row of this guard stops the switch* is a true fact about the guard | `hooks/worktree-guard.py:3290` | confirmed | Read: every row above the dirty row exits when it speaks; row 4 below is silent |
| 🟢 | `git commit` and `git stash` pass the guard issued alone | `hooks/worktree-guard.py:3302` | confirmed | Executed: thirteen spellings silent under the press in a dirty tree, including `-u`, `-am` and `git -C <path>` from elsewhere |
| 🟢 | S12 refuses a per-form clause | `tests/test_the_guard_asks_once_per_session.py#test_one_text_for_every_switch_form` | confirmed | Executed: planted clause, six of sixteen red; against `0f1663f5`'s hook all sixteen red |
| 🟢 | S2: the attended `ask` is byte-identical to the base | `hooks/worktree-guard.py:3329` | confirmed | Executed: block comparison identical; the three guard modules pass |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --stat` over the three printed nothing |
| 🟢 | The record edits add markers and change no verdict or ground | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-2.md` | confirmed | Executed: word diff over `rounds/` shows only marker parentheticals added |
| 🟢 | The 13 survivor exemptions are true where they stand | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/survivors.md` | confirmed | Executed: `survivor-check --exempt` exit 0. Read: each of the 13 lines |
| 🟢 | The policy paragraph and ledger rows S4, S9, S12 and `Corrected · S2` state what the head does | `docs/worktree-guard-spec.md:56` | confirmed | Read against `main` and the cases; S1 and S9 are named under 🟡 2 and 🟡 1. Executed: `evidence-check` on the fragment, 38 ok |

## Paste-ready fixes

```python
                    "This row of the guard stops a branch switch while "
                    "uncommitted tracked changes are present, and says nothing "
                    "of a switch once none are.\n\n"
```
```python
                    "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 "
                    "동안 브랜치 전환을 막고, 변경이 없으면 전환에 대해 아무 "
                    "말도 하지 않습니다.\n\n"
```
```python
            "This row of the guard stops a branch switch while uncommitted "
            "tracked changes are present, and says nothing of a switch once "
            "none are.\n"
```
```python
        "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 동안 브랜치 "
        "전환을 막고, 변경이 없으면 전환에 대해 아무 말도 하지 않습니다.\n"
```
```python
                    "issued alone. Which of them fits this switch, and what to "
                    "run after it, is yours to decide.\n\n"
```
```python
                    "꼽는 목록에 있어, 따로 실행하면 이 guard 를 통과합니다. 이 "
                    "전환에 어느 쪽이 맞는지, 그 뒤에 무엇을 실행할지는 직접 "
                    "정하세요.\n\n"
```
```python
            "alone. Which of them fits this switch, and what to run after it, is "
            "yours to decide.\n"
```
```python
        "그 뒤에 무엇을 실행할지는 직접 정하세요.\n"
```
```markdown
switch and what follows. Each is a command of
```
```markdown
     one fits, and what comes after, to the model.
```
```
that the choice and what follows are the model's,
```
```markdown
  follows it, is the model's to decide. It
```
```python
def option_words(reason):
    """Every option-shaped word in REASON (`-c`, `--orphan`), which a text
    keyed on no switch form has none of. The command word `git_at` hands back
    (`git -C <path>`) and the phantom note's `restore --staged` are the text's
    own spellings, not a switch form, so they are taken out first."""
    reason = re.sub(r"git -C (?:'[^']*'|\S+)", "git", reason)
    return OPTION_WORD.findall(reason.replace("restore --staged", "restore"))
```

## Executed probes

| What was run | Result |
|---|---|
| Executed — `bin/test` over `tests/test_the_guard_asks_once_per_session.py`, `tests/test_worktree_guard.py` and `tests/test_worktree_guard_signals.py` at the target | exit 0; 263 passed, 1 skipped |
| Executed — S1 and S12 against `0f1663f5`'s hook copied into the clone, then restored | exit 1; 17 failed (S1 and all sixteen S12 rows), each on the pinned text |
| Executed — S12 with a clause planted in the hook only where the command names `newb`, then restored | exit 1; 6 failed (the six `newb` rows), 10 passed |
| Executed — one-file probe, under the press in a dirty tree, fifteen spellings through the guard | thirteen commit and stash spellings silent; `git stash pop` silent; `git stash branch foo` deny |
| Executed — same probe, `git -C <repo> switch feature/x` from a shell in another repository | deny; `option_words` on the reason returns `-C` four times |
| Executed — same probe, clean tree under the press, through rows 1, 1-b and 2 with one session id | deny, deny, ask |
| Executed — a Python probe with real git in a fresh repository: `git stash -q`, `git commit -q -am x` | both exit 0 with empty output; `git stash list` shows the stash |
| Executed — `bin/test` over `tests/test_a_record_states_what_the_tree_has.py`, `tests/test_a_folded_statement_names_what_enforces_it.py` and `tests/test_docs_line_wrap.py` | exit 0; 174 passed |
| Executed — `bin/evidence-check --ledger seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` | exit 0; 38 ok, 0 drifted, 0 broken |
| Executed — `bin/survivor-check --range 34c26823..HEAD`, without and then with `--exempt` on this item's `survivors.md` | exit 1 naming 13 places; then exit 0, every survivor excused (13) |
| Executed — `git grep` for `--orphan`, `way 2` and `stash pop` in `hooks/worktree-guard.py` at the target | no match, exit 1 |
| Executed — `git diff --stat c38f97d7..127d593b` over the three S8 hooks | no output |
| Executed — the attended `respond("ask", …)` block at `c38f97d7` and at the target, compared | identical text; only the window's first and last lines differ |
| Executed — `git diff --word-diff=porcelain 34c26823..127d593b` over `rounds/`, `questions.md` and `spec.md` | only `NAME NOT IN TREE` parentheticals in `rounds/` and `spec.md`; two status cells in `questions.md` |
| The broad gate: full suite, repository lint, typecheck | not yet — not run by this round; the sealer's, once the rounds settle |

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
| round-2 | `tests/test_the_guard_asks_once_per_session.py#test_a_creating_switch_under_the_press_takes_the_stash_way` | round 2's 🟢 — confirmed (removed at the reframe after round 3: NAME NOT IN TREE) |
| round-3 | `hooks/worktree-guard.py:3307` | round 3's 🟡 1 — deferred |
| round-3 | `hooks/worktree-guard.py:3310` | round 3's 🟡 2 — deferred |
| round-3 | `hooks/worktree-guard.py:3300` | round 3's 🟢 — confirmed |
| round-3 | `hooks/worktree-guard.py:3343` | round 3's 🟢 — confirmed |
| round-3 | `tests/test_the_guard_asks_once_per_session.py#test_an_orphan_switch_under_the_press_takes_the_commit_way` | round 3's 🟢 — confirmed (removed at the reframe after round 3: NAME NOT IN TREE) |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
