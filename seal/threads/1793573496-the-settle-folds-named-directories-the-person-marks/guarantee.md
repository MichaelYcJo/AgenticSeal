# Guarantee: 1793573496-the-settle-folds-named-directories-the-person-marks

| Field | Value |
|---|---|
| Broad gate | bdbb9d416 against 8d39d6f80 |

The base `origin/release/v0.28.0` resolves to `8d39d6f80` here, executed
(`git rev-parse --verify --quiet`). `trail/gate.md` names `bdbb9d416`, an
ancestor of HEAD `2a7ed1249`, and `git log --no-merges --name-only
bdbb9d416..HEAD ^8d39d6f80` names one commit after it, touching
`seal/threads/1793573496-the-settle-folds-named-directories-the-person-marks/trail/gate.md`
alone, executed. The run's counts (6170 passed, 11 skipped) are read from
the orchestrator's output file, not re-run. `seal pr-body` with `--check`
on the body file exited 0 under the installed plugin and under the tree's
`bin/seal`, executed. `chain_check.py --baseline 8d39d6f80 --root .
--sealing` at HEAD exited 0, executed. After the orchestrator rewrote its
part of the body file, HEAD is still `2a7ed1249` with the same one commit
after the gate's, and `seal pr-body` with `--check` exited 0 again under
both, executed; the second verdict block reads that rewritten part.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Every case phase 1 and the fix passes added was red before the change (seen red) | `trail/phases/phase-1.md:55-62`; `trail/rounds/round-2.md` close of finding 1; `trail/rounds/round-4.md` closes | In a `git clone --no-local` of the worktree at `2a7ed1249`, `settle.py` restored from `8d39d6f80`: `pytest tests/skills/test_settle.py -p no:xdist -k '<the 15 new cases and the heading case>'` | Holds, executed: 22 failed, 0 passed. A1 and the heading case on `AttributeError: DOCUMENTS_HEADING`; every `--from` case on argparse's exit 2 |
| The new cases pass at HEAD, and the signature case runs rather than skips | `trail/rounds/round-5.md:108-117` | `bin/test tests/skills/test_settle.py -p no:xdist -q -rs -k '<same selection>'` in the worktree | Holds, executed: 21 passed, none skipped, exit 0 |
| Dropping `--cc` turns the merge cases red | `trail/rounds/round-4.md` close of finding 1; `trail/rounds/round-5.md:24-28` | `--cc` removed from `history`'s arguments in the clone, `-k 'clean_merge or resolved_a_document'` | Holds, executed: both failed |
| Widening the add test to `"A" in status` turns the `AM` case red | `trail/rounds/round-2.md` close of finding 1 | That mutation in the clone, `-k one_parent_lacks` | Holds, executed: failed |
| The `D` arm turned to `if True:` turns the deletion case red | `trail/rounds/round-2.md` close of finding 1 | That mutation in the clone, `-k deletion_is_no_change` | Holds, executed: failed |
| `--root --no-show-signature` hold the walk under the person's log config | `trail/rounds/round-3.md` close of finding 2; `changelog.md:3` | Both flags removed in the clone, `-k 'show_root or show_signature'` | Holds, executed: both failed |
| A run without `--from` prints what it printed before, line for line | design *Scope* item 3; `changelog.md:3` | In the clone, `bin/seal settle --released-at HEAD` with HEAD's `settle.py`, then with `8d39d6f80`'s, and `cmp` of the two outputs | Holds, executed: both exit 0, 325 lines, `cmp` exit 0 |
| `--from` refuses beside `--apply`, under the `seal/` root, a missing path and a path outside the repository, each with exit 2 and one sentence naming the path as read; a directory above the root is accepted | `changelog.md:3`; `skills/settle/SKILL.md` *Directories a person names* | In the clone: `seal settle --from docs --apply`, `--from seal/threads`, `--from nope`, `--from ..`, `--released-at HEAD --from .` | Holds, executed: four exits 2 with the sentences of `settle.py#FROM_*`, and `--from .` exit 0 listing 696 documents, the root's among them |
| Removes: "It asks nobody at any step", "A reference root is history, never input." and the README rows' "asking nobody" and "누구에게도 묻지 않습니다" stand nowhere | `frame/design.md:171-173` | A scan of `skills`, `templates`, `docs`, `README.md` and `README.ko.md` at HEAD, line breaks folded, for "asks/asking/ask nobody", "never input" and "묻지 않" | Holds, executed: every hit left is about another party (the framer, `seal gate`, the first-setup and migration questions, the tagline), except `docs/release-checklist.md:47`, which the design's `change` rewrites at the settle (`frame/design.md:174`) |
| The four `from` values of `## Rule changes` stand in their sections at HEAD | `frame/design.md:44` (P2 at `421e44038`) | Whitespace-collapsed search of each `from` in its file at HEAD | Holds, executed: each found once; the `add`'s section heading found once |
| No citation outside the skill names a step of *The settling session's procedure* by number | `trail/phases/phase-2.md:19-27` | `git grep -n -i -E` for a step number near the procedure or the settle, outside `seal/threads` and the skill | Holds, executed: the one hit, `hooks/lib/config.py:262`, cites `skills/config/SKILL.md` |
| CI at `1ec48bd77` passed on all three platforms | the pull request body's first part; `trail/rounds/round-5.md:100-102` | `gh run view 41366101808 --json conclusion,headSha,jobs` | Holds, executed: `success` at `1ec48bd77`, every pytest leg on ubuntu, macos and windows `success`. The signature case changed after it (`ffb376cfa`), so whether each leg at HEAD signs or skips is `unverified`, answered by the pull request's CI |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `seal settle --from <dir>` lists git's facts about each document and proposes nothing; the session asks two questions before its first edit, proposes, and the person marks; nothing under a named directory is written; A7 has no case (Q1 default (a)); five rows of *The earlier decisions* depart: D1, D2, D3, D4, D6 (`frame/design.md:32-37`) | the issue's *The change* bullets, read as D1 states; the tree at HEAD; the changelog | none of the build's or the changelog's facts. The orchestrator's part of the body states its departures as two |
| the build | `settle.py` gains `--from`, its four refusals, the listing and `history`'s one rule over `--cc` statuses; `SKILL.md` gains steps 1 to 3, *Directories a person names* and the rewritten reference-root paragraph; the README rows and *Reference specs* name `--from` | the design's *Scope* items 1 to 8, re-run above; phase 1's departure to `git diff HEAD`, folded into the design (`frame/design.md:99`) | none |
| the last round | round 5 at `8e6cf41b6`: no finding; confirms round 4's two closes; the full suite and each CI leg's signing are not judged | the build and the re-runs above; its `Not judged` rows are answered by the broad run and by the pull request's CI | none |
| the changelog | the flag, the listing's facts, the merge rule, the refusals, the two questions, the skip of the root's files, a run without `--from` unchanged, the rule changes the next settle writes | the build, re-run above, and the design | none |
| the orchestrator's part of the pull request body, as rewritten after the first verdict | the change; the judgment stays with the session, on design D5 and the core's section; the design's table states a departure with grounds in five of its six rows, D1, D2, D3, D4 and D6, each given in one line; five rounds 4, 1, 2, 2, 0, none `must`; #1283; Q1; its commits; the merge, CI and broad run | the design at `frame/design.md:32-37`, each departure line read against its row's *Builds on or departs* and *Grounds* cells, and D5's row for the judgment bullet; the rounds' severities (every finding `should`), the commits it lists (each touches `plan.md` or `design.md` as said), the merge `bdbb9d416` with no combined diff, #1283's title, the CI run, the gate output | none. The first verdict's point (the departures counted as two) is gone, and the attribution to the owner with no coordinate is gone with it |

The issue's *Done when* closes "A case pins each of these"; the design departs from it for A7 with
`questions.md` Q1 built on default (a), and the body, the changelog and `gaps.md` state that
departure alike, so it is the owner's to read at this pull request and not a disagreement.

```seal
target: 2a7ed1249 against 8d39d6f80
Verdict: withheld reason: the orchestrator's part of the pull request body says "The design names six it builds on or departs from (D1 to D6). Two departures carry grounds", and the design contradicts it at `frame/design.md:32`, `:34` and `:35`, where D1, D3 and D4 each also depart, with grounds, besides D2 and D6; the bullet must name the departures the design states (D1, D2, D3, D4 and D6) or drop the count
```

```seal
target: 2a7ed1249 against 8d39d6f80
Verdict: sealed
```
