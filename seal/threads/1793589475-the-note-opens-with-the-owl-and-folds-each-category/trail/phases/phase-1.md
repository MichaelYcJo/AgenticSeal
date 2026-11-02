# Phase 1: 1793589475-the-note-opens-with-the-owl-and-folds-each-category

## What this phase found

### The frame, checked before the build

The frame holds for phase 1. Every coordinate that `frame/design.md` and
`frame/plan.md` give for this phase was opened at `06f006898` and stood as
stated (read). `release_body` is at `.github/scripts/publish_release_note.py:651-709`.
The `### <heading>` line over each type is at `:684-687`. The full-changelog
fold at `:702-708` already has the shape *Scope* item 5 asks of every fold.
`TYPES` and `OTHER` are at `:453-465`, and the module docstring states the
type headings at `:35-41`.

### What the renderer writes now

Each type with pull requests is a `<details>` element in place of its
`### <heading>` line. The `<summary>` is the type's name as `TYPES` or `OTHER`
spells it, a space, and the number of its pull requests in parentheses. A
blank line follows the summary line, and another comes before `</details>`.
One blank line parts two folds. The order of the types, the pull request
lines, the glance, the thanks section, the update section and the
full-changelog fold are unchanged. Phase 2 owns the glance.

The parts of *Scope* item 6 that state the folds were rewritten in the same
commit. They are the module docstring's sentence on the summary, the comment
over `TYPES`, and `release_body`'s docstring. The docstring now carries the
limit sentence of *Scope* item 5, with the framer's count of 0 in 318 merged
titles (`frame/design.md` *Grounding*, read and not re-counted). The test
module's own docstring states A5 with the folds.

### The cases, and how each was shown red

Two cases hold S1, both in `tests/github/test_publish_release_note.py#Test_main`.

1. `test_each_type_is_a_fold_under_its_name_and_count` replaces
   `test_every_change_is_one_line_under_its_type`, which pinned the headings.
   It asserts the folds' exact text, in order, and that no `### ` line names a
   type. It keeps the old case's check that a keyword in a code span closes
   nothing.
2. `test_github_reads_each_fold_as_one_element_holding_its_lines` renders the
   note with `cmarkgfm`, the renderer the suite pins, and reads each `details`
   element back as its summary and its list items. A title that quotes
   `</details>` in a code span is among the pull requests. The case asserts
   that the title's line stays in its own fold.

Both ran red against the renderer at `06f006898`, with the new cases in the
working tree and the renderer not yet edited (executed, exit 1). The first
failed at its fold-text assertion. The second read only the full-changelog
fold.

After the commit, `seal mutate` ran four mutants of the fold, one command
each, all `red` (executed, exit 0 each):

| Mutant | Case run | Failing line |
|---|---|---|
| the blank line after the summary line removed | the render case alone | `assert folds_read(body) == ...`: the Features fold read with no list items, because its lines became raw HTML |
| the count read as every pull request in the release | the text case | `assert f"\n\n{folds}\n\n" in body` |
| the blank line before `</details>` removed | the text case | the same line |
| the blank line before `<details>` removed | the text case | the same line |

The render case was not run against the last two mutants. The text case is
what holds those two blank lines.

### Decision: the render case reads `cmarkgfm` directly, not `tests/gfm_table_oracle.py`

S1 asks for the note as the pinned renderer reads it. The oracle renders with
raw HTML left out, and its docstring gives the reason. A `details` tag would
come back as an omitted-HTML comment, and the oracle reads only tables. The
case therefore calls `cmarkgfm.github_flavored_markdown_to_html` with
`Options.CMARK_OPT_UNSAFE`, which keeps raw HTML as a GitHub release note
does. The framer's probe of GitHub's own renderer showed the same result
(`frame/design.md` *Grounding*). A small `html.parser` reader beside the
case collects each element. Judged against `frame/design.md` S1 and
`.github/scripts/run_tests.py#CMARKGFM`.

The module now imports `cmarkgfm` at its top. Every run that collects it
installs the package (read): `bin/test` through `run_tests.py#PACKAGES`,
`.github/workflows/test.yml:149`, and the `seal` job at
`.github/workflows/publish-release.yml:126`. The one job that installs pytest
alone runs `tests/skills/test_arm_check.py` only.

### Pins the frame did not list for phase 1

The `### ` line after the glance moved, so five pins that read it changed in
this commit. `frame/design.md` *Removes* lists four of them for phase 2's
rewrite, and phase 1 edited each only as far as the moved line requires.

- `tests/github/test_publish_release_note.py#Test_main::test_the_glance_counts_the_release`
  now cuts the glance at the first `<details>`.
- `#Test_module::test_the_glance_block_is_built_by_one_function_and_its_sealed_twin_by_another`
  now expects the glance followed by the Features fold, built by the module's
  `fold` helper from `FOLDED`.
- `#Test_main::test_the_fragments_are_kept_folded_under_the_summary` found
  the full-changelog fold by the first `<details>`, which is now a category's.
  It now finds the fold by its own summary line. *Removes* does not list
  this case. It is an adjustment and not a removal.
- `tests/github/test_release_seal.py#Test_main::test_accepts_a_published_note_and_replaces_its_glance_table`
  (`:661`) now expects the Features fold after the sealed block.
- The same module's case `the glance table is there twice` (`:738`) now
  splits the note at the first `<details>`.

### What phase 2 needs

`FOLDED` and `fold` in `tests/github/test_publish_release_note.py` hold the
fixture release's folds, and the header cases can reuse them. The module
docstring's sentence "after the theme the note says ... a count" still puts
the count after the theme. Phase 2 rewrites it with the header.

### The phase-boundary run

`bin/test tests/github/test_publish_release_note.py tests/github/test_release_seal.py tests/skills/test_settle.py tests/behaviour/test_a_release_publishes_its_note.py tests/test_censuses.py`
passed with 412 cases (executed, exit 0). The fifth module is the
real-identifier census, which the spawn asked for. `bin/seal layout --check tests`
refused nothing (executed, exit 0), and `bin/seal layout --pairs` named no
pair in the changed module (executed, exit 0). `uvx ruff check` and
`uvx ruff format --check` passed on the three changed Python files (executed,
exit 0 each).
