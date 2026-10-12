# 1791779434-under-automation-the-guard-asks-nobody — round 6 report

| Field | Value |
|---|---|
| Round | 6, the verifying round for round 5 |
| Target SHA | `1a128488b5e2198347165213888081e082a4035e` |
| Base | `origin/release/v0.21.0` at `c38f97d7` |
| Range reviewed | round 5's fixes, `45af38a1..18c5a9e0` (four commits), with the deny's whole pressed text read again in both languages |
| Worked in | a `git clone --no-local` at the target, under `<scratchpad>/1791779434-under-automation-the-guard-asks-nobody/round-6/clone`, removed before the handover |

## Summary

Round 5's four findings are closed. The four claims 🟡 1 named are now true
of the hook, word for word. The docstring, the whole-text pin and the
"listed shapes" wording each say what the code does. S2 and S8 hold.

Nothing found in this round needs a fix. Four notes remain. Two are
claims the fix did not reach, and two are halves of a claim that no case
pins.

```
round 5's fixes ............................................ closed (4 of 4)

🟡 1 narrowed four claims to "the one sentence about git is the shared note"
        │
        ├─ ⬜ 1  the policy's paragraph title still reads
        │        "Why the reason predicts nothing"
        ├─ ⬜ 2  spec §Why still says the deny "drops every sentence about what
        │        git will do", and overview.md quotes In 2's old words
        └─ ⬜ 4  the note the four claims now name is in no case under the
                 press; dropping it from the deny SURVIVED

⬜ 3 pinned the deny issued through `git -C` whole, in English
        └─ ⬜ 3  the Korean half is not pinned; a Korean clause keyed on
                 `git -C` SURVIVED
```

## What this round was asked, in order

### 1. 🟡 1's fix (d664e911): are the four claims now true, and is there a fifth?

Each claim was read against the pressed block at
`hooks/worktree-guard.py:3284`:

- **The policy's reason paragraph** (`docs/worktree-guard-spec.md:37`)
  says the reason's one sentence about git is the index-residue note it
  shares with the `ask`, word for word. That is true. The deny and the
  `ask` interpolate the same `note` variable, built once at line 3253.
  Executed: with a force-staged ignored file under the press, the note's
  lines in the deny equal the note's lines in the attended `ask`.
- ***Why the reason predicts nothing***, the body
  (`docs/worktree-guard-spec.md:63`), now says each sentence *of the row's
  own* was taken out and the note stays. That is true.
- **Ledger S1** says the same as the policy, and it is true. One half of
  it is pinned by no case (⬜ 4).
- **`spec.md` In 2** (line 80) says the reason infers nothing beyond the
  note. That is true.

The other sentences of the deny were read again. One of them names
`git commit` and `git stash` as *on this guard's list of commands that
leave the branch where it is*. That clause names `LEAVES_THE_TREE` by the
definition its comment gives, *leaves HEAD's branch where it was*. It
describes the guard's list, not an outcome of a switch. So the deny's
only sentence about what git does is still the note.

A fifth claim was searched for with `git grep` over the hook, the docs,
the ledgers, the tests and the work item, excluding the round files:

- `hooks/worktree-guard.py:3277`, *says nothing about what git does for
  any switch form*: narrowed by its own last words, and true.
- The changelog, *says nothing about what any kind of switch does with the
  changes*: narrowed the same way, and true.
- `dirty_deny`'s docstring and S12's docstring: each speaks of a case
  whose fixture has no force-staged path, so its text carries no note.
  True of the case.
- Not narrowed: the policy's paragraph title (⬜ 1); `spec.md:168` and
  the two `spec.md` headings, and `overview.md:23`'s quote of In 2 (⬜ 2).
- `plan.md:111` and the phase records keep the older words as the record
  of what each step changed. `survivors.md` already excuses that kind of
  line.

### 2. ⬜ 2–4's corrections

- **⬜ 2, the S1 docstring (dad015f7).** It now lists *the choice and what
  follows left to the model* and says the text *predicts nothing of its
  own*. Both are true of what the case pins.
- **⬜ 3, the whole-text pin of the deny issued through `git -C <repo>`
  (fc5fb6d1).** A clause with no option word, appended only when the
  command holds `git -C`, was planted in the English text through
  `mutation-check`. `test_the_press_is_read_from_the_sessions_own_root`
  went red on its equality assertion. The same plant in the Korean text
  SURVIVED all three guard modules, 368 passed. The case pins English only
  (⬜ 3 below).
- **⬜ 4, "listed shapes that pass the guard alone" (18c5a9e0).** The
  module docstring, `Corrected · S2` and `spec.md` In 2 now carry it. It is
  true: `commit` and `stash` are in `LEAVES_THE_TREE`, `stash branch` is
  read apart as unlisted, and a listed shape returns before the ladder.
  `survivor-check` over the fix range finds none of the 19 removed
  sentences standing.

### 3. S2 and S8

- **S2.** Executed: the attended `respond("ask", …)` block, extracted at
  `c38f97d7` and at the target, compares equal.
- **S8.** Executed: `git diff --quiet c38f97d7 1a128488` over
  `hooks/commit-review-gate.py`, `hooks/worktree_consent.py` and
  `hooks/cmdline_base.py` exits 0.

### 4. The whole pressed text, in both languages

Read sentence by sentence at `hooks/worktree-guard.py:3284` to `:3327`:

| Sentence | What it is |
|---|---|
| the lead and *no other row of this guard stops the switch* | a fact about the guard |
| the listing | what `git status` printed |
| the note | the shared note; its own wording is #900's and was not judged |
| the press sentence | byte-identical to `PRESS`, in both languages |
| *This row of the guard stops a branch switch …* | true of this row |
| *Issue each command on its own …* | a fact about the guard, held by S5 |
| *`git commit` and `git stash` are on this guard's list …* | a fact about the guard's list |
| *Which of them fits … is yours to decide* | no claim |
| the re-issue sentence | a fact about the guard |

The Korean text says the same sentence for sentence. Nothing new was
found here.

### The facts that arrived as coordinates

- `round_record.py close` exit 0 for round 5: not run here. Read: the
  record `round-5.md` carries each fix verdict merged into its row.
- The smith's last run, 1001 passed, and `evidence-check --strict` exit 0:
  `unverified`. This round ran three guard modules and four document
  modules and narrowed `evidence-check` to the two ledgers the range
  touched. The sealer answers the rest.

## Findings from reading, confirmed by execution

### ⬜ 1 — The policy's paragraph title still says the reason predicts nothing

`docs/worktree-guard-spec.md:53`.

d664e911 narrowed the body of the paragraph. Its title still reads *Why
the reason predicts nothing*. The reason includes the note, and the note
predicts *These commands clean the tree*. Round 5 showed that prediction is
false for a tracked file that `.gitignore` matches.

The body under the title states the exception, and the paragraph above it
does too. So a reader is not misled about what the code does, and that is
why this is ⬜ and not 🟡.

The fix has a cost. The title sits inside `## Decision matrix`, and six
ledger rows hash that section. d664e911 re-hashed them once already, and a
new title drifts them again.

### ⬜ 2 — The spec's §Why still says the deny drops every sentence about git

`seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md:168`.

The last paragraph of *Why the deny predicts nothing* says the reframed
deny *drops every sentence about what git will do*. The deny keeps the
note, and the note is such a sentence. In 2 at line 80 now says so, and
this paragraph contradicts it. The two headings, In 2's at line 72 and §Why
at line 140, carry the same unqualified word.

`overview.md:23` quotes the reframed In 2 as *"The reason states what the
guard read and nothing it inferred"*. In 2 no longer says that.

This is the run's paperwork, so it is a correction.

### ⬜ 3 — The deny issued from another repository is pinned in English only

`tests/test_the_guard_asks_once_per_session.py:2100`.

fc5fb6d1 pins the whole English deny issued through `git -C <repo>`. No
case runs the Korean module with `git -C`. S1 and S12 run Korean from
inside the tree.

Executed: a Korean clause, appended only when the command holds `git -C`,
SURVIVED all three guard modules. The fenced block below catches it. A
one-file probe with that block passed at the target and went red against
the same plant, on the equality assertion.

### ⬜ 4 — The note the four claims now name is in no case under the press

`hooks/worktree-guard.py:3292`; the claim is ledger S1 and
`docs/worktree-guard-spec.md:38`.

S1 cites only `test_under_the_press_the_dirty_row_is_a_deny_to_the_model`.
That case's fixture has no force-staged path, so the deny it pins carries
no note. No other case under the press has one either.

Executed: `{note}` taken out of the English deny through `mutation-check`
SURVIVED all three guard modules, 368 passed. The deny would then carry no
sentence about git, and the ledger would still say its one sentence is the
note.

The code is right today, and that is why this is ⬜. The fenced case below
puts a force-staged file under the press and asserts that the deny carries
the `ask`'s note, line for line. A one-file probe with that case passed at
the target and went red against the same mutation, on its presence
assertion.

## Regression tests to plant

- `tests/test_the_guard_asks_once_per_session.py`, at the end of
  `test_the_press_is_read_from_the_sessions_own_root`: the Korean half (⬜ 3).
- `tests/test_the_guard_asks_once_per_session.py`, after S1's case: the
  note carried under the press (⬜ 4), added to ledger S1's evidence column.

## Facts for the evidence ledger

- If ⬜ 4's case is planted, S1's evidence gains it. Seen red: `{note}`
  taken out of the deny's English text through `mutation-check`.
- If ⬜ 1's title changes, the rows hashing `## Decision matrix` in both
  fragments drift and are read again.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | The policy's paragraph title still reads *Why the reason predicts nothing*; the reason carries the note, whose *These commands clean the tree* is a prediction | `docs/worktree-guard-spec.md:53` | open | Read: d664e911 narrowed the body and not the title; the body and the paragraph above state the exception, so no reader is misled about the code. A new title drifts six rows hashing `## Decision matrix` |
| ⬜ 2 | `spec.md`'s §Why says the deny *drops every sentence about what git will do*, and `overview.md:23` quotes In 2's pre-fix words | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md:168` | open | Read: In 2 at line 80 now says the opposite; a correction to the run's paperwork |
| ⬜ 3 | The deny issued through `git -C <repo>` is pinned whole in English only; a Korean clause keyed on `git -C` survives | `tests/test_the_guard_asks_once_per_session.py:2100` | open | Executed: Korean plant SURVIVED, 368 passed; the fenced block red against it in a probe and green at the target |
| ⬜ 4 | The index-residue note, which ledger S1 and the policy now name as the deny's one sentence about git, is in no case under the press | `hooks/worktree-guard.py:3292` | open | Executed: `{note}` taken out of the deny SURVIVED, 368 passed; the fenced case red against it in a probe and green at the target |
| 🟢 | round 5's finding 1 is closed — the policy's reason paragraph, its *Why* body, ledger S1 and `spec.md` In 2 each say the deny's one sentence about git is the note it shares with the `ask`, and each is true of the hook | `docs/worktree-guard-spec.md:37` | confirmed | Read: both readers interpolate one `note`; every other sentence is a fact about the guard or what it read. Executed: under the press with a force-staged file, the deny's note lines equal the `ask`'s |
| 🟢 | round 5's note 2 is closed — S1's docstring says the choice and what follows are the model's, and that the text predicts nothing of its own | `tests/test_the_guard_asks_once_per_session.py:1939` | confirmed | Read: the docstring against the case's assertions |
| 🟢 | round 5's note 3 is closed for English — the deny issued through `git -C <repo>` is pinned whole | `tests/test_the_guard_asks_once_per_session.py:2104` | confirmed | Executed: an English clause keyed on `git -C`, with no option word, turned the W2 case red on its equality assertion. The Korean half is ⬜ 3 |
| 🟢 | round 5's note 4 is closed — the module docstring, `Corrected · S2` and `spec.md` In 2 name `git commit` and `git stash` as listed shapes that pass the guard alone | `hooks/worktree-guard.py:30` | confirmed | Read: both are in `LEAVES_THE_TREE`, and a listed shape returns before the ladder. Executed: `survivor-check` over the fix range, no removed wording standing |
| 🟢 | S2: the attended `ask` is byte-identical to the base | `hooks/worktree-guard.py:3329` | confirmed | Executed: the block at `c38f97d7` and at the target compares equal |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --quiet c38f97d7 1a128488` over the three files, exit 0 |
| 🟢 | rounds 1 to 4's findings stay closed — no per-form sentence, no stash way, no carry, no clause about git's output | `hooks/worktree-guard.py:3286` | confirmed | Executed: S1 and all sixteen S12 rows pass in the guard modules at the target. Read: the pressed text in both languages |
| ❓ | the smith's last run (1001 passed) and `evidence-check --strict` over the tree | `bin/broad-gate` | ❓ out of verified scope | the broad gate's, run once after the rounds settle; the sealer answers it |

## Paste-ready fixes

### ⬜ 1 — the policy's paragraph title

`docs/worktree-guard-spec.md`, line 53:

```markdown
**Why the row's own sentences predict nothing.** The guard reads three facts here: the
```

The line is 86 columns, inside `tests/test_docs_line_wrap.py`'s limit of
88, so nothing else in the paragraph moves. The rows hashing `## Decision
matrix` are read again.

### ⬜ 2 — the spec's §Why and the overview's quote

`spec.md`, lines 165–168:

```markdown
So the reframed deny keeps every sentence that is a fact the guard read or a
fact about the guard itself — the changes listed from `git status`, the
press, that `commit` and `stash` are listed shapes (S4), that a compound
meets the same row (S5), that a re-issue meets the same refusal — and drops
every sentence of its own about what git will do. The index-residue note it
shares with the `ask` stays as the `ask` has it.
```

`overview.md`, line 23, the quote at the end of the second cell:

```
The reframed In 2: "The reason states what the guard read, and infers nothing beyond the index-residue note it shares with the `ask`"
```

### ⬜ 3 — the Korean half of the deny issued from another repository

At the end of `test_the_press_is_read_from_the_sessions_own_root`, after the
`ask` assertion:

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

### ⬜ 4 — the note carried under the press

After `test_under_the_press_the_dirty_row_is_a_deny_to_the_model`:

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The index-residue note's own prediction, *These commands clean the tree*, is false for a tracked file `.gitignore` matches, in both readers | #900; already deferred in round 5 | the repository owner, who decides whether the note reads HEAD before naming a path force-staged |

Needs a fix: no

Loses a record or crashes: no

The four notes are ⬜. None of them changes what the guard does, and each
has a fenced answer the smith may plant or answer with grounds. Nothing is
open that holds the run.

Two things follow from the generator's dry run in the clone:

- `Pass` stays unticked while the four notes are open. They close once, at
  the run's end, through `round-record notes`, and the record already reads
  `Fixes checked by | no fixes to check`, which that subcommand needs.
- The generated record names the two cases removed at the reframe, with no
  marker, in its inherited coordinates. Round 5 deferred that. The
  orchestrator repeats 7bc54620's two `NAME NOT IN TREE` markers on this
  record, as on round 5's.

The generator also noticed that the changelog fragment predates d664e911
and 18c5a9e0. The fragment was read against both, and it still says what
ships, so nothing is owed there.

The broad gate comes due once the notes are closed and `Pass` is ticked. The
next act after that is the sealer's spawn.

## Proof

Files opened in this round:

- `hooks/worktree-guard.py` (lines 20–35, 1251–1290, 1910–1975, 2165–2200, 2796–2860 by search, 3200–3345)
- `tests/test_the_guard_asks_once_per_session.py` (lines 30–45, 80–110, 1248–1275, 1768–1780, 1840–1960, 2040–2125)
- `tests/test_guard_resolves_the_tree_it_judges.py` (lines 495–530)
- `docs/worktree-guard-spec.md` (lines 25–80)
- `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` (rows S1, S9, `Corrected · S2`, through the fix diff and search)
- `seal/ledger/1791384157-the-hooks-read-the-session-waiver-and-creation-one-way.md` (the rows the fix diff re-hashed)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md` (lines 68–175)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/changelog.md`, `overview.md` (lines 15–75), `survivors.md`, `plan.md` (lines 100–116)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-5.md`, `round-5-report.md`, `round-5-fixes.md`
- `skills/verify/scripts/mutation_check.py` (lines 1–80), `bin/mutation-check`
