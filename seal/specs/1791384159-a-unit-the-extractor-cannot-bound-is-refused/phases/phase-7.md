# 1791384159-a-unit-the-extractor-cannot-bound-is-refused — phase 7

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | 9d842981 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

`plan.md` phase 7: #864's seven fragment rows re-anchored in place
(`test.yml#"pytest:"`); one `Corrected ·` row per released family whose
newest member still carries a refused coordinate, the claim unchanged;
`Corrected ·` rows with the citation alone for `0.4.0.md` L51 and L67; this
item's own fragment rewritten (U1 narrowed to three answers, U2 to the
refusals, U3 kept, U4–U7 removed, U8 deferred to phase 8, the 0.4.0 L17
`Corrected ·` row restated); `--reverify --into` for every released row a
changed unit drifted, read first. S4's repository half and S10:
`bin/evidence-check --strict .` 0 `BROKEN`, 0 `DRIFTED` against
`origin/release/v0.21.0`, quoted here; `survivor-check` and
`correction-check` over the range. The spawn added: #864's fragment rows are
in the release branch and are re-anchored in place.

## What this phase found

**S10 holds: the branch reads exactly as the release branch does.** The
release branch's own tree, extracted from `origin/release/v0.21.0` into a
scratch directory (deleted after) and read by its own checker with
`--strict .`, and this branch at 9d842981 read by its checker, give the same
findings, file by file (`diff` of the two per-file finding counts, exit 0):

```
release   7698 ok · 33 drifted · 0 broken
branch    7761 ok · 33 drifted · 0 broken
```

All 33 are the release branch's own and none is this work item's: 8 on
`agents/warden.md#"## Report"`, 14 on `templates/config.md#"# Repository
config"`, 10 on `tests/test_every_reader_ends_a_line_where_gfm_does.py#OUT_OF_CLASS`,
1 on `skills/verify/scripts/payload_meter.py#heading_starts`. Both exit 2 for
them. Q2 is therefore 0 and 0.

**There were 16 bare YAML rows, not 14.** #869's fragment
(`seal/ledger/1791384158-the-broad-gate-reads-its-counts-from-the-recorder.md`,
in the release branch since the frame was written) holds two rows on
`publish-release.yml#jobs`: K14 and its `Corrected · W3`. Both were
re-anchored in place with a Notes trace, and the `W3` family's newest member
is that `Corrected ·` row, so no released W3 correction was owed here.

**The quoted paragraphs, read 2026-10-12.** `test.yml#"pytest:"` is lines
32–145 and hashes `fd3a49c3`, the hash the bare key held, so #864's seven rows
kept their hashes. `test.yml#"ledger:"` is 147–181, not 163–181 as the frame
read: the job's comment above its key has no blank line before the key, so
the paragraph begins at the comment, which is where the warning's three
causes are written. `publish-release.yml`'s `publish` job has a blank line
inside it, so W3, a claim on both jobs and the note step's `created` output,
quotes three paragraphs: `"publish:"` (46–60), the note step
`"- name: publish the GitHub Release for this tag"` (62–69) and `"seal:"`
(71–148). The frame's two quotes would have left the note step out.

**0.20.0's S1 needed its own `Corrected ·` row; S4 and S8 did not.** S4's and
S8's newest members are #864's `Corrected ·` rows, re-anchored in place. S1's
newest was #864's `Re-read · S1`, and re-anchoring it changed the coordinate
the family is keyed on, so 0.20.0's S1 still carried `test.yml#pytest` alone.
Its correction quotes `"pytest:"` and `"on:"` (3–18): the claim's second half,
that `test.yml` can be dispatched, rests on `workflow_dispatch:`, which the
bare key never covered.

**Released `Corrected ·` rows were retired by citing them, not doubled.**
`docs/the-evidence-ledger.md` §*A released row is read again*: "Once both
have folded, a `Corrected ·` row citing one of them retires it." The four
0.19.0 corrections that cited deleted cases (`"re-stamps the fragments"`,
`"judges each code"`, `"prints one"`, `"never writes onto"`) are each retired
by a `Corrected ·` row citing them, the claim kept where it named nothing
removed and restated where it named the unsure place. 0.16.0's H1 is
restated for the quoted paragraph that replaced the generic block.

**`--into` was narrowed, and three rows it wrote were removed.** It was run
over this fragment, #864's, and the twelve release files holding a row this
branch drifted. Families with a member in those files wrote three `Re-read ·`
rows for coordinates this branch did not change (0.16.0's G14 on
`OUT_OF_CLASS`, 0.5.0's S8 on `templates/config.md`, 0.9.2's S3 on
`agents/warden.md`); they were taken out of the fragment unread, and those
families read as they do on the release branch. #867's fragment holds its
own claim rows K23, the fenced-section `Corrected ·` row and `Corrected · C1`
on changed units; they were re-stamped in place by hand, with a Notes trace,
because an in-place `--reverify` of that file re-stamps its release-branch
drift too.

**One commit broke the cadence.** 38f75d90 was made in the same Bash call as
its `git add`; it landed and the rule was kept for every commit after it.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| This fragment's U4–U7 and U8 of the first design, and its `Re-read ·` rows for the families it now corrects (H1, the four 0.19.0 corrections, 0.4.0's declaration-rule and `--migrate` rows) | U4–U7 of the redesign, the `Corrected ·` rows, and phase 8's U8 |
| Every bare `.yml` coordinate in the ledgers | quoted job-key lines, in place in #864's and #869's fragments and by `Corrected ·` rows for 0.15.5's S7 and 0.20.0's S1 |
