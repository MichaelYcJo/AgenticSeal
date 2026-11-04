# Implementation Plan: 1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds

## Technical context

The work rewrites 23 comment and docstring lines and two fixture lines in 17 files. `frame/design.md` D1 lists each line at `f93d70ea4` with its disposition. No code path changes, and no case is added or removed.

The build waits for #1255 and #1256 to land on `release/v0.32.0` (#1355 *Order*). Their diffs change the text of none of the 25 lines, and each moves one of them (executed: the measure run on each branch, and each branch's three-dot diff against `origin/release/v0.32.0`):

- #1255 moves `tests/test_censuses.py:934`, D1 row 22, further down the file. Its merge base, `479a79d15`, still holds `evals/scripts/noninferiority.py`'s cited line, which #1254 rewrote at `f93d70ea4`. #1255's diff touches that file only in its `__main__` block, so the merge leaves the line removed.
- #1256 moves `tests/behaviour/test_a_cited_section_stands_in_its_file.py:445`, D1 row 4, to `:590`. It edits `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` at line 488 and `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` at line 634, neither of them D1 rows 6 or 15.

So the phase runs the measure again on the release branch after both land, and builds against the lines it prints. A line the measure prints that D1 does not list is read by D1's four dispositions and recorded in the phase record as a departure.

Two existing structures constrain the rewrites. `tests/censuses.py#old_names` refuses `seal/specs` outside a `HISTORY_PATH` token, so a rewrite that drops the commit names the issue and not the old path. `tests/text/test_a_cited_commit_outlives_the_squash.py` reads every token in the tracked files and refuses an unreached commit, so a fixture built when its case runs takes the fixture out of that case's reading.

**The failure scenario of the chosen approach, six months on.** A later work item writes a new provenance comment in a test as a `<commit>:<path>`, its commit on `main`. No check refuses it, because D2 adds none. The proofer reading that diff against `skills/core/SKILL.md` *The rule a mechanism is kept against* is the only party that sees it, and #1355's measure finds it when someone runs it again. What it costs in the meantime is the bytes every reader of that file pays. It sends nobody to a commit that cannot be opened, because the squash case still refuses that.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Rewrite each line by D1's four dispositions, build the two fixtures when their cases run, add no case and keep the squash case as it is | A rewrite that cites an issue number points at a page that does not hold the grounds the sentence sends the reader for, and the reader finds nothing there | **chosen.** The phase confirms each cited page with `gh` (`frame/questions.md` Q1), and the proofer reads each rewrite. The design's D2 gives the grounds for adding no case |
| A2. Add an arm to `tests/text/test_a_cited_commit_outlives_the_squash.py` that refuses any `COMMIT_PATH` token in a tracked file outside `seal/` | A writer refused by the arm moves the provenance to a bare commit or to prose. The tree outside `seal/` already holds 51 distinct bare tokens that resolve as commits, and the case reads none. So the arm moves the text and not its cost. #1355's *Done when* also allows a line that carries why it stays, and the arm would need an exemption mark to let it. On the day it lands, the arm has caught nothing, because this work removes the 25 by hand. And none of the 25 misdirected a reader: `origin/main` reaches every cited commit (executed) | rejected. By `skills/core/SKILL.md` *The rule a mechanism is kept against*, the arm has no record of a catch to outweigh its cost. Whether a citation holds grounds a reader acts on is a judgment of meaning, which a spelling check would re-encode as a grammar rule (*The first value*) |
| A3. Replace the squash case's structure: narrow its corpus to `seal/`, since shipped text will hold no token after this work | A token that returns to a test or a workflow with a commit no `main` or release ref reaches goes unrefused, and its reader is sent to a commit no clone holds after the squash | rejected. The premise that keeps the structure was checked: the form can be written in any tracked file, and an unreached commit misdirects wherever it stands. `read_here` admits every tracked file except three kinds of record (read: `tests/text/test_a_cited_commit_outlives_the_squash.py`, `read_here`) |
| A4. Remove the passes the censuses give the form, `tests/censuses.py#HISTORY_PATH` in `old_names` and `#COMMIT_PATH` in `vacated_paths`, since shipped text will hold no token | `seal/follow-up.md:42` holds a token whose path is under `seal/specs/`, an old name (`OLD_NAME`, `tests/censuses.py:997`, read). `old_names` reads `seal/follow-up.md`, because `OLD_NAME_RECORDS` passes only `seal/threads/` whole (read). So `old_names` would refuse a citation that `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* states as the form a settled record is cited in | rejected. The premise that keeps the passes was checked (executed: `git grep -nP` over `seal/`; read: the census lines). #1255 also edits `tests/censuses.py` |
| A5. Keep the two fixtures' literal tokens, each with a comment at its line saying why it stays, as #1355's *Done when* allows | `ELSEWHERE` is a triple-quoted string, so a comment at its line becomes fixture text and changes what the S7 case reads. The squash case also goes on reading each fixture as a real citation, so a fixture's commit has to stay reachable for an unrelated case to pass | rejected. The squash case builds its own tokens when its cases run, "so this file holds no `<commit>:<path>` of its own" (read), and the two fixtures follow it |
| A6. Cite the release tag that holds each record, `<tag>:<path>`, in place of the commit | A tag is never squashed away, but the citation keeps its hundred-odd characters, names a path the tree no longer holds, and opens only through `git show`. It is the same cost, with a ref that does not move | rejected. *What changes* asks for the grounds in one sentence or `#N` |
| A7. State the rule in policy: change `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*'s "A document that still cites a record of it" to say that text outside `seal/` states what its reader needs, or cites `#N` | The layout documents are opened where a party places or writes a record (`docs/README.md` *docs/layout/*, read). A writer of a test comment does not open them, so the sentence reaches nobody who writes the form. The rule it would state already stands in `skills/core/SKILL.md`, which every party receives, so the same fact would stand twice | rejected. `frame/design.md` `## Rule changes` holds the no-change block |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2 and 3, built on `release/v0.32.0` after #1255 and #1256 have landed | S1 to S6 of `frame/design.md` *User scenarios & acceptance*, each with its command and output in the phase record. The narrow runs of the touched modules, `tests/test_censuses.py` and `tests/text/test_a_cited_commit_outlives_the_squash.py` pass. The full suite is `unverified`, and the orchestrator's broad gate answers it | 98920cf80 |

## Operational impact

None. The work changes comments, docstrings and two fixtures' spelling. It adds no dependency or environment variable, and it leaves `.claude-plugin/plugin.json`'s version alone, because this work item is not the release's first.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-04 | The frame is folded to phase 1 as built: D1 rows 1, 2, 4, 12, 19, 21, 22 and 24, the fixture rule, the `## Removes` rows on `test.yml` and the two docstrings, and the plan's line on #1255 state what phase 1 did; Q1 records the work's answer; the line numbers #1255's move left stale give way to the place they name | The crafter's hand-back named each statement HEAD contradicts, read whole against HEAD by the orchestrator: no issue page holds what rows 1, 2, 12, 19 and 24 were to cite, row 21's path moved, and row 4's token is built at load. A line number kept beside the tree drifts at the next edit with nothing to catch it | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*; `skills/core/SKILL.md` *The rule a mechanism is kept against* |
| 2026-11-04 | D1 rows 1 and 2 and the `## Removes` `test.yml` row are folded to round 1's fix pass, which moved the shard arithmetic into the comment | The fix pass named each statement HEAD contradicts (round-1#1, `fixed a43c13166`), read against HEAD by the orchestrator | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
