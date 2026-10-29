# Review round 4: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 26a25b1a, fixes 924a3c66..26a25b1a

## Findings

None.

## Confirmations

confirms: round-3#1
The frame now holds. `frame/design.md:26-43` (*Scope* item 1) says the
section is rewritten in two of its paragraphs. It names
`skills/code-review/orchestration.md:54-58` for the orchestrator's
sentences. It names the paragraph *The fix pass then finds what the fixes
left standing* for the commit sentence. At `26a25b1a` the first paragraph
is `skills/code-review/orchestration.md:54-62`. It holds the bold sentence
that the orchestrator writes neither line, and that its fix-pass prompt
leaves both lines to the crafter. It also holds the doubted close going
into the verifying round's spawn prompt, and that the orchestrator does
not rewrite the line. It holds no timing. The second paragraph is
`:71-80`, and it ends at `:78-80` with the one commit for the whole pass,
after the fix commits and "those corrections" (read). The frame dates its
line numbers to `5287dd42` (`frame/design.md:3-4`). At that commit the
first paragraph stands at `:54-58` (executed,
`git show 5287dd42:skills/code-review/orchestration.md`). So the coordinate
is right under the frame's own convention.

The sentence after the list, `frame/design.md:41-43`, opens "The
paragraph keeps its citation of `docs/the-review-record.md` *The round
record*". Two paragraphs now stand above it. What it lists picks one of
them: the citation, the coordinate appended to `location:`, and the
clause on no phase record and no `plan.md` row. Only the paragraph at
`:54-62` holds those. So it has one reading for a reader who opens the
file, and this round raises no finding for it.

A `grep` of `frame/design.md`, `frame/plan.md`, `frame/questions.md`,
`gaps.md` and `changelog.md` matched "54-58", "paragraph", "three things",
"fix-pass section" and "fix-pass paragraph". It found no other place that
names a paragraph for the commit sentence (executed). The three other
matches name the paragraph at `:54-58` for the build's rewrite, and each
is true:
- `frame/plan.md:33`, under *What the tree says now (read, at `5287dd42`)*;
- `frame/plan.md:83`, phase 1's row, which says the fix-pass paragraph was
  rewritten in place, as `749cb56c` did;
- `frame/design.md:154`, S1, which reads the fix-pass section as a whole.

The range changes only `frame/design.md` (executed,
`git diff --stat 924a3c66..26a25b1a`), so no test module reads a changed
file and none was run.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `verdict:` and `answer:` lines of round-3#1, which still read `open` and empty. Round 4 was asked to rewrite them to `fixed 26a25b1a` with an answer. It declined: the proofer's definition makes earlier records read-only, and its one write is its own round record. By the rule this work item adds (`frame/design.md:170-171`), a finding closed without a fix pass takes both lines from the orchestrator, in one commit. `chain_check.py` refuses round 3's `open` until they are written | `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/trail/rounds/round-3.md:12`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/trail/rounds/round-3.md:56` | the orchestrator, who made the fix |
| The full suite, the repository-wide lint and the typecheck at `26a25b1a`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 924a3c66..26a25b1a` | one file: `frame/design.md`, 12 insertions and 9 deletions |
| `git show 5287dd42:skills/code-review/orchestration.md`, lines 54 to 58 | the fix-pass paragraph, from "The crafter's fix pass changes two lines" to "no `plan.md` row." |
| `grep -n` over the frame, `gaps.md` and `changelog.md` for "54-58", "paragraph", "three things", "fix-pass section" and "fix-pass paragraph" | matches at `frame/design.md:29-41` and `:154`, `frame/plan.md:33`, `:49` and `:83`, and `changelog.md:3`; none names a wrong paragraph |
| `python3 skills/code-review/scripts/chain_check.py --baseline 5287dd42 --root <worktree> --worktree`, after this record was written | see the report: round 3's `open` verdict, no gate record and no guarantee |
