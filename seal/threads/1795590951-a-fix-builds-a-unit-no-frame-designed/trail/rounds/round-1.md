# Review round 1: 1795590951-a-fix-builds-a-unit-no-frame-designed

```seal
target: 8562ea70f against origin/release/v0.39.0
```

The range read is `6f4802fa8...8562ea70f`, ten commits, in a `git clone --no-local` at the target. This is the first round, so no earlier round's facts are carried: each fact below was opened or run in this round. The work item's records that state the present were each read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, with `trail/phases/phase-1.md`. No `pr.<lang>.md` stands, since `Commit and pull request language` is English. `seal/parity.json` is not declared. Outside the diff, this round opened `agents/framer.md:224-233`, `agents/crafter.md:17-72`, `docs/running/the-agent-set.md:94-110`, `skills/implement/orchestration.md:21-178` whole, `skills/code-review/orchestration.md:23-105` and `:200-245`, and `skills/code-review/scripts/chain_check.py:1420-1440`.

The spawn prompt asked three questions, and this paragraph answers each. First, the definition of a unit and the stop do not read one way to the three parties: findings 1, 2 and 3 name the clauses that read two ways. A fix pass can apply a proofer's paste-ready fix that adds a private helper without meeting the stop, on the reading finding 2 names, wherever the frame states the behaviour the helper carries out. Second, of the three departures `trail/phases/phase-1.md` records, the first holds and the frame was not folded with it (finding 6). The second holds, but it missed a fourth sentence of the section (finding 7). The third holds in substance, but its sentence copies the other paragraph and cites the wrong one (finding 4). Third, the ground the frame gives for rejecting every mechanism beside the text holds for the crafter's stop and not for the orchestrator's two acts (finding 9).

## Findings

### 1. The definition does not tell a new unit from a change to a body: an existing part the frame never names, and a rule sentence added to a section, each read both ways

```seal
severity: should
location: `skills/implement/fix-pass.md:52-71`, `skills/code-review/orchestration.md:228`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:41-43`
evidence: read `skills/implement/fix-pass.md:46-71`, `agents/framer.md:224-226`, `skills/implement/orchestration.md:72-74`, `skills/code-review/orchestration.md:228`; executed `python3 -I test_tmp_md_units.py` from the round's scratch directory, over the repository's object store
```

Why it matters: the stop is the work's one new judgment, and a crafter and an orchestrator that read its condition differently send the same finding down different routes. Two clauses read two ways.

The first is the existing part. The stop fires where "a finding's fix needs a unit the frame does not name" (`skills/implement/fix-pass.md:64-65`). The condition does not say "new". The definition calls every file, function, module-level name and section a unit (`:52-56`), and its exemption says "A change to the body of a named unit is not a new unit" (`:58-59`). A fix that changes the body of an existing helper the frame never mentions, such as a function under `lib/` that no phase of this work item built, therefore needs "a unit the frame does not name" on a literal reading, and the pass stops. The bold lead says the unit "is built only once the framer's fold has designed the unit" (`:46-47`), which reads as a unit the fix adds, and on that reading the pass fixes it. "a named unit" at `:58` reads two ways as well: a unit with a name, which every unit is by `:52`, so the sentence would say nothing, or a unit the frame names, which leaves the body of an unframed part unanswered. The frame's own test for naming looks in "the `frame/plan.md` row of the phase that built the code" (`:60-61`), and code no phase of the work item built has no such row. The route table's new cell has the same gap: "where what the fix did is a unit the frame does not name" (`skills/code-review/orchestration.md:228`).

The second is the rule sentence. The definition counts "a rule a procedure gains that adds a mechanism `agents/framer.md` *A mark is not the answer to a blocked step* lists" (`:56-58`). That list is "a gate, a check, a hook, a CI step, a rule, a line grammar, a label or a mark" (`agents/framer.md:224-226`). A rule is on it, so the qualifier filters no rule out, and every rule a procedure gains is a unit. A section is a unit too (`:56`), and a sentence a fix adds to a section is a change to that section's body by `:58-59`. A sentence that states a rule, added to an existing section of a skill, is then a unit by one clause and a body change by the other. This repository's procedures are made of such sections. The orchestrator, which sends a finding before the pass where "its paste-ready fix or its grounds show the unit" (`skills/implement/orchestration.md:72-74`), can read a snippet's new sentence as a rule the procedure gains, and the crafter can read the same sentence as a body change and build it.

G11 and G12 count code declarations only, so no grounding row measures how often the stop fires on procedure text. The probe counted, over the 161 `fixed` commits the round records at HEAD name, 1 that adds a heading and 2 that add a paragraph opened by a bold sentence in `skills/`, `agents/`, `docs/` or `templates/`. That count is a grammar proxy: a rule sentence written into an existing paragraph is not bounded by it.

The definition is the frame's, `frame/design.md` *Scope* item 1 in the same words, so the change is a round finding located in a frame file, a decision the framer folds first (`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*). The fix pass then carries the fold into `skills/implement/fix-pass.md` and the route table cell. Findings 2 and 3 change other sentences of the same paragraph, and none of the three snippets overlaps another. The snippet below replaces `skills/implement/fix-pass.md:52-59` up to "is a new case in a test module." and the first words of the stop at `:64`; whether a rule written as its own paragraph is a unit is the framer's choice, and the snippet takes the reading the bold lead suggests.

```markdown
A unit is a part of the tree with a name or a path of its own: a file or a
directory; a function, a class, a type or a module-level name, private
helpers among them; a hook or its entry; a `seal` subcommand or flag; a
configuration key; a field or a line of a record's form; a section of a
skill, a document or a template; a rule a procedure gains as a paragraph
of its own, opened by its bold sentence; and a gate, a check, a hook, a CI
step, a line grammar, a label or a mark a procedure gains, the other
mechanisms `agents/framer.md` *A mark is not the answer to a blocked step*
lists. A unit is new where the tree at the round's `target:` holds no part
by its name or path. A change to the body of a unit the tree already
holds, whether or not the frame names it, is not a new unit: a sentence a
fix adds to an existing paragraph is one, and so is a new case in a test
module.

Where a finding's fix needs a new unit the frame does not name, a
paste-ready fix's among them, ...
```

The route table cell at `skills/code-review/orchestration.md:228`:

```markdown
where what the fix did is add a unit the frame does not name, the framer's fold designs the unit before that fix pass, as `skills/implement/fix-pass.md` *A fix that needs a unit the frame does not name waits for the fold* states
```

```seal
verdict: fixed 474d41883
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/changelog.md`
answer: Built to the framer's fold at `d154f13fd`, `frame/design.md` *Scope* item 1, not to the snippet. `skills/implement/fix-pass.md` now defines a unit as a new name or path the frame holds nowhere, new where the tree at the round's `target:` holds no part by it, and drops "a rule a procedure gains" and "a section" for "a heading". A paragraph of its own says a change to the body of a part the tree already holds, whether or not the frame names it, adds no unit, a sentence added to a section among them. The stop reads "a unit the frame does not hold". The route table cell at `skills/code-review/orchestration.md:228` reads "where what the fix did is add a unit the frame does not hold". The changelog's first item and its first *Process changes* row state the new definition. The frame's half is the fold's.
```

### 2. "By what it does" lets a helper that carries out a behaviour the frame states pass the stop, which is #1612's link chase

```seal
severity: should
location: `skills/implement/fix-pass.md:59-62`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:42`
evidence: read `skills/implement/fix-pass.md:59-71`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:22-24`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/plan.md:20`
```

Why it matters: the spawn prompt asked whether a fix pass can apply a proofer's paste-ready fix that adds a private helper without meeting the stop. It can, on one of two readings of the sentence that says when the frame names a unit.

`skills/implement/fix-pass.md:59-62` says the frame names a unit where a frame section "states the unit by its name or by what it does". A compliance finding is a place where the frame states a behaviour the code lacks, so a helper a fix adds to supply it does what the frame states. On reading A, that helper is named by what it does, and the pass builds it. On reading B, the frame names a part only where it describes that part, as #1612's fold described `_widened` by what it does and not by name (G12, `frame/design.md:22`), and a behaviour the frame states names no part.

G13 (`frame/design.md:23`) is reading A's case. #1612's round 1 finding 3 "went straight to the fix pass, since the frame already said the hook reads no file outside the item's directory", and the guard the fix built covered one place of three. Under reading A the new stop lets that guard through again, and G14 builds *Scope* item 3 on the premise that a fold designs it first. Under reading B the stop holds it. The orchestrator's sort, which sends a finding "where its paste-ready fix or its grounds show the unit", reads B. A crafter judging what its own fix "needs" can read A.

The frame holds the same sentence at *Scope* item 1's second bullet, so the framer folds it first, as finding 1 says.

```markdown
The frame names a unit where `frame/design.md` *Scope* or *Data &
interfaces*, or the `frame/plan.md` row of the phase that built the code,
states the unit by its name, or describes it as a part of its own by what
it does, such as a guard, a reader or a check. A behaviour the frame
states, which the unit would carry out, does not name the unit.
```

```seal
verdict: fixed 474d41883
answer: Built to the fold's reading B, `frame/design.md` *Scope* item 1's second bullet at `d154f13fd`, not to the snippet. `skills/implement/fix-pass.md` says the frame holds a unit where a frame section "writes the unit's name or path", and "A helper whose job the frame states, but whose name the frame does not hold, is a unit". "By what it does" is gone from the file.
```

### 3. A new test module and a helper in a test module are units, which no grounding row measured

```seal
severity: should
location: `skills/implement/fix-pass.md:52-59`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:41`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/questions.md:5`
evidence: read `skills/implement/fix-pass.md:52-59`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:21-22`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/plan.md:24`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/questions.md:5`
```

Why it matters: the stop costs a framer exchange and a resume each time it fires, and the definition lets it fire where the review chain asks for tests most.

The definition exempts only "a new case in a test module" (`skills/implement/fix-pass.md:58-59`). A new test module is a file, and a fixture or a helper in a test module is a function, "private helpers among them" (`:52-54`). Both are units. The counts that ground the definition read units outside the tests: G11 reads "a new file outside `tests/` and `seal/`, or an added line that declares ... outside the tests" (`frame/design.md:21`), and G12 reads the same way. `frame/questions.md:5` grounds "What a unit is, private helpers included" on *Scope* item 1 with G11, and the plan row *Leave private helpers out of what a unit is* (`frame/plan.md:24`) rests on G11 too. So the test half of the definition stands on no measurement.

The cost falls on regression tests. `skills/code-review/SKILL.md` *Probes and regression tests* makes a missing regression test a `should` finding "whose `location:` names the file it belongs in". A fix for such a finding that needs a fixture, or a new module beside a new source file, now waits for a framer fold that designs a test helper.

The frame holds the definition, so the framer folds first, as finding 1 says. Whether test-only parts are exempt or grounded is the framer's choice. The snippet adds one sentence after the exemption that finding 1's snippet writes.

```markdown
A part only the tests read, a new test module or a helper, a fixture or a
constant in one, is not a new unit either.
```

```seal
verdict: fixed 474d41883
answer: Built to the fold, `frame/design.md` *Scope* item 1's third bullet at `d154f13fd`, which exempts test parts and names the stop's stated limit. `skills/implement/fix-pass.md`'s paragraph opening "Two kinds of change add no unit" gives the second kind as "a part only the tests read, such as a test module, or a helper, a fixture or a constant in one". It also says a fix that writes a helper's code into an existing body is not stopped, the stop's stated limit, which answers this round's first *Not judged* row as the fold decided it.
```

### 4. Four statements of the narrowing say "after a fix" where its home says "a fix or a build", and the `skills/implement/SKILL.md` sentence cites the paragraph that holds only one of its halves

```seal
severity: should
location: `skills/implement/orchestration.md:108-112`, `skills/implement/SKILL.md:107-112`, `skills/implement/fold-and-reframe.md:56-59`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:50`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:55`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:59`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:103-117`
evidence: read `skills/implement/orchestration.md:76-112`, `skills/implement/SKILL.md:103-112`, `skills/implement/fold-and-reframe.md:43-60`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/trail/phases/phase-1.md:11`; executed `grep -n -E "what a fix changed|a fix or a build|after a fix"` over `skills/implement/*.md`, `skills/code-review/orchestration.md`, the work item's `frame/*.md` and `changelog.md`
```

Why it matters: the orchestrator folds after every build phase, and a fold the narrowing does not reach is the restatement this work removes.

The home, the paragraph opening **The framer writes a decision's fold**, says "A fold whose source is what a fix or a build changed removes the frame sentence HEAD contradicts, or narrows it" (`skills/implement/orchestration.md:83-86`), and the changelog's fourth item and its second *Process changes* row say the same. Four statements narrow only after a fix:

- `skills/implement/orchestration.md:110-111`: a sentence that says what the work does "is rewritten with a decision's fact, or removed or narrowed where its source is what a fix changed".
- `skills/implement/SKILL.md:108-110`: "a fold rewrites it with a decision's fact, or removes or narrows it where its source is what a fix changed".
- `skills/implement/fold-and-reframe.md:56-57`: "Every other fold after a fix narrows".
- The `to:` of `frame/design.md` `## Rule changes`: "every other fold after a fix only removes or narrows" and "A fold whose source is what a fix changed writes no account of it" (`:104-111`), which the settle writes into `docs/running/the-agent-set.md`.

The orchestrator's fold of a build phase's hand-back, such as this work item's own `947674dfd`, falls under the home and under none of the four. By the sentence the orchestrator reads while it folds (`orchestration.md:108-112`), a sentence of the frame that a build contradicts is "rewritten with a decision's fact", and no decision stands behind it. The framer's fold of a round 1 finding, which follows a build, is outside "after a fix" in the framer's own file. The frame says both: *Scope* item 2's third bullet (`frame/design.md:49`) holds "a fix or a build", and its fourth bullet, *Scope* item 3's last bullet and *Scope* item 5 (`:50`, `:55`, `:59`) hold "a fix".

Departure 3 (`phase-1.md:11`) kept the decision's half of the `skills/implement/SKILL.md` sentence, and that much holds: a decision's fold still rewrites. But the sentence now copies the sentence of the paragraph opening **One fold reaches every statement of the fact it changes.**, and it cites the paragraph opening **The framer writes a decision's fold** for both halves. That paragraph holds the narrowing alone, and the copy already differs from the home on "or a build".

The four statements in the tree follow. The citation in `skills/implement/SKILL.md` keeps the words `RULES` key `"33 "` reads. The frame's sentences at `:50`, `:55`, `:59` and the `to:` are the framer's to fold.

`skills/implement/orchestration.md:110-111`:

```markdown
that says what the work does or concludes is rewritten with a decision's
fact, or removed or narrowed where its source is what a fix or a build
changed; a
```

`skills/implement/SKILL.md:108-112`:

```markdown
concludes is no claim about that commit: a fold rewrites, removes or
narrows it as the paragraph opening **The framer writes a decision's fold**
of `skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* and the paragraph after it state, and a reader holds it against
HEAD.
```

`skills/implement/fold-and-reframe.md:56-57`:

```markdown
unit already or the unit is not owed, as you reject any decision. Every
other fold after a fix or a build narrows, by the paragraph opening **The framer
```

```seal
verdict: fixed 474d41883
answer: Built to the fold, `frame/design.md` *Scope* items 2, 3 and 5 at `d154f13fd`, which have each statement cite the narrowing's one home and state no scope of its own, in place of the snippets' "or a build". `skills/implement/orchestration.md`, the paragraph opening **One fold reaches every statement of the fact it changes.**, now says a sentence that says what the work does "is rewritten with a decision's fact, and is otherwise folded as the paragraph opening **The framer writes a decision's fold** states". `skills/implement/SKILL.md` says a fold "rewrites it with a decision's fact, and otherwise folds it as" that paragraph states, and keeps the words `RULES` key `"33 "` reads. `skills/implement/fold-and-reframe.md` says "Every other fold is written as" that paragraph states. Key `"33 "`'s links in the last two were seen red again at `474d41883` with `seal mutate`, each removing "the paragraph opening" before the bold lead. `git grep -n -E "what a fix changed|a fix or a build|after a fix"` over `skills/implement/` and `skills/code-review/orchestration.md` now exits 1 and prints nothing, executed after `6d924dc05`; the home's own "what a fix or a build changed" wraps across two lines, so this line search is a sample. The frame's sentences are the fold's.
```

### 5. Where the framer rejects the decision, no step closes the finding the stop left open

```seal
severity: should
location: `skills/implement/fix-pass.md:68-71`, `skills/code-review/orchestration.md:86-94`
evidence: read `skills/implement/fix-pass.md:64-71`, `skills/code-review/orchestration.md:86-94`, `skills/implement/fold-and-reframe.md:55-56`, `skills/implement/orchestration.md:139-144`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:84-86`
```

Why it matters: a finding the stop leaves open while no step answers it holds the round record's one commit, and the run has no step after it.

`skills/implement/fold-and-reframe.md:55-56` lets the framer reject the decision "where the frame names the unit already or the unit is not owed". The two files that say what follows the hand-back state only the path where a fold designed the unit. `skills/implement/fix-pass.md:68-71` says "Once the orchestrator has committed the framer's fold, the fix pass that follows builds the unit to the fold's design and closes the finding, and its `answer:` names the *Scope* item the fold added". `skills/code-review/orchestration.md:88-90` says the orchestrator "sends the finding to the framer, commits the fold, and resumes the fix pass". On a rejection there is no fold to commit, no design to build and no *Scope* item to name. `skills/implement/orchestration.md:139-144` has the orchestrator record a rejection in its row, with "what the decision's source takes instead, a finding's route", but `skills/implement/fix-pass.md` does not send the pass to that row. The round record's one commit waits for "the hand-back that leaves no finding open for a fold" (`skills/code-review/orchestration.md:90-91`). Acceptance row A4 names the rejection (`frame/design.md:86`), and A1 and A2 name no step after it.

`skills/implement/fix-pass.md`, after the stop's last sentence:

```markdown
Where the framer rejects the decision, the fix pass that follows answers
the finding by the route the orchestrator's row of `frame/plan.md`
*Judgments of the run* gives it, and its `answer:` names that row.
```

`skills/code-review/orchestration.md:88-90`:

```markdown
name waits for the fold* has it, ends no pass: the orchestrator sends the
finding to the framer, commits the fold, or its row that records the
framer's rejection, and resumes the fix pass, or spawns it fresh by the
threshold above.
```

```seal
verdict: fixed 474d41883
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/changelog.md`
answer: Both snippets applied as given. `skills/implement/fix-pass.md`'s stop paragraph ends "Where the framer rejects the decision, the fix pass that follows answers the finding by the route the orchestrator's row of `frame/plan.md` *Judgments of the run* gives it, and its `answer:` names that row". `skills/code-review/orchestration.md` has the orchestrator commit "the fold, or its row that records the framer's rejection" before it resumes or spawns the pass. Neither sentence adds a unit by `skills/implement/fix-pass.md`'s own definition: each is a sentence added to a section the tree holds. The changelog's first two items and two *Process changes* rows name the path.
```

### 6. The frame still says the resumed pass builds the unit, where the target lets it be a fresh spawn

```seal
severity: should
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:44`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:57`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:84`
evidence: read `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/trail/phases/phase-1.md:7`, `skills/implement/fix-pass.md:68-71`, `skills/code-review/orchestration.md:34-47`, `skills/code-review/orchestration.md:88-90`; executed `git show 947674dfd`
```

Why it matters: the sealer and the next fold read the frame's *Scope* for what the work does, and these sentences state one case of two.

Departure 1 (`phase-1.md:7`) wrote "the fix pass that follows" (`skills/implement/fix-pass.md:69`) and "resumes the fix pass, or spawns it fresh by the threshold above" (`skills/code-review/orchestration.md:89-90`), because a fix pass is a fresh spawn at the context threshold (`:34-47`). That departure holds, judged against that section. The frame was not folded with it. *Scope* item 1's fourth bullet still says "the resumed pass builds the unit" (`frame/design.md:44`), *Scope* item 4's first bullet "and resumes the fix pass" (`:57`), and acceptance row A2 "resumes the fix pass" (`:84`). `947674dfd` folded two other coordinates of phase 1 and left these three. Where the following pass is a fresh spawn, each states what the work does not do. These are frame sentences, so the orchestrator folds them, by the narrowing.

`frame/design.md:44`, the bullet's opening:

```markdown
   - Once the orchestrator has committed the framer's fold, the fix pass that follows builds the unit to the fold's design and closes the finding, and its `answer:` names the *Scope* item the fold added.
```

`:57` and `:84`, each "resumes the fix pass" becoming:

```markdown
resumes the fix pass, or spawns it fresh at the context threshold
```

```seal
verdict: fixed d154f13fd
answer: The framer's fold rewrote the three sentences. At HEAD `frame/design.md` *Scope* item 1's fifth bullet reads "the fix pass that follows builds the unit", *Scope* item 4's first bullet "resumes the fix pass, or spawns it fresh at the context threshold", and acceptance row A2 "resumes the fix pass or spawns it fresh at the context threshold", read. No tree change was owed.
```

### 7. The prevention home's deadline is still the next spawn, a fourth sentence of the section that departure 2's list missed

```seal
severity: should
location: `skills/implement/orchestration.md:170-176`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/trail/phases/phase-1.md:9`
evidence: read `skills/implement/orchestration.md:21-178`; executed `git grep -n -i -E "spawn" -- skills/implement/orchestration.md`
```

Why it matters: a home that lands after the resume it was meant to precede lets the recurring problem run once more in the resumed pass.

Departure 2 (`phase-1.md:9`) says "Three other sentences of the section gave the fold's deadline as a spawn alone", and "Each now names the spawn or the resume, since a fold for a unit is read by a resumed fix pass". The section *Orchestrator: the order inside a ticket* holds a fourth. "the orchestrator gives it a home before the next spawn" (`skills/implement/orchestration.md:171-172`), and "The home is a decision, so the framer folds it" (`:174-175`). Where the problem recurs in a fix pass, the next act is a resume, which "the next spawn" does not name, so a resumed pass can run before the home. The departure's three were named as the section's set, and the spawn search over the file lists the fourth. Departure 2 otherwise holds, judged against contract rule 19: the three sentences it changed, and the change of "rewrites" to "folds" at `:108`, read as the new rule reads.

```markdown
the same problem appears a second time in one run, the orchestrator gives it
a home before the next spawn or resume: a mechanism that stops it, or a rule written
```

```seal
verdict: fixed 474d41883
location: `tests/text/test_the_rules_have_one_owner.py`
answer: `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* now gives the prevention home "before the next spawn or resume", with the paragraph rewrapped. `git grep -n -i "before the next spawn"` over the tree outside `seal/threads/` then printed one more statement, the docstring of `tests/text/test_the_rules_have_one_owner.py#test_a_recurring_problem_gets_a_prevention_home`, which `6d924dc05` rewrote the same way. A search on words is a sample. The record `trail/phases/phase-1.md:9` stays as the phase wrote it, since a fix pass writes no phase record.
```

### 8. The follow-up row cites `frame/design.md` G11, which the settle removes before the owner answers the row

```seal
severity: should
location: `seal/follow-up.md:46`
evidence: read `seal/follow-up.md:43-46`, `docs/layout/the-record-layout.md:21`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:21`
```

Why it matters: the owner answers this row at the next release and compares the folded units against a measurement the row only points to.

The row reads "whose folded units are followed by a `regression:` or `reopens:` line as often as #1614's `frame/design.md` G11 measured for unframed ones". `seal/follow-up.md` outlives the release (`docs/layout/the-record-layout.md:21`). The settle removes the work item's directory with its `frame/design.md` (`skills/settle/SKILL.md`, its description). The owner who answers the row then finds no G11 at HEAD, and the row names no commit to read it at. The two rows above it carry their measurement in the row, as in "the 14 of 72 that #1613 measured".

```markdown
as often as the unframed ones #1614 counted on 2026-11-25: of the `fixed` commits that added a unit, 7 of 14 in this repository and 20 of 36 in owlery were followed by such a line, against 127 of 522 and 31 of 147 of those that added none
```

```seal
verdict: fixed 6ee02726f
answer: The orchestrator's commit wrote the counts into the row. At HEAD `seal/follow-up.md:46` reads "as often as the unframed ones #1614 counted on 2026-11-25: of the `fixed` commits that added a unit, 7 of 14 in this repository and 20 of 36 in owlery were followed by such a line, against 127 of 522 and 31 of 147 of those that added none", read; `0fd12e5ba` changed the same row for the held commit and left that clause.
```

### 9. The frame rejects every mechanism beside the text on a ground that holds for the crafter's stop and not for the orchestrator's two acts

```seal
severity: should
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/plan.md:17`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/plan.md:26-33`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:26`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/pr.md:1`
evidence: read `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/plan.md:15-36`, `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:25-26`, `skills/implement/fix-pass.md:3-4`, `skills/implement/orchestration.md:72-74`, `skills/code-review/orchestration.md:86-94`, `skills/code-review/scripts/chain_check.py:1420-1427`
```

Why it matters: the routing gave the framer which mechanism beside the text holds the order, and the frame answers it for one of the three acts.

The chosen row's verdict says "The text is read at the call, the condition 0.38.8's hook was built to meet (G16)" (`frame/plan.md:17`). G16 quotes 0.38.8: the orchestrator "read the rule when it wrote `routing.md` and still stopped an unattended run twice, since nothing put the rule in front of it at the call". It then says the fix pass's stop is read at its call, because the pass opens `skills/implement/fix-pass.md` before it judges the first finding (`frame/design.md:26`). That holds for the crafter (`skills/implement/fix-pass.md:3-4`). The orchestrator's two acts are the sort before the pass (`skills/implement/orchestration.md:72-74`) and the round record's commit held until no finding waits for a fold (`skills/code-review/orchestration.md:86-94`). The orchestrator reads both files once, before round 1, and acts on them rounds later. That is 0.38.8's condition, not the one G16 claims. Every mechanism row the plan weighs (`frame/plan.md:26-33`) is a hook or a tool on the crafter's edits, its hand-back or its range, and none weighs the orchestrator's half.

The orchestrator's half has two backstops the frame does not name. The crafter's stop catches a finding the sort missed, at the cost of one hand-back and one resume. A round record committed with a finding left open is refused as `open` by `chain_check.py` (`:1426-1427`), but that refusal blocks only the ready pull request, rounds later. A check that refuses a round record while an earlier record holds a finding with no close block reads an exact fact, and no row weighs it. The answer is the framer's: weigh that check, or narrow the chosen row's ground to the crafter's stop and name the backstops. `pr.md:1` quotes the verdict cell, so the quote follows the fold word for word.

```markdown
| ... | ... | chosen (`frame/design.md` *Scope* items 1 to 5). The crafter's stop is read at the call, the condition 0.38.8's hook was built to meet (G16), and a unit is a meaning question an agent answers (G1). The orchestrator's sort and its held commit are read once a session; the crafter's stop catches a finding the sort missed, and `skills/code-review/scripts/chain_check.py` refuses a finding left with no close block |
| `chain_check.py` refuses a round record while an earlier record of the work item holds a finding with no close block | (the framer's failure scenario) | (the framer's verdict) |
```

The second row's last two cells are the framer's to write, so the snippet leaves them as words in parentheses.

```seal
verdict: fixed d154f13fd
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/questions.md`
answer: The framer's fold narrowed the chosen row's ground to the crafter's stop, named the backstops of the orchestrator's sort and held commit, and weighed four mechanisms on the orchestrator's half in `frame/plan.md` *Alternatives considered*, the `chain_check.py` check among them, each rejected; `frame/questions.md`'s line on mechanisms names the new rows, read. `pr.md:1` quotes the new verdict cell at `0fd12e5ba`, and its words stand in `frame/plan.md`'s cell, read. No tree change was owed.
```

### 10. The `## Rule changes` `to:` repeats the reason `skills/implement/fix-pass.md` keeps, so the settle leaves the passage in two files

```seal
severity: should
location: `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/frame/design.md:103-117`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.0 --root <the branch worktree> --worktree`; read `skills/implement/fix-pass.md:46-50`, `skills/implement/orchestration.md:83-88`
```

Why it matters: after the settle writes the `to:` into `docs/running/the-agent-set.md` *What each party writes, and when*, the reason for the stop stands there and in the procedure. The next change rewrites one and leaves the other.

The check printed this notice at `frame/design.md:103`: "this `to` repeats a passage of `skills/implement/fix-pass.md`: 5 of its runs of 15 words stand there, one of them "fix pass designs and builds in one act reaches the next round with no judge"". The `to:` reads "A unit a fix pass designs and builds in one act reaches the next round with no judge but its builder" (`:106-107`), and `skills/implement/fix-pass.md:47-48` keeps "A unit the fix pass designs and builds in one act reaches the next round with no judge but its builder". Its clause "since the code, its docstring and the finding's close block hold that" (`:111-112`) restates the home at `skills/implement/orchestration.md:86-88` as well. The policy's sentence can cite the procedure for the reason, as it already cites it for the definition.

The snippet also carries finding 4's "or a build". The framer folds it, and the parse G24 ran is run again over the new section.

```markdown
- add
  file: docs/running/the-agent-set.md
  section: What each party writes, and when
  to: **A fix that needs a unit the frame does not name waits for the framer's
    fold, which designs the unit before the fix pass builds it, and every other
    fold after a fix or a build only removes or narrows what HEAD contradicts.**
    The framer judges what the work should be, so it designs the unit, and the
    crafter builds it to that design. What a unit is, the fix pass's stop and
    its reason are `skills/implement/fix-pass.md` *A fix that needs a unit the
    frame does not name waits for the fold*. The order and the narrowing are
    `skills/implement/orchestration.md` *Orchestrator: the order inside a
    ticket*.
    check: tests/text/test_the_rules_have_one_owner.py
```

```seal
verdict: fixed d154f13fd
answer: The framer's fold applied the snippet's `to:`, with "or a build", and dropped the reason and the close-block clause. `python3 -I skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.0 --root <the repository> --worktree`, executed after `6d924dc05`, exited 0 and printed no notice that this design's `to` repeats a passage. Its only lines on this work item name this record's findings as open, which these close blocks answer.
```

## Confirmations

What matched: `skills/implement/fix-pass.md:44` places *Scope* item 1's section between *A paste-ready fix is read before it is applied* and *The narrow set, then the read of the range*, as `frame/plan.md` *Technical context* says, and the section ends with `check: tests/text/test_the_rules_have_one_owner.py` (`:72`), read.

What matched: `tests/text/test_the_rules_have_one_owner.py:378-397` adds key `"32 "` owned by `FIX_PASS_PROCEDURE` with the carriers `ORCH_IMPL`, `ORCH` and `FOLD`, and key `"33 "` owned by `ORCH_IMPL` with `FOLD` and `IMPLEMENT`, as *Scope* item 6 says, read. The plan row's narrow set exited 0 with 199 passed at the target, executed. One link of the phase record's seen-red table was re-derived: with the `fold-and-reframe.md` citation of key `"32 "` removed, `test_every_link_names_the_owner[32 ...]` failed on a line that names that carrier and the owner, executed. The other five rows of that table are carried as the phase's claim.

What matched: the two searches of `frame/plan.md` phase 1's *Verified by* cell each exited 1 at the target, executed, so acceptance row A5's search half holds.

What matched: `changelog.md` ends with `### Process changes` and one row for each of the four procedure files *Scope* items 1 to 4 change, as acceptance row A8 and G17 ask, read. Each list item's claims were read against the target, and none is contradicted beyond what finding 4 names. The counts in its first item agree with G11.

What matched: each quote of `pr.md` stands word for word at its coordinate, `frame/plan.md:17` and `frame/questions.md:14`, read. Finding 9's fix changes the first one's source.

What matched: `seal/follow-up.md:46` holds *Scope* item 8's row, with each of its three mechanisms and the repository owner as its answerer, read. Finding 8 is the one defect in it.

What matched: `gaps.md` holds three `## Not verified` rows, each naming who answers it. Its second row's question is this round's, and findings 1, 2, 3 and 5 answer it.

No case of the diff is new: the two `RULES` rows are data for the existing `test_every_link_names_the_owner`, and the docstring change at `:595-596` follows the bold lead's new deadline.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a fix the pass writes in its own words, with a helper's code put into an existing function's body, is meant to escape the stop. `skills/implement/fix-pass.md:58-59` makes such a change no new unit, so the stop as written rewards inlining over a named helper | `skills/implement/fix-pass.md:28-42`, `skills/implement/fix-pass.md:58-59` | the framer, in the fold findings 1 to 3 send |
| Whether the passage check reads key `"33 "`'s bold-lead citation as `phase-1.md:15` says of `skills/settle/scripts/passages.py#SECTION`, carried as the phase's claim and not re-derived | `seal/threads/1795590951-a-fix-builds-a-unit-no-frame-designed/trail/phases/phase-1.md:15` | the orchestrator's broad gate, which runs `tests/text/test_no_passage_is_pasted_into_a_second_file.py` |
| The suite beyond the plan row's set, the repository-wide lint and the format check, `unverified` | the tree at `8562ea70f` | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py tests/skills/test_passages.py`, in the clone at the target | exit 0, 199 passed |
| `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py -k test_every_link_names_the_owner`, with the citation of `skills/implement/fix-pass.md` *A fix that needs a unit the frame does not name waits for the fold* in `skills/implement/fold-and-reframe.md:45-47` replaced by "the fix pass's file" through `Edit`, then restored with `git checkout` | exit 1, one case failed, key `"32 "`, on a line naming `skills/implement/fold-and-reframe.md` and the owner; the clone's `git status --short` then printed nothing |
| `python3 -I test_tmp_md_units.py <repository>`, over the `fixed` commits named by every `trail/rounds/round-*.md` at HEAD | 161 commits; 1 adds a heading, 2 add a paragraph opened by a bold sentence, 0 add a `check:` line in `skills/`, `agents/`, `docs/` or `templates/`; 8 add a `def`, a `class` or an upper-case module name in a `.py` file outside `tests/`. The first run pointed at the clone, which lacks the objects of squashed branches, and was run again against the repository's own object store; the figures above are the second run's |
| `git grep -n -F 'is folded with the fact it' -- agents skills docs templates` and `git grep -n -F 'a fold rewrites it with the fact' -- agents skills docs templates`, in the clone at the target | each exit 1, nothing printed |
