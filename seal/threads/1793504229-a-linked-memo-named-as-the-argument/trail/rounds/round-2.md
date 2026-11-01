# Review round 2: 1793504229-a-linked-memo-named-as-the-argument

```seal
target: f50c0e26, fixes 39dcdb1f..f50c0e26
```

This is the verifying round. Its target is the diff from round 1's record (39dcdb1f) to HEAD: the fix commits b7d19345, de9a4f01 and 32541252, and the orchestrator's fold at f50c0e26. The base is `origin/release/v0.27.1` at 48d035aa. No `seal/parity.md` is declared, so no original is compared and no `original:` line is owed. The record language is English, since `seal/config.md` has no `Record language` row.

Carried from round 1, not re-established: where the presence check, the typo check and the second arm stand in `main`, and that `ls-tree -r` lists a tracked link as one blob under its own name and lists nothing through it. Re-derived this round: every verdict below, by running round 1's fixtures again at HEAD and opening the fix diff.

## Findings

### 1. A `..` after a link inside the repository resolves that link, so a lost row named through it passes with exit 0

```seal
severity: should
location: `skills/verify/scripts/unverified_check.py:1091-1104`, `skills/verify/scripts/unverified_check.py:941-942`, `seal/threads/1793504229-a-linked-memo-named-as-the-argument/frame/plan.md:45`, `tests/skills/test_unverified_check.py:1609`
evidence: executed `python3 round-2/test_tmp_probe.py (each fixture run with the 48d035aa, ab958884 and f50c0e26 scripts)`, `bin/test tests/skills/test_unverified_check.py -q (with the fix below applied to the clone)`, `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -k test_accepts_a_link_a_parent_does_not_step_out_of_under_its_own_name (at HEAD's script)`
regression: round-1
```

Why it matters: the unit is `absolute` (`skills/verify/scripts/unverified_check.py:1091-1104`), which b7d19345 added to answer round 1's *Not judged* row on `..`. `frame/design.md` *Scope* item 1 keeps every component inside the repository as the person named it, and `frame/plan.md:45` reads a `..` physically by resolving "the part of the path up to its last `..`"; `absolute` does exactly that, and so it also resolves the links the `..` never steps out of, which the physical reading does not need, and the defect comes from the judgment's rule being wider than its own grounds.

Take `specs/L`, a directory at the base holding `gaps.md` with two rows and a subdirectory `x`. The branch moves it to `specs/D`, leaves `specs/L` as a link to `D`, and drops a row. The probe ran each script on each spelling:

- Named `specs/L/gaps.md`: ab958884 and f50c0e26 both exit 1 with `specs/L/gaps.md:1  2 rows at HEAD, 1 here`.
- Named `specs/L/x/../gaps.md`, or `specs/L/x/..`: ab958884 exits 1, and f50c0e26 exits 0 with nothing reported.
- With the memo deleted instead, `specs/L/x/../gaps.md` exits 2 at f50c0e26 with `no such path ... and nothing under it at HEAD either`. That is false, since the base held `specs/L/gaps.md`. ab958884 exits 1 with `present at HEAD and not here`.

The cause is in `absolute`. It hands `specs/L/x/..` whole to `real()`, which resolves `L` to `D` on the way. `cd -P specs/L/x/..` lands in the directory `specs/L` names, because `x` is no link. So keeping `L` as named reads the `..` the way the file system does. The physical reading only has to resolve a component the `..` steps out of, and only where that component is a link.

The released base exits 0 on the lost row too, since it resolved every link. So this is no regression against 0.27.0. It is a regression against round 1's target, and it is the issue's own class: a named link inside the repository read as its target. The fix pass's two `..` cases do not reach it. `Test_as_named::test_accepts_a_parent_after_a_link_as_the_file_system_reads_it` puts the `..` directly after the link, and `Test_repository_of`'s case puts it after a link out of the repository.

The comment in `#overviews` (`:941-942`) says "nothing below it is resolved". That has been false since b7d19345 wherever a `..` steps out of a link, and it stays false under the fix, so the fix rewrites it in place. Other readers of the argument still read `..` by its text through `os.path.abspath`: `settled_root`, `absent_root`, `unwritten_root` and `nearest_existing`. They did so at 48d035aa as well, and none of them holds a base listing against a tree path, so they are outside this finding.

The fix, applied to the clone: the module passed, 388 cases, every `..` fixture of the probe exited 1, and the case below failed at HEAD's script (`AssertionError: ... 'specs/1780000000-work/gaps.md' == ... 'specs/hop/gaps.md'`) and passed under the fix. The `frame/plan.md:45` row is the orchestrator's. Its second sentence becomes: "Each `..` steps up from where the component before it leads: that component is resolved where it is a link, and every other component, a link the `..` does not step out of among them, is kept as named."

```python
# skills/verify/scripts/unverified_check.py, replacing absolute
def absolute(path):
    """`path` made absolute, each `..` in it read as the file system reads it.

    `os.path.abspath` drops `a/..` by its text, so where `a` is a link it
    named a directory the file system does not reach through that path, and
    the check compared a path nobody named. A `..` steps up from where the
    component before it leads: that component is resolved through `real`
    where it is a link, as `cd -P` and git do, and dropped by its text where
    it is not, since stepping out of a directory lands where it stands.
    Every other component, a link the `..` does not step out of among them,
    is kept as named (#1225)."""
    parts = pathlib.PurePath(path).parts
    # Windows drops `a\..` by its text before any link is read, and
    # `ntpath.realpath` does the same, so the textual reading is its own.
    if os.pardir not in parts or os.name == "nt":
        return os.path.abspath(path)
    # Precondition: `os.getcwd()` is already a real path, and
    # `os.path.islink` asks about the last component with every link before
    # it followed. A component that does not exist is no link, and is
    # dropped by its text, as `os.path.realpath` drops it.
    if os.path.isabs(path):
        here, parts = parts[0], parts[1:]
    else:
        here = os.getcwd()
    for part in parts:
        if part != os.pardir:
            here = os.path.join(here, part)
            continue
        if os.path.islink(here):
            here = real(here)
        here = os.path.dirname(here)
    return here

# skills/verify/scripts/unverified_check.py, #overviews, the comment
        # The argument is read through `as_named`, which resolves the way to
        # the repository's top and a link a `..` steps out of, and keeps
        # every other component as named.
```

```python
# tests/skills/test_unverified_check.py, in Test_as_named after
# test_accepts_a_parent_after_a_link_as_the_file_system_reads_it
    def test_accepts_a_link_a_parent_does_not_step_out_of_under_its_own_name(
        self, plain, tmp_path
    ):
        """`hop/x/..` lands in `hop` itself where `x` is no link, so `hop`, a
        link inside the repository, keeps its own name, as it does where the
        path holds no `..`."""
        d = copy_of(plain, tmp_path)
        (d / "specs" / WORK / "x").mkdir()
        symlink_or_skip(WORK, str(d / "specs" / "hop"), True)
        given = os.path.join(str(d), "specs", "hop", "x", os.pardir, "gaps.md")
        assert UC.as_named(given) == os.path.join(
            os.path.realpath(str(d)), "specs", "hop", "gaps.md"
        )
```

The Windows line rests on the phase record's reading of CPython's `ntpath.py`, which this round did not re-read. No Windows run reached it.

## Confirmations

```seal
confirms: round-1#1
```
What holds: a memo deleted behind a link inside the repository is refused again, executed. I wrote round 1's probe again from its `## Probes` row and ran each fixture with the 48d035aa, ab958884 and f50c0e26 scripts. A tracked directory link with one of two memos deleted, named `specs/a`, gives 1, 0 and 1. An untracked `view -> specs` with one memo deleted, named `view`, gives 1, 0 and 1. The only memo deleted behind the link gives 1, 2 and 1. The deleted memo named through the link gives 1, 2 (`nothing under it at HEAD either`) and 1. A dropped row behind the link gives 1 on all three. At HEAD each deletion line is the one 48d035aa prints. The issue's P1 and P8 still exit 1 at HEAD, and so does P1 named from a sibling directory through `../`. The fix touches the four places round 1 named: the typo check (`unverified_check.py:1716`), the prefixes and `here` (`:1805-1806`), and `spellings` (`:1106-1131`). `Test_main::test_refuses_a_memo_deleted_behind_a_link_inside_the_repository` (`tests/skills/test_unverified_check.py:2501`) carries round 1's case with a third shape for the typo check. The module passed at HEAD, 388 cases, executed.

```seal
confirms: none
```
What matched: the fix pass's argument against round 1's paste-ready fix holds, executed. Round 1 read the base under two spellings, the path as named and the real path, and held `here` to the same two. I put round 1's `here` into the clone through `Edit` and ran the named-link cases. `test_refuses_a_row_lost_through_a_link_the_person_names[a linked tree holding a file link]` and `test_accepts_a_link_the_person_names_that_lost_no_row[a linked tree holding a file link]` failed. The second one printed `specs/1780000001-other/gaps.md:1  present at HEAD and not here` for a memo that is there. The base lists that memo at `specs/OTHER/gaps.md`, which is neither the named `view/OTHER/gaps.md` nor the real `specs/WORK/gaps.md`. So round 1's fix would have shipped a false deletion line, and `spellings` was the change the finding called for. With the lost row at HEAD, the probe prints the same two lines 48d035aa prints, for `specs/W` and `specs/O`. ab958884 printed only the first.

```seal
confirms: none
```
What matched: the shape `spellings` cannot make, an upper link kept with a lower one resolved, leaves no `must`, executed and read. The probe built it. `specs/L1` was a directory at the base holding `X/gaps.md` and a tracked link `L2 -> X`. The branch moved it to `specs/D`, left `specs/L1 -> D`, and dropped a row. Named `specs/L1/L2/gaps.md` or `specs/L1/L2`, all three scripts exit 0, so nothing regressed against the release or against round 1's target. Named `specs/L1`, or `specs/L1/X/gaps.md`, ab958884 and HEAD exit 1 and 48d035aa exits 0. For the shape to arise, the base must already hold a link below a directory that the branch turns into a link, and the person must name a path through both. The plugin's layout puts no link under `seal/threads/`, so a pull request cannot build the shape against a base that lacks the lower link. It is disclosed in `gaps.md:18` and in the phase record (`trail/phases/phase-1.md:52`), with the reason that a second resolver would be owed. The fix pass says the list of spellings is whole apart from this shape. That holds: the spellings of one file on disk are the subsets of its links resolved, and `spellings` gives every subset that resolves a prefix of the path, read at `unverified_check.py:1106-1131`. The claim assumes a link that stood at the base still points where it did. A retargeted link gives the base a spelling of another file, and design *Scope* item 3 already owes that path no comparison at the base.

```seal
confirms: none
```
What matched: the sweep table in `trail/phases/phase-1.md` *Round 1's fix pass* is built by a method that makes the list whole, read. It takes the module apart into its seven `subprocess.run` sites and every site that turns a tree path into a repository-relative one. Opened at HEAD: `grep -n` for `subprocess.`, `relpath` and `repo_relative(` lists the same sites. I checked each `safe` row against the code. The first arm reads the real path, which `ls-tree` spells. `overviews_at`'s reference-root filter treats a prefix as named where it sits under a reference root, so the `specs` spelling of `view` keeps a reference root's memos in the base listing. The walk keeps them too, through `reference_rule` at the named path (`:1003-1023`). The settle test reads the disk, and `settled` reads the base alone. `tree_at`, `_text_at` and `open_record_rows` are not reached from `main`. The four `fixed` rows are the four places round 1 named, and the probe above shows each refusing.

```seal
confirms: none
```
What matched: the second arm compares each spelling once and names the spelling it compared, read and executed. `owed.setdefault` (`:1777-1784`) keys on the spelling. Two scanned paths that share a spelling reach one file on disk, since resolving a component changes the spelling and not the file. The line is built from `under_root(root, at)` (`:1794`), a change a person sees, and mutant 7 of the phase record pins it. Where a spelling leaves the repository part way, through a link to a directory outside it, `mode_at` and `show` get a `../` path that git refuses, so the arm reports nothing and nothing crashes. The probe's `LEAVE` fixture exits 0 at HEAD, as at ab958884.

```seal
confirms: none
```
What matched: each new test, read against its group, covers something its group did not. `Test_spellings` tests a new function. `Test_repository_of`'s `..` case is the one case where `repository_of` reads through `absolute` (mutant 9). The fourth `NAMED_LINK` shape is the only case whose base spelling is neither the named path nor the real one. The `named` parameter of `test_accepts_a_link_to_a_file_beyond_the_repository_as_not_compared` is the only case that hands `spellings` a spelling with no relative form (mutant 10). `bin/seal layout --pairs tests/skills/test_unverified_check.py` exits 0 with 0 pairs, executed.

```seal
confirms: none
```
What matched: the fold at f50c0e26, read. Design's scenario row *A tree reached through a link* now names a path through a link inside the repository and cites `Test_main::test_refuses_a_memo_deleted_behind_a_link_inside_the_repository`, which exists at `tests/skills/test_unverified_check.py:2501`. The plan's *Verified by* cell names `Test_repository_of` and `Test_spellings`, and the cell's command with both classes gives 101 passed in the clone, executed. `gaps.md` names #1238. `gh issue view 1238` shows it open, in milestone `backlog: gates & hooks`, titled for the macOS case fold, executed. Round 1's close block reads `verdict: fixed b7d19345`, and b7d19345 touches `skills/verify/scripts/unverified_check.py`, a path round 1's `location:` names.

```seal
confirms: none
```
What matched: the changelog fragment states what the probe shows, read and executed. Three named-link runs that exited 0 now exit 1. A memo deleted behind a link is still reported `present at <base> and not here`. P8 moved from exit 2 to exit 1. The fragment says nothing of `..`. Against the released base, nothing about `..` changes that a person sees, except finding 1's shape, which 48d035aa also passed. `uvx ruff check` and `uvx ruff format --check` on the two changed files exit 0 in the clone, executed.

```seal
confirms: none
```
What matched: the label on the broad gate is honest. `gaps.md` lists the full suite and the repository-wide lint as unverified, with the orchestrator through `seal gate` as the answerer. No record on the branch claims a broad run, and this round ran none. Once finding 1 is closed, what comes due is the orchestrator's broad run, then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `spellings`, `as_named` and finding 1's fix behave on Windows as read: `ntpath.realpath` giving the disk's case and dropping `..` by its text, and git's case-sensitive lookup answering None at a typed spelling. No run reached a Windows machine | `skills/verify/scripts/unverified_check.py:1061-1131` | the Windows legs of `.github/workflows/test.yml` on this pull request, as `gaps.md` *Not verified* names |
| The full suite, the repository-wide `ruff check` and `ruff format --check` | the branch at f50c0e26 | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 round-2/test_tmp_probe.py`, from clones at f50c0e26, ab958884 and 48d035aa, each fixture run with each clone's script, `--baseline HEAD` | Round 1's fixtures, in the order 48d035aa, ab958884, f50c0e26: tracked directory link, one of two deleted: 1, 0, 1. Scanned: 1, 1, 1. Deleted memo named through the link: 1, 2, 1. Untracked `view`: 1, 0, 1. Only memo deleted: 1, 2, 1. Dropped row: 1, 1, 1. P1 named: 0, 1, 1. P1 through `../`: 0, 1, 1. P8: 2, 1, 1. Mutant 5's layout with nothing lost: 0, 0, 0, and with a row lost: 1 with two lines, 1 with one line, 1 with two lines. The open shape named through both links or the lower link: 0, 0, 0. Named the upper link, or through it alone: 0, 1, 1. `specs/L/x/../gaps.md` and `specs/L/x/..` with a row lost: 0, 1, 0. With the memo deleted: 2, 1, 2. `specs/L/gaps.md`: 0 or 2 at 48d035aa, 1 at ab958884 and at f50c0e26. A link to a directory outside the repository holding a link: 2, 0, 0, no traceback |
| `bin/test tests/skills/test_unverified_check.py -q` at f50c0e26 | EXIT=0, 388 passed |
| `bin/test tests/skills/test_unverified_check.py -q -k "Test_real or Test_overviews or Test_unique_by_target or Test_main or Test_as_named or Test_repository_of or Test_spellings"` at f50c0e26 | 101 passed |
| Round 1's two-spelling `here` put into the clone through `Edit`, then `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -rf -k "test_accepts_a_link_the_person_names_that_lost_no_row or test_refuses_a_row_lost_through_a_link_the_person_names"` | 2 failed, both `[a linked tree holding a file link]`, one printing a false `present at HEAD and not here`; 5 passed. Taken back through `Edit` |
| Finding 1's `absolute` put into the clone through `Edit`, then the module, the probe, and finding 1's case | The module passed, 388. Every `..` fixture exited 1. The case passed, and with `absolute` back at HEAD's bytes it failed with `AssertionError`. Both edits taken back through `Edit`, and `git status --short` in the clone was empty |
| `bin/seal layout --pairs tests/skills/test_unverified_check.py` | EXIT=0, 1 file read, 0 pairs |
| `uvx ruff check` and `uvx ruff format --check` on the two changed files | EXIT=0 and EXIT=0 |

The probe file, the three clones and the fixtures were removed before hand-back.
