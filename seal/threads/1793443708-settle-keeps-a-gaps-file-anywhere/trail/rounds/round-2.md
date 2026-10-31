# Review round 2: 1793443708-settle-keeps-a-gaps-file-anywhere

target: b00c434e, fixes e6c957da..b00c434e

## Findings

### 1. A settle case still makes its directory link with its own `os.symlink`, so a misbuilt fixture skips instead of failing

severity: should
location: `tests/skills/test_settle.py:1157-1164`
evidence: executed `bin/seal mutate tests/skills/test_settle.py --tests "bin/test tests/skills/test_settle.py -q -p no:xdist -rs -k link" --replace <trail.mkdir() removed>`, `git grep -n "os\.symlink\|\.symlink_to(" -- tests evals`
verdict: fixed d79bed62
reopens: round-1#2

The close holds for the coordinate round 1 named and not for the class. The answer drew the class as "every copy of a conftest helper in the files this phase touched", listed from the helpers this phase added. That method leaves out, by how it is built, any copy that stood in a touched file before the phase. One does. In `Test_main::test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none`, the `link` shape at `tests/skills/test_settle.py:1157-1164` makes its link inline: `os.symlink(held, trail / "rounds", target_is_directory=True)` inside a `try` that turns every `OSError` and `NotImplementedError` into `pytest.skip("this platform makes no symbolic link here")`. It has no check that the link's parent exists. It is the same copy of `tests/conftest.py#symlink_or_skip` that finding 2 named, in the same module, and it exists for the same reason: the shared helper took no directory flag. This fix pass gave the helper that flag in 851fb4cc, whose subject says "the settle's link cases make their links through conftest's symlink_or_skip". This case does not.

The defect reproduces here as finding 2 described it. With `trail.mkdir()` removed from the case's fixture, the `link` shape skipped as "this platform makes no symbolic link here" on a machine that makes links, and `seal mutate` reported the mutation as surviving (executed, `## Probes`). The same mutation against `symlink_or_skip` fails on "the link's parent does not exist", which this round reproduced for `Test_misplaced` (executed). Contract rule 12 asks for the class to be listed by a method that makes the list whole. A `git grep` for `os.symlink` and `.symlink_to(` over `tests` and `evals` lists every link the suite makes outside the helper (executed). Outside `tests/conftest.py`, it returns this case and three calls in `tests/skills/test_agentic_pytest_record.py:882`, `:904` and `:929`. Those three make links under `skipif(os.name == "nt")` with no `try`, so a misbuilt fixture there fails on POSIX rather than skipping. They are not instances of this defect, and this finding does not ask for them.

The fix replaces the inline `try` with the shared helper. `symlink_or_skip` is already imported at `tests/skills/test_settle.py:47`, and `os` and `pytest` stay in use elsewhere in the module. Precondition: `trail` exists, made at `:1154`, which the helper now asserts. `directory=True` keeps what the case passed before. Show the case failing with `trail.mkdir()` removed before committing (contract rule 15).

```python
        elif shape == "link":
            held = repo / "elsewhere"
            held.mkdir()
            (held / "round-1.md").write_text("# Review round 1\n", encoding="utf-8")
            symlink_or_skip(held, trail / "rounds", directory=True)
```

answer: The finding holds, and d79bed62 fixes it as proposed. The inline `try` around `os.symlink` is replaced by `symlink_or_skip(held, trail / "rounds", directory=True)`. With `trail.mkdir()` removed, `bin/seal mutate tests/skills/test_settle.py` now turns the `link` shape red on "the link's parent does not exist", where this round saw it survive as a skip (executed). Round 1's class was drawn from the helpers this phase added, so a copy that stood in a touched file before the phase fell outside it by how the list was built. This time the class is every link a case makes in the seven files this work item touches. Those files come from `git diff --name-only a83ce23e..HEAD` without the records. In them, `git grep -n -E "symlink|symlink_to|hardlink|os\.link\(|\.link_to\(|mklink|ln -s|CreateSymbolicLink|junction"` was run, setting aside the `symlink_or_skip(` calls (executed). It listed `tests/skills/test_settle.py:1162`, now fixed, and `tests/conftest.py:647`, the helper's own `os.symlink`. `tests/conftest.py:1412`'s `shutil.copytree(..., symlinks=True)` copies a template's links and makes none of a case's own, so it stands. The same search for `mkfifo` and `os.mknod`, the sibling helper `fifo_or_skip`'s class, finds only that helper. `README.md`, `README.ko.md`, `skills/settle/SKILL.md`, `skills/settle/scripts/settle.py` and `tests/text/test_settle_reads_before_it_removes.py` make no link. `tests/skills/test_agentic_pytest_record.py` is outside these files and stays as this round named it. The search reads spellings, so it is complete for the spellings listed, and a link made through another API would escape it. `bin/test tests/skills/test_settle.py -q -rs` gives 101 passed, none skipped (executed).

## Confirmations

confirms: round-1#1
The close holds. Step 4's paragraph is pinned clause by clause in `test_the_skill_states_the_settling_sessions_procedure` at `tests/text/test_settle_reads_before_it_removes.py:118-122`. The command block, the dry run's item and `--apply`'s item are pinned in the new case at `:165-192`, and each README edition's row at `:317-324` (read). Claimed: 16 pins, each seen red by `seal mutate`. That count is an aggregate. The diff adds 14 asserted strings: 3 in the procedure list, 9 in the new case and 1 per README edition. This round re-ran a sample of nine mutants (executed, `## Probes`). Seven deleted or cut a sentence of `skills/settle/SKILL.md`: step 4's first clause, step 4's clause on the pull request body, the dry-run item's last sentence, its "exact name" clause, `--apply`'s bold sentence, `--apply`'s last clause, and the command block's clause. Two removed each README edition's new clause. All nine were red, and the clone was clean after each. Claimed: the crafter departed from the proposed fix by making a new case instead of extending the `from` case. Found: `test_the_skill_says_a_from_locates_and_is_no_precondition` at `:150-162` is named for `from` and the policy write, so a separate case is the better home. The dry-run section quotes `## Not verified` at `skills/settle/SKILL.md:186`, so the proposed split on `"## "` would have cut the section above the new item. The new case cuts it at `"\n## "` from the raw text instead (read). Claimed: every clause of the six changed places is now pinned. Found: one clause is not, the dry-run item's "such as `trail/gaps.md` or a top-level `design.md`, each with the record it is named like" at `skills/settle/SKILL.md:191-192`. It gives examples, and the line format it describes is pinned in `tests/skills/test_settle.py` through the `not_read` helper, so this is no finding (read).

confirms: none
The new units hold. `symlink_or_skip`'s `directory=False` at `tests/conftest.py:626` passes on as `target_is_directory`, and the parent assertion still comes before the call (read). `git grep -n symlink_or_skip` lists every caller (executed). Every caller but `tests/skills/test_settle.py:732` passes two arguments, so the default keeps the behaviour they had. The switch of `released_item` and `records_in_place` to `conftest.py#write` at `tests/skills/test_settle.py:203` and `:698` matches what it replaced: `write` at `tests/conftest.py:1197-1201` makes the parent directories and writes UTF-8 text (read). The new case was read against its group. `bin/seal layout --pairs tests` names no pair for the module (executed). No other case in `tests/text/test_settle_reads_before_it_removes.py` reads the dry-run item or `--apply`'s new item (read). `bin/test tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py -q -rs` at b00c434e: 119 passed, none skipped (executed).

confirms: none
The records commit b00c434e changes only round 1's two `verdict:` lines and two `answer:` lines (executed, `git diff -U0 e6c957da..b00c434e -- seal`). Each `fixed` commit touches a path its finding's `location:` names: a7bca714 changes `tests/text/test_settle_reads_before_it_removes.py`, and 851fb4cc changes `tests/skills/test_settle.py` and `tests/conftest.py` (executed, `git show --stat`). The fix diff touches no file under `skills/` and no README. So round 1's confirmations of `settle.py`, the skill's text and the labels in `gaps.md` were carried as coordinates and not re-derived this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the repository-wide lint and the format check (the `Broad gate` row). `tests/conftest.py` changed, so every module reads it | `seal/config.md` | the orchestrator, by `seal gate --base origin/release/v0.27.0 --record 1793443708-settle-keeps-a-gaps-file-anywhere` |
| The crafter's run of 24 modules with 2192 passed: an aggregate, not re-run; two of its modules were re-run here | round 1's answer to finding 2 | the orchestrator's broad gate |
| Whether Windows needs `target_is_directory` for a link to a directory that already exists. The new docstring sentence at `tests/conftest.py:627-629`, like Python's own `os.symlink` docstring, says it does. `tests/skills/test_seal.py:637` and `:1164` link existing directories without the flag, and the crafter left them | `tests/conftest.py:627-629`, `tests/skills/test_seal.py:637`, `tests/skills/test_seal.py:1164` | the `windows-latest` legs of `.github/workflows/test.yml` on the pull request |
| Both `Test_misplaced` cases run, neither skipped, on Windows (carried from round 1) | `gaps.md` *Not verified* | the `windows-latest` legs of `.github/workflows/test.yml` on the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_settle.py tests/text/test_settle_reads_before_it_removes.py -q -rs`, in a `git clone --no-local` of the worktree at b00c434e | exit 0, 119 passed, none skipped |
| `bin/seal mutate skills/settle/SKILL.md --tests "bin/test tests/text/test_settle_reads_before_it_removes.py -q -p no:xdist -x"` with seven `--replace` pairs, one per sentence or clause named under `confirms: round-1#1` | baseline passed; 7 mutants, 7 red, 0 survived; file restored |
| `bin/seal mutate README.md` and `bin/seal mutate README.ko.md`, each removing its row's new clause, same `--tests` | each red, on `test_both_cheat_sheets_carry_the_command` for its edition; files restored |
| `bin/seal mutate tests/skills/test_settle.py`, removing `(top / "trail").mkdir()` before the link in `test_accepts_a_file_or_a_link_to_one_at_another_path`, `-k` that case | red: `AssertionError: the link's parent does not exist`; file restored |
| `bin/seal mutate tests/skills/test_settle.py`, removing `trail.mkdir()` in `test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none`, `-k link -rs` | survived: the `link` shape skipped as "this platform makes no symbolic link here"; 2 passed, 1 skipped; file restored |
| `bin/seal mutate tests/conftest.py`, removing the parent assertion, `-k Test_misplaced` | survived, as expected: both cases build their fixtures correctly, so no case reaches the assertion; file restored |
| `bin/seal layout --pairs tests` | exit 0; no pair names either changed module |
| `git grep -n "os\.symlink\|\.symlink_to(" -- tests evals` | outside `tests/conftest.py`: `tests/skills/test_settle.py:1162` and `tests/skills/test_agentic_pytest_record.py:882`, `:904`, `:929` |
