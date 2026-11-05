# Design: remove the seal candidates (#1375)

## Grounding

Every line coordinate and every present-tense statement of the tree in this file was read at 858c5fb7, the branch's routing commit, whose tree differs from v0.32.2 (9dd67e2a) only by this work item's `routing.md` (executed: `git show --stat 858c5fb7`). The file names no measured fact without its command. #1368 is the open prevention home for dating these statements.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | History goes to git, the release notes and the work record. The eleven files leave the tree and stay readable at v0.32.2, so nothing is kept beside the tree to stand for them. The same commit removes what stood on them: the README section, its links, the preview sentence's clause and the notice's clause. |
| `skills/agent-contract/SKILL.md` rule 19 | Each sentence that states the directory is found by `git grep` and rewritten in place. G1 lists them. |
| `docs/releasing/branch-and-release.md` *The version moves at the start of a release, in the first pull request into `release/vX.Y.Z`* (read, `:31`) | This work item's pull request is the release's first into `release/v0.32.3`, so its build moves `.claude-plugin/plugin.json` from 0.32.2 to 0.32.3. #1374 leaves the version alone (spawn prompt, read; #1374's branch holds only its `routing.md`, executed: `git diff --stat 9dd67e2a chore/1374-the-directory-tracks-a-dist-branch`). |
| `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* | The build writes `changelog.md` in this work item's directory. The diff touches none of the files that call for a `### Process changes` table. |
| the owner's decision of 2026-11-05 (spawn prompt and #1375's body, read) | The directory goes. #1100 kept the owl and the bee as candidates, and #1101 made the owl the mark (read: `git log -- assets/seals/candidates`), so the bee is the one kept candidate this removes. |
| #1375 *Done when* (read: `gh issue view 1375`, no comments) | No shipped file names the directory, by `git grep -n "seals/candidates\|candidates/"` outside `seal/threads/`. The README and the notice state the directory as it is. Every check that reads a cited path or a link in the two files passes. |

**G1. What stands on the directory (executed).** `git ls-files assets/seals/candidates` lists eleven files: `bee-28-pixel.{ans,png,txt}`, `bee-web.{png,svg}`, `section-14-light-red.{ans,png,txt}` and `section-28.{ans,png,txt}`. `git grep -n -i "candidates/\|seals/candidates\|bee-28\|bee-web\|section-28\|section-14"` outside `seal/threads/` hits `TRADEMARKS.md:11` and `assets/seals/README.md` alone. `git grep -n -i "\bbee\b"` outside `seal/threads/` hits the README alone. Each README hit is inside `## Candidates` (`:231` to the file's last line, `:319`), except two:

- `:36`, the preview rule's clause "in this directory and in `candidates/`";
- `:121`, the horned owl's entry, "over the bee below", whose "below" points into `## Candidates`.

This list is made by the third method of contract rule 12 over the class "a shipped sentence that names the directory or one of its marks". Searching the words "candidate" and "section sign" over `docs/`, `skills/`, `agents/`, `hooks/`, `tests/` and the two READMEs found no other sentence about the seal candidates. The hits in `docs/layout/one-root-by-lifetime.md:155` and `skills/implement/SKILL.md:96` use "commit candidate", which means something else (read).

**G2. Nothing reads the directory (executed).** No test, script, hook or workflow names `assets/seals` except `.github/scripts/publish_release_note.py:653`. That line is a comment about `assets/seals/owl.svg`, which stays. The README says the same at `:242`: "no code reads any of them".

**G3. The links in the two files (executed, a read-only probe).** For each `](<target>)` in `assets/seals/README.md`, resolved from `assets/seals/`, and in `TRADEMARKS.md`, resolved from the root, `test -e` was run. Every target exists. The four `candidates/*.png` targets are at `:268`, `:281`, `:296` and `:300`, all inside `## Candidates`, so they leave with the section. The other targets stay and keep resolving: `../../.claude-plugin/icon.png`, `../../TRADEMARKS.md`, `gold-lily.png`, `red-lily.png`, `placeholder-s.png`, `horned-owl.png`, `owl.png`, `horned-owl.svg`, `owl-social.png`, `assets/seals/` and `LICENSE`.

**G4. The checks that read the two files (read).** No check reads a markdown link's target. Three checks read the two files:

- `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads `path` *section* and `path#name` citations in every tracked file outside the records. The README's `seal_stamp.py#read_sprite` (`:259`) and `seal_stamp.py#SPRITE_COLOURS` (`:129`, `:161`, `:285`) start with a bare file name. No tracked top-level entry has that name (executed: `git ls-files`, first segments), so the check does not read them. The README's one section citation, `docs/checks/the-stamp.md` *The stamp* at `:4`, stays, and that file has `## The stamp` (executed: `grep -n`).
- `tests/behaviour/test_docs_line_wrap.py` covers `TRADEMARKS.md` (`:124`), so the rewritten list item keeps the file's wrap.
- `tests/behaviour/test_the_release_check_watches_what_ships.py:55` puts `assets` and `TRADEMARKS.md` among the paths whose change alone moves no version. This change moves the version for the release, not because of those paths.

**G5. What the preview sentence measured (executed).** `git log -S` gives two commits. The rule's Pillow 12.3.0 measurement first appeared at 43cbc361 as "the five previews made before the placeholder S's". Its present wording came at 74a680c1. At 74a680c1, `git ls-tree -r` lists `.ans` previews for the gold lily, the red lily and the placeholder S in the directory, and for `section-28`, `section-14-light-red` and `bee-28-pixel` in `candidates/`. `owl.ans`, now `horned-owl.ans` after 33c09a93, "was drawn the same way". The sentence records a measurement, so its subject after the removal is the set it measured, less `candidates/`: the gold lily's, the red lily's and the placeholder S's previews. Writing "every preview of a `.ans` in this directory" would also cover `owl.png`, which is drawn with Pillow 13.0.0 and described by the next sentence. That subject would be wider than what was measured.

**G6. The sprite rule the Candidates section explains stands in the code (read).** The paragraph "A sprite becomes the mark by replacing `seal-mark.txt` with it" (`:258`) explains what `skills/verify/scripts/seal_stamp.py#read_sprite`'s docstring and the module docstring (`:13`) already state, and the paragraph's citation of `read_sprite` is at `:259`. Removing the paragraph leaves that rule stated in the code. `## The next entry` (`:222`) keeps how a new mark gets its entry.

**G7. `TRADEMARKS.md` after the removal (executed).** `ls assets/seals/*.txt` matches nothing, so the clause "and each `.txt` file there, the sprite or chart of a mark" names no file once `candidates/` is gone. The sprite the stamp presses is `skills/verify/scripts/seal-mark.txt`, which has its own list item (`:15`). The notice at each earlier tag still names that tag's candidates. The notice at HEAD states what HEAD holds, as #1375 *Done when* asks.

## Scope

In:

1. The eleven tracked files under `assets/seals/candidates/` (G1) are removed with `git rm`, so the directory is gone from the tree.
2. `assets/seals/README.md`: the section `## Candidates`, from its heading to the end of the file, is removed with its three `###` entries and the four image links (G1, G3). The file ends with `## The next entry`'s paragraph.
3. `assets/seals/README.md`, preview rule (`:34`-`:37`): the clause about the Pillow 12.3.0 measurement names the previews it measured that remain, the gold lily's, the red lily's and the placeholder S's. It says each matched its `.ans` pixel for pixel, and keeps "and `horned-owl.png` was drawn the same way" (G5). It no longer says "in `candidates/`".
4. `assets/seals/README.md:121`: "over the bee below" loses "below" and names nothing outside the directory (G1). The owl's decision in #857 stays as written.
5. `TRADEMARKS.md:10`-`:14`: the first list item names every `.svg`, `.png` and `.ans` file under [`assets/seals/`](assets/seals/) as the emblem each release carried. The phrases "its `candidates/` included", "and each `.txt` file there, the sprite or chart of a mark" and "and the candidates kept beside it, which no release carried" are removed (G7). The file keeps its wrap (G4).
6. `.claude-plugin/plugin.json`'s `version` moves from 0.32.2 to 0.32.3 (Grounding, `docs/releasing/branch-and-release.md`).
7. This work item's `changelog.md` holds one entry under `### Removed` naming #1375. It says the eleven files of marks no release carried are gone with the README section and the notice's clause, and that git's history keeps them at v0.32.2. It has no `### Process changes` table (Grounding).

Out:

- `.gitattributes`, `export-ignore` and the `dist` branch. They belong to #1374, which builds the branch. Once this lands, `assets/seals/candidates/` is not a path #1374 has to leave out.
- Every other entry of `assets/seals/README.md` and every file it links. No hit in G1 or G3 touches them.
- A new check that a link in `assets/seals/README.md` resolves. G4 finds that no such check exists. Adding one would be a mechanism with nothing caught on record (*Removes*, last row).
- Redrawing any preview. Scope 3 narrows a recorded measurement and asserts nothing new (G5).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the directory is gone | Given the build's HEAD, when its tree is listed, then nothing under `assets/seals/candidates/` is tracked or on disk | `git ls-files assets/seals/candidates` prints nothing, and `test -e assets/seals/candidates` exits 1 |
| S2 no shipped file names it | Given the build's HEAD, when #1375's search runs outside `seal/threads/`, then it finds nothing | `git grep -n "seals/candidates\|candidates/" -- ':!seal/threads'` exits 1. With `bee-28\|bee-web\|section-28\|section-14` it also exits 1 |
| S3 every link resolves | Given the build's HEAD, when each `](<target>)` of `assets/seals/README.md` and `TRADEMARKS.md` is resolved from its file's directory, then each target exists | G3's probe rerun at HEAD |
| S4 the README states the directory as it is | Given the README at HEAD, when a reader reads it, then it has no `## Candidates` section, its preview rule names the three measured previews with no `candidates/`, and the owl's entry points at no section below | read against *Scope* 2, 3 and 4 |
| S5 the notice states the drawings as they are | Given `TRADEMARKS.md` at HEAD, when a reader reads its first list item, then it names the emblem each release carried under `assets/seals/`, with no candidates and no `.txt` | read against *Scope* 5, and `tests/behaviour/test_docs_line_wrap.py` passes |
| S6 the cited sections still resolve | Given HEAD, when the citation check runs, then it reports no dangling citation | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes |
| S7 the release's version | Given HEAD, when `.claude-plugin/plugin.json` is parsed, then its `version` reads `0.32.3` | `python3 -c 'import json; print(json.load(open(".claude-plugin/plugin.json"))["version"])'` prints `0.32.3` |

## Data & interfaces

None. No code, schema or command changes. A user's installed plugin copies the repository's root, so after an update it no longer holds the eleven files.

## Rule changes

- nothing
  why: The work removes `assets/seals/candidates/` and edits `assets/seals/README.md` and `TRADEMARKS.md`, none of which is under the policy root. No document under `docs/` names the directory (G1), so no rule changes.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the eleven candidate files | `assets/seals/candidates/` | git's history at v0.32.2. Nothing reads them (G2), and the owner decided their removal on 2026-11-05 |
| the candidates section, its three entries and four image links | `assets/seals/README.md` *Candidates* | Its subject leaves the tree. The sprite rule it explained stands in `skills/verify/scripts/seal_stamp.py#read_sprite` (G6), and the text stays readable at v0.32.2 |
| the clause "and in `candidates/`" of the preview rule | `assets/seals/README.md`, the preview rule's paragraph | restated over the measured previews that remain (G5) |
| "below" in the horned owl's entry | `assets/seals/README.md` *The horned owl — 0.23.1 to 0.25.0* | The section it pointed at is gone |
| the candidates and `.txt` clauses of the notice | `TRADEMARKS.md`, the first list item | The files they named leave the tree (G7). The notice at each earlier tag still names them |
| no mechanism is added | none | The work adds no gate, check, hook, CI step, rule, label or mark, so nothing has to go in return |

Framed 2026-11-05 by framer, before the build.
