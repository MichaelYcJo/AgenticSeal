# the stamp is drawn from the sealer's verdict (#975) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**What the ticket left open and the tree answered**, so nobody reopens it.
Each is argued in `plan.md` §*Alternatives considered* or `spec.md`.

1. *Who reads `guarantee.md`'s `sealed`, and at which HEAD* — the plugin's
   git `post-commit` hook, at the commit that adds or changes the file, in
   the worktree it landed in (`plan.md` A1). The orchestrator already commits
   `guarantee.md` before the pull request is marked ready, so that commit is
   the HEAD the stamp names.
2. *How once per work item is held with nothing stored beside the tree* — by
   the `Target SHA` row's own `; earlier run: <sha> <verdict>` chain (a
   `sealed` after a `sealed` queues nothing) and by the values file's name
   `<ns>-<id>-<target sha>` (a re-commit of the same guarantee queues no
   second file). The `.drawn.json` claim is the one marker that exists today
   (`plan.md` B1).
3. *Whether the names change* — `hooks/sealer-stamp.py`, `bin/seal-stamp`,
   `seal_stamp.py` and `specseal-stamp/` keep their names; the stamp is the
   sealer's now, so the names say the true thing and only the words inside
   them change. #969's Alternatives row 4 weighed the rename the other way
   and left it to the reader this issue is (`plan.md` C1).
4. *The gate's pass and fail words* — `BROAD GATE PASSED` and `BROAD GATE
   FAILED`, beside the gate's own `PREFLIGHT PASSED`/`PREFLIGHT FAILED`
   (`broad_gate.py:2886-2887`). The owner's rule says only what the line must
   not say; any word that is not `sealed` builds the same code, so this is an
   assumption written down, not a question.
5. *Where the stamp's policy lives* — `docs/the-review-record.md` §*The
   stamp*, beside the verdict it is drawn from; `docs/the-broad-gate.md`
   loses §*Where the stamp is drawn* (`plan.md` F1).
6. *Whether an agent definition changes* — `agents/sealer.md:99-100`'s clause
   *from its own run* alone; measured against #969's reference in phase 4.
   No other definition names the stamp or the gate's line, and the contract
   is untouched, so no other agent is measured.
7. *The gate's terminal drawing* — gone; one form on every stream
   (`plan.md` D1).
8. *The `scale` key* — written by nothing from this release, which
   `docs/the-broad-gate.md:177-181` named as the first after 0.21.
9. *A person's own commit of a `sealed` guarantee* — queues nothing: the
   stamp is a session's turn-end drawing and a person at a keyboard has no
   turn; `spec.md` §*Scope* states it.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | What rows does the sealer's stamp carry? The 2026-10-07 panel (#832, the owner's design) carried the suite's counts, the chain's exit, the steps CI also runs and the deferral homes, all of them the gate's measurements. The owner's rule of 2026-10-18 puts the stamp apart from the test suite, and the writer runs at the guarantee's commit, where the gate's counts are not at hand without re-reading the gate's outputs | a person (the repository owner) | (a) `SEALED` · `tree` with the branch under it · `base` · `item` · `gate ✓ <run>` · `rounds <N>` — what the records at HEAD say, nothing re-measured; (b) (a) plus the deferral homes under `rounds`, read from the round records at the commit as `broad_gate.rounds_rows` reads them today, which moves that reader to `seal_stamp.py`; (c) (a) plus the suite's counts, which means the gate writing its counts to a file for the writer to pick up — `plan.md` E2, rejected on the frame's grounds | (a); the build proceeds on it under `Automation \| yes`, and an answer of (b) is one later change to the writer's rows | open |
| Q2 | How much does the second duty add to a judged commit's latency? Today 209–400 ms a commit under load (`docs/the-commit-gate-inside-git.md:233-236`). The new reader runs one `git diff-tree` on every judged commit and, only where a `guarantee.md` was touched, one `git show`, two record reads and the `chain_check.py` import | a measurement — phase 2 times `git commit` with and without the duty on the same fixture, and the phase record carries both figures beside the doc's | the doc's latency bullet gains the measured figure; where the `diff-tree` alone costs more than about 50 ms, the writer reads `GIT_INDEX_FILE`-free `git diff-tree` once and nothing else before deciding there is nothing to do | — (the work measures it) | open |
| Q3 | Does `noninferiority.py compare` accept a new side whose `--suite-rev` is this branch's commit against a reference whose `suite_rev` is `1483d8ba`? The trees are equal (`git rev-parse HEAD:evals/behaviour/sealer` = `5c3e8119…` at `a09ed4ce`, `executed`), and `compare` reads `suite_tree` (`noninferiority.py:404, 473, 963`, `read`) | a measurement — phase 4's `compare` exit code | exit 0, the comparison written; exit 2 means the suite moved under the branch, and the phase runs the reference again at the new tree before comparing, as #969's phase 6 did | — (the work measures it) | open |

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

Q1 is a person's row and does not stop this build: the owner pressed
`automation` (`routing.md`), the default builds the same mechanism as every
other option, and a different answer changes the writer's row list and
nothing else.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
