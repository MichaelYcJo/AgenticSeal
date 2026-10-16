# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 9

target: a6ccc363, fixes 80636f64..a6ccc363

Extended past round 8: round 8 found 3, round 7 found 5, and the frame took round 8's regression.

A verifying round over the reframe after round 8 (3e6edf87), its approval
(2dbebf7c) and phase 5d-v (a6695b61, 5441ebdb, a6ccc363). Round 8's three
findings read `deferred the frame`, so this round owes them nothing. No
commit in the range is a fix pass's: 5d-v is a build phase the framer
designed and the owner approved, so nothing below carries a regression
line, and no earlier close was found not to hold, so nothing below
carries a reopens line either.

The reader holds where the row aimed it. The new line is read with its
line number, a reference to a round alone is refused, a finding with both
relations is refused at the later line, and dangling and round-1
references are refused by line (confirmations below). The 59 modules that
name a file the range touched pass.

Four findings follow, in cause order. Finding 1 is the source: the texts
give a `fixed` commit that touched its finding's unit and did not fix it
to both relations at once, and the two route differently. Finding 2 is
the run's arithmetic: the unchanged extension rule stops extending at any
round carrying a regression, while 5d-v routes that round to a fix pass
or to a redesign whose run goes on. This record's own extension line is
the measured case. Finding 3 is the run-end sentence 5d-v wrote. It omits
the second condition that S26 and the check both hold. Finding 4 is the
reader's one fail-open edge: a label with no value is read as no line.

Findings from reading and from execution are labelled in each finding. The
full suite was not run. It is `unverified`, and the sealer answers it.

## Findings

### 1. A fixed commit that changed the defect's unit and did not fix it is given both a regression line and a reopens line, and the two are routed differently

severity: should
location: `docs/the-review-record.md:261-285`, `agents/warden.md:136-148`, `templates/sdd-round.md:47-59`
verdict: open

Every `fixed <commit>` touches a path its finding names, because the check
refuses one that does not (`docs/the-review-record.md:46-55`). So a fix
that did not hold has, in the ordinary case, changed the unit the defect
still stands in. The texts give that finding two lines.

- The trigger sentence. `docs/the-review-record.md:262-266` says that
  where a finding stands in a unit a fix pass's own commits added or
  changed, the warden writes its regression line. `agents/warden.md:136-137`
  says such a finding carries one.
- The reopen sentence. `docs/the-review-record.md:282-285` and
  `agents/warden.md:146-148` say that a `fixed` commit that did not fix
  it, where no fix pass's commit made the defect, takes a reopens line.

The defect predates the fix, so by the definition at `:262` it is no
regression. The trigger sentence still fires on it, because the unit is
one the fix pass changed. The check refuses a finding with both lines, so
the warden must pick one, and the pick decides the route. A reopens line
gets a fix pass. A regression line is routed by the comparison, may send
the item to its framer, counts toward the loop guard, and stops the
extension rule (finding 2). `spec.md` S9 narrows its case to a `fixed`
commit "that changed another unit", which leaves the common case open.

read: the five coordinates at a6ccc363, and `spec.md` S9 at `:623`. The
fix below keeps the phrase the module
`tests/test_the_rules_have_one_owner.py` pins ("a fix pass's own commits
added or changed").

```markdown
<!-- docs/the-review-record.md:262-266, the trigger sentence -->
regression is a defect a fix pass's own commit introduced. Where a finding
stands in a unit a fix pass's own commits added or changed, and those
commits introduced its defect, the warden writes its `regression:` line,
naming the finding whose fix made the unit as `round-<N>#<n>`, or that
round as `round-<N>` where no finding named the unit, and names the unit
first in the grounds.

<!-- docs/the-review-record.md:282-285, the reopen sentence -->
A close that does not hold where no fix pass's commit made the defect, a
`rejected` finding that holds after all or a `fixed` commit that did not
fix it, in the unit that commit changed or in another, is raised again as
an ordinary finding with a `reopens:` line naming it, and gets its fix
pass.
```

```markdown
<!-- agents/warden.md:136-137 -->
  The diff's new units are reviewed as code. A finding whose unit is one a
  fix pass's own commits added or changed, and whose defect those commits
  introduced, carries a `regression:` line —

<!-- agents/warden.md:146-148 -->
  A close that does not hold where no fix pass's commit made the defect —
  a rejection that was wrong, a `fixed` commit that did not fix it, in the
  unit it changed or in another — takes `reopens:`, not `regression:`
  (`docs/the-review-record.md` §*The run*).
```

```markdown
<!-- templates/sdd-round.md:47-49 -->
  regression:  only on a finding in a unit a fix pass's own commits added
               or changed, where those commits introduced the defect: the
               earlier finding as `round-<N>#<n>`, or `round-<N>` for a fix
               pass no finding named. A defect the fix found standing and
               did not repair takes `reopens:`. A unit a build phase made
               is new work and takes none. The grounds then owe
```

answer:

### 2. The extension rule stops the run at any round carrying a regression, while phase 5d-v sends that round to a fix pass or to a redesign whose run goes on

severity: should
location: `docs/the-review-record.md:246-274`, `templates/sdd-round.md:23-25`, `skills/code-review/orchestration.md:119-123`, `agents/framer.md:310-311`, `README.md:90-92`, `README.ko.md:78-81`
verdict: open

`docs/the-review-record.md:246-251` lets the orchestrator spawn a finding
round past round 3 only while the latest round found fewer findings than
the one before and "none of them is a regression". The template's line
(`templates/sdd-round.md:25`) and both READMEs say the same. Before 5d-v
that clause agreed with the route, because every regression went to the
framer with no fix pass. 5d-v keeps the clause and changes the route in
two ways, and each now contradicts it.

- The fix-pass route. `docs/the-review-record.md:275-277` gives a
  regression an ordinary fix pass. That pass writes `fixed <commit>`, and
  the check refuses a last record holding one
  (`docs/the-review-record.md:164-171`). Past round 3 the extension rule
  forbids the round that would read it, and the cap's ladder takes only
  findings still open (`:257-258`). The run can neither end nor go on.
- The framer route. `docs/the-review-record.md:274` and
  `skills/code-review/orchestration.md:122-123` say the run goes on with
  the redesign's build and its rounds. Past round 3 the extension rule
  forbids those rounds, since a framer route always follows a round
  carrying a regression. `agents/framer.md:311` still calls that round
  "the record that stopped the run".

executed: this record's own extension line. The spawn prompt gave
"and the frame took round 8's regression", which the template's line does
not have and the rule does not state. Round 8's finding 2 carries a
regression line naming round-7#3, so under `:246-251` no round 9 may be
spawned.
read: the coordinates above at a6ccc363. `spec.md:488` keeps the clause
and S26 at `:634` says the run goes on, so the frame holds both. Which way
to settle it is the framer's choice, and the paste below is one way that
keeps the clause for finding rounds.

```markdown
<!-- docs/the-review-record.md:246-251 -->
**A run has three finding rounds by default, and extends one round at a time
while the findings shrink.** Past round 3 the orchestrator spawns one more
finding round only while the latest round found fewer findings than the one
before it and none of them is a regression. A verifying round owed after a
fix pass, a regression's fix pass among them, is spawned whatever the
count, since the check refuses a last record holding a `fixed` or
`rejected` finding. A round routed to the framer starts the count again, so
the redesign's build has three finding rounds of its own. Each extension is
one line in that round's record, written by the warden from the reason the
spawn prompt gives:
```

```markdown
<!-- agents/framer.md:310-311 -->
line under your mark, `Reframed <date> by <who>, after round <N>.`, where
`<N>` is the record whose regression was routed to you. `docs/the-review-record.md` §*The
```

```markdown
<!-- README.md:90-92 -->
The review run is bounded: three finding rounds by default, and one more at
a time only while each round finds fewer findings than the one before and
none of them is a regression, a defect a fix pass's own commit introduced.
A verifying round owed after a fix pass is spawned whatever the count, and
a reframe starts the count again.
```

```markdown
<!-- README.ko.md:80-81 -->
지적을 고치는 단계(fix pass)의 커밋이 새로 만든 결함(regression)이 아닐 때에만
한 회차씩 늘립니다. 고친 뒤에 필요한 검증 회차는 횟수와 상관없이 돌리고,
프레임을 다시 그리면 횟수를 처음부터 다시 셉니다.**
```

answer:

### 3. The run-end sentence states one of the check's two conditions, so the orchestration can end a run the check then refuses

severity: should
location: `skills/code-review/orchestration.md:123-127`
verdict: open

`skills/code-review/orchestration.md:123-127` says the run ends only on a
round whose record holds no `open`, `fixed` or `rejected` finding, "since
the check refuses a ready pull request whose last record holds one". The
check holds a second condition on the same record: its `target:` commit is
HEAD, or only the work item's own records follow it
(`docs/the-review-record.md:164-168`). `spec.md` S26 at `:634` asks the
section to say both. It names the run ending "with no commit outside the
item's records after its `target:`". The plan row 5d-v named only the
first, and the sentence followed the row.

The gap is reachable. At the cap, the ladder's first rung sends a finding
the branch owns to "the diff" (`docs/the-review-record.md:293`). That
commit follows the cap round's `target:`, so the round reads clean by the
sentence and is refused by the check, which then owes a verifying round.

read: the coordinates above at a6ccc363. T44 pins the first condition and
not the second, so the paste keeps T44's phrase contiguous.

```markdown
item returns to its framer the run goes on with the redesign. The run ends
only on a round whose record holds no `open`, `fixed` or `rejected` finding
and whose `target:` commit is HEAD, or is followed only by the work item's
own records — a verifying round, or the round at the cap whose open
findings took the filing ladder — since the check refuses a ready pull
request whose last record fails either.
```

answer:

### 4. A reopens or regression line with nothing after it is read as no line, so it escapes the empty-value refusal and the both-lines refusal

severity: should
location: `skills/code-review/scripts/chain_check.py:111-112`, `skills/code-review/scripts/chain_check.py:813`, `tests/test_chain_check.py`
verdict: open

`spec.md` S24 says that a label with nothing after it, its trailing space
trimmed, is the exact form, and that its value's reader judges the empty
value. For `verdict:` and `location:` the empty line is refused. The two
reference labels are compiled as `^reopens: (.*)$` and
`^regression: (.*)$` (`chain_check.py:111-112`). That pattern needs a
space, so a bare label matches neither. It is exact by `EXACT_LABEL`, so
it is not refused as misspelt. It is a finding label, so it is not refused
as out of place. The finding then reads with no relation. A bare regression
line beside `reopens: round-1#1` also escapes the both-lines refusal that
`docs/the-review-record.md:139` states. A bare line naming an owed
`fixed` finding is still caught: the earlier finding is refused as
unnamed. A bare line on any other finding passes silently.

5d-v carried this into the new label. The regression half stands since the
reader of 5d-ii, and `overview.md:82` names only the empty verdict and
location cases.

executed: probe 1 below. A bare reopens line read as `(1, None, None)`
with no error. A bare regression line beside `reopens: round-1#1` read as
`(1, (1, 1), None)` with no error. The fix below with the case below:
exit 0, 50 passed with `tests/test_chain_check.py`. The case without the
fix: exit 1, 1 failed (probe 2).

```python
# skills/code-review/scripts/chain_check.py:111-112
REGRESSION_LABEL = re.compile(r"^" + re.escape(REGRESSION) + r"(?: (.*))?$")
REOPENS_LABEL = re.compile(r"^" + re.escape(REOPENS) + r"(?: (.*))?$")

# skills/code-review/scripts/chain_check.py:812-816, in finding_of's one()
        said = [
            (i, pattern.match(lines[i]).group(1) or "")
            for i in range(first + 1, stop)
            if pattern.match(lines[i])
        ]
```

```python
# tests/test_chain_check.py, TestFindings
    def test_a_reference_label_with_nothing_after_it_is_refused(self):
        """S24: a bare `reopens:` or `regression:` line is the exact form,
        and its reader refuses the empty value; a bare `regression:` beside
        a `reopens:` line is refused as a finding holding both."""
        for bare in ("reopens:", "regression:"):
            text = record(
                "abc1234",
                [
                    finding(1, "open").replace(
                        "verdict: open\n", f"verdict: open\n{bare}\n"
                    )
                ],
                n=2,
            )
            lines = reader.readable(text)
            found, errors = chain.findings(reader, lines, "r.md")
            assert found == [], bare
            assert [line for _r, line, _w in errors] == [
                lines.index(bare) + 1
            ], errors
        both = record(
            "abc1234",
            [
                finding(1, "open", reopens="round-1#1").replace(
                    "verdict: open\n", "verdict: open\nregression:\n"
                )
            ],
            n=2,
        )
        found, errors = chain.findings(reader, reader.readable(both), "r.md")
        assert found == [], errors
        assert any("`reopens:` line" in why for _r, _l, why in errors), errors
```

answer:

## Confirmations

confirms: none
The reader reads a reopens line as the row says. It reads the line into
its finding with its number, refuses `reopens: round-1` through
`reopened_of` (`chain_check.py:636-643`), refuses a second reopens line,
and refuses a finding holding both relations at the later line, naming
which line each case takes (`chain_check.py:868-876`). executed: T42 in
the module run, and probe 1, where `round-1#0`, two references, two
spaces, a trailing space and an empty value after the space were each
refused by line, and a tab or a space before the colon was refused as
another spelling.

confirms: none
The channel counts a reopens reference as covering and checks it as it
checks the other two (`chain_check.py:1071-1104`). A reopens line in round
1, one naming a later record, and one naming a finding the record does not
hold are each refused by line. The unnamed-finding refusal names all three
labels. executed: T43 in the module run. A reopens line naming an earlier
`deferred` finding passes, which `questions.md` states on purpose (the
check reads no earlier verdict for any of the three lines). executed:
probe 1, `channel` returned nothing.

confirms: none
The regression route reads the same in the document, the orchestration,
the warden and the framer. Each routes on one sentence of the grounds
comparing the fix with the frame. The document and the orchestration's
table name the three routes, the loop guard among them, and no carrier
sends the item to its framer on the line alone. T44 and T45 pin what
`spec.md` S26 and S27 say they pin. read:
`docs/the-review-record.md:261-286`, `skills/code-review/orchestration.md:129-151`,
`agents/warden.md:136-148`, `agents/framer.md:300-312`,
`tests/test_the_rules_have_one_owner.py:227-325`. Findings 1 to 3 are
where the texts disagree with each other or with the check.

confirms: none
Nothing the range touched broke. executed: the 59 modules that name a
path the range changed outside `seal/specs/`, plus the row's twelve, exit
0. `bin/rules --check` resolves 428 targets in 60 files. `chain_check.py`
before this file refused no record's shape.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The phase record's reference run: 58 modules and 2,806 passed. The list rebuilt here from its description holds 59 modules, and they gave 2,449 passed and 9 skipped. The list the phase ran is not written down, so the two runs cannot be compared | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/phases/phase-5d.md:779-782` | the smith, from the phase's command |
| The seven mutations the phase record names. They were read and not re-run | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/phases/phase-5d.md:725-736` | the sealer, if it samples them |
| The full suite | the tree at a6ccc363 | the sealer |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into `<scratchpad>/923-r9/clone`, at a6ccc363, with `origin/release/v0.22.0` from the worktree | every run below ran there. The worktree was only read, apart from this file |
| probe 1: `python3 -I <scratchpad>/923-r9/test_tmp_reopens_edges.py <clone>`, `findings` over a round-2 record per edge, and `channel` over two records | exit 0. A bare reopens line read as `(1, None, None)` with no error. A bare regression line beside `reopens: round-1#1` read as `(1, (1, 1), None)` with no error. `reopen:`, `reopened:` and a quoted line read as prose. `reopens: ` with a trailing space, two spaces, a trailing space after the reference, `round-1#0` and two references were refused by line. A tab, or a space before the colon, was refused as another spelling. A reopens line naming a `deferred` finding gave no problem. A bare reopens line on round 2 left round 1's `fixed` finding refused as unnamed |
| `bin/test` over the 59 modules that `git grep -l` finds in `tests/` for each path `git diff --name-only 80636f64..a6ccc363` lists outside `seal/specs/`, with the row's twelve, `-q` | exit 0, 2,449 passed, 9 skipped |
| probe 2: finding 4's fix applied to the clone's `chain_check.py` with the Edit tool, finding 4's case as `tests/test_tmp_bare_label.py`; `bin/test tests/test_tmp_bare_label.py tests/test_chain_check.py -q -p no:xdist`; the file restored with `git checkout`; the case alone again | with the fix: exit 0, 50 passed. Without it: exit 1, 1 failed, the bare reopens line read into a finding. The case file was deleted and `git status --short` was empty |
| `bin/rules --check --root <clone>` | exit 0: all 428 targets in 60 rule files resolve |
| `chain_check.py --baseline origin/release/v0.22.0 --root <clone>`, before this file | exit 0. The pull request's state is unknown, so nothing was judged as ready. Owed: round 8 behind HEAD (a6695b61 touches `chain_check.py`), and `broad-gate.md` and `guarantee.md`, the sealer's |
| this file committed in the clone by a Python `subprocess` call, then `chain_check.py --baseline origin/release/v0.22.0 --root <clone>` and `--worktree`; `bin/test tests/test_no_real_identifiers.py tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py -q`; an emoji scan of the file | the first draft was refused at one prose line opening with a backticked label, and rewrapped. Then exit 0 for both: this record's four findings named as `open`, round 8 no longer behind HEAD, `broad-gate.md` and `guarantee.md` owed to the sealer, no refusal of the record's shape. Tests exit 0, 64 passed. No emoji character |
| the full suite | not run: `unverified`, the sealer's |
