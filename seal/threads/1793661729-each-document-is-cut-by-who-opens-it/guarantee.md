# Guarantee: 1793661729-each-document-is-cut-by-who-opens-it

| Field | Value |
|---|---|
| Broad gate | 0ebcd944d against 95cbd99a4 |

This run audits be9b962d5, after the verdicts against b3872b934,
361aafb82 and 5645d2d62 below. The base `release/v0.30.0` resolves through
`origin/release/v0.30.0` to 95cbd99a4 (executed). `trail/gate.md`'s last
block names the run at 0ebcd944d, an ancestor of HEAD, and `git log
--no-merges --name-only 0ebcd944d..HEAD ^95cbd99a4` lists b3872b934,
0f252679f, 361aafb82, c103c7224, 5645d2d62, 17662adf4 (`guarantee.md`) and
be9b962d5 (`frame/plan.md`), every path under the work item's directory
(executed). `git diff --stat 0ebcd944d HEAD -- ':!seal/'` prints nothing
(executed), so the tree the first run re-ran its `seen red` sample and its
`## Removes` check against is the tree at HEAD, and this run re-runs only
the claims whose coordinates 17662adf4 and be9b962d5 touched: the rows
`frame/plan.md:97` and `frame/plan.md:100`, and the orchestrator's part of
the pull request body, which changed with them. `seal pr-body <item>
--body pr-1312.md --check` exited 0 (executed). The issue body was read
again; it was last updated 2026-11-02T23:44:15Z, before the first run
(executed). `seal/parity.md` is not tracked (executed), so no `original:`
line is owed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The version row cites `docs/releasing/branch-and-release.md` *The version is named at the cut* | `frame/plan.md:97` | `grep -n 'The version is named at the cut' docs/releasing/branch-and-release.md`; `ls docs/branch-and-release.md` | holds: the rule opens at line 353 of the moved document; the old path no longer exists |
| "the second sealer withheld on that count alone, with the two files named" | `frame/plan.md:100` | read `guarantee.md`'s verdict block against 361aafb82 | holds |
| "The sealer spawned after 5645d2d62 reads this correction" | `frame/plan.md:100` | `git log --no-merges --name-only 0ebcd944d..HEAD`; read the verdict block against 5645d2d62 | holds: that run audited 5645d2d62 and found the changelog's docstring count holds |
| "The changelog figures both verdicts name were written from a phase record's moment rather than from the base and HEAD" | `frame/plan.md:100` | read the verdict blocks against b3872b934 and 361aafb82; `git show 361aafb82 -- changelog.md`; `git log -1 --format=%s 170372c72 d990b38b5`; for every branch commit, `grep -l <sha>` over `trail/phases/*.md` and `trail/rounds/*.md`; `grep -n -i docstring trail/phases/phase-6.md trail/phases/phase-7.md` | holds for the first verdict's figures (the cut skills' sizes and the replay "at its end"), not for the second's: the "one docstring" count at `changelog.md:9` was written at 361aafb82 about the commits after b1880c1db, and the two that reword a docstring, 170372c72 and d990b38b5, come after the last phase record and are named only in `trail/rounds/round-1.md` and `round-2.md`; no phase record names them or counts a docstring after b1880c1db. The count was a miscount of the range b1880c1db..HEAD, which matches 170372c72's subject, "one case's docstring", and leaves out d990b38b5's |
| `tests/test_censuses.py` and `tests/text/test_the_record_is_written_in_words.py` pass after be9b962d5 | the spawn prompt (a claim) | `.venv/bin/python -m pytest -q tests/test_censuses.py tests/text/test_the_record_is_written_in_words.py >/dev/null 2>&1; echo $?` | holds: exit 0, 179 passed |
| "The sealer withheld three times, each time on the records or on this body's own part, and never on a file outside `seal/`"; the verdicts stand against b3872b934, 361aafb82 and 5645d2d62; the repairs are 361aafb82, 5645d2d62 and be9b962d5, each touching only the work item's records | the pull request body, the orchestrator's part, line 11 | read the three verdict blocks; `git show --name-only --format= <c>` for the three repairs | holds: each verdict names `changelog.md`, `frame/plan.md` or the body; the repairs list no path outside the work item's directory |
| The orchestrator's commits touch only the work item's records: every branch commit whose subject opens with `routing:`, `review:`, `gate:` or `seal:`, and 384e4f1f3, 5645d2d62 and be9b962d5 | the pull request body, the orchestrator's part, last bullet | `git log --no-merges --grep='^\(routing\|review\|gate\|seal\):' 95cbd99a4..HEAD`, then `git show --name-only --format= <c>` for those nine and the three named, counting paths outside the work item's directory | holds: 0 for each of the twelve; the `frame:` commits 7849e7757, 4acbbd215 and 52939d4f5, and 361aafb82 and 44d0f6a09, which no phase or round record names, also list none |
| Round 2's fix touched that record alone | the pull request body, the orchestrator's part, *Rounds* | `git show --name-only 540cb8515` | holds: `frame/plan.md` alone |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1-D9, unchanged since the first run (no commit since b3872b934 touches `frame/design.md`) | the issue's five items and its boundary paragraph, read again | none |
| the build | phases 1-7, unchanged since the first run; the tree outside `seal/` is the one the first run re-ran its sample against | the design, and the tree on every claim re-run there | none |
| the last round | round 2's one finding, closed `fixed 540cb8515`; `frame/plan.md:99` bounds the proofer at 276 fewer to 1,043 more | the finding and the transcripts, as the second run re-ran them; no commit since 361aafb82 touches `trail/rounds/` or `frame/plan.md:99` | none |
| the changelog | the cut skills' sizes at the base and HEAD, the replay against b1880c1db, and the two docstrings reworded after it | the tree on every figure the earlier runs re-ran; no commit since 5645d2d62 touches `changelog.md` | none |
| the orchestrator's part of the pull request body, and its judgment rows `frame/plan.md:97` and `frame/plan.md:100` | the owner's decisions, eleven `## Removes` rows, the preloads, the reading against b1880c1db, two rounds, three withholds and their three repairs, the record-only commits; the rows record the version move and the orchestrator's own correction of the docstring count | the issue; `changelog.md`'s quoted sentences; the verdict blocks, the commits and the diffs it names (executed) | `frame/plan.md:100` "The changelog figures both verdicts name were written from a phase record's moment rather than from the base and HEAD", where the second verdict's figure, the "one docstring" count, was written at 361aafb82 about commits after the last phase record (170372c72, d990b38b5) that no phase record names |

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

```seal
target: be9b962d5 against 95cbd99a4
Verdict: withheld reason: the orchestrator's judgment row (`frame/plan.md:100`, rewritten at be9b962d5) says "The changelog figures both verdicts name were written from a phase record's moment rather than from the base and HEAD", which holds for the figures the verdict against b3872b934 names but not for the one the verdict against 361aafb82 names: the "one docstring" count at `changelog.md:9` was written at 361aafb82 about the commits after b1880c1db, and the two that reword a docstring, 170372c72 and d990b38b5, come after the last phase record and are named only in `trail/rounds/round-1.md` and `round-2.md`, so that count was a miscount of b1880c1db..HEAD, not a figure taken from a phase record's moment; the version row (`frame/plan.md:97`), the rest of row 100, the body's withhold and commit lines, and every other claim re-run hold
```
