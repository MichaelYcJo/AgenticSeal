# 1792459424-docs-states-the-current-rule-in-one-read — review round 4

target: 63013972, fixes 5ddc6b61..63013972

## Findings

None this round.

## Confirmations

confirms: round-3#1
The close at fcb7e8f0 holds (executed). This round timed `NEAR` at
63013972 in a child process with a 20-second timeout, on lines that hold
no label:

- 5000 `#` and 20,000 `#`: 0.0004 s and 0.0017 s.
- Mixed runs of 5000 to 10,000 characters: `# `, `* `, `*_`, `-#>|`, `1.`,
  `1`, `[ ]`, `#*` and `# *`, each under 2 ms.
- 64 `#` followed by ` check: x`: still a match.

Round 3 measured the old `#{1,6}` past 10 seconds at 30 hashes. The fix
answers 20,000 in under 2 ms, so it removes the exponential path. It does
not merely move it.

`bin/rules --check` reads 240 lines and exits 0, so no line in the tree is
answered differently. `fcb7e8f0` changes `.github/scripts/rules.py`, which
the finding's `location:` names.

What is left is quadratic, as the answer says:

- a run of `*`, which both the bullet alternative and the emphasis after
  the group can take: 0.285 s at 5000;
- a run of spaces: 0.176 s at 5000.

Both need a shown line thousands of characters long to cost a fraction of
a second, and both still answer, so neither is a finding.

The fix pass also checked that `[0-9]{1,9}[.)]` cannot split ambiguously,
because every piece must end at a `.` or `)`. That holds on the pattern
(read, `.github/scripts/rules.py:60`). This round measured it too: 5000
digits and 5000 `1.` pieces each answer in under 1 ms (executed).

confirms: none
The new case, `test_a_long_run_of_markup_with_no_label_is_answered_at_once`,
reads as code (read,
`tests/test_the_rules_command_reads_each_rule_off_its_test.py:440-459`).

- **The timeout lives in the child.** The child process holds the
  10-second timeout, and `subprocess.run` kills it on expiry. The run then
  raises `TimeoutExpired`, so the case fails at 10 seconds rather than
  stalling the run.
- **Arguments go as a list.** With no shell, the `|`, `>` and space marks
  reach the child as written on every platform.
- **The encoding sweep's refusal is respected.**
  `encoding="utf-8", errors="replace"` replaces `text=True`, which the sweep
  refuses, and the decoded stderr still reaches the assertion message.
- **Red before green.** The fix pass reports the `#` row timed out against
  3b01852d's `#{1,6}`, and that `mutation-check` reproduced the failure.
  This round did not re-run the old pattern. Round 3's executed timing
  (past 10 s at 30 hashes) means 64 hashes cannot finish inside the case's
  10 seconds.
- **What it does not pin.** The case asserts the answer comes in time. It
  does not assert linear time, so a quadratic pattern passes it. That
  matches its docstring's claim, which is about exponential time, and it is
  no finding.

The rules module and the encoding sweep module pass, 212 cases. `ruff
check` and `ruff format --check` pass on both changed files (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 63013972: `unverified` | the branch | the orchestrator, at `broad-gate` once the rounds settle |
| Whether "two hook processes racing for one record" is behaviour the tree cannot observe, carried from round 1 unanswered | `docs/commit-review-gate-spec.md`, the backlog row closed on *Registration* | the framer, through the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 -I probe/near_time.py <clone>` (`NEAR` at 63013972, each line in a child with a 20 s timeout) | 20,000 `#` 0.0017 s; mixed markup runs under 2 ms; 5000 `*` 0.285 s; 5000 spaces 0.176 s; 64 `#` before `check: x` still matches |
| `bin/rules --check` | exit 0, all 240 check lines in 61 rule files hold |
| `bin/test` over the rules module and `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | 212 passed |
| `uvx ruff check` and `uvx ruff format --check` over `rules.py` and the rules test module | all checks passed, 2 files already formatted |
