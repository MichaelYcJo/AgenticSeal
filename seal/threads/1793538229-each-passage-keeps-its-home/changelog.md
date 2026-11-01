### Changed

- **Three passages that restated a rule now stand in one file, and the paste check no longer counts a passage two agent definitions share (#1231).** `agents/crafter.md` step 5 cites `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* for the test-first order instead of repeating it. `skills/implement/SKILL.md` cites `docs/one-root-by-lifetime.md` for why the two language rows are independent, and cites contract rule 5 for what an unlabelled fact is. The instructions mean what they meant before. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` leaves out a pair of two files under `agents/`, because a sentence two definitions share states a fact about each file that holds it. A definition paired with a skill or a document is still counted, so a skill that pastes a definition's prose is refused. The module's stored table of allowed counts drops from 16 entries to the two `README.md` entries that #1102 removes.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-01 | `agents/crafter.md` *Order of work* step 5 cites `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* for how a unit that adds behaviour is built, and no longer restates the order | The crafter opens that skill at step 1, so a second copy could only drift from it | https://github.com/MichaelYcJo/AgenticSeal/issues/1231 |
