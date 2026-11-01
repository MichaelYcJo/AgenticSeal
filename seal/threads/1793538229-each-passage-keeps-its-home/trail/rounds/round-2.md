# Review round 2: 1793538229-each-passage-keeps-its-home

```seal
target: 6ed359a5, fixes 4785c1da..6ed359a5
```

This is a verifying round. Its target is the diff of round 1's fixes, `4785c1da..6ed359a5`: `541e8c5e` (the orchestrator's fold of finding 1 into `frame/design.md:3` and `:14`, and one new row in `frame/plan.md` *Judgments of the run*), `25c268b4` (the fix pass's one-line change to the module docstring) and `6ed359a5` (the close block). `git diff --stat 4785c1da..6ed359a5` lists those four files and nothing else (executed). No `seal/parity.md` is declared, so the round writes no `original:` line. The review ran in a `git clone --no-local` of the branch worktree at `6ed359a5`, under the round's scratch directory.

Carried from round 1 and not re-established: the coordinates `docs/branch-and-release.md:158` and `docs/one-root-by-lifetime.md:45-46` for what a squash does to a SHA citation, and round 1's verdicts on the phase's code, which this round does not re-review. Re-run rather than carried: round 1's `evidence: executed` line for finding 1. `79252e48` is still no object in a fresh clone, still no ancestor of `origin/main` (exit 1), and the measure's `trail/phases/phase-1.md` is byte for byte the same at `79252e48` and `48d035aa` (`git diff --quiet`, exit 0, in the worktree, whose object store holds both).

The orchestrator asked this round to judge one line the fix pass left: `trail/phases/phase-1.md:7`, which still says the measure "stand[s] at `79252e48`". The judgment is under *Confirmations*: it stands.

## Findings

### 1. The new judgment row counts the orphaned citation as one instance found by a round, and the tree and the tracker hold more, seven of which passed a sealed chain

```seal
severity: should
location: `seal/threads/1793538229-each-passage-keeps-its-home/frame/plan.md:46`
evidence: executed `git grep -n '79252e48:' 5f0cf7a7 -- seal`, `git merge-base --is-ancestor 48d035aa 569780ef`, `git log --oneline origin/release/v0.27.3 -- seal/threads/1793521558-the-record-decides-each-proposed-verifier`, `git grep -l 79252e48 origin/release/v0.27.3`, `gh issue list --state all --search 79252e48`, `gh issue view <N> --json body -q .body, for N in 1231 to 1236, 1255 and 1256`
regression: round-1#1
```

Why it matters: the unit is the row `541e8c5e` added to `frame/plan.md` *Judgments of the run*, line 46. The phase's plan row delivers *Scope* items 1 to 7, and *Scope* item 7 has the docstring "cite the measure at its commit"; the fold moved that citation to `48d035aa` and added a row deciding that no issue is filed for a check of `<sha>:<path>` citations, on the grounds "one instance, found by the round that reads every citation"; the defect came from round 1's second `## Not judged` row, which left the class beyond the diff unenumerated, being answered with the count of what round 1 happened to find.

`skills/core/SKILL.md` *The first value: efficient development through the workflow*, in its paragraph "A judgment stands on a source document", says the settle reads these rows "against what they cost and caught" and rewrites the guidance where a kind of judgment keeps costing more than it returns. This row tells the settle that the class had one instance and that a round catches it. Both halves are contradicted by commands that list every citation of this one commit:

- `git grep -n '79252e48:' 5f0cf7a7 -- seal`, at this branch's base, lists 7 more `<sha>:<path>` citations of the same commit, outside this work item: `seal/threads/1793521558-the-record-decides-each-proposed-verifier/frame/design.md:60`, `frame/plan.md:13`, and `trail/phases/phase-3.md:29`, `:30`, `:364`, `:500` and `:507`. That work item merged as `569780ef` (#1257), and `48d035aa` is an ancestor of `569780ef` (exit 0). The squash had therefore landed before #1257 merged, and those citations passed that work item's rounds and its sealer already orphaned. No round caught them.
- The 0.27.x settle, `14bfd992` on `origin/release/v0.27.3`, removed that work item, and `git grep -l 79252e48 origin/release/v0.27.3` lists nothing (exit 1). So in the tree this branch merges into, the count is this work item's own lines. The row does not say its count is scoped that way.
- The bodies of eight open issues cite `79252e48`: #1231 (three times), #1232, #1233, #1235 and #1236 (twice each), #1234, #1255 and #1256 (once each). `phase-3.md:533` and `:557` of the settled work item are draft issue bodies, "The measure is ... at `79252e48`", so the drafts carried the orphaned SHA into the tracker. #1231 is this work item's own issue, which the sealer reads.

The row can still decide that no check is built: a tree check reads no issue body, and the settle removed the seven record lines. That weighing is the orchestrator's. What the row may not do is give the settle a count of one and a catch by a round where the record shows seven citations a sealed chain merged and eight issue bodies. Contract rule 12 asks a hand-back to name its method and to call a sample a sample. The row names no method, and "one instance" is the instance round 1 met.

The grounds cell, rewritten in place. The judgment cell's last sentence stays or reverses on these grounds, at the orchestrator's weighing:

```markdown
`git merge-base --is-ancestor 48d035aa origin/release/v0.27.3` exits 0 (executed). The class, listed for this one commit by `git grep -n '79252e48:'` at the base `5f0cf7a7` and `gh issue view <N> --json body` (executed): this work item's docstring and two frame lines, fixed; its `trail/phases/phase-1.md:7`, a record of what phase 1 read, kept; seven citations in `seal/threads/1793521558-the-record-decides-each-proposed-verifier/`, which #1257 merged at `569780ef` after `48d035aa` had landed, so no round of that work item caught them, and which the 0.27.x settle `14bfd992` removed; and the bodies of #1231 to #1236, #1255 and #1256. A citation of another squashed commit is not listed, so the list is a sample of the class. Weighed against a new mechanism: a tree check would have refused #1257's seven lines and reads no issue body
```

```seal
verdict: fixed 0d248cf2
answer: The finding holds. The orchestrator rewrote the row at `frame/plan.md:46` in place with the round's grounds cell, which names the method and calls the list a sample, and reversed its last judgment: the class is filed as #1270 rather than judged one instance. Nothing outside the work item's records changed.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `tests/text/test_no_passage_is_pasted_into_a_second_file.py:30` cites `48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md` *The table*, row K2. In the fresh clone `git cat-file -t 48d035aa` answers `commit` and `git cat-file -t 79252e48` answers "Not a valid object name", so the citation now opens where the old one did not. `48d035aa` is an ancestor of `origin/main` and of `origin/release/v0.27.3` (exit 0 each). Row K2's *Grounds* at `48d035aa` holds the docstring's clause "a link would cost every spawn a read and remove nothing said twice" (`git show ... | grep -c`, 1). The close claimed the module green and lint clean. In the clone at `6ed359a5`, `bin/test` over the module and `tests/test_censuses.py` passed 185, and `ruff check` and `ruff format --check` on the module exit 0. `git grep 79252e48 6ed359a5` lists no file outside `seal/threads/`, so the close's narrower search over six directories and the root files holds over the whole tree. Executed.

```seal
confirms: none
```
What matched: `frame/design.md:3` and `:14` cite the measure at `48d035aa`, and `:3` tells the reader to "read with `git show 48d035aa:<path>`", which resolves in the fresh clone. The plan row's clause "the squash on `main`" holds: `48d035aa` is an ancestor of `origin/main` (exit 0). `tests/test_censuses.py` read the new plan row and the changed frame lines green in the run above. Executed.

```seal
confirms: none
```
What matched: `trail/phases/phase-1.md:7` stands as written. The sentence records what the crafter read before the first edit: "The measure's row K2 and *Instances K2* stand at `79252e48` as design G6 quotes them". That was true where the crafter read it, since the main checkout's object store holds `79252e48`, and the worktree resolves it today. Rewriting the SHA would make the record say phase 1 read a commit it did not read, and `skills/core/SKILL.md` *The rule a mechanism is kept against* sends history to the work record. The line differs from the two frame lines round 1 named: it tells no reader to run `git show` on the SHA. A reader who re-checks the claim reaches the same bytes at `48d035aa`, which `frame/design.md:3` names (`git diff --quiet` of the two blobs, exit 0). "As design G6 quotes them" still holds, since G6's quoted text is unchanged and only its SHA moved. The line leaves with the work item at the settle. The fix pass named the line in its close block rather than leaving it unsaid. Executed and read.

```seal
confirms: none
```
What matched, outside the fix diff and reported because it was opened: this branch's base has moved. `origin/release/v0.27.3` gained the 0.27.x settle `14bfd992`, and HEAD does not descend from it (`git merge-base --is-ancestor`, exit 1). The settle rewrote `docs/the-record-layout.md`, and the rule change's `from`, "No two rule documents may share more 15-word runs than their pair was measured at, which does not see a rule restated in fresh words.", still stands in it, whitespace collapsed (`grep -o`, exit 0). The settle touched none of the other three files this branch changes (`git diff --stat 5f0cf7a7 origin/release/v0.27.3`). Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `6ed359a5` | `gaps.md` *Not verified*, first row | the orchestrator, by `seal gate`, once the rounds settle |
| Bringing the moved base `origin/release/v0.27.3`, which holds the settle `14bfd992`, into the branch before the gate; this round read only whether the rule change's `from` survives it | the branch | the orchestrator |
| Whether a check of `<sha>:<path>` citations is filed, re-weighed on finding 1's count; and whether the eight issue bodies citing `79252e48` are edited to `48d035aa` | `frame/plan.md:46`; issues #1231 to #1236, #1255, #1256 | the orchestrator |

## Probes

No probe file was written; each row is a command run once.

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree, `git checkout 6ed359a5`, then `git cat-file -t 48d035aa` and `git cat-file -t 79252e48` in the clone | `commit`, exit 0; "fatal: Not a valid object name 79252e48", exit 128 |
| `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/test_censuses.py -q -p no:xdist`, in the clone | exit 0, 185 passed |
| `uvx ruff check` and `uvx ruff format --check` on `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, in the clone | both exit 0 |
| `git merge-base --is-ancestor 48d035aa` against `origin/main`, `origin/release/v0.27.3`, `release/v0.27.3` and `569780ef`; `79252e48` against `origin/main`; `origin/release/v0.27.3` against `6ed359a5` | 0, 0, 0, 0; 1; 1 |
| `git diff --quiet 79252e48:<path> 48d035aa:<path>` for the measure's `phase-1.md` and `phase-2.md`, in the worktree | exit 0 for each |
| `git grep -n 79252e48 6ed359a5`; `git grep -n '79252e48:' 5f0cf7a7 -- seal`, without this work item's lines; `git grep -l 79252e48 origin/release/v0.27.3` | only lines under `seal/threads/` at HEAD; 7 lines, all in `1793521558`; nothing, exit 1 |
| `gh issue view <N> --json body -q .body`, counting `79252e48`, for 1231 to 1236, 1255, 1256 and 1102 | 3, 2, 2, 1, 2, 2, 1, 1, 0 |
