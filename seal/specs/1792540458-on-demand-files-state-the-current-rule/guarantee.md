# Guarantee: 1792540458-on-demand-files-state-the-current-rule

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md is written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` *The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | e0ce992e9103328640158dc4862d2e697b33c8e1 against b3154f436405182f5a1d486f55b9c879c8d383fd; earlier run: 8e4d1a64 withheld |
| Broad gate | f1c0e1a7 against b3154f43 |

The base `release/v0.22.3` resolves to b3154f43 through `@{upstream}`, and
`git ls-remote origin` gives the same commit for the base and e0ce992e for
the branch (executed). This audit follows `agents/sealer.md` and
`templates/sdd-guarantee.md` as they stand at HEAD, as the spawn prompt
directs, because the loaded plugin copy (0.22.2) writes the older verdict
shape.

This is a re-run. The earlier run at 8e4d1a64 withheld the seal on three
sentences of the pull request body. One commit follows it, e0ce992e, and it
touches the item's `guarantee.md` and `overview.md`. `overview.md` is not a
closing record, so the commit owes a new audit. Nothing outside the item's
directory changed since 8e4d1a64 (executed:
`git diff --quiet 8e4d1a64 HEAD -- . ':(exclude)seal/specs/<item>'`, exit
0). The rows marked *carried* were executed at 8e4d1a64 on a tree that
equals HEAD outside the item's records. The rows re-run here are the body,
read again from the file the prompt names, and the `overview.md` row the
commit changed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Step 1: the broad run is at HEAD, or only the item's records follow it (`executed`) | `broad-gate.md:5` | `git merge-base --is-ancestor f1c0e1a7 HEAD` exit 0; `git log --no-merges --name-only f1c0e1a7..HEAD ^b3154f43` | holds: 8e4d1a64 and e0ce992e follow it, and both touch only `seal/specs/<item>/broad-gate.md`, `guarantee.md` and `overview.md` |
| Nothing but the item's records changed since the earlier run (`executed`) | the earlier `Target SHA` | `git log --name-only 8e4d1a64..HEAD`; `git diff 8e4d1a64 HEAD -- <item>/overview.md`; the `:(exclude)` diff above | holds: one commit; `overview.md` changes one cell, the S13 row's `Chosen` |
| Body line 7 now matches the tree: "`CLAUDE.md` gives the two directions in a short section of its own and names that skill section for the whole statement." (`executed`) | pull request body line 7; earlier run's finding 2 | `sed -n 44,54p CLAUDE.md` | holds: *Repo rule: text an agent or a check reads has one reading* is a section of its own that states the two directions and names `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* |
| Body line 36 now matches the records: cases listed in the phase records and the round-2 record, most seen red by `mutation-check` against the new text, some against the base files before the edit, two lowered `BASELINE` entries seen red one below their count and the rest not mutated one by one (`executed`) | pull request body line 36; earlier run's finding 1 | read `phases/phase-1.md:48-53`, `phase-3.md:356-357`, `phase-9.md:389-393`, `rounds/round-2.md:74,135`; `git show --name-only` for the three fix commits bd1aa449, 1f1dae03 and 0874e5bc | holds: phases 1 and 3 name reds against the tree before the edit; phase 9 names two mutated entries and says the others were not mutated one by one; of the fix commits only 1f1dae03 touches a test (`tests/test_first_setup_asks_once.py`), and round 2's record lists its cases |
| Body line 43 now states the restatement check's direction: "its `BASELINE` entries drop to their measured counts (one from 153 to 18)" (`executed`) | pull request body line 43; earlier run's finding 3 | `grep -n '"agents/smith.md", "agents/warden.md"'` over the module at b3154f43 and at HEAD | holds: 153 at b3154f43, 18 at HEAD |
| The owner kept the framer's and warden's sets over S13, on 2026-10-21 (`read`) | pull request body line 27; `overview.md` S13 row | `git diff 8e4d1a64 HEAD -- <item>/overview.md` | holds as read: the row now reads "shipped over, and reported; kept by the repository owner on 2026-10-21, asked by the orchestrator", which agrees with the body's *By* cell. That the owner gave the answer is the orchestrator's account, recorded there, and no file holds the owner's own words |
| The four `tests` runs at 4ce4daf0, ac92a9e6, 623c771e and 0f7fb366 passed on every leg (`executed`, carried) | pull request body line 37 | `gh run view <id> --json headSha,conclusion,jobs` for 39531314997, 39533477920, 39534663738, 39535133679 | holds: each `completed success` at the SHA named, 13 jobs, every `pytest`, `lint`, `arm-check-grammar` and `durations` job `success`; `release-report` is skipped, and it runs only for a base of `main` (`.github/workflows/test.yml:253`) |
| The broad run: ruff clean, 7393 passed, 13 skipped, chain exit 0 (`read`, carried) | pull request body line 38; `overview.md` *Not verified* | read the orchestrator's `broad-gate.log` beside the body | holds as read: `BROAD GATE PASSED … @ f1c0e1a7 against … @ b3154f43`, the row `uvx ruff check . && uvx ruff format --check . && bin/test -q`, `7393 passed · 13 skipped`, `chain ✓ exit 0`. Not re-run, by `agents/sealer.md` *Never* |
| S13 byte sums per agent at b3154f43 and 493d9816 (`executed`, carried) | `phases/phase-9.md:419-427`; body lines 27 and 35 | `git cat-file -s <rev>:<path>` summed over each set `spec.md` *Data and interfaces* lists | holds: framer 110,562 to 112,603; smith 146,526 to 117,039; warden 76,287 to 78,706; sealer 55,861 to 23,597; orchestrator 105,113 to 100,664, and with both `verify` files 159,334 to 151,600. The body dates them to phase 9's commit |
| Block 1,669 bytes, `CLAUDE.md` 3,066 from 8,524, `skills/verify/SKILL.md` 21,960 from 54,221 (`executed`, carried) | body lines 8 to 10 | `git cat-file -s` at b3154f43 and HEAD | holds at HEAD. No record states 3,066; phases 3 and 9 state 3,049, the size before bd1aa449 rewrote `CLAUDE.md`'s writing rule. `phases/phase-5.md:323` says 54,220 at b3154f43; the tree says 54,221, which the body uses |
| `CLAUDE.md`'s sections are the goal, the tenet, merge method, identifiers and the writing rule (`executed`, carried) | body line 9; `spec.md` Scope 3 | `grep -n '^#' CLAUDE.md` | holds: five `##` headings, those five |
| Five new pins and round 2's clause pin were seen red (`executed`, carried) | `phases/phase-2.md:201-206`, `phase-3.md:356`, `phase-5.md:160-166`, `phase-6.md:422`; `rounds/round-2.md:74` | in an at-base `git clone --no-local` at 8e4d1a64, each changed file restored from b3154f43 and its case run with `bin/test -p no:xdist -q <case>`; for round 2's case, "Except under `no work item`, " deleted from the HEAD template by a script asserting one match; the clone removed after | holds: all six green at HEAD (exit 0) and each exit 1 against the base file or the deletion, on its own assert. Against the base template, round 2's case fails on its paragraph finder instead, so the deletion is the red that holds |
| Phase 9's lowered `BASELINE` holds, and a lowered entry is tight (`executed`, carried) | `phases/phase-9.md:362-393` | the same clone: the module run; then `("agents/scribe.md", "agents/sealer.md")` lowered from 5 to 4 and the module run | holds: 8 passed, exit 0; one below its count exit 1, "share 5 runs of 15 words where 4 were measured" |
| S16: `bin/rules --check` exits 0 (`executed`, carried) | `spec.md` S16 | `bin/rules --check` in the clone | holds: exit 0, "all 244 check lines in 62 rule files hold" |
| S8: the section sign stands only in contract-number citations (`executed`, carried) | `phases/phase-9.md:323-335` | `git grep -n '§' -- 'skills/*.md' 'templates/*.md' CLAUDE.md CONTRIBUTING.md ':!skills/agent-contract'` | holds: 13 lines, the ones phase 9 lists, some at shifted line numbers; no `§*heading*` citation |
| Issue numbers left the rewritten files (`executed`, carried) | `spec.md` Scope 7 | `grep -c '#[0-9]\{2,\}'` at b3154f43 and HEAD | holds: `verify/SKILL.md` 22 to 0, `implement/orchestration.md` 18 to 0, `CONTRIBUTING.md` 11 to 0, `code-review/orchestration.md` 8 to 0, `templates/config.md` 7 to 0; `verify/orchestration.md` keeps #300, #377 and #642 on the grounds of `phases/phase-5.md:213-219` |
| `## Removes`, every row (`executed`, carried) | `spec.md` *Removes* | `git grep` for `specseal:start` in `CLAUDE.md` and `claude_block` outside the records; `ls` of the removed script and module; `grep` of `GENERATED`, the three `CLAUDE.md` rows, verify's headings, the branch bullet and `perf/403`, and the spec template's heading | holds: nothing of any row stands. The ASCII bullet keeps its reason and links *Branch names*; "named with whose" stands once inside the writing rule, where Scope 1 folds it |
| `## Rule changes`: each `from:` line stands in its `docs/` file (`executed`, carried) | `spec.md` *Rule changes* | `git grep -c -F` of each `from:` fragment over `docs/` | holds: one hit in each of the four files named |
| The rewritten files leave each agent no worse at its cases (`unverified`) | `questions.md` Q1; `overview.md` *Not verified* | none: the paid non-inferiority run, not made under Q1's default | no party claims it; the body names it as open, and the repository owner answers it |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | Scopes 1 to 11, Scope 9 amended to drain before `broad-gate --preflight`, S1 at 1,669 bytes, four `## Rule changes` items, the `## Removes` table | the issue body's five owner decisions; the tree on every `Removes` row; the build, through the divergences `overview.md` records | none |
| the build | nine phases at the commits `plan.md` names; S13 holds for the smith, the sealer and the orchestrator and fails for the framer and the warden, which the owner kept; nine divergences in `overview.md` | the tree on every figure and red re-run; the spec through those divergences; the body's decisions table | none on the tree. Two record slips that mislead nobody: `phases/phase-5.md:323` gives 54,220 for 54,221, and `phases/phase-9.md:307-321` gives section 6's heading and moment as phase 9 built them, which round 1's fix replaced and `overview.md` records |
| the last round | round 4 confirms round 3's two fixes and opens nothing; rounds 1 to 3 hold nine, two and two findings, each `fixed` at a named commit | the tree: section 6, the seal README and the questions template read as the rounds confirm; `bin/rules --check` exit 0 | none |
| the changelog | three writing rules; the block at 1,669 bytes with its routing rule and scoped lint rule; one copy; both orchestration halves; the `verify` split at about two fifths of its size; the branch rule; the templates; `CONTRIBUTING.md`; the drain before the broad run | the tree, the spec and the build | none |
| the pull request body | the changes above, the decisions table, the verification table, the gate change with the restatement check's tighter direction, and what is left open | the tree, the phase and round records, `overview.md` and the CI runs, on every claim re-run, the three earlier disagreements included | none |

Verdict: sealed
