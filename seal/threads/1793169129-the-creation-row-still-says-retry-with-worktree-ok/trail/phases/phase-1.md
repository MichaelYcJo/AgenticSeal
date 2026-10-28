# Phase 1: 1793169129-the-creation-row-still-says-retry-with-worktree-ok

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | b1dfeee1 |

## What this phase was asked

Build the plan's one phase. Under the automation press, row 5's deny in
`hooks/worktree-guard.py` names no `[worktree-ok]` and asks for no
confirmation, in both languages. Attended, its text stays byte-identical to
the base. The pin in
`tests/hooks/test_worktree_guard.py#test_the_transcript_is_read_at_most_twice_per_creation`
and the stale comments are rewritten in place, as `frame/design.md` *Removes*
lists. Each scenario's case is seen red at `977b6613` before the code
changes.

The orchestrator settled two things for this phase. P1 of
`frame/questions.md` is built on its default (a), so row 2 is unchanged. W1
is decided here and recorded below. The two `change` items in `frame/design.md`
*Rule changes* belong to the settle, so this phase does not edit
`docs/worktree-guard-spec.md`. The phase edits only
`hooks/worktree-guard.py`, `tests/hooks/test_worktree_guard.py` and this work
item's records.

## What this phase found

**W1 is decided as its own function.** `switch_lines(git)` returns the three
`git switch` command lines, with no trailing newline. `steer_to_switch(git)`
returns `switch_lines(git)`, a blank line and the confirmation sentence, so
its output is unchanged for row 2, for row 3's attended fallback and for row
5 attended. Under the press, row 5 ends with `switch_lines(git)`, a blank
line, `press_sentence()` and `reissue_sentence()`. The flag was not taken,
because its `True` arm would have had one caller, and the name of a separate
function says what the pressed arm prints.

**The frame held against the tree.** Each coordinate it names in
`hooks/worktree-guard.py` and in the test file was opened and matched the
base `977b6613`. That covers rows 3 and 4's press read, `plain_origin`,
`press_sentence`, `reissue_sentence`, `steer_to_switch`'s callers and the
comment ranges *In* lists.

**One wording in the frame is loose, and the exact reason in *In* decides
it.** *Data & interfaces* says row 5 ends with "the switch command lines,
then `"\n\n"`, then" the press sentences. With `switch_lines` ending on its
last command line, that composition gives the reason *In* quotes word for
word: one blank line between the lines and the press sentence. The new
helper `single_stream_deny` in the test file builds that reason, and S1
compares against it whole.

**Row 5's press read is the third read site.** It sits after rows 1 to 4,
as the frame says, and reads `automation_pressed(repo_paths(cwd)[0], ...)`
as rows 3 and 4 do. S5's pin is now `[1, 2, 2, 2]`. No reading of any input
is new.

**S1 and S2 are one case.** `test_under_the_press_the_single_stream_row_names_no_token`
is parametrised over the parsed command and the command with an unbalanced
quote. It takes three attempts in each language for both commands. S2 asks
for two attempts, so three covers it.

**How each case was seen red.**

- S1 and S2 were run against the base hook before the code changed, with
  the hook file still equal to `977b6613`. Both were red: the reason ended
  with the confirmation sentence naming `[worktree-ok]`. For the unbalanced
  command the first line named `[worktree-ok]` too.
- S5 was red in the same run. It read `[1, 2, 1, 2]`.
- S3 was green at the base by design. After the code, it went red under
  `seal mutate` with row 5's press read forced to `True`.

**Mutation over each unit added.** One `seal mutate` batch ran five mutants
over the S1, S2, S3 and S5 cases, and all five went red:

- row 5's press forced to `True`;
- row 5's press forced to `False`;
- row 5's opening reduced to `origin` under the press;
- `press_sentence()` dropped from the pressed ending;
- the blank line after `switch_lines` in `steer_to_switch` cut to one newline.

The `origin` mutant survives S3 alone, as expected, because attended the
opening is `origin` either way. S1's unbalanced command is the case that
catches it.

**Comments rewritten in place.** These are the module docstring's creation
ladder and its *Under the press* paragraph, and the comment above `elsewhere`.
They also cover the comment above row 5's deny and the comment above
`plain_origin`. In the test file they are the docstrings of
`test_an_unbalanced_quote_under_the_press_names_no_token` and
`test_the_transcript_is_read_at_most_twice_per_creation`. The comment that
opened row 5's deny is now headed `5) Single stream`, in English. Rows 1 to 4
carry Korean headers, and this phase added no Korean comment.

**`git grep` for the old fact.** The search covered `rows 3 and 4`,
`names no token`, `plain_origin` and `steer_to_switch`, outside `seal/` and
the changelogs. It finds no other sentence in code or tests that says only
rows 3 and 4 drop the token. `docs/worktree-guard-spec.md` still states the
old fact at *B. Worktree creation* and *Choice sites*. `frame/design.md`
*Rule changes* carries both, and the settle writes them.

**No `.test_durations` key was added.** The three new node ids are unpriced.
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_durations_file_prices_the_suite`
tolerates a share of unpriced cases (read), and a duration written here
would be a number nobody measured on Windows. Whether the suite stays under
that share is a whole-suite reading, which `gaps.md` *Not verified* hands to
the orchestrator.
