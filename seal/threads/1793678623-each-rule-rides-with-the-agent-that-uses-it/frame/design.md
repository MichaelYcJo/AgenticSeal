# Design: each rule rides with the agent that uses it (#1313)

Issue #1313, the first item of milestone `release: 0.30.1`. This design reads
the issue body as it stood on 2026-11-03 after the owner widened it with
*What the reading removes, not only moves* (`gh issue view 1313 --json
body,comments`, executed by this framer; no comments). The milestone
description and the bodies of #1020, #1286, #1288, #1277 and #1234 were read
with `gh` (executed). Every coordinate below is at the base 0c68b9933 (the
0.30.0 release). HEAD 2ddab09c4 adds only `routing.md` (`git diff --stat`,
executed). The installed plugin's contract and definitions are byte-identical
to the tree's (`diff`, executed).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *A document is cut by who opens it and at which step, so a party opens only what its step needs* (read) | A party pays for every byte of each file it opens, on every spawn. The preload is the one file set every spawn pays whatever its step, so a sentence that one agent acts on, or that only one step uses, is weighed for a home that only that agent or step opens |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A fact has one source, and every other place links to it." "History goes to git, the release notes and the work record." Both are the grounds of the removals (D3, D4). A count of lines added against lines removed is context, never a criterion |
| `skills/core/SKILL.md` *Each agent judges its own target* (read) | "An agent's own rules live in its definition or in the document it reads at that step; this file holds what they share." A rule two agents share at one step stays where both read it (D1) |
| `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* (read) | "A rule that would need a per-role exception is not universal." "The contract's rule numbers are stable", and how a retired rule keeps its number "is the contract's own preamble". The preamble keeps the numbering rule, rewritten (D2), so the policy sentence stays true |
| `docs/running/the-agent-set.md` *What a spawn costs* (read) | A spawn's payload is paid on every spawn. The measure is `.github/scripts/release_report.py#preloads` (read: the sum of the definition, the core and the contract, `share == "agent"`) |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | Which subject a work item has is the framer's judgment. This work item's subject is the code: the contract, the agent definitions and the skills that cite them. The issue puts `docs/` outside this item. No `docs/` sentence states a fact this work changes (D7), so `## Rule changes` holds nothing |
| `skills/agent-contract/SKILL.md` preamble (read) | "A rule number is never reused and never re-ordered: a rule that retires keeps its number as one line naming what replaced it." This work rewrites that sentence (D2) |
| `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat` (read) | Holds the one-line form of a retired rule today. D2 changes what it reads |
| `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_every_cited_section_exists` (read) | Every `contract rule <N>` outside the records, and every bare `rule <N>` in the contract and `agents/`, must name a section the contract has. A citation of a number D2 retires fails it, so this case lists the citations to re-point. It is the producer of that list (contract rule 12) |
| `skills/verify/SKILL.md` *The narrow command still has to be able to fail* (read) | A move is proved by the existing cases at the new path, with no case written new. Only D2's numbering reader is new behaviour, so only it is shown red first |
| Owner decisions in memory, as the spawn prompt carries them (orchestrator's finding) | No numeric caps; no ad-hoc tags or marks as an answer to a failure; docs state the latest rule. This design adds no mark and no tag |

### Measured at the base (each executed by this framer in its scratch directory, since removed)

| What | Reading |
|---|---|
| `release_report.py --against v0.30.0 --at <clone> --root <clone>`, run in a `git clone --no-local` at 0c68b9933 | preload `crafter` 33,081; `framer` 36,362; `proofer` 32,293; `sealer` 31,879; `tracer` 25,085 bytes |
| Section bytes (a probe splitting each file at `#` headings and `**` leads) | given per row in *The reading* below |
| Spawns that opened a file, from the 338 `agentic:*` subagent transcripts under this repository's Claude Code project directory (a Read's `file_path` or a Bash command naming the path) | crafter 88 spawns: `skills/implement/SKILL.md` 87, `skills/writing-style/SKILL.md` 86, `skills/verify/SKILL.md` 46, `skills/code-review/SKILL.md` 11. framer 54: implement 53, writing-style 53, verify 7. proofer 136: code-review 136, writing-style 135, implement 38, verify 11. sealer 60: implement 14, verify 4, writing-style 0 |
| Round and guarantee records ever citing `contract rule <N>` (`git log --all -G'[Cc]ontract rule N([^0-9]\|$)' --name-only`, distinct paths) | rule 2: 76 rounds, 15 guarantees; 12: 71, 2; 19: 60, 1; 15: 31, 2; 14: 25, 0; 18: 7, 0; 9: 6; 3: 5; 13: 3, 1; 4, 11: 3 each; 6: 2, 2; 5, 7: 1; 17: 0, 1; 1, 10, 16: 0. Citations in the `§N` spelling before #1005 are not counted, so each count is a floor |
| Ten-word-run census (D6's method) over `agents/*.md`, the contract and the core | crafter 245 of 1,683 words shared; framer 185 of 2,263; proofer 180 of 1,588; sealer 77 of 1,505; tracer 43 of 451; contract 58 of 2,145; core 146 of 1,574; all 934 of 11,209. This tokenizer differs from the issue's, so only D6's own before and after compare |
| History search: `grep -n -E '#[0-9]{2,}\|20[0-9]{2}-[0-9]{2}\|[0-9]+\.[0-9]+\.[0-9]+\|twice\|used to\|before #\|until #\|ever\|history'` over the three file sets | two hits that are history: contract rule 8's `Retired by #1027` and rule 20's `Retired by #1312`. Every section was also read whole (below), so the list is whole for these files, read |

## Scope

In:

1. **The reading**, recorded below in *The reading*: each contract rule with
   the agents that act on it, and each section of each agent definition with
   the step that uses it, each with its decision.
2. **Rules leave the contract where one agent acts on them** (D1): rule 16
   moves into `skills/implement/SKILL.md` *2.*, with one sentence of contract
   rule 6 stating the `git -C` form and pointing there for the agents that
   commit without opening it, and rule 2's phase-boundary set moves into
   `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*.
3. **The retired lines go** (D2): rules 8 and 20, and rule 16's number once
   it moves, become numbers the preamble lists as retired. The numbering
   reader reads that list.
4. **Copies go** (D3): the plugin-path sentence of all five definitions goes
   into contract rule 11 once. The reference-root step sentence leaves the
   crafter's and the framer's definitions, the parity record leaves the
   proofer's and the sealer's step 5, and the framer's reframe rule loses
   its first sentence. Two copied sentences leave the contract's preamble,
   and rule 19 cites the core for what the core states.
5. **History goes** (D4): the two `Retired by` lines, with item 3.
6. **The measurement** (D6): `preloads` and the ten-word census before and
   after, in the last phase record, for the pull request.

Out, each with its grounds:

- **Rules 12, 13, 14, 15, 18 and 19 stay in the contract.** The crafter acts
  on each, and the proofer reads each at review. Proofer records cite them
  (71, 3, 25, 31, 7 and 60 records). The contract is the one text both
  receive on every spawn. The proofer opens `skills/implement/SKILL.md` in 38
  of 136 spawns and the crafter opens `skills/code-review/SKILL.md` in 11 of
  88, so any other home takes the rule away from one of the two at its step.
- **The crafter's *A fix pass appends close blocks* (1,937 bytes) stays.**
  Only a fix pass uses it, but no file a fix pass opens can take it: in
  `skills/implement/SKILL.md` *5.* the framer, which reads that file in 53
  of 54 spawns, would pay for it. #1286 rewrites this rule in 0.31.0.
- **The proofer's *A verifying round answers the closed findings* stays.**
  Only a verifying round uses it, and #1020 rewrites it in 0.31.0.
- **The framer's *An orchestrator's reading of the frame is answered in one
  exchange* stays.** The reading reaches a framer on every framed work item
  (`skills/implement/orchestration.md` *The frame is read against the issue
  at the spawn*), so a moved rule would mean one more file to open on most
  items.
- **The writing-style step stays in the crafter's, the framer's and the
  proofer's definitions.** Each agent opens one section by range and needs
  its two headings' spellings, and
  `tests/text/test_a_language_section_of_writing_style_opens_alone.py` holds
  them. In the contract, the sealer and the tracer would pay for a step
  they do not take.
- **Two shared phrases stay, because tests pin them in every definition:**
  the opening sentence (`tests/text/test_every_agent_reads_the_contract.py#SENTENCE`)
  and the write bound (`#BOUNDS`). D6's census counts them as shared runs
  before and after.
- **`docs/` and `skills/*/orchestration.md`** are outside the reading. The
  issue says so, and #1277 and #1234 edit `docs/` in this release. Only
  citations of a number D2 retires are re-pointed in
  `skills/implement/orchestration.md` and `skills/implement/multi-repository.md`.
- **#1312's *Scope* line that no agent's own rules leave its definition**
  is weighed again, as the issue asks. It holds for every agent rule except
  the D3 sentences. Each of those copies a text the agent opens at the same
  step, so the agent still has the rule in front of it at that step.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The reading is recorded | Given this design, when a reviewer opens a row of *The reading*, then its coordinate at 0c68b9933 holds the section, its agents and step are named, and its decision matches what the diff did | the proofer opens the coordinates with `git show 0c68b9933:<path>` |
| S2 A one-agent rule rides with its step | Given HEAD, when the crafter or the session builds a phase, then the commit form of old rule 16 stands in `skills/implement/SKILL.md` *2.* and the phase-boundary set in `skills/verify/SKILL.md`'s *Scope* table; the contract no longer holds the set, and holds of the commit rule only rule 6's sentence stating the `git -C` form and pointing at implement's rule, for the agents that commit without opening implement *2.* | `tests/behaviour/test_a_commit_names_its_repository.py`, retargeted at the new home, with its case `test_the_contract_points_every_agents_commit_at_the_rule`; `tests/text/test_broad_gate_rule.py`; run narrow |
| S3 A retired number is listed, not kept as a line | Given the contract at HEAD, when the numbering case reads it, then its headings increase and repeat no number, every missing number up to the highest is in the preamble's retired list, and no listed number is a heading | the new numbering cases, each seen red first against a planted gap and a planted listed heading (phase 1) |
| S4 No citation names a retired number | Given HEAD, when the cited-section case runs, then no tracked file outside the records cites rules 8, 16 or 20 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, run narrow |
| S5 Every agent still resolves the plugin's paths | Given any agent at HEAD, when it reads its preload, then contract rule 11 states once where `skills/`, `templates/`, `docs/` and `agents/` paths resolve, and no definition restates it | `git grep -n "two directories above" -- agents/` lists nothing; `tests/text/test_every_agent_reads_the_contract.py` passes |
| S6 Each removed copy is reachable at its step | Given each D3 row, when its reader takes that step, then the kept side is a file that agent opens at that step | the proofer reads each D3 row against *The reading*'s *Opened at that step* column |
| S7 No preload grows, and the change shows | Given v0.30.0 and HEAD, when `release_report.py` runs, then no agent's preload is larger at HEAD, the last phase record holds the table it measured with the commit it measured, and `changelog.md` holds the figures at the work item's last code commit for the pull request body | D6; the command and its table in the phase record; the changelog's figures against each agent's `wc -c` sum at HEAD |
| S8 The census is taken before and after | Given the base and HEAD, when D6's census runs on each, then both readings and each removed copy's pair are in the last phase record, with the commit it measured, and `changelog.md` holds the reading at the work item's last code commit | D6 |
| S9 Nothing the issue keeps out moves | Given the diff, when the proofer reads it, then no `docs/` file changes, and `skills/*/orchestration.md` changes only where a retired number was cited | `git diff --stat 0c68b9933...HEAD -- docs/ skills/*/orchestration.md` |

## Data & interfaces

### The reading: contract rules

Agents are those that take the act the rule governs, read from each
definition's steps. "All" is the five.

| Rule (line, bytes) | Agents that act on it, at which step | Decision |
|---|---|---|
| preamble (`:16`, 715) | all, on every spawn: how to cite a rule | stays. Its first sentence copies every definition's opening sentence, and "A role's rules live in that role's definition" copies the core's *Each agent judges its own target*; both go (D3). The numbering sentence is rewritten (D2) |
| 1 (`:28`, 360) | all, at every command | stays |
| 2 (`:36`, 729) | the phase-boundary set: the crafter at step 7, and the session where it builds. The rest, that no agent runs the broad gate and the suite goes over `unverified`: all | the phase-boundary set moves (D1); the rest stays |
| 3 (`:48`, 740) | all, at each spawn prompt | stays |
| 4 (`:61`, 386) | all, at the hand-back | stays |
| 5 (`:69`, 642) | all, at the handoff | stays |
| 6 (`:80`, 555) | all, at every write and at the hand-back | stays |
| 7 (`:91`, 900) | all five probe | stays |
| 8 (`:104`, 239) | none: retired | the line goes, and the number is listed (D2, D4) |
| 9 (`:110`, 850) | all that edit: crafter, framer, proofer's probes, sealer's `guarantee.md` | stays |
| 10 (`:126`, 747) | all, at every read | stays |
| 11 (`:139`, 900) | all, at every `seal/` path and record | stays, and gains the plugin-path sentence (D3) |
| 12 (`:155`, 1,050) | crafter at a fix, proofer judging the method, framer listing a class; 71 proofer records cite it | stays; #1020 reworks it |
| 13 (`:172`, 248) | crafter writing a defence's case; proofer at review | stays (Out, first item) |
| 14 (`:178`, 364) | crafter at a change to a message; proofer at review (25 records) | stays |
| 15 (`:186`, 390) | crafter planting a case; proofer (31 records) and sealer re-running `seen red` | stays; #1286 may extend it where it stands |
| 16 (`:194`, 714) | crafter at each commit. No other definition names a commit: the proofer's and the sealer's leave it to the orchestrator, the tracer writes nothing, and the framer commits only where a spawn prompt asks, as this one did. The orchestrator cites it at `skills/implement/orchestration.md:364` and `skills/implement/multi-repository.md:20`. No record cites it | moves (D1); contract rule 6 keeps one sentence pointing every agent's commit, a probe's included, at its new home, because the framer and the probes of the proofer, sealer and tracer commit without opening implement *2.* (round 1) |
| 17 (`:208`, 495) | all, at clean-up | stays |
| 18 (`:218`, 351) | crafter at a refusing check; proofer at review (7 records) | stays |
| 19 (`:226`, 548) | crafter at every change; proofer at review (60 records) | stays; its first clause copies the core's last paragraph, so it cites the core (D3) |
| 20 (`:236`, 265) | none: retired | the line goes, and the number is listed (D2, D4) |

### The reading: agent definitions

Each row is a section: a `##` heading, a numbered step, or a `**` rule lead.
Bytes are per section. *Opened at that step* names the file the agent has in
front of it at that step, where a D3 removal relies on it.

**`agents/crafter.md` (10,952)**

| Section (line) | Step that uses it | Decision |
|---|---|---|
| frontmatter and opening (`:1`, `:12`) | every spawn | stays; pinned |
| *Job* (`:17`, 465) | every spawn | stays |
| step 1 (`:28`) | every spawn. Its sentence "Every `skills/`, `templates/` and `docs/` path in this file is the plugin's, …" (`:29-33`) copies the framer's, proofer's, sealer's and tracer's | the sentence goes into contract rule 11 (D3) |
| step 2 (`:34`) | every spawn. "A reference root (…) is read where the work touches what it describes, and cited where `frame/design.md` cites it." (`:37-39`) copies `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, which step 1 opens (87 of 88 spawns) | the sentence goes (D3) |
| steps 3, 4 (`:40`, `:41`) | build spawn | stay |
| steps 5, 6 (`:43`, `:51`) | build phase | stay |
| step 7 (`:53`) | build phase boundary; names "the phase-boundary set contract rule 2 names" | cites `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, which step 5 already opens (D1) |
| step 8 (`:55`) | closing a phase | stays (Out, writing-style) |
| step 9 (`:62`) | fix pass | stays |
| step 10 (`:64`) | every hand-back | stays |
| *Never* (`:72`, 648) | every spawn | stays; the reference-root line is pinned by `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` |
| *The frame is judged before it is built to* (`:88`, 501); *A declared frame that is absent stops the build* (`:96`, 257) | build spawn | stay |
| *The handoff's facts are coordinates to open* (`:101`, 333) | every spawn | stays |
| *A new test starts from its group* (`:107`, 414); *Commit before you mutate* (`:114`, 371); *Mutation-test every unit* (`:120`, 846) | build phase | stay |
| *A stop at three failed fixes is handed back* (`:136`, 295) | build and fix | stays |
| *Find the runner* (`:142`, 464); *The broad gate is not yours* (`:150`, 469) | every spawn | stay |
| *Each phase closes with its record* (`:158`, 320) | build phase | stays |
| *A fix pass appends close blocks* (`:164`, 1,937) | fix pass only | stays (Out) |
| *The chain ends at a pull request* (`:193`, 258) | every hand-back | stays |

**`agents/framer.md` (14,233)**

| Section (line) | Step that uses it | Decision |
|---|---|---|
| *Job* (`:19`, 1,313) | every spawn | stays |
| step 1 (`:43`) | every spawn; the plugin-path sentence (`:44-47`) | the sentence goes into rule 11 (D3) |
| step 2, step 3 (`:48`, `:52`) | every spawn | stay |
| step 4 (`:57`) | every spawn. "A reference root (…) is read where the work touches what it describes, and cited in `frame/design.md` by path." copies `skills/implement/SKILL.md` *Document layout*, which the framer opens on every spawn for *A design states its rule changes* | the sentence goes (D3) |
| steps 5 to 8 (`:86`-`:98`) | every spawn | stay; step 6 is the writing-style step (Out) |
| *Never* (`:114`, 378) | every spawn | stays; pinned as the crafter's is |
| *You ask nobody anything* (`:126`, 416) through *Bound each call, not the reading* (`:220`, 486), eleven rules | every spawn. *A question a command answers* (1,406) applies wherever a probe can answer, which is most frames; *A mark is not the answer to a blocked step* (771) is weighed on every design | stay |
| *An orchestrator's reading of the frame is answered in one exchange* (`:228`, 578) | the exchange before the first build spawn, on most framed items | stays (Out) |
| *The one route back is the review chain's* (`:237`, 644) | a reframe spawn only. Its first sentence, "A builder that finds the frame does not hold writes it into its phase record and hand-back, and you are not spawned again for it.", is the crafter's act, which `agents/crafter.md` *The frame is judged before it is built to* states; a framer is never spawned at that moment | the first sentence goes (D3). The rest stays: no file the framer opens on a reframe states the new phase rows and the kept commits for it, since `docs/running/the-run.md` *The run* gives only the `Reframed` line and `skills/code-review/orchestration.md:218` is the orchestrator's |

**`agents/proofer.md` (10,164)**

| Section (line) | Step that uses it | Decision |
|---|---|---|
| *Job* (`:17`, 267) | every spawn | stays |
| step 1 (`:26`) | every spawn; the plugin-path sentence (`:27-30`) | goes into rule 11 (D3) |
| steps 2 to 4 (`:31`-`:36`) | every round | stay |
| step 5 (`:38`) | a repository with `seal/parity.md`. "Where the pull request changes a path outside `docs/` and `seal/`, write the `original:` line …; where the original could not be resolved, write no line and raise an `unread` finding." copies `skills/legacy-parity/SKILL.md` *Recording the comparison*, which the same step opens | the copied sentences go, and the step cites that section (D3) |
| step 6 (`:44`) | writing the record | stays (Out) |
| step 7 (`:48`, with the `chain_check.py` notice sentences) | every round | stays |
| *Never* (`:69`, 582) | every round | stays |
| *The record goes to the branch worktree* (`:84`), *The clone is named …* (`:90`), *The implementer's account is a claim* (`:98`) | every round | stay |
| *Earlier rounds carry coordinates* (`:109`, 864) | every round after the first | stays |
| *A verifying round answers the closed findings* (`:124`, 1,357) | verifying rounds | stays (Out) |
| *Each new test is read against its group* (`:143`), *The broad gate is not yours* (`:150`), *Runs are narrow* (`:160`), *A probe leaves nothing* (`:171`) | every round | stay |

**`agents/sealer.md` (9,750)**

| Section (line) | Step that uses it | Decision |
|---|---|---|
| *Job* (`:22`, 1,831) | every spawn; the plugin-path sentence (`:43-45`) | the sentence goes into rule 11 (D3); the rest stays |
| steps 1 to 4 (`:57`-`:99`) | every audit | stay |
| step 5 (`:100`) | every audit. Its parity part, from "Where git carries `seal/parity.md`" to "never a line.", copies `skills/legacy-parity/SKILL.md` *Recording the comparison*, which the same sentence opens | the copied part becomes a citation of that section (D3) |
| step 6, *Never*, the six rules (`:118`-`:175`) | every audit; *The guarantee covers HEAD, and a re-run audits what came after* (584) on a second audit, which follows any commit after a verdict | stay |

**`agents/tracer.md` (2,956)**

| Section (line) | Step that uses it | Decision |
|---|---|---|
| step 1 (`:27`) | every spawn; "the plugin's, at the root two directories above the base directory the harness printed with the contract" | the clause goes, since rule 11 states it (D3) |
| every other section | every spawn | stay |

**`skills/core/SKILL.md` (9,223)**: every section is read by every party.
The census pairs it shares with `docs/running/what-a-script-gates.md`,
`skills/implement/orchestration.md` and `CONTRIBUTING.md` (20, 13 and 10
runs) are copies of the core in files this item leaves alone, and one copy
the core keeps with the four cited headings of its table. No sentence of the
core is history or a copy whose other side its readers open, so it does not
change.

### D1 One-agent rules move to where their step reads

| Rule | New home | Why there |
|---|---|---|
| 16, whole, with its `check:` line | `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*, as a bold-lead rule after *Commit at the smallest step that stands on its own* | the parties that build read that file: the crafter (87 of 88 spawns), the session where it builds, and the orchestrator that cites the rule. An agent that commits without opening it, the framer where a spawn prompt asks and any agent's probe, has contract rule 6's one sentence pointing at it, so every agent pays that sentence in place of the 714 bytes |
| 2's first sentence, the phase-boundary set | the *Phase boundary* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, which now holds the set itself | the crafter's step 5 already sends it to the table beneath that one, and the session that builds reads `verify` too. Rule 2 keeps the slice tests, the broad gate and the `unverified` hand-over |

Rule 16's text moves with its wording, apart from "A file edit is rule 9's",
which becomes "contract rule 9". The citations of rule 16 go to its new
home: `skills/implement/orchestration.md:364`,
`skills/implement/multi-repository.md:20`, and the module docstring and
`test_the_orchestration_cites_contract_rule_16` of
`tests/behaviour/test_a_commit_names_its_repository.py`, which read the new
section (the existing cases at the new path). The cited-section case gives
the whole list. Any citation of rule 2 that names the phase-boundary set
names the verify row, `agents/crafter.md:53` and `skills/verify/SKILL.md:144`
among them.

### D2 A retired number is listed in the preamble

The preamble's numbering sentence becomes, within the same length:

> A rule number is never reused and never re-ordered. A rule that retires
> leaves the file and its number stays unused; the retired numbers are 8, 16
> and 20, and a new rule takes the number after the highest of these and of
> the rules below.

Git holds what the retired rules said. Rules 8 and 20 go as sections.

`test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat` becomes
a reader of that list. Headings increase, and no number repeats. The numbers
missing from 1 up to the highest heading are exactly the listed ones, and no
listed number is a heading. Two planted contracts show it can fail: one with
a gap the list does not name, and one whose list names a number that has a
heading. Each is seen red against the old case's code before it is committed.
The module docstring says the same in place.

`tests/behaviour/test_a_probe_that_commits_says_so.py#test_the_retired_rule_keeps_its_number_and_none_of_its_shapes`
reads rule 8's body, so it goes with the line. The module's other cases stay,
and its docstring drops the sentence on the rule 8 line. Citations of rules 8
and 20 are re-pointed or reworded where they stand: `tests/conftest.py:1144`,
`tests/skills/test_broad_gate.py:2625`,
`tests/text/test_a_moved_rule_leaves_its_definition.py:46`,
`tests/behaviour/test_a_probe_that_commits_says_so.py:6`, and any other the
cited-section case lists. A bare `rule 20` in a test,
`tests/text/test_the_rules_have_one_owner.py:206`, is not a citation the case
reads, and is reworded by the same rule 19.

### D3 Copies: which side stays

| Copy | Kept on | The other side | Opened at that step |
|---|---|---|---|
| where the plugin's `skills/`, `templates/` and `docs/` paths resolve | contract rule 11, as one sentence naming `agents/` too, for this file and the agent's definition; the heading becomes *Where the plugin's paths and the `seal/` root resolve, and the record language* | the sentence leaves `agents/crafter.md:29-33`, `agents/framer.md:44-47`, `agents/proofer.md:27-30`, `agents/sealer.md:43-45`; `agents/tracer.md:27-29` keeps "Open `skills/legacy-parity/SKILL.md`." | the contract, preloaded before the definition |
| the reference root is read where the work touches it | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | leaves crafter step 2 and framer step 4. The *Never* lines stay. `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`'s reader case for the two definitions reads the implement section (the existing case at the new path) | crafter step 1 opens implement; the framer opens *Document layout* for *A design states its rule changes* |
| the parity record's `original:` line | `skills/legacy-parity/SKILL.md` *Recording the comparison* | proofer step 5 and sealer step 5 keep the act, "compare", and cite the section for the record | each step opens that skill in the same sentence |
| who writes when the frame does not hold | `agents/crafter.md` *The frame is judged before it is built to* | the first sentence of the framer's *The one route back is the review chain's* goes | the framer is not spawned at that moment, so it needs no copy |
| the contract preamble's "You received this file at startup, before your first tool call, through the `skills:` list in your definition." | every definition's opening sentence | the preamble sentence goes | the definition |
| the preamble's "A role's rules live in that role's definition" | the core's *Each agent judges its own target* | the clause goes; "a rule that would need a per-role exception here is not universal" stays | the core, preloaded first |
| rule 19's "and in the same commit removes or corrects what stood on the old fact" | the core's *The rule a mechanism is kept against* | rule 19 cites the core for the rule, and keeps the method: `git grep` on its words, a sample named as rule 12 asks, and no correction beside its sentence | the core, preloaded |

One copy stays on both sides. `skills/implement/SKILL.md` *2.*'s *An edit must
be able to fail* and the two paragraphs after it restate contract rule 9.
Its readers include a session that builds where `Implementation` is `the
session`, and the orchestrator. Neither is preloaded with the contract, which
binds such a session "only if you load it" (`skills/implement/SKILL.md:20-25`,
read). So at that step the kept side would be a file its reader does not
open, and implement keeps its paragraphs, the `assert old in text` form among
them (the orchestrator's reading, agreed).

### D4 History

The two hits are rule 8's and rule 20's `Retired by` lines. D2 removes both.
Their record is git, the release notes of #1027 and #1312, and those work
items' records.

### D5 Expected preloads

Estimated from the section bytes above. The measurement decides.

| Agent | Base | Change (estimate) |
|---|---|---|
| crafter | 33,081 | about -1,500 |
| framer | 36,362 | about -1,700 |
| proofer | 32,293 | about -1,500 |
| sealer | 31,879 | about -1,550 |
| tracer | 25,085 | about -1,300 |

The contract loses about 1,300 bytes and every agent shares that.
`skills/implement/SKILL.md` grows by rule 16, about 600 bytes, for the
crafter and the framer when they read *2.*.

### D6 The measurement

- **Preloads:** `uv run python .github/scripts/release_report.py --against
  v0.30.0 --at <base> --root <head>`, with `<base>` a clone at 0c68b9933
  and `<head>` a clone at HEAD, since `--at` is the tag's tree and `--root`
  the current one. The `preload` rows at v0.30.0 are the before, and the
  rows at HEAD are the after.
- **Census:** a read-only probe in the crafter's scratch directory, run at
  0c68b9933 and at HEAD. It tokenizes every tracked `.md` and `.py` file
  outside `seal/` and `tests/` into lowercase runs of
  `[a-z0-9_/.'-]+` with `.` and `'` stripped from each end. For each file of
  `agents/*.md`, the contract and the core, it counts the words inside any
  ten-word run another corpus file also holds, and the six files it shares
  most runs with. The reading at the base must equal the one above, which
  shows the probe is the same. A copy D3 removed is named as gone from its
  pair. The two pinned phrases stay shared by design.
- Both readings, the commands and the list of D3 and D4 removals go into the
  last phase record, which states the commit it measured. A fix after that
  phase that changes a measured file brings the figures in `changelog.md`
  to the new HEAD, and the pull request body copies the figures from the
  changelog.

### D7 Policy in force

`docs/running/the-agent-set.md` says a retired rule's numbering is "the
contract's own preamble"; D2 keeps it there. `docs/checks/the-routing-check.md:77`
cites rule 9 and `docs/layout/one-root-by-lifetime.md:28` cites rule 11, and
both rules keep their numbers and their facts. No `docs/` file cites rules 2,
8, 16, 19 or 20 for what changes (`git grep`, executed). So the policy root
needs no edit, and the settle gathers nothing from this item. The unsettled
design `seal/threads/1793661729-each-document-is-cut-by-who-opens-it/` states
`- nothing` too (read).

## Rule changes

- nothing
  why: This work item's subject is the contract, the agent definitions and two skills, and no document of the policy root states a fact it changes (D7).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| rule 8's retired line | `skills/agent-contract/SKILL.md` *8 Retired: no gate reads a probe's commit* | the preamble's list of retired numbers; git and #1027's records hold its text (D2, D4) |
| rule 20's retired line | `skills/agent-contract/SKILL.md` *20 Retired: do not avoid the change a problem calls for* | the same list; #1312's records hold it (D2, D4) |
| rule 16 as a contract section | `skills/agent-contract/SKILL.md` *16 A commit names its repository in the command that makes it* | `skills/implement/SKILL.md` *2.*; its number joins the list (D1) |
| the phase-boundary set in rule 2 | `skills/agent-contract/SKILL.md` *2 Narrow and often; the broad gate is the orchestrator's* | the *Phase boundary* row of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* (D1) |
| the case reading rule 8's body | `tests/behaviour/test_a_probe_that_commits_says_so.py#test_the_retired_rule_keeps_its_number_and_none_of_its_shapes` | the rule it reads is gone; the numbering case reads the list (D2) |
| the one-line form of a retired rule, as the numbering case reads it | `tests/text/test_the_agent_contract_holds_the_universal_rules.py#test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat` | the same case, reading the preamble's list (D2) |
| the plugin-path sentence in five definitions | `agents/crafter.md` *Order of work*, `agents/framer.md` *Order of work*, `agents/proofer.md` *Order of work*, `agents/sealer.md` *Job*, `agents/tracer.md` *Order of work* | contract rule 11 (D3) |
| the reference-root step sentence | `agents/crafter.md` *Order of work* step 2, `agents/framer.md` *Order of work* step 4 | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (D3) |
| the parity record's sentences | `agents/proofer.md` *Order of work* step 5, `agents/sealer.md` *Order of work* step 5 | `skills/legacy-parity/SKILL.md` *Recording the comparison* (D3) |
| the crafter's act in the framer's reframe rule | `agents/framer.md` *The one route back is the review chain's*, first sentence | `agents/crafter.md` *The frame is judged before it is built to* (D3) |
| two copied sentences of the preamble | `skills/agent-contract/SKILL.md` preamble | every definition's opening sentence, and `skills/core/SKILL.md` *Each agent judges its own target* (D3) |
| rule 19's restatement of the core | `skills/agent-contract/SKILL.md` *19 A change rewrites the text it amends in place* | `skills/core/SKILL.md` *The rule a mechanism is kept against* (D3) |

This work adds no mechanism. D2 changes what an existing case reads, and the
case refuses the same defect, a lost or reused number, in the form the new
numbering rule gives.

Framed 2026-11-03 by framer, before the build.
