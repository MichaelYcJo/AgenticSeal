# Phase 3: 1795432997-cases-copy-facts-whose-source-is-code

## What this phase found

**The frame holds for this phase, with one fact it did not state.** At `aeae21ac0`, the lines S4 searches for were the hand readers and the `Broad gate` refusal of `tests/behaviour/test_evals_layout.py`, and the lines S5 searches for were `scalar`, `grader_from` and `SCALAR` with their cases (read, in the files G16 and G17 name; neither search was run at that commit). `tests/evals/test_rule_cases.py` called `grader_from` at `:80` and `:191`, as G17 says. `seal/follow-up.md` holds two rows, and neither waits on this phase (G18). The fact the frame did not state: a committed sealer grader names its file as `target: {source: 'file', path: ...}`, not as a top-level `path:`. The old regular expression `path: '[^']*/guarantee\.md'` matched it inside the flow map. The two fixtures of the layout module wrote a top-level `path:`, which the regular expression matched as well. `sealer_grade_gaps` now reads `target.path`, the field the runner reads, and the fixtures write the target as `evals/scripts/behaviour.py#report_regex` does. This was judged against `frame/design.md` *Scope* item 9, which reads a grader by what it does.

**The parser reads what the hand readers read, over every committed file.** The probe `phase-3/test_tmp_parser_equals_hand_readers.py`, under this work item's scratch directory, ran once at `aeae21ac0` (executed: 2 passed). Over the 25 `case.yaml` files, `top_level_keys`, `block_keys` of `execution` and `context`, and the `scaffold_script` match each equal what `yaml.BaseLoader` gives. Over the 172 grader files, `split("---")[1]` cuts the same front matter as the line cut, and `grader_from`'s type and config equal the parsed fields, with integers read as their strings and `match` as `contains` where a file names none. So no case of the tree reads other values after the rewrite, and no call needs a row like phase 1's S9 table.

**Decisions settled while writing the code.** Each was judged against `frame/design.md` *Scope* item 9 and *Data & interfaces*, and `CONTRIBUTING.md` *The test layout*. That section says a helper two test files use is defined once.

- `tests/workflows.py` gains `front_matter(text)` beside `parse`, a function the frame does not name. *Data & interfaces* defines a grader's front matter as the text between its first two `---` lines. The layout module and `tests/evals/test_rule_cases.py` both cut it, so the cut is defined once. It cuts by lines, so a pattern holding `---` stays whole, which `split("---")` did not do. It raises `ValueError` where the text does not open and close a front matter, as `grader_from` did.
- `Test_parse` holds two cases. The second, `test_refuses_a_text_of_two_documents_such_as_a_whole_grader_file`, came from `seal layout --check`, whose first boundary run refused `tests/test_workflows.py: class Test_parse has no test_refuses_ case`. A whole grader file is two YAML documents, and `parse` reads one.
- `sealer_grade_gaps` reads a grader's `input_match` as a regular expression and asks that it find `seal gate --base`, as `frame/plan.md` A13a chose. `test_a_bound_on_the_sealers_run_in_another_spelling_is_no_gap` holds that a pattern of another spelling passes. Its first build also asked `"input_match" in g`. That guard survived its break: `tool` is read first, and every grader whose tool is `Bash` names an `input_match`. `711266845` took it out. A `Bash` grader with no `input_match` now raises `KeyError` in the layout case, and no committed grader is one.
- `test_a_verdict_grader_that_reads_no_block_is_a_gap` is renamed `test_a_verdict_grader_that_reads_no_block_of_the_guarantee_is_a_gap`. It now changes the block, the file and the verdict line one at a time, as the bound case changes its three fields. Both cases build their case through `sealer_case`, whose two graders `VERDICT_GRADER` and `BOUND_GRADER` stand once.
- `case_graders` of `tests/evals/test_rule_cases.py` reads a grader with no `match` as `contains`, the runner's default, which `grader_from` supplied until now.
- `tests/evals/test_behaviour.py` keeps `TARGET` and its census line. The phase built it with no class, as the frame then chose (now `frame/plan.md` A15c, rejected), on the premise that only the reader left with `Test_grader_from`. That premise was false. The removed `Test_grader_from::test_accepts_what_behaviour_writes_field_for_field` also held the writer, `report_regex` through `grader` and `squote`, which `evals/scripts/rule_cases.py` calls. No case held the writer's doubling of a quote after the phase: `Test_parse` reads a hand-typed spelling, and no committed grader holds a doubled quote. Round 1's finding 1 showed it, and its fix pass added `Test_report_regex` (`trail/rounds/round-1.md`).

**Item 11: the prose that stood on what this phase removed.** `git grep` on `grader_from`, `scalar(`, `SCALAR`, `top_level_keys`, `block_keys`, `Test_scalar`, `Test_grader_from`, `behaviour_for_rule_cases`, `reader of a grader`, `YAML parser`, `PyYAML` and `Broad gate` outside `seal/threads/` (executed). Each sentence rewritten:

| File | What it said | What it says now |
|---|---|---|
| `CONTRIBUTING.md` *Running the checks* | the YAML parser reads a workflow file | it reads a workflow file, an eval case's `case.yaml` and a grader's front matter |
| `tests/requirements.txt`, the PyYAML comment | the same | the same three |
| `tests/workflows.py`, docstring | the suite's one reading of a workflow file | its one reading of a YAML text, through `parse`, with `front_matter` for a grader |
| `tests/test_workflows.py`, docstring | `load`'s two properties | the same, and where a front matter ends |
| `tests/evals/test_rule_cases.py`, docstring and two helper docstrings | a grader is read back through `grader_from`, "as a side records them" | it is read back through `front_matter`, from its front matter |
| `evals/scripts/behaviour.py`, docstring | `grader_from` reads a grader back | the sentence goes |
| `tests/behaviour/test_evals_layout.py`, `BLOCK_PATTERN`'s comment, `sealer_grade_gaps`'s and `test_every_sealer_case_grades_the_guarantee`'s docstrings | the pattern as the YAML spells it; the `Broad gate` refusal | the pattern as a regular expression spells it; the parsed fields a grader is judged by |

The two hits of `Broad gate` that remain, at `skills/verify/scripts/broad_gate.py:36` and `:549`, name the configuration key, not a grader. That list is a sample (contract rule 12): it is the spellings searched. A sentence that paraphrases a removed reader without naming it is not reached. It stands in the tree's other prose, which the review rounds read.

**Seen red, and `seal mutate`.** The three cases of `Test_parse` and `Test_front_matter` that `d7c573076` holds were run before `parse` and `front_matter` existed. Each of their five runs, the refusal case's three parameters among them, failed with `AttributeError: module 'workflows' has no attribute ...` (executed). `test_a_bound_on_the_sealers_run_in_another_spelling_is_no_gap` was run against the old reader. It failed on its first spelling, `seal gate --base`, with the gap named (executed). Each break below ran with `-p no:xdist`, one break per run, and each failing line was read for the guard it names. Logs are under `phase-3/mutate/`.

| Break | Verdict, and the case that went red |
|---|---|
| `parse` with `yaml.SafeLoader` | red: `Test_parse`'s accepting case, on `{'max': 0} != {'max': '0'}` |
| `parse` through `next(yaml.load_all(...))` | red: the two-document case, `DID NOT RAISE YAMLError` |
| `front_matter` without its opening check | red: the refusal case's `no opening rule` |
| `front_matter` without its closing check | red: the `no closing rule` case, on the message `'---' is not in list` |
| `front_matter` cut by `text.split("---")[1]` | red: the accepting case, on a scanner error at `'a` |
| `sealer_grade_gaps`: `.endswith(".md")` for `/guarantee.md` | red: the verdict case's file change |
| without `BLOCK_PATTERN in` the pattern | red: the verdict case's block change |
| without `"Verdict: " in` the pattern | red: the verdict case's verdict-line change |
| the tool check read as `True` | red: the bound case's `tool: 'Write'` |
| without the `input_match` search | red: the bound case's `--preflight` |
| the search read as equality with `seal\s+gate\s+--base` | red: the other-spelling case |
| without `max == "0"` | red: the bound case's `max: 1` |
| `"input_match" in g` read as `True` | SURVIVED, exit 1; the guard went (above) |
| `test_a_tool_used_grader_bounded_at_zero_can_pass` without the `min` check | red, on every committed `max: 0` grader |
| `bound_gaps` reading `execution` from the top level | red: `test_every_case_sets_its_bounds_where_the_runner_reads_them` |
| `scaffold_gaps` comparing the mapping with a list | red: `test_every_scaffold_is_a_file_beside_its_case` |
| `scaffold_gaps` reading the key `scaffold` | red: the same case |
| `case_graders` defaulting `match` to `regex` | red: `Test_proofer_case`'s `'regex' == 'contains'` |
| `test_a_tool_used_grader_bounded_at_zero_can_pass`'s `max == "0"` read as `max == 0` | SURVIVED |
| the `context` check of `scaffold_gaps` read as `False` | SURVIVED |
| the scaffold path fixed to `scaffold.sh` | SURVIVED |

The last three are guards whose only case reads the tree, and the tree holds no file that breaks them. No case held them before this phase either: the old readers' `^max: 0$`, the `context` comparison and the path read by `re.search` stood with no fixture behind them. `gaps.md` `## Not done` records them.

The two-document break ran with `711266845`'s case uncommitted. The file it broke, `tests/workflows.py`, was as `d7c573076` committed it, and `seal mutate` restored it from its own copy. After the last run, `git status` showed no change under `tests/` or `evals/` (executed).

**The census.** At `711266845`, S4 and S5 print nothing, each `git grep` exiting 1 (executed). Outside `seal/threads/`, `git grep` for `grader_from`, `top_level_keys`, `block_keys`, `Test_scalar`, `Test_grader_from` and `behaviour_for_rule_cases` prints nothing (executed). `bin/seal layout --check tests` exits 0 (executed).

**The boundary run took two commands.** The first command's set came from `git grep` with the pathspec `tests/**/*.py`. That pathspec does not reach the test files directly under `tests/`. It ran `tests/text`, `tests/behaviour`, `tests/test_workflows.py`, `tests/evals`, and every other module that search listed for naming `workflows`, `evals`, `requirements.txt` or `CONTRIBUTING` (executed: 2454 passed, 10 skipped, at `711266845`). Its first run, at `d7c573076`, failed on the layout refusal above. The second command ran the two files directly under `tests/` that the first missed, `tests/test_run_tests.py` and `tests/test_censuses.py` (executed: 296 passed). Every test file under `tests/` declares a `TARGET` outside `tests/text/` and `tests/behaviour/`, so those two directories hold the tree-wide files. `uvx ruff check` and `uvx ruff format --check` over the six changed Python files exit 0 (executed).

**A comment wrap after the record's first commit.** Reading the range whole found that the rewritten PyYAML comment of `tests/requirements.txt` ran its last sentence onto one long line. `730d99f79` wraps it, a change to a comment alone. The four modules that read the file, `tests/test_run_tests.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py`, `tests/behaviour/test_the_release_seal_is_drawn.py` and `tests/github/test_publish_release_note.py`, pass over it (executed: 158 passed).
