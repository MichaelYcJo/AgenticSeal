# Feature Specification: #1012 the records carry no comment and the readers drop it

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* | A mechanism stays only while its history shows what it caught against what it costs. The record readers' comment state caught nothing a record needs once records carry no comment, and in 0.22.3 it produced three reader defects: a comment opener in a code span hid verdict lines (#1000), and a fenced comment opener dropped rule-change operations twice (#988, rounds 2 and 3). |
| `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md` *Scope* item 14, and its `## Rule changes` (unsettled, so part of the policy in force) | A record a template starts carries no HTML comment, and the record readers keep their comment state only until #1012 strips the old records. That spec names the states this work removes: `unverified_check.py#comment_scan`, `#strip_comments` and `#readable`, the comment half of `chain_check.py#unclosed`, and the comment skip in `rule_changes.py#parse`. |
| `seal/specs/1792627930-the-section-sign-is-still-syntax/questions.md` Q6, the owner's answer of 2026-10-22 | The old records are stripped after the backlog settle, not before it. The settle is merged (#1024, `4d5a6917`), so this work runs now. The decision is not reopened. |
| `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md` *Scope*, out of scope | Comments a reader needs stay: the changelog markers, the `CLAUDE.md` block markers, `seal/config.md` and its parked rows, `templates/pact.md`, and `unverified_check.py#live_lines`, whose callers read files that are not records. `hooks/blocks.py`'s comment-block walk and `hooks/routing.py#shown` stay, because the routing reader runs in the commit gate of every consuming repository. |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion*, the rule *Whether a line is live is asked by what the line does* | Its third answer says `unverified_check.py#readable` blanks comment text. After this work it blanks fenced lines only. `## Rule changes` rewrites the sentence. |
| `docs/the-review-record.md` *What the check reads at the pull request* | A labelled line inside a fence or a comment is not a line, and a fence or a comment that never closes is refused. After this work only the fence half holds, and a line beginning `<!--` is refused at its line. The same section says the check judges every `routing.md` a pull request's own commits add or change, which is why this work strips no `routing.md` (*Scope* item 5). |
| `docs/the-record-layout.md` *seal/specs/<work-item-id>/* | Where the rule this work adds lands, after the two rules 1792627930 adds to the same section. |
| `skills/settle/SKILL.md` *Rule changes* and *A rule has one shape* | The grammar of `## Rule changes`. A rule whose test drives a script that can fail a required pull-request job names a marker on its check line, so the new rule names the marker `record-comment-line-refused`. |
| `docs/the-record-layout.md` *The unverified record, and the baseline it is read against*, and `unverified_check.py#main` (read: the `--baseline` loop, where a base section that cannot be read is a `not compared` notice) | A base overview holding a comment line is reported as not compared, never counted as zero rows. |

## Scope

**In scope.**

1. **The records under `seal/specs/` lose their HTML comments, in one commit with items 2 and 3.** Every record file except `routing.md` (item 5) loses each HTML comment that stands outside every fence. A comment inside a fence is part of a quoted fix and stays. At `f6650b8b`, 219 tracked files under `seal/specs/` hold `<!--` on 340 lines (executed: `git grep -l -F '<!--' -- seal/specs | wc -l`, and the same without `-l`). 283 of those lines begin with `<!--` after leading whitespace (executed: `git grep -h -E`), and an awk reading of the fence rule puts 273 of them outside every fence, in 208 files, as comment blocks spanning about 4,079 lines; the other 10 stand inside fences (executed; a regex count, not the shared reader's). 57 lines hold `<!--` later in the line. Most of them quote it in a code span, which is text and stays. Five are bare inline comments, `<!-- NAME NOT IN TREE -->` in `seal/specs/1791384158-the-broad-gate-reads-its-counts-from-the-recorder/plan.md` and `spec.md`, and nothing reads that marker any longer (read: `git grep 'NAME NOT IN TREE'` finds it in no script). The smith recounts with the shared reader at the phase's base. The comments are template guidance copied into each record, and git history keeps them.
2. **The record readers lose their comment state.** By construction, the readers that keep a comment state are the code that matches `<!--` (executed: `git grep -n -E '<!--|OPENER|CLOSER|-->' -- '*.py' ':!tests/'`). Of them, these read records, and their comment state goes:
   - `skills/verify/scripts/unverified_check.py#comment_scan` and `#strip_comments` go. `#readable` blanks fenced lines only, so a comment in what it returns is text. Its callers lose the state with it: `#check_text` (each `overview.md`), `chain_check.py` (round records, `guarantee.md`, `broad-gate.md`, and the grammar tables of `docs/the-review-record.md`, which holds no `<!--`: executed, `git grep -c -F '<!--' -- docs/` prints nothing), `seal_stamp.py` (`guarantee.md`), `.github/scripts/release_seal.py` through `chain_check.py#record_findings`, and `evals/scripts/noninferiority.py` and `evals/scripts/replay_targets.py`.
   - `skills/code-review/scripts/chain_check.py#unclosed` loses its comment half and keeps its fence half.
   - `skills/settle/scripts/rule_changes.py#parse` loses its comment skip and reads the spec with no comment state, for its headings and for its code-span refusal (#988) alike. `#headings`, as `#apply_op` and `#overlapping` call it on policy documents, keeps the comment state of `live_lines`.
3. **A record line that begins with `<!--` is refused at its line, by the reader that reads it.** The line is one outside every fence whose text, leading whitespace removed, begins with `<!--`. One function of the shared reader, `unverified_check.py`, finds such lines, and each record reader of item 2 asks it of the file it reads:
   - `chain_check.py` refuses one in a round record, a `guarantee.md` and a `broad-gate.md`, naming the file and the line.
   - `unverified_check.py#check_text` refuses one in an `overview.md`. At a base revision the refusal is the existing `not compared` notice, so the stripping pull request, and a consuming repository's, is not failed for a base it cannot edit.
   - `rule_changes.py#parse` refuses one inside the `## Rule changes` section. That is the section `settle` and `chain-check` read.
   - `seal_stamp.py` takes no stamp from a `guarantee.md` holding one, the answer it already gives a guarantee it cannot read as sealed.
   A `<!--` anywhere later in a line is text, in a code span or not.
4. **The evaluation tooling reads a historic record with the reader that judged it.** `evals/scripts/replay_targets.py` reads round records from release tags, where comments still stand: the round template carried 8 comments at `v0.21.0`, 5 at `v0.22.0` and `v0.22.2`, and none at `v0.22.3` (executed: `git show <tag>:templates/sdd-round.md | grep -c -F '<!--'`). It already judges each record with the `chain_check.py` and reader of the commit that last wrote it (`#checks_at`, `#written_at`), and then reads the record's lines with this tree's reader. After this work it reads them with the same reader it judged them by. That is the rule #985's owner decision set for the judgment, applied to the reading.
5. **What keeps reading comments, and why.**
   - `routing.md` is not stripped and not refused. Its one reader, `hooks/routing.py#shown`, keeps the comment-block walk of `hooks/blocks.py`, because it runs in the commit gate of every consuming repository (1792627930's *Scope*). `chain_check.py` reads `routing.md` through it. A strip would also put 35 declarations under this pull request's judgment: `chain_check.py#main` judges every `routing.md` the pull request's own commits change (`#changed_routing`, `#carried_by`), and 35 of the 41 work items left after the settle hold a `routing.md` with a comment (executed: `git grep -l -F '<!--' -- 'seal/specs/*/routing.md'`). All 35 declare `through the review chain`. 18 of them hold no `rounds/` directory, and 3 more hold round records with no `target:` line, the table shape from before 0.22.0 (executed: a listing of each directory and `grep -l '^target:'` over its records). `chain_check.py#records` refuses a declared chain with no round record, and `tests/test_chain_check.py`'s `test_refuses_an_old_shape_record_and_an_unclosed_fence` pins its refusal of the old shape (read), so at least those 21 would be refused. The old `routing.md` files leave with their directories at a later settle, and a new one carries no comment, because its template holds none.
   - The changelog markers (`.github/scripts/gather_changelog.py`, through `live_lines`), the `CLAUDE.md` block markers (`templates/claude-md-block.md`), `seal/config.md` (`hooks/config.py`, `skills/implement/scripts/seal.py`) and `templates/pact.md` keep their comments, and their readers keep their comment state.
   - `unverified_check.py#live_lines` and `#liveness` keep their comment state for the callers that read no record: `gather_changelog.py` on release files, `fold_check.py` on the policy root's index, and `rule_changes.py#apply_op` on policy documents.

**Out of scope.**

- Stripping `routing.md`, for the reasons in item 5.
- Refusing a mid-line `<!--`. Records quote `<!--` in code spans (most of the 57 mid-line lines at `f6650b8b`), so refusing it outside a span needs a code-span state in every record reader, the state #1000 broke. The cost is stated in `plan.md`'s *Technical context*.
- The comment state of `live_lines`, `liveness` and the `hooks/blocks.py` walk, which serve files that are not records (1792627930's *Scope*).
- Line coordinates that one record's prose gives into another record, such as `changelog.md:29` in `seal/specs/1792449518-settle-squashes-specs-into-docs-in-place/guarantee.md`. The strip moves the lines they name. A record states the moment it was written, git keeps that moment, and no check reads those coordinates (read: no workflow under `.github/workflows/` runs the coordinate kernel over `seal/specs/`).
- A command that strips a consuming repository's records. `questions.md` Q1 holds it, and the default ships none.
- The stale `from` value of `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/spec.md`'s first change to `docs/the-review-record.md` *What the check reads at the pull request*. It quotes a sentence that no longer reads that way in `docs/`. It is that work item's, and the orchestrator reports it.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the strip changes no reading | Given each record file the strip changes, when the reader before this work reads the original and the reader after it reads the stripped file, then the two `readable` results agree on their non-blank lines, in order, each with trailing whitespace removed | The smith computes the comparison over every stripped file in the run that strips them, and the phase record gives the file count and the count that differed, which is zero |
| S2 no record but `routing.md` holds a comment line | Given the tree after phase 1, when the new shared function reads every `.md` under `seal/specs/`, then it finds lines in `routing.md` files only | One command over the tree, its output in the phase record |
| S3 a round record's comment line is refused | Given a round record holding the line `<!-- a note -->`, when `chain_check.py` reads the record, then it refuses it at that line, where before it read past it | A case in `tests/test_chain_check.py`, seen red against the old code |
| S4 a mid-line opener is text | Given a round record whose `answer:` line holds a bare `<!--` that nothing closes, when `chain_check.py` reads it, then nothing is refused and every finding after it is read, where before it was refused as a comment that never closes | A case in `tests/test_chain_check.py`, seen red against the old code |
| S5 a guarantee's or a gate record's comment line is refused | Given a `guarantee.md` holding `<!-- Verdict: sealed -->` above its `Verdict: sealed` line, and a `broad-gate.md` holding a line beginning `<!--`, when `chain_check.py` reads each, then each is refused at that line | Cases in `tests/test_chain_check.py` |
| S6 an overview's comment line is refused, and a base holding one is not compared | Given an `overview.md` holding a line beginning `<!--`, when `unverified_check.py` reads it in the working tree, then it fails naming the line; when it reads one only at the `--baseline` merge base, then it prints the `not compared` notice and the exit code is the working tree's | Cases in `tests/test_unverified_check.py` |
| S7 a rule-changes comment line is refused, and a comment hides no operation | Given a spec whose `## Rule changes` holds a line beginning `<!--`, when `rule_changes.py#parse` reads it, then it is refused at that line; given a spec with an unclosed mid-line `<!--` above the section, then every operation is read; given a line beginning inside a code span an earlier line opened, then it is refused as before (#988) | Cases in `tests/test_rule_changes.py`, the first two seen red against the old code |
| S8 no stamp from a guarantee with a comment line | Given a sealed `guarantee.md` holding a line beginning `<!--`, when `seal_stamp.py` reads it, then it takes no stamp | A case in `tests/test_seal_stamp.py` |
| S9 the comments a reader needs still read | Given a changelog marker, a parked row in `seal/config.md`, a commented row in a `routing.md` and the `CLAUDE.md` block markers, when their readers run, then each reads as it did before | The existing cases in `tests/test_gather_changelog.py`, `tests/test_config.py`, `tests/test_routing.py` and `tests/test_blocks.py` pass unchanged |
| S10 replay reads history as it was judged | Given the release tags, when `replay_targets.py --list` runs at phase 2's base and at its head, then the two outputs are identical; and each committed replay case under `evals/behaviour/warden/` regenerates with `--case` into the same files | The two runs and the diffs, in the phase record |
| S11 the stripped specs still parse | Given the 41 `spec.md` files the strip changes, when `chain_check.py` parses each `## Rule changes` section, then none is refused | `rule_changes.parse` over the 41, in the phase record |

## Data & interfaces

No file format changes for a record written from today's templates, which carry no comment. The interfaces that change:

- `skills/verify/scripts/unverified_check.py`: `comment_scan` and `strip_comments` go. `readable(text)` returns `blank_fences(gfm_lines(text))`. One new function returns the indices of the lines of `readable(text)` whose text, leading whitespace removed, begins with `OPENER`, and its name is the smith's. `liveness` and `live_lines` take a keyword that turns the comment state off, true by default, so `rule_changes.py#parse` can read a record without it and every other caller is unchanged. `check_text` refuses the first comment line, at its line.
- `skills/code-review/scripts/chain_check.py`: `unclosed` keeps the fence half. The read of a round record, `guarantee` and `broad_gate` each refuse a comment line, at its line, with one message spelt once. The new message is pinned by a test (contract rule 14).
- `skills/settle/scripts/rule_changes.py`: `parse` drops `line.lstrip().startswith("<!--")`, reads with the comment state off, and refuses a section line beginning `<!--`. `headings` takes the same keyword for `parse`'s use.
- `skills/verify/scripts/seal_stamp.py`: the two reads of `guarantee.md` (`#_queue_one`, `#queue_for_local_guarantee`) take no stamp where the guarantee holds a comment line.
- `evals/scripts/replay_targets.py`: `labelled`, `labelled_round` and the readers after them read a record's lines with the reader of the commit that judged it. `evals/scripts/noninferiority.py`'s docstring and its use of `unclosed` follow `unclosed`'s new reading.
- Docstrings that describe the comment state are rewritten in place (contract rule 19): `unverified_check.py`'s module text, `#fence_spans`, `#liveness`, `#live_lines` and `#readable`; `chain_check.py#unclosed` and `#verdicts_of`; `rule_changes.py`'s module text and the comment in `#parse`; `noninferiority.py`. The smith finds the rest with `git grep` on `comment`.

## Rule changes

- change
  file: docs/the-record-layout.md
  section: The fold, and what tells it from a deletion
  from: `unverified_check.py#readable` blanks comment text and fenced lines with the indices intact, and a region nobody closed to the end of the file.
  to: `unverified_check.py#readable` blanks fenced lines with the indices
    intact, and a fence nobody closed to the end of the file. It reads a
    comment as text, because a record carries none, and the reader that
    judges a record refuses a line that begins with `<!--`.
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: A labelled line inside a fence or a comment is not a line, so a finding whose only verdict stands in its fix block has none, and a fence or a comment that never closes, which would hide every finding after it, is refused at the line that opened it.
  to: A labelled line inside a fence is not a line, so a finding whose only
    verdict stands in its fix block has none, and a fence that never closes,
    which would hide every finding after it, is refused at the line that
    opened it. A line outside every fence that begins with `<!--` is refused
    at its line, because the check reads a comment as text.
- add
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  to: **A reader of a record keeps no comment state: it reads `<!--` as
    text, and refuses at its line a line outside every fence that begins
    with `<!--`.** A record carries no comment, so a comment state in its
    reader models nothing the record holds, and that state is where three
    reader defects of one release came from. The refusal stands where the
    reader reads: `chain_check.py` in a round record, a `guarantee.md` and
    a `broad-gate.md`, `unverified_check.py` in an `overview.md`, and
    `rule_changes.py` in a spec's `## Rule changes`. A base revision that
    holds such a line is not compared, because nobody can edit a commit
    that already happened. A `routing.md` is the exception: its reader
    runs in the commit gate, where a refusal would stop each commit of a
    work item framed before its template lost its comments, so that reader
    keeps the comment walk of `hooks/blocks.py`.
    check: record-comment-line-refused

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The HTML comments outside every fence in each record under `seal/specs/` but `routing.md`: about 273 line-start blocks in 208 files, and five bare inline comments, at `f6650b8b` | every such file, enumerated at build time by the reader in force before phase 1 | Template guidance copied into each record. Its homes are the skills and agent definitions 1792627930 moved it to, and git history keeps every copy |
| The comment walk of the shared reader | `skills/verify/scripts/unverified_check.py#comment_scan`, `#strip_comments` | No record holds a comment line after the strip, and the new refusal keeps it so |
| The comment blanking in `readable` | `skills/verify/scripts/unverified_check.py#readable` | `readable` blanks fences only; a comment line is refused by the reader that reads the record |
| The comment half of the unclosed-region refusal | `skills/code-review/scripts/chain_check.py#unclosed` | The comment-line refusal of *Scope* item 3, which refuses at the opener's line as the old half did |
| The comment skip in the rule-changes reader | `skills/settle/scripts/rule_changes.py#parse` | The section refuses a line beginning `<!--`, and reads with the comment state off |
| The cases that pin the removed states | `tests/test_unverified_check.py#Test_comment_scan`, `#Test_strip_comments`; the comment arm of `tests/test_chain_check.py`'s `test_refuses_a_fence_or_comment_that_never_closes_at_its_opener` and `test_refuses_a_verdict_in_a_comment_and_reads_two_lines_as_two`; the comment arms of `tests/test_rule_changes.py`'s `test_a_section_quoted_in_a_fence_or_a_comment_is_not_read`; the `strip_comments` reads of `tests/test_a_phase_hands_the_next_one_a_record.py`; the comment rows of `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` that pin `readable`; the comment fixtures of `tests/test_noninferiority.py` | Each becomes a case of the new reading (S3 to S8), or goes where the template it read carries no comment. The smith enumerates the rest with `git grep` on `comment_scan`, `strip_comments`, `unclosed` and `<!--` under `tests/` |
| The docs sentences that state the comment state | `docs/the-record-layout.md` *The fold, and what tells it from a deletion*, `docs/the-review-record.md` *What the check reads at the pull request* | `## Rule changes` above |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-25 by framer, before the build.
