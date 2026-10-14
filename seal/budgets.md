# Budgets

<!-- What this repository holds its own size and speed to, one row per
budget. `.github/scripts/budget_check.py` measures each row on every pull
request and holds it to its ceiling, from both sides where the reading is
the tree's own; its docstring states the band, the ratchet, the families and
the `Budget raised:` line a raise needs in the pull request body. A ceiling
moves in the same pull request as the change that moves the measurement. The
`slow-file`, `docs-history` and `unenforced` rows hold every file their own
table below does not list, and give the files it does list their unit, slack
and kind. `enforced-unresolved` counts the `Enforced by:` targets in the rule
files that do not resolve, and `unenforced` a rule file's rule paragraphs
with no `Enforced by:` line or one saying `nothing — <why>`; a rule that
gains its test lowers its file's row in the same pull request.
A row read off one run — a CI run's minutes, or `.test_durations` — is
`one-sided`: its ceiling is 1.3 times its reading, rounded up, every test
file whose reading times 1.3 reaches the 120 s threshold is listed, and the
release lowers these ceilings from the trend line. The seconds ceilings are
written in one set of prices; `## Price level` says how the committed
`.test_durations` prices stand against them, and a refresh of that file
restates it to the number the checker names. A `bytes` row counts each CRLF
as the one LF git stores, so a checkout on any platform measures the same
commit alike. -->

## Budgets

| Budget | Unit | Ceiling | Slack | Kind |
|---|---|---|---|---|
| preload:framer | bytes | 95730 | 2 % | gate |
| preload:scribe | bytes | 29554 | 2 % | gate |
| preload:sealer | bytes | 36113 | 2 % | gate |
| preload:smith | bytes | 101344 | 2 % | gate |
| preload:warden | bytes | 102229 | 2 % | gate |
| preload:claude-md | bytes | 9126 | 2 % | gate |
| suite-seconds | seconds | 9185 | one-sided | gate |
| slow-file | seconds | 120 | one-sided | gate |
| docs-history | lines | 0 | +0 lines | gate |
| ci-minutes:ubuntu | minutes | 15 | one-sided | gate |
| ci-minutes:windows | minutes | 59 | one-sided | gate |
| ci-minutes:macos | minutes | 32 | one-sided | gate |
| rounds-bytes | bytes | 142823 | one-sided | report |
| enforced-unresolved | targets | 0 | +0 | gate |
| unenforced | rules | 0 | +0 rules | gate |

## Price level

| Prices | Per mille |
|---|---|
| .test_durations | 1000 |

## Slow test files

| File | Seconds ceiling |
|---|---|
| tests/test_the_seal_is_taken_once_by_the_sealer.py | 1538 |
| tests/test_the_commit_gate_decides_at_the_commit.py | 1479 |
| tests/test_the_fixes_close_the_record.py | 627 |
| tests/test_chain_check_at_the_pull_request.py | 488 |
| tests/test_a_fix_of_a_fix_is_counted.py | 431 |
| tests/test_the_record_is_generated.py | 245 |
| tests/test_no_shape_the_base_stops_reads_silent.py | 241 |
| tests/test_one_heredoc_shape_is_data_to_the_commit_gate.py | 224 |
| tests/test_the_record_is_held_to_the_floor_and_the_depth.py | 215 |
| tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py | 215 |
| tests/test_a_record_precedes_the_fixes_it_commissions.py | 210 |
| tests/test_a_fragment_left_behind_is_named.py | 189 |
| tests/test_a_finding_id_is_a_bare_integer.py | 176 |
| tests/test_the_last_rounds_fixes_are_checked.py | 164 |
| tests/test_the_chain_goes_back_to_its_framer.py | 147 |
| tests/test_a_note_closes_once_at_the_runs_end.py | 142 |
| tests/test_settle_reads_before_it_removes.py | 140 |
| tests/test_the_guard_asks_once_per_session.py | 128 |

## Docs history lines

| File | Lines ceiling |
|---|---|
| docs/branch-and-release.md | 9 |
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
| docs/the-pact.md | 0 |
| docs/the-reader-registry.md | 2 |
| docs/the-record-layout.md | 8 |
| docs/the-review-and-parity-arms.md | 3 |
| docs/worktree-guard-spec.md | 39 |

## Unenforced rules

| File | Rules ceiling |
|---|---|
| CLAUDE.md | 7 |
| CONTRIBUTING.md | 21 |
| agents/framer.md | 35 |
| agents/scribe.md | 3 |
| agents/sealer.md | 21 |
| agents/smith.md | 11 |
| agents/warden.md | 17 |
| docs/branch-and-release.md | 24 |
| docs/commit-review-gate-spec.md | 20 |
| docs/issues-and-milestones.md | 23 |
| docs/measuring-a-run.md | 3 |
| docs/one-root-by-lifetime.ko.md | 38 |
| docs/one-root-by-lifetime.md | 38 |
| docs/release-checklist.md | 8 |
| docs/review-chain-spec.md | 52 |
| docs/review-handoff-protocol.md | 42 |
| docs/round-record-spec.md | 43 |
| docs/the-agent-set.md | 6 |
| docs/the-broad-gate.md | 5 |
| docs/the-commit-gate-inside-git.md | 9 |
| docs/the-pact.md | 1 |
| docs/the-reader-registry.md | 4 |
| docs/the-review-and-parity-arms.md | 8 |
| docs/worktree-guard-spec.md | 43 |
| skills/agent-contract/SKILL.md | 2 |
| skills/audit/SKILL.md | 6 |
| skills/build-fix/SKILL.md | 4 |
| skills/checkpoint/SKILL.md | 4 |
| skills/code-review/SKILL.md | 27 |
| skills/code-review/orchestration.md | 41 |
| skills/commit-pr-convention/SKILL.md | 24 |
| skills/confidence-check/SKILL.md | 6 |
| skills/config/SKILL.md | 13 |
| skills/gap-analysis/SKILL.md | 10 |
| skills/implement/SKILL.md | 26 |
| skills/implement/orchestration.md | 41 |
| skills/learn/SKILL.md | 4 |
| skills/legacy-parity/SKILL.md | 2 |
| skills/parity-setup/SKILL.md | 7 |
| skills/preset-setup/SKILL.md | 6 |
| skills/security-audit/SKILL.md | 1 |
| skills/settle/SKILL.md | 28 |
| skills/update/SKILL.md | 11 |
| skills/verify/SKILL.md | 42 |
| skills/writing-style/SKILL.md | 40 |
| templates/claude-md-block.md | 5 |
| templates/config.md | 37 |
| templates/sdd-plan.md | 1 |
| templates/sdd-questions.md | 5 |
| templates/sdd-round.md | 1 |
| templates/seal-README.md | 2 |
