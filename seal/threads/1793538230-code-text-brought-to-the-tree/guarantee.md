# Guarantee: 1793538230-code-text-brought-to-the-tree

| Field | Value |
|---|---|
| Broad gate | c5ea675c against 14bfd992 |

The base `release/v0.27.3` resolves through `release/v0.27.3@{upstream}` to `cd694aa3` (executed: `git rev-parse --verify --quiet`). The merge base of HEAD with it is `14bfd992`, the commit the gate ran against. `cd694aa3` adds #1271 and #1272 to it. Those two change `agents/crafter.md`, `skills/implement/SKILL.md`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and two other work items' records. None of the seven code files this work changes is among them (executed: `git diff --name-only 14bfd992 cd694aa3`). `trail/gate.md`'s run `c5ea675c` is an ancestor of HEAD. Between it and HEAD, `git log --no-merges --name-only c5ea675c..HEAD ^cd694aa3` lists one commit, 3fed6313, and that commit touches only `seal/threads/1793538230-code-text-brought-to-the-tree/trail/gate.md` (executed). `seal pr-body … --check` exited 0 on the body file (executed). Git carries no `seal/parity.md` (executed: `git ls-files`), so this block owes no `original:` line.

## Claims re-run

The re-runs were made in a `git clone --no-local` of the worktree at 3fed6313, under `<scratchpad>/1793538230-code-text-brought-to-the-tree/at-base/`, with the worktree's `.venv` interpreter. The clone was removed afterwards, and the tree under audit was not touched.

| Claim | Source | Command | Result |
|---|---|---|---|
| Seen red: before the fix, the new case fails for all three scripts, each with `stdin` at `('cp949', 'strict')`, `stderr` at `('utf-8', 'replace')` and exit codes 2, 0 and 2 | `trail/phases/phase-1.md`, *Seen red* | `git checkout cd694aa3 -- .github/scripts/release_report.py .github/scripts/release_seal.py .github/scripts/rules.py`, then `python -m pytest tests/hooks/test_console.py -q -p no:xdist -p no:cacheprovider -k release_script` | Holds (executed): 3 failed, exit 1. Each failure diff shows `{'stdin': ('cp949', 'strict'), 'stdout': ('utf-8', 'replace'), 'stderr': ('utf-8', 'replace')}` against the `STREAMS` answer, with exit codes 2, 0 and 2. |
| The case passes after the fix | `trail/phases/phase-1.md`, *Seen red* | The same `pytest` command at 3fed6313 | Holds (executed): 3 passed, exit 0. |
| The case reads `STREAMS` at run time, so a change to `STREAMS` turns it red (design S2) | `trail/phases/phase-1.md`, *Mutation*, the `STREAMS` row | In `hooks/lib/console.py`, `("stdout", "replace")` changed to `("stdout", "strict")`, then the same `pytest` command | Holds (executed): 3 failed, exit 1. Restored after the run. |
| A script's loop that leaves out a pair turns its parameter red | `trail/phases/phase-1.md`, *Mutation*, the `release_seal.py` row | In `.github/scripts/release_seal.py`, the `("stdin", "replace"),` line deleted, then `pytest … -k "release_script and release_seal"` | Holds (executed): 1 failed, exit 1. Restored after the run. |
| The phase-1 modules pass at the work's head | `trail/rounds/round-1.md` *Probes*, row 1 (144 passed); phase 1's boundary set | `python -m pytest tests/hooks/test_console.py tests/github/test_release_report.py tests/github/test_release_seal.py tests/github/test_rules.py -q -p no:xdist -p no:cacheprovider` at 3fed6313 | Holds (executed): 144 passed, exit 0. |
| #1258 and #1231, merged into the base after the broad run, leave this work whole | The orchestrator's part of the pull request body, the last bullet | In the clone, `git merge cd694aa3` (no conflict), then the four modules above plus `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, the test the moved base adds | Holds (executed): 153 passed, exit 0. The passage test reads `*.md` files, and this work changes no `*.md` outside `seal/`. |
| S4: no `dispatch.py:N` citation stands outside `seal/threads/`, and the only `path:line` left in shipped code text is the eval fixture | `trail/phases/phase-2.md`, the S4 rows | `git grep -n "dispatch.py:[0-9]" -- . ':!seal/threads'`; `git grep -nE '[A-Za-z_/.-]+\.(py\|md\|yml\|sh):[0-9]+' -- hooks skills .github/scripts bin evals/scripts` | Holds (executed): no line, exit 1; only `evals/scripts/rule_cases.py:809`. |
| S5: `overwide_rows` stands nowhere outside `seal/threads/` | `trail/phases/phase-2.md`, the S5 row | `git grep -n "overwide_rows" -- . ':!seal/threads'` | Holds (executed): no line, exit 1. |
| S6: the listing command prints 19 files, which the console docstring names by group | `trail/phases/phase-2.md`, the S6 row; `hooks/lib/console.py`, the module docstring | `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'` | Holds (executed): 19 files, the three `.github/scripts/` files, `hooks/dispatch.py`, `hooks/lib/console.py` and 14 under `skills/*/scripts/`. Each group is named in the docstring (read). |
| None of the three scripts reads `stdin` outside its loop | `frame/design.md` *Data & interfaces*; `changelog.md`, the first bullet | `git grep -n stdin -- .github/scripts/release_report.py .github/scripts/release_seal.py .github/scripts/rules.py` | Holds (executed): three lines, each the loop's `("stdin", "replace")` pair. |
| Every production path that starts the three scripts runs `__main__`, so moving `release_seal.py`'s loop out of `main` loses no caller | `trail/rounds/round-1.md`, the second confirmation | `git grep -n "release_seal\|release_report\|rules\.py" -- .github/workflows bin skills/implement/scripts/seal.py` | Holds (executed): `publish-release.yml:158`, `hygiene.yml:174` and `test.yml:291` run each file as a script, and `seal.py:178` names `rules.py` for its `execv`. |
| `hooks/lib/cmdline.py`'s paragraph says what `hooks/dispatch.py#run_gate` does | `trail/phases/phase-2.md`, decision 1 | Read `hooks/dispatch.py:114-157` and the module docstring at lines 25-30 | Holds (read): `run_gate` appends the failure to `FAILED` and returns `""`. The docstring says the skip writes a record "once per gate per session" and that the `stop` group says it. |

**Removes**, each row of `frame/design.md` *## Removes*, confirmed gone at 3fed6313 (executed):

| Row | Command | Result |
|---|---|---|
| `hooks/dispatch.py:72` and "silence" in `hooks/lib/cmdline.py` | `grep -n -i "silence\|except Exception" hooks/lib/cmdline.py`, and the S4 command above | no line |
| `test_release_hygiene.py#overwide_rows` in the fence comment | the S5 command above | no line |
| The figure "five" in `hooks/lib/console.py`, and "seven" twice in `tests/hooks/test_console.py` | `grep -n -i "five scripts\|seven" hooks/lib/console.py tests/hooks/test_console.py` | no line |
| `errors="replace"` for `stderr`, and the two-stream tuple, in the three scripts and in `release_seal.py#main` | `grep -n '"stderr"\|errors=\|reconfigure' …` over the three scripts; `release_seal.py:532-551` read | Each `stderr` pair is `backslashreplace`. The only other `errors="replace"` lines are file reads (`release_report.py:196`, `rules.py:216`). `main` holds no loop. |

The changelog names the same removals, and each is covered by the table above.

**Not re-run:** the other seven mutants of phase 1's table, and phase 2's S6 number-word search. Both are read, not executed, and no verdict rests on them. The figure "suite 6271 passed, 9 skipped" in the orchestrator's part of the body is unverified, because `trail/gate.md` holds only the run line. The record of that run is the gate's, and the orchestrator answers for the figure. Whether the new case holds on the Windows legs (`frame/questions.md` Q1) is unverified, and the pull request's Windows `pytest` legs answer it.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | Five scope items: the three scripts give `STREAMS`' three pairs first in `__main__`, pinned by one case reading `STREAMS` at run time; `cmdline.py` cites `run_gate` by name and drops "silence"; the fence comment drops `overwide_rows`; the console docstring names the places that copy the loop, with no count; the test docstring drops "seven". After two folds, *Scope* 4 says `chain_check.py` states a reason and #1255 owns which entry points owe the answer | Issue #1235's scope and *Done when*; the diff; the tree at each Removes row | none |
| the build | Phase 1 built Scope 1 and showed the case red against the base. Phase 2 built Scope 2 to 5. Phase 2's decision 2 still states the "standalone by design" premise it took, and round 2's fourth confirmation judged it a record of that time | The design; the diff; each claim re-run above | Its decision 2's premise is contradicted by the tree. Rounds 1 and 2 corrected it in the code, and the record is history, so it is no disagreement about the work |
| the last round | Round 3, at bee67bfe, is verifying: it confirms round 2's findings 1 and 2, opens nothing, and finds the fixes converged | The code at HEAD: `hooks/lib/console.py:50-54` and `chain_check.py`'s loop before its loads (read); the changelog | none. It holds no `fixed` finding, so no fix pass awaits this audit |
| the changelog | Two `### Fixed` bullets: the three scripts' stream answer, with arguments, exits and stdout unchanged and no `stdin` read; and the drifted texts, where only `chain_check.py` states a reason for its copy and #1255 owns which entry points owe the answer | The diff; the design; the re-run `stdin` and Removes checks | none |
| the orchestrator's part of the pull request body | `Closes #1235`, `fix:`, the frame folds and their regression route, Q1 left to the Windows legs, and the merge of the base at c5ea675c with the broad run against 14bfd992. It also says #1258 and #1231 touch none of this work's files | The diff; `frame/plan.md` *Judgments of the run*, both rows; issue #1235's comment it links (executed: `gh issue view 1235 --json comments`); `git diff --name-only 14bfd992 cd694aa3`; the merged narrow run above | none. The suite count it gives is unverified, as stated above |

```seal
target: 3fed6313 against cd694aa3
Verdict: sealed
```
