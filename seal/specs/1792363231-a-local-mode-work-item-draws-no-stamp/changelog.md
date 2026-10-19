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
- **A `sealed` over a commit the work item's branch does not hold is refused
  at its commit, and its repair draws the stamp (#976).** Since #975, a
  `sealed` whose audited commit was not on the branch drew nothing. Yet once
  committed it counted as the work item's one stamp, so the corrected re-seal
  drew nothing either. Now the commit gate inside git refuses, in
  `pre-commit`, a commit that stages such a `guarantee.md` on the branch its
  `routing.md` declares. The refusal names the file, the commit the row
  names, the branch and HEAD, and the one way on: a new audit of the sealer
  at HEAD. It has no waiver. Before it prints, the hook leaves an empty file
  under `<git-common-dir>/specseal-stamp-refused/`. The earlier-run chain
  skips a `sealed` that file names, so the new audit, which keeps the
  refused verdict on its row, draws the stamp. In local mode the edit hook
  writes the same record and says one line naming the commit and the branch.
  Three limits are stated, none of which arises in this plugin's own flow.
  A wrong row committed where the gate does not run, under `--no-verify` or
  in a foreign hooks slot, or one an amend folds into the commit it audited,
  still leaves its work item with no stamp. A sealed item copied onto its
  branch in a second clone draws a second stamp there. A conflicted merge
  that brings in a side's `sealed` is refused, and `--no-verify` is its way
  on. `docs/the-review-record.md` §*The stamp* states each. On one machine,
  as medians of 11 commits, an ordinary judged commit takes 268 ms against 260 ms
  before, and one staging a `sealed` guarantee 310 ms against 283 ms.
  (`1792363231-a-local-mode-work-item-draws-no-stamp`, #976)
