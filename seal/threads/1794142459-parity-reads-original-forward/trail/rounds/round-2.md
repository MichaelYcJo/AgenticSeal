# Review round 2: 1794142459-parity-reads-original-forward

```seal
target: dc8a3da5e, fixes aa185613e..dc8a3da5e
```

This is a verifying round over the diff of round 1's fixes,
`aa185613e..dc8a3da5e` (executed: `git log --oneline aa185613e..HEAD` lists
`a550e71c0` round 1, `5c6575aaf` the fixes, `a65e2388d` the records'
corrections, `71aa2698f` the close blocks and `dc8a3da5e` the orchestrator's
fold). The code read is that diff: `agents/tracer.md` steps 3 and the rule's
lead, the two new sentences of `skills/legacy-parity/SKILL.md`, the
rewritten paragraph under `skills/code-review/SKILL.md` *Comparison axes*,
the new case in `tests/text/test_review_axes.py`, and the records the range
changes. Beside it, `routing.md`, the three frame files, `gaps.md`,
`changelog.md` and `pr.md` were read whole at `dc8a3da5e`, and
`trail/phases/` and `trail/rounds/round-1.md` for their coordinates.

Carried from round 1, not re-established: the coordinates of its four
findings, which this round opened at their lines; that no `seal/parity.md`
is declared here, so no `original:` line is owed; and the weighing of the
template's guidance line at `frame/plan.md:62`, which the fix diff does not
touch. Re-derived: every verdict below, and the `check:` targets, through
`bin/seal rules --check` (all 219 hold, executed).

## Findings

### 1. The new case passes against the sentence round 1's second finding found defective, so it does not hold the port it is named for

```seal
severity: should
location: `tests/text/test_review_axes.py:99-112`
evidence: executed the Edit of `skills/legacy-parity/SKILL.md:121-122` to "`location:` names `frame/design.md`, since the fix adds the item to the list." then `bin/test "tests/text/test_review_axes.py::test_an_item_the_list_and_the_port_both_lack_is_located_in_both" -q -p no:xdist` (1 passed), then the Edit back and `git status --short` (clean); read `tests/text/test_review_axes.py:99-112`, `skills/legacy-parity/SKILL.md:96-128`
regression: round-1#2
```

The unit is `test_an_item_the_list_and_the_port_both_lack_is_located_in_both`,
which `5c6575aaf` added. `frame/design.md` *Scope* item 6, delivered by the
phase 1 row of `frame/plan.md` *Phases*, says each case pins a fact a
reader acts on and is shown red with that fact removed, and *Scope* item 2
now states that the `location:` of such a finding names the port's entry
point beside `frame/design.md`. The fix pass wrote guards on `` `location:` ``
and `` `frame/design.md` `` alone. The defect came from choosing the two
backticked tokens of the sentence as the guards, while the fact that tells
the fix from round 1's defect, the port, stayed in the comment.

Why it matters: round 1's second finding was that such an item was
located in `frame/design.md` alone. With the sentence edited back to that
defect, the port gone and the design kept, the case passes (the probe
above). So the case pins nothing of the change it was written for. Its
name says "located in both", its docstring says "a fix that adds the item
to the list alone does not close it", and its comment says "the design
among the places it names beside the port". Contract rule 15 says a case
that passes against the defect it was written for pins nothing.

Claimed (round 1's close of finding 2): the case was seen red before the
skill was edited, failing on its first guard, and `seal mutate` over each
guard went red. Found: both hold as stated. At `aa185613e` neither guard's
string stands in *Parity review*'s prose (executed: `git show
aa185613e:skills/legacy-parity/SKILL.md` through `grep`, exit 1), and each
guard's string occurs once in that prose at HEAD (read). Neither run
removed the port, so neither could show this.

The fix adds the port as a third guard. "port's entry point" stands once in
the section's prose, in the new sentence; "port" alone stands in four other
sentences and would stay green. Under `docs/running/what-a-script-gates.md`
*The checks* the guard holds a fact a reader acts on, where a finding is
located. The fix pass shows it red with the port removed, as the probe
above did. If finding 2 of this round is fixed, its rewording keeps the
phrase "the port's entry point", so this guard stays valid.

```python
    rel, heading = PARITY_REVIEW
    body = prose(rel, heading)
    # The round record's field that says where a finding shows, and the two
    # places it names: the port, where the item is missing, and the design.
    for part in ("`location:`", "port's entry point", "`frame/design.md`"):
        assert part in body, (
            f"{rel} {heading} does not locate an item both lack with {part!r}"
        )
```

### 2. The sentence for an item the list and the port both lack gives it `differs` with no default, beside the sentence that makes it `grounded` where a policy clause is quoted

```seal
severity: should
location: `skills/legacy-parity/SKILL.md:119-122`, `skills/legacy-parity/SKILL.md:80-81`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:3`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:6`
evidence: read `skills/legacy-parity/SKILL.md:42-54`, `skills/legacy-parity/SKILL.md:78-81`, `skills/legacy-parity/SKILL.md:104-122`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:3`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:6`, `seal/threads/1794142459-parity-reads-original-forward/frame/design.md:36-37`, `seal/threads/1794142459-parity-reads-original-forward/trail/rounds/round-1.md:115-119`
regression: round-1#2
```

The unit is the sentence `5c6575aaf` added to `skills/legacy-parity/SKILL.md`
*Parity review* at `:119-122`, with its pair at `:80-81`. `frame/design.md`
*Scope* item 2, delivered by the phase 1 row of `frame/plan.md` *Phases*,
says an item the port lacks is `differs` by default and `grounded` where a
policy clause is quoted. The fix wrote "is one finding, `differs`" with no
default and located it in the port "since the fix adds the item to both".
The defect came from round 1's own paste-ready snippet
(`round-1.md:115-119`), which the fix pass applied as written.

Why it matters: the sentence before it (`:116-119`) gives every item the
port lacks `differs` by default and `grounded` where a quoted policy clause
leaves it out, as *Three-way judgment* asks (`:46-50`). The new sentence
names a narrower case, an item the list lacks too, and gives it `differs`
outright. A reader takes the narrower sentence over the general one. Take
an item the original sends, which a policy clause says the new service
leaves out, and which the framer left off the list as well. Under the
sentence before, it is `grounded`, and the port is right not to send it.
Under the new sentence, it is `differs` and located in the port, and the
fix pass adds the item to the port against the policy. The list lacking it
is still a defect of the frame, since the list is the original's surface,
whatever the port does. `skills/writing-style/SKILL.md` *에이전트와 검사가
읽는 글은 한 가지로만 읽히게 쓴다* asks for one reading; the paragraph now
has two for this case. *The original's coordinates* (`:80-81`) has the same
gap: it puts the item in the port wherever the port lacks it.

The fix makes the port's location follow the verdict. It reaches the
skill's two sentences. The fix pass owes the same change to `changelog.md:3`
("located in the port's entry point and in `frame/design.md`") and to the
Updating line at `changelog.md:6`. It also owes it to the docstring of the
case in finding 1, which says the finding "is located in the port as well".
`frame/design.md` *Scope* items 1 and 2 state the sentences as they stand,
and folding them is the orchestrator's.

In *Parity review*, replacing the sentence that opens "An item the
original sends that the design's list and the port both lack":

```markdown
An item the original sends that the design's list and the port both lack
is one finding, with the verdict the sentence before gives it. Its
`location:` names `frame/design.md`, and the port's entry point beside it
where the verdict is `differs`, since that fix adds the item to both.
```

In *The original's coordinates*, the sentence's second line:

```markdown
by the walk, and it is a finding on the frame, located in `frame/design.md`
and, where the port lacks it too with no grounds, in the port as well
(*Parity review*).
```

### 3. The fold row says the fix pass named *Scope* item 2 as contradicted by HEAD, and round 1's record names items 1, 3 and 5 and *Removes* only

```seal
severity: should
location: `seal/threads/1794142459-parity-reads-original-forward/frame/plan.md:69`
evidence: read `seal/threads/1794142459-parity-reads-original-forward/frame/plan.md:69`, `seal/threads/1794142459-parity-reads-original-forward/trail/rounds/round-1.md:81`, `seal/threads/1794142459-parity-reads-original-forward/trail/rounds/round-1.md:123`, `seal/threads/1794142459-parity-reads-original-forward/trail/rounds/round-1.md:170`, `seal/threads/1794142459-parity-reads-original-forward/trail/rounds/round-1.md:214`; executed `git diff aa185613e..dc8a3da5e -- seal/threads/1794142459-parity-reads-original-forward/frame/design.md`
```

Why it matters: the row folds *Scope* items 1, 2, 3 and 5 and *Removes*.
Its grounds say the fix pass "named these frame statements as contradicted
by HEAD". Round 1's four close blocks name item 3 and *Removes*
(`round-1.md:81`), item 1 (`:123`) and item 5 (`:170`, `:214`). None names
item 2. Item 2 was not contradicted either: before the fold it described
*Parity review* without the new clause, which leaves it short, not wrong.
Adding the clause was the orchestrator's own reading, and a sound one, but
the row credits it to the fix pass. The settle reads this column to weigh
what each judgment cost and caught (`skills/core/SKILL.md` *A judgment
stands on a source document, and is written down with both*). A row that
names the wrong source tells it the fix pass flagged something it did not.

The grounds cell of the row becomes:

```markdown
The fix pass closed round 1's four findings `fixed 5c6575aaf` (`trail/rounds/round-1.md`) and named *Scope* items 1, 3 and 5 and *Removes* as contradicted by HEAD; item 2 describes *Parity review*, which the same commit gave the clause on an item the list and the port both lack, so it gains that clause too
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `agents/tracer.md:32-35` starts step 3 at the original's
entry point for each ported entry point, opens the design's coordinates
from there, and names the axes and items of the surface they leave. The
rule's lead at `:60-61` says the same, matching the skill's
`skills/legacy-parity/SKILL.md:78-79` (read). Neither old phrase stands
outside the records (executed: `git grep` on "design's coordinates",
"Grounding cites" and "axes they leave" printed only the two rewritten
lines and records under `seal/threads/`, where `frame/design.md:16` is the
*Grounding* row dated to `9e758b0b0`). Step 1's opening, the
guessed-original rule and "leaves nothing behind (rule 7)" stand, and their
two modules pass in the narrow run (executed). The `## Not done` paragraph
that argued step 3 stands is replaced (read: `gaps.md:13-20`).

```seal
confirms: round-1#2
```
What holds: the defect round 1 named, an item both lack located in
`frame/design.md` alone, no longer stands. *The original's coordinates*
locates it in the port too (`skills/legacy-parity/SKILL.md:80-81`), and
*Parity review* names the port's entry point beside `frame/design.md`
(`:119-122`). `changelog.md:3` and `:6` say the same (read). The case that
was to pin it and the verdict the sentence gives are findings 1 and 2 of
this round.

```seal
confirms: round-1#3
```
What holds: `skills/code-review/SKILL.md:92-94` makes the reference what
stage 1 reads above the code, the policy documents and the work item's
`frame/design.md`, with the original added in a migration. That matches
stage 1 at `:26-28` and holds where no work item exists. `changelog.md:4`
carries the same sentence (read).

```seal
confirms: round-1#4
```
What holds: `skills/code-review/SKILL.md:94-99` raises a field the
reference says the response carries and the code lacks, and, as a separate
sentence, a field the reference says the response leaves out and the code
sends. The next sentence is limited to a field "the reference does not
mention", so an excluded field no longer falls under it. `changelog.md:4`
carries both (read). The lines wrap inside 88 columns (executed:
`tests/behaviour/test_docs_line_wrap.py` in the narrow run).

What matched: the fold's *Scope* items 1, 3 and 5 and its new *Removes*
row state HEAD's sentences (read: `frame/design.md:36`, `:38`, `:40`,
`:86`, against `agents/tracer.md:32-35`, `:60-61`,
`skills/legacy-parity/SKILL.md:78-81`, `skills/code-review/SKILL.md:91-100`).
*Scope* item 2's added sentence matches `skills/legacy-parity/SKILL.md:119-122`;
finding 2 names what both now say.

What matched: each of the six quotes in `pr.md` stands at its source,
word for word with runs of whitespace collapsed (executed: a script over
`pr.md`, `changelog.md`, `frame/plan.md` and `gaps.md` printed six
matches).

What matched: the closing memo's diff. Rows 1 and 3 of `## Not verified`
are reworded in place, with the same item and answerer, and no row left
(read: the range's diff of `gaps.md`). The `## Not done` paragraph is
replaced because its item, step 3 left as it was, was done; `## Not done`
holds decisions, and the closing rule for rows binds `## Not verified`
only (`skills/implement/SKILL.md` *4. The closing memo — only what the
diff cannot show*, read).

What matched: the new case, read against its group. The other case on
*Parity review*, `test_an_item_the_port_lacks_differs_and_the_walk_stands_in_the_round`,
holds the verdict word and the walk's home, and no case in the module held
`location:`, so the new case is no duplicate (read:
`tests/text/test_review_axes.py:81-112`).

Weighed and not raised: `frame/design.md` *Scope* item 6 lists the facts
the cases pin and does not name the new case's fact, which *Scope* item 2
states; the list is short of HEAD, and nothing in it is contradicted. The
`## Not done` paragraph says "Round 1's first finding rewrote both in
place" (`gaps.md:15-16`), where the fix pass did the rewriting; that sentence
reads badly and is not wrong about the tree.

## Not judged

| What | Location | Who answers |
|---|---|---|
| whether a framer, a tracer and a proofer in a migration act on the rewritten sentences; no original resolves here and no case runs any of them | `frame/questions.md` Q1, `gaps.md:8` | a measurement: the orchestrator of the first migration run after the release |
| the full suite, the repository-wide lint and the format check at the target; this round ran six modules and `seal rules --check`, and the suite stays `unverified`, which is the label `gaps.md:7` gives it | `gaps.md:7` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_review_axes.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_record_is_written_in_words.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_probe_that_commits_says_so.py -q -p no:xdist` | 315 passed, exit 0 |
| `bin/seal rules --check` | "all 219 check lines in 68 rule files hold", exit 0 |
| the Edit of `skills/legacy-parity/SKILL.md:121-122` to drop the port, then `bin/test "tests/text/test_review_axes.py::test_an_item_the_list_and_the_port_both_lack_is_located_in_both" -q -p no:xdist`, then the Edit back | 1 passed against the defective sentence; `git status --short` clean afterwards |
| `git show aa185613e:skills/legacy-parity/SKILL.md` over the *Parity review* lines, through `grep -n "location:\|frame/design.md"` | nothing, exit 1 |
| `git grep -n -i` on "design's coordinates", "Grounding cites", "axes they leave", "located in `frame/design.md`", "reference is the work item", "each field the reference states" outside `trail/` | `agents/tracer.md:33`, `:60` (the rewritten lines), `skills/legacy-parity/SKILL.md:80` (the rewritten sentence), and dated or quoting lines of this work item's records |
| a script comparing each `pr.md` quote with its source, whitespace collapsed | six matches |
