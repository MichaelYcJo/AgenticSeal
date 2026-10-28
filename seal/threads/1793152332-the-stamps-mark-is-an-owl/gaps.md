# Overview: 1793152332-the-stamps-mark-is-an-owl

## Why this work exists

The stamp carried a placeholder S that no longer stood for the name; the owl the owner chose becomes the mark, drawn for the terminal's grid and as a vector for a page, and the plugin gains its icon.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Where `draw` reads the manifest | `frame/design.md` *Data & interfaces*: `draw` reads the manifest under `CODE` | under `ROOT` | `ROOT` is the module's name for the tree it reads data from, and a case can point it at a fixture; `CODE` also loads `publisher()`, `gate()` and `readers()` in the same run. In the release job the two are one path |
| The order `read_sprite` checks a sprite in | `frame/design.md`: the faults the reader reports, in a listed order | every line's shape first, then the field and the shadow | the shadow check on line N reads line N + 1, which a single pass had not yet shape-checked; the faults are still reported in the listed order |
| The shadow's colour against the owner's candidate | `assets/seals/candidates/owl-28-pixel.ans` drew the 25 shadow cells in (78, 8, 12) | `DROP`, (84, 8, 12), the stamp's own shadow | `frame/design.md` and `frame/questions.md`: every colour is one of the stamp's; the other 275 field cells match the candidate |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through the tree's `bin/seal gate` after the review rounds settle |

## Not done

nothing

## Fed back into the spec

none
