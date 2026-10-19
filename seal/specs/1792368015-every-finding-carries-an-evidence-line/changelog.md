### Changed

- **Every finding in a round record names what its claim rests on, and the
  check refuses one that does not (#985).** A finding carries one
  `evidence:` line. `evidence: executed` is followed by each command the
  round ran, and `evidence: read` by each `path:line` or `path:first-last`
  it opened, each backticked and joined by `, `. `chain_check` refuses a
  finding with no such line, with two, with the label spelt another way, or
  with a value of another shape, at its line and with the reason. The line
  is one row of the grammar table in `docs/the-review-record.md` §*The round
  record*, and the check's code did not change.

  A claim of absence, that nothing catches, calls or states something, is
  `executed` only, because no line opened can show an absence. The check
  cannot tell whether a claim is one of absence. The warden that writes the
  line and the round that reads it judge that. A later round re-runs an
  earlier finding's `executed` line rather than deriving the claim again.

  `agents/warden.md` names the line among a finding's lines and states the
  absence rule where it ordered the coverage probe. The warden's preload is
  27,168 bytes, 5 fewer than before. `templates/sdd-round.md` and
  `skills/code-review/SKILL.md` carry the line in place of the old
  "executed and read labelled apart".

  A record written before the row lacks the line, and that is no finding.
  The check reads only the records of the work items a pull request
  carries, so no merged record is read again or rewritten. Two readers
  still read old records at a release tag. v0.22.2's release panel shows
  its `deferred` row as `not read`, by the owner's decision. And
  `evals/scripts/replay_targets.py` leaves out every labelled record
  written before the row, listing 13 replay targets where it listed 31.
