# Phase 4: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 449e5864 |

## What this phase was asked

Build phase 4 of `frame/plan.md`: the files go. `changelog/` and
`CHANGELOG.md` are removed, with every reader `## Removes` lists outside
`docs/`: the release hygiene cases, the chain-hooks case, the sealer case's
changelog span, the census entries and fixtures, `RENAMED_RECORDS`,
`STAYS_HOME`, the `session_cost.py` message and its pin,
`skills/verify/orchestration.md`, `CLAUDE.md`, `CONTRIBUTING.md`,
`skills/implement/SKILL.md`, `skills/settle/SKILL.md` and the two
`seal/follow-up.md` rows. This work item's `changelog.md` is written,
carrying the sentence `frame/questions.md` Q1's default (a) asks for: an
update from 0.23.1 or earlier reports a mismatch once at step 2b, the update
has landed, and the installed copy's `.claude-plugin/plugin.json` names the
version. S12's grep runs at the close, its hits recorded here. Phase 5, the
republish of the 26 notes, is the orchestrator's and is not built here.

## What this phase found

**S12's grep (executed at `268480ac`, and at `449e5864` with the same
hits).** `git grep -n -E
'changelog/|CHANGELOG\.md'` outside `docs/`, `seal/` and the two emptied
test files finds eight lines. None sends a reader to those paths for the
notes:

| Hit | What it is |
|---|---|
| `.test_durations:1107` | the test runner's cache, naming a parameter id that no longer exists. The frame leaves the file to the runner |
| `tests/behaviour/test_release_hygiene.py:1051`, `:1057`, `:1100` | S7 and S8: the docstring saying step 2b read `CHANGELOG.md` until #1053, and two assertions that step 2b and step 3 name neither path |
| `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:685` | the docstring saying #1053 removed `changelog/` and the entry is the v0.20.0 release note's |
| `tests/github/test_publish_release_note.py:246`, `:258`, `:302` | A1 and S1: assertions, and S1's docstring, that the note names no `changelog/` path |

Under `seal/`, `seal/follow-up.md` names `changelog/0.12.2.md` read at
`v0.23.1` as the folded text of the v0.12.2 release note, which is where the
frame moved its coordinate.

**The frame does not hold on where a released file is read (executed).**
`frame/design.md` *Scope* items 5 and 8, S11 and `frame/plan.md`'s phase 5
row read each file "at its own tag", `git show vX.Y.Z:changelog/X.Y.Z.md`.
`git cat-file -e` over the 58 version tags finds a tag's own file at 14
tags, `v0.18.1` to `v0.23.1`, and at none of the 44 before them: #770 split
`CHANGELOG.md` into the per-release files on 2026-10-04. All 26 versions the
republish covers are among the 44. `v0.23.1` holds all 58 files, identical
to `49ca77ee`'s (`git diff --quiet v0.23.1 49ca77ee -- changelog/
CHANGELOG.md` exit 0). `449e5864` makes this work item's `changelog.md` and
the two `seal/follow-up.md` rows name `v0.23.1`, and phase 5 and S11 read
each file there. The frame is left as it stands; `gaps.md` holds the
divergence.

**How the changed pins were seen red (executed).** After the build commit,
`seal mutate` put `session_cost.py`'s old words back ("which its file under
`changelog/` names"), and `test_the_reading_says_its_family_rows_moved_at_377`
went red. It then replaced the illustrative-version case's read of the tags
with a set holding `1.2.3`, and the case went red. Both runs exited 0, the
mutant noticed. The removed cases need no red: nothing of what they read
remains.

**The illustrative-version case reads the tags.** `shipped_versions` read
`CHANGELOG.md`'s headings. The case now asks `shipped_tags`, which the
module's own docstring already named as the truthful source for *shipped*.
Its message for an empty set says no `v*` tag is readable, as the
neighbouring tag case does.

**`RENAMED_RECORDS` is one prefix now.** With `"changelog/"` removed, the
loop that asserted every record prefix but `seal/threads/` holds a tracked
file iterated over nothing. The loop and `SETTLED_RECORDS` went, and the
comment and docstring say why. `gaps.md` holds this and the three docstrings
in `tests/behaviour/test_release_hygiene.py` that `## Removes` did not list.

**The `CONTRIBUTING.md` paragraph is one sentence and a pointer.** *House
rules* said one branch writes the changelog. It now says no branch writes
the release notes, and points at `docs/branch-and-release.md` *Work
accumulates on a release branch*, the section `## Rule changes` rewrites.
Until the settle that section still describes the gather, which is how the
policy root reads between a merge and its settle.

**The two `seal/follow-up.md` rows keep their question and answerer.** Each
names the v0.12.2 GitHub Release as the released copy and `changelog/0.12.2.md`
at `v0.12.2` as its folded text. Each says a published note is never rebuilt,
where it said the gather decides by marker. The `CONTRIBUTING.md` rule each
cited is now in the past tense, because that rule is gone.

**The run over every module naming a changed path (executed).** 75 modules,
`bin/test -q`: 2913 passed, 10 skipped, exit 0. `bin/seal layout --check`
and `bin/seal rules --check` exited 0, and `ruff check` and `ruff format
--check` over the phase's Python files exited 0.
