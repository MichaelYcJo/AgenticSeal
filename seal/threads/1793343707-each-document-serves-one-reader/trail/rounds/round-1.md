# Review round 1: 1793343707-each-document-serves-one-reader

target: 16056d31 against origin/release/v0.25.1

## Findings

### 1. The check passes a finding located in code when its fix commit touched only the records

severity: must
location: `skills/code-review/scripts/chain_check.py:1746`, `skills/code-review/scripts/chain_check.py:34-45`, `skills/code-review/scripts/chain_check.py:1358-1372`, `tests/skills/test_chain_check.py`, `README.md:207-213`, `README.ko.md:201-206`, `agents/sealer.md:93-98`, `skills/code-review/orchestration.md:99-105`, `skills/implement/acts.md:72`, `seal/threads/1793343707-each-document-serves-one-reader/changelog.md:14`
evidence: executed `bin/test tests/skills/test_tmp_round1_mixed_location.py -q -p no:xdist -s`
verdict: fixed 0e0601ab

The records-only exemption reads only the fix commit. It never reads where
the finding is located. `records` hands `channel` the predicate
`records_only(root, item, f.verdict[1])` (`chain_check.py:1746`), which is
true when every path the commit changed lies under the work item's
directory. `verdict_problems` passes a `fixed` commit that touches any one
of the `location:` paths. So take a finding located at `f.txt:1` and at
`seal/threads/<id>/gaps.md`, closed `fixed <c>` where `<c>` edited
`gaps.md` alone. Both checks pass it. No round reads the code half, and the
pull request is green. The probe below built that branch from the module's
own fixtures and `chain_check.py` exited 0.

This is the common shape, not an edge. The design's own Grounding row for
#1177 counts 4 of its 10 findings as naming a record beside a shipped file.
The design's grounds for the exemption are records-only fixes of findings
about the records (#1045's five verifying rounds). Scope item 5 says "a
`fixed` that touched any other path still owe[s] the round". Its intent is
that a defect in shipped code is read by a round. The sealer's new step-4
sentence sends the sealer to "read the record at HEAD against what the
finding asked". The record says the finding is fixed. The code half is
read by nobody.

The class is every place that states the passing condition by the commit
alone. Each carrier in `location:` says "a `fixed` whose commit touched
only the work item's records". With the narrowed check, each says that the
finding must also be located in the records alone. The design's
`## Rule changes` entry for `docs/the-review-record.md` *What the check
reads at the pull request* states the same condition. It is the framer's
text, and the orchestrator folds it.

```python
# skills/code-review/scripts/chain_check.py, records(): the exemption holds
# only for a finding every one of whose `location:` paths lies under the
# work item's records, fixed by a commit that touched nothing else.
    problems.extend(
        channel(
            rounds,
            lambda f: all(under(q, item) for q in f.paths)
            and records_only(root, item, f.verdict[1]),
        )
    )
```

```python
# tests/skills/test_chain_check.py, class Test_main, beside the two #1148 cases
    @pytest.mark.rule("run-ends-with-verifying-round")
    @pytest.mark.rule("last-record-at-head")
    def test_refuses_a_last_records_code_finding_fixed_in_its_records_alone(
        self, branch, ready, capsys
    ):
        """S4 of #1148: a finding that names a path outside the records owes
        the round, even where its `fixed` commit touched only the records."""
        root, code_sha = branch
        git(root, "rm", "-q", f"{ITEM}/trail/rounds/round-2.md")
        commit(root, "no verifying round")
        write(root, f"{ITEM}/gaps.md", "# overview\n\nthe row, corrected\n")
        fix = commit(root, "the record half alone")
        rel = f"{ITEM}/trail/rounds/round-1.md"
        located = f"`f.txt:1`, `{ITEM}/gaps.md`"
        write(
            root,
            rel,
            record(code_sha, [finding(1, f"fixed {fix[:8]}", location=located)]),
        )
        commit(root, "the fix pass's verdict")
        seal(root)
        code, out = check(root, capsys)
        assert code == 1, out
        line = next(
            ln for ln in out.splitlines() if ln.startswith(f"{rel}:") and "### 1." in ln
        )
        assert chain.VERIFYING_ROUND in line, line
```

```markdown
<!-- README.md:207-213, and the same change in README.ko.md:201-206 -->
A ready pull request fails while a commit outside the work item's records
follows the commit on the last record's `target:` line, or while a finding of
that record reads `rejected`, or `fixed` where the finding names a path
outside the work item's records or its commit touched one — a review cannot
have passed while the fixes that closed its findings went unread. A finding
located in the records alone and fixed in them alone is read by the sealer at
HEAD and owes no round. On a draft it prints and names the verifying round.
```

The new case is seen red against `chain_check.py` at 16056d31 before the
predicate changes, as the probe shows. The other carriers take the same
narrowing in their own words.

answer: `chain_check.py#records` hands `channel` `located_in_records(item, f) and records_only(root, item, f.verdict[1])`, so a `fixed` finding passes in the last record only where every `location:` path lies under the work item's directory and its commit touched nothing else. `test_refuses_a_last_records_code_finding_fixed_in_its_records_alone` failed against the check at 6c3f6482 and passes after (executed), and a mutant of `located_in_records` returning `True` went red (executed). The module docstring's `records` row and the docstrings of `channel` and `records` say the same. The shipped carriers are narrowed in the same commit: `README.md`, `README.ko.md`, `agents/sealer.md` step 4, `skills/code-review/orchestration.md` (the opening of *Orchestrator: the run ends with a verifying round*, its *When* row, the cap paragraph's refusal sentence and the run-ends sentence), `skills/implement/acts.md`'s row and `skills/implement/SKILL.md`'s drain row, with the fragment's sentence and process row. Their pins in `tests/behaviour/test_the_sealer_guarantees.py` and `tests/text/test_the_rules_have_one_owner.py` were rewritten and seen red before the prose changed. `505e76e6` rewords the acts row, which the paste check found sharing a fifteen-word run with the README. `docs/` states the old condition until the settle writes the frame's folded rule change.

### 2. Running `seal pr-body` again on a body 0.25.0 wrote is refused, and the release note says it recovers

severity: should
location: `skills/code-review/scripts/pr_body.py:500-508`, `tests/skills/test_pr_body.py:352-363`, `seal/threads/1793343707-each-document-serves-one-reader/changelog.md:3`, `seal/threads/1793343707-each-document-serves-one-reader/frame/plan.md:75`
evidence: executed `bin/seal pr-body seal/threads/1793343707-each-document-serves-one-reader --body <round scratch>/old-body.md --check`, `bin/seal pr-body seal/threads/1793343707-each-document-serves-one-reader --body <round scratch>/old-body.md`
verdict: fixed 42c85a93

The fragment says a 0.25.0 body "is refused until `seal pr-body` runs
again". The plan's *Operational impact* says the orchestrator runs
`seal pr-body` again and "its own part is then written above the new
line". Phase 5 claimed the plan "already sends the orchestrator to a fresh
run". The code does not do that. `main` calls `split(body)` on any body
file that exists. `split` raises when no line reads `## From the records`
(`pr_body.py:500-508`). A 0.25.0 body has only `## Not from the records`,
so the write is refused exactly as `--check` is. Both runs exited 1, each
printing that no line reads the heading "so the body has no part of its own
to keep", and the file was left as it stood.

A user whose work item is in flight across the update reads the release
note, runs the command, and meets a refusal that names no way out. Contract
rule 14 makes a changed message owe its pin. The plan's sentence is the
framer's, so the orchestrator folds it.

```python
# skills/code-review/scripts/pr_body.py, split()
    raise Refused(
        [
            (
                None,
                0,
                f"no line reads `{HEADING}`, so the body has no part of its own "
                f"to keep: write your part above a line reading `{HEADING}`, or "
                "remove the file, and run the command again",
            )
        ]
    )
```

```python
# tests/skills/test_pr_body.py, Test_split.test_refuses_a_body_with_no_heading_line
        for body in (
            "## What changed\n\n## From the records, really\n",
            "## What changed\n\n## Not from the records\n",
        ):
            with pytest.raises(PR.Refused) as refused:
                PR.split(body)
            assert "or remove the file, and run the command again" in (
                refused.value.causes[0][2]
            )
```

```markdown
<!-- changelog.md:3, the sentence on --check -->
`seal pr-body --check` compares only the part below that line. A body written
by 0.25.0 has no such line, so both `--check` and a new run refuse it until
its own part stands above a `## From the records` line or the file is
removed.
```

answer: `pr_body.py#split`'s refusal now ends `write your part above a line reading `## From the records`, or remove the file, and run the command again`, and `Test_split.test_refuses_a_body_with_no_heading_line` pins that sentence for both bodies it refuses, 0.25.0's among them; the pin was seen red before the message changed, and a mutant dropping "remove the file" went red (executed). `seal pr-body` over a 0.25.0-shaped body exits 1 printing the repair (executed). The fragment's sentence says both runs refuse such a body until its own part stands above the line or the file is removed. `frame/plan.md`'s *Operational impact* line is the framer's fold at 6c3f6482.

### 3. The fragment and the plan state counts that no longer match the tree

severity: should
location: `seal/threads/1793343707-each-document-serves-one-reader/changelog.md:3`, `seal/threads/1793343707-each-document-serves-one-reader/changelog.md:16`, `seal/threads/1793343707-each-document-serves-one-reader/frame/plan.md:78`
evidence: executed `git show fba13ab2:skills/implement/orchestration.md | wc -w`, `git show 183a31b6:skills/implement/orchestration.md | wc -w`, `wc -w skills/implement/orchestration.md`, `.venv/bin/python -I -c '<load skills/settle/scripts/rule_changes.py and hooks/lib/config.py; print each operation pending returns for 1793343707>'`
verdict: fixed 2641c43f

The fragment says `skills/implement/orchestration.md` "drops from 5,971
words to 3,422". Its process row says sessions read "2,549 words" that they
did not need. The release note is read against 0.25.0, where the file has
5,959 words. 5,971 is a mid-branch count at `183a31b6`. At 16056d31 the
file has 3,424 words, because phase 5 edited it after phase 4 measured
3,422. So both numbers are wrong for the reader of the note, and the
difference is 2,535, not 2,549. The plan says the policy changes "through
this design's fourteen rule changes". The parser reads 17 operations for
this work item: the folds at `6be0c1f1`, `195b452f` and `91ebff35` added
three.

These lines are copied by `seal pr-body` and published by the release note.
A count beside the thing it counts is the copy the design removes. The
measurement has its home in `trail/phases/phase-4.md`, which records the
moment it was taken. The fix removes the copies and does not correct them.

```markdown
<!-- changelog.md:3 -->
`skills/implement/orchestration.md` keeps what every run acts on. Its table of
orchestrator acts moves to `skills/implement/acts.md`, and its procedure for a
work item that commits in more than one repository moves to
`skills/implement/multi-repository.md`.
```

```markdown
<!-- changelog.md:16, the Why cell -->
| ... | Every orchestrating session read the acts table, the multi-repository procedure and the routing rows' reasoning, which only a maintainer, a work item across repositories or a reader questioning a criterion needs | ... |
```

The plan's line 78 is the framer's. It reads "through this design's
`## Rule changes`", with no count.

answer: The fragment's sentence and its orchestration row no longer state a word count: the sentence says the file keeps what every run acts on, and the Why cell names the three bodies that moved. The measurement's home is `trail/phases/phase-4.md`. The fragment's other numbers stand: each is a baseline read from released records (0.24.0's 12 of 17, #1177's eleven rows, 0.22.1 to 0.22.4's five rounds), not a count beside the tree. `frame/plan.md:78` is the framer's fold at 6c3f6482.

### 4. The settle's measure has no step in the procedure a settling session follows

severity: should
location: `skills/settle/SKILL.md:219`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:56`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:264`
evidence: executed `grep -n -i 'flow\|measure\|the-review-record\|before the records leave\|count' skills/settle/SKILL.md`
verdict: fixed 0a15911b

Scope item 7 makes the measure the test of the whole redesign: "A release
whose records-alone count does not fall says the structure did not remove
the copies". It is taken "at the settle, before the records leave". Its
home is one `add` to `docs/the-review-record.md` *The run*, with
`check: none reader: the settling session`. Table B keeps
`skills/settle/SKILL.md` unchanged. Its *The settling session's procedure*
is the sequence that session executes. Nothing in it counts round records
or names the flow log; the search printed only unrelated lines. Step 7 runs
`seal settle --apply`, which removes the records. At the first settle the
session writes the rule while settling this design and may act on it. At
every settle after that the rule stands only in a policy section the
procedure never opens, and the records leave uncounted. The command the
design gives leaves with this design at that first settle.

A rule an agent never reaches is a sentence nobody acts on. The step goes
where the reader is. Adding it inside step 7 keeps the step numbers that
step 6 and step 8 cite.

```markdown
<!-- skills/settle/SKILL.md, The settling session's procedure, step 7 -->
7. For each released work item routed through the review chain, count from
   its `trail/rounds/round-*.md` the four numbers
   `docs/the-review-record.md` *The run* names, and post them as that
   section says. Then run `seal settle --apply`, which removes the records.
```

The design's Table B row for `skills/settle/SKILL.md` is the framer's, and
the orchestrator folds it. A pin for the new clause belongs in
`tests/skills/test_settle.py`.

answer: Step 7 of *The settling session's procedure* now counts the four numbers `docs/the-review-record.md` *The run* names for each released work item routed through the review chain, posts them, then runs `seal settle --apply`; step numbers 6 and 8 are unchanged. The pin went into `tests/text/test_settle_reads_before_it_removes.py#test_the_skill_states_the_settling_sessions_procedure`, the case that already holds every step of that procedure in order, not into `tests/skills/test_settle.py`, which tests the script; it was seen red before the step changed, and a mutant of the clause went red (executed). The Table B row is the framer's fold at 6c3f6482.

### 5. The measure's third command counts any path starting with `se` as located in the records

severity: should
location: `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:179`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:183`
evidence: executed `B=$(printf '\140'); printf '%s\n' "location: ${B}seal/README.md:3${B}" "location: ${B}setup.cfg:1${B}" "location: ${B}seal/threads/x/gaps.md:2${B}" | grep -vc "${B}[^s${B}][^${B}]*${B}\|${B}s[^e][^${B}]*${B}"`
verdict: fixed 6c3f6482

The design defines the third count as findings "whose every `location:`
path is under `seal/threads/`". Line 183 says the command counts lines
"whose every path opens with `seal/`". The regex keeps a line when no path
in it starts with a letter other than `s`, or with `s` followed by a letter
other than `e`. Three lines went in: one under `seal/threads/`, one at
`seal/README.md` and one at `setup.cfg`. All three were counted. This
repository's round records hold findings at `seal/` paths outside the
threads directory, two by `git log --all -p` over the round records. The
count is the baseline the next release is judged against, so it has to
count what the rule names. #1177's reading stays 1 with the fix below.

```
git grep -h '^location: ' -- 'seal/threads/<id>/trail/rounds/round-*.md' | sed 's/`seal\/threads\/[^`]*`//g' | grep -vc '`'
```

Line 183 then reads: "The third line deletes every backticked path under
`seal/threads/` and counts the `location:` lines with no backtick left."
Both lines are the framer's, and the orchestrator folds them.

answer: The framer's fold at 6c3f6482 rewrites both lines: the third command deletes every backticked path under `seal/threads/` and counts the `location:` lines with no backtick left. No shipped file states the command; `trail/phases/phase-6.md` quotes the old one as the run it records.

### 6. The change adds more lines than it removes, against scenario S10 and the issue's last *Done when*

severity: must
location: `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:88`, `seal/threads/1793343707-each-document-serves-one-reader/gaps.md:31-39`
evidence: executed `git diff --shortstat fba13ab2...HEAD -- . ':(exclude)seal/threads'`, `git diff --shortstat fba13ab2...HEAD -- . ':(exclude)seal/threads' ':(exclude)tests'`, `git diff --numstat fba13ab2...HEAD -- tests`
verdict: deferred frame/questions.md Q2

S10 says that, outside `seal/threads/`, "deletions exceed insertions". The
issue's bullet reads "the change removes more lines than it adds". The
diff adds 1,128 lines and removes 988. Shipped files outside `tests/` net
−80 (567 added, 647 removed). `tests/` nets +220 (561 added, 341 removed),
and `tests/behaviour/test_waiver_decided_at_start.py` alone adds 133 more
than it removes. Phase 6's numbers are right.

`gaps.md` *Not done* says the change "was neither padded nor trimmed to
meet the count, as the spawn for phase 6 directed". That is the spawn's
account. No policy, frame or test says the scenario may fail, so it is no
grounds for a pass. The criterion is exact and it fails. What to do about
it is a question for a person. The fix pass cannot write a frame sentence,
and it cannot choose which pins to cut. One of these two closes it:

- The owner accepts the miss at the pull request, and the framer rewrites
  S10 to the reading the owner gives. For example: "shipped files outside
  `tests/` remove more lines than they add". `gaps.md` *Not done* keeps
  the numbers.
- A phase removes at least 141 more lines outside `seal/threads/`. Read
  against #1146's cut of phrase pins, the candidates are the new
  phrase-only cases in `test_waiver_decided_at_start.py` and
  `test_the_rules_have_one_owner.py`. Each removal is weighed against
  contract rule 14.

```markdown
<!-- frame/design.md:88, the S10 row, if the owner takes the first option -->
| S10 The release moves the version and removes more than it adds | Given the branch at its last commit, when `git diff --shortstat <base>...HEAD -- . ':(exclude)seal/threads' ':(exclude)tests'` runs, then deletions exceed insertions; `tests/` is reported beside it; `.claude-plugin/plugin.json` reads `0.25.1` in the fragment's commit | `tests/behaviour/test_release_hygiene.py`; `tests/github/test_publish_release_note.py`; both shortstats in the phase record |
```

answer: The owner answers it at the pull request as `frame/questions.md` Q2. Its default is to accept the shortfall: S10 stays as written and fails, and the orchestrator's part of the pull request body states the three counts (1,128 added and 988 removed outside `seal/threads/`; 567 and 647 outside `tests/`; 561 and 341 in `tests/`), so the owner reads a miss and not a pass.

## Confirmations

confirms: none
This is round 1, so no fact was carried from an earlier round. These
claims were re-run here: phase 3's seen-red of the two `chain_check.py`
cases, phase 6's shortstat and measure, and phase 4's word counts. These
were read and not re-run: the seen-red and mutant claims of phases 1, 2, 4
and 5. Phase 3 claimed the two new cases gave `1 failed, 1 passed`
against the old check. With `chain_check.py` at `fba13ab2` they gave
exactly that, and only the records-only case failed (executed).

confirms: none
For a finding located in the records alone, the exemption behaves as the
frame states. A records-only `fixed` in the last record passes. A `fixed`
whose commit also touched `f.txt` is refused at the finding's heading.
`follows` still refuses any later commit outside the work item's
directory. A merge commit or an empty commit makes `touched` list nothing,
so `records_only` is false and the round is still owed: the check fails
closed (read, `skills/code-review/scripts/chain_check.py:1433-1455`).

confirms: none
`pr_body.py` writes the order and the fold the design lays out. `compose`
returns `HEADING`, a blank line, `<details>`, the summary, a blank line,
the sections and `</details>`. `split` returns the orchestrator's part
first. `main` keeps that part byte for byte. `_check` offsets its line
numbers by the part above, which the case pins at body line 13 (read,
`skills/code-review/scripts/pr_body.py:432-530`). Seven narrow modules
passed: `test_pr_body.py`, `test_chain_check.py`, `test_launch.py`,
`test_waiver_decided_at_start.py`, `test_the_rules_have_one_owner.py`,
`test_every_orchestrator_act_names_its_delivery.py` and
`test_a_cited_section_stands_in_its_file.py`, 425 passed, exit 0
(executed).

confirms: none
The direction rule holds for shipped text an agent or a user reads.
`git grep -l 'CONTRIBUTING\|CLAUDE\.md' -- agents templates 'skills/**/*.md'`
prints `skills/update/SKILL.md` alone, and it names the user's own
`CLAUDE.md`. `hooks/lib/launch.py`'s refusal ends at the command to type,
and `tests/hooks/test_launch.py` pins it. The five other names of
`CONTRIBUTING.md` under `hooks/` and `skills/` are comments and
docstrings, and none of those files reads `__doc__` (executed).

confirms: none
The two moved sections are the old ones whole. A `diff` of the base's
*Orchestrator: which of these acts runs itself* against
`skills/implement/acts.md` shows only the opening, the three "files this
file's opening names" substitutions and the five changed rows. A `diff` of
the base's *A work item that commits in more than one repository* against
`skills/implement/multi-repository.md` shows only the opening, the `##`
heading and the citation that replaces "in the shape above" (executed).
All 17 of this design's rule changes parse through
`skills/settle/scripts/rule_changes.py#pending`, the `docs/the-pact.md`
change after the blank line among them (executed). No file under `docs/`
changes on the branch (executed, `git diff --stat`).

confirms: none
`gaps.md`'s row for phase 3 names the proofer. It concerns the four
statements of the records-only exemption at `README.md:207-213`,
`README.ko.md:201-206`, `skills/implement/acts.md:72` and
`skills/implement/SKILL.md:511`. Each states what the check does for a
finding located in the records (read). Finding 1 narrows all four. A
search for the removed facts outside `seal/threads/` and `docs/` found
only the old spellings that tests now assert are absent, and fixtures the
phase records name. The search covered the divergence and fed-back
sections, the asked section, the `Approved` line, `## Not from the
records`, "first part", "above the line", "under that line" and the
crafter's old three-fix lead (executed, `git grep -n -F` on each phrase).

confirms: none
`frame/questions.md` Q1 asks for a stage-1 reading in place of the
behaviour suite, and this round read each changed sentence of the four
agent definitions against the rule it moves or states. The framer's *A
mark is not the answer to a blocked step* and *An orchestrator's reading
of the frame is answered in one exchange* say what
`skills/implement/orchestration.md` *The frame is read against the issue
at the spawn* says: the same three answers, the same bound, and a
rejection as an Alternatives row. The crafter's Job, its step 8 and the
case agree on `gaps.md`'s one trigger. Its *A stop at three failed fixes
is handed back* cites `skills/implement/SKILL.md` *2.*, which holds the
rule with its `check:` line. The proofer's bullet stands on its own words.
The sealer's step 2 reads the part above the line as the orchestrator's,
and step 4 carries finding 1's gap (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| GitHub's rendering of the fold, and of a copied `</details>` inside a sentence, indented, as `<details open>` or as `</DETAILS>`, which the equality test does not refuse | `skills/code-review/scripts/pr_body.py:466-474` | the orchestrator, reading the first body this change writes |
| The behaviour suite over `agents/framer.md`, `agents/crafter.md`, `agents/proofer.md` and `agents/sealer.md`, not run on Q1's default | `seal/threads/1793343707-each-document-serves-one-reader/frame/questions.md` | the owner, at the pull request |
| The full suite, the repository-wide lint and format check | the branch at 16056d31 | the orchestrator, through `seal gate` |
| Cross-platform run 41031172175 at 16056d31 | the tests workflow | the orchestrator |
| A records-only `fixed` that edits `frame/design.md` `## Rule changes` passes with no round, and the settle writes that text into the policy root. The design's A8c weighed a fragment edit, not a rule change | `skills/code-review/scripts/chain_check.py:1450-1455` | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round1_mixed_location.py -q -p no:xdist -s`, one case built from `test_chain_check.py`'s fixtures: a finding located at `f.txt:1` and at the work item's `gaps.md`, fixed by a commit that touched `gaps.md` alone, in the last record, with no verifying round | `chain_check.py` exited 0; `1 passed`; the file and its bytecode were deleted after the run |
| `bin/seal pr-body seal/threads/1793343707-each-document-serves-one-reader --body <round scratch>/old-body.md --check`, then the same without `--check`, over a body in 0.25.0's shape (the copy, `## Not from the records`, the orchestrator's part) | both exited 1 with `refused: old-body.md: no line reads ... so the body has no part of its own to keep`; the file was unchanged |
| `git checkout fba13ab2 -- skills/code-review/scripts/chain_check.py`, then `bin/test tests/skills/test_chain_check.py -q -k 'touched_only_its_records or also_touched_code'`, then the file restored from HEAD | exit 1, `1 failed, 1 passed`, the records-only case failing; `git status --short` empty after the restore |
| `bin/test` over the seven modules named in the third confirmation | exit 0, `425 passed` |
| `git diff --shortstat fba13ab2...HEAD -- . ':(exclude)seal/threads'`, the same with `':(exclude)tests'`, and over `tests` | `60 files changed, 1128 insertions(+), 988 deletions(-)`; `38 files changed, 567 insertions(+), 647 deletions(-)`; `22 files changed, 561 insertions(+), 341 deletions(-)` |
| The measure's four commands over `seal/threads/1793273065-the-core-reaches-no-users-repository/` | 10, 3, 1 and 8 |
| The corrected third command over the same records, and over six sample `location:` lines | 1 for #1177; 2 of 6 for the sample, the two whose every path is under `seal/threads/` |
| `wc -w` of `skills/implement/orchestration.md` at `fba13ab2`, `183a31b6` and HEAD | 5,959; 5,971; 3,424 |
| `rule_changes.pending` over the clone's tree, filtered to this work item | 17 operations, the `docs/the-pact.md` change last |
