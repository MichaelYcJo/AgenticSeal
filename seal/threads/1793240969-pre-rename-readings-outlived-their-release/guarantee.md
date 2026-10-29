# Guarantee: 1793240969-pre-rename-readings-outlived-their-release

| Field | Value |
|---|---|
| Target SHA | 56a2951a against 1e82fd0a |
| Broad gate | 0c05299a against 1e82fd0a |

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The broad run's record names a commit HEAD follows only through this work item's records | `trail/gate.md:5` | `git log --no-merges --name-only 0c05299a..HEAD ^1e82fd0a`, after `git merge-base --is-ancestor 0c05299a HEAD` exit 0 | holds: one commit follows, 56a2951a, and it touches only `trail/gate.md` (executed) |
| The pull request body above `## Not from the records` is the records' own text | the body file the prompt names | `seal pr-body seal/threads/1793240969-pre-rename-readings-outlived-their-release --body <file> --check`, run before and again after the orchestrator's one-line change | holds: exit 0 both times (executed) |
| S1's case was seen red against the reader at 1e82fd0a, failing at `assert code == 0` | `trail/phases/phase-1.md:30-35` | in a clone at 56a2951a with `chain_check.py` and `routing.py` restored from 1e82fd0a: `bin/test tests/skills/test_chain_check.py tests/hooks/test_routing.py -q -p no:randomly -p no:xdist -k "<S1 case> or <S2 case>"` | holds: exit 1, S1 failed with `assert 1 == 0` at `tests/skills/test_chain_check.py:2978`, the old reader naming the `SpecSeal-Routing:` commit as undeclared (executed) |
| S2's case was seen red against the parser at 1e82fd0a, failing with `assert 'crafter' is None` | `trail/phases/phase-2.md:23-27` | the same run as the row above | holds: S2 failed with `AssertionError: assert 'crafter' is None` at `tests/hooks/test_routing.py:140` (executed) |
| Both cases, S3, S4 and the censuses pass with the branch's code | `trail/phases/phase-1.md`, `trail/phases/phase-2.md`, plan phase rows | in the same clone with the code back at 56a2951a: `bin/test tests/skills/test_chain_check.py tests/hooks/test_routing.py tests/hooks/test_implementer_notice.py tests/test_censuses.py -q` | holds: exit 0, 517 passed (executed) |
| S5: no living file names a removed unit | `frame/design.md` S5 | `git grep -n -e OLD_TRAILER -e OLD_BY_CRAFTER -- ':!seal/threads'` at 56a2951a | holds: exit 1, nothing printed (executed) |
| Every `## Removes` row is gone from the tree: the second `key=`, the docstring words, the module docstring clause, the two `parse` lines, the orchestration sentence, and both old cases | `frame/design.md` `## Removes` | `git diff 1e82fd0a...HEAD -- ':!seal/threads'`, and `git grep -n -e 'under either key' -e 'on one made before the rename' -e OLD_BY_CRAFTER -e 'Implementation \| smith'` | holds: the one hit is S2's own input at `tests/hooks/test_routing.py:136`, under its `# exempt from old_names:` line; `docs/the-routing-check.md:101` stands, as the last row of `## Removes` says it does until the settle (executed) |
| No ref outside `origin/main` carries a `SpecSeal-Routing` trailer, and no `routing.md` on any ref answers `smith` | `frame/design.md` *Scope* | over the 13 local and `origin/` refs: `git log --format='%(trailers:key=SpecSeal-Routing,valueonly)' <ref> ^origin/main`, and `git grep -l -E '^\| *Implementation *\| *smith' <ref> -- 'seal/threads/*/routing.md'` | holds: no trailer value and no file on any ref (executed) |
| Removing the census item for the old key, as the issue's first done-when line asks, would flag the policy sentence this pull request may not edit | `frame/plan.md` Alternatives D, `frame/questions.md` second judgment | in the clone, the item removed through the Edit tool, then `bin/test tests/test_censuses.py -q -p no:randomly` | holds: exit 1, `old_names` flags `docs/the-routing-check.md:101` and `tests/skills/test_chain_check.py:2969`, `:2974`, `:2976`; the clone was removed after (executed). `skills/implement/SKILL.md:75` says a pull request does not edit the policy root (read) |
| 645c9c80 touches the census comment alone, 0c05299a writes Q1's status alone, 5b8fcd02 moves the version alone | `trail/rounds/round-2.md`, the spawn prompt | `git show --stat 645c9c80 0c05299a 5b8fcd02` | holds: `tests/censuses.py`, `frame/questions.md`, `.claude-plugin/plugin.json`, one file each (executed) |
| The broad run printed 6722 passed and 14 skipped | the orchestrator's part of the body | `grep` over the run's log `gate.log` in the scratchpad | holds as the log reads: `BROAD GATE PASSED ... @ 0c05299a against origin/release/v0.24.1 @ 1e82fd0a`, `6722 passed · 14 skipped`, chain exit 0 (read; the run itself is the orchestrator's) |
| The readings Q1 leaves out are #1154 | the orchestrator's part of the body | `gh issue view 1154` | holds: open, and it names the CLAUDE.md block markers and `seal.py#OLD_PLUGIN_CLONE` with the pins and census items `gaps.md` *Not done* names (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Remove `OLD_TRAILER` and `OLD_BY_CRAFTER` with their readers, comments and the orchestration sentence; rewrite the two pins into their opposites; keep the census item and the policy sentence until the settle; leave the other readings out on Q1 | the issue's two readings and its second done-when line; the tree at 56a2951a; the measurement re-run above | the issue's first done-when line on the census item. The tree decides for the design: removing the item turns `tests/test_censuses.py` red on `docs/the-routing-check.md:101`, and a pull request does not edit the policy root (`skills/implement/SKILL.md:75`) |
| the build | e1fc252d and f4d3d4a3 remove both readings and rewrite S1 and S2, each seen red at 1e82fd0a; 645c9c80 rewrites the census comment without a count | the design's `## Removes` and scenarios; the diff; both red runs and the green run above | none |
| the last round | Round 2 confirms round 1's fixed finding at 645c9c80 and its rejected finding, and opens nothing | the diff of 645c9c80; round 1's confirmations of S1 to S5 | none. The rejected finding (the version moved in a commit of its own) is an ordering of commits inside a squashed pull request, and the tree the release branch receives is the same either way |
| the changelog | Two readings removed; the looser verdict for an old trailer and an old answer; no open branch or work item carries either; the block markers and the old clone line stay | the diff; the ref measurement above; `gaps.md` *Not done* | none |
| the orchestrator's part of the pull request body | The version moves to 0.24.1 in a commit of its own, as round 1 records; the left-out readings are #1154; the broad run printed 6722 passed and 14 skipped; closes #1142 | 5b8fcd02's stat; `trail/rounds/round-1.md` finding 2; issue #1154; the run's log and `trail/gate.md` | none |

Verdict: sealed
