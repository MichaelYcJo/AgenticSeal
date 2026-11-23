# Review round 2: 1795439973-six-test-modules-cost-past-the-rewrite-bound

```seal
target: fdcb54064, fixes 283f33baf..fdcb54064
```

This is a verifying round. Its target is the diff of the fold and the fix
pass that answered round 1: `b1eebbe2b` (the fold of *Scope* item 11, plan
row 9, Q2, the orchestrator's grounds cell of the run-45244493975 row and a
new *Judgments of the run* row), `9b1bbc499` (`changelog.md`, `gaps.md` and
part 4 of `trail/phases/phase-9.md`) and `fdcb54064` (the two close blocks).
The range changes no test file and no shipped file (executed:
`git diff --stat 283f33baf fdcb54064 -- tests skills lib bin hooks .github`
printed nothing). So no case was run again, and nothing round 1 executed
over the six modules is re-derived here.

Read whole at `fdcb54064`: `routing.md`, `frame/design.md`,
`frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and
`pr.md`, and `trail/phases/phase-9.md`, the one phase record the range
changes. No `pr.<lang>.md` stands, and none is owed, since
`seal/config.json` names English for both language keys. No
`seal/parity.json` is declared.

Carried from round 1 as coordinates, and opened again here:
`tests/skills/test_settle.py:697-711` (`at`), `:163` (`dry_run`), and the
base's `git`, `commit`, `repo`, `settled_repo` and `local` at
`ef776317b:tests/skills/test_settle.py:84`, `:99`, `:110`, `:379`, `:512`;
`tests/skills/test_chain_check.py:466-488` (`answered`). Carried as round
1's own and not re-run, because no test or shipped file changed after its
target: the assertion comparison of the six modules, the mutation tables
of the two gates' modules, the read-only probe over the three templates
and the narrow runs.

The round's main check was the fix pass's new part 4 rows. A script
listed every row of part 4 whose verdict opens with "Answered" and printed
the source of the test function each names (executed: `show_cases.py` in
this round's scratch). It found 32 rows, the count the close names. Each
row was read against its function's assertions at `fdcb54064`. Findings 1
and 2 come from that reading and from reading the fold against item 11.

## Findings

### 1. Two restatements of *Scope* item 11's verdicts disagree with item 11 and with phase 9's own rows

```seal
severity: should
location: `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:94`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/frame/plan.md:69`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/frame/design.md:131`
evidence: read `frame/design.md:131`, `frame/plan.md:45`, `frame/plan.md:69`, `trail/phases/phase-9.md:27`, `:90`, `:94`, `:126`, `:135`, `:139`, `:140`, `:144`, `:147`, `:180`, `tests/skills/test_chain_check.py:4645`, `:5067`, `skills/code-review/scripts/chain_check.py:2177-2180`
regression: round-1#2
```

Why it matters: round 1's second finding was that the record of the stop
judgment named two kinds of verdict where phase 9 had used three. The fix
added the third kind to item 11, then restated it in two other places. Each
restatement says something different from item 11. A sealer who checks the
stop judgment's grounds against the record will find the same kind of gap
round 1 found.

The unit is the legend of part 4 at `trail/phases/phase-9.md:94`, written by
`9b1bbc499`, and the grounds cell at `frame/plan.md:69`, written by
`b1eebbe2b`. Round 1's fix said to fold the third kind into item 11 and to
make the record name each case's fact. The fold put the `answered` run
second in item 11. The two restatements then described it from round 1's
wording of "a third kind", not from item 11 as folded.

- **Claimed** at `phase-9.md:94`: "'Answered' is *Scope* item 11's third
  verdict". **Found**: `frame/design.md:131` lists the unit call first,
  the `main` run with `answered` second ("Or, where its fact is what `main`
  does with an arm's answer ..."), and the real-git case third. Plan row 9's
  *Verified by* (`frame/plan.md:45`) uses the same order. A reader who opens
  item 11 to see what "Answered" means finds the real-git case there. Part 4
  calls that case "Kept".
- **Claimed** at `plan.md:69`, in the grounds: the third verdict is "a
  `main` run with `read_record`, `tracked_files` and `follows` answered and
  the rest of `main`'s git real, whose fact is what `main` does with an
  arm's answer". **Found**: 7 of the 32 answered rows name the root's entry
  as their fact (`phase-9.md:126`, `:135`, `:139`, `:140`, `:144`, `:147`,
  `:180`). That is not an arm's answer: `_checked` decides it inline
  (`chain_check.py:2177-2180`), and item 11 gives those cases a sentence of
  their own. Two answered runs also keep `follows` real
  (`tests/skills/test_chain_check.py:4645`, `:5067`), as `phase-9.md:27` and
  `:90` record. So 9 of the 32 rows match no verdict the grounds cell lists.
- **The source itself.** Item 11 says the answered run keeps "its `main` run
  with `answered` replacing `read_record`, `tracked_files` and `follows`".
  It does not say that a reader the refusal rests on may stay real. The two
  `follows` cases are recorded only in the phase record it cites. Once the
  two restatements cite item 11 and stop restating it, item 11 is the one
  source, so it has to state that exception too.

`skills/core/SKILL.md` *The rule a mechanism is kept against*: "A fact has
one source, and every other place links to it." The fix makes item 11 that
source and has the other two cite it. Nothing else restates the verdicts:
`changelog.md:15` describes them in general terms and in item 11's order,
and `gaps.md:61` and `frame/questions.md` Q2 state only that item 11 keeps
such a run.

The sentence in item 11 at `frame/design.md:131`, which the framer's fold
owns:

```markdown
Or, where its fact is what `main` does with an arm's answer, such as the exit on a ready or a draft pull request, `--sealing`'s exit or a notice, it keeps its `main` run with `answered` replacing `read_record`, `tracked_files` and `follows`, a reader its refusal rests on kept real (`answered`'s `real`), the rest of the git `main` starts stays real, and the record names the fact of `main` it holds (`trail/phases/phase-9.md` *Departures from the frame*).
```

The legend's sentence at `trail/phases/phase-9.md:94`, which the crafter
owns:

```markdown
"Answered" is a case *Scope* item 11 keeps as a `main` run with `answered`, and its line names the fact of `main` the case holds, or, for the cases of the root's entry, that entry.
```

The sentence in the grounds cell at `frame/plan.md:69`, which the
orchestrator owns:

```markdown
Phase 9 gave each listed case one of the three verdicts *Scope* item 11 names, as folded after round 1, so the cases that stay are each named with the reason they stay;
```

### 2. Three rows the fix pass wrote name more than their case asserts

```seal
severity: should
location: `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:98`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:121`, `seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md:122`
evidence: executed `python3 -I show_cases.py tests/skills/test_chain_check.py trail/phases/phase-9.md`, which printed 32 rows, each with its function's source; read `tests/skills/test_chain_check.py:1843-1875`, `:3382-3384`, `:3465-3482`, `:4037-4072`
regression: round-1#2
```

Why it matters: the close of round 1's second finding says each of the 32
rows was "written from that case's assertions at HEAD". The legend says
each line names the fact the case holds. The stop judgment's grounds rest
on the record saying what each kept case holds. A reader who takes one of
these lines as held will not add the case that would hold it. Three lines
state more than the case asserts, and the extra words in each come from
the case's docstring, not from its assertions.

The unit is the 32 rows `9b1bbc499` rewrote. Round 1's fix said to write
each row "from each case's assertions". For these three, the fix copied
the docstring.

- **Claimed** at `phase-9.md:98`: the second run "exits 1 naming the
  release's own work item's missing files". **Found**: the case asserts one
  file, `f"{own}/trail/gate.md" in out`
  (`tests/skills/test_chain_check.py:1870`).
- **Claimed** at `phase-9.md:121`: `main` exits 1 "with the body arm's one
  refusal at the work item's directory, and refuses nothing else".
  **Found**: the case asserts exit 1 and `body_lines(out) == [...]`
  (`:3465-3482`). `body_lines` keeps only the lines that hold "the pull
  request's body" (`:3382-3384`), so a refusal from any other arm leaves
  the case green. "Nothing else is refused" stands in the docstring
  (`:3471`) and in no assertion.
- **Claimed** at `phase-9.md:122`: `main` "exits 0 on a draft with the same
  lines". **Found**: the draft run asserts exit 0 and the undeclared-trailer
  line alone (`:4069-4071`). The `no work item` line is asserted only on the
  ready run (`:4057`). "A draft prints the same lines" stands in the
  docstring (`:4043`).

The other 29 rows say what their case asserts. The list is whole: the
script printed every "Answered" row and the source of each function, and
each was read.

```markdown
| `Test_rule_changes_read::test_accepts_a_spec_another_pull_requests_squash_carried_unread` | 104 | 41 | Answered, its three runs: `main` leaves the design another pull request's squash carried unread and exits 0 on the release pull request, exits 1 naming the release's own work item's `trail/gate.md`, and reads the same design on the head branch's own pull request. `carried_by` and the squash stay git's (part 3). One commit of both specs replaces three commits and a round. |
```

```markdown
| `Test_body::test_refuses_a_body_sent_before_the_seal_at_the_mark` | 54 | 26 | Answered, over the template: `main` exits 1 on a ready pull request, and the body arm prints one line, its refusal at the work item's directory. |
```

```markdown
| `Test_routing_trailers::test_refuses_a_commit_naming_a_work_item_no_declaration_names` | 40 | 36 | Answered, its two runs: `main` exits 1 on a ready pull request naming the commit whose trailer names an undeclared work item, prints the one reading `no work item` as a notice, and exits 0 on a draft still naming the first commit. The trailers stay git's. |
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `changelog.md:20` now says that `at` runs `survey` at a ref and
then `report`, or `apply` under `--apply`, and that a `--draft` case runs
`settle.main`. `changelog.md:30` names `git` and `commit` as helpers,
`settled_repo` as a builder and `repo` and `local` as fixtures. Read
against `tests/skills/test_settle.py:697-711`, where `at` calls
`settle.apply` or `settle.report`; `:163`, where `dry_run` calls
`settle.main`, which the `--draft` cases at `:3910`, `:3952` and `:3967`
use; and the base at `ef776317b`, where only `repo` (`:110`) and `local`
(`:512`) carry `@pytest.fixture`. No other line of `changelog.md` names
`at` or the five helpers (read).

```seal
confirms: round-1#2
```
What holds: the defect round 1 named is gone. Item 11
(`frame/design.md:131`) now names the `main` run with `answered` as a
verdict and gives the cases of the root's entry their own sentence. The
coordinate it cites, `chain_check.py:2177-2180`, is the inline `gone`
decision inside `_checked`, which starts at `:2128` (read). Plan row 9's
*Verified by* (`frame/plan.md:45`) and Q2 (`frame/questions.md:15`) follow
item 11. `changelog.md:15` gives three verdicts. `gaps.md:61` no longer
says that item 11 keeps the readers' agreement with git, and says those
readers are held by their own classes and by the runs with every reader
real. Each of the 32 "Answered" rows of part 4, the 11 round 1 named among
them, now names a fact of `main` or the root's entry, and 29 of them say
what their case asserts (executed: `show_cases.py`; read: each function's
source). The two stray closing tags at the end of `phase-9.md` are gone
(read: the diff). Findings 1 and 2 are new defects in the units this fix
wrote, so this close holds beside them.

What matched: `pr.md` is unchanged in the range. Each of its five quotes
stands word for word in `frame/plan.md`, runs of whitespace collapsed
(executed: a comparison of each quote against the file). The quote of the
run-45244493975 row is that row's judgment cell, which the fold left as it
was.

What matched: `gaps.md` loses no row in the range. Its only change is the
paragraph at `:61`, and `## Not verified` is untouched (read: the diff).

What matched: the new row at `frame/plan.md:73` says what the range did.
Item 11 was amended, the grounds cell of the run-45244493975 row was
rewritten, and `9b1bbc499` gave the 11 rows their facts and corrected
`changelog.md` and `gaps.md` (read: the diff). The fix pass also rewrote
the 21 other answered rows, which the row does not mention; that leaves out
work and claims none.

One sentence that is no finding: the *Removes* row the fold rewrote
(`frame/design.md:178`) names items 6, 7, 11, 12 and 13 for a command run
with readers answered and leaves out item 10. Cases of
`tests/skills/test_settle.py` run `settle.main` under `answered`, and
items 10 and 13 both govern them. Item 13 is listed, and leaving out item
10 changes no case or reader the row names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target. The suite stands `unverified`. | the repository | the orchestrator, once the rounds settle |
| Each module's Windows figure after the rounds, and *Done when* on the first push run on `main` after the release | `frame/questions.md` Q3 and Q4 | the orchestrator for Q3, the repository owner for Q4 |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 283f33baf fdcb54064 -- tests skills lib bin hooks .github` | printed nothing: the range changes no test and no shipped file |
| `python3 -I show_cases.py tests/skills/test_chain_check.py seal/threads/1795439973-six-test-modules-cost-past-the-rewrite-bound/trail/phases/phase-9.md`, in this round's scratch | `ROWS: 32`, no function not found, each row printed with the source of the function it names |
| a comparison of each quote of `pr.md` against `frame/plan.md`, whitespace collapsed | all five found |
| an `ast` walk over `tests/skills/test_settle.py` for cases that call `answered` and run `dry_run` or `main` | 23 cases, the basis of the sentence on the *Removes* row |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6 --root <the branch worktree> --worktree`, with this record in place | exit 0; it refuses this record's two findings as open, which the fix pass closes, and names the missing `trail/gate.md` and `guarantee.md`; no notice at a line of `frame/design.md` |
