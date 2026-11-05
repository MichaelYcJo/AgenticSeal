# Guarantee: 1793853197-a-bare-commit-goes-or-states-its-reason

This run audits eee494edc against c17433966. The base `release/v0.32.4`
resolves through `release/v0.32.4@{upstream}` to c17433966 (executed);
the local `release/v0.32.4` stands at 31558c76, the merge base and the
commit the phase records number their lines at. `trail/gate.md`'s last
block names the run at a0b71874, an ancestor of HEAD (`git merge-base
--is-ancestor`, exit 0), and `git log --no-merges --name-only
a0b71874..HEAD ^c17433966` lists eee494edc alone, which touches
`trail/gate.md` alone (executed). `seal pr-body <item> --body pr-body.md
--check` exited 0 from the installed plugin and from the tree's `bin/seal`
(executed). The issue body and its one comment were read with `gh issue
view 1359 --comments`; the issue was last updated 2026-11-04T15:16:01Z,
before the frame (executed). `seal/parity.md` is not tracked (executed), so
no `original:` line is owed.

Every probe ran in a scratch clone of this repository, checked out at
eee494edc, and the tree under audit was not changed. The clone was removed
after its runs.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| "Without this module, contract rule 9's body pasted back into `agents/proofer.md` under a new heading leaves `test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`, `test_every_agent_reads_the_contract` and `test_the_agent_contract_holds_the_universal_rules` all green." Round 1 left it to this audit (`trail/rounds/round-1.md` *Not judged*, row 1) | `tests/text/test_a_moved_rule_leaves_its_definition.py:8-11`, written by phase 1 (`trail/phases/phase-1.md` row 78, G) | in the clone, `agents/proofer.md` replaced by the module's own `paste_back(read(path), 9)`, which appends `## What rule 9 states` and the rule's body and whose docstring calls it "the orchestrator's mutation of 2026-09-03"; then `pytest -q` over the four named modules (executed) | does not hold: exit 1, 1 failed and 51 passed. `test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract[agents/proofer.md]` fails at `tests/text/test_every_agent_reads_the_contract.py:138`: "the `## ` headings are (..., '## Rules', '## What rule 9 states'), not (..., '## Rules')"; a new `## Editing files` heading failed the same way. That heading check entered on 2026-10-18 (#957, 2fc33333), after the 2026-09-03 measurement the old sentence dated. The same body under a `###` heading, or as a bold-lead paragraph, leaves the four green (52 passed, exit 0, executed) and turns this module red (3 failed, executed). So the present tense holds for a sub-heading and not for a new `##` heading, the one the module's own `paste_back` makes |
| S7 is red against the base's reader | `trail/phases/phase-2.md` *Each case seen red*, S7 | in the clone, the base's module (`git show c17433966:tests/text/test_a_cited_commit_outlives_the_squash.py`) with HEAD's `# --- bare commits` section appended and HEAD's added assertion in `test_no_reaching_ref_judges_nothing`; `pytest -q -k 'bare or no_reaching or names_no_commit'` (executed) | holds: both parameters fail `assert [] == [('docs/a.md', 2, …)]` and `[('hooks/a.py', 2, …)]` |
| S8 is red on its control against the base, and red on its guard with `seal/` taken in | phase 2, S8, and the `seal mutate` row "the `seal/` exclusion" | the same hybrid run; then HEAD's module with `if not rel.startswith("seal/"):` made `if True:` (executed) | holds: against the base, `assert [] == [('docs/a.md', 2, …)]`; with the guard removed, "Left contains 2 more items, first extra item: ('seal/follow-up.md', 2, …)" at `:412`, four lines below phase 2's `:408`, as its record says `fb35d158` moved them |
| S9 is green against the base, and red with resolution removed and with containment removed | phase 2, S9, and the rows "the resolution" and "containment" | the same hybrid run; then HEAD's module with `answer.split()[1:2] == ["commit"]` made `answer`, and separately with `unreached`'s `if not (run.returncode == 0 and run.stdout.strip()):` made `if True:` (executed) | holds: green in the hybrid; red at `:422` with the 12-hex value that names nothing listed, and red at `:422` with the reached commit listed |
| S10 and the skip text are red against the base | phase 2, S10 and "The skip text" | the same hybrid run (executed) | holds: S10 fails `assert outcome == "failed"` (`'passed' == 'failed'`); `test_no_reaching_ref_judges_nothing` fails on "named bare" absent from the base's `NO_REF` |
| The new module passes at HEAD | phase 2, *The phase boundary* | `pytest -q -p no:xdist tests/text/test_a_cited_commit_outlives_the_squash.py` in the clone (executed) | holds: 17 passed, exit 0 |
| The touched test modules pass | phase 1 *S4*; phase 2 *The phase boundary* | `pytest -q -n auto` over the 28 test modules `git diff --name-only 31558c76 HEAD -- 'tests/*.py'` lists, `tests/block_shapes.py` aside, in the clone (executed) | holds: 2,678 passed, 2 skipped, exit 0 |
| No rewritten token stands outside `seal/` but as data | phase 1 *S1*; `changelog.md` | the 44 tokens of phase 1 rows 1 to 85, `git grep -nP '\b(<44>)\b' HEAD -- . ':(exclude)seal/'` (executed) | holds: one line, `evals/behaviour/proofer/seeded-7a8899d5/prompt.md:5`, D1 row 41's data |
| 72 P, 4 G and 9 N lines, 85 in all, in 29 files | `changelog.md`; the pull request body, the orchestrator's part, line 1 | the disposition column of phase 1 rows 1 to 85 counted; `git diff --name-only 665eef15 43b9b1be -- . ':(exclude)seal/'` (executed) | holds: P 72, G 4, N 9; 29 files |
| 34 of the rewritten hashes name a commit no clone holds once squashed | `changelog.md`; the pull request body, line 1; `frame/design.md` *Grounding*, reachability | for each of the 44 tokens, `git rev-parse --verify "<t>^{commit}"`, then `git for-each-ref --contains <sha> refs/remotes/origin` (executed) | holds: 12 resolve nowhere and 22 are contained by no remote ref; the 32 that resolve are 32 distinct commits |
| The 30 data lines keep hashes `main` holds | `changelog.md`; the pull request body, line 1; phase 1 *S1* | M1 at HEAD, `git grep -I -ohP '\b[0-9a-f]{7,40}\b' HEAD -- . ':(exclude)seal/'` through one `git cat-file --batch-check`, then `git merge-base --is-ancestor <sha> origin/main` for each (executed) | holds: 6,454 distinct tokens, 18 commits, all 18 ancestors of `origin/main` |
| No new commit is cited | `frame/design.md` S2 | `git diff -U0 31558c76 HEAD -- . ':(exclude)seal/'`, the `+` lines' 7-to-40-hex tokens resolved (executed) | holds: the added lines hold no such token |
| `.github/workflows/test.yml` and `skills/implement/scripts/seal.py` change comments only | `changelog.md`; `frame/design.md` S3 | `git diff -U0 31558c76 HEAD` of the two files, each `+` and `-` line not opening with `#` listed (executed) | holds: none |
| Each `## Removes` row stands nowhere in the tree | `frame/design.md` *Removes* | `git grep -nF` at HEAD outside `seal/` for "12,819", "37580460950", "the sealer, at", "Proofer round 1 on", "green at 6137faf8", "the frame's shapes", "Measured 2026-09-03", "A bare commit is not read", with the 44-token grep above (executed); each hit read | holds for every row but the last: the hits are other files' sentences. The last row, the layout's exemption at `docs/layout/the-record-layout.md:165-168`, stands, and the row says where it lands: `## Rule changes`, which the settle writes, as `frame/design.md` *Rule changes* and the body's *What departs* say |
| The comment above `UNREADABLE` says what `classify` and `merge` do with a gate's output | phase 1 row 29, N | read `tests/hooks/test_dispatch.py:281-283` against `hooks/dispatch.py#run_gate`, `#classify` and `#merge` | holds (read) |
| The broad run passed at a0b71874 against c17433966 | the pull request body, the orchestrator's part, line 9 | read `trail/gate.md` and the run's output in the session's scratch `gate.log` | the record names the run (read); the run itself was not re-run, so its counts, 6,398 passed and 12 skipped, are `unverified` here and the orchestrator's `seal gate --record` answers them |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | D1: 115 lines take P, G, N or D; D2: the squash case reads bare commits outside `seal/` and refuses the unreached; the layout sentence changes at the settle | the issue's dispositions, *Done when* and *Out of scope*, and its comment asking for a written pattern (M1, M2) | D1 row 36 asks that the defect "stays in the present", which HEAD cannot hold for the module's own paste (row 1 above) |
| the build | phase 1 rewrote 85 lines and listed all 115; phase 2 added the reader inside `cited`, four cases seen red, and the cost | the design, with its two recorded departures; the tree on every claim re-run but one | `tests/text/test_a_moved_rule_leaves_its_definition.py:8-11` states in the present that the paste leaves the four green, and `tests/text/test_every_agent_reads_the_contract.py:138` refuses the paste the same module's `paste_back` makes |
| the last round | round 1 at 8a6aa184, no finding; its *Not judged* hands the moved-rule sentence to this audit | the build on every claim it opened; the tree on the claims re-run above | none: it judged nothing on that sentence and named it unjudged |
| the changelog | 85 lines in 29 files, 72 P, 4 G, 9 N, 34 unreached, 30 data lines `main` holds, comments only in the two non-test files, the new reading and its refusal | the tree on every figure re-run above | "Four held the grounds of a behaviour, which now stand in the sentence": one of the four, phase 1 row 78, states a behaviour HEAD contradicts |
| the orchestrator's part of the pull request body | the same figures, `Closes #1359`, the departure from #1355's D2, round 1 with no finding and one note for the sealer, the broad run line | the changelog, `frame/plan.md` *Alternatives considered* A2, `trail/rounds/round-1.md`, `trail/gate.md` (read), and the figures re-run above (executed) | none of its own; it states no claim on the moved-rule sentence |

```seal
target: eee494edc against c17433966
Verdict: withheld reason: the build's rewrite at `tests/text/test_a_moved_rule_leaves_its_definition.py:8-11` (phase 1 row 78, G) says in the present that contract rule 9's body pasted into `agents/proofer.md` under a new heading leaves `test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`, `test_every_agent_reads_the_contract` and `test_the_agent_contract_holds_the_universal_rules` all green, but at HEAD the module's own `paste_back` (a new `## What rule 9 states` heading) turns `test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract[agents/proofer.md]` red at `tests/text/test_every_agent_reads_the_contract.py:138` on the `## ` heading list; the four stay green only under a `###` heading or as a paragraph; every other claim sampled holds
```
