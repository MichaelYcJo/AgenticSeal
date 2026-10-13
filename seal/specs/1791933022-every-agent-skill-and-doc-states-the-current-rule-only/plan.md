# Implementation Plan: every agent, skill and doc states the current rule only

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved <date> by <who>, when `smith` was spawned.

## Summary

The check lands first, as two ratchet families over every file an agent reads (`bytes:<path>`, `history:<path>`), built into #930's checker and table so no new step, job or reader is added. Then the warden's preload is rewritten to the shape one file per phase, each phase proving its before and after bytes and tokens, moving the file's ledger rows and test pins, and lowering the file's rows to what it reached. The smith's and the framer's preloads follow the same procedure. Everything an agent reads on demand, and `docs/`, is held at today's numbers here and rewritten by follow-on items framed from the targets table.

## Technical context

Read at 99176470; the checker is #930's at 661dc60b.

- `.github/scripts/budget_check.py` (#930, not yet on `release/v0.22.0`): `FILE_TABLES` maps a family to its per-file table; `rule_lines` opens a block only on a line starting `**`; `HISTORY` is four marks; `docs_lines` globs `docs/*.md`; an unlisted file is held at its family row's ceiling. The suite case `tests/test_a_budget_ratchets.py::test_the_trees_budgets_hold` runs the checker over the real tree, so a lowered row is seen locally before the push. **Phase 1 starts after #930's pull request merges into `release/v0.22.0` and this branch rebases onto it**; until then the frame's numbers come from the checker run on a copy of this tree with #930's `seal/budgets.md` placed in it (exit 0, every row holds).
- `skills/verify/scripts/payload_meter.py --agent <a> --sections` — bytes and estimated tokens per file and section of a preload; `--calibrate` needs a baseline spawn, which is the orchestrator's act (#930 Q2).
- `skills/evidence-check/scripts/evidence_check.py --reverify --checked <date> --into seal/ledger/<id>.md` — writes a `Re-read ·` row for every released row whose coordinate drifted; a row whose heading is gone is `BROKEN` and takes a `Corrected ·` row by hand. So each rewrite keeps its file's section headings (`agents/warden.md`: `## Where you work`, `## Role`, `## Report`, and the report fence's `## Verdicts`, `## Paste-ready fixes`) and the 26 + 4 rows drift rather than break; the 4 quoted-line rows break and are corrected onto the test that holds each claim, or onto the new line.
- `tests/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` — the pair counts; a drained pair's entry is lowered in the same commit. `tests/test_a_moved_rule_leaves_its_definition.py#WINDOW` — the contract's sentences may not appear in a definition.
- `tests/test_every_agent_reads_the_contract.py` — pins the opening paragraph's body sentences of every `agents/*.md`; the rewrite keeps that paragraph. `tests/test_docs_line_wrap.py#COVERED` — 88 columns over the covered files.
- `skills/code-review/scripts/survivor_check.py` — reads every sentence the range removed and refuses one still standing in another file; this is the reader for the sentence-level removals the frame cannot list.
- `skills/settle/scripts/fold_check.py#shape_problems` — the docs statement shape (marker, bold opener, one `Enforced by:`); the rewrite of an agent file borrows the shape without the marker.
- The measurements and their commands, all `executed` at 99176470 from `/private/tmp/…/scratchpad/923/` (scripts `classify_all.py`, `anchors.py`, `pins.py`, `paras.py`, `targets.py`, `spawn_tokens.py`): `wc -lc` over the 68 files; `budget_check.classify` over each; the paragraph census; ledger anchors by `\b(agents|skills|docs|templates)/…\.md#…@` over `seal/ledger.md` and `seal/releases/*.md`; test pins by `ast` string literals ≥ 25 characters found verbatim in a prose file; `git log --numstat --follow` per file; first-turn `usage` of 204 subagent transcripts under `~/.claude/projects/-Users-michael-Documents-GitHub-SpecSeal/{916bffa3,c3cbb402,20f122bc,7cfd1159}/subagents/`, kind read off the prompt's first words, 185 classified and 19 not.

**What breaks in 6 months with the chosen approach.** A rewrite satisfies `history:` by dropping the issue numbers and keeping the story, and `bytes:` by cutting a rule to make room for it; the two numbers then say the file is compact while an agent still reads narrative. What catches it is the review's stage 1 against `spec.md` §*The shape of a compact file* and the rule census each phase writes, and neither is a check. Second: the `Budget raised:` line becomes boilerplate and the preloads creep back one declared raise at a time; the release checklist's trend line (#930 phase 4) is the reader, and if it is not read the ratchet has become a report. Third: the next agent definition is written long because nothing but the family ceiling (`bytes` unlisted at 16,000) bounds a new file, and that ceiling is a number this frame chose.

## Alternatives considered

| Approach | Failure scenario (six months on) | Verdict |
|---|---|---|
| A. Two tree ratchets per file (`bytes`, `history` with widened marks and the list-item opener) in #930's checker; the shape's paragraph bar, why-sentence and link held by review | above | **chosen** |
| B. A diff check: a hunk adding ≥ N lines and deleting none inside an existing section is refused | a moved section reads as an append; deleting one word satisfies it; a legitimate new rule under an old heading is refused and the waiver habit forms, as `SPECSEAL_CASE_CEILING_S=600` did on every 0.21.1 seal; it needs the merge base, so the suite case cannot run it on a worktree | rejected |
| C. Narrative marks alone, no bytes row | a paragraph with no mark grows freely: 278 of `agents/warden.md`'s 579 lines sit in paragraphs that open with no rule, and the marks find 19 | rejected alone; kept as the half that names narrative |
| D. Bytes alone, no marks | the file sits at its ceiling while a story replaces a rule under it; nothing says which half grew | rejected alone; kept as the half that stops an append |
| E. The #730 restatement ratchet alone | it finds copies and not rewordings, by its own docstring; #755 measured 219 copies and 58 paraphrases | kept as is; its pairs lowered as they drain |
| F. A per-paragraph line cap as a gate | lists and tables trip it; an author splits a paragraph to pass; a check on form that reads no meaning becomes a formatting game | rejected as a gate; the 8-line bar is review's |
| G. Strip history lines mechanically, no rewrite | a rule whose grounds were in the story loses its grounds, and the agent reasons past a rule with nothing under it, which is §2's own measured failure ("every reader met a prohibition with nobody in the room") | rejected; the shape keeps one why-sentence and a link |
| H. Every file in one work item | ~837 ledger rows and 144 test modules move in one pull request; the review chain caps at its reopening and the run ends with the rewrite half-reviewed; #822's 67 rows for one rename were the largest finding class of its cycle | rejected; the split below |
| I. Move the narration into one history file or `docs/experiments/` | a second corpus nobody reads, which the one-home rule then governs; git history and the issues already hold every story, by their number | rejected |
| J. Tokens as the unit | #930 alternative E: a tokenizer upgrade moves every number with no file changed | rejected there; bytes, with the fit stated once in `spec.md` |
| K. Rewrite the docs first | a `docs/` file is read on demand by a session, a preload by every spawn: warden's preload is 102 KB on every one of 81 review spawns in four sessions, `docs/worktree-guard-spec.md` was opened in 6 | rejected; preload first |

**How a cut is shown not to lose a rule the agent needed.** Three readers and one honest gap. The rule census in each phase record maps every bold-led rule of the old file to its new coordinate or its `## Removes` row (S9). Every ledger row anchored on the file is re-read against the new text one at a time, and a claim the new text no longer holds is a `Corrected ·` row somebody has to write, which is the moment a lost rule surfaces (S8). Every test that pinned a sentence is green on the new sentence or removed with a row (S7, S10). The gap: nothing measures an agent's behaviour before and after a cut. What the next runs show is in the records they write — a finding class returning in the round records is how a lost rule would be seen — and the ratchet makes re-adding one cost a raise line, not a redesign. `docs/measuring-a-run.md` §*Where a reading goes* is where the segment costs go, so the token saving is a posted number and not this plan's claim.

**CI cost.** No new job or step: the rows ride #930's hygiene step (ubuntu, under a minute) and its suite case (one case, under a second, on the three legs). In a private repository that is ≈ 0.02 Linux-equivalent minutes per run at Windows 2× and macOS 10× — nothing against #929's 292-minute median per pull request (`read` from #930's `plan.md`; prices unverified, #929's). The prose-pin modules this item edits run no longer than they do now; a removed pin is one case fewer.

## The split

Three parts, each landing the check it needs already holding:

| Part | Holds | Order and release |
|---|---|---|
| A — this work item | the check (phase 1); the preload set rewritten (phases 2–5); every other file's rows at today's values | 0.22.0, after #930 merges; the owner's item 2 lands in phase 1 |
| B — the on-demand set | `skills/verify/SKILL.md`, `skills/evidence-check/SKILL.md`, both `orchestration.md`, `skills/settle/SKILL.md`, the small skills, `templates/`, `CONTRIBUTING.md`, `CLAUDE.md`; one work item per heavy file or per group of small ones | 0.22.0 where the release has room after A, otherwise 0.22.1; each framed from the table below |
| C — `docs/` | one work item per heavy file (`review-chain-spec`, `round-record-spec`, `worktree-guard-spec`, `review-handoff-protocol`, `the-evidence-ledger`), one for the rest; Q1 for the `one-root-by-lifetime` pair | 0.22.1; each lowers its `history:` row to 0 and its `bytes:` row to what it reached |

Why: a rewrite's cost is per file (its ledger rows, its test pins, its restatement pairs), so files on separate branches touch separate fragments and separate test modules and do not conflict at the squash; the review chain reads one file's rule census per run; and part A's check is what makes every later part's pull request a lowering the summary shows. The orchestrator files B and C as issues, since an agent posts nothing.

Targets for B and C, from the kept-shape estimate (headings, fences, tables, the first paragraph under each heading and each bold-led paragraph capped at 8 lines; `executed`, `targets.py`), rounded up — the bar each follow-on frame starts from and re-measures: `skills/verify/SKILL.md` 59,722 → 30,000 · `skills/evidence-check/SKILL.md` 53,733 → 30,000 · `skills/implement/orchestration.md` 52,161 → 25,000 · `skills/code-review/orchestration.md` 46,760 → 22,000 · `skills/settle/SKILL.md` 25,437 → 14,000 · `CONTRIBUTING.md` 23,896 → 13,000 · `CLAUDE.md` 9,261 → 6,000 · `templates/config.md` 41,405 → 25,000 · `templates/sdd-round.md` 30,242 → 15,000 (a template's content is its comments, so its estimate is read by hand) · `docs/review-chain-spec.md` 70,140 → 45,000 · `docs/round-record-spec.md` 69,835 → 45,000 · `docs/worktree-guard-spec.md` 74,355 → 35,000 · `docs/review-handoff-protocol.md` 55,638 → 28,000 · `docs/the-evidence-ledger.md` 52,159 → 27,000 · `docs/commit-review-gate-spec.md` 44,198 → 17,000 · `docs/the-pact.md` 34,343 → 15,000 · `docs/branch-and-release.md` 27,016 → 15,000 · `docs/release-checklist.md` 27,564 → 11,000 · `docs/issues-and-milestones.md` 25,081 → 13,000 · `docs/the-record-layout.md` 22,593 → 14,000 · `docs/the-commit-gate-inside-git.md` 23,228 → 10,000 · the eight remaining docs at ≤ 60 % of today; every `history:` row to 0.

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The check, in #930's checker and table: the `history` family replacing `docs-history` over the 68 files (19 rows renamed at their numbers, the family row at 0 for unlisted files, every other in-scope file listed at today's count), the widened marks and the list-item opener, the `bytes` family with its `## File bytes` table at today's bytes (2 % slack, family row 16,000) and its measurer; T1–T6 seen red; the PR body's `Budget removed:` lines; the `docs/the-record-layout.md` §*seal/* row's sentence and `budget_check.py`'s docstring rewritten in place | `budget_check.py` exit 0 on the tree; S1 and S2 probed on a scratch copy against the unrewritten `agents/warden.md` (append → exit 1 on both rows; in-place reword → exit 0); `test_the_trees_budgets_hold` green; numbers in `phases/phase-1.md` | |
| 2 | `agents/warden.md` to the shape at ≤ 12,000 B, headings kept; the 26 + 4 drifted rows by `--reverify --into`, the 4 broken rows corrected; the 28 modules' 101 pins re-pointed or removed with a row; `BASELINE` lowered for the warden pairs; `bytes:agents/warden.md`, `history:agents/warden.md` and `preload:warden` lowered; the rule census (25 rules → new coordinates) and `payload_meter --agent warden` before and after in `phases/phase-2.md` | S1, S2 probed again on the rewritten file; `evidence-check` exit 0; the prose-pin modules green (narrow run, one module each); the checker exit 0 with the three rows at their new values | |
| 3 | `skills/agent-contract/SKILL.md` ≤ 8,000 B with §1–§17 kept, then `skills/code-review/SKILL.md` ≤ 12,000 B; rows, pins and pairs as in phase 2; `preload:warden` ≤ 53,010 | S11; `test_a_moved_rule_leaves_its_definition.py` and `test_every_agent_reads_the_contract.py` green; the checker exit 0; before and after per file in `phases/phase-3.md` | |
| 4 | `agents/smith.md` ≤ 10,500 B and `skills/implement/SKILL.md` ≤ 15,000 B; `preload:smith` ≤ 54,510, `preload:framer` moves with the skill | as phase 3, for the smith's pins (`test_a_phase_hands_the_next_one_a_record.py`, `test_the_rules_have_one_owner.py` rule 5) | |
| 5 | `agents/framer.md` ≤ 9,000 B and `agents/sealer.md` ≤ 7,000 B; `agents/scribe.md` read against the shape and its row left; `preload:framer` ≤ 53,010, `preload:sealer` ≤ 15,000, `preload:scribe` ≤ 17,128 | as phase 3; every `preload:*` row at or under its target in the checker's summary | |
| 6 | The close: the changelog fragment; the ledger fragment with this spec's clauses on the checker's units and their tests (test rows, no hashes); `overview.md`; `questions.md` rows the work answered ticked; the per-agent before/after table (bytes, tokens by the fit) in the changelog fragment for the release's trend line | `evidence-check` exit 0; `chain-check` names no fragment left behind; the hygiene summary at the pushed tip shows every row holding, read by the orchestrator | |

This table is also where the work records how far it got. **Status is empty, or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — the mutation each case kills

| Case | Guards | Mutation it kills |
|---|---|---|
| T1 `test_a_file_bytes_row_holds_the_file_and_an_unlisted_one_the_family` (NAME NOT IN TREE until phase 1) | S1, S3, S4 | the `bytes` measurer off by one; the unlisted file not held |
| T2 `test_a_history_row_counts_every_file_in_scope_not_only_docs` (NAME NOT IN TREE until phase 1) | S4, S13 | the glob left at `docs/*.md`: a fixture `agents/x.md` with a history line passes |
| T3 `test_a_list_item_opening_bold_is_a_rule_block` (NAME NOT IN TREE until phase 1) | S5 | `rule_lines` opening on `**` alone: the fixture's `- **rule** … #999` line counts as history |
| T4 `test_the_widened_marks_count_outside_a_rule_and_not_inside` (NAME NOT IN TREE until phase 1) | S6 | each mark dropped from `HISTORY`, one parametrised case per mark; a mark inside a rule block counted |
| T5 `test_an_appended_paragraph_fails_both_rows_and_a_reword_in_place_holds` (NAME NOT IN TREE until phase 1) | S1, S2 | the fixture tree at its ceilings; the append read as holding, or the reword read as over |
| T6 `test_the_renamed_family_is_read_at_the_old_rows_numbers` (NAME NOT IN TREE until phase 1) | S13 | a `history:docs/x.md` row read as new at 0 rather than at its listed ceiling |

The six names above are planted by phase 1, in `tests/test_a_budget_ratchets.py` beside #930's cases; the `budget_check.py` units this plan names (`FILE_TABLES`, `rule_lines`, `HISTORY`, `docs_lines`) are on #930's branch and resolve here once this branch rebases onto it.

`test_the_trees_budgets_hold` (#930 T13) is the gate's local form for every phase and takes no mutation of its own. Each phase's rewrite is verified by the rows it lowers, the pins it re-points and the ledger run, not by a new case.

## Operational impact

- This branch rebases onto `release/v0.22.0` after #930 merges; `seal/budgets.md` and `budget_check.py` are #930's files edited here, and the ratchet asks for a `Budget removed:` line per renamed `docs-history` row plus one for the family in this pull request's body.
- Every later pull request that edits a file in scope meets two rows per file: a grown file needs its line, a cut one lowers its row. #929's and #931's branches meet `bytes:` rows for the prose files they touch after they rebase.
- No new job, step, dependency or scope; stdlib Python at the floor.
- The preloads change what every spawn reads from phase 2 on. A rule that a rewrite dropped and a later run misses comes back as a raise with its reason in a body line, which is the designed price.
