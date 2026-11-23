# Phase 2: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

## What this phase found

**The frame holds for this phase.** Each coordinate `frame/design.md` G10 to G14 gives was opened at `cfd9ee98e` and stood as the frame read it at `15636c7f0`: `lib/gaps.py#OVERVIEW` and its comment, its readers in `settle.py` and `unverified_check.py`, `broad_gate.py#CHAIN_SEALING` and the case that held it equal, the two copies of the `yes` switch, the roll script's `LABEL`, and the delimiters in `lib/lines.py`, `lib/fields.py` and `lib/tables.py`. `seal/follow-up.md` holds no row. Judged against `skills/implement/SKILL.md` *1. Read the documents that outrank the code first*.

**Decisions settled while writing the code.** Each was judged against `frame/design.md` *Scope* and *Data & interfaces*, which name the homes and leave the rest to the build.

- `settle.py` reads the closing memo's name as `GAPS = _optin.GAPS`, beside `DESIGN`, `PLAN` and `CHANGELOG`, which it already took from `lib/optin.py`. `unverified_check.py` already loads `lib/optin.py` as `OPTIN`, and its module name `GAPS` is the loaded `lib/gaps.py`, so it reads `OPTIN.GAPS`.
- `broad_gate.py#main` loads `chain_check.py` after the redirect to the tree's own gate and after the line that names the running copy, and before `gate`. A copy that hands over to the tree's gate needs no check of its own, and the refusal stands under the line that says which copy refused. The chain arm reads `SEALING` from the module the loader already holds. `gate` takes no new argument, so the cases that call `gate` directly keep their calls.
- The path `skills/code-review/scripts/chain_check.py` is spelt once in `broad_gate.py`, as `CHAIN_CHECK`. `CHAIN`, the path the arm runs, is built from it, and `rounds_rows` loads through it.
- A `chain_check.py` that is absent stops the gate with the loader's sentence at exit 2, as `frame/design.md` *Scope* item 5 asks. A `chain_check.py` that raises while it executes is not caught: the exception reaches `main` unchanged and the process ends at exit 1 with a traceback, before any arm runs. `lib/sibling.py#load` leaves that case to the caller, and the gate treats every other module it loads the same way. The frame's sentence "where the module cannot be loaded, the gate stops at exit 2 with the loader's sentence" holds for an absent file only.
- `lib/config.py#switch` stands in its own section, after `declared_mode`, because neither the reference roots nor the policy root reads it. `SWITCH_NOT_YES` is built by concatenation around `SWITCH_ON`, so the value `yes` is spelt once and `{key}`, `{value}` and `{off}` stay fields.
- `lib/blocks.py#FENCE_RUN` is a compiled pattern, because `lib/fields.py` calls `.match` on it. `FENCE` and `BLOCK_LOOKING` are built from `FENCE_RUN.pattern`. The comment kind of `lib/tables.py#HTML_KINDS` is built from `re.escape` of `blocks.OPENER` and `blocks.CLOSER`.

**Departures from the frame.**

- `settle.py#misplaced` read its `reader` argument for `OVERVIEW` alone. With the name read from `GAPS`, the argument has no use, so it goes, with its two call sites and the two calls in `tests/skills/test_settle.py#Test_misplaced`. `frame/design.md` *Removes* does not name it. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*, which removes what stood on the old fact in the same commit.
- The comment `roll_flow_measurement_issue.py#close_issue` leaves on a closed log spelt `flow-measurement` inside its f-string. It now names `{LABEL}`, and the comment reads as before. S8's search could not find it, because the label there is not a whole string literal.
- With `test_the_gate_and_the_check_spell_the_flag_alike` gone, no case watched that the chain arm passes the flag: mutant g2 below SURVIVED the whole of `tests/skills/test_broad_gate.py`. `6c9167b20` adds one assertion to `Test_gate::test_accepts_a_green_tree_and_runs_every_check_in_order`: the arm's command, as the kept `chain.txt` records it, ends with `chain.SEALING`. It reads the command the gate ran, not a constant, so S15's search does not find it. g2b is red against it.
- The docstring of `lib/gaps.py#check_text` cited `lib/lines.py#OPENER`, and now cites `lib/blocks.py#OPENER`.

**Seen red.** The S6 case and the three `Test_switch` cases were each run before their code was written, against the tree as it stood: `3b8337e92` for S6 and `715018a09` for `Test_switch`. Each was then run against `15636c7f0`, as the plan row asks. That tree was written under this phase's scratch directory through a temporary index (`git read-tree`, then `git checkout-index`), because `git archive` leaves `tests/` out by `.gitattributes`. Each case was added there alone and run with this worktree's `.venv`. Both runs of each failed the same way.

- `Test_main::test_refuses_a_copy_without_its_chain_check_before_any_arm` failed on `assert out.returncode == 2`: the gate printed `BROAD GATE FAILED`, with the chain arm at exit 2 on `can't open file .../chain_check.py`, and exited 1.
- The seven parametrised runs of `Test_switch` each failed with `AttributeError: module 'config_under_test' has no attribute 'switch'`.

**Mutation runs.** Each ran after its commit, one break per run, through `bin/seal mutate`. Every verdict is `red` unless it says otherwise, and each failing line was read for the guard named.

| Run | Unit and break | Case that went red |
|---|---|---|
| s1 | `switch`: the value compared lowercased | `test_refuses_any_other_value_and_a_refusal_naming_the_key[Yes]` |
| s2 | `switch`: the empty and absent value no longer silent | `test_refuses_no_root_no_key_and_an_empty_key_in_silence[no file]` |
| s3 | `switch`: the refusal answered with no sentence | `test_refuses_any_other_value_and_a_refusal_naming_the_key[written twice]` |
| s4 | `SWITCH_ON` read as `on` | `test_accepts_yes_exactly_as_on_and_says_nothing` |
| s5 | `SWITCH_NOT_YES` without its closing words | `test_refuses_any_other_value_and_a_refusal_naming_the_key[Yes]` |
| s6 | `pr_body.py#seal_mark`: the switch closed by `""` in place of `NO_MARK` | `tests/skills/test_pr_body.py::Test_seal_mark::test_refuses_a_row_other_than_yes[Yes]` |
| s7 | `release_seal.py#mark_on`: the switch asked for the pull request's key | `tests/github/test_release_seal.py::Test_main::test_a_row_other_than_yes_attaches_nothing_and_puts_the_results_alone[Yes]` |
| g1 | `broad_gate.py#main`: the early load of the check taken out | `Test_main::test_refuses_a_copy_without_its_chain_check_before_any_arm`, on `not keep.exists()`: the suite arm had run |
| g2 | the chain arm: `sealing` dropped from its command | none: SURVIVED the whole file at `7adbf590d` |
| g2b | the same break, after `6c9167b20` | `Test_gate::test_accepts_a_green_tree_and_runs_every_check_in_order`, on the new `endswith` line |

s1 to s5 also ran as one call of five mutants, with five `red`. s6 and s7 show the cases `frame/design.md` S7 names watch the new call sites; those cases pass unchanged.

**What moved and adds no behaviour.** *Scope* items 4, 7 and 8 rename or move a value, and each reader prints what it printed. The existing cases prove them at the new names: `tests/lib/test_gaps.py`, `tests/skills/test_unverified_check.py` and `tests/skills/test_settle.py` for `GAPS`; `tests/github/test_roll_flow_measurement_issue.py` and `tests/skills/test_session_cost.py` for the label; `tests/lib/test_blocks.py`, `test_lines.py`, `test_fields.py`, `test_tables.py` and `test_gaps.py` for the delimiters and the fence run. The census of the old spellings is the design's searches, run at `a2b5ec4e4`. Each search that prints nothing there was also run at `cfd9ee98e`, where it found its target.

- S4: `git grep -n '= "gaps.md"' -- '*.py' ':!tests'` printed `lib/optin.py:62` alone. `git grep -n 'OVERVIEW' -- lib skills` printed nothing; at `cfd9ee98e` it found 11 lines in `lib/gaps.py`, `settle.py` and `unverified_check.py`.
- S5: `git grep -n '"--sealing"' -- '*.py' ':!tests'` printed `skills/code-review/scripts/chain_check.py:227` alone. `git grep -n 'CHAIN_SEALING' -- '*.py'` printed nothing; at `cfd9ee98e` it found 2 lines in `broad_gate.py`.
- S7: `git grep -n -e MARK_ON -e KEY_NOT_YES -e KEY_REFUSED -- '*.py' ':!tests'` printed nothing; at `cfd9ee98e` it found 9 lines in each of the two scripts. `tests/skills/test_chain_check.py` holds a fixture pair named `MARK_ON`, a config row it writes, which copies no script's constant and stands.
- S8: `git grep -n '"flow-measurement"' -- '*.py' ':!tests'` printed `skills/verify/scripts/session_cost.py:2745` alone; at `cfd9ee98e` it printed the roll script's line too.
- S9: the delimiter search printed `lib/blocks.py:104`, `lib/blocks.py:105` and `skills/code-review/scripts/pr_body.py:896`, the line *Scope* puts out. `git grep -n -F '~{3,}' -- '*.py' ':!tests'` printed `lib/blocks.py:99` alone; at `cfd9ee98e` it printed three lines.
- S15's first search printed nothing; at `cfd9ee98e` it printed `tests/skills/test_broad_gate.py:199`, the case this phase removed.

**The boundary run.** The set is the plan row's twelve files, the 91 test files `git grep -l` lists over `tests/` for the names of the changed modules, and `tests/text` and `tests/behaviour`, which hold every test file that declares no `TARGET`: 42 arguments to one `bin/test -q` command, at `6c9167b20`. It passed: 5169 passed, 10 skipped, and 5 warnings, each a `UserWarning` from `tests/behaviour/test_a_cited_section_stands_in_its_file.py` about a pending rule change of another work item. `a2b5ec4e4` then rewrapped one comment and one docstring of `pr_body.py`, and `tests/skills/test_pr_body.py` passed after it, 107 cases. `bin/seal layout --pairs tests` names no pair among this phase's cases.

**For the next phase.** `seal gate` now loads `chain_check.py` in `main`, so the `sibling.going_on` block of `broad_gate.py#rounds_rows` is not reached with an absent check through the command; `gaps.md` *Not done* says why it stays. `lib/blocks.py` holds `FENCE_RUN` beside `FENCE`, and `lib/config.py` holds `switch` beside `declared_mode`.
