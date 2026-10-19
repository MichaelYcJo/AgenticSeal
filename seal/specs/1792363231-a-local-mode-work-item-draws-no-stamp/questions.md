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
   which is false in local mode, so the word went in phase 4 (contract §19)
   and phase 5 measured it. The redesign after round 2 changes no
   definition, so nothing is measured again (`spec.md` S9).
6. *Where the line `seal-stamp --from <path>` goes in local mode.* There is
   no commit output to carry it, so it goes as the edit gate's
   `systemMessage`. `seal_stamp.QUEUED` is unchanged, so both modes say one
   sentence.
7. *The form Q2's (b) was first built in.* Q2's option (b) named A8,
   patch-equivalence inside `sealed_before`; reading #975's rounds 4 and 5
   settled that A8 is round 4's shape again, so phases 3 and 4 built a
   refusal record the refusing writer leaves in its own clone, under guards
   (`plan.md` A11). Rounds 1 and 2 then found the record failing in both
   directions wherever a guarantee travels, one path per guard, and the
   owner chose a redesign on 2026-10-19 ("설계를 다시").
8. *What structure closes the re-seal gap without a clone-local inference
   that each git operation can defeat.* Refusing the wrong verdict at its
   commit (`plan.md` A14). The fact the readers kept trying to recover after
   the fact, that a `sealed` names a commit the branch does not hold, is
   known with certainty at exactly one moment to exactly one party: the
   `pre-commit` hook of the commit that would make it history, in the clone
   that commits it. The commit gate already runs there, reads the index, and
   prints into the command's output. Stopped there, the verdict is never a
   fact for another clone to misread, and #975's once readers need no
   change. Weighed as equals: A11 with round 2's two guards (A15, the next
   path is this repository's own push-then-rebase flow with a `sealed` on
   the tracking ref), a stated limit (A16, the owner's rejected answer, and
   the common case stays open), a record that travels with the file (A17,
   either direction of marker fails Q8 or round 1), and the sealer or
   `git notes` writing it (A18). In local mode no commit exists to refuse,
   and the record of phase 3 stays there, because a local root never leaves
   its clone and so "did this clone draw" is the whole question
   (`spec.md` S14); it gains the line a person needs, since no pull request
   reads a local guarantee (`spec.md` S4).
9. *Whether the `reference-transaction` backstop should judge the same
   fact for `--no-verify`.* No. The backstop exists for the arms, which an
   agent could step around by a flag; no agent of this plugin issues
   `--no-verify`, and a second reader of the same fact at a second hook is
   the shape the subtraction rule refuses. Stated as a limit (`spec.md`
   S13, `plan.md` A14).
10. *Whether the guard-2 measurement Q4 recorded still holds a rule.* It
    does not after phase 7: nothing reads the reflog. The row stays as the
    record of a measurement that was made.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a `PostToolUse` hook fired by a subagent's `Write` carry the main session's `session_id`? The local values file is keyed by it, and the main session's `Stop` reads only its own directory. #400's `questions.md` Q2 measured this for `SubagentStop` on 2026-09-28, and `hooks/hooksession.py` measured it for the environment variable a subagent's Bash child carries. Nobody has measured it for `PostToolUse`. The tree cannot answer it, because it is the harness's behaviour, and no case can spawn a subagent (contract §6) | a measurement — the orchestrator, before phase 2 closes: a scratch `PostToolUse` hook logging `session_id` and `agent_id`, then any subagent that writes one file, then compare with the main session's id. Or the owner, on the first local-mode run after 0.22.2 | (a) it is the parent's id: the build stands as framed; (b) it is the subagent's own id: the gate keys the file by the payload's parent id where the payload names one, or the stamp is missing and §*The stamp* says so | (a), the same shape as `SubagentStop` | answered (a) 2026-10-19 by the orchestrator, by measurement: `hooks/session-lease.py`, a `PostToolUse` hook on `Write\|Edit\|NotebookEdit`, names its lease file by the payload's `session_id`. The only process that wrote into this worktree before b1dd8e79's framer finished was that framer subagent, and `.git/worktrees/976/specseal-leases/` held exactly one file, `df5caeb2-ee37-44ef-8c91-cb0853f0eb20`, the main session's id (stamped 07:49–07:51). The framer's transcript lines carry the same `sessionId` |
| Q2 | #976's comment carries #975's Q7 gap. A `sealed` over a commit the branch does not hold draws nothing, and the corrected re-seal draws nothing either, because the history cannot tell it from a `sealed` stamped before a rebase (#975 Q8, never twice). Does #976 close with that gap as a stated limit, or build a mechanism? The tree argues for the limit: the gap only follows a guarantee the pull request's check already refuses as stale, and the one mechanism found (A8, patch-equivalence) adds a fourth reading to the reader rounds 3 to 6 kept regressing. But the owner sent the gap to this issue, and closing the issue without a mechanism is the owner's to accept | a person (the repository owner) | (a) a stated limit: the "#976 carries" sentences say so (S8), and no code changes for it; (b) build A8 in shared mode's `sealed_before`, as one more phase with its own red cases against round 5's rebase case | (a); the build proceeds on it under `Automation \| yes`, and an answer of (b) is one later phase that touches `sealed_before` alone | answered (b) 2026-10-19 by the repository owner: "막는 장치를 만들도록 해 — 한계만 적으면 계속 공백인 거잖아". Built as phase 3 in the form the head's item 7 gives; redesigned after round 2 on the owner's "설계를 다시" (2026-10-19) into the form the head's item 8 gives, phases 6 to 8 |
| Q4 | Does `git reflog -1 --format=%gs HEAD`, read inside `post-commit`, already show the commit that triggered it, and with which subjects across the git versions CI runs: `commit:` for a plain commit, `commit (amend):`, `rebase (pick):` or `rebase (continue):`, `cherry-pick:`, `commit (merge):`? Guard 2 reads it, and a subject it does not know must write no record | a measurement — phase 3's guard-2 cases run each of those commands against real git in the fixtures, on every CI leg | — | — | answered 2026-10-19 by the orchestrator, from `phases/phase-3.md`: on git 2.50.1 (Apple Git-155) the reflog's newest entry inside a real `post-commit` already names the triggering commit, with the subjects `commit (initial): `, `commit: `, `commit (amend): `, `cherry-pick: `, `rebase (pick): `, `rebase (continue): ` and `commit (merge): `. After phase 7 nothing reads the reflog, and `test_guard_two_reads_what_post_commit_sees_in_the_reflog` goes with the guard (head item 10) |
| Q3 | On Windows, does `os.path.realpath` on the payload's `file_path` and on `git rev-parse --git-common-dir` give two strings that compare equal, given drive-letter case and separators? | the work — phase 2 meets it in the Windows leg of CI and normalizes with `os.path.normcase` where the leg says so | — | — | open |
| Q5 | The refusal at the commit (`plan.md` A14) has no waiver: a `sealed` whose `Target SHA` names a commit the declared branch does not hold cannot be committed on that branch while the stub judges, and the only way on the text names is a new audit of the sealer at HEAD. The tree argues for none: the pull request's check refuses the same file (`docs/the-review-record.md` §*The guarantee*), the arms' waivers exist because a declaration or a parity record is something a person may rightly not have yet, and here there is nothing a person rightly has. But a refusal with no way past is a product decision, and the owner has asked that a question name its paths. Does the refusal offer a waiver? | a person (the repository owner) | (a) no waiver: the text names the sealer's new audit as the one way on, and `--no-verify` stays git's own flag, a stated limit (S13); (b) `git -c specseal.waive=stamp commit …` and `: '[no-stamp]';`, read by `commitgate.waived` as the arms' are, which commits the wrong row and leaves the gap for that item as #975 left it | (a); phase 6 builds it so, and an answer of (b) is one later change to `gate.py`'s token tables and the text, with its own case | answered (a) 2026-10-19 by the repository owner: no waiver |
| Q7 | What does the one `git diff --cached --name-only` on every judged commit, and the `git show` plus the `chain_check.py` import on a commit that stages a `sealed` guarantee, add to a judged commit's latency? `docs/the-commit-gate-inside-git.md`'s bullet reads 209–400 ms a commit under load, and #975's phase 2 measured its `diff-tree` at about 10 ms as medians of 11 commits | a measurement — phase 6 times `git commit` with and without the refusal on the same fixture, as #975's phase 2 did, and the phase record and the latency bullet carry both figures | — (the work measures it) | — | open |
| Q6 | Does `git show :<path>` inside `pre-commit` read the index the commit will write for every commit shape the stub judges: a plain `git add` then `commit`, `commit -a`, and `commit <pathspec>`, where git hands the hook a temporary index through `GIT_INDEX_FILE` (#692's M2 measured that for the paths listing)? | the work — phase 6's S12 case runs each shape against real git, on every CI leg, and a shape whose index the hook misreads fails there naming the shape | — | — | open |

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

Q2 was the one person's row of the first frame. The owner answered it during
the run, after phase 1 had closed, and the answer added phase 3 without
changing phase 1's trigger. Q5 is the one person's row of the reframe after
round 2, and its default lets the build proceed: a different answer is one
later change to the refusal's text and tokens.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
