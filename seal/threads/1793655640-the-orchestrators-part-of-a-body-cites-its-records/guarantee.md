# Guarantee: 1793655640-the-orchestrators-part-of-a-body-cites-its-records

| Field | Value |
|---|---|
| Broad gate | 1b44b1b53 against 1854b5e9f |

The audit is of HEAD 8a0591674 against `release/v0.29.0`, resolved as `origin/release/v0.29.0` at 1854b5e9f (`release/v0.29.0@{upstream}` and `release/v0.29.0` resolve to nothing in this clone; executed). `trail/gate.md`'s last block names 1b44b1b53, an ancestor of HEAD, and `git log --no-merges --name-only 1b44b1b53..HEAD ^1854b5e9f` lists ad164954e and 8a0591674, each touching only a path under `seal/threads/1793655640-the-orchestrators-part-of-a-body-cites-its-records/` (executed). `seal pr-body <item> --body <file> --check` exited 0 with the installed plugin's `seal` and with the tree's `bin/seal` (executed).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The S3 search prints nothing after the edit, and printed the three old sentences before it | `trail/phases/phase-1.md:5`, `frame/design.md:55` | `git grep -n -e "기록에 없는 것만" -e "does not restate it" -e "restates no record" <rev> -- skills evals agents templates` at HEAD and at 85a238c6 | holds: at HEAD nothing, exit 1; at 85a238c6 `orchestration.md:369`, `commit-pr-convention/SKILL.md:242`, `outside-the-review.md:28`, exit 0, so the check can fail (executed) |
| The phase's edit of `orchestration.md` is one hunk and leaves #883's paragraph alone | `trail/phases/phase-1.md:24` | `git diff -U0 85a238c6 6b7c9a08e -- skills/code-review/orchestration.md` | holds: one hunk, `@@ -369,2 +369,11 @@` (executed) |
| The narrow run of the modules that open the changed files passes | `trail/phases/phase-1.md:37`, `trail/rounds/round-3.md` *Probes* | `bin/test -q -p no:xdist` over the ten modules round 3 names, at HEAD | holds: 436 passed, exit 0 (executed). The phase's 1349 passed over 40 modules is read, not re-run |
| `ruff check` and `ruff format --check` on `evals/scripts/rule_cases.py` exit 0 | `trail/phases/phase-1.md:37` | `uvx ruff check evals/scripts/rule_cases.py`; `uvx ruff format --check evals/scripts/rule_cases.py` at HEAD | holds: both exit 0 (executed) |
| The rule change parses as one `change` and applies once | `frame/design.md:62` | `rule_changes.parse` over `frame/design.md`, then `apply_op` over `docs/the-review-record.md`, at HEAD | holds: one `Op(kind='change')`, `errors=[]`, `unread=[]`; `from` count 1 to 0, `to` count 0 to 1 (executed) |
| Ten pull requests merged into `release/v0.28.0` state record facts above `## From the records` | `frame/design.md:12` (G4), left to the sealer by `trail/rounds/round-3.md` *Not judged* | `gh pr list --base release/v0.28.0 --state merged --json number,body`, each body cut at the heading and record paths counted; #1287's part read | holds: ten bodies, each naming at least one record path above the fold, and #1287's part states round and design facts (executed). My path pattern counts 1 to 16 where G4 says 2 to 13; G4's count of bodies stands |
| In 0.29.0 the sealer withheld for #1270 and #1289 on a sentence citing a record row that did not hold its fact | `changelog.md:9`, Why cell | `git show 1854b5e9f:seal/threads/<dir>/guarantee.md \| grep -n "Verdict:"` for both directories | holds: `1793599988-a-citation-opens-after-the-squash/guarantee.md:57` and `1793599989-a-release-is-sized-with-no-ceiling/guarantee.md:35` each withhold on a sentence citing a design or plan row that does not hold it (executed) |
| Every `## Removes` row's text stands nowhere in the tree | `frame/design.md:74-81` | `git grep -n -e "names the record's path" -e "기록의 경로를 적는다" -e "기록에 없는 검증만" -e "표에 남는 것은" -e "part does not restate" -e "restates a record" HEAD -- . ':!seal/threads'` | holds: nothing, exit 1 (executed) |
| `trail/gate.md` is written only on a passing run | `frame/questions.md:13`, Q1 `Status` | read `skills/verify/scripts/broad_gate.py:3071-3086` | holds: `write_gate_file` is reached only after `if failures: ... return 1` (read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | *Scope* items 1 to 6: the four points of item 1 rewrite one sentence of *Orchestrator: the pull request opens once the sealer seals*, and "Nothing else in the section changes" (`frame/design.md:33`); four `## Removes` rows | the build on items 1 to 5 and the four removals; the issue's *Done when* (rule in the file read before the part is written, no new check) | the build: e88b42fd6, the fix of round 1 finding 2, also rewrote the repair sentence of that section, which at HEAD ends "Your part stays as you wrote it, except where the repair changed a record that a sentence of your part copies or cites: open that record again, and correct the sentence or its coordinate." (`skills/code-review/orchestration.md:383-386`, read). The orchestrator folded round 1 finding 1 into the frame (`frame/plan.md` *Judgments of the run*, row 1) and did not fold finding 2 |
| the build | the diff 1854b5e9f...HEAD changes `orchestration.md`, `commit-pr-convention/SKILL.md`, `implement/acts.md`, `outside-the-review.md` and a comment in `evals/scripts/rule_cases.py`; the phase record's departures ("attributed to", the colon) | the design's items 1 to 5, the rounds; the base merge 1b44b1b53 resolved no conflict: `git merge-tree --write-tree` of its parents gives its own tree, 51287ad5 (executed) | the design's `:33` and the changelog's count, as the other rows say |
| the last round | round 3 at d28734cf confirms round 2 finding 1 and opens nothing | the build at HEAD; nothing touched outside the work item's records since d28734cf except the base merge (executed: commit file lists) | none |
| the changelog | `### Fixed`: the section "now says four things", and it lists item 1's four points (`changelog.md:3`); the `### Process changes` Change cell names the same rule and nothing else (`changelog.md:9`) | the design's item 1; the Why cell agrees with G4, G6 and the two 0.29.0 withheld blocks (executed above) | the build: neither entry names the repair sentence's new exception at `orchestration.md:383-386`, a change to what the orchestrator does after a withhold |
| the orchestrator's part of the pull request body | the two quotes of `changelog.md` `### Fixed`; prefix grounds (G4); the milestone move; `## Removes`; prompt budget none; three rounds; the base merge; its commits touch only the records except the merge | the records it quotes, word for word; the milestone description's "Moved in on 2026-11-02 (owner) from release: 0.30.0: #1290" (executed: `gh api .../milestones`); round counts and verdicts (read); every non-merge commit outside 6b7c9a08e, e88b42fd6 and 96cc18224 touches only the work item's records (executed); prompt budget per `CONTRIBUTING.md:365` (no question added, read) | none blocking. Two sentences reach past their coordinate in wording and are not contradicted: "one no body kept" cites G4, which says no body of 0.28.0 kept the rule; a sample of the bodies merged into `release/v0.26.0` to `release/v0.29.0` all name record paths above the fold, and #1226's states round facts (executed). "#883's rewrite of another paragraph": #883's af889979c adds four lines to *On the broad run's exit 1 spawn nothing* and changes no existing line (executed), as G11 says "inserts" |

```seal
target: 8a0591674 against 1854b5e9f
Verdict: withheld reason: the design (frame/design.md:33, Scope item 1) says "Nothing else in the section changes", and the changelog (changelog.md:3, ### Fixed) says the section "now says four things" with the Process changes row (changelog.md:9) naming the same four; the tree at skills/code-review/orchestration.md:383-386 also carries a fifth change, made by e88b42fd6 for round 1 finding 2: "Your part stays as you wrote it, except where the repair changed a record that a sentence of your part copies or cites: open that record again, and correct the sentence or its coordinate." Fold round 1 finding 2 into Scope item 1 as finding 1 was folded, and name the repair exception in the ### Fixed entry and the Process changes Change cell; then run seal pr-body again
```

## Re-audit at e53b1ec9b

| Field | Value |
|---|---|
| Broad gate | 1b44b1b53 against 1854b5e9f |

HEAD is e53b1ec9b. `git log --no-merges --name-only 1b44b1b53..HEAD ^1854b5e9f` lists ad164954e, 8a0591674 and e53b1ec9b, each touching only paths under `seal/threads/1793655640-the-orchestrators-part-of-a-body-cites-its-records/`, and `git diff 1b44b1b53 HEAD` outside that directory is empty (executed). The base still resolves as `origin/release/v0.29.0` at 1854b5e9f (executed). `seal pr-body <item> --body <file> --check` exited 0 with the installed `seal` and with the tree's `bin/seal` (executed). e53b1ec9b touched `frame/design.md:33`, `changelog.md:3` and `changelog.md:9`, and committed the block above unchanged. No code changed since the earlier audit, so its re-run claims stand as they were, and only those coordinates were re-run.

### Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The design's quote of the repair clause is the tree's sentence | `frame/design.md:33` | the clause searched in `frame/design.md` and, with line breaks joined, in `skills/code-review/orchestration.md` | holds: one occurrence in each, word for word (executed) |
| The rule change still parses as one `change` after the design's edit | `frame/design.md` `## Rule changes` | `rule_changes.parse` over `frame/design.md` at HEAD | holds: one `change`, `errors=[]`, `unread=[]` (executed) |
| The section now says five things, the fifth being the repair exception | `changelog.md:3` | read against `skills/code-review/orchestration.md:369-386` | holds: the four points of `:369-380` and the exception at `:383-386` (read) |
| The Process changes Change cell names the repair exception | `changelog.md:9` | read against `skills/code-review/orchestration.md:381-386` | holds: "corrected before the sealer's next spawn" names one of the two moments the tree's sentence gives (each later spawn of the sealer and each `gh api -X PATCH`) and contradicts neither (read) |

### The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | *Scope* item 1 now names the repair clause after round 1's finding 2, and then "Nothing else in the section changes" (`frame/design.md:33`) | the build: the section's changes at HEAD are item 1's four points and that clause (read) | none |
| the build | unchanged since the earlier audit; nothing outside the work item's records changed after 1b44b1b53 (executed) | the design, the rounds, the changelog | none |
| the last round | round 3 at d28734cf opens nothing; no round record changed | the build | none |
| the changelog | `### Fixed`: "now says five things", the fifth being the repair exception; the Change cell gains it (`changelog.md:3`, `:9`) | the build and the design's item 1 | none |
| the orchestrator's part of the pull request body | as before, with "one the bodies merged into `release/v0.28.0` did not keep (`frame/design.md` G4)" and "#883's insertion into another paragraph ... (`frame/design.md` G11)" | G4 and G11, which e53b1ec9b did not touch (read); the two `changelog.md` `### Fixed` sentences it quotes still stand word for word in `changelog.md:3` (read); e53b1ec9b touches only the records, so "touch only the work item's records, except that merge" still holds (executed) | none |

```seal
target: e53b1ec9b against 1854b5e9f
Verdict: sealed
```
