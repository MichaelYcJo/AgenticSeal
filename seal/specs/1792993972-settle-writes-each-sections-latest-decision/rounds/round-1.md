# Review round 1: 1792993972-settle-writes-each-sections-latest-decision

target: a82541df against release/v0.22.4

Round 1 has no earlier record, so nothing is carried. Every fact below was
established this round in a `git clone --no-local` of the repository at
`a82541df`, against the fork point `2974871d`.

## Findings

### 1. The branch turns the suite red: `.test_durations` now prices 96 cases the suite no longer collects

severity: must
location: `.test_durations`, `seal/specs/1792993972-settle-writes-each-sections-latest-decision/overview.md:36-38`
evidence: executed `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite`, `gh run view 40282308738 --log-failed`
verdict: open

The `tests` workflow run 40282308738 at `a82541df` concluded `failure`.
Three legs failed (ubuntu, macos group 3, windows group 4), each on the one
case `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite`:
"99.4 s of the file's 1,301.1 s (7.6%) belong to 96 entries the suite no
longer collects ... over the 5% STALE_SHARE allows". The first entries it
names are this branch's retired `Test_retired` cases of
`tests/test_chain_check.py`. The same case passes at `2974871d` and fails
at `a82541df` in the clone, so the branch's removals cross the threshold.

The implementer's account claimed the stale entries are not this branch's
to touch: `overview.md` *Not done* says the file "is the durations CI
unions after a run, not a list kept by hand". The case this branch turned
red says the opposite, and its message gives the refresh: the branch's own
`tests` run produced the `test-durations` artifact, and the committed file
is replaced from it. A pull request opened at this head fails its required
`tests` job.

```sh
gh run download 40282308738 -n test-durations -D <dir>
mv <dir>/.test_durations .test_durations   # LF line ends already; commit it
```

The `overview.md` *Not done* paragraph on `.test_durations` goes in the same
commit, since the claim it makes no longer holds.

answer:

### 2. Applied to `docs/`, two of the rule changes collide with text this branch wrote, the class #952 met

severity: should
location: `README.md:262`, `skills/settle/SKILL.md:175-181`, `tests/test_settle_reads_before_it_removes.py:103`
evidence: executed `bin/test $(git grep -l -e the-record-layout -e release-checklist -e the-review-and-parity-arms -e the-review-record -- tests/ | grep -E '^tests/test_[^/]*[.]py$') tests/test_docs_line_wrap.py tests/test_rules.py tests/test_settle.py tests/test_rule_changes.py -q`
verdict: open

The probe applied this spec's eight `## Rule changes` operations, as written,
to the clone's four documents, then ran the 49 modules that read them. Three
cases fail, and two of the three come from text this branch wrote beside its
own `to` values:

- `tests/test_no_passage_is_pasted_into_a_second_file.py` (two cases):
  `README.md` and `docs/release-checklist.md` share the 15-word run "writes
  each section as its group's latest decision, checked against the code, and
  closes each". The README row at `README.md:262` restates operation 5's `to`.
- The same check: `docs/the-record-layout.md` and `skills/settle/SKILL.md`
  share "decision, the code is the later fact and the section states what the
  code does." Step 2 of the skill's procedure restates operation 3's `to`.
- `tests/test_settle_reads_before_it_removes.py::test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule`
  pins "it is retired by that rule, with no marker", the sentence operation 2
  retires. Its docstring says the sentences change at the settle, and
  `questions.md` A9 puts this pin on the settle. That one is the frame's
  design and no finding.

`questions.md` A3 moves #952's class into the settle's own edits, and the
settle can reword a section. These two copies are not the settle's to
create: this branch wrote both sides now, and the rule of one fact in one
place (`CLAUDE.md` *The rule a mechanism is kept against*) applies to them
today. Left as they stand, the 0.22.4 settle meets them as a red broad gate,
which step 8 runs once.

Rewrite each copy to point at its home rather than repeat it.

```markdown
<!-- README.md:262, the sentence after "It refuses nothing." -->
The session running the settle then writes the sections and decides the open rows, asking nobody (`skills/settle/SKILL.md` *The settling session's procedure*).
```

```markdown
<!-- skills/settle/SKILL.md, step 2 -->
2. For each group, read every operation in merge order, the section as it
   stands, and the code the rule names, its `check:` targets first. Write
   the section as the latest decision states it, in your own words. Where
   the code has moved past that decision, write what the code does. An
   earlier operation the latest one restates is superseded: it is settled
   with its group and not applied. The rest of the document stays as it
   was, and no marker is written.
```

The pin `tests/test_settle_reads_before_it_removes.py:103` holds step 2's
sentence ("the code is the later fact and the section states what the code
does"), so that line changes to the new wording in the same commit.

answer:

### 3. A sentence of the policy root still says `settle --apply` applies the spec's rule changes, and no rule change rewrites it

severity: should
location: `seal/specs/1792993972-settle-writes-each-sections-latest-decision/spec.md:199-354`, `docs/the-record-layout.md:242-250`
evidence: executed `grep -n 'section: seal/specs' seal/specs/1792993972-settle-writes-each-sections-latest-decision/spec.md`, `git grep -n -i -E 'settle[^.]{0,40}appl' -- docs/`
verdict: open

`docs/the-record-layout.md` *seal/specs/<work-item-id>/* says the files
"stay until `settle --apply` applies the spec's rule changes, and then the
directory goes whole". After this branch `--apply` writes no document
(`skills/settle/scripts/settle.py:566-604`), and a directory goes once its
record holds no open row. The spec's eight operations name four sections,
and none is that one (the grep returns nothing). `spec.md` *Out* argues the
loose sentences of `docs/one-root-by-lifetime.md` still hold, since "the
settle" there names the act. This sentence names the command, so it is false
once the branch merges. Contract rule 19 asks that every sentence stating the
old fact change with it, and the policy root changes only through
`## Rule changes`.

```markdown
- change
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  from: stay until `settle --apply` applies the spec's rule changes,
    and then the directory goes whole
  to: stay until the settle: the settling session writes the spec's
    sections, and `settle --apply` removes the directory whole once its
    record holds no open row
```

Add it to `spec.md` `## Rule changes` and re-run `rule_changes.py#parse`
over the file (S12).

answer:

### 4. The deletion message still says a renamed directory reads as a deletion; it now reads as a settle

severity: should
location: `skills/verify/scripts/unverified_check.py:1670-1674`, `tests/test_unverified_check.py:2293-2306`
evidence: read `skills/verify/scripts/unverified_check.py:1594-1600`, `skills/verify/scripts/unverified_check.py:1641-1674`, `tests/test_unverified_check.py:1978-1997`
verdict: open

The error `unverified-check --baseline` prints for a removed `overview.md`
ends "a renamed directory reads the same way, and says so out loud rather
than dropping the rows". Since this branch a renamed directory is gone whole
from its old path, so `settled` names it settled (the case
`test_refuses_a_record_that_left_whole[a file and a rename]` asserts exactly
that). The message now reaches only a memo removed from a directory that
stays, and its rename clause tells a person the opposite of what the tool
does.

The implementer's account claimed "its rows are read where it went"
(`phases/phase-2.md`). The rows at the new path are listed, but they are
never counted against the old path: `base_text` is None for a path the base
never held, and the loop continues (`unverified_check.py:1597-1599`). So a
rename that also drops rows passes. That is inside the limit the frame wrote
for a whole removal outside a settle (`spec.md` operation 1's `to`), since
deleting the directory outright drops every row too, and so it is no gate
finding. The message is.

```python
                deleted.append(
                    annotate(
                        "error",
                        display_path(os.path.join(root, rel), cwd),
                        1,
                        f"present at {named} and not here. Whatever it "
                        "recorded as unverified left with it, and its "
                        "directory still stands, so this is no settle",
                    )
                )
```

Contract rule 14: `test_refuses_a_removal_no_settle_explains`
(`tests/test_unverified_check.py:2293`), whose memo removals are the shape
that still reaches this message, pins the new words.

answer:

### 5. The settling session's procedure leaves two decisions with two readings

severity: should
location: `skills/settle/SKILL.md:184-203`, `tests/test_settle_reads_before_it_removes.py:108`
evidence: executed `grep -n -i -E 'first (row|kind) that|in that order|before the others|wins' skills/settle/SKILL.md`, `grep -n -E 'test_docs_line_wrap|no_passage|line_wrap|passage' skills/settle/SKILL.md`
verdict: open

`CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*
asks each instruction to name who acts, when, on which file and what counts
as done. Two steps fall short, and both searches return nothing.

- Step 4's table gives each row kind a `When`, and a row can meet two of
  them: a Windows run of a hook the tree no longer holds is both moot and a
  measurement nobody has taken. One reading closes it, the other opens an
  issue. The table states no order.
- Step 6 says "Run the repository's checks over what you wrote" and names
  no set and no done condition. The checks that catch #952's class read
  every document rather than one by name (finding 2's probe met the passage
  check that way). A session that reads "the `check:` targets" as the set
  finds the rest at step 8, which runs once.

```markdown
   | The row is | When | What closes it |
   |---|---|---|
   | moot | it names a unit the tree no longer holds | the coordinate showing the unit gone |
   | answered | another record or a later run already answered it | that record or run, named |
   | a measurement nobody has taken | it names a run, a platform or a reading no record holds | the issue it is re-homed to |

   A row that fits more than one kind takes the first that fits, in the
   table's order.
```

```markdown
6. Run, over what you wrote, each rule's `check:` targets and every check of
   the repository that reads the whole policy root (a line-length, a
   duplicated-passage or an edition check, where the repository has one),
   then the dry run again: a `to` not found is where you reworded, which the
   body explains. The step is done when each of those passes. Change whatever
   the written sections leave standing on an old fact, such as a pin under
   `tests/` or a README copy, and name each in the pull request body.
```

The pin `tests/test_settle_reads_before_it_removes.py:108` holds step 6's
opening words, so it changes with the step.

answer:

## Confirmations

confirms: none
The predicate does not let a pull request escape a declaration of its own.
`chain_check.py#retired` passes `settled` only declarations gone from HEAD,
and `settled` asks whether the directory held a file at the merge base
(`skills/verify/scripts/unverified_check.py:1266-1279`). A work item's own
directory was added on the branch, so it fails that question and its
removed declaration stays refused. A whole removal of a sibling's directory
reads as a settle, and the frame wrote that limit into the rule (`spec.md`
operation 1's `to`, `plan.md` *Alternatives considered*). Such a directory
is not the work the pull request's work item owns, which is where
`CLAUDE.md` *The rule a mechanism is kept against* puts a gate. A rename
adds nothing a whole deletion cannot already do (finding 4). Read.

confirms: none
S10 holds: the dry run over the real `origin/main` (`67694cba`) prints 41
released work items, 6 stating rule changes, 48 groups and 62 open rows in
41 records. It refuses nothing, and the two `from` values not found are
`1792619408` `spec.md:196` and `1792627930` `spec.md:279`, as
`phases/phase-1.md` records. Executed.

confirms: none
The eight `## Rule changes` operations parse (S12) and place against the
policy in force. Six `from` values are in `docs/` at `a82541df`. Operations 2
and 3 quote the fold section as `1792628098`'s unsettled check-line changes
leave it (`seal/specs/1792628098-tests-rebuilt-one-file-per-module/spec.md:503-512`),
and each ends on that spec's `to`. Executed with the dry run at
`--released-at HEAD`, read for the two.

confirms: none
Every item of `## Removes` is gone with its cases: `replay`, `conflicts`,
`apply_op`, `_cut`, `rule_plan`, `rule_arm`, the base headings and
`NO_BASE_SAYS`, `wrote_a_spec`, `policy_documents`, and each case name the
table lists. The only hit, `tests/test_chain_check.py`'s
`test_every_reader_of_a_retirement_calls_the_one_predicate`, is that
module's own case, rewritten for two readers. Executed with `git grep` over
the tree outside `seal/specs/`.

confirms: none
The divergences in `overview.md` hold. `_ancestor` stays because S5's
`unordered` mark needs ancestry, and `spec.md` *Data & interfaces*
contradicted S5. S8 could not pass unchanged: its named cases removed
directories whole, which *In* item 4 makes a settle, and each rewritten case
keeps a partial removal as a deletion (`tests/test_unverified_check.py:2293-2306`,
`tests/test_chain_check.py:3392-3401`). `policy_documents` and `SPEC` had no
reader left. The dry run listing every released directory is what makes the
citations print on a corpus where every record holds a row. Read.

confirms: none
The touched modules pass: `bin/test` over `tests/test_settle.py`,
`tests/test_rule_changes.py`, `tests/test_settle_reads_before_it_removes.py`,
`tests/test_unverified_check.py`, `tests/test_chain_check.py`,
`tests/test_the_retired_rules_await_their_settle.py` and
`tests/test_settle_applies_rule_changes_in_place.py`, 711 passed.
`test-layout --pairs` over the five changed test files names no pair.
Executed.

confirms: none
The Windows legs ran every case. Groups 1 to 3 of the Windows leg passed, and
group 4 failed only on the durations case of finding 1, which fails the same
way on ubuntu and macos. The one added git read, `settle.py#tracked_names`,
reads `ls-files -z` as bytes, and no added case writes a subprocess's stdin.
So the `overview.md` *Not verified* row naming the Windows legs has its
answer in run 40282308738. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the 0.22.4 settle runs the tree's `settle.py` and reads the tree's `skills/settle/SKILL.md`. The installed 0.22.3 plugin holds the literal replay, so its `bin/settle --apply` would write `docs/`, and its skill states the old procedure | `plan.md` *Operational impact* | the orchestrator, at the release preparation |
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three, and CI's run is red on finding 1 | `broad-gate.md` | the orchestrator, by `broad-gate` once the rounds settle |
| The pull request body's failure direction, prompt budget and removals, and the `Part of #1033` line of Q2's default | `CONTRIBUTING.md` *What a change to a gate must carry* | the orchestrator, when the body is written |
| Q1's default, one issue per distinct measurement, against how the owner wants the tracker to read | `questions.md` Q1 | the repository owner, at the settle's pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` at `a82541df`, then at `2974871d` | head: 1 failed, "99.4 s of the file's 1,301.1 s (7.6%) belong to 96 entries"; base: 1 passed |
| the eight operations applied by `Edit` to the clone's `docs/the-record-layout.md`, `docs/release-checklist.md`, `docs/the-review-and-parity-arms.md` and `docs/the-review-record.md`, then `bin/test` over the 49 modules that name those documents | 3 failed, 1699 passed, 10 skipped: two passage cases and the spec-less pin; the documents restored afterwards |
| `python3 skills/settle/scripts/settle.py --released-at gh/main`, `gh/main` fetched as the real `origin/main` at `67694cba` | exit 0; 41 released, 6 with rule changes, 48 groups, 62 open rows in 41 records |
| `python3 skills/settle/scripts/settle.py --released-at HEAD` | exit 0; this spec's eight operations in groups 8, 11, 26 and 50, operations 2 and 3 with `from` not found |
| `bin/test-layout --pairs` over the five changed test files | 5 files read, 0 pairs |
