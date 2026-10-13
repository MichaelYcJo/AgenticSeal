# Round 1 report — 1791867522 (#922), PR #927

Target `7db671f0` on `fix/922-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs`; base `origin/release/v0.21.1` at `2d4fbdff`, which is also the merge base. The whole branch was reviewed: seven commits, ten files. The review worked in a `git clone --no-local` at the target SHA under the session scratchpad, and that clone has been removed.

## In short

The branch does what #872's round 3 asked of it. No finding needs a fix.

- 🟡 10 is closed. Both declaring clauses are scoped past a fence that closes, a case now holds the comment half, and the statement's `Enforced by:` line names both routing cases. The new case went red under a mutation of `shown` (executed).
- 🟡 11 is closed. The `Reads:` line names five inputs, and the code hands it exactly those five (read: every caller traced).
- The 23 re-stamped rows hold against the merged sections. Every family was read, including #911's rule 3 and #903's Windows bullet.
- Two ⬜ notes remain. Both are about how the "five inputs" route is described, not about which inputs there are.

## Stage 1 — spec compliance

### 🟡 10: the statement now says what each reader does, and a case pins the comment half

The account claimed the two clauses were reworded in place, a new case was added, and R3 plus the new case were added to `Enforced by:`. The code at `docs/the-evidence-ledger.md:638-651` matches round 3's paste-ready text word for word. Line 664 names R3's test (`test_the_routing_shapes_read_as_the_frame_expects`) and the new case beside the table module's two. The prose is rewritten in place and carries no change narrative. That meets the owner's rule. #872's changelog fragment (`seal/specs/1791852615-…/changelog.md:16-17`) carries the same qualifier, also in place.

Is the new wording true? I checked it against the two readers.

- `hooks/routing.py#shown` hides only what the walk is sure of (`walked.hidden()`, no base). Below an unclosed line-start comment opener, a closed fence is still hidden, which is R8 in `tests/block_shapes.py:198`. Every other line below the opener is shown. So "still declares there, unless a fence that closes holds it" is what the code does.
- `hooks/config.py#hidden_lines` falls back to `blocks.fence_only` where the walk is unsure. A closed fence below the unclosed opener is hidden, and anything below an unclosed fence is hidden. The clause names both cases.

The new case is `tests/test_routing_is_recorded.py:834`. I ran a mutation of `shown` that hides everything below a line-start comment opener with no closer after it (executed, in the clone, file restored from held bytes). The case went red (`parse` returned None). The mutation is cruder than round 3's renderer-exact one, so `test_the_routing_reader_never_leaves_both_readings` caught it too (624 documents). `tests/test_waiver_decided_at_start.py` did not. The smith's N1 records the renderer-exact mutation and the 225 cases that survived it. That count is round 3's measurement, carried rather than re-run here.

### 🟡 11: the five-input claim holds against the code

The account said the `Reads:` line names five inputs, one more than #922 and round 3 named, and that the fifth is `pact_reviews`. I traced every call of `hidden_lines`, `fence_map`, `unfenced`, `gfm_table` and `read_table` outside `tests/` with `git grep -w` (read).

| Input | How it reaches `hidden_lines` |
|---|---|
| `seal/config.md` | `indexed_config_rows` (`hooks/config.py:366`), `refusal` (`:465`), `skills/implement/scripts/seal.py#table_span` (`:1453`), all through `unfenced`; also `fence_map` called directly by `skills/verify/scripts/broad_gate.py#fence_left_open` (`:1045`) and `skills/implement/scripts/seal.py#write_row` (`:1587`), and `hidden_lines` called directly by `skills/verify/scripts/broad_gate.py#hidden_row_at` (`:976`) · NAME NOT IN TREE |
| `seal/pact.md` | `pact_signers` → `read_table` → `gfm_table` → `unfenced` (`hooks/config.py:1518`, `:1460`, `:1350`); called by `pact_check.py:542` and `chain_check.py:4844` |
| a `seal/pact-changes/` record | `pact_changes` → `gfm_table` (`hooks/config.py:1553`); called by `pact_check.py:807` and `evidence_check.py:5237` |
| a `seal/pact-reviews/` record | `pact_reviews` → `read_table` (`hooks/config.py:1591`); called by `pact_check.py:730` |
| the machine-local pact path map | `skills/evidence-check/scripts/pact_check.py#path_map` → `config.unfenced` (`:302`) |

Five inputs, no sixth. `guess` and `mixed` are unchanged, and `tests/test_a_reader_declares_its_input_class.py` passes (executed). The table also shows where the account is slightly off. Two direct callers of `fence_map` are missing from it, and they are ⬜ 1 and ⬜ 2 below.

### The 23 re-stamped rows hold against the merged sections

From `edcd9c7c` (#917) and `2d4fbdff` (#916), `docs/worktree-guard-spec.md` gained four changes against 0.21.0:

- rule 3's `multiSelect` sentence;
- the prompt budget scoped to the press's own clone, plus two cases on that paragraph's `Enforced by:`;
- the Windows bullet's creation half;
- the press bullet re-wrapped, with its orchestration-section reference shortened.

§*Choice sites* also changed, but no re-stamped coordinate rests on it at a moved hash.

Thirteen families were read against the merged §*Known limits* and §*Creation consent* (read):

- K6, G17, F4, F5, R4, S12, S27 hold, because the bullets they describe are unchanged in substance.
- S9's four Known-limits facts all stand.
- I9's redirected and zsh-prefixed `git` sit at §*Creation consent* lines 200-207.
- S15a's `place` sentence is at line 121.
- S5 is rule 3's new sentence, and its case is on that paragraph's `Enforced by:`.
- Corrected S13 and S14 each name the Windows bullet's creation half and the scoped budget, and both are in the text.

The count is 23: 11 rows in 1791852610's fragment and 12 in 1791852612's. Only the hashes moved. No claim text changed.

One row was left unstamped, and it is right to leave it: `Re-read · S13` in 1791852610's fragment, line 28, still reads `@b08d98e5`. I measured whether anything reads it (executed, by a deleted probe). With that row's hash replaced by zeros, `evidence-check --strict` stays at exit 0, 8,744 ok. With the Corrected S13 row's hash replaced instead, it exits 2 with one DRIFTED. The newer `Corrected · S13` in 1791852612 is the family's reading, and the older row is not judged.

### The #871 seam

The branch touches `hooks/config.py` at one line, 189, the `Reads:` line, and nothing else (`git diff --stat`: 1 +, 1 −). #871's rewrite will conflict there only if it rewrites that docstring line too.

## Stage 2 — quality

The branch adds no code, so stage 2 covers prose and records. Correctness, removed behaviour and cross-file effects were all checked above. Two notes, both ⬜, about the route rather than the inputs.

### ⬜ 1 — N3 says the inputs arrive "all through `unfenced` but one", and three `seal/config.md` paths bypass it

N3, the ledger row at `seal/ledger/1791867522-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs.md:3`, lists `seal/config.md`'s callers as `config_rows`, `indexed_config_rows`, `refusal`, `table_span` and `hidden_row_at`, "which calls `hidden_lines` directly". `fence_map` is called directly by `broad_gate.py#fence_left_open` (`:1045`) and by `seal.py#write_row` (`:1587`), and both read `seal/config.md` without going through `unfenced`. The input set is right, so no reader is misled about which files reach the function. The caller list is short by two. This is the run's paperwork, so it is a correction.

### ⬜ 2 — the `Reads:` line says "through `unfenced`", and `seal/config.md` also reaches it through `fence_map` and directly

`hooks/config.py:189` names the five inputs correctly. Its route, "through `unfenced` and `hooks/blocks.py#walk`", leaves out the three direct paths above. All three carry `seal/config.md`, which the line already names, and the class and direction the census reads are right. So nothing a check reads is wrong, and the release ships no defect if this stands. The text below is offered for whoever next opens the line, for example #871.

```python
    Reads: guess — the lines of `seal/config.md`, `seal/pact.md`, a `seal/pact-changes/` record, a `seal/pact-reviews/` record and the machine-local pact path map, through `unfenced`, `fence_map` or directly, and `hooks/blocks.py#walk`; unknown mixed
```

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | N3's caller list says the inputs arrive "all through `unfenced` but one" and omits `fence_map`'s two direct callers, `broad_gate.py#fence_left_open` and `seal.py#write_row`, both reading `seal/config.md` | `seal/ledger/1791867522-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs.md:3` | open | read: `git grep -w` of every `fence_map`, `unfenced`, `hidden_lines`, `gfm_table`, `read_table` call outside `tests/`; `broad_gate.py:1045`, `seal.py:1587`. The input set is right; the route is short by two |
| ⬜ 2 | the `Reads:` line's route, "through `unfenced` and `hooks/blocks.py#walk`", omits the direct paths through `fence_map` and `hidden_row_at`; every input is named and class and direction are right | `hooks/config.py:189` | open | read: the same grep; `broad_gate.py:976`, `:1045`, `seal.py:1587`. Wording only; nothing a check reads moves |
| 🟢 | #872 round 3's 🟡 10 is closed — both declaring clauses scoped past a fence that closes, the comment half pinned, both routing cases on `Enforced by:` | `docs/the-evidence-ledger.md:638-664`, `tests/test_routing_is_recorded.py:834` | confirmed | read: `shown` and `hidden_lines` against the wording, R8 at `tests/block_shapes.py:198`. Executed: the new case red under a mutation of `shown`, green on the tree; the four narrow modules pass |
| 🟢 | #872 round 3's 🟡 11 is closed — the `Reads:` line names all five inputs the function is handed, `pact_reviews` the fifth | `hooks/config.py:189` | confirmed | read: every caller traced (table in the prose). Executed: `tests/test_a_reader_declares_its_input_class.py` passes |
| 🟢 | the 23 rows re-stamped in 1791852610's and 1791852612's fragments hold against the merged §*Known limits* and §*Creation consent* | `seal/ledger/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis.md`, `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md` | confirmed | read: each of the thirteen families' claim text against the merged sections, rule 3 and the Windows bullet included. Executed: `evidence-check --strict .` exit 0, 8,744 ok, 0 drifted |
| 🟢 | the doc edits rewrite in place with no change narrative, and `hooks/config.py` changes at the `Reads:` line only | `docs/the-evidence-ledger.md:638-651`, `hooks/config.py:189` | confirmed | read: the diff against `2d4fbdff` |

## Executed probes

| What was run | Result |
|---|---|
| `bin/evidence-check --strict .` in the clone at `7db671f0` | exit 0; total 8,744 ok, 0 drifted, 0 broken |
| `bin/test` on `tests/test_routing_is_recorded.py`, `tests/test_a_reader_declares_its_input_class.py`, `tests/test_a_folded_statement_names_what_enforces_it.py`, `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, with `SPECSEAL_CASE_CEILING_S=600` | exit 0, 251 passed |
| `bin/test` on `tests/test_no_real_identifiers.py`, `tests/test_docs_line_wrap.py`, `tests/test_a_document_has_room_for_the_next_fold.py`, `tests/test_one_word_one_meaning.py`, `tests/test_no_passage_is_pasted_into_a_second_file.py`, same ceiling | exit 0, 117 passed |
| `bin/test` on `tests/test_a_released_row_is_read_again_in_a_fragment.py` and `tests/test_the_ledger_fragments_fold_at_release.py`, same ceiling | exit 0, 535 passed |
| a `test_tmp_` probe, run once and deleted: `shown` mutated to hide every line below a line-start comment opener with no closer after it, then the three routing modules, file restored from held bytes | routing module exit 1, the new case alone failing (`parse` returned None); renderer module exit 1 (crude direction); waiver module exit 0 |
| a `test_tmp_` probe, run once and deleted: the `Re-read · S13` row's Known-limits hash in 1791852610 zeroed, then the `Corrected · S13` row's in 1791852612, `evidence-check --strict .` after each, restored from held bytes | first: exit 0, 8,744 ok; second: exit 2, 1 drifted. The older row is not judged |
| the broad gate — full suite, repository lint, typecheck | not yet. It is not run by this round, and the sealer answers it |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Regression tests to plant

None. The comment half now has its case, and the fence half is R3. The S13 family probe measured `evidence-check`'s existing family rule and nothing this branch changed.

## Facts for the evidence ledger

- N3's caller list, if ⬜ 1 is taken: `seal/config.md` reaches `hidden_lines` also through `fence_map`, from `skills/verify/scripts/broad_gate.py#fence_left_open` and `skills/implement/scripts/seal.py#write_row`.

## The broad gate

Not yet. Nothing in this round needs a fix, so the sealer's spawn has come due once the orchestrator verifies this report. The smith's handover labels the suite `unverified` with the sealer as its answerer, and that label is honest. No broad run happened on this branch.

Needs a fix: no
Loses a record or crashes: no

## Proof block

Files opened in this round, all at `7db671f0` in the clone unless noted:

- `docs/the-evidence-ledger.md` (lines 600-670)
- `docs/worktree-guard-spec.md`: §*Known limits* in full, §*Creation consent* searched, and the diff `321e9de1..2d4fbdff`
- `hooks/config.py` (lines 140-260, 1575-1600, and every `unfenced`, `hidden_lines`, `gfm_table`, `read_table` call site)
- `hooks/routing.py#shown`
- `skills/evidence-check/scripts/pact_check.py` (lines 280-305 and the call sites)
- `skills/implement/scripts/seal.py` (lines 1575-1592)
- `skills/verify/scripts/broad_gate.py` (lines 960-980, 1035-1048)
- `skills/evidence-check/scripts/evidence_check.py` (`newest_hash`)
- `tests/block_shapes.py` (R shapes)
- `tests/test_routing_is_recorded.py` (the new case)
- `seal/ledger/1791852610-…`, `seal/ledger/1791852612-…`, `seal/ledger/1791852615-…`, `seal/ledger/1791867522-…` (the diff)
- `seal/releases/0.18.0.md`, `0.20.0.md`, `0.21.0.md` (the thirteen families' claim text)
- `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/rounds/round-3.md`, `round-3-report.md`, `changelog.md`
- `seal/specs/1791867522-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs/overview.md`, `routing.md`
