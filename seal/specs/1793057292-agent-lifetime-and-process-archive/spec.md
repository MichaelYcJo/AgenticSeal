# Feature Specification: #945 an agent lives one phase, the orchestrator's steps sit where it acts, two re-checks leave, and each release records how the process changed

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A mechanism stays only while its history shows what it caught against what it costs, and a thing is re-checked only when the diff or CI shows it changed. The audit in *Scope* item 4 applies it to the two re-checks this item owns, and nothing is kept because it exists |
| `CLAUDE.md` *The goal a design is chosen against* | Nothing this item adds asks a person anything mid-run. The agent-lifetime rule is decided by a number the orchestrator reads, not by a question |
| `CONTRIBUTING.md` *What a change to a gate must carry* | Phase 3 takes one step out of two workflows and one arm out of the broad gate. The pull request states the failure direction (the gate allows more: a row deleted rather than closed passes CI), a prompt budget of zero, and what it removes (`## Removes`) |
| `skills/implement/SKILL.md` *3. The SDD file set* | The work changes what the orchestrator and the framer read and act on, and what the broad gate prints, so it is on the top rung |
| `docs/release-checklist.md` *0. Before starting* | **Never rebase a work item's branch, for any reason.** The ticket's rebase rule is read against this (`questions.md` Q2) |
| `docs/the-review-record.md` *The handoff* | What a fresh spawn is handed: coordinates, each fact labelled. The agent-lifetime rule hands a fresh smith the phase records and a brief in that shape |
| `docs/the-record-layout.md` *seal/* and *Every kind of record, at a glance* | The process archive is a new kind of record under the `seal/` root, so it gets a row in both tables (`## Rule changes`) |
| `docs/issues-and-milestones.md` *An issue is its body and its comments together* | Today it offers an `Update <date>` block written beside the old body as one of two ways. The folding rule replaces that with a body rewritten in place (`## Rule changes`) |
| `docs/measuring-a-run.md` *The unit is a segment, and a segment has its own transcript* | The largest per-turn context becomes part of a segment's reading (`## Rule changes`) |
| #940's frame, `seal/specs/1792540458-on-demand-files-state-the-current-rule/questions.md` Q2 | #940 left this ticket's orchestrator rules to this frame (default (b), `read`), so the two orchestration files are rewritten here, in place, and not by #940 as the ticket's body says |
| #944's frame, `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/spec.md` *Out, and whose* | The unverified reader, round-record inheritance and the hand-back re-run were measured there and left to this ticket to judge |
| #923's frame, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md` *Grounding*, the `#945 §3` row, and its table of what leaves | Round-record inheritance moved to #923, and #923 took out `round-N-report.md` and the `## Inherited coordinates` section (`read`). Nothing of it is left for this item |
| `tests/conftest.py#census_case` and #949's closing comment | #949 closed as not planned on 2026-10-15, merged into #942: each module's own test file runs every census over its module (`executed`, `gh issue view 949`; `git grep -n census_case -- tests` returns 146 lines). That is the class of the one catch the hand-back re-run has on record |

## Scope

**In.**

1. **An agent lives one phase.** Each phase of a work item is a fresh
   `smith` spawn, handed the phase records the earlier phases wrote and a
   brief in the shape of `docs/the-review-record.md` *The handoff*. The
   orchestrator never resumes a smith across a phase boundary.
2. **A fix pass resumes the implementer only while its context is small.**
   The implementer is the smith that wrote the last commit the round
   reviewed. A fix pass resumes it while its largest per-turn context, read
   with `session-cost --segments` on its own transcript, is below 806,241
   tokens, and is a fresh spawn handed the round record and the phase records
   otherwise. A fix pass also takes a fresh spawn where the implementer's
   session no longer exists, as today. The figure is the largest context a
   fresh, never-resumed smith reached in the 0.22.0 run, measured by phase 1
   with the new column (`executed`, `phases/phase-1.md`; `questions.md` Q3).
3. **`session-cost --segments` reports each segment's largest per-turn
   context.** It is a column of the table and a key of each `--json` row,
   and it gates nothing.
4. **The orchestrator's steps sit in the file it reads at the act.** None
   goes into `CLAUDE.md`.
   - `skills/code-review/orchestration.md`: rules 1 and 2 above, rewritten
     in place over *Orchestrator: a fix pass resumes the implementer*.
   - Same file, *Orchestrator: the pull request opens once the sealer seals*:
     after the pull request opens, and after each push to it, the
     orchestrator reads `gh pr view <N> --json mergeable` before it waits on
     CI. `CONFLICTING` means GitHub made no merge ref and runs no
     `pull_request` CI, and nothing else says so. `UNKNOWN` is read again.
   - Same section: a conflict with the base is integrated by merging the base
     into the branch, never by a rebase (`docs/release-checklist.md` *0.
     Before starting*). The merge is taken once, after the branch it
     conflicts with has landed. A merge that resolved a conflict in a file
     outside the work item's records gets a verifying round on that
     resolution, because the chain check reads no merge commit
     (`skills/code-review/scripts/chain_check.py#follows` lists commits with
     `--no-merges`, `read`). The broad gate and the sealer then run again,
     as the section's repair path already says.
   - `skills/implement/orchestration.md` *Orchestrator: the order inside a
     ticket*: a decision made after the frame is committed is folded, in
     place, into `spec.md` or `plan.md` before the next smith spawns, by the
     orchestrator. Until it is folded, the orchestrator keeps one line in
     `plan.md` naming the comments to fold, below the approval line or, where
     the plan has none yet, below the title. Before framing, the decision is
     folded into the issue body (`## Rule changes`, the
     `docs/issues-and-milestones.md` item).
   - Same section: where a work item stands is `plan.md`'s Status column,
     `overview.md` and the phase records. The orchestrator that hands the
     work over writes a `handoff.md` only to move the work to another session
     or machine, and the orchestrator that takes it over deletes it once read.
   - Same section: when a problem recurs within a run, the orchestrator gives
     it a prevention home at once, before the next spawn, as a mechanism or as
     a rule in the file the act is read from. The work item in progress
     builds that home, and the orchestrator records it on that work item's
     issue (round 1 findings 5 and 6).
5. **The audit of the re-checks this ticket owns.** Each verdict's grounds
   are in `plan.md` *Alternatives considered*.
   - **The orchestrator's re-run of each hand-back is deleted.** Its one
     catch on record, #929's census defect on 2026-10-14 (the ticket's body,
     `read`), belongs to a class each module's test file now closes
     (*Grounding*, the `census_case` row).
   - **The unverified record loses its two gate arms and keeps its reader.**
     The CI step *the unverified record is readable, and rows leave it
     closed* (in `.github/workflows/hygiene.yml` and `templates/hygiene.yml`)
     and the broad gate's `unverified` arm leave. In 142 failed hygiene runs
     from 2026-09-23 to 2026-10-25, that step failed in none (`executed`,
     `gh run list --workflow hygiene.yml --status failure` and each run's
     failing steps). Its recorded issues are its own defects (#272, #612,
     #688), and #1034 fixed another one two days ago. What stays:
     `unverified_check.py` as the module ten readers import, the
     `unverified-check` command a person types, its `--baseline` mode with
     the rules `docs/the-record-layout.md` states for it, and `settle`'s
     list of every open row of a released record.
   - **Round-record inheritance** is #923's and already gone. No act here.
6. **The process archive.**
   - `templates/process.md`: the shape of `seal/process/<X.Y.Z>.md`, a title
     and one table, `| Date | Change | Why | Source |`, one row per change.
   - The release-checklist step that writes it at release preparation, once
     per release, from the milestone's issue comments and the history of the
     base files (`## Rule changes`, the `docs/release-checklist.md` *2.
     Gather, bump* item). The base is `CLAUDE.md`, `agents/*.md` and
     `skills/*/orchestration.md`. `skills/verify/orchestration.md` counts,
     because #940 split the orchestrator's verify half into it
     (`executed`, `git show --stat 5aed51cb`).
   - Rows for the archive in `docs/the-record-layout.md` (`## Rule changes`).
   - One line in `agents/framer.md` step 4: read the latest
     `seal/process/<X.Y.Z>.md` once, where the `seal/` root holds one. No
     spawn preloads it.

**Out, and whose.**

- The survivor sweep: deleted in #944. The census in the narrow runner: #949,
  closed into #942. The CI legs per pull request: #943. All three are closed
  (`executed`, `gh issue view`).
- Round-record inheritance: #923, landed at 8350c578.
- The `--baseline` mode of `unverified-check` and the reader module: kept
  (`plan.md` *Alternatives considered*, row U-C).
- Archive files for 0.22.0 to 0.22.3: not written (`questions.md` Q1).
- The first archive file: written at the preparation of the release that
  ships this item, by whoever prepares it, not by this work item.
- A size check on the archive: none. Its size is a row of the release
  report #923 built (`.github/scripts/release_report.py`, the
  `release-report` job of `.github/workflows/test.yml`): the report's
  document glob reaches `seal/process/*.md`, so each archive file's bytes
  are printed beside the other documents', at the last release tag and now.
  The report fails nothing. No `seal/budgets.md` has ever been committed
  (`executed`). The frame first missed the report because its name is
  hyphenated (the sealer's withhold, 085530de).
- Every policy document: changed only through `## Rule changes`, never by a
  commit of this branch.

**Limits, stated and not guarded.**

- Until a settle applies this spec, the archive step stands in this spec's
  `## Rule changes` and not in `docs/release-checklist.md`. The release
  preparation that ships this item reads it there, as the policy in force.
- A repository whose workflow was installed from an earlier release keeps
  the unverified step until `seal pr-checks install` writes the file again,
  because the workflow is pinned to the release that wrote it.
- The threshold reads the implementer's largest turn, so a compaction that
  shrank its context still reads the size before it. The orchestrator then
  spawns fresh where a resume was possible, which costs calls and is the
  cheaper mistake.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the column | Given a run's transcript with segments beside it, When `session-cost --segments <it>` runs, Then each row prints its largest per-turn context, and each `--json` row carries it under one key | a case class of its own in `tests/test_session_cost.py`, seen red with the column's computation removed |
| S2 a turn's context | Given one assistant message split over several rows of the transcript, When the column is computed, Then the message counts once, and its context is `input_tokens` + `cache_creation_input_tokens` + `cache_read_input_tokens` | the same class, a case with a split message and a case with all three fields |
| S3 a resumed file | Given a resumed agent's own transcript, When `--segments` cuts it into slices, Then each slice prints its own largest context; a slice with no assistant message prints a dash, never 0 | the same class |
| S4 the threshold measured | Given the 0.22.0 run's transcripts where they are still on disk, When phase 1 runs the column over them, Then its phase record states the largest context of the resumed smith and of each fresh smith, and says which transcripts were gone | `phases/phase-1.md`, labelled `executed` |
| S5 a phase spawns fresh | Given a closed phase, When the orchestrator reads `skills/code-review/orchestration.md`, Then it reads that the next phase is a fresh smith handed the phase records, and that a fix pass resumes only below the threshold, with the command that reads it | `tests/test_the_rules_have_one_owner.py`, a case pinning the rule's bold sentence |
| S6 the acts table | Given the renamed fix-pass heading and the shortened sealer heading, When `tests/test_every_orchestrator_act_names_its_delivery.py` runs, Then both headings have their row and no row names a heading that is gone | that module |
| S7 mergeable | Given an open pull request, When the orchestrator is about to wait on CI, Then the section it reads names `mergeable`, what `CONFLICTING` and `UNKNOWN` mean, and the merge route with its verifying round | a pin in `tests/test_the_rules_have_one_owner.py` |
| S8 the hand-back re-run is gone | When `git grep -n "a phase is re-run"` runs outside `seal/specs` and `changelog`, Then it prints nothing; the paragraph *A hand-back's verification claim is a claim* is gone and so is its pin | the grep, and the module's case list |
| S9 folding, handoff, prevention home | Given `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, Then it states the three rules of *Scope* item 4 that name it | a pin each in `tests/test_the_rules_have_one_owner.py` |
| S10 the unverified arms are gone | When the broad gate runs, Then its summary lists no `unverified` arm; `.github/workflows/hygiene.yml` and `templates/hygiene.yml` hold no step running `unverified_check.py`; `PARTITION` and the workflow still agree | `tests/test_broad_gate.py`, `tests/test_arm_check.py` and `tests/test_the_gate_names_every_step_ci_runs.py`, which holds `PARTITION` to the workflow |
| S11 the reader stays | When `unverified-check seal/specs/` and `unverified-check --baseline <ref> seal/specs/` run, Then each prints as before; `settle` still lists open rows | `tests/test_unverified_check.py` and `tests/test_settle.py` unchanged and green |
| S12 the teammate flow | Given the template with one step fewer, When `tests/e2e/teammate/test_teammate_flow.py` runs, Then every remaining step passes a pull request that declares nothing | that module |
| S13 the archive template | Given `templates/process.md`, When the template censuses run, Then it carries no comment and its field words are plain words | `tests/test_a_record_carries_no_comment.py`, `tests/test_the_record_is_written_in_words.py` |
| S14 the framer line | Given `agents/framer.md`, Then step 4 names the latest `seal/process/<X.Y.Z>.md` once, where the root holds one | the warden reads it; the line is the only change to the definition |

## Data & interfaces

- `skills/verify/scripts/session_cost.py`: a new function computing one
  slice's largest per-turn context from the slice's assistant messages, each
  message counted once by its key, as `load` counts turns. Its cases form a
  class of their own in `tests/test_session_cost.py`, named after the
  function, so the branch of #1017, which adds cases to other classes of
  that file, meets this one only as text. `report_segments` prints the value
  as a column. `measure_segments` puts it on each row under one key, which
  `--json` prints. The run-level `context` line `token_thirds` feeds is
  unchanged.
- `skills/verify/scripts/broad_gate.py`: the `unverified` arm, its name
  constant, its `run` call and its `PARTITION` row leave. The record
  `broad-gate.md` names no arm today (`read`, the latest one under
  `seal/specs`), so no reader of it changes.
- `.github/workflows/hygiene.yml` and `templates/hygiene.yml`: the step
  *the unverified record is readable, and rows leave it closed* and the
  comments that explain it leave.
- `templates/process.md`, new: a title line `# Process changes: X.Y.Z` and
  the table `| Date | Change | Why | Source |`. A row's Source is a link to
  the issue comment or the commit the change came from.
- `seal/process/<X.Y.Z>.md`: written from it at release preparation. No
  file is written by this branch.

## Rule changes

- add
  file: docs/measuring-a-run.md
  section: The unit is a segment, and a segment has its own transcript
  to: **A segment's reading carries the largest context any one of its turns
    read.** A turn's context is the input side of its one model call: the
    tokens sent fresh, the tokens written to the cache and the tokens read
    from it, each message counted once. A resumed agent pays its whole
    earlier context again on every turn, so its largest turn is the number
    that tells a resume worth taking from one that is not, and the
    orchestrator reads it before it resumes an implementer for a fix pass.
    It is measured, and it gates nothing.
    check: tests/test_session_cost.py
- change
  file: docs/issues-and-milestones.md
  section: An issue is its body and its comments together
  from: What the body owes in return is that nobody has to **reconcile** it. A body that contradicts a comment leaves the reader to work out which is current. Two ways to pay it, and which one fits depends on whether the original text is worth keeping:
  to: **A decision is folded into the body in place, and the comment that
    carried it records why.** A body that contradicts a comment leaves the
    reader to work out which is current, and a block of updates written
    above the old text leaves two versions to choose between. GitHub keeps
    the body's edit history, so rewriting it loses nothing. Once an item is
    framed, its frame is what the builder reads, and a later decision is
    folded into the frame instead (`skills/implement/orchestration.md`
    *Orchestrator: the order inside a ticket*).
    check: none reader: the framer at every frame
- remove
  file: docs/issues-and-milestones.md
  section: An issue is its body and its comments together
  from: - **Consolidate the body**, once the design is settled. The comments stay and are still part of the issue; what goes away is the need to cross-check four places to learn what the ticket asks for.
- remove
  file: docs/issues-and-milestones.md
  section: An issue is its body and its comments together
  from: - **Leave the body and open it with `> **Update <date>.**`**, naming what has moved since it was written: the original design is preserved and the block says which things below it have changed.
- change
  file: docs/release-checklist.md
  section: 0. Before starting
  from: - [ ] **Squash the work items back to back.** `unverified_check` resolves its baseline to `git merge-base <the base ref> HEAD`, so a work item squashed into the release branch after a sibling forked is not that sibling's removal. Merge the release branch into a work item's branch only when the branch needs something the release branch holds; the squash discards the merge commit either way.
  to: - [ ] Merge the release branch into a work item's branch only when the
    branch needs something the release branch holds; the squash discards
    the merge commit either way.
- remove
  file: docs/release-checklist.md
  section: 3. Verify before committing
  from: python3 skills/verify/scripts/unverified_check.py --baseline origin/main seal/specs/
- add
  file: docs/release-checklist.md
  section: 2. Gather, bump
  to: **The preparation commit writes the process archive,
    `seal/process/X.Y.Z.md`, from `templates/process.md`.** The archive
    records what this release changed in the way of working and why, one
    row per change: `CLAUDE.md`, `agents/*.md` and
    `skills/*/orchestration.md` are the way of working, and
    `git log vA.B.C..HEAD` over those paths with the milestone's issue
    comments gives the rows. Each row is a date, the change, one line of
    why, and a link to the issue comment or commit it came from, and nothing
    else. It is written once, here, because one file that every branch edits
    is the conflict the changelog fragments ended. A release that changed
    none of those files writes no archive file.
    check: none reader: the framer of the next release
- change
  file: docs/the-record-layout.md
  section: Every kind of record, at a glance
  from: | The follow-up list | `seal/follow-up.md`, one row per item that waits on a named party | under target | its rows, each naming who answers it |
  to: | The follow-up list | `seal/follow-up.md`, one row per item that waits on a named party | under target | its rows, each naming who answers it |
    | The process archive | `seal/process/<X.Y.Z>.md`, one file per release, written at its preparation | each file under target | the file name, by version |
- change
  file: docs/the-record-layout.md
  section: seal/
  from: | `seal/follow-up.md` | which items wait on a named party, and who |
  to: | `seal/follow-up.md` | which items wait on a named party, and who |
    | `seal/process/<X.Y.Z>.md` | what one release changed in the way of working, and why |
- change
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  from: `broad-gate.md`, `guarantee.md`, and a `handoff.md` or `pr.*.md` where one was written)
  to: `broad-gate.md`, `guarantee.md`, and a `pr.*.md` where one was written)
- change
  file: docs/one-root-by-lifetime.md
  section: Shared or local
  from: A hygiene workflow left behind in local mode is red forever:
    `unverified_check.py` runs second and exits 2 for a path that is nowhere,
    and with no `continue-on-error` the job stops, so `chain_check.py` never runs.
    Had it run, it would have exited 0 having examined nothing.
  to: A hygiene workflow left behind in local mode passes having examined
    nothing: `chain_check.py`, the one record check it runs, finds no root
    in the tree and exits 0.
- change
  file: docs/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: local 모드에 남은 hygiene 워크플로는 영원히 빨간불입니다.
    `unverified_check.py` 가 두 번째로 돌면서 어디에도 없는 경로에 대해 2 로
    끝나고, `continue-on-error` 가 없으니 잡이 멈춰 `chain_check.py` 는 돌지
    않습니다. 돌았다면 아무것도 안 본 채 0 으로 끝났을 것입니다.
  to: local 모드에 남은 hygiene 워크플로는 아무것도 보지 않은 채 통과합니다.
    그 워크플로가 돌리는 기록 검사는 `chain_check.py` 하나뿐이고, 트리에서
    루트를 찾지 못해 0 으로 끝납니다.
- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: would read the root's own `specs` path as a typo, turning every
    pull request after a complete fold red, the shipped `templates/hygiene.yml`
    included.
  to: would read the root's own `specs` path as a typo when a person runs it
    after the fold, and refuse a finished settle.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The rule that a fix pass always resumes the implementer while its session exists | `skills/code-review/orchestration.md` *Orchestrator: a fix pass resumes the implementer*, its first bold sentence and the paragraph after it | rewritten in place to *Scope* items 1 and 2, under a heading that names both |
| The heading *Orchestrator: a fix pass resumes the implementer* and its row | the heading, and its row in `skills/implement/orchestration.md` *Orchestrator: which of these acts runs itself* | the renamed heading and its row, rewritten in the same commit |
| The orchestrator's re-run of each hand-back | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals, and a phase is re-run*, the paragraph *A hand-back's verification claim is a claim.* | nothing replaces it: its one catch's class is closed by `tests/conftest.py#census_case` (*Grounding*) |
| The clause *and a phase is re-run* in that heading, and every citation of it | the heading; `CONTRIBUTING.md` *Opening a pull request*; `skills/implement/SKILL.md` *6. Drain the rows before the broad run, and keep the records*; `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* and the acts table's row and grounds | the shortened heading, cited by the same words everywhere in the same commit |
| The pins on the re-run and on the old heading | `tests/test_the_rules_have_one_owner.py`, the case `9 a hand-back's verification claim is a claim` and the constant `AFTER_THE_SEAL`; `tests/test_broad_gate_rule.py`, the heading string | the case leaves; the strings follow the new heading |
| The CI step of the unverified record | `.github/workflows/hygiene.yml`, the step *the unverified record is readable, and rows leave it closed* and its comment block | no catch in 142 failed runs (*Scope* item 5); the review reads an overview's diff |
| The same step shipped to users | `templates/hygiene.yml`, that step, its comment and the header comment that names `unverified_check.py` | the same; `CONTRIBUTING.md` *Running the checks*, the sentence counting three shipped steps, is rewritten to two |
| The broad gate's `unverified` arm | `skills/verify/scripts/broad_gate.py`: the docstring's arm 2, `UNVERIFIED`, `UNVERIFIED_NAME`, the `PARTITION` row and the `run` call; the cases in `tests/test_broad_gate.py` and `tests/test_arm_check.py` that name that arm | the same; the phase enumerates every other case naming the arm or the step by `git grep -n -i unverified -- tests skills/verify .github templates` |
| The sentence that a deleted row fails the next pull request | `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show*, the sentence naming `unverified-check --baseline origin/<base>` as what fails the pull request | rewritten in place: the warden reads the overview's diff, and the command names a row that left without closing when a person runs it |
| The release-day ordering for the unverified baseline | `docs/release-checklist.md` *0. Before starting*, the bullet's first sentences; *3. Verify before committing*, the `unverified_check.py` line | `## Rule changes` |
| The `Update <date>` block as a way to amend an issue body | `docs/issues-and-milestones.md` *An issue is its body and its comments together* | `## Rule changes`: the body is rewritten in place |
| A `handoff.md` kept until the settle | `docs/the-record-layout.md` *seal/specs/<work-item-id>/* | `## Rule changes`; the act is in `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-27 by framer, before the build.
