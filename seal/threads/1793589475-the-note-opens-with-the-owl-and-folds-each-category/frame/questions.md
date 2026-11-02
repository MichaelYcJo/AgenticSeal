# Questions for the planner: the note opens with the owl and folds each category (#1153)

The issue left these judgments open, and the tree answered each. Their
grounds stand where each line points, and nobody needs to reopen them:

- Which job writes the header: `plan.md` *Alternatives considered*, rows A1 to A3.
- The reader without images: `frame/design.md` *Scope* item 3.
- What is removed: `frame/design.md` *Removes*.
- PNG or SVG: `frame/design.md` *Grounding*, the probe row on how release assets are served, and `plan.md` row A7.
- How a fragment or a title inside a fold is kept from closing it: `frame/design.md` *Scope* item 5, and `plan.md` row A6.
- The emoji in the category summaries: `frame/design.md` *Grounding*, the row on the owner's rule, and `plan.md` row A8.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the published 0.28.0 note show the owl beside the results, readable, in a browser at desktop and at phone width? | a measurement | It is read on the releases page once the first note in the new shape is published. If the image crowds the text at phone width, a later change can narrow the image's width in the header; the structure stays. | The header as `frame/design.md` *Data & interfaces* gives it, with the image at the width `draw` answers. | open |

Q1's reason it is a row: GitHub's renderer was probed (`frame/design.md`
*Grounding*) and returned the header's HTML intact, but how a browser lays
the table out on the releases page can be seen only on a published release.
Publishing a release is a write to GitHub, which no framer's probe makes.
