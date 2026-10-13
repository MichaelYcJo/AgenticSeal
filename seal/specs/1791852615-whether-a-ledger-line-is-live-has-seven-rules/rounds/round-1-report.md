# 1791852615 — round 1 report (warden)

Target SHA `f8c96c3b`, base `origin/release/v0.21.1` (`321e9de1`), the whole
build, phases 1 to 3. Read in a `git clone --no-local` of the worktree at the
target SHA. Stage 1 (spec compliance) first, then stage 2 (quality).

## How the findings relate

The work states one rule in `docs/` and has seven units declare against it.
Three findings say the same thing from three sides: the words written down
do not match what the code does in every case.

1. The excusing bullet's headline and its "what this protects" sentence are
   false for `hidden_lines` on one shape, and the bullet admits this two
   sentences earlier (🟡 1).
2. The holding bullet names one shape on which the rider check and the
   checker part. They part on three, and on one of them the rider reads
   less (🟡 2).
3. The four holding readers give the same answer on doubt and declare two
   different direction words (🟡 3).

Two notes on the work item's own paperwork come after them (⬜ 4, ⬜ 5).

## Stage 1 — spec compliance

The statement is in `docs/the-evidence-ledger.md` §*The fold, and what tells
it from a deletion*, under this work item's marker, with one `Enforced by:`
line (S1). The SKILL sentence sits in §*What counts as a claim* (S2). All
seven units carry a `Reads:` line and a consequence sentence, and the seven
census lines are gone (S3). The direction table holds seven readers by eight
shapes (S4). No released ledger file changed (S5).

I accept two of the smith's divergences on grounds I checked myself:

- **Eight shapes instead of six.** With six shapes, no shape puts the two
  span readings of `live_lines` in disagreement, and no shape tells the two
  `quoted_lines` apart. My probe repeated the two-space fence: the checker
  skips the row and the rider check reads it.
- **Three declarations changed from the frame's proposal.** The checker's
  `quoted_lines` is handed more than ledgers through `unquoted`
  (`skills/evidence-check/scripts/evidence_check.py:1673`, `:1928`,
  `:2079`), so `guess` is right. `readable` has callers that end two ways.
  `chain_check.py`, `round_record.py`, the `--exempt` reader in
  `survivor_check.py`, `.github/scripts/release_seal.py:375` and the
  review-history guard all refuse a table it hid, or name the record as
  unread. `skills/verify/scripts/broad_gate.py#sealed_record` draws a label
  without the table (`broad_gate.py:2899`). So `guess` and `mixed` are
  right.

The third divergence is that `hidden_lines`' direction is written as the
code behaves. The unit's own docstring gets this right: "not taken on doubt
where the older reading would not take it". The statement in `docs/` does
not, and that is 🟡 1.

### 🟡 1 — the excusing bullet says "not taken on doubt", and one of its two readers takes a line on doubt

`docs/the-evidence-ledger.md:629` opens the bullet with **"is not taken on
doubt"**. Line 637 ends it with "What this protects is that nothing is
excused or declared by a line nobody wrote live."

Between those two sentences the bullet says that `hidden_lines` reads a row
below a comment opener nobody closed. A renderer hides that row, because an
HTML comment block that never closes runs to the end of the document. The
walk is unsure of it (`hooks/blocks.py#walk` marks every live line below the
opener uncertain, `blocks.py:366`). The table pins `read` for this case
(`tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:202`,
the fourth cell of the `config.py#hidden_lines` row). So on this shape the
bullet's headline and its protection sentence are both false for one of the
two readers the bullet names.

This matters because the bold sentence is the rule a session takes away. A
session that puts a config or routing row below a stray comment opener,
expecting the rule to park it, finds the row declared.

The fix qualifies the headline and limits the protection sentence. It does
not move the reader, because no verdict may move in this work.

### 🟡 2 — the rider check parts from the checker on three shapes, not one, and on one of them it reads less

`docs/the-evidence-ledger.md:625` to `:628` gives one difference between the
rider check and the checker: a fence opened at one to three spaces, which
the rider reads. Line 615 says, for all four holding readers: "A fence nobody
closed is a malformed file whose lines are read."

My probe (executed, below) asked all seven readers about two more shapes:

| Shape | checker `quoted_lines` | rider check `quoted_lines` |
|---|---|---|
| a fence that closes, inside a line-start comment that closes | not read | **read** |
| a fence that closes, below a `~~~~` fence nobody closed | read | **not read** |

The second shape contradicts line 615 for the rider. The walk reads the
unclosed opener as an ordinary line and then takes the inner fence as
certain (`blocks.py:321`). The checker's fence rule never closes the outer
`~~~~`, so it reads everything below it. The rider's behaviour is defensible,
because a renderer hides those lines either way. But the statement claims
the opposite, and `overview.md:24` says the two readers "differ on a fence
opened at one to three spaces" as though that were the whole difference.

This matters because the overview's divergence row and the statement are
the ground recorded for not merging the two `quoted_lines` (spec §*Out*, the
first row). A later merge argued from a single-shape difference would miss
the other two.

### 🟡 3 — the four holding readers declare `passed` twice and `refused` twice for the same answer

The checker's `quoted_lines` (`evidence_check.py:370`) and `claim_lines`
(`evidence_check.py:5591`) declare `unknown passed`. The rider check's
`quoted_lines` (`.github/scripts/rider_check.py:238`) and `anchored_rows`
(`skills/settle/scripts/settle.py:590`) declare `unknown refused`. All four
give the same answer on doubt: the line is read. In all four, the caller
then judges the line as if it were live. A quoted example then ends loud:
`BROKEN` at exit 2, a refused name at exit 2, or a directory kept at exit 1.

The registry reads a direction "through to the decision the unit's value
feeds" (`docs/the-reader-registry.md` §*The four classes*). Two of the four
units contradict their own `Reads:` line two sentences later:

- `claim_lines`: "the wrong answer is a false refusal at exit 2" beside
  `unknown passed`.
- the checker's `quoted_lines`: "a parked or malformed row reported, never
  one dropped" beside `unknown passed`.

The statement itself describes the holding group's wrong answer as loud
(`docs/the-evidence-ledger.md:619`). `passed` comes from the inventory's
rows E9 and E58. Those rows described the effect on the line ("unclosed
regions are read") rather than the decision the line feeds. Row S9, for
`anchored_rows`, read through to the decision and wrote `refused`.

This is the class #905 is about: a direction word a reviewer reads, and the
code contradicts. The paste-ready fix uses `refused` for both units. The
other way to make the group consistent is `passed` on all four, which would
need the rider check's and `anchored_rows`' sentences rewritten too. Either
way, the four should not split. Changing a docstring line moves both units'
hashes, so W2's coordinates and the re-read rows for A4, P2-1, P2-3, P4-1,
P4-2 and R5 need `--reverify --into` again, and W2's text names the words.

## Stage 2 — quality

### ⬜ 4 — one `BY_BIAS` cell is a stated cell, labelled with a reason that does not hold

`tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:220`
to `:222` labels (`config.py#hidden_lines`, *a mid-line comment before the
row*) as answered by bias: "Where the walk is unsure the fence-only reading
stands". The walk is sure of that line. My probe returned `live` with
`uncertain=False`, because the inline comment closes on the line that holds
the row. The `hidden_lines` docstring states the answer directly: a line is
hidden "inside a fenced block or a line-start HTML comment block that
closes". The cell's answer, `read`, is correct. Only its label is wrong.

So `BY_BIAS` holds three bias cells, not four. The figure "four cells" also
appears in W1's Notes cell, in `questions.md` Q4 and in `phases/phase-1.md`.
Those are paperwork and close with the run.

### ⬜ 5 — the overview's first `Not verified` row can be answered from the code

`overview.md:31` asks whether `hooks/blocks.py#walk` can return a line that
is both `fence` and uncertain. It cannot, at `f8c96c3b`, by construction:

- In `walk`, a fenced range is written as a slice, and the index jumps past
  it (`blocks.py:321` to `:324`). Its lines never reach the code that sets
  `uncertain` (`:340`, `:343`, `:359`).
- The tail loops make a line uncertain only where it is `live` (`:363` to
  `:368`).
- `walk_text` adds `inside` only where the kind is `live` (`:424` to `:428`).

A seeded fuzz over 200,000 generated texts, through both `walk` and
`walk_text`, found 0 such lines (executed). So the surviving mutation on
`and not walked.uncertain[index]` is an equivalent mutant: the clause is
unreachable. It is defensive code, not untested code. The row can move from
`Not verified` to a stated fact. Its answerer can stay as it is, for the day
the walk changes.

## Regression tests to plant

`tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, where
🟡 2's fix makes the two shapes stated answers. The answers below were
measured at `f8c96c3b`. `anchored_rows` reads every line, so it reads both.

```python
    # A fence that closes inside a line-start comment that closes: comment
    # text to a renderer, so the walk opens no fence there, while the shared
    # delimiter rule does.
    "a fence inside a comment that closes": [
        "intro", "", "<" + "!--", "```", ROW, "```", "--" + ">", "", "after",
    ],
    # A fence that closes below a fence nobody closed: the delimiter rule
    # reads everything below the unclosed opener, and the walk takes the
    # inner fence as certain, which a renderer hides either way.
    "a closed fence below a fence nobody closed": [
        "intro", "", "~~~~", "x", "```", ROW, "```", "", "after",
    ],
```

The cells, in TABLE order, appended to each row's tuple:

```python
# evidence_check.py#quoted_lines   (..., N, R)
# evidence_check.py#claim_lines    (..., N, R)
# settle.py#anchored_rows          (..., R, R)
# rider_check.py#quoted_lines      (..., R, N)
# unverified_check.py#live_lines   (..., N, N)
# config.py#hidden_lines           (..., N, N)
# unverified_check.py#readable     (..., N, N)
```

Under `agent-contract` §15, each new cell must be seen red before it is
planted. The rider mutation from phase 1 ("a line the walk is unsure of
hidden") does not reach either shape. Mutating the rider to the checker's
delimiter rule turns both cells red.

## Facts for the evidence ledger

- **Executed 2026-10-13 at `f8c96c3b`:** the checker's and the rider check's
  `quoted_lines` part on three shapes, not one. The rider reads a fence
  opened at one to three spaces and a fence inside a closed line-start
  comment, and it skips a closed fence below a fence nobody closed. Both
  `quoted_lines` agree on the other eight shapes measured.
- **Executed and read 2026-10-13 at `f8c96c3b`:** `hooks/blocks.py#walk` and
  `#walk_text` never return a line both `fence` and uncertain. The reading
  is `blocks.py:321`, `:340` to `:368` and `:424` to `:428`, and the fuzz
  found 0 lines in 200,000 texts.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the excusing bullet's headline "is not taken on doubt" and its sentence "nothing is excused or declared by a line nobody wrote live" are false for `hidden_lines` on a row below a comment opener nobody closed, which the same bullet says it declares and the table pins as read | `docs/the-evidence-ledger.md:629` | open | read: the bullet at lines 629 to 640; `hooks/blocks.py:366` makes the line uncertain; the table pins `read` at `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:202` |
| 🟡 2 | the statement names one shape on which the rider check parts from the checker; they part on three, and on a closed fence below a fence nobody closed the rider does not read, against line 615's "a fence nobody closed is a malformed file whose lines are read" | `docs/the-evidence-ledger.md:625` | open | executed: the probe on two added shapes (rider reads and checker skips; checker reads and rider skips); read: `hooks/blocks.py:321`; `overview.md:24` carries the same narrow claim |
| 🟡 3 | the checker's `quoted_lines` and `claim_lines` declare `unknown passed` while the rider check's `quoted_lines` and `anchored_rows` declare `unknown refused` for the same answer on doubt; both `passed` units' own consequence sentences name a refusal | `skills/evidence-check/scripts/evidence_check.py:370` | open | read: the four `Reads:` lines and their sentences; `docs/the-reader-registry.md` §*The four classes* reads direction at the decision; inventory rows E9 and E58 against S9 |
| ⬜ 4 | one `BY_BIAS` cell (`hidden_lines` on a mid-line comment) is answered by the docstring itself, and its label's reason, "where the walk is unsure", does not hold: the walk is sure of that line | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:222` | open | executed: the walk returns `live`, `uncertain=False`, on that line; the cell's answer is right; "four cells" also appears in W1, Q4 and phase 1 |
| ⬜ 5 | `overview.md`'s first `Not verified` row can be answered from the code: the walk cannot return `fence` and uncertain together, so the surviving mutation is equivalent | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/overview.md:31` | open | read: `hooks/blocks.py:321`, `:340` to `:368`, `:424` to `:428`; executed: fuzz, 0 lines in 200,000 texts |
| 🟢 | the seven census lines are gone, and each of the seven units carries one `Reads:` line in the grammar and one consequence sentence | `tests/undeclared_readers.txt` | confirmed | read: the diff, all seven lines; the census test is the orchestrator's executed run at `f8c96c3b` |
| 🟢 | `mixed` for `live_lines`, `hidden_lines` and `readable` holds when read through each unit's callers | `skills/verify/scripts/unverified_check.py:744` | confirmed | read: `live_lines` callers in settle, fold_check, survivor_check, gather_changelog and fold_ledger; `hidden_lines` callers at `hooks/config.py:176` and `broad_gate.py:976`; `readable` callers in chain_check, round_record, release_seal, survivor_check, broad_gate and the review-history guard |
| 🟢 | the corpus grown to eight shapes is what makes the `live_lines` mutation and the two `quoted_lines` visible | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:79` | confirmed | executed: the two-space fence, checker not read and rider read |
| 🟢 | W1 and W2 reshaped after MALFORMED: W1 holds its two tests alone, and W2 holds the seven units | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | confirmed | read: the fragment; `evidence-check --strict .` exit 0 is the orchestrator's executed run; W2's direction words follow 🟡 3 |
| 🟢 | no released ledger file changed | `seal/releases` | confirmed | executed: `git diff --stat 321e9de1 f8c96c3b -- seal/releases seal/ledger.md` printed nothing |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/test_a_folded_statement_names_what_enforces_it.py` and `tests/test_docs_line_wrap.py` with `-q` and `SPECSEAL_CASE_CEILING_S=600`, in the clone at `f8c96c3b` | exit 0, 131 passed |
| `bin/fold-check --root .` in the clone | exit 0: 186 statements in 19 documents, 0 over the 1000-line ceiling; `docs/the-evidence-ledger.md` is 702 lines |
| `git diff --stat 321e9de1 f8c96c3b -- seal/releases seal/ledger.md` | empty |
| one test_tmp probe script, run once with `python3 -I` against the clone's modules, then deleted: four shapes asked of all seven readers and of the walk, and a seeded fuzz of 200,000 texts through `walk` and `walk_text` | inner closed fence below an unclosed `~~~~`: checker read, rider not read, walk `fence` and certain. Fence inside a closed comment: checker not read, rider read. Mid-line comment: walk `live`, `uncertain=False`. Two-space fence: checker not read, rider read. Fuzz: 0 lines both `fence` and uncertain |
| the broad gate: full suite, repository lint, typecheck | not yet. It belongs to the sealer, once the rounds settle |

## Paste-ready fixes

### 🟡 1

`docs/the-evidence-ledger.md`, replace lines 629 to 640, the whole second
bullet. The comment opener is written in words, as the changelog entry
already writes it. If a backticked opener is preferred, put it back by hand.

```markdown
- **A line that EXCUSES or DECLARES something — a fold marker, a
  `seal/config.md` row, a `routing.md` row — is not taken on doubt, except
  where a declaring reader keeps an older reading that took it.**
  `unverified_check.py#live_lines` parks a line inside any fence or comment,
  closed or not, and a line its two span readings disagree about.
  `hooks/config.py#hidden_lines` keeps, wherever its walk is unsure, the
  fence-only reading it gave before #667: a row below a fence nobody closed
  declares nothing, and a row below a comment opener nobody closed still
  declares, because that reading never hid one and work item 1790645290 was
  bound to miss no row the older reading saw. That row is the one place a
  line nobody wrote live declares something; everywhere else, what this
  protects is that nothing is excused or declared by a line nobody wrote
  live. The wrong answer is a fold reported as a deletion at exit 1, a
  fragment the sweep keeps, a hook that says nothing, or a gate that asks.
```

The table test's `bullets()` keys on `EXCUSES` in the first bold run, which
this keeps. The changelog's second sentence already scopes itself to
"nothing is excused" and needs no change.

### 🟡 2

`docs/the-evidence-ledger.md`, replace lines 625 to 628, from "The rider" to
"before the walk.":

```markdown
  The rider check reads by `hooks/blocks.py#walk` rather than by the
  delimiter rule, and parts from the checker three ways: it reads a fence
  its walk is not sure of, one opened at one to three spaces, which the
  delimiter rule closes, because a rider the walk cannot place is read as it
  was before the walk; it reads a fence inside a line-start comment that
  closes, which a renderer shows as comment text; and it skips a fence that
  closes below a fence nobody closed, which a renderer hides either way.
```

`overview.md:24`, the divergence row's second cell:

```markdown
| Whether the checker's and the rider check's `quoted_lines` differ | `plan.md` §*Alternatives considered*: "a difference measured at zero rows" / they differ on three shapes: a fence opened at one to three spaces, a fence inside a closed line-start comment, and a closed fence below a fence nobody closed | both, scoped | The zero is about the released ledgers, which carry no fence line (P2-3), and it holds there. On markdown in general they differ, and the table pins the difference |
```

### 🟡 3

`skills/evidence-check/scripts/evidence_check.py:370`:

```python
    Reads: guess — a markdown file's lines, a ledger's or any `.md` file an anchor names, by the shared fence rule; unknown refused
```

`skills/evidence-check/scripts/evidence_check.py:5591`:

```python
    Reads: guess — a record's lines, a session's prose in the records' template shape; unknown refused
```

W2's claim in the ledger fragment, the clause on direction words:

```markdown
`refused` for the checker's two, `anchored_rows` and the rider check's, `mixed` for the other three
```

Then run `evidence-check --reverify --into
seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md
--checked <date>` for the rows the two hashes move: A4, P2-1, P2-3, P4-1,
P4-2, R5, W2 and W3.

Needs a fix: yes — 🟡 1, 🟡 2 and 🟡 3: the statement's excusing headline,
the statement's account of how the rider check parts from the checker, and
the two `passed` direction words in the holding group.
Loses a record or crashes: no

The broad gate is not yet run. It belongs to the sealer, and it comes due
once a round leaves nothing open, which this one does not.

## Proof block

Files opened at `f8c96c3b` in the clone:

- `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/`:
  `spec.md`, `overview.md`, `questions.md`, `changelog.md`,
  `phases/phase-1.md`, `phases/phase-2.md`, `phases/phase-3.md`
- `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md`
- `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, the
  whole module
- `docs/the-evidence-ledger.md`, the diff and lines 606 to 650;
  `docs/the-reader-registry.md` §*The four classes*
- `skills/evidence-check/scripts/evidence_check.py`: `quoted_lines`,
  `unquoted`, `claim_lines` and the `quoted_lines` call in the migrate walk
- `skills/settle/scripts/settle.py`: `anchored_rows` and `coordinates`
- `.github/scripts/rider_check.py`: `quoted_lines` and `comment_blocks`
- `hooks/config.py#hidden_lines`; `hooks/blocks.py#walk`, `#walk_text` and
  `Walk`
- `skills/verify/scripts/unverified_check.py`: `live_lines`, `readable`,
  `folded_items` and `open_record_rows`
- callers: `.github/scripts/fold_ledger.py#live_markers`,
  `.github/scripts/gather_changelog.py#live_markers`,
  `skills/code-review/scripts/survivor_check.py#gathered_fragments`,
  `skills/code-review/scripts/survivor_check.py#read_exemptions`,
  `.github/scripts/release_seal.py:335` to `:400`,
  `skills/verify/scripts/broad_gate.py#sealed_record`, and
  `hooks/review-history-guard.py:135` to `:150`
- `skills/evidence-check/SKILL.md` §*What counts as a claim*
- `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/4-ledger-settle-seal.md`
  rows E9, E58 and S9
