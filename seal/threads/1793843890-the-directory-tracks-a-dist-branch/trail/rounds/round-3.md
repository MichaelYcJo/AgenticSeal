# Review round 3: 1793843890-the-directory-tracks-a-dist-branch

```seal
target: 48cc56ce, fixes e657142d..48cc56ce
```

This is the verifying round over the repair the stated-limit path of `skills/code-review/orchestration.md` sends a defect only one platform shows. The diff read is `git diff e657142d 48cc56ce`: 0ccb500f changes `evals/scripts/noninferiority.py#extract`, and 48cc56ce changes three rows of `gaps.md` *Not verified*. The review stayed inside that diff and the statements of the facts it changes. Round 2's finding 1 is answered below, as it closed `fixed 20d32144`.

Carried from round 2 and not re-established: no ruleset reaches `dist`, no workflow starts on a push to `dist`, every `from:` passage of the rule changes stands in its section, `marketplace.json`'s `source` is `./`, and the merge base with `origin/release/v0.32.3` is `9dd67e2a`. The fix diff touches none of the files those facts rest on. The merge base was read again with `git merge-base` and still names `9dd67e2a` (executed). The remote was not fetched.

The crafter claimed the defect's cause from git's source, and claimed 254 passed on macOS for the module. Both were checked. The source was read at both upstream git and Git for Windows. The module was run in this round's clone. `## Confirmations` gives what each showed.

The hygiene run at HEAD, 41964657964, fails on three lines of `chain_check.py`. They say the last round, the gate record and the guarantee are each behind HEAD, because 0ccb500f touches a file outside the work item's records (read, `gh run view --log-failed`). Those three lines are this round, the orchestrator's broad run and the sealer's spawn, which the stated-limit path names. They are no finding.

No test was added by the diff, so no test is read against its group.

## Findings

### 1. The extract row of `gaps.md` says no Windows seen-red exists for the repair, and run 41963550875 is that red

```seal
severity: should
location: `seal/threads/1793843890-the-directory-tracks-a-dist-branch/gaps.md:9`
evidence: read `seal/threads/1793843890-the-directory-tracks-a-dist-branch/gaps.md:9`, `tests/evals/test_noninferiority.py:649-699`; executed `gh run view 41963550875 --log-failed`, `gh run view 41964657990 --json jobs`, `gh run view --job 127038753507 --log`
```

Why it matters: the row reads "No Windows seen-red or green exists for the repair, because `os.sep` is `/` on macOS and the change does nothing there". The cause it gives holds for macOS alone. Run 41963550875 at `e657142d` ran the four `Test_extract` cases on Windows against the code before the repair, and all four failed on the defect. Its log lists four `FAILED tests/evals/test_noninferiority.py::Test_extract::` lines and the summary `4 failed, 3093 passed, 22 skipped`. Each `cannot create directory at` path ends in `<INTO>\evals`, as the row's own second sentence says. That run is the red the row says does not exist. The row contradicts itself. A reader that weighs seen-red claims, the sealer among them, reads that the four cases were never shown failing on the platform where they hold the defect.

The green now exists too. Run 41964657990 at `48cc56ce` passed every Windows leg. Its Windows group 1 leg lists `tests/evals/test_noninferiority.py` among its timings. The leg ended 3097 passed and 22 skipped, the earlier leg's 3093 passed plus the four. So the row's answerer has answered, and the drive-component premise held on the runner. The fix below states both runs and closes the row. It reaches every statement of the fact in the work item: the search `git grep -n -i "windows" -- seal/threads/1793843890-the-directory-tracks-a-dist-branch` (executed) finds the fact in this row alone, apart from round 1's `## Not judged` row, which states its own round.

```markdown
| closed `noninferiority.py#extract` on Windows. Run 41963550875 at `e657142d` failed the four `Test_extract` cases that write under an INTO not yet made, each with `fatal: cannot create directory at '<INTO>\evals'`. The cause is in git's `entry.c#create_directories` (v2.50.1, read): `checkout-index` creates a missing leading directory at a `/` and at no other separator. A prefix spelt with `\` therefore reaches `mkdir` as one long component whose parent does not exist. The repair at `0ccb500f` hands git the prefix spelt with `/`. On POSIX the prefix is the same string as before, so macOS can show the repair neither red nor green | answered by the `tests` workflow on the pull request. Run 41963550875 at `e657142d` is the four cases' red on Windows against the code before the repair. Run 41964657990 at `48cc56ce` is their green: its Windows group 1 leg lists `tests/evals/test_noninferiority.py` among its timings and ends 3097 passed with none failed, so Git for Windows read the drive component `C:` as a directory |
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the last paragraph of `## Removes` reads "This work adds a job, a script, a census reading and six attribute lines" (`seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/design.md:175`, read). Round 2's `executed` line was re-run: `git grep -n "five attribute\|five lines\|Five lines"` over the worktree at 48cc56ce. In this work item it finds the dated *Grounding* row (`frame/design.md:25`), the phase records and the two earlier round records, and no statement of the present count (executed).

What matched: the cause the crafter claimed. `create_directories` in `entry.c` at git v2.50.1 copies the path up to the next `/` and calls `mkdir` on each prefix so cut. It splits at no other character. The function is the same text at Git for Windows `v2.50.1.windows.1` (read, both fetched with `gh api` and compared with `diff`, exit 0). The red log agrees with that reading. For the whole-tree case it prints `error: unable to create file ...\all\.gitattributes` before `fatal: cannot create directory at '...\all\evals': No such file or directory`. git tried the full backslash path as one name, and the parent was missing (executed, `gh run view 41963550875 --log-failed`).

What matched: the repair at `evals/scripts/noninferiority.py:195` changes only the separator of the prefix. `os.path.abspath` gives a Windows path with `\`, and `.replace(os.sep, "/")` turns each into `/`. On POSIX `os.sep` is `/`, so the string is unchanged (read). The docstring sentence at `:186-188` says what `create_directories` does (read). The two callers in `run_side` (`:632-638`) pass a directory that `os.makedirs`, `shutil.copytree` or the first `extract` has made, so the old code worked for them, and the new code does too (read).

What matched: the class of the defect is every place that hands git a filesystem prefix that `create_directories` cuts at `/`. Only `checkout-index --prefix` gives that function a caller's prefix, as the `base_dir_len` comment in `entry.c` says (read). `git grep -n "checkout-index\|--prefix"` outside `seal/threads/` lists `evals/scripts/noninferiority.py:186` and `:197` alone (executed). So the repair reaches the whole class in the tree.

What matched: the crafter's narrow run. `bin/test tests/evals/test_noninferiority.py -q` in this round's clone at 48cc56ce ended 254 passed, exit 0 (executed).

What matched: the two rows 48cc56ce closes. The census row (`gaps.md:8`) and the `dist_branch.py` row (`gaps.md:13`) cite run 41963550875 at `e657142d`. In that run the four Windows legs split the suite four ways, and only group 1 failed. Its log names the four `Test_extract` cases and no other failed case. In no Windows leg's skip summary does a `SKIPPED` line name `test_dist_branch.py`, `test_plugin_directory_check.py`, the census module or the extract module (executed, `gh run view --job <id> --log` for jobs 127035231670, 127035231684, 127035231740 and 127035231850). Since 0ccb500f changes only `noninferiority.py`, both answers stand at HEAD. Each closed row opens with `closed`, the spelling `skills/implement/SKILL.md` *An item is closed by marking it* gives (read).

What matched: the pushed HEAD's `lint` job passed in run 41964657990, so the two changed lines of `noninferiority.py` satisfy the repository's ruff configuration on that runner (read, `gh run view 41964657990 --json jobs`). This round did not run ruff itself.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether an INTO on a UNC path, `\\server\share\...`, still checks out after the repair. Spelt with `/` its first cut is `//server`, which `create_directories` stats and may try to `mkdir`. Before the repair, an INTO that already existed reached git with no `/` in its prefix. The eval runner's INTO is `tempfile.mkdtemp()` under the runner's temp directory, and the cases' INTO is pytest's `tmp_path`, so the normal flow makes no UNC INTO. This round read the code and has no Windows host to run it on. | `evals/scripts/noninferiority.py:195` | the orchestrator, which decides whether the limit earns a sentence in the docstring |
| The full suite, the repository-wide lint and the format check at HEAD. The suite stays `unverified` here. | the whole tree | the orchestrator's broad run |
| The seal at HEAD. `guarantee.md` seals `7cf83b01`, and 0ccb500f follows it outside the records. | `seal/threads/1793843890-the-directory-tracks-a-dist-branch/guarantee.md` | the sealer, spawned after the broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/evals/test_noninferiority.py -q` in this round's clone at 48cc56ce | 254 passed, exit 0 |
| `gh run view 41963550875 --log-failed`, and `gh run view --job <id> --log` for its four Windows jobs | group 1: 4 failed, 3093 passed, 22 skipped, every failure a `Test_extract` case at `<INTO>\evals`; groups 2 to 4 green; no skip of the named modules |
| `gh run view 41964657990 --json jobs`, and `gh run view --job <id> --log` for its four Windows jobs | every job green; group 1: 3097 passed, 22 skipped, `test_noninferiority.py` among its timings; no skip of the extract module |
| `gh api` of `entry.c` at `git/git` `v2.50.1` and at `git-for-windows/git` `v2.50.1.windows.1`, then `diff` of the two `create_directories` bodies | both fetched, exit 0; `diff` exit 0 |
| `gh run view 41964657964 --log-failed` | the `release` job's chain check refuses the last round, the gate record and the guarantee as behind HEAD at 0ccb500f |
| `git grep -n "checkout-index\|--prefix"` outside `seal/threads/`, and `git grep -n -i "windows"` over the work item | the first lists `noninferiority.py:186` and `:197`; the second lists `gaps.md:8`, `:9` and `:13` and round 1's `## Not judged` row |
