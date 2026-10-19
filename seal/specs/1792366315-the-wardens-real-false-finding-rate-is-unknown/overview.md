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
| Two of the comment's facts have moved | #971's first comment: "is in no agent-contract at 4d316179 or at 2dfa53a9 (read)", and "`gh issue view` (executed) shows #873 closed and #877 open" / `git cat-file -t 2dfa53a9` fails in this clone, and `gh issue view 877` shows it closed (executed 2026-10-19) | the classes stand, and both rows record the fact as found | Neither fact decides a class: the §19 rule is absent at 4d316179 alone, and #873 and #877 share a subject whichever is open (`evals/false-rows.md`, phase 3 seeded-4d316179 r1.F2 and seeded-ad447367 r1.F2) |

## Not verified

| Item | Who must answer |
|---|---|
| The finding wording of all 74 rows, which only #971's first comment holds now that the traces are gone | the repository owner, who wrote the comment; no command can re-check it |
| The full suite, the repository-wide lint and the typecheck over this branch | the orchestrator, through `broad-gate` |

## Not done

nothing

## Fed back into the spec

none
