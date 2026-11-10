# Review round 1: 1794352646-a-phase-spawn-preloads-the-fix-pass-procedure

```seal
target: bbb765088 against release/v0.37.3
```

This is the first round, so no earlier record carries a coordinate and every
fact below was established here. The diff was read from `7c2801838`, the tip
of `release/v0.37.3`, to `bbb765088`. `routing.md`, the three frame files,
`gaps.md`, `changelog.md` and `pr.md` were each read whole at `bbb765088`.
No `pr.<lang>.md` stands, and none is owed: `seal/config.json` names English
for both language keys. No `seal/parity.json` is declared.

The axes this change carries beyond the table of `skills/code-review/SKILL.md`
are these. What each agent preloads. Whether each moved sentence still reaches
the party that acts on it, and in the same order. Whether each citation the
move writes resolves. Whether the form's facts about a close block now stand
in one place. Which route a session's fix pass takes, beside the crafter's.
And the release's version move. The request-shaped axes (inputs,
authorization, query scope, concurrency, security) have nothing to compare in
a move of prose between skill files, and no code path changes.

## Findings

### 1. Step 9 now tells a fix pass to skip steps 5 and 6, where it used to replace only their record

```seal
severity: should
location: `agents/crafter.md:62-63`, `tests/text/test_a_moved_rule_leaves_its_definition.py:530`, `tests/text/test_a_moved_rule_leaves_its_definition.py:612-615`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/changelog.md:3`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:30`
evidence: read `agents/crafter.md:42-63` at `bbb765088`, `git show 7c2801838:agents/crafter.md` lines 42-66, `skills/implement/fix-pass.md:1-78`, `docs/running/what-a-script-gates.md:69`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:60`; executed `git grep -n -i "seal mutate" -- skills/implement skills/code-review agents docs/running`
```

Why it matters: the crafter acts on step 9 in every fix pass. A fix that adds
behaviour, such as a guard a finding asks for, is now told not to run
`seal mutate` and not to read its change against the table in
`skills/verify/SKILL.md` *The narrow command still has to be able to fail*.
The work claims the opposite. `frame/plan.md:60`, which `pr.md` quotes,
says "what a fix pass does is unchanged".

The grounds:

- **Before.** Step 9 at `7c2801838` ended "then append each close block
  instead of steps 5 to 8's record". What it replaced was the record that
  steps 5 and 8 write into `trail/phases/phase-N.md`, and its own run took
  the place of step 7's run. Steps 5 and 6 still bound a fix pass: read the
  change against the verify table, build a behaviour-adding unit test-first,
  commit, and run `seal mutate` over each unit that adds behaviour.
- **After.** `agents/crafter.md:62-63` reads "open
  `skills/implement/fix-pass.md` and follow it in place of steps 5 to 8".
  `skills/implement/fix-pass.md` holds no read against the verify table and
  no `seal mutate` run. `git grep` over `skills/implement`, `skills/code-review`,
  `agents` and `docs/running` finds `seal mutate` only at
  `agents/crafter.md:50` (step 6) and `:127-140`, and in
  `docs/running/what-a-script-gates.md:69`, which assigns the run to "the
  crafter at each unit that adds behaviour". So for a fix pass, no text now
  asks for the run.
- **The frame.** `frame/design.md:30` (*Scope* item 2) gives the new
  sentence word for word, so the crafter built what the frame says. The
  frame's own account of what step 9 held is narrower. *Removes* row 1
  (`frame/design.md:81`) lists "read the round record, judge each finding,
  run the round's set, append the closes", and D1 moves nothing from steps
  5 or 6. The sentence widens the replacement beyond what the frame says
  moved.
- **The pins.** The case pins the wider sentence
  (`tests/text/test_a_moved_rule_leaves_its_definition.py:612-615`), and its
  docstring repeats it (`:530`). `changelog.md:3` quotes it as what step 9
  now reads.

The fix restores the old scope in the new form:

```markdown
9. In a fix pass, open `skills/implement/fix-pass.md` and follow it in place
   of step 7's run and step 8's record; steps 5 and 6 hold for each fix.
```

The snippet covers `agents/crafter.md` alone. The fix pass also owes:

- the case's assertion at `:613-614` and its docstring at `:530`, set to
  the new sentence;
- `changelog.md:3`, both the quoted sentence and the preload figure. Step 9
  grows by about 40 bytes, so `release_report.py#preloads` is measured again
  and the 33,717 there is replaced by the new number.

`frame/design.md:30` (*Scope* item 2) is a frame statement, which the fix
pass names in its hand-back for the orchestrator to fold.

### 2. The frame and the closing memo say the orchestrator files an issue for `docs/running/the-agent-set.md:93`, and the orchestrator judged it takes none

```seal
severity: should
location: `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/gaps.md:12`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:44`
evidence: read `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:44`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/gaps.md:12`, `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:59`, `skills/code-review/scripts/pr_body.py:15`, `skills/code-review/scripts/pr_body.py:201`, `docs/forms/the-round-record.md:21`
```

Why it matters: the records give two answers to one question. A reader has
to choose between them. The sealer reads `gaps.md`, and `seal pr-body`
copies its `## Not done` section into the pull request body
(`skills/code-review/scripts/pr_body.py:15`, `:201`). Under
`docs/forms/the-round-record.md:21`, a wrong line that `seal pr-body` copies
is a `should`.

- **Claimed** in `frame/design.md:44`: "The orchestrator files it, since it
  is a `docs/` sentence this work does not edit."
- **Claimed** in `gaps.md:12`: *Scope* "leaves it to the orchestrator to
  file".
- **Found** in `frame/plan.md:59`: the orchestrator's row reads "takes no
  issue", on the grounds that a work item to change one clause costs more
  than a reader loses.

`b9e5f1b49` added that row and folded `frame/design.md` in the same commit,
but it left *Scope*'s sentence about filing as it was. The row and its
grounds stand, so the two sentences that promise an issue are the ones to
change:

```markdown
- **`docs/running/the-agent-set.md:93`**, "the fix pass writes two lines of each finding it answers". It names neither the verdict values nor the `location:` rule. Its count of two lines predates #1198's close block, which holds a third line where the fix went elsewhere. It is a `docs/` sentence this work does not edit, and `frame/plan.md` *Judgments of the run* holds the orchestrator's judgment that it takes no issue.
```

```markdown
`docs/running/the-agent-set.md:93` still says "the fix pass writes two lines of each finding it answers", where a close block holds a third line when the fix went elsewhere. `frame/design.md` *Scope* puts that `docs/` sentence out of this work, because this work changes no `docs/` text and no rule, and `frame/plan.md` *Judgments of the run* judges that it takes no issue.
```

The first replaces `frame/design.md:44` and the second replaces `gaps.md:12`.
`frame/design.md` is a frame file, so the fix pass changes `gaps.md` and
names the *Scope* bullet for the orchestrator to fold.

## Confirmations

What matched: `skills/implement/fix-pass.md:12-78` holds the five sections D1
lists, in D1's order (`frame/design.md:66-70`). Each moved sentence keeps its
words except for the three exceptions *Scope* item 1 names. The verdict list
and the `location:` sentence are gone, replaced by one citation of
`docs/forms/the-round-record.md:17` and `:55` by their bold leads. The
section keeps the moved `check:` line at `:70`. Read, and checked line by
line against `git show 7c2801838:agents/crafter.md` lines 204-232 and
`git show 7c2801838:skills/implement/SKILL.md` lines 409-435.

What matched: the form states every fact the move took out of the four
files. The three verdict values are at `docs/forms/the-round-record.md:17`.
The `location:` line of a close block and `deferred <where it was repaired>`
are at `:55-61`. The rule that a `fixed` commit touches a named path,
dropped from *5.* without a citation, stands at `:24-31`, and
`chain_check.py` enforces it. Read.

What matched: the phase's census of the old spellings outside `seal/threads/`
holds at `bbb765088`. "A fix pass appends close blocks and writes no phase
record" stands only in `skills/implement/fix-pass.md:53` and in the case.
The verdict list stands in `lib/fields.py:179`, `chain_check.py:339`,
`tests/skills/test_chain_check.py:3974` and the case. "`location:` line
naming" stands in the form and the case. "the table step 7 cites" and
"instead of steps 5 to" stand nowhere. Executed: `git grep -n -F` on each of
the six spellings with `':!seal/threads'`.

What matched: no citation in the tree names the moved rule or *5.*'s old
paragraphs. Executed: `git grep -n -i` on "A fix pass appends close blocks",
"crafter.md` *A fix pass", "5. Incorporate review", "step 9", "steps 5 to 8"
and "third path" outside `seal/threads/`. The only hits are the new file,
step 9 itself and the case.

What matched: the preload claim in `changelog.md:3` and S1. At `bbb765088`,
`release_report.py#preloads` gives `crafter` 33,717 B, `framer` 39,806,
`proofer` 33,254, `sealer` 33,962 and `tracer` 25,402. That is the figure
`trail/phases/phase-1.md:36` reports at `0083fe9e2`. Executed, *Probes*
row 1.

What matched: the cases that read the moved text and the tree-wide readers
the move meets pass at `bbb765088`. Executed, *Probes* row 2.

What matched: the phase's six `seal mutate` reds (`trail/phases/phase-1.md:15-26`).
Read, not re-run. Each absence assertion
(`tests/text/test_a_moved_rule_leaves_its_definition.py:593-599`) is a plain
containment check over the flattened file. Each pasted-back copy in the
phase's table contains its guarded string, so each run's red follows from
the code as written.

What matched: `pr.md` at `bbb765088`. Its six quotes stand word for word at
the coordinates they name in `frame/plan.md`: rows 1, 2 and 7 of
*Alternatives considered*, and the two rows of *Judgments of the run* with
that row's Grounds cell. Quote 4 writes its inner quotes as `\"`, which
Markdown renders as `"`, and so matches. It quotes no sentence of
`changelog.md`. It holds `Closes #1471.` and the attribution line, which
opens with U+1F916 and which `skills/code-review/orchestration.md:401-402`
allows. Quote 6's clause "what a fix pass does is unchanged" is true once
finding 1 is fixed.

What matched: the four statements the orchestrator's `b9e5f1b49` folded stand
in the frame. They are *Scope* item 1's third exception
(`frame/design.md:29`), *Scope* item 5's absence list (`:34`), red at
`87a4730f7` in S2 (`:52`) and in the plan's *Verified by* cell
(`frame/plan.md:34`), and `0083fe9e2` in S1 and S5 (`frame/design.md:51`,
`:55`). Read.

What matched: the version move. `.claude-plugin/plugin.json:4` reads `0.37.3`
in `0083fe9e2`, the commit that adds `changelog.md`. No other tracked file
outside `seal/threads/` and the changelogs names `0.37.2`. Executed:
`git show --stat 0083fe9e2`, `git grep -n "0\.37\.2"`.

The rewritten case's presence check of `deferred <where it was repaired>` in
the form repeats `tests/text/test_the_record_is_written_in_words.py:128`.
*Scope* item 5 states that fact, so it opens no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the work item's HEAD; the suite is `unverified` here | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/gaps.md:8` | the orchestrator, by `seal gate --record` after the rounds settle |
| Whether a fix pass, a resumed implementer among them, opens `skills/implement/fix-pass.md` at step 9 (S3) | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:53` | the orchestrator, from the transcript of the first fix pass after the merge |
| The crafter eval smoke run's `Verdict: pass` (S5), not re-run here: each side is a full eval run | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/trail/phases/phase-1.md:40-45` | the sealer, where it samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_preload.py <repository root>`, run from `<scratchpad>/<work-item-id>/round-1/`. It loads `.github/scripts/release_report.py` by path and prints `preloads(root, meter())` | `{'crafter': 33717, 'framer': 39806, 'proofer': 33254, 'sealer': 33962, 'tracer': 25402}`, exit 0. Run once; the file and its directory were deleted |
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/github/test_rules.py -q -p no:xdist` | 415 passed, 2 warnings, exit 0. One warning names a pending rule change in another work item, `seal/threads/1794289596-implement-orchestration-grew-back/` |
