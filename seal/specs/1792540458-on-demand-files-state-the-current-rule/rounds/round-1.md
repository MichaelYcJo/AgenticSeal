# Review round 1: 1792540458-on-demand-files-state-the-current-rule

target: 4ce4daf0 against release/v0.22.3

The base is `release/v0.22.3` at b3154f43. This is round 1, so no earlier
round's coordinates were carried; every fact below was established this
round, in a `git clone --no-local` at 4ce4daf0. The implementer's account
(`overview.md`, `phases/phase-1.md` to `phase-9.md`, and the spawn prompt)
was read as claims, and each finding says what was claimed and what the tree
shows.

## Findings

### 1. The block's routing bullet tells a session to write `routing.md` under every answer, and names no file for question 1 or the boxes

severity: should
location: `templates/claude-md-block.md:16`
evidence: read `templates/claude-md-block.md:16`, `skills/implement/orchestration.md:279-287`, `skills/implement/SKILL.md:28-30`, `seal/specs/1792540458-on-demand-files-state-the-current-rule/phases/phase-2.md:61`
verdict: open

Every session on a machine with the plugin reads this bullet, and it is the
only routing text a session in a repository that already has a `seal/` root
is sure to read. Two things it needs to act correctly are gone.

First, the condition on the write. The bullet says "Before the first edit,
write `seal/specs/<work-item-id>/routing.md` ... then commit it" with no
exception, and only afterwards "Under `no work item`, every commit carries
`: '[no-review]';`". A session that was answered `no work item` reads both
sentences as applying, writes a declaration nobody gave, and the commit gate
then reads the branch as a declared work item. The old bullet said "no
frame, no review, no seal, no `routing.md`" for that answer. Phase 2's map
(`phases/phase-2.md:61`) claims question 1's options are kept in the block
as "the three labels" and land in *Question 1*; `orchestration.md:287` does
hold "no `routing.md`", but the block never sends a rooted repository's
session there, so the condition left the one text that session reads. Phase
3 claims for this sentence "the moment is the first edit; done is the
commit"; the condition is the part that dropped out, which is the defect
`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*
rule 3 names.

Second, the referent. "Ask question 1 alone; the boxes in a second call"
does not say what question 1 asks or what the boxes are, and the bullet
names `skills/implement/orchestration.md` only under the Bootstrap
condition. Where a root exists, the pointer to the file holding both is
`skills/implement/SKILL.md:28-30`, which reaches only a session that has
loaded the implement skill.

Both repairs together put the block at 1,669 bytes with finding 2's fix
(executed `wc -c` on the candidate), over Scope 2's 1,500. `questions.md` Q4's
default covers that: the phase record names each sentence over and why it is
a rule. `tests/test_first_setup_asks_once.py` reads the lead before
"write `seal/specs/" for `Bootstrap`, which the text below keeps, and
`tests/test_review_axes.py` refuses the box vocabulary in the block, which it
does not add.

```markdown
- **Routing, decided at the start.** Where `seal/` exists at neither `<repo>/seal/` nor `$(git rev-parse --git-common-dir)/seal/`, first follow the Bootstrap section of `skills/implement/orchestration.md`; where the root lands is the user's decision. **Ask question 1 alone; the boxes in a second call only under `per axis`.** Its answers are `automation`, `per axis` and `no work item`, and that file's *Orchestrator: how the work is routed* states the question and the boxes. Except under `no work item`, write `seal/specs/<work-item-id>/routing.md` from `templates/sdd-routing.md` before the first edit, in a command of its own, then commit it. Under `no work item`, every commit carries `: '[no-review]';` in front of it, `[no-parity]` too where a migration config is declared.
```

answer:

### 2. The block states two rules for one lint run: before every commit, and once after the rounds

severity: should
location: `templates/claude-md-block.md:14`, `templates/claude-md-block.md:8`
evidence: read `templates/claude-md-block.md:8`, `templates/claude-md-block.md:14`, `skills/agent-contract/SKILL.md:39-42`, `skills/code-review/orchestration.md:301-303`
verdict: open

Line 14 says "Run lint, format and typecheck before committing." Line 8
says "the full suite, lint and typecheck run once, after the review rounds
settle". A smith commits at every phase, so the two lines give it opposite
instructions for the same word, and contract §2 forbids the second reading
to every agent ("the repository-wide lint ... no agent runs any of the
three"). Both lines were rewritten in phase 3, and phase 3's census
(`phases/phase-3.md`) folds the Verification Scope sentence without naming
the clash. The intended reading is the narrow one:
`skills/code-review/orchestration.md:301-303` has the orchestrator run "the
lint of its changed files" at a phase boundary. Naming the scope of each
removes the second reading; `tests/test_broad_gate_rule.py:365` still finds
`Verification Scope` in the block.

```markdown
- **Verification Scope**: narrow and often; the full suite, the repository-wide lint and the typecheck run once, after the review rounds settle, and an edit after that run spends it.
```

```markdown
- Before each commit, run lint, format and typecheck over the files it changes.
```

answer:

### 3. "The default branch" names the release branch two sentences after the release branch was called the default

severity: should
location: `skills/implement/orchestration.md:475`
evidence: executed `sed -n 460,478p skills/implement/orchestration.md`, `git show b3154f43:skills/implement/orchestration.md`
verdict: open

The paragraph at lines 460 to 467 says "The release branch is the default."
Line 475 then says "Where the repository gathers fragments, basing on the
default branch means running the gather". Read in place, the orchestrator
runs the release gather for every pull request into the release branch,
which is the shared-region collision the paragraph exists to prevent. The
base text said "basing on `main` means running the gather, because that is
the branch where the entries are due"; the rewrite swapped `main` for a
phrase this file had just given another meaning, and dropped the reason.
Phase 2's imperative-sentence list does not name this sentence.

```markdown
Where the repository gathers fragments, basing on `main` means running the
gather, because `main` is the branch where the entries are due; the
contribution guide names the command.
```

answer:

### 4. The routing template says the orchestrator answers the routing question, where the hook reads the person's answer in the session's transcript

severity: should
location: `templates/sdd-routing.md:90`
evidence: read `templates/sdd-routing.md:88-91`, `hooks/question-gate.py:17-22`, `skills/implement/orchestration.md:369-372`
verdict: open

The comment says `hooks/question-gate.py` refuses every question "but the
routing question put alone before the orchestrator has answered it". The
orchestrator puts the question; the person answers it, and the hook lets the
question through while "this session's transcript ... holds no answer to it"
(`hooks/question-gate.py:17-18`). `skills/implement/orchestration.md:371`
still says "before the session has answered it". Phase 7 replaced "the
session" with "the orchestrator" throughout this template, which is right
where the session means the party and wrong here, where it means the
conversation. An orchestrator reading this line can conclude its own
earlier question counts as the answer. The rest of the template's
replacements were read and hold.

```markdown
     WHAT HOLDS IT is `hooks/question-gate.py`. While the row reads `yes`, it
     refuses every question on this branch but the routing question put
     alone before the person has answered it in this session, so the run
     builds on the default a question states instead.
```

answer:

### 5. Section 6 names the sealer's spawn as the moment to drain rows, which falls after the broad run that a drain makes stale

severity: should
location: `skills/implement/SKILL.md:474-483`, `skills/code-review/orchestration.md:173-176`
evidence: read `skills/implement/SKILL.md:472-483`, `skills/code-review/orchestration.md:173-185`, `agents/sealer.md:54-63`, `skills/verify/orchestration.md:149-151`
verdict: open

The section says "The orchestrator moves every unresolved row out before it
spawns the sealer", and its table says a doable item is "done now ...: the
sealer's spawn is the last moment before the pull request opens".
`skills/code-review/orchestration.md:173-185` orders the steps as preflight,
broad run, commit `broad-gate.md`, then the sealer's spawn. The last moment
before the sealer is therefore after the broad run. Each destination in the
table then breaks a later check:

- a doable item is a code commit after the broad run, which
  `skills/verify/orchestration.md:149-151` forbids, and which the sealer
  answers with `Verdict: withheld reason: no broad run at HEAD`
  (`agents/sealer.md:54-63`);
- a row moved to `seal/follow-up.md` is a path outside
  `seal/specs/<item>/`, which the same step of the sealer reads as a stale
  record.

The frame dictated the moment (`spec.md` Scope 9: "moves each row out before
it spawns the sealer"), and phase 9 built it as framed, so the defect is the
frame's sentence carried into the skill. The moment that satisfies Scope 9's
grounds and the broad run is after the last round settles and before the
preflight; `code-review/orchestration.md` lists the steps taken before the
broad run and is where the drain belongs as a precondition.

```markdown
**The orchestrator moves every unresolved row out once the last round record
has no finding open, and before it runs `broad-gate --preflight`**, whichever
party `routing.md`'s `Implementation` row names: the orchestrator opens the
pull request, and every commit after the broad run, a `seal/follow-up.md` row
among them, leaves `broad-gate.md` stale for the sealer
(`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals, and a phase is re-run*). A row is out when it stands
at its destination below:

| Remaining item | Destination |
|---|---|
| Doable within this pull request | done now, by the party that builds the work item, and reviewed by a verifying round before the broad run |
```

```markdown
sealer's spawn. You take them once you have written the pull request body to
a file, the work item's `changelog.md` states what the work item ships, and
every row `skills/implement/SKILL.md` *6. Drain the rows before the sealer is
spawned, and keep the records* names has reached its destination.
```

answer:

### 6. Two counts are stated twice and disagree: two writing rules against three, and one Bootstrap question against two

severity: should
location: `CLAUDE.md:47`, `skills/implement/orchestration.md:72`
evidence: read `CLAUDE.md:45-55`, `skills/writing-style/SKILL.md:253`, `skills/writing-style/SKILL.md:330`, `skills/implement/orchestration.md:72-73`, `skills/implement/orchestration.md:101-102`
verdict: open

`CLAUDE.md:47` says "two rules bind every sentence of them" and links the
writing-style section, which says "아래 세 규칙" (line 253) and, in the English
link, "the three rules" (line 330). The two directions the owner gave became
three rules in the skill, and the count in `CLAUDE.md` is a second statement
of a value the skill already states, which is rule (a)'s own instance. The
same class stands in the Bootstrap: line 72 says the orchestrator "asks one
question before creating anything", and step 1 at lines 101-102 says "one
`AskUserQuestion` carrying **two questions**". These were the two counts in
the rewritten sentences of the files every session here and every
orchestrator read. A search for other counted rules and questions in the
rewritten files found none that disagree (executed `git grep -n -E
'(one|two|three|four) (rules|questions|question) '` over `skills/*.md`,
`templates/*.md`, `CLAUDE.md` and `CONTRIBUTING.md`: the other hits are
`skills/implement/orchestration.md:178`, which counts the criterion's three
rules as `templates/config.md` does, and an unrelated
`skills/verify/orchestration.md:84`). The search reads one line at a time, so
a count broken across a line end is outside it.

```markdown
A session here writes skills, agent definitions, templates and frames, and
the owner's two directions bind every sentence of them. Nothing an agent
writes or a check
```

```markdown
**When `seal/` exists at neither place, the orchestrator asks once, in one
`AskUserQuestion` call, before creating anything, then does two more things
before continuing.**
```

answer:

### 7. The update skill's sentence on installing a clone's block names no target, and one of `install.sh`'s answers writes a copy back into the clone's `CLAUDE.md`

severity: should
location: `skills/update/SKILL.md:104-106`
evidence: read `skills/update/SKILL.md:103-106`, `install.sh:22-42`, `tests/test_the_installer_writes_the_block_from_its_template.py:76`
verdict: open

Scope 4 makes this sentence the one place that says how a session developing
SpecSeal gets the tree's block: "running `./install.sh` from that clone
installs the clone's block". `install.sh:22-42` writes `~/.claude/CLAUDE.md`
with no argument and no terminal, but with a terminal it asks, and option 2,
like `--project`, writes `$(pwd)/CLAUDE.md`, which from the clone is the
repository's own `CLAUDE.md`. That puts back the copy this work item removed,
and `tests/test_the_installer_writes_the_block_from_its_template.py:76`
(`test_this_repository_carries_no_copy_of_the_block`) then fails the suite.
The sentence names neither the file it writes nor the answer to avoid, which
rule 3 of the writing section asks of an instruction.

```markdown
`templates/claude-md-block.md` is the block's one source, and no other file
carries a copy. A session in a clone of the plugin's own repository reads the
installed block too, which is the last release's, not the clone's:
`bash install.sh "$HOME/.claude/CLAUDE.md"`, run from that clone, writes the
clone's block there. `--project`, or option 2 at the script's prompt, writes
a copy into the clone's own `CLAUDE.md`, which
`tests/test_the_installer_writes_the_block_from_its_template.py` refuses.
```

answer:

### 8. `broad_gate.py`'s docstring cites this repository's `CLAUDE.md` for the Verification Scope rule, which only the template now carries

severity: should
location: `skills/verify/scripts/broad_gate.py:4`
evidence: executed `git grep -n 'Verification Scope' -- CLAUDE.md templates/claude-md-block.md`
verdict: open

Scope 4 rewrites every sentence that stood on the generated copy, and names
`broad_gate.py`'s docstrings. Line 4 says "`CLAUDE.md` §*Verification
Scope* says the full suite ... run once"; that was true here only through
the copy. The search finds the rule in `templates/claude-md-block.md:8`
alone. Phase 3 rewrote the `PARTITION` entry and phase 5 the section path in
the same file, and neither reached this line. The section sign is the later
item's (#1005); the stale target is this item's.

```python
Issue #30. The CLAUDE.md block's **Verification Scope** rule
(`templates/claude-md-block.md`) says the full suite, the
```

answer:

### 9. Phase 9's orchestrator reading compares the base with both verify halves against the new set with one

severity: should
location: `seal/specs/1792540458-on-demand-files-state-the-current-rule/phases/phase-9.md:151-163`
evidence: executed `bash -c 's=0; for p in skills/implement/orchestration.md skills/code-review/orchestration.md skills/implement/SKILL.md skills/code-review/SKILL.md skills/verify/orchestration.md skills/verify/SKILL.md; do s=$((s+$(git cat-file -s 493d9816:$p))); done; echo $s'`, `bash -c 'b=0; for p in skills/implement/orchestration.md skills/code-review/orchestration.md skills/implement/SKILL.md skills/code-review/SKILL.md skills/verify/SKILL.md; do b=$((b+$(git cat-file -s b3154f43:$p))); done; echo $b'`
verdict: open

The record says "Counted with that file, the base is 159,334 against
129,640." The base figure adds the whole of `skills/verify/SKILL.md` at
b3154f43; the new figure adds `skills/verify/orchestration.md` and leaves out
`skills/verify/SKILL.md`, which the orchestrator still reads ("The
orchestrator reads both", `skills/verify/orchestration.md:9-10`;
`skills/verify/SKILL.md:17`). Counted alike, the readings are 159,334 at
b3154f43 and 151,600 at 493d9816. The conclusion holds, the orchestrator's
set is smaller, but the margin the record states is 29,694 bytes where the
like-for-like margin is 7,734. The sealer reads this record and the pull
request body copies record sentences, so the wrong number travels.

```markdown
| orchestrator, with both `skills/verify/` files | 159,334 | 151,600 | yes |
```

answer:

## Confirmations

confirms: none
S1 and S5 hold: `wc -c` prints 1,498 for `templates/claude-md-block.md` and 3,049 for `CLAUDE.md` at 4ce4daf0 (executed).

confirms: none
S2 holds: `git grep -n 'specseal:start' -- CLAUDE.md` prints nothing (executed, exit 1), and `git grep -n claude_block -- ':!seal' ':!changelog'` prints nothing; the one `generated copy` hit is `tests/test_the_installer_writes_the_block_from_its_template.py:162`, which asserts its absence (executed). `.github/workflows/hygiene.yml` holds no step running the script (read, the diff).

confirms: none
S8 holds: the section-sign grep over `skills/*.md`, `templates/*.md`, `CLAUDE.md` and `CONTRIBUTING.md` outside the contract prints only contract numbers and the `§6` label line at `skills/verify/orchestration.md:258`, which `overview.md` names for #1005 (executed).

confirms: none
S13's framer and warden readings are right: 110,562 to 112,603 and 76,287 to 78,706 bytes at b3154f43 and 493d9816, and the same at 4ce4daf0 (executed `git cat-file -s` over each set as `spec.md` lists it). The growth is phase 1's commit 92a89dc7 to `skills/writing-style/SKILL.md`, 3,447 bytes, of which the new section is 2,909 and the two link lines and the description 538; `overview.md` calls all 3,447 "the three writing rules", which is the commit rather than the section, and the reading stands either way.

confirms: none
S16 holds: `bin/rules --check` exits 0, "all 244 check lines in 62 rule files hold" (executed).

confirms: none
The `verify` split loses nothing either party acts on. The broad gate section moved whole, less its history and the stored `CI also` count (read, base `skills/verify/SKILL.md:381-534` against `skills/verify/orchestration.md:14-151`). The smith handles a broad-gate failure from its own definition (`agents/smith.md:143-149`), and the sealer's one cited heading, *The hand-back's labels carry the claims, and the one seal is the sealer's*, stays in `skills/verify/SKILL.md:243` (read).

confirms: none
The block's routing bullet maps to `skills/implement/orchestration.md` as phase 2's table claims for every row but finding 1's (read, base block against the routing, Question 1, Question 2 and What the answer writes sections). The Bootstrap and parity setup sections keep every instruction the base held (read, base lines 44-245 against 60-256).

confirms: none
Moved and renamed headings leave no stale citation outside `seal/`, `changelog/` and `docs/` in the Markdown in scope: 149 of the italic citations in `skills/`, `templates/`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, `agents/`, `hooks/` and the scripts resolve to a heading exactly and two to a heading's leading words (executed, the probe below). The old heading texts appear in `docs/` only at the three lines `spec.md` `## Rule changes` names (executed `git grep` per old heading).

confirms: none
The removed `CLAUDE.md` rows have homes: commit early at `skills/implement/SKILL.md:248`, and the fragment rule at `skills/code-review/orchestration.md:173-180`, which names the party that writes it as the overview's divergence row says (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Rewritten prose this round did not read sentence by sentence for a second reading: `templates/config.md`, `CONTRIBUTING.md` beyond its census, the phase 6 skills other than `commit-pr-convention`, `config`, `legacy-parity`, `update` and `preset-setup`, `skills/writing-style/outside-the-review.md`, and the templates `sdd-questions.md`, `sdd-overview.md`, `sdd-guarantee.md`, `seal-README.md`, `pact.md`, `parity.md`, `hygiene.yml` | the files named | round 2's warden, where the orchestrator's spawn names them |
| The tests run 39531314997 at 4ce4daf0, which the spawn prompt says is running | CI | the orchestrator, who relays a failure |
| The full suite, the repository-wide lint and the typecheck: not run by this round, as contract §2 requires; the suite stays `unverified` | the branch | the orchestrator's `broad-gate` run once the rounds settle |
| Whether the rewritten files leave each agent no worse at its cases, which only the paid non-inferiority run measures | `questions.md` Q1 | the repository owner |

## Probes

| Command | Result |
|---|---|
| `python3 test_tmp_citations.py` in the clone, walking the italic `path` *heading* citations of the tracked Markdown and scripts in scope | 149 exact, 2 leading-words matches (`skills/verify/scripts/session_cost.py:62,2576`); misses only in `.py` files and `agents/`, out of scope, and `skills/verify/scripts/broad_gate.py:4` (finding 8); the file was deleted after the run |
| `bin/rules --check` | exit 0, all 244 check lines in 62 rule files hold |
| the two `git cat-file -s` sums of finding 9, and the framer and warden sums over `spec.md`'s sets at b3154f43, 493d9816 and 4ce4daf0 | 159,334 and 151,600; framer 110,562, 112,603, 112,603; warden 76,287, 78,706, 78,706 |
| `wc -c` of the block with findings 1 and 2 applied, written to the round's scratch directory | 1,669 bytes |
