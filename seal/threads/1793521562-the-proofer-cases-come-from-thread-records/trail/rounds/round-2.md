# Review round 2: 1793521562-the-proofer-cases-come-from-thread-records

```seal
target: a6aa894cbae6a5cbdc1fef80b7620f5699114fda, fixes e09f5577..a6aa894c
```

This is a verifying round. Its target is the diff of round 1's fix pass, `e09f5577..a6aa894c`. The round answers round 1's one finding and reviews the units that diff added or changed. All work ran in a `git clone --no-local` of the branch worktree at the target. `origin` was set to the GitHub URL, and tags and `+refs/pull/*/head` were fetched. The local `v0.27.1` and `v0.27.0` name the same commits as the remote tags (executed: `git ls-remote`). No `seal/parity.md` is declared, so the round block carries no `original:` line.

Carried from round 1 and not searched again: the coordinates of the generator code (`evals/scripts/seed_defects.py#seed`, `evals/scripts/replay_targets.py#truth_pattern`, `#LOCATION`) and of its tests (`tests/evals/test_seed_defects.py`). Also carried are the two rows round 1 left to the owner, Q1 and the replay scaffold's `origin`. Re-established this round: whether any truth's `location:` line passes another truth's grader in the four seeded cases, the generators' output, the scaffold runs, the narrow modules and the test pairs. Every verdict below is this round's.

## Findings

### 1. The 15-line margin of the new seed check, the part that fixes the instance round 1 reported, is pinned by no case; the path filter is not pinned either

```seal
severity: should
location: `tests/evals/test_seed_defects.py:217-267`, `evals/scripts/seed_defects.py:191-194`, `evals/scripts/seed_defects.py:212`
evidence: executed `bin/seal mutate evals/scripts/seed_defects.py --replace "first - rt.WINDOW <= line <= last + rt.WINDOW for first, last in spans" "first <= line <= last for first, last in spans" --replace (the target_at wiring made []) --replace "            if m[\"path\"] != path:" "            if False:" --tests "bin/test -q -p no:xdist tests/evals/test_seed_defects.py"`
regression: round-1#1
```

Why it matters: the units are `seed_defects.py#seed`'s new span check (`:191-194`) and `seed_defects.py#named` (`:201-223`). Both were added at `87ebbc41`. The frame's *Scope* item 5 says the seed's window is kept off every coordinate a finding's `location:` names. The fix does that by refusing a seed within 15 lines of each span (`first - rt.WINDOW <= line <= last + rt.WINDOW`). Its cases put the seed line inside every span they test, so they never test the 15-line margin.

That margin is what fixes the instance round 1 reported. In `seeded-55b66958` the old seed was `unverified_check.py:1053`, and the coordinate it overlapped was `unverified_check.py:1060-1086`. So the seed lay 7 lines outside the range, not inside it. A `seed()` that kept only the range itself would place that seed again, and no case would notice.

The crafter claimed that `seal mutate` went red on each of the five new units, the span check among them. I ran three mutants in one batch:

- With the margin removed (`first <= line <= last`), the mutant SURVIVED. All 28 cases of the module passed.
- With the `target_at` wiring made `[]`, the mutant went red.
- With `if m["path"] != path:` made `if False:`, the mutant SURVIVED.

The crafter's span-check mutant must have removed the whole check, which these cases do catch. The margin inside the check is unpinned.

In `test_keeps_the_seed_off_every_coordinate_a_truths_location_names`, `g`'s line is 45. It sits inside each case's span: `20-60`, `45`, the unit `g` and the whole file. The `Test_target_of` case names `a.py:40`, which is exactly `g`'s line in `SEEDED_SOURCE` (`tests/evals/test_seed_defects.py:36-38`).

The path filter is a separate gap. Without it, a coordinate in another file blocks the same line numbers in the seed's file. `--count` would then refuse lines it may take, so the case it writes could change, or a commit could drop out as `bf9efcba` did. Every case here names `a.py` alone, so none catches that.

The fix adds two rows that set a coordinate within 15 lines of `g` but not over it, and one case for a coordinate in another file. Every name used is in the tree. `found[:2]` and `found[4]` avoid restating the operator's text. The fix assumes nothing at an OS boundary.

```python
    @pytest.mark.parametrize(
        ("later", "line"),
        [
            ("`a.py:20-60`", 80),
            ("`a.py:20\N{EN DASH}60`", 80),
            ("`a.py:45`", 80),
            ("`a.py:55`", 80),
            ("`a.py:25-35`", 80),
            ("`a.py#g`", 80),
            ("`a.py`", None),
        ],
        ids=[
            "range",
            "en-dash-range",
            "line",
            "line-within-the-window",
            "range-ending-within-the-window",
            "unit",
            "bare-path",
        ],
    )
    def test_keeps_the_seed_off_every_coordinate_a_truths_location_names(
        ...

    def test_a_coordinate_in_another_file_leaves_the_line_free(
        self, tmp_path, monkeypatch
    ):
        """A coordinate names lines of its own path only: `b.py:45` keeps no
        seed off `a.py:45`, so `g` takes the seed."""
        sd = load_script("seed_defects")
        repo, base = based_repo(tmp_path, monkeypatch)
        write(
            repo,
            "a.py",
            "def f(a):\n    return a == 1\n"
            + "\n" * 41
            + "def g(a):\n    return a == 2\n"
            + "\n" * 33
            + "def h(a):\n    return a != 3\n",
        )
        target = commit_everything_as_e(repo, "target")
        found = sd.seed(
            base,
            target,
            [sd.rt.truth_pattern("`a.py:1`", target)],
            ["`a.py:1`, `b.py:45`"],
        )
        assert found[:2] == ("a.py", 45) and found[4] == ["g"], found
```

The two new rows go red against the margin mutant. `a.py:55` is 10 lines past `g` and 25 short of `h`. `a.py:25-35` ends 10 lines before `g`. The new case goes red against the path mutant.

### 2. `frame/plan.md` still says the work changes neither generator, and `frame/questions.md` still tells the reader not to reopen whether either generator changes

```seal
severity: should
location: `seal/threads/1793521562-the-proofer-cases-come-from-thread-records/frame/plan.md:5`, `seal/threads/1793521562-the-proofer-cases-come-from-thread-records/frame/questions.md:8`
evidence: executed `git grep -n -E "changes neither|Whether either generator" -- seal/threads/1793521562-the-proofer-cases-come-from-thread-records/frame`, `git diff --stat e09f5577..a6aa894c -- evals/scripts`
regression: round-1#1
```

Why it matters: the units are `frame/plan.md` *Technical context* and the do-not-reopen list of `frame/questions.md`. The fix pass changed both files, at `2dedc608` and `a6aa894c`. The frame now says the generators' choice of cases stands and the seed's placement changes (`frame/design.md` *Scope* item 5 and the narrowed *Out*). The fix changed `evals/scripts/seed_defects.py` and `evals/scripts/replay_targets.py` (`#LOCATION` gains `last`, and `truths_with` reads it). The folds rewrote *Out* and the counts but left two sentences that stood on the old scope.

`plan.md:5` reads: "The work builds on the two generators as 0.27.1 left them, and changes neither." That is false at HEAD. `questions.md:8` lists "Whether either generator changes: `frame/plan.md` A3" among the judgments the tree answered and that nobody is to reopen. A3 rejects a change to how `--count` chooses, not a change to a generator. A reader who takes the list at its word reads the diff to `evals/scripts/` as outside the frame.

These are wrong sentences that agents act on: the sealer reads the frame against the tree. So the finding is `should`. Contract rule 19 asks that the commit making a fact false rewrites what stood on it.

```markdown
<!-- frame/plan.md, Technical context, first line -->
The work builds on the two generators as 0.27.1 left them. How either chooses its cases stays as it is. Where `seed_defects.py#seed` places a seed changes (`frame/design.md` *Scope* item 5): `seed()` takes the `location:` values of the truths' findings, and `replay_targets.py#LOCATION` gains the `last` group that `truths_with` also reads.

<!-- frame/questions.md, the list of answered judgments -->
- Whether either generator changes how it chooses its cases: `frame/plan.md` A3. Where a seed is placed inside a chosen case does change (`frame/design.md` *Scope* item 5).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: no truth's `location:` line now passes another truth's grader in any seeded case. The fix pass closed round 1's finding `fixed bbf155e5`, with the code at `87ebbc41`. For each of the four seeded cases, I searched every `truth-` grader over every finding's `location:` line in round 1's record at its tag. I also compared the seed line against every coordinate in the seed's file, for every finding, truths and others alike (executed, the first probe). Results:

- `seeded-55b66958`, seed at `skills/verify/scripts/unverified_check.py:1739`: finding 1's line passes `truth-1` alone. The nearest coordinate is `:1759-1760`, 20 lines away.
- `seeded-5fd6b88c`, seed at `evals/scripts/replay_targets.py:210`: findings 1 and 2 each pass their own grader alone. The nearest coordinate is 107 lines away.
- `seeded-7a8899d5`, seed at `hooks/lib/blocks.py:451`: findings 1 and 3 pass `truth-1` and `truth-3` alone. Finding 2, not a truth, passes none. No finding names `hooks/lib/blocks.py`.
- `seeded-ea73e94f`, seed at `skills/settle/scripts/settle.py:537`: finding 1 passes `truth-1` alone, and no finding names `settle.py`.

Contract rule 15 holds for all 13 graders:

- Each `truth-seeded` matches `location:` at its seed line and at neither 16 lines before nor 16 lines after.
- Each `truth-<n>` matches the record and stops matching once finding `<n>`'s `location:` line is removed.

The crafter claimed the new cases were red against the old `seed()` by a TypeError. That red comes from the signature, not the behaviour. The behavioural evidence is `seal mutate`. This round re-ran four mutants, and all four went red: the range end (`int(m["last"] or m["line"])` made `int(m["line"])`), the unit span, the bare path, and the `target_at` wiring (executed). Finding 1 names the two mutants that survived. The close holds for the code and the cases. The gap in the tests is finding 1, not a reopening.

```seal
confirms: none
```
What matched: Scenario 2 for the regenerated seeded half. In the clone, `seed_defects.py --list` exited 0 and offers four commits: `55b66958` at `:1739`, `ea73e94f` at `:537`, `5fd6b88c` at `:210` and `7a8899d5` at `hooks/lib/blocks.py:451`. It leaves `bf9efcba` out with "no added line in a Python unit takes an operator" (executed). `--count 4` exited 0 and wrote those four names. `--case` with the four names exited 0. `diff -r` of each written case against its committed directory exited 0, for both runs (executed). That matches the changelog fragment's names and the reason it gives for `bf9efcba`. It also matches `frame/questions.md` Q2's "four commits once round 1's seed fix keeps `bf9efcba` out".

```seal
confirms: none
```
What matched: Scenario 3 for the two scaffolds the fix pass changed. `seeded-55b66958/scaffold.sh` and `seeded-7a8899d5/scaffold.sh` each exited 0 in an empty directory under this round's scratch directory, and the scaffold's own `assert` on the old text held. Each tree's `seal/README.md` opens with `# What AgenticSeal maintains in seal/`. Neither tree holds `seal/specs/`. Each holds its work item's `routing.md`, and neither holds the report its prompt names (executed).

```seal
confirms: none
```
What matched: the counts the folds wrote. The replay and seeded cases hold 14 `truth-` graders, 1 in each replay case and 2, 3, 3 and 2 in `seeded-55b66958`, `seeded-5fd6b88c`, `seeded-7a8899d5` and `seeded-ea73e94f` (executed: `ls graders | grep -c`). That is the 14 in `changelog.md`, `frame/design.md` *Grounding*, `frame/plan.md` and `frame/questions.md` Q2. The changelog says the seed now stays "more than 15 lines" from every coordinate. The code refuses `first - 15 <= line <= last + 15` (`evals/scripts/seed_defects.py:191-194`, read), which matches. `git grep` for `bf9efcba` outside `seal/threads/` finds nothing, and `.test_durations` holds no key for either changed case name (executed).

```seal
confirms: none
```
What matched: the `truths_with` rewrite keeps its behaviour. `truths_with` matches each entry with `LOCATION.fullmatch` (`evals/scripts/replay_targets.py:755`). Under a full match, the new `last` group holds exactly what the old `re.search(r"[-\N{EN DASH}](\d+)$", location)` found. No reader indexes `LOCATION`'s groups by position (`git grep -n LOCATION`, executed). So adding the group shifts no index. The range grammar is now written once, and `seed_defects.py#named` reads the same group (read).

```seal
confirms: none
```
What matched: the method behind `named`'s list of coordinates (contract rule 12). The coordinates are built from what produces them, the `location:` grammar of `hooks/lib/fields.py:97-98` and `:150-155`. That grammar allows `path`, `path:line` or `path:first-last`, each backticked and joined by `, `. The `.py` files a seed can land in fall inside `replay_targets.py#LOCATION`'s path class. `named` covers each form: a line, a range, and the bare path as the whole file. It also covers the en dash and `path#unit` of the older labelled records (read). So the list is whole for every record the generators read, not a sample of spellings.

```seal
confirms: none
```
What matched: the new tests, read against their group. `test_keeps_the_seed_off_every_coordinate_a_truths_location_names` is the only case in `Test_seed` that passes `locations`. `test_keeps_the_seed_off_a_later_coordinate_of_round_1s_finding` is the only case that reaches `target_at`'s passing of them. The wiring mutant shows it covers what the other case cannot. Neither repeats a case of its group. `bin/seal layout --pairs` exited 0 and names no pair in `tests/evals/test_seed_defects.py` (executed).

```seal
confirms: none
```
What matched: the narrow modules, through the runner. `bin/test -q` over `tests/evals/test_seed_defects.py`, `tests/evals/test_replay_targets.py`, `tests/evals/test_rule_cases.py`, `tests/behaviour/test_evals_layout.py`, `tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py`, `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` and `tests/test_censuses.py` passed 269 cases, exit 0 (executed). That is round 1's 263 plus the six new ones. The crafter's claim of 1421 passed over 29 modules is a different module set, and this round did not re-run it (read).

```seal
confirms: none
```
What matched: `trail/phases/phase-1.md` reads as history, not as a stale claim. Each fact it states is tied to the commit it was taken at: `1c54abf4`, `3895ed77`, `dd333022`. The `frame/plan.md` *Phases* row closes phase 1 at `dd333022`. Its sentences on the eight names, the 13 graders and the seed lines 1605 and 1053 describe what `--count` wrote at that commit, which is true of that commit. The move to the regenerated cases is recorded where a reader of HEAD looks for it: round 1's close block, the appended sentence of `frame/design.md` *Grounding*'s `--count` row, and the changelog fragment (read). Nothing in the phase record speaks of HEAD.

```seal
confirms: none
```
What matched: the replay overlap the fix pass left. #1249 is open, titled "fix: the replay generator lets two truths of one case accept the same location line, …" (executed: `gh issue view 1249`). Each committed replay case holds one `truth-` grader (executed: count above). So no two truths of a committed replay case can accept one line. The `frame/plan.md` *Judgments of the run* row says no committed case carries the overlap, and that holds. Its count of 11 of 48 rounds is the fix pass's, and this round did not re-derive it (read).

```seal
confirms: none
```
What matched: the broad gate's label. `gaps.md` *Not verified* still labels the full suite, the repository-wide lint and the format check unverified and names the orchestrator, by `seal gate` after the rounds settle. The fix pass ran a module set and no broad gate, so the label is honest. This round ran no broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the proofer, on the current release, reads a new case's earlier records and writes its record at the prompt's path. Only a paid run shows it, and the owner withheld paid runs for 0.27.2. This row is carried from round 1 | `frame/questions.md` Q1; `gaps.md` *Not verified* | the owner, at the first paid proofer run after 0.27.2 |
| The cost of the case that joined. `seeded-7a8899d5` reviews a 3051-line diff, where `seeded-bf9efcba` reviewed 351 (executed: `seed_defects.py --list`). Q2's cost statement for (a) counts the replay diffs alone, and the *Grounding* row's appended sentence gives no size for the new case. Whether the suite should carry it is part of which rounds the suite measures | `frame/questions.md` Q2; `frame/design.md` *Grounding*, the `--count` row | the owner |
| Whether a replay scaffold that keeps `origin` lets the proofer fetch the later rounds of the record it replays. Carried from round 1, which carried it from `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/rounds/round-1.md:231`, and not judged again | `evals/behaviour/proofer/replay-*/scaffold.sh` | the owner |
| The full suite, the repository-wide lint and the format check at the target | the tree at `a6aa894c` | the orchestrator, by `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_round2_seeded.py` in the clone, one file, run once and deleted. For each seeded case: every `truth-` grader over every finding's `location:` line of round 1's record at its tag; the seed line against every coordinate in its file; `truth-seeded` at the seed and at 16 lines either side; each `truth-<n>` with its finding's line removed | every finding's line passes its own grader alone or none; the nearest coordinate to a seed is 20 lines away; all 13 graders pass the rule 15 checks; exit 0 |
| `python3 evals/scripts/seed_defects.py --list`, then `--count 4 --out <scratch>/count`, then `--case` with the four seeded names `--out <scratch>/case`, then `diff -r` of each written case against its committed directory | each exit 0; four commits offered, `bf9efcba` left out with no line to seed; every `diff -r` exit 0 |
| `sh scaffold.sh` of `seeded-55b66958` and `seeded-7a8899d5`, each in its own empty scratch directory, then `head -1 seal/README.md`, `test -d seal/specs`, `ls seal/threads/*/routing.md`, `test -e` of the report path | both exit 0, marker line, no `seal/specs`, routing present, no report |
| `bin/seal mutate evals/scripts/seed_defects.py` with `--tests "bin/test -q -p no:xdist tests/evals/test_seed_defects.py"`, one mutant per run: the range end made `int(m["line"])`, the unit span's `spans.append(span)` made `pass`, the bare path's append made `pass` | each red (2, 1 and 1 cases failed) |
| the same `bin/seal mutate` as one batch of three: the margin removed from the span check, the `target_at` wiring made `[]`, the path filter made `if False:` | baseline passes; margin SURVIVED, wiring red, path filter SURVIVED; `git status --short` empty afterwards |
| `bin/test -q` over the seven modules named in the eighth confirmation | 269 passed, exit 0 |
| `bin/seal layout --pairs` | exit 0; no pair in `tests/evals/test_seed_defects.py` |
