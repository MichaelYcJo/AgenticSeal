# Implementation Plan: 1793591507-the-settle-reads-what-earlier-settles-judged

## Technical context

The work builds on `skills/settle/scripts/settle.py` as #1292 left it at
`47ec17cb8`:

- `judgments` (`settle.py:972`) reads each released plan from the working
  tree through `rules.reader().gfm_lines`, `rules.headings`,
  `rules.section_lines` and `config.gfm_table` under `JUDGMENTS_HEADER`
  (`settle.py:202`). It names a near heading with `NEAR_JUDGMENTS`
  (`settle.py:204`).
- `survey` (`settle.py:1171`) puts its result in `found["judgments"]`.
  `report` prints it under `JUDGMENTS_HEADING` (`settle.py:799`) at
  `settle.py:1509` to `:1530`, before the named directories and the removal
  list.
- `adding_commit` (`settle.py:315`), `version` (`settle.py:484`),
  `PULL_REQUEST_RE` (`settle.py:312`) and `git_out` (`settle.py:468`, every
  pathspec literal) are the exact readers #1139 built. The earlier reading
  calls them and adds no second parser of a tag or a `(#N)`.
- `tests/skills/test_settle.py:1074`,
  `Test_main::test_the_judgments_are_printed_by_the_document_each_stands_on`,
  pins today's block exactly, from `JUDGMENTS_HEADING` up to
  `REMOVES_HEADING`. Its fixture's history deletes no plan, so the case
  passing unchanged is the pin for design S2.

Constraints:

- The reading runs on `--released-at`, the ref the dry run already resolves.
  It adds no argument and asks no `gh`. Shared mode still asks `gh` only in
  `--apply` (`skills/settle/SKILL.md` *In local mode*, the bullet *What
  released means*).
- The query has to be a non-merge diff. A `git log` without `-m` shows no
  diff for a merge, so a deletion is listed at the squash commit that made
  it. `<commit>^` is that commit's only parent. Each of the five deleting
  commits on `origin/main` has one parent and a subject ending in its
  `(#N)`, from `(#1098)` to `(#1269)` (executed: `git rev-list --parents
  -n1` and `git log -1 --format=%s` on each; design G8).

Failure scenario of the chosen approach, six months out. The section grows
by every release's rows: 74 rows now (G8). At the 0.27.x rate of about 40 a
release, it holds several hundred rows six releases on. The settling session reads all of
them at every settle, and a rows-per-document scan is the only aid the
script gives it. That cost is the owner's decision of 2026-11-02 that no
count or window decides judgment (design G4). The way out is the settle's
own rewrites: a kind that keeps recurring gets a section that answers it,
and its later rows stop coming. Two smaller failures are limits:

- A shallow clone holds no history past its boundary, so the section lists
  less there and says nothing about it.
- A plan deleted by a merge commit's own resolution is not listed, because
  no non-merge commit deletes it.

The skill states both as limits, and no guard covers them.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Read every `seal/threads/<id>/frame/plan.md` a commit on `--released-at` deleted, at the parent of that commit, through the same table reader, and print its rows with the release its adding commit's lowest tag names and the removing commit's `(#N)` | The section grows each release (*Technical context*). A shallow clone or a history rewrite hides earlier rows with no line saying so. | **Chosen.** Every fact is git's output or a row the existing reader returns (design G2, G11, G12). The history is the tree's own (G3). The probe read all 20 plans that hold the section, at their deleting commits' parents (G8). |
| A2. Read earlier settles' pull request bodies, under *The judgments*, through `gh` | A body names only what its settle judged to recur within its own release. A kind each release judged once never reaches a body, so the issue's symptom stays (G5, G6). #1182's body holds no such section (G7). No form says which pull request is a settle: the head branches and titles follow a convention, such as #1214's `chore/settle-0.26.0-and-0.27.0`. The body is prose, so the script could only copy it. The dry run would ask `gh` in shared mode for the first time. | Rejected. The removing commit's `(#N)`, printed by A1, leads the settling session to that body when a row calls for it. |
| A3. Keep a ledger under `seal/`, such as a judgments file each settle appends to | The ledger is a copy of the history kept beside the tree. It drifts when a settle forgets to append, and nothing reads it against git. | Rejected by `skills/core/SKILL.md` *The rule a mechanism is kept against* (G3). |
| A4. Replace the removal: `--apply` keeps each `frame/plan.md`, or moves the plans into an archive directory | The tree accumulates records whose role ended at the release (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). Every corpus reader under `tests/` and `chain_check.py` then reads them. The archive is a second copy of what git holds. | Rejected. The premise that keeps the removal was checked: git holds every removed plan whole at its deleting commit's parent (G8, `executed`). |
| A5. Print only the earlier rows whose `Judged against` cell, or whose first backticked path, matches a current row's | In 74 earlier rows, one section is spelt in four ways (G9). A filter by spelling hides a row the settling session would read as the same kind, which is the result `skills/core/SKILL.md` calls the worst a script can give. | Rejected. |
| A6. Count the rows per cell across releases, or flag a kind seen in N releases | A count of cells measures spelling, not kind (G9). A trigger at N recurrences is the threshold the owner ruled out on 2026-11-02 (G4). | Rejected. |
| A7. Carry each earlier work item's round count, from `git ls-tree <commit>^ seal/threads/<id>/trail/rounds/` | A third git read per plan, for a number the earlier settle already weighed for its own release. The rows' own grounds cells name the rounds where they mattered (G10: "Past the third finding round"). | Rejected for this work. A later settle that finds it needs the count can ask for it with this reading's coordinates in hand. |
| A8. Replace today's block: merge the earlier rows into the current groups under one heading, each member marked with its release | Every run with an earlier settle changes today's block. Exact-cell merging still splits one kind across spellings (G9). Today's exact pin (`tests/skills/test_settle.py:1074`) would have to be rewritten, and the issue asks that a run with no earlier settle print what it prints today. | Rejected. A separate section keeps today's block and its pin as they stand. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* items 1 to 8 | `tests/skills/test_settle.py` (S1 to S5, and the S2 pin at `Test_main::test_the_judgments_are_printed_by_the_document_each_stands_on` passing unchanged); `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_settle_applies_rule_changes_in_place.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/hooks/test_launch.py` and `tests/test_censuses.py` (the real-identifier census reads this work item's records and the new fixtures); every other module that reads a path the phase changed, taken by `git grep -l` at the phase's base (contract rule 2); `bin/seal layout --check tests`; `uvx ruff check` and `uvx ruff format --check` on the touched files. Each negative case (S3, S5) is shown red with its named guard alone removed, and the phase record says how. S6 is replayed in a `git clone --no-local` under `<scratchpad>/1793591507-the-settle-reads-what-earlier-settles-judged/`, and its counts are recorded. The suite is `unverified`, and the orchestrator's broad gate answers it. | |

## Operational impact

None for a deployer. The dry run makes one `git log` of the ref, and three
git reads for each earlier plan: the `git show`, the `adding_commit` log
and the `git tag --contains`. It adds no dependency, no environment
variable and no argument. `--apply`, `--draft` and `--from` are unchanged.

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-02 | The design's G4 cites the owner's no-cap decision at #1289's body and #1288's *Done when*, where the framer had it only through the spawn prompt | The decision was written into both issues the same day; a coordinate lets the sealer and the settle read it rather than take the orchestrator's word | `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* |
