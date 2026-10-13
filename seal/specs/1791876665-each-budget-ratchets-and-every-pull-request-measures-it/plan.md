# Implementation Plan: each budget ratchets and every pull request measures it

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-14 by the repository owner, when `smith` was spawned.

## Summary

One file names the budgets, one reader measures and compares them, and three places run the reader: a `hygiene.yml` step on every pull request (tree budgets, ratchet against the merge base, raise line from the body), a `test.yml` job after the suite (CI minutes), and one pytest case (so a session and the sealer see the tree budgets before pushing). Phase 1 proves the whole chain on one budget, `preload:warden`, with its before and after numbers and the gate seen red on a raise and green on a fall. Later phases add rows, not mechanism.

## Technical context

Everything the build stands on, read at f95f0ba8:

- `skills/verify/scripts/payload_meter.py` — resolves an agent's `skills:` list to files and reports bytes per file; `--json` carries the rows; the `CLAUDE.md` pair row is marked as the harness share. The preload measurer calls it and drops that row.
- `skills/settle/scripts/fold_check.py` + `tests/test_a_document_has_room_for_the_next_fold.py` — the shape to copy: a ceiling in a `seal/` table, one reader, one pytest case that runs the reader over the real tree.
- `skills/verify/scripts/unverified_check.py` `--baseline` — resolves the base to `git merge-base <ref> HEAD`; the ratchet reads `seal/budgets.md` at that commit with `git show <base>:seal/budgets.md`.
- `.github/workflows/hygiene.yml` — step order, `permissions: contents: read, issues: read`, the survivor step's `base_ref == main` exemption, `PR_BODY` through `env:` (the issue-claims step).
- `.github/workflows/test.yml` — matrix job names `pytest (<os>, 3.12, <split>, <timeout>)`; the leg is read off the name. The new `budgets` job: `needs: pytest`, `if: ${{ !cancelled() }}`, `permissions: actions: read`, `gh api repos/${{ github.repository }}/actions/runs/${{ github.run_id }}/jobs --paginate`.
- `hooks/config.py` — the GFM table walker every reader of a `seal/` table uses (#871); the budgets file is read through it, never by a grammar of its own.
- `tests/conftest.py#CASE_CEILING_S`, `tests/test_a_slow_case_names_itself.py::test_every_pytest_leg_has_a_timeout_and_the_job_reads_it` — the existing ceilings and the test that pins workflow shape; the budgets job gets a sibling case.
- `.github/scripts/issue_claims_check.py` — the precedent for a script that reads the pull request body from an environment variable and exits by what it found.
- `docs/the-reader-registry.md` — every new `def`/`class` carries a `Reads:` line; `tests/test_a_script_says_which_interpreter_it_needs.py` wants the floor line.

Slow files at ≥ 120 s in `.test_durations` (seconds, `executed` at f95f0ba8; the starting rows of `## Slow test files`): `test_the_seal_is_taken_once_by_the_sealer.py` 1183 · `test_the_commit_gate_decides_at_the_commit.py` 1137 · `test_the_fixes_close_the_record.py` 482 · `test_chain_check_at_the_pull_request.py` 375 · `test_a_fix_of_a_fix_is_counted.py` 331 · `test_a_corrected_sentence_survives_elsewhere.py` 293 · `test_a_released_row_is_read_again_in_a_fragment.py` 217 · `test_the_record_is_generated.py` 188 · `test_no_shape_the_base_stops_reads_silent.py` 185 · `test_one_heredoc_shape_is_data_to_the_commit_gate.py` 172 · `test_the_record_is_held_to_the_floor_and_the_depth.py` 165 · `test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py` 165 · `test_a_record_precedes_the_fixes_it_commissions.py` 161 · `test_a_fragment_left_behind_is_named.py` 145 · `test_a_finding_id_is_a_bare_integer.py` 135 · `test_the_last_rounds_fixes_are_checked.py` 126.

Docs history lines per file (`executed`, the classifier of `spec.md`): branch-and-release 11 · commit-review-gate-spec 15 · issues-and-milestones 8 · measuring-a-run 2 · one-root-by-lifetime.ko 32 · one-root-by-lifetime 38 · release-checklist 11 · review-chain-spec 25 · review-handoff-protocol 22 · round-record-spec 17 · the-agent-set 0 · the-broad-gate 0 · the-commit-gate-inside-git 8 · the-evidence-ledger 4 · the-pact 0 · the-reader-registry 2 · the-record-layout 10 · the-review-and-parity-arms 3 · worktree-guard-spec 38. The build re-measures every starting value with the checker itself at its own SHA; the frame's numbers are what it should find.

**What breaks in 6 months with the chosen approach.** The `Budget raised:` line becomes boilerplate and the file becomes a log of raises nobody reads. What catches it is the release summary's trend line (one line per budget against the last tag), which the release pull request prints without anyone asking for it; if that line is ignored too, the ratchet has become a report, and the fix is the owner's, not the mechanism's. Second: the docs classifier is four regexes, and a rewrite can satisfy it by deleting issue numbers rather than narrative; the printed rule/history ratio is the reader's check on that, and #923's review is where it is read.

## Alternatives considered

| Approach | Failure scenario (six months on) | Verdict |
|---|---|---|
| A. One `seal/budgets.md`, one checker, two-sided ratchet, gate or report per row | above | **chosen** |
| B. Keep adding ceilings where the existing ones live (`timeout-minutes`, `CASE_CEILING_S`, `Document line ceiling`) | a fifth ceiling in a fifth file with a fifth spelling; nothing compares a release with the last; files sit at 995–1,000 lines because the ceiling is the only reader | rejected |
| C. Reports only, no gate | the summary is on every run and nobody opens it; #908's table was filled once, by hand, and that was the mechanism's whole life | rejected for the deterministic rows; kept for the two rows whose number is not the pull request's to fix |
| D. Gate everything, `rounds-bytes` and `ledger-rereads` included | a chain goes red at round 4 with no fix that does not rewrite a committed record; a waiver habit forms, as `SPECSEAL_CASE_CEILING_S=600` already did on every 0.21.1 seal | rejected |
| E. Tokens as the unit, a tokenizer in CI | a tokenizer upgrade moves every number with no file changed, and it is not Claude's tokenizer; the ratchet fires on a `pip` resolve | rejected; bytes, with the calibration stated once |
| F. Measure the suite per pull request with `--store-durations` on the shards (#914) instead of the committed file | 1.2× run-to-run noise turns a per-file gate red on a quiet pull request; and the cadence of the file is #931's decision | rejected here; `ci-minutes:*` is the per-run measurement and it carries the noise allowance |
| G. A sticky pull-request comment instead of the job summary | needs `pull-requests: write`; #359 narrowed every scope to `read` on purpose, and a write scope every step inherits is the thing it removed | rejected |
| H. Split the work item | the CI-minutes job (phase 3) is the one separable part — a different workflow, a token scope, the API; split, it would land a release later and #929's leg decision would be framed against a row nobody measures on a pull request | not split; if the run must shrink, phase 3 is what leaves, after phases 1–2 |

**CI cost if this repository goes private** (`read` from #929 for prices; `executed` for minutes). Per pull request at the median: 9.8 ubuntu + 2 × 41.9 Windows + 10 × 19.8 macOS = 292 Linux-equivalent minutes ≈ US$2.33 at $0.008; at the ceilings, 15 + 2 × 59 + 10 × 32 = 453 ≈ $3.62. At #929's 40 runs a day, $93–145 a day, 68 % of it macOS. The price list date is unverified: the figures are #929's (mid-2026) and nobody opened the page for this frame. The lever is #929's item 3, which legs run on a pull request; the summary prints the billable line so that decision is made against a number.

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | One budget end to end: `seal/budgets.md` with the `preload:warden` row (ceiling 102,229, slack 2 %); `.github/scripts/budget_check.py` with the measure, the two-sided compare, the ratchet against `--baseline`, the body line, exit codes 0/1/2, the summary; the `hygiene.yml` step; `tests/test_a_budget_ratchets.py` with T1–T7, T12, T13, T16; the `docs/the-record-layout.md` §*seal/* row | before: 102,229 B measured by the checker at the phase's SHA; a probe adds 1,000 B to `agents/warden.md` → exit 1 (S1); removes 3,000 B → exit 1 asking to lower (S4); raises the row with and without the line → S2/S3; the hygiene step runs on the branch's pull request and is green. Numbers in `phases/phase-1.md` | |
| 2 | The tree budgets widen: the other four `preload:*` rows and `preload:claude-md`; the docs classifier and the `## Docs history lines` table; `suite-seconds` and the `## Slow test files` table with the 120 s threshold; T8–T10 | `budget_check.py` exit 0 on the tree; each case seen red by the mutation it names | |
| 3 | `ci-minutes:*`: the `budgets` job in `test.yml` (`needs: pytest`, `actions: read`), the jobs reader, the per-leg sum, the billable line; T11, T14; `CONTRIBUTING.md` §*Running the checks* "CI runs five jobs" rewritten in place | the job runs on the branch's pull request, the summary shows three legs against 15/59/32; a fixture-driven case per leg classification | |
| 4 | The reports and the trend: `rounds-bytes` per open work item, `ledger-rereads` on base `main`, `--trend <tag>`; `docs/release-checklist.md` §*2* gains the one-line-per-budget step (read from the summary, nothing to fill by hand); the changelog fragment; the ledger fragment with this spec's clauses anchored to units and tests | `--trend v0.21.1` prints one line per budget; `evidence-check` exit 0 | |

This table is also where the work records how far it got. **Status is empty, or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — the mutation each case kills

| Case | Guards | Mutation it kills |
|---|---|---|
| T1 `test_measured_over_ceiling_fails_naming_the_row` | S1 | `>` becomes `>=`, or the compare is dropped: the fixture is measured = ceiling + 1 |
| T2 `test_measured_inside_the_band_holds` | the band | the band inequality inverted: measured = ceiling exactly passes, ceiling × 1.02 passes |
| T3 `test_a_ceiling_above_the_band_asks_to_lower` | S4 | the lower-band check removed: measured = ceiling / 1.05 at slack 2 % fails and names the number to lower to |
| T4 `test_a_raise_without_its_line_fails`, `test_a_raise_with_its_line_passes_and_the_summary_shows_it` | S2, S3 | the baseline read dropped (raise passes), or the line regex loosened to any mention of the name (a line without the new value passes) |
| T5 `test_a_removed_row_is_a_raise` | the ratchet | a missing row treated as new: baseline has the row, HEAD does not, no `Budget removed:` line → must fail |
| T6 `test_base_main_skips_the_line_and_keeps_the_ceiling` | S6 | the whole check skipped on `main`: a raise passes, but measured > ceiling still fails |
| T7 `test_a_new_row_needs_no_line` | the first pull request | a new row treated as a raise |
| T8 `test_the_preload_measurer_sums_the_agents_files_and_not_the_pair` (NAME NOT IN TREE until phase 2 plants it) | `preload:*` | the `CLAUDE.md` pair row included: a hand-built tree with known sizes gives a different sum |
| T9 `test_the_docs_classifier_skips_fences_comments_headings_and_rule_blocks` (NAME NOT IN TREE until phase 2 plants it) | S8 | each exclusion dropped, one parametrised case per exclusion; the history regex narrowed to `#\d+` alone |
| T10 `test_an_unlisted_file_over_the_threshold_fails_and_a_listed_one_may_not_grow` (NAME NOT IN TREE until phase 2 plants it) | S7 | the threshold check removed; the per-file compare removed |
| T11 `test_ci_minutes_sum_each_leg_off_the_job_name_and_price_the_run` (NAME NOT IN TREE until phase 3 plants it) | S9 | leg read off `runner_name` instead of the job name (fixture names carry one, not the other); the 2×/10× factors swapped |
| T12 `test_the_summary_goes_to_the_step_file_when_set_and_names_no_path` | S5 | writing to stdout when `GITHUB_STEP_SUMMARY` is set; a machine path in the summary |
| T13 `test_the_trees_budgets_hold` | the gate, locally | none — this is the gate's local form, as `test_every_document_in_docs_is_under_the_ceiling_or_frozen` is; its value is that the sealer's run sees the tree's own budgets |
| T14 `test_the_workflows_run_the_checker_where_the_plan_says` (NAME NOT IN TREE until phase 3 plants it) | S5, S9 | the hygiene step without `--baseline`; the `budgets` job without `needs: pytest` or `actions: read` |
| T16 `test_a_malformed_row_or_a_missing_file_is_exit_2` | S11 | a malformed row skipped with exit 0; a missing file read as empty |

## Operational impact

- A new job in `test.yml` (`budgets`, ubuntu, under a minute) with `permissions: actions: read` declared on the job — the first explicit permission block in that workflow. A new step in `hygiene.yml` with no new scope.
- A pull request that edits `agents/*.md`, the injected skills, `CLAUDE.md`, `docs/*.md` or a listed test file may now need a `seal/budgets.md` edit in the same pull request, and a raise needs a `Budget raised:` line in the body. #929, #931 and #923 are the first pull requests to meet this; each one's frame cites the rows it moves.
- No new dependency; the checker is stdlib Python at the floor; `gh` is on the runner already.
- Nothing is removed and no default changes; a contributor's pull request that touches none of the measured files sees one more green step and one more green job.
