### Changed

- **The pull request opens once the sealer has sealed, and CI runs then
  (#943).** The orchestration used to open a draft pull request at the end
  of the build, before round 1. CI then ran the suite on three platforms at
  every push of every round, and marking the draft ready ran it once more on
  a commit it had already run. Now the branch is pushed freely while it is
  built and reviewed, and a branch with no pull request runs nothing. The
  pull request opens ready after `guarantee.md` reading `sealed` is
  committed, with the body the sealer read. A run whose routing says
  `stop before the pull request` pushes nothing and hands the branch back
  committed and unpushed, as before. Where the work's risk is
  specific to one platform, the orchestrator runs
  `gh workflow run tests --ref <branch>` once the build's last phase closes
  and reads the result before its broad run. The stated limit: a defect that
  only one platform shows, in work nobody expected to be platform-specific,
  is found when the pull request opens, after the sealer. Its fix takes the
  existing repair path: a verifying round, the broad run again and the
  sealer again, and a repaired body is given to the open pull request with
  `gh api -X PATCH`. A repository whose people still open drafts is not refused,
  because `chain_check` still excuses a draft and `hygiene` re-runs it when
  the draft is marked ready.

  The owner section in `skills/code-review/orchestration.md` is now titled
  *Orchestrator: the pull request opens once the sealer seals, and a phase
  is re-run*, and every document citing it moved with it. The sealer is
  spawned before the pull request exists and reads its body from a file the
  prompt names. `broad-gate --record`'s last line now reads
  `CI reads HEAD, so commit it before you push`. The framer's route no
  longer labels the pull request `chain: reframed`: it runs before any pull
  request exists, and nothing read the label.

  The sealer's definition changed, so it was measured against #976's side
  on the same five-case suite:

  | Agent | Tree | Preload bytes | Tokens per tool call | Spend USD | Graders passed | Verdict |
  |---|---|---|---|---|---|---|
  | sealer | `f99ab3a9` → `95ab5fd0`, one suite (`5c3e8119`) | 24,690 → 24,505 | 35,600.6 → 35,906.3 | 3.3379 → 3.0371 | 68 → 68 of 68 | fail, rule 5 alone |

  The rule-5 fail is 0.9%, with total tokens down 10% and tool calls down
  from 81 to 72; the first side of the same change, 117 bytes longer, read
  35,060.4 per call. It is recorded as it reads and shipped, the owner's
  rule for a rule-5-only fail with every outcome grader holding.
  `evals/sealer-phase-3.md` and `evals/sealer-phase-3b.md` hold both sides.

- **`tests` no longer runs when a draft is marked ready, and a newer push
  cancels the older run (#943).** `.github/workflows/test.yml` dropped
  `ready_for_review` and `converted_to_draft`: nothing in it reads draft
  state, so those events only re-ran the suite on the same commit.
  `hygiene.yml` keeps them, because `chain_check.py` reads draft state. Both
  workflows declare a concurrency group per workflow and pull request, and a
  newer pull-request run cancels the one still in progress. A run that is
  not a pull request's, such as a push to `main`, takes a group of its own
  (`github.run_id`), so it is never held pending or cancelled.
  `tests/test_ci_gives_the_checks_what_they_need.py` requires the draft
  events exactly where a workflow runs `chain_check.py`, and holds the
  concurrency block.
  (`1792367880-ci-runs-once-when-the-pull-request-opens`, #943)
