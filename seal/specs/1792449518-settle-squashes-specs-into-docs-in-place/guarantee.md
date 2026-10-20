# 1792449518-settle-squashes-specs-into-docs-in-place — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 48486293 against adac0891 |
| Broad gate | feb20458 against adac0891 |

`broad-gate.md` names feb20458, an ancestor of HEAD. The one commit after it,
48486293, touches only `broad-gate.md` and `overview.md` under this work
item's directory (`git log --no-merges --name-only feb20458..HEAD ^adac0891`,
executed). The run's log in the orchestrator's scratchpad reads
`BROAD GATE PASSED … @ feb20458`, `7311 passed · 12 skipped`, `chain ✓ exit 0`
(read). Every re-run below was made in a clone at 48486293 under the
sealer's scratchpad. Where a case pins code that did not exist at the base,
"the code before the change" is the fix removed by hand in that clone, and
the row says so. The clone was restored after each run and removed at the
end.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Both model pins went red with the four carriers back at their old text (5 failed) | `phases/phase-5.md:53-54` | `git checkout adac0891 -- skills/implement/SKILL.md agents/framer.md README.md README.ko.md`, then `bin/test tests/test_settle_reads_before_it_removes.py::test_the_implement_skill_states_the_model tests/test_settle_reads_before_it_removes.py::test_every_other_carrier_points_to_the_model tests/test_waiver_decided_at_start.py::test_the_framer_writes_rule_changes_from_the_index -q -p no:randomly -p no:xdist` | holds: exit 1, 5 failed. The two pins named are 4 of the 5; the framer pin is the fifth. Executed |
| Merge order missed a moved directory, and a case found it red before `--no-renames` | `phases/phase-2.md:25-28` | `--no-renames` removed from `rule_changes.py#order`, then `bin/test tests/test_settle_applies_rule_changes_in_place.py::test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it` | holds: exit 1, "no commit on main adds its spec.md". Executed |
| S10 is seen red with the replay comparison stubbed to accept | `phases/phase-3.md:65-69`; `plan.md:109` | `unverified_check.py:1323` replaced by `if True:`, then `bin/test` over `test_a_removal_whose_rule_docs_does_not_hold_still_fails`, `test_a_settled_work_item_is_not_read_as_this_branchs_deletion` and `test_a_rule_change_half_applied_is_not_settled` | holds: exit 1, 3 failed (S10 and both half-applied rows), and the S9 control passed. Executed |
| The fix pass's new cases fail against round 1's scripts (10 failed) | `rounds/round-2.md:162`; the pull request body's verification table | `git checkout a8bd7772 -- skills/settle/scripts/rule_changes.py skills/settle/scripts/settle.py skills/settle/scripts/fold_check.py skills/verify/scripts/unverified_check.py`, then `bin/test tests/test_settle_applies_rule_changes_in_place.py -q -p no:randomly -p no:xdist` | holds: exit 1, 10 failed and 51 passed. The ten are the four Windows values, the two sentinel near misses, the nested wait, the `S child` conflict and both case variants. Executed |
| Every unit added in `settle.rule_plan` is caught, the three survivors included once they got cases | the pull request body's verification table, first row (no phase record states it; commit 1c01de0c's subject says "the cases mutation found missing") | three runs, one mutation each in `settle.py#rule_plan`: the spec read from disk instead of the released ref, the no-adding-commit hold dropped, the parse-error hold dropped; each followed by `bin/test` over `test_the_text_applied_is_the_spec_as_released`, `test_a_spec_no_commit_adds_is_held` and `test_a_section_that_does_not_parse_keeps_its_directory` | holds: each run exited 1 with exactly the one case that pins its mutation failing. That the three survived before the cases existed was not re-run. Executed |
| `fold-check` names the two documents past 25000 and exits 0 | `spec.md:171-174`; `overview.md:36`; the pull request body, "One read" | `bin/fold-check --root <clone>` | holds: exit 0, `docs/one-root-by-lifetime.ko.md` about 28936 and `docs/worktree-guard-spec.md` about 37178, and "the index docs/README.md names every document". Executed |
| `settle --retire` and `settle --retire-process` get an argument error, exit 2 | `changelog.md:19-20`; the pull request body | `bin/settle --root <clone> --retire`, the same with `--retire-process` | holds: exit 2 for both, "unrecognized arguments". Executed |
| `git grep -n "one writer that does is"` returns only the case asserting its absence | `phases/phase-5.md:51-52` | `git grep -n -F "one writer that does is" -- . ':!seal/specs' ':!changelog' ':!CHANGELOG.md'` | holds: two hits, `tests/test_settle_reads_before_it_removes.py:802` and `:813`, both `not in` assertions. Executed |
| The CI run at a8bd7772 failed and the run at 0e93d61d passed on every leg | the spawn prompt; the pull request body's verification table | `gh run view 39346594309` and `gh run view 39348926688`, `--json headSha,conclusion,jobs` | holds: 39346594309 at a8bd7772 is `failure`, with failing legs on ubuntu, macOS and Windows. 39348926688 at 0e93d61d is `success` on lint, ubuntu, three macOS and four Windows splits. Which cases failed on each leg was not opened. Read |
| `## Removes`: the marker as fold record, the spec-less predicate, both arms and their flags, the freeze, the line row, the restated values, the index table, "the one writer", the session-writes split, the marker-based cases, the docs-edit sentences, the old release sequence | `spec.md:199-213` | `git grep -n -F` over the tree outside `seal/specs`, `changelog`, `CHANGELOG.md` and `.test_durations`, for each of the 53 symbols, case names and sentences the rows list, and `ls` of the two removed test files | holds: 44 come back empty, and both files are gone. Of the 9 with hits, 8 are cases asserting the text absent or refused (`test_a_document_has_room_for_the_next_fold.py:182`, `test_settle_applies_rule_changes_in_place.py:654`, `test_settle_reads_before_it_removes.py:732`, `:793`, `:802`, `:813`, `:916`), cases `## Removes` says are rewritten under their old names, or `seal.py#work_item_of`, which `overview.md:18` keeps. The ninth is a width fixture string that still names the removed case (`tests/test_docs_line_wrap.py:378-379`, `WIDE_TARGET`). Nothing resolves that string, so it is no live carrier. Executed |
| The changelog's removals: no `Over the ceiling` read, no line row, no marker written | `changelog.md:29`, `:33-35` | the same search; `seal/config.md` read | holds: `seal/config.md` holds `Document token ceiling | 25000` and neither old row. `git grep -c` counts 127 live `<!-- specs/` lines in `docs/`, the framing's 129 less the 2 that left with the line-ceiling statement (`overview.md:21`). Executed |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the issue body (#953) | a spec states its rule changes, a pull request does not edit `docs/`, `settle` applies in place in merge order and removes what it applied, one read, an index, the policy root a row, settle when the owner calls it, local mode is #955 | the spec; the tree (`skills/settle/SKILL.md`, `rule_changes.py`, `settle.py`, `unverified_check.py#settled`, `fold_check.py`, `docs/README.md`) | item 4's split "in the same pull request" is overturned by the owner's Q6 answer (`questions.md:55`, read; the answer was put to the owner by the orchestrator, and that is not verified here) |
| the spec | as the issue, with Q6's report, the grammar pointed to the skill, and this item's own `docs/` edits made in its diff (`## Rule changes`: `nothing — …`) | the issue; the build; `overview.md`'s divergence rows, each with grounds | none that stands: S12's exit 1 and the 37,178 value were revised to Q6 (`spec.md:168-174`, `:204`) |
| the build (diff, phases 1-5, `overview.md`) | five phases as planned, with the divergences `overview.md:12-25` records | the spec, the issue and every claim re-run above | none |
| the last round (round 2) | all ten round-1 findings confirmed at fedc2790, nothing opened; Q2, Q3 and Q4 named as the owner's and a measurement's | the build; the re-run of its 10-failed claim | none |
| the changelog | the five `Changed` entries | the tree and the claims re-run above | none |
| the pull request body | the changelog's entries, the installed-repository notes, the decisions, the verification and the gate notes | the changelog, the records and the tree, except one sentence | its second bullet, quoted under the verdict, says the opposite of `changelog.md:12-16` and of the tree |

The second bullet of the pull request body reads:

> A spec it cannot place, one whose record holds an open row, and two that
> merge order cannot decide at one place are refused at their line. A section
> and a sub-section it holds count as one place. So is a `file:` holding `\`
> or `:`, one differing from another document only in case, and a `nothing`
> line written with a hyphen, which is told to use the em dash.

The changelog carries the place rule as a parenthesis inside the refusal
sentence, so its next sentence's "So is" means *refused too*:

> … and two that merge order cannot decide at one place (a section and a
> sub-section it holds are one place) are refused at their line and stay. So
> is a `file:` holding `\` or `:`, …

The body moved the parenthesis into a sentence of its own. "So is" now
follows "count as one place", so the body says a `file:` holding `\` or `:`,
a case variant and a hyphenated `nothing` each count as one place. The tree
refuses all three. `rule_changes.py:166-169` refuses the `file:`,
`settle.py:300-303` holds the case variant, and `rule_changes.py:111-116`
refuses the hyphen, naming the em dash.

Verdict: withheld — the pull request body's second bullet, "So is a `file:` holding `\` or `:`, one differing from another document only in case, and a `nothing` line written with a hyphen", follows "A section and a sub-section it holds count as one place", so it says those three count as one place. `changelog.md:12-16` makes them refusals, and so does the tree (`skills/settle/scripts/rule_changes.py:166-169`, `skills/settle/scripts/settle.py:300-303`, `skills/settle/scripts/rule_changes.py:111-116`). The fix is the body's sentence order: put the place sentence before the refusal sentence, or open the last sentence with "Refused too:". Everything else this audit re-ran or read holds.
