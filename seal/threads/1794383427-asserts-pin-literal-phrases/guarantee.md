# Guarantee: 1794383427-asserts-pin-literal-phrases

The sealer audited `58c9748fd` against `dbed1d5ff`, the commit that
`release/v0.37.4@{upstream}` and `origin/release/v0.37.4` both resolve to.
The local `release/v0.37.4` resolves to `18a7e18fb`, which is stale, and
this audit does not use it.

Step 1 holds. `trail/gate.md` names the run `1b26a3287 against dbed1d5ff`.
`1b26a3287` is an ancestor of HEAD. The one commit after it, `58c9748fd`,
touches only `frame/questions.md` and `trail/gate.md` of this work item
(executed: `git log --no-merges --name-only 1b26a3287..HEAD ^dbed1d5ff`).

Step 2 holds. `seal pr-body <item> --body <scratchpad>/1794383427-asserts-pin-literal-phrases/pr-body.md --check`
exits 0, and the part above the heading is `pr.md` byte for byte (executed).
No `pr.<lang>.md` is owed, because both language keys of `seal/config.json`
read English. No `seal/parity.json` stands, so no legacy comparison is owed.

Every re-run below ran in a `git clone --no-local` of the worktree at
`58c9748fd`, under `<scratchpad>/1794383427-asserts-pin-literal-phrases/sealer/`.
The tree under audit was not changed. Each mutant was applied with `Edit`
in that clone and restored with `git checkout`, and `git status --short`
was clean after the restore (executed).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The listing at `18a7e18fb` gives 696 asserts, 151 of them absence asserts, and after the build gives 434 and 21 | `changelog.md` *The counts* table; `trail/phases/phase-5.md` *The counts* | design *The listing* script, `python3 -I listing.py <tree>`, over `tests/text` and `tests/behaviour` written out of `18a7e18fb` with `git show`, and over the clone at HEAD | holds: `comparisons 735 asserts 696 absence asserts 151 cases 342 modules 72` at `18a7e18fb`, and `comparisons 455 asserts 434 absence asserts 21 cases 263 modules 66` at HEAD (executed) |
| The issue's two forms give 388 and 134 at `18a7e18fb`, and 287 and 16 after the build | `changelog.md` *The counts* table | the two `git grep -E` commands of design *The counts*, at `18a7e18fb` and at HEAD | holds: 388 and 134, then 287 and 16 (executed) |
| Kept absence: `/tmp/run.txt` absent from `skills/verify/SKILL.md`, restored by fix pass 1 | `trail/rounds/round-1.md` finding 1's close block; `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:206` | the case is green at HEAD; with `/tmp/run.txt` planted in *Capture once, filter locally.* it is run again with `bin/test -q` | holds: red on `:206`, the absence assert itself (executed) |
| Kept absence: `` `.git/seal/` `` absent from the Bootstrap section, restored by fix pass 1 | the same close block; `tests/behaviour/test_first_setup_asks_once.py:109` | the same, with `` `.git/seal/` `` planted in the **local** option of `skills/implement/bootstrap.md` | holds: red on `:109` (executed) |
| Kept absence: `seal stamp --from` absent from `agents/sealer.md` | `trail/phases/phase-3.md` *Absence asserts kept*; `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:341` | the same, with `seal stamp --from` planted in the sealer's *Never* bullet on a stamp | holds: red on `:341` (executed) |
| Kept absence: `persist-credentials` absent from the `dist` checkout, re-ruled on #1486's text | `trail/phases/phase-5.md` *The rulings*; `tests/behaviour/test_a_release_publishes_its_note.py:198` | the same, with `persist-credentials: false` planted in the checkout's `with:` in `.github/workflows/publish-release.yml` | holds: red on `:198` (executed) |
| Cut literal: `exits 0` in the contribution guide's table | `trail/phases/phase-4.md` *Mutation*; `tests/behaviour/test_the_contributor_has_a_procedure.py:130` | the same, with `exits 0` rewritten to `passes` in `CONTRIBUTING.md:74` | holds: red on `:130` (executed) |
| Fix pass 1 kept `release/vX.Y.Z` in the `::error::` line of the hygiene step | `trail/rounds/round-1.md` finding 2's close block; `tests/behaviour/test_the_release_check_watches_what_ships.py:197` | the same, with `release/vX.Y.Z` taken out of `.github/workflows/hygiene.yml:108` | holds: red on `:197`. The six mutants together gave 6 failed and 32 passed. Each failure is the named case on its own assert line (executed) |
| Each check line resolves (S4) | every phase record's S4; `trail/rounds/round-2.md` *Probes* | `bin/seal rules --check` | holds: exit 0, "all 177 check lines in 69 rule files hold." (executed) |
| `## Rule changes` parses, and each `from` stands in its section (S8) | design G14; round 2 *Probes* | `rule_changes.parse(design, "docs")` from a `test_tmp_` probe; `grep` for each `from` in its file | holds: 6 operations, 0 errors, 0 unread. Each `from` stands at HEAD, for example `docs/layout/the-pact.md:39` inside *When there is a pact at all* (executed) |
| No file outside `seal/threads/` names a removed case or helper (S5, and the issue's *Done when* "No `check:` line names a deleted case") | phase records S5; round 1 *Probes* | a probe listing each top-level function, class and module constant of the two directories at `dbed1d5ff` that is gone at HEAD, 117 names, then `git grep -n -w -F <name> HEAD -- . ':!seal/threads'` on each | holds: three names have hits, `KEEP`, `offenders` and `uncovered`. Each hit is a local name of another module or the fixture string in `tests/test_conftest.py`, as `trail/phases/phase-4.md` S5 says (executed, then read) |
| The old-roots module keeps `tracked`, `lines_naming_the_second_root` and #1059's three cases (S6) | design *Scope* item 5; `trail/phases/phase-4.md` S6 | `grep -n '^def '` on the module; `grep -c -w` of each removed unit | holds: those five functions stand, and none of the nine removed names occurs in the module (executed) |
| Removes row: the `check:` line after **Three failed fixes stop the work.** is gone | design `## Removes`; `changelog.md` *Changed*, third bullet | `git diff dbed1d5ff HEAD -- skills/implement/SKILL.md`; `sed -n 242,256p` | holds: the line is removed, and no `check:` line stands in that paragraph (executed) |
| Removes row: the script docstring no longer cites a removed case | `changelog.md` *Changed*, third bullet; `trail/phases/phase-1.md` | `git diff dbed1d5ff HEAD -- .github/scripts/release_completeness_check.py` | holds: the sibling sentence is gone (executed) |
| Removes row: the citation of `#uncovered` at `tests/behaviour/test_both_editions_carry_the_same_folds.py:94` | design `## Removes` | `sed -n 90,98p` on the file | holds: the docstring states its own `unread` (read) |
| Removes rows due at the settle: the check-line targets on `docs/layout/one-root-by-lifetime.md:29` and its Korean edition, `docs/forms/the-round-record.md:107` and `docs/running/the-broad-gate.md:33`, and the line at `docs/layout/the-pact.md:39` | design `## Removes`, the rows marked "at the settle" | the parse above; `grep -n` of each line | holds as a pending operation: each line stands today, and `## Rule changes` holds its operation. The rows promise the settle, not this tree (executed) |
| Removes row 1: each removed absence assert held text or a design a shipped release removed, and no rule of that text itself forbids its literal. Round 2 left to the sealer the 129 removals it weighed on the line alone | design `## Removes` row 1; `trail/rounds/round-2.md` *Not judged* | `git diff dbed1d5ff HEAD -- tests/text tests/behaviour`, filtered to removed lines holding `not in` (141 lines), then 8 opened in their case at `dbed1d5ff` and their text searched for a rule of its own: `anything under seal/` and `seal/threads` (`tests/text/test_a_segment_feeds_the_flow_log.py:391`, `:398`), `\| Mode \|` and `first Bash call` (`tests/text/test_the_mode_is_a_row_and_a_command.py:47`, `:58`), `a root in local mode` and `Local mode is refused` (`tests/text/test_settle_reads_before_it_removes.py:186`, `:189`), `CHANGELOG.md` (`tests/behaviour/test_release_hygiene.py:1081`), `rule 8` (`tests/behaviour/test_a_probe_that_commits_says_so.py:25`) | holds for the sample. Each literal is a former sentence, row, path or citation, and `grep` finds no rule in its own text that names it (`skills/update/SKILL.md` names no `CHANGELOG`, and no agent definition names `rule 8`). The sample was chosen by judgment and is disjoint from round 2's twelve. The other 121 lines were not opened by the sealer (executed for the list, read for the eight) |
| The broad gate passed at `1b26a3287` | `trail/gate.md`; `frame/questions.md` Q1 Status | read only; the sealer runs nothing broad (rule 2) | `read`: the record names the run. The Q1 cell's "5773 passed" stands in the gate's output, not in `trail/gate.md`, which holds only the run line |
| The suite beyond the cases re-run here | phase records S9; round 2 *Not judged* | not re-run | `unverified` by the sealer; answered by the orchestrator's broad gate, whose record is above |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Each listed assert's case is read whole. A fact of four kinds is kept with a comment and cut to the fact. Wording goes. An absence of what a shipped release removed goes, except where a rule of that text itself forbids the literal there. The old-roots scan goes, and six `## Rule changes` reach `docs/` at the settle | the issue's *Change*: it keeps facts a reader acts on, and removes absences of removed designs. The tree: 3 such absences stand with a rule of their own text cited (`/tmp/run.txt`, `` `.git/seal/` ``, `seal stamp --from`), and the fold at `5416a887c` states that exception at design `:157`, `:159`, `:161`, `:238` and plan `:24` (read) | none. The exception for a rule of that text itself narrows the issue's second sentence. The design argues it in plan A14, and `pr.md`'s second quote puts it before the owner. That is the framer's design choice, and the sealer does not re-judge it |
| the build | Five phase records and fix pass 1 give 320 kept, 239 removed and 106 not ruled of 666, plus 19, 1 and 1 on #1486's text. 59 cases are removed, and no module is deleted | `changelog.md`; the counts re-taken above; the mutants above; `gaps.md`. `routing.md` reads `crafter`, and each of the five phases with a commit in `frame/plan.md` *Phases* has its `trail/phases/phase-N.md` (read) | none that bears on the tree. `trail/phases/phase-1.md:229` says five literals were mutated and names seven. Round 1 named that and opened no finding (read) |
| the last round | Round 2: two `should` findings, both located in this work item's records. It confirms the fix pass's rulings and the counts at HEAD, and it leaves the 129 removed absences to the sealer | Finding 1, `fixed 5416a887c`: the three statements now carry the exception the finding's paste asked for, at design `:157` and `:238` and plan `:24` (read at HEAD). Finding 2, `fixed 65407e62a`: plan `:82` cites `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* (read at HEAD). Both commits touch only `frame/design.md` and `frame/plan.md` of this work item (executed, `git log --name-only`) | none |
| the changelog | the counts table, the 320, 239 and 106 ledger, 59 removed cases, the old-roots scan gone, the six settle operations, one `check:` line and one docstring corrected | the counts re-taken above. 106 + 70 + 13 per phase sums to the round's 315, 237 and 113. Fix pass 1's 3 kept and 4 removed of the seven, and its 2 restored absences, give 320, 239 and 106 (read). The `exits 0` and `` `git -C` `` cut literals hold, and `exits 0` was mutated above | none |
| the orchestrator's part of the pull request body | `Closes #1488.` and five quotes of the frame, each with a coordinate | the five quotes stand word for word at `frame/design.md:159` and `:161`, and `frame/plan.md:84`, `:83` and `:81` (read). `routing.md` *Why this way* gives grounds for a tests-only change, and the diff outside `seal/threads/` is test modules under `tests/text/`, `tests/behaviour/` and `tests/github/`, one script docstring and one `check:` line of `skills/implement/SKILL.md`, which the grounds describe (executed, `git diff --name-only`) | none |

```seal
target: 58c9748fd against dbed1d5ff
Verdict: sealed
```
