# 1791779434-under-automation-the-guard-asks-nobody — round 4 report

| Field | Value |
|---|---|
| Round | 4, the redesign's first round (`skills/code-review/orchestration.md` §*A record after the stop is the redesign's*) |
| Target SHA | `127d593bf41b4e884a953e29ec2203ebbc54a541` |
| Base | `origin/release/v0.21.0` at `c38f97d7` |
| Range reviewed | the redesign's build, `34c26823..127d593b`, against the reframed `spec.md` and `plan.md` |
| Worked in | a `git clone --no-local` at the target, under `<scratchpad>/1791779434-under-automation-the-guard-asks-nobody/round-4/clone`, removed before the handover |

## Summary

The reframe holds where it matters most. The per-form recipe is gone from
the hook, from both languages and from the policy. Round 3's two findings
close by removal. S12 catches a per-form clause, and both named commands
pass the guard alone in every spelling probed. S2 and S8 stand.

Two sentences of the new text are not what the reframe says every sentence
is: a fact the guard read, or a true fact about the guard.

```
the reframe's rule: every sentence is a fact the guard read or a fact about the guard
        │
        ├─ 🟡 1  "This guard ... says nothing of a switch once none are"
        │        a fact about the guard, stated for the whole guard, false for three rows of it
        │
        └─ 🟡 2  "git's own output reports what each one did"
                 a sentence about git, the class the reframe removed, false under -q
```

Both are wording, and each fix is a deletion or one word. Neither loses a
record or crashes.

## Findings from reading, confirmed by execution

### 🟡 1 — The deny says the whole guard is silent once the tree is clean, and three rows of it are not

`hooks/worktree-guard.py:3296` (English) and `:3315` (Korean), pinned by
`tests/test_the_guard_asks_once_per_session.py:1863` and `:1881`.

The text reads: *This guard stops a branch switch while uncommitted tracked
changes are present, and says nothing of a switch once none are.* The
Korean half says the same of `이 guard`.

The first half is true of the guard. The second half is true of this row
and false of the guard. A clean switch still meets row 1 (an ACTIVE session
denies), row 1-b (idle sessions, a `choose`) and row 2 (detection unusable,
a `choose`). Under the press, `choose` denies once per session per
direction and asks after that. So the guard does speak of a clean switch,
and one of the ways it speaks puts a question to a person.

- Executed. Under the press in a clean tree, rows 1, 1-b and 2 answered
  `deny`, `deny` and `ask`. The third was the session's second choice-row
  stop.
- Read. The spec asks for the row's own scope. In 2 says the reason *says
  what the row means … where none are present it says nothing (§A's clean
  row — an owned fact)*. §A's clean row is *single work stream, clean*.
  The policy paragraph keeps that scope (*says the row stops a switch …
  and says nothing once none are*). The code widened *row* to *guard*, so
  S9's *the policy says what the code does* fails on this sentence.

Why it matters. The sentence before it, *so no other row of this guard
stops the switch*, is true now (see the 🟢 row). Read together, the two
sentences tell the model that a stash or a commit is all that stands
between it and a silent switch. That is a promise about the guard's next
verdict, and the guard does not keep it when the sessions in the tree
change between the two issues. The reframe exists to make no such promise.

The fix scopes the sentence to the row, in both languages and in S1's pin.

### 🟡 2 — The deny tells the model that git's output reports what each command did, and with `-q` it reports nothing

`hooks/worktree-guard.py:3305–3307` (English) and `:3323–3325` (Korean),
pinned by `tests/test_the_guard_asks_once_per_session.py:1871–1872` and
`:1889–1890`. The same clause is in `docs/worktree-guard-spec.md:43`,
`changelog.md:14`, `spec.md:102` and ledger row S1.

*Which of them fits this switch, and what to run after it, is yours to
decide, and git's own output reports what each one did.* The second clause
is a sentence about what git does. It is neither a fact the guard read nor
a fact about the guard.

- Executed. `git stash -q` and `git commit -q -am x` each exited 0 with
  empty output, and the stash was made. This repository's agents use `-q`.
  The measured stops in `spec.md` §*What was measured* are `git checkout
  -q` and `git switch -q`.
- Read. The policy paragraph says the reason states *what the guard read and
  what the guard is, and nothing it inferred*. Ledger row S1 says the text
  names *nothing git does*. Both claims are false while this clause stands.

Why it matters. This is the class the reframe was built to remove: a
sentence about git that holds in most cells, fails in some, and rests on
nothing the guard reads. It is cheap now and costs a round later. A
round 5 reviewer will find `-q`, and the fix then is either another
sentence about git or this deletion.

The fix deletes the clause. Five places carry it, and the class is
enumerated by `git grep "git's own output"` and `git grep "git 의 출력"`.
The hook (en, ko), `dirty_deny` (en, ko), the policy paragraph, ledger
row S1, the changelog fragment and `spec.md` In 2. `phases/phase-3.md`
records history and keeps its words; `survivor-check` will name it, and it
goes into `survivors.md`.

### ⬜ 3 — S12's option-word check would refuse the deny's own `git -C <path>` spelling, so it is sound only for the shell position its fixture uses

`tests/test_the_guard_asks_once_per_session.py:1903` (`option_words`).

The round asked whether the pattern refusal is sound in both directions.

- **It does not pass a per-form clause.** Executed: a clause planted only
  when the command names `newb` turned the six `newb` rows of S12 red. The
  equality half carries this direction. The word half is a supplement, and
  it would miss a prediction spelled with words outside its list (`carry`,
  `applies`, `restores`).
- **It does not reject the text's own `-C` today, because S12 never
  produces it.** Executed: the same deny issued from a shell in another
  repository, through `git -C <repo> switch feature/x`, returns a reason in
  which `option_words` finds `-C` four times. The phantom note's `restore
  --staged` would be refused the same way. The docstring's *never appears
  here* holds for S12's fixture and for nothing else.

This is a note, not a defect. No shipped text is wrong. But the next round
that adds an S12 row from outside the tree will meet a red case on the
text's own command word, and may be tempted to weaken the check instead of
stripping the command word. The fence below strips it.

## What this round was asked, in order

1. **Does the reframed deny predict nothing?** No per-form sentence
   remains. `git grep` over the hook at the target for `--orphan`, `way 2`
   and `stash pop` exits 1. The lead's *so no other row of this guard stops
   the switch* is a fact about the guard, and it is true: rows 1, 1-b, 2
   and the creation's judgment all sit above the dirty row and exit when
   they speak, and the only row below is row 4, which is silent. Two
   sentences still say more than the guard knows (🟡 1, 🟡 2).
2. **Is every factual claim about the guard true?** `git commit` and `git
   stash` pass alone in every spelling probed, thirteen in all. That covers
   `-u`, `-am`, `-q` and `--keep-index`, `git -C <path>` from inside the
   tree and from a shell elsewhere, and `git -c` in front. `git stash
   branch foo` is denied, and the text does not claim it. `LEAVES_THE_TREE`
   lists `stash` with that one exception. The row blocks only while tracked
   changes are present. The guard as a whole does not, which is 🟡 1. The
   re-issue sentence holds while the tree is dirty, because the same row
   is reached again with the same press. S1, S5 and S6 pass at the target.
3. **S12.** It is sound against a per-form clause, and it is sound against
   `-C` only for its fixture (⬜ 3). Its sixteen rows are round 3's table,
   row for row.
4. **S2 and S8.** The attended `respond("ask", …)` block is byte-identical
   to `c38f97d7`'s. The three hooks show no diff.
5. **The record edits.** The word diff over `rounds/` adds only
   `NAME NOT IN TREE` parentheticals, and no verdict or ground word
   changed. The `⬜ → ✅` changes are W3's and W4's status cells in
   `questions.md`, not round records.
6. **The 13 survivor exemptions.** Each excused line was opened, and each
   sentence is true where it stands. With `--exempt`, `survivor-check`
   exits 0 and excuses all thirteen.
7. **The policy paragraph and the ledger rows.** *Why the reason predicts
   nothing* matches round 3's table and the record of rounds 1–3. S4, S9,
   S12 and `Corrected · S2` state what the head does. S1 carries 🟡 2's
   clause, and S9's *the policy says what the code does* fails on 🟡 1's
   sentence until it is fixed. `evidence-check` on the fragment reads 38
   ok and 0 drifted.

Carried rather than re-established: round 2's word diff of the
`1791384157` fragment as hash moves only. This round's word diff of the
same file again shows only `main@` and §Decision matrix hashes changing.
The claims of those seven rows were not re-derived, and the only one that
names the dirty row (0.15.6 W4) was read and still holds of the lead.

## Regression tests to plant

- `tests/test_the_guard_asks_once_per_session.py`: S1 and S12 pin the whole
  text, so both fixes are pinned by editing `dirty_deny`. No new case is
  needed. Seen red: S1 and S12 fail on the hook until the hook is edited.
- Optional, with ⬜ 3: one S12-shaped row issued from another repository,
  so the stripped command word is exercised.

## Facts for the evidence ledger

- S1's claim loses *and git's output reports them* with 🟡 2's fix.
- S9 stands once 🟡 1's sentence says *row*. Its row text needs no change.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The deny says the whole guard says nothing of a switch once no changes are present; rows 1, 1-b and 2 still stop a clean switch, and under the press a repeated choice row asks a person | `hooks/worktree-guard.py:3296` | open | Executed: clean tree under the press, rows 1, 1-b, 2 gave deny, deny, ask. Read: In 2 and the policy scope this to the row; the code says the guard |
| 🟡 2 | The deny says git's own output reports what each command did; with `-q` it reports nothing, and the clause is a sentence about git, the class the reframe removed | `hooks/worktree-guard.py:3305` | open | Executed: `git stash -q` and `git commit -q -am x` exit 0 with empty output. Read: the policy's *nothing it inferred* and ledger S1's *nothing git does* are false while it stands |
| ⬜ 3 | S12's option-word check finds four `-C` in the deny issued through `git -C <repo>` from another repository; it is sound only for its fixture's shell position | `tests/test_the_guard_asks_once_per_session.py:1903` | open | Executed: the probe from another repository; the planted per-form clause turned six S12 rows red, so the other direction holds |
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

The probe files, the clone and the scratch repositories were deleted
before the handover.

## Paste-ready fixes

### 🟡 1 — scope the sentence to the row

`hooks/worktree-guard.py`, English, replacing lines 3296–3298:

```python
                    "This row of the guard stops a branch switch while "
                    "uncommitted tracked changes are present, and says nothing "
                    "of a switch once none are.\n\n"
```

`hooks/worktree-guard.py`, Korean, replacing lines 3315–3317:

```python
                    "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 "
                    "동안 브랜치 전환을 막고, 변경이 없으면 전환에 대해 아무 "
                    "말도 하지 않습니다.\n\n"
```

`tests/test_the_guard_asks_once_per_session.py`, `dirty_deny`, English,
replacing lines 1863–1864:

```python
            "This row of the guard stops a branch switch while uncommitted "
            "tracked changes are present, and says nothing of a switch once "
            "none are.\n"
```

`tests/test_the_guard_asks_once_per_session.py`, `dirty_deny`, Korean,
replacing lines 1881–1882:

```python
        "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 동안 브랜치 "
        "전환을 막고, 변경이 없으면 전환에 대해 아무 말도 하지 않습니다.\n"
```

### 🟡 2 — delete the clause about git's output

`hooks/worktree-guard.py`, English, replacing lines 3305–3307:

```python
                    "issued alone. Which of them fits this switch, and what to "
                    "run after it, is yours to decide.\n\n"
```

`hooks/worktree-guard.py`, Korean, replacing lines 3323–3325:

```python
                    "꼽는 목록에 있어, 따로 실행하면 이 guard 를 통과합니다. 이 "
                    "전환에 어느 쪽이 맞는지, 그 뒤에 무엇을 실행할지는 직접 "
                    "정하세요.\n\n"
```

`tests/test_the_guard_asks_once_per_session.py`, `dirty_deny`, English,
replacing lines 1871–1872:

```python
            "alone. Which of them fits this switch, and what to run after it, is "
            "yours to decide.\n"
```

`tests/test_the_guard_asks_once_per_session.py`, `dirty_deny`, Korean,
replacing lines 1889–1890:

```python
        "그 뒤에 무엇을 실행할지는 직접 정하세요.\n"
```

`docs/worktree-guard-spec.md`, replacing line 43's first clause:

```markdown
switch and what follows. Each is a command of
```

`seal/specs/1791779434-under-automation-the-guard-asks-nobody/changelog.md`,
replacing line 14:

```markdown
     one fits, and what comes after, to the model.
```

`seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md`, row S1's
claim, replacing the one clause:

```
that the choice and what follows are the model's,
```

`seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md`, In 2,
replacing line 102's clause:

```markdown
  follows it, is the model's to decide. It
```

### ⬜ 3 — strip the command word before the option check

```python
def option_words(reason):
    """Every option-shaped word in REASON (`-c`, `--orphan`), which a text
    keyed on no switch form has none of. The command word `git_at` hands back
    (`git -C <path>`) and the phantom note's `restore --staged` are the text's
    own spellings, not a switch form, so they are taken out first."""
    reason = re.sub(r"git -C (?:'[^']*'|\S+)", "git", reason)
    return OPTION_WORD.findall(reason.replace("restore --staged", "restore"))
```

Needs a fix: yes — 🟡 1 (the deny says the whole guard is silent once the
tree is clean) and 🟡 2 (the deny says git's output reports what each
command did, which `-q` falsifies)
Loses a record or crashes: no

## Proof

Files opened in this round:

- `hooks/worktree-guard.py` (lines 1–30, 1925–1960, 2796–3354), and its
  diff `34c26823..127d593b`; `0f1663f5`'s copy, run in the clone
- `tests/test_the_guard_asks_once_per_session.py` (its diff
  `34c26823..127d593b`, lines 80–112, 542–567, 1194–1275, 1768–1780,
  1855–1909)
- `docs/worktree-guard-spec.md` (diff `34c26823..127d593b`, lines 38–46)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md`
  (lines 1–198 and the S-table rows the survivor check named)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/plan.md`
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/survivors.md`
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/changelog.md`
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/phases/phase-3.md`
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-1.md`,
  `round-2.md`, `round-3.md` (verdict tables and record rows),
  `round-3-fixes.md`, the fix tables of `round-1-fixes.md` and
  `round-2-fixes.md`, and `round-3-report.md`'s sixteen-setup table
- `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md`
  (rows S1, S4, S9, S12, `Corrected · S2`)
- `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md`
  (its word diff; line 30)
- `seal/releases/0.15.6.md` (row W4)
- `skills/code-review/orchestration.md` (lines 322–362)
