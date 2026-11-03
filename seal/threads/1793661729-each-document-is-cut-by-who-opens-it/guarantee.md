# Guarantee: 1793661729-each-document-is-cut-by-who-opens-it

| Field | Value |
|---|---|
| Broad gate | 0ebcd944d against 95cbd99a4 |

This run audits 5645d2d62, after the verdicts against b3872b934 and
361aafb82 below. The base `release/v0.30.0` resolves through
`origin/release/v0.30.0` to 95cbd99a4 (executed). `trail/gate.md`'s last
block names the run at 0ebcd944d, an ancestor of HEAD, and `git log
--no-merges --name-only 0ebcd944d..HEAD ^95cbd99a4` lists b3872b934,
0f252679f, 361aafb82, c103c7224 (`guarantee.md`) and 5645d2d62
(`changelog.md`, `frame/plan.md`), every path under the work item's
directory (executed). `git diff --stat 0ebcd944d HEAD -- ':!seal/'` prints
nothing (executed), so the tree the first run re-ran its `seen red` sample
and its `## Removes` check against is the tree at HEAD, and this run
re-runs only the claims whose coordinates c103c7224 and 5645d2d62 touched:
`changelog.md:9`, the new last row `frame/plan.md:100`, and the
orchestrator's part of the pull request body, which changed with them.
`seal pr-body <item> --body pr-1312.md --check` exited 0 (executed). The
issue body was read again; it was last updated 2026-11-02T23:44:15Z,
before the first run (executed). `seal/parity.md` is not tracked
(executed), so no `original:` line is owed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The commits after b1880c1db reword a few sentences in the READMEs, the cut skills, the record layout and two docstrings, `skills/code-review/scripts/chain_check.py`'s and one test's, and touch no agent definition | `changelog.md:9` | `git diff --stat b1880c1db HEAD -- ':!seal/'`; `git diff b1880c1db HEAD -- skills/code-review/scripts/chain_check.py tests/text/test_the_rules_have_one_owner.py`; `git diff --stat b1880c1db HEAD -- agents skills/core skills/agent-contract` | holds: ten files, the two READMEs, `docs/layout/the-record-layout.md`, five files of the cut skills and the two `.py` files; each `.py` hunk lies inside a docstring (`chain_check.py:79-80`, the module docstring; `test_the_rules_have_one_owner.py:455-456`, `test_the_orchestrators_run_judgments_are_rows_of_the_plan`'s); the third command prints nothing |
| `git diff --stat b1880c1db 361aafb82 -- ':!seal/'` lists exactly those two `.py` files beside the READMEs, the cut skills and the record layout; the fix is one phrase in a record | `frame/plan.md:100` | the same `--stat` at 361aafb82 and at HEAD, and `git diff 361aafb82 5645d2d62 -- ':!seal/'` | holds: the same ten files at both commits, nothing outside `seal/` changed after 361aafb82; the changelog diff replaces "one docstring" with "two docstrings, `skills/code-review/scripts/chain_check.py`'s and one test's" |
| The second sealer withheld on that count alone, with the two files named | `frame/plan.md:100` | read `guarantee.md`'s verdict block against 361aafb82 | holds |
| "Both withholds were a changelog figure written from a phase record's moment" | `frame/plan.md:100` | read `guarantee.md`'s verdict block against b3872b934 | does not hold for the first withhold: besides three changelog figures it named `frame/plan.md:99`'s bound on the proofer, a figure in a judgment row that the round-2 fix pass wrote, not a changelog figure |
| "the second sealer reads this correction" | `frame/plan.md:100` | `git log --format='%h %s' 361aafb82..HEAD`; read the row | does not hold: the same row names the second sealer as the run that withheld against 361aafb82 (verdict committed at c103c7224); the correction is 5645d2d62, after it, and the run that reads it is this one, the third |
| `tests/test_censuses.py`, `tests/text/test_the_record_is_written_in_words.py` and `tests/text/test_the_rules_have_one_owner.py` pass after 5645d2d62 | the spawn prompt (a claim) | `.venv/bin/python -m pytest -q` over the three modules at HEAD | holds: 208 passed, exit 0 |
| The orchestrator's commits touch only the work item's records: 384e4f1f3, 316c608b4, 350048ba0, 2d531a293, 0ebcd944d, b3872b934, 0f252679f, c103c7224 and 5645d2d62 | the pull request body, the orchestrator's part, last bullet | `git show --name-only --format= <c>`, counting paths outside `seal/threads/1793661729-each-document-is-cut-by-who-opens-it/` | holds: 0 for each of the nine |
| 361aafb82's diff touches `changelog.md`, `frame/plan.md` and `trail/rounds/round-2.md` alone; at 361aafb82 the changelog counted one reworded docstring where there are two (c103c7224); 5645d2d62 corrected it | the pull request body, the orchestrator's part, *The sealer withheld twice* | `git log --no-merges --name-only` above; read `guarantee.md` | holds |
| "At b3872b934 on three: two sizes in `changelog.md`, the commit its replay ran against, and a bound in a row of `frame/plan.md` *Judgments of the run* (0f252679f). 361aafb82 repaired all three" | the pull request body, the orchestrator's part, *The sealer withheld twice* | read the sentence against `guarantee.md`'s verdict block against b3872b934 | does not hold: the sentence counts three and names four (two sizes, the replay's commit, a bound), and that verdict names the same four claims: the framer's 7,383 and 43,620 bytes and the crafter's 5,388 bytes at `changelog.md:7`, the replay "at its end" at `changelog.md:9`, and the bound at `frame/plan.md:99` |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1-D9, unchanged since the first run (no commit since b3872b934 touches `frame/design.md`) | the issue's five items and its boundary paragraph, read again | none |
| the build | phases 1-7, unchanged since the first run; the tree outside `seal/` is the one the first run re-ran its sample against | the design, and the tree on every claim re-run there | none |
| the last round | round 2's one finding, closed `fixed 540cb8515`; `frame/plan.md:99` bounds the proofer at 276 fewer to 1,043 more | the finding and the transcripts, as the second run re-ran them; no commit since 361aafb82 touches `trail/rounds/` or `frame/plan.md:99` | none |
| the changelog | the cut skills' sizes at the base and HEAD, the replay against b1880c1db, and what came after it, now two docstrings | the tree on every figure the earlier runs re-ran, and on the ten files and two docstrings after b1880c1db | none |
| the orchestrator's part of the pull request body, and its judgment row `frame/plan.md:100` | the owner's decisions, eleven `## Removes` rows, the preloads, the reading against b1880c1db, two rounds, the two withholds and their repairs, nine record-only commits; the row records the orchestrator's own correction of the docstring count | the issue; `changelog.md`'s quoted sentences; the nine commits and the diffs it names (executed) | the body's "At b3872b934 on three ... 361aafb82 repaired all three" names four claims and counts three; `frame/plan.md:100` "Both withholds were a changelog figure", where the first also named `frame/plan.md:99`'s bound; `frame/plan.md:100` "the second sealer reads this correction", where the second sealer is the run that withheld before the correction and the third reads it |

```seal
target: b3872b934 against 95cbd99a4
Verdict: withheld reason: three figures do not hold at HEAD; the changelog (`changelog.md:7`) says a framer opens 7,383 bytes where it opened 43,620 (HEAD `skills/settle/rule-changes.md` 7,564, base `skills/settle/SKILL.md` 43,170) and that the crafter's whole read of `skills/implement/SKILL.md` is 5,388 bytes smaller (30,663 to 25,406, 5,257); the changelog (`changelog.md:9`) gives the replay "at its end" as -6.5%, -2.0%, -10.0%, which is b1880c1db, not HEAD (-6.3%, -1.9%, about -9.9%), and the body's *The reading* bullet quotes it; the round-2 fix pass's row (`frame/plan.md:99`) bounds the proofer at 778 fewer to 265 more on a read "over the question-gate paragraph", but that read is base lines 541-643, 276 of the paragraph's 956 bytes, so the bound is 276 fewer to 1,043 more, still under 0.3%
```

```seal
target: 361aafb82 against 95cbd99a4
Verdict: withheld reason: the changelog (`changelog.md:9`, written at 361aafb82) says the commits after b1880c1db reword sentences in "the READMEs, the cut skills, the record layout and one docstring", but they reword two docstrings: `skills/code-review/scripts/chain_check.py:78-80` (d990b38b5) and `tests/text/test_the_rules_have_one_owner.py:455-456` (170372c72); every other figure 361aafb82 wrote holds
```

```seal
target: 5645d2d62 against 95cbd99a4
Verdict: withheld reason: the changelog now holds, but the orchestrator's account of the withholds does not; its judgment row (`frame/plan.md:100`) says "the second sealer reads this correction", where the same row names the second sealer as the run that withheld against 361aafb82, before 5645d2d62, and the run that reads the correction is the third; the row says "Both withholds were a changelog figure", where the verdict against b3872b934 also named `frame/plan.md:99`'s bound, a judgment-row figure; and the orchestrator's part of the pull request body (*The sealer withheld twice*) says "At b3872b934 on three" and "361aafb82 repaired all three" while naming four claims, two sizes, the replay's commit and a bound, the four that verdict names
```
