# Phase 1: 1793853197-a-bare-commit-goes-or-states-its-reason

## What this phase found

**The frame holds for this phase.** The phase was built on `665eef15c`, whose tree outside `seal/` is `31558c76`'s. M1 and M2 of `frame/design.md` *Grounding*, run there in this clone, gave the frame's figures: 6,500 distinct hex tokens, 49 that resolve as commits, and 45 short mixed tokens that do not (executed). The two lists together are the 61 tokens of D1, and `git grep -nP '\b(<the 61 tokens>)\b' -- . ':(exclude)seal/'` printed 115 lines in 46 files, each at the line D1 names (executed). No sibling of 0.32.4 had landed on `release/v0.32.4`, so no line had moved. Each sentence a rewrite touched was read whole at its line, with the paragraph around it (read).

**Each of the 115 lines, at `31558c76`.** "removed" means the clause or sentence holding the token went, and the text around it stands as it was, rewrapped where a line broke short. Rows 1 to 85 are D1 rows 1 to 40, and rows 86 to 115 are D1 rows 41 to 46.

| # | Line | Token | Disposition | What replaced it |
|---|---|---|---|---|
| 1 | `.github/workflows/test.yml:78` | `5623d728` | P | "because every leg collects the same cases, so group k of a count holds the same cases on both." The count, commit and run id went |
| 2 | `skills/implement/scripts/seal.py:1216` | `8fb1fb5` | P | removed: "(measured at `8fb1fb5`)". The sentence ends "with both guards off." |
| 3 | `skills/implement/scripts/seal.py:2191` | `55aea15d` | P | removed: "(the sealer, at `55aea15d`)". Git's quoted refusal ends the sentence |
| 4 | `tests/skills/test_seal.py:3330` | `55aea15d` | P | "`install` stages the file, and git refuses a plain `git rm` of a file staged and never committed." |
| 5 | `tests/behaviour/test_a_release_publishes_its_note.py:122` | `4134055a` | P | "#1117's against the workflow that fired on the tag alone." |
| 6 | `tests/behaviour/test_chain_hooks_hardening.py:91` | `5287dd42` | P | removed: the docstring ends "and no row names anything else." |
| 7 | `tests/behaviour/test_chain_hooks_hardening.py:282` | `5623d728` | P | removed: the docstring ends "says a diff git could not take is asked about." |
| 8 | `tests/behaviour/test_first_setup_asks_once.py:15` | `7e44106` | P | removed: the paragraph at lines 15 to 17, with "the output is in the body of the commit that added this file" |
| 9 | `tests/behaviour/test_first_setup_asks_once.py:142` | `81888e2` | P | removed: the comment paragraph at lines 141 to 143 and the empty comment line above it |
| 10 | `tests/behaviour/test_first_setup_asks_once.py:668` | `589cf25` | P | removed: "and the cases that read it were written against the block as it stood at 589cf25, each failing first". The sentence ends "said so in every project on the machine." |
| 11 | `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:21` | `0e676e6` | P | removed: the paragraph at lines 21 to 23 |
| 12 | `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:337` | `4edc5de6` | N | "Every line of each shape in `COMMENT_SHAPES` is a place a reading of fences or comments has had to be right." The section header at line 335 reads "the comment shapes" for "the frame's shapes" |
| 13 | `tests/block_shapes.py:12` | `4edc5de6` | N | "Most shapes are an earlier reader's test strings, taken verbatim, because each is a place an earlier attempt at these readers was wrong." |
| 14 | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:69` | `2759a60d` | P | removed: "red against 2759a60d's sealer step". The sentence ends "never by an edit of the row." |
| 15 | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:179` | `1e956838` | P | removed: the sentence at lines 178 and 179. The docstring already says the paragraph names none of the guards the removed `post-commit` record had |
| 16 | `tests/github/test_publish_release_note.py:38` | `8a1173c8` | P | removed: the paragraph at lines 35 to 41 |
| 17 | `tests/github/test_publish_release_note.py:40` | `c55c3083b` | P | removed with row 16's paragraph |
| 18 | `tests/github/test_publish_release_note.py:1185` | `4134055a` | P | removed: the docstring ends "names no pull request (#1139)." |
| 19 | `tests/github/test_release_seal.py:614` | `e01e1b12` | P | removed: the docstring ends "capped is read from the labels alone." |
| 20 | `tests/github/test_release_seal.py:640` | `7966a9f9` | P | removed: the docstring ends "and the log names it." |
| 21 | `tests/github/test_release_seal.py:659` | `7966a9f9` | P | removed: the docstring ends "and the log names the record." |
| 22 | `tests/github/test_roll_flow_measurement_issue.py:586` | `0d59003` | N | "A `gh issue create` failure after a successful close whose message names only the failed create call says nothing of the old issue being closed already, and an operator debugging a red release-workflow step has to check separately whether it is still open." |
| 23 | `tests/hooks/test_config.py:870` | `4dfb3d0d` | P | removed: the docstring ends "The walk reads no row and refuses." |
| 24 | `tests/hooks/test_config.py:1027` | `4dfb3d0d` | P | removed: the docstring ends "does not double the config's `Mode` row." |
| 25 | `tests/hooks/test_config.py:1040` | `4dfb3d0d` | P | removed: the docstring ends "so the count goes on past it." |
| 26 | `tests/hooks/test_config.py:1368` | `977b6613` | P | removed: the docstring ends "and nothing is refused." |
| 27 | `tests/hooks/test_config.py:1859` | `4dfb3d0d` | P | removed: the docstring ends "names one signer and the refusal." |
| 28 | `tests/hooks/test_config.py:1878` | `4dfb3d0d` | P | removed: the docstring ends "and is refused." |
| 29 | `tests/hooks/test_dispatch.py:281` | `551c7967` | N | "Shapes a gate can print that `classify` and `merge` read without raising. Both read them after the gates have run and outside `run_gate`'s isolation, where a raise would end the whole group with exit 1." |
| 30 | `tests/hooks/test_dispatch.py:424` | `02e47435` | P | removed: the docstring ends "was read as absent." |
| 31 | `tests/hooks/test_routing.py:493` | `126ee7b5` | N | "A record that is an empty file names no branch, so it lets nothing through, and a run on a branch adds that branch as its first line." |
| 32 | `tests/skills/test_arm_check.py:669` | `346b4af7` | P | "On Python 3.14, before the tables held them, it named `Interpolation` and `TemplateStr`." |
| 33 | `tests/skills/test_arm_check.py:701` | `346b4af7` | P | "Red how: on Python 3.14 with no `ONLY_ON_SOME_PYTHONS`, naming the five aliases." |
| 34 | `tests/skills/test_arm_check.py:998` | `346b4af7` | P | "Red how: on Python 3.14 with both in neither table, `UnknownNodeType` naming `TemplateStr`." |
| 35 | `tests/skills/test_arm_check.py:1010` | `346b4af7` | P | "Red how: on Python 3.14 with `Interpolation` in neither table, refused." |
| 36 | `tests/skills/test_arm_check.py:1415` | `a340221b` | P | "Red how: against a script whose `clear_bytecode_cache` does not take `cwd`, the relative parameter's runs see the planted cache." |
| 37 | `tests/skills/test_arm_check.py:1615` | `a340221b` | P | "Red how: against the script without the first run, both arms are filed as no verdict after four 0.3s waits and nothing is raised" |
| 38 | `tests/skills/test_arm_check.py:1694` | `a340221b` | P | "Red how: against the script without the first run there are four calls and the first sees a mutation" |
| 39 | `tests/skills/test_arm_check.py:1730` | `6bbaa4d1` | P | "Red how: with the pair's output decoded strictly, `UnicodeDecodeError` leaves `run_arms`." |
| 40 | `tests/skills/test_arm_check.py:2316` | `a340221b` | P | "Red how: against the script without the first run, every shape prints `killed` beside both arms and exits 0." |
| 41 | `tests/skills/test_arm_check.py:2390` | `a340221b` | P | "Red how: against the script without the first run, both arms land in the no-verdict list at exit 0." |
| 42 | `tests/skills/test_arm_check.py:2424` | `a340221b` | N | "Every other run ends with the module put back from the bytes held, and a refusal must not be the one path that keeps the cases' version instead" |
| 43 | `tests/skills/test_arm_check.py:2434` | `6bbaa4d1` | N | "at exit 1, where a refusal exits 2." |
| 44 | `tests/skills/test_arm_check.py:2436` | `6bbaa4d1` | P | "Red how: with the refusal leaving the module unrestored, the module is left as the command changed it, and the line says *Nothing was written*" |
| 45 | `tests/skills/test_arm_check.py:2437` | `dc1b0d14` | P | "with the put-back's error raised out of the `finally`, the locked module is a `PermissionError` traceback and no line." |
| 46 | `tests/skills/test_arm_check.py:2542` | `6bbaa4d1` | P | "Red how: without the entry block, the refusal line is followed by a traceback and exit 1." |
| 47 | `tests/skills/test_chain_check.py:2134` | `c783f18f4` | P | removed: the docstring ends "named at the `add`'s `to`." |
| 48 | `tests/skills/test_chain_check.py:2162` | `a10750aea` | P | removed: the docstring ends "names the other document." |
| 49 | `tests/skills/test_chain_check.py:2192` | `4105fd13c` | P | removed: the docstring ends "and none is named." |
| 50 | `tests/skills/test_chain_check.py:2225` | `4105fd13c` | P | removed: the docstring ends "with the section reader's reason." |
| 51 | `tests/skills/test_chain_check.py:2248` | `4105fd13c` | P | removed: the docstring ends "the error's name is the platform's." |
| 52 | `tests/skills/test_chain_check.py:2271` | `4105fd13c` | P | removed: the docstring ends "rather than ending the check." |
| 53 | `tests/skills/test_chain_check.py:2297` | `4105fd13c` | P | removed: the docstring ends "rather than reading as no pin." |
| 54 | `tests/skills/test_pact_check.py:305` | `977b6613` | P | removed: the docstring ends "every line it did not is a sentence." |
| 55 | `tests/skills/test_pact_check.py:819` | `977b6613` | P | removed: the docstring's first sentence ends "at exit 2." |
| 56 | `tests/skills/test_pact_check.py:822` | `28edee12` | P | removed: the docstring ends "(#1132, S1)." |
| 57 | `tests/skills/test_pact_check.py:889` | `977b6613` | P | removed: the first sentence ends "the line names the row to write." |
| 58 | `tests/skills/test_pact_check.py:891` | `28edee12` | P | "The token is read in any case (#1132, S6), so each of the six ids that spell it otherwise is refused too." |
| 59 | `tests/skills/test_pact_check.py:998` | `29e1b040` | P | removed: the docstring ends "and nothing is refused." |
| 60 | `tests/skills/test_pact_check.py:999` | `49bb6ba5` | P | removed with row 59's sentence |
| 61 | `tests/skills/test_pact_check.py:1053` | `977b6613` | P | removed: the docstring ends "is named at exit 2." |
| 62 | `tests/skills/test_payload_meter.py:402` | `0830987a` | P | removed: the docstring ends "and `y.md` is no row." |
| 63 | `tests/skills/test_payload_meter.py:422` | `346cd01d` | G | "A dangling import loads nothing and says nothing in a session, so the meter says it" |
| 64 | `tests/skills/test_payload_meter.py:448` | `346cd01d` | G | "Claude Code reads a file once when two memory files import it by one path, so one real path is one row across the pair" |
| 65 | `tests/skills/test_payload_meter.py:1245` | `346cd01d` | G | "#1177. An import through a symlink loads the target, so the row is the target's, by its real path and its bytes." |
| 66 | `tests/skills/test_payload_meter.py:1293` | `0830987a` | P | removed: the docstring ends "The import after the fence closes is read." |
| 67 | `tests/skills/test_payload_meter.py:1316` | `0830987a` | P | removed: the docstring ends "(`frame/design.md` G3 of #1185)." |
| 68 | `tests/skills/test_payload_meter.py:1338` | `0830987a` | P | removed: the docstring ends "and the import after it is read." |
| 69 | `tests/skills/test_payload_meter.py:1347` | `0830987a` | P | removed, with the mutation that showed the case red: the docstring ends "the import in the next paragraph is read." |
| 70 | `tests/skills/test_payload_meter.py:1372` | `0830987a` | P | removed: the docstring ends "hides the rest of the file." |
| 71 | `tests/skills/test_payload_meter.py:1382` | `0830987a` | P | removed: the docstring ends "the chain keeps the path as written." |
| 72 | `tests/skills/test_payload_meter.py:1488` | `6137faf8` | P | removed, with the mutation that showed the case red: the docstring ends "the one module it loads." |
| 73 | `tests/skills/test_seal_stamp.py:1677` | `15a5ce66` | P | "The `as filed` shape is the guarantee's shape before #1198." |
| 74 | `tests/skills/test_session_cost.py:4499` | `ab116d1e` | P | removed: the docstring ends "well under the file's own." |
| 75 | `tests/skills/test_session_cost.py:4770` | `7b4162fd` | P | removed: the docstring's last paragraph is the round 1 finding it answers, alone |
| 76 | `tests/skills/test_unverified_check.py:505` | `6137faf8` | P | removed, with the mutation list: the class docstring ends "a comment's delimiters stand in none." |
| 77 | `tests/test_conftest.py:533` | `977b6613` | P | removed: the docstring ends "is taken away as before." |
| 78 | `tests/text/test_a_moved_rule_leaves_its_definition.py:8` | `e51fd0b` | G | "Without this module, contract rule 9's body pasted back into `agents/proofer.md` as a paragraph, or under a `###` heading, leaves `test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`, `test_every_agent_reads_the_contract` and `test_the_agent_contract_holds_the_universal_rules` all green. Only a paste under a new `##` heading is caught there, by the list of `## ` headings `test_every_agent_reads_the_contract` holds each definition to (#957)." The next sentence reads "When phases 1 and 2 wrote their two modules, every assertion in them was a presence check". "81 passed, exit 0" went with the measurement. Phase 1 wrote "under a new heading leaves … all green" and "Every assertion … is a presence check" here, and the sealer withheld on the first (`guarantee.md` at `7b03f3aa`): the fix pass after it wrote this text, as the next paragraph says |
| 79 | `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:26` | `5d51b319` | P | removed: the paragraph at lines 25 to 29 |
| 80 | `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:28` | `c48cd5e3` | P | removed with row 79's paragraph |
| 81 | `tests/text/test_a_rider_reaches_its_file.py:70` | `74c7963a` | P | removed: the docstring ends "the one place the old convention survived." |
| 82 | `tests/text/test_ci_gives_the_checks_what_they_need.py:673` | `5287dd42` | P | removed: the docstring ends "carries the whole history." |
| 83 | `tests/text/test_ci_gives_the_checks_what_they_need.py:702` | `5287dd42` | P | removed: the docstring ends "rather than listing the refusals." |
| 84 | `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:30` | `1fa25931` | N | "A gone phrase is the carrier's own wording before #639." |
| 85 | `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:48` | `5a66666d`, `1fa25931` | N | "Its gone half is also the wording before #639." |
| 86 | `evals/behaviour/proofer/seeded-55b66958/case.yaml:2` | `55b66958` | D | stays |
| 87 | `evals/behaviour/proofer/seeded-55b66958/prompt.md:5` | `48d035aa`, full SHA | D | stays |
| 88 | `evals/behaviour/proofer/seeded-55b66958/scaffold.sh:5` | `48d035aa…` full SHA | D | stays |
| 89 | `evals/behaviour/proofer/seeded-55b66958/scaffold.sh:6` | `48d035aa…` full SHA | D | stays |
| 90 | `evals/behaviour/proofer/seeded-55b66958/scaffold.sh:22` | `48d035aa…` full SHA | D | stays |
| 91 | `evals/behaviour/proofer/seeded-5fd6b88c/case.yaml:2` | `5fd6b88c` | D | stays |
| 92 | `evals/behaviour/proofer/seeded-5fd6b88c/prompt.md:5` | `a92c358b`, full SHA | D | stays |
| 93 | `evals/behaviour/proofer/seeded-5fd6b88c/scaffold.sh:5` | `a92c358b…` full SHA | D | stays |
| 94 | `evals/behaviour/proofer/seeded-5fd6b88c/scaffold.sh:6` | `a92c358b…` full SHA | D | stays |
| 95 | `evals/behaviour/proofer/seeded-5fd6b88c/scaffold.sh:22` | `a92c358b…` full SHA | D | stays |
| 96 | `evals/behaviour/proofer/seeded-7a8899d5/case.yaml:2` | `7a8899d5` | D | stays |
| 97 | `evals/behaviour/proofer/seeded-7a8899d5/prompt.md:5` | `15a5ce66`, full SHA | D | stays |
| 98 | `evals/behaviour/proofer/seeded-7a8899d5/scaffold.sh:5` | `15a5ce66…` full SHA | D | stays |
| 99 | `evals/behaviour/proofer/seeded-7a8899d5/scaffold.sh:6` | `15a5ce66…` full SHA | D | stays |
| 100 | `evals/behaviour/proofer/seeded-7a8899d5/scaffold.sh:22` | `15a5ce66…` full SHA | D | stays |
| 101 | `evals/behaviour/proofer/seeded-ea73e94f/case.yaml:2` | `ea73e94f` | D | stays |
| 102 | `evals/behaviour/proofer/seeded-ea73e94f/prompt.md:5` | `5560c742`, full SHA | D | stays |
| 103 | `evals/behaviour/proofer/seeded-ea73e94f/scaffold.sh:5` | `5560c742…` full SHA | D | stays |
| 104 | `evals/behaviour/proofer/seeded-ea73e94f/scaffold.sh:6` | `5560c742…` full SHA | D | stays |
| 105 | `evals/behaviour/proofer/seeded-ea73e94f/scaffold.sh:22` | `5560c742…` full SHA | D | stays |
| 106 | `.test_durations:1585` | `279a580b` | D | stays |
| 107 | `tests/evals/test_replay_targets.py:1043` | `279a580b` | D | stays |
| 108 | `tests/evals/test_seed_defects.py:582` | `279a580b` | D | stays |
| 109 | `tests/evals/test_seed_defects.py:604` | `279a580b` | D | stays |
| 110 | `tests/evals/test_replay_targets.py:632` | `ce448bbe` | D | stays |
| 111 | `tests/evals/test_replay_targets.py:641` | `ce448bbe` | D | stays |
| 112 | `tests/behaviour/test_a_cited_section_stands_in_its_file.py:668` | `f6ae6db6` | D | stays |
| 113 | `tests/test_censuses.py:982` | `5f11923f` | D | stays |
| 114 | `tests/test_censuses.py:983` | `67694cba`, `0ed5dd3b` | D | stays |
| 115 | `tests/test_censuses.py:1055` | `5f11923f` | D | stays |

**`frame/questions.md` Q1, answered by the work.** For each G and N line, the choice of number:

- Rows 63 to 65 (D1 row 31), option (c), with `#1177` kept as the work item tag it already was. `gh issue view 1177` and `gh pr view 1186` (executed, 2026-11-05) show #1177's page asks whether an `@` import follows a symlink and whether a file imported twice is read once, and holds neither answer, nor the dangling import's behaviour. So no sentence sends its reader to #1177 for the probe's result: each states the harness behaviour itself. Rows 63 and 64 keep their opening "#1177, S5." Row 65 opened with "#1177's first frame, … probe b:", and now opens "#1177." like its neighbours. This departs from D1 row 31's "`#1177` stays where its page holds what the sentence sends the reader there for", because the page holds the question and not the behaviour. The grounds are Q1's default, judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a citation of a page that does not hold the fact misdirects as a dead commit does.
- Row 78 (D1 row 36), option (c). The sentence states the defect itself; `#107` stands in the paragraph above and is not added again. Phase 1 kept the measurement's "under a new heading" and its present tense without running the claim at HEAD, and HEAD contradicted it. The fix pass after the sealer's withholding ran it (executed, in a scratch clone at `853b3fbc`, removed afterwards): rule 9's body appended to `agents/proofer.md` three ways, then one `pytest -q` over the four named modules and one over this module. With the module's own `paste_back`, a new `## What rule 9 states` heading, the four gave exit 1, with `test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract[agents/proofer.md]` failing on the `## ` heading list. Under a `### What rule 9 states` heading, and as a bare paragraph, the four gave 52 passed at exit 0. This module gave exit 1 with 3 failed in all three shapes, and 189 passed at exit 0 with nothing planted. The heading list entered at `2fc33333` (#957, 2026-10-18, by `git log --follow -S'headings are'`). The second sentence's "is a presence check" was false at HEAD for the same list, so it now says what held when #107's phases wrote the two modules.
- Rows 84 and 85 (D1 row 40), option (a), `#639`, which both lines already named. `gh issue view 639` (executed) shows its *Where it lives* section quoting the old wording of three of the carriers. Each line now dates the gone wording by #639 and names no commit.
- Rows 12, 13, 22, 29, 31, 42 and 43, option (c). Each says in the present what its case or constant holds. Row 13 adds no number, because `(#667)` stands on the title line. Row 29 is the comment above `UNREADABLE`, and the case that iterates it, `test_refuses_json_a_gate_prints_that_is_not_a_hooks_output_and_ends_nothing`, plants each shape beside a neighbour's `deny` and `systemMessage` and holds that both survive (read).

**Three P rewrites state what the case refuses in place of the commit (read, each against the code the commit named).** D1's P disposition keeps "what the earlier code did" in present terms where the docstring says nothing else of it.

- Rows 32 to 35. `git show 346b4af7:skills/verify/scripts/arm_check.py` holds neither `TemplateStr` nor `ONLY_ON_SOME_PYTHONS` (executed), so each *Red how* names the missing table entry or declaration.
- Rows 36 to 38, 40 and 41. At `a340221b`, `clear_bytecode_cache(path)` takes no `cwd` and `run_arms` makes no run before the first mutation (executed: `git show a340221b:skills/verify/scripts/arm_check.py`, the signature at line 758 and no `baseline`). So each *Red how* names the script "without the first run", the docstrings' own term for that run, or the missing `cwd`.
- Rows 39, 44, 45 and 46. `6bbaa4d1` and `dc1b0d14` resolve nowhere in this clone (M2), so each *Red how* names the defect the docstring above it states: the strict decode, the refusal that does not put the module back, the put-back's error raised out of the `finally`, and the missing entry block.

Row 58 keeps that the case's six other ids are refused. The case's parameter list holds eight shapes, each asserted at exit 2 (read), and the old clause was the only sentence that said the case covers the other spellings.

**Rewraps beside the rewrites.** Where a removed clause left a line short, the paragraph was rewrapped to its next sentence break, with no word changed: `.github/workflows/test.yml:79-84`, `skills/implement/scripts/seal.py:1216-1219` and `:2191-2193`, `tests/block_shapes.py:11-14`, the comment of row 10, the docstrings of rows 22 and 78, and the docstrings of `tests/skills/test_arm_check.py` rows 33, 35, 37 and 38. `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:335`'s header is the one line changed that holds no token, and D1 row 12 names it.

**S1, the tokens left (executed at `43b9b1be`, in this clone, which holds the commits).**

- `git grep -nP '\b(<the 61 tokens>)\b' -- . ':(exclude)seal/'` printed 30 lines: the 20 under `evals/behaviour/proofer/seeded-*/`, `.test_durations:1585`, `tests/evals/test_replay_targets.py:632`, `:641`, `:1043`, `tests/evals/test_seed_defects.py:582`, `:604`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py:668`, and `tests/test_censuses.py:982`, `:983`, `:1055`. These are rows 86 to 115.
- M1 lists 18 tokens: `0ed5dd3b`, `15a5ce66` and its full SHA, `279a580b`, `48d035aa` and its full SHA, `5560c742` and its full SHA, `55b66958`, `5f11923f`, `5fd6b88c`, `67694cba`, `7a8899d5`, `a92c358b` and its full SHA, `ce448bbe`, `ea73e94f`, `f6ae6db6`. Each is a row 86 to 115 token, and `git merge-base --is-ancestor <token> origin/main` holds for all 18, with `origin/main` at `31558c76`.
- M2 lists 33 tokens, the 33 the frame reads as naming no commit. The 12 commit tokens it listed at the base are gone: `0d59003`, `0e676e6`, `589cf25`, `5d51b319`, `6bbaa4d1`, `7966a9f9`, `7e44106`, `81888e2`, `8fb1fb5`, `dc1b0d14`, `e01e1b12`, `e51fd0b`.

**S2, no new commit (executed).** `git diff -U0 31558c76 43b9b1be -- . ':(exclude)seal/'`, its `+` lines grepped with M1's pattern, printed no token.

**S3, code unchanged (read).** In `git diff -U0 31558c76 43b9b1be -- .github/workflows/test.yml skills/implement/scripts/seal.py`, every `+` and `-` line is a comment.

**S4, the touched modules hold (executed).** One `bin/test -q` over 55 modules: the 26 touched test modules, every test module whose text names `test.yml`, `workflows`, `block_shapes` or `implement/scripts/seal.py`, and `tests/test_censuses.py`. On `43b9b1be` before this record and the closing memo existed, it gave 3,620 passed, 14 skipped and one failure, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which names this work item for having no `gaps.md`. The memo this phase writes is what that case asks for. With this record and the memo in the tree, the same command gave 3,621 passed and 14 skipped at exit 0, and a second `bin/test -q` over the 26 other test modules whose text names `seal/threads` or `"threads"` gave 1,073 passed at exit 0. `uvx ruff check` and `uvx ruff format --check` over the 28 changed Python files exited 0.

**S5.** This record, rows 1 to 115.

**S6, a cited issue holds what it is cited for (executed).** `gh issue view 639` for rows 84 and 85; `gh issue view 1177` and `gh pr view 1186` for rows 63 to 65, whose answer is the departure above. No other rewrite names an issue where the base named a commit.

**No mutation run.** The phase changes comments and docstrings alone and adds no behaviour, so `skills/verify/SKILL.md` *The narrow command still has to be able to fail* asks only that each module imports, which S4's run holds.
