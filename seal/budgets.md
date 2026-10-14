# Budgets

<!-- What this repository holds its own size and speed to, one row per
budget. `.github/scripts/budget_check.py` measures each row on every pull
request and holds it to its ceiling from both sides; its docstring states the
band, the ratchet, the families and the `Budget raised:` line a raise needs in
the pull request body. A ceiling moves in the same pull request as the change
that moves the measurement. The `slow-file` and `docs-history` rows hold every
file their own table below does not list, and give the files it does list
their unit, slack and kind. The seconds ceilings are written in one set of
prices; `## Price level` says how the committed `.test_durations` prices
stand against them, and a refresh of that file restates it to the number the
checker names. A `bytes` row counts each CRLF as the one LF git stores, so a
checkout on any platform measures the same commit alike. -->

## Budgets

| Budget | Unit | Ceiling | Slack | Kind |
|---|---|---|---|---|
| preload:framer | bytes | 99089 | 2 % | gate |
| preload:scribe | bytes | 29554 | 2 % | gate |
| preload:sealer | bytes | 36113 | 2 % | gate |
| preload:smith | bytes | 106350 | 2 % | gate |
| preload:warden | bytes | 102229 | 2 % | gate |
| preload:claude-md | bytes | 9261 | 2 % | gate |
| suite-seconds | seconds | 7862 | 5 % | gate |
| slow-file | seconds | 120 | 10 % | gate |
| docs-history | lines | 0 | +0 lines | gate |
| ci-minutes:ubuntu | minutes | 15 | one-sided | gate |
| ci-minutes:windows | minutes | 59 | one-sided | gate |
| ci-minutes:macos | minutes | 32 | one-sided | gate |
| rounds-bytes | bytes | 142823 | one-sided | report |
| ledger-rereads | rows | 230 | one-sided | report |

## Price level

| Prices | Per mille |
|---|---|
| .test_durations | 1000 |

## Slow test files

| File | Seconds ceiling |
|---|---|
| tests/test_the_seal_is_taken_once_by_the_sealer.py | 1183 |
| tests/test_the_commit_gate_decides_at_the_commit.py | 1137 |
| tests/test_the_fixes_close_the_record.py | 482 |
| tests/test_chain_check_at_the_pull_request.py | 375 |
| tests/test_a_fix_of_a_fix_is_counted.py | 331 |
| tests/test_a_corrected_sentence_survives_elsewhere.py | 293 |
| tests/test_a_released_row_is_read_again_in_a_fragment.py | 217 |
| tests/test_the_record_is_generated.py | 188 |
| tests/test_no_shape_the_base_stops_reads_silent.py | 185 |
| tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py | 172 |
| tests/test_the_record_is_held_to_the_floor_and_the_depth.py | 165 |
| tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py | 165 |
| tests/test_a_record_precedes_the_fixes_it_commissions.py | 161 |
| tests/test_a_fragment_left_behind_is_named.py | 145 |
| tests/test_a_finding_id_is_a_bare_integer.py | 135 |
| tests/test_the_last_rounds_fixes_are_checked.py | 126 |

## Docs history lines

| File | Lines ceiling |
|---|---|
| docs/branch-and-release.md | 11 |
| docs/commit-review-gate-spec.md | 15 |
| docs/issues-and-milestones.md | 8 |
| docs/measuring-a-run.md | 2 |
| docs/one-root-by-lifetime.ko.md | 33 |
| docs/one-root-by-lifetime.md | 39 |
| docs/release-checklist.md | 11 |
| docs/review-chain-spec.md | 25 |
| docs/review-handoff-protocol.md | 22 |
| docs/round-record-spec.md | 17 |
| docs/the-agent-set.md | 0 |
| docs/the-broad-gate.md | 0 |
| docs/the-commit-gate-inside-git.md | 8 |
| docs/the-evidence-ledger.md | 4 |
| docs/the-pact.md | 0 |
| docs/the-reader-registry.md | 2 |
| docs/the-record-layout.md | 11 |
| docs/the-review-and-parity-arms.md | 3 |
| docs/worktree-guard-spec.md | 39 |
