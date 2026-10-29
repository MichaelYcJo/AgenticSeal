# Phase 2: 1793251202-the-citation-case-misses-files-and-wrapped-comments

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 37434c86 |

## What this phase was asked

Build `plan.md` row 2. One corpus function in
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` holds the
`ls-files` call, and `citations(root)` and the contract-rule reader both
read through it. `cited_sections` and `near_citations` read
`flowing(rel, text)`. `tree_files`, `CITED_TREES` and `CITED_FILES` go. New
cases cover S3 to S7, the module docstring states S8, and the registry row
in `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` names the
scope that holds the listing. Each new case of S3, S5, S6 and S7 is shown
red first against phase 1's commit, with the corpus function replaced by the
old walk over the fixture root and `flowing` left out of the two readers,
then green against this phase's code. Then run phase 1's command.

## What this phase found

The frame held. The tree at this phase's head reads as the frame's probes
said it would at the base: `corpus(ROOT)` lists 912 tracked paths and reads
325 files, and the contract-rule reader recognises 232 citations over them,
with none dangling and no near miss (executed, through the module's own
functions in one `python -c`). The four paths more than the frame's 908 are
this work item's own records under `seal/threads/`, which the corpus leaves
out.

**Three choices differ from the plan's wording.**

- The contract-rule reader does not take a root. `contract_dangling` still
  takes `[(rel, text)]` and the section numbers, and each case that reads a
  tree passes `corpus(root)[1]`, so fixture trees are read as the plan
  asked. The tree case needs the file list as well as the dangling list,
  for its two floors, so a reader taking a root would have meant a second
  listing or a second return value. The seven moved fixture cases keep
  their in-memory `(rel, text)` pairs and build no repository.
- S4 is not a case of its own. The crafter rule *A new test starts from its
  group* sends it to `test_a_record_is_not_read`, which already builds a
  fixture under each prefix of `RECORDS` beside an `a.md`. That case now
  puts `contract rule N` in both files and asserts that only `a.md:2` is
  named, beside its section-citation assertion.
- The indented `.yml` fixture of S5 is `hooks/x.yml`, a path the frame did
  not name. The old walk skipped every `.yml` file, so copy A below cannot
  tell its red from reach; copy B shows the red comes from `flowing`.

**The red-first runs** used two scratch copies of phase 1's tree,
`git archive 97052b16`, each with this phase's module copied in and edited.
The new cases are byte for byte the committed ones. Each copy ran under the
worktree's `.venv` with
`python -m pytest tests/behaviour/test_a_cited_section_stands_in_its_file.py -k "outside_the_six_trees or wrapped_in_code or wrapped_across_comment_markers or record_is_not_read" -p no:xdist -p no:cacheprovider -q -rA`
(executed).

- Copy A is the plan's harness. `corpus` walks the six trees, the five
  extensions and `CONTRIBUTING.md` under the fixture root, and both readers
  read the raw text. Exit 1, 7 failed. S3 failed with
  `assert [] == [('.github/wo...', 'rule 21')]`, so none of the four files
  was named. The three S5 and S6 ids failed with `assert [] == [('hooks/x.py:1', 'rule 21')]`
  and its siblings, and S7 with `assert [] == [1]`. The two ids of
  `test_a_record_is_not_read` also failed, at the section-citation
  assertion (`Found(read=0, ...)` against `Found(read=1, ...)`). That red
  is the harness's: copy A's `corpus` feeds `citations()` as well, and the
  old walk does not read a top-level `a.md`. The plan's *S4 passes on both
  sides* assumed a separate case.
- Copy B keeps this phase's `corpus` and leaves only `flowing` out of the
  two readers. Exit 1, 4 failed, 3 passed. The three S5 and S6 ids and S7
  failed as in copy A, and S3 and both record ids passed. So the S5, S6 and
  S7 reds come from `flowing` alone, and the S3 red from the corpus alone.

The same cases ran green at this phase's code: `bin/test` on the module
with that `-k`, `-p no:xdist` and `-rA` passed 13 of 13, exit 0
(executed).

**`seal mutate`**, one run per unit this phase adds, after the commit, with
`--tests "bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -k <cases>"`
(executed; each printed `red`, exit 0, and `git status` was clean after the
five):

| Unit | Mutation | Cases | Result |
|---|---|---|---|
| `cited_sections` reads `flowing` | `flow = flowing(rel, text)` to `flow = text` | `wrapped_in_code` | 3 failed |
| `near_citations` reads `flowing` | the same, in `near_citations` | `wrapped_across_comment_markers` | 1 failed |
| `corpus` leaves the records out | the `RECORDS` filter dropped | `record_is_not_read` | 2 failed |
| `corpus` reads every extension | only `.md` kept | `outside_the_six_trees` | 1 failed |
| `corpus` drops a file that is not UTF-8 | `if text is not None` dropped | the two tree cases | 2 failed, `TypeError` on a `None` text |

The last unit has no fixture case. The tree's own nine `.png` files are what
kill it, through the two cases that read `ROOT`.

**What else the phase run showed** (executed): phase 1's command, the eight
modules with `-q`, passed 337, exit 0. `uvx ruff check` and
`uvx ruff format --check` over the two changed modules: exit 0. A `git grep`
for `tree_files`, `CITED_TREES`, `CITED_FILES` and
`test_a_cited_section_stands_in_its_file.py#citations` outside
`seal/threads/` finds no line of this module or the registry; its two hits
are `chain_check.py`'s unrelated `worktree_files`.

The write hook rewrote S7's `"...{n}".format(n=7)` into an f-string holding
`{7}`. The case now holds the literal `"# per the contract's\n# rule 7\n"`.
In this file's own source the `\n` is two characters, so the near-miss
reader does not match the line when the tree case reads this module.

The five new case ids have no `.test_durations` keys. The plan asked only
for the 15 moved keys, and `test_the_durations_file_prices_the_suite`
allows 5 % of collected cases unpriced (`STALE_SHARE`).
