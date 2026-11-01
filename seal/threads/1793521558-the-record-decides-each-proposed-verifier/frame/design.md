# Design: 1793521558-the-record-decides-each-proposed-verifier

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A mechanism stays only while its record of what it caught outweighs what it costs; existing is no reason to keep it", and "A reading that is noisy or guessed from words is reported, never used to block" | The test every candidate is read against. A proposed mechanism with no catch of its own in the record is dropped. An existing mechanism a candidate sits beside or would change is weighed for removal as an equal of keeping it, and a verdict for keeping names the premise it checked. A kept check must read its fact exactly, as the same section's "A script holds a gate only on a fact it reads exactly" says |
| G2 `skills/core/SKILL.md` *The first value: efficient development through the workflow* | A candidate that adds a judging pass, a person's step or a run (C8, C13, C14) is weighed on what it costs the run as well as on what it catches |
| G3 issue #1038, body *What the record must answer, per candidate* and *Done when* (read: `gh issue view 1038 --json body,comments`, 2026-11-01) | The questions the reading answers for C1, C2, C3 to C6 and C7, and the three outcomes: build with its own issue, drop with its reason, and no follow-up issue for a drop. The body's "Each build has its own issue ... in this milestone" is superseded by G5's later sentence "the kept ones are filed into one minor together"; this frame takes G5's |
| G4 issue #1038's three comments, folded here (read, the same command): 2026-10-29 re-homes rows R40 and R37 of #956's audit; 2026-10-30 asks whether the behaviour suite stays, narrows to a gross-breakage smoke run, or goes as the proof of a preload rewrite; 2026-11-01 adds K12 and K13 from #1147's audit and says the home of the `seal/follow-up.md` row on `console.to_utf8()` becomes this issue's decision | C4, C5, C8, C9 and C10, and *Scope* item 4 |
| G5 milestone `release: 0.27.2`'s description (read: `gh api repos/:owner/:repo/milestones/76 --jq .description`, 2026-11-01) | Adds #1020's, #951's, #27's and #6's proposals (C11, C12, C13, C14); "#951 and #1048 close where #1038 drops them"; "A patch: it decides and documents, and builds no feat" |
| G6 the owner's two decisions of 2026-11-01: no paid eval run (`claude plugin eval`, `evals/scripts/noninferiority.py run`) anywhere in 0.27.2, and nobody asked anything after the routing answer | The second is `routing.md`'s `Automation` `yes` (read, committed at `bf67191b`). The first stands in no file of the tree: unverified, carried from the spawn prompt, and the orchestrator answers it. A candidate whose answer only a paid run gives is decided on the record without that run, and the run's question is a `## Not verified` row of `gaps.md` with its answerer named (*Scope* item 5) |
| G7 `docs/the-record-layout.md` *A fact of a work item has one record, and every other record cites it by path and heading* | Each candidate's reading has one home, its row in the phase record that decides it. Each draft, each `gaps.md` row and #1038's body cite that row; none restates its figures |
| G8 `skills/agent-contract/SKILL.md` rule 6, "post nothing, push nothing, open no pull request, and spawn no agent", and rule 12 | The crafter files no issue, closes none and edits no issue or comment; every tracker act is the orchestrator's (plan *Operational impact*). Each list a reading builds names its method, and a list built from a search is called a sample, with its open part named |
| G9 `docs/issues-and-milestones.md` *One thing reads a milestone, and it can stop a release*, and `.github/scripts/release_completeness_check.py#judge` (read) | An open issue of `release: 0.27.2` that no pull request of the release carries by a closing keyword fails the release (`M \ D`). #27 and #6 are open in that milestone (executed: `gh issue list --milestone 'release: 0.27.2' --state all`, 2026-11-01). A dropped issue closes through this pull request's keyword; a kept one leaves the milestone before the release. A carried issue outside the milestone is `D \ M`, reported and not failed |
| G10 `docs/branch-and-release.md` *A closing keyword does nothing when the base is `release/vX.Y.Z`.*, and `docs/issues-and-milestones.md` *A keyword claims the one number after it* | A drop closes by `Closes #N` in this pull request's body, one keyword in front of each number, and the release workflow closes it when 0.27.2 reaches `main` |
| G11 `docs/issues-and-milestones.md` *An issue is its body and its comments together*: "A decision is folded into the body in place" | #1038's *Done when* asks that its body record each decision. The orchestrator rewrites the body from the phase records (*Scope* item 6), folding the three comments G4 names |
| G12 `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*, the bullet on `seal/follow-up.md`: "this work may be that prerequisite. If so, include the item in this change and delete its row" | Two rows of `seal/follow-up.md` *Schedulable items with nowhere else to go* are instances of a candidate: the row opening "`console.to_utf8()` is owed by an entry point" (C9, by G4's third comment) and the row opening "Three cases assert what a script may invoke by searching its folded source" (C4: two negative pins that read a script as text, the class R37 names). *Scope* item 4 decides each row's home |
| G13 `skills/settle/SKILL.md` *Rule changes*, and #1147's audit as precedent (read: `813665f0:seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md` *Rule changes*, `- nothing`) | This work changes no rule. A decision that changes a rule is filed as an issue whose own design states the rule change (plan row A2) |
| G14 `docs/release-checklist.md` *0. Before starting*, "Never rebase a work item's branch, for any reason", and `skills/code-review/orchestration.md` *A conflict with the base is integrated by merging the base into the branch, never by a rebase.* (read) | C2's baseline: the merge route #945 shipped in 0.22.4 (executed: `gh issue view 945`, closed in `release: 0.22.4`) and the verifying round it owes where a merge resolved a file outside the records |
| G15 `agents/sealer.md` step 3, *A claim against the fact.* (read) | C7's baseline: the sealer re-runs a sample of the crafter's `executed` and `seen red` claims and leaves the rest on the phase record. #1148, after which C7 is read, closed in `release: 0.25.1` (executed: `gh issue view 1148`) |
| G16 `evals/README.md` *The behaviour suite — `behaviour/<agent>/`*, its lead "A rewrite of an agent's preload is proved not worse by running this suite on the old tree and on the new one", and its sentence "Nothing in the tree makes a later edit owe a run" (read) | C8's object. The file is outside the policy root: `seal/config.md` holds no `Policy root` row, so the root is `docs/` (read) |
| G17 #956's audit, the comment on #956 that opens "This is the audit #956 asks for" (executed: `gh issue view 956 --json comments --jq '.comments[-2].body' \| grep -n '#1038'`, three rows) | The rows whose *Fix* cell names #1038 are R10, R37 and R40, which with R36 (#1129, folded into #1038, read: `gh issue view 1129`) are candidate 3's whole list, built from the audit's *Fix* column. R10 still stands at `813665f0`: `hooks/lib/routing.py#parse` reads an `Automation` value outside `AUTOMATION_ANSWERS` as `None`, and `hooks/question-gate.py` refuses a question only where the value is `AUTOMATION_YES` (read) |
| G18 #1043's case landed as `tests/behaviour/test_a_cited_section_stands_in_its_file.py` (executed: `git log --oneline --grep='#1043'`, `946c9317`, #1131) | C6 audits that module the way #956's rows are audited (#1129 *Done when*) |
| G19 `docs/issues-and-milestones.md` *A milestone answers when, and takes three shapes*: "Three or four is a ceiling, not a target" | The minor the builds go to is a release planning choice; `frame/questions.md` Q1 holds it with the default the run proceeds on |

## Scope

1. **Each candidate is read and decided in one row of *The decisions*, in the phase record that reads it.** The candidates, numbered once here:

   | Id | Candidate | Its source | Its issue |
   |---|---|---|---|
   | C1 | a project-specific verifier that drives the real application | #1038 body, candidate 1 | none |
   | C2 | a verdict kept across a rebase where `git patch-id` shows the same patch | #1038 body, candidate 2 | none |
   | C3 | R10: an `Automation` value near `yes` leaves the run attended | G17 | none |
   | C4 | R37: negative pins that read a tracked file as text pass every spelling but the literal | G4, G17 | none |
   | C5 | R40: a `not_contains` eval grader passes every other spelling | G4, G17 | none |
   | C6 | R36: #1043's tree-wide citation case, audited | G17, G18 | #1129, closed into #1038 |
   | C7 | the sealer reads every `executed` and `seen red` claim against the implementing agent's transcript | #1038 body, candidate 4 | #1048 |
   | C8 | the behaviour suite as the proof of a preload rewrite: keep, narrow to a gross-breakage smoke run, or remove | G4, the 2026-10-30 comment | none |
   | C9 | K12: every entry point gives the answer `hooks/lib/console.py#STREAMS` gives, read by a census wider than `hooks/` | G4, the 2026-11-01 comment | none |
   | C10 | K13: a `path#name` in shipped text names a name its file defines | G4, the 2026-11-01 comment | none |
   | C11 | a check that reads recurrence across review rounds, or the mediated exchange at a finding's first `reopens:` | G5 | #1020 |
   | C12 | a static type check in CI | G5 | #951 |
   | C13 | a check of a session's procedure rather than its commits | G5 | #27 |
   | C14 | a separate perspective pass in the review | G5 | #6 |

2. **Each candidate's question and what decides it.** The decision words are `build` and `drop` for a proposed mechanism; for C3 to C6 also `limit`, a fix kept as a limit sentence where the shape cannot arise in the one-issue automation flow (#1038 body, candidate 3); for C8 `keep`, `narrow` or `remove`. A catch is a defect the record shows reaching a merge, a release or a later work item, which the candidate would have stopped and the verification the tree has did not; a planted probe shows a candidate can catch, and is not a catch.

   | Id | The question the record answers | Decided by |
   |---|---|---|
   | C1 | Which issues labelled `from-use` or `bug` (all states) describe a defect that shipped past a green suite because no command or test reached the behaviour, with the behaviour and the release; which closed `## Not verified` rows at the release tags were answered by a person running the application, and at what cost. In this repository the application is a Claude Code session running the plugin, and the existing driver of one is the behaviour suite, so C1 is read in the same phase as C8 (plan row A5). A user's repository's record is not in this tree, and the row names that open part | drop where no such defect and no recurring row stands |
   | C2 | Since 0.22.4, how many work items integrated the base after a review round, how many verifying rounds that added, and whether any round's `target:` was orphaned | drop where the merge route cost nothing measurable; the never-rebase rule stays either way (#1038 body) |
   | C3 | Whether any committed `routing.md`, on any ref, writes `Automation` outside the two values, and whether a question was asked on such a branch | #1038 body, candidate 3: drop, `limit`, or build |
   | C4 | Which defect the record shows passing a negative pin that reads a tracked file as text, the two cases of G12's folded-source row among the pins read. The 131 asserts R37 left unsorted are sorted only where C4 is built, because the count scopes the filed issue and changes no drop (plan row A6) | as C3 |
   | C5 | Which compare record under `evals/` shows a leftover that a `not_contains` grader passed. How `claude plugin eval` reads such a grader whose target file is absent is a paid run's answer (G6) and is *Scope* item 5's row | as C3 |
   | C6 | What the case reads and decides, what it does with a citation it cannot read, and whether that lets a dangling citation through, each with an executed probe in a scratch clone; the row for #956's audit in that audit's columns, with the commit it was read at (#1129 *Done when*) | as C3 |
   | C7 | Which `executed` or `seen red` claims outside a sealer's sample turned out false, found by a later round, a later work item or use; the samples' sizes from each `guarantee.md` *Claims re-run* at the release tags; the labels as `skills/verify/SKILL.md` states them at `813665f0` | drop where the record holds none; #1048 closes |
   | C8 | Of the compare records `git log --all` holds under `evals/`, which failed, which fail was acted on as a defect, which run caught a defect later confirmed, and what each side cost as its record states. No side is run (G6) | `keep`, `narrow` or `remove`, under G1 and G2 |
   | C9 | The catches the record shows for a drifted entry-point answer (G12's row; `79252e48:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md` *Instances K12*), against the census's cost | build or drop |
   | C10 | The catches the record shows for a dangling `path#name` (*Instances K13* of the same record), read with C6's audit | build or drop |
   | C11 | Since #1148 shipped in 0.25.1, the recurring findings per work item (a `regression:` or `reopens:` naming an earlier finding), split into those standing in a work item's records alone and those reaching shipped text, as #1020's comment of 2026-10-29 split 0.24.0's | #1020's comment of 2026-10-30: where recurrences in shipped text remain, the case for the exchange or the check; where they fell to near zero, drop; #1020 closes on a drop |
   | C12 | Which fix commits or `bug` issues name a defect a static type check reads (a changed return value or signature, a `None` used as a value) that shipped past the suite; the cost as #951's comment of 2026-10-29 measured it at `475653e7`. No type checker runs (plan row A7) | build or drop; #951 closes on a drop |
   | C13 | For each of #27's seven rows, who catches it at `813665f0`: a gate, by path; the agent that reads the rule, by rule; or nobody | drop where every row has a catcher or is a reading no gate can make; #27 closes on a drop |
   | C14 | Since the review axes became a floor (`skills/code-review/SKILL.md` *Comparison axes*), which findings a later round, the sealer or use raised of a kind no axis of that release names, on lines an earlier round of the same work item read: the axes leaking, in #6's words | #6's own test: where axes keep leaking, build; otherwise drop, and #6 closes |

3. **A draft for each tracker act a decision calls for**, in the phase record that decides it: an issue body for each `build` or `limit` with no issue yet, the `limit` sentences of C3 to C6 gathered into one draft; an evidence comment for each kept candidate that has an issue; a reason comment for each dropped candidate that has an issue; C6's row for #956's audit. A dropped candidate with no issue gets no draft, and its row in #1038's body is its record (#1038 *Done when*: "or never filed").
4. **The two `seal/follow-up.md` rows G12 names leave that file only where a filed draft takes their question**: the `console.to_utf8()` row with a C9 build, the folded-source row with a C4 build. The draft carries the row's question in full. On a drop the row stays, and the decision row cites it.
5. **`gaps.md`**, from `templates/records/sdd-gaps.md` when the first phase closes, holds in `## Not verified` the question of C5 that only a paid run answers, answered by the repository owner through one eval run over a case whose agent writes no such file, in a release where paid runs are taken; and any other question of a candidate that only such a run answers, each with its answerer.
6. **#1038's body**: the last phase's record holds a preamble and one command that prints it with the header of *The decisions* and every candidate's row in candidate order, copied from the phase records. The orchestrator runs it and replaces each draft id with the number it filed.

Out of scope, each with its reason:

- Building any verifier or fix, a `limit` sentence included: #1038 *Out of scope*, and the issues this work files build them (plan row A2).
- Repairing an instance a reading finds, such as K12's three drifted answers: a repair is drafted or named in its row, never made here (plan row A2).
- Any paid eval run (G6), and any type checker run over the tree (plan row A7).
- Every tracker act by the crafter (G8).
- #947's measurement, which milestone 76 orders after this item.
- A changelog fragment: nothing a user of the plugin meets changes (plan row A10).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 every candidate decided once | Given the phase records at HEAD, when C1 to C14 are looked for, then each has one row of *The decisions* in one record, and its *Decision* cell holds one word of *Scope* item 2's for that candidate | `grep -n '^| C[0-9]' seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-*.md` |
| S2 a reading repeats | Given a row's command, when the proofer runs it at the commit or on the date the row names, then it prints what the row states | each `Command C<n>` run as written |
| S3 each act has a draft | Given *Scope* item 3, when a row's *Act* cell names a draft or a comment, then that draft stands under the record's `### Drafts`, and no `build`, `limit`, kept issue or dropped issue lacks one | read each row against `### Drafts` |
| S4 the tree is untouched | Given HEAD, when `git diff --name-only 813665f0..HEAD` runs, then it lists only this work item's directory and, where *Scope* item 4 moved a row, `seal/follow-up.md` | the command |
| S5 the paid run's question is named | Given `gaps.md`, when its `## Not verified` table is read, then C5's harness question stands with the repository owner as its answerer | `tests/behaviour/test_unverified_rows_close.py`, and read |
| S6 a sample says so | Given a row whose list came from a search, when its *Command or coordinate* cell is read, then it calls the list a sample and names the open part | read, by contract rule 12 |
| S7 the body is the rows | Given *Scope* item 6's command, when it runs, then every row it prints equals its phase record's row byte for byte | `diff` of the printed rows against `grep '^| C[0-9]'` over the phase records |

## Data & interfaces

**The decisions** is one table with the same header in every phase record, under `### The decisions` in `## What this phase found`:

| Column | Holds |
|---|---|
| Candidate | `C<n>` and its name from *Scope* item 1 |
| Command or coordinate | the heading `Command C<n>` of the same record, where the command stands whole and names the commit `813665f0` or the tracker read with its date, labelled `executed`; or a record read at a tag as `git show v<X.Y.Z>:<path>`, labelled `read`; and `sample` where the list came from a search |
| What the record shows | each catch at its coordinate, and the cost the record states with its source; the heading `Instances C<n>` holds the instances read one by one |
| Decision | one word of *Scope* item 2's |
| Grounds | the G-row of this design, or the clause it was judged against, quoted |
| Act | `file D<n>`, `comment D<n> on #N`, `close #N with D<n>`, `row for #956 D<n>`, or `none` |

A draft stands under `### Drafts` as `#### D<n>`, numbered across the work item, each naming the candidate it answers and its proposed home. A draft cites the row it stands on as the record's path at the sealed commit, and restates no figure the row holds.

## Rule changes

- nothing
  why: This work reads the record and decides, and changes no rule. Each decision that changes a rule is filed as its own issue, and that issue's design states the rule change.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the row opening "`console.to_utf8()` is owed by an entry point", only where C9 is built | `seal/follow-up.md` *Schedulable items with nowhere else to go* | the issue C9's draft files, which carries the row's question; on a drop the row stays (*Scope* item 4) |
| the row opening "Three cases assert what a script may invoke by searching its folded source", only where C4 is built | `seal/follow-up.md` *Schedulable items with nowhere else to go* | the issue C4's draft files, which carries the row's question; on a drop the row stays (*Scope* item 4) |

This design adds no mechanism: no gate, check, hook, CI step, rule, line grammar, label or mark. A mechanism a candidate would add is weighed in its own issue, against what it removes.

Framed 2026-11-01 by framer, before the build.
