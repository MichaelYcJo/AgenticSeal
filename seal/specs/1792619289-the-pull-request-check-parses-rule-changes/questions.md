# Questions for the planner: the pull request check parses each spec's rule changes (#1006)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md holds the decisions
only a human can make, extracted so nothing ships on a silent assumption.
Before adding a row, the framer checks the inheritance rule: where policy is
silent but existing behaviour answers the question, the framer inherits that
answer and records it; only a new rule belongs here. -->

**Judgments the issue left open that the tree answered.** Each is decided in
`spec.md` or in `plan.md`'s Alternatives table, with its grounds there, and
nobody reopens it here.

- **Which `spec.md` files are read.** The `spec.md` of each work item whose
  `routing.md` the check judges, and every work item `spec.md` the pull
  request's own commits add or change on a pull request that declares at
  least one work item (`plan.md` A1 against A2, A3 and A9). Round 1's
  finding 1 decided the second set, and the reframe recorded it.
- **A pull request that declares nothing.** It reads no `spec.md`, which
  keeps the promise in `.github/workflows/hygiene.yml` and `CONTRIBUTING.md`
  (`plan.md` A2).
- **A `spec.md` a squash of another pull request carried, or one only
  moved.** Not read, because *An item is judged at the pull request that
  carries it* and *The check reads the diff as declarations, not as file
  identity* in the same section decide it for declarations, and the same
  `carried_by` and moved set serve.
- **A work item declared `the session`.** Read like one declared `framer`,
  because the parse is owed under either `Planning` answer.
- **Which reader, and how it is loaded.** `rule_changes.parse`, through
  `unverified_check.py#rule_changes`, the loader `chain_check.py#retired`
  already reaches (`plan.md` A8).
- **Which policy root.** `unverified_check.py#policy_root`, the value
  `settle` passes, so a `file:` outside that root is refused as `settle`
  refuses it.
- **Draft, ready and `--sealing`.** The read is judged like every refusal of
  the check, and stays a refusal under `--sealing`. The broad run and the
  preflight print it and do not fail on it, because no pull request exists
  when they run (`spec.md` *Scope* item 3). Whether they should judge it
  strictly is round 1's `## Not judged` row for the owner, and is not
  reopened here.
- **A section holding only the template's comment.** Refused with the
  parser's reason, `the section is empty`, because `settle` refuses it too.
- **The refusal's text.** One constant, fixed in `spec.md` *Data &
  interfaces*, with the parser's reason last and verbatim.
- **The table in `docs/the-review-and-parity-arms.md` *The declaration, and
  where the check went*.** Unchanged, because it lists what each `Review`
  answer owes and the parse is owed under both.
- **The hygiene step's name.** Unchanged (`spec.md` *Scope*, the last item
  under *Out*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Should the check refuse a `spec.md` that the pull request adds with no `## Rule changes` section at all? The tree cannot answer it. `skills/settle/SKILL.md` *What `--apply` does* says a spec with no section *was written before the section existed; it is named and stays*, which describes specs older than the template's section and says nothing of a new one. Issue #1006 item 3 leaves such a spec alone. Whether a spec written after the template gained the section owes one is a rule nobody has written | a person | (a) leave it alone, as the issue says: a new spec with no section merges, and `settle` names it and keeps its directory after the release. (b) refuse a `spec.md` this pull request adds with no section, at its first line: a new rule in `docs/the-review-record.md`, and one more condition in `rule_changes_read`, which has to ask the diff whether the file was added. Measured at the frame: none of the 119 specs in the tree lacks the section (executed, in memory), so (b) would refuse nothing that stands today | (a). The build proceeds on it, and (b) is one condition and one case added later | open |

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

The orchestrator carries each answered row into `spec.md`'s `## Rule
changes` (a policy clause or an open-questions section) when it drains the
work item's rows, at the moment `skills/implement/SKILL.md` *6. Drain the
rows before the broad run, and keep the records* names.
