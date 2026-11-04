# Review round 2: 1793829112-a-release-branch-requires-its-checks

```seal
target: 22bd6607, fixes 2b67e07c..22bd6607
```

This is a verifying round. Its target is the diff of round 1's fixes,
`git diff 2b67e07c 22bd6607`, read in the branch's linked worktree at
22bd6607 (executed: `git log --oneline -8`, `git status --short`, clean).
The diff changes `docs/releasing/branch-and-release.md`,
`docs/releasing/release-checklist.md`, the work item's `changelog.md`,
`frame/design.md` and `frame/plan.md`, and appends round 1's three close
blocks to `trail/rounds/round-1.md` (executed: `git diff --stat`). It holds
no Python file and no test. `seal/parity.md` is not declared, so no
`original:` line is owed.

Carried from round 1 and not re-established, because the fix diff does not
touch them: the live readings of the `main` ruleset 23858898 and the
`release` ruleset 23856929, the check-run names of #1360, the G2 grep over
the tree, and the version move in fc538c70. Re-established this round:
`chain_check.py#follows` and the section of `skills/code-review/orchestration.md`
the new paragraph cites (read), the jobs of `.github/workflows/test.yml` and
`hygiene.yml` (read), and the narrow modules (executed, *Probes*).

## Findings

None. Each of round 1's three closes holds, and the fix diff adds no unit
that carries a defect.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the paragraph at `docs/releasing/branch-and-release.md:232-246`
no longer says the chain check refuses the merge commit an up-to-date rule
would force. It says the chain check reads no merge commit and passes that
merge, and that the merge moves HEAD past the work item's broad run and
seal, so the orchestrator runs both again. Both halves stand in the tree.
`skills/code-review/scripts/chain_check.py:980-982` lists the commits after
a record with `rev-list --no-merges HEAD ^<sha> ^<base>`, and its docstring
at `:971-972` says merge commits and the base's own commits are not the
branch's (read). `skills/code-review/orchestration.md:311-323`, under the
heading the paragraph cites at `:248`, says the merge "moves HEAD past
`trail/gate.md` and `guarantee.md`" and that the orchestrator then runs the
broad gate, `seal pr-body` and the sealer again (read). The crafter claimed
its own wording was chosen because the paste-ready "which is often after its
own seal" could read as the first item's seal. That reading is open in the
paste-ready text, and the tree's "after the second's broad run and seal"
(`branch-and-release.md:236-237`) closes it. The frame half holds too: G8
(`frame/design.md:14`) and plan *Alternatives considered* row 5
(`frame/plan.md:24`) carry the same reason and no longer name a refusal
(read). `frame/questions.md:7` cites G8 and states no reason of its own, as
round 1 said. The crafter claimed the two new citations were not checked by
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`; `gaps.md:8`
says that module was not run. It reads every tracked file outside
`seal/threads/` and `evals/behaviour/` (`tests/censuses.py:986`), its
`PATH_CITED` pattern at `:86` spans a line break inside the italics, and its
`NAME_TOKEN` pattern at `:257` reads `chain_check.py#follows` (read). This
round ran it at 22bd6607 and it exited 0 (executed), so both citations now
stand checked. Every added line of the paragraph is at most 74 columns
(executed: `awk` over lines 232-246), and
`tests/behaviour/test_docs_line_wrap.py` exited 0 (executed).

```seal
confirms: round-1#2
```
What holds: the first box of *0. Before starting*
(`docs/releasing/release-checklist.md:13-19`) asks that no check of each
work item's pull request was red at the commit that merged. It says the
rulesets hold `lint` and `release` there, and it names no job list, so
`durations` is inside the look again. `.github/workflows/test.yml:194-196`
gives `durations` `needs: pytest` and `if: ${{ !cancelled() }}` with no base
filter, and only `release-report` is limited to a base of `main` (`:259`);
`hygiene.yml` has the one job `release` (read). The last sentence of
`changelog.md:3` reads "asks a person about the checks no ruleset requires",
matching the box (read). The frame half holds: G12 (`frame/design.md:18`)
gives the reason the box names no list, and its parenthesis lists `pytest`,
`arms-grammar` and `durations`, which are the three jobs that run on a
pull request into a release branch and that no ruleset requires (read).
Scope 3 (`:30`), S4 (`:49`) and the first *Removes* row (`:80`) say the
box keeps the checks no ruleset requires and names none (read). The
sentence at `branch-and-release.md:225-226` that the `pytest` and
`arms-grammar` jobs are not required stays, as round 1 said it could. A
search of the work item's present-tense files and `docs/releasing/` for
`arms-grammar`, `durations` and `green` lists no other statement of the old
two-job box (executed: `git grep -n -E` over `frame/`, `changelog.md`,
`gaps.md`, `routing.md` and `docs/releasing/`). That search covers the
closed set of rule 12's second method, each of those files read whole for
the box's wording.

```seal
confirms: round-1#3
```
What holds: `frame/plan.md:39` (*Operational impact*) and the grounds cell
of *Judgments of the run* row 2 (`frame/plan.md:56`) now name only the cost
after the seal, `guarantee.md` behind HEAD, and no longer say a reading
committed after the broad run leaves `trail/gate.md` behind it (read). That
matches `chain_check.py:986-992`, where `follows` passes a commit touching
only the work item's directory. Of the three calls of `follows`
(`:1450`, `:1631`, `:1673`), the guarantee arm's at `:1673` alone narrows
that with `only` (executed: `grep -n "follows("`). Design G10 (`frame/design.md:16`)
still says the act is taken before the broad run, which stays true of the
step before `seal gate --preflight` (read).

What matched: the crafter declined to add a close-block `location:` line for
findings 1 and 2. `docs/forms/the-round-record.md:55` owes that line only
"Where its fix went to a path the finding's `location:` does not name". Both
findings' `location:` lines already name `frame/design.md`, and finding 1's
names `frame/plan.md`, the paths 09792bf1 changed for them, and 200fc280
touches `branch-and-release.md`, `release-checklist.md` and `changelog.md`,
which their `location:` lines also name (read). So no line is owed, and each
`fixed` commit touches a path its finding names. The two answers say the
frame half came in 09792bf1, so a reader of the close is told which commit
holds which half.

What matched, weighed and no finding: the box's new wording asks that no
check "was red", where the old box asked that CI "was green". A check that
was cancelled or still running at the merging commit is neither. On a pull
request, `test.yml:19-21` cancels a run only when a later push starts one,
and the box's next sentence already covers a merge pressed while a later
push was on its way, so the narrower word loses no case the old box caught.
Plan row 5 (`frame/plan.md:24`) says the merge costs the second item "a
second broad run and a second seal" without the "often" of
`branch-and-release.md:236`; where the first item lands before the second's
broad run, the second merges first and pays neither. The decision, strict
`false`, stands on the common case either way, and no party acts on the row's
unconditional wording, so it reads loosely and is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| S1, S2 and S5: the `release` ruleset after the `gh api` PUT, `main` unchanged at that moment, and this pull request merging with `lint` and `release` required | `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:46-50` | the orchestrator, at the apply step of `frame/plan.md` *Operational impact* and at the merge |
| Whether GitHub refuses the cut of a release branch with `do_not_enforce_on_create` `false`, carried from round 1 | `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/design.md:13` | the orchestrator, at the next cut of `release/vX.Y.Z` |
| Whether the owner's answer of applying the ruleset after the seal admits the move to before the preflight, carried from round 1 | `seal/threads/1793829112-a-release-branch-requires-its-checks/frame/plan.md:56` | the owner, reading the record after the run |
| The suite, the repository-wide lint and the typecheck, labelled `unverified` in `gaps.md:9`, which is honest: no party has run them | `seal/threads/1793829112-a-release-branch-requires-its-checks/gaps.md:9` | the orchestrator, at the broad gate |

This round leaves no finding open. What comes due is the orchestrator's
apply step of `frame/plan.md` *Operational impact*, its broad run, and the
sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/test <module> -q -p no:xdist`, each alone, for the 18 modules `git grep -l -E 'branch-and-release\|release-checklist' -- tests/` lists besides `tests/conftest.py`, at 22bd6607 | exit 0 each |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist` | exit 0 |
| `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist` and `bin/test tests/hooks/test_version_check.py -q -p no:xdist`, each alone, two of the modules `gaps.md:8` names as not run | exit 0 each |
| `awk` over `docs/releasing/branch-and-release.md:232-246` and `docs/releasing/release-checklist.md:13-20` for line length | at most 74 and 75 columns |
