# 1791779434-under-automation-the-guard-asks-nobody — review round 5

| Field | Value |
|---|---|
| Target SHA | cdd0ce137490ab1092f44da2baee7f633408dd39 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 897 |
| Broad gate | not yet |
| Fixes checked by | round-6 |
| Fix range | `45af38a1c7fb7295048267463a87b3cd7fafe5c6..18c5a9e076c14caaf860e40658594246def6ef42`, 4 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (the policy, ledger S1 and spec In 2 say the deny infers nothing about git, and its index-residue note predicts a clean tree that a tracked ignored file does not reach) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 5 of #894 (PR #897), verifying round 4's fixes at 5e2e9ad5..7bc54620 (`rounds/round-4-fixes.md`). Attack in this order:

1. **🟡 1's fix (b6851ffb):** the deny now says "This row of the guard stops a branch switch …", in English and Korean, in the hook and in `dirty_deny`. Read the whole pressed text again, sentence by sentence. Is every claim now a fact about this row or about what the guard read, with nothing about git's behaviour?
2. **🟡 2's fix (927497cc):** the clause about git's output is gone from the hook EN/KO, `dirty_deny`, the policy paragraph, the changelog, spec.md (lines 102 and 247) and ledger S1. Grep for any remaining twin. W3's closed row in `questions.md` keeps it as history: is that acceptable?
3. **⬜ 3's correction (97ee27c4):** `option_words` strips `git -C <path>` and `restore --staged` before scanning. Can the strip hide a real per-form clause? Plant one through `mutation-check` that uses `-C` inside a clause and see whether S12 still catches it.
4. **Record markers (7bc54620)** on `round-4.md:152,157`: markers only, no verdict text changed.
5. **S2 and S8** still hold.

Facts arriving as coordinates: `round_record.py close` exit 0 for round 4. The smith re-ran only the record module after 7bc54620, not the full set of nine guards; unverified.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The policy, ledger S1 and spec In 2 say the deny infers nothing about git; its index-residue note says *These commands clean the tree*, and for a tracked file `.gitignore` matches, the restore leaves it dirty | `docs/worktree-guard-spec.md:37` | **fixed** `d664e911` | fixed at d664e911 — the report's paste-ready text: `docs/worktree-guard-spec.md`'s reason paragraph and *Why the reason predicts nothing*, ledger S1 and `spec.md` In 2 now say the deny's one sentence about git is the index-residue note it shares with the `ask`. The note itself is unchanged, because S2 pins it in the attended `ask` and it predates the branch; the orchestrator files it as an issue; Executed: probe with a tracked ignored file staged under the press; after the note's restore the status was ` M g.txt` and the switch met the deny again. Read: In 2 keeps the note *as today*; the policy's *nothing it inferred* and *each sentence about what git does was taken out* are false while it stands |
| ⬜ 2 | S1's docstring still says the choice is left to the model and git's output | `tests/test_the_guard_asks_once_per_session.py:1939` | answered | corrected at dad015f7 — S1's docstring says the choice and what follows are left to the model, and that the text predicts nothing of its own; Read: the docstring at the target; `survivor-check` misses it because the wording differs and wraps |
| ⬜ 3 | The deny issued through `git -C <repo>` from another repository is pinned by a substring and the option check only; a clause keyed on that spelling survives | `tests/test_the_guard_asks_once_per_session.py:2104` | answered | corrected at fc5fb6d1 — `test_the_press_is_read_from_the_sessions_own_root` pins the whole deny issued through `git -C <repo>`: S1's text with `git_at`'s command word. With one command word left plain through `mutation-check`, it was red; Executed: planted clause SURVIVED, 224 passed across two modules; the fenced whole-text assertion passes at the target and is red with the clause planted |
| ⬜ 4 | The module docstring, ledger `Corrected · S2` and `spec.md:98` call commit and stash commands that empty the tree; a plain `git commit` with an unstaged change exits 1 and empties nothing | `hooks/worktree-guard.py:30` | answered | corrected at 18c5a9e0 — the hook's module docstring, ledger `Corrected · S2` and `spec.md` In 2 name `git commit` and `git stash` as listed shapes that pass the guard alone, not commands that empty the tree; Executed: plain `git commit -m x` over an unstaged change, exit 1, status ` M f.txt` |
| 🟢 | round 4's first finding is closed — the clean-tree sentence speaks for this row, in both languages, in the hook and in `dirty_deny` | `hooks/worktree-guard.py:3296` | confirmed | Executed: with the old sentence put back through `mutation-check`, S1 red on its assertion. Read: every sentence of the pressed text, both languages |
| 🟢 | round 4's second finding is closed — the clause about git's output is gone from the hook, `dirty_deny`, the policy, the changelog, `spec.md` and ledger S1 | `hooks/worktree-guard.py:3306` | confirmed | Executed: either language's clause put back, S1 red; `survivor-check` over the fix range finds no removed wording. Read: W3 and the phase records keep it as history; the docstring twin is ⬜ 2 |
| 🟢 | round 4's note 3 is answered — `option_words` reads past the command word, and the strip hides no clause the equality checks would catch | `tests/test_the_guard_asks_once_per_session.py:1903` | confirmed | Executed: without the strip the W2 case is red; a planted `-C` clause turned two S12 rows and W2 red |
| 🟢 | 7bc54620 adds two markers to round 4's inherited coordinates and changes no verdict or ground | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-4.md:152` | confirmed | Executed: word diff shows two `NAME NOT IN TREE` parentheticals and nothing else |
| 🟢 | S2: the attended `ask` is byte-identical to the base | `hooks/worktree-guard.py:3329` | confirmed | Executed: the `ask` block extracted at `c38f97d7` and at the target compares equal |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --quiet c38f97d7 cdd0ce13` over the three files, exit 0 |
| 🟢 | rounds 1 to 3's findings stay closed — no per-form sentence, no stash way, no carry | `hooks/worktree-guard.py:3286` | confirmed | Executed: S1 and all sixteen S12 rows pass in the guard modules at the target |
| ❓ | the plugin's own checks after 7bc54620, beyond the modules this round ran | `bin/broad-gate` | ❓ out of verified scope | the broad gate's, run once after the rounds settle; the sealer answers it |

## Paste-ready fixes

```markdown
session's own directory, never against the tree the switch names. The reason
states what the guard read and what the guard is. Its one sentence about what
git does is the index-residue note it shares with the `ask`, word for word. It
opens with the same lead and lists the changes as the `ask` does, carries the
```
```markdown
text, the class this repository judges not to converge (§*Known limits*, the
brace reader), so each sentence of the row's own about what git does was taken
out rather than corrected again. The index-residue note it shares with the
`ask` stays as the `ask` has it. A form found later is a row in the case that
pins one text for every form, never a sentence here.
```
```
It names no question tool and no switch option, and its one sentence about what git does is the index-residue note it shares with the `ask`.
```
```markdown
tracked-changes row of §A answers `deny` instead of `ask`. **The reason
states what the guard read, and infers nothing beyond the index-residue note
it shares with the `ask`.** The guard holds three
```
```python
    """S1, rewritten at the reframe after round 3. The whole text is pinned in
    both languages: the changes listed, the press sentence byte for byte, what
    the row does, `git commit` and `git stash` as commands that pass this guard
    issued alone, the choice and what follows left to the model, the re-issue
    sentence, and no question tool. It names no switch option and predicts
    nothing of its own. Seen red at `c38f97d7` (`ask`) and at `0f1663f5`,
    whose text named `-c`, `--orphan` and way 2."""
```
```python
    write_transcript(projects, "me", ask_entries(repo))
    decision, reason = decide(monkeypatch, capsys, repo, command)
    at = f"git -C {shlex.quote(top)}"
    want = (
        dirty_deny("en", SINGLE["en"])
        .replace("`git ", f"`{at} ")
        .replace("&& git ", f"&& {at} ")
    )
    # Round 5, note 3: issued from another repository, the deny is S1's text
    # with the command word `git_at` hands back, and nothing else.
    assert (decision, reason) == ("deny", want), reason
    assert option_words(reason) == [], reason
```
```python
    pressed `automation`, a `deny` to the model instead, naming `git commit`
    and `git stash` as listed shapes that pass this guard alone and promising
    no outcome, one text for every switch form (#894)
```
```
which since #894 is a `deny` to the model naming `git commit` and `git stash` as listed shapes that pass the guard alone and promising no outcome, one text for every switch form;
```
```markdown
- names `git commit` and `git stash`, each as a listed shape that passes
```

## Executed probes

| What was run | Result |
|---|---|
| Executed — `bin/test` over `tests/test_the_guard_asks_once_per_session.py`, `tests/test_worktree_guard.py`, `tests/test_worktree_guard_signals.py` and `tests/test_guard_resolves_the_tree_it_judges.py` at the target | exit 0; 387 passed, 1 skipped |
| Executed — `bin/test` over `tests/test_a_record_states_what_the_tree_has.py`, `tests/test_a_folded_statement_names_what_enforces_it.py`, `tests/test_docs_line_wrap.py` and `tests/test_no_real_identifiers.py` | exit 0; 180 passed |
| Executed — `bin/evidence-check --ledger seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` | exit 0; 38 ok, 0 drifted, 0 broken |
| Executed — `bin/survivor-check --range 5e2e9ad5..HEAD` | exit 0; 31 removed sentences, none still standing |
| Executed — `git grep` for the removed clause in both languages at the target | matches only in round 4's report, record and fixes |
| Executed — `mutation-check` on the hook, b6851ffb's old sentence put back, S1 selected | red; S1 failed on its text assertion |
| Executed — `mutation-check` on the hook, 927497cc's clause put back in English, then in Korean, S1 selected | red both times, on the English and then the Korean assertion |
| Executed — `mutation-check` on the test module, 97ee27c4's strip line removed, the W2 case selected | red; W2 failed on the option check |
| Executed — `mutation-check` on the hook, a clause naming `` `{git} -C newb` `` added when the command holds ` -C `, the module run | red; S12 `-C new`, S12 `-C existing` and W2 failed |
| Executed — `mutation-check` on the hook, a clause with no option word added when the command starts with `git -C`, two modules run | SURVIVED; 224 passed |
| Executed — the same surviving clause against ⬜ 3's whole-text assertion, in a one-file probe | red |
| Executed — ⬜ 3's whole-text assertion at the target, in the same probe | passes |
| Executed — one-file probe: a file tracked in HEAD and matched by `.gitignore`, its change staged, `git switch feature/x` under the press, then the note's `restore --staged`, then the switch again | deny carrying the note; status after the restore ` M g.txt`; deny again |
| Executed — Python probe with real git: plain `git commit -m x` over one unstaged change | exit 1; status ` M f.txt` |
| Executed — `mutation-check` with a first plant that did not compile | printed `red` with exit 0 on a collection `SyntaxError` (see Deferred) |
| Executed — the attended `respond("ask", …)` block at `c38f97d7` and at the target, compared as strings | identical |
| Executed — `git diff --quiet c38f97d7 cdd0ce13 -- hooks/commit-review-gate.py hooks/worktree_consent.py hooks/cmdline_base.py` | exit 0 |
| Executed — `git diff --word-diff=porcelain` over 7bc54620 | two `NAME NOT IN TREE` parentheticals added, nothing removed |
| Executed — `round-record new` on this report in the clone, then `bin/evidence-check` | generator exit 0, every table parsed; `evidence-check` exit 2, two NOT-IN-TREE rows, both in the generated record's inherited coordinates and none in this report |
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
| round-4 | `hooks/worktree-guard.py:3305` | round 4's 🟡 2 — fixed |
| round-4 | `tests/test_the_guard_asks_once_per_session.py:1903` | round 4's ⬜ 3 — answered |
| round-4 | `hooks/worktree-guard.py:3286` | round 4's 🟢 — confirmed |
| round-4 | `hooks/worktree-guard.py:3290` | round 4's 🟢 — confirmed |
| round-4 | `hooks/worktree-guard.py:3302` | round 4's 🟢 — confirmed |
| round-4 | `tests/test_the_guard_asks_once_per_session.py#test_one_text_for_every_switch_form` | round 4's 🟢 — confirmed |
| round-4 | `hooks/worktree-guard.py:3329` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-2.md` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/survivors.md` | round 4's 🟢 — confirmed |
| round-4 | `docs/worktree-guard-spec.md:56` | round 4's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The index-residue note labels a tracked file that `.gitignore` matches as *force-staged*, and says its `restore --staged` cleans the tree, which leaves a staged modification or deletion dirty; both readers carry it, and S2 freezes the `ask` in this item | a new issue | the repository owner, who decides whether the note reads HEAD before naming a path force-staged |
| `mutation-check` prints `red` and exits 0 when the mutated file no longer compiles, so a seen-red claim can rest on an import error | a new issue | the repository owner, as the owner of `skills/verify/scripts/mutation_check.py` |
| `round-record new` rebuilds the inherited coordinates from each earlier round's verdicts and drops the marker 7bc54620 added by hand, so this round's record will again name the two removed cases with no marker, and `evidence-check` refuses both | a new issue; until it lands, the orchestrator repeats 7bc54620's two markers on round 5's record | the repository owner, as the owner of `skills/code-review/scripts/round_record.py` |
