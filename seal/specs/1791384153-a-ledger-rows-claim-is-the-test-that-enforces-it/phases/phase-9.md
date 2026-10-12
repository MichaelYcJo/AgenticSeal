# 1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it — phase 9

| Field | Value |
|---|---|
| Phase | 9 |
| Commit | 91c7ae2d |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The documents and this item's records (`spec.md` D7, D8, D11, S23):
statements 1 and 2 of `docs/the-evidence-ledger.md` §*A claim held by a
test* rewritten, their `Enforced by:` lines naming phases 6–8's cases; the
test-row paragraph of `skills/evidence-check/SKILL.md` §*Verdicts and what
to do*; `templates/ledger.md` §*A row held by a test*;
`skills/evidence-ci/SKILL.md` §*Updating later*; five pins removed and the
new sentences pinned; `changelog.md` rewritten for what ships; the
fragment's T4 and T15 rewritten and rows for S15–S22 added;
`--reverify --into` for every released row phases 6–8 drift; `overview.md`'s
divergence rows for the reframe and its Not done.

## What this phase found

**The documents.** Statement 1 now says reading the file establishes one
thing — a `def` or `class` of the cited name defined once — and that
collection and marks are predictions the sealed run answers; statement 2
says the gate hands its ledger arm the record of the run it seals, a row is
OK there only where every line for the cited test says `passed`, and what a
run with no record prints. The skill paragraph, the template's last
sentence and the evidence-ci paragraph say the same in their own places,
and the gate's docstring item 2 (phase 8) is pinned with them. No sentence
of the five files says what *reads as a test* or names a mark (a `grep` at
the phase's head found none). Nine new sentences are pinned and each went
red with one word changed (`bin/mutation-check`); five pins of removed
sentences left.

**The constant case was renamed** `test_a_constant_names_no_def_or_class`:
its old name said a unit pytest does not collect is no test, which is the
prediction the reframe removed. The framer's `spec.md` line and this item's
phase-6 record that name the old one were marked or unquoted.

**Records naming a removed unit.** Once the units left, the records arm
refused 13 lines naming them in backticks: this item's `overview.md`,
`phases/phase-1.md` and `phases/phase-6.md` (now unquoted), two lines of
`spec.md` and seven of `rounds/round-2-report.md` and `rounds/round-2.md`
(now carrying ` · NAME NOT IN TREE`, the round-2 table rows inside their
Grounds cell, the verdict cells untouched).

**The drift was wider than the frame named.** `bin/evidence-check --strict
.` at the documents' head read 136 drifted: 86 on `broad_gate.py#gate`,
which phase 8 edited and `spec.md` D8 did not list, 43 on
`evidence_check.py#main`, 6 on the skill's two sections, and one released
row, 0.11.3's, whose minor anchor quoted the gate's ledger call line
verbatim — phase 8 split that call, so the statement stands nowhere and a
re-read could not clear it. That row's claim (*`broad-gate` passes
`--strict` at its ledger call site*) is held whole by the case it already
named, so it moved onto it by a `Corrected ·` test row. A dry run of
`--into` over an archive of the head said 12 `Re-read ·` rows and 29
in-place re-stamps were owed; every claim was read against phases 6–8's
diffs first — the 12 released ones (0.16.0 O3 and R4, 0.18.1 F1 and the
narrowing row, 0.19.0 W8, W10 and four more, 0.4.0, 0.8.3, 0.9.0 R5), the
3 of this item's own re-reads on the skill's sections, and the 26 rows of
`1791384158` citing `gate` (the failure lines, the record read once, the
draft chain, the preflight, the stamp) — and none turned on the ledger
arm's argv or on `main`'s options. The run then wrote 12 rows and
re-stamped 29.

**The checker reads its own repository by existence**, and says so:
`--strict .` here prints the existence line, since no record is handed to a
hand-typed run. Whether every cited case of this fragment is held against
the full suite's record is the sealer's gate, the one run that hands one.

Executed at 91c7ae2d, output read:

```
bin/evidence-check --strict .                 exit 0
  total: 7872 ok · 0 drifted · 0 broken · 0 external · 0 old-format · 0 malformed · 0 overflow
  test rows were read for existence alone: no suite record was given, …
  7 work items read · 85 unread · 2146 names read · 4 stamps read · 0 refused · 0 drifted · 0 external
bin/correction-check --range origin/release/v0.21.0...HEAD   exit 0
bin/survivor-check --range origin/release/v0.21.0...HEAD --exempt …/survivors.md   exit 0
  48 sentences the range removed; 4 survivors, each exempt
bin/fold-check                                exit 0, 176 statements
bin/test <the eight guard modules, the new module, the fold module, the lenient-run module>   615 passed
```

## What this phase removes

| Removed item | Where it must land |
|---|---|
| the sentences of the five documents on what reads as a test and on marks, and their five pins | statements 1 and 2 of §*A claim held by a test*, the skill paragraph, the template and evidence-ci sentences, each pinned anew |
| fragment T15's static claim and T4's collection clause | T15 rewritten for the existence reader; T18–T23 for the record |
