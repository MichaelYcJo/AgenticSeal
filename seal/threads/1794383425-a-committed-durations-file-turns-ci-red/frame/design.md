# Design: 1794383425-a-committed-durations-file-turns-ci-red (#1486)

## Grounding

The tree as read at `196a450a5`.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A mechanism stays only while what it caught outweighs what it costs, and nothing is kept beside the tree to stay in step with it. The committed `.test_durations` is such a thing: 38 commits have touched it (executed, `git log --oneline -- .test_durations`), and its age verdict caught a stale file and no defect. The issue's five red runs (40611201777, 40895243786, 41203186159, 41407725325, 42179293981) and the red 0.37.0 release run (42714377663) are the issue's claim, labelled executed there, and not opened by the framer. |
| `skills/core/SKILL.md` *The first value: efficient development through the workflow* | A script reads what a real parser returns and does not re-encode a grammar. The tests that read a workflow's jobs, steps and keys by indentation and regular expressions read PyYAML's result instead. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | This work item's subject is the code, so the one policy-root sentence it makes false, in `docs/releasing/release-checklist.md` *The release pull request*, is stated under `## Rule changes` for the settle. `CONTRIBUTING.md` is outside the policy root and is rewritten in place. |
| `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/frame/design.md` `## Rule changes` | An unsettled design changes two other sentences of the same checklist section. Neither is the sentence this work removes (read). |
| Issue #1486 *Decisions* (2026-11-11) | Durations: a union from `main` runs, kept in `actions/cache` and restored by pull requests, so the shard balance stays and no committed file ages. YAML: PyYAML pinned the way `markdown-it-py` and `cmarkgfm` are, and the walker and the indentation compare go. Both are decided and not reopened here. |
| The package index's JSON for PyYAML | PyYAML's newest release is 6.0.3, with wheels for CPython 3.12 and 3.14 on Windows (amd64), macOS (x86_64 and arm64) and manylinux x86_64, so no runner compiles it. Its dist-info directory is `pyyaml-6.0.3.dist-info` (executed: the JSON read, and `uv pip install pyyaml==6.0.3` into a scratch venv). |
| PyYAML 6.0.3, `yaml.safe_load` against `yaml.BaseLoader` | `safe_load` reads the top-level `on:` key of all six workflow files as the boolean `True`, because PyYAML reads YAML 1.1. `BaseLoader` keeps the key `on` and returns every scalar as a string, such as `'15'`, `'3.12'` and `''` for an empty `pull_request:` (executed: `test_tmp_yaml_probe.py` over `.github/workflows/*.yml` and `templates/setup/hygiene.yml`). The walker returned strings with their quotes off, so `BaseLoader` keeps the values the cases compare. |
| pytest-split 0.11.0, `pytest_split/plugin.py#Base` and `algorithms.py#_get_avg_duration_per_test` | A missing durations file reads as `{}`. Every case is then priced at 1 s, the split is by count, and the plugin prints `No test durations found`. Durations are filtered to the collected cases before the mean is taken, so an entry for a removed case changes no division (read, in the scratch venv). |
| `actions/cache` README at `v4`, `restore/README.md`, `tips-and-workarounds.md` | A default-branch cache is available to other branches. `restore-keys` matches by prefix, newest first. A cache key is immutable, so a run that saves uses a key of its own. A cache unused for a week is evicted, and a repository holds 10 GB. A cache's version hashes its `path` and compression, and a cache saved on ubuntu restores on Windows only where `enableCrossOsArchive: true` is set (read, fetched with `gh api` into scratch). |
| The repository's Actions settings | `main` is the default branch, and the repository is public. It holds no active cache. Artifacts are kept 90 days, the maximum allowed (executed: `gh repo view`, `gh api …/actions/cache/usage`, `gh api …/actions/permissions/artifact-and-log-retention`). |
| `main`'s push runs | Eight `tests` push runs on `main` from 2026-11-08 to 2026-11-11, and eight tags `v0.34.1` to `v0.37.3` over the same days (executed: `gh run list`, `git for-each-ref`). A cache written on each push to `main` is rewritten about daily. |
| CI job times, 39 `tests` runs from 2026-11-09 to 2026-11-11 | The slowest job per leg: ubuntu 3.12 130 s, ubuntu 3.14 140 s, a macOS shard 128 s, a Windows shard 242 s. Medians: 104 s, 123 s, 85 s and 174 s (executed: `gh api …/runs/<id>/jobs` for the 40 newest completed runs, one of which answered `Server Error`, summed by `test_tmp_job_times.py`). |
| The same runs, as a model | Over the 38 runs with every shard: Windows spent a median 432 s and at most 521 s of case time across its four shards, and its slowest shard took a median 200 s and at most 242 s. macOS spent a median 115 s and at most 177 s across three shards. With the fixed costs `test.yml` states (62 s Windows, 45 s macOS), macOS run as one job is estimated at 160 s on the median run and 222 s on the slowest (executed as a model by `test_tmp_shard_model.py`, not run as one job). |
| `.github/workflows/test.yml` comments | 14 lines carry an eleven-digit run id (executed, `grep -c -E '[0-9]{11}'`). The issue counts 15. |
| `.github/scripts/release_report.py#durations` | It reads `.test_durations` from the tree at `--at` and at `--root`, and exits 2 when the file cannot be read. With the file gone from the tree, the `release-report` job would be red on every release pull request (read). |
| Readers of `.test_durations` | `.gitattributes:23`, `.github/scripts/release_report.py`, `.github/scripts/durations_union.py`, `.github/workflows/test.yml`, `CONTRIBUTING.md:145-189` and `:296`, `docs/releasing/release-checklist.md:141-147`, `tests/censuses.py#OLD_NAME_RECORDS`, `tests/test_censuses.py:1069`, `tests/conftest.py#posix_id` and the comment above `COLLECTED_NODE_IDS`, `tests/behaviour/test_the_release_check_watches_what_ships.py:71`, `tests/text/test_the_direct_answer_owes_the_sealers_record.py:44`, `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:46`, `tests/github/test_release_report.py`, `tests/github/test_durations_union.py` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` (executed: `git grep -n -e test_durations -e test-durations -e durations_union`, the whole tree less `seal/threads/`). |
| Sentences resting on "no YAML parser is installed" | In the suite: `tests/conftest.py:69`, `tests/test_conftest.py:107` and `tests/text/test_ci_gives_the_checks_what_they_need.py:213`, and `tests/behaviour/test_the_gate_names_every_step_ci_runs.py:28`, which #1483 removes. In shipped scripts: `skills/verify/scripts/broad_gate.py:1776` and `skills/verify/scripts/deferral_check.py:22`, which stay true because the plugin ships no parser (executed: `git grep -n -i` for `pyyaml`, `yaml parser`, `no parser`, `hand-parsed`). |
| Importers of the walker | Two modules import from `tests/text/test_ci_gives_the_checks_what_they_need.py`: `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` and `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`. The issue counts three (executed, `git grep`). |
| The CI test environments | Two jobs install the suite's packages: `test.yml`'s `pytest` job (`:150`) and `publish-release.yml`'s `seal` job (`:137`), which runs the suite at the tag. No other workflow runs pytest (executed, `grep` over the workflows and the template). |
| `tests/behaviour/test_release_hygiene.py` version-token rows | A version-shaped token at or above the running version in a loaded file needs a row naming the file and the token, as `("CONTRIBUTING.md", "4.2.0")` does for markdown-it-py. PyYAML's `6.0.3` in `CONTRIBUTING.md` needs one (read). |
| `seal/follow-up.md` | Both tables are empty, so no item waits on this work (read). |
| `seal/parity.json` | Absent, so no original sits between the ticket and the code (executed, `ls`). |
| `routing.md` | Present: framer, crafter, review chain, automation yes (read). |

## Scope

In scope:

1. **PyYAML 6.0.3 is pinned for the suite.** `.github/scripts/run_tests.py` holds the pin beside `MARKDOWN_IT` and `CMARKGFM`, and `PACKAGES` installs it. The two pairs `has_markdown_it`/`add_markdown_it` and `has_cmarkgfm`/`add_cmarkgfm` become one pair driven by a table of the three pins, each with its dist-info directory and the sentence naming what reads it. The `pip install` lines of `test.yml`'s `pytest` job and `publish-release.yml`'s `seal` job, and the two fallback commands in `CONTRIBUTING.md` *Running the checks*, carry the pin. The cases that hold each line to the runner's constant hold this pin too. `tests/behaviour/test_release_hygiene.py` gains the row for `("CONTRIBUTING.md", "6.0.3")`.
2. **One loader reads a workflow.** A new module, `tests/workflows.py`, holds `load(path)`, which returns `yaml.load(text, Loader=yaml.BaseLoader)`. It is the suite's one reading of a workflow file. It sits beside `tests/commonmark_oracle.py` and `tests/gfm_table_oracle.py`, so a missing PyYAML fails the modules that read a workflow and leaves `tests/conftest.py` importable. `Test_load` pins that `on` comes back as the key `on` and a scalar as a string, seen red under `yaml.SafeLoader`, and holds a relative path read from another working directory and a missing path refused, as `CONTRIBUTING.md` *The test layout* asks of a public function.
3. **The named walker and the indentation compare go.** `tests/text/test_ci_gives_the_checks_what_they_need.py:85-470` goes with its six cases: `strip_comments`, `read`, `workflows`, `raw`, `workflow_texts`, `steps`, `command`, `top_level`, `events`, `concurrency`, `jobs`, `_flow_mapping`, `matrix_include_entries` and the `MATRIX` fixture. The module's remaining cases read `tests/workflows.py#load`. A case whose subject is a comment, the one-line pointer above each shared step in `test_the_steps_the_template_shares_have_one_source`, reads that comment from the raw text, because a parser drops comments. `tests/behaviour/test_a_release_publishes_its_note.py#workflow`, `#job` and `#steps` go, and its three cases read the loader. The two importing modules read the loader as well: `test_the_windows_leg_runs_in_shards_that_make_the_whole.py` loses `job_steps`, `step_fields`, `uploads` and `job_keys`, and `test_the_suite_has_a_command_that_is_cheap_twice.py` loses its imports of `jobs`, `matrix_include_entries` and `read`.
4. **Every other test that reads a workflow's structure reads the loader.** The class is a test helper that takes a job, a step, or a key's value out of `.github/workflows/*.yml` or `templates/setup/hygiene.yml` by indentation, by a regular expression over lines, or by splitting on a neighbour's text. The build enumerates it by its own method: every file under `tests/` that names one of those paths (`git grep -l` gave 27 files at `196a450a5`), each read for such a helper. The framer's own sample, read: `tests/conftest.py#code_lines`, `#_indent`, `#_unquote`, `#workflow_steps`, `#workflow_step` and `#step_running` with their cases in `tests/test_conftest.py` and the premise comments at `tests/conftest.py:69` and `tests/test_conftest.py:107`; `tests/behaviour/test_a_body_naming_two_issues_claims_one.py:54`; `tests/behaviour/test_release_hygiene.py:1015` and `:1257`; `tests/e2e/teammate/test_teammate_flow.py#run_blocks`; `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py#keyed_under_env` and its base reader; `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py#job_block`; and `tests/behaviour/test_the_release_check_watches_what_ships.py#ships_pattern`. A `run:` value the parser returns still holds the script's own shell comments, so a reader that reads a script for a flag strips them, and `tests/conftest.py#code_line` stays for that reading alone, its docstring saying so. A substring test over a whole file, such as `"publish_release_note.py" not in hygiene`, reads no structure and is outside the class.
5. **`.test_durations` leaves the tree, and the union lives in the cache.** The file is deleted, and `.gitignore` names `/.test_durations`, so neither a restored nor a downloaded copy is committed. Each Windows shard restores the newest union from `actions/cache` before its pytest line. The `durations` job writes the union to `.test_durations` and, on every run that is not a pull request's, saves it to the cache. `.github/scripts/durations_union.py` keeps the union, its refusals and its per-shard report, and loses the age verdict: `STALE_SHARE`, `REMEDY`, `Staleness`, `staleness`, `verdict`, `--committed`, `--stale-fails` and the per-part price ratio against the committed file.
6. **The release table reads the union from run artifacts.** `.github/scripts/release_report.py` takes `--durations FILE` for this run's union and `--durations-at FILE` for the tag's. An absent file reads as no reading in the suite row and the test-file table, as an absent job list does. A present file that does not parse still exits 2. The `release-report` job needs `durations`, downloads this run's `test-durations` artifact, and downloads the tag's push run's artifact with `gh run download`.
7. **The documents and comments that stated the committed file are rewritten in place.** `CONTRIBUTING.md` *Running the checks* states the cache and the absence of any refresh, and its module-rewrite threshold at `:296` reads the newest `test-durations` artifact of a push run on `main`. The checklist's refresh sentences go through `## Rule changes`. `.gitattributes:23`, the entry in `tests/censuses.py#OLD_NAME_RECORDS` and its comment, `tests/test_censuses.py:1069`, `tests/behaviour/test_the_release_check_watches_what_ships.py:71`, the comment at `tests/text/test_the_direct_answer_owes_the_sealers_record.py:44` and the docstring at `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py:46` lose the file or name the union. `tests/conftest.py#posix_id` and the comment above `COLLECTED_NODE_IDS` state the reason that remains.
8. **`test.yml` sizes its legs from recent runs and names no run.** The comments hold no run id. The timeouts follow the rule they already state, 1.5 times the slowest measured job, rounded up to 5 minutes: ubuntu at 3.12 and 3.14 take 5, macOS takes 10, and Windows takes 10. macOS runs as one job, because its whole suite is estimated to finish inside the Windows leg's slowest shard, so a shard of it shortens no run. Windows keeps four shards, the balance the issue's decision keeps. The slowest Windows shard is recorded before, from the measurement in *Grounding*, and after, from this work item's own pull request run, in the phase record.

Out of scope:

- **The shipped scripts' YAML readers**, `broad_gate.py`'s step reader, `deferral_check.py` and `payload_meter.py`. The plugin ships with no third-party dependency, so a user's repository has no parser, and `broad_gate.py`'s section goes with #1483.
- **More than four Windows shards.** Five or six would shorten the slowest shard by an estimated 33 s or 55 s for one or two more jobs, each paying about 62 s of fixed cost. The issue's decision keeps the four-shard balance, and the after reading is what a later change would weigh.
- **`posix_id` and the interpreter-path case.** `tests/conftest.py#repo_relative` and `tests/behaviour/test_a_test_file_takes_the_root_from_the_conftest.py:61` use `posix_id` for paths, and a Windows runner's interpreter path changes with its tool cache. Both keep a reason, so only their docstrings change, under *Scope* item 7.
- **A schedule that keeps the cache warm.** `main` takes a push about daily, and every pull request's restore counts as a use. An evicted cache divides by count and turns nothing red.
- **Literal-phrase asserts in files this work does not rewrite.** That sweep is #1488's.
- **The eval cases' `case.yaml` files.** `evals/scripts/behaviour.py` writes them, and no code in this repository reads them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 a pull request after a push to `main` | Given a push run on `main` saved a union under a key starting `test-durations-`, when a pull request's Windows shard runs, then its restore step restores `.test_durations` and pytest-split divides by it. | The restore step's log names the matched key, and the shard's log has no `No test durations found` line. Only a run after this workflow reaches `main` can show it (`frame/questions.md` Q1). |
| S2 no cache | Given no cache matches, as on this work item's own pull request, when the Windows shards run, then each splits by count and passes or fails on its cases alone. | pytest-split's source (*Grounding*), and this work item's pull request run, whose Windows logs carry `No test durations found` and whose jobs pass. |
| S3 no run fails on a file's age | Given any run, the `durations` job exits 0 where the parts make the whole suite and 2 where they do not, and no step reads the age of a file. | `tests/github/test_durations_union.py`. A workflow case asserts the union step's command carries no `--committed` and no `--stale-fails`. |
| S4 a push to `main` writes the union | Given a push run on `main`, the `durations` job saves `.test_durations` under a key starting `test-durations-` with `enableCrossOsArchive: true`, and uploads the `test-durations` artifact kept 90 days. On a pull request it saves nothing and keeps the artifact 7 days. | Workflow cases in `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` read the loaded workflow. The restore step's `restore-keys` is the save key's prefix, and both name the same `path` and the same cross-OS flag. |
| S5 the release table | Given a pull request into `main`, `release-report` prints the suite row and the test-file table from this run's union and the tag's push run's union. Where either file is absent, the cells read as no reading and the script exits 0. | `tests/github/test_release_report.py` drives `--durations` and `--durations-at` over present, absent and unparsable files. `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py` holds the job's `needs` and downloads. |
| S6 the tree holds no durations file | `git ls-files .test_durations` prints nothing, and `git check-ignore .test_durations` names `.gitignore`. | Both commands at the build's last commit. |
| S7 an adopted `.venv` | Given a `.venv` without PyYAML 6.0.3, `bin/test` installs it once in one step and runs pytest. A failed install is a sentence, and pytest is still called. | `tests/github/test_run_tests.py`: the adopted and failed-install cases parametrized over the three pins, and the fresh-build case naming the three constants and asserting the table holds exactly them. |
| S8 CI installs the pin | Each CI line that builds the test environment installs `PyYAML==6.0.3` and no other PyYAML version. | `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py#test_ci_installs_the_parser_the_runner_pins` and `tests/behaviour/test_the_release_seal_is_drawn.py` read the loaded workflows. |
| S9 one reading of a workflow | No test helper takes a job, a step or a key out of a workflow by indentation or a regular expression. Comments are read from text only where a comment is the subject. | The enumeration of *Scope* item 4, written in the phase record with its method, and read by the proofer. |
| S10 `test.yml` names no run | `grep -c -E '[0-9]{11}' .github/workflows/test.yml` prints 0. The timeouts are 5, 5, 10 and 10 minutes by the stated rule, macOS is one entry, and Windows is four. | The command, and `tests/text/test_ci_gives_the_checks_what_they_need.py#test_every_pytest_leg_has_a_timeout_and_the_job_reads_it` with the shard cases. |
| S11 before and after | The slowest Windows shard is recorded before (a median 200 s and at most 242 s over 38 runs, *Grounding*) and after (this work item's pull request run). | The phase record of *Scope* item 8. The balanced after reading is `frame/questions.md` Q2. |

## Data & interfaces

**The pytest job's restore step**, before the pytest line, on the entries that split:

```yaml
- if: matrix.split != ''
  uses: actions/cache/restore@v4
  with:
    path: .test_durations
    key: test-durations-${{ github.run_id }}
    restore-keys: test-durations-
    enableCrossOsArchive: true
```

**The `durations` job.** The union step runs
`python .github/scripts/durations_union.py --parts parts --count 4 --out .test_durations`.
The upload step keeps `name: test-durations`, `path: .test_durations`,
`include-hidden-files: true`, `if-no-files-found: error` and `overwrite: true`,
and sets
`retention-days: ${{ github.event_name == 'pull_request' && 7 || 90 }}`.
A save step follows it:

```yaml
- if: ${{ !cancelled() && github.event_name != 'pull_request' && hashFiles('.test_durations') != '' }}
  uses: actions/cache/save@v4
  with:
    path: .test_durations
    key: test-durations-${{ github.run_id }}-${{ github.run_attempt }}
    enableCrossOsArchive: true
```

The key carries the attempt because a cache key is immutable, and a re-run
of a failed job on `main` saves again.

**`durations_union.py`**: `durations_union.py --parts DIR --count K --out FILE`.
Exit 0 wrote the union and its report. Exit 2 refused and wrote nothing. The
report keeps the entry count, the live seconds, each part's cases and seconds,
and the spread.

**`release_report.py`**: `release_report.py --against TAG --at DIR [--root DIR] [--ci-jobs FILE] [--ci-jobs-at FILE] [--durations FILE] [--durations-at FILE]`.
`DURATIONS` names no tree path any more.

**The `release-report` job**: `needs: [pytest, durations]`. An
`actions/download-artifact@v4` step with `name: test-durations` and
`path: ${{ runner.temp }}/durations` runs with `continue-on-error: true`,
because a refused union uploads nothing. The run step adds
`gh run download "$run" -n test-durations -D "$RUNNER_TEMP/durations-at" || true`
where `$run` is found, and passes both files.

**`run_tests.py`**: `PYYAML_VERSION = "6.0.3"` and `PYYAML = f"PyYAML=={PYYAML_VERSION}"`.
One table holds each pin, its dist-info directory name
(`markdown_it_py-4.2.0.dist-info`, `cmarkgfm-2025.10.22.dist-info`,
`pyyaml-6.0.3.dist-info`) and what reads it. One `has_` function and one
`add_` function take a row. The failure sentence for PyYAML names the modules
that import `tests/workflows.py` as a class, not as a list, since later phases add importers.

**`tests/workflows.py`**: `load(path)` returns the mapping
`yaml.load(text, Loader=yaml.BaseLoader)` gives for the file at `path`, a
repository-relative path or an absolute one. Every scalar is a string, and
the trigger key is `"on"`.

## Rule changes

- remove
  file: docs/releasing/release-checklist.md
  section: The release pull request
  from: The version moved in the release's first pull
    request, so the one pull request that may come between the last work item
    and this one refreshes `.test_durations`. The release pull request's
    `durations` job is red when the committed file prices too little of the
    suite its run measured, and its sentence names the refresh: the run's
    `test-durations` artifact, committed alone with the trailer
    `Seal-Routing: no work item`, in a pull request into `release/vX.Y.Z`,
    as `CONTRIBUTING.md` *Running the checks* gives it. The release pull
    request's next run reads the refreshed file.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The committed durations file, 881,625 B | `.test_durations` | The cache entry the `durations` job saves on every run that is not a pull request's, and the `test-durations` artifact kept 90 days on those runs. |
| Its export rule | `.gitattributes:23` | Nothing: an untracked file is in no archive. `.gitignore` keeps it out of the tree. |
| The age verdict and its remedy | `.github/scripts/durations_union.py#STALE_SHARE`, `#REMEDY`, `#Staleness`, `#staleness`, `#verdict`, the `--committed` and `--stale-fails` options, and the price ratio in `#report` | Nothing: no committed file ages, and pytest-split filters dead entries before it prices (*Grounding*). Catch record: six red runs of a stale file, the issue's claim, and no defect. |
| The verdict's condition and the committed file's argument | `.github/workflows/test.yml`, the union step's `--committed .test_durations` and `${{ github.base_ref == 'main' && '--stale-fails' || '' }}` | Nothing, for the reason above. |
| The verdict's and the committed file's cases | `tests/github/test_durations_union.py`, every case of `staleness`, `verdict`, `REMEDY`, `--committed` and `--stale-fails`; `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_verdict_is_asked_into_main_alone_and_the_upload_outlives_it`, `#test_the_durations_file_parses_and_names_cases` and `#ASK_THE_VERDICT` | The cases of the union and its refusals stay. The workflow cases of S3 and S4 hold the new steps. |
| The refresh recipe and its pin | `CONTRIBUTING.md` *Running the checks*, the paragraph opening "`.test_durations` goes stale"; `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` | One paragraph stating the cache, where it is written and read, and that nothing refreshes it by hand. Whether a case pins it is the build's to weigh against #1488's criterion. |
| The checklist's refresh sentences | `docs/releasing/release-checklist.md` *The release pull request* | The settle, through `## Rule changes`. |
| The tree read of the release table's durations | `.github/scripts/release_report.py#durations`, which reads `os.path.join(root, DURATIONS)` | `--durations` and `--durations-at`, the run artifacts. |
| Three entries naming the file | `tests/censuses.py#OLD_NAME_RECORDS` and the sentence above it, `tests/test_censuses.py:1069`, `tests/behaviour/test_the_release_check_watches_what_ships.py:71` | Nothing: the path no longer exists. |
| Run ids and the sizing argument of a 7,530 s suite | `.github/workflows/test.yml:43-67` and `:85-96`, 14 lines with a run id | The rule and its values stay in the comment. The measurement goes to the phase record of *Scope* item 8, and history to git. |
| The macOS shards | `.github/workflows/test.yml`, the three `macos-latest` entries with `split`; `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#SHARDED`'s macOS row | One `macos-latest` entry with no split. |
| The hand-written walker and its six cases | `tests/text/test_ci_gives_the_checks_what_they_need.py:85-470` | `tests/workflows.py#load`. |
| The indentation compare | `tests/behaviour/test_a_release_publishes_its_note.py#workflow`, `#job`, `#steps` | `tests/workflows.py#load`. |
| The shard module's own readers | `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#job_steps`, `#step_fields`, `#uploads`, `#job_keys` | `tests/workflows.py#load`. |
| conftest's workflow readers and their cases | `tests/conftest.py#_indent`, `#_unquote`, `#workflow_steps`, `#workflow_step`, `#step_running`, the comment at `:69`; `tests/test_conftest.py`'s cases of those helpers and the comment at `:107` | `tests/workflows.py#load`. `#code_line` and `#code_lines` stay only where a reader strips shell comments from a `run:` script. |
| The other structure readers *Scope* item 4 enumerates | each helper the build's enumeration lists | `tests/workflows.py#load`. |
| Two copies of the pinned-install pair | `.github/scripts/run_tests.py#has_markdown_it`, `#add_markdown_it`, `#has_cmarkgfm`, `#add_cmarkgfm` | One table-driven `has_`/`add_` pair over the three pins. |

A mechanism this work adds, with what goes in its place:

- The cache save and restore steps, and `.gitignore`'s `/.test_durations` line, replace the committed file, its age verdict and the hand refresh.
- PyYAML and `tests/workflows.py` replace the walker, the indentation compare and every helper *Scope* item 4 lists.
- The version-token row for `("CONTRIBUTING.md", "6.0.3")` is the cost of naming the pin in the fallback commands, which `CONTRIBUTING.md` already does for the other two pins.

Framed 2026-11-11 by framer, before the build.
