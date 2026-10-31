# Review round 2: 1793408293-less-text-means-nothing-said-twice

target: 633792f2, fixes 4f15c508..633792f2

## Findings

No finding. The fix range changes `skills/core/SKILL.md` lines 107 to 109,
the fragment's lines 3 and 9, and round 1's `verdict:` and `answer:` lines
(`git diff 4f15c508..633792f2 --stat`, executed), and nothing in it holds a
defect this round found.

## Confirmations

confirms: round-1#1
The close holds. Claimed: the clause now states what a count is and asks no
party to produce one, in the proposed words, wrapped differently. Found:
`skills/core/SKILL.md:106-109` reads "a change that grows is kept where what
it adds serves a reader, and a count of the lines a change adds against
those it removes is context, never a criterion." (read at `633792f2`). The
clause's subject is the count and its verb is "is", so it says what a count
is where one is given. It names no act, so no crafter, proofer or sealer can
read a duty to produce one. The three parts *Scope* item 1 of
`frame/design.md` asks a rewording to keep are there: nothing said twice and
not fewer lines, a growing change kept where it serves a reader, and a
change's net count held as context only. The scope is the same one count, a
change's additions against its removals, so S2 still holds: `CAP`, the
`Stop` hook cap and the resumed crafter's token bound each bound what one
reader takes in, and the clause does not name them (read; the three
coordinates are carried from round 1). The fragment's *Changed* entry
(`changelog.md:3`) and process row (`changelog.md:9`) carry the same clause
(read), and `git grep` for "reported as context" or "held as a criterion"
finds the old clause in no shipped file, only in this work item's frame and
in round 1's quotes of it (executed). Lines 106 to 108 are 77, 75 and 71
columns, as the answer says (executed). The orchestrator's reading of lines
106 to 109 agrees with this one; this round reached it from the text.

confirms: none
The records state the shipped text consistently enough for the sealer at
HEAD, and no finding is opened on them. `frame/design.md:26` still quotes
the old clause, and `trail/phases/phase-1.md:9` still says the sentence is
*Scope* item 1 word for word. Both are true of what they describe: the
framer's proposed text, and the phase's build at `af0bdaff`. Neither says
what the tree holds after the fix. `frame/design.md:28` lets a builder
reword the sentence, keeping its three parts and its scope, and asks for the
new text and why in a phase record. A fix pass may not write a phase record
(`agents/crafter.md:164` in the installed plugin, read), so that sentence
cannot be met to the letter after review. Round 1's `answer:` line holds the
new clause verbatim and why it changed, and it stays in the tree until the
settle (read). It is also the one place among these records that
`seal pr-body` copies into the pull request body, since that command copies
each finding's labelled lines and copies no `frame/design.md` *Scope* text
and no phase record's prose (`skills/code-review/scripts/pr_body.py`
docstring, read). The settle carries nothing of *Scope* item 1 either: the
frame's `## Rule changes` is the no-change block (read). So the old clause
reaches no reader as the shipped text. A sealer who sets the frame's quote
beside the core finds a difference the frame itself allows, and round 1's
finding 1 explains it. Leaving the framer's record unedited is also what
the fix pass's writes allow.

confirms: none
S3 still holds after the fix. The enumeration command of `frame/design.md`
*Data & interfaces*, at `633792f2`, lists seventeen lines, exit 0
(executed): the frame's fifteen, unchanged, and `skills/core/SKILL.md:106`
(`fewer lines`) and `:107` ("a change that grows"). None holds a change's
added lines against its removed lines as a criterion.

confirms: none
S4 still holds. `hooks/lib/core.py#output` in the main clone at `633792f2`
returns 6,513 characters against `CAP` 10,000 (executed). That is 10 fewer
than round 1's 6,523, which matches the reworded clause being shorter.

Carried rather than re-established: the three limits' coordinates of S2
(`hooks/lib/core.py:41`, `docs/the-review-record.md:493`,
`skills/code-review/orchestration.md:30`), which the fix range does not
touch; the verdict on them was re-derived against the new clause. The
crafter's 45-module run was not re-run; this round ran the nine modules in
`## Probes`. Everything else here was opened or run again.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad suite, the repository-wide lint and `seal gate` at the branch's HEAD; the crafter's 45-module narrow run was not re-run beyond the nine modules in `## Probes` | `seal/threads/1793408293-less-text-means-nothing-said-twice/gaps.md:7` | the orchestrator, by `seal gate --base release/v0.25.2 --record 1793408293-less-text-means-nothing-said-twice` |

## Probes

| Command | Result |
|---|---|
| The enumeration command of `frame/design.md` *Data & interfaces*, in a `git clone --no-local` at `633792f2` under `<scratchpad>/1793408293-less-text-means-nothing-said-twice/round-2/` | 17 lines, the frame's fifteen and `skills/core/SKILL.md:106`, `:107`; exit 0 |
| `git grep -n -i -E 'reported as context\|held as a criterion'` at `633792f2` | `frame/design.md:26`, `:28`, `:45`, `frame/plan.md:9`, `:20` and round 1's quotes, all under this work item; no shipped file; exit 0 |
| `awk` printing the length of `skills/core/SKILL.md` lines 103 to 111 | 72, 72, 70, 77, 75, 71, 72, 74, 74 |
| `bin/test -q tests/hooks/test_core.py tests/behaviour/test_docs_line_wrap.py tests/github/test_publish_release_note.py tests/skills/test_pr_body.py tests/text/test_a_record_carries_no_comment.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_release_hygiene.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_the_rules_claude_md_names_have_one_home.py` in the clone | 212 passed, exit 0 |
| `python3 -I -c` calling `hooks/lib/core.py#output` with the main clone as both arguments | 6513 characters, `CAP` 10000 |
