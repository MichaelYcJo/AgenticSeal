# Feature Specification: every agent, skill and doc states the current rule only

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | A mechanism stays only while its history shows what it caught against what it costs; a fact has one source; a change rewrites in place and removes what stood on the old fact. Every mechanism this frame keeps is weighed by it, and the frame's own first version lost three to it (`plan.md` §*Alternatives considered* B, C, J) |
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. A raise is a `Budget raised:` body line CI reads; a rewrite is proved not worse by a run nobody scores by hand |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The widened `history` row is a gate change: its case seen red, its failure direction (it blocks more), a prompt budget of zero, a `Reads:` line per unit, and `## Removes` below |
| `docs/the-record-layout.md` §*Every kind of record, at a glance*, §*The size a reader takes whole* | A rule has one home and the copy is the defect; a file a reader takes whole is ≤ 1,000 lines. This work adds the stricter bound a preload is held to: the bytes its rewrite reached |
| `docs/the-agent-set.md` §*One contract every agent receives, and one definition each*, §*What a spawn costs* | A definition keeps only its own application of a contract section; §1–§17 are never reused or re-ordered, so the rewrite keeps them as headings; a spawn's payload is paid on every spawn |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; a removal a phase makes that it does not name is an `overview.md` divergence |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The work alters what every spawn reads, which is the top rung |
| `tests/test_a_moved_rule_leaves_its_definition.py`, `tests/test_no_passage_is_pasted_into_a_second_file.py`, `tests/test_the_agent_contract_holds_the_universal_rules.py`, `tests/test_every_agent_reads_the_contract.py` | A definition may cite a contract section and say what it means for its role, never carry its sentences; a drained pair lowers its `BASELINE` entry in the same change; the contract's sections each keep one pinned phrase and the opening paragraph of every definition names the contract |
| #923's body, rewritten 2026-10-15 by the owner, and the owner's correction of 2026-10-15 relayed by the orchestrator | The one source for what was decided: the principle, the five things the item builds, the rules the rewrite states in place, the two axes of the proof. The correction: a definition IS a `CLAUDE.md`; a restated or stale rule is a defect that pulls behaviour off course, not a cost; the improvement comes first and the proof stays smaller than the rewrite it proves |

## What a definition is, and what the defect is

An agent definition and the skills its `skills:` list injects are the instruction set the model acts on — a `CLAUDE.md` for one role, written into every spawn's context before its first tool call. Three things in such a file are defects in their own right, before any token is counted:

- **A rule stated twice in different words.** The agent receives two instructions for one act and has to reconcile them; where they differ by a nuance, it follows one and is wrong by the other. Measured below: a warden spawn carries four such pairs inside its own context, a smith spawn four, a framer two.
- **A concept that no longer exists.** A rule about a thing the tree removed is a rule the agent tries to apply to nothing, or applies to the nearest thing it can find. Measured below: the preload set names nothing #944 removed, so this class is empty today; the check in §*How the check holds it* is what keeps it empty.
- **Narrative under a rule.** What a rule used to say, which round found it, what was measured — the agent reads it as instruction, because nothing marks it as story. Measured below: 805 of the 1,693 lines a warden spawn reads sit in paragraphs that open with no rule.

Removing these is expected to improve what an agent does, and the proof below reads outcome first for that reason. The byte and token figures are the cost axis and the second reason.

## The problem, measured

`executed` on this branch at 9e23de25 (= `origin/release/v0.22.0` at 5b1f6fae, the tree after #930 and #944 merged, plus this item's frame and phase 2) with `measure.py` in the frame's scratchpad: `budget_check.classify` and `rule_paragraphs` over each file, `payload_meter.py --agent <a> --json`, a paragraph census, Jaccard over paragraphs of ≥ 12 content words, `ast` string literals ≥ 25 characters of `tests/*.py` found verbatim in a file, `gh pr diff` of the open pull requests.

| What | Value |
|---|---|
| The preload set | 10 files: `agents/{warden,smith,framer,sealer,scribe}.md`, `skills/{agent-contract,code-review,implement,writing-style,legacy-parity}/SKILL.md` |
| Per file — bytes · lines · history lines (#930's marks) · rule paragraphs · lines in paragraphs opening with no rule | `agents/warden.md` 32,121 · 562 · 19 · 24 · 338 — `agents/smith.md` 25,400 · 402 · 12 · 19 · 191 — `agents/framer.md` 19,700 · 368 · 11 · 35 · 145 — `agents/sealer.md` 15,189 · 269 · 0 · 21 · 47 — `agents/scribe.md` 3,763 · 71 · 0 · 3 · 53 — `skills/agent-contract/SKILL.md` 20,409 · 369 · 9 · 2 · 271 — `skills/code-review/SKILL.md` 26,150 · 440 · 6 · 27 · 142 — `skills/implement/SKILL.md` 34,330 · 578 · 4 · 26 · 245 — `skills/writing-style/SKILL.md` 21,000 · 322 · 1 · 40 · 54 — `skills/legacy-parity/SKILL.md` 5,325 · 117 · 0 · 2 · 54 |
| What one spawn preloads, agent share — bytes · lines · history lines · lines in no-rule paragraphs | warden 99,680 · 1,693 · 35 · 805 — smith 101,139 · 1,671 · 26 · 761 — framer 95,439 · 1,637 · 25 · 715 — sealer 35,598 · 638 · 9 · 318 — scribe 29,497 · 557 · 9 · 378. Every prefix also carries `CLAUDE.md` 9,008 B and `~/.claude/CLAUDE.md` 8,139 B, the harness's share |
| Tokens per spawn, estimated | `payload_meter` at its assumed 3.2 B/token, nothing calibrated: warden 36,508 (31,150 agent share) · smith 36,964 · framer 35,182 · sealer 16,483 · scribe 14,576. The previous frame's fit over 185 real spawns was 2.79 B/token above a 39,249-token harness share (`read` from that frame; the transcripts were not re-read). The baseline's traces carry each run's real `usage`, which is what the proof reads (Q2) |
| `Enforced by:` in the preload set | 0 of 199 rule paragraphs name an enforcer; `seal/budgets.md`'s `unenforced` rows hold each file at that count (warden 24, smith 19, framer 35, sealer 21, scribe 3, contract 2, code-review 27, implement 26, writing-style 40, legacy-parity 2). A rule a rewrite gives its test lowers the row in the same pull request — #944's mechanism, reused |
| A rule the agent receives twice in one context (Jaccard ≥ 0.35 between paragraphs of two files one spawn preloads) | warden: `agents/warden.md:144` ↔ `skills/code-review/SKILL.md:286` (one depth per finding, 0.71) · `:236` ↔ `:335` (a bare marker in `#`, 0.58) · `:245` ↔ `:301` (an unnumbered 🔴/🟡 is refused, 0.54) · `:252` ↔ `:308` (an `open` verdict cell is refused, 0.44). smith: `agents/smith.md:190` ↔ `skills/implement/SKILL.md:506` (a fix pass hands over a fix table, 0.51) · `:350` ↔ `:234` (what is unresolved is handed over, 0.35) · `skills/agent-contract/SKILL.md:217` ↔ `skills/implement/SKILL.md:294` (an edit must be able to fail, 0.55) · `:323` ↔ `:103` (where `seal/` resolves, 0.41). framer: the contract ↔ implement pair, both. Across spawns: `agents/framer.md:129` ↔ `agents/sealer.md:227` (§6's four withheld acts, 0.52); `skills/code-review/SKILL.md:29,35,46,176` ↔ `skills/implement/SKILL.md:38,45,74,130` (the orchestrator-file preamble and the records' history, 0.37–0.47). The 10 pairs at 1.0 are the definitions' identical opening paragraph, pinned on purpose by `test_every_agent_reads_the_contract.py` |
| Stale concepts | 0 lines of the preload set name the ledger, `evidence-check`, `survivor-check`, `--reverify` or `evidence-todo.md`. `tests-todo.md` (4 lines) is live: `hooks/review-history-guard.py` and three `docs/` files read it |
| Narrative the marks miss | `skills/code-review/SKILL.md:176–180` (where the records used to live), `agents/warden.md` §*Role* and §*Report* stories (the five rows under `## Removes`), `skills/agent-contract/SKILL.md` §2, §6, §7, §9 stories (four rows below). None carries a #930 mark on every line, which is why the ceiling is review's bar as well as the checker's |
| Test pins — modules · literals found verbatim | `agents/warden.md` 40 · 88 — `agents/smith.md` 47 · 77 — `agents/framer.md` 16 · 38 — `agents/sealer.md` 20 · 40 — `agents/scribe.md` 2 · 3 — contract 20 · 65 (`test_the_agent_contract_holds_the_universal_rules.py` 20 alone) — code-review 38 · 68 — implement 55 · 117 — writing-style 2 · 3 — legacy-parity 1 · 1 |
| `BASELINE` pairs the verbatim ratchet holds in the set | warden–smith 153 · warden–code-review 53 · smith–implement 46 · warden–round-record-spec 36 · code-review–sdd-round 30; every definition pair 65–72 (the shared opening paragraph) |
| The suite phase 2 built, as it stands | 20 behaviour cases: warden 9 (4 replay, 4 seeded, 1 fixture with 13 `rule-` graders), smith 4 × 10 `rule-` graders, framer 4 × 14, sealer 3 × 11 — 149 sentence graders in all; every warden case also carries 1 `reach-`, 4 `shape-` and 1–2 `truth-` graders. `replay_targets.py --list` finds 25 rounds with confirmed truths on this tree, `seed_defects.py --list` 14 seedable diffs. Three replay truths and one seeded case cite the ledger or `survivor_check.py` (`replay-1791384160-r2/truth-1`, `replay-1791779434-r5/truth-1`, `replay-1791852615-r2/truth-6`, `seeded-770d721f`). The runner records no cost: `noninferiority.py` carries `--max-cost-usd` and nothing that reads a run's spend, tokens or seconds |
| What phase 2 measured of the runner (`read` from `phases/phase-2.md`) | one warden replay run ≈ $2.5 and 300–500 s; smith 8 runs in 3.5 min; sealer 6 runs in 47 s; the command runs on the owner's account and a case reaches `specseal:<agent>` through the `Agent` tool; a side's JSON and traces are saved under `<out>.raw/` before anything reads them |
| Open pull requests touching the set | #915 adds a six-line rule paragraph to `agents/warden.md` §*Role* (`Reads:` lines are claims); #939 (#929) rewords two sentences of `agents/sealer.md` and one of `skills/code-review/orchestration.md`; #937 (#931) touches nothing in the set |
| The model-pin sentence | `skills/code-review/orchestration.md:438–440` (*the model is a spawn-time argument … which `agents/*.md` pins nowhere*), `docs/review-handoff-protocol.md:468` and `docs/round-record-spec.md:763` (*agent definitions pin no model*). No `agents/*.md` carries `model:` today |

## The shape of a compact file

A file an agent reads holds rules, formats and links, and nothing that narrates.

1. **A rule is one paragraph.** It opens with the rule in bold, in one or two sentences; a list item whose text opens bold is a rule paragraph too. It holds at most one sentence of why. It ends with what identifies it: `Enforced by: <test node ids>` where a test holds it, and otherwise one link — a `docs/*.md §*heading*`, an issue, or a work item's record at its release tag. Eight live lines is the bar review holds a paragraph to; one needing more is two rules, or a rule and a story.
2. **A format is a fence or a table**, kept whole: a report skeleton, a command, a row shape. A generator parses these, so they are not shortened.
3. **A link replaces a copy.** A rule another file is the home of is one sentence naming the home. The contract keeps §1–§17 with their numbers; a definition keeps its own application of a section and never its sentences; a skill two agents preload is the home of what both need, and the definitions link.
4. **No line outside a rule paragraph narrates.** What a rule used to say, which round found it, what was measured and when — none of it stays. Its homes already exist: git history, the issue the rule cites, the work item's records. A rule whose only grounds were a story keeps the one why-sentence and the link.

## How the check holds it — two rows a pull request already meets, nothing new

Both rows are #930's, in `seal/budgets.md`, read by `.github/scripts/budget_check.py` on every pull request and by `tests/test_a_budget_ratchets.py::test_the_trees_budgets_hold` locally; the ratchet is #930's too: a ceiling moves down in the pull request that moves the measurement, and moving one up takes a commit that changes the budget and a `Budget raised:` line with its reason in the body, which CI reads.

- **`preload:<agent>`** — the bytes of a definition and the skills it injects, already a two-sided gate at 2 % slack. A paragraph appended to any file of the set fails it. Each rewrite phase lowers the rows of the agents whose preload it shrank to the measured value, which is what makes the shape above the standing bar rather than a hope. It sees no meaning: a story the same length as the rule it replaced passes, and review's stage 1 against §*The shape* is what reads that.
- **`history:<path>`** — #930's `docs-history` family, read over every rule file (`budget_check.RULE_FILES`: `CLAUDE.md`, `CONTRIBUTING.md`, `agents/*.md`, `docs/*.md`, `skills/*/SKILL.md`, `skills/*/orchestration.md`, `templates/*.md`) instead of `docs/*.md` alone, under the name `history`. A history line is one outside a rule paragraph, a fence, a comment and a heading that carries a #930 mark (`#NN`, `round N`, a date, `measured`). A rule paragraph is what `rule_paragraphs` already reads — opening on `**`, `- **`, `* **` or `N. **` — so an agent's list-item rules stop counting as history and the two readers of what a rule paragraph is become one. Ceiling 0 for every file this item rewrites, today's count for every other listed file, 0 for an unlisted one. **How it errs:** over on a link to an issue outside its paragraph, under on a story carrying no mark; the bytes row and review are what read the second.

**Gate against report.** The two rows above are gates: deterministic, measured on the tree in CI. The proof below is a report the orchestrator runs on its own account and the phase record carries; CI never runs an agent and no test in the tree makes a later edit owe a run (`plan.md` alternative J). A restatement is removed by the rewrite and counted once at the close by the same Jaccard pass as above; whether that count becomes a report row is Q10, default no.

## The proof — outcome first, then cost, on a small set of real cases

**A rewrite phase closes when the agents whose preload it changed do at least as well on the same inputs and read less.** Two sides, the baseline tree and this branch, run through `claude plugin eval` on the cases under `evals/behaviour/<agent>/`, N = 2 runs a side, `-j 4`; `evals/scripts/noninferiority.py compare` writes `seal/specs/<id>/evals/<agent>-phase-N.md` from the two JSON results, and `tests/test_a_rewritten_definition_proved_non_inferior.py` recomputes the verdict from the record's own numbers. The baseline is taken once, as the build's first step, on the tree after #939 (#929) and #937 (#931) merge and this branch rebases onto it — both are open, both change little in the set, and a baseline taken before them would be compared against a tree they moved.

**The cases, and what each protects.** Small, real, per agent; the sentence graders go (`## Removes`).

| Agent | Cases | Outcome graders — what the case protects |
|---|---|---|
| warden | 4 replay: a historical round's target clone at its `Target SHA`, its spawn prompt — `replay-1791382684-r5`, `replay-1791384160-r2`, `replay-1791779434-r5` stand; `replay-1791852615-r2` (the ledger's own item) is replaced from `--list` by the smallest round with ≥ 2 truths and no ledger fact, `1791382684-r2` first candidate. 3 seeded: a shipped diff with one `mutation-check` operator in a unit it touched — `9b644676`, `4d316179`, `ad447367` stand; `770d721f` (`survivor_check.py`, removed) goes. 1 fixture: `rule-warden-one-finding`, a planted spec violation | `truth-N`: each finding the next round confirmed fixed, matched on path and line window — the real defects the agent still finds; the report's 🔴/🟡 rows no truth matches — the false findings; `shape-`: the report exists at its path, its Verdicts table, its `Needs a fix:` and `Loses a record or crashes:` lines — what the orchestrator's generator must be able to read; `reach-`: the session spawned the warden |
| smith | 4 one-phase builds on a fixture repository (`rule-smith-*`) | the unit exists with its signature and its test file beside it, the phase record exists, a commit landed in the fixture, nothing left behind outside it — the work was built and handed over in the shape the next phase reads |
| framer | 4 small frames (`rule-framer-*`) | `spec.md`, `plan.md` and `questions.md` exist with the mark and a Phases table carrying `Verified by`; no `Write`/`Edit` outside `seal/specs/` — a frame was drawn and nothing was built |
| sealer | 3 broad runs: green, a failing test, a record left open (`rule-sealer-*`) | the `Broad gate` cell written on green and not otherwise, the report says which of the three outcomes, no commit — the one run and the one write |
| scribe | none | no parity fixture exists and the definition is 3,763 B of the shape already; its preload changes only through the contract, whose phase runs the other four. A stated hole, not a silent one |

Every grader is mechanical: `regex` over a file or the last message, `file_exists`, `tool_used`. No LLM judge scores anything, and nobody reads a report by hand to pass a phase.

**Cost, per run, read off the trace.** The stream-json `result` event of a `claude -p` session carries `total_cost_usd`, `duration_ms` and `usage` (`read`: the harness's documented event shape; the baseline's first saved `raw.json` is where the build confirms the field names — Q12). `noninferiority.py run` records them per run beside the graders; `compare` writes both sides' pooled spend, tokens read (input + cache creation + cache read) and wall seconds, and the preload bytes of the side's tree.

**The pass rule**, per agent, pooled over the cases × N = 2 runs a side:

1. recall of truth findings, new ≥ old; a deficit of exactly one truth that at least one new run found is noise and passes, anything larger fails naming the findings;
2. false-finding rate, new ≤ old + 0.05;
3. every shape and reach grader at 100 % on both sides;
4. **cost falls**: the preload bytes of the new side are below the old (deterministic, always true of a rewrite that shrank the file), and the new side's pooled tokens read and spend are not more than 1.1 × the old's — a compaction that leaves the agent wandering shows up as spend before it shows up as findings. Wall seconds are written and never judged, because the machine's load is in them;
5. a side whose runs were cut by `--max-cost-usd` or a timeout is no result, and the test refuses the record.

The fix on a failure is to restore the rule the output lost, in the shape; the bar never moves in a rewrite phase. Each phase runs the sets of the agents whose preload it changed; the contract phase runs all four; the close runs all four once more on the finished tree against the same baseline.

**Cost of the proof** (from phase 2's measurements; nothing else has run): the baseline ≈ 16 warden runs at ≈ $2.5 plus 22 cheap runs, ≈ $45 and ≈ 1.5 h at `-j 4`; a warden phase the same 16 runs; the contract phase every agent; the close every agent — ≈ 120 runs and ≈ $150 over the item on the orchestrator's account. CI runs none of it.

## Scope

**In — this work item.** The preload set rewritten to the shape, one or two files per phase, warden's first: `agents/warden.md`, `skills/agent-contract/SKILL.md`, `skills/code-review/SKILL.md`, `agents/smith.md`, `skills/implement/SKILL.md`, `agents/framer.md`, `agents/sealer.md`, `skills/writing-style/SKILL.md` (Q9); `agents/scribe.md` and `skills/legacy-parity/SKILL.md` read against the shape and left where they already hold. In each rewrite: the rules #923's body says the rewrite states in place, the restated pairs above made one home and one link, the stories removed, each rule that a test holds given its `Enforced by:` line and the `unenforced` row lowered, the `preload:*` rows lowered to the measured value, the test pins re-pointed or removed with a row, the `BASELINE` pairs lowered, before and after bytes and tokens in the phase record. The proof made light (the graders cut, the two ledger cases replaced, cost read) and the baseline taken once. The `history` family over every rule file. `agents/sealer.md` pins `model: sonnet` and the three sentences that say no definition pins one are rewritten in place.

**Targets** — the bar each phase is held to; the ceiling written is the value measured under it:

| File or row | Now | Target | Basis |
|---|---|---|---|
| `agents/warden.md` | 32,121 | ≤ 12,000 | 24 rules × ≤ 8 lines + its report fence and tables |
| `skills/agent-contract/SKILL.md` | 20,409 | ≤ 8,000 | 17 sections, each a rule, one why, one link |
| `skills/code-review/SKILL.md` | 26,150 | ≤ 12,000 | 27 rules + the findings-format fences |
| `agents/smith.md` | 25,400 | ≤ 10,500 | 19 rules |
| `skills/implement/SKILL.md` | 34,330 | ≤ 15,000 | 26 rules + the layout tree and the SDD table |
| `agents/framer.md` | 19,700 | ≤ 9,000 | 35 rules, most already short |
| `agents/sealer.md` | 15,189 | ≤ 7,000 | 21 rules |
| `skills/writing-style/SKILL.md` | 21,000 | ≤ 16,000 | 40 rules, already mostly the shape; its comment block and two stories go |
| `preload:warden` · `:smith` · `:framer` | 99,690 · 101,344 · 95,730 | ≤ 48,000 · ≤ 49,500 · ≤ 48,000 | the files above |
| `preload:sealer` · `:scribe` | 36,113 · 29,554 | ≤ 15,000 · ≤ 17,100 | |
| `history:<every rewritten file>` | today's count | 0 | |

**Out, and whose.** What an agent opens on demand — `skills/verify/SKILL.md`, `skills/settle/SKILL.md`, both `orchestration.md` (except the one model sentence above), the small skills, `templates/`, `CONTRIBUTING.md`, `CLAUDE.md` — is #940: their `history:` rows land here at today's values. `docs/` is #941, its 18 `docs-history` rows becoming `history` rows at the same numbers; the two docs sentences on model pins are rewritten here because this item makes them false. What one task makes an agent read beyond its preload — the round records a reviewer inherits, the process archive — is #945. `README.md` and `README.ko.md` are read by people, not by a spawn. The work item records under `seal/specs/` are history by design, retired by `settle --retire-process`. The test suite's own size is #929; a test module is this item's only where it asserts on a file of the set's text, and moves with the text.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a rewritten preload is proved not worse | `agents/warden.md` rewritten; the orchestrator runs the warden set on both sides and `compare` | `evals/warden-phase-1.md` holds both run ids, the pooled recall, false rate, shape rate, tokens, spend and preload bytes of both sides, every grader's two counts, and `Verdict: pass`; the record test recomputes it green |
| S2 a worse definition is caught | the two terminal-line rules removed from `agents/warden.md` (phase 2's measured case) | `Verdict: fail` naming both shape graders; a record saying `pass` over failing numbers is red |
| S3 a costlier definition is caught | a side whose pooled spend is 1.2 × the baseline's with outcome equal | `Verdict: fail` naming rule 4 |
| S4 a cut side is no result | a side cut by `--max-cost-usd` or a timeout | `Verdict: no result`; the test refuses the record |
| S5 the sentence graders are gone | phase 1 lands | no `rule-*.md` under `evals/behaviour/`; `tests/test_evals_layout.py` refuses the kind; `rule_cases.py` writes outcome graders only |
| S6 an appended paragraph fails | a paragraph citing `#NNN` appended to a rewritten file | `budget_check.py` exit 1 naming `preload:<agent>` over its ceiling and `history:<path>` 1 over 0, with the line |
| S7 an in-place rewrite holds | a rule paragraph reworded at the same size, no mark added | exit 0 |
| S8 a list-item rule is a rule | `- **rule** … (#544)` in a fixture | not a history line; `rule_lines` removed, the mutation that opens on `**` alone turns the case red |
| S9 every rule file is held | a `skills/x/SKILL.md` with a history line and no row | held at the family row's 0, exit 1 naming the file |
| S10 the docs rows move with their numbers | phase 2 | 18 `history:docs/…` rows at the `docs-history` ceilings of f975ea66; the body carries the `Budget removed:` lines |
| S11 a restated pair is one home | each rewrite phase | the pairs §*The problem, measured* lists for its files: one keeps the rule, the other links by file and heading; the Jaccard pass at the close finds none of them ≥ 0.35 |
| S12 the rules the owner named are stated | phases 1 and 3 | `agents/warden.md`: the report goes to the branch worktree's `seal/specs/<item>/rounds/`; the contract: an agent cleans up only what it started, by its own PIDs, never by command name or a glob over a shared directory; the contract: a check that refuses correct code is fixed or reported, never dodged by bending the code; §5 absorbs the premise check (a conclusion that nothing should change is a claim to open). Each a rule paragraph with its link |
| S13 the sealer runs on Sonnet by default | phase 5 | `agents/sealer.md` frontmatter `model: sonnet`; a case holds the pin; the three sentences saying no definition pins a model rewritten in place; the sealer set's new side runs on Sonnet and its record says `pass` |
| S14 the contract keeps its numbers | phase 3 | `## §1` … `## §17` in order; `test_the_agent_contract_holds_the_universal_rules.py` and `test_every_agent_reads_the_contract.py` green |
| S15 no rule is lost unseen | each rewritten file | the phase record lists every bold-led rule of the old file with its new coordinate or its removal; every test that pinned a sentence is green on the new sentence or removed with a row in `overview.md` |
| S16 nothing asks a person | the whole change | no `AskUserQuestion`, no `input()`, no new prompt; a raise is a body line; the eval runs under `--trust-plugin --allow-tools --scaffold --max-cost-usd` and scores itself |
| S17 nothing in the tree obliges a later run | after the close | no test reads `evals/baseline-*.json` against the tree's preload; `owed_records` is gone |

## Data & interfaces

`seal/budgets.md`: the `docs-history` row and `## Docs history lines` table become the `history` row and `## History lines`, every rule file with a nonzero count listed. `budget_check.py`: `docs_lines` reads `rule_files` and `classify` opens a rule paragraph on `RULE_PARAGRAPH`; `rule_lines` and `docs_history_values` go; `FILE_TABLES["history"]`. `evals/scripts/noninferiority.py`: `run` records `total_cost_usd`, `duration_ms` and `usage` per run; `compare` and `verdict` carry rule 4; `census_problems`, `owed_records` and the census constants go. `evals/scripts/rule_cases.py`: outcome graders only. `tests/test_a_rewritten_definition_proved_non_inferior.py`: T11 gains rule 4's cases and loses T10 and T12. `tests/test_evals_layout.py`: `KINDS` without `rule`. `agents/sealer.md`: `model: sonnet`. `skills/code-review/orchestration.md:438–440`, `docs/review-handoff-protocol.md:468`, `docs/round-record-spec.md:763`: rewritten to say the sealer pins Sonnet, a spawn's model overrides it, and `Ran by` records what ran. The changelog fragment `seal/specs/<id>/changelog.md` carries the per-agent before/after table.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence graders | `evals/behaviour/*/*/graders/rule-*.md` (149 files), `rule_cases.py#contract_rules`, `#rule_regex`, `#rule_tool` | a grader per sentence of today's text scores deleting a bloated sentence as a loss; a rule worth keeping shows as an outcome case going red (#923, the owner) |
| the rule census | `noninferiority.py#census_problems`, `#CENSUS`, `test_the_census_refuses_a_rule_with_neither_grader_nor_reason`, `test_every_census_in_the_tree_names_a_grader_or_a_reason` | per-rule bookkeeping the owner refused; the phase record's rule list (S15) is read by the round, not by a checker |
| the owed-record coupling | `noninferiority.py#owed_records`, `test_a_changed_preload_with_no_passing_record_is_red`, `test_every_baseline_in_the_tree_is_answered` | a tree-wide test making every later definition edit owe a paid run is the apparatus the owner refused; the record keeps the preload hashes it measured |
| two cases whose truth is a removed thing | `evals/behaviour/warden/replay-1791852615-r2/`, `evals/behaviour/warden/seeded-770d721f/` | replaced from `replay_targets.py --list` and `seed_defects.py --list` by cases whose truth stands on the tree |
| the `docs-history` family and its table | `seal/budgets.md#"## Docs history lines"`, `budget_check.py#docs_history_values` | the `history` family, same numbers, every rule file |
| the second reader of a rule paragraph | `budget_check.py#rule_lines` | `classify` reads through `rule_paragraphs`' opener |
| the round-3 story under the venv rule | `agents/warden.md#"## Where you work">"This line arrived at round 3 of one work item, after two rounds had each"` | the rule stays; the story is #107's |
| the "one round that ever looked" story | `agents/warden.md#"## Role">"Opening something anyway is allowed and is the point — the one round that"` | the rule stays with its why; the count is #228's |
| the report/record history | `agents/warden.md#"## Role">"That distinction is the whole of the second of them. Until it was"` | #228 |
| the #187 story under the fence rule | `agents/warden.md#"## Report">"That was #187: the report's snippets lived only in a transcript, and the fix"` | #187 |
| the first-user story under the terminal lines | `agents/warden.md#"## Report">"The field's first user hit exactly that and had nothing to read. Neither line"` | the shape example stays |
| §2's missing-copy history | `skills/agent-contract/SKILL.md#"## §2 Narrow and often; the broad gate is one act with one owner">"This rule sat in two agent definitions in near-identical words, and a third"` | #107 |
| §6's former shape | `skills/agent-contract/SKILL.md#"## §6 You return a report">"This section used to carve the exceptions instead — each one named in the"` | git history of the file |
| §7's #30 story | `skills/agent-contract/SKILL.md#"## §7 A probe is named `test_tmp_*`, one file, run once, deleted">"The file half is what a reviewer did follow, to the letter, during #30's"` | #30 |
| §9's 128-edit measurement | `skills/agent-contract/SKILL.md#"## §9 Edits go through the `Edit` tool">"across 47 files, and a column insertion that silently did not happen because"` | the why-sentence keeps the mechanism; the number is in #107's record |
| where the records used to live | `skills/code-review/SKILL.md#"## Cross-session records — `seal/specs/<work-item-id>/`">"The records used to be keyed by a pull request number"` | `docs/review-handoff-protocol.md` holds it |
| the second copy of each restated pair | the eight in-context pairs and the cross-spawn pairs of §*The problem, measured*, by line | one home keeps the rule; the other becomes a link naming it |

Sentence-level removals inside a rewritten section are the rewrite itself: the phase record lists each old rule's new coordinate (S15), the pins that held a dropped sentence go with a row, and the suite shows the agent still does what the rules say.

## Open questions → questions.md

Reframed 2026-10-15 by framer, on the tree after #944 — not after a round, so this line stands above the mark, where `chain_check.py#frame_foot` does not read it.

Framed 2026-10-14 by framer, before the build.
