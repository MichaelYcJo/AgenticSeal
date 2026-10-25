# Review round 3: 1792926874-the-records-carry-no-comment-and-the-readers-drop-it

target: 2bf45ae1, fixes 8e644ca2..2bf45ae1

## Findings

none

## Confirmations

confirms: round-2#1
The fix holds. Round 2 found that the `fence_spans` docstring named `rule_changes.py#parse` as a reader that walks fences only through `liveness`, and `chain_check.py` as one that walks them only through `readable`. Both claims are gone from `skills/verify/scripts/unverified_check.py:238-245` at `2bf45ae1`. The docstring now names no caller outside its own module (read).

Each sentence the fix wrote was checked against the code. The first says the walk keeps no comment state and no code-span state. The loop at `unverified_check.py:255-266` holds only `opener` and `first`, so that holds (read). The second says that in this module `closed_fence_lines` and `blank_fences` walk it, and `readable` through `blank_fences`. A search for the three names called in this module finds `fence_spans` at `:274` and `:291` and `blank_fences` at `:612`, inside `readable`, and no other caller in the file (executed). The third says callers in other scripts are found with `git grep`. The same search over the tree finds `chain_check.py:1162` calling `fence_spans`, `rule_changes.py:115` calling `blank_fences`, and the `readable` callers in `chain_check.py`, `seal_stamp.py`, `noninferiority.py` and `replay_targets.py` (executed). The docstring names the chain through `blank_fences` and `readable`, so an agent who searches those three names finds every caller round 2 said the old text missed. The fourth says `liveness` keeps a comment or code-span state and asks `fence_opener` and `fence_closes` directly. `:346` opens a fence only where `not comment and span is None`, so that holds. `liveness` is the only walk in the module that does so. The other direct call, `:482` in `_paragraph_ends_at`, judges one line and keeps no state (executed: the `grep` for `fence_opener|fence_closes` in the file).

Round 1's defect does not come back. That finding was a claim that every reader of a record lacks a code-span state. The new text describes only what `fence_spans` itself keeps, and makes no claim about the readers of a record (read).

The `live_lines` sentence at `:575-577` now says that `blank_fences` and `readable` keep no comment state because a record carries none, and that they serve the readers of a record. It names no reader, so it no longer leaves out `parse`'s line 115. It does not say they serve only records. That matters because `chain_check.py:396` also reads `docs/the-review-record.md`'s grammar tables through `readable`, and `spec.md` *Scope* item 2 records that the file holds no `<!--`, so no comment is misread there (read).

The fix pass claimed that it derived each sentence from the call graph and did not paste round 2's text. The diff matches: neither docstring holds round 2's suggested wording (read: `git diff 8e644ca2..2bf45ae1`). The fix commit `09326125` changes `skills/verify/scripts/unverified_check.py`, which round 2's `location:` names.

confirms: none
The fix pass's two lines in `rounds/round-2.md` are the only change `2bf45ae1` makes to that record: the `verdict:` line, now `fixed 09326125`, and the `answer:` line (executed: `git diff 8e644ca2..2bf45ae1`). The answer's caller list matches a rerun of its own command at `0c532fe8`, the commit round 2 reviewed: `fence_spans` at `unverified_check.py:272` and `:289`, `readable` at `:610`, and `check_text`'s call at `:886` (executed: `git grep` at `0c532fe8`). At `2bf45ae1` each of those four in-module coordinates sits two lines lower, at `:274`, `:291`, `:612` and `:888`, because `09326125` added two docstring lines above them. The record speaks for round 2's target, so this is not a finding. The other scripts' coordinates are unchanged at the head (executed).

confirms: none
The fix pass's sweep was read against the diff. Its five standing items each hold at `2bf45ae1`. `unverified_check.py:90-111` lists the functions of this module that ask the delimiter rule, and the code holds that. This work item did not change those lines; its diff to that region touches only the comment-delimiter comment below them (executed: `git diff 4d5a6917..2bf45ae1` over the file). The `chain_check.py#unclosed` docstring at `chain_check.py:1152-1154` says its walk is `fence_spans` on the raw lines, as `readable` does, and `:1162` does that. `rule_changes.py:13-20` names `blank_fences` among the functions it reads through, and `:115` calls it. `tests/test_docs_line_wrap.py:281` names where the rule lives, not who calls it. `tests/test_unverified_rows_close.py:298` describes the walks its own case compares (read, all four). The sweep's `git grep` also finds code lines in `tests/test_unverified_check.py:401-429` and `:851` and in `tests/test_the_hooks_hide_what_a_renderer_hides.py:641`. The answer does not list them. Each is a call or a test class name, and none is a sentence about who walks `fence_spans`. The docstrings around `:851` and `:641` describe what their own case compares, and both hold (read).

Carried, not re-established: the orchestrator's `uvx ruff check` and `uvx ruff format --check` on `unverified_check.py`, and `bin/test -n auto -q` over `tests/test_unverified_check.py`, `tests/test_chain_check.py`, `tests/test_rule_changes.py` and `tests/test_unverified_rows_close.py` at `2bf45ae1`, 669 passed (executed by the orchestrator, not re-run here). The diff changes two docstrings and two record lines and no code, and no test reads either docstring (executed: `git grep` under `tests/` for the docstrings' phrases and for `__doc__` readers of the module). Also carried: that `closed_fence_lines` has no caller outside `tests/` at the base `4d5a6917`. At the head the sweep agrees (executed). The orchestrator names it in the pull request, and it predates this work item. Carried from rounds 1 and 2: the confirmations of phases 1 and 2, S1, S2, S11, and the reading of every record. The fix diff touches none of the code they rest on.

This round leaves nothing open. What comes due is the orchestrator's broad run, then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `2bf45ae1`, which `overview.md` labels unverified, honestly | the whole tree | the orchestrator, through `broad-gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git diff 8e644ca2..2bf45ae1` | two files: the `fence_spans` docstring and the `live_lines` sentence in `unverified_check.py`, and the `verdict:` and `answer:` lines of `rounds/round-2.md` |
| `git grep -n -E '(fence_spans\|blank_fences\|readable)\(' -- . ':(exclude)tests' ':(exclude)seal/specs'` | `fence_spans` at `unverified_check.py:274`, `:291` and `chain_check.py:1162`; `blank_fences` at `unverified_check.py:612` and `rule_changes.py:115`; `readable` at `unverified_check.py:888`, `chain_check.py:396, 1176, 1239, 1413, 1448, 1830, 1855`, `seal_stamp.py:1209, 1344`, `noninferiority.py:306`, `replay_targets.py:243, 275` |
| `git grep -n -E '(fence_spans\|blank_fences\|readable)\(' 0c532fe8 -- skills/verify/scripts/unverified_check.py` | `:272`, `:289`, `:610`, `:886`, the answer's coordinates |
| `git grep -n -E 'fence_spans\|blank_fences\|closed_fence_lines' -- . ':(exclude)seal/specs' ':(exclude)changelog' ':(exclude).test_durations'` | the five standing items of the sweep, the docstrings and calls in `unverified_check.py`, and code lines in `tests/test_unverified_check.py`, `tests/test_unverified_rows_close.py` and `tests/test_the_hooks_hide_what_a_renderer_hides.py` |
| `grep -n -E 'fence_opener\|fence_closes' skills/verify/scripts/unverified_check.py` | direct calls at `:257`, `:260` (`fence_spans`), `:342`, `:346` (`liveness`) and `:482` (`_paragraph_ends_at`) |
| `git grep` under `tests/` for `may not touch`, `no list of them` and `found with`, and for `__doc__` readers naming the module | nothing pins either docstring |
