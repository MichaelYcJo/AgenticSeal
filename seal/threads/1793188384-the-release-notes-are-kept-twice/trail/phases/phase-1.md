# Phase 1: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 270e8fa9 |

## What this phase was asked

Build phase 1 of `frame/plan.md` against the frame at `49ca77ee`: the note
built from the fragments. `publish_release_note.py` gains the range,
fragment, theme and section functions of `frame/design.md` *Data &
interfaces*, and loses the release-file reader, the gather advice and the
link line. Its docstring and `publish-release.yml`'s header comment say where
the body comes from. `tests/github/test_publish_release_note.py` loses the
gatherer and the release-file fixture, its A1 and A3 cases are re-pointed,
and S1 to S6 are added, each seen red against the script at `8a1173c8`.
`frame/questions.md` Q3 stands on its default (a): the workflow's
`permissions` block is not changed.

## What this phase found

**The frame's coordinates held, and its measurement did not cover the
reader built (read; round 1 executed).** Every coordinate *Removes* gives
for `publish_release_note.py` and `test_publish_release_note.py` stood where
the frame says at `49ca77ee`, and `release_seal.py` imports none of the
removed names. This phase did not re-run the frame's 0.19.0 to 0.23.1
comparison against the reader it built. Round 1 did, and found the
per-path `git log` missed a fragment a settle removed on the release branch
when the tag is the merge into `main` (0.22.4, finding 1). The fix pass's
commit `d60ca012` adds `--full-history` and skips a fragment the range's
lower tag already holds.

**How S1 to S6 were seen red (executed).** The new module ran against the
script unchanged from `8a1173c8` (`git diff --quiet 8a1173c8 --` on the
script exited 0): 38 failed and 2 passed. The new cases failed because the
functions they call or patch did not exist; that red shows the behaviour was
absent and does not show which line holds it. So after the build commit,
`seal mutate` broke each added unit once, 18 mutants in one batch over the
module with `-x`: 18 red, 0 survived (`seal mutate` exit 0). The mutants cut
the first parent from the tag read, compared versions as strings, dropped the
previous tag from the range, read modified fragments as added, turned rename
detection on, skipped the tree check, kept empty fragments, joined entries
with one newline, matched any milestone, kept an empty description, read a
failed list as empty, kept the `Purpose:` label, stopped the sentence at any
`.`, read past the first line, kept the whitespace, kept the first letter's
case, dropped the theme line and published an empty range. That shows the
cases test what they cover. It does not show the reader safe on a shape no
case built: S1's history is linear and its tag is the settle commit.

**`release_body` changed its signature.** It is `release_body(theme,
rendered, pulls, owner)`. `repo` and `tag` fed only the link line, which is
gone. `tests/github/test_release_seal.py#note` calls it, so its one call
changed with it. The plan names that module only as one that runs green.

**S1 carries two shapes beyond the frame's wording.** Mutation showed that
nothing pinned `--no-renames` or the skip of an empty fragment. In S1's
history, the settle's commit now also adds a fragment with the removed
one's text and an empty fragment. The first is read as a rename without
`--no-renames`, and the second must give no entry. Both mutants went red
with these shapes in place.

**The milestone's first line is read through `blocks.gfm_lines`.** The
census case in the module refused `.splitlines(` on a description a person
writes. The `git log` output is split with `.splitlines(` under the
exemption comment other scripts in `.github/scripts/` use.

**Three printed lines changed.** The list failure now says the note is "the
theme line and the fragments alone". The empty range names the range it
read, and a tag that is not `vX.Y.Z` no longer names a changelog section.
`test_the_list_is_read_from_the_release_branch` now pins the first. S5 pins
the second, and the existing `not a vX.Y.Z tag` assertion still holds the
third.

**The workflow's checkout comment named the old reason for
`fetch-depth: 0`.** It now names the range read. Leaving it would have left a
comment stating a fact the change removed.

**A limit, not guarded.** A description that is only the `Purpose:` label
gives an empty theme. The job then logs `no theme line: the milestone
`release: X.Y.Z``, which names the milestone but not why it gave no line.
No release milestone has that shape (read: the frame's milestone reading,
2026-10-28).
