# 1792368013-the-scribe-is-written-anew-from-its-job — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | e128244f against b196fe9b |
| Broad gate | d9fac6ed against b196fe9b |

## Claims re-run

<!-- One row per act of `agents/sealer.md` step 3, whatever the act, and one
per thing the act checks. `Result` reads `holds`, or `does not hold — <what
came back>`, and a `does not hold` is what the verdict names. -->

Every `executed` row ran in a `git clone --no-local` of the branch at
e128244f under the scratchpad, removed after; the tree under audit was only
read. The base is `release/v0.22.2@{upstream}`, b196fe9b. "At base" means
that clone with `agents/scribe.md`, `skills/legacy-parity/SKILL.md` and
`skills/implement/scripts/seal.py` checked out from b196fe9b and every test
at HEAD.

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run is at HEAD, followed only by this item's records | `broad-gate.md:5` | `git log --no-merges --name-only d9fac6ed..HEAD ^b196fe9b`; `git merge-base --is-ancestor d9fac6ed HEAD` | holds, executed: ancestor (exit 0); d47d39c1 touches `broad-gate.md` alone and e128244f `overview.md` alone, both under `seal/specs/1792368013-…/` |
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
| Narration pins on the scribe were removed | PR body `:30` | read `phases/phase-2.md:71-72`, `phases/phase-1.md:77-84`, `questions.md:48` | does not hold — read: phase 2 says *No pin on the scribe pinned narration, so no case was removed*, phase 1's table removes no pin, and Q3's answer says *none was removed* |
| The new cases were each seen red, *then by `mutation-check`* | PR body `:29` | read the phase records, both rounds, `overview.md` and d3a59161's message | holds for T3, T4, T5 and the resolution-order case (phase 1 and 2 tables, round 1's answer, read); the `seal` refusal case has a recorded red against the old line and no recorded `mutation-check` run (unverified; the orchestrator, who made d3a59161, answers it). T1, named as *the scribe's shape*, is an existing case whose skip left, not a new one (read) |
| #988 is filed in 0.22.3 | PR body `:36`, `questions.md:46` | `gh issue view 988 --json title,state,milestone` | holds, executed: open, milestone `release: 0.22.3`, the title the row describes |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | The scribe preloads the contract alone and opens `legacy-parity` at step 1; the skill to the shape with four verdict words, its writer named, its field table pointed at the template; B5's five sites; skips and the follow-up row removed; measured on the read set at or below 25,691 B, outcome `unverified` with the owner named | the issue body's three bullets and its byte measure; the tree for every `## Removes` row; the build | none. Its line coordinates moved after #976 and #943 merged and its README class was four sentences where the tree has eight; `overview.md:22-23` records both, and the tree bears out the overview |
| the build | Phases 1–3 at c6738f51, c8391342, ef570495; d3a59161 (the `seal` line) and 22187f49 (round 1's fixes) after them | the spec, the tree, every red and byte figure re-run above | none |
| the last round | Round 2 at 98c5729d confirms round 1's three closes and opens nothing | the tree at HEAD: the three fixed sentences stand (read) and the resolution-order case is red under both mutations (executed) | none |
| the changelog | Five `### Changed` items; preload 40,466 → 34,697, read set 40,466 → 40,392, agent share 25,691 → 25,617; outcome `unverified`, the owner at the first parity run | the tree and the meter at HEAD; the issue body's measure | none. Its README item says the smith asked *where `seal/` lives and whether the project ports an original*, which matches the eight README sentences |
| the pull request body | What changes, the byte table, the verification table, #988 left for later | the changelog, the tree and the meter on every figure and every line of *What changes* but `:11` | `:30` says *narration pins removed*; `phases/phase-2.md:71-72` and `questions.md:48` say none was. `:11` says the READMEs said *in eight places* that the smith asks where `seal/` lives and creates the layout; two of the eight (`README.md:240`, `README.ko.md:231` at HEAD) were the parity question, which the changelog's item names and the body drops. `:29` claims `mutation-check` for the `seal` refusal case, which no record shows |

<!-- One line: `sealed`, `withheld — <the claim, its party, its coordinate>`
or `undecided — <the question, for the owner>`. An owner's answer is a line
under it, `Answered <date> by <who>: <answer>`, which the next run keeps. -->

Verdict: withheld — the pull request body is untrue at three lines: `:30` claims narration pins were removed, where `phases/phase-2.md:71-72` and `questions.md:48` say no pin pinned narration and none was removed; `:11` says the READMEs said in eight places that the smith asks where `seal/` lives, where two of the eight (`README.md:240`, `README.ko.md:231`) asked the parity question, as `changelog.md:11-13` says; `:29` claims `mutation-check` for the `seal` refusal case, which no record shows. The tree, the gate's record, the spec, the build, round 2 and the changelog hold.
