# Feature Specification: every agent, skill and doc states the current rule only

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against* | Nothing here asks a person. Growth is declared in the pull request body (`Budget raised:`), read by CI |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The widened checker is a gate: every case seen red, the failure direction stated (it blocks more), a prompt budget of zero, a `Reads:` line per unit, a frame that names what it removes |
| `docs/the-record-layout.md` §*Every kind of record, at a glance*, §*The size a reader takes whole* | A rule has one home and "the copy is the defect"; a file a reader takes whole is ≤ 1,000 lines and 64 KB. This work adds the stricter bound: a file an agent preloads is held to the bytes a rewrite to the shape below reached |
| `docs/the-agent-set.md` §*One contract every agent receives, and one definition each*, §*What a spawn costs* | A definition keeps only its own application; section numbers of the contract are never reused or re-ordered, so the rewrite keeps §1–§17 as headings |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*, §*A claim held by a test* | Released ledger files never change. Every row an edit reaches gets one `Re-read ·` or `Corrected ·` row in `seal/ledger/1791933022-….md`; a row moves onto its test by one `Corrected ·` row when the edit reaches it, never in bulk (the owner's 2026-10-08 answer) |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below; a removal a phase makes that it does not name is a divergence in `overview.md` |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | Ledger rows and the changelog go to this work item's fragments |
| `skills/implement/SKILL.md` §*3. The SDD file set* | The work alters what every spawn reads, which is the top rung |
| `tests/test_no_passage_is_pasted_into_a_second_file.py` (docstring, *Why a ratchet*) | A pair this work drains lowers its `BASELINE` entry on purpose in the same change |
| `tests/test_a_moved_rule_leaves_its_definition.py` (docstring, *Where this draws the line*) | An agent definition may cite a contract section and say what it means for its role; it may not carry the contract's sentences |

## The problem, measured

`executed` at 99176470 (= `origin/release/v0.22.0`, 0.21.1) with the commands in `plan.md` §*Technical context*; #930's checker at 661dc60b run on a copy of this tree with #930's `seal/budgets.md` placed in it.

| What | Value |
|---|---|
| Preload per spawn, agent share (`preload:*`) | framer 99,089 B · smith 106,350 · warden 102,229 · sealer 36,113 · scribe 29,554; plus `CLAUDE.md` 9,261 and `~/.claude/CLAUDE.md` 8,042 in every prefix |
| First-turn prefix in tokens, median over 185 classified spawns of four sessions | sealer 58,386 (38 spawns) · warden 78,624 (81) · framer 83,437 (30) · smith 84,823 (36); fit over the four: 2.79 B/token above a 39,249-token harness share, residual ≤ 3,539 |
| Prose read on demand in a run, median bytes of `agents/`, `skills/`, `docs/`, `templates/` files opened | warden 27,564 (max 310,555) · framer 69,921 · smith 112,015 (max 534,834) · sealer 0 |
| The corpus an agent can read: 68 files | 22,587 lines · 1,500,921 B; `docs/` 19 files 9,911 lines 708,070 B with three at 999/999/1,000 lines; `skills/verify/SKILL.md` 1,020 lines |
| Narrative by #930's marks (outside rule blocks) | 439 lines over 68 files; 250 in `docs/`; 484 lines cite an issue number |
| Narrative by paragraph census (`agents/warden.md`) | 579 lines: 25 bold-led rule paragraphs, 278 lines in paragraphs that open with no rule, 42 lines of fences and tables; the #930 reader counts 43 rule lines because it opens a rule block only on a line that starts with `**`, and an agent's rules are list items |
| How it grew | `agents/warden.md` 164 → 579 lines over 36 commits, +789/−210; 10 of the 35 commits after the first deleted nothing. `agents/smith.md` +666/−235 · `skills/verify/SKILL.md` +1,158/−138 · `docs/round-record-spec.md` +1,035/−35 |
| Restatement debt (the #730 ratchet's `BASELINE`) | warden–smith 153 shared 15-word runs · warden–`code-review/SKILL.md` 53 · warden–`round-record-spec.md` 36 · smith–`implement/SKILL.md` 46; 106 pairs in the table |
| Ledger coupling | 3,354 released rows in 46 files; 837 anchor a prose file (1,127 mentions). `agents/warden.md` 34: 26 on its three section headings, 4 on headings inside its report fence, 4 on quoted lines. `templates/config.md` 151 · `docs/worktree-guard-spec.md` 103 · `skills/implement/orchestration.md` 89 · `skills/verify/SKILL.md` 74 · `CONTRIBUTING.md` 60 |
| Test coupling | 144 of 191 test modules pin at least one sentence (a string literal ≥ 25 characters found verbatim in a prose file; 2,564 hits). `agents/warden.md`: 28 modules, 101 literals (`test_the_rules_have_one_owner.py` 17, `test_broad_gate_rule.py` 11, `test_the_record_is_generated.py` 8, `test_the_reviewers_report_reaches_the_record.py` 8) |

## The shape of a compact file

A file an agent reads holds rules, formats and links, and nothing that narrates.

1. **A rule is one paragraph.** It opens with the rule in bold, in one or two sentences; a list item whose text opens bold is a rule paragraph too. It holds at most one sentence of why. It ends with where the rest lives: `Enforced by: <test node ids>` where a test holds it, and otherwise one link — an issue, a `docs/*.md §*heading*`, or a work item's record at its release tag. Eight live lines is the bar a rewrite is held to by review; a paragraph needing more is two rules or a rule and a story.
2. **A format is a fence or a table**, kept whole: a report skeleton, a command, a row shape. These are what a generator parses, so they are not shortened.
3. **A link replaces a copy.** A rule another file is the home of is one sentence naming the home (`docs/the-record-layout.md` §*Every kind of record, at a glance*). The contract keeps §1–§17 with their numbers; a definition keeps its own application of a section and never its sentences.
4. **No line outside a rule paragraph narrates.** What a rule used to say, which round found it, what was measured and when, who did what — none of it stays. Its homes already exist: git history, the issue the rule cites, the work item's records. A rule whose only grounds were a story keeps the one why-sentence and the link, so the next reader can open the story and the agent never reasons past a rule with nothing under it.

**What a check holds, and how it errs.** Two numbers per file, both rows of `seal/budgets.md` read by `.github/scripts/budget_check.py` on every pull request and by the suite case (#930):

- `bytes:<path>` — the file's bytes, a two-sided ratchet at 2 % slack. An appended paragraph fails it; a rewrite that frees bytes lowers it in the same pull request; a new rule raises it with a `Budget raised:` line. Its ceiling after a rewrite is the number the rewrite reached, which is what makes the shape above the standing bar rather than a hope. It errs neither way on bytes and sees no meaning: a story the same length as the rule it replaced passes, and review's stage 1 against this section is what reads that.
- `history:<path>` — #930's `docs-history` family generalised to every file in scope, ceiling 0 once the file is rewritten. A line outside a rule paragraph, a fence, a comment and a heading that carries `#NN`, `round N`, a date, `measured`, `used to`, `no longer`, `arrived at` or `before this` is a history line. A rule paragraph opens on `**`, `- **`, `* **` or `N. **` and closes at `Enforced by:` or its blank line. It errs over on a link to an issue that sits outside its paragraph, and under on a story that carries none of the marks — 278 of `agents/warden.md`'s lines sit in such paragraphs and the marks find 19.

Together: an append of a paragraph is red on both rows; a rewrite in place at the same size is green; a cut is green once its row is lowered. The paragraph bar, the why-sentence and the link are review's half.

## Scope

**In — this work item.** Measured first (above). The check: the `history` family over `agents/*.md`, `skills/*/SKILL.md`, `skills/*/orchestration.md`, `templates/*.md`, `docs/*.md`, `CLAUDE.md`, `CONTRIBUTING.md` (the 19 `docs-history` rows become `history` rows at the same numbers), the `bytes` family over the same files, the widened marks and the list-item opener, each case seen red. Then the preload set rewritten to the shape, one file per phase, warden's first: `agents/warden.md`, `skills/agent-contract/SKILL.md`, `skills/code-review/SKILL.md`, `agents/smith.md`, `skills/implement/SKILL.md`, `agents/framer.md`, `agents/sealer.md`; `agents/scribe.md` read against the shape and left where it already holds. For each: the ledger rows it drifts re-read or corrected in the fragment, the tests pinning its sentences re-pointed or removed with a row here, the #730 pairs it drains lowered, its `bytes:`, `history:` and `preload:*` rows lowered to what it reached, before and after bytes and tokens in the phase record.

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

**Out, and whose.** The on-demand skills and templates (`skills/verify/SKILL.md` 59,722 B, `skills/evidence-check/SKILL.md` 53,733, the two `orchestration.md` 46,760 and 52,161, `skills/settle/SKILL.md`, `templates/config.md` 41,405, `templates/sdd-round.md` 30,242, `CONTRIBUTING.md`, `CLAUDE.md`) and `docs/` (19 files, 708 KB, ~400 ledger rows): their `bytes:` and `history:` rows land here at today's values, and each file's rewrite is its own work item framed from the targets table in `plan.md` §*The split* — one pull request per heavy file, because a rewrite moves that file's ledger rows and test pins and the review chain caps at the reopening. `skills/writing-style/SKILL.md`: the owner's own style canon, mirrored from `~/.claude/skills/`, which shadows the tree's copy on this machine (26,422 B there); not this item's to cut. `README.md` and `README.ko.md`: read by people, not by a spawn (#755 cluster d). The work item records under `seal/specs/` and the round records a reviewer inherits: history by design, retired by `settle --retire-process`; "records that summarise" (#930 §*Out*) is a different design and a different item. `docs/one-root-by-lifetime.md` and its `.ko.md`: `questions.md` Q1. The test suite's own size and which cases guard nothing: #929. The budgets' mechanism: #930, which this branch builds on.

**The boundary with #929.** A test module is this item's — or the follow-on item's for its file — when it opens a file under `agents/`, `skills/`, `docs/`, `templates/`, `CLAUDE.md` or `CONTRIBUTING.md` and asserts on that file's text; it moves with the text, its pin re-pointed or removed with a row. Every other test is #929's. Where #929 removes a module that also pins prose, #929's removal stands and this item does not plant the pin again.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 an appended paragraph fails | a paragraph citing `#NNN` is appended to `agents/warden.md` after its rewrite; `budget_check.py` runs | exit 1 naming `bytes:agents/warden.md` over its ceiling and `history:agents/warden.md` 1 over 0, with the line number |
| S2 an in-place rewrite holds | a rule paragraph of the same file is reworded in place at the same size, no mark added | exit 0 |
| S3 a cut lowers its row | a rewrite drops a file under its band and the pull request lowers `bytes:<path>` | exit 1 until the row moves, then 0 (#930 S4) |
| S4 every file in scope is held | a new `agents/*.md` or `skills/*/SKILL.md` with no row | held at the family's ceiling (`history` 0; `bytes` the family row's), exit 1 naming the file |
| S5 a list-item rule is a rule block | `- **rule** …` lines in a fixture; the classifier runs | counted rule, not history; the mutation that opens only on `**` turns the case red |
| S6 the widened marks | a fixture line with `used to`, `no longer`, `arrived at`, `before this` outside a rule paragraph | counted history; inside one, not |
| S7 warden's preload reaches its target | phases 2–3 land | `preload:warden` ≤ 53,010 measured by the checker; `history:agents/warden.md` 0; `payload_meter.py --agent warden` before and after in `phases/phase-2.md` and `phase-3.md` |
| S8 no released ledger file changes | every phase | `git diff --stat origin/release/v0.22.0 -- seal/releases seal/ledger.md` empty; every drifted row has a `Re-read ·` or `Corrected ·` row in the fragment; `evidence-check` exit 0 |
| S9 no rule is lost unseen | each rewritten file | the phase record's rule census: every bold-led rule of the old file → its new coordinate, or its `## Removes` row, or an `overview.md` divergence; every test that pinned it green on the new sentence or removed with a row |
| S10 the pairs drained | `agents/warden.md` rewritten | `tests/test_no_passage_is_pasted_into_a_second_file.py` `BASELINE` lowered for the warden pairs in the same commit; the case green |
| S11 the contract keeps its numbers | `skills/agent-contract/SKILL.md` rewritten | `## §1` … `## §17` headings present in order; `tests/test_every_agent_reads_the_contract.py` green |
| S12 nothing asks a person | the whole change | no `AskUserQuestion`, no `input()`, no new prompt; a raise is a body line |
| S13 the `docs-history` rows move with their numbers | phase 1 | 19 `history:docs/…` rows at the 19 ceilings of 661dc60b; the body carries the `Budget removed:` lines the ratchet asks for |

## Data & interfaces

`seal/budgets.md` (from #930) gains the `bytes` family row and its `## File bytes` table (`| File | Bytes ceiling |`), and the `## Docs history lines` table becomes `## History lines` under the `history` family row, both read through `hooks/config.py#gfm_table`. `budget_check.py`: `HISTORY` widened, `rule_lines` opening on a list-item bold lead, a bytes measurer (`measure_bytes`, NAME NOT IN TREE until phase 1), the `bytes` family in `FILE_TABLES`. Ledger rows: this spec's clauses on the checker's units and their tests in `seal/ledger/1791933022-every-agent-skill-and-doc-states-the-current-rule-only.md`, with the `Re-read ·` and `Corrected ·` rows each phase writes.

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
| §9's 128-edit measurement | `skills/agent-contract/SKILL.md#"## §9 Edits go through the `Edit` tool">"across 47 files, and a column insertion that silently did not happen because"` | the why-sentence keeps the mechanism (a missed pattern exits zero); the number is in `skills/implement/SKILL.md` §2's own story until that file's item |

Sentence-level removals inside a rewritten section are the rewrite itself: `survivor-check` reads every sentence a range removed and refuses one still standing elsewhere, and the phase record's rule census names each rule's new coordinate. A test pin dropped with its sentence is an `overview.md` divergence row naming the module and the literal.

## Open questions → questions.md

Framed 2026-10-14 by framer, before the build.
