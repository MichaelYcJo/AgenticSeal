# 1791779434-under-automation-the-guard-asks-nobody — round 2 fixes

Fix range: `c67fc2e5..1ac03f4d`.

## Fixes

| # | Verdict | Commit or grounds |
|---|---|---|
| 1 | fixed | 04f450ea — the report's paste-ready text: way 1 now names `--orphan`, which starts from an empty tree no pop carries onto, in both languages, the policy paragraph and the changelog fragment; `test_an_orphan_switch_under_the_press_takes_the_commit_way` runs way 1 with real git, seen red through `mutation-check` with the sentence removed (the case was removed at the reframe after round 3: NAME NOT IN TREE) |
| 2 | fixed | 8c1db4bd — the report's paste-ready text: the premise says a switch that keeps the changes carries them, in both languages and the policy paragraph, with the attended `ask` untouched; `test_the_deny_does_not_say_a_discarding_switch_carries_the_changes` pins `--discard-changes`, `-f` and `--orphan`, seen red through `mutation-check` with the old premise restored (the case was removed at the reframe after round 3: NAME NOT IN TREE) |
| 3 | answered | corrected at 1ac03f4d — 0.15.6 W9's re-read row in the 1791384157 fragment is back at `main@08a308fb`, as A4 and S2 stand; `--reverify` left it there because `Corrected · W9` supersedes the family |

Round 1's ⬜ 5 grounds ("the base's `ask` text, carried word for word")
were wrong, as round 2's 🟡 2 found: the premise was this item's own sentence
from c68fa49b. 🟡 2's fix is the repair.

## Fix surface

| Field | Value |
|---|---|
| Contract changes | none |
| New units | `tests/test_the_guard_asks_once_per_session.py#test_an_orphan_switch_under_the_press_takes_the_commit_way`, `tests/test_the_guard_asks_once_per_session.py#test_the_deny_does_not_say_a_discarding_switch_carries_the_changes` (both removed at the reframe after round 3: NAME NOT IN TREE) |
