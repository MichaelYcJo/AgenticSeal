# Review round 3: 1795389517-three-github-scripts-ship-in-dist

```seal
target: bb6ab8ad1837b6923025299258a12709f5d0cfdc, fixes fdc3dcb98..bb6ab8ad1
```

This is a verifying round over `git diff fdc3dcb98..bb6ab8ad1`. That range holds the orchestrator's routing row in `frame/plan.md` *Judgments of the run* (`8f0e23bdb`), the fix pass's one commit (`7affd41b0`, the comment above `tests/censuses.py#SHIPPED`), and round 2's close block (`bb6ab8ad1`). It was read in a `git clone --no-local` under the round's scratch directory, checked out at the target. No `seal/parity.json` is declared, so no parity comparison was owed. No `pr.<lang>.md` is owed, because `Commit and pull request language` and `Record language` are both English.

Carried from rounds 1 and 2 and not established again: the pattern at `.github/workflows/hygiene.yml:92` matches the paths round 1's probe listed, the two other branches of the release share no hunk with this one, and `bin/seal rules --check` exits 0. The fix range changes none of the files those facts rest on. Re-derived this round: every verdict below, the `.py` paths the archive holds at the target, and the read of `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, each whole at the target. The three phase records were read for their coordinates.

## Findings

### 1. `pr.md` cites "the row of 2026-11-23" of *Judgments of the run*, and two rows now carry that date

```seal
severity: should
location: `seal/threads/1795389517-three-github-scripts-ship-in-dist/pr.md:1-2`
evidence: read `seal/threads/1795389517-three-github-scripts-ship-in-dist/pr.md:1-2`, `seal/threads/1795389517-three-github-scripts-ship-in-dist/frame/plan.md:72-75`, `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*; executed `grep -n '^| 2026-11-23' frame/plan.md` in the work item at the target, and a script counting each quote of `pr.md` in its source with runs of whitespace collapsed (the `## Probes` rows)
```

Why it matters: `pr.md` becomes the pull request body's first part, and the sealer and the owner open each quote at its coordinate. `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* says a quote's coordinate follows it as "the record's path, then the heading, row, finding or line that holds the sentence". `pr.md:1` cites "`frame/plan.md` *Judgments of the run*, the row of 2026-11-23", and `pr.md:2` cites the same row and "its Grounds cell". When `pr.md` was written, the table held one row. The orchestrator's commit `8f0e23bdb` in this range added a second row dated 2026-11-23, the route of round 2's regression, at `frame/plan.md:75`. The grep prints `:74` and `:75`. So "the row of 2026-11-23" now names two rows, and the target contradicts the definite article. Both quotes are still found word for word, once each, in the first row (executed). The fix only has to make the coordinate name one row again. No quoted sentence changed, so the orchestrator's rule on rewriting a quote after a fold did not fire, and it would not have caught this.

The paste-ready fix below names the row by its Judgment cell, which no other row shares. It changes the two coordinates and leaves the quotes as they stand. No other record cites the table by date: `git grep -n "row of 2026-11-23"` over the work item's tracked files prints only these two lines (executed). A line of `pr.md` is the orchestrator's to repair, by the section above.

```markdown
- "The pull request's title takes `fix:`" (`frame/plan.md` *Judgments of the run*, the row on the title's prefix)
- "The version check is a shipped behaviour that was wrong: a change to a `.github/scripts/` file or to `docs/` alone reached every installed copy without moving the version." (`frame/plan.md` *Judgments of the run*, the row on the title's prefix, its Grounds cell)
```

### 2. The routing row of round 2's regression is judged against the routing table alone, and the guidance asks it to name *The run*

```seal
severity: should
location: `seal/threads/1795389517-three-github-scripts-ship-in-dist/frame/plan.md:75`
evidence: read `seal/threads/1795389517-three-github-scripts-ship-in-dist/frame/plan.md:75`, `skills/code-review/orchestration.md:218-237`, `docs/running/the-run.md` *The run*; executed `git grep -h -E '^\| 20.*regression' -- 'seal/threads/*/frame/plan.md'`, its last cells counted
```

Why it matters: the row is a new unit of the fix range, written by the orchestrator in `8f0e23bdb`, and no round has read it. A row of *Judgments of the run* is what the settle reads to weigh a kind of judgment against what it cost, and its *Judged against* cell names the guidance the settle would rewrite. Two texts give that cell for this judgment. `skills/code-review/orchestration.md:235-237` says the orchestrator writes the route as one row, "the regression it answers and the route as the judgment, the comparison as its grounds, and *The run* as the document". `docs/running/the-run.md` *The run* says each such decision "is a row of `frame/plan.md` *Judgments of the run* naming the counts weighed and this section". The row names the regression, the route, the comparison and the counts, which matches. Its *Judged against* cell reads only "`skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, its second row", and it does not name *The run*. The row's own Judgment rests on *The run*, too: "the verifying round after it is owed whatever the count" is that section's sentence "A regression's fix pass is followed by one verifying round whatever the count". The routing table does not hold that sentence. So the settle, reading this row, sees no judgment made against *The run*. The search over the other work items' rows finds one regression route that names both documents, and the fix below follows it.

The fix adds *The run* to the cell and keeps the table's row as written. No other statement of the row needs to change.

```markdown
| 2026-11-23 | Round 2's finding 1 (`regression: round-1#3`) takes an ordinary fix pass, and the verifying round after it is owed whatever the count | The finding's grounds say the defect came from round 1's paste-ready snippet, applied as given: the frame does not state the census's scope, so the fix did something the frame does not say. Two finding rounds so far, three findings then one, and the fix changes a comment alone | `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, its second row, and `docs/running/the-run.md` *The run* |
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: `tests/censuses.py:40-44` now reads that `splitlines` and `heading_rule` read `lib/` and `skills/` and the release automation under `.github/scripts/`, and that a `.py` file under any other root is not read, naming `hooks/`, which the plugin ships, and `tests/`. The commit is the round's paste-ready comment, word for word (read in `git show 7affd41b0`). Each claim holds at the target. `_python` (`tests/censuses.py:121-126`) returns nothing for a path that does not end in `.py` or does not start with one of `SHIPPED` (read). `SHIPPED` is used at `:816` and `:878` alone, by those two censuses (executed: `grep -n SHIPPED tests/censuses.py`). The archive at the target holds 37 `.py` files: 16 under `lib/`, 20 under `skills/` and one under `hooks/` (executed). `git grep -n -i ship` over `tests/censuses.py` prints the comment, the constant and the three docstring and comment lines that say "under `SHIPPED`", so the comment is the one statement of the scope that claims anything about what ships, as the close says (executed). `bin/test tests/test_censuses.py -q` passes, and ruff passes the file (executed, the `## Probes` rows).

Two readings of the comment were weighed and are not findings. The list after "is not read:" names `hooks/` and `tests/` and leaves out `evals/`, which holds three tracked `.py` files (`evals/scripts/behaviour.py`, `noninferiority.py`, `rule_cases.py`). The sentence before the colon says a `.py` file under any other root is not read, which covers `evals/`, so a reader adding a file there is not led to trust the census. The clause "which the workflows run from the tree" covers twelve of the fourteen scripts under `.github/scripts/`. `finding_counts.py` and `plugin_directory_check.py` are run by a person from `docs/releasing/release-checklist.md:80` and `:270`, and no workflow names them (executed: `git grep -l <name> -- .github/workflows` for each script). The census reads both all the same, so no reading of the clause changes what anyone trusts the census to read.

The fix pass's close in round 2 corrects round 1's close of finding 3, whose sentence "`skills/settle/scripts/rules.py` entered it" is wrong, and leaves round 1's block as written. The correction holds. `rules.py` stood at `.github/scripts/rules.py` at the base, inside `SHIPPED`, as round 2's prose found too. Round 1's record is history, and the correction stands in the next record, so this round opens nothing on it.

What matched: the new row's Grounds cell at `frame/plan.md:75` holds against the records. Round 1 opened three findings and round 2 one, and `7affd41b0` changes comment lines of `tests/censuses.py` alone (executed: `git show --stat 7affd41b0`). The route matches the second row of `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, "a review record's paste-ready fix applied as given", which round 2's grounds state (read). Finding 2 concerns its *Judged against* cell alone.

What matched: the records read whole at the target state nothing else that the fix range contradicts. `routing.md`, `frame/design.md`, `frame/questions.md`, `gaps.md` and `changelog.md` did not change in the range. Each quote of `pr.md` is found word for word, once each, at the file its coordinate names (executed). Finding 1 concerns the row its first two coordinates name.

What matched: the suite stays `unverified`, as the fix pass labelled it, and that label is honest. The pass's own run of four modules, 1339 passed, was not repeated. `gaps.md:7-9` names the orchestrator as the answerer of the full suite, the lint and the format check.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `hygiene` step *a change to what ships must move the version* run by GitHub's bash on ubuntu at a pull request into `main`, with `docs` in its pattern | `.github/workflows/hygiene.yml:92` | the release pull request's CI run, read by the orchestrator |
| `bin/test.cmd` under cmd.exe at `%here%..\tests\run_tests.py` | `bin/test.cmd:7` | the repository owner, on a Windows machine |
| The full suite, the repository-wide lint and the format check at the target, which no agent runs (contract rule 2) | `seal/threads/1795389517-three-github-scripts-ship-in-dist/gaps.md:7-9` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_censuses.py -q`, in the clone at the target | 231 passed, exit 0 |
| `uvx ruff check tests/censuses.py` and `uvx ruff format --check tests/censuses.py` | exit 0, exit 0 |
| `git archive HEAD \| tar -t`, its `.py` paths counted by top-level directory | 16 under `lib`, 20 under `skills`, 1 under `hooks` |
| `git ls-files '*.py'`, counted by top-level directory | 14 under `.github`, 3 under `evals`, 1 under `hooks`, 16 under `lib`, 20 under `skills`, 149 under `tests` |
| `git grep -l <script> -- .github/workflows` for each file under `.github/scripts/` | one or two workflows for twelve scripts; none for `finding_counts.py` and `plugin_directory_check.py` |
| `grep -n '^\| 2026-11-23' frame/plan.md`, in the work item | two rows, `:74` and `:75` |
| A script counting each quote of `pr.md` in its source, runs of whitespace collapsed | all five found, once each |
| `git grep -h -E '^\| 20.*regression' -- 'seal/threads/*/frame/plan.md'`, the last cell of each row | six rows; one regression route names `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* and `docs/running/the-run.md` *The run*, and this work item's names the first alone |
