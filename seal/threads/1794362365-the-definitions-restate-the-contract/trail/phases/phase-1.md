# Phase 1: 1794362365-the-definitions-restate-the-contract

## What this phase found

**The frame holds, and the build departs from it in two places.** Before the build, the coordinates of `frame/design.md` G5 to G13 and of *Removes* were opened at `4effb3ab6`, whose tree outside this work item's directory is `9c6907942`'s (executed: `git diff --stat 9c6907942 HEAD` lists the four files of this directory alone). `wc -c` printed G16's sizes for all seven files (executed). Every text T1 to T24 has its old text in place at the coordinate the frame gives (read). Judged against `frame/design.md` *Scope* and `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*. The two departures follow, and the statements of the frame that HEAD now contradicts go to the orchestrator in the hand-back, because this phase does not write the frame.

**Departure 1: the headings of rules 7 and 17 are shorter than T1 and T2 give them.** T1's heading and T2's heading are each 105 columns. `tests/behaviour/test_docs_line_wrap.py` covers `skills/agent-contract/SKILL.md` at 88 display columns, and a Markdown heading cannot wrap (executed: the case failed on lines 87 and 183). The frame measured its texts unwrapped (G17), so it did not see this. The headings now read:

- ``## 7 A probe is named `test_tmp_*`, run once, and leaves nothing outside your scratch``
- ``## 17 Name your scratch for the work item, remove nothing, stop only what you started``

Each keeps T1's or T2's subject. Rule 7's body still opens "A probe is one file named `test_tmp_*`", and "your scratch" is the word the definitions' leads use. The contract therefore holds 12,779 B, 40 B under G17's 12,819 B, and 7 fewer words than G18's reading with the texts in place. Grounds: S10 asks the narrow cases to pass, S11 keeps the diff to the files *Scope* names, and contract rule 18 lets a check that refuses correct text be fixed, but a heading over the limit is the case the check exists for. Judged against `frame/design.md` S10 and S11.

**Departure 2: the proofer's case reads its scratch directory quoted whole.** `test_the_wardens_clone_is_named_for_the_work_item_and_the_round` checked `<scratchpad>/<work-item-id>/round-<n>/` with a plain substring test. The clone's path, `<scratchpad>/<work-item-id>/round-<n>/clone`, begins with that spelling, so the clause stayed green with T11's directory sentence deleted. That held at `9c6907942` too, because both spellings stood there (read). This phase changed the clause's message, so contract rule 15 owed it a red, and it could not go red. It now reads the spelling inside backticks, which only the directory sentence holds. Commit `18f699ddd`. Judged against contract rule 15.

**Rule 17's case pins "share one scratchpad", not the words "share" and "scratchpad".** Rule 17 also says "Never delete by glob in a directory another session shares", and its directory spelling holds "scratchpad", so a clause on the two words stays green with the reason's sentence deleted. Its third clause, "add `-2` to the leaf", holds S7. The case pins no sentence on "Nobody removes", because *Scope* item 11 names the clauses and `frame/plan.md` *Alternatives considered* row 13 declines a pin for each kept narrowing. Judged against contract rule 15 and `agents/crafter.md` *A new test starts from its group*. The module was read whole as the group before the cases were written, and the new cases join it (read).

**`.test_durations:5786` keeps its entry for the removed case.** `CONTRIBUTING.md` *Running the checks* says a work item never commits `.test_durations` and that whoever prepares the release refreshes it from CI's `test-durations` artifact. `tests/censuses.py#OLD_NAME_RECORDS` passes the file over as the cache the test runner rewrites (read). A stale entry unbalances the shards and drops no case. Judged against `CONTRIBUTING.md` *Running the checks* (*Scope* item 12).

**The texts went in as `frame/design.md` *Data & interfaces* gives them, apart from the two headings.** A script collapsed whitespace and found each of the 24 quoted texts in the file it belongs to (executed). Two paragraphs were rewrapped around the new words: the framer's *A question a command answers is answered by running it* and the sealer's step 2. "rule 4" in the sealer's step 7 stays on one line. Commit `f0394fa83` holds *Scope* items 1 to 12, so no sentence stood in two files or in none between commits. No case that pins a sentence this work rewrites needed a change (*Scope* item 12): the narrow run below passed with the pins as they stood (executed).

**Shown red (contract rule 15).** For each changed or added clause of *Scope* item 11, `seal mutate` ran one mutant alone, which prints the cases' output, and restored the file from its own copy. Every run read `red`, every failing line names the clause it ran for, and `git status` was clean afterwards (executed). The command was `bin/seal mutate <file> --replace <old> <new> --tests "bin/test tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py -q -p no:xdist -k <case>"`, at `18f699ddd`.

| File | Mutant | The assertion that failed |
|---|---|---|
| `skills/agent-contract/SKILL.md` | rule 17's first sentence, which names `<scratchpad>/<work-item-id>/<leaf>/`, deleted | "contract rule 17 does not name the scratch directory as `<scratchpad>/<work-item-id>/<leaf>/`" |
| `skills/agent-contract/SKILL.md` | "Agents of one session share one scratchpad, and that name keeps a parallel agent's files apart from yours." deleted | "contract rule 17 names the directory and not why: agents of one session share one scratchpad" |
| `skills/agent-contract/SKILL.md` | "Where the directory already stands … or the next number free." deleted | "contract rule 17 does not say what an agent does where its directory already stands" |
| `skills/agent-contract/SKILL.md` | rule 21's removal sentence as it stood at `9c6907942` put back | "skills/agent-contract/SKILL.md writes `rm -rf`, and no agent removes its scratch directory (contract rule 17)" |
| `agents/crafter.md` | T8's sentence deleted | "`agents/crafter.md` *Rules* does not name a phase's directory as `<scratchpad>/<work-item-id>/phase-<n>/`" |
| `agents/crafter.md` | T8's fix-pass clause deleted | "the section does not name a fix pass's directory as `<scratchpad>/<work-item-id>/fix-<n>/`" |
| `agents/proofer.md` | T11's directory clause deleted | "the section does not name the round's scratch directory as `<scratchpad>/<work-item-id>/round-<n>/`" |
| `agents/proofer.md` | T11's clone clause deleted | "`agents/proofer.md` *Rules* does not name the clone directory as `<scratchpad>/<work-item-id>/round-<n>/clone`" |
| `agents/framer.md` | T21's sentence deleted | "`agents/framer.md` *Rules* does not name the probe's directory as `<scratchpad>/<work-item-id>/frame/`" |

**No unit adds behaviour, so no `seal mutate` run was owed for one** (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, row *Prose only*). The runs above are contract rule 15's red for the changed cases.

**The scenarios**, at `18f699ddd` (executed unless stated):

- S1: `wc -c` gives `agents/crafter.md` 10,211 B, `agents/framer.md` 14,824 B, `agents/proofer.md` 10,763 B and `agents/sealer.md` 11,058 B, which is 46,856 B. At `9c6907942` the four held 48,810 B, so the work takes 1,954 B out, against the bound of 47,310 B. The crafter is 25 B and the sealer 24 B over G17's figures, from wrapping.
- S2: the census below.
- S3: `git grep -n 'read. or .unverified' -- agents` prints nothing and exits 1. At `9c6907942` it prints `agents/crafter.md:66` and `agents/sealer.md:139`. Each text T4 to T21 cites the rule or step it repeated, or keeps only the agent's own narrowing, or goes with its *Removes* row (read).
- S4: `git grep -n -i 'share one scratchpad' -- agents skills` prints `skills/agent-contract/SKILL.md:189` alone. Each definition G7 lists with a directory names it and cites rule 17 (read). `skills/verify/SKILL.md:284-285` still gives the same reason, wrapped across two lines so the search does not see it; the frame puts that file *Out*, and the hand-back names it.
- S5: the search of G8 over `agents` and `skills`, scripts and `.py` files excluded, gives 136 hits, and each was read. None tells an agent or the orchestrator to remove its scratch directory or a file in one. Rule 7 deletes a probe's leavings outside the scratch directory, and the other hits concern records, settles, rows, citations, the plugin's install directories or a guard removed for a red. `README.md` and `README.ko.md` say no agent removes its directory, and the *Rule changes* operation says the same. The `rm -rf` clause passes.
- S6: the cases on the crafter's, the proofer's and the framer's directories pass, and the sealer's `at-base/` stands in `test_the_gates_capture_file_carries_the_work_item_id`, which passes.
- S7 (read): T2 tells an agent that finds its directory standing to leave it and add `-2` to the leaf, and the rule 17 case holds that clause.
- S8 (read): T1 deletes everything a probe made outside the scratch directory, the file itself in a working tree among them. The `shape-no-probe-left` graders were not run.
- S9: `wc -c skills/agent-contract/SKILL.md` gives 12,779 B, 415 B more than 12,364 B, against the bound of 12,864 B.
- S10: the phase-boundary run below.
- S11: `git diff --stat 9c6907942...HEAD -- ':!seal/'` lists `README.md`, `README.ko.md`, the four definitions, `skills/agent-contract/SKILL.md`, `skills/code-review/SKILL.md`, `skills/implement/orchestration.md` and the scratch test module, and no other file.

**What a spawn preloads**, the core, the contract and the definition, by `wc -c` at `9c6907942` and at `18f699ddd` (executed): a crafter 33,097 B and 32,312 B, 785 B less; a framer 36,632 B and 36,925 B, 293 B more; a proofer 32,685 B and 32,864 B, 179 B more; a sealer 33,140 B and 33,159 B, 19 B more; a tracer 24,580 B and 24,995 B, 415 B more.

**The ten-word census (*Scope* item 13).** The probe follows #1320's D6: it reads every tracked `.md` and `.py` file outside `seal/` and `tests/` from the object store at the commit given, splits each into lowercase runs of `[a-z0-9_/.'-]+` with `.` and `'` stripped from each end, and counts, for each measured file, the words inside any ten-word run another corpus file also holds. It ran once, over four commits (executed). At `0c68b9933` and `20e140537` it gave #1320's readings in every cell, 934 of 11,209 and 754 of 10,733 words, so it is the same census. At `9c6907942` it gave G18's reading in every cell.

| File | `9c6907942` | `18f699ddd` |
|---|---|---|
| `agents/crafter.md` | 274 of 1,775 | 254 of 1,592 |
| `agents/framer.md` | 140 of 2,391 | 140 of 2,369 |
| `agents/proofer.md` | 151 of 1,733 | 141 of 1,695 |
| `agents/sealer.md` | 102 of 1,794 | 81 of 1,727 |
| `agents/tracer.md` | 26 of 442 | 26 of 442 |
| `skills/agent-contract/SKILL.md` | 90 of 2,048 | 90 of 2,133 |
| `skills/core/SKILL.md` | 133 of 1,595 | 133 of 1,595 |
| all | 916 of 11,778 | 865 of 11,553 |

The contract's 2,133 words are 7 fewer than G18's 2,140 with the texts in place, the two shorter headings above. Every commit after `18f699ddd` on this phase changes only this work item's directory, which the corpus excludes, so the reading holds at HEAD.

**The other statements of the reworded rules across the tree are a sample.** Method: `git grep` over every tracked file outside `seal/threads/`, on the leads this phase removed or rewrote, on "rule 7", "rule 17" and "rule 21" in both languages, on "scratch", on "A probe leaves nothing", "step 10", "the prompt's summary" and "never a merge", and the search of G8 (executed). Each hit was read. Each one either cites a rule whose number and fact stand, or is one of the following, which stand:

- `docs/running/the-agent-set.md:134-143` says the name lives in the definitions. The operation of `frame/design.md` *Rule changes* rewrites it at the settle.
- `skills/verify/SKILL.md:283-285` gives the shared-scratchpad reason for the capture file. `frame/design.md` *Scope* puts the file *Out*.
- `agents/tracer.md:66-67` says a probe "leaves nothing behind (rule 7)". `frame/design.md` *Scope* item 17 keeps it.
- The docstring of `tests/behaviour/test_a_probe_that_commits_says_so.py:9` paraphrases rule 7 as "a probe leaves nothing behind". Its pins still hold, and S11 keeps the file out of the diff.
- The docstring of `tests/behaviour/test_chain_hooks_hardening.py:1041` says where the chain ends "is the orchestrator's to read in the crafter's hand-back". The case reads `docs/running/the-run.md`, which still states it.

The search does not reach a restatement in other words, so the part it did not reach is any paraphrase of the removed sentences outside these files.

**The phase-boundary set**, one command through the repository's runner, run with this record, `gaps.md`, `changelog.md` and the Status cell written and not yet committed: `bin/test tests/text tests/behaviour "tests/skills/test_chain_check.py::test_the_proofer_and_the_review_skill_name_every_line_a_finding_needs" "tests/skills/test_chain_check.py::test_the_template_is_the_record_the_check_reads" -q`. It covers `tests/text` and `tests/behaviour`, which `CONTRIBUTING.md` names as the tree-wide files and which hold every module S10 names, and the two cases outside them that read a path the phase changed (`agents/proofer.md` and `skills/code-review/SKILL.md`). The other test files that name a changed path write it into a fixture they build (read). It gave 1,862 passed and 8 skipped, exit 0 (executed). Its two warnings name `docs/running/the-review-and-parity-arms.md:56` and a pending rule change of another work item, `seal/threads/1794289596-implement-orchestration-grew-back/`, which this phase does not touch. An earlier run of the same set, before the records stood, failed `tests/behaviour/test_docs_line_wrap.py` on the two headings and on two lines of the framer's and the sealer's rewrapped paragraphs, and `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview` for want of `gaps.md`; the headings are departure 1, the lines were rewrapped before `f0394fa83`, and `gaps.md` now stands. After the passing run, only this paragraph changed, from a placeholder to the result.
