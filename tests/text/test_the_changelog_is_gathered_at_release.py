"""No case: the changelog gather is gone, held until work item 1793188384's settle.

Work item 1793188384-the-release-notes-are-kept-twice (#1053) removed
`.github/scripts/gather_changelog.py`, `changelog/` and `CHANGELOG.md`: the
release note is built at the tag from the fragments the release's commits
added and the previous tag does not already hold
(`tests/github/test_publish_release_note.py`). The cases here read the
hygiene step that ran the gather's check, the documents that sent a change to
its gathered file, and this repository's gathered files, and every one of
them is gone.

`docs/the-record-layout.md` and `docs/release-checklist.md` still name this
file on their `check:` lines. The policy root changes only at the settle
that writes that work item's `## Rule changes`, and `seal rules --check`
refuses a target that does not resolve. So the file stays with no case until
then. Nothing removes it on its own, because `settle` touches no file under
`tests/`: the pull request that settles that work item deletes it.
"""
