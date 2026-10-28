# Overview: 1793152332-the-stamps-mark-is-an-owl

## Why this work exists

The stamp carried a placeholder S that no longer stood for the name; the owl the owner chose becomes the mark, drawn for the terminal's grid and as a vector for a page, and the plugin gains its icon.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Where `draw` reads the manifest | `frame/design.md` *Data & interfaces*: `draw` reads the manifest under `CODE` | under `ROOT` | `ROOT` is the module's name for the tree it reads data from, and a case can point it at a fixture; `CODE` also loads `publisher()`, `gate()` and `readers()` in the same run. In the release job the two are one path |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through the tree's `bin/seal gate` after the review rounds settle |

## Not done

nothing

## Fed back into the spec

none
