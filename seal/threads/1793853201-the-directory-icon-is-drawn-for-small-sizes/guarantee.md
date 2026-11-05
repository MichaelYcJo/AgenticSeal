# Guarantee: 1793853201-the-directory-icon-is-drawn-for-small-sizes

The base `release/v0.32.4` resolves here through `release/v0.32.4@{upstream}` to 12d48178, the commit `trail/gate.md` names. HEAD's merge base with it is a909d25c; the one base commit HEAD does not hold, 12d48178 (#1386), touches no path this diff touches. `trail/gate.md` names 0c8850ca, an ancestor of HEAD, and the one commit after it, b5ffa864, touches only `seal/threads/1793853201-the-directory-icon-is-drawn-for-small-sizes/trail/gate.md`. `seal pr-body ... --check` on the body file exited 0, both with the installed 0.32.3 copy and with the tree's `bin/seal`. The work item holds no `frame/`, no phase record and no round record, as `routing.md` (`straight to the PR`, planning and implementation by the session) gives; there is no issue, so the owner's decision read is `routing.md`'s answer and the request the spawn prompt quotes. No `seal/parity.md` is tracked, so no parity comparison is owed. With no phase record there is no crafter `executed` or `seen red` claim to sample, and with no `frame/design.md` no `## Removes` row; the changelog names no removal. The sample is therefore taken from the claims `changelog.md`, `gaps.md`, `assets/seals/README.md` and `TRADEMARKS.md` make about the tree.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| Each committed PNG is the drawing of its SVG at 512 x 512 by `rsvg-convert` (librsvg 2.58.4) | `assets/seals/README.md:237-242` | `rsvg-convert --version`; `rsvg-convert -w 512 -h 512 assets/seals/owl-icon-<c>.svg -o <scratch>/owl-icon-<c>.png` then `cmp` against the committed PNG, for cream and coral | holds (executed): version 2.58.4; both renders exit 0 and `cmp` exits 0 for both, byte for byte; `file` reads both as 512 x 512 RGBA |
| The two drawings differ only in the owl's colour | `changelog.md:3`; `assets/seals/README.md:232-233` | `diff` of the two SVGs split at `>` | holds (executed): one line differs, the masked rect's fill, `#f6ecd8` against `#ff7a6a` |
| The wax outline is copied from `owl.svg`'s outer path | `assets/seals/README.md:228` | `grep -o` of the `M 1177.4...` path data in `owl-icon-cream.svg` and `owl.svg`, each piped to `md5` | holds (executed): both hash to 157eff8e0590c9e8a251621718b592a1 |
| The drawing keeps a darker pressed disc, one plain ring, ringed eyes, the beak, one wing line each side, two rows of breast scallops and the branch | `assets/seals/README.md:228-232`; `changelog.md:3` | read of `owl-icon-cream.svg`; the rendered `owl-icon-cream.png` opened as an image | holds (read): disc `#9e1016` inside wax `#c41a1e`; one stroked circle r=430; two stroked eye circles with pupils; one beak path; two wing curves; scallops 3 and 2; a branch stroke with two leaves |
| `.claude-plugin/icon.png` stays as it is | `changelog.md:3`; the owner's request in the spawn prompt | `git diff --quiet 12d48178 HEAD -- .claude-plugin/icon.png` | holds (executed): exit 0 |
| No code reads the new files | `routing.md:16`; `assets/seals/README.md:19` | `git grep -n owl-icon HEAD -- . ':!seal/threads'` | holds (executed): the only hits are `assets/seals/README.md:224`, `:241`, `:247` |
| `TRADEMARKS.md` names the drawings among those the MIT License does not cover | `changelog.md:3` | read of the `TRADEMARKS.md` diff | holds (read): the new files fall under "every `.svg`, `.png` and `.ans` file under `assets/seals/`", and the line now names the owl drawn for the plugin directory's icon |
| The favicon-size drawing was not committed | `gaps.md:12` | `git diff --stat 12d48178...HEAD` | holds (executed): the diff adds the two SVGs, the two PNGs, `TRADEMARKS.md`, `assets/seals/README.md` and the work item's records, and no other drawing |
| The broad run passed at 0c8850ca: suite 6393 passed, 12 skipped, chain exit 0 | the orchestrator's part of the pull request body, paragraph 3; `trail/gate.md` | read of `trail/gate.md`; rule 2 keeps the broad run the orchestrator's | `trail/gate.md` records `run: 0c8850ca against 12d48178` (read); the printed counts are unverified, answered by the orchestrator's run, which wrote the record |
| The image the directory's form holds is the committed `owl-icon-cream.png` | `changelog.md:3`; `gaps.md:8` | none can run here | unverified, answered by the owner, as `gaps.md` names |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | no `frame/`; `routing.md` records the owner's answer of 2026-11-05: two drawings under `assets/seals/` and one README entry, no code reads either, the session plans and builds, the broad run and the sealer stand for review rounds | the owner's request in the prompt (two simplified icons, cream and light red, cream uploaded, `icon.png` unchanged); the diff | none |
| the build | the diff at b5ffa864: two SVGs, their PNGs, the README entry inside the little owl's section, one `TRADEMARKS.md` line, the records; no phase record | `routing.md`; `changelog.md`; the re-run rows above | none |
| the last round | none: `routing.md` routes `straight to the PR`, and `trail/rounds/` does not exist | `routing.md` | none |
| the changelog | the fragment's one `Added` entry: the two drawings, what they keep and simplify, cream uploaded, `icon.png` and every release seal unchanged, the README entry and `TRADEMARKS.md` | the diff and every re-run row; `gaps.md`. The README shows the one `rsvg-convert` command for the cream PNG and says "Draw each PNG again ... with `rsvg-convert`"; the same command with `coral` drew the committed coral PNG byte for byte, so "the command that draws each PNG" holds | none |
| the orchestrator's part of the pull request body | the changelog's facts restated, cited to `changelog.md`; no issue, owner's request in the session, `routing.md`'s light route; the broad run's printed line at 0c8850ca against 12d48178 | `changelog.md`; `routing.md`; `trail/gate.md`'s commit and base; the diff | none; its suite counts are the orchestrator's claim, unverified here |

```seal
target: b5ffa864 against 12d48178
Verdict: sealed
```
