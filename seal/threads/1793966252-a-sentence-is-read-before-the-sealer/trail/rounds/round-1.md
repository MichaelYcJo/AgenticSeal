# Review round 1: 1793966252-a-sentence-is-read-before-the-sealer

```seal
target: a817731d3 against origin/release/v0.34.0
```

This round ran under the installed 0.33.0 proofer definition, whose step 3
does not list `routing.md`, `frame/questions.md`, `changelog.md` or `pr.md`.
The spawn prompt asked for the read the branch's `agents/proofer.md` states,
so this round read those seven files whole at `a817731d3` and judged each
sentence against the target. The sections dated to `1359abcb9`
(`frame/design.md` *Grounding*, `frame/plan.md` *Technical context*) were
judged against `1359abcb9`. No earlier round exists, so no fact is carried
and every verdict below is this round's own. No `seal/parity.md` is
declared, so `legacy-parity` does not apply.

## Findings

### 1. The *Grounding* row on a thread's top-level files says no reader lists them, and a reader did at the commit the row is dated to

```seal
severity: should
location: `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/design.md:20`
evidence: executed `git show 1359abcb9:tests/behaviour/test_the_pull_request_language_is_the_repositorys.py | grep -n 'startswith("pr.")'` (line 262); read `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/trail/phases/phase-2.md:22`, `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/plan.md:53`
```

Why it matters: the row says "No reader lists them" and "So a new `pr.md`
is refused by no reader". Its search covered `lib/`, `skills/*/scripts/`
and `.github/scripts/` and did not cover `tests/`. At `1359abcb9`, the commit
the section is dated to, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:262`
already listed every `pr.*.md` of every thread with a name filter that
matches `pr.md`. Phase 2 found that the first committed `pr.md` would have
turned that case red, and it changed the filter (`trail/phases/phase-2.md:22`).

So the sentence is false at its own dated commit, not only at HEAD. Dating a
section protects it against later changes to the tree; it does not protect
a sentence that was wrong when it was written. The orchestrator's row at
`frame/plan.md:53` left it unfolded on the grounds that it is dated, and
that ground does not cover this case. The sealer reads `frame/design.md`
whole and can withhold on the sentence. That is the outcome this work item
exists to prevent.

The snippet replaces the row's cell in `frame/design.md` *Grounding*. The
judgment row at `frame/plan.md:53` records a decision on its date and is
left as it stands.

```markdown
| A thread's top-level files | `git grep` for `listdir`, `scandir`, `glob` and `iterdir` in `lib/`, `skills/*/scripts/` and `.github/scripts/` finds only `trail/rounds/` listings and `pact_check.py`'s glob of `frame/design.md` (executed). The search did not reach `tests/`, where `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_the_existing_mirrors_are_consistent_with_the_rule` lists every `pr.*.md` of every thread by a filter that matches `pr.md`, so a new `pr.md` turns that case red until the filter leaves it out (`trail/phases/phase-2.md`). No other reader refuses a new `pr.md`, and it leaves with its directory at the settle |
```

```seal
verdict: fixed d727b29c5
answer: The finding holds: at 1359abcb9 the case's filter `name.startswith("pr.") and name.endswith(".md")` stood at line 262 and matches `pr.md` (executed). The row is a frame file the crafter does not write, so the orchestrator applied the snippet at d727b29c5 (frame/questions.md Q1 (a)); this pass read frame/design.md:20 at HEAD and it holds the snippet's row.
```

### 2. Phase 3's Status cell names a commit at which the version it delivers does not yet stand

```seal
severity: should
location: `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/plan.md:37`
evidence: executed `git show c64707f4:.claude-plugin/plugin.json | grep version` ("0.33.1"), `git show --stat eb0bd16b`, `git show --stat 22d0599b`; read `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/design.md:35`, `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/trail/phases/phase-3.md:40`, `agents/crafter.md:160-163`
```

Why it matters: the *Phases* row 3 delivers *Scope* item 8, which now says
"the version stands at 0.34.0". Its *Verified by* cell names "the version's
commit after the rename shows it at 0.34.0". Its Status cell still reads
`c64707f4`, and at that commit `.claude-plugin/plugin.json` reads 0.33.1.
Phase 3's own record says `eb0bd16b7` moved the version to 0.34.0 as part
of the phase (`trail/phases/phase-3.md:40`).

`agents/crafter.md` *Each phase closes with its record* says the Status cell
holds the commit. Phase 1 is the precedent in this work item: when a later
commit, `91e05888`, narrowed one of phase 1's sentences, `22d0599b` moved
phase 1's Status cell to it. Phase 3 was reopened for the version move, and
its Status cell was not moved. The orchestrator reads where a work item
stands from the Status column (`skills/implement/orchestration.md`, the
paragraph opening **Where a work item stands is read from `plan.md`'s Status
column**). This cell tells that reader that phase 3 closed before the
version reached the release's number.

```markdown
| 3 | *Scope* items 5, 6 and 8 | `trail/phases/phase-3.md` lists each statement in `agents/` and `skills/` of what a round reads, found by `git grep` and by `agents/proofer.md`'s `check:` targets; `git show --stat` of the commit that adds `changelog.md` shows `.claude-plugin/plugin.json` moved in it, and the version's commit after the rename shows it at 0.34.0; the *Phase boundary* set over the touched files | eb0bd16b |
```

```seal
verdict: fixed 480ff41d8
answer: The finding holds: c64707f4's plugin.json reads 0.33.1 and eb0bd16b7 moved it to 0.34.0 as part of phase 3. The Status cell of frame/plan.md row 3 now reads eb0bd16b, the commit the snippet names; the same commit closes the gaps.md row round 1 confirmed and opens one for the 0.34.0 definition alone, since that crafter ran with the move named in its spawn prompt.
```

### 3. The chosen approach's row says the one new check compares bytes, and it compares lines with their line ends removed

```seal
severity: should
location: `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/plan.md:20`
evidence: read `skills/code-review/scripts/pr_body.py:769-786`, `lib/blocks.py:382-388`, `skills/code-review/scripts/pr_body.py:736`
```

Why it matters: the *Alternatives considered* row of the chosen approach
ends "the only check it adds compares bytes". The check is
`pr_body.py#_first_part`. It compares `READER.gfm_lines(head)` with
`READER.gfm_lines(own)`, and `lib/blocks.py:388` strips `\r` and `\n` from
each line when `keepends` is false. So a body whose first part differs from
`pr.md` only in its line ends, such as CRLF against LF, passes `--check`.

The design's own description of the check is correct: *Data & interfaces*
says `--check` "refuses at each line above the heading where the body and
`pr.md` differ". The plan's sentence is the one statement that claims more.
The row is the grounds for rejecting a quote script, and the settle weighs
the mechanism by what that row says it checks. The other statement in the
same words, `frame/design.md:9` ("byte for byte"), stands in the *Grounding*
section dated to `1359abcb9`. There it states why the fact may be gated, not
what the code compares. The snippet leaves it as it stands.

```markdown
| `pr.md` is a committed record that `seal pr-body` writes above the heading and every round reads (*Scope* items 2, 3 and 5) | The scenario under *Technical context* | Chosen. It meets #1415 *Done when*'s second line as the issue wrote it, and the only check it adds compares the body's lines above the heading with `pr.md`'s, line ends aside |
```

```seal
verdict: fixed d727b29c5
answer: The finding holds: `_first_part` compares `READER.gfm_lines(head)` with `READER.gfm_lines(own)`, and `lib/blocks.py#gfm_lines` strips `\r` and `\n` unless `keepends` is set (read). The row is a frame file the crafter does not write, so the orchestrator applied the snippet at d727b29c5 (frame/questions.md Q1 (a)); this pass read frame/plan.md:20 at HEAD and it holds the snippet's verdict.
```

### 4. The refusal of a `pr.md` that is not UTF-8 text is new behaviour, and no case holds it

```seal
severity: should
location: `skills/code-review/scripts/pr_body.py:364-369`, `tests/skills/test_pr_body.py:564`
evidence: executed `grep -rn "cannot be read as UTF-8" tests/` (no hit), `grep -n "UTF-8\|xff" tests/skills/test_pr_body.py` (no case for the refusal)
```

Why it matters: `read_own` is new in this diff. It refuses a `pr.md` that
does not decode as UTF-8 at `pr.md`, line 0, with "cannot be read as UTF-8
text". Without the `except`, a `UnicodeDecodeError` would escape `main`,
which catches `Refused` alone, and the sealer would get a traceback instead
of a `refused:` line to copy into its verdict. `Test_read_own` covers the
added line end and the heading refusal, and no case reaches this branch,
so a change that dropped the `except` would pass the suite (read, not run).
The two older decode refusals
in the same file (`pr_body.py:329` for a record, `:759` for the body file)
have no case either. That is the module's current state, not a ground
that excuses a new branch with no case.

```python
    def test_refuses_a_pr_md_that_is_not_utf_8(self, tmp_path):
        """A `pr.md` that does not decode as UTF-8 is refused at `pr.md`,
        with no line, rather than raising out of the command."""
        item = item_of(tmp_path, RECORDS)
        (item / "pr.md").write_bytes(b"Closes #1.\n\xff\n")
        with pytest.raises(PR.Refused) as refused:
            PR.read_own(str(item))
        ((where, line, why),) = refused.value.causes
        assert (where, line) == ("pr.md", 0)
        assert why.startswith("cannot be read as UTF-8 text ("), why
```

The case belongs in `Test_read_own` in `tests/skills/test_pr_body.py`. The
fix pass still owes contract rule 15: see the case red with the `except`
branch in `read_own` removed, and read its failing line.

```seal
verdict: fixed 960fa60cb
answer: The finding holds. `Test_read_own::test_refuses_a_pr_md_that_is_not_utf_8` is the snippet, with its docstring naming how it was seen red. Seen red: `seal mutate` replaced `except (OSError, UnicodeDecodeError) as exc:` with `except OSError as exc:` in `read_own`, and the case failed at tests/skills/test_pr_body.py:599, `PR.read_own(str(item))` inside `pytest.raises(PR.Refused)`, on `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff` (executed, verdict red; pr_body.py restored by seal mutate, `git diff --quiet` exit 0). The two older decode refusals at pr_body.py:329 and :759 stay without a case, as the finding leaves them. c09c9ec71 adds the refusal to changelog.md's list of what both forms refuse.
```

## Confirmations

What matched: each of the seven quotes in `pr.md` stands word for word, with
runs of whitespace collapsed, at the source its coordinate names (read).
Quote 1 is `changelog.md:3`, the first item's bold lead, without the bold
markers. Quotes 2 to 4 are `changelog.md:6`, `:7` and `:8`. Quote 5 is
`frame/plan.md:55`, the prefix row. Quote 6 is `frame/questions.md:14`,
option (a). Quote 7 is `frame/questions.md:15`, the *Default until answered*
cell. The file holds no heading or sentence of the orchestrator's own, and
its `Closes` lines and attribution line match *Data & interfaces*.

What matched: `pr.md` was committed in `a817731d3`, after phase 3's last
record commit and before this round, as *Scope* item 2 and
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals* require (executed: `git log --oneline 33ced573b..a817731d3`).

What matched: every `from:` of `frame/design.md` `## Rule changes` stands
once in its file at the target, with whitespace collapsed (executed: a
read-only count over the six `docs/` files). The *Out* list names rung 4 of
`docs/running/the-run.md` *The run*, which is the table row at
`docs/running/the-run.md:51`. The `## Rule changes` operation on that file
changes the automation paragraph at `:61-62`, so the two do not conflict
(read).

What matched: the coordinates in `frame/plan.md` *Technical context* hold at
`1359abcb9`: `pr_body.py#split` at 689, `#_check` at 729, `#main` at 771,
`evals/scripts/rule_cases.py:827`, `agents/sealer.md:68-80`,
`agents/proofer.md:30-32` and `:129`, `skills/code-review/orchestration.md:115`,
`:366-369` and `:385`, `skills/implement/orchestration.md:109` and `:373`,
`skills/commit-pr-convention/SKILL.md:236`, `skills/verify/orchestration.md:414`,
`templates/records/sdd-plan.md:23` and `agents/crafter.md:19-25`. The
*Grounding* row on `agents/crafter.md` also holds: `git show v0.32.6:agents/crafter.md | grep -c 'Read whole'`
gives 1, and `5005355d8` resolves (executed).

What matched: `gaps.md` `## Not verified` row 1 names this round as its
answerer. `fe8df522` adds `changelog.md` and moves `.claude-plugin/plugin.json`
from 0.33.0 to 0.33.1 in one commit, and `eb0bd16b` moves it to 0.34.0
(executed: `git show --stat` of each). So the last phase's crafter made the
move in the commit that adds `changelog.md`, as `agents/crafter.md` *Job*
now asks. Closing the row is its writer's act. Finding 2 covers the Status
cell of that phase.

What matched: *Scope* items 1 to 8 each name what the diff holds (read
against `git diff 33ced573b..a817731d3`). Item 1: `agents/crafter.md:23-29`,
`skills/implement/orchestration.md` **Which branch the pull request lands
on** and **Where an entry accumulates**, and the `sdd-plan.md` placeholder.
Item 2: the six carriers it lists. Item 3: `pr_body.py` `read_own`,
`_first_part`, `_check` and the module docstring, and the sealer scaffolds
under `evals/behaviour/sealer/`. Item 4: `skills/verify/orchestration.md`
and `skills/commit-pr-convention/SKILL.md`. Item 5: `agents/proofer.md`
step 3 and its new rule, the two rows of `skills/code-review/orchestration.md`
and both READMEs. Item 6: no change to the crafter's read. Item 7:
`agents/framer.md:191` under `## Rules`. Item 8: as finding 2 qualifies.

What matched: the claims about the tickets in `changelog.md` *Process
changes* rows 3 and 4 and in `frame/design.md` *User scenarios &
acceptance* match the issue bodies. #1415 *What the sealer caught in #1376*
names the `frame/questions.md` Q1 sentence and the fragment sentence. #1401
counts eight of twelve stale copies as a count or an ordinal, and its *Done
when* asks for fewer than eight (executed: `gh issue view 1415` and
`gh issue view 1401`). `frame/plan.md` *Judgments of the run*, the prefix
row, holds: `release/v0.33.1` is gone from the remote, `release/v0.34.0` is
at `33ced573b`, and the `release: 0.34.0` milestone is open (executed:
`git ls-remote --heads origin 'release/*'` and `gh api .../milestones`).

What matched: `f98ac0c3` took a paragraph out of `gaps.md` `## Not done`,
not a row of `## Not verified`. The paragraph said no `## Rule changes`
operation changes the bold lead of `docs/forms/the-guarantee.md`. That
operation now stands at `frame/design.md:139-146`, so the paragraph was
corrected in place, and the range diff, where `gaps.md` is new, shows no
row leaving (read).

What matched: `chain_check.py --worktree` printed one notice on the frame:
"seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/design.md:142
a test pins text this operation takes out of `docs/forms/the-guarantee.md`:
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:134`
holds "in the repository's language", and the `to` does not" (executed).
That case reads `skills/commit-pr-convention/SKILL.md`
(`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:30`),
which keeps the phrase once, and it never reads
`docs/forms/the-guarantee.md` (read). The settle's change to the guarantee
document leaves the pinned file as it is. So the notice names no pin of this
operation's wording and no copy, and it is no finding.

What matched: the new cases in `tests/skills/test_pr_body.py` each cover a
branch their group did not: the written body from `pr.md`, the three
first-part mismatches, the absent `pr.md` under both forms, and the two
`read_own` cases. The narrow run of the modules of this slice passed
(executed, below). It is not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the lint and the format check. This round ran only the narrow modules below, so the suite stands `unverified` | `seal/config.md` *Broad gate* | the orchestrator, at its broad run after the rounds settle |
| Where the gate lines the orchestrator is told to "Quote, as printed" go. The paragraph names no destination. Before this change, the orchestrator's first part of the body could hold the broad run's printed figures. Now `pr.md` holds no sentence of the orchestrator's own and is written before the gate runs. The diff did not touch the paragraph, and phase 2's census terms did not reach it | `skills/code-review/orchestration.md:450-455` | the orchestrator, or the owner where it means the pull request body |
| Whether the sealer evals and `evals/behaviour/proofer/rule-proofer-one-finding/` still reach their verdicts. No paid eval ran | `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/frame/questions.md:15`, `seal/threads/1793966252-a-sentence-is-read-before-the-sealer/gaps.md:12` | the owner, at the milestone's paid run |

## Probes

No probe file was written. The commands below ran in the clone.

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py tests/evals/test_rule_cases.py tests/behaviour/test_evals_layout.py tests/behaviour/test_the_sealer_guarantees.py tests/text/test_the_chain_section_has_one_shape.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py tests/text/test_the_rules_have_one_owner.py -q` | 245 passed, exit 0 |
| a read-only `python3 -I -c` count of each `## Rule changes` `from:` in its `docs/` file, whitespace collapsed | each count 1 |
