# 1792365855-the-placeholder-s-emblem-has-no-assets-entry — overview

## Scope confirmation

`assets/seals/` gains the placeholder S's entry (`placeholder-s.ans`, `placeholder-s.png` and its section in `README.md`), and the README's sentences saying the S has no entry are rewritten in place; no gate, hook, instruction or code changes.

## Why this work exists

The emblems page keeps every emblem the stamp has carried, and the one on every stamp since 0.20.0 was missing from it (#978).

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The tag the entry is drawn from | The spawn prompt: "the draw-again command against the right tag (v0.22.0 is the last that drew it)". `git show v0.22.1:skills/verify/scripts/seal-mark.txt` hashes the same as at v0.20.0, v0.21.0, v0.21.1 and v0.22.0, so v0.22.1 carries the S too; since #975 the sealer presses it rather than the broad gate's run | v0.22.1, the last tag when the entry was written | The page's other entries are each drawn from the last tag that carried the emblem (`The file is v0.19.0's`). The disc is cell-for-cell the same at all five tags, measured by comparing `compose`'s first 28 columns; only the sample panel differs (a `ledger` row until #944, the sealer's shorter panel from #975) |
| The lilies' command shape does not draw the S | `stamp(m.SAMPLE_ROWS, m.DEFAULT_SCALE)` with only the module exec'd: from v0.20.0 the module reads `seal-mark.txt` beside `__file__` at load and fails with `NameError: name '__file__' is not defined`, and v0.22.1's `stamp` takes no scale | The S's command writes the tag's chart into a temporary directory, sets the module's `__file__` there and calls `stamp(m.SAMPLE_ROWS)`; the README's paragraph on the commands says so | spec silent; the page's rule is that "the source of each entry is its tag", so the chart is read from the tag rather than from the working tree |
| The README's reason an entry waits for its tag | "The version check in `tests/test_release_hygiene.py` refuses a version at or above the running one unless a tag names it" | The sentence is gone; `## The next entry` now says only that #857's mark gets its entry once a tag carries it | `tests/test_release_hygiene.py#LOADED` lists `skills`, `agents`, `docs`, `templates` and four root files, not `assets`. The sentence was true while the page lived at `docs/seals/`, before #832 moved it |

## Not verified

| Item | Who must answer |
|---|---|
| `placeholder-s.ans` printed with `cat` in a truecolour terminal. Its bytes are the tag's own `stamp` output, compared with `cmp`, and its preview was looked at; the file itself was not printed in a terminal | the owner, through the orchestrator |
| How the preview's three new styles read beside a real terminal's: dim drawn at half opacity, bold as Menlo Bold, green as xterm's (0, 205, 0). No earlier preview carried them, so no file fixed them, and the README now states them as the rule | the owner, through the orchestrator |

## Not done

No `changelog.md`. `docs/the-record-layout.md` §*A change writes fragments, never a shared file* says where a fragment goes, and a fragment is what a release note carries to plugin users. Nothing a plugin user runs or reads in operation changes here: no code reads `assets/seals/`, as its README says. The page is the repository's gallery.

No case. The page states no rule a case could hold. It describes files that no code reads, and the one claim a case could pin, that each command reproduces its `.ans`, was run once by hand for the new entry.

The PNG renderer stays outside the tree, as the earlier previews' did. The README now states the rule it draws by, and the five earlier previews redraw by it pixel for pixel.

## Fed back into the spec

none
