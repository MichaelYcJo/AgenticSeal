# Guarantee: 1793661729-each-document-is-cut-by-who-opens-it

| Field | Value |
|---|---|
| Broad gate | 0ebcd944d against 95cbd99a4 |

This run audits 361aafb82, after the verdict against b3872b934 below. The
base `release/v0.30.0` resolves through `origin/release/v0.30.0` to
95cbd99a4 (executed). `trail/gate.md`'s last block names the run at
0ebcd944d, an ancestor of HEAD, and `git log --no-merges --name-only
0ebcd944d..HEAD ^95cbd99a4` lists b3872b934 (`trail/gate.md`), 0f252679f
(`guarantee.md`) and 361aafb82 (`changelog.md`, `frame/plan.md`,
`trail/rounds/round-2.md`), all under the work item's directory (executed).
`git diff --stat b3872b934 361aafb82 -- ':!seal/'` prints nothing, and
neither `frame/design.md` nor any phase record changed since b3872b934
(executed), so the claims the earlier run re-ran against the tree stand,
and this run re-runs only those whose coordinates 361aafb82 touched.
`seal pr-body <item> --body pr-1312.md --check` exited 0 (executed).
`seal/parity.md` is not tracked (executed), so no `original:` line is owed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| A framer that follows its citation of the grammar opens 7,564 bytes where it opened 43,170 | `changelog.md:7` | `git show 361aafb82:skills/settle/rule-changes.md \| wc -c`; `git show 95cbd99a4:skills/settle/SKILL.md \| wc -c` | holds: 7564 and 43170 |
| A crafter's whole read of `skills/implement/SKILL.md` is 5,257 bytes smaller | `changelog.md:7` | `git show <c>:skills/implement/SKILL.md \| wc -c` at 95cbd99a4 and 361aafb82 | holds: 30663 and 25406, 5,257 |
| Against b1880c1db the replayed bytes fell 6.5% for the crafter, 2.0% for the framer and 10.0% for the sealer, and did not move for the proofer, over 540 past spawns | `changelog.md:9`; `trail/phases/phase-7.md:351-411` | phase 7's script, copied from `trail/phases/phase-7.md:92-343` into the scratchpad, `python3 -I replay.py <root> 2d38c75af b1880c1db <transcripts>`; deleted | holds: crafter -363,892 (-6.5%), framer -91,437 (-2.0%), proofer +0. The transcripts now hold 545 spawns; the sealer's two new spawns, one of them the earlier run of this audit, add one Read call and move the sealer to -16,198 (-9.9%). Over the 159 sealer spawns the record counts, -16,198 of 162,270 is -10.0% |
| The commits after b1880c1db touch no agent definition | `changelog.md:9` | `git diff --stat b1880c1db 361aafb82 -- agents skills/core skills/agent-contract` | holds: prints nothing |
| The commits after b1880c1db reword a few sentences in the READMEs, the cut skills, the record layout and one docstring | `changelog.md:9` | `git diff --stat b1880c1db 361aafb82 -- ':!seal/'`; `git log --name-only b1880c1db..361aafb82 -- ':!seal/'` | does not hold: ten files, two of them docstrings. d990b38b5 rewords `skills/code-review/scripts/chain_check.py:78-80`, the module docstring; 170372c72 rewords `tests/text/test_the_rules_have_one_owner.py:455-456`, the docstring of `test_the_orchestrators_run_judgments_are_rows_of_the_plan`. The other eight are the two READMEs, five files of the cut skills and `docs/layout/the-record-layout.md` |
| `seal fold` names no document past the ceiling; the largest is about 11,884 tokens where `docs/the-review-record.md` was about 25,387 | `changelog.md:9` | `bin/seal fold`; `wc -c docs/releasing/branch-and-release.md`; `git show 95cbd99a4:docs/the-review-record.md \| wc -c` | holds: 23 documents, 0 past it, exit 0; 23,768 and 50,774 bytes, halved as the fold estimates |
| The proofer's one read over the question-gate paragraph starts at base line 541 and covers 4 of its 14 lines, 276 of its 956 bytes; its total lies between 276 fewer and 1,043 more | `frame/plan.md:99`; `trail/rounds/round-2.md:71` | `git show 2d38c75af:docs/the-review-record.md \| sed -n 531,544p \| wc -lc` and the same over 541-544; a grep of the transcripts for ranged reads of that file at offsets 5xx, and the `.meta.json` of the spawn that read at offset 541 | holds: 14 lines 956 bytes, 4 lines 276 bytes, 7 × 149 = 1,043; the read is `offset 541, limit 103` by an `agentic:proofer` spawn (#1020 round 2) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1-D9, unchanged since the earlier run (no commit since b3872b934 touches `frame/design.md`) | the issue's five items and its boundary paragraph, read again | none |
| the build | phases 1-7, unchanged since the earlier run; the tree outside `seal/` is the one the earlier run re-ran its sample against | the design, and the tree on every claim re-run there | none |
| the last round | round 2's one finding, closed `fixed 540cb8515`; the close block's `answer:` and `frame/plan.md:99` now bound the proofer at 276 fewer to 1,043 more | the finding, which asked that the row name both passages and the nine reads, and does; the transcripts and the base file, re-run above | none |
| the changelog | the cut skills' sizes at the base and HEAD, the replay against b1880c1db, and what came after it | the tree on both sizes, the replay figures, no agent definition touched, `seal fold` and the two token estimates | `changelog.md:9` "reword a few sentences in the READMEs, the cut skills, the record layout and one docstring": two docstrings changed after b1880c1db, `skills/code-review/scripts/chain_check.py:78-80` (d990b38b5) and `tests/text/test_the_rules_have_one_owner.py:455-456` (170372c72) |
| the orchestrator's part of the pull request body | the owner's decisions, eleven `## Removes` rows, the preloads, the reading against b1880c1db, two rounds, the withhold and its repair, seven record-only commits | the issue; `changelog.md:9`'s percentage sentence, quoted word for word; 361aafb82 touching the three records it names and 0f252679f touching `guarantee.md` alone (executed); the other six commits as the earlier run executed them | none; it does not quote the docstring sentence |

```seal
target: b3872b934 against 95cbd99a4
Verdict: withheld reason: three figures do not hold at HEAD; the changelog (`changelog.md:7`) says a framer opens 7,383 bytes where it opened 43,620 (HEAD `skills/settle/rule-changes.md` 7,564, base `skills/settle/SKILL.md` 43,170) and that the crafter's whole read of `skills/implement/SKILL.md` is 5,388 bytes smaller (30,663 to 25,406, 5,257); the changelog (`changelog.md:9`) gives the replay "at its end" as -6.5%, -2.0%, -10.0%, which is b1880c1db, not HEAD (-6.3%, -1.9%, about -9.9%), and the body's *The reading* bullet quotes it; the round-2 fix pass's row (`frame/plan.md:99`) bounds the proofer at 778 fewer to 265 more on a read "over the question-gate paragraph", but that read is base lines 541-643, 276 of the paragraph's 956 bytes, so the bound is 276 fewer to 1,043 more, still under 0.3%
```

```seal
target: 361aafb82 against 95cbd99a4
Verdict: withheld reason: the changelog (`changelog.md:9`, written at 361aafb82) says the commits after b1880c1db reword sentences in "the READMEs, the cut skills, the record layout and one docstring", but they reword two docstrings: `skills/code-review/scripts/chain_check.py:78-80` (d990b38b5) and `tests/text/test_the_rules_have_one_owner.py:455-456` (170372c72); every other figure 361aafb82 wrote holds
```
