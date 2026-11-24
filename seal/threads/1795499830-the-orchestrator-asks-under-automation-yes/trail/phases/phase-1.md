# Phase 1: 1795499830-the-orchestrator-asks-under-automation-yes

## What this phase found

### The frame, read against the tree before the build

The frame holds for this phase. At `06b72451c`, the coordinates it hands the build stand where it says (read): `lib/routing.py:103` and `:205` state that no script decides on `Automation`, `tests/behaviour/test_chain_hooks_hardening.py#HOOK_ENTRIES` and `#HOOK_FILES` stand at lines 28 and 29, `skills/implement/scripts/seal.py#other_worktrees` at line 1584, and `ruff.toml` lints `hooks/*.py` and `lib/*.py` at 3.9. The count search of `frame/design.md` *Grounding* printed the 36 lines it lists (executed). `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser` lets a citation through where a pending item's `from` holds it and its `to` does not (read), so G12's reading of the renamed `CONTRIBUTING.md` item holds, and the module passed at the boundary run.

### Decisions settled while building

- **`open_declarations` answers `[]` for an empty `cwd`.** `git -C ""` runs git in the process's own directory, so an empty `cwd` would read the work items of whatever repository the hook process started in. The guard is the one `lib/routing.py#item_dir` keeps for an empty root. Grounds: `frame/design.md` *Scope* item 1, which lists the inputs that answer `[]`; an empty `cwd` names no repository, as a directory outside git does.
- **The hook reads `payload["cwd"]` with no type check.** A `cwd` that is missing or not a string raises in `open_declarations` or in the payload read, and the `__main__` block prints nothing for it, which is what *Scope* item 2 asks. A first version checked `isinstance(cwd, str)`; no case could tell it from the catch, so it went in `fea9cbf9e`. Grounds: `frame/design.md` *Scope* item 2, and `skills/core/SKILL.md` *The rule a mechanism is kept against*.
- **A question with no string `header` is named by its `question` text.** *Scope* item 2 names a refused question by its `header`. Claude Code sends one with every question (`frame/design.md` *Grounding*, executed by the framer), and a missing one would otherwise print `None`. Grounds: `frame/design.md` *Data & interfaces*, the input shape.
- **The porcelain listing is split on `\n`, not `splitlines`.** `tests/censuses.py#splitlines` flags `.splitlines(` in `lib/`, and git prints LF. Grounds: `CONTRIBUTING.md` *The test layout*, the census rule.
- **`declare_automation` stands in `tests/conftest.py`.** Both `tests/lib/test_routing.py` and `tests/hooks/test_ask_under_automation.py` write a declaration with an `Automation` row, and `tests/hooks/test_ask_under_automation.py` runs the command through `tests/hooks/test_core_start.py#start`, which takes an `event` now. Grounds: `CONTRIBUTING.md` *The test layout*, a helper two test files use is defined once.

### Departures from the frame

- **The hardening case is renamed.** `test_the_plugin_registers_two_hooks_and_writes_none_into_git` became `test_the_plugin_registers_its_hooks_and_writes_none_into_git`, because the old name states the count *Scope* item 6 removes outside the READMEs' list. The one other file naming it, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#OPENS_NOTHING`, names the new one (executed: `git grep -n registers_two_hooks -- . ':!seal/threads'` prints nothing at `752164072`). Under `seal/threads/`, one line of `1794396808-test-files-declare-no-target/trail/phases/phase-3.md` names the old name, as a record of what that phase met, and stays. The rename adds no behaviour; the existing case runs at the new name and passed at the boundary run.
- **One case beyond the frame's list, in `tests/lib/test_routing.py`.** `Test_open_declarations::test_refuses_a_listing_from_a_git_that_exited_non_zero` holds the non-zero exit guard *Scope* item 1 names. Without it, `seal mutate` breaking that guard survived (row R6 below): a real git that fails prints no worktree line, so nothing told the guard from its absence. The case puts a stub `git` first on `PATH` that prints a listing and exits 1, and skips on Windows, where a `sh` script does not start by name (`gaps.md`).
- **One case beyond the frame's list, in the hook's module.** `test_refuses_a_marker_with_nothing_after_it_on_its_line` holds the "same line" half of *Scope* item 2's form: `No default:` at a line's end, with the reason on the next line, states nothing.
- **`CONTRIBUTING.md` *House rules* says how the `PreToolUse` hook refuses.** The item said no hook returns the exit 2 that keeps a turn going. It now adds that the `PreToolUse` hook refuses a call through the deny it prints and the session goes on, so a reader does not take "exit 0" to mean the hook never refuses.
- **`lib/launch.py`'s docstring adds the third consequence.** Below the floor, behind ` || exit 0`, no question would be refused, beside the core and the stamp it already named.

### Seen red

Every new case was first run against `06b72451c`'s code, where no hook script stands and `lib/routing.py` has no `open_declarations` (executed): the hook's module failed at collection on the missing file, and the six cases of `Test_open_declarations` then present failed with `AttributeError`. Each case was then shown red with only the guard it names broken, through `seal mutate` over the committed file, below. S1's and S9's cases read the paragraph's first and last lines from the tree's own `docs/running/the-run.md`.

S7's case for an input with no question list is held by two guards, the shape test of `_questions` and the `__main__` block's catch. `seal mutate` breaking either alone survived (rows H11 and H12), as `frame/design.md` S7 says it would. A probe, `test_tmp_both_guards.py` in this phase's scratch, run once, copied the hook with both removed and ran the case's three inputs (executed). The input `{}` exited 1 with `TypeError: 'NoneType' object is not iterable` on stderr, which the case's `start` refuses. The input with a question holding no `question` still printed nothing, through the per-question half of the shape test the probe left in place.

S8 was shown red by removing the `PreToolUse` entry from `hooks/hooks.json` (row S8). S11 is a search, not a case: at `06b72451c` it printed 36 lines, and at `752164072` it prints `docs/running/measuring-a-run.md:140` and `:143` alone (executed).

### Mutation runs

Each row is one `seal mutate` run over a committed file (executed). The `R` rows break `lib/routing.py` and run `bin/test tests/lib/test_routing.py -q -p no:xdist -k <case>`; the `H` rows break `hooks/ask-under-automation.py` and run `bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist -k <case>`. R1 to R6 ran at `fea9cbf9e`, and every other row at `52da56cb1`, the commit that adds R6b's case.

| # | Break | Case | Verdict and failing line |
|---|---|---|---|
| R1 | the branch test dropped: `if real not in seen:` | `test_refuses_a_branch_no_worktree_has_checked_out` (S5) | red: `assert [(…'branch': 'feature/released'…)] == []` |
| R2 | the reading narrowed to `cwd`'s branch: `checked_out = {current_branch(cwd)}` | `test_accepts_a_linked_worktrees_declaration_once_in_shared_mode` (S6) | red: `assert [] == [<linked>/seal/threads/…/routing.md]` |
| R3 | the real-path dedupe dropped | `test_accepts_a_local_roots_declaration_once_from_two_worktrees` (S6) | red: the left side holds the local root's `routing.md` twice |
| R4 | `except gitcmd.Failed:` read as `except ValueError:` | `test_refuses_to_raise_where_git_is_not_on_path` (S7) | red: `gitcmd.Unrun: git worktree list --porcelain could not be run: git is not on PATH` |
| R5 | the empty-`cwd` guard dropped | `test_refuses_a_repository_with_no_root_and_a_directory_outside_git` | red: the call with `""` answered this repository's own open work item. The red needs a run from a checkout whose branch an open declaration names, which this one is |
| R6 | the non-zero exit guard dropped | every case of `Test_open_declarations` then present | SURVIVED, so the case of the next row was written |
| R6b | the same break | `test_refuses_a_listing_from_a_git_that_exited_non_zero` | red: `assert [(…)] == []` |
| H1 | every question read as not stating why: `unstated = list(questions)` | `test_accepts_a_call_whose_every_question_states_why` (S2) | red: the deny object printed where `""` was expected |
| H2 | the first question read alone: `questions[:1]` | `test_refuses_a_call_one_of_whose_questions_does_not_state_why` (S3) | red: nothing printed, `JSONDecodeError` in `refused` |
| H3 | the near-spelling sentence dropped: `if False:` | `test_refuses_a_marker_in_another_case_and_names_it_as_not_read` (S4) | red: the assertion on `"Near" holds \`no default:\`, which this hook does not read` |
| H4 | the same-line rule loosened to `\s*\S` | `test_refuses_a_marker_with_nothing_after_it_on_its_line` | red: nothing printed, `JSONDecodeError` in `refused` |
| H5 | `LEAD` dropped from the fallback sentence | `test_refuses_with_the_coordinate_where_the_paragraph_is_gone` (S9) | red: `assert said in reason`, the fallback sentence |
| H6 | `CLAUDE_PLUGIN_ROOT` ignored: `root = OWN_ROOT` | the same case (S9) | red: `assert said in reason`, since the tree's own paragraph was printed in the fallback's place |
| H7 | the open work items dropped from the reason | `test_refuses_a_question_under_automation_yes_with_the_rule` (S1) | red: `assert ITEM in reason and BRANCH in reason` |
| H8 | the `yes` filter dropped: `if True` | `test_accepts_a_tree_where_no_open_work_item_reads_yes` (S5) | red: the tree whose row reads `no` printed a deny object |
| H9 | the `__main__` catch read as `except ZeroDivisionError:` | `test_accepts_a_payload_that_is_not_json_and_prints_nothing` (S7) | red: exit 1 with a `JSONDecodeError` traceback |
| H10 | the paragraph not found: `if False:` for the `LEAD` test | `test_refuses_a_question_under_automation_yes_with_the_rule` (S1) | red: `assert lines[0] in reason and lines[-1] in reason` |
| H11 | the list half of the shape test dropped | `test_accepts_a_payload_with_no_question_list_and_prints_nothing` (S7) | SURVIVED: the catch still prints nothing. The probe above shows both removed |
| H12 | the `__main__` catch, as H9 | the same case (S7) | SURVIVED: the shape test still prints nothing |
| S8 | the `PreToolUse` entry removed from `hooks/hooks.json` | `test_the_plugin_registers_its_hooks_and_writes_none_into_git` | red: `assert ['SessionStart', 'Stop'] == ['PreToolUse', …]` |
| S8b | the matcher read as `Bash` | the same case | red: `('PreToolUse', {'matcher': 'Bash', …})` |
| F1 | `` `hooks/ask-under-automation.py` `` removed from `README.md`'s list | `test_both_readmes_say_what_the_stamp_hook_writes_and_leaves` | red: `('README.md', '`hooks/ask-under-automation.py`')` |
| F2 | the same, in `README.ko.md` | the same case | red: `('README.ko.md', '`hooks/ask-under-automation.py`')` |

A first break of `README.ko.md`, renaming the list item's `` `PreToolUse` `` label, survived: the section names `` `PreToolUse` `` in two other sentences, which hold the fact as `README_FACTS` reads it.

### The boundary run

One `bin/test ... -q` over 34 paths passed 4,381 cases and skipped 10, at `752164072` with `gaps.md` on disk (executed). The paths hold the eight modules `frame/plan.md`'s phase 1 row names, five of them through `tests/behaviour`, and every other test file that loads a module importing `lib/routing.py` or names a file this phase changed (`git grep -l` over `tests/*.py` for `routing.py`, `import routing`, `chain_check`, `seal_stamp`, `pr_body`, `settle.py`, `unverified_check`, `launch.py`, `core-start`, `hooks.json` and `ask-under-automation`, with `tests/conftest.py`, `tests/censuses.py` and `tests/run_tests.py` left out as no test files), `tests/skills/test_session_cost.py`, and `tests/text` and `tests/behaviour`. The first run, at `52da56cb1`, failed `tests/behaviour/test_docs_line_wrap.py` on `README.ko.md:381`, a line this phase's edit had joined to the next; `8523bdc0f` rewrapped it. The plan's two searches print what its *Verified by* cell expects at `752164072` (executed): the count search prints `docs/running/measuring-a-run.md:140` and `:143` alone, and `git grep -n -i -E 'decides anything on it' -- . ':!seal/threads' ':!skills/implement/orchestration.md'` prints nothing.

### For phase 2

- `hooks/ask-under-automation.py#MARKER` and `#LEAD` are the names *Scope* item 7's first passage cites. The hook's `MARKER` comment says a document that states the form cites `hooks/ask-under-automation.py#MARKER`.
- `skills/implement/orchestration.md:289` is the one line the S10 search still prints.
