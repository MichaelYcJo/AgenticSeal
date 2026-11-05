# Implementation Plan: the README names every network place (#1382)

## Technical context

All coordinates were read at `d7f4d9bf`.

- `README.md:269` opens `## What runs on your machine`. The hook table
  begins at the line opening `| Gate |`, and its rows end before the
  sentence "No hook stops a session from switching the branch ...". The
  side-effects paragraph opens "No hook sends your code, your paths or your
  prompts anywhere." The network paragraph is `README.md:308` to `:312`.
  `## Commands` follows at `:314`.
- `README.ko.md:271` opens `## 내 컴퓨터에서 도는 것`, and its network
  paragraph is `README.ko.md:311` to `:316`. `## 명령` follows at `:318`.
- `tests/behaviour/test_chain_hooks_hardening.py:408` to `:437` pins the
  two hook sentences and refuses three count phrases. `conftest.flat` folds
  a file's line breaks. That is the reader *Scope* 3 extends. The new
  assertions read only the passage from the pinned sentence to the next
  heading, because `README.md:335` already names `/agentic:update` in the
  commands table, and a search over the whole file would pass with the
  network row gone.
- `hooks/version-check.py:23` to `:25` hold the docstring sentence
  *Scope* 4 rewrites. No case reads that sentence: `git grep "second network
  touch"` over `tests/` finds nothing (executed).
- The census table in `frame/design.md` *Grounding* holds every fact the
  rows state, with the coordinate of each. The crafter opens those
  coordinates before writing a row, as contract rule 5 asks, and writes no
  fact the census does not hold.

**The failure scenario of the chosen approach.** In six months a skill
gains a `gh` call or a hook gains a fetch, and nothing tells its author to
add a row. The README is then short again, and a directory reviewer reads a
list that misses a place. What limits that: the hook half is held by
`CONTRIBUTING.md` *House rules*, and the rest is held by review, which reads
a diff that adds a `gh` call or a `curl`. The census method in the design is
the procedure a later work item can re-run. Row 4 of *Alternatives
considered* is why no script holds it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Keep the hook paragraph and its pinned sentence, and add a lead sentence and one table for the commands and workflow steps (rows 3 to 8) | The hooks are in prose and the rest in a table, so a reader meets two shapes for one list. The pinned sentence and the hook table's test stay as they are, and the hooks' timing is already in the hook table's Where column | **Chosen.** It keeps two prior decisions, #1055's pinned sentence and #1102's hook table, intact, and it adds one table with six rows |
| 2. Replace the paragraph with one table of all eight places, hooks included | The hooks' facts would then stand in the hook table and the new table, two places that hold one fact. The pinned sentence would move, so the #1055 case would need new pins and give no new protection | Rejected: a second copy of the hook facts, for one shape |
| 3. Name exactly the issue's four places, as its proposal says ("Nothing else changes") | The issue's own *Done when* census finds four more: `seal gate`'s `gh pr view` (executed), `seal settle`'s `gh`, the workflow's own `gh` and push, and the CI clone the pull-request checks make. The directory answer would stay untrue of the README | Rejected: *Done when* outranks the proposal's sentence, because it is the test the issue sets. The issue's own `When` cell for `seal cost --post` also contradicts `skills/verify/orchestration.md`, and the README follows the skill |
| 4. Add a check that reads every network call in the shipped code and fails where the README's passage lacks one | It decides on spellings: a `gh` call reached through a helper, as in `settle.py#ask_gh`, or an instruction in prose, as in "push the branch", escapes any list of patterns. A false red stops a correct pull request. `skills/core/SKILL.md` *The rule a mechanism is kept against* says no script carries a list of spellings, and that a reading guessed from words never blocks | Rejected. The census method in the design stays a procedure a session runs |
| 5. Widen `CONTRIBUTING.md`'s rule from "every hook that reaches the network" to every shipped network call | The rule's conditions (an opt-in, a throttle, silence on failure) fit a hook and not a command a person runs. `docs/running/measuring-a-run.md` *Where a reading goes* argues exactly this for `--post`. Widening it is a rule change the issue did not ask for | Rejected for this work. `frame/questions.md` Q1 asks the owner, and the default leaves the rule as it reads |
| 6. Move the network list out of the README into a `docs/` document and link it | The owner's directory answer is "listed in README", and the reviewer reads the README. #1102 kept "the hooks that reach the network" on the page because no other shipped file states it | Rejected: the README is the place the answer names. This is the structure-replacing alternative, and the premise that keeps the structure is the owner's directory answer, which the issue body records (read) |
| 7. Leave `docs/running/measuring-a-run.md` and `hooks/version-check.py` alone, since the issue names only the READMEs | The README would say the orchestrator posts after each segment while the policy says only a person's typing starts the write. The hook's docstring would still call it the second and last touch. A reader would meet two contradicting accounts | Rejected: contract rule 19 corrects every sentence that states the old fact, in the same change. Policy outranks the README, so the policy sentence changes through `## Rule changes` |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* 1, 2, 3 and 4 of `frame/design.md` | S1 to S7. Narrow runs of `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and `tests/behaviour/test_release_hygiene.py`. The widened case is seen red with one row deleted. The census re-run over `git archive HEAD` and the `git grep` of S7 are recorded in the phase record | b7e392d8 |

## Operational impact

- No migration, environment variable, dependency or compatibility break.
- The directory reads the README at the next release's `dist` commit, as
  #1374 set up. Nothing is resubmitted.
- **Sibling overlap.** #238 works on version-check's notice and its test,
  and #1359 edits bare commit hashes tree-wide. This work edits
  `hooks/version-check.py` only in the module docstring sentence of
  *Scope* 4, at lines 23 to 25. A textual conflict at the release branch is
  possible where a sibling edits the same lines, and the orchestrator
  resolves it at the merge.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
