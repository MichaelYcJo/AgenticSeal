# Guarantee: 1792619289-the-pull-request-check-parses-rule-changes

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md is written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` *The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | a013383d against 5aed51cb; earlier run: bf127d7c withheld |
| Broad gate | 87c2afce against 5aed51cb |

## Claims re-run

<!-- This run audits what came after bf127d7c. `git diff --stat bf127d7c
a013383d` holds one path, this work item's `guarantee.md`, so no claim's
coordinate changed, and the rows below that name the scratch clone were
executed at bf127d7c on the code a013383d carries unchanged. The pull
request body was re-read whole. -->

| Claim | Source | Command | Result |
|---|---|---|---|
| Nothing but this work item's records follows the broad run, through a013383d | `broad-gate.md:5` | `git log --no-merges --name-only 87c2afce..HEAD ^5aed51cb`; `git merge-base --is-ancestor 87c2afce HEAD` | holds: bf127d7c touches `broad-gate.md` and `overview.md`, a013383d touches `guarantee.md`, all under this work item; 87c2afce is an ancestor of HEAD (executed at a013383d) |
| No code changed since the earlier run | the coordinator's message | `git diff --stat bf127d7c HEAD` | holds: one file, this work item's `guarantee.md` (executed at a013383d) |
| The new cases pass | `phases/phase-1.md:27-31`, `phases/phase-2.md:27-29` | in a scratch clone at bf127d7c, `bin/test tests/test_chain_check.py tests/test_settle_applies_rule_changes_in_place.py -q -p no:xdist -k "TestRuleChangesRead or near_miss or other_letters"` | holds: 33 passed, exit 0 (executed at bf127d7c) |
| Each refusal case (S1, S2, S3, S5, S6, S7, S9, S10) was seen red against the frame commit's `chain_check.py` | `plan.md:120`, `phases/phase-1.md:15-18`, `pr-body.md:27` | same clone, `skills/code-review/scripts/chain_check.py` restored from 5aed51cb (identical to the frame commit 33dc1040's), `bin/test tests/test_chain_check.py -p no:xdist -k TestRuleChangesRead -rA --tb=line` | holds: S1, S2, S3, S5, S6, S7, S9 and S10 fail on assertions; S4's three cases pass; exit 1 (executed at bf127d7c) |
| S12, S13 and S14 failed against 22bfec31, and S15, S16 and S6's second half passed there | `phases/phase-2.md:33-36`, `pr-body.md:27` | same clone, `chain_check.py` restored from 22bfec31, the same command | holds: S12, S13, S14 fail at `assert code == 1` (`tests/test_chain_check.py:2149`, `:2165`, `:2186`), and the edited exit-2 case at `:2248`; S15, S16, S6 and the carried-spec, depth-and-name cases pass; exit 1 (executed at bf127d7c) |
| The twelve near-miss cases were seen red before the fix | `rounds/round-1.md:136` | same clone, `skills/settle/scripts/rule_changes.py` restored from 5aed51cb, `bin/test tests/test_settle_applies_rule_changes_in_place.py -p no:xdist -k "near_miss or other_letters" -rA --tb=line` | holds: all 12 near-miss cases fail; the other-letters boundary passes; exit 1 (executed at bf127d7c) |
| `rule_changes.parse` over the 119 specs under `seal/specs/` refuses none | `phases/phase-2.md:57-58`, `pr-body.md:13`, `pr-body.md:29` | a probe in the clone loading `unverified_check.py#rule_changes` and `#policy_root`, parsing every `seal/specs/*/spec.md` | holds: 119 specs, 0 refused (executed at bf127d7c) |
| This work item's own `## Rule changes` parses | `plan.md:163-166`, `rounds/round-1.md:179` | the same probe on this work item's `spec.md` | holds: one `change` and one `add` op, no error (executed at bf127d7c) |
| `Removes` row 1: the docstring's *The arms are five:* | `spec.md` `## Removes` | `git grep -n "The arms are five" HEAD -- skills` | holds: no match; `chain_check.py:9` reads *The arms are six:* (executed at bf127d7c) |
| `Removes` row 2: the hygiene comment's list opening *It fails for what the author can fix*, with the dashed qualifier | `spec.md` `## Removes` | `git grep -n "and — on a pull request that is not a draft" HEAD -- .github templates`; `git diff 5aed51cb...HEAD -- .github/workflows/hygiene.yml` | holds: no match; the list opens *On a pull request that is not a draft it fails for what the author can fix* and names the spec read (executed at bf127d7c) |
| `Removes` row 3: the template comment's list opening *It never fails a pull request that declared nothing* | `spec.md` `## Removes` | `git grep -n "once the pull request is no longer a draft it fails a" HEAD -- templates` | holds: no match; rewritten as row 2 (executed at bf127d7c) |
| `Removes` row 4: the policy sentence lands at settle, and this pull request leaves `docs/` as it is | `spec.md` `## Removes` | `git diff --stat 5aed51cb HEAD -- docs`; `sed -n 178,182p docs/the-review-record.md` | holds: `docs/` unchanged; the `change` item's `from:` text stands at `docs/the-review-record.md:180-181` (executed at bf127d7c) |
| `tests` runs 39685286823 at be5a9330 and 39689643276 at 06e3232f passed every leg | `pr-body.md:30` | `gh run view <id> --json headSha,conclusion,jobs` | holds: both `success` at those commits, every `pytest`, `lint` and `arm-check-grammar` job `success`, `release-report` skipped (executed at bf127d7c) |
| The broad run: ruff check and format clean, 7426 passed, 13 skipped, chain-check exit 0 | `pr-body.md:31` | read `broad-gate.log` | holds: `Broad gate` is `uvx ruff check . && uvx ruff format --check . && bin/test -q`, `BROAD GATE PASSED ... @ 87c2afce`, `suite ✓ 7426 passed · 13 skipped`, `chain ✓ exit 0` (read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `chain-check` parses `## Rule changes` with the one reader in two sets: each judged work item's `spec.md`, and on a declaring pull request every work item `spec.md` its own commits add or change, less carried and moved; refusals take the check's draft, ready and `--sealing` strictness, with the broad run's limit stated (*Scope* items 1-5, `## Removes`) | the issue body items 1-3; the diff (`chain_check.py#rule_changes_read`, `#rule_changes_of`, `#edited_work_items`, `main`); the cases re-run above | none. The near-miss refusal in `rule_changes.py` is outside *Scope*, and `overview.md`'s second divergence row records it, from round 1's finding 3 |
| the build | phase 1 at 22bfec31 reads the judged set; phase 2 at 2a3ea1a2 adds the edited set and the filter cases; the fix pass adds the near-miss class to the one reader | the spec; the diff; each red and green run above | none |
| the last round | round 3 at d7705fa5: round 2's finding 1 fixed at f31de4a4, opens nothing; `--sealing` strictness stays `## Not judged` for the owner | the diff of f31de4a4 (`chain_check.py:16-22`, `skills/settle/SKILL.md:79-82` carry the qualifier); round 1 and round 2 verdicts | none |
| the changelog | the spec read at the pull request, its draft and broad-run behaviour, what is left alone, exit 2; the near-miss heading refused in the one reader | the spec; the diff; `rounds/round-1.md:102` | none |
| the pull request body | `pr-body.md`, re-read whole at this run: the same change and limits; `How it was verified` now reads, at `:27`, the refusal cases red against the frame commit and S12, S13 and S14 red against the phase 1 commit with S15, S16 and S6's second half passing; at `:28`, one surviving unit in phase 1 and four in phase 2 with the cases that hold them; at `:32`, two round 1 findings to the framer and two fixed | the changelog for *What changes*; `phases/phase-2.md:33-36` and the re-run against 22bfec31 for `:27`; `phases/phase-1.md:45-47` and `phases/phase-2.md:37-46` for `:28`; `rounds/round-1.md:14`, `:72`, `:109`, `:143` and `phases/phase-2.md:20-21` for `:32`; the CI runs, the broad run and the reader over the tree | none. Q1 reads `open` in `questions.md:52`, and the body's *By* cell, *the stated default*, says no person answered it |

Verdict: sealed
