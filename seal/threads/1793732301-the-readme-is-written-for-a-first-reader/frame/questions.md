# Questions for the planner: the README is written for a first reader (#1102)

The ticket left these judgments open, and the tree answered each one:

- The subject is the two editions and not the policy root, so the ratchet sentence changes through `## Rule changes`: `frame/design.md` *Grounding*, the `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* row.
- The owl stands above the title, and the sentence stands directly under it: `frame/design.md` *Grounding*, the `docs/layout/one-root-by-lifetime.md` *Naming* row.
- Reference material with a home elsewhere is linked, and the rest stays below the first screen: `frame/plan.md` *Alternatives considered*, the second row.
- The page carries the owl, a `mermaid` workflow and the stamp image, and no recording: `frame/plan.md` *Alternatives considered*, the ASCII and the recorded-demo rows.
- The social preview's file, format and source: `frame/design.md` *Scope* 8 and *Grounding*, the GitHub and probe rows; `frame/plan.md` *Alternatives considered*, the three social-preview rows.
- The README's first line is held by a case: `frame/plan.md` *Alternatives considered*, the two first-line rows.
- The page describes no recurrence check: `frame/design.md` *Grounding*, the issue comment 5 row.
- The build runs in three phases: `frame/plan.md` *Alternatives considered*, the last row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the social preview carry the AgenticSeal name, or the sentence, beside the owl, and on which field colour? The tree cannot answer it because this is a choice about the brand's look, and no file states one. No probe can answer it either, because a render shows what an option looks like and not which option the owner wants. | a person | (a) The owl alone on a solid field. The entry's command redraws the PNG on any machine, and GitHub's card sets the name and description beside the image. (b) The owl and the name as text. The PNG depends on the fonts of the machine that drew it, so the entry records the font, and another machine's redraw may differ. (c) The owl and the name as outlined paths. The command redraws the file anywhere, and the lettering becomes a drawing under `TRADEMARKS.md`, with a second source to keep beside `owl.svg`. Any field colour changes only the SVG's `<rect>`. | (a): `assets/seals/owl-social.svg` places `owl.svg` at 480 × 480, centred, on `#f4ecdc` | open |
| Q2 | Does the Claude Code plugin directory render the README's relative image path (`assets/seals/owl.svg`) and its `mermaid` block the way GitHub does? A command could answer it, but no probe can run here: the directory's page for this release exists only after the release ships, and no subagent can open it. | a measurement | (a) Relative paths and `mermaid`. GitHub renders both (`frame/design.md` *Grounding*), and a viewer that renders neither shows the owl's alt text and the fence's arrows as text. (b) An absolute URL to the image's raw file on GitHub, on `main`. This renders anywhere that fetches images, but before the release merges to `main` it points at a file `main` does not hold yet. | (a). After the release, the owner opens the plugin's page in the directory and files an issue if the owl or the chart does not show. | open |
