# Phase 3: 1793171931-checks-that-read-text-pass-what-they-cannot-read

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 234962eb |

## What this phase was asked

Audit family C, readers R25 to R31 of `frame/design.md` *The readers to
audit*, at `c825fd2c`. Each row's verdict carries an executed probe recorded
here; the probe lives in the scratch directory as `test_tmp_*`, runs once and
is deleted before the phase closes. No tree file outside the work item
directory changes.

## What this phase found

### The rows

The `Fix` cell reads as phase 1's does.

| Row | Reader | Reads and decides | On input it cannot read | Lets through | Probe | Fix |
|---|---|---|---|---|---|---|
| R25 | `.github/scripts/gather_changelog.py#live_markers`, `#leaves_open`, `#ungathered`, `#heading_re`, as `--check` runs in `.github/workflows/hygiene.yml:124-130` | changelog fragments and the release files' markers; `--check` exits 1 for a fragment no release file marks | `mixed`: a marker it cannot read leaves its fragment ungathered, and the check fails; a fragment written at any path but `seal/threads/<id>/changelog.md` is no fragment, and the check passes without it | `yes`: an entry written as `frame/changelog.md` or as `changelog.markdown` reaches no release file, and `--check` says every fragment was gathered | `<!--specs/1-a -->`, a trailing space after the marker, and the marker inside a fence: exit 1, the fragment named; a second work item's fragment under `frame/`, and one named `changelog.markdown`: exit 0, "1 changelog fragments, all gathered" | 0.24.1 `gather_changelog.py` |
| R26 | `.github/scripts/issue_claims_check.py#read`, `#prose_only`, `#claimed_spans`, as `hygiene.yml:62-66` runs it | the pull request body, the orchestrator's; prints what it claims and what it only names | `passes`: every body exits 0, a keyword it cannot read included; only a missing body exits 2 | `no`: the step reports and never fails (`docs/issues-and-milestones.md:261-264`), so its result is no verdict and the reader leaves the class by its second condition; it stays a row because R28 compares it | `Closes: #14 and #15` through the script: exit 0, "claimed: none", "mentioned only: #14, #15" | none |
| R27 | `.github/scripts/release_completeness_check.py#judge` and the set D it reads | the release range's pull request bodies' closing keywords, against the milestone `release: X.Y.Z`; exit 1 refuses the release | `mixed`: a closing keyword it cannot read leaves the issue out of D, and the release is refused; a milestone under another title, or a branch not named `release/vX.Y.Z`, is judged as nothing, at exit 0 with a line saying so | `limit`: the release automation names the branch and the owner titles the milestone by `docs/issues-and-milestones.md`'s convention, so the one-issue flow does not produce either near miss; the run prints that it verified nothing | `judge` with M of 11, 14 and 15 and D read from `Closes #11`, `**Closes** #15` and `Closes: #14`: M \ D names #14 and #15, failed; `main` with `HEAD_BRANCH=release/v9.9.9`: exit 0 and a warning that no milestone `release: 9.9.9` exists and the run verified nothing; with `release/9.9.9`: exit 0, "nothing to judge" | 0.24.1 limits |
| R28 | the closing keyword as R26, R27 and `.github/scripts/close_issues_on_release.py#keywords_in` read it, with `skills/code-review/scripts/pr_body.py#_claims` | pull request bodies, the orchestrator's | `refuses`: all four read each near miss alike, and an unread keyword leaves the issue out of D, which R27 refuses | `no`: no near miss tried is read by one and not another, since R26 imports `CLOSING`, `FENCE` and `SPAN` from the closer and `pr_body` calls `keywords_in` | twelve bodies: `Closes #11`, `<!-- Closes #18 -->`, `closes  #19` and `This does not fix #23` were read as claims by all four; `Closes: #14`, `**Closes** #15`, `Closes** #16**`, a code span, `Closes#20`, `Closes o/r#21` and an issue URL by none; `Closes #12 and #13` claimed #12 for all four and warned of #13 in R26 | none |
| R29 | `.github/scripts/rules.py#check_lines`, `#parse`, `#line_problems`, `#check` | the `check:` lines of every rule file; exit 1 for a line out of grammar or a target that does not resolve | `mixed`: a label in another case, without its space or under emphasis, and two spaces between targets, are refused at the line; a target wrapped onto the next line is not read at all | `yes`: a target that does not exist, written on the line after a `check:` line as a hard wrap leaves it, passes `seal rules --check` | nine rules in a scratch `CLAUDE.md`: seven lines read; `Check:`, `check:` with no space, `**check:**`, a missing target and two spaces each refused; the wrapped `tests/missing_wrapped.py` named by nothing; the lines inside a closed fence and a closed comment not read, as the module states | 0.24.1 `rules.py` |
| R30 | `skills/settle/scripts/fold_check.py#index_problems`, `#past_ceiling`, `#config_rows` | the policy root's documents and its `README.md` index; exit 1 for an index out of step | `mixed`: an index row without backticks, or inside a fence, is refused; a `Policy root` item spelt otherwise is the default `docs` (R16), and the fold checks `docs/` instead | `limit`: in a repository holding both directories, `Policy Root` sends the fold to `docs/`, and `policy/README.md` out of step passes; the row is written once at setup, and the one-issue flow never writes it | a scratch repository per shape: a row without backticks: exit 1, two problems; the index in a fence: exit 1; `Policy root` naming `policy` with `policy/README.md` missing a row: exit 1; `Policy Root`: exit 0, "the index docs/README.md names every document" | 0.24.1 limits |
| R31 | `skills/settle/scripts/settle.py#open_rows`, `#survey`, with `--apply`, through `unverified_check.py#open_record_rows` | each released work item's `gaps.md`, read for open rows before `--apply` removes the directory | `mixed`: a section it cannot read is an entry that keeps the directory; a `gaps.md` anywhere but the work item's own directory is no record, and the directory goes with its rows | `yes`: an open row written in `trail/gaps.md` was removed with its directory by `seal settle --apply` | six released work items on `main` in a scratch repository: an open row, `Closed`, `**closed**` and `## Not Verified` kept, exit 1; `closed the suite` removed, as it should be; the open row in `trail/gaps.md` removed | 0.24.1 `settle.py` |

### Pairs for R43

- R28 is the pair row for the closing keyword: four readers, one grammar,
  and no disagreement on the twelve bodies tried.
- R31 and R13 read `## Not verified` with one function, `check_text`; the
  settle reads the working tree's side with no relaxation, as the pull
  request's check does.

### A shape three rows share

R11, R25 and R31 each read a record at one path and say nothing of a record
written at another: a round named `Round-2.md`, a fragment under `frame/`, a
`gaps.md` under `trail/`. Each passes the check its record exists for. The
three fixes are filed per module; phase 5's closing paragraph names the
shape for #1038, since a reader that refuses an unlooked-for record path
across the records would be shared.

### What the frame said that the probe answers

R26: the frame asked whether the step can fail. It exits 2 only when no body
is handed to it, and 0 for every body.

### The probe

`python3 -I <scratch>/c956/test_tmp_3.py > <scratch>/c956/out3.txt 2>&1; echo "exit $?"`
printed `exit 1`. It printed R25 and then raised a `TypeError` in the probe's
own call to `pr_body._claims`, which takes a line number and the record's
lines, not a line of text. The file was edited to drop R25's loop and to
call `_claims` as it is written, and run once more:
`python3 -I <scratch>/c956/test_tmp_3.py > <scratch>/c956/out3b.txt 2>&1; echo "exit $?"`
printed `exit 0` for R26 to R31. R27's `main` ran twice as a subprocess with
`REPO=MichaelYcJo/AgenticSeal`, reading the milestone list through `gh`; it
writes nothing. The file, both outputs and the scratch folder it made were
deleted by their recorded paths before this record was committed.

### Q3

No row of this family reaches either situation `SECURITY.md` names. R26,
R27 and R28 read a pull request body in CI, and a fork's body that claims an
issue claims it for GitHub too, which merges nothing by itself. R25, R29,
R30 and R31 read records and documents a contributor already writes.
