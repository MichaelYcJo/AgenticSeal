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

  | Agent | Preload bytes | Tokens per tool call | Spend USD | Recall | False rate | Verdict |
  |---|---|---|---|---|---|---|
  | warden | 27,173 → 27,168 | 87,862.4 → 85,306.7 | 41.7424 → 39.7893 | 19 → 13 | 0.558 → 0.641 | fail on rules 1 and 2, recorded as noise and shipped by the owner |

  The pair is #967's last warden side, at `af716289`, and this item's, at
  `ba2a3187`, on one suite (`af9c924b`), eighteen runs a side, none cut
  short. Every lost find is in a replay case. The largest loss is both runs
  of one case declining the prompt's wider read under the warden's
  verifying-round rule, which this item did not change. The baseline's 19
  is the highest of six sides measured on this suite. All 39 findings of
  the new side carry an `evidence:` line, 28 of them `executed`.

  A record written before the row lacks the line, and that is no finding.
  The check reads only the records of the work items a pull request
  carries, so no merged record is read again or rewritten. The release
  panel reads every record of a release by this grammar, so v0.22.2's
  panel shows its `deferred` row as `not read`, by the owner's decision.

- **The replay generator reads each record by the grammar of its own time
  (#985).** `evals/scripts/replay_targets.py` judges a labelled record
  through the `chain_check.py` of the commit that last wrote it, with the
  grammar table that commit holds, and reads a record no commit wrote
  through the tree's. So the `evidence:` row does not cost it the rounds
  written before it: `--list` names the same 31 replay targets it named
  before the row.
