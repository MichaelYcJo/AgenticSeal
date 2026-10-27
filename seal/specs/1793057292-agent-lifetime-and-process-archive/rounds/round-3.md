# Review round 3: 1793057292-agent-lifetime-and-process-archive

target: 17b287af, fixes 8eca5d5d..17b287af

Round 3 is the verifying round after the sealer withheld at `8eca5d5d`
(`guarantee.md`, committed in 085530de). Round 2 closed no finding, so no
earlier finding is owed a `confirms:`, `reopens:` or `regression:` line.
The round answers the sealer's three items in `guarantee.md` *What must
change* and judges phase 5. It read the diff `8eca5d5d..17b287af` in the
worktree the spawn named. The probe ran in a `git clone --no-local` of that
worktree at `17b287af`. No `seal/parity.md` is declared, so no parity
comparison applies. The pull request body is the orchestrator's, and the
sealer re-reads it. This round did not judge it.

One fact is carried and not re-established: the seven slice values of
#930's smith, 377,894, 569,013, 655,847, 778,563, 904,072, 931,652 and
941,799. They come from `phases/phase-1.md`'s table, and the sealer
(`guarantee.md`, *Claims re-run*) and phase 5 each re-ran
`session-cost --segments` on the transcript. This round did not open the
transcript, because the spawn kept its reads inside the worktree. It
re-derived the threshold's effect from those values and the rule. Every
other verdict below was re-derived at `17b287af`.

## Findings

### 1. `overview.md` and phase 5's record call `236a596d` the head before phase 5, and three commits stood between them

severity: should
location: `seal/specs/1793057292-agent-lifetime-and-process-archive/overview.md:25`, `seal/specs/1793057292-agent-lifetime-and-process-archive/phases/phase-5.md:93-94`
evidence: executed `git log --format='%h %s' --name-only 08469dff..17b287af`
verdict: open

The sealer withheld in part because `overview.md` said "the commit after
it" where two commits followed `08469dff` (`guarantee.md` *What must
change*, item 3). Phase 5 rewrote that row correctly, and in the same pass
wrote the same kind of miscount into the row above it. Row 1 of *Not
verified* now says the broad run was "at `236a596d`, the head before phase
5". Phase 5's record says the same at lines 93-94. Three commits came after
`236a596d` and before phase 5's `1718924d`: `8eca5d5d`, `085530de` and
`f8408d5e`. Each one changes only this work item's records. `f8408d5e`
rewrote `spec.md`, `plan.md` and `questions.md`, so the broad run did not
cover the frame as it stands now. The sealer reads this row against
`broad-gate.md` to decide what the broad run covered. The phrase tells it
that nothing landed between the run and phase 5.

The class is a record sentence that names one commit as next to another.
This round checked every such sentence the fix range writes. Row 2 of
`overview.md` ("Of the commits after it, only phase 5's `1718924d` changes
a file outside this work item's records") holds. Phase 5's own list
("236a596d, 8eca5d5d, 085530de and f8408d5e change only this work item's
records") holds. Only these two places are wrong.

`overview.md`, row 1 of *Not verified*:

```markdown
| closed the full suite, the repository-wide lint and format check, and the typecheck at `236a596d`; the three commits after it and before phase 5, `8eca5d5d`, `085530de` and `f8408d5e`, change only this work item's records | `broad-gate.md` records the run at `236a596d` against `5bab081e`; its printed report read BROAD GATE PASSED, ruff check and format clean, the suite 6,561 passed and 14 skipped, chain-check exit 0. The repository has no typecheck to run (#951 adds one) |
```

`phases/phase-5.md`, the sentence at lines 93-94:

```markdown
`tests/test_release_report.py`. `overview.md` *Not verified* now says so,
and names the `236a596d` broad run with the three record commits after it
and before this phase. Two open
```

answer:

### 2. The workflow's comment sends the release table's reader to *2. Gather, bump*, and the checklist tells the reader to read the table in *5. The release pull request*

severity: should
location: `.github/workflows/test.yml:242-247`
evidence: executed `awk '/^## 2\. Gather, bump/,/^## 3\./' docs/release-checklist.md | grep -n -i -e table -e report`, `git merge-base --is-ancestor 6046f0622 5bab081e`
verdict: open

The comment on the `release-report` job says whoever prepares the release
reads the table "(`docs/release-checklist.md` *2. Gather, bump*)". Section
2 does not mention the table or the report: the search prints nothing. The
instruction to read the table is at `docs/release-checklist.md:172-178`,
*5. The release pull request*. The comment's next clause calls
`.github/scripts/release_report.py` "the rule", so the comment is where a
reader of the job looks for the rule's home. Phase 5 changed that script
and wrote that the job's comment "stand[s]" (`phases/phase-5.md:44-47`).
That holds for the comment's list of what the table shows. It does not hold
for the citation.

The citation is older than this branch. It came in 6046f062, which is in
the base `5bab081e`. This round reports it because phase 5 read the comment
and passed it. No case pins the citation: `git grep -n "Gather, bump" --
tests .github` finds only the comment.

```yaml
  # On a pull request into `main`, the release table: each agent's preload
  # bytes, the suite's seconds, each leg's minutes and each document's bytes
  # beside the same reading at the last release tag, appended to this job's
  # summary. It fails nothing, and whoever prepares the release reads it
  # (`docs/release-checklist.md` *5. The release pull request*);
  # `.github/scripts/release_report.py` is
```

answer:

## Confirmations

confirms: none
The sealer's item 1 is answered in the tree. `release_report.py:54` adds
`seal/process/*.md` to `DOCUMENTS`. The module docstring (lines 23-26) and
`documents()`'s docstring (lines 179-181) name the archive files.
`spec.md:121-128` (*Out*), `questions.md` A5 and `plan.md` P-C now say the
archive's size is a row of the release report, with no check. They no
longer rest on the report not existing. `plan.md` has a phase 5 row with
Status `1718924d`. The changelog's archive item names the row. The issue
body's section 4 asks that the archive's size be "a row of the release
report #923 builds". The build gives one row for each archive file, and the
frame's P-C chooses that. An archive file is written once, so each release
shows its new file as `new` with that file's bytes, and the earlier files
read `+0`. The tag's side has the earlier files because `release-report`
unpacks the tag with `git archive "$tag"` (`.github/workflows/test.yml:277`),
and `.gitattributes` declares no `export-ignore`: `git archive HEAD` in
the clone lists 686 paths under `seal/`. A5's claim that `seal/budgets.md`
was never committed holds: `git log --all -- seal/budgets.md` prints
nothing. Executed.

confirms: none
The phase 5 case pins the change. With `"seal/process/*.md"` taken out of
`DOCUMENTS` in the clone, `tests/test_release_report.py` ran 1 failed and
15 passed. The failure was the new case: its list of `seal/` rows came back
empty where it expects the one archive row. That repeats phase 5's
seen-red result by hand, and it is the same edit as the mutant phase 5 ran
through `bin/mutation-check`. The file was put back, and
the clone's status was clean. At `17b287af` the module and
`tests/test_the_release_table_reads_two_trees_and_fails_nothing.py` run 17
passed. The case asserts that the archive file is a row, and that
`seal/README.md` and a file under `seal/specs/` are not. No other case of
the module covers `documents()` under `seal/`. `bin/test-layout --pairs`
names no pair. `bin/test-layout --check` exits 0. It reports `documents`
among thirteen functions with no `Test_<function>` class, which the module
already lacked before phase 5. Executed.

confirms: none
`documents()` is the only code that reads `DOCUMENTS`
(`release_report.py:183`; `git grep -n DOCUMENTS` outside `seal/specs`
finds nothing else). The texts that describe the table's documents do not
list them. `HEADER` says "each document's size". The job's comment says
"each document's bytes". `docs/release-checklist.md:172-178` says the same.
`CONTRIBUTING.md:150` names the job with no list. So none of them is now
short of the archive. `changelog/0.22.0.md:20-26` lists the old three
globs. It is a released changelog, so it records history and stays as it
is. `Test_module`'s docstring says "a row for every `docs/*.md`". It says
nothing about `seal/process/`, which holds no file yet, so it is not
false. Executed with `git grep`, read for the rest.

confirms: none
The sealer's item 2 is answered at its source. `phases/phase-1.md:102-111`
now applies the rule at `skills/code-review/orchestration.md:29-37`. Before
each fix pass, the rule reads the implementer's largest per-turn context
and resumes only below the threshold. Under 487,998, slice 1's 377,894
resumes the smith for slice 2, and slice 2's 569,013 starts a fresh smith
for slice 3. Under 806,241, slice 4's 778,563 resumes it for slice 5, and
slice 5's 904,072 starts a fresh smith for slice 6. The sentence says
exactly this. The slice values are carried (see above). Read.

confirms: none
The sealer's item 3 is answered. *Fed back* in `overview.md` (lines 95-98)
says the fold line sits below the approval line where the plan carries one,
and below the title where it does not. That is the rule at
`skills/implement/orchestration.md:36-39`. Row 2 of *Not verified* names
the commits after run 40430474904 correctly. `phases/phase-2.md:62-67` still
says the line sits below the approval line. It records what phase 2 built:
at f7fb7028, `skills/implement/orchestration.md:37` read "`plan.md` carries
one line of its own below its approval line". `rounds/round-1.md` finding 6
records the change in 5be7d538, and `overview.md` states the rule now in
force. A phase record is the work record, and the history of the rule
belongs there. Executed with `git show f7fb7028:skills/implement/orchestration.md`,
read for the rest.

confirms: none
The `tests` run 40434089606 at `17b287af` finished `success`. It passed
ubuntu, the three macOS groups, the four Windows groups, lint, both
`arm-check-grammar` legs and `durations`. `release-report` was skipped,
because the base is not `main`. That answers the Linux and Windows part of
row 3 of `overview.md` *Not verified*, the row for `1718924d`. Closing the
row is the orchestrator's. The full suite, lint and format parts stay with
the broad run. Executed with `gh run view 40434089606 --json headSha,status,conclusion,jobs`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `17b287af`. This round ran none of the three. The broad run at `236a596d` comes before phase 5's code commit | `broad-gate.md` | the orchestrator, by `broad-gate --base release/v0.22.4 --record` once this round's findings are closed |
| The archive's row in a live `release-report` summary. The job runs only on a pull request into `main`, and no `seal/process/*.md` exists yet | `overview.md` *Not verified*, row 4 | whoever prepares the release that ships this work item |
| The pull request body's sentences the sealer named at lines 5, 10, 13, 18 and 52. The body is the orchestrator's file and is not in the tree | `guarantee.md` *What must change*, item 2 | the sealer, at its next audit |
| Q1, no archive files for 0.22.0 to 0.22.3, and Q2, a merge and never a rebase, both on their defaults | `questions.md` Q1, Q2 | the owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_release_report.py tests/test_the_release_table_reads_two_trees_and_fails_nothing.py -q -p no:xdist` at `17b287af` | exit 0, 17 passed |
| `.venv/bin/python -m pytest -p no:xdist -p no:cacheprovider -q tests/test_release_report.py` in the clone with `"seal/process/*.md"` taken out of `DOCUMENTS` | exit 1, 1 failed and 15 passed: `test_accepts_each_process_archive_file_as_a_document_row`, `assert [] == [...]`; the file was put back with `git checkout --`, and the clone's status was clean |
| `bin/test-layout --check tests/test_release_report.py` | exit 0, 0 refused; reports 13 functions with no `Test_<function>` class, `documents` among them |
| `bin/test-layout --pairs tests/test_release_report.py` | exit 0, 0 pairs |
| `git archive HEAD` in the clone, piped to `tar -t`, counted under `seal/` | 686 paths, `seal/README.md`, `seal/config.md` and `seal/follow-up.md` at the root |
| `git log --all --oneline -- seal/budgets.md` | no commit |
| `gh run view 40434089606 --json headSha,status,conclusion,jobs` | `17b287af`, completed, `success`; `release-report` skipped |
| `awk '/^## 2\. Gather, bump/,/^## 3\./' docs/release-checklist.md` piped to `grep -n -i -e table -e report` | nothing |
