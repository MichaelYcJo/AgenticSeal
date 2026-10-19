### Fixed

- **A work item in local mode draws its stamp (#976).** The stamp was
  queued only at the commit of a `guarantee.md` reading `sealed`. In local
  mode the `seal/` root sits under the git directory, where no commit
  carries it, so a local-mode work item never drew one. A new `post-edit`
  hook, `sealer-stamp-queue`, now queues the stamp at the `Write` or `Edit`
  that leaves a local root's `guarantee.md` reading `sealed`, and prints the
  line `post-commit` prints in shared mode, naming the queued file and
  `seal-stamp --from`. The `Stop` hook draws it at the end of the turn, as
  before. It is queued once per work item, and only where the audited
  commit is on the branch the work item's `routing.md` names, so editing a
  guarantee sealed long ago draws nothing. Every other file edit is passed
  over on its path alone, before anything is loaded or any `git` runs.
  Shared mode is unchanged. A local guarantee that arrives by a shell write
  or `seal import` queues nothing.

  The sealer's definition lost one word, `committed`, since a local-mode
  verdict is never committed. So it was measured again against #975's
  phase-4 side on the same five-case suite:

  | Agent | Tree | Preload bytes | Tokens per tool call | Spend USD | Graders passed | Verdict |
  |---|---|---|---|---|---|---|
  | sealer | `981b0acc` → `f99ab3a9`, one suite (`5c3e8119`) | 24,700 → 24,690 | 35,992.6 → 35,600.6 | 3.5731 → 3.3379 | 68 → 68 of 68 | pass |

  Each figure is read from `evals/sealer-phase-5.md`, which compares #975's
  `evals/sealer-phase-4.json` with this work item's
  `evals/sealer-phase-5.json`. Both sides are 10 runs, two of each case, and
  neither was cut short.
  (`1792363231-a-local-mode-work-item-draws-no-stamp`, #976)
- **A `sealed` the plugin refused no longer takes the place of the stamp it
  never drew (#976).** Since #975, a `sealed` whose audited commit was not on
  the branch drew nothing, yet it still counted as the work item's one
  stamp, so the corrected re-seal drew nothing either. Now the refusing hook
  leaves an empty file under `<git-common-dir>/specseal-stamp-refused/`, and
  the readers that hold "once per work item" skip a verdict this clone
  refused, so the repair draws the stamp. A record is written only where the
  verdict cannot have been stamped in another clone. The commit must
  introduce the verdict as a plain commit, not an amend, a rebase, a
  cherry-pick or a merge. No other branch of the clone may hold a `sealed`
  guarantee for the work item, as one does after a `merge --squash`, a
  `cherry-pick -n` or a `checkout` of the work item's directory. And its target must have no
  patch-equivalent copy in the history. The gap stays where no record can
  settle it: a repair committed in another clone, a refusal no hook judged,
  a verdict a rewrite introduced, one brought from another branch, a target
  with a copy in the history, and a clone whose reflog is off. Each is stated in `docs/the-review-record.md` §*The stamp*.
  (`1792363231-a-local-mode-work-item-draws-no-stamp`, #976)
