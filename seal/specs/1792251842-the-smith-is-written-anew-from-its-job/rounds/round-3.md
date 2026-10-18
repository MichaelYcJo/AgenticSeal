# 1792251842-the-smith-is-written-anew-from-its-job — review round 3

target: 700a8a08, fixes 21321cd1..700a8a08

## Findings

### 1. The memo's Q1 row still says the item's total is 227.8875, one row above the row that makes it 233.3384

severity: should
location: `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:36`
verdict: open
reopens: round-2#2

Why the close does not hold. Round 2's finding 2 was that the memo did not
account for the smith's third take, and it named `overview.md:36`, the Q1
row, whose Grounds then read "the item's total is 227.8873". eb75405c added
the third take's row below it and corrected the figure to 227.8875, but
left the sentence in the present tense. So the memo now states the item's
total twice with two values: row 36's Chosen cell says "the item's total is
227.8875", and row 37's Grounds say "the item's evaluation total is
233.3384". A reader who takes the memo's total for the pull request body or
the next item's budget, the sealer among them, has two to choose from, and
the first one met is the one that stopped being true at 2c7716bd.

Read. The class is every statement of the item's total in the records.
`overview.md:37` states 233.3384 and is right. `phases/phase-5.md:81` and
`:85` state 227.8875, inside the paragraph on the item passing Q1's stop
before phase 4's second take, written when phase 5 closed; a phase record is that
phase's account and stays as written, so they are not part of this
finding. No other record states an item total (the sweep is under
`## Probes`).

Executed. The figure itself is right: 104.1452 + 60.5128 + 63.2295 =
227.8875, under the rounding rule `## Confirmations` names. Only the
tense is wrong.

```diff
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md
@@
-| Q1's spend stop passed (phase 4's second take) | `questions.md` Q1: this item stops before the next agent once its summed spend passes $150 | phase 1 spent 104.1452 and phase 4's first take 60.5128, so the item stood at 164.6580 before the second take, which spent 63.2295 more; the item's total is 227.8875 | the owner, asked on 2026-10-18 whether to spend about $60 past the night's $200, answered "decide and go with your recommendation", and the orchestrator took the second take; the `## Not verified` row below is closed with that answer |
+| Q1's spend stop passed (phase 4's second take) | `questions.md` Q1: this item stops before the next agent once its summed spend passes $150 | phase 1 spent 104.1452 and phase 4's first take 60.5128, so the item stood at 164.6580 before the second take, which spent 63.2295 more and brought it to 227.8875; the smith's third take in the row below brings it to 233.3384 | the owner, asked on 2026-10-18 whether to spend about $60 past the night's $200, answered "decide and go with your recommendation", and the orchestrator took the second take; the `## Not verified` row below is closed with that answer |
```

The rung this round would give it, as the cap's last round: rung 1 of
`docs/the-review-record.md` §*The run*. The branch owns the unit, the fix
is one cell of the memo, and it goes into the diff before the pull request.

answer:

## Confirmations

confirms: round-2#1
Holds. Read: `phases/phase-4.md:38-41` now says the comparison includes
"#969's changes named above", and the paragraph above it (`:25-31`) names
contract §2, one sentence of `agents/warden.md`,
`docs/the-review-record.md`, `skills/code-review/scripts/chain_check.py`
and `agents/sealer.md`. `overview.md:32` ends "#969's changes named here",
after the same list in the same cell. Executed: a sweep across line wraps
of every tracked file under `seal`, `docs`, `agents`, `skills`,
`templates` and `changelog`, round records left out, for "few contract"
and "§2 change" finds only #969's own `questions.md:40`, about a different
fact, as the fix pass's answer said.

confirms: round-2#3
Holds. Executed: the planted case
`tests/test_a_moved_rule_leaves_its_definition.py::test_the_smiths_hand_back_carries_what_it_may_not_record_and_ends_in_no_block`
reads `agents/smith.md` through `SMITH` (`:265`), slices `## Order of work`
to `## Never` and `## Never` to `## Rules`, the headings at `agents/smith.md:23`,
`:59` and `:77`, and flattens whitespace, so the clause wrapped across
`:56-57` is matched. It passed on the tree. `mutation-check` on the one
clause round 2's two mutations did not touch, making "a leftover for
`seal/follow-up.md`" read "a leftover for `seal/later.md`", gave `red`,
the case failing at `:547`, and `agents/smith.md`'s sha256 was the same
before and after. `ruff check` and `ruff format --diff` are clean on the
module. Read: no paragraph of `## Order of work` or `## Never` carries an
`Enforced by:` line, so nothing had to be re-pointed, as the answer says;
`bin/rules --check` resolves all 483 targets.

confirms: none
Every spend figure in `phases/phase-1.md`, `phases/phase-4.md`,
`phases/phase-5.md`, `overview.md` and `changelog.md` recounts from the
eval JSONs' top-level `costUsd`, and the records add up to one total,
233.3384, under one rounding rule: each side's `costUsd` is rounded to
four places, half up, and the totals are sums of those rounded figures.
Executed, read only, over `evals/baseline-<a>.json` at 700a8a08, the three
`evals/<a>-phase-4.json` at 668fd5f4 (first take) and at 6f3ee98b (second
take), `evals/smith-phase-4.json` at 700a8a08 (third take) and the cut-short
warden's `raw.json` under `SpecSeal-worktrees/967-baseline-raw/warden-cut-short-1`:
phase 1 sides 6.6210, 42.2333, 16.9055 (65.7598), the cut-short warden
34.5493; first take 5.6044, 38.3511, 16.5573 (60.5128); second take 5.3675,
41.7424, 16.1196 (63.2295); third take 5.4509. So 38.3854 = 34.5493 +
3.8361, 104.1452 = 65.7598 + 38.3854, 123.7423 = 60.5128 + 63.2295,
129.1932 = 123.7423 + 5.4509, 164.6580, 227.8875 and 233.3384 = 104.1452 +
129.1932 each follow, and the changelog's and `phases/phase-4.md`'s
percentages (-18.9%, -1.2%, -4.6%, -17.7%) recompute. Summed unrounded, the
same JSONs give 60.5127, 63.2296, 129.1931 and 233.3383: the records differ
from a raw sum by 0.0001 in those four, always by the rule above, and in
no figure by anything else. No record states the rule. The framer's stopped
side, 3.8361, is in no JSON; it is under `## Not judged`.

confirms: none
The changelog's commit coordinate holds. Executed: `git log -1` on each of
the six `evals/<a>-phase-4.json` and `.md` files gives 6f3ee98b for the
warden's and the framer's and 2c7716bd for the smith's, which is what
`changelog.md:46-47` now says. The new memo row's other coordinates hold:
`git log -- agents/smith.md` shows a72d5b53 as round 1's fix to the
definition, and `plan.md:134`, row 4, says "no third run".

confirms: none
The fix range's records and case are green in the modules that read them.
Executed in the clone at 700a8a08: `bin/test` over eleven modules, 681
passed. `git grep -F` over `tests` and `evals` for the changed fragments
("named above as well", "named here as well", "2c7716bd", 63.2295, 123.7423,
129.1932, 227.8875, 233.3384) finds nothing but the planted case's own
name, so no case pins the corrected sentences. The record commit 700a8a08
changes only the three findings' `verdict:` and `answer:` lines of
`rounds/round-2.md`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The framer's stopped phase-1 side, 3.8361 USD, inside 38.3854 and 104.1452: its eval directory was removed in phase 1, so no JSON holds it and this round carried it from the record | `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-1.md:142-145` | the orchestrator, from phase 1's session transcript |
| Whether the item's spend figures should state their rounding rule (each side rounded to four places, then summed), since a reader summing `costUsd` raw gets 0.0001 more or less in four totals | `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md:89-92`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:37` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck on this branch | the branch at 700a8a08 | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the checkout into the round's scratch directory, checked out at 700a8a08 | exit 0 |
| a reader of the top-level `costUsd` of every eval JSON named under `## Confirmations`, at 700a8a08, 668fd5f4 and 6f3ee98b and in `SpecSeal-worktrees/967-baseline-raw/warden-cut-short-1/raw.json`, summing both raw and rounded | exit 0: the figures under `## Confirmations` |
| `git log -1 --format=%h` on each of the six `evals/<a>-phase-4.json` and `.md` files | 6f3ee98b four times, 2c7716bd twice |
| `bin/test tests/test_a_moved_rule_leaves_its_definition.py -p no:xdist -q -k test_the_smiths_hand_back_carries_what_it_may_not_record_and_ends_in_no_block` | exit 0: 1 passed |
| `mutation-check agents/smith.md --replace <OLD> <NEW> --tests "bin/test tests/test_a_moved_rule_leaves_its_definition.py -p no:xdist -q -k test_the_smiths_hand_back_carries_what_it_may_not_record_and_ends_in_no_block"`, OLD the step-10 clause naming the follow-up file and NEW the same clause naming `seal/later.md`; `shasum -a 256` before and after | exit 0: `red`; the hashes equal |
| `uvx ruff check` and `uvx ruff format --diff` on `tests/test_a_moved_rule_leaves_its_definition.py` | exit 0, exit 0 |
| `bin/rules --check --root <clone>` | exit 0: all 483 targets in 60 rule files resolve |
| `bin/test` over `test_a_moved_rule_leaves_its_definition`, `test_no_real_identifiers`, `test_the_record_is_written_in_words`, `test_docs_line_wrap`, `test_one_word_one_meaning`, `test_a_rewritten_definition_proved_non_inferior`, `test_the_set_a_work_item_always_has`, `test_unverified_rows_close`, `test_the_changelog_is_gathered_at_release`, `test_no_passage_is_pasted_into_a_second_file`, `test_every_reader_ends_a_line_where_gfm_does`, `-q` | exit 0: 681 passed |
| `git grep -n -F` over `tests` and `evals` for each changed fragment of the fix range | only the planted case's own definition line |
| `git grep -n -E` over the tree for the old and the raw-sum totals, and for "item's total" and "in all" in the work item's records outside `rounds/` | the old totals only in round records; the totals at `overview.md:23`, `:36`, `:37`, `phases/phase-1.md:145`, `phases/phase-4.md:92`, `phases/phase-5.md:81` |
| a sweep across line wraps of tracked files under `seal`, `docs`, `agents`, `skills`, `templates`, `changelog`, round records left out, for "few contract" and "§2 change" | exit 0: #969's `questions.md` alone |
| `git diff 21321cd1..700a8a08 -- <work item>/rounds/round-2.md` | three `verdict:` and three `answer:` lines, nothing else |
