# Round 2 report — 1791940762, the record of truth is tests, not coordinates (#944)

| Field | Value |
|---|---|
| Round | 2, verifying |
| Target SHA | 475c666f8733c6198c3c0a8e818096a535c6b426 |
| Base | `origin/release/v0.22.0` (f975ea66) |
| Fix range checked | `5a3ffdb4..67275a50`, 8 commits, plus the orchestrator's 8a63e245 and 6b6c5248 |
| Reviewed by | warden, in a `git clone --no-local` of the worktree at the target SHA |

## What was asked, and how it was read

This round verifies round 1's eight fixes at their commits, answers round 1's
❓ row by running `mutation-check`, reviews the two orchestrator commits after
the fix range, and judges as code the six units the fix range created
(`round-1.md`'s `New units` row). It looked only inside those diffs, plus the
lines the claims under review cite.

The account under review is the eight fix commits' messages, round 1's
record, `overview.md`, `phases/phase-4.md`, `phases/phase-8.md`, the two
orchestrator commit messages and the PR body. Each claim was checked against
the code or a run, and the verdicts below say which.

## How the findings relate

- **Round 1's eight fixes hold, and round 1's ❓ is answered.** Each defect
  is gone at its commit. Each fix rewrote its text in place, and what stood
  only on the old fact left with it. Eleven `mutation-check` runs went red,
  one per sampled unit or pin.
- **The orchestrator's two commits are right except for one ceiling.** The
  workflow is restored byte for byte, and the price level matches what the
  checker computes. But 6b6c5248 lists `tests/test_pact_check.py` at a
  ceiling equal to its reading, against the rule `seal/budgets.md` states for
  a one-sided row (🟡 1).
- **The refresh left three sentences in `overview.md` describing the file as
  unrefreshed** (⬜ 2, a paperwork correction).

## Findings

### 🟡 1 — `tests/test_pact_check.py` is listed with no headroom, so the next refresh of `.test_durations` is likely to fail the gate

`seal/budgets.md:73` lists `| tests/test_pact_check.py | 121 |`. The file's
reading is 120.69 s: raw 136.6 s at the stated level of x1.132. The budget
shows 0 headroom (0.0 %). The same file's own comment (`seal/budgets.md:15-17`)
says how a one-sided row's ceiling is set: "its ceiling is 1.3 times its
reading, rounded up". `.github/scripts/budget_check.py:94` says the same thing
and gives the reason: one refresh moved files of 10 s or more 0.46 to 1.54
times the level. For a reading of 120.69 s that rule gives 157.

Executed. This refresh alone moved this file 1.49 times the level. Its reading
went from 81.0 s at base to 120.7 s. The commit message itself says the file
takes the same 22.2 s locally on both trees, so the move is runner noise.
Noise of that size, against a ceiling equal to the reading, fails the next
pull request whose refresh reads this file at 122 s or more. That pull request
would be red over a file it did not touch, and its fix would be a second
`Budget raised:` line for the same file.

Not a record and not a crash: the gate fails closed, toward red.

The fix needs two changes made together. The ceiling becomes 157, and the PR
body's line becomes `120 -> 157`. The checker compares the line's numbers
exactly. Executed in the clone, then restored: with both changes,
`budget_check.py --baseline origin/release/v0.22.0 --pr-body-env` exits 0.
With only the ceiling changed it exits 1 and names the line to write.

### ⬜ 2 — `overview.md` still describes `.test_durations` as unrefreshed after 8a63e245 refreshed it

- `overview.md:56`, a `## Not verified` row: "617 of 9,208 collected cases
  are unpriced (6.7 %), over `STALE_SHARE`, so
  `test_the_durations_file_prices_the_suite` is red until the file is
  refreshed", answerer the orchestrator.
- `overview.md:34`, the divergence row "`.test_durations` is pruned, not
  refreshed".
- `overview.md:77-79`, the `## Not done` bullet saying about 2,600 stale
  entries remain until the refresh drops them.

Executed: `test_the_durations_file_prices_the_suite` passes at the tip, and
the commit dropped 2,655 entries (11,863 at e05213e0, 9,208 at the tip). This
is the work item's own paperwork (`seal/specs/`), so it is a correction and
is not counted in `Needs a fix`. The `## Not verified` row matters most of the
three, because `unverified-check --baseline` reads that section. A row whose
check has since run makes that section say less than the truth.

## Round 1's fixes, one by one

Each was read at its commit in `git diff 5a3ffdb4..67275a50`. Where a run is
named, it was executed in the clone.

1. **`rules` resolves in the user's repository** (89b000a9). `ROOT` is gone
   from `.github/scripts/rules.py`. `--root` defaults to
   `optin.py#repo_root` of the current directory, falling back to the current
   directory itself (`rules.py:163-172`). The module docstring and both
   READMEs' new `rules` rows say so (`README.md:260`, `README.ko.md:247`).
   Mutation (`repo_root(...) or root` replaced by `root = root`): red,
   `test_with_no_root_the_targets_resolve_where_the_command_runs[subdirectory]`.
2. **`rules` no longer crashes on a target under an `if`** (04da85ca).
   `rules.py#docstring` takes the one span `coordinates.py#py_spans` gives for
   the name, which is walked the way `named_unit` walks it. It then reads the
   definition that starts and ends there, so the `next()` that raised is
   gone. Read: two definitions cannot share a start line and an end line, so
   the match is unique. Mutation (`ast.walk(tree)` replaced by `tree.body`):
   red on 3 cases, the under-an-`if` case among them.
3. **Indented rule paragraphs are counted** (7b8edffb). The regex is
   `(?:LIST_MARKER|[ ]{0,3})`, and the comment above it now matches what it
   does. The six `unenforced:` ceilings rose by 1, 8, 8, 6, 8 and 15. That
   totals 46, round 1's count file by file, and `budget_check.py` reports
   each row held at 0 headroom. Mutation (the old regex restored): red,
   `[an indented paragraph]`. §12 was checked for the class: no visible
   bold-led paragraph opens 4 or more spaces in, in any of the 61 rule files.
   The only 5 such lines sit inside an HTML comment in
   `templates/sdd-round.md:319-368`, which the count skips by design.
4. **The layout's resolver statement** (0bda17c7) is rewritten in place at
   `docs/the-record-layout.md:243-250`. Its `Enforced by:` line now names
   `test_a_name_defined_twice_is_no_target`, which exists at
   `tests/test_a_folded_statement_names_what_enforces_it.py:206`. There is no
   `.ko.md` edition to keep in step.
5. **The test-first cadence wording** (e28d7a5d). The two phrases are
   replaced at `skills/implement/orchestration.md:18` and
   `agents/smith.md:27`, and the bootstrap bullet is deleted. A `git grep`
   for *evidence feedback*, *evidence rows* and *feedback rule*, outside
   records and changelogs, finds nothing.
6. **The follow-up row on the sweep** (0c01f8ad) is deleted. The divergence
   row at `overview.md:44` is rewritten in place to say three rows changed.
   No *marker-shape* or *survivor sweep* text remains in `seal/follow-up.md`,
   `docs`, `agents`, `skills` or `templates`.
7. **The `(F2, built)` citation** (d978ba3d) is gone. No `(F<n>` citation
   remains in any rule file.
8. **The todo-layout case** (67275a50) now pins `tests-todo.md` alone,
   against `settle.py#process_plan`. Read: that function reads
   `PROCESS_TODOS` at the work item's own level and takes `rounds/` whole, so
   the new docstring's claim, a file under `rounds/` leaves "open rows and
   all", is what the code does. The comment block that stood on the removed
   fold went in the same commit. Three test references to `evidence-todo.md`
   remain, and they are not of this class. In
   `tests/test_a_process_record_drop_passes_the_readers.py:222` and
   `tests/test_settle_retires_the_process_record.py:422` it is a near-miss
   name the arm must keep. In `tests/test_settle_reads_before_it_removes.py`
   it is a fixture heading, which `overview.md` §*Not done* leaves to #942.

**The six new units, judged as code.** `DEFINITIONS`, `GATED`,
`test_a_target_the_resolver_finds_in_a_block_prints_its_sentence`,
`test_with_no_root_the_targets_resolve_where_the_command_runs`, `TODO_FILE`
and `test_the_todo_file_sits_where_settle_looks` have no defect found. The
`[top]` case of the no-root test would be red on the pre-fix code, where the
target resolved under the plugin's tree (read). The mutation above did not
turn it red because the mutation kept the current directory as the root.

## Round 1's ❓ — W2 and S11, answered by running them

Round 1 left one question open: were the moved kernel cases (W2) and the
re-pointed pins (S11) each really seen red? Eleven `mutation-check` runs
answer it, and every one exited 0 with `red`. Each ran against the whole
module named below, not a `-k` selection, and `git status` was clean after
the run.

- **W2, five units** in `skills/verify/scripts/coordinates.py`, against
  `tests/test_a_unit_is_bounded_where_a_parser_decides.py`. Each red case is
  the one `phases/phase-4.md` names for that unit.
  - `parsed_spans`, the span started at the `def`:
    `test_a_decorator_is_part_of_the_span`.
  - `normalise`, indentation stripped:
    `test_the_hash_does_not_ignore_indentation`.
  - `named_unit`, `A.b` accepted:
    `test_the_resolver_hands_each_caller_its_own_answer`.
  - `unescape`, the pipe left escaped:
    `test_an_escaped_pipe_matches_a_real_one`.
  - `PACT_ANCHOR_RE`, its look-behind removed:
    `test_a_word_ending_in_pact_is_not_a_pact_anchor`.
- **S11, three pins.**
  - The record layout's retire-process sentence, reworded: red,
    `test_each_carrier_says_when_the_process_record_leaves`. That is phase
    1's re-pointed pin.
  - The implement skill's step 2 heading, reworded: red,
    `test_each_home_states_its_rule_under_its_section`. That is phase 2's.
  - The template's `Pact notify` statement, reworded: red,
    `test_the_template_and_the_config_skill_carry_the_pact_row_alone`. That
    is phase 8's.
- **Round 1's fixes, three runs.** These are listed under fixes 1 to 3
  above.

The sample is 8 of the 21 kernel mutations and pins the two phases list. The
other 13 were not re-run.

## The orchestrator's two commits

- **8a63e245 restores `.github/workflows/test.yml` byte for byte.** The blob
  goes `8605019a → db3d18bc`, and `db3d18bc` is the blob e05213e0 started
  from. Against the base, the only workflow difference left is 95309a5d's
  removal of the `ledger` job. The commit's figure holds: 11,863 entries go
  to 9,208, which is 2,655 dropped.

  The file was measured at e05213e0, so the fix range's 7 new case ids are
  unpriced and one renamed id is stale:
  `test_the_two_todo_files_sit_where_the_release_guard_looks`. Both are
  inside the design. The durations case reads only collected ids, and it
  passes at the tip with 9,214 collected (executed).
- **6b6c5248's price level is the one the checker computes.** It prices the
  8,531 shared cases at x1.132, and `budget_check.py` would name the number
  if the level disagreed. Exit 0 with the PR body; exit 1 with an empty one,
  naming only the `slow-file` raise. The listed ceiling is 🟡 1.
- **Only one of the PR body's `Budget raised:` lines is read.** The six
  `unenforced:<file>` lines, and `Budget removed: ledger-rereads`, are inert.
  The `unenforced` family is new on this branch (761829e9), so against the
  base those rows are new, and a new row needs no line. `ledger-rereads` was
  a `report` row at base. Round 1's report said fix 3 "owes `Budget raised:`
  lines", which was wrong. The lines do no harm and need no change.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `tests/test_pact_check.py` is listed at a ceiling equal to its reading, 0 headroom, against the 1.3-times rule its own file states, so the next refresh likely fails the gate on an unrelated pull request | `seal/budgets.md:73` | open | executed: `budget_check.py` reads 121 s (raw 137 at x1.132) against 121, 0.0 % headroom; this refresh alone moved the file 1.49 times the level; read: `seal/budgets.md:15-17` and `budget_check.py:94` give 157 |
| ⬜ 2 | `overview.md` still says `.test_durations` is unrefreshed and its case red, after 8a63e245 refreshed it | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/overview.md:56` | open | executed: `test_the_durations_file_prices_the_suite` passes at the tip; also `overview.md:34` and `:77-79`; paperwork, not counted in `Needs a fix` |
| 🟢 | round 1's finding 1 is closed — `rules` resolves in the repository it is typed in, and both READMEs carry its row | `.github/scripts/rules.py:163` | confirmed | executed: mutation red on the subdirectory case; read: `ROOT` gone, the module docstring and `README.md:260`, `README.ko.md:247` |
| 🟢 | round 1's finding 2 is closed — a target under an `if` or a `try` prints its sentence, never a traceback | `.github/scripts/rules.py:62` | confirmed | executed: mutation red on 3 cases; the module passes |
| 🟢 | round 1's finding 3 is closed — indented rule paragraphs are counted, and six ceilings rose by 46 in total | `.github/scripts/budget_check.py:219` | confirmed | executed: mutation red; every `unenforced:` row holds; no visible paragraph opens 4 or more spaces in (§12) |
| 🟢 | round 1's finding 4 is closed — the resolver statement is rewritten in place with its third enforcer | `docs/the-record-layout.md:243` | confirmed | read: the named case exists at `tests/test_a_folded_statement_names_what_enforces_it.py:206`; the module passes |
| 🟢 | round 1's finding 5 is closed — the test-first cadence replaces evidence feedback, and the bootstrap bullet is deleted | `skills/implement/orchestration.md:18` | confirmed | executed: `git grep` for the three phrases outside records is empty |
| 🟢 | round 1's finding 6 is closed — the follow-up row is deleted and the divergence row is rewritten in place | `seal/follow-up.md:74` | confirmed | read: `overview.md:44`; executed: no sweep text remains in the rule files or `seal/follow-up.md` |
| 🟢 | round 1's finding 7 is closed — the F2 citation is gone | `docs/the-record-layout.md:17` | confirmed | executed: no `(F<n>` citation remains in any rule file |
| 🟢 | round 1's finding 8 is closed — the case pins `tests-todo.md` where `process_plan` reads it | `tests/test_the_set_a_work_item_always_has.py:308` | confirmed | read: `settle.py:773` and `:824-856` match the docstring; the module passes; the remaining `evidence-todo.md` strings are near-miss names and #942's fixtures |
| 🟢 | round 1's open question is answered — the W2 kernel cases and the S11 pins were seen red | `tests/test_a_unit_is_bounded_where_a_parser_decides.py` | confirmed | executed: 8 `mutation-check` runs over W2 and S11, each red on the case the phase record names; 13 of the 21 listed were not re-run |
| 🟢 | the fix range's six new units hold as code | `tests/test_the_rules_command_reads_each_rule_off_its_test.py:111` | confirmed | read and executed: no defect; the `[top]` case is red on the pre-fix code by reading |
| 🟢 | 8a63e245 restores the workflow byte for byte, and its durations file prices the suite | `.github/workflows/test.yml:94` | confirmed | executed: blob `db3d18bc` before e05213e0 and at the tip; the durations case passes with 9,214 collected |
| 🟢 | 6b6c5248's price level matches the checker, and the PR body's one line it reads is present | `seal/budgets.md:49` | confirmed | executed: exit 0 with the body, exit 1 with an empty one naming only the `slow-file` raise; the six `unenforced:` lines are inert |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on the four fixed modules, `tests/test_a_folded_statement_names_what_enforces_it.py` and `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, at 475c666f | 232 passed, 2 skipped (the two need the whole suite collected), exit 0 |
| `bin/test tests -q -k "test_the_durations_file_prices_the_suite or test_no_collected_id_carries_the_interpreters_path"` | 2 passed, 9,212 deselected, exit 0 |
| `budget_check.py --baseline origin/release/v0.22.0 --pr-body-env PRB --base-ref release/v0.22.0` with the PR body | exit 0; `slow-file:tests/test_pact_check.py` 121 against 121, 0.0 % headroom (🟡 1) |
| the same with an empty body | exit 1; only `slow-file:tests/test_pact_check.py 120 -> 121` is asked for |
| the same with the ceiling at 157 and the body's line at `120 -> 157`, the file then restored | exit 0, 36 s headroom; with the body unchanged, exit 1 naming the line |
| `mutation-check`, 11 runs: five W2 kernel units, three S11 pins, three round-1 fixes | all 11 `red`, exit 0; `git status` clean after |
| `git show` of e05213e0 and 8a63e245 for `.github/workflows/test.yml` | `db3d18bc → 8605019a → db3d18bc` |
| `.test_durations` read at base, e05213e0 and HEAD for `tests/test_pact_check.py` | 81.0 s / 81.0 s / 136.6 s over 68 ids; entries 13,482 / 11,863 / 9,208 |
| a scan of the 61 rule files for visible bold-led paragraphs 4 or more spaces in | 5 lines, all inside an HTML comment in `templates/sdd-round.md` |
| the PR's CI | read, not run: at the time of reading, four pytest legs were still pending |
| the broad gate (full suite, lint, typecheck) | not yet — the sealer's, once, after the rounds settle; nothing above stands for it |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Regression tests to plant

None. 🟡 1 is a data row, and `budget_check.py` reads that row on every pull
request.

## Paste-ready fixes

### 🟡 1

`seal/budgets.md:73`, in place:

```markdown
| tests/test_pact_check.py | 157 |
```

The PR body's line, replacing the `120 -> 121` one:

```
Budget raised: slow-file:tests/test_pact_check.py 120 -> 157: measured 121 s at the corrected price level on one Windows run (raw 137 s at x1.132), listed at 1.3 times that reading as seal/budgets.md states for a one-sided row; locally the file takes 22.2 s on both the base and this branch, so the file did not grow
```

### ⬜ 2

`overview.md:56`: delete the `.test_durations` row from `## Not verified`.
Then rewrite `:34` in place:

```markdown
| `.test_durations` is pruned, then refreshed | `plan.md` phase 4 "`.test_durations` from the run's `test-durations` artifact" / phase 4 removed the deleted files' entries and carried the 54 moved and renamed cases' Windows prices; 8a63e245 replaced the file with run 38646055747's unsharded Windows leg, which dropped 2,655 ids nothing collects | the build, then the orchestrator | no run existed without a push; the refresh came once the pull request was open |
```

and delete the `:77-79` bullet ("About 37 `.test_durations` entries …").

Needs a fix: yes — 🟡 1: `tests/test_pact_check.py`'s slow-file ceiling is listed at its reading, 121, with no headroom; it is 157 by the file's own rule, and the PR body's line moves with it

Loses a record or crashes: no

The broad gate has not come due: 🟡 1 is open, so the sealer's spawn waits
for the round that closes it.

## Proof block

```
📋 code-review applied
· spec:     seal/specs/1791940762-…/rounds/round-1.md, rounds/round-1-report.md, overview.md (34, 44, 48-82), phases/phase-4.md (40-130), phases/phase-8.md (40-110), phases/phase-2.md (88-130), phases/phase-1.md (60-80), phases/phase-5.md (50-70), spec.md (S11 row)
· opened:   git diff 5a3ffdb4..67275a50 (all of it but .test_durations), git show e05213e0 / 8a63e245 / 6b6c5248, .github/scripts/rules.py (whole), .github/scripts/budget_check.py (1-160, 295-330, 870-910), skills/verify/scripts/coordinates.py (140-240, 480-560), skills/settle/scripts/fold_check.py (180-200, 280-330, 480-500), skills/settle/scripts/settle.py (760-870), hooks/optin.py (40-80), seal/budgets.md (1-75), templates/sdd-round.md (290-375), templates/config.md (420-436), tests/test_a_process_record_drop_passes_the_readers.py (200-250), tests/test_settle_retires_the_process_record.py (405-440), tests/test_settle_reads_before_it_removes.py (25-60), tests/test_the_rules_claude_md_names_have_one_home.py (40-60), bin/rules, bin/rules.cmd, bin/test, bin/mutation-check, skills/verify/scripts/mutation_check.py (docstring), the PR body
· verified: executed — the probes table above; read — the fix-by-fix notes; unverified — the full suite, lint and typecheck (the sealer's), the 13 W2/S11 mutations not re-run (nobody owes them; the sample was red throughout), and the PR's own CI run (pending at reading; the orchestrator reads it)
```
