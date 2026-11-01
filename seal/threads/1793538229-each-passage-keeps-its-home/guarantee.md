# Guarantee: 1793538229-each-passage-keeps-its-home

| Field | Value |
|---|---|
| Broad gate | e759ff53 against 14bfd992 |

`trail/gate.md`'s last `seal` block names `e759ff53`, an ancestor of HEAD `0d8b7ab8` (`git merge-base --is-ancestor`, exit 0). `git log --no-merges --name-only e759ff53..HEAD ^14bfd992` lists one commit, `0d8b7ab8`, touching only `seal/threads/1793538229-each-passage-keeps-its-home/trail/gate.md`. The base `release/v0.27.3` resolved through `release/v0.27.3@{upstream}` to `14bfd992`. Executed. `seal pr-body seal/threads/1793538229-each-passage-keeps-its-home --body <pr-body.md> --check` exited 0 under both the installed plugin's `seal` and the tree's `bin/seal`. Executed. `chain_check.py --baseline 14bfd992 --root . --sealing` exited 0 at HEAD, and its one line named the guarantee file this audit writes. Executed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S4's case was red against the module at the base, with `Left contains 1 more item: {('agents/a.md', 'agents/b.md'): 1}` | `trail/phases/phase-1.md:17` | In a `git clone --no-local` at `0d8b7ab8` under the scratchpad, `shared_counts` restored to its `14bfd992` body (diff of the function against `git show 14bfd992:<module>` empty), then `.venv/bin/python -m pytest <module> -k two_definitions_share -p no:xdist` | Holds: 1 failed, `Left contains 1 more item`. Executed. Under the base body, `test_no_pair_shares_more_than_it_was_measured_at` also fails, because `BASELINE` no longer holds the definition pairs. That is expected, and the phase record ran its case before `BASELINE` was edited. |
| S3 was red under the mutant `and pair[1]` → `or pair[1]`, failing at `assert named, found` | `trail/phases/phase-1.md:18` | The same clone with that one substitution, then the module run | Holds: `[agents/crafter.md-skills/planted/SKILL.md]` failed at `assert named, found`, and S4's case failed too. Executed. |
| S5: `if count > allowed:` → `>=` turns `test_a_count_over_its_baseline_is_named_and_one_at_it_is_not` red | `trail/phases/phase-1.md:20` | The same clone, filter restored, that one substitution, the module run | Holds: that case failed (with `test_no_pair_shares_more_than_it_was_measured_at`). Executed. |
| S5: `if count > allowed:` → `!=` turns `test_a_removed_copy_passes_without_a_baseline_edit` red at 18 runs where 26 were measured | `trail/phases/phase-1.md:20-22` | The same clone, that one substitution, the module run | Holds: only that case failed, naming `docs/one.md and skills/two/SKILL.md share 18 runs of 15 words where 26 were measured`. Executed. The clone was removed afterwards. |
| The module runs green, 9 passed | `trail/phases/phase-1.md:26` | `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py -p no:xdist -rA` in the worktree at HEAD | Holds: 9 passed, every case listed. Executed. |
| The modules design G12 names stay green | `frame/design.md:20`, S6 | `bin/test` over the module, `test_the_handoff_before_round_one.py`, `test_the_pull_request_language_is_the_repositorys.py`, `test_a_cited_section_stands_in_its_file.py`, `test_a_shrunken_corpus_declines_to_judge.py`, `test_every_agent_reads_the_contract.py` and `test_chain_hooks_hardening.py`, `-q -p no:xdist`, at HEAD | Holds: exit 0, 220 passed. Executed. |
| Only the two `README.md` pairs share a run, and the module holds no passage's text | `frame/design.md` S1 and S2; the issue's *Done when* | An inline `.venv/bin/python -I -c` importing the module at HEAD: `shared_counts(tree())`, and its own source's `windows(words(...))` against each of the 61 corpus texts | Holds: `{('README.md', 'skills/implement/acts.md'): 1, ('README.md', 'skills/implement/SKILL.md'): 2}`; no corpus file shares a run with the module. Executed. |
| The rule change parses, and its `from` stands in *The root records* after the settle `14bfd992` rewrote `docs/the-record-layout.md` | `frame/design.md` S7, P3 | `rule_changes.parse(<design.md text>, "docs")`, `section_lines(<doc>, "The root records")`, then the whitespace-collapsed `from` searched within those lines, at HEAD | Holds: one `change`, `errors=[]`, `unread=[]`; the section stands at lines 341-359 and holds the `from`. Executed. |
| Every `## Removes` row of `frame/design.md` and every removal the changelog names | `frame/design.md:80-92`; `changelog.md:3` | `git grep -n -F` at HEAD, over `agents/crafter.md`, `skills/implement/SKILL.md` and the module, for "each case first, seen red", "different audiences", "whoever comes", "assertion nobody has opened", "reached five documents", "cluster by cluster", "#755", "parity-setup/SKILL.md", "Sanctioned", `"agents/crafter.md", "agents/` and `max(counts`; `BASELINE` printed | Holds: no hit. `BASELINE` holds only the two `README.md` keys at 2 and 1. The one `texts = tree()` left (`:245`) is in the paste case, not in the two ratchet cases the row names. Executed. |
| Each citation lands on a section that states the removed words | `skills/implement/SKILL.md:53-55`, `:161-164`; `agents/crafter.md:45-47` | Read `docs/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read* and `skills/agent-contract/SKILL.md` rule 5 at HEAD; the cited-section module ran in the 220 above | Holds: the docs section gives "Two rows, because one cannot express the middle answer" and the two audiences; rule 5 gives "an assertion nobody has opened" and "aggregate … is not a coordinate". Read, and executed through `test_a_cited_section_stands_in_its_file.py`. |
| Round 2's `fixed 0d248cf2`: the judgment row names its method, calls its list a sample, and files the class | `trail/rounds/round-2.md:41-42`; `frame/plan.md:46` | `git show --stat 0d248cf2`; read `frame/plan.md:46`; `gh issue view 1270 --json title,state` | Holds: `0d248cf2` touched `frame/plan.md` alone. The row carries the round's grounds cell, "the list is a sample of the class", and files #1270, which is open. Executed and read. |
| The suite at `e759ff53`: 6270 passed, 9 skipped | the pull request body's first part | none: the full suite is no agent's to run (contract rule 2) | Unverified. `trail/gate.md` holds a run that `seal gate --record` writes only on success (`skills/verify/scripts/broad_gate.py:88`, read), but not the counts. The orchestrator answers for them. |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | K2.6, K2.8 and K2.9 each keep one home; the count leaves out a pair of two definitions; `BASELINE` keeps the two `README.md` entries; two ratchet cases move to planted texts; one rule change to *The root records* | the issue body's *Scope*, *Rule change* and *Done when*; the diff; the claims re-run above | none |
| the build | Phase 1 delivers *Scope* 1 to 7 at `43eaa555`, with three stated departures (S3 as a parameter, the docstring under *What is counted*, one `DEFINITIONS` constant) | the diff; the design (round 1 read the departures against it); every seen-red claim re-run above | none |
| the last round | Round 2 confirms round 1's fix, keeps `trail/phases/phase-1.md:7` at `79252e48` as a record of what phase 1 read, and finds the judgment row undercounted the class, fixed at `0d248cf2` | the tree at HEAD: `trail/phases/phase-1.md:7` still reads "stand at `79252e48`", and `frame/plan.md:46` holds the rewritten row | none |
| the changelog | Three passages now stand in one file; the paste check no longer counts two definitions; a definition paired with a skill is still refused; `BASELINE` drops from 16 entries to the two `README.md` ones | the diff (`BASELINE` at `14bfd992` holds 16 keys); the design; the issue | none |
| the orchestrator's part of the pull request body | Summarises the change and its folds; says "541e8c5e and 25c268b4 moved every citation to `48d035aa`, the squash on `main`" | the diff, the design, the changelog; #1270 filed; the merge `e759ff53` has parents `f81f1361` and `14bfd992`, and `14bfd992` is the 0.27.x settle (#1269) | the last round and the tree: `seal/threads/1793538229-each-passage-keeps-its-home/trail/phases/phase-1.md:7` still cites the measure at `79252e48`, kept on purpose by round 2 (`trail/rounds/round-2.md:60`), so not every citation moved |

```seal
target: 0d8b7ab8 against 14bfd992
Verdict: withheld reason: the orchestrator's part of the pull request body says "541e8c5e and 25c268b4 moved every citation to `48d035aa`", and the tree contradicts it at `seal/threads/1793538229-each-passage-keeps-its-home/trail/phases/phase-1.md:7`, which still says the measure stands at `79252e48`, kept on purpose by round 2 (`trail/rounds/round-2.md:60`); the sentence must name the citations that moved (the module docstring and `frame/design.md:3` and `:14`) and the one record line that keeps the old commit
```

## Re-audit at 9342ad9c

| Field | Value |
|---|---|
| Broad gate | e759ff53 against 14bfd992 |

`trail/gate.md`'s last `seal` block still names `e759ff53`, an ancestor of HEAD `9342ad9c` (`git merge-base --is-ancestor`, exit 0). `git log --no-merges --name-only e759ff53..HEAD ^14bfd992` lists three commits, `0d8b7ab8` (`trail/gate.md`), `3446cddc` (`guarantee.md`) and `9342ad9c` (`frame/plan.md`), every path under `seal/threads/1793538229-each-passage-keeps-its-home/`. The base `release/v0.27.3` resolved through `release/v0.27.3@{upstream}` to `14bfd992`. Executed. `seal pr-body seal/threads/1793538229-each-passage-keeps-its-home --body <pr-body.md> --check` exited 0 under both the installed plugin's `seal` and the tree's `bin/seal`. Executed. `chain_check.py --baseline 14bfd992 --root . --sealing` exited 0 at HEAD; its two lines named this file as behind HEAD and its verdict as `withheld`, which this block answers. Executed. `git diff --stat 0d8b7ab8 HEAD` lists `frame/plan.md` (one line added, line 47) and `guarantee.md` alone, so the claims of the first audit whose coordinates no commit since touched stand as it re-ran them, and only the ones below are re-run. Executed.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| 541e8c5e moved `frame/design.md:3` and `:14`, and 25c268b4 the module's docstring, to `48d035aa` | the pull request body's first part, line 6 | `git show 541e8c5e`, `git show 25c268b4`, filtered to changed lines; `git grep -n '79252e48\|48d035aa' HEAD` | Holds: `541e8c5e` rewrites `frame/design.md` lines 3 and 14 from `79252e48` to `48d035aa`; `25c268b4` rewrites one docstring line, now `tests/text/test_no_passage_is_pasted_into_a_second_file.py:30`. Executed. |
| `trail/phases/phase-1.md:7` keeps `79252e48` as the record of what phase 1 read, which round 2 judged to stand | the pull request body's first part, line 6; `trail/rounds/round-2.md:60` | `sed -n 7p trail/phases/phase-1.md`; the same `git grep` | Holds: line 7 reads "The measure's row K2 and *Instances K2* stand at `79252e48` as design G6 quotes them", and no other line of the tree outside the round records, the plan row and `guarantee.md` cites `79252e48`. Executed. |
| c1837d28 rewrote *The probes*' interpreter path | the pull request body's first part, line 6 | `git show c1837d28 -- frame/design.md` | Holds: the absolute `.venv/bin/python` path becomes "the main checkout's `.venv/bin/python -I`". Executed. |
| Round 2's `regression: round-1#1` is routed to an ordinary fix pass, taken at 0d248cf2, owing no verifying round | `frame/plan.md:47` (added by `9342ad9c`) | `git show 9342ad9c`; `grep -n regression` over both round records; read `skills/code-review/orchestration.md:102-112` and `:190-202`; `git show --stat 0d248cf2` | Holds: `9342ad9c` touches `frame/plan.md` alone. Round 2's sentence (`trail/rounds/round-2.md:24`) places the defect in how the fold's row was written, the table's ordinary-fix-pass route; round 1 carries no `regression:` line, so the unit had no earlier one; `0d248cf2` touched `frame/plan.md` alone, a records-only fix the section exempts from a verifying round. Executed and read. |
| Round 2's `fixed 0d248cf2` still stands at `frame/plan.md:46` | `trail/rounds/round-2.md:41-42` | `git diff -U0 0d8b7ab8 HEAD -- frame/plan.md`; `gh issue view 1270 --json title,state` | Holds: the diff's one hunk is `@@ -46,0 +47 @@`, so line 46 is as the first audit read it; #1270 is open. Executed. |
| The suite at `e759ff53`: 6270 passed, 9 skipped, as the gate printed | the pull request body's first part, line 7 | none: the full suite is no agent's to run (contract rule 2) | Unverified. The body now attributes the counts to the gate's printed output, not to `trail/gate.md`, which holds the run line alone (read). The orchestrator answers for them. |
| No `seal/parity.md` in git, so no comparison with an original is owed | `agents/sealer.md` step 5 | `git ls-files seal/parity.md` | Holds: nothing listed. Executed. |

### The parties

Read at `9342ad9c`. Every record but `frame/plan.md` and `guarantee.md` is as the first audit read it at `0d8b7ab8`; the issue body was read again with `gh issue view 1231` (last updated `2026-11-01T03:27:41Z`, unchanged).

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | as the first audit read it: K2.6, K2.8 and K2.9 each keep one home; a pair of two definitions is not counted; `BASELINE` keeps the two `README.md` entries; one rule change to *The root records* | the issue body; the diff; the claims re-run in both audits | none |
| the build | as the first audit read it: phase 1 at `43eaa555`, three stated departures | the diff; the design; every seen-red claim the first audit re-ran | none |
| the last round | round 2: round 1's fix confirmed, `trail/phases/phase-1.md:7` kept, the judgment row's undercount `fixed 0d248cf2` | `frame/plan.md:46` at HEAD; `frame/plan.md:47`, which records the finding's route on the round's own sentence | none |
| the changelog | as the first audit read it: three passages in one file each; two definitions no longer counted; `BASELINE` from 16 entries to 2 | the diff; the design; the issue | none |
| the orchestrator's part of the pull request body | the change and its folds; names `frame/design.md:3` and `:14` and the docstring as moved, `trail/phases/phase-1.md:7` as kept; round 2's regression route has a row in *Judgments of the run*; the suite counts are the gate's printed output | the tree (the claims re-run above); round 2 (`trail/rounds/round-2.md:60`); `frame/plan.md:45-47`; the merge `e759ff53` of `14bfd992` | none |

```seal
target: 9342ad9c against 14bfd992
Verdict: sealed
```
