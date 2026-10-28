# Review round 3: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 38aea7be, fixes 921bfce7..38aea7be

## Findings

### 1. The frame still says the fix-pass paragraph states the answer commit, which `ea5f22e6` moved to another paragraph

severity: should
location: `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:26-39`, `skills/code-review/orchestration.md:78-80`
evidence: read `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:26-39`, `skills/code-review/orchestration.md:54-80`
verdict: open
regression: round-2#1

The unit is the commit sentence that `ea5f22e6` moved to
`skills/code-review/orchestration.md:78-80`. The frame's Scope item 1 says
the paragraph at `:54-58` states the answer commit as the first of three
things. The fix moved that sentence out of that paragraph, to the end of
the paragraph *The fix pass then finds what the fixes left standing*. The
defect came from round 2's paste-ready block, which the fix applied as
given, and not from the frame or from how the fix was written.

Why it matters. `frame/design.md:26-39` reads "the paragraph at `:54-58`,
is rewritten in place. It states three things", and the first of the three
is the commit of the two lines. At `38aea7be` that paragraph states two of
them (`skills/code-review/orchestration.md:54-62`). The third stands in a
different paragraph, `:71-80`. The built text is the right one: read in
order, it now puts the answer commit after the corrections, with one
reading. The frame is the text that went false. The sealer reads every
party's account against the tree. A frame naming the wrong paragraph for a
rule is the kind of restatement a sealer stops on. The crafter's sweep in
round 2's answer checked the frame's wording ("all name the corrections")
and not which paragraph the frame names. The frame is not the crafter's to
write (`agents/crafter.md:17-21`), so this change falls to the orchestrator.

The fix rewrites Scope item 1's opening in place, and keeps the two
sentences after its list as they stand:

```markdown
1. **The orchestrator writes neither line of a finding that a fix pass
   answers.** `skills/code-review/orchestration.md` *Orchestrator: a phase
   is a fresh crafter, and a fix pass resumes the implementer* is rewritten
   in place, in two of its paragraphs:
   - the paragraph at `:54-58` states that the orchestrator writes neither
     line of such a finding and that its fix-pass prompt leaves both lines
     to the crafter, and that a close the orchestrator doubts goes into the
     verifying round's spawn prompt, where the orchestrator does not
     rewrite the line;
   - the paragraph *The fix pass then finds what the fixes left standing*
     ends with the crafter's fix pass committing the `verdict:` and
     `answer:` lines of every finding it answered in one commit for the
     whole pass, after its fix commits and the corrections that paragraph
     names.
```

answer:

## Confirmations

confirms: round-2#1
The close holds on both halves. On the timing, the commit sentence now
ends the paragraph on what the fixes left standing
(`skills/code-review/orchestration.md:71-80`). It reads "Last, the fix pass
commits the two lines of every finding it answered in one commit for the
whole pass, after its fix commits and those corrections". "Those
corrections" refers back to the crafter's "corrects each" at `:76`. Read in
order, the answer commit comes after the sweep, with one reading, and
`agents/crafter.md:156-158` gives the same order. The fix-pass paragraph at
`:54-62` no longer states any timing (read). On the policy text, the `to:`
lead at `frame/design.md:170` now reads "each time that party closes
findings, one commit carries the lines of all of them". The body gives the
orchestrator's closes "in one commit" at that step, so both parties have a
count (read). The pin at `tests/text/test_the_rules_have_one_owner.py:192-193`
holds the moved words. The modules that read the changed files passed
(executed). The crafter's red run at `8311f660` was read, not repeated: the
pinned words are new in `ea5f22e6` (read). Finding 1 above is about the
frame's description of where the sentence went, not about this close.

confirms: round-2#2
The run is gone. I measured it with the paste check's own `longest_run`
on the `to:` text that `rule_changes.parse` returns at each commit. Against
`skills/code-review/orchestration.md` it was 15 at `8311f660`, then 0 at
`4fa7a630`, `ea5f22e6` and `38aea7be`. It was 0 against
`agents/crafter.md` at all four commits, and 0 between the orchestrator's
file and `agents/crafter.md` (executed). `over_baseline` on the tree read
in memory passes. It also passes with the `to:` text at `38aea7be` appended
to `docs/the-review-record.md` the way a word-for-word settle writes it
(executed). `parse` returns one whole `add` and no errors at each commit
(executed).

confirms: none
The changelog fragment's first item now places the orchestrator file's
commit sentence at the end of the paragraph on what the fixes left
standing (`changelog.md:3`), which matches `skills/code-review/orchestration.md:78-80` (read). `38aea7be`
changes only `trail/rounds/round-2.md` and holds both findings' two lines
in one commit after `ea5f22e6`. The work item's own rule held on its own
fix pass (executed, `git diff --stat ea5f22e6 38aea7be`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `38aea7be`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 11 modules that `git grep -l` finds under `tests/` naming `skills/code-review/orchestration.md`, `code-review/orchestration.md` or `test_the_rules_have_one_owner`, plus `tests/text/test_the_rules_have_one_owner.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `-q` | exit 0, 235 passed |
| `bin/seal layout --check` | exit 0 |
| `bin/seal rules --check` | exit 0 |
| `git diff --check 921bfce7..38aea7be` | exit 0, nothing printed |
| the repository venv's python calling `longest_run` from `tests/text/test_no_passage_is_pasted_into_a_second_file.py` on the parsed `to:` text against `skills/code-review/orchestration.md` and `agents/crafter.md`, each read through `git show` at `8311f660`, `4fa7a630`, `ea5f22e6` and `38aea7be` | against the orchestrator's file: 15, 0, 0, 0; against the crafter's file: 0 at all four; the two files against each other: 0 at all four |
| the same module's `over_baseline` on the tree read in memory, then again with the `to:` text at `38aea7be` appended to `docs/the-review-record.md` | no refusal either time |
