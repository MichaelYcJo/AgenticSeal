# Implementation Plan: 1793521558-the-record-decides-each-proposed-verifier

## Technical context

The work builds nothing. Each phase reads the record for a group of candidates, decides each, drafts the tracker acts its decisions call for, and writes all of it into its own `trail/phases/phase-N.md` under `## What this phase found`, in the shape the design's *Data & interfaces* gives. The tree is read at `813665f0`, the tip `release/v0.27.2` was cut at.

What the phases read, by source:

- The tracker: the issues and comments the design's *Scope* item 1 names, and the `from-use` and `bug` labels (C1, C12), read with `gh` and dated.
- The records at the release tags `v0.22.4` to `v0.27.1`, read as `git show v<X.Y.Z>:<path>`: round records, `guarantee.md` *Claims re-run*, `gaps.md` `## Not verified`, and the standing work items under `seal/threads/` at `813665f0`. A work item settled before a tag is read at the tag that last held it.
- The pull requests' own commits, kept by GitHub under `refs/pull/<n>/head`, for C2's merges and orphaned targets. A fetch of those refs writes, so it runs in a `git clone --no-local` under the crafter's scratch directory named after this work item, never in the worktree.
- The compare records under `evals/` that `git log --all` holds (C8), read and never re-run.
- #956's audit (C3 to C6) and #1147's records (C9, C10): `79252e48:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` *Instances K12*, *Instances K13* and *D6*.

How the review chain reads the records. The proofer reads each phase's rows against the design's *Scope* item 2: the question answered, the decision word allowed, the grounds against G1. It runs each `Command C<n>` and compares what it prints (S2), opens the catches a row names, and reads each draft (S3). The sealer reads the records against #1038's *Done when* and the tree.

Failure scenario of the chosen approach, six months on: a dropped candidate's defect ships, and a reader asks whether the drop was wrong. The row names the commands and the commit or date they read, and the instances it judged, so the reader reruns the command, sees what was read, and reads the new defect against it; what a later run cannot repeat is the judgment of whether an issue's defect was one a candidate would have stopped, and the *Instances C<n>* lists keep each such judgment at its coordinate.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1** Each candidate's reading in its deciding phase record, one table with one header (chosen) | #1038's body is assembled from three records, so the orchestrator copies rows in order; *Scope* item 6's command does it and S7 checks the copy | chosen: G7, and #1147's audit took the same shape (`813665f0:seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md` row A2) |
| A1 alternative: a new `audit.md` at the work item's top | `docs/the-record-layout.md` *seal/threads/<work-item-id>/* lists no such file, so the settle's dry run names it as not read | rejected |
| **A2** Every change to the tree a decision calls for is drafted as an issue and not made here, a `limit` sentence and a narrowed rule sentence included (chosen) | A one-sentence change costs a work item of its own. The `limit` sentences are gathered into one draft (design *Scope* item 3) to bound that cost | chosen: the frame cannot state a rule change before the reading decides it, so a rule change made here would reach `## Rule changes` only by an orchestrator fold or a reframe; and milestone 76 says the patch "builds no feat" (G5) |
| A2 alternative: the crafter writes the `limit` sentences and C8's rewritten lead in this pull request | The diff mixes the decision with its build, the review reads both at once, and a sentence in the policy root (such as `docs/what-a-script-gates.md` *The checks*) needs a `## Rule changes` item no party can write in advance | rejected |
| **A3** Every tracker act is the orchestrator's, taken after the seal and before the pull request opens, from the drafts (chosen) | A draft the sealer read is filed as written; the issue numbers stand on GitHub only, in #1038's body and the pull request body's orchestrator part, since `chain_check.py`'s guarantee arm allows no record commit after the verdict but `trail/gate.md` and `guarantee.md` | chosen: G8, and #1147's audit's row A7 |
| A3 alternative: the crafter files and closes as it decides | contract rule 6 withholds posting from every agent | rejected |
| **A4** A drop of an existing issue closes through `Closes #N` in this pull request's body, with the reason comment posted when the pull request opens (chosen) | The close fires only when 0.27.2 reaches `main`, so for days the issue reads open with a reason comment on it | chosen: G9 and G10; the owner sees each drop in the pull request before anything closes, and #27 and #6 must be carried by a keyword or leave the milestone, or the release fails |
| A4 alternative: `gh issue close --comment` at the pull request's opening | The decision closes issues before the owner has read the pull request that holds it, and a rejected pull request leaves them closed | rejected |
| **A5** C1 read in the same phase as C8 (chosen) | A defect of a user's repository that only a click-through reaches is not in this tree's record, so C1's row can say only what this repository's record shows; it names that open part | chosen: in this repository the application is a Claude Code session running the plugin, and the behaviour suite already drives one, so C1's verifier and C8's smoke run are two answers to one question |
| A5 alternative: C1 read only as a verifier for users' repositories | No record of one is in the tree, so the row drops C1 for an absence of evidence it never read | rejected |
| **A6** R37's 131 unsorted asserts sorted only where C4 is built (chosen) | A reader expecting R37's count from #1038 finds the range 123 to 264 #956 left, with the reason | chosen: the decision stands on catches, and a count inside the range changes no drop; a build needs the count to scope its issue, so the build's draft carries the sort |
| A6 alternative: sort every assert now | Reading 131 asserts one by one costs a phase's context for a figure no drop uses | rejected |
| **A7** C12 decided on the record of fix commits and issues, with #951's measure at `475653e7`, and no type checker run (chosen) | A latent defect a type check would find today and the record never showed stays unknown; the row names it as the open part | chosen: contract rule 2 names the typecheck among the acts no agent runs, and the question #1038 asks is what the record shows |
| A7 alternative: run a type checker in a scratch clone | It is the act contract rule 2 withholds | rejected |
| **A8** The existing mechanism each candidate sits beside is weighed for removal as an equal of keeping (chosen) | A mechanism kept for having existed survives another release with no recorded catch | chosen: G1. Each row that keeps one names the premise it checked: the never-rebase rule for C2, the sealer's sample for C7, the behaviour suite for C8, the citation case for C6 and C10, `tests/censuses.py#entry_point` for C9, the review axes floor for C14 |
| **A9** Three phases grouped by the evidence they read (chosen) | A phase's reading of a candidate finds an overlap with one another phase decides; the later phase reads the earlier record and cites its row | chosen |
| A9 alternative: one phase for all fourteen | One spawn reads the tracker, the tags, the pull requests' commits and the compare records, and the context runs short before the last rows | rejected |
| A9 alternative: one phase per candidate | Fourteen spawns, each paying the reading of the frame and the contract | rejected |
| **A10** No changelog fragment (chosen) | The 0.27.2 notes say nothing of the decisions, and a reader learns them from #1038 | chosen: the tree outside the records does not change, and #1147's audit made the same choice (its row A6) |
| **A11** The builds go to one new minor milestone, by `frame/questions.md` Q1's default | The owner may want them beside #1020 in `release: 0.29.0` | chosen as the default; Q1 holds it |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 to 3 for C1, C7 and C8; *Scope* item 5, with `gaps.md` from its template | each `Command C<n>` of the record run as written; S4's `git diff --name-only 813665f0..HEAD`; `tests/behaviour/test_unverified_rows_close.py`, `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` | |
| 2 | *Scope* items 1 to 3 for C2, C11, C13 and C14 | the same, for its rows | |
| 3 | *Scope* items 1 to 3 for C3, C4, C5, C6, C9, C10 and C12; *Scope* items 4 and 6 | the same, for its rows; S7; `tests/text/test_a_rider_reaches_its_file.py` where `seal/follow-up.md` changed | |

## Operational impact

None for a deployer: the tree changes only under this work item's directory, and in `seal/follow-up.md` where *Scope* item 4 moves a row.

The tracker acts are the orchestrator's, after the seal and before the pull request opens, in this order, each from the draft the phase records hold:

1. Where any candidate other than C11 is `build`, create the minor milestone Q1 names, with a purpose line naming #1038's kept verifiers.
2. File each `file D<n>` draft as a new issue in that milestone.
3. For each kept candidate that has an issue, post its evidence comment and move the issue into that milestone; #27 and #6 leave `release: 0.27.2` (G9), and #1020 stays in `release: 0.29.0`, the milestone made for it.
4. For each dropped candidate that has an issue, post its reason comment and move the issue into `release: 0.27.2` where it stands elsewhere, so the release check's `D \ M` reports nothing.
5. Edit #956's audit comment to add C6's row (#1129 *Done when*).
6. Rewrite #1038's body with *Scope* item 6's command, replacing each draft id with the number filed.
7. Open the pull request with `Closes #1038` and one `Closes #N` line for each dropped issue (G10).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-01 | G6's first decision is the owner's answer, not a carried claim: no paid eval run is taken in 0.27.2 | The orchestrator put the question through `AskUserQuestion` before the first edit, and the owner chose "돌리지 않음" (no run); a row only such a run answers is a `## Not verified` row with its answerer named | `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* |
| 2026-11-01 | The frame was read against #1038 and its milestone and spawned as committed, with no proposal to the framer; Q1 is built on its default (a) | The candidates, the build-or-drop table per phase and the tracker acts held by the orchestrator meet the issue's *Done when*; the milestone's later sentence "the kept ones are filed into one minor together" outranks the body's "in this milestone", and Q1's default follows it | `skills/implement/orchestration.md` *The frame is read against the issue at the spawn* |
