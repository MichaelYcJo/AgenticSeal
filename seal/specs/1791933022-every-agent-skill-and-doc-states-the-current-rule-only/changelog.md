### Changed

- **A review round is one file the warden writes, in words, and nothing
  generates it (#923).** `seal/specs/<id>/rounds/round-N.md`, from
  `templates/sdd-round.md`, opens with a `target:` line naming the commit
  the round reviewed. Under `## Findings` each finding is a
  `### <n>. <symptom>` section with lowercase labels at the start of their
  lines: `severity:` (`must` or `should`, which no check reads),
  `location:` (backticked coordinates where the defect shows), `verdict:`
  (`open`, `fixed <commit>`, `rejected` or `deferred <home>`), a
  `regression:` line where the finding sits in a unit the fixes under
  review made, and the fix pass's `answer:`. The paste-ready fix sits inside
  its finding. What the round confirmed is a `confirms:` line under
  `## Confirmations`, left out when there is nothing to confirm; what it
  could not judge is a row of `## Not judged`; the commands it ran are
  `## Probes`. No emoji stands anywhere in a record. The fix pass rewrites
  `verdict:`, writes `answer:`, and adds the coordinate it fixed to
  `location:` where that is somewhere else. No `round-N-report.md` stands
  beside the record any more, and the fields a generator wrote leave:
  `Pass`, `Fixes checked by`, `Needs a fix`, `Written late`, `Fix range`,
  `Contract changes`, `New units`, `Fix of a fix`,
  `Loses a record or crashes`, `Ran by` and `PR`. The rules around the
  rounds are stated once, in `docs/the-review-record.md`: a run ends with a
  verifying round, it has three finding rounds by default and extends one
  at a time while the findings shrink, a finding with a `regression:` line
  sends the work item back to its framer, and a leftover finding takes the
  first rung of the filing ladder that fits.
  **A work item in flight when you update** keeps records in the old shape,
  and the check refuses each one by name once its pull request is ready.
  Before you mark it ready, rewrite each record: the `| Field | Value |`
  table becomes `target: <its Target SHA value>`; each 🔴 or 🟡 row becomes
  a `### <n>.` section with `severity: must` for 🔴 and `should` for 🟡,
  `location:` holding its Location cell's coordinates, each backticked and
  joined by `, `, `verdict:` holding its Verdict cell (`answered` is
  `rejected` now), its paste-ready block, and `answer:` holding what the fix
  pass wrote; each 🟢 row becomes `confirms: round-<N>#<n>` naming the
  finding it confirmed, or `confirms: none`, with its text on the next line;
  each ❓ row becomes a row of `## Not judged`; `## Executed probes` becomes
  `## Probes`. Then run `python3 skills/code-review/scripts/chain_check.py
  --baseline origin/<base> --worktree` and fix what it still names. The
  other way is to finish that work item on 0.21.1 before you update.
  (`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
  #923)
- **The check at the pull request reads what a record states in its
  labelled lines, refuses what it cannot read, and a ready pull request
  fails on any refusal (#923).** `chain_check.py` judges the `routing.md`
  naming the pull request's branch and every one its own commits add or
  change. The declaration has to parse. A declared framer left `spec.md`,
  `plan.md` and its mark. A declared review chain left at least one round,
  and four facts hold of its records. Every finding has an answer: none
  reads `open`. Every `fixed <commit>` is a commit on the branch that
  changed a path its `location:` line names. Every `fixed` or `rejected`
  finding of round N is named by a `confirms:` or `regression:` line of
  round N+1, or it is refused at its own heading. The last round's
  `target:` commit is HEAD or only the work item's own records follow it,
  and none of that round's findings is `fixed` or `rejected`, since no
  round read them. A label in any other spelling (`Verdict:`, `Target SHA`,
  `refixes:`), a value outside its shape, a missing or doubled line and a
  fence that never closes are each refused by line, never passed.
  `broad-gate.md` names HEAD. `guarantee.md` names HEAD and reads `sound`.
  A draft prints every refusal and fails nothing. A declaration that
  reached the branch inside another pull request's squash, a commit GitHub
  made with a subject ending `(#N)`, was judged at that pull request and is
  named rather than judged again, so a release pull request into `main`
  passes over the items squashed into its release branch. What to do: move
  the `v<version>` in your copy of `templates/hygiene.yml` to this release's
  tag, and delete its step that fetched `refs/pull/*/head`, which nothing
  reads now. From then on, a work item's pull request is marked ready only
  after its sealer has run.
  (`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
  #923)
- **The broad run has one home, `broad-gate.md`, on either routing answer
  (#923).** `broad-gate --record <item>` writes it on a green run, newest
  run first with every earlier run kept behind it, where 0.21.1 wrote the
  last round record's `Broad gate` cell for a reviewed item and the file
  only for one that went straight to the pull request.
  (`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
  #923)
- **The sealer is the final, independent guarantor, and it runs on Opus
  (#923).** It used to run one command and judge nothing. It now runs after
  the pull request body and the changelog fragment are written, and its
  reference is the issue and the tree, never another agent's account. It
  runs the broad gate, then re-runs a sample of the smith's `executed` and
  `seen red` claims, chosen where the evidence is thinnest, and confirms
  that nothing this release removed has come back. It reads the spec, the
  build, the warden's last round,
  the changelog fragment and the pull request body as one story and names
  the party the issue and the tree contradict. It does not re-judge the
  design or the code's quality. Its
  verdict is `seal/specs/<id>/guarantee.md`, from
  `templates/sdd-guarantee.md`: the claims it re-ran, the parties it
  compared and one `Verdict:` line, `sound`, `not sound — <what>` or
  `undecidable — <question>`. An undecidable question is yours: answer it on
  a line under the verdict, and the sealer runs again at the new HEAD.
  `agents/sealer.md` pins `model: opus`, so a sealer spawn now costs an
  Opus session where it cost one command.
  (`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
  #923)

### Removed

- **`bin/round-record` and the round-record generator leave (#923).**
  `round_record.py` with its `new`, `close`, `notes` and `seal`
  subcommands, `bin/round-record` and `bin/round-record.cmd`, the
  `tests-todo.md` file kind, and `hooks/review-history-guard.py`, the
  reminder printed on `gh pr review` and `gh pr merge`. A script or note
  that types `round-record` meets a command that is gone: the warden writes
  the round, and the fix pass writes its two lines by hand.
  `docs/round-record-spec.md`, `docs/review-chain-spec.md` and
  `docs/review-handoff-protocol.md` give way to `docs/the-review-record.md`.

  | File | Lines before, at `ce448bbe` |
  |---|---|
  | `skills/code-review/scripts/chain_check.py` | 6,153 |
  | `skills/code-review/scripts/round_record.py` | 5,596, gone |
  | `skills/verify/scripts/broad_gate.py` | 3,648 |
  | `hooks/review-history-guard.py` | 303, gone |
  | `templates/sdd-round.md` | 460 |
  | the three record documents | 2,725, one document now |
  | `agents/sealer.md` | 268 |

  Counted on `origin/release/v0.22.0` at `ce448bbe`, before this work item;
  `wc -l <file>` in this release gives a kept file's size after.
  (`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
  #923)
