# Design: 1793411151-judgment-where-meaning-is-the-question

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*: "a script does not re-encode that judgment as a grammar rule: it reads what a command wrote or what a real parser returns" (read, at `f80f48e6`) | The rule the issue asks for is in the core since #1186. What is missing is its application: five scripts still carry a grammar of spellings a label "means", and one reads another tool's format by hand. Table A under *Data & interfaces* lists every gate with what it reads, and Scope items 5 to 10 apply the sentence to each. |
| the same, *The rule a mechanism is kept against*: "A script blocks work only on a fact it reads exactly, such as an exit code or a parser's result; a reading that is noisy or guessed from words is reported, never used to block." | The sentence says what a script may block on and does not say what a script owes for what it did not read. Scope item 1 rewrites it: a script reads the plugin's own forms in one spelling each, names what it did not read, and carries no list of the spellings a label is written in. The near-miss refusals become reports. |
| the same, *Judgment is not licence to skip a party*: "A few invariants hold the chain and are not open to judgment: ... Each names what it protects and is held by a mechanism" | The sentence promises a protection and a mechanism per invariant and names neither. Table B gives both; Scope item 1 puts the table in the core, the one file every party reads. |
| the same, *A rule is guidance for a judgment, not a sequence to execute* | The round cap, the regression routing and the filing ladder are still written as sequences in `skills/code-review/orchestration.md` and `docs/the-review-record.md` *The run*. Scope item 11 rewrites them as what to weigh, what each option costs and which signals say the rounds are not converging. |
| the same, *A judgment stands on a source document, and is written down with both*: "Whoever judges, the orchestrator or an agent, writes the decision, its grounds and the document it judged against into the work item's records" and "the settle, or a command run by the owner ... reads them" | The framer, the proofer and the sealer already have such a place (Table C). The orchestrator's run judgments have none, and nothing reads any of them. Scope item 11 gives them `frame/plan.md` *Judgments of the run*; Scope item 12 gives the settle's dry run the reading. The owner left the choice between the settle and a command to this frame (the issue's comment of 2026-10-31): the settle, for the grounds in `frame/plan.md` A5. |
| the same, *Asking a person is the most expensive step*; `routing.md` answers `Automation` `yes` | Nothing in this run asks a person. Every judgment the issue left open is decided here with its grounds, and `frame/questions.md` holds no row for a person. |
| the same, *A mechanism stays only while its record of what it caught outweighs what it costs* and *Nothing is kept beside the tree to stay in step with it* | Table A is a policy table, not a stored count: each row names a script that has its own tests and its own home sentence, and the settle reads policy against code. No test holds Table A against the tree (`frame/plan.md` A7). |
| `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*: policy outranks the ticket, and "Verify clause numbers a ticket cites" | The issue cites `CLAUDE.md` *The rule a mechanism is kept against* and *The rules steer judgment, and a few invariants hold the chain*. Since #1186 both live in `skills/core/SKILL.md` under the headings this table cites, and `CLAUDE.md` names that file (read). Every citation below is to the core. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* and `skills/settle/SKILL.md` *Rule changes*: the policy root is written by the settle from the released designs' `## Rule changes`, and an `add` with no `section` is a new document | Every change under `docs/` is an item of `## Rule changes` below and lands at the settle after this release; `aa9221d3` and `f80f48e6`, the last two work items, touched no file under `docs/` (executed, `git show --stat`). Skills, agent definitions, templates, tests and `CONTRIBUTING.md` are edited in place. |
| `docs/the-review-record.md` *The round record*: "A line that means a label and is spelt another way ... is refused at its line as the label its `Means` cell names" and the `Old spelling` table | The grammar of meant spellings. Probe B below shows a finding whose verdict reads `Verdict: open` refused as "a label in another spelling"; probe A shows the same finding with no `verdict:` line at all refused as "no `verdict:` line". The second refusal is structural and stays; the first is a judgment of meaning and becomes a report (Scope item 5). |
| `docs/the-review-record.md` *What the check reads at the pull request*: "Of a round record the check reads its labelled lines, and refuses what it cannot read" | Kept. Added: the check names each file under `trail/rounds/` whose name is no `round-N.md`. Probe D shows a `Round-2.md` beside a clean record named by nothing (0 lines of output). |
| `docs/the-review-record.md` *The run*: the cap "counted from the last design change", the extension line, "A second regression on the same unit after a fix-pass route goes to the framer whatever the comparison says", "A leftover finding takes the first rung that fits" | The three-round default stays as the point where the orchestrator weighs rather than spawns by habit; the count-driven extension, the hard second-regression route and the rung order become guidance with their signals and costs. The extension line, written by the proofer from the spawn prompt's reason, was never written in any round record: 0 under `seal/threads/` (executed, `grep -rn "Extended past round"`), and the 6 commits `git log -S` finds for it touching `seal/` are the documents and templates that stated it. It goes; the orchestrator's row in `frame/plan.md` replaces it. |
| `docs/the-review-record.md` *The guarantee*: "written exactly so and with no emphasis. Any other spelling of the line is refused at it." | A `Verdict:` line spelt otherwise becomes a named, unread line; a guarantee with no `Verdict:` line, or with two, is refused as now. `seal_stamp.py#queue_for_written_guarantee` and `#sealed_before` read the verdict through `chain_check.verdicts_of` (read, `seal_stamp.py:1164`, `:1347`), so one change reaches both readers. |
| `docs/the-pact.md` *The pact anchor*: "The anchor table is the table whose header means `| Pact | Clause | Hash |`, and one closed normalisation decides that." | A script deciding that `pact` means `Pact` is the judgment the core delegates. The exact header is read; a header the normalisation would have taken is named as a table the tool did not read (Scope item 6). The template writes the exact header (`templates/setup/pact.md:23`, read). |
| `skills/settle/SKILL.md` *Rule changes* ("is a near miss: it is refused at its line") and *A rule has one shape* ("A line whose only content before the label is Markdown block markup or emphasis is a near miss and is refused at its line") | Two more refusals by meant spelling, in `rule_changes.py#parse` and `.github/scripts/rules.py#NEAR`. Both become reports (Scope items 7 and 8); the skill's sentences change in place. |
| `skills/verify/SKILL.md` *The answerer has to exist*: "It reads command text rather than a YAML graph" and the five outcomes | `seal deferrals` reads a workflow's `on:` key by hand (`deferral_check.py#read_events`, `#block_entries`, `#continued`), and the owner's comment lists two shapes YAML refuses that the scan answers. No YAML parser is importable where the tool runs (executed, `python3 -c "import yaml"` fails here; CI installs none, read `.github/workflows/test.yml:149`). The trigger reading goes; the tool names each workflow holding a runner for its reader to open (Scope item 10). |
| `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*: "검사가 읽는 줄은 정해진 철자 하나만 읽히고 조금 틀린 철자는 그 줄에서 거절되어야 한다" | The sentence states the rule this work removes and is the home #1170 names. It changes in the commit that changes the readers (contract rule 19), to the core's rule: one spelling is read, a line spelt otherwise is named and never refused for its spelling, and whether it meant the label is the reading agent's (Scope item 2). |
| `docs/the-agent-set.md` *What a spawn costs*: "The orchestrator's acts are counted, each against what delivers it" and `skills/implement/acts.md` | The headings of the two rewritten sections keep their text, so the acts table keeps its rows; their Grounds cells are reread (Scope item 11). |
| `docs/the-record-layout.md` *seal/threads/<work-item-id>/*: the `frame/plan.md` row | Gains the judgments the orchestrator writes there (`## Rule changes`). #1148's pending change to the same row applies first in merge order. |
| `docs/release-checklist.md` *2b. Settle what earlier releases left behind* | The settling session reads the dry run's judgments before `--apply` removes the records that hold them (`## Rule changes`). |
| `CONTRIBUTING.md` *What a change to a gate must carry* (this repository's, read) | Gains the bullet **What it reads**: a change to a gate names the form it reads, what it names as unread and the agent that judges the meaning. #1149's bullet on removal is that issue's. |
| The issue whole: body, the owner's comment of 2026-10-29 (two `seal deferrals` misreadings) and the orchestrator's comment of 2026-10-31 (the settle-or-command choice is the framer's) (executed, `gh issue view 1167 --json body,comments`, 2026-10-31) | Each *Done when* is judged in *Scope*. The two misreadings close as moot: the scan that misread is removed. |
| Milestone 75, `release: 0.26.1`, renamed from 0.25.3 on 2026-10-31 (executed, `gh api repos/:owner/:repo/milestones/75`); its ten issues all open and all in that milestone (executed, `gh issue view` on each) | The spawn named 0.25.3; the tracker now says 0.26.1. Table D decides each of the ten against this frame's result: three are built here, seven keep their decision and their milestone. |
| Probe A, executed in a `git clone --no-local` under the scratchpad: a round record whose finding has no `verdict:` line, `chain_check.py --baseline origin/release/v0.25.2 --worktree` | Refused: "no `verdict:` line: a finding carries one, at the start of a line and with no emphasis". The structural refusal for a required line exists and needs no near-miss rule. |
| Probe B, the same with `Verdict: open` and no lowercase line | Refused: "a label in another spelling: the check reads `verdict:` at the start of a line, lowercase, with no emphasis and one space after the colon". After this work the same record is refused by probe A's sentence, and the line is named as not read. |
| Probe C, the same with `refixes: round-1#1` beside `verdict: deferred #1` | Refused as another spelling of `regression:`. After this work the line is named as not read and the finding stands as written; in a later round the finding it meant to name is refused as unnamed by the next record. |
| Probe D, a clean `round-1.md` and a copy of it as `Round-2.md` | 0 output lines name `Round-2.md`. #1121's R11, reproduced at this base. |
| `git log -S` over `seal/specs` and `seal/threads` for `refixes:`, `fix of a fix:` and `Target SHA:` (executed): 22, 6 and 51 commits | The old spellings are the labels records carried before 0.22.x renamed them; every work item that wrote them has been settled and removed, and no record under `seal/threads/` carries one today (executed, `grep -rln` finds none). The `Old spelling` table has nothing left to translate. |
| `tests/skills/test_chain_check.py`: 3,790 lines, 133 cases; near-miss cases at `:837`, `:1068`, `:2646`, `:3370` (executed, `grep -n`) | The cases the chain_check phase rewrites or removes. |
| `tests/behaviour/test_one_word_one_meaning.py`: 24 cases pinning "the pinned phrasing AND the absence of the loose one" across documents (read, its docstring; executed, `grep -c`) | A case that pins a sentence's wording turns red when the wording changes and the meaning does not, which the core calls the worst result the workflow can give. Its removal is #1197's, not this work item's (Scope item 4). |
| `hooks/lib/core.py#CAP` is 10,000 characters, and `core.output` over the core at `f80f48e6` is 6,647 characters; over a draft of Scope item 1's text, the rewritten sentence and Table B's five rows as written above, it is 8,147, a margin of 1,853 (executed, `core.output(root, root)` in a `git clone --no-local` under the scratchpad with the draft written into its `skills/core/SKILL.md`; the header line there carries the scratch path, so a user's output is shorter by the path's difference) | Item 1 fits under the hook's cap with room for the crafter's wording. Phase 1's *Verified by* measures the committed text the same way, and where the margin falls under 1,000 characters Table B's `Held by` cells name each mechanism by its path alone and the explanation stays in `docs/what-a-script-gates.md`. |
| Milestone 74 is `release: 0.26.0`, #1167 is in it, 70 is `release: 0.27.0`, `origin/release/v0.26.0` and `origin/release/v0.25.2` both resolve to `f80f48e6`, no pull request has the new branch as its base, and `.claude-plugin/plugin.json` reads `0.25.2` (executed, `gh api`, `gh issue view`, `git rev-parse`, `gh pr list`, 2026-10-31, after the orchestrator's frame reading named the rename) | Scope item 14: the base, the version move and the `feat:` prefix. The probes above ran against `origin/release/v0.25.2`, which is the same commit. |

## Scope

In. Each item is one decision of this frame; `frame/plan.md`'s Delivers cells cite them by number.

1. **The core states the rule for scripts and lists the invariants with their protections and mechanisms.** In `skills/core/SKILL.md` *The rule a mechanism is kept against*, the sentence "A script blocks work only on a fact it reads exactly ... never used to block" is rewritten: a script holds a gate only on a fact it reads exactly, an exit code, a parser's result or a line of the plugin's own forms in the one spelling the form gives it; what it did not read it names and decides nothing about; no script carries a list of the spellings a label is written in; whether a line spelt otherwise meant the label is the judgment of the agent that reads the record. The sentence on noisy readings stays. In *Judgment is not licence to skip a party*, the list of five invariants becomes Table B, each row with what it protects and the mechanism that holds it, and the paragraph's two sentences around it stay.
2. **`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* says what the core says.** The sentences from "검사가 읽는 줄은 정해진 철자 하나만 읽히고" to "그 줄을 읽지 않은 것과 같다" are rewritten: a line a check reads is written in the one spelling the check reads; a line spelt otherwise is named by the check as one it did not read and is never refused for its spelling; whether it meant the label is the reading agent's judgment. The paragraph's `check:` line names `tests/skills/test_chain_check.py` and `tests/github/test_rules.py` as what holds the naming. This is #1170's second half, done here because the sentence stands on the fact Scope items 5 to 9 remove (contract rule 19).
3. **`CONTRIBUTING.md` *What a change to a gate must carry* gains the bullet "What it reads".** A pull request that adds or changes a gate names the form the gate reads, what the gate names as unread, and the agent and step that judge the meaning of the same text; `skills/core/SKILL.md` *The rule a mechanism is kept against* is why. The bullet cites no document this release does not ship.
4. **`tests/behaviour/test_one_word_one_meaning.py` stays in this work item; its removal is #1197.** Phase 1 found that three `check:` lines under the policy root name the module (`docs/the-broad-gate.md:33`, `docs/the-pact.md:18`, `:31`), that `.github/scripts/rules.py` refuses a line whose target is gone and excuses only a pending `remove` of a whole section, and that the removal reaches eight more places this frame's `## Removes` did not name (`trail/phases/phase-1.md`). The orchestrator took it out on 2026-10-31: the removal needs rule changes landed at a settle before the module can go, and none of #1167's *Done when* turns on it. `tests/text/test_the_rules_have_one_owner.py` is kept, because its cases pin that a rule's owner states the rule and that each link names the owner, and the crafter rewrites its sentences for the sections item 11 changes.
5. **`skills/code-review/scripts/chain_check.py` reads each label in one spelling, names what it did not read, and refuses only what the grammar requires.** The near-miss refusal (`misspelt`, `spelt_otherwise`, the `MEANT` pattern over `SPELT`) becomes a report: a line outside every fence whose first word, case folded and stripped of emphasis, is a label's and ends in a colon, and that is not the label, is printed as `path:line  not read: <why>` and changes no exit code. The `Old spelling` table is no longer loaded: `OLD_COLUMNS`, `old_spelling` and `OLD_SPELLINGS` go, and `grammar` reads the one table and stops at exit 2 only where that one cannot be read. `original_of` counts the exact `original:` line only, so a misspelt one is absent and refused where owed (#1121's R9). `round_records` names each file under `trail/rounds/` whose name `routing.py#round_number` does not match as not read (#1121's R11). `verdicts_of` reads `Verdict:` at the start of a line exactly and names a line that opens like the label and is not it; `seal_stamp.py` reads through it unchanged. The refusal texts for a missing required line stand and are pinned (contract rule 14). Every case is seen red (contract rule 15).
6. **`skills/verify/scripts/pact_check.py` reads the anchor table under the exact header `| Pact | Clause | Hash |`**, and a table whose header `header_key` would have matched is named at its line as a table the tool did not read, with the exact header to write; it is not graded and is no refusal. The signer's summary is unchanged.
7. **`skills/settle/scripts/rule_changes.py#parse` treats a heading near `## Rule changes` as another section** and names it in the parse result as one it did not read, so `chain_check.py` prints it and passes, and the settle's dry run lists the design among those to read whole. `skills/settle/SKILL.md` *Rule changes*' near-miss sentence changes in place.
8. **`.github/scripts/rules.py` reads `check:` lines in the one shape and names a near one** (`NEAR`'s match that is not the shape) as a line it did not read, at exit 0. `skills/settle/SKILL.md` *A rule has one shape* changes in place: the two near-miss bullets become one sentence on naming, and a target wrapped onto the next line is stated as not read, which is #1125's decision.
9. **`skills/verify/scripts/unverified_check.py` reads `closed` exactly and the no-change block exactly.** `NEAR_CLOSED` goes: a row whose first word is `closed` followed by punctuation is open, the safe direction. `NEAR_NOTHING`'s refusal becomes a report naming the line; a section with neither a table nor the block is refused as unreadable, as now. `LOOSE_HEADING`'s naming of a near `## Not verified` heading stays: it is the pattern this work asks of every reader.
10. **`skills/verify/scripts/deferral_check.py` reads no trigger.** `read_events`, `block_entries`, `continued`, `unquoted`, `ON_KEY`, `KEY`, `COMMENT`, `EVENT_NAME` and `PRE_MERGE_EVENTS` go. For each kind, the tool prints every workflow file and hook that holds a runner command, with the command line it read, and one line saying the trigger is the reader's to open; it exits 1 only where nothing holds a runner. `skills/verify/SKILL.md` *The answerer has to exist* names three outcomes in place of five and says the reader opens each named workflow for its trigger. The owner's two misreadings (a tab-indented block, a U+2028 inside a comment) close as moot.
11. **A judgment has a place, and the chain's sequences read as guidance.** `templates/records/sdd-plan.md` gains `## Judgments of the run`, a table `| Date | Judgment | Grounds | Judged against |` the orchestrator writes: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame. `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* keeps the verifying round and the check's facts and rewrites the cap as guidance: the signals that a run is not converging (a round finding as many as the one before, a regression, one kind of finding returning with a new instance, a fix that adds a mechanism), what going on costs (a round close to a finding round's price) and what stopping costs (each open finding its home), with three finding rounds since the last design change as the point where the orchestrator weighs rather than spawns, and the judgment written as a row of the table. *A regression is routed by comparing the fix with the frame* keeps its comparison table and makes the second regression on one unit a signal the orchestrator answers in the table rather than a route taken whatever the sentence says. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* says a folded decision's grounds go to the same table. `agents/crafter.md` step 8 and `templates/records/sdd-phase.md`'s placeholder say a decision in a phase record carries its grounds and the document it was judged against. The section headings keep their text; `skills/implement/acts.md`'s Grounds cells for the two sections are reread. The tests that pin the rewritten skill sentences change in the same commit.
12. **`seal settle`'s dry run prints *The judgments*.** For each released work item, the rows of `frame/plan.md` *Judgments of the run*, grouped by their `Judged against` cell, with the work item's round count beside each group, read through `hooks/lib/config.py#gfm_table`. A plan with no such section prints nothing for it. `skills/settle/SKILL.md` *What the dry run shows* and *The settling session's procedure* name the section and what the session does with it: where one kind of judgment recurs or keeps costing rounds, the section it stands on is rewritten in that settle.
13. **The policy root's changes are the `## Rule changes` below**, applied at the settle: the new document `docs/what-a-script-gates.md` holding Table A, its row in `docs/README.md`, and the sections of `docs/the-review-record.md`, `docs/the-pact.md`, `docs/the-record-layout.md`, `docs/the-agent-set.md` and `docs/release-checklist.md` this work changes.
14. **The release.** The work is a feature, `feat:` in the commit and pull request convention: a reading the settle did not have, readers that name instead of refuse, rules rewritten. Its release is 0.26.0, milestone 74, and the base is `release/v0.26.0`, cut at `f80f48e6`, the same commit as `release/v0.25.2`, with no pull request into it yet (executed, `gh api repos/:owner/:repo/milestones/74`, `git rev-parse origin/release/v0.26.0`, `gh pr list --base release/v0.26.0 --state all`, 2026-10-31). So phase 5's fragment commit moves `.claude-plugin/plugin.json` from `0.25.2` to `0.26.0` (`docs/branch-and-release.md` *The version is named at the cut*), and `changelog.md` opens with the feature under `### Added`, keeps `### Changed` for the rewritten rules and the readers, and holds one `### Process changes` row per change in the way of working.

Out.

- #1122 (the stamp queue and the guarantee arm read an unclosed fence differently): kept for 0.26.1 as filed. This work changes neither reader's fence handling; both read the verdict line through `chain_check.verdicts_of`, which item 5 changes, and the one-reader fix for `unclosed` is that issue's.
- #1126 (`seal settle --apply` removes a directory whose open rows sit in `trail/gaps.md`): kept for 0.26.1 with this frame's decision recorded in Table D: the script names a `gaps.md` it finds anywhere but at the directory's top as a file it did not read, and keeps nothing on a guess.
- #1128 (limit sentences for seven readers): kept for 0.26.1; the sentences stand on the rule item 1 writes.
- #1150 (`replay_targets.py` reads one layout and prints nothing): kept; its *Done when* already asks the tool to say so, which is item 1's rule.
- #1147, #1149, #1020: untouched, by the milestone's order. #1020's recurrence refusal is not built; the signal it would have read is guidance in item 11.
- The fix-pass threshold of 806,241 tokens (`skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter...*): read and kept. It names what each option costs and the measured reference it rests on, which is the shape item 11 asks for.
- *Orchestrator: the pull request opens once the sealer seals* and *the order inside a ticket*: sequences of the invariants in Table B, with no judgment in them, so they stay sequences.
- A YAML dependency for `seal deferrals`: weighed in `frame/plan.md` A6 and not taken.
- A test holding Table A against the tree: weighed in `frame/plan.md` A7 and not built.
- `pr_body.py` copying the judgments table into the pull request body: not changed; the orchestrator's part names the path where it needs the fact.
- The tests under `tests/text/` other than the two items 4 and 11 name: #1111 kept each phrase pin as a fact or removed it, and this work reopens none.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A round record carries a label in another spelling | Given a finding with `Verdict: open` and no `verdict:` line, when `chain_check.py` reads it, then the finding is refused as lacking its `verdict:` line and the `Verdict:` line is printed as not read, with the exit code the missing line alone gives | a case in `tests/skills/test_chain_check.py`, seen red against the near-miss refusal text |
| A record stands under another name | Given `trail/rounds/Round-2.md` beside a clean `round-1.md`, when the check runs, then one line names `Round-2.md` as not read and the exit code is unchanged | a case seen red at `f80f48e6`, where probe D printed nothing |
| A misspelt `original:` in a guarantee | Given a migration repository and `Original: <sha>` alone, when the guarantee arm runs, then the guarantee is refused as holding no `original:` line | a case seen red: today the line counts as present and the arm passes (#1121 R9) |
| An old spelling in a record | Given `refixes: round-1#2` in round 2 and nothing else naming round-1#2, when the check runs, then round 1's finding 2 is refused as unnamed by the next record and the `refixes:` line is printed as not read | a case seen red against the "another spelling" refusal |
| The grammar document loses its second table | Given `docs/the-review-record.md` *The round record* with the `Old spelling` table removed, when `chain_check.py` is imported, then it loads | a case constructing the document without the table |
| A pact anchor under a near header | Given `| pact | clause | hash |`, when `seal pact` runs, then the table is named at its line as not read with the exact header to write, no row of it is graded, and the exit code is 0 where nothing else refuses | a case in `tests/skills/test_pact_check.py`, seen red against the graded reading |
| A near `## Rule Changes` heading | Given a design with `## Rule Changes`, when `chain_check.py` and `seal settle` read it, then the check prints the heading as not read and passes, and the dry run lists the design among those to read whole | cases in `tests/skills/test_rule_changes.py` and `tests/skills/test_chain_check.py`, seen red against the refusal |
| A `Check:` line in a rule file | Given `Check: tests/x.py`, when `seal rules --check` runs, then the line is printed as not read and the exit code is 0 | a case in `tests/github/test_rules.py`, seen red against exit 1 |
| A `closed.` row | Given a `## Not verified` row opening `closed.`, when `seal unverified` reads it, then the row is open | a case seen red against the closed reading |
| A workflow with a trigger YAML refuses | Given a workflow whose `on:` block is indented by a tab and holds `pull_request:`, and a `run: pytest` step, when `seal deferrals` runs, then the output names the file with its runner line and says the trigger is the reader's to open, and no outcome names an event | a case in `tests/skills/test_deferral_check.py`, seen red against `resolves` |
| Nothing runs the suite | Given no workflow or hook holds a runner for `tests`, when `seal deferrals` runs, then it exits 1 and says nothing holds one | the existing case, kept |
| The orchestrator ends the rounds | Given round 3 found as many findings as round 2, when the orchestrator decides, then `frame/plan.md` *Judgments of the run* holds one row with the decision, the two counts as grounds and `docs/the-review-record.md` *The run* as the document | the proofer at review; a case holds the template's section |
| The settle reads the judgments | Given two released work items with rows under *Judgments of the run*, when `seal settle` runs, then the dry run prints *The judgments* grouped by the `Judged against` cell with each work item's round count | a case in `tests/skills/test_settle.py`, seen red |
| A session reads the core | Given `skills/core/SKILL.md`, when a party opens *Judgment is not licence to skip a party*, then each invariant stands in one row with what it protects and the mechanism that holds it, and every mechanism named is a file of the tree | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and the proofer |

## Data & interfaces

### Table A. Every check that gates, with what it reads

Table A is the table under *The checks* in the `add` item for `docs/what-a-script-gates.md` in `## Rule changes` below, and it stands there once: that text is what the settle writes, and a second copy here would be two tables for a reviewer to compare (`skills/core/SKILL.md` *The rule a mechanism is kept against*: "Less text means nothing said twice"). Every "Table A" in this frame names that one. The issue numbers its rows rest on, kept out of the policy text: the `hooks/mode-gate.py` row's stated limit is #1128's R18; the `seal rules --check` row's wrapped target is #1125; the row on the cases that read prose is #1111 and Scope item 4; the stamp row's fence is #1122's.

### Table B. The invariants, in the core

| Invariant | What it protects | Held by |
|---|---|---|
| The routing answer comes before the first edit, and no question to a person follows it | a person is asked once, before the first edit, and nothing stops to ask afterwards | `hooks/routing-edit-gate.py` refuses the first edit on an undeclared branch; `hooks/question-gate.py` refuses the question tool under `Automation` `yes` |
| No review without a build | a round reads a committed tree and its record names the commit | `chain_check.py`'s records arm: `target:` and every `fixed` commit are commits the branch holds |
| No fix that no round reads | every change after the last round is read by a round, or by the sealer where it touched the work item's records alone | `chain_check.py`: the last record is at HEAD or only the work item's records follow it, and every `fixed` or `rejected` finding is named by the next record |
| No seal without the broad run at HEAD | the sealer guarantees a tree the repository's `Broad gate` row in `seal/config.md` passed at HEAD | `agents/sealer.md` step 1 withholds without `trail/gate.md` at HEAD; `chain_check.py`'s broad gate arm |

The rows go into the core as written, with `chain_check.py` spelt by its path in the first row that names it and "the same check" after; the core is shipped to every repository, so the fourth row names the `Broad gate` row by its coordinate and no tool, since what the row runs is each repository's own (this one's runs ruff and `bin/test`, and no typecheck).
| No pull request without a seal | nothing reaches the base that the last independent party did not guarantee | `chain_check.py`'s guarantee arm: a ready pull request fails without `Verdict: sealed` at HEAD |

### Table C. Where each party's judgment stands

| Party | The place, today | This work |
|---|---|---|
| framer | `frame/design.md` *Grounding*; `frame/plan.md` *Alternatives considered* | unchanged |
| crafter | `trail/phases/phase-N.md` *What this phase found* | the placeholder and `agents/crafter.md` step 8 say a decision carries its grounds and the document it was judged against |
| proofer | a finding's grounds and its `evidence:` line; `## Not judged` | unchanged |
| sealer | `guarantee.md` *The parties* and the verdict line | unchanged |
| orchestrator | `routing.md` *Why this way* for the routing; nothing for the run | `frame/plan.md` *Judgments of the run*, read by the settle |

The table's shape:

```markdown
## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| <date> | <a round spawned past the default or the run ended; a regression's route; a leftover's home; a decision folded into the frame> | <what was weighed, in one or two sentences> | <the backticked path and the italic heading of the document the judgment stands on> |
```

### Table D. The ten issues of milestone 75 against this result

| Issue | What the frame decides | Where |
|---|---|---|
| #1170 | Built here: the writing-style sentence changes in the commit that changes the readers it described | Scope item 2 |
| #1121 | Built here: R9 and R11 by item 5; R3 by the limit sentence in `## Rule changes` (*What the check reads at the pull request*): a whole finding inside a fence is no finding, and the orchestrator's read before the commit catches it | Scope item 5 |
| #1125 | Decided here: a wrapped target is not read, stated in `skills/settle/SKILL.md` *A rule has one shape*; no grammar for the continuation line | Scope item 8 |
| #1122 | Kept for 0.26.1 as filed; this work changes the verdict reader both share and not the fence reading | Out |
| #1126 | Kept for 0.26.1; the fix is naming the `gaps.md` the script did not read, not keeping the directory on a guess | Out |
| #1128 | Kept for 0.26.1; the limit sentences stand on item 1's rule | Out |
| #1150 | Kept for 0.26.1; its *Done when* is item 1's rule applied to an evals script | Out |
| #1149 | Kept for 0.26.1; item 3's bullet is about reading, that issue's about removal, in the same list | Out |
| #1147 | Kept for 0.26.1 | Out |
| #1020 | Kept for 0.26.1, last; the recurrence signal is guidance in item 11, and no check reads it | Out |

The closing of #1170, #1121 and #1125 is the orchestrator's act in the pull request body, by `Closes` lines (`.github/scripts/issue_claims_check.py`: one number per keyword).

## Rule changes

- change
  file: docs/the-review-record.md
  section: The round record
  from: **The record's grammar is the two tables below, and nothing else states it.**
  to: **The record's grammar is the table below, and nothing else states it.**
- change
  file: docs/the-review-record.md
  section: The round record
  from: A line that means a label and is spelt another way, in another case, under emphasis, with a space before the colon, or as an old spelling the second table names, is refused at its line as the label its `Means` cell names, and the finding carrying it is not read past it. So a finding holding both spellings does not pass on the lowercase one.
  to: A line spelt otherwise, in another case, under emphasis or with a space before the colon, is prose to the check, and the check names it at its line as one it did not read, which changes no exit code. A finding that then lacks a line the table says is `one` is refused as lacking it. An optional line spelt otherwise does what prose does, so a `reopens:` or `regression:` line the check did not read leaves the finding it meant to name unnamed in the next record, which is refused at that finding's heading. Whether the line meant the label is the orchestrator's reading at the preflight and the sealer's at the records, never the check's, and no table of spellings stands beside the grammar: a list of the ways a label is written grows by one row for every near miss a round finds and never converges (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*).
- remove
  file: docs/the-review-record.md
  section: The round record
  from: | Old spelling | Means |
    |---|---|
    | `Target SHA:` | `target:` |
    | `refixes:` | `regression:` |
    | `fix of a fix:` | `regression:` |
- change
  file: docs/the-review-record.md
  section: The round record
  from: **`chain_check.py` reads the two tables from this section and stops at exit 2 where it cannot.** It loads them once, when it is imported, from `docs/the-review-record.md` beside itself, which every copy of the plugin carries, the hygiene workflow's clone among them. It finds each table by this section's heading and the table's header row.
  to: **`chain_check.py` reads the table from this section and stops at exit 2 where it cannot.** It loads it once, when it is imported, from `docs/the-review-record.md` beside itself, which every copy of the plugin carries, the hygiene workflow's clone among them. It finds the table by this section's heading and its header row.
- remove
  file: docs/the-review-record.md
  section: The round record
  from: An old spelling's row it cannot read is one whose cell is not one code span, whose `Means` is no label of the first table, whose `Old spelling` is one, or which names a spelling a row above it names.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: It reads every line *The round record*'s table has a row for, and a ready pull request fails for any line that table refuses.
  to: It reads every line *The round record*'s table has a row for, and a ready pull request fails for any line that table refuses. It names each file under `trail/rounds/` whose name is no `round-N.md` as one it did not read, so a record under another name is a line of the check's output and never a silent pass, and it names each line outside a fence that opens like a label and is not one.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: A labelled line inside a fence is not a line, so a finding whose only verdict stands in its fix block has none, and a fence that never closes, which would hide every finding after it, is refused at the line that opened it.
  to: A labelled line inside a fence is not a line, so a finding whose only verdict stands in its fix block has none, and a whole finding written inside a closed fence is no finding: a fenced block is the paste-ready fix by the template, and the orchestrator's read of the record before its commit, against the template, is what catches a finding written there. A fence that never closes, which would hide every finding after it, is refused at the line that opened it.
- change
  file: docs/the-review-record.md
  section: The run
  from: **A run has three finding rounds by default, counted from the last design change, and extends one round at a time while the findings shrink.**
  to: **The orchestrator ends the rounds when they stop paying, and a run has three finding rounds by default, counted from the last design change, as the point where it weighs that rather than spawning the next round by habit.** A design change is a reframe, or a new phase the owner approved in `frame/plan.md`, so the first finding round that reviews new work starts the count again at one, whatever the record's number. The signals that a run is not converging: a round finds as many findings as the one before it or more; a finding carries a `regression:` line; one kind of finding returns with a new instance, each fix pass fixing the coordinate it was handed; a fix adds a mechanism, a check, a mark or a grammar rule, in place of removing a cause. Going on costs a round close to a finding round's price, since the frame, the inherited records and the probes set it. Stopping costs each open finding its home, by the table below, and a defect the release ships where the home is nobody's. A round that opens nothing needing a fix is the loop having converged and counts toward nothing. A regression's fix pass is followed by one verifying round whatever the count, because a fix nobody read is the invariant Table B of the core holds. The orchestrator writes each decision to go on past the third round, or to stop, as one row of `frame/plan.md` *Judgments of the run*, with the counts it weighed and this section as the document; the proofer writes no line for it. No person is asked mid-run.
    check: tests/text/test_the_rules_have_one_owner.py
- remove
  file: docs/the-review-record.md
  section: The run
  from: Past the third round of the count the orchestrator spawns one more finding round only while the latest round found fewer findings than the one before it and none of them is a regression. A regression routed to a fix pass is followed by one verifying round, whatever the count, which reads that fix and is not an extension. A second regression it finds on the same unit goes to the framer, as the next paragraph says, and anything else it leaves open past the cap takes the ladder. Each extension is one line in that round's record, written by the proofer from the reason the spawn prompt gives:
- remove
  file: docs/the-review-record.md
  section: The run
  from: Extended past round 3, counting from round 1: round 3 found 2, round 2 found 4, and none is a regression.
- change
  file: docs/the-review-record.md
  section: The run
  from: At the cap every finding still open takes the filing ladder below and reads `deferred <home>`. No person is asked mid-run.
  to: When the orchestrator stops, every finding still open takes a home from the table below and reads `deferred <home>`.
- change
  file: docs/the-review-record.md
  section: The run
  from: A second regression on the same unit after a fix-pass route goes to the framer whatever the comparison says.
  to: A second regression on the same unit after a fix-pass route is the signal that the frame is wrong whatever the sentence reads, and the orchestrator routes it to the framer unless it can write, as the row's grounds in `frame/plan.md` *Judgments of the run*, why the frame holds and the fix alone was wrong.
- change
  file: docs/the-review-record.md
  section: The run
  from: **A leftover finding takes the first rung that fits.** A new issue is the third rung, not the default:
  to: **A leftover finding goes where somebody will act on it, and the orchestrator writes why there.** The homes, with when each fits, are the rows below; the cheapest home that reaches a party who agreed to act is the one to take, a new issue is not the default, and the row the orchestrator writes in `frame/plan.md` *Judgments of the run* names the home and the party:
- add
  file: docs/the-review-record.md
  section: The run
  to: **The orchestrator's judgments of a run are rows of `frame/plan.md` *Judgments of the run*, each with its grounds and the document it stands on.** The decisions this section leaves to the orchestrator, to go on past the third round or to stop, a regression's route, a leftover's home, and a decision folded into the frame after the frame was committed, are judgments and not sequences, and `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* asks that each be written where the next session reads it. The settle's dry run prints the rows of every released work item grouped by the document they stand on, and the settling session rewrites the section where one kind of judgment keeps costing rounds. The framer's judgments stand in its *Alternatives considered* and the proofer's in its findings, and neither is copied here.
    check: none reader: the settling session, at the dry run's judgments
- change
  file: docs/the-review-record.md
  section: The guarantee
  from: and with no emphasis. Any other spelling of the line is refused at it.
  to: and with no emphasis. A line that opens like the label and is not it is prose, named by the check as one it did not read, and a guarantee with no `Verdict:` line, or with two, is refused naming the file.
- change
  file: docs/the-pact.md
  section: The pact anchor
  from: **The anchor table is the table whose header means `| Pact | Clause | Hash |`, and one closed normalisation decides that.**
  to: **The anchor table is the table whose header is `| Pact | Clause | Hash |`, cell for cell, and a table whose header is near it is named and not read.** A header whose cells, case folded and with one emphasis run removed, are those words is the near one: `seal pact` names it at its line, with the exact header to write, grades no row of it and refuses nothing for it. Whether `| pact | clause | hash |` meant the anchor table is the judgment of the person reading the report and of the proofer reading the frame, never the tool's, so the tool carries no normalisation of the header (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*). The template writes the exact header. A code span is a mention of the word rather than a use, strikethrough marks it deleted, and a plural, another word, another order or another width is another table. A second exact header is refused as a second anchor table.
    check: tests/skills/test_pact_check.py
- remove
  file: docs/the-pact.md
  section: The pact anchor
  from: Each header cell is compared case folded, after one emphasis run is removed where it wraps the whole cell: `*` or `_`, one to three long, the same run on both sides and no space just inside it. So `| pact | clause | hash |` and `| **Pact** | Clause | Hash |` head the anchor table, and its rows are graded and refused as the exact header's are. GitHub renders a header cell bold, and the same letters in another case are the same word, so a script that answered that these differ would report a signer citing nothing where it cites a clause. Nothing else is in the normalisation. A code span is a mention of the word rather than a use, strikethrough marks it deleted, and a plural, another word, another order or another width is another table. A second header the normalisation reads is refused as a second anchor table.
- change
  file: docs/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: | `frame/plan.md` | in which phases it is built, how each is shown, and the approval line |
  to: | `frame/plan.md` | in which phases it is built, how each is shown, which approach was chosen over which, and the judgments the orchestrator made in the run, each with its grounds and the document it stands on |
- add
  file: docs/the-agent-set.md
  section: What each party writes, and when
  to: **A judgment is written where its party writes, with its grounds and the document it stands on, and the orchestrator's go to `frame/plan.md` *Judgments of the run*.** The framer's stand in `frame/design.md` *Grounding* and `frame/plan.md` *Alternatives considered*; the crafter's in the phase record's *What this phase found*, each decision with its grounds and the document; the proofer's as a finding's grounds and `evidence:` line; the sealer's in `guarantee.md` *The parties*. The orchestrator has no record of its own, and a judgment it made in the run, to go on or stop, to route a regression, to file a leftover, to fold a decision into the frame, reached the next session only through a spawn prompt or memory, so it writes each as one row of the plan's table, which the settle reads (`docs/the-review-record.md` *The run*).
    check: none reader: the settling session, at the dry run's judgments
- add
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  to: **Before `seal settle --apply`, the settling session reads the dry run's *The judgments*, the orchestrators' rows from every released `frame/plan.md` grouped by the document each stands on, and rewrites a section where one kind of judgment recurs across work items or kept costing rounds.** The rows leave with their directories at `--apply`, so this is the one reading they get; `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* says the guidance improves from that record and not from memory.
    check: none reader: the owner's settling session, at this step
- add
  file: docs/README.md
  section: The checks
  to: | `docs/what-a-script-gates.md` | which gates a script holds and which an agent holds, what each script reads, and what it does with what it did not read |
- add
  file: docs/what-a-script-gates.md
  to: # What a script gates, and what an agent judges

    A script holds a gate only on a fact it reads exactly, an agent holds the
    gates on meaning, and every check that gates is listed here with what it
    reads and what it does with what it did not read. The rule is
    `skills/core/SKILL.md` *Judgment is spent where meaning is the question,
    and a script answers the rest* and *The rule a mechanism is kept against*;
    this document is the standing account of its application.

    ## Which gate a script holds

    **A script gates a closed form, in one spelling, and names what it did not
    read; a judgment of meaning belongs to the agent that already reads the
    text, at a named step.** A closed form is an exit code, a real parser's
    result, a structure a command wrote, or a line of the plugin's own forms
    in the one spelling the form gives it, such as `verdict:` at the start of
    a line or the header `| Pact | Clause | Hash |`. A line spelt otherwise is
    prose to the script: where the form requires the line, its absence is
    refused; where it does not, the line is named as one the script did not
    read, and whether it meant the label is the reading agent's judgment. No
    script carries a list of the spellings a label is written in, because such
    a list grows by one row for each near miss a review round finds and never
    converges. What a script answers exactly stays a script and the session
    waits on its exit code. A check added or changed names, in its pull
    request, the form it reads, what it names as unread, and the agent and
    step that judge the meaning of the same text.
    check: tests/skills/test_chain_check.py tests/skills/test_pact_check.py tests/github/test_rules.py tests/skills/test_rule_changes.py

    ## The checks

    The table reads: "Runs at" is the moment the check decides; "Unread" is
    what it does with what it cannot read; "Agent" is the judgment of meaning
    left to a party on the same text.

    | Check | Runs at | Reads | Unread | Agent |
    |---|---|---|---|---|
    | `hooks/routing-edit-gate.py` | every `Write`, `Edit`, `NotebookEdit` | `routing.md`'s rows for the checked-out branch through `hooks/lib/routing.py`; the `seal no-work-item` record | refuses the edit while no declaration it can read names the branch | none; the routing answer is the person's |
    | `hooks/question-gate.py` | every `AskUserQuestion` | the `Automation` row | a declaration it cannot read is the attended answer: silence | none |
    | `hooks/mode-gate.py` | the session's commands | `config.md`'s `Mode` row | a table it cannot read is silence, a stated limit | none |
    | `hooks/review-skill-gate.py` | a `Skill` call naming a review | the skill's name | nothing to read otherwise | the person picks the review |
    | `hooks/sealer-stamp-queue.py`, `hooks/sealer-stamp.py` | the write of `guarantee.md`; the turn's end | the one `Verdict:` line, through `chain_check.verdicts_of` | queues nothing where the file holds no one `Verdict: sealed`; a line spelt otherwise is named by the check | the verdict is the sealer's |
    | `hooks/lint-python.py` | the write of a `.py` in a repository with a ruff config | ruff's exit code and output | nothing | none |
    | `skills/code-review/scripts/chain_check.py`, as hygiene's chain step and `seal gate`'s arm 2 | the pull request; the preflight and the broad run | routing rows; the frame's mark; `## Rule changes` through `rule_changes.py`; the round records' labelled lines in one spelling each; `trail/gate.md`; `guarantee.md`'s rows and verdict line; the branch's commits and `Seal-Routing` trailers; `seal/parity.md`'s `Baseline commit` | refuses at its line a required line it cannot read; names each file under `trail/rounds/` it did not read and each line that opens like a label and is not one; a line spelt otherwise is prose | whether a fix holds: the verifying round; whether the parties agree: the sealer; what a named unread line meant: the orchestrator at the preflight |
    | `seal gate`'s `Broad gate` row and arm 3 | the orchestrator's one run | the row's command's exit code; the gate's pytest recorder; the `Mode` row | refuses at exit 2 a row it would not run as the command it reads as, which goes to a person | none; `new`, `failing on base too` and `new?` are reported and the orchestrator acts |
    | hygiene's other steps: `issue_claims_check.py`, the version step, `release_completeness_check.py`, the mode step, the READMEs step | the pull request | the body's closing keywords by GitHub's own grammar; `plugin.json`; the milestone through `gh`; commit subjects' `(#N)`; two files | the body is reported at exit 0, never failed; the rest refuse on the fact read | none |
    | `ruff check`, `ruff format --check`, `pytest` | CI and the broad run | code | a real tool's own | none |
    | `seal rules --check`, through `tests/github/test_rules.py` | the suite | `check:` lines in the one shape | names a near line as not read; a target it cannot resolve is refused; a target wrapped onto the next line is not read | whether a target enforces its rule: review |
    | `seal layout --check`, `seal arms`, `seal mutate` | the crafter; the suite | test files and modules through `ast` | refuses on the tree | none |
    | `seal unverified` | the settle; a session | `## Not verified` rows and the no-change block | fails on a section it cannot read, never on an open row; names a near heading and a near block | none |
    | `seal settle`, `skills/settle/scripts/rule_changes.py` | the owner | `## Rule changes`, open rows, `frame/plan.md` *Judgments of the run* | a section that does not parse is refused at its line at the pull request and read whole at the settle; a near heading is named and is another section | the settling session writes the latest decision |
    | `seal pact` | a person, at the pact's repository | the anchor table under the exact header, through `gfm_table` | refuses at exit 2 a row it cannot grade; names a table under a near header and grades none of it | the proofer: a line meant as an anchor that the tool did not read is a finding |
    | `seal deferrals` | a session, before it writes an `unverified` row | the command lines of workflows and hooks that run a kind of check | names each workflow holding a runner for the reader to open; reads no trigger | whether the workflow runs on pull requests: the agent that opens it |
    | `seal pr-body --check` | the sealer | the body file against the records | withholds | none |
    | the cases under `tests/text/` and `tests/behaviour/` that read prose | the suite | a sentence, a citation, a heading | a case pins a fact a reader acts on; one that pins wording goes | the proofer reads prose for meaning |
    | `seal fold`, `seal core` | the owner at the settle; the orchestrator | document sizes and the index; the transcript's first core line | reports; `seal fold` refuses a document the index does not name | none |

    **How this table is kept true.** No case holds it against the tree. Each
    row names a script that has its own tests and its own home sentence, so a
    row that drifts is found when that script's home is read, and the settle
    reads this document against the code as it reads every policy document.
    A test that held the table from both sides would be a mechanism with no
    catch to its name on the day it was added, and
    `skills/core/SKILL.md` *The rule a mechanism is kept against* is why it is
    not built.
    check: none reader: the settling session, and the proofer at a change to a gate

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `Old spelling` table and the loader that reads it (`OLD_COLUMNS`, `old_spelling`, `OLD_SPELLINGS`) | `docs/the-review-record.md` *The round record*, the second table (`## Rule changes`); `skills/code-review/scripts/chain_check.py:180`, `:367-386`, `:429`, `:517`, `:531`, `:1002` | the old spellings are the labels records carried before 0.22.x renamed them; every work item that wrote them is settled and gone, and no record under `seal/threads/` carries one (executed, `grep -rln`). A report needs no list: the near-miss net is derived from the one table's labels. |
| The near-miss refusal of a labelled line (`misspelt`, `spelt_otherwise`, `MEANT` and `SPELT` in their refusing role) | `chain_check.py:528-540`, `:995-1002`, `:1102-1109`, and their use in `findings` | the same lines become a report, `path:line  not read: <why>`, that changes no exit code; a required line's absence is refused by the count rule, which probe A shows standing |
| `original_of` counting a line spelt otherwise as present | `chain_check.py:1820-1844` | the exact label alone counts; a misspelt line is absent and refused where owed (#1121 R9) |
| `MEANT_VERDICT`'s loose reading of the guarantee's verdict line in `verdicts_of` | `chain_check.py:139`, `:1912-1925` | `Verdict:` at the start of a line, exactly; a line that opens like it is named as not read; `seal_stamp.py` reads through the same function and changes nothing |
| `header_key`'s normalisation of the anchor table's header | `skills/verify/scripts/pact_check.py:300` and `first_table`'s `key` argument (`:319`) | the exact header is read; the normalisation stays only as the net that names a near header, and grades nothing |
| The near-miss refusal of a heading near `## Rule changes` | `skills/settle/scripts/rule_changes.py:86-106`; `skills/settle/SKILL.md` *Rule changes*, the bullet "is a near miss: it is refused at its line" | the heading is another section and is named in the parse result; the design is read whole at the settle, which is the stated path for a design with no such section |
| `NEAR`'s refusal of a near `check:` line | `.github/scripts/rules.py:72-78`, `:147-156`; `skills/settle/SKILL.md` *A rule has one shape*, the bullets "A line whose only content before the label is Markdown block markup or emphasis is a near miss and is refused at its line" and "Every other spelling of the label is refused at its line too" | the line is named as not read at exit 0; the proofer reads rule files |
| `NEAR_CLOSED`'s reading of `closed` followed by punctuation as closed | `skills/verify/scripts/unverified_check.py:156`, `:807` | the row is open, the safe direction; the settling session closes it in the one spelling |
| `NEAR_NOTHING`'s refusal of a near no-change block | `unverified_check.py:153`, `:687`, `:717` | the line is named; a section with neither a table nor the block is refused as unreadable, as now |
| The trigger reading of `seal deferrals` (`read_events`, `block_entries`, `continued`, `unquoted`, `ON_KEY`, `KEY`, `COMMENT`, `EVENT_NAME`, `PRE_MERGE_EVENTS`) and the outcomes `too late` and `wrong trigger` | `skills/verify/scripts/deferral_check.py:81-230`, `:291-345`; `skills/verify/SKILL.md` *The answerer has to exist*, the five outcomes and the sentence "It reads an event's name and not its filters" | the tool names each workflow holding a runner and says the trigger is the reader's; the agent that opens the file judges whether it runs on pull requests. Its catch, a push-only workflow answering a deferral, is still caught: the reader sees `on: push` in the file the tool named. The two misreadings the owner deferred (a tab-indented block, a U+2028 in a comment) go with the scan. |
| The extension line the proofer writes from the spawn prompt's reason | `docs/the-review-record.md` *The run*, the code block and the sentence "Each extension is one line in that round's record" (`## Rule changes`); `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, where it names the line | the orchestrator's row in `frame/plan.md` *Judgments of the run*; the line was written in no round record (executed, 0 under `seal/threads/`) |
| The hard route "A second regression on the same unit after a fix-pass route goes to the framer whatever the comparison says" | `docs/the-review-record.md` *The run* (`## Rule changes`); `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, the table's third row | a signal the orchestrator answers in the judgments table, with the framer as the route unless it writes why the frame holds |
| "A leftover finding takes the first rung that fits" as an order of rungs | `docs/the-review-record.md` *The run* (`## Rule changes`) | the homes with when each fits and what each costs; the orchestrator writes the home and the party in the judgments table |
| The sentence "검사가 읽는 줄은 정해진 철자 하나만 읽히고 조금 틀린 철자는 그 줄에서 거절되어야 한다. 조금 틀린 철자를 말없이 지나치는 검사는 그 줄을 읽지 않은 것과 같다." | `skills/writing-style/SKILL.md:264-267` | rewritten in place to the core's rule (Scope item 2); it stood on the refusals this work removes |

Framed 2026-10-31 by framer, before the build.
