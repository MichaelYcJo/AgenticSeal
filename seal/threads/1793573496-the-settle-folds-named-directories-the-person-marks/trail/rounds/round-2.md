# Review round 2: 1793573496-the-settle-folds-named-directories-the-person-marks

```seal
target: f37176aef, fixes 0cdf4ce70..f37176aef
```

This verifying round read the diff `0cdf4ce70..f37176aef` in the branch's own
worktree. That diff holds the fix pass's three commits (`47c1bf70b`,
`57559a4a6`, `aea93bf36`), its record `228588eda`, and the orchestrator's frame
fold (`e1640f385`, `f37176aef`). Carried from round 1 as coordinates and not
re-established: where the listing lives (`settle.py#history`, `#changed`,
`#documents`, `#named_directory`), the cases of `Test_main` that read it, and
the two README rows. Round 1's finding 1 probe was written again and run, as
its `## Probes` row gives it. No `seal/parity.md` is declared, so the round
block holds no `original:` line. `seal/config.md` holds no `Record language`
row, so the record is English. Every claim of the fix pass's close blocks was
read as a claim and checked against the tree below.

## Findings

### 1. A document a merge wrote, which neither parent holds, is listed as one no commit adds

```seal
severity: should
location: `skills/settle/scripts/settle.py:885-913`, `skills/settle/scripts/settle.py:62-64`, `skills/settle/SKILL.md:218-224`, `tests/skills/test_settle.py:1998-2025`
evidence: executed `bin/test tests/skills/test_tmp_round2_1054.py -q -rP -p no:xdist (a merge run with --no-commit that writes adr/0002.md, which neither parent holds, then settle.main --from adr; and git log --cc over adr/0002.md)`
```

Why it matters: the line `no commit adds it` tells the settling session that
a file was never committed. The skill says it is read only for a file
"untracked or staged and never committed" (`skills/settle/SKILL.md:223-224`).
The session uses the adding commit to place a promoted document in the
timeline, and the last change to tell a document skipped at an earlier settle.
A document printed as no commit adds loses both, and it sorts last.

The fix for round 1's finding 1 made `history` read merge commits with `--cc`.
Its docstring now claims a merge's status "holds one letter per parent, so it
never reads as an add" (`settle.py:890-892`). The loop at `settle.py:904`
counts an add only where the status is exactly `A`. Under `--cc` a merge's
status is one letter per parent, and the letter `A` against a parent means
that parent does not hold the path. So the status `AA` says the merge itself
added the file, and the loop drops it.

The probe merged `side` into `main` with `--no-commit`, wrote `adr/0002.md`,
and committed. `git ls-files` listed `adr/0002.md` as tracked. `git log --cc`
named it once, at the merge, with the fields `""`, `"AA"`, `"adr/0002.md"`.
The listing printed `adr/0002.md  no commit adds it`. The cause is round 1's
finding 1's: the merge's change was not read as what it is. The fix pass's
close names no enumeration of that class, and this is an instance of it the
fix left. It is not a regression: before `--cc` the merge was not read at all,
and the line was the same.

The add/add conflict does not take this path. There both parents hold the
file, so the status is `MM`, and the two side commits that added it remain
the adding commits.

```python
    added, last, commit, status = {}, {}, None, None
    for place, field in enumerate(fields):
        if status is not None:
            last[field] = commit
            # One letter per parent under --cc; `A` against every parent is
            # a path no parent holds, which the merge itself added.
            if set(status) == {"A"}:
                added[field] = (place, commit)
            status = None
            continue
```

The docstring at `settle.py:890-893` then reads "its status holds one letter
per parent, and it reads as an add only where every letter is `A`, a path no
parent holds". The module docstring (`settle.py:62-64`) and the skill's
listing bullet (`skills/settle/SKILL.md:220-222`) gain "and a merge that wrote
a file no parent holds is the commit that added it". The case goes beside
`test_a_merge_that_resolved_a_document_is_its_last_change`. The merge is
clean, so `git` with `check=True` stands:

```python
    def test_a_merge_that_wrote_a_document_no_parent_holds_adds_it(
        self, repo, capfd, monkeypatch
    ):
        """#1054, round 2's finding 1: a merge whose result holds a document
        neither parent holds is the commit that added it, since `--cc` gives
        that path one `A` per parent."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        write(repo, "adr/0001.md", "one\n")
        commit(repo, "a decision")
        git(repo, "checkout", "-qb", "side")
        write(repo, "adr/side.md", "side\n")
        commit(repo, "side")
        git(repo, "checkout", "-q", "main")
        write(repo, "adr/main.md", "main\n")
        commit(repo, "main")
        git(repo, "merge", "--no-ff", "--no-commit", "-q", "side")
        write(repo, "adr/0002.md", "written in the merge\n")
        commit(repo, "merge side, adding adr/0002.md")
        merged = stamp(repo)
        monkeypatch.chdir(repo)
        code, text = dry_run(repo, capfd, "--from", "adr")
        assert code == 0, text
        assert f"    adr/0002.md  added {merged}  last changed {merged}\n" in text, text
```

`skills/settle/scripts/rule_changes.py#order` reads a design's adding commit
with no merge diff, so a design a merge wrote is not found there either. That
line is outside this diff. A design is added by its work item's own commits,
so the shape does not arise there in the workflow.

```seal
verdict: fixed 2ba0c6866
answer: Fixed as a decided reader, not as one more edge, per `plan.md`'s last judgment. `settle.py#history`'s docstring now states every status `git log --no-renames --name-status --cc` prints for a path, enumerated by a probe run once (ordinary `A`, `M`, `D`, `T`; two-parent `MM`, `AA`, `AM`, `MA`, `DD`, with a clean merge and a merge keeping one parent's content naming nothing; octopus `AAA`) and by git's rule that a merge is named only where its result differs from every parent, so one status is all `D` or all from `A`, `M`, `T`. One rule reads them: no `D` changes the path, all `A` also adds it, all `D` adds and changes nothing. One case per class, each seen red: `test_a_merge_that_wrote_a_document_no_parent_holds_adds_it` (the finding's case, all `A`) and `test_a_deletion_is_no_change_to_a_document_head_holds` (all `D`: a branch's deletion the walk read after the kept content was printed as the last change) failed at 2c4023db8's reader; the change class is round 1's `MM` case plus `test_a_merge_that_rewrote_a_document_one_parent_lacks_changes_it` (`AM`, fed390e7b), added because `seal mutate` widening the add test to `"A" in status` survived until it stood, then went red. `seal mutate` also turned the add arm (`status == "A"`) and the `D` arm (`if True:`) red. The module docstring, the skill's listing bullet and the changelog say a merge that wrote a file no parent holds added it and a deletion is neither. Left as a stated limit, not built: a path deleted and held again only untracked keeps its earlier dates, since the reader reads no tree. The design's *Data & interfaces* (design.md:99) still says the adding commit is "the last `A` line" and the last change "the last line naming it", for the orchestrator to fold.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `settle.py#history` reads its `git log` with `--cc`
(`settle.py:895-899`). The fix pass claimed the case
`Test_main::test_a_merge_that_resolved_a_document_is_its_last_change`
(`tests/skills/test_settle.py:1998-2025`) holds the conflict a merge resolved.
Round 1's probe, written again and run, printed `adr/0001.md  added 03057c9
last changed bdf5ddc`, the merge, and `--cc` gave the merge the fields `""`,
`"MM"`, `"adr/0001.md"`, executed. The committed case passed in the narrow run
below, executed. Its claim to have been seen red at `a3c3d24c9` and under
`seal mutate` was read, not re-run. The docstring, the module docstring
(`settle.py:62-64`), the skill's bullet (`skills/settle/SKILL.md:218-222`) and
the changelog say a merge that resolved a conflict is the last change, read.
The `added` half of the same cause stands as this round's finding 1.

```seal
confirms: round-1#2
```
What holds: the fix pass widened the fix from one sentence to every `--from`
refusal that names a path. Its method takes the artefact apart: the four
`FROM_` constants (`settle.py:478-495`). `FROM_WITH_APPLY` names no path, and
the other three now end "it reads as {path} from the directory this runs in",
with `path` set to `os.path.abspath(given)` (`settle.py:862-870`), read. No
other refusal formats `given` (`settle.py:1278`, `settle.py:1311-1312`), read.
The parametrized case (`tests/skills/test_settle.py:2044-2088`) gained the row
`--from adr` run in `docs/` and the row `../elsewhere`. It asserts the path as
read on every row, and it passed in the narrow run, executed. The assertion
is red for code that prints GIVEN or a path from the top, because
`os.path.abspath` there runs after `chdir`, read. A probe named a link inside
the repository that points outside it. The sentence said `--from link is
outside the repository at <repo>: it reads as <repo>/link`, executed. The
path it names sits textually inside the repository, but it is the path the
person typed, and opening it shows the link. A link that leaves the
repository is outside the flow of naming a decisions directory, so this round
weighs it as no finding.

```seal
confirms: round-1#3
```
What holds: `test_the_cheat_sheets_name_the_design_file_the_settle_reads`
reads the row from the cell to the end of its line
(`tests/text/test_settle_reads_before_it_removes.py:22-35`), read. Each
README holds the cell once (`grep -c` gave 1 for each), executed, so `[1]` is
the row. `README.md:265` says again "asks the person, before its first edit"
and "`--apply` refuses `--from` and writes no document". `README.ko.md:259`
says "첫 편집 전에" and "`--apply` 는 `--from` 을 거부하고". Both are true
against `FROM_WITH_APPLY` (`settle.py:478-482`), read. `document` stays in use
by the module's other cases (`test_settle_reads_before_it_removes.py:103`,
`:120`, `:132`, `:154`), so no helper is left unused. The case passed in the
narrow run, executed. The mutation claim was read, not re-run.

```seal
confirms: round-1#4
```
What holds: the docstring of `test_no_hook_names_the_0_3_x_roots`
(`tests/behaviour/test_no_document_names_the_old_roots.py:98-101`) opens "No
code of the plugin opens `.specseal/` or a top-level `specs/` on its own",
read. Its assertion is unchanged, and it passed in the narrow run, executed.
The fix pass's close calls its wording search a sample, which contract rule 12
asks.

```seal
confirms: none
```
What matched: the orchestrator's fold names the commands the build reads.
Design *Data & interfaces* (`frame/design.md:99`) names `--cc` and `git diff
HEAD --name-only -z --no-renames`. Plan *Technical context*
(`frame/plan.md:8`) names `--name-status --cc`. Both match
`settle.py:895-899` and `settle.py:916-920`, read. `git status --porcelain`
still stands in G15, in P1 and in A6 (`frame/design.md:23`, `:43`, `:82`).
G15 and P1 record what probe P1 ran, and A6 names how its case compares, so
each stays true. The changelog says "with `changed in the working tree`"
where it said "with a mark", as round 1 suggested, read.

```seal
confirms: none
```
What matched: each new case covers what its group did not, read against
`Test_main`'s named-directory cases. No other case builds a merge, and the
two new refusal rows are the only ones run outside the top or with a relative
path that leaves the repository. The narrow run passed, executed: `bin/test
tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py
tests/behaviour/test_no_document_names_the_old_roots.py
tests/behaviour/test_a_reference_root_is_read_and_never_taken.py
tests/behaviour/test_docs_line_wrap.py -q`, exit 0, 193 passed. That is a
narrow run, not the broad gate. `settle.py:68` is 89 characters, one over
`line-length`. `ruff.toml` selects no `E501`, so no lint reads it, read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the lint and the format check at HEAD. This round ran five modules and labels the suite `unverified` | the repository's `Broad gate` row | the orchestrator, by `seal gate --base origin/release/v0.28.0 --record <item>`, then the sealer |
| The red-first and `seal mutate` claims in the fix pass's close blocks, read and not re-run | `trail/rounds/round-1.md`, close blocks of findings 1 to 3 | the sealer, which re-runs a sample of the crafter's claims |
| Round 1's rows for design A7, and for Windows and case-insensitive paths, carried as they stand and not re-judged in this fix diff | `trail/rounds/round-1.md` *Not judged* | the answerers round 1 names |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round2_1054.py -q -rP -p no:xdist`, one file of three cases in the worktree's `tests/skills/`, using `test_settle`'s fixtures | Round 1's probe again: exit 0, `adr/0001.md  added 03057c9 2026-11-02  last changed bdf5ddc 2026-11-02`, the merge, and `--cc` gave the merge `""`, `"MM"`, `"adr/0001.md"`. A merge that wrote `adr/0002.md`, which neither parent holds: `git ls-files` listed it, `--cc` gave the merge `""`, `"AA"`, `"adr/0002.md"`, and the listing printed `adr/0002.md  no commit adds it`. `--from link`, a link inside the repository to a directory outside it: exit 2, `settle: --from link is outside the repository at <repo>: it reads as <repo>/link from the directory this runs in, so nothing was read.` The probe file was removed before hand-back |
