# Phase 1: 1793171931-checks-that-read-text-pass-what-they-cannot-read

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | a41783fd |

## What this phase was asked

Audit family A, readers R1 to R15 of `frame/design.md` *The readers to
audit*, at `c825fd2c`, and any pair for R43 met there. Each row's verdict
carries an executed probe recorded here. Probes live in the crafter's scratch
directory as `test_tmp_*`, are loaded by path, run once and are deleted
before the phase closes. No tree file outside the work item directory
changes.

## What this phase found

### The rows

The `Fix` cell names where the fix goes; phase 5 writes the issue number in
its place. `0.24.1 <module>` is one issue per module in `release: 0.24.1`,
and `0.24.1 limits` is the one issue that carries every `limit` sentence.

| Row | Reader | Reads and decides | On input it cannot read | Lets through | Probe | Fix |
|---|---|---|---|---|---|---|
| R1 | `hooks/lib/blocks.py#walk_text` | which lines of a markdown file a renderer hides in a fence or a comment block, for R10 and R16; returns a kind and an uncertain flag per line, and no verdict of its own | `mixed`: a fence or comment block that closes is hidden and certain; below a fence or comment nobody closed, and from a fence inside a list item on, every line is uncertain and the caller keeps its base reading | `no`: the walk decides nothing; R10 and R16 carry what their callers do with an uncertain line | a table row below a fence nobody closed: live, uncertain, the fence reported unclosed at line 2; below a `<!--` nobody closed: live, uncertain; a fence inside a list item: every line uncertain; inside a fence that closes: hidden, certain | none |
| R2 | `skills/code-review/scripts/chain_check.py#grammar` | the two tables of `docs/the-review-record.md` *The round record*, the owner's; a table it cannot read raises `GrammarError`, exit 2 at import | `mixed`: a cell it cannot read is refused at its line; a blank line inside a table ends the table there, and the rows after it are dropped unread unless one of them is a row the check reads | `limit`: a dropped old-spelling row lets a record line in that spelling through as prose, where the full table refuses it; the tables are written by the settle, not by a work item's pull request | a blank line before the `fix of a fix:` row: the grammar loads with two old spellings, and a finding line `fix of a fix: round-1#1` is then read as prose with no error, where the full grammar refuses it as `regression:` in another spelling; a `Line` cell under emphasis: refused at line 47; a blank line before the `severity:` row or the `answer:` row: refused, since a row the check reads went with it | 0.24.1 limits |
| R3 | `chain_check.py#findings`, `#record_lines`, `#confirmations`, `#round_of` | `trail/rounds/round-N.md`, the proofer's and the fix pass's; each line it cannot read is an error, and a ready pull request fails on it | `mixed`: a label in another case, under emphasis or with a homoglyph, and a finding heading at the wrong level, are refused at their line; a finding inside a fence that closes is no finding and is skipped | `yes`: an open finding written inside a closed fence reaches a ready pull request, and `records()` names no problem | `Verdict: open`: refused at line 12; `vеrdict:` with a Cyrillic `е`: refused, the finding has no verdict line; a second finding headed `#### 2.`: refused, the first finding then holds two of each label; `verdict: **open**`: refused; finding 2 at `verdict: open` inside a closed fence beside finding 1 at `deferred #1`: `records()` returned no problem, and the same record unfenced returned the open finding | 0.24.1 `chain_check.py` |
| R4 | `chain_check.py#verdicts_of`, `#verdict_word` | the `Verdict:` line of `guarantee.md`, the sealer's; a ready pull request fails unless it reads one `Verdict: sealed` | `refuses`: every near miss reads as no word or as no verdict line, and `guarantee` refuses both | `no`: nothing but the exact line reads `sealed` | `**Verdict:** sealed`, `Verdict: **sealed**`, `Verdict: Sealed`, `Verdict: sealed.`, a blockquoted line, a four-space indent and two spaces after the colon: no word; a Cyrillic `е` in the label and the verdict as a table row: no verdict line; a trailing U+200B: `sealed`, the invisible character stripped; `Verdict: sound`: the retired word, refused with its own sentence; end to end, `guarantee` refused the emphasised line | none |
| R5 | `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee`, and `#sealed_before`, which the frame names `#sealed_names` | the same line through R4's two functions, at the guarantee's write; queues the stamp a person reads as sealed | `mixed`: a verdict line R4 cannot read queues nothing; a fence nobody closed is not looked for, so a `Verdict: sealed` above one queues the stamp | `yes`: the stamp is queued for a guarantee whose unclosed fence hides a second line, `Verdict: withheld`, and the pull request's arm refuses the same file (R43) | in a scratch repository, the write read before its commit: the well-formed guarantee queued the stamp and the arm said nothing; `Verdict: sealed`, a fence nobody closed, then `Verdict: withheld reason: ...`: queued, and the arm refused it as a fence that never closes; `**Verdict:** sealed`: nothing queued, the arm refused it | 0.24.1 `seal_stamp.py` |
| R6 | `chain_check.py#target_row`, with `#target_of` and `#earlier_verdicts` | the `Target SHA` row of `guarantee.md`, the sealer's | `refuses`: a backticked or emphasised commit, a missing `against`, and `Earlier run` capitalised are each refused at the row | `no` | each of the four near misses: "is not read" at the row; a third cell after the value: read, with no refusal, and the cell carries nothing the row is read for | none |
| R7 | `chain_check.py#frame_foot` | the framer's mark and `Reframed` lines at the foot of `frame/design.md` | `refuses`: emphasis, a missing period, a comment line after the mark and a `Reframed` line with no period each leave no mark, and `frame` refuses a design with none; `by Framer` is read, and `frame` refuses a mark naming anyone but the framer | `no`: the date is not read for its shape, and it is not what the check exists to stop | the mark under emphasis, with no period, followed by a comment line, and followed by a `Reframed` line with no period: no mark; `by Framer`: read as `Framer`; `Framed yesterday by framer, ...`: read | none |
| R8 | `chain_check.py#routing_trailers`, `#trailer_findings` | `Seal-Routing` trailers of the pull request's commits, any committer's | `mixed`: a value in another case or with a trailing mark is refused as a work item no declaration names; a key git does not read as `Seal-Routing` is no trailer, and that commit is not judged | `limit`: `docs/the-routing-check.md:115-117` already states that a commit with no such trailer is not judged, a session's that dropped it included | six commits in a scratch repository: git read `Seal-Routing:`, `seal-routing:` and `Seal-Routing :` as the key, and not `SealRouting:`; `No work item` and `no work item.` were each a problem; five problems and no notice | none: the limit sentence stands |
| R9 | `chain_check.py#original_of`, `#originals_of` | `original:` lines of round records and of `guarantee.md`, in a migration repository | `mixed`: in a round record a misspelt `original:` is refused by `round_of`; in the guarantee of a work item answering `straight to the PR` a misspelt one counts as present, and nothing reads it | `yes`: a guarantee naming another baseline as `Original: 0000000` passes the parity arm, where `original: 0000000` is refused | in a scratch migration repository, straight to the PR: `Original: 0000000`, `**original:** 0000000` and `original:0000000` each passed the parity arm and the guarantee arm; `original: 0000000` was refused as another commit; no line was refused as missing | 0.24.1 `chain_check.py` |
| R10 | `hooks/lib/routing.py#parse`, `#shown`, `#table_rows`, as `chain_check.py`, `hooks/routing-edit-gate.py#decide` and `hooks/question-gate.py#main` call them | `routing.md`, the orchestrator's | `mixed`: a `Review`, `Destination` or `Branch` value it cannot read makes the file no declaration, so the edit gate denies and the pull request check refuses; an `Automation` value it cannot read is unanswered, and the question gate lets the question through | `yes`: on a branch whose `routing.md` reads `Automation` `Yes`, the question gate allows a question, the stopped run it exists to end | `parse`: `Yes`, `**yes**` and a backticked `yes` read as no answer, `yes` with a trailing space reads `yes`; the question gate in a scratch repository: `yes` denied, `Yes` and `**yes**` exited 0 with no output; the edit gate on `Through the review chain`: denied; a backticked branch is read with its backticks and names no branch | #1038: `parse` reads an unreadable optional row as unanswered on purpose (its docstring), and `docs/the-record-layout.md:153-172` says a declaring line is not taken on doubt, so failing closed here is a rule change for every reader of `routing.md` |
| R11 | `hooks/lib/routing.py#rounds`, `#rounds_unreadable`, `#stray_rounds`, with `chain_check.py#round_records` | the file names under `trail/rounds/` | `skips`: a name `round_number` does not match is no record, in the working tree and at HEAD, and neither `rounds_unreadable` nor `stray_rounds` names it | `yes`: a misnamed round holding an open finding, beside a clean `round-1.md`, passes `records()` | `round-2.md`: its open finding refused; `Round-2.md`, `round_2.md` and `round-2.MD`: `records()` named no problem; `rounds()` listed `round-1.md` alone, `rounds_unreadable` was False and `stray_rounds` empty | 0.24.1 `chain_check.py` |
| R12 | `skills/settle/scripts/rule_changes.py#parse` | `## Rule changes` of `frame/design.md`, the framer's | `mixed`: a heading whose letters spell `Rule changes` and every off-shape item line are refused at their line; a heading whose letters differ is no section, so the pull request check says nothing | `no`: `settle` lists a design with no section to be read whole (`skills/settle/scripts/settle.py:521-522`, read), so no rule change is dropped | `## Rule Changes`: refused as a near miss; `## Rule change`: no section, no error; `- Change`, a field indented three spaces, a backticked file and `- **nothing**`: each refused at its line | none |
| R13 | `skills/verify/scripts/unverified_check.py#check_text`, `#parse_section`, `#nothing_block`, `#closing_word`, `#live_lines` | `## Not verified` of `gaps.md`, the crafter's and the orchestrator's | `refuses`: every near miss of the heading, the closing word, the cell count, the nothing block, and a line after the table, is refused at its line; `**closed** suite` reads as an open row | `no`: a closing word it cannot read leaves the row open, the direction the module chooses | `## Not Verified`, `## **Not verified**`, `### Not verified` and `## Not verified:`: no section, refused naming the near miss; `Closed suite` and `closed: suite`: refused; three cells: refused; `**closed** suite`: one open row | none |
| R14 | `skills/verify/scripts/deferral_check.py#inspect`, `#runners_in`, `#read_events` | CI workflow files a person wrote, read to say whether a named answerer runs a kind of check before merge | `passes`: an `on:` block it cannot read yields no event, and a workflow with no event that runs the kind counts as answering | `yes`: a workflow that runs `pytest` only on push answers the deferral, exit 0, where the same file keyed `on:` at two spaces reads `too late` | `on:` with `push:`: `too late`; `"on":` with `push:`: `answers ... (trigger unread)`; `on:` with `push:` indented four spaces: `answers ... (trigger unread)`; `run: echo skip pytest`: read as a runner | 0.24.1 `deferral_check.py` |
| R15 | `skills/code-review/scripts/pr_body.py#_check`, `#split` | a pull request body file, the orchestrator's, held against the records | `refuses`: a line that differs from the records' line is refused at it, and a heading line with a trailing space is no heading | `no` | a trailing space, added emphasis, and the heading with a trailing space: each refused; CRLF line ends: matches, the lines being the same | none |

### Pairs for R43

- R4 and R5 read one `Verdict:` line with one reader, and disagree on a
  fence nobody closed: the pull request's `guarantee` refuses the file, and
  the stamp is queued for it (R5's probe).
- `pr_body.py` reads round records through `chain_check.py`'s grammar, the
  same reader as R3, so the two cannot disagree on a record line (read,
  `pr_body.py:27-29`).
- `routing.parse` is the one reader of `routing.md` for the edit gate, the
  question gate and the pull request check; the three disagree only where
  `parse` reads a row as optional, which is R10's `Automation` arm.

### Where the frame does not hold

- R5 names `seal_stamp.py#sealed_names`. That function composes the label
  `<branch> @ <tree> against <base>` and reads no `Verdict:` line
  (`seal_stamp.py:703-727`, read). The reader at the frame's own coordinate,
  `:1103-1104`, is `#sealed_before`, which reads history through the same two
  functions as `queue_for_written_guarantee`. The row audits
  `#sealed_before` under that name. Its direction follows the write-time
  probe, since both ask R4's reader and neither looks for an unclosed fence
  (read, `:1100-1110`).
- R2's tree claim, "a table it cannot read stops it at exit 2, never a pass"
  (`docs/the-review-record.md:63-86`), holds for a cell it cannot read and
  not for a table a blank line cuts short.

### The probes

Two files, each loaded the readers by path from this worktree.

- `python3 -I <scratch>/test_tmp_1.py > <scratch>/out1.txt 2>&1; echo "exit $?"`
  printed `exit 1`. It printed R1 to R9 and R10's `parse` cases, then stopped
  making R10's second scratch repository: `r10-yes` and `r10-Yes` are one
  name on a case-insensitive file system. Two of its cases were measured
  wrong and were measured again by the second file: R5's guarantee was
  committed before the stamp read it, so `sealed_before` found it in history
  and nothing was queued; R3's fenced finding sat beside a `rejected` one,
  whose owed verifying round was the only refusal.
- `python3 -I <scratch>/test_tmp_1b.py > <scratch>/out1b.txt 2>&1; echo "exit $?"`
  printed `exit 0`. It ran R3, R5, R9 and R11 end to end, and R10 to R15.

Both files and the scratch repositories they made were deleted by their
recorded paths before this record was written.

### Q3

No row of this family reaches either situation `SECURITY.md` *What this
project is, and where its risk actually sits* names. Each let-through is a
check that passes a misspelt record. In a fork's pull request it yields a
check that reads green, and nothing a fork's run holds is reached by a pass.
On an untrusted local repository it yields a stamp or an allowed question.
None of them writes, reads or runs anything the check would otherwise have
stopped.
