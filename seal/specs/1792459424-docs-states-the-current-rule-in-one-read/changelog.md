### Changed

- **A rule names what reads it on one `check:` line (#941).** The line names
  repository files, eval case directories `evals/behaviour/<agent>/<case>/`,
  or a marker its tests carry as `@pytest.mark.rule("<marker>")`, separated
  by single spaces; a rule nothing can hold writes
  `check: none reader: <who reads it>`. The grammar is
  `skills/settle/SKILL.md` *A rule has one shape*. `rules --check` refuses
  every other spelling at its line, exit 1, naming the spelling it expected:
  `Enforced by:`, another case, a bullet or emphasis in front, a space before
  the colon, and a value holding `::`, a comma or an em dash. A consuming
  repository's `Enforced by:` lines are refused until rewritten. `rules
  <doc>` prints each target's module docstring, or for a marker each test
  carrying it.
- **`fold-check` no longer reads a rule's shape (#941).** The `Fold shape
  from` row is read by nothing and `--shape-from` is gone; a script that
  passes it gets an argument error, exit 2. `fold-check` holds the policy
  root to one read and one index.
