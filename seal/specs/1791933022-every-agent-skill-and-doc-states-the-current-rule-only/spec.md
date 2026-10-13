# Feature Specification: every agent, skill and doc states the current rule only

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. Growth is declared in the pull request body (`Budget raised:`), read by CI; a rewrite is proved not worse by a run nobody scores by hand; a restated rule is caught by a reader or by the round already running |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The widened checker and the non-inferiority test are gates: every case seen red, the failure direction stated (they block more), a prompt budget of zero, a `Reads:` line per unit, a frame that names what it removes |
| `docs/the-record-layout.md` §*Every kind of record, at a glance*, §*The size a reader takes whole* | A rule has one home and "the copy is the defect"; a file a reader takes whole is ≤ 1,000 lines and 64 KB. This work adds the stricter bound: a file an agent preloads is held to the bytes a rewrite to the shape below reached, and a rule's home is identified by what enforces it |
| `docs/the-agent-set.md` §*One contract every agent receives, and one definition each*, §*What a spawn costs* | A definition keeps only its own application; the contract's section numbers are never reused or re-ordered, so the rewrite keeps §1–§17 as headings |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*, §*A claim held by a test* | Released ledger files never change. Every row an edit reaches gets one `Re-read ·` or `Corrected ·` row in `seal/ledger/1791933022-….md`; a row moves onto its test by one `Corrected ·` row when the edit reaches it, never in bulk (the owner's 2026-10-08 answer) |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; a removal a phase makes that it does not name is a divergence in `overview.md` |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file*, §*seal/specs/<work-item-id>/* | Ledger rows and the changelog go to this item's fragments; its eval records live under its directory, read by one test, retired with the process record |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The work alters what every spawn reads, which is the top rung |
| `tests/test_no_passage_is_pasted_into_a_second_file.py` (docstring, *Why a ratchet*, *What it does not catch*) | A pair this work drains lowers its `BASELINE` entry in the same change; the verbatim ratchet does not see a rule restated in fresh words, which is what §*A rule stated twice* adds |
| `tests/test_a_moved_rule_leaves_its_definition.py` (docstring, *Where this draws the line*) | An agent definition may cite a contract section and say what it means for its role; it may not carry the contract's sentences |
| The owner's two conditions, 2026-10-14 | Compacting must not produce output worse than today's (§*Non-inferiority, proved per phase*); a rule restated in different words is caught, not left to review alone (§*A rule stated twice*) |

## The problem, measured

`executed` at 99176470 (= `origin/release/v0.22.0`, 0.21.1) with the commands in `plan.md` §*Technical context*; #930's checker at 661dc60b run on a copy of this tree with #930's `seal/budgets.md` placed in it.

| What | Value |
|---|---|
| Preload per spawn, agent share (`preload:*`) | framer 99,089 B · smith 106,350 · warden 102,229 · sealer 36,113 · scribe 29,554; plus `CLAUDE.md` 9,261 and `~/.claude/CLAUDE.md` 8,042 in every prefix |
| First-turn prefix in tokens, median over 185 classified spawns of four sessions | sealer 58,386 (38 spawns) · warden 78,624 (81) · framer 83,437 (30) · smith 84,823 (36); fit over the four: 2.79 B/token above a 39,249-token harness share, residual ≤ 3,539 |
| One run of each agent, medians over the same spawns | warden 13 min wall, 447 k uncached input tokens, 13.0 M cache-read, 51 tool calls · smith 32 min, 1.0 M, 81.6 M, 219 · framer 14 min, 1.26 M, 9.4 M, 43 · sealer 10 min, 188 k, 0.6 M, 6 |
| Prose read on demand in a run, median bytes of `agents/`, `skills/`, `docs/`, `templates/` files opened | warden 27,564 (max 310,555) · framer 69,921 · smith 112,015 (max 534,834) · sealer 0 |
| The corpus an agent can read: 68 files | 22,587 lines · 1,500,921 B; `docs/` 19 files 9,911 lines 708,070 B with three at 999/999/1,000 lines; `skills/verify/SKILL.md` 1,020 lines |
| Narrative by #930's marks (outside rule blocks) | 439 lines over 68 files; 250 in `docs/`; 484 lines cite an issue number |
| Narrative by paragraph census (`agents/warden.md`) | 579 lines: 25 bold-led rule paragraphs, 278 lines in paragraphs that open with no rule, 42 lines of fences and tables; the #930 reader counts 43 rule lines because it opens a rule block only on a line that starts with `**`, and an agent's rules are list items |
| Rule paragraphs and what identifies them (bold-led, outside fences, tables and comments) | 1,176 over the 68 files; 143 end in `Enforced by:`; 302 name any enforcer or link (a test, a unit, a `docs/*.md §*…*`, an issue); 874 name none. 18 enforcer targets are named by paragraphs in two or more files (25 paragraphs): 10 are the `one-root-by-lifetime` pair's sanctioned mirror, 2 the grammar's own `tests/test_x.py::test_y` examples, and 4 are real — `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` (`skills/implement/SKILL.md`, `skills/implement/orchestration.md`), `.github/workflows/hygiene.yml` (`docs/branch-and-release.md`, `docs/release-checklist.md`), `tests/test_release_hygiene.py` (`docs/issues-and-milestones.md`, `docs/release-checklist.md`), one heredoc case (`docs/commit-review-gate-spec.md`, `docs/the-commit-gate-inside-git.md`) |
| Paraphrase, by stdlib token-set similarity (Jaccard over lower-cased words minus 40 stopwords, paragraphs of ≥ 12 words, across files) | 51 pairs at ≥ 0.35, 21 at ≥ 0.5; of the 21, 10 are the agents' identical contract paragraph and 2 the `CLAUDE.md` block, both deliberate copies with a test of their own; 9 are restatements |
| How it grew | `agents/warden.md` 164 → 579 lines over 36 commits, +789/−210; 10 of the 35 commits after the first deleted nothing. `agents/smith.md` +666/−235 · `skills/verify/SKILL.md` +1,158/−138 · `docs/round-record-spec.md` +1,035/−35 |
| Restatement debt the verbatim ratchet sees (#730 `BASELINE`) | warden–smith 153 shared 15-word runs · warden–`code-review/SKILL.md` 53 · warden–`round-record-spec.md` 36 · smith–`implement/SKILL.md` 46; 106 pairs in the table |
| Ledger coupling | 3,354 released rows in 46 files; 837 anchor a prose file (1,127 mentions). `agents/warden.md` 34: 26 on its three section headings, 4 on headings inside its report fence, 4 on quoted lines. `templates/config.md` 151 · `docs/worktree-guard-spec.md` 103 · `skills/implement/orchestration.md` 89 · `skills/verify/SKILL.md` 74 · `CONTRIBUTING.md` 60 |
| Test coupling | 144 of 191 test modules pin at least one sentence (a string literal ≥ 25 characters found verbatim in a prose file; 2,564 hits). `agents/warden.md`: 28 modules, 101 literals (`test_the_rules_have_one_owner.py` 17, `test_broad_gate_rule.py` 11, `test_the_record_is_generated.py` 8, `test_the_reviewers_report_reaches_the_record.py` 8) |
| Ground truth for a warden replay, in the tree | 8 work items with 32 round records; 19 with a `Target SHA` that resolves, 11 of those with findings: 1 🔴 and 32 🟡, each closed `fixed <sha>` and confirmed 🟢 in the next round. Retired records of earlier releases read at their tags (`git show v0.21.0:seal/specs/<id>/rounds/round-N.md`) |
| The eval harness on this machine (`read` from `claude plugin eval --help`, 2.1.296; never run here) | cases are `<eval dir>/**/case.yaml` + `prompt.md` + `graders/*.md`; a target is a path; `--runs`, `--json`, `--max-cost-usd`, `--threshold`, `--concurrency 1–8`, `--trust-plugin`, `--allow-tools`, `--scaffold`; graders: regex over a file or the last message, `file_exists`, `tool_used`, an LLM judge (haiku). `evals/` already holds 5 cases that have never run and `tests/test_evals_layout.py` holds their shape |

## The shape of a compact file

A file an agent reads holds rules, formats and links, and nothing that narrates.

1. **A rule is one paragraph.** It opens with the rule in bold, in one or two sentences; a list item whose text opens bold is a rule paragraph too. It holds at most one sentence of why. It ends with what identifies it: `Enforced by: <test node ids, units or files>` where something holds it, and otherwise one link — an issue, a `docs/*.md §*heading*`, or a work item's record at its release tag. Eight live lines is the bar a rewrite is held to by review; a paragraph needing more is two rules or a rule and a story.
2. **A format is a fence or a table**, kept whole: a report skeleton, a command, a row shape. These are what a generator parses, so they are not shortened.
3. **A link replaces a copy.** A rule another file is the home of is one sentence naming the home (`docs/the-record-layout.md` §*Every kind of record, at a glance*). The contract keeps §1–§17 with their numbers; a definition keeps its own application of a section and never its sentences.
4. **No line outside a rule paragraph narrates.** What a rule used to say, which round found it, what was measured and when, who did what — none of it stays. Its homes already exist: git history, the issue the rule cites, the work item's records. A rule whose only grounds were a story keeps the one why-sentence and the link, so the next reader can open the story and the agent never reasons past a rule with nothing under it.

**What a check holds, and how it errs.** Two numbers per file, both rows of `seal/budgets.md` read by `.github/scripts/budget_check.py` on every pull request and by the suite case (#930):

- `bytes:<path>` — the file's bytes, a two-sided ratchet at 2 % slack. An appended paragraph fails it; a rewrite that frees bytes lowers it in the same pull request; a new rule raises it with a `Budget raised:` line. Its ceiling after a rewrite is the number the rewrite reached, which is what makes the shape above the standing bar rather than a hope. It errs neither way on bytes and sees no meaning: a story the same length as the rule it replaced passes, and review's stage 1 against this section is what reads that.
- `history:<path>` — #930's `docs-history` family generalised to every file in scope, ceiling 0 once the file is rewritten. A line outside a rule paragraph, a fence, a comment and a heading that carries `#NN`, `round N`, a date, `measured`, `used to`, `no longer`, `arrived at` or `before this` is a history line. A rule paragraph opens on `**`, `- **`, `* **` or `N. **` and closes at `Enforced by:` or its blank line. It errs over on a link to an issue that sits outside its paragraph, and under on a story that carries none of the marks — 278 of `agents/warden.md`'s lines sit in such paragraphs and the marks find 19.

Together: an append of a paragraph is red on both rows; a rewrite in place at the same size is green; a cut is green once its row is lowered. The paragraph bar, the why-sentence and the link are review's half; whether the agent still behaves is §*Non-inferiority*'s; whether the rule already stands elsewhere is the next section's.

## A rule stated twice is caught, in three arms

A rule written again by a model never comes back in the same words, so the verbatim ratchet misses the duplicates that will occur. What makes two paragraphs one rule is that they are held by the same thing, and the shape makes that a name a reader can compare. Three arms, in the same checker and the same hygiene step and suite case; a `.ko.md` edition is read as its `.md`'s mirror and never paired with it.

1. **Identity by enforcer — a gate.** Two rule paragraphs in different files whose `Enforced by:` lines name the same target are one rule stated twice: exit 1 naming both, and the pull request makes one of them a link to the other (a paragraph of at most two live lines that names the other's file and heading is a link and is never paired). A target is read as the ledger reads one — `tests/x.py::case`, `path#unit`, a file — and only where it resolves in the tree, so the grammar's own `tests/test_x.py::test_y` examples pair nothing. How it errs: over where one target holds two different rules, which is a module-level target (`tests/test_release_hygiene.py` holds several) — the shape asks for the case, and naming it is the repair; under on every paragraph that names no enforcer, 874 today, which is arm 2's. Four real pairs today (§*The problem, measured*), each a phase-1 link; the gate's reach grows with every rewrite that gives a rule its enforcer, which the rule census forces for every rule an output can show.
2. **Same conclusion, no enforcer — the round already running.** For every rule paragraph a pull request adds or changes that names no enforcer, the checker prints under `## Restatement candidates` in its summary the three standing rule paragraphs of other files nearest it by token-set similarity (Jaccard over normalised words, ≥ 0.35), each with its file, heading and first line. The warden's round reads that list in its clone (`budget_check.py --candidates <base>` prints the same) and judges each candidate for one conclusion: a match is a 🟡 *already at `<file> §heading`, link it*, with the paste-ready link. No person is asked; a reviewer reads a list of at most three per paragraph rather than the corpus. How it errs: under on a paraphrase that shares no vocabulary, which no cheap similarity finds; over in the candidates, never in a verdict, since the reviewer decides.
3. **Light paraphrase — a report.** `restated` is a `report` row: the count of cross-file rule-paragraph pairs at Jaccard ≥ 0.5, stdlib only (frozensets over 1,176 paragraphs, under two seconds), printed on every pull request and in the release trend. 21 today, 12 of them deliberate copies with tests of their own, which is why it is not a gate: a gate would need an allowlist that rots. If the number climbs across two releases it becomes a two-sided ratchet like `bytes`, with the deliberate pairs listed once.

**With the non-inferiority proof.** Merging two restated rules into one home happens only in a rewrite phase, where the suite runs: both old paragraphs are rows of that phase's rule census mapped to the one home, each nuance an output can show keeps its rule-exercise grader (pass rule 4 names a grader every old run satisfied and no new run does), and the ledger rows anchored on either old paragraph are re-read against the home, so a nuance the merge dropped is a `Corrected ·` row somebody has to write, never a silent loss.

## Non-inferiority, proved per phase

**A rewrite phase closes only when the agents whose preload it changed score at least as well as today's definitions on the same inputs, and a test holds the record.** The runs are `claude plugin eval` over a behaviour suite under `evals/behaviour/`, run once against the plugin tree at the merge base (the baseline, taken before the first rewrite and committed as `seal/specs/<id>/evals/baseline-<agent>.json`) and once against this branch after each rewrite; a comparator writes `seal/specs/<id>/evals/<agent>-phase-N.md` from the two JSON results, and `tests/test_a_rewritten_definition_proved_non_inferior.py` recomputes the verdict from the record's numbers for every `agents/*.md` and preloaded skill that differs from the merge base. No person scores anything; the orchestrator runs one command at the phase boundary, on its own machine and credential, never in CI.

**The suite, three kinds of case, every grader mechanical.**

| Kind | Agents | Input | Ground truth and graders |
|---|---|---|---|
| Replay | warden | a historical review target: the clone at a round record's `Target SHA`, its base, its spawn prompt; from the tree's 11 rounds and the last two release tags' retired records, generated by `evals/scripts/replay_targets.py` | each finding the round closed `fixed` and the next round confirmed 🟢 is a regex grader over the report file: its path and its unit, or its line within ±15; a grader `round_record.py new --report <file>` exits 0 (the shape); the 🔴/🟡 rows matching no truth are the false findings |
| Seeded | warden | a shipped diff with one `mutation-check` operator applied to a unit it touched, in the scaffold clone; `evals/scripts/seed_defects.py` | the mutated `path#unit`, one grader; supply unbounded, so the set is regenerated per release and never tuned to |
| Rule exercise | warden, smith, framer, sealer, scribe through the contract cases | a fixture repository with a one-phase plan, a one-finding review, a small issue to frame, a broad run to take; one case per rule of the census that an output can show | `file_exists` (the phase record, the three frame files, the report at its path, the one cell), regex (the proof block, `Needs a fix:` and `Loses a record or crashes:` lines, the `executed`/`read`/`unverified` labels, a bare integer finding id, `nothing to drain`), `tool_used` (`Edit` and never a heredoc, no `Agent`, no `git commit` in the sealer), the clean `git status` after the run (nothing left behind) |

**The rule census is the suite's index.** Each phase lists every bold-led rule of the old file with its new coordinate or its `## Removes` row, and for each: `Exercised by: <case>/<grader>` or `not exercisable — <why>`. The test refuses a census row with neither, so a rule nobody can observe is a stated hole and not a silent one.

**The pass rule**, per agent, pooled over K cases × N = 2 runs a side (the baseline's N runs are taken once and reused by every phase):

1. recall of truth findings, new ≥ old; a deficit of exactly one truth that at least one new run did find is read as noise and passes, anything larger fails naming the findings;
2. false-finding rate, new ≤ old + 0.05;
3. shape graders at 100 % on both sides;
4. per rule-exercise grader: a grader any old run satisfied and no new run satisfied fails naming the rule — this is the clause that catches a rarely exercised rule, independent of the pooled numbers;
5. a side whose runs were cut by `--max-cost-usd` or a timeout is no result: the record says so and the test refuses it.

The fix on a failure is to restore the rule, in the shape; the bar never moves in a rewrite phase. The sizes: warden K = 8 (4 replay, 4 seeded) plus its rule cases; smith K = 4 one-phase builds capped at `max_turns` 80 and 20 min; framer K = 4 small frames; sealer K = 3; `--concurrency 4`.

**Cost** (estimated from the run medians above; nothing has run): the baseline once, all four agents, 38 runs, ≈ 9 h serial and ≈ 2.5 h at `-j 4`, ≈ 25 M uncached input tokens and ≈ 1 B cache-read; a warden phase 16 runs ≈ 1 h at `-j 4`, ≈ 7 M uncached and 210 M cache-read; the contract phase runs every agent, 38 runs. CI runs none of it: one test reads the records in under a second on the three legs, so a private repository pays no added minute for it (#929's price table, unverified).

**What is not verified by this frame.** That `claude plugin eval` is enabled on the owner's account and that a case's session reaches the plugin's agents through the `Agent` tool as production does: `read` from `--help`; `evals/README.md` says early access. Phase 2 proves the harness on one case with a deliberately broken definition before any baseline counts, and where the command does not run, the fallback is `claude -p --plugin-dir <tree> --agent specseal:<name>` driven by the same comparator (`plan.md` alternative E7).

## Scope

**In — this work item.** Measured first (above). The check: the `history` family over `agents/*.md`, `skills/*/SKILL.md`, `skills/*/orchestration.md`, `templates/*.md`, `docs/*.md`, `CLAUDE.md`, `CONTRIBUTING.md` (the 19 `docs-history` rows become `history` rows at the same numbers), the `bytes` family over the same files, the widened marks and the list-item opener, the three restatement arms and the four pairs they find today turned into links, each case seen red. The non-inferiority harness: the behaviour suite and its generators, the comparator, the record test, and the baseline of all four agents on today's definitions. Then the preload set rewritten to the shape, one file per phase, warden's first: `agents/warden.md`, `skills/agent-contract/SKILL.md`, `skills/code-review/SKILL.md`, `agents/smith.md`, `skills/implement/SKILL.md`, `agents/framer.md`, `agents/sealer.md`; `agents/scribe.md` read against the shape and left where it already holds. For each: the eval pass for every agent whose preload it changed, the ledger rows it drifts re-read or corrected in the fragment, the tests pinning its sentences re-pointed or removed with a row here, the #730 pairs it drains lowered, its `bytes:`, `history:` and `preload:*` rows lowered to what it reached, before and after bytes and tokens in the phase record.

**Targets** — the bar each phase is held to; the ceiling written is the measured value under it:

| File | Now | Target | Basis |
|---|---|---|---|
| `agents/warden.md` | 33,258 | ≤ 12,000 | 25 rules × ≤ 8 lines + 42 format lines; the kept-shape estimate is 13,079 with narration still inside long paragraphs |
| `skills/agent-contract/SKILL.md` | 20,426 | ≤ 8,000 | 17 sections, each a rule, one why, one link |
| `skills/code-review/SKILL.md` | 27,535 | ≤ 12,000 | 26 rules + the findings format fences (42 lines) |
| `agents/smith.md` | 27,070 | ≤ 10,500 | 16 rules; kept-shape estimate 10,363 |
| `skills/implement/SKILL.md` | 37,844 | ≤ 15,000 | 28 rules + the layout tree and the SDD table (70 format lines) |
| `agents/framer.md` | 19,809 | ≤ 9,000 | 32 rules, most already short |
| `agents/sealer.md` | 15,687 | ≤ 7,000 | 21 rules; 8 of them over 8 lines today |
| `agents/scribe.md` | 3,764 | 3,764 | already the shape |
| `skills/writing-style/SKILL.md` | 21,010 | 21,010 | out, below |
| `preload:warden` | 102,229 | ≤ 53,010 | the four files above; ≈ 64,500 tokens by the fit, from 78,624 |
| `preload:smith` · `:framer` | 106,350 · 99,089 | ≤ 54,510 · ≤ 53,010 | |
| `preload:sealer` · `:scribe` | 36,113 · 29,554 | ≤ 15,000 · ≤ 17,128 | |
| `history:<every file in scope>` | today's count | 0 after its rewrite | |

**Out, and whose — all of it in 0.22.0.** The on-demand skills and templates (`skills/verify/SKILL.md` 59,722 B, `skills/evidence-check/SKILL.md` 53,733, the two `orchestration.md` 46,760 and 52,161, `skills/settle/SKILL.md`, `templates/config.md` 41,405, `templates/sdd-round.md` 30,242, `CONTRIBUTING.md`, `CLAUDE.md`) are #940, and `docs/` (19 files, 708 KB, ~400 ledger rows) is #941: their `bytes:` and `history:` rows land here at today's values, and each is framed separately from the targets table in `plan.md` §*The split*, on phase 1's check and phase 2's harness. `docs/one-root-by-lifetime.md` and its `.ko.md` are rewritten to the current rule in #941 (the owner's answer to Q1). `skills/writing-style/SKILL.md`: the owner's own style canon, mirrored from `~/.claude/skills/`, which shadows the tree's copy on this machine (26,422 B there); not this item's to cut. `README.md` and `README.ko.md`: read by people, not by a spawn (#755 cluster d). The work item records under `seal/specs/` and the round records a reviewer inherits: history by design, retired by `settle --retire-process`; "records that summarise" (#930 §*Out*) is a different design and a different item. The test suite's own size and which cases guard nothing: #929. The budgets' mechanism: #930, which this branch builds on.

**The boundary with #929.** A test module is this item's — or #940's or #941's for its file — when it opens a file under `agents/`, `skills/`, `docs/`, `templates/`, `CLAUDE.md` or `CONTRIBUTING.md` and asserts on that file's text; it moves with the text, its pin re-pointed or removed with a row. Every other test is #929's. Where #929 removes a module that also pins prose, #929's removal stands and this item does not plant the pin again.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 an appended paragraph fails | a paragraph citing `#NNN` is appended to `agents/warden.md` after its rewrite; `budget_check.py` runs | exit 1 naming `bytes:agents/warden.md` over its ceiling and `history:agents/warden.md` 1 over 0, with the line number |
| S2 an in-place rewrite holds | a rule paragraph of the same file is reworded in place at the same size, no mark added | exit 0 |
| S3 a cut lowers its row | a rewrite drops a file under its band and the pull request lowers `bytes:<path>` | exit 1 until the row moves, then 0 (#930 S4) |
| S4 every file in scope is held | a new `agents/*.md` or `skills/*/SKILL.md` with no row | held at the family's ceiling (`history` 0; `bytes` the family row's), exit 1 naming the file |
| S5 a list-item rule is a rule block | `- **rule** …` lines in a fixture; the classifier runs | counted rule, not history; the mutation that opens only on `**` turns the case red |
| S6 the widened marks | a fixture line with `used to`, `no longer`, `arrived at`, `before this` outside a rule paragraph | counted history; inside one, not |
| S7 warden's preload reaches its target | phases 3–4 land | `preload:warden` ≤ 53,010 measured by the checker; `history:agents/warden.md` 0; `payload_meter.py --agent warden` before and after in the phase records |
| S8 no released ledger file changes | every phase | `git diff --stat origin/release/v0.22.0 -- seal/releases seal/ledger.md` empty; every drifted row has a `Re-read ·` or `Corrected ·` row in the fragment; `evidence-check` exit 0 |
| S9 a rewritten preload is proved not worse | `agents/warden.md` differs from the merge base; the suite runs | `seal/specs/<id>/evals/warden-phase-3.md` holds the baseline run id, the new run id, the pooled recall, false rate and shape rate of both sides, every rule grader's two counts, and `Verdict: pass`; `tests/test_a_rewritten_definition_proved_non_inferior.py` recomputes the verdict from those numbers and is green |
| S10 a worse definition is caught | `agents/warden.md` with its `## Report` fence deleted, or with the `Needs a fix:` rule removed, run through the suite in phase 2 | the comparator writes `Verdict: fail` naming the shape grader or the rule grader; the test is red on that record; a record saying `pass` over failing numbers is red too |
| S11 a rarely exercised rule is lost | a new side where one rule grader every old run satisfied is satisfied by no new run, while the pooled numbers hold | `Verdict: fail` naming the rule (pass rule 4), whatever the pooled recall says |
| S12 a changed preload with no record | a rewritten `agents/*.md` or preloaded skill and no `evals/<agent>-phase-N.md`, or one whose runs were cut short | the test is red naming the file and the agents owed a record |
| S13 no rule is lost unseen | each rewritten file | the phase record's rule census: every bold-led rule of the old file → its new coordinate or its `## Removes` row, each with `Exercised by:` or `not exercisable — <why>`; the test refuses a row with neither; every test that pinned it green on the new sentence or removed with a row |
| S14 the pairs drained | `agents/warden.md` rewritten | `tests/test_no_passage_is_pasted_into_a_second_file.py` `BASELINE` lowered for the warden pairs in the same commit; the case green |
| S15 the contract keeps its numbers | `skills/agent-contract/SKILL.md` rewritten | `## §1` … `## §17` headings present in order; `tests/test_every_agent_reads_the_contract.py` green |
| S16 nothing asks a person | the whole change | no `AskUserQuestion`, no `input()`, no new prompt; a raise is a body line; the eval runs under `--trust-plugin --allow-tools --scaffold --max-cost-usd` and scores itself; a restatement candidate goes to the round, never to a person |
| S17 the `docs-history` rows move with their numbers | phase 1 | 19 `history:docs/…` rows at the 19 ceilings of 661dc60b; the body carries the `Budget removed:` lines the ratchet asks for |
| S18 the same enforcer in two files fails | two fixture rule paragraphs in different files end `Enforced by: tests/test_a.py::test_b`, which resolves | exit 1 naming both paragraphs by file, heading and first line; with one of them a two-line link naming the other's file and heading, exit 0; with a target that does not resolve, nothing is paired; the `.ko.md` mirror pairs nothing |
| S19 a new unenforced rule gets its candidates | a pull request adds a bold-led paragraph with no `Enforced by:` whose words overlap a standing paragraph of another file | the summary's `## Restatement candidates` lists the standing paragraph with file, heading and first line, at most three per new paragraph; `--candidates <base>` prints the same list on stdout; the tree's own run against itself lists none |
| S20 the paraphrase count is reported | any run | `restated` row in the summary with the pair count and the ten highest pairs; `report` kind, never exit 1 |
| S21 today's four pairs are links | phase 1 | the four shared targets of §*The problem, measured* each name one home; the gate exit 0 on the tree |

## Data & interfaces

`seal/budgets.md` (from #930) gains the `bytes` family row and its `## File bytes` table (`| File | Bytes ceiling |`), the `## Docs history lines` table becomes `## History lines` under the `history` family row, and a `restated` report row joins the Budgets table, all read through `hooks/config.py#gfm_table`. `budget_check.py`: `HISTORY` widened, `rule_lines` opening on a list-item bold lead, a bytes measurer (`measure_bytes`, NAME NOT IN TREE until phase 1), the `bytes` family in `FILE_TABLES`, a rule-paragraph reader with its enforcer targets resolved through `evidence_check.py#named_unit` as `fold_check.py#target_problem` does, the enforcer gate, `--candidates <base>` and the `## Restatement candidates` summary section (`rule_paragraphs`, `shared_enforcers`, `candidates`, `restated_pairs`, NAME NOT IN TREE until phase 1). `evals/behaviour/<agent>/<case>/` cases with `case.yaml`, `prompt.md`, `scaffold.sh`, `graders/*.md`; `evals/scripts/replay_targets.py`, `seed_defects.py`, `rule_cases.py` (generators, NAME NOT IN TREE until phase 2) and `evals/scripts/noninferiority.py` (the comparator, NAME NOT IN TREE until phase 2); `tests/test_evals_layout.py` recursing as `claude plugin eval` does; `seal/specs/<id>/evals/baseline-<agent>.json` and `<agent>-phase-N.md`. The warden's round reads the candidates list: one sentence in `skills/code-review/SKILL.md` §*Comparison axes* (rewritten in phase 4 with that file). Ledger rows: this spec's clauses on the checker's and the comparator's units and their tests in `seal/ledger/1791933022-every-agent-skill-and-doc-states-the-current-rule-only.md`, with the `Re-read ·` and `Corrected ·` rows each phase writes.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the `docs-history` family and its table | `seal/budgets.md#"## Docs history lines"` | the `history` family, same numbers, every file in scope |
| the round-3 story under the venv rule | `agents/warden.md#"## Where you work">"This line arrived at round 3 of one work item, after two rounds had each"` | the rule stays; the story is in the contract's own history (#107) |
| the "one round that ever looked" story | `agents/warden.md#"## Role">"Opening something anyway is allowed and is the point — the one round that"` | the rule stays with its why; the count is #228's |
| the report/record history | `agents/warden.md#"## Role">"That distinction is the whole of the second of them. Until it was"` | #228 holds it |
| the #187 story under the fence rule | `agents/warden.md#"## Report">"That was #187: the report's snippets lived only in a transcript, and the fix"` | #187 |
| the first-user story under the terminal lines | `agents/warden.md#"## Report">"The field's first user hit exactly that and had nothing to read. Neither line"` | the shape example stays; the story goes |
| §2's missing-copy history | `skills/agent-contract/SKILL.md#"## §2 Narrow and often; the broad gate is one act with one owner">"This rule sat in two agent definitions in near-identical words, and a third"` | #107 |
| §6's former shape | `skills/agent-contract/SKILL.md#"## §6 You return a report">"This section used to carve the exceptions instead — each one named in the"` | git history of the file |
| §7's #30 story | `skills/agent-contract/SKILL.md#"## §7 A probe is named `test_tmp_*`, one file, run once, deleted">"The file half is what a reviewer did follow, to the letter, during #30's"` | #30 |
| §9's 128-edit measurement | `skills/agent-contract/SKILL.md#"## §9 Edits go through the `Edit` tool">"across 47 files, and a column insertion that silently did not happen because"` | the why-sentence keeps the mechanism (a missed pattern exits zero); the number is in `skills/implement/SKILL.md` §2's own story until #940 |

Sentence-level removals inside a rewritten section are the rewrite itself: `survivor-check` reads every sentence a range removed and refuses one still standing elsewhere, the phase record's rule census names each rule's new coordinate, and the suite shows the agent still does what the rules say. The second copy of each of phase 1's four shared-enforcer pairs becomes a link and is not removed. A test pin dropped with its sentence is an `overview.md` divergence row naming the module and the literal.

## Open questions → questions.md

Framed 2026-10-14 by framer, before the build.
