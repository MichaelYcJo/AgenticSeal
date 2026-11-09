# Phase 4: 1794187229-the-body-carries-the-seal-mark

## What this phase found

**The frame holds for this phase.** `pr_body.py#_mark_line` built
`<repository>/raw/v<version>/<icon>` and `MARK_FIELDS` read
`("repository", "version", "icon")`, as G21 states (read at `7e6caa2e`).
`templates/setup/config.md` *The seal mark* held the sentence *Removes*
quotes, and one more sentence on the old fact: the paragraph's first
sentence said the line is "the plugin's icon at the tag of the plugin's
version" (read). `tests/skills/test_pr_body.py` held the `version` row of the
manifest-field parametrization and a `MARK_LINE` fixture at `raw/v1.2.3`
(read).

**Decision: the two-manifest case sits in `Test_seal_mark` and reads
`seal_mark`, not `_mark_line`.** The group's cases call `seal_mark` with a
manifest path, and S10 is about the line `seal pr-body` writes. Two
manifests that differ in `version` alone must give one line. The case
collects the two lines into a set and compares it with the one
`raw/HEAD` line, so a failure shows both lines. Judged against
`frame/design.md` *Scope* item 6, "a case shows two manifests differing in
`version` alone compose one mark line".

**Seen red.** The case ran red against `_mark_line` as it stood before this
phase, with the tag address (executed, `bin/test`). The left set held
`raw/v1.2.3` and `raw/v9.9.9`. It ran green after the change.

**Sentences on the old fact, rewritten in `429582c3`.** The list covers
every sentence the frame names and every one `git grep` found outside the
work item's records on `raw/v`, `tag of the` and `version's tag`. It is a
sample of the class "every sentence in the tree that says what the mark's
address names" (rule 12). The searches reached the whole tree, so the part
they did not reach is a sentence that says the same thing in other words.

- `pr_body.py`'s module docstring and `_mark_line`'s docstring now say
  that the address names no version, and why.
- `templates/setup/config.md` *The seal mark*: the paragraph's first
  sentence now names the icon at the default branch of the plugin's
  repository. The *Removes* sentence is rewritten in place, as *Removes*
  says: the image shows while the repository stays public and the icon
  stays at its path on the default branch.
- `test_pr_body.py`: the comment above the `MANIFEST` fixture said the
  fixture held "the three fields the mark's address is built from". The
  address now reads two of them. The fixture keeps `version`, which the
  two-manifest case varies, and the comment says so.

`docs/forms/the-guarantee.md` line 40 still says the mark is the icon "at
the tag of the plugin's version". It is in the policy root, and
`frame/design.md` `## Rule changes` rewrites it at the settle, as phase 3
left the other policy sentences (read).

**`git grep` finds no `raw/v` and neither *Removes* sentence outside the
work item's records** (executed, exit 1 for each, at `429582c3`).

**Mutations, after the commit** (executed, `bin/seal mutate`, both red):

- The address with the version put back,
  `raw/v{fields.get('version')}`, run against the two-manifest case: red.
  The left set held `raw/v1.2.3` and `raw/v9.9.9`.
- `MARK_FIELDS` without `icon`, run against
  `test_refuses_a_manifest_lacking_a_field`: the `icon` row went red with
  a `KeyError` in place of the note naming the field.

**The mark line this tree's `bin/seal pr-body` writes equals the one
`chain_check.py` composes** (executed, one run of a probe deleted after it
ran). The probe took `tests/skills/test_chain_check.py`'s `bodied` fixture,
a work item sealed at HEAD under a `yes` row. It ran this tree's
`bin/seal pr-body --body <file> <item>` as a subprocess. The body file it
wrote held one mark line, equal to `test_chain_check.py#MARK`, which is
`pr_body.py#_mark_line` on the plugin's own manifest. The whole body equaled
the fixture's composed `late` body, and the check's body arm printed nothing
over it, with exit 0. The plugin's own line is
`<img src="https://github.com/MichaelYcJo/AgenticSeal/raw/HEAD/.claude-plugin/icon.png" alt="Sealed" width="128">`
(executed).

**What the change leaves standing.** The arm of this release refuses a body
written by an installed plugin of an earlier release, since that body
carries the tag address. `seal pr-body` from this release clears it. The
`changelog.md` *Updating* paragraph now says this, in place of the two
sentences that said a version skew is refused on the mark line. The
`### Fixed` list gains the address change. The `gaps.md` *Not verified* row
on two copies of the plugin is closed, answered by the frame fold at
`12dc1d24` and this phase.

**No unit was renamed or moved,** so no census is owed. The phase removed
what *Removes* names for it: the version in the address and in
`MARK_FIELDS`, the `version` row of the parametrization, and the
`config.md` sentence, rewritten in place.

**The phase-boundary run.** One `bin/test` command ran the files that read
a path this phase changed or that phase 3 ran:
`tests/skills/test_pr_body.py`, `tests/skills/test_chain_check.py`,
`tests/evals/test_rule_cases.py`, `tests/skills/test_seal.py`,
`tests/e2e/teammate/test_teammate_flow.py`,
`tests/github/test_issue_claims_check.py`, `tests/hooks/test_core_start.py`,
`tests/lib/test_core.py`, `tests/lib/test_config.py`,
`tests/skills/test_broad_gate.py`, `tests/skills/test_fold_check.py`,
`tests/github/test_release_seal.py` and
`tests/github/test_publish_release_note.py`. It also ran `tests/text` and
`tests/behaviour`. It exited 0, with 3269 passed and 9 skipped (executed,
at `429582c3` with this record's `changelog.md` and `gaps.md` edits in the
working tree).
