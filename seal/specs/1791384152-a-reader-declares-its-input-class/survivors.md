# Survivors — a reader declares its input class

`survivor-check --range origin/release/v0.21.0...HEAD` names each place that
still carries wording this item's range removed. Each row below was read at
the branch's head, and its grounds say why the standing text stays.

| Path | Quote | Grounds |
|---|---|---|
| `tests/test_a_phase_hands_the_next_one_a_record.py` | Issue #107 is the worked failure: phase 4 of an earlier work item moved a rule out of `agents/smith.md` into an interim home | The module's docstring tells #107 as the reason a build phase leaves a record at all, which stays true: the phase record still exists for it. The removed copy was the retired removal table's comment in `templates/sdd-phase.md`, whose job moved to the frame's `## Removes`; the same docstring now says a phase record carries no removal table |
| `skills/evidence-check/scripts/correction_check.py` | work-item id — write the epoch prefix of the first work item the | `correction_check.py#cutoff_at` reads `Ledger frozen from` out of `seal/config.md` at a git revision, and its refusal is its own sentence for that input. The sentence this range moved is still produced, word for word, by `evidence_check.py#cutoff_row` for the freeze row, so both readers still say the same thing; reading the revision through `cutoff_row` would change what `correction-check` reads, which is not this item's |
