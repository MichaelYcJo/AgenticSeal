# Implementation Plan: an import inside a fence is not charged (#1185)

## Technical context

`skills/verify/scripts/payload_meter.py#imports_of` (`:360-392`) runs `IMPORT` (`:117`) over the decoded text of each file, at every hop. `pair_rows` (`:415-447`) calls it for the two `CLAUDE.md` files. `heading_starts` (`:283-319`) is the one reader in the meter that already walks a fence state, through `_fence_rule()` (`:160-181`). That loader brings in `unverified_check.py`, which re-exports `hooks/lib/blocks.py#fence_opener`, `fence_closes` and `gfm_lines` (`unverified_check.py:118-127`).

`unverified_check.py#liveness` (`:326-407`) holds the one scan of fences, comments and code spans. Its loop moves `pos` through each line and already knows every live piece. It keeps only the flag of whether the line begins live. `_partner_ahead` (`:512-530`) and `_paragraph_ends_at` (`:453`) decide whether a backtick run with no partner on its own line opens a span across lines. `live_lines` calls the scan twice, once with spans across lines and once without, and ANDs the two flags. The meter needs one reading, so it asks the scan with `spans_cross_lines=True`, the CommonMark reading wherever `_paragraph_ends_at` is right.

`session_composition` (`:450-473`) loads `_core()` before `pair_rows`. So the copy-alone case that runs with no flag still names `hooks/lib/core.py` first, whatever the machine's `~/.claude/CLAUDE.md` holds. The `--sections` case still reaches `_fence_rule()` at the head of `measure`.

**The failure scenario of the chosen approach.** In six months a Claude Code release changes what its reader skips, for example by scanning a comment again or by skipping indented code under the docs. The meter keeps reading the documented shapes. A `CLAUDE.md` with that shape is then charged wrongly, and nothing in the tree says so, because the meter cannot run Claude Code's lexer. The docstring names the source and the version read (G2, G3). A person who reads the docs page again finds the drift there. The second risk is the refactor of `liveness`. A change in its flags on some shape would move every reader of `liveness` and `live_lines`: `unverified_check.py` itself, `skills/settle/scripts/rule_changes.py` and `skills/settle/scripts/fold_check.py` (executed: `git grep -n 'live_lines(\|liveness('` outside `seal/threads/`). Their existing cases and those of `tests/skills/test_unverified_check.py` are what hold it (S7).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Extend the one scan in `unverified_check.py` to return the live pieces of each line, and have `imports_of` match only there (chosen) | A refactor of `liveness` that shifts one flag moves every reader of `live_lines`. Their cases catch a shift on the shapes they hold, and a shape none of them holds would pass unseen | Chosen. The scan already decides fences, comments and spans by position, and a second scan would be a second source of the same fact (`skills/core/SKILL.md` *The rule a mechanism is kept against*). |
| Keep the structure: `imports_of` walks lines with `fence_opener` and `fence_closes`, as `heading_starts` does, and masks spans and comments with a pattern of its own | The meter then holds a second span rule and a second comment rule beside `liveness`. The two drift the way the readers before #584 drifted. The comment at `unverified_check.py:98-117` lists readers that keep their own rule on purpose, and the meter has no purpose to differ | Rejected. The premise that would keep it is that `liveness` cannot give positions, and it was checked false: its loop holds `pos` at every live piece (G7). |
| Fences alone, as the ticket's Done-when names them | `` `cat @a.md` `` and `<!-- @a.md -->` stay charged. The docs name spans in the same sentence as fences (G2), and the probe charged both (G6). A later issue would reopen the same function for the same paragraph of the docs | Rejected. Contract rule 12 asks for the class. The class here is listed by taking the docs' import section apart sentence by sentence, and that list is closed. |
| Also replace `tests/behaviour/test_the_old_block_leaves_through_update.py#IMPORT` with a call to `imports_of` | That module tests `/agentic:update`'s removal of the old block, the area #1184 works in this release. Its pattern reads more as an import than the meter does, which is the safe direction for "`CLAUDE.md` imports nothing" | Rejected for this work item. The copy is a second spelling with a different purpose, a test that must fail where anything looks like an import. A change to it collides with a parallel branch for no reading that is wrong today. |
| Follow Claude Code 2.1.318's reader everywhere it goes past the docs: indented code, other HTML blocks, `#` fragments, the first-character filter, non-text extensions and frontmatter | Each shape is read off one binary's minified source, and the next release can change it without a line in the docs. The meter would claim an exactness it cannot keep | Rejected as the default, and named in the docstring as what the meter does not model (`questions.md` Q1). |
| Run Claude Code itself to list what a `CLAUDE.md` imports | The meter runs offline in CI and on any machine. A run of the harness needs credentials and costs a session each time | Rejected. Nothing offline answers it but a copy of the rule. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* 1, 2, 3 and 4, test-first. | S1 to S6 as new cases in `tests/skills/test_payload_meter.py`, each seen red at 0830987a, with how in the phase record. S7 through the existing cases of `tests/skills/test_unverified_check.py` and `tests/skills/test_payload_meter.py`, with no assertion edited. S8 through the copy-alone case with its purpose string moved, seen red against the old sentence. The narrow run of the modules the phase touched and the test modules of every caller of `liveness` and `live_lines` named in *Technical context*. The suite stays `unverified` until the orchestrator's broad run. | |

## Operational impact

None. No new dependency, environment variable or exit code. A run with no `CLAUDE.md` that holds an `@` behaves as it does today. The JSON of `seal payload` keeps its shape, and a `--baseline` file from 0.32.1 still reads.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
