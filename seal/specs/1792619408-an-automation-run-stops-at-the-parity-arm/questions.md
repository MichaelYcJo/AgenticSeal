# Questions for the planner: an automation run stops at the parity arm

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md holds the decisions
only a human can make, extracted so nothing ships on a silent assumption.
Before adding a row, the framer checks the inheritance rule: where policy is
silent but existing behaviour answers the question, the framer inherits that
answer and records it; only a new rule belongs here. -->

## What the tree answered, so nobody reopens it

The issue left these open and the repository settled them; the grounds are
in `spec.md` and in `plan.md`'s Alternatives table.

- **The design is B: a chain declaration quiets the arm at the commit, and
  the pull-request check reads an `original:` line in every round record.**
  The issue's four candidates are rows B, C, E and the rest of `plan.md`'s
  table, each with its failure scenario.
- **The smith writes no parity mark and no comparison record.**
  `skills/legacy-parity/SKILL.md` *Recording the comparison* names the
  writers, contract §6 withholds the spawn of a scribe from the smith, and
  the builder certifying its own comparison is what the review arm's two
  answers refuse (rows C and D).
- **No routing row and no fifth box.** Question 2 is at its cap, and
  `seal/parity.md` already declares the migration (row F).
- **The commit-time arm, its mark and `[no-parity]` stay for an undeclared
  branch.** The premise was checked: question 1's `no work item` answer
  exists, and the visible waiver is that path's only trace (row G).
- **Every round record owes the line, not only the last.** A finding round
  reads the branch and a verifying round reads only its fixes, so each
  round compares a different range. A verifying round whose fixes touch
  only `docs/` and `seal/` still writes the line; different answers here do
  not change what the build writes, so this is the assumption.
- **The line names the baseline, and the check compares it with
  `seal/parity.md`.** `legacy-parity` *The migration config* says a
  comparison against a guessed original proves nothing; naming the baseline
  makes that a line the check can refuse.
- **The grammar row is edited into `docs/` by the build, and the prose rules
  go through `## Rule changes`.** `chain_check.py#grammar` loads the table
  from `docs/the-review-record.md` when it runs, so a row applied after the
  release would leave the release's reader without its line; #1000 edited
  its old-spellings table the same way (`ebbbd2f0`, its phase 3).
- **The parity arm's attended refusal text gains no *declare the routing*
  option.** Where both arms stand, the review arm's options already offer
  the declaration; where the parity arm stands alone, the review arm was
  waived with `[no-review]`, so the commit belongs to no work item and a
  declaration is not its way on. `tests/test_routing_is_recorded.py#test_the_parity_arm_gains_no_third_way`
  keeps its property under a `straight to the PR` declaration.
- **A chain branch that stops before the pull request is checked by
  nothing.** That is the review arm's stated cost
  (`docs/the-review-and-parity-arms.md` *The declaration, and where the check
  went*, *What it costs*), and the new paragraph names it for this arm.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **Does a declaration answering `straight to the PR` quiet the parity arm too?** The tree cannot answer it: under that answer no review round exists to carry a comparison, so the choice is between what the direct answer means in a migration repository and how much protection it keeps, and no document says which. A per-axis run with `Automation` `yes` and `straight to the PR` in a migration repository still stops at its first code commit under the default | a person | **(a) the arm stays at the commit under `straight to the PR`** (the default): that run shape stops and hands back as it does today, and the new `docs/` paragraph states it as a limit. **(b) the declaration quiets it, and the pull request owes a comparison record the orchestrator writes**: a new home is needed, because the direct answer owes `broad-gate.md` and `guarantee.md` and neither holds a comparison; this is a further work item. **(c) the declaration quiets it and nothing is owed**: that answer then carries no parity protection anywhere | (a) | open |
| Q2 | **Where does the `Baseline commit` reader live, and how does `chain_check.py` load the doc-root rule?** Unknowable at framing time: it turns on what `hooks/config.py#read_table` accepts for the `Field` and `Value` header `templates/parity.md` writes, and on how `chain_check.py` already loads modules by path (`SHARED_READER`) | the work | phase 1 decides and records it in `phases/phase-1.md`, under the constraint that each fact has one reader: one function reads the cell, and `hooks/gate.py#DOC_ROOTS` is not copied | one function in `hooks/config.py`, and `hooks/gate.py` loaded by path | open |

**`Who can answer` takes one of three values and nothing else.**

- **a person**: what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build. Q1 is this kind, and the build proceeds on its
  default.
- **a measurement**: a probe, a command or a count settles it, so a person is
  the wrong instrument, and queueing the row behind one wastes a round trip.
- **the work**: unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once. Q2 is this kind.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing, and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way also keeps the batch short
enough to answer in one sitting: two of the three kinds never need a person.

The orchestrator carries each answered row into `spec.md`'s `## Rule
changes` (a policy clause or an open-questions section) when it drains the
work item's rows, at the moment `skills/implement/SKILL.md` *6. Drain the
rows before the broad run, and keep the records* names.
