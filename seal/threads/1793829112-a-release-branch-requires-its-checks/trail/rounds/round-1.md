# Review round 1: 1793829112-a-release-branch-requires-its-checks

```seal
target: 815a183a against release/v0.32.1
```

The target is the branch at 815a183a against `release/v0.32.1`, which is
`main` at 3b2190c4 (executed: `git rev-parse`). The tree diff is
`docs/releasing/branch-and-release.md`, `docs/releasing/release-checklist.md`
and `.claude-plugin/plugin.json`, plus the work item's records. This is round
1, so no earlier round's coordinates were carried, and every fact below was
established this round. The `release` ruleset change of design Scope 1 is not
applied yet. So the documents were read against the setting design *Data &
interfaces* says will be applied, and against the live `main` ruleset.

## Findings

### 1. The paragraph says the chain check refuses the merge commit an up-to-date rule would force, and the chain check reads no merge commit

```seal
severity: should
location: `docs/releasing/branch-and-release.md:232-236`, `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:14`, `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/plan.md:24`
evidence: read `skills/code-review/scripts/chain_check.py:963-993`, `skills/code-review/scripts/chain_check.py:1631`, `skills/code-review/scripts/chain_check.py:1673`, `skills/code-review/orchestration.md:311-322`, `agents/sealer.md:56-62`
```

Why it matters: the new paragraph gives the reason neither ruleset requires a
branch to be up to date. It says the second of two work items would "merge the
release branch in after its last review round, and the chain check refuses
that merge commit as a change no round read" (`branch-and-release.md:233-236`).
Design G8 states the same thing ("the chain check refuses it as a fix no round
read", `frame/design.md:14`), and so does plan row 5 ("the chain check refuses
that commit", `frame/plan.md:24`). The check does the opposite.
`chain_check.py#follows` lists the commits after a record with `rev-list
--no-merges HEAD ^<record> ^<base>` (`chain_check.py:980-982`), and its
docstring says "Merge commits and the base's own commits are not the branch's"
(`:971-972`). The records arm, the broad-gate arm (`:1631`) and the guarantee
arm (`:1673`) all read through `follows`, so none of them refuses a pure merge
of the base. `skills/code-review/orchestration.md:317-322` states this
outright: "the chain check lists the branch's commits with `--no-merges` and
reads no merge commit". The sealer's step 1 applies the same rule
(`agents/sealer.md:56-58`). The real cost of `strict` is different.
`orchestration.md:319-323` says a merge of the base "moves HEAD past
`trail/gate.md` and `guarantee.md`", so the orchestrator runs the broad gate
again, runs `seal pr-body` again and spawns the sealer again. The decision,
strict `false`, holds on that reason too. The sentence a person reads before a
merge names a refusal that does not exist, and a reader who trusts it would
expect the check to catch a merge it lets through.

The fix reaches three statements: the paragraph, G8 and plan row 5.
`frame/questions.md:7` cites G8 and states no reason of its own, so it stays.

```markdown
be up to date with its base before it merges. Requiring it would make the
second of two work items running side by side merge the release branch in
once the first has landed, which is often after its own seal. The chain
check reads no merge commit, so the merge would pass it, but the merge
moves HEAD past the work item's broad run and its seal, and the
orchestrator then runs both again (`skills/code-review/orchestration.md`
*Orchestrator: the pull request opens once the sealer seals*). There are no
bypass actors and no override, so the rule applies to the owner too.
```

For G8 (`frame/design.md:14`), replace the sentence "That commit touches files
outside its `seal/threads/<id>/`, and the chain check refuses it as a fix no
round read." with:

```markdown
The chain check reads no merge commit (`skills/code-review/scripts/chain_check.py#follows`), so the merge passes it, but it moves HEAD past `trail/gate.md` and `guarantee.md`, and the orchestrator then runs the broad gate and the sealer again (`skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*).
```

For plan row 5 (`frame/plan.md:24`), the failure-scenario cell becomes:

```markdown
Design G8: the second of two work items running side by side has to merge the release branch in once the first lands, and that merge costs it a second broad run and a second seal.
```

```seal
verdict: fixed 200fc280
answer: The finding holds: `chain_check.py#follows` lists commits with `--no-merges` and excludes the base's, and `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* says the base merge moves HEAD past `trail/gate.md` and `guarantee.md` and the orchestrator runs the broad gate and the sealer again. In 200fc280 the paragraph of `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* gives that reason in the crafter's own words, not the paste-ready text as given: the paste-ready "which is often after its own seal" could read as the first item's seal, so the paragraph says the merge comes once the first item lands, often after the second's broad run and seal, that the chain check passes the merge, citing `chain_check.py#follows`, and that the merge moves HEAD past the work item's broad run and seal so the orchestrator runs both again. G8 in `frame/design.md` and plan row 5 in `frame/plan.md`, the frame half, were fixed by the orchestrator in 09792bf1; both paths stand in this finding's `location:`, so no `location:` line is added here.
```

### 2. The checklist box names `pytest` and `arms-grammar` as the jobs left, and `durations` also runs on every pull request into a release branch with no ruleset requiring it

```seal
severity: should
location: `docs/releasing/release-checklist.md:13-19`, `seal/threads/1793829112-a-release-branch-requires-its-checks/changelog.md:3`, `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:18`, `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:30`, `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:49`, `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:80`
evidence: executed `gh pr view 1360 --json baseRefName,statusCheckRollup`; read `.github/workflows/test.yml:194-198`, `.github/workflows/test.yml:257-259`
```

Why it matters: before this change, the first box of *0. Before starting* had
a person confirm that each work item's pull request "CI was green at the
commit that merged". That covered every check. The new box asks about "its
pull request's `pytest` and `arms-grammar` jobs" only
(`release-checklist.md:14`). Design G12 grounds this as "The box keeps the
jobs no ruleset requires, `pytest` and `arms-grammar`" (`frame/design.md:18`).
That list is incomplete. `test.yml` has a `durations` job with `needs: pytest`
and `if: ${{ !cancelled() }}` and no base filter (`test.yml:194-198`). It runs
on every pull request, and it fails where a leg's durations artifact is
missing (`if-no-files-found: error`). #1360, whose base is
`release/v0.32.0`, shows a `durations` run beside `lint`, `release`, the
`pytest` legs and the `arms-grammar` legs (executed). Only `release-report` is
limited to a base of `main` (`test.yml:259`). Neither ruleset requires
`durations`, so after this change no ruleset and no box covers a red
`durations` run. The release would ship a checklist that tells a person to
look at less than the old box did, which nobody asked for. A wording that
names no jobs also avoids a list in the checklist that has to stay in step
with `test.yml`, the copy the paragraph itself warns about
(`branch-and-release.md:226-228`).

The fix also reaches the changelog fragment's last sentence
(`changelog.md:3`, "asks a person about the `pytest` and `arms-grammar` jobs
only") and the frame cells that state the same list: G12 (`design.md:18`),
Scope 3 (`:30`), S4 (`:49`) and the first *Removes* row (`:80`). The paragraph
in `branch-and-release.md:225-226` says "The `pytest` and `arms-grammar` jobs
are not required". That sentence is true and claims no full list, so it can
stay.

```markdown
- [ ] Every work item of the release is squash-merged into `release/vX.Y.Z`
      and no check of its pull request was red **at the commit that
      merged**. The rulesets hold the `lint` and `release` jobs there
      (`docs/releasing/branch-and-release.md` *Work accumulates on a
      release branch*), so the look is for the jobs no ruleset requires. A
      merge pressed while a later push was still on its way takes the
      earlier commit; the corrections then need a pull request of their
      own.
```

The changelog's last sentence then reads: "The first box of
`docs/releasing/release-checklist.md` *0. Before starting* asks a person about
the checks no ruleset requires."

```seal
verdict: fixed 200fc280
answer: The finding holds: `durations` in `.github/workflows/test.yml` runs on every pull request and no ruleset requires it, so a box naming `pytest` and `arms-grammar` asked about less than the old box did. In 200fc280 the first box of `docs/releasing/release-checklist.md` *0. Before starting* asks that no check of the pull request was red at the commit that merged, says the rulesets hold `lint` and `release` there, and names no job list. It follows the paste-ready text except that it says "the checks no ruleset requires" where the paste-ready says "the jobs", so the box and the changelog say the same. The last sentence of `changelog.md` reads as the finding gives it. The sentence of `docs/releasing/branch-and-release.md` saying the `pytest` and `arms-grammar` jobs are not required stays, as the finding says. G12, Scope 3, S4 and the first *Removes* row of `frame/design.md`, the frame half, were fixed by the orchestrator in 09792bf1; that path stands in this finding's `location:`, so no `location:` line is added here.
```

### 3. The plan says a reading committed after the broad run leaves `trail/gate.md` behind HEAD, and the gate arm passes a commit that touches only the work item's records

```seal
severity: should
location: `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/plan.md:39`, `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/plan.md:56`
evidence: read `skills/code-review/scripts/chain_check.py:963-993`, `skills/code-review/scripts/chain_check.py:1609-1636`, `skills/code-review/scripts/chain_check.py:1673`, `docs/checks/the-pull-request-check.md:52-54`, `agents/sealer.md:56-62`
```

Why it matters: the orchestrator folded the apply step's timing into the frame
at a1d33e6d, and the grounds it recorded name two costs. *Operational impact*
says "A commit of the reading after the broad run or after the seal would
leave `trail/gate.md` or `guarantee.md` behind HEAD" (`plan.md:39`). The
second row of *Judgments of the run* says "one committed after the broad run
leaves `trail/gate.md` behind it" (`plan.md:56`). The half about `guarantee.md`
holds. The guarantee arm calls `follows` with `only=CLOSING_RECORDS`, so a
commit to `plan.md` after the seal is refused (`chain_check.py:1673`). The half
about `trail/gate.md` does not hold. The broad-gate arm calls `follows`
without `only` (`chain_check.py:1631`), and `follows` passes every commit that
touches only paths under the work item's directory (`:986-992`).
`docs/checks/the-pull-request-check.md:52-54` says the same: the newest run "is
HEAD, or only the work item's records follow it". The sealer's step 1 goes on
in that case too (`agents/sealer.md:60-61`). So a reading committed between
the broad run and the seal costs nothing. The settle reads these judgment rows
to learn what each kind of judgment cost. This row would teach it a cost the
check does not impose. The decision to apply the change before the seal still
stands, on the guarantee half and on the sealer reading the live setting.

```markdown
**A repository setting changes, outside the tree.** The orchestrator applies Scope 1 once the last round record has no finding open and before it runs `seal gate --preflight`, so the reading of step 3 is committed with the work item's records, the sealer reads S1 and S2 against the live setting, and this pull request is the first to merge under it (design S5). A commit of the reading after the seal would leave `guarantee.md` behind HEAD, and the sealer would run again.
```

The grounds cell of row 2 (`plan.md:56`) becomes:

```markdown
The owner's batch answer puts the act with the orchestrator after the work item is sealed (`routing.md` *Why this way*); a reading committed after the seal leaves `guarantee.md` behind HEAD, so the act moves to the step before the preflight, where its record costs no second seal and the sealer reads the setting the documents state
```

```seal
verdict: fixed 09792bf1
answer: The finding holds, and the orchestrator fixed it in 09792bf1: `frame/plan.md` *Operational impact* and the grounds cell of *Judgments of the run* row 2 now name only the cost after the seal, `guarantee.md` behind HEAD, and no longer say a reading committed after the broad run leaves `trail/gate.md` behind it. The fix pass made no change of its own for this finding.
```

## Confirmations

What matched: the table's `main` row matches the live setting. Ruleset 23858898
is named `main`, targets `~DEFAULT_BRANCH`, allows `merge` only, and requires
`lint` and `release` from integration 15368. `strict_required_status_checks_policy`
is `false` and `bypass_actors` is empty (executed: `gh api
repos/MichaelYcJo/SpecSeal/rulesets/23858898`). The row writes the target as
"the default branch, `main`". `trail/phases/phase-1.md:28-31` claimed that as a
reading of Scope 2a, and it holds, because the default branch is `main`.

What matched: the live `release` ruleset, 23856929, equals the "before" JSON
in design *Data & interfaces* field by field (executed: `gh api
repos/MichaelYcJo/SpecSeal/rulesets/23856929`). So the `rules` body there is
not stale, and its `pull_request` rule is the live one unchanged. The table's
`release` row (`branch-and-release.md:215`) names `release`, `release/**/*`,
`squash`, and `lint` and `release`. That is the setting the body applies, and
it matches what the frame says will be applied.

What matched: the two required context names are the check-run names GitHub
reports. #1360's rollup holds `lint` and `release` by those names. The
`pytest` and `arms-grammar` names carry matrix values, such as `arms-grammar
(3.13)` (executed: `gh pr view 1360 --json statusCheckRollup`). So the
paragraph's reason for leaving those legs out (`branch-and-release.md:225-229`)
holds.

What matched: the build departs from Scope 2b in one sentence. The phase
record claimed that the broad-gate arm reads `trail/gate.md` of declared work
items only (`trail/phases/phase-1.md:18-26`). It holds: `chain_check.py:2019`
calls `broad_gate` inside the loop over declared items, so a pull request that
declares no item reads no gate record. "a work item's ready pull request whose
broad run is not at HEAD" (`branch-and-release.md:228-229`) is the accurate
form, and the departure is right.

What matched: Scope 2c. The no-bypass clause left the sentence after the table
and stands once in the new paragraph (`branch-and-release.md:236-237`). The
"No workflow can therefore commit the version to a release branch" sentence
stays (`:219-220`) (read). The bold lead `**Two rulesets enforce the merge
methods.**` stands word for word at `:207`, as G13 requires (read).

What matched: S3's second half. I re-ran G2's grep over the tree, excluding
`seal/threads/`, for `bypass`, `ruleset`, `required check`, `required status`,
`status check`, `branch protection`, `CI was green`, `green at the commit` and
`commit that merged`. Outside the edited section it lists
`branch-and-release.md:36`, `:176` and `:198`, which stay true, plus
`hooks/review-skill-gate.py:127` and `tests/hooks/test_launch.py:197-199`,
which use "bypass" in another sense (executed). A second grep for red-check
and merge-button wording lists nothing else that states a ruleset fact
(executed). Both greps search on words, so they are a sample.

What matched: the version move. `.claude-plugin/plugin.json` moves from
0.32.0 to 0.32.1 in fc538c70, the commit that adds `changelog.md`. That is the
shape of precedent 9c36bbda, which moved `plugin.json` and added a fragment in
one commit (read: `git show 9c36bbda --stat`). No file outside `seal/threads/`
names 0.32.0 at HEAD (executed: `git grep -n -F 0.32.0`). This matches plan
*Judgments of the run* row 1.

What matched: the crafter claimed 18 modules from the frame's grep, each run
alone with exit 0. The grep lists 18 modules besides `tests/conftest.py`
(executed). Three of them were re-run here through `bin/test <module> -q -p
no:xdist`, each alone, and each exited 0:
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py`,
`tests/behaviour/test_docs_line_wrap.py` and
`tests/behaviour/test_release_hygiene.py` (executed). The other 15 are carried
as the crafter's claim. The phase record says the added lines under `docs/` are
at most 76 columns, and they are (executed: an `awk` length over the added
lines).

What matched: the suite's label is honest. `gaps.md:7-9` names the unapplied
setting, the modules reading `plugin.json` or other `docs/releasing/` text
that were not run, and the suite, lint and typecheck. Each is labelled
unverified with the orchestrator as its answerer (read). The phase record
claims no case and no mutation run. That is the *Prose only* reading of a
docs-only diff, and the diff holds no Python file (read: `git diff --stat`).

What matched: `frame/plan.md:51` opens with `<` and a letter. It is the
template's own instruction line (`templates/records/sdd-plan.md:25`), left
above a filled table, and no fence follows it in that file, so it is no
finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| S1, S2 and S5: the `release` ruleset after the `gh api` PUT, `main` unchanged at that moment, and this pull request merging with `lint` and `release` required | `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:46-50` | the orchestrator, at the apply step of `frame/plan.md` *Operational impact* and at the merge |
| Whether GitHub refuses the cut of a release branch with `do_not_enforce_on_create` `false`, the assumption G7 rests on | `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:13` | the orchestrator, at the next cut of `release/vX.Y.Z` (`frame/plan.md:45`) |
| The 15 narrow modules the crafter ran and this round did not re-run, and the modules reading `plugin.json` or other `docs/releasing/` text | `seal/threads/1793829112-a-release-branch-requires-its-checks/gaps.md:8-9` | the orchestrator, at the broad gate |
| Whether the owner's answer of applying the ruleset after the seal (`routing.md:16`) admits the move to before the preflight that plan row 2 records | `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/plan.md:56` | the owner, reading the record after the run |

## Probes

| Command | Result |
|---|---|
| `gh api repos/MichaelYcJo/SpecSeal/rulesets/23858898` and `.../23856929`, and `gh api repos/MichaelYcJo/SpecSeal/rulesets` | read only; `main` as in G3, `release` equal to *Data & interfaces*' before JSON, no other ruleset |
| `gh pr view 1360 --json baseRefName,statusCheckRollup` | base `release/v0.32.0`; `lint`, `release`, eight `pytest` legs, two `arms-grammar` legs and `durations` succeeded, `release-report` skipped |
| `bin/test <module> -q -p no:xdist` for the three modules named above, each alone | exit 0 each |
| `git grep -l -E 'branch-and-release\|release-checklist' -- tests/` | 18 modules besides `tests/conftest.py` |
