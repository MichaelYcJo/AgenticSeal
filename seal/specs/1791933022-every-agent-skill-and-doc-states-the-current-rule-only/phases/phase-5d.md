# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 5d

| Field | Value |
|---|---|
| Phase | 5d (5d-i, 5d-ii, 5d-iii and 5d-iv) |
| Commit | 5d-i: 44ad6eeb · 5d-ii: 9ef773c4 · 5d-iii: 9a4ce364 · 5d-iv: 274a9443, each the last build commit of its sub-phase; this record's commit follows it |

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

### 5d-iii

`plan.md`'s row 5d-iii: every party and grader states the shape 5d-i and
5d-ii built, in words, and the build closes. `agents/warden.md`,
`agents/smith.md` and `agents/sealer.md` where they say how a round is
written, filled or read; `skills/code-review/SKILL.md` (the findings format,
the proof block's verdict line in words); `skills/implement/SKILL.md` §5;
`skills/code-review/orchestration.md`; both READMEs, the cap paragraph
among them; both hygiene step comments; the evals (`shape-findings` with a
`not_contains` over the emoji ranges, the `^location: ` truth,
`SEALER_ROUND`, the warden and sealer cases regenerated with `--case`); T39
test-first; this item's `changelog.md` first two entries, with what a user
whose work item is in flight at the update must do; the overview's
divergence rows; `.test_durations` pruned by collection; this section and
the row's Status. Every sentence rewritten in place; part B's rewrite of
the rest of each definition stays part B's.

The orchestrator relayed two sets of the owner's decisions of 2026-10-16
during the spawn, to build inside 5d-iii test-first, each step its own
commit, with `spec.md` left to the framer:

- `## Confirmations` holds one `confirms: round-<N>#<n>` (or
  `confirms: none`) line per entry with its prose after it, read with the
  other labels' fail-closed rules; a finding left unconfirmed is refused at
  its own heading in its own record; a record with nothing to confirm may
  leave the section out, and two are refused.
- The `| Field | Value |` table goes and `target: <sha> against <base>` or
  `target: <sha>, fixes <a>..<b>` names the reviewed commit, one line,
  `Target SHA` refused as another spelling; `refixes:` is `regression:`;
  the verdict `answered` is `rejected`, owing the next round a
  confirmation or a regression reference as `answered` did. The reason
  given: the reader is mostly an agent, so every label and value is a plain
  English word.

### 5d-iv

`plan.md`'s row 5d-iv, approved at its line 16: the owner's answer to
`questions.md` Q11. A repair made outside the tree with no commit closes
`deferred <where it was repaired>`, one a commit made closes
`fixed <commit>`, and `rejected` keeps the one meaning *the finding does
not hold*. A text phase with no reader change. The spawn asked for the
class re-grepped at the start, every hit named here; T41 seen red before
`docs/the-review-record.md`'s fix-pass paragraph was rewritten in place,
with T41 added to its `Enforced by:`; this item's `changelog.md:35`
mapping each old close to its word; one clause each in the template's
`deferred <home>` comment and the smith's fix-pass sentence, pointing at
the document; T39's module docstring rewritten; the overview's row *A
repair that made no commit*; this section and the row's Status. It also
asked for `tests/test_docs_line_wrap.py` over the tree, since the framer
had edited `spec.md`, `plan.md` and `questions.md` and run nothing.

### 5d-v

`plan.md`'s row 5d-v, approved at its line 17: round 8's findings 1 and 2
and the owner's decision of 2026-10-16 on round 8, with its refinement the
same day. A close that does not hold, where no fix pass's commit made the
defect, is raised again on a `reopens:` line as an ordinary finding that
gets its fix pass; a `regression:` line is routed by one sentence of its
grounds comparing the fix with the frame; and the run ends only on a round
whose record holds no `open`, `fixed` or `rejected` finding. The spawn
asked for T42, T43, T44, T45, T38's extension and the language cases seen
red on the tree before the change; then the reader (`REOPENS`,
`REOPENS_LABEL`, the label sets, `Finding.reopens`, `channel`); then the
texts the row lists, each rewritten in place and never appended, the
orchestration's run-end sentence among them; this section and the row's
Status. It asked for no widening into stating the record's rules once and
pointing at them from every other file, which is #957's.

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

### 5d-iii

**The commits.** 4ed5dd39 the reader, the template, `templates/config.md`'s
literals and every fixture that writes a record; 92991623 the six records;
5b637fee `docs/the-review-record.md` and the three documents that named a
round's `Target SHA`; 9d61c520 the parties' texts, the READMEs, the hygiene
comments and T39; e6f7a000 two pins re-pointed at the warden's new words;
71fd384f the evals and the regenerated cases; bc2f3fd5 `.test_durations`;
9a4ce364 the release seal's docstring and the review skill's heading.

**The red runs.** T39 on the tree at 7c678b52 with only its file added:
`bin/test tests/test_the_record_is_written_in_words.py -q -p no:xdist`,
exit 1, fifteen lines named — `agents/warden.md:150, 154, 221, 262-264`
and `skills/code-review/SKILL.md:207-210, 214, 217, 221, 225, 296`. The
reader's cases, rewritten to the owner's decisions, on 9ef773c4's reader:
`bin/test tests/test_chain_check.py -q -p no:xdist --tb=line`, 22 failed and
24 passed — `TestVerdictOf` (`ANSWERED` read, `REJECTED` absent),
`TestRecordTarget` both (`record_target` absent), the four `TestFindings`
cases and the new out-of-place case, both `TestRecordFindings`, both
`TestConfirmations` (a table expected), all three `TestChannel`, and seven
`TestMain` cases that could not read the new fixture. The eval cases'
red is the first mutation below, the old row pattern put back.

**The mutations.** `bin/mutation-check`, one break each, through three
scratch scripts; every one `red`, exit 0 from the tool, `git status
--short` empty after each.

| Break | Cases |
|---|---|
| a table row in `## Confirmations` read as prose | `TestConfirmations` |
| `confirms` dropped from `MISSPELT_LABEL` | the label case |
| a `confirms:` value the reader cannot read skipped as `none` | `TestConfirmations` |
| an unconfirmed finding refused at line 0 of the next record | `TestChannel` |
| a record with no `## Confirmations` refused | `TestConfirmations` |
| a second `## Confirmations` accepted | `TestConfirmations` |
| any value after the commit read as a `target:` | `TestRecordTarget` |
| two `target:` lines accepted | `TestRecordTarget` |
| no `target:` line accepted | `TestRecordTarget` |
| `Target SHA:` not named as `target:` | the label case |
| a `target:` or `confirms:` line inside a finding read | the out-of-place case |
| a `confirms:` line outside `## Confirmations` accepted | the out-of-place case |
| the old `refixes` not named as `regression:` | the label case |
| `answered` still read as a verdict | `TestVerdictOf` |
| a `rejected` finding owing the next round nothing | `TestChannel` |
| the last record's `target:` not read against HEAD | `TestMain::test_the_last_record_is_at_head…` |
| an emoji in the template, in `agents/warden.md`, in `agents/smith.md`, in the skill's proof block (four breaks) | T39, each |
| `truth_pattern` back to the old `^\| (?:🔴\|🟡) \d+ \|` row | `test_a_truth_pattern_holds…` |
| `truth_pattern` with no `^location: ` anchor | the same |
| `FINDING_ROW` reading any backticked coordinate | `test_the_report_rows_are_the_last…` |

**The six records.** `rewrite_records.py`, run once from the scratch
directory and deleted, loaded 4ed5dd39's parent's reader beside the new one
and wrote only the six files: the field table to one `target:` line with
the value it held, `refixes:` to `regression:` six times, and each
`## Confirmations` row to a `confirms:` line with its what-holds, location
and grounds on one prose line after it. Per record it asserted that the
new reader reads it with no refusal and that its verdicts, regression
references, confirmation references and target commit equal what the old
reader read; over the six, that the channel names nothing. No finding
read `answered`, so none became `rejected`. The diff was read whole
(`git diff -U0`): the six tables, the six `refixes:` lines and the 35 rows,
nothing else.

**The check on this branch.** `chain_check.py --baseline
origin/release/v0.22.0 --root <worktree>` at 9a4ce364: exit 0, every record
read and none refused; it prints the three lines owed since 5d-i, round 6
behind HEAD (now as *the last round's `target:`*) and no `broad-gate.md` or
`guarantee.md`.

**S20.** The `git grep` of S20's list outside `seal/specs/` and
`changelog/0.*.md` at 9a4ce364 finds no statement of the old shape. What
it still finds, each named:

- `skills/gap-analysis/SKILL.md:50` `## Verdicts` — that skill's own report
  heading, not the round record.
- `skills/implement/orchestration.md:592` and
  `tests/test_every_orchestrator_act_names_its_delivery.py:59, 254, 415` — the
  `Grounds` cell of the orchestrator-act table.
- `tests/test_the_verifying_round_is_bounded_not_cheapest.py:96, 108` — the
  grounds cell of `docs/the-review-record.md`'s rung table.
- `skills/verify/scripts/unverified_check.py:538` and
  `tests/test_one_heading_rule_holds_to_commonmark.py:5` — history in a
  comment and a docstring.
- `tests/test_broad_gate.py:127`, `tests/test_chain_check.py:131`,
  `tests/test_the_release_seal_is_drawn.py:415` — the old-shape fixtures
  the check must refuse.
- `tests/test_chain_check.py:728-736` and
  `tests/test_a_rewritten_definition_proved_non_inferior.py:655` — the
  misspelt labels the cases plant on purpose.

`git grep -n "Verdict:"` finds the guarantee's line and its readers
(`chain_check.py#verdicts_of` and `#guarantee`, `templates/sdd-guarantee.md`,
`agents/sealer.md:49, 73`, `docs/the-review-record.md` §*The guarantee*, the
sealer cases' graders and `rule_cases.py`, `tests/test_the_sealer_guarantees.py`,
`tests/test_evals_layout.py:135`), `noninferiority.py`'s own comparison
record and its cases, `arm_check.py`'s `class Verdict:`, and the misspelt
labels of `tests/test_chain_check.py:152, 723, 760, 766` and
`tests/test_broad_gate.py:149`. `.test_durations` held three ids naming
the old fields and lost them with the prune.

**The graders read by hand.** `shape-findings` and `shape-words-only`, as
written into the cases, run through node's `RegExp` (the runner's engine,
flag `m`) against the template, round 2 of this item and five wrong
shapes: the template matches the first and not the second; round 2
matches both (its prose quotes the old marks, `questions.md` Q10); a record
with `## Verdicts`, one with `Verdict: open`, and one whose `verdict:`
stands under another heading fail the first; an emoji or a check mark
trips the second. The script asserted those seven answers.

**The regenerated cases.** `replay_targets.py --case` for the four replay
cases, `seed_defects.py --case` for the four seeded ones, `rule_cases.py`
for the fixture set: each warden case lost `shape-verdicts-table` and
gained the two graders, its truths read `^location: `, and its grader
bodies name `finding <k>` in place of a mark; the three sealer scaffolds
write the record in the current shape; the smith and framer cases came out
byte-identical.

**The prune.** 7,609 cases collected; 7,348 entries to 7,329; 19 dropped,
0.6 s, each a case 5d-i, 5d-ii or this phase removed or renamed; none
uncollected after; 280 collected cases unpriced, under the bound
`test_the_durations_file_prices_the_suite` holds, which then passed, run
and not skipped. The guard held, as in 5a.

**What moved beyond the row** is in `overview.md`'s divergence rows: the
owner's decisions and the `spec.md` sections they leave for the framer,
`noninferiority.py`'s finding rows, the documents beyond the row's files,
T39's reach, the repair that made no commit (`questions.md` Q11), and the
changelog's migration paragraph naming the old marks. `agents/framer.md:302`
and `skills/implement/orchestration.md:637` still say a round *marks* a
finding `fix of a fix`; both files are part B's, and the concept's name was
not renamed, only the label.

**The verification the row names.** `bin/test` over the row's ten modules:
exit 0, 287 passed. `bin/test tests -q -p no:xdist -k
test_the_durations_file_prices_the_suite`: exit 0, 1 passed, not skipped.
`bin/rules --check --root <worktree>`: exit 0, 419 targets in 60 files.
`uvx ruff check` and `uvx ruff format --check` on the fourteen touched
`.py` files and `evals/scripts/`: exit 0. Beside the row, the 84 modules
that name a document this phase touched (`docs/the-review-record.md`, the
two skills, the two definitions, the READMEs, `hygiene.yml`, the release
documents, `templates/config.md`, `templates/sdd-round.md`), at 9a4ce364:
exit 0, 3,828 passed, 10 skipped; `tests/test_the_seal_is_taken_once_by_the_sealer.py`,
whose fixture 4ed5dd39 changed, on its own at 4ed5dd39's tree: exit 0, 378
passed. Their first run at 9d61c520 found two pins on the warden's old
words, re-pointed at e6f7a000.

### 5d-iv

**The frame held.** The two sentences the row names were where it said:
`docs/the-review-record.md:61-62` and this item's `changelog.md:34-35`.
The other coordinates it lists use `rejected` for a finding that does not
hold and state no repair rule, as it says.

**The commits.** 8445feb8 the document's paragraph, T41, the module
docstring, the template's `deferred` line, the smith's fix-pass sentence
and the changelog mapping; 78b08b01 the smith's clause moved onto its own
line, so the line grep below reads it as the `deferred` it says; 274a9443
the smith's `## Phases` rider re-stamped. The rider is the one defect this
phase caused: 8445feb8 moved its section's hash, and
`tests/test_a_rider_reaches_its_file.py` went red on two cases in the
module run. The rider asks only that the waiver example above it stand
verbatim. The edit is fifty lines below the example and adds no shell
text, so it was read and re-stamped with
`rider_check.py --reverify --only agents/smith.md`, not re-measured.

**The red run.** T41 added alone at 85bf9e5c's document, which is the
row's 096aafb9 document byte for byte (`git diff 096aafb9 85bf9e5c --
docs/the-review-record.md` is empty):
`bin/test tests/test_the_record_is_written_in_words.py -q -p no:xdist`,
exit 1, 1 failed and 1 passed. It failed at the outside-the-tree assertion
on the sentence *A correction to a record, or a repair made outside the
tree, produced no commit on the branch and closes `rejected` with where
the repair is.* After the rewrite, the same command gave exit 0, 2 passed.

**The mutations.** `bin/mutation-check docs/the-review-record.md`, cases
`-k test_a_repair_with_no_commit_closes_deferred_where_it_was_made`, at
8445feb8. Both breaks were `red`, the tool exited 0, and `git status
--short` was empty after each.

| Break | Where T41 failed |
|---|---|
| the outside-the-tree sentence put back to closing `rejected` | the outside-the-tree assertion |
| the `fixed <commit>` clause dropped from the record-correction sentence | the record-correction assertion |

**The class.** It was enumerated at 85bf9e5c, before the first edit, over
`agents/`, `skills/`, `docs/`, `templates/`, both READMEs and this item's
`changelog.md`. Two hits sent a repair to `rejected`, and both were
rewritten: `docs/the-review-record.md:61-62` and `changelog.md:34-35`.
Every other hit stays, for the reason given.

`git grep -n -i -E 'outside the tree|correction to a record|repair'`:

- Uses of *repair* for something other than a finding's verdict, which
  stay: `agents/smith.md:204` and `skills/code-review/orchestration.md:55`
  (a fix repairs the coordinate a finding named);
  `skills/code-review/orchestration.md:167` (the sealer's `not sound`
  repair); `docs/branch-and-release.md:352, 365`;
  `docs/issues-and-milestones.md:304`;
  `docs/release-checklist.md:29, 295, 364`;
  `docs/the-broad-gate.md:89, 90, 98, 219, 242`;
  `docs/the-record-layout.md:115, 171, 174`; `skills/config/SKILL.md:130`;
  `skills/update/SKILL.md:52, 54`; `skills/verify/SKILL.md:547`;
  `templates/config.md:276, 290`; `templates/hygiene.yml:51`.
- Code comments and docstrings about other repairs, which also stay:
  `skills/implement/scripts/seal.py:1512, 1577`;
  `skills/settle/scripts/settle.py:60`;
  `skills/verify/scripts/arm_check.py:60, 301, 702`;
  `skills/verify/scripts/broad_gate.py:341, 528, 537, 657, 1231, 1268, 2212`;
  `skills/verify/scripts/seal_stamp.py:599, 898`;
  `skills/verify/scripts/session_cost.py:1008, 2180, 2738, 2740, 2745, 2932, 3008`;
  `skills/verify/scripts/unverified_check.py:1553`.

`git grep -n -w rejected`:

- The verdict meaning *the finding does not hold*, or a `fixed` or
  `rejected` finding owing the next round a reference. These stay:
  `README.md:197`; `README.ko.md:187`; `agents/smith.md:192, 284`;
  `agents/warden.md:120, 210`; `docs/the-review-record.md:36, 71, 125,
  132, 149, 152`; `changelog.md:10, 52, 56`;
  `skills/code-review/SKILL.md:189`;
  `skills/code-review/orchestration.md:96, 115`;
  `skills/code-review/scripts/chain_check.py:19, 22, 160, 167, 168, 559,
  994, 996`; `templates/config.md:126`;
  `templates/sdd-round.md:41, 57, 82`.
- The English word, not the verdict, which stays:
  `docs/one-root-by-lifetime.md:694`;
  `docs/the-review-and-parity-arms.md:66, 75, 76, 85`;
  `skills/code-review/orchestration.md:114`;
  `skills/verify/scripts/broad_gate.py:527`;
  `templates/sdd-routing.md:77`.

At 274a9443, S25's grep for a line naming a repair, a correction or the
outside of the tree beside `` `rejected` `` found nothing outside
`seal/specs/` and `changelog/0.*.md`, and nothing in this item's
`changelog.md`. The only remaining hits are T41's own lines in
`tests/test_the_record_is_written_in_words.py:103, 105`, which are the
pin. At 8445feb8 the same grep also read `agents/smith.md:192`, because
the new clause began on the line listing the verdicts. 78b08b01 moved the
clause onto its own line.

**Beside the row.** The plan's text for the changelog mapping reads
`deferred <where>`. The fragment writes
`deferred <where it was repaired>`, the spelling the document and the
template use, so a user reads one value in both places. The six round
records hold no `rejected` finding and were not edited.

**The verification the row names.** At 274a9443: `bin/test` over the 31
modules naming a file this phase touched (`docs/the-review-record.md`,
`templates/sdd-round.md`, `agents/smith.md`, T39's module, this item's
`changelog.md`), exit 0, 1,509 passed, 6 skipped. Their first run, at
78b08b01, was the rider's two red cases above.
`bin/test tests/test_docs_line_wrap.py -q -p no:xdist` over the tree:
exit 0, 37 passed. `bin/rules --check --root <worktree>`: exit 0, 420
targets in 60 files, T41 among them. `uvx ruff check` and
`uvx ruff format --check` on `tests/test_the_record_is_written_in_words.py`:
exit 0 each. `chain_check.py --baseline origin/release/v0.22.0 --root
<worktree>`: exit 0, printing the same three owed lines as at 9a4ce364:
round 6 behind HEAD, and no `broad-gate.md` or `guarantee.md`.

### Round 7 fix pass

**The owner's decision, 2026-10-16.** Round 7 marked four of its five
findings `regression: round-6#1`. Under `docs/the-review-record.md`
§*The run* as it stood, that sent the item back to its framer with no fix
pass. The owner ruled that a regression is a defect a fix pass's own commit
introduced, and that a defect in a phase the framer designed and the owner
approved, as 5d-i to 5d-iv were, is an ordinary finding of new work. So
round 7 got a fix pass.

The commit that adds this section states the ruling in place: §*The run*'s
paragraph, the template's `regression:` comment, the warden's sentence on
new units, the cap sentence of both READMEs and this item's `changelog.md`.
`tests/test_the_rules_have_one_owner.py::test_a_regression_is_a_defect_a_fix_passs_own_commit_made`
holds the document, the template and the warden to it. It failed against
the old paragraph before the rewrite (exit 1, 1 failed). The four findings
keep the `regression:` lines the warden wrote: the fix pass writes only
`verdict:`, `answer:` and an appended coordinate. `spec.md` states the old
rule in four places, which `overview.md`'s row *What a `regression:` line
marks* names for the framer.

### 5d-v

**The frame held.** Every coordinate the row names stood where it said at
2dbebf7c, whose code is 80636f64's (`git diff --stat 80636f64 2dbebf7c`
lists `plan.md`, `questions.md` and `spec.md` alone):
`agents/warden.md:119-123`, `:135-142`, `:212-217` and `:277`;
`skills/code-review/SKILL.md:187-191`;
`skills/code-review/orchestration.md:96`, `:113-120` and `:122-135`;
`skills/implement/orchestration.md:637`; `agents/framer.md:302-304`;
`templates/sdd-round.md:47-51`, `:62` and `:86-87`;
`docs/the-review-record.md:74-77`, `:138`, `:227-228` and `:248-259`; and
this item's `changelog.md:25-26`. Two places the row does not name were in
the class, and both were rewritten (`overview.md`): the tracker document's
pointer at the orchestration heading this phase renamed, and the
document's first paragraph, which listed the finding's lines.

**The commits.** a6695b61 the reader, the template, `templates/config.md`
and the cases in `tests/test_chain_check.py` and the language module;
5441ebdb the document, the warden, the review skill and its orchestration,
the framer, the delivery table, the tracker document's pointer, this
item's `changelog.md` and T44 and T45. No agent file's rider drifted:
`tests/test_a_rider_reaches_its_file.py` passed in the module run after
both agent edits, so nothing was re-stamped.

**The red runs.** Each case was run before the code or text it pins:

- `bin/test tests/test_chain_check.py tests/test_the_rules_have_one_owner.py
  -q -p no:xdist -k "reopens or spelling or template_is_the_record or
  test_a_close_that_does_not_hold or routed_by_comparing or owner_states or
  link_names"` on the unchanged reader and texts: exit 1, 7 failed and 14
  passed. T32's two new spellings (`Reopens: round-1#1` read as prose, so
  finding 1 stayed in the list), T42 and T38 (`'Finding' object has no
  attribute 'reopens'`), T43 (round 1's findings named only by `reopens:`
  lines refused as unnamed), rule 16's owner sentence, T44 (*§*The run*
  does not say a close that does not hold reopens*) and T45 (the bold
  sentence absent).
- `bin/test tests/test_the_pull_request_language_is_the_repositorys.py -q
  -p no:xdist` on the unchanged reader: exit 2, a collection error,
  `module 'chain_check' has no attribute 'REOPENS'`.
- After the reader and before the template: `tests/test_chain_check.py`
  exit 1, 1 failed (T38: the template's comments do not name `reopens:`)
  and 48 passed; the language module exit 1, 3 failed
  (`test_the_round_template_carries_the_fields_it_is_expected_to[reopens:]`
  and both exclusion-list cases for `reopens:`) and 113 passed.
- Green: the two modules after the template and `templates/config.md`,
  exit 0, 165 passed. The rules-owner module with the pasted-passage,
  line-wrap, delivery, rider and one-word modules after the texts: the
  first run exit 1, 3 failed — the warden's and the review skill's new
  channel sentences each shared a run of 15 words or more with the
  orchestration's `Job` row or the document's verifying-round sentence,
  and one line of `agents/framer.md` ran to 107 columns. Each was reworded
  or rewrapped, and the second run gave exit 0, 152 passed.

**The mutations.** `bin/mutation-check`, at 5441ebdb, each `red`, the tool
exiting 0 and `git status --short` empty after each:

| Break | File | Cases | Where it failed |
|---|---|---|---|
| `reopens:` references dropped from `channel`'s list | `chain_check.py` | T43 | round 1's two findings named only by `reopens:` refused as unnamed |
| the both-lines refusal dropped (`if False:`) | `chain_check.py` | T42 | findings 4 and 5 read with both relations |
| `reopens: round-<N>` accepted (`reopened_of` returning `reference_of`'s value) | `chain_check.py` | T42 | finding 2 read with `(1, None)` |
| `reopens` dropped from `MISSPELT_LABEL` | `chain_check.py` | T32 | `Reopens: round-1#1` read as prose |
| the orchestration's run-end sentence put back to *and the run ends at that round* | `skills/code-review/orchestration.md` | T44 | *the run ends at that round* found in the verifying-round section |
| §*The run*'s framer route put back as *A round carrying a `regression:` line gets no fix pass* | `docs/the-review-record.md` | T45 | the framer route's condition absent, the first route assertion |
| the loop guard's sentence dropped | `docs/the-review-record.md` | T45 | the loop guard absent |

**The class.** Enumerated at 2dbebf7c before the first edit, and again at
5441ebdb with the row's three greps outside `seal/specs/` (and
`changelog/0.*.md` for the last two).

- `git grep -n "the run ends at that round"`: at 2dbebf7c,
  `skills/code-review/orchestration.md:120`, rewritten. At 5441ebdb only
  `tests/test_the_rules_have_one_owner.py:274`, T44's absence assertion.
- `` git grep -n "regression:\` line" ``: every hit at 5441ebdb names
  `reopens:` beside it or states the regression rule.
  Naming `reopens:` on the same or the next line: `agents/warden.md:123`;
  `docs/the-review-record.md:79, 83, 148, 240`;
  `skills/code-review/SKILL.md:191`; `skills/code-review/orchestration.md:96,
  122`; `skills/code-review/scripts/chain_check.py:23, 707, 715, 1058,
  1061`; `templates/config.md:127`; `templates/sdd-round.md:72, 97`.
  Stating the regression rule: `agents/framer.md:302`,
  `agents/warden.md:137, 145`, `docs/the-review-record.md:264, 281`,
  `skills/code-review/orchestration.md:132`,
  `skills/implement/orchestration.md:637`. Test docstrings and pins, which
  stay: `tests/test_chain_check.py:584, 644, 706, 790, 1053` and
  `tests/test_the_rules_have_one_owner.py:206, 218, 222, 243, 286, 315,
  323`; the T36 docstring at `:1053` was given T43's case beside it.
- `git grep -n -i "sends the work item back to its framer\|stops the fix
  passes"`: at 2dbebf7c, `docs/the-review-record.md:248`,
  `skills/code-review/orchestration.md:122`,
  `skills/implement/orchestration.md:637` and rule 16's entry, each
  rewritten. At 5441ebdb: `templates/sdd-spec.md:67`, which says where the
  `Reframed` line goes *when the review chain sends the work item back to
  its framer* and routes nothing, so it stays; and T45's two absence pins.
  The tracker document's pointer at `docs/issues-and-milestones.md:185`
  named the old heading and is the third grep's class one word apart; it
  was rewritten to the new heading.

**Beside the row.** The reader refuses `reopens: round-<N>` through a
helper, `reopened_of`, which reads the value with `reference_of` and drops
a reference naming no finding; the row says `finding_of` reads the line
*through `reference_of`*, which it still does. The orchestration's route
table has three rows and keeps the framer's steps under *The framer's
route*. `rounds/round-8.md` is not edited and its three findings stay
`deferred the frame`; `chain_check.py` reads finding 2's
`regression: round-7#3` as before.

**The verification the row names.** At 5441ebdb: `bin/test` over the
twelve modules the row lists and the modules naming a file this phase
touched (`git grep -l` over `tests/` for each path), 58 modules, exit 0,
2,806 passed, 9 skipped. `bin/rules --check --root <worktree>`: exit 0,
428 targets in 60 files, T42–T45 among them. `uvx ruff check` and
`uvx ruff format --check` on `chain_check.py`, `tests/test_chain_check.py`,
`tests/test_the_pull_request_language_is_the_repositorys.py` and
`tests/test_the_rules_have_one_owner.py`: exit 0 each.
`chain_check.py --baseline origin/release/v0.22.0 --root <worktree>`:
exit 0, no record's shape refused, three owed lines: round 8 behind HEAD
(a6695b61 touches `chain_check.py`, so a verifying round is owed), and no
`broad-gate.md` or `guarantee.md`. The full suite was not run:
`unverified`, the sealer's.
