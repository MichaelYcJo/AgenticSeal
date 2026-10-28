# Implementation Plan: 1793188384-the-release-notes-are-kept-twice

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

The release notes are written once, in each work item's `changelog.md`, and
published once, as the GitHub Release at the tag. The work removes the copy
in between. `.github/scripts/publish_release_note.py` reads the fragments
the release's commits added from the history at the tag, and opens the note
with the release's theme from its milestone. The gather script, its hygiene
step, `changelog/` and `CHANGELOG.md` go, after the 26 published notes that
lack their file's text are republished with it. The `update` skill confirms
a version from `plugin.json` and shows the GitHub Releases. The policy
root's sentences change through `frame/design.md`'s `## Rule changes`, and
the two test files its `check:` lines name stay with no case until the
settle.

## Technical context

- `.github/scripts/publish_release_note.py:541-556` reads
  `changelog/X.Y.Z.md` and refuses a tag without it.
  `:449-507` builds the body, and `:505` links the file at the tag.
  `.github/scripts/release_seal.py:88-91` loads this module by path and
  imports its glance helpers, which stay as they are.
- `.github/workflows/publish-release.yml` checks out with `fetch-depth: 0`,
  so every tag and commit the range reader needs is in the job. Its
  `permissions` block holds `contents: write` alone, and
  `tests/behaviour/test_a_release_publishes_its_note.py#test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit`
  refuses an `issues:` scope.
- `skills/settle/scripts/settle.py#released` judges a work item released by
  its directory's presence at a ref, and reads no `changelog/` file. So the
  settle is not affected by the removal (read).
- The settle can remove a release's own work items before its tag: the
  settle in `de11df75` did so for 0.22.4 (executed: `git ls-tree -r
  v0.22.4` lists no `changelog.md`). The range reader reads each fragment at
  the newest commit of the range that holds it, which is why that shape
  still gets its entries (executed: the reader's id set equals each released
  file's markers for 0.19.0 to 0.23.1).
- The installed `update` skill that runs an update is the old version's.
  An installed copy at 0.23.1 or earlier greps `CHANGELOG.md` in the new
  install at step 2b and finds no file. `frame/questions.md` Q1 holds the
  choice.
- **The chosen approach's failure scenario, six months on.** A release is
  tagged while an earlier version tag is missing, or is not merged into the
  tagged commit's first parent. The range then reaches back past the
  earlier release, and the note carries both releases' fragments. Nothing
  fails: the note is visibly too long on the releases page, and one
  `gh release edit` repairs it. A tag pushed by hand on a commit outside
  `main`'s first-parent line meets the same shape.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Read the fragments the range's commits added, each at the newest commit of the range that holds it (chosen) | A missing or unmerged previous version tag widens the range, and the note carries a second release's fragments. Visible on the page, repaired by one edit | Chosen. It matched every released file's markers for eleven releases, the settle-before-tag release included, and it needs no file written before the tag, which #1117's removal of the preparation commit requires |
| Read the fragments in the tree at the tag, net of the previous tag (`git diff --diff-filter=A <prev> <tag>`) | A settle in the release's own range removes the release's fragments before the tag, and the note has none. 0.22.4 is that shape, measured: zero fragments against nine markers | Rejected: it fails on a shape the history already holds |
| Build the notes before the settle, in the preparation commit, and read that file at the tag | The file is the gathered copy this issue removes, kept under another name, and #1117 removes the preparation commit that would write it | Rejected |
| Keep `changelog/` and `CHANGELOG.md` (the structure kept). Premise that would keep them: an agent or a person works from the tree's copy | Two copies drift. They already have: `seal/follow-up.md:47` and `:49` record two 0.12.2 sentences corrected in the fragments and never in the released file. The premise was checked and is false: outside the release scripts, CI, the tests that pin them and the documents that describe the gather, the readers are the `update` skill, four sentences that cite a release by its file (`skills/verify/orchestration.md` three times and `session_cost.py`'s message) and the two follow-up rows (executed, `git grep -n -E 'changelog/\|CHANGELOG\.md'`) | Rejected |
| Replace the hygiene step with a check at the release pull request: the release adds a fragment, and every fragment closes its blocks | It keeps the #584 refusal for a reader that no longer exists. A fragment left with an open fence hides the fragments after it in the rendered note, which shows on the page and is repaired by one edit; the refusal was added from a review round's finding on #584 (read: `gather_changelog.py`'s docstring cites round 1's finding 1), not from a release that shipped broken | Rejected. The empty range is still refused, at the tag (S5), where the old note refused a missing section |
| Keep the #586 refusal of a fragment line starting `## ` | Nothing ends a section at a `## ` line any more: the fragments are rendered whole inside the folded block | Rejected: the hazard it guarded is gone with `section_body` |
| Take the theme from the release pull request's title, the `symptoms:` line the title already reads | The title already carries it, so the theme would repeat the title on the same page | Rejected: the issue names the milestone's description, and the owner decided it |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The note from the fragments. `publish_release_note.py` gains the range, fragment, theme and section functions of `frame/design.md` *Data & interfaces*, and loses the release-file reader, the gather advice and the link line. Its docstring and `publish-release.yml`'s header comment say where the body comes from. `tests/github/test_publish_release_note.py` loses the gatherer and the release-file fixture, its A1 and A3 cases are re-pointed, and S1 to S6 are added | S1 to S6, each seen red against the script at `8a1173c8`. `tests/github/test_publish_release_note.py`, `tests/behaviour/test_a_release_publishes_its_note.py` and `tests/github/test_release_seal.py` run green | 270e8fa9 |
| 2 | The `update` skill. Step 2b reads the installed `plugin.json`'s `version`, and step 3 reads the GitHub Releases from the public API with no token, as `frame/design.md` *Scope* item 6 says | S7 and S8, each seen red against the skill at `8a1173c8`. `tests/behaviour/test_release_hygiene.py` runs green | |
| 3 | The gather goes. `.github/scripts/gather_changelog.py`, its hygiene step, the step's rows in `broad_gate.py`, `tests/conftest.py#gathered_entry`, and the gather's mentions in the comments and docstrings `## Removes` lists. `tests/github/test_gather_changelog.py` and `tests/text/test_the_changelog_is_gathered_at_release.py` keep a docstring and no case, the first with one caseless class carrying `second-gather-appends` | S9 and S10. `bin/seal rules --check` exits 0. `tests/behaviour/test_the_gate_names_every_step_ci_runs.py`, `tests/github/test_rules.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/skills/test_unverified_check.py` and `tests/github/test_issue_claims_check.py` run green | |
| 4 | The files go. `changelog/` and `CHANGELOG.md` are removed, with every reader `## Removes` lists outside `docs/`: the release hygiene cases, the chain-hooks case, the sealer case's changelog span, the census entries and fixtures, `RENAMED_RECORDS`, `STAYS_HOME`, the `session_cost.py` message and its pin, `skills/verify/orchestration.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `skills/implement/SKILL.md`, `skills/settle/SKILL.md` and the two `seal/follow-up.md` rows. This work item's `changelog.md` is written, carrying the sentence `frame/questions.md` Q1's default asks for | S12's grep, its hits recorded in the phase record. `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/test_censuses.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_the_release_check_watches_what_ships.py`, `tests/skills/test_session_cost.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` run green | |
| 5 | The 26 notes republished. The orchestrator does this, not `crafter`, because contract rule 6 withholds a post from every agent. For each version *Scope* item 5 lists, it appends the file's text read at its own tag, folded under `📋 Full changelog — what each change does and why`, below the note as it stands, with `gh release edit v<version> --notes-file`. It then re-runs the comparison over all 58 versions | S11: the comparison reports every note holding its file, recorded in this phase's record with the date it ran | |

## Operational impact

- **An installed copy at 0.23.1 or earlier reports a failed update once.**
  Its `update` skill, which is the one that runs the update to the release
  carrying this work, reads `CHANGELOG.md` in the new install at step 2b,
  finds no file, and stops with *a mismatch*. Its step 3 then has no
  `changelog/` file to read. The update has landed all the same, and the
  next update runs the new skill. Under Q1's default, this work item's
  `changelog.md` says so, in the release note the user is pointed at. Q1
  holds the alternative.
- **The republish writes 26 published notes once.** Each write appends
  and replaces nothing, so a note a person edited by hand keeps every word.
  The largest file is 34,778 bytes (executed, `wc -c changelog/*.md`),
  well under GitHub's limit for a release body.
- **The theme read is first exercised at the release carrying this work.**
  The case holds the code, and whether `contents: write` alone lets the
  job list the milestones is read in that tag run's log (Q3).
- **No new dependency, environment variable or workflow scope.** The
  update skill's step 3 reaches `api.github.com` without credentials,
  under the unauthenticated rate limit of 60 requests an hour, and it
  makes one.
- **The settle owes two deletions.** The settle that applies this work
  item's `## Rule changes` deletes
  `tests/github/test_gather_changelog.py` and
  `tests/text/test_the_changelog_is_gathered_at_release.py` in its pull
  request, because `settle` touches no file under `tests/`.
