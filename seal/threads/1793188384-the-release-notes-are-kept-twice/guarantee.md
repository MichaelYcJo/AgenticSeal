# Guarantee: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Target SHA | d1bdc2a6 against faf093f1; earlier run: 65b3fabc withheld |
| Broad gate | b80ea124 against faf093f1 |

The base `release/v0.24.0` resolves to `faf093f1` through
`release/v0.24.0@{upstream}` (executed). `trail/gate.md` names `b80ea124`,
an ancestor of HEAD, and the one commit after it, `d1bdc2a6`, touches only
`seal/threads/1793188384-the-release-notes-are-kept-twice/trail/gate.md`
(executed: `git log --no-merges --name-only b80ea124..HEAD ^faf093f1`).
`seal pr-body seal/threads/1793188384-the-release-notes-are-kept-twice
--body <file> --check` exited 0, from both the tree's `bin/seal` and the
installed one (executed). The commits since the earlier run's `65b3fabc`
change four files, all under this work item's directory: `frame/design.md`,
`gaps.md`, `guarantee.md` and `trail/gate.md` (executed: `git diff --stat
65b3fabc HEAD`). So this run re-runs the claims whose coordinates those
commits touched, and carries the rest from the earlier run, whose results
stand on code no commit since has changed. No `seen red` was re-run in this
run, so no clone was made.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The earlier withheld finding is fixed: `gaps.md` *Not done* no longer says `skills/implement/orchestration.md` still states the gather or that the file is #1041's, and `frame/design.md` no longer lists that file as out of scope under Q4 | `b80ea124`'s commit message; the spawn prompt | `git diff 65b3fabc HEAD -- frame/design.md gaps.md`; `git grep -n -E '#1041\|Q4\|orchestration\.md\|:530\|:578\|:538\|:541'` over this work item's records, the round records and `guarantee.md` left out | holds (executed). The paragraph and the bullet are removed. The hits left are `frame/plan.md:75` (phase 6, "which #1041 owned while it ran"), `frame/questions.md:50` (Q4, whose Status says (a) can no longer be taken), `trail/phases/phase-3.md:19-20` (what phase 3 was asked) and `trail/phases/phase-6.md`, each true at HEAD |
| Phase 6 rewrote the gather sentences of `skills/implement/orchestration.md` and kept `:538` and `:541` as a host repository's convention | `trail/phases/phase-6.md:29-30`, `:46` | `git grep -n -i -E "gather\|changelog marker\|CHANGELOG\.md\|changelog/" -- skills/implement/orchestration.md` | holds (executed): only `:538` and `:541` match, as the phase record keeps them |
| `gaps.md` *Not verified*: the full suite, the lint and the typecheck closed by the gate at `782f24a3` against `faf093f1`, passed | `gaps.md:26` | read of `trail/gate.md` | holds (read): `trail/gate.md` names `782f24a3 against faf093f1` as the earlier run, and the newest run, `b80ea124`, covers the two record commits after it |
| Each of the 17 restored notes equals its backup but for one trailing newline | the spawn prompt; `frame/questions.md:48` Q2 Status says each was restored from its backup | `cmp -s <(gh release view vX.Y.Z --repo MichaelYcJo/AgenticSeal --json body --jq .body) <(cat note-X.Y.Z.md; printf '\n')` over v0.2.0, v0.3.0 to v0.7.0, v0.8.0 to v0.8.3, v0.9.0 to v0.9.5 and v0.10.0, the backups read from the orchestrator's `scratchpad/1053-republish/`, at 2026-10-28T15:43:05Z by the machine clock | holds (executed): 17 of 17 exit 0, `gh` adding the one newline. No backup holds a `<details` block or the `📋 Full changelog` summary (executed: `grep`). The `**Full changelog**` lines of v0.6.0, v0.7.0, v0.8.0, v0.8.2 and v0.9.0 are their own hand-written links, which their `new-` files keep above the appended block (read). That the backups were read before the edit rests on the orchestrator: each `note-` file carries the same mtime as its `new-` file, 2026-10-28T22:53:33+0900 for 0.3.0 (read) |
| The check lines and the layout hold | `trail/rounds/round-9.md` last confirmation | `bin/seal rules --check`, `bin/seal layout --check` | holds (executed): exit 0 and exit 0 |
| S1 to S6 fail against the script before the change | `trail/phases/phase-1.md` *How S1 to S6 were seen red* | carried from the earlier run: `git checkout faf093f1 -- .github/scripts/publish_release_note.py` in a clone, then the six cases of `tests/github/test_publish_release_note.py` | holds (executed at `65b3fabc`): 13 failed on `AttributeError`, and all 16 sampled cases passed at HEAD. No commit since touches the script or the module |
| S7 and S8 fail against the skill before the change, on their first assertions | `trail/phases/phase-2.md` *How S7 and S8 were seen red* | carried: `git checkout faf093f1 -- skills/update/SKILL.md` in a clone, then the two cases of `tests/behaviour/test_release_hygiene.py` | holds (executed at `65b3fabc`): S7 failed on `'CHANGELOG.md' not in`, S8 on `'https://api.github.com/repos/' in`. No commit since touches either file |
| The merge-tag case failed against the phase 1 build with `assert [] == [('1700000001-first', '- first entry')]` | `trail/rounds/round-1.md` finding 1 *answer* | carried: `git checkout 270e8fa9 -- .github/scripts/publish_release_note.py` in a clone, then `Test_module::test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge` | holds (executed at `65b3fabc`): it failed with that assertion and passed at HEAD |
| The `session_cost.py` pin goes red on the old message | `trail/phases/phase-4.md` *How the changed pins were seen red* | carried: `git checkout faf093f1 -- skills/verify/scripts/session_cost.py` in a clone, then `tests/skills/test_session_cost.py::Test_main::test_the_reading_says_its_family_rows_moved_at_377` | holds (executed at `65b3fabc`): it failed on `'#377, which its release note names' in` and passed at HEAD |
| S11: `v0.23.1` holds `changelog/X.Y.Z.md` for all 58 versions | `trail/phases/phase-5.md` *S11* | carried: `git cat-file -e v0.23.1:changelog/<version>.md` over every `v*` tag | holds (executed at `65b3fabc`): 58 tags, 0 missing. Tags are not this branch's commits |
| None of the 26 notes holds the appended block after the restore | `trail/phases/phase-5.md` *The published notes after the restore* | carried: `gh api --paginate 'repos/MichaelYcJo/AgenticSeal/releases?per_page=100'`, a read, at 2026-10-28T15:37:08Z | holds (executed at `65b3fabc`): none of the 26 held the summary or a `<details` block. The 17 edited ones equal their backups now (the row above) |
| Every `## Removes` row and every removal the changelog names stands nowhere in the tree | `frame/design.md` *Removes*; `changelog.md` *Removed* | carried: `test -e` on the gather script, `changelog/` and `CHANGELOG.md`, `grep` of each row's names at its coordinate | holds (executed at `65b3fabc`). No commit since touches a path outside this work item's directory |
| S12: no living text outside `docs/` and `seal/` sends a reader to `changelog/` or `CHANGELOG.md` for the notes | `trail/phases/phase-4.md` *S12's grep* | carried: `git grep -n -E 'changelog/\|CHANGELOG\.md'` outside `docs/`, `seal/` and the two emptied modules | holds (executed at `65b3fabc`). `CLAUDE.md:33` reads "History goes to git, the release notes and the work record" (read at HEAD), as the issue's *The change* asks |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | The note is built at the tag from the fragments with a theme line; the gather, `changelog/` and `CHANGELOG.md` go; no published note is republished (Q2's answer); `frame/plan.md` phase 6 rewrites the gather sentences of `skills/implement/orchestration.md`, and Q4's Status says (a) can no longer be taken | the build, the changelog, the issue except its republish clause, the tree at HEAD | none. The out-of-scope bullet that gave the file to #1041 is gone (executed above) |
| the build | Six phases and their fix passes, each phase record naming its commit; phase 6 rewrites `:530` and `:578` and keeps `:538` and `:541`; `gaps.md` *Not done* names only #950's `fold_ledger` leftover | the diff `faf093f1...HEAD`, the cases re-run, the release listing, the 17 restored notes | none. `gaps.md` *Not done* no longer says the file is #1041's (executed above) |
| the last round | `trail/rounds/round-9.md`: round 8's finding 1 closed at `c6730b99`, nothing opened | the tree at `afc53ac5` for what it checked; the commits since touch only this work item's records | none on its own findings |
| the changelog | The note is built from the fragments at the tag with a theme line; the update skill reads `plugin.json` and the GitHub Releases; an update from 0.23.1 or earlier reports one mismatch; `changelog/`, `CHANGELOG.md` and the gather are gone and readable at `v0.23.1` | the diff, S1 to S8, S11, `skills/update/SKILL.md` steps 2b and 3 (read at `65b3fabc`, unchanged since) | none |
| the orchestrator's part of the pull request body | `Closes #1053` | the spec under Q2's answer, which the body's *Questions* row carries, and the body's *Not done* part, which no longer asks the orchestrator to name any sentence | none. Round 1's finding 4 answer, copied into the body, says `:578` "is #1041's under Q4"; it was true when that round ran, before `9477538d`, and the body's Q4 row states the change (read) |

**Whether `Closes #1053` stands.** The issue's *Done when* asks that "every
released version's GitHub Release holds its notes", and 26 Releases do not
hold their file's text. Q2's Status records the owner's answer of
2026-10-28: no note is republished, because every file stays readable at
`v0.23.1`. I read that answer as the owner's. S11 holds what the clause
protects, and the 17 notes edited on 2026-10-28 are back to their text
before the edit (executed above). So `Closes #1053` stands. The issue has no
comment and was last updated 2026-10-27T02:26:00Z (executed: `gh issue
view 1053`), so a reader of the closed issue finds the republish clause
with no note of the departure. Whether that departure goes on the issue is
left to the owner.

Verdict: sealed
