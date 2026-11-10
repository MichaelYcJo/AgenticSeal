# Guarantee: 1794289596-implement-orchestration-grew-back

Audited on 2026-11-10 by the sealer, at `aac059556` against the base
`release/v0.37.2`, whose `@{upstream}` resolved to `1959c3ea1`; the local
ref stands at `df775c52c` and was not used (`executed`: `git rev-parse
--verify --quiet` on the three forms). The gate record `trail/gate.md`
names `run: 6e10f7ed8 against 1959c3ea1`. `6e10f7ed8` is an ancestor of
HEAD, and the one commit after it, `aac059556`, touches only
`trail/gate.md` (`executed`: `git merge-base --is-ancestor` and `git log
--no-merges --name-only 6e10f7ed8..HEAD ^1959c3ea1`). The broad gate's pass
is the orchestrator's account; the sealer read the record and ran nothing
broad (`read`, contract rule 2). `seal pr-body <item> --body <file>
--check` exited 0 with the tree's `bin/seal` and with the installed
plugin's `seal` (`executed`), and the part of the body above `## From the
records` is `pr.md` byte for byte (`executed`, `diff`). The repository
declares no `seal/parity.json` (`executed`: `git ls-files seal/parity.json`
printed nothing), so no comparison with an original is owed.
`chain_check.py --baseline 1959c3ea1 --sealing` exited 0 (`executed`).

The four commits after round 2's record (`41d5fa30f`), `07767cad7`,
`a3777952d`, `c843ba6d7` and `6e10f7ed8`, touch only files under this work
item's directory (`executed`, `git log --name-only`), and both round 2
findings are located there alone. No round read them, so the sealer read
each against what its finding asked, as `skills/core/SKILL.md` *Judgment is
not licence to skip a party*, the row *No fix that no round reads*, has it
in the tree's text; the two rows of the last round below record that read.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The rewritten fold case fails against the order section before the rewrite, on every row whose wording is new, the three new clauses among them | `trail/phases/phase-2.md`, the run against phase 1's text; `trail/phases/phase-3.md`, the case's new phrases | In a clone at HEAD under the scratchpad, `skills/implement/orchestration.md`, `skills/implement/SKILL.md`, `agents/proofer.md` and `agents/crafter.md` restored from `1959c3ea1`: `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_a_decision_after_the_frame_is_folded_into_it` | Holds. Exit 1, one failure at `:622` naming rows 4, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23 and 24 of D1. Rows 22, 23 and 24, the new clauses, are among them; the others are the rows phases 2 and 3 reworded |
| `test_the_planning_row_is_a_record_and_not_a_checkbox` reads the box tables in `routing-question.md`, and was shown red on each of its two guards | `trail/phases/phase-1.md` Exception 4 and its table, the two rows of that case | In the same clone with HEAD's code restored: box 4's label made `**plan with the framer**`, then, restored, the table's header `Box` made `Choice`; each time `bin/test tests/behaviour/test_waiver_decided_at_start.py -q -p no:xdist -k test_the_planning_row_is_a_record_and_not_a_checkbox` | Holds. Exit 1 at `:762`, "the `Planning` axis reached a checkbox table"; exit 1 at `:760`, "the routing question's file holds no table of boxes to read". Each failing line names the guard removed |
| The language-key case reads its paragraph in `routing-question.md` and goes red without `gh pr list --state all --limit 10` | `trail/phases/phase-1.md`, its table, the row of `test_the_batch_asks_for_the_language_rows_and_names_where_a_default_is_recorded` | In the same clone, that phrase removed from `routing-question.md`; `bin/test tests/behaviour/test_waiver_decided_at_start.py -q -p no:xdist -k test_the_batch_asks_for_the_language_rows_and_names_where_a_default_is_recorded` | Holds. Exit 1 at `:873`, "the batch shows no history beside the language question" |
| The modules that read the moved and reworded passages, and S7's two, pass at HEAD | `trail/phases/phase-3.md`, the set at the phase boundary; `frame/design.md` S3, S5, S6, S7 | In the same clone, clean at HEAD: `bin/test` over `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_waiver_decided_at_start.py`, `tests/text/test_review_axes.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/lib/test_core.py`, `tests/hooks/test_core_start.py` and `tests/text/test_a_cited_commit_outlives_the_squash.py`, `-q` | Holds. 280 passed and 1 failed: `test_every_cited_commit_outlives_the_squash` on `frame/plan.md:40` citing `1959c3ea1`, because the clone's `origin/release/v0.37.2` is the worktree's stale local ref. Run in the worktree, where `origin/release/v0.37.2` holds `1959c3ea1` (`git branch -r --contains`), the module exits 0 with 17 passed. The two warnings name `docs/running/the-review-and-parity-arms.md:56` as excused by *Rule changes* (S6) |
| S1: the body holds at most 5,242 words with the release branch merged in; 7,311 at 0.37.1 | `frame/design.md` S1 and G5; `changelog.md` *Changed*, the first item; `gaps.md:7` | `wc -w skills/implement/orchestration.md`; `git show <c>:skills/implement/orchestration.md \| wc -w` for `v0.30.0`, `v0.37.1`, `1959c3ea1` and `a1a93b3b1` | Holds. 5,233 at HEAD and at `a1a93b3b1`; 5,242 at `v0.30.0`; 7,311 at `v0.37.1`; 7,321 at `1959c3ea1` |
| Each phase's count: 5,597 at `4112c5924`, 5,704 and a fold rule of 979 at `500d2cb98`, 5,225 at `02740215a` | `trail/phases/phase-1.md`, `phase-2.md`, `phase-3.md`; `frame/design.md` D3 | `git show <c>:skills/implement/orchestration.md \| wc -w`, and `sed -n 55,139p \| wc -w` at `500d2cb98` | Holds, each number |
| Row 20's counts: round 1's sentence 52 words, the old sentence 43, the built one 41, the body 5,225 at `9c17b22bc`, so 5,244 after #1476 | `frame/plan.md:40`, as folded by `07767cad7` | `sed -n 67,71p trail/rounds/round-1.md \| wc -w`; `git show <c>:skills/implement/orchestration.md \| sed -n 316,319p` at `9c17b22bc` and `f07bd7f60`, each `wc -w` less the two words "Where the" of the next sentence | Holds. 52; 45 less 2 is 43; 43 less 2 is 41; 5,225 + 9 + 10 = 5,244 |
| S4: each new file is named once in the body, in D4's words | `trail/phases/phase-3.md`; `frame/design.md` S4, D4 | `grep -n` of both paths in `skills/implement/orchestration.md` | Holds. `:222` and `:317`, each in the sentence D4 gives |
| No case is added or removed | `frame/design.md` *Removes*, its last paragraph; `frame/plan.md` *Phases* | The `def test_` names of the three changed case modules at `1959c3ea1` and at HEAD, sorted and compared | Holds. The same names in each module |
| Nothing of *Removes* rows 1 to 21 stands in the body, and each moved passage stands in its new file | `frame/design.md` *Removes* | A `python3 -I` read of the body, whitespace collapsed, for a phrase of each row taken from `9e9d1087f`; `grep` of the landed leads in `routing-question.md` and `merge-order.md` | Holds. Every row's phrase is absent. "No check refuses an earlier edit", which row 9 keeps, and "Before it sends", which D1 row 7 keeps, stand. **Ask question 1 alone**, **The ceiling.** and **The exit is last** stand in `routing-question.md`, and the late move's verifying round in `merge-order.md:30`. The migration paragraph is the one sentence row 18 gives, at `:294-297` |
| The removals the changelog names: nine statements, the opening's list, the ladder's two sentences | `changelog.md` *Removed* | The same read | Holds. The nine are *Removes* rows 9, 10, 11, 12 (two), 13, 16, 19 and 20, each absent; row 14's list and row 17's two sentences are absent |
| Each `pr.md` quote stands word for word at its coordinate | `pr.md` | A `python3 -I` comparison, whitespace collapsed, of each quote with the file it names | Holds. 9 of 9 |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | The routing question and the two language keys move to `skills/implement/routing-question.md`, the merge order to `skills/implement/merge-order.md`, each named by one sentence of the body; the fold rule becomes six paragraphs of judgment with every clause of D1; the body drops what another place states; the dated-section rule states its exception at its owner, and the proofer and the crafter carry it; no case added or removed | The issue's *Change* and its three *Done when* lines; the diff; S1 and the counts re-run; the issue's "What it did not catch", which G8 and *Scope* item 9 answer | none |
| the build | Phases 1 to 3, each with its record, at `4112c5924`, `500d2cb98` and `02740215a`, the Status cells of `frame/plan.md`; `routing.md` answers `Implementation` with `crafter`, and each phase whose Status holds a commit has its `trail/phases/phase-N.md` | The design, item by item against the diff (`read`); the claims re-run above; the six paragraphs at `skills/implement/orchestration.md:52-134`, each with a bold lead (`read`) | none |
| the last round | Round 2 at `10fc3a7f7` confirms round 1's three findings, reads the merge of `1959c3ea1`, and names two `should` findings in the records: the count 5,223 in `changelog.md:3`, `pr.md:1` and `gaps.md:7`, and row 20's counts in `frame/plan.md:40` | Finding 1, `fixed a3777952d`, with `6e10f7ed8` for `pr.md`: `changelog.md:3` and `pr.md:1` say 5,233, and `gaps.md:7` is closed in place with the round's text, each count reproducing (`executed`, above). Finding 2, `fixed 07767cad7`: `frame/plan.md:40` holds the round's text with "at `9c17b22bc`" added, and every count reproduces (`executed`, above). Both fixes touch the work item's records alone | none |
| the changelog | *Changed*: the body is under 0.30.0's size at 5,233, and the two files hold what it says and open on the conditions it gives; the fold rule is six paragraphs with two new clauses; the dated-section exception at its owner and in both definitions; the citing files name the new homes. *Removed*: nine statements and the ladder's two sentences. *Process changes*: three rows | The diff and the counts re-run; the files' first paragraphs and the body's sentences at `:222` and `:316-319` (`read`); `docs/running/the-review-and-parity-arms.md:56` still cites *Question 1*, as its closing line says | none |
| the orchestrator's part of the pull request body | Eight quotes of `changelog.md`, the title judgment `refactor:` from `frame/plan.md` *Judgments of the run*, and `Closes #1477.` | Each quote stands at its coordinate; `seal pr-body --check` exit 0; the diff adds no gate, check, hook or script, which the `refactor:` row's grounds say | none |

`routing.md` *Why this way* gives the orchestrator's grounds under
`agentic` for the full route: a framer for the fold rule's rewrite, a
crafter, the review chain and the pull request. The diff is that rewrite,
two moved passages, their citations and the dated-section sentence of
*Scope* item 9, which the fold of `8e49bb39b` added with the row of
*Judgments of the run* that records it (`read`). The grounds describe it.

```seal
target: aac059556260830c0f8ec438066ace8dbb0623fb against 1959c3ea1e8b41c76ab54fdbd2fb89f75616cc15
Verdict: sealed
```
