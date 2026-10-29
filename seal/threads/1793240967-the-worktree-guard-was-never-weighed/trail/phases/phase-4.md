# Phase 4: 1793240967-the-worktree-guard-was-never-weighed

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | aeed95df |

## What this phase was asked

Build `frame/plan.md` *Phases* row 4, the last phase. Rewrite the text that still names the guard: the skills, `CONTRIBUTING.md`, the issue template, and the hook and test comments. Write the work item's `changelog.md` in the shape of merged fragments, ending with a `### Process changes` table in the shape `templates/records/process.md` gives, because this work removes a gate and changes `skills/implement/orchestration.md`. The fragment states what a person running the plugin loses and what they no longer meet, and the line counts the phase records hold. Read phases 1 to 3's *What this phase found* first. Phase 3's sweep output adds four lines of `hooks/lib/cmdline.py` (the `drop_heredoc_bodies` docstring, the `_heredoc_split` comment, the `# RIDER:`, which must keep `# RIDER:`, and the `parse_git` docstring) and `tests/hooks/test_cmdline.py:318`. The sweep misses `tests/hooks/test_cmdline.py:259` and the `split_segments_with_separators` docstring. Build on `frame/questions.md` P1's default (a). Run the sweep, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/github/test_rules.py` and `bin/seal layout --check tests`. Do not merge the release branch, and do not move the plugin's version.

## What this phase found

**The frame holds, with three divergences.** `gaps.md` records each as a row. A suite case read the paragraph row 4 removes from `skills/implement/SKILL.md`. Text naming the guard or its files stood in eight places `## Removes` does not list. The sweep prints one line S7 does not list.

**Removing the `SKILL.md` paragraph turned a case red that the plan does not name.** `tests/text/test_the_rules_claude_md_names_have_one_home.py` keeps, for each rule, sentences only the rule's home writes. Its cadence rule held "*Commit as you go* alone does not settle the cadence.", the first sentence of the removed paragraph. The case went red (executed, exit 1). The needle is now the section's bold rule, "**Commit at the smallest step that stands on its own.**", which no other file writes (executed, `git grep`). The case passes (executed, exit 0), and `seal mutate` replacing that sentence turns it red (executed, exit 0, verdict red).

**The sweep after `aeed95df` prints three lines outside the records and the replay eval (executed, `git grep`, exit 0):**

```
docs/the-review-record.md:633:which is why the worktree guard never reads it as consent. It is read
docs/the-routing-check.md:81:routing question, read through `hooks/worktree_consent.py#automation_answered`,
tests/hooks/test_root_migrate.py:927:        assert (git_dir / "agentic-leases" / "s1").is_file()
```

The two `docs/` lines are the ones `frame/design.md` *Rule changes* corrects at the settle. Inside the records at `aeed95df`, the sweep matches 104 lines of this work item, its changelog fragment among them, 306 lines of 13 other work items, and one line of `evals/behaviour/proofer/replay-1791779434-r5/`. `tests/hooks/test_root_migrate.py:927` pins `hooks/root-migrate.py#STATE_NAMES` renaming an earlier release's `specseal-leases`, and it stays (`gaps.md`).

**Text the sweep does not match was rewritten too.** Phase 2's record named `seal/README.md:51`, `skills/implement/scripts/seal.py:56` and `hooks/lib/routing.py:447`. `templates/setup/seal-README.md` carries the same line as `seal/README.md`, and `tests/behaviour/test_first_setup_asks_once.py` requires the two to stay equal (executed, exit 0). The `split_segments_with_separators` docstring, `tests/hooks/test_cmdline.py:259` and the "sibling guard" of `hooks/mode-gate.py#already_asked` were rewritten as well. No comment now names `apply_chdir`, `project_slug`, a lease or the worktree choices outside the records.

**The rider in `hooks/lib/cmdline.py` keeps its marker and has no reader.** It now says `--git-dir` and `--work-tree` name no directory in `chdirs`, and that no reader follows `chdirs`: `hooks/implementer-notice.py` judges the session's own repository from the payload's `cwd` (read, `notify`). `chdirs` and the separator `split_segments_with_separators` keeps are outputs nobody reads now. `gaps.md` *Not done* records them.

**The guard this work removes still runs in the session that removes it.** The plugin copy installed under `~/.claude/plugins/cache/agenticseal/agentic/0.24.0` refused a `bash -c` command holding `git diff`, run to lint this phase's files, with a Korean prompt naming `hooks/worktree-guard.py`'s `LEAVES_THE_TREE`. The lint ran again with the file names written out. This is one more instance of the cost `frame/design.md` *The record* counts, and it ends when this release is installed.

**Narrow runs over the working tree that became `aeed95df` (executed, each exit 0):** `tests/behaviour/test_a_cited_section_stands_in_its_file.py` 23 passed, `tests/github/test_rules.py` 59, `tests/text/test_the_rules_claude_md_names_have_one_home.py` 6, `tests/hooks/test_cmdline.py` 23, `tests/behaviour/test_chain_hooks_hardening.py` 30, `tests/text/test_a_rider_reaches_its_file.py` 8, `tests/hooks/test_implementer_notice.py` 26, `tests/skills/test_seal.py -k "beside_the_root or export"` 18, `tests/behaviour/test_first_setup_asks_once.py` 50, `tests/hooks/test_mode_gate.py` 33, `tests/hooks/test_review_skill_gate.py` 18, `tests/hooks/test_question_gate.py` 25, `tests/hooks/test_implementer_mark.py` 10 and `tests/hooks/test_sealer_stamp_queue.py` 24. `bin/seal layout --check tests` read 152 files and refused none. `uvx ruff check` and `uvx ruff format --check` over the 14 changed Python files exit 0.

**No unit was added, so no mutation run is owed beyond the needle's.** Every other change is a comment, a docstring, prose or a fixture name. Phase 4 adds no case, so `.test_durations` gains no unpriced entry.
