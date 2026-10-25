# 1792368015-every-finding-carries-an-evidence-line — guarantee

| Field | Value |
|---|---|
| Target SHA | b8c96ad2 against c26a791e; earlier run: bf60b581 withheld |
| Broad gate | 58a2100e against c26a791e |

## Claims re-run

This run audits b8c96ad2. The one commit since the earlier run's bf60b581
is b8c96ad2, and it touches only this file (`git log --no-merges
--name-only bf60b581..HEAD`, executed), so no claim's coordinate moved and
the rows executed at bf60b581 stand for b8c96ad2's code unchanged. What
changed is outside the tree: the pull request body's review row, which the
earlier run withheld on, and #985's issue body, which now holds the owner's
decisions under `## Decisions taken during the build`. Both were read again
against the records, and the parties table below is this run's.

The earlier run audited bf60b581. The base is
`release/v0.22.2@{upstream}`, c26a791e. The branch was cut at b196fe9b, and
`git diff --stat b196fe9b c26a791e` over the five code files this item
changes is empty, so b196fe9b's copies are the base's. "At base" means a
`git clone` of the branch at bf60b581 under the scratchpad, with
`agents/warden.md`, `docs/the-review-record.md`,
`evals/scripts/replay_targets.py`, `skills/code-review/SKILL.md` and
`templates/sdd-round.md` checked out from b196fe9b and every test at HEAD.
The clone was removed after. The tree under audit was only read. Its records
were judged with the tree's `chain_check.py`, as this item's grammar
requires.

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD, or only this item's records follow it | `broad-gate.md:5` | `git log --no-merges --name-only 58a2100e..HEAD ^c26a791e`; `git merge-base --is-ancestor 58a2100e HEAD` | holds — two commits: bf60b581, touching `broad-gate.md` and `overview.md`, and b8c96ad2, touching `guarantee.md`, all in this directory; 58a2100e is an ancestor (re-run at b8c96ad2) |
| The sampled new cases pass at HEAD | `phases/phase-1.md:77-91`, `phases/phase-2.md:53-63` | `bin/test -q -p no:xdist` over the six `tests/test_chain_check.py` cases that name the row, the two `tests/test_review_axes.py` pins, `PROBE`'s `test_the_definition_separates_a_coverage_probe_from_a_seal` and the two replay cases, in the clone at HEAD | holds — 12 passed |
| S1 to S6 and the spelling case are red without the row | `phases/phase-1.md:77-80` | the same six `tests/test_chain_check.py` cases at base | holds — all six failed, each on the missing `evidence:` row (the table's label set, `needed` lacking it, `Evidence:` not refused at its line, the malformed findings read, the stand-in sentence absent, the template's line absent) |
| The two record-document pins are red before their paragraphs | `phases/phase-1.md:79-80` | `test_a_later_round_re_runs_an_executed_line` and `test_a_record_written_before_a_line_was_added_is_no_finding` at base | holds — both failed on the missing sentence |
| The moved `PROBE["warden.md"]` pin is red before its text | `phases/phase-2.md:53-57` | `test_the_definition_separates_a_coverage_probe_from_a_seal` at base | holds — `[warden.md]` failed, `[smith.md]` passed |
| The narrowed drift case goes red when the skill's list drops `evidence:` | `phases/phase-2.md:44-51` | in the clone at HEAD, `evidence:` removed from `skills/code-review/SKILL.md:123` with the `Edit` tool, then `TestGrammar::test_the_warden_and_the_review_skill_name_every_line_a_finding_needs` | holds — failed with `§*The record* does not name ['evidence:']` |
| The replay case is red before the per-commit reading | the pull request body, *How it was verified*, row 2; 0a843334, 0a5d3445 | with only `evals/scripts/replay_targets.py` at b196fe9b, the two replay cases | holds — both failed: no `written_at` in the module |
| Round 1 #2's case fails when `targets` drops the writing commit | `rounds/round-1.md:139` | in the clone at HEAD, `replay_targets.py:603` changed to `confirmed(nxt, n, following)`, then `test_targets_reads_the_next_round_by_the_commit_that_wrote_it` | holds — failed with `[(1, 'seal/specs/i/rounds/round-2.md', None)]` |
| Round 3: the encoding census catches `text=True` in the replay case's helper | `rounds/round-3.md:23-25`, `:49` | in the clone at HEAD, `text=True` restored at `tests/test_a_rewritten_definition_proved_non_inferior.py:1567`, then `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | holds — 1 failed, 150 passed; the one site named is `:1563` |
| The warden's preload is 27,168 bytes, and the shipped `agents/warden.md` is the one measured | `phases/phase-2.md:27`, `changelog.md:22-23`, `evals/warden-phase-3.md:89` | `wc -c agents/warden.md skills/agent-contract/SKILL.md`; `shasum -a 256 agents/warden.md` | holds — 10,565 + 16,603 = 27,168; `12c1c4c2…`, the record's hash |
| `evals/warden-phase-3.md` is what the two side files give, and the baseline is #967's side | `spec.md:137` (S12), `phases/phase-3.md:28-31` | `noninferiority.py compare --agent warden --phase 3 --old evals/baseline-warden.json --new evals/warden-phase-3.json --out <scratch>`, `diff`; `noninferiority.py check evals/warden-phase-3.md`; `cmp` of `baseline-warden.json` with `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/warden-phase-4.json` | holds — compare exit 0, `diff` identical; check exit 1: recall 19 to 13, false rate 0.558 to 0.641; `cmp` identical; the side files name revs `af716289` and `ba2a3187`, one suite, neither cut short |
| All 39 findings of the side's 18 final records carry one `evidence:` line, 28 `executed` | `phases/phase-3.md:66-69`, `changelog.md:36-37`, the pull request body | a scratch script over `985-warden-raw/traces/*.jsonl`, replaying each run's `Write` and `Edit` of its round record and counting `### <n>.` sections and `evidence:` lines (deleted) | holds — 39 findings, 39 with one line, 28 `executed`; one `Edit` in `003.jsonl` did not apply in the replay and changes no count |
| `--list` names the same 31 targets as before the row | `changelog.md:50-52`, `overview.md:20`, the pull request body, *What changes*, last bullet | `python3 evals/scripts/replay_targets.py --list` in the worktree, read-only; its kept set compared with the build's `replay-before.txt` and `replay-fixed.txt` in the scratchpad (read) | holds — 32 kept, 57 left out, none for a check's refusal; the 32 are the build's 31, which equal the before-the-row set, plus this item's own round 1, written after the claim; no `specseal-replay-check-*` directory left |
| The item's records pass the tree's check | `rounds/round-1.md` to `round-3.md` | `python3 skills/code-review/scripts/chain_check.py --baseline c26a791e --root <worktree> --worktree` | holds — exit 0 at b8c96ad2 with this file written, and no line refused (re-run) |
| `## Removes` 1 and 2, and the changelog's named removal: the template's "executed and read labelled apart" | `spec.md:172-173`, `changelog.md:24-25` | `git grep -n -e 'labelled apart' -- . ':!seal'` | holds — no hit |
| `## Removes` 3: the review skill's "grounds, executed and read" bullet | `spec.md:174` | the same search, and `git grep -n -e 'executed and read$' -- . ':!seal'` | holds — no hit |
| `## Removes` 4: the warden's coverage-probe sentence | `spec.md:175` | `git grep -n -e 'is not that run' -- . ':!seal'` | holds — no hit; `agents/warden.md:153-156` holds the absence rule |
| `## Removes` 5: the old `PROBE["warden.md"]` pin | `spec.md:176` | `git grep -n -e 'catches this — is a different' -- . ':!seal'` | holds — no hit |
| `## Removes` 6: "rewrites its records into the shape before its pull request goes ready" | `spec.md:177` | `git grep -n -e 'rewrites its records into the shape' -e 'Nothing reads a record of the old' -e 'read by nothing again' -- . ':!seal'` | holds — no hit |
| The base's advance past b196fe9b (#970) touches none of this branch's files | the spawn prompt | `git diff --name-only b196fe9b c26a791e`; `git merge-tree --write-tree --name-only HEAD c26a791e` | does not hold — both change `tests/test_review_axes.py`, at different places; the merge is clean (exit 0, no conflicted path). The broad run at 58a2100e ran the branch's tree, not the merged one. This is the prompt's claim, not a party's, and the verdict does not rest on it |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | one `evidence:` row, a finding, `one`; three meaning paragraphs; the template, the skill and the warden state the line in place; the cases and fixtures; `chain_check.py` unchanged; one measured side not worse (S12) | the issue's five points; the diff (no change to `chain_check.py`; no other item's record touched); every `## Removes` row, gone from the tree | the build on two points the overview records as divergences: `replay_targets.py` changed (`overview.md:20`, the owner's answer) and S12's bar not met (`overview.md:21`). Both rest on owner decisions the records quote (`questions.md:41-42`, `phases/phase-3.md:123-134`), and #985's issue body now states both under `## Decisions taken during the build` (owner, 2026-10-19), with Q1 and Q2 beside them; #992's body repeats the second |
| the build | phases 1 to 3 at 1fc88d09, ee05f824, 8d4585b0: the row needs no code, the cases were seen red, the preload is 27,168, the side fails rules 1 and 2 and ships as noise by the owner's decision | every red, count and hash re-run above | none |
| the last round | round 3 at ffed3c38 confirms the encoding fix right and complete and opens nothing; rounds 1 and 2 close and confirm three shoulds | the tree's check, exit 0; round 3's red, re-run | none |
| the changelog | the row, the absence rule, the re-run rule; the warden's measured row and its noise reading; the release panel's `not read`; the replay generator reads by the grammar of a record's time, and `--list` names the same 31 | the evals record and its recompute; the 39 and 28 counts; `--list`'s 31, now with this item's own round 1 beside them | none |
| the pull request body | the same changes; measurement and #992; *How it was verified*: "Review — three rounds, written in the new grammar; round 2 confirms round 1's three closes, and round 3, the last, confirms the encoding fix the first broad run called for and opens nothing" | the tree: `rounds/round-1.md` to `round-3.md`, round 2 confirming round-1#1 to #3, round 3 at ffed3c38 confirming the fix for the run at 12660916 and opening nothing; and every other line: the measurement row, #992's body, the replay red, the preload, the absence rule, the release panel, `chain_check.py` unchanged | none; the line the earlier run withheld on is rewritten |

Verdict: sealed
