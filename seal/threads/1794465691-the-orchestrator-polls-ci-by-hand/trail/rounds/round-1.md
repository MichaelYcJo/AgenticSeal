# Review round 1: 1794465691-the-orchestrator-polls-ci-by-hand

```seal
target: be4b321da against release/v0.38.0
```

This is the first round, so no earlier record carries a coordinate, and
every fact below was established here unless it says it was carried. The
diff was read from the base `79f815a74` to `be4b321da`. `routing.md`, the
three frame files, `gaps.md`, `changelog.md` and `pr.md` were each read
whole at `be4b321da`, and both phase records after them. No `pr.<lang>.md`
stands, and none is owed: `seal/config.json` names English for both
language keys. No `seal/parity.json` is declared. The probes ran in a
`git clone --no-local` of the branch at `be4b321da` under the round's
scratch directory, never in the branch worktree.

Carried and not re-established: the frame's measurements of live `gh`
answers, *Grounding* G9 to G12 (pull request #1537, the jobs of its `tests`
run, the run durations, the concurrency of the two workflows). They need
the network and a real pull request, and `frame/questions.md` Q1 is the
measurement that answers them for this command. G7 was re-read here, in
the framer's copy of `pkg/cmd/pr/checks/checks.go` and `aggregate.go` at
v2.92.0: the exporter returns at `checks.go:189-190` before any exit is
computed, `no checks reported` is an error at `checks.go:302-303`, and the
buckets stand at `aggregate.go:73-82` as G7 gives them.

## Findings

### 1. A head that moves after the wait has started makes `seal pr-wait` wait forever and print nothing

```seal
severity: should
location: `skills/code-review/scripts/pr_wait.py:319-336`, `skills/code-review/scripts/pr_wait.py:43-48`, `skills/code-review/orchestration.md:272-275`, `skills/code-review/orchestration.md:283`, `tests/skills/test_pr_wait.py`
evidence: executed `bin/test -q -p no:xdist tests/skills/test_tmp_round1_probe.py` in the round's clone (`test_tmp_head_moves_after_the_start`: views `[view(), view(head=BEFORE)]`, one pending `pull_request` check, ends on the fake clock's "the wait never ended" at 3600 seconds); read `skills/code-review/scripts/pr_wait.py:311-336`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/frame/plan.md:17`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/trail/phases/phase-1.md:92-95`
```

Why it matters: the orchestrator runs the wait after every push and acts
on its exit code. Once a `pull_request` check has been listed on HEAD,
`started` is true, and a later read whose `headRefOid` is not HEAD takes
the `elif pr["headRefOid"] != sha` branch at `pr_wait.py:322-323`. That
branch reads no check, and the limit at `pr_wait.py:331` applies only while
`started` is false. So the loop sleeps and reads again with no end and no
line on stdout. The probe ran that loop to the fake clock's one-hour guard.
The procedure this replaces had no such hang: `gh pr checks --watch` read
whatever the pull request's head was, and ended.

Claimed: `frame/plan.md:17`, row 1, says "only the orchestrator pushes to
a work item's branch", and `trail/phases/phase-1.md:92-95` and the docstring
at `pr_wait.py:46-48` take the hang as that assumption's consequence. Found:
the assumption does not hold for the pull request this command waits on.
GitHub's own "Update branch" button pushes a merge of the base onto the
branch, and the base of this release moves each time another work item
lands on it. Nothing in the SDD set or a policy document says the wait may
run without end. The paragraph at `orchestration.md:272-275` tells the
orchestrator that the wait "ends when no check is pending", which is not
true on this path.

The fix ends the wait at exit 3 once the head leaves HEAD after the start,
naming both commits. Exit 3's act already fits: report, wait no longer, do
not treat the pull request as checked.

```python
        elif pr["headRefOid"] != sha:
            if started:
                return NO_CHECK, [
                    f"the pull request's head moved from {sha} to "
                    f"{pr['headRefOid']} after its checks started, so no "
                    "check on the commit pushed last can be read"
                ]
            why = f", and the pull request's head stayed {pr['headRefOid']}"
```

The same fact stands in more places, and the fix pass owes each of them.
The docstring's exit 3 entry at `pr_wait.py:22-24` gains the moved head,
and the sentence at `pr_wait.py:46-48` that says the command keeps waiting
is removed. Row 3's *When* cell at `orchestration.md:283` gains the moved
head. The exit 3 sentence of `changelog.md:3` changes too. A case in
`tests/skills/test_pr_wait.py` `Test_wait` serves `[view(), view(head=BEFORE)]`
with a pending check and asserts exit 3 and the line. It is seen red
against the code as it stands, where it ends on the fake clock's guard.
`frame/design.md:85` and `:90` state the exit and the limit, and they are
the orchestrator's to amend with the frame.

### 2. Under a `mergeable` that stays `UNKNOWN`, exit 3 says no check was listed, and the paragraph has the orchestrator report it, though the command read no check

```seal
severity: should
location: `skills/code-review/scripts/pr_wait.py:319-335`, `skills/code-review/scripts/pr_wait.py:22-24`, `skills/code-review/orchestration.md:283`, `tests/skills/test_pr_wait.py:410-427`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/changelog.md:3`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/frame/design.md:85`
evidence: executed `bin/test -q -p no:xdist tests/skills/test_tmp_round1_probe.py` in the round's clone (`test_tmp_unknown_says_no_check_listed_with_checks_reported`: a rollup of three checks, `mergeable` `UNKNOWN`, exit 3 with the line opening "no check of a pull_request run was listed on", and no `gh pr checks` call); read `git show release/v0.38.0:skills/code-review/orchestration.md` lines 266-278 and 305-313, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/frame/design.md:58`
```

Why it matters: this is the act the closing memo's third row asks this
round to read. Under `UNKNOWN` the loop never calls `gh pr checks`
(`pr_wait.py:320-321`; the existing case asserts 13 calls, all `view`, at
`test_pr_wait.py:427`). Past the limit it still prints "no check of a
pull_request run was listed on <SHA> within 120 seconds", and row 3 at
`orchestration.md:283` then has the orchestrator say in its report "that no
check of a `pull_request` run reported on that SHA". The probe served a
rollup of three checks, and the command still printed that line. A report
built on it states a fact nobody read.

The two paragraphs this replaced kept the cases apart. At
`release/v0.38.0:skills/code-review/orchestration.md:277-278`, `UNKNOWN`
"means GitHub has not computed the answer yet, and the orchestrator reads
it again". At `:310-312`, the report that no check reported is made "Under
`OPEN` and `MERGEABLE`" alone. The frame asks that the output say which
cause held (`frame/design.md:58`, S8: "exits 3 past it, saying that
mergeable was never known"). The line does say it, but after a lead that
asserts something else. The frame's exit 3 row at `frame/design.md:85`
gives one report for all three causes, and that is where the paragraph's
row came from.

```python
        if not started and clock() - start >= LIMIT:
            if pr["mergeable"] == "UNKNOWN":
                return NO_CHECK, [
                    f"GitHub never said within {LIMIT} seconds whether the "
                    f"pull request is mergeable, so no check on {sha} was read"
                ]
            return NO_CHECK, [
                f"no check of a pull_request run was listed on {sha} within "
                f"{LIMIT} seconds{why}"
            ]
```

With that, the `UNKNOWN` branch at `pr_wait.py:320-321` sets no `why`. Row
3 of the paragraph becomes:

```markdown
| 3 | within the limit on the start, no check of a `pull_request` run was listed on HEAD, or GitHub never said whether the pull request is mergeable, and the output names the SHA and which | says in its report what the output names about that SHA, waits no longer, and does not treat the pull request as checked |
```

The pin's `"| 3 |"` still matches that row. The fix pass also owes the
other statements of this fact. These are the docstring's exit 3 entry at
`pr_wait.py:22-24`, the assertion at `test_pr_wait.py:420-426`, and the
exit 3 sentence of `changelog.md:3`. The orchestrator owes the frame's cell
at `frame/design.md:85`. Findings 1 and 2 both change exit 3's lines, so one
fix pass takes them together.

### 3. Three exit-2 guards the frame states hold no case: an unknown `mergeable`, a `gh pr view` answer without a head or rollup, and an answer that is not JSON

```seal
severity: should
location: `tests/skills/test_pr_wait.py:445-468`, `skills/code-review/scripts/pr_wait.py:216-220`, `skills/code-review/scripts/pr_wait.py:241-252`
evidence: executed `bin/test -q tests/skills/test_pr_wait.py` in the round's clone with the guards at `pr_wait.py:216`, `:241` and `:246-248` each replaced by `if False:` through `Edit`: 29 passed, exit 0, and the file restored with `git checkout` after the run; read `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/frame/design.md:32`, `:84`
```

Why it matters: `frame/design.md:84`, the exit 2 row that *Scope* item 1
builds to, names "a `bucket`, `state` or `mergeable` value that is none of
those G7 and G3 name" as exit 2. The `bucket` guard and the `state` guard
each have a case. The `mergeable` guard does not, nor does the shape guard
on `headRefOid` and `statusCheckRollup`, nor does `_answer`'s refusal of an
answer that is not JSON of its kind. With all three guards removed, every
case still passes. Without the `mergeable` guard, a value `gh` adds later is
neither `CONFLICTING` nor `UNKNOWN`, so `wait` reads it as mergeable and can
reach exit 0. That is the false pass the plan's *What breaks in six months*
(`frame/plan.md:11`) says a renamed value never reaches. These are the
*Regression test* row's `should`.

```python
    @pytest.mark.parametrize(
        "answer, said",
        [
            (
                view(mergeable="BLOCKED"),
                "could not read the answer: `gh pr view` answered mergeable "
                "'BLOCKED', which is none of MERGEABLE, CONFLICTING, UNKNOWN",
            ),
            (
                {**view(), "headRefOid": None},
                "could not read the answer: `gh pr view` answered no headRefOid "
                "string or no statusCheckRollup list",
            ),
            (
                {**view(), "statusCheckRollup": None},
                "could not read the answer: `gh pr view` answered no headRefOid "
                "string or no statusCheckRollup list",
            ),
        ],
    )
    def test_refuses_a_view_gh_does_not_shape(self, monkeypatch, answer, said):
        """S9: a value or a shape `gh pr view` does not name is exit 2."""
        serve(monkeypatch, views=[answer])
        with pytest.raises(PR.Unanswered) as raised:
            PR.once(12)
        assert raised.value.lines() == [said]

    def test_refuses_an_answer_that_is_not_json_of_its_kind(self, monkeypatch):
        """S9: `gh` printing a list where a dict is read is exit 2."""
        monkeypatch.setattr(PR, "gh", lambda *args: "[]")
        with pytest.raises(PR.Unanswered) as raised:
            PR.once(12)
        assert raised.value.lines() == [
            "could not read the answer: `gh pr view 12 --json "
            "state,mergeable,headRefOid,statusCheckRollup` printed no JSON dict"
        ]
```

Both cases go in `Test_once`, beside `test_refuses_a_state_gh_does_not_name`.
Each case is seen red with its own guard removed (contract rule 15). With
the `mergeable` guard or the shape guard gone, `once` returns exit 0 and the
case fails on `DID NOT RAISE`. With `_answer`'s guard gone, the list reaches
`answer.get` and the case fails on an `AttributeError`. That red is what the
command prints without the guard, as phase 1 read its `KeyError` and
`TypeError` reds.

### 4. The docstring cites no source for two of the four reasons *Scope* item 1 names, while the frame and the phase record say every reason cites one

```seal
severity: should
location: `skills/code-review/scripts/pr_wait.py:54-65`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/frame/design.md:32`
evidence: read `skills/code-review/scripts/pr_wait.py:52-85`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/frame/design.md:32`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/trail/phases/phase-1.md:99-110`, the framer's copy of `pkg/cmd/pr/checks/checks.go` at v2.92.0, lines 189-190 and 302-303
```

Why it matters: *Removes* row 3 moves the reasons for the reads out of the
skill and into this docstring, so after the settle the docstring is their
only home. `frame/design.md:32` says that "each reason cites a source that
outlives the work item". `trail/phases/phase-1.md:104-105` claims "Each
reason in `pr_wait.py`'s docstring states its fact with the source a reader
can still open". Found: the runs reason cites `.github/workflows/test.yml`
(`pr_wait.py:69`), and the cancelled reason cites `aggregate.go`
(`pr_wait.py:76`). The head reason (`:54-55`), the empty rollup reason
(`:56-60`) and the `pull_request` reason (`:61-65`) cite nothing, yet each
rests on a measurement of `gh` or of GitHub. The frame's sentence states
what the work does, and the target contradicts it.

```python
- **The head is compared with HEAD.** Right after a push the pull request
  still lists the commit before it, whose checks may all have finished
  (work item #1222, at tag v0.27.2).
- **The rollup is counted before the checks are asked for.** With no check
  reported, `gh pr checks` exits 1, with or without `--json`: its
  `no checks reported` is an error raised before its JSON is written
  (`pkg/cmd/pr/checks/checks.go` in `cli/cli`, at v2.92.0), while
  `gh pr view --json statusCheckRollup` exits 0 with an empty list. An exit
  1 is also every other `gh` failure, so this command reads "no check yet"
  from the empty list and takes every non-zero exit as exit 2.
- **The start counts checks of event `pull_request` alone.** A `push` run
  on the pushed commit lists its checks on the pull request too, often
  finished before the pull request opens (work item #1222, round 1, at tag
  v0.27.2). A check of another CI service,
```

The bullet's remaining lines stay as they are. The other way to close the
finding is to narrow `frame/design.md:32` to the reasons that rest on `gh`'s
code or on the workflow. That way leaves the measurements with no source.

### 5. `frame/design.md` says every exit's line names the SHA, and `--once` names the pull request's head while an early exit 2 names none

```seal
severity: should
location: `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/frame/design.md:92`
evidence: read `skills/code-review/scripts/pr_wait.py:339-345`, `:370-380`, `tests/skills/test_pr_wait.py:488-529`, `seal/threads/1794465691-the-orchestrator-polls-ci-by-hand/trail/phases/phase-1.md:87-91`
```

Why it matters: *Data & interfaces* is the statement the sealer and the
settle read the command against. `frame/design.md:92` says every other
exit prints a line that "names N, the SHA and the outcome", and the SHA it
defines at `:70` is HEAD. Found: under `--once`, `main` prints the pull
request's `headRefOid` (`pr_wait.py:344-345`, `:373`). An exit 2 raised
before any read names no commit (`pr_wait.py:379`; the cases at
`test_pr_wait.py:498-501` and `:525-529` pin both lines). Phase 1 made both
choices and recorded them (`trail/phases/phase-1.md:87-91`). The fold at
`035bd8ad0` that brought the design up to phase 1 left this sentence as it
was. The docstring at `pr_wait.py:87-88` already says it right: "the
commit where one was read".

```markdown
**What it prints.** An argument `argparse` refuses prints its usage error on stderr at exit 2. Every other exit prints one line on stdout that opens `seal pr-wait:` and names N, the commit where one was read (HEAD for the wait, the pull request's head under `--once`, none where an exit 2 came before any read), and the outcome. Exit 1 adds a line for each check in `fail` or `cancel`, and exit 2 adds the `gh` or `git` command and its stderr. The crafter writes each line's words, and a case pins each (contract rule 14).
```

## Confirmations

What matched: the paragraph at `skills/code-review/orchestration.md:266-286`
against the two paragraphs it replaced, at
`release/v0.38.0:skills/code-review/orchestration.md:266-313` (read, both
whole). This answers the closing memo's third row. Each act has a row:

- The read when the pull request opens, before each push and after each
  push becomes `--once` before a push and the wait at the opening and after
  a push (`:266-268`).
- "Waits on CI only under `OPEN` and `MERGEABLE`" is now the command's job
  (`pr_wait.py:314-325`).
- `MERGED` stops the push, and the repair goes on a new branch cut from the
  base (row 4, `:284`).
- `CLOSED` pushes nothing, and the report says a repair is pending (row 5,
  `:285`).
- `CONFLICTING` leads to the merge of the base (row 6, `:286`), and the old
  text left that act to the next paragraph too.
- The reason the wait reads every workflow's checks is kept (`:270-272`).
- Past the limit, the report names the SHA, the wait goes no longer, and
  the pull request is not treated as checked (row 3, `:283`).

The reasons the old text gave for `MERGED` and `CONFLICTING` left with it,
as *Scope* item 4 ("Nothing else of the two paragraphs stays") and phase
2's fourth decision state. The acts do not rest on them. The one act that
changed is the report under `UNKNOWN`, which is finding 2.

What matched: each exception path in `pr_wait.py` ends at exit 2.
`Unanswered` is raised for a missing `gh`, a timeout, an `OSError`, a
non-zero exit, a non-JSON answer and each value guard, and `main` catches
it (`:377-378`). No path was found that raises anything else past `main`
(read `:161-345`). That matters because Python's own exit on an uncaught
exception is 1, which row 1 reads as a failed check.

What matched: scenarios S1 to S9 each have a case, and the module's 29
cases pass (executed, `bin/test -q tests/skills/test_pr_wait.py`, exit 0).
The cases for S6 and S7 serve what G10 and G7 describe and fail on the exit
code where their guard is gone, as the phase 1 table at
`trail/phases/phase-1.md:26-45` claims. That was read and not re-run.

What matched: the registration in `skills/implement/scripts/seal.py:169-172`,
its pair at `tests/skills/test_seal.py:3651`, its `SHIPPED` row and the
`VERSIONS_OF_ANOTHER_PRODUCT` row. Executed, `bin/test -q
tests/text/test_the_rules_have_one_owner.py
tests/behaviour/test_a_reference_root_is_read_and_never_taken.py
tests/behaviour/test_release_hygiene.py
tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`:
107 passed, 8 skipped, exit 0. Executed, `bin/test -q
tests/skills/test_seal.py -k accepts_each_tool`: 14 passed.

What matched: the tree keeps no other statement of the old wait. Executed,
`git grep -n` for `--watch`, `headRefOid`, `state,mergeable`, `pr checks`,
`pr-wait` and `pr_wait`, and case-blind for `wait on CI`, `waits on CI`,
`checks reported` and `no check of a`, outside `seal/threads/`. The only
hits are the new paragraph, the registration, the pin and its docstring,
and one unrelated `--watch=false` in `tests/skills/test_session_cost.py`.
G18's reading holds: `skills/verify/scripts/session_cost.py:143-158` gives
no family a line opening with `seal` (read).

What matched: each new case in `tests/skills/test_pr_wait.py`, read against
its group. The file is new, so its group is its own cases and the pairs
`seal layout --pairs` prints. The report printed 48 pairs, every one two
cases of a class that call `gh` or `wait` with equal arguments while the hub
serves them different answers. None is a duplicate (executed, exit 0).
Phase 1 claimed 39 pairs (`trail/phases/phase-1.md:126`). The report gives
48 at `be4b321da`, and the file has not changed since `e9c45b77d`. The claim
that none is a duplicate holds, and the count is not one this round could
reproduce.

What matched: each quote of `pr.md` stands word for word at its coordinate,
`frame/plan.md:48`, `:49`, `frame/questions.md:20` and `frame/plan.md:56`
(read). `gaps.md` is new in this range, so no row of it left the memo. Its
first row labels the broad gate `unverified`, with the orchestrator as its
answerer, and the label is honest: no phase record claims the whole suite.

Two readings the build made that no case holds and the frame does not
state. An empty `gh run list` counts as every run completed
(`pr_wait.py:283`). Each `gh` call is bounded at 60 seconds
(`pr_wait.py:127`, `:173-178`). Phase 1 discloses both at
`trail/phases/phase-1.md:74-86`. Neither holds a fact of *Scope* or of an
acceptance row, so this round opens no finding for them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The command against a real pull request: whether it exits 0 only after the jobs that `needs:` another have finished, and how long the first `pull_request` check takes to be listed after a push; G9 to G12 are carried from the frame, not re-measured | `frame/questions.md` Q1 | the orchestrator, at this pull request's first `seal pr-wait` run |
| Whether `gh pr checks --json event` prints an empty event on GitHub Enterprise Server | `frame/questions.md` Q2 | whoever runs the plugin against an Enterprise Server |
| What the orchestrator does at exit 2 from `--once` before a push: push, retry, or stop. Row 2 says only that nothing about the pull request is known, and the paragraphs it replaced did not say either | `skills/code-review/orchestration.md:282` | the orchestrator, or the owner where it judges the row should say |
| `tests/skills/test_pr_wait.py` on Linux, Windows, Python 3.12 and 3.14, the `gh.cmd` stub among it | `gaps.md:8` | the pull request's `tests` workflow |
| The whole suite, the repository-wide lint and the format check at HEAD | `gaps.md:7` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/skills/test_pr_wait.py` in the round's clone at `be4b321da` | 29 passed, exit 0 |
| The same, with `pr_wait.py:216`, `:241` and `:246-248` each replaced by `if False:` | 29 passed, exit 0: no case holds the three guards (finding 3); the file was restored with `git checkout` |
| `bin/test -q -p no:xdist tests/skills/test_tmp_round1_probe.py`, first run | 2 errors at collection: the `clock` fixture was not imported, so nothing ran |
| The same, with `clock` imported | 2 passed, exit 0: a head that moves after the start runs to the fake clock's one-hour guard (finding 1), and `UNKNOWN` with a rollup of three checks exits 3 with "no check of a pull_request run was listed on" and no `gh pr checks` call (finding 2) |
| `bin/test -q` on the pin, the `SHIPPED`, release hygiene and script-reach modules | 107 passed, 8 skipped, exit 0 |
| `bin/test -q tests/skills/test_seal.py -k accepts_each_tool` | 14 passed, exit 0 |
| `bin/seal layout --pairs tests/skills/test_pr_wait.py` | 48 pairs, exit 0 |
