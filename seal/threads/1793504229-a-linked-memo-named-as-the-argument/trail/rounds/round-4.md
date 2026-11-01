# Review round 4: 1793504229-a-linked-memo-named-as-the-argument

```seal
target: 792cf390, fixes d9b5f6e3..792cf390
```

This is the verifying round. Its target is the diff from round 3's target (d9b5f6e3) to HEAD: the round 3 record and the orchestrator's plan rows at 9acfafe1, the fix commit b46c616b, the phase record and closing memo at cd5fb330, and the close blocks at 792cf390. The base is `origin/release/v0.27.1`, whose merge base with HEAD is 48d035aa. No `seal/parity.md` is declared, so no original is compared and no `original:` line is owed. The record language is English, since `seal/config.md` has no `Record language` row.

Carried from rounds 1 to 3, not re-established: where the presence check, the typo check and the second arm stand in `main`; that `ls-tree -r` lists a tracked link as one blob under its own name and nothing through it; and the layouts of their probe fixtures, written again from their `## Probes` rows. Re-derived this round: every verdict below. Every fixture ran at `main` level with the scripts of 48d035aa and 792cf390, and the whole diff since d9b5f6e3 was read.

**What the removal decides.** The plan's `..` row says a named path that holds a `..` is read as the release reads it, by its real path, so it cannot regress against the release. The fixtures bear that out (executed). No fixture exits 0 at HEAD where 48d035aa exits 1. Every fixture whose argument holds a `..` gives 48d035aa's exit and 48d035aa's line at HEAD. The shapes that exit 0 at both are #1240's or the frame's *Out*. Four of them exited 1 at d9b5f6e3 and exit 0 again now: the round-2 shape `specs/L/x/../gaps.md`, W1, W2, and P1 named from `specs/b` as `../a/gaps.md`. That is the cost the plan's row accepts, and the closing memo states it. The release notes do not, and finding 1 is about that.

Finding 2 lies outside the fix diff. The W4 fixture of round 3 reaches it, and this round read the line that round 3 counted only by its exit.

## Findings

### 1. The changelog fragment says every named path keeps its parts as typed, but a path that holds a `..` is read through its real path, so a link named that way still passes a lost row

```seal
severity: should
location: `seal/threads/1793504229-a-linked-memo-named-as-the-argument/changelog.md:3`
evidence: executed `python3 round-4/test_tmp_round4.py (fixtures P1 and L, each run with the 48d035aa and 792cf390 scripts)`
```

Why it matters: the fragment becomes the release note a person reads. It says "The check now resolves a named path only up to the repository's top and keeps every part inside the repository as typed", and that "the memo named where it became a link" now exits 1. b46c616b made `absolute` return `real(path)` for any path that holds a `..` (`skills/verify/scripts/unverified_check.py:1102-1103`). So a link named on such a path is read as its target, as at 48d035aa. The probe ran issue P1, where `specs/a/gaps.md` (two rows at the base) is now a link to `../b/gaps.md` (one row). Named `specs/a/gaps.md`, the run exits 0 at 48d035aa and 1 at HEAD. Named from `specs/b` as `../a/gaps.md`, or as `specs/b/../a/gaps.md`, it exits 0 at both. Typing `../` from a sibling directory is an ordinary way to name a memo. A person who reads the note expects the refusal, gets exit 0, and takes the memo as intact.

`gaps.md` *Not done* already states this cost, and the plan's `..` row decides it. Only the fragment lacks the sentence. Contract rule 19 asks that the commit which changes a fact also correct what stood on it, and b46c616b and cd5fb330 left this sentence as it was. The fix touches the records alone. In `changelog.md`, after "keeps every part inside the repository as typed.", insert:

```markdown
A path that holds a `..` is still read through its real path, as before, so a link named on such a path, such as `../a/gaps.md` typed from a sibling directory, is read as its target, and the rows its own path held are not compared (#1240).
```

```seal
verdict: fixed fa73cf34
answer: The sentence is rewritten in place, in my own words, because finding 2's fix adds a second path the check reads through its real path. After "keeps every part inside the repository as typed." the fragment now says: "A path that holds a `..`, or that runs through a link loop, is still read through its real path, as before. So a link named on a path that holds a `..`, such as `../a/gaps.md` typed from a sibling directory, is read as its target, and the rows its own path held are not compared (#1240)." The loop names no lost row, since a loop read through `real` prints the release's line. The second sentence is round 4's, split in two.
```

### 2. A named link loop is kept as named, so the scan reads nothing under it, and the base's memo under its real spelling is reported deleted though it is there

```seal
severity: should
location: `skills/verify/scripts/unverified_check.py:1073-1076`, `skills/verify/scripts/unverified_check.py:1714`, `tests/skills/test_unverified_check.py:2527`
evidence: executed `python3 round-4/test_tmp_round4.py (fixture W4, each run with the 48d035aa and 792cf390 scripts)`, `python3 skills/verify/scripts/unverified_check.py --baseline HEAD specs/loop (in W4, with the ab958884, de9a4f01 and d9b5f6e3 scripts)`, `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -rf -k test_tmp_refuses (the case below, under the fix and at 792cf390's script)`, `bin/test tests/skills/test_unverified_check.py -q (under the fix)`
```

Why it matters: take W4. `specs/a/gaps.md` held two rows at the base and now holds one, and `specs/loop -> loop/..` stands beside it. Named `specs/loop`, 48d035aa exits 1 with `specs/a/gaps.md:1  2 rows at HEAD, 1 here`, which is true. HEAD also exits 1, but with `specs/a/gaps.md:1  present at HEAD and not here. Whatever it recorded as unverified left with it, and its directory still stands, so this is no settle`. That is false: the memo is there, and it lost a row. The message tells the person to restore a memo that was never deleted, and it does not name the row that was lost.

The cause: `as_named` (`skills/verify/scripts/unverified_check.py:1073-1076`) keeps `specs/loop` as named, since the argument holds no `..`. The scan walks the named path and enters nothing, because a loop is no directory. `spellings` (`:1714`) ends at `real()`'s spelling, which for this loop is `specs` (executed: `os.path.realpath` gives `specs` under CPython 3.13.5). So the presence check lists the base's `specs/a/gaps.md` under a prefix that the scan never read. The line has stood since de9a4f01. ab958884 exits 2 with `no such path: specs/loop`, and de9a4f01 and d9b5f6e3 print the false line (executed). Round 3 ran W4 named `specs/loop` and recorded only its exit, 1. The unit that keeps the loop as named is `as_named`, which phase 1 built, so this is new work and carries no `regression:` line. Like round 3's finding 2, it comes from a loop. A loop is an unlikely argument, but the run tells the person something false.

The fix reads a loop through `real`, as 48d035aa read every argument. The probe ran it in the clone. W4 named `specs/loop` then gives 1 with `2 rows at HEAD, 1 here`. Every other fixture kept its exit pair. The module passed, 388 cases. `uvx ruff check` and `uvx ruff format --check` on the script exited 0. The case below passed under the fix. At 792cf390's script it failed, `assert ('2 rows at HEAD, 1 here' in ...)`, with the false line in the output.

```python
# skills/verify/scripts/unverified_check.py, at the top
import errno

# in as_named, after `full = absolute(path)`
    try:
        os.stat(full)
    except OSError as error:
        # A link loop, such as `loop -> loop/..`, leads nowhere the walk can
        # enter, so the path is read as `real` reads it, as before #1225.
        # Kept as named, the scan read nothing under it and the base's memo
        # under the real spelling was reported deleted.
        if error.errno == errno.ELOOP or getattr(error, "winerror", None) == 1921:  # 1921 NOT RUN HERE
            return real(full)
```

```python
# tests/skills/test_unverified_check.py, Test_main, after
# test_refuses_a_row_lost_through_a_link_the_person_names
    def test_refuses_a_row_lost_under_a_named_link_loop_as_real_reads_it(
        self, tmp_path, monkeypatch, capsys
    ):
        """`loop -> loop/..` leads nowhere the walk can enter, so a named loop
        is read as `real` reads it, as before #1225. Kept as named, the scan
        read nothing under it, and the base's memo under its real spelling
        was reported deleted though it is there."""
        d = _committed(tmp_path, {f"specs/{WORK}/gaps.md": memo(CANONICAL)})
        write(d, f"specs/{WORK}/gaps.md", memo(CANONICAL.replace(WINDOWS + "\n", "")))
        symlink_or_skip(os.path.join("loop", os.pardir), str(d / "specs" / "loop"))
        monkeypatch.chdir(d)
        assert run([os.path.join("specs", "loop"), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "2 rows at HEAD, 1 here" in out and "not here" not in out, out
```

Precondition, beside the OS boundary: on POSIX, `os.stat` of a path through a loop raises `OSError` with `errno.ELOOP`, which the probe ran. On Windows, the error for a reparse-point loop is taken to be `ERROR_CANT_RESOLVE_FILENAME` (1921). That was read and not run, so the Windows legs answer for it. If the fix pass leaves the loop as it stands, the close is `deferred` to a home the orchestrator names. #1240's *Done when* does not cover this case: a comparison by file identity still finds nothing scanned under the loop.

```seal
verdict: fixed fa73cf34
answer: Round 4's fallback is built in `absolute` (`skills/verify/scripts/unverified_check.py:1095-1119`), not after the call to it in `as_named`. `as_named` reads the argument through `absolute`, so it falls back as the finding asks. `repository_of` reads the argument through `absolute` too, so the root and the compared path still come from one reading, as `trail/phases/phase-1.md:13` states. Where `os.stat(path)` raises with `errno.ELOOP`, or with `winerror` 1921, `absolute` returns `real(path)`, as 48d035aa read every argument. The Windows code is read and not run. CPython 3.12.11's `ntpath.py:675-676` lists 1921, `ERROR_CANT_RESOLVE_FILENAME`, as "implies unfollowable symlink" among the errors `realpath` steps past. `gaps.md` *Not verified* names the Windows legs as its answerer, and says that Windows may resolve `loop\..` by its text, so that the case builds no loop there. The docstrings of `absolute` and `as_named` and the comment in `overviews` name the loop in the same commit. The case is round 4's, `Test_main::test_refuses_a_row_lost_under_a_named_link_loop_as_real_reads_it` (`tests/skills/test_unverified_check.py:2542`), placed after `test_refuses_a_row_lost_through_a_link_the_person_names`; no case in `Test_main` or `Test_as_named` named a loop before it. It failed against 792cf390's script, which 6431e637 holds byte for byte, with `present at HEAD and not here` in the output, and passed after the fix (executed). Two `seal mutate` runs at fa73cf34 each went red: the condition replaced by `if False:`, and the fallback's `return real(path)` replaced by `pass` (executed, each `seal mutate` exit 0). The module passed with 389 cases, the phase-boundary set of 30 modules with 2396 and the same 9 skips, and `uvx ruff check` and `uvx ruff format --check` on the two files exited 0 (executed). The class was listed by the errors `os.stat` raises for an argument whose path holds a link. `ELOOP` is the one where the scan enters nothing while `real` gives another spelling. A dangling link raises `ENOENT`, and the memo is then absent, so `not here` is true. That second instance was read and not run, so the list is a sample.
```

### 3. The plan's `..` row and the phase record each name a different two of the three `..` readings this item built, and neither says that the cases at `trail/phases/phase-1.md:79-80` went

```seal
severity: should
location: `seal/threads/1793504229-a-linked-memo-named-as-the-argument/frame/plan.md:45`, `seal/threads/1793504229-a-linked-memo-named-as-the-argument/trail/phases/phase-1.md:13`
evidence: executed `git show b7d19345:skills/verify/scripts/unverified_check.py`, `git diff d9b5f6e3..792cf390 -- seal/threads/1793504229-a-linked-memo-named-as-the-argument`, `git grep -n test_accepts_a_parent_after_a_link`
```

Why it matters: this item built three readings of `..` before the current one. Phase 1 used `os.path.abspath`, by text, and round 1 asked about it. Round 1's fix pass (b7d19345) resolved "the part up to the last `..`" through `real` and kept the rest as named, and round 2 found a row lost behind it. Round 2's fix pass built the walk, and round 3 found two defects in it. The plan's grounds (`frame/plan.md:45`) say "Two readings ... by text up to the last `..` (round 2), and by a walk", which names b7d19345's reading backwards: it resolved up to the last `..`, and it did not read it by text. The phase record (`trail/phases/phase-1.md:13`) says "Two other readings": phase 1's and the walk. It leaves out b7d19345's. So the two records disagree about which readings were tried. The settle reads the plan row to weigh what the judgment cost, and the sealer reads both records against each other, so each will act on a wrong count.

The orchestrator asked about `trail/phases/phase-1.md:79-80`. Those lines name `Test_as_named::test_accepts_a_parent_after_a_link_as_the_file_system_reads_it` and `Test_repository_of::test_accepts_a_parent_after_a_link_as_the_file_system_reads_it`, which b46c616b removed (`git grep` finds them only in the records). The lines sit in *Round 1's fix pass*, and they say each case was seen red at ab958884 and passed at de9a4f01. Both statements are true at those commits. History belongs in the work record, so the lines stand as written. Mutants 8 and 9 at `:94-95` stand for the same reason. The defect is in line 13. It says "The walk and its budget are gone, and so are their cases", but these two cases are b7d19345's, not the walk's. A reader at HEAD is not told that they went. The fix rewrites line 13 to cover them and leaves lines 79-80 alone.

The fix touches the records alone. The plan cell is the orchestrator's.

```markdown
<!-- frame/plan.md:45, the first sentence of the Grounds cell -->
Three readings of `..` were built, and the round after each one questioned or refuted it: by text through `os.path.abspath` (round 1's *Not judged* row); through `real` up to the last `..` and as named after it (round 2: a link the `..` never left was resolved); and by a walk that follows the link a `..` leaves (round 3: Windows reads it by text, and a link loop climbs out of the repository).
```

```markdown
<!-- trail/phases/phase-1.md:13, replacing from "Two other readings" to "in that second reading.", and the sentence on the cases -->
Three other readings were built for this work item, and the round after each one questioned or refuted it. Phase 1 dropped `a/..` by its text through `os.path.abspath`, which names a directory the file system does not reach where `a` is a link, and round 1 asked about it. Round 1's fix pass resolved the part up to the last `..` through `real`, which also resolved a link the `..` never stepped out of, and round 2 found a row lost behind it. Round 2's fix pass followed only the link a `..` steps out of, by that link's own text. Round 3 found two defects in that third reading.
...
The walk and its budget are gone, and so are the `..` cases of each earlier reading, the two that *Round 1's fix pass* lists as seen red among them.
```

```seal
verdict: fixed fa73cf34
answer: The plan cell, `frame/plan.md:45`, was rewritten with round 4's text by the orchestrator at 6431e637. fa73cf34 rewrote `trail/phases/phase-1.md:13` with round 4's paste-ready text: "Three other readings" through "in that third reading", and the sentence on the cases that left. The b7d19345 reading was checked at `git show b7d19345:skills/verify/scripts/unverified_check.py`, whose `absolute` resolves the part up to the last `..` through `real` (read). Lines 79-80 and 94-95 stand, as the finding says. In the same commit, the passage's sentence on what `absolute` gives, and a closing sentence, name finding 2's loop reading, because `absolute` changed there.
```

## Confirmations

```seal
confirms: round-3#1
```
What holds: no `..` case expects one platform's result, read and executed. `absolute` has no branch on `os.name` (`skills/verify/scripts/unverified_check.py:1092-1104`). The three cases round 3 named are gone, and the two `..` cases left, `Test_repository_of::test_accepts_a_parent_as_real_reads_it` (`tests/skills/test_unverified_check.py:1568-1579`) and `Test_as_named::test_accepts_a_path_holding_a_parent_as_real_reads_it` (`:1610-1621`), assert against `os.path.realpath` of the same path. On Windows both sides call `ntpath.realpath` (read). With the `..` branch mutated to `real(os.path.abspath(path))` through `Edit`, both cases failed (executed). b46c616b touches `tests/skills/test_unverified_check.py` and `skills/verify/scripts/unverified_check.py`, both of which round 3's `location:` names. The module passed at HEAD, 388 cases (executed). Whether the link cases run on the Windows legs stays in `## Not judged`.

```seal
confirms: round-3#2
```
What holds: the walk and its budget are gone, so no loop climbs out of the repository (read, `:1092-1104`; executed, W4). Named `specs/loop/..` with a row lost, HEAD exits 1 with `specs/a/gaps.md:1  2 rows at HEAD, 1 here`, as 48d035aa does. Named `specs/loop/../a/gaps.md`, both exit 2 with `no such path`, and the false `is not in one` is gone. `trail/phases/phase-1.md:13` states no budget and no loop. b46c616b touches `skills/verify/scripts/unverified_check.py`, a path round 3's `location:` names. Named `specs/loop` with no `..`, the line is wrong, which is finding 2. That path is outside round 3's finding and outside b46c616b.

```seal
confirms: round-3#3
```
What holds: `gaps.md:18` no longer gives the second-resolver reason, read. It rests the deferral on the layout and on #1240. `gh issue view 1240` shows #1240 open, in milestone `backlog: gates & hooks`, and its *Symptom* lists the four shapes, `..` among them (executed). cd5fb330 touches `gaps.md`, the path round 3's `location:` names.

```seal
confirms: none
```
What matched: the plan's `..` row says that a path holding `..` reads as the release reads it, and at `main` level that holds, executed. Each `..` argument of the probe gives 48d035aa's exit and 48d035aa's line at HEAD. `specs/b/../a`, with one of two memos deleted behind a tracked link: 1 and 1. `specs/b/../a/gaps.md`, with the memo deleted behind the link: 1 and 1. P1 as `../a/gaps.md` from `specs/b`, or as `specs/b/../a/gaps.md`: 0 and 0. P1 scanned as `specs/b/..`: 1 and 1. P8 through `specs/b/..`: 2 and 2, with the same `is not in one` line. The round-2 shape as `specs/L/x/../gaps.md` or `specs/L/x/..`: 0 and 0 with a row lost, 2 and 2 with the memo deleted. W1, W2 and both W3 forms: 0 and 0 with a row lost, and W1 2 and 2 with the memo deleted. W4 through `..`: as in the confirmation of round-3#2. W5: 1 and 1 for both forms. The table under `## Probes` has every fixture.

```seal
confirms: none
```
What matched: `gaps.md` *Not done*, the two paragraphs cd5fb330 added, states what the probe shows (executed). The old name left as a link (W3), named by its new path, gives 0 at 48d035aa and at HEAD. The `..` paragraph's shape is the round-2 layout. Named `specs/L/gaps.md` it gives 0 and 1, and named `specs/L/x/../gaps.md` it gives 0 and 0, as the paragraph says. `trail/phases/phase-1.md:13` says a `..` path's real path holds no link, so `as_named` gives it back unchanged. That holds as read: `absolute` returns `real(path)`, and `as_named` joins `real(prefix)` of a real path to the rest (`skills/verify/scripts/unverified_check.py:1073-1089`). The same line says Phase 1's lost-row cases name no `..`. That holds too: every `..` in `Test_main` is in a link's text, and none is in an argument (`git grep`, executed).

```seal
confirms: none
```
What matched: each new test, read against its group, covers something its group did not. `Test_repository_of::test_accepts_a_parent_as_real_reads_it` is the one case in that class whose argument holds a `..`. `Test_as_named::test_accepts_a_path_holding_a_parent_as_real_reads_it` is the one such case in its class, and its layout puts a link above the link the `..` steps out of. So it fails a mutant that reads only the stepped-out link, and a mutant that reads by text (executed, the mutant above). `bin/seal layout --pairs tests/skills/test_unverified_check.py` exits 0 with 0 pairs, and `uvx ruff check` and `uvx ruff format --check` on the two changed files exit 0 (executed).

```seal
confirms: none
```
What matched: the label on the broad gate is honest. `gaps.md` lists the full suite and the repository-wide lint as unverified, with the orchestrator through `seal gate` as the answerer. No record on the branch claims a broad run, and this round ran none. Once the three findings close, the orchestrator's broad run comes due, then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the Windows legs run the link cases or skip them. Whether `ntpath.realpath` drops `..` by its text before it reads a link, so that a `..` path reads there as 48d035aa read it. Finding 2's Windows error code. Each was read, and no run here reached Windows | `skills/verify/scripts/unverified_check.py:1062-1104`, `tests/skills/test_unverified_check.py:1568-1621` | the Windows legs of `.github/workflows/test.yml` on this pull request, as `gaps.md` *Not verified* names |
| The full suite, the repository-wide `ruff check` and `ruff format --check` | the branch at 792cf390 | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 round-4/test_tmp_round4.py`, from the round's scratch directory, with a `git clone --no-local` at 792cf390 and 48d035aa's `skills` and `hooks` trees extracted beside it, each fixture run at `main` level with each script, `--baseline HEAD`, CPython 3.13.5 | Exits in the order 48d035aa, 792cf390. Round 1 and the design's probes: a tracked directory link with one of two memos deleted, named `specs/a`, scanned, or as `specs/b/../a`: 1, 1. An untracked `view -> specs` with one memo deleted, the only memo deleted, or a row dropped: 1, 1. The only memo deleted behind a tracked link, named `specs/a`, `specs/a/gaps.md` or `specs/b/../a/gaps.md`: 1, 1. A row dropped behind the link: 1, 1. P1 named: 0, 1. P1 named `specs/a` or scanned: 1, 1. P1 as `../a/gaps.md` from `specs/b`, or as `specs/b/../a/gaps.md`: 0, 0. P1 as `specs/b/..`: 1, 1. P2 named, and P3: 0, 1. P2 scanned: 1, 1. P8: 2, 1. P8 through `..`: 2, 2. P9: 0, 0. P4, a link to the top with a row dropped, a memo deleted, or named `<link>/specs`: 1, 1. P5 and P6, named or scanned: 0, 0. P7 and Q1: 0, 0. Round 2: mutant 5's layout with nothing lost, named `view` or `specs`: 0, 0. With a row lost: 1, 1, each printing both lines, for `specs/W/gaps.md` and `specs/O/gaps.md`. The open shape through both links or the lower link: 0, 0. Through the upper link, named `specs/L1` or `specs/L1/X/gaps.md`: 0, 1. The round-2 shape named `specs/L/gaps.md`: 0, 1 with a row lost and 2, 1 with the memo deleted. Its two `..` forms: 0, 0 with a row lost and 2, 2 with the memo deleted. A link to an outside directory that holds a link: 2, 0, with no traceback. Scanned: 0, 0. Round 3: W1: 0, 0 with a row lost and 2, 2 with the memo deleted. W2: 0, 0. W3 named by the new name, or through `jump` with relative or absolute text: 0, 0. W4 `specs/loop/..`: 1, 1. `specs/loop/../a/gaps.md`: 2, 2. `specs/loop`: 1, 1, with 48d035aa printing `2 rows at HEAD, 1 here` and HEAD printing `present at HEAD and not here` (finding 2). W5, both forms: 1, 1. No fixture gives 1 then 0 |
| `python3 skills/verify/scripts/unverified_check.py --baseline HEAD specs/loop` in W4, with the trees of ab958884, de9a4f01 and d9b5f6e3 | ab958884 EXIT=2, `no such path: specs/loop`. de9a4f01 and d9b5f6e3 EXIT=1, `specs/a/gaps.md:1  present at HEAD and not here` |
| `absolute`'s `..` branch changed to `real(os.path.abspath(path))` through `Edit`, then `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -rf -k "test_accepts_a_parent_as_real_reads_it or test_accepts_a_path_holding_a_parent_as_real_reads_it"` | 2 failed, 386 deselected. Taken back through `Edit` |
| Finding 2's fix put into the clone through `Edit`, then the probe again, `bin/test tests/skills/test_unverified_check.py -q`, and `uvx ruff check` and `uvx ruff format --check` on the script | W4 `specs/loop` gave 1, 1 with `2 rows at HEAD, 1 here` from both. Every other fixture's exit pair was the same as in the first run. Module EXIT=0, 388 passed. Ruff EXIT=0 and EXIT=0 |
| Finding 2's case added to the clone's test module through `Edit` as a `test_tmp_` case, then `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -rf -k test_tmp_refuses`, under the fix and with the script back at 792cf390's bytes | 1 passed under the fix. EXIT=1 at 792cf390, `assert ('2 rows at HEAD, 1 here' in ...)`. The case was taken back through `Edit`, and `git status --short` in the clone was empty |
| `bin/test tests/skills/test_unverified_check.py -q` at 792cf390 | EXIT=0, 388 passed |
| `bin/seal layout --pairs tests/skills/test_unverified_check.py` | EXIT=0, 1 file read, 0 pairs |
| `gh issue view 1240` and `gh issue view 1238` | both OPEN, milestone `backlog: gates & hooks` |

The probe file, the fixtures, the clone and the extracted script trees were removed before hand-back.
