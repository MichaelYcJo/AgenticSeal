# Review round 1: 1793504229-a-linked-memo-named-as-the-argument

```seal
target: ab958884 against origin/release/v0.27.1
```

The base is `origin/release/v0.27.1` at 48d035aa. No earlier round exists, so no fact was carried: every coordinate below was opened this round. No `seal/parity.md` is declared, so no original is compared and no `original:` line is owed. The record language is English, since `seal/config.md` has no `Record language` row.

## Findings

### 1. A memo deleted behind a link inside the repository now passes with exit 0, where the base script refused it

```seal
severity: must
location: `skills/verify/scripts/unverified_check.py:1658`, `skills/verify/scripts/unverified_check.py:1669-1678`, `skills/verify/scripts/unverified_check.py:1759-1760`, `skills/verify/scripts/unverified_check.py:1060-1086`, `tests/skills/test_unverified_check.py:2412`
evidence: executed `python3 round-1/test_tmp_probe.py (each fixture run with the 48d035aa script and the ab958884 script)`, `bin/test tests/skills/test_unverified_check.py -q`, `bin/test tests/skills/test_tmp_round1.py -q -p no:xdist`
```

Why it matters: `docs/the-record-layout.md` *The fold, and what tells it from a deletion* says a closing memo removed from a directory that stays fails the run. This branch makes that check pass in a layout the base script refused.

The cause is how the presence check builds its prefixes. `as_named` keeps every component inside the repository as typed (`unverified_check.py:1080-1083`). The presence check then asks the base's `ls-tree` for memos under that spelling (`:1759`). But `ls-tree -r` never lists a path through a link: it lists a tracked link as one blob under its own name, and an untracked link not at all. So where a component inside the repository is a link, the prefix matches no line of the base listing, `gone` is empty, and nothing reports the deleted memo. The base script read the prefix from `real(p)`, which is the spelling the base lists.

The probe ran each fixture with both scripts:

- A tracked directory link `specs/a -> b`, standing at the base and now. `specs/b/one/gaps.md` is deleted, `specs/b/two/gaps.md` stays, and the run names `specs/a`. At 48d035aa it exits 1 with `specs/b/one/gaps.md:1  present at HEAD and not here`. At ab958884 it exits 0 with nothing reported. Scanning `specs` still exits 1.
- An untracked link `view -> specs` in the checkout, one of two memos deleted, the run naming `view`. At 48d035aa it exits 1; at ab958884 it exits 0.
- With the deleted memo the only one behind the link, ab958884 exits 2 with `no gaps.md found under specs/a — nothing was checked`. That is false, since the base held a memo there. Naming the deleted memo itself, `specs/a/gaps.md`, makes the typo check (`:1669-1678`) exit 2 with `nothing under it at HEAD either`. That is false too: the base held `specs/b/gaps.md`, which is that path. 48d035aa exits 1 in each case, naming the deletion.
- A dropped row behind the same links still exits 1 on both scripts. The row comparison reads real paths through `unique_by_target`, so only the presence check and the typo check lost the case.

The class is built from what produces the defect: every place that hands `ls-tree` the named spelling and expects the base's spelling back. That is the typo check (`:1676`) and the presence check's prefixes and its `here` set (`:1759-1760`). The other-volume refusal (`:1659`) asks only whether a relative form exists, so it is outside the class. A link is one way the named spelling differs from the base's. A second way should exist on Windows, though no run reached it: `ntpath.realpath` returns the case the disk holds, while `as_named` keeps the typed case of each component inside the repository. A component typed in another case (`Seal/threads`) then gives a prefix git's case-sensitive tree lookup matches nowhere, and the base script's `real(p)` gave the disk's case. So the phase record's claim that "a path with no link therefore keeps the exact spelling `real()` gave it before" holds on POSIX and fails on Windows (`unverified_check.py:1080-1083`, read).

The frame missed this layout. `frame/design.md:58` pins "a tree reached through a link ... with a memo deleted" only through `test_refuses_a_deletion_reached_through_a_linked_path` (`tests/skills/test_unverified_check.py:2412`). That case puts the link outside the repository, pointing at its top, where `as_named` resolves the link. No case puts the link inside the repository. The whole module passes at ab958884, 377 cases, with the defect in place, so nothing in the suite catches it.

The fix reads the base under both spellings: the path as named, and its real path where that lies inside the repository. It counts a file as here under both spellings. The real-path spelling is the one the base script used, so every layout it refused is refused again. The named spelling still carries #1225's cases. With this change applied to the scratch clone, all of the probe's fixtures exit 1, issue P1 and P8 included. The module passes with 377, and the case below fails twice at ab958884 (`assert 0 == 1`) and passes under the fix. Precondition: `real(p)` resolves every link, so a real path outside the repository gives a `..` form, which is dropped. A real path on another volume gives None, which is dropped too, and the other-volume refusal above already stopped that run.

```python
# skills/verify/scripts/unverified_check.py, in main, after `outside` is refused
        # Each spelling the base may hold an argument's memos under: the path
        # as named, which carries a named link's own path (#1225), and the
        # real path, since `ls-tree` lists nothing through a link and a
        # component inside the repository may be one.
        spelt = {
            p: sorted(
                {
                    rel
                    for rel in (
                        repo_relative(compared[p], root),
                        repo_relative(real(p), root),
                    )
                    if rel is not None and rel.split("/")[0] != ".."
                }
            )
            for p in args.path
        }

# the typo check
            if not overviews_at(root, base, spelt[p])

# the presence check
        prefixes = sorted({rel for p in args.path for rel in spelt[p]})
        here = {repo_relative(f, root) for f in files} | {
            repo_relative(os.path.realpath(f), root) for f in files
        }
```

```python
# tests/skills/test_unverified_check.py, in Test_main beside
# test_refuses_a_deletion_reached_through_a_linked_path
    @pytest.mark.parametrize(
        "tracked", [True, False], ids=["a tracked link", "a link of this checkout"]
    )
    def test_refuses_a_memo_deleted_behind_a_link_inside_the_repository(
        self, tmp_path, monkeypatch, capsys, tracked
    ):
        """`ls-tree` lists nothing through a link, so the base is read under
        the real path as well as the path as named, and a memo deleted behind
        a link inside the repository is reported as it was before #1225."""
        d = _committed(
            tmp_path,
            {
                f"specs/{WORK}/gaps.md": memo(CANONICAL),
                f"specs/{WORK}/keep.txt": "kept\n",
                f"specs/{OTHER}/gaps.md": memo(CANONICAL, OTHER),
            },
        )
        symlink_or_skip("specs", str(d / "view"), directory=True)
        if tracked:
            commit_everything_as_e(d, "the link")
        os.remove(d / "specs" / WORK / "gaps.md")
        monkeypatch.chdir(d)
        assert run(["view", "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "present at HEAD and not here" in out, out
```

The fix pass also owes the frame's scenario row and the changelog fragment a sentence for this layout, if the fix changes what they state.

```seal
verdict: fixed b7d19345
answer: Fixed wider than the paste-ready fix. `spellings` gives the path as named, then with the components through each one resolved, ending at the real path; the typo check, the presence check's prefixes and its `here`, and the second arm read every spelling, and the second arm's line names the spelling it compared. The two-spelling fix misses the spelling between them: with `view` a link of this checkout to `specs`, and a memo that was a file at the base now a link, it reports a memo that is there as `present at HEAD and not here`, which mutant 5 of `trail/phases/phase-1.md` *Round 1's fix pass* shows. The round's case is in `Test_main` with a third shape for the typo check, each seen red at ab958884's script, and a fourth `NAMED_LINK` shape pins the spelling between. The phase record's table names every place in the module that holds a base listing against a tree path, as fixed or safe. The Windows case fold is covered by reading and stays in `gaps.md` *Not verified*. The macOS case fold predates the work (executed at 48d035aa) and is in *Not done*. The changelog fragment carries the sentence; the frame's scenario row is the framer's and is left to the orchestrator. The `..` row of *Not judged* is built as `frame/plan.md` *Judgments of the run* decides, in `absolute`, with a case in `Test_as_named` and one in `Test_repository_of`.
```

## Confirmations

```seal
confirms: none
```
What matched: the issue's *Done when* holds. A file link named as the argument, whose target holds fewer rows than the base held at the link's path, exits 1 with `specs/a/gaps.md:1  2 rows at HEAD, 1 here`, the line naming the link's own path. The probe ran it with both scripts: 48d035aa exits 0 and ab958884 exits 1, executed. The case is `Test_main::test_refuses_a_row_lost_through_a_link_the_person_names` (`tests/skills/test_unverified_check.py:2427`), read, and the module ran green, executed.

```seal
confirms: none
```
What matched: the named link out of every repository (P8). 48d035aa exits 2 with `needs a git repository, and specs/a/gaps.md is not in one`. ab958884 exits 1, comparing the link's own path and listing the target under `not compared`. Executed by the probe. This is the phase record's claim that the out-of-every-repository case was red as `assert 2 == 1`. The premise holds: the base script exits 2 there. The phase record's other seen-red claims were not re-run.

```seal
confirms: none
```
What matched: the first departure, `repository_of` as a function of its own (`skills/verify/scripts/unverified_check.py:1039-1057`), read. It keeps Scope item 2's order: the real path's repository first, and the deepest link's only where that is None. `main`'s root (`:1622`) and `as_named` (`:1070`) both read it, which is the phase record's reason for a function of its own. The departure holds.

```seal
confirms: none
```
What matched: the second departure, `Test_repository_of` added beyond Scope item 5's list (`tests/skills/test_unverified_check.py:1544-1566`), read. Its first case pins a checkout linked from a directory that is itself a repository. No case pinned that layout before, and it is the one the rejected deepest-link alternative breaks. The class tests a function no earlier test covered. Read against its group, it covers something new. `seal layout --pairs` reports 0 pairs for the module, executed. The departure holds.

```seal
confirms: none
```
What matched: the third departure, the lost-nothing case with two shapes and not three (`tests/skills/test_unverified_check.py:2469`), read. For a file link and for a file under a linked directory, the presence check's prefix and the `here` entry are both the path as named, `specs/OTHER/gaps.md`. In both, the second arm runs because the path is not its own real path. A third parameter would therefore exercise no line the first does not. The departure holds. Finding 1 lies in the presence check, but in a layout this case does not reach, since here the base held a file at the named path.

```seal
confirms: none
```
What matched: the other departures the phase record names. First, the other-volume refusal now reads `as_named(p)` instead of `real(nearest_existing(p))` (`:1658-1659`). A relative form to `root` exists in exactly the cases it did before, read. Second, the second arm's condition `os.path.realpath(path) == path` has no case fold (`:1739`). A mistyped case makes `show` and `ls-tree` answer None at the typed spelling, so the arm adds no line and none is doubled, read. The presence check's half of the case question is finding 1's.

```seal
confirms: none
```
What matched: the five sites `frame/design.md` *Grounding* lists all read the argument through the new reader, and `real(` now stands only inside `as_named`, `repository_of` and `real` itself, read from the diff. The four sentences Scope item 4 names are rewritten in place (`:940-945`, `:1025-1036`, `:1166-1168`, `:1731-1737`), read. `git grep` for `resolved once`, `come through here` and `islink(path)` outside `seal/threads/` finds only sentences about the base revision and other readers' own links, executed. That is a search on wordings, so it is a sample, and the phase record says so.

```seal
confirms: none
```
What matched: the plan's *Verified by* command, `bin/test tests/skills/test_unverified_check.py -q -k "Test_real or Test_overviews or Test_unique_by_target or Test_main or Test_as_named or Test_repository_of"`, gives 90 passed in the clone at ab958884, executed, as the phase record states. `gaps.md` labels the full suite and the repository-wide lint `unverified`, with the orchestrator through `seal gate` as the answerer. That label is honest: this round ran no broad gate, and no record on the branch claims one.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `as_named` takes `os.path.abspath` first, so a `..` after a link is removed by text. `specs/a/../b` reads `specs/b` where `specs/a` links elsewhere. The base script, and `open()` on the same path, follow the link first. Only the phase record calls this deliberate: no frame sentence or case states it, and no changelog line tells a person. So it is a question, not a pass: is the textual reading the intended one, and if it is, does it owe a sentence in `as_named`'s docstring and a case? | `skills/verify/scripts/unverified_check.py:1073` | the orchestrator, who brings the framer's design in on the fix pass |
| Whether `as_named` and the case reasoning of finding 1 behave on Windows as read: `os.path.samefile` finding the top, and `ntpath.realpath` returning the disk's case. No run reached a Windows machine. | `skills/verify/scripts/unverified_check.py:1060-1086` | the Windows legs of `.github/workflows/test.yml` on this pull request, as `gaps.md` *Not verified* already names |
| The full suite, the repository-wide `ruff check` and `ruff format --check` | the branch at ab958884 | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 round-1/test_tmp_probe.py`, from a `git clone --no-local` at ab958884, each fixture run with that clone's script and a second clone's at 48d035aa, `--baseline HEAD` | Tracked directory link with one of two memos deleted, named `specs/a`: 48d035aa EXIT=1, ab958884 EXIT=0. Untracked `view -> specs`, the same deletion, named `view`: 1 and 0. The same with the only memo deleted: 1 and 2 (`nothing was checked`). The deleted memo named through the link: 1 and 2 (`nothing under it at HEAD either`). A dropped row behind the link: 1 and 1. Issue P1 named: 0 and 1. P1 scanned: 1 and 1. P8: 2 and 1. |
| `bin/test tests/skills/test_unverified_check.py -q -k "Test_real or Test_overviews or Test_unique_by_target or Test_main or Test_as_named or Test_repository_of"` at ab958884 | EXIT=0, 90 passed |
| `bin/test tests/skills/test_unverified_check.py -q` at ab958884 | EXIT=0, 377 passed. The defect of finding 1 stands at this commit, so no case in the module catches it |
| `bin/seal layout --pairs tests/skills/test_unverified_check.py` | EXIT=0, 1 file read, 0 pairs |
| Finding 1's fix applied to the scratch clone through `Edit`, then the probe, the module and `tests/skills/test_tmp_round1.py` (finding 1's case) | Every probe fixture exits 1. The module passes, 377. The case passes twice. With the edit taken back, the case fails twice at ab958884, `assert 0 == 1` |

Every probe file, both clones and the fixtures were removed before hand-back.
