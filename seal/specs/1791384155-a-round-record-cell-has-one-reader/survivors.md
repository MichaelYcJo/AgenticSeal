# Survivors — a round-record cell has one reader

`survivor-check --range origin/release/v0.21.0...HEAD`, run 2026-10-12 at
the end of the build (b251dafe), named 32 places carrying wording the range
removed. Two were false and were corrected in the same pass: the docstring of
`test_pass_is_ticked_when_nothing_is_open_and_the_gate_is_the_flag`, which
said `run_check` tells the check `draft`, and the 2026-09-14 measurement in
`test_the_empty_span_repair_did_not_widen_the_shared_separators`, which now
says where the home is read since #866. The rest are true where they stand
and are excused below.

| Path | Quote | Grounds |
|---|---|---|
| `seal/releases/0.8.0.md` | The record already carried the fact and one reader looked at it. | a released row's notes, history of 0.8.0, frozen by `Ledger frozen from`; R11 itself is superseded by this item's `Corrected · R11` |
| `seal/releases/0.8.0.md` | The direction is ALLOW, one record wider in one sequence, and it is the cheaper mistake because the only way to satisfy the old walk was rewriting | the same released row; its claim stands and `record_facts`' docstring carries the reasoning now |
| `seal/releases/0.8.0.md` | Two readings a later change would take in good faith are refused here | released row F9's notes; superseded by `Corrected · F9`, and the reasoning is true of `floor_walks` |
| `seal/releases/0.10.0.md` | The tidy-up is judging it ready, since a ready pull request is what the gate is for. | released row S7's notes, true of 0.10.0's gate; superseded by this item's `Corrected · S7` |
| `seal/releases/0.11.4.md` | applies it to the verdict cell one line before | a released row's 2026-09-14 measurement, true of the code it measured; the test docstring that carried the same measurement now says what changed in #866 |
| `seal/releases/0.11.5.md` | Why the fallback still refuses: | a released row whose claim holds: the depth refusal's direction is unchanged |
| `seal/releases/0.19.0.md` | test_a_foreign_range_with_no_open_row_reads_no@ed0177c1 | a released row's coordinates; #860's `Corrected · A1` cites it and was re-stamped by this work |
| `seal/specs/1790815615-the-seal-names-what-it-sealed-and-counts-only-the-steps-that-run/overview.md` | reads the home off the same verdict cell | a released work item's memo, true of 0.17.0's panel; retired by `settle`, not edited |
| `seal/specs/1790815615-the-seal-names-what-it-sealed-and-counts-only-the-steps-that-run/spec.md` | because the letter twin exists for a console that is not UTF-8 | the same released work item's spec |
| `seal/specs/1790815615-the-seal-names-what-it-sealed-and-counts-only-the-steps-that-run/plan.md` | A console that is not UTF-8 is what the letter twin exists for | the same released work item's plan; the panel still writes a home in ASCII for that reason |
| `seal/specs/1790993139-the-release-seal-is-drawn-and-attached-at-publish-time/spec.md` | is the set of distinct issue numbers named in a Verdicts cell whose verdict word is | a released work item's spec, true of 0.18.0's release seal; superseded by this item's `Corrected · C3` |
| `skills/code-review/scripts/chain_check.py` | flag was considered for the local case and rejected for the | `pull_request_state`'s docstring, true: the reasoning the document's reworded paragraph keeps in fewer words |
| `skills/code-review/scripts/chain_check.py` | becomes the quietest way | the same docstring's table, true |
| `skills/code-review/scripts/chain_check.py` | not where, which is the state a | the comment on `DEFERRED`, true; the document's paragraph was shortened and says the same |
| `skills/code-review/scripts/chain_check.py` | empty for a record this cannot read: the | another function's docstring, true of it |
| `skills/code-review/scripts/round_record.py` | Where the range cannot resolve one, it still refuses and says so. | `depth_two`'s docstring, true: the fallback is unchanged |
| `docs/review-chain-spec.md` | Every record after a reopening answers to THAT round rather than to the one that met the floor. | the floor's rule, true; `record_facts`' docstring states the same |
| `docs/review-chain-spec.md` | The direction is ALLOW, one record wider in that one sequence | the floor's rule, true |
| `docs/review-chain-spec.md` | The row still reads | the floor's rule, true |
| `docs/round-record-spec.md` | It refuses because that is the direction every verdict the checker cannot read takes | the depth fallback, true |
| `docs/the-review-and-parity-arms.md` | The shell discards it, git never sees it, and the word stays in the command where shell history keeps it | the waiver's spelling, a different subject sharing the phrase *stays in the command* |
| `hooks/gate.py` | The ways on name commands that run. | the commit gate's waiver, a different subject |
| `agents/warden.md` | keys its depth refusal on a finding | the warden's split rule, true: `close` keys its depth refusal on the `Location`, read as path forms |
| `templates/sdd-round.md` | The row then reads | the template's floor note, true |
| `tests/test_chain_check_at_the_pull_request.py` | Treating it as a draft would make | a case's docstring about the unknown state, true |
| `.github/scripts/release_completeness_check.py` | a session running this by hand has no such commit and gets | a different subject sharing *a session running … by hand* |
| `skills/verify/scripts/broad_gate.py` | no pull request to read. | the milestone step's sentence, a different subject |
| `tests/test_a_release_cannot_ship_an_untrue_milestone.py` | A session running this outside CI has no pull request | a different subject |
| `.test_durations` | test_one_thing_named_is_not_two[Opus 5] | timing data for pytest-split, not prose |
| `.test_durations` | test_an_untracked_file_under_a_work_item_is_work_in_progress | the same data; the ids of the two removed home cases stay in it until the next `--store-durations` run |
