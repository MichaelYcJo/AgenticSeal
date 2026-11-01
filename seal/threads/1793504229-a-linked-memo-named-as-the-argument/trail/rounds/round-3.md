# Review round 3: 1793504229-a-linked-memo-named-as-the-argument

```seal
target: d9b5f6e3, fixes fca2bc9d..d9b5f6e3
```

This is the verifying round. Its target is the diff from round 2's record (fca2bc9d) to HEAD: the fix commits a06475d7 and f688d596, the phase record at 6430c61a, and the orchestrator's plan row and close block at d9b5f6e3. The base is `origin/release/v0.27.1`, whose merge base with HEAD is 48d035aa. No `seal/parity.md` is declared, so no original is compared and no `original:` line is owed. The record language is English, since `seal/config.md` has no `Record language` row.

Carried from rounds 1 and 2, not re-established: where the presence check, the typo check and the second arm stand in `main`; that `ls-tree -r` lists a tracked link as one blob under its own name and nothing through it; and the layouts of round 2's probe fixtures, written again from its `## Probes` row. Re-derived this round: every verdict below. The fixtures ran at `main` level with the scripts of 48d035aa, f50c0e26 and HEAD, and the fix diff was read whole, its Windows branch included.

**What the walk decides, and what it does not.** The orchestrator asked whether the walk settles the mechanism each round has found a regression in: how a named path is spelt against the base. On POSIX it settles the `..` part. Every `..` fixture below lands where `cd -P` lands and is compared under the base's spelling, and none passes a lost row. The mechanism as a whole is `spellings`, and the walk does not settle that. `spellings` makes the base's spellings from the named path by resolving its prefixes through `real()`, so it only ever moves from the named path toward the real path. Four shapes stay outside it:

- A link kept above a link resolved. This exits 0 on a lost row at all three scripts (executed, the open shape). It is disclosed, and its stated reason no longer holds (finding 3).
- An old name that is now a link to a directory on the named path. Take `specs/H`, a directory at the base, moved to `specs/D`, with `specs/H -> D` left behind. Naming `specs/D/a/gaps.md` exits 0 on a lost row, and so does a `..` whose link text names `D`. This holds at 48d035aa and f50c0e26 alike (executed, W3). The issue does not report it.
- The macOS case fold, #1238.
- Windows, where `absolute` reads `..` by its text. Finding 1 is about the cases that pin it.

All four have one cause. The check lists spellings from one end of the path. It does not ask the file system whether a path the base lists and a path the scan read are now the same file. `## Not judged` puts that question to the orchestrator.

## Findings

### 1. Three `..` cases pin the POSIX walk's result, but `absolute` reads `..` by its text on Windows, so they fail on the Windows legs

```seal
severity: must
location: `tests/skills/test_unverified_check.py:1640-1653`, `tests/skills/test_unverified_check.py:1609-1624`, `tests/skills/test_unverified_check.py:1568-1578`, `skills/verify/scripts/unverified_check.py:1105-1108`
evidence: executed `bin/test tests/skills/test_tmp_round3.py -p no:xdist -s -q -rf (os.name set to "nt" in the script module, the three cases as at HEAD)`, `bin/test tests/skills/test_tmp_round3b.py -p no:xdist -s -q -rf (os.name set to "nt" in both modules, the three cases as patched below)`, `bin/test tests/skills/test_unverified_check.py -q (patched)`
regression: round-2#1
```

Why it matters: the unit is `Test_as_named::test_accepts_a_link_above_the_link_a_parent_steps_out_of_under_its_own_name` (`tests/skills/test_unverified_check.py:1640-1653`), which a06475d7 added. The same commit made `absolute` return `os.path.abspath(path)` when `os.name == "nt"` (`skills/verify/scripts/unverified_check.py:1105-1108`). `frame/plan.md:45` and `:47` read a `..` as the file system reads it, and `trail/phases/phase-1.md:13` says Windows reads it by its text. The fix built that reading for Windows, but the case it added asserts the POSIX result on every platform, so the defect comes from the case and not from the code.

On Windows, `specs\hop\jump\..\gaps.md` goes through `os.path.abspath`, which gives `specs\hop\gaps.md`. The case expects `specs\hop\a\gaps.md`. `ntpath.abspath` calls `normpath` before anything reads a link, and `ntpath.realpath` does the same at its first line (CPython 3.12.11's `ntpath.py:582-585` and `:708-709`, read). Two older cases have the same defect. `Test_as_named::test_accepts_a_parent_after_a_link_as_the_file_system_reads_it` (`:1609-1624`) expects `deep\WORK`, and the textual reading gives `specs\WORK`. `Test_repository_of::test_accepts_a_parent_after_a_link_as_the_file_system_reads_it` (`:1568-1578`) expects the second repository, and `ext\..` read by text is the first. Both came in at b7d19345. At f50c0e26, Windows went through `ntpath.realpath`, which also normalizes first, so both were already red there. Round 2 did not read them for Windows.

The probe set `os.name` to `"nt"` in the script module alone, and the three cases failed with exactly those paths. Every other case in the two classes passed. This shows the branch, not `ntpath`. `tests/conftest.py#symlink_or_skip` says a GitHub `windows-latest` runner holds the privilege to make links, so these cases run there and do not skip. `.test_durations`, which only the Windows legs store (`.github/workflows/test.yml:105-108`), gives `Test_main::test_accepts_a_tracked_link_counted_once_and_not_deleted` 0.96 s. That suggests link cases do run on those legs (read). No Windows run reached this branch, so the red leg itself is unverified. The answerer is the Windows legs of `.github/workflows/test.yml` on this pull request.

The fix gives each case the result each platform's reading gives. With it applied to the clone, the module passed (391), and the three cases passed with `os.name` set to `"nt"` in both modules. `uvx ruff check` and `uvx ruff format --check` on the file exited 0. The `skipif` form is wrong here for the reason `symlink_or_skip`'s docstring gives: it would drop the Windows reading from every leg.

```python
# tests/skills/test_unverified_check.py, Test_repository_of::test_accepts_a_parent_after_a_link_as_the_file_system_reads_it
        symlink_or_skip(str(second / "inner"), str(d / "ext"), directory=True)
        # Windows drops `ext\..` by its text, which lands in the first.
        landed = d if os.name == "nt" else second
        assert same_path(UC.repository_of(str(d / "ext" / "..")), landed)

# Test_as_named::test_accepts_a_parent_after_a_link_as_the_file_system_reads_it
        given = os.path.join(str(d), "specs", "hop", os.pardir, WORK, "gaps.md")
        # Windows drops `hop\..` by its text before any link is read.
        landed = "specs" if os.name == "nt" else "deep"
        assert UC.as_named(given) == os.path.join(
            os.path.realpath(str(d)), landed, WORK, "gaps.md"
        )

# Test_as_named::test_accepts_a_link_above_the_link_a_parent_steps_out_of_under_its_own_name
        given = os.path.join(str(d), "specs", "hop", "jump", os.pardir, "gaps.md")
        # Windows drops `jump\..` by its text before any link is read.
        landed = ("hop",) if os.name == "nt" else ("hop", "a")
        assert UC.as_named(given) == os.path.join(
            os.path.realpath(str(d)), "specs", *landed, "gaps.md"
        )
```

Precondition, beside the OS boundary: Win32 path handling drops `a\..` by its text before any reparse point is read. The code's comment at `:1105-1106` already assumes this, and no run here checked it.

```seal
verdict: fixed b46c616b
answer: Fixed by removing the reading the three cases pinned, not by the paste-ready fix. `frame/plan.md` *Judgments of the run*, the `..` row at 9acfafe1, reads a path that holds a `..` as the release did, by `real(path)`. So `absolute` now gives `real(path)` for such a path and `os.path.abspath(path)` for every other one, with no walk and no branch on `os.name`. `Test_as_named` keeps one `..` case, `test_accepts_a_path_holding_a_parent_as_real_reads_it`, on the layout of the link-above case, and it asserts `as_named(given) == os.path.realpath(given)`. Its other `..` cases are removed, because under the decision each pins the same equality and the kept layout fails every mutant they fail. `Test_repository_of::test_accepts_a_parent_as_real_reads_it` asserts that the repository is `os.path.realpath(given)`, since `ext/..` lands at a repository's top under either platform's reading. Neither case expects one platform's result, so the paste-ready fix's per-platform `landed` is not needed, and both sides call the same `realpath` on Windows (read). The `as_named` case failed against d9b5f6e3's script with `.../hop/a/gaps.md` against `.../<WORK>/a/gaps.md` (executed). The `repository_of` case cannot fail there: on POSIX the walk lands in the directory `real` lands in, and on Windows both drop the `..` by its text. Two `seal mutate` runs on the `..` branch, `real(path)` replaced by `os.path.abspath(path)` and by `real(os.path.abspath(path))`, each failed both cases (executed). The module passed with 388 cases, and the phase-boundary set of 30 modules passed with 2395 and the same 9 skips (executed). Whether the link cases run on the Windows legs stays with those legs, as `gaps.md` *Not verified* names.
```

### 2. A link loop spends the walk's budget and then climbs one directory per link, so `specs/loop/..` is named "not in" a repository

```seal
severity: should
location: `skills/verify/scripts/unverified_check.py:1109-1131`, `tests/skills/test_unverified_check.py:1655-1664`, `seal/threads/1793504229-a-linked-memo-named-as-the-argument/trail/phases/phase-1.md:13`
evidence: executed `bin/test tests/skills/test_tmp_round3.py -p no:xdist -s -q -rf (fixture W4, each script)`, `bin/test tests/skills/test_tmp_round3b.py -p no:xdist -s -q -rf (HEAD's absolute on W4, and W4 with the fix below)`, `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -k test_accepts_a_parent_stepping_out_of_a_link_loop_without_a_crash (the case below at HEAD's script)`
regression: round-2#1
```

Why it matters: the unit is the budget in `absolute` (`skills/verify/scripts/unverified_check.py:1109-1131`). a06475d7 added it, and f688d596 added its case. `frame/design.md` *Scope* item 1 and `frame/plan.md:47` say a named path is read as the file system reads it, and the comment at `:1109-1110` says that past 40 links "the walk leaves it where it stands". The code does not do that. Once `hops` is 0, the `while` stops following. But each level of the recursion still runs its own `here = os.path.dirname(here)` as it unwinds. So a loop climbs one directory for each link it spent, and the defect comes from where the budget stops the walk.

HEAD's `absolute` turns `<repo>/specs/loop/../a/gaps.md`, with `specs/loop -> loop/..`, into `/a/gaps.md` (executed). At `main`, W4 gives these exits, in the order 48d035aa, f50c0e26, HEAD. Named `specs/loop/..` with a row lost: 1, 1 and 2. HEAD prints `--baseline HEAD needs a git repository, and specs/loop/.. is not in one`, which is false. Named `specs/loop/../a/gaps.md`: 2, 2 and 2, and at HEAD the reason changes from `no such path ... nothing under it` to the same false `is not in one`. The case f688d596 added asserts only `os.path.isabs`, and `/a/gaps.md` passes it. So the case covers the `RecursionError` and nothing about where the path lands. A loop is an unlikely argument, and the run still exits nonzero. But it names a reason that is false, and the lost row goes unreported.

With the fix below in the clone, W4 gives 1, 2 and 1 for `specs/loop/..`, `specs/loop/../a/gaps.md` and `specs/loop`, which are 48d035aa's and f50c0e26's exits. The module passed (391). The rewritten case failed against HEAD's script with `AssertionError: assert '/' == '<tmp>/repo'` and passed under the fix. `uvx ruff check` and `uvx ruff format --check` on both files exited 0. The case pins "inside the repository" and not one exact path, because `os.path.realpath` reads a loop differently across Python versions. The runner here was CPython 3.14.3, and the floor is 3.12. The sentence in `trail/phases/phase-1.md:13`, "a loop such as `loop -> loop/..` gives a path back and raises no `RecursionError`", is rewritten to say the loop is read through `real`.

```python
# skills/verify/scripts/unverified_check.py, in absolute, replacing the budget comment to the return
    # Past 40 links, the most Linux's `open` follows, the chain is a loop,
    # such as `a -> a/..`, which the file system refuses (ELOOP), so no place
    # is where it lands.
    hops = 40

    def walk(here, parts):
        nonlocal hops
        for part in parts:
            if part != os.pardir:
                # An absolute part, the root of an absolute path or of a
                # link's text, replaces `here`.
                here = os.path.join(here, part)
                continue
            # `os.path.islink` asks about the last component with every link
            # before it followed, which is where that link stands. A
            # component that does not exist is no link.
            while os.path.islink(here):
                if not hops:
                    raise _LinkLoop
                hops -= 1
                text = pathlib.PurePath(os.readlink(here)).parts
                here = walk(os.path.dirname(here), text)
            here = os.path.dirname(here)
        return here

    try:
        return walk(os.getcwd(), parts)
    except _LinkLoop:
        # Stopping the walk where the budget ran out left each level of the
        # recursion to step up once more, so a loop climbed to `/` and the
        # run named the path "not in" a repository. `real` reads the loop as
        # the check did before the walk.
        return real(path)


class _LinkLoop(Exception):
    """`absolute` met more links than the file system follows."""
```

```python
# tests/skills/test_unverified_check.py, Test_as_named, replacing the loop case's docstring and assertion
        """`loop -> loop/..` leads nowhere the file system reaches, and
        following its text had no end, so the walk stops where `open` would
        and reads the path as `real` does, inside the repository. Stopping
        where the budget ran out climbed one directory for each link spent,
        to `/`."""
        d = copy_of(plain, tmp_path)
        symlink_or_skip(os.path.join("loop", os.pardir), str(d / "specs" / "loop"))
        given = os.path.join(str(d), "specs", "loop", os.pardir, "gaps.md")
        top = os.path.realpath(str(d))
        assert os.path.commonpath([UC.as_named(given), top]) == top
```

Precondition: `real` is `os.path.realpath`, which the Python documentation says resolves a loop as far as it can and raises nothing when `strict` is false. The fix assumes nothing else.

```seal
verdict: fixed b46c616b
answer: Fixed by the removal. The walk and its 40-link budget left `absolute` at b46c616b, so a loop is read as `os.path.realpath` reads it, as at 48d035aa, and nothing climbs once a budget runs out. The paste-ready `_LinkLoop` fallback and its rewritten case were not applied, because they repair a walk that no longer exists. The loop case `test_accepts_a_parent_stepping_out_of_a_link_loop_without_a_crash` went with the walk, since a loop is now no branch of its own: a path that holds a `..` goes to `real` whatever links it holds, and `Test_as_named::test_accepts_a_path_holding_a_parent_as_real_reads_it` pins that branch. With `specs/loop -> loop/..` in a fresh repository, `as_named` gave `<repo>/a/gaps.md` for `specs/loop/../a/gaps.md` and `<repo>` for `specs/loop/..`, both inside the repository, and `repository_of` gave `<repo>` for each (executed, CPython 3.12.11, a scratch directory, then removed). `trail/phases/phase-1.md:13` is rewritten in place at cd5fb330 and states no budget and no loop.
```

### 3. `gaps.md` keeps the shape `spellings` cannot make open because it needs a per-link reader, and `absolute` is now that reader

```seal
severity: should
location: `seal/threads/1793504229-a-linked-memo-named-as-the-argument/gaps.md:18`
evidence: read `seal/threads/1793504229-a-linked-memo-named-as-the-argument/gaps.md:18`, `skills/verify/scripts/unverified_check.py:1124-1127`, `skills/verify/scripts/unverified_check.py:1134-1159`, `seal/threads/1793504229-a-linked-memo-named-as-the-argument/trail/phases/phase-1.md:52`
```

Why it matters: `gaps.md` *Not done* (`:18`) gives two reasons for leaving open the spelling that keeps a link above a link it resolves. The first is that "giving that spelling needs a reader that resolves one link at a time through `os.readlink`, which is a second resolver beside `real()`". a06475d7 added exactly that reader. `absolute` follows one link by its own text through `os.readlink` and keeps the link above it as named (`skills/verify/scripts/unverified_check.py:1124-1127`). So the cost the sentence names has already been paid, and the sealer and the settle will weigh the deferral on a reason the tree no longer bears. Contract rule 19 asks that the commit which changes a fact also fix what stood on it, and a06475d7 left this sentence. The second reason, that no layout of the plugin makes the shape, still holds. Round 2 checked it, and this round reran the fixture: named `specs/L1/L2/gaps.md` or `specs/L1/L2`, a lost row exits 0 at 48d035aa, f50c0e26 and HEAD (executed, in `## Probes`).

The fix pass can take either way. One way reuses the walk's step in `spellings`: for each link on the path, follow it by its own text and keep the links above it as named. That closes this shape and leaves the other three that `## Not judged` names. The other way rewrites the sentence so the deferral rests on the reason that holds:

```markdown
`spellings` does not give a spelling that keeps a link above a link it resolves, because `real()` resolves every link before the one it is asked about (`trail/phases/phase-1.md` *Round 1's fix pass*, *Where the class stays open*). The base spells a path that way only where a component that was a directory at the base is now a link, and holds below it a link that stood at the base too. `absolute` already follows one link by its own text and keeps the link above it as named, and `spellings` could take that step for the base's spellings. It is left out because no layout of the plugin makes the shape: the plugin puts no link under `seal/threads/`, so a pull request cannot build it against a base that lacks the lower link.
```

```seal
verdict: fixed cd5fb330
answer: Fixed by rewriting the sentence in place, in my own words and not as the paste-ready text. b46c616b removed the walk, so the paste-ready sentence that `absolute` already follows one link by its own text would no longer be true. The sentence about a second resolver is gone. The paragraph now says that no layout of the plugin makes the shape, and that it is #1240's, because the shape comes from matching the base's listing to the scan by spellings of one path. The same commit adds two paragraphs to `gaps.md` *Not done*. The first is the old name left behind as a link, from the preamble and W3, which held at 48d035aa. The second is the path that holds a `..`, now read through its real path: a link the person names on it is read as its target, and the release read it that way too. Both cite #1240. The case fold stays with #1238, as it stood.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: on POSIX, a `..` after a link the `..` never leaves keeps that link's name, and a lost row named through it is refused (executed). The round-2 shape (`specs/L` a directory at the base, now a link to `D`, with `x` no link) gives these exits in the order 48d035aa, f50c0e26, HEAD. Named `specs/L/x/../gaps.md` or `specs/L/x/..` with a row lost: 0, 0, 1, with `specs/L/gaps.md:1  2 rows at HEAD, 1 here`. With the memo deleted: 2, 2, 1, with `specs/L/gaps.md:1  present at HEAD and not here`. The false exit 2 round 2 found is gone. The wider form the fix pass argued for holds at `main` too. W1 (`specs/H` a directory at the base, now a link to `D`, with `D/jump -> a/b`), named `specs/H/jump/../gaps.md`, gives 0, 0, 1 with a row lost and 2, 2, 1 with the memo deleted, each line naming `specs/H/a/gaps.md`. W2, a link whose text holds a `..` that steps out of the link above it (`D/jump -> ../H/sub`), gives 0, 0, 1. The fix pass's argument against round 2's paste-ready form holds, read: `real(here)` at `specs/hop/jump` resolves `hop` as well, since `os.path.realpath` resolves every component. The walk calls `os.readlink` on the stepped-out link alone (`skills/verify/scripts/unverified_check.py:1124-1127`). `a06475d7` touches `skills/verify/scripts/unverified_check.py`, a path round 2's `location:` names. The module passed at HEAD, 391 cases (executed).

```seal
confirms: none
```
What matched: round 1's and round 2's fixtures keep their exits at `main` level (executed). They were written again from round 2's `## Probes` row, and the exits below are in the order 48d035aa, f50c0e26, HEAD. A tracked directory link with one of two memos deleted: 1, 1, 1, named `specs/a`, scanned or through the link. An untracked `view -> specs` with one memo deleted, the only memo deleted, or a row dropped: 1, 1, 1. Issue P1 named, and named from `specs/b` through `../a/gaps.md`: 0, 1, 1. P8: 2, 1, 1. Mutant 5's layout with nothing lost, named `view`: 0, 0, 0. With a row lost, named `view`: 1, 1, 1. The second probe printed both deletion lines, for `specs/W/gaps.md` and `specs/O/gaps.md`, at 48d035aa and at HEAD, named `view` or `specs`. The open shape named through the upper link only (`specs/L1`, `specs/L1/X/gaps.md`): 0, 1, 1. A link to an outside directory that holds a link: 2, 0, 0, with no traceback. W5, a `..` out of the repository's top named through a link from outside it (`toplink/specs/../specs/a`, `toplink/../w5/specs`): 1, 1, 1.

```seal
confirms: none
```
What matched: the Windows branch of `absolute` reads `..` the way `ntpath` does (read). `ntpath.abspath` normalizes before it asks the system (`ntpath.py:582-585`, CPython 3.12.11), and `ntpath.realpath` opens with `path = normpath(path)` (`:708-709`). So at f50c0e26, Windows also dropped `..` by its text, and then resolved every link before the last `..` through `real()`. At HEAD it keeps those links as named. On Windows the round-2 shape therefore moves from a passed lost row to a compared one, as on POSIX. Finding 1 is about the cases, not this branch. Whether Win32 itself reads `..` by text is a platform fact that no run here checked, and `## Not judged` keeps it.

```seal
confirms: none
```
What matched: the records the fix pass and the orchestrator rewrote state the code as built, read. `frame/plan.md:45` and `:47` and `trail/phases/phase-1.md:13` say that a `..` follows only the link it steps out of, by that link's text, read from the directory that holds it, and that every other component keeps its name. The phase record also says that Windows reads `..` by text. `skills/verify/scripts/unverified_check.py:1092-1131` does each of these. The `#overviews` comment (`:941-943`) and the `absolute` docstring were rewritten in place. The phase record's loop sentence is the one exception, and it is finding 2's.

```seal
confirms: none
```
What matched: each new test, read against its group, covers something its group did not. `test_accepts_a_link_a_parent_does_not_step_out_of_under_its_own_name` is the one case with a `..` after a component that is no link. `test_accepts_a_link_above_the_link_a_parent_steps_out_of_under_its_own_name` is the one case whose stepped-out link has a link above it. The loop case is the one case that reaches the budget, though it pins only the absence of a crash (finding 2). `bin/seal layout --pairs tests/skills/test_unverified_check.py` exits 0 with 0 pairs (executed).

```seal
confirms: none
```
What matched: the label on the broad gate is honest. `gaps.md` lists the full suite and the repository-wide lint as unverified, and names the orchestrator, through `seal gate`, as the answerer. No record on the branch claims a broad run, and this round ran none.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the Windows legs run the link cases or skip them, and whether Win32 drops `a\..` by its text before any reparse point is read, as `absolute`'s Windows branch assumes. Finding 1's probe changed `os.name` and not `ntpath` | `skills/verify/scripts/unverified_check.py:1105-1108`, `tests/skills/test_unverified_check.py:1568-1664` | the Windows legs of `.github/workflows/test.yml` on this pull request, as `gaps.md` *Not verified* names |
| Whether the base's spellings should stop being listed from the named path and become a file-identity comparison. Each path the base lists would be read in the working tree as the file system resolves it, then held against what the scan read by `os.path.samefile`. That one comparison would cover all four shapes the preamble names, #1238's case fold among them. `frame/plan.md:28` rejected a base-listing loop because the prefixes still came from the argument; listing the whole base tree would not need them. That is a question about the design, not a defect of this diff | `skills/verify/scripts/unverified_check.py:1134-1159`, `seal/threads/1793504229-a-linked-memo-named-as-the-argument/frame/plan.md:28` | the orchestrator: a follow-up issue, or a re-frame of this work item |
| The full suite, the repository-wide `ruff check` and `ruff format --check` | the branch at d9b5f6e3 | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round3.py -p no:xdist -s -q -rf`, in a `git clone --no-local` at d9b5f6e3, each fixture run with the scripts of 48d035aa, f50c0e26 and HEAD, `--baseline HEAD` | The exits in each confirmation above and in findings 1 and 2. The open shape named `specs/L1/L2/gaps.md` or `specs/L1/L2`, with a row lost: 0, 0, 0. W3, with `specs/H` moved to `D` and named `specs/D/a/gaps.md`, or `specs/H/jump/../gaps.md` with `jump`'s text, absolute or relative, naming `D`: 0, 0, 0 with a row lost. W4, named `specs/loop/..`: 1, 1, 2 (`is not in one`). With `os.name` set to `"nt"` in the script module: 3 failed, the three cases of finding 1, and 8 passed |
| `bin/test tests/skills/test_tmp_round3b.py -p no:xdist -s -q -rf`, with findings 1's and 2's fixes put into the clone through `Edit` | HEAD's `absolute` on W4 gave `/a/gaps.md`. Under the fix, W4 gave 1, 2 and 1 for `specs/loop/..`, `specs/loop/../a/gaps.md` and `specs/loop`. Mutant 5's layout printed both deletion lines at 48d035aa and at HEAD. With `os.name` set to `"nt"` in both modules, the patched classes passed, 11 |
| `bin/test tests/skills/test_unverified_check.py -q`, with both fixes in the clone | EXIT=0, 391 passed. `uvx ruff check` and `uvx ruff format --check` on the two files: EXIT=0 and EXIT=0 |
| `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -k test_accepts_a_parent_stepping_out_of_a_link_loop_without_a_crash`, with the script back at HEAD's bytes and finding 2's case kept | EXIT=1, `AssertionError: assert '/' == '<tmp>/repo'` |
| `bin/test tests/skills/test_unverified_check.py -q` at d9b5f6e3, the clone back at HEAD's bytes | EXIT=0, 391 passed |
| `bin/seal layout --pairs tests/skills/test_unverified_check.py` | EXIT=0, 1 file read, 0 pairs |

The runner's interpreter was CPython 3.14.3. Both probe files, the fixtures, the clone and the extracted script trees were removed before hand-back.
