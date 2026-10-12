# 1791779434-under-automation-the-guard-asks-nobody — review round 6

| Field | Value |
|---|---|
| Target SHA | 1a128488b5e2198347165213888081e082a4035e |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 897 |
| Broad gate | 741243f9 against dae101ab |
| Fixes checked by | no fixes to check |
| Fix range | `5356b8a6142788be077224810f1c2e78bb93a7fa..8141dbee33ce55a5aff74562acd062bd0d008a9d`, 8 commits |
| Contract changes | none |
| New units | test_the_deny_carries_the_note_the_ask_carries (depth 1) |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 6 of #894 (PR #897), verifying round 5's fixes at 45af38a1..18c5a9e0 (`rounds/round-5-fixes.md`). The record that reads these fixes ends the run whatever it finds. Attack in this order:

1. **🟡 1's fix (d664e911):** four claims now say the deny's one sentence about git is the index-residue note it shares with the attended `ask`. These are the policy's reason paragraph, *Why the reason predicts nothing*, ledger S1, and spec In 2. Is each claim now true of the hook, word for word? Is there any other claim of "nothing about git" left un-narrowed anywhere in the tree?
2. **⬜ 2–4's corrections (dad015f7, fc5fb6d1, 18c5a9e0):**
   - the S1 docstring;
   - the full-text pin of the deny issued via `git -C <repo>`: does it fail on a planted, form-specific clause with no option word?
   - the "listed shapes that pass the guard alone" wording in the module docstring, `Corrected · S2` and spec In 2.
3. **S2 and S8** still hold.
4. A last read of the whole pressed text in both languages. The index-residue note is #900's and out of scope.

Facts arriving as coordinates: `round_record.py close` exit 0 for round 5. The smith's final run after 7878d20d: the nine guards plus three more, 1001 passed; `evidence-check --strict` 0. These are the smith's, unverified.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | The policy's paragraph title still reads *Why the reason predicts nothing*; the reason carries the note, whose *These commands clean the tree* is a prediction | `docs/worktree-guard-spec.md:53` | answered | corrected at 0f1f6efb — the policy paragraph is titled *Why the row's own sentences predict nothing*, so the title no longer covers the index-residue note the deny shares with the `ask`. The six ledger rows hashing `## Decision matrix` were read again against the new title and re-stamped; none of their claims rests on it, and S9's claim now names it; Read: d664e911 narrowed the body and not the title; the body and the paragraph above state the exception, so no reader is misled about the code. A new title drifts six rows hashing `## Decision matrix` |
| ⬜ 2 | `spec.md`'s §Why says the deny *drops every sentence about what git will do*, and `overview.md:23` quotes In 2's pre-fix words | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md:168` | answered | corrected at 8141dbee — `spec.md` §Why's last paragraph says the deny drops every sentence of its own about what git will do and keeps the note as the `ask` has it. Its heading and In 2's say *its own sentences*, and the references to it in `spec.md`, `plan.md` and `questions.md` follow. `overview.md` quotes In 2 as it now reads and names the policy paragraph's new title; Read: In 2 at line 80 now says the opposite; a correction to the run's paperwork |
| ⬜ 3 | The deny issued through `git -C <repo>` is pinned whole in English only; a Korean clause keyed on `git -C` survives | `tests/test_the_guard_asks_once_per_session.py:2100` | answered | corrected at e5ea20f2 — `test_the_press_is_read_from_the_sessions_own_root` pins the whole Korean deny issued through `git -C <repo>`, the report's fenced block. A Korean clause appended only where the command word carries `git -C` turned it red through `mutation-check`. Ledger W2 names the Korean half at 0f1f6efb; Executed: Korean plant SURVIVED, 368 passed; the fenced block red against it in a probe and green at the target |
| ⬜ 4 | The index-residue note, which ledger S1 and the policy now name as the deny's one sentence about git, is in no case under the press | `hooks/worktree-guard.py:3292` | answered | corrected at e5ea20f2 — `test_the_deny_carries_the_note_the_ask_carries` puts a force-staged ignored file under the press and asserts the deny carries the attended `ask`'s note line for line, the report's fenced case. `{note}` taken out of the deny's English text turned it red through `mutation-check`. Ledger S1 cites it at 0f1f6efb; Executed: `{note}` taken out of the deny SURVIVED, 368 passed; the fenced case red against it in a probe and green at the target |
| 🟢 | round 5's finding 1 is closed — the policy's reason paragraph, its *Why* body, ledger S1 and `spec.md` In 2 each say the deny's one sentence about git is the note it shares with the `ask`, and each is true of the hook | `docs/worktree-guard-spec.md:37` | confirmed | Read: both readers interpolate one `note`; every other sentence is a fact about the guard or what it read. Executed: under the press with a force-staged file, the deny's note lines equal the `ask`'s |
| 🟢 | round 5's note 2 is closed — S1's docstring says the choice and what follows are the model's, and that the text predicts nothing of its own | `tests/test_the_guard_asks_once_per_session.py:1939` | confirmed | Read: the docstring against the case's assertions |
| 🟢 | round 5's note 3 is closed for English — the deny issued through `git -C <repo>` is pinned whole | `tests/test_the_guard_asks_once_per_session.py:2104` | confirmed | Executed: an English clause keyed on `git -C`, with no option word, turned the W2 case red on its equality assertion. The Korean half is ⬜ 3 |
| 🟢 | round 5's note 4 is closed — the module docstring, `Corrected · S2` and `spec.md` In 2 name `git commit` and `git stash` as listed shapes that pass the guard alone | `hooks/worktree-guard.py:30` | confirmed | Read: both are in `LEAVES_THE_TREE`, and a listed shape returns before the ladder. Executed: `survivor-check` over the fix range, no removed wording standing |
| 🟢 | S2: the attended `ask` is byte-identical to the base | `hooks/worktree-guard.py:3329` | confirmed | Executed: the block at `c38f97d7` and at the target compares equal |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --quiet c38f97d7 1a128488` over the three files, exit 0 |
| 🟢 | rounds 1 to 4's findings stay closed — no per-form sentence, no stash way, no carry, no clause about git's output | `hooks/worktree-guard.py:3286` | confirmed | Executed: S1 and all sixteen S12 rows pass in the guard modules at the target. Read: the pressed text in both languages |
| ❓ | the smith's last run (1001 passed) and `evidence-check --strict` over the tree | `bin/broad-gate` | ❓ out of verified scope | the broad gate's, run once after the rounds settle; the sealer answers it |

## Paste-ready fixes

```markdown
**Why the row's own sentences predict nothing.** The guard reads three facts here: the
```
```markdown
So the reframed deny keeps every sentence that is a fact the guard read or a
fact about the guard itself — the changes listed from `git status`, the
press, that `commit` and `stash` are listed shapes (S4), that a compound
meets the same row (S5), that a re-issue meets the same refusal — and drops
every sentence of its own about what git will do. The index-residue note it
shares with the `ask` stays as the `ask` has it.
```
```
The reframed In 2: "The reason states what the guard read, and infers nothing beyond the index-residue note it shares with the `ask`"
```
```python
    # Round 6, note 3: the Korean half, issued from another repository.
    write_transcript(projects, "me", ask_entries(repo))
    monkeypatch.setenv("SPECSEAL_LANG", "ko")
    wko = load_hook_module("worktree-guard.py", "wg_894_w2_ko")
    monkeypatch.setattr(wko.worktree_consent, "PROJECTS_ROOT", str(projects))
    decision, ko = verdict_in(
        wko, monkeypatch, capsys, repo, command, ([], [], True), "me"
    )
    want_ko = (
        dirty_deny("ko", SINGLE["ko"])
        .replace("`git ", f"`{at} ")
        .replace("&& git ", f"&& {at} ")
    )
    assert (decision, ko) == ("deny", want_ko), ko
```
```python
def test_the_deny_carries_the_note_the_ask_carries(
    monkeypatch, capsys, projects, repo
):
    """S1's last clause: the deny's one sentence about what git does is the
    index-residue note, line for line the attended `ask`'s. Round 6, note 4:
    no case under the press had a force-staged path, so the note could
    leave the deny with every case green."""
    dirty(repo)
    (repo / ".gitignore").write_text("ign.txt\n", encoding="utf-8")
    (repo / "ign.txt").write_text("x\n", encoding="utf-8")
    git_in(repo, "add", "-f", "ign.txt")

    write_transcript(projects, "me", ask_entries(repo))
    decision, deny = decide(monkeypatch, capsys, repo, "git switch feature/x")
    write_transcript(projects, "me", [])
    attended, ask = decide(monkeypatch, capsys, repo, "git switch feature/x")
    assert (decision, attended) == ("deny", "ask"), (deny, ask)

    head = "Index-only residue invisible in the working tree:"
    assert head in ask.split("\n"), ask
    assert head in deny.split("\n"), deny

    def note(text):
        lines = text.split("\n")
        first = lines.index(head)
        last = max(i for i, x in enumerate(lines) if "restore --staged" in x)
        return lines[first : last + 1]

    assert note(deny) == note(ask), (deny, ask)
```

## Executed probes

| What was run | Result |
|---|---|
| Executed — `bin/test` over `tests/test_the_guard_asks_once_per_session.py`, `tests/test_worktree_guard.py`, `tests/test_worktree_guard_signals.py` and `tests/test_guard_resolves_the_tree_it_judges.py` at the target | exit 0; 387 passed, 1 skipped |
| Executed — `bin/test` over `tests/test_a_record_states_what_the_tree_has.py`, `tests/test_a_folded_statement_names_what_enforces_it.py`, `tests/test_docs_line_wrap.py` and `tests/test_no_real_identifiers.py` | exit 0; 180 passed |
| Executed — `bin/evidence-check --ledger` on the two fragments the range touched, `1791779434` and `1791384157` | exit 0 each; 38 ok and 239 ok, 0 drifted, 0 broken |
| Executed — `bin/survivor-check --range 45af38a1..18c5a9e0` | exit 0; 19 removed sentences, none still standing |
| Executed — `mutation-check` on the hook: an English clause with no option word, appended when the command holds `git -C`; three guard modules | red; the W2 case failed on its equality assertion |
| Executed — `mutation-check` on the hook: the same clause in Korean; three guard modules | SURVIVED; 368 passed |
| Executed — `mutation-check` on the hook: `{note}` taken out of the deny's English text; three guard modules | SURVIVED; 368 passed |
| Executed — one-file probe holding ⬜ 3's and ⬜ 4's fenced cases, at the target | exit 0; 2 passed |
| Executed — `mutation-check`, the Korean plant against ⬜ 3's case in the probe | red, on the equality assertion |
| Executed — `mutation-check`, `{note}` taken out against ⬜ 4's case in the probe | red, on the presence assertion |
| Executed — the attended `respond("ask", …)` block at `c38f97d7` and at the target, compared as strings | identical |
| Executed — `git diff --quiet c38f97d7 1a128488 -- hooks/commit-review-gate.py hooks/worktree_consent.py hooks/cmdline_base.py` | exit 0 |
| Executed — `git grep` over the hook, docs, ledgers, tests and work item for claims that the deny says nothing about git | the places named under ⬜ 1 and ⬜ 2; the rest narrowed or history |
| Executed — `round-record new` on this report in the clone, then `bin/evidence-check` and the record modules on the generated record | generator exit 0, every table parsed, `Pass` unticked while the four notes are open; `evidence-check` exit 2 and `tests/test_a_record_states_what_the_tree_has.py` red on two NOT-IN-TREE rows, both in the generated record's inherited coordinates for the two cases removed at the reframe, none in this report |
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
| round-5 | `docs/worktree-guard-spec.md:37` | round 5's 🟡 1 — fixed |
| round-5 | `tests/test_the_guard_asks_once_per_session.py:1939` | round 5's ⬜ 2 — answered |
| round-5 | `tests/test_the_guard_asks_once_per_session.py:2104` | round 5's ⬜ 3 — answered |
| round-5 | `hooks/worktree-guard.py:30` | round 5's ⬜ 4 — answered |
| round-5 | `hooks/worktree-guard.py:3306` | round 5's 🟢 — confirmed |
| round-5 | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-4.md:152` | round 5's 🟢 — confirmed |
| round-5 | `bin/broad-gate` | round 5's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The index-residue note's own prediction, *These commands clean the tree*, is false for a tracked file `.gitignore` matches, in both readers | #900; already deferred in round 5 | the repository owner, who decides whether the note reads HEAD before naming a path force-staged |
