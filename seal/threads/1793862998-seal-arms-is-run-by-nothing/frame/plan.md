# Implementation Plan: 1793862998-seal-arms-is-run-by-nothing

## Technical context

`seal mutate` (`skills/verify/scripts/mutation_check.py`, 740 lines) loads `skills/verify/scripts/arm_check.py` (1,308 lines) by path at lines 161 to 177 and binds three of its functions, `clear_bytecode_cache` (`arm_check.py` lines 765 to 818), `restore` (lines 821 to 840) and `command_words` (lines 1162 to 1184). Those three use only the standard library (`os`, `sys`, `hashlib`, `shlex`), so they move without bringing any of `arm_check.py`'s tables or dataclasses along. `mutation_check.py` already imports `hashlib`, `os` and `sys`; `shlex` is the one import the move adds, and `importlib.util`, used only by `_sibling` (lines 167 and 168), is the one it takes out (read: its import block, lines 120 to 132).

`tests/skills/test_arm_check.py` (2,564 lines) holds the only cases for four behaviours of those functions (design G9). `tests/skills/test_mutation_check.py` (1,718 lines) loads its target through `module()` (line 172) and mostly calls `main`; the moved cases call the functions on that same module.

Three test modules use `seal arms` as an example or a classified row, and their cases fail once `TOOLS` drops `arms` (design G10, *Scope* item 7). `docs/running/the-broad-gate.md` carries a check line naming both deleted files, which `tests/github/test_rules.py` holds against the tree (design G6, G7). So the code, the policy root and those tests change in one commit, as `skills/core/SKILL.md` *The rule a mechanism is kept against* asks of a change and what stood on it.

Failure scenario of the chosen approach, six months out: `seal mutate` is the one caller, and a second command that needs a bytecode clear or a byte-exact restore copies them out of `mutation_check.py` rather than importing them. The cost is a second copy that can drift. That is the question to ask when such a command is framed, and the answer then is a shared module under `skills/verify/scripts/`. No such command is proposed now.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1 Keep `seal arms`, its job and its seven issues, and repair the issues | Seven open issues and a CI job are kept for a command no agent runs and no record shows run (#1393's *Symptom*). Each repair spends a review chain on a mechanism that has caught nothing on record. | Rejected. The premise that would keep the structure is a record of what it caught, and the owner's decision of 2026-11-05 reads that record as not outweighing the cost (design G1, G2). This frame does not reopen it. |
| A2 Move the three shared functions into `mutation_check.py`, its one caller, and delete `arm_check.py` whole | Covered under *Technical context*: a later second caller copies them. | Chosen. One caller, one home, and the path loader with its `sys.modules` registration goes. |
| A3 Keep the three functions in a new shared module under `skills/verify/scripts/` | A module with one caller keeps the path loader and a second file a reader has to open for three functions. `mutation_check.py`'s docstring, lines 105 to 111, gives the loader's cost: a bare import fails under `PYTHONSAFEPATH` and under an `importlib` spec. | Rejected while `seal mutate` is the only caller. |
| A4 Keep `arm_check.py` holding only the three functions, with no command | The file's name and its docstring describe arms, and a reader opening it for the bytecode clear finds a module named for a command that does not exist. | Rejected. |
| A5 State the policy root's change in `## Rule changes` as a `remove` with a `from`, for the settle | `seal rules --check` refuses the check line naming the two deleted files at HEAD from this merge to the settle, and `tests/github/test_rules.py` goes red (design G6). A `remove` with no `from` would take out the section's other rules. | Rejected. `docs/` is edited in place, as work item `1793756609` did on the same grounds (design G7). |
| A6 Keep the `arms-grammar` job, pointed at `tests/skills/test_mutation_check.py` | It would keep 3.13 and 3.14 running the moved cases until #1065. It would also be a new job the owner did not decide, and #1065 already holds the decision for 3.14 (design G3). | Rejected. The gap is recorded in design *Not covered until #1065* for `gaps.md`. |
| A7 Keep `.test_durations`' 100 entries for a later refresh | `pytest-split` gives an unknown case the average and never drops one, so nothing breaks. The entries would price cases that no longer exist, and `.github/scripts/release_report.py` reads per-file seconds from the file. | Rejected. The entries go, as pull request #1333 did for its deleted cases (design G13). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 and 2. `arm_check.py` still exists and `seal arms` still runs, so this phase stands alone. | The four moved cases and every case of `tests/skills/test_mutation_check.py` pass at the new path, with no case written new (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*); `grep -n "arm_check" skills/verify/scripts/mutation_check.py` prints nothing | 8eb4b2d5 |
| 2 | *Scope* items 3 to 8, in one commit, because the check line of *Scope* item 5 names files *Scope* item 3 deletes | The modules *Scope* item 7 names, `tests/skills/test_seal.py`, `tests/github/test_rules.py`, `tests/behaviour/test_release_hygiene.py` and `tests/text/test_ci_gives_the_checks_what_they_need.py` pass; the command of design G14 prints nothing outside `seal/threads/` and exits 1; `bin/seal arms` exits non-zero | |

## Operational impact

`seal arms` stops existing. A person with a script that calls it gets argparse's invalid-choice refusal. No agent definition, hook or workflow outside the removed job calls it (design G16, G14). The `arms-grammar` check name disappears from pull requests. No ruleset requires it (`docs/releasing/branch-and-release.md` *Work accumulates on a release branch*), so no ruleset changes. No new dependency, environment variable or migration.

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
