# Review round 1: 1794178397-a-durations-refresh-costs-no-round

```seal
target: f237ce30 against release/v0.36.0
```

This round reviewed the branch at `f237ce30` against its base `94d04d30`.
It read the issue (#1444), `routing.md`, the three frame files, `gaps.md`,
`changelog.md`, `pr.md` and both phase records whole at the target, then
the code diff: `.github/scripts/durations_union.py`,
`.github/workflows/test.yml`, `CONTRIBUTING.md`, `tests/conftest.py`,
`tests/github/test_durations_union.py` and
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`.
No earlier round exists, so nothing was carried from one. Carried from the
frame and not re-derived: *Grounding* G8's counts of `main`'s union, and
G4's reading that a no-work-item pull request into the release branch owes
no round and no sealer, which the settle's pull requests already show. No
`seal/parity.md` is declared.

The axes walked, beyond the table's: the verdict's boundary on each share,
the exit codes the script now has, the two GitHub expressions, the job
summary as a Markdown page a person reads, the removed cases' entries left
in `.test_durations`, and every other statement of the old refresh schedule
across the tree.

## Findings

### 1. The red verdict's job summary tells the reader to move `/.test_durations`: the `<dir>` placeholder outside a code span is parsed as an HTML tag and dropped

```seal
severity: should
location: `.github/scripts/durations_union.py:81-82`, `tests/github/test_durations_union.py:374`
evidence: executed a `test_tmp_*` probe rendering `durations_union: ` plus `du.verdict(du.staleness(...))` through `cmarkgfm.github_flavored_markdown_to_html`, the renderer `test.yml` pins as GitHub's; read `.github/scripts/durations_union.py:78-89`, `.github/scripts/durations_union.py:364-367`
```

Why it matters: the design's *Data & interfaces* sends the sentence to the
job summary, and `main` appends it there (`durations_union.py:366-367`).
A job summary is rendered as GitHub-flavoured Markdown. `REMEDY` puts the
first `<dir>` inside a code span and the second outside one:
`then move <dir>/.test_durations over the committed .test_durations`, where
only the first command of the sentence is backticked. CommonMark reads
a bare `<dir>` as a raw HTML open tag, because `dir` is a valid tag name.
The probe rendered the sentence through `cmarkgfm`, the GitHub renderer the
`pytest` job installs. In safe mode the output is
`then move <!-- raw HTML omitted -->/.test_durations over the committed`.
In unsafe mode `<dir>` passes through as an element, and GitHub's sanitizer
keeps no `dir` element. Either way the person preparing the release reads
"move /.test_durations" on the summary page. The job log, which takes the
same sentence on stderr, reads correctly. The old remedy had the same words
but printed them only as a pytest assertion message, which is plain text.
This change sends them to a Markdown page for the first time.
`CONTRIBUTING.md:186-187` already writes the path as
`` `<dir>/.test_durations` ``.

The fix puts the path in a code span and moves the pin with it (contract
rule 14). Those two lines are the only statements of the bare path: the
comment above `REMEDY` and `CONTRIBUTING.md` do not write it bare.

```python
# .github/scripts/durations_union.py, inside REMEDY
    "`gh run download <run id> -n test-durations -D <dir>`, then move "
    "`<dir>/.test_durations` over the committed .test_durations and commit it "

# tests/github/test_durations_union.py, Test_verdict, the `said` tuple
            "move `<dir>/.test_durations` over the committed .test_durations",
```

### 2. `gaps.md` names one leftover `.test_durations` entry of a removed case, where eight stand

```seal
severity: should
location: `seal/threads/1794178397-a-durations-refresh-costs-no-round/gaps.md:23-27`
evidence: executed `git diff 94d04d30..f237ce30 -- tests/` for every removed `def test_`, then `grep -c "::<name>\""` on `.test_durations` for each, at the target
```

Why it matters: the paragraph reads "`.test_durations` keeps the entry of
the case phase 2 removed, `test_the_durations_file_prices_the_suite`, at
0.016 s". Phase 2 removed eight cases from
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`:
the suite case and the seven fixture cases that *Removes* row 4 names. Each
of the eight keeps its entry in `.test_durations` (lines 1223 to 1231 and
1234). The paragraph lists one because its list came from the plan row's
`git grep 'prices_the_suite\|STALE_SHARE'`. That search finds a spelling,
not the class of entries the removed cases leave. The class is closed and
the diff lists it (contract rule 12, the second method), so a single entry
handed back as the whole is a sample. The settle and the sealer read this
memo. The memo's reasoning still holds: the release refresh drops every
entry, and together they hold well under a second, far inside the share.
Only the count and the names are wrong.

```markdown
`.test_durations` keeps the entries of the eight cases phase 2 removed from
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`:
`test_the_durations_file_prices_the_suite` and the seven fixture cases
`frame/design.md` *Removes* row 4 names. This work makes the rule that no
work item commits the file, so phase 2 left them. The next release refresh,
taken from a union that no longer holds those cases, drops the entries.
```

### 3. `Test_staleness::test_accepts_an_entry_no_part_ran_as_dead_and_never_unpriced` covers nothing its class does not already cover

```seal
severity: should
location: `tests/github/test_durations_union.py:328-336`
evidence: read `tests/github/test_durations_union.py:316-326`, `tests/github/test_durations_union.py:328-336`, `tests/github/test_durations_union.py:386-399`, `.github/scripts/durations_union.py:96-115`, `.github/scripts/durations_union.py:202-222`
```

Why it matters: the case asserts two things. An entry the union does not
hold is dead and never unpriced. The unpriced share is then zero. The case
before it in the same class,
`test_accepts_the_union_and_the_file_and_names_each_side_in_order`, gives a
union and a file that each hold ids the other lacks. It asserts the exact
`unpriced` list `[c, a]`, which leaves out the dead `z` and `y`, the exact
`dead` list, the counts and both shares. A mutation of `staleness` or of
`Staleness`'s properties that makes a dead entry count as unpriced, or that
changes either share, fails that case's exact assertions. That holds for an
inverted membership test, a `/` turned into `*` on either share, or a
changed comprehension. The zero share is also held at the boundary, by
`Test_verdict::test_refuses_one_more_dead_second_naming_the_seconds_and_the_first`.
Its file holds only dead extras, and it asserts "have no price" is absent
from the sentence. The old suite case this one rewrites
(`test_an_entry_nobody_collects_is_not_counted`) also checked that the
seconds side fails. That fact now sits in `Test_verdict`, not in a case of
`staleness`. *Removes* row 4 still holds after the deletion, because its
fact lands in the case above. This claim rests on reading every assertion
in the class; no mutation run backs it.

```python
# tests/github/test_durations_union.py: delete lines 328-336, the whole
# `test_accepts_an_entry_no_part_ran_as_dead_and_never_unpriced` method.
```

## Confirmations

What matched: *Scope* item 1 and scenario S1. `git grep -n 'prices_the_suite' -- tests` printed nothing at the target. The three modules the phase 2 row names passed with the case gone: `bin/test tests/github/test_durations_union.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/text/test_ci_gives_the_checks_what_they_need.py -q` gave 61 passed and 1 skipped (executed). `collects_the_suite`, `tests/conftest.py#COLLECTED_NODE_IDS` and `test_no_collected_id_carries_the_interpreters_path` stay, as *Scope* item 1 says (read, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:261-297`).

What matched: *Scope* item 2 and *Data & interfaces*. `staleness` (`.github/scripts/durations_union.py:202-222`) returns `Staleness` (`:96-115`), holding the five fields and the two shares that the design's rewritten line 59 names. `report` (`:256`) and `verdict` (`:225`) both read it. The empty union is refused. `STALE_SHARE` is 0.05 at `:70`. The module docstring states exit codes 0, 1 and 2 (read). This is the statement the orchestrator's `dd20fbc8` folded, and the target agrees with it.

What matched: the boundary on each side. `>` against `STALE_SHARE` at `:231` and `:238`, and `Test_verdict::test_accepts_exactly_the_share_on_each_side` passes at exactly 50 of 1,000 on each side. 50/1000 and the literal 0.05 are the same float, so the exact-share case asserts what it names (read).

What matched: *Scope* item 3 and scenario S4. The union step ends in `${{ github.base_ref == 'main' && '--stale-fails' || '' }}`, and the upload's `if:` is `${{ !cancelled() && hashFiles('union/.test_durations') != '' }}` (`.github/workflows/test.yml:214-215`, read). `github.base_ref` takes only the two literal strings, so the expression injects no text. The claim that phase 2's two cases were seen red was re-run. With `CONTRIBUTING.md` and `test.yml` checked out at `94d04d30`, `test_the_verdict_is_asked_into_main_alone_and_the_upload_outlives_it` failed on `assert run.endswith(" " + ASK_THE_VERDICT)`. `test_the_recipe_names_the_artifact_and_the_checklist_has_no_box` failed on "A work item never commits `.test_durations`" (executed). Both files were restored to the target afterwards.

What matched: *Scope* items 4 to 6 and scenario S5. `CONTRIBUTING.md:163-196` states the release remedy, the trailer, the branch cut from `release/vX.Y.Z`, the pull request into it, the limit sentence, and that a work item never commits the file. `docs/releasing/release-checklist.md` *0. Before starting* holds no refresh box. The docstring paragraph at `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:37-45` and the comment at `tests/conftest.py:852-857` were rewritten in place (read).

What matched: scenario S2, which phase 1 claimed is held by two existing cases. `write_parts`'s default committed file is 16.7 % unpriced: the new exit-1 case reads exactly that from it. `Test_main::test_the_summary_names_each_parts_seconds_the_spread_and_the_live_sum` (`tests/github/test_durations_union.py:238-249`) drives that default without the switch and asserts exit 0 (read).

What matched: the census of the old schedule. The phase 2 row's census `git grep -n 'prices_the_suite\|STALE_SHARE' -- ':!seal/threads'` lists the script, its cases, `CONTRIBUTING.md:182`, `test.yml:194`, the behaviour module's `:42` and `:333`, and `.test_durations:1234`. That is the list the plan row, as `5c327456` rewrote it, gives. `git grep -n 'durations' -- docs skills agents templates README.md CLAUDE.md` lists only `docs/running/measuring-a-run.md:24` and `skills/verify/scripts/session_cost.py:2181`, both about an agent run's duration. The search found no statement of the per-branch refresh left in `seal/` outside the threads, `evals`, `lib`, `bin` or `hooks` (executed).

What matched: the `gaps.md` *Not done* claim that `seal layout --check` reports eight functions of `durations_union.py` with no class. `bin/seal layout --check` printed exactly those eight (executed). `bin/seal layout --pairs` named no pair in either test file (executed).

What matched: the frame statements the orchestrator's commits folded. `frame/questions.md` Q2's Status names the switch on the union step, which `test.yml:214-215` holds. Each quote in `pr.md` stands word for word at its source: lines 1 to 4 in `changelog.md:3`, line 5 in `frame/plan.md:50`, line 6 in `gaps.md:9` (read). No other sentence of the frame, `gaps.md`, `changelog.md` or `pr.md` is contradicted by the target, except the one in finding 2.

One gap in a comment, which is no finding: the test module's docstring at `tests/github/test_durations_union.py:18-19` says `Test_staleness` sits at the share's boundary on a thousand cases. None of its cases does; only `Test_verdict`'s do.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub evaluates `github.base_ref == 'main' && '--stale-fails' \|\| ''` to the switch on a pull request into `main` and to nothing elsewhere, and whether `hashFiles('union/.test_durations')` matches the dot-named union file. Read only; no run evaluated either. | `.github/workflows/test.yml:214-215`, `gaps.md:9` | a measurement: this branch's pull request run and 0.36.0's release pull request, read by the orchestrator |
| Whether the verdict reads a real four-part union and prints in a real step summary | `gaps.md:8`, `frame/questions.md` Q1 | a measurement: the `durations` job on 0.36.0's release pull request, read by the orchestrator of that release |
| The full suite, the repository-wide lint and the format check at the target; `unverified`, which `gaps.md:7` labels honestly | the branch | the orchestrator, at the broad gate |
| Phase 1's 18 mutants and phase 2's mutants, claimed executed and not re-run here | `trail/phases/phase-1.md:70-101`, `trail/phases/phase-2.md:53-82` | the sealer, which samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_durations_union.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/text/test_ci_gives_the_checks_what_they_need.py -q` | exit 0, 61 passed, 1 skipped |
| `git checkout 94d04d30 -- CONTRIBUTING.md .github/workflows/test.yml`, then `bin/test tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -k "verdict_is_asked or recipe_names"`, then a checkout back to `f237ce30` | exit 1, 2 failed, each on the line phase 2 names |
| `bin/test tests/test_tmp_summary_render.py -q -p no:xdist -s`, which rendered the 51-of-1,000 verdict sentence through `cmarkgfm` in safe and unsafe mode; the file was deleted afterwards | safe mode gave `then move <!-- raw HTML omitted -->/.test_durations`, and unsafe mode passed `<dir>` through as an element |
| for each `def test_` the diff removes, `grep -c "::<name>\""` on `.test_durations` | 1 for each of the eight |
| `bin/seal layout --check` and `bin/seal layout --pairs` | exit 0; the eight functions `gaps.md` names; no pair in either test file |
