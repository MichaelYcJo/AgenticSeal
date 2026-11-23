# Phase 1: 1795439973-six-test-modules-cost-past-the-rewrite-bound

## What this phase found

### The frame, read against the tree before the build

The frame holds for this module. At `9e6158f74`, `git grep -n -E '^def (git|commit|repo)\(' -- tests/skills/test_settle.py` printed `:86`, `:101` and `:113`, the three lines `frame/design.md` *Grounding* names (executed). The module's own `local` fixture stood at `:514`. The 15 files that import from the module were the 15 that `frame/design.md` *Data & interfaces* lists, by `git grep -l -E "from test_settle import|import test_settle" -- tests` (executed). Seven of them take `past_the_bound` and `unanswered`, and eight take `unanswered` alone.

One cost stood outside what the frame named. `frame/questions.md` Q1 lets the phase rebuild what holds such a cost.

### Q1: where the module's seconds went before the rebuild

`bin/test tests/skills/test_settle.py -q -p no:xdist --durations=0` at `9e6158f74` passed 190 cases in 57.7 s (executed). Setup took 11.9 s and the cases' calls took 45.6 s. `Test_main` took 39.9 s of calls and 9.1 s of setup.

A probe split each case's seconds by the process it started and by the code that started it (executed: a pytest plugin named `test_tmp_profile.py` under this phase's scratch, which wrapped `subprocess.Popen`). Almost all of the 58 s was spent in child processes.

- The cases and their fixtures started 1,963 processes, which took 30.6 s.
- `settle.py` and `lib/` started 1,094 processes, which took 26.2 s.
- Of the second group, 43 runs of the module's `gh` stub took 13.2 s, about 0.3 s each.

The stub's cost was not Python. A script written to a new file and run for the first time took 0.40 to 0.62 s on this macOS machine, and each later run of the same file took 0.02 to 0.03 s (executed: three fresh stubs, each run three times). The `gh` fixture wrote a new stub for every case, so every case paid that first run. This is the cost `frame/design.md` *Grounding* did not name.

### What the rebuild changed

All three changes are in `60fab641d`.

- The module's `git`, `commit` and `repo` go, as `frame/design.md` *Removes* asks. Every call reaches `tests/conftest.py#git_out`, `#git` or `#commit_everything`. A token rewrite made the change and counted it, with an assertion on each count: 126 `git(` calls, 99 `commit(` calls, 553 uses of `repo` and 122 uses of `local` inside the case functions that took those fixtures.
- Two worlds are built once per module and copied into `tmp_path / "repo"` for each case: `_shared_world`, copied by `shared_repo`, and `_local_world`, copied by `local_repo`. Neither name shadows a fixture in `tests/conftest.py`. The module's `local` fixture goes with them, as `frame/design.md` *Scope* item 1 asks. A third world, `_removals_world`, holds the history `three_removals` builds. The four cases that read that history take it through `removals`, which copies it.
- The `gh` stub is written once per module by `_gh_stub`. Each case's `gh` fixture names the case's own directory in `AGENTIC_SETTLE_GH_STUB_HOME`, and the stub reads its answers and writes its call log there. A case that writes into a world writes into its copy, so `frame/design.md` S5 holds by construction. Under `-n auto` and under `-p no:xdist`, every case passed (executed, below).

### Departures from the frame

- **`commit_everything` costs one more process per commit.** The frame lands the module's commit helper on `tests/conftest.py#commit_everything` (`frame/design.md` *Removes*). That helper runs `git rev-parse HEAD` after each commit, which the module's own helper did not. In the rebuilt module that adds 296 processes and 3.9 s to the local run (executed, the same probe). The phase followed the frame. At the five places where a case or helper read HEAD right after a commit, it now takes the hash `commit_everything` returns, so those places start no `rev-parse` of their own. Making the helper cheaper is a change to `tests/conftest.py`, which `gaps.md` *Not done* explains.
- **`settled_repo` goes, beyond `frame/design.md` *Removes*.** It ran `git init` and a commit for each of the six cases of `Test_main::test_accepts_a_settled_root_and_says_so`. The case now takes `shared_repo` and makes `seal/threads/` empty on disk where `keep_empty_dir` asks. Grounds: `CONTRIBUTING.md` *The test layout*, the paragraph opening "A rewritten module builds its world once and reads a command without git".
- **`tests/conftest.py#tree` is not changed.** It is a fixture of `tests/conftest.py`, not one of this module's own, and `tests/lib/test_sibling.py` takes it too. It still builds a repository for each of the 20 cases that take it. `gaps.md` *Not done* says why the phase left it.

### The four parts `CONTRIBUTING.md` *The test layout* asks of a rebuilt module

**1. The move check, and the mutation table.**

`bin/seal layout --moved 9e6158f74 --from tests/skills/test_settle.py --to tests/skills/test_settle.py` exited 1 (executed). Its last line is `seal layout: moved: 139 old cases, 189 items against 189 at 9e6158f74a33, 228 failed`. Each failing item's body names `shared_repo`, `local_repo`, `git_out` or `commit_everything` where the old body named `repo`, `local`, `git` or `commit`. So the module carries the mutation table.

The mutants sit at decision points of `skills/settle/scripts/settle.py`, one or two for each function the classes reach. All 38 ran in one call, `bin/seal mutate skills/settle/scripts/settle.py --replace … (38 pairs) --tests "bin/test tests/skills/test_settle.py -q -x"`, and the call printed `38 mutants, 33 red, 5 SURVIVED` (executed). A red run exits 2, which is xdist stopping after the first failing case. Mutant 1, run alone, showed `FAILED …::Test_main::test_s5_settle_shows_a_work_item_released_under_agentic_seal` and `1 failed, 175 passed` (executed). The pairs are in this phase's scratch, in `mutants.py`.

| # | Unit | Mutant | New file | Old file |
|---|---|---|---|---|
| 1 | `threads` | the root's own name replaced by `seal` | red | not run |
| 2 | `work_items` | a file directly under the threads directory listed as a work item | SURVIVED | SURVIVED, an old gap |
| 3 | `show` | the output of a failed `git show` returned as text | red | not run |
| 4 | `released` | a path directly under the threads directory read as a work item | SURVIVED | SURVIVED, an old gap |
| 5 | `policy_root` | the root's resolution replaced by `""` | red | not run |
| 6 | `adding_commits` | the newest add of a path kept instead of the oldest | SURVIVED | SURVIVED, an old gap |
| 7 | `adding_commits` | no pull request number read from a subject | red | not run |
| 8 | `merged_pull_requests` | every merge commit read as none | red | not run |
| 9 | `versions` | a tag that peels to something other than a commit taken | red | not run |
| 10 | `versions` | the commits labelled highest tag first | red | not run |
| 11 | `blobs` | an answer other than `blob` read as text | red | not run |
| 12 | `published_releases` | a draft release read as published | red | not run |
| 13 | `carries` | the older notes' marker not read | red | not run |
| 14 | `notes` | a tag with no published release not kept | red | not run |
| 15 | `released_local` | `gh` asked again for a branch already asked | red | not run |
| 16 | `released_local` | a merge commit the ref does not reach taken | red | not run |
| 17 | `named_paths` | a bare file name not read as a path | red | not run |
| 18 | `in_tree` | a path holding `/` looked up among bare file names | SURVIVED | SURVIVED, an old gap |
| 19 | `misplaced` | a directory or a link to nothing named as a record | red | not run |
| 20 | `misplaced` | a record at its own place named as misplaced | red | not run |
| 21 | `plan_rows` | a near heading not named | red | not run |
| 22 | `earlier_judgments` | the window of two removing commits removed | red | not run |
| 23 | `earlier_judgments` | a path holding a newline asked for | red | not run |
| 24 | `earlier_judgments` | the release tag of the adding commit not looked up | red | not run |
| 25 | `timeline` | a design that does not parse grouped | red | not run |
| 26 | `history` | a merge that adds a document not read as its add | red | not run |
| 27 | `history` | a deletion read as a change | red | not run |
| 28 | `tracked_text` | the work items' own files read as citing files | red | not run |
| 29 | `tracked_text` | a binary file read | red | not run |
| 30 | `citations` | a file outside `tests/` that names the threads directory read as a check | SURVIVED | SURVIVED, an old gap |
| 31 | `names` | an abbreviated path not read as a citation | red | not run |
| 32 | `draft` | each operation applied to the document as it stands on disk | red | not run |
| 33 | `apply` | a directory kept for its note left out of the exit code | red | not run |
| 34 | `apply` | the published note read in local mode | red | not run |
| 35 | `main` | `--all-earlier` beside `--apply` not refused | red | not run |
| 36 | `main` | a root holding no work item not answered as settled | red | not run |
| 37 | `named_directory` | a directory outside the repository read | red | not run |
| 38 | `report` | the local headings printed in shared mode | red | not run |

The old files' column was run for the five survivors alone. The call put the base's file at `tests/skills/test_tmp_settle_old.py`, ran `bin/seal mutate … --tests "bin/test tests/skills/test_tmp_settle_old.py -q -x"` over the same five pairs, and printed `5 mutants, 0 red, 5 SURVIVED` (executed). The probe file was removed after the run. Each of the five is an old gap, so no new case is owed for it (`CONTRIBUTING.md` *The test layout*, the move check's bullet).

**2. Cases and seconds, before and after, on this macOS machine.**

| Measure | Before, `9e6158f74` | After, `60fab641d` |
|---|---|---|
| Cases | 190 | 190 |
| `bin/test tests/skills/test_settle.py -q -p no:xdist` | 57.7 s, of which 11.9 s setup | 38.4 s, of which 3.8 s setup |
| `bin/test tests/skills/test_settle.py -q`, under `-n auto` | 14.8 s, in `seal mutate`'s baseline run with `-x` | 9.1 s |
| Child processes the cases and fixtures started | 1,963 | 1,338 |
| Seconds in `gh` stub runs | 13.2 s over 43 runs | 1.2 s over 43 runs |
| Windows leg, run 45181872904's `test-durations` artifact | 252.8 s | not measured |

The local estimate `frame/design.md` S1 asks for is 38.4 s times 252.8 / 57.7, which is about 168 s on the Windows leg. That is above 60 s.

**Q2: the floor.** The module does not come under 60 s in this phase, and the estimate says why. After the rebuild, 176 of the 190 cases still start git. The processes `settle.py` starts itself take 14.6 s of the 38.4 s locally: 13.4 s of git and 1.2 s of the `gh` stub (executed, the same probe). Scaled by the same ratio, that is about 64 s on the Windows leg before any case builds its history. Those processes are the command reading a real history, which is what the `Test_main` cases are about: merge order, release at a ref, history earlier settles removed, and the `--from` listing. `frame/design.md` *Scope* item 1 scoped this module to building its worlds once, and did not move its cases off `main`. Coming under 60 s would turn most `Test_main` cases into unit calls on `survey`'s readers, a rebuild the frame did not plan. `gaps.md` *Not done* hands that decision to the orchestrator. The CI figure is the orchestrator's, by `frame/design.md` S1.

**3. The real-git cases kept.** Every case that ran real git at the base still runs it, and no case became a unit call. The probe counted 176 cases that start a git process: 134 of `Test_main`, 11 of `Test_report`, 9 of `Test_apply`, 6 of `Test_module`, 3 each of `Test_versions` and `Test_show`, and 2 each of `Test_tracked_text`, `Test_citations`, `Test_adding_commit`, `Test_blobs` and `Test_policy_root`. Their names are unchanged in the file, and the same probe lists them again from any run. A copied list here would go stale beside the tree.

**4. Old cases cut or rewritten.** No case was cut. These cases were rewritten in their inputs:

- `Test_main::test_accepts_a_settled_root_and_says_so`, six parametrized cases. It guards that a root with no work item, its threads directory empty or absent, is answered as settled under the report, `--apply` and `--draft`, and that the tree is left as it was. Before, `settled_repo` built its repository, with `docs/one-root.md` on git's default branch. Now `shared_repo`, with `docs/a.md` on `main`, holds the same fact. No assertion reads the document or the branch. Mutant 36 holds the arm.
- `Test_main::test_reads_the_plans_of_the_two_newest_removing_commits_and_names_the_rest`, `test_a_batched_read_that_fails_keeps_the_line_of_older_commits`, `test_all_earlier_reads_the_plans_of_every_removing_commit` and `test_refuses_all_earlier_beside_apply_or_draft_and_reads_nothing`, the last with two parameters. Each built `three_removals` itself. Each now reads a copy of `_removals_world`, which `three_removals` built once, with the lines it returned. Their assertions are as they were. Mutants 22 and 35 hold them.

Every other case's body changed only by the renames the move check names. Its assertions read as they did. A case of the local mode and of the published note reaches `gh` through the stub written once per module, with the same answers and the same call log.

No case of the module reads a document's prose. The cases that open or run a file of this repository take scripts and `bin/seal`, which are code. So no case is left in place for its prose, and none is left waiting for another module to be rebuilt.

### Checks at the phase's close

The commands below were run at `60fab641d`, all executed.

- `bin/test tests/skills/test_settle.py -q` passed 190, and `-p no:xdist` passed 190.
- `bin/seal layout --check tests/skills/test_settle.py` exited 0: `1 files read, 0 refused`. It also prints 39 `report:` lines, each naming a function of `settle.py` with no class. The rebuild changed no class name, so the lines are the base's too (read, not run at the base). They are reports, not refusals.
- `git grep -n -E '^def (git|commit|repo)\(' -- tests/skills/test_settle.py` printed nothing and exited 1.
- `uvx ruff check` and `uvx ruff format` passed on the file.

`f6b98c557` then reshaped one case's body, `Test_main::test_accepts_a_settled_root_and_says_so`, to drop an alias of its fixture, and rewrapped a comment. The module passed again under `-n auto`, and mutant 36, run alone over that case with `-k settled_root`, was red (executed).

The phase boundary's run is in the hand-back.
