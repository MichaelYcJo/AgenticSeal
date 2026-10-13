# 1791876665-each-budget-ratchets-and-every-pull-request-measures-it — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | a81d2a22 |
| Ran by | smith on Opus 5.5, as `routing.md`'s models line gives it |

## What this phase was asked

Widen the tree budgets and stop before phase 3: the other four `preload:*`
rows and `preload:claude-md`; the docs classifier and the `## Docs history
lines` table; `suite-seconds` and the `## Slow test files` table with the
120 s threshold; T8–T10. Re-measure every starting value with the checker at
this phase's own SHA and record the numbers and probes here. Leave
`.test_durations`, `test.yml` and the commit-gate test module alone: #929 and
#931 change them on their own branches, and the seconds rows read the file as
it stands on this branch.

Mid-phase, the orchestrator's decision from #931's refresh run 38475370013:
one refresh moved `suite-seconds` from 7,861.7 to 8,490.3 s, 553.9 s of it the
same 13,454 cases priced 1.071 times higher, 10 of 16 slow files past 10 % and
two unlisted files over 120 s. So where `.test_durations` differs between the
baseline and HEAD, measure the price level as the seconds-weighted ratio over
the case ids both hold and compare the seconds rows in the base's prices,
printing the raw value, the ratio and the normalised value; choose the ratio's
computation and edge cases, name them here, record the divergence in
`overview.md`, and add a case that a uniform ×1.07 rescale holds every row and
one that a single file doubling against the rest still fails its row, each
seen red.

## What this phase found

**The decision as given fails one pull request later, so the level is a row.**
Built literally — HEAD's seconds divided by the ratio against the base — the
refresh's own pull request holds. The next one does not: its base already
holds the refreshed file, the ratio is 1, and its seconds are in the new
prices while every ceiling is in the old. On a scratch clone with every case
×1.071 the next pull request's `suite-seconds` read 8,420 against 7,862, and
so did the suite case with no baseline. So the ceilings stay in one set of
prices and `seal/budgets.md` states how the committed file's prices stand
against them, `## Price level`, one row, per mille (1000 now). Every seconds
reading is divided by that level. With `--baseline` the ratio is measured as
decided, and the level must equal the base's level times it, rounded per
mille, or the run fails first, naming the number to write. A refresh restates
one number and writes no `Budget raised:` line, and a level edited over an
unchanged file fails. `questions.md` Q6 asks the orchestrator whether this is
the reading it wants; the row is what is built.

The ratio: HEAD's seconds summed over the case ids both files hold, over the
base's for the same ids. Its edges:

- no case id in common: exit 2, nothing to read a level from;
- the base pricing the common ids at 0 s: exit 2;
- no `.test_durations` at the base: ratio 1, the rows read as they stand;
- the same file at both: exactly 1, by the same sum.

Seconds-weighted, as decided. One slow file moving shifts the level a little:
a file doubling at 251 s of a 7,862 s suite moved it to 1.016, which reads
every other file 1.6 % lower, inside the 10 % slack. A median of per-case
ratios would ignore that file entirely; it was not built, because the decision
named the weighting.

**The docs classifier's rule block is bounded by its paragraph.** `spec.md`
reads "from a line opening with `**` to the next `Enforced by:` line". Read
literally, a bold lead with no `Enforced by:` after it takes the rest of the
document: 118 history lines over `docs/` against the frame's 246. Four
readings were measured at 65a0ba5f with the repository's own fence, comment
and heading readers:

| Rule block ends at | History lines | Files off the frame's number |
|---|---|---|
| no rule exclusion at all | 486 | 18 |
| `Enforced by:` only (literal) | 118 | 15 of 19 lower |
| `Enforced by:` or the next heading | 155 | 12 |
| `Enforced by:` or the next `**` line or heading | 323 | 14 |
| `Enforced by:` or the end of the paragraph (built) | 251 | 4, each by 1–2 |

The four: `one-root-by-lifetime.ko.md` 33 (frame 32), `one-root-by-lifetime.md`
39 (38), `the-record-layout.md` 12 (10), `worktree-guard-spec.md` 39 (38). One
of the record layout's two was phase 1's own `seal/budgets.md` row, whose
"measured against" matched the `measured` mark; this phase reworded it to
"held to", leaving 11. The rows hold the checker's numbers, as the plan says:
250 history lines over 19 documents, 4,049 rule lines.

**The numbers** (`executed`, the checker at a81d2a22, exit 0; the same at
65a0ba5f for every row this phase did not word):

| Budget | Measured = ceiling | Frame's |
|---|---|---|
| `preload:framer` · `scribe` · `sealer` · `smith` · `warden` | 99,089 · 29,554 · 36,113 · 106,350 · 102,229 bytes | the same |
| `preload:claude-md` | 9,261 bytes | the same |
| `suite-seconds` | 7,862 s (7,861.70 summed over 13,482 cases) | the same |
| `slow-file:*` | the frame's 16 files at its 16 numbers, the seconds of each file rounded half up | the same |
| `slow-file` | 120 s; the largest unlisted file is 113 s, `tests/test_the_chain_goes_back_to_its_framer.py` | — |
| `docs-history:*` | 19 files, 250 lines, the four above one over the frame | 246 |
| `docs-history` | 0 for a file the table does not list | — |

**The families measured per file.** The family's own row in the Budgets table
gives the unit, the slack and the kind, and its ceiling is what every file
the table does not list is held to. So an unlisted test file over 120 s and an
unlisted document with a history line both fail, naming the file and, for a
document, its lines. Listing a file above that ceiling is a raise from it and
takes its line, and a file row whose family row is gone takes none of its
own. A listed test file may sit under the threshold. A row naming a file the
durations do not price, or a document the tree lacks, is exit 2.

**Probes** (`executed` on a scratch clone of 4c72ecad, the checker run from
this worktree, the clone removed after):

| Probe | Exit | What it said |
|---|---|---|
| the tree as committed | 0 | every row holds; slow-file largest unlisted 113 s |
| `docs/the-pact.md` + "This rule came from #999." | 1 | `docs-history:docs/the-pact.md` 1 over 0, at line 412 |
| every case ×1.071, level left at 1000 | 1 | the price level first: 1000 × 1.071 = 1071, write it; then 17 seconds rows over |
| the same, level restated to 1071 | 0 | `suite-seconds` 7,862 (raw 8,420 at ×1.071) |
| the next pull request after that refresh | 0 | ratio 1, read at 1071 |
| the refreshed tree with no baseline | 0 | the suite case's reading |
| `tests/test_the_last_rounds_fixes_are_checked.py` doubled, level 1016 | 1 | that file 247 s against 126; nothing else |

**Every case seen red** (`executed`, `bin/mutation-check` on committed trees,
42 mutations, every one `red`). T8: the pair counted, `CLAUDE.md` off by a
byte. T9: the marks narrowed to `#\d+`, `Measured` matched case-sensitively,
fences and comments read, headings read, rule blocks read, the block
unbounded, `Enforced by:` not closing it. S8: an unlisted document not held.
T10: the threshold check removed, the per-file compare removed. The suite sum
taken as a maximum, rounded half to even. A file row not held at its family's
ceiling at the base; a family's removal asking a line per file. The price
level forced to 1, the slow files and the suite not divided, the raw value
left out of the summary, the stated level ignored, the level not held to the
file, the base's level read as 1000, an absent price table refused, its rows
unchecked, the level an unweighted maximum, and each of the three edges. The
family and file refusals, one each: a table with no family row, a family with
no table, a file twice, a bad file name, a family row in another unit, a
durations file that is no JSON or no seconds, an unpriced test file, no
`CLAUDE.md`. The price problem dropped, and printed after the rows it
explains. The two phase-1 ratchet mutations again, on the reworked ratchet.

**For #931, and for the merge of its refresh into this branch.** A pull request
that refreshes `.test_durations` must restate `## Price level` in
`seal/budgets.md` to the number the hygiene step names. Where #931 lands on
the release branch first, this branch's rebase brings that refresh in with
the level still 1000, and the suite case then fails until the level is
restated in the rebase; the number is `budget_check.py --baseline <the
release branch before #931>` against the merged tree.

**For phase 3**, from phase 1's record, unchanged: the per-run `ci-minutes:*`
rows are one-sided (#929 Q2, approved by the owner); #931 Q4 keeps its
durations job and this item's budgets job apart in `test.yml`.
