# 1792368013-the-scribe-is-written-anew-from-its-job — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | 11b7ffd9 against b196fe9b; earlier run: e128244f withheld |
| Broad gate | d9fac6ed against b196fe9b |

## Claims re-run

<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->

This run audits 11b7ffd9. The one commit since the earlier run's e128244f is
11b7ffd9, and it touches only this file (`git log --no-merges --name-only
d9fac6ed..HEAD`, executed), so no claim's coordinate moved and the rows
executed at e128244f stand for 11b7ffd9's code unchanged. What changed is the
pull request body, outside the tree; its rows were read again against the
records. Every `executed` row of the earlier run ran in a `git clone
--no-local` of the branch at e128244f under the scratchpad, removed after;
the tree under audit was only read. The base is `release/v0.22.2@{upstream}`, b196fe9b. "At base" means
that clone with `agents/scribe.md`, `skills/legacy-parity/SKILL.md` and
`skills/implement/scripts/seal.py` checked out from b196fe9b and every test
at HEAD.

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD, followed only by this item's records | `broad-gate.md:5` | `git log --no-merges --name-only d9fac6ed..HEAD ^b196fe9b`; `git merge-base --is-ancestor d9fac6ed HEAD` | holds, executed, re-run at 11b7ffd9: ancestor (exit 0); d47d39c1 touches `broad-gate.md` alone, e128244f `overview.md` alone and 11b7ffd9 `guarantee.md` alone, all under `seal/specs/1792368013-…/` |
| Every case the build planted or re-pointed is green at HEAD | `phases/phase-1.md:113`, `phases/phase-2.md:122`, `rounds/round-2.md:61` | `bin/test -p no:xdist -q` over `test_every_agent_reads_the_contract.py`, T3, `test_the_record_is_written_in_words.py`, `test_review_axes.py`, the `seal` refusal case, `test_absence_claims.py`, the probe pin, `test_docs_line_wrap.py` | holds, executed: exit 0, 86 passed, 1 skipped (the framer's `NOT_YET_REWRITTEN` entry) |
| T4 was seen red before the rewrite: it read the labels as the four emoji | `phases/phase-1.md:88-89` | the same command, at base | holds, executed: `the labels are ['🔴', '🟡', '🟢', '❓'], not ['differs', 'grounded', 'equivalent', 'unread']` |
| T5 was seen red: it lost *the warden in a review round* | `phases/phase-1.md:89` | the same command, at base | holds, executed: `the record of a comparison lost 'the warden in a review round'` |
| T6 goes red on the emoji once `SKIP` is gone | `phases/phase-1.md:89-91` | the same command, at base | holds, executed: names `skills/legacy-parity/SKILL.md:91` to `:94`. The phase's run had `SKIP` in place and went red on its own assertion; this run is the case as committed |
| T1 and T3 were seen red on the old scribe | `phases/phase-2.md:87-89` | the same command, at base | holds, executed: T1 `skills: lists ['agent-contract', 'legacy-parity'], not agent-contract alone`; T3 `agents/scribe.md has no ## Rules section` |
| The resolution-order case is red without its rule, including the mutation round 2 did not re-run | `rounds/round-1.md:73`, `rounds/round-2.md:27-29` | at base; then at HEAD with *A comparison against a guessed original proves nothing.* deleted alone from `skills/legacy-parity/SKILL.md` (a Python replace asserting one match), `bin/test …::test_the_resolution_order_ends_with_the_caller_asking`, file restored | holds, executed: at base the section heading is missing; under the mutation exit 1, `the resolution order lost 'A comparison against a guessed original proves nothing.'` |
| The `seal` refusal case was seen red against the old line | `overview.md:41-43`, d3a59161's message | the same command, at base | holds, executed: the output carried *The first time the smith works in a repository …* and the case failed |
| The scribe joins `COVERED` and is wrapped | `spec.md` S9 | the same command, at base and at HEAD | holds, executed: at base `agents/scribe.md:22 is 158 columns (limit 88)`; green at HEAD |
| The read set's agent share is 25,617 B against 25,691; preload 40,466 → 34,697, read set 40,466 → 40,392 | `changelog.md:29-39`, PR body `:17-23` | `bin/payload-meter --root <clone> --agent scribe`; `wc -c skills/legacy-parity/SKILL.md`; `git show <c>:<file> \| wc -c` at 43cbc361 and b196fe9b | holds, executed: scribe 3,319, contract 16,603, `CLAUDE.md` pair 14,775, total 34,697; skill 5,695; 3,319 + 16,603 + 5,695 = 25,617; 34,697 + 5,695 = 40,392. Both baselines read 3,763 + 5,325 + 16,603 = 25,691, and with the pair 40,466 |
| `## Removes`: the scribe's `legacy-parity` preload, contract paragraph, *Called by smith*, parenthesis and §6 paragraph | `spec.md:208-211` | read `agents/scribe.md`; `git grep -n 'Called by smith' -- agents/scribe.md` | holds: `skills:` is `agent-contract` alone (T1 green, executed); the grep printed nothing (executed); the paragraphs are gone (read) |
| `## Removes`: the emoji labels, the field table, the reader's *ask the user and record the answer*, the narration under the three-way table | `spec.md:212-215` | `git grep` of `\| Policy root`, `ask the user and record the answer`, `Inflating the open-questions` over `skills/legacy-parity` | holds, executed: each exit 1; the labels are the four words (T4 green) |
| `## Removes`: `docs/policies/` as a shipped or proposed value (S7) | `spec.md:216`, `:145` | `git grep -n 'docs/policies' -- ':!seal/specs' ':!changelog' ':!tests' ':!.test_durations'` | holds, executed: one hit, `skills/implement/orchestration.md:52`, the sentence saying not to create it |
| `## Removes`: both skip entries, the line-wrap docstring lines, the follow-up row | `spec.md:217-220` | `git grep` of `NOT_YET_REWRITTEN`, `^SKIP`, `#968 to #970`, `scribe.md   160` over `tests/`; the diff of `seal/follow-up.md` | holds: `NOT_YET_REWRITTEN` holds `agents/framer.md` alone, the other greps exit 1 (executed); the follow-up row is deleted (read) |
| `## Removes`: the README cells and *the smith asks* (S10) | `spec.md:221-222`, `:148` | S10's `git grep`; a wider `git grep -i -E 'smith (builds\|creates\|asks)\|smith 가 …'` over the READMEs, `skills`, `hooks`, `bin`, `templates`, `docs` | holds, executed: both exit 1; the scribe's rows list `agent-contract` alone and the counts read three and thirteen (read) |
| No hook, script or test reads the old parity labels | PR body `:31`, changelog `:18` | `git grep -P '(🔴\|🟡\|🟢\|❓) *(differs\|equivalent\|out of)'` over the tree outside records; `git grep -E 'differs from original\|out of verified scope'` over `hooks bin skills .github tests evals/scripts templates` | holds, executed: both exit 1 |
| None of the scribe's pins pinned narration, so none was removed; the rule pins were re-pointed (the body as rewritten) | PR body `:30` | read `phases/phase-2.md:71-83`, `phases/phase-1.md:77-84`, `questions.md:48` | holds, read: phase 2 says *No pin on the scribe pinned narration, so no case was removed* and its table re-points the absence and probe pins; Q3's answer says *none was removed*. The earlier run's *narration pins removed* is gone |
| The READMEs said in eight places that the smith asks where `seal/` lives and whether the project ports an original, and creates the layout (the body as rewritten) | PR body `:11` | read the diff of `README.md` and `README.ko.md` against b196fe9b, `changelog.md:11-13` | holds, read: the eight changed sentences are, in each README, the parity question, the `seal/` creation, the creation from `templates/` and the *Shared or local* question; the wording is the changelog's |
| The new cases and the shape case were each seen failing against the tree before the change; the records name a `mutation-check` run for each unit of phases 1 and 2 and for the resolution order; the `seal` refusal case claims only its red (the body as rewritten) | PR body `:29` | the at-base run above (executed at e128244f, the code unchanged at 11b7ffd9); read `phases/phase-1.md:95-102`, `phases/phase-2.md:95-105`, `rounds/round-1.md:73` | holds: every named case was red at base (executed). Phase 1's table covers T4, T5, T6 and phase 2's T1, T2, T3 and the two pins (read). The resolution order's `mutation-check` runs are named in the fix pass's answer at `rounds/round-1.md:73` rather than in a `phases/` file; the fact the line states holds (read) |
| #988 is filed in 0.22.3 | PR body `:36`, `questions.md:46` | `gh issue view 988 --json title,state,milestone` | holds, executed: open, milestone `release: 0.22.3`, the title the row describes |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | The scribe preloads the contract alone and opens `legacy-parity` at step 1; the skill to the shape with four verdict words, its writer named, its field table pointed at the template; B5's five sites; skips and the follow-up row removed; measured on the read set at or below 25,691 B, outcome `unverified` with the owner named | the issue body's three bullets and its byte measure; the tree for every `## Removes` row; the build | none. Its line coordinates moved after #976 and #943 merged and its README class was four sentences where the tree has eight; `overview.md:22-23` records both, and the tree bears out the overview |
| the build | Phases 1–3 at c6738f51, c8391342, ef570495; d3a59161 (the `seal` line) and 22187f49 (round 1's fixes) after them | the spec, the tree, every red and byte figure re-run above | none |
| the last round | Round 2 at 98c5729d confirms round 1's three closes and opens nothing | the tree at HEAD: the three fixed sentences stand (read) and the resolution-order case is red under both mutations (executed) | none |
| the changelog | Five `### Changed` items; preload 40,466 → 34,697, read set 40,466 → 40,392, agent share 25,691 → 25,617; outcome `unverified`, the owner at the first parity run | the tree and the meter at HEAD; the issue body's measure | none. Its README item says the smith asked *where `seal/` lives and whether the project ports an original*, which matches the eight README sentences |
| the pull request body | What changes, the byte table, the verification table, #988 left for later; `:11`, `:29` and `:30` rewritten after the earlier run | the changelog, the tree, the meter, the phase records, `questions.md` Q3 and both rounds, line by line | none. Each of the earlier run's three lines now says what the records say. One looseness stays and changes no fact: `:29` credits *the phase records* with the resolution order's `mutation-check`, which `rounds/round-1.md:73`'s fix-pass answer records |

<!-- One line: `sealed`, `withheld — <the claim, its party, its coordinate>`
or `undecided — <the question, for the owner>`. An owner's answer is a line
under it, `Answered <date> by <who>: <answer>`, which the next run keeps. -->

Verdict: sealed
