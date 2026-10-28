# Review round 1: 1793169129-the-creation-row-still-says-retry-with-worktree-ok

target: 843c04dc against 977b6613

## Findings

This round found no defect. Stage 1 read the diff of `hooks/worktree-guard.py` and `tests/hooks/test_worktree_guard.py` against `frame/design.md` *In*, *The class*, *User scenarios & acceptance*, *Data & interfaces* and `## Removes`, and found each clause built. Stage 2 walked the axes below and found nothing to fix. Each check is an entry under `## Confirmations`, labelled executed or read.

The axes walked: inputs (no parameter of `guard_worktree_creation` changed); the press read and its scope (the session's own root, after rows 1 to 4); exclusions and boundaries (attended, under the press, the press's own clone, an unbalanced quote, the token given); deliberate non-exclusions (row 2 under the press, P1's default (a)); error paths (an unreadable press); the failure direction; the transcript reads per creation; both languages; the class of token sites in the creation direction; the comments that stated the old fact; the platform; test quality against each new case's group. Concurrency and atomicity: the change adds one read of the transcript and no write, and holds no state across a call, so no second actor can interleave with anything it decides. Security: the change crosses no new process boundary. `repo_paths` runs the same `git rev-parse` that `git_at` already runs for the same `cwd`, and no new input is trusted.

## Confirmations

confirms: none
Under the press, row 5's deny names no `[worktree-ok]` and asks for no confirmation, in both languages, on three attempts each, for the parsed command and for the one with an unbalanced quote. `hooks/worktree-guard.py:1947-1978` reads the press after rows 1 to 4, opens with `plain_origin`, and ends with `switch_lines(git)`, a blank line, `press_sentence()` and `reissue_sentence()` where pressed (read). The composed English text is `frame/design.md` *In*'s quoted reason word for word: the situation string ends with a blank line, and `press_sentence` ends with one before `reissue_sentence` (read, `hooks/worktree-guard.py:1490-1514`). The crafter claimed S1 and S2 red at `977b6613`. Executed in a `git clone --no-local` of the branch at `843c04dc`, with `hooks/worktree-guard.py` restored to `977b6613`: both parametrisations of `test_under_the_press_the_single_stream_row_names_no_token` failed. The reason ended with the confirmation sentence naming `[worktree-ok]`, and the unbalanced command's first line carried the quote note naming it too. With the file restored to `843c04dc`, the module passed.

confirms: none
Attended, row 5 is byte-identical to the base. The crafter claimed attended text unchanged. Executed: `steer_to_switch("git")` and `steer_to_switch("git -C /x")` printed in English and Korean from the hook at `977b6613` and at `843c04dc`. `cmp` found the two outputs identical in each language. `switch_lines` (`hooks/worktree-guard.py:1388-1401`) holds the three command lines, and `steer_to_switch` (`:1404-1416`) adds `"\n\n"` and the confirmation sentence in its own `tr`. Its three callers, row 2 (`:1836`), row 3's attended fallback (`:1910`) and row 5 attended (`:1975`), therefore print what they printed at the base. `test_attended_the_single_stream_row_reads_as_at_the_base` (`tests/hooks/test_worktree_guard.py:4481-4496`) pins row 5's attended text in another clone in both languages, with the quote note on the unbalanced command only. It passed at `977b6613` (executed), as the frame says it should. That it goes red with the press forced on rests on the crafter's `seal mutate` run, which this round read and did not re-run (`## Not judged`).

confirms: none
S5's pin is `[1, 2, 2, 2]` (`tests/hooks/test_worktree_guard.py:4431`). The crafter claimed `[1, 2, 1, 2]` at the base. Executed: against `hooks/worktree-guard.py` at `977b6613`, `test_the_transcript_is_read_at_most_twice_per_creation` failed with `[1, 2, 1, 2]`. The bound of two reads per creation holds. Row 0 reads the transcript once for the creation's clone (`:1712`). A creation reaches at most one of rows 3, 4 and 5, because `choose` and `respond` end the hook. Each of those rows reads the press once for the session's own root (read).

confirms: none
The class in `frame/design.md` *The class* matches the tree. Executed: `grep -n "worktree-ok" hooks/worktree-guard.py` at `843c04dc` finds string sites at `:1411-1413` (the confirmation sentence, now only in `steer_to_switch`), `:1829-1833` (row 2's `ask`, P1), `:2053-2058` (the quote note, which row 5 drops under the press) and `:3350-3359` (the switch direction's options). Every other hit is in a docstring or a comment. `choose` returns before it reads the switch options under the press (`hooks/worktree-guard.py:1579-1580`, read). No third creation-direction hint exists.

confirms: none
The failure direction is neither, as the frame says. Row 5 is `deny` in every state before and after. `automation_pressed` (`hooks/worktree-guard.py:2640-2658`) returns False on a missing session or root and on every exception. An unreadable press therefore gives the attended deny, never a pass and never a hook that raises (read). Attended, the press read adds one `git rev-parse` and one transcript scan to row 5, which the frame's *What the transcript costs* counts.

confirms: none
Every comment and docstring that `frame/design.md` *In* lists was rewritten in place: the module docstring's creation ladder and its *Under the press* paragraph, the comment above `elsewhere`, the new comment that heads row 5, the comment above `plain_origin`, and the two test docstrings (read, the diff `977b6613..843c04dc`). Executed: `git grep` outside `seal/` and the changelogs for `retry with [worktree-ok]`, `rows 3 and 4 name no token` and `single-stream deny's way past` found no sentence in code or tests that still says only rows 3 and 4 drop the token. `docs/worktree-guard-spec.md` still states the old fact at *B. Worktree creation* and *Choice sites*. The frame's two `change` items quote both `from:` texts as the spec reads them (read, `docs/worktree-guard-spec.md:161` and `:418-420`). `skills/implement/SKILL.md` gives the policy root to the settle, not to the pull request. The crafter's account of leaving the document alone therefore holds.

confirms: none
Row 2 is unchanged, on P1's default (a). The diff touches no line of row 2's `ask`, and `test_the_token_still_reaches_its_own_row` (`tests/hooks/test_worktree_guard.py:4309`) passed in the module run (executed). Rows 3 and 4 are unchanged except for the comment above `elsewhere`.

confirms: none
The new cases cover what their group did not. `bin/seal layout --pairs` names no pair in `tests/hooks/test_worktree_guard.py` (executed). Before this work, no case in the file pinned row 5's whole text in another clone. `test_refuses_a_creation_with_no_repository_or_no_consent` checks a prefix, and the check at `:2687` checks only that `unbalanced quote` is present (read). S1 is the only case on row 5 under the press, and S3 is the only one on its attended text in both languages.

confirms: none
The crafter claimed the module green at 354 passed and 3 skipped. Executed in the clone: `bin/test tests/hooks/test_worktree_guard.py -q` gave 354 passed and 3 skipped. The neighbouring modules that read the guard also passed: `tests/e2e/creation/test_creation_flow.py` and `tests/hooks/test_worktree_consent.py` (63 passed), and `tests/behaviour/test_the_frozen_reading_never_grows.py` and `tests/text/test_a_rider_reaches_its_file.py` (11 passed). Ruff `check` and `format --check` passed over the two changed files only. The crafter's hand-back labels the full suite `unverified`, names the orchestrator through `seal gate`, and names `.test_durations` as part of that reading. The label is honest: the durations case skips unless the whole suite is collected (`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, read).

confirms: none
`gaps.md` *Where spec and implementation diverged* records one row, and it is no divergence. `frame/design.md` *Data & interfaces* says the reason ends with the switch lines, then `"\n\n"`, then the two press sentences. That is what `hooks/worktree-guard.py:1973` does (read). The row says the code matches the frame's exact reason, and it does. *Fed back into the spec* reads `none`, which matches the diff.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The five `seal mutate` mutants the crafter reports red, the S3 mutant with row 5's press forced on among them; this round re-ran none of them. By reading, the `origin` mutant under the press is caught by S1's unbalanced command, which expects no quote note | `trail/phases/phase-1.md`, *Mutation over each unit added* | the sealer, which re-runs a sample of the crafter's claims |
| The full suite, the repository-wide lint and the typecheck, including whether `.test_durations` still prices the suite with three unpriced node ids. This round declined them under contract rule 2 | `gaps.md` *Not verified* | the orchestrator, through `seal gate` |
| Whether row 5 is unreachable on Windows; it rests on `docs/worktree-guard-spec.md` *Known limits*, and this round ran on macOS only | `hooks/worktree-guard.py:1947-1978` | the Windows leg of the pull request's CI |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_worktree_guard.py -q`, in a `git clone --no-local` of the branch at `843c04dc` | 354 passed, 3 skipped |
| `git restore --source=977b6613 hooks/worktree-guard.py`, then `bin/test tests/hooks/test_worktree_guard.py -q -p no:xdist -k "single_stream_row or read_at_most_twice"`, then `git restore hooks/worktree-guard.py` | 3 failed (S1 parsed, S1 unbalanced, S5 at `[1, 2, 1, 2]`), 1 passed (S3); the file was restored and `git status` was clean |
| `python3 -c` printing `steer_to_switch("git")` and `steer_to_switch("git -C /x")` with `SPECSEAL_LANG` set to `en` and to `ko`, at `977b6613` and at `843c04dc`, then `cmp` per language | identical in both languages |
| `bin/test tests/e2e/creation/test_creation_flow.py tests/hooks/test_worktree_consent.py -q` | 63 passed |
| `bin/test tests/behaviour/test_the_frozen_reading_never_grows.py tests/text/test_a_rider_reaches_its_file.py -q` | 11 passed |
| `uvx ruff check` and `uvx ruff format --check` over `hooks/worktree-guard.py` and `tests/hooks/test_worktree_guard.py` | all checks passed; 2 files already formatted |
| `bin/seal layout --pairs` | 128 pairs, none in `tests/hooks/test_worktree_guard.py` |
| `grep -n "worktree-ok" hooks/worktree-guard.py` | string sites at `:1411-1413`, `:1829-1833`, `:2053-2058` and `:3350-3359`; the rest are docstrings and comments |
| `git grep` outside `seal/` and the changelogs for `retry with [worktree-ok]`, `rows 3 and 4 name no token` and `single-stream deny's way past` | only `steer_to_switch`'s sentence, its test pin at `tests/hooks/test_worktree_guard.py:2965`, and the rewritten comments |
