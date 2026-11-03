# Guarantee: 1793661729-each-document-is-cut-by-who-opens-it

| Field | Value |
|---|---|
| Broad gate | 0ebcd944d against 95cbd99a4 |

This run audits 180869b7f, after the verdicts against b3872b934,
361aafb82, 5645d2d62 and be9b962d5 below. The base `release/v0.30.0`
resolves through `origin/release/v0.30.0` to 95cbd99a4 (executed).
`trail/gate.md`'s last block names the run at 0ebcd944d, an ancestor of
HEAD (`git merge-base --is-ancestor`, exit 0), and `git log --no-merges
--name-only 0ebcd944d..HEAD ^95cbd99a4` lists b3872b934, 0f252679f,
361aafb82, c103c7224, 5645d2d62, 17662adf4, be9b962d5, f1986c942
(`guarantee.md`) and 180869b7f (`frame/plan.md`), every path under the work
item's directory (executed). `git diff --stat 0ebcd944d HEAD -- ':!seal/'`
prints nothing (executed), so the tree the first run re-ran its `seen red`
sample and its `## Removes` check against is the tree at HEAD, and this run
re-runs only the claims whose coordinates f1986c942 and 180869b7f touched:
the row `frame/plan.md:100`, and the orchestrator's part of the pull request
body, whose withhold and commit lines changed with them. `seal pr-body <item>
--body pr-1312.md --check` exited 0, from the installed plugin and
from the tree's `bin/seal` (executed). The issue body was read again; it was
last updated 2026-11-02T23:44:15Z, before the first run (executed).
`seal/parity.md` is not tracked (executed), so no `original:` line is owed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| 180869b7f removes the row's diagnosis of the withholds and changes nothing else | the spawn prompt (a claim); `frame/plan.md:100` | `git diff --name-only be9b962d5 HEAD`; `git diff --word-diff be9b962d5 HEAD -- frame/plan.md` | holds: the paths are `frame/plan.md` and `guarantee.md` (f1986c942); the one change is the removed sentence "The changelog figures both verdicts name were written from a phase record's moment rather than from the base and HEAD.", which the verdict against be9b962d5 named |
| "the second sealer withheld on that count alone, with the two files named (`guarantee.md`, the verdict against 361aafb82)" | `frame/plan.md:100` | read `guarantee.md`'s verdict block against 361aafb82 | holds: it names the "one docstring" count alone, with `chain_check.py` and `test_the_rules_have_one_owner.py` |
| "the fix is one phrase in a record" | `frame/plan.md:100` | `git show 5645d2d62 --word-diff -- changelog.md` | holds: "one docstring," becomes "two docstrings, `skills/code-review/scripts/chain_check.py`'s and one test's," at `changelog.md:9` |
| "`git diff --stat b1880c1db 361aafb82 -- ':!seal/'` lists exactly those two `.py` files beside the READMEs, the cut skills and the record layout (executed)" | `frame/plan.md:100` | the same command | holds: `README.md`, `README.ko.md`, `docs/layout/the-record-layout.md`, five files under `skills/implement/` and `skills/settle/`, and the two `.py` files `skills/code-review/scripts/chain_check.py` and `tests/text/test_the_rules_have_one_owner.py` |
| "The sealer spawned after 5645d2d62 reads this correction" | `frame/plan.md:100` | read the verdict block against 5645d2d62 | holds: that run audited 5645d2d62 and wrote "the changelog now holds" |
| No other record states an account of the withholds that 180869b7f left behind | `frame/plan.md`, `changelog.md`, `trail/` | `grep -rn -i -E 'withh\|phase record.s moment\|three times\|twice'` over the work item's directory but `guarantee.md`; read `frame/plan.md` *Judgments of the run* | holds: the hits are three uses of "twice" in phase records about other things; the four judgment rows hold no other account of the withholds; row 99's "the withheld verdict against b3872b934" names a verdict that stands |
| `tests/test_censuses.py` and `tests/text/test_the_record_is_written_in_words.py` pass after 180869b7f | the spawn prompt (a claim) | `.venv/bin/python -m pytest -q tests/test_censuses.py tests/text/test_the_record_is_written_in_words.py >/dev/null 2>&1; echo $?` | holds: exit 0, 179 passed |
| "The sealer withheld four times, each time on the records or on this body's own part, and never on a file outside `seal/`"; the verdicts stand against b3872b934, 361aafb82, 5645d2d62 and be9b962d5; the repairs are 361aafb82, 5645d2d62, be9b962d5 and 180869b7f, each touching only the work item's records | the pull request body, the orchestrator's part, line 11 | read the four verdict blocks; `git show --name-only --format= <c>` for the four repairs, counting paths outside the work item's directory | holds: the verdicts name `changelog.md`, `frame/plan.md` and the body; 0 paths outside for each repair |
| The orchestrator's commits touch only the work item's records: every branch commit whose subject opens with `routing:`, `review:`, `gate:` or `seal:`, and 384e4f1f3, 5645d2d62, be9b962d5 and 180869b7f | the pull request body, the orchestrator's part, line 12 | `git log --no-merges --format=%h --grep='^\(routing\|review\|gate\|seal\):' 95cbd99a4..HEAD`, then `git show --name-only --format= <c>` for those ten and the four named, counting paths outside the work item's directory | holds: 0 for each of the fourteen |
| Round 2's fix touched that record alone | the pull request body, the orchestrator's part, line 10 | `git show --name-only --format= 540cb8515` | holds: `frame/plan.md` alone |
| The body quotes `changelog.md` and `frame/design.md` in their own words | the pull request body, the orchestrator's part, lines 3 and 7-9 | `grep -cF <quote> changelog.md` for the three opening quotes, the preload sentence and the reading sentence; read `frame/design.md:388-389` | holds: each quote is found once; the design's sentence stands across lines 388-389 |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1-D9, unchanged since the first run (no commit since b3872b934 touches `frame/design.md`) | the issue's five items and its boundary paragraph, read again | none |
| the build | phases 1-7, unchanged since the first run; the tree outside `seal/` is the one the first run re-ran its sample against | the design, and the tree on every claim re-run there | none |
| the last round | round 2's one finding, closed `fixed 540cb8515`; `frame/plan.md:99` bounds the proofer at 276 fewer to 1,043 more | the finding and the transcripts, as the second run re-ran them; no commit since 361aafb82 touches `trail/rounds/` or `frame/plan.md:99` | none |
| the changelog | the cut skills' sizes at the base and HEAD, the replay against b1880c1db, and the two docstrings reworded after it | the tree on every figure the earlier runs re-ran; no commit since 5645d2d62 touches `changelog.md` | none |
| the orchestrator's part of the pull request body, and its judgment row `frame/plan.md:100` | the owner's decisions, eleven `## Removes` rows, the preloads, the reading against b1880c1db, two rounds, four withholds and their four repairs, the record-only commits; the row records the orchestrator's own correction of the docstring count, its grounds, and the sealer that reads it | the issue; `changelog.md`'s and `frame/design.md`'s quoted sentences; the four verdict blocks, the commits and the diffs it names (executed) | none: the sentence the verdict against be9b962d5 named is gone, and the row's remaining claims hold |

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

```seal
target: 180869b7f against 95cbd99a4
Verdict: sealed
```
