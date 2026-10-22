# Guarantee: 1792627930-the-section-sign-is-still-syntax

| Field | Value |
|---|---|
| Target SHA | 0f6ae7c4 against 0d62145a; earlier run: bc8e8c7a withheld |
| Broad gate | 5992b4d3 against 0d62145a |

## Claims re-run

The base resolves to 0d62145a through `release/v0.22.3@{upstream}` (executed).
`git log --no-merges --name-only 5992b4d3..HEAD ^0d62145a` lists three
commits, and each touches one file of this work item: bc8e8c7a touches
`broad-gate.md`, 42a80503 touches `guarantee.md`, and 0f6ae7c4 touches
`changelog.md` (executed). This run audits what changed since the earlier
run at bc8e8c7a. That is `changelog.md:16` and the pull request body, which
was read again whole. The rows the earlier run executed against code, tests
and CI stand as executed then, because no commit since bc8e8c7a touches a
path outside this work item's directory (executed, `git diff --stat
bc8e8c7a 0f6ae7c4`). A "seen red" claim was re-run in a clone at 0d62145a,
with the case's module copied in from HEAD. A mutation was made in a second
clone at HEAD. Both clones were removed afterwards, and the tree under audit
was not changed. `pr-body.md` is the pull request body file the orchestrator
handed over.

| Claim | Source | Command | Result |
|---|---|---|---|
| The four pins of the printed `Contract rule 6` label were seen red against the old script | `phases/phase-1.md:77-78` | `pytest` on the four cases of `tests/test_session_cost.py` that pin `Contract rule 6`, in the clone at 0d62145a, and then at HEAD | holds: 4 failed at the base and 4 passed at bc8e8c7a (executed in the earlier run) |
| The section-sign case was seen red before the rewrite | `phases/phase-3.md:18-21` | `pytest tests/test_no_living_file_writes_the_section_sign.py` in the clone at 0d62145a, and then at HEAD | holds: it fails at the base, listing `<path>:<line>` for each living line with the sign, and passes at bc8e8c7a (executed in the earlier run) |
| The no-comment case was seen red listing 24 template lines | `phases/phase-4.md:19-23` | `pytest tests/test_a_record_carries_no_comment.py` in the clone at 0d62145a, and then at HEAD | holds: it fails at the base naming 24 distinct `templates/sdd-*.md` lines, and passes at bc8e8c7a (executed in the earlier run) |
| The case that holds the fence rule and line split to `hooks/blocks.py` was seen red against the copies | `phases/phase-5.md:22-24` | `pytest tests/test_unverified_rows_close.py::test_the_fence_rule_and_the_line_split_are_the_hooks` in the clone at 0d62145a, and then at HEAD | holds: it fails at the base on the `fence_opener` source-file assertion, and passes at bc8e8c7a (executed in the earlier run) |
| The five preloads, base against head | `rounds/round-3.md:39-41` and `:97`, `changelog.md:16`, `pr-body.md:16` and `:46` | `noninferiority.preload_bytes` for framer, smith, warden, sealer and scribe, in the clone at 0d62145a in the earlier run, and at 0f6ae7c4 in this run | holds: framer 25255 to 25239 (16 bytes), smith 24746 to 24668 (78), warden 25370 to 25300 (70), sealer 23383 to 23302 (81), scribe 18545 to 18486 (59). The changelog and the pull request body now give 16 for the framer and 16 to 81 overall (executed) |
| S8: `## Rule changes` yields four `change` and two `add` | `spec.md:210`, `rounds/round-3.md:30-33`, `pr-body.md:18` | `rule_changes.parse` on `spec.md` | holds: change, change, change, change, add, add (executed in the earlier run). `apply_op` was not re-run (read from round 3) |
| S3: no living file writes the section sign; 743 lines in 143 files at the base | `spec.md:205`, `pr-body.md:47` | `git grep -n -I -P '\x{00A7}'`, excluding `seal/specs/`, `changelog/`, `CHANGELOG.md` and `evals/behaviour/`, at 0d62145a and at HEAD | holds: 743 lines in 143 files at the base and none at bc8e8c7a. Without `-I`, only the two binary PNGs under `assets/seals/candidates/` match (executed in the earlier run) |
| S9: the records of a moment are untouched | `spec.md:211` | `git diff --name-only 0d62145a...HEAD -- seal/specs changelog CHANGELOG.md evals/behaviour` | holds: only this work item's directory (executed in the earlier run; the commits since touch only that directory) |
| A near-miss contract citation is refused at its line | `pr-body.md:9` | `pytest tests/test_the_agent_contract_holds_the_universal_rules.py -k near` | holds: 5 passed (executed in the earlier run). Its red is round 1's mutation run (read, `rounds/round-1.md:199`) |
| CI run 39711220166 at ce84116a failed on the census | `rounds/round-1.md:18-21`, `pr-body.md:38` | `gh run view 39711220166 --log-failed` | holds: two cases of `tests/test_a_shrunken_corpus_declines_to_judge.py`, `test_no_scope_in_the_suite_lists_paths_from_git_without_a_guard` and `test_an_unguarded_scope_is_named_although_a_module_is_mid_edit`, failed on each of the ubuntu leg, macOS shard 1 and Windows shard 1. The body now says so (executed in the earlier run; the body read in this run) |
| CI passed at ea3141ed and at 14e4b411 | `pr-body.md:39` | `gh run view 39713225557` and `gh run view 39714074783` | holds: both `success` (executed in the earlier run) |
| The broad run at 5992b4d3 | `broad-gate.md`, `pr-body.md:40` | read the run's log in the orchestrator's scratchpad | holds (read): `BROAD GATE PASSED` at 5992b4d3 against 0d62145a, 7481 passed and 13 skipped, chain exit 0 |
| Removes: the five copies of the contract heading pattern | `spec.md:318` | `git grep -n HEADING -- tests` | holds: each of the five modules imports `HEADING` from `tests/test_the_agent_contract_holds_the_universal_rules.py` (executed in the earlier run) |
| Removes: `OTHER_FILE`, the list arm, `CITED_NUMBER` | `spec.md:319-320` | `git grep -n -E '\bOTHER_FILE\b\|\bCITED_NUMBER\b\|^NUMBER\s*=' -- tests` | holds: no match (executed in the earlier run) |
| Removes: the second copy of the fence rule and of the line split | `spec.md:327`, `pr-body.md:47` | `git grep` for the four definitions in `skills/verify/scripts/unverified_check.py` and `hooks/blocks.py` | holds: the definitions stand only in `hooks/blocks.py`, and `unverified_check.py:112-121` takes them from it (executed in the earlier run) |
| Removes: the two cases that held the copies in step | `spec.md:328`, `pr-body.md:47` | `git grep` for both case names under `tests/` | holds: neither name stands. The agreement half stands as `test_the_fence_walks_agree_shape_by_shape`, as round 1 finding 2 asked and `pr-body.md:36` says (executed in the earlier run) |
| Removes: the three docs sentences | `spec.md:322-324` | `git grep` for each sentence under `docs/` | holds as framed: they stand at `docs/the-agent-set.md:19`, `docs/one-root-by-lifetime.md:25`, `docs/the-review-and-parity-arms.md:79` and `docs/the-review-record.md:286`, and no `docs/` file is in the diff. They change through `## Rule changes` at the owner's settle, as `pr-body.md:18` says (executed in the earlier run) |
| Owner's sample: the fact of the deleted `test_the_template_says_why_a_tick_is_refused` is held | `rounds/round-1.md:315-316` | in the clone at bc8e8c7a, `skills/implement/SKILL.md` mutated twice, each time followed by `pytest tests/test_the_set_a_work_item_always_has.py`: "asserts a **past** state" became "asserts a state", then "a tick and the word `done` are refused" became "a tick is discouraged" | holds: each mutation turned `test_the_skill_says_why_a_tick_is_refused` red, exit 1, and the module passes unmutated (executed in the earlier run) |
| Owner's sample: the fact of the deleted `test_the_template_ships_the_vocabulary_the_parser_accepts` is held | `rounds/round-1.md:321-323` | in the clone at bc8e8c7a, `templates/sdd-routing.md` mutated three times, each time followed by `pytest tests/test_waiver_decided_at_start.py`: the `Review` answer, the `Destination` answer, and the `Implementation` placeholder's second word | holds: 3, 3 and 1 of the template PARSES cases turned red, exit 1 each, and the module passes unmutated. `test_the_orchestration_offers_the_vocabulary_the_parser_accepts` holds the orchestration's words against the parser (executed in the earlier run) |
| Phase 4's guidance table rows | `rounds/round-3.md:87`, `pr-body.md:37` | count the table rows at `phases/phase-4.md:35-81` | holds for the body: 47 rows, which `pr-body.md:37` now gives. 32 are "stated", 1 is "stated in other words", 11 are "moved", 1 is half stated and half moved, and 2 are "placeholder". Round 3's "about 30 of 46" is one row short (executed in the earlier run) |
| The left-open item, the follow-up issues, and Q2's issue | `pr-body.md:17`, `:25`, `:51` | `gh issue view 956`, `gh issue view 1012`, `gh issue view 913` | holds (read): #956's body has a paragraph on this citation reader. #1012 (0.22.4) strips the old records after the settle. #913 (0.22.5) takes the coordinate grammar and the pact anchors |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | No living file writes the section sign. A contract rule is cited as `contract rule <N>`, or `rule <N>` inside the contract and `agents/`. Another file's section is cited by path and italic heading. The record templates carry no comment. There is one fence rule. `docs/` changes through four `change` and two `add` items | the issue body, with Q1, Q2, Q3 and Q6 answered by the owner on 2026-10-22 (`questions.md:40-45`, read); the tree (S3, S8, S9 and the Removes rows above, executed); the build; the last round | none. The removal of the contract preamble's list of agent names is not in scope item 1. `overview.md:13` records it, and round 1 confirmed nothing read the list |
| the build | Phases 1 to 5 at 0ca1bee3, 0c8e94cf, 9b2ec5e4, 152bcb40 and 281f8960. Fix passes at dae18434 and 7eb63541, and the framer's frame commit at 14e4b411 | the spec; the tree on every "seen red" re-run above and on every removal (executed) | none at its own commits. Phase 5's framer figure of 61 bytes was true at 281f8960, and 7eb63541 raised the framer preload by 45 bytes |
| the last round | Round 3 at 14e4b411 confirms round 2's finding closed, opens nothing, and reads framer 25239 against 25255 | the tree (preload row, executed); the spec's S8 | none of substance. Its "about 30 of 46" counts phase 4's table one row short, which has 47 |
| the changelog | Three entries: the citation spelling with the section-sign case, the comment-free templates, and the single fence rule. The framer's preload fell 16 bytes | the spec; the tree, including the five preload figures (executed at 0f6ae7c4); the pull request body | none |
| the pull request body | What changes, the owner's answers, the divergence, the verification, the removals and the left-open item, read again whole in this run | the spec, the build and round 3 on what changed. The tree on the five preload figures, 743 lines in 143 files, the near-miss refusal, both census cases of the first CI run, the later CI runs, the broad run, the 47 rows of phase 4's table, #956, #1012 and #913. Its `:47` now names both second copies and the cases that held them in step, as `spec.md` `## Removes` does | none |

Verdict: sealed
