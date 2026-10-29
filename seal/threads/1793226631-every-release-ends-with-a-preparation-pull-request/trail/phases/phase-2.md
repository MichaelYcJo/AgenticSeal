# Phase 2: 1793226631-every-release-ends-with-a-preparation-pull-request

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 20137f6b |

## What this phase was asked

Build phase 2 of `frame/plan.md` against the frame at `7bead7e7`. A work
item's process rows ride in its fragment. `publish_release_note.py#section`
lifts every fragment's `### Process changes` rows into one table above the
fragments (S9), and renders what it rendered before where no fragment
carries one (S10). `templates/records/process.md` is reshaped from a file's
template to that section's. `seal/process/` is removed with every reader
`## Removes` lists for it, and `agents/framer.md` step 4 reads the rows
where they now are. S9 is seen red against `section` at `4134055a`.

## What this phase found

**The frame holds against the tree (read, at `7bead7e7`).** Every phase 2
coordinate in *Removes* resolves: `release_report.py:24-25`, `:54` and
`:178-180`, `tests/github/test_release_report.py:247-267`,
`tests/censuses.py:1056`, `tests/test_censuses.py:788`, `:806` and `:926`,
`tests/text/test_a_record_carries_no_comment.py:18-19` and
`agents/framer.md:63-67`. *Removes* names the census entry and not the
sentence above it that gave the entry's reason; that sentence went with it.

**The defaults this phase built on.** Q1, Q2 and Q3 do not reach phase 2.

**How S9 was seen red (executed).** `bin/test
tests/github/test_publish_release_note.py -q -p no:xdist -k Test_section`
exited 1 against `section` at `4134055a`. The output held the first
fragment's marker line and prose above the table, where S9 asks for the
table first. The case reading the table's shape from the template failed
with `AttributeError`, because no `process_shape` existed.

**How the census exemption's removal was seen red (executed).** With
`"seal/process/"` out of `OLD_NAME_RECORDS` and the fixtures still planting
`seal/process/0.1.0.md`, `bin/test tests/test_censuses.py -q -p no:xdist`
exited 1 with two cases red:
`Test_old_names::test_accepts_the_new_names_kept_spellings_records_and_the_migration`
and `Test_vacated_paths::test_accepts_the_records_and_a_recorded_case`. Both
passed once the fixture paths went.

**The section ends at the next heading, not at the next `#`.** The design
says the section runs "up to the next line starting with `#`". The first
draft spelled that test with `line.startswith("#")`, and
`tests/censuses.py#heading_rule` refused it: a shipped script asks
`skills/verify/scripts/unverified_check.py#heading_level` and spells no
second heading rule. The code asks `heading_level`, so a wrapped line
opening `#120)` does not end the section. `gaps.md` records the divergence.

**The table's shape has one source.** `process_shape` reads the heading, the
header row and the delimiter row from `templates/records/process.md`, so the
template and the renderer cannot drift apart. `Test_module` holds the reader
to the template's lines.

**The lint hook took an import out between two edits.** The import of
`heading_level` was added in one edit and its use in the next. The hook's
`ruff --fix` ran after the first edit and removed the import as unused. The
next run of the module failed with `NameError`, and the import was added
again (executed).

**Mutants (executed, `bin/seal mutate`, one command per unit).**
`process_shape`'s rows, `split_process`'s four arms and its slice past the
header rows, `section`'s empty-body marker line, its early return with no
rows, its blank line before the fragments, and its row accumulation were
each broken and each turned a case red. One survived: the arm that ends the
section at the next heading. `20137f6b` adds the case that holds it, and
the mutant then failed one case of three (exit 0).

**A `git rm` staged ahead of an unrelated commit.** The three archives were
removed with `git -C <worktree> rm`, which stages the deletion. The next
commit was the phase 1 rename, and it carried the deletions with it. That
commit was undone with `git reset --soft HEAD~1` before anything read it.
The deletions were unstaged and committed with phase 2 at `498c7b5d`.
