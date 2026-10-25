# Implementation Plan: #1012 the records carry no comment and the readers drop it

Approved <date> by <who>, when `smith` was spawned.

## Summary

Strip the HTML comments from the records the backlog settle left, take the comment state out of every reader of a record, and refuse a record line that begins with `<!--` where each reader reads. The strip, the removal and the refusal land in one commit, phase 1, as the issue's step 2 asks. Phase 2 makes the evaluation tooling read a historic record with the reader that judged it, because release tags still hold commented records that this tree's reader no longer models. `routing.md` keeps its comments and its reader keeps the walk (`spec.md` *Scope* item 5).

## Technical context

The code this builds on, read at `f6650b8b`:

- `skills/verify/scripts/unverified_check.py:224` `comment_scan`, `:281` `strip_comments`, `:625` `readable` (which returns `blank_fences(strip_comments(gfm_lines(text)))`), `:350` `liveness` and `:551` `live_lines`, which hold the comment state the non-record callers keep. `:884` `check_text` reads each `overview.md` through `readable`. The `--baseline` loop in `main` (about `:1640`) turns a base it cannot read into a `not compared` notice, and `:1379` `open_record_rows` reads a base overview with the same relaxations; `settle` asks it.
- `skills/code-review/scripts/chain_check.py:1146` `unclosed`, whose comment half calls `reader.comment_scan` and `reader.strip_comments`; `:1236` `read_whole` (round records); `:1797` `broad_gate`, `:1821` `verdicts_of`, `:1850` `target_row`, `:1860` `guarantee`; `:396` `grammar`, which reads `docs/the-review-record.md` through `readable`. `:2060` onward is `main`: a `routing.md` the pull request's own commits change is judged whole, and a changed `spec.md` is parsed.
- `skills/settle/scripts/rule_changes.py:78` `parse`: `:101` reads `live_lines`, `:109` reads `liveness(lines, spans_cross_lines=False)`, and `:121` skips a line beginning `<!--`. `:61` `headings` serves `parse`, `#apply_op` and `#overlapping`.
- `skills/verify/scripts/seal_stamp.py:1190` `_queue_one` and `:1281` `queue_for_local_guarantee` read `guarantee.md` through `chain_check.py`'s readers.
- `evals/scripts/replay_targets.py:162` `record_reader` (this tree's reader), `:203` `checks_at` (the reader of the commit that wrote a record), `:228` `labelled`, `:237` `labelled_round`. `evals/scripts/noninferiority.py:306` calls `readable` and `unclosed`.
- `hooks/routing.py:125` `shown` and `hooks/config.py` read through `hooks/blocks.py#walk`, and stay.

**What each phase's smith runs.** The tests of the modules the phase touches, as contract rule 2 says, with `bin/test -n auto -q <files>` where it helps. The broad gate is the orchestrator's, after the review rounds settle.

**How the strip is made.** It is 208 files, so it is produced by a script the smith writes outside the tree and does not commit, with nothing after this commit to read it. Contract rule 9 allows that where the environment leaves no choice, on the condition that every substitution is asserted. The script runs before the readers change, against the reader in force, and does three things in one run:

1. It enumerates each comment through `comment_scan`, skipping every line inside a fence by `hooks/blocks.py`'s fence rule.
2. It removes each comment. A line left blank by the removal goes, and a removal that joins two runs of blank lines leaves one blank line.
3. It asserts S1 for every file it changes, the old `readable` of the original against a fence-only reading of the result, comparing non-blank lines with trailing whitespace removed.

A file whose comparison fails is written only after the smith reads the difference and finds it to be the old reader's own misreading, not the strip's (`questions.md` Q3). The phase record names each such file, because it is a place where the old reader hid something a renderer shows.

**The failure scenario in six months.** A record writer, an agent or a person, puts a comment in the middle of a line, such as `verdict: fixed abc1234 <!-- see round 2 -->`. A renderer hides it, and the check now reads the comment as part of the value. Most such values fail their shape, and the refusal is loud. The silent case is a mid-line opener on one line whose `-->` closes lines below: the renderer hides the lines between, while the check reads them, the permissive direction. The plan accepts it. Refusing it needs a code-span state in every record reader, the state #1000 broke, and records quote `<!--` in code spans often. The warden's reading of each record, and the orchestrator's against the template, are what catch it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the comment state in the record readers, and only strip the records | The state stays modelled for records that hold no comment. Three defects in one release came from it (#1000, #988 rounds 2 and 3), and each new reader of a record has to model it again | Rejected. The owner decided the removal (1792627930's Q6), and the premise that kept the state, records carrying template comments, is false once the strip lands |
| Remove the state and refuse nothing, reading a comment as text | An old record a consuming repository still carries reads its template comment as content: `check_text` reads the old overview template's indented example rows inside `## Not verified`, and a round record's comment lines read as prose inside a finding. Each failure is a parse error far from its cause, or a silent miscount | Rejected. The refusal names the line and the fix |
| Refuse every `<!--` outside a code span, not only at a line start | Needs a code-span state in every record reader, the state that broke in #1000; 57 lines at `f6650b8b` hold `<!--` after the start of the line, most of them quoted in spans | Rejected. The cost is the mid-line case in *Technical context* |
| A tree-wide case refusing a comment line in every record file, `plan.md`, `questions.md` and `phases/` included | It gates files no reader reads, against `CLAUDE.md` *The rule a mechanism is kept against*: a check gates only a fact it reads. A comment in `plan.md` misleads no check | Rejected. Each reader refuses in what it reads; the files no reader reads are stripped once, by this work |
| Strip `routing.md` too | `chain_check.py#main` judges every `routing.md` this pull request's commits change. 35 declarations would be judged as this pull request's own, and at least 21 of them hold no round record or only table-shaped ones (`spec.md` *Scope* item 5). The pull request goes red on records nobody can repair | Rejected. Its reader keeps the walk, so its comments mislead nothing, and the files leave at a later settle |
| Strip `routing.md`, and make `chain_check.py` ignore a change to it that only removes comments | A rule for one transition, kept after the transition ends, and a second idea of "changed" beside git's | Rejected for the same reason |
| Replace `readable` with a fence-free reading as well | A finding's paste-ready fix stays fenced, and a fix to a record's own grammar can hold a line shaped like a label (1792627930's *Scope* item 12). Dropping the fence state would read that line as the record's own | Rejected. The premise that keeps `readable`'s fence blanking was checked: the fence rule's case in `tests/test_chain_check.py` and the 10 fenced comment lines at `f6650b8b`, all inside fixes in `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/rounds/` |
| Give `rule_changes.py#parse` its own record reading: a keyword on `liveness` and `live_lines` that turns the comment state off | One walk, one switch, every other caller unchanged by default | Chosen |
| Give `parse` a second walk, with fences and spans and no comments | Two copies of the span walk, the duplication #491 and #1005 removed | Rejected |
| Keep `parse` on `live_lines` and refuse every line-start `<!--` anywhere in the spec | A mid-line opener nobody closes above the section still hides every operation below it, the class #988 found twice; and `settle` would hold every released spec whose header still carries the old template's comment, in a consuming repository | Rejected |
| At the `--baseline` merge base, keep stripping comments, so the stripping pull request still compares its 19 commented overviews | Keeps the comment walk alive for bases only, a relaxation that never ends while any consumer's base holds an old overview | Rejected. A base holding a comment line takes the existing `not compared` notice. The cost is that a row deleted in the stripping commit itself goes uncompared once, and the review reads the strip diff, which only removes lines |
| Land the strip and the reader change as two commits, each green | Two commits are each green: the old readers read stripped records the same (S1). The review would read a mechanical diff apart from the logic | Rejected, because the issue's step 2 asks for one commit, and nothing makes one impossible. Phase 1's record lists the strip's files apart from the code so the review can read them separately |
| Read historic records in `replay_targets.py` with this tree's reader | The release tags hold rounds written from templates with 5 to 8 comments (`spec.md` *Scope* item 4); this tree's reader reads them as text, and the comment under `## Findings` at `v0.22.2` holds indented guide lines shaped like labels, `severity:`, `location:`, `evidence:` and `verdict:` (read: `git show v0.22.2:templates/sdd-round.md`), which a reading without the comment state meets inside the findings section | Rejected. Phase 2 reads each record with the reader that judged it |
| Ship a command that strips a consuming repository's records | One more script with tests, for a transition each repository makes once | Not built by default. `questions.md` Q1 holds the owner's choice |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | One commit: the strip of *Scope* item 1, the comment state removed from the readers of item 2, the refusal of item 3 with its message pinned, the docstrings rewritten, and every case that pinned the old state rewritten or removed | `tests/test_unverified_check.py`, `tests/test_chain_check.py`, `tests/test_rule_changes.py`, `tests/test_seal_stamp.py`, `tests/test_noninferiority.py`, `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/test_a_phase_hands_the_next_one_a_record.py`, `tests/test_a_record_carries_no_comment.py`, and S9's four files, green; S1's comparison and S2's command, their output in the phase record; S11's parse of the 41 specs; `unverified_check.py --baseline <phase base> seal/specs/`, its exit code and its notices; each new case shown red against the old code (contract rule 15) | |
| 2 | `evals/scripts/replay_targets.py` reads a historic record's lines with the reader of the commit that judged it (*Scope* item 4) | `tests/test_replay_targets.py` green; S10, `--list` at the phase's base and head identical, and `--case` for each committed replay case regenerating identical files | |

## Operational impact

**The release note carries the consuming-repository case.** After a consuming repository upgrades, a record under its `seal/specs/` that holds a line beginning `<!--` outside a fence is refused at that line until the comment is removed:

- `unverified-check` reads every `overview.md` under `seal/specs/` on every pull request, so an old overview in any directory turns every pull request red, not only one that touches it.
- `chain-check` refuses a round record, `guarantee.md` or `broad-gate.md` of each work item the pull request declares, so an in-flight work item framed under the old templates is refused until its records are stripped.
- `settle` keeps the directory of a released work item whose `overview.md` holds such a line, at the tree or at the merge base of `origin/main` (`unverified_check.py#open_record_rows`), and holds a spec whose `## Rule changes` holds one.

The comments are template guidance that nothing reads, and `routing.md` and `seal/config.md` are not affected. The orchestrator writes this into the work item's `changelog.md` before the sealer is spawned.

**This repository's next settle.** The 41 directories left after #1024 are stripped by this work. `settle` reads a released spec at `origin/main`, and `main` holds the stripped records only once 0.22.4 merges, so the next settle runs after that merge, as #1024's did.

**This spec's rule changes wait on earlier ones.** Its places overlap those of 1792627930 (`docs/the-record-layout.md` *seal/specs/<work-item-id>/*), 1792628098 (*The fold, and what tells it from a deletion*) and 1792619408 (`docs/the-review-record.md` *What the check reads at the pull request*), all three still in `seal/specs/`. `rule_changes.py#replay` makes a later spec wait while an earlier one at an overlapping place is refused. 1792619408's first `from` no longer matches `docs/` (read: `docs/the-review-record.md:181`), so until that is repaired this spec's change at that place waits behind it.

No migration, environment variable or dependency is added.
