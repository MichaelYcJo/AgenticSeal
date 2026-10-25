# 1792540458-on-demand-files-state-the-current-rule — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | dcd25bf4 |


## What this phase was asked

`skills/verify/SKILL.md` rewritten to the current rule and split along its
own headings: *The broad gate* and *Measure the segment, and feed the flow
log* move to a new `skills/verify/orchestration.md`, under headings without a
dash and below an opening paragraph saying the orchestrator reads it and the
smith and the sealer do not. Every citation outside `docs/` names the new file
in the same commit: `skills/commit-pr-convention/SKILL.md`, the measurement
paragraph of `skills/implement/orchestration.md`, `broad_gate.py` and
`session_cost.py`. The two `docs/` citations are the `## Rule changes` items
already in `spec.md`. Every imperative sentence whose actor or condition the
smith had to choose is listed here for the warden.

## What this phase found

**The frame holds for this phase, with two additions.**

- `.github/scripts/roll_flow_measurement_issue.py` cites the moved section
  four times, once in the comment it posts when it closes a log, so it is
  moved with the others (S9). The posted sentence is a string a person reads
  and no case pinned it, so
  `tests/test_a_release_rolls_the_flow_measurement_issue.py#test_the_close_comment_names_the_version_this_release_shipped`
  now holds its path (dcd25bf4; red under `mutation-check` with the old path
  put back, executed).
- `skills/code-review/orchestration.md` now links
  `skills/verify/orchestration.md` *The broad gate* at the step that runs the
  gate. Without the link the orchestrator meets the new file only through
  `skills/implement/orchestration.md`'s measurement paragraph, and the
  section holding what each word beside a failing file means is not on its
  path at the act.

**A stored count was stale since phase 3.** The broad gate section said a
run on a SpecSeal feature branch reads `CI also · 3 more steps`, three of the
six CI runs for that base. Since phase 3 removed the copy's step the release
job runs five steps for a release-branch base and the run answers three, so
the line reads two more (executed, `broad_gate.coverage_line` over the
workflow for `release/v0.22.3`). The example left the file rather than being
corrected: the gate prints the count, and a copy of it in a document goes
stale at the next step added or removed. The pin that held it now refuses
the sentence's return.

**"you" in a file three parties read.** `skills/verify/SKILL.md` is opened by
the smith, the sealer and the orchestrator, and its "you" read as any of
them. The opening now says each instruction binds the party making a claim,
and every "you" became that party, the claim's tree or an impersonal clause.
`skills/verify/orchestration.md` has one reader and no "you".

**"A claim is sealed" read as the sealer's verdict.** `sealed` is the word the
sealer's `guarantee.md` writes; the opening now says a claim *stands*. The
Scope table's `Seal` column became `Label`, because its cells are condition 4's
labels.

**The title names the concept every citation already uses.** Three files
cite `skills/verify/SKILL.md` *The Seal Test*, a heading no file carried
(`broad_gate.py`, `templates/config.md`, and test comments; read, `git grep`).
The title `# verify — the smith's own gate before handoff` is now
`# The Seal Test`, which also drops a dash and a claim that only the smith
opens the file.

**What stays in `SKILL.md` and why.** The four conditions with `arm-check`
and `mutation-check`, the procedure, the hand-back's labels and the one seal
(`agents/sealer.md` links that heading, and agents are out of scope), the
scope rule and its three ways back, the cost of a repeated run, and the
counterfeits. The Scope table's last row names the orchestrator and links
*The broad gate*. The whose paragraph in the hand-back section restates
`skills/writing-style/SKILL.md` *여럿이 가질 수 있는 것은 누구 것인지 밝힌다*, and
it stays: `tests/test_one_word_one_meaning.py` holds this file as its owner
(`SEAL_OWNER`) and `agents/sealer.md` links it. Moving the owner is a change
to the sealer's preload, which is the later item's.

**The three notes on comparing readings across a change stay, shortened.**
The measurement section carried, for #300, #377 and #642, what a reader
comparing a reading taken before the change must know. The durable
`flow-baseline` log holds readings across versions, so an orchestrator holding
an old reading would misread it without them. Each is now one sentence after
the current rule, and keeps its issue number because the number is how a
reader finds the release that changed the rule.

**Headings renamed or moved** (S14, `git grep` of each old text outside
`seal/`, `changelog/` and `docs/`, executed; none is cited in `docs/`):

| Old | New |
|---|---|
| `# verify — the smith's own gate before handoff` | `# The Seal Test` |
| `### 4. Executed, read, or unverified — labeled` | `### 4. Each claim labelled executed, read or unverified` |
| `## Scope — cheap and often, broad and once` | `## Scope: cheap and often, broad and once` |
| `## The cost of the run you repeat` | `## The cost of a run that repeats` |
| `## The broad gate — after the rounds, then compare against the base` | `skills/verify/orchestration.md` `## The broad gate` |
| `## Measure the segment, and feed the flow log` | `skills/verify/orchestration.md`, the same heading |

The one hit for the old title's words is `README.md`'s sentence calling
`verify` the smith's own gate, which is prose about the skill and no citation.

**Section signs.** `skills/verify/SKILL.md` holds none. The orchestration file
holds `contract §2`, `contract §6`, and the `§6` line `session_cost.py`
prints, all the contract's numbers. The `.py` files keep their section signs
with the new path, as `spec.md` Scope 8 leaves them to a later item. The
citation of `templates/config.md` *Choosing a value — the criterion* keeps
that heading's dash until phase 7 renames it.

**Census (S11): what left, and why it could go.**

| What left | Grounds |
|---|---|
| *The community baseline … stops at freshness* | folded into one sentence: freshness alone accepts any green command |
| `arm-check`: #262's table of 33 arms against 31, *#262's own table … is a `remove` count*, *because #262's table is a removal count*, *Three of this module's arms are that shape* | history; the rule that a hand count goes stale and the two operators stay |
| the operator table's third column, measured 2026-09-09 on a hook since removed, and its paragraph | a measurement of nothing in the tree; replaced by the rule that a survivor count is taken with the command and never written down |
| *Whether the bound should reach the whole process group is #313*, and `(#313)` in `mutation-check` | an open issue's number; the limit itself stays stated |
| *each used to print `killed`* | history; the reason stays in the present |
| `(#129)`; *Measured 2026-10-01 … 0.6 s a run against 0.02 s* | history and anecdote; the reasons stay |
| *the rotted hand count with a shebang on it* | figure of speech; the rule stays |
| condition 4's middle dots, the procedure's arrows and en dash | rule (a): a list and words |
| Scope: *twenty broad runs, every one of them followed by more edits* | anecdote; the rule stays |
| *Both were measured, and both looked like a sealed claim* | anecdote, and it said two ways where the section gives three |
| the narrow command's *Measured: a documentation-only change was sealed* | kept as the example, without the anecdote |
| the answerer's *Measured: a session narrowed to a single domain's tests* | condensed to the general case: workflows that run no suite, a hook on the committer's machine |
| *One here said the gates had never been seen rendering in a TUI* | anecdote |
| *(#272). Before that, squashing one item turned every sibling red* | history |
| the cost section's 131s and 137s, 225s and 83s, 194s and 203s, and `(#544)` | anecdote; the rules and the fenced example stay |
| the counterfeits' *Measured: a `mypy .` that died in four seconds* | anecdote; the counterfeit stays |
| broad gate: *The rule used to say when the gate fires …* | history |
| *(#638)*, *(#423)* with *used to pass green*, *(#832)*, *(#666)*, *(#473)* | issue numbers and history; the rules stay |
| *for three releases the list was kept in step … #424 added a step* | history; the declaration and its two failure directions stay |
| the stale feature-branch example, above | a stored count |
| *Measured: a session ran a 19,000-test suite serially*; *Measured on one repository: ten failures* | anecdote; the reason stays in one sentence |
| measurement: *What was measured is that this meter sat unreferenced* | history; *nothing here does* stays |
| *where this step used to be one invocation per transcript*; *the split that used to be done by eye*; *a cycle counted as a segment is how three segment kinds came to have bands* | history |
| the run table's middle dots and `(#174)` | rule (a) and an issue number |
| *what they say is yours* | the orchestrator's, named; the sentence was reworded so it shares no run with `docs/measuring-a-run.md`, which states the same reason |

**Cases rewritten or retired** (each seen red after its commit by
`mutation-check` on the new text, executed):

| Case | What changed |
|---|---|
| `tests/test_a_segment_feeds_the_flow_log.py`, every case | reads `skills/verify/orchestration.md`; the section reader takes the file's last section; the order case became `#test_the_section_is_the_orchestrators_and_the_smiths_skill_names_it` (new pin: the smith's file carries no copy, prices the repeated run, and names the orchestrator's file in its opening) |
| `tests/test_broad_gate_rule.py`, five cases | the broad gate read from the orchestration file; the citation form without a section sign; `#test_verify_says_when_not_only_what` also holds the broad gate absent from `SKILL.md` and the opening's two sentences (new pin); the cost heading |
| `tests/test_arm_check.py#test_the_skill_calls_its_survivor_counts_a_measurement_and_not_a_property` | holds the new sentence and refuses a count's return |
| `tests/test_one_word_one_meaning.py` | `SEGMENT_OWNER` is the orchestration file; `SEAL_SWEPT` and `SEGMENT_SWEPT` read it too |
| `tests/test_the_seal_is_taken_once_by_the_sealer.py`, four cases | read the orchestration file; the `CI also` sentence without dashes; the stored count refused |
| `tests/test_the_gate_names_every_step_ci_runs.py`, `tests/test_the_gate_asks_the_range_ci_will_ask.py` | read the orchestration file |
| `tests/test_the_chain_section_has_one_shape.py`, `tests/test_the_handoff_before_round_one.py` | the table's owner is the orchestration file; the first row is `Rounds, finding and verifying`; the bars section in `docs/` may name either path until the settle applies the rule change |
| `tests/test_absence_claims.py` | *a case known to be present* |
| `tests/test_session_cost_post.py`, a comment in `tests/test_one_word_one_meaning.py` | the citation's path |

**The restatement check reads the tree through `git ls-files`.** The first
run over this phase's module set passed with the new file untracked, so the
check did not see it; after the commit it found two shared runs with
`docs/measuring-a-run.md` and the sentence was reworded at 291bebcc. A phase
that adds a file stages it before its boundary run.

**Imperative sentences whose actor or condition the smith chose.**

| Sentence | What was chosen |
|---|---|
| `SKILL.md` opening: *the smith opens it before it hands work back, and the sealer opens it for the conditions, the labels and the verdicts* | the two parties and the moment each opens the file |
| *Each instruction below binds the party making a claim, whichever of the three it is* | the actor of every bare imperative in the file |
| *A suite the party making the claim did not run is `unverified`* | the actor, which was "you" |
| *restore it from the commit made before the run* | the commit, which was "your commit" |
| Scope table: *full suite, lint, typecheck, once, by the orchestrator* | the actor of the last row |
| orchestration opening: *The smith and the sealer open that one and never this one, because contract §2 … and contract §6 …* | the grounds for who does not open it |
| *After every smith or warden segment ends, the orchestrator measures its transcript* | the actor, which the sentence left out |
| *the orchestrator takes the two steps as part of the segment that just finished* | the actor, which was a bare imperative |
| *The orchestrator does this before the next segment spawns* | the actor and the moment |
| *the orchestrator posts to it without asking whether to* | the actor, which was "whoever is watching a segment finish" |
| *It refuses without `--says`: what the numbers mean is the orchestrator's sentence to write* | whose sentence it is |
| code-review step: *`skills/verify/orchestration.md` *The broad gate* says what the run covers* | where the link sits: the step that runs the gate |

**Restatement pairs of these files** (Scope 10, measured at 291bebcc with the
module's own `shared_counts`, executed):

| Pair | Measured | `BASELINE` | Whose the residue is |
|---|---|---|---|
| `agents/sealer.md`, `skills/verify/SKILL.md` | 0 | 1 | drained; phase 9 removes the entry |
| `docs/measuring-a-run.md`, `skills/verify/SKILL.md` | 0 | 1 | drained; phase 9 removes the entry |
| `docs/one-root-by-lifetime.md`, `skills/verify/SKILL.md` | 0 | 3 | drained; phase 9 removes the entry |
| `skills/code-review/orchestration.md`, `skills/verify/SKILL.md` | 0 | 5 | drained; phase 9 removes the entry |
| `skills/verify/SKILL.md`, `templates/sdd-phase.md` | 0 | 10 | drained; phase 9 removes the entry |
| any pair of `skills/verify/orchestration.md` | 0 | none | the new file shares no run |

**Bytes** (executed `wc -c`): `skills/verify/SKILL.md` 54,220 at b3154f43 and
21,960 at 20102a80; `skills/verify/orchestration.md` 28,976.
