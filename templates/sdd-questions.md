# Questions for the planner: <work item>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md holds the decisions
only a human can make, extracted so nothing ships on a silent assumption.
Before adding a row, the framer checks the inheritance rule: where policy is
silent but existing behaviour answers the question, the framer inherits that
answer and records it; only a new rule belongs here. -->

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | | | | | open |

**`Who can answer` takes one of three values and nothing else.**

- **a person**: what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement**: a probe, a command or a count settles it, so a person is
  the wrong instrument, and queueing the row behind one wastes a round trip.
- **the work**: unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing, and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way also keeps the batch short
enough to answer in one sitting: two of the three kinds never need a person.

Answered rows feed back into `spec.md`'s `## Rule changes` (a policy clause
or an open-questions section) before this directory's work merges.
