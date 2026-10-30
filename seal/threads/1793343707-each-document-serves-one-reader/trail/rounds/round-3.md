# Review round 3: 1793343707-each-document-serves-one-reader

target: e7ad0fe1, fixes d0ad1d03..e7ad0fe1

## Findings

### 1. The settle's step 7 puts `seal settle --apply` under its `flow-baseline` condition, so a repository with no log reads no removal

severity: should
location: `skills/settle/SKILL.md:219-227`, `tests/text/test_settle_reads_before_it_removes.py:138`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:131`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:265`
evidence: read `skills/settle/SKILL.md:219-227`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:56`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:131`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:265`, `skills/verify/orchestration.md:204-207`
verdict: open
regression: round-2#1

The unit is step 7 of `skills/settle/SKILL.md` *The settling session's
procedure*, which round 1's fix pass added at `0a15911b` and `634e8b26`
rewrote. The frame's Scope item 7 says the session takes the counts at
step 7 "before it runs `seal settle --apply`", with no condition on the
removal; the fix opened the step with "Where the repository keeps a
`flow-baseline` log" and closed it with "Then run `seal settle --apply`";
the defect came from round 2's paste-ready text for finding 1, which had
that shape, and the fold at `e7ad0fe1` copied it into the Table B row.

The step now reads: where a log is kept, count; post the four numbers to
that log; then run `seal settle --apply`. In a repository with no log, the
count and the post do not apply. Whether the removal still applies, the
step does not say: "Then" follows a post that did not happen.
`skills/verify/orchestration.md:204-207` says most installed repositories
never create the label, so this reader is the common one. The Table B row
at `frame/design.md:131` states it in one sentence, and its grammar puts
the removal under the condition: "where the repository keeps a
`flow-baseline` log, it states and counts the four numbers ... and posts
them there, then runs `seal settle --apply`". A settling session that takes
that reading removes no released directory, runs step 8 and opens the
settle's pull request with every record still on disk. Before `634e8b26`
the step had no condition, and the removal had one reading.
`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다* names this defect: a condition that drops out of an
instruction, or attaches to the wrong clause.

The same class holds one more place. The `add` to *The run* at
`frame/design.md:265` puts the condition on the post alone: the session
"counts them at step 7 ..., and posts them to the `flow-baseline` log
where the repository keeps one". The step puts it on the count too. The
policy sentence cites the step for how, so the two should agree on when.
The changelog row at `changelog.md:20` and Scope item 7 already agree with
the step, or say nothing of the removal.

```markdown
<!-- skills/settle/SKILL.md, step 7, from the end of the list -->
   `seal/threads/` is deleted from them, and the record files. Post the four
   numbers to that log. With a log or without one, run `seal settle --apply`
   next, which removes the records.
```

```python
# tests/text/test_settle_reads_before_it_removes.py:138, the step 7 entry
        "With a log or without one, run `seal settle --apply` next, which "
        "removes the records.",
```

The two frame lines are the framer's, and the orchestrator folds them.
The Table B row's decision cell at `frame/design.md:131` reads "kept; step
7 of *The settling session's procedure* is the home of the measure: where
the repository keeps a `flow-baseline` log, it states and counts the four
numbers for each released work item routed through the review chain and
posts them there; with a log or without one, it then runs `seal settle
--apply`; `docs/the-review-record.md` *The run* cites it (*Scope* item
7)". The `add`'s second sentence at `frame/design.md:265` reads "Where the
repository keeps a `flow-baseline` log, the settling session counts them
at step 7 of `skills/settle/SKILL.md` *The settling session's procedure*,
which says how, and posts them there."

answer:

### 2. The settle's step 7 counts with `git grep`, which reads no round record in local mode

severity: should
location: `skills/settle/SKILL.md:222`, `tests/text/test_settle_reads_before_it_removes.py:150-151`
evidence: executed `git grep -h '^\[core\]' -- .git/config`, `grep -n 'procedure is the same' skills/settle/SKILL.md`
verdict: open
regression: round-2#1

The unit is step 7 of `skills/settle/SKILL.md` *The settling session's
procedure*, as in finding 1. The frame's *Data & interfaces* gives the four
counts as `git grep -h` commands over `seal/threads/<id>/trail/rounds/`,
run in this repository, whose `Mode` is `shared` (`seal/config.md:9`); the
fix wrote `git grep -h` into the shipped step; the defect came from round
2's paste-ready text, which carried the design's command for this
repository into a step that every repository's settling session reads.

*In local mode* in the same skill says every `seal/threads/<id>/` path is
read under `$(git rev-parse --git-common-dir)` (`skills/settle/SKILL.md:273`),
and "The settling session's procedure is the same"
(`skills/settle/SKILL.md:309`). `git grep` searches the tracked files of
the work tree, and nothing under the git directory is tracked. Over
`.git/config`, which holds a `[core]` line, `git grep -h '^\[core\]'`
printed nothing and exited 1. So in a local-mode repository that keeps a
`flow-baseline` log, three of the four counts read zero and the file count
does not. The session posts those zeros to the durable log. The `add` to
*The run* reads a records-alone count that falls as the structure working,
so a zero reads as success that did not happen.

```markdown
<!-- skills/settle/SKILL.md:222, step 7 -->
   chain, with `grep -h` over its `trail/rounds/round-*.md`: the
```

The line assumes the session resolves `seal/threads/<id>/` as *In local
mode* says. `grep` reads the files wherever they lie and needs no other
precondition. Rule 14 asks a pin for the changed text; the entry goes in
the same case, after "count for each released work item routed through
the review chain":

```python
# tests/text/test_settle_reads_before_it_removes.py, the step 7 entries
        "with `grep -h` over its `trail/rounds/round-*.md`",
```

The guard at `tests/text/test_settle_reads_before_it_removes.py:152-153`
reads step 6 alone and stays right after this change. The comment above
it names the tool step 7 uses, so it changes with the step:

```python
# tests/text/test_settle_reads_before_it_removes.py:150-151
    # Step 6 alone: step 7 counts the round records with `grep`, which
    # searches no test (round 2 of #1148, finding 1).
```

answer:

## Confirmations

confirms: round-2#1
The close holds as far as the finding asked: step 7 states the four counts
itself, and no shipped sentence sends the reader to *The run* for them.
`git grep` for "The run* names" and "as that section says" over `skills`,
`docs`, `tests`, `agents`, `templates`, both READMEs and the frame printed
nothing (executed). The fix pass claimed the pins were seen red before the
step changed. With `skills/settle/SKILL.md` at `d0ad1d03`, the procedure
case failed on the missing step 7 entries (executed). It claimed two
mutants went red. Planting a `git grep` in step 6 failed the case on "step
6 still searches the tests' text", and dropping "Post the four numbers to
that log." failed it on that entry (executed, each alone, through the
`Edit` tool in the clone). The fix pass departed from round 2's text twice
and gave grounds for both. The heading phrase: a `### <n>.` written in the
step holds the characters `## `, and the case cuts the procedure at
`split("## ")`, so the round's phrase would have cut step 7 short (read,
`tests/text/test_settle_reads_before_it_removes.py:109`). The guard: its
message always named step 6, and the slice it now reads is step 6 whole,
from "6. Run each rule's" to the one " 7. " of the procedure, each found
once, with `git grep` in the procedure and not in the slice (executed). The
slice fails closed. A moved step 6 opening raises at the split, and a lost
" 7. " widens the slice to step 7's `git grep`. Findings 1 and 2 above are
new defects in the unit this fix rewrote.

confirms: round-2#2
The close holds. `frame/design.md:56` names
`tests/text/test_settle_reads_before_it_removes.py#test_the_skill_states_the_settling_sessions_procedure`
(read). `git grep` finds the step's opening clause pinned only at
`tests/text/test_settle_reads_before_it_removes.py:130` (executed).

confirms: round-2#3
The close holds. The `to:` at `frame/design.md:250` now opens "It is
spawned after the last fixes are committed, and a fix pass owes none only
where ..." (read). `git grep -i 'fixes to a file outside'` over `skills`,
`docs` and the frame printed nothing (executed). `rule_changes.parse` over
the design at `e7ad0fe1` read 17 operations with no refusal, and every
`section` and every `from` stands in its document (executed).

confirms: none
The narrow modules that read a path the fix changed,
`tests/text/test_settle_reads_before_it_removes.py`,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`,
`tests/skills/test_settle.py` and `tests/skills/test_rule_changes.py`, gave
198 passed, exit 0 (executed). Step 7 newly cites
`skills/verify/orchestration.md` *Measure the segment, and feed the flow
log*, which stands at `skills/verify/orchestration.md:153` (executed).
`ruff check` and `ruff format --check` over the one Python file the fix
diff changed exited 0 (executed). Each of the four commits carries
`Seal-Routing: 1793343707-each-document-serves-one-reader` (executed).
`83a6fbfa` changed only round 2's three `verdict:` and `answer:` lines
(executed, `git diff`). No test function was added, so no group was read.
Carried from round 2 and not re-established: round 2's search showing *The
run* holds no count at `fba13ab2`, and its coordinates for the pin's case.
Re-run: every executed line of round 2's three findings.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Findings 1 and 2 are regressions on step 7, the unit round 2's finding 1 already found a regression in after a fix-pass route. `docs/the-review-record.md:609-610` sends a second regression on the same unit to the framer whatever the comparison says; how this run routes them, and how the cap applies, is the orchestrator's | `skills/settle/SKILL.md:219-227` | the orchestrator |
| Round 1's finding 6 stands `deferred frame/questions.md Q2` and is not written up again; its counts were not re-taken, since the fix diff touches no path outside `seal/threads/` but the settle skill and its test | `seal/threads/1793343707-each-document-serves-one-reader/frame/questions.md` | the owner, answering Q2 |
| Carried from round 2: 19 of the 25 commits in `fba13ab2..b3b36143` carry no `Seal-Routing:` trailer | `fba13ab2..b3b36143` | the orchestrator |
| Carried from round 1: a finding located in `frame/design.md` `## Rule changes` and fixed there alone passes with no round, and the settle writes that text into the policy root | `skills/code-review/scripts/chain_check.py:1452-1456` | the owner |
| Carried from round 1: the behaviour suite over the four agent definitions, not run on Q1's default | `seal/threads/1793343707-each-document-serves-one-reader/frame/questions.md` | the owner, at the pull request |
| Carried from round 1: GitHub's rendering of the body's fold | `skills/code-review/scripts/pr_body.py` | the orchestrator, reading the first body this change writes |
| The full suite, the repository-wide lint and format check, and the cross-platform run at `e7ad0fe1`; the suite is `unverified` here | the branch at `e7ad0fe1` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_settle_reads_before_it_removes.py -q -p no:xdist` in the clone at `e7ad0fe1` | exit 0, `17 passed` |
| The procedure case's step 6 slice computed with the case's own `flattened` and splits | each marker found once; the slice is step 6 whole; `git grep` in the procedure, not in the slice |
| `git checkout d0ad1d03 -- skills/settle/SKILL.md`, then `bin/test ... -k settling_sessions_procedure -p no:xdist`, then the file restored from `e7ad0fe1` | exit 1, `1 failed`, the step 7 entries missing; `git status --short` empty after the restore |
| Step 6's last sentence edited to hold `git grep -l`, then the same case, then the file restored | exit 1, "step 6 still searches the tests' text"; restored |
| "Post the four numbers to that log." deleted, then the same case, then the file restored | exit 1, that entry missing; restored |
| `git grep -h '^\[core\]' -- .git/config` in the clone | no output, exit 1 |
| `rule_changes.parse` over the design at `e7ad0fe1`, each op's `section` and `from` looked up in its document | 17 ops, 0 refusals, 0 missing |
| `bin/test` over the four narrow modules named in the last confirmation | exit 0, `198 passed` |
| `uvx ruff check` and `uvx ruff format --check` over `tests/text/test_settle_reads_before_it_removes.py` | exit 0 and exit 0 |
