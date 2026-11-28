# Review round 1: 1795849901-number-read-at-cut

```iadd
target: 4547bb91 against release/v0.43.0
```

Round 1 is a finding round over the whole range `596c79a6..4547bb91`, where `596c79a6` is `release/v0.43.0`. It was read in the worktree the orchestrator named, checked out at `4547bb91`, and nothing in it was changed. No earlier round exists, so no verdict is carried. The coordinates of `frame/plan.md` *Technical context* and of the three phase records were opened again at the target rather than taken from the records. No `agentory/parity.json` is declared, so no parity comparison is owed. The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, the three keep files, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` to `phase-3.md`. The record language and the pull request language are both English, so no `pr.<lang>.md` stands. The `docs/releasing/` text is read as the policy in force: the baseline plus the latest decision of the unsettled designs' `## Rule changes`, in merge order. Those designs are this item's and the released `1795841828-settle-only-release-note`'s.

The axes walked are the table of `skills/code-review/SKILL.md`. This change adds four of its own: the release number's boundary values, the timing between the release merge, the close and the next squash, the transition release that still runs from a numbered branch, and the policy in force after both settles.

## Findings

### 1. The rule change and *Scope* item 5 say an unreadable release pull request body never fails the job, and for a note of settles alone the code fails it

```iadd
severity: should
location: `agentory/threads/1795849901-number-read-at-cut/frame/design.md:99-102`, `agentory/threads/1795849901-number-read-at-cut/frame/design.md:240-246`, `agentory/threads/1795849901-number-read-at-cut/changelog.md:5`
evidence: read `.github/scripts/publish_release_note.py:1034-1049`, `agentory/threads/1795841828-settle-only-release-note/frame/design.md:72-77`; executed `git grep -n -F "cannot be read leaves" -- agentory/threads/1795849901-number-read-at-cut .github/scripts` at 4547bb91, and `python3 -I test_tmp_rule_changes.py` (## Probes)
```

Why it matters: `main` reads the release pull request's body once, at `.github/scripts/publish_release_note.py:1034`. For a note of fragments, a body that cannot be read leaves no theme line and the run goes on (line 1037). For a range of settles alone, the same failure prints `Nothing published.` and returns 1 (lines 1039-1044). So the job fails. That is the rule the released `1795841828-settle-only-release-note` writes into the same section, *Cutting a release*: "the job goes red where that body cannot be read or is empty" (its `frame/design.md:72-77`).

This design's `to` for that section (`frame/design.md:240-246`) says "a body that cannot be read leaves the note without one and never fails the job". It does not limit the clause to a note of fragments. The probe placed both items' operations in merge order, and the section then holds both sentences. One says an unreadable body never fails the job, and the other says the job goes red when that body cannot be read. A settling session or an orchestrator reading a red publish run cannot tell which one governs. *Scope* item 5 (`frame/design.md:99-102`) carries the same unlimited clause, "and fails nothing". `changelog.md:5` says "a body that cannot be read leaves the note without one" right after the settles-alone clause, so it reads as covering that case too. For settles alone no note is published at all. The module docstring, `.github/scripts/publish_release_note.py:79-83`, does limit the clause ("for a note of fragments"), so the code's own account is right.

The `git grep` printed `changelog.md:5`, `frame/design.md:242` and `trail/phases/phase-2.md:63`. The phase record already limits the clause to "a note of fragments", and it states its own moment, so it stays. The `frame/design.md:101-102` statement wraps across lines and was found by reading. A search on the fact's words is a sample under contract rules 12 and 19, because a statement in other words escapes it.

```markdown
<!-- frame/design.md, Scope item 5, the sentence from "The theme" -->
   request by the merge commit the tag names, with no head name. The theme
   line is the first sentence of that pull request's body. For a note of
   fragments, a body that cannot be read leaves the note without one and
   fails nothing. A note of settles alone carries none, since that body
   stands whole beneath it, and still fails where that body cannot be
   read. `milestone_description`, `MILESTONE_TITLE` and `PURPOSE_LABEL`

<!-- frame/design.md, ## Rule changes, the second operation on Cutting a release: its to -->
  to: The release's theme follows it, the first sentence of the body of
    the release pull request whose merge commit the tag names. For a note
    of fragments, a body that cannot be read leaves the note without one
    and never fails the job; a note of settles alone, whose changes are
    that body, carries none. A summary read from the pull requests whose
    squash commits the tag's range holds, each named by the `(#N)` its
    subject ends with, follows:

<!-- changelog.md, line 5, its last two sentences -->
The theme line is the first sentence of its body. A note of settles alone carries no theme line, since that body stands whole beneath it, and for a note of fragments a body that cannot be read leaves the note without one.
```

```iadd
verdict: fixed 83733457
answer: The framer folded *Scope* item 5 and the second operation on *Cutting a release* in `c7825eb0`, each now limiting the clause to a note of fragments. This pass rewrote `changelog.md:5` against the fold in its own words rather than the paste-ready line, since the fold also says a note of settles alone still fails: "For a note of fragments, a body that cannot be read leaves the note without a theme line, and the job goes on. A note of settles alone carries no theme line, since that body stands whole beneath it, and the job still fails where that body cannot be read." That matches `.github/scripts/publish_release_note.py:1034-1049`, read. The evidence's `git grep -n -F "cannot be read leaves" -- agentory/threads/1795849901-number-read-at-cut .github/scripts`, run again at `62208e10`, prints `changelog.md:5`, `frame/design.md:101` and `:259`, `trail/phases/phase-2.md:63` and lines of this record. Each limits the clause to a note of fragments, except this record's lines, which quote the finding. Round 1's probe `test_tmp_rule_changes.py`, re-run at `62208e10` as `python3 -I ../round-1/test_tmp_rule_changes.py <worktree>` from `<scratchpad>/1795849901-number-read-at-cut/fix-1/`, parsed both designs with no problem and placed every operation. A new probe of this pass, `fix-1/test_tmp_after_both.py`, run once and placing the same operations, printed *Cutting a release* holding "the job goes red where that body cannot be read or is empty" for settles alone beside "For a note of fragments, a body that cannot be read leaves the note without one and never fails the job" (both executed).
```

### 2. Two sentences of the policy in force contradict the code after both settles, and no operation of `## Rule changes` reaches them

```iadd
severity: should
location: `agentory/threads/1795849901-number-read-at-cut/frame/design.md:217-582`, `docs/releasing/release-checklist.md:291-293`, `docs/releasing/issues-and-milestones.md:264-267`
evidence: executed `git grep -n -E 'release/v|merged: X|gh pr list|theme|HEAD_BRANCH|first pull request|Purpose:|milestone|hotfix|could not be listed' -- docs/` at 4547bb91, and `python3 -I test_tmp_rule_changes.py` (## Probes); read `agentory/threads/1795841828-settle-only-release-note/frame/design.md:113-118`, `.github/scripts/publish_release_note.py:585-589`, `.github/scripts/publish_release_note.py:644`, `.github/scripts/release_completeness_check.py:184-191`
```

Why it matters: the settle writes only the sections that `## Rule changes` names. A sentence that this change makes false, and that no operation reaches, stays in `docs/releasing/` after the settle. The probe placed the released settle-only item's operations and then this item's, and it printed both sentences as they will stand:

- `docs/releasing/release-checklist.md` *After the merge*, as the settle-only item writes it (its `frame/design.md:113-118`): "Where the job log says the pull requests could not be listed, the note went out as the theme line and the fragments alone, and for a range of settles alone as the theme line and the release pull request's body alone." Under this change a note of settles alone carries no theme line (`publish_release_note.py:1045-1050`). The log no longer says the pull requests could not be listed. It says `gh pr view <N> failed, so the note is the theme line and the fragments, or the release pull request's body, with no summary of the pull requests` (`WITHOUT_SUMMARY`, lines 585-589, printed at line 644). A person following the checklist looks for a log line that is no longer printed, and expects a theme line that is not there.
- `docs/releasing/issues-and-milestones.md` *A label says a ticket is already in, before the release ships*, lines 264-267: "a label naming a release the issue is not in **fails**, because that is always a hand-edit or a squash subject that lost its `(#N)`". `merged: next` names no release. The check's own refusal names a third cause, "or a label the last release's close did not take off" (`release_completeness_check.py:184-191`), and `frame/plan.md` A7 relies on that third cause. The operation at `frame/design.md:441-447` rewrites the opening clause of this sentence and leaves the clause that states the cause.

`frame/plan.md` *Overlap with the release* names the work items built beside this one. The released, unsettled settle-only item is cited only in G3, so its `## Rule changes` were not read against this one. Phase 3 found two more sentences of this class, and the fold `72844ffd` reached them. The search above is a sample under contract rules 12 and 19. It found these two among the lines it printed, and each other printed line is under an operation, or states a past release or a fact that still holds. A statement in other words escapes it. The fix pass owes the same probe after it adds the two operations, because no check at the pull request places a `from`.

```markdown
- change
  file: docs/releasing/release-checklist.md
  section: After the merge
  from: Where the job log says the pull requests could not be listed, the note went out as the theme line and the fragments alone, and for a range of settles alone as the theme line and the release pull request's body alone. One `gh release edit` repairs either.
  to: Where the job log says one of the release's pull requests could not
    be read, the note went out with no summary of the pull requests: the
    theme line and the fragments, or for a range of settles alone the
    release pull request's body with no theme line. One `gh release edit`
    repairs either.
- change
  file: docs/releasing/issues-and-milestones.md
  section: A label says a ticket is already in, before the release ships
  from: a label naming a release the issue is not in **fails**, because that is always a hand-edit or a squash subject that lost its `(#N)` and one command repairs it,
  to: a `merged: next` on an issue the release does not carry **fails**,
    because that is a hand-edit, a squash subject that lost its `(#N)`, or
    a label the last release's close did not take off, and one command
    repairs each,
```

The first operation's `from` quotes the settle-only item's `to`, because in merge order that text is what the section holds when this operation is placed. That is the order `frame/plan.md` *Overlap with the release* gives for #1583. A row for `1795841828-settle-only-release-note` in that table records it.

```iadd
verdict: fixed c7825eb0
answer: The framer folded it in `c7825eb0`. `## Rule changes` adds the two operations of the paste-ready fix, on `docs/releasing/release-checklist.md` *After the merge* and `docs/releasing/issues-and-milestones.md` *A label says a ticket is already in, before the release ships*. `frame/plan.md` *Overlap with the release* adds a row for `1795841828-settle-only-release-note` (#1667), and the framer's G17 records its placement probe in merge order. This pass ran the probe the finding owes. Round 1's `test_tmp_rule_changes.py`, re-run at `62208e10`, printed no `NOT PLACED` line for either design. This pass's `fix-1/test_tmp_after_both.py`, run once over the same placement, printed the checklist sentence as "Where the job log says one of the release's pull requests could not be read, the note went out with no summary of the pull requests: …" and the label bullet as "a `merged: next` on an issue the release does not carry **fails**, because that is a hand-edit, a squash subject that lost its `(#N)`, or a label the last release's close did not take off". After both, no sentence holds "could not be listed", "always a hand-edit", "hotfix" or "milestone steps" (all executed). The evidence's `git grep` over `docs/` reads the tree, which the settle changes, so it still prints the lines it printed at the target. Each of the two lines this finding names is now under an operation, as the probe shows.
```

### 3. The routing paragraph still sends a gate fix into `main`, the route `frame/questions.md` Q2 removed, and the frame's verdict on that paragraph does not weigh it

```iadd
severity: should
location: `agentory/threads/1795849901-number-read-at-cut/frame/design.md:46`, `agentory/threads/1795849901-number-read-at-cut/frame/design.md:162-163`, `skills/implement/orchestration.md:424-427`
evidence: read `skills/implement/orchestration.md:405-427`, `agentory/threads/1795849901-number-read-at-cut/frame/plan.md:40-52`, `agentory/threads/1795849901-number-read-at-cut/frame/questions.md` Q2; executed `git grep -n -i -E "hotfix|straight (in)?to .?main|takes .main. when|into .main. directly" -- skills agents templates hooks lib bin CONTRIBUTING.md README.md README.ko.md .github` at 4547bb91
```

Why it matters: the owner answered Q2 with (a). After the settle, `docs/releasing/branch-and-release.md` says "Nothing reaches `main` but the release pull request from `release/next`", and gives the reason: a branch merged into `main` beside it makes the next release pull request conflict on `plugin.json`, with no repair through a squash (design G5 (d)). `frame/plan.md`'s failure scenario names that merge as this design's main risk, and says "nothing enforces it beyond the `main` ruleset's required checks, which such a pull request can pass".

The orchestrator routes a pull request by `skills/implement/orchestration.md` *Orchestrator: how the work is routed*. Lines 424-427 of that section say: "The release branch is the default. The orchestrator takes `main` when the accumulated entries read as one release, or when the change is a gate or a hook firing where it should not, which does not wait for other changes." In this repository a gate firing where it should not is exactly the urgent fix the old hotfix row carried. The routing rule still offers it `main`.

The frame's verdict on the section, the row at `frame/design.md:46` ("stay: both state the convention of a repository that names the version ... The version pull request belongs to no work item"), weighs only the version move. *Out of scope* at lines 162-163 rests on that row. Neither weighs the sentence that picks `main`. This is the one statement of a route into `main` outside `docs/` that the search found. The search is a sample under contract rule 12.

The answer belongs to the frame: either the sentence is limited, or the row says why it stays. Limiting it changes a skill an installed plugin ships, so `frame/plan.md` *Operational impact*, which today names only *Scope* item 8's sentence, and `changelog.md` would name it too. A paste-ready form of the first option:

```markdown
<!-- skills/implement/orchestration.md, lines 424-427 -->
where it has not moved already, and the tag follows the merge. The release
branch is the default. Where the repository's convention lets a pull
request other than the release reach `main`, the orchestrator takes `main`
when the accumulated entries read as one release, or when the change is a
gate or a hook firing where it should not, which does not wait for other
changes.

<!-- frame/design.md, line 46, the verdict cell, with this sentence added -->
... so no routing rule there reaches it. The sentence that takes `main` for a gate or a hook firing where it should not is limited to a repository whose convention lets a pull request other than the release reach `main`, which `## Rule changes` leaves none of here (*Scope* item 12)
```

That option also needs a *Scope* item 12 and a row in `frame/plan.md` *Phases* or in the fix pass. The second option keeps the skill as it is. Its row states which document outranks the routing sentence in this repository and where the orchestrator reads that document before it routes.

```iadd
verdict: fixed 83733457
answer: The framer took the first option as *Scope* item 12 and rewrote the verdict row at `frame/design.md:46` in `c7825eb0`. This pass built it in `83733457`. `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, lines 424-429, now reads "The release branch is the default. Where the repository's convention lets a pull request other than the release reach `main`, the orchestrator takes `main` when the accumulated entries read as one release, or when the change is a gate or a hook firing where it should not, which does not wait for other changes." That is the paste-ready sentence, read against *Scope* item 12. The same commit adds a *Changed* entry to `changelog.md`. It also adds the fragment's `### Process changes` table with one row: `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* asks for one once the diff changes a `skills/*/orchestration.md` file, and the work item's diff did not until now. `publish_release_note.py#split_process` read the table's one row from the fragment (executed). No case was added (contract rule 14, weighed). That rule asks a pin of what a person sees and acts on: a message, a verdict, a rendered line. This sentence is guidance an orchestrator weighs when it routes. A case holding its words would re-encode the reading of a judgment as a grammar rule, which `skills/core/SKILL.md` *The first value* keeps out of scripts. So review reads it, as `skills/implement/SKILL.md` gives a rule no case can hold. `git grep -n -i 'accumulated entries\|gate or a hook\|firing where it\|branch is the default' -- tests evals skills agents docs templates` printed no pin, and no other statement of the route outside `skills/implement/orchestration.md` (executed). The evidence's `git grep -n -i -E "hotfix|straight (in)?to .?main|takes .main. when|into .main. directly" -- skills agents templates hooks lib bin CONTRIBUTING.md README.md README.ko.md .github`, run again at `62208e10`, prints nothing. The rewrap puts "takes `main`" and "when" on separate lines, so the search misses the new sentence, which was read at `skills/implement/orchestration.md:425-429`.
```

### 4. `Test_main::test_refuses_a_patch_moved_where_a_feat_reads_a_minor` holds nothing its group does not already hold

```iadd
severity: should
location: `tests/github/test_release_completeness_check.py:368-381`
evidence: read `tests/github/test_release_completeness_check.py:368-446`, `tests/github/test_release_completeness_check.py:211-234`; executed `bin/agentic layout --pairs tests/github/test_release_completeness_check.py` at 4547bb91, which named no pair for it
```

Why it matters: the rule this proofer holds new tests to says a new test that covers nothing its group does not already cover is a `should`. The case builds `Tracker(label=[88], subjects=[FEAT])` with the head at `PATCH` and wires `{10: "Closes #88"}`. That is the same fixture as `test_both_readings_run_on_one_read_of_the_subjects` two cases below it. The case asserts `main() == 1`, `::error::the head moves plugin.json to 0.8.2` and the backticked `feat:` subject in the output.

The case below asserts `main() == 1`, an `::error::` line and the same backticked subject on the same fixture. It also asserts that the label reading ran and that the subjects were read once. `test_both_refusals_are_reported_together` asserts the `::error::the head moves plugin.json` prefix through `main`. `Test_judge_number::test_refuses_a_patch_where_a_feat_reads_a_minor_and_names_each_subject` holds the full `moves plugin.json to 0.8.2` text of the refusal. `test_accepts_a_release_and_measures_from_where_it_left_main` and `test_the_range_is_measured_to_the_head_the_pull_request_names` hold that the head version is read at the head. So every fact in the case is held at the same or a finer grain by another case of the file. S2's wiring is held by the case below it, which already carries the rule marker.

`agentic layout --pairs` compares arguments and bodies, and it did not name this pair. The method is reading, not a mutation run, so the claim is a judgment on the group as it stands.

```python
# tests/github/test_release_completeness_check.py: remove lines 368-381, the
# case `test_refuses_a_patch_moved_where_a_feat_reads_a_minor`, and carry its
# one specific assertion into the case that has its fixture.

    @pytest.mark.rule("a-patch-carries-no-feat")
    def test_both_readings_run_on_one_read_of_the_subjects(self, monkeypatch, capsys):
        """S2 of #1671, through the wiring: a release whose labels agree with
        its range does not let a wrong number through, the head's version is
        the one named, and the range is read once for both readings."""
        m = gate()
        tracker = Tracker(label=[88], subjects=[FEAT])
        tracker.versions["HEAD"] = PATCH
        wire(monkeypatch, m, tracker, {10: "Closes #88"})
        assert m.main() == 1
        out = capsys.readouterr().out
        assert f"::error::the head moves plugin.json to {PATCH}" in out, out
        assert f"`{FEAT}`" in out, out
        assert "D (carried by this release): #88" in out, (
            "the label reading did not run beside the number reading"
        )
        logs = [args for args in tracker.calls if args[0] == "git" and "log" in args]
        assert len(logs) == 1, f"the subjects were read {len(logs)} times"
```

```iadd
verdict: fixed 62208e10
answer: The finding holds, read: the two cases built the same fixture and the second held all but the head version of the first's refusal line. The paste-ready fix was read against the code and applied in this pass's own words. As written, it keeps the name `test_both_readings_run_on_one_read_of_the_subjects` and removes `Test_main`'s one `test_refuses_` case, and `agentic layout --check` refuses a class with none (`trail/phases/phase-1.md`, the paragraph on the first phase-boundary run). So the two cases are one, `Test_main::test_refuses_a_patch_where_a_feat_reads_a_minor_on_one_read_of_the_subjects`, marked `a-patch-carries-no-feat`. It carries the paste-ready docstring and the first case's `::error::the head moves plugin.json to {PATCH}` assertion beside the label and single-read assertions. `git grep` of both old names prints only this record (executed). `bin/agentic layout --check tests/github/test_release_completeness_check.py` printed `0 refused` (executed). The one new assertion of the merged case was shown red (contract rule 15): `agentic mutate .github/scripts/release_completeness_check.py` replacing `plugin.json to {head}, and the subjects` with `plugin.json to {base}, and the subjects` in the refusal, run with `-k on_one_read_of_the_subjects`, printed `red`, failing at `test_release_completeness_check.py:381`, the new assertion (executed). The narrow set, at `62208e10`: `bin/test tests/github/test_release_completeness_check.py tests/lib/test_core.py tests/skills/test_chain_check.py tests/skills/test_settle.py tests/text tests/behaviour -q` printed `1401 passed, 10 skipped`. Every file of it is the `bin/test` suite's, which the *Verified by* cells of phases 1 and 3 name. `tests/lib/test_core.py`, `tests/skills/test_chain_check.py` and `tests/skills/test_settle.py` stand in it because each names `skills/implement/orchestration.md`, which finding 3's fix changed. `uvx ruff check` and `uvx ruff format --check` over the test file were clean. Phase 3's keep search printed nothing, and `bin/agentic rules --check` printed `1 excused in 187 check lines` (all executed). The read of the range, at `62208e10`: `bin/agentic range agentory/threads/1795849901-number-read-at-cut --from 4547bb91 --out <scratchpad>/1795849901-number-read-at-cut/fix-1/range.txt` printed `agentic range: 4547bb91a7e1127bed97b5aaf8c7eb3ae60eaf87..62208e1012e1c5c21c00727241554048c035e7ca` and `wrote: …/fix-1/range.txt, 2020 lines`, and was read to its last line. It made no correction. One statement HEAD contradicts stands in a file a fix pass does not write. `trail/phases/phase-3.md`, the paragraph opening **The fragment carries no `### Process changes` table**, held at the phase's close, and finding 3's fix adds the table, so the orchestrator weighs a fold. The sample `git grep -n 'test_both_readings_run_on_one_read\|test_refuses_a_patch_moved_where_a_feat'` printed only this record. The sample `git grep -n -i -E 'takes .main. when|accumulated entries read as one release|gate or a hook firing' -- . ':!agentory/threads'` printed only `skills/implement/orchestration.md:427-428`, the rewritten sentence. A statement in other words escapes both samples.
```

## Confirmations

No finding was closed before this round, so no `confirms:` line is owed. What matched:

What matched: *Scope* item 1, read at `.github/scripts/release_completeness_check.py:224-287`. `number_read` gives `A.(B+1).0` for a `feat:` subject and `A.B.(C+1)` otherwise. `judge_number` fails only a head that is neither the base nor the number and is not a major above the base with minor and patch 0. It prints the number, both versions and each `feat:` subject, and names near spellings as not read. Executed by hand at the target as `HEAD_SHA=HEAD REPO=MichaelYcJo/AgenticSeal python3 .github/scripts/release_completeness_check.py`. It exited 1 with `the head moves plugin.json to 0.43.0, and the subjects read 0.42.0` and read three `feat:` subjects. That is the refusal `gaps.md` *Not verified* row 5 records and leaves to the orchestrator.

What matched: *Scope* item 2, executed. The phase 1 search of `frame/plan.md`'s *Verified by* cell, run at the target, prints one line opening `>` against `frame/keep-1.txt`: the `milestone_titles` docstring line phase 2 removed. `frame/design.md` *Kept lines of the searches* and `trail/phases/phase-2.md` *The keep files* both say so. The step at `.github/workflows/hygiene.yml:143-161` passes `GH_TOKEN`, `HEAD_SHA`, `BASE` and `REPO` and no `HEAD_BRANCH`.

What matched: *Scope* items 3 and 4, read at `.github/scripts/label_merged_on_release_branch.py:81-107` and `:193-197` and in the diff of `.github/scripts/close_issues_on_release.py`. The label script holds `INTEGRATION_BRANCH` and `MERGED_LABEL` once each and labels a push to `release/next` alone. Its description has 83 characters. The closer spends both labels after the close, on an issue it closed and on one already closed, and only where the read says the issue carries them. *Departure 1* of phase 1, the load of the label script inside `spent_labels`, stands at `close_issues_on_release.py:196-206` as described.

What matched: *Scope* item 5, read at `.github/scripts/publish_release_note.py:591-654` and `:1034-1058`. `merged_pulls` reads the `(#N)` of each subject in the tag's range with `lib/closing.py#MERGED_PR` and makes one `gh pr view` per number. `release_pull_body` lists the pull requests merged into `main` with no head name. `release_mark.py` passes the same range. The phase 2 record lists the new failure path: a hand-written `(#N)` that names an issue drops the summary. The note then goes out without one and fails nothing, so it is no regression of the job. Other new failure paths are a `plugin.json` version that is not `X.Y.Z`, which ends the check loudly at `parts`, and a ref `git show` cannot read. Each is loud, and phase 1 names both.

What matched: *Scope* items 6 to 8 and 11, executed. The phase 2 and phase 3 searches print nothing against `frame/keep-2.txt` and `frame/keep-3.txt` at the target. The old step test path has no citation outside this item's directory. The narrow runs in *Probes* passed.

What matched: the rule changes place, executed. The probe placed every operation of the settle-only item and then of this item on `docs/` at the target. No `from` failed to be found.

The `chain_check.py` run on the branch worktree printed nine notices at lines of `frame/design.md`, each weighed by `docs/running/what-a-script-gates.md` *The checks*. The notice at line 271 says "`tests/text/test_the_rules_claude_md_names_have_one_home.py:64` holds "| a feature branch | `release/vX.Y.Z` | **squash** | *Squash and merge* |", and the `to` does not". That pin holds a table row a person matches against a merge's direction, so it is a fact a reader acts on, which the settle repoints, and `frame/design.md` *Kept lines of the searches* names it. The notice at line 222 names `tests/text/test_the_rules_have_one_owner.py:687`, which holds "*Orchestrator: how the work is routed*". The seven at line 412 name pins holding "*Orchestrator: the order inside a ticket*" or its full citation. Each of those pins reads another file, `skills/implement/orchestration.md` or the core's closing text, where the citation stays, so the operation does not take its text away. None of the nine is a finding.

Two smaller points went into no finding. The case name `Test_create_label::test_refuses_a_name_or_a_description_that_carries_a_number`, at `tests/github/test_label_merged_on_release_branch.py:160`, holds *Scope* item 3's fact but feeds no bad input: `create_label` takes only the repository. The name answers `agentic layout --check`'s demand for a `test_refuses_` case in each class, so the orchestrator may weigh that demand for a function with no input under contract rule 18. The `## Not done` paragraph of `gaps.md:16-19` now records something done: the move it once deferred was built.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head: this round ran narrow modules alone, and the suite stays `unverified` | `agentory/config.json` `Broad gate` | the orchestrator, at the broad gate; the inspector's spawn follows it |
| The changed `hygiene` step on a real `pull_request` run, the label workflow on a real push to `release/next`, the close-issues run that takes `merged: next` off, and the publish reads under the workflow token | `agentory/threads/1795849901-number-read-at-cut/gaps.md:8-10` | the orchestrator, at the runs `gaps.md` names |
| Whether `0.43.0` is the number the subjects read once this branch merges the `main` that holds 0.42.0 | `agentory/threads/1795849901-number-read-at-cut/gaps.md:11` | the orchestrator, after that merge |
| The tracker state the frame read on 2026-11-28, the rulesets of G4 and the milestones of G12, was not read again | `agentory/threads/1795849901-number-read-at-cut/frame/design.md` G4, G12 | the orchestrator, at the tracker acts of `frame/plan.md` *Operational impact* |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_close_issues_on_release.py tests/github/test_publish_release_note.py tests/github/test_release_mark.py tests/github/test_tag_release.py tests/github/test_roll_flow_measurement_issue.py -q` | `325 passed` |
| `bin/test tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/text/test_the_release_check_runs_from_its_step.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/text/test_a_merged_ticket_says_so_on_the_tracker.py -q` | `143 passed` |
| `HEAD_SHA=HEAD REPO=MichaelYcJo/AgenticSeal python3 .github/scripts/release_completeness_check.py` | exit 1: `number read: 0.42.0, the next minor of 0.41.0, from 3 feat: subject(s)`, `plugin.json: 0.41.0 at the base, 0.43.0 at the head`, D and L none |
| the three *Verified by* searches of `frame/plan.md`, each piped to `diff` against its keep file | phase 1: one line opening `>`, the removed `milestone_titles` line; phases 2 and 3: no difference |
| `python3 -I test_tmp_rule_changes.py <worktree>`, under the round's scratch directory `<scratchpad>/1795849901-number-read-at-cut/round-1/`: `rule_changes.py#parse` and `#apply_op` over the settle-only item's design and then this item's, on `docs/` at the target | both parse with no error and every operation is placed; it printed the checklist sentence and the label bullet of finding 2 and the theme sentence of finding 1 as they will stand |
| `bin/agentic layout --pairs` over the eight changed test files | 10 pairs, none of them the pair of finding 4 |
| `python3 skills/code-review/scripts/chain_check.py --baseline release/v0.43.0 --root <worktree> --worktree` | the nine design notices weighed above, and the open-chain notices for a branch with no round, gate or inspection yet |
