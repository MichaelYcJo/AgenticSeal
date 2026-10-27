# Review round 4: 1793057292-agent-lifetime-and-process-archive

target: d44cfb2b, fixes 17b287af..d44cfb2b

Round 4 is the verifying round for round 3. Round 3 opened two `should`
findings, and the fix pass closed both `fixed`: finding 1 in 31e0d5b1 and
finding 2 in 6efbbaa8. d44cfb2b writes the two verdicts and answers into
`rounds/round-3.md`. This round read the diff `17b287af..d44cfb2b` in the
worktree the spawn named. It made no clone, because it ran no probe that
changes a file. No `seal/parity.md` is declared, so no parity comparison
applies. `guarantee.md` still describes the sealer's earlier audit. It is
the sealer's file, rewritten at its next run, so this round did not judge
it.

Carried from round 3 and not re-established: the line coordinates of
finding 2's grounds and the release checklist's sections. This round
re-opened each one it relied on. It re-ran the CI read itself:
`gh run view 40434089606` printed `17b287af`, completed, `success`, with
`release-report` skipped. Every verdict below was re-derived at
`d44cfb2b`.

## Findings

No finding opened this round.

## Confirmations

confirms: round-3#1
Round 3 found that `overview.md` and `phases/phase-5.md` called `236a596d`
"the head before phase 5". The answer claims both places now name the three
record commits between them. `git log --name-only 236a596d..1718924d^`
prints `f8408d5e`, `085530de` and `8eca5d5d`. They change only `spec.md`,
`plan.md`, `questions.md`, `guarantee.md`, `broad-gate.md`, `changelog.md`
and `overview.md` of this work item. `overview.md:25`, row 1 of *Not
verified*, now names those three commits and says they change only this
work item's records. `phases/phase-5.md:94-95` names the `236a596d` broad
run "with the three record commits after it and before this phase".
`git grep "head before phase"` finds only `rounds/round-3.md`. The fix also
rewrote row 3 (`overview.md:27`), the row for `1718924d`. That row now says
run 40434089606 at `17b287af` answered the Linux and Windows cases, and it
leaves the full suite and the lint and format check to the broad run. The
run's jobs bear this out: ubuntu, the three macOS groups and the four
Windows groups passed, and `17b287af` contains `1718924d`. The row's
"passed every leg" reads against the `pytest` legs, the same way row 2's
does for run 40430474904. The job that was skipped, `release-report`, runs
no case. `phases/phase-5.md:96-97` still says phase 5 added a row for "the
branch's next `tests` run". That is a record of what phase 5 wrote, and
round 3 settled that a phase record keeps that history. Executed for the
log, the grep and the run, read for the rest.

confirms: round-3#2
Round 3 found that the `release-report` job's comment cited
`docs/release-checklist.md` *2. Gather, bump* as where the table is read.
At `d44cfb2b`, `.github/workflows/test.yml:246` cites *5. The release pull
request*. That heading is `docs/release-checklist.md:160`. Its paragraph
*Read the release table before the merge* at lines 172-178 is the
instruction the comment points to. 6efbbaa8 changes only that line. The
answer enumerates the class as section citations under `.github/` and
names four others. `git grep` for a backticked file followed by an
italicised section under `.github/` finds six others: the four the answer
names, `rules.py:19` and `tracker_labels.py:103`. `rules.py:19` cites
`skills/settle/SKILL.md` *A rule has one shape*, which is that file's
heading at line 94. `tracker_labels.py:103` cites a work item's `spec.md`
*Judgments* 11 as history. Neither script differs from the base
`5bab081e`, and neither cites the checklist. The answer's count of four
misses them, and the class it was enumerating holds. The two other
citations of *2. Gather, bump*, at `CONTRIBUTING.md:383` and
`docs/the-record-layout.md:42`, cite the gather command, which section 2
holds. Three modules that read `.github/workflows/test.yml` pass
(`tests/test_ci_gives_the_checks_what_they_need.py`,
`tests/test_arm_check.py`,
`tests/test_a_unit_is_bounded_where_a_parser_decides.py`). Executed for
the grep and the run, read for the rest.

confirms: none
d44cfb2b changes only `rounds/round-3.md`. It turns the two `verdict:`
lines from `open` to `fixed 31e0d5b1` and `fixed 6efbbaa8`, and it fills
the two `answer:` lines. Each `fixed` commit touches a path named on its
finding's `location:` line: 31e0d5b1 touches `overview.md` and `phases/phase-5.md`,
and 6efbbaa8 touches `.github/workflows/test.yml`. Read with
`git diff 17b287af..d44cfb2b`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `d44cfb2b`. This round ran none of the three. The broad run at `236a596d` comes before phase 5's code commit `1718924d` | `broad-gate.md`, `overview.md` *Not verified* row 3 | the orchestrator, by `broad-gate --base release/v0.22.4 --record` now that this round leaves nothing open, and the sealer's spawn after it |
| The pull request body's sentences the sealer named. The body is the orchestrator's file and is not in the tree | `guarantee.md` *What must change*, item 2 | the sealer, at its next audit |
| Q1, no archive files for 0.22.0 to 0.22.3, and Q2, a merge and never a rebase, both on their defaults | `questions.md` Q1, Q2 | the owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `git log --format='%h %s' --name-only 236a596d..1718924d^` | `f8408d5e`, `085530de`, `8eca5d5d`, each changing only this work item's files under `seal/specs/` |
| `git grep -n "head before phase"` | `rounds/round-3.md` lines 26, 37 and 67 only |
| `gh run view 40434089606 --json headSha,status,conclusion,jobs` | `17b287af`, completed, `success`; every `pytest` leg, lint, both `arm-check-grammar` legs and `durations` succeeded; `release-report` skipped |
| `git grep -n -E` for a backticked `.md` path followed by an italicised section, over `.github` | 7 lines: `test.yml:246` and the six named in the round-3#2 entry |
| `git diff --quiet 5bab081e HEAD -- .github/scripts/tracker_labels.py .github/scripts/rules.py` | exit 0 |
| `bin/test tests/test_ci_gives_the_checks_what_they_need.py tests/test_arm_check.py tests/test_a_unit_is_bounded_where_a_parser_decides.py -q -p no:xdist` | exit 0, 118 passed and 2 skipped |
