# Review round 1: 1794383424-the-gate-ships-a-copy-of-one-workflow

```seal
target: 27bbbdd75 against release/v0.37.4
```

This is the first round, so no earlier record carries a coordinate and every
fact below was established here. The diff was read from the branch's cut,
`18a7e18fb`, to `27bbbdd75`. `release/v0.37.4` has since gained `10e721f11`
(#1498), which touches no file this diff changes. `routing.md`, the three
frame files, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md`
were each read whole at `27bbbdd75`. No `pr.<lang>.md` stands, and none is
owed: `seal/config.json` names English for both language keys. No
`seal/parity.json` and no `Pact` key is declared. The runs below were taken
in a `git clone --no-local` of the worktree at `27bbbdd75`, under the round's
scratch directory.

## Findings

### 1. The comment the diff writes above `resolve_base` calls `moved_line` the one reader of `base.given`, and the refusal four lines below reads it too

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:2236-2242`, `skills/verify/scripts/broad_gate.py:2244-2249`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:29`
evidence: executed `grep -n -E '\.given\b' skills/verify/scripts/broad_gate.py` at `27bbbdd75`, which lists `:500-529` inside `moved_line` (`def` at `:458`) and `:2246` inside `gate`; read `skills/verify/scripts/broad_gate.py:2236-2249`, `tests/skills/test_broad_gate.py:150-162`
```

Why it matters: the comment tells the next editor of `gate()` how many
places take the caller's unresolved spelling of the base. #1485 rewrites this
file's comments next, from this text. The old comment listed its readers as
"none of them a check" and named two. The new one makes a count, "The one
reader of `base.given`, the caller's spelling, is no check: `moved_line`".
`gate()` itself reads `base.given` at `:2246`, in the refusal raised where
the base does not resolve: `f"seal gate: --base {base.given} does not
resolve in {root} — nothing "`. No case holds the count.
`Test_module#test_the_gate_reads_the_given_base_exactly_once`
(`tests/skills/test_broad_gate.py:150-162`) counts reads of `args.base` and
never of `base.given`, as `frame/design.md` G10 says.

The frame prescribed the sentence. *Scope* item 2 says the comment "names
`moved_line` as the one reader of `base.given`", so the fix changes that
clause as well, or the frame states a comment HEAD no longer has. Finding 2
changes the same line of the frame, and its snippet for line 29 carries this
finding's clause.

```python
    # commit CI will compare against. The readers of `base.given`, the
    # caller's spelling, are none of them a check: `moved_line`, which
    # exists to say how that spelling differs from what it resolved to, and
    # the refusal below, which names the spelling that resolved to nothing.
```

In `frame/design.md:29`, the clause becomes:

```markdown
`gate`'s comment at `:2610-2620` names `moved_line` and the refusal of a base that does not resolve as the readers of `base.given`
```

### 2. The frame and the phase record name `gate()` as `main`

```seal
severity: should
location: `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:12`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:29`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:60`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/design.md:78`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/frame/plan.md:7`, `seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow/trail/phases/phase-1.md:12`
evidence: executed `git show 5909a2776:skills/verify/scripts/broad_gate.py | grep -n -E '^def (main|gate)\b'`, which gives `gate` at `:2571` and `main` at `:2804`; `git grep -n "panel(" -- '*.py'`, which gives `skills/verify/scripts/broad_gate.py:2355` inside `gate` as the plugin's one call; read `5909a2776:skills/verify/scripts/broad_gate.py:2655-2664`, `:2678-2694`, `:2744-2752`, and `skills/verify/scripts/broad_gate.py:2197`, `:2414`, `:2491` at `27bbbdd75`
```

Why it matters: these sentences place the comments, the coverage call, the
arm runs and the `panel` call in `main`. At `5909a2776`, the commit the frame
says it read, every one of those lines stands inside `def gate(args,
ascii_marks=False)` (`:2571-2803`). `main` (`:2804`) parses the arguments
and calls `gate` (`:2491` at HEAD). The commit the section is dated to
contradicts its own coordinates. *Data & interfaces* says "`main` is its one
caller in the plugin" of `panel`. A sealer that opens `main` to check it
finds no call of `panel` there. The crafter's account claims at
`trail/phases/phase-1.md:5` that every coordinate G4 gives "stood where the
frame placed it". The lines did stand there, but the function the frame
named did not hold them, and the record repeats the name at `:12`. So the
account's reading of the frame missed it.

`frame/design.md:61`, "`broad_gate.main`'s stderr loses the coverage line",
can stay. `main` runs `gate`, and the stream is `main`'s. Each line below
replaces the clause named:

```markdown
design.md:12  `gate`'s comments at `:2610-2620` and `:2655-2669`, its call at `:2660-2664`, and its `panel` call at `:2749`.
design.md:29  `gate` reads no workflow, prints no coverage line, and passes no workflow to `panel`.
design.md:29  `gate`'s comment at `:2610-2620` names `moved_line` and the refusal of a base that does not resolve as the readers of `base.given`, and the comment at `:2666-2669` loses the ground that `PARTITION`'s cases read each `checks[...] = run(...)`.
design.md:60  `gate` is its one caller in the plugin (executed: `git grep -n "panel("` over `skills`, `lib` and `.github`).
design.md:78  `broad_gate.py#panel` rows at `:2314-2337`, `#unanswered`, `#coverage_line`, and `gate` at `:2655-2664`
plan.md:7     The gate's arms are the repository's command, the chain check and the mode check, listed in the module docstring at `:12-29` and run by `gate` at `:2678-2694` (read).
phase-1.md:12 `gate`'s comment above the chain arm gave `PARTITION`'s cases as the reason a preflight keeps one list of arms.
```

## Confirmations

What matched: *Scope* items 1 to 9 against the diff `18a7e18fb..27bbbdd75`,
read hunk by hunk. The section at `5909a2776:skills/verify/scripts/broad_gate.py:1722-2059`
is gone whole. `panel` takes no `workflow`, and its one call
(`skills/verify/scripts/broad_gate.py:2355-2363`) passes `gate_copy(...)`
fifth, where `copy` now stands. Each test caller of `panel` passes four
positional arguments, or five with `copy` fifth (`tests/skills/test_broad_gate.py:1564`).
The module docstring, the comments at `:168-171` and `:180-184`,
`copy_origin`'s docstring and `panel`'s docstring state what stands. The
comment above the arms keeps the ground that remains. Read.

What matched: S4. `git grep -n -w` over the names S4 lists, with
`seal/threads` and `.test_durations` excluded, printed nothing and exited 1.
A wider `git grep` for `CI also`, `more steps`, `coverage line`,
`partition`, `DOT`, `mirrored`, `named arm`, `declared rather than
remembered` and the deleted file's name found only
`assets/seals/red-lily.ans:11`, which *Out* keeps as history, and unrelated
uses of `str.partition`. Executed.

What matched: S5. `bin/seal rules --check` exited 0 and named no line of
`docs/running/the-broad-gate.md`. No file cites the old heading `What the gate
runs, and how the list is kept true` (executed: `git grep -n "kept true"`).
Executed.

What matched: S3, by reading. At `18a7e18fb`, `gate()` called
`coverage_line(workflow, base.given)` for any `workflow_text(root)` that was
not None and printed it to stderr. `panel` added the `CI also` row wherever
`job_steps(workflow, "release")` was not empty. `FIXTURE_WORKFLOW` has a
`release` job with three named steps. Each half of
`Test_main::test_a_workflow_with_a_release_job_leaves_the_run_as_it_was` is
therefore red against the base, as `trail/phases/phase-1.md:18` claims. The
case reads the labels the run printed (`run_gate` passes `--shape`), so it
does not hand `panel` an input the new signature cannot take. Read; the
case's green is executed in the narrow run below.

What matched: G5 and S1. `templates/setup/hygiene.yml` declares one job,
`hygiene` (`:56`), and `seal pr-checks install` writes that file
(`skills/implement/scripts/seal.py:38`, `:1442`). So the old row and line
printed nothing in a repository that installed it. Read.

What matched: `seal_stamp.DOT` had no reader left. `TWIN_ASCII`
(`skills/verify/scripts/seal_stamp.py:410`) maps the character `·` and not
the constant, so `SEP`'s ASCII form is unchanged. `LABEL_WIDTH` stays 7.
Read.

What matched: the documents. `skills/verify/orchestration.md` *The broad
gate* lost the four paragraphs G7 names, and the paragraph before them now
runs on to the baseline paragraph. Neither paragraph states the table. The
guidance the fourth paragraph gave, that a repository names its own checks in
the `Broad gate` key, still stands at `templates/setup/config.md:227-258`
("what the broad run covers is exactly that"). `docs/running/the-broad-gate.md`
dropped the rule and its `check:` line, and the section's other rules are
unchanged. No file under `agents/`, `skills/`, `docs/` or `templates/` names
the row or the coverage line. Executed (`git grep`) and read.

What matched: `changelog.md` and `pr.md`. Each sentence of the fragment
matches the diff and G5. Both quotes in `pr.md` stand word for word at
`frame/plan.md:17`, in the verdict cell of the chosen row, and at
`frame/plan.md:55`, in the judgment cell of the title row.
`bin/seal pr-body` composed the body from them with exit 0. Executed and
read.

What matched: the narrow run's two failures,
`tests/test_conftest.py::Test_census_case::test_accepts_a_target_every_census_passes`
and `::test_refuses_a_target_one_census_flags_naming_it`, fail the same way at
`18a7e18fb`, as `trail/phases/phase-1.md:24` claims. Executed.

What matched: the deleted cases. Every case of
`tests/behaviour/test_the_gate_names_every_step_ci_runs.py`, and every case
`tests/skills/test_broad_gate.py` loses, reads a name G4 lists, the `CI also`
row or a removed sentence. No case of a unit that stays was removed. The
renamed `Test_panel` case and the rewritten S3 case each hold a fact their
group's other cases do not. Read.

A note with no finding: the rewrap in the module docstring left
`skills/verify/scripts/broad_gate.py:71` at 96 columns, against 74 or less on
the lines around it. `ruff.toml` selects no `E501`, and no case holds a
docstring's width, so nothing acts on it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD: the full suite, `uvx ruff check .` and `uvx ruff format --check .`. The suite is `unverified` here (contract rule 2). The crafter's label for it in `gaps.md:7` is honest. | `seal/config.json` `Broad gate` | the orchestrator's broad run |
| S2: no `CI also` row in the gate's report at HEAD, and no stderr line opening `seal gate: .github/workflows/hygiene.yml's` | `gaps.md:8` | the orchestrator, reading its broad run's output |
| S3's case on `windows-latest`, where `os.path.join` spells the searched path with `\` | `tests/skills/test_broad_gate.py` `Test_main::test_a_workflow_with_a_release_job_leaves_the_run_as_it_was` | CI on the pull request |
| Whether `CONTRIBUTING.md` *What a change to a gate must carry* asks this body to state a failure direction and a prompt budget for a change that leaves the gate's verdicts and exit codes as they were (`frame/design.md:61`). If it does, which record `pr.md` quotes for them. No record of this work item states either. | `CONTRIBUTING.md`, `pr.md` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_a_release_publishes_its_note.py tests/test_conftest.py tests/skills/test_seal_stamp.py tests/github/test_rules.py tests/behaviour/test_this_repository_passes_its_own_checks.py tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py tests/github/test_tracker_labels.py -q`, in the clone at `27bbbdd75` | exit 1: 618 passed, 1 skipped, 2 failed, the two `Test_census_case` cases |
| `bin/test tests/test_conftest.py -q -k Test_census_case`, in a worktree of the clone at `18a7e18fb` | exit 1: the same two cases fail, so both are failing on base too |
| `uvx ruff check` and `uvx ruff format --check` over the eight changed Python files, through `xargs` | both exit 0 |
| S4's `git grep -n -w` | no output, exit 1 |
| `bin/seal rules --check` | exit 0, nothing named for `docs/running/the-broad-gate.md` |
| `python3 -I -c` summing `.test_durations` over the ids of the deleted file and of each `def` or `class` the diff removes | 59 entries, 13.35 s of 1616.51 s (0.83%). This is under `STALE_SHARE` by entries and by seconds. The match takes in same-named cases of other classes, so it does not reproduce G13's 45. |
| `bin/seal pr-body --body <scratch>/pr-body.txt seal/threads/1794383424-the-gate-ships-a-copy-of-one-workflow` | exit 0: `pr.md`, then the fragment and the records under `## From the records` |
