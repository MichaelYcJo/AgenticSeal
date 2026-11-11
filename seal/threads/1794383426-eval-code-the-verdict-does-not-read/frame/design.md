# Design: 1794383426-eval-code-the-verdict-does-not-read

## Grounding

The tree as read at `887127e61`.

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1487 *Decision*, given by the owner on 2026-11-11 before the first edit (read, `gh issue view 1487 --json body,comments`; no comments) | The plugin stops reporting the proofer's recall and false-finding rate (#971). The removal under *Change* goes ahead, and the eight proofer cases (`replay-*` and `seeded-*` under `evals/behaviour/proofer/`) stay frozen as they stand. This frame does not reopen either. |
| #1254, merged as `f93d70ea4` (read, `gh issue view 1254`) | It narrowed the suite to a smoke run and decided that "Recall, the false-finding rate and the token figures are recorded and judge nothing". The owner's decision above retires the first two. The token figures, spend, wall seconds, tool calls and preload bytes stay written, as #1254 decided. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A mechanism with no reader goes, and the same change removes what stood on it: the check, the exemption, the comment and the copy. Every unit this frame removes is found by following what reads the retired values (Scope), not by a search for their names. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | This work item's subject is the code, so the sentence of the policy root it falsifies, in `docs/checks/the-pull-request-check.md`, changes through `## Rule changes` below and is written by the settle. `evals/README.md` is not in the policy root (`docs/`, no `Policy root` key in `seal/config.json`, read), so the build rewrites it in place. |
| `skills/settle/rule-changes.md` *Rule changes* and `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser` (read) | A `path#name` citation whose file is deleted dangles unless a pending `## Rule changes` item's `from` holds it whole and its `to` does not. The `from` below quotes `evals/scripts/replay_targets.py#LAYOUTS` whole for that reason. The issue's third *Done when* line is met at the 0.37.4 settle, which writes the `to`. |
| `evals/scripts/noninferiority.py#verdict`, lines 782-794 (read) | The verdict reads shape and reach graders and the cut flags alone. Its docstring says no truth grader, row count, token, tool call, spend, second or preload byte is judged. |
| `evals/scripts/noninferiority.py#cheaper_model`, lines 1092-1119 (read) | `model` reads every grader's row, truth graders among them, and refuses a record with no truth grader. Its record is the sealer's. The sealer's four truth graders target `guarantee.md`, which `reads_record` does not match, so they already keep the eval's own result (read, `evals/behaviour/sealer/rule-sealer-no-gate/graders/truth-no-gate.md:3`). Truth graders therefore stay a grader kind. |
| Truth graders by case (executed, `find evals/behaviour -name 'truth-*.md'`) | 20 truth graders stand: 14 in the frozen proofer cases, 2 in `proofer/rule-proofer-one-finding`, and 4 in the sealer's rule cases. The issue's "serve only the proofer's 4 replay and 4 seeded cases" holds for the generators, not for the kind. |
| Readers of the generators (executed, `git grep -n -l 'replay_targets\|seed_defects\|recurred_truths\|regrade'`, outside `seal/threads/`) | `noninferiority.py` imports `replay_targets` for `record_reader` alone (line 324). `rule_cases.py` imports it for `truths_with` alone (line 318), which reads `recurred_truths.json`. That file holds one entry, the `truth-shout-twice-uncovered` grader of `proofer/rule-proofer-one-finding`. |
| `report_text` and its readers (read, lines 306-411 and 564-596) | `annotate` records each run's `report_text`, the round record the proofer's session printed, masked by `tests/censuses.py`. Its readers are `finding_rows`, through `text_of`, and `regrade`. `finding_rows` gives the report rows, the false rows and the re-grading of a truth grader over a round record. All three exist for recall and the false-finding rate. |
| Rule cases against their generator (executed, `rule_cases.py --out <scratch>` in a `git clone --no-local` of `887127e61`, then `diff -rq` per case) | All 17 rule cases the generator writes equal the committed ones byte for byte. Phase 2 must leave that equality, with the recurred truth written from `rule_cases.py` itself. |
| Durations the removed cases hold (executed, a `json` read of `.test_durations`) | `tests/evals/test_replay_targets.py` and `tests/evals/test_seed_defects.py` hold 115.3 s of the file's 1,616.5 s, 7.13 %. `.github/scripts/durations_union.py#STALE_SHARE` is 0.05, so dead entries past 5 % fail the release pull request's `durations` job under `--stale-fails` (read, lines 70 and 238-244). |
| Frozen case files and the refused words (executed, `grep -inE` with the stems of `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py#STEMS`) | `replay-1793411151-r2/prompt.md` and `scaffold.sh` hold `judgment` in a copied branch and item name, and `seeded-5fd6b88c/scaffold.sh` holds `evals/scripts/...` in its mutation line. Today the generator's text exempts those values. With the generators gone, nothing can. |
| `tests/censuses.py#RECORDS`, line 989 (read) | `evals/behaviour/` is a record prefix, so the frozen cases' own citations of removed files, such as `evals/scripts/replay_targets.py#records` in `seeded-5fd6b88c/graders/truth-seeded.md`, are not read by the citation case. `seeded-5fd6b88c/scaffold.sh` mutates `replay_targets.py` in a clone fetched at `ea27b618`, so deleting the file at HEAD leaves the case's run as it is. |
| `seal/follow-up.md` (read) | Both tables are empty. No item waits on this work. |

## Scope

In scope, numbered for `plan.md`:

1. `noninferiority.py regrade` goes, with every unit only it reads: `grader_at`, `suite_files`, `is_truth_file`, `truths_at`, `mean`, `regraded`, `differs`, `unreproduced`, `regrade`, `REGEX_FLAGS` and `SCORE_ERROR`.
2. The reader of the printed round record goes: `report_text`, `masked`, `apart`, `identifier_scan`, `finding_rows`, `text_of`, `reads_record`, `grade`, `RECORD_PATH`, `SCAN`, `UNREAD` and the `import replay_targets as rt`. `side_numbers` keeps the eval's recorded result for every grader. `annotate` records each run's cost and tool calls and no `report_text`. `compare` reads a side whose runs keep no `report_text`, since nothing it computes reads one.
3. The record `compare` writes drops the four row-count rows (`Baseline report rows`, `Baseline false rows`, `New report rows`, `New false rows`) and the two `tokens per true find` rows, in `render`, `cost_rows`, `merged` and `parse_record`. The `## Graders` table keeps every grader the eval graded, truth graders among them, and no rate is computed from them. `verdict`, `check` and `model` decide as before, and a record written before this change still checks, since `check` reads no row the change removes.
4. `scalar` and `grader_from`, whose readers after Scope 1 are tests alone, move into `tests/evals/test_rule_cases.py` with their cases. `case_runs` stays in `noninferiority.py`, where `side_numbers` reads it.
5. Text that states the removed reading is rewritten in place: the module docstring of `noninferiority.py`, and `evals/README.md` *The behaviour suite* where it states finding rows, recall, the false-finding rate, `regrade`, the `report_text` refusal and the point a proofer comparison is taken from. `tests/censuses.py`'s module docstring paragraph on being loaded without pytest, and `#refused_domains`'s sentence citing `noninferiority.py#masked`, go with the masking.
6. `evals/scripts/replay_targets.py`, `evals/scripts/seed_defects.py`, `evals/scripts/recurred_truths.json`, `tests/evals/test_replay_targets.py` and `tests/evals/test_seed_defects.py` go.
7. `rule_cases.py` writes `truth-shout-twice-uncovered` from a literal tuple beside `shout`, its pattern and body those of the committed grader file, so every rule case it writes stays byte for byte as committed. `truths_with` and the `rt` import go. In `tests/evals/test_rule_cases.py` the recurred-entry cases and their helpers (`recurred_file`, `entry`, `rule_truths`, `truth_regex`) go, and the module loads scripts with `conftest.load_module` in place of `test_replay_targets.load_script`.
8. `tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py` goes. It guarded one finding counted as two in recall (#971 round 1), and recall is no longer computed.
9. `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` passes over a `replay-` or `seeded-` case whole, as the record of a run at a recorded commit. The generator-text exemption (`generators`, `rendered`, `pattern_of`, `copied_spans`, `COPIED`, `READ`, `SLOT`, `STALE`) and its case `test_a_word_in_the_generators_text_is_refused_and_one_it_copied_is_not` go. Every other case file is read as before.
10. `tests/censuses.py#OLD_NAME_RECORDS` drops `evals/scripts/recurred_truths.json`, and `#KEPT_FILES` with its comment goes, both naming removed files. `tests/test_censuses.py` stops planting those paths.
11. `evals/README.md` rewritten where it states the generators: the sentence that cases are generated with `--list`, `--count` and `--case`, the generator table's two removed rows, the `recurred_truths.json` paragraph, and the copied-value exemption, which becomes the passing-over of Scope 9.
12. `.test_durations` drops the entries of every case Scopes 1, 2, 6 and 8 remove, where the file still stands when the phase builds.

`docs/checks/the-pull-request-check.md` changes through `## Rule changes` below and is not edited by the build.

Out of scope:

- Every case under `evals/behaviour/`. The frozen proofer cases stay as the owner decided, and the rule cases stay byte for byte (Scope 7).
- The cost figures and `run`'s collection of them: spend, tokens read, tool calls, wall seconds, preload bytes and tokens per tool call. #1254 decided they are written, and the owner's decision names recall and the false-finding rate alone.
- Truth graders as a kind, and `model`. The sealer's record reads them (Grounding).
- A case comparing every rule case with the generator's output. Phase 2 runs that comparison once and records it; a standing case would be a new mechanism with no catch on record.
- Any paid run of the suite.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given the tree after phase 1, when `python3 evals/scripts/noninferiority.py regrade --side a.json --suite-rev HEAD --out b.json` runs, then argparse refuses the subcommand and the exit code is 2. | executed, exit code read directly; `tests/evals/test_noninferiority.py` *Test_main* no longer lists `regrade` |
| S2 | Given two sides, when `compare` writes a record, then the record holds no `report rows`, `false rows` or `tokens per true find` row, and its verdict on the shape and reach graders is the one it gave before. | `tests/evals/test_noninferiority.py` *Test_render* and *Test_compare*, each changed case seen red first |
| S3 | Given a side whose runs keep no `report_text`, when `compare` reads it, then it writes the record and exits 0 where it exited 2 before. | a case in *Test_compare*, seen red against the old refusal |
| S4 | Given a record written before this change, with its four row-count rows, when `check` and `model` read it, then they compute the same verdict and the same model as before. | a case in *Test_check* over a record carrying the old rows |
| S5 | Given a saved side, when `run --from-raw` writes it again, then no run carries `report_text`, and each run's cost and tool calls are as before. | *Test_annotate* |
| S6 | Given the tree after phase 2, when `rule_cases.py --out <scratch>` runs, then every rule case it writes equals the committed one byte for byte. | executed: `diff -rq` per case against `evals/behaviour/<agent>/`, recorded in the phase record; `tests/behaviour/test_evals_layout.py` *test_the_sealer_cases_are_the_generators_output* |
| S7 | Given the tree after phase 2, then `evals/scripts/` holds `behaviour.py`, `noninferiority.py` and `rule_cases.py` alone, and `git diff 887127e61 -- evals/behaviour/` is empty. | executed: `ls` and `git diff --stat` |
| S8 | Given a `prompt.md` of a `rule-` case holding a refused word, when the evaluated-words case runs, then it names that file, line and word, while a `replay-` or `seeded-` case is not read. | `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py`, a planted case seen red |
| S9 | Given the tree after phase 2, then `evals/README.md` names no removed command, file or record row. | executed: `grep -n 'regrade\|replay_targets\|seed_defects\|recurred_truths\|report_text\|false rows\|true find' evals/README.md` prints nothing |
| S10 | Given the tree after phase 2, when the citation case reads `docs/checks/the-pull-request-check.md`, then `evals/scripts/replay_targets.py#LAYOUTS` is excused by this design's pending `change`, not dangling. | `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, run by the orchestrator's broad gate |

## Data & interfaces

- `noninferiority.py`'s command line loses the `regrade` subcommand; `run`, `compare`, `check` and `model` keep their arguments.
- A side written by `run` loses `agentic.report_text` on each run. A side that carries it is still read, and the key is ignored.
- A record written by `compare` loses the header rows Scope 3 names. `parse_record` stops reading them, so a record that carries them still parses.
- `rule_cases.py` takes the same arguments and writes the same bytes.

## Rule changes

- change
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: Three readers outside the check still open merged records: the
    release workflow's `seal` job reads every record of a release with the
    `chain_check` of the tree it runs from, and
    `evals/scripts/replay_targets.py` and `evals/scripts/seed_defects.py`
    read each labelled record, and each record in `seal` blocks, with the
    `chain_check` of the commit that last wrote it, from either layout a
    release has kept its records in: the one before 0.23.0, and
    `seal/threads/<id>/trail/rounds/` since
    (`evals/scripts/replay_targets.py#LAYOUTS` names both).
  to: One reader outside the check still opens merged records: the release
    workflow's `seal` job reads every record of a release with the
    `chain_check` of the tree it runs from.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `regrade` subcommand and its units (Scope 1) | `evals/scripts/noninferiority.py#regrade`, lines 1188-1501 but `scalar`, `grader_from` and `case_runs` | Nothing: it re-graded a paid side on a new truth, for recall alone. The issue's *What it could lose* names it, and the owner accepted that loss. |
| Its cases | `tests/evals/test_noninferiority.py` *Test_grader_at*, *Test_suite_files*, *Test_is_truth_file*, *Test_truths_at*, *Test_grade*, *Test_mean*, *Test_regraded*, *Test_differs*, *Test_unreproduced*, *Test_regrade*, and *Test_main*'s `regrade` parameter | Nothing: the code they pin goes. |
| The reader of the printed round record (Scope 2) | `evals/scripts/noninferiority.py#report_text`, `#masked`, `#apart`, `#identifier_scan`, `#finding_rows`, `#text_of`, `#reads_record`, `#grade`, `#RECORD_PATH`, `#SCAN`, `#UNREAD`, and the `replay_targets` import | Nothing: its values were recall and the false rows, which the owner stopped reporting. A run's raw trace still holds the printed record under `<out>.raw/`. |
| Their cases | `tests/evals/test_noninferiority.py` *Test_module*, *Test_identifier_scan*, *Test_masked*, *Test_apart*, *Test_finding_rows*, *Test_text_of*, *Test_reads_record*, *Test_report_text*, and the verdict case `a false-finding rate risen by a tenth is written and not judged` | Nothing: the code they pin goes. |
| The `#986` refusal of a side with no `report_text` | `evals/scripts/noninferiority.py#compare`, through `#side_numbers` and `#text_of`; `evals/README.md` *The behaviour suite*, the paragraph opening "A side that keeps no `report_text` is refused" | Nothing: no number `compare` writes reads `report_text` any more (S3). |
| The header rows Scope 3 names | `evals/scripts/noninferiority.py#render`, `#cost_rows`, `#merged`, `#parse_record` | Nothing: they reported the false-finding rate and recall's token cost. |
| The front-matter reader of a grader file (Scope 4) | `evals/scripts/noninferiority.py#scalar`, `#grader_from`, and *Test_scalar*, *Test_grader_from* | `tests/evals/test_rule_cases.py`, its one remaining reader. |
| The masking paragraph and citation in the census | `tests/censuses.py`, module docstring lines 26-28, and `#refused_domains` lines 1058-1060 | Nothing: no script loads the census to mask any more. |
| The two generators and their input (Scope 6) | `evals/scripts/replay_targets.py`, `evals/scripts/seed_defects.py`, `evals/scripts/recurred_truths.json` | Nothing, except the one recurred entry, which lands in `evals/scripts/rule_cases.py` as a literal truth (Scope 7). |
| Their cases | `tests/evals/test_replay_targets.py`, `tests/evals/test_seed_defects.py` | Nothing: the code they pin goes. `load_script`, which `tests/evals/test_rule_cases.py` imports, is replaced by `conftest.load_module`. |
| The recurred-truth reader in the rule generator and its cases | `evals/scripts/rule_cases.py`, line 318 and docstring lines 13-15; `tests/evals/test_rule_cases.py` *Test_main* recurred-entry cases, `#recurred_file`, `#entry`, `#rule_truths`, `#truth_regex` | `evals/scripts/rule_cases.py`, as a literal tuple. |
| The case that no two truths accept one location (Scope 8) | `tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py` | Nothing: it guarded recall's count. |
| The generator-text exemption (Scope 9) | `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py#generators`, `#rendered`, `#pattern_of`, `#copied_spans`, `#COPIED`, `#READ`, `#SLOT`, `#STALE`, and `#test_a_word_in_the_generators_text_is_refused_and_one_it_copied_is_not` | The same module passes over a `replay-` or `seeded-` case whole, as `tests/censuses.py#RECORDED_CASE` already does. |
| Two exemptions of the old-names census (Scope 10) | `tests/censuses.py#OLD_NAME_RECORDS`'s `recurred_truths.json` entry, `#KEPT_FILES` and its comment; `tests/test_censuses.py`, the planted paths at lines 928-930 and 945-947 | Nothing: the files they exempt go. |
| The README's account of the removed code (Scopes 5 and 11) | `evals/README.md` *The behaviour suite* | Rewritten in place to the commands that remain. |
| The durations of the removed cases (Scope 12) | `.test_durations` | Nothing: the cases go. Where #1486 has removed the file first, nothing is edited. |
| The sentence on the generators as readers of merged records | `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* | `## Rule changes` above, written at the settle. |

Framed 2026-11-11 by framer, before the build.
