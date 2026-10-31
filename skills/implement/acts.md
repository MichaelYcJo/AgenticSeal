# implement, the orchestrator's acts

This file tables every act addressed to the orchestrator against what
delivers it. A maintainer reads it when an act is added, moved or renamed,
and `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`
reads it at every run of the suite; an orchestrating session acts on the
files it tables and does not open this one. It tables the headings of
`skills/implement/orchestration.md`, `skills/implement/bootstrap.md`,
`skills/implement/multi-repository.md`, `skills/code-review/orchestration.md`
and this file.

## Orchestrator: which of these acts runs itself

Every act addressed to the orchestrator sits under a heading carrying the
`Orchestrator:` prefix, in one of the files this file's opening names, and
this is the list of them.
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` holds it against
those files from both sides: an act with no row fails, and a row naming an act
no file carries fails.

**The row set is mechanical.** Every `##` heading whose text begins
`Orchestrator:` in any of them, plus every `###` heading directly beneath
one. This section is one of those headings, so it has a row of its own.

**`Delivered by` answers one question: when the orchestrator forgets this
act, what notices?** Four values and nothing else.

| Value | What it says |
|---|---|
| `command: <path>` | the act is one command somebody types, so there is nothing to reconstruct from prose. The path has to exist |
| `check: <path>` | something refuses, or says so, when the act did not happen. The path has to exist |
| `part of its parent's act` | a `###` describing its parent's act rather than naming one of its own. A `##` cannot take it |
| `still a sentence` | nothing notices. The `Grounds` cell says what was looked at and came back empty, and an empty cell there fails |

**A command does not make anybody run it, and a row naming one says so where
that is the case.** The grounds of a row whose delivery reaches only part of
its act name the part it does not reach. A row that reads closed over a tree
that is not is worse than no row at all, because the next work item picks
its subject from this table.

**What this does not catch**: an act written for the orchestrator under a
heading carrying no marker has no row and nothing notices. The check reads
the marker, not the meaning, which is the limit
`tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py` states
for itself. The two read the headings through one parser, so they cannot
come to different answers about what a heading is.

**One act is outside this table, because the table cannot hold it.** Posting
a segment's reading to the flow log is the orchestrator's (contract rule 6
withholds posting from every agent), and it lives in
`skills/verify/orchestration.md` *Measure the segment, and feed the flow
log*, under a heading carrying no
marker, in a file the row rule above does not read. Its delivery is
`seal cost … --post`, which resolves the label, applies the invariant and
posts the reading with what a person says about it. **Nothing makes it
run**: the measurement can go untaken while the posting never fails. So this
paragraph is the row that act would have, and it is not a closed-looking
one.

| Act | File | Delivered by | Grounds |
|---|---|---|---|
| Orchestrator: the order inside a ticket | `skills/implement/orchestration.md` | still a sentence | Nothing reads the order. Each step it sequences has a row of its own, and what the sequence itself asserts, which party runs when, is in no file a check opens. A run that opened the pull request after the rounds leaves the same tree as one that opened it before them, and so does a session that never ran `seal core` before its first edit. Nothing reads the three rules under the steps either: a decision left in an issue comment, a framer spawned with no line on the issue's comments, a `handoff.md` kept after its move and a recurring problem given no home leave a tree no check refuses |
| The frame is read against the issue at the spawn | `skills/implement/orchestration.md` | still a sentence | Nothing reads whether the exchange happened: a frame built with it and one built without it leave the same tree, and the framer's fold is one commit among the frame's. The counts reach the flow log only through `seal cost --post`, which nothing makes run. Nothing reads the spawn prompt's shape either: a prompt that hands a fact with no coordinate spawns the crafter as one that labels every fact does |
| Orchestrator: Bootstrap | `skills/implement/bootstrap.md` | check: `hooks/mode-gate.py` | A root with no `Mode` row in `config.md` is exactly nobody was asked, and this gate stops the next command until `seal mode` writes it. It reaches the mode question alone. Nothing reads the `Broad gate` proposal, so a repository that was never offered candidates meets `seal gate`'s own refusal after the rounds have settled. The workflow file is written by `seal pr-checks install`, whose substitution of the version `tests/skills/test_seal.py` holds, and nothing checks that the orchestrator ran it under the second answer. A yes at step 3 follows `skills/parity-setup/SKILL.md` *Procedure*, and nothing reads that it ran: the pull request's parity arm wakes on `seal/parity.md` existing, so a setup that never happened is silence rather than a refusal, and a guessed original produces a file that parses |
| Orchestrator: how the work is routed | `skills/implement/orchestration.md` | check: `hooks/routing-edit-gate.py` | The first `Write`, `Edit` or `NotebookEdit` is refused until a declaration naming the branch stands under the `seal/` root or the session ran `seal no-work-item` on that branch, and the core, `skills/core/SKILL.md`, which the plugin's `SessionStart` hook prints into every session, names this section and `hooks/routing-edit-gate.py`. What neither reaches is the shape of the asking: a declaration built from four separate questions parses exactly like one built from the asking this section mandates |
| Question 1 | `skills/implement/orchestration.md` | part of its parent's act | The three options of the first `AskUserQuestion` call its parent describes, put alone. It names no act of its own |
| Question 2 | `skills/implement/orchestration.md` | part of its parent's act | The four boxes of the second call, put only after a `per axis` answer, and the ceiling on how many there may be. It names no act of its own |
| What the answer writes | `skills/implement/orchestration.md` | check: `skills/code-review/scripts/chain_check.py` | It refuses a `Review` or `Destination` value outside the vocabulary at the pull request, and `hooks/lib/routing.py` parses the same rows at every edit. The three optional rows are read by nothing that refuses: `hooks/implementer-notice.py` says one line after a commit where a declared agent left no mark, and blocks nothing |
| Orchestrator: where a decision or a lesson is written | `skills/implement/orchestration.md` | still a sentence | Nothing reads where a lesson went. A lesson kept only in a session's local memory leaves the same tree as a run that learned nothing, and no check can open a machine's memory to find it there. Nothing reads a lesson judged not worth a home either: its grounds are a sentence of the work item's records, which the settle reads and no check refuses |
| Orchestrator: a work item that commits in more than one repository | `skills/implement/multi-repository.md` | check: `hooks/routing-edit-gate.py` | In each opted-in repository the first edit is refused until a declaration naming that repository's branch stands there, so a repository the step skipped is noticed at its first edit. What it does not reach: an id minted twice is legitimate in a signer's own work item and nothing tells the two apart, and a missing `Pact` row is noticed only when somebody runs `seal pact` at the pact's repository, which refuses a relationship recorded on one side |
| Orchestrator: which of these acts runs itself | `skills/implement/acts.md` | check: `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` | The test reads this table against the headings of the files this file's opening names, in both directions. What it reads is the marker rather than the meaning, so a heading with no prefix puts its act in neither the table nor the test |
| Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer | `skills/code-review/orchestration.md` | still a sentence | A phase built by a resumed crafter and one built by a fresh crafter leave identical trees, and so do a resumed fix pass and a fresh one, so nothing at the pull request can tell them apart, and the choice of session is in no file. `seal cost --segments` prints the context the threshold is read against and gates nothing, so the reading can go untaken while the spawn succeeds. Whether the orchestrator's one commit after the fix pass carried a finding's `verdict:` and `answer:` lines is in the round record's history and no check reads it, and a refusal at the pull request could be cured only by rewriting the branch's history; who wrote the two lines, and whether that commit changed what the fix pass left, is in no commit, because the fix pass commits neither line |
| Orchestrator: the run ends with a verifying round | `skills/code-review/orchestration.md` | check: `skills/code-review/scripts/chain_check.py` | It fails a ready pull request when a commit touching a file outside the work item's records follows the commit on the last record's `target:` line, or a finding of that record reads `rejected`, or `fixed <commit>` for a finding located outside the work item's records or by a commit that changed a file outside them, which is the run whose own last fixes nobody opened; on a draft it prints and names the verifying round. What it cannot read is the cap: the extension lines are the proofer's, and the sealer reads the count |
| A regression is routed by comparing the fix with the frame | `skills/code-review/orchestration.md` | still a sentence | The proofer's `regression:` line routes nothing mechanical, and neither does the sentence of its grounds the route reads: `skills/code-review/scripts/chain_check.py` reads the line only as a reference to an earlier finding, and the `Reframed` line only for its author against the declaration, and the sealer reads the records |
| Orchestrator: the pull request opens once the sealer seals | `skills/code-review/orchestration.md` | still a sentence | A pull request opened before the sealer leaves the same tree as one opened after it, so nothing reads the timing, nothing records that a platform-specific change ran `gh workflow run tests` before the broad run, nothing records that `mergeable` was read before CI was waited on, and nothing gives a merge that resolved a conflict outside the records its verifying round, because the chain check reads no merge commit. What is delivered is the step the section ends on: `skills/code-review/scripts/chain_check.py` fails a ready pull request whose `trail/gate.md` is absent or names a commit other than HEAD, which is what makes the orchestrator's broad run and the sealer's spawn after it happen. The step before that run, `seal gate --preflight`, is recorded nowhere either, and a session that skips it loses time and nothing else: the broad run asks the same arms and refuses the same way. The body's copy of the records is read: the sealer's step 2 runs `seal pr-body --check` on the body file and withholds where the part below the line `skills/code-review/scripts/pr_body.py#HEADING` holds is not the records' text at HEAD, so a body written before `trail/gate.md` was committed, not written again after a repair, or edited below that line is refused before the pull request opens. Nothing reads whether the orchestrator's part above that line restates a record; the sealer reads that part as one party among five |
| Orchestrator: verify before posting | `skills/code-review/orchestration.md` | still a sentence | The four checks are readings the orchestrator takes before posting, and nothing in the tree records that any of them happened. The one part a record carries is the new HEAD on the next round's `target:` line where HEAD moved |
