### Changed

- **`settle --apply` applies each released spec's rule changes to `docs/` in
  place (#953).** A spec states the rules it changes in a `## Rule changes`
  section: an operation line (`- add`, `- change`, `- remove`) and the fields
  `file:`, `section:`, `from:` and `to:`, one per line. The grammar is
  `skills/settle/SKILL.md` §*Rule changes*, and
  `skills/settle/scripts/rule_changes.py` is its one reader. `--apply` works
  in merge order, the later spec winning, and applies a spec whole or not at
  all. It writes no marker, and removes each applied spec's directory whole,
  its process record included. A spec it cannot place, one whose record holds
  an open row, and two that merge order cannot decide at one place (a
  section and a sub-section it holds are one place) are
  refused at their line and stay. So is a `file:` holding `\` or `:`, one
  differing from another document only in case, and a `nothing` line written
  with a hyphen, which is told to use the em dash. `settle` with no flag is
  the dry run.

  `settle --retire` and `settle --retire-process` are gone, and a script that
  calls either gets an argument error, exit 2. A spec with no
  `## Rule changes` section was written before it existed: `settle` names it,
  keeps it, and counts it in its last line.

- **The CI readers tell a settle from a deletion without a marker (#953).**
  `unverified-check --baseline` and `chain-check` accept a directory removed
  whole when, at the merge base, nothing in its record is open and either it
  states no rule (no `spec.md`, or a spec with no `## Rule changes`) or its
  rule changes, replayed over the base's `docs/` in merge order, are what
  `docs/` holds. A `<!-- specs/<id> -->` marker no longer excuses a removal.
  `unverified-check` names such a directory `settled`, where it said
  `folded` or `retired by the rule`.

- **One read is a token row, and a report (#953).** `Document token
  ceiling` replaces `Document line ceiling`, and `Over the ceiling` is no
  longer read. `fold-check` and `settle --apply` name each document whose
  estimate (UTF-8 bytes halved) is past the row as one to split along its own
  headings, and exit 0 on it. A repository that declared a line ceiling has
  no size check until it declares the token row.
- **The policy root is a row, and it has an index (#953).** `Policy root`
  (default `docs`) names the directory `settle --apply` writes and every
  reader of the policy reads; the first `--apply` creates it with an empty
  index. Where `<policy root>/README.md` exists, `fold-check` refuses a
  document no row names, one named on two rows, and a row that names none.
  This repository's index is `docs/README.md`.
- **A pull request does not edit the policy root (#953).** The `implement`
  skill states the model once: the policy root is the baseline, and the
  policy in force is it plus every unsettled spec's rule changes in merge
  order. The framer writes `## Rule changes`, picking each file from the
  index, and nothing gates the rule yet.
