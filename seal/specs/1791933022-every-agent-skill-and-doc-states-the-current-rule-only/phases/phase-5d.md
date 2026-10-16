# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 5d

| Field | Value |
|---|---|
| Phase | 5d (5d-i and 5d-ii written; 5d-iii adds its own sections) |
| Commit | 5d-i: 44ad6eeb · 5d-ii: 9ef773c4, each the last build commit of its sub-phase; this record's commit follows it |

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

### 5d-ii

`plan.md`'s row 5d-ii, under the paragraph *Edited 2026-10-16*: the owner's
decisions of that day on the record 5d-i built, as `spec.md` §*What a round
records* (its eight rules and the six-records paragraph), §*Data &
interfaces*, §*The sealer* and `## Removes` state them, with Alternatives
AN–AV, test rows T31–T38 and T40, and `questions.md` Q10 at its default
(the six records keep the emoji that are quotations).

- The labels `severity:`, `location:`, `verdict:`, `refixes:`, `answer:`,
  lowercase at the start of a line with one space after the colon; any other
  spelling of these words, the old `Fix of a fix:` among them, refused by
  line, never skipped.
- `severity:` reads `must` or `should`, read by nothing.
- `location:`: one line per finding, backticked coordinates joined by `, `;
  an unreadable line refused; a `fixed` commit must touch at least one listed
  path, equal or under, through `git diff-tree --no-commit-id --name-only -r
  --root`. The sealer's manual act over the location leaves step 3.
- The channel: `round-<N>#<n>`, or `round-<N>` for a fix pass, in the
  `Confirms` column of `## Confirmations` and on `refixes:`; every `fixed` or
  `answered` finding of round N named in round N+1; the last record's
  `fixed` or `answered` findings fail a ready pull request as *a verifying
  round is owed*.
- No emoji in the template, or in any text this phase writes.
- The six records rewritten by a second one-shot script under the scratch
  directory, its diff read whole before the commit.
- T32–T38 and T40 seen red before their code; the mutation list of the row;
  the modules it lists with `bin/test`, `bin/rules --check`, `chain_check.py
  --baseline origin/release/v0.22.0` exit 0, and three tamperings on a
  scratch copy each exit 1. 5d-iii — the other parties' texts, the READMEs,
  the evals, the changelog and `.test_durations` — was not this spawn's.

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

### 5d-ii

**The commits.** cf9b116e the reader, the template, `templates/config.md`'s
literals and every fixture that reads a record; 50ea8051 the sealer's step 3
and T40; 10701104 one condition in `channel` made readable; 451dc1f2 the six
records; 9ef773c4 `docs/the-review-record.md`.

**The red runs.** Every case was run before the code it pins, on 44ad6eeb's
reader (`git diff --quiet 44ad6eeb 6f98cb2b` over `chain_check.py`,
`templates/sdd-round.md` and `agents/sealer.md`, exit 0): `bin/test
tests/test_chain_check.py -q -p no:xdist --tb=line`, exit 1, 20 failed and
23 passed.

| Case | What came back |
|---|---|
| T33 `TestLocationOf` | `AttributeError: … no attribute 'location_of'` |
| T35 `TestReferenceOf` | `AttributeError: … no attribute 'reference_of'` |
| `TestFindings::test_each_finding_is_read_by_its_labelled_lines` | `[('r.md', 9, … no `Verdict:` line …)]`: the old reader did not read the lowercase labels |
| T26 `TestFindings::test_what_the_check_cannot_read_is_refused_by_name` | `assert [] == ['### 10. …']` |
| T32 `TestFindings::test_a_label_in_another_spelling_is_refused_by_line` | `'tuple' object has no attribute 'number'` |
| T38 `TestFindings::test_the_template_is_the_record_the_check_reads` | `'tuple' object has no attribute 'verdict'`; once the reader stood, red again on the old template — line 44 refused as *a label in another spelling* (`Severity:`) — and then on its first rewrite, whose `` `path:line` `` the strict reader refuses |
| `TestRecordFindings` (both) | the old reader named *no `Verdict:` line* for the lowercase fixture |
| `TestConfirmations` (both) | `AttributeError: … no attribute 'confirmations'` |
| T36 `TestChannel` (both), and its last-record case | `AttributeError: … no attribute 'round_of'`, `… 'channel'` |
| `TestMain`: S11's reviewed branch, T27, T28, T34, T37, T12, the broad-gate case | each exit 1 or a line naming *no `Verdict:` line*: the old reader could read no record of the new fixture |
| T40 `TestDefinition::test_step_3_holds_two_acts_and_reads_no_location` | `AssertionError` on step 3 as it stood, its *touches the row's `Location`* sentence printed (`bin/test … -p no:xdist --tb=line`, exit 1) |
| the language test's `ROUND_RECORD_FIELDS`, as it stood, on the new template and `config.md` | 10 failed, one per capitalised label and `Fix of a fix:`, in both of its cases |

T32, T34 and T37 went red on 44ad6eeb because the old reader read none of
the lowercase fixture, not because each rule was missing. What shows each
case holds its own rule is its mutation below, each break taken alone on
the new reader.

**The mutations.** `bin/mutation-check`, one break each, run through one
scratch script; every one `red`, exit 0 from the tool, the tree clean after
each (`git status --short` empty).

| Break | Cases |
|---|---|
| `MISSPELT_LABEL` dropped (`misspelt` reads nothing) | T32, 1 failed |
| the touch read against the first located path only | T34, 1 failed |
| the touch read against none | T34, 1 failed |
| a path sharing a located directory's prefix read as under it | T34, 1 failed |
| `location_of` accepting a bare `` `:617` `` | T33, 1 failed |
| `reference_of` accepting `Round-1#2` (`re.I`) | T35, 1 failed |
| the channel read for `answered` dropped | T36, 1 failed |
| `deferred` findings required a confirmation | T36's passing case, 1 failed |
| a reference in the first record passed | T36, 1 failed |
| a finding number the record does not hold passed | T36, 1 failed |
| a `## Confirmations` header whose first cell is not `Confirms` read as a table | `TestConfirmations`, 1 failed |
| the last-record rule dropped | T37, 2 failed (the channel case and the `TestMain` case) |
| `is_ancestor` dropped | T28, 1 failed |
| the location act put back in step 3 | T40, 1 failed |

**The reader.** `findings` returns a `Finding` per section — its `verdict:`
line, heading, heading number, verdict, located paths, `refixes:` reference
and that line — so the panel and the release seal now read `f.verdict`.
`round_of` reads one record for the arm: its findings, its `Confirms`
cells, and the number of every `### <n>. ` heading, read or refused, so a
reference to a refused finding still names one the record holds; without
that, recapitalising one `verdict:` line also refused every `Confirms` cell
naming that finding. `verdict_problems` holds the three refusals of one
verdict. `overview.md` carries each place this departs from `spec.md`'s
letter as a divergence row: the template's `` `path:12` ``, a bare `label:`
read as the exact form, a missing or doubled `## Confirmations` refused,
where the channel's refusal is printed, `round_of`, the two counters'
unpacking, and T40's anchor sentence.

**The six records.** `rewrite_records.py`, run once from the scratch
directory and deleted, wrote only the six files. Per record it asserted that
`round_of` reads it with no refusal, that its verdicts equal the old
`Verdict:` lines in order, that `Target SHA` is unchanged and that
`verdict_problems` names nothing for any finding; over the six, that
`channel` names nothing. It changed: the four labels lowercased on every
finding; `blocks merge` to `must` twice and `fix or justify` to `should`
fifteen times; each of the six `Fix of a fix:` lines to `refixes:` —
`round-1#1` and `round-1#5` (round 2), `round-3` (round 4), `round-4#1` and
`round-4#2` (round 5), `round-5#1` (round 6) — with its unit moved into the
first sentence of the grounds as *The unit refixed: <unit>.*; a `Confirms`
column on every `## Confirmations` table, reading `round-N#k` where the row
led with a round's marked finding (fourteen rows) and `none` elsewhere,
round 5's *round 4's ❓* lead among them; every `round N's 🔴 k` or `🟡 k`
outside a fence respelt `round-N#k`, so the one at `round-1.md:75`, inside a
paste block, stands as pasted; the three shorthand items of rounds 5 and 6
given the path before them; and round 1's finding 5 gaining
`` `.test_durations` `` (Alternative AU). The diff was read whole, hunk by
hunk and as a word-level tally of every change kind; nothing outside those
kinds moved. Other marks in prose — `🟡 3 is an instance of …`, *round 2's
⬜*, every 🔴 and 🟡 inside an answer or a quoted fix — stay, as Q10's
default keeps them.

**The check on this branch.** `chain_check.py --baseline
origin/release/v0.22.0 --root <worktree>` at 9ef773c4: exit 0, judged
unknown, every finding and confirmation of the six records read, none
refused. It prints the three lines 5d-i left owed: round 6 behind HEAD (a
verifying round), and no `broad-gate.md` or `guarantee.md`.

**The three tamperings.** A scratch clone of the branch at 9ef773c4, its
`origin/release/v0.22.0` fetched in, judged ready through an event payload
with `--worktree`, each tampering undone before the next, the clone deleted
after:

| Tree | Exit | The line it adds to the three owed ones |
|---|---|---|
| untouched | 1 | none |
| round 1's finding 5 with `.test_durations` taken back off its line | 1 | `round-1.md:157  ### 5. … reads verdict: fixed 1b875efc, and 1b875efc touches no path its location: names (.github/scripts/release_report.py): it changed .test_durations, …` |
| round 2's `Confirms` cell for `round-1#2` made `none` | 1 | `round-2.md:0  round-1#2 (### 2. …) reads verdict: fixed fabc1eba, and this record neither confirms nor refixes it` |
| round 1's finding 1 `Verdict: fixed 18315ee2` | 1 | `round-1.md:19  ### 1. … — a label in another spelling: the check reads verdict: …` |

**The verification the row names.** `bin/test tests/test_chain_check.py
tests/test_broad_gate.py tests/test_the_seal_is_taken_once_by_the_sealer.py
tests/test_the_release_seal_is_drawn.py
tests/test_the_pull_request_language_is_the_repositorys.py
tests/test_the_sealer_guarantees.py
tests/test_no_passage_is_pasted_into_a_second_file.py
tests/test_docs_line_wrap.py tests/test_the_rules_have_one_owner.py
tests/test_a_document_that_names_a_script_says_how_to_reach_it.py
tests/test_no_real_identifiers.py -q`: exit 0, 706 passed, 6 skipped. `bin/rules
--check --root <worktree>`: exit 0, 414 targets in 60 files. `uvx ruff check`
and `uvx ruff format --check` on the nine touched `.py` files: exit 0. Beside
the row, the eighteen other modules that name `templates/sdd-round.md`,
`docs/the-review-record.md`, `agents/sealer.md` or the reader: 918 passed.

**For 5d-iii.** S20's `git grep -n "Verdict:"` will find, beside the
guarantee's readers, the misspelt labels T32 and T30 plant on purpose
(`tests/test_chain_check.py`, `tests/test_broad_gate.py`); they are the
refused spellings S24 names, not a statement of the shape.
`docs/the-review-record.md`'s labels paragraph quotes `VERDICT:` for the
same reason. `agents/warden.md`, `agents/smith.md`, the skills, the READMEs,
both `hygiene.yml` comments, the evals and this item's `changelog.md` still
state the capitalised labels; they are 5d-iii's row.
