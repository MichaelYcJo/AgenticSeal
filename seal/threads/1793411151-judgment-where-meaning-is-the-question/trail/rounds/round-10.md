# Review round 10: 1793411151-judgment-where-meaning-is-the-question

target: e95ee8e2, fixes f9454e2e..e95ee8e2

This is a verifying round over round 9's three closes. The fix diff holds
`5b1dc057`, `604ec0e8`, `3b484a3c`, the answer `b2808e66` and the frame
fold `e95ee8e2`. `5b1dc057` and `e95ee8e2` are the orchestrator's, and this
round read them as new units. It reviewed nothing outside the diff except
the code the diff calls into: `hooks/lib/routing.py#rounds_unreadable` and
`skills/settle/scripts/rule_changes.py#headings`, `#letters` and
`#section_lines`.

Carried from round 9 and not established again: where `rules.letters`
stands (`skills/settle/scripts/rule_changes.py:94-97`), and that the
`Judged against` cells of `frame/plan.md` *Judgments of the run* name
sections in their files. Re-established here: that `routing.rounds` catches
`NotADirectoryError` and returns `[]` (`hooks/lib/routing.py:599-609`), what
`rounds_unreadable` returns for each shape (`:611-645`), and every verdict.

The spawn prompt and `b2808e66`'s answers were read as claims. The crafter's
claims were checked where they could be run. The five new cases are red
against `settle.py` from `5b1dc057` and pass at `e95ee8e2`, and the module
passes 90 cases (both executed). One claim has no case behind it.
Finding 2's answer says "a plan holding both gets the line and its rows",
and nothing in `tests/skills/test_settle.py` holds a plan with both
headings. That is the finding below.

## Findings

### 1. The near-heading naming in `seal settle`'s judgments reader has a case at the fence and none at the HTML comment or beside the exact section, so two mutants of it survive the module

severity: should
location: `tests/skills/test_settle.py:1029`, `skills/settle/scripts/settle.py:521-522`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md:55`
evidence: executed `bin/seal mutate skills/settle/scripts/settle.py --replace "        marks = rules.headings(lines)" "        marks = rules.headings(lines, comments=False)" --replace "if t != JUDGMENTS and rules.letters(t) == rules.letters(JUDGMENTS)" "if t != JUDGMENTS and rules.letters(t) == rules.letters(JUDGMENTS) and not any(u == JUDGMENTS for _m, _l, u in marks)" --tests "bin/test tests/skills/test_settle.py -q -p no:xdist"`
verdict: open
regression: round-9#2

The unit is the near-heading scan that `604ec0e8` added to `judgments`
(`skills/settle/scripts/settle.py:535-546`) and its cases
(`tests/skills/test_settle.py:1004-1041`). The frame says each edge of the
scope where a gate reads a form carries a case (`frame/design.md:46`, and
`CONTRIBUTING.md:389-391` as built), and phase 5's row
(`frame/plan.md:59`) verifies *Scope* item 12 by `test_settle.py`. The fix
cased the fence edge alone. The defect came from round 9's paste-ready
grounds, which named the fence as the one edge, and the fix took them as
written.

The code itself holds. Round 9's defect, a near heading passed over in
silence, is gone: the three parametrised headings are red against
`settle.py` from `5b1dc057` and pass at `e95ee8e2` (executed). A probe
over `settle.judgments` found the reader names what it should and nothing
more (executed). A near heading inside `<!-- -->` is not named. A
`### Judgments Of The Run` inside the exact section is named, and its rows
are not read, so the line's "none of its rows were read" is true there. A
plan holding a near heading and then the exact section gets the line for
the first and the rows of the second. `## Judgments of the run:` is named,
and an exact heading at level 1 is read.

The scope is every live heading of the plan. Both the naming and the read
of the exact section take it from the same `rules.headings(lines)` call.
`unverified_check.py#live_lines` defines a live line as one outside a
fence, an HTML comment and a code span (`skills/verify/scripts/unverified_check.py:542-545`,
read). So the scope has a second edge, the comment, and it has no case.
The plan with both headings is the other path the fix pass named in its
answer, and it has no case either. Two mutants show it. Reading the
headings with `comments=False`, which names a heading inside a comment,
survived all 90 cases of `test_settle.py`. Naming a near heading only
where the exact section is absent survived too (executed). The first is
the defect class this run has met three times: a line named where the
reader does not read the form. The second loses the near heading's rows
without a word, which is round 9's finding 2 again for a plan holding
both headings.

Two sentences state the scope as the fence alone. The docstring at
`settle.py:522` says "A heading inside a fence is no heading". The frame at
`frame/design.md:55` says "a heading near *Judgments of the run* outside a
fence is named as not read". A heading inside a comment is outside a fence,
and it is not named.

The fix adds two cases to `Test_main` in `tests/skills/test_settle.py`,
after `test_accepts_a_near_heading_inside_a_fence_without_a_word`. They
were run once in this round's clone at `e95ee8e2`. Both passed there. The
first went red under the `comments=False` mutant, and the second went red
under the absent-section mutant (executed). They use the module's own
helpers and assume no OS precondition.

```python
    def test_accepts_a_near_heading_inside_a_comment_without_a_word(
        self, repo, capfd
    ):
        """The other edge of round 9's finding 2: a heading inside an HTML
        comment is no live heading, so the reader names nothing for it."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n<!--\n## Judgments of the Run\n-->\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert settle.JUDGMENTS_HEADING not in text, text

    def test_a_near_heading_is_named_beside_the_section_it_is_not(
        self, repo, capfd
    ):
        """A plan holding a near heading and the exact section gets the line
        for the first and the rows of the second: the naming runs before the
        reader looks for the exact section."""
        item(repo, "1700000001-a", "- nothing\n  why: x.")
        header = "| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
        (specs_dir(repo, "1700000001-a") / "frame" / "plan.md").write_text(
            "# Implementation Plan: a\n\n## Judgments Of The Run\n\n"
            + header
            + "| 2026-10-01 | near | y | z |\n\n## Judgments of the run\n\n"
            + header
            + "| 2026-10-02 | exact | y | z |\n",
            encoding="utf-8",
        )
        commit(repo, "a")
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        block = text.split(f"\n{settle.JUDGMENTS_HEADING}\n")[1]
        assert block.startswith(
            "    1700000001-a  seal/threads/1700000001-a/frame/plan.md  not read: "
            "line 3: `## Judgments Of The Run` opens like `## Judgments of the run`"
        ), block
        assert "2026-10-02  exact\n" in block, block
        assert "2026-10-01  near" not in block, block
```

The docstring sentence at `settle.py:522` becomes:

```python
    is in neither. A heading inside a fence or an HTML comment is no
    heading (`unverified_check.py#live_lines`). A row
```

The orchestrator folds `frame/design.md:55`'s "a heading near *Judgments
of the run* outside a fence is named as not read" to "a live heading near
*Judgments of the run*, one outside a fence and an HTML comment, is named
as not read".

answer:

## Confirmations

confirms: round-9#1
The close `fixed 604ec0e8` holds. `judgments` counts rounds only where
`routing.rounds_unreadable` is false (`skills/settle/scripts/settle.py:558-563`,
read). `rounds_unreadable` is true for any link, for a path that exists and
is not a directory, and for a directory whose `os.listdir` raises
(`hooks/lib/routing.py:626-644`, read). The report prints "its trail/rounds
is not a directory this can list, so no round was counted" in place of a
count (`settle.py:883-888`, read). Both rows of
`test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none`, a
file and a link to a directory holding `round-1.md`, are red against
`settle.py` from `5b1dc057` and pass at `e95ee8e2` (executed). The case
asserts no count line at all, so a link read as `1 round` would be caught.
`skills/settle/SKILL.md:193-195` and `changelog.md:3` say the count is
replaced by a name (read). The answer's correction of the phase-5 claim
matches `routing.py:599-609` (read). The unlistable directory has no case,
because `chmod 000` does not hold for root, the crafter says. The settle
reaches that shape through the same boolean the file and link cases pin, so
no mutant of `settle.py` tells the shapes apart. Its branch lives in
`routing.py:637-643`, outside this fix diff, and `git grep
rounds_unreadable` over `tests/` finds only `test_settle.py` (executed).
That is a row of `## Not judged`.

confirms: round-9#3
The close `fixed 3b484a3c` holds. The `gaps.md:12` row now ends "nothing
reads at the pull request whether a row was written". The clause and the
`, and` before it are gone, and the rest of the row is as round 9's
paste-ready row gives it (read, `git diff f9454e2e..e95ee8e2`).

confirms: none
The four rows `5b1dc057` and `e95ee8e2` add to `frame/plan.md`
*Judgments of the run* (`:87-90`) hold where this round opened them, and
so does the grounds cell `5b1dc057` corrects (`:85`). The
two fold rows name `2b7eef28` and `788e866e`, and each commit changes
`frame/design.md` alone, as its message and the row say (executed,
`git show --stat`). Round 8 was committed at `458645e2` before round 7 at
`9adb7de5`. Round 7 holds the stale `gaps.md` line as a `## Not judged` row
for round 9 (`trail/rounds/round-7.md:152`), and round 9 took it up as its
finding 3. So the moved-finding row's grounds hold (executed,
`git log`). Each `Judged against` cell names a section that stands:
*The fix pass then finds what the fixes left standing* is the bold lead at
`skills/code-review/orchestration.md:71`, and *Orchestrator: the run ends
with a verifying round* the heading at `:102` (read). The parallel-run
row's grounds now say that no file holds the owner's request. That is a
statement of where the request stands, and this round has no coordinate to
check it against.

confirms: none
`e95ee8e2`'s fold says what `604ec0e8` built, except the scope sentence
finding 1 names. *Scope* item 12 (`frame/design.md:55`) names the near
heading and the unlistable `trail/rounds`. Table A's `seal settle` row
(`:298`) adds both to its Unread cell (read). The design's `## Rule
changes` still parses: `rule_changes.parse` returned 22 ops, no `nothing`
block, no errors and no unread (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch. `gaps.md` labels them `unverified` | the branch at `e95ee8e2` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| The crafter's six mutants and its 295-module run, not re-run here. This round ran `test_settle.py` whole, the citation and unverified modules, and four mutants of its own | `skills/settle/scripts/settle.py`, `tests/skills/test_settle.py` | the orchestrator's broad run |
| The five new cases of `test_settle.py` on Windows, including the link row, which skips where no link can be made | `tests/skills/test_settle.py:962-1041` | the orchestrator, at the Windows legs of the pull request's CI run |
| Whether `routing.rounds_unreadable`'s unlistable-directory branch gets a case of its own, by a skip under root or by patching `os.listdir`. No test in the tree reaches it, and the crafter's reason, "`chmod 000` does not hold for root", rules out one way of making the case, not every way | `hooks/lib/routing.py:637-643`, `tests/hooks/test_routing.py` | the orchestrator, as a leftover's home, since the branch lies outside this fix diff |

## Probes

| Command | Result |
|---|---|
| `tests/skills/test_tmp_round10_probe.py`, one case calling `settle.judgments` over six plans, run once with `bin/test ... -q -s -p no:xdist` in a `git clone --no-local` at `e95ee8e2` under the scratchpad, then deleted | a near heading in a comment was not named; a level-3 near heading inside the exact section was named, and only the exact section's row was read; a near heading before the exact section was named, and the exact section's row was read; `## Judgments of the run:` was named; an exact heading at level 1 was read |
| `bin/seal mutate` over `settle.py` with the two mutants of finding 1, against `bin/test tests/skills/test_settle.py -q -p no:xdist` | baseline passed; both mutants SURVIVED |
| `tests/skills/test_tmp_round10_cases.py`, finding 1's two paste-ready cases, run once under `bin/seal mutate` with the same two mutants, then deleted | baseline passed; mutant 1 red; mutant 2 red |
| `settle.py` checked out from `5b1dc057`, `bin/test tests/skills/test_settle.py -q -p no:xdist -k` on the five new cases, then restored and the module run whole | 5 failed, and the fence case passed, as an edge does; restored, 90 passed |
| `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/skills/test_unverified_check.py -q -p no:xdist` | 387 passed |
| `rule_changes.parse` over `frame/design.md` with policy root `docs` | 22 ops, no `nothing` block, 0 errors, 0 unread |
| `git log` over rounds 7 and 8; `git show --stat 2b7eef28 788e866e`; `git grep rounds_unreadable` over `hooks`, `skills` and `tests` | round 8 committed before round 7; each fold commit changes `frame/design.md` alone; `rounds_unreadable` is read only by `settle.py` and named only in `test_settle.py` |
