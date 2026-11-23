# Implementation Plan: 1795432997-cases-copy-facts-whose-source-is-code

## Technical context

The tree as read at `f885ba546`.

The work changes test modules, `tests/conftest.py`, `tests/workflows.py`, one comment of `skills/settle/scripts/passages.py`, `evals/scripts/behaviour.py`, one sentence of `CONTRIBUTING.md` and one comment of `tests/requirements.txt`. No shipped gate changes what it reads or prints.

The shared `section` builds on `lib/lines.py#readable`, `#headings`, `#sections` and `#heading_level` (`frame/design.md` G8), loaded once in `tests/conftest.py` through `load_lib_module` (`:448`), which already loads `lib/optin.py` at module level (`:459`). `tests/workflows.py` imports PyYAML at its top, so `tests/conftest.py` stays importable without it (`tests/workflows.py:20-22`), and `parse` goes there for that reason.

The cases that read code constants load the module the way that module's own test file does: `lib/routing.py` through `load_lib_module`, `pr_wait.py` as `tests/skills/test_pr_wait.py:24` does, and `chain_check.py` and `broad_gate.py` through the loaders their test files use.

**Failure scenario of the chosen approach, six months on.** A case written after this work cuts a section with `text.split(heading, 1)` inline, because the inline cuts stay (`frame/design.md` *Scope* **Out**), and the next audit finds a second generation of hand readers. The shared `section` is one import away and its docstring names the fence rule, but nothing refuses an inline cut. A second risk is a constant renamed in `lib/routing.py` or `pr_wait.py`: the text case then fails at import or at an attribute, where it used to fail at an assertion naming the document. That failure names the code, which is the source, so a reader fixes the right file.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1a. The shared `section` stops at the next heading of its level or above | A case that leaned on running past a higher heading, as `test_first_setup_asks_once.py#section` could, reads less text | **Chosen.** It is how a renderer bounds a section, `tests/skills/test_coordinates.py`'s kernel and two of the old helpers already stop so, and S9 names any call whose text changes |
| A1b. It stops at the next heading of the same level only | A `###` section runs past the `##` that closes its parent, into the next chapter, and a pin finds its phrase there | Rejected |
| A1c. It stops at the next `## ` | A `###` section is cut at its first sibling only if that sibling is `##`, so it swallows its `###` siblings | Rejected |
| A2a. `section` returns the body without its heading line | A caller that printed the heading in a message prints it from its own argument | **Chosen.** A phrase pinned in the body is never satisfied by the heading itself, as `test_the_agent_contract_holds_the_universal_rules.py#spans` already guards |
| A2b. It returns the heading with the body | A pin on a word the heading holds passes with the body silent | Rejected |
| A3a. `heading` is the whole heading line, `## Name` | A caller must know the level it reads | **Chosen.** `lib/lines.py#sections` compares whole lines, and the level then decides the stop with no second argument |
| A3b. `heading` is the text, at any level, as `test_the_rules_claude_md_names_have_one_home.py#section` takes it | Two headings of one text at two levels both match, and the helper picks one silently or refuses a file that is correct | Rejected |
| A4a. Keep each module's `section` and make it a one-line wrapper over a shared core | Ten names for one reading stay, and a module adds its own stop rule back inside its wrapper | Rejected: *Done when* asks that no module define one, and the premise for keeping them, that each reads a different shape, does not hold (`frame/design.md` G9) |
| A4b. One `section` in `tests/conftest.py` | A call whose old helper read more or less text now reads the shared amount | **Chosen**, with S9 recording each such call |
| A5a. Row 18 of `RULES` goes, and the derivation of 806,241 stands in git and in #945's record | A person changing the threshold finds its grounds with `git log -S'806,241'` rather than in the tree, and this release's notes carry #1579's sentence that the comment held it, which this work's changelog entry corrects | **Chosen.** The number is a measurement no code reads (`frame/design.md` G13), the case pins only that the document spells it, and history goes to git (`skills/core/SKILL.md` *The rule a mechanism is kept against*) |
| A5b. Keep row 18 | The case stays a stored copy of a measured number: an edit to the threshold fails the suite and is fixed by editing the case to match, which catches nothing | Rejected |
| A5c. Move the derivation back beside the number in `skills/code-review/orchestration.md` | Reverses #1579, which moved it out in this release because the orchestrator never acts on it | Rejected: a decision those rounds made is not reargued here |
| A6a. The routing answers come from `lib/routing.py`'s constants | A new axis's answers reach the case only where the case names its tuple | **Chosen.** The constants are the source, and the case keeps its stated reason for leaving `crafter` out |
| A6b. Keep the text read of `lib/routing.py` for `'"{answer}"'` | A constant built from parts, or renamed, fails the grep while the parser accepts the answer, and the reverse | Rejected: it reads code as text where the module can be loaded |
| A7a. Remove `test_review_axes.py`'s routing case and keep the waiver module's | A reader of the review-axes module no longer finds the routing answers there | **Chosen.** The waiver module's `# No TARGET` line names it the home of the routing rule, and it holds each of that case's facts (`frame/design.md` G12) |
| A7b. Remove the waiver module's cases and keep `test_review_axes.py`'s | The routing rule's home loses its cases of the vocabulary to a module about review rounds | Rejected |
| A8a. The `check:` case asserts one line, and `seal rules --check` resolves its targets | A target swapped for another file that exists stays green, as for every other rule | **Chosen.** Whether a target holds its rule is review's (`frame/design.md` G14) |
| A8b. Keep `WRITING_RULE_CHECKS` | Every change to the line's targets fails the suite and is fixed by copying the new line into the case, which catches nothing | Rejected |
| A9a. The moved-rule window cases go, and the paste test holds the pairs | A contract rule pasted into a definition inside a fenced block is not caught, since `passages.py#words` drops fences | **Chosen.** The paste test reads every pair the moved-rule cases read (`frame/design.md` G15), and a paste inside a fence was never the measured failure |
| A9b. Keep the moved-rule structure and point it at `passages.py`'s functions | Two cases name every paste of a contract rule into a definition, and one of them parametrises every rule by every definition, pairs the other already reads | Rejected: the premise for keeping it, that it reads pairs the paste test does not, does not hold |
| A10a. The measurement that chose `WINDOW` moves to the comment over `passages.py#WINDOW` | The code's comment holds history a reader of the code does not act on | **Chosen.** It is the grounds of the number in the file that holds the number, which no agent preloads; three docstrings cite it rather than state it |
| A10b. The measurement goes to git with the cases | The number 15 stands with no grounds in the tree, and a person moving it re-measures blind | Rejected |
| A11a. `tests/workflows.py` gains `parse`, and eval YAML reads through it | The module's name says workflows while it also reads eval files | **Chosen.** It is already the suite's one YAML reader, with the `BaseLoader` reasoning in its docstring; its docstring and `CONTRIBUTING.md:88` name what it reads |
| A11b. A new module for eval YAML | Two modules spell the loader and the reason for `BaseLoader` | Rejected |
| A11c. Each case calls `yaml.load` itself | The `BaseLoader` choice is made again in each case, and one `safe_load` turns `0` into an integer | Rejected |
| A12a. The cases that cut a section inline stay, out of scope | A later case copies an inline cut (Technical context) | **Chosen.** They define no helper, and the issue's *Done when* bounds the class to definitions, as #1575 bounded its inline joins (`seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/frame/design.md` *Scope* **Out**) |
| A12b. Convert every inline cut too | The diff reaches many more modules, several of them #1581's, and each conversion is a reading a round must judge, while #1581 waits on this item | Rejected for this item; the orchestrator files it as an issue |
| A13a. The sealer grader's `input_match` is compiled and must find `seal gate --base` | A broader pattern, such as `seal`, also passes, which still bounds the gate at zero | **Chosen.** It reads what the grader does, not how its YAML spells it (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*) |
| A13b. The parsed `input_match` must equal `seal\s+gate\s+--base` | A grader that bounds the same command in another spelling is named a gap | Rejected |
| A14a. The `Broad gate` refusal goes | A generator change that writes a `Broad gate` grader again passes the layout case | **Chosen.** The sealer stopped writing the cell at 0.22.0, and the generator is the one writer of the sealer cases (`frame/design.md` G16) |
| A14b. Keep it | A refusal of a form no writer produces costs a branch and a docstring paragraph and has caught nothing since 0.22.0 | Rejected |
| A15a. `tests/evals/test_behaviour.py` keeps its `TARGET` and census line with no class | The layout report names `behaviour.py`'s public functions without classes, as it already does | **Chosen.** The census over `evals/scripts/behaviour.py` keeps running |
| A15b. Delete the file | No census runs over `evals/scripts/behaviour.py` | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3 and 4, with item 11 for what they remove | `bin/test -q tests/test_conftest.py tests/text tests/behaviour tests/skills/test_coordinates.py tests/skills/test_broad_gate.py tests/github/test_issue_claims_check.py tests/lib/test_fields.py` passes, and so does `bin/test -q "tests/skills/test_chain_check.py::Test_rule_changes_read::test_refuses_a_section_the_parser_refuses_at_its_line"`, the one case that read `#template_section`, a reading over `tests/conftest.py#section` since phase 1; each case of `Test_section` is seen red with only its guard removed; S1, S2, S3 and S9 hold | `d685ae9cb` |
| 2 | `frame/design.md` *Scope* items 5, 6, 7 and 8, with item 11 for what they remove | `bin/test -q tests/text tests/behaviour tests/skills/test_passages.py` passes; S6, S7 and S8 hold | `d5b667723` |
| 3 | `frame/design.md` *Scope* items 9, 10, 11 and 12 | `bin/test -q tests/test_workflows.py tests/behaviour/test_evals_layout.py tests/evals` passes; the cases of `parse` are seen red, and `sealer_grade_gaps`'s rewritten cases are seen red with the guard each names removed; S4 and S5 hold | |

The searches are those of `frame/design.md` *User scenarios & acceptance*. A rewritten case keeps the fact it held, and where its reading changed the phase record says how (S9). A case is cut only with the case or fact that holds it now named in `frame/design.md` *Removes* or in the phase record. The broad gate is the orchestrator's, after the rounds settle (contract rule 2); every phase hands the suite over as `unverified`.

## Overlap with the release

The spawn names #1581 and #1596. #1596's frame was read at `e36796bb8` on branch `fix/1596-a-records-only-commit-after-the-gate-owes-the-whole-broad-run`, its *Scope*, *Phases* and *Overlap with the release* (executed: `git show e36796bb8:<path>`); none of its phases is closed. #1581 is not started, and its issue was read (executed: `gh issue view 1581`).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1596, a records-only commit after the gate owes the whole broad run | `tests/skills/test_chain_check.py`: this work replaces `#template_section` (`:1461-1469` at `f885ba546`) with a reading over `tests/conftest.py#section`, among the rule-change cases, and #1596's *Scope* item 8 adds a case to *Test_broad_gate*. #1596's *Scope* items 3 to 5 edit `skills/code-review/orchestration.md`, `skills/code-review/gate-to-pull-request.md` and `skills/implement/orchestration.md`, which this work's rewritten cases in `tests/text/test_broad_gate_rule.py`, `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` and `tests/text/test_the_rules_have_one_owner.py` read. This work's S1 and S2 read every test module, the one #1596 adds a case to among them. #1596 changes no code of `chain_check.py`, whose `TRAILER`, `NO_WORK_ITEM`, `FIXED` and `REJECTED` this work reads | #1596 | Both frames give this order. #1596's diff is the smaller and likelier sealed first, and this item's searches read the content #1596 adds, so this item merges the base after it and runs them over that content inside rounds it spends anyway. The two edits to `test_chain_check.py` stand in different classes. #1596's case defines no helper |
| #1581, six test modules cost past 60 s | `tests/skills/test_broad_gate.py`: this work renames `#flat` (`:498`) and changes its import in `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:24`. `tests/skills/test_chain_check.py`: this work replaces `#template_section` with a reading over `tests/conftest.py#section`. #1581 rewrites both modules from the code | #1580 | `routing.md` *Why this way* orders #1581 after this item. #1581 writes the two modules anew and reads their old cases for inputs (`CONTRIBUTING.md` *The test layout*), so it starts from the shared `section` and the renamed helper, and no rewrite of it is redone here |

## Operational impact

None for a deployer. No dependency is added: PyYAML 6.0.3 is already pinned in `tests/requirements.txt` and imported by `tests/workflows.py`. `evals/scripts/behaviour.py` loses two functions no code outside `tests/` calls (`frame/design.md` G17). The version is not moved; #1571 moved it to 0.38.6.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
