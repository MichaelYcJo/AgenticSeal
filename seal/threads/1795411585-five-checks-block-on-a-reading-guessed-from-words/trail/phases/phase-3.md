# Phase 3: 1795411585-five-checks-block-on-a-reading-guessed-from-words

## What this phase found

**The frame holds against the tree at `2c0c21552`, and #1574 moved two of
its coordinates.** `git diff 22803718e 2c0c21552 --
skills/verify/scripts/pact_check.py` shows #1574's two hunks in
`near_headers` and `first_table`, which take one line from each function
(executed). The token units were not touched. At `2c0c21552` the docstring
paragraph stood at `:57-61`, the exit-2 item at `:117`, the comment at
`:241-247`, `INLINE_TOKEN` at `:248` and `INLINE` at `:271-278`, as
`frame/design.md` G5 gives them. The loop stood at `:811-814`, two lines
above G5's `:813-816` (read). In `tests/skills/test_pact_check.py`,
`INLINE` stood at `:108-115` as G5 gives it. The refusal case stood at
`:985-1016`, not G5's `:975-1007`, because #1574 added ids to the case
above it (read). The case went in phase 3's commit `ac46a0f10`.

**The docstring paragraph goes, and its one sentence opens the paragraph
above it.** `frame/design.md` *Scope* item 5 has the paragraph at `:57-61`
become one sentence: nothing outside the anchor table is read as an anchor.
The paragraph above it already opened with `Nothing else in a frame is read
as an anchor.` A second paragraph saying the same would state one fact
twice. So the token paragraph went whole, and the sentence above it now
reads `Nothing in a frame outside the anchor table is read as an anchor.`
That is *Scope* item 5's wording, and it matches the `to:` of the design's
first `## Rule changes` operation (judged against `frame/design.md` *Scope*
item 5 and `skills/core/SKILL.md` *The rule a mechanism is kept against*:
a fact has one source).

**Two comments that named the token went with it.** The comment over the
refusal sentences in `pact_check.py` named a row or a token, and the
matching comment in the test file named an anchor row and an inline
anchor. Each now names the row alone. G5 does not list either comment, and each stood on the
removed refusal (judged against `skills/core/SKILL.md` *The rule a
mechanism is kept against*: a change removes what stood on the old fact in
the same commit).

**The accepting case keeps its fence.** *Scope* item 5 removes that case's
token lines and sentences. The prose `The compact:x note...` went, and so
did the `pact:orders-api/...` line inside the fence. The fenced anchor table
and the fenced lower-case header stay, because the case's docstring still
says a table inside a closed fence is not read. The docstring's three token
clauses went: a token inside a fence, the word `compact:`, and a space
beside the colon.

**S7's case is `Test_check.test_accepts_a_pact_token_in_prose_as_no_anchor`.**
It writes S7's frame, a graded anchor row and the prose `Built against
pact:abc.`. It asserts exit 0, no `REFUSED` line, and a `READ` line that
counts one anchor. The `READ` count goes beyond S7's cell: it pins that the
token is not counted as an anchor, which is what the plan's
*Alternatives considered* row for `seal pact` relies on to show a person a
frame citing nothing. `bin/seal layout --pairs tests/skills/test_pact_check.py`
named no pair holding the new case, and `bin/seal layout --check` on the
file exited 0 (executed).

**Seen red (executed, at `2c0c21552` before the fix).** The case failed on
`assert 2 == 0`. Its output held a `REFUSED` line for the frame's line 5,
the token's line, in the removed `INLINE` sentence. The run was at `2c0c21552`, not at
`22803718e`, which the plan row names. As the first paragraph says, the
units it ran are the same bytes at both commits.

**Mutation (executed, one `bin/seal mutate` run, red).** The phase adds no
behaviour, so no run is owed (`skills/verify/SKILL.md` *The narrow command
still has to be able to fail*). One run checked that S7's case still
watches a token refusal at HEAD. It put a refusal of any frame holding
`pact:` back in `check`, ran the case with `-k
test_accepts_a_pact_token_in_prose_as_no_anchor`, and printed `red`. The
tree was clean after it.

**Searches 1 and 2 print what S10 states (executed after the fix).**
Search 1 printed `docs/layout/the-pact.md:110` alone. Search 2 printed
`docs/layout/the-pact.md:102` and `:109` alone. Before the fix, at
`2c0c21552`, search 1 also printed `pact_check.py:59`, `:241`, `:248`,
`:271`, `:812` and `:814` and `tests/skills/test_pact_check.py:108` and
`:1016`. Search 2 also printed `pact_check.py:57`, `:117`, `:242` and `:272`.
So each search could fail. `git grep -n -e refuses_the_inline_anchor -e
INLINE_TOKEN -- ':!seal/threads'` printed nothing (executed).

**Other statements of the rule across the tree (a sample).**
`git grep -n -i -e 'inline anchor' -e 'inline pact' -e 'pact: token' -e
'pact token'` and a search for the token followed by a non-space character,
outside `seal/threads/`, found `docs/layout/the-pact.md:102-117` alone
outside the two changed files. The design's `## Rule changes` owns that
section for the settle. `skills/code-review/SKILL.md:53-61` has the proofer
read a frame against `pact_check.py`'s *What each frame is read for*, and it
says a line written as an anchor outside that shape is a finding, because
`seal pact` reads it as no anchor. That holds unchanged, and it now covers a
token. `docs/running/what-a-script-gates.md:64` names no token (read). The
searches are by spelling, so a statement in other words is outside them.

**The phase boundary set (executed, one `bin/test -q` command).** It held
the plan row's two files and the test files that name `pact_check` or
`the-pact` (`tests/lib/test_config.py`, `tests/lib/test_tables.py` and
`tests/skills/test_seal.py`). The `tests/behaviour/` files that name them
ran inside that directory. It also held `tests/test_censuses.py` and the
two tree-wide directories, `tests/text` and `tests/behaviour`. Result: 2475
passed, 9 skipped. Its five warnings are citations that pending rule
changes of other work items excuse, none in a file this phase changed. The
rewrap commit `51a0ff390` came after this run and changes only a docstring.
Ruff passed on the file and the case it belongs to passed after it.
