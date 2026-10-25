# Phase 1: 1792926874-the-records-carry-no-comment-and-the-readers-drop-it

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 3ae1bbed |

## What this phase was asked

Build phase 1 as one commit, as `plan.md` *Phases* row 1 and *Technical context* "How the strip is made" say. The strip script lives outside the tree, runs before the readers change, asserts every substitution, and asserts S1 per file. Record S1's file count and differing count, S2's command and output, and S11's parse of the specs the strip changes. Answer `questions.md` Q2 and Q3, the two measurements. Build Q1's default (a): no strip command. Show each new case red against the old code before the change. Run tests with `bin/test -n auto -q <files>` for the files the phase touches, and lint each changed Python file with `uvx ruff check` and `uvx ruff format --check` before the commit. The broad gate is the orchestrator's.

## What this phase found

**The strip.** The script read every tracked `.md` under `seal/specs/` except `routing.md`, with `unverified_check.py` as it stood at `f7f5450a`. It walked each file outside every fence, by `fence_opener` and `fence_closes`, and removed what `comment_scan`'s inner walk blanks. A line the removal left blank went, and a blank run the removal joined kept one blank line. Every removed piece was asserted to stand in its line, to open with `<!--` unless it continued a comment from the line above, and to close with `-->` unless the line ended inside it.

- S1, executed in the same run: 173 files changed, and 0 differ. For each file, the old `readable` of the original and `blank_fences(gfm_lines(...))` of the result agree on their non-blank lines, in order, trailing whitespace removed. No file ended inside a comment.
- The strip's diff is `git show --stat 3ae1bbed -- seal/specs ':!seal/specs/1792926874-the-records-carry-no-comment-and-the-readers-drop-it'`: 173 files, 11 insertions and 1,048 deletions. The code and tests are `git show --stat 3ae1bbed -- ':!seal/specs'`: 12 files. By name, the strip changed 40 `spec.md`, 40 `plan.md`, 38 `questions.md`, 19 `overview.md`, 9 `guarantee.md` and 27 `phases/phase-N.md`. It changed no round record and no `broad-gate.md`.
- Every removal but 11 starts at the beginning of its line. The 11 are `<!-- NAME NOT IN TREE -->`, 10 in `seal/specs/1791384158-the-broad-gate-reads-its-counts-from-the-recorder/spec.md` and 1 in its `plan.md`. Six of them stood inside a table cell, which keeps the space that stood before the comment; S1 compares the line as the old reader read it, so the cells were not retouched.
- A cross-check against `hooks/blocks.py#walk`, executed: the strip removed 816 lines whole. The walk calls 806 of them a comment block, and calls the other 10 uncertain, which means it does not decide them. Those 10 are one comment block, `seal/specs/1791076830-every-file-the-plugin-reads-or-writes-names-its-encoding/spec.md:287-296` at `f7f5450a`. I read it: the template's guidance above the framer's mark, opened by `<!--` at the start of a line and closed by `-->`.
- The frame's counts differ from the reader's: 208 files against 173, 41 specs against 40, five inline comments against 11. `overview.md` *Where spec and implementation diverged* gives each with its grounds.

**Q2, executed at `f7f5450a` before the strip was written.** `rule_changes.parse`, as it stood, read the `## Rule changes` section of each of the 40 specs the strip changes: 40 parsed, 0 refused. Answer (a): all 40 were stripped.

**Q3, executed in S1's run.** No file differs under S1, and no file ends inside a comment. Answer (a): every file was stripped.

**I did not write the Status cells of Q2 and Q3.** The spawn asked for `answered 2026-10-25 by smith` in them. `agents/smith.md` *Job* names no write to `questions.md`, so the orchestrator writes the two cells from the answers above.

**S2, executed after the change.** The command:

```
python3 -c 'import glob,importlib.util,os; s=importlib.util.spec_from_file_location("uc","skills/verify/scripts/unverified_check.py"); uc=importlib.util.module_from_spec(s); s.loader.exec_module(uc); files=sorted(glob.glob("seal/specs/**/*.md",recursive=True)); hits={f:len(uc.comment_lines(uc.readable(open(f,encoding="utf-8").read()))) for f in files}; hits={f:n for f,n in hits.items() if n}; print(len(files),"files read;",len(hits),"hold a comment line;",sum(hits.values()),"lines; basenames:",sorted({os.path.basename(f) for f in hits}))'
```

Its output: `457 files read; 35 hold a comment line; 70 lines; basenames: ['routing.md']`.

**S11, executed after the change.** `rule_changes.parse`, as this commit leaves it, read the 40 stripped specs: 40 parsed, 0 refused. Over all 42 `seal/specs/*/spec.md`: 42 parsed, 0 refused.

**`unverified-check --baseline f7f5450a seal/specs/`, executed after the change.** Exit 0. `41 overviews · 62 open · 106 closed · 0 unreadable · 19 not compared`. The 19 are the stripped overviews. Each notice says the section at `f7f5450a` could not be read, and gives `unverified_check.py#COMMENT_LINE` as the reason. The strip removes no table row (S1), so the uncompared counts did not fall.

**How each new case was seen red.** The strip was written first. The test edits then ran against the old code: 21 failed, 1,079 passed. Each new case failed on its assertion except where noted:

- `tests/test_unverified_check.py`: `Test_readable::test_accepts_the_lines_with_fences_blanked_and_a_comment_as_text` read `''` where the comment line stands. `Test_check_text::test_accepts_the_rows_of_the_one_section[a bare opener mid-line]` was refused, `1 cells, expected 2`. `Test_main::test_accepts_a_base_holding_a_comment_line_as_not_compared` exited 1, the base compared and the row counted deleted. `Test_comment_lines` (two cases) and the two `comments=False` cases of `Test_liveness` and `Test_live_lines` failed on the missing function and keyword.
- `tests/test_chain_check.py`: `Test_record_findings::test_accepts_a_bare_opener_later_in_a_line_as_text` was refused by the old `unclosed`, as a comment opened at that line that never closes. `Test_comment_lines` (two cases) failed on the missing function.
- `tests/test_rule_changes.py`: `test_an_opener_nobody_closes_above_the_section_hides_no_operation` read no section, `ops` None.
- `tests/test_seal_stamp.py`: both `..._holding_a_comment_line_queues_nothing` cases queued a stamp.
- `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`: the three changed `readable` cells read `not read`.
- Five refusing cases failed first on the missing `COMMENT_LINE`: `Test_check_text::test_refuses_a_comment_line_at_its_line`, and in `tests/test_chain_check.py` the `test_refuses_a_comment_line_at_its_line` of `Test_record_findings`, `Test_guarantee` and `Test_broad_gate`, and `tests/test_rule_changes.py::test_a_comment_line_in_the_section_is_refused_at_its_line`. Each was then shown red with its refusal removed, by `mutation-check` below.

**`mutation-check`, executed after the commit.** 17 mutants, 17 red, 0 survived:

- `unverified_check.py`, 5: `comment_lines` without the `lstrip`, `check_text`'s refusal off, `liveness` ignoring `comments`, and `live_lines` dropping `comments` from either reading.
- `chain_check.py`, 5: `comment_lines` returning nothing, `read_whole`, `guarantee` and `broad_gate` each without it, and `unclosed` refusing no fence.
- `rule_changes.py`, 5: the section's refusal off, and `parse`'s `headings`, `live_lines` and `liveness` each read with the comment state on, and `headings` dropping `comments`.
- `seal_stamp.py`, 2: each read of `guarantee.md` without the refusal.

**Tests, executed.** Every test module that loads one of the changed scripts, with `tests/test_routing.py` and `tests/test_a_record_carries_no_comment.py`, before the commit: 3,610 passed, 9 skipped, and 1 failed. The failure was `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, for this work item, which had no `overview.md`. The commit adds it, and the module then passed, 26 cases. S9's four files, `tests/test_gather_changelog.py`, `tests/test_config.py`, `tests/test_routing.py` and `tests/test_blocks.py`, are among the modules run, unchanged. `test-layout --check` and `--pairs` over the five changed test files of a `TARGET`: 0 refused, 0 pairs.

**Cases removed or rewritten, and why.** `Test_comment_scan` and `Test_strip_comments` went with their functions, and `test_readable_would_erase_every_fold_record` went because `readable` no longer blanks a marker. The comment arms of `test_refuses_a_fence_or_comment_that_never_closes_at_its_opener` and `test_a_section_quoted_in_a_fence_or_a_comment_is_not_read` went, and each case keeps its fence arm under a name without the word comment. `test_refuses_a_verdict_in_a_comment_and_reads_two_lines_as_two` is now `test_refuses_to_read_two_verdict_lines_as_one`. The `Test_guarantee` arm that hid the verdict behind an unclosed comment now hides it behind an unclosed fence. In `tests/test_noninferiority.py`, `UNCLOSED` is an unclosed tilde fence, and the rows that pinned the old reader's comment misreadings went. `tests/test_a_phase_hands_the_next_one_a_record.py` reads the templates through `readable`.

**`.test_durations` still names the removed cases.** It is measured by CI runs, and no case reads a stale entry, so it was left.

**For phase 2.** `evals/scripts/replay_targets.py#labelled` and `#labelled_round` still read a record's lines with this tree's reader, which since this commit reads a comment as text.
