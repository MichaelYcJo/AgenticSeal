# Review round 2: 1793057292-agent-lifetime-and-process-archive

target: 08469dff, fixes 25afe39a..08469dff

Round 2 is the verifying round for round 1's seven findings, each closed
`fixed <commit>`. It read the fix diff `25afe39a..08469dff` in the worktree
the spawn named. The spawn also asked for one more reading of the whole
branch diff `fa7d1374...08469dff`, and the round did that too; what that
reading found outside the fix diff is reported like the rest. No
`seal/parity.md` is declared, so no parity comparison applies.

Three facts are carried from round 1 and not re-established. The first is
that `chain_check.py#follows` lists commits with `--no-merges` (round 1's
third `confirms: none`). The other two are the facts round 1 left in
`## Not judged`: the 142 failed hygiene runs, and phase 1's 806,241. This
round re-established the rest: each fix against its finding, the template
census, the rule pins, the durations entries, the settle dry run at the
branch head and at the fork point, and the CI run at `08469dff`.

## Findings

No finding opened this round.

## Confirmations

confirms: round-1#1
`agents/framer.md:62-66` names `templates/process.md` as the shape of each
row of the archive, in round 1's text. The fix range changes no other line
of the definition. `bin/test tests/test_the_pull_request_language_is_the_repositorys.py -q -k test_every_template_is_named_by_a_document_that_ships`
exits 0 with 1 passed, where it exited 1 at `25afe39a`. The `tests` run
40430474904 at `08469dff` concluded `success` on ubuntu, on the three macOS
groups and on the four Windows groups, and the `durations` job passed.
Executed.

confirms: round-1#2
`def test_a_draft_is_tolerated_and_still_owes_the_record():` stands again at
`tests/test_the_rules_have_one_owner.py:193`, so the fix-pass case at line
174 ends at its own two `not in` assertions, and the draft case's docstring
is a docstring again. Collecting the module gives 31 cases, the draft case
among them. Every `.test_durations` key of the module names a collected
case. One key differs only because the comparison spelt an escaped
character of a parameter id differently, and it names a collected case.
Executed with `bin/test tests/test_the_rules_have_one_owner.py --collect-only -q -p no:xdist`,
compared with the module's keys in `.test_durations`.

confirms: round-1#3
`spec.md:283-290` holds a `change` for `docs/the-record-layout.md` *The
fold, and what tells it from a deletion*. Its `from` is the clause that says
every pull request after the fold turns red, the shipped template included.
Its `to` says a person runs the command after the fold and the command
refuses a finished settle. The orchestrator wrote a shorter `from` than
round 1's fenced text, and it still covers the whole false clause and no
more. The settle dry run at `08469dff` lists it as operation 10 of group
26, `from found, to not found`. `git grep -n "turning every" -- seal/specs docs skills`
finds the sentence at `docs/the-record-layout.md:189`, this item's `from`
and round 1's record, and no other spec's `to` states it again. Executed.

confirms: round-1#4
`README.ko.md:251` ends its list of a row's numbers with "토큰, 그리고 가장
큰 턴 하나가 읽은 컨텍스트", as `README.md`'s row names the largest context.
The rest of the cell is unchanged. `git diff --stat fa7d1374...08469dff`
shows the branch changes 2 lines of `README.md` and 2 of `README.ko.md`, so
no other row is left unmirrored. Executed for the stat, read for the cell.

confirms: round-1#5
The prevention-home rule at `skills/implement/orchestration.md:51-57` now
has one reading. The work item in progress builds the home, and the issue
of the work item in progress records it. The fix also added a sentence:
the orchestrator folds the home into that work item's frame. That sentence
is round 1's fenced text. It applies the folding rule at lines 33-43, which
already binds every decision made after the frame is committed, so it adds
no behaviour of its own. `spec.md` *Scope* item 4's last bullet (d21e38bd)
names the same builder and the same issue. It does not repeat the fold,
which the bullet on folding above it states. `overview.md` *Not verified*
no longer holds the row naming the two readings. The changelog fragment's
item says the same as the rule. `bin/test tests/test_the_rules_have_one_owner.py tests/test_every_orchestrator_act_names_its_delivery.py -q`
exits 0 with 45 passed. Executed for the run, read for the rest.

confirms: round-1#6
The folding rule at `skills/implement/orchestration.md:33-43` names the
orchestrator as the party that keeps the line. The line sits below the
approval line, or below the title before the plan is approved. The handoff
rule at lines 45-49 names the orchestrator that hands the work over as the
writer, and the orchestrator that takes it over as the one that deletes.
Nothing in the tree parses the lines under `plan.md`'s title: `git grep -n
"Approved" -- '*.py'` outside `tests/` finds only an eval fixture. So a fold
line written there before approval disturbs no check.

The smith also added pins in 5be7d538 that round 1 did not ask for. They
pin the named actors, which are what this finding was about, and contract
rule 14 asks for a pin on a changed sentence a person acts on. The pins are
not idle. In a scratch clone at `08469dff`, with
`skills/implement/orchestration.md` restored to its 098d2b45 text, both
cases fail on the new pins: "the orchestrator keeps one line of its own in
`plan.md`" and "The orchestrator that hands the work over writes". The file
was put back after the run. `bin/test-layout --pairs tests/test_the_rules_have_one_owner.py`
names no pair. `git grep` of the pinned phrases over `tests`, `skills` and
`docs` finds them only in the rule and in this module. Executed.

confirms: round-1#7
`overview.md:14-19` *Where spec and implementation diverged* no longer holds
the threshold row, and it keeps its other four rows, unchanged. Nothing else
in the memo states 461,000. Read at `overview.md:12-19`, and executed with
`git grep -n "461,000" -- seal/specs/1793057292-agent-lifetime-and-process-archive/overview.md`,
which prints nothing.

confirms: none
This work item did not cause the settle dry run's `from not found` for
`seal/specs/1792993972-settle-writes-each-sections-latest-decision/spec.md:260`.
It was already so at `fa7d1374`. The branch changes no file under `docs/`:
`git diff --stat fa7d1374 08469dff -- docs` prints nothing. The operation's
`from` ends with `check: tests/test_settle.py`, while
`docs/the-record-layout.md:100` reads `check: tests/test_settle_reads_before_it_removes.py`.
It read the same at `fa7d1374`, by `git show fa7d1374:docs/the-record-layout.md`.
#1001's b451e503 made that change. A dry run in a clone at `fa7d1374`
prints the same `from not found` for that operation. It prints the same
for operation 7 of the group, `spec.md:302` of the same work item. The dry
run refuses nothing on a `from not found`, and the settling session writes
each section's latest decision, so weighing this is the release settle's
job. Executed.

confirms: none
The whole branch diff, read once more, gives nothing round 1 missed.
`git grep` outside the records for a count of gate arms, for the removed
step's name and for `unverified-rows` finds no stale text.
`broad_gate.py`'s `--preflight` paragraph says "arms 2 and 3". The other
`docs/` sentences naming `unverified` state general rules: the record
layout's baseline section and the `unverified_check.py#settled` predicate.
They are true without the arm. `CONTRIBUTING.md`'s new row says no CI step
reads an `overview.md`, and that holds. `chain_check.py` and
`gather_changelog.py` name no `overview`. `issue_claims_check.py` loads the
reader only for `gfm_lines` over the pull request body. No test reads the
repository's own overviews. `session_cost.py#largest_context` reads every
message with a `usage` block once by `message_key`. A split message takes
each field's largest value. An empty window answers None, and the table
prints a dash for it. `segment_slices` indexes the result by the slice's
window. Executed with `git grep`, read for the code.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at this head. This round ran none of the three. This round leaves no finding open, so the orchestrator's broad run comes due, and the sealer's spawn after it | `broad-gate.md` | the orchestrator, by `broad-gate --base release/v0.22.4 --record` |
| That the removed step failed in none of 142 failed hygiene runs from 2026-09-23 to 2026-10-25. Carried from round 1, not re-run | `spec.md` *Scope* item 5 | the sealer, in its sample of claims |
| That 806,241 is the largest context a fresh, never-resumed smith reached in the 0.22.0 run. Carried from round 1, not re-run | `phases/phase-1.md` | the sealer, in its sample of claims |
| Whether the branch merges cleanly into `release/v0.22.4`, which has moved to 5bab081e. No pull request exists yet | `gh pr view <N> --json mergeable` | the orchestrator, once the pull request opens |
| Q1, no archive files for 0.22.0 to 0.22.3, and Q2, a merge and never a rebase, both on their defaults | `questions.md` Q1, Q2 | the owner, at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_the_pull_request_language_is_the_repositorys.py -q -k test_every_template_is_named_by_a_document_that_ships` | exit 0, 1 passed |
| `bin/test tests/test_the_rules_have_one_owner.py tests/test_every_orchestrator_act_names_its_delivery.py -q` | exit 0, 45 passed |
| `bin/test tests/test_the_rules_have_one_owner.py --collect-only -q -p no:xdist`, compared with the module's keys in `.test_durations` | 31 collected, 24 priced, every priced key collected, `test_a_draft_is_tolerated_and_still_owes_the_record` among them |
| `bin/test tests/test_the_rules_have_one_owner.py -q -k "test_a_decision_after_the_frame_is_folded_into_it or test_a_handoff_file_is_written_only_to_move_the_work"` in a scratch clone at `08469dff` with `skills/implement/orchestration.md` at 098d2b45 | 2 failed, each on a pin 5be7d538 added; the file was restored and the clone's status is clean |
| `bin/test-layout --pairs tests/test_the_rules_have_one_owner.py` | exit 0, 0 pairs |
| `python3 skills/settle/scripts/settle.py --released-at HEAD` at `08469dff` | exit 0; this spec's operations each read `from found` where they have a `from`; `1792993972-settle-writes-each-sections-latest-decision/spec.md:260` and `:302` read `from not found` |
| `python3 skills/settle/scripts/settle.py --released-at HEAD` in a `git clone --no-local` at `fa7d1374` | exit 0; the same two operations read `from not found` |
| `gh run view 40430474904 --json headSha,conclusion,status` | `08469dff`, completed, `success` |
