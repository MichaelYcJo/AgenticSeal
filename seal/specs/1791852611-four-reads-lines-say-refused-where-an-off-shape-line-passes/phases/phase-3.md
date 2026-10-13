# 1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 49835329 |
| Ran by | specseal:smith on claude-opus-5-5 |

## What this phase was asked

Phase 3 of `plan.md`, the records, written last so the frame's own
`## Removes` rows read as gone the moment the work item becomes live:
`seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md`
with test-held rows for S1–S3, hashed rows for S5 and S6 (quoted-line
anchors on the rewritten clauses and the warden's sentence), and the
`Re-read ·` row for #835's D1 written by `evidence-check --reverify --into`;
`changelog.md` under `### Fixed`; `overview.md`; this record.

## What this phase found

**The fragment holds ten rows of this work and six `Re-read ·` rows.** The
four test-held rows are S1, S2, S3 and M1, the heading boundary the
orchestrator's amendment added. The six hashed rows are R1 and R2 (the
registry's sentence and the template's comment from phase 2), three S5 rows
and the S6 row. Each was written with `@00000000`, and one `--reverify
--into … --checked 2026-10-13` run stamped all six that moved and wrote the
citing rows. Before that run, each drifted released row's claim was read
against the changed section: A11, the depth split (D1 of 0.15.1), V1, A6,
C2, N13 and the 0.9.3 verifying-round row on `agents/warden.md#"## Role"`,
and #835's D1 on the registry document. None of them says anything the new
paragraph or sentences contradict. The registry's D1 still holds: every
statement keeps one `Enforced by:` line and the document is under the
ceiling (`bin/fold-check --root .` exit 0 in phases 1 and 2). Six citing
rows cover thirteen drifted readings, because the checker writes one per
family of rows citing the same released row.

**The frame's own rows read as gone.** With the fragment present the work
item is live, and the records arm reads its `spec.md`: 1 work item read,
0 refused, 0 standing. The three `## Removes` rows are silent, and the
prose under `### Why these rows` is read by the name half without a finding.

**Verification, executed at 49835329's tree.** `bin/evidence-check --strict
.` exit 0: 8451 ok, 0 drifted, 0 broken, 0 malformed, 0 overflow. `bin/correction-check
--range origin/release/v0.21.1...HEAD` exit 0. `bin/unverified-check
--baseline origin/release/v0.21.1` exit 0. The overview's two rows are open
and each names who answers it. `bin/survivor-check --range
origin/release/v0.21.1..HEAD` exit 0: eight removed sentences, none still
standing.
