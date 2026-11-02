# Review round 1: 1793591507-the-settle-reads-what-earlier-settles-judged

```seal
target: e59ec5995 against 47ec17cb8
```

The target is the branch's diff against `origin/release/v0.28.0` at the
branch point `47ec17cb8`. The release branch has moved since, with #1153;
this round reads nothing past the branch point. No earlier round exists, so
no fact is carried from one. Three facts are carried from the build's
records and not re-established here: the frame's G19 parse of
`## Rule changes`, the phase's `log.follow` measurement behind dropping
`--no-follow`, and the phase's mutation scores other than the two survivors
this round weighs.

## Findings

### 1. A removed plan whose work item id holds a non-ASCII character is neither read nor named as not read

```seal
severity: should
location: `skills/settle/scripts/settle.py:1111-1138`, `tests/skills/test_settle.py:1421`
evidence: executed `python3 test_tmp_quotepath.py`, `bin/test tests/skills/test_tmp_round1.py -q -p no:xdist`
```

Why it matters: `earlier_judgments` reads the history with `git log
--name-only` and no `-z` (`settle.py:1112-1123`). Under git's default
`core.quotePath`, a path holding a byte above ASCII is printed in double
quotes with octal escapes. `REMOVED_PLAN_RE.fullmatch` then fails on it
(`settle.py:1133`), and the loop skips the line with no word
(`settle.py:1134-1135`). The plan's rows never print, and no `not read:`
line names it. The work item directory form is
`seal/threads/<unix-epoch-seconds>-<slug>/` (`skills/implement/SKILL.md:324`),
and nothing limits the slug to ASCII. A repository whose records are written
in Korean can hold such an id. The released reading, `work_items(records)`,
lists directories from the file system and reads that same work item under
*The judgments*. The history reading drops it once a settle removes it, so
the kind the issue wants seen across releases goes missing exactly for those
work items. `skills/core/SKILL.md` *The rule a mechanism is kept against*
says a script "names as not read a line or a file that looks like one of
its form's and is not one". This loop does neither. The same file reads
every other path listing with `-z`: `settle.py:1422`, `:1446` and `:1452`.

Executed, in a `git clone --no-local` of `e59ec5995` under the scratchpad.
A probe repository held two plans, `1700000001-ascii` and `1700000002-` plus
U+C815 U+B82C, both added, tagged and deleted. `earlier_judgments` returned
the ASCII work item's group alone and an empty `unread`. `git log` listed the
second path as `"seal/threads/1700000002-\354\240\225\353\240\254/frame/plan.md"`.
The second case below, run through the module's fixtures, failed against
the unchanged code. With the fix below applied, both cases and all 156
cases of `tests/skills/test_settle.py` passed. `bin/seal settle
--released-at origin/main` printed output identical to the unchanged
code's on this repository's history.

```python
    try:
        listed = git_out(
            root,
            "log",
            "-z",
            "--no-renames",
            "--full-history",
            "--no-show-signature",
            "--diff-filter=D",
            "--name-only",
            "--format=%x01%H %h %s",
            ref,
            "--",
            SPECS,
        )
    except RuntimeError as failed:
        return [], [("", str(failed))]
    deleted, seen = [], set()
    commit = None
    # `-z` ends each path with a NUL and quotes none, whatever
    # `core.quotePath` says; a commit's field opens with U+0001, which no
    # path under SPECS starts with.
    for line in listed.split("\0"):
        line = line.lstrip("\n")
        if line.startswith("\x01"):
            commit = line[1:].split(" ", 2)
            continue
```

The rest of the loop is unchanged. The case, in `Test_main`
(`tests/skills/test_settle.py`), was run red against `e59ec5995` and green
with the fix above:

```python
    def test_a_removed_plan_of_a_non_ascii_id_is_read(self, repo, capfd):
        """#1281. A work item id may hold any character the slug takes, and
        git quotes such a path unless `-z` is given, so the history is read
        with `-z`. Seen red against the reading without it."""
        old = "1700000001-정렬"
        plan = judgments_plan([("2026-10-01", "ended the rounds", "y", "z")])
        write(repo / "seal" / "threads" / old, "frame/plan.md", plan)
        commit(repo, "the old work item (#3)")
        git(repo, "rm", "-rq", f"seal/threads/{old}")
        commit(repo, "settle 0.1.0 (#7)")
        write(repo / "seal" / "threads" / "1700000002-new", "routing.md", "# new\n")
        commit(repo, "released new")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert f"\n    {old}  " in text, text
```

```seal
verdict: fixed 0e45a9122
answer: The finding holds. Before taking the paste-ready reading, its parse was checked against git's own output (executed: `git log -z --name-only "--format=%x01%H %h %s"` over `origin/main`, read through `od -c`): each commit's field ends in a NUL, and the first path after it opens with a newline, which the `lstrip("\n")` takes off, so no path is swallowed into a subject. The reading went in as given, `--no-show-signature` with it, as `settle.py#history` reads; the comment above the loop is in my own words, and the docstring and `skills/settle/SKILL.md` *What the dry run shows* now name `-z` and why. The case went in as `Test_main::test_a_removed_plan_of_a_non_ascii_id_is_read`, with the released item made by `released_item`. Seen red against `bcafb8f69`, the unchanged code, at its last line, `assert f"\n    {old}  " in text` (executed). `--no-show-signature` had no case, so `29bbfba17` adds `test_a_signed_removal_is_read_under_any_show_signature`, which signs the removing commit with an ssh key as the `--from` case does; it went red with `--no-show-signature` alone removed, at the same assertion (executed, `seal mutate`). The class, listed from every `git` call in `settle.py` and `rule_changes.py` that prints paths (rule 12): `settle.py#tracked_names`, `#tracked_text` (which `#citations` reads), `#history`, `#changed` and `#documents` read with `-z`; `settle.py#notes` reads only whether `ls-tree` printed anything, and `#adding_commit` prints no path; `settle.py#released` (`ls-tree -r --name-only`, no `-z`) and `rule_changes.py#order` (`log --name-only`, no `-z`) read a quoted path. A probe repository whose one work item id ends in two Hangul syllables printed "0 work items; 1 unreleased" (executed), so `released` reads such a work item as never released. Both came before this branch and lie outside its frame, and are named in the hand-back for the orchestrator to route.
```

### 2. No case pins `--no-renames`, and the closing memo's grounds for its surviving mutant name the wrong case

```seal
severity: should
location: `tests/skills/test_settle.py:1421`, `seal/threads/1793591507-the-settle-reads-what-earlier-settles-judged/gaps.md:13`
evidence: executed `sh test_tmp_renames.sh`, `bin/test tests/skills/test_tmp_round1.py::test_a_plan_deleted_where_another_is_added_is_still_read -q -p no:xdist`, `git show --no-renames --diff-filter=A --name-only --format= 14bfd9921 -- seal/threads`
```

Why it matters: claimed, in `gaps.md:13`: "A case would have to build a
work item directory renamed in place, which no settle does." Git's rename
detection does not need a directory renamed in place. It pairs any path one
commit deletes with any similar path the same commit adds under the
pathspec. Every plan starts from `templates/records/sdd-plan.md`, so two
plans are often similar. A commit that removes one work item's directory and
adds another's plan is enough. With renames on, `git log --diff-filter=D`
then lists no deletion, and the earlier plan's rows vanish from the section
with no line saying so. The flag in the code is right today, and the output
on this repository is right: none of the five deleting commits on
`origin/main` adds a path under `seal/threads` (executed, all five). The
defect is that the one guard against this loss has no case. A later edit
can remove the flag as redundant, and the memo's own sentence argues that it
changes nothing. The design asks that each guard of the new reading be shown
red with the guard alone removed (`frame/plan.md` *Phases*, row 1).

Executed: a probe repository whose one commit deleted
`seal/threads/1700000001-old/frame/plan.md` and added
`seal/threads/1700000002-new/frame/plan.md` from the same template. `git
log --diff-filter=D` listed nothing with `diff.renames=true`, and listed the
old plan with `--no-renames`. The case below passed against `e59ec5995` and
failed with `--no-renames` alone removed from `settle.py:1115`.

```python
    def test_a_plan_deleted_where_another_is_added_is_still_read(self, repo, capfd):
        """#1281, design *Scope* item 1. One commit deletes a work item's plan
        and adds another's from the same template, so git's rename detection
        would pair the two and list no deletion. Seen red with `--no-renames`
        removed from `earlier_judgments`."""
        git(repo, "config", "diff.renames", "true")
        old, new = "1700000001-old", "1700000002-new"
        plan = judgments_plan([("2026-10-01", "ended the rounds", "y", "z")])
        write(repo / "seal" / "threads" / old, "frame/plan.md", plan)
        commit(repo, "the old work item (#3)")
        git(repo, "rm", "-rq", f"seal/threads/{old}")
        write(repo / "seal" / "threads" / new, "frame/plan.md", plan)
        commit(repo, "settle 0.1.0 and frame the new one (#7)")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert f"\n    {old}  " in text, text
```

The memo's paragraph then loses its `--no-renames` half. What it says of
`--full-history` stays; Confirmations below weighs it.

```seal
verdict: fixed 0e45a9122
answer: The finding holds: the closing memo's grounds named a directory renamed in place, and one commit that removes a plan and adds another work item's from the same template is enough. The case went in as given, as `Test_main::test_a_plan_deleted_where_another_is_added_is_still_read`; it passed at `0e45a9122` and went red with `--no-renames` alone removed, at `assert f"\n    {old}  " in text` (executed, `seal mutate`). The docstring of `earlier_judgments` and `skills/settle/SKILL.md` *What the dry run shows* now say what `--no-renames` keeps. `gaps.md` *Not done* was rewritten at `8c38dcf69`: its paragraph now names `--full-history` alone, with the grounds the round's edges give for it. The phase record's mutation paragraph still says `--no-renames` survived; it is phase 1's account, and a fix pass writes no phase record.
```

## Confirmations

```seal
confirms: none
```
What matched: nothing is kept beside the tree. The diff from `47ec17cb8`
changes `skills/settle/SKILL.md`, `skills/settle/scripts/settle.py`,
`tests/skills/test_settle.py` and this work item's records, and adds no file,
cache, count or coordinate under `seal/` or anywhere else (executed: `git
diff --stat 47ec17cb8 e59ec5995`). The earlier rows come from `git log` and
`git show` of `--released-at` at each run (`settle.py:1111-1140`, read).

```seal
confirms: none
```
What matched: the section prints only what it reads exactly and decides no
kind. Each row's four cells come from `plan_rows`, the same reader the
released plans use (`settle.py:1041-1078`, read). The release comes from
`adding_commit` and `version`, the removing commit's number from
`PULL_REQUEST_RE`, and the grouping is a dictionary keyed on the cell as
written (`settle.py:1140-1170`, read). Nothing counts, filters or matches
rows. The heading says "The script matches no row to another" and leaves
the kind to the settling session (`settle.py:817-824`, pinned by
`Test_module::test_the_dry_runs_headings_say_who_decides`). The skill's
bullet and step 5 say the same, in so many words: "two cells spelt apart
are not two kinds", and the kind is read "not from its cell's spelling"
(`skills/settle/SKILL.md:222-243`, `:345-354`, read). The replay over this
repository's history matched the phase's account (executed, `bin/seal
settle --released-at origin/main` in the clone, exit 0): 74 rows, 41 groups
and 18 work items, 41 work item lines removed by `14bfd992 (#1269)` and 24 by
`a92c358b (#1214)`, releases v0.26.0 to v0.27.2, and no line not read.

```seal
confirms: none
```
What matched: design S2. The exact pin in
`test_the_judgments_are_printed_by_the_document_each_stands_on` bounds its
block from `JUDGMENTS_HEADING` to `REMOVES_HEADING`
(`tests/skills/test_settle.py:1170-1188`, read), and `report` prints the new
section inside that span (`settle.py:1654-1666`, read). A heading printed
with nothing under it would fail the pin. `bin/test
tests/skills/test_settle.py -q` passed 156 cases at `e59ec5995` (executed).

```seal
confirms: none
```
What matched: the doubled-heading survivor's grounds hold. Claimed in
`gaps.md:11`: the branch came unchanged from `judgments` and was only moved.
The diff shows the `section_lines` call and its `why` moved from
`judgments` into `plan_rows` with the same condition
(`settle.py:1068-1070` against `47ec17cb8`'s `judgments`, read). A move owes
no new case (`skills/code-review/SKILL.md` *Probes and regression tests*,
the row *Regression test*).

```seal
confirms: none
```
What matched: the departure that a plan whose `git show`, adding-commit read
or tag read fails prints none of its rows (`trail/phases/phase-1.md`). A row
with no release would read as one whose release is known. The core's rule
that a script names what it did not read and decides nothing on it is the
document judged against, and the departure keeps it. The failing-git case
covers all three reads (`tests/skills/test_settle.py:1527`, read).

```seal
confirms: none
```
What matched: the new cases each cover something their group does not.
S1 pins the earlier block whole, and the existing pin covers today's block
only. The near-heading case for a removed plan pins the `<short>^:`
coordinate that the released-plan near-heading case cannot reach. The
once-only case pins the newest-deletion choice and the removal order
(`tests/skills/test_settle.py:1351-1572`, read).

Edges this round judged not worth a finding, with their grounds:

- `--full-history` has no case either, and `gaps.md:13` gives it no grounds
  beyond being the frame's flag. Default history simplification prunes a
  deletion only where a merge's `seal/threads` matches one parent's exactly
  and the deletion stands on the other parent's line. A release merge into
  `main` brings that release's deletions, so it does not match the old
  `main`. No normal flow produces the pruned shape, and a case would build
  that merge by hand.
- The heading says the rows are "grouped by the document each stands on",
  while the grouping is by the cell as written. It copies
  `JUDGMENTS_HEADING`'s wording, which has said this since #1167. The same
  heading says the script matches no row to another, and step 5 tells the
  settling session to read the kind from what each row says. A reader is
  not misled into taking a group for a kind.
- The dry run on this repository took 3.72 seconds, against 0.38 seconds at
  `47ec17cb8` (executed). The adding-commit and tag reads run for all 55
  listed plans, 35 of which hold no section. Reading `plan_rows` first and
  skipping a plan with no row and no unread line would remove most of them.
  The dry run runs once per release, so the cost does not reach a finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `e59ec5995`, labelled `unverified` in `gaps.md`; this round ran only `tests/skills/test_settle.py` | the branch at `e59ec5995` | the orchestrator, at `seal gate` after the rounds settle |
| Whether `#1289` and `#1288` hold the owner's no-cap decision as design G4 quotes them; this round opened no issue on the code-hosting service | `frame/design.md` G4 | the sealer |
| Whether the three `## Rule changes` operations still place against `docs/`; carried from the framer's G19 run, not re-run | `frame/design.md` *Rule changes* | the settling session after the release |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py -q`, in a `git clone --no-local` at `e59ec5995` | exit 0, 156 passed |
| `bin/seal settle --released-at origin/main`, timed, at `e59ec5995` and at `47ec17cb8` | both exit 0; 3.72 s and 0.38 s; the new section held 74 rows, 41 groups, 18 work items and no line not read |
| `git show --no-renames --diff-filter=A --name-only` over each of the five deleting commits on `origin/main` | no path under `seal/threads` added by any of them |
| `sh test_tmp_renames.sh`: one commit deletes one plan and adds a similar one, then `git log --diff-filter=D` with renames on and off | renames on listed nothing; `--no-renames` listed the deleted plan |
| `python3 test_tmp_quotepath.py`: `earlier_judgments` over a repository whose two removed plans have an ASCII id and an id ending U+C815 U+B82C | one group, for the ASCII id; `unread` empty; `git log` printed the other path quoted with octal escapes |
| `bin/test tests/skills/test_tmp_round1.py -q -p no:xdist`, the two cases of findings 1 and 2, at `e59ec5995` | the non-ASCII case failed, the rename case passed |
| the rename case, with `--no-renames` alone removed from `settle.py:1115` | failed |
| both cases and `tests/skills/test_settle.py`, with finding 1's fix applied; then `bin/seal settle --released-at origin/main` | exit 0, 158 passed; dry run output identical to the unchanged code's |

Each probe file, the probe repositories and the clone were removed before
this record was written.
