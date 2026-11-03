# Implementation Plan: each rule rides with the agent that uses it (#1313)

## Technical context

The preload is `agents/<agent>.md`, then `skills/core/SKILL.md`, then
`skills/agent-contract/SKILL.md`, injected whole by the harness through each
definition's `skills:` list (`tests/text/test_every_agent_reads_the_contract.py#PRELOADS`,
read). `.github/scripts/release_report.py:106` sums those three files per
agent (read; run at the base, executed: see `frame/design.md` *Grounding*).

Three readers hold the contract's shape, and every phase runs them:

- `tests/text/test_the_agent_contract_holds_the_universal_rules.py`. The
  numbering, one `check:` line per rule, and the facts of rules 1 and 11,
  which are pinned inside their own bodies, so rule 11's new sentence must
  leave both `seal/` spellings in its body.
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_every_cited_section_exists`.
  Every contract citation names a section that exists, so it lists every
  citation a retired number leaves.
- `tests/text/test_every_agent_reads_the_contract.py`. The shape of a
  definition, its opening sentence, its write bound, and every plugin path a
  step names.

Pins of moved text: `tests/behaviour/test_a_commit_names_its_repository.py`
reads rule 16's body; `tests/behaviour/test_a_probe_that_commits_says_so.py`
reads rule 8's; `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py:96-140`
reads the definitions' reference-root sentences and *Never* lines;
`tests/text/test_broad_gate_rule.py` reads the crafter's citations of rules
2 and 3 (all read).

The agents this run spawns read the installed 0.30.0 contract and
definitions, so none of them works under this branch's text (spawn prompt,
the orchestrator's finding).

Failure scenario of the chosen approach, six months on: a later rule only one
agent acts on is added to the contract, because the contract is where rules
have always gone, and the preload grows again. Nothing here refuses that, by
design, since a check of "one agent acts on it" would be a judgment encoded
as a script. What holds it is the core's *A document is cut by who opens it*,
the reading recorded in this frame, and the `preload` rows `release-report`
prints at every release. A second risk is the retired-number list going
stale when a rule retires without its number being added. D2's numbering case
refuses that: a missing number the list does not name is red.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep each retired rule as a one-line section (today's preamble) | every retired or moved rule costs every spawn a heading, a line and a `check:` line, about 250 bytes, kept for a reader of old records who can `git show` the release instead. Moving a rule out of the contract would then save only its body minus that line | rejected: D2 lists the numbers in one sentence, so the numbering holds at a few bytes per number |
| Drop retired numbers with no list | the next rule after 19 takes 20 again, and a record citing old rule 20 now names a different rule. That is the reuse the numbering rule forbids | rejected: the list is what keeps the next number from being reused |
| Replace the shared contract with a contract per agent, or a build step that writes each agent's rules into its definition | the plugin ships its files as written and the harness injects `skills:` entries whole (`tests/text/test_every_agent_reads_the_contract.py`, read). A per-agent contract restates every shared rule five times, and a generated definition needs a step that keeps it in step with its source, which the core forbids ("Nothing is kept beside the tree to stay in step with it"). Premise checked: of the 18 live rules, 10 bind all five agents (rule 2 by its broad-gate part), rule 9 binds four, and 6 bind both the crafter and the proofer; only rule 16 and rule 2's phase-boundary set bind one (`frame/design.md` *The reading: contract rules*) | rejected: the shared preload is the one structure whose readers really are every agent, so it stays, emptied of what only one agent acts on |
| Move rules 13, 14, 15 and 18 into `agents/crafter.md` *Rules* | the proofer stops having them in front of it at review, and its records show it applies them (3, 25, 31 and 7 records). `check: none reader: the proofer at review` would then name a reader that never receives the rule | rejected (`frame/design.md` *Scope*, Out) |
| Move rules 13, 14, 15 and 18 into `skills/implement/SKILL.md` *2.* | the crafter reads them, and so does the framer, which never writes a test (53 of 54 framer spawns open that file). The proofer opens it in 38 of 136 spawns | rejected, the same grounds |
| Move rule 16 into `agents/crafter.md` | the orchestrator's own commits would then cite an agent's definition, and the session that builds where `Implementation` is `the session` never reads that file | rejected: `skills/implement/SKILL.md` *2.* is read by every party that builds, and contract rule 6 points every other agent's commit at it |
| Move the phase-boundary set into `agents/crafter.md` step 7 | the session that builds reads no agent definition, so it loses the set. `skills/verify/SKILL.md`'s table, which both read, would then cite a definition | rejected: the verify row is the one home both builders read |
| Move the writing-style step into contract rule 11 | the sealer and the tracer, which take no such step (the sealer opened `writing-style` in 0 of 60 spawns), would pay for it on every spawn. A shorter pointer loses the two heading spellings a range read needs, and `tests/text/test_a_language_section_of_writing_style_opens_alone.py` holds them | rejected (`frame/design.md` *Scope*, Out) |
| Move the crafter's fix-pass rule into `skills/implement/SKILL.md` *5.* | the framer pays 1.9 KB more in its read of that file, and #1286 rewrites the rule in 0.31.0 | rejected |
| Move the framer's reframe rule into `docs/running/the-run.md` *The run* | it edits `docs/`, which the issue puts outside this item and #1277 and #1234 edit in this release | rejected: only its copied first sentence goes |
| Move the framer's exchange rule out of its definition | the reading arrives on most framed items, so the framer would open one more file nearly every time | rejected (`frame/design.md` *Scope*, Out) |
| Move the plugin-path sentence into the contract (chosen) | every agent's preload changes by its own copy's length against the contract's one sentence, about +20 bytes for four agents and about +130 for the tracer, which held a shorter clause. The issue's decision: a passage every agent needs belongs in the contract once | chosen; D5's net still falls for every agent |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 3 and 5: D2 and D4. The preamble lists retired numbers 8 and 20; their sections go; the numbering case reads the list; the case reading rule 8's body goes; every citation of rules 8 and 20 the cited-section case lists is re-pointed or reworded. The phase record's first entry checks *The reading*'s coordinates against the tree, as the crafter's *The frame is judged before it is built to* asks | the two new numbering cases seen red against the old case's code, with how they were shown; then in one command `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_a_probe_that_commits_says_so.py` and every module that reads a changed path, all passing | 1884c3c3d |
| 2 | Scope 2: D1. Rule 16 moves into `skills/implement/SKILL.md` *2.* and 16 joins the retired list; the phase-boundary set moves into the verify row; crafter step 7 cites that row; rule 19 cites the core (D3); every citation of rule 16 is re-pointed | `tests/behaviour/test_a_commit_names_its_repository.py` and `tests/text/test_broad_gate_rule.py` retargeted at the new homes and passing (existing cases, new path); the cited-section case and the contract-shape case passing; `git grep -n "contract rule 16"` outside `seal/` lists nothing, executed | d68e9b1d6 |
| 3 | Scope 4: the rest of D3. The plugin-path sentence goes into rule 11 and leaves the five definitions; the reference-root step sentences, the parity record sentences, the framer's copied reframe sentence and the preamble's two copied sentences go | `tests/text/test_every_agent_reads_the_contract.py`, `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` (its reader case retargeted at implement *Document layout*), the contract-shape case and the cited-section case passing in one command; `git grep -n "two directories above" -- agents/` empty, executed | 6455bc17a |
| 4 | Scope 1 and 6: D6. The measurement, and `changelog.md`. This is the first pull request into `release/v0.30.1`, so the commit that adds `changelog.md` also moves `.claude-plugin/plugin.json` to `0.30.1` (`docs/releasing/branch-and-release.md`, the feature pull request bullet) | `release_report.py --against v0.30.0 --at <base clone> --root <clone at HEAD>`, executed, its preload table in the phase record with no agent above its v0.30.0 row; D6's census at 0c68b9933 matching *Grounding*'s reading and at HEAD, executed; the list of every D3 and D4 removal, each with the `git grep` showing it gone, executed; `git show HEAD:.claude-plugin/plugin.json` reading `0.30.1`, executed | 08b43c65f |

## Operational impact

None for a deployer. The plugin's agents read the new preload once the
release that ships it is installed. A spawn prompt that cites `contract rule
16` after that names a retired number. The orchestrator's own skills are
re-pointed in phase 2, and a prompt typed from memory is caught by nothing,
which is why D2's list names the number.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-03 | No paid behaviour-suite run is taken for this preload rewrite | `evals/README.md:19` opens with "A rewrite of an agent's preload is proved not worse by running this suite", and the same section states that nothing in the tree makes a later edit owe a run; #1312's preload rewrite took none on that sentence (`seal/threads/1793661729-each-document-is-cut-by-who-opens-it/frame/design.md:27`), and 0.32.0's #1254 narrows the suite because its record does not bear the opening sentence out. The owner was told and may ask for a run | `evals/README.md` *The behaviour suite — `behaviour/<agent>/`* |
| 2026-11-03 | Round 1's fix (3a4d969b7) is folded into the frame: `frame/design.md` row 16 and D1, and this plan's rule-16 alternative, now say contract rule 6 points every agent's commit at implement's rule | The fix pass changed who the moved rule reaches, and its hand-back named these three statements, which it does not edit, as still saying only the builders and the orchestrator commit; the verifying round and any later crafter read one rule | `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* |
| 2026-11-03 | Round 2's findings 1 and 3 and the frame half of finding 2 are folded by reading the whole frame against HEAD, not only the lines named: S2, S7, Scope 2, D6 and Q1 now state rule 6's sentence, where the figures for the body stand, and the commits Q1 counts | The first fold took only the three statements the fix pass named and left S2 standing, which round 2 found; every statement of the frame that rests on the fix's fact is in this one file set, so it is read whole | `skills/agent-contract/SKILL.md` *12 A defect belongs to a class, so enumerate the class* |
| 2026-11-03 | Four more frame statements the round 2 fix pass named, from its whole reading of the work item's records, are folded: D1's phase-boundary row, D3's rule 11 heading, D6's and phase 4's `release_report.py` flags, and S8. D5 stays, being labelled an estimate the measurement decides | The builders recorded each departure in their phase records, and the frame kept the earlier wording; the sealer reads the frame against the tree | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-03 | Round 3's finding is fixed by widening Q1 to every act the five `gaps.md` rows citing it hand over, and the run stops after it, with no fourth round | Three rounds have found something; each later finding was one kind, a statement of the records a fix left standing, and each smaller; round 3's lies in `frame/questions.md` and `gaps.md` alone, and a fix in the work item's records owes no verifying round, since the sealer reads every record at HEAD. Going on would spend a round near a finding round's price on records the sealer reads anyway | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* |
