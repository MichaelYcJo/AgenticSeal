# Phase 4: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 0c1144ef |

## What this phase was asked

Phase 4 of `frame/plan.md`, and only that phase. Write the work item's
`changelog.md` with the `### Fixed` entry and the `### Process changes` row,
in the shape `docs/the-record-layout.md` *A change writes fragments, never a
shared file* and `templates/records/process.md` give. In the same commit,
move `.claude-plugin/plugin.json` from `0.24.2` to `0.25.0`, because this is
the first pull request into `release/v0.25.0`. Any other file that states
the plugin's version and is held to `plugin.json` moves with it, where a case
requires it. The release note says that the core arrived, as the issue's
Done-when asks. `tests/github/test_publish_release_note.py` and
`tests/behaviour/test_release_hygiene.py` were to pass.

## What this phase found

**The frame held.** `git grep -n '0\.24\.2' -- ':!seal/threads'` printed
`.claude-plugin/plugin.json:4` and nothing else, and
`.claude-plugin/marketplace.json` holds no version, so no other file moved.
`origin/release/v0.25.0` is an ancestor of HEAD and its `plugin.json` still
says `0.24.2`, so this branch is the one that moves it.

**The fragment follows `frame/design.md` *Data & interfaces*: one `### Fixed`
entry, then one process row.** The removal of `bash install.sh --project` and
the move of the old block's rules are sentences of that entry. They are not
`### Removed` or `### Changed` sections, because the design names one entry.
The process row is the framer's draft, with the paths of the core and of
`CLAUDE.md` added.

**Two claims in the entry come from earlier records and were not measured
again.** The share a user's session reads from `~/.claude/CLAUDE.md`, 1,786 B
before and 6,810 B after, is `trail/phases/phase-3.md`'s. The double read by
an agent, about 2,100 tokens per spawn, is `gaps.md` *Not done*'s, and it
rests on #292's calibration, which phase 3 did not measure. The entry says
"should" for it and names #1183, and it says nothing that contradicts
`gaps.md`.

**Neither named module reads this fragment.** Both build their fragments
in fixture repositories. The fragment's shape was read instead by the
release note's own parser: `split_process` and `section` of
`.github/scripts/publish_release_note.py`, run over the file, lifted one
process row and left the `### Fixed` entry without the section.

**No case was written and no `seal mutate` ran.** The fragment is prose, and
the version is a value that the cases reading `plugin.json` already read; no
unit adds behaviour.

**The phase-boundary set passed.** It was one `bin/test -q` command over 54
modules: every test module that names `plugin.json`, `.claude-plugin`,
`changelog.md` or `seal/threads`, with the two named modules. It passed
3,880 cases and skipped 1.
