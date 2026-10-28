# Guarantee: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Target SHA | 65b3fabc against faf093f1 |
| Broad gate | 782f24a3 against faf093f1 |

The base `release/v0.24.0` resolves to `faf093f1` through
`release/v0.24.0@{upstream}` (executed). `trail/gate.md` names `782f24a3`,
an ancestor of HEAD, and the one commit after it, `65b3fabc`, touches only
`seal/threads/1793188384-the-release-notes-are-kept-twice/trail/gate.md`
(executed: `git log --no-merges --name-only 782f24a3..HEAD ^faf093f1`).
`seal pr-body 1793188384-the-release-notes-are-kept-twice --body <file>
--check` exited 0, from both the tree's `bin/seal` and the installed one
(executed). Every `seen red` below ran in a clone at
`<scratchpad>/1793188384-the-release-notes-are-kept-twice/at-base/`, with
the named file restored by `git checkout` and checked back to HEAD after the
run. The clone is removed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1 to S6 fail against the script before the change | `trail/phases/phase-1.md` *How S1 to S6 were seen red* | `git checkout faf093f1 -- .github/scripts/publish_release_note.py`, then `bin/test -q -p no:xdist` on the S1, S2, S4, S5, S3 and S6 cases of `tests/github/test_publish_release_note.py` | holds (executed): 13 failed, on `AttributeError` for the missing `theme_of`, `previous_tag` and the patched functions. All 16 sampled cases pass at HEAD |
| S7 and S8 fail against the skill before the change, on their first assertions | `trail/phases/phase-2.md` *How S7 and S8 were seen red* | `git checkout faf093f1 -- skills/update/SKILL.md`, then the two cases of `tests/behaviour/test_release_hygiene.py` | holds (executed): S7 fails on `'CHANGELOG.md' not in`, and S8 fails on `'https://api.github.com/repos/' in` |
| The merge-tag case failed against the phase 1 build with `assert [] == [('1700000001-first', '- first entry')]` | `trail/rounds/round-1.md` finding 1 *answer* | `git checkout 270e8fa9 -- .github/scripts/publish_release_note.py`, then `Test_module::test_a_fragment_the_settle_removed_reaches_a_note_tagged_on_a_merge` | holds (executed): it fails with that assertion, and passes at HEAD |
| The `session_cost.py` pin goes red on the old message | `trail/phases/phase-4.md` *How the changed pins were seen red* | `git checkout faf093f1 -- skills/verify/scripts/session_cost.py`, then `tests/skills/test_session_cost.py::Test_main::test_the_reading_says_its_family_rows_moved_at_377` | holds (executed): it fails on `'#377, which its release note names' in`, and passes at HEAD |
| S11: `v0.23.1` holds `changelog/X.Y.Z.md` for all 58 versions | `trail/phases/phase-5.md` *S11* | `git cat-file -e v0.23.1:changelog/<version>.md` over every `v*` tag | holds (executed): 58 tags, 0 missing |
| None of the 26 notes holds the appended block after the restore | `trail/phases/phase-5.md` *The published notes after the restore*; `frame/questions.md` Q2 Status | `gh api --paginate 'repos/MichaelYcJo/AgenticSeal/releases?per_page=100'`, a read, at 2026-10-28T15:37:08Z by the machine clock | holds (executed): 58 releases. None of the 26 holds the summary `📋 Full changelog` or a `<details` block, and each `updated_at` equals the phase record's table. The summary stands in v0.15.1 to v0.23.1 alone |
| Each restored note equals its backup but for a trailing newline | the spawn prompt; no record holds the comparison | none: the backups are not in the tree | unverified. The orchestrator answers it, holding the backups |
| Every `## Removes` row stands nowhere in the tree | `frame/design.md` *Removes* | `test -e` on the gather script, `changelog/` and `CHANGELOG.md`; `grep` of each row's names at its coordinate | holds (executed): every path is gone, and no row's name is found where the row places it. The two emptied modules hold no `def test_`, and `second-gather-appends` stands on one caseless class |
| No removal the changelog names stands | `changelog.md` *Removed* | the same checks, and `grep -n -i "gather\|changelog" .github/workflows/hygiene.yml skills/verify/scripts/broad_gate.py` | holds (executed): no match |
| S12: no living text outside `docs/` and `seal/` sends a reader to `changelog/` or `CHANGELOG.md` for the notes | `trail/phases/phase-4.md` *S12's grep* | `git grep -n -E 'changelog/\|CHANGELOG\.md'` outside `docs/`, `seal/` and the two emptied modules | holds (executed): `.test_durations:1107` and the assertions and docstrings the phase table judges, at their lines today |
| The check lines and the layout hold | `trail/rounds/round-9.md` last confirmation | `bin/seal rules --check`, `bin/seal layout --check` | holds (executed): exit 0 and exit 0 |
| `gaps.md` *Not done*: `skills/implement/orchestration.md:530` and `:578` "still state the gather", Q4's default (a) leaves the file alone, and the orchestrator names the sentences in the pull request body | `gaps.md:32` | `git grep -n -i -E "gather\|changelog marker\|CHANGELOG\.md\|changelog/" -- skills/implement/orchestration.md`; `git diff 9477538d 0ae4229a -- skills/implement/orchestration.md` | does not hold (executed). Phase 6's `0ae4229a` rewrote `:529-530` to "the accumulated entries go out under it" and `:577-578` to "the marker the release note carries above that fragment". Only `:538` and `:541` match, which phase 6 kept as a host repository's convention. Q4's Status says (a) can no longer be taken. The orchestrator's part of the body is `Closes #1053` and names no sentence |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | The note is built at the tag from the fragments with a theme line; the gather, `changelog/` and `CHANGELOG.md` go; no published note is republished (Q2); `frame/plan.md` phase 6 rewrites the gather sentences of `skills/implement/orchestration.md` | the build, the changelog, the issue except its republish clause, the tree | itself: `frame/design.md:127-130` still lists `skills/implement/orchestration.md:530` and `:578` as out of scope under Q4, which `frame/plan.md:75` and Q4's Status contradict, and the tree at `0ae4229a` contradicts (read) |
| the build | Six phases and their fix passes, each phase record naming its commit; phase 6 rewrites `:530` and `:578` and keeps `:538` and `:541` | the diff `faf093f1...HEAD`, the cases re-run above, the release listing | the build's own closing memo: `gaps.md:32` *Not done* still says the four sentences stand and the file is #1041's |
| the last round | `trail/rounds/round-9.md`: round 8's finding 1 closed at `c6730b99`, nothing opened | the tree at `afc53ac5` for what it checked, and the gate record | none on its own findings. It carried round 8's reading of phase 6 and did not re-read `gaps.md` *Not done*, which neither round opened |
| the changelog | The note is built from the fragments at the tag with a theme line; the update skill reads `plugin.json` and the GitHub Releases; an update from 0.23.1 or earlier reports one mismatch; `changelog/`, `CHANGELOG.md` and the gather are gone and readable at `v0.23.1` | the diff, S1 to S8 at HEAD, S11, `skills/update/SKILL.md` steps 2b and 3 (read) | none |
| the orchestrator's part of the pull request body | `Closes #1053` | the spec under Q2's answer, which the body's *Questions* row carries | the body's *Not done* part, copied from `gaps.md:32`, says the orchestrator "names the sentences in the pull request body"; this part names none, and the tree has no such sentences left to name |

**Whether `Closes #1053` stands.** The issue's *Done when* asks that "every
released version's GitHub Release holds its notes", and 26 Releases do not
hold their file's text (executed above). Q2's Status records the owner's
answer of 2026-10-28: no note is republished, because every file stays
readable at `v0.23.1`. I read that answer as the owner's, and it decides
the one clause the build departs from. S11 holds what the clause protects:
the notes of all 58 versions remain reachable. So the close is decided, not
undecided, and `Closes #1053` stands once the finding below is fixed. The
issue carries no comment and has not been edited since 2026-10-27
(executed), so a reader of the closed issue finds an unmet clause with no
note of the departure. Whether that departure goes on the issue is left to
the owner.

**What the orchestrator fixes, and nothing else.** The class is the
records that still state Q4's default (a) after phase 6 took the file. Two
instances were found (executed: `git grep` for `#1041`, `Q4` and the four
coordinates over this work item's records, the round records left out). One
is `gaps.md:32`, the crafter's closing memo: its first *Not done* paragraph
is false at HEAD and goes, or is rewritten to what phase 6 did. The other
is `frame/design.md:127-130`, the orchestrator's frame: its out-of-scope
bullet goes, or names phase 6. `trail/phases/phase-3.md:20` stands, since
it quotes what phase 3 was asked. After the fix, `seal pr-body` is re-run so
the body's *Not done* part drops the sentence, and this audit is re-run on
the new HEAD. The `gaps.md` *Not verified* row "The full suite, the
repository-wide lint and the typecheck over this branch" was answered by
the gate at `782f24a3`. It is no ground for this verdict, and it can close
in the same pass.

Verdict: withheld reason: gaps.md:32, the crafter's Not done paragraph that the pull request body copies, says skills/implement/orchestration.md:530 and :578 still state the gather and Q4's default (a) leaves the file to #1041, while 0ae4229a rewrote both lines at :529-530 and :577-578 and Q4's Status says (a) can no longer be taken; frame/design.md:127-130 states the same out-of-scope reading
