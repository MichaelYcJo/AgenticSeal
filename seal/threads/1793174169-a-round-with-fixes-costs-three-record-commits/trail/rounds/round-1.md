# Review round 1: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 87e89f17 against 5287dd42

## Findings

### 1. The one-commit sentence reads as one commit per finding, so it does not deliver the two record commits the work item promises

severity: should
location: `agents/crafter.md:151-152`, `skills/code-review/orchestration.md:58-60`, `skills/code-review/orchestration.md:161`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:169-170`, `tests/text/test_a_moved_rule_leaves_its_definition.py:510-512`, `tests/text/test_the_rules_have_one_owner.py:191-194`, `tests/text/test_the_rules_have_one_owner.py:214-216`
evidence: read `agents/crafter.md:148-158`, `skills/code-review/orchestration.md:54-80`, `skills/code-review/orchestration.md:161`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:101-114`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/changelog.md:3`
verdict: fixed b413456f

Why it matters. The work item exists to cut a round with fixes to two
record commits: the round record's commit and one answer commit.
`frame/design.md:101-104` states that cost as "one answer commit holding
both lines of every finding the pass answered". The changelog fragment
repeats it (`changelog.md:3`: "two record commits, the round record's and
the answer commit"). The text the crafter acts on does not say that.

Grounds. `agents/crafter.md:151-152` says "Commit both lines of each finding
together, in one commit after your fix commits." The phrase "each finding
... in one commit" distributes over the findings. A crafter that makes one
commit per finding obeys it word for word, and a pass over six findings then
makes six answer commits. The sentence has a second reading, and the
crafter cannot ask which one is meant. `skills/writing-style/SKILL.md`
*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* forbids that. The
same wording stands at `skills/code-review/orchestration.md:58-60` ("It
commits both lines of each finding together, in one commit after any fix
commit it made"). It also stands in row *The record* at
`skills/code-review/orchestration.md:161` ("you write both lines of each
finding in one commit"). The frame's `## Rule changes` item carries it into
policy at the settle (`frame/design.md:169`: "A finding's `verdict:`
and `answer:` lines are one party's, written in one commit."). The two test
clauses pin the ambiguous words, so they hold the second reading in place.

The sentence also leaves the timing open. At `agents/crafter.md:154-157`
and `skills/code-review/orchestration.md:73-80` the fix pass corrects
every other place stating a reworded rule "once the fixes are committed".
Those corrections are commits of the fix pass. In the paragraph, the
one-commit sentence comes before them. Whether the answer commit comes
before or after them is not stated.

The implementer's account claims the text delivers the cost (`changelog.md:3`).
The design's evidence (`frame/design.md:105-111`) is six answer commits
that each held every finding of their pass. That is the reading the work
item means. No sentence it adds states it.

The fix states one commit for the whole pass, after the last fix commit,
the sweep's corrections included. In `agents/crafter.md`, the commit
sentence moves to the end of the paragraph:

```markdown
**A fix pass writes two lines of each finding and no phase record.** It
rewrites `verdict:` to `fixed <commit>`, `rejected` or `deferred <home>` (a
repair with no commit on the branch is `deferred <where it was repaired>`)
and writes `answer:` (`docs/the-review-record.md` *The round record*).
Where your fix changed none of the paths `location:` lists, append the one
it did change after `, ` and name it in `answer:`. Once the fixes are
committed, find every other place stating each rule your range reworded or
removed, by `git grep` and its `check:` target, and correct each or say in
the hand-back why it stands (rule 12). Then commit the `verdict:` and
`answer:` lines of every finding you answered in one commit for the whole
pass, after your last fix commit and its corrections.
```

In `skills/code-review/orchestration.md:58-60`, and in row *The record* at
`:161`:

```markdown
`trail/phases/phase-N.md` and no `plan.md` row. It commits the two lines of
every finding it answered in one commit for the whole pass, after its last
fix commit, because a `fixed` verdict names a commit that already exists.
```

```markdown
| The record | every open finding closes `deferred the frame`, and its `answer:` line names the regression that sent the work item back; you write both lines of every open finding in one commit |
```

The clauses in `tests/text/test_a_moved_rule_leaves_its_definition.py:510-512`
and `tests/text/test_the_rules_have_one_owner.py:191-194` and `:214-216`
take the new words, and each is seen red against `87e89f17` first. The
frame's `## Rule changes` `to:` line needs the same words before the
settle: "A finding's `verdict:` and `answer:` lines are one party's, and
one commit carries every finding that party closes in the pass." The frame
is not on the crafter's list of writes (`agents/crafter.md:17-21`), so the
orchestrator decides who edits it.

answer: The finding holds: "each finding ... in one commit" distributes over the findings, and the sentence stood before the sweep. `b413456f` takes the record's words. In `agents/crafter.md` the commit sentence moves to the end of the fix-pass rule, after the sweep's corrections. `skills/code-review/orchestration.md:58-60` and row *The record* now say one commit for every finding. The pins in `tests/text/test_a_moved_rule_leaves_its_definition.py` and `tests/text/test_the_rules_have_one_owner.py` take the new words, and each exited 1 against the text at `87e89f17` before the text changed. The changelog fragment's first two items now state one commit for the pass. The `git grep` sweep finds the old reading only in this work item's frame: `frame/design.md:31`, `:53` and `:152` and `frame/plan.md:73`. They stand because the frame is not the crafter's to write, and the orchestrator decides who edits them. One more thing for the settle: the new orchestrator sentence shares a 21-word run with the frame's `to:` text ("commits the two lines of every finding it answered in one commit for the whole pass, after its last fix commit"). That frame text sits under `seal/`, which the paste check skips. If the settle writes the text verbatim into `docs/the-review-record.md`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads that pair at its 15-word window.

## Confirmations

confirms: none
S1 holds. `skills/code-review/orchestration.md:54-64` says the orchestrator
writes neither line of a finding the fix pass answers. It says the
orchestrator's fix-pass prompt leaves both lines to the crafter. It says a
doubted close goes into the verifying round's spawn prompt and the line is
not rewritten. The paragraph keeps its citation of
`docs/the-review-record.md` *The round record*, the `location:` coordinate
and the "no phase record, no `plan.md` row" clause, as Scope item 1 asks
(read). Rule 19 of `tests/text/test_the_rules_have_one_owner.py:140-148`
and the clauses at `:191-194` hold it. They passed in the module run under
`## Probes` (executed).

confirms: none
S2 and S3 hold, apart from the wording finding 1 raises. Row *The record* at
`skills/code-review/orchestration.md:161` names the `answer:` line and one
commit of the orchestrator's. `agents/crafter.md:151-152` gains the commit
sentence (read). The cases at `tests/text/test_the_rules_have_one_owner.py:204-220`
and `tests/text/test_a_moved_rule_leaves_its_definition.py:510-512` passed
(executed). The new framer's-route case is not a copy of its group: the
regression-route case at `tests/text/test_the_rules_have_one_owner.py:539-565`
reads only that the heading exists in the orchestrator's file, not the row
(read).

confirms: none
S4 holds. The paste check, the wrap check and the delivery check passed
among the 31 modules that name a changed path (executed, `## Probes`).
`git diff --check 5287dd42..HEAD` printed nothing. `uvx ruff check` and
`uvx ruff format --check` over the two changed test modules exited 0
(executed). The longest run of words shared between the new orchestrator
paragraph and the `## Rule changes` text is 14 words, "doubts goes into
the verifying round's spawn prompt, since that round weighs every close"
(read, counted by hand). That is under the check's 15.

confirms: none
S5 holds. `chain_check.py --baseline 5287dd42 --root <worktree> --worktree`
exited 0 under both the plugin's copy and the tree's copy. The work item
drew no refusal from the `## Rule changes` reader (executed). Calling
`skills/settle/scripts/rule_changes.py#parse` on `frame/design.md` directly
returned no errors. It returned one `add` operation on
`docs/the-review-record.md`, section *The round record*, at line 166,
with the whole `to:` text and its `check:` line (executed).

confirms: none
S6 holds. The changelog fragment (`changelog.md:5`) cites lines 7832, 8016
and 8972 of session `50face2d-96d3-4774-92e7-faa0805279a3`. `grep -n` over
that transcript finds "Leave every `verdict:` line as it stands; they are
the orchestrator's." at 7832, inside an `Agent` call titled "Fix pass #955
round 1". It finds "Leave `verdict:` as it stands." at 8016, in #955's
round 2 prompt. It finds the same words at 8972, in a prompt for #1016 and
#1018 (executed). Commits `2b68252c` and `517a1139` add 6 and 1 `answer:`
lines and no `verdict:` line. `137d0a9c` and `f294b3bd` add 6 and
1 `verdict:` lines and no `answer:` line (executed, `git show` counted per
prefix). The same instruction also stands at line 10016, in a fix-pass
prompt for #945. That line is neither in the fragment nor in
`frame/design.md` Scope item 4. It falls between 8972 and the line 11321
where the frame says the session stopped, so it supports the cause and
changes nothing the fragment claims (executed).

confirms: none
The divergence `gaps.md:12` records holds. The frame's transcript line
numbers are one lower than `grep -n` prints. "chore: verify #955's round 1
answers" first stands at 7954, and `49a2dd0d` first stands at 8067
(executed).

confirms: none
The `Grounds` sentence added at `skills/implement/orchestration.md:666` is
true. `gaps.md:21` names this round as its reader. The chain check's git
history reads are a `log` of a declaration file's squash commits
(`skills/code-review/scripts/chain_check.py:681-690`), a `rev-list` of the
commits after a `target:` (`:1499-1501`), and a `log` of routing trailers
(`:2098-2107`). None of them reads who wrote a `verdict:` or `answer:`
line (executed, a `grep` of the script for `log`, `rev-list` and `blame`,
then read). The phase record states that `seal mutate` left that sentence
surviving (`trail/phases/phase-1.md:20`). That matches a cell no case reads
its words from.

confirms: none
The `routing.md` divergence (`gaps.md:11`) holds as the frame settled it.
`skills/code-review/scripts/chain_check.py` is byte-identical to the
plugin's 0.23.1 copy, and the branch diff does not touch it (executed,
`diff` and `git diff --stat`). Q1 of `frame/questions.md` stays open on its
default (a). The spawn prompt says that alone is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `87e89f17`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |
| The phase record's red-first runs and its `seal mutate` results. Read, and not run again by this round. Each new clause is absent at `5287dd42` (executed, `git grep` at that commit), so a red run is the expected outcome | `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/trail/phases/phase-1.md:18-20` | the sealer, at its sample of the crafter's claims |
| Whether a split commit of the two lines should also be refused by a check, `frame/questions.md` Q1 | `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/questions.md:42` | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 31 modules that `git grep -l` finds under `tests/` naming `agents/crafter.md`, `crafter.md`, `skills/code-review/orchestration.md` or `skills/implement/orchestration.md`, plus the two changed test modules, `-q` | exit 0, 801 passed |
| `bin/seal layout --check` | exit 0: 158 files read, 0 refused |
| `bin/seal rules --check` | exit 0: all 266 check lines in 55 rule files hold |
| `python3 skills/code-review/scripts/chain_check.py --baseline 5287dd42 --root <worktree> --worktree`, under the tree's copy and the plugin's 0.23.1 copy | exit 0 both times. Three notices: no `round-N.md`, no `trail/gate.md` and no `guarantee.md` yet. No refusal from the rule-changes reader |
| `rule_changes.parse` on `frame/design.md`, loaded by path in a `python3 -c` call | no errors; one `add` operation, file `docs/the-review-record.md`, section *The round record*, line 166 |
| `grep -n` over `/Users/x/.claude/projects/<project>/50face2d-96d3-4774-92e7-faa0805279a3.jsonl` for the two spawn-prompt sentences, the `137d0a9c` subject and `49a2dd0d` | the sentences at 7832, 8016, 8972 and 10016; the subject first at 7954; the hash first at 8067 |
| `git show <commit>` counted for added `verdict:` and `answer:` lines, over `2b68252c`, `517a1139`, `137d0a9c` and `f294b3bd` | 0 and 6, 0 and 1, 6 and 0, 1 and 0 |
| `git diff 5287dd42..HEAD` searched for a user path, a home path or an email host | nothing found |
