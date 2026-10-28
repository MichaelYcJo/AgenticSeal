# Phase 2: 1793152332-the-stamps-mark-is-an-owl

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 5e70612d |

## What this phase was asked

Build `frame/plan.md` row 2 and nothing of phases 3 and 4.
`skills/verify/scripts/seal-mark.txt` becomes the owl's sprite. `read_sprite`
and the `SPRITE_*` names replace `read_chart` and the `CHART` names.
`seal_stamp.py#build` draws each sprite letter in its colour, puts the drop
shadow on a field cell whose upper-left neighbour is drawn, and no longer
shades by neighbour. The letter twin keeps `KEY`. In
`tests/skills/test_seal_stamp.py` the reference picture and the frame counts
move to the sprite, and the S's hash case and `Test_read_chart` go. The owl
must match the owner's `owl-28-pixel.ans` cell for cell except at the
shadow. The stamp with its label must fit `MESSAGE_BUDGET`. Only the new
behaviour owes a red run, nothing runs `seal mutate`, and one `bin/test`
command closes the phase.

## What this phase found

**The frame holds.** The sprite file is byte for byte the candidate
`owl-28-pixel.txt` at `c8bb9693` (`cmp`, executed). At an offset of six cells
every drawn cell and every shadow cell lies inside the field, and the shipped
sprite passes `read_sprite`. Every letter's colour is one of the nine, so
`KEY` and the twin did not change.

**The shadow against the candidate.** The candidate's field was transcribed
from its SGR stream at `c8bb9693` by a script that read no line of
`seal_stamp.py`. Of the 300 field cells, 275 are the colour `build` draws. The
other 25 are the shadow: the candidate paints them (78, 8, 12), and `build`
paints them `DROP`, (84, 8, 12). That is every shadow cell and nothing else,
so the shadow differs in colour only, not in where it falls. `DROP` is used
because `frame/questions.md` settles it from the tree: the owner's brief says
every colour is one of the stamp's existing reds, and (78, 8, 12) is not one.
The candidate's frame also differs from `build`'s in its outer half-rows. The
reference keeps the settled frame and takes only the field from the
candidate.

**The message budget.** The owl's block over the widest reference panel,
with its label, is 5,959 UTF-16 units. The same block with the placeholder S
at `39582907` is 5,258 units. `MESSAGE_BUDGET` is 9,000. The case that
bounded the size at 5,500 now reads its bound from `MESSAGE_BUDGET`, and its
docstring states both measured figures.

**How `read_sprite` orders its faults.** `read_chart` checked each line's
shape and its field in one pass. A shadow check on line N reads line N + 1,
which that pass has not yet checked for shape. So `read_sprite` checks the
shape of every line first: the count of lines, then each line's length and
characters. Only then does it check the field. A drawn cell outside the field
is reported before the shadow it would cast.

**The new cases, and how each was seen red.** Each ran once against
`39582907`, with the cases written and the module and the sprite file not yet
changed:

- `Test_read_sprite::test_accepts_the_shipped_sprite_and_a_copy_saved_with_a_byte_order_mark`
  and the five parameters of
  `Test_read_sprite::test_refuses_a_sprite_of_another_shape_naming_the_fault`
  (`short`, `wide`, `stray`, `on-the-rim`, `its-shadow-on-the-rim`; S3) each
  failed with `AttributeError: module 'seal_stamp_under_test' has no
  attribute 'SPRITE'`.
- `Test_build::test_accepts_every_cell_by_the_owners_rule_in_the_frames_counts`
  (S1), rebuilt from the sprite with the letter table `OWL_LETTERS` written
  in the test, failed the same way.
- `Test_compose::test_accepts_the_owners_reference_cell_for_cell` (S2),
  with `REFERENCE_DISC` and `REFERENCE_TWIN` transcribed from the candidate
  for the field and from the earlier reference for the frame, failed at the
  twin's fourth line: the module drew the S's
  `  mmMMNN............NMnnmm` where the owl's reference has
  `  mmMMNNx..........xNMnnmm`.

**Existing cases relied on, renamed or rewritten without a red run.**
`Test_disc_cells` and `Test_compose::test_accepts_the_disc_left_of_the_text_each_centred`
now read `stamp.SPRITE`. `Test_stamp`'s size case is renamed
`test_accepts_the_widest_reference_panel_with_its_label_in_one_message`,
and its bound is `MESSAGE_BUDGET`. `Test_stamp`'s twin footprint case now
draws `REFERENCE_ROWS` with a row carrying `→`, in place of the removed
`SAMPLE_AT_5623D728`.
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py` pins the new
docstring sentence `a 16 x 16 sprite in seal-mark.txt beside this file, read
as data`. `tests/skills/test_broad_gate.py`'s case that writes a raising
`seal_stamp.py` (S4) is unchanged.

**Removed.** `Test_read_chart`, the hash half of the old
`test_accepts_the_drawing_byte_for_byte_as_it_was_before_the_scale_left`,
`SAMPLE_AT_5623D728`, `DRAWN_AT_5623D728`, the `hashlib` import, and the
neighbour rule in `owners_disc`.

**What else stated the old fact.** `git grep` for `chart`, `placeholder S`,
`SAMPLE_AT` and `DRAWN_AT` outside `seal/`, `changelog/`, `CHANGELOG.md` and
`.test_durations` finds three places beyond this commit:

- `assets/seals/README.md` still says `read_chart` reads `seal-mark.txt`, and
  it still treats the S as the stamp's mark and the owl as a candidate. Row 4
  rewrites that README, so the sentences stay until phase 4.
- `seal_stamp.py`'s comment on the retired scale names the lily's chart of
  #30's time. That sentence is history of the scale, and it is still true.
- `tests/skills/test_broad_gate.py` raises `ValueError('the chart is ...')`
  from a stand-in module. That text is a fixture's own sentence, not a claim
  about the stamp, and S4 keeps the case unchanged.

`.test_durations` still lists the removed cases' keys. The plan's
*Operational impact* leaves that to the orchestrator's broad run.

**The stamp, drawn by its path.** `bin/seal stamp --shape` printed the owl in
the twin's letters (executed, read). `bin/seal stamp` ran under `script` in a
UTF-8 pseudo-terminal. Its stream was transcribed and drawn to an image
beside the candidate's, and the two read as the same owl on their two frames
(executed, read). The stream holds only the nine colours, with 25 `DROP`
cells.

**The run.** One `bin/test` command ran the row's named modules and every
test module that `git grep -l -e seal_stamp -e seal-mark -e broad_gate --
tests` lists, 31 modules in all. It exited 0 with 2,354 passed and 9
skipped. `uvx ruff check` and `uvx ruff format --check` passed over the four
Python files the commit changes.
