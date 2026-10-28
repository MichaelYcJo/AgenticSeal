# Phase 4: 1793152332-the-stamps-mark-is-an-owl

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 0b2e6a53 |

## What this phase was asked

Build `frame/plan.md` row 4, the last phase. Move the owl's SVG to
`assets/seals/owl.svg` with `git mv`, and remove the owl's four candidate
files that `frame/design.md` *Removes* lists. Write the owl's entry in
`assets/seals/`: `owl.ans` and `owl.png` drawn by the README's rule, and a
README section in the shape of each earlier entry. Rewrite every README
sentence the change made untrue: the S as the mark, `read_chart`, the letter
list, which now cites the module, and *The next entry*. Write the work
item's changelog fragment. Answer `frame/questions.md` Q4 by redrawing
`placeholder-s.png` first. Draw any image without adding an imaging library
to the tree. Owe no new case, no red run and no `seal mutate`, and close
with one `bin/test` command.

## What this phase found

**The frame holds.** The four candidate files and the SVG were where *Removes*
says. The tree's `seal_stamp.py` and `seal-mark.txt` were unchanged from
HEAD, so a command reading HEAD draws what the working tree draws.

**Q4: the preview rule reproduces pixel for pixel.** The renderer was a
throwaway script in the session scratchpad, run under `uv run --no-project
--with pillow==12.3.0` with `UV_CACHE_DIR` in the scratchpad, so Pillow came
from an environment outside the tree and nothing was added to its
dependencies. It draws by the README's rule: 12 × 24 cells, a half-block as
its two halves, Menlo at 19 pixels with the anchor at the cell's centre,
xterm's 256-colour table, grey (128, 128, 128) for the default foreground,
Menlo Bold for bold, dim at alpha 128 and green as (0, 205, 0). It redrew
`placeholder-s.png` with 0 differing pixels on its first run. It also redrew
`gold-lily.png`, `red-lily.png` and the three remaining candidate previews,
`section-28.png`, `section-14-light-red.png` and `bee-28-pixel.png`, each
with 0 differing pixels. `owl.png` was then drawn by the same script from
`owl.ans`, 816 × 336 pixels, and read as the owl on the disc beside the
sample panel when opened. The renderer stays in the scratchpad, and the
README now says no script in the tree draws a preview.

**S11: the owl's command draws `owl.ans` byte for byte.** The README's
command names v0.23.1, which is not tagged yet. The command line was taken
from the README as committed, its `v0.23.1:` replaced by `HEAD:`, and run
from the repository's top directory. Its output and `assets/seals/owl.ans`
are equal under `cmp`, 6,199 bytes. *The next entry* now states this
practice: the files are drawn from the commit that writes them, with the
command's tag replaced by that commit.

**What else was untrue in the README, beyond what the row names.**

- The paragraph on the parchment sheet said "All three stand on the
  parchment sheet". After the owl leaves, the candidates are the two
  section signs and the bee, and the bee's `.ans` is a disc alone (its
  preview is 336 × 336). It now names the two section signs.
- `section-28`'s bullet said `read_chart` refuses its chart, and
  `section-14-light-red`'s said `read_chart` refuses it. Both sentences
  were rewritten without the reader.
- The placeholder S's entry said the disc is the same at every tag from
  v0.20.0 to v0.22.1. Drawing the disc at v0.20.0, v0.21.0, v0.22.0, v0.22.1
  and v0.23.0 gave the same half-blocks at each, so it now reads "to
  v0.23.0", and the entry closes at 0.23.0.
- The heading *Candidates for #857* became *Candidates*, because #857 has
  chosen. No file outside `seal/` cites the heading.

**The bee is a sprite the module accepts.** `read_sprite` reads
`candidates/bee-28-pixel.txt` without a fault, so the bee's entry says it
would become the mark by replacing `seal-mark.txt`.

**The owl's SVG paints in seven reds, none of the stamp's nine.** Its seven
fill colours are the ones `frame/questions.md` Q1 lists, and none equals a
`DISC_COLOURS` value. Q1's default ships the SVG unchanged, and the README
states the difference.

**The row's closing grep matches one line.** `git grep -n -e owl-web -e
owl-28-pixel` outside `seal/`, `changelog/` and `CHANGELOG.md` matches
`tests/skills/test_seal_stamp.py` line 128. That comment, written in phase
2, cites the candidate at a commit: `assets/seals/candidates/owl-28-pixel.ans`
at c8bb9693. The citation stays true after the file leaves the tree, because
`git show c8bb9693:<path>` still opens it, and it is the coordinate the
reference case was transcribed from. It was left as it stands.

**The files were placed by `cp`.** `owl.ans` carries escape bytes and
`owl.png` is binary, so both were written in the scratchpad by their
commands and copied into `assets/seals/`. The `cmp` above checks `owl.ans`
after the copy.

**No case was written new, and none was removed.** The phase relied on the
existing cases of the modules below.

**The run.** One `bin/test` command ran 776 cases, and all passed (exit 0).
It covered the row's two modules, `tests/behaviour/test_one_word_one_meaning.py`
and `tests/test_censuses.py`. It covered the modules `git grep -l -e
assets/seals -e candidates -- tests` lists: `test_first_setup_asks_once.py`,
`test_seal_stamp.py` and `test_settle.py`. It covered the modules that read a
changelog fragment or `assets/`: `test_release_hygiene.py`,
`test_the_contributor_has_a_procedure.py`,
`test_the_release_check_watches_what_ships.py`, `test_gather_changelog.py`,
`test_root_migrate.py`, `test_the_changelog_is_gathered_at_release.py` and
`test_the_rules_have_one_owner.py`. It also covered four modules that sweep
the tree's Markdown: `test_one_heading_rule_holds_to_commonmark.py`,
`test_no_passage_is_pasted_into_a_second_file.py`,
`test_no_document_names_the_old_roots.py` and
`test_the_set_a_work_item_always_has.py`. The commit changes no Python file,
so no ruff run was owed.
