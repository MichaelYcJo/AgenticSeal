# 1791852615 — round 3 report (warden)

The verifying round after the run's one reopening. Target SHA `f9020934`,
base `origin/release/v0.21.1` (`321e9de1`). The target is round 2's fix
diff, `5eeb24b8..259b82ee`, one commit. I read it in a
`git clone --no-local` of the worktree at the target SHA. Round 1's and
round 2's records and reports were read first, for coordinates. Every
verdict below is re-derived here.

## How the findings relate

Round 2's 🟡 6 is closed on each of its three counts. The sentence and the
`Reads:` line the fix wrote each carry one new defect, and both are the same
shape as the finding they closed: a claim about a reader that is narrower or
wider than the reader.

1. 🟡 6 is closed. The bullet credits `seal/config.md` to `hidden_lines` and
   `routing.md` to `hooks/routing.py#shown`, a routing row below a fence
   nobody closed is now stated to declare, and the `Reads:` line no longer
   names `routing.md`.
2. The new routing sentence has no case behind its comment half. The case
   the smith cites as its pin passes with the routing reader hiding that
   row (🟡 10). Read literally, the same sentence is also false for a row a
   fence that closes holds, which R8 in
   `tests/test_routing_is_recorded.py` pins.
3. The new `Reads:` line names `seal/config.md` alone. Through `unfenced`,
   `hidden_lines` is also handed the pact files (🟡 11). The fix commit
   says the line now "names only what its callers hand it".

Both findings sit in text this run wrote, so by `docs/review-chain-spec.md`
§*The cap bounds rounds, and not the fixes of the round it stopped* the
branch owns them: rung 1 of the ladder, the diff.

⬜ 4, 5, 7, 8 and 9 are carried open and are not reported again.

## The answer — round 2's 🟡 6

### 🟡 6 is closed on all three counts

The finding had three parts, and each is answered at `259b82ee`.

- **The attribution.** `docs/the-evidence-ledger.md:638` now says
  `hidden_lines` reads `seal/config.md`, and `:643` says
  `hooks/routing.py#shown` reads a `routing.md` and is not one of the seven.
  Both hold. `shown` (`hooks/routing.py:127` to `:147`) calls the walk
  directly and passes no base, so a line the walk is unsure of stays shown.
  The routing reader is not among the seven the table module holds.
- **The "one place" sentence.** It is gone. The routing reader's older
  reading is stated as hiding nothing, and the row below a fence nobody
  closed is stated to declare. My probe (executed) asked `shown` about a
  routing row below an unclosed fence and below an unclosed line-start
  comment opener: it shows both. R3 in `tests/test_routing_is_recorded.py` pins the
  fence half; it is red against the reader from before #658.
- **The `Reads:` line.** `hooks/config.py:189` no longer names
  `routing.md`. No caller hands `hidden_lines` one, which round 2 found and I
  confirmed: the routing reader never reaches `unfenced` or `hidden_lines`.

So the round 2 finding is closed. What the fix wrote in its place opens
🟡 10 and 🟡 11, which are new claims and not round 2's finding left open.

### The three re-stamped rows hold

The fix moved two anchors: `hooks/config.py#hidden_lines` and the section
§*The fold, and what tells it from a deletion*. `git grep` over `seal/`
finds them anchored by exactly P3-1 (`seal/releases/0.16.0.md`), C2
(`seal/releases/0.18.0.md`) and W2. P3-1 and C2 each have a `Re-read` row at
the new hash, and W2 carries the new `hidden_lines` hash.
`bin/evidence-check --strict .` reports 0 drifted and 0 broken in every
section, and `bin/fold-check` lists 0 documents over the ceiling, which is
C2's claim (executed). No released ledger file changed.

## Two new findings in what the fix wrote

### 🟡 10 — the routing sentence's comment half is held by nothing, and the sentence over-reaches past a fence that closes

`docs/the-evidence-ledger.md:643` to `:646` says the routing reader's older
reading "hid nothing: a row below a fence or a comment opener nobody closed
still declares there". The smith's account names
`tests/test_the_hooks_hide_what_a_renderer_hides.py::test_the_routing_reader_never_leaves_both_readings`
as the pin. That case asks a different question. It holds that every line
the routing reader hides is one a renderer hides. A renderer hides
everything below an unclosed line-start comment opener, so a routing reader
that hid those lines would pass it.

I measured that (executed). I changed `shown` in the clone to hide, below a
line-start comment opener nobody closed, exactly the lines the renderer
oracle hides. The probe then showed the routing row below such an opener
hidden. All three modules that exercise the routing reader passed:
`tests/test_routing_is_recorded.py`,
`tests/test_the_hooks_hide_what_a_renderer_hides.py` and
`tests/test_waiver_decided_at_start.py`, 225 cases, exit 0. So the comment
half of the new sentence can go false with no case turning red. A cruder
mutation that also hid lines a renderer shows was caught by the cited case
(403 documents), which is the direction it does hold.

The fence half is pinned, but not by the cited case: it is R3 in
`tests/test_routing_is_recorded.py::test_the_routing_shapes_read_as_the_frame_expects`.
The statement's `Enforced by:` line names neither.

Read literally, the sentence is also false on a shape the same test module
pins. R8 parks a row in a fence that closes, below a line-start comment
opener nobody closed. The routing reader hides that row, and R8 is red
against the old reader for that reason. My probe found the same for a row
in a closed fence below an unclosed `~~~~` (executed). The `hidden_lines`
clause two lines up, "a row below a comment opener nobody closed still
declares", has the same over-reach: `hidden_lines` hides that R8 row too.
The next sentence's "at every other fence or comment" can be read as
covering it, but a reader has to reconcile two sentences to find the rule.

Why it matters: the statement is what a person reads to know which parked
row the commit gate takes. Its routing half was added by this run's fix,
and §14 of the agent contract asks that a fix changing what a person reads
also pin it. The behaviour is right today.

The fix scopes both clauses past a fence that closes, adds one case for the
comment half, and names both routing cases in the statement's
`Enforced by:` line. The proposed case was red against the mutation above
and green at `f9020934` (executed).

### 🟡 11 — `hidden_lines`' `Reads:` line names one of its inputs

`hooks/config.py:189` now reads "the lines of `seal/config.md`". The fix
commit says this line "names only what its callers hand it". The code says
otherwise. `hidden_lines` is called by `unfenced` (`hooks/config.py:176`),
and `unfenced` is handed these files:

- `seal/config.md`, by `config_rows`, `refusal`, `indexed_config_rows` and
  `skills/implement/scripts/seal.py#table_span`;
- `seal/pact.md`, through `hooks/config.py#pact_signers`, then
  `read_table`, then `gfm_table` (`hooks/config.py:1350`), called by
  `pact_check.py:542` and `chain_check.py:4844`;
- a `seal/pact-changes/` record, through `hooks/config.py#pact_changes`,
  called by `pact_check.py:807` and `evidence_check.py:5237`;
- the machine-local `~/.claude/specseal/pact-paths.md`, by
  `skills/evidence-check/scripts/pact_check.py#path_map` (`:302`).

`broad_gate.py#hidden_row_at` hands it `seal/config.md` directly.

The class (`guess`) and the direction (`mixed`) are still right, and those
are the two words the check reads. The prose between them is what
`docs/the-reader-registry.md` §*The four classes and the line that declares
one* leaves to the reviewer, and it now names one input of four. A reader
deciding whether a change to `hidden_lines` reaches the pact gate would
read "no". Round 2's finding was the same line naming an input it is not
handed; this is the same line missing inputs it is handed. Round 2's own
paste-ready text proposed the narrowed wording, and round 1's caller check
traced `hidden_lines`' direct callers but not those of `unfenced`.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's finding 6 is closed — the bullet credits `seal/config.md` to `hidden_lines` and `routing.md` to `hooks/routing.py#shown`, a routing row below a fence nobody closed is stated to declare, and the `Reads:` line no longer names `routing.md` | `docs/the-evidence-ledger.md:643` | confirmed | executed: the probe, `shown` shows a routing row below an unclosed fence and below an unclosed comment opener; read: `hooks/routing.py:127` to `:147`, `hooks/config.py:176`, `:189`, `:247`; R3 pins the fence half |
| 🟢 | the three re-stamped rows hold — P3-1, C2 and W2 — and no other row anchors the two moved anchors | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | confirmed | executed: `bin/evidence-check --strict .` 0 drifted, 0 broken; `bin/fold-check` 0 over the ceiling; `git grep` over `seal/` finds exactly P3-1, C2 and W2 |
| 🟡 10 | the routing sentence's comment half is held by no case, and the cited case passes with the routing reader hiding that row; read literally, "a row below a fence or a comment opener nobody closed still declares" is false for a row a fence that closes holds (R8), for both readers | `docs/the-evidence-ledger.md:645` | open | executed: a renderer-exact mutation of `shown` hid the row and the three routing modules passed, 225 cases; the proposed case was red on it and green at `f9020934`; R8 pins the routing reader hiding a fenced row below an unclosed opener. Text this run wrote at `259b82ee`, so rung 1: the branch's diff |
| 🟡 11 | `hidden_lines`' `Reads:` line names `seal/config.md` alone; through `unfenced` it is also handed `seal/pact.md`, `seal/pact-changes/` records and the machine-local pact path map; the fix commit says it names only what its callers hand it | `hooks/config.py:189` | open | read: `hooks/config.py:176`, `:1350`, `:1460`, `:1504`, `:1553`; `pact_check.py:302`, `:542`, `:807`; `chain_check.py:4844`; `evidence_check.py:5237`. The line was written by this run in phase 2 and rewritten at `259b82ee`, so rung 1: the branch's diff |

## Paste-ready fixes

### 🟡 10

Replace `docs/the-evidence-ledger.md` lines 638 to 651:

```markdown
  `hooks/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
  wherever its walk is unsure, the fence-only reading it gave before #667:
  a row below a fence nobody closed declares nothing, and a row below a
  comment opener nobody closed still declares unless a fence that closes
  holds it, because that reading never hid one and work item 1790645290
  was bound to miss no row the older reading saw. `hooks/routing.py#shown`,
  which reads a `routing.md` and is not one of the seven, keeps the reading
  it gave before #667 the same way, and that reading hid nothing: a row
  below a fence or a comment opener nobody closed still declares there,
  unless a fence that closes holds it. Those rows are the places a line
  nobody wrote live declares something; at every other fence or comment,
  what this protects is that nothing is excused or declared by a line
  nobody wrote live. The wrong answer is a fold reported as a deletion at
  exit 1, a fragment the sweep keeps, a hook that says nothing, or a gate
  that asks.
```

Extend the statement's `Enforced by:` line (the line after "is argued
against these three."):

```markdown
Enforced by: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_each_reader_gives_its_stated_answer_on_each_shape, tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_the_statement_names_each_reader_under_its_answer, tests/test_routing_is_recorded.py::test_the_routing_shapes_read_as_the_frame_expects, tests/test_routing_is_recorded.py::test_a_declaration_below_a_comment_opener_nobody_closed_still_reads
```

Add to `tests/test_routing_is_recorded.py`, after
`test_the_routing_shapes_read_as_the_frame_expects`:

```python
def test_a_declaration_below_a_comment_opener_nobody_closed_still_reads():
    """#872 round 3, finding 10. `hooks/routing.py#shown` keeps the reading
    it gave before #667 wherever its walk is unsure, and that reading hid
    nothing, so a table below a line-start comment opener nobody closed
    still declares, although a renderer hides it. R3 holds the fence half;
    this holds the comment half, which no case did."""
    text = "<" + "!-- nobody closed this\n\n" + two_axis_text()
    parsed = routing.parse(text)
    assert parsed is not None and parsed["review"] == CHAIN, parsed
```

### 🟡 11

Replace `hooks/config.py:189`:

```python
    Reads: guess — the lines of `seal/config.md`, `seal/pact.md`, a `seal/pact-changes/` record and the machine-local pact path map, through `unfenced` and `hooks/blocks.py#walk`; unknown mixed
```

## Regression tests to plant

- `tests/test_routing_is_recorded.py`: the case in 🟡 10's fix. It was seen
  red against a `shown` that hides, below an unclosed line-start comment
  opener, the lines a renderer hides, and green at `f9020934`.

## Facts for the evidence ledger

- `hooks/config.py#hidden_lines` is reached through
  `hooks/config.py#unfenced` by the config readers, the pact signer and
  pact change readers, and `skills/evidence-check/scripts/pact_check.py#path_map`.
  Read in this round; no row is proposed, since the `Reads:` line is the
  place this fact belongs.

## Executed probes

| What was run | Result |
|---|---|
| one test_tmp probe script, run with the clone's `.venv` interpreter against the clone's modules, then deleted: `hooks/routing.py#shown`, `hooks/config.py#hidden_lines` and the walk on a routing row in four shapes, plus R3 and R8 | below an unclosed fence: shown, hidden, walk unsure. Below an unclosed line-start comment opener: shown, not hidden, walk unsure. In a closed fence below an unclosed `~~~~`: not shown, hidden, walk sure. In a closed fence below an unclosed comment opener: not shown, hidden, walk sure. R8's fenced row: not shown, hidden. R3's rows: shown |
| a crude mutation of `shown` in the clone, hiding every walk-unsure line below the first line-start comment opener with no closer after it; `bin/test` on the three routing modules with `-q` and `SPECSEAL_CASE_CEILING_S=600` | exit 1: `test_the_routing_reader_never_leaves_both_readings` failed on 403 documents, 224 passed |
| a renderer-exact mutation of `shown` in the clone, hiding below an unclosed line-start comment opener only the lines the renderer oracle hides; the same three modules, same flags | exit 0, 225 passed. The probe above, rerun, showed the row below the unclosed opener hidden |
| the case in 🟡 10's fix as a test_tmp module in the clone's `tests/`, run once on the second mutation and once after `git checkout -- hooks/routing.py`, then deleted | exit 1 on the mutation, exit 0 at `f9020934` |
| `bin/evidence-check --strict .` in the clone | exit 0: every section 0 drifted, 0 broken, 0 malformed |
| `bin/fold-check --root .` in the clone | exit 0: 186 statements in 19 documents, 0 over the 1000-line ceiling |
| `git diff --stat 321e9de1 HEAD -- seal/releases seal/ledger.md` in the clone | empty, exit 0 |
| the broad gate: full suite, repository lint, typecheck | not yet. It belongs to the sealer, once the rounds settle |

The clone, its `.venv` and every probe file were removed before handover.
The worktree under review was only read; its HEAD is still `f9020934` and
its status is clean.

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:222` | round 1's ⬜ 4 — open, carried to the run's end |
| round-1 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/overview.md:31` | round 1's ⬜ 5 — open, carried to the run's end |
| round-2 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/plan.md:58` | round 2's ⬜ 7 — open, carried to the run's end |
| round-2 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/changelog.md:14` | round 2's ⬜ 8 — open, carried to the run's end. Since `259b82ee` the line "`hooks/config.py` is the one reader of the second kind that still reads a row below a comment opener nobody closed" also contradicts the statement, which now names the routing reader doing the same |
| round-2 | `docs/the-evidence-ledger.md:631` | round 2's ⬜ 9 — open, carried to the run's end |
| round-2 | `docs/the-evidence-ledger.md:643` | round 2's 🟡 6 — closed here |

Needs a fix: yes — 🟡 10, the routing sentence's comment half has no case
and the sentence over-reaches past a fence that closes; 🟡 11, the
`hidden_lines` `Reads:` line names one of its four inputs.

Loses a record or crashes: no

## Proof block

Files opened in this round, at `f9020934`:

- `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/rounds/round-1.md`
- `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/rounds/round-2.md`
- `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/rounds/round-2-report.md`
- `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/changelog.md`, lines 10 to 18
- `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md`, the diff
- `docs/the-evidence-ledger.md`, lines 595 to 675
- `docs/the-reader-registry.md`, lines 1 to 80
- `docs/review-chain-spec.md`, lines 76 to 110 and 470 to 540
- `hooks/routing.py`, lines 100 to 175
- `hooks/config.py`, lines 170 to 260, 335 to 370, 455 to 468, 1504 to 1512, and the callers listed under 🟡 11
- `hooks/blocks.py`, lines 154 to 160 and 253 to 278
- `skills/implement/scripts/seal.py`, lines 1375 to 1470
- `skills/evidence-check/scripts/pact_check.py`, lines 270 to 310, 536 to 545 and 800 to 808
- `skills/evidence-check/scripts/evidence_check.py`, lines 5228 to 5237
- `skills/code-review/scripts/chain_check.py`, lines 4836 to 4845
- `tests/test_the_hooks_hide_what_a_renderer_hides.py`, lines 705 to 745
- `tests/test_routing_is_recorded.py`, lines 90 to 97 and 760 to 850
- `tests/block_shapes.py`, the R3 to R8 shapes and their renderer spans
