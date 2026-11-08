# Review round 3: 1794142459-parity-reads-original-forward

```seal
target: ee6ea32a3, fixes dc8a3da5e..ee6ea32a3
```

This is a verifying round over the diff of round 2's fixes,
`dc8a3da5e..ee6ea32a3` (executed: `git log dc8a3da5e..HEAD` lists
`d8e6f4d76` round 2, `267ac10fa` the orchestrator's route rows, its
correction of the fold row and its fold of *Scope* item 2, `1fcaac0ad` the
fixes, `475458849` the close blocks and `ee6ea32a3` the orchestrator's fold
of *Scope* items 1 and 2). The code read is that diff: the two rewritten
sentences of `skills/legacy-parity/SKILL.md` (`:78-82` and `:120-124`), the
reworked case at `tests/text/test_review_axes.py:99-113`, and the records
the range changes. Beside it, `routing.md`, the three frame files,
`gaps.md`, `changelog.md` and `pr.md` were read whole at `ee6ea32a3`, and
`trail/phases/` and `trail/rounds/round-1.md` and `round-2.md` for their
coordinates.

Carried from earlier rounds, not re-established: that no `seal/parity.md`
is declared in this repository, so no `original:` line is owed; round 1's
weighing of the template's guidance line at `frame/plan.md:62`, which this
diff does not touch; and round 2's weighing that `frame/design.md` *Scope*
item 6 is short of the new case's fact and not contradicted. Re-derived:
every verdict below, and the `check:` targets through `bin/seal rules
--check` (all 219 hold, executed).

## Findings

### 1. *Scope* item 2 says the sealer walks the list, where the built paragraph and phase 1 say it walks the original's surface

```seal
severity: should
location: `seal/threads/1794142459-parity-reads-original-forward/frame/design.md:37`
evidence: read `seal/threads/1794142459-parity-reads-original-forward/frame/design.md:37`, `skills/legacy-parity/SKILL.md:128-130`, `seal/threads/1794142459-parity-reads-original-forward/trail/phases/phase-1.md:45-53`, `seal/threads/1794142459-parity-reads-original-forward/frame/plan.md:66`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:3`; executed `git grep -n -o "walks the list[^.]*\|walks the surface[^.]*\|walks the original's surface[^.]*" -- . ':!seal/threads/*/trail/*'` and `git log -S "walks the list" 9e758b0b0..HEAD` over the work item
```

Why it matters: *Scope* item 2 states what *Parity review* says, and it
ends "Under `straight to the PR` the sealer walks the list the same way".
The paragraph at HEAD says "the sealer walks the original's surface the same
way" (`skills/legacy-parity/SKILL.md:128-130`), and `changelog.md:3` says
"walks the surface the same way". Phase 1 departed from the frame on exactly
this reading. Its record says that a walk of the list starts at the list, so
an item the list lacks is met by nobody, "which is the defect item 1
removes" (`trail/phases/phase-1.md:51-53`). The fold at `41f9d662c`
corrected the proofer's walk in item 2 and left the sealer's clause (the
`git log -S` above lists `377e21a3f`, the frame, and `41f9d662c`, which
kept the clause). The fold row at `frame/plan.md:66` names only the
proofer's walk. So the frame now gives the sealer the direction this work
exists to remove. The sealer reads the frame against the tree, and a fix
pass or a later framer that takes item 2 as the statement of *Parity
review* would restore that direction. The `git grep` above lists this
clause as the one statement in the work item's present records of a walk
of the list.

This is not a `regression:` line: no fix pass's commit made the clause. It
stands since the frame's commit, and no earlier round named it. The fix
touches the work item's records alone, so the sealer reads it, and a
fourth round would catch nothing that read does not.

In `frame/design.md` *Scope* item 2, the last sentence but one:

```markdown
Under `straight to the PR` the sealer walks the original's surface the same way, and its record stays the `original:` line *Recording the comparison* gives it.
```

```seal
verdict: fixed e46f18d67
answer: The finding holds. `frame/design.md` *Scope* item 2 now reads "the sealer walks the original's surface the same way", as `skills/legacy-parity/SKILL.md` *Parity review* and `changelog.md` say. The fold is the orchestrator's, in the work item's records alone, and `frame/plan.md` *Judgments of the run* holds its row, which also ends the rounds here.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the case `test_an_item_the_list_and_the_port_both_lack_is_located_in_both`
now guards "port's entry point" between `` `location:` `` and
`` `frame/design.md` `` (`tests/text/test_review_axes.py:111`). The phrase
stands once in *Parity review*'s prose, in the both-lack sentence
(executed: `grep` over `skills/legacy-parity/SKILL.md:114-131`). With the
port clause removed from that sentence by an Edit, the case failed on
`tests/text/test_review_axes.py:111` with "does not locate an item both
lack with \"port's entry point\"", exit 1 (executed). The fix pass's claim
that `seal mutate` turned the case red on the same guard therefore holds
as stated. The comment names the two places, and the docstring follows the
reworded sentence.

```seal
confirms: round-2#2
```
What holds: *Parity review* gives an item that the list and the port both
lack "the verdict an item the port does not send takes", which is the
sentence before it: `differs` by default, `grounded` where a quoted policy
clause leaves it out (`skills/legacy-parity/SKILL.md:117-124`). Its
`location:` names `frame/design.md`, and the port's entry point only where
the verdict is `differs`. *The original's coordinates* says the same
without a verdict word, "where the port lacks it too with no grounds for
leaving it out, in the port as well" (`:80-82`), so the tracer's section
gives no verdict, as round 1's finding 2 asked. The fix pass reworded the
snippet's "the verdict the sentence before gives it", and the new wording
names the same verdict, so the sentence has one reading. Every statement of
the both-lack location now follows the verdict (executed: `git grep` on
"both lack", "port as well", "lacks it too" and "port's entry point beside"
outside `trail/`). It lists `changelog.md:3` and `:6`, `frame/design.md:36`
and `:37`, the skill's two sentences and the case's docstring, each
conditional. `frame/plan.md:69` also appears there, and it is a judgment row
that states the fold of `5c6575aaf`, which HEAD does not contradict.

```seal
confirms: round-2#3
```
What holds: the grounds of the fold row at `frame/plan.md:69` now say the
close blocks named *Scope* items 1, 3 and 5 and *Removes*, and that item 2
was short and the orchestrator's own addition. Round 2 read round 1's four
close blocks for that (`round-1.md:80`, `:122`, `:169`, `:213`), and this
round carried those coordinates and opened them: the four `verdict:` lines
are at those lines. The row now names its source correctly.

What matched: the three new rows of `frame/plan.md` *Judgments of the run*,
read against HEAD. The rows at `:70` and `:71` route round 2's two
regressions to an ordinary fix pass, and the second row of the table in
`skills/code-review/orchestration.md` *A regression is routed by comparing
the fix with the frame* (`:239`) gives that route both to a fix that did
something the frame does not say and to a review record's paste-ready fix
applied as given. The third row of that table (`:240`) did not apply: round 2
held the run's first `regression:` lines (read: `round-1.md` holds none).
Row `:71`'s claim that the fold at `dc8a3da5e` copied the sentence into
*Scope* item 2 holds (executed: `git diff dc8a3da5e..HEAD` over
`frame/design.md` shows the old item 2 with "is one finding, `differs`").
Row `:72`'s claim that the fix pass named both items as contradicted holds
(read: the close of `round-2.md` finding 2 names *Scope* items 2 and 1). Its
fold is what `ee6ea32a3` did (executed: `git diff --word-diff 267ac10fa
ee6ea32a3` over `frame/design.md`).

What matched: each of the six quotes in `pr.md` stands at its source,
word for word with runs of whitespace collapsed (executed: a script over
`pr.md` against `changelog.md`, `frame/plan.md` and `gaps.md` printed six
matches). The second quote is still the sentence of `changelog.md:3` that
the fix left unchanged.

What matched: the closing memo's diff. Row 1 of `## Not verified` is
reworded in place with the same item and answerer, and no row left (read:
the range's diff of `gaps.md`). Its new clause on round 2's fix pass is the
implementer's account. The one Python file that pass changed passes the
lint and the format check (executed: `uvx ruff check` and `uvx ruff format
--check` over `tests/text/test_review_axes.py`, both exit 0). The
`## Not done` paragraph now names the fix pass as the party that rewrote
the tracer's step 3, which round 2 weighed.

What matched: the phases' greps still print what their rows say (executed:
`git grep -n "Start every comparison there" -- . ':!seal/threads'` printed
nothing, exit 1; `git grep -n "included/excluded fields" -- .
':!seal/threads'` printed the one cell `skills/code-review/SKILL.md:81`).

Weighed and not raised: no case holds that the port's location follows the
verdict. With the both-lack sentence edited back to round 2's defect, "one
finding, `differs`, whose `location:` names the port's entry point beside
`frame/design.md`", the module passed, 10 passed, exit 0 (executed). The
fix pass's close of round 2's finding 2 declines that guard, because a guard
on "where the verdict is" would pin wording. That reason stands on the row
of `docs/running/what-a-script-gates.md` *The checks* at `:67`. The two
sentences differ only in the clause that refers back to the sentence before
it, and no token outside that wording separates them. So this round opens
no finding on it. A revert of the condition is caught by a reader of
*Parity review* and by no case, and a later round could catch it only by
reading.

## Not judged

| What | Location | Who answers |
|---|---|---|
| whether a framer, a tracer and a proofer in a migration act on the rewritten sentences; no original resolves here and no case runs any of them | `frame/questions.md` Q1, `gaps.md:8` | a measurement: the orchestrator of the first migration run after the release |
| the full suite, the repository-wide lint and the format check at the target; this round ran four modules, `seal rules --check`, and the lint and format check over one file, and the suite stays `unverified`, which is the label `gaps.md:7` gives it | `gaps.md:7` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_review_axes.py tests/text/test_the_record_is_written_in_words.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist` | 122 passed, exit 0 |
| `bin/seal rules --check` | "all 219 check lines in 68 rule files hold", exit 0 |
| the Edit of `skills/legacy-parity/SKILL.md:121-124` to drop the port clause, then `bin/test "tests/text/test_review_axes.py::test_an_item_the_list_and_the_port_both_lack_is_located_in_both" -q -p no:xdist`, then the Edit back | exit 1, failing at `tests/text/test_review_axes.py:111` on "port's entry point"; `git status --short` clean afterwards |
| the Edit of `skills/legacy-parity/SKILL.md:121-124` back to round 2's defective sentence, then `bin/test tests/text/test_review_axes.py -q -p no:xdist`, then the Edit back | 10 passed, exit 0; `git status --short` clean afterwards |
| `uvx ruff check tests/text/test_review_axes.py`; `uvx ruff format --check tests/text/test_review_axes.py` | exit 0, exit 0 |
| a script comparing each `pr.md` quote with its source, whitespace collapsed | six matches |
| `git grep` on the both-lack location and on what the sealer walks, outside `trail/` | the statements listed under the confirmation of `round-2#2` and under finding 1 |
