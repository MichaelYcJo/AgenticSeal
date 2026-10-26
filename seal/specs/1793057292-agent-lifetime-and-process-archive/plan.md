# Implementation Plan: #945 an agent lives one phase, the orchestrator's steps sit where it acts, two re-checks leave, and each release records how the process changed

## Summary

Four parts, built in four phases. The meter first: `session-cost --segments`
gains each segment's largest per-turn context, and phase 1 reads the 0.22.0
run with it, so the threshold the agent-lifetime rule uses is measured
before it is written. Then the two orchestration files are rewritten once
each: an agent lives one phase, a fix pass resumes only below the
threshold, `mergeable` is read before CI is waited on, a conflict is
integrated by a merge, decisions are folded into the one source the next
reader reads, and the orchestrator's re-run of each hand-back leaves. Then
the unverified record's two gate arms leave and its reader stays. Last, the
process archive's template and the framer's one line.

The policy documents change only through `spec.md` `## Rule changes`. No
phase edits `docs/`.

## Technical context

- **The fix-pass rule today** is `skills/code-review/orchestration.md`
  lines 17 to 30 (`read`): resume the session that built the branch, never a
  fresh spawn while it exists. Its acts-table row is
  `skills/implement/orchestration.md` line 627, delivered `still a sentence`.
  The tree says nothing about a phase boundary: `agents/smith.md`'s
  description says it builds one phase, and the 0.22.0 run resumed one smith
  across phases 1 to 4 and two fix passes (#945's comment of 2026-10-14,
  `read`).
- **The meter today**: `session_cost.py#load` keeps, per call-carrying
  message, `input_tokens + cache_read_input_tokens` as `turns[i][1]` (line
  1016, `read`), which leaves out `cache_creation_input_tokens` and every
  message with no tool call. `token_thirds` reads that for the run's
  `context` line. `measure_segments` (line 1730) builds one row per segment
  or per slice of a resumed file, and `report_segments` (line 2566) prints
  span, calls, tools per turn, mean gap and tokens. The new value is
  computed beside these, not by changing `turns`, so the run-level
  `context` line keeps its meaning.
- **The hand-back re-run** is `skills/code-review/orchestration.md` lines
  301 to 309 (`read`), cited by its heading's clause *and a phase is
  re-run* in `CONTRIBUTING.md` line 36, `skills/implement/SKILL.md` line
  498, `skills/implement/orchestration.md` lines 29 and 630, and pinned in
  `tests/test_the_rules_have_one_owner.py` lines 44 to 47 and 84 to 87 and
  `tests/test_broad_gate_rule.py` line 375 (`executed`, `git grep`).
- **The unverified arms**: `.github/workflows/hygiene.yml` line 157 onward,
  `templates/hygiene.yml` lines 15, 58 and 71 onward,
  `skills/verify/scripts/broad_gate.py` lines 29, 147, 175 to 180, 2230 and
  2993 to 2995 (`executed`, `grep -n`). `PARTITION` is held to the workflow
  by `tests/test_the_gate_names_every_step_ci_runs.py`. The module
  `unverified_check.py` stays: `chain_check.py`, `settle.py`,
  `fold_check.py`, `rule_changes.py`, `coordinates.py`, `gather_changelog.py`,
  `issue_claims_check.py` and `rules.py` load it (`executed`, `git grep`).
- **The chain check and a merge**: `chain_check.py#follows` lists the
  commits after a round's target with `--no-merges` and refuses a target
  HEAD does not descend from (`("off", ...)`), so a rebase is already
  refused and a merge commit is never read (`read`, lines 1476 to 1500).
- **The record layout**: `docs/the-record-layout.md` *seal/* and *Every kind
  of record, at a glance* list what the root holds; five unsettled specs
  change *seal/specs/<work-item-id>/*, and one changes *seal/* (`executed`,
  grep of their `## Rule changes`). The settle groups them by section, so
  this spec's items there join those groups.
- **Concurrent branches**: #1017 adds cases to other classes of
  `tests/test_session_cost.py`, and #1016 changes `hooks/root-migrate.py`,
  which no phase here touches.

**Failure scenario of the chosen approach, six months out.** The threshold
is one number read from one run. A model with a larger window, or a smith
whose fresh spawns grow past it, makes the rule spawn fresh where a resume
was cheaper: more calls, never a wrong tree. The number is in one sentence
with its source, so a later measurement rewrites it in place. The second:
with the unverified arms gone, a smith that deletes an open row instead of
closing it passes CI, and only the warden reading the overview's diff and
the sealer stand between that and the release. The measurement says that
has not happened in the step's recorded life; if it does, the arm comes
back with the case that shows it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| L-A. Keep: resume the implementer for every fix pass and leave phase boundaries to habit | One smith reached 941,799 tokens of context in one turn and 274 M tokens over 1,099 turns, against 165k to 461k for fresh spawns (#945's comment of 2026-10-14, `read`). Every turn re-reads all earlier work | rejected: the measured case is the failure |
| L-B. Replace: every phase and every fix pass is a fresh spawn | A fix pass on a small context re-establishes what the resumed session holds: 282 calls fresh against 30 resumed (the section's measurement before #940 rewrote it, as #945's comment of 2026-10-14 quotes it, `read`) | rejected: costs calls where the resume is cheap |
| L-C. A phase is a fresh spawn; a fix pass resumes below a context threshold | The threshold is one run's number (*Failure scenario* above) | **chosen**: the phase record already exists to be the handoff, and the fix pass keeps the cheap resume where it is cheap |
| T-A. Write 461,000 as the owner's comment states it | The figure was never measured by a tool in the tree; the column does not exist yet (`executed`, `grep -n -i "largest\|peak" session_cost.py` finds no such column) | rejected alone |
| T-B. Phase 1 builds the column and reads the 0.22.0 transcripts; phase 2 writes the threshold from that reading, 461,000 where the transcripts are gone | Two session transcripts from 2026-10-13 to 2026-10-15 remain on this machine (`executed`, `find -newermt`); whether #930's smith is among their segments is unknown | **chosen**: `questions.md` Q3 |
| C-A. Change `load`'s `turns` to carry the full input side, and read the largest from it | `token_thirds` and the run's `context` line change meaning with it, in a file #1017 is also editing | rejected |
| C-B. A new function beside `turns`, reading every assistant message once, with its own case class | One more pass over the slice's rows | **chosen** |
| H-A. Keep the orchestrator's re-run of each hand-back | One catch on record, #929's census defect (#945's body, `read`). Each module's test file now runs every census over its module (`tests/conftest.py#census_case`, 146 lines, `executed`), so the class it caught is closed where the smith's narrow run reaches it. Kept, it re-runs what the party that changed it already ran, at every phase boundary | rejected: the premise that kept it is gone |
| H-B. Narrow it to the census modules | The narrow run already holds them (H-A) | rejected |
| H-C. Delete it; the warden's rounds, the broad gate and the sealer's re-run of a sample of claims read the work after | A false green in one phase is found by round 1 instead of before the next phase is built | **chosen** |
| U-A. Keep the unverified CI step and gate arm | 0 failures of the step in 142 failed hygiene runs from 2026-09-23 to 2026-10-25 (`executed`); its issues are its own defects (#272, #612, #688) and #1034's fix two days ago. It also put an ordering duty on release day (`docs/release-checklist.md` *0. Before starting*) | rejected under `CLAUDE.md` *The rule a mechanism is kept against* |
| U-B. Delete the CI step in both workflows and the broad-gate arm; keep the module, the command, its `--baseline` mode and `settle`'s list of open rows | A row deleted rather than closed passes CI; the warden reads the overview's diff (`skills/code-review/SKILL.md` line 30, `read`) | **chosen** |
| U-C. U-B and also delete `--baseline` with its cases | `docs/the-record-layout.md` *The unverified record, and the baseline it is read against* names `check: one-merge-base`, which only `tests/test_unverified_check.py` carries (`executed`). Deleting the case before a settle removes the rule leaves `rules --check` refusing that line in every run; #1034's pending rule on the same section describes the mode too | rejected: the command costs nothing in CI, and a person can still run it |
| U-D. Narrow the step to run only when a pull request changes an `overview.md` | Same zero catches; saves seconds and keeps the release-day duty | rejected |
| R-A. The ticket's rule: a rebase after review closes is followed by a verifying round on the rebased tip | Policy forbids rebasing a work item's branch (`docs/release-checklist.md` *0. Before starting*, `read`), and the chain check already refuses a target off the history | rejected by default: `questions.md` Q2 |
| R-B. Integrate a conflict by merging the base, once, after the branch it conflicts with lands; a merge that resolved a conflict outside the records gets a verifying round | The chain check does not read merge commits, so the verifying round rests on the orchestrator reading this sentence | **chosen**: no target is orphaned, and the one unreviewed hunk gets a reader |
| I-A. Keep the issue body's two options, consolidate or an `Update <date>` block | The block is a correction written beside the text it corrects, which contract rule 19 refuses for every other text | rejected |
| I-B. Fold the decision into the body in place; the comment says why | GitHub keeps the edit history | **chosen** |
| P-A. The archive as `seal/process/<X.Y.Z>.md`, written once at release preparation | A release whose preparer skips the step has no file; the framer then reads the one before | **chosen**, as the ticket fixes it |
| P-B. Each work item writes a fragment of the archive, gathered at release | Each branch then edits a process record, and the base is already rewritten in place by the work item that changes it | rejected |
| P-C. A size check on the archive (a budget row or a release-report row) | Neither home exists (`spec.md` *Scope*, Out); a new check has no history to keep it | rejected: the template's one row per change bounds it |
| P-D. The archive's shape as a code block inside the checklist step, with no template file | The step reaches `docs/` only at the settle, so before it the shape would sit in this spec alone | rejected: `templates/process.md` exists from the merge |
| F-A. Only the first framer of a release reads the archive | Nothing in the tree tells a framer it is the first: `seal/specs/` holds work items of several releases until a settle (`executed`, `ls`) | rejected |
| F-B. Every framer reads the latest archive file once, where one exists | A read per frame, of a file bounded by one row per change | **chosen** |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The largest per-turn context: a function in `skills/verify/scripts/session_cost.py`, a column in `report_segments`, a key on each `measure_segments` row; its cases in a class of their own in `tests/test_session_cost.py` (S1 to S3), each seen red; `skills/verify/orchestration.md` *Measure the segment, and feed the flow log* step 1's list of a row's numbers rewritten in place; the reading of the 0.22.0 run's transcripts that remain (S4) in `phases/phase-1.md` | `bin/test tests/test_session_cost.py`; `session-cost --segments` on one resumed agent's own file, its output quoted in the phase record; this spec's `## Rule changes` read by `skills/settle/scripts/rule_changes.py#parse` with no refusal, which the framer did not run | |
| 2 | The two orchestration files, each written once: in `skills/code-review/orchestration.md`, the fix-pass section rewritten in place under a heading naming both rules, with the threshold phase 1 measured (or 461,000, Q3) and the command that reads it; *mergeable* and the merge route in the sealer section; the hand-back paragraph deleted and the heading's clause *and a phase is re-run* dropped. In `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the folding rule, the `handoff.md` rule and the prevention-home rule, and the acts table's rows rewritten. Every citation of the two old headings (`CONTRIBUTING.md`, `skills/implement/SKILL.md`, the acts table) and the pins of `## Removes` follow (S5 to S9) | `bin/test tests/test_every_orchestrator_act_names_its_delivery.py tests/test_the_rules_have_one_owner.py tests/test_broad_gate_rule.py`; `git grep -n "a phase is re-run" -- . ":!seal/specs" ":!changelog"` prints nothing; `git grep -n "fix pass resumes the implementer"` prints only the new heading's citations | |
| 3 | The unverified record's gate arms out: the step in `.github/workflows/hygiene.yml` and `templates/hygiene.yml` with their comments, the `unverified` arm of `skills/verify/scripts/broad_gate.py` and its `PARTITION` row, the cases naming them, `CONTRIBUTING.md` *Running the checks*'s count of shipped steps, and `skills/implement/SKILL.md`'s sentence that a deleted row fails the next pull request, rewritten in place. Every other site found by `git grep -n -i unverified` outside `seal/specs` and `changelog` is read and either corrected or named in the phase record with why it stands (S10 to S12) | `bin/test tests/test_broad_gate.py tests/test_arm_check.py tests/test_the_gate_names_every_step_ci_runs.py tests/test_seal.py tests/test_unverified_check.py tests/e2e/teammate/test_teammate_flow.py` | |
| 4 | `templates/process.md`; the one line in `agents/framer.md` step 4 (S13, S14); the work item's `changelog.md` | `bin/test tests/test_a_record_carries_no_comment.py tests/test_the_record_is_written_in_words.py tests/test_every_agent_reads_the_contract.py` | |

Phases 3 and 4 depend on nothing in phases 1 and 2. Phase 2 reads phase 1's
record for the threshold.

## Operational impact

- `templates/hygiene.yml` loses a step. A repository gets the new file at
  its next `seal pr-checks install`; one installed earlier keeps the step,
  pinned to the release that wrote it.
- The broad gate's summary prints one arm fewer. `broad-gate.md` names no
  arm, so no record changes shape.
- `session-cost --segments --json` rows gain one key. The change only adds,
  so a reader of the old keys is unaffected.
- No new dependency, environment variable or migration.
