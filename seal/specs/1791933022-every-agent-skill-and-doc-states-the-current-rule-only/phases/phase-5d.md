# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 5d

| Field | Value |
|---|---|
| Phase | 5d (5d-i written; 5d-ii adds its own sections) |
| Commit | 5d-i: 44ad6eeb, the last build commit; this record's commit follows it |

## What this phase was asked

### 5d-i

`plan.md`'s row 5d-i, under the fourth reframe paragraph: the round record
designed anew from its jobs, the owner's decision of 2026-10-16 to stop
patching the old verdict table. The reader, the template, this item's six
records, the tests and the two documents that state the shape, with the tree
green at the end so everything `bin/test` and `bin/rules --check` read lands
here.

- `chain_check.py`: `findings(reader, lines, rel)` reads the one
  `## Findings` section, split at its `### ` headings, each holding exactly
  one `^Verdict: (.*)$` line; `verdict_of(value)` reads `open`,
  `fixed <7–40 hex>`, `answered` or `deferred <home>` and nothing else;
  everything else is refused by path, line and heading; `open` fails a ready
  pull request; a `fixed` commit HEAD does not descend from is refused.
  `Severity:`, `Location:` and `Answer:` are read for nothing. The old table
  reader, its constants and its tests leave as `spec.md` §*Removes* lists.
- T25–T29 test-first, each seen red; T30 for `rounds_rows` and
  `chain_counts` reporting an old-shape record as not read.
- `templates/sdd-round.md` written anew to the spec's literal format;
  `docs/the-review-record.md` §*The round record* and §*What the check reads
  at the pull request* rewritten in place; `docs/the-agent-set.md:56`;
  `templates/config.md`'s literals and the language test's.
- The six records rewritten mechanically by a one-shot script outside the
  tree, verdicts and grounds unchanged, the diff read whole before the
  commit; round 6's finding keeps `Verdict: deferred the frame`.
- `test_no_passage…`'s thresholds re-measured where they move.

The orchestrator added two things during the spawn: a fence or a comment
that never closes is refused at its opener, pinned red first; and a `### `
heading with no `Verdict:` line is refused, with a case pinning it.

## What this phase found

### 5d-i

**The red runs.** Each case was seen failing before the code it pins:

| Case | Red on | What came back |
|---|---|---|
| T25 `TestVerdictOf::test_the_four_values_read_and_nothing_else_does` | 9a7d0b32 (the readers unchanged since e9baf154: `git diff --quiet e9baf154 9a7d0b32` over the three scripts and the template, exit 0) | `AttributeError: … no attribute 'ANSWERED'` |
| T26 `TestFindings::test_what_the_check_cannot_read_is_refused_by_name` | 9a7d0b32 | `AttributeError: … no attribute 'findings'` |
| `TestFindings::test_each_finding_is_read_by_its_one_verdict_line` | 9a7d0b32 | the same |
| T29 `TestFindings::test_the_template_is_the_record_the_check_reads` | 9a7d0b32 | the same; once `findings` existed, red again on the old template: `('t', 0, 'no ## Findings section …')` |
| T27 `TestMain::test_an_open_finding_fails_a_ready_pull_request` | 9a7d0b32 | the old check could not read the new shape; exit and line asserted wrong |
| T28 `TestMain::test_a_fixed_commit_head_does_not_descend_from_is_refused` | 9a7d0b32 | the same |
| S11 `TestMain::test_an_old_shape_record_under_the_declared_item_is_refused` | 9a7d0b32 | the old check read the old table and printed `🔴 1 reads open …`, no `no ## Findings` refusal |
| S11 `TestMain::test_a_reviewed_branch_passes_a_ready_pull_request` (the merged item's old record never opened) | 9a7d0b32 | red because the old check refused the new-shape record of the declared item |
| `TestDeferredHome::test_no_home_and_prose_name_no_issue` | 9a7d0b32 | `assert 12 is None` for `deferred #12.` |
| T30 `TestRoundsRows::test_the_count_and_every_records_deferred_homes` | e9baf154's three scripts checked out over the tree, then restored from HEAD | `[('rounds', '5'), ('', '1 deferred → #9')]`: the old panel counted the old-shape record's `#9` and none of the new records |
| T30 `test_a_deferred_count_nobody_could_read_is_none_and_the_log_says_why` | the same | the log named `round-1.md` (the new shape) as unread and not `round-2.md` (the old one) |
| `TestRecordFindings` (both) and `TestMain::test_an_unclosed_fence_hiding_an_open_finding_fails_a_ready_pull_request` | 193ce92e's `chain_check.py` checked out, then restored from HEAD | 3 failed; the end-to-end case exited 0 with finding 2 at `open` hidden behind the fence |

**The mutations.** `bin/mutation-check`, one break each, every one `red`
(exit 0 from the tool, the tree clean after each):

| Break | Cases |
|---|---|
| `VERDICT_LABEL` compiled with `re.IGNORECASE` | `TestFindings` |
| emphasis allowed around `Verdict:` in the label | `TestFindings` |
| a second `Verdict:` line accepted (`> 99`) | `TestFindings` |
| a value outside the four passed | `TestFindings` |
| a `Verdict:` line outside a finding accepted | `TestFindings` |
| a finding with no `Verdict:` line accepted | `TestFindings` |
| no `## Findings` read as empty | `TestFindings`, the old-shape `TestMain` case |
| the ancestor check dropped | `test_a_fixed_commit_head…` |
| `fixed` widened to six digits and capitals | `TestVerdictOf` |
| `open` not refused on a ready pull request | `test_an_open_finding_fails…` |
| the unclosed-comment refusal dropped | `TestRecordFindings` |
| the unclosed-fence refusal dropped | `TestRecordFindings` |
| `rounds_rows` counting a refused record | `TestRoundsRows` |
| `chain_counts` counting a refused record | the release seal's deferred cases |

**A home is the whole of what follows `deferred`.** The old reader cut a
home at ` — ` and called the rest a note, stripped code marks and a
trailing period. The new value has one shape, so `deferred #854 — fixed in
0.20.0 as #858` names no issue (the note belongs on `Answer:`), the panel
prints a backticked home with its backticks, and `deferred #12.` names no
issue. The panel and release-seal cases were rewritten to that.

**A record with any refusal adds nothing to a count.** `rounds_rows` used to
count a bare `deferred` as a homeless deferral; a bare `deferred` is now a
value the reader refuses, so its whole record adds nothing beneath `rounds`
and leaves the release seal's count unread. `overview.md` carries both as
divergence rows.

**One reader for the arm and both counts.** The fence-and-comment refusal
needs the record's text, and `findings` takes `readable` lines in which such
a region is already blanked. So `record_findings(reader, text, rel)` runs
`unclosed` (comments through `reader.comment_scan`, then fences through
`reader.fence_spans` on what the comments left, `readable`'s own order) and
then `findings`, and the records arm, `broad_gate.py#rounds_rows` and
`release_seal.py#chain_counts` all read through it. `findings` keeps the
signature `spec.md` §*Data & interfaces* gives it.

**Where the region refusal does not reach.** A fence that closes on the
wrong line hides what lies between without being unclosed: a ```` ``` ````
fix block opened inside another finding's ```` ``` ```` block closes it early
or late, and a heading or `Verdict:` line inside is not seen. Nothing here
refuses that, because a fix block legitimately quotes markdown with `### `
headings in it. `unverified`; the next round's warden answers whether it
needs a check.

**The six records.** `rewrite_records.py`, run once from the scratch
directory and deleted, moved each 🔴 or 🟡 row to a `### N.` section (its
bold lead the heading, a leading `fix of a fix —` or `` `fix of a fix`: ``
taken off), its mark to `Severity:`, its Location and Verdict cells to
`Location:` and `Verdict:`, its paste-ready section inside it, and its
`· fix pass:` or `· orchestrator:` tail to `Answer:` (the orchestrator's
prefixed `orchestrator:`). Each fix of a fix got a `Fix of a fix:` line in
the record's own words for its unit. 🟢 and ❓ rows moved unchanged to
`## Confirmations` and `## Not judged`; `| What was run | Result |` became
`| Command | Result |`, and `` `## Executed probes` `` in prose became
`` `## Probes` ``. The script asserted, per record, that the new text reads
with no refusal, that its verdicts equal the old cells in order and that
`Target SHA` is unchanged: 17 findings (7, 3, 2, 2, 2, 1), 35
confirmations, 3 not-judged rows. The removed lines (`git diff -U0`) were
read whole: the old table rows, its headers, `## Verdicts`, the paste
headings, `## Executed probes` and its header, and the intro lines naming
it, nothing else. The intros still say "labelled in each Grounds cell",
left as written.

**The check on this branch.** `chain_check.py --baseline
origin/release/v0.22.0 --root <worktree>` at 44ad6eeb: exit 0, judged
unknown, every finding read and none refused; the three lines it prints are
owed later (round 6 behind HEAD, so a verifying round; `broad-gate.md` and
`guarantee.md`, the sealer's). Judged as a ready pull request it exits 1 on
those three alone. On a scratch clone whose round 6 finding reads
`Verdict: confirmed`, `--worktree` judged ready exits 1 and names
`round-6.md:49  ### 1. … — reads Verdict: confirmed, which the check cannot
read: a verdict is open, fixed <commit>, answered or deferred <home>` beside
the same three; the clone was deleted.

**The passage thresholds.** The four pairs naming `templates/sdd-round.md`
measured 0 shared runs after the rewrite (30, 83, 5 and 9 before), so their
entries left `BASELINE`: a pair not in it fails at its first shared run.

**Beyond the row.** `docs/the-review-record.md` §*The run*'s fix-of-a-fix
sentence named the `Finding` cell, which the template no longer has; it now
names the `Fix of a fix:` line. `docs/the-agent-set.md:59`'s `Enforced by:`
names `TestFindings` rather than the template case, to fit the line limit
`tests/test_docs_line_wrap.py` holds that file to. The language test's
docstring stating `## Verdicts` as the case's history was rewritten to the
current literals.

**Declined.** The orchestrator asked for the region refusal to be recorded
in `spec.md` §*What leaves* as well. `spec.md` is the framer's file and not
a write `agents/smith.md` names, so it is recorded here and in
`overview.md`, and the frame's row is the framer's to add.
