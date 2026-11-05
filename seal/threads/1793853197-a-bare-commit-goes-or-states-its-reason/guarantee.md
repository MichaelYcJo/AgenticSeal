# Guarantee: 1793853197-a-bare-commit-goes-or-states-its-reason

This run audits 34f93a4a against 703ab88c. The base `release/v0.32.4`
resolves through `release/v0.32.4@{upstream}` to 703ab88c (executed),
which is not an ancestor of HEAD; the merge base is still 31558c76, the
commit the phase records number their lines at. `trail/gate.md`'s last
block names the run at 9de1ab25, an ancestor of HEAD (`git merge-base
--is-ancestor`, exit 0), and `git log --no-merges --name-only
9de1ab25..HEAD ^703ab88c` lists 34f93a4a alone, which touches
`trail/gate.md` alone (executed). `seal pr-body <item> --body pr-body.md
--check` exited 0 (executed). The issue body was read with `gh issue view
1359` (executed). `seal/parity.md` is not tracked (executed), so no
`original:` line is owed.

The earlier run withheld at eee494edc (its block stands last but one
below). This run re-runs the claims whose coordinates a commit since
eee494edc touched: the module docstring of
`tests/text/test_a_moved_rule_leaves_its_definition.py`,
`trail/phases/phase-1.md` row 78 and its Q1 bullet, `frame/design.md` D1
row 36 and the new `frame/plan.md` judgment row. The rows of the earlier
run on coordinates no later commit touched (phase 2's reds, the 44
rewritten tokens, the counts, S2, S3) are carried from that run and not
re-run here. The base moved from c17433966 to 703ab88c in the meantime, so
this run also read the tree the pull request merges into.

Every probe ran in a scratch clone of this repository at 34f93a4a, under
the session's scratchpad, and the tree under audit was not changed. The
clone was removed after its runs.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Rule 9's body pasted into `agents/proofer.md` as a paragraph, or under a `###` heading, leaves the four named modules green; only a paste under a new `##` heading is caught there, by the `## ` heading list (#957) | `tests/text/test_a_moved_rule_leaves_its_definition.py:8-14`, written by the fix pass 5e2718cf (`trail/phases/phase-1.md` row 78, G) | in the clone, `agents/proofer.md` rewritten four ways by a script that asserts each write: unchanged, rule 9's body under `### What rule 9 states`, as a bare paragraph, and through the module's own `paste_back` (`## What rule 9 states`); for each, one `pytest -q` over `test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`, `test_every_agent_reads_the_contract` and `test_the_agent_contract_holds_the_universal_rules`, and one over this module (executed) | holds. The four: 52 passed at exit 0 unchanged, under `###` and as a paragraph; 1 failed, 51 passed at exit 1 under `##`, the failure `test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract[agents/proofer.md]` on "the `## ` headings are (..., '## Rules', '## What rule 9 states'), not (..., '## Rules')". This module: 189 passed at exit 0 unchanged, 3 failed and 186 passed at exit 1 in each of the three shapes |
| The fix pass's figures: 52 passed under `###` and as a paragraph, exit 1 under `##`, this module 3 failed in all three shapes and 189 passed with nothing planted | `trail/phases/phase-1.md`, the Q1 bullet for row 78 | the same runs (executed) | holds: each figure matches |
| The heading list entered at 2fc33333 under #957 on 2026-10-18, after the 2026-09-03 measurement, so the presence-check sentence belongs to the time phases 1 and 2 wrote | `tests/text/test_a_moved_rule_leaves_its_definition.py:13-16`; phase 1 row 78; `frame/design.md` D1 row 36 | `git log --follow -S'headings are' -- tests/text/test_every_agent_reads_the_contract.py`; `git log --follow --diff-filter=A` on the contract modules (executed) | holds: 2fc33333, 2026-10-18; `test_every_agent_reads_the_contract.py`, `test_the_agent_contract_holds_the_universal_rules.py` and this module were added at 438cffe4, 2026-09-03 |
| The plan's judgment row cites the assertion that failed in the `##` probe | `frame/plan.md` *Judgments of the run*, row 2 | read `tests/text/test_every_agent_reads_the_contract.py:136-138` (read) | holds: `:138` is `assert shape_problems(read(path)) == [], name(path)` |
| The fix range adds no commit outside `seal/` | round 2 *Confirmations*, the last row | `git diff -U0 7b03f3aa HEAD -- . ':(exclude)seal/'`, the `+` lines' 7-to-40-hex tokens (executed) | holds: none |
| Each `## Removes` row stands nowhere in the tree | `frame/design.md` *Removes* | `git grep -lF` at HEAD outside `seal/` for "12,819", "37580460950", "the sealer, at", "Proofer round 1 on", "green at 6137faf8", "the frame's shapes", "Measured 2026-09-03", "e51fd0b", "81 passed, exit 0" and "A bare commit is not read" (executed); each hit read | holds for every row but the last: "the frame's shapes" and "Measured 2026-09-03" stand only in other files' sentences, none holding a hex token, and the moved-rule module holds neither. The layout's exemption at `docs/layout/the-record-layout.md:165` stands, and its row says it lands through `## Rule changes` at the settle |
| The chain holds at HEAD | `trail/rounds/round-2.md`, `trail/gate.md` | `python3 skills/code-review/scripts/chain_check.py --baseline 31558c76 --root <worktree> --worktree` (executed) | holds: exit 0 |
| The tree case passes on the tree the pull request merges into. Round 1 found that the siblings' added lines held no bare commit "in this clone" and said "the tree case should therefore pass on the merged tree"; the design's *Scope* says "The sibling work items' sentences. None holds a token" | `trail/rounds/round-1.md` *Confirmations*, the siblings row, at base c17433966; `frame/design.md` *Scope* and *Grounding*, the siblings row | in the clone, `git merge --no-edit 703ab88c` (exit 0, no conflict), then `pytest -q -p no:xdist tests/behaviour/test_chain_hooks_hardening.py tests/text/test_a_cited_commit_outlives_the_squash.py` (executed) | does not hold: exit 1, 1 failed and 44 passed. `test_every_cited_commit_outlives_the_squash` refuses `tests/behaviour/test_chain_hooks_hardening.py:443 cites 3538fd59`. The line is 703ab88c's `:445`, "Seen red at `3538fd59`, whose passages named none of them", added by #1382's squash. `git for-each-ref --contains 3538fd59` names only #1382's local feature branch and no `main` or release ref (executed); the remote holds that branch no more (`git ls-remote`, executed), so a fresh clone does not resolve it and passes, while this repository's own clone refuses it |
| The broad run passed at 9de1ab25 against 703ab88c | the pull request body, the orchestrator's part, the broad run paragraph; `trail/gate.md` | read `trail/gate.md`, the run's output in the session's scratch `gate2.log`, and `skills/verify/scripts/broad_gate.py` near `worktree add` (read) | the record names the run (read). The gate ran the suite on HEAD's tree and checked the base out apart only to compare failures, so it did not run the merge with 703ab88c. Its counts, 6,398 passed and 12 skipped, were not re-run and are `unverified` here; the orchestrator's `seal gate --record` answers them |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1 row 36 now states the split: a paragraph or `###` paste leaves the four green, a new `##` heading is caught by #957's list, and the presence-check sentence belongs to the time phases 1 and 2 wrote; *Scope* says the sibling work items' sentences hold no token | the module at HEAD and the probes above (executed); the issue's dispositions and *Out of scope* | the base: 703ab88c, #1382's squash, added a bare commit at `tests/behaviour/test_chain_hooks_hardening.py:445`, so a sibling's sentence now holds a token this work's class covers |
| the build | phase 1 row 78 quotes the new docstring and its Q1 bullet records the three pastes; phase 2 is unchanged since the earlier run | the module at HEAD word for word (read) and every figure of the Q1 bullet (executed) | none at HEAD |
| the last round | round 2 at 022242a0, no finding; it re-ran the three pastes and read the records against the docstring | the build and the tree on every claim it opened (executed above) | none on its range. It read the fix range and not the moved base, and round 1's forecast that the tree case passes on the merged tree was made against c17433966 |
| the changelog | "No test, workflow or script comment names a commit by its bare hash any more, and a bare hash outside `seal/` that names a commit no `main` or release branch holds is refused" | HEAD's own tree: no rewritten token stands but as data (carried from the earlier run), and the module docstring now holds (executed) | the tree it ships into: once merged into `release/v0.32.4`, `tests/behaviour/test_chain_hooks_hardening.py:445` names 3538fd59 bare, and the case it describes refuses that line in this repository's clone (executed) |
| the orchestrator's part of the pull request body | the figures, `Closes #1359`, the departure from #1355's D2, round 1, the sealer's withholding at 7b03f3aa, the fix pass and round 2, the broad run line | the changelog, `trail/rounds/round-1.md`, `trail/rounds/round-2.md`, the earlier `guarantee.md`, `trail/gate.md` and `gate2.log` (read) | none of its own: its broad run line names HEAD and the base as the run printed them, and it claims nothing of the merged tree |

```seal
target: eee494edc against c17433966
Verdict: withheld reason: the build's rewrite at `tests/text/test_a_moved_rule_leaves_its_definition.py:8-11` (phase 1 row 78, G) says in the present that contract rule 9's body pasted into `agents/proofer.md` under a new heading leaves `test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`, `test_every_agent_reads_the_contract` and `test_the_agent_contract_holds_the_universal_rules` all green, but at HEAD the module's own `paste_back` (a new `## What rule 9 states` heading) turns `test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract[agents/proofer.md]` red at `tests/text/test_every_agent_reads_the_contract.py:138` on the `## ` heading list; the four stay green only under a `###` heading or as a paragraph; every other claim sampled holds
```

```seal
target: 34f93a4a against 703ab88c
Verdict: withheld reason: the changelog's "No test, workflow or script comment names a commit by its bare hash any more" and the design's *Scope* "The sibling work items' sentences. None holds a token" do not hold for the tree this pull request merges into: the base 703ab88c (#1382's squash) added `tests/behaviour/test_chain_hooks_hardening.py:445`, "Seen red at `3538fd59`", a commit only #1382's feature branch holds, and HEAD merged with 703ab88c fails `tests/text/test_a_cited_commit_outlives_the_squash.py::test_every_cited_commit_outlives_the_squash` on that line in this repository's clone (executed; the broad run at 9de1ab25 ran HEAD's tree, not the merge); the line is this work's class, a P clause, and the branch has to take in 703ab88c to remove it; every claim re-run at HEAD holds, the moved-rule docstring that the earlier run withheld on among them
```
