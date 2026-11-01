# Implementation Plan: 1793528484-the-process-measured-on-0-27-2

## Technical context

The work writes records and no code. What each measure reads, and where it stands:

- Preload: `agents/*.md` and their `skills:` lists. At the after tree every definition lists `core` and `agent-contract` (executed: the frontmatter of each of the five files). At `a8d83663` the definitions are `framer.md`, `scribe.md`, `sealer.md`, `smith.md` and `warden.md` (executed: `git show a8d83663:agents/`).
- The suite: `.test_durations` at the after tree prices 6,181 cases at 995 seconds in all (executed: a `json.load` of the file at `94b03636`). `.github/workflows/test.yml` runs the whole suite on every pull request, ubuntu whole, macOS in three shards and Windows in four, and the Windows shards write the durations (read: its matrix and its `pytest` line). PR #1253's `tests` run `41296448338` lists those jobs with their start and end times (executed: `gh api .../runs/41296448338/jobs --paginate`).
- The runs: G10 of `frame/design.md` gives both samples. A subagent's transcript is `subagents/agent-<id>.jsonl` beside a `.meta.json` holding its `agentType` and spawn description (executed). `skills/verify/scripts/payload_meter.py#first_prefix` is the tree's reader of a first prefix (read).
- The rounds: `.github/scripts/finding_counts.py` (read). At `v0.21.0` 14 work items, and at `v0.21.1` 8, hold files matching `seal/specs/<id>/rounds/round-<n>.md` (executed: `git ls-tree -r --name-only`). A tag holds every work item not yet settled, so the round measure takes its list from `v0.20.0..v0.21.1`, as `frame/design.md` *Scope* item 1 says.
- The withholds: #1038's `trail/phases/phase-1.md` *Command C7* (b) at `3937d861`, which reads `refs/pull/*/head` in a scratch clone (read).

The failure scenario of the chosen approach, six months on: a reader takes a `better` row as the process's own effect, when the after sample is five small work items and the before sample one session's runs. A harness release moved the first prefix as well. The reading names each sample's size and the Claude Code version on each side, and the rows cite their phase record rows, so the claim can be opened and narrowed. A second failure: #51's body section reads as standing while the process moves again. The section names the commit and the date it was taken at, and #51's own rule replaces it at the next reading.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Re-run every before at its source with the command the after side uses, and report whether it reproduced | A before that does not reproduce leaves two figures for one measure. The row then shows both, and the comparison rests on the re-run, which is the one whose method is written down | Chosen. The body asks for the after "measured the same way", and for one row, prose opened on demand, no record states the way (`frame/design.md` G11) |
| A2 Take the body's *Before* figures as given and measure only the after | Two of the seven rows have a method nobody can open, so a `better` there could be a change of method. A reviewer cannot tell | Rejected |
| A3 Replace the structure: add the missing readings to the tree's instruments, such as a `--prose` reading in `session_cost.py` or a 0.21.x pairing in `release_report.py`, and measure with them | The milestone builds no feat (G2). An instrument kept for a one-off reading has no catch to keep it by `skills/core/SKILL.md` *The rule a mechanism is kept against*, and it adds cases to a suite this reading measures. `release_report.py` pairs agents by name, so the rename leaves every 0.21.x agent row unpaired, and it gives documents per file where the body gives totals | Rejected. The probes live in the scratch directory, and each record carries its probe's text whole, so the reading can be re-run without a tool in the tree |
| A4 Keep the structure as it stands: `release_report.py`, `payload_meter.py`, `finding_counts.py` and `session_cost.py` used where each reads the measure as the body defines it | Each reads one of the measures exactly. The premise that keeps them is that they read the body's definitions. It was checked: `finding_counts.py` reads the rounds through the pull-request check's own reader (G13), and `payload_meter.py#first_prefix` reads the first `usage` block G11 names (read) | Chosen for rounds and first prefix. The tree measures are `git show` and `git ls-tree` readings, which give any commit's tree without a checkout |
| A5 The reading's home is #51, a body section with a comment as its evidence | #51's body is long (16,889 characters, executed) and a section can be missed. The section opens with its date and commit | Chosen (G4) |
| A6 The reading goes to a new file under `seal/` or `docs/` | #1144 removed `seal/process/` for keeping readings beside the tree (G5). A reading is no ratified norm, so `docs/` is the wrong root by `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | Rejected |
| A7 The reading goes to the release note's `### Process changes` table | That table records changes to the way of working, written by a work item whose diff changes one of the files `docs/the-record-layout.md` lists; this one changes none (G5) | Rejected. The changelog fragment says what was measured |
| A8 The reading goes to the rolling log #1246 | The next release discards it (G4) | Rejected |
| A9 Read the round cap across every 0.22.x work item, as the body asks | The cap it judged was replaced at `a92c358b` (G6). The reading would judge a mechanism that no run uses | Rejected |
| A10 Change *The run* now to a hard cap of three | The owner reviewed the settle that made three a default at which the orchestrator weighs (G6), after the decision of 2026-10-16. A patch that rewrites it on this reading overrides the later decision, and #1038's C11 already sends recurrence to #1020's check (G7) | Rejected. A loop item 9 finds is an issue draft |
| A11 Count withheld verdicts from the final `guarantee.md` files | Before 0.27.0 the next sealer run replaced a withheld block, so the final file shows only the last verdict (#1038 `trail/phases/phase-1.md` *Whether the frame holds*, read) | Rejected. The pull requests' heads are read, by C7 (b)'s method |
| A12 Measure the runs from readings posted to the flow log | #1246 holds none (G9) | Rejected. The transcripts on this machine hold both samples (G10) |
| A13 Replace the structure: close #947 as stale, with its grounds, and measure nothing | The owner's question since 0.22.0 stays unanswered, #1044's last *Done when* bullet stays unmet, and the milestone names the measurement as half its purpose (G2). Only the asks *Out* lists are stale, and every measure of the *Before* table still has a source | Rejected |
| A14 One phase for every measure | One record would hold three kinds of source, and a stall reading transcripts would hold back the tree figures. It would also pass the size one read takes | Rejected. Three phases, one per kind of source, and the third writes the reading over all three |
| A15 The crafter posts the comments and files the issues | Contract rule 6 withholds posting from every agent (G14) | Rejected. The orchestrator takes each act from phase 3's drafts |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3, 4 and 5 | The `git diff --stat` of *Scope* item 1 and of scenario S8, each printing nothing. Scenarios S1 and S2 for every row. Then, in one command, `bin/test tests/test_censuses.py -q` with every other module `git grep -l 'seal/threads' -- tests` lists that reads a work item's records, per contract rule 2 | 1b493ce2 |
| 2 | `frame/design.md` *Scope* items 6 and 7, over the segments *Scope* item 1 lists | Each segment named by session prefix and agent file, with its kind and plugin version. Scenarios S1, S2 and S9. The same one command as phase 1 | 361c4532 |
| 3 | `frame/design.md` *Scope* items 8, 9, 10, 11 and 12 | Scenarios S1 to S9, S3 to S7 read against phases 1 and 2's records. The same one command as phase 1 | |

## Operational impact

None to deploy. No dependency, variable or file outside the work item's directory changes.

The orchestrator's acts, after the seal and before or with the pull request:

1. Edit #51's body with D1, and post D2 on #51.
2. Post D3 on #1044.
3. File each issue draft of phase 3 in the milestone `frame/questions.md` Q1 gives, and name each issue in the pull request body.
4. Close #947 through this pull request's body, one closing keyword before its number. The keyword closes nothing on a `release/v0.27.2` base and closes #947 when the release reaches `main` (`docs/branch-and-release.md` *A closing keyword does nothing when the base is `release/vX.Y.Z`.*).

Each phase spawn hands the crafter the scratch directory and says not to write that path, or any transcript's path, into a record (G15). Where `seal pr-body` refuses an issue number written after a closing keyword in a record, as it did on #1038's branch at `3937d861`, the number is written as a code span.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-01 | G3's no-paid-eval decision is the owner's answer, not a carried claim | The orchestrator put the question through `AskUserQuestion` before the first edit of 0.27.2, and the owner chose "돌리지 않음" (no run) | `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* |
| 2026-11-01 | #947 started before #1038's merge, and the frame was spawned as committed with Q1 built on its default (a) | Every work item of 0.27.2 that changes a process file had merged at `94b03636`; #1038's diff is its own records and one `seal/follow-up.md` row, which the framer confirmed, so the tree measured is the release's final one; the frame meets the issue's asks that still read a thing the tree holds and names the stale ones with grounds | `skills/implement/orchestration.md` *The frame is read against the issue at the spawn* |
