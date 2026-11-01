# Closing memo: 1793521559-a-finding-is-counted-once

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set, the plan's two modules with every module that loads `chain_check.py`, reads `.github/scripts/` or reads the records under `seal/threads/`, and ran `ruff check` and `ruff format --check` on its changed Python files alone (contract rule 2) | answered by `trail/gate.md`: the broad gate row of `seal/config.md`, the full suite with the repository-wide `ruff check` and `ruff format --check`, passed at `91fe3b4d against ad5246ce` (read by the settle that opens 0.27.3) |
| closed S9: that the chain check reads this design's `## Rule changes` with no refusal at the branch's head. The framer's probe parsed them at e156cf3b (`frame/design.md` *Grounding*, the `## Rule changes` row), and phase 1 did not run the check | answered by `guarantee.md` *Claims re-run*, the row *S9*: the sealer parsed the design's `## Rule changes` with `rule_changes.parse`, matched each `from` in its section, and ran the chain check (executed) |

## Not done

`.github/scripts/finding_counts.py`'s `chained`, `item_counts`, `load` and `readers` have no test class of their own, which `seal layout --check` reports and does not refuse. Each is reached through `main`. The mutation table in `trail/phases/phase-1.md` shows a case of `Test_main` going red under a mutation of each arm of `chained` and `item_counts`. `load` and `readers` hold no arm, and a reader that will not load is `Test_main`'s readers case. A class per function would restate those cases one call lower and would catch nothing more.
