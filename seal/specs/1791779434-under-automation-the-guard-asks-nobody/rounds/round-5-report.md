# 1791779434-under-automation-the-guard-asks-nobody — round 5 report

| Field | Value |
|---|---|
| Round | 5, the verifying round for round 4 |
| Target SHA | `cdd0ce137490ab1092f44da2baee7f633408dd39` |
| Base | `origin/release/v0.21.0` at `c38f97d7` |
| Range reviewed | round 4's fixes, `5e2e9ad5..7bc54620` (four commits), with the deny's whole pressed text read again |
| Worked in | a `git clone --no-local` at the target, under `<scratchpad>/1791779434-under-automation-the-guard-asks-nobody/round-5/clone`, removed before the handover |

## Summary

Round 4's three findings are closed. The clean-tree sentence now speaks for
this row alone, in both languages. The clause about git's output is gone
from every live text. The option check reads past the deny's own `git -C`
command word. Each fix commit's seen-red claim was re-run through
`mutation-check` and went red on the assertion, not on an import error.
S2 and S8 hold.

Reading the whole pressed text again found one sentence about git that the
reframe never touched, because it sits in the index-residue note and not in
the row's own text. The policy says the reason infers nothing, and that
note makes a prediction that a probe falsified.

```
round 4's fixes ............................................. closed (3 of 3)

the reframe's claim: "the reason states what the guard read ... and nothing it inferred"
        │
        ├─ 🟡 1  the index-residue note says "These commands clean the tree";
        │        for a tracked file .gitignore matches, the tree is still dirty after them
        │
        ├─ ⬜ 2  S1's docstring still says the choice is left to "the model and git's output"
        ├─ ⬜ 3  the deny issued through `git -C <repo>` from elsewhere is pinned by a
        │        substring only; a clause keyed on that spelling SURVIVED
        └─ ⬜ 4  the module docstring and ledger call commit and stash
                 "commands that empty the tree"; a plain `git commit` empties nothing
```

## Findings from reading, confirmed by execution

### 🟡 1 — The policy says the deny infers nothing, but its index-residue note predicts what git restore does, and the prediction is false for one reachable state

`docs/worktree-guard-spec.md:37`, `docs/worktree-guard-spec.md:62`, ledger
S1, `spec.md:81`; the note itself is at `hooks/worktree-guard.py:3255`.

The policy paragraph says the reason *states what the guard read and what
the guard is, and nothing it inferred*. *Why the reason predicts nothing*
says *each sentence about what git does was taken out*. Ledger S1 says the
deny names *nothing git does*. `spec.md` In 2 opens with the same claim.

The deny under the press still carries the index-residue note, kept *as
today* by In 2. That note says *These commands clean the tree*, followed by
`git -C <top> restore --staged <path>`. That sentence is about what git does.

Executed: in the fixture repository, a file `g.txt` is tracked in HEAD and
also matched by `.gitignore`. A staged change to it (`M  g.txt`) reaches the
row under the press. `phantom_entries` labels it *gitignored path
force-staged into the index*, because `check-ignore --no-index` matches any
path the pattern names, tracked or not. The deny says the restore cleans the
tree. After running exactly that restore, `git status --porcelain` shows
` M g.txt`, and the next switch meets the same deny.

- Under the press, the model follows the note, spends a command, and meets
  the deny again. No record is lost and nothing loops.
- The defect the branch adds is the claim. Round 4's 🟡 2 was raised on the
  same ground: the policy's *nothing it inferred* and ledger S1's *nothing
  git does* are false while a sentence about git stands in the deny.
- The note's own error predates this item and reaches the attended `ask`
  too. S2 pins that `ask` byte for byte, so this item cannot change the
  note there. That half is listed under Deferred.

The fix narrows the four claims to what is true. The deny says nothing of
its own about git, and the one sentence it carries is the note it shares
with the `ask`. The other fix would take *These commands clean the tree* out
of the deny only. That changes S1's pinned text, and splits a note the two
readers share today. The prose fix is the one fenced below.

### ⬜ 2 — S1's docstring still says the choice is left to "the model and git's output"

`tests/test_the_guard_asks_once_per_session.py:1939`.

927497cc removed the clause from the hook, `dirty_deny`, the policy, the
changelog, `spec.md` and ledger S1. The docstring of the case that pins the
text still lists *the choice and what follows left to the model and git's
output*. `survivor-check` over the fix range finds no removed wording,
because the docstring words it differently and wraps it across two lines.

The case asserts the right text, so nothing ships wrong. The docstring
describes a sentence the pinned text no longer has.

W3's closed row in `questions.md` keeps the clause in its ask column, and
`phases/phase-3.md:14` and `phases/phase-4.md:28` describe the text as it
stood at those phases. Those three are records of what was asked and built,
and that is acceptable. The docstring describes the case as it is today, so
it is not history.

### ⬜ 3 — The deny issued through `git -C <repo>` from another repository is a form whose text no case pins whole

`tests/test_the_guard_asks_once_per_session.py:2104`.

S12 pins one text across sixteen forms, all issued from a shell inside the
repository. The one case that issues the switch from another repository,
`test_the_press_is_read_from_the_sessions_own_root`, asserts a substring and
`option_words(reason) == []`. It does not assert the whole text.

Executed through `mutation-check`: a clause added only when the command
starts with `git -C`, worded with no option word (*The changes stay in that
tree.*), SURVIVED. It ran against both this module and
`tests/test_guard_resolves_the_tree_it_judges.py`, and 224 cases passed.

The asked question was whether the strip can hide a per-form clause. It can
hide only the token right after `git -C`. A planted clause that names `-C`
inside it was caught: two S12 rows and the W2 case went red. The gap is a
different one. The from-elsewhere spelling is a form that S12's table does
not hold, and the W2 case reads only part of its text.

The fence pins the whole text, with S1's bytes and the command word
`git_at` hands back. Executed: it passes at the target, and with the
surviving clause planted it goes red.

### ⬜ 4 — The module docstring and two records call `git commit` and `git stash` "commands that empty the tree"

`hooks/worktree-guard.py:30`; also ledger `Corrected · S2` and `spec.md:98`.

The deny no longer says what either command does to the tree. It says both
are on the guard's list and pass it alone. The module docstring still
describes the deny as *naming the plain commands that empty the tree*, and
ledger `Corrected · S2` uses the same words. `spec.md:98` says *the plain
commands that leave a tree with no uncommitted tracked change*.

Executed: in a fresh repository with one unstaged change, a plain `git
commit -m x` exits 1, and `git status --porcelain` still shows ` M f.txt`.
These three describe a git outcome the reframe took out of the deny itself.

## What this round was asked, in order

1. **🟡 1's fix (b6851ffb).** Read sentence by sentence, in both languages:
   - the lead plus *so no other row of this guard stops the switch*: a fact
     about the guard, confirmed in round 4 and unchanged;
   - the listing: what `git status` printed;
   - the note: a sentence about git (🟡 1 above);
   - the press sentence: byte-identical, and pinned by `PRESS`;
   - *This row of the guard stops a branch switch …*: true of this row,
     which under the press denies while entries exist and falls to the
     clean row's `exit 0` when none do;
   - *Issue each command on its own: this guard reads the tree before a
     command runs*: a fact about the guard, held by S5;
   - *on this guard's list of commands that leave the branch where it is …
     passes it when issued alone*: names `LEAVES_THE_TREE`, carried from
     round 4's thirteen spellings;
   - *which fits, and what to run after it, is yours to decide*: no claim;
   - the re-issue sentence: a fact about the guard.

   Apart from the note, every sentence is a fact about this row or about
   what the guard read. Executed: with the old sentence put back, S1 went
   red.
2. **🟡 2's fix (927497cc).** No live twin remains in the hook, the policy,
   the ledger or the changelog. The test docstring is ⬜ 2. W3 and the phase
   records keep the clause as history, which is acceptable. Executed: with
   either language's clause put back, S1 went red.
3. **⬜ 3's correction (97ee27c4).** The strip hides nothing that the
   equality half of S1 or S12 would catch. Its only blind spot is the token
   right after `git -C`. Executed: with the strip removed, the W2 case went
   red. A planted `-C` clause turned two S12 rows and W2 red. The form left
   uncovered is ⬜ 3. The `restore --staged` replace is exercised by no
   committed case, because no fixture under the press has a force-staged
   path. The 🟡 1 probe exercised it, and `option_words` returned `[]`.
4. **Record markers (7bc54620).** The word diff adds two `NAME NOT IN TREE`
   parentheticals at `round-4.md:152` and `:157` and nothing else.
5. **S2 and S8.** Both hold (executed).

The fact that arrived as a coordinate: the smith re-ran only the record
module after 7bc54620. This round ran the record module and three document
modules, and all passed. The plugin's remaining checks belong to the broad
gate, so they are a ❓ row below.

## Regression tests to plant

- `tests/test_the_guard_asks_once_per_session.py`, in
  `test_the_press_is_read_from_the_sessions_own_root`: the whole-text
  assertion in ⬜ 3's fence. Seen red in this round with the surviving
  clause planted.

## Facts for the evidence ledger

- Ledger S1 and the policy, once 🟡 1's fence lands: the deny's one sentence
  about git is the index-residue note it shares with the `ask`.
- W2: once ⬜ 3's fence lands, the case pins the whole text of a deny issued
  from another repository, and its `Enforced by:` reading becomes true for
  *names that clone in every command*.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | The policy, ledger S1 and spec In 2 say the deny infers nothing about git; its index-residue note says *These commands clean the tree*, and for a tracked file `.gitignore` matches, the restore leaves it dirty | `docs/worktree-guard-spec.md:37` | open | Executed: probe with a tracked ignored file staged under the press; after the note's restore the status was ` M g.txt` and the switch met the deny again. Read: In 2 keeps the note *as today*; the policy's *nothing it inferred* and *each sentence about what git does was taken out* are false while it stands |
| ⬜ 2 | S1's docstring still says the choice is left to the model and git's output | `tests/test_the_guard_asks_once_per_session.py:1939` | open | Read: the docstring at the target; `survivor-check` misses it because the wording differs and wraps |
| ⬜ 3 | The deny issued through `git -C <repo>` from another repository is pinned by a substring and the option check only; a clause keyed on that spelling survives | `tests/test_the_guard_asks_once_per_session.py:2104` | open | Executed: planted clause SURVIVED, 224 passed across two modules; the fenced whole-text assertion passes at the target and is red with the clause planted |
| ⬜ 4 | The module docstring, ledger `Corrected · S2` and `spec.md:98` call commit and stash commands that empty the tree; a plain `git commit` with an unstaged change exits 1 and empties nothing | `hooks/worktree-guard.py:30` | open | Executed: plain `git commit -m x` over an unstaged change, exit 1, status ` M f.txt` |
| 🟢 | round 4's first finding is closed — the clean-tree sentence speaks for this row, in both languages, in the hook and in `dirty_deny` | `hooks/worktree-guard.py:3296` | confirmed | Executed: with the old sentence put back through `mutation-check`, S1 red on its assertion. Read: every sentence of the pressed text, both languages |
| 🟢 | round 4's second finding is closed — the clause about git's output is gone from the hook, `dirty_deny`, the policy, the changelog, `spec.md` and ledger S1 | `hooks/worktree-guard.py:3306` | confirmed | Executed: either language's clause put back, S1 red; `survivor-check` over the fix range finds no removed wording. Read: W3 and the phase records keep it as history; the docstring twin is ⬜ 2 |
| 🟢 | round 4's note 3 is answered — `option_words` reads past the command word, and the strip hides no clause the equality checks would catch | `tests/test_the_guard_asks_once_per_session.py:1903` | confirmed | Executed: without the strip the W2 case is red; a planted `-C` clause turned two S12 rows and W2 red |
| 🟢 | 7bc54620 adds two markers to round 4's inherited coordinates and changes no verdict or ground | `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-4.md:152` | confirmed | Executed: word diff shows two `NAME NOT IN TREE` parentheticals and nothing else |
| 🟢 | S2: the attended `ask` is byte-identical to the base | `hooks/worktree-guard.py:3329` | confirmed | Executed: the `ask` block extracted at `c38f97d7` and at the target compares equal |
| 🟢 | S8: the three other readers are byte-identical to the base | `hooks/commit-review-gate.py` | confirmed | Executed: `git diff --quiet c38f97d7 cdd0ce13` over the three files, exit 0 |
| 🟢 | rounds 1 to 3's findings stay closed — no per-form sentence, no stash way, no carry | `hooks/worktree-guard.py:3286` | confirmed | Executed: S1 and all sixteen S12 rows pass in the guard modules at the target |
| ❓ | the plugin's own checks after 7bc54620, beyond the modules this round ran | `bin/broad-gate` | ❓ out of verified scope | the broad gate's, run once after the rounds settle; the sealer answers it |

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| The index-residue note labels a tracked file that `.gitignore` matches as *force-staged*, and says its `restore --staged` cleans the tree, which leaves a staged modification or deletion dirty; both readers carry it, and S2 freezes the `ask` in this item | a new issue | the repository owner, who decides whether the note reads HEAD before naming a path force-staged |
| `mutation-check` prints `red` and exits 0 when the mutated file no longer compiles, so a seen-red claim can rest on an import error | a new issue | the repository owner, as the owner of `skills/verify/scripts/mutation_check.py` |
| `round-record new` rebuilds the inherited coordinates from each earlier round's verdicts and drops the marker 7bc54620 added by hand, so this round's record will again name the two removed cases with no marker, and `evidence-check` refuses both | a new issue; until it lands, the orchestrator repeats 7bc54620's two markers on round 5's record | the repository owner, as the owner of `skills/code-review/scripts/round_record.py` |

## Paste-ready fixes

### 🟡 1 — narrow the four claims to what the deny says

`docs/worktree-guard-spec.md`, lines 36–38:

```markdown
session's own directory, never against the tree the switch names. The reason
states what the guard read and what the guard is. Its one sentence about what
git does is the index-residue note it shares with the `ask`, word for word. It
opens with the same lead and lists the changes as the `ask` does, carries the
```

`docs/worktree-guard-spec.md`, lines 61–64:

```markdown
text, the class this repository judges not to converge (§*Known limits*, the
brace reader), so each sentence of the row's own about what git does was taken
out rather than corrected again. The index-residue note it shares with the
`ask` stays as the `ask` has it. A form found later is a row in the case that
pins one text for every form, never a sentence here.
```

Ledger S1, the sentence that ends its claim:

```
It names no question tool and no switch option, and its one sentence about what git does is the index-residue note it shares with the `ask`.
```

`spec.md`, line 80–81:

```markdown
tracked-changes row of §A answers `deny` instead of `ask`. **The reason
states what the guard read, and infers nothing beyond the index-residue note
it shares with the `ask`.** The guard holds three
```

### ⬜ 2 — the docstring says what S1 pins

```python
    """S1, rewritten at the reframe after round 3. The whole text is pinned in
    both languages: the changes listed, the press sentence byte for byte, what
    the row does, `git commit` and `git stash` as commands that pass this guard
    issued alone, the choice and what follows left to the model, the re-issue
    sentence, and no question tool. It names no switch option and predicts
    nothing of its own. Seen red at `c38f97d7` (`ask`) and at `0f1663f5`,
    whose text named `-c`, `--orphan` and way 2."""
```

### ⬜ 3 — pin the whole text of the deny issued from another repository

In `test_the_press_is_read_from_the_sessions_own_root`, in place of the
substring assertion and the option check:

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

### ⬜ 4 — describe the two commands as the deny does

`hooks/worktree-guard.py`, lines 29–31:

```python
    pressed `automation`, a `deny` to the model instead, naming `git commit`
    and `git stash` as listed shapes that pass this guard alone and promising
    no outcome, one text for every switch form (#894)
```

Ledger `Corrected · S2`, the clause:

```
which since #894 is a `deny` to the model naming `git commit` and `git stash` as listed shapes that pass the guard alone and promising no outcome, one text for every switch form;
```

`spec.md`, lines 98–99:

```markdown
- names `git commit` and `git stash`, each as a listed shape that passes
```

Needs a fix: yes — 🟡 1 (the policy, ledger S1 and spec In 2 say the deny
infers nothing about git, and its index-residue note predicts a clean tree
that a tracked ignored file does not reach)

Loses a record or crashes: no

## Proof

Files opened in this round:

- `hooks/worktree-guard.py` (lines 25–33, 1245–1290, 2420–2460, 3220–3345, and the base's `ask` block)
- `tests/test_the_guard_asks_once_per_session.py` (lines 80–110, 1760–1780, 1855–2115)
- `docs/worktree-guard-spec.md` (lines 28–70)
- `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md`
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/spec.md` (lines 40–52, 80–110, 240–256)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/questions.md` (rows W1, P3, W3)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/changelog.md`
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/phases/phase-3.md` (lines 8–34), `phases/phase-4.md` (lines 20–34)
- `seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-4.md`, `round-4-fixes.md`, `round-4-report.md` (lines 1–30, 105–130), `round-1-report.md` (lines 30–70)
- `skills/verify/scripts/mutation_check.py` (lines 20–60)
- `bin/test`, `bin/mutation-check`
