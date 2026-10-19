# 1792368015-every-finding-carries-an-evidence-line — review round 1

target: 51e1fa5b against b196fe9b

This is round 1, so no earlier round's coordinates were carried; every fact
below was established this round. The three findings share one cause. This
item states that nothing reads a record written before the `evidence:` row,
and the cut-over rests on that statement. The build then met two readers
that do read such records, and it fixed one of them. Finding 1 is the
sentence that still says nothing reads them. Finding 2 is the one call in
the fixed reader that no test holds. Finding 3 is a limit of the new line
that the spec says is stated and that no document states.

## Findings

### 1. The review-record document still says nothing reads a merged record, after this item found two readers that do

severity: should
location: `docs/the-review-record.md:232-235`
evidence: read `docs/the-review-record.md:232-235`, `.github/scripts/release_seal.py:287-295`, `.github/scripts/release_seal.py:305-323`, `evals/scripts/replay_targets.py:553-566`
verdict: open

The paragraph this item rewrote opens "Nothing reads a record of the old
table's shape" and says a record a merged pull request left behind "is read
by nothing again, whatever its shape". The item's own frame names two readers
that read exactly those records. `release_seal.py#chain_counts` reads every
round record of a release's pull requests with the `chain_check` of the tree
it runs from (`readers`, `:287-295`). That is why `questions.md` Q2 accepts
v0.22.2's `deferred` row as `not read`. `replay_targets.py#targets` reads every
labelled record in the tree and at the last tags (`:553-566`). This build had
to change it, because the row cost it 18 of 31 targets (`overview.md`, the
second divergence row).

The sentence is wrong, and an agent acts on it. The next item that adds a row
to the table will read this paragraph to decide whether old records need
care. If it takes the paragraph at its word, it meets the replay loss and the
release panel again, which is what this item met in phase 1. The claim the
paragraph needs is narrower and true: the check at a pull request judges no
merged record again. Contract §19 asks that the amended text be rewritten in
place. The rewrite breaks no pin: the search in `## Probes` finds no test
that quotes either sentence.

```markdown
**The check reads no record of the old table's shape.** It opens the
records of the work items this pull request's own commits declare or change
and no other, so a record a merged pull request left behind is never judged
at a pull request again, whatever its shape. Two readers outside the check
still open merged records: `.github/scripts/release_seal.py#chain_counts`
reads every record of a release with the `chain_check` of the tree it runs
from, and `evals/scripts/replay_targets.py` reads each labelled record with
the `chain_check` of the commit that last wrote it. One of the old shape
under an item this pull request carries has no `## Findings` section, and is
refused by name. A work item in flight across a change to the table meets
the change as its records stand: a renamed line is rewritten into its new
spelling, and an added line is never supplied after the round that would
have written it, so an item whose records predate an added line merges
before the change or has its rounds written after it. A record written
before a line was added lacks it, and the lack is no finding for a later
round.
```

answer:

### 2. No test fails when the replay generator reads the next round with the tree's check again

severity: should
location: `tests/test_a_rewritten_definition_proved_non_inferior.py:1546-1630`, `evals/scripts/replay_targets.py:596-597`
evidence: executed `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist`, `git grep -n -l replay_targets -- tests`
verdict: open

`targets` reads two records for each round. It reads the round itself at
`:565` and the round after it at `:597`, and the round after it decides
which fixed findings become truths. Both calls now pass the commit that
wrote the record. Only the first is held. The new test stubs
`labelled_round` inside `targets`, so `targets` never reaches `confirmed`.
The test's direct call `confirmed(nxt, 1, at=written)` shows that
`confirmed` honours `at`. It does not show that `targets` passes `at`.

Commit 0a5d3445 claims the replay case "now holds both", the next round read
by its own check and `targets` passing a commit. I found that it holds the
second only for the round itself. In the round's clone I changed `:597` to
`confirmed(nxt, n, following)`, which drops the commit. The whole module
then passed, 105 tests. `git grep -l replay_targets -- tests` names no other
test module. Under that change, every round whose next round predates the
row confirms nothing. It drops out as "no fixed finding the next round
confirmed", which is the 31-to-13 loss this build repaired, and only a
manual `--list` would show it.

The test below was run in the clone. It passed against the tree as
committed, and it failed against the change above with `[(1,
'seal/specs/i/rounds/round-2.md', None)]`. It goes after
`test_a_labelled_record_is_read_by_the_grammar_of_the_commit_that_wrote_it`.

```python
def test_targets_reads_the_next_round_by_the_commit_that_wrote_it(monkeypatch):
    """Guards the owner's decision on #985 where `targets` reads the round
    after a fixed finding: that round is judged by the check of the commit
    that wrote it, so a round written before the `evidence:` row still
    confirms the fix it names, and the replay keeps the target."""
    rt = load_script("replay_targets")
    two = "seal/specs/i/rounds/round-2.md"
    monkeypatch.setattr(
        rt,
        "records",
        lambda _tags, _items=None: {
            ("i", 1): LABELLED_ROUND_1,
            ("i", 2): LABELLED_ROUND_2,
        },
    )
    monkeypatch.setattr(rt, "written_at", lambda rel, _tags: f"at {rel}")
    monkeypatch.setattr(
        rt,
        "labelled_round",
        lambda _text, _rel, _n, at=None: (
            {
                "sha": "abc1234",
                "value": "abc1234 against main",
                "findings": [(1, "x", "`src/a.py:12`", True)],
                "confirms": set(),
            },
            "",
        ),
    )
    monkeypatch.setattr(rt, "resolve", lambda _rev: True)
    monkeypatch.setattr(rt, "target_base", lambda _value, _target: ("abc1234", "main"))
    # The one git call left before `confirmed`: routing.md at the target.
    monkeypatch.setattr(rt, "git", lambda *_args, check=True: "| Branch | b |\n")
    asked = []

    def spy(_text, n, rel, at=None):
        asked.append((n, rel, at))
        return set()

    monkeypatch.setattr(rt, "confirmed", spy)
    rt.targets([])
    assert asked == [(1, two, f"at {two}")], asked
```

answer:

### 3. A command holding a backtick cannot stand on an `evidence: executed` line, and the limit the spec calls stated is stated nowhere

severity: should
location: `docs/the-review-record.md:102-107`
evidence: executed `grep -n "backtick" docs/the-review-record.md templates/sdd-round.md`, `grep -n -i "backtick\|\$( " agents/warden.md skills/code-review/SKILL.md templates/sdd-round.md`
verdict: open

The row's `executed` form is `` `[^`]+` ``, so a backtick ends the command
(`docs/the-review-record.md:46`). `spec.md:150-151` accepts that as "a stated
limit (use `$( … )`)". The two searches above find no statement of it in
the row's meaning paragraph, the template, the warden's definition or the
review skill. The only hits are the word "backticked" in the two rows that
take coordinates, for `location:` and `evidence:`.

This matters in this repository more than most. Its documents put labels and
names in backticks, so the search an absence claim rests on often looks for
a backticked string, for example a `git grep` for a label written with its
backticks. The warden writes the command as it ran it. The check refuses the
line and repeats the row's `Refused as`, which does not say how to write
such a command. The warden then has two ways out, and both are worse: it
names a different command from the one it ran, or it moves an absence claim
to `read`, which the absence rule forbids. The warden's preload has 4 bytes
to spare, so the statement belongs in the paragraph the warden opens at
step 7, not in `agents/warden.md`.

```markdown
**A finding's `evidence:` line names what its claim rests on.** `executed`
names each command the round ran for it, and `read` each `path:line` it
opened, so a later reader repeats the act instead of trusting the prose. A
claim resting on neither is no finding but a row of `## Not judged`. The
check holds the line to its row and reads nothing out of it. A backtick
ends a command on the line, so a command that holds one is written so the
shell makes it, with `$(printf '\140')` in place of the character, and it
runs as the command the round ran.
```

answer:

## Confirmations

confirms: none
The warden's preload is 27,168 bytes, at most 27,172 as S11 asks: `wc -c
agents/warden.md skills/agent-contract/SKILL.md` gives 10,565 and 16,603,
executed. The `agents/warden.md` measured in phase 3 is the one shipped. Its
sha256 at 51e1fa5b equals the `12c1c4c2…` hash in
`evals/warden-phase-3.md` (executed, `shasum -a 256`), and nothing under
`agents`, `skills`, `templates` or `docs` changed after ba2a3187 (executed,
`git diff --stat ba2a3187..51e1fa5b`).

confirms: none
S1 to S6 are seen red without the row. In the round's clone I deleted the
row for `evidence:` from `docs/the-review-record.md` and ran the six cases
that name it. All six failed: the two `TestGrammar` cases, the spelling case, the
two new evidence cases and the template case (executed). With the row back,
`tests/test_chain_check.py` and `tests/test_review_axes.py` pass, 91 tests
(executed).

confirms: none
The per-commit loading in `replay_targets.py` holds across the history it
reads. A probe read every labelled record at the last two tags and at every
tag through `written_at` and `labelled_round`. There were 51 records, written
by 11 commits, giving 6 distinct sets of `CHECK_FILES`. Every set loaded, no
record was refused by its writer's check, and the tree's check refuses 38 of
them. The temporary directories were gone after the run (executed, the first
probe row). Each copy is imported under its own module name, and
`module_from_spec` does not add it to `sys.modules`, so no copy's state
reaches another (read, `evals/scripts/replay_targets.py:146-216`). A record
no commit wrote falls back to the tree's check (read, `:181-192`).

confirms: none
The release pull request into `main` does not judge the 0.22.2 items whose
records predate the row, #943 and #970 among them. The check gives a
declaration that only GitHub's squash commits touched to the pull request
that carried it (read, `skills/code-review/scripts/chain_check.py:592-628`,
`:1820-1830`). The spawn prompt says the base gained #970 after b196fe9b,
and #970's branch holds two rounds (executed, `git diff --name-only` of that
branch against b196fe9b). Merged before this item, they fall under the
rewritten paragraph's rule.

confirms: none
No other reader of round records breaks on the new line. `git grep` across
`skills/*/scripts`, `hooks`, `.github/scripts`, `evals/scripts` and `bin`
names the readers. `broad_gate.py` and `seal_stamp.py` read through
`chain_check`. The finding regex in `evals/scripts/behaviour.py:77-81`
skips any line before `verdict:` lazily. `rule_cases.py`'s sealer round
holds no finding. `noninferiority.py` grades only `location:` lines
(executed, the reader search; read, the coordinates named).

confirms: none
The account's claim that `--list` names 31 targets: in the round's clone,
with the source's remote-tracking refs fetched in, `--list` keeps 15. None of
the rounds it leaves out is refused by a check. 61 are left because their
target commit does not resolve in the clone, and 10 have no next round, no
confirmed fix or no base that resolves (executed). The refusal half of the
claim holds. The count itself is a `## Not judged` row.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `replay_targets.py --list` names 31 targets in the source repository, whose object store holds commits this round's clone does not | `seal/specs/1792368015-every-finding-carries-an-evidence-line/overview.md` | the orchestrator, by running `--list` in the main checkout |
| `written_at` takes the commit that last wrote a record, not the first. A commit that edits an old record after a later grammar change, such as one respelling a renamed label, moves that record to the newer grammar, so it would be refused for a row it never owed. Whether "the grammar of its own time" means the first write or the last is the owner's call | `evals/scripts/replay_targets.py:181-192` | the owner |
| Whether the warden side's fail on rules 1 and 2 is noise: recorded and shipped by the owner's decision of 2026-10-19, and the spawn prompt says not to reopen it | `seal/specs/1792368015-every-finding-carries-an-evidence-line/phases/phase-3.md` | the owner, decided |
| The full suite, the repository-wide lint and the typecheck at 51e1fa5b, which this round did not run (`unverified`) | the branch | the orchestrator's `broad-gate` run |

## Probes

| Command | Result |
|---|---|
| `python3 evals/scripts/test_tmp_replay_probe.py`, run once in the round's clone and deleted: `written_at` and `labelled_round` for every labelled record at the last two tags and at every tag, then `targets` | 51 labelled records, 11 writing commits, 6 check sets loaded, 0 refused by the writer's check, 38 refused by the tree's, and no `specseal-replay-check-*` directory left after exit |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k labelled` | 4 passed |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist`, with `replay_targets.py:597` changed to `confirmed(nxt, n, following)` in the clone, then restored | 105 passed: the change survives |
| `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k targets_reads_the_next_round`, with finding 2's test added in the clone, against the tree and then against the change above, then both restored | passed against the tree, failed against the change with `[(1, 'seal/specs/i/rounds/round-2.md', None)]` |
| `bin/test tests/test_chain_check.py -q -p no:xdist -k "evidence or another_spelling or template_is_the_record or table_loads or name_every_line"`, with the `evidence:` row deleted in the clone, then restored | 6 failed |
| `bin/test tests/test_chain_check.py tests/test_review_axes.py -q -p no:xdist` | 91 passed |
| `python3 evals/scripts/replay_targets.py --list`, in the clone with the source's remote-tracking refs fetched | 15 kept; 0 left out by a check refusal, 61 by a target that does not resolve in the clone, 10 for other reasons |
| `wc -c agents/warden.md skills/agent-contract/SKILL.md` | 10565 + 16603 = 27168 |
| `git grep -n "Nothing reads a record\|read by nothing again\|old table's shape" -- . ':!seal'` | `docs/the-review-record.md:232`, `.github/scripts/release_seal.py:317` and `tests/test_broad_gate.py:137`; no test quotes either sentence of finding 1 |
