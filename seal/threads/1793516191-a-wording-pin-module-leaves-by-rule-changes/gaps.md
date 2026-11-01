# Closing memo: 1793516191-a-wording-pin-module-leaves-by-rule-changes

## Not verified

| Item | Who must answer |
|---|---|
| The full suite with the three `to` values standing in `docs/`. Phase 1 ran the thirteen modules of design S3 in a scratch clone and no other module, because the broad run is not the crafter's (contract rule 2) | the settling session, at `skills/settle/SKILL.md` *The settling session's procedure* step 8, over the settle's own pull request |
| The `to` values in the words the settle writes. The rehearsal wrote each `to` as the design spells it; a settle that writes a sentence in its own words meets `seal rules --check`, `tests/behaviour/test_docs_line_wrap.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` with text nobody ran here | the settling session, by the same step 8 |
| Which modules other than the rule reader turn red when the module is deleted. S5 ran `seal rules --check` and `git grep` over the deletion and no test module | the crafter of the successor issue that carries the removal, at that build's phase boundary |

## Not done

The places outside `docs/` that #1197 lists stay as they are, and the module stays. The grounds are `frame/design.md` *Scope*, the first two bullets under Out, and `frame/plan.md` A2: changed before the settle, each would state a false fact until the removal.
