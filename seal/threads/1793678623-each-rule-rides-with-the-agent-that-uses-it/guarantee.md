# Guarantee: 1793678623-each-rule-rides-with-the-agent-that-uses-it

| Field | Value |
|---|---|
| Broad gate | 93f2ef9b1 against 0c68b9933 |

The audit read the tree at b735d76dd. The base is `release/v0.30.1`, and its
upstream, `origin/release/v0.30.1` and the local branch all resolve to
0c68b9933, which is the `v0.30.0` tag (`git rev-parse --verify --quiet`,
executed). `trail/gate.md`'s last `seal` block names `93f2ef9b1 against
0c68b9933`, and 93f2ef9b1 is an ancestor of HEAD (`git merge-base
--is-ancestor`, executed, exit 0). `git log --no-merges --name-only
93f2ef9b1..HEAD ^0c68b9933` lists b735d76dd alone, which touches only
`trail/gate.md` (executed). The repository tracks no `seal/parity.md` (`git
ls-files`, executed, no output), so this block owes no `original:` line.
`seal pr-body seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it
--body <scratchpad>/1793678623-each-rule-rides-with-the-agent-that-uses-it/pr-body.md
--check` exited 0 (executed). Every re-run below took place in a `git clone
--no-local` at b735d76dd under
`<scratchpad>/1793678623-each-rule-rides-with-the-agent-that-uses-it/at-base/`,
with a second clone at 0c68b9933 beside it for the base side. Both clones
and their logs have been removed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| seen red: run against the base contract, the new numbering cases fail only at `test_a_listed_number_that_has_a_heading_is_named`, with `AttributeError`, and the others pass | `trail/phases/phase-1.md:53-56` | `git checkout 0c68b9933 -- skills/agent-contract/SKILL.md`; `bin/test tests/text/test_the_agent_contract_holds_the_universal_rules.py -q -p no:xdist -k "numbered or gap or repeated or listed"` | holds (executed): exit 1, 1 failed and 4 passed, `AttributeError` at `:198` |
| seen red: with the old case's comparison put back into `numbering_faults`, the numbering case, the gap case and the listed case all fail | `trail/phases/phase-1.md:58-66` | the old case's line `return [] if numbers == list(range(1, len(numbers) + 1)) else [numbers]` inserted after `numbers = …` (the inserted text was asserted to match once); `bin/test <module> -q -p no:xdist -k "numbered or test_a_gap or test_a_listed"` | holds (executed): exit 1, 3 failed |
| seen red: with the repeat check replaced by `if False:`, `test_a_repeated_number_is_named` fails | `trail/phases/phase-1.md:67-70` | that one substitution, asserted to match once; `bin/test <module> -q -p no:xdist -k repeated` | holds (executed): exit 1, 1 failed |
| seen red: round 1's new case `test_the_contract_points_every_agents_commit_at_the_rule` fails against the contract as it stood before 3a4d969b7 | `trail/rounds/round-1.md:86` (the close's answer) | `git checkout e045e7264 -- skills/agent-contract/SKILL.md`; `bin/test tests/behaviour/test_a_commit_names_its_repository.py -q -p no:xdist` | holds (executed): exit 1, 1 failed and 4 passed, the failure being the named case |
| executed: at 3354cef75 with only the contract of d68e9b1d6, the cited-section case names four dangling `rule 16` citations | `trail/phases/phase-2.md:97-105` | `git checkout 3354cef75`, then `git checkout d68e9b1d6 -- skills/agent-contract/SKILL.md`; `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -k test_every_cited_section_exists` | holds (executed): exit 1, naming `skills/implement/multi-repository.md:20`, `skills/implement/orchestration.md:364` and `tests/behaviour/test_a_commit_names_its_repository.py:3` and `:70` |
| executed: the changed and dependent modules pass at HEAD | `trail/rounds/round-1.md` *Probes*, `trail/rounds/round-3.md` *Probes* | `bin/test` over the contract-shape, cited-section, commit, probe, reference-root, broad-gate (`tests/skills/test_broad_gate.py`), moved-rule, one-owner, every-agent, broad-gate-rule, line-wrap and writing-style-section modules, `-q` | holds (executed): exit 0, 693 passed and 1 skipped |
| executed: each agent's preload falls from v0.30.0 to 31,730, 34,836, 30,840, 30,556 and 23,970 bytes, and implement grows by 721 bytes and verify by 111 | `changelog.md:6` | `uv run python .github/scripts/release_report.py --against v0.30.0 --at <clone at 0c68b9933> --root <clone at HEAD>`; also `git show <commit>:<path> \| wc -c` summed per agent at 0c68b9933 and HEAD | holds (executed): exit 0, and the rows read 33,081 to 31,730, 36,362 to 34,836, 32,293 to 30,840, 31,879 to 30,556 and 25,085 to 23,970; implement 25,406 to 26,127 and verify 15,097 to 15,208 |
| executed: the census falls from 934 of 11,209 to 766 of 10,769 words shared | `changelog.md:6` | one probe, `python3 -I test_tmp_census.py <base clone> <HEAD clone>`, written to `frame/design.md` D6's method and deleted after its one run | holds (executed): exit 0, with every per-file cell of the base equal to `frame/design.md` *Grounding*'s row, and 766 of 10,769 at HEAD, the contract at 70 of 1,975 |
| executed: no tracked file outside the records cites retired rule 8, 16 or 20 as a live rule | `trail/phases/phase-1.md:102-131`, `trail/rounds/round-1.md` S4 confirmation | one probe, a regex with whitespace folded over `git ls-files` outside `seal/`, `CHANGELOG.md` and `.test_durations`, matching `rule` or `rules`, an optional list, then 8, 16 or 20, and `§` with 8, 16 or 20 | holds (executed): five hits, all in `tests/behaviour/test_a_probe_that_commits_says_so.py`, each naming rule 8 as retired |
| `## Removes`, every row: nothing of each removal stands in the tree | `frame/design.md` *Removes*, `trail/phases/phase-4.md:132-147` | each `git grep` of the phase 4 table at HEAD, plus `git grep -n -E "^## [0-9]+ " -- skills/agent-contract/SKILL.md` | holds (executed): every search exits 1. `two directories above` outside `seal/` lists only `skills/agent-contract/SKILL.md:135`, contract rule 11. The headings run 1 to 7, 9 to 15 and 17 to 19. The removed case's name stands only as the `.test_durations:130` price entry, which `gaps.md` *Not done* names with its grounds |
| the removals the changelog names: the moved commit rule, the phase-boundary set, rules 8 and 20, the five plugin-path copies, the reference-root, parity, reframe and preamble copies, and rule 19's restatement | `changelog.md:3-5` | `git diff 0c68b9933...HEAD -- ':!seal/' ':!tests/'`, read against each clause | holds (read): each clause matches a hunk, and the sealer's step 5 keeps its comparing condition as the changelog says |
| the history search over the core, the contract and `agents/` finds no history sentence at HEAD | `frame/design.md` *Grounding*, the history row; `frame/design.md` D4 | `git grep -n -E '#[0-9]{2,}\|20[0-9]{2}-[0-9]{2}\|[0-9]+\.[0-9]+\.[0-9]+\|twice\|used to\|before #\|until #\|history' -- agents/ skills/core/SKILL.md skills/agent-contract/SKILL.md` | holds (executed): four hits, two test-module names in `check:` lines and two present-tense core sentences, none of them history |
| the commits no crafter made touch only the work item's records | pull request body, line 21 | `git show --name-only` of every `routing:`, `frame:` and `seal:` commit in `0c68b9933..HEAD`, and of 3354cef75 and 20e140537, filtered for paths outside the work item's directory | holds (executed): none lists a path outside it. Which party made each commit is read from the subjects, not established |
| the broad run printed 6360 passed, 12 skipped, chain exit 0 | pull request body, line 20 | read `<scratchpad>/1793678623-each-rule-rides-with-the-agent-that-uses-it/gate.log` | holds (read): lines 6, 12 and 13 print those. The run is the orchestrator's, and no agent re-runs it (contract rule 2) |
| round 3's finding, closed `fixed e896e0e33` in the records alone, holds at HEAD | `trail/rounds/round-3.md:41-108` | read `frame/questions.md` Q1 and `gaps.md` rows 7, 10, 11, 14 and 15 at HEAD; `git show --name-only e896e0e33` | holds (read): e896e0e33 touches `gaps.md` alone. Q1's question names every act the five rows hand it. After 93f2ef9b1 its options cell measures each act too, the retired-number reads included. Row 7 now asks about an agent reading rule 8, 16 or 20 |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | the contract loses rule 16 to implement *2.*, the phase-boundary set to verify's row, and rules 8 and 20 to a preamble list of 8, 16 and 20. The plugin-path sentence goes into rule 11 once, the D3 copies and the D4 history go, and no `docs/` file changes (`frame/design.md` *Scope*, D1 to D7, *Removes*) | the issue's four candidates and its *Done when*: each is read and decided. The tree matches each *Removes* row. S9: `git diff --stat` touches no `docs/` file, and in `skills/*/orchestration.md` only the re-pointed citation | none. Its departures (D2's range, D3's heading, D6's flags, rule 2 with no pointer) are recorded with grounds in the phase records and folded at cab91086e, and round 3 read them |
| the build | phases 1 to 4 built D1 to D4 and D6, and each phase record names its commits, its seen-red cases and its boundary set (`trail/phases/phase-1.md` to `phase-4.md`) | the diff, and the six claims re-run above | none |
| the last round | round 3 confirms round 2's closes of findings 1 and 2. Its one finding reopens round 2's finding 3 on the enumeration of the `gaps.md` rows citing Q1, closed `fixed e896e0e33` (`trail/rounds/round-3.md:44`, `:121`, `:139`) | the records at HEAD: Q1 and the five `gaps.md` rows ask the same acts | none |
| the changelog | the rule-16 and phase-boundary moves, the retired list, the copies removed, the preload figures and the census figures (`changelog.md:3-6`), with three *Process changes* rows | the diff, `release_report.py`'s rows and the census re-run, each executed | none |
| the orchestrator's part of the pull request body | closes #1313 and gives the preload table from `changelog.md`. It names the `refactor:` prefix and the version move, the owner's decisions, the frame exchange at 1d099e006, the paid-run judgment, the rounds, the broad run and the non-crafter commits (pull request body, lines 1-23) | the changelog's preload figures; `routing.md`; the milestone description (`gh api …/milestones`, executed: "A patch: it builds no feat"); `frame/design.md` D3's "(the orchestrator's reading, agreed)" and 1d099e006's diff; `frame/plan.md` *Judgments of the run*; `gate.log`; the commit listing above | the last round. Line 19 says "Round 3 confirmed those and opened one, `reopens: round-2#3`", where "those" are round 2's three findings. `trail/rounds/round-3.md` confirms only round 2's findings 1 and 2 (`confirms: round-2#1` at `:121`, `confirms: round-2#2` at `:139`). Of finding 3 it says "Why the close does not hold" (`:47`) and reopens it (`:44`). The tree contradicts the body |

```seal
target: b735d76dd against 0c68b9933
Verdict: withheld reason: the orchestrator's part of the pull request body, line 19, says round 3 "confirmed those", round 2's three findings, where trail/rounds/round-3.md confirms only round-2#1 (:121) and round-2#2 (:139) and reopens round-2#3 because its close does not hold (:44, :47); every other claim sampled and every other party holds at b735d76dd
```

## Re-audit at 880aa5da7

The only commit since the block above names b735d76dd is 880aa5da7, and
it adds `guarantee.md` alone (`git log --no-merges --name-only
b735d76dd..HEAD`, `git diff --stat b735d76dd 880aa5da7`, executed). No
claim above has a coordinate that commit touched, so none is re-run. The
base still resolves to 0c68b9933 (executed). `trail/gate.md`'s last block
still names `93f2ef9b1 against 0c68b9933`. Nothing outside this work item's
directory follows 93f2ef9b1 (`git log --no-merges --name-only
93f2ef9b1..HEAD ^0c68b9933`, executed). `seal pr-body … --check` on the
repaired body file exited 0 (executed). The parties were read again, and the
orchestrator's part of the pull request body was read whole.

| Claim | Source | Command | Result |
|---|---|---|---|
| round 1's finding is the quoted heading, round 2 confirmed round-1#1 and opened three findings each `regression: round-1#1`, and round 3 confirms round-2#1 and round-2#2 and reopens round-2#3, closed `fixed e896e0e33` | pull request body, *Rounds* item | `grep -n` for the heading in `trail/rounds/round-1.md`, `confirms: round-1#1` and `regression: round-1#1` in `round-2.md`, and `confirms:`, `reopens:` and `verdict:` in `round-3.md` | holds (executed): `round-1.md:21` is the heading word for word. `round-2.md:178` confirms round-1#1, and the round holds three `regression: round-1#1` lines. `round-3.md:44` reopens round-2#3, `:114` is `fixed e896e0e33`, and `:121` and `:139` confirm round-2#1 and round-2#2 |
| the commits no crafter made touch only the work item's records | pull request body, *The commits no crafter made* item | `git show --name-only 880aa5da7` | holds (executed): 880aa5da7 is a `seal:` commit adding `guarantee.md` alone, so the item's rule covers it |

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design, the build, the last round, the changelog | unchanged since b735d76dd. No file of theirs changed | the rows of the first run's table, read again | none |
| the orchestrator's part of the pull request body | as before. The *Rounds* item now gives round 1's finding by its heading, round 2's `confirms: round-1#1`, and round 3's two confirmations and its reopen of round-2#3 | `trail/rounds/round-1.md`, `round-2.md` and `round-3.md`, and every coordinate the first run's row checked | none |

```seal
target: 880aa5da7 against 0c68b9933
Verdict: sealed
```
