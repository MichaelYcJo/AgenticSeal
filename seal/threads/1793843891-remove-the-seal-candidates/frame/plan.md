# Implementation Plan: remove the seal candidates (#1375)

## Technical context

Every line coordinate and every present-tense statement of the tree in this file was read at 858c5fb7, the branch's routing commit, whose tree differs from v0.32.2 (9dd67e2a) only by this work item's `routing.md` (executed: `git show --stat 858c5fb7`). #1368 is the open prevention home for dating these statements.

The work touches two prose files, one directory and one JSON field. No code is involved:

- `assets/seals/candidates/`: eleven tracked files, read by nothing (`frame/design.md` G1, G2).
- `assets/seals/README.md`: 319 lines (executed: `wc -l`). `## Candidates` runs from `:231` to the file's end. The two sentences outside it that name the candidates are at `:36` and `:121` (G1).
- `TRADEMARKS.md`: 21 lines. The list item at `:10`-`:14` names the candidates and the `.txt` files, which only `candidates/` holds (G7).
- `.claude-plugin/plugin.json:4`: `"version": "0.32.2"`.

The previous release's version move is the precedent. Work item `1793833679-update-reads-the-config-dir-in-use` moved the version in phase 1's last commit, together with its changelog fragment, so round 1 read both (read: its `frame/plan.md` *Phases*, and `git show 6adb548e`).

No case is added. The work removes files and text and changes no behaviour. The checks that already read the two files are the proof (G4). Each acceptance row is a command or a reading that needs no new case.

**Failure scenario of the chosen approach, six months on.** Someone wants the bee again, or wants to show how the owl was chosen. The drawings are only at tags up to v0.32.2. The horned owl's entry still says the owner chose the owl over the bee, but names no place where the bee can be seen. The cost is one `git show v0.32.2:assets/seals/candidates/bee-28-pixel.png` for a reader who knows to look there. The README names no tag for the bee because a shipped `candidates/` path would fail #1375's own search (*Alternatives considered*, row 3).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep `assets/seals/candidates/` as it is, and have #1374's `dist` branch leave it out with `export-ignore` | The tree keeps eleven files nothing reads, plus a README section and a notice clause to keep true beside them. The `dist` branch carries a pattern that exists only to hide them. This is the structure kept. Its premise was that a candidate might still become the mark. #1101 made the owl the mark, and the owner decided on 2026-11-05 to remove the directory, so the premise does not hold (`frame/design.md` *Grounding*, the owner's row) | rejected |
| Remove the directory and every sentence that states it (chosen) | A reader who wants a candidate looks in git's history, as `skills/core/SKILL.md` *The rule a mechanism is kept against* says history is read. The cost is in *Technical context* | chosen |
| Replace `## Candidates` with a short note naming v0.32.2 as the tag that holds the candidates | The note uses the path `assets/seals/candidates/` or `candidates/`, which #1375 *Done when* forbids in a shipped file. Without the path, the note says only "an earlier tag held other marks", which tells a reader nothing they can open. The note would also describe files the directory does not hold, and the README's title says the directory keeps "the emblems the stamp has carried" | rejected |
| Restate the preview rule by dropping only "and in `candidates/`", so it reads "every preview of a `.ans` in this directory matched" | The directory now holds `owl.ans`, whose preview Pillow 13.0.0 drew and the next sentence describes. The shortened sentence would then claim a 12.3.0 match for `owl.png` that was never measured (`frame/design.md` G5) | rejected; *Scope* 3 names the three previews the measurement covered that remain |
| Keep `TRADEMARKS.md`'s candidates clause, so the notice still reserves the drawings git's history holds | The notice at HEAD would name files HEAD does not hold. The notice at each earlier tag already reserves that tag's candidates (`frame/design.md` G7), and #1375 *Done when* asks the notice to state the directory as it is | rejected |
| Move the version in a commit of its own, before the removal | A commit of its own still reaches round 1, so the round read is the same. The precedent puts the move in the phase's last commit with the fragment, which keeps it beside the entry the release note reads (*Technical context*) | rejected; the phase's last commit carries it |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* 1 to 7. The phase's last commit adds this work item's `changelog.md` and moves `.claude-plugin/plugin.json`'s `version` from 0.32.2 to 0.32.3, so round 1 reads both. #1374 leaves the version alone. A fix pass that changes what the work ships updates the fragment in the same range (`docs/layout/the-record-layout.md` *A commit after the build brings its changelog fragment along*). | S1, S2, S3 and S7 by their commands at HEAD. S4 and S5 by reading the two files against *Scope* 2 to 5. S5's wrap and S6 by the narrow run of `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, with `tests/behaviour/test_the_release_check_watches_what_ships.py` beside them, all unchanged. `git diff --name-only` against the base lists the eleven removed files, `assets/seals/README.md`, `TRADEMARKS.md`, `.claude-plugin/plugin.json` and this work item's records, and nothing else. The suite stays `unverified` until the orchestrator's broad run. | 4c453c20 |

## Operational impact

None for a deployer. A user's installed plugin copies the repository's root, so the first update to 0.32.3 drops the eleven files from the install. No code reads them (G2), so nothing at runtime changes. No dependency, variable or migration is added.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
