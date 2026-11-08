# Review round 1: 1794142459-parity-reads-original-forward

```seal
target: aa185613e against release/v0.35.1
```

This is a finding round over the whole branch, `9e758b0b0..aa185613e`
(executed: `git rev-parse HEAD` and `git merge-base HEAD release/v0.35.1`).
No earlier round exists, so no fact is carried; every coordinate below was
opened this round. No `seal/parity.md` is declared in this repository, so
no comparison with an original is recorded and no `original:` line is
owed; the work item changes the parity method's text, which this round
reads as text a framer, a tracer, a proofer and a sealer act on.

## Findings

### 1. The tracer still starts at the design's coordinates and searches the original only for the axes they leave, beside a skill section that now starts at the original's entry point

```seal
severity: should
location: `agents/tracer.md:32-33`, `agents/tracer.md:58`, `seal/threads/1794142459-parity-reads-original-forward/gaps.md:11-17`
evidence: read `agents/tracer.md:27-39`, `agents/tracer.md:58-60`, `skills/legacy-parity/SKILL.md:66-83`, `seal/threads/1794142459-parity-reads-original-forward/trail/phases/phase-1.md:139-146`; executed `git show 9e758b0b0:skills/legacy-parity/SKILL.md` and `git show 9e758b0b0:agents/tracer.md` (the removed sentence and step 3 side by side), and `grep -rn "Start from the design's coordinates\|axes they leave" tests agents skills docs`, which printed `agents/tracer.md:33` and `agents/tracer.md:58` alone
```

Why it matters: the work removed "Start every comparison there instead of
searching the original" from `skills/legacy-parity/SKILL.md` *The
original's coordinates* (`frame/design.md` *Removes*, row 1). At the base,
`agents/tracer.md:32-33` restated that sentence for the tracer: "Start from
the original's coordinates the design's Grounding cites, search the
original only for the axes they leave". The rule at `agents/tracer.md:58`
leads with the same instruction, "Start from the design's coordinates".
Both still stand. The tracer opens *The original's coordinates* at step 1
(`agents/tracer.md:27-29`), which now reads "A comparison starts at the
original's entry point and opens the list's coordinates there"
(`skills/legacy-parity/SKILL.md:78-79`). So the tracer gets two starting
points and has to pick one. That is the side-by-side contract rule 19
refuses, and `skills/core/SKILL.md` *The rule a mechanism is kept against*
says the change removes what stood on the old fact in the same commit.

Claimed (`gaps.md:13-17`, `trail/phases/phase-1.md:139-146`): step 4,
"Trace each axis to what the original sends the client", still reaches an
item on a cited axis, so steps 3 and 6 do not contradict each other. Found:
step 4 traces forward from what step 3 started at. That reaches every field
of a response the design cites, because the trace ends at the finished
response. It does not reach a query axis the design left out on an axis it
cites. A query axis is what the original accepts (`skills/legacy-parity/SKILL.md:69-70`).
It is parsed at the entry point, upstream of any cited coordinate, and step
3 tells the tracer not to search there. It also misses an error code raised
on a branch the cited path does not take. The issue's two dropped items
were a status field and a filter axis (`frame/design.md` *Grounding*, the
issue-body row). The filter axis is the kind step 3 leaves unsearched, and
step 6 now asks the tracer to report that kind
(`agents/tracer.md:37-38`). `frame/design.md` *Scope* item 3 kept "every
rule" as it was, and no case pins the rule's lead or step 3 (the grep
above), so nothing ties the old sentences in place.

The fix rewrites both statements in place. Each line fits within the
file's 88 display columns (`tests/behaviour/test_docs_line_wrap.py`). Step 1's
opening, the guessed-original rule and "leaves nothing behind (rule 7)"
stay, so `tests/text/test_a_moved_rule_leaves_its_definition.py` and
`tests/behaviour/test_a_probe_that_commits_says_so.py` stay green. Once
step 3 is amended, the `## Not done` paragraph of `gaps.md:11-17` states
work that was done, so the fix pass rewrites or removes it in the same
commit. `frame/design.md` *Scope* item 3, "every rule stay as they are", is
the frame's sentence at its commit, and folding it is the orchestrator's
act.

```markdown
3. Start at the original's entry point for each entry point the work
   ports, open there the coordinates the design's Grounding cites, and say
   which axes, and which items of the original's output surface, they leave.
```

```markdown
**Start at the original's entry point, open the design's coordinates there,
and report the axis nobody looked at.**
```

### 2. An item that both the design's list and the port lack is located in `frame/design.md` alone, which is the issue's own case

```seal
severity: should
location: `skills/legacy-parity/SKILL.md:78-80`, `skills/legacy-parity/SKILL.md:112-118`
evidence: read `skills/legacy-parity/SKILL.md:16-18`, `skills/legacy-parity/SKILL.md:78-80`, `skills/legacy-parity/SKILL.md:112-118`, `skills/code-review/SKILL.md` *The record* (the `location:` bullet), `seal/threads/1794142459-parity-reads-original-forward/frame/design.md:36`
```

Why it matters: *The original's coordinates* says that an item the
original sends and the list lacks "is a finding on the frame, located in
`frame/design.md`" (`skills/legacy-parity/SKILL.md:79-80`). The sentence
does not separate a list that lacks an item the port has from one that
lacks an item the port lacks too. The second is the issue's case: nobody
listed the two items, so nobody built them. *Parity review* says an item
the port does not send is `differs` (`:115-116`). It does not say whether
that is the same finding as the frame finding or a second one. A proofer
that follows the first sentence as written locates the item in
`frame/design.md` alone. A fix pass then closes it with a commit that adds
the item to the list and touches the one path named. The port still lacks
the item, which is the defect the work exists to catch.
`skills/code-review/SKILL.md` *The record* asks `location:` to name every
place the defect shows. These two sentences name one place, and the reader
of the parity skill acts on them. `frame/design.md` *Scope* item 1 holds
the same sentence at its commit.

The clause goes in *Parity review*, not in *The original's coordinates*.
The tracer reads the latter (`skills/legacy-parity/SKILL.md:16-18`), and it
gives no verdict (`agents/tracer.md:51-52`). The snippet follows the
sentence at `:115-118` that ends "as *Three-way judgment* asks of every
divergence."

```markdown
An item the original sends that the design's list and the port both lack
is one finding, `differs`, whose `location:` names the port's path beside
`frame/design.md`, since the fix adds the item to both.
```

### 3. The response-shape paragraph names the work item's `frame/design.md` as the only non-migration reference, dropping the `docs/` policies stage 1 reads first

```seal
severity: should
location: `skills/code-review/SKILL.md:91-93`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:4`
evidence: read `skills/code-review/SKILL.md:3-9`, `skills/code-review/SKILL.md:26-28`, `skills/code-review/SKILL.md:74-81`, `skills/code-review/SKILL.md:91-97`, `seal/threads/1794142459-parity-reads-original-forward/trail/phases/phase-2.md:36-40`, `templates/setup/config.md:374-380`
```

Why it matters: the paragraph says "The reference is the work item's
`frame/design.md`, or the original in a migration"
(`skills/code-review/SKILL.md:91-93`). Stage 1 of the same file reads "the
code against the ratified documents above it, the `docs/` policies first
and then the work item's SDD set" (`:26-28`). A response field that a policy
document states, such as an API contract under `docs/` or under a reference
root (`templates/setup/config.md:374-380`), is then left out of the walk
whenever the design does not restate it. The skill is also used for "review
this PR" with no work item at all (`:6-7`), and then no `frame/design.md`
exists to walk from.

Claimed (`trail/phases/phase-2.md:36-40`): naming the path keeps the
paragraph from reading as "the design" or "the policy". Found: it reads as
"the design" alone, and the rows of the table it qualifies say "the policy
or the design" (`:80`). The fragment repeats the narrowed sentence
(`changelog.md:4`, "The reference is the work item's `frame/design.md`, or
the original in a migration"), so the fix reaches it too.

This snippet replaces the paragraph's first two sentences. Finding 4
replaces the sentence after them, so the two fixes do not overlap.

```markdown
The response-shape row is walked from the reference to the code. The
reference is what stage 1 reads above the code, the `docs/` policies and the
work item's `frame/design.md`, or the original in a migration
(`skills/legacy-parity/SKILL.md` *Parity review*).
```

In `changelog.md:4`, the sentence becomes:

```markdown
The reference is the policy documents and the work item's `frame/design.md`, or the original in a migration.
```

### 4. The response-shape default makes a field the reference excludes into a field the code must send

```seal
severity: should
location: `skills/code-review/SKILL.md:93-96`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:4`
evidence: read `skills/code-review/SKILL.md:81`, `skills/code-review/SKILL.md:93-96`, `seal/threads/1794142459-parity-reads-original-forward/changelog.md:4`, `seal/threads/1794142459-parity-reads-original-forward/frame/design.md:40`
```

Why it matters: the row's cell names "included/excluded fields"
(`skills/code-review/SKILL.md:81`). The paragraph's default says "The
proofer looks for each field the reference states in the code, and a field
it does not find there is a finding by default" (`:93-95`). A reference that
says a field is excluded, such as "the response never carries
`password_hash`", states that field. Read as written, the default turns a
correct build that leaves the field out into a finding. It also never says
that a build sending the excluded field is one. The next sentence covers
only a field "the reference does not" state (`:95-96`), and an excluded
field is one the reference does state. A proofer acting on this paragraph
raises a false finding on the correct code and has no sentence for the
real defect. `changelog.md:4` repeats the default in the same words, and
`frame/design.md` *Scope* item 5 holds it at its commit.

The snippet replaces the sentence at `:93-95` that starts "The proofer
looks for each field". Finding 3's snippet replaces the two sentences
before it.

```markdown
The proofer looks in the code for each field the reference says the
response carries, and a field it does not find there is a finding by
default; a field the reference says the response leaves out and the code
sends is a finding too.
```

In `changelog.md:4`, the sentence becomes:

```markdown
A paragraph under the table states the default: the proofer looks in the code for each field the reference says the response carries, and a field it does not find there is a finding by default, as is a field the reference leaves out and the code sends.
```

## Confirmations

What matched: *Scope* item 1. `skills/legacy-parity/SKILL.md:66-83` lists
the output surface by entry point in `frame/design.md` *Grounding*, names
the framer as writer and `original not found`, and keeps the pin clause and
the baseline sentence. The removed sentence is gone outside the records
(executed: `git grep -n "Start every comparison there" -- . ':!seal/threads'`
printed nothing, exit 1).

What matched: *Scope* item 2 at `skills/legacy-parity/SKILL.md:112-125`.
The walk goes forward from the original's entry point, `differs` is the
default, `grounded` needs a quoted clause, the round record and its
`## Confirmations` are the walk's home, the sealer's walk is recorded as
the `original:` line, and the paragraph ends in a `check:` line. The
opening sentence's amendment at `:97-99` (phase 1's second departure) keeps
the section in one reading, as `trail/phases/phase-1.md:37-43` claims
(read). *Recording the comparison* has no hunk in the diff (read: `git diff
9e758b0b0..aa185613e -- skills/legacy-parity/SKILL.md`).

What matched: *Scope* items 3 and 4. `agents/tracer.md:36-39` names each
lacking item with its coordinate. `agents/framer.md` step 4 cites
`skills/legacy-parity/SKILL.md` *The original's coordinates*, and the cited
heading resolves (read; `tests/behaviour/test_a_cited_section_stands_in_its_file.py`
passed in the run below, executed).

What matched: *Scope* item 5's cell. `git grep -n "included/excluded fields"
-- . ':!seal/threads'` printed the one rewritten cell at
`skills/code-review/SKILL.md:81` (executed).

What matched: *Scope* item 6. The four cases in
`tests/text/test_review_axes.py:45-109` pin the list's home and writer,
the framer's citation, `differs` among `PARITY_WORDS`, the round record as
the walk's home, and the tracer's step 6. Read against their group, no case
duplicates another: the module's existing cases pin the record's writer and
the resolution order, and
`tests/text/test_a_moved_rule_leaves_its_definition.py` pins tracer step 1
and the guessed-original rule, not step 6. The claim that each was seen red
(`trail/phases/phase-1.md:97-105`) holds against the base text: at
`9e758b0b0` none of the four guards' strings stands in its section (read:
`git show 9e758b0b0:` of the three files). The narrow run is green
(executed, the first row of `## Probes`).

What matched: `bin/seal rules --check` reads the two new `check:` lines
and all 219 hold (executed).

What matched: the prefix row of `frame/plan.md` *Judgments of the run*.
The diff touches no `lib/`, `templates/`, `bin/` or script file, and adds
no record format, field or command (executed: `git diff --stat
9e758b0b0..aa185613e`). `.claude-plugin/plugin.json` reads 0.35.0 at the
base and at the target, as *Operational impact* states (executed).

What matched: the fold row of `frame/plan.md` *Judgments of the run*.
`tests/text/` holds neither line-wrap nor cited-section module and
`tests/behaviour/` holds both (executed: `ls`). The frame's lines now name
`tests/behaviour/`.

What matched: each of the six quotes in `pr.md` stands word for word at the
source its coordinate names: `changelog.md:3` for quotes 1, 2 and 4,
`changelog.md:4` for quote 3, `frame/plan.md:68` for quote 5, and
`gaps.md:8` for quote 6 (read).

What matched: the present-state files `routing.md`, `frame/design.md`,
`frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and
`pr.md` were read whole at the target. Apart from what findings 1 to 4
locate in `gaps.md` and `changelog.md`, no sentence the target contradicts
was found (read).

Weighed and not raised: two guards of `tests/text/test_review_axes.py`
hold the act together with the party. One is `"framer writes the list"` at
`:63`, the other `"lacks"` at `:107`. A rewording turns each one red, as
mutation 8 of `trail/phases/phase-1.md:129-130` shows for `lacks`. Each is
also the only guard that holds its fact: who writes the list, and that
step 6 names what the list lacks. So under `docs/running/what-a-script-gates.md`
*The checks* they pin a fact a reader acts on, and this round raises no
finding on them. `frame/plan.md:62` keeps the template's guidance line
above the *Judgments of the run* table, as the sibling work item's plan
does. It states nothing about the tree.

## Not judged

| What | Location | Who answers |
|---|---|---|
| whether a framer, a tracer and a proofer in a migration act on the rewritten sentences; no original resolves here and no case runs any of them | `frame/questions.md` Q1, `gaps.md:8` | a measurement: the orchestrator of the first migration run after the release |
| the full suite, the repository-wide lint and the format check at the target; this round ran five modules and `seal rules --check`, and the suite stays `unverified` | `gaps.md:7` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_review_axes.py tests/text/test_the_record_is_written_in_words.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist` | 310 passed, exit 0 |
| `bin/seal rules --check` | "all 219 check lines in 68 rule files hold", exit 0 |
| `grep -rn "Start from the design's coordinates\|axes they leave" tests agents skills docs` | two lines, `agents/tracer.md:33` and `agents/tracer.md:58`; no case pins either |
| `git grep -n "Start every comparison there" -- . ':!seal/threads'` | nothing, exit 1 |
| `git grep -n "included/excluded fields" -- . ':!seal/threads'` | the one cell, `skills/code-review/SKILL.md:81` |
