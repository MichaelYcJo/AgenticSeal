# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 8

target: d5c83efd, fixes 9f293cb0..d5c83efd

Extended past round 7: round 7 found 5, round 6 found 1, and none is a regression.

A verifying round over round 7's fix pass (a6075755 to 6a40c790), the
framer's edit that hands part B to #957 (4da731fc) and the text cleanup
(c98acabf, 399ea88b, d5c83efd). Four of round 7's five fixes hold and are
confirmed below. The fifth, round 7's finding 3, holds for a rejection that
stands and not for one that does not, which is finding 2. The split, the
cleanup and the new statement of what a `regression:` line marks hold where
they were aimed, apart from findings 1 and 3.

Three findings follow, in cause order. Finding 1 is a gap in the channel
between rounds that phase 5d-iii built: when a verifying round finds that an
earlier close does not hold and no fix pass's commit made the defect, the
record has no line the round may write and the check accepts. Finding 2 is
the sentence round 7's fix for finding 3 wrote over that gap. It says the
run ends at the round that names a rejection on a `regression:` line, while
a round carrying that line goes back to its framer. It stands in the
paragraph 46cd674a wrote, so it names round-7#3, and by
`docs/the-review-record.md` §*The run* this round then gets no fix pass.
Finding 3 is the frame still stating the truth graders' old shape after
round 7's fix for finding 1 changed it.

Findings from reading and from execution are labelled in each finding and
confirmation, and every command named there is in `## Probes`. The full
suite was not run. It is `unverified`, and the sealer answers it.

## Findings

### 1. A verifying round that finds a rejection does not hold, or a fix that changed another unit, has no line it may write: the channel asks for a regression line, which the template gives only to a unit a fix pass's commits made, and which sends the item to its framer

severity: should
location: `templates/sdd-round.md:47-51`, `docs/the-review-record.md:248-259`, `agents/warden.md:119-123`, `agents/warden.md:212-217`, `skills/code-review/SKILL.md:187-191`, `skills/code-review/orchestration.md:96`
verdict: deferred the frame

Every finding round N closed `fixed <commit>` or `rejected` must be named in
round N+1. The warden's definition (`:119-123`, `:212-217`), the review
skill (`:187-191`) and the orchestration table (`:96`) all give two ways:
a `confirms:` line where the close holds, and a finding whose regression
line names it where it does not. Since a6075755 a regression is "a defect a
fix pass's own commit introduced", and the template gives the line "only on
a finding in a unit a fix pass's own commits added or changed".

Two closes that do not hold involve no such unit. One is a `rejected`
finding that holds after all, since a rejection makes no commit. The other
is a `fixed` commit that changed a file other than the one the defect
stands in. For either, the warden may not write a `confirms:` line, because
the close does not hold, and by the template may not write a `regression:`
line. With neither, `channel` refuses the earlier finding at its heading.
A warden that follows its own definition instead and writes the line
anyway sends the work item to its framer, since §*The run*
gives a round carrying that line no fix pass. That is the reframe the
owner's ruling of 2026-10-16 kept for a defect a fix pass made, spent on a
disagreement over a rejection. `skills/code-review/orchestration.md:113-120`
meets exactly this case, and finding 2 is what it says there.

Not a regression: the template's "only" and the four channel sentences stood
at 9f293cb0 in phase 5d-iii's wording ("a unit the fixes under review added
or changed"), which a rejection did not meet either. a6075755 narrowed the
wording and did not open the gap.

read: the six coordinates above at d5c83efd, and `templates/sdd-round.md`
and `docs/the-review-record.md` §*The run* at 9f293cb0. The paste below is
one way to close the gap that keeps the check unchanged. Whether a re-raised
rejection should stop the fix passes is a design choice, and the framer may
choose another.

`templates/sdd-round.md:47-51`, the `regression:` entry of the comment:

```markdown
  regression:  on a finding in a unit a fix pass's own commits added or
               changed: the earlier finding as `round-<N>#<n>`, or
               `round-<N>` for a fix pass no finding named. A round
               carrying one gets no fix pass. Also on a finding that raises
               an earlier `rejected` or `fixed` finding again where no fix
               pass's commit made the defect, naming it: that line stops
               nothing. A unit a build phase made is new work and takes
               none. Delete the line otherwise
```

`docs/the-review-record.md:248-259`, the paragraph, its `Enforced by:` line
kept:

```markdown
**A regression stops the fix passes, at any round.** A regression is a
defect a fix pass's own commit introduced. Where a finding stands in a unit
a fix pass's own commits added or changed, the warden writes its
`regression:` line, naming the finding whose fix made the unit as
`round-<N>#<n>`, or that round as `round-<N>` where no finding named the
unit, and names the unit first in the grounds. A defect in a unit a build
phase made, one the framer designed and the owner approved in `plan.md`, is
an ordinary finding of new work, with no `regression:` line, even where the
round that finds it reads that phase. A finding that raises an earlier
close again where no fix pass's commit made the defect, a `rejected`
finding that holds after all or a `fixed` one whose commit changed another
unit, names that finding on its `regression:` line, since the check reads
no other line for it, and says so first in its grounds; it is an ordinary
finding and stops nothing. A round carrying a `regression:` line on a unit
a fix pass's own commits made gets no fix pass: the work item goes back to
its framer, who writes `Reframed <date> by <who>, after round <N>.` under
the mark at the foot of `spec.md`.
```

answer: Deferred to the frame by the orchestrator: finding 2 carries a regression line, so this round gets no fix pass. The owner ruled on 2026-10-16 that both relations are needed now: a `regression:` line for a defect a fix pass's commit made, and a `reopens:` line for a close that does not hold; the frame takes findings 1 to 3 together.

### 2. The review skill says the run ends at the round that names a rejection on a regression line, but a round carrying that line goes back to its framer and the run goes on

severity: should
location: `skills/code-review/orchestration.md:113-120`
verdict: deferred the frame
regression: round-7#3

The unit: the paragraph 46cd674a wrote for round 7's finding 3, from
round 7's paste. Its last sentence gives the extra verifying round two ways
to name a rejected finding, a `confirms:` line, or "a finding's
regression line where the rejection does not hold" (quoted without its
code span), and ends "and the run ends at that round". The first way holds. The second does not.

§*The run* gives a round carrying a `regression:` line no fix pass and
sends the work item to its framer. The section right below the paragraph
(`skills/code-review/orchestration.md:122-135`) says the same: the record's
open findings close `deferred the frame`, the framer redraws, and the
redesign is built and reviewed. This item's own run went on past a reframe,
with round 7 after round 6's. And under finding 1's paste, where such a line
stops nothing, the finding that carries it reads `open` and owes a fix pass
and one more verifying round, so the run does not end there either. An
orchestrator that follows the sentence spawns the sealer over a last record
holding an `open` finding, and the ready pull request fails on it, which is
the failure round 7's finding 3 was raised to prevent.

read: `skills/code-review/orchestration.md:96-135` at d5c83efd, and its
diff over 9f293cb0..d5c83efd, where that clause, which names the
rejection on a finding's regression line, is 46cd674a's.

`skills/code-review/orchestration.md:113-120`:

```markdown
The condition is not *this round found nothing* — that would be unbounded, and
it was considered and rejected. A verifying round that raises a `should`
finding the smith closes `rejected`, with its grounds, has opened nothing
needing a fix, and it does not consume the cap. Its record is still not the
last one: the check refuses a `fixed` or `rejected` finding in the last
record, so one more verifying round reads that answer alone. Where the
rejection holds, that round names it on a `confirms:` line and the run ends
there. Where it does not, that round raises the finding again with a
`regression:` line naming it, and the run goes on as
`docs/the-review-record.md` §*The run* says for that line.
```

answer: Deferred to the frame by the orchestrator: finding 2 carries a regression line, so this round gets no fix pass. The owner ruled on 2026-10-16 that both relations are needed now: a `regression:` line for a defect a fix pass's commit made, and a `reopens:` line for a close that does not hold; the frame takes findings 1 to 3 together.

### 3. The frame still says a truth grader reads a finding's path and unit, after round 7's fix made every truth read a line window and refuse a unit

severity: should
location: `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:514-518`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:721-722`
verdict: deferred the frame

`spec.md` §*The proof harness, as this item leaves it* says "a `truth-`
grader reads a finding's `location:` line for the path and unit or line",
and §*Data & interfaces* says `truth_pattern` and `seed_defects.py` emit
`^location: .*<path and unit or lines>`. Since f5ba02f1 the tree does the
opposite. `truth_pattern` reads a line window, takes a unit's lines only to
place that window, and `test_a_truth_never_matches_a_coordinate_the_check_refuses`
holds that no truth matches `path#unit`. All twelve warden truths read a
line window. Neither `overview.md` nor `phases/phase-5d.md` records the
divergence, and the framer's edit at 4da731fc rewrote the paragraph above
these lines without them. The sealer reads the frame against the tree as
one party's story against another, so it meets a frame that promises the
shape the check refuses.

The same bullet's "Rule 3 reads shape graders on the new side only" now
points at a numbered list the split cut from §*The proof*. The rule stands
in `noninferiority.py#verdict`, which phase 1 built.

Not a regression: neither line is in a unit a fix pass's commits added or
changed, and the frame edit after the fix pass left them.

read: `spec.md:509-518` and `:719-724` at d5c83efd, `git grep` of
`unit or line`, `path and unit` and `line window` over the work item's
documents. executed: the twelve truth patterns read with `grep -n
"^pattern"` over the warden cases' graders, each a `path:` line window.

`spec.md:514-518`:

```markdown
  a `truth-` grader reads a finding's `location:` line for its path and a
  line within ±15 of the truth, a unit's lines placing that window where an
  old location named a unit, and never a `path#unit`, which the check
  refuses (`evals/scripts/behaviour.py`, `replay_targets.py#truth_pattern`,
  `seed_defects.py`), in place of the table row they read. The pass rule
  `noninferiority.py#verdict` numbers 3 reads shape graders on the new side
  only, since the old side's shape is the old record's by construction;
  `reach-` graders stay at 100 % on both sides.
```

`spec.md:721-722`:

```markdown
holds the record free of emoji; `replay_targets.py#truth_pattern` and
`seed_defects.py` emit `^location: .*<path>:<line window>`; the nine
```

answer: Deferred to the frame by the orchestrator: finding 2 carries a regression line, so this round gets no fix pass. The owner ruled on 2026-10-16 that both relations are needed now: a `regression:` line for a defect a fix pass's commit made, and a `reopens:` line for a close that does not hold; the frame takes findings 1 to 3 together.

## Confirmations

confirms: round-7#1
A `path#unit` coordinate is refused and no truth grader rewards it, at
`skills/code-review/scripts/chain_check.py:142-143`,
`evals/scripts/replay_targets.py:265-293` and `evals/scripts/rule_cases.py:280`.
executed: T33 and `test_a_truth_never_matches_a_coordinate_the_check_refuses`
pass at the target, and the second, new in the fix pass, fails against
9f293cb0's `replay_targets.py` (exit 1, the old pattern matching a
`a.py#f` location). The eight cases the fix regenerated come out byte for
byte the same from `replay_targets.py --case` and `seed_defects.py --case`
at the target, and `rule_cases.py` leaves the tree unchanged. All twelve
warden truth patterns read a line window and none holds a `#`. The check
reads the seven records with no location refused. read: `seed_defects.py`'s
docstring says a line window. This answers round 7's second row of
`## Not judged`

confirms: round-7#2
A finding heading with no number, or with a number an earlier heading
carries, is refused at the heading before its labels are read, at
`skills/code-review/scripts/chain_check.py:714-734`. executed:
`tests/test_chain_check.py` passes at the target with
`test_a_heading_with_no_number_or_a_number_twice_is_refused` in it, and the
check reads the seven records with no heading refused. read: round 7's probe
showed the case red on the old reader; a refused section is left out of the
findings, so `channel` never forms `round-<N>#None`;
`docs/the-review-record.md:131-132`, its `Enforced by:` line and
`templates/sdd-round.md:59-60` name the refusal

confirms: round-7#4
The upgrade note can be followed for a 0.21.1 record, at
`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:29-72`.
read: it maps `answered`, `withdrawn`, `not a defect`, `agreed, fixed` and
a bare `fixed`, the note, `carried`, `fix-surface` and `fragment` rows, the
old field row to a regression line, a two-commit target to its later commit
and a `path#unit` to its path; it says the last record may hold no `fixed`
or `rejected` finding; and it runs the installed copy. executed: the
installed plugin keeps `chain_check.py` under
`~/.claude/plugins/cache/<marketplace>/specseal/<version>/skills/code-review/scripts/`,
the layout the note names. read: `--root` defaults to the working
directory, so the installed copy run in the worktree reads that worktree

confirms: round-7#5
The orchestrator's delivery table names the `target:` line, the regression
line and the last record's closed findings, at
`skills/implement/orchestration.md:636-639`. executed:
`tests/test_every_orchestrator_act_names_its_delivery.py` passes with row
`:637` renamed to the heading d5c83efd renamed, and `grep -c` of
`Target SHA`, `both SHAs` and the old mark's name over the file gives 0

confirms: none
What a `regression:` line marks is stated once and pointed at from the
rest, apart from finding 1, at `docs/the-review-record.md:248-260`,
`templates/sdd-round.md:47-51`, `agents/warden.md:135-142`,
`agents/framer.md:301-306`, `README.md:91-92` and `README.ko.md:78-81`.
read: each says a regression is a defect a fix pass's own commit introduced
and a build phase's unit is new work, and none restates the stop's steps.
executed: `test_a_regression_is_a_defect_a_fix_passs_own_commit_made` and
the rules-owner module pass, and the case fails against 9f293cb0's template
(exit 1, "does not say a `regression:` line is for a unit a fix pass's own
commits made"). `tests/test_no_passage_is_pasted_into_a_second_file.py`
passes

confirms: none
The frame promises part A alone, at
`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:480-497`,
`:532-556`, `:593-596` and `:820-838`. read: §*Scope*, §*The agent
definitions this item touches* and §*The proof harness* frame only what
phases 1 to 5d-iv built; every cut is named under `## Removes` as moved to
#957 (the three part-B removals, the agents section, the proof's baseline
and budget, S14 to S18, plan rows 6 to 9, Alternative L, Q4 to Q6 and the
run budget); `plan.md` keeps no row 6 to 9 and names 6a40c790 as #957's
reference; `questions.md` and `overview.md` send their part-B rows to
#957, matching #957's body. No remaining sentence of the four says part B is
in this item. The exceptions are finding 3's two lines

confirms: none
The cleanup leaves the old mark's name only where it is refused or history
in shipped text, at `docs/the-review-record.md:26`,
`skills/code-review/scripts/chain_check.py:117-128` and
`tests/test_chain_check.py:720-733`. executed: `git grep -n -i` for it
outside `seal/specs/` and `changelog/0.*` returns those three places alone.
read: the frame still names the concept so at `spec.md:455`, `:580`, `:709`
and `:727`, `questions.md:19` and `plan.md:258`, where S9 defines it as the
regression stop; `:727` cites the review skill's old heading. Those are the
framer's, named in `## Not judged`

confirms: none
Round 7's other rows of `## Not judged` are answered or moved, at
`agents/framer.md:301-306` and `skills/agent-contract/SKILL.md:283`. read:
d5c83efd rewrote the framer's route back to the regression line. The
contract's `Target SHA` is still a word a checker reads, since
`guarantee.md` keeps that row. The proof block's marker is #957's and
#940's by the frame's emoji row. The quoted-label limit stands as round 7
wrote it

confirms: none
The branch's own check and rules read clean apart from what is owed, at
the target. executed: `chain_check.py --baseline origin/release/v0.22.0` on
the clone exits 0 and names round 7's five `fixed` findings and HEAD past
its target as owing this round, and `broad-gate.md` and `guarantee.md` as
the sealer's. `bin/rules --check` resolves all 422 targets in 60 rule files

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether this round's extension line meets the extension rule. The rule extends a run only while the latest round found fewer findings than the one before, and round 7 found 5 against round 6's 1. Whether a verifying round owed after a fix pass needs the line at all is not stated | `docs/the-review-record.md:233-246`, the line under `target:` above | the orchestrator, from the owner's rule |
| Whether the frame's remaining names of the old stop (`spec.md:455`, the S9 title at `:580`, `:709`, `:727` citing the heading d5c83efd renamed, `questions.md:19`, `plan.md:258`) fall in the cleanup's class. S9 defines the name as the regression stop, so none misleads by itself | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md` | the framer |
| Round 7's four `regression: round-6#1` lines stand while the owner ruled those units new work, so the records show a round carrying the line that got a fix pass. `phases/phase-5d.md` §*Round 7 fix pass* and round 7's answers explain it | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/rounds/round-7.md` | the sealer, reading the parties against each other |
| The full suite | the tree at d5c83efd | the sealer |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r8/clone`, checked out at d5c83efd, with `origin/release/v0.22.0` fetched from the worktree (a8d83663); the clone's origin URL set to the GitHub repository so the generators write a scaffold, and the worktree's object store added as an alternate so the orphaned targets of two replay cases resolve | every run below ran there. The worktree was only read, apart from this file |
| `python3 -I evals/scripts/replay_targets.py --case replay-1791382684-r2 --case replay-1791382684-r5 --case replay-1791384160-r2 --case replay-1791779434-r5 --out <scratch>`; `python3 -I evals/scripts/seed_defects.py --case seeded-279a580b --case seeded-4d316179 --case seeded-9b644676 --case seeded-ad447367 --out <scratch>`; `diff -r` against `evals/behaviour/warden/` | exit 0 each; all eight cases identical to the tree |
| `python3 -I evals/scripts/rule_cases.py`; `git status --short` | exit 0; the tree unchanged |
| `grep -n "^pattern"` over the warden cases' `truth-*.md` graders | twelve patterns, each a `path:` line window, none holding a `#` |
| `bin/test tests/test_chain_check.py tests/test_the_rules_have_one_owner.py tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_every_orchestrator_act_names_its_delivery.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_the_record_is_written_in_words.py tests/test_one_word_one_meaning.py tests/test_no_real_identifiers.py tests/test_evals_layout.py tests/test_the_sealer_guarantees.py tests/test_broad_gate.py -q` | exit 0, 228 passed |
| `evals/scripts/replay_targets.py` and `templates/sdd-round.md` checked out at 9f293cb0; `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_the_rules_have_one_owner.py -q -p no:xdist -k "test_a_truth_never_matches_a_coordinate_the_check_refuses or test_a_regression_is_a_defect_a_fix_passs_own_commit_made"`; both files restored | exit 1, 2 failed: the old pattern matched `location: a.py#f`, and the old template "does not say a `regression:` line is for a unit a fix pass's own commits made" |
| `bin/rules --check --root <clone>` | exit 0: all 422 targets in 60 rule files resolve |
| `chain_check.py --baseline origin/release/v0.22.0 --root <clone>`, before this file | exit 0. The pull request's state is unknown, so nothing was judged as ready. Owed later: round 7's five `fixed` findings and HEAD past round 7's target, and `broad-gate.md` and `guarantee.md`, the sealer's |
| `ls` of the installed plugin's `skills/code-review/scripts/chain_check.py` under the plugin cache | present, under `<marketplace>/specseal/<version>/` |
| this file committed in the clone by a Python `subprocess` call, then `chain_check.py --baseline origin/release/v0.22.0 --root <clone>` and `--worktree`; `bin/test tests/test_no_real_identifiers.py tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py -q`; an emoji scan of the file | the first two drafts were refused at five prose lines opening with a quoted label, and rewrapped. Then exit 0: this record's three findings named as `open`, round 7's findings 1, 2, 4 and 5 confirmed and its finding 3 named by finding 2's regression line, round 7 no longer behind HEAD, `broad-gate.md` and `guarantee.md` owed to the sealer, no refusal of the record's shape. Tests exit 0, 64 passed. No emoji character |
| the full suite | not run: `unverified`, the sealer's |

Every probe file and the clone sat under `<scratchpad>/923-r8/` and were
deleted with it.
