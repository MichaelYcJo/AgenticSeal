# 1792473741-dash-shapes-become-field-words — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | a3b95d63 |

## What this phase was asked

`## Not verified` reads the no-change block, `- nothing` with `  why:`, in
place of `none — <why>` (S1 to S4). The block's word, field and reading
move into `unverified_check.py`, and `rule_changes.py` and `settle.py` read
them from there. The working tree refuses the old line at its line, and a
base revision reads it as no rows. `templates/sdd-overview.md`,
`skills/implement/SKILL.md` §4 and `templates/config.md` §*What no row
governs* are rewritten, the fixture lines and `evals/scripts/rule_cases.py`
rewritten, and the five sealer scaffolds regenerated.

The owner's direction for the build: no symbol a reader can trip on as
syntax, no value stated twice, no spelling a near miss could pass, the rule
once. At the phase boundary the repository-wide meta modules, every module
naming a changed document, `bin/rules --check`, `bin/fold-check` and
`bin/settle --released-at HEAD` run beside the touched modules. A pattern
that repeats gets a timing case.

## What this phase found

- **The block is read by the item grammar, so the grammar moved with it.**
  `unverified_check.py` now holds the item line, the field line, the
  four-space continuation and the field checks (`items`, `field_values`),
  beside `NOTHING`, `WHY` and `nothing_block`. `rule_changes.py` keeps only
  its operations (`GRAMMAR`) and the `file` path check. Left in
  `rule_changes.py`, the field line and the continuation would have been
  spelled twice. S4's grep prints two lines, both of `unverified_check.py`.
- **One refusal names the block for both sections:** "a section that holds
  nothing writes the block `- nothing` with `  why: <reason>`". The old
  `## Rule changes` wording named a spec, and one reader cannot word it for
  one section.
- **A near miss is a first line whose letters, after any list marker, open
  with `none` or `nothing` in any case** (`NEAR_NOTHING`). `nonesuch` is not
  one, and is refused as prose, as before. At a base the near miss reads as
  no rows, which is what lets `nothing — x` read there too, as S2 asks,
  although the old reader never read it.
- **The frame counted 9 fixture lines, 4 in
  `tests/test_unverified_rows_close.py`; the module held 3.** The other two
  `none` lines there are `## Fed back into the spec` and a malformed
  fixture, which the reader never reads as the block. 8 lines were
  rewritten.
- **The live count holds at the phase's base.** `bin/unverified-check
  seal/specs/` under the new reader reads 119 overviews, 0 unreadable, exit 0.
- **The timing case has no red run.** With `NEAR_NOTHING` mutated to the
  nested `(?:[-*+\s]+)*(?:none|nothing)\b`, `mutation-check` timed out after
  40 s with no verdict: the case cannot pass under it, but it never failed
  either. Each of the other 15 mutations went red.
- **A case was added for a block after an operation.** No case pinned where
  `rule_changes.py` refuses `- nothing` written after an operation. It is
  now refused at its own line, where it was refused at the first operation's
  before.
