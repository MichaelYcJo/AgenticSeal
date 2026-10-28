# Questions for the planner: 1793152332-the-stamps-mark-is-an-owl

## Answered by the tree, not to be reopened

- **The colour of each sprite letter.** `assets/seals/README.md` *The owl
  and the bee in the stamp's reds* gives it, and every colour is one of the
  nine `DISC_COLOURS` in `skills/verify/scripts/seal_stamp.py`.
- **The drop shadow's colour is `DROP`, `(84, 8, 12)`.** The candidate
  `owl-28-pixel.ans` the owner looked at paints the shadow `(78, 8, 12)`,
  which is not one of the stamp's reds (executed, a one-off probe). The
  owner's brief says every colour is one of the stamp's existing reds, and
  the README says the shadow cell takes the drop shadow.
- **The disc's frame is `build`'s.** The candidate's outer half-rows differ
  from `build`'s (executed). The owner settled the frame on 2026-10-07, and
  `build` draws it.
- **The sprite fits the field.** Every drawn cell and every shadow cell lies
  inside the field at an offset of six cells (executed).
- **The stamp still fits one hook message.** The widest reference panel with
  its label is 5,959 UTF-16 units against `MESSAGE_BUDGET`'s 9,000
  (executed).
- **The letter twin keeps `KEY`.** Every sprite colour is one of the nine,
  so each disc cell still has one letter (executed).
- **The plugin icon is a PNG, not the SVG.** `claude plugin validate .` on
  Claude Code 2.1.312 refuses SVG and WebP and asks for a square PNG or JPEG
  of 512 to 2048 pixels under 2 MB (executed). The plugin reference says the
  field is `icon`, a path inside the plugin, read by Anthropic's directory
  and ignored by Claude Code at load time (read).
- **The release seal is the page image.** Issue #857's body, *What closes
  this issue*, makes the SVG the source of the release note's `seal.png`.
- **`rsvg-convert` draws the SVG faithfully.** At 480 pixels its output and
  the candidate preview `owl-web.png` differ by a root-mean-square 1.45 per
  cent and read the same when opened (executed).
- **Pillow goes.** Its only reader outside the suite is `release_seal.py#draw`,
  which stops painting in phase 1. `CLAUDE.md` *The rule a mechanism is kept
  against* decides it.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | The owl's SVG fills its shapes with seven reds of its own, none of them equal to one of the stamp's nine: `#961c20`, `#c43434`, `#78141a`, `#8a181e`, `#46080c`, `#ec6e68` and `#ce3e3c`, where the stamp's are, for example, `WAX_EDGE` `(150, 24, 28)` and `LIGHT` `(222, 86, 78)`. Should the page form be recoloured to the stamp's exact nine? The tree cannot answer it: the owner chose `owl-web.svg` as drawn and also said every colour is one of the stamp's reds, and the two statements disagree only at this level of exactness | a person | (a) Ship the SVG as the owner chose it: the icon and the release seal look exactly like the preview the owner approved. (b) Map each fill to the nearest of the nine: the page form and the sprite share exact colours, and the drawing differs from the one the owner looked at | (a): the SVG moves unchanged and the icon is drawn from it as it stands | open |
| Q2 | How large is the page image? The directory accepts 512 to 2048 pixels on a side. The release note shows the image at its width divided by `DENSITY`, 2, so the side decides the note's display size; today's sprite disc shows at 168 CSS pixels. The tree states no size for a page | a person | (a) 512 pixels: the smallest the directory accepts, shown at 256 CSS pixels in the note, about 68 KB. (b) 1024 pixels: sharper in the directory, shown at 512 CSS pixels unless a display width separate from `DENSITY` is added | (a) 512 pixels | open |
| Q3 | Should the README (`README.md` and `README.ko.md`) show the owl, and should the GitHub social preview be set to it? Issue #857's body names both as places a page shows the vector, but its *What closes this issue* list names neither. The social preview is a repository setting a person uploads on GitHub, not a file of the tree, so no phase can set it | a person | (a) Neither in this work item: the README and the social preview wait for a work item or an act of the owner's. (b) The README shows the owl in this work item, as one more phase; the social preview is still the owner's act | (a) Neither in this work item | open |
| Q4 | The owl entry's `owl.png` preview is drawn by the rule in `assets/seals/README.md`, which names Menlo at 19 pixels and Pillow 12.3.0, and no script in the tree draws it. Can the crafter of phase 4 reproduce the rule exactly on its machine? | the work | The crafter first redraws `placeholder-s.png` by the rule. Where it matches pixel for pixel, `owl.png` is drawn by the same renderer. Where it does not, `owl.png` is drawn anyway and the phase record states the difference as a divergence | The crafter of phase 4 draws it and records the comparison | answered by phase 4: `placeholder-s.png`, both lilies and the three candidates redrew with 0 differing pixels, and `owl.png` was drawn by the same renderer (`trail/phases/phase-4.md`) |
