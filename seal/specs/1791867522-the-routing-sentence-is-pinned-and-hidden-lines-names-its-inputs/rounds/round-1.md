# 1791867522-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs — review round 1

| Field | Value |
|---|---|
| Target SHA | 7db671f07e5040e6a0d2d2746d0b614fa8adc96c |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #927 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 1 of #922, target 7db671f0 against `origin/release/v0.21.1` at 2d4fbdff, over the whole branch: round 3 of #872's 🟡 10 and 🟡 11, and the re-reading of 23 ledger rows that drifted on the release branch when #917 and #916 merged. The reviewer was asked to check the five-input claim against the code, to spot-check the re-stamped claims against the merged guard spec, to hold every doc edit to the rewrite-in-place rule, and to confirm the branch changes only the `Reads:` line of `hooks/config.py`.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | N3's caller list says the inputs arrive "all through `unfenced` but one" and omits `fence_map`'s two direct callers, `broad_gate.py#fence_left_open` and `seal.py#write_row`, both reading `seal/config.md` | `seal/ledger/1791867522-the-routing-sentence-is-pinned-and-hidden-lines-names-its-inputs.md:3` | open | read: `git grep -w` of every `fence_map`, `unfenced`, `hidden_lines`, `gfm_table`, `read_table` call outside `tests/`; `broad_gate.py:1045`, `seal.py:1587`. The input set is right; the route is short by two |
| ⬜ 2 | the `Reads:` line's route, "through `unfenced` and `hooks/blocks.py#walk`", omits the direct paths through `fence_map` and `hidden_row_at`; every input is named and class and direction are right | `hooks/config.py:189` | open | read: the same grep; `broad_gate.py:976`, `:1045`, `seal.py:1587`. Wording only; nothing a check reads moves |
| 🟢 | #872 round 3's 🟡 10 is closed — both declaring clauses scoped past a fence that closes, the comment half pinned, both routing cases on `Enforced by:` | `docs/the-evidence-ledger.md:638-664`, `tests/test_routing_is_recorded.py:834` | confirmed | read: `shown` and `hidden_lines` against the wording, R8 at `tests/block_shapes.py:198`. Executed: the new case red under a mutation of `shown`, green on the tree; the four narrow modules pass |
| 🟢 | #872 round 3's 🟡 11 is closed — the `Reads:` line names all five inputs the function is handed, `pact_reviews` the fifth | `hooks/config.py:189` | confirmed | read: every caller traced (table in the prose). Executed: `tests/test_a_reader_declares_its_input_class.py` passes |
| 🟢 | the 23 rows re-stamped in 1791852610's and 1791852612's fragments hold against the merged §*Known limits* and §*Creation consent* | `seal/ledger/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis.md`, `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md` | confirmed | read: each of the thirteen families' claim text against the merged sections, rule 3 and the Windows bullet included. Executed: `evidence-check --strict .` exit 0, 8,744 ok, 0 drifted |
| 🟢 | the doc edits rewrite in place with no change narrative, and `hooks/config.py` changes at the `Reads:` line only | `docs/the-evidence-ledger.md:638-651`, `hooks/config.py:189` | confirmed | read: the diff against `2d4fbdff` |

## Paste-ready fixes

no paste-ready fix in the report

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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
