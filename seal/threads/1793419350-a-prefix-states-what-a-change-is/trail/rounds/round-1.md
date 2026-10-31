# Review round 1: 1793419350-a-prefix-states-what-a-change-is

target: 45936903 against release/v0.26.0

This round reads the branch from `f80f48e6` to `45936903`: the build commit
`c6ed2331`, the renames in `3c2012fe`, and the records and fragment in
`45936903`, against the frame (`frame/design.md`, `frame/plan.md`,
`frame/questions.md`). It is round 1, so no fact is carried from an earlier
record. The range was re-established with `git log --oneline`. The crafter's
seen-red claim was run again (`## Probes`). The core sentence that the
release check's comment on `FEAT` cites is on #1167's branch and not on this
base, and no finding counts its absence. No `seal/parity.md` is declared, so
the record has no `original:` line.

## Findings

### 1. Under the first-row rule `perf:` is never reached, and a tests-only change that adds a case reads as `fix:`

severity: should
location: `skills/commit-pr-convention/SKILL.md:118-128`
evidence: read `skills/commit-pr-convention/SKILL.md:118-128`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:64-74`
verdict: open

The skill now says a change takes the first row that fits, read from the
top, and a change two rows fit takes the higher one (`:118-120`). The
`refactor:` row (`:126`) reads "the same kinds of outcome, reached another
way ... nobody gains anything to use or to meet". A change that makes the
same behaviour faster fits those words whole, and `refactor:` stands above
`perf:` (`:127`). A writer who applies the first-row sentence titles every
speed-up `refactor:`. A writer who reads the `perf:` row titles it `perf:`.
That is two answers, which the rewrite exists to prevent.

`test:` has the same defect in part. The `fix:` row (`:125`) ends "a check
that starts refusing what its stated rule always refused is here". A
commit that only adds a test case pinning a rule already stated is such a
check, and `fix:` stands above `test:` (`:128`). The old table had no
first-row rule, so the order did not decide anything. Now it does. The
frame's table (`frame/design.md:64-74`) carries the same order, so the build
holds to the frame, and the defect is the frame's.

The fix puts the two rows that fit only a whole change of one kind first.
Neither can take a part of a larger change, so the sentence about stopping
at `feat:` still holds.

```markdown
**A change takes the first row that fits, read from the top.** A change two
rows fit takes the higher one, so a writer who finds one part of the change
that adds something stops at `feat:`. `test:` and `perf:` stand first
because each fits only a change that is wholly that kind, and the rows
below them would otherwise take it.

| prefix | when |
|---|---|
| `test:` | tests only |
| `perf:` | the same behaviour, faster, and nothing else |
| `feat:` | after the change, a user or a party has something to use or to meet that nothing gave before: a command, a record format or a field in one, a step, a reading, or a refusal on a rule the change itself states |
| `fix:` | behaviour existed and was wrong against a rule already stated in the tree, and the change makes it match; a check that starts refusing what its stated rule always refused is here |
| `refactor:` | the same kinds of outcome, reached another way: which party holds a judgment, a script that stops refusing what an agent now reads, a sequence rewritten as guidance, a structure moved; nobody gains anything to use or to meet |
| `docs:` | text no party acts on: an explanation, a README, a comment |
| `chore:` | release preparation, such as the version move, the changelog fold and the settle; configuration and dependencies that tell no party to do anything new; a commit that writes only a work item's own records |
```

answer:

### 2. The `chore:` row names the settle and a work item's records, and the two sentences under the table say text a party acts on is never `chore:`

severity: should
location: `skills/commit-pr-convention/SKILL.md:130`, `skills/commit-pr-convention/SKILL.md:136-142`
evidence: read `skills/commit-pr-convention/SKILL.md:126-142`, `seal/threads/1793419350-a-prefix-states-what-a-change-is/frame/design.md:74`
verdict: open

The `chore:` row (`:130`) names "the settle" and "a commit that writes only
a work item's own records". Both write text a party reads and acts on. A
frame is what the crafter builds against, and a round record is what the
fix pass answers. The settle rewrites the policy documents that every party
reads first. The paragraph at `:136-139` says text a party reads and acts on
is behaviour, and a change to it takes `feat:`, `fix:` or `refactor:`,
"never `docs:` or `chore:`". Its list says "such as", so it is not closed.
The sentence at `:141-142` says `chore:` is never a change a party acts on.
The first-row rule points the same way: the settle moves a rule from a frame
into a policy document, which is "a structure moved" in the `refactor:` row,
and that row stands above `chore:`.

So a writer committing a frame or a settle gets `chore:` from the row and
`feat:`, `fix:` or `refactor:` from the two sentences and the row order.
This repository's own record commits on this branch are titled `chore:`
(`48adaf9b`, `9a0e06ea`, `45936903`), so the row is the intended reading. The
sentences do not say so, and the skill ships to other repositories, whose
writers have only the text.

```markdown
**Text a party reads and acts on is behaviour.** A skill, an agent
definition, a template a party fills and a hook's message are such text, so
a change to one takes `feat:`, `fix:` or `refactor:`, and never `docs:` or
`chore:`. Two writes take `chore:` although a party reads them, whichever
row above also fits them, and the `chore:` row names both: a work item's own
records, which only that item's parties read and which leave with it, and
the settle, which writes into the policy documents what the released work
items' frames already decided.

**Apart from those two, `chore:` is never a change a party acts on**: not a
check, a gate, a record's shape or a process step.
```

answer:

### 3. The branch-name examples teach two prefixes the rewritten table refuses

severity: should
location: `skills/commit-pr-convention/SKILL.md:271-274`
evidence: read `skills/commit-pr-convention/SKILL.md:261-274`, `skills/commit-pr-convention/SKILL.md:136-142`
verdict: open

*Branch names* says a branch name takes the same prefix vocabulary as the
commits (`:261`), and its two examples are
`chore/940-on-demand-files-state-the-current-rule` and
`docs/the-merge-rule-is-enforced-now` (`:272-273`). The first slug is a
change to text a party reads and acts on. `:136-139` now says such a change
is never `chore:`. The second slug is a rule now enforced, which is a
refusal: `fix:` where the rule stood before, `feat:` where the change states
it. It is never `docs:`, which is "text no party acts on". A writer who
copies an example learns the default the rewrite removes. Contract rule 19
asks that a change remove what stood on the old fact in the same commit.
The frame's rule change for `docs/issues-and-milestones.md`'s example title
shows the frame meant to do this, and these two examples were not on its
list.

```
fix/940-on-demand-files-state-the-current-rule
docs/the-readme-says-how-to-install
```

answer:

### 4. The missing-milestone warning was reworded and no case pins the new words

severity: should
location: `tests/github/test_release_completeness_check.py:339`, `tests/github/test_release_completeness_check.py:359`, `.github/scripts/release_completeness_check.py:372-381`
evidence: read `.github/scripts/release_completeness_check.py:372-381`, `tests/github/test_release_completeness_check.py:319-360`
verdict: open

The crafter's departure 4 (`trail/phases/phase-1.md`) rewrote the
`::warning::` line from "this run verified NOTHING ... Passing anyway" to "the
milestone reading verified NOTHING ... That reading passes anyway". The
reason is right: the run can now exit 1 on the version reading after this
line prints, and the old words would then tell the person reading the log
that a failing run passed. The claim "the pinned words `verified NOTHING`
stay" is also true. But those words are in both the old and the new line, so
both cases that read the warning (`:339`, `:359`) pass on the old text. An
edit that puts "Passing anyway" back beside an exit 1 leaves the module
green. Contract rule 14 asks that a changed message have a case that pins
the new text.

```python
        # in test_a_milestone_that_does_not_exist_says_it_verified_nothing
        assert m.main() == 0
        out = capsys.readouterr().out
        assert "the milestone reading verified NOTHING" in out, out
        assert "That reading passes anyway" in out, out
        assert MILESTONE in out

        # in test_a_feat_in_a_patch_refuses_where_the_milestone_does_not_exist
        assert m.main() == 1
        out = capsys.readouterr().out
        assert "the milestone reading verified NOTHING" in out, out
        assert "Passing anyway" not in out, out
        assert "::error::" in out and "`feat: a thing (#100)`" in out, out
```

answer:

## Confirmations

confirms: none
The table gives one answer for the two cases the frame names. #1167's
*Scope* items 11 and 12 add a record section and a reading in `seal settle`'s
dry run. The `feat:` row names "a record format or a field in one" and "a
reading" (`skills/commit-pr-convention/SKILL.md:124`), and the first-row
sentence (`:118-120`) stops the writer there, whatever share of the change is
a refactor. #1198 adds a record format and the commands that build it, the
same row. The frame departs from the owner's note on #1167, and it states the
grounds (`frame/design.md` *The first cases*, `frame/plan.md` A10): the note
weighs the bulk, and the table decides by the first row any part fits. Read.

confirms: none
S9 holds: a change to what a check refuses is never `chore:`
(`skills/commit-pr-convention/SKILL.md:141-142`), and the `feat:` and `fix:`
rows separate a refusal on a new rule from one on a rule already stated
(`:124-125`, `:132-133`). Read.

confirms: none
The not-read naming stays within the scope where the reading reads that
form. `judge_feat` reads the first word of every subject in the release
branch's range, in a patch and in a minor
(`.github/scripts/release_completeness_check.py:312-313`). A near spelling
is named only among those subjects, after the counted ones are excluded, and
it changes no exit code (`:313`, `:342`). A head that is not
`release/vX.Y.Z` returns before any subject is read (`:349-354`). The step
does not run off `main` (`.github/workflows/hygiene.yml:156-158`). A word
that only begins with `feat` is not named, and S4's case pins it with
`featured:`. In a minor the reading still prints a count and "carries no
feat:", and a `Feat:` subject is what would make that line wrong, so naming
it there is inside the scope. Read.

confirms: none
The five departures in `trail/phases/phase-1.md` hold. (1) A YAML plain
scalar cannot end in `:` followed by a line end. Quoting the name was the
other way, but `skills/verify/scripts/broad_gate.py#STEP_RE` takes the text
after `name:` as it stands, quotes included, so dropping the colon kept every
reader. (2) `git grep -n "the work it carries"` outside `seal/threads/`
returns only the new name: `hygiene.yml:141`, `broad_gate.py:2223`,
`broad_gate.py:2260` and the two lines in `tests/skills/test_broad_gate.py`.
Executed. (3) The seven `Test_main` cases that moved from `feat:` to `fix:`
each assert a range or a tracker read, never the prefix. Read. (4) The
missing-milestone case goes through `wire` because the subjects are now read
before the early return. Read, and finding 4 is about its pin. (5) "the
changelog fold" and *Before the pull request opens* item 2
(`skills/commit-pr-convention/SKILL.md:285-286`) follow from the rewrite.
Read.

confirms: none
The crafter's seen-red claim holds. With the script restored to `f80f48e6`
and the tests at `45936903`, the module gave 10 failed and 27 passed. The ten
are the eight `Test_judge_feat` cases and the two new `Test_main` cases, as
`trail/phases/phase-1.md` says. Executed (`## Probes`).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* lists the full
suite, the repository-wide lint and the format at this branch's head after
`release/v0.26.0` is merged in, with the orchestrator answering. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `seal mutate`'s 19 mutants, 19 red, and the 83-module boundary run with 4,825 passed. The crafter ran both and this round did not run them again. A mutation score shows the reading is tested, not that it is safe | `trail/phases/phase-1.md` | the sealer, by its sample |
| Whether each edge of the not-read scope carries a case, which #1167's `CONTRIBUTING.md` bullet will ask for. A near spelling in a minor and one on the missing-milestone path have no case. The bullet is not on this base | `tests/github/test_release_completeness_check.py:260-283` | the orchestrator, after `release/v0.26.0` is merged in |
| The core sentence that the comment on `FEAT` cites, and #1167's Table A row that `## Rule changes` item 4 changes, are both on #1167's branch | `.github/scripts/release_completeness_check.py:285-288` | the orchestrator, at the merge of `release/v0.26.0` into this branch |
| The renamed step and its `::error::` line on a real release pull request into `main` | `.github/workflows/hygiene.yml:141` | the orchestrator, at the release pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_release_completeness_check.py tests/text/test_a_release_cannot_ship_an_untrue_milestone.py tests/behaviour/test_the_gate_names_every_step_ci_runs.py tests/skills/test_test_layout.py -q` | exit 0, 133 passed |
| `bin/seal layout --pairs tests/github/test_release_completeness_check.py` | exit 0, 1 file read, 0 pairs |
| In a scratch clone at `45936903`: `git checkout f80f48e6 -- .github/scripts/release_completeness_check.py`, then `python -m pytest tests/github/test_release_completeness_check.py -q -p no:xdist` | exit 1, 10 failed and 27 passed; the clone was removed |
| `git grep -n "the work it carries" -- ':!seal/threads'` | five lines, each carrying the new step name |
