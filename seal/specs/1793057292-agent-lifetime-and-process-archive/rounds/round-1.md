# Review round 1: 1793057292-agent-lifetime-and-process-archive

target: 25afe39a against release/v0.22.4

Round 1 has no earlier record, so nothing is carried from a round. The round
read the branch in the worktree the spawn named, at `25afe39a`, against the
fork point `fa7d1374`. No `seal/parity.md` is declared, so no parity
comparison applies. Two facts are carried from the frame and the phase
records without being re-run: the 142 failed hygiene runs in which the
removed step failed in none (`spec.md` *Scope* item 5), and phase 1's reading
of the 0.22.0 transcripts that gives 806,241 (`phases/phase-1.md`). Both are
rows of `## Not judged`.

## Findings

### 1. CI is red on every platform: no shipped prose document names `templates/process.md`

severity: must
location: `templates/process.md`, `agents/framer.md:62-65`, `tests/test_the_pull_request_language_is_the_repositorys.py:818-877`
evidence: executed `gh run view 40428052644 --log-failed`, `bin/test tests/test_the_pull_request_language_is_the_repositorys.py -q -k test_every_template_is_named_by_a_document_that_ships`
verdict: open

The `tests` run 40428052644 at `25afe39a` failed on ubuntu, on macOS group 3
and on Windows group 4. Each leg failed one case and passed the rest:
`test_every_template_is_named_by_a_document_that_ships`, with "templates no
shipped prose document names, so a session bootstrapping one has nothing to
copy: ['templates/process.md']". The same case fails in the worktree.

The case reads the `.md` files under `skills/`, `agents/`, `hooks/` and
`docs/`. `agents/framer.md` names `seal/process/<X.Y.Z>.md` and not the
template. The only text that names `templates/process.md` as the shape to
write from is this spec's `## Rule changes` item for
`docs/release-checklist.md` *2. Gather, bump*, and that reaches `docs/` only
at the settle. `skills/implement/SKILL.md` *3. The SDD file set* states the
same rule in prose: a template no shipped document names is a template a
session cannot find.

Phase 4 claimed that "the 58 test modules that name `templates/` or
`agents/framer.md`" exited 0. This module was not among them, because it
lists `templates` without the slash. `overview.md` *Not verified* labels the
full suite for the orchestrator, so the label was honest and the narrow
selection missed the census.

The framer's line can name the template without becoming a second line:

```markdown
   rounds argued through is not argued again in your `plan.md`. The process
   archive of the highest version, `seal/process/<X.Y.Z>.md`, once, where
   the `seal/` root holds one: what that release changed in the way of
   working, and why, one row per change in the shape of
   `templates/process.md`. The ticket and its comments, and `seal/parity.md`
   where it is declared, which puts the original between the ticket and the
   code.
```

answer: In 2e6c40ed, the framer's archive sentence in `agents/framer.md` step 4 names `templates/process.md` as the shape of each row, in the round's text. `test_every_template_is_named_by_a_document_that_ships` failed at d62c6a6e (exit 1) and passes after the commit. Its module and the nine other modules that read `agents/framer.md` exit 0.

### 2. The draft-tolerance case lost its `def` line, so its body runs inside the new fix-pass case and `.test_durations` still prices it

severity: should
location: `tests/test_the_rules_have_one_owner.py:174-204`, `.test_durations:5471`
evidence: executed `python3 test_tmp_durations.py`, `git grep -n test_a_draft_is_tolerated`
verdict: open

Phase 2 replaced the line `def test_a_draft_is_tolerated_and_still_owes_the_record():`
with `FIX_PASS` and the new case
`test_the_fix_pass_reads_the_implementers_context_before_it_resumes`. The old
case's docstring and its three assertions now follow the new case's last
assertion, as a bare string statement and three more assertions of the new
case. The draft rule is still asserted, so the suite passes. A failure of it
now reports under the fix-pass case's name, and its docstring is no longer
a docstring.

The case no longer exists, and `.test_durations:5471` still prices
`tests/test_the_rules_have_one_owner.py::test_a_draft_is_tolerated_and_still_owes_the_record`.
Phase 3 claimed `.test_durations` prices no removed case. The probe collected
the eleven test modules the branch changed, 698 cases, and compared them
with the file: this is the one entry priced and not collected. The class was
enumerated over those eleven modules, and no other case lost its `def`.

```python
    assert "Orchestrator: a fix pass resumes the implementer" not in text
    assert "never spawn a fresh one while that session still exists" not in text


def test_a_draft_is_tolerated_and_still_owes_the_record():
    """#943 stopped telling an orchestrator to open a draft, and did not
    refuse a repository whose people still open one.
```

The rest of the old case stays as it stands below that line, so its
`.test_durations` entry prices a case that exists again.

answer: In c72c49ae, the `def test_a_draft_is_tolerated_and_still_owes_the_record():` line stands again above its docstring, so the fix-pass case holds only its own assertions. Before the commit, `-k test_a_draft_is_tolerated` selected no case (exit 5). After it, the case is collected under its own name and passes. `mutation-check` over `skills/code-review/orchestration.md`, replacing "still opens a draft is not refused" with "still opens a draft is refused", turned it red under its own name. `.test_durations:5471` now prices a case that exists, and the file is unchanged.

### 3. `docs/the-record-layout.md` still says the shipped workflow runs `unverified-check`, and no rule change covers it

severity: should
location: `docs/the-record-layout.md:186-191`, `seal/specs/1793057292-agent-lifetime-and-process-archive/spec.md:182-279`
evidence: executed `git grep -n -i unverified -- docs`, `git grep -n "turning every" -- seal/specs docs skills`
verdict: open

*The fold, and what tells it from a deletion* says that, read as unusable,
"`unverified-check --baseline` would read the root's own `specs` path as a
typo, turning every pull request after a complete fold red, the shipped
`templates/hygiene.yml` included". Phase 3 removed the step from both
workflows, so no pull request runs the command any more. The sentence is now
false. Phase 3 rewrote the same claim in place in
`unverified_check.py#settled_root`'s docstring ("A person who runs
`unverified-check --baseline origin/<base> seal/specs/` after the settle hands
this tool that path"). The policy copy was left standing, and phase 3's
census of policy sentences named only `docs/one-root-by-lifetime.md` and its
Korean edition. No `## Rule changes` item of this spec or any sibling spec
names the sentence.

Add to `spec.md` `## Rule changes`:

```markdown
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: Read as
    unusable, `settle` would exit 2 on its own finished work, and `unverified-check
    --baseline` would read the root's own `specs` path as a typo, turning every
    pull request after a complete fold red, the shipped `templates/hygiene.yml`
    included.
  to: Read as unusable, `settle` would exit 2 on its own finished work, and
    `unverified-check --baseline`, run by a person after the fold, would read
    the root's own `specs` path as a typo and refuse a finished settle.
```

The `check: an-empty-root-is-settled` line under the paragraph stays: its
cases in `tests/test_unverified_check.py` and `tests/test_settle.py` test
the predicate, not the workflow.

answer: In d62c6a6e, the orchestrator added the `change` item for `docs/the-record-layout.md` *The fold, and what tells it from a deletion* to `spec.md` `## Rule changes`, at `spec.md:280`. Its `to` says a person runs `unverified-check --baseline` after the fold, and the command refuses a finished settle. `settle.py --released-at HEAD` (exit 0) lists it as operation 10 of that section's group, `from found, to not found`. This pass made no commit for the finding.

### 4. `README.ko.md` still lists a segment row's columns without the new context column

severity: should
location: `README.ko.md:251`
evidence: executed `git diff --stat fa7d1374...25afe39a`, `grep -n "session-cost --segments" README.ko.md`
verdict: open

Phase 1 rewrote the `session-cost --segments` row of `README.md` in 765ba3ac,
because it listed a row's numbers without the largest context, and it cited
contract rule 19 for that edit. `README.ko.md` carries the same row, and the
branch does not touch the file. Its list still ends "평균 대기, 토큰".
`CONTRIBUTING.md` *House rules* says both READMEs move together and tell the
same story about what exists. The hygiene step *both READMEs move together*
warns and does not fail, so CI will not catch this.

```markdown
| `session-cost --segments <트랜스크립트>` | 그 실행이 스폰한 에이전트마다 한 행씩, 각자의 트랜스크립트에서 읽어 찍습니다 — 걸린 시간, 호출 수, 한 턴에 나간 도구 수, 평균 대기, 토큰, 그리고 가장 큰 턴 하나가 읽은 컨텍스트. 이 "걸린 시간"은 ...(the rest of the cell unchanged)
```

answer: In 5273fe44, `README.ko.md`'s `session-cost --segments` row ends its list with "토큰, 그리고 가장 큰 턴 하나가 읽은 컨텍스트", as `README.md`'s row does, and the rest of the cell is unchanged. The branch changes no other line of `README.md`, so no other row is left unmirrored. The 24 modules that name `README.ko` exit 0.

### 5. The prevention-home rule's "the work item" names two different work items, so the orchestrator cannot tell which one builds the home or whose issue records it

severity: should
location: `skills/implement/orchestration.md:50-54`, `tests/test_the_rules_have_one_owner.py:366-369`, `seal/specs/1793057292-agent-lifetime-and-process-archive/spec.md:69-72`
evidence: read `skills/implement/orchestration.md:50-54`, `seal/specs/1793057292-agent-lifetime-and-process-archive/phases/phase-2.md:71-76`, `seal/specs/1793057292-agent-lifetime-and-process-archive/overview.md:30`
verdict: open

The rule says the home is "a rule in the work item that rewrites the file
the recurring act is read from" and that the orchestrator records it "in a
comment on that work item's issue". Read one way, the work item is the one
the run is building. Read the other way, it is whichever work item rewrites
that file, which may be another branch or no work item yet. Phase 2 and
`overview.md` *Not verified* flagged the two readings and left them to the
orchestrator. `CLAUDE.md` *text an agent or a check reads has one reading*
asks that a thing more than one party can have is named with whose. The
ticket's own words, "in the item that rewrites the file", carry the same two
readings, so the frame copied the ambiguity from the issue.

The sentence's own frame settles it for the first reading. "At once" and
"before the next spawn" bind the run in progress. Only the work item in
progress has a next spawn this orchestrator controls. The same section's
folding rule is the route by which a run adds a rule to its own frame. The
owner can take the other reading at the pull request. Either way the
sentence has to name which work item.

```markdown
**A problem that recurs within a run gets a prevention home at once.** When
the same problem appears a second time in one run, the orchestrator gives it
a home before the next spawn: a mechanism that stops it, or a rule written
into the file the recurring act is read from. The work item in progress
builds that home. The orchestrator folds it into that work item's frame, as
any decision after the frame is folded, and records the home in a comment on
the issue of the work item in progress.
```

The pins at `tests/test_the_rules_have_one_owner.py:366-369` follow the new
words. *Scope* item 4's last bullet in `spec.md` is the frame's sentence,
and the orchestrator folds the answer there.

answer: In 098d2b45, the prevention-home rule in `skills/implement/orchestration.md` takes the round's text: the work item in progress builds the home, and its issue records it. The pins in `test_a_recurring_problem_gets_a_prevention_home` follow the new words, and the changed pin failed against the old text before the rule was rewritten (exit 1). The changelog fragment's item says the same in the same commit. *Scope* item 4 of `spec.md` and `overview.md` *Not verified* row 4 still carry the two readings, and they are the orchestrator's fold.

### 6. Two of the order's new rules leave out who acts: who writes the line naming the comments to fold, and which of two orchestrators deletes `handoff.md`

severity: should
location: `skills/implement/orchestration.md:36-39`, `skills/implement/orchestration.md:44-48`
evidence: read `skills/implement/orchestration.md:33-48`, `skills/implement/orchestration.md:58-74`
verdict: open

The folding rule says "`plan.md` carries one line of its own below its
approval line naming the comments to fold". It names no writer, only the
party that deletes the line. It also places the line below an approval line
that a plan does not have between the frame's commit and the first spawn.
That is the usual window in which a person answers `questions.md`. *The plan
is approved at the spawn* puts the approval line under the title, so a line
written below the title before approval still ends up below the approval
line.

The `handoff.md` rule says "The orchestrator writes a `handoff.md` ... and
deletes it once the session that takes the work over has read it". A move
has two orchestrators. The one that wrote the file has stopped. Only the
receiving session knows when the file has been read. "The orchestrator"
therefore names whichever one the reader is, and the writing session cannot
do the deletion it is told to do.

This is one class: an act in the three new rules with no named actor, or
with an actor two parties could be. Finding 5 is its third member.

```markdown
**A decision made after the frame is committed is folded, in place, into
`spec.md` or `plan.md` before the next smith spawns.** The orchestrator
rewrites the sentence of the frame the decision changes, where it stands,
because a smith reads the frame and not the issue's comments. Until the
decision is folded, the orchestrator keeps one line of its own in `plan.md`
naming the comments to fold, below the approval line where the plan carries
one and below the title where it does not, and deletes that line in the
commit that folds them. Before the frame is committed, the orchestrator
folds the decision into the issue body instead
(`docs/issues-and-milestones.md` *An issue is its body and its comments
together*).

**Where a work item stands is read from `plan.md`'s Status column,
`overview.md` and the phase records.** The orchestrator that hands the work
over writes a `handoff.md` in the work item's directory only to move the
work to another session or another machine. The orchestrator that takes the
work over deletes it once it has read it.
```

The pins in `test_a_decision_after_the_frame_is_folded_into_it` and
`test_a_handoff_file_is_written_only_to_move_the_work` hold the new text
unchanged ("naming the comments to fold", "a `handoff.md` in the work item's
directory only to move the work to another session or another machine",
"deletes it once").

answer: In 5be7d538, both rules take the round's text. The orchestrator keeps the fold line in `plan.md`, below the approval line where the plan carries one and below the title where it does not. The orchestrator that hands the work over writes `handoff.md`, and the orchestrator that takes it over deletes it. The two cases gained pins for the named actors ("the orchestrator keeps one line of its own in `plan.md`", "below the title where it does not", "The orchestrator that hands the work over writes", "The orchestrator that takes the work over deletes it once"), and both cases failed against the old text first (exit 1). The changelog fragment's two items say the same in the same commit.

### 7. `overview.md` reports a divergence on the threshold that 25afe39a removed, and quotes a spec sentence that is gone

severity: should
location: `seal/specs/1793057292-agent-lifetime-and-process-archive/overview.md:16`
evidence: read `seal/specs/1793057292-agent-lifetime-and-process-archive/overview.md:16`, `seal/specs/1793057292-agent-lifetime-and-process-archive/spec.md:29-37`
verdict: open

The row says *Scope* item 2 reads "is below 461,000 tokens", and its grounds
quote *Scope* item 2 as saying "Phase 1 measures it again". At `25afe39a`,
*Scope* item 2 says 806,241 and that phase 1 measured it, and the quoted
sentence is gone. Spec and code now agree, so no divergence is left to
report. The sealer reads this memo, and the pull request body copies its
factual sentences, so the false row would reach the pull request.

Delete the row at `overview.md:16`. The table keeps its other four rows.

answer: In 822d3776, the threshold row leaves `overview.md` *Where spec and implementation diverged*, and the table keeps its other four rows. `unverified-check` over the work item and the modules that read `overview.md` records exit 0.

## Confirmations

confirms: none
The removed gate leaves nothing that runs, cites or counts it.
`.github/workflows/hygiene.yml` and `templates/hygiene.yml` hold no step and
no comment naming `unverified_check.py`. `broad_gate.py` holds no
`UNVERIFIED`, `UNVERIFIED_NAME`, `SPECS`, `PARTITION` row or `run` call for
it, its docstring numbers the arms 1 to 3, and `--preflight` says "arms 2 and
3". `CONTRIBUTING.md` counts two shipped steps, and the template holds the
chain and mode steps beside the clone step. `tests/test_arm_check.py` names
no `unverified` arm, as phase 3 said (0 hits). Executed with `git grep`
and `grep -c`. The CI run at `25afe39a` passed every case on Linux, macOS
and Windows except finding 1's case. That includes
`tests/test_the_gate_names_every_step_ci_runs.py`, `tests/test_broad_gate.py`
and the teammate end-to-end module. Executed with `gh run view`.

confirms: none
The gate-change account stands in `overview.md` *The gate change, for the
pull request* and in the changelog fragment's `### Removed` item. It gives a
failure direction (the gate allows more: a deleted row passes CI and the
broad gate), a prompt budget of zero, the platforms, and what it removes.
Each is true against the diff. The platform line deferred Linux and Windows
to CI. The CI run has answered them: red only on finding 1, which does not
involve the removed step. Read.

confirms: none
`chain_check.py#follows` lists the branch's commits with
`rev-list --no-merges HEAD ^<target> ^<base>` (`skills/code-review/scripts/chain_check.py:1493-1495`).
A merge commit is never read, and the base's commits it brings in are
excluded. So the merge route's sentence, that the chain check reads no merge
commit and a resolution outside the records needs its own verifying round,
is true. The three `mergeable` values the paragraph reads, `MERGEABLE`,
`CONFLICTING` and `UNKNOWN`, are the three GitHub returns. Read.

confirms: none
The threshold has one living source. 806,241 stands in
`skills/code-review/orchestration.md:30`. Its pin is
`tests/test_the_rules_have_one_owner.py:141`, and the rest are this work
item's records (`spec.md`, `questions.md`, `overview.md`, `changelog.md`).
No other skill, agent definition or document states it. Executed with
`git grep -n "806,241\|806241\|461,000"`. The acts-table row cites the
section and does not restate the number.

confirms: none
The `session-cost` column holds against S1 to S3. A turn is one message
carrying a `usage` block, keyed by `message_key`. A split message keeps each
input field at its largest value across its rows. `CONTEXT_FIELDS` names
all three input fields. A window with no message answers None and prints a
dash. `segment_slices` reads a resumed file once for the column
(`largest_context(transcript, cuts)`) and takes each kept slice's value at
its window. `load`'s `turns` and `token_thirds` are unchanged. Read at
`skills/verify/scripts/session_cost.py:1986-2047` and `1695-1741`. The file
is opened as UTF-8 with replacement, with no path join of its own, and the
Windows legs ran `tests/test_session_cost.py` green. Executed with
`gh run view`. A harness task output names a `.output` symlink to the
agent's `agent-*.jsonl`. The fix-pass sentence names the `.jsonl` itself, so
the orchestrator types the right file. Executed with `ls -la` over this
session's tasks directory.

confirms: none
Every `## Rule changes` operation parses and finds its `from`. The dry run
at `--released-at HEAD` places this spec's twelve operations in twelve
groups. Every `change` and `remove` reads `from found`, and every `to` and
`add` reads `not found`. No sibling spec in a shared group changes the same
text. Executed with `python3 skills/settle/scripts/settle.py --released-at HEAD`.

confirms: none
S8 holds: `git grep -n "a phase is re-run" -- . ":!seal/specs" ":!changelog"`
prints nothing and exits 1. S14 holds by reading. `agents/framer.md` step 4
gains one sentence naming the archive of the highest version, read once
where the root holds one, and no other line of the definition changed. The
sentence that the orchestrator deletes the fold line in the folding commit
(`overview.md` *Not verified*, row 4) reads as one act with its moment. No
case pins it, and the acts table delivers the section as `still a sentence`.
Executed for the grep, read for the rest.

confirms: none
The new cases do not duplicate their groups. `bin/test-layout --pairs` over
`tests/test_session_cost.py`, `tests/test_the_rules_have_one_owner.py`,
`tests/test_review_axes.py` and `tests/test_a_record_carries_no_comment.py`
names 20 pairs, and none of them involves a case this branch added. Rules 17
and 18 pin the two bold sentences. `test_the_fix_pass_reads_the_implementers_context_before_it_resumes`
pins the command and the hand-over. `test_review_axes.py#test_the_fix_pass_resumes_the_implementer`
pins the reason, the fallback and the compaction limit. No phrase is pinned
twice. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three; the dispatched `tests` run is finding 1's evidence, not the broad gate | `broad-gate.md` | the orchestrator, by `broad-gate --base release/v0.22.4 --record` once the rounds settle |
| That the removed step failed in none of 142 failed hygiene runs from 2026-09-23 to 2026-10-25. Carried from the frame, not re-run | `spec.md` *Scope* item 5 | the sealer, in its sample of claims |
| That 806,241 is the largest context a fresh, never-resumed smith reached in the 0.22.0 run. Carried from phase 1's reading of the transcripts, not re-run | `phases/phase-1.md` | the sealer, in its sample of claims |
| Q1, no archive files for 0.22.0 to 0.22.3, and Q2, a merge and never a rebase, both on their defaults | `questions.md` Q1, Q2 | the owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `gh run view 40428052644 --log-failed` | at `25afe39a`: ubuntu 1 failed and 6556 passed, macOS group 3 1 failed, Windows group 4 1 failed, each `test_every_template_is_named_by_a_document_that_ships` naming `templates/process.md`; every other job green |
| `bin/test tests/test_the_pull_request_language_is_the_repositorys.py -q -k test_every_template_is_named_by_a_document_that_ships` | exit 1, 1 failed |
| `python3 test_tmp_durations.py` (collects the 11 changed test modules with `bin/test --collect-only -p no:xdist` and compares with `.test_durations`) | 698 collected; 1 priced and not collected, `test_a_draft_is_tolerated_and_still_owes_the_record`; the probe file is deleted |
| `python3 skills/settle/scripts/settle.py --released-at HEAD` | exit 0; this spec's 12 operations, each `from found` where it has a `from` |
| `bin/test-layout --pairs` over four changed test modules | exit 0, 20 pairs, none involving a new case |
