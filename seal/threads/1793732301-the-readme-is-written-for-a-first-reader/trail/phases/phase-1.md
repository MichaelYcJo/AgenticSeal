# Phase 1: 1793732301-the-readme-is-written-for-a-first-reader

## What this phase found

**The frame holds for this phase.** Read before the build: `assets/seals/owl.svg`
exists, with a `viewBox` of 1200 × 1200, so 480 × 480 scales it without
cropping. `TRADEMARKS.md` reserves every `.svg` and `.png` under
`assets/seals/`, so the two new files fall under the notice with no edit to
it. `tests/behaviour/test_the_release_check_watches_what_ships.py#STAYS_HOME`
holds `assets`, so the new files move no version. The GitHub page the frame
cites was fetched again on 2026-11-04 (executed: WebFetch). It says "Your
image should be a PNG, JPG, or GIF file under 1 MB in size", recommends
"1280 by 640 pixels for best display", and recommends "an image with a solid
background" where the author is unsure. Q1 and Q2 stay open, and the build
follows Q1's default (a), as the spawn prompt says.

**The command needs `resources_dir`, and without it resvg fails silently.**
The icon's command passes only `svg_path`. Run that way over
`owl-social.svg` from the repository's top directory, `resvg_py` 0.5.0
exited 0 and wrote a 4,647-byte PNG of the field alone, with no owl
(executed). The relative `href` is not read against the SVG's own
directory. With `resources_dir="assets/seals"` it wrote 190,963 bytes, the
size the framer's probe recorded, and the owl stands centred. So the
entry's command passes `resources_dir`, and the entry says what happens
without it. Judged against `frame/design.md` *Scope* 8, which names the
command and leaves its arguments to the build.

**The PNG is RGBA, and every pixel is opaque.** resvg writes RGBA. Pillow,
from a throwaway environment, read the alpha channel's extrema as
(255, 255) and the corner pixels as (244, 236, 220, 255), the `#f4ecdc`
field (executed). *Scope* 8 asks for an opaque image, and this one is
opaque. Converting it to RGB would need a second tool after the command,
so the one documented command would no longer redraw the committed file.
Judged against *Scope* 8 and *User scenarios* S8, which ask that the
command write the committed file byte for byte.

**The verification S8 and the plan's row 1 ask for** (executed, after the
commit 2d43466d2):

- The command line, taken from `assets/seals/README.md` by `grep` rather
  than typed, ran under `uv run --isolated --no-project --with
  resvg_py==0.5.0 sh -c` over a deleted `owl-social.png`. It exited 0, and
  `git diff --quiet HEAD -- assets/seals/owl-social.png` exited 0. The
  redrawn file's `git hash-object` is the blob at HEAD,
  `c577714bd607728a21e690f6da5adb910f317541`.
- `file` printed "PNG image data, 1280 x 640, 8-bit/color RGBA,
  non-interlaced", and `wc -c` printed 190963.
- The committed PNG was viewed: the little owl's red wax seal, whole, centred
  on the parchment field, with even margins left and right.

b8365df07 then rewords one sentence of the paragraph. GitHub's page
recommends a solid background, and the first wording said the page asks
for one. The command line is not in that diff, so the redraw above still
stands for it (read: `git diff 2d43466d2 b8365df07`). The two corpus
modules that read the file passed again at b8365df07 (executed).

**The narrow set** (executed, one command):
`bin/test -q -p no:xdist tests/behaviour/test_release_hygiene.py
tests/behaviour/test_the_release_check_watches_what_ships.py
tests/behaviour/test_a_cited_section_stands_in_its_file.py
tests/behaviour/test_one_heading_rule_holds_to_commonmark.py
tests/behaviour/test_both_editions_carry_the_same_folds.py` exited 0, 120
passed. The first two are the plan row's. The other three read a path this
phase changed: the cited-section check reads every tracked file, and the
other two read every tracked `.md`. The set came from `git grep` over
`tests` for `assets`, `seals`, `.png`, `.svg` and the listing calls
(`ls-files`, `glob`, `rglob`, `os.walk`). Each listing call's scope was
read for whether it reaches `assets/`.

**No case is written and no `seal mutate` runs.** The phase adds two image
files and prose, and no code. `skills/verify/SKILL.md` *The narrow command
still has to be able to fail* gives prose "whatever actually parses those
files", which is the three corpus modules above. S8 states that no case
reads the preview, and why.

**One departure from the frame: a second sentence of `assets/seals/README.md`
changes.** `frame/design.md` *Data & interfaces* gives the entry "one
paragraph and one image line more". The directory's opening section said
"Each owl's entry holds a third, an `.svg`", and once the little owl's
entry holds the social preview's two files, that sentence is no longer
whole. So the same commit adds the social preview's `.svg` and `.png` to
it. Judged against `skills/agent-contract/SKILL.md` rule 19. A `git grep`
for `assets/seals`, `owl.svg` and `social preview` outside the records
found no other sentence that lists the directory's files. That grep is a
sample: its search words are the only method used.

**The paragraph's grounds for what nothing checks.** It follows the icon's
*What nothing checks* item, and adds one fact the icon does not have: the
preview's live copy is the one in the repository's settings, so a redraw
without a new upload still leaves the old image on a shared link. The
setting's path, Settings, General, Social preview, is written without
italics. That keeps the cited-section check from reading it as a citation
of a section.
