# Phase 2: 1794401941-payload-calibration-reached-by-tests-alone

## What this phase found

**The frame holds against the tree at `8215135a9` for *Scope* items 8 to
12, and its `## Removes` misses one case and one sentence.** Each
coordinate those items and `## Removes` name stood where they say (read).
`git grep -n -w` on the five names outside `seal/threads` found them only
at the places G8 lists (executed). Each colour constant `DISC_COLOURS`
listed is still read by the stamp's letter map, `KEY`, at
`skills/verify/scripts/seal_stamp.py:144-158` after the cut (executed:
`grep -n -w` per constant). `PARITY_CONFIG` is read by
`chain_check.py#originals_of` at `:1640` and by `seal.py#mode_report` at
`:2207`, so the comment above it names
`chain_check.py` and `seal mode` (read).

**The case that pinned the rider goes with the rider.**
`tests/text/test_a_rider_reaches_its_file.py::test_the_riders_exist_where_the_rows_said_they_would`
asserted that `lib/optin.py` holds a `# RIDER:` line, and `lib/optin.py`
was the only file in its tuple. *Scope* item 10 deletes that rider as
spent, and the first boundary run at `da714c4d5` failed on this case alone
(executed: 1 failed, 3,913 passed). The case's own docstring records how
each earlier file left the tuple with its rider (#1049, #1376). With the
last file gone, the loop would assert nothing, so the case goes in
`ad8a55543`. The file's other three cases read `seal/follow-up.md` and
stay. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept
against*: the same change removes what stood on the old fact, a case among
it. `## Removes` does not name this case.

**One sentence of `tests/lib/test_optin.py`'s module docstring goes with
*Test_parity_config*.** "The migration config is `seal/parity.json` and
only that." described what that class held, and no case left in the file
holds it. `## Removes` does not name the sentence. The rule it echoed is
still held, because `chain_check.py` and `seal mode` read the
`PARITY_CONFIG` constant. Judged against the same section of
`skills/core/SKILL.md`.

**`strip_ansi` in the test file is written over the file's own `SGR`
pattern, not with the shipped body's literal.** *Scope* item 12 asks for
"the same name and body". `tests/skills/test_seal_stamp.py:43` already
compiles `\x1b\[[0-9;]*m` as `SGR`, the pattern the shipped body wrote
out. So the helper returns `SGR.sub("", s)`, which strips the same codes,
and the file states the pattern once. Judged against `skills/core/SKILL.md`
*The rule a mechanism is kept against*: a fact has one source. The move
adds no behaviour, so no case was written for it. The two cases that call
the helper were shown to depend on it: `seal mutate` replaced its body
with `return s`, and both
`Test_compose::test_accepts_the_owners_reference_cell_for_cell` and
`Test_stamp::test_accepts_a_value_as_wide_as_the_panel_at_eighty_columns`
failed (executed, verdict `red`, `git status` clean after the restore).

**The other four units are only removed, so no case was written new for
them and no `seal mutate` run was owed** (`skills/verify/SKILL.md` *The
narrow command still has to be able to fail*). `git grep -w` finds no
reference to any of them, and the boundary run loads each changed module.

**Three sentences near the removed units stay, each judged true at HEAD.**
The `fence_spans` docstring keeps **An unclosed block is reported, not
decided.** It states the rule `docs/checks/the-fold.md` gives a reader of
an unclosed block, and does not name `closed_fence_lines`. The
`home_at` docstring keeps the sentence saying the opt-out is read once
and the migration config sits inside the root it takes back. It names no
removed unit, and `PARITY_CONFIG` still names a file under the root. The comment above the colour constants keeps "every cell
of the disc is exactly one of these fifteen". "These fifteen" names the
constants, which all stay.

**The scenarios, as run.** S4: in a `git clone --no-local` of
`ad8a55543` under this phase's scratch directory,
`uvx vulture --min-confidence 60 agents bin evals hooks lib skills .github`
exited 3 with 20 lines, none naming the five (executed; G8 counted 25 at
the base). `git grep -n -w` in that clone found `stray_rounds`,
`DISC_COLOURS`, `parity_config` and `closed_fence_lines` nowhere outside
`seal/threads`, and `strip_ansi` only at
`tests/skills/test_seal_stamp.py:275`, `:821` and `:862` (executed). S6:
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` passed in the
boundary run (executed).

**The boundary set was the plan row's five files, the module test files
that name a changed module, and `tests/text` and `tests/behaviour`.** The
module files are the ones a `git grep -l` on `optin`, `routing`,
`lines.py` and `seal_stamp` lists outside the two tree-wide directories,
less `tests/censuses.py` and `tests/conftest.py`, which hold no cases. The
run at `ad8a55543` passed, 3,913 passed and 9 skipped (executed). A test
file that reaches a changed module only through a script it runs is not in
the set; `gaps.md` names the broad gate as its answerer.
