# 1792366315-the-wardens-real-false-finding-rate-is-unknown — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. A rule that must outlive this work item goes
to its home under `docs/` with the test that holds it, not here. -->

## Why this work exists

The warden's false-finding rate counted every real defect a case does not list
as false; this work records what each false row really is, re-grades the
committed sides under a suite that lists the recurring defects, and puts both
figures side by side.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The two `remark (fenced)` rows name no re-run command | `plan.md` phase 1, Verified by: "every `wrong`, `unclear` and `remark` row names its re-run command and result (S2)" / the two rows of phase 3's replay-1791382684-r2 run 0, rows 5 and 6, say "No command" and why | the code | Their class rests on where a line sat in the printed record, and that record is gone. The committed row keeps the `location:` line alone, so no command at any commit can show the fence (`evals/false-rows.md`, the two rows; `phases/phase-1.md`) |
| The finding's wording is marked once, not row by row | the spawn of phase 1: "the rows whose finding text is only in #971's first comment marked as such" / the Finding column's header and *How to read a row* say it once | the code | Every row is such a row: the committed sides keep only `location:` lines and the traces are gone (`spec.md` §*What the issue's step 1 stands on, opened*). A tag on all 74 rows would be the same word 74 times |
| `regrade` sits after the record's recomputation in `evals/README.md`, not beside `run --from-raw` | `spec.md` §*Scope* item 5: "`evals/README.md` (… `regrade` beside `run --from-raw`)" / the README names no `run --from-raw` (`git grep -n -e 'from-raw' b5f93d94 -- evals/README.md` exits 1, executed 2026-10-19); the paragraph follows the sentence that the test module recomputes the record, and the module docstring carries `regrade` beside `run --from-raw` | the code | There is no `run --from-raw` sentence in the README to sit beside; the docstring is where both subcommands are listed |
| Two of the comment's facts have moved | #971's first comment: "is in no agent-contract at 4d316179 or at 2dfa53a9 (read)", and "`gh issue view` (executed) shows #873 closed and #877 open" / `git cat-file -t 2dfa53a9` fails in this clone, and `gh issue view 877` shows it closed (executed 2026-10-19) | the classes stand, and both rows record the fact as found | Neither fact decides a class: the §19 rule is absent at 4d316179 alone, and #873 and #877 share a subject whichever is open (`evals/false-rows.md`, phase 3 seeded-4d316179 r1.F2 and seeded-ad447367 r1.F2) |

## Not verified

| Item | Who must answer |
|---|---|
| The finding wording of all 74 rows, which only #971's first comment holds now that the traces are gone | the repository owner, who wrote the comment; no command can re-check it |
| The full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through `broad-gate` |

## Not done

nothing

## Fed back into the spec

Inferred during implementation (phase 2), so a planner may overturn each.
`spec.md` §*Data & interfaces* describes `regrade` as replacing the truth
graders and their results and writing `suite_rev` and `suite_tree`. The
build adds four things to it:

- **The scores follow the truths.** Each run's `score` and `passed`, each
  case's `aggregates` and the side's `aggregates` are recomputed from the
  graders. Otherwise a regraded side would carry the scores of the grading
  it replaced. The formula is the one that reproduces every recorded value
  in #957's eight committed sides (executed 2026-10-19): a run's score is
  its passed graders' weight over every scored grader's, passing at the
  suite's threshold; a case's score and pass rate are its runs' means; the
  side's are its cases' means; and its cases passed are those whose every
  run passed.
- **The self-check covers the scores too.** A side whose own suite gives
  back its truth results but not its recorded scores, or whose recorded
  truth graders are not its suite's files, is refused like one whose rows
  do not reproduce.
- **A truth no report row can answer is refused**: a grader that is not a
  `contains` regex, one carrying a flag Python's `re` has no letter for,
  or a file with no front matter. Each is refused with exit 2, naming the
  case or the file.
- **The written side says it was regraded.** `specseal.regraded_from`
  holds the suite the side ran, so a regraded side cannot pass for one run
  on the new suite.
