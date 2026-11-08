# Phase 2: 1794142459-parity-reads-original-forward

## What this phase found

**The frame holds for this phase, with one coordinate that does not.**
`frame/design.md` *Grounding* places the response-shape row at line 81 of
`skills/code-review/SKILL.md`, and it stood there at `41f9d662c`. The
section *The table is a floor, not a ceiling* and the stage 1 sentence
the new paragraph names stood as quoted. The *no*, judged against the tree
before the first edit:

- `frame/plan.md` *Phases* row 2's Verified by cell expects its
  `git grep` to print the one rewritten cell. At HEAD it prints five
  lines: the cell at `skills/code-review/SKILL.md:81`, and four lines of
  this work item's own frame that quote the cell as it stood at
  `9e758b0b0`: `frame/design.md:14`, `frame/design.md:40`,
  `frame/design.md:84` and `frame/plan.md:49`, the row that holds the
  pattern. With `-- . ':!seal/threads'` it prints the cell alone
  (executed). This is the same defect phase 1 found in row 1's grep, and
  the fold at `41f9d662c` did not reach row 2. Folding it is the
  orchestrator's; this phase leaves the frame's lines as they are.

**Where the paragraph stands.** *Scope* item 5 puts it under the table,
before *The table is a floor, not a ceiling*. It stands after the two
sentences on the table's last two rows, which were already there, so
those two sentences stay next to the rows they qualify. Both readings of
the item hold for that place.

**What the paragraph names, and why.**

- The party is the proofer, as in phase 1's paragraph of *Parity review*.
  The grounds are `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는
  글은 한 가지로만 읽히게 쓴다*, which asks each instruction to name who
  acts. `skills/code-review/SKILL.md` already names the proofer as the
  reader of the frame at stage 1 (line 55).
- The reference in a repository without an original is "the work item's
  `frame/design.md`", where *Scope* item 5 writes "the design". The file
  names the path where it means that file (line 56), and the table's rows
  use "the design" next to "the policy". The path keeps the paragraph
  from reading as either.
- The cell and the paragraph both say "walked", the word of *Scope* item
  5's cell, of the same file's "Walk them like the rest", and of phase 1's
  *Parity review* paragraph. One act has one word.

**No case and no mutation run, by the frame's choice.** The scenario *The
greenfield response shape is walked forward* is verified by `read`. The
docstring of `tests/text/test_review_axes.py` says why the axes stand
under no case: a table pinned by its row labels turned red at a rewording
and said nothing about whether a round walked an axis. A case on the
direction would pin the paragraph's wording, which
`docs/running/what-a-script-gates.md` *The checks* refuses, so none was
written. The paragraph carries no `check:` line, as
`skills/implement/SKILL.md` *2. Implement test-first, and let each rule
name its test* asks of a rule no case can hold, and review reads it. No
`seal mutate` run was made: no case covers the paragraph, so a broken
paragraph stays green, which is the fact the frame accepted.

**What can fail for this change.** It is prose, the first row of
`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*. Three readers open the file: `tests/behaviour/test_docs_line_wrap.py`
lists it in `COVERED` at line 136, so the new lines are held to 88
display columns; `tests/behaviour/test_a_cited_section_stands_in_its_file.py`
resolves the new citation of `skills/legacy-parity/SKILL.md` *Parity
review*; and `seal rules --check` reads the file's check lines, which
this phase left as they were (exit 0, executed).

**The fragment.** `changelog.md` opens with `### Fixed`, the heading for
the `fix:` prefix that `frame/design.md` *Grounding* argues, as earlier
`fix:` fragments do (`a3f45e587`, `0fc878f0a`). It states phase 1's
change and this phase's, each with the issue's number. Its
`### Process changes` table has one row, because the range changes
`agents/framer.md` and `agents/tracer.md`, which
`docs/layout/the-record-layout.md` *A change writes fragments, never a
shared file* names. The table has the heading, the header row and the
four cells `templates/records/process.md` gives (read). The commit adds
no version move: `frame/plan.md` *Operational impact* leaves
`.claude-plugin/plugin.json` at 0.35.0.

**Other statements of the reworded cell across the tree.** `git grep`
over the whole tree on the cell's words, "dedup basis",
"included/excluded" and "response shape", finds the cell alone outside
`seal/threads/`; `docs/layout/the-pact.md` uses "response shape" for a
contract between repositories, not for the axis (executed). A wider
`git grep -i` on "axes" and "axis" over `agents`, `skills/code-review`,
`docs`, `templates` and `evals` finds no second statement of the
response-shape row (executed). Both lists are a sample: the class is
every sentence of the tree that says how a review reads a response's
fields, in any words, and no search for words makes that list whole. The
part not reached is a sentence that states the direction in words none
of these searches holds; this phase read whole only
`skills/code-review/SKILL.md` *Comparison axes* and *Two stages, in
order*.

**The phase's scoped run.** One command over the phase's 82 test modules,
`bin/test <82 modules> -q`. The plan row's three modules are among them.
The other 79 are every module under `tests/` whose source names a path
this phase changed (`code-review`, `changelog`, `gaps.md`, `plan.md`,
`phase-`, `threads`, `process.md`, `test_review_axes`), or that lists or
walks the tree (`ls-files`, `os.walk`, `glob(`, `rglob`, `listdir`). The
list comes from one `grep -rlE` over the `test_*.py` files of `tests/`.
The census runs through `tests/test_censuses.py`, which is among them.
It ran over `5eb02256a` with this record, `gaps.md` and the Status cell
in the working tree, and gave 4662 passed and 9 skipped, exit 0
(executed). The words "by default" went into the fragment's second item
while that run was going, so the 16 modules of the 82 whose source names
`changelog`, `tests/test_censuses.py` among them, ran once more over the
tree the records commit holds, less this sentence: 889 passed, exit 0
(executed). Row 2's three modules gave 118 passed, exit
0, over `5eb02256a` (executed).
