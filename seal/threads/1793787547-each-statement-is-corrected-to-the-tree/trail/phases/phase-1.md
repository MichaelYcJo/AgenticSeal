# Phase 1: 1793787547-each-statement-is-corrected-to-the-tree

## What this phase found

**The frame holds for this phase.** I checked it against the tree at
`479c2f21e` before the first edit (read, unless marked).

- `templates/setup/seal-README.md:85-90` and `seal/README.md:85-90` held the
  entry *Scope* S1 quotes, and the two files were byte-identical (executed:
  `cmp`, exit 0). The entry was each file's only mention of `Record
  language` (executed: `git grep -n`).
- `templates/setup/config.md` documents the ten items that
  `skills/config/SKILL.md:38` tables. Its paragraph on absent rows names
  `Mode` and `Broad gate` as the two exceptions, which contradicts the old
  entry's "no file and no row both mean the default" for `Broad gate`.
- `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:44-45`
  held the comment S2 quotes. No shipped Python, shell or YAML file spells
  `Commit and pull request language`: the only files are four test modules,
  `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`,
  `tests/conftest.py`, `tests/hooks/test_config.py` and
  `tests/text/test_the_settings_have_a_front_door.py` (executed: `git grep
  -ln` over `*.py`, `*.sh` and `*.yml`). So no shipped script
  asks `hooks/lib/config.py` for this row by its name. That module's one
  mention of the row is a comparison in the `declared_mode` docstring
  (`hooks/lib/config.py:557`).
- The README's other readers that the design names assert none of the
  entry's words: `test_first_setup_asks_once.py` (the byte equality, both
  places, the marker, the drain citation),
  `test_the_set_a_work_item_always_has.py` (the `follow-up.md` tree line),
  and `test_the_pull_request_language_is_the_repositorys.py#test_the_layout_lists_the_config`,
  which asserts only that `config.md` is named.

**The entry's words.** Both copies now read: "what this repository says
about itself, one row per item. `templates/setup/config.md` in the plugin
documents every item and what an absent row means". The entry follows the
head comment of `seal/config.md:3-5`, as S1 asks, and it keeps the tree's
24-column indent. It lists no item and makes no claim about an absent row.
Grounds: `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A
fact has one source, and every other place links to it", and
`frame/plan.md` *Alternatives considered* A1.

**The comment's words.** At `707d356d5` the comment read "The row's item,
which a session looks for in the file because the skill tells it to. No
script reads this row." Reading the range whole, I found that "No script"
can be read against this module's own cases. `#configured_language`'s loop
parses the row through `hooks/lib/config.py#config_rows`, which the module
loads as `items`. `8c8c8a24f` rewrites the comment: "The row's item. A session
looks for it in the file because the skill tells it to. No hook or command
of the plugin asks for this row; the cases of this file parse it through
`hooks/lib/config.py#config_rows`." The assert below it is unchanged, and
the module passes, 93 cases (executed: `bin/test ... -q -p no:xdist`, exit
0, with `uvx ruff check` and `uvx ruff format --check` exit 0).

**The `ROW_READERS` entry went in the same commit as the README edit.** The
README no longer names a language row, so the parametrised case
`test_every_document_that_names_a_language_row_names_the_shipped_one`
would fail on it (`frame/design.md` *Removes*, second row). I showed this
after the commit with `seal mutate`. It put the entry back into
`ROW_READERS` and ran the case under `-k`, and the
`templates/setup/seal-README.md` case failed: "templates/setup/seal-README.md
does not name `Record language`" (executed: verdict `red`, exit 1 from the
cases, and the tree clean after the restore).

**Seen red and mutation.** No unit adds behaviour in this phase. The README
entry is the *Prose only* row of `skills/verify/SKILL.md` *The narrow
command still has to be able to fail*, the comment is the *A comment or
docstring inside source* row, and the `ROW_READERS` change removes one
parameter. So no case was written new, and no `seal mutate` run is owed.
The one `seal mutate` run above shows that the removal was needed. It does
not prove a new case.

**The census of `config.md`'s items, re-run at `707d356d5`.** I re-ran the
design's *Grounding* probe as a script in the session's scratch directory,
not in the tree. It lists each paragraph of the tracked `*.md`, `*.py`,
`*.yml` and `*.sh` files outside `seal/threads/` and `evals/behaviour/`
that names three or more of the ten items in backticks. At `479c2f21e` it
listed the five paragraphs the design gives. At `707d356d5` it lists three
(executed):

- `skills/config/SKILL.md:38` tables all ten items with their defaults, and
  agrees with the template.
- `skills/config/SKILL.md:130` names the two fold rows that
  `templates/setup/config.md` *The fold's values* gives.
- `tests/skills/test_fold_check.py:220` says the template writes `Mode` and
  `Broad gate` as rows with an empty cell, and `templates/setup/config.md:75-76`
  does.

Each one holds. Two more searches went beyond the probe:

- `git grep -ln 'Commit and pull request language'` over Python found
  `tests/text/test_the_settings_have_a_front_door.py`. Its `ROWS` lists all
  ten items. Its docstring's first paragraph says "Issue #105. Three rows
  exist", and `gaps.md` *Not done* gives why that sentence stays.
- `git grep -i -E` for a number followed by `rows`, over `*.md` and `*.py`
  outside the records, found no count of `config.md`'s rows (executed).

The list is a sample, because the class is a kind of claim and these
searches match spellings. `gaps.md` *Not verified* says where the part the
searches did not reach stands.

**Other places that state the two corrected claims, a sample.** `git grep
-n -i -E 'no file and no row|both mean the default|and .Mode. has none'`
outside `seal/threads/` prints nothing at `707d356d5`. `git grep -n -E`
for `config.py` followed by "reads" or "read by", outside the records,
found no other sentence that says `hooks/lib/config.py` reads a language
row (executed). Neither corrected statement carries a `check:` line.

**Narrow run.** I ran the seven modules of the plan row's *Verified by*
cell in one `bin/test ... -q` over the tree `707d356d5` commits, before
the commit: 269 passed (executed, exit 0). `uvx ruff check` and `uvx ruff format
--check` on the changed test module exited 0 (executed).

**Phase boundary run.** This is the *Phase boundary* row of
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, run as
one `bin/test ... -q`. The first two runs were over 42 modules: the plan
row's seven and every module under `tests/` that walks files (`ls-files`,
`glob`, `rglob`, `os.walk`) and names `.md` or `templates` (executed: `git
grep -l` and `grep`). The first run at `707d356d5` had one failure:
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
because this work item had a frame and no `gaps.md` yet. The second run,
over `707d356d5` with this record, `gaps.md` and the Status cell in the
working tree, gave 2489 passed and 9 skipped (executed, exit 0). The third
run added `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`,
which reads the phase records, for 43 modules. It ran over `8c8c8a24f`
with this record's last edits in the working tree, and gave 2499 passed
and 9 skipped (executed, exit 0). The selection is my reading of "a
module that reads a path the phase changed".
A module that reads those files through a helper these searches do not
name is outside it, and the broad run covers that.

**For the next phases.** `test_chain_hooks_hardening.py`'s memo case is
green from here on, since `gaps.md` exists. Phases 2 to 4 add their rows to
`gaps.md`.
