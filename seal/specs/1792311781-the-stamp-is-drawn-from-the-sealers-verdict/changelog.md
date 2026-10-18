### Changed

- **The stamp is the sealer's, and it is drawn once per work item, at the
  commit of a `guarantee.md` reading `sealed` (#975).** Before this, the
  broad gate drew a stamp when its run went green, before the sealer had read
  anything, so a passing suite looked like finished work. Now git's
  `post-commit` reads the committed `guarantee.md`. Where its `Verdict:`
  reads `sealed`, it writes the stamp's values for your session and prints
  one line: ``specseal: the stamp for <id> is drawn at the end of this turn
  from <path>; where none appears, `seal-stamp --from <path>` draws it``. The
  `Stop` hook draws it after the turn's text, as before. `withheld` and
  `undecided` draw nothing. A re-seal after `withheld` draws the stamp then,
  and a work item that was already stamped draws nothing more, whatever
  commit the new verdict names. That holds in another clone of the same
  branch too, since its history shows the guarantee already read `sealed`;
  the one exception is a second clone amending the sealing commit itself,
  which draws the stamp again there. A squash or a cherry-pick of the
  guarantee onto another branch draws nothing either, and neither does a
  `sealed` whose `Target SHA` names a commit the branch does not hold. That
  `sealed` still counts as the work item's one stamp, so a later commit that
  corrects the row draws none either: the history cannot tell it from a
  stamp drawn before a rebase, and #976 carries that gap. The stamp's rows
  are what the records at that commit say: the audited commit and its branch,
  the base, the work item, the newest broad run, and the count of round
  records. The suite's counts are no longer on it.

  `seal-stamp --from <path>` is unchanged, and so are `hooks/sealer-stamp.py`
  and the `specseal-stamp/` directory. A clone whose git hooks slot is
  somebody else's (`core.hooksPath`, or a hook file the plugin did not
  write) draws no stamp and prints no line, and neither does a repository in
  local mode, where no commit carries `guarantee.md` (#976). There the pull
  request's check is what says the work item was sealed.

  The sealer's definition changed by one clause, so it was measured again
  against #969's reference on the same five-case suite:

  | Agent | Tree | Preload bytes | Tokens per tool call | Spend USD | Graders passed | Verdict |
  |---|---|---|---|---|---|---|
  | sealer | `1483d8ba` → `981b0acc`, one suite (`5c3e8119`) | 24,702 → 24,700 | 37,080.5 → 35,992.6 | 3.3898 → 3.5731 | 68 → 68 of 68 | pass |

  Each figure is read with `noninferiority.py#side_numbers` from #969's
  `evals/reference-sealer.json` and this work item's
  `evals/sealer-phase-4.json`; the verdict is `evals/sealer-phase-4.md`. Both
  sides are 10 runs, none cut short.
  (`1792311781-the-stamp-is-drawn-from-the-sealers-verdict`, #975)
- **The broad gate's run says `BROAD GATE PASSED` or `BROAD GATE FAILED`,
  and draws nothing (#975).** The `SEALED` and `NOT SEALED` heads are gone:
  the word is the sealer's verdict alone. A passing run prints the head, the
  report's rows as plain text and the line saying `broad-gate.md` is not
  committed, the same on a terminal and a pipe, with ASCII marks on a
  console that is not UTF-8. It writes no stamp values and draws no disc.
  Its refusals say `run` where they said `seal`, for example "there is no
  command to run". A script of yours that looks for a line starting `SEALED`
  in the gate's output should look for `BROAD GATE PASSED`.
  (`1792311781-the-stamp-is-drawn-from-the-sealers-verdict`, #975)
