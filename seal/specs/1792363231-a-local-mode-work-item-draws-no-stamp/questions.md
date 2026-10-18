# a local-mode work item draws no stamp (#976) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**What the ticket left open and the tree answered**, so nobody reopens it.
Each is argued in `plan.md` §*Alternatives considered* or `spec.md`.

1. *Which event marks a local-mode `sealed`.* The `Write` or `Edit` that
   leaves the file reading it, seen by a gate in the existing `post-edit`
   group. A `Stop` or commit scan would draw every item `settle` never
   retired, and a command would be an act to remember (`plan.md` A1, A3, A4,
   A6).
2. *Replace `post-commit` for both modes, or add beside it.* Beside it. The
   replacement would lose today's shared-mode stamp wherever the sealer works
   in a scratch clone, and it would draw before the orchestrator commits the
   verdict the pull request's check reads (`plan.md` A2).
3. *How once per work item is held in local mode.* The values files are
   enough, because the local root and `specseal-stamp/` share one common
   directory. The row's earlier-run chain and the audited commit standing on
   the `Branch` row's branch add to them. No history is read, because none
   exists (`plan.md` A10, `spec.md` S3, S4).
4. *A separate gate file or the drawing hook answering two events.* A
   separate file, `hooks/sealer-stamp-queue.py`, so the pin that holds the
   drawing hook to `Stop` stands (`plan.md` A9).
5. *Whether `agents/sealer.md` changes, and whether that owes a run.* The
   clause says the stamp is drawn from the sealer's *committed* `sealed`,
   which is false in local mode, so the word goes (contract §19). #957's
   rule measures any changed read set, so phase 4 runs one side against
   #975's phase-4 side. The definition shrinks by one word, so rule 4
   (preload) cannot get worse.
6. *Where the line `seal-stamp --from <path>` goes in local mode.* There is
   no commit output to carry it, so it goes as the edit gate's
   `systemMessage`. `seal_stamp.QUEUED` is unchanged, so both modes say one
   sentence.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a `PostToolUse` hook fired by a subagent's `Write` carry the main session's `session_id`? The local values file is keyed by it, and the main session's `Stop` reads only its own directory. #400's `questions.md` Q2 measured this for `SubagentStop` on 2026-09-28, and `hooks/hooksession.py` measured it for the environment variable a subagent's Bash child carries. Nobody has measured it for `PostToolUse`. The tree cannot answer it, because it is the harness's behaviour, and no case can spawn a subagent (contract §6) | a measurement — the orchestrator, before phase 2 closes: a scratch `PostToolUse` hook logging `session_id` and `agent_id`, then any subagent that writes one file, then compare with the main session's id. Or the owner, on the first local-mode run after 0.22.2 | (a) it is the parent's id: the build stands as framed; (b) it is the subagent's own id: the gate keys the file by the payload's parent id where the payload names one, or the stamp is missing and §*The stamp* says so | (a), the same shape as `SubagentStop` | open |
| Q2 | #976's comment carries #975's Q7 gap. A `sealed` over a commit the branch does not hold draws nothing, and the corrected re-seal draws nothing either, because the history cannot tell it from a `sealed` stamped before a rebase (#975 Q8, never twice). Does #976 close with that gap as a stated limit, or build a mechanism? The tree argues for the limit: the gap only follows a guarantee the pull request's check already refuses as stale, and the one mechanism found (A8, patch-equivalence) adds a fourth reading to the reader rounds 3 to 6 kept regressing. But the owner sent the gap to this issue, and closing the issue without a mechanism is the owner's to accept | a person (the repository owner) | (a) a stated limit: the "#976 carries" sentences say so (S8), and no code changes for it; (b) build A8 in shared mode's `sealed_before`, as one more phase with its own red cases against round 5's rebase case | (a); the build proceeds on it under `Automation \| yes`, and an answer of (b) is one later phase that touches `sealed_before` alone | open |
| Q3 | On Windows, does `os.path.realpath` on the payload's `file_path` and on `git rev-parse --git-common-dir` give two strings that compare equal, given drive-letter case and separators? | the work — phase 2 meets it in the Windows leg of CI and normalizes with `os.path.normcase` where the leg says so | — | — | open |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip. Measured: six probes at about three seconds each answered a row that
  had been written into the human batch, and they showed the ticket's own
  instruction was wrong.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way is also what keeps the
batch short enough to answer in one sitting: two of the three kinds never
needed a person at all.

Q2 is a person's row and does not stop this build. The owner pressed
`automation` (`routing.md`). The default builds the same trigger as either
answer, and an answer of (b) adds one phase to shared mode's reader and
changes nothing in the local trigger.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
