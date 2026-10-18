# 1792126889-every-agent-is-written-anew-from-its-job — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | aafffa6c against af9c924b; earlier run: 1e833533 not sound |
| Broad gate | sealed |

The broad gate was run by the orchestrator before this spawn (#957 item 6,
the owner's), not by the sealer, and this run read its record rather than
running it: `broad-gate.md` names cc43f940 against af9c924b, the gate's log
prints `SEALED chore/957-every-agent-is-written-anew-from-its-job @ cc43f940
against origin/release/v0.22.1 @ af9c924b` over the repository's `Broad gate`
row (`uvx ruff check . && uvx ruff format --check . && bin/test -q`), no
commit after 8d7e6a44 touches a file outside this directory, and of the two
commits after cc43f940 one is the gate's own record (1e833533) and the other
(aafffa6c) changes `changelog.md` and `overview.md` in this directory alone.

This is the second run. The first, at 1e833533, read `not sound` on one
sentence of the changelog fragment; aafffa6c repaired it. This run audited
the commits since 1e833533 and re-read the changelog fragment and the pull
request body whole; no claim the first run re-ran stands on a coordinate
aafffa6c touched, so none was re-run again.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| `broad-gate.md`'s SHA is the last commit touching anything outside the item's records | `broad-gate.md:5` | `git diff --stat 8d7e6a44 cc43f940 -- . ':!seal/specs/<item>'`; `git diff --stat cc43f940 1e833533`; `git log 8d7e6a44..1e833533 -- . ':!seal/specs/<item>'` | holds — the first and third empty, the second only `broad-gate.md` |
| The gate ran the repository's `Broad gate` row and sealed | the scratchpad's `broad-gate-957.log`; `seal/config.md:10` | read the log against the config row | holds — the log quotes the row verbatim and prints `SEALED` at cc43f940 |
| The eight committed side files are what `run` wrote from the kept raw output | `phases/phase-1.md`, `phases/phase-3.md` | `noninferiority.py run --from-raw <957-baseline-raw or 957-phase-3-raw>/<side>.raw --out <scratch>`, then `cmp` with `evals/`, warden, smith, framer, sealer | holds — 16 exits 0, all eight byte-identical |
| Phase 2's two warden sides are what `run` wrote | `phases/phase-2.md` | `run --from-raw` over `957-phase-2-raw` and `957-phase-2b-raw`, `cmp` | holds — exit 0, identical |
| The four phase-3 records reproduce | `phases/phase-3.md` §*The evaluation* | `noninferiority.py compare --phase 3` over the re-derived sides, `diff` with `evals/<a>-phase-3.md` | holds — compare 0 and diff 0 for all four |
| The six records read the verdicts they state | `evals/*.md`, `rounds/round-2.md` | `noninferiority.py check` on each | holds — warden-phase-3 0, smith-phase-3 0, framer-phase-3 1 (rule 5), sealer-phase-3 1 (rules 3, 5), warden-phase-2 1 (rule 3), warden-phase-2-run-1 1 (rule 3) |
| Evaluation spend in this item $204.30; baseline $62.04 for 40 runs | the pull request body | `side_numbers` summed over the ten committed side files (a scratch script, deleted) | holds — 204.3044; baseline 3.0366 + 6.3830 + 16.5896 + 36.0352 = 62.0444 over 40 runs |
| The preload figures 27,032 at 93c1878c and 76,019 at af9c924b | `changelog.md:6-7`, the pull request body | `git show 93c1878c:<f> \| shasum -a 256` and `wc -c` against `evals/warden-phase-3.json`'s `preload`; `wc -c` at af9c924b | holds — both hashes equal the record's; 10,495 + 16,537 = 27,032; 18,031 + 20,368 + 16,620 + 21,000 = 76,019 |
| Seen red: the §2 hand-over pin fails on the contract before 8d7e6a44 | `rounds/round-2.md` finding 1's answer | contract from 74c6a75a in a clone, `bin/test tests/test_broad_gate_rule.py::test_the_prohibition_itself_has_one_home_and_it_is_the_contract`; restored, again | holds — exit 1, the case failing; exit 0 at HEAD |
| Seen red: the two unrun-case verdict cases fail on the harness before 857aa1af | `rounds/round-1.md` finding 2's answer | `noninferiority.py` from 45f0d963 in a clone, `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py` | holds — exit 1, exactly those two failing, 62 passing |
| Seen red: the warden's `--root` pin fails on the definition before 0067cff0 | `rounds/round-1.md` finding 8's answer | `agents/warden.md` from 0067cff0^ in a clone, `bin/test … -k branch_worktree` | holds — exit 1, `test_the_warden_checks_its_record_in_the_branch_worktree` failing |
| Seen red: T5 fails on the smith's and the framer's figures | `phases/phase-3.md` | both definitions from af9c924b in a clone, `bin/test tests/test_a_moved_rule_leaves_its_definition.py -k tools_per_turn` | holds — exit 1, `1.08–1.17` (smith) and `1.4`, `2.3–3.1` (framer) named |
| Seen red: T1 fails on the old warden | `phases/phase-2.md` | `agents/warden.md` from af9c924b in a clone, `bin/test tests/test_every_agent_reads_the_contract.py -k shape` | holds — exit 1 on `[agents/warden.md]` |
| Seen red: T4 fails on the old contract | `phases/phase-3.md` | the contract from af9c924b in a clone, `bin/test … -k "cited_section or four_rules"` | holds — exit 1 on T4; T3 passes there, consistent with its record, which shows it red by a planted `contract §21` only |
| Seen red: the preload pin catches a definition without the contract | `rounds/round-1.md` finding 3's answer | `agent-contract` removed from the clone's `agents/smith.md` with `Edit`, `bin/test … -k preloads_the_contract` | holds — exit 1 on `[agents/smith.md]` alone |
| The narrow modules and the rule targets hold at HEAD | `rounds/round-3.md` | `bin/test` over the broad-gate, contract, non-inferiority, reads-the-contract and moved-rule modules; `bin/rules --check`, in a clone at 1e833533 | holds — exit 0, 384 passed, 4 skipped; exit 0, 464 targets in 60 files |
| CI green on three legs | the spawn prompt; the pull request body | `gh run view` 39041691702, 39043767134, 39044553922 | holds — all success; the first is at 314f6166, not 2dfa53a9 as the prompt said, whose tree outside this directory is identical; 7e8e194e's tree outside it equals HEAD's |
| Removes: `skills:` beyond the contract (warden) | `spec.md` §*Removes* row 1 | read `agents/warden.md:7-8` | holds — `agent-contract` alone |
| Removes: the per-segment numbers in the definitions | `spec.md` §*Removes* row 3 | `git grep -E "tools per turn\|1\.89\|1\.08\|1\.17\|Your number is 1\.4" -- agents/` | holds — exit 1, none |
| Removes: the contract's incident paragraphs and its numbering section | `spec.md` §*Removes* row 5; `changelog.md:25-27` | `git grep` for `#30`, `#36`, `28 minutes`, `128 shell`, `milestone-49`, `sat in two`, `284k` and `How the sections are numbered` | holds — exit 1, none; 20 sections, 20 `Enforced by:` lines |
| Removes: the proof block and emoji in `code-review` and the warden | `spec.md` §*Marks and labels*, §*Removes* row 7 | `git grep` for `applied` blocks and the emoji ranges over `skills/code-review/SKILL.md`, `agents/warden.md`, the contract | holds — exit 1, none |
| Removes: the pins on the gate's single assigner and the incident lessons | `phases/phase-3.md` | `git grep test_only_one_definition_assigns_the_broad_gate\|test_the_method_lessons_moved_in -- tests docs skills agents` | holds — exit 1, none |
| The old §16 is in §11, the old §17 is §16, §17–§20 are new, and no other number moved | `changelog.md:28-31`; `docs/the-agent-set.md:26-31` | the contract's `## ` headings at af9c924b against HEAD; `git grep -P "§1[67](?!\d)"` outside `seal/specs` | holds |
| The commits since the first run touch only this item's records | aafffa6c's message; the coordinator's hand-over | `git log 1e833533..aafffa6c`; `git diff --stat 1e833533 aafffa6c`, whole and outside this directory | holds — one commit, `changelog.md` and `overview.md` only; outside this directory empty |
| "The smith and the framer changed through the contract and the loss of their tools-per-turn figures" (the first run found "changed only through the contract" false here) | `changelog.md:22-24` at aafffa6c | `git diff af9c924b aafffa6c -- agents/smith.md agents/framer.md`, read against the sentence | holds — the two definitions' only changes are the smith's item 5 (`1.08–1.17 tools per turn`, 21,097 → 20,829 B) and the framer's `2.3–3.1` figure and its `1.4 tools per turn` paragraph, replaced by a pointer to the per-segment bars (19,857 → 19,545 B) |
| `overview.md` closes its CI row on three runs, the last holding the code the gate ran | `overview.md:38` at aafffa6c | `gh run view` 39041691702, 39043767134, 39044553922 (first run); `git diff --stat 7e8e194e 1e833533` outside this directory | holds — all three `tests` runs succeeded on the ubuntu, macOS and Windows legs at 314f6166, 155920f5 and 7e8e194e; 7e8e194e's tree outside this directory equals cc43f940's and HEAD's |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The issue, with the owner's split comment of 2026-10-17 | #957 keeps the baseline at af9c924b, the verdict against the baseline (tokens across every model per tool call), the warden with `code-review`, and the contract; the other four agents are #967 to #970 | the build, the last round, the pull request body | none |
| The spec | the whole six-phase item, drawn before the split: §2 saying no agent runs the gate, the contract numbered anew from §1, the sealer, smith, framer and scribe in this item | the build on the warden, the contract's four new rules, the baseline and the verdict | the build on §2's wording, the numbering, and phases 4 to 6; each is a divergence row in `overview.md` with its grounds (round 1 finding 1, phase 3's numbering, the owner's split), and the spec's own §*Grounding* says the issue body holds where they differ |
| The build (the diff and the phase records) | the warden and `code-review` written anew; the contract at twenty rules; the verdict judging every rule against one baseline; phase 2 closed on one grader's `fail`, phase 3 closed with the framer's rule-5 `fail` carried and the sealer's record unread | the issue; the re-derived records and the re-run cases above | none found in the tree |
| The last round (round 3, verifying) | round 2's two fixes hold, nothing opens | the tree at HEAD, the re-run pin of round-2#1 | none |
| The changelog fragment | what a plugin user meets: the warden's preload, the contract's twenty rules and two moved numbers, a per-agent table at af9c924b → 93c1878c | every figure re-read above, and since aafffa6c the tree on how the smith's and the framer's definitions changed | none |
| The pull request body | the same two changes, the proof, $204.30 spent, three rounds, `Closes #957` | the issue, the records, the figures re-read above, #971's first comment (one wrong finding on each side) | none found |

Verdict: sound
