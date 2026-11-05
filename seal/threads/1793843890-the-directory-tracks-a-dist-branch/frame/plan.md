# Implementation Plan: the directory tracks a dist branch (#1374)

## Technical context

Every line coordinate and every present-tense statement of the tree in this
section was read at commit `efd8edec` (`routing: declare #1374 under
automation`, on `release/v0.32.3` cut from `9dd67e2a`, v0.32.2), and a
crafter reading a later HEAD reads them as of that commit.

What this builds on:

- `.gitattributes` holds one line, `* text=auto eol=lf`.
- `.github/workflows/publish-release.yml` lines 57 to 97: the `publish` job's tag step (`.github/scripts/tag_release.py`) writes the output `tag`, empty on a push to `main` that moved no version (line 66). The note step runs only where `tag` is set (line 91). The workflow's `permissions:` is `contents: write` (lines 54 to 55). The `seal` job (lines 99 to 163) checks out the tag with `persist-credentials: false`, because it pushes nothing. The `dist` job pushes, so it keeps the default.
- `.github/scripts/tag_release.py` with `tests/github/test_tag_release.py` is the pattern a workflow step follows here: a script reading its inputs from the environment, cases in `tests/github/` that run it against fixture repositories, and a case reading the workflow's text in `tests/behaviour/test_a_release_publishes_its_note.py`.
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py`: `corpus` (lines 210 to 223) lists `git ls-files` outside `tests/censuses.py#RECORDS` and reads each file from disk. `citations` (lines 226 to 259) and `names` (lines 318 to 354) read only a target whose first segment is a top-level entry of what was listed (`top`, lines 231 and 323). The two tree cases (lines 386 to 404) hold a floor of 100 citations read. The fixtures cite files under `manual/`, and `repo(tmp_path, files)` (line 409) builds a tracked fixture tree.
- `.github/workflows/test.yml` lines 257 to 292: the `release-report` job runs on a pull request into `main`. It extracts the last tag with `git archive "$tag" | tar -x -C "$RUNNER_TEMP/at"` (line 280) and hands that directory to `release_report.py --at`, which reads `.test_durations` and `CLAUDE.md` there (`.github/scripts/release_report.py` lines 56 to 58) and exits 2 where it cannot read the first. `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py` reads the job's block.
- `evals/scripts/noninferiority.py#extract` (lines 173 to 179) archives REV's PATHS and extracts them with `filter="data"`. `run_side` calls it for the plugin tree at `--rev` (line 614) and for `evals/behaviour/` at `--suite-rev` (line 618). `tests/evals/test_noninferiority.py#Test_extract` holds it, and its case for an unresolvable REV matches `^git archive` (line 654).
- `.github/scripts/plugin_directory_check.py#is_ancestor` (lines 187 to 211) answers True, False or None, and `#line` (lines 214 to 260) prints "Reachable from", "NOT reachable from" or "unknown here" for the one `--ref`, `main` by default (line 293). `tests/github/test_plugin_directory_check.py` holds it.
- `tests/behaviour/test_the_release_check_watches_what_ships.py#test_every_top_level_entry_is_classified` (lines 129 to 140) is where a new top-level entry is met first.
- The probes in `frame/design.md` *Grounding* give the spellings that work and the ones that do not: `git archive` of a path the attributes drop exits 0 with nothing, attribute sources do not lift `export-ignore`, `git check-attr` misses directory patterns, and both a worktree and a temporary index give a tag's whole tree.

The failure scenario of the chosen approach, six months on:

- A pull request marks a whole top-level entry `export-ignore`, say `/templates/`. The census reads the archive with the module's rule that a path under an entry the repository lacks is not read, so a skill's citation into `templates/` goes unread there, and CI stays green while `dist` lacks what the implement skill bootstraps from. Review of the `.gitattributes` line is what reads it, and the release's smoke run from the archive is what would show it. The module's docstring states this as a limit.
- Somebody pushes to `dist` by hand. The job reads `dist`'s tip at each run, so the next release's commit stands on the hand-made one and the directory gets a branch whose history holds a commit no tag made. A push is refused only where `dist` moves between the job's read of its tip and its push, and the job then goes red without rewriting anything.
- A tag is pushed by hand for an older version. The job adds a commit whose tree is the older release's, and the directory picks it up as the newest version. `dist_branch.py`'s docstring states this as a limit, since the hand-pushed tag is the repair path for a failed tag step and names the newest release there.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| `dist` built from `git archive` of the tag, the paths that leave marked `export-ignore` in `.gitattributes` | A whole top-level entry marked by mistake passes the census unread (*Technical context*). | Chosen. The owner chose the name and the mechanism on 2026-11-05, and the list lives in one file. |
| A list of what stays, held in the workflow | A path left off the list is missing from every listed copy, and nothing in the tree reads the listed copy, so nobody sees it. | Rejected, by the owner and for that scenario. |
| Replace the structure: move the plugin into a subfolder and submit it with the form's plugin path, which the directory reads alone (`claude.com/docs/plugins/submit`, *Update a published plugin*, read) | Every `${CLAUDE_PLUGIN_ROOT}` path in `hooks/hooks.json`, every plugin path `contract rule 11` resolves, `marketplace.json`'s `source` and every installed copy move at once, and the repository's own suite resolves the plugin from a new root. | Rejected. The premise that keeps the plugin at the root is checked: the directory reads the tracked branch at the plugin's path, and an empty path means the branch's root (read, the same page, *Submit a plugin*). So a branch holding only the plugin at its root answers the form at the cost of one job, where the move rewrites the tree. |
| Force-push `dist` as one orphan commit per release | The directory serves a scanned commit of the tracked branch, and a rewritten branch orphans the commit a listing is served from (`docs/releasing/branch-and-release.md` *Work accumulates on a release branch*). | Rejected, by the owner and for that scenario. |
| Each `dist` commit takes the tag as a second parent, so `dist`'s history links to `main`'s | A fetch of `dist` then fetches `main`'s whole history. Whether the directory reads history is not known here, and the size the form timed out on could return through it. | Rejected. The commit's message names the tag and its commit instead. |
| The census reads every citation the archive holds, with no top-level rule | The 14 citations that kept files make into `tests/` and `evals/` fail on the first run (executed, *Grounding*), and each would need an exemption kept beside the tree. They are a contributor's coordinates, which `contract rule 11` does not count among the plugin's paths. | Rejected for the module's own top-level rule applied to the archive. |
| The census reads membership through `git check-attr export-ignore` | `check-attr` answers `unspecified` for a file under a directory pattern such as `/tests/` (executed), so the reader would miss every directory the archive drops. | Rejected. The census reads the list of paths `git archive` writes. |
| One list for both questions: the hygiene step's version-bump roots and the paths `dist` holds | `docs/` is in `STAYS_HOME`, because a change to it alone needs no version bump, and `dist` holds it, because agents open it (read). One list would either demand a bump for every document edit or drop `docs/` from `dist`. | Rejected. The premise is checked: the two sets answer different questions. `test_every_top_level_entry_is_classified`'s message points at `.gitattributes` so both are decided where a new entry is met. |
| Keep `git archive` in the two readers of a tag's whole tree, with an attribute source that lifts `export-ignore` | `git --attr-source` and `GIT_ATTR_SOURCE` still drop the paths (executed). | Rejected for a checkout of the whole tree, by a worktree or a temporary index (both executed). |
| The `dist` step inside the `publish` job | A failure of the note step skips it, and its own failure reads as the note's. | Rejected for a job of its own, which `needs: publish` and conditions on the tag alone, so a re-run of a release whose note already exists still fills `dist`. |
| Name the branch `release` | git cannot hold `release` beside `release/vX.Y.Z`, and the `release` ruleset's `release/**/*` pattern and the release branches stand on that name (#1374's body). | Rejected, by the owner. |
| Leave `plugin_directory_check.py` reading pins against `main` alone | A marketplace pin of a `dist` commit reads "NOT reachable from main", which the message explains as a squashed release branch, and sends the reader after a defect that is not there. | Rejected. The pin is read against both refs. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 4 | `tests/evals/test_noninferiority.py` and `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, run narrow. The new `extract` case is shown red against the archive-based `extract`. The `release-report` command is run against a fixture tag marking paths `export-ignore`, and the phase record shows `.test_durations` there. | ec580f88 |
| 2 | Scope 1, 2 and 3 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/behaviour/test_the_release_check_watches_what_ships.py`, run narrow. The fixture case for a cited file marked `export-ignore` is shown red with the archive reading removed. The phase record names the git commands the archive reading runs and what an uncommitted change does to them. | c4ffaa78 |
| 3 | Scope 5, 6 and 7, and the row of `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`'s `LISTS_A_FIXTURE` that phase 1's case `tests/evals/test_noninferiority.py#test_leaves_the_repository_s_own_index_as_it_was` owes, with one for each new case of phase 3 that lists files | `tests/github/test_dist_branch.py`, the workflow-text case, and `tests/github/test_plugin_directory_check.py`, run narrow. Each new case is shown red against the code without its guard; the no-force case is shown red with a `--force` push in its place. The phase record holds the smoke run of Scope 7 from the extracted archive of HEAD, `executed`. | 6ee044c9 |

Scope 8, the rule changes, is written in `frame/design.md` and the settle applies it, so no phase builds it.

## Operational impact

- No new dependency and no new environment variable. The `dist` job uses the workflow's existing `contents: write` token, and the commit's author and committer follow `frame/questions.md` Q1.
- The first release after the merge, v0.32.3, creates `dist` as a root commit. Each later release adds one commit to it.
- GitHub's "Source code" zip and tarball of each release from v0.32.3 on lose `tests/`, `evals/`, `seal/`, `.test_durations` and `CLAUDE.md`. `/plugin marketplace add` and a user's CI clone are unchanged, since both read `main` or the tag through git, not an archive.
- `bin/test` in `dist` prints that it runs AgenticSeal's own suite and exits 2, because `dist` has no `tests/`.
- The owner's acts after the release, none of which the run waits on:
  - Enter `MichaelYcJo/AgenticSeal@dist` in the portal's form and read whether it answers, which is #1374's first *Done when* item. Submitting it there may also be the move of the Console listing to the portal, which the owner reads on the Console page (`docs/releasing/release-checklist.md` *6. After the merge*).
  - Install the plugin from `@dist` into a scratch repository and start a session, the live form of Scope 7's smoke run.
  - Optionally add a ruleset on `dist` that refuses force-pushes and deletion. The `dist` job pushes fast-forward only, so it needs no bypass for that rule. A rule that restricts who may update `dist` needs the workflow's actor as a bypass. Where the owner adds one, the ruleset table in `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* gains its row through a later rule change.
  - Delete `MichaelYcJo/agenticseal-dir-test`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-05 | Phase 3's spawn also writes the `LISTS_A_FIXTURE` row phase 1's index case owes, which phase 2 found failing at 1884ce52 and left to the orchestrator in `gaps.md` *Not done*. | The row is the same kind phase 3 owes its own cases that list files, in the same module, so one spawn writes both; a fix pass of its own would reopen phase 1 for one table row. | `skills/implement/SKILL.md` *3. The SDD file set*, a scope a spawn gives beyond the Delivers cell is folded into the plan before the spawn |
| 2026-11-05 | Round 1's `must` (the `dist` push carries `.github/workflows/`, which the workflow's token may not push) is answered by marking `/.github/workflows/` `export-ignore`, and the orchestrator folds *Scope* 1 and *Out* to it before the fix pass. Round 1's `should` on the `dist` job's `if:` goes to the same fix pass, which reads GitHub's documentation on a failed job's outputs before choosing between the `!cancelled()` condition and restating the four sentences. | The other answer to the `must`, a token with the `workflows` permission held as a secret, is a credential only the owner can create, and the run is under automation. No installed copy reads this repository's workflows: `seal pr-checks` writes from `templates/setup/hygiene.yml` (read). | `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*; `skills/core/SKILL.md` *Asking a person is the most expensive step* |
