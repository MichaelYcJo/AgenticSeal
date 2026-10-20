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
- **A spec that changes or removes nothing writes the no-change block
  (#941).** In `## Rule changes` and `## Removes`, `- nothing` with its one
  field `why:` replaces `nothing — <why>`. `settle` refuses every other
  spelling of a no-change line at its line, naming the block, and the block
  stands alone in its section.
- **Every policy document under `docs/` states the current rule once
  (#941).** Each keeps its rules, their grounds and their `check:` lines, and
  drops the history, the issue numbers, the section signs and the readers'
  mechanics, which the cases named on those lines hold. Every document fits
  one read, so none is split. `docs/one-root-by-lifetime.md` and its Korean
  edition are no longer the 0.4.0 design record: both state what still rules,
  the root, the dependency rule, the opt-in, first setup, naming and the
  config rows, and its six dated decision sections are gone. Headings that
  carried a dash, a middle dot, a pipe or an issue number are renamed:
  *Registration*, *The PreToolUse reading of a commit*, *Which repository*,
  *The implementer mark and notice*, *The commit gate inside git*, *Review
  arm*, *Parity arm*, *Creation consent*, *Decided before git runs*,
  *Declared work streams*, *Which tree*, *2b. Settle what earlier releases
  left behind*, *3. Verify before committing* and *The opt-in signal is the
  root itself*.
- **`fold-check` no longer reads a rule's shape (#941).** The `Fold shape
  from` row is read by nothing and `--shape-from` is gone; a script that
  passes it gets an argument error, exit 2. `fold-check` holds the policy
  root to one read and one index.
