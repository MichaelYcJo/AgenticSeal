# Implementation Plan: 1794383423-settle-reprints-every-earlier-judgment (#1481)

## Technical context

The tree as read at `18a7e18fb`.

The work builds on `skills/settle/scripts/settle.py` as #1281 and the
settles after it left it:

- `earlier_judgments` (`settle.py:1105-1200`) lists the deletions with one
  `git log -z --no-renames --full-history --diff-filter=D` of the ref. It
  then reads each plan with three calls inside one `try`: `git show`
  (`:1170`), `adding_commit` (`:1173`) and `version` (`:1176`). A failure of
  any of the three names that plan as not read and prints none of its rows.
- `adding_commit` (`:340-384`) builds its `git log` through
  `lib/gitcmd.py#argv` and takes one path. `notes` (`:625`) and
  `.github/scripts/publish_release_note.py:286` call it too.
- `version` (`:505-515`) asks `git tag --contains` for one commit. `notes`
  (`:632`) calls it too.
- `git_out` (`:487-502`) builds through `argv` with `--literal-pathspecs` and
  passes no standard input. `cat-file --batch` and `rev-list --stdin` need
  it, so the batched reads need a sibling of `git_out` that takes input, or
  an `input` parameter on it.
- `plan_rows` (`:1059-1096`) is the one reader of a plan's section, and the
  batched reading feeds it the same text.
- `main` (`:1873`) refuses `--draft` beside `--apply` (`DRAFT_WITH_APPLY`)
  and beside `--from`, and `--from` beside `--apply`. The new refusals follow
  the same pattern.

Constraints:

- The printed output for the plans read is byte-identical to today's
  (design G13). The #1281 cases pin it (design S5), so phase 1 changes no
  expected text.
- The tag read stays exact. The lowest `vX.Y.Z` tag that holds a commit is
  the lowest by number, as `version` reads it today. `git name-rev` and
  `git describe --contains` prefer the oldest tag by date, which is another
  fact, so neither is the tag read.
- A path goes to `cat-file --batch` on one line, as `<commit>^:<path>`.
  A work item id holds no newline, and `-z` already keeps a non-ASCII id
  whole in the deletion log (`tests/skills/test_settle.py:1484`).

Failure scenario of the chosen approach, six months out:

- **A kind that skips two settle periods is shown once.** Say a kind stands
  in one release, is absent from the next two settles' periods, and comes
  back. The default dry run shows only the new instance, and the settling
  session sees it recur only if it runs `--all-earlier`. Step 5 sends it
  there where the section the kind stands on was rewritten by an older
  settle. A kind that never reached a rewrite gives no such signal. G11
  found no such gap in the settle bodies it reads.
- **A settle that covers many releases makes the window large.** #1400
  covered eleven releases, and its plans' rows are 69,522 B alone. The
  section then shrinks again after the next two settles. It never grows
  with the number of releases in the history.
- **A stray removing commit takes a slot.** A commit that removes a plan
  outside a settle, such as a work item dropped by hand, counts as one of
  the two. The older-commit line says that more stand behind it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Read the plans of the two newest removing commits by default, name how many older removing commits were not read, read every one under `--all-earlier`, and batch the reads | The six-month scenarios above. Two is a number taken from the settle bodies design G11 reads, and a longer gap in a later record would argue for more. | **Chosen.** The bound is a fact git gives exactly (G2), and it keeps every recurrence the record shows (G11). At this tree it prints 48,176 B where today prints 247,730 B, in 0.51 s with 24 git calls (G13). The call count is the same at every bound. |
| A2. The plans of the newest removing commit alone | #1432's recurrence would have rested on one row (G11). | Rejected. It saves 41 KB at this tree and loses a case on record. |
| A3. The last N releases, by each plan's version tag, as the issue names first | A settle covers from one to eleven releases (G10), so a window of N releases cuts a settle's period at a point no settle chose. A long release run pushes the whole previous settle out of view. Choosing the plans needs every plan's tag first. | Rejected. The removing commit is the unit a settling session read whole as current, and its line already carries the `(#N)` step 11 names. |
| A4. Only the groups whose `judged against` document is one this settle writes, the issue's second candidate | Three paths carry 251 of the 316 rows (G14), so the filter saves little, and it still grows with every release. The groups a settle writes name `docs/` files, while the rows mostly name `skills/`. A filter by a cell's spelling hides a row the session would read as the same kind (#1281's A5). | Rejected. |
| A5. The section only behind a flag, and nothing by default, the issue's third candidate | Step 5 would have to send every settle to the flag, and the cost comes back. Without that, a recurrence across settles goes unseen at every settle whose session does not think to run it. That is the case #1281 was built for. | Rejected as the default. Kept as the way to reach past the window (A1). |
| A6. Keep the reading unbounded and batch it | It meets the time and the call count (0.70 s, 24 calls; G13). The output stays 247,730 B and grows by every release's rows, which fails the first *Done when* item. | Rejected. |
| A7. Shorten each earlier row, such as dropping the grounds | The output still grows with every release. The grounds cell is what tells the session whether two rows are one kind. | Rejected. |
| A8. The window's size as an argument, `--earlier N` | The settling session would pick a number with no grounds at hand. One fixed window and one flag that reads all cover the two uses. | Rejected. |
| A9. Batched readers beside today's `adding_commit` and `version` | Two readers of one fact can disagree on an edge, such as a tag that is not a commit, and the next fix lands in one of them (`skills/core/SKILL.md` *The rule a mechanism is kept against*, one source per fact). | Rejected. `adding_commit` calls `adding_commits`, and `version` goes for `versions`, which `notes` calls (design *Scope* item 5). |
| A10. Replace the structure: remove *The judgments earlier settles removed* | Each settle since #1281 used the section to name kinds that recurred across releases (design G11). Without it, each settle sees one period again, which is what #1281 fixed. | Rejected. The premise that keeps the section was checked: each settle body design G11 reads names a kind that recurred across releases. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 4, 5 and 6, with the reading still unbounded | `tests/skills/test_settle.py`: the #1281 cases at `:1371-1578` passing with no expected text changed (S5); `:1541` and `:1580` changed to replace the batched readers and to fail each in turn; S4 and S6 as new cases. `tests/github/test_publish_release_note.py`, for `adding_commit`'s other caller. Every other module that reads a path the phase changed, taken by `git grep -l` at the phase's base. `uvx ruff check` and `uvx ruff format --check` on the touched files. S4 is shown red against the per-plan reads, and S6 with its guard alone removed. The phase record says how. The suite is `unverified`, and the orchestrator's broad gate answers it. | bc5f349c6 |
| 2 | Design *Scope* items 1, 2, 3, 7, 8 and 9 | `tests/skills/test_settle.py`: S1, S2 and S3 as new cases, and the `EARLIER_HEADING` pins at `:3153-3158` passing. `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, `tests/test_censuses.py`, and every other module that reads a path the phase changed, taken by `git grep -l` at the phase's base. `chain-check`'s reading of this design's `## Rule changes`. `uvx ruff check` and `uvx ruff format --check` on the touched files. S1 is shown red with the bound alone removed. S7 is replayed in a `git clone --no-local` under the crafter's scratch directory, and its time, call counts and section bytes go into the phase record. The suite is `unverified`, and the orchestrator's broad gate answers it. | |

## Overlap with the release

Read: the spawn's list of the release's other open work items, #1498,
#1483, #1486, #1487 and #1488, and the issue bodies of #1486, #1488 and
#1482 (executed: `gh issue view`). No frame of theirs is committed on this
branch's base. #1483 changes `skills/verify/scripts/broad_gate.py` and its
test, and #1487 changes `evals/scripts/`: this work reads and changes
neither. #1488 changes literal-phrase asserts under `tests/text/` and
`tests/behaviour/`. A `git grep` of those directories for the passages this
work rewrites found no assert on them (executed), so #1488 does not meet
this work either.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1498 | `tests/censuses.py#_root_names`, which every tracked file's census run reads, this work item's records and new cases among them | #1498 | It carries the version move, and the spawn orders it first. This work's records hold no user path and no real identifier, so the census reads them the same before and after #1498. |
| #1486 | The durations `.github/scripts/durations_union.py` prices are the test ids, and this work adds cases to `tests/skills/test_settle.py` | either | No file is changed by both. `--stale-fails` runs only on the release pull request, and fails only past `STALE_SHARE`, 5 % of the union's cases unpriced (`durations_union.py:24-26`, `:70`). A handful of new cases does not cross it whichever merges first. |
| #1482 | `skills/settle/scripts/settle.py`: #1482 changes `load` and the loaders `plan_rows` calls, and this work changes `earlier_judgments`, `adding_commit`, `git_out`, `notes` and `main`, adds `git_run`, `decoded`, `versions`, `blobs` and `adding_commits`, and removes `version` | #1481 | The milestone orders #1481 first, and #1482's body says it builds after #1481. #1482 then moves the loaders of a reading that already reads fewer plans. |

## Operational impact

None for a deployer. `seal settle` gains `--all-earlier`, refused beside
`--apply` and `--draft`. The dry run's earlier section is shorter by
default, and its git calls stay fixed in number. It adds no dependency and
no environment variable. `--apply` and `--draft` print what they print
today. This pull request does not move the version; #1498 carries the move.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
