### Changed

- **A review round is one file the warden writes, and nothing generates it
  (#923).** `seal/specs/<id>/rounds/round-N.md`, from
  `templates/sdd-round.md`, holds the commit the round reviewed
  (`Target SHA`), its findings in the five-column `## Verdicts` table, the
  paste-ready fixes and the probes it ran. No `round-N-report.md` stands
  beside it any more. The fix pass closes each open 🔴 or 🟡 row by filling
  two cells: `Verdict` reads `fixed <commit>`, `answered` or
  `deferred <home>`, and `Grounds` gains what the fix pass did. The fields a
  generator wrote around the table leave with it: `Pass`,
  `Fixes checked by`, `Needs a fix`, `Written late`, `Fix range`,
  `Contract changes`, `New units`, `Fix of a fix`,
  `Loses a record or crashes`, `Ran by` and `PR`. ⬜ is no longer a
  severity; a wrong sentence an agent acts on is a 🟡. Records written
  before 0.22.0 read as they stand, because the check reads only their
  `Target SHA` and their verdict table. The rules around the rounds are
  stated once, in `docs/the-review-record.md`: a run ends with a verifying
  round, it has three finding rounds by default and extends one at a time
  while the findings shrink, a finding marked `fix of a fix` sends the work
  item back to its framer, and a leftover finding takes the first rung of
  the filing ladder that fits.
  (`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
  #923)
- **The check at the pull request reads five facts, and a ready pull request
  fails on any of them (#923).** `chain_check.py` judges the `routing.md`
  naming the pull request's branch and every one its own commits add or
  change. The declaration has to parse. A declared framer left `spec.md`,
  `plan.md` and its mark. A declared review chain left at least one round,
  every row of every round reads a word that closes it, whatever mark the
  row carries: `fixed`, `answered`, `deferred <home>`, `confirmed` or
  `out of verified scope`. A refusal names the words for the row's mark:
  a fix pass's three for a 🔴 or 🟡 row, `confirmed` for a 🟢 row, and
  `❓ out of verified scope` for a ❓ row. The last round's commit is HEAD
  or only the work item's own records follow it. `broad-gate.md` names
  HEAD.
  `guarantee.md` names HEAD and reads `sound`. A draft prints every refusal
  and fails nothing. A declaration that reached the branch inside another
  pull request's squash, a commit GitHub made with a subject ending `(#N)`,
  was judged at that pull request and is named rather than judged again, so
  a release pull request into `main` passes over the items squashed into
  its release branch. What to do: move the `v<version>` in your copy of
  `templates/hygiene.yml` to this release's tag, and delete its step that
  fetched `refs/pull/*/head`, which nothing reads now. From then on, a work
  item's pull request is marked ready only after its sealer has run.
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
  `seen red` claims, chosen where the evidence is thinnest. It confirms each
  `fixed <commit>` is on the branch and touches the location it fixes, and
  that nothing this release removed has come back. It reads every 🔴 and 🟡
  row of every round: the check passes one closed `confirmed` or `out of
  verified scope`, and the sealer's verdict is `not sound` unless a later
  round answers it. It reads the spec, the build, the warden's last round,
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
  the round, and the fix pass fills its two cells by hand.
  `docs/round-record-spec.md`, `docs/review-chain-spec.md` and
  `docs/review-handoff-protocol.md` give way to `docs/the-review-record.md`.

  | File | Lines before | Lines after |
  |---|---|---|
  | `skills/code-review/scripts/chain_check.py` | 6,153 | 1,128 |
  | `skills/code-review/scripts/round_record.py` | 5,596 | gone |
  | `skills/verify/scripts/broad_gate.py` | 3,648 | 3,400 |
  | `hooks/review-history-guard.py` | 303 | gone |
  | `templates/sdd-round.md` | 460 | 46 |
  | the three record documents | 2,725 | 232, one document |
  | `agents/sealer.md` | 268 | 147 |

  Counted against `origin/release/v0.22.0` at `ce448bbe`. The suite holds
  143 test modules where it held 167, and 31,996 lines of tests left
  against 3,135 added.
  (`1791933022-every-agent-skill-and-doc-states-the-current-rule-only`,
  #923)
