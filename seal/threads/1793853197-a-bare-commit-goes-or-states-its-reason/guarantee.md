# Guarantee: 1793853197-a-bare-commit-goes-or-states-its-reason

This run audits a3f1275d against 703ab88c. The base `release/v0.32.4`
resolves through `release/v0.32.4@{upstream}` to 703ab88c (executed), and
703ab88c is now an ancestor of HEAD, merged at a9d9f64a (`git merge-base
--is-ancestor`, exit 0, executed), so HEAD's tree is the tree the pull
request merges into. `trail/gate.md`'s last block names the run at
71374dc4, an ancestor of HEAD (exit 0), and `git log --no-merges
--name-only 71374dc4..HEAD ^703ab88c` lists a3f1275d alone, which touches
`trail/gate.md` alone (executed). `seal pr-body <item> --body pr-body.md
--check` exited 0, through the installed `seal` and through the tree's
`bin/seal` (executed). The issue body was read with `gh issue view 1359`
(executed). `seal/parity.md` is not tracked (`git ls-files`, executed), so
no `original:` line is owed.

The earlier run withheld at 34f93a4a (its block stands last below). This
run re-runs the claims whose coordinates a commit since 34f93a4a touched:
the merge a9d9f64a, the line caab8bc0 removed at
`tests/behaviour/test_chain_hooks_hardening.py:443`, the phase 1 addendum,
`changelog.md`, `gaps.md`, the frame's D1 row 47 and the eight statements
of its totals (9591cb4e, 38cd9881), and rounds 3 and 4. The claims of the
earlier runs on coordinates no later commit touched (phase 2's reds, the
moved-rule docstring's four-module probe, whose inputs `agents/proofer.md`,
`skills/agent-contract/SKILL.md` and the four modules no commit since
34f93a4a changed, executed) are carried and not re-run.

Every probe ran in a `git clone --no-local` of this worktree at a3f1275d,
under the session's scratchpad, whose `refs/remotes/origin/` hold `main`,
the release branches and #1382's feature branch. The tree under audit was
not changed. The clone and the probe's logs were removed after the runs.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The tree case passes on the tree the pull request merges into, now that the branch holds 703ab88c | `trail/phases/phase-1.md`, the addendum's second bullet (17 and 28 passed); `trail/rounds/round-3.md` *Confirmations* | in the clone at a3f1275d, `bin/test -q -p no:xdist tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_chain_hooks_hardening.py tests/text/test_a_moved_rule_leaves_its_definition.py` (executed) | holds: 234 passed at exit 0 |
| The case refuses the line caab8bc0 removed, so the merged tree failed on it and the fix is what turns it green; D2's catch record, "row 47's is one the case itself refused, on HEAD merged with `703ab88c`" | `frame/design.md` *Removes*, the paragraph after the table; D1 row 47; phase 1 addendum, row 116 | in the same clone, `git checkout a9d9f64a -- tests/behaviour/test_chain_hooks_hardening.py` (the line before the fix), then `bin/test -q -p no:xdist tests/text/test_a_cited_commit_outlives_the_squash.py`; then the file restored from a3f1275d (executed) | holds: exit 1, 1 failed and 16 passed, the one refusal `tests/behaviour/test_chain_hooks_hardening.py:443 cites 3538fd59` |
| The removed sentence stands nowhere, and only #1382's local feature branch holds 3538fd59 | phase 1 addendum, row 116 and its first bullet | `git grep -n 3538fd59 -- . ':(exclude)seal/'` at HEAD; `git for-each-ref --contains 3538fd59` (executed) | holds: grep exit 1, no line; the only ref is `refs/heads/docs/1382-the-readme-names-two-of-four-network-places`. HEAD's docstring ends "also names every place in `NETWORK_PLACES`." (read) |
| The merge's added lines outside `seal/` hold two hex tokens, 3538fd59 and the work item id 1790644505, which names no commit; the fix range adds none | phase 1 addendum, the third bullet; round 3 *Confirmations* | `git diff -U0 a9d9f64a^1 a9d9f64a -- . ':(exclude)seal/'` and `git diff -U0 a9d9f64a HEAD -- . ':(exclude)seal/'`, the `+` lines grepped for 7-to-40-hex tokens; `git cat-file -t 1790644505` (executed) | holds: the merge's two tokens and no other; the fix range none; `cat-file` answers "Not a valid object name" |
| M1 on the merged tree lists the same 18 commits as at 43b9b1be | phase 1 addendum, the third bullet | `git grep -I -ohP '\b[0-9a-f]{7,40}\b' -- . ':(exclude)seal/'` at HEAD, then one `git cat-file --batch-check` (executed) | holds: 6,454 distinct tokens, 18 of them commits. M2's 33 was not re-run here and is carried from round 3 (read) |
| None of the 45 tokens of D1 rows 1 to 40 and 47 stands outside `seal/` but as data | `frame/design.md` D1; `changelog.md` | the tokens taken from D1's third column for those rows, then `git grep -nwF -f <list> -- . ':(exclude)seal/'` at HEAD (executed) | holds: 45 tokens, one hit, `evals/behaviour/proofer/seeded-7a8899d5/prompt.md:5`, which holds `15a5ce66` as D1 row 41's data |
| 86 lines in 29 files, the line row 47 adds sitting in a file already among the 29 | `changelog.md`; the pull request body's first paragraph; phase 1 addendum | `git show --name-only` for 43b9b1be and caab8bc0, outside `seal/` (executed) | holds: 43b9b1be changes 29 files, `tests/behaviour/test_chain_hooks_hardening.py` among them, and caab8bc0 changes that file alone. The 31 files of `git diff --name-only 703ab88c HEAD` outside `seal/` are those 29 and the two phase 2 changed (executed) |
| The merge resolved nothing by hand and changed no file of this work item | round 3 *Confirmations*, the merge row | `git merge-tree --write-tree 881fad6d 703ab88c` against `git rev-parse a9d9f64a^{tree}`; `git diff --stat a9d9f64a^1 a9d9f64a -- <item dir>` (executed) | holds: both 29031fa5; the item's diff is empty. The merge changes `tests/text/test_a_moved_rule_leaves_its_definition.py` at lines 25 to 30, 262 and 435, not the docstring at 8 to 19 the earlier runs audited (read) |
| Each `## Removes` row stands nowhere in the tree, the base's lines included | `frame/design.md` *Removes* | `git grep -lF` at HEAD outside `seal/` for "12,819", "37580460950", "the sealer, at", "Proofer round 1 on", "green at 6137faf8", "the frame's shapes", "Measured 2026-09-03", "e51fd0b", "81 passed, exit 0", "A bare commit is not read" and "Seen red at \`3538fd59\`" (executed) | holds for every row but the last, as the earlier run found: "the frame's shapes" and "Measured 2026-09-03" stand only in files no commit since 34f93a4a touched (`git diff --name-only`, empty, executed), and the layout's exemption at `docs/layout/the-record-layout.md` stands, its row landing through `## Rule changes` at the settle |
| The chain holds at HEAD | `trail/rounds/round-4.md`, `trail/gate.md` | `python3 skills/code-review/scripts/chain_check.py --baseline 31558c76 --root <worktree> --worktree` (executed) | holds: exit 0 |
| Round 3's finding 1, `fixed 38cd9881`, was read by round 4 and touched nothing outside `seal/` | `trail/rounds/round-3.md`, finding 1; `trail/rounds/round-4.md` `confirms: round-3#1` | `git diff --name-only 9591cb4e HEAD -- . ':(exclude)seal/'` (executed); the eight statements read at HEAD against round 3's paste-ready text (read) | holds: empty; each statement counts row 47 (D1 heading, D2's 35 of 45, *Scope* item 1's 86, *Removes*' 73, the catch record's 35, the plan's 115 and row 47, "no sibling removes", A2's 35) |
| The broad run passed at 71374dc4 against 703ab88c, 6,403 passed and 12 skipped | the pull request body, the orchestrator's part, the broad run paragraph; `trail/gate.md` | read `trail/gate.md` and the run's output in the session's scratch `gate3.log` (read) | the record names the run and the log prints `BROAD GATE PASSED` at 71374dc4 against 703ab88c with those counts (read). The counts were not re-run and are `unverified` here; the orchestrator's `seal gate --record` answers them. Since the branch holds 703ab88c, the run's tree is the merged tree |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1 adds row 47, `tests/behaviour/test_chain_hooks_hardening.py:445` at 703ab88c, a P line; every statement of D1's totals counts it (86 lines, 73 P, 35 of 45 unreached); *Scope* exempts the siblings' sentences but for row 47's line | the tree at HEAD and the probes above (executed); the issue's dispositions and *Out of scope*; the changelog's figures | none |
| the build | the phase 1 addendum's row 116 removes the whole seen-red sentence, and the rewritten lines are 86, 73 P, in the same 29 files | the tree at HEAD (read), the case's red on the restored line and its green at HEAD, the 29 files (executed) | none |
| the last round | round 4 at d1c2d3f8, no finding, `confirms: round-3#1`; round 3 ran the merged tree and found only the frame's totals | the frame at HEAD (read) and every figure round 3 ran that this run re-ran: 6,454 and 18, the merge's two tokens, the merge-tree equality, the one data hit (executed) | none |
| the changelog | "Eighty-six comment and docstring lines in 29 files", "Thirty-five" unreached, "Seventy-three" P, and a bare hash outside `seal/` that no `main` or release branch holds is refused | the design, the build and the tree (executed above) | none |
| the orchestrator's part of the pull request body | eighty-six lines in 29 files, thirty-five unreached, `Closes #1359`, the departure from #1355's D2, the two withholdings, the merge and fix pass, rounds 3 and 4, the broad run line at 71374dc4 | the changelog, `trail/rounds/round-3.md`, `trail/rounds/round-4.md`, the earlier blocks below, `trail/gate.md` and `gate3.log` (read) | none. It says the fix pass "dropped that clause"; the phase record says the whole sentence went, since both its halves were red evidence, and the sentence is that clause's whole, so the two agree |

```seal
target: eee494edc against c17433966
Verdict: withheld reason: the build's rewrite at `tests/text/test_a_moved_rule_leaves_its_definition.py:8-11` (phase 1 row 78, G) says in the present that contract rule 9's body pasted into `agents/proofer.md` under a new heading leaves `test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`, `test_every_agent_reads_the_contract` and `test_the_agent_contract_holds_the_universal_rules` all green, but at HEAD the module's own `paste_back` (a new `## What rule 9 states` heading) turns `test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract[agents/proofer.md]` red at `tests/text/test_every_agent_reads_the_contract.py:138` on the `## ` heading list; the four stay green only under a `###` heading or as a paragraph; every other claim sampled holds
```

```seal
target: 34f93a4a against 703ab88c
Verdict: withheld reason: the changelog's "No test, workflow or script comment names a commit by its bare hash any more" and the design's *Scope* "The sibling work items' sentences. None holds a token" do not hold for the tree this pull request merges into: the base 703ab88c (#1382's squash) added `tests/behaviour/test_chain_hooks_hardening.py:445`, "Seen red at `3538fd59`", a commit only #1382's feature branch holds, and HEAD merged with 703ab88c fails `tests/text/test_a_cited_commit_outlives_the_squash.py::test_every_cited_commit_outlives_the_squash` on that line in this repository's clone (executed; the broad run at 9de1ab25 ran HEAD's tree, not the merge); the line is this work's class, a P clause, and the branch has to take in 703ab88c to remove it; every claim re-run at HEAD holds, the moved-rule docstring that the earlier run withheld on among them
```

```seal
target: a3f1275d against 703ab88c
Verdict: sealed
```
