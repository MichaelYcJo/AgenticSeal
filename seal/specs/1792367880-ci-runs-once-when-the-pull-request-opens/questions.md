# CI runs once, when the pull request opens (#943) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

**No row here needs a person.** The owner decided the rule (#943 §1, 2026-10-15), its scope (parts 1 and 2; part 3 is #984), and the limit (2026-10-19). The tree answered every judgment the ticket left open, and `plan.md` §*Alternatives considered* holds the grounds, so none of these is to be reopened:

- **Which workflows keep the draft events.** A workflow keeps them where it runs `chain_check.py`, the one script that reads draft state. Today that is `hygiene.yml` alone.
- **Whether the heading keeps *a phase is re-run*.** It does, because the section's *A hand-back's verification claim is a claim* paragraph is that re-run.
- **How the sealer reads a pull request body that is not open yet.** From a file the prompt names. `agents/sealer.md:38-39` already allows this, and #990's sealer read `976-pr.md` that way.
- **Whether `push` to `main` is cancelled.** It is not, because `release-report` reads the tag's `push` run.
- **When the platform-specific `workflow_dispatch` runs.** After the build's last phase closes, and the orchestrator reads its result before its broad run.
- **Whether `templates/hygiene.yml` gets the concurrency block.** It does not, because #943 is about this repository's minutes.
- **Whether `CONTRIBUTING.md` tells a contributor to use `workflow_dispatch`.** It does not, because dispatching a workflow upstream takes write access an outside contributor lacks. The maintainer's step lives in the owner section.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does GitHub behave as the YAML says? Three things to check: marking a draft ready starts `hygiene` and not `tests`, a second push cancels the first push's `tests` and `hygiene` runs, and a bare `pull_request:` runs on `opened`, `synchronize` and `reopened`. No local run can show trigger or cancellation behaviour, so the framer could not settle it from the tree | a measurement — this work item's own pull request: its checks on opening, and on any later push, read with `gh run list --branch <branch>` by the orchestrator | holds → nothing to do. Does not hold → a fix commit to the workflow, which takes the repair path the owner section states | the YAML is read as GitHub documents it | open |
| Q2 | What exact text replaces `CELL_UNCOMMITTED`'s *before the pull request is marked ready*? It has to be true for a pull request not yet open, for one already open (the repair path), and for a repository that opens drafts. The framer cannot fix the wording without seeing the cases that read it | the work — phase 2, within those constraints. `plan.md` suggests `commit it before you push` | any wording that meets the three constraints | `CI reads HEAD, so commit it before you push` | open |
| Q3 | Does `tests/test_every_orchestrator_act_names_its_delivery.py` need more than the acts-table row renamed to the new heading? The framer read only that test's docstring and the names of its helpers | the work — phase 2, by running it | rename only, or a further row change the test names | rename only | open |

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

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
