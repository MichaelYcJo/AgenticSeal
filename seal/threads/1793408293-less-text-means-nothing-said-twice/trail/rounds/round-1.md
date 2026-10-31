# Review round 1: 1793408293-less-text-means-nothing-said-twice

target: 9a803e0b against release/v0.25.2

## Findings

### 1. The new core sentence's last clause reads two ways: as a duty to report every change's added and removed lines, with no party named, or as a limit on how such a count is used

severity: should
location: `skills/core/SKILL.md:106-109`, `seal/threads/1793408293-less-text-means-nothing-said-twice/changelog.md:3`, `seal/threads/1793408293-less-text-means-nothing-said-twice/changelog.md:9`
evidence: read `skills/core/SKILL.md:106-110`, `skills/writing-style/SKILL.md:250-289`, `seal/threads/1793408293-less-text-means-nothing-said-twice/frame/design.md:28`

The core is read by every party in every repository, and its present tense
states what is done: "A fact has one source", "A script blocks work only on
a fact it reads exactly". Read that way, "the lines a change adds against
those it removes are reported as context" is an instruction. It names no
party, no moment and no file, so a crafter can add a count of added and
removed lines to each hand-back, a proofer to each round, and a sealer can
look for one and find it missing. Read the other way, the clause only says
what such a count is where somebody gives one. `skills/writing-style/SKILL.md`
*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks text an agent reads
to have one reading. Its third rule asks an instruction to name who, when,
in which file, and when it is done. The clause meets neither rule. The
parallel clause two lines down, "a reading that is noisy or guessed from
words is reported, never used to block", has its actor, "A script", in the
same sentence (`skills/core/SKILL.md:109-110`). The new clause has no actor.

The owner's ruling (PR #1191 comment 6534214778, read with `gh api`) gives
counts as context for one reader. It does not ask any party to report a
count. The frame's own statement of the third part is "a change's net count
held as context only" (`frame/design.md` *Scope* item 1). So the fix stays
inside the frame and drops only the duty. The issue's example sentence
carried the same "reported as context", and the frame records that its
wording is not fixed.

The wrapped text, keeping every line under 80 columns, `fewer lines` on
line 106 and "a change that grows" on line 107, so the enumeration of
`frame/design.md` *Data & interfaces* still finds the sentence on the same
two lines:

```markdown
other place links to it. Less text means nothing said twice, not fewer lines:
a change that grows is kept where what it adds serves a reader, and a count of
the lines a change adds against those it removes is context, never a
criterion. A script blocks work only on a fact it reads exactly, such as
```

The fragment's two copies of the clause change with it, in the same commit
(contract rule 19). In `changelog.md` line 3, the *Changed* entry's
"and the lines a change adds against those it removes are reported as
context, never held as a criterion." becomes:

```markdown
and a count of the lines a change adds against those it removes is context, never a criterion.
```

In line 9, the process row's "and a change's added lines against its
removed lines are reported as context, never held as a criterion" becomes:

```markdown
and a count of a change's added lines against its removed lines is context, never a criterion
```

The phase record of the fix pass states the new text and why, as
`frame/design.md` *Scope* item 1 asks of a builder who rewords the sentence.

verdict: fixed a45c2f93
answer: The finding holds: "are reported as context" names no party and reads as a duty, and the owner's comment asks nobody to report a count. The paste-ready text was read as every party in every repository reads the core. It states what a count is where one is given and asks no party to produce one, and it keeps the frame's three parts and scope. The new clause is the proposed wording: "and a count of the lines a change adds against those it removes is context, never a criterion." Only its wrap differs: line 107 breaks after "a count", so lines 106 to 108 are 77, 75 and 71 columns, inside the paragraph's band, where the proposal ran line 107 to 78. Line 106 keeps `fewer lines` and line 107 keeps "a change that grows". The enumeration of `frame/design.md` *Data & interfaces* at the fix lists the same seventeen lines, the frame's fifteen and `skills/core/SKILL.md:106` and `:107` (executed). The fragment's lines 3 and 9 carry the proposed text in the same commit. The 45-module narrow run, which includes `tests/hooks/test_core.py`, `tests/behaviour/test_docs_line_wrap.py` and every module that reads the fragment, gave 2,909 passed and 9 skipped, exit 0 (executed). `git grep` for the clause's words found it also in `frame/design.md:26`, the framer's Scope item 1, which is left for the framer. The S1 row of the same file and `frame/plan.md` already state the count as context with no duty. `trail/phases/phase-1.md` says the sentence is Scope item 1 word for word, which was true at `af0bdaff`. A fix pass writes no phase record, so this answer records the new text and why in place of the phase record that *Scope* item 1 names.

## Confirmations

confirms: none
S1 holds. Claimed: the sentence follows the anchor on line 106, the
anchor's own last line, not the line after it. Found: `skills/core/SKILL.md:106`
ends the anchor "A fact has one source, and every other place links to it."
and opens the sentence on the same line, and `git grep -n -F 'Less text
means nothing said twice' -- skills/core/SKILL.md` gives that one line
(read). The sentence carries the three parts the frame names: nothing said
twice and not fewer lines, a growing change kept where what it adds serves
a reader, and a change's added lines against its removed lines never a
criterion. Its text is `frame/design.md` *Scope* item 1 word for word
(`git diff 13dc7c63..9a803e0b -- skills/core/SKILL.md`, executed). The
departure from the plan's *Verified by* cell is recorded in
`trail/phases/phase-1.md` and is about where a line breaks, not what the
sentence says.

confirms: none
S2 holds: the sentence leaves each reader's limit standing.
`hooks/lib/core.py:41` (`CAP`, 10,000 characters) bounds the whole hook
output one session receives. `docs/the-review-record.md:493` is the
harness's 10,000-character cap on one `Stop` hook message.
`skills/code-review/orchestration.md:30` bounds one implementer's per-turn
context at 806,241 tokens. Each bounds what one reader takes in at once.
None compares a change's additions with its removals, which is the one
count the sentence rules out. The sentence's middle clause agrees with
`CAP`: a change that pushed the core past it would leave the reader a
preview in place of the core, so what it added would not serve a reader.
The `Document token ceiling` rows (`templates/setup/config.md:438-448`,
`skills/config/SKILL.md:50`) bound one document and are reported, never
failing, so they also stand (read).

confirms: none
S3 holds. Claimed: seventeen lines at HEAD, the fifteen recorded and the
sentence's lines 106 and 107. Found: the enumeration command of
`frame/design.md` *Data & interfaces*, run against `9a803e0b`, lists
exactly the fifteen lines of the frame's table and `skills/core/SKILL.md:106`
(`fewer lines`) and `:107` (`change that grows`), seventeen in all, exit 0
(executed). None of them holds a change's added lines against its removed
lines as a criterion. The same alternation's net-count phrasings over
`skills/`, `agents/`, `templates/`, `hooks/`, `.github/scripts/`,
`evals/scripts/` and every `.py` file find `evals/scripts/replay_targets.py:663`
(a size reported as context, as the frame says), `skills/verify/orchestration.md:429`
(a measurement in a table with no verdict), the new sentence, and
`tests/skills/test_fold_check.py:174`, which feeds a retired row name to a
refusal case and is no criterion (executed).

confirms: none
S4 holds. Claimed: 6,523 characters against `CAP`, and the 130-character
gap from P1's 6,653 left untraced. Found: `hooks/lib/core.py#output` in
the main clone at `9a803e0b` returns 6,523 characters (executed). The
header's first line carries the core's absolute path. P1 ran in a clone
under the scratchpad's `1793408293-less-text-means-nothing-said-twice/frame/`
directory, and that path, with a `clone` directory under it, is 130
characters longer than the main clone's (executed, by `len` of the two
paths; the name `clone` is assumed, since the frame does not record it).
The gap is the header path, not the core's text. `bin/test -q
tests/hooks/test_core.py tests/behaviour/test_docs_line_wrap.py` gave 60
passed, exit 0 (executed). The paragraph's lines 103 to 110 are 70 to 77
columns (executed).

confirms: none
S5 holds. `.claude-plugin/plugin.json` reads `0.25.2` at `9a803e0b`, and
`.claude-plugin/marketplace.json` carries no version (read).
`gh pr list --base release/v0.25.2 --state all` returned `[]` (executed),
so this is the release branch's first pull request, which
`skills/implement/orchestration.md:318-325` gives the version move. The
fragment ends with `### Process changes` and one row in the four columns of
`templates/records/process.md` (read). The row's source is the owner's
comment, which says what the entry and the row say: the count was never
the criterion, and a change that grows is kept where what it adds serves a
reader (executed, `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6534214778`).

confirms: none
The build changes no other shipped text, and nothing in the tree cites the
core by a line number the three added lines would shift: `git grep` for
`core/SKILL.md` followed by a line number, outside `seal/threads/`,
found nothing, exit 1 (executed). No case is written new. `frame/plan.md`
*Alternatives considered* rows B to D reject a pin and a sweep, and no
sentence of the core is pinned for its wording today (read), so contract
rules 14 and 15 ask nothing here.

Carried rather than re-established: nothing. No earlier round exists. The
frame's enumeration, P1's measure and the owner's comment were each opened
or run again this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad suite, the repository-wide lint and `seal gate` at the branch's HEAD; the crafter's 45-module narrow run was not re-run beyond the two modules in `## Probes` | `seal/threads/1793408293-less-text-means-nothing-said-twice/gaps.md:7` | the orchestrator, by `seal gate --base release/v0.25.2 --record 1793408293-less-text-means-nothing-said-twice` |

## Probes

| Command | Result |
|---|---|
| The enumeration command of `frame/design.md` *Data & interfaces*, with `9a803e0b` as the tree | 17 lines, the frame's fifteen and `skills/core/SKILL.md:106`, `:107`; exit 0 |
| The net-count part of the same pattern over `skills agents templates hooks .github/scripts evals/scripts '*.py'` at `9a803e0b` | 4 lines: `evals/scripts/replay_targets.py:663`, `skills/core/SKILL.md:106`, `skills/verify/orchestration.md:429`, `tests/skills/test_fold_check.py:174`; exit 0 |
| `python3 -c` calling `hooks/lib/core.py#output` with the main clone as both arguments | 6523 characters |
| `bin/test -q tests/hooks/test_core.py tests/behaviour/test_docs_line_wrap.py` | 60 passed, exit 0 |
| `git grep -n -E` for `core/SKILL.md` followed by `:<n>`, ` line <n>` or `#L<n>`, outside `seal/threads` | no match, exit 1 |
