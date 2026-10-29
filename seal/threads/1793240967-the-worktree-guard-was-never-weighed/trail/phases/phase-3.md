# Phase 3: 1793240967-the-worktree-guard-was-never-weighed

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 4c9abc11 |

## What this phase was asked

Build `frame/plan.md` *Phases* row 3 and nothing of row 4. Remove `hooks/lib/cmdline_base.py`, `hooks/lib/tokens.py` and `hooks/lib/one_heredoc.py` with their tests, prune `hooks/lib/cmdline.py` to what `hooks/implementer-notice.py` reaches, and re-cite the full-history example. Read phase 1's and phase 2's *What this phase found* first. Answer `frame/questions.md` M1 and W1 in this record; the orchestrator writes their Status cells. Do not merge the release branch, where #1142 has edited `tests/censuses.py`'s `KEPT_OLD_NAMES` comment. A removal is proved by the cases that still stand passing and by the removed cases going with their code; a red-first case is owed only for new behaviour. Write `## What this phase found` for phase 4's crafter, and add rows to `gaps.md` for each divergence, unverified item or fed-back clause.

## What this phase found

**The frame holds, with four divergences.** `gaps.md` records each as a row. The full-history citation went to another case than the plan names, because M1's measurement answered no. Two removals went beyond `## Removes`: the `stand_in` parameter of `command_word` and the constant `VACATED_KEPT_FILES`. One case was added although the frame plants none, because a mutant of the edited `command_word` survived. Docstrings that gave the removed token reader as their reason were rewritten here and not in phase 4.

**M1: the replay case does not need history (executed).** In a clone made with `git clone --depth 1 --no-tags` from this branch at `d0c8eb59`, `tests/evals/test_replay_targets.py -k test_a_named_case_is_read_at_every_release_tag` passed (exit 0, 2 passed). Its body replaces `last_tags`, `targets` and `origin_url` with stand-ins, so it reads no tag and no commit. In the same clone, `tests/behaviour/test_release_hygiene.py` failed on `test_this_checkout_has_tags_to_read_the_shipped_set_from` and `test_the_illustrative_version_is_not_one_this_repository_could_ship` (exit 1), because `shipped_tags` reads no `v*` tag. The frozen-reading case skipped there, as its old citation said. So `fetch-depth: 0` keeps its reason. `.github/workflows/test.yml` and `tests/text/test_ci_gives_the_checks_what_they_need.py` now cite the tag case. The clone was deleted after the run.

**The full-history check lost its silent case.** `test_every_job_that_runs_pytest_has_the_whole_history` was written because a case that resolved an old commit skipped at depth 1. No case in the suite skips on a missing commit now (read: every `pytest.skip` and `skipif` under `tests/`). The tag cases fail at depth 1 instead of skipping. Whether the workflow check still earns its place is not this phase's to decide; `gaps.md` *Not done* records it.

**W1: the name closure holds, and no case showed a dropped definition reached (executed).** After the prune, an `ast` closure from `drop_comments`, `drop_heredoc_bodies`, `parse_git` and `split_segments` keeps all 18 top-level names of `hooks/lib/cmdline.py` and drops none. The 20 names `## Removes` lists are gone. `hooks/implementer-notice.py` holds no `getattr` and no `importlib`, and no other file under `hooks/`, `tests/` or `skills/` imports `cmdline` (`git grep`). `tests/hooks/test_cmdline.py`, `tests/hooks/test_implementer_notice.py` and `tests/hooks/test_dispatch.py` pass. The file is 925 lines, down from 1,382.

**`command_word` lost its `stand_in` parameter.** Only the guard passed a value other than `git`, to find an `eval`'s argument. The literal `git` now stands in. A mutant that looks for `gitx` instead survived `tests/hooks/test_cmdline.py` and `tests/hooks/test_implementer_notice.py` (executed, `seal mutate` exit 1, 48 passed). The `WRAPPED` table names every runner shape, and since #1027 no case read it beyond the names. `Test_parse_git::test_accepts_a_commit_behind_every_enumerated_wrapper` reads a commit through each shape. It was red under that mutant (executed, `seal mutate` exit 0, verdict red, 'arch', 'caffeinate', 'chroot' and more missed) and passes against the tree.

**The dispatcher still names the notice when `cmdline.py` breaks.** `tests/hooks/test_dispatch.py` passes, its `cmdline` parameter included (executed, 49 passed).

**Narrow runs, after the last code commit `4c9abc11` (executed, each exit 0):** `tests/hooks/test_cmdline.py` 23 passed, `tests/hooks/test_implementer_notice.py` 26 passed. Over `48ed5ae3` (executed, each exit 0): `tests/hooks/test_dispatch.py` 49, `tests/test_censuses.py` 175, `tests/text/test_ci_gives_the_checks_what_they_need.py` 25, `tests/github/test_rules.py` 59, `tests/text/test_a_rider_reaches_its_file.py` 8, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` 23, `tests/skills/test_test_layout.py` 82 and `tests/behaviour/test_release_hygiene.py` 33. `uvx ruff check` and `uvx ruff format --check` over the changed Python files exit 0.

**`.test_durations` lost 223 entries and keeps 6,073.** They are the 163 cases of the three deleted test files and the 60 removed cases of `tests/hooks/test_cmdline.py`. The file still parses as one JSON object (executed). The new wrapper case is not priced.

**What phase 4 needs to know.**

- The sweep of `frame/design.md` *Data & interfaces* prints, outside the records and the replay eval, the lines phase 2's record lists, less every phase 3 file, plus these in `hooks/lib/cmdline.py`: `drop_heredoc_bodies`'s docstring (`hooks/worktree-guard.py` recorded the same residual), the comment in `_heredoc_split` near "the worktree guard went silent", the `# RIDER:` of `_git_options` (`the worktree guard's apply_chdir`) and `parse_git`'s docstring ("the whole question the worktree guard answers"). It also prints `tests/hooks/test_cmdline.py`'s `Test_parse_git::test_accepts_the_command_word_behind_a_list_opener` docstring (executed, `git grep`, after `4c9abc11`).
- The sweep misses `tests/hooks/test_cmdline.py`'s `Test_drop_heredoc_bodies::test_a_hash_inside_an_expansion_closes_no_brace_in_either_model` docstring, which breaks "worktree" and "guard" across two lines.
- The rider must keep `# RIDER:`, which `tests/text/test_a_rider_reaches_its_file.py#test_the_riders_exist_where_the_rows_said_they_would` reads. Its reason names the guard's `apply_chdir`. No reader of `parse_git` follows a directory now: `hooks/implementer-notice.py` judges the session's own repository and ignores the `-C` values.
- `split_segments_with_separators`' docstring still argues for keeping the separator from "the prompt volume this exists to reduce". No caller reads the separator now; `split_segments` drops it. The sweep does not find this sentence.
