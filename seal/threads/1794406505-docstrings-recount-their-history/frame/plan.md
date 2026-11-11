# Implementation Plan: docstrings recount their history (#1485)

## Technical context

The tree as read at `38123f839`.

The work edits the docstrings and comments of the files design *Scope* items 2 to 7 name, a test assertion only where it pins a sentence the work rewrites or removes, and a sentence elsewhere only where this work's rewrite made it false (design *Scope* item 10). No code, string constant or printed message of those files changes, and design S1 proves it per phase by comparing each edited script's syntax tree, docstrings taken out, across the phase's range. The design's counting command lists each phase's starting lines (`--hits`), and the crafter reads each hit with the code it stands over before it judges the sentence. A sentence outside the hit listing is judged by the same rule where the crafter meets it. A second listing helps find those: the same command with the pattern `\bround \d+\b|\bfinding \d+\b|frame/design\.md|questions\.md|\bwork item \d{10}\b|\bno longer\b` gives 196 lines at the base, 114 of them outside the main listing (executed). It is a sample, noisy by design: `chain_check.py` names `frame/design.md` because it reads that file, and "no longer" can describe the present.

Constraints met in the build:

- `broad_gate.py`'s module docstring keeps one paragraph naming both `origin/` and `upstream`, `seal_stamp.py` keeps `` `seal-mark.txt` ``, and `seal_stamp.py#admitted`'s docstring keeps every line within 79 columns (design G9). `session_cost.py#token_thirds`' docstring keeps the three present facts its case in design G9 still asserts, and `settle.py#survey`'s and `#apply`'s docstrings keep the phrases their case in G9 reads.
- A citation the build rewrites resolves, by design G10's module.
- The first line of the module docstrings of `issue_claims_check.py`, `release_report.py` and `rules.py`, and the first paragraph of `payload_meter.py`'s, stay as they are (design G8).
- `lib/*.py`, `hooks/*.py` and the scripts `ruff.toml` lists under `[per-file-target-version]` are linted at Python 3.9. Prose cannot reach that, and S6 runs the lint over each phase's files.

The failure scenario of the chosen approach, six months on: a maintainer meets a branch whose reason the build cut along with its history. A sentence such as "the fallback rather than the rule (#377)" carried the only statement that the branch was deliberate, and the rewrite kept the code and dropped the sentence. The maintainer removes the branch as dead and the defect it held returns. Design S4 is the guard: the review reads each removed sentence against the code it stood over, and *Scope* item 1 says a reason is rewritten and never dropped. `git blame` still leads from the line to the issue.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. All 50 files and `bin/test`, in six phases, the five largest first | The diff is large prose, design G5's hit lines and the sentences around them, and the review reads it whole; a removed reason can hide in volume. Each phase's code command and the review's S4 read bound that | chosen |
| A2. The five largest files only, as a literal reading of "starting with", and the rest to a new issue | The hit lines of design *Scope* items 5 to 7 stay, the count cannot fall below any value that says the issue is done, and the new issue repeats this frame | rejected: the issue's title, *Done when* and the core's rule cover every script |
| A3. Add a census to `tests/censuses.py` that refuses a `#N`, a date or "used to" in a script's docstring or comment, so the history cannot grow back | It refuses `Closes #1` in `issue_claims_check.py`, a commit title's `(#N)` and every present "measured". The core says a reading guessed from words is reported and never used to block (design G3). It is a mechanism with no catch record, which the core weighs against its cost | rejected |
| A4. Move each file's history into a history section, or into a document under `docs/checks/` | A second copy of what git, the release notes and the issues hold, kept beside the tree to stay in step with it, which the core forbids (design G2) | rejected |
| A5. Replace the structure: cut each docstring to one line and move the reasons into `docs/checks/` documents, so the scripts carry no prose to go stale | A reason away from its line drifts from the code it explains, and a maintainer meets the branch without it. The core names the docstring as the home of text no agent acts on (design G2, the premise read at `skills/core/SKILL.md`) | rejected: the premise that keeps the structure is checked |
| A6. Keep the docstrings as they are | The issue's 865 lines stay, and the core's rule that history goes to git stands unmet in the files that rest on it | rejected |
| A7. Keep every issue number as the coordinate of the reason beside it, and remove only the narrative | Most of design G5's hit lines carry a `#N`, so the count barely falls. The issue accepts losing the number because `git blame` leads there (design G1). The keep class K4 holds the one case where the number is the source a value is held to, an owner's decision | rejected, with K4 kept |
| A8. Rewrite the docstrings of `tests/` and `evals/` too | #1489 rewrites the docstrings of the test files it moves, so both items edit the same lines; the issue names the scripts | rejected; design *Scope* Out |
| A9. One phase per file for the five largest | Five spawns where three read the same amount, and the crafter of `chain_check.py` alone meets 17 lines | rejected for cost |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* item 1 for item 2, and item 8 at the base | S1, S5 (G10's module and the case on `token_thirds`' docstring) and S6 executed; S3 and S4 read at review; the rest of the suite `unverified`, answered by the orchestrator's broad gate | `386e46c8b` |
| 2 | Item 1 for item 3 | S1, S5 (G10's module and the case on `broad_gate.py`'s docstring) and S6 executed; S3 and S4 read at review; the rest of the suite `unverified`, answered by the orchestrator's broad gate | `ead171191` |
| 3 | Item 1 for item 4 | S1, S5 (G10's module and the case on `survey`'s and `apply`'s docstrings) and S6 executed; S3 and S4 read at review; the rest of the suite `unverified`, answered by the orchestrator's broad gate | `4ac403501` |
| 4 | Item 1 for item 5 | S1, S5 (G10's module and the two cases on `seal_stamp.py`) and S6 executed; S3 and S4 read at review; the rest of the suite `unverified`, answered by the orchestrator's broad gate | `e455a72e8` |
| 5 | Item 1 for item 6 | S1, S5 (G10's module) and S6 executed; S3 and S4 read at review; the rest of the suite `unverified`, answered by the orchestrator's broad gate | `a01158430` |
| 6 | Item 1 for item 7, item 8 at its commit, item 9, and item 10 | S1, S2, S5 (G10's module), S6 and S7's search executed; S3, S4 and each line S7 lists read at review; the rest of the suite `unverified`, answered by the orchestrator's broad gate | `a296ae8e4` |

Phases 1 to 5 touch no file #1489 has edited (design G16) and can be built from the base in order. Phase 6 starts after #1489 has merged into `release/v0.37.4` and this branch has taken `release/v0.37.4` by a merge, never a rebase, so it edits the docstrings as #1489 left them. Where #1489 has not merged when phase 5 closes, the orchestrator judges whether to wait or build phase 6 from the branch as it stands. That judgment and its grounds go to *Judgments of the run*.

Each phase runs the code command from the commit it started at, or from the commit after a merge it took, to its last commit, over design S1's pathspecs. A docstring pin of design G9 stands in the file #1489 left it in, found by the case's name with `git grep`. A case that fails because it pins a sentence the phase rewrote changes with the sentence in the same commit, and the phase record names each assertion it changed. The test file stays outside S1's pathspecs, and the review reads the change.

## Overlap with the release

The spawn named one open item, #1489, read on its branch at `d0ed5f84d` with its frame at that commit, then in build phase 6 of 8. It merged into `release/v0.37.4` as `810ef9018` (PR #1531), and this branch took it by the merge `79a5f94c7`, from which phase 6 started (executed: `gh pr view 1531`, `git log -1 --format=%P 79a5f94c7`). #1482, #1483 and #1484, which the issue builds after, are merged into the base (read: `git log 38123f839`).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1489 | The docstrings and comments of `lib/blocks.py`, `lib/routing.py`, `lib/tables.py` and `skills/verify/scripts/test_layout.py`, which its branch edits and this work's phase 6 rewrites (design G16), and `tests/github/test_label_merged_on_release_branch.py`, whose class docstring its branch edits at `871c8e346` and whose comment phase 6 corrects (design *Scope* item 10; executed: `git diff --stat 38123f839...test/1489-test-files-declare-no-target`). Its later phases may rewrite a citation of a moved test case in any script's docstring (its design *Scope* item 9), which can meet phases 1 to 5 at a line. It also moves or rules the cases of design G9 that this work's S5 runs | #1489 | It was in build when this frame was drawn, and the issue says #1485 builds last; #1489's frame states the same order. Merging second, this work rewrites those files as #1489 left them in one phase after the merge, and a later citation edit meets a line this work changed at most once, at the merge of `release/v0.37.4` into this branch |

## Operational impact

None. The work adds no migration, environment variable or dependency, breaks no compatibility, and moves no version.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-11 | The frame statements phase 1 named went to the framer as a fold before phase 2 | Design S1 and *Scope* item 1 say no code changes, and phase 1 changed a docstring-pinning case design G9 did not list; each later phase runs S1, so the frame settles it before phase 2 | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-12 | The frame statements phases 3 to 5 named went to the framer as one fold after phase 5, and phase 6 waits for #1489 to merge into `release/v0.37.4` | None of the statements bore on the phase after it, so one fold costs one spawn; #1489 is in review and edits phase 6's files, and building phase 6 before its merge would rewrite docstrings a merge then conflicts on | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*; `frame/plan.md` *Phases*, the paragraph on phase 6 and #1489 |
| 2026-11-12 | The frame statements phase 6 named went to the framer as one fold before the first round | A round reads the build against design *Scope* items 1 and 10 and *Removes*, and phase 6 departed from K3 with recorded grounds and found two coordinates the merge of #1489 shifted | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-12 | The title takes `docs:`, as the issue's title does: the diff changes docstrings and comments and no line of code | The prefix names the kind of change that dominates the diff | `skills/commit-pr-convention/SKILL.md` |
