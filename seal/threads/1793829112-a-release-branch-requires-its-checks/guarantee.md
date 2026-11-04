# Guarantee: 1793829112-a-release-branch-requires-its-checks

Audited at b7bd43d3 against `release/v0.32.1`, which resolves to 3b2190c4 here
(executed: `git rev-parse --verify --quiet 'release/v0.32.1@{upstream}'`). No
earlier `guarantee.md` stood, and `seal/parity.md` is not in git, so no
`original:` line is owed.

`trail/gate.md` names `run: 60f2e40a against 3b2190c4`. 60f2e40a is an
ancestor of HEAD, and the commits after it, cffcd9f5 and b7bd43d3, touch only
`trail/gate.md` and `gaps.md` under this work item's directory (executed:
`git merge-base --is-ancestor 60f2e40a HEAD`, exit 0;
`git log --no-merges --name-only 60f2e40a..HEAD ^3b2190c4`).
`seal pr-body seal/threads/1793829112-a-release-branch-requires-its-checks --body <pr-body.md> --check`
exited 0 (executed), so the part below `## From the records` is the records'
text.

No phase record claims a `seen red`: phase 1 states it wrote no case and ran
no `seal mutate`, under the *Prose only* row (`trail/phases/phase-1.md:43-49`),
and the diff holds no Python file and no test (executed: `git diff --name-only
3b2190c4...HEAD -- skills/ hooks/ .github/ tests/` lists nothing). So no
at-base clone was made. The sample below is of `executed` claims and of the
statements of the setting, where the outcome rests.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The 18 modules `git grep -l -E 'branch-and-release\|release-checklist' -- tests/` lists besides `tests/conftest.py` each pass alone at HEAD | `trail/phases/phase-1.md:58-61` | the grep, then `bin/test <module> -q -p no:xdist` for each module alone, exit code read directly | holds: 18 modules, exit 0 each (executed, at b7bd43d3) |
| `squash_rule` still ends its paragraph at `**Two rulesets enforce the merge methods.**` | `trail/phases/phase-1.md:61-63`; design G13 | `grep` of `tests/text/test_the_release_tail_does_not_end_at_the_tag.py`; the lead in `docs/releasing/branch-and-release.md:207`; the module's run above | holds: the case indexes that literal at `:211`, the lead stands word for word, the module exits 0 (executed) |
| Every line the range adds under `docs/` is at most 76 columns | `trail/phases/phase-1.md:54-56` | `git diff -U0 3b2190c4...HEAD -- docs/` through `awk` on added-line length | holds: 76 (executed) |
| `test_docs_line_wrap.py` passed over the 96-column line because `branch-and-release.md` is not in `COVERED` and `release-checklist.md` is | `trail/phases/phase-1.md:51-54` | read `tests/behaviour/test_docs_line_wrap.py` `COVERED` | holds: `docs/releasing/release-checklist.md` is listed, `branch-and-release.md` is not (read) |
| The modules `gaps.md` once named as not run pass | `gaps.md` *Not verified* row 2; round 2 *Probes* | `bin/test <module> -q -p no:xdist` for `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/hooks/test_version_check.py`, each alone | holds: exit 0 each (executed) |
| S1: the `release` ruleset holds `non_fast_forward`, the unchanged `pull_request` rule and one `required_status_checks` rule, `lint` and `release` from 15368, strict `false`, `do_not_enforce_on_create` `true`, `bypass_actors` empty | `frame/plan.md` *Judgments of the run* row 3; design S1 and *Data & interfaces* | `gh api repos/MichaelYcJo/AgenticSeal/rulesets/23856929 --jq '{name,target,enforcement,conditions,bypass_actors,rules}'`; `gh api repos/MichaelYcJo/AgenticSeal/rules/branches/release/v0.32.1` | holds: the rules equal the *Data & interfaces* after body field by field, target `refs/heads/release/**/*`, enforcement `active`; the branch lists `non_fast_forward`, `pull_request`, `required_status_checks`, all from 23856929 (executed, read-only) |
| S2: the `main` ruleset equals G3 | `frame/plan.md` *Judgments of the run* row 3; design S2 and G3 | `gh api repos/MichaelYcJo/AgenticSeal/rulesets/23858898 --jq '{...}'`; `gh api repos/MichaelYcJo/AgenticSeal/rulesets` | holds: `bypass_actors` `[]`; `deletion`; `required_status_checks` `lint`, `release` from 15368, strict `false`, `do_not_enforce_on_create` `false`; `non_fast_forward`; `pull_request` `merge`; target `~DEFAULT_BRANCH`; the repository holds these two rulesets only (executed, read-only) |
| The required contexts are the names GitHub reports, and the `pytest` and `arms-grammar` names carry matrix values | design G4; round 1 *Confirmations* | `gh pr view 1360 --repo MichaelYcJo/AgenticSeal --json baseRefName,statusCheckRollup` | holds: `lint` and `release` by those names; `pytest (windows-latest, 3.12, --splits 4 --group 1, ...)`, `arms-grammar (3.13)` and `durations` beside them (executed) |
| The doc's paragraph: the chain check reads no merge commit, and the orchestrator re-runs the broad gate and the sealer after a base merge | `docs/releasing/branch-and-release.md:232-240` | read `skills/code-review/scripts/chain_check.py:963-994` and `skills/code-review/orchestration.md:248`, `:317-323` | holds: `follows` lists `rev-list --no-merges HEAD ^<sha> ^<base>`; the cited heading stands and says the merge moves HEAD past `trail/gate.md` and `guarantee.md` (read) |
| The doc's paragraph: a release branch is cut at a commit of `main` no pull request's `hygiene` run reported on; `lint` is in `test.yml`, `release` in `hygiene.yml` | `docs/releasing/branch-and-release.md:222-231` | read `.github/workflows/hygiene.yml:1-35`, `.github/workflows/test.yml:1-33` | holds: `hygiene` runs on `pull_request` only and has the one job `release`; `test.yml`'s `lint` job runs `ruff check` and `ruff format --check` (read) |
| The table names the `main` ruleset's target "the default branch, `main`" | `trail/phases/phase-1.md:28-31` | `gh repo view MichaelYcJo/AgenticSeal --json defaultBranchRef` | holds: `main` (executed) |
| The version moves 0.32.0 to 0.32.1 in the commit that adds the release's first changelog fragment | `frame/plan.md` *Judgments of the run* row 1; design *Scope* Out | `git show --stat fc538c70`; `git grep -n -F 0.32.0 -- . ':!seal/threads/'`; `gh pr list --base release/v0.32.1 --state all` | holds: fc538c70 changes `.claude-plugin/plugin.json` and `changelog.md` only; no file outside `seal/threads/` names 0.32.0; no pull request into `release/v0.32.1` exists yet, and its tip is 3b2190c4, `main`'s (executed) |
| The departure in plan row 2: a reading committed after the seal leaves `guarantee.md` behind HEAD | `frame/plan.md` *Judgments of the run* row 2 | read `skills/code-review/scripts/chain_check.py:165`, `:1631`, `:1673` | holds: `CLOSING_RECORDS` is `trail/gate.md` and `guarantee.md` only, and the guarantee arm calls `follows` with `only=CLOSING_RECORDS`, so a commit to `plan.md` or `gaps.md` after the seal fails it; the gate arm calls `follows` without `only`, so cffcd9f5 and b7bd43d3 pass it (read) |
| `Removes` row 1: the person's look at `lint` and `release` leaves the checklist box | design *Removes* row 1 | read `docs/releasing/release-checklist.md:13-20`; `git grep -n -E 'CI was green' -- . ':!seal/threads/'` | holds: the box says the rulesets hold `lint` and `release` and asks about the checks no ruleset requires; the grep lists nothing (executed) |
| `Removes` row 2: the names "Main" and "Release branches" and the target `release/*` leave the table | design *Removes* row 2 | `git grep -n -E 'Release branches' -- . ':!seal/threads/'`; `git grep -n -F '`release/*`' -- docs/releasing/branch-and-release.md docs/releasing/release-checklist.md` | holds: both list nothing; the table reads `main` and `release`, `release/**/*` (executed) |
| `Removes` row 3: the clause "and there are no bypass actors: the rule applies to the owner too" leaves the sentence after the table | design *Removes* row 3 | `git grep -n -E 'no bypass actors: the rule applies' -- . ':!seal/threads/'`; read `docs/releasing/branch-and-release.md:217-220`, `:240-241` | holds: the grep lists nothing; the no-bypass rule stands once, in the new paragraph (executed) |
| The broad run's row is `uvx ruff check . && uvx ruff format --check . && bin/test -q` and runs no typechecker | `gaps.md` *Not verified* row 3 | read `seal/config.md:10` | holds (read). The run's own exit and counts are the orchestrator's (`trail/gate.md`), not re-run here, as rule 2 gives |
| The issue's other coordinates: `CLAUDE.md` and `CONTRIBUTING.md` state no ruleset, and the diff touches no check | design G2, G10 | `git grep -n -i -E 'bypass\|ruleset' -- CLAUDE.md CONTRIBUTING.md`; `git diff --name-only 3b2190c4...HEAD -- skills/ hooks/ .github/ tests/` | holds: both list nothing (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Both rulesets require `lint` and `release` at the merging commit, no `pytest` or `arms-grammar` leg is required, no up-to-date rule, no enforcement on create, no bypass actor and no override; the two release documents state it, and three statements leave (`frame/design.md` *Scope*, *Removes*) | the issue body's three *What to build* bullets, each decided with grounds, and its *Not this*, since no case reads the ruleset and the chain check is untouched; the live rulesets (S1, S2); the diff | none |
| the build | `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* gains the table column and the paragraph, the checklist box asks about the checks no ruleset requires, and `plugin.json` moves to 0.32.1 (`trail/phases/phase-1.md`; the diff) | the design's Scope 2 and 3 and every `Removes` row; the live setting; the one departure the phase names, "a work item's ready pull request", which round 1 confirmed against `chain_check.py:2019` | none |
| the last round | Round 2, `target: 22bd6607`, confirms round 1's three fixes and opens nothing (`trail/rounds/round-2.md`) | the tree: each confirmation's coordinate stands as stated; the commits after 22bd6607 touch only this work item's records, which this audit read: 60f2e40a's plan row 3, *Operational impact* step 2 and `gaps.md` row 1, cffcd9f5's `trail/gate.md`, b7bd43d3's `gaps.md` rows 2 and 3 | none |
| the changelog | The `release` ruleset now requires `lint` and `release` as `main` did; no up-to-date rule, no rule on create, no bypass actor; the two documents state it (`changelog.md`) | the live rulesets; the diff; the design | none |
| the orchestrator's part of the pull request body | The setting changed outside the tree and was read back; it went in before the broad run, not after the seal, with grounds; the first `PUT` under the old name stopped at `HTTP 307`; the version moves here; round 1 opened three `should`s and round 2 none; the broad run passed at 60f2e40a | `frame/plan.md` *Judgments of the run* rows 1 to 3; `routing.md` *Why this way*; rounds 1 and 2; `trail/gate.md`; the live rulesets; the issue body on #445 | none. Its "this pull request is the first to merge under the rule" is S5's, which is read at the merge; at this audit no pull request into `release/v0.32.1` exists |

The departure from the owner's answer was weighed as a claim. `routing.md`
*Why this way* records the owner's answer that the orchestrator applies the
ruleset after the work item is sealed. Plan row 2 moves the act to before the
preflight, and the body states the move and says the owner can overturn it.
Its ground holds in the tree (the row above, `chain_check.py:165`, `:1673`).
The issue body sets no timing, and the act it asks for is done as the design
states it. So no party contradicts another, and the timing is the owner's to
overturn after the run, not a question this verdict holds open.

```seal
target: b7bd43d3 against 3b2190c4
Verdict: sealed
```
