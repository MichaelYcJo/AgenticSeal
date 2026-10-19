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
  an open row, and two that merge order cannot decide at one place are
  refused at their line and stay. `settle` with no flag is the dry run.

  `settle --retire` and `settle --retire-process` are gone, and a script that
  calls either gets an argument error, exit 2. A spec with no
  `## Rule changes` section was written before it existed: `settle` names it
  and keeps it.

- **The CI readers tell a settle from a deletion without a marker (#953).**
  `unverified-check --baseline` and `chain-check` accept a directory removed
  whole when, at the merge base, nothing in its record is open and either it
  states no rule (no `spec.md`, or a spec with no `## Rule changes`) or its
  rule changes, replayed over the base's `docs/` in merge order, are what
  `docs/` holds. A `<!-- specs/<id> -->` marker no longer excuses a removal.
  `unverified-check` names such a directory `settled`, where it said
  `folded` or `retired by the rule`.
