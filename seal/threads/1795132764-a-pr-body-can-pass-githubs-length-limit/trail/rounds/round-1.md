# Review round 1: 1795132764-a-pr-body-can-pass-githubs-length-limit

```seal
target: 6a135ec96 against release/v0.38.3
```

The round reviewed the whole diff `fab41dc91..6a135ec96`. `fab41dc91` is the merge base with `origin/release/v0.38.3`, which has since moved to `c63d0b070` by #1557's merge alone. The review ran in a `git clone --no-local` of the repository at `6a135ec96`, in the round's scratch directory. No earlier round exists, so no fact was carried and every fact below was established this round. The issue was read with `gh issue view 1559 --json title,body,comments`, and its *Decision* and *Done when* are what the build was judged against. Each work item record named in the proofer's step 3 was read whole at `6a135ec96`, and so was `trail/phases/phase-1.md`. No `pr.<lang>.md` stands: both language keys of `seal/config.json` read `English`.

## Findings

### 1. The length refusal reports a body length that counts the seal mark's room, and calls a body GitHub would keep "past GitHub's 65,536"

```seal
severity: should
location: `skills/code-review/scripts/pr_body.py:307-313`, `skills/code-review/scripts/pr_body.py:944-983`, `tests/skills/test_pr_body.py:333-341`, `tests/skills/test_pr_body.py:1623-1660`, `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/changelog.md:5`
evidence: executed `bin/test tests/skills/test_tmp_round1.py -q -s -p no:xdist` (probe `test_tmp_refusal_names_a_length_the_body_does_not_have`); read `skills/code-review/scripts/pr_body.py:931-983`
```

Why it matters: `_folded` adds `room` to the length it measures (`pr_body.py:959-968`). `_room` gives 114 units for the mark's line and its blank line wherever no mark is written (`pr_body.py:931-942`). The refusal then formats that same `length` into `TOO_LONG` as "the body would be {length:,} characters ... past GitHub's 65,536" (`pr_body.py:309-313`, `:982`). Reserving the room is the design's choice (D4), and refusing at that length is D5. But the number the line prints is not the body's length where the mark is not written, and the line then calls the body past GitHub's limit. The probe built records whose body, folded as far as it needs and written with no mark, measures 65,526 units. `compose` refused it as "the body would be 65,640 characters ... past GitHub's 65,536". A person who reads that line is told something false about the body GitHub would receive. The changelog repeats the claim: "The line gives the body's length" (`changelog.md:5`). S5's case pins the number with the room in it (`test_pr_body.py:333-341`, where the comment does say so, and `:1648-1655`). The case does not pin the wording that would tell a reader about the room.

The fix names the room in the line, and the statements that stand on the line change with it. The snippet covers `TOO_LONG` and `_folded`'s docstring. The fix pass also owes three more. S5's expected `said` at `test_pr_body.py:1648-1655` takes the new words. `changelog.md:5` reads "The line gives the body's length, the seal mark's line counted whether or not it is written, and the length of each first-part file and of `changelog.md`". D5 at `frame/design.md:74` says "`why` gives the body's length"; that is a frame sentence, and the fix pass names its departure from it in its close.

```python
# The refusal on the work item's directory where folding every section that
# a fold shortens leaves the body, with the seal mark's room, past `LIMIT`.
TOO_LONG = (
    "the body would be {length:,} characters, the seal mark's line counted "
    "whether or not it is written, with every section after "
    f"`{CHANGED}` folded that a fold shortens, past GitHub's {LIMIT:,}; "
    "{files}, so {which} is shortened before `seal pr-body` runs again"
)
```

In `_folded`'s docstring, `pr_body.py:954-956`:

```python
    not folded. Refused on the work item's directory where the body still
    passes `LIMIT`, naming its length with ROOM counted, each file of PARTS
    and the changelog of TEXTS with theirs."""
```

### 2. The changelog's *Updating* paragraph says only a body past GitHub's limit folds, so no open pull request changes

```seal
severity: should
location: `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/changelog.md:7`
evidence: executed `bin/test tests/skills/test_tmp_round1.py -q -s -p no:xdist` (probe `test_tmp_a_body_within_the_limit_folds`); executed `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/evals/test_rule_cases.py -q -p no:xdist` (S10's case `test_counts_a_character_outside_the_basic_plane_as_two`); read `skills/code-review/scripts/pr_body.py:834-838`, `skills/code-review/scripts/pr_body.py:931-942`
```

Why it matters: the paragraph reads "Only a body past GitHub's limit folds, and GitHub refused such a body before this release, so no open pull request changes." The code folds in two more cases. The first is a body within 114 units of the limit with no mark written, because the fold measures with the mark's room (D4). The probe composed records whose unfolded body measures 65,486 units, which GitHub keeps, and `compose` folded `## Not verified`. The second is a body whose code-point count fits and whose UTF-16 count does not (D1). That count is the one G7 reports GitHub uses, and S10's case is built on exactly such a body. An open pull request in either band was sent under 0.38.2. The orchestrator reruns `seal pr-body` before every `gh api -X PATCH` of the body (`skills/code-review/orchestration.md:442-443`), and under 0.38.3 the rerun folds. A `hygiene.yml` pinned to 0.38.2 composes no fold, and so refuses it. The paragraph tells that reader no action is needed.

```markdown
Updating: where `seal pr-checks install` wrote `.github/workflows/hygiene.yml` pinned to 0.38.2 or earlier, the pull request's check composes no fold, and it refuses a folded body at its first folded section. A body folds only where it would pass GitHub's limit counted in UTF-16 code units with room for the seal mark's line. So an open pull request changes only where its body came within that room of the limit, or held characters outside the Basic Multilingual Plane. To open or update one whose body folds, run `seal pr-checks remove` and then `seal pr-checks install` once the plugin is 0.38.3, and commit the result.
```

### 3. `orchestration.md` still lists the places a `refused:` line of `seal pr-body` names without the work item's directory, which the build's length refusal names

```seal
severity: should
location: `skills/code-review/orchestration.md:434-437`, `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/frame/design.md:43`
evidence: read `skills/code-review/orchestration.md:426-446`, `skills/code-review/scripts/pr_body.py:116-121`, `skills/code-review/scripts/pr_body.py:978-983`, `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/frame/design.md:43`; executed `git show 6b703783b --stat`
```

Why it matters: this answers the orchestrator's reading it asked this round to judge. The sentence at `orchestration.md:434-437` reads "On exit 1 its `refused:` lines name a record's file and line, `pr.md` and `pr.<lang>.md` among the records, or a language key `config.json` lacks: repair that record or write that key". The build adds `TOO_LONG`. It is refused as `("", 0, why)` (`pr_body.py:983`), which `_place` prints as `seal/threads/<id>`, the work item's directory with no line. That place is none of the three the sentence lists. The build itself treated the list as a fact to keep whole. Commit `6b703783b` added "the work item's directory" to `pr_body.py`'s *Exit* paragraph (`pr_body.py:116-121`), and its message says the language keys' refusals already stood there. `orchestration.md` states the same fact, and contract rule 19 asks the same change to correct every other statement of it. The orchestrator is the party that reads this sentence at the step, and the sentence offers it no repair for a line on the directory. *Scope*'s Out bullet (`frame/design.md:43`) leaves the file out because "the refusal ... names its own repair in its text". That argues against adding a new sentence. It does not cover leaving a closed list that the build made incomplete. The fix rewrites the list in place, and adds no sentence.

The language keys' directory refusals, `NO_TRANSLATION` and `TRANSLATIONS`, already stood there before the build. The list covered them only in spirit, through "`pr.<lang>.md` among the records". The fix covers them too.

The fix touches one more statement. The fix pass corrects `frame/design.md:43`, or names in its close that it departs from it. That is how the phase record handled `chain_check.py#body`'s docstring.

```markdown
whatever the file held. On exit 1 its `refused:` lines name a record's file
and line, `pr.md` and `pr.<lang>.md` among the records, a language key
`config.json` lacks, or the work item's directory with the files to repair
named in the line: repair that record or write that key, commit it, and run
the command again.
```

### 4. The one-file form of the length refusal holds no case, and `gaps.md` says one would need a fixture

```seal
severity: should
location: `tests/skills/test_pr_body.py:438`, `skills/code-review/scripts/pr_body.py:980`, `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/gaps.md:12`
evidence: executed `bin/test tests/skills/test_tmp_round1_snippet.py -q -p no:xdist` (the case below, passing at the target); read `skills/code-review/scripts/pr_body.py:976-983`, `tests/skills/test_pr_body.py:1623-1660`
```

Why it matters: `which = "one of them" if len(held) > 1 else "it"` (`pr_body.py:980`) chooses the words a person reads, and the diff added it. Only the three-file form is pinned (`test_pr_body.py:1623-1660`). A mutant that always writes "one of them" passes every case. Contract rule 14 asks that a changed message be pinned. The *Regression test* row of `skills/code-review/SKILL.md` makes a behaviour the diff changed with no case holding it a `should`. `gaps.md:12` declines the case because "a case for the other shape would add a fixture for one word". That claim does not hold. One `compose` call over `RECORDS` without `changelog.md` reaches the branch, and the probe ran the case below green at `6a135ec96`. A record of the `Not done` section is not a `## Not verified` row, so the fix pass rewrites or removes the paragraph at `gaps.md:12` once the case lands. The case's asserted ending does not change under finding 1's fix.

```python
    def test_refuses_a_first_part_alone_past_the_limit(self):
        """D5 of #1559. Where the first part alone passes the limit and the
        work item holds no `changelog.md`, the refusal names the one file
        and asks for it to be shortened."""
        texts = {rel: text for rel, text in RECORDS.items() if rel != "changelog.md"}
        own = "p" * 70000 + "\n"
        with pytest.raises(PR.Refused) as refused:
            PR.compose(NAME, texts, parts=[("pr.md", own)])
        [(where, line, why)] = refused.value.causes
        assert (where, line) == ("", 0)
        assert why.endswith(
            f"; `pr.md` holds {units(own):,}, so it is shortened before "
            "`seal pr-body` runs again"
        )
```

## Confirmations

What matched: the issue's *Decision* holds in the code. `_folded` folds whole sections from the longest down until the body fits, ties going to the earlier one (`pr_body.py:969-975`). `## What changed` stands in `top` and never in `SECTIONS` (`pr_body.py:824-831`, `:885-889`). `compared` composes through the same `_unfolded` and `_folded` as `main` (`pr_body.py:1150-1157`, `:1226-1229`). Read, and executed through S1, S2 and S7 in the narrow run.

What matched: *Done when*. A folded body measures within `LIMIT` and the run names the folded sections (S1 and S6). `--check` and the body arm accept the folded body and refuse an edited or unfolded one (S6 and S7). The issue's "for any work item" cannot hold under its own *Decision*, which keeps `## What changed` whole, and the build answers it with D5's refusal before the seal. That reading stands in `frame/design.md` *Scope* item 2 and `frame/plan.md` *Alternatives considered* row 5. Executed in the narrow run, and read.

What matched: the phase record's `seen red` claims, sampled on two guards. A mutation in the clone gave the tie key `(-whole[i], -i)`, and `test_folds_the_earlier_of_two_sections_of_one_length` failed with `## Not verified` copied whole. A second mutation removed `_room`'s `if mark: return 0`, and `test_folds_the_same_sections_with_the_mark_and_without` failed with the marked body folding. Each failing line names the guard. Executed, and the clone was restored with `git checkout`.

What matched: S9's search, `git grep -n "nothing here repeats it" -- skills/code-review/scripts/pr_body.py`, exits 1. Executed.

What matched: the phase record's seventh item, the departure on `chain_check.py#body`. The arm's code is unchanged, and only its docstring names the fold's sentence as a notice (`chain_check.py:1827-1832`). Read.

What matched: the eight quotes of `pr.md` were each found word for word at the coordinate they name, in `frame/questions.md` row Q1, in `frame/plan.md` *Alternatives considered* row 3 and *Judgments of the run*, and in `trail/phases/phase-1.md` items two and seven. Read.

What matched: S7's case sets `LIMIT` on `PR_BODY`, which `tests/skills/test_chain_check.py:3156-3159` loads as its own module instance. `chain_check.py#pr_body_reader` loads another, so the patch reaches `composed_body` and not the arm, and the case's refusal is real. Read.

What matched: the new cases of `Test_compose`, `Test_main` and `Test_body` each hold a behaviour no earlier case of their group held: the fold, the tie, the mark's room, the first part's measure, the refusal over folded lines, the UTF-16 count, the length refusal, the fold's line and the arm's notice. Read.

`frame/design.md:71`, in D2, lacks a full stop between "copies from it" and "It names no commit". The sentence reads badly and misleads no one, so it is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub counts a line end as one character, or counts the body after turning each LF into CRLF. Q1's measurement, as `frame/questions.md` writes it, sends one-line bodies and cannot tell. A body of many lines folded to 65,536 units would be refused under the second count | `seal/threads/1795132764-a-pr-body-can-pass-githubs-length-limit/frame/questions.md:14` | a measurement by whoever may post to a scratch pull request, with a body of many short lines added to Q1's |
| The full suite, the repository-wide lint and the format check at the work item's HEAD. The crafter's `gaps.md:7` labels them not verified and names the orchestrator, which is honest; this round ran only the three modules below | `seal/config.json` `Broad gate` | the orchestrator's broad run once the rounds settle, then the sealer's spawn |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/evals/test_rule_cases.py -q -p no:xdist`, in the clone at `6a135ec96` | exit 0, 354 passed |
| `bin/test tests/skills/test_tmp_round1.py -q -s -p no:xdist` | exit 0, 2 passed. The mark's room is 114. A body measuring 65,526 units with no mark was refused as "the body would be 65,640 characters". An unfolded body of 65,486 units folded `## Not verified` |
| `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k "earlier_of_two_sections_of_one_length or same_sections_with_the_mark"`, with the tie key made `(-whole[i], -i)` and `_room`'s `if mark: return 0` removed | exit 1, 2 failed, each on the line its guard holds; the clone restored with `git checkout` |
| `bin/test tests/skills/test_tmp_round1_snippet.py -q -p no:xdist` | exit 0, 1 passed: finding 4's case holds at `6a135ec96` |
| `git grep -n "nothing here repeats it" -- skills/code-review/scripts/pr_body.py` | exit 1, no line |
